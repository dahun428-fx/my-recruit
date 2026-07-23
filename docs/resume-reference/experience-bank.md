# Experience Bank

This file stores reusable evidence for resumes, self-introductions, and cover
letters. Each entry should be factual enough to support multiple tailored
versions.

## How To Add An Entry

Use this structure:

```markdown
## Project / Experience Name

- Period:
- Context:
- Problem:
- Role:
- Actions:
- Technologies:
- Result:
- Metrics:
- Evidence / links:
- Reusable keywords:
- Notes for tailoring:
```

## Entries

Rows and sections marked `TBD` are placeholders and must not be used as source
facts in drafted application text.

### AI 건강검진 챗봇 제품화 및 플랫폼 확장

- Period: 2025.07 ~ 2025.10
- Context: 대웅제약 AI추진팀 / AI 헬스케어·B2B 플랫폼 (신규 고객사 웰체크 온보딩 포함, user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인)
- Problem: 목업 수준의 AI 건강검진 챗봇을 실사용 가능한 서비스로 고도화해야 했고, LLM 답변 지연, Markdown/표/링크 렌더링, 오류 대응, 고객사별 화면 확장 구조가 부족했다.
- Role: 프론트엔드 유일 담당자로 FE 기술적 의사결정권을 가지고 아키텍처 설계·분석부터 구현·테스트까지 독립적으로 수행, BE/LLM 개발자와 협의하며 AI/백엔드 응답 정책 조율 및 LLM/BE 로직 일부에 참여(팀 공동 기여, 단독 구축 아님), 서비스 품질 및 확장 구조 구축 (user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인)
- Actions:
  - AI 개발자와 API 응답 형식, 스트리밍, 오류 정책 조율
  - SSE 기반 실시간 응답, 답변 중지/재시도/오류 상태를 포함한 대화 흐름 설계
  - Markdown 전용 렌더링 계층 구축, 표/목록/링크/차트의 React 컴포넌트 변환
  - XSS 필터링, 404/500/LLM 오류 가드레일 적용
  - React Query 캐싱, 코드 스플리팅, 이미지 최적화, HTTP/2 전환
  - Base-Theme과 Config-Driven UI로 고객사별 테마/문구/기능 노출 조건 분리 — 전사 요구사항인 "기능별로 차별점을 두어 애플리케이션 가격을 매기고 싶다"(기능별 차등 가격 정책)에 대응하기 위해 feature flag 형태로 구현, 운영/기획자가 FE 단에서 기능을 분할·제한할 수 있도록 설계 (user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인)
  - 위 Config-Driven UI 전환을 위해 이미 완성돼 있던 챗봇 소스코드의 상당 부분을 수정하는 대규모 리팩토링 수행 (user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인)
- Technologies: React, TypeScript, TanStack Query, Recoil, SSE, Chart.js, Tailwind CSS
- Result:
  - PoC 수준의 AI 서비스를 실사용 가능한 AI 건강검진 챗봇으로 전환
  - 신규 AI 챗봇 반복 구축에 사용할 수 있는 공통 FE 확장 구조 확보
- Metrics:
  - 3,493명 규모 PoC 운영
  - 사용성 4.18점, 서비스 만족도 4.06점, 완성도 4.05점
  - AI 답변 출력 시간 10초 -> 4초, 60% 단축
  - 초기 서비스 진입 시간 30초 -> 6초, 80% 단축
  - 400건 발화 검증 기준 답변 화면 정상 출력률 100%
  - Lighthouse 91점
  - 신규 AI 챗봇 구축 기간을 10주에서 2주로 줄일 수 있는 공통 구조 확보(원문 표현: 80% 단축 가능한 구조) — **스코프 정정(user-attested 2026-07-23, headhunter-advisor 인터뷰)**: 10주는 챗봇 최초 구현 기간, 2주는 신규 고객사(웰체크) 입점 시 Base-Theme을 활용해 색상·CI·기능을 커스터마이징해 FE 단을 납품한 기간. 2주는 FE 납품 기준 수치이며 LLM/BE 일정은 별도로 고려되지 않았으므로, "챗봇 전체를 2주 만에 만들었다"는 식으로 확대 해석 금지
  - 계획 대비 2주 빠르게 PoC 고도화 완료
