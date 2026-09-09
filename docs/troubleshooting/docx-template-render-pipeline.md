# docx 지정양식 렌더·검증 파이프라인 트러블슈팅

지정양식(회사·서치펌 템플릿) docx를 XML 수술로 채우고 Word로 PDF 검증하는
파이프라인에서 반복 발생한 장애 모음. 출처: 2026-08-25 코오롱베니트
써치라인 v2~v4 세션 (macOS + Microsoft Word + python3 표준 라이브러리).

공통 원칙: **템플릿 zip을 베이스로 복사하고 `word/document.xml`(+ 필요한
rels·media)만 교체한다.** 지원 파일(styles·numbering·settings·header·footer)
은 템플릿 원본을 그대로 쓴다 — F-09(지정양식 무변형)의 구현 측면.

---

## 1. Homebrew python의 expat 깨짐 (ElementTree 사용 불가)

- **재현 조건**: `/opt/homebrew/bin/python3`(3.14 계열)에서 `xml.etree` 사용
  시 `ImportError: Symbol not found: _XML_SetAllocTrackerActivationThreshold`.
- **확인 명령어**: `python3 -c "from xml.etree import ElementTree"` 실패 여부.
- **검증 방법**: `/usr/bin/python3 -c "from xml.etree import ElementTree"` 성공.
- **해결 절차**: docx XML 작업은 **`/usr/bin/python3`(시스템 파이썬)** 으로
  실행한다.
- **재발 방지**: 렌더 스크립트 실행 커맨드에 `/usr/bin/python3`를 명시한다.

## 2. Word AppleScript PDF 변환 플래키

- **재현 조건**: `osascript`로 Word에 open→save as PDF 지시. 세 가지 실패
  양상 — (a) `active document doesn't understand "save as"`,
  (b) `document 1 = missing value`(문서 카운트 0), (c) **이전 시도에서 열려
  있던 다른 문서가 대신 내보내져 엉뚱한 PDF가 생성**(파일 크기가 직전
  변환물과 동일하면 의심).
- **확인 명령어**: 변환 후 PDF 페이지 수
  `python3 -c "import re;print(len(re.findall(rb'/Type\\s*/Page[^s]', open('out.pdf','rb').read())))"`
  와 파일 크기를 직전 산출물과 비교. 내용 검증은 Read(PDF)로 1페이지 육안 확인.
- **검증 방법**: 페이지 수·1페이지 내용이 기대와 일치.
- **해결 절차**: 변환 전 `pkill -9 -x "Microsoft Word"; sleep 3`로 완전
  종료 → `open file name <경로>` + 문서 카운트 폴링(0.5s×40) 후
  `save as document 1` → 종료. 실패 시 강제 종료 후 1회 재시도.
- **재발 방지**: "Word 완전 종료 → 변환 → 종료"를 한 단위로 묶은 스크립트
  (`scripts/render_kolon_benit_searchline.py` 주석의 convert5.applescript
  패턴)만 사용. 변환 직후 페이지 수 검증을 파이프라인에 포함.

## 3. Word가 문서를 열지 못함 (빈 표 셀)

- **재현 조건**: XML 수술로 표 셀(`<w:tc>`) 안의 마지막 문단을 삭제해 셀이
  문단 없이 남으면, XML은 well-formed여도 Word가 열지 못함(§2-(b)로 표면화).
- **확인 명령어**: `ET.fromstring`은 통과하는데 Word open만 실패하면 구조
  위반 의심. 삭제 diff에서 `<w:tc>` 직후가 `</w:tc>`인 곳 검색.
- **검증 방법**: 수정 후 Word 변환 성공.
- **해결 절차**: 문단 삭제 시 대상이 셀 내부인지 확인하고, 셀 안 마지막
  문단은 절대 삭제하지 않는다(빈 `<w:p/>`라도 유지).
- **재발 방지**: "빈 문단 정리"류 수술은 반드시 표 범위(`</w:tbl>` 이후)로
  한정해 매칭한다.

## 4. 푸터 총페이지(NUMPAGES) 캐시 불일치

- **재현 조건**: 템플릿 푸터의 `PAGE/NUMPAGES` 필드는 마지막 저장 시점
  값을 캐시함 — 본문 페이지 수가 바뀌면 "12/11"처럼 어긋나 보임(빈 템플릿
  자체도 "5/4"). 과거 출고본은 NUMPAGES를 리터럴로 하드코딩해 리플로우에
  취약했음.
- **확인 명령어**: 렌더 PDF 마지막 페이지 푸터 표기 vs 실제 페이지 수 비교.
- **검증 방법**: Word에서 문서를 열면 필드가 갱신되어 일치.
- **해결 절차**: 필드를 리터럴로 바꾸지 말 것. `settings.xml`의
  `<w:zoom .../>` 앞에 `<w:updateFields w:val="true"/>`를 넣어 열 때 자동
  갱신되게 한다.
- **재발 방지**: 제출 전 Word로 한 번 열어 저장(필드 갱신 확정). 검증용
  자동 변환 PDF의 푸터 숫자는 캐시일 수 있음을 감안하고 페이지 수는 PDF
  실측으로 판정.

## 5. 텍스트 검색 실패 — run 분절과 태그 변형

