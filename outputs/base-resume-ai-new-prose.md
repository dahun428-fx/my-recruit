# base-resume-ai.md — 신규·변경 문장 리뷰 범위 (companion)

대상: `docs/resume-reference/base-resume-ai.md` (2026-11-12 신설)
비교 기준: `docs/resume-reference/base-resume.md`. 이 목록에 없는 본문 문장은
`base-resume.md`에서 **무수정** 승계했거나 `canonical-lines.md` `approved` 문장을
**무수정** 재사용한 것이다(아래 「fast lane」 참조). 상단 메타 4섹션(문서
아키텍처·편집 규칙·상태·메모)은 복제 시 제거하는 운영 메타라 산문 리뷰 대상에서
뺐다 — 단, 메타의 「쓰지 않은 것」 표는 사실 판단이 담겨 있으므로 reviewer가
함께 대조하길 권한다.

## Fast lane (리뷰 면제 후보 — 무수정 재사용)

- `canonical-lines.md` approved(EXP-01, roles에 ai-product 포함):
  - "AI 개발자와 API 응답 형식, 스트리밍 방식, 오류 정책을 조율" — 경력기술서 2 「서비스 간 연동 규약」
  - "400건 발화 검증 기준 답변 화면 정상 출력률 100% 달성" — 경력기술서 2 「응답 출력 검증」
- `base-resume.md` 무수정 승계: 경력기술서 3·4·5 문제 단락; 3 「하네스 엔지니어링 구축」「FE AX 개발 표준 단독 설계」「학습의 조직 이식」「일하는 방식의 전환」; 4 「서비스·데이터 구조 분석」「배포 자동화」「검증·배포 자동화」; 5 「구간 분리 측정 진단」「클라/서버 경계 설계」「백엔드 응답 경량화」「대시보드 성능 개선」「모바일 검색 개선」; 6 「한국 웹 전환 리드」「렌더링 경계 판단」「전면 전환 완수」「성능 개선」; 2 「실사용 서비스 전환」; 경력 섹션 다나아 첫 줄·대웅 스쿼드 줄·내담 팀 규모 줄·한국미스미 줄; 학력·교육 전부, 자격 정보처리기사 줄, 어학 TOEIC 줄.
  - 주의: `base-resume.md` 자체는 `canonical-lines.md`에 approved로 적재되지 않은 문장이 많다. 소유자 확정 문면이지만 은행 approved 기준으로 엄격히 보면 리뷰 대상이 된다 — orchestrator 판단 사항.

## (a) 신규·변경 산문

