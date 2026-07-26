# Agent Instructions

This file is the canonical project guidance for all coding agents working in
`my-recruit`.

## Purpose

`my-recruit` is a project for managing the owner's resume / CV.

## Process Rules

All agents follow the active and probation rules in
`docs/harness-reference/process-rules.md` — the owner's process-preference
ledger for how agents work (reporting, procedure, delegation, confirmation).
Probation rules are provisional but still applied; only the top-level agent
logs `적용` history and proposes promotion. Claude loads the ledger
automatically via a `CLAUDE.md` import; **any non-Claude agent must
read the ledger before substantive work.** Top-level agents summarize the
relevant active/probation rules into every subagent dispatch prompt.
Rules marked `범위: Claude` bind only Claude sessions. Only the top-level
agent edits rule text or state, and only with owner approval; the capture and
lifecycle protocol lives in the ledger header and `CLAUDE.md`.

## Repository Layout

`my-recruit` is **not** its own git repository. The git root is the parent
directory `C:\workspaces2`, which also tracks unrelated sibling projects
(`bizcare`, `my-fortune`, `my-health-ai-coach-web`, etc.).

- `git status` / `git log` here reflect the **entire** workspace. Scope git
  commands to this directory, for example `git status -- .`.
- Do not stage or commit changes from sibling projects.
- Do not auto-push from this project. Ask before push or commit workflows.

## Beads Issue Tracker

This project uses **bd (beads)** for local issue tracking. Run `bd prime` for
full workflow context.

> **Architecture in one line:** Issues live in a local Dolt database
> (`.beads/dolt/`); cross-machine sync uses `bd dolt push/pull` (a
> git-compatible protocol), stored under `refs/dolt/data` on your git remote,
> separate from `refs/heads/*` where code lives. `.beads/issues.jsonl` is a
> passive export, not the wire protocol.
>
> See [SYNC_CONCEPTS.md](https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md)
> for the one-screen overview and anti-patterns: do not treat JSONL as the
> source of truth, do not run `bd import` during normal operation, and do not
> reach for third-party Dolt hosting before trying the default.

Quick commands:

```bash
bd prime
bd ready
bd show <id>
bd update <id> --claim
bd close <id>
```

Project rules:

- Use beads for project task tracking when an issue/task record is useful.
- If `bd` is not found in a new shell, use
  `C:\Users\jungdahun\AppData\Local\Programs\bd\bd.exe` or reopen the terminal
  after PATH refresh.

## Non-Interactive Shell Commands

Always use non-interactive flags with file operations to avoid hanging on
confirmation prompts.

Shell commands like `cp`, `mv`, and `rm` may be aliased to include `-i`
(interactive) mode on some systems, causing the agent to hang indefinitely
waiting for y/n input.

Use these forms instead:

```bash
# Force overwrite without prompting
cp -f source dest           # NOT: cp source dest
mv -f source dest           # NOT: mv source dest
rm -f file                  # NOT: rm file

# For recursive operations
rm -rf directory            # NOT: rm -r directory
cp -rf source dest          # NOT: cp -r source dest
```

Other commands that may prompt:

- `scp` - use `-o BatchMode=yes` for non-interactive
- `ssh` - use `-o BatchMode=yes` to fail instead of prompting
- `apt-get` - use `-y` flag
- `brew` - use `HOMEBREW_NO_AUTO_UPDATE=1` env var

## Cross-Agent Review

Use `scripts/claude_review.py` when you want an independent Claude review pass
on the working diff. The default input is scoped to this project with
`git diff -- .`.

Examples:

```bash
.\.venv\Scripts\python.exe scripts\claude_review.py
.\.venv\Scripts\python.exe scripts\claude_review.py --files AGENTS.md CLAUDE.md
.\.venv\Scripts\python.exe scripts\claude_review.py --staged
```

## Agent Team

This project uses a team of specialist subagents defined in
`.claude/agents/`. Each maps to one stage of the resume workflow and owns a
narrow set of files. **Critics are read-only** (no `Write`/`Edit`); producers
write only within their owned files. Dispatch them via the agent/Task tool.

