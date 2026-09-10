#!/usr/bin/env /usr/bin/python3
"""피플렙 지정양식 docx 2종(이력서·개인정보동의서)에 geoyoung_content.py 값을 주입.

원칙(F-09·troubleshooting/docx-template-render-pipeline.md):
- 템플릿 zip을 베이스로 복사하고 word/document.xml(+사진 media·rels·content type·settings updateFields)만 교체.
- 앵커는 문단 단위 <w:t> 결합 검색(find_para), 모든 앵커 assert, ET 파싱 검증, 텍스트 시퀀스 difflib 대조.
- 셀 안 마지막 문단은 삭제하지 않는다(빈 <w:p/> 유지).
실행: /usr/bin/python3 scripts/build_geoyoung_docx.py <템플릿_이력서.docx> <템플릿_동의서.docx>
"""
import os, re, sys, zipfile, difflib
from xml.etree import ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import geoyoung_content as C

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL_RESUME, TPL_CONSENT = sys.argv[1], sys.argv[2]
# argv[3]: 출력 접미사(선택). 기존 제출본을 덮어쓰지 않고 새 파일로 내보낼 때 사용.
#   예) /usr/bin/python3 scripts/build_geoyoung_docx.py <이력서템플릿> <동의서템플릿> _v2
SUFFIX = sys.argv[3] if len(sys.argv) > 3 else ''
OUT_RESUME = os.path.join(REPO, 'outputs', f'정다훈(만{C.AGE}세)_AI개발_지오영_(주)피플렙_임덕빈2026{SUFFIX}.docx')
OUT_CONSENT = os.path.join(REPO, 'outputs', f'정다훈_개인정보수집 동의서 양식(2026년){SUFFIX}.docx')
PHOTO = os.path.join(REPO, 'outputs', 'assets', 'jungdahun-profile.jpg')

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def texts(d):
    return [''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', m.group(0)))
            for m in re.finditer(r'<w:p[ >].*?</w:p>', d, re.S)]

def find_para(d, key, start=0, nth=0):
    hits = 0
    for m in re.finditer(r'<w:p[ >].*?</w:p>', d[start:], re.S):
        txt = ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', m.group(0)))
        if key in txt:
            if hits == nth:
                return start + m.start(), start + m.end()
            hits += 1
    raise AssertionError(f'문단을 찾지 못함: {key!r} (nth={nth})')

def para_pPr(p):
    m = re.search(r'<w:pPr>.*?</w:pPr>', p, re.S)
    return m.group(0) if m else ''


_AUTOSPACE_OFF = '<w:autoSpaceDE w:val="0"/><w:autoSpaceDN w:val="0"/>'

def no_autospace(ppr):
    """기존 pPr의 autoSpaceDE/DN을 off로. 없으면 스키마 순서에 맞게 삽입."""
    if not ppr:
        return ppr
    if 'autoSpaceDE' in ppr or 'autoSpaceDN' in ppr:
        ppr = re.sub(r'<w:autoSpaceDE\s*/>', '<w:autoSpaceDE w:val="0"/>', ppr)
        ppr = re.sub(r'<w:autoSpaceDN\s*/>', '<w:autoSpaceDN w:val="0"/>', ppr)
        return ppr
    for anchor in ('<w:spacing ', '<w:ind ', '<w:jc ', '</w:pPr>'):
        i = ppr.find(anchor)
        if i != -1:
            return ppr[:i] + _AUTOSPACE_OFF + ppr[i:]
    return ppr

def strip_para_rpr(ppr):
    """pPr 안의 문단 마크 rPr에서 <w:b/> 제거(볼드 상속 방지)."""
    return re.sub(r'<w:b/>|<w:bCs/>', '', ppr)