- Evidence / links:
  - `sources/이력서_20260624.pdf`
  - `extracted/이력서_20260624.txt`
  - `sources/2026_상반기종합평가.xlsx`
  - `extracted/2026_상반기종합평가.md`
  - `sources/연종합평가2025_정다훈.xlsx`
  - `extracted/연종합평가2025_정다훈.md`
  - user-attested 2026-07-23 (headhunter-advisor 인터뷰에서 사용자 직접 확인) — Config-Driven UI/Base-Theme 배경, 리팩토링 규모, "10주->2주" 스코프 정정, 웰체크 실명 사용 동의
- Reusable keywords: AI 서비스 제품화, LLM 챗봇, SSE Streaming, Markdown Renderer, XSS 필터링, Config-Driven UI, Base-Theme, feature flag, PoC 고도화
- Notes for tailoring: AI/플랫폼/프론트엔드 아키텍처 직무에서 최우선 사례로 사용. `2026_상반기종합평가`는 2026년 상반기 평가 자료이므로 2025.07~2025.10 프로젝트의 후속 안정화/확장 성과를 함께 입증하는 보조 근거로만 사용. 신규 고객사 실명 "웰체크"는 소유자 동의로 외부 문서에 사용 가능(user-attested 2026-07-23). "10주->2주" 수치를 인용할 때는 반드시 위 Metrics의 스코프 정정(10주=최초 구현, 2주=웰체크 FE 납품 기준)을 함께 확인하고, "챗봇 전체를 2주 만에 구축"처럼 과장 해석하지 않는다.

### B2B 임직원 건강 플랫폼 풀스택 내재화

- Period: 2025.11 ~ 2026.02
- Context: 외주 중심으로 운영되던 검진 예약 서비스를 내부 개발/운영 가능한 임직원 건강 플랫폼으로 전환
- Problem: jQuery/Thymeleaf 화면, Spring Boot 서버 로직, MySQL 데이터 구조가 기능별로 결합돼 변경 영향 파악이 어려웠고 Web/Admin/App 권한과 데이터 출력 정책이 달랐다. 당시 BE-FE가 분리되지 않은 모놀리식 구조였고 Spring Boot가 RESTful하지 않았으며 Thymeleaf와 강결합되어 있어 SPA 형태로 한 번에 전환할 수 없었다 (user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인).
- Role: 서비스/데이터 구조 분석, MySQL/Spring Boot/REST API/Web/Admin 개발, WebView 앱 운영 및 CI/CD 구축. 9주 내 108개 페이지·82개 화면 전환은 본인이 단독으로 수행(팀 산출이 아닌 개인 기여) (user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인)
- Actions:
  - 기존 소스와 DB 스키마 분석, 화면 요청부터 Controller/Service/Query/DB/화면 출력까지 데이터 흐름 정리
  - 건강관리 신규 기능에 필요한 MySQL 데이터 모델, Spring Boot 서버 로직, REST API, Web/Admin 화면 End-to-End 개발
  - 2019년에 작성된 레거시 스파게티 코드를 걷어내고 재활용 가능한 컴포넌트 구조로 빠르게 UI/UX를 개편하는 것을 목표로 설정 (user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인)
  - jQuery/Thymeleaf와 React가 화면 단위로 공존하는 점진적 전환 구조 설계 — BE-FE 미분리·비RESTful Spring Boot·Thymeleaf 강결합 제약으로 SPA를 한 번에 도입할 수 없어, island-loader 패턴을 활용해 React를 SPA는 아니지만 화면 단위로 컴포넌트를 재사용할 수 있는 수준으로 구현 (user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인)
  - island-loader 패턴을 선택한 이유: (a) 이후 목표였던 Next.js 전환을 쉽게 하기 위한 사전 단계였고, (b) island-loader로 컴포넌트를 재활용하는 것이 풀 리라이트 대비 비용적으로 더 저렴하다고 판단 — 이 구조 덕분에 9주 내 UI/UX 개편을 빠르게 완료할 수 있었음 (user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인)
  - 사용자 권한, 메뉴, 브랜딩, 데이터 출력 정책을 공통 기준으로 정리
  - Jenkins 빌드/검증/배포 파이프라인과 WebView 호환성 검증 기준 수립
- Technologies: React, TypeScript, jQuery, Thymeleaf, Java, Spring Boot, REST API, MySQL, Tailwind CSS, Jenkins CI/CD, WebView, iOS, Android
- Result:
  - 외주 의존 서비스의 기능 변경과 배포를 내부 대응 가능한 운영 구조로 전환
  - 고객사별 CI/메뉴/기능 노출 변경에 반복 대응 가능한 SaaS형 기반 확보
