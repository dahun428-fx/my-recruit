# smilegate-full-resume-draft.md — New Prose Companion

이 파일은 `outputs/smilegate-full-resume-draft.md`의 fast-lane 리뷰 범위를 정의한다.
base-resume.md 대비 신규·수정·비산문 변경 내역만 기록한다.
(최종 갱신: 점수 게이트 R3-1~R3-5 반영 — 2026-08-04)

---

## (a) 신규 작성·수정된 산문 문장

base 원문과 달라진 모든 산문 문장을 "원문 → 수정문" 대비로 기록한다.

### 헤드라인

- 변경 없음. base 원문 verbatim 유지: `프론트엔드에서 풀스택, AI까지 확장해 온 Product Engineer`
- 사유: 헤드라인·요약의 궤적 서사(FE→풀스택→AI)는 불변 항목. 예외 ① Java 가시화 범위는 요약 스택 나열·핵심 성과 칩·기술 표에 한정 (오케스트레이터 검수 2026-08-04 원복).

### 인적사항 — 경력 연차 (reviewer S-1)

- 원문: `경력: 총 5년 9개월`
- 수정: `경력: 총 5년 10개월`
- 사유: 시점 재계산 — 내담씨앤씨 입사 2020.10 ~ 2026.08 기준.

### 요약 (전체 교체 — 복수 수정 누적 반영)

- base 원문:
  `6년차 풀스택 개발자. React·Next.js 프론트엔드부터 Node.js·Spring Boot·MySQL·AWS까지 모든 계층에서 아키텍처를 설계하고 개발하는 Product Engineer입니다. 프론트엔드 개발자로 커리어를 시작해 풀스택으로 영역을 넓혔고, 현재는 프롬프트 → 컨텍스트 → 하네스 엔지니어링으로 Claude·Codex 활용을 단계적으로 심화하며 팀의 AX 전환을 리드하고 있습니다.`

- 최종 수정문 (R3-1·R3-2 반영):
  `6년차 풀스택 개발자. Java·Spring Boot·MySQL·REST API 백엔드부터 React·Next.js 프론트엔드까지 모든 계층에서 아키텍처를 설계하고 개발하는 Product Engineer입니다. 프론트엔드 개발자로 커리어를 시작해 풀스택으로 영역을 넓혔고, AI 건강검진 챗봇을 설계·개발해 실서비스로 제품화하고, 임직원 건강검진 통합플랫폼을 풀스택으로 내재화했으며, 현재는 팀의 AX 전환을 리드하고 있습니다. Java 웹 개발 교육과 정보처리기사로 백엔드 기반을 닦고, 삼성물산 현장 데이터 플랫폼에서 Spring REST API 필터링·정렬 설계를 거쳐, 대웅제약 임직원 건강검진 통합플랫폼에서 MySQL 데이터 모델·Spring Boot·REST API E2E를 단독으로 완수하며 Java 백엔드 역량을 실무에서 단계적으로 쌓아 왔습니다. 대웅제약에서 실현한 AI 웹서비스 제품화·팀 AX 전환 경험을 스마일게이트 AI센터의 AX 포털 고도화와 AI 탑재 웹서비스 개발에 적용하고 싶습니다.`

