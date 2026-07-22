# CLAUDE.md

This file provides Claude Code-specific guidance for working in this repository.
Follow `AGENTS.md` first for the canonical project rules shared by all agents.

## Claude Code Scope

Use this file only for Claude-specific behavior, tooling, and skills. Shared
project rules such as repository layout, beads usage, git safety, and shell
behavior belong in `AGENTS.md`.

## Adversarial Verification (Claude subagent hardening loop)

Harden non-trivial output with an **independent Claude subagent** review pass
instead of an external model. Dispatch a fresh subagent (the read-only
`reviewer` for resume drafts, or a `general-purpose` subagent for other
artifacts) that has not seen the drafting conversation, so it reviews the
artifact cold and catches blind spots.

For any substantive task (code, design, important docs), run this loop:

1. Claude produces a draft.
2. Dispatch a Claude subagent with the actual artifact (full code/diff, not a
   summary) and an adversarial prompt: "find bugs, edge cases, and weaknesses
   only - no praise."
3. Triage each point as accept / reject (with reason) / defer. Do not blindly
   follow the subagent; push back on wrong critiques and show the reasoning.
4. Apply accepted fixes, then dispatch another review pass.
5. Stop when the subagent returns no new critical issues twice, or after 3
   rounds.

Each round, show the user what the subagent raised and what was accepted vs.
rejected. Skip the loop only for trivial or mechanical edits.

## Feedback Rule Capture (선호 축적 루프)

Owner feedback accumulates into two approval-gated ledgers:

- **Output style** (wording, tone, content emphasis, structure) →
  `docs/resume-reference/feedback-rules.md`. Capture runs during any
  resume/CV writing or revision session. Categories 어투/문장/내용/구조,
  soft cap ~30 active.
- **Process** (how the AI works: reporting, procedure, delegation,
  confirmation) → `docs/harness-reference/process-rules.md`. Capture runs in
  **every** session. Categories 보고/절차/위임/확인, soft cap 15 active,
  probation → active lifecycle. Its rules are imported below, so they are
  always in context.

Shared capture loop for both ledgers:

1. When the user gives corrective feedback, apply the fix first.
2. Propose a one-line rule candidate (category + strength MUST/NEVER/PREFER +
   generalized sentence) only when the feedback is **generalizable and
   durable**: for style, a pattern rather than a one-off typo or a
   company-specific targeting call; for process, persistence wording
   ("앞으로는/항상/매번") or the same correction recurring twice — first
   sightings without persistence wording go to the process ledger's
   관찰 로그, not into a rule. One-off instructions ("이번엔 짧게") are
   never ledgered. Ask for approval.
3. Record **only approved** candidates, following each ledger's header rules
   (generalize-over-add, contradiction check, soft caps). Approved style
   rules become `active`; approved process rules start at `probation`.
4. Before ending a substantive session, sweep for **eligible** (durable,
   generalizable per step 2) feedback that was applied but not yet proposed
   and propose leftovers in one batch — first-sighting process corrections
   are logged to the 관찰 로그, one-offs are ignored. Also self-check the
   session against active/probation process rules (fix violations before the
   final response; report unfixable ones), log `적용` history on any
   probation rule that was exercised (operational metadata, no approval
   needed, per the ledger's counting rules), and propose
   promotions/retirements that fall out of that check.

Routing table — where a piece of feedback belongs. Mixed feedback is split
into separate candidates, one per destination — never forced into one bucket:

| Feedback about | Destination |
| --- | --- |
| Wording/tone/content/structure of output documents | `docs/resume-reference/feedback-rules.md` |
| How the AI works (reporting, procedure, delegation, confirmation) — including durable preferences about how to handle/report failures | `docs/harness-reference/process-rules.md` |
| Visual/layout | `DESIGN.md` (+ one-line pointer in the style ledger) |
| Company-specific targeting calls | `docs/resume-reference/target-companies.md` |
| Tooling failure incidents (repro, root cause, recovery writeups) | `docs/troubleshooting/` |
| Behavior the harness itself must guarantee every time (the model cannot be trusted to remember) | settings.json hooks via the `update-config` skill; preference-shaped candidates go through the process ledger first and escalate per its header |

## Process Rules (작업 방식 규칙)

The process ledger is imported here so its active/probation rules are in
context every session:

@docs/harness-reference/process-rules.md

## Agent Team

Specialist subagents live in `.claude/agents/` (`archivist`, `writer`,
`tailor`, `reviewer`, `ats`, `recruiter-screen`, `tech-screen`, `designer`).
Dispatch them with the agent/Task tool. The **canonical roster, file ownership,
and handoff order live in `AGENTS.md`** — do not duplicate them here.

Claude-specific notes:

- The critics `reviewer` and `ats` are **read-only** (no `Write`/`Edit`); they
  report findings instead of editing drafts.
- `recruiter-screen` (인사담당자) and `tech-screen` (기술담당자) are read-only
  **score graders** that gate the pipeline: after `reviewer`/`ats` fixes, run
  both in parallel and treat the draft as final only when **both** return
  `PASS` (each ≥ 80, no blockers). On `FAIL`, have `writer`/`tailor` fix the
  blockers and re-score, up to 3 rounds; if still failing, report scores and
  stop rather than shipping a sub-threshold draft. See the **Score gate** in
  `AGENTS.md` for the canonical rule.
- `reviewer` is a same-model pass and **complements** the adversarial
  verification loop above; run a fresh Claude subagent hardening pass after
  `reviewer`.

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
- For substantive portfolio reports or rewrites, run the adversarial
  verification loop (a fresh Claude subagent) after synthesis, using the
  read-only critics plus `portfolio-synthesizer` as the hardening path.

## Project Skills

Project-native:

- `resume-engine`: 새 회사 이력서 재조립 엔진 드라이버 (자동 2-스톱 /
  인터뷰 모드, 갭 인터뷰). 정본 흐름은 `AGENTS.md`의 Resume Engine 섹션.

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
