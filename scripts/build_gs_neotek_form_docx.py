#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-
"""GS네오텍 입사지원서(pptx 양식)를 Word(docx)로 재현해 작성.

- 양식 원본: ~/Downloads/[GS네오텍] 입사지원서 양식.pptx (5장: 기본사항·병역·학력·자격·외국어·해외연수 /
  경력·경험·수상 / 자기소개서 ①②③ / ④ / ⑤ 경력기술). 섹션명·칸 이름·순서·열 폭(cm)은 pptx 도형 좌표를 그대로 옮김.
- 기본사항 좌상단 빈 영역(4.4×3.5cm, 도형 없음)은 사진 칸으로 사용.
- 패키지 베이스: 보배써치 표준이력서 docx의 styles·theme·fonts만 차용(본문·머리글 참조는 모두 교체/제거).
- 값 원천: outputs/gs-neotek-fullstack-resume-draft.md(경력기술 ⑤) + outputs/gs-neotek-form-self-intro.md(①~④ 소유자 원문, 무수정)
  + 아래 FORM 딕셔너리(profile.md·target-companies 결정값).
실행: /usr/bin/python3 scripts/build_gs_neotek_form_docx.py <보배써치_템플릿.docx>
"""
import os, re, sys, zipfile
from xml.etree import ElementTree as ET

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = sys.argv[1]
OUT = os.path.join(REPO, 'outputs', '정다훈(만35세)_플랫폼개발_GS네오텍_입사지원서2026.docx')
PHOTO = os.path.join(REPO, 'outputs', 'assets', 'jungdahun-profile.jpg')
DRAFT = open(os.path.join(REPO, 'outputs', 'gs-neotek-fullstack-resume-draft.md'), encoding='utf-8').read()
SI = open(os.path.join(REPO, 'outputs', 'gs-neotek-form-self-intro.md'), encoding='utf-8').read()

# ---------------------------------------------------------------------------
# 양식 값 (profile.md · target-companies GS네오텍 결정 · 초안 md)
# ---------------------------------------------------------------------------
FORM = {
    '지원분야': '플랫폼개발(풀스택)',
    '성명(한글)': '정다훈', '신입/경력': '경력 (총 5년 11개월)',
    '성명(영문)': 'Jung Dahun', '전화(집)': '',
    '성명(한자)': '丁多勳', '휴대폰': '010-4346-0429',
    '생년월일': '1991.04.29', 'E-mail': 'dahun428@naver.com',
    '우편번호': '', '현주소': '경기도 구리시 인창동',
    '장애여부': '비대상', '보훈여부': '비대상', '보훈관계': '',
    '희망연봉': '면접 시 협의', '희망직위': '면접 시 협의',
}
MILITARY = [('실역구분', '군필'), ('입대일자', '2011.09'), ('군별/병', '육군'), ('주특기', '행정병'),
            ('계급', '병장'), ('제대일자', '2013.06'), ('역종', '현역'), ('전역사유', '만기제대')]
EDU = [('성공회대학교', '일어일본학과(경영학과 복수전공)', '2010.03', '2017.02', '3.8/4.5', '주간', '서울'),
       ('여의도고등학교', '-', '2007.03', '2010.02', '-', '주간', '서울'),
       ('', '', '', '', '', '', '')]
CERT = [('정보처리기사', '20202050514D', '2020.08.28', '', '', '한국산업인력공단'),
        ('KT AICE Associate (100/100)', '', '2026.08', '', '', 'KT'),
        ('Microsoft Certified: Azure Fundamentals (AZ-900)', 'BFC5A4-H4872F', '2023.06', '', '', 'Microsoft'),
        ('자산관리사(FP)', '1604027370', '2016.11', '', '', '한국금융연수원')]