- 변경 이력:
  - 강조(2026-08-04 소유자 지시): 요약에 볼드 5곳 추가 — 문장당 1개(스택 범위 / AI 챗봇 제품화 / AX 전환 리드 / Java E2E 완수 / 스마일게이트 적용 방향). 문면 무변경, 강조만. base 요약(볼드 0) 대비 이 변형 한정 예외.
  - 메타 라인(2026-08-04 소유자 지시): 경력기술서 5번(미스미) 기간 라인에서 "· 3개 프로젝트" 토큰 제거 — base 원문 "2022.06 ~ 2024.10 · 3개 프로젝트" 대비 이 변형 한정 삭제.
  - 1문: 스택 나열 Java 전진 (예외 ①) — 신규 작문
  - 2문(궤적 서사): base 원문 verbatim 유지 (불변)
  - 3문: S-2(AI 술어 범위) + A-6("등" 제거, 완료/현재 시제 분리) 반영 — 신규 작문
  - 4문 **(R3-1 갱신)**: 연도 나열("삼성물산 Spring REST API(2024)와 …")에서 역량 축적 서사로 재구성. 교육→삼성물산 Spring 설계 경험→대웅 MySQL·Spring Boot·REST API E2E 완수의 단계적 흐름. **연수 합산 수치 미포함**. 근거: EXP-04 "Spring REST API의 필터링·정렬 로직 설계" / EXP-02 "MySQL 데이터 모델, Spring Boot 서버 로직, REST API E2E"
  - 5문 **(R3-2 갱신)**: G-1(스마일게이트 특정 없이 직무 방향성)에서 스마일게이트 AI센터 명시 + 능동 어조("적용하고 싶습니다")로 강화. 엔트리 signals 범위("AX 포털 고도화·AI 탑재 웹서비스 개발") 내 서술. 게임 사업 등 외부 지식 창작 없음.
  - 근거: profile.md Languages Java; EXP-04 Spring REST API; EXP-02 MySQL·Spring Boot E2E; EXP-01 AI 서비스 제품화; EXP-03 AX 전환 리드; target-companies.md Smilegate Job scope

### 경력 섹션 — 대웅제약 AI추진팀 BE 스택 라인

- 원문: `(FE React·Next.js / BE Node.js·Spring Boot·Nest.js·MySQL·PostgreSQL·MongoDB)`
- 수정: `(FE React·Next.js / BE Java·Spring Boot·Node.js·Nest.js·MySQL·PostgreSQL·MongoDB)`
- 사유: "Java" 단어 추가 — 예외 ① Java 상단 가시화. 근거: profile.md Languages Java 등재.

---

## (b) 재사용한 candidate 상태 canonical-lines 문장

스마일게이트 초안에서 `candidate` 상태의 canonical-lines를 verbatim 재사용한 문장 없음.

(경력기술서 본문은 base-resume.md 소유자 확정 문면 그대로 재사용 — 2026-07-27 reviewer+적대검증 통과본이며 이번 편집에서 내부 문장 변경 없음.)

---

## (c) 신규·변경된 비산문 콘텐츠 라인

### 헤드라인 (텍스트)

- 변경 없음. base 원문 verbatim 유지 (불변 항목).

### 핵심 성과 — 번호 재부여 (A-5)

- 문서 순서대로 ①②③④ 재부여:
  - 구 ② 대규모 레거시 전환 → **신 ① 대규모 레거시 전환 · 풀스택 내재화**
  - 구 ① AI 챗봇 → **신 ② AI 건강검진 챗봇 제품화**
  - ③ 대용량 데이터 → ③ 유지
  - ④ 개발 표준화·팀 정착 → ④ 유지

### 핵심 성과 ① — 타이틀·칩·근거 변경 (A-3, A-4, reviewer S-3)

**타이틀 수정** (A-4):
- 구: `② 대규모 레거시 전환 · Java E2E 풀스택`
- 신: `① 대규모 레거시 전환 · 풀스택 내재화`
- 사유: 최대 수치(108p 전환)가 FE 작업이라 Java 간판과 불일치. Java·Spring 토큰은 칩·근거 줄에 유지.

**칩 수정** (A-3 + reviewer S-3 + G-2):
- 구: `기술 리드 · Java·Spring Boot·MySQL·REST API End-to-End · FE–BE 전 구간 단독 설계`
  (reviewer S-3에서 "기술 리드" → "풀스택 총괄"로 먼저 수정됨)
