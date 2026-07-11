# Portfolio Review - 2026-06-28

## Executive Verdict

**Usable with fixes.** The portfolio is clean, readable, and mostly fact-safe,
but it currently undersells the candidate. It describes products and features
more strongly than it proves engineering ownership, measurable impact, and role
fit. Before using it for applications, fix the scanability and evidence density
issues below.

Review limitation: I inspected the HTML, CSS, and embedded PNG assets directly.
The PDF file exists, but this shell does not have `pdftotext`, `pdfinfo`, or an
image renderer such as ImageMagick installed, so PDF-specific conclusions should
be treated as CSS-based risk assessment until the PDF is visually checked.

Inputs reviewed:

- `C:\Users\jungdahun\Documents\Codex\2026-06-24\new-chat-4\outputs\portfolio.html`
- `portfolio.css`
- `portfolio.pdf` presence only; PDF extraction tool was unavailable
- `portfolio-assets/portfolio-aicoach-chat-custom.png`
- `portfolio-assets/portfolio-biz365-custom.png`
- `portfolio-assets/portfolio-bioage-custom.png`
- `docs/resume-reference/profile.md`
- `docs/resume-reference/experience-bank.md`
- `docs/resume-reference/metric-registry.md`
- `docs/resume-reference/source-log.md`

## Must-Fix Items

### 1. Add project-level ownership metadata

- Location: all pages, project headers.
- Problem: Each page has a product title and short headline, but no project
  period, role, tech stack, team scope, or ownership boundary. A recruiter has
  to infer whether this was frontend-only, full-stack, lead role, support role,
  or maintenance work.
- Recommended fix: Add a compact metadata row under each headline:
  `기간 / 역할 / 핵심 기술 / 담당 범위`.
- Evidence source:
  - AI코치: `experience-bank.md` `AI 건강검진 챗봇 제품화 및 플랫폼 확장`
  - 비즈 36.5: `experience-bank.md` `B2B 임직원 건강 플랫폼 풀스택 내재화`
  - 바이오에이지: extracted 2025/2026 evaluation evidence around BioAge
    UI/report operations.

### 2. Separate service description from personal contribution

- Location: all `서비스 소개` and `개발사항` sections.
- Problem: The portfolio spends much of the first scan explaining what the
  service does. The candidate's engineering contribution appears later and in
  softer language. For a hiring reader, this delays the main signal.
- Recommended fix: Add a short `내 역할` or `Contribution Summary` block near the
  top of each page, before or beside the feature list. Use one sentence with
  problem, action, and result.

### 3. Tighten the broad QA/operations claim

- Location: Page 2, `개발사항`.
- Claim: "주요 사용자 흐름과 화면 변경 영향 범위를 기준으로 확인 절차를 정리해 운영 및 QA 시간을 줄였습니다."
- Problem: This implies measurable operational/QA reduction, but the page does
  not give a metric or direct evidence thread. The evidence base has QA
  automation metrics, but those are broader FE AX/operations evidence and should
  not be casually attached to this B2B page unless the scope is made explicit.
- Recommended fix: Either rephrase to the non-metric claim
  `확인 절차를 정리해 운영 대응 기준을 명확히 했습니다`, or add a verified metric
  with source-safe wording if this page is meant to include the FE AX thread.

### 4. Strengthen measurable impact where the registry already allows it

- Location: all pages.
- Problem: The portfolio avoids most metrics. That keeps it safe, but weakens
  credibility because the evidence base has usable metrics.
- Recommended fix:
  - AI코치: add `답변 출력 10초 -> 4초` if the page can spare one line; status
    is `confirmed`.
  - 비즈 36.5: keep `108페이지 / 82화면`; status is `source_stated`. Add `9주 내`
    only if wording stays close to the registry.
  - 바이오에이지: consider `기존 고객 112처 중 93처 안정 전환`; status is
    `source_stated`.
- Do not add:
  - 만족도 점수 without confirming survey scope.
  - 400건 정상 출력률 without scope note.
  - 매출 기여 unless the total/breakdown caveat is handled.

## Should-Fix Items

### 5. AI코치 page is strongest, but still hides architecture depth

- Location: Page 1.
- Current strength: SSE streaming, API response handling, rendering flow,
  responsive UI, exception cases are all supported by the evidence base.
- Problem: The page does not mention the deeper differentiators already in the
  evidence base: Markdown renderer, XSS filtering, answer stop/retry/error
  states, Config-Driven UI, Base-Theme.
- Recommended fix: Replace one generic dev bullet with an architecture bullet:
  `SSE, Markdown 렌더링, 오류 상태, XSS 필터링을 포함한 AI 응답 렌더링 가드레일을 정리했다.`

### 6. 비즈 36.5 screenshot does not prove the written claim

- Location: Page 2 image.
- Problem: The image is visually polished but mostly shows a public/hero screen.
  It does not show customer-specific branding, menu/permission structure,
  Web/Admin/App integration, or the 108-page/82-screen migration.
- Recommended fix: First inspect the unused bundled `biz365-public.png` asset.
  If it does not show stronger contribution evidence, use or add a second image
  crop that shows navigation, customer-specific menu/branding, admin/settings,
  or before/after structure. If sensitive, use annotated masked wireframe blocks.

