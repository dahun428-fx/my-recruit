# Agent Instructions

This file is the canonical project guidance for all coding agents working in
`my-recruit`.

## Purpose

`my-recruit` is a project for managing the owner's resume / CV.

## Repository Layout

`my-recruit` is **not** its own git repository. The git root is the parent
directory `C:\workspaces2`, which also tracks unrelated sibling projects
(`bizcare`, `my-fortune`, `my-health-ai-coach-web`, etc.).

- `git status` / `git log` here reflect the **entire** workspace. Scope git
  commands to this directory, for example `git status -- .`.
- Do not stage or commit changes from sibling projects.
- Do not auto-push from this project. Ask before push or commit workflows.

## Beads Issue Tracker

This project uses **bd (beads)** for local issue tracking. Run `bd prime` for
full workflow context.

> **Architecture in one line:** Issues live in a local Dolt database
> (`.beads/dolt/`); cross-machine sync uses `bd dolt push/pull` (a
> git-compatible protocol), stored under `refs/dolt/data` on your git remote,
> separate from `refs/heads/*` where code lives. `.beads/issues.jsonl` is a
> passive export, not the wire protocol.
>
> See [SYNC_CONCEPTS.md](https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md)
> for the one-screen overview and anti-patterns: do not treat JSONL as the
> source of truth, do not run `bd import` during normal operation, and do not
> reach for third-party Dolt hosting before trying the default.

Quick commands:

```bash
bd prime
bd ready
bd show <id>
bd update <id> --claim
bd close <id>
```

Project rules:

- Use beads for project task tracking when an issue/task record is useful.
- If `bd` is not found in a new shell, use
  `C:\Users\jungdahun\AppData\Local\Programs\bd\bd.exe` or reopen the terminal
  after PATH refresh.

## Non-Interactive Shell Commands

Always use non-interactive flags with file operations to avoid hanging on
confirmation prompts.

Shell commands like `cp`, `mv`, and `rm` may be aliased to include `-i`
(interactive) mode on some systems, causing the agent to hang indefinitely
waiting for y/n input.

Use these forms instead:

```bash
# Force overwrite without prompting
cp -f source dest           # NOT: cp source dest
mv -f source dest           # NOT: mv source dest
rm -f file                  # NOT: rm file

# For recursive operations
rm -rf directory            # NOT: rm -r directory
cp -rf source dest          # NOT: cp -r source dest
```

Other commands that may prompt:

- `scp` - use `-o BatchMode=yes` for non-interactive
- `ssh` - use `-o BatchMode=yes` to fail instead of prompting
- `apt-get` - use `-y` flag
- `brew` - use `HOMEBREW_NO_AUTO_UPDATE=1` env var

## Cross-Agent Review

Use `scripts/claude_review.py` when a Codex session needs an independent Claude
review pass. The default input is scoped to this project with `git diff -- .`.

Examples:

```bash
.\.venv\Scripts\python.exe scripts\claude_review.py
.\.venv\Scripts\python.exe scripts\claude_review.py --files AGENTS.md CLAUDE.md
.\.venv\Scripts\python.exe scripts\claude_review.py --staged
```

## Agent Team

This project uses a team of six specialist subagents defined in
`.claude/agents/`. Each maps to one stage of the resume workflow and owns a
narrow set of files. **Critics are read-only** (no `Write`/`Edit`); producers
write only within their owned files. Dispatch them via the agent/Task tool.

| Agent | Role | Owns / writes | Access |
| --- | --- | --- | --- |
| `archivist` | Ingest raw sources; extract verified facts | `experience-bank.md`, `source-materials.md`, `source-log.md` | read-write |
| `writer` | Draft resume / cover letter / self-intro | drafts in `outputs/` | read-write |
| `tailor` | Adapt a draft to a specific job posting | `target-companies.md` notes, variants in `outputs/` | read-write |
| `reviewer` | Fact-check vs evidence base; guideline critique | — (reports findings) | **read-only** |
| `ats` | Keyword-coverage check vs a JD | — (reports findings) | **read-only** |
| `designer` | Render visual / print artifacts | artifacts in `outputs/` | read-write |

Producers must follow the no-fabrication rule in
`docs/resume-reference/writing-guidelines.md`: use only verified facts from
`profile.md` and `experience-bank.md`, and mark missing evidence with a
`[확인 필요]` placeholder rather than inventing it. The `designer` follows
`DESIGN.md` and must not alter prose.

