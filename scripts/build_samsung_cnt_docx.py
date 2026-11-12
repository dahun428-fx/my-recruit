#!/usr/bin/env python3
"""삼성물산 건설부문 지정양식 docx에 초안 md 값을 주입한다.

원칙(F-09): 템플릿의 스타일·라벨·구성요소는 유지하고 값 칸만 채운다.
- 값 셀은 첫 문단의 pPr과 첫 런의 rPr을 복제해 텍스트만 교체한다.
- 지원직무 드롭다운(SDT)은 선택지 중 하나("AI서비스 개발")로 확정한다.
- 경력 상세 4번 블록·장학금 표는 손대지 않는다(빈 칸 유지).
실행: python3 scripts/build_samsung_cnt_docx.py <양식.docx> [출력접미사]
"""
import copy, os, re, sys
import docx
from docx.oxml.ns import qn

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRAFT = os.path.join(REPO, 'outputs', 'samsung-cnt-agentic-ai-resume-draft.md')
TPL = sys.argv[1]
SUFFIX = sys.argv[2] if len(sys.argv) > 2 else ''
OUT = os.path.join(REPO, 'outputs', f'삼성물산건설부문_AI서비스개발_정다훈_입사지원서{SUFFIX}.docx')

md = open(DRAFT, encoding='utf8').read()


# ---------- 초안 파싱 ----------
def section(title):
    m = re.search(rf'^## {re.escape(title)}\s*$(.*?)(?=^## |\Z)', md, re.S | re.M)
    assert m, title
    return m.group(1)


def table_rows(text):
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith('|') or re.match(r'^\|\s*-', line):
            continue
        rows.append([c.strip() for c in line.strip('|').split('|')])
    return rows[1:]  # 헤더 제외


kv = {r[0]: r[1] for r in table_rows(section('인적사항'))}
edu = table_rows(section('학력사항'))
career = table_rows(section('경력사항'))
qual = section('자격/어학/기타')
certs = table_rows(re.search(r'### 자격(.*?)###', qual, re.S).group(1))
langs = table_rows(re.search(r'### 외국어(.*?)###', qual, re.S).group(1))

detail = section('경력 상세')
blocks = []
for b in re.split(r'^### 블록 \d+\s*$', detail, flags=re.M)[1:]:
    if '(비움)' in b:
        continue
    g = lambda k: re.search(rf'^{k}:\s*(.*)$', b, re.M).group(1).strip()
    body = re.search(r'주요업무 및 성과\s*\n(.*?)\n전직사유:', b, re.S).group(1).strip('\n')
    note = re.search(r'^(※.*)$', b, re.M)
    lines = ([note.group(1), ''] if note else []) + body.splitlines()
    period = re.sub(r'\s*\(\d+년 \d+개월\)', '', g('근무 기간'))
    blocks.append(dict(name=g('회사명'), intro=g('회사 개요'), period=period,
                       body=lines, reason=g('전직사유')))
assert len(blocks) == 3, len(blocks)

vision = section('지원동기 및 입사 후 Vision')
vision = [p.strip() for p in vision.split('\n\n') if p.strip() and not p.strip().startswith('(글자수')]
assert sum(len(p) for p in vision) >= 500


# ---------- docx 조작 ----------
d = docx.Document(TPL)
T = d.tables


def set_cell(cell, text):
    """첫 문단 서식을 보존하며 셀 텍스트를 교체. text는 문자열 또는 줄 목록."""
    lines = text if isinstance(text, list) else [text]
    p0 = cell.paragraphs[0]
    ppr = p0._p.pPr
    r0 = p0.runs[0]._r if p0.runs else None
    rpr = copy.deepcopy(r0.rPr) if r0 is not None and r0.rPr is not None else None
    if rpr is None and ppr is not None and ppr.find(qn('w:rPr')) is not None:
        rpr = copy.deepcopy(ppr.find(qn('w:rPr')))
        rpr.tag = qn('w:rPr')
    for p in cell.paragraphs[1:]:
        p._p.getparent().remove(p._p)
    tpl_p = copy.deepcopy(p0._p)
    for child in list(tpl_p):
        if child.tag != qn('w:pPr'):
            tpl_p.remove(child)
    body_p = p0._p
    for child in list(body_p):
        if child.tag != qn('w:pPr'):
            body_p.remove(child)
    targets = [body_p]
    for _ in lines[1:]:
        np_ = copy.deepcopy(tpl_p)
        targets[-1].addnext(np_)
        targets.append(np_)
    for p_el, line in zip(targets, lines):
        for i, seg in enumerate(line.split('**')):
            if not seg:
                continue
            r = p_el.makeelement(qn('w:r'), {})
            if rpr is not None:
                rp = copy.deepcopy(rpr)
                for tag in ('w:b', 'w:bCs'):
                    for e in rp.findall(qn(tag)):
                        rp.remove(e)
                if i % 2 == 1:
                    rp.insert(1 if rp.find(qn('w:rFonts')) is not None else 0, rp.makeelement(qn('w:b'), {}))
                r.append(rp)
            t = r.makeelement(qn('w:t'), {qn('xml:space'): 'preserve'})
            t.text = seg
            r.append(t)
            p_el.append(r)


