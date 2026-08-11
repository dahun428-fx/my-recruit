# Portfolio Text Inventory — 2026-08-11

## Review scope

- Source reviewed: `outputs/portfolio-extended.html`
- Review mode: visible text only.
- Included: headings, metadata, body copy, captions, technology labels, metrics, responsibility statements, and outcome statements.
- Excluded: visual design, layout, CSS, image quality, and any inference from screenshots.
- Evidence references consulted for candidate matching only: `docs/resume-reference/ai-readable.yaml`, `profile.md`, and `experience-bank.md`.
- This inventory does not approve, reject, fact-check, or rewrite any claim.

## Project and page list

| Page | Chapter / project | Visible purpose |
| --- | --- | --- |
| 1 | Cover / document introduction | Candidate positioning, contact, career length, table of contents, disclosure about internal/B2B services and dummy data |
| 2 | AI코치 | Productization summary, role, stack, functionality, adoption, quality metrics, screen captions |
| 3 | AI코치 | Hospital-search conversation flow caption |
| 4 | 비즈36.5 | Platform summary, migration decision, role, stack, delivery scale, responsive/WebView work |
| 5 | 비즈36.5 | Health-result chart behavior, information architecture, cross-service entry point captions |
| 6 | 비즈36.5 | Responsive handling across content, list, and navigation screens |
| 7 | 바이오에이지 | Operations system, report extraction client, delivery, deployment, customer migration, screen captions |
| 8 | 검증 하네스·어드민 도구 | AX/quality workflow, tool behavior, team adoption, productivity metrics, admin preview captions |
| 9 | 검증 하네스·어드민 도구 | E2E, LLM-review, and execution-setting captions |

## Atomic claim table

