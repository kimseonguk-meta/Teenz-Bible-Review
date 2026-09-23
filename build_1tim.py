#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — 1 Timothy."""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))
KO_SRC = json.load(open('/tmp/ko_15books.json'))
BOOK = '1 Timothy'
EN_CH = {c['num']: c for c in EN_SRC[BOOK]}
KO_CH = {c['num']: c for c in KO_SRC[BOOK]}
EN_TITLE = {c['num']: c.get('title', '') for c in EN_SRC[BOOK]}

def E(ch, i): return EN_CH[ch]['paragraphs'][i]
def K(ch, i):
    return re.sub(r'^\d+(-\d+)?\s*\n', '', KO_CH[ch]['paragraphs'][i])

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
p57 = E(1, 3).replace('**love**', 'love')
p1920 = ("Some people have already bailed on their faith by being lazy and thinking they can do whatever "
 'they want. Hymenaeus and Alexander are a couple of them. I handed them over to Satan to teach them a '
 'lesson or two about not disrespecting God.')
split1 = [
  {'msg_range': '15-19', 'paras': [7, 8, 9],
   'note': 'MSG prints one 15-19 paragraph block (incl. doxology and Timothy charge); split into 3 teen paragraphs sharing the badge'},
  {'msg_range': '19', 'paras': [9, 10],
   'note': 'MSG 15-19 and 19-20 overlap on v19; badges kept as printed in MSG'}]
en1, ko1 = chap(1,
  [('§Watch Out for False Teaching', '1-2'),
   (E(1, 1), '1-2'),
   ('§Self-Appointed Experts', '3-4'),
   (E(1, 2), '3-4'),
   (p57, '5-7'),
   (E(1, 4), '8-11'),
   (E(1, 5), '12-14'),
   (E(1, 6), '15-19'),
   (E(1, 7), '15-19'),
   (E(1, 8), '15-19'),
   (p1920, '19-20')],
  [('§거짓 가르침을 조심하라', '1-2'),
   (K(1, 1), '1-2'),
   ('§가짜 선생님들한테 속지 마라', '3-4'),
   (K(1, 3), '3-4'),
   (K(1, 4), '5-7'),
   (K(1, 5), '8-11'),
   (K(1, 6), '12-14'),
   (K(1, 7), '15-19'),
   (K(1, 8), '15-19'),
   (K(1, 9), '15-19'),
   (K(1, 10), '19-20')],
  splits=split1,
  changes=[
    'Ch1: badges corrected to MSG (1-2 / 3-4 / 5-7 / 8-11 / 12-14 / 15-19 / 19-20)',
    'Ch1: added §Self-Appointed Experts header before 3-4 (MSG own section title; matches KO §가짜 선생님들한테 속지 마라)',
    'Ch1: MSG 15-19 block (word to depend on + doxology + Timothy charge) kept as 3 paragraphs sharing badge 15-19; declared in splits',
    'Ch1: restored "handed them over to Satan" in EN 19-20 (was softened to "kick them out")',
    'Ch1: stripped ** markdown from EN 5-7 love line'])
en_patch.append(en1); ko_patch.append(ko1)

# ---------------- CH 2 ----------------
en2, ko2 = chap(2,
  [('§Instructions on Worship', '1-3'),
   (E(2, 1), '1-3'), (E(2, 2), '4-7'), (E(2, 3), '8-10'), (E(2, 4), '11-15')],
  [('§예배 지침', '1-3'),
   (K(2, 2), '1-3'), (K(2, 3), '4-7'), (K(2, 4), '8-10'), (K(2, 5), '11-15')],
  changes=[
    'Ch2: badges already match MSG (1-3 / 4-7 / 8-10 / 11-15); §header badged 1-3',
    'Ch2: removed KO-only line "모든 일의 기본은 기도지" (no EN counterpart)',
    'Ch2: EN content verified complete vs MSG (pray for rulers, one Priest-Mediator, holy hands, Adam-then-Eve, childbearing) — no restoration needed'])
en_patch.append(en2); ko_patch.append(ko2)

# ---------------- CH 3 ----------------
_p1416 = E(3, 3).replace('and then he had the ultimate transformation and went back to heaven.',
                        'and then he was taken up into heaven in glory.')
