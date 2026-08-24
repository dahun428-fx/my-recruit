# Target Companies And Roles

Use this file for company-specific and role-specific notes. Keep research notes
separate from final application prose.

## Entry Template

```markdown
## Company / Role

- Source job posting:
- Application deadline:
- Target position:
- Role preset:       (fe-platform | ai-product | fullstack | fintech | commerce | ax-harness — see role-presets.md; 브리프 승인 시 확정)
- Required skills:
- Preferred skills:
- Company / team signals:
- Job scope:
- Candidate evidence to emphasize:
- Risks or gaps:
- Keywords to include:
- Screen profile:   (Balanced | AI-Product | Platform-DS | Scale-Perf — see screen-profiles.md; owner-approved)
- Pass bar:         (optional override of the default 80)
- Draft status:
```

`Screen profile:` and `Pass bar:` position the `recruiter-screen` /
`tech-screen` graders to this company (see
`docs/resume-reference/screen-profiles.md`). They are set only with owner
approval; an untagged entry is graded with `Balanced` at bar 80 plus a warning.

`Role preset:` links the entry to a targeting preset in
`docs/resume-reference/role-presets.md`. It is fixed when the owner approves
the targeting brief for the company; the brief's company-specific exceptions
are recorded in the entry so they feed back into the preset.

## Companies

Rows and sections marked `TBD` are placeholders and must not be used as source
facts in drafted application text.

### CJ ENM / [Mnet Plus] Frontend Engineer (경력)

- Source job posting: https://www.jobkorea.co.kr/Recruit/GI_Read/49425117 (JobKorea, 2026-06-27 확인)
- Application deadline: 2026.06.12 ~ 상시채용 (홈페이지 지원)
- Target position: Frontend Engineer / Product Engineer (서울 마포구 상암동, 정규직)
- Required skills: FE 4년+ · React 또는 Vue · JavaScript(ES6+)/TypeScript · Tailwind ·
  AI Coding Assistant 활용 · 생성형 AI 기반 개발
- Preferred skills: React·Vue 모두 실무 · Hybrid App · 디자인 시스템 구축 · 대규모 서비스 운영 ·
  테스트 자동화
- Job scope: AI 기반 개발 혁신(AI Front-end Harness, Markdown 개발 표준, AI Agent 프로세스, 테스트 자동화,
  생성형 AI 생산성) · FE 서비스 개발(React/Vue Web, Mobile Web/App, 반응형) · FE 플랫폼(공통 컴포넌트,
  디자인 시스템, 아키텍처)
- Skill set(공고 명시): React, Vue 3, Vite, TanStack Query, Tailwind4, AI Agent, 테스트 자동화(Vitest/Playwright)
- Company / team signals: "특정 기술 스택에 국한되지 않고 AI로 비즈니스 문제를 해결하는 Product Engineer 지향"
- Candidate evidence to emphasize: AI 챗봇 제품화·SSE·Markdown Renderer(↔ AI 개발 혁신/Markdown 표준),
  FE AX SOP·AI 생성 코드 검증(↔ AI Agent), Config-Driven UI·Base-Theme·Storybook(↔ 디자인 시스템),
  Playwright 600건 E2E(↔ 테스트 자동화), Vue 3·React Native(↔ React·Vue 모두/Hybrid App),
  글로벌 B2B 커머스 성능(↔ 대규모 서비스)
- Risks or gaps: Vite 실무 경험 없음(후보는 Next.js/Vercel) → 날조하지 않고 제외.
  Vitest 미사용 → Jest/Playwright로 사실 표기.
- Keywords to include: Product Engineer, React, Vue 3, TypeScript, Tailwind, TanStack Query,
  디자인 시스템, AI Agent/생성형 AI, 테스트 자동화, Hybrid App, 대규모 서비스
- Screen profile: AI-Product   (근거: "AI로 비즈니스 문제를 해결하는 Product Engineer 지향", AI 기반 개발 혁신 job scope)
- Draft status: 완료 — outputs/resume-career-cj-enm.{txt,html,css,pdf} (9p). reviewer+ats+Codex(2R) 통과.
  제출 전 사용자 확인 필요: 정보처리기사·TOEIC·JLPT 발급/취득일(needs_confirmation).

### NHN Dooray! / 프론트엔드 개발자 (경력)

- Source job posting: [URL 미확인 — 사용자 제공 JD 텍스트 기준, 2026-07-03 수집]
- Application deadline: [확인 필요]
- Target position: 프론트엔드 개발자 (경력) / 협업서비스개발실 (서비스 운영 포함)
- Required skills:
  - FE 및 유관 경력 6년 이상
  - 컴퓨터공학 전공 또는 준하는 지식
  - React·Vue·Angular 등 SPA 웹서비스 개발 경험
  - TypeScript 개발 경험
  - 협업·커뮤니케이션 능숙
- Preferred skills:
  - 성능 최적화 및 코드 품질 개선
  - 협업시스템 사용 경험
  - 빌드 프로세스 구축 경험
  - AI 활용·적용 경험
  - 학습·적용·공유에 적극적
- Company / team signals:
  - 올인원 협업 도구(메일/프로젝트/위키/메신저/캘린더/AI + 전자결재/게시판/ERP), 공공·교육·민간 고객사
  - 구축형(설치형)과 SaaS 모두 제공, 글로벌 통합 SaaS 지향
  - 협업서비스개발실은 협업 부분(프로젝트/메일/캘린더/메신저/AI) 개발·운영, 안정적 서비스 운영 중시
  - 수평적 소통, 직급보다 논리, 고객 업무 흐름·페인포인트 관찰, AI 트렌드 분석·적용 중시
- Job scope:
  1. Dooray! 서비스 프론트엔드 개발 및 운영
  2. 구축형 유지보수
  3. 디자인시스템 등 신규 컴포넌트 개발 및 유지보수
  4. AI 기능 서비스에 도입
- Candidate evidence to emphasize:
  - React·Vue 3·TypeScript 기반 SPA 개발 (→ 자격요건: SPA 개발 경험)
  - Config-Driven UI·Base-Theme·Storybook 기반 공통 컴포넌트·디자인시스템 구조 (→ 주요업무 3)
  - 고객사별 CI·메뉴·기능 노출 정책 관리, 레거시 점진 전환, 1주 내 배포 대응 구조 (→ 주요업무 2 구축형 유지보수)
  - SSE 기반 실시간 응답·Markdown 렌더링·오류 가드레일 실서비스 도입 (→ 주요업무 4 AI 도입)
  - Playwright 600건 E2E·Jenkins·GitLab CI/CD·Vercel 배포 자동화 (→ 우대사항: 빌드 프로세스)
  - 미스미 8초→2초, 삼성물산 2.5초→1초대, 챗봇 30초→6초 성능 개선 (→ 우대사항: 성능 최적화)
  - 개발 세미나 12회·기술 문서 48건·FE AX SOP 문서화 (→ 우대사항: 학습·적용·공유)
- Risks or gaps:
  - (a) 경력 연수: 자격요건 6년 이상 대비 후보 총 경력 약 5년 9개월 (2020.10~2026.07 기준). 이력서에 "6년차"로 표기하되 기간 수치는 정확히 표기. 면접 시 경력 연수 질문에 대비 필요.
  - (b) 컴퓨터공학 비전공: 성공회대 일어일본학과+경영학 복수전공. 정보처리기사(2020.08)와 응용SW엔지니어링 교육과정(2020.03~09)으로 보완하나, 전공 우대 항목의 직접 충족은 어려움.
  - (c) Angular 무경험: 자격요건에 React·Vue·Angular 중 택일로 기재되어 있어 React/Vue로 충족 가능. 날조 금지, Angular 경험은 없음으로 표기.
  - (d) 협업툴 자체 구축 경험 없음: 그룹웨어·메신저·위키·캘린더를 직접 개발한 이력 없음. 대신 B2B 플랫폼 실시간(SSE)·다국어·권한/메뉴 정책·고객사별 배포 경험으로 전이 가능성 제시.
  - (e) "구축형(설치형)" 자체 경험 없음: experience-bank는 임직원 건강 플랫폼을 "SaaS형 기반"으로 규정. reviewer 검증 후 초안에서 "구축형 서비스 내재화" 표현을 "외주 서비스 내재화 + 고객사별 유지보수"로 정정. JD의 구축형 유지보수는 고객사별 배포·유지보수 경험으로 전이 어필하되, 설치형 경험을 있는 것처럼 쓰지 않음.
- Keywords to include:
  - React, Vue 3, TypeScript, SPA, 성능 최적화, 코드 품질, 디자인시스템, 공통 컴포넌트, Storybook,
  - 빌드 프로세스, Jenkins, GitLab CI/CD, Vercel, 구축형 유지보수, 레거시 전환, 고객사별 배포,
  - SSE, AI 기능 도입, Playwright, 테스트 자동화, 학습·공유
- Screen profile: Platform-DS   (근거: 협업 플랫폼 개발·운영, 디자인시스템/공통 컴포넌트 job scope, 안정적 서비스 운영 중시)
- Draft status (경력기술서): 초안 완료 + reviewer/ats 반영 — outputs/nhn-dooray-full-resume-draft.md.
  reviewer(팩트)·ats(키워드) 통과, 지적사항 반영: 미스미 기법(폰트 최적화 환원), 다국어 언어 일반화,
  2025 근거 지표(Jenkins 10→2분)를 2026 경력기술서에서 제거, 병역 표기 정리, "구축형→고객사별 유지보수"
  정정, 협업·커뮤니케이션 명시 보강. 독립 검증(Claude 서브에이전트 하드닝) 대기.
- Draft status (자기소개서): 완료 — outputs/nhn-dooray-cover-letter-draft.md. 참고 자소서(CJ ENM판) 스타일의
  제목형 5단 서술로 작성, JD 재타깃. reviewer(팩트, must-fix 없음)·ats(자격 5/5·주요업무 4/4·우대 4/5)
  ·Codex 2R 통과. 반영: CS 근거(정보처리기사·응용SW과정) 도입부 명시, 설치형·그룹웨어 직접개발 아님 정직
  방어, 6년 정밀수치 제거("6년차"만), 백엔드 범위를 FE 영향파악용으로 한정, AI 적용은 가능성 표현, 팀문화
  단정 완화. 미충족(면접 대비): 협업시스템(Jira 등) 직접 사용 근거 없음 → 날조 없이 제외. 제출 전 사용자
  확인: 정보처리기사·TOEIC·JLPT 발급/취득일. 분량 약 1,950자(다단 서술) — 800~1,000자 압축본 요청 시 별도 생성.
- 검증 상태 (Codex 2R 반영):
  - 정상 출력률 100%(400건 기준)·테스트 커버리지 98% 수준·만족도 4.18/4.06/4.05(3,493명 검증): 후보 본인
    공식 평가/이력서(연종합평가2025·2026상반기종합평가·이력서 extracted)에서 값·스코프 확인됨. 초안 문구가
    원본 스코프와 일치. 단, 커버리지 세부 기준(라인/브랜치)과 만족도 "5점 만점" 표기는 원본 미기재 —
    현행 문구("98% 수준", "만족도 조사 기준") 이상으로 단정 금지.
  - 자격/어학: TOEIC 825(2024.05)·JLPT 1급(2018.08)·병역(군필 육군 병장)은 이력서 extracted로 확인,
    profile.md 등재 완료. 정보처리기사는 취득월이 원본 미표기여서 초안에서 월 삭제(기관명만 표기).
  - eligibility risk(사용자 판단): 경력 5년 9개월 vs 자격요건 6년 이상. 초안은 정확 수치 표기, "6년차" 미사용.

### 두산로보틱스(주) / Fullstack Developer (경력)

- Source job posting: [URL 미확인 — 리멤버 채용공고, 사용자 제공 JD 텍스트 기준, 2026-07-04 수집]
- Application deadline: [확인 필요]
- Target position: Fullstack Developer / AI·SW 본부 신설팀 (로보틱스 SW 플랫폼 설계·개발·운영)
- Required skills:
  - TypeScript, Node.js, React 기반 서비스 개발 경험
  - gRPC, RESTful 또는 GraphQL API 설계 및 구현 경험
  - 모듈화된 코드 구조와 클린 아키텍처 이해
- Preferred skills:
  - WebSocket, gRPC, TCP/IP, UDP 등 실시간 통신 구조 구현 경험
  - Go 또는 Python, Node 기반 백엔드 경험
  - 다양한 프론트엔드 개발 경험 및 업무 자동화 경험
- Company / team signals:
  - 대한민국 협동로봇 1위·글로벌 4위, 5년 내 매출 1조원 목표(Organic/Inorganic 성장)
  - AI/SW 본부 신설팀: 로보틱스 SW 플랫폼 End-to-End 설계·개발·운영, 내부 생산성·시스템 효율 개선,
    자체 솔루션 구축, AI 활용 Agentic 솔루션·파이프라인·자동화 지향
