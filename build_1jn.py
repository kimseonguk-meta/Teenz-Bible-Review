#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — 1 John (5장)."""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))
KO_SRC = json.load(open('/tmp/ko_15books.json'))
BOOK = '1 John'
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
e67 = ("If we claim we have a shared life with him but keep stumbling around in the dark, we're lying through our teeth "
       "— not living what we say we believe. But if we walk in the light, God himself being the light, we also share a life "
       "with each other, as the sacrificed blood of Jesus, God's Son, purges all our sin.")
en1, ko1 = chap(1,
  [(E(1, 1), '1-2'),
   (E(1, 2), '3-4'),
   ('§Walk in the Light', '5'),
   (E(1, 3), '5'),
   (e67, '6-7'),
   (E(1, 4), '8-10')],
  [(K(1, 1), '1-2'),
   (K(1, 2), '3-4'),
   ('§빛 가운데로 가자', '5'),
   (K(1, 4), '5'),
   (K(1, 5), '6-7'),
   (K(1, 6), '8-10')],
  changes=[
    'Ch1: restored omitted 6-7 in EN (claim vs walk in light; blood of Jesus purges all sin)',
    'Ch1: replaced EN-added §Walking in the Light with MSG own header §Walk in the Light (badged 5)',
    'Ch1: removed KO-only header §빛 가운데 행함; added § to KO "빛 가운데로 가자" (badged 5)'])
en_patch.append(en1); ko_patch.append(ko1)

# ---------------- CH 2 ----------------
e46 = ("If someone claims, 'I know him well!' but doesn't keep his commandments, he's obviously a liar — his life doesn't match "
       "his words. But the one who keeps God's word is the person in whom we see God's mature love. This is the only way to be "
       "sure we're in God. Anyone who claims to be close with God ought to live the same kind of life Jesus lived.")
k1213 = ' '.join([K(2, 7), K(2, 8), K(2, 9)])
k1314 = ' '.join([K(2, 10), K(2, 11), K(2, 12)])
s2 = [{'msg_range': '2', 'paras': [0, 2], 'note': 'MSG 1-2 and 2-3 overlap on v2; badges kept as printed in MSG'},
      {'msg_range': '12-13', 'note': 'MSG prints 12-13 as one para (children/veterans/newcomers addressed inside); 3 KO sub-addresses folded into one para'},
      {'msg_range': '13-14', 'note': 'MSG prints 13-14 as one para (second reminder); 3 KO sub-addresses folded into one para'}]
en2, ko2 = chap(2,
  [(E(2, 1), '1-2'),
   ("§The Only Way to Know We're in Him", '2-3'),
   (E(2, 2), '2-3'),
   (e46, '4-6'),
   (E(2, 3), '7-8'),
   (E(2, 4), '9-11'),
   ('§Loving the World', '12-13'),
   (E(2, 5), '12-13'),
   (E(2, 6), '13-14'),
   (E(2, 7), '15-17'),
   ('§Antichrists Everywhere You Look', '18'),
   (E(2, 8), '18'),
   (E(2, 9), '19'),
   (E(2, 10), '20-21'),
   (E(2, 11), '22-23'),
   (E(2, 12), '24-25'),
   (E(2, 13), '26-27'),
   ('§Live Deeply in Christ', '28'),
   (E(2, 14), '28'),
   (E(2, 15), '29')],
  [(K(2, 1), '1-2'),
   ('§그 안에 있는지 아는 유일한 방법', '2-3'),
   (K(2, 2), '2-3'),
   (K(2, 4), '4-6'),
   (K(2, 5), '7-8'),
   (K(2, 6), '9-11'),
   ('§세상을 사랑하지 마', '12-13'),
   (k1213, '12-13'),
   (k1314, '13-14'),
   (K(2, 13), '15-17'),
   ('§적그리스도의 등장', '18'),
   (K(2, 15), '18'),
   (K(2, 16), '19'),
   (K(2, 17), '20-21'),
   (K(2, 18), '22-23'),
   (K(2, 19), '24-25'),
   (K(2, 20), '26-27'),
   ('§그리스도 안에 깊이 살자', '28'),
   (K(2, 22), '28'),
   (K(2, 23), '29')],
  splits=s2,
  changes=[
    'Ch2: restored omitted 4-6 in EN ("I know him well!" liar; live the same kind of life Jesus lived)',
    'Ch2: folded KO 3-way splits of 12-13 and 13-14 back into MSG single paras (splits recorded)',
    'Ch2: added MSG own headers §The Only Way to Know We\'re in Him (2-3), §Loving the World (12-13), §Antichrists Everywhere You Look (18), §Live Deeply in Christ (28) in EN',
    'Ch2: added § to KO "적그리스도의 등장" (badged 18); added § to KO "세상을 사랑하지 마" (badged 12-13); new KO headers "그 안에 있는지 아는 유일한 방법" (2-3), "그리스도 안에 깊이 살자" (28)',
    'Ch2: removed EN-added §Stay Tight with God and KO-only headers §새 계명 / §하나님의 진짜 자녀'])
en_patch.append(en2); ko_patch.append(ko2)

# ---------------- CH 3 ----------------
e1213 = ("We must not be like Cain, who joined the Evil One and then killed his brother. And why did he kill him? "
         "Because he was deep in the practice of evil, while his brother's actions were righteous. So don't be surprised, "
         "friends, when the world hates you — this has been going on a long time.")
