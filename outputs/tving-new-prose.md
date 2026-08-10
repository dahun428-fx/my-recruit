# tving-new-prose.md — 티빙(TVING) 이력서 변경분 companion

base-resume.md 대비 변경된 모든 줄을 3개 섹션으로 분류한다.
reviewer가 이 파일의 파티션 불변식을 전수 검사한다.

---

## (a) 신규 작성·수정된 산문 문장

### 헤드라인

- [수정] `웹·웹뷰 서비스의 성능 최적화와 AI 기반 개발 생산성 개선을 함께 다루는 Frontend Engineer`
  - base: `프론트엔드에서 풀스택, AI까지 확장해 온 Product Engineer`
  - 변경 근거: 소유자 승인 헤드라인 (target-companies.md 기재)

### 요약 (전체 재작성)

- [수정] `6년차 프론트엔드 개발자. React·Next.js 웹·웹뷰 서비스의 성능 최적화부터 AI 기반 개발 프로세스 개선까지 함께 다루는 Frontend Engineer입니다. 미디어 쿼리 기반 반응형 웹, WebView 호환성 검증, GitLab MR·AI 코드 리뷰를 실무로 운용했고, AWS S3·EC2 배포 파이프라인을 활용·운영하며 FE 역할 범위를 API·배포까지 이해하는 방식으로 확장해 왔습니다. 대규모 트래픽 서비스의 웹·웹뷰 사용자 여정을 성능과 품질 자동화로 뒷받침하는 환경에서 이 역량을 더 깊이 발전시키고 싶습니다.`
  - base: `6년차 풀스택 개발자. React·Next.js 프론트엔드부터 Node.js·Spring Boot·MySQL·AWS까지 모든 계층에서 아키텍처를 설계하고 개발하는 Product Engineer입니다. 프론트엔드 개발자로 커리어를 시작해 풀스택으로 영역을 넓혔고, 현재는 프롬프트 → 컨텍스트 → 하네스 엔지니어링으로 Claude·Codex 활용을 단계적으로 심화하며 팀의 AX 전환을 리드하고 있습니다.`
  - 변경 근거: FE 정면 포지셔닝. 풀스택/백엔드 전면 제거, WebView·반응형·GitLab MR·AWS 활용 신호 추가. "6년차 프론트엔드 개발자"로 포지션 어구 변경.
  - [Fix 4 — 점수 게이트 1R] 요약 말미 티빙 연결 문장 1문장 추가(초안): `대규모 트래픽 서비스의 성능 안정성과 웹·웹뷰 사용자 경험을 함께 다루는 환경에서 이 역량을 더 깊이 발전시키고 싶습니다.`
  - [Fix 3 — 점수 게이트 2R] 동기 문장 강화 — Company signals(웹·웹뷰 사용자 여정·품질 자동화) 차용으로 교체: `대규모 트래픽 서비스의 웹·웹뷰 사용자 여정을 성능과 품질 자동화로 뒷받침하는 환경에서 이 역량을 더 깊이 발전시키고 싶습니다.` — 합니다체, S-01 금지어 미사용, 티빙 사명 직접 언급 없음, 1문장.

### 경력기술서 1번 성과 — 스코프 병기 (점수 게이트 1R Fix 2 + 2R Fix 1, Fix 2)

- [수정] `실사용 **발화 400여 건 검증 전체 통과**, SSE·React Query 캐싱 설계로 AI 응답 평균 2초대(네트워크 수신 기준)·Lighthouse 91점(AI 챗봇 화면 기준)`
  - base: 동일 문장에서 `AI 응답 평균 2초대` (스코프 미병기), `Lighthouse 91점` (스코프 미병기)
  - 1R Fix 2: `AI 응답 평균 2초대(네트워크 수신 기준)` — EXP-01 Metrics 기준, metric-registry needs_scope 준수 (C-05)
  - 2R Fix 1: `Lighthouse 91점(AI 챗봇 화면 기준)` — metric-registry needs_scope 준수; "5점 만점" 등 원본 없는 척도 미부가