- Metrics:
  - 9주 내 108개 페이지, 82개 화면을 임직원 건강 플랫폼으로 전환 — island-loader 패턴 기반 컴포넌트 재사용 구조로 달성했으며 108개 페이지·82개 화면 전환은 본인 단독 수행 (근거: 위 Role/Actions, user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인)
  - 건강관리 신규 기능 3건을 데이터 모델부터 서버/API/화면까지 End-to-End 개발
  - 고객사별 CI/메뉴/기능 노출 변경을 1주 내 대응 가능한 구조 구축
- Evidence / links:
  - `sources/이력서_20260624.pdf`
  - `extracted/이력서_20260624.txt`
  - `sources/2026_상반기종합평가.xlsx`
  - `extracted/2026_상반기종합평가.md`
  - user-attested 2026-07-23 (headhunter-advisor 인터뷰에서 사용자 직접 확인) — 108개 페이지·82개 화면 전환 단독 수행 여부, BE-FE 미분리·비RESTful Spring Boot·Thymeleaf 강결합이라는 기술적 배경, island-loader 패턴 채택 배경과 이유(Next.js 전환 사전 단계, 풀 리라이트 대비 비용 절감)
- Reusable keywords: B2B 플랫폼, 풀스택 내재화, Spring Boot, MySQL, Web/Admin, WebView, Jenkins CI/CD, SaaS형 구조, island-loader 패턴, 점진적 SPA 전환
- Notes for tailoring: 풀스택/플랫폼/운영 안정화 직무에 적합. 108개 페이지·82개 화면 전환은 개인 단독 기여이므로 "본인이 단독으로 수행"이라는 개인 기여 프레이밍을 사용할 수 있다. island-loader 패턴 채택은 당시 모놀리식·비RESTful·Thymeleaf 강결합 제약 하의 기술적 의사결정(전면 SPA 전환 대신 화면 단위 컴포넌트 재사용, Next.js 전환의 사전 단계, 비용 효율)으로 서술할 것 — 풀 SPA 전환을 했다고 과장하지 않는다.

### 품질·개발·운영 자동화 및 FE AX 기준 수립

- Period: 2026년 상반기
- Context: AI코치, 비즈36.5, 바이오에이지 운영 서비스와 공통 컴포넌트 증가
- Problem: 수동 발화 테스트, 반복 UI 개발, 배포 전후 확인, 운영 지표 조회가 병목이 되었고 AI 생성 코드의 품질/보안/일관성을 검증할 기준이 필요했다.
- Role: 테스트/배포/운영 데이터 확인 절차 자동화 및 팀 개발 기준 수립
- Actions:
  - E2E 발화 테스트, LLM 응답 검증, 타입/테스트/빌드, 배포 전후 확인을 품질 흐름으로 통합
  - Playwright 기반 주요 사용자 흐름과 회귀 시나리오 자동화
  - Storybook 중심의 컴포넌트 개발/검증 절차 수립
  - GA4/PostHog 기반 운영 데이터 대시보드 구축
  - AI 생성 코드의 컨텍스트 관리, 금지 패턴, 보안 위험, 검증 절차를 FE AX SOP로 문서화
  - Codex·Claude Code 등 AI 코딩 에이전트를 활용한 개발과, 생성 코드의 검증·금지 패턴·보안 기준 수립 (user-attested 2026-07-22 — AX본부 JD 대응 세션에서 사용자 직접 확인. 문서 근거 미확보, pending documentary source)
- Technologies: Playwright, Storybook, Jest, ESLint, TypeScript, Jenkins, GitLab CI/CD, GA4, PostHog, Codex, Claude Code
- Result:
  - QA, 운영 확인, 반복 컴포넌트 개발의 수작업 의존도를 낮추고 팀 개발 기준을 조직 자산화
- Metrics:
  - 600여 건의 E2E 회귀 시나리오 자동화
  - 반복 QA 시간 3시간 -> 1시간
  - 운영 데이터 확인 절차 3단계 -> 1단계
  - 반복 컴포넌트 개발 시간 90분 -> 15분, 약 83% 단축
  - 기획-개발 검증 리드타임 2일 -> 1일
  - 테스트 커버리지 98% 수준 확보