| Agent | Role | Owns / writes | Access |
| --- | --- | --- | --- |
| `archivist` | Ingest raw sources; extract verified facts | `experience-bank.md`, `source-materials.md`, `source-log.md` | read-write |
| `writer` | Draft resume / cover letter / self-intro | drafts in `outputs/` | read-write |
| `tailor` | Adapt a draft to a specific job posting | `target-companies.md` notes, variants in `outputs/` | read-write |
| `reviewer` | Fact-check vs evidence base; guideline critique | — (reports findings) | **read-only** |
| `ats` | Keyword-coverage check vs a JD | — (reports findings) | **read-only** |
| `recruiter-screen` | HR/recruiter screening score (인사담당자); 0-100 + PASS/FAIL gate | — (reports score) | **read-only** |
| `tech-screen` | Technical hiring-manager score (기술담당자); 0-100 + PASS/FAIL gate | — (reports score) | **read-only** |
| `designer` | Render visual / print artifacts | artifacts in `outputs/` | read-write |

Producers must follow the no-fabrication rule in
`docs/resume-reference/writing-guidelines.md`: use only verified facts from
`profile.md` and `experience-bank.md`, and mark missing evidence with a
`[확인 필요]` placeholder rather than inventing it. The `designer` follows
`DESIGN.md` and must not alter prose.

Producers (`writer`, `tailor`) must also follow the owner's personal style
ledger `docs/resume-reference/feedback-rules.md`. On conflict with
`writing-guidelines.md`, the ledger's active rules win (no-fabrication always
stays supreme). `reviewer` audits drafts against every active `MUST`/`NEVER`
ledger rule and reports violations by rule ID; `PREFER` deviations are
reported as questions, not blockers. The ledger's own header defines how rules
are captured, generalized, toggled (`active`/`retired`), and capped.

### Handoff playbook

```
archivist  → build / refresh the evidence base
   ↓
writer     → draft from the bank
   ↓
tailor     → produce a JD-specific variant
   ↓
reviewer + ats  → parallel read-only critique
   ↓
(writer / tailor revise)
   ↓
recruiter-screen + tech-screen  → SCORE GATE (parallel, read-only)
   ↓  ← both PASS?  no → (writer / tailor revise) → re-score
   ↓  ← both PASS?  yes ↓
designer   → render the final visual artifact
```

`reviewer` is a same-model fact/guideline pass. It **complements, not replaces**,
the adversarial verification loop (see `CLAUDE.md`): a fresh Claude subagent
hardening pass that should run after `reviewer`.

#### Score gate (인사·기술담당자 통과 기준)

Every resume/CV draft must clear a two-grader score gate before it is treated as
final (rendered by `designer`, or delivered to the owner as done). After
`reviewer`/`ats` findings are addressed, dispatch **both** graders in parallel
on the current draft:

- `recruiter-screen` (인사담당자) and `tech-screen` (기술담당자) each return a
  `0-100` score, a `PASS`/`FAIL` verdict, and blockers.
- **Positioned to the target company.** Both graders position themselves to the
  target company using `docs/resume-reference/screen-profiles.md`: the entry's
  `Screen profile:` tag selects the rubric **weights**, the persona lens is
  grounded **only** in the entry's signals/scope/skills, and company-specific
  auto-FAIL **blockers** derive from its `Required skills` / `Risks or gaps`.
  An entry with **no `Screen profile:` tag or `TBD` signals** is graded with
  `Balanced` at bar 80 plus a warning.
