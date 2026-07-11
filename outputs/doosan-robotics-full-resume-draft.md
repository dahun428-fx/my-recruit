# 정다훈 이력서 및 경력기술서 — 두산로보틱스 Fullstack Developer 지원용

## API·BFF부터 React UI·배포 자동화까지 구현하는 Fullstack Developer

## 인적사항

- 이름: 정다훈
- 포지션: Fullstack Developer
- 경력: 총 5년 9개월
- 휴대폰: 010-4346-0429
- Email: dahun428@naver.com
- 주소: 경기 구리시 인창동
- Portfolio: github.com/dahun428-fx
- 병역: 군필 (육군 병장)

## 요약

React·TypeScript로 화면을 만들면서, 그 화면에 필요한 데이터가 어떤 REST API와 서버 로직, Query를 거쳐 내려오는지까지 함께 개발해 온 풀스택 개발자입니다. Web/Admin 화면과 서버 기능을 같이 다루고, 여러 백엔드 응답을 React 화면에 맞게 모아 돌려주는 Node.js(Express) BFF를 만들어 왔습니다.

Spring Boot·MySQL로 데이터 모델과 서버 로직을 짜고 REST API를 설계해 Web/Admin 화면까지 개발했습니다. 외주로 돌아가던 검진 예약 서비스를 9주 만에 108개 페이지·82개 화면 규모의 임직원 건강 플랫폼으로 옮겨, 외주 없이 내부에서 개발·운영할 수 있게 바꿨습니다.

AI 챗봇에서는 SSE로 내려오는 LLM 응답의 중지·재시도·오류 상태를 화면과 맞추고, Markdown·표·링크를 React 컴포넌트로 바꾸는 렌더링을 붙였습니다. Playwright E2E와 Jenkins·GitLab CI/CD로 반복 QA와 배포 전 점검을 자동화했습니다. 두산로보틱스 AI/SW 본부에서 React UI부터 Node.js BFF·REST API, 배포 자동화까지 다뤄 온 경험으로 내부 도구와 API를 만드는 데 힘을 보태고 싶습니다.

## 핵심 성과

### 1. 서버 기능·REST API·React 화면을 함께 개발

Spring Boot·MySQL로 데이터 모델과 서버 로직을 짜고 REST API를 설계해 Web/Admin 화면까지 개발했습니다. 외주로 돌아가던 검진 예약 서비스를 9주 만에 108개 페이지·82개 화면 규모의 임직원 건강 플랫폼으로 옮기고, 신규 건강관리 기능 3건을 DB부터 화면까지 직접 만들었습니다.

### 2. React 화면에 맞춘 Node.js BFF 구축

React 화면이 여러 API를 따로 부르지 않도록, 백엔드 응답을 모아 화면 기준으로 돌려주는 BFF를 Node.js(Express)로 만들었습니다. 프론트와 백엔드를 하나의 TypeScript 코드로 맞추고, REST API와 필터링·정렬·역할별 조회 로직을 설계했습니다.

### 3. 고객사별 정책을 Config와 공통 컴포넌트로 분리

고객사마다 다른 UI·문구·기능 노출을 Config-Driven UI·Base-Theme로 나누고, 반복되는 화면을 공통 컴포넌트·Custom Hook으로 정리했습니다. 반복 컴포넌트 개발·검증 시간을 90분에서 15분으로 줄였습니다.

### 4. SSE 기반 LLM 응답 처리와 렌더링 구현

SSE로 내려오는 답변의 중지·재시도·오류 상태를 화면과 맞추고, Markdown·표·링크·차트를 React 컴포넌트로 바꿨습니다. AI 답변이 화면에 뜨는 시간을 10초에서 4초로 줄이고, 발화 400건 검증에서 화면 정상 출력률 100%를 확인했습니다.

### 5. E2E·CI/CD 기반 반복 검증 자동화

