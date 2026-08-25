#!/usr/bin/env /usr/bin/python3
"""코오롱베니트 써치라인 v4 재조립 스크립트 (2026-08-25 세션 영속화본).

- 베이스: outputs/코오롱베니트_플랫폼개발운영_정다훈_써치라인_v2.docx
  (템플릿 충실 v2 — 써치라인 원본 템플릿에 F-09 무변형 원칙으로 값만 채운 판)
- 출력: outputs/..._써치라인_v4.docx (F-10 포맷 세트 + 소유자 개고 자소서)
- 함정·검증 루틴: docs/troubleshooting/docx-template-render-pipeline.md 참조
  (expat/시스템 파이썬, run 분절 find_para, Word 변환 플래키, NUMPAGES 캐시)
- PDF 검증 변환(AppleScript, Word 완전 종료 후 실행):
    tell application "Microsoft Word"
      activate
      open file name <입력 경로>
      repeat 40 times / if (count of documents) > 0 then exit repeat / delay 0.5
      save as document 1 file name <출력 경로> file format format PDF
      close every document saving no
    end tell
"""

import re, zipfile, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(REPO, 'outputs', '코오롱베니트_플랫폼개발운영_정다훈_써치라인_v2.docx')
OUT = os.path.join(REPO, 'outputs', '코오롱베니트_플랫폼개발운영_정다훈_써치라인_v4.docx')

src = zipfile.ZipFile(BASE)
doc = src.read('word/document.xml').decode('utf-8')

RPR_N = '<w:rPr><w:rFonts w:ascii="맑은 고딕" w:hAnsi="맑은 고딕" w:eastAsia="맑은 고딕"/><w:b w:val="0"/><w:i w:val="0"/><w:sz w:val="19"/></w:rPr>'
RPR_B = '<w:rPr><w:rFonts w:ascii="맑은 고딕" w:hAnsi="맑은 고딕" w:eastAsia="맑은 고딕"/><w:b/><w:i w:val="0"/><w:sz w:val="19"/></w:rPr>'

PPR_INTRO = '<w:pPr><w:spacing w:after="40" w:line="259" w:lineRule="auto"/><w:ind w:right="340"/></w:pPr>'
PPR_HEAD = '<w:pPr><w:keepNext/><w:spacing w:after="40" w:before="160" w:line="259" w:lineRule="auto"/><w:ind w:right="340"/></w:pPr>'
PPR_BULLET = '<w:pPr><w:spacing w:after="40" w:line="259" w:lineRule="auto"/><w:ind w:right="340" w:left="240" w:hanging="127"/></w:pPr>'
PPR_CELL_BULLET = '<w:pPr><w:spacing w:after="20" w:before="20" w:line="259" w:lineRule="auto"/><w:ind w:left="240" w:hanging="240"/></w:pPr>'
PPR_PROSE = '<w:pPr><w:spacing w:after="120" w:before="40" w:line="259" w:lineRule="auto"/><w:ind w:right="340"/></w:pPr>'
PPR_SUBHEAD = '<w:pPr><w:keepNext/><w:spacing w:after="40" w:before="120" w:line="259" w:lineRule="auto"/><w:ind w:right="340"/></w:pPr>'

def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def md_para(ppr, text):
    """'**볼드**' 마커를 볼드 런으로 파싱해 문단 XML 생성."""
    runs = ''
    for i, seg in enumerate(text.split('**')):
        if not seg:
            continue
        rpr = RPR_B if i % 2 == 1 else RPR_N
        runs += f'<w:r>{rpr}<w:t xml:space="preserve">{esc(seg)}</w:t></w:r>'
    return f'<w:p>{ppr}{runs}</w:p>'

def find_para(d, key, start=0):
    for m in re.finditer(r'<w:p[ >].*?</w:p>', d[start:], re.S):
        txt = ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', m.group(0)))
        if key in txt:
            return start + m.start(), start + m.end()
    raise AssertionError(f'문단을 찾지 못함: {key}')

# ---- 1. 핵심역량 --------------------------------------------------------
INTRO = ('React·TypeScript 프론트엔드부터 Java·Spring Boot·MySQL·Node.js 서버까지 '
         '서비스 전 구간을 개발하고 직접 배포·운영해 온 Full-stack Product Engineer입니다.')