- **Gate = AND.** The draft passes only when **both** verdicts are `PASS`
  (each total **≥ the entry's pass bar, default 80**, with no blockers). A
  single `FAIL` fails the gate.
- On failure, the orchestrator has `writer`/`tailor` fix the reported blockers
  and re-runs both graders. Cap at **3 revision rounds**; if it still fails,
  stop and report the remaining blockers and scores to the owner rather than
  silently shipping a sub-threshold draft or loosening the bar.
- The graders are **read-only** and only score persuasiveness/credibility;
  they never override the no-fabrication rule or the `reviewer`'s fact findings.
  A high score never excuses an unresolved fabrication flag. An **honestly
  acknowledged** gap is a score penalty, not an auto-FAIL — the gate must never
  pressure a draft toward fabrication.

Tunable knobs: rubric weights and presets live in `screen-profiles.md`; the
default pass bar (80) and per-company `Pass bar:` overrides are set there and in
`target-companies.md`; the gate mode (AND / 3 rounds) lives in this section.
New companies get a `Screen profile:` proposed by `tailor` and approved by the
owner before it is written into the entry.

## Resume Engine (재조립 엔진: 브리프 → fast lane → 2-스톱)

**표준 시작점 = base 이력서 (edit-from-base).** New-company resume variants
start from the owner's standard résumé
`docs/resume-reference/base-resume.md` (전 섹션 확정된 base-theme 정본) and
its render template `outputs/base-resume.{html,css}`. The default flow is to
**copy base-resume.md and edit only its "가변" levers** to fit the JD (see the
base-resume.md header's "새 JD로 이력서 쓰는 법" + 편집 규칙), then render by
reusing the `base-resume.html/css` structure (DESIGN.md canonical
implementation). The reassembly machinery below —
`docs/resume-reference/canonical-lines.md` (owner-approved sentence bank) and
`docs/resume-reference/role-presets.md` (per-role presets + brief template) —
remains the **verification/promotion substrate**: new or changed prose is
checked against the bank, and confirmed new lines feed back into base-resume.md
and canonical-lines. The owner still reviews **two small artifacts** (a
targeting brief, then a new-prose diff) instead of full drafts.

### Flow (자동 모드, 2-스톱)

```
JD 수집 (tailor가 target-companies.md에 기록)
   ↓
① 타겟팅 브리프 선승인  ← role-presets.md 프리셋 + 예외 하이라이트
   ↓
초안 = base-resume.md 복제 → JD에 맞춰 "가변" 레버만 편집
   (갭만 신규 작문; canonical-lines.md는 검증·승격 기준)
   ↓
크리틱 (fast lane 축소 적용) → 수정 → 점수 게이트
   ↓
② diff 승인  ← 소유자는 companion 파일 전체를 리뷰
   (base 대비 변경분 + 신규 작문 + 신규 구조·목록 항목, 라벨 구분)
   ↓
designer 렌더 (base-resume.html/css 구조 재사용)
```

**인터뷰 모드**: 소유자가 요청하면 자동 진행 대신 JD 분석 후 섹션별로
질문을 주도하며 항목을 하나씩 확정해 쌓는다 (프리셋이 없는 직무군이거나
소유자가 세밀히 통제하고 싶을 때).

**갭 인터뷰 (두 모드 공통)**: JD 요건 중 canonical-lines/experience-bank에
근거가 없는 갭을 만나면 "무경험 — 제외"로 처리하기 전에 멈추고 소유자에게
질문한다. 답변은 user-attested로 `archivist`를 통해 experience-bank에
적재한다 — 다음 회사부터 같은 질문이 반복되지 않는다.

### Fast lane (재조립 변형 축소 검증)

A draft qualifies for the fast lane when it is built by reassembly: `approved`
canonical lines reused **verbatim** plus a bounded set of new content. The
producer (writer/tailor) must save a companion file
`outputs/<slug>-new-prose.md` with **three sections**: (a) every newly
written or modified prose sentence, (b) every `candidate`-status bank line
reused — candidate lines are owner-unapproved and get the same review as new
prose, and (c) every new or changed **non-prose content line** (skill-list
tokens, section headings, 직함·기간·인적사항 meta lines). The companion file
must be **updated on every revision** (critic fixes, gate-blocker fixes), not
just at first draft.

- `reviewer` (integrity check, **exhaustive, not sampled**): verify the
  partition invariant over every **content line** of the draft (prose,
  list item, heading, meta line) — each either (1) matches an `approved` bank
  line, or (2) appears in the companion file. The match unit is the full bank
  `line:` string (bullet-level; a multi-sentence bullet matches as a whole),
  after normalization: strip bullet markers/leading whitespace and unescape
  quoting. Sentence-level comparison applies only to text unmatched at bullet
  level. Any orphan line, any near-match (altered canonical line), or any
  `candidate` match not listed in section (b) is a must-fix finding and
  reverts that content to new-prose treatment.
- `reviewer` (fact check): full fact-check on the companion file's contents
  only. `approved` matches are exempt — **except time-sensitive claims**
  (연차·기간·"현재" 시점 수치), which must be rechecked against today's date
  even when byte-matched.
- `reviewer` (guideline/ledger/consistency/placeholder checks): run
  **draft-wide** even in fast lane — these are composition-level properties
  (emphasis order, cross-line date/metric agreement, MUST-rule audit) that a
  pure reassembly can still violate. Only the fact check narrows.
- `ats`: runs normally (keyword coverage is JD-wide, cheap).
- Score gate: **1 round**, which **counts as round 1 of P-01's 3-round cap**.
  On FAIL, fall back to the full lane — re-entering at the **critic stage with
  full reviewer scope** (not just re-scoring), with up to 2 further gate
  rounds.
- Adversarial verification pass: companion-file contents only, single pass,
  run **before** the score gate so accepted fixes are scored. (This is a
  sanctioned reduction of the CLAUDE.md hardening loop for the fast lane; the
  full lane keeps the full loop.)
- **Final integrity re-run**: after the last draft mutation (critic fixes,
  adversarial fixes, gate-blocker fixes), re-run the reviewer integrity check
  before stop ② — the partition invariant must hold on the version that
  ships, not just the first draft.

**Full lane** (기존 전체 파이프라인 그대로) applies when: a new base resume is
written, a **new EXP-NN entry** is added to `experience-bank.md` (a
gap-interview addition to an *existing* entry does not trigger full lane — its
sentences are new prose anyway), the draft's new-prose share exceeds ~50% of
content lines (reused `candidate` lines do **not** count toward this share —
they are already fully covered by companion review and stop ②), or the
fast-lane gate FAILs. The lane call at brief time is
**provisional**; re-check it once the draft exists and switch silently to full
lane if the conditions say so, reporting the switch at stop ②. When in doubt,
full lane.

**승격 루프**: a variant finalized through either lane feeds back — its new
prose is proposed for `canonical-lines.md` promotion (approval-gated,
proposed right after the render step), and its approved brief exceptions are
recorded in `target-companies.md` to strengthen the preset.

**기록 주체**: `canonical-lines.md` and `role-presets.md` are written only by
the **top-level orchestrator**, and only with owner approval for
status-bearing changes (line promotion/retirement, preset edits). Subagents —
including producers — never edit these two files; producers read them.

## Headhunter Advisor (포지셔닝 베이스 레이어)

`profile.md`/`experience-bank.md`(사실) 다음, `writer`/`tailor`가 초안을 쓰기
전에 참고하는 **회사-무관 포지셔닝 레이어**다. 매 회사 지원마다 도는
`resume-engine`과 달리, 한 번(또는 가끔) 깊게 쌓아두고 이후 모든 초안이
재사용한다 — `experience-bank.md`와 같은 1회성 구축 + 증분 갱신 패턴.
결과물은 `docs/resume-reference/positioning.md`.

### 페르소나 에이전트 (완전 몰입형, 개별 파일)

세 개의 read-only 서브에이전트가 서로 다른 헤드헌터 관점을 연기한다. 리서치
결과(원칙·말투·출처)는 각 에이전트 파일의 시스템 프롬프트에 **직접 박혀
있다** — 공용 참조 파일을 조회하는 방식이 아니다(소유자가 몰입감을 위해
선택). 리프레시하려면 해당 에이전트 파일을 직접 고친다(소유자 승인 필요).

| Agent | 관점 | 대표 소스 |
| --- | --- | --- |
| `headhunter-startup` | 스타트업/스케일업 테크 헤드헌터 — 임팩트·오너십·확장성 | SearcHRight 블로그 등 |
| `headhunter-searchfirm` | 정통 서치펌/대기업 인사출신 — 조직적합·커리어 서사·완성도 | 퇴사한 이형, 김나이 커리어 액셀러레이터 등 |
| `headhunter-techlead` | 실무형 엔지니어링 리더(CTO/테크리드) — 기술 깊이·문제해결·아키텍처 판단 | 개발바닥 유튜브, 빅테크 채용 기준 등 |

페르소나는 특정 인물의 1:1 재현이 아니라, 리서치한 여러 실존 소스를 종합한
**합성 아키타입**이다. 각 페르소나 파일의 리서치 근거 절은 인용 소스의
**공개 보도 내용**임을 명시하고, 실존 인물/채널에 대한 전기적 사실을
독립 검증 없이 단정하지 않는다.

`headhunter-techlead`만 `model: opus`(나머지 둘은 `sonnet`)인 이유:
`tech-screen`(opus)/`recruiter-screen`(sonnet) 선례와 동일하게, 기술적
트레이드오프 판단이 필요한 관점에만 더 무거운 모델을 쓴다.

### 흐름

1. **리서치 단계 (1회, 승인제)** — 소유자 지정 소스가 없으면 최상위
   에이전트가 web search로 IT 개발자 이직/헤드헌팅 분야 신뢰할 만한 소스를
   조사해 소유자에게 리스트를 보여주고 승인받은 뒤, 각 페르소나 에이전트
   파일에 직접 반영한다.
2. **인터뷰 단계 (매 실행)** — "grill-me 스타일"은 `grill-me` 스킬을 실제로
   호출한다는 뜻이 아니라, 그 스킬의 **한 번에 하나씩 묻고 답을 받은 뒤
   다음으로 넘어가는 진행 방식**만 차용한다는 뜻이다.
   a. 최상위 에이전트가 이번 라운드의 인터뷰 범위(어떤 `EXP-NN`/`전체·서사`가
      대상인지)를 먼저 확정한다 — 이 스코프가 **authoritative**하다. 3개
      페르소나 에이전트를 병렬 호출할 때 이 스코프를 명시적으로 전달한다.
      각 에이전트도 자체적으로 `positioning.md`를 다시 확인하지만, 이는
      안전망일 뿐 스코프 자체를 바꾸지 않는다. **증분 기준**: 대상 직무가
      이전 라운드와 같고 해당 `EXP-NN`에 이미 항목이 있으면 건너뛴다. 직무가
      다르면(예: 이전엔 백엔드, 이번엔 프론트엔드) 그 항목은 재인터뷰
      대상으로 포함하되 새 직무 관점의 `target_fit_notes`만 추가한다. 모든
      대상이 이미 커버돼 스코프가 비면, 에이전트를 호출하지 않고 그 사실을
      보고한 뒤 멈춘다.
   b. 각 에이전트는 `profile.md`·`experience-bank.md`·`positioning.md`(기존
      커버리지 확인용)·직무를 참고해 후보 질문 5-8개를 만들고, 스스로 "핵심
      포지셔닝을 바꿀 만한 질문인가"를 평가해 상위 3개로 압축한다.
   c. 최상위 에이전트가 3×3(최대 9개) 후보를 병합한다: 같은 `EXP-NN`을
      묻고 실질적으로 같은 정보를 캐묻는 질문끼리만 병합 대상이며, 병합 시
      더 구체적인 표현을 남기고 나머지 페르소나는 `source_persona`에
      추가한다. 목표는 6-9개이지 하한선은 아니다 — 억지로 채우지 않는다.
      병합 후 하나씩 순서대로 소유자에게 질문한다(어떤 페르소나가 왜
      궁금해하는지 표시).
   d. 답변마다 **사실**과 **포지셔닝/메타데이터**로 나눠 가공해 소유자에게
      다시 보여주고 write 승인을 받는다. 답변이 `experience-bank.md`에
      아직 없는 **완전히 새로운 경험**을 드러내면, 먼저 갭 인터뷰 방식대로
      `archivist`가 새 항목을 적재하고, 최상위 에이전트가 `canonical-lines.md`
      매핑에 새 `EXP-NN`을 추가 제안(승인제)한 뒤에만 그 경험을
      `positioning.md`에서 참조한다.
   e. Confirm 시: 새 사실은 기존 갭 인터뷰 방식대로 `archivist`를 통해
      `experience-bank.md`에 적재한다. 포지셔닝/메타데이터는 최상위
      에이전트가 직접 `positioning.md`에 기록한다.

### 파일 소유

`docs/resume-reference/positioning.md`는 `canonical-lines.md`/
`role-presets.md`와 같은 "기록 주체" 원칙을 따른다 — 서브에이전트가 아니라
**최상위 에이전트만** 승인받아 직접 쓴다. `EXP-NN` ID는 `canonical-lines.md`의
매핑을 그대로 재사용한다(새 경험이 추가되면 그 파일의 매핑을 먼저 갱신).
`experience-bank.md`에 `canonical-lines.md` 매핑이 아직 없는 항목을
만나면(archivist가 매핑 갱신보다 먼저 새 경험을 적재했을 수 있음), 그
항목은 인터뷰 대상에서 제외하고 매핑 추가를 소유자에게 먼저 제안한다.

`writer`/`tailor`는 `positioning.md`를 표준 참조 목록(아래 "Resume Reference
Material")에서 `experience-bank.md` 다음 순번으로 읽는다.

이 스킬(`.claude/skills/headhunter-advisor/`)이 절차를 운전한다.

## Portfolio Review Harness

Portfolio work is a first-class workflow, separate from the resume drafting
pipeline above. Use it when reviewing or improving portfolio HTML, PDF, image
assets, project case studies, or portfolio summaries.

The portfolio harness uses specialist subagents in `.claude/agents/`:

| Agent | Role | Owns / writes | Access |
| --- | --- | --- | --- |
| `portfolio-curator` | Inventory portfolio files and extract project claims | review inventory in `outputs/` | read-write |
| `portfolio-fact-checker` | Verify claims against the evidence base | -- (reports findings) | **read-only** |
| `portfolio-story-reviewer` | Critique recruiter-facing project narrative | -- (reports findings) | **read-only** |
| `portfolio-ux-reviewer` | Critique HTML/PDF layout, visual hierarchy, accessibility, print fit | -- (reports findings) | **read-only** |
| `portfolio-synthesizer` | Combine findings into prioritized feedback | final review report in `outputs/` | read-write |

Portfolio source files outside this repository are read-only inputs unless the
user explicitly asks to import or edit them. Record the path and file list in
`docs/portfolio-reference/source-materials.md` before review.

Portfolio agents must follow the same no-fabrication rule as resume agents: use
only verified facts from `docs/resume-reference/profile.md`,
`docs/resume-reference/experience-bank.md`, and
`docs/resume-reference/metric-registry.md`. Unsupported claims are findings, not
permission to rewrite history.

### Portfolio handoff playbook

```
portfolio-curator
   -> portfolio-fact-checker + portfolio-story-reviewer + portfolio-ux-reviewer
   -> portfolio-synthesizer
   -> Claude subagent hardening pass when the output is substantive
```

Default portfolio review reports go under `outputs/` using a dated name such as
`portfolio-review-YYYY-MM-DD.md`. Keep raw extracted claims, critique notes, and
final recommendations separate enough that a later agent can trace feedback back
to the source file and evidence record.

## Cloud / Mobile Sessions (claude.ai/code)

This project can be run from the Claude mobile app via Claude Code in the cloud
(`claude.ai/code`) against the standalone **private** GitHub repo. The cloud
sandbox clones the repo, so the subagents in `.claude/agents/` and the
project skills run there unchanged. The following rules apply **only** to cloud /
mobile sessions, where the local PC toolchain is absent:

- **Adversarial verification still runs.** The hardening pass is a Claude
  subagent (see `CLAUDE.md`), so it works unchanged in the cloud — no external
  model is required.
- **No beads.** The Dolt database lives under `refs/dolt/data` and does not
  follow the clone, so `bd` commands will not work. Do issue tracking on the PC.
- **Deliverables as Markdown.** Save drafts to `outputs/*.md` and show the full
  text in the chat. Print-ready PDF/HTML via the `designer` agent stays a
  PC-side step (it needs the local render toolchain).
- **Write back via branch / PR, never push to `main` directly.** Commit cloud
  work to a feature branch and open a PR; the PC syncs with `git pull` / merge.
- **Raw source binaries are absent by design.** `docs/resume-reference/sources/`
  (résumé PDF, salary / appraisal xlsx) is gitignored and will not be in the
  clone. Work from the derived `*.md` / `*.yaml`; do not attempt re-extraction
  from raw sources in the cloud.

## Resume Reference Material

Before drafting or editing a resume, cover letter, self-introduction, or
job-specific application document, read the reference files under
`docs/resume-reference/` in this order:

1. `README.md`
2. `ai-use-rules.md`
3. `ai-readable.yaml`
4. `metric-registry.md`
5. `profile.md`
6. `experience-bank.md`
7. `positioning.md`
8. `writing-guidelines.md`
9. `feedback-rules.md`
10. `canonical-lines.md`
11. `role-presets.md`
12. `target-companies.md`
13. `source-materials.md`
14. `source-log.md`

Also read `DESIGN.md` before creating visual or print-ready artifacts.