| ID | Claim | Location | Type | Candidate evidence hint |
| --- | --- | --- | --- | --- |
| C-001 | The candidate has expanded from frontend work into full-stack and AI work. | p.1 headline | positioning / career scope | `profile.md` positioning and target roles; AI코치, 비즈36.5, and automation entries in `experience-bank.md` |
| C-002 | Total career length is 5 years 10 months. | p.1 cover metadata | time-sensitive metric | `profile.md` career periods; recompute against the portfolio's reference date |
| C-003 | At 대웅제약 AI추진팀, the candidate led frontend work across AI코치, 비즈36.5, and 바이오에이지. | p.1 document introduction | role / scope | `profile.md` career facts plus the three corresponding `experience-bank.md` entries |
| C-004 | The candidate directly created validation and configuration tools supporting development and operations. | p.1 document introduction | ownership | `experience-bank.md` “품질·개발·운영 자동화 및 FE AX 기준 수립” and AI코치 configuration-related evidence |
| C-005 | The portfolio is a deep-dive expansion of a three-page summary version. | p.1 document introduction | document metadata | Compare against the referenced summary artifact if retained; not a career-evidence claim |
| C-006 | Every included service is an internal or B2B service and cannot be linked publicly. | p.1 document introduction | disclosure | Owner/project confidentiality confirmation; `docs/portfolio-reference/source-materials.md` |
| C-007 | Every included screen uses a test account and dummy data. | p.1 document introduction | disclosure | Source-image preparation record or owner confirmation |
| C-008 | AI코치 work ran from 2025.07 through 2025.10. | p.2 metadata | period | `ai-readable.yaml` AI health chatbot experience; corresponding `experience-bank.md` entry |
| C-009 | The candidate had overall frontend responsibility for AI코치, from architecture through implementation and testing. | p.2 metadata | role / ownership | AI코치 role and actions in `ai-readable.yaml` and `experience-bank.md` |
| C-010 | AI코치 used React, TypeScript, TanStack Query, Recoil, SSE, Vitest, and Playwright. | p.2 metadata | technology | AI코치 technologies in `experience-bank.md`; stack attribution should be checked item by item |
| C-011 | AI코치 is an AI health-consultation service that lets users understand and ask follow-up questions about health-check results. | p.2 body | product scope | AI코치 context/problem in `ai-readable.yaml` and `experience-bank.md` |
| C-012 | AI코치 began as a mockup-level chatbot with weaknesses in response delay, Markdown rendering, error handling, and customer-specific extensibility. | p.2 body | problem statement | AI코치 problem field in `ai-readable.yaml`; corresponding detailed experience entry |
| C-013 | The candidate implemented SSE-based real-time streaming for AI코치. | p.2 body | action / ownership | AI코치 actions in `ai-readable.yaml` and `experience-bank.md` |
| C-014 | The candidate implemented stop, retry, and regenerate flows for AI answers. | p.2 body | action / ownership | AI코치 actions and evidence notes in `experience-bank.md` |
| C-015 | The candidate designed a rendering layer that converts LLM Markdown responses into React table, chart, and link components. | p.2 body and caption | architecture / ownership | AI코치 Markdown renderer evidence in `experience-bank.md` |
| C-016 | AI코치 includes health-data analysis covering checkup results, health scores, and chronic-disease analysis. | p.2 body | product capability | AI코치 actions/modules in `experience-bank.md`; product specification if available |
| C-017 | AI코치 contains 12 domain modules, including AI consultation and hospital recommendation. | p.2 body | scope metric | AI코치 metrics/modules in `experience-bank.md`; module inventory or repository evidence |
| C-018 | AI코치 was converted into a production service. | p.2 body | outcome | AI코치 result in `ai-readable.yaml` and `experience-bank.md` |
| C-019 | 3,493 employees actually used AI코치. | p.2 body | adoption metric | AI코치 usage metric in `experience-bank.md` / performance-review source mapping |
| C-020 | Across a 400-utterance validation set, the AI answer screen rendered normally 100% of the time. | p.2 body | quality metric | AI코치 metric registry/evidence notes; preserve the stated scope of the metric |
| C-021 | Average AI response time was in the two-second range, measured by network receipt. | p.2 body | performance metric | AI코치 response-time evidence in `experience-bank.md`; confirm measurement definition |
| C-022 | The AI chatbot screen scored 91 in Lighthouse. | p.2 body | performance metric | AI코치 Lighthouse evidence in `experience-bank.md`; test date/configuration if available |
| C-023 | AI코치 provides copy and regenerate interactions around rendered answers. | p.2 caption | UI capability | AI코치 implementation/evidence notes; screenshot caption itself is a source pointer |
| C-024 | AI코치 renders chronic-disease composite scores with gauge and radar charts. | p.2 caption | UI capability | AI코치 domain-module evidence; corresponding screenshot |
| C-025 | AI코치 combines disease-trend views with LLM summaries. | p.2 caption | UI capability | AI코치 domain-module evidence; corresponding screenshot |
| C-026 | The hospital-search task proceeds from welcome, to body-part selection, to result cards. | p.3 caption | interaction flow | AI코치 hospital-recommendation flow evidence; corresponding screenshot sequence |
| C-027 | 비즈36.5 work ran from 2025.11 through 2026.02. | p.4 metadata | period | `ai-readable.yaml` B2B health-platform experience; corresponding `experience-bank.md` entry |
| C-028 | The candidate performed the full-stack 비즈36.5 work alone, from data model through screen implementation. | p.4 metadata | role / ownership | B2B platform role/actions in `ai-readable.yaml`; detailed ownership notes in `experience-bank.md` |
| C-029 | 비즈36.5 used React, TypeScript, Spring Boot, MySQL, Node.js, Playwright, Jenkins, and Docker. | p.4 metadata | technology | B2B platform technologies in `experience-bank.md`; check each technology's project attribution |
| C-030 | 비즈36.5 is a B2B health-check platform covering employee booking, result review, and health management. | p.4 body | product scope | B2B platform context in `ai-readable.yaml` and `experience-bank.md` |
| C-031 | Its jQuery/Thymeleaf legacy was written in 2019 and was tightly coupled to Spring Boot and MySQL. | p.4 body | legacy-system fact | B2B platform problem/architecture notes in `experience-bank.md`; source-code history if available |
| C-032 | A one-time SPA migration was impractical because of the legacy coupling. | p.4 body | technical assessment | B2B platform architecture notes; migration decision record if available |
| C-033 | After comparing rewrite/regression risk with long-term jQuery coexistence cost, the candidate chose screen-level incremental React coexistence. | p.4 body | architecture decision / ownership | B2B platform actions and notes in `ai-readable.yaml` and `experience-bank.md` |
| C-034 | The candidate prioritized areas with frequent changes and incidents. | p.4 body | prioritization / ownership | B2B platform delivery notes, issue history, or owner attestation |
| C-035 | The candidate alone converted 108 pages and 82 screens within nine weeks. | p.4 body | delivery metric / ownership | B2B platform metrics in `ai-readable.yaml` and `experience-bank.md`; clarify page-versus-screen counting |
| C-036 | For new health-management features, the candidate developed the MySQL model, Spring Boot logic, REST API, and UI end to end. | p.4 body | full-stack ownership | B2B platform actions in `ai-readable.yaml` and `experience-bank.md` |
| C-037 | The service supports both PC and mobile sizes through media queries. | p.4 body and caption | responsive implementation | B2B platform implementation notes; corresponding screenshots |
| C-038 | 비즈36.5 is delivered on mobile through WebView. | p.4 body | platform fact | B2B platform context/technology notes; app integration evidence |
| C-039 | The candidate established iOS and Android WebView compatibility criteria. | p.4 body | quality / ownership | B2B platform WebView verification notes in `experience-bank.md` |
| C-040 | The health-result trend chart includes normal-range shading and a no-result state on PC and mobile. | p.5 caption | UI capability | Corresponding screenshot and implementation record |
| C-041 | The GNB mega-menu represents an information architecture spanning 108 pages. | p.5 caption | scale / information architecture | B2B platform 108-page metric plus corresponding screenshot |
| C-042 | The mobile home uses an AI코치 banner as an entry point connecting services. | p.5 caption | cross-service capability | Corresponding screenshot; AI코치/비즈36.5 integration notes |
| C-043 | Health-policy boards, examination-product selection, and mobile navigation each received screen-type-specific responsive handling. | p.6 caption | responsive implementation | Corresponding screenshots and B2B platform responsive notes |
| C-044 | 바이오에이지 work spans 2025 through the present. | p.7 metadata | time-sensitive period | 바이오에이지 / 2025 business-contribution entry in `experience-bank.md`; recompute “present” at review time |
| C-045 | The candidate's 바이오에이지 role is maintenance, modification, and operation. | p.7 metadata | role | 바이오에이지 role/actions in `experience-bank.md` |
| C-046 | 바이오에이지 used React, Electron, AWS S3, and EC2. | p.7 metadata | technology | 바이오에이지 technologies in `experience-bank.md`; check each attribution |
| C-047 | 바이오에이지 converts checkup data into analysis reports for hospitals. | p.7 body | product scope | 바이오에이지 context in `experience-bank.md` |
| C-048 | The candidate took over an externally developed V2 and reduced UI and data-operation risks. | p.7 body | action / outcome | 바이오에이지 actions/results in `experience-bank.md`; clarify what “reduced risks” denotes |
| C-049 | The candidate directly developed or modified report-management and standard-code-management screens. | p.7 body and captions | action / ownership | 바이오에이지 actions in `experience-bank.md`; corresponding screenshots |
| C-050 | The resulting work was delivered to Seoul St. Mary's Hospital. | p.7 body | delivery outcome | 바이오에이지 customer/delivery evidence in `experience-bank.md` |
| C-051 | The candidate maintained an Electron desktop client that automatically extracts reports. | p.7 body and caption | action / product capability | 바이오에이지 Electron-client evidence in `experience-bank.md` |
| C-052 | The candidate operated a deployment pipeline on a pre-existing AWS S3/EC2 environment. | p.7 body | operations / scope boundary | 바이오에이지 deployment evidence; wording distinguishes operation from initial setup |
| C-053 | Of 112 existing customers, 93 were stably migrated. | p.7 body | migration metric | 바이오에이지 customer-migration metric in `experience-bank.md` / performance-review source |
| C-054 | The report-management preview shown uses test data and a development checkup-center identity. | p.7 caption | disclosure | Corresponding screenshot preparation record |
| C-055 | Sensitive information, version text, and local storage paths were cropped or withheld from the Electron screenshot. | p.7 caption | disclosure | Corresponding screenshot/redaction record |
| C-056 | The quality/AX initiative ran from 2026.01 through 2026.06. | p.8 metadata | period | Automation/FE AX entry in `experience-bank.md` |
| C-057 | The candidate led the team's AX transition and independently designed the validation harness. | p.8 metadata | role / ownership | Automation/FE AX role and ownership notes in `experience-bank.md` |
| C-058 | The initiative used Claude Code, Codex, GitLab merge requests, Playwright, Storybook, GA4, and PostHog. | p.8 metadata | technology / tool | Automation/FE AX technologies in `experience-bank.md`; check each tool's role and attribution |
| C-059 | Utterance tests, LLM-response review, type/build checks, and pre/post-deployment checks were combined into tools applying consistent criteria. | p.8 body | process / automation | Automation/FE AX actions in `ai-readable.yaml` and `experience-bank.md` |
| C-060 | Playwright E2E became a mandatory deployment-pipeline gate. | p.8 body | process / quality gate | Automation/FE AX evidence in `experience-bank.md`; pipeline configuration if available |
| C-061 | All ten team members adopted the same validation and deployment approach. | p.8 body | adoption metric | Automation/FE AX user-attested team adoption notes in `experience-bank.md` |
| C-062 | The LLM-response review tool automatically enters prepared questions and regression-checks responses containing Markdown, tables, and buttons. | p.8 body | tool capability | Automation/FE AX tool notes; tool source or run artifacts if available |
| C-063 | The UI/UX E2E tool drives screens step by step from JSON scenarios. | p.8 body | tool capability | Automation/FE AX tool notes; JSON scenario examples |
| C-064 | The UI/UX E2E tool supports multiple viewports and visual regression checks. | p.8 body and p.9 caption | tool capability | Automation/FE AX tool notes; baseline configuration and run artifacts |
| C-065 | The admin configuration builder controls tenant-specific AI코치 content, themes, and feature flags. | p.8 body and captions | admin capability | AI코치 configuration-driven UI evidence in `experience-bank.md`; builder implementation evidence |
| C-066 | Configuration changes appear immediately in a preview screen. | p.8 body and caption | admin capability | Builder implementation evidence; corresponding screenshot |
| C-067 | The quality system reduced repeated QA from three hours to 30 minutes. | p.8 body | productivity metric | Automation/FE AX metrics in `experience-bank.md`; owner-attested final override is noted there |
| C-068 | Repeated component-development time fell from 90 minutes to 15 minutes. | p.8 body | productivity metric | Automation/FE AX metrics in `experience-bank.md` |
| C-069 | Operational-data checks were automated from three steps to one. | p.8 body | process metric | Automation/FE AX metrics in `ai-readable.yaml` and `experience-bank.md` |
| C-070 | The E2E tool exposes viewport selection and a visual-regression baseline-folder setting. | p.9 caption | tool capability | Corresponding screenshot and E2E tool configuration |
| C-071 | The LLM-review tool accepts Excel input and can save screenshots as output. | p.9 caption | tool capability | Corresponding screenshot and tool implementation/run artifact |
| C-072 | The tool execution flow covers session injection, scenario upload, and execution. | p.9 caption | operating procedure | Corresponding screenshot and tool operating notes |