LANG = [('영어', 'TOEIC 825점', '2024.05'), ('일본어', 'JLPT N1', '2018.08')]
ABROAD = [('일본', '2018.09', '2019.06', '워킹홀리데이 · 무인양품 도쿄 지사 근무, 비즈니스 일본어 실무 활용'), ('', '', '', ''), ('', '', '', '')]
CAREER = [('다나아데이터(대웅 계열사)', '플랫폼개발팀', '팀원', '2026.06', '재직 중', '5,700만원', '정규직', '헬스케어 서비스', '재직 중(플랫폼 개발 경험 확장)'),
          ('대웅제약', 'AI추진팀', '팀원', '2025.07', '2026.05', '-', '정규직', '제약', '계열사 조직 이관'),
          ('내담씨앤씨', 'SI사업부', '대리', '2020.10', '2025.06', '-', '정규직', 'IT 서비스(SI)', '자사 서비스 조직 이동')]
EXPERIENCE = [('교육', '2020.03', '2020.09', '중앙에이치티에이㈜', '웹 콘텐츠 개발을 위한 응용SW엔지니어링 과정 수료 (Java 기반 웹 개발)')]
AWARD = [('', '', '', '')]
NOTE_CAREER = '※ 대웅제약 AI추진팀(2025.07~2026.05)에서 2026년 6월 계열사 조직 이관으로 다나아데이터 플랫폼개발팀에 소속이 변경되었으며, 같은 서비스 개발·운영 업무를 이어서 담당하고 있습니다.'

# ---------------------------------------------------------------------------
# XML 헬퍼
# ---------------------------------------------------------------------------
CM = 567
FONT = '<w:rFonts w:ascii="맑은 고딕" w:eastAsia="맑은 고딕" w:hAnsi="맑은 고딕" w:cs="맑은 고딕"/>'

def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def rpr(sz=17, bold=False, color=None):
    return '<w:rPr>' + FONT + ('<w:b/><w:bCs/>' if bold else '') + (f'<w:color w:val="{color}"/>' if color else '') + f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/></w:rPr>'

def runs(text, sz=17, bold=False, color=None):
    out = ''
    for i, seg in enumerate(text.split('**')):
        if seg:
            out += f'<w:r>{rpr(sz, bold or i % 2 == 1, color)}<w:t xml:space="preserve">{esc(seg)}</w:t></w:r>'
    return out

def para(text, sz=17, bold=False, jc='center', after=0, before=0, color=None, ind=None, line=240):
    ind_x = ''
    if ind:
        ind_x = f'<w:ind w:left="{ind[0]}" w:hanging="{ind[1]}"/>'
    return (f'<w:p><w:pPr><w:wordWrap w:val="0"/><w:spacing w:before="{before}" w:after="{after}" w:line="{line}" w:lineRule="auto"/>{ind_x}<w:jc w:val="{jc}"/></w:pPr>'
            f'{runs(text, sz, bold, color)}</w:p>')

def cell(content_paras, w_cm, fill=None, span=1, vmerge=None, valign='center'):
    tc = f'<w:tc><w:tcPr><w:tcW w:w="{int(w_cm * CM)}" w:type="dxa"/>'
    if span > 1:
        tc += f'<w:gridSpan w:val="{span}"/>'
    if vmerge == 'restart':
        tc += '<w:vMerge w:val="restart"/>'
    elif vmerge == 'cont':
        tc += '<w:vMerge/>'
    if fill:
        tc += f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>'
    tc += f'<w:vAlign w:val="{valign}"/></w:tcPr>'
    tc += content_paras if content_paras else '<w:p><w:pPr><w:spacing w:before="0" w:after="0"/></w:pPr></w:p>'
    return tc + '</w:tc>'

def label(t, w, span=1, vmerge=None):
    return cell(para(t, sz=17, bold=True), w, fill='F2F2F2', span=span, vmerge=vmerge)

def value(t, w, span=1, jc='center'):
    return cell(para(t, sz=17, jc=jc) if t else '', w, fill='FFFFFF', span=span)

def row(cells, h_cm=0.7, cant_split=True):
    return (f'<w:tr><w:trPr>{"<w:cantSplit/>" if cant_split else ""}<w:trHeight w:val="{int(h_cm * CM)}" w:hRule="atLeast"/></w:trPr>'
            + ''.join(cells) + '</w:tr>')

BORDER = ''.join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="000000"/>' for s in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'))