# 런 서식: 템플릿 본문과 동일(minorHAnsi = 맑은 고딕 계열 테마 폰트, 10pt)
def rpr(bold=False, sz=20, color=None):
    s = '<w:rPr><w:rFonts w:asciiTheme="minorHAnsi" w:eastAsiaTheme="minorHAnsi" w:hAnsiTheme="minorHAnsi" w:cs="Arial" w:hint="eastAsia"/>'
    if bold: s += '<w:b/><w:bCs/>'
    if color: s += f'<w:color w:val="{color}"/>'
    s += f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/></w:rPr>'
    return s

def runs(text, sz=20, bold_all=False, color=None):
    out = ''
    for i, seg in enumerate(text.split('**')):
        if not seg: continue
        out += f'<w:r>{rpr(bold=(bold_all or i % 2 == 1), sz=sz, color=color)}<w:t xml:space="preserve">{esc(seg)}</w:t></w:r>'
    return out

def para(ppr, text, sz=20, bold_all=False, color=None):
    return f'<w:p>{ppr}{runs(text, sz, bold_all, color)}</w:p>'

def set_para_text(d, key, text, nth=0, start=0, sz=None, bold_all=None, keep_ppr=True):
    """앵커 문단을 같은 pPr로 단일(또는 볼드 마커) 런 문단으로 교체."""
    s, e = find_para(d, key, start=start, nth=nth)
    old = d[s:e]
    ppr = para_pPr(old) if keep_ppr else ''
    # 원 런의 크기·볼드를 상속(첫 런 기준)
    m = re.search(r'<w:r[ >].*?</w:r>', old, re.S)
    first_rpr = re.search(r'<w:rPr>.*?</w:rPr>', m.group(0), re.S).group(0) if m and '<w:rPr>' in m.group(0) else ''
    if sz is None:
        mm = re.search(r'<w:sz w:val="(\d+)"/>', first_rpr); sz = int(mm.group(1)) if mm else 20
    if bold_all is None:
        bold_all = '<w:b/>' in first_rpr
    new = para(ppr, text, sz=sz, bold_all=bold_all)
    return d[:s] + new + d[e:], s + len(new)

def cell_after_label(d, label, start=0, nth=0):
    """라벨 셀 문단을 찾고, 그 다음 <w:tc>(값 셀)의 (start,end)를 반환."""
    ls, _ = find_para(d, label, start=start, nth=nth)
    lab_tc_end = d.find('</w:tc>', ls) + 7
    vs = d.find('<w:tc>', lab_tc_end)
    ve = d.find('</w:tc>', vs) + 7
    return vs, ve

def replace_cell_text(d, vs, ve, text, sz=20, bold_all=False, jc=None):
    cell = d[vs:ve]
    body_s = cell.find('</w:tcPr>') + 9
    m = re.search(r'<w:p[ >].*?</w:p>', cell[body_s:], re.S)
    ppr = no_autospace(strip_para_rpr(para_pPr(m.group(0)))) if m else ''
    if jc:
        ppr = re.sub(r'<w:jc w:val="[a-z]+"/>', f'<w:jc w:val="{jc}"/>', ppr)
    new_cell = cell[:body_s] + para(ppr, text, sz=sz, bold_all=bold_all) + '</w:tc>'
    return d[:vs] + new_cell + d[ve:], vs + len(new_cell)

def row_bounds(d, key, start=0):
    s, _ = find_para(d, key, start=start)
    rs = d.rfind('<w:tr ', 0, s)
    re_ = d.find('</w:tr>', s) + 7
    return rs, re_

def fill_row(d, rs, re_, values, sz=20):
    """행의 각 셀 첫 문단을 값으로 교체(빈 값은 빈 문단 유지)."""
    row = d[rs:re_]
    cells = list(re.finditer(r'<w:tc>.*?</w:tc>', row, re.S))
    assert len(cells) == len(values), (len(cells), values)
    out, pos = '', 0
    for c, v in zip(cells, values):
        cell = c.group(0)
        body_s = cell.find('</w:tcPr>') + 9
        m = re.search(r'<w:p[ >].*?</w:p>', cell[body_s:], re.S)
        ppr = no_autospace(strip_para_rpr(para_pPr(m.group(0)))) if m else ''
        new_cell = cell[:body_s] + (para(ppr, v, sz=sz) if v else f'<w:p>{ppr}</w:p>') + '</w:tc>'
        out += row[pos:c.start()] + new_cell
        pos = c.end()
    out += row[pos:]
    return d[:rs] + out + d[re_:], rs + len(out)

