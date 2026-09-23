#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — Titus."""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))
KO_SRC = json.load(open('/tmp/ko_15books.json'))
BOOK = 'Titus'
EN_CH = {c['num']: c for c in EN_SRC[BOOK]}
KO_CH = {c['num']: c for c in KO_SRC[BOOK]}
EN_TITLE = {c['num']: c.get('title', '') for c in EN_SRC[BOOK]}

def E(ch, i): return EN_CH[ch]['paragraphs'][i]
def K(ch, i):
    return re.sub(r'^\d+(-\d+)?(절)?:\s*', '', KO_CH[ch]['paragraphs'][i])

def chap(num, en_paras, ko_paras, splits=None, merges=None, changes=None, confirmations=None):
    vr = [b for _, b in en_paras]
    assert len(en_paras) == len(ko_paras), f'ch{num} EN/KO 문단 수 불일치'
    assert [b for _, b in ko_paras] == vr, f'ch{num} EN/KO 배지 불일치'
    en = {'chapter': num, 'title': EN_TITLE[num],
          'paragraphs': [t for t, _ in en_paras], 'verseRanges': vr, 'msg_ranges': list(vr),
          'merges': merges or [], 'splits': splits or [],
          'changes': changes or [], 'confirmations_needed': confirmations or []}
    ko = {'chapter': num, 'title': EN_TITLE[num],
          'paragraphs': [t for t, _ in ko_paras], 'verseRanges': list(vr), 'msg_ranges': list(vr),
          'merges': merges or [], 'splits': splits or [],
          'changes': changes or [], 'confirmations_needed': confirmations or []}
    return en, ko

en_patch, ko_patch = [], []

# ---------------- CH 1 ----------------
p59 = E(1, 2).replace('smart, fair, and have his act together.',
                      'smart, fair, reverent, and have his act together.')
en1, ko1 = chap(1,
  [(E(1, 1), '1-4'),
   ('§A Good Grip on the Message', '5-9'),
   (p59, '5-9'),
   (E(1, 3), '10-16')],
  [(K(1, 2), '1-4'),
   ('§메시지를 단단히 붙잡아라', '5-9'),
   (K(1, 4), '5-9'),
   (K(1, 5), '10-16')],
  changes=[
    'Ch1: badges already match MSG (1-4 / 5-9 / 10-16)',
    'Ch1: replaced EN-added §Qualifications for Leaders with MSG own header §A Good Grip on the Message (badged 5-9)',
    'Ch1: replaced KO-only headers §지도자의 자격 / "디도서 1장" / "크레타에서의 디도의 사역" with §메시지를 단단히 붙잡아라 (badged 5-9)',
    'Ch1: restored "reverent" in EN 5-9 leader list (MSG "wise, fair, reverent")'])
en_patch.append(en1); ko_patch.append(ko1)

# ---------------- CH 2 ----------------
en2, ko2 = chap(2,
  [('§A God-Filled Life', '1-6'),
   (E(2, 1), '1-6'),
   (E(2, 2), '7-8'),
   (E(2, 3), '9-10'),
   (E(2, 4), '11-14'),
   (E(2, 5), '15')],
  [('§하나님으로 가득 찬 삶', '1-6'),
   (K(2, 2), '1-6'),
   (K(2, 3), '7-8'),
   (K(2, 4), '9-10'),
   (K(2, 5), '11-14'),
   (K(2, 6), '15')],
  changes=[
    'Ch2: badges corrected to MSG (1-6 / 7-8 / 9-10 / 11-14 / 15)',
    'Ch2: replaced EN-added §Teaching Sound Doctrine with MSG own header §A God-Filled Life (badged 1-6)',
    'Ch2: replaced KO-only headers §바른 교훈을 가르치다 / "하나님으로 꽉 찬 삶" with §하나님으로 가득 찬 삶 (badged 1-6)',
    'Ch2: EN content verified complete vs MSG — no restoration needed'])
en_patch.append(en2); ko_patch.append(ko2)

# ---------------- CH 3 ----------------
p15 = "Everyone here says 'sup. Give a shout-out to all our friends in the faith. Grace to all of you."
split3 = [{'msg_range': '8', 'paras': [2, 3],
           'note': 'MSG 3-8 and 8-11 overlap on v8; badges kept as printed in MSG'}]
en3, ko3 = chap(3,
  [('§He Put Our Lives Together', '1-2'),
   (E(3, 1), '1-2'),
   (E(3, 2), '3-8'),
   (E(3, 3), '8-11'),
   (E(3, 4), '12-13'),
   (E(3, 5), '14'),
   (p15, '15')],
  [('§우리 삶을 하나로 모으셨다', '1-2'),
   (K(3, 2), '1-2'),
   (K(3, 3), '3-8'),
   (K(3, 4), '8-11'),
   (K(3, 5), '12-13'),
   (K(3, 6), '14'),
   (K(3, 7), '15')],
  splits=split3,
  changes=[
    'Ch3: badges corrected to MSG (1-2 / 3-8 / 8-11 / 12-13 / 14 / 15); declared v8 overlap of 3-8 and 8-11 in splits',
    'Ch3: replaced EN-added §Doing Good with MSG own header §He Put Our Lives Together (badged 1-2)',
    'Ch3: replaced KO-only headers §선을 행하라 / "우리 삶을 완전 조화롭게 만드신 구주 하나님" with §우리 삶을 하나로 모으셨다 (badged 1-2)',
    'Ch3: restored MSG closing "Grace to all of you" in EN 15 (was "Grace and peace to all of you")'])
en_patch.append(en3); ko_patch.append(ko3)

outdir = os.path.join(BASE, 'fixes')
json.dump(en_patch, open(os.path.join(outdir, 'en_Titus.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(ko_patch, open(os.path.join(outdir, 'ko_Titus.json'), 'w'), ensure_ascii=False, indent=1)
print('written:', len(en_patch), 'chapters')
r = subprocess.run([sys.executable, os.path.join(BASE, 'validate_translation.py'),
                    os.path.join(outdir, 'en_Titus.json'),
                    os.path.join(outdir, 'ko_Titus.json')],
                   capture_output=True, text=True)
print(r.stdout, r.stderr)
sys.exit(r.returncode)
