# AI 멀티 에이전트 데모 저장소 스펙 (지오영 지원 근거용, 2026-09-09 초안)

목적: 이력서의 "RAG·VectorDB·멀티 에이전트·Redis 세션·SSE 스트리밍을 백엔드부터 프론트까지
설계·구현할 수 있다"를 **소유자 명의 공개 코드**로 증명. 기술 인터뷰 필수 질문 5개
(에이전트 분해·툴 정의·컨텍스트 소스·실패 시 사람 개입·검증 기준)에 저장소로 답한다.
beads: my-recruit-8kl

## 범위 (1.5일 목표 — Claude Code 활용)

- 도메인: 건강검진 결과 Q&A (AI코치와 겹치되 사내 코드·데이터 미사용, 공개 참고치 샘플만)
- 서버 (Python 3.12 · FastAPI · asyncio)
  - `POST /chat` → SSE 스트리밍 (이벤트: progress / route / token / result / error / done)
  - 오케스트레이터: 프리필터(PII 정규식) → 의도 분류(LLM, JSON) → 라우팅 → 서브에이전트 병렬(asyncio.gather) → 종합
  - 서브에이전트 3개: `interpret`(검진 수치 해석, RAG) / `hospital`(안내, MCP 도구 호출) / `general`(폴백)
  - 턴 예산(예: 30초)·에이전트별 타임아웃·부분 실패 시 나머지 결과로 응답
  - LLM 어댑터: Anthropic + OpenAI (env로 전환), 재시도 1회·타임아웃 명시
- 메모리: Redis — 세션별 최근 N턴(STM), TTL. (선택) 요약 LTM
- RAG: Qdrant(로컬 docker) + 한국어 임베딩(KR-SBERT 또는 API), 공개 참고치 문서 청킹·인덱싱 스크립트
- MCP: FastMCP 서버 1개(`search_guideline` 도구, stdio) — `hospital` 에이전트가 MCP 클라이언트로 호출
- 클라이언트: React + TypeScript, SSE 수신·토큰 렌더·중지·재시도·에러 상태
- 검증 하네스: pytest(라우팅·프리필터·타임아웃 단위 테스트) + 발화 회귀 스크립트(질문 xlsx → 응답 저장·판정 규칙)
- 관측: 턴별 trace_id, 토큰·비용 로그(SQLite 또는 jsonl)
- 인프라: docker-compose (api · redis · qdrant), README에 아키텍처 다이어그램·설계 결정(트레이드오프) 5개

## 이력서 매핑
- 핵심역량 ① 능력 주장 근거 → "개인 프로토타입 3건" 뒤에 "멀티 에이전트 데모(GitHub)" 추가
- 상세경력: 개인 프로젝트 항목 신설 또는 자소서 학습 서사에 링크
- 면접: 설계 결정 5개(라우팅 방식·예산·폴백·컨텍스트 조립·검증 기준)를 README에 그대로 답변화

## 제외
- 사내 데이터·코드·프롬프트 재사용 금지(보안), 결과 수치 과장 금지(측정치만 README에)
