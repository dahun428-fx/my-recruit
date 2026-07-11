# Portfolio Reference Index

This directory stores workflow guidance and source records for portfolio review.
It complements `docs/resume-reference/`; it does not replace the verified career
evidence kept there.

## Read Order

1. `README.md` - this index and usage rules.
2. `evaluation-rubric.md` - review criteria and severity levels.
3. `source-materials.md` - portfolio inputs and provenance.
4. `review-playbook.md` - agent handoff and output expectations.
5. `../resume-reference/ai-use-rules.md` - safe AI use rules.
6. `../resume-reference/ai-readable.yaml` - normalized experience IDs.
7. `../resume-reference/metric-registry.md` - allowed numeric claims.
8. `../resume-reference/profile.md` - stable candidate facts.
9. `../resume-reference/experience-bank.md` - verified project evidence.
10. `../resume-reference/source-log.md` - provenance for verified evidence.
11. `../../DESIGN.md` - required for HTML, PDF, and visual critique.

## Usage Rules

- Treat external portfolio files as read-only inputs unless the user explicitly
  asks to import or edit them.
- Verify concrete claims against the resume reference material before accepting
  them as true.
- Do not invent project dates, metrics, product names, roles, tools, or business
  outcomes.
- Separate factual findings from narrative or visual recommendations.
- Save final review reports under `outputs/` with a dated filename.

## Default Output

Use `outputs/portfolio-review-YYYY-MM-DD.md` for the synthesized review. If the
review needs intermediate artifacts, use names such as
`outputs/portfolio-inventory-YYYY-MM-DD.md`.
