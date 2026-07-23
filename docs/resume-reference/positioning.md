# Positioning (헤드헌터 인터뷰 기반 포지셔닝 레이어)

`experience-bank.md`(사실)와 `writer`/`tailor`(문구 작성) 사이에 있는
**회사-무관 전략 레이어**다. `headhunter-advisor` 스킬의 인터뷰로 채워진다.
사실이 아니라 "이 경험을 어떻게 포지셔닝할지, 뭘 강조할지, 약점을 어떻게
방어할지" 같은 전략적 판단만 담는다 — `experience-bank.md`의 "사실만" 원칙을
지키기 위해 별도 파일로 분리했다.

## 운영 규칙

- **기록 주체**: `canonical-lines.md`/`role-presets.md`와 동일 원칙 — 최상위
  에이전트만 소유자 confirm을 받고 직접 쓴다. 서브에이전트는 이 파일을
  편집하지 않는다.
- **사실 분리**: 인터뷰 중 아직 `experience-bank.md`에 없는 새 사실(수치·역할·
  기간 등)이 나오면, 여기 적기 전에 기존 갭 인터뷰 방식대로 `archivist`를
  통해 `experience-bank.md`에 먼저 적재한다. 이 파일은 그 위에 얹는 전략
  판단만 기록한다.
- **`EXP-NN` ID**: `canonical-lines.md`의 경험 ID 매핑을 그대로 재사용한다.
  새 경험이 추가되면 그 파일의 매핑을 먼저 갱신한 뒤 여기서 참조한다.
  경험 단위가 아닌 서사 전체에 대한 판단은 `전체/서사`로 표기한다. 아직
  `canonical-lines.md`에 매핑이 없는 `experience-bank.md` 항목은 이 파일에
  적지 않는다 — 매핑 추가(승인제)가 먼저다.
- **증분**: 이미 항목이 있는 `EXP-NN` × 직무 조합은, 소유자가 명시적으로
  재인터뷰를 요청하지 않는 한 다음 인터뷰 라운드에서 건너뛴다. 직무가
  다르면(예: 기존 항목은 백엔드 기준, 이번은 프론트엔드) 스킵하지 않고
  해당 직무 관점의 `target_fit_notes`를 추가한다.
- **출처 표기**: 어떤 헤드헌터 페르소나(`headhunter-startup` /
  `headhunter-searchfirm` / `headhunter-techlead`)의 질문에서 이 판단이
  나왔는지 남긴다 — 나중에 어떤 관점이 이 강조를 이끌어냈는지 추적 가능하게.

## 스키마

```yaml
- exp: EXP-01              # canonical-lines.md 매핑 재사용, 서사 전체는 "전체/서사"
                            # 여러 경험에 걸친 판단이면 리스트로: [EXP-01, EXP-05]
  job_function: IT 개발자   # 이 판단을 이끌어낸 인터뷰 라운드의 직무
  headline_angle: "이 경험을 한 줄로 포지셔닝하면"
  strengths: [강조할 포인트 1, 강조할 포인트 2]
  weak_points_defense: "이 경험/서사의 약점과 방어 논리"
  target_fit_notes: "어떤 직무/회사군에 특히 잘 맞는지"
  source_persona: [headhunter-startup, headhunter-techlead]
  confirmed: YYYY-MM-DD   # 소유자 confirm 받은 날짜
```

**같은 `EXP-NN`, 다른 `job_function`**: 새 블록을 통째로 추가한다(부분
필드만 있는 블록은 만들지 않는다). `headline_angle`/`strengths`/
`weak_points_defense`가 이전 직무 판단과 동일하면 그대로 반복해서 적고,
`target_fit_notes`만 새 직무 관점으로 다시 쓴다 — 각 블록이 항상 완결된
판단 단위여야 나중에 `writer`/`tailor`가 직무별로 골라 읽기 쉽다.

## 항목

