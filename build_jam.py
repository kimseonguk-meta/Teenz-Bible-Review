#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — James (5장)."""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))
KO_SRC = json.load(open('/tmp/ko_15books.json'))
BOOK = 'James'
EN_CH = {c['num']: c for c in EN_SRC[BOOK]}
KO_CH = {c['num']: c for c in KO_SRC[BOOK]}
EN_TITLE = {c['num']: c.get('title', '') for c in EN_SRC[BOOK]}

def E(ch, i): return EN_CH[ch]['paragraphs'][i]
def K(ch, i):
    return re.sub(r'^\d+(-\d+)?(절)?\.?::?\s*', '', KO_CH[ch]['paragraphs'][i])

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
greet1 = E(1, 1) + ' Hello!'
e1921 = E(1, 8).replace('make your life a masterpiece. Let His Word take root in you and save you.',
                        'landscape your life with the Word, making a salvation-garden of your life.')
e2224, _ = E(1, 9).split('If you actually pay attention')
e2224 = e2224.rstrip()
e25 = ("But whoever catches a glimpse of God's revealed counsel — the free life! — even out of the corner of "
       "their eye, and sticks with it, is no distracted scatterbrain but a person of action. That person will "
       "find delight and affirmation in the action.")
en1, ko1 = chap(1,
  [(greet1, '1'),
   ('§Faith Under Pressure', '2-4'),
   (E(1, 2), '2-4'),
   (E(1, 3), '5-8'),
   (E(1, 4), '9-11'),
   (E(1, 5), '12'),
   (E(1, 6), '13-15'),
   (E(1, 7), '16-18'),
   ('§Act on What You Hear', '19-21'),
   (e1921, '19-21'),
   (e2224, '22-24'),
   (e25, '25'),
   (E(1, 10), '26-27')],
  [(K(1, 1), '1'),
   ('§힘든 시련을 버티는 믿음', '2-4'),
   (K(1, 3), '2-4'),
   (K(1, 4), '5-8'),
   (K(1, 5), '9-11'),
   (K(1, 6), '12'),
   (K(1, 7), '13-15'),
   (K(1, 8), '16-18'),
   ('§들은 대로 바로 실행 가자', '19-21'),
   (K(1, 10), '19-21'),
   (K(1, 11), '22-24'),
   (K(1, 12), '25'),
   (K(1, 13), '26-27')],
  changes=[
    'Ch1: badges corrected to MSG (1 / 2-4 / 5-8 / 9-11 / 12 / 13-15 / 16-18 / 19-21 / 22-24 / 25 / 26-27)',
    'Ch1: removed EN-added §Trials and Temptation (MSG has no header before 1:1); added MSG own header §Faith Under Pressure (badged 2-4)',
    'Ch1: added MSG own header §Act on What You Hear (badged 19-21) in EN and KO',
    'Ch1: split EN merged 22-24+25 para into MSG\'s 22-24 and 25 paras (v25 was folded into 22-24)',
    'Ch1: restored "Hello!" in EN greeting 1',
    'Ch1: restored "making a salvation-garden of your life" in EN 19-21 (was "make your life a masterpiece")',
    'Ch1: removed KO-only header §시련과 유혹'])
en_patch.append(en1); ko_patch.append(ko1)

