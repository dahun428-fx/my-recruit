# Portfolio Inventory - 2026-06-28

## Source Files Reviewed

- Source directory: `C:\Users\jungdahun\Documents\Codex\2026-06-24\new-chat-4\outputs`
- `portfolio.html`
- `portfolio.css`
- `portfolio.pdf` (file present; PDF CLI extractor not available in this shell)
- `portfolio_package.zip`
- `portfolio-assets/`

## Artifact Structure

- Format: 3-page A4 HTML/PDF portfolio.
- Language: Korean.
- Page pattern: project header, service introduction, feature list, screenshot,
  development items, core contribution, footer.
- CSS pattern: fixed A4 page size, print media support, local Noto Sans KR,
  muted navy accent, screenshot frame, absolute footer.

## Projects

| Page | Project | Label | Screenshot |
| --- | --- | --- | --- |
| 1 | 나만의 건강 AI코치 | Healthcare AI Service | `portfolio-aicoach-chat-custom.png` |
| 2 | 비즈 36.5 | B2B Platform | `portfolio-biz365-custom.png` |
| 3 | 바이오에이지 | Health Data Report | `portfolio-bioage-custom.png` |

## Claim Table

| ID | Location | Claim | Type | Evidence hint |
| --- | --- | --- | --- | --- |
| C01 | Page 1 headline | 건강검진 결과를 사용자가 이해하고 질문할 수 있는 AI 상담 서비스로 전환 | outcome | `exp-ai-health-chatbot` |
| C02 | Page 1 service intro | 검진 결과 기반 AI 건강 상담 서비스 | product scope | `exp-ai-health-chatbot` |
| C03 | Page 1 features | 이상소견, 검사 항목, 만성질환 분석, 병원 검색, 건강관리 질문 | feature scope | `experience-bank.md`, extracted evaluations |
| C04 | Page 1 dev items | SSE 기반 스트리밍 응답 적용 | technology/action | `exp-ai-health-chatbot`, `metric-ai-answer-time` |
| C05 | Page 1 dev items | AI API 응답 처리 규칙과 렌더링 흐름 정리 | action | `exp-ai-health-chatbot`; related evidence includes Markdown renderer, XSS filtering, stop/retry/error states, Config-Driven UI, Base-Theme |
| C06 | Page 1 dev items | 모바일, 태블릿, 데스크톱 반응형 화면 구성 | action | `exp-ai-health-chatbot`, profile skills |
| C07 | Page 1 dev items | 반복 질문, 실패, 빈 결과, 예외 상황을 POC 환경에서 검증 | quality/action | `exp-ai-health-chatbot`; stronger metric exists but not used |
| C08 | Page 2 headline | 기업 건강관리 기능을 고객사별 확장 가능한 B2B 플랫폼 구조로 개선 | outcome | `exp-b2b-health-platform` |
| C09 | Page 2 service intro | 검진 예약, 결과 확인, 건강제도, 사후관리, 건강관리 서비스 제공 | product scope | `exp-b2b-health-platform` |
| C10 | Page 2 dev items | 고객사별 CI, 로고, 메뉴, 탭, 제도 조건, 노출 항목 반영 구조 | action | `metric-b2b-client-change-response`, extracted 2026 H1 |
| C11 | Page 2 dev items | 108페이지 / 82화면 규모 플랫폼 개편 | metric | `metric-b2b-pages-screens`; source wording also supports `9주 내` when used close to registry wording |
| C12 | Page 2 dev items | 검진 결과 확인 이후 AI코치 진입 흐름 연결 | action/outcome | extracted 2026 H1 |
| C13 | Page 2 dev items | 주요 사용자 흐름과 변경 영향 기준 확인 절차로 운영 및 QA 시간 감소 | outcome | related to automation evidence; wording is broad and needs tightening or direct metric support |
| C14 | Page 3 headline | 검진 데이터를 생체나이 리포트로 안정 생성하고 운영할 수 있도록 개선 | outcome | BioAge entries in 2025/2026 extracted sources |
| C15 | Page 3 service intro | 생체나이와 질병 위험도를 리포트로 제공 | product scope | product context; contribution ownership is not established by this sentence alone |
| C16 | Page 3 dev items | 리포트 디자인/퍼블리싱을 내부 수정/반영 가능한 구조로 정리 | action | 2025 annual evaluation KR4 |
| C17 | Page 3 dev items | 기존 고객의 새 리포트 구조 전환 안정화 | outcome | `metric-bioage-transition` exists but not used |
| C18 | Page 3 dev items | 리포트 누락 시 DB, API, PDF 생성 흐름을 따라 문제 범위 축소 | action | extracted 2026 H1 lines on BioAge report issue |
| C19 | Page 3 core contribution | DB, API, PDF 생성 흐름을 확인하며 고객 전환과 제작 과정 안정화 | action/outcome | extracted 2026 H1 + 2025 annual evaluation |

## Assets

| Asset | Size | Review note |
| --- | --- | --- |
| `portfolio-aicoach-chat-custom.png` | 1600 x 500 | Strongest evidence image; shows actual chat flow and modal/search states. |
| `portfolio-biz365-custom.png` | 1600 x 500 | Polished but mostly public/service hero screen; weak evidence for platform architecture contribution. |
| `portfolio-bioage-custom.png` | 1600 x 500 | Explains report output, but reads like brochure material rather than contribution proof. |
| `aicoach-brochure.png` | 1684 x 1191 | Present but not used in HTML. |
| `bioage-brochure.png` | 1684 x 1191 | Present but not used in HTML. |
| `biz365-public.png` | 1264 x 1462 | Present but not used in HTML. |

## Open Review Questions

- Is the portfolio intended for a specific role, or as a general healthcare
  product portfolio?
- Should confidential/customer-sensitive UI be masked further before sharing?
- Can stronger project metrics be safely added from `metric-registry.md`,
  especially AI response time, B2B page/screen conversion, and BioAge transition?
- Should the portfolio include the candidate's title, period, tech stack, and
  ownership per project on the first scan?
- Do the unused bundled assets (`aicoach-brochure.png`, `bioage-brochure.png`,
  `biz365-public.png`) contain stronger evidence crops than the three images
  currently embedded in the HTML?