```yaml
- exp: 전체/서사
  job_function: IT 개발자
  headline_angle: null   # 강조가 아니라 방어 목적 판단
  strengths: []
  weak_points_defense: >
    2017~2020 IT 무관 공백(3년 7개월)은 올리브영 매장 판매직 재직
    (2017.03-2018.07), 일본 워킹홀리데이(2018.09-2019.06), IT 국비지원학원
    자바 풀스택 과정 수료(2020.03-2020.09)로 전부 설명 가능. 이력서
    자체에는 IT 무관 이력이라 미기재하기로 함(소유자 결정) — 면접 등에서
    공백을 질문받으면 이 타임라인으로 방어. 국비학원 수료(자바 풀스택)를
    IT 커리어 실질 출발점으로 잡으면 "진로 전환 후 5년+ 꾸준한 성장"이라는
    서사로도 프레이밍 가능.
  target_fit_notes: 공백 자체는 직무 적합도와 무관 — 서사 완결성/면접 방어용
  source_persona: [headhunter-searchfirm, headhunter-startup]
  confirmed: 2026-07-23

- exp: 전체/서사
  job_function: IT 개발자
  headline_angle: >
    SI 5년 후 AI 제품 조직으로: ChatGPT-4o 등장 시점 AI 기술 습득
    필요성을 느끼고 스스로 학습(ML/DL/LLM: Langchain, HuggingFace, RAG,
    VectorDB)한 뒤 AI 활용 플랫폼/SW를 만드는 조직으로 의도적으로 이직
  strengths:
    - 이직 전 자발적 학습으로 방향 전환을 준비한 능동성
    - SI 환경에서 라이브러리/스택 선택권은 없었지만 캡슐화·디자인패턴을
      고려한 코드 구성으로 설계 판단력을 발휘
  weak_points_defense: >
    SI 5년간 기술스택 의사결정권은 없었다(구조적 제약) — 숨기지 않되, 그
    안에서도 캡슐화/디자인패턴을 고려한 코드 구성이라는 설계 판단을
    스스로 행사했다는 근거로 방어. LLM 관련 학습(Langchain/HuggingFace/
    RAG/VectorDB)은 이직 준비를 위한 자기학습이며, 현재 실무 프로덕션
    적용 사례는 EXP-01의 SSE 기반 프론트엔드 통합 수준이다 — 백엔드 LLM
    파이프라인을 직접 구축한 경험으로 과장하지 않는다.
  target_fit_notes: >
    AI 제품/플랫폼 직무, 특히 "기술 트렌드에 능동적으로 반응하는 인재"를
    찾는 회사에 서사 적합. LLM 스킬은 실무 스킬로 나열하지 말고
    자기소개서 동기 서술에만 활용할 것.
  source_persona: [headhunter-searchfirm, headhunter-startup]
  confirmed: 2026-07-23

- exp: 전체/서사
  job_function: IT 개발자
  headline_angle: null
  strengths: []
  weak_points_defense: >
    삼성물산 프로젝트 표기 종료(2025.04)와 대웅제약 입사(2025.07) 사이
    3개월은 실제 이직 준비 공백이 아니다 — 내담씨앤씨 재직은 2025.06까지
    계속됐고, 경력기술서에는 대표 프로젝트(삼성물산) 위주로 적혀 있어
    시각적으로 공백처럼 보일 뿐이다. 이 기간의 업무는 삼성물산 프로젝트의
    연장으로 설명한다(소유자 확인 2026-07-23 — 별도 프로젝트명 특정은
    하지 않음; `profile.md`/`experience-bank.md`의 공식 표기 기간은
    변경하지 않고 이 서사만 인터뷰/자기소개 방어용으로 둔다). 대웅제약행은
    반응적 이직이 아니라 위 블록에서 확인한 AI 전환 동기에 따른 계획된
    이동이다.
  target_fit_notes: 타임라인 정합성 방어용, 강조 포인트 아님
  source_persona: [headhunter-searchfirm]
  confirmed: 2026-07-23

- exp: EXP-01
  job_function: IT 개발자
  headline_angle: >
    유일한 프론트엔드 담당자로 AI 건강검진 챗봇의 FE 아키텍처를
    설계·구현·테스트까지 단독 수행하고, BE/LLM 로직에도 교차 기여한
    풀사이클 오너십 사례
  strengths:
    - FE 영역 단독 기술 의사결정권 + End-to-End 수행(설계~테스트)
    - BE/LLM 개발자와 협업하며 경계를 넘나든 교차 기여
  weak_points_defense: >
    LLM/BE 기여는 팀 공동이며 단독 구축이 아니다 — "LLM 서버를 직접
    구축했다"처럼 과장하지 않고, 정확히 "프론트엔드 단독 오너십 + BE/LLM
    일부 기여"로 구분해서 서술한다.
  target_fit_notes: >
    오너십·독립적 문제해결을 중시하는 스타트업/스케일업 스크리닝에
    최우선 카드로 사용. 인원 규모가 큰 대기업 스크리닝에서는 "왜 혼자
    담당했는가"(팀 규모 제약)를 먼저 설명해야 방어적으로 읽히지 않는다.
  source_persona: [headhunter-startup]
  confirmed: 2026-07-23

- exp: EXP-01
  job_function: IT 개발자
  headline_angle: >
    전사 차등가격 정책 요구를 Config-Driven UI + feature flag 아키텍처로
    해결 — 완성된 코드베이스의 대규모 리팩토링을 감수하고 신규 고객사
    (웰체크) 커스터마이징을 FE 기준 2주로 단축
  strengths:
    - 비즈니스 요구(기능별 차등 과금)를 아키텍처 결정으로 직접 번역한
      설계 판단
    - 기획자/운영자도 FE 단에서 기능을 제어할 수 있게 해 조직 전체의
      반복 운영 비용을 낮춤
    - 이미 완성된 코드베이스를 갈아엎는 리스크를 감수하고 구조 전환 수행
  weak_points_defense: >
    "10주→2주" 단축 수치는 FE 작업 기준이며 BE/LLM 납품 일정은 별도다 —
    스코프를 명시하지 않고 "전체 챗봇을 2주 만에 만들었다"처럼 쓰면
    과장이 된다. 반드시 "FE 커스터마이징 기준"으로 한정해서 서술한다.
    도입 고객사명(웰체크) 공개는 소유자 승인 완료(2026-07-23).
  target_fit_notes: >
    시스템 설계/아키텍처 판단력을 중시하는 테크리드/CTO 관점 스크리닝에
    강한 카드. 스코프(FE 한정) 왜곡 없이 정확히 서술해야 tech-screen
    게이트에서 감점되지 않는다.
  source_persona: [headhunter-techlead]
  confirmed: 2026-07-23

- exp: EXP-06
  job_function: IT 개발자
  headline_angle: >
    4.66억 매출 기여는 조직 전체 KR 인용이지만, 4개 프로젝트 전부에 FE
    개발자로 직간접 기여 — 프로젝트별 기여 강도가 다르므로 구분해서
    정직하게 서술
  strengths:
    - 비즈케어 UI/UX 개편을 주도해 실제 판매(1.0억)로 직접 연결시킨
      가장 뚜렷한 개인 기여 사례
    - 4개 프로젝트(비즈케어/AI코치/생체나이/에스크미) 전체에 FE
      개발자로 참여한 폭넓은 커버리지
  weak_points_defense: >
    4.66억은 조직 전체 KR 목표 수치이지 개인 단독 성과가 아니다 —
    본인이 직접 인정한 사실. 프로젝트별 기여 강도도 다르다: 비즈케어
    (UI/UX 개편 주도)가 매출과 가장 직접 연결되는 가장 강한 사례이고,
    생체나이(외주 V2 유지보수·수정)와 에스크미(유지보수 지원)는 상대적
    으로 약한 기여, AI코치(비즈케어 파생 패키지 판매)는 간접적이다.
    "4.66억 매출 기여"를 단일 숫자로 전면에 내세우면 팀 성과 포장으로
    읽힐 위험이 크다 — 반드시 "조직 KR 대비" 스코프를 밝히고, 개인
    기여가 가장 뚜렷한 비즈케어 UI/UX 개편 사례를 대표로 내세운다.
  target_fit_notes: >
    매출 수치를 헤드라인으로 쓰기보다 비즈케어 UI/UX 개편처럼 기여가
    명확한 사례 중심으로 서술할 것. recruiter-screen 게이트에서 "팀
    성과 포장" 리스크로 감점되지 않도록 writer/tailor가 이 구분을
    반드시 반영해야 한다.
  source_persona: [headhunter-startup]
  confirmed: 2026-07-23

- exp: EXP-02
  job_function: IT 개발자
  headline_angle: >
    모놀리식+Thymeleaf 강결합 환경에서 SPA 전면 전환이 불가능한 제약
    아래, island-loader 패턴으로 컴포넌트 재사용 가능한 점진 전환
    구조를 설계 — 108페이지·82화면 전체를 단독으로 9주 내 전환
  strengths:
    - 기술적 제약(레거시 강결합)을 인지하고 실현 가능한 전환 경로를
      스스로 설계
    - 향후 Next.js 전환까지 내다본 단계적 아키텍처 로드맵 수립
    - 108페이지·82화면 전체를 단독으로 수행한 실행력
  weak_points_defense: >
    "island-loader"는 업계 표준 용어(예: Astro의 island architecture)와
    혼동될 수 있으니, 면접에서는 본인이 실제 구현한 방식(React를 화면
    단위로 부분 마운트해 재사용 가능하게 만든 패턴)을 구체적으로 설명할
    준비가 필요하다. "Next.js 전환을 쉽게 하기 위해"라는 목표가 실제로
    실행됐는지(이 프로젝트가 아니라 EXP-05는 다른 회사/프로젝트) 여부를
    정확히 구분해서 말해야 한다 — 아직 실행 전이면 "계획된 로드맵"으로
    한정해서 서술한다.
  target_fit_notes: >
    시스템 설계/마이그레이션 전략을 중시하는 테크리드 스크리닝에 강한
    카드. "레거시 강결합 환경에서 점진 전환 전략을 설계한 사례"로 사용.
  source_persona: [headhunter-techlead]
  confirmed: 2026-07-23

- exp: [EXP-02, EXP-07]
  job_function: IT 개발자
  headline_angle: >
    island-loader(EXP-02)와 Node/Express BFF(EXP-07)는 개별 기술 선택이
    아니라, 모놀리식(Spring Boot+Thymeleaf 강결합) 구조를 점진적으로
    RESTful/컴포넌트화하려는 하나의 아키텍처 전략의 두 축
  strengths:
    - 개별 프로젝트를 넘어서는 시스템 수준의 일관된 아키텍처 판단력
    - 두 프로젝트를 묶어 서술하면 "단발성 기술 선택"이 아니라 "의도된
      마이그레이션 로드맵"으로 읽힘
  weak_points_defense: >
    EXP-07의 BFF 구축은 experience-bank.md에 명시된 대로 "팀 공동"이다
    — 이번 답변에서도 런타임 선택을 단독 주도했다는 명시적 확인은
    없었다. 전략적 배경(왜 이런 선택을 했는지)은 본인 관점에서 설명하되,
    "의사결정을 단독으로 주도했다"고 과장하지 않는다 — 팀 공동
    의사결정 안에서 이 전략적 맥락을 이해하고 실행에 기여했다는
    수준으로 서술한다.
  target_fit_notes: >
    두 프로젝트를 하나의 아키텍처 서사로 묶어 테크리드/CTO 관점
    스크리닝에 제시하면 개별 사례보다 설득력이 크다. writer/tailor는
    이 둘을 같은 이력서/자소서 섹션에서 연결해서 서술하는 것을 고려.
  source_persona: [headhunter-techlead]
  confirmed: 2026-07-23
```
