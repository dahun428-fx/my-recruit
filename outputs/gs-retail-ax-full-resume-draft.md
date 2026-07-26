# 정다훈 이력서 및 경력기술서 — GS리테일 AX본부 개발 프로젝트 지원용

## 프론트엔드 AI Transformation(FE AX)으로 팀 생산성을 끌어올리는 Product Engineer

## 인적사항

- 이름: 정다훈
- 포지션: Full-stack Product Engineer
- 경력: 총 5년 9개월
- 휴대폰: 010-4346-0429
- Email: dahun428@naver.com
- 주소: 경기 구리시 인창동
- Portfolio: github.com/dahun428-fx
- 병역: 군필 (육군 병장)

## 요약

5년 9개월간 **프론트엔드에서 풀스택으로 확장해 온 Product Engineer**로, **AI Agent를 활용한 프론트엔드 AI Transformation(FE AX)**에 익숙하고 팀 내 **AI 활용 확산과 개발 생산성 향상**을 이끌어 왔습니다. 화면 구현을 넘어 API 응답 정책·오류 대응·배포·운영까지 제품 완성도 관점으로 설계하고, 사람마다 달랐던 AI 활용 방식을 **FE AX 표준(SOP)**으로 묶어 팀 공통 생산성으로 전환해 온 것이 강점입니다.

대웅제약 AI추진팀에서 AI 건강검진 챗봇 PoC를 3,493명 규모 실사용 제품으로 배포·운영하고, 외주 중심 B2B 임직원 건강 플랫폼을 풀스택으로 내재화했으며, Codex·Claude Code 활용 개발과 Playwright E2E·배포 검증 자동화로 팀 개발 기준을 세웠습니다. 내담씨앤씨에서는 글로벌 B2B 커머스의 Next.js 전환과 대용량 데이터 대시보드 성능 개선을 담당했습니다. 현업과 가설을 정의하고 프로토타입을 실사용 기준으로 배포·운영하며 그 경험을 재사용 표준으로 남기는 AX본부의 일하는 방식이 지금까지 해온 일과 맞닿아 있습니다.

## 핵심 성과

### 1. Codex·Claude Code 활용 개발과 검증 기준의 표준화 (Harness Engineering·재사용 표준화)

Codex·Claude Code 등 AI 코딩 에이전트로 개발하면서, 생성 코드의 컨텍스트 관리·금지 패턴·보안 위험·검증 절차를 **FE AX 표준(SOP)으로 수립**해 사람마다 달랐던 AI 활용 개발 방식을 팀이 반복 사용할 수 있는 **표준으로 정리**했습니다. Playwright E2E 자동화를 단독으로 판단·도입해 팀이 채택하게 만들었고, 개발 세미나 12회와 기술 문서 48건으로 이 표준을 조직에 축적했습니다.

### 2. AI 서비스 프로토타입을 실사용 제품으로 배포·운영 (프로토타입 구축 → 배포·운영)

목업 수준의 AI 건강검진 챗봇을 **3,493명 규모 PoC에서 실사용 가능한 서비스로 고도화**했습니다. SSE 기반 실시간 응답과 Markdown·표·링크·차트 렌더링 계층을 구축해 **AI 답변 출력 시간을 10초 → 4초(약 60%), 초기 진입 시간을 30초 → 6초(약 80%)로 단축**하고, 400건 발화 검증 기준 답변 화면 정상 출력률 100%와 AI 챗봇 화면 기준 Lighthouse 91점을 확인했습니다.

### 3. 가설·판정 기준 기반 품질 검증 (판정 기준 수립·MECE 검증)

현업과 검증 대상을 MECE로 분해해 발화 테스트·LLM 응답 검증·타입/빌드·배포 전후 확인을 **판정 기준으로 묶고**, Playwright로 주요 사용자 흐름과 회귀 시나리오 600여 건을 자동화했습니다. 같은 판정 기준으로 반복 검증할 수 있게 정리해 배포마다 동일 기준을 적용하며 **반복 QA 시간을 3시간 → 1시간으로** 줄였습니다.