en1416_intro, en1416_hymn = _p1416.split('but some parts are crystal clear. ')
en1416_intro += 'but some parts are crystal clear.'
ko1416_intro = K(3, 14) + ' ' + K(3, 15)
ko1416_hymn = K(3, 16) + ' ' + K(3, 17)
ko17 = ' '.join(K(3, i) for i in range(2, 8))
ko813 = ' '.join(K(3, i) for i in range(8, 14))
split3 = [{'msg_range': '14-16', 'paras': [3, 4],
           'note': 'MSG prints the 14-16 intro and the confession hymn as separate paragraphs sharing the badge'}]
en3, ko3 = chap(3,
  [('§Leaders in the Church', '1-7'),
   (E(3, 1), '1-7'),
   (E(3, 2), '8-13'),
   (en1416_intro, '14-16'),
   (en1416_hymn, '14-16')],
  [('§교회의 지도자', '1-7'),
   (ko17, '1-7'),
   (ko813, '8-13'),
   (ko1416_intro, '14-16'),
   (ko1416_hymn, '14-16')],
  splits=split3,
  changes=[
    'Ch3: badges already match MSG (1-7 / 8-13 / 14-16); §header badged 1-7',
    'Ch3: split MSG 14-16 block into 2 paras sharing the badge (intro + confession hymn), declared in splits',
    'Ch3: consolidated KO verse-by-verse paragraphs into 3 MSG paragraphs 1:1 with EN (was 18 paras; removed kicker "교회 리더의 조건")',
    'Ch3: restored "taken up into heaven in glory" in EN 14-16 hymn (was "ultimate transformation and went back to heaven")'])
en_patch.append(en3); ko_patch.append(ko3)

# ---------------- CH 4 ----------------
en4, ko4 = chap(4,
  [('§Training in Godliness', '1-5'),
   (E(4, 1), '1-5'),
   (E(4, 2), '6-10'),
   ('§Teach with Your Life', '11-14'),
   (E(4, 3), '11-14'),
   (E(4, 4), '15-16')],
  [('§경건의 훈련', '1-5'),
   (K(4, 1), '1-5'),
   (K(4, 2), '6-10'),
   ('§너의 삶으로 직접 보여줘', '11-14'),
   (K(4, 4), '11-14'),
   (K(4, 5), '15-16')],
  changes=[
    'Ch4: badges corrected to MSG (1-5 / 6-10 / 11-14 / 15-16); EN 11-13 rebadged 11-14, EN 13-16 rebadged 15-16',
    'Ch4: added §Teach with Your Life header before 11-14 (MSG own section title; matches KO §너의 삶으로 직접 보여줘)',
    'Ch4: KO embedded "N-M" line prefixes stripped; § added to 너의 삶으로 직접 보여줘',
    'Ch4: EN content verified complete vs MSG (demonic illusions, gym vs godliness, young Timothy, cultivate) — no restoration needed'])
en_patch.append(en4); ko_patch.append(ko4)

# ---------------- CH 5 ----------------
_e57 = E(5, 7)
en519, en520 = _e57.split('If someone does mess up, ')
en520 = 'If someone does mess up, ' + en520
en5, ko5 = chap(5,
  [('§Advice for Different Groups', '1-2'),
   (E(5, 1), '1-2'),
   (E(5, 2), '3-8'),
   (E(5, 3), '9-10'),
   (E(5, 4), '11-15'),
   (E(5, 5), '16'),
   (E(5, 6), '17-18'),
   (en519, '19'),
   (en520, '20'),
   (E(5, 8), '21-23'),
   (E(5, 9), '24-25')],
  [('§다양한 사람들을 위한 조언', '1-2'),
   (K(5, 2), '1-2'),
   (K(5, 3), '3-8'),
   (K(5, 4), '9-10'),
   (K(5, 5), '11-15'),
   (K(5, 6), '16'),
   (K(5, 7), '17-18'),
   (K(5, 8), '19'),
   (K(5, 9), '20'),
   (K(5, 10), '21-23'),
   (K(5, 11), '24-25')],
  changes=[
    'Ch5: badges corrected to MSG (1-2 / 3-8 / 9-10 / 11-15 / 16 / 17-18 / 19 / 20 / 21-23 / 24-25)',
    'Ch5: split merged 19-20 into MSG\'s separate 19 and 20 paras in EN and KO',
    'Ch5: removed KO-only kicker "성도를 대하는 자세" (no EN counterpart)',
    'Ch5: KO embedded "N-M" line prefixes stripped'])
