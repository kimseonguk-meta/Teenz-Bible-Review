#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — 2 Thessalonians."""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))
KO_SRC = json.load(open('/tmp/ko_15books.json'))
BOOK = '2 Thessalonians'
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
p510 = ("All the tough stuff you're going through? It's actually a good sign. It shows God's getting you "
 'ready for his kingdom. Yeah, you\'re taking some hits now, but payback is coming. When the boss, Jesus, '
 'rolls up from heaven in a blaze of fire with his squad of powerful angels, it\'s going to be epic. '
 "He's coming to settle the score with everyone who gave you a hard time. For all the people who ghosted "
 "God and ignored his message, it's the end. They'll be permanently kicked out from the awesome presence "
 "of the Lord and his incredible power. But for us, his followers, it's the moment we've all been waiting "
 "for. He's going to get a massive hero's welcome from everyone who believed, and that includes you, "
 'because you trusted what we told you.')
en1, ko1 = chap(1,
  [('§Encouragement in Persecution', '1-2'),
   (E(1, 1), '1-2'),
   (E(1, 2), '3-4'),
   ('§Justice Is on the Way', '5-10'),
   (p510, '5-10'),
   (E(1, 4), '11-12')],
  [('§핍박 속의 격려', '1-2'),
   (K(1, 1), '1-2'),
   (K(1, 2), '3-4'),
   ('§주님이 다시 오시는 날', '5-10'),
   (K(1, 4), '5-10'),
   (K(1, 5), '11-12')],
  changes=[
    'Ch1: badges corrected to MSG (1-2 / 3-4 / 5-10 / 11-12); v3-4 para rebadged 3-4 (was 3-5)',
    'Ch1: added §Justice Is on the Way header before 5-10 (MSG own section title; matches KO §주님이 다시 오시는 날 placement)',
    'Ch1: restored "blaze of fire" detail in EN 5-10 (was slang "it\'s going to be lit")',
    'Ch1: EN content otherwise verified complete vs MSG — no other restoration needed'])
en_patch.append(en1); ko_patch.append(ko1)

# ---------------- CH 2 ----------------
p13_new = ("Alright guys, listen up, for real \u2014 read this part carefully. Chill out, and don't let anyone "
 'rattle you with claims that the day already came when our Master, Jesus Christ, comes back and we all '
 "gather to welcome him. I know some people are spreading false rumors or a phony letter that looks like "
 "it's from me, saying you missed the whole thing. Don't fall for that garbage.")
ko35 = ("그날이 오기 전에 몇 가지 사건이 먼저 터질 거야. 먼저, 다들 믿음을 버리는 배신이 있을 거고, 그 다음에\n"
 '빌런, 완전 사탄의 똘마니가 나타날 거임. 걔는 신이라고 불리는 모든 거랑 제단 같은 거에 다 덤비고 싹 다 먹어버릴 거임. '
 '반대하는 애들 다 쓸어버리고, 하나님의 성전에 자리 잡고 앉아서 "내가 바로 전능한 하나님이다!" 이럴 거라니까. '
 '내가 너희랑 같이 있을 때 이 얘기 다 해줬던 거 기억 안 남? 기억력이 완전 금붕어 수준임?')
ko68 = ("그리고 그 빌런이 정해진 시간까지는 봉인될 거라고 한 내 말도 기억할걸. 그렇다고 지금 악의 기운이 없는 건 아님. "
 '그 기운은 지금도 지하에서 몰래 움직이고 있거든. 언젠가는 그 빌런이 봉인 해제돼서 풀려날 때가 올 거임. 근데 걱정 아니. '
 "주 예수님이 나타나서 한 방에 날려버릴 거니까. 주님이 나타나서 입김 한 번 '훅' 불면 그 빌런은 그냥 먼지처럼 사라져버릴 거임.")
en2, ko2 = chap(2,
  [('§The Day of the Lord', '1-3'),
   (p13_new, '1-3'),
   (E(2, 2), '3-5'),
   (E(2, 3), '6-8'),
   (E(2, 4), '9-12'),
   (E(2, 5), '13-14'),
   (E(2, 6), '15-17')],
  [('§주의 날', '1-3'),
   (K(2, 2), '1-3'),
   (ko35, '3-5'),
   (ko68, '6-8'),
   (K(2, 4), '9-12'),
   (K(2, 5), '13-14'),
   (K(2, 6), '15-17')],
  changes=[
    'Ch2: badges corrected to MSG (1-3 / 3-5 / 6-8 / 9-12 / 13-14 / 15-17)',
    'Ch2: restored MSG 1-3 details in EN ("read this part carefully", "we all gather to welcome him")',
    'Ch2: split KO 3-8 para into 3-5 + 6-8 (was merged; EN already had them separate) — now 1:1 with MSG',
    'Ch2: removed KO-only kicker line "데살로니가후서 2장: 빌런의 등장" (duplicates chapter title; EN never had it)'])
en_patch.append(en2); ko_patch.append(ko2)

# ---------------- CH 3 ----------------
p1013 = ('Remember the golden rule we had? "If you don\'t work, you don\'t eat." Simple. But now we\'re hearing '
 'that some of you are just being lazy bums, mooching off the hard work of others. That\'s not cool. '
 "We're telling those people to get a job, no excuses, and start paying their own way. For the rest of you, "
 "don't get tired of doing the right thing \u2014 don't burn out, keep going and keep doing good.")
p16 = ("May the Lord of Peace himself give you the gift of getting along with each other \u2014 peace at all "
 'times, in every way. May the Lord be with you all.')
en3, ko3 = chap(3,
  [('§Warning Against Laziness', '1-3'),
   (E(3, 1), '1-3'),
   (E(3, 2), '4-5'),
   (E(3, 3), '6-9'),
   (p1013, '10-13'),
   (E(3, 6), '14-15'),
   (p16, '16'),
   (E(3, 8), '17'),
   (E(3, 9), '18')],
  [('§게으름에 대한 경고', '1-3'),
   (K(3, 2), '1-3'),
   (K(3, 3), '4-5'),
   (K(3, 4), '6-9'),
   (K(3, 5), '10-13'),
   (K(3, 6), '14-15'),
   (K(3, 7), '16'),
   (K(3, 8), '17'),
   (K(3, 9), '18')],
  changes=[
    'Ch3: merged EN 10-12 + 13 paras into one 10-13 para (MSG single paragraph; matches KO; removed doubled "don\'t get tired/burn out" phrasing)',
    'Ch3: restored "getting along with each other" in EN 16 (was reduced to "give you peace")',
    'Ch3: removed KO-only kicker line "데살로니가후서 3장 - 게으름뱅이들한테 경고함" (duplicates title/§header; EN never had it)',
    'Ch3: badges corrected to MSG (1-3 / 4-5 / 6-9 / 10-13 / 14-15 / 16 / 17 / 18)'])
en_patch.append(en3); ko_patch.append(ko3)

outdir = os.path.join(BASE, 'fixes')
json.dump(en_patch, open(os.path.join(outdir, 'en_2Thessalonians.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(ko_patch, open(os.path.join(outdir, 'ko_2Thessalonians.json'), 'w'), ensure_ascii=False, indent=1)
print('written:', len(en_patch), 'chapters')
r = subprocess.run([sys.executable, os.path.join(BASE, 'validate_translation.py'),
                    os.path.join(outdir, 'en_2Thessalonians.json'),
                    os.path.join(outdir, 'ko_2Thessalonians.json')],
                   capture_output=True, text=True)
print(r.stdout, r.stderr)
sys.exit(r.returncode)