### 4. 비개발 직군이 직접 검증할 수 있는 확인 환경 설계 (비개발 직군 수정·테스트 환경)

기획·운영이 배포 전후 상태와 운영 지표를 직접 확인할 수 있도록 절차를 자동화해, **운영 데이터 확인을 3단계 수작업 → 1단계로**, 기획–개발 검증 리드타임을 2일 → 1일로 줄였습니다. Storybook 기반으로 컴포넌트를 독립 확인 가능하게 만들어 반복 컴포넌트 개발을 90분 → 15분(약 83%)으로 단축했습니다.

### 5. Python·데이터 처리와 AI 응답 로직 개선 (데이터 모델·가공·AI 응답)

MySQL 데이터 모델을 신규 설계하고 역할별 조회·필터링·정렬 로직을 SQL로 개발했으며, React 전용 데이터 집계·프록시(BFF) API를 Node.js로 신규 구축해 다중 백엔드 데이터 연동을 단일 계층으로 정리했습니다. AI 챗봇 서버의 Python 프롬프트 구성·응답 후처리(Markdown·표·링크 변환) 로직을 수정·개선했고, VectorDB·RAG 구현과 Langchain 활용 파인튜닝 과정에 참여하며 Python pandas로 기초 데이터 처리를 다뤘습니다.

### 6. AWS S3·EC2 기반 배포·운영 (AWS 기반 개발·운영)

바이오에이지 서비스에서 AWS S3 정적 호스팅 기준으로 배포·빌드를 수행하고, 별도로 EC2에서 서버 운영을 다뤘습니다. 외주로 도입된 버전을 유지보수·수정해 서울성모병원에 납품했습니다. 대웅 AI추진팀 CI/CD 정비 과정에서 **Jenkins 빌드·검증·배포 리드타임을 10분 → 2분(약 80%)으로** 단축했습니다.

## 경력

### 대웅제약 AI추진팀

- 기간: 2025.07 ~ 재직중
- 직무: Full-stack Product Engineer / 프론트엔드 아키텍처 설계·개발 / AI 서비스 제품화 / 팀 개발 기준 수립

Codex·Claude Code 등 AI 코딩 에이전트로 개발하면서 생성 코드의 검증 기준을 **FE AX 표준(SOP)**으로 수립해 팀 표준으로 정착시켰습니다. AI 건강검진 챗봇의 실시간 응답 처리와 배포·운영, 데이터 집계 API·AI 응답 로직 개선, 임직원 건강 플랫폼 풀스택 내재화, AWS S3·EC2 기반 배포·운영을 담당했습니다.

- Codex·Claude Code 활용 개발, **FE AX 표준(SOP) 수립**으로 AI 활용 개발 기준을 팀 표준으로 정착 (Harness Engineering)
- SSE 기반 실시간 LLM 응답·렌더링 계층 구축, AI 답변 출력 **10초 → 4초**, 초기 진입 **30초 → 6초**
- Playwright E2E 자동화 단독 도입, 주요 흐름·회귀 시나리오 600여 건 자동화, 반복 QA **3시간 → 1시간** (판정 기준·MECE 검증)
- React 전용 데이터 집계·프록시(BFF) API를 Node.js로 신규 구축, MySQL 데이터 모델 신규 설계
- AI 챗봇 서버 Python 프롬프트·응답 후처리 로직 개선 참여, VectorDB·RAG·Langchain·pandas 활용 참여
- AWS S3 정적 배포·빌드와 EC2 서버 운영, Jenkins CI/CD 정비로 배포 리드타임 **10분 → 2분**

### 내담씨앤씨 SI사업부

- 기간: 2020.10 ~ 2025.06
- 직무: 대리 / 웹 프론트엔드 개발자 / 레거시 전환·성능 최적화

