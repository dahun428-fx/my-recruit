# Resume Reference Index

This directory stores source material that agents should read before drafting or
editing resumes, cover letters, self-introductions, and job-specific application
documents.

## Read Order

1. `ai-use-rules.md` - rules for safe AI use of the reference material.
2. `ai-readable.yaml` - normalized candidate, career, experience, and source
   IDs for AI drafting.
3. `metric-registry.md` - status and safe wording for numeric claims.
4. `profile.md` - stable candidate facts, positioning, and constraints.
5. `experience-bank.md` - reusable project and achievement evidence.
6. `writing-guidelines.md` - writing rules for Korean resume / cover-letter
   work.
7. `feedback-rules.md` - the owner's personal style ledger; active rules
   override `writing-guidelines.md` on conflict.
8. `target-companies.md` - company- or role-specific notes.
9. `source-materials.md` - imported source files and extraction notes.
10. `source-log.md` - provenance for facts added to this reference set.

Read `../../DESIGN.md` before creating visual, HTML, PDF, or print-ready
artifacts. It is optional for plain-text drafting or analysis tasks.

## Usage Rules

- Treat these files as reference material, not final copy.
- Do not invent facts, employers, dates, metrics, certifications, or education.
- If a required fact is missing, leave a clear placeholder or ask for it.
- For AI drafting, prefer `ai-readable.yaml` and `metric-registry.md` before
  reading long extracted source files.
- Prefer concrete evidence from `experience-bank.md` over generic claims.
- When tailoring to a company, use `target-companies.md` plus the job posting
  supplied in the current task.
- If target-company notes conflict with `profile.md` constraints, `profile.md`
  wins unless the user explicitly confirms a change.
- Keep finished application documents outside this directory, preferably under
  `outputs/` or another task-specific delivery directory.

## Maintenance

Update these files whenever new validated information appears in a chat,
document, portfolio, or application draft. Also add a row to `source-log.md`
describing where the information came from and which files changed.

Exception: `feedback-rules.md` is updated only through its propose-then-approve
capture process (see its header) by the top-level agent; producer subagents
never edit it.

Keep raw facts and polished phrasing separate so future drafts can be tailored
without losing the source evidence.