- Evidence / links:
  - `sources/이력서_20260624.pdf`
  - `extracted/이력서_20260624.txt`
  - `sources/2026_상반기종합평가.xlsx`
  - `extracted/2026_상반기종합평가.md`
- Reusable keywords: Playwright, Storybook, FE AX, SOP, 품질 자동화, 운영 데이터 대시보드, 회귀 테스트, AI 생성 코드 검증
- Notes for tailoring: 생산성/품질/AI 개발 프로세스 개선을 강조할 때 사용.

### 삼성물산 데이터·모바일 서비스 고도화

- Period: 2024.10 ~ 2025.04
- Context: 데이터 플랫폼과 React Native 모바일 애플리케이션 고도화
- Problem: Web 대시보드의 대용량 테이블/시계열 데이터 렌더링과 모바일 앱의 반복 API 호출 및 플랫폼별 동작 차이가 사용자 대기와 운영 부담을 만들었다.
- Role: 대용량 데이터 시각화, Spring REST API/데이터 연동, React Native iOS/Android 개발 및 배포
- Actions:
  - Vue 3, ECharts, RealGrid 기반 대용량 데이터 화면 개발
  - 테이블/차트 렌더링 생명주기 분리와 Lazy Rendering 적용
  - Spring REST API와 필터링/정렬 로직 설계, 역할별 데이터 조회/표현 구조 개발
  - React Native 앱 검색/조회 흐름 개선 및 플랫폼별 이슈 대응
- Technologies: Vue 3, React Native, TypeScript, ECharts, RealGrid, Java, Spring, REST API, MyBatis, MySQL, Recoil, SQLite, Firebase FCM
- Result:
  - 대용량 데이터 조회와 모바일 검색 체감 성능 개선
- Metrics:
  - 대용량 데이터 대시보드 렌더링 시간 2.5초 -> 1초대
  - React Native 앱 검색 응답 시간 5초 -> 1초, 80% 단축
- Evidence / links:
  - `sources/이력서_20260624.pdf`
  - `extracted/이력서_20260624.txt`
- Reusable keywords: 데이터 시각화, Vue 3, ECharts, RealGrid, React Native, REST API, 성능 개선
- Notes for tailoring: 데이터 플랫폼, 모바일 앱, 대시보드 직무에 활용.

### 한국미스미 글로벌 B2B 커머스 개선 및 Next.js 전환

- Period: 2022.06 ~ 2024.10
- Context: 글로벌 B2B 커머스의 레거시 유지보수, 성능/SEO/다국어/모니터링 개선
- Problem: PHP/jQuery 기반 레거시 환경에서 유지보수성과 페이지 성능, SEO, 다국어 대응, 오류 추적이 필요했다.
- Role: 사용자 기능 개발, PHP/jQuery 레거시 분석, Next.js 전환, 렌더링/성능/SEO/다국어/배포/모니터링 구조 개선
- Actions:
  - PHP/jQuery 기반 B2B 쇼핑몰을 React/Next.js/TypeScript 구조로 전환
  - Lighthouse, GA, Adobe Analytics, Datadog 기반 성능/SEO/오류 추적 운영
  - Lazy Loading, 비동기 API, 폰트 최적화 적용
- Technologies: Next.js, React, TypeScript, JavaScript, Redux, RxJS, i18next, PHP, jQuery, Twig, Vercel, Datadog, Google Lighthouse, Google Analytics, Adobe Analytics
- Result:
  - 레거시 B2B 커머스의 평균 로딩 속도와 접근 성능 개선
- Metrics:
  - 페이지 접근 시간 8초 -> 2초 단축
  - Next.js 전환 후 기존 PHP 서비스 대비 평균 로딩 속도 약 50% 개선
- Evidence / links:
  - `sources/이력서_20260624.pdf`
  - `extracted/이력서_20260624.txt`
- Reusable keywords: B2B 커머스, Next.js 전환, 레거시 개선, 성능 최적화, SEO, 모니터링
- Notes for tailoring: 커머스/프론트엔드 성능 개선 사례로 활용.

### 2025 대웅제약 성과 평가 기반 사업 기여