글로벌 B2B 커머스·데이터 플랫폼·모바일 앱 프로젝트에서 프론트엔드 아키텍처 개선과 성능 최적화를 수행했습니다. **PHP·jQuery 레거시를 React·Next.js·TypeScript 구조로 단계적으로 전환**하고, Vue 3·React Native로 데이터 대시보드와 모바일 서비스를 함께 개발했습니다.

- **PHP·jQuery 기반 글로벌 B2B 커머스를 React·Next.js·TypeScript 구조로 단계적 전환** (레거시 점진 전환)
- Lighthouse 병목 분석·리소스 최적화로 페이지 접근 시간 **8초 → 2초** 단축
- Vue 3·ECharts·RealGrid 기반 대용량 데이터 대시보드 Lazy Rendering 적용, 렌더링 **2.5초 → 1초대**
- React Native 기반 iOS·Android 앱 기능 고도화, 검색 응답 **5초 → 1초** 단축
- Vercel 배포 자동화, Lighthouse·GA·Adobe Analytics·Datadog 기반 성능·SEO·오류 추적 체계 운영 (관측성)

## 기술

### 클라우드·배포·운영

AWS S3(정적 배포·빌드) · AWS EC2(서버 운영) · Jenkins CI/CD · GitLab CI/CD · Vercel

- 바이오에이지 서비스에서 AWS S3 기반으로 정적 배포·빌드를 수행하고, 별도로 EC2에서 서버 운영을 다룸
- 대웅 AI추진팀 CI/CD 정비 과정에서 Jenkins 빌드·검증·배포 리드타임을 10분 → 2분(약 80%)으로 단축
- 배포 전후 상태와 운영 지표를 기획·운영이 직접 확인할 수 있도록 확인 절차 자동화

### AI 활용 개발·검증

Codex · Claude Code · Harness Engineering · LLM 챗봇 제품화 · SSE Streaming · AI 생성 코드 검증 SOP

- Codex·Claude Code로 개발하고, 생성 코드의 금지 패턴·보안 위험·검증 절차를 FE AX 표준(SOP)으로 수립
- AI 챗봇 PoC를 실사용 서비스로 배포·운영하고 답변 렌더링·오류 대응을 안정화

### 데이터·AI·언어

Python · SQL(MySQL · Oracle) · TypeScript · JavaScript · Java
AI 데이터 파이프라인(VectorDB · RAG · LangChain) 참여 경험 · pandas 기초 데이터 처리

- MySQL 데이터 모델을 신규 설계하고 역할별 조회·필터링·정렬 로직을 SQL로 개발
- React 전용 데이터 집계·프록시(BFF) API를 Node.js로 신규 구축해 다중 백엔드 데이터 연동을 단일 계층으로 정리
- AI 챗봇 서버의 Python 프롬프트·응답 후처리 로직 수정·개선 참여
- VectorDB·RAG 구현과 Langchain 활용 파인튜닝 과정에 참여, Python pandas로 기초 데이터 처리 참여

### 품질·검증 자동화

Playwright · Storybook · Jest · ESLint

- Playwright E2E 자동화를 단독 판단·도입해 주요 사용자 흐름·회귀 시나리오 600여 건 자동화, 반복 QA 3시간 → 1시간
- 판정 기준을 세워 400건 발화 검증 기준 정상 출력률 100% 확인 (내부 측정 기준)

### 프론트엔드

React · Next.js · Vue 3 · React Native · TanStack Query · Recoil · Tailwind CSS

- Config-Driven UI·Base-Theme로 고객사별 화면 확장을 반복 대응 가능하게 정비
- 대용량 데이터 시각화와 성능 개선(렌더링 2.5초 → 1초대)

---

## 경력기술서

### 1. 대웅제약 | AI 활용 개발 검증 기준·검증 환경 표준화