- Job scope:
  1. 로보틱스 다양한 인터페이스 기반 최적화 SW 구현
  2. 백엔드(API·데이터 파이프라인)부터 프론트엔드(React UI)까지 전체 스택 설계·구현
- Candidate evidence to emphasize:
  - React·TypeScript FE + Spring Boot·MySQL·REST API BE를 DB→API→화면 End-to-End 개발 (→ 전체 스택)
  - REST API·필터링/정렬·역할별 조회 로직 설계 (→ 자격요건: API 설계·구현)
  - Config-Driven UI·Base-Theme·공통 컴포넌트·Custom Hook·레이어드 데이터 흐름 (→ 자격요건: 모듈화·클린 아키텍처)
  - SSE 기반 실시간 LLM 스트리밍·오류 가드레일 실서비스 도입 (→ 우대: 실시간 통신 구조, 전이 경험)
  - Playwright 600건 E2E·Jenkins/GitLab CI/CD·FE AX SOP·AI 생성 코드 검증 (→ 우대: 다양한 FE + 업무 자동화)
- Risks or gaps:
  - (a) Node.js: user-attested(2026-07-05)로 비즈36.5에서 React 프론트 전용 BFF를 Express로 신규 구축(팀 공동)한 사실 확인됨 → 이력서 반영. 단 "Spring Boot 대체"·"Node 단독 백엔드 전면"은 아니므로 "신규 BFF 구축" 범위로만. 문서 근거 미확보라 면접 대비 필요.
  - (b) gRPC / GraphQL: 무경험. REST 설계 경험으로 제시하고 gRPC/GraphQL은 주장하지 않음.
  - (c) WebSocket / TCP/IP / UDP: 무경험. SSE 실시간 경험으로 인접 표현만.
  - (d) Python: user-attested(2026-07-05)로 AI 챗봇(Python) 서버의 프롬프트·응답 후처리 로직 일부 기여(팀 공동) 확인됨 → 이력서 반영. "Python 서버 구축/개발"은 아니므로 "로직 일부 기여" 범위로만. Go는 무경험 — 제외.
  - (e) 로보틱스 도메인 무경험: SW 플랫폼·자동화·실시간 관점의 전이 어필로 대응.
- Keywords to include:
  - TypeScript, React, Node(SSR), Fullstack, End-to-End, REST API 설계, 모듈화, 클린 아키텍처,
  - 실시간(SSE), 데이터 파이프라인, 업무 자동화, AI 활용, CI/CD, 테스트 자동화
- Draft status: 초안 완료 — outputs/doosan-robotics-full-resume-draft.md.
  reviewer 2회 + Codex 2R 통과, must-fix/날조 0건. 반영 내역:
  (1) Node.js(Express) BFF 신규 구축·Python AI 챗봇 응답 로직 일부 기여를 user-attested(2026-07-05) 범위로 정직 반영,
  (2) Backend/API 스킬을 숙련도 tier로 분리(주력 Java/Spring · Node BFF · Python 일부 기여),
  (3) "실시간 통신" 라벨 → "SSE 실시간 스트리밍"으로 정정(WebSocket/gRPC 오해 차단),
  (4) Python 표기에서 "서버의" 제거해 서버 구축 오해 차단,
  (5) 포지셔닝 하이브리드 확정 — H1 "Frontend 중심 Fullstack Developer" / 포지션 "Fullstack Developer(Frontend 중심)",
  (6) 비즈36.5(비즈케어) 명칭 통일, 커버리지 98%에 "(내부 측정 기준)" 출처 표기.
  제출 전 사용자 확인 필요: 만족도 4.18/4.06/4.05·커버리지 98% 수준(needs_scope), 정보처리기사·해외경험 발급/기간,
  BFF·Python 기여의 문서 증빙 부재(면접 대비용). 공고 URL·마감일 미확인.
  PDF 완성 — outputs/doosan-robotics-full-resume.{html,css,pdf} (9p, 페이지구조 정본 템플릿, millie-full-resume와 동일 형식:
  프로필 사진·info-box·페이지별 푸터 n/9·skill-block·경력기술서 project 블록). cj-enm-full-resume-draft.css 재사용,
  headless Chrome --print-to-pdf 렌더. scripts/render_doosan_resume.py는 정적 HTML 인쇄 전용. 자격증 취득월 미확인이라 날짜 미표기.
  다음 단계(선택): 자기소개서(gRPC/WebSocket/Go 갭 방어 서술).
  [2026-07-08 리포지셔닝] "FE-heavy 풀스택" 인상 제거 → "플랫폼형 풀스택"으로 재정렬. 제목 "API·데이터 흐름부터 React UI·배포
  자동화까지 구현하는 Fullstack Developer". 요약/핵심성과를 API·DB·BFF·자동화 우선으로 재배치(성능 최적화 항목은 핵심성과에서
  경력기술서로 이동). Node BFF를 "집계·프록시·프론트 요구 기반 응답"으로 구체화(검증 범위 내). SSE는 "단방향 이벤트 스트리밍·상태
  처리"로 전면 표기(WebSocket/gRPC 오해 차단). "클린 아키텍처 지향"→"계층 분리·의존성 정리". reviewer 통과. 미확인(추가하려면
  사용자 확인 필요): Node BFF의 인증/권한 연계·응답 스키마 표준화 — 실제 수행 시 핵심성과 #2에 추가하면 필수요건 방어력 상승.
  [2026-07-08] 사용자 요청으로 이력서(HTML/PDF/draft)에서 "팀 공동"·"팀과 함께" 표기 전부 제거, 내담 서술의 "(주요 프로젝트: 삼성물산…
  상세는 경력기술서)" 절도 제거. 단 실제 사실은 BFF·Python 모두 팀 공동이며, experience-bank 엔트리에 기록 유지 → 면접에서 협업 여부
  질문 시 정직하게 "팀 공동" 답변. 이력서 노출 문구에서만 생략한 것이므로, "정확성 위해 팀 공동 재추가" 같은 되돌림 금지.

### 넥스트증권 / 웹 프론트엔드 개발자 (경력)

- Source job posting: 사용자 제공 JD 텍스트 기준, 2026-07-22 수집 — URL 미확인
- Application deadline: [확인 필요]
- Target position: 웹 프론트엔드 개발자 (경력) / 내부 백오피스 + 고객 접점 홈페이지 담당
- Required skills:
  - 5년 이상 혹은 그에 준하는 웹 프론트엔드 개발 경험
  - 복잡한 데이터 구조를 다루는 관리자/운영 시스템 개발 경험 (테이블·폼·대시보드 등)
  - 웹 성능 최적화 및 크로스 브라우저 호환성 실무 경험
  - 주도적 커뮤니케이션·자기주도적 업무 수행
- Preferred skills:
  - React, TypeScript, Next.js, TanStack Query, Emotion, PNPM, Vite·ESBuild, GitHub Actions
- Company / team signals:
  - 내부 백오피스(원장·환전·이체 등 금융 운영 데이터 관리 및 워크플로우)
  - 파트너·외부 연동 플랫폼 DX 설계
  - 홈페이지 개편 및 B2C 제품 판매 플로우
  - 금융 데이터 기반 대시보드 및 테이블 최적화
  - 크로스 브라우저 호환성 및 반응형 웹 구현
- Job scope:
  1. 내부 백오피스 UI/UX 설계 및 핵심 기능 개발 (원장·환전·이체 등 운영 데이터 관리)
  2. 파트너·외부 연동 플랫폼 DX 설계 및 구현
  3. 홈페이지 개편 및 B2C 제품 판매 플로우 구현
  4. 내부 사용자 피드백 기반 기능 개선·유지보수
  5. 관리자 도구·데이터 조회·처리 인터페이스 개발
  6. 금융 데이터 기반 대시보드·테이블 최적화
  7. 크로스 브라우저 호환성·반응형 웹 구현
- Candidate evidence to emphasize:
  - 삼성물산 Vue 3·ECharts·RealGrid 대용량 데이터 대시보드(2.5초→1초대), 역할별 데이터 조회·필터·정렬 설계 → JD 최우선 요건(관리자/운영 시스템·테이블·대시보드)
  - B2B 임직원 건강 플랫폼 Web/Admin, 신규 기능 DB→API→Web/Admin End-to-End 개발 → 관리자 도구·데이터 조회·처리 인터페이스
  - 한국미스미 Next.js 전환 페이지 접근 8초→2초, 삼성 2.5초→1초대, AI 서비스 진입 30초→6초 → 성능 최적화
  - WebView 호환성 검증, 반응형/크로스 브라우저 직접 명시 근거는 약함 — evidence 범위 내 인접 어필만
  - React·Next.js·TypeScript·TanStack Query 실무 보유 → 스택 정면 매칭
  - Config-Driven UI·Storybook·BFF(집계·프록시 REST API) → DX 인접 어필(플랫폼 DX 직접 경험은 아님)
  - 기획·AI·백엔드·운영 조직 API 정책 조율, WBS·ETA 다중 우선순위, 운영팀 피드백 기반 개선 → 주도적 커뮤니케이션·자기주도
  - 미스미 B2B 커머스 홈페이지 개편·상품·주문·비교·멀티다운로드 → 홈페이지 개편·B2C 판매 플로우 전이
- Risks or gaps:
  - 경력 연수 충족: 자격요건 5년 이상 vs 총 5년 9개월. 이력서에 "총 5년 9개월"로 정확 표기. "6년차"는 요약 산문에서만 허용, 수치 병기 금지.
  - Emotion 무경험: 보유 스택 Tailwind CSS·SCSS로만 표기. Emotion/CSS-in-JS 경험 있는 것처럼 쓰지 말 것.
  - Vite·ESBuild 무경험: Next.js/Lighthouse 근거 내 번들 최적화 일반 경험으로만. Vite·ESBuild 보유처럼 쓰지 말 것.
  - PNPM·GitHub Actions 무경험: Jenkins·GitLab CI/CD 일반 경험으로 표기. PNPM·GitHub Actions 보유처럼 쓰지 말 것.
  - 금융/증권 도메인 무경험: 운영 시스템·대시보드·데이터 조회 전이 어필. 금융 도메인 경력 창작 금지 (자격요건 아님, 탈락 사유 아님).
  - 크로스 브라우저 직접 근거 약함: WebView 호환성 검증, Next.js 범용 SSR 구조 범위 내에서만 어필.
  - DX(파트너/외부 연동 개발자 경험) 직접 근거 없음: Config-Driven UI·공통 컴포넌트·BFF로 인접 어필만.
  - needs_scope 강지표(사용성 4.18·400건 출력률·커버리지 98%·매출 4.66억·FE 에러 0건)는 스코프 병기 없이 본문 강조 금지 (C-05).
  - Node.js BFF는 "신규 BFF 구축(집계·프록시)" 범위로만 (C-01: "팀 공동" 노출 금지).
- Keywords to include:
  - React, TypeScript, Next.js, TanStack Query, 관리자/운영 시스템, 백오피스, 데이터 대시보드, 테이블, 폼, 성능 최적화, 크로스 브라우저, 반응형 웹, CI/CD, 주도적 커뮤니케이션, 역할별 데이터 조회, End-to-End, 홈페이지 개편
- Draft status (이력서): 완료 — outputs/next-securities-full-resume-draft.md. tailor 작성 → reviewer(팩트, must-fix 반영: Datadog 중복·리드타임 오타·삼성물산 SI 소속 병기)·ats(필수 4/4·필수 스택 4/4) 통과. 스코어 게이트: 인사 72→86·기술 84 둘 다 PASS. Emotion·Vite·ESBuild·PNPM·GitHub Actions는 무경험으로 정직 제외. 제출 전 사용자 확인: 어학(TOEIC/JLPT) 포함 여부(넥스트증권 요구 시)·정보처리기사 2020.08 병기 완료. Codex 미사용(P-02). PDF 렌더는 다음 단계.
- Draft status (자기소개서): 완료 — outputs/next-securities-cover-letter-draft.md. 제목형 5단(F-06). reviewer(팩트, must-fix 0)·ats(필수 7/7) 통과. 스코어 게이트: 인사 78→80.3·기술 74→81.5 둘 다 PASS(2라운드). 반영: 대시보드 스택(Vue 3·ECharts·RealGrid) 정합화, TanStack Query 실사용 서사, WebView·크로스브라우저 연결, 홈페이지·B2C 동기 축, 비즈니스 임팩트·Lazy Rendering 트레이드오프. 갭(금융 도메인·Emotion·Vite·PNPM·GitHub Actions·크로스브라우저) 정직 방어. 면접 대비: Node BFF·Python 팀 공동, DX 직접 근거 없음.

### 카카오페이증권 / MTS 프론트엔드 ('제대로 투자하다') (경력)

