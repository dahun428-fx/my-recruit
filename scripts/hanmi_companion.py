#!/usr/bin/env /usr/bin/python3
"""한미글로벌 초안 md → companion(new-prose) 생성.

출처 자동 판정: 정규화한 라인이 코퍼스(지오영 v14 제출 docx / 지오영 md 초안 /
코오롱베니트 v4 제출 docx / GS글로벌 v7 초안 md)에 그대로 있으면 `재사용`,
아니면 `신규/수정`.
"""
import os, re, sys, zipfile, io, subprocess

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, 'outputs')
DRAFT = os.path.join(OUT, 'hanmi-global-ax-resume-draft.md')
COMP = os.path.join(OUT, 'hanmi-global-ax-new-prose.md')

def norm(s):
    s = s.replace('**', '')
    s = re.sub(r'^[\s○▪■→\-–·•]+', '', s)
    s = re.sub(r'^\d+\.\s*', '', s)
    return re.sub(r'\s+', '', s)

corpus = {}
def add_docx(path, label):
    if not os.path.exists(path): return
    d = zipfile.ZipFile(path).read('word/document.xml').decode('utf8')
    for m in re.finditer(r'<w:p[ >].*?</w:p>', d, re.S):
        t = ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', m.group(0)))
        if t.strip(): corpus.setdefault(norm(t), set()).add(label)

def add_git_docx(relpath, label):
    r = subprocess.run(['git','show','HEAD:'+relpath], cwd=REPO, capture_output=True)
    if r.returncode: return
    d = zipfile.ZipFile(io.BytesIO(r.stdout)).read('word/document.xml').decode('utf8')
    for m in re.finditer(r'<w:p[ >].*?</w:p>', d, re.S):
        t = ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', m.group(0)))
        if t.strip(): corpus.setdefault(norm(t), set()).add(label)

def add_md(path, label):
    if not os.path.exists(path): return
    for ln in open(path, encoding='utf8'):
        if ln.strip(): corpus.setdefault(norm(ln), set()).add(label)

add_docx(os.path.join(OUT, '정다훈(만35세)_AI개발_지오영_(주)피플렙_임덕빈2026.docx'), '지오영 v14 제출본')
add_git_docx('outputs/정다훈(만35세)_AI개발_지오영_(주)피플렙_임덕빈2026.docx', '지오영 v14 커밋본')
add_md(os.path.join(OUT, 'geoyoung-ai-dev-resume-draft.md'), '지오영 md 초안')
add_docx(os.path.join(OUT, '코오롱베니트_플랫폼개발운영_정다훈_써치라인_v4.docx'), '코오롱 v4')
add_md(os.path.join(OUT, 'gs-global-fde-full-resume-draft.md'), 'GS v7')

SEC = None
rows = []          # (section, line, origin, kind)
section_of = {}
kindmap = [
    (re.compile(r'^\|'), 'meta'),
    (re.compile(r'^기술:'), 'meta'),
    (re.compile(r'^\d{4}\.\d{2}'), 'meta'),
    (re.compile(r'^■'), 'meta'),
    (re.compile(r'^○'), 'heading'),
    (re.compile(r'^\*\*\d\.'), 'heading'),
    (re.compile(r'^#'), 'heading'),
]

for raw in open(DRAFT, encoding='utf8'):
    ln = raw.rstrip('\n')
    s = ln.strip()
    if not s: continue
    if s.startswith('### ') or s.startswith('## '):
        SEC = s.lstrip('#').strip()
        continue
    if s.startswith('# '):
        SEC = '문서 헤더'
    if set(s) <= set('|- :'):     # 표 구분선
        continue
    kind = 'prose'
    for rx, k in kindmap:
        if rx.match(s): kind = k; break
    key = norm(s)
    origin = ('재사용(' + '·'.join(sorted(corpus[key])) + ')') if key in corpus else '신규/수정'
    rows.append((SEC or '-', s, origin, kind))

new_rows = [r for r in rows if r[2] == '신규/수정']
reuse_rows = [r for r in rows if r[2] != '신규/수정']

L = []
L.append('# 한미글로벌 AX실 AI 개발 — companion (new-prose) · 2026.09.11\n')
L.append(f'- 전체 콘텐츠 라인: **{len(rows)}**')
L.append(f'- 신규/수정: **{len(new_rows)}** ({len(new_rows)*100//len(rows)}%)')
L.append(f'- 재사용: **{len(reuse_rows)}** ({len(reuse_rows)*100//len(rows)}%)')
L.append(f'- 레인 판정: **{"full lane (신규 작문 50% 초과)" if len(new_rows)*2 > len(rows) else "fast lane 유지 (신규 작문 50% 이하)"}**\n')

L.append('## (a) 신규 작성·수정 산문 (prose)\n')
L.append('| # | 섹션 | 문장 |')
L.append('| --- | --- | --- |')
i = 0
for sec, line, _, kind in new_rows:
    if kind != 'prose': continue
    i += 1
    esc = line.replace('|', '\\|')
    L.append(f'| {i} | {sec} | {esc} |')
L.append('')

L.append('## (b) candidate 상태 은행 문장 재사용\n')
L.append('해당 없음 — 이 초안은 canonical-lines.md 은행이 아니라 지오영 v14 제출본을')
L.append('베이스로 재조립했다. 재사용 출처는 아래 (d)에 전량 표기한다.\n')

L.append('## (c) 신규·변경된 비산문 콘텐츠 라인 (표/헤딩/기술·기간 메타)\n')
L.append('| # | 섹션 | 종류 | 내용 |')
L.append('| --- | --- | --- | --- |')
i = 0
for sec, line, _, kind in new_rows:
    if kind == 'prose': continue
    i += 1
    esc = line.replace('|', '\\|')
    L.append(f'| {i} | {sec} | {kind} | {esc} |')
L.append('')

L.append('## (d) 재사용 라인 (출처 태그)\n')
L.append('| # | 섹션 | 출처 | 내용 |')
L.append('| --- | --- | --- | --- |')
for i, (sec, line, origin, kind) in enumerate(reuse_rows, 1):
    esc = line.replace('|', '\\|')
    L.append(f'| {i} | {sec} | {origin} | {esc} |')

open(COMP, 'w', encoding='utf8').write('\n'.join(L) + '\n')
print(f'wrote {COMP}')
print(f'총 {len(rows)} / 신규 {len(new_rows)} / 재사용 {len(reuse_rows)}')
print('신규 비중 %d%%' % (len(new_rows)*100//len(rows)))