- 신: `풀스택 총괄 · Java·Spring Boot·MySQL·REST API End-to-End · FE–BE 전 구간 단독 개발 · 삼성물산(2024)·대웅(2025) Java/Spring 실무`
- 사유:
  - "단독 설계"는 전환 구조·데이터 모델에 한정; 은행 Role은 "개발" → "단독 개발" (A-3)
  - G-2(점수 게이트 2라운드): Java 백엔드 실무 기간 귀속 가시화. 총 연차 미주장, 프로젝트·연도 단위 표기로 조작 위험 회피. 근거: EXP-04 Spring REST API 2024, EXP-02 Java E2E 2025.11~2026.02. 물결표 표기는 reviewer SF-1(종료 프로젝트의 진행 중 오독 소지)로 연도 단독 표기로 정정(2026-08-04).
  - [F-08 의도된 중복 예외 명기]: 요약 4문이 "삼성물산 Spring REST API(2024)와 대웅제약 Java E2E 개발(2025)"을 이미 명시하므로 엄밀히는 F-08(두 계층 중복 금지) 위반. 그러나 핵심 성과 칩은 스캔 경로 최상단으로 요약 4문보다 먼저 눈에 잡히고, G-2 목적(recruiter/tech-screen 스캔 시 Java 기간 즉시 포착)을 달성하기 위한 의도된 계층 간 중복으로 허용. 예외 명기로 다음 세션 되돌림 방지.

**근거 줄 2행 복원** (A-4):
- 1행(유지): `→ **108개 페이지·82개 화면을 9주 내 단독 전환**, MySQL 데이터 모델부터 Spring Boot·REST API·화면까지 **신규 건강관리 기능 3건 E2E 개발**, 매출 1.0억 기여`
- 2행(신규 복원): `→ **6인 팀 리드로 전면 전환 완수**, 평균 로딩 약 50% 개선 · 페이지 접근 8초 → 2초`
- 사유: base 병합 카드(미스미 성과) 복원. 검증된 성과를 제거로 처리하지 않는 원칙 (A-4). 2행은 EXP-05 canonical approved 라인 근거.
- "3건" 근거: **confirmed** — metric-registry.md `metric-b2b-new-features` (`src-resume-20260624`, `src-eval-2026-h1`); experience-bank.md EXP-02 Actions; canonical-lines.md approved (doosan·cj-enm·nhn·millie)

### 핵심 성과 ② — 칩 변경 (A-8)

- 구 칩: `SaaS 구조 완성 · FE AX 전환 · 분석–설계–구현 전 과정 주도`
- 신 칩: `SaaS 구조 완성 · AI 서비스 제품화 · 분석–설계–구현 전 과정 주도`
- 사유: "FE AX 전환"은 AI센터 JD보다 내부 조직 색채. "AI 서비스 제품화"로 교체. 근거: canonical-lines.md approved EXP-01 헤드라인 "AI 서비스 제품화 및 실시간 응답 UI 구축" (sources: millie).

### 핵심 성과 ④ — 타이틀·칩·근거 줄 전면 재조립 (A-7 + R3-3)

**타이틀 수정** (A-7 → R3-3 갱신):
- 구: `④ 표준화·문서화·조직 자산화`
- 중간(A-7): `④ 개발 표준화·팀 정착`
- 신(R3-3): `④ 배포·검증 자동화 및 개발 표준화`
- 사유: JD 신호(CI/CD·AI E2E·자동화) 전면화. "팀 정착" 서사는 근거 줄에 유지.

**칩 수정** (A-7 → R3-3 갱신):
- 구: `개발 표준 단독 설계 · 공통 컴포넌트 표준화 · 기술 지식 이식`
- 중간(A-7): `개발 표준 단독 수립 · Playwright E2E 하네스 구축 · 세미나·문서로 팀 전파`
- 신(R3-3): `CI/CD 파이프라인 구축 · AI 기반 E2E 게이트 운영 · FE AX 개발 표준 수립`
- 사유: JD 우대 키워드 CI/CD·AI 서비스 개발 관심 신호를 칩 최상단으로. 근거: EXP-02·EXP-03 Jenkins CI/CD·Playwright E2E 게이트 bank 확인.

