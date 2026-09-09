# Source Materials

This file records the source files imported into the project and how they should
be used when drafting resumes or cover letters.

## Imported Files

| File | Type | Imported To | Extracted Text |
| --- | --- | --- | --- |
| `이력서_20260624.pdf` | Existing resume PDF | `sources/이력서_20260624.pdf` | `extracted/이력서_20260624.txt` |
| `2026_상반기종합평가.xlsx` | 2026 first-half performance review | `sources/2026_상반기종합평가.xlsx` | `extracted/2026_상반기종합평가.md` |
| `연종합평가2025_정다훈.xlsx` | 2025 annual performance review | `sources/연종합평가2025_정다훈.xlsx` | `extracted/연종합평가2025_정다훈.md` |
| `월별피드백_정다훈.xlsx` | 대웅제약 재직 중 월별 자가 피드백 13개월치 (2025.07~2026.07) | `sources/월별피드백_정다훈.xlsx` | `daewoong-history.md` (본인 · 잘한 점 칼럼만 추출, 원문 보존) |
| `월별피드백_정다훈 (7).xlsx` | 위 파일의 갱신본 — 2026년 8월분(14번째 월)이 추가됨. 시트 "2026년 8월 월별피드백", 구분=본인·잘한 점 칼럼만 소유자 2026-09-09 사용 승인(지오영 AI 개발 지원 세션 갭 인터뷰). | 원본은 `~/Downloads/월별피드백_정다훈 (7).xlsx`에 있으며 **이 프로젝트 `sources/`로 아직 임포트되지 않음** — archivist 세션에 xlsx를 직접 여는 도구(Bash/python3+openpyxl)가 없어 셀 원문 재확인·복사를 하지 못했다([확인 필요]: 파일 임포트 및 원본 셀 구조 재확인). | `daewoong-history.md` 「월별 원문」 2026-08 절(요약, [전사 방식 주석] 참조), `experience-bank.md` EXP-03 증강, `metric-registry.md`(상위 에이전트가 기등재) |
| `정다훈_직무급 지원서_잡멘토(멘토).docx` | 사내 직무급 지원용 변화혁신과제 보고서 (2026-03 작성, STAR 구조) | `sources/직무급지원서_변화혁신과제_정다훈.docx` | `daewoong-history.md` 부록 A |
| 자격증 스크린샷 2건 (Microsoft AZ-900, 자산관리사(FP)) | 사용자 제공 스크린샷 이미지 (파일 미보관, 텍스트만 전사) | N/A — 원본 이미지 파일 경로 미제공 | 자격 정보를 `source-log.md` 2026-08-21 항목에 전사·기록. `profile.md` Education / Certifications 반영은 archivist 소관 밖이라 제안만 전달(편집 없음) |
| `my-health-ai-coach-llm-version2` (로컬 git 저장소, 지오영 AI 개발 지원 세션, 2026-09-09 archivist 코드 조사) | AI코치 v2 멀티 에이전트 서버(llm-aicoach-007-MAS 전환) 코드베이스 | `/Users/2302-n0214/Documents/workspaces/my-health-ai-coach-llm-version2` | 추출 파일 없음 — 직접 코드 열람. 커밋 저자: kimhyungjun 195/208, soooz 9, 김진희 3, taehan lee 1, **정다훈 0건**(기여 범위는 EXP-01 user-attested + 이 저장소 documentary 병용, `experience-bank.md` 신규 항목 "나만의 건강 AI코치 v2 멀티 에이전트 서버(llm-aicoach-007-MAS) 전환 참여" 참조) |
| `my-health-ai-coach-web` (로컬 git 저장소, 같은 세션, 2026-09-09 archivist 코드 조사) | AI코치 웹 프런트엔드 코드베이스 | `/Users/2302-n0214/Documents/workspaces/my-health-ai-coach-web` | 추출 파일 없음 — 직접 코드 열람. 커밋 저자: **정다훈 1,077/1,117**(2025-07-03~2026-09-04, 압도적 본인 기여). `experience-bank.md` EXP-03("품질·개발·운영 자동화 및 FE AX 기준 수립") 증강분(에러 리포트 파이프라인·LLM 채팅 응답 검수 도구 확인·SSE·성능·PostHog 대조 도구·`.claude/` 하네스 자산) 참조 |
| `chatbot-boilerplate` (로컬 git 저장소, 같은 세션, 2026-09-09 archivist 코드 조사) | 개인 사이드 프로젝트 — React/TypeScript LLM 챗봇 보일러플레이트 | 경로 미기록(archivist 로컬 조사, 소유자 워크스페이스) | 추출 파일 없음 — 직접 코드 열람. 커밋 저자: 정다훈 19/19(2026-01-02, 전량 단독). `experience-bank.md` "AI 소프트웨어 사이드 프로젝트 (개인)" 항목 증강분 참조 |
| `mcp_test` (로컬 git 없음, 같은 세션, 2026-09-09 archivist 코드 조사) | 개인 프로토타입 — Python FastMCP 터미널 서버 + MCP 클라이언트 2종 | 경로 미기록(archivist 로컬 조사, 소유자 워크스페이스) | 추출 파일 없음 — 직접 코드 열람. git 저장소 없음(커밋 이력 미확인, 날짜는 파일시스템 기준 2025-10-09~10 추정). 사내 MCP 서버(EXP-03)와 별개 — 혼용 금지. `experience-bank.md` "AI 소프트웨어 사이드 프로젝트 (개인)" 항목 증강분 참조 |
| `test-vector` (로컬 git 없음, 같은 세션, 2026-09-09 archivist 코드 조사) | 개인 프로토타입 — Qdrant+KR-SBERT+LangChain RetrievalQA+Gemini 1.5 RAG(Gradio 앱) | 경로 미기록(archivist 로컬 조사, 소유자 워크스페이스) | 추출 파일 없음 — 직접 코드 열람. git 저장소 없음(날짜는 파일시스템 기준 2025-07-04 추정). **보안: `vector_app.py`에 Google API 키 평문 하드코딩 확인 — 소유자에게 키 폐기·교체 권고, 코드 내용 인용 금지.** `experience-bank.md` "AI 소프트웨어 사이드 프로젝트 (개인)" 항목 증강분 참조 |

## Use Guidance

- Use `profile.md` for stable personal and career facts.
- Use `experience-bank.md` for reusable project evidence, metrics, and bullet
  fragments.
- Use extracted files only for audit or when additional detail is needed.
- Do not paste long raw excerpts from the extracted files into final
  application documents.
- Treat performance-review improvement sections as development themes, not as
  negative wording to copy directly into applications.
- Product names may vary by source. Normalize naming in final documents:
  - `비즈케어` / `비즈36.5`
  - `생체나이` / `바이오에이지`
- Some metrics are source-stated but need scope confirmation before use in
  high-stakes external documents. Check `experience-bank.md` > `Metrics To
  Verify`.

## Sensitive Data Notes

- Contact information, age, gender, address, salary, and private evaluation
  content may be sensitive. Confirm inclusion before producing external-facing
  documents.