- Period: 2025년
- Context: 에스크미, AI코치, 생체나이, 비즈케어 관련 성과
- Problem: 외주/분산 구조 내재화, AI코치 신규 개발, 생체나이 서비스 이관, 운영 리스크 제거가 필요했다.
- Role: AI코치 신규 개발, 비즈케어 내재화, 생체나이 UI/운영 리스크 개선, 데모/서비스 도입 지원. 프로젝트별 기여 성격 — 비즈케어: UI/UX를 전면 개편해 대웅제약 대상 판매로 이어진 사례를 본인이 주도, 생체나이: 외주로 도입된 V2 버전을 본인이 유지보수·수정하여 서울성모병원에 납품, 에스크미: 한국 KMI를 대상으로 유지보수 지원, AI코치: 비즈케어의 사이드 상품으로 패키지 형태 추가 판매(파생 매출)에 기여 (user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인)
- Actions:
  - 비즈케어 외주/분산 구조 내재화 및 고도화 — UI/UX를 전면 개편해 대웅제약 대상 판매로 이어지는 성과에 본인이 주도적으로 기여 (user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인)
  - AI코치 신규 개발 및 실서비스 전환 주도 — 비즈케어의 사이드 상품으로 패키지 형태 추가 판매되는 파생 매출 구조에 해당 (user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인)
  - 생체나이 서비스 UI와 데이터 운영 리스크 제거 — 외주로 도입된 V2 버전을 본인이 유지보수·수정하여 서울성모병원에 납품 (user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인)
  - 에스크미 한국 KMI를 대상으로 유지보수 지원 (user-attested 2026-07-23 — headhunter-advisor 인터뷰에서 사용자 직접 확인, 원본 평가 문서에 없던 신규 항목)
  - 개발 세미나 12회 운영, 기술 문서 48건 축적
- Technologies: AI코치, WebView, AWS, Jenkins CI/CD, Storybook, PostHog, Tailwind CSS
- Result:
  - 매출 지표와 서비스 안정성, 내재화 속도 개선
- Metrics:
  - 원문 기준 총 4.66억 원 매출 창출, KR1 목표 대비 93.2%
  - 원문 세부 항목: 비즈케어 1.0억, AI코치 0.2억, 생체나이 2.5억, 에스크미 0.9억. 세부 항목 합계는 4.6억으로 총액 4.66억과 차이가 있어 외부 문서에서는 총액 또는 세부 항목 중 하나만 사용 권장
  - 생체나이 기존 고객 112처 중 93처, 83% 안정 전환
  - AI코치 신규 화면 11건, 신규 기능 13건 개발
  - 2차 PoC 사용자 3,493명, 사용성 4.18점, 만족도 4.06점, 완성도 4.05점
  - HTTP/2 전환으로 네트워크 비용 1,200KB -> 900KB, 25% 감소
  - 평균 응답 속도 1.2s -> 0.7s
  - FE 에러 0건
  - Jenkins CI/CD 배포 리드타임 10분 -> 2분, 80% 단축
  - 비즈케어 내재화 3일 내 완료
- Evidence / links:
  - `sources/연종합평가2025_정다훈.xlsx`
  - `extracted/연종합평가2025_정다훈.md`
  - user-attested 2026-07-23 (headhunter-advisor 인터뷰에서 사용자 직접 확인) — 프로젝트별 기여 성격(비즈케어 UI/UX 개편 주도, 생체나이 외주 V2 유지보수·수정 후 서울성모병원 납품, 에스크미 한국 KMI 유지보수 지원, AI코치 비즈케어 파생 패키지 판매) 및 4.66억(세부 4개 항목 포함)이 개인이 아닌 조직/팀 전체 KR 목표 수치라는 확인
- Reusable keywords: 매출 기여, 내재화, AI코치, 생체나이, 비즈케어, FE 에러 0건, CI/CD, 기술 세미나
- Notes for tailoring: 사업성과/조직기여/내재화 관점이 필요한 자기소개서에 활용. 비즈케어와 비즈36.5, 생체나이와 바이오에이지는 문맥에 따라 함께 쓰이는 명칭이므로 제출 문서에서는 하나의 명칭으로 통일. **팀 KR 가드레일(user-attested 2026-07-23, headhunter-advisor 인터뷰)**: Metrics의 총 4.66억 및 세부 항목(비즈케어 1.0억/AI코치 0.2억/생체나이 2.5억/에스크미 0.9억)은 조직/팀 전체 KR 목표 수치이며 본인 개인의 매출 성과가 아니다. 본인은 4개 프로젝트 전부에 FE 개발자로 직간접 기여했지만 기여 강도는 프로젝트마다 다르다(비즈케어=UI/UX 개편 주도, 생체나이=외주 V2 유지보수·수정 후 납품, 에스크미=유지보수 지원, AI코치=비즈케어 파생 패키지 판매). 자기소개서·이력서 작성 시 이 총액/세부 금액을 본인 단독 성과처럼 서술하지 말고, 반드시 "팀/조직 성과에 기여" 프레이밍과 위 Role의 프로젝트별 기여 성격을 함께 명시할 것 — writer/tailor는 팀 성과를 개인 성과처럼 과장하지 않는다.