# =============================================================================
# 1. 이력서
# =============================================================================
src = zipfile.ZipFile(TPL_RESUME)
doc = src.read('word/document.xml').decode('utf-8')
before = texts(doc)
pos = 0

# ---- 기본사항 표 ---------------------------------------------------------
vs, ve = cell_after_label(doc, '지원회사/분야'); doc, _ = replace_cell_text(doc, vs, ve, C.BASIC['지원회사/분야'])
vs, ve = cell_after_label(doc, '성       명');   doc, _ = replace_cell_text(doc, vs, ve, C.BASIC['성명'])
vs, ve = cell_after_label(doc, '주       소');   doc, _ = replace_cell_text(doc, vs, ve, C.BASIC['주소'])
vs, ve = cell_after_label(doc, '병 역 사 항');   doc, _ = replace_cell_text(doc, vs, ve, C.BASIC['병역'])
vs, ve = cell_after_label(doc, '현 재 연 봉');   doc, _ = replace_cell_text(doc, vs, ve, C.BASIC['현재연봉'])
vs, ve = cell_after_label(doc, '희 망 연 봉');   doc, _ = replace_cell_text(doc, vs, ve, C.BASIC['희망연봉'])
vs, ve = cell_after_label(doc, '입사 가능일');   doc, _ = replace_cell_text(doc, vs, ve, C.BASIC['입사가능일'])
print('1. 기본사항 OK')

# ---- 사진 ------------------------------------------------------------------
ps, pe = find_para(doc, '사진')
ppr = para_pPr(doc[ps:pe])
CX, CY = 1080000, 1432653   # 3.0cm × 3.98cm (원본 245×325 비율)
drawing = (f'<w:r><w:rPr><w:noProof/></w:rPr><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
           f'<wp:extent cx="{CX}" cy="{CY}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
           f'<wp:docPr id="901" name="증명사진"/><wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
           f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
           f'<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr><pic:cNvPr id="901" name="jungdahun-profile.jpg"/><pic:cNvPicPr/></pic:nvPicPr>'
           f'<pic:blipFill><a:blip r:embed="rIdPhoto901"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
           f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{CX}" cy="{CY}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
           f'</a:graphicData></a:graphic></wp:inline></w:drawing></w:r>')
doc = doc[:ps] + f'<w:p>{ppr}{drawing}</w:p>' + doc[pe:]
assert 'xmlns:wp=' in doc[:3000] and 'xmlns:r=' in doc[:3000], '네임스페이스 선언 확인 필요'
print('2. 사진 OK')

# ---- 학력 표 ---------------------------------------------------------------
for key, vals in zip(['2007.03 ~ 2009.02', '2000.03 ~ 2007.02', '1997.03 ~ 2000.02'], C.EDU):
    rs, re_ = row_bounds(doc, key); doc, _ = fill_row(doc, rs, re_, vals)
print('3. 학력 OK')

# ---- 경력요약 ----------------------------------------------------------------
doc, _ = set_para_text(doc, '경력요약(총', f'경력요약(총 {C.TOTAL_CAREER})')
for key, vals in zip(['2021.03~현재', '2015.05~2021.03', '2013.09~2015.01', '2010.04~2013.09', '2006.09~2007.09'], C.CAREER_ROWS):
    rs, re_ = row_bounds(doc, key); doc, _ = fill_row(doc, rs, re_, vals)