## Visible caption inventory

- AI코치: rendered AI table response; chronic-disease composite-score gauges/radar; disease trends with AI summary; hospital-search conversation flow.
- 비즈36.5: PC/mobile booking; result-trend charts; GNB mega-menu; mobile AI코치 entry banner; health-policy board; examination-product selection; mobile menu.
- 바이오에이지: report detail/preview; report operations list; standard-code management; Electron report-extraction client.
- 검증 하네스·어드민 도구: live configuration preview; feature-flag control; viewport/baseline settings; Excel/screenshot-output settings; session/scenario execution screen.

No binary asset inspection was performed because the requested scope was text only. The list above records captions as visible copy, not an assessment of the depicted images.

## Open questions for follow-up reviewers

1. What date should anchor the cover's “5 years 10 months” calculation, and is that value intended to remain static?
2. Does “프론트엔드를 총괄한 세 서비스” mean sole frontend ownership for each service, or overall coordination with different contribution levels by service?
3. Is there a retained artifact for the “three-page summary version” referenced on the cover?
4. Can one source record confirm that all included services are non-public internal/B2B services and that every screenshot uses only test/dummy data?
5. For AI코치, what is the authoritative inventory behind “12 domain modules,” and how is a module counted?
6. For AI코치's 3,493 users, what period and user definition apply (eligible, signed in, or active users)?
7. For the 400-utterance/100% metric, were all utterances run in one environment and period, and what counted as normal output?
8. For the two-second AI response metric, does “network receipt” mean first byte, first token, or completed response?
9. For Lighthouse 91, what device profile, test date, and run conditions apply?
10. For 비즈36.5, how are “108 pages” and “82 screens” distinguished, and what exactly was “converted” within nine weeks?
11. Does “풀스택 단독 수행” apply to the entire platform conversion, the new health-management functions, or both?
12. Is the legacy system's “written in 2019” date supported by repository history or owner attestation?
13. Which newly developed health-management functions substantiate the end-to-end ownership statement?
14. For 바이오에이지, what exact start month underlies “2025 ~ 재직중,” and should “재직중” be replaced or date-checked at publication?
15. What observable changes support “UI와 데이터 운영 리스크를 걷어냈고” and “안정적으로 전환”?
16. For the 112-to-93 customer migration metric, what happened to the other 19 customers and what defined a stable transition?
17. Does “팀 AX 전환 리드” refer to the ten-person squad named later, and what leadership responsibilities are included?
18. The evidence bank records the three-hour-to-30-minute QA value as an owner-attested override without documentary support; what publication evidence level is desired?
19. Which repository/configuration artifacts support the mandatory pipeline-gate claim and the ten-of-ten team-adoption claim?
20. Are the admin configuration builder and the test harnesses production tools, internal local tools, or a mix? Their operating scope may need to be distinguished during fact-checking.
