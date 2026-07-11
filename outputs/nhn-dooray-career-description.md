# 정다훈 경력기술서 (NHN Dooray! 지원용)

회사 > 프로젝트 단위로 정리한 경력기술서입니다. 각 프로젝트는 배경, 주요 역할
및 담당업무, 주요 성과, 사용 기술 순으로 기술합니다.

---

## 대웅제약 AI추진팀

- 기간: 2025.07 ~ 재직중
- 직무: Frontend 중심 Product Engineer (프론트엔드 아키텍처 / AI 서비스 제품화)

### AI코치 — AI 건강검진 챗봇 실서비스 전환 및 FE 공통 품질 기준 구축

- 기간: 2025.07 ~ 2025.10 (챗봇 실서비스 고도화) · 2026년 상반기 (FE 공통 품질·개발 기준)

목업 수준의 AI 건강검진 챗봇(AI코치)을 3,493명이 검증하는 실사용 서비스로 고도화하고, 서비스 확대에 맞춰 AI코치를 비롯한 비즈36.5·바이오에이지 운영 서비스 전반의 프론트엔드 공통 품질·개발 기준을 세워야 했다.

#### 주요 역할 및 담당업무

- 프론트엔드 아키텍처 설계·개발 및 AI·백엔드 응답 형식·스트리밍·오류 정책 조율
- SSE 기반 실시간 응답, 답변 중지·재시도·오류 상태 흐름 설계·구현
- Markdown 전용 렌더링 계층 구현(표·목록·링크·차트를 React 컴포넌트로 변환), XSS 필터링·404·500·LLM 오류 가드레일 적용
- Base-Theme·Config-Driven UI 기반 공통 컴포넌트 구조 구축(고객사별 화면·테마·문구·기능 노출 조건 분리)
- AI코치·비즈36.5·바이오에이지 운영 서비스 전반의 FE 공통 품질·개발 기준 수립: Playwright E2E·Storybook 컴포넌트 검증·배포 전후 확인을 하나의 품질 흐름으로 통합
- AI 생성 코드의 컨텍스트 관리·금지 패턴·보안 위험·검증 절차를 FE AX SOP로 문서화
- React Query 캐싱·코드 스플리팅·이미지 최적화·HTTP/2 전환으로 초기 진입·네트워크 병목 개선

#### 주요 성과

- 3,493명 규모 PoC를 실사용 가능한 서비스로 전환, 만족도 조사 기준 사용성 4.18·서비스 만족도 4.06·완성도 4.05 확보
- AI 답변 출력 시간 10초→4초(60%), 초기 서비스 진입 30초→6초(80%) 단축
- 400건 발화 검증 기준 답변 화면 정상 출력률 100%, Lighthouse 91점 달성
- (AI코치·비즈36.5·바이오에이지 공통 품질 기준) Playwright 기반 600여 건 E2E 회귀 시나리오 자동화, 반복 QA 시간 3시간→1시간 단축
- (공통 품질 기준) 반복 컴포넌트 개발·검증 시간 90분→15분 단축, 테스트 커버리지 98% 수준 확보
- 신규 AI 챗봇 구축 기간을 10주→2주로 단축 가능한 공통 구조 확보

#### 사용 기술

React, TypeScript, TanStack Query, Recoil, SSE, Chart.js, Tailwind CSS, Playwright, Storybook, Jest, ESLint, Jenkins, GitLab CI/CD, GA4, PostHog

---

### 비즈36.5 — 임직원 건강 플랫폼 풀스택 내재화

- 기간: 2025.11 ~ 2026.02

외주 중심으로 운영되던 검진 예약 서비스(비즈36.5)를 내부에서 개발·운영 가능한 임직원 건강 플랫폼으로 전환해야 했고, jQuery·Thymeleaf 화면과 Spring Boot·MySQL 구조가 기능별로 결합돼 변경 영향 파악과 고객사별 대응이 어려웠다.

#### 주요 역할 및 담당업무

- React·TypeScript 기반 Web/Admin 화면 개발 및 jQuery·Thymeleaf↔React 화면 단위 점진 전환 구조 설계
- 사용자 권한·메뉴·브랜딩·데이터 출력 정책을 공통 기준으로 정리해 고객사별 배포 대응 구조 확보
- 신규 건강관리 기능의 MySQL 데이터 모델·Spring Boot 서버 로직·REST API를 End-to-End 개발
- 화면 요청부터 Controller·Service·Query·DB·화면 출력까지 데이터 흐름과 의존 관계 정리
- Jenkins 빌드·검증·배포 파이프라인과 WebView 호환성 검증 기준 수립