- 기간: 2026년 상반기
- [주요 업무]: AI코치·비즈36.5·바이오에이지 운영 서비스에서 Codex·Claude Code 활용 개발·FE AX 표준(SOP) 수립으로 팀 개발 기준 수립, 검증·운영 확인 절차 설계 (FE AX·Harness Engineering)

#### 문제

수동 발화 테스트, 반복 UI 개발, 배포 전후 확인, 운영 지표 조회가 병목이었고, AI로 생성한 코드의 품질·보안·일관성을 판정할 팀 공유 기준이 없었습니다.

#### 주요 실행

- Codex·Claude Code 등 AI 코딩 에이전트로 개발하고, 생성 코드의 컨텍스트 관리·금지 패턴·보안 위험·검증 절차를 FE AX 표준(SOP)으로 수립 (Codex·Claude Code 활용·재사용 표준)
- E2E 발화 테스트·LLM 응답 검증·타입/테스트/빌드·배포 전후 확인을 판정 기준으로 정리 (판정 기준 수립·하네스)
- Playwright E2E 자동화를 단독으로 판단·도입해 주요 사용자 흐름·회귀 시나리오 600여 건 자동화, 팀 채택으로 확산 (MECE 검증)
- Storybook 기반 컴포넌트 독립 개발·확인 절차 수립 (비개발 직군 확인 환경)
- GA4·PostHog 기반 운영 데이터 확인 절차 구축 (비개발 직군 수정·테스트)

#### 성과

- 반복 QA 시간 3시간 → 1시간 단축
- 운영 데이터 확인 3단계 → 1단계 전환
- 반복 컴포넌트 개발 90분 → 15분(약 83%) 단축
- 기획–개발 검증 리드타임 2일 → 1일 단축

**기술:** Playwright · Storybook · Jest · ESLint · TypeScript · Jenkins · GitLab CI/CD · GA4 · PostHog · Codex · Claude Code

---

### 2. 대웅제약 | AI 건강검진 챗봇 제품화 및 배포·운영

- 기간: 2025.07 ~ 2025.10
- [주요 업무]: 프론트엔드 아키텍처 설계·개발과 AI/백엔드 응답 정책 조율, SSE 기반 실시간 응답·렌더링 계층과 Config-Driven UI 기반 고객사별 확장 구조 설계

#### 문제

목업 수준의 AI 챗봇을 실사용 서비스로 배포·운영해야 했고, LLM 답변 지연·Markdown/표/링크 렌더링·오류 대응·고객사별 화면 확장 방식이 부족했습니다.

#### 주요 실행

- AI 개발자와 API 응답 형식·스트리밍·오류 정책 정의 (현업과 문제 정의)
- SSE 기반 실시간 응답과 중지/재시도/오류 상태를 포함한 대화 흐름 설계
- Markdown 렌더링 계층 구축, 표·목록·링크·차트의 React 컴포넌트 변환
- XSS 필터링과 404/500/LLM 오류 가드레일 적용
- Base-Theme·Config-Driven UI로 고객사별 테마·문구·기능 노출 조건 분리 (재사용 표준화)

#### 성과

- 3,493명 규모 PoC를 실사용 서비스로 전환
- AI 답변 출력 10초 → 4초(약 60%), 초기 진입 30초 → 6초(약 80%) 단축
- 400건 발화 검증 기준 답변 화면 정상 출력률 100%, AI 챗봇 화면 기준 Lighthouse 91점 확인
- 신규 고객사 온보딩 시 Base-Theme 기반 FE 커스터마이징·납품 기간을 최초 구현 10주 대비 2주로 단축 가능한 구조 확보 (10주=챗봇 최초 구현, 2주=신규 고객사 FE 납품 기준)

**기술:** React · TypeScript · TanStack Query · Recoil · SSE · Chart.js · Tailwind CSS

---

### 3. 대웅제약 | 데이터 집계 API 및 AI 챗봇 Python·RAG 로직 개선