Playwright로 주요 화면 E2E 600여 건을 자동화하고, LLM 응답 확인과 타입·테스트·빌드·배포 전 점검을 Jenkins·GitLab CI/CD에 넣어 자동으로 돌게 했습니다. 반복 QA를 3시간에서 1시간으로, 배포를 10분에서 2분으로 줄였습니다. AI 생성 코드의 컨텍스트·금지 패턴·보안 위험·확인 절차를 FE AX SOP로 정리했습니다.

## 경력

### 대웅제약 AI추진팀

- 기간: 2025.07 ~ 재직중
- 직무: Fullstack Developer / 백엔드·API 개발 / 프론트엔드 아키텍처 / AI 서비스 제품화

Spring Boot·MySQL·REST API 기반 기능과 React·TypeScript 프론트엔드를 함께 개발하며 AI 서비스 제품화와 B2B 플랫폼 내재화를 진행했고, 개발·검증·배포 흐름을 개선했습니다. Config-Driven UI·Base-Theme로 공통 컴포넌트 구조를 설계했고, LLM 챗봇에 SSE 스트리밍·Markdown 렌더링·오류 가드레일을 적용했습니다. 고객사별 CI·메뉴·기능 노출 정책을 공통 구조로 정리해 운영 대응 시간을 줄였습니다.

- MySQL 데이터 모델·Spring Boot 로직·REST API·Web/Admin 화면을 End-to-End 개발 (풀스택)
- 비즈36.5에서 여러 백엔드 응답을 프론트 요구에 맞게 집계·프록시하는 BFF를 Node.js(Express)로 신규 구축 (프론트–백엔드 TypeScript 스택 통일)
- Python 기반 AI 챗봇의 프롬프트·응답 후처리 로직 일부 수정·기여- Config-Driven UI·Base-Theme 기반 공통 컴포넌트 구조 설계 및 운영 (모듈화·클린 아키텍처)
- SSE 기반 실시간 LLM 응답 스트리밍·오류 가드레일 실서비스 도입 (SSE 실시간 스트리밍)
- 3,493명 대상 AI 건강검진 챗봇 PoC를 실사용 가능한 서비스 형태로 고도화
- LLM 답변 출력 10초 → 4초, 초기 진입 30초 → 6초, Lighthouse 91점
- 고객사별 CI·메뉴·기능 노출 변경을 1주 내 대응 가능한 운영 구조 확보
- Playwright 기반 600여 건 E2E 회귀 시나리오 자동화 및 Jenkins CI/CD 빌드·배포 파이프라인 구축
- AI 생성 코드 검증 기준(FE AX SOP) 문서화, 개발 세미나 12회·기술 문서 48건 (업무 자동화·AI 활용)

### 내담씨앤씨 SI사업부

- 기간: 2020.10 ~ 2025.06
- 직무: 웹개발자 / 프론트엔드 개발자 (백엔드 REST API 연동 병행)

B2B 쇼핑몰, React Native 앱, 생산관리 대시보드 등 웹·모바일 프로젝트에서 프론트엔드 개발과 Spring REST API 연동을 수행했습니다. 레거시 유지보수성, 성능 저하, 모바일 사용성, 대용량 데이터 시각화 관련 문제를 React·Next.js·Vue·React Native로 개선했습니다.

- PHP/jQuery 기반 B2B 쇼핑몰을 React/Next.js/TypeScript 구조로 단계적 전환 (레거시 점진 전환)
- 상품 비교·멀티 다운로드 등 복잡한 기능을 공통 컴포넌트·Custom Hook으로 모듈화
- Vue 3·ECharts·RealGrid 기반 대용량 생산 공정 데이터 시각화 대시보드 개발
- Spring REST API·필터링·정렬 로직 설계 및 역할별 데이터 조회·표현 구조 구성
- React Native 기반 iOS/Android 앱 기능 고도화 및 플랫폼별 이슈 대응
- Lazy Loading, 비동기 API, 폰트 최적화를 통한 성능 개선 (페이지 접근 시간 8초 → 2초)
- Vercel 배포 자동화, Lighthouse·GA·Adobe Analytics·Datadog 기반 성능·SEO·오류 추적 체계 운영