CORE = [
    ('▪ React·TypeScript 기반 서비스 개발·운영', [
        '- 비즈36.5·AI코치·바이오에이지 3개 서비스 프론트엔드 총괄',
        '- 신규 기능을 데이터 모델·API부터 화면까지 End-to-End 개발',
        '- AI 챗봇을 10주 만에 구축해 실서비스 전환, **임직원 3,493명 규모 운영**',
        '- 푸시·인증 토큰·딥링크 네이티브 브릿지 연동, RN 앱 스토어 출시·운영',
    ]),
    ('▪ Java·Spring Boot와 DB 설계·개발 End-to-End', [
        '- 신규 기능 3건 MySQL 모델부터 서버·API·Web/Admin 화면까지 직접 개발',
        '- 레거시 스키마 무변경 신규 테이블 추가 : PK·FK·조회 인덱스 직접 설계',
        '- 삼성물산 프로젝트에서 렌더링·DB 양단 튜닝으로 대용량 화면 **2.5초 → 1초대 단축**',
    ]),
    ('▪ Node.js 서버 개발과 Electron 데스크톱 유지보수', [
        '- 여러 백엔드를 집계·중계하는 Node.js API 계층 신규 구축 주도',
        '- 모놀리식 백엔드–프론트엔드 분리 전략으로 RESTful 구조 점진 도입',
        '- 바이오에이지 Electron 데스크톱 클라이언트 유지보수',
    ]),
    ('▪ AI Tool·API 활용', [
        '- 사내용 MCP 서버 2종 개발·수정, Codex·Claude Code 연동 환경 구성',
        '- LLM 응답 회귀 평가·UI E2E 도구 직접 제작으로 AI 산출물 검증 자동화',
        '- 프론트엔드 AI 활용 개발 표준 사내 공식 문서 채택, **10명 팀 전원 정착**',
    ]),
    ('▪ 검증 자동화와 운영 안정성', [
        '- 발화·LLM 응답·빌드·배포 검증 통합, E2E 5종 배포 필수 게이트 편입',
        '- Jenkins 파이프라인 전환으로 배포 리드타임 **10분 → 2분(약 80%)**, Docker Blue-Green 무중단 배포 운영',
        '- 오류 4유형 복구 전략과 GA4·PostHog 대시보드로 운영 지표 확인',
        '- iOS WebView 호환성 오류를 원인 추적·수정, E2E 회귀·실기기 체크리스트로 재발 방지',
    ]),
]
_hs, h_end = find_para(doc, '[ 핵심역량 ]')
_ks, _ = find_para(doc, '[ 경력사항 ]', start=h_end)
new_core = md_para(PPR_INTRO, INTRO)
for head, bullets in CORE:
    new_core += md_para(PPR_HEAD, '**' + head + '**')
    new_core += ''.join(md_para(PPR_BULLET, b) for b in bullets)
doc = doc[:h_end] + new_core + doc[_ks:]
print('1. 핵심역량 OK')

# ---- 2. 회사 개요 2곳 ---------------------------------------------------
o1s, o1e = find_para(doc, '[회사 개요]')
doc = doc[:o1s] + md_para(PPR_INTRO, '**[회사 개요]** 제약 · 매출 약 1조 5,709억 원(2025 연결 기준) · 임직원 약 2,000명') + doc[o1e:]
o2s, o2e = find_para(doc, '[회사 개요]', start=o1s + 200)
doc = doc[:o2s] + md_para(PPR_INTRO, '**[회사 개요]** IT 서비스(SI·SM) · 매출 약 290억 원(2024년 기준) · 직원 약 100명') + doc[o2e:]
print('2. 회사 개요 OK')

# ---- 3. 재직 기간 2곳 삭제 ----------------------------------------------
for _ in range(2):
    ps, pe = find_para(doc, '[재직 기간]')
    doc = doc[:ps] + doc[pe:]
print('3. 재직 기간 삭제 OK')