# 표 직후 빈 문단에 각주(코오롱 전례) 주입
_last_rs, _ = row_bounds(doc, '2020.10~2025.06')
_tbl_end = doc.find('</w:tbl>', _last_rs) + 8
_m = re.search(r'<w:p[ >].*?</w:p>', doc[_tbl_end:], re.S)
_ppr = strip_para_rpr(para_pPr(_m.group(0)))
doc = doc[:_tbl_end + _m.start()] + para(_ppr, C.CAREER_NOTE, sz=16, color='595959') + doc[_tbl_end + _m.end():]
print('4. 경력요약 OK (+각주)')

# ---- 핵심역량 (○ 5개 + 하위 불릿) ----------------------------------------------
hs, _ = find_para(doc, '○ 서비스센터')
_, last_e = find_para(doc, 'KS서비스 인증')
head_ppr = strip_para_rpr(para_pPr(doc[hs:find_para(doc, '○ 서비스센터')[1]]))
sub_s, sub_e = find_para(doc, ' - 공공기관')
sub_ppr = strip_para_rpr(para_pPr(doc[sub_s:sub_e]))
head_ppr = no_autospace(re.sub(r'<w:ind [^>]*/>', '<w:ind w:left="200" w:hanging="200"/>', head_ppr))
sub_ppr = no_autospace(re.sub(r'<w:ind [^>]*/>', '<w:ind w:left="620" w:hanging="220"/>', sub_ppr))
head_ppr_sp = re.sub(r'<w:spacing [^>]*/>', '', head_ppr).replace('<w:pPr>', '<w:pPr><w:keepNext/>', 1)
head_ppr_sp = re.sub(r'(<w:autoSpaceDN w:val="0"/>|<w:wordWrap/>)', r'\1<w:spacing w:before="120" w:after="30" w:line="259" w:lineRule="auto"/>', head_ppr_sp, count=1)
sub_ppr_sp = re.sub(r'<w:spacing [^>]*/>', '', sub_ppr)
sub_ppr_sp = re.sub(r'(<w:autoSpaceDN w:val="0"/>|<w:wordWrap/>)', r'\1<w:spacing w:before="0" w:after="20" w:line="259" w:lineRule="auto"/>', sub_ppr_sp, count=1)
# 한 ○ 그룹(소제목+불릿)이 페이지 경계에서 쪼개지지 않도록 마지막 불릿 외 keepNext
sub_ppr_keep = sub_ppr_sp.replace('<w:pPr>', '<w:pPr><w:keepNext/>', 1)
new_core = ''
for head, bullets in C.CORE:
    new_core += para(head_ppr_sp, head, bold_all=True)
    for bi_, b in enumerate(bullets):
        last_b = (bi_ == len(bullets) - 1)
        new_core += para(sub_ppr_sp if last_b else sub_ppr_keep, b)
doc = doc[:hs] + new_core + doc[last_e:]
# 섹션 헤딩 고아 방지 — 템플릿 헤딩에 keepNext (코오롱 v4 전례)
for _key in ('핵심역량   **', '상세경력사항'):
    _hs2, _he2 = find_para(doc, _key)
    _p2 = doc[_hs2:_he2]
    if '<w:keepNext/>' not in _p2:
        if '<w:pPr>' in _p2:
            _p2 = _p2.replace('<w:pPr>', '<w:pPr><w:keepNext/>', 1)
        else:
            _p2 = _p2.replace('>', '><w:pPr><w:keepNext/></w:pPr>', 1)
        doc = doc[:_hs2] + _p2 + doc[_he2:]
print('5. 핵심역량 OK (+헤딩 keepNext)')