**근거 줄 수정** (R3-3):
- 구: `Vitest 약 2,600케이스·Playwright E2E 하네스 단독 구축, **팀 10명 전원의 개발 절차로 정착**, **세미나 12회·기술 문서 48건**`
- 신: `**배포 리드타임 10분 → 2분(약 80%) 단축** · **AI 기반 Playwright E2E를 배포 파이프라인 필수 게이트로 편입**, 팀 10명 전원의 개발 절차로 정착 · 세미나 12회·기술 문서 48건`
- 사유: CI/CD 정량 성과(배포 리드타임)·AI E2E 게이트 편입을 앞으로, 팀 정착·문서 수를 뒤로. 수치는 기존 확인값 그대로 재배치. 날조 없음.
  - "배포 리드타임 10분 → 2분" 근거: experience-bank.md EXP-02 Metrics "[배포 자동화] Jenkins CI/CD 배포 리드타임 10분→2분" — bank 확인값.
  - "AI 기반 Playwright E2E 게이트" 근거: EXP-03 Actions "Playwright E2E를 배포 파이프라인의 필수 게이트로 편입" — bank 확인값.

### 경력 내담 라인 수치 — 원복 (A-2)

- 구(초안 오류): `대시보드 렌더링 2.5초 → 1초대`
- 신(base 원복): `대시보드 렌더링 2.5초 → 1초`
- 사유: base 소유자 2026-07-27 확정값 "2.5초 → 1초"가 정본. "1초대"는 경력기술서 성과 불릿 표현으로 경력 라인과 구분.

### 경력기술서 EXP-02 기술 라인 스택 순서 (reviewer M-1)

- 원문(base): `React · TypeScript · Java · Spring Boot · REST API · MySQL · Node.js · Express · jQuery · Thymeleaf · Playwright · Jenkins · Docker · WebView`
- 수정: `Java · Spring Boot · MySQL · REST API · React · TypeScript · Node.js · Express · jQuery · Thymeleaf · Playwright · Jenkins · Docker · WebView`
- 사유: 예외 ① 라인 단위 적용.

### 경력기술서 — 항목 배치 순서 변경

- base: 1.AI챗봇 / 2.임직원플랫폼 / 3.AX전환 / 4.삼성물산 / 5.미스미
- smilegate: 1.임직원플랫폼(EXP-02) / 2.AI챗봇(EXP-01) / 3.AX전환(EXP-03) / 4.삼성물산(EXP-04) / 5.미스미(EXP-05)
- 사유: 승인된 브리프 강조 경험 순서 EXP-02 → EXP-01 → EXP-03 → EXP-04 → EXP-05.

### 기술 표 — 행 순서 변경 (예외 ① + A-9)

- smilegate 순서: 백엔드(1위) → AI 활용 개발(2위) → 프론트엔드(3위) → 데이터베이스 → 이하 base 동일
- base: AI 활용 개발 최상단
- 백엔드 행: `Java · Spring Boot · Spring Framework · Node.js · Express · Nest.js · Python · FastAPI · REST API`
  - Spring Framework 신규 추가 (base 대비 변경 — JD "Spring Framework" 명시 요건 대응)
- 사유: 예외 ① "백엔드 행 최상단". A-9 "AI 활용 개발 2위(과회전 방지)".

### 교육·자격증 섹션 — 전진 배치 (예외 ③)

- base: 뒷단 (학력→해외경험→교육→자격증→어학)
- smilegate: 요약 직후·핵심 성과 이전 (교육→자격증 순)
- 사유: 예외 ③ 비전공 보완 신호 강화. A-1 제1원칙 보완: 요약 4문은 "기반"으로만 → 섹션 자체로 상세 노출, 중복 해소.

### 경력기술서 EXP-02 — 권한·정책 공통 기준 정의 불릿 추가 (G-4)

- 신규 추가 위치: EXP-02 주요 실행 섹션 (BFF 계층 다음, AI 기반 회귀 검증 전)
- 추가 내용: `Web·Admin·App의 사용자 권한, 메뉴, 데이터 출력 정책이 제각각이던 것을 공통 기준으로 정리해 멀티 채널 정책 일원화`
- 근거: experience-bank.md EXP-02 Actions "사용자 권한, 메뉴, 브랜딩, 데이터 출력 정책을 공통 기준으로 정리" — bank 확인값. 날조 없음.

