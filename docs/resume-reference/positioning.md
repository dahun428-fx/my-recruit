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

(아직 없음 — `headhunter-advisor` 스킬 인터뷰로 채워진다.)