| # | 위치 | 문장 (요지 또는 원문) | 근거 |
| --- | --- | --- | --- |
| a1 | 헤드라인 | 멀티 에이전트·RAG 서비스의 API·연동·검증을 구현하는 AI Product Engineer | EXP-01 [갱신 2026-11-12]·[FastAPI 담당 범위 확정], EXP-03 하네스 |
| a2 | 요약 1문 | 6년 경력의 AI 서비스 개발자입니다. | profile.md Career Facts (2020.10~ 연속 재직) |
| a3 | 요약 2문 | 팀 단위로 개발한 멀티 에이전트·RAG 서비스에서 서브에이전트 오케스트레이션·하이브리드 검색·LangChain 파이프라인·프롬프트와 컨텍스트 구성·가드레일·평가 하네스의 설계·구현에 참여하며 직접 코드를 작성했고, FastAPI 서빙 API와 SSE 스트리밍 규격을 설계해 화면·백엔드와 연결했습니다. | EXP-01 [갱신 2026-11-12 — 이전 기록 대체], [FastAPI 엔드포인트 설계 판단 3종]; v2 MAS Notes [갱신 2026-11-12] 허용 문구 |
| a4 | 요약 3문 | 프론트엔드로 시작해 Node.js·Spring Boot 백엔드와 Docker·Jenkins 배포까지 영역을 넓혔고, 현재는 LLM 응답은 평가 세트와 회귀 검수로, 코드는 E2E 배포 게이트로 검증하는 체계를 만들며 팀의 AX 전환을 리드하고 있습니다. | EXP-07 BFF, EXP-02 배포, v2 MAS 평가 하네스, EXP-03 [LLM 채팅 응답 검수 도구]·[배포 파이프라인 필수 게이트]·[역할 지속 여부] |
| a5 | 핵심 성과 ① 타이틀·칩 | 멀티 에이전트·RAG 서비스 구현 / 오케스트레이터·서브에이전트 · 한국어 하이브리드 RAG · LangChain 파이프라인 · 프롬프트·컨텍스트 구성 | EXP-01 [갱신 2026-11-12], v2 MAS Actions(오케스트레이터 7단계·하이브리드 RAG) |
| a6 | 핵심 성과 ① 근거 | 팀이 구축한 서브에이전트 18개·8카테고리 멀티 에이전트 서버에서 오케스트레이션·검색·컨텍스트 코드 직접 작성, 운영 경로 그대로 비교하는 LLM-judge A/B 평가 240건 하네스 작성 참여 | v2 MAS Actions(서브에이전트 18개·8카테고리, eval/ 240건) — "팀이 구축한 시스템 규모" 인용 허용; registry 미등재 |
| a7 | 핵심 성과 ② 타이틀·칩 | AI 서빙 API·실서비스 전환 / FastAPI 엔드포인트 설계 · SSE 이벤트 규격 · LLM 오류·타임아웃 처리 · 서비스 단위 독립 배포 | EXP-01 [FastAPI 담당 범위 확정]·[설계 판단 3종]·[배포 아키텍처] |
| a8 | 핵심 성과 ② 근거 | 임직원 3,493명 실사용 서비스로 계획 대비 2주 조기 전환, 400건 발화 검증 기준 답변 화면 정상 출력률 100% | `metric-ai-poc-users`(confirmed), `metric-ai-render-success`(confirmed); 2주 조기는 EXP-01 Metrics(user-attested 2026-07-27, registry 미등재) |
| a9 | 핵심 성과 ③ 타이틀·칩 | AI 개발 하네스·사내 MCP 연동 / 사내 MCP 서버 2종 · FE AX 개발 표준 · E2E 배포 게이트 · LLM 응답 회귀 검수 | EXP-03 [MCP 서버 용도 확정]·FE AX SOP·[필수 게이트]·[LLM 채팅 응답 검수 도구] |
| a10 | 핵심 성과 ③ 근거 | 개발 표준·검증 하네스가 팀 10명 전원의 개발 절차로 정착, AI 기반 명세 분석으로 RESTful API 29건 예상 기간 4주 → 1주 | EXP-03 Role(10명 전원 채택), `metric-restful-api-29`(source_stated, 문면 "예상 기간 4주 → 1주" — EXP-03 [서버 구현 스택 확정]) |
| a11 | 핵심 성과 ④ 타이틀·칩 | 백엔드·연동·배포 / Node.js BFF · Spring Boot·MyBatis REST API · Jenkins·Docker 무중단 배포 · 건설 현장 앱 API 연동 | EXP-07, EXP-02 [매핑 레이어]·[배포 자동화], EXP-04 [도메인 확정] |
| a12 | 핵심 성과 ④ 근거 | 화면 렌더링 분리와 Oracle 인덱싱·DTO 투영을 함께 적용해 대시보드 렌더링 2.5초 → 1초대, 신규 건강기록 기능 3건을 데이터 모델부터 API까지 End-to-End 개발 | `metric-samsung-dashboard-render`(source_stated), `metric-b2b-new-features`(confirmed), EXP-02 [기능 성격 확정] |
| a13 | 경력 다나아 직무 라인 | AI 서비스 개발 / AI코치 차기 버전 멀티 에이전트 서버 전환 참여 / 팀 AX 전환 리드 | v2 MAS Period(2026.04~ 이관 후 지속), EXP-03 [역할 지속 여부] |
| a14 | 경력 다나아 불릿 2 | AI코치 차기 버전 서브에이전트 18개 멀티 에이전트 서버 전환 — 오케스트레이터·RAG·컨텍스트 구성·평가 하네스 코드 작성 참여 (Python·FastAPI·LangChain·FAISS·Qdrant) | v2 MAS Role [갱신 2026-11-12], Technologies |
| a15 | 경력 다나아 불릿 3 | AI 기반 명세 분석·구현·테스트로 AI코치 RESTful API 29건 교체 (Node.js·Express) | EXP-03 [RESTful API 교체 29건]·[서버 구현 스택 확정] (2026-07, 이관 후 기간) |
| a16 | 경력 다나아 불릿 4 | 비즈36.5 2단계 건강관리실·검진센터 업무 DX 기능화 기획 — 현업 요구사항 분석·기능 설계, 기획 확정 | 「비즈36.5 2단계 건강관리실·검진센터 AX 기획」 [내재화 vs 기능화 가드레일], 2026-11-12 상태 "기획 확정, 개발 전" |
| a17 | 경력 대웅 직무 라인 | AI 서비스·풀스택 개발 / AI코치 LLM·에이전트 서버 API 개발 / 팀 AX 전환 리드 | EXP-01 [FastAPI 담당 범위 확정], EXP-03 |
| a18 | 경력 대웅 불릿 | AI코치 LLM 릴레이·에이전트 서버 API 직접 설계·구현 — SSE 이벤트 규격·LLM 오류·타임아웃 처리·요청/응답 스키마 (Python·FastAPI·SSE) | EXP-01 [FastAPI 담당 범위 확정]·[설계 판단 3종] |
| a19 | 경력 대웅 불릿 | AI코치 RAG·Vector DB·LangChain 파이프라인과 에이전트별 프롬프트·컨텍스트 구성 코드 작성 (LangChain·Qdrant·FAISS·BM25) | EXP-01 [갱신 2026-11-12], EXP-07 [VectorDB·RAG 구현 참여 — 갱신 2026-11-12] |
| a20 | 경력 대웅 불릿 | 사내 MCP 서버 2종 개발·Claude Code·Codex 연동, 개발 표준·E2E 배포 게이트로 팀 AX 전환 리드 (MCP·Playwright) | EXP-03 [MCP 서버 개발·연동]·[용도 확정]·[필수 게이트] |
| a21 | 경력 대웅 불릿 | 비즈36.5 Node.js BFF 신규 구축·Spring Boot REST API, 운영 서버 Blue-Green 무중단 배포 (Node.js·Spring Boot·MySQL·Jenkins·Docker) | EXP-07, EXP-02 [배포 자동화] |
| a22 | 경력 대웅 불릿 | AWS EC2·S3로 구성된 환경 위에서 배포·운영, Linux 서버 SSH 운영 (Docker·Nginx) | EXP-06 [AWS 스코프 정밀화], EXP-03 [Linux 서버 SSH 운영] — 프로젝트 귀속 미확인이라 경력(재직 전반) 계층에만 배치 |
| a23 | 경력 내담 불릿 | 삼성물산 건설부문 현장 앱·데이터 플랫폼 API·연동 — Spring REST API 필터링·정렬·역할별 조회, Oracle 인덱싱·DTO 투영 (Spring·MyBatis·Oracle·React Native) | EXP-04 [도메인 확정], Actions [BE] |
| a24 | 경력 내담 불릿 (변경) | 대용량 데이터 처리 및 처리 소요 시간 단축 (대시보드 렌더링 2.5초 → **1초대** · 수만 건 검색 응답 5초 → 1초) — base "1초"를 registry 값으로 | `metric-samsung-dashboard-render`, `metric-samsung-rn-search` |
| a25 | 경력기술서 목차 | 7개 항목 목차 | — |
| a26 | 1 헤더 | 대웅제약 → 다나아데이터 \| AI코치 멀티 에이전트·RAG 파이프라인 개발 / 기간 2025.07 ~ 재직중 · 차기 버전 전환 2026.04 ~ · 2026.06 조직 이관 후 지속 | EXP-01 Period, v2 MAS Period(해소(부분) 2026-11-12) |
| a27 | 1 [주요 업무] | 팀 단위로 개발한 AI 건강검진 챗봇 AI코치에서 서브에이전트 구성·오케스트레이션, RAG·Vector DB, LangChain 파이프라인, 에이전트 아키텍처의 설계·구현에 참여하며 직접 코드 작성 — 에이전트별 프롬프트·컨텍스트 구성, 가드레일·후처리, 평가 하네스 담당 | EXP-01 [갱신 2026-11-12] 4개 영역 + 프롬프트/컨텍스트/가드레일/평가 |
| a28 | 1 문제 단락 (3문) | 의도 분류 기반 → 멀티 에이전트 전환 / 복합 질의 분할·병렬·합성, 개인정보·의학 단정 표현 차단 / 구조 변경 효과의 비교 기준 필요 | v2 MAS Context(v1 의도 분류 → v2), Actions(multi-intent 라우팅·Synthesizer·PII·출력 필터·single vs multi A/B). **문제 동기는 시스템 구성에서 역산한 서술 — 소유자 확인 권장** |
| a29 | 1 에이전트 구성·오케스트레이션 | 사전 필터 → 의도 분류·RAG 검색 병렬 → 컨텍스트 구성 → 라우팅 → 병렬 실행 → 응답 합성 오케스트레이터에서 에이전트 정의·라우팅·병렬 실행·응답 합성 코드 작성, 라우터 판단이 불확실하면 정적 라우트로 되돌아가는 폴백 구조 | v2 MAS Actions(오케스트레이터 7단계, 라우팅 4경로 중 "LLM 동적 라우터 confidence + 정적 폴백"), EXP-01 [갱신] ① |
| a30 | 1 RAG 파이프라인 | 임베딩·인덱싱·검색·재랭킹 코드 작성 — FAISS 벡터 검색과 형태소 분석 기반 BM25를 함께 쓰는 한국어 하이브리드 검색, Jaccard 재랭킹, Qdrant 벡터 저장소 | EXP-01 [갱신] ②, v2 MAS Actions(한국어 하이브리드 RAG) |
| a31 | 1 LangChain 파이프라인 | LangChain 기반 체인·도구 연결 코드 작성 | EXP-01 [갱신] ③ (은행에 메커니즘 세부 없음 — 서술 범위 최소화) |
| a32 | 1 프롬프트·컨텍스트 | 설계 논의·리뷰에서 에이전트 프롬프트·컨텍스트 구성 방식을 제안해 반영, 에이전트별 프롬프트 작성·개선과 대화 이력·사용자 검진 데이터·검색 결과를 모델 입력으로 조립하는 컨텍스트 구성 코드 작성 | EXP-01 [→ 해소(부분): 설계 기여], [갱신 2026-11-12] |
| a33 | 1 가드레일·후처리 | LLM 입력 전 개인정보를 가리고 스트리밍 응답에서 복원하는 PII 마스킹, 의학적 단정 표현을 완화하는 출력 필터, 표·마크다운 깨짐과 링크·버튼 변환을 바로잡는 응답 후처리 코드 작성 | EXP-01 [갱신] 가드레일·후처리, v2 MAS Actions(PII 마스킹/스트리밍 unmask, 출력 필터 의학 단정 완화), EXP-07 [응답 후처리 구체화] |
| a34 | 1 평가 하네스 | 운영 경로 그대로 single·multi-agent를 비교하는 블라인드 LLM-judge 평가 코드와 데이터셋 작성 참여 — 5축 루브릭과 FAIL 게이트로 구조 변경의 효과를 판정하는 기준 | EXP-01 [갱신] 평가 하네스, v2 MAS Actions(eval/) |
| a35 | 1 성과 ×3 | 멀티 에이전트 구조 전환(18개·8카테고리 서버 전환에 직접 참여) / 검증 가능한 품질 기준(복합 질의 120건 × 2 arm, A/B 평가 240건 평가 세트·FAIL 게이트) / 응답 안전 장치(마스킹·완화 필터·후처리로 출력 기준 확보) | v2 MAS Actions·Metrics(시스템 규모 documentary), C-11 완성 문법. 운영 성과 수치 없음 — 은행 Result [확인 필요] |
| a36 | 2 헤더·[주요 업무] | 대웅제약 \| AI코치 서빙 API·SSE 규격과 실서비스 전환 / 개발자 5명 팀으로 10주 내 실서비스 전환 — FastAPI 엔드포인트·SSE 규격 직접 설계·구현, 프론트엔드 단독 담당으로 응답 화면 연결 | EXP-01 [프로젝트 팀 규모], 프로젝트 목표(10주), Role(프론트엔드 유일 담당자), [FastAPI 담당 범위 확정] |
| a37 | 2 문제 단락 (2문) | PoC 일괄 응답 대기·토큰/오류/종료 혼재로 중단·완료 미구분 / 서비스 단위 독립 배포라 응답 형식·오류 규약부터 정해야 함 | EXP-01 [이벤트 형식 정의의 계기](a)(b), [배포 아키텍처] |
| a38 | 2 서빙 API 설계·구현 | LLM 릴레이·에이전트 서버의 FastAPI 라우트·엔드포인트 직접 설계·구현, 대화 이력·컨텍스트를 담는 요청·응답 스키마 설계 | EXP-01 [FastAPI 담당 범위 확정], [설계 판단 3종] ③ |
| a39 | 2 SSE 이벤트 규격 정의 | 일괄 응답 대기와 신호 혼재를 함께 풀기 위해 토큰·진행·오류·종료를 이벤트 단위로 나눠 화면이 중단과 완료를 구분하도록 규격을 정하고 프론트엔드 상태와 맞춤 | [설계 판단 3종] ①, [이벤트 형식 정의의 계기] — 이벤트 수·10초→4초 연결 안 함 |
| a40 | 2 LLM 오류·타임아웃 처리 | LLM 호출 실패·지연 시 재시도·타임아웃·부분 실패 각각의 응답 방식 결정 | [설계 판단 3종] ② — 초·횟수 미기재 |
| a41 | 2 독립 배포 구조 운영 | 프론트엔드·Python LLM 서버·백엔드·MongoDB·Qdrant가 서비스 단위로 분리 배포되는 구조에서 Docker·Docker Compose 컨테이너를 직접 빌드·배포·재기동 | EXP-01 [배포 아키텍처] 서술 허용 범위, [오케스트레이션·배포 실행 주체 확정] — MSA 표현 없음 |
| a42 | 2 응답 화면 연결 | SSE 이벤트를 중지·재시도·재생성 흐름과 Markdown·표·링크 렌더링 컴포넌트에 연결 | EXP-01 Actions(SSE 대화 흐름·Markdown 렌더링 계층) — FE 항목 1줄 축약(C-12) |
| a43 | 2 SaaS 제품화 | 고객사별 테마·기능 노출을 설정으로 제어하는 Config-Driven 구조로 신규 고객사 FE 커스터마이징 2주 납품 — 최초 구현 10주 대비 | `metric-ai-build-period`(source_stated, FE 기준 스코프), EXP-01 Base-Theme·Config-Driven UI |
| a44 | 3 헤더·기간·[주요 업무] | 대웅제약 → 다나아데이터 \| AI 개발 하네스·사내 MCP 연동 — 팀 AX 전환 리드 / 2026.01 ~ 재직중 · 이관 후 역할 지속 / 팀의 AI 활용 개발 방식 전반을 설계·리드 — 사내 MCP 서버 개발·연동, AI 생성 코드와 LLM 응답 검증을 위한 하네스 엔지니어링 구축, FE AX 개발 표준 단독 설계, 팀 지식 자산화 주도 | EXP-03 Period·[역할 지속 여부]·[MCP 서버 개발·연동] (base [주요 업무] 변경) |
| a45 | 3 사내 MCP 서버 개발·연동 | 사내 문서·지식 검색용과 테스트·검증 도구 호출용 MCP 서버 2종을 직접 개발·수정해 Claude Code·Codex에 연동, AI 에이전트가 사내 문서와 검증 도구를 호출하도록 구성 | EXP-03 [MCP 서버 개발·연동](a)(b), [용도 확정] — 연결 방식 세부 미기재 |
| a46 | 3 LLM 응답 회귀 검수 | 엑셀 질문 목록을 챗봇 화면에 자동 입력해 마크다운·표·버튼이 포함된 LLM 응답을 Playwright로 수집하고 스크린샷·JSON·HTML 갤러리로 저장하는 회귀 검수 도구 제작 | EXP-03 [LLM 채팅 응답 검수 도구 — 본인 구축]·[documentary 확인] (samsung-cnt 초안 문장 변형) |
| a47 | 3 AI 오류 분석 리포트 | PostHog 오류 스택과 GitLab 소스를 GPT-4o에 넘겨 심각도·원인·수정 diff를 JSON으로 받는 오류 분석 리포트 생성 스크립트를 TypeScript로 구축, CI 잡 정의 — 러너 제약으로 수동 실행 | EXP-03 [AI 기반 에러 리포트 파이프라인] 가드("운영 중" 금지) |
| a48 | 3 AI 기반 API 교체 | AI 기반 명세 분석·구현·테스트 방식으로 AI코치 RESTful API 교체 29건의 Node.js·Express 서버 구현과 프론트 연동 수행 | EXP-03 [RESTful API 교체 29건]·[작업 범위 확정]·[서버 구현 스택 확정] |
| a49 | 3 성과 API 개발 기간 단축 | AI코치 RESTful API 29건 예상 기간 4주 → 1주(약 75%) | `metric-restful-api-29` |
| a50 | 3 성과 하네스 전제 개발 | 비즈36.5 Web 전환을 분석·개발·테스트·E2E 자동화 하네스 전제로 설계해 비슷한 규모 작업의 기존 소요 기간 6주 → 2주(약 67%) | `metric-react-harness-6w-2w`, EXP-03 [6주의 기준] |
| a51 | 3 성과 검증 인력 효율 | E2E 검증 자동화로 반복 QA 3시간 → 30분, 검증 인력을 개발에 재투입 | `metric-qa-time`(confirmed, 문서 근거 미확보), EXP-03 Result (a) — base 1번 성과에서 3번으로 이동·문장 변경 |
| a52 | 4 헤더·[주요 업무] | 임직원 건강검진 통합플랫폼 백엔드·BFF·배포 구조 개편 / 레거시 현대화의 백엔드·연동·배포 구간 담당 — 구조 분석, Node.js BFF, MySQL·Spring Boot REST API, Jenkins·Docker 배포 | EXP-02 Role, EXP-07 |
| a53 | 4 BFF 계층 신규 구축 (변경) | React 전용 데이터 집계·중계 API를 Node.js·Express로 신규 구축하며 구조 설계와 주요 엔드포인트 구현 담당, 비즈니스 로직·데이터 소유는 Spring Boot에 두고 조회 조합·가공·권한 확인만 BFF에서 처리 | EXP-07 [BFF 담당 범위 정밀화]·[BFF 책임 경계] |
| a54 | 4 데이터 모델·REST API | 신규 건강기록 기능 3건을 레거시 스키마를 바꾸지 않고 PK·FK 제약을 선언한 신규 테이블로 연결, 사용자 ID+기록일 복합 인덱스를 실행 계획으로 확인하고 Spring Boot·MyBatis REST API 개발 | EXP-02 [테이블 설계 방식]·[FK 제약 DB 선언 확인]·[인덱스 컬럼]·[실행 계획 확인]·[매핑 레이어] |
| a55 | 4 백엔드 테스트·권한 검증 | JUnit으로 서비스·MyBatis 매퍼 단위·통합 테스트 작성, 화면 라우트 가드와 서버 서비스 로직 내 역할 검사의 이중 검증 적용 | EXP-02 [백엔드 테스트]·[서버 검증 방식 확정] |
| a56 | 4 성과 데이터-투-API 오너십 (변경) | 신규 건강기록 기능 3건을 MySQL 모델부터 서버·API·화면까지 End-to-End 개발 | `metric-b2b-new-features`(confirmed) |
| a57 | 4 성과 내부 개발·운영 전환 (변경) | 화면 단위 점진 전환으로 108개 페이지·82개 화면을 9주 내 단독 전환, 외주 없이는 못 고치던 서비스를 내부 개발·운영 구조로 전환 | `metric-b2b-pages-screens`(source_stated) — FE 항목 1줄 축약(C-12) |
| a58 | 5 헤더·[주요 업무] | 삼성물산 건설부문 \| 건설 현장 앱·데이터 플랫폼 API·연동 고도화 / 장비·인력 데이터를 다루는 React Native 현장 앱·Vue 3 데이터 플랫폼에서 Spring REST API·역할별 조회·DB 응답 경량화와 앱 출시·운영 — 병목 진단부터 API·DB·화면까지 | EXP-04 [도메인 확정](서술 허용 "건설 현장 업무 시스템"), Role |
| a59 | 5 현장 앱 출시·운영 | React Native 현장 앱을 App Store·Google Play에 출시·운영하고 카메라·파일·푸시 토큰·인증 토큰을 주고받는 네이티브 모듈 브릿지 직접 설계·구현 | EXP-04 [RN 앱 스토어 출시·운영]·[네이티브 모듈 브릿지] — 특정 API명 미기재 |
| a60 | 6 [주요 업무]·문제 (축약 변경) | 6인 팀의 한국 웹 마이그레이션 리드 — 일본 본사와 일본어 직접 협업, PHP·jQuery → Next.js·TypeScript / 문제 단락 2문으로 축약 | EXP-05, positioning EXP-05(원설계 일본 본사 — "아키텍처 설계" 표현 없음) |
| a61 | 7 전체 (신설) | 업무 외 개인 프로토타입 3건: [주요 업무] 1문 + 실행 3불릿(RAG 프로토타입·MCP 에이전트 프로토타입·LLM 챗봇 보일러플레이트) | 「AI 소프트웨어 사이드 프로젝트 (개인)」 documentary 3건 + [이력서 기재 승인 2026-11-12](업무 외 명시 조건). 실행 3문 중 앞 2문은 `outputs/samsung-cnt-agentic-ai-resume-draft.md` 문장 무수정 재사용(비은행 초안), 3번째는 같은 문장의 괄호를 풀어 어순만 변경(S-02) |
| a62 | 해외경험 (변경) | …비즈니스 일본어로 수행 — JLPT **N1** 실전 활용 | profile.md JLPT 행 정정(2026-09-13) |

