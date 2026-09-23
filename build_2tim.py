#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — 2 Timothy."""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))
KO_SRC = json.load(open('/tmp/ko_15books.json'))
BOOK = '2 Timothy'
EN_CH = {c['num']: c for c in EN_SRC[BOOK]}
KO_CH = {c['num']: c for c in KO_SRC[BOOK]}
EN_TITLE = {c['num']: c.get('title', '') for c in EN_SRC[BOOK]}

def E(ch, i): return EN_CH[ch]['paragraphs'][i]
def K(ch, i):
    return re.sub(r'^\d+(-\d+)?(절)?\.?\s*\n', '', KO_CH[ch]['paragraphs'][i])

def chap(num, en_paras, ko_paras, splits=None, merges=None, changes=None, confirmations=None):
    vr = [b for _, b in en_paras]
    assert len(en_paras) == len(ko_paras), f'ch{num} EN/KO 문단 수 불일치'
    assert [b for _, b in ko_paras] == vr, f'ch{num} EN/KO 배지 불일치: {vr} vs {[b for _, b in ko_paras]}'
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
p12 = ("Hey, it's Paul — I'm on special assignment for Christ, carrying out God's plan laid out in the Message "
       "of Life by Jesus. Writing this to you, Timothy — you're like a son to me, I love you so much. "
       "All the best from our God and Christ be yours!")
p1112 = E(1, 5).replace('as a preacher and a teacher.', 'as a preacher, emissary, and teacher.')
en1, ko1 = chap(1,
  [(p12, '1-2'),
   ('§To Be Bold with God\'s Gifts', '3-4'),
   (E(1, 2), '3-4'),
   (E(1, 3), '5-7'),
   (E(1, 4), '8-10'),
   (p1112, '11-12'),
   (E(1, 6), '13-14'),
   (E(1, 7), '15-18')],
  [(K(1, 1), '1-2'),
   ('§하나님의 선물을 대담하게 쓰라', '3-4'),
   (K(1, 2), '3-4'),
   (K(1, 3), '5-7'),
   (K(1, 5), '8-10'),
   (K(1, 6), '11-12'),
   (K(1, 7), '13-14'),
   (K(1, 8), '15-18')],
  changes=[
    'Ch1: badges corrected to MSG (1-2 / 3-4 / 5-7 / 8-10 / 11-12 / 13-14 / 15-18)',
    'Ch1: removed EN-added §Fan the Flame; added MSG own header §To Be Bold with God\'s Gifts (badged 3-4, after greeting) per MSG layout',
    'Ch1: removed KO-only header "불꽃을 되살려라" and KO-only line "메시지를 위한 고생, 같이 하자고" (no EN counterparts)',
    'Ch1: restored "on special assignment for Christ, carrying out God\'s plan laid out in the Message of Life by Jesus" in EN 1-2',
    'Ch1: restored "emissary" in EN 11-12 (MSG "preacher, emissary, and teacher")'])
en_patch.append(en1); ko_patch.append(ko1)

# ---------------- CH 2 ----------------
p19 = ("But God's firm foundation is as solid as ever, like a building with these words carved into stone: "
       "**God knows his squad.** And **if you're on God's team, you gotta ditch the bad stuff.**")
p2021 = ("Think of it like a well-furnished kitchen — in a fancy kitchen, you've got crystal goblets and silver "
         "platters for serving amazing food, but also waste cans and compost buckets for taking out the garbage. "
         "Become the kind of container God can use to serve up any and every kind of blessing to his guests.")
en2, ko2 = chap(2,
  [('§Doing Your Best for God', '1-7'),
   (E(2, 1), '1-7'),
   (E(2, 2), '8-13'),
   (E(2, 3), '14-18'),
   (p19, '19'),
   (p2021, '20-21'),
   (E(2, 5), '22-26')],
  [('§하나님을 위해 최선을 다하라', '1-7'),
   (K(2, 2), '1-7'),
   (K(2, 3), '8-13'),
   (K(2, 4), '14-18'),
   (K(2, 5), '19'),
   (K(2, 6), '20-21'),
   (K(2, 7), '22-26')],
  changes=[
    'Ch2: badges corrected to MSG (1-7 / 8-13 / 14-18 / 19 / 20-21 / 22-26)',
    'Ch2: replaced EN-added §A Good Soldier with MSG own header §Doing Your Best for God (badged 1-7)',
    'Ch2: removed KO-only headers "좋은 군사" and "디모데후서 2장: 하나님이 쓰시는 클라스" (no EN counterparts)',
    'Ch2: split EN merged 19-21 paragraph into MSG\'s separate 19 (foundation stones) and 20-21 (kitchen containers) paragraphs; restored crystal-goblets/silver-platters/waste-cans wording'])
