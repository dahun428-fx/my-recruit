#!/usr/bin/env /usr/bin/python3
"""한미글로벌 [AX실] AI 개발자 지원서 콘텐츠 — 초안 md를 파싱해 구조로 만든다.

지오영은 content.py가 정본이고 md가 파생이었는데, 이번엔 반대로 md가 정본이다.
소유자가 md를 직접 편집하므로 docx와 문면이 어긋날 수 없게 파싱 방식으로 둔다.
정본: outputs/hanmi-global-ax-resume-draft.md
"""
import os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(REPO, 'outputs', 'hanmi-global-ax-resume-draft.md')
SRC = open(MD, encoding='utf8').read()

TODAY = '2026.09.11'
AGE = 35                       # 1991.04.29 생, 2026-09-11 기준 만 나이

# ---- 섹션 분해 -------------------------------------------------------------
def section(name):
    """### <name> 다음부터 다음 ### 또는 ## 까지."""
    m = re.search(r'^###\s+' + re.escape(name) + r'.*$', SRC, re.M)
    if not m:
        raise AssertionError(f'섹션 없음: {name}')
    nxt = re.search(r'^#{2,3}\s', SRC[m.end():], re.M)
    return SRC[m.end(): m.end() + (nxt.start() if nxt else len(SRC))], m.group(0)

def rows(body, ncol):
    """마크다운 표 → 데이터 행 리스트(헤더·구분선 제외)."""
    out = []
    for ln in body.splitlines():
        ln = ln.strip()
        if not ln.startswith('|'):
            continue
        cells = [c.strip() for c in ln.strip('|').split('|')]
        if all(set(c) <= set('-: ') for c in cells):      # 구분선
            continue
        if len(cells) != ncol:
            continue
        out.append(cells)
    return out[1:]                                        # 첫 행은 헤더

def pad(lst, n, ncol):
    return lst + [[''] * ncol for _ in range(n - len(lst))]

# ---- 기본사항 --------------------------------------------------------------
_basic = dict((r[0], r[1]) for r in rows(section('기본사항')[0], 2))
BASIC = {k: _basic[k] for k in
         ['지원회사/분야', '성명', '주소', '병역', '현재연봉', '희망연봉', '입사가능일']}

# ---- 학력 (템플릿 3행) -----------------------------------------------------
EDU = pad(rows(section('학력사항')[0], 5), 3, 5)

# ---- 경력요약 (템플릿 5행) -------------------------------------------------
_career_body, _career_head = section('경력요약')
TOTAL_CAREER = re.search(r'경력요약\(총\s*(.+?)\)', _career_head).group(1)
CAREER_ROWS = pad(rows(_career_body, 5), 5, 5)
CAREER_NOTE = next(l.strip() for l in _career_body.splitlines() if l.strip().startswith('※'))

# ---- 핵심역량 --------------------------------------------------------------
CORE = []
for ln in section('핵심역량')[0].splitlines():
    s = ln.strip()
    if s.startswith('○'):
        CORE.append((s, []))
    elif s.startswith('- ') and CORE:
        CORE[-1][1].append(s)

# ---- 자격 / 교육 / 기타 ----------------------------------------------------
CERTS     = rows(section('자격사항')[0], 4)
TRAININGS = rows(section('교육사항')[0], 3)
ETC       = rows(section('기타사항')[0], 4)

# ---- 상세경력사항 ----------------------------------------------------------
BLOCKS = []
_cur = _pj = None
for ln in section('상세경력사항')[0].splitlines():
    s = ln.strip()
    if not s:
        continue
    if s.startswith('■'):
        _cur = {'header': s, 'intro': '', 'note': '', 'projects': [], 'reason': ''}
        BLOCKS.append(_cur); _pj = None
    elif s.startswith('[회사소개]'):
        _cur['intro'] = s
    elif s.startswith('※'):
        _cur['note'] = s
    elif s.startswith('[주요업무]'):
        pass
    elif s.startswith('[이직사유]'):
        _cur['reason'] = s
    elif re.match(r'^\d+\.\s', s):
        _pj = {'title': s, 'period': '', 'results': [], 'execs': [], 'tech': ''}
        _cur['projects'].append(_pj)
    elif s.startswith('기술:'):
        _pj['tech'] = s
    elif s.startswith('- '):
        _pj['execs'].append(s)
    elif _pj is not None and not _pj['execs'] and not _pj['period']:
        _pj['period'] = s                                  # 제목 바로 다음 줄 = 기간 메타

# ---- 자기소개서 ------------------------------------------------------------
SELF_INTRO = {}
for name in ['[본인 소개 및 성격 특장점]', '[직무수행 역량 및 자세]', '[지원동기 및 입사 후 포부]']:
    body = section(name)[0]
    paras = []
    for blk in body.split('\n\n'):
        t = blk.strip()
        if not t or t.startswith('지원자 :') or t.startswith('위 사항은'):
            continue
        paras.append(' '.join(x.strip() for x in t.splitlines()))
    SELF_INTRO[name] = paras

SIGN = '지원자 : 정 다 훈 拜上'

if __name__ == '__main__':
    print('TOTAL_CAREER', TOTAL_CAREER)
    print('BASIC', len(BASIC), BASIC['지원회사/분야'])
    print('EDU', len(EDU), 'CAREER', len(CAREER_ROWS))
    print('CORE', [(h, len(b)) for h, b in CORE])
    print('CERTS', len(CERTS), 'TRAININGS', len(TRAININGS), 'ETC', len(ETC))
    for b in BLOCKS:
        print('BLOCK', b['header'][:40], '| projects:',
              [(p['title'][:28], len(p['execs']), bool(p['tech']), p['period'][:20]) for p in b['projects']],
              '| reason:', bool(b['reason']))
    for k, v in SELF_INTRO.items():
        print('SELF', k, len(v), '문단')