- Source job posting: 사용자 제공 JD 텍스트 기준, 2026-07-22 수집 — URL 미확인
- Application deadline: [확인 필요]
- Target position: 카카오페이증권 MTS(주식 모으기·펀드·주식 선물하기·프로모션 등) 프론트엔드 개발·운영, 기술 리딩 성격
- Required skills:
  - 프론트엔드 7년 이상, SDLC 개발·운영·고도화
  - React·Next.js·TypeScript·TanStack Query·웹소켓·웹뷰 기반 FE
  - FE 3~5인 중규모 팀 리드·멘토링
  - SSR·CSR 등 다양한 렌더링, 대규모 트래픽 대응
  - 관측성 도구(OpenTelemetry·Grafana·OpenSearch·Sentry)
  - 단위 테스트·e2e 테스트
  - LLM 기반 AI 도구(Cursor·Claude) 실무 적용·팀 도입
  - 협업 도구(Slack·Figma·Jira·Confluence)
- Preferred skills: 트레이딩 시스템(MTS·HTS)·금융 서비스 개발, 문제 분해·주도적 실행, 실패 학습 문화, 효율성·생산성 개선, 오픈소스 기여·컨퍼런스 발표
- Company / team signals: 소액·저경험 사용자의 금융 접근성 확대, PM·디자인·BE·FE 목적 조직, 사용성·기술 리스크 사전 예측·구조 개선의 기술 리딩
- Candidate evidence to emphasize:
  - 웹뷰 환경 React 화면 운영·iOS/Android 호환성 검증 (→ 웹뷰 기반 FE)
  - SSE 기반 실시간 LLM 스트리밍·중지/재시도/오류 상태 처리 (→ 실시간, 웹소켓 인접)
  - 미스미 Next.js SSR·CSR 전략 분리·8초→2초 (→ SSR·CSR)
  - Playwright 600여 건 E2E·Jest 단위 테스트·커버리지 98% 수준 (→ 단위·e2e 테스트)
  - Cursor·Claude LLM 도구 실무 적용·FE AX SOP 문서화·세미나 12회 (→ LLM 도구 팀 도입, 멘토링)
  - Datadog·GA4·PostHog·Lighthouse 기반 지표 분석·개선 (→ 관측성 인접)
- Risks or gaps (사용자 확정 2026-07-22 — 정직한 상향지원으로 진행):
  - (a) 경력 7년 요구 vs 총 5년 9개월(약 1년 3개월 미달). 이력서는 "총 5년 9개월" 정확 표기, "7년차" 미사용. 자소서에서 연차 대신 경험 밀도로 상쇄. 사용자: "실경력은 모자라지만 지원."
  - (b) 웹소켓: 실무 무경험, **사이드 프로젝트로 직접 구현·학습(user-attested 2026-07-22)**. 이력서 본문 미노출(C-06), 자소서에서만 "실무는 SSE 단방향, 웹소켓 양방향은 사이드 프로젝트로 구현·학습"으로 정직 표기. "실무 웹소켓 경험" 주장 금지.
  - (c) FE 3~5인 팀 리드 직함 미확인. 세미나·SOP·기준 수립으로 멘토링/기술 리딩만 표기, 인원수·직함 주장 금지.
  - (d) 금융/트레이딩 도메인 무경험(사용자 수용). 인접 역량(실시간·웹뷰·관측성·B2B 다국어/권한) 전이 어필, 도메인 경력 창작 금지.
  - (e) 관측성 특정 도구(OpenTelemetry·Grafana·OpenSearch·Sentry) 미보유. 보유 도구(Datadog 등)로 "관측성 기반 개선" 방법론만 어필, 특정 도구 보유 위장 금지.
  - (f) 협업 도구(Jira·Confluence·Figma·Slack) evidence base 미기재 → 이력서 미노출. 실무 사용 여부 [확인 필요].
  - (g) needs_scope 지표(출력률 100%·커버리지 98%) — 사용자 확정 2026-07-22: 스코프 병기해 **유지**(쿠팡 전례 동일).
- Screen profile: [미지정 — Balanced로 채점됨, 경고]. MTS 특성상 Scale-Perf 또는 AI-Product 검토 여지(소유자 승인 필요).
- Keywords to include: React, Next.js, TypeScript, TanStack Query, 웹뷰, SSR·CSR, 실시간, SSE, 단위·e2e 테스트, Playwright, Jest, LLM 도구, Cursor, Claude, 관측성, 멘토링
- Draft status (이력서): 완료 — outputs/kakaopay-securities-full-resume.{md,html,css,pdf} (9p, 정본 템플릿, headless Chrome 렌더). tailor 성격 작성 → reviewer(팩트, must-fix 3건 반영: 헤드라인 "금융" 삭제·"(보조)" 삭제·25% 괄호화)·ats(필수 9/12·우대 1/4) 통과. 점수 게이트: recruiter-screen 66·tech-screen 68 = 둘 다 FAIL(≥80 미달) — blocker 대부분이 구조적 실경력 갭이라 날조 없이는 80 불가, 사용자가 정직한 상향지원으로 진행 확정. 독립 검증(Claude 서브에이전트 하드닝) 대기.
- Draft status (자기소개서): 작성 — outputs/kakaopay-securities-cover-letter-draft.md.

### 쿠팡 / 쿠팡이츠 웹 플랫폼 Staff Frontend Engineer (경력)

- Source job posting: [사용자 제공 JD 텍스트 기준, 2026-07-21 수집] — 쿠팡 본사 소속, 쿠팡이츠(음식 배달 O2O) 웹 플랫폼
- Application deadline: [확인 필요]
- Target position: Staff-level Frontend Engineer / 쿠팡이츠 웹 플랫폼 (PC·모바일 웹 아키텍처 설계·리드)
- Required skills:
  - 프론트엔드 엔지니어링 7년 이상
  - 웹 아키텍처 설계·구현 2년 이상
  - React·Vue·Node.js 등 웹 프레임워크 풍부한 지식·경험
  - 모바일/PC 웹 솔루션 풍부한 경험
  - 웹 애플리케이션 성능·생산성 향상 경험
  - 컴포넌트화·모듈화 설계 깊은 지식
- Preferred skills:
  - 빠르게 변화하는 환경에서 다양한 팀·다중 우선순위 업무 처리
  - E-commerce, O2O 도메인 근무 경력
- Job scope:
  - 쿠팡이츠 웹 플랫폼 전략·아키텍처 설계, 유연·효율적 PC/모바일 웹 아키텍처 구축
  - Product·UX·Backend·Mobile 팀과 협업해 프로젝트 리드
  - 새로운 고객 경험을 위한 웹 기능 구축·개발
  - (Staff) 팀 담당 웹 제품의 품질·생산성 제고, 팀 엔지니어의 아키텍처·디자인 가이드
- Candidate evidence to emphasize:
  - 한국미스미 Next.js 전환·SSR/CSR 분리·성능(8초→2초, 약 50%)·다국어·모니터링 (→ 웹 아키텍처 2년+·성능·E-commerce)
  - Config-Driven UI·Base-Theme·공통 컴포넌트·Custom Hook·Storybook (→ 컴포넌트화·모듈화)
  - React·Next.js·Vue 3·React Native·WebView (→ React·Vue·모바일/PC 웹)
  - Node.js(Express) BFF 신규 구축 (→ Node.js 프레임워크)
  - Playwright 600여 건 E2E·반복 QA 3→1시간·배포 10→2분·컴포넌트 90→15분·FE AX SOP·세미나 12회·문서 48건 (→ Staff 품질·생산성·가이드)
  - Product·UX·AI·백엔드 크로스팀 정책 조율·WBS/ETA 다중 우선순위 (→ 크로스팀 리드·빠른 환경)
- Risks or gaps:
  - (a) 경력 연수: 자격요건 7년 이상 대비 후보 총 경력 약 5년 9개월(2020.10~2026.07)로 약 1년 3개월 미달. 이력서에 "총 5년 9개월"로 정확 표기하고 "7년"·"7년차" 미사용. 가장 큰 서류 리스크 — 사용자 지원 여부 판단 필요. 날조 금지.
  - (b) Staff 레벨 직접 리드/멘토링: 다른 시니어 엔지니어를 직접 기술 리드·멘토링한 명시 이력은 evidence base에 없음. 세미나 12회·FE AX SOP·팀 기준 수립으로 간접 입증. 면접 대비 필요.
  - (c) O2O 도메인: 배달·O2O 플랫폼 직접 경력 없음(E-commerce는 미스미로 보유). 우대사항이므로 탈락 사유 아님, 면접 보완 논리 필요.
  - (d) Node.js BFF: user-attested(2026-07-05)·문서 근거 미확보·팀 공동. 이력서에는 "신규 BFF 구축" 범위로만 노출(C-01 준수), 면접 대비 필요.
- Keywords to include:
  - Frontend Engineer, 웹 아키텍처, PC·모바일 웹, React, Vue 3, Node.js, 성능 최적화, 생산성,
  - 컴포넌트화, 모듈화, Config-Driven UI, Base-Theme, Storybook, 크로스팀 협업, E-commerce, 다중 우선순위
- Draft status: 초안 완료 — outputs/coupang-eats-full-resume-draft.md.
  tailor 작성 → reviewer(팩트, blocking 0건)·ats(필수 5.5/6·우대 1.5/2) 통과.
  반영: S-01 금지어 "공통 구조 확보"→"공통 컴포넌트 구조 설계", "조직 자산화"→"정착" 완화, 다중 우선순위 신호 보강,
  E-commerce 근거 강화. needs_scope 지표(사용성 4.18·400건 출력률·커버리지 98%·매출 4.66억·FE 에러 0건)는 본문 미노출(레지스트리 준수).
  제출 전 사용자 확인 필요: (1) 7년 갭 하에 지원 여부, (2) needs_scope 강지표 스코프 병기 복원 여부(두산판 선례), (3) 정보처리기사·TOEIC·JLPT 발급/취득일.
  독립 검증(Claude 서브에이전트 하드닝)·PDF 렌더는 다음 단계.

### GS리테일 / AX본부 개발 프로젝트 (경력)

- Source job posting: 스크린샷 `C:\Users\jungdahun\Pictures\화면 캡처 2026-07-22 215251.png` (GS리테일 7월 경력사원 채용 공고 화면 캡처, 2026-07-22 수집)
- Application deadline: [확인 필요]
- Target position: AX본부 개발 프로젝트 트랙 (채용은 시스템 운영·개발프로젝트·Pricing 3트랙 중 이 지원은 개발프로젝트)
- Role preset: ax-harness (선택 근거: JD가 "AI 활용 프로토타입 구축·배포·운영", "과제 경험 재사용 표준화", "비개발 직군 수정·테스트 환경 설계", "하네스 엔지니어링" 등 ax-harness 신호 100% 일치. AI-product 프리셋과 유사하나, 서버리스 인프라 설계·운영 요건 및 GCP/AWS 직접 운영 요건이 ax 도메인 특수 요건으로 갭을 가짐)
- Required skills:
  - 경력: 최소 3년 최대 10년 이하 선호
  - GCP·AWS 기반 개발·운영 경험
  - DynamoDB, Lambda, S3 등 클라우드 인프라 직접 설계 및 운영 경험 보유
  - Python·SQL 기반 데이터 분석·가공 능력
  - Codex, Claude Code 활용 개발 및 Harness Engineering 경험 보유
- Preferred skills: [JD 명시 없음 — 자격요건이 곧 필수요건]
- Company / team signals:
  - GS리테일 AX본부: 현업 문제를 AI로 검증·해결하는 조직으로 보임
  - "비개발 직군이 직접 수정·테스트할 수 있는 환경" 강조 — 민주화·도구화 지향
  - "과제 경험을 재사용 가능한 표준으로 정리" — 지식 자산화 중시
  - "MECE 분해, 판정 기준 수립" — 구조적 문제 해결 방법론 명시
  - 하네스 엔지니어링 용어 명시 — AI 코딩 에이전트 기반 개발 문화
- Job scope:
  1. 현업과 함께 문제 정의 및 가설 기반 검증 설계 (MECE 분해, 판정 기준 수립)
  2. 하네스 엔지니어링 기반 프로토타입 구축 → 배포·운영
  3. 비개발 직군이 직접 과제를 수정·테스트할 수 있는 환경 설계
  4. 과제 경험을 재사용 가능한 표준으로 정리
