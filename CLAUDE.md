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

## Feedback Rule Capture (선호 축적 루프)

`docs/resume-reference/feedback-rules.md` is the owner's personal style
ledger. During any resume/CV writing or revision session, run this capture
loop:

1. When the user gives corrective feedback on wording, tone, content
   emphasis, or structure, apply the fix first.
2. If the feedback is **generalizable** (a pattern, not a one-off typo or a
   company-specific targeting call), immediately propose a one-line rule
   candidate: category (어투/문장/내용/구조) + strength (MUST/NEVER/PREFER) +
   generalized rule sentence. Ask for approval.
3. Record **only approved** candidates in the ledger, following its header
   rules (generalize-over-add, contradiction check, soft cap ~30 active).
4. Before ending a substantive writing session, sweep for feedback that was
   applied but not yet proposed as a rule, and propose the leftovers in one
   batch.

Do not propose a rule for every edit — only when a durable preference is
visible. Visual/layout feedback goes to `DESIGN.md` (leave a one-line pointer
in the ledger); tooling failures go to `docs/troubleshooting/`.

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

Portfolio review has its own subagent harness, also defined in
`.claude/agents/`: `portfolio-curator`, `portfolio-fact-checker`,
`portfolio-story-reviewer`, `portfolio-ux-reviewer`, and
`portfolio-synthesizer`. The canonical roster and handoff order live in
`AGENTS.md`.

Claude-specific portfolio notes:

- Run `portfolio-curator` first so every critic reviews the same inventory of
  files, projects, and claims.
- Run `portfolio-fact-checker`, `portfolio-story-reviewer`, and
  `portfolio-ux-reviewer` as independent read-only critiques when possible.
- Have `portfolio-synthesizer` merge the findings into one prioritized report in
  `outputs/`.
- For substantive portfolio reports or rewrites, run the Codex ping-pong loop
  after synthesis. If the cloud/mobile session cannot use Codex, state that and
  use the read-only critics plus `portfolio-synthesizer` as the local hardening
  path.

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
