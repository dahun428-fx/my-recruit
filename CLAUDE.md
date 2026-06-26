# CLAUDE.md

This file provides Claude Code-specific guidance for working in this repository.
Follow `AGENTS.md` first for the canonical project rules shared by all agents.

## Claude Code Scope

Use this file only for Claude-specific behavior, tooling, and skills. Shared
project rules such as repository layout, beads usage, git safety, and shell
behavior belong in `AGENTS.md`.

## Codex Ping-Pong (output quality loop)

Codex CLI is registered as a local MCP server (`codex` via
`codex mcp-server`). Use it as an independent second model to review and harden
non-trivial output. Codex should generate or verify what Claude did not, helping
catch same-model blind spots.

For any substantive task (code, design, important docs), run this loop:

1. Claude produces a draft.
2. Send the actual artifact (full code/diff, not a summary) to Codex with an
   adversarial prompt: "find bugs, edge cases, and weaknesses only - no praise."
3. Triage each point as accept / reject (with reason) / defer. Do not blindly
   follow Codex; push back on wrong critiques and show the reasoning.
4. Apply accepted fixes, send back for another pass.
5. Stop when Codex returns no new critical issues twice, or after 3 rounds.

Each round, show the user what Codex raised and what was accepted vs. rejected.
Skip the loop only for trivial or mechanical edits.

## Agent Team

Six specialist subagents live in `.claude/agents/` (`archivist`, `writer`,
`tailor`, `reviewer`, `ats`, `designer`). Dispatch them with the agent/Task
tool. The **canonical roster, file ownership, and handoff order live in
`AGENTS.md`** — do not duplicate them here.

Claude-specific notes:

- The critics `reviewer` and `ats` are **read-only** (no `Write`/`Edit`); they
  report findings instead of editing drafts.
- `reviewer` is a same-model pass and **complements** the Codex ping-pong loop
  above; run Codex as the independent-model hardening pass after `reviewer`.

## Project Skills

Imported from `dahun428-fx/my-item-skill` into `.claude/skills/`:

- `commit-writer`: write concise commit messages from scoped diffs.
- `secret-scan`: check changes for hardcoded credentials before committing or
  sharing.
- `troubleshooting-harness`: turn recurring failures into
  `docs/troubleshooting/` writeups.

Intentionally not imported:

- `health-line-chart`: specific to health chart UI work.
- `safe-push`: useful globally, but risky here because the git root is
  `C:\workspaces2` and includes unrelated sibling projects.
- `monthly-feedback`: performance/KPI reporting is not needed for this
  resume/CV project.
- `project-templates/danaadata-toolkit`: assumes a
  React/GitLab/multi-tenant SaaS structure that this repository does not
  currently have.