- [수정] `Vitest 약 2,600케이스·Playwright E2E로 **반복 QA 3시간 → 30분**, PostHog·Web Vitals 기반 사용성 4.18점·만족도 4.06점(2차 PoC 검증 기준) 확보`
  - base: `사용성 4.18점·만족도 4.06점` (스코프 미병기)
  - 2R Fix 1: `(2차 PoC 검증 기준)` 추가 — EXP-01 Metrics "2차 PoC 검증 기준" 그대로. "5점 만점" 척도 미부가.

### 경력기술서 2번 제목 변경

- [수정] `2. 대웅제약 | 팀 AX 전환 리드 — AI 개발 프로세스 개선`
  - base: `3. 대웅제약 | 팀 AX 전환 리드 — 하네스 엔지니어링과 개발 표준화`
  - 변경 근거: JD 담당업무 1번 "AI 기술 활용 개발 프로세스 개선" 키워드 직결

### 경력기술서 2번 [주요 업무] 변경

- [수정] `[주요 업무]: 팀의 AI 활용 개발 방식 전반을 설계·리드 — AI 생성 코드 검증을 위한 하네스 엔지니어링 구축, FE AX 개발 표준 단독 설계, GitLab MR 기반 AI 코드 리뷰 도입, 품질·운영 자동화와 팀 지식 자산화 주도`
  - base: `[주요 업무]: 팀의 AI 활용 개발 방식 전반을 설계·리드 — AI 생성 코드 검증을 위한 하네스 엔지니어링 구축, FE AX 개발 표준 단독 설계, 품질·운영 자동화와 팀 지식 자산화 주도`
  - 변경 근거: GitLab MR + AI 코드 리뷰 명시 추가 (JD 코드 리뷰 문화 요건 정면 대응)

### 경력기술서 2번 주요 실행 — GitLab MR 불릿 신규 추가 (적대 검증 수정 반영)

- [신규] 불릿 `**GitLab MR 기반 AI 코드 리뷰 도입**` 전체:
  > GitLab MR 양방향 코드 리뷰(작성자·리뷰어 모두 수행) 문화에 **AI 코드 리뷰 도구를 MR 흐름에 편입해 활용**
  - 근거: EXP-03 user-attested 2026-08-10 (GitLab MR 양방향 코드 리뷰 + AI 코드 리뷰 도입)
  - ※ 초안의 "생성 코드의 금지 패턴·보안 기준 검증을 자동화" 삭제 — AI 도구 도입(attested)과 SOP 문서화(별개 사실)를 융합한 무근거 주장이었으므로 제거. 금지 패턴·보안 기준은 FE AX 개발 표준 불릿(base 서사)에 귀속 유지.

### 경력기술서 3번 [주요 업무] 변경

- [수정] `[주요 업무]: 2019년 레거시 검진 서비스를 React 기반 임직원 건강검진 통합플랫폼으로 현대화 — 서비스·DB 구조 분석부터 점진 전환 설계, MySQL·Spring Boot·REST API·화면 End-to-End 개발, 배포 자동화, WebView 호환성 검증까지 풀스택 총괄`
  - base: `[주요 업무]: 2019년 레거시 검진 서비스를 React 기반 임직원 건강검진 통합플랫폼으로 현대화 — 서비스·DB 구조 분석부터 점진 전환 설계, MySQL·Spring Boot·REST API·화면 End-to-End 개발, 배포 자동화까지 풀스택 총괄`
  - 변경 근거: WebView 호환성 검증 명시 추가

### 경력기술서 3번 주요 실행 — 배포 자동화 불릿 변경 (MF-1 수정 반영)

- [수정] 배포 자동화 불릿 끝에 추가:
  > **WebView 호환성 검증 기준 수립**, 반응형 웹(미디어 쿼리 기반 PC/모바일 대응) 적용
  - 근거: EXP-02 user-attested 2026-08-10 (반응형 웹 / WebView)
  - ※ 초안에 있던 "AWS 배포 파이프라인 활용" 불릿은 귀속 오류로 제거 — AWS S3·EC2는 EXP-06 바이오에이지 귀속. 대신 경력 섹션 대웅제약 불릿에 바이오에이지 귀속 명시로 ATS 커버리지 유지.