### 비즈36.5 Node.js(Express) BFF 신규 구축 및 AI 챗봇 Python 로직 기여

- Period: 2025.07 ~ 재직중 중 대웅제약 AI추진팀 기간 내 (정확한 시작월 [확인 필요])
- Context: 대웅제약 AI추진팀 / 비즈36.5(비즈케어) B2B 헬스케어 플랫폼 및 AI 건강검진 챗봇
- Problem: 신규 기능에서 React 프론트가 여러 백엔드 데이터를 집계·가공해 받아야 했고, AI 챗봇 응답의 프롬프트 구성·후처리 품질을 개선해야 했다. 더 넓게는 모놀리식 구조에서 BE-FE를 분리하려는 전략의 일환이었고, RESTful API를 점진적으로 도입해 Spring Boot/Thymeleaf의 강결합을 개선하려는 목적도 있었다.
- Role: 프론트 전용 BFF API 신규 구축(팀 공동), AI 챗봇 서버의 Python 프롬프트·후처리 로직 기여(팀 공동)
- Actions:
  - 비즈36.5에서 React 프론트 전용 데이터 집계·프록시(BFF) REST API를 Node.js(Express)로 신규 구축 (기존 Spring Boot 대체가 아닌 신규 개발)
  - 비동기 I/O 이점과 프론트–백엔드 TypeScript 스택 통일을 위해 Node를 선택
  - BE-FE 미분리 모놀리식 구조를 분리하는 전략의 일환으로, RESTful API를 점진 도입해 Spring Boot/Thymeleaf 강결합을 개선하는 방향으로 BFF를 구축(팀 공동)
  - AI 챗봇(Python) 서버의 프롬프트 구성·응답 후처리(Markdown/표/링크 변환 등) 로직 일부를 직접 수정·기여
- Technologies: Node.js, Express, TypeScript, Python, REST API, SSE
- Result:
  - React 프론트의 다중 백엔드 데이터 연동을 단일 BFF 계층으로 단순화
  - AI 챗봇 응답 포맷·프롬프트 품질 개선에 기여
- Metrics:
  - 정량 지표 미확보 (있으면 추후 추가)
- Evidence / links:
  - user-attested 2026-07-05 (grilling 세션에서 사용자 직접 확인)
  - user-attested 2026-07-23 (headhunter-advisor 인터뷰에서 사용자 직접 확인) — BFF 구축이 모놀리식 구조에서 BE-FE를 분리하려는 전략의 일환이었고, RESTful API 점진 도입으로 Spring Boot/Thymeleaf 강결합을 개선하려는 목적도 있었다는 전략적 배경 확인 (팀 공동 범위는 변경 없음)
  - 문서 근거 미확보 — 이력서 PDF·평가 문서에는 미기재. pending documentary source.
- Reusable keywords: Node.js, Express, BFF, TypeScript 스택 통일, 비동기 I/O, Python, LLM 프롬프트, 응답 후처리, 풀스택
- Notes for tailoring: Node/Python이 필수·우대인 포지션(두산로보틱스 Fullstack 등)에서 사용. 반드시 "신규 BFF 구축(팀 공동)"·"Python 로직 일부 기여(팀 공동)" 범위로만 표기. "Spring Boot를 Node로 대체", "Python AI 서버 구축/개발" 같은 표현은 사실과 다르므로 금지. 정량 지표가 없으므로 수치 창작 금지.

## Achievement Fragments

Use this section for short, validated bullet material that can be remixed.