- Candidate evidence to emphasize:
  - EXP-03: FE AX SOP·하네스 엔지니어링 기반 검증 기준 표준화, Codex·Claude Code 활용 개발 및 생성 코드 검증 절차 (→ JD 핵심: Harness Engineering, Codex·Claude Code 활용, 재사용 표준화)
  - EXP-01: AI 건강검진 챗봇 프로토타입 → 실사용 서비스 전환·배포·운영 (→ JD: 프로토타입 구축 → 배포·운영)
  - EXP-03: 운영 데이터 확인 절차 3단계→1단계, Storybook 기반 비개발 직군 독립 확인 환경 (→ JD: 비개발 직군 수정·테스트 환경 설계)
  - EXP-02: Jenkins CI/CD 배포 운영, AWS 연계 WebView 운영 경험 (→ JD: AWS 기반 운영, 인접 어필)
  - EXP-07: Python 프롬프트·응답 후처리 로직 기여, SQL·MySQL 데이터 구조 설계·쿼리 (→ JD: Python·SQL 데이터 분석·가공, 인접 어필)
- Risks or gaps (갭 인터뷰 2026-07-24 결과 반영):
  - [구조적 블로커 — 부분 해소] DynamoDB·Lambda·S3 직접 설계·운영: 갭 인터뷰 결과 **S3는 바이오에이지에서 활용(서버리스 환경 개발·배포·빌드), EC2도 활용**(user-attested 2026-07-24, EXP-06 적재). **DynamoDB·Lambda는 여전히 무경험** — 미주장/미기재 유지. S3·EC2 실사실 반영으로 tech 게이트가 이전 59(캡)→73으로 상승했으나, DynamoDB·Lambda·GCP 부재로 80은 날조 없이 불가.
  - [갭 확정 — 무경험] GCP: 갭 인터뷰 결과 **GCP 무경험 확정**(user-attested 2026-07-24). 이력서 미기재. 다음 지원에서도 재질문 불요.
  - [부분 해소] Python·데이터: 갭 인터뷰 결과 **VectorDB·RAG 구현 참여, Langchain 파인튜닝 경험, Python pandas 데이터 처리**(user-attested 2026-07-24, EXP-07 적재). 단 소유자 자평 "깊이는 깊지 않음" — "참여·기초" 톤 한정, 문서 근거 미확보(면접 대비).
  - 경력 연수: 총 5년 9개월(2020.10~2026.07). JD 선호 범위(3~10년) 이내 — 연수 리스크 없음.
  - Codex·Claude Code 활용 개발: EXP-03에서 확인됨 (user-attested 2026-07-22).
  - [면접 대비] 반복 QA 수치는 이력서에 문서값 3시간→1시간 사용(실측 2h→30분은 문서 미확보). 서버리스 깊이 질문엔 S3 정적 배포 기준으로 답변. RAG/파인튜닝 모델·데이터셋 상세 정리 권장. 2020.10~2022.05 내담 초기 ~1.5년 경력기술서 공백(채우려면 소유자 확인 필요).
- Keywords to include:
  - Harness Engineering, AI 코딩 에이전트, Codex, Claude Code, 프로토타입 구축·배포·운영, 재사용 표준, 판정 기준, MECE, 비개발 직군 환경 설계, AWS, GCP, Python, SQL, DynamoDB, Lambda, S3
- Screen profile: AI-Product (근거: ax-harness 프리셋의 Screen profile 제안이 AI-Product. JD가 "AI를 활용해 프로토타입을 배포·운영하고 재사용 표준으로 정리"하는 AI 제품화·하네스 엔지니어링 직무로, AI-Product 루브릭의 AI 제품화·구축 오너십·운영 깊이 축이 JD 핵심과 일치함)
- Pass bar: 80 (default)
- Draft status: **완료(정직한 상향지원본) — outputs/gs-retail-ax-full-resume.{md-draft,html,css,pdf} (10p, 정본 페이지 템플릿, headless Chrome 렌더).** full lane. 흐름: 갭 인터뷰(2026-07-24, S3/EC2·RAG/pandas 적재) → writer 재조립 → reviewer(팩트/무결성, must-fix 0)·ats(필수 8/13 강·2 약·3 정직갭) → 적대검증(fresh Claude, 서버리스 우산어·EC2 모순·RAG 톤 지적 반영) → 점수 게이트 **recruiter 71 / tech 73 둘 다 FAIL(bar 80, 블로커 0)** → P-01대로 구조적 블로커(GCP·DynamoDB·Lambda 실경력 부재, 날조 불가)로 3라운드 강행 대신 점수·블로커 보고, 소유자 "정직한 상향지원" 확정으로 진행 → 요약 서버리스 우산어 최종 정리 → 최종 무결성 재검(통과) → designer 렌더. companion: outputs/gs-retail-ax-new-prose.md. 이전 초안(ax-harness-engineering-resume-draft.md, 76/59캡)은 별도 파일로 보존. 자기소개서는 소유자 요청 시 이력서 확정 후 작성(서버리스·GCP 갭 정직 방어 서술). Codex 미사용(P-02). [2026-07-24 하우스 포맷 개정] 소유자 피드백 10건 반영 — 합니다체 전환·강점 볼드·요약 강점부각·섹션 재편(인적사항→요약→핵심성과→경력→기술→경력기술서→학력·교육·자격·어학)·헤드라인 축약·[주요 업무] 라벨·학력(여의도고)·교육(중앙에이치티에이) 추가. reviewer 재검 통과, designer 재렌더(12p). 이 피드백에서 하우스 규칙 승격: T-05(산문 합니다체)·F-07(섹션 순서)·F-01([주요 업무] 라벨)·F-03(헤드라인 간결) — feedback-rules.md.

### 스마일게이트 / [AI센터] AI 웹서비스 개발 담당 (경력)

- Source job posting: 사용자 제공 JD 텍스트 기준, 2026-08-04 수집 — 스마일게이트 채용 페이지
- Application deadline: 2026.08.31
- Target position: AI 웹서비스 개발 담당 (경력) / AI센터 — AX 포털 고도화 및 신규 AI 웹서비스 개발·운영
- Role preset: fullstack   (2026-08-04 브리프 승인. 승인된 예외: ①핵심 성과·기술 표에서 Java·Spring 상단 가시화 ②스마일게이트 AI센터 연결 동기 문장 추가 ③비전공 보완 신호(정보처리기사·Java 교육과정) 1페이지권 강화 ④EXP-01 AI 웹서비스 레이어를 fullstack 표준 순서보다 전진)
- Required skills:
  - 컴퓨터 관련 학과 대학교 졸업(학사) 이상
  - Java 개발 경력 3년 이상 (혹은 그에 준하는 역량)
  - Java / Spring Framework / Spring Boot 사용 경험
  - Java를 활용한 웹서비스 설계 및 개발 경험
  - Restful API 활용 경험
- Preferred skills:
  - React, Vue.js 등 JavaScript 기반 프론트엔드 기술 경험
  - UML 기반의 분석 설계 경험
  - DB 스키마 설계 경험
  - AI 서비스 프로토타입 개발에 관심
  - K8S, CI/CD에 관심
  - 신기술 도전에 두려움 없는 분
- Company / team signals:
  - AI센터: AX 포털 고도화 + AI 활용 웹서비스·서비스 플랫폼 비즈니스 구조 설계 및 개발
  - AI 기술을 탑재한 웹 기반 서비스 개발·관리
  - Java/Spring 백엔드 축 + React/Vue.js 프론트엔드 축의 풀스택 지향 조합
  - 스마일게이트: 글로벌 게임·엔터테인먼트 기업, AI센터는 내부 AX 플랫폼 성격
- Job scope:
  1. AX 포털 고도화 및 신규 기능 추가
  2. AI 활용 웹서비스 및 서비스 플랫폼 비즈니스 구조 설계·개발
  3. AI 기술을 탑재한 웹 기반 서비스 개발·관리
- Candidate evidence to emphasize:
  - EXP-02: Java·Spring Boot·MySQL·REST API End-to-End 개발, DB 스키마(MySQL 데이터 모델) 직접 설계 → 자격요건 정면 충족
  - EXP-04: Spring REST API 필터링·정렬·역할별 조회 설계, DB 인덱싱·DTO 투영 → Java/Spring 백엔드 실무 심도
  - EXP-01: React 기반 AI 웹서비스 구조 설계·개발·운영, AI 챗봇 제품화·SSE·LLM 서버 협업 → AI 웹서비스 개발 직접 부합
  - EXP-05: React/Next.js 프론트엔드 + Vue 3 경험 → 우대 FE 기술 충족
  - EXP-03: Jenkins CI/CD·GitLab CI/CD·Playwright E2E 파이프라인 → CI/CD 관심 신호
  - 정보처리기사(2020.08) + 웹 응용SW엔지니어링 교육과정(2020.03~09, Java 기반 웹 개발) → 컴공 비전공 보완 신호
- Risks or gaps:
  - [구조적 갭] 컴퓨터 관련 학과 요건: 성공회대 일어일본학과. 정보처리기사 + 응용SW엔지니어링 과정(Java 기반 웹 개발)으로 보완하나 직접 충족 아님. 이력서 상단 교육·자격 신호 강화 필요.
  - [갭 인터뷰 완료 2026-08-04] UML: 소유자가 실무 경험은 있다고 답했으나 **미기재로 결정** ("uml 실무 경험은 따로 쓰지말자") — 이력서·자소서에 쓰지 않는다.
  - [갭 인터뷰 완료 2026-08-04] Java 실무 기간: 소유자 확인 — 내담 초기 20개월(2020.10~2022.05)에 Java/Spring 실무가 있었음(세부 미제공, experience-bank 미적재·이력서 미기재 유지). **Spring 서사는 비즈36.5(EXP-02) 중심으로 싣기로 결정.** 3년 요건은 "그에 준하는 역량" 트랙 + 면접 방어.
  - [갭 인터뷰 완료 2026-08-04] K8S: 접점 없음 — 미기재, CI/CD 실무(Jenkins·GitLab CI/CD·Docker·Blue-Green)로만 우대 대응.
  - base 원본 채점 이슈: 이력서 상단 1/3에 "Java" 단어 자체 미노출(요약 스택 나열 부재), 동기·문화 신호 전무.
- Keywords to include:
  - Java, Spring Framework, Spring Boot, RESTful API, 웹서비스 설계·개발, DB 스키마 설계, MySQL, React, Vue.js, CI/CD, AI 웹서비스, AI 서비스, 풀스택
- Screen profile: Balanced   (2026-08-04 소유자 승인 — JD가 Java/Spring 스택 고정형이라 AI-Product 루브릭 부적합)
- Pass bar: 80 (default)
- Draft status: **완료 (2026-08-04)** — outputs/smilegate-full-resume.{html,css,pdf} (9p, 오버플로우 0, base 캐논 재사용).
  초안 outputs/smilegate-full-resume-draft.md + companion smilegate-new-prose.md.
  reviewer 3회(무결성 2·최종 1)·적대 검증 1회·게이트 3라운드: 인사 74→75.5→74.5 FAIL / 기술 72→77.5→83 PASS.
  AND 게이트 미통과(잔여 감점은 구조적: 비전공·Java 연수·내담 초기 공백, 날조 불가) →
  **소유자 결정: 정직한 상향지원으로 출고** (2026-08-04, 카카오페이·GS리테일 전례). 헤드라인 base 유지 확정(대안 A 미채택).
  후속(2026-08-04 소유자 지시): 요약 볼드 5곳 추가, 미스미 기간 라인 "3개 프로젝트" 제거(변형 한정),
  자기소개서 base 정본 합본 — outputs/smilegate-full-resume-with-self-intro.{html,css,pdf} (12p = 이력서 9p + 자소서 3p, 자소서는 base verbatim·타겟 편집 없음).

### 네이버웹툰 / 프런트엔드 개발자 (글로벌 웹 플랫폼) (경력)

- Source job posting: 사용자 제공 JD 텍스트 기준, 2026-08-10 수집 — NAVER WEBTOON Careers
- Application deadline: 2026.07.27 ~ 2026.08.17 (23:59)
- Target position: 프런트엔드 개발자 (경력) / 글로벌 웹 플랫폼 팀 — 웹툰CONNECT(창작자·비즈니스 파트너 포털: 원고 관리·정산·계약), 팬 커뮤니티 서비스, 라인망가 웹 서비스. 근무지 정자동 그린팩토리
- Role preset: fe-platform   (2026-08-10 그릴링 세션 승인. 승인된 예외: ①강조 순서를 프리셋 기본(EXP-01 선두)이 아닌 **경력 역순**(대웅 → 삼성물산 → 미스미)으로 — 소유자 지시 ②헤드라인·요약·핵심 성과에서는 미스미(EXP-05: 레거시→Next.js 아키텍처 개편·SSR·다국어·성능)를 리드 스토리로 ③일본어 협업 카드(JLPT 1급·무인양품 도쿄 근무)를 어학·요약에 명시)
- Required skills:
  - FE 개발 경력 4년 이상 혹은 그에 준하는 역량
  - React, TypeScript 능숙, Next.js 등 SSR 환경·Node.js 서버 사이드 동작 이해
  - 공통 컴포넌트 설계·코드 구조 개선
  - 복잡한 비즈니스 요구사항의 견고한 프런트엔드 모델링
  - 렌더링 성능·사용자 경험 품질
  - 기획·디자인·타 개발 조직과의 협업 리드