def table(grid_cm, rows_xml):
    total = int(sum(grid_cm) * CM)
    return (f'<w:tbl><w:tblPr><w:tblW w:w="{total}" w:type="dxa"/><w:jc w:val="center"/><w:tblLayout w:type="fixed"/>'
            f'<w:tblBorders>{BORDER}</w:tblBorders><w:tblCellMar><w:top w:w="0" w:type="dxa"/><w:left w:w="57" w:type="dxa"/>'
            f'<w:bottom w:w="0" w:type="dxa"/><w:right w:w="57" w:type="dxa"/></w:tblCellMar></w:tblPr>'
            f'<w:tblGrid>{"".join(f"<w:gridCol w:w={chr(34)}{int(g * CM)}{chr(34)}/>" for g in grid_cm)}</w:tblGrid>'
            + ''.join(rows_xml) + '</w:tbl>')

W = 19.6
def section_bar(title):
    return table([W], [row([cell(para(title, sz=19, bold=True), W, fill='D7D7D7')], 0.7)])

def gap(pt=4):
    return f'<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="{pt * 20}" w:lineRule="exact"/></w:pPr></w:p>'

PAGE_BREAK = '<w:p><w:pPr><w:pageBreakBefore/><w:spacing w:before="0" w:after="0" w:line="20" w:lineRule="exact"/></w:pPr></w:p>'  # 빈 줄 없이 다음 요소를 새 페이지로

CX, CY = 900000, 1188000  # 2.5 × 3.3 cm (245×325 비율)
PHOTO_RUN = (f'<w:r><w:rPr><w:noProof/></w:rPr><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
             f'<wp:extent cx="{CX}" cy="{CY}"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:docPr id="901" name="증명사진"/>'
             f'<wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
             f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
             f'<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr><pic:cNvPr id="901" name="jungdahun-profile.jpg"/><pic:cNvPicPr/></pic:nvPicPr>'
             f'<pic:blipFill><a:blip r:embed="rIdPhoto901"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
             f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{CX}" cy="{CY}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
             f'</a:graphicData></a:graphic></wp:inline></w:drawing></w:r>')

# ---------------------------------------------------------------------------
# 1/5 기본사항·병역·학력·자격·외국어·해외연수
# ---------------------------------------------------------------------------
body = []
body.append(table([W], [row([cell(para('[GS네오텍 입사지원서]', sz=28, bold=True), W, fill='FFFFFF')], 0.9)]))
body.append(section_bar('[기본사항]'))
G = [2.0, 2.4, 2.2, 5.1, 2.8, 5.1]
photo_p = f'<w:p><w:pPr><w:spacing w:before="0" w:after="0"/><w:jc w:val="center"/></w:pPr>{PHOTO_RUN}</w:p>'
F = FORM
rows = [
    row([cell(photo_p, 4.4, fill='FFFFFF', span=2, vmerge='restart'), label('지원분야', 2.2), value(F['지원분야'], 13.0, span=3)]),
    row([cell('', 4.4, span=2, vmerge='cont'), label('성명(한글)', 2.2), value(F['성명(한글)'], 5.1), label('신입/경력', 2.8), value(F['신입/경력'], 5.1)]),
    row([cell('', 4.4, span=2, vmerge='cont'), label('성명(영문)', 2.2), value(F['성명(영문)'], 5.1), label('전화(집)', 2.8), value(F['전화(집)'], 5.1)]),
    row([cell('', 4.4, span=2, vmerge='cont'), label('성명(한자)', 2.2), value(F['성명(한자)'], 5.1), label('휴대폰', 2.8), value(F['휴대폰'], 5.1)]),
    row([cell('', 4.4, span=2, vmerge='cont'), label('생년월일', 2.2), value(F['생년월일'], 5.1), label('E-mail', 2.8), value(F['E-mail'], 5.1)]),
    row([label('우편번호', 2.0), value(F['우편번호'], 2.4), label('현주소', 2.2), value(F['현주소'], 13.0, span=3)]),
    row([label('장애여부', 2.0), value(F['장애여부'], 2.4), label('보훈여부', 2.2), value(F['보훈여부'], 5.1), label('보훈관계', 2.8), value(F['보훈관계'], 5.1)]),
    row([label('희망연봉', 2.0), value(F['희망연봉'], 9.7, span=3), label('희망직위', 2.8), value(F['희망직위'], 5.1)]),
]
body.append(table(G, rows))
body.append(gap(8))