- 3,493명 대상 AI 건강검진 챗봇 PoC를 실서비스로 전환하고, 사용성 4.18점·서비스 만족도 4.06점·완성도 4.05점을 확보했다.
- SSE 기반 실시간 응답과 Markdown 렌더링 안정화로 AI 답변 출력 시간을 10초에서 4초로 60% 단축했다.
- Config-Driven UI와 Base-Theme 구조로 신규 고객사(웰체크) 온보딩 시 FE 커스터마이징 납품 기간을 10주(최초 챗봇 구현 기간)에서 2주(FE 납품 기준, LLM/BE 일정 별도)로 단축 가능한 구조를 설계했다.
- B2B 임직원 건강 플랫폼을 9주 내 108개 페이지·82개 화면으로 전환하고, 신규 건강관리 기능 3건을 End-to-End로 개발했다.
- Playwright 기반 600여 건의 E2E 회귀 시나리오를 자동화해 반복 QA 시간을 3시간에서 1시간으로 줄였다.
- 운영 데이터 확인 절차를 3단계 수작업에서 1단계 자동화 대시보드로 전환했다.
- 반복 컴포넌트 개발 시간을 90분에서 15분으로 약 83% 단축했다.
- 대용량 데이터 대시보드 렌더링 시간을 2.5초에서 1초대로 개선했다.
- React Native 앱 검색 응답 시간을 5초에서 1초로 80% 단축했다.
- PHP 기반 B2B 커머스를 Next.js/React/TypeScript 구조로 전환하며 평균 로딩 속도를 약 50% 개선했다.
- 2025년 비즈케어·AI코치·생체나이·에스크미 전반에서 원문 기준 총 4.66억 원 매출 기여를 기록했다.

## Metrics To Verify

Numbers here are not ready to use until confirmed.
Do not use these metrics in final copy until their status is changed to
`confirmed`.

| Claim | Source | Status |
| --- | --- | --- |
| 정보처리기사 발급일(월) | `sources/이력서_20260624.pdf` | confirmed — 취득월 2020.08 (user-attested 2026-07-22). 원본 PDF는 미표기였으나 소유자 확인 |
| TOEIC 825점 취득일 | `extracted/이력서_20260624.txt` | confirmed — 취득일 2024.05 |
| JLPT 1급 취득일 | `extracted/이력서_20260624.txt` | confirmed — 취득일 2018.08 |
| 연봉 5,700만원 포함 여부 | `sources/이력서_20260624.pdf` | user confirmation required |
| 테스트 커버리지 98%의 기준(라인/브랜치/시나리오) | `extracted/연종합평가2025_정다훈.md`(L68), `extracted/이력서_20260624.txt`(L200) | value confirmed as "98% 수준" — 라인/브랜치/시나리오 세부 기준은 원본 미기재이므로 "98% 수준"으로만 표기, 특정 기준 단정 금지 |
| 답변 화면 정상 출력률 100%의 검증 범위 | `extracted/2026_상반기종합평가.md`(L10), `extracted/이력서_20260624.txt`(L129) | confirmed — 400건 기준. 사용 시 "400건 발화 검증 기준" 스코프를 항상 함께 표기 |
| FE 에러 0건의 측정 기간/범위 | `sources/연종합평가2025_정다훈.xlsx` | scope confirmation needed |
| 만족도 점수의 척도(5점 만점 여부) | `extracted/연종합평가2025_정다훈.md`(L18,25), `extracted/이력서_20260624.txt`(L127) | values confirmed (3,493명 검증, 사용성 4.18/만족도 4.06/완성도 4.05, "4점 이상" 목표). 명시적 "5점 만점" 문구는 원본에 없으므로 "5점 만점" 단정 금지 |
| 2025년 총 4.66억 매출과 세부 항목 4.6억의 차이 | `sources/연종합평가2025_정다훈.xlsx` | reconciliation needed |
| 신규 AI 챗봇 구축 기간 10주->2주 단축의 범위 | `experience-bank.md`(EXP-01 Metrics), headhunter-advisor 인터뷰 (user-attested 2026-07-23) | confirmed — 10주는 챗봇 최초 구현 기간, 2주는 신규 고객사(웰체크) 온보딩 시 Base-Theme을 활용한 FE 커스터마이징 납품 기간(FE 납품 기준, LLM/BE 일정 별도). 사용 시 이 스코프를 항상 함께 표기하고 "챗봇 전체를 2주 만에 구축"이라는 확대 해석 금지 |
| 2020.10~2022.05 내담씨앤씨 초기 프로젝트 상세 | `sources/이력서_20260624.pdf` | needs source detail |