## 기술

### Languages

TypeScript, JavaScript(ES6+), Java, PHP, Python

- TypeScript 중심의 프론트엔드·API 연동 개발
- Java 기반 Spring Boot 서버 로직·REST API 구현

### Backend / API

Java · Spring Boot · Spring Framework · REST API · MySQL · MyBatis · Oracle (주력 백엔드) / Node.js(Express) — 프론트 전용 BFF(집계·프록시) 신규 구축(팀 공동) / Python — AI 챗봇 응답 로직 일부 기여
- 화면 요청부터 Controller·Service·Query·DB 조회까지 End-to-End 개발
- REST API 및 필터링·정렬·역할별 데이터 조회 로직 설계·구현
- MySQL 데이터 모델링 및 신규 기능의 서버 로직·API·화면 End-to-End 개발
- Node.js(Express)로 여러 백엔드 응답을 집계·프록시하는 React 프론트 전용 BFF 신규 구축- Python 기반 AI 챗봇의 프롬프트·응답 후처리 로직 일부 기여
### Frontend

React, Next.js, Vue 3, React Native, Redux, Recoil, TanStack Query, Tailwind CSS

- React·Vue 3 기반 SPA 서비스 개발 및 운영
- Next.js 기반 SSR·CSR 렌더링 전략 분리 (Node 런타임 기반 SSR)
- React Native 기반 iOS·Android 앱 기능 개발 및 배포
- 컴포넌트 구조 설계 및 공통 UI 재사용 구조 구축

### Architecture / Modularization

Config-Driven UI, Base-Theme, 공통 컴포넌트, Custom Hook, 레이어드 데이터 흐름, Storybook

- 공통 요소와 고객사별 차이를 Config-Driven UI / Base-Theme로 분리 (모듈화)
- 복잡한 기능을 공통 컴포넌트·Custom Hook으로 구조화 (계층 분리·의존성 정리)
- Storybook 중심 컴포넌트 개발·검증 절차 수립

### Realtime / AI / Visualization

SSE, Markdown Renderer, ECharts, RealGrid, Chart.js, Firebase FCM

- SSE 단방향 이벤트 스트리밍으로 LLM 응답의 중지·재시도·오류 상태와 UI 동기화 처리
- Markdown 전용 렌더링 계층으로 표·목록·링크·차트를 React 컴포넌트로 변환
- 대용량 테이블·시계열 데이터 시각화 및 Lazy Rendering 최적화

### Quality / Build / Delivery

Playwright, Jest, Storybook, ESLint, Jenkins, GitLab CI/CD, Vercel, GA4, PostHog, Datadog

- Playwright 기반 E2E 회귀 시나리오 자동화 및 배포 전후 검증
- Jenkins·GitLab CI/CD 빌드·검증·배포 파이프라인 구축, Vercel 배포 자동화
- AI 생성 코드 검증 기준(FE AX SOP) 문서화 및 업무 자동화

## 학력 / 교육 / 자격 / 어학

### 학력

- 2010.03 ~ 2017.02 성공회대학교 일어일본학과 졸업
  - 복수전공: 경영학과
  - 학점: 3.8 / 4.5
- 2010 여의도고등학교 졸업

### 교육

- 2020.03 ~ 2020.09 웹 콘텐츠 개발을 위한 응용SW엔지니어링 / 중앙에이치티에이㈜
  - Java 기반 웹 애플리케이션의 백엔드와 프론트엔드 개발 과정 이수
  - Spring Framework를 활용한 팀 프로젝트 진행
  - 습득 기술: HTML5, JavaScript, jQuery, Vue.js, CSS, JSP, Java, Spring Framework, AWS, RESTful API, OracleDB, MariaDB, Git/GitHub, Subversion, Tomcat, Eclipse

### 자격증

- 정보처리기사 / 한국산업인력공단

### 해외경험

- 2018.09 ~ 2019.06 일본 워킹홀리데이 10개월
  - 무인양품 일본지사(도쿄) 근무
  - 일본 비즈니스 언어 활용