#### 주요 성과

- 9주 내 108개 페이지·82개 화면을 임직원 건강 플랫폼으로 전환
- 건강관리 신규 기능 3건을 DB~서버~API~Web/Admin 전 구간 End-to-End 개발
- 외주 의존 기능 변경·배포를 DB·백엔드·Web·Admin·App 전 영역에서 내부 대응 가능한 구조로 전환
- 고객사별 CI·메뉴·기능 노출 변경을 1주 내 대응 가능한 운영 구조 확보

#### 사용 기술

React, TypeScript, jQuery, Thymeleaf, Java, Spring Boot, REST API, MySQL, Tailwind CSS, Jenkins CI/CD, WebView, iOS, Android

---

## 내담씨앤씨 SI사업부

- 기간: 2020.10 ~ 2025.06
- 직무: 웹개발자 / 프론트엔드 개발자 (고객사 SI 파견 프로젝트)

### 삼성물산 — 데이터 플랫폼·React Native 모바일 서비스 고도화

- 기간: 2024.10 ~ 2025.04 (SI 파견)

Web 대시보드는 대용량 테이블·시계열 데이터를 빠르게 제공해야 했고, React Native 앱은 반복 API 호출과 플랫폼별 동작 차이로 사용자 대기 시간과 운영 부담이 컸다.

#### 주요 역할 및 담당업무

- Vue 3·ECharts·RealGrid 기반 대용량 데이터 시각화 화면 개발
- 테이블·차트 렌더링 생명주기 분리 및 Lazy Rendering 적용으로 초기 처리량 최적화
- Spring REST API와 필터링·정렬 로직 설계, 사용자 역할별 데이터 조회·표현 구조 구성
- 검색마다 API를 호출하던 구조를 화면 진입 시 비동기 선조회 후 Recoil 저장 방식으로 개선
- React Native iOS/Android 공통 기능, Firebase FCM 실시간 알림, 플랫폼별 배포·운영 이슈 대응

#### 주요 성과

- 대용량 데이터 대시보드 렌더링 시간 2.5초→1초대 개선
- React Native 앱 검색 응답 시간 5초→1초(80%) 단축
- Web 데이터 흐름부터 iOS·Android 개발·배포까지 크로스플랫폼 개발 범위 확보

#### 사용 기술

Vue 3, React Native, TypeScript, ECharts, RealGrid, Java, Spring, REST API, MyBatis, MySQL, Recoil, SQLite, Firebase FCM

---

### 한국미스미 — 글로벌 B2B 커머스 Next.js 전환 및 성능 개선

- 기간: 2022.06 ~ 2024.10 (SI 파견)

PHP·jQuery 기반 글로벌 쇼핑몰은 화면 결합도가 높아 확장·유지보수가 어려웠고, 긴 초기 접근 시간과 단일 렌더링 구조로 성능과 검색 노출을 함께 최적화하기 어려웠다.

#### 주요 역할 및 담당업무

- PHP·jQuery 레거시를 Next.js·React·TypeScript 컴포넌트 구조로 단계적 전환
- 페이지 특성별 SSR·CSR 렌더링 전략 분리
- 상품 비교·멀티 다운로드 등 복잡한 기능을 공통 컴포넌트·Custom Hook으로 구조화
- Redux 기반 상태 관리로 화면 간 상태 일관성 확보
- Lighthouse 병목 분석 후 Lazy Loading·비동기 API·폰트 최적화 적용
- i18next 기반 글로벌 다국어 구조, Vercel 배포 자동화, Datadog·GA·Adobe Analytics 모니터링 체계 구축

#### 주요 성과

- 페이지 접근 시간 8초→2초 단축
- Next.js 전환 후 기존 PHP 서비스 대비 평균 로딩 속도 약 50% 개선
- 화면 개발에서 아키텍처·성능·다국어·배포 자동화·모니터링까지 책임 범위 확장

#### 사용 기술

Next.js, React, TypeScript, JavaScript, Redux, RxJS, i18next, PHP, jQuery, Twig, Vercel, Datadog, Lighthouse, GA, Adobe Analytics
