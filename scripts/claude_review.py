"""Ask Claude Code to review an artifact through claude-agent-sdk.

Default input is the scoped git diff for this project (`git diff -- .`), which
matters because this directory is inside a larger git workspace.
"""

from __future__ import annotations

import argparse
import asyncio
import re
import subprocess
import sys
from pathlib import Path

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ResultMessage,
    TextBlock,
    query,
)


DEFAULT_REVIEW_PROMPT = (
    "Find bugs, edge cases, incorrect assumptions, and weaknesses only. "
    "Do not praise the work. Be concise and include concrete file references "
    "when possible."
)


def run_git_diff(cwd: Path, staged: bool) -> str:
    command = ["git", "diff"]
    if staged:
        command.append("--staged")
    command.extend(["--", "."])

    result = subprocess.run(
        command,
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git diff failed")
    return result.stdout


def read_files(paths: list[str], cwd: Path, max_chars: int) -> str:
    chunks: list[str] = []
    total_chars = 0
    for raw_path in paths:
        raw = Path(raw_path)
        path = raw.resolve() if raw.is_absolute() else (cwd / raw).resolve()
        try:
            path.relative_to(cwd.resolve())
        except ValueError as exc:
            raise ValueError(f"Refusing to read outside project: {raw_path}") from exc
        if not path.is_file():
            raise ValueError(f"Not a regular file: {raw_path}")
        text = path.read_text(encoding="utf-8", errors="replace")
        total_chars += len(text)
        if total_chars > max_chars:
            raise ValueError(
                f"selected files exceed --max-artifact-chars ({max_chars})"
            )
        chunks.append(f"--- FILE: {raw_path} ---\n{text}")
    return "\n\n".join(chunks)


def build_prompt(review_prompt: str, artifact: str) -> str:
    longest_backtick_run = max((len(match.group(0)) for match in re.finditer(r"`+", artifact)), default=0)
    fence = "`" * max(4, longest_backtick_run + 1)
    return (
        f"{review_prompt}\n\n"
        "Review this artifact:\n\n"
        f"{fence}text\n"
        f"{artifact}\n"
        f"{fence}"
    )


def extract_text(message: AssistantMessage) -> list[str]:
    output: list[str] = []
    for block in message.content:
        if isinstance(block, TextBlock):
            output.append(block.text)
    return output


def print_text(text: str, *, stderr: bool = False) -> None:
    stream = sys.stderr if stderr else sys.stdout
    try:
        print(text, file=stream)
    except UnicodeEncodeError:
        safe_text = text.encode(stream.encoding or "utf-8", errors="replace").decode(
            stream.encoding or "utf-8",
            errors="replace",
        )
        if hasattr(stream, "buffer"):
            stream.buffer.write(safe_text.encode(stream.encoding or "utf-8") + b"\n")
        else:
            stream.write(safe_text + "\n")


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


async def ask_claude(
    args: argparse.Namespace,
    prompt: str,
    cwd: Path,
) -> tuple[list[str], str | None]:
    options = ClaudeAgentOptions(
        cwd=str(cwd),
        allowed_tools=[],
        disallowed_tools=["Bash", "Read", "Write", "Edit", "Glob", "Grep"],
        max_turns=args.max_turns,
        max_budget_usd=args.max_budget_usd,
        setting_sources=[],
        model=args.model,
    )

    responses: list[str] = []
    result_subtype: str | None = None
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, AssistantMessage):
            responses.extend(extract_text(message))
        elif isinstance(message, ResultMessage):
            result_subtype = message.subtype
    return responses, result_subtype


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Send a scoped diff or selected files to Claude for review."
    )
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument(
        "--files",
        nargs="+",
        help="Project-relative files to review instead of git diff.",
    )
    input_group.add_argument(
        "--text",
        help="Literal text to review instead of git diff.",
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help="Review staged changes with git diff --staged -- .",
    )
    parser.add_argument(
        "--review-prompt",
        default=DEFAULT_REVIEW_PROMPT,
        help="Reviewer instruction sent before the artifact.",
    )
    parser.add_argument(
        "--cwd",
        default=str(Path.cwd()),
        help="Project directory. Defaults to the current directory.",
    )
    parser.add_argument(
        "--max-turns",
        type=int,
        default=1,
        help="Maximum Claude turns.",
    )
    parser.add_argument(
        "--max-budget-usd",
        type=float,
        default=None,
        help="Optional Claude SDK budget cap.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Optional Claude model override.",
    )
    parser.add_argument(
        "--max-artifact-chars",
        type=int,
        default=200_000,
        help="Fail before calling Claude if the artifact is larger than this.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the prompt that would be sent without calling Claude.",
    )
    return parser.parse_args()


def main() -> int:
    configure_stdio()
    args = parse_args()
    cwd = Path(args.cwd).resolve()

    if args.staged and (args.files or args.text is not None):
        print_text("error: --staged only applies when reviewing git diff input.", stderr=True)
        return 2

    try:
        if args.files:
            artifact = read_files(args.files, cwd, args.max_artifact_chars)
        elif args.text is not None:
            artifact = args.text
        else:
            artifact = run_git_diff(cwd, args.staged)
    except Exception as exc:
        print_text(f"error: {type(exc).__name__}: {exc}", stderr=True)
        return 2

    if not artifact.strip():
        print_text("No artifact content to review.", stderr=True)
        return 1
    if len(artifact) > args.max_artifact_chars:
        print_text(
            f"error: artifact is {len(artifact)} chars, above --max-artifact-chars "
            f"({args.max_artifact_chars}). Review smaller files or raise the limit.",
            stderr=True,
        )
        return 2

    prompt = build_prompt(args.review_prompt, artifact)
    if args.dry_run:
        print_text(prompt)
        return 0

    try:
        responses, result_subtype = asyncio.run(ask_claude(args, prompt, cwd))
    except Exception as exc:
        print_text(f"error: Claude review failed: {type(exc).__name__}: {exc}", stderr=True)
        return 3

    if responses:
        print_text("\n\n".join(responses))
    else:
        if result_subtype is None:
            detail = "without assistant text or result status"
        else:
            detail = f"with result status {result_subtype!r} but no assistant text"
        print_text(f"error: Claude review ended {detail}.", stderr=True)
        return 3
    if result_subtype and result_subtype != "success":
        print_text(f"\n[claude result: {result_subtype}]", stderr=True)
        return 4
    return 0 if responses else 1


if __name__ == "__main__":
    raise SystemExit(main())