### 어학

- 영어: TOEIC 825점 (2024.05)
- 일본어: JLPT 1급 (2018.08)

## 경력기술서

### 1. 대웅제약 | B2B 플랫폼 풀스택 내재화

**외주 서비스 내재화와 DB·백엔드·REST API·Web·Admin End-to-End 개발**

- 기간: 2025.11 ~ 2026.02
- 책임 범위: 서비스·데이터 구조 분석, MySQL·Spring Boot·REST API·Web·Admin 개발, Node.js(Express) 프론트 전용 BFF 신규 구축(팀 공동), 권한·메뉴 정책 공통화, WebView 앱 운영·CI/CD

#### 문제

외주 중심으로 운영되던 검진 예약 서비스를 내부 개발·운영 가능한 임직원 건강 플랫폼으로 전환해야 했습니다. 기존 jQuery·Thymeleaf 화면과 Spring Boot·MySQL 구조가 기능별로 결합되어 변경 영향 범위 파악이 어려웠고, 고객사별 CI·메뉴·기능 노출 정책이 일관되지 않아 운영 대응 속도를 높이기 어려웠습니다.

#### 주요 실행

- 화면 요청부터 Controller·Service·Query·DB·화면 출력까지 데이터 흐름과 의존 관계를 정리 (레이어드 구조 분석)
- 신규 건강관리 기능의 MySQL 데이터 모델, Spring Boot 로직, REST API, Web/Admin 화면을 End-to-End 개발 (풀스택)
- jQuery·Thymeleaf와 React가 화면 단위로 공존하는 점진적 전환 구조 설계 (레거시 점진 전환)
- 사용자 권한, 메뉴, 브랜딩, 데이터 출력 정책을 공통 기준으로 정리해 고객사별 배포 대응 구조 확보 (모듈화)
- 신규 기능의 React 프론트 전용 데이터 집계·프록시(BFF) REST API를 Node.js(Express)로 신규 구축 (Spring Boot 대체가 아닌 신규 개발 / 프론트–백엔드 TypeScript 스택 통일)
- Jenkins 빌드·검증·배포 파이프라인과 WebView 호환성 검증 기준 수립

#### 성과

- 9주 내 108개 페이지·82개 화면을 임직원 건강 플랫폼으로 전환
- 건강 데이터를 차트·대시보드로 시각화한 신규 기능 3건 End-to-End 개발
- 외주 의존 기능 변경·배포를 DB·백엔드·Web·Admin·App 전 영역에서 내부 대응 가능한 구조로 개선
- 고객사별 CI·메뉴·기능 노출 변경을 1주 내 대응 가능한 운영 구조 확보

**기술:** React, TypeScript, jQuery, Thymeleaf, Java, Spring Boot, Node.js, Express, REST API, MySQL, Tailwind CSS, Jenkins CI/CD, WebView, iOS, Android

---

### 2. 대웅제약 | AI 실시간 서비스 도입·공통 컴포넌트 구조

**SSE 기반 실시간 LLM 응답과 Base-Theme·Config-Driven UI 기반 모듈화 구조 구축**

- 기간: 2025.07 ~ 2025.10
- 책임 범위: 프론트엔드 아키텍처 설계·개발, AI·백엔드 응답 정책 조율, 실시간 응답 처리, 공통 컴포넌트 기반 서비스 확장 구조 구축

#### 문제

목업 수준의 AI 건강검진 챗봇을 실사용 가능한 서비스로 고도화해야 했습니다. 초기 PoC는 답변 생성 후 일괄 출력하는 구조라 체감 대기 시간이 길었고, Markdown·표·링크·차트 등 비정형 실시간 응답을 안정적으로 렌더링하는 체계와 고객사별 화면·테마·기능 노출 조건을 일관되게 관리하는 구조가 없었습니다.

#### 주요 실행

