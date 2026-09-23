#!/usr/bin/env python3
"""Parse MSG cache files (msg_<Book>.txt) into chapter -> [[range, text]] paragraphs.
Rules:
- two-token "A B text": new chapter iff A == cur+1 (else warning).
- one-token "N text": new chapter iff N == cur+1 AND expected > verse_count[cur]
  (i.e. current chapter already complete); elif N == expected -> verse N of cur;
  else warning.
- bare "R text": verse paragraph of cur, expected = max(R)+1.
- "? ..." line: continuation appended to previous paragraph text.
- "* * *" separators and "#" comments and blanks are skipped.
After parsing, verifies each chapter covers exactly 1..verse_count.
Usage: parse_msg.py <Book>  (reads msg_<Book>.txt, verse counts from /tmp/<book>_vc.json)
Writes msg_paras_<Book>.json
"""
import re, json, sys

BOOK = sys.argv[1]
VC = json.load(open(f'/tmp/{BOOK.lower()}_vc.json'))

two = re.compile(r'^(\d+)\s+(\d[\d\-,]*)\s+(.*)$')
one = re.compile(r'^(\d+)\s+(?=[A-Z*"\u201c\u2018(\u00bf\xa1])')
bare = re.compile(r'^(\d[\d\-,]*)\s+(.*)$')
qline = re.compile(r'^\?\s?(.*)$')
sep = re.compile(r'^\*\s*\*\s*\*$')

def rng_max(r):
    m = 0
    for part in str(r).split(','):
        part = part.strip()
        if '-' in part:
            m = max(m, int(part.split('-')[1]))
        elif part.isdigit():
            m = max(m, int(part))
    return m

def rng_cover(r):
    out = set()
    for part in str(r).split(','):
        part = part.strip()
        if '-' in part:
            a, b = part.split('-')
            out.update(range(int(a), int(b) + 1))
        elif part.isdigit():
            out.add(int(part))
    return out

chapters = []
cur = None
paras = []
expected = 1
warnings = []
n_sep = 0
n_q = 0

def close_chapter():
    global cur, paras, expected
    if cur is not None:
        chapters.append({'chapter': cur, 'paras': paras})
    cur = None; paras = []; expected = 1

for ln in open(f'msg_{BOOK}.txt', encoding='utf-8').read().split('\n'):
    s = ln.strip()
    if not s or s.startswith('#'):
        continue
    if sep.fullmatch(s):
        n_sep += 1
        continue
    mq = qline.match(ln)
    if mq:
        if paras:
            paras[-1][1] += ' ' + mq.group(1).strip()
            n_q += 1
        else:
            warnings.append(f'?-line with no previous para: {ln[:60]}')
        continue
    m = two.match(ln)
    if m:
        n1, n2, text = int(m.group(1)), m.group(2), m.group(3).strip()
        if cur is None or n1 == cur + 1:
            close_chapter()
            cur = n1
            paras = [[n2, text]]
            expected = rng_max(n2) + 1
        else:
            warnings.append(f'two-token non-transition: [{n1} {n2}] {text[:50]} (cur={cur})')
        continue
    m = one.match(ln)
    if m:
        n = int(m.group(1))
        text = ln.split(None, 1)[1].strip()
        if cur is None:
            cur = n
            paras = [['1', text]]
            expected = 2
        elif n == cur + 1 and expected > VC[str(cur)]:
            close_chapter()
            cur = n
            paras = [['1', text]]
            expected = 2
        elif n == expected:
            paras.append([str(n), text])
            expected = n + 1
        else:
            warnings.append(f'one-token ambiguous: [{n}] {text[:50]} (cur={cur}, expected={expected})')
        continue
    m = bare.match(ln)
    if m:
        r, text = m.group(1), m.group(2).strip()
        if cur is None:
            warnings.append(f'bare range before any chapter: [{r}]')
            continue
        paras.append([r, text])
        expected = rng_max(r) + 1
        continue
    # plain continuation line -> append to previous paragraph
    if paras and cur is not None:
        paras[-1][1] += ' ' + s
    else:
        warnings.append(f'stray line: {ln[:60]}')

close_chapter()

# verify coverage
cov_problems = []
for ch in chapters:
    c = ch['chapter']
    cov = set()
    for r, t in ch['paras']:
        cov |= rng_cover(r)
    want = set(range(1, VC[str(c)] + 1))
    if cov != want:
        missing = sorted(want - cov)
        extra = sorted(cov - want)
        cov_problems.append({'chapter': c, 'missing': missing, 'extra': extra,
                             'ranges': [r for r, t in ch['paras']]})

print(f'book={BOOK} chapters={len(chapters)} seps={n_sep} qlines={n_q} warnings={len(warnings)} cov_problems={len(cov_problems)}')
for w in warnings[:20]:
    print('WARN:', w)
for cp in cov_problems[:20]:
    print('COV:', cp)

json.dump(chapters, open(f'msg_paras_{BOOK}.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('wrote', f'msg_paras_{BOOK}.json')