### 경력기술서 EXP-02 — 풀스택 E2E 개발 불릿 MySQL DB 스키마 태깅 (R3-4)

- 원문: `신규 건강관리 기능의 **MySQL 데이터 모델, Spring Boot 서버 로직, REST API, Web/Admin 화면까지 전 구간 직접 개발**`
- 수정: `신규 건강관리 기능의 **MySQL DB 스키마·데이터 모델 설계, Spring Boot 서버 로직, REST API, Web/Admin 화면까지 전 구간 직접 개발**`
- 사유: JD 우대 "DB 스키마 설계 경험" 정면 대응. experience-bank.md EXP-02 Actions "기존 소스와 DB 스키마 분석"·"건강관리 신규 기능에 필요한 MySQL 데이터 모델 … 개발" — 분석·설계 모두 bank 확인값. 날조 없음.

### 경력기술서 EXP-04 — 백엔드 응답 경량화 표현 구체화 (G-3 + R3-5)

- G-3 수정: `**Spring REST API의 필터링·정렬 로직 설계**, **DB 인덱싱과 DTO 기반 필요 필드만 투영**으로 응답 경량화 직접 수행`
- R3-5 추가 수정: `**MyBatis 기반 Spring REST API의 필터링·정렬 로직 설계**, **DB 인덱싱과 DTO 기반 필요 필드만 투영**으로 응답 경량화 직접 수행`
- 사유: experience-bank.md EXP-04 Technologies "MyBatis" 명시 + 기술줄 `Java · Spring · REST API · MyBatis · Oracle` 확인. MyBatis = ORM/쿼리 매핑 방식으로 Spring REST API 구현 방식 귀속. 날조 없음 — bank 기술 목록 확인값.
- G-3 나머지: 서버측 설계 판단 근거(island-loader·모놀리식 분석·클라/서버 경계 정의) 전량 이미 반영 완료. 추가 bank 근거 없음.

### 병역 — 미기재 유지

- 승인된 브리프 "병역 1페이지 미기재" 확정.

---

## 레인 재판정

- **신규 작문 비중**: 약 22~26% (R3 반영 후)
  - 신규 산문: 요약 1·3·4·5문(신규/수정), 경력 BE 스택 라인 단어 추가
  - 비산문: 핵심 성과 ④ 타이틀·칩·근거 줄 전면 재조립(R3-3), 경력기술서 목차 순서, 기술 표 행 순서·Spring Framework 추가, 교육·자격 전진 배치, 경력 내담 수치 원복, EXP-02 DB 스키마 태깅(R3-4)·권한 정책 불릿 추가(G-4), EXP-04 MyBatis 귀속·DTO 투영 표현(R3-5/G-3)
  - 경력기술서 내부: EXP-02 실행 불릿 2건·EXP-04 실행 불릿 1건 수정 외 전량 base 확정 문면 verbatim
- **판정**: fast lane 가능

---

## 갭 인터뷰 사후 처리 확인

| 갭 항목 | 처리 |
| --- | --- |
| UML | 미기재 (소유자 결정) |
| K8S | 미기재 (CI/CD 실무로만 대응) |
| 내담 초기 20개월 Java 실무 | 미기재. 요약 4문은 삼성물산 2024·대웅 2025 귀속으로만 서술 (A-1) |
| 컴공 비전공 | 정보처리기사·응용SW엔지니어링(Java 기반 웹 개발)을 요약 "기반" + 전진 배치 섹션으로 보완 |

---

## 소유자 선택 대기 — 헤드라인 대안

오케스트레이터 검수(2026-08-04)에서 헤드라인 교체는 승인 범위 밖으로 판정되어 초안 본문은 base 원문으로 원복. 아래 대안은 스톱 ②에서 소유자 선택용으로 보존 — 초안 본문에는 미반영.

**대안 A** (Java + AI 웹서비스 조합):
`Java·Spring Boot·React로 AI 웹서비스를 End-to-End 설계·개발하는 Fullstack Engineer`