- AI 개발자와 API 응답 형식, 스트리밍 방식, 오류 정책을 조율 (API 설계 협업)
- SSE 기반 실시간 응답, 답변 중지·재시도·오류 상태 흐름 설계 (SSE 실시간 스트리밍)
- Markdown 전용 렌더링 계층을 구현해 표·목록·링크·차트를 React 컴포넌트로 변환
- Python 기반 AI 챗봇의 프롬프트 구성·응답 후처리(Markdown·표·링크 변환 등) 로직 일부를 직접 수정·기여- XSS 필터링과 404·500·LLM 오류 가드레일을 적용해 비정형 응답 출력 안정성 확보
- 공통 화면·테마·컴포넌트를 Base-Theme로 분리하고 고객사별 차이를 Config-Driven UI로 관리 (모듈화)
- React Query 캐싱, 코드 스플리팅, 이미지 최적화, HTTP/2 전환으로 초기 진입·네트워크 병목 개선

#### 성과

- 3,493명 규모 PoC 운영
- 만족도 조사 기준 사용성 4.18, 서비스 만족도 4.06, 완성도 4.05 확보
- AI 답변 출력 시간을 10초에서 4초로 단축
- 초기 서비스 진입 시간을 30초에서 6초로 단축
- Lighthouse 91점 확보
- 400건 발화 검증 기준 답변 화면 정상 출력률 100% 달성
- 신규 AI 챗봇 구축 기간을 10주에서 2주로 단축 가능한 공통 구조 확보

**기술:** React, TypeScript, TanStack Query, Recoil, SSE, Python, Chart.js, Tailwind CSS

---

### 3. 대웅제약 | 테스트·빌드·배포 자동화 및 AI 활용 개발 프로세스

**테스트 자동화·빌드 프로세스·FE AX SOP 기반 서비스 운영 품질 기준 수립**

- 기간: 2026년 상반기
- 적용 서비스: AI코치, 비즈36.5, 바이오에이지
- 책임 범위: 빌드·배포 파이프라인 자동화, 테스트·배포 전후 검증 흐름 구축, 운영 지표 대시보드, FE 개발 기준 문서화

#### 문제

서비스 수와 공통 컴포넌트가 늘면서 수동 QA, 반복 UI 개발, 배포 전후 확인, 운영 지표 조회가 병목이 되었습니다. AI 생성 코드의 품질·보안·일관성을 검증할 기준도 마련되어 있지 않아, 서비스 안정 운영을 위한 자동화 기준과 팀 공유 체계가 필요했습니다.

#### 주요 실행

- Playwright 기반 주요 사용자 흐름과 E2E 회귀 시나리오를 자동화
- Storybook 중심으로 컴포넌트 상태별 개발·검증 절차 수립
- LLM 응답 검증, 타입·테스트·빌드 확인, 배포 전후 확인을 하나의 품질 흐름으로 연결
- Jenkins CI/CD 빌드·검증·배포 파이프라인을 정비하고 WebView 호환성 검증 기준 수립
- GA4·PostHog 기반 운영 지표 대시보드를 구성해 기획·운영 부서가 직접 데이터를 확인할 수 있도록 개선
- AI 생성 코드의 컨텍스트 관리, 금지 패턴, 보안 위험, 검증 절차를 FE AX SOP로 문서화 (AI 활용 자동화)
- 개발 세미나 12회 운영, 기술 문서 48건 작성으로 팀 학습·적용·공유 체계 정착

#### 성과

- Playwright 기반 600여 건 E2E 회귀 시나리오 자동화
- 반복 QA 시간을 3시간에서 1시간으로 단축
- 반복 컴포넌트 개발·검증 시간을 90분에서 15분으로 단축
- 운영 데이터 확인 절차를 3단계에서 1단계로 전환
- 기획-개발 검증 리드타임을 2일에서 1일로 단축
- 테스트 커버리지 98% 수준 확보 (내부 측정 기준)

**기술:** Playwright, Storybook, Jest, ESLint, TypeScript, Jenkins, GitLab CI/CD, GA4, PostHog

---

### 4. 삼성물산 | 데이터 플랫폼·모바일 애플리케이션