# ---- 4. 개괄(다나아) 라벨 불릿 ------------------------------------------
p1s, _ = find_para(doc, 'AI추진팀 다나아데이터 스쿼드')
tbl = doc.find('<w:tbl', p1s)
assert 0 < p1s < tbl
WORK_DANAA = [
    '- 담당 : 비즈36.5·AI코치·바이오에이지 3개 서비스 프론트엔드 총괄(2026.06 계열사 조직 이관 후 동일 서비스·업무 연속), 신규 기능을 데이터 모델·API부터 화면까지 End-to-End 개발, 바이오에이지 Electron 데스크톱 클라이언트 유지보수',
    '- 운영 : 비즈36.5(앱 사용자 약 4,000명) RN 앱의 스토어 심사 대응·버전 관리·크래시 모니터링, 운영팀·고객사 문의와 GA4·PostHog 지표·배포 검증·헬스체크로 관측, iOS WebView 호환성 오류를 원인 추적·수정하고 E2E 회귀·실기기 체크리스트로 재발 방지',
    '- 인프라·AI : AWS S3·EC2 빌드·배포 파이프라인 운영, 팀 AI 활용 개발 방식 전환 리드',
]
doc = doc[:p1s] + ''.join(md_para(PPR_BULLET, b) for b in WORK_DANAA) + doc[tbl:]
print('4. 개괄(다나아) OK')

# ---- 5. 개괄(내담) 라벨 불릿 --------------------------------------------
n1s, _ = find_para(doc, 'SI사업부 소속으로 고객사에 파견')
tbl2 = doc.find('<w:tbl', n1s)
assert 0 < n1s < tbl2
WORK_NAEDAM = [
    '- 담당 : SI사업부 소속으로 고객사 파견, 웹·모바일 프론트엔드와 서버·데이터 연동 수행',
    '- 주요 프로젝트 : 삼성물산 데이터 플랫폼·모바일 서비스와 한국미스미 글로벌 B2B 커머스, 두 곳 모두 레거시 성능·구조 개선과 신규 기능 개발 병행',
]
doc = doc[:n1s] + ''.join(md_para(PPR_BULLET, b) for b in WORK_NAEDAM) + doc[tbl2:]
print('5. 개괄(내담) OK')