# ---------------- CH 2 ----------------
en2, ko2 = chap(2,
  [('§The Royal Rule of Love', '1-4'),
   (E(2, 1), '1-4'),
   (E(2, 2), '5-7'),
   (E(2, 3), '8-11'),
   (E(2, 4), '12-13'),
   ('§Faith in Action', '14-17'),
   (E(2, 5), '14-17'),
   (E(2, 6), '18'),
   (E(2, 7), '19-20'),
   (E(2, 8), '21-24'),
   (E(2, 9), '25-26')],
  [('§사랑이라는 고귀한 법', '1-4'),
   (K(2, 2), '1-4'),
   (K(2, 3), '5-7'),
   (K(2, 4), '8-11'),
   (K(2, 5), '12-13'),
   ('§행함이 있는 믿음', '14-17'),
   (K(2, 7), '14-17'),
   (K(2, 8), '18'),
   (K(2, 9), '19-20'),
   (K(2, 10), '21-24'),
   (K(2, 11), '25-26')],
  changes=[
    'Ch2: badges already match MSG (1-4 / 5-7 / 8-11 / 12-13 / 14-17 / 18 / 19-20 / 21-24 / 25-26)',
    'Ch2: replaced EN-added §Faith and Actions with MSG own header §The Royal Rule of Love (badged 1-4)',
    'Ch2: added MSG own header §Faith in Action (badged 14-17) in EN and KO',
    'Ch2: replaced KO-only headers §믿음과 행동 with §사랑이라는 고귀한 법 (badged 1-4)'])
en_patch.append(en2); ko_patch.append(ko2)

# ---------------- CH 3 ----------------
e35, e56 = E(3, 2).split('It just takes one little spark')
e56 = 'It just takes one little spark' + e56
e710, e1012 = E(3, 3).split('Seriously, my guys,')
e1012 = ('Seriously, my friends, this can\'t go on. A spring doesn\'t gush fresh water one day and brackish the '
         'next, right? Apple trees don\'t bear strawberries, and raspberry bushes don\'t bear apples. You\'re not '
         'going to dip into a polluted mud hole and get a cup of clear, cool water, are you?')
e710 = e710.rstrip()
s3 = [{'msg_range': '5', 'paras': [2, 3],
       'note': 'MSG 3-5 and 5-6 overlap on v5; badges kept as printed in MSG'},
      {'msg_range': '10', 'paras': [4, 5],
       'note': 'MSG 7-10 and 10-12 overlap on v10; badges kept as printed in MSG'}]
en3, ko3 = chap(3,
  [('§When You Open Your Mouth', '1-2'),
   (E(3, 1), '1-2'),
   (e35.rstrip(), '3-5'),
   (e56, '5-6'),
   (e710, '7-10'),
   (e1012, '10-12'),
   ('§Live Well, Live Wisely', '13-16'),
   (E(3, 4), '13-16'),
   (E(3, 5), '17-18')],
  [('§입을 열 때', '1-2'),
   (K(3, 2), '1-2'),
   (K(3, 3), '3-5'),
   (K(3, 4), '5-6'),
   (K(3, 5), '7-10'),
   (K(3, 6), '10-12'),
   ('§잘 살아라, 지혜롭게 살아라', '13-16'),
   (K(3, 8), '13-16'),
   (K(3, 9), '17-18')],
  splits=s3,
  changes=[
    'Ch3: badges corrected to MSG (1-2 / 3-5 / 5-6 / 7-10 / 10-12 / 13-16 / 17-18); declared v5 and v10 overlaps in splits',
    'Ch3: replaced EN-added §Taming the Tongue with MSG own header §When You Open Your Mouth (badged 1-2)',
    'Ch3: added MSG own header §Live Well, Live Wisely (badged 13-16) in EN and KO',
    'Ch3: split EN merged 3-6 para into MSG\'s 3-5 (horse/rudder) and 5-6 (spark/forest fire) paras',
    'Ch3: split EN merged 7-12 para into MSG\'s 7-10 (untamable tongue) and 10-12 (spring/trees) paras; restored omitted raspberry bushes and mud-hole cup in EN 10-12',
    'Ch3: removed KO-only headers §혀를 다스리라 / §말의 힘, 이거 완전 놀라워 / §진짜 지혜'])
en_patch.append(en3); ko_patch.append(ko3)

# ---------------- CH 4 ----------------
s4 = [{'msg_range': '2', 'paras': [1, 2],
       'note': 'MSG 1-2 and 2-3 overlap on v2; badges kept as printed in MSG'}]
