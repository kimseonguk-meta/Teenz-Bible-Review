#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — 2 Peter (3장)."""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))
KO_SRC = json.load(open('/tmp/ko_15books.json'))
BOOK = '2 Peter'
EN_CH = {c['num']: c for c in EN_SRC[BOOK]}
KO_CH = {c['num']: c for c in KO_SRC[BOOK]}
EN_TITLE = {c['num']: c.get('title', '') for c in EN_SRC[BOOK]}

def E(ch, i): return EN_CH[ch]['paragraphs'][i]
def K(ch, i):
    s = KO_CH[ch]['paragraphs'][i].replace('\\n', '\n')
    return re.sub(r'^\d+(-\d+)?(절)?\.?::?\s*', '', s)

def chap(num, en_paras, ko_paras, splits=None, merges=None, changes=None, confirmations=None):
    vr = [b for _, b in en_paras]
    assert len(en_paras) == len(ko_paras), f'ch{num} EN/KO 문단 수 불일치: {len(en_paras)} vs {len(ko_paras)}'
    assert [b for _, b in ko_paras] == vr, f'ch{num} EN/KO 배지 불일치: {vr} vs {[b for _, b in ko_paras]}'
    base = {'chapter': num, 'title': EN_TITLE[num], 'verseRanges': vr, 'msg_ranges': list(vr),
            'merges': merges or [], 'splits': splits or [],
            'changes': changes or [], 'confirmations_needed': confirmations or []}
    en = dict(base); en['paragraphs'] = [t for t, _ in en_paras]
    ko = dict(base); ko['paragraphs'] = [t for t, _ in ko_paras]
    return en, ko

en_patch, ko_patch = [], []

# ---------------- CH 1 ----------------
en1, ko1 = chap(1,
  [(E(1, 1), '1-2'),
   ("§Don't Put It Off", '3-4'),
   (E(1, 2), '3-4'),
   (E(1, 3), '5-9'),
   (E(1, 4), '10-11'),
   ('§The One Light in a Dark Time', '12-15'),
   (E(1, 5), '12-15'),
   (E(1, 6), '16-18'),
   (E(1, 7), '19-21')],
  [(K(1, 1), '1-2'),
   ('§미루지 마', '3-4'),
   (K(1, 3), '3-4'),
   (K(1, 4), '5-9'),
   (K(1, 5), '10-11'),
   ('§어두운 시절에 만난 한줄기 빛', '12-15'),
   (K(1, 6), '12-15'),
   (K(1, 7), '16-18'),
   (K(1, 9), '19-21')],
  changes=[
    'Ch1: badges already match MSG (1-2 / 3-4 / 5-9 / 10-11 / 12-15 / 16-18 / 19-21)',
    'Ch1: replaced EN-added §Growing in Faith with MSG own header §Don\'t Put It Off (badged 3-4)',
    'Ch1: added MSG own header §The One Light in a Dark Time (badged 12-15) in EN; added § to KO "어두운 시절에 만난 한줄기 빛"',
    'Ch1: removed KO-only headers §믿음 안에서 성장 / "하나님이 주신 진짜 큰 초대장이랑 약속"'])
en_patch.append(en1); ko_patch.append(ko1)

# ---------------- CH 2 ----------------
e68 = ("God decreed destruction for the cities of Sodom and Gomorrah. A mound of ashes was all that was left — "
       "a grim warning to anyone bent on an ungodly life. But that good man Lot, driven nearly out of his mind by "
       "the sexual filth and perversity around him, was rescued. Surrounded by moral rot day after day after day, "
       "that righteous man was in constant torment.")
s2 = [{'msg_range': '2', 'paras': [1, 2],
       'note': 'MSG 1-2 and 2-3 overlap on v2; badges kept as printed in MSG'}]