en_patch.append(en2); ko_patch.append(ko2)

# ---------------- CH 3 ----------------
en3, ko3 = chap(3,
  [('§Difficult Times Ahead', '1-5'),
   (E(3, 1), '1-5'),
   (E(3, 2), '6-9'),
   ('§Keep the Message Alive', '10-13'),
   (E(3, 3), '10-13'),
   (E(3, 4), '14-17')],
  [('§힘든 시기가 다가오고 있다', '1-5'),
   (K(3, 2), '1-5'),
   (K(3, 3), '6-9'),
   ('§메시지를 살아 있게 하라', '10-13'),
   (K(3, 5), '10-13'),
   (K(3, 6), '14-17')],
  changes=[
    'Ch3: badges corrected to MSG (1-5 / 6-9 / 10-13 / 14-17)',
    'Ch3: replaced EN-added §The Last Days with MSG own header §Difficult Times Ahead (badged 1-5)',
    'Ch3: added MSG own header §Keep the Message Alive (badged 10-13) in EN and KO',
    'Ch3: removed KO-only lines "마지막 때" kicker and "메시지를 살아있게 하셈" replaced by proper § header (no EN counterparts)',
    'Ch3: EN content verified complete vs MSG (vice list, Jannes/Jambres, Antioch/Iconium/Lystra, God-breathed) — no restoration needed'])
en_patch.append(en3); ko_patch.append(ko3)

# ---------------- CH 4 ----------------
p22 = "May God be with you. Grace be with you too."
ko21a = '너는 겨울 오기 전에 꼭 와야 돼.'
ko21b = '여기 있는 으불로, 부데, 리노, 글라우디아, 그리고 네 모든 친구들이 너한테 안부 전한대.'
split4 = [{'msg_range': '21', 'paras': [6, 7],
           'note': 'MSG prints "Try hard to get here before winter" and the Eubulus greetings under one badge 21; kept as two teen paragraphs sharing the badge'}]
en4, ko4 = chap(4,
  [(E(4, 1), '1-2'),
   (E(4, 2), '3-5'),
   (E(4, 4), '6-8'),
   (E(4, 5), '9-13'),
   (E(4, 6), '14-15'),
   (E(4, 7), '16-18'),
   (E(4, 8), '19-20'),
   (E(4, 9), '21'),
   (E(4, 10), '21'),
   (p22, '22')],
  [(K(4, 1), '1-2'),
   (K(4, 2), '3-5'),
   (K(4, 3), '6-8'),
   (K(4, 5), '9-13'),
   (K(4, 6), '14-15'),
   (K(4, 7), '16-18'),
   (K(4, 8), '19-20'),
   (ko21a, '21'),
   (ko21b, '21'),
   (K(4, 10), '22')],
  splits=split4,
  changes=[
    'Ch4: badges corrected to MSG (1-2 / 3-5 / 6-8 / 9-13 / 14-15 / 16-18 / 19-20 / 21 / 22)',
    'Ch4: removed EN-added headers §Final Charge and §Paul\'s Farewell (MSG has no section headers in ch4; uses * * * divider) and KO counterparts §마지막 당부 / §바울의 작별',
    'Ch4: split KO merged 21 para into two paras sharing badge 21 (MSG prints both under badge 21); declared in splits',
    'Ch4: restored "Grace be with you" in EN 22 (was "Peace out")'])
en_patch.append(en4); ko_patch.append(ko4)

outdir = os.path.join(BASE, 'fixes')
json.dump(en_patch, open(os.path.join(outdir, 'en_2Timothy.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(ko_patch, open(os.path.join(outdir, 'ko_2Timothy.json'), 'w'), ensure_ascii=False, indent=1)
print('written:', len(en_patch), 'chapters')
r = subprocess.run([sys.executable, os.path.join(BASE, 'validate_translation.py'),
                    os.path.join(outdir, 'en_2Timothy.json'),
                    os.path.join(outdir, 'ko_2Timothy.json')],
                   capture_output=True, text=True)
print(r.stdout, r.stderr)
sys.exit(r.returncode)