- 기간: 2025.07 ~ 재직중
- [주요 업무]: 프론트 전용 BFF API 신규 구축, AI 챗봇 Python 로직 수정·개선, VectorDB·RAG·Langchain·pandas 활용 참여

#### 문제

신규 기능에서 React 프론트가 여러 백엔드 데이터를 집계·가공해 받아야 했고, AI 챗봇 응답의 프롬프트 구성·후처리 품질과 검색 정확도를 개선해야 했습니다.

#### 주요 실행

- React 전용 데이터 집계·프록시(BFF) REST API를 Node.js(Express)로 신규 구축
- 비동기 I/O와 프론트–백엔드 TypeScript 스택 통일을 이유로 Node 채택
- AI 챗봇(Python) 서버의 프롬프트 구성·응답 후처리(Markdown·표·링크 변환) 로직 수정·개선
- VectorDB·RAG(Retrieval-Augmented Generation) 구현과 Langchain 활용 파인튜닝 과정에 참여 (AI 데이터 파이프라인 활용 경험)
- Python pandas로 데이터 처리 작업에 참여 (Python 데이터 가공)

#### 성과

- React 프론트의 다중 백엔드 데이터 연동을 단일 BFF 계층으로 단순화
- AI 챗봇 응답 포맷·프롬프트 품질 개선에 기여
- VectorDB·RAG·Langchain 파인튜닝 실사용 환경 참여 경험 확보

**기술:** Node.js · Express · TypeScript · Python · LangChain · VectorDB · RAG · pandas · REST API · SSE

---

### 4. 대웅제약 | B2B 임직원 건강 플랫폼 풀스택 내재화 및 배포·운영

- 기간: 2025.11 ~ 2026.02
- [주요 업무]: 외주 서비스 내재화를 위한 서비스·데이터 구조 분석과 End-to-End 개발, jQuery·Thymeleaf→React 점진 전환, WebView 앱 운영·CI/CD 정비

#### 문제

외주 중심으로 운영되던 검진 예약 서비스의 화면·서버·DB가 기능별로 결합돼 변경 영향 파악이 어려웠고, Web·Admin·App 권한과 출력 정책이 달랐습니다.

#### 주요 실행

- 기존 소스·DB 스키마 분석, 화면 요청부터 Controller·Service·Query·DB·출력까지 정리
- 신규 건강관리 기능의 MySQL 데이터 모델·Spring Boot 서버 로직·REST API·Web/Admin을 End-to-End 개발
- jQuery/Thymeleaf와 React가 화면 단위로 공존하는 점진적 전환 설계 (레거시 점진 전환)
- Jenkins 빌드·검증·배포와 WebView 호환성 검증 기준 수립 (배포·운영)

#### 성과

- 9주 내 108개 페이지·82개 화면 전환, 신규 건강관리 기능 3건 End-to-End 개발
- 고객사별 CI·메뉴·기능 노출 변경을 1주 내 대응 가능하게 정비

**기술:** React · TypeScript · Java · Spring Boot · REST API · MySQL · jQuery · Thymeleaf · Jenkins CI/CD · WebView

---

### 5. 대웅제약 | 바이오에이지 서비스 유지보수 및 AWS S3·EC2 배포·운영

- 기간: 2025년
- [주요 업무]: 외주 도입 바이오에이지 서비스 유지보수·수정과 UI·운영 리스크 개선, AWS S3 정적 배포·빌드와 EC2 서버 운영, 서울성모병원 납품

#### 문제

외주로 도입된 바이오에이지 서비스의 UI와 데이터 운영 리스크를 제거하고, 서울성모병원 납품 기준으로 안정화해야 했습니다.

#### 주요 실행

- 외주로 도입된 바이오에이지 버전을 유지보수·수정해 서울성모병원에 납품
- AWS S3 기반으로 정적 배포·빌드를 수행하고, 별도로 EC2에서 서버 운영을 다룸 (AWS 기반 개발·운영)
- 운영 서비스의 UI와 데이터 운영 리스크 개선