- Preferred skills:
  - 대규모 코드베이스 아키텍처 설계·구조 개편 주도
  - 정산·계약 등 복잡한 비즈니스 도메인
  - Cursor·Claude Code·Copilot 등 AI 도구·LLM API 실무 활용
  - Electron 등 웹 기술 기반 데스크톱 앱
  - EPUB·Canvas·WebGL 등 콘텐츠 뷰어·미디어 렌더링
  - Node.js BFF 개발·운영, Docker·K8s 컨테이너 배포
  - 다국어 서비스 개발, 영어·일본어 협업 커뮤니케이션
- Company / team signals:
  - 글로벌 콘텐츠 서비스(국내+일본+글로벌 팬), 일본 현지 기획·디자인 조직과 협업
  - 질문이 자연스러운 수평 문화, 스스로 문제를 과제로 만들어 설득·리드
  - 코드리뷰·기술 공유·스터디, AI 코딩 도구 적극 도입(AX 과제 발굴·주도)
  - Next.js SSR 서버가 BFF 역할, 사내 Docker 기반 클라우드 배포·모니터링 직접 수행
  - 전형 절차: 지원서 리뷰 → 프리 인터뷰 → 실무 인터뷰(코딩테스트 포함) → Culture-Fit 인터뷰 (2026-08-11 JD 전문 재확인으로 추가)
- Job scope:
  1. 웹툰CONNECT FE 개발·고도화 (원고 관리·정산·계약의 복잡한 요구사항 → 직관적 UX)
  2. 팬 커뮤니티·라인망가 웹 서비스 (다국어·다지역, 일본 조직 협업)
  3. Electron 기반 데스크톱 뷰어 (렌더링·캐싱·오프라인) — 참여 가능성 항목
  4. React·TypeScript·Next.js(SSR)+BFF 설계·개발·운영, Docker 배포·모니터링
  5. AI 도구·LLM 활용 AX 과제 발굴·주도
- Candidate evidence to emphasize:
  - EXP-05 미스미: PHP/jQuery 레거시 → Next.js/React/TypeScript 전환 주도, SSR·성능(8초→2초)·다국어·SEO·모니터링 → 필수(SSR·성능·아키텍처 개편) + 우대(대규모 개편 주도·다국어) 정면 대응. **리드 스토리**
  - EXP-01/03: Config-Driven UI·Base-Theme·공통 컴포넌트·Storybook, EXP-03 공통/로컬 판정 주체(3개 서비스 신규 화면 개발 시 본인이 개발 시점에 직접 판정, user-attested 2026-08-12)·회귀 방지 장치 3종(Storybook 스토리 확인·TypeScript 타입/빌드 검사·E2E(Playwright)·수동 회귀 확인) → 공통 컴포넌트 설계·코드 구조 개선. EXP-01의 "변경 이유가 같은 것만 공통화" 기준은 챗봇(EXP-01) 내부 UI 판단에 한정 — 3개 서비스 간 공통 레이어 판정 근거로 재사용 금지(EXP-01 68-75행 가드레일)
  - EXP-01·자소서 항목 3: 고객사별 기능·가격 정책의 제품 규칙화, 비즈36.5 권한·메뉴·정책 구조화 → 복잡한 비즈니스 요구사항의 FE 모델링 (정산·계약 도메인 전이 어필)
  - EXP-07: Node.js(Express) BFF 신규 구축 → Node BFF 우대 (C-01: "신규 BFF 구축" 범위)
  - EXP-02: Docker 기반 Blue-Green 무중단 배포·Jenkins → Docker 배포 요건
  - EXP-03: Claude Code·Cursor 실무, FE AX SOP·하네스, 세미나 12회·문서 48건 → AI 도구/AX 과제 정면 대응
  - EXP-06: 바이오에이지 CA(Electron) 유지보수 (user-attested 2026-08-10) → Electron 우대 한 줄
  - JLPT 1급(2018.08)·무인양품 도쿄 지사 근무·TOEIC 825 → 일본어 협업 우대 (라인망가·일본 조직)
- Risks or gaps:
  - 경력 4년+ 요건: 총 5년 10개월로 충족 — 연차 리스크 없음
  - [갭 인터뷰 완료 2026-08-10] Electron: 바이오에이지 CA 유지보수 실경험 확인(user-attested). 세부 범위 미확인 — "유지보수" 한 줄 노출만, IPC·패키징 등 단정 금지. 면접 대비 세부 정리 권장
  - [갭 인터뷰 완료 2026-08-10] Canvas·WebGL·EPUB: 무경험 확정 — 미기재. ECharts·RealGrid 대용량 시각화는 그대로 두되 "Canvas 경험"으로 표기하지 않음
  - [갭 인터뷰 완료 2026-08-10] 정산·계약 직접 경험 없음 — 비즈36.5 권한·메뉴·정책 구조화·EXP-01 요금제(기능별 차등 과금) 규칙화로 도메인 전이 어필만, 정산·계약 개발 이력 창작 금지 (2026-08-12 정정: "미스미 견적·주문"은 `experience-bank.md` EXP-05에 문자열 근거 없음을 확인 — 인사담당자 게이트 2라운드 R3 대응 세션에서 grep 무매치 확인 후 삭제. EXP-05가 문서화하는 복잡 기능은 "상품 비교·멀티다운로드"이며 견적/주문과는 다름)
  - K8s 무경험(2026-08-04 확정) — 미기재, Docker·Blue-Green 실무로만 대응
  - 웹툰·콘텐츠 도메인 무경험 — 우대 아님, 글로벌 B2B 커머스·다국어로 전이
  - [갭 인터뷰 완료 2026-08-12, 게이트 보완 라운드] 공통 컴포넌트 설계·코드
    구조 개선(필수 3번) 뒷받침용 기술 아키텍처 축: (1) 3개 서비스 신규
    화면 개발 시 공통/로컬 판정을 본인이 개발 시점에 직접 수행, (2)
    공통 컴포넌트 변경이 3개 서비스로 퍼질 때 Storybook 스토리 확인·
    TypeScript 타입/빌드 검사·E2E(Playwright)·수동 회귀 확인으로 회귀
    방지, (3) 공통 컴포넌트는 평면 구조 — 프리미티브/도메인 계층 구조·
    버저닝·서비스 간 채택률은 무경험 확정, 기재 금지(experience-bank.md
    EXP-03 362-375·424-429행 적재)
- Keywords to include:
  - React, TypeScript, Next.js, SSR, Node.js, BFF, 공통 컴포넌트, 디자인시스템, Storybook, 레거시 전환, 아키텍처 개편, 렌더링 성능, 다국어, i18n, 일본어, JLPT, Docker, CI/CD, Claude Code, Cursor, AI 도구, AX, Electron, 코드리뷰, 협업 리드
- Screen profile: Platform-DS   (2026-08-10 소유자 승인 — 공통 컴포넌트·아키텍처 개편·안정 운영 중심 JD)
- Pass bar: 80 (default)
- needs_scope 지표: 스코프 병기 유지 (2026-08-10 소유자 승인 — 두산·카카오페이 전례. base 자소서 verbatim에 수치 포함되므로 문서 간 정합 목적)
- 자기소개서: base 정본 verbatim 합본 (2026-08-10 소유자 승인 — 타겟 편집 없음, 스마일게이트 방식)
- Draft status: **확정·렌더 완료** (2026-08-12). fast lane으로 시작, 게이트 1R FAIL로 full lane 전환. 점수 게이트 3라운드(인사 77→74→79 / 기술 70.5→72→77) + 소유자 요청 보완 2라운드(갭 인터뷰 반영 79·77 / 최종 폴리싱 74·75.5) 모두 AND 게이트(80) 미통과 — 블로커·날조 0건, 잔여 감점은 구조적 갭(계층형 디자인시스템·정산·계약 무경험)과 채점 편차. **소유자 결정: 정직한 상향지원으로 출고** (2026-08-12 스톱 ② diff 승인 — 카카오페이·GS리테일 전례와 동일 처리). 최종 렌더: `outputs/naver-webtoon-resume.{html,pdf}` (9p). 보류 항목 소유자 확정: 요약 '약 50%' 표기 유지 / 요약 궤적 SSR→BFF 재작성 승인(base '불변' 규정의 회사별 예외) / 요약 3문단(동기·C-06 이탈 포함) 존치. **해소(2026-08-14 소유자 확정)**: 경력기술서 2 기간은 이 변형·은행 표기인 2025.11~2026.02가 정답이며, 티빙 최종본의 2026.01~2026.06은 오기였음을 소유자가 확인 — 레퍼런스 체크 대비 티빙 산출물(`outputs/tving-full-resume.pdf` 등) 재확인·정정 필요.

### 티빙(TVING) / Frontend Engineer — Web Core Development (경력)

- Source job posting: 사용자 제공 JD 텍스트 기준, 2026-08-10 수집 — 티빙 대규모 경력 채용
- Application deadline: 2026-08-17(월) 23:00 KST — 채용 완료 시 조기 마감 가능 명시
- Target position: Frontend Engineer / Web Core Development 단독 지원 (Player Development 미기입 — 소유자 확정 2026-08-10). PC Web·Mobile Web·App WebView 핵심 사용자 경험 개발·운영
- Role preset: fe-platform   (2026-08-10 브리프 승인. 생산 방식은 base-resume edit-from-base. 승인된 예외: ①EXP-05 미스미 성능·대규모를 EXP-02보다 전진 배치 ②WebView·반응형·GitLab MR·AWS를 자격요건 정면 대응으로 명시 ③AI 개발 프로세스(FE AX SOP·AI 코드 리뷰)를 담당업무 1번 대응으로 상위 노출)
- Required skills:
  - 웹 프론트엔드 3년 이상 8년 미만 — **후보 5년 9개월로 정합, 연차 리스크 없음**
  - 적정 기술·엔지니어링 역량 균형
  - 모바일 앱 웹뷰 기반 FE 개발
  - 반응형 웹 개발 경험
  - AWS 서비스 활용 경험
  - GitHub PR 코드 리뷰 문화
  - 협업 커뮤니케이션
- Preferred skills: AI 활용 비즈니스 임팩트, 대규모 트래픽 서비스, 실행 책임감, 팀 협업, 구조적 UI 설계·디자인 시스템
- Company / team signals: 대규모 스트리밍 플랫폼 성능 개선·글로벌 확장 아키텍처, 안정적 서비스 운영. Web Core: 회원·계정·구독·결제 사용자 여정, SEO, MFE 기반 Web Platform, CI/CD 자동화·성능 최적화·품질 관리 체계. 담당업무 1번이 "AI 기술을 활용한 개발 프로세스 개선". 상세 경력기술서 제출 필수(협업 프로젝트 ROLE 명확화). 1차 면접은 티빙 사례 기반 설계 과제(토론·손 설계)
- Job scope:
  1. AI 기술 활용 개발 프로세스 개선
  2. TVING 웹·스마트TV 서비스 개발·운영
  3. 모바일 앱 웹뷰 기능 개발·운영
  4. FE 성능 최적화·배포 환경 고도화
  5. 공통 모듈·패키지 설계·개발
- Candidate evidence to emphasize:
  - EXP-05 미스미: 성능(8초→2초·평균 로딩 50%)·SEO·월 방문자 112만(GA·Adobe Analytics 기준, user-attested 2026-08-10)·반응형 → 성능·대규모·SEO·반응형
  - EXP-02 비즈36.5: WebView 앱 운영·호환성 검증·반응형(미디어 쿼리, WebView 모바일 전제) → 웹뷰 자격요건 정면
  - EXP-03: FE AX SOP·Codex/Claude Code·GitLab MR 양방향 코드 리뷰+AI 코드 리뷰 도입·Playwright CI 게이트 → AI 개발 프로세스(담당업무 1)·코드 리뷰 문화·품질 체계
  - EXP-01: AI 챗봇 제품화(30초→6초·활성 3,493명)·Config-Driven UI·Base-Theme·Storybook → AI 비즈니스 임팩트(우대)·공통 모듈·디자인 시스템
  - AWS: S3·EC2 배포 파이프라인 운영(구성된 환경 위, user-attested 2026-08-10) → AWS 활용 요건
- Risks or gaps (갭 인터뷰 2026-08-10 완료):
  - 반응형: **해소** — 비즈36.5·미스미 미디어 쿼리 기반 PC/모바일 대응 (user-attested 2026-08-10, experience-bank 적재)
  - GitHub PR: GitLab MR 실무(양방향 리뷰+AI 코드 리뷰)로 정직 인접 표기 — "GitHub PR" 직접 주장 금지
  - AWS: S3·EC2 "활용·운영" 동사만, "구축" 금지. CloudFront 무경험 — 미기재
  - MFE: 무경험 확정 — **이력서 완전 미기재** (소유자 결정 2026-08-10). island-loader 서사는 유지하되 MFE 연결 표현 금지. 면접 방어: island-loader 점진 전환을 인접 논리로 준비
  - 스트리밍/미디어 도메인 무경험: 우대 아님·자격요건 아님, 도메인 창작 금지
  - needs_scope 지표: base 문면(스코프 병기) 그대로 승계 (2026-08-10 브리프 확정)