Producers (`writer`, `tailor`) must also follow the owner's personal style
ledger `docs/resume-reference/feedback-rules.md`. On conflict with
`writing-guidelines.md`, the ledger's active rules win (no-fabrication always
stays supreme). `reviewer` audits drafts against every active `MUST`/`NEVER`
ledger rule and reports violations by rule ID; `PREFER` deviations are
reported as questions, not blockers. The ledger's own header defines how rules
are captured, generalized, toggled (`active`/`retired`), and capped.

### Handoff playbook

```
archivist  → build / refresh the evidence base
   ↓
writer     → draft from the bank
   ↓
tailor     → produce a JD-specific variant
   ↓
reviewer + ats  → parallel read-only critique
   ↓
(writer / tailor revise)
   ↓
designer   → render the final visual artifact
```

`reviewer` is a same-model fact/guideline pass. It **complements, not replaces**,
the independent-model Codex ping-pong loop (see `CLAUDE.md`), which should run as
a final hardening pass after `reviewer`.

## Portfolio Review Harness

Portfolio work is a first-class workflow, separate from the resume drafting
pipeline above. Use it when reviewing or improving portfolio HTML, PDF, image
assets, project case studies, or portfolio summaries.

The portfolio harness uses specialist subagents in `.claude/agents/`:

| Agent | Role | Owns / writes | Access |
| --- | --- | --- | --- |
| `portfolio-curator` | Inventory portfolio files and extract project claims | review inventory in `outputs/` | read-write |
| `portfolio-fact-checker` | Verify claims against the evidence base | -- (reports findings) | **read-only** |
| `portfolio-story-reviewer` | Critique recruiter-facing project narrative | -- (reports findings) | **read-only** |
| `portfolio-ux-reviewer` | Critique HTML/PDF layout, visual hierarchy, accessibility, print fit | -- (reports findings) | **read-only** |
| `portfolio-synthesizer` | Combine findings into prioritized feedback | final review report in `outputs/` | read-write |

Portfolio source files outside this repository are read-only inputs unless the
user explicitly asks to import or edit them. Record the path and file list in
`docs/portfolio-reference/source-materials.md` before review.

Portfolio agents must follow the same no-fabrication rule as resume agents: use
only verified facts from `docs/resume-reference/profile.md`,
`docs/resume-reference/experience-bank.md`, and
`docs/resume-reference/metric-registry.md`. Unsupported claims are findings, not
permission to rewrite history.

### Portfolio handoff playbook

```
portfolio-curator
   -> portfolio-fact-checker + portfolio-story-reviewer + portfolio-ux-reviewer
   -> portfolio-synthesizer
   -> Claude/Codex hardening pass when the output is substantive
```

Default portfolio review reports go under `outputs/` using a dated name such as
`portfolio-review-YYYY-MM-DD.md`. Keep raw extracted claims, critique notes, and
final recommendations separate enough that a later agent can trace feedback back
to the source file and evidence record.

## Cloud / Mobile Sessions (claude.ai/code)

This project can be run from the Claude mobile app via Claude Code in the cloud
(`claude.ai/code`) against the standalone **private** GitHub repo. The cloud
sandbox clones the repo, so the six subagents in `.claude/agents/` and the
project skills run there unchanged. The following rules apply **only** to cloud /
mobile sessions, where the local PC toolchain is absent:

- **Skip the Codex ping-pong loop.** The `codex` MCP server is not available in
  the cloud sandbox. Use the `reviewer` subagent as the (same-model) hardening
  pass instead. The Codex independent-model pass resumes on the PC.
- **No beads.** The Dolt database lives under `refs/dolt/data` and does not
  follow the clone, so `bd` commands will not work. Do issue tracking on the PC.
- **Deliverables as Markdown.** Save drafts to `outputs/*.md` and show the full
  text in the chat. Print-ready PDF/HTML via the `designer` agent stays a
  PC-side step (it needs the local render toolchain).
- **Write back via branch / PR, never push to `main` directly.** Commit cloud
  work to a feature branch and open a PR; the PC syncs with `git pull` / merge.
- **Raw source binaries are absent by design.** `docs/resume-reference/sources/`
  (résumé PDF, salary / appraisal xlsx) is gitignored and will not be in the
  clone. Work from the derived `*.md` / `*.yaml`; do not attempt re-extraction
  from raw sources in the cloud.

## Resume Reference Material

Before drafting or editing a resume, cover letter, self-introduction, or
job-specific application document, read the reference files under
`docs/resume-reference/` in this order:

1. `README.md`
2. `ai-use-rules.md`
3. `ai-readable.yaml`
4. `metric-registry.md`
5. `profile.md`
6. `experience-bank.md`
7. `writing-guidelines.md`
8. `feedback-rules.md`
9. `target-companies.md`
10. `source-materials.md`
11. `source-log.md`

Also read `DESIGN.md` before creating visual or print-ready artifacts.
