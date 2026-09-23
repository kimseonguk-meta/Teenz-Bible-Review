#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — 2 John + 3 John (각 1장)."""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))
KO_SRC = json.load(open('/tmp/ko_15books.json'))
EN_TITLE = {b: EN_SRC[b][0].get('title', '') for b in ('2 John', '3 John')}

def E(b, i): return EN_SRC[b][0]['paragraphs'][i]
def K(b, i):
    s = KO_SRC[b][0]['paragraphs'][i].replace('\\n', '\n')
    return re.sub(r'^\d+(-\d+)?(절)?\.?::?\s*', '', s)

def chap(book, num, en_paras, ko_paras, splits=None, merges=None, changes=None, confirmations=None):
    vr = [b for _, b in en_paras]
    assert len(en_paras) == len(ko_paras), f'{book} ch{num} EN/KO 문단 수 불일치: {len(en_paras)} vs {len(ko_paras)}'
    assert [b for _, b in ko_paras] == vr, f'{book} ch{num} EN/KO 배지 불일치: {vr} vs {[b for _, b in ko_paras]}'
    base = {'chapter': num, 'title': EN_TITLE[book], 'verseRanges': vr, 'msg_ranges': list(vr),
            'merges': merges or [], 'splits': splits or [],
            'changes': changes or [], 'confirmations_needed': confirmations or []}
    en = dict(base); en['paragraphs'] = [t for t, _ in en_paras]
    ko = dict(base); ko['paragraphs'] = [t for t, _ in ko_paras]
    return en, ko

en_patch, ko_patch = [], []

# ---------------- 2 John ----------------
k3 = ('은혜랑 자비랑 평화가 우리랑 함께 하기를! 하나님 아버지랑 예수 그리스도, 아버지의 아들한테서 오는 진리랑 사랑 안에서 말이야!')
k7 = K('2 John', 5) + ' ' + K('2 John', 4)
k1213 = K('2 John', 8) + ' ' + K('2 John', 9)
en2j, ko2j = chap('2 John', 1,
  [(E('2 John', 1), '1-2'),
   (E('2 John', 2), '3'),
   (E('2 John', 3), '4-6'),
   ("§Don't Walk Out on God", '7'),
   (E('2 John', 4), '7'),
   (E('2 John', 5), '8-9'),
   (E('2 John', 6), '10-11'),
   (E('2 John', 7), '12-13')],
  [(K('2 John', 2), '1-2'),
   (k3, '3'),
   (K('2 John', 3), '4-6'),
   ('§하나님을 버리지 마', '7'),
   (k7, '7'),
   (K('2 John', 6), '8-9'),
   (K('2 John', 7), '10-11'),
   (k1213, '12-13')],
  splits=[{'msg_range': '7', 'note': 'MSG 7 is one para; KO had it split ("속이는 자! 적그리스도!" punchline first); folded back into MSG order'},
          {'msg_range': '12-13', 'note': 'MSG 12-13 is one para; KO sister-congregation greeting folded in'}],
  changes=[
    '2 John: replaced EN-added §Truth and Love with MSG own header §Don\'t Walk Out on God (badged 7)',
    '2 John: restored omitted v3 in KO (grace, mercy, peace from the Father and Jesus Christ)',
    '2 John: folded KO over-splits of 7 and 12-13 back into MSG single paras (splits recorded)',
    '2 John: removed KO-only paras §진리와 사랑 and "요한2서 1장" label'])
en_patch.append(en2j); ko_patch.append(ko2j)

# ---------------- 3 John ----------------
e58 = E('3 John', 2) + ' ' + E('3 John', 3)
e1314a, e1314b = E('3 John', 8).split('Peace to you! ')
e1314b = 'Peace to you! ' + e1314b
_k910 = K('3 John', 3)
k910a, k910b = _k910.split('그걸로도 모자라서, ')
k910b = '그걸로도 모자라서, ' + k910b
_k1314 = K('3 John', 7)
k1314a, k1314b = _k1314.split('평화가 있기를! ')
k1314b = '평화가 있기를! ' + k1314b
en3j, ko3j = chap('3 John', 1,
  [(E('3 John', 0), '1-4'),
   ('§Model the Good', '5-8'),
   (e58, '5-8'),
   (E('3 John', 4), '9-10'),
   (E('3 John', 5), '9-10'),
   (E('3 John', 6), '11'),
   (E('3 John', 7), '12'),
   (e1314a.strip(), '13-14'),
   (e1314b.strip(), '13-14')],
  [(K('3 John', 1), '1-4'),
   ('§선을 본받자', '5-8'),
   (K('3 John', 2), '5-8'),
   (k910a.strip(), '9-10'),
   (k910b.strip(), '9-10'),
   (K('3 John', 5), '11'),
   (K('3 John', 6), '12'),
   (k1314a.strip(), '13-14'),
   (k1314b.strip(), '13-14')],
  splits=[{'msg_range': '9-10', 'paras': [3, 4], 'note': 'MSG prints 9-10 as two paras (rumors / hospitality refusal)'},
          {'msg_range': '13-14', 'paras': [7, 8], 'note': 'MSG prints 13-14 as two paras (paper-and-ink / peace greeting)'}],
  merges=[{'msg_range': '5-8', 'paras': [2], 'note': 'EN had over-split MSG single 5-8 para into two; merged back'}],
  changes=[
    '3 John: replaced EN-added §Support the Travelers with MSG own header §Model the Good (badged 5-8)',
    '3 John: merged EN over-split 5-8 back into MSG single para (merges recorded)',
    '3 John: split KO 9-10 and 13-14 into MSG two-para structure (splits recorded)',
    '3 John: moved misplaced KO §선을 본받자 from before 11 to its MSG position before 5-8; removed KO-only §동역자들을 돕다'])
en_patch.append(en3j); ko_patch.append(ko3j)

outdir = os.path.join(BASE, 'fixes')
json.dump([en2j], open(os.path.join(outdir, 'en_2John.json'), 'w'), ensure_ascii=False, indent=1)
json.dump([ko2j], open(os.path.join(outdir, 'ko_2John.json'), 'w'), ensure_ascii=False, indent=1)
json.dump([en3j], open(os.path.join(outdir, 'en_3John.json'), 'w'), ensure_ascii=False, indent=1)
json.dump([ko3j], open(os.path.join(outdir, 'ko_3John.json'), 'w'), ensure_ascii=False, indent=1)
ok = True
for pair in [('en_2John.json', 'ko_2John.json'), ('en_3John.json', 'ko_3John.json')]:
    r = subprocess.run([sys.executable, os.path.join(BASE, 'validate_translation.py'),
                        os.path.join(outdir, pair[0]), os.path.join(outdir, pair[1])],
                       capture_output=True, text=True)
    print(pair[0], '->', r.stdout.strip(), r.stderr.strip())
    ok = ok and r.returncode == 0
sys.exit(0 if ok else 1)