# ---- 자격사항 표 (3행 → 5행: 마지막 행 복제) -----------------------------------
rows = [row_bounds(doc, k) for k in ['2021.12', '2010.11', '2006.08']]
tmpl_row = doc[rows[2][0]:rows[2][1]]
tmpl_row = re.sub(r' w14:paraId="[0-9A-F]+"', '', tmpl_row)
doc = doc[:rows[2][1]] + tmpl_row * (len(C.CERTS) - 3) + doc[rows[2][1]:]
p = 0
for vals in C.CERTS:
    rs, re_ = row_bounds(doc, 'OOOO', start=p) if 'OOOO' in doc[p:p+400000] else (None, None)
    # 첫 3행은 OOOO 앵커, 복제 행도 OOOO 앵커 → 순서대로 소진
    doc, p = fill_row(doc, rs, re_, vals)
print('6. 자격 OK')

# ---- 교육사항 표 ---------------------------------------------------------------
rs, re_ = row_bounds(doc, '2021.11.29'); doc, p = fill_row(doc, rs, re_, C.TRAININGS[0])
print('7. 교육 OK')

# ---- 기타사항 표 ---------------------------------------------------------------
rs, re_ = row_bounds(doc, '2013년'); doc, p = fill_row(doc, rs, re_, C.ETC[0])
print('8. 기타 OK')

# ---- 상세경력사항: 템플릿 블록 3개 → 우리 블록 2개 --------------------------------
b1s, _ = find_para(doc, '■ 0000.00', nth=0)
sig_s, _ = find_para(doc, '자기소개서')          # 섹션 헤딩 "자기소개서  …"

# 문단 서식 정의 — 템플릿 pPr 상속 대신 명시 지정(행간 1.08배, 들여쓰기 계층 고정)
LINE = '<w:spacing w:before="%d" w:after="%d" w:line="259" w:lineRule="auto"/>'
def PPR(before=0, after=20, left=0, hanging=0, keep=False, jc='left'):
    ind = ''
    if left or hanging:
        ind = f'<w:ind w:left="{left}"' + (f' w:hanging="{hanging}"' if hanging else '') + '/>'
    return ('<w:pPr>' + ('<w:keepNext/>' if keep else '') + '<w:wordWrap/>' + _AUTOSPACE_OFF
            + (LINE % (before, after)) + ind + f'<w:jc w:val="{jc}"/>'
            + '<w:textAlignment w:val="baseline"/></w:pPr>')

PPR_HDR    = PPR(before=240, after=60, keep=True)                      # ■ 회사 헤더
PPR_INTRO2 = PPR(before=0, after=20, left=200, keep=True)              # [회사소개]
PPR_NOTE   = PPR(before=0, after=60, left=200)                         # ※ 각주
PPR_LABEL  = PPR(before=80, after=60, keep=True)                       # [주요업무]
PPR_TITLE  = PPR(before=130, after=20, left=200, hanging=200, keep=True)  # 프로젝트 제목
PPR_PERIOD = PPR(before=0, after=50, left=400, keep=True)              # 기간 메타
PPR_RES      = PPR(before=0, after=20, left=420, hanging=180)          # → 성과 선행 줄
PPR_RES_LAST = PPR(before=0, after=90, left=420, hanging=180)          # → 성과(마지막, 실행과 간격)
PPR_EXEC     = PPR(before=0, after=20, left=460, hanging=200)          # - 실행 불릿
PPR_EXEC_L   = PPR(before=0, after=60, left=460, hanging=200)          # - 실행(마지막, 기술과 간격)
PPR_TECH   = PPR(before=40, after=0, left=420)                         # 기술 줄
PPR_REASON = PPR(before=90, after=0, left=200, hanging=200)           # [이직사유]
PPR_GAP    = PPR(before=0, after=0)

spacer = f'<w:p>{PPR_GAP}</w:p>'