en4, ko4 = chap(4,
  [('§Get Serious', '1-2'),
   (E(4, 1), '1-2'),
   (E(4, 2), '2-3'),
   (E(4, 4), '4-6'),
   (E(4, 5), '7-10'),
   (E(4, 6), '11-12'),
   ('§Nothing but a Wisp of Fog', '13-15'),
   (E(4, 7), '13-15'),
   (E(4, 8), '16-17')],
  [('§진지해져라', '1-2'),
   (K(4, 2), '1-2'),
   (K(4, 3), '2-3'),
   (K(4, 5), '4-6'),
   (K(4, 6), '7-10'),
   (K(4, 7), '11-12'),
   ('§한줌 안개 같은 인생', '13-15'),
   (K(4, 9), '13-15'),
   (K(4, 10), '16-17')],
  splits=s4,
  changes=[
    'Ch4: badges already match MSG (1-2 / 2-3 / 4-6 / 7-10 / 11-12 / 13-15 / 16-17); declared v2 overlap of 1-2 and 2-3 in splits',
    'Ch4: replaced EN-added §Get Serious with God with MSG own header §Get Serious (badged 1-2)',
    'Ch4: removed EN-added §Pick a Side (MSG has no header there)',
    'Ch4: added MSG own header §Nothing but a Wisp of Fog (badged 13-15) in EN and KO',
    'Ch4: removed KO-only headers §하나님께 진지해져라 / "하나님 뜻대로 사는 삶" / §편을 골라라'])
en_patch.append(en4); ko_patch.append(ko4)

# ---------------- CH 5 ----------------
e1315 = E(5, 8).replace("get your church's distinguished leaders to pray for you.",
                        "get your church's distinguished leaders to pray for you and anoint you with oil in the name of the Master.")
en5, ko5 = chap(5,
  [('§Destroying Your Life from Within', '1-3'),
   (E(5, 1), '1-3'),
   (E(5, 2), '4-6'),
   (E(5, 4), '7-8'),
   (E(5, 5), '9'),
   (E(5, 6), '10-11'),
   (E(5, 7), '12'),
   ('§Prayer to Be Reckoned With', '13-15'),
   (e1315, '13-15'),
   (E(5, 9), '16-18'),
   (E(5, 10), '19-20')],
  [('§속에서부터 무너지는 삶', '1-3'),
   (K(5, 2), '1-3'),
   (K(5, 3), '4-6'),
   (K(5, 5), '7-8'),
   (K(5, 6), '9'),
   (K(5, 7), '10-11'),
   (K(5, 8), '12'),
   ('§들어주셔야 할 기도', '13-15'),
   (K(5, 10), '13-15'),
   (K(5, 11), '16-18'),
   (K(5, 12), '19-20')],
  changes=[
    'Ch5: badges already match MSG (1-3 / 4-6 / 7-8 / 9 / 10-11 / 12 / 13-15 / 16-18 / 19-20)',
    'Ch5: replaced EN-added §Warning to the Rich with MSG own header §Destroying Your Life from Within (badged 1-3)',
    'Ch5: removed EN-added §Patience and Prayer (MSG has * * * divider there, not a header); added MSG own header §Prayer to Be Reckoned With (badged 13-15)',
    'Ch5: restored "anoint you with oil in the name of the Master" in EN 13-15',
    'Ch5: removed KO-only headers §부자들에 대한 경고 / §부자들에게 주는 경고 / §인내와 기도'])
en_patch.append(en5); ko_patch.append(ko5)

outdir = os.path.join(BASE, 'fixes')
json.dump(en_patch, open(os.path.join(outdir, 'en_James.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(ko_patch, open(os.path.join(outdir, 'ko_James.json'), 'w'), ensure_ascii=False, indent=1)
print('written:', len(en_patch), 'chapters')
r = subprocess.run([sys.executable, os.path.join(BASE, 'validate_translation.py'),
                    os.path.join(outdir, 'en_James.json'),
                    os.path.join(outdir, 'ko_James.json')],
                   capture_output=True, text=True)
print(r.stdout, r.stderr)
sys.exit(r.returncode)