en_patch.append(en5); ko_patch.append(ko5)

# ---------------- CH 6 ----------------
p68 = E(6, 3).replace("So if we've got food and clothes, we're good. That's enough.",
                      "So if we've got bread on the table and shoes on our feet, we're good. That's enough.")
p1112 = E(6, 5).replace('Go hard after a life that\'s legit—full of integrity, faith, love, and patience.',
                        'Go hard after a legit life — one full of wonder, faith, love, steadiness, and courtesy.')
p1316 = E(6, 6).replace('the King of all kings and Lord of all lords.',
                        'the High King, the High God.').replace(
    "All honor and power to him forever! You know it.",
    "All honor to him, and eternal rule! Oh, yes.")
_p2021 = E(6, 8).replace("Stay blessed!", "Overwhelming grace keep you!")
p2021_treasure, p2021_grace = _p2021.split('Overwhelming grace keep you!')
p2021_treasure = p2021_treasure.rstrip()
p2021_grace = 'Overwhelming grace keep you!'
split6 = [{'msg_range': '2', 'paras': [1, 2],
           'note': 'MSG 1-2 and 2-5 overlap on v2; badges kept as printed in MSG'},
          {'msg_range': '20-21', 'paras': [8, 9],
           'note': 'MSG prints the treasure-guarding charge and the closing "Overwhelming grace keep you!" as separate paragraphs sharing the 20-21 badge'}]
en6, ko6 = chap(6,
  [('§Money and Contentment', '1-2'),
   (E(6, 1), '1-2'),
   (E(6, 2), '2-5'),
   (p68, '6-8'),
   (E(6, 4), '9-10'),
   (p1112, '11-12'),
   (p1316, '13-16'),
   (E(6, 7), '17-19'),
   (p2021_treasure, '20-21'),
   (p2021_grace, '20-21')],
  [('§돈과 만족', '1-2'),
   (K(6, 1), '1-2'),
   (K(6, 2), '2-5'),
   (K(6, 3), '6-8'),
   (K(6, 5), '9-10'),
   (K(6, 7), '11-12'),
   (K(6, 8), '13-16'),
   (K(6, 9), '17-19'),
   (K(6, 10), '20-21'),
   (K(6, 11), '20-21')],
  splits=split6,
  changes=[
    'Ch6: badges corrected to MSG (1-2 / 2-5 / 6-8 / 9-10 / 11-12 / 13-16 / 17-19 / 20-21); declared v2 overlap of 1-2 and 2-5 in splits',
    'Ch6: split MSG 20-21 block into 2 paras sharing the badge (treasure charge + closing grace greeting), declared in splits',
    'Ch6: restored "bread on the table and shoes on our feet" in EN 6-8 (was "food and clothes")',
    'Ch6: restored "wonder, faith, love, steadiness, courtesy" in EN 11-12 (was "integrity, faith, love, patience")',
    'Ch6: restored "High King, High God" and "eternal rule" in EN 13-16 (was added phrase "King of all kings and Lord of all lords" + "power")',
    'Ch6: restored MSG closing "Overwhelming grace keep you!" in EN 20-21 (was "Stay blessed!")',
    'Ch6: removed KO-only headers "돈 욕심" and "믿음 안에서 힘을 다해 달려가라" (no EN counterparts)'])
en_patch.append(en6); ko_patch.append(ko6)

outdir = os.path.join(BASE, 'fixes')
json.dump(en_patch, open(os.path.join(outdir, 'en_1Timothy.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(ko_patch, open(os.path.join(outdir, 'ko_1Timothy.json'), 'w'), ensure_ascii=False, indent=1)
print('written:', len(en_patch), 'chapters')
r = subprocess.run([sys.executable, os.path.join(BASE, 'validate_translation.py'),
                    os.path.join(outdir, 'en_1Timothy.json'),
                    os.path.join(outdir, 'ko_1Timothy.json')],
                   capture_output=True, text=True)
print(r.stdout, r.stderr)
sys.exit(r.returncode)