blocks = ''
for bi, blk in enumerate(C.BLOCKS):
    blocks += para(PPR_HDR if bi == 0 else PPR(before=260, after=60, keep=True), blk['header'], bold_all=True)
    blocks += para(PPR_INTRO2, blk['intro'], sz=18, color='595959')
    if blk.get('note'):
        blocks += para(PPR_NOTE, blk['note'], sz=17, color='808080')
    blocks += para(PPR_LABEL, '[주요업무]', bold_all=True)
    for pj in blk['projects']:
        blocks += para(PPR_TITLE, pj['title'], bold_all=True)
        if pj.get('period'):
            blocks += para(PPR_PERIOD, pj['period'], sz=17, color='808080')
        execs = pj.get('execs', [])
        for ri, r in enumerate(pj.get('results', [])):
            last_res = (ri == len(pj['results']) - 1)
            blocks += para(PPR_RES_LAST if (last_res and execs) else PPR_RES, r, sz=19)
        for ei, e in enumerate(execs):
            last_ex = (ei == len(execs) - 1)
            blocks += para(PPR_EXEC if (last_ex and pj.get('tech')) else
                           (PPR_EXEC_L if last_ex else PPR_EXEC), e, sz=19)
        if pj.get('tech'):
            blocks += para(PPR_TECH, pj['tech'], sz=17, color='595959')
    blocks += para(PPR_REASON, blk['reason'], sz=19)
    # 회사 블록 사이 빈 문단 제거 — 다음 헤더 before 여백으로 대체(페이지 절약)
doc = doc[:b1s] + blocks + doc[sig_s:]
print('9. 상세경력 OK')

# ---- 자기소개서 -----------------------------------------------------------------
h1s, h1e = find_para(doc, '[본인 소개')
h2s, h2e = find_para(doc, '[직무수행 역량')
h3s, h3e = find_para(doc, '[지원동기 및')
sig_s, sig_e = find_para(doc, '지원자 : 0 0 0')
prose_ppr = ('<w:pPr><w:wordWrap/>' + _AUTOSPACE_OFF + '<w:spacing w:before="0" w:after="140" w:line="300" w:lineRule="auto"/>'
             '<w:ind w:left="120" w:right="120"/><w:jc w:val="left"/>'
             '<w:textAlignment w:val="baseline"/></w:pPr>')
subhead_ppr = ('<w:pPr><w:keepNext/><w:wordWrap/>' + _AUTOSPACE_OFF + '<w:spacing w:before="200" w:after="60" w:line="300" w:lineRule="auto"/>'
               '<w:ind w:left="120"/><w:jc w:val="left"/>'
               '<w:textAlignment w:val="baseline"/></w:pPr>')
h1 = doc[h1s:h1e]; h2 = doc[h2s:h2e]; h3 = doc[h3s:h3e]

def section(paras):
    out = ''
    for ptxt in paras:
        if ptxt.startswith('**') and ptxt.endswith('**') and ptxt.count('**') == 2 and len(ptxt) < 60:
            out += para(subhead_ppr, ptxt)
        else:
            out += para(prose_ppr, ptxt)
    return out + spacer

keys = list(C.SELF_INTRO.keys())
new_si = h1 + section(C.SELF_INTRO[keys[0]]) + h2 + section(C.SELF_INTRO[keys[1]]) + h3 + section(C.SELF_INTRO[keys[2]]) + spacer
doc = doc[:h1s] + new_si + doc[sig_s:]
doc, _ = set_para_text(doc, '지원자 : 0 0 0', C.SIGN)
print('10. 자기소개서 OK')

# ---- 검증 ---------------------------------------------------------------------
ET.fromstring(doc.encode('utf-8'))
assert 'OOOO' not in doc and '0000년생' not in doc and '홍 길 동' not in doc, '자리표시자 잔존'
after = texts(doc)
diff = [l for l in difflib.unified_diff(before, after, lineterm='', n=0) if l[:1] in '+-' and l[:3] not in ('+++', '---')]
open(os.path.join(REPO, 'outputs', 'geoyoung-docx-textdiff.txt'), 'w').write('\n'.join(diff))
print(f'   텍스트 diff {len(diff)}줄 → outputs/geoyoung-docx-textdiff.txt')

