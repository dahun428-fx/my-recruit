#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-
"""보배써치 표준이력서 docx에 GS네오텍 초안 md(outputs/gs-neotek-fullstack-resume-draft.md) 값을 주입.

원칙(F-09·docs/troubleshooting/docx-template-render-pipeline.md):
- 템플릿 zip을 베이스로 복사하고 word/document.xml(+사진 media·rels·content type)만 교체.
- 템플릿 본문을 최상위 요소(문단·표) 단위로 쪼개 인덱스로 다룬다. 인덱스마다 앵커 텍스트를 assert.
- 섹션 제목·구분선(drawing)·서식은 유지하고, 지원자용 작성 안내(마젠타 FF00FF 런)만 제거(소유자 결정 2026-09-13).
  단 7번 문단 "**하기에 기술한 내용은…" 고지 문구는 양식 고정 문구라 유지.
- ET 파싱 검증, 자리표시자 잔존 검사, 텍스트 시퀀스 diff 출력.
실행: /usr/bin/python3 scripts/build_gs_neotek_docx.py <템플릿.docx> [출력접미사]
"""
import os, re, sys, zipfile, difflib
from xml.etree import ElementTree as ET

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = sys.argv[1]
SUFFIX = sys.argv[2] if len(sys.argv) > 2 else ''
MD = os.path.join(REPO, 'outputs', 'gs-neotek-fullstack-resume-draft.md')
OUT = os.path.join(REPO, 'outputs', f'정다훈(만35세)_플랫폼개발_GS네오텍_보배써치2026{SUFFIX}.docx')
PHOTO = os.path.join(REPO, 'outputs', 'assets', 'jungdahun-profile.jpg')

# ---------------------------------------------------------------------------
# md 파싱
# ---------------------------------------------------------------------------
md = open(MD, encoding='utf-8').read()

def section(title):
    m = re.search(r'^## ' + re.escape(title) + r'[^\n]*\n(.*?)(?=^## |\Z)', md, re.S | re.M)
    assert m, title
    return m.group(1)

def bullets(block):
    return [l[2:].strip() for l in block.splitlines() if l.startswith('- ')]

PERSONAL = dict(l.split(' : ', 1) for l in bullets(section('개 인 정 보')))
CORE = bullets(section('핵 심 역 량'))
EDU = bullets(section('학 력 사 항'))
career_heading = re.search(r'^## 경 력 사 항 \(총 경력: ([^)]+)\)', md, re.M).group(1)
CAREER = section('경 력 사 항')
PROJ = section('주 요 project 내역')
ETC = bullets(section('기 타 사 항'))
SAL = bullets(section('연봉 사항 및 입사 시기'))
MOVE = section('이직 및 지원 사유')
SI = section('자기 소개서')