e2124 = ("And friends, once we're no longer accusing or condemning ourselves, we're bold and free before God! We're able "
         "to stretch out our hands and receive what we asked for because we're doing what he said, doing what pleases him. "
         "Again, this is God's command: to believe in his personally named Son, Jesus Christ. He told us to love each other, "
         "in line with the original command. As we keep his commands, we live deeply and surely in him, and he lives in us. "
         "And this is how we experience his deep and abiding presence in us: by the Spirit he gave us.")
en3, ko3 = chap(3,
  [(E(3, 1), '1'),
   (E(3, 2), '2-3'),
   (E(3, 3), '4-6'),
   (E(3, 4), '7-8'),
   (E(3, 5), '9-10'),
   (E(3, 6), '11'),
   (e1213, '12-13'),
   (E(3, 7), '14-15'),
   (E(3, 8), '16-17'),
   ('§When We Practice Real Love', '18-20'),
   (E(3, 9), '18-20'),
   (e2124, '21-24')],
  [(K(3, 1), '1'),
   (K(3, 2), '2-3'),
   (K(3, 3), '4-6'),
   (K(3, 4), '7-8'),
   (K(3, 5), '9-10'),
   (K(3, 6), '11'),
   (K(3, 7), '12-13'),
   (K(3, 8), '14-15'),
   (K(3, 9), '16-17'),
   ('§참된 사랑의 실천', '18-20'),
   (K(3, 11), '18-20'),
   (K(3, 12), '21-24')],
  changes=[
    'Ch3: restored omitted 12-13 in EN (Cain, joined the Evil One, killed his brother; world hates you)',
    'Ch3: restored omitted 21-24 in EN (bold and free before God; believe in Jesus Christ; Spirit he gave us)',
    'Ch3: removed EN-added §Children of God and KO-only §하나님의 자녀 (MSG ch3 has no opening header)',
    'Ch3: added MSG own header §When We Practice Real Love (badged 18-20) in EN; added § to KO "참된 사랑의 실천"'])
en_patch.append(en3); ko_patch.append(ko3)

# ---------------- CH 4 ----------------
en4, ko4 = chap(4,
  [("§Don't Believe Everything You Hear", '1'),
   (E(4, 1), '1'),
   (E(4, 2), '2-3'),
   (E(4, 4), '4-6'),
   ('§God Is Love', '7-10'),
   (E(4, 5), '7-10'),
   (E(4, 6), '11-12'),
   (E(4, 7), '13-16'),
   ('§To Love, to Be Loved', '17-18'),
   (E(4, 8), '17-18'),
   (E(4, 9), '19'),
   (E(4, 10), '20-21')],
  [('§듣는 말 다 믿지 마', '1'),
   (K(4, 1), '1'),
   (K(4, 2), '2-3'),
   (K(4, 3), '4-6'),
   ('§하나님은 사랑이시라', '7-10'),
   (K(4, 5), '7-10'),
   (K(4, 6), '11-12'),
   (K(4, 7), '13-16'),
   ('§사랑하고 사랑받는 법', '17-18'),
   (K(4, 8), '17-18'),
   (K(4, 9), '19'),
   (K(4, 10), '20-21')],
  changes=[
    'Ch4: replaced EN-added §Testing the Spirits with MSG own header §Don\'t Believe Everything You Hear (badged 1)',
    'Ch4: moved §God Is Love to its MSG position before 7-10 (badged 7-10) in EN; added § to KO "하나님은 사랑이시라"',
    'Ch4: added MSG own header §To Love, to Be Loved (badged 17-18) in EN and KO ("사랑하고 사랑받는 법")',
    'Ch4: added § to KO "듣는 말 다 믿지 마" (badged 1); removed KO-only header §영을 분별하라'])
en_patch.append(en4); ko_patch.append(ko4)

# ---------------- CH 5 ----------------
en5, ko5 = chap(5,
  [(E(5, 1), '1-3'),
   ('§The Power That Brings the World to Its Knees', '4-5'),
   (E(5, 2), '4-5'),
   (E(5, 3), '6-8'),
   (E(5, 4), '9-10'),
   (E(5, 5), '11-12'),
   ('§The Reality, Not the Illusion', '13-15'),
   (E(5, 6), '13-15'),
   (E(5, 7), '16-17'),
   (E(5, 8), '18-21')],
  [(K(5, 1), '1-3'),
   ('§세상을 이기는 힘', '4-5'),
   (K(5, 3), '4-5'),
   (K(5, 4), '6-8'),
   (K(5, 5), '9-10'),
   (K(5, 6), '11-12'),
   ('§진짜를 가졌음', '13-15'),
   (K(5, 8), '13-15'),
   (K(5, 9), '16-17'),
   (K(5, 10), '18-21')],
  changes=[
    'Ch5: replaced EN-added §Faith Overcomes with MSG own header §The Power That Brings the World to Its Knees (badged 4-5)',
    'Ch5: replaced KO header §믿음이 이긴다 with "세상을 이기는 힘" (badged 4-5)',
    'Ch5: added MSG own header §The Reality, Not the Illusion (badged 13-15) in EN; added § to KO "진짜를 가졌음"'])
en_patch.append(en5); ko_patch.append(ko5)

outdir = os.path.join(BASE, 'fixes')
json.dump(en_patch, open(os.path.join(outdir, 'en_1John.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(ko_patch, open(os.path.join(outdir, 'ko_1John.json'), 'w'), ensure_ascii=False, indent=1)
print('written:', len(en_patch), 'chapters')
r = subprocess.run([sys.executable, os.path.join(BASE, 'validate_translation.py'),
                    os.path.join(outdir, 'en_1John.json'),
                    os.path.join(outdir, 'ko_1John.json')],
                   capture_output=True, text=True)
print(r.stdout, r.stderr)
sys.exit(r.returncode)