body.append(section_bar('[병역사항]'))
G = [1.8, 1.8, 1.8, 2.4, 1.8, 3.5, 1.8, 4.7]
m = MILITARY
body.append(table(G, [
    row([label(m[0][0], 1.8), value(m[0][1], 1.8), label(m[1][0], 1.8), value(m[1][1], 2.4), label(m[2][0], 1.8), value(m[2][1], 3.5), label(m[3][0], 1.8), value(m[3][1], 4.7)]),
    row([label(m[4][0], 1.8), value(m[4][1], 1.8), label(m[5][0], 1.8), value(m[5][1], 2.4), label(m[6][0], 1.8), value(m[6][1], 3.5), label(m[7][0], 1.8), value(m[7][1], 4.7)]),
]))
body.append(gap(8))

body.append(section_bar('[학력사항]'))
G = [4.1, 4.1, 1.8, 1.8, 2.3, 2.1, 3.4]
hdr = ['학교', '전공', '입학연월', '졸업연월', '평점(백분율)', '주야', '소재지']
body.append(table(G, [row([label(h, g) for h, g in zip(hdr, G)])] + [row([value(v, g) for v, g in zip(r, G)]) for r in EDU]))
body.append(gap(8))

body.append(section_bar('[자격사항]'))
G = [4.2, 3.5, 2.3, 1.7, 3.5, 4.4]
hdr = ['자격명', '자격번호', '취득일자', '갱신연월', '유효기간', '발행처']
body.append(table(G, [row([label(h, g) for h, g in zip(hdr, G)])] + [row([value(v, g) for v, g in zip(r, G)]) for r in CERT]))
body.append(gap(8))

body.append(section_bar('[외국어사항]'))
G = [8.3, 7.1, 4.2]
hdr = ['외국어명', '취득점수(레벨)', '취득일자']
body.append(table(G, [row([label(h, g) for h, g in zip(hdr, G)])] + [row([value(v, g) for v, g in zip(r, G)]) for r in LANG]
                  + [row([cell(para('※ 공인인증어학 성적이 없다면, 구사 가능한 외국어 수준(상/중/하) 을 표기하십시오.', sz=15, jc='left'), W, fill='FFFFFF', span=3)], 0.5)]))
body.append(gap(8))

body.append(section_bar('[해외연수]'))
G = [4.2, 2.8, 2.8, 9.8]
body.append(table(G, [
    row([label('연수국가', 4.2, vmerge='restart'), label('연수기간', 5.6, span=2), label('연수목적 및 활동내역', 9.8, vmerge='restart')], 0.5),
    row([cell('', 4.2, fill='F2F2F2', vmerge='cont'), label('From', 2.8), label('To', 2.8), cell('', 9.8, fill='F2F2F2', vmerge='cont')], 0.5),
] + [row([value(r[0], 4.2), value(r[1], 2.8), value(r[2], 2.8), value(r[3], 9.8, jc='left')], 0.9) for r in ABROAD]))

# ---------------------------------------------------------------------------
# 2/5 경력·경험·수상
# ---------------------------------------------------------------------------
body.append(PAGE_BREAK)
# [핵심역량] — pptx 양식에는 없는 란. 소유자 요청(2026-09-14)으로 2쪽 경력사항 앞에 추가. 원천: 초안 md "## 핵 심 역 량"
core = [l[2:].strip() for l in re.search(r'^## 핵 심 역 량\n(.*?)(?=^## )', DRAFT, re.S | re.M).group(1).splitlines() if l.startswith('- ')]
core_paras = ''
for c in core:
    line = f'- **{c.split(" : ", 1)[0]}** : {c.split(" : ", 1)[1]}' if ' : ' in c else f'- {c}'
    core_paras += para(line, sz=17, jc='left', after=40, ind=(170, 170), line=260)
