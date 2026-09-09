#!/usr/bin/env /usr/bin/python3
"""geoyoung_content.py → md 초안 + companion(new-prose) 생성.

companion의 출처 태그는 자동 판정: 정규화한 문장이 GS글로벌 v7 초안 md 또는
코오롱베니트 v4 제출 docx 문면에 그대로 존재하면 `재사용`, 아니면 `신규/수정`.
"""
import os, re, sys, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import geoyoung_content as C

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DRAFT = os.path.join(REPO, 'outputs', 'geoyoung-ai-dev-resume-draft.md')
OUT_COMP = os.path.join(REPO, 'outputs', 'geoyoung-ai-dev-new-prose.md')

def norm(s):
    s = s.replace('**', '')
    s = re.sub(r'^[\s○▪■→\-–·•]+', '', s)
    s = re.sub(r'^\d+\.\s*', '', s)
    return re.sub(r'\s+', '', s)

# ---- 출처 코퍼스 ----------------------------------------------------------
corpus = {}
gs = open(os.path.join(REPO, 'outputs', 'gs-global-fde-full-resume-draft.md'), encoding='utf8').read()
for ln in gs.splitlines():
    if ln.strip():
        corpus.setdefault(norm(ln), set()).add('GS v7')
kz = zipfile.ZipFile(os.path.join(REPO, 'outputs', '코오롱베니트_플랫폼개발운영_정다훈_써치라인_v4.docx'))
kd = kz.read('word/document.xml').decode('utf8')
for m in re.finditer(r'<w:p[ >].*?</w:p>', kd, re.S):
    t = ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', m.group(0)))
    if t.strip():
        corpus.setdefault(norm(t), set()).add('코오롱 v4')

def origin(line):
    key = norm(line)
    if key in corpus:
        return '재사용(' + '·'.join(sorted(corpus[key])) + ')'
    # 부분 재사용: 코퍼스 문장을 구두점 단위로 쪼갠 절이 모두 들어 있으면 수정
    return '신규/수정'

# ---- 초안 md --------------------------------------------------------------
D, K = [], []   # draft lines, companion entries (section, line, origin)
def add(section, line, kind='prose'):
    D.append(line)
    if line.strip():
        K.append((section, line, origin(line), kind))

D.append(f'# 지오영 AI 개발 지원서 초안 — ㈜피플렙 지정양식 구조 (작성일 {C.TODAY})\n')
D.append('## 이 력 서\n')
D.append('### 기본사항\n')
D.append('| 항목 | 내용 |\n| --- | --- |')
for k, v in C.BASIC.items():
    add('기본사항', f'| {k} | {v} |', 'meta')
add('기본사항', '| 사진 | (증명사진 삽입 — outputs/assets/jungdahun-profile.jpg, 양식 사진 칸) |', 'meta'); D.append('')
D.append('### 학력사항\n')
D.append('| 기간 | 출신학교명 | 학과 | 평점/만점 | 소재지 |\n| --- | --- | --- | --- | --- |')
for r in C.EDU:
    if any(r): add('학력', '| ' + ' | '.join(r) + ' |', 'meta')
D.append('')
add('경력요약', f'### 경력요약(총 {C.TOTAL_CAREER})', 'meta'); D.append('')
D.append('| 기간 | 년월수 | 회사명 | 담당업무 | 이직사유(요약) |\n| --- | --- | --- | --- | --- |')
for r in C.CAREER_ROWS:
    if any(r): add('경력요약', '| ' + ' | '.join(r) + ' |', 'meta')
D.append(''); add('경력요약', C.CAREER_NOTE, 'meta')
D.append('\n### 핵심역량\n')
for head, bullets in C.CORE:
    add('핵심역량', head)
    for b in bullets: add('핵심역량', b)
    D.append('')
D.append('### 자격사항\n')
D.append('| 내용 | 취득일자 | 점수/수준/등급 | 발급기관 |\n| --- | --- | --- | --- |')
for r in C.CERTS: add('자격', '| ' + ' | '.join(r) + ' |', 'meta')
D.append('\n### 교육사항\n')
D.append('| 기간 | 내용 | 기관 |\n| --- | --- | --- |')
for r in C.TRAININGS:
    if any(r): add('교육', '| ' + ' | '.join(r) + ' |', 'meta')
