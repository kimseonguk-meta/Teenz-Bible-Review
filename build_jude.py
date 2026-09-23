#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — Jude (1장)."""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))['Jude'][0]
KO_SRC = json.load(open('/tmp/ko_15books.json'))['Jude'][0]
TITLE = EN_SRC.get('title', '')

def E(i): return EN_SRC['paragraphs'][i]
def K(i):
    s = KO_SRC['paragraphs'][i].replace('\\n', '\n')
    return re.sub(r'^\d+(-\d+)?(절)?\.?::?\s*', '', s)

e34 = E(2) + ' ' + E(3)
e57 = E(5) + ' ' + E(6)
e911 = E(8) + ' ' + E(9)
e1416 = E(11) + ' ' + E(12)

en_paras = [
    (E(1), '1-2'),
    ('§Fight with All You Have in You', '3-4'),
    (e34, '3-4'),
    ('§Lost Stars in Outer Space', '5-7'),
    (e57, '5-7'),
    (E(7), '8'),
    (e911, '9-11'),
    (E(10), '12-13'),
    (e1416, '14-16'),
    (E(13), '17-19'),
    (E(14), '20-21'),
    (E(15), '22-23'),
    (E(16), '24-25')]
ko_paras = [
    (K(1), '1-2'),
    ('§모든 걸 걸고 싸워!', '3-4'),
    (K(3), '3-4'),
    ('§우주 미아가 된 별들', '5-7'),
    (K(5), '5-7'),
    (K(6), '8'),
    (K(7), '9-11'),
    (K(9), '12-13'),
    (K(10), '14-16'),
    (K(11), '17-19'),
    (K(12), '20-21'),
    (K(13), '22-23'),
    (K(14), '24-25')]

vr = [b for _, b in en_paras]
assert len(en_paras) == len(ko_paras), f'EN/KO 문단 수 불일치: {len(en_paras)} vs {len(ko_paras)}'
assert [b for _, b in ko_paras] == vr, f'EN/KO 배지 불일치: {vr} vs {[b for _, b in ko_paras]}'
merges = [{'msg_range': r, 'paras': [i], 'note': 'EN had over-split MSG single para into two; folded back'}
          for r, i in [('3-4', 2), ('5-7', 4), ('9-11', 6), ('14-16', 8)]]
base = {'chapter': 1, 'title': TITLE, 'verseRanges': vr, 'msg_ranges': list(vr),
        'merges': merges, 'splits': [],
        'changes': [
            'Jude: folded EN over-splits of MSG single paras 3-4, 5-7, 9-11, 14-16 back into single paras (merges recorded)',
            'Jude: replaced EN-added §Contend for the Faith with MSG own header §Fight with All You Have in You (badged 3-4)',
            'Jude: replaced EN-added §Remember the Examples with MSG own header §Lost Stars in Outer Space (badged 5-7)',
            'Jude: moved misplaced KO "우주 미아가 된 별들" from before 12-13 to its MSG position before 5-7, added §',
            'Jude: added § to KO "모든 걸 걸고 싸워!" (badged 3-4); removed KO-only headers §믿음을 위해 싸우라 / §경고의 예들을 기억하자'],
        'confirmations_needed': []}
en = dict(base); en['paragraphs'] = [t for t, _ in en_paras]
ko = dict(base); ko['paragraphs'] = [t for t, _ in ko_paras]

outdir = os.path.join(BASE, 'fixes')
json.dump([en], open(os.path.join(outdir, 'en_Jude.json'), 'w'), ensure_ascii=False, indent=1)
json.dump([ko], open(os.path.join(outdir, 'ko_Jude.json'), 'w'), ensure_ascii=False, indent=1)
r = subprocess.run([sys.executable, os.path.join(BASE, 'validate_translation.py'),
                    os.path.join(outdir, 'en_Jude.json'),
                    os.path.join(outdir, 'ko_Jude.json')],
                   capture_output=True, text=True)
print(r.stdout, r.stderr)
sys.exit(r.returncode)