- Keywords to include: Frontend Engineer, WebView(웹뷰), 반응형 웹, 성능 최적화, SEO, AWS, 코드 리뷰, AI 개발 프로세스, 공통 모듈, 디자인 시스템, Config-Driven UI, Storybook, CI/CD, Playwright, 대규모 트래픽, Next.js, React, TypeScript
- Screen profile: Scale-Perf   (2026-08-10 소유자 승인 — 조직 소개·담당업무가 대규모 스트리밍 성능·안정성 축, 성과임팩트·성과신뢰성 가중이 티빙 스크리너 시선과 부합)
- Pass bar: 80 (default)
- 헤드라인/포지션 (2026-08-10 소유자 승인): 포지션 `Frontend Engineer` / 헤드라인 `웹·웹뷰 서비스의 성능 최적화와 AI 기반 개발 생산성 개선을 함께 다루는 Frontend Engineer`
- 산출물 (2026-08-10 브리프 확정): ①이력서+상세 경력기술서(정본 템플릿 PDF) ②자기소개서 base 정본 verbatim 합본(타겟 편집 없음, 스마일게이트 전례)
- Draft status: **최종 렌더 완료 (2026-08-11)** — 소유자 diff 승인(스톱 ②, 2026-08-11) 후 designer 렌더: outputs/tving-full-resume.pdf(9p) + outputs/tving-full-resume-with-self-intro.pdf(12p, 자소서 base-self-introduction.md verbatim 합본). 스마일게이트 정본 템플릿(CSS byte-for-byte 재사용), 문면 변경 없음 검증 완료. 초안: outputs/tving-full-resume-draft.md + companion tving-new-prose.md.
  edit-from-base(fast lane → 1R 게이트 FAIL로 full lane 전환). reviewer 3회(1차 must-fix 2건: AWS 비즈36.5 오귀속·"반응형 구조 완비" 과장 / 2차 전체 재검 / 최종 무결성 통과)·ats(필수 7/7·우대 5/5)·적대 검증 1회(critical 1: 삼성물산 WebView 무근거 삽입 → base 복원, major: AI 코드 리뷰 자동화 융합 축소).
  점수 게이트(Scale-Perf/80) 3라운드: 인사 71.7→77.5→**83.2 PASS** / 기술 73(레지스트리 블로커)→78.5→**81.5 PASS** — AND 게이트 통과, 블로커 0.
  주요 라운드 수정: base 편집 노트 잔존 제거, "2초대(네트워크 수신 기준)"·"Lighthouse 91점(AI 챗봇 화면 기준)"·"사용성·만족도(2차 PoC 검증 기준)" 스코프 병기, 핵심 성과 재배열(①성능 ②AI 프로세스 ③WebView ④챗봇), 티빙 지향 동기 문장, 경력기술서 2번 기간 2026.01~2026.06.
  기각(base 소유자 확정 승계): 매출 1.0억 문면·"풀스택 총괄"·경력 라인 "2.5초→1초"·체류 32%.
  면접 대비 메모: 웹뷰 "성능 최적화" 수치는 본문에 없음(호환성 검증·운영까지만) — 비즈36.5 WebView 서빙 성능 연결 논리 준비. MFE는 island-loader 점진 전환 인접 논리로 방어. 내담 초기 20개월 공백 질문 대비.
  잔여 확인(소유자): 미스미 112만·SKU 10만 문서 근거(pending documentary source — GA/Adobe 스크린샷 확보 권장), AI 코드 리뷰 도구명.
  다음 단계: 소유자 최종 PDF 확인 → 제출 (마감 2026-08-17 23:00 KST, 조기 마감 가능).

### 빗썸(주식회사 빗썸코리아, 빗썸페이) / Frontend Engineer (경력)

- Source job posting: https://www.jobkorea.co.kr/Recruit/GI_Read/49702320 (JobKorea Gno=49702320, 2026-08-13 수집)
- Application deadline: [확인 필요]
- Target position: Frontend Engineer (빗썸페이) / 정규직(수습 3개월), 경력 3년 이상, 학력 무관. 근무지 서울 강남구 테헤란로 124 삼원타워
- Role preset: fintech — 2026-08-13 소유자 승인 (근거: 회사가 가상자산거래소/핀테크 도메인이고 우대사항 "React Admin·Backoffice 개발 경험"이 fintech 프리셋의 백오피스형 evidence(EXP-04·EXP-02)와 정합. 단 이 JD의 담당업무 1번·자격요건 1번이 React Native 모바일 앱 개발이며, 기존 fintech 프리셋의 두 하위형(백오피스형·트레이딩형) 어디에도 "네이티브 모바일 앱이 주력"인 신호가 없다 — 브리프의 최대 예외 항목으로 다룸. 프리셋 자체의 세 번째 하위형(모바일 프로덕트형) 신설 여지가 있으나, 이는 이번 브리프에서 제안만 하고 role-presets.md 편집은 소유자 승인 후 별도 처리)
- Required skills:
  - React Native 또는 React 경험 3년 이상 (택일)
  - TypeScript 기반 앱·웹 개발 경험
  - iOS·Android 크로스 플랫폼 경험
  - 실용적이고 합리적인 기술적 결정 능력
  - 자기주도적 문제 해결 능력
  - 제품 오너십 경험
  - 팀 협업 및 열린 커뮤니케이션 능력
- Preferred skills:
  - Expo, Expo Router, EAS Build·Update 경험
  - 상태 관리 및 폼 검증 구조 설계 경험
  - 모바일 보안 기능(인증, 생체인증 등) 개발 경험
  - React Admin·Backoffice 개발 경험
  - 코드 리팩터링 및 성능 개선 주도 경험
  - 0 to 1 제품 전 사이클 경험
  - 간편결제·금융·가상자산 도메인 경험
  - AI 기반 학습 및 개발 생산성 향상 의욕
- Company / team signals:
  - 가상자산거래소·디지털 금융 플랫폼(빗썸코리아), 빗썸페이 자체 프로덕트 조직
  - React Native 앱 + React/TypeScript Admin의 소규모 풀사이클 프로덕트 조합 — "초기 기획 단계부터 밀착 참여"·"빠른 실행 중심" 표현이 스타트업형 프로덕트 조직 신호
  - 전형: 서류 → 1차 실무 인터뷰 → 2차 컬쳐핏 인터뷰 → 최종합격 → 레퍼런스 체크 (컬쳐핏 별도 단계 존재)
- Job scope:
  1. React Native 기반 iOS·Android 앱 개발 및 운영
  2. React·TypeScript 기반 Admin 개발 및 운영
  3. 초기 기획 단계부터 밀착 참여, 팀 구성원과 빠른 실행 중심 제품 개선 주도
- Candidate evidence to emphasize:
  - EXP-04(삼성물산): React Native iOS/Android 앱 개발·배포, FlatList 가상화·getItemLayout 기반 검색 응답 5초→1초(80%) 단축, 측정 기반 병목 진단(API 응답 시간 vs 화면 노출 시점 분리) → 자격요건 1(RN)·3(크로스플랫폼)·4(실용적 기술 결정)·5(자기주도 문제 해결) 정면 대응. **리드 스토리**
  - EXP-04: 웹/RN 공통화 범위 제한(로직·타입 공유, UI는 플랫폼별 분리), 상태 관리 경계 판단(React Query/로컬 state/Recoil) → 우대 "상태 관리 구조 설계 경험" 정면 대응(단, 폼 검증 구조는 근거 없음 — 아래 갭 참조)
  - EXP-02(비즈36.5): React/TypeScript 기반 Web/Admin End-to-End 개발, 사용자 권한·메뉴·데이터 출력 정책 구조화, 108개 페이지·82개 화면 전환 단독 수행, island-loader 트레이드오프 판단(전면 재작성 대비 점진 전환 비용 판단) → 우대 "React Admin·Backoffice" 정면 대응 + 자격요건 4(실용적 기술 결정)·6(제품 오너십) 보강. Admin 스택은 React 기준(EXP-04 대시보드는 Vue 3라 "React Admin" 직접 근거는 EXP-02가 우선)
  - EXP-01(AI 챗봇): PoC → 실서비스 제품화·운영까지 오너십, Config-Driven UI 전환을 위한 대규모 리팩토링, 기획·AI·백엔드 조직과 정책 조율 → 우대 "0 to 1 제품 전 사이클"·"코드 리팩터링 주도" + 자격요건 6(제품 오너십)·7(협업) 대응
  - EXP-03: Claude Code·Cursor 실무 활용, FE AX 개발 표준 수립, 세미나 12회 → 우대 "AI 기반 학습 및 개발 생산성 향상 의욕" 대응
- Risks or gaps:
  - [핵심 리스크 — 상향 지원 성격] React Native "3년 이상" 요건은 React 전체 경력(총 5년 10개월)으로 disjunctive 충족되나, RN 자체 실무는 삼성물산 프로젝트 1건(2024.10~2025.04, 약 7개월)뿐이다. JD 담당업무 1번이 RN 앱 개발·운영 자체이므로, 서류상 요건은 통과해도 "RN 전담 3년+" 후보 대비 실무 밀도는 얕다 — 정직한 상향지원 성격. 날조 금지, RN 실무 기간을 부풀리지 않는다.
  - [갭 인터뷰 완료 2026-08-13] Expo: 사이드 프로젝트 사용 경험 있음(user-attested), EAS Build·Update는 무경험 — 사이드 프로젝트 한정으로만 표기 가능, EAS는 미기재.
  - [소유자 결정 2026-08-13] 모바일 보안 기능(인증, 생체인증 등): 케이스에서 제외 — 미기재.
  - [갭 해소 2026-08-13] 폼 검증 구조 설계: react-hook-form·yup/zod 사용, 공통 검증 구조를 만들어 context에서 핸들링(user-attested) — experience-bank 적재 후 사용 가능.
  - [갭 인터뷰 완료 2026-08-13] 간편결제·금융·가상자산 도메인: 무경험 확인 — fintech 프리셋 공통 가드대로 전이 어필만(EXP-02 결제·정책 인접), 도메인 창작 금지.
  - [RN 범위 보강 2026-08-13, user-attested] RN 실무가 삼성물산 건 외에 비즈36.5·삼성물산 사내 애플리케이션 개발/유지보수에도 사용됨 — 기간·세부는 experience-bank 적재분 기준으로만 표기, 기간 창작 금지.
  - 컴퓨터 관련 학과 등 학력 요건 없음("학력 무관") — 이 JD는 학력 갭 리스크 없음.
  - 경력 연수: 총 5년 10개월(2020.10~2026.08 기준, 2026-08-13 시점 재계산) — JD 요건(3년 이상) 충분히 충족, 연차 리스크 없음.
  - EXP-04 대시보드(Vue 3·ECharts·RealGrid)는 "React Admin" 요건과 스택이 다름 — 관리자형 데이터 화면 경험으로만 인접 어필, React Admin 직접 경험은 EXP-02로 한정.
  - needs_scope 지표(사용성 4.18·400건 출력률·커버리지 98%·매출 4.66억·FE 에러 0건): 스코프 병기 없이 본문 강조 금지(공통 가드). 이 JD는 성과 규모보다 직무적합 신호가 우선이라 강지표 의존도는 낮을 전망.
- Keywords to include:
  - React Native, TypeScript, iOS, Android, 크로스플랫폼, React, Admin, Backoffice, 상태 관리, 제품 오너십, 자기주도, 실용적 기술 결정, 리팩터링, 성능 개선, 0 to 1, 협업, 커뮤니케이션
- Screen profile: Balanced — 2026-08-13 소유자 승인 (근거: 기존 4개 프리셋 중 어느 축도 이 JD를 정확히 대표하지 않음 — Scale-Perf의 대규모 트래픽·Platform-DS의 안정 운영·AI-Product의 AI 중심 문제해결 어디에도 강하게 걸리지 않는 소규모 프로덕트 조직 신호라 중립 프리셋이 안전. 대안: AI-Product — "자기주도 문제 해결·실용적 기술 결정·제품 오너십"이 이 프리셋의 강조 축(문제해결 30·직무적합 30)과 결이 비슷하나, "특정 스택 비고정" 전제와는 어긋남(이 JD는 RN/React/TS로 스택이 고정형). 둘 중 소유자 승인 필요)
- Pass bar: 80 — 2026-08-13 소유자 승인
- Draft status: 최종 렌더 완료(2026-08-14) — `outputs/bithumb-pay-resume.{md,html,css,pdf}`. 갭 인터뷰 3회(2026-08-13 ×2, 2026-08-14)로 RN 운영·WebView↔RN 경계·Admin 기제·폼 검증 귀속 확보. 점수 게이트(Balanced 80) 3라운드: 인사 70→75→78 / 기술 66→69.5→71.5, 블로커 0 — AND 게이트 미통과였으나 소유자 결정(2026-08-14)으로 **정직한 상향지원** 출고(카카오페이·GS리테일 전례와 동일 처리). 잔여 감점은 구조적(RN 실무 밀도, 동기 문장 미기재 정책). fast lane 시작 → 1R FAIL로 full lane 전환.