body.append(section_bar('[핵심역량]'))
body.append(table([W], [row([cell(core_paras, W, fill='FFFFFF', valign='top')], 0.7, cant_split=False)]))
body.append(gap(8))
body.append(section_bar('[경력사항]'))
G = [3.0, 2.5, 1.3, 2.3, 2.3, 1.6, 1.8, 2.1, 2.7]
body.append(table(G, [
    row([label('근무회사', 3.0, vmerge='restart'), label('소속', 2.5, vmerge='restart'), label('직위', 1.3, vmerge='restart'),
         label('근무기간', 4.6, span=2), label('연봉', 1.6, vmerge='restart'), label('고용형태', 1.8, vmerge='restart'),
         label('업종', 2.1, vmerge='restart'), label('퇴직사유', 2.7, vmerge='restart')], 0.5),
    row([cell('', 3.0, fill='F2F2F2', vmerge='cont'), cell('', 2.5, fill='F2F2F2', vmerge='cont'), cell('', 1.3, fill='F2F2F2', vmerge='cont'),
         label('From', 2.3), label('To', 2.3), cell('', 1.6, fill='F2F2F2', vmerge='cont'), cell('', 1.8, fill='F2F2F2', vmerge='cont'),
         cell('', 2.1, fill='F2F2F2', vmerge='cont'), cell('', 2.7, fill='F2F2F2', vmerge='cont')], 0.5),
] + [row([value(v, g) for v, g in zip(r, G)], 0.9) for r in CAREER]
  + [row([value('', g) for g in G], 0.9) for _ in range(6 - len(CAREER))]))
body.append(para(NOTE_CAREER, sz=15, jc='left', before=40, color='595959'))
body.append(gap(8))

body.append(section_bar('[경험사항]'))
G = [2.5, 2.3, 2.3, 3.5, 9.0]
body.append(table(G, [
    row([label('구분', 2.5, vmerge='restart'), label('활동기간', 4.6, span=2), label('활동단체', 3.5, vmerge='restart'), label('활동내용', 9.0, vmerge='restart')], 0.5),
    row([cell('', 2.5, fill='F2F2F2', vmerge='cont'), label('From', 2.3), label('To', 2.3), cell('', 3.5, fill='F2F2F2', vmerge='cont'), cell('', 9.0, fill='F2F2F2', vmerge='cont')], 0.5),
] + [row([value(r[0], 2.5), value(r[1], 2.3), value(r[2], 2.3), value(r[3], 3.5), value(r[4], 9.0, jc='left')], 0.7) for r in EXPERIENCE]))
body.append(gap(8))

body.append(section_bar('[수상실적]'))
G = [4.8, 2.3, 4.9, 7.6]
hdr = ['수상명', '수상일자', '수여기관', '수상내용']
body.append(table(G, [row([label(h, g) for h, g in zip(hdr, G)])] + [row([value(v, g) for v, g in zip(r, G)]) for r in AWARD]))

# ---------------------------------------------------------------------------
# 3~5/5 자기소개서 ①~⑤
# ---------------------------------------------------------------------------
def si_block(num_title):
    m = re.search(r'^## ' + re.escape(num_title) + r'[^\n]*\n(.*?)(?=^## |\Z)', SI, re.S | re.M)
    assert m, num_title
    return [p.strip() for p in m.group(1).strip().split('\n\n') if p.strip()]

def essay_row(label_lines, paras_text, min_h):
    lab = ''.join(para(l, sz=17, bold=True) for l in label_lines)
    content = ''.join(para(t, sz=17, jc='both', after=100, line=264) for t in paras_text)
    return (f'<w:tr><w:trPr><w:trHeight w:val="{int(min_h * CM)}" w:hRule="atLeast"/></w:trPr>'
            + cell(lab, 3.5, fill='F2F2F2') + cell(content, 16.1, fill='FFFFFF', valign='top') + '</w:tr>')