# ---------------------------------------------------------------------------
# XML 헬퍼
# ---------------------------------------------------------------------------
def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def ttext(x):
    return ''.join(re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>', x))

def top_items(body):
    out, stack, start = [], [], 0
    for t in re.finditer(r'<(/?)w:(p|tbl)\b[^>]*?(/?)>', body):
        close, tag, selfc = t.group(1), t.group(2), t.group(3)
        if selfc:
            if not stack:
                out.append(body[t.start():t.end()])
            continue
        if not close:
            if not stack:
                start = t.start()
            stack.append(tag)
        else:
            stack.pop()
            if not stack:
                out.append(body[start:t.end()])
    return out

def ppr_of(p):
    m = re.search(r'<w:pPr>.*?</w:pPr>', p, re.S)
    return m.group(0) if m else ''

def runs_of(p):
    return re.findall(r'<w:r[ >](?:(?!</w:r>).)*?</w:r>', p, re.S)

def text_rpr(p):
    """텍스트가 있는 첫 런의 rPr(색상 제거)."""
    for r in runs_of(p):
        if '<w:t' in r and 'AlternateContent' not in r:
            m = re.search(r'<w:rPr>.*?</w:rPr>', r, re.S)
            rp = m.group(0) if m else '<w:rPr></w:rPr>'
            return re.sub(r'<w:color w:val="[0-9A-Fa-f]+"/>', '', rp)
    return '<w:rPr><w:rFonts w:ascii="맑은 고딕" w:eastAsia="맑은 고딕" w:hAnsi="맑은 고딕" w:cs="Tahoma"/><w:sz w:val="22"/></w:rPr>'

def set_bold(rpr, on):
    rpr = re.sub(r'<w:b/>|<w:bCs/>', '', rpr)
    if on:
        rpr = rpr.replace('<w:rPr>', '<w:rPr><w:b/><w:bCs/>', 1)
    return rpr

def set_underline(rpr, on):
    rpr = re.sub(r'<w:u w:val="[a-z]+"/>|<w:shd [^>]*/>', '', rpr)
    if on:
        rpr = rpr.replace('</w:rPr>', '<w:u w:val="single"/></w:rPr>')
    return rpr

def mk_runs(text, rpr, bold_base=False):
    out = ''
    for i, seg in enumerate(text.split('**')):
        if not seg:
            continue
        out += f'<w:r>{set_bold(rpr, bold_base or i % 2 == 1)}<w:t xml:space="preserve">{esc(seg)}</w:t></w:r>'
    return out

def mk_para(ppr, text, rpr, bold_base=False):
    return f'<w:p>{ppr}{mk_runs(text, rpr, bold_base)}</w:p>'

def strip_magenta(p):
    for r in runs_of(p):
        if 'w:val="FF00FF"' in r:
            p = p.replace(r, '', 1)
    return p

def replace_text_keep_drawing(p, text, rpr, bold_base=False):
    """drawing(구분선) 런과 그 뒤 br 런은 유지, 텍스트 런만 교체."""
    keep = ''
    for r in runs_of(p):
        if 'AlternateContent' in r or ('<w:br/>' in r and '<w:t' not in r):
            keep += r
    return f'<w:p>{ppr_of(p)}{keep}{mk_runs(text, rpr, bold_base)}</w:p>'

def keep_next(p):
    if '<w:keepNext/>' in p:
        return p
    if '<w:pPr>' in p:
        return p.replace('<w:pPr>', '<w:pPr><w:keepNext/>', 1)
    return re.sub(r'^(<w:p\b[^>]*>)', r'\1<w:pPr><w:keepNext/></w:pPr>', p, count=1)

def heading_set(p, new_head_text):
    """제목 문단: 마젠타 안내 제거 후, 굵은 제목 텍스트 런들을 새 텍스트 1런으로."""
    p = strip_magenta(p)
    rs = [r for r in runs_of(p) if '<w:t' in r and 'AlternateContent' not in r]
    rpr = re.search(r'<w:rPr>.*?</w:rPr>', rs[0], re.S).group(0)
    keep = ''.join(r for r in runs_of(p) if 'AlternateContent' in r)
    return f'<w:p>{ppr_of(p)}{keep}<w:r>{rpr}<w:t xml:space="preserve">{esc(new_head_text)}</w:t></w:r></w:p>'

# ---------------------------------------------------------------------------
# 템플릿 로드
# ---------------------------------------------------------------------------
src = zipfile.ZipFile(TPL)
doc = src.read('word/document.xml').decode('utf-8')
b0 = doc.find('<w:body>') + len('<w:body>')
b1 = doc.rfind('</w:body>')
body = doc[b0:b1]
sect = body[body.rfind('<w:sectPr'):]
body_wo = body[:body.rfind('<w:sectPr')]
T = top_items(body_wo)
before = [ttext(x) for x in T]

def A(i, key):
    assert key in ttext(T[i]), (i, key, ttext(T[i])[:60])
    return T[i]

# 앵커 검증
for i, k in [(0, '사진'), (2, '홍 길 동'), (7, '하기에 기술한'), (9, '개 인 정 보'), (10, '생년월일'), (11, '성별'),
             (12, '주소'), (13, '연락처'), (16, '핵심 역량'), (17, 'OOOO 수립'), (18, 'OOOO 발굴'), (22, '학 력 사 항'),
             (23, '경영대학원'), (24, '경영학과 졸업'), (25, '고등학교'), (28, '경 력 사 항'), (30, 'AA'), (33, '팀장(차장)'),
             (35, '연/중장기'), (36, '예상 재무제표'), (69, '주요 project'), (71, 'M&amp;A'), (76, '기 타 사 항'),
             (78, '병역'), (79, '영어구사능력'), (80, '연수/교육'), (81, '포상'), (82, '자격사항'), (83, '보훈여부'),
             (84, 'PC활용능력'), (87, '연봉 사항'), (89, '현재연봉'), (90, '희망연봉'), (91, '입사시기'),
             (94, '이직 및 지원 사유'), (95, '퇴직 사유'), (96, 'BB산업'), (97, '중장기적'), (100, '지원 사유'),
             (103, '자기 소개서'), (104, '업무 스타일'), (105, '- '), (108, '업무적 측면'), (112, '성격 및 대인관계')]:
    A(i, k)
assert T[118].startswith('<w:tbl')

new = []

# ---- 0. 사진 --------------------------------------------------------------------
CX, CY = 1128000, 1496000   # 사진 사각형(1371600×1590675 EMU) 안쪽, 원본 245×325 비율
pic = (f'<w:r><w:rPr><w:noProof/></w:rPr><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
       f'<wp:extent cx="{CX}" cy="{CY}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
       f'<wp:docPr id="901" name="증명사진"/><wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
       f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
       f'<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr><pic:cNvPr id="901" name="jungdahun-profile.jpg"/><pic:cNvPicPr/></pic:nvPicPr>'
       f'<pic:blipFill><a:blip r:embed="rIdPhoto901"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
       f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{CX}" cy="{CY}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
       f'</a:graphicData></a:graphic></wp:inline></w:drawing></w:r>')
p0 = T[0]
choice = re.search(r'<mc:Choice.*?</mc:Choice>', p0, re.S).group(0)
tx_p = re.search(r'<w:txbxContent>(.*?)</w:txbxContent>', choice, re.S).group(1)
tx_ppr = ppr_of(tx_p)
choice_new = choice.replace(tx_p, f'<w:p>{tx_ppr}{pic}</w:p>', 1)
p0 = p0.replace(choice, choice_new, 1)
# VML 대체(fallback)의 "사진" 글자는 비움(Word 2010+는 Choice 사용)
fb = re.search(r'<mc:Fallback>.*?</mc:Fallback>', p0, re.S).group(0)
p0 = p0.replace(fb, re.sub(r'<w:t>사진</w:t>', '<w:t></w:t>', fb), 1)
assert ttext(p0).strip() == ''
new.append(p0)
new.append(T[1])

# ---- 2. 성명·추천 포지션 (텍스트박스 Choice/Fallback 모두) ----------------------------
p2 = T[2]
def fix_txbx_para(m):
    p = m.group(0)
    t = ttext(p)
    if '홍 길 동' in t:
        return f'<w:p>{ppr_of(p)}<w:r>{text_rpr(p)}<w:t xml:space="preserve">정 다 훈</w:t></w:r></w:p>'
    if '추천 포지션' in t:
        return f'<w:p>{ppr_of(p)}<w:r>{text_rpr(p)}<w:t xml:space="preserve">추천 포지션: 플랫폼개발(풀스택)</w:t></w:r></w:p>'
    return p
def fix_txbx(m):
    return '<w:txbxContent>' + re.sub(r'<w:p[ >](?:(?!</w:p>).)*?</w:p>', fix_txbx_para, m.group(1), flags=re.S) + '</w:txbxContent>'
p2 = re.sub(r'<w:txbxContent>(.*?)</w:txbxContent>', fix_txbx, p2, flags=re.S)
assert '홍 길 동' not in p2 and 'OOOOO' not in p2
new.append(p2)
new.extend(T[3:10])

# ---- 10~13. 개인정보 --------------------------------------------------------------
y, mo, dd = PERSONAL['생년월일'].split('.')
vals = [f'생년월일 : {y}년 {mo}월 {dd}일', f'성별 : {PERSONAL["성별"]}', f'주소 : {PERSONAL["주소"]}']
email, phone = [s.strip() for s in PERSONAL['연락처'].split('/')]
vals.append(f'연락처 : {email} / (핸드폰) {phone}')
for i, v in zip(range(10, 14), vals):
    new.append(mk_para(ppr_of(T[i]), v, text_rpr(T[i])))
new.extend(T[14:16])

# ---- 16~20. 핵심 역량 ----------------------------------------------------------------
new.append(strip_magenta(T[16]))
brpr = text_rpr(T[18])
def core_line(c):
    if ' : ' in c:
        lab, rest = c.split(' : ', 1)
        return f'- **{lab}** : {rest}'
    return f'- **{c}**'
new.append(replace_text_keep_drawing(T[17], core_line(CORE[0]), brpr))
for c in CORE[1:]:
    new.append(mk_para(ppr_of(T[18]), core_line(c), brpr))
new.append(T[21])

# ---- 22~25. 학력 --------------------------------------------------------------------
new.append(strip_magenta(T[22]))
new.append(replace_text_keep_drawing(T[23], EDU[0], text_rpr(T[24])))
for e in EDU[1:]:
    new.append(mk_para(ppr_of(T[24]), e, text_rpr(T[24])))
new.extend(T[26:28])

# ---- 28~66. 경력사항 --------------------------------------------------------------------
new.append(heading_set(T[28], f'경 력 사 항 (총 경력: {career_heading})'))
new.append(T[29])
CO_PPR, CO_RPR = ppr_of(T[30]), text_rpr(T[30])
POS_PPR, POS_RPR = ppr_of(T[33]), text_rpr(T[33])
CAT_PPR = ppr_of(T[35])
CAT_RPR = set_underline(set_bold(text_rpr(T[35]), True), True)
DASH_PPR, DASH_RPR = ppr_of(T[36]), text_rpr(T[36])
BLANK = T[40]
NOTE_RPR = set_bold(text_rpr(T[36]), False).replace('</w:rPr>', '<w:color w:val="595959"/><w:sz w:val="20"/></w:rPr>')
NOTE_RPR = re.sub(r'<w:sz w:val="22"/>', '', NOTE_RPR, count=1)

def company_para(line):
    head, rest = line.split('): ', 1)
    head += ')'
    ul = set_underline(set_bold(CO_RPR, True), True)
    return (f'<w:p>{CO_PPR}<w:r>{ul}<w:t xml:space="preserve">{esc(head)}</w:t></w:r>'
            f'<w:r>{CO_RPR}<w:br/></w:r><w:r>{set_underline(set_bold(CO_RPR, False), False)}<w:t xml:space="preserve">: {esc(rest)}</w:t></w:r></w:p>')

first_company = True
for raw in CAREER.strip().splitlines():
    line = raw.strip()
    if not line:
        continue
    if re.match(r'^\S.+\(\d{4}년 \d+월 ~ .+\): ', line):
        if not first_company:
            new.append(BLANK)
        first_company = False
        new.append(company_para(line))
    elif re.match(r'^(팀원|대리) / ', line):
        new.append(mk_para(POS_PPR, line, POS_RPR))
    elif line.startswith('※'):
        new.append(mk_para(DASH_PPR, line, NOTE_RPR))
    elif line.startswith('[') and line.endswith(']'):
        new.append(BLANK)
        new.append(mk_para(ppr_of(T[33]).replace('<w:numPr><w:ilvl w:val="1"/><w:numId w:val="37"/></w:numPr>', ''),
                           line.strip('[]'), set_bold(POS_RPR, True)))
    elif line.startswith('▪'):
        new.append(BLANK)
        new.append(mk_para(CAT_PPR, line.lstrip('▪ ').strip(), CAT_RPR))
    elif line.startswith('- '):
        new.append(mk_para(DASH_PPR, line, DASH_RPR))
    else:
        raise AssertionError('경력 줄 미분류: ' + line)
new.extend(T[67:69])

# ---- 69~73. 주요 project 내역 ---------------------------------------------------------
new.append(strip_magenta(T[69]))
new.append(T[70])
PJ_PPR, PJ_RPR = ppr_of(T[71]), text_rpr(T[71])
SUB_PPR = PJ_PPR.replace('<w:wordWrap/>', '<w:wordWrap/>', 1).replace('<w:jc w:val="left"/>', '<w:ind w:left="440" w:hanging="220"/><w:jc w:val="left"/>', 1)
TECH_RPR = PJ_RPR.replace('</w:rPr>', '<w:color w:val="595959"/></w:rPr>')
first_pj = True
for raw in PROJ.strip().splitlines():
    if not raw.strip():
        continue
    if raw.startswith('- '):
        if not first_pj:
            new.append(T[74])
        first_pj = False
        new.append(mk_para(PJ_PPR, '- ' + raw[2:].strip(), PJ_RPR, bold_base=True))
    elif raw.startswith('  - '):
        t = raw[4:].strip()
        if t.startswith('기술:'):
            new.append(mk_para(SUB_PPR, '· ' + t, TECH_RPR))
        else:
            lab, rest = t.split(' : ', 1)
            new.append(mk_para(SUB_PPR, f'· **{lab}** : {rest}', PJ_RPR))
    else:
        raise AssertionError('project 줄 미분류: ' + raw)
new.extend(T[74:76])

# ---- 76~84. 기타사항 --------------------------------------------------------------------
new.append(strip_magenta(T[76]))
new.append(T[77])
ETC_PPR, ETC_RPR = ppr_of(T[78]), text_rpr(T[78])
for e in ETC:
    new.append(mk_para(ETC_PPR, e, ETC_RPR))
new.extend(T[85:87])

# ---- 87~91. 연봉 ------------------------------------------------------------------------
new.append(strip_magenta(T[87]))
new.append(T[88])
for i, s in zip((89, 90, 91), SAL):
    new.append(mk_para(ppr_of(T[i]), s, text_rpr(T[i])))
new.extend(T[92:94])

# ---- 94~101. 이직 및 지원 사유 -------------------------------------------------------------
new.append(strip_magenta(T[94]))
new.append(strip_magenta(T[95]))
reasons = [l.strip() for l in re.search(r'### 퇴직 사유\n(.*?)### 지원 사유', MOVE, re.S).group(1).splitlines() if re.match(r'^\d\. ', l.strip())]
support = re.search(r'### 지원 사유\n(.*)', MOVE, re.S).group(1).strip()
for r in reasons:
    head, rest = r.split(' : ', 1)
    new.append(mk_para(ppr_of(T[96]), head, text_rpr(T[96]), bold_base=True))
    new.append(mk_para(ppr_of(T[97]), '- ' + rest, text_rpr(T[97])))
new.append(T[99])
new.append(strip_magenta(T[100]))
new.append(mk_para(ppr_of(T[105]).replace('<w:ind w:firstLineChars="100" w:firstLine="220"/>', ''), support, text_rpr(T[105])))
new.extend(T[101:103])

# ---- 103~117. 자기소개서 -----------------------------------------------------------------
new.append(strip_magenta(T[103]))
SUBH_PPR, SUBH_RPR = ppr_of(T[104]), text_rpr(T[104])
BODY_PPR = ppr_of(T[105]).replace('<w:ind w:firstLineChars="100" w:firstLine="220"/>',
                                   '<w:spacing w:after="80"/>' if False else '')
BODY_PPR = BODY_PPR.replace('<w:spacing w:line="0" w:lineRule="atLeast"/>', '<w:spacing w:after="100" w:line="0" w:lineRule="atLeast"/>')
BODY_RPR = text_rpr(T[105])
first_h = True
for raw in SI.strip().splitlines():
    line = raw.strip()
    if not line:
        continue
    if line.startswith('### '):
        if not first_h:
            new.append(T[107])
        first_h = False
        new.append(mk_para(SUBH_PPR, line[4:], SUBH_RPR, bold_base=True))
    elif re.match(r'^\*\*.+\*\*$', line):
        new.append(mk_para(SUBH_PPR, line.strip('*'), SUBH_RPR, bold_base=True))
    else:
        new.append(mk_para(BODY_PPR, line, BODY_RPR))
new.extend(T[115:])

# ---------------------------------------------------------------------------
# 조립·검증
# ---------------------------------------------------------------------------
HEAD_KEYS = ('핵심 역량', '학 력 사 항', '경 력 사 항', '주요 project', '기 타 사 항', '연봉 사항', '이직 및 지원 사유', '자기 소개서', '퇴직 사유', '지원 사유')
for i in range(len(new)):
    t = ttext(new[i]).strip()
    is_head = any(t.startswith(k) for k in HEAD_KEYS)
    is_line_only = (t == '' and 'AlternateContent' in new[i])
    is_sub = t.startswith('[') or re.match(r'^\d\. ', t) or (t.startswith('- ') and '<w:b/>' in new[i][:600] and ('(대웅제약' in t or 'SI 프로젝트,' in t or '(대웅제약·' in t))
    is_company = bool(re.match(r'^\S.+\(\d{4}년 \d+월 ~ ', t))
    if is_head or is_line_only or is_sub or is_company:
        new[i] = keep_next(new[i])
out_doc = doc[:b0] + ''.join(new) + sect + doc[b1:]
assert 'xmlns:wp=' in out_doc[:4000] and 'xmlns:r=' in out_doc[:4000] and 'xmlns:pic' not in out_doc[:0]
try:
    ET.fromstring(out_doc.encode('utf-8'))
except ET.ParseError as e:
    ln, col = e.position
    print('PARSE ERROR context:', out_doc.split('\n')[ln - 1][max(0, col - 400):col + 100])
    raise
alltext = ttext(out_doc)
for bad in ['홍 길 동', 'OOOO', 'AA전자', 'BB Korea', 'hong@naver', '1900년', '기재 요망', '(참고)', 'M&amp;A', '6,500만원', 'HRD후보', '확인 필요']:
    assert bad not in out_doc, '자리표시자/안내 잔존: ' + bad
after = [ttext(x) for x in top_items(out_doc[out_doc.find('<w:body>') + 8:out_doc.rfind('<w:sectPr')])]
diff = [l for l in difflib.unified_diff(before, after, lineterm='', n=0) if l[:1] in '+-' and l[:3] not in ('+++', '---')]
open(os.path.join(REPO, 'outputs', 'gs-neotek-docx-textdiff.txt'), 'w', encoding='utf-8').write('\n'.join(diff))

rels = src.read('word/_rels/document.xml.rels').decode('utf-8')
rels = rels.replace('</Relationships>', '<Relationship Id="rIdPhoto901" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/jungdahun-profile.jpg"/></Relationships>')
ct = src.read('[Content_Types].xml').decode('utf-8')
if 'Extension="jpg"' not in ct and 'Extension="jpeg"' not in ct:
    ct = ct.replace('<Default Extension=', '<Default Extension="jpg" ContentType="image/jpeg"/><Default Extension=', 1)
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for item in src.infolist():
        data = src.read(item.filename)
        if item.filename == 'word/document.xml':
            data = out_doc.encode('utf-8')
        elif item.filename == 'word/_rels/document.xml.rels':
            data = rels.encode('utf-8')
        elif item.filename == '[Content_Types].xml':
            data = ct.encode('utf-8')
        z.writestr(item, data)
    z.write(PHOTO, 'word/media/jungdahun-profile.jpg')
src.close()
print('paragraphs:', len(T), '->', len(after), '| textdiff lines:', len(diff))
print('output:', OUT)