### 경력기술서 3번 기술 라인 (MF-1 수정 반영)

- [유지] `기술: React · TypeScript · Java · Spring Boot · REST API · MySQL · Node.js · Express · jQuery · Thymeleaf · Playwright · Jenkins · Docker · WebView`
  - AWS S3 · EC2 미포함 (귀속 오류 정정 — 바이오에이지 EXP-06 귀속이 맞음, 비즈36.5 귀속 아님)

### 경력기술서 4번 주요 실행 — 글로벌 요구 대응 불릿 변경

- [수정] `i18next 기반 **영·중·일 다국어 구조와 SEO 대응**, **Lighthouse·GA·Adobe Analytics·Datadog으로 성능·SEO·오류 지표화**, **Vercel 배포 자동화**, 미디어 쿼리 기반 PC/모바일 반응형 웹 적용`
  - base: `i18next 기반 **영·중·일 다국어 구조와 SEO 대응**, **Lighthouse·GA·Adobe Analytics·Datadog으로 성능·SEO·오류 지표화**, **Vercel 배포 자동화**`
  - 변경 근거: 반응형 웹 명시 추가 (EXP-05 user-attested 2026-08-10)

### 경력기술서 4번 성과 — 성능 개선 불릿 변경

- [수정] `유지보수·성능 개선 프로젝트에서 Lighthouse 병목 분석과 리소스 최적화로 **페이지 접근 시간 8초 → 2초 단축** / 월 방문자 약 112만(GA·Adobe Analytics 기준) 서비스`
  - base: `유지보수·성능 개선 프로젝트에서 Lighthouse 병목 분석과 리소스 최적화로 **페이지 접근 시간 8초 → 2초 단축**`
  - 변경 근거: 월 방문자 112만 규모 추가 (EXP-05 user-attested 2026-08-10, 스코프 "GA·Adobe Analytics 기준" 병기 필수 — 지시사항)

---

## (b) 재사용한 candidate 상태 뱅크 라인

(해당 없음 — canonical-lines.md 조회 결과 candidate 상태 라인 재사용 없음. base에서 직접 승계하거나 신규 산문으로 처리.)

---

## (c) 신규·변경된 비산문 콘텐츠 라인

### 인적사항

- [수정] 포지션: `Frontend Engineer` (base: `Full-stack Product Engineer`)
- [수정] 경력: `총 5년 10개월` (base: `총 5년 9개월` — 2020.10~2026.08 재계산)

### 핵심 성과 섹션 전면 재편

- [수정] ① 타이틀·칩·근거 전체:
  - 타이틀: `① 성능 최적화 · 대규모 서비스` (base: `② 대규모 레거시 전환`)
  - 칩: `성능 개선 주도 · 반응형 웹 · 대규모 B2B 커머스 · SSR·CSR 렌더링 전략`
  - 근거 (최종): `**페이지 접근 8초 → 2초 단축** · 글로벌 B2B 커머스 전면 전환 · 월 방문자 약 112만(GA·Adobe Analytics 기준)`
  - [Fix 5 — 점수 게이트 1R] 근거 줄에 "글로벌 B2B 커머스 전면 전환 ·" 추가 — 112만 수치 변경 없음, 칩의 "대규모 B2B 커머스"와 연동해 규모 맥락 가시화.
  - [Fix 4 — 점수 게이트 2R] 근거 줄 과부하 축소 — "평균 로딩 약 50% 개선" 및 "대시보드 렌더링 2.5초→1초대" 제거. 두 수치는 경력기술서 4번(미스미 성능 개선)·5번(삼성물산 대시보드)에 각각 보존 — 문서 전체 정보 손실 없음.
