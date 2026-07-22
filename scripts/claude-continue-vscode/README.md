# Claude Continue by PID

VS Code 분할 터미널의 shell PID를 찾아 `계속해`를 한 번 전송합니다.

## 설치

VS Code에서 `Ctrl+Shift+P` → `Developer: Install Extension from Location...`을 선택하고
이 폴더를 지정합니다. 설치 후 VS Code를 다시 로드합니다.

## 실행

PowerShell에서:

```powershell
.\scripts\schedule-claude-continue.ps1 `
  -Pids 22228,13108 `
  -At "2026-07-22 23:00:00"
```

스크립트는 지정 시각까지 대기한 뒤 한 번만 요청을 보내고 종료합니다.
