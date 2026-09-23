#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — 1 Thessalonians.
사용법: python3 build_1thess.py  (fixes/en_1Thessalonians.json, fixes/ko_1Thessalonians.json 생성 후 검증)
"""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))
KO_SRC = json.load(open('/tmp/ko_15books.json'))
BOOK = '1 Thessalonians'
EN_CH = {c['num']: c for c in EN_SRC[BOOK]}
KO_CH = {c['num']: c for c in KO_SRC[BOOK]}
EN_TITLE = {c['num']: c.get('title', '') for c in EN_SRC[BOOK]}

def E(ch, i):
    return EN_CH[ch]['paragraphs'][i]

def K(ch, i):
    t = KO_CH[ch]['paragraphs'][i]
    return re.sub(r'^\d+(-\d+)?\s*\n', '', t)  # "1-3\n" 같은 절 라벨 접두 제거

def chap(num, en_paras, ko_paras, splits=None, merges=None, changes=None, confirmations=None):
    vr = [b for _, b in en_paras]
    assert len(en_paras) == len(ko_paras), f'ch{num} EN/KO 문단 수 불일치'
    assert [b for _, b in ko_paras] == vr, f'ch{num} EN/KO 배지 불일치'
    en = {'chapter': num, 'title': EN_TITLE[num],
          'paragraphs': [t for t, _ in en_paras], 'verseRanges': vr,
          'msg_ranges': list(vr),
          'merges': merges or [], 'splits': splits or [],
          'changes': changes or [], 'confirmations_needed': confirmations or []}
    ko = {'chapter': num, 'title': EN_TITLE[num],
          'paragraphs': [t for t, _ in ko_paras], 'verseRanges': list(vr),
          'msg_ranges': list(vr),
          'merges': merges or [], 'splits': splits or [],
          'changes': changes or [], 'confirmations_needed': confirmations or []}
    return en, ko

en_patch, ko_patch = [], []

# ---------------- CH 1 ----------------
split5 = [{'msg_range': '5', 'paras': [3, 4],
           'note': 'MSG prints 2-5 then 5-6 (overlap on v5); badges kept as printed in MSG'}]
en1, ko1 = chap(1,
  [('§Thankful for You', '1'),
   (E(1, 1), '1'),
   ('§Convictions of Steel', '2-5'),
   (E(1, 2), '2-5'),
   (E(1, 3), '5-6'),
   (E(1, 4), '7-10')],
  [('§너희에게 감사하다', '1'),
   (K(1, 1), '1'),
   ('§강철 같은 확신', '2-5'),
   (K(1, 3) + ' ' + K(1, 4), '2-5'),
   (K(1, 5), '5-6'),
   (K(1, 6) + ' ' + K(1, 7), '7-10')],
  splits=split5,
  changes=[
    'Ch1: badges corrected to MSG (1 / 2-5 / 5-6 / 7-10); §Thankful for You now badged 1 (shares with greeting para)',
    'Ch1: added §Convictions of Steel header before 2-5 (MSG own section title; matches existing KO §강철 같은 확신 header)',
    'Ch1: KO merged into 6 paragraphs 1:1 with EN (was 8; KO-only splits of MSG 2-5 and 7-10 rejoined)',
    'Ch1: EN content verified complete vs MSG — no restoration needed'])
en_patch.append(en1); ko_patch.append(ko1)

# ---------------- CH 2 ----------------
en2, ko2 = chap(2,
  [('§Paul\'s Ministry', '1-2'),
   (E(2, 1), '1-2'), (E(2, 2), '3-5'), (E(2, 3), '6-8'),
   (E(2, 4), '9-12'), (E(2, 5), '13'), (E(2, 6), '14-16'), (E(2, 7), '17-20')],
  [('§바울의 사역', '1-2'),
   (K(2, 1), '1-2'), (K(2, 2), '3-5'), (K(2, 3), '6-8'),
   (K(2, 4), '9-12'), (K(2, 5), '13'), (K(2, 6), '14-16'), (K(2, 7), '17-20')],
  changes=[
    'Ch2: badges corrected to MSG (1-2 / 3-5 / 6-8 / 9-12 / 13 / 14-16 / 17-20); v13 para rebadged 13 (was 13-14)',
    'Ch2: EN content verified complete vs MSG (Philippi rough treatment, mother/father care, Judea churches, Satan blocking) — no restoration needed'])
en_patch.append(en2); ko_patch.append(ko2)

# ---------------- CH 3 ----------------
en3, ko3 = chap(3,
  [('§Encouraged by Your Faith', '1-2'),
   (E(3, 1), '1-2'), (E(3, 2), '3-5'), (E(3, 3), '6-8'),
   (E(3, 4), '9-10'), (E(3, 5), '11-13')],
  [('§하나님을 기쁘시게', '1-2'),
   (K(3, 1), '1-2'), (K(3, 2), '3-5'), (K(3, 3), '6-8'),
   (K(3, 4), '9-10'), (K(3, 5), '11-13')],
  changes=[
    'Ch3: badges corrected to MSG (1-2 / 3-5 / 6-8 / 9-10 / 11-13)',
    'Ch3: EN content verified complete vs MSG (Athens/Timothy, Tempter warning, "faith alive keeps us alive", clear-the-road prayer) — no restoration needed'])
en_patch.append(en3); ko_patch.append(ko3)

# ---------------- CH 4 ----------------
p45 = "Basically, have some self-respect. Your body is a temple, not a trash can, so don't treat it like people who don't even know God."
p67 = "Don't be mean to your friends and family or step on them to get ahead. God sees that, and trust me, He'll handle it. We've told you before, God didn't call us to be messy and horrible. He's calling us to a powerful shift, inside and out."
en4, ko4 = chap(4,
  [('§Live to Please God', '1-3'),
   (E(4, 1), '1-3'),
   (p45, '4-5'),
   ('§God Called You to Be Holy', '6-7'),
   (p67, '6-7'),
   (E(4, 4), '8'),
   (E(4, 5), '9-10'),
   (E(4, 6), '11-12'),
   ('§The Master\'s Coming', '13-14'),
   (E(4, 7), '13-14'),
   (E(4, 8), '15-18')],
  [('§하나님을 기쁘게 해드리는 법', '1-3'),
   (K(4, 1), '1-3'),
   (K(4, 2), '4-5'),
   ('§준비하고 있어', '6-7'),
   (K(4, 4), '6-7'),
   (K(4, 5), '8'),
   (K(4, 6), '9-10'),
   (K(4, 7), '11-12'),
   ('§주님의 재림과 죽은 자의 부활', '13-14'),
   (K(4, 9), '13-14'),
   (K(4, 10), '15-18')],
  changes=[
    'Ch4: split the old merged 3-6 para into 4-5 (body dignity) and 6-7 (don\'t trample others) — now 1:1 with MSG and KO',
    'Ch4: §God Called You to Be Holy moved before 6-7 (badge 6-7); added §The Master\'s Coming before 13-14 (MSG section header; matches KO)',
    'Ch4: KO header badges fixed (added § to 하나님을 기쁘게 해드리는 법 / 주님의 재림과 죽은 자의 부활), embedded "N-M" line prefixes stripped',
    'Ch4: EN content verified complete vs MSG (victory dance, sexual promiscuity, holy-beautiful life, archangel thunder) — no restoration needed'])
en_patch.append(en4); ko_patch.append(ko4)

# ---------------- CH 5 ----------------
p13_new = ('Hey, what\'s up, guys? So, about when all this crazy end-of-the-world stuff is gonna go down... '
 'honestly, I don\'t even need to get into it. You already know the deal. The Master\'s return isn\'t something '
 'you can just mark on your calendar. He\'s not gonna send you a message with a heads-up. It\'s gonna be more '
 'like a thief in the night \u2014 totally random. Just when everyone\'s chilling, thinking, "We\'re so set, life is good," '
 'BAM! Everything goes sideways. It\'ll hit as suddenly and inescapably as labor pains hitting a pregnant woman.')
split13 = [{'msg_range': '13', 'paras': [5, 6],
            'note': 'MSG prints 12-13 then 13-15 (overlap on v13); badges kept as printed in MSG'}]
en5, ko5 = chap(5,
  [('§The Day of the Lord', '1-3'),
   (p13_new, '1-3'),
   (E(5, 2), '4-8'),
   (E(5, 3), '9-11'),
   ('§The Way He Wants You to Live', '12-13'),
   (E(5, 4), '12-13'),
   (E(5, 5), '13-15'),
   (E(5, 6), '16-18'),
   (E(5, 7), '19-22'),
   (E(5, 8), '23-24'),
   (E(5, 9), '25-27'),
   (E(5, 10), '28')],
  [('§마지막 지시', '1-3'),
   (K(5, 1), '1-3'),
   (K(5, 2), '4-8'),
   (K(5, 3), '9-11'),
   ('§하나님이 원하시는 라이프스타일', '12-13'),
   (K(5, 5), '12-13'),
   (K(5, 6), '13-15'),
   (K(5, 7), '16-18'),
   (K(5, 8), '19-22'),
   (K(5, 9), '23-24'),
   (K(5, 10), '25-27'),
   (K(5, 11), '28')],
  splits=split13,
  changes=[
    'Ch5: badges corrected to MSG (1-3 / 4-8 / 9-11 / 12-13 / 13-15 / 16-18 / 19-22 / 23-24 / 25-27 / 28)',
    'Ch5: restored MSG 1-3 birth-pangs metaphor in EN ("as suddenly and inescapably as labor pains hitting a pregnant woman") — was replaced by "pop quiz"',
    'Ch5: added §The Way He Wants You to Live header before 12-13 (MSG section header; matches KO §하나님이 원하시는 라이프스타일)',
    'Ch5: KO embedded "N-M" line prefixes stripped; § added to 하나님이 원하시는 라이프스타일'])
en_patch.append(en5); ko_patch.append(ko5)

# ---------------- write & validate ----------------
outdir = os.path.join(BASE, 'fixes')
json.dump(en_patch, open(os.path.join(outdir, 'en_1Thessalonians.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(ko_patch, open(os.path.join(outdir, 'ko_1Thessalonians.json'), 'w'), ensure_ascii=False, indent=1)
print('written:', len(en_patch), 'chapters')
r = subprocess.run([sys.executable, os.path.join(BASE, 'validate_translation.py'),
                    os.path.join(outdir, 'en_1Thessalonians.json'),
                    os.path.join(outdir, 'ko_1Thessalonians.json')],
                   capture_output=True, text=True)
print(r.stdout, r.stderr)
sys.exit(r.returncode)