# ---- 6. 주요 실행 5셀 (':' 구분자 + 볼드) --------------------------------
EXEC = [
    [  # ◆1
     '- 검증 체계 자동화 : 발화·LLM 응답·빌드·배포 검증을 자동 실행 체계로 통합, **E2E 5종을 배포 필수 게이트로 편입**',
     '- LLM 응답 회귀 평가 도구 직접 제작 : 엑셀 질문 자동 입력, **스크린샷·JSON·HTML 갤러리로 비개발 직군도 판정 참여**',
     '- UI E2E 테스트 도구 직접 제작 : JSON 시나리오 자동 조작, **기준 화면 대비 시각 차이 2%(기본값) 판정**',
     '- 프론트엔드 AI 활용 개발 표준 설계 주도 : 컨텍스트 관리·금지 패턴·보안·검증 절차 표준화, **사내 공식 문서 채택**',
     '- 사내용 MCP 서버 2종 직접 개발·수정 : Codex·Claude Code에 연동해 **AI 에이전트가 사내 도구를 호출하는 환경 구성**',
     '- GA4·PostHog 운영 데이터 대시보드 구축 : 지표 기반 개선 과제 도출, **진입·이탈 과제는 실행까지 완료**',
     '- 3개 서비스 공통 컴포넌트 레이어 운영 : **변경 이유가 같은 UI만 공통 승격**, 회귀는 타입·빌드 검사·Playwright E2E·수동 확인으로 방지',
     '- Storybook 스토리 210개로 재사용 컴포넌트 카탈로그화 : **신규 화면 조립을 공통 컴포넌트 기반으로 전환**',
     '- 기획·운영팀 요구사항·화면설계서 작성 가이드 교육 : 작성 기준·템플릿 수립·배포',
     '- 지식 자산화 : 외부 컨퍼런스 인사이트를 **사내 개발 세미나 12회·기술 문서 48건**으로 축적',
    ],
    [  # ◆2
     '- 레거시 구조 분석 : Controller·Service·Query·DB 전 구간과 테이블 참조 관계를 추적해 **변경 영향 범위 파악**',
     '- React 화면 단위 점진 전환 구조 직접 설계 : 전면 재작성의 일정·회귀 리스크와 jQuery 공존 비용을 저울질해 채택, **변경·장애 빈도 기준으로 전환 순서 결정**',
     '- 공존 비용 관리 : 이중 상태 관리·공통 CSS와 React 스타일 충돌 격리·공존 기간 유지비를 감수하며 전환 기간 운영',
     '- 풀스택 End-to-End 개발 : 신규 기능의 **MySQL 모델·Spring Boot 로직·MyBatis 쿼리·REST API·Web/Admin 화면 직접 개발**',
     '- 테이블 설계 : 운영 중 레거시 스키마를 변경하지 않고 신규 테이블을 참조 관계로 연결(조인 증가·정합성의 앱 계층 보증 감수), **사용자 ID+기록일 복합 인덱스와 PK·FK 직접 설계**',
     '- 트랜잭션 경계 : 다중 테이블 쓰기 기능은 **서비스 계층 트랜잭션으로 묶어 원자성 확보**',
     '- API 통합 계층 신규 구축 : 비동기 I/O와 프론트–백엔드 TypeScript 통일을 위해 Node.js 선택, **구조 설계·주요 엔드포인트 구현 주도**, 하위 호출 타임아웃과 실패 시 오류 응답 처리',
     '- BFF·서버 책임 분리 : **응답 조합·화면 맞춤 가공·권한 확인은 BFF**, 비즈니스 로직·데이터 소유는 Spring Boot에 유지, 운영·배포 대상 증가와 응답 모델 이중 관리는 감수',
     '- 웹·네이티브 브릿지 직접 설계·구현 : WebView 인터페이스와 RN 네이티브 모듈 브릿지로 **카메라·파일·푸시 토큰·로그인/인증 토큰·딥링크 연동**',
     '- 권한·정책 공통화 : 역할·리소스 매핑과 **라우트 가드·서버 검증 이중화**로 Web·Admin·App 정책 통일',
     '- 회귀 검증 자동화 : **82개 화면 전환을 Playwright E2E로 검증**',
     '- 배포 자동화 : FileZilla 수동 이관을 Jenkins 파이프라인으로 전환, 운영 서버는 **Docker Blue-Green 무중단 배포로 헬스체크 후 전환·이상 시 이전 컨테이너 롤백**',
    ],
    [  # ◆3
     '- 현업 요구를 제품 설계 문제로 재정의 : 기능별 차등 과금 요구를 **하나의 서비스로 여러 상품을 운영하는 문제로 정의**',
     '- Base-Theme·Config-Driven UI 전환 : **운영 담당자가 설정값으로 테마·기능·상품 구성**, 테넌트별 관리자 프리뷰 도구 개발',
     '- 아키텍처 전제 선합의 : 기획자와 MVP 범위, **AI 개발자와 응답 형식·스트리밍·오류 정책을 먼저 합의**',
     '- AI 채팅 경험 구현 : **SSE 실시간 스트리밍**, 중지·재시도·재생성, Markdown 표·차트·링크 렌더링 계층 설계',
     '- 오류 복구 전략 적용 : XSS 필터링과 **오류 4유형 분류로 404/500과 LLM 응답 오류까지 복구**',
     '- 도메인 12개 모듈·다국어 구현 : Python 프롬프트·LLM 응답 변환 수정 참여, VectorDB·RAG 구현·활용 과정 참여',
    ],
    [  # ◆4
     '- 추정 대신 구간 분리 측정 : API 응답과 화면 노출 시점을 나눠 **병목을 클라이언트 렌더링 구간으로 특정**',
     '- 렌더링 최적화 : 렌더링 생명주기 분리·Lazy Rendering, **FlatList 가상화와 재렌더링 제거** 적용',
     '- 사용자 행동 단위 API 호출 설계 : debounce·동일 조건 캐시·중복 요청 취소, **클라이언트 필터링과 서버 검색 경계 정의**',
     '- 백엔드 응답 경량화 : Spring REST API 필터링·정렬 설계와 SQL 튜닝, **Oracle DB 인덱싱과 DTO 투영**',
    ],
    [  # ◆5
     '- 한국 웹 전환 리드 : 한국 팀 React 최숙련 개발자로 **6인 팀 마이그레이션을 완료까지 견인**',
     '- 일본 본사 개발자와 크로스보더 협업 : **일본어로 직접 소통**하며 전 지사 아키텍처 통일의 한국 파트 수행',
     '- 렌더링 경계 판단 : 상품·검색 유입은 SSR, 로그인 후 상호작용은 CSR, **페이지별 렌더링 비용을 기준으로 경계 직접 판단**',
     '- 성능·글로벌 요구 대응 : **code splitting·next/image·prefetch 최적화**, i18next 영·중·일 다국어와 SEO 대응',
     '- 관측성·배포 자동화 : Lighthouse·GA·Adobe Analytics·Datadog 지표화, Vercel 배포 자동화',
    ],
]
pos = 0
for n, bullets in enumerate(EXEC, 1):
    lab, _ = find_para(doc, '[주요 실행]', start=pos)
    lab_tc_end = doc.find('</w:tc>', lab) + 7
    val_tc_s = doc.find('<w:tc>', lab_tc_end)
    val_tc_e = doc.find('</w:tc>', val_tc_s) + 7
    cell = doc[val_tc_s:val_tc_e]
    body_s = cell.find('</w:tcPr>') + 9
    new_cell = cell[:body_s] + ''.join(md_para(PPR_CELL_BULLET, b) for b in bullets) + '</w:tc>'
    doc = doc[:val_tc_s] + new_cell + doc[val_tc_e:]
    pos = val_tc_s + len(new_cell)
    print(f'6. 주요 실행 ◆{n} OK ({len(bullets)}불릿)')