- [수정] ② 타이틀·칩·근거 전체 (MF-2 수정 반영):
  - 타이틀: `② WebView 기반 플랫폼 운영` (base: `③ 대용량 데이터 렌더링·쿼리 성능 설계`에서 내용 교체)
  - 칩: `모바일 WebView · iOS/Android 호환성 검증 · 배포 자동화 · 풀스택 End-to-End`
  - 근거: `**108개 페이지 9주 단독 내재화**, 미디어 쿼리 반응형·WebView 호환성 검증 / 매출 1.0억 기여`
  - ※ "반응형·WebView 구조 완비" → "미디어 쿼리 반응형·WebView 호환성 검증"으로 완화 — user-attested 범위(미디어 쿼리 PC/모바일 대응, WebView 호환성 검증) 내 표현으로 조정, "완비" 단정 삭제
- [수정] ③ 타이틀·칩·근거 전체:
  - 타이틀: `③ AI 개발 프로세스 · 공통 모듈` (base: `④ 소통과 기술 리더십`)
  - 칩: `AI 기반 개발 표준화 · GitLab MR + AI 코드 리뷰 · Playwright CI 게이트 · Config-Driven UI`
  - 근거: `Playwright E2E 하네스 단독 구축, **팀 10명 전원의 개발 절차로 정착**, **세미나 12회·기술 문서 48건**`
- [수정] ④ 타이틀·칩·근거 전체:
  - 타이틀: `④ AI 챗봇 제품화 · 비즈니스 임팩트` (base: `① AI 건강검진 챗봇 제품화`에서 순서 이동·칩 교체)
  - 칩: `FE 아키텍처 분석·설계·구현 전 과정 주도 · SaaS 확장 구조 · SSE 실시간 스트리밍`
  - 근거: `**임직원 3,493명 실사용**, 신규 고객사 **FE 커스터마이징 2주 납품 — 최초 구현 10주 대비**`

### 경력 섹션

- [수정] 대웅제약 직무 라인: `Frontend Engineer / 비즈36.5·AI코치·바이오에이지 신규 개발 및 유지보수 / 팀 AX 전환 리드`
  - base: `풀스택 Product Engineer / 비즈36.5·AI코치·바이오에이지 신규 개발 및 유지보수 / 팀 AX 전환 리드`
- [수정] 대웅제약 경력 AX 전환 리드 불릿: `**AX 전환 리드** (Claude Code·Codex·GitLab MR·AI 코드 리뷰·하네스 엔지니어링)`
  - base: `**AX 전환 리드** (Claude Code·Codex·Harness Engineering)`
- [신규] 대웅제약 경력 AWS 불릿 (MF-1 수정 — 바이오에이지 귀속 명시):
  `바이오에이지 서비스 **AWS S3·EC2 배포 파이프라인 활용·운영**`
  - 근거: EXP-06 user-attested 2026-08-10 (AWS S3·EC2 활용·운영, 동사 "구축" 금지)
- [수정] 내담씨앤씨 미스미 불릿 — 반응형·WebView 신호 추가:
  `한국미스미 **Global B2B 커머스 신규 개발과 레거시 전환**, 반응형 웹·다국어·SEO 대응, **일본 본사와 일본어 직접 협업** (PHP·jQuery → Next.js·TypeScript)`
  - base: `한국미스미 **Global B2B 커머스 신규 개발과 레거시 전환**, **일본 본사와 일본어 직접 협업** (PHP·jQuery → Next.js·TypeScript)`
- [복원 — 적대 검증 C-1] 내담씨앤씨 삼성물산 불릿 — base 문면 복원:
  `**삼성물산 사내 웹·앱 플랫폼 신규 개발·유지보수** (Vue 3·React Native·Spring·Oracle)`
  - 초안에서 삽입했던 "WebView·앱 플랫폼", "반응형 WebView 호환성 검증" 제거. EXP-04에 WebView·반응형 근거 없음 — 2026-08-10 user-attested 반응형은 EXP-02·EXP-05 귀속.

### 경력기술서 목차