## (b) candidate 상태 bank 문장 재사용

- 없음.

## (c) 신규·변경 비산문 항목

| # | 위치 | 항목 | 근거 |
| --- | --- | --- | --- |
| c1 | 인적사항 | 포지션: AI 서비스 개발 · Product Engineer | 신규 |
| c2 | 인적사항 | 경력: 총 6년 1개월 (base "5년 9개월" → 2026-11 재계산) | profile.md Career Facts, samsung-cnt 초안과 동일 계산 |
| c3 | 경력기술서 기간 줄 | 1: 2025.07 ~ 재직중 · 2026.04 ~ · 이관 후 지속 / 3: 2026.01 ~ 재직중 · 이관 후 역할 지속 / 7: 2025.07 ~ 2026.01 · 저장소 작성 시점 기준 | v2 MAS Period, EXP-03 Period·[역할 지속 여부], 사이드 프로젝트 documentary 날짜 |
| c4 | 경력기술서 기술 줄 | 1: Python · FastAPI · asyncio · LangChain · FAISS · BM25 · Qdrant · MongoDB · Anthropic Claude · OpenAI GPT · LLM-judge · Docker Compose | v2 MAS Technologies, EXP-01 [갱신] |
| c5 | 경력기술서 기술 줄 | 2: Python · FastAPI · SSE · MongoDB · Qdrant · Docker · Docker Compose · Nginx · React · TypeScript | EXP-01 Technologies·[배포 아키텍처] |
| c6 | 경력기술서 기술 줄 | 3: Claude Code · Codex · GitHub Copilot · MCP · Harness Engineering · Playwright · OpenAI API · PostHog · GitLab CI/CD · Jenkins · Node.js · Express · TypeScript | EXP-03 Technologies, [AI 기반 에러 리포트](OpenAI GPT-4o) |
| c7 | 경력기술서 기술 줄 | 4: Java · Spring Boot · MyBatis · MySQL · JUnit · REST API · Node.js · Express · Jenkins · Docker · React | EXP-02, EXP-07 |
| c8 | 경력기술서 기술 줄 | 5: Java · Spring · REST API · MyBatis · Oracle · React Native · Vue 3 · Firebase FCM | EXP-04 Technologies |
| c9 | 경력기술서 기술 줄 | 6: Next.js · React · TypeScript · PHP · jQuery · i18next · Vercel · Datadog (base 대비 축약) | EXP-05 |
| c10 | 경력기술서 기술 줄 | 7: Python · FastMCP · LangChain · LangGraph · Qdrant · Gemini · React · TypeScript | 사이드 프로젝트 documentary 실측 스택 |
| c11 | 경력기술서 라벨 | 신규 라벨: 에이전트 구성·오케스트레이션 / RAG 파이프라인 / LangChain 파이프라인 / 프롬프트·컨텍스트 엔지니어링 / 가드레일·후처리 / 평가 하네스 / 멀티 에이전트 구조 전환 / 검증 가능한 품질 기준 / 응답 안전 장치 / 서빙 API 설계·구현 / SSE 이벤트 규격 정의 / LLM 오류·타임아웃 처리 / 서비스 간 연동 규약 / 독립 배포 구조 운영 / 응답 화면 연결 / 응답 출력 검증 / SaaS 제품화 / 사내 MCP 서버 개발·연동 / LLM 응답 회귀 검수 / AI 오류 분석 리포트 / AI 기반 API 교체 / API 개발 기간 단축 / 하네스 전제 개발 / 검증 인력 효율 / 데이터 모델·REST API / 백엔드 테스트·권한 검증 / 데이터-투-API 오너십 / 내부 개발·운영 전환 / 현장 앱 출시·운영 / RAG 프로토타입 · 2025.07 / MCP 에이전트 프로토타입 · 2025.10 / LLM 챗봇 보일러플레이트 · 2026.01 | — |
| c12 | 기술 표 | 카테고리 재편: AI·LLM 서비스(신규) · LLM API(신규) · AI 개발 도구(신규, base "AI 활용 개발" 대체) · 백엔드 · 데이터베이스 · 품질·검증 · 배포·인프라 · 프론트엔드(후순위) · 분석·관측 · 협업. 신규 토큰: 멀티 에이전트 오케스트레이션·Qdrant·FAISS·BM25·LLM-judge 평가·Anthropic Claude·OpenAI GPT·GitHub Copilot·MCP·MyBatis·JUnit·Docker Compose·Linux. 제거 토큰: 상태관리·UI·시각화 행 전체, Storybook·Chromatic·Vercel·Lighthouse·Adobe Analytics·Nest.js | EXP-01 [갱신], v2 MAS, EXP-03, EXP-02, profile Skills |
| c13 | 자격증 | KT AICE Associate · KT · 합격(100/100) · 2026.08 (신규) | profile.md 자격 표(표기 승인 2026-11-12, 지원서별 판단) |
| c14 | 어학 | 일본어 JLPT N1 · 2018.08 (base "1급" 정정) | profile.md |
| c15 | 경력 직무 라인 | 다나아·대웅 직무 라인 교체(a13·a17) | — |

## JD 갭 (base라 대상 JD 없음 — AI 직무 공통 예상 갭)

- 서비스 간 인증·권한 방식(연동 인터페이스의 auth) — 은행 [확인 필요], 문면 미기재. AI EM 면접 프로브 예상.
- 차기 버전 운영 지표(품질·지연·비용) — 은행에 없음. 평가 240건의 결과 수치도 없음.
- 본인 담당 모듈 구체 예시 — 커밋 0건 리스크와 직결.
- Kubernetes·클라우드 관리형 AI 서비스(GCP·Bedrock 등)·Cursor — 미보유 확정 또는 근거 없음, 문면 미기재(C-06).