### CJ푸드빌 / 프론트엔드 개발자 — 뚜레쥬르 APP 리빌딩 (경력)

- Source job posting: 사용자 제공 JD 텍스트 기준, 2026-08-17 수집 — CJ푸드빌 채용
- Application deadline: 2026-08-19(수) 마감
- Target position: 프론트엔드 개발자 (경력) / CJ푸드빌 베이커리·외식 브랜드 통합 디지털 채널(웹/앱/어드민) 개발·운영 / 뚜레쥬르 APP 리빌딩 참여
- Role preset: fe-platform 제안(브리프 승인 시 확정)
  (선택 근거: 통합 디지털 채널 웹/앱/어드민 개발·운영, 공통 모듈·디자인 토큰·브릿지 레이어 설계, 레거시 리빌딩, 안정 운영, AI 기능 도입 — fe-platform 신호 일치)
- Required skills:
  - 학사 이상 (컴공·산공·소프트웨어공학 관련)
  - 프론트엔드 4년 이상
  - React·Next.js·TypeScript·TanStack Query로 웹 서비스 개발
  - 앱·웹 함께 다루며 코드·타입·디자인 시스템 일관성 유지 경험
  - 운영 환경 성능·안정성·UX·보안 고려 설계
  - Claude Code·ChatGPT Codex 등 AI 개발 도구 활용
- Preferred skills:
  - React Native 앱 출시·운영
  - 네이티브-웹 통신 구조(RN 브릿지, WebView 인터페이스) 설계
  - JSP 기반 레거시 웹 점진 마이그레이션
  - F&B 또는 e커머스 운영 경험
  - ISMS-P·시큐어코딩 등 보안 요구사항 대응
  - AI 기반 기능(챗봇·추천·자동화) 구현·연동
  - 웹·앱 및 온·오프라인 연계(O2O) 서비스 개발
- Company / team signals:
  - CJ푸드빌: CJ그룹 계열, 뚜레쥬르·빕스·제일제면소·더플레이스 브랜드 운영
  - 뚜레쥬르 APP 리빌딩: 앱/웹 공유 공통 모듈·디자인 토큰·브릿지 레이어 설계·고도화 강조
  - 기획·디자인·백엔드 협업 / 코드 리뷰·기술 논의로 높은 코드 기준 정립·개발 문화 향상 중시
  - 전형: 서류→CJ CFT(컬처핏)→면접→평판조회→검진→처우
- Job scope:
  1. 푸드빌 베이커리·외식 브랜드 통합 디지털 채널(웹/앱/어드민) 개발·운영
  2. 뚜레쥬르 APP 리빌딩 참여
  3. 웹·앱 공유 공통 모듈·디자인 토큰·브릿지 레이어 설계·고도화
  4. 서비스 성능·품질 개선, 장애 대응, 레거시 리빌딩
  5. 기획·디자인·백엔드 협업
  6. 코드 리뷰·기술 논의로 코드 기준 정립·개발 문화 향상
- Candidate evidence to emphasize:
  - EXP-04 삼성물산: React Native iOS/Android 개발·배포, 웹/RN 공통화(비즈니스 로직·타입 공유, UI 분리), TanStack Query — React Native·웹/앱 코드·타입 일관성 정면 대응
  - EXP-02 비즈36.5: jQuery/Thymeleaf → React 점진 전환(island-loader 패턴), WebView 운영·호환성 검증, Jenkins CI/CD Blue-Green — 레거시 리빌딩·점진 마이그레이션 인접, WebView 브릿지 인접
  - EXP-01 AI 챗봇: Config-Driven UI·Base-Theme으로 고객사별 테마·기능 분리, Storybook 기반 공통 컴포넌트 — 디자인 시스템 일관성·공통 모듈
  - EXP-03: GitLab MR 코드 리뷰 문화(양방향 리뷰·AI 코드 리뷰 도입), FE AX 개발 표준 문서화·세미나 12회·문서 48건 — 코드 기준 정립·개발 문화 향상 정면 대응
  - EXP-03: Claude Code·Codex AI 개발 도구 실무 활용·생성 코드 검증 기준 — AI 개발 도구 활용 자격요건 정면
  - EXP-05 미스미: PHP/jQuery 레거시 → Next.js/React 전환, 성능(8초→2초)·SEO, B2B 커머스(e커머스 우대) — 레거시 전환·e커머스 경험
  - EXP-01: AI 건강검진 챗봇 실서비스(AI 기반 기능 구현·연동 우대) — XSS 필터링(보안 인접, C-05 준수)
- Risks or gaps:
  - [구조적 갭] 컴공 관련 학과 요건: 성공회대 일어일본학과. 정보처리기사(2020.08) + 응용SW엔지니어링 과정으로 보완. 스마일게이트 전례와 동일 처리 — 상단 자격 신호 강화 필요
  - [갭 인터뷰 필요] 아래 "갭 인터뷰 항목" 참조
  - JSP 레거시: 은행은 jQuery/Thymeleaf·PHP/jQuery 레거시 전환만 — JSP 직접 경험 없음으로 추정. 서버사이드 템플릿 레거시 점진 전환 전이로만 표기, 소유자가 JSP 실경험 있으면 archivist 적재 후 반영
  - 보안(ISMS-P·시큐어코딩): XSS 필터링(EXP-01)·AI 생성 코드 검증 기준(EXP-03)으로 인접 어필만; ISMS-P 인증 대응 직접 경험 없음
  - O2O 서비스: 배달·O2O 플랫폼 직접 경력 없음. e커머스(미스미)·WebView(비즈36.5) 전이 어필만
- Keywords to include:
  - React, Next.js, TypeScript, TanStack Query, React Native, WebView, 공통 모듈, 디자인 시스템, 레거시 리빌딩, 점진 마이그레이션, 성능 최적화, 코드 리뷰, 개발 문화, AI 개발 도구, Claude Code, Codex, e커머스, 브릿지 레이어, Config-Driven UI, Storybook
- Screen profile: Platform-DS 제안(소유자 승인 대기)
  (근거: 통합 디지털 채널 운영·공통 모듈·디자인 시스템·레거시 리빌딩·안정 운영 JD — Platform-DS 루브릭의 디자인시스템·서비스 안정성 축이 JD 핵심과 일치)
- Pass bar: 80 (default)
- Draft status: 브리프 대기 (2026-08-17 작성)

### GS글로벌 / FDE 경력 (과장급) — 헤드헌터 경유

- Source job posting: 헤드헌터(HR컨설팅그룹, jtchoi35@hrcg.co.kr) 제공 JD 텍스트, 2026-08-21 수집
- Application deadline: 채용시 마감 (ASAP)
- Target position: FDE(Forward Deployed Engineer) 과장급 — AX 과제 발굴 / LLM·Agent PoC·MVP 개발·검증 / AX 솔루션 도입·변화관리
- Submission format: **GS글로벌 지정양식 docx** (이력서+회사별 경력기술서+자기소개서, 현재연봉·희망연봉 필수) — 이메일 제출
- Role preset: ax-harness (근거: GS리테일 AX와 동일 계열 — AI 활용 프로토타입 개발·검증, 현업 문제 재정의, 재사용/표준화 신호)
- Screen profile: AI-Product / Pass bar: 80 (GS리테일 AX 전례 재사용)
- Required skills: 경력 5년+ / Python 데이터 분석·LLM/Agent 프로토타이핑 / SQL·클라우드(AWS·Azure) 데이터 추출·가공 / Docker 배포·운영 / ERP·CRM 레거시 API 설계·통합 / 현업 요구 재정의 / 커뮤니케이션·설득
- Preferred: 종합상사 업무 이해 또는 AX 프로젝트 경험 / 비즈니스 외국어 / 애자일·이터레이션 마인드셋
- Grill-me 확정 결정 (2026-08-21, 플랜 ~/.claude/plans/logical-conjuring-lantern.md):
  1. 산출: md 초안 → 게이트 → python-docx로 지정양식 직접 주입 (.docx)
  2. 베이스: base-resume 재조립 (GS리테일 AX 초안은 2급 참고)
  3. ERP·CRM 연동: 실경험 없음 확정 — 미주장, 인접 근거(EXP-02 레거시 점진 전환·REST API / EXP-07 BFF 통합) 서사만
  4. Azure: AZ-900 자격(2023.06.18) 신규 적재 — 자격사항 기재 + '지식' 수준 표기, 실무 운영 미주장 (실무 클라우드는 AWS S3·EC2 운영 스코프만)
  5. 자격 신규 2건 적재: AZ-900, 자산관리사(FP) 2016.11.18
  6. 연봉 기재 (하우스 규칙 "급여 미기재"의 폼 필수 예외, 소유자 승인): 현재 5,700만원 / 희망 "회사 내규에 따름"
  7. 퇴직 사유: 내담씨앤씨 = AI 중심 조직으로의 의도적 커리어 전환(positioning 정합), 대웅제약 = 재직 중
  8. 자소서 [성격의 장/단점]: 증거 기반 초안 제안 → 소유자 교정 (단점은 보완 행동 사실 필수)
  9. 개인 데이터: 생년월일 1991.04.29 / 여의도고 2007.03~2010.02 / 사진 파일 확보(bmp→jpg 변환 삽입)
  10. 회사 개요: 웹서치 조사 — 대웅제약(제약, 2025 연결 매출 1조 5,709억, 임직원 약 2,000명 / 잡코리아·사람인), 내담씨앤씨(SI·컴퓨터 프로그래밍 서비스업, 2024 매출 289.8억, 직원 약 100명, 2008 설립 / 잡코리아) — 초안 리뷰 시 소유자 최종 확인
  11. 미스미 상사·외국어 우대 각도: 부각하지 않음 — 기술/AX 적합도 중심 (어학·자격은 자격사항에만)
- Risks or gaps:
  - [구조적] ERP·CRM 레거시 API 연동 실경험 없음 — 미주장 (게이트 감점 예상, 날조 금지)
  - [구조적] Azure 실무 무경험 (AZ-900 지식 수준만) / GCP·DynamoDB·Lambda 무경험 확정 (재질문 불요)
  - Python·RAG·pandas "참여·기초" 톤 한정 (EXP-07 가드)
  - 경력 5년+ 요건: 총 경력 충족(2020.10~) — 여유 크지 않음, 과장급 레벨핏 면접 대비
  - 내담 초기 1.5년(2020.10~2022.05) 공백 — 회사 단위 경력기술서 재편 시 노출 가능
- Keywords to include: FDE, AX, PoC, MVP, LLM, Agent, Python, SQL, AWS, Azure, Docker, API 설계, 레거시 연동, 현업 요구 재정의, 변화관리, 프로토타입 배포·운영, 재사용 표준
- Draft status: **완료(게이트 PASS 출고) — outputs/gs-global-fde-{full-resume-draft.md,new-prose.md,resume.docx}.** 지정양식 docx 직접 주입(python-docx, 사진 blipFill 삽입·서식 변환). 최종 게이트 인사 86 · 기술 81.5 둘 다 PASS(AI-Product 80, 블로커 0). 자소서는 소유자 직접 작성본(가드 수정 6건). Codex 미사용(P-02)
- JD 회사 소개 (헤드헌터 제공 JD 원문 기재분, 2026-08-21 수집 — 초안 지원동기의 회사 사실 출처):
  1954년 회사 설립. 철강, 석탄/바이오매스, 석유/화학제품 및 기계/물자 등의 수출·수입·삼국간 거래, 수입자동차 물류 등 사업. 2009년 GS그룹 편입. "Value No.1 Solution Provider" 지향. 수십 년 사업 경험과 30여개 해외 Network 기반.