- [수정] 목차 순서 전면 변경:
  `1. 대웅제약 AI 건강검진 챗봇 제품화 / 2. 대웅제약 팀 AX 전환 리드 — AI 개발 프로세스 개선 / 3. 대웅제약 임직원 건강검진 통합플랫폼 구축 / 4. 한국미스미 글로벌 B2B 커머스 Next.js 전면 전환 / 5. 삼성물산 대용량 데이터 플랫폼·모바일 고도화`
  - base 순서: 1(챗봇) / 2(통합플랫폼) / 3(AX 전환) / 4(삼성물산) / 5(미스미)
  - 변경 근거: JD 담당업무 1번(AI 개발 프로세스 개선) 대응을 위해 AX 전환 항목을 2번으로 전진; 미스미 성능·대규모를 4번에서 상위 배치

### 경력기술서 2번 기간 표기 (점수 게이트 2R Fix 5)

- [수정] 기간: `2026.01 ~ 2026.06` (base·이전 draft: `2026년 상반기`)
  - 변경 근거: 상반기의 정의역(1월~6월)을 월 단위 표기로 통일 — 신규 사실 없음, 다른 경력기술서와 형식 일치

### 경력기술서 2번 기술 라인

- [수정] `기술: Codex · Claude Code · GitLab MR · AI 코드 리뷰 · Playwright · Storybook · Jest · ESLint · TypeScript · GA4 · PostHog · Jenkins · GitLab CI/CD`
  - base: `기술: Codex · Claude Code · Playwright · Storybook · Jest · ESLint · TypeScript · GA4 · PostHog · Jenkins · GitLab CI/CD`
  - 변경 근거: GitLab MR · AI 코드 리뷰 토큰 추가

### 기술 섹션 전면 재편 (카테고리 순서·내용)

- [수정] 기술 표 전체 — 카테고리 순서를 JD 연관도 순으로 재편:

| 구분 | 기술 |
| --- | --- |
| 프론트엔드 | React · Next.js · Vue 3 · React Native · TypeScript · JavaScript |
| WebView·반응형 | WebView(iOS/Android) · 미디어 쿼리 · 반응형 웹 · SSR · CSR |
| AI 활용 개발 | Claude Code · Codex · GitLab MR AI 코드 리뷰 · SSE · LangChain · RAG · VectorDB |
| 공통 모듈·디자인 시스템 | Config-Driven UI · Base-Theme · Storybook · TanStack Query · Redux · Recoil · i18next |
| 품질·검증 | Playwright · Vitest · Jest · ESLint · Chromatic |
| 배포·인프라 | Jenkins · Docker · GitLab CI/CD · Vercel · AWS S3 · EC2 · Nginx |
| 백엔드 | Node.js · Express · Java · Spring Boot · Python · FastAPI · REST API |
| 데이터베이스 | MySQL · Oracle · PostgreSQL · MongoDB |
| 분석·관측 | Datadog · GA · Adobe Analytics · GA4 · PostHog · Lighthouse |
| 협업 | Figma · Jira · Slack · Confluence · Notion · Git · GitLab |

  - base 표 대비 주요 변경:
    - `AI 활용 개발` → `GitLab MR AI 코드 리뷰` 추가 (Harness Engineering 토큰 제거)
    - `WebView·반응형` 신규 카테고리 추가 (JD 요건 1순위 반영)
    - `공통 모듈·디자인 시스템` 카테고리 신설 (base의 `상태관리·데이터 페칭` + `UI·시각화` 일부 통합)
    - `상태관리·데이터 페칭` 카테고리 삭제, 항목은 `공통 모듈·디자인 시스템`으로 이동
    - `UI·시각화` 카테고리 삭제, ECharts·RealGrid 제거 (티빙 JD 비연관). i18next는 경력기술서 4번·경력 불릿과의 표-본문 일치를 위해 `공통 모듈·디자인 시스템` 행에 복원 (적대 검증 수정)
    - 카테고리 순서: 프론트엔드 → WebView·반응형 → AI 활용 → 공통 모듈 → 품질 → 배포 순 (JD 연관도 순)

---

## 연차 재계산 근거

- 2020.10 ~ 2026.08 = 5년 10개월 (base 2026.07 기준 5년 9개월에서 +1개월)
- "6년차"는 요약 산문에서만 허용, 수치 병기 금지 (JD 밴드 3~8년 정합)