**Vue 3 기반 대용량 데이터 대시보드 성능 최적화 및 React Native 모바일 서비스 고도화**

- 기간: 2024.10 ~ 2025.04
- 소속: 내담씨앤씨 SI 프로젝트
- 책임 범위: 대용량 데이터 시각화 성능 개선, Spring REST API·데이터 연동, React Native iOS·Android 개발·배포

#### 문제

Web 대시보드는 대용량 테이블·시계열 데이터를 빠르게 제공해야 했고, 모바일 앱은 반복 API 호출과 플랫폼별 동작 차이로 사용자 대기 시간과 운영 부담이 발생했습니다.

#### 주요 실행

- Vue 3·ECharts·RealGrid 기반 대용량 데이터 시각화 화면 개발
- 테이블·차트 렌더링 생명주기를 분리하고 Lazy Rendering을 적용해 초기 처리량 최적화 (성능 개선)
- Spring REST API와 필터링·정렬 로직을 설계하고 사용자 역할별 데이터 조회·표현 구조 구성 (API 설계)
- 검색 시마다 API를 호출하던 구조를 화면 진입 시 비동기 선조회 후 Recoil에 저장하는 방식으로 변경 (코드 품질·UX 개선)
- React Native 기반 iOS·Android 공통 기능, Firebase FCM 실시간 알림, 플랫폼별 배포·운영 이슈 대응

#### 성과

- 대시보드 렌더링 시간을 2.5초에서 1초대로 개선
- React Native 앱 검색 응답 시간을 5초에서 1초로 단축
- Web 데이터 흐름부터 iOS·Android 개발·배포까지 크로스플랫폼 개발 범위 확보

**기술:** Vue 3, React Native, TypeScript, ECharts, RealGrid, Java, Spring, REST API, MyBatis, MySQL, Recoil, SQLite, Firebase FCM

---

### 5. 한국미스미 | 글로벌 B2B 커머스

**PHP 레거시 Next.js 전환 및 글로벌 B2B 서비스 성능·배포·모니터링 구조 개선**

- 기간: 2022.06 ~ 2024.10
- 소속: 내담씨앤씨 SI 프로젝트
- 책임 범위: PHP·jQuery 레거시 분석, Next.js 단계적 전환, 렌더링·성능·SEO·다국어·배포 자동화·모니터링 구조 개선

#### 문제

PHP·jQuery 기반 글로벌 쇼핑몰은 화면 결합도가 높아 확장과 유지보수가 어려웠고, 긴 초기 접근 시간과 단일 렌더링 구조로 성능·검색 노출을 함께 최적화하기 어려웠습니다. 다국어 환경과 국가별 배포 요건을 지원하면서 단계적으로 현대화해야 했습니다.

#### 주요 실행

- PHP·jQuery 레거시를 Next.js·React·TypeScript 컴포넌트 구조로 단계적 전환 (레거시 점진 전환)
- 페이지 특성별 SSR·CSR 렌더링 전략 분리 (Node 런타임 환경)
- 상품 비교, 멀티 다운로드 등 복잡한 기능을 공통 컴포넌트와 Custom Hook으로 구조화 (모듈화)
- Redux 기반 상태 관리로 화면 간 상태 일관성 확보
- Lighthouse 병목 분석 후 Lazy Loading, 비동기 API, 리소스 최적화 적용 (성능 최적화)
- i18next 기반 글로벌 다국어 구조 구축
- Vercel 배포 자동화, Datadog·GA·Adobe Analytics 기반 운영 모니터링 체계 구축 (빌드·배포 자동화)

#### 성과

- 페이지 접근 시간을 8초에서 2초로 단축
- Next.js 전환 후 기존 PHP 서비스 대비 평균 로딩 속도 약 50% 개선
- 화면 개발에서 아키텍처, 성능, 다국어, 배포 자동화, 모니터링까지 책임 범위 확장

**기술:** Next.js, React, TypeScript, JavaScript, Redux, RxJS, i18next, PHP, jQuery, Twig, Vercel, Datadog, Lighthouse, GA, Adobe Analytics
