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