en2, ko2 = chap(2,
  [('§Lying Religious Leaders', '1-2'),
   (E(2, 1), '1-2'),
   (E(2, 2), '2-3'),
   (E(2, 3), '4-5'),
   (e68, '6-8'),
   (E(2, 4), '9'),
   ('§Predators on the Prowl', '10-11'),
   (E(2, 5), '10-11'),
   (E(2, 6), '12-14'),
   (E(2, 7), '15-16'),
   (E(2, 8), '17-19'),
   (E(2, 9), '20-22')],
  [('§거짓말쟁이 종교 지도자들', '1-2'),
   (K(2, 2), '1-2'),
   (K(2, 3), '2-3'),
   (K(2, 4), '4-5'),
   (K(2, 5), '6-8'),
   (K(2, 6), '9'),
   ('§먹잇감을 노리는 약탈자들', '10-11'),
   (K(2, 8), '10-11'),
   (K(2, 9), '12-14'),
   (K(2, 10), '15-16'),
   (K(2, 11), '17-19'),
   (K(2, 12), '20-22')],
  splits=s2,
  changes=[
    'Ch2: badges already match MSG (1-2 / 2-3 / 4-5 / 6-8 / 9 / 10-11 / 12-14 / 15-16 / 17-19 / 20-22); declared v2 overlap of 1-2 and 2-3 in splits',
    'Ch2: replaced EN-added §False Teachers with MSG own header §Lying Religious Leaders (badged 1-2)',
    'Ch2: restored omitted 6-8 in EN (Sodom and Gomorrah ashes; Lot rescued from filth and perversity)',
    'Ch2: added MSG own header §Predators on the Prowl (badged 10-11) in EN; added § to KO "먹잇감을 노리는 약탈자들"',
    'Ch2: removed KO-only headers §거짓 교사 / §가짜 선생님들 조심해라'])
en_patch.append(en2); ko_patch.append(ko2)

# ---------------- CH 3 ----------------
e1718 = E(3, 8) + ' ' + E(3, 9)
_k310 = K(3, 10)
k1416, k1718 = _k310.split('하지만 친구들아, 너네는 이미 다 배웠잖아.')
k1416 = (K(3, 9) + ' ' + k1416.strip()).strip()
k1718 = ('하지만 친구들아, 너네는 이미 다 배웠잖아.' + k1718).strip()
en3, ko3 = chap(3,
  [('§In the Last Days', '1-2'),
   (E(3, 1), '1-2'),
   (E(3, 2), '3-4'),
   (E(3, 3), '5-7'),
   ('§The Day the Sky Will Collapse', '8-9'),
   (E(3, 4), '8-9'),
   (E(3, 5), '10'),
   (E(3, 6), '11-13'),
   (E(3, 7), '14-16'),
   (e1718, '17-18')],
  [('§마지막 때', '1-2'),
   (K(3, 2), '1-2'),
   (K(3, 3), '3-4'),
   (K(3, 4), '5-7'),
   ('§하나님의 심판날', '8-9'),
   (K(3, 6), '8-9'),
   (K(3, 7), '10'),
   (K(3, 8), '11-13'),
   (k1416, '14-16'),
   (k1718, '17-18')],
  changes=[
    'Ch3: badges already match MSG (1-2 / 3-4 / 5-7 / 8-9 / 10 / 11-13 / 14-16 / 17-18)',
    'Ch3: replaced EN-added §The Day of the Lord with MSG own header §In the Last Days (badged 1-2)',
    'Ch3: added MSG own header §The Day the Sky Will Collapse (badged 8-9) in EN; added § to KO "하나님의 심판날"',
    'Ch3: merged EN over-split 17-18 warning + doxology into single MSG 17-18 para',
    'Ch3: restructured KO: merged Paul part back into 14-16, split 17-18 out as its own para',
    'Ch3: removed KO-only header §주의 날'])
en_patch.append(en3); ko_patch.append(ko3)

outdir = os.path.join(BASE, 'fixes')
json.dump(en_patch, open(os.path.join(outdir, 'en_2Peter.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(ko_patch, open(os.path.join(outdir, 'ko_2Peter.json'), 'w'), ensure_ascii=False, indent=1)
print('written:', len(en_patch), 'chapters')
r = subprocess.run([sys.executable, os.path.join(BASE, 'validate_translation.py'),
                    os.path.join(outdir, 'en_2Peter.json'),
                    os.path.join(outdir, 'ko_2Peter.json')],
                   capture_output=True, text=True)
print(r.stdout, r.stderr)
sys.exit(r.returncode)
