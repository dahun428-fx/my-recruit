# troubleshooting-harness

장애·에러 제보를 **단발성 답변이 아니라 표준 트러블슈팅 문서**로 전환하는 [Claude Code](https://claude.com/claude-code) 스킬입니다. "원인 분석해줘" 수준의 일회성 응답 대신, 매번 **같은 사고 흐름**을 강제해 재현·검증 가능한 팀 지식 자산으로 축적합니다.

## ✨ 무엇을 하나

장애 징후가 보이면 자동 발동해 아래 흐름을 끝까지 탑니다:

```
1. 트러블슈팅 대상 판단
2. 프로젝트 조사 (evidence-first, 기계적 탐색은 저사양 Explore로 위임)
3. 정보 부족 시 핵심만 되묻기 → 나머지는 ASSUMPTIONS로 명시하고 진행
4. 8섹션 산출물 생성 (5 필수 + 3 조건부)
5. docs/troubleshooting/YYYY-MM-DD-<slug>.md 로 저장
```

## 📋 산출물 (고정 8섹션)

**필수 5** — 증상요약 · 환경정보 · 원인후보 · 즉시확인명령어 · 해결절차
**조건부 3** — 재현조건 · 검증방법 · 재발방지 체크리스트

검증방법(7번)은 **문제 유형에 따라 자동 분기**합니다:

| 문제 유형 | 7. 검증 방법 |
|---|---|
| 코드·로직 버그 | **테스트 코드** (red → green) |
| 환경·빌드·배포·네트워크·권한 | **검증 명령어 / 재현 스크립트 / 체크리스트** |

> 테스트 코드를 모든 장애에 강제하지 않습니다. ADB 인식·signing error·포트 충돌·SSH 접속·경로 권한 등은 검증 명령어가 더 적합합니다.

## 🚀 사용법

별도 호출 없이, 장애성 표현이 보이면 자동으로 잡힙니다:

```
"Bioage Agent 리포트 다운로드가 안 돼"
"Metro가 8081 포트 충돌로 reload 안 돼"
"ADB에서 device가 안 잡혀"
"iOS 빌드가 signing 에러로 실패해"
```

- 산출물은 **항상 한국어** (코드·명령어·로그·경로는 원문 유지).
- 결과는 현재 프로젝트 `docs/troubleshooting/` 에 frontmatter(date·project·component·symptom·root_cause·tags·status·severity)와 함께 저장됩니다.
- 단순 정보성 질문("X가 뭐야?")에는 발동하지 않습니다.

## 📦 설치

```bash
cp -r troubleshooting-harness ~/.claude/skills/troubleshooting-harness
```

또는 마켓플레이스로 `dahun-personal` 플러그인 전체와 함께 설치됩니다.

자세한 동작·규칙은 [`SKILL.md`](./SKILL.md), 문서 골격은 [`templates/troubleshooting-doc.md`](./templates/troubleshooting-doc.md) 참고.