### 7. 바이오에이지 page needs sharper scope boundaries

- Location: Page 3.
- Problem: The copy mixes product explanation, report UI work, customer
  transition, DB/API/PDF troubleshooting, and operation stabilization. These are
  valid evidence threads, but the reader cannot see which was the main project.
- Recommended fix: Choose one lead angle:
  - Use `리포트 UI 내재화 및 운영 안정화` if the page should rely on 2025 annual
    evaluation evidence.
  - Use `리포트 누락 이슈 대응 체계와 고객 전환 안정화` if the page should rely on
    2026 H1 evidence.
  Then keep the other as a supporting bullet. The 2026 H1 angle is stronger for
  technical troubleshooting; the 2025 angle is stronger for business/operations
  continuity.

### 8. The portfolio needs a compact overview signal

- Location: document start.
- Problem: Page 1 immediately starts with Project 01. There is no top-level
  positioning such as `헬스케어 AI/B2B 플랫폼 포트폴리오` and the candidate's
  verified target role. This makes the first read project-heavy but
  candidate-light.
- Recommended fix: Add a compact Korean overview line near the first page top:
  `정다훈 | Frontend-focused Product Engineer | 헬스케어 AI/B2B 플랫폼 포트폴리오`.
  Keep it to one line if the portfolio must remain 3 pages.

## Could-Improve Items

### 9. Add project-specific technology tags

- Location: each page header or end of `개발사항`.
- Recommended fix:
  - AI코치: React, TypeScript, TanStack Query, Recoil, SSE, Chart.js, Tailwind.
  - 비즈 36.5: React, TypeScript, Spring Boot, REST API, MySQL, Jenkins,
    WebView.
  - 바이오에이지: use only verified technologies from the extracted evidence;
    avoid implying full ownership of technologies not explicitly tied to the
    BioAge work.

### 10. Reduce repeated "구성했습니다 / 정리했습니다 / 개선했습니다"

- Location: development bullets and core contribution paragraphs.
- Problem: The verbs are safe but repetitive. They make distinct work streams
  feel similar.
- Recommended fix: Use more precise verbs where supported: `조율`, `설계`,
  `검증`, `추적`, `전환`, `내재화`, `표준화`.

### 11. Reconcile visual style with `DESIGN.md` and page budget

- Location: `portfolio.css`.
- Current state: The document mostly follows the project design system:
  A4, restrained palette, print media, local Korean font, footer/page numbers.
- Deviation: Body text is much smaller than `DESIGN.md` body guidance
  (`8.1-8.25pt` vs `10.2pt`). This is acceptable for dense portfolio pages but
  can reduce readability in printed form.
- Recommended fix: Choose one page budget before rewriting:
  - 3-page version: add only the metadata row, one overview line, and one metric
    per page; remove equal or greater service-description text.
  - 4-page version: add a compact overview page or section, increase body text
    closer to 9-10pt, and allow richer contribution proof.

## Unsupported Or Needs-Care Claims

| Claim | Status | Reason | Recommendation |
| --- | --- | --- | --- |
| "운영 및 QA 시간을 줄였습니다" | Needs care / must fix wording | Portfolio does not state a metric; evidence exists for automation/QA reduction, but Page 2 wording is broad. | Either tie to verified QA automation context or rephrase to "확인 절차를 정리했습니다." |
| BioAge "DB, API, PDF 생성 흐름" | Verified with extracted evidence | Found in 2026 H1 extracted evaluation, but not strongly represented in `experience-bank.md` as a standalone entry. | Safe to use, but add concise context and avoid overstating ownership. |
| BioAge "안정 생성하고 운영" | Needs specificity | Supported directionally, but broad. | Tie to report missing issue response, customer transition, or UI/report internalization. |
| Product feature descriptions | Mostly product-context, not personal claims | Features may be true service facts, but they do not prove candidate contribution by themselves. | Keep shorter and shift space to role/actions/results. |

## Suggested Next Work Order

1. Decide page budget: compact 3-page revision or more readable 4-page revision.
2. Add metadata row per project: period, role, tech stack, ownership.
3. Rewrite each page's top section so personal contribution appears before the
   long service explanation.
4. Reword Page 2's broad QA/operations reduction claim or attach a scope-safe
   verified metric.
5. Add 1-2 safe metrics:
   - AI코치 response time `10초 -> 4초`.
   - 비즈 36.5 `9주 내 108페이지·82화면`.
   - 바이오에이지 `112처 중 93처 안정 전환`, if the BioAge page leads with
     customer transition.
6. Inspect unused bundled assets before creating new visuals; then replace or
   supplement Page 2 and Page 3 screenshots with contribution-proof visuals or
   masked annotated crops.
7. Print-test the PDF after text changes because the current CSS uses fixed A4
   page height and `overflow: hidden`.

## Bottom Line

This portfolio is not highly risky from a fabrication standpoint, but Page 2's
QA/operations reduction wording needs tightening. Its main issue is positioning:
it reads like a service brochure with contribution notes, not yet like a
candidate case-study portfolio. The fastest improvement is to make each page
answer, within the first scan: "What was the problem, what did I own, what
changed, and why does it matter?"