- 보조 리서치 (2026-08-21 웹서치): GS그룹 차원 현장 중심 AX — 52g("(5)Open (2)Innovation GS") 이니셔티브에 GS글로벌 참여 (ZDNet 2026-04, 파이낸셜투데이 등). 초안에는 명칭·수치 없이 "그룹 차원 디지털 전환" 배경 한 문장으로만 사용.
- 하우스 규칙 예외 (지정양식 사유, 소유자 플랜 승인 2026-08-21; F-01은 2026-08-22 성과 선행 포맷 확정으로 추가): F-01 경력기술서 고정 골격·F-02 핵심 성과 섹션·F-03 헤드라인·F-07 섹션 순서 미적용 — GS 지정양식 구조([핵심역량] 등)가 우선. F-08 전면 계층 수치는 [핵심역량]이 유일한 1페이지 스캔 섹션이라 시그니처 지표 위주로 유지.
- 폼 글자수 제한: docx 셀 자유 입력 — 명시 제한 없음 (자소서 항목당 600~900자는 내부 기준).
- JD 보완 기록 (2026-08-21): 담당업무 3 원문은 "AX 솔루션 도입 관련자(현업, 임원진, **IT 인프라/보안팀**) 간 소통 조율 및 변화 관리 수행" — 보안 조직 협업이 JD에 실재(자소서 "현업·IT·보안 조직과 협업" 근거).
- 결정 11 갱신 (2026-08-21): 자기소개서는 소유자 직접 작성본으로 전면 교체(가드 수정 6건 반영 — S-01 치환·"검증"→"참여"·"구축"→"구성"·SQL 범위·"전환" 동사·삼성물산 양단 인과 복원). 미스미 일본어 협업 사례가 자소서 [직무수행] 4에 포함됨 — "외국어 각도 부각 안 함" 결정은 협업 사례 서술까지 막지 않는 것으로 갱신.
- 게이트 이력: 1R 71/69.5 FAIL → 2R 77/74(루브릭, S-01 신규 유입 블로커로 59 캡) → 3R 77/75 FAIL(블로커 0, P-01 3라운드 소진·정지) → 소유자 지시 갭 인터뷰 2회(MCP 서버 개발·용도 2종, 데이터 과제 정의+실행 체인, Python 수정 대상, pandas 철회) 적재 후 보강 라운드(캡 비산입) 81/78.5 → 2차 보강 82/82.5 **둘 다 PASS** → 자소서 소유자 교체본 재확인 **86/81.5 PASS 유지**(블로커 0).
- 면접 대비 (tech-screen 기록): ① Python 데이터 분석 패키지 공백(pandas 철회 — 정직 갭) ② MCP 서버 구현 깊이(도구 스키마·인증) ③ 데이터 과제 실행 결과 수치 미확보 답변 준비 ④ 체류 32%·로딩 약 50% 스코프 질문 ⑤ BFF "신규 구축"은 팀 공동 범위 ⑥ SQL 튜닝 실체(필터링·정렬+인덱싱·DTO 투영) ⑦ TOEIC 2026.05 유효기간 만료 인지.
- 압축 개정 (2026-08-22, 소유자 grill-me): 경력기술서(제2부)만 개조식 압축 — 불릿 1줄화·문제 1~2문장·개괄/메타/퇴직사유 압축(225→148행, 약 34%). 판단 프레이밍 3문장·가능형 표현(MF 2건)·기제 절 복원 후 확정. 압축본 게이트: recruiter 89 / tech 82.5 둘 다 PASS(블로커 0). 무결성 재검 통과(수치·게이트 근거 100% 보존). 제출본: outputs/gs-global-fde-resume-v3.docx (11p, 작성일 2026.08.22). v1(산문형 초판)·v2(레이아웃 개선판)는 보존.
- 소유자 인지 사항: ① 퇴직 사유 압축으로 positioning "자발 학습→AI 조직 이직" 서사가 문서 전역에서 제거됨(소유자 교체 자소서에도 없음 — 면접 구두 방어로 이동) ② 압축 시 "가능형" 표현(참여 가능·확인 가능)이 은행 근거 경계임이 확인돼 C-20 가드에 등재.
- 포맷 개정 2차 (2026-08-22, 소유자 grill-me): 경력기술서를 "성과 선행 고정 포맷"으로 재조립 — 프로젝트 5개 동일 리듬(◆ 제목—역할(기간) → "→" 성과 수치 줄 → 주요 실행 4~5불릿 → 기술:), 문제·[주요 업무] 메타 삭제(판단 프레이밍은 실행 불릿에 "제약 → 대응"으로 흡수), 제2부 103행(최초 대비 54% 감량). **하우스 규칙 예외 추가: F-01(경력기술서 고정 골격·[주요 업무] 라벨) 미적용 — 소유자 확정 성과 선행 포맷이 우선** (F-02·F-03·F-07 예외와 동일 취지).
- 포맷 개정 2차 결과: 게이트 recruiter 92 / tech 82 둘 다 PASS(블로커 0). 무결성 재검에서 통합 과정 정밀 오류 6건(가능형 소실 3회째·기제/귀속 전이·registry 표현 이탈·M-6 인과 재결합) 발견·전건 수정 후 확정. 제출본: outputs/gs-global-fde-resume-v4.docx (10p). 교훈 방침화(companion C-21a): 정성 라벨 삭제 시 종속절(기제·귀속·스코프)이 딸려 나가는 패턴 — 포맷 변경 전 종속절을 본문으로 먼저 이동, 가능형 3곳·스코프 병기 5종은 매 라운드 고정 grep.
- 렌더 개정 3차 (2026-08-22, 소유자 grill-me): 경력기술서를 제1부와 동일한 2열 격자(왼쪽 라벨 열 [프로젝트]/[기간]/[성과]/[주요 실행]/[기술] + 오른쪽 내용, 세로선 없음·프로젝트 경계 연한 가로선)로 docx 렌더 — **문면은 v4 게이트 확정본(92/82 PASS) 그대로, md 정본 불변, 재채점 불요(레이아웃 전용 변경)**. python-docx 중첩 표로 구현. 제출본: outputs/gs-global-fde-resume-v5.docx (10p). 렌더 스크립트: 세션 스크래치 inject_docx_v5.py (프로젝트 기간은 제목 괄호에서 분리해 [기간] 행으로).
- 재라이팅 4차 (2026-08-22, 소유자 grill-me — 레퍼런스 조사 기반): 외부 레퍼런스 3원칙(불릿 1.5줄 이내 1메시지·볼드는 수치만·지표당 개행) 적용 — 성과 행 지표당 1줄(볼드 수치 전용, 제2부 볼드 102→31), 실행 불릿 1줄 1메시지 재분해(25→38개), 판단 프레이밍 "제약 →" 절 보존. 게이트 recruiter 94 / tech 83.5 둘 다 PASS(전 라운드 최고). 무결성 재검 must-fix 2건(8초→2초 프로젝트 귀속·"보조" C-01 격하) 수정 후 확정. 제출본: outputs/gs-global-fde-resume-v6.docx (10p, 2열 격자 렌더 유지). companion C-22·C-22a 정본.
- 외부 피드백 대개편 (2026-08-22, 소유자 제공 외부 전문가 리뷰 트리아지 — companion C-23·C-23a): 수용 7·수정수용 3·기각 1(Python 추가 구체화 — 은행 한계). 반영: 핵심역량 5불릿 재구성(현업 재정의 1번), 프로젝트 제목 FDE 분류 전환(역할어 본문 유지 — 은폐 아님), 대웅 소속 화살표 통일, 삼성물산·미스미 압축(W3b 토큰 FlatList·code splitting 복원), 전면 계층 단독→주도, 기획·운영팀 교육·템플릿 배포 불릿 신설(EXP-03 문서 근거 선별 적재 — daewoong-history 1059·574행, 충돌 8건과 무관 확인). 자소서는 소유자 결정으로 불변(수정안은 outputs/gs-global-fde-self-intro-revision-proposal.md 보존 — "프론트엔드" 2곳은 가드 스코프라 유지 확인). 글로벌 협업 핵심역량 불릿은 미추가(기존 결정 유지). 최종 게이트: recruiter 96 / tech 85.5 둘 다 PASS(블로커 0, 최고점). 제출본: outputs/gs-global-fde-resume-v7.docx (10p).
- 외부 추가 피드백 3건 반영 (2026-08-22, companion C-23a): ① 대웅 개괄 End-to-End 선행·FE 총괄 후치("제품 개발 총괄"은 근거 초과라 미채택 — 수정 수용) ② "2019년 구축 레거시 시스템" 명확화 ③ "3건 단독 개발"→"End-to-End 개발"(단독 빈도 3→2, 대표 1곳·양단 적용 유지). 게이트 재확인 96/85.5 PASS 유지. v7 docx 갱신 재생성.

### 코오롱베니트 / 플랫폼 개발/운영 (경력, 정규직)

- Source job posting: [URL 미확인 — 헤드헌터(㈜써치라인) 제공 JD 텍스트 기준, 2026-08-24 수집]
- Application deadline: [미확인 — 헤드헌터 경유 상시]
- Target position: 플랫폼 개발/운영 (과천 코오롱타워, 정규직). 코오롱그룹 IT서비스 전문기업(매출 5,059억·직원 530명 — 헤드헌터 제공 수치)
- Role preset: fullstack (전례: 두산로보틱스 — "실시간 통신" 라벨 금지 → SSE 단방향 이벤트 스트리밍, "클린 아키텍처 지향" 금지 가드 승계)
- Required skills: 개발/운영 경력 · React JS·Java 기반 개발 및 운영 · DB 설계·개발
- Preferred skills(필요 자격/스킬): React JS 중급+ · Java 중급+ · DB 설계/개발 중급+ · Electron JS 개발 경험 · Node.js 기반 서버 개발 · AI Tool·API 등 AI 기술 활용
- Company / team signals: 우대사항이 기술이 아닌 태도 3종 — 작업 지침 준수·꼼꼼한 검토 / 신기술 탐구 지속력 / 업무 의도 이해·명확한 전달(커뮤니케이션)
- Job scope: 사내 메신저·커뮤니케이션 플랫폼 개발/운영 · PC/모바일 기반 사내 서비스 개발/운영 · 웹하드 솔루션 운영·유지보수
- Candidate evidence to emphasize: React/TypeScript 전 경력(↔React 중급+), 비즈36.5 Spring Boot·MySQL 신규 기능 3건 End-to-End(↔Java·DB 설계/개발), Node.js(Express) 집계·중계 API(↔Node.js 서버), Electron CA "Report Export Service Manager" 유지보수(↔Electron — **동사 "유지보수" 고정, 구축·설계 금지**), MCP·LLM 챗봇·회귀평가·Codex/Claude Code(↔AI 활용), 사내(임직원) 서비스 3종 운영·B2B 플랫폼 운영(↔사내 서비스 개발/운영), 검증 자동화·E2E 게이트(↔꼼꼼한 검토 우대)
- Risks or gaps:
  - [구조적] 사내 메신저·커뮤니케이션 플랫폼, 웹하드 솔루션 직접 경험 없음 — 미주장, 인접 근거(사내 임직원 서비스 개발/운영)로만 커버
  - Electron 구현 세부(IPC·패키징 등) 미확인 — "유지보수" 스코프 초과 서술 금지 (experience-bank EXP-06 가드)
  - Java 밀도: FE 중심 경력이라 tech-screen에서 Java 깊이 지적 가능 — 비즈36.5 End-to-End·삼성물산 Spring REST API 연동 범위로 사실 표기
- Keywords to include: React, TypeScript, Java, Spring Boot, MySQL, Oracle, DB 설계, Node.js, Electron, REST API, 사내 서비스 운영, AI Tool, MCP, LLM, 유지보수, 무중단 배포
- Screen profile: Platform-DS   (소유자 승인 2026-08-24)
- Pass bar: 80
- 지정양식: ㈜써치라인 헤드헌터 양식 docx 4p (`/Users/2302-n0214/Downloads/코오롱베니트_직무_이름_써치라인.docx`) — 개인신상(지원부문·생년·주소·연락처·사진)/학력 표/근무사항 표(총 경력 년·월)/핵심역량(자유 단락)/경력사항(자유 단락, 최근 순)/기타사항(병역·외국어·자격)/입사가능시기(협의)/희망연봉 표/자기소개서(자유)/개인정보 동의·서명. python-docx 직접 주입.
- 결정 (소유자 승인 2026-08-24, 스톱①):
  1. 연봉: **현재 기본연봉·총연봉 모두 5,700만원 기재** — 코오롱베니트 제출본 한정 예외 재승인(GS글로벌 전례와 동일 취지, 다른 문서 노출 금지 유지). 희망연봉은 양식 prefill "협의" 유지
  2. Screen profile: Platform-DS 80
  3. 경력사항 포맷: GS 성과 선행 포맷(◆ 제목 → 성과 수치 줄 → 실행 불릿 → 기술:) 압축 재사용 — 대웅 3개 프로젝트 상세 + 삼성물산·미스미 압축, 전체 6~7p 목표
  4. 직급 표기: 다나아데이터 플랫폼개발팀 "팀원", 내담씨앤씨 "대리". 연봉 표 직급란도 동일
- Draft status: 진행 중 (2026-08-24 착수)
