---
name: resume-engine
description: 새 회사 이력서를 재조립 엔진으로 생산한다. 자동(2-스톱) 모드와 인터뷰 모드를 지원하며, 갭 인터뷰로 experience-bank를 키운다. Use when the owner asks for a new company resume variant or says "이력서 엔진 돌려줘".
---

# Resume Engine (2-스톱 드라이버)

`AGENTS.md`의 **Resume Engine** 섹션이 정본이다. 이 스킬은 그 흐름을 최상위
에이전트가 운전하는 절차서다. 산출물 규칙(no-fabrication, feedback-rules,
canonical verbatim)은 각 서브에이전트 파일과 참조 문서가 정본이며 여기서
반복하지 않는다.

## 모드 선택

- 소유자가 "인터뷰 모드" / "수동으로" / "물어보면서 하자"라고 하면 → 인터뷰
  모드. 프리셋 없는 직무군이면 인터뷰 모드를 먼저 제안한다.
- 그 외 기본은 자동(2-스톱) 모드.

## 자동 모드 (2-스톱)

1. **JD 수집** — JD 텍스트를 소유자에게 받아 `tailor`가
   `target-companies.md`에 엔트리를 만든다 (수집일·출처 필수).
2. **브리프 생성** — `tailor`가 `role-presets.md`에서 프리셋을 고르고 브리프
   템플릿대로 작성. 갭 인터뷰 항목(은행/experience-bank 무근거 JD 요건)을
   반드시 포함시킨다.
3. **⏸ 스톱 ①: 브리프 승인** — AskUserQuestion으로 브리프 승인/수정을 받는다.
   갭 인터뷰 항목이 있으면 이 시점에 함께 질문한다 (한 번에 묶어서).
   - 갭 답변은 user-attested로 `archivist`를 통해 `experience-bank.md`에
     적재한 뒤 진행한다.
   - Screen profile / Role preset 태그도 이 승인으로 확정하고 엔트리에 쓴다.
4. **자율 핑퐁 (원칙적으로 소유자 개입 없음)** —
   a. `writer`/`tailor`가 재조립 초안 + `outputs/<slug>-new-prose.md`(신규
      작문 / candidate 재사용 / 신규 구조·목록 항목, 3섹션) 생성. 초안이
      나오면 **레인 재판정** — `AGENTS.md`의 full lane 조건 목록(정본)을
      기준으로 재검사하고, 갭 인터뷰로 experience-bank가 갱신될 때마다도
      재판정한다. 신규 작문 과반 판정에서 candidate 재사용은 산입하지
      않는다(companion 리뷰로 이미 커버되므로 — `AGENTS.md` 참조). 조건
      해당 시 full lane으로 조용히 전환하고 스톱 ②에서 보고한다.
   b. `reviewer`(fast lane이면 전수 무결성 대조 + companion 스코프 명시) +
      `ats` 병렬 → 지적사항을 `writer`/`tailor`가 수정. **수정할 때마다
      companion 파일도 갱신한다.**
   c. companion 파일 내용에 한해 적대 검증 패스(fresh Claude subagent) 1회
      (fast lane 한정 축소 — full lane은 CLAUDE.md 루프 전체 적용). 수용된
      지적은 여기서 수정한다 — **채점 전에** 끝내야 점수가 최종본 기준이
      된다.
   d. `recruiter-screen` + `tech-screen` 병렬 (해당 회사 Screen profile로
      포지셔닝). fast lane 채점은 **P-01 3라운드 캡의 1라운드째로 집계**한다.
      FAIL이면 full lane으로 전환해 **크리틱 단계부터**(전체 스코프 reviewer
      포함) 재진입, 남은 2라운드 안에 미통과면 점수·블로커를 보고하고 멈춘다.
      블로커 수정으로 초안이 바뀌면 재채점 전에 companion을 갱신한다.
   e. **최종 무결성 재검증** — 마지막 초안 변경 이후 `reviewer` 무결성
      패스(전수 대조)를 다시 실행한다. 채점·수정 과정에서 approved 문장이
      변형됐는데 companion에 반영되지 않은 경우를 잡는 마지막 관문이며,
      이 재검증을 통과해야 스톱 ②로 간다.
   - **예외**: 이 구간에서 새 갭(은행/experience-bank 무근거 JD 요건)이
     발견되면 자율 진행을 중단하고 갭 인터뷰를 연다. 요건을 조용히 빼는 것은
     금지.
5. **⏸ 스톱 ②: diff 승인** — `<slug>-new-prose.md` **전체**(신규 작문 +
   재사용된 candidate 문장 + 신규 구조·목록 항목, 라벨 구분) + 게이트 점수
   요약 + 레인 전환 여부를 보여주고 승인받는다. 수정 요청은 4로 되돌아간다.
   PASS 이후 소유자 요청으로 도는 수정·재채점 라운드는 P-01의 3라운드
   실패 캡에 산입하지 않는다(캡은 FAIL 누적 기준).
6. **렌더 + 승격 루프** — `designer`가 PDF/HTML 렌더. 확정된 신규 문장을
   `canonical-lines.md` 승격 후보로, 브리프 예외를 `target-companies.md`에
   기록 제안한다 (둘 다 승인제).

## 인터뷰 모드

1. JD 수집은 자동 모드와 동일.
2. JD를 섹션 요건으로 분해한 뒤, **섹션별로 한 번에 하나씩** 소유자와
   확정한다: "이 요건에는 은행에 이 문장들이 있다(후보 제시) — 쓸까요,
   새로 말씀해줄 내용이 있나요?" 형식. AskUserQuestion 사용, 항목마다
   은행 후보를 preview로 보여준다.
3. 갭을 만나면 즉시 갭 인터뷰 (자동 모드와 동일하게 experience-bank 적재).
4. 전 섹션 확정 후, 자동 모드 4단계로 합류하기 **전에 미니 브리프 확인**을
   한 번 받는다: Screen profile / Role preset 태그 확정(엔트리에 기록),
   레인(잠정) 고지, 인터뷰 중 누적된 프리셋 예외 요약 — 스톱 ①의 부수 효과
   (게이트 포지셔닝·승격 루프의 예외 기록)를 여기서 수행한다.
5. 이후 자동 모드 4-6단계(자율 핑퐁 → diff 승인 → 렌더)로 합류한다.
   diff 승인에서 소유자가 항목별 확정한 뒤 **변경되지 않은** 항목은 요약
   확인으로 가볍게, 자율 핑퐁 중 수정된 항목(크리틱·게이트·적대 패스 반영분)
   은 자동 모드와 동일하게 전문을 보여준다.

## 레인 판정

fast lane / full lane 조건은 `AGENTS.md` Resume Engine 섹션 기준.
판단이 애매하면 full lane. 어느 레인인지 스톱 ①에서 소유자에게 고지한다.
