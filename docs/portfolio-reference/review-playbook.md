# Portfolio Review Playbook

Use this workflow when reviewing a portfolio artifact.

## Handoff Order

1. `portfolio-curator`
   - Reads the portfolio files and source-material record.
   - Produces an inventory of pages, projects, assets, and concrete claims.
2. `portfolio-fact-checker`
   - Read-only.
   - Verifies claims against `docs/resume-reference/`.
3. `portfolio-story-reviewer`
   - Read-only.
   - Reviews recruiter-facing narrative, project selection, and positioning.
4. `portfolio-ux-reviewer`
   - Read-only.
   - Reviews HTML/PDF layout, hierarchy, accessibility, and print fit.
5. `portfolio-synthesizer`
   - Merges the critiques into a prioritized final report under `outputs/`.

## Report Requirements

The final report must include:

- Executive verdict: ready, usable with fixes, or not ready.
- Must-fix items.
- Should-fix items.
- Could-improve items.
- Unsupported claims and the evidence needed to resolve them.
- Suggested next work order.

## Hard Rules

- Do not rewrite the portfolio during review unless the user explicitly asks.
- Do not alter verified reference files while reviewing a portfolio.
- Do not recommend adding skills, metrics, or outcomes unless they exist in the
  verified evidence base or are clearly marked as needing confirmation.