#### 성과

- 외주 도입 서비스를 내부 유지보수·수정 가능한 상태로 안정화해 서울성모병원 납품

**기술:** AWS S3(정적 배포·빌드) · AWS EC2(서버 운영) · WebView · Tailwind CSS

---

### 6. 삼성물산 | 데이터·모바일 서비스 고도화

- 기간: 2024.10 ~ 2025.04
- 소속: 내담씨앤씨 SI 프로젝트
- [주요 업무]: Vue 3 기반 대용량 데이터 대시보드 성능 최적화와 데이터 시각화·REST API 연동, React Native 모바일 서비스 고도화·배포

#### 문제

Web 대시보드의 대용량 테이블·시계열 렌더링과 모바일 앱의 반복 API 호출·플랫폼별 동작 차이가 사용자 대기와 운영 부담을 만들었습니다.

#### 주요 실행

- Vue 3·ECharts·RealGrid 기반 대용량 데이터 화면 개발, 렌더링 생명주기 분리와 Lazy Rendering 적용
- Spring REST API와 필터링·정렬 로직 설계, 역할별 데이터 조회·표현 구조 개발
- React Native 앱 검색·조회 흐름 개선 및 플랫폼별 이슈 대응

#### 성과

- 대용량 데이터 대시보드 렌더링 2.5초 → 1초대 개선
- React Native 앱 검색 응답 5초 → 1초(약 80%) 단축

**기술:** Vue 3 · React Native · TypeScript · ECharts · RealGrid · Java · Spring · REST API · MyBatis · MySQL

---

### 7. 한국미스미 | 글로벌 B2B 커머스 개선 및 Next.js 전환

- 기간: 2022.06 ~ 2024.10
- 소속: 내담씨앤씨 SI 프로젝트
- [주요 업무]: 사용자 기능 개발과 PHP·jQuery 레거시 분석·Next.js·React 전환, 성능·SEO·다국어·모니터링 구조 개선

#### 문제

PHP·jQuery 레거시 환경에서 유지보수성·페이지 성능·SEO·다국어·오류 추적이 필요했습니다.

#### 주요 실행

- PHP·jQuery 기반 B2B 쇼핑몰을 React·Next.js·TypeScript로 전환 (레거시 점진 전환)
- 페이지 특성별 SSR·CSR 렌더링 전략 분리, Lazy Loading·비동기 API·리소스 최적화 적용
- Lighthouse·GA·Adobe Analytics·Datadog 기반 성능·SEO·오류 추적 운영 (관측성)

#### 성과

- 페이지 접근 시간 8초 → 2초 단축
- Next.js 전환 후 기존 PHP 서비스 대비 평균 로딩 속도 약 50% 개선

**기술:** Next.js · React · TypeScript · Redux · RxJS · i18next · PHP · jQuery · Vercel · Datadog

---

## 학력

- 2010.03 ~ 2017.02 성공회대학교 일어일본학과 졸업
  - 복수전공: 경영학과
  - 학점: 3.8 / 4.5
- 2010 여의도고등학교 졸업

## 교육

- 2020.03 ~ 2020.09 웹 콘텐츠 개발을 위한 응용SW엔지니어링 / 중앙에이치티에이㈜
  - Java 기반 웹 애플리케이션의 백엔드와 프론트엔드 개발 과정 이수
  - 습득 기술: HTML5, JavaScript, jQuery, Vue.js, CSS, JSP, Java, Spring Framework, AWS, RESTful API, OracleDB, MariaDB, Git/GitHub

## 자격

- 정보처리기사 / 한국산업인력공단 (2020.08)

## 어학

- 영어: TOEIC 825점 (2024.05)
- 일본어: JLPT 1급 (2018.08)
</content>
</invoke>