D.append('\n### 기타사항(해외연수/특허/수상/봉사활동/동아리활동 등)\n')
D.append('| 날짜 | 내용 | 등급 | 기관 |\n| --- | --- | --- | --- |')
for r in C.ETC:
    if any(r): add('기타', '| ' + ' | '.join(r) + ' |', 'meta')
D.append('\n### 상세경력사항\n')
for blk in C.BLOCKS:
    add('상세경력', blk['header'], 'heading'); D.append('')
    add('상세경력', blk['intro'], 'meta')
    if blk.get('note'): add('상세경력', blk['note'], 'meta')
    D.append('')
    D.append('[주요업무]\n')
    for p in blk['projects']:
        add('상세경력', p['title'], 'heading')
        if p.get('period'): add('상세경력', p['period'], 'meta')
        for r in p['results']: add('상세경력', r)
        for e in p['execs']: add('상세경력', e)
        add('상세경력', p['tech'], 'meta'); D.append('')
    add('상세경력', blk['reason']); D.append('')
D.append('## 자기소개서\n')
for head, paras in C.SELF_INTRO.items():
    D.append(f'### {head}\n')
    for p in paras:
        add('자기소개서', p); D.append('')
add('자기소개서', C.SIGN, 'meta')
D.append(''); add('자기소개서', '위 사항은 사실과 다름이 없으며 만약 위 사실이 다를 경우 입사가 취소됨 (양식 원문 고정 문구)', 'meta'); D.append('')
D.append('---\n\n## 개인정보 수집·이용 동의서 (별도 docx)\n')
for k, v in C.CONSENT.items():
    add('동의서', f'- {k}: {v}', 'meta')
add('동의서', '- 동의함 체크박스: ☒ (동의) — 양식 체크박스 컨트롤 체크', 'meta')

open(OUT_DRAFT, 'w', encoding='utf8').write('\n'.join(D) + '\n')

# ---- companion --------------------------------------------------------------
L = ['# 지오영 AI 개발 지원서 — companion (new-prose)\n',
     '출처 태그 자동 판정: `재사용(...)` = GS글로벌 v7 초안 md / 코오롱베니트 v4 제출 docx 문면에 정규화 후 그대로 존재. '
     '`신규/수정` = 이번 세션 신규 작문 또는 기존 문장 수정. canonical-lines.md(2026-07-23 적재)에는 GS·코오롱 문장이 미등재이므로 '
     '재사용분도 무결성 검사 대상으로 본 파일에 전량 기재한다. 파일 제목(1행)·구획 헤딩(## …)·양식 고정 섹션 라벨(### 기본사항·학력사항·핵심역량·자격사항·교육사항·기타사항·상세경력사항·자소서 3항목 헤딩·[주요업무])·표 헤더 행은 제출 문면 외 스캐폴딩 또는 양식 원문으로 파티션 비대상이다.\n',
     '## (a) 신규 작문·수정 문장 (prose)\n']
for s, line, o, kind in K:
    if kind == 'prose' and o == '신규/수정':
        L.append(f'- [{s}] {line}')
L.append('\n## (a\') 재사용 prose (GS v7 / 코오롱 v4 제출 문면, 은행 미등재)\n')
for s, line, o, kind in K:
    if kind == 'prose' and o != '신규/수정':
        L.append(f'- [{s}] {line}  ← {o}')
L.append('\n## (b) candidate 은행 문장 재사용\n\n- 없음 (canonical-lines candidate 문장 미사용)\n')
L.append('\n## (c) 신규·변경 비산문 콘텐츠 라인 (표 셀·헤딩·메타·기술 줄)\n')
for s, line, o, kind in K:
    if kind != 'prose':
        L.append(f'- [{s}] {line}  ← {o}')
open(OUT_COMP, 'w', encoding='utf8').write('\n'.join(L) + '\n')
n_new = sum(1 for _, _, o, k in K if k == 'prose' and o == '신규/수정')
n_re = sum(1 for _, _, o, k in K if k == 'prose' and o != '신규/수정')
print(f'draft → {OUT_DRAFT}\ncompanion → {OUT_COMP}\nprose 신규/수정 {n_new} / 재사용 {n_re} / 비산문 {len(K)-n_new-n_re}')