# ⑤ 경력기술: 초안 md "주 요 project 내역" 압축(성과 요약·문제·주요 실행 2~3개·기술)
proj = re.search(r'^## 주 요 project 내역\n(.*?)(?=^## )', DRAFT, re.S | re.M).group(1)
career_paras = []
blocks = [b for b in re.split(r'\n(?=- )', proj.strip()) if b.strip()]
for b in blocks:
    lines = b.splitlines()
    title = lines[0][2:].strip()
    subs = [l.strip()[2:] for l in lines[1:] if l.strip().startswith('- ')]
    keep = []
    for s in subs:
        lab = s.split(' : ', 1)[0] if ' : ' in s else s.split(':', 1)[0]
        if lab in ('문제', '기술', '검증') or s.startswith('기술:'):  # 검증은 AI 도구 블록 E2E와 중복
            continue
        keep.append(s)
    body_lines = [f'**■ {title}**'] + ['· ' + (f"**{s.split(' : ', 1)[0]}** : {s.split(' : ', 1)[1]}" if ' : ' in s else s) for s in keep]
    # 기술 줄은 ⑤ 한 페이지 수용을 위해 생략(스택은 2쪽 [핵심역량] 란에 존재)
    career_paras.append(body_lines)

def career_cell():
    out = ''
    for bl in career_paras:
        out += para(bl[0], sz=17, jc='left', before=60, after=20)
        for l in bl[1:]:
            out += para(l, sz=16, jc='left', after=6, ind=(280, 140), line=240)
    return out

body.append(PAGE_BREAK)
body.append(section_bar('[자기소개서]'))
body.append(table([3.5, 16.1], [
    essay_row(['① 본인의 핵심역량', '(차별화된 강점 등)'], si_block('① 본인의 핵심역량'), 3.0),
    essay_row(['② 성격의 장단점 및', '보완노력'], si_block('② 성격의 장단점'), 3.0),
    essay_row(['③ 열정을 다해 성공', '적으로 마친 경험 (업', '무/프로젝트/활동)'], si_block('③ 열정을 다해'), 3.0),
]))
body.append(PAGE_BREAK)
body.append(table([3.5, 16.1], [essay_row(['④ 지원동기 및 입사', '후 포부'], si_block('④ 지원동기'), 21.3)]))
body.append(PAGE_BREAK)
body.append(table([3.5, 16.1], [
    f'<w:tr><w:trPr><w:trHeight w:val="{int(3.0 * CM)}" w:hRule="atLeast"/></w:trPr>'
    + cell(''.join(para(l, sz=17, bold=True) for l in ['⑤ 경력기술', '(*경력기술서 파일', '첨부로 대체 가능)']), 3.5, fill='F2F2F2')
    + cell(career_cell(), 16.1, fill='FFFFFF', valign='top') + '</w:tr>'
]))
body.append('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="20" w:lineRule="exact"/></w:pPr></w:p>')

# ---------------------------------------------------------------------------
# 조립
# ---------------------------------------------------------------------------
src = zipfile.ZipFile(BASE)
doc = src.read('word/document.xml').decode('utf-8')
head = doc[:doc.find('<w:body>') + len('<w:body>')]
sect = ('<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="567" w:right="397" w:bottom="567" w:left="397" '
        'w:header="397" w:footer="397" w:gutter="0"/><w:cols w:space="425"/><w:docGrid w:linePitch="360"/></w:sectPr>')
out_doc = head + ''.join(body) + sect + '</w:body></w:document>'
try:
    ET.fromstring(out_doc.encode('utf-8'))
except ET.ParseError as e:
    ln, col = e.position
    print('PARSE ERROR:', out_doc.split('\n')[ln - 1][max(0, col - 300):col + 100])
    raise

rels = src.read('word/_rels/document.xml.rels').decode('utf-8')
rels = rels.replace('</Relationships>', '<Relationship Id="rIdPhoto901" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/jungdahun-profile.jpg"/></Relationships>')
ct = src.read('[Content_Types].xml').decode('utf-8')
if 'Extension="jpg"' not in ct:
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
for bad in ['OOOO', '홍 길 동', '확인 필요']:
    assert bad not in out_doc, bad
print('output:', OUT)