def left_align(cell):
    for p in cell.paragraphs:
        ppr = p._p.get_or_add_pPr()
        jc = ppr.find(qn('w:jc'))
        if jc is None:
            jc = ppr.makeelement(qn('w:jc'), {})
            ppr.append(jc)
        jc.set(qn('w:val'), 'left')


# 인적사항
t = T[2]
set_cell(t.rows[0].cells[2], kv['성명'])
set_cell(t.rows[1].cells[2], kv['영문 성명'])
set_cell(t.rows[1].cells[4], kv['생년월일'])
set_cell(t.rows[2].cells[2], kv['E-mail'])
set_cell(t.rows[2].cells[4], kv['휴대폰'])
set_cell(t.rows[3].cells[2], kv['주소'])

# 지원직무 드롭다운
sdt = d.element.body.find('.//' + qn('w:sdt'))
opts = [e.get(qn('w:displayText')) for e in sdt.iter(qn('w:listItem'))]
assert kv['지원직무'] in opts, (kv['지원직무'], opts)
pr = sdt.find(qn('w:sdtPr'))
ph = pr.find(qn('w:showingPlcHdr'))
if ph is not None:
    pr.remove(ph)
ts = list(sdt.find(qn('w:sdtContent')).iter(qn('w:t')))
ts[0].text = kv['지원직무']
for x in ts[1:]:
    x.text = ''
for rs in sdt.find(qn('w:sdtContent')).iter(qn('w:rStyle')):
    rs.getparent().remove(rs)

# 학력
for ri, row in ((1, edu[0]), (2, edu[1])):
    cells = T[3].rows[ri].cells
    for ci, val in zip(range(2, 8), row[1:7]):
        set_cell(cells[ci], val)

# 경력사항 표
for ri, row in enumerate(career, start=1):
    cells = T[4].rows[ri].cells
    period = row[0].replace(' ~ ', ' ~ ')
    for ci, val in zip(range(1, 7), [period] + row[1:6]):
        set_cell(cells[ci], val)

# 자격 / 어학 / 병역
t = T[5]
for ri, c in enumerate(certs, start=1):
    cells = t.rows[ri].cells
    set_cell(cells[1], c[0]); set_cell(cells[2], c[1]); set_cell(cells[3], c[2])
for ri, l in enumerate(langs, start=1):
    cells = t.rows[ri].cells
    set_cell(cells[4], l[0]); set_cell(cells[5], l[1]); set_cell(cells[6], l[2]); set_cell(cells[7], l[3])
set_cell(t.rows[0].cells[9], '필')
set_cell(t.rows[2].cells[9], 'N')
set_cell(t.rows[3].cells[9], 'N')

# 경력 상세 블록 1~3 (블록 4는 비움)
for b, tb in zip(blocks, T[6:9]):
    set_cell(tb.rows[0].cells[2], b['name'])
    set_cell(tb.rows[1].cells[2], b['intro'])
    set_cell(tb.rows[2].cells[2], b['period'])
    body = [ln for ln in b['body']]
    # 프로젝트 제목 줄(번호.) 볼드
    body = [f'**{ln}**' if re.match(r'^\d+\. ', ln) else ln for ln in body]
    # 프로젝트 사이 빈 줄 유지, 연속 빈 줄 축약
    out = []
    for ln in body:
        if ln == '' and (not out or out[-1] == ''):
            continue
        out.append(ln)
    set_cell(tb.rows[3].cells[2], out)
    left_align(tb.rows[3].cells[2])
    set_cell(tb.rows[4].cells[2], b['reason'])
    left_align(tb.rows[4].cells[2])

# 지원동기
vc = T[11].rows[1].cells[0]
set_cell(vc, vision)
left_align(vc)


# 동의·확인 문단
def rewrite_para(p, new_text):
    runs = p.runs
    runs[0].text = new_text
    for r in runs[1:]:
        r._r.getparent().remove(r._r)


hits = 0
for p in d.paragraphs:
    if '(예, 아니오)' in p.text:
        # 마지막 '(' 런부터 교체: 빨간 '(예, 아니오)' 런 유지하며 텍스트만 변경
        rs = p.runs
        idx = max(i for i, r in enumerate(rs) if '(' in r.text)
        rs[idx].text = '(■예, □아니오)'
        for r in rs[idx + 1:]:
            r._r.getparent().remove(r._r)
        hits += 1
    elif re.search(r'20\s+년\s+월\s+일', p.text):
        lead = re.match(r'\s*', p.text).group(0)
        rewrite_para(p, f'{lead}2026년 11월 12일           위 본인 지원자 성 명   {kv["성명"]}                 (인 또는 서명)')
        hits += 1
assert hits == 5, hits  # 동의 2 + 사실확인 1 + 날짜 2

d.save(OUT)
print(OUT)