- **재현 조건**: (a) 같은 문장이 여러 `<w:t>` run으로 쪼개져
  `doc.find('[ 핵심역량 ]')`류 문자열 검색이 -1을 반환 → `find(x)+6` 같은
  후속 산술이 **문서 맨 앞을 오염**시키는 대형 사고로 이어짐.
  (b) 렌더러가 만든 문단은 `<w:p>`(무속성)라 `rfind('<w:p ', ...)`(공백
  포함)가 건너뜀. (c) 본문이 sdt(content control) 안에 있으면 단순 문단
  순회 덤프에서 통째로 누락.
- **확인 명령어**: 앵커 검색 결과가 -1이 아닌지 assert. 수술 후
  `ET.fromstring` + 문서 선두 120자 육안 확인.
- **검증 방법**: 문단 텍스트 조인 기반 탐색이 앵커를 찾고, 수술 후 파싱
  통과 + 렌더 확인.
- **해결 절차**: 원시 `str.find` 대신 **문단 단위로 `<w:t>`를 이어 붙여
  키를 찾는 `find_para(doc, key)` 헬퍼**를 쓴다. 문단 시작 탐색은
  `max(rfind('<w:p '), rfind('<w:p>'))`. 모든 앵커에 assert를 걸어 -1
  산술을 차단한다.
- **재발 방지**: 수술 스크립트마다 (1) 앵커 assert, (2) `ET.fromstring`
  파싱 검증, (3) 수술 전후 `<w:t>` 텍스트 시퀀스 difflib 대조(의도한 변경만
  존재하는지)를 표준 3종 검증으로 실행한다.

## 6. 서식 속성의 스키마 순서·상속 함정

- **재현 조건**: (a) `<w:pPr>`에 `keepNext/keepLines/pageBreakBefore`를
  넣을 때 `pStyle`보다 앞에 두면 Word가 무시할 수 있음. (b) 표 행
  `cantSplit`은 행 분할을 막아 페이지 하단에 큰 공백을 만듦. (c) 셀 폭은
  `tcW`(dxa)로 고정 — 좁은 셀(예: 595dxa≈1cm)에 전화번호를 넣으면 숫자
  중간 절단.
- **확인 명령어**: 렌더 PDF에서 고아줄·반쪽 페이지·셀 내 절단 육안 확인.
- **검증 방법**: 수정 후 렌더에서 해소 확인.
- **해결 절차**: keep류는 `pStyle` 바로 뒤에 삽입. 긴 콘텐츠 행은
  `cantSplit` 제거로 자연 분할(GS v7 흐름). 좁은 셀은 폭을 바꾸지 말고
  (세로 괘선 정렬 붕괴) 내용을 줄이거나 축소 글씨·의도적 개행으로 처리.
- **재발 방지**: 고아줄 방지는 pageBreakBefore(반쪽 페이지 유발)보다
  블록 keepNext 체인을 우선 검토.

## 7. 소유자 Word 세션이 열려 있을 때 AppleScript `open`이 무한 대기 (2026-09-09 지오영 세션)

- **재현 조건**: 소유자가 Word로 다른 문서를 편집 중(문서 카운트 ≥1)인 상태에서
  `open file name`을 보내면 `AppleEvent timed out (-1712)`. 갓 만든 출력물뿐
  아니라 **검증된 기존 제출본(코오롱 v4)도 동일하게 실패**하므로 파일 결함이
  아니라 Word 세션 상태 문제다. `count of documents` 같은 조회 이벤트는 정상
  응답한다(모달이 아닌 "열기 큐 점유" 양상). §2의 `pkill -9 -x "Microsoft Word"`
  선행은 소유자 미저장 작업을 날릴 수 있어 **사용 금지**.
- **확인 명령어**: `osascript -e 'with timeout of 8 seconds
  tell application "Microsoft Word" to (count of documents) & name of document 1
  end timeout'` — 소유자 문서명이 나오면 이 케이스.
- **검증 방법**: 소유자 문서가 닫힌 뒤(또는 Word 재시작 후) 같은 스크립트가
  정상 변환되면 확정.
- **해결 절차**: 자동 변환을 보류하고 (1) `unzip -t` + 전 XML 파트
  `ET.fromstring` 파싱 + 텍스트 시퀀스 diff로 구조·문면을 기계 검증한 뒤
  (2) 소유자에게 "Word의 다른 문서를 닫은 뒤 docx를 직접 열어 확인" 또는
  변환 재시도 시점을 알린다. `settings.xml`의 `updateFields`는 푸터에
  NUMPAGES가 없으면 넣지 않는다(열 때 "필드 업데이트" 모달 유발 가능 —
  이번 양식은 PAGE 필드만 있어 제거).
- **재발 방지**: 변환 스크립트 첫 단계에 "Word 문서 카운트 > 0이면 변환
  건너뛰고 보고" 가드를 둔다. AppleScript는 항상 `with timeout of N seconds`로
  감싸 세션을 붙잡지 않게 한다.

---

## 표준 검증 루틴 (수술 1회마다)

1. 빌드 스크립트의 앵커 assert 전부 통과
2. `/usr/bin/python3` + `ET.fromstring` 파싱 통과
3. 수술 전후 텍스트 시퀀스 difflib 대조 — 승인된 변경만 존재
4. Word 완전 종료 → PDF 변환 → 페이지 수 실측 + 변경 페이지 육안 확인
5. (제출 전) Word에서 열어 저장 — 필드 갱신 확정