# ---- 조립(사진 media·rels·content types·settings updateFields) ---------------------
rels = src.read('word/_rels/document.xml.rels').decode('utf-8')
rels = rels.replace('</Relationships>', '<Relationship Id="rIdPhoto901" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/jungdahun-profile.jpg"/></Relationships>')
ct = src.read('[Content_Types].xml').decode('utf-8')
if 'Extension="jpg"' not in ct:
    ct = ct.replace('<Default Extension="png"', '<Default Extension="jpg" ContentType="image/jpeg"/><Default Extension="png"')
settings = src.read('word/settings.xml').decode('utf-8')
# 푸터는 PAGE 필드만 있어(NUMPAGES 없음) updateFields 불필요 — Word 열 때 "필드 업데이트" 모달을 유발하므로 넣지 않는다.
with zipfile.ZipFile(OUT_RESUME, 'w', zipfile.ZIP_DEFLATED) as z:
    for item in src.infolist():
        data = src.read(item.filename)
        if item.filename == 'word/document.xml': data = doc.encode('utf-8')
        elif item.filename == 'word/_rels/document.xml.rels': data = rels.encode('utf-8')
        elif item.filename == '[Content_Types].xml': data = ct.encode('utf-8')
        elif item.filename == 'word/settings.xml': data = settings.encode('utf-8')
        z.writestr(item, data)
    z.write(PHOTO, 'word/media/jungdahun-profile.jpg')
src.close()
print('output:', OUT_RESUME)

# =============================================================================
# 2. 개인정보 동의서
# =============================================================================
src = zipfile.ZipFile(TPL_CONSENT)
doc = src.read('word/document.xml').decode('utf-8')
before = texts(doc)
# 동의함 체크박스(첫 sdt) 체크
i = doc.find('동의함(')
sdt_s = doc.find('<w:sdt>', i); sdt_e = doc.find('</w:sdt>', sdt_s) + 8
sdt = doc[sdt_s:sdt_e]
assert '<w14:checked w14:val="0"/>' in sdt and '☐' in sdt
sdt = sdt.replace('<w14:checked w14:val="0"/>', '<w14:checked w14:val="1"/>').replace('☐', '☒')
doc = doc[:sdt_s] + sdt + doc[sdt_e:]
# 날짜
doc, _ = set_para_text(doc, '2026년 1 월', C.CONSENT['날짜'])
# 표: 성명·출생연도·이메일·전화
doc, _ = set_para_text(doc, '홍 길 동', C.CONSENT['본인성명'])
doc, _ = set_para_text(doc, '1986', C.CONSENT['출생연도'])
for label, key in [('이메일주소', '이메일주소'), ('전화번호', '전화번호')]:
    # 라벨 셀은 표 안의 것(본문 안내문에도 같은 단어가 있으므로 <w:tc> 직전 문단만)
    n = 0
    while True:
        ls, le = find_para(doc, label, nth=n)
        if doc.rfind('<w:tc>', 0, ls) > doc.rfind('</w:tc>', 0, ls) and ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', doc[ls:le])).strip() == label:
            break
        n += 1
    lab_tc_end = doc.find('</w:tc>', ls) + 7
    vs = doc.find('<w:tc>', lab_tc_end); ve = doc.find('</w:tc>', vs) + 7
    doc, _ = replace_cell_text(doc, vs, ve, C.CONSENT[key], sz=18, jc='center')
ET.fromstring(doc.encode('utf-8'))
after = texts(doc)
diff = [l for l in difflib.unified_diff(before, after, lineterm='', n=0) if l[:1] in '+-' and l[:3] not in ('+++', '---')]
print('   동의서 텍스트 diff:'); print('\n'.join('   ' + l for l in diff))
with zipfile.ZipFile(OUT_CONSENT, 'w', zipfile.ZIP_DEFLATED) as z:
    for item in src.infolist():
        data = src.read(item.filename)
        if item.filename == 'word/document.xml': data = doc.encode('utf-8')
        z.writestr(item, data)
src.close()
print('output:', OUT_CONSENT)