# ---- 7. 자기소개서 (소유자 개고안, QA 지표 명칭 통일) --------------------
COVER = [
    ('React·Java·DB를 연결해 서비스 운영까지 책임집니다', [
        '비즈36.5에서는 jQuery·Thymeleaf·Spring Boot·MySQL 기반 레거시를 분석하고, 기존 서비스를 중단하지 않으면서 React 화면 단위로 점진 전환하는 구조를 설계했습니다. 신규 기능 3건은 **MySQL 데이터 구조부터 Spring Boot 서버·REST API·React 화면까지 직접 개발**하며 기능 단위의 End-to-End 개발을 수행했습니다.',
        '여러 백엔드의 데이터를 연결하기 위한 **Node.js 집계·중계 API 계층을 신규 구축**했고, 수동 배포는 Jenkins 파이프라인으로 전환해 **배포 시간을 10분에서 2분으로 단축**했습니다. 운영 환경에는 Docker Blue-Green 방식을 적용해 서비스 중단 없이 배포할 수 있도록 구성했습니다.',
        '삼성물산 프로젝트에서도 화면만 최적화하는 데 그치지 않고 렌더링 구조와 SQL·인덱스를 함께 개선해 **대용량 화면 응답을 2.5초에서 1초대로, 모바일 검색을 5초에서 1초로 단축**했습니다. 프론트엔드부터 서버·DB·배포까지 연결해 문제를 해결하는 것이 제 강점입니다.',
    ]),
    ('개발과 운영의 품질을 반복 가능한 기준으로 만듭니다', [
        '대웅제약에서 AI 코딩 에이전트가 도입된 이후 팀원마다 활용 방식과 결과물 검증 수준에 차이가 발생했습니다. 이를 개인의 숙련도 문제가 아니라 개발 프로세스의 문제로 보고, 컨텍스트 관리·금지 패턴·보안·검증 절차를 정리한 **프론트엔드 AI 활용 개발 표준을 설계했습니다.**',
        '해당 기준은 사내 공식 문서로 채택됐고, 개발 세미나 12회와 기술 문서 48건을 통해 **10명 팀 전원이 동일한 기준으로 활용할 수 있도록 정착**시켰습니다.',
        '반복 QA에 많은 시간이 소요되던 문제도 사람이 더 꼼꼼하게 확인하는 방식이 아니라 자동화로 해결했습니다. **LLM 응답 및 UI 회귀평가 도구를 직접 개발해 반복 QA 시간을 3시간에서 30분으로 단축**했습니다. 개발 속도뿐 아니라 작업 지침, 검증 기준, 운영 안정성까지 함께 관리하는 것을 중요하게 생각합니다.',
    ]),
    ('AI 서비스를 실제 사용 가능한 제품으로 전환했습니다', [
        'AI 건강검진 챗봇에서는 기획자와 함께 MVP 범위를 정의하고 **10주 만에 서비스를 구축해 임직원 3,493명이 사용하는 실서비스로 전환**했습니다. AI 개발자와 응답 데이터 형식, SSE 스트리밍 방식, 오류 정책을 사전에 정의하고 재시도·오류 복구 구조까지 구현해 실제 운영 환경에서 사용할 수 있도록 했습니다.',
        '최근에는 **사내용 MCP 서버를 직접 개발해 Codex·Claude Code와 연결하고, AI 에이전트가 내부 문서와 검증 도구를 사용할 수 있는 환경을 구성**했습니다. 새로운 기술은 단순히 적용하는 데 그치지 않고, 실제 업무에 사용할 수 있는 수준으로 검증하고 팀의 개발 방식에 연결해 왔습니다.',
    ]),
    ('구축 경험을 넘어, 지속적으로 개선되는 플랫폼을 만들고 싶습니다', [
        'SI 프로젝트에서는 다양한 고객 시스템을 구축했고, 이후에는 직접 만든 서비스를 운영하며 성능·품질·배포 방식을 지속적으로 개선해 왔습니다. 이 과정에서 새로운 서비스를 만드는 것만큼이나 **사용자가 매일 사용하는 시스템을 안정적으로 운영하고 작은 개선을 반복하는 일이 중요하다는 것을 경험했습니다.**',
        '코오롱베니트 플랫폼 개발/운영 직무는 사내 메신저와 커뮤니케이션 플랫폼, PC·모바일 서비스를 직접 개발하고 지속적으로 운영하는 역할입니다. 저는 React 화면 개발뿐 아니라 Java·Spring Boot 서버, MySQL·Oracle 데이터, Node.js API 계층, CI/CD와 운영 환경까지 실무에서 다뤄 왔습니다.',
        '입사 후에는 먼저 기존 플랫폼의 코드와 데이터 흐름, 운영 구조를 빠르게 파악하겠습니다. 이후 작은 개선부터 충분한 검증과 함께 배포하며 운영 안정성을 높이고, 장기적으로는 **레거시 점진 전환·E2E 검증 자동화·무중단 배포 경험을 팀이 반복해서 활용할 수 있는 개발·운영 기준으로 축적하겠습니다.**',
    ]),
]
_cs, c_head_end = find_para(doc, '[ 자기소개서 ]')
_ds, _ = find_para(doc, '입사지원용', start=c_head_end)
new_cover = ''
for sub, paras in COVER:
    new_cover += md_para(PPR_SUBHEAD, '**' + sub + '**')
    new_cover += ''.join(md_para(PPR_PROSE, p) for p in paras)
doc = doc[:c_head_end] + new_cover + doc[_ds:]
print('7. 자기소개서 OK')

# ---- 8. 연봉: 현재 기본 5,500 -------------------------------------------
occ = [m.start() for m in re.finditer(re.escape('5,700 (만원)'), doc)]
assert len(occ) == 2
doc = doc[:occ[0]] + doc[occ[0]:occ[0]+30].replace('5,700', '5,500', 1) + doc[occ[0]+30:]
assert doc.count('5,500 (만원)') == 1
print('8. 기본연봉 5,500 OK')

# ---- 9. 9주 단독 전환 기제 병기 -----------------------------------------
_ps, _pe = find_para(doc, '9주 내 단독')
_mech = f'<w:r>{RPR_N}<w:t>(컴포넌트 재사용 구조 기반 화면 조립)</w:t></w:r>'
doc = doc[:_pe-6] + _mech + doc[_pe-6:]
print('9. 9주 기제 OK')

# ---- 조립 ---------------------------------------------------------------
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for item in src.infolist():
        data = src.read(item.filename)
        if item.filename == 'word/document.xml':
            data = doc.encode('utf-8')
        z.writestr(item, data)
src.close()
print('output:', OUT)
