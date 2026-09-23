#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — Hebrews (13장)."""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))
KO_SRC = json.load(open('/tmp/ko_15books.json'))
BOOK = 'Hebrews'
EN_CH = {c['num']: c for c in EN_SRC[BOOK]}
KO_CH = {c['num']: c for c in KO_SRC[BOOK]}
EN_TITLE = {c['num']: c.get('title', '') for c in EN_SRC[BOOK]}

def E(ch, i): return EN_CH[ch]['paragraphs'][i]
def K(ch, i):
    return re.sub(r'^\d+(-\d+)?(절)?(::)?\s*', '', KO_CH[ch]['paragraphs'][i])

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
e7 = "When it comes to angels, God's like, 'Yeah, they're like super-fast messengers, like gusts of wind or flashes of fire.'"
e89 = ("But to his Son, he says, 'You're God, and you're in charge forever. You're all about doing the right thing "
       "and you can't stand fakes. That's why I, your God, picked you to be the king and hooked you up with more "
       "good stuff than all your friends.'")
e13 = "And for the record, God never said to an angel, 'Come chill with me on my throne until I make your enemies your footstool.'"
e14 = "It's pretty clear that angels are just the support crew, sent to help out everyone who's getting saved."
s1 = [{'msg_range': '3', 'paras': [0, 2],
       'note': 'MSG 1-3 and 3-6 overlap on v3; badges kept as printed in MSG'}]
en1, ko1 = chap(1,
  [(E(1, 1), '1-3'),
   ('§The Son Is Higher than Angels', '3-6'),
   (E(1, 2), '3-6'),
   (e7, '7'), (e89, '8-9'), (E(1, 4), '10-12'), (e13, '13'), (e14, '14')],
  [(K(1, 1), '1-3'),
   ('§아들은 천사들보다 높으시다', '3-6'),
   (K(1, 2), '3-6'),
   (K(1, 3), '7'), (K(1, 4), '8-9'), (K(1, 5), '10-12'), (K(1, 6), '13'), (K(1, 7), '14')],
  splits=s1,
  changes=[
    'Ch1: badges corrected to MSG (1-3 / 3-6 / 7 / 8-9 / 10-12 / 13 / 14); declared v3 overlap of 1-3 and 3-6 in splits',
    'Ch1: moved MSG own header §The Son Is Higher than Angels to its MSG position (badged 3-6, after greeting); removed EN-added §Jesus Is Greater Than Angels from chapter start',
    'Ch1: split EN merged 7-8 para into MSG\'s 7 (angels as winds/fire) and 8-9 (Son on throne) paras; split EN merged 13-14 into 13 and 14 paras',
    'Ch1: replaced KO-only header §예수님은 천사보다 위대하시다 with §아들은 천사들보다 높으시다 (badged 3-6)'])
en_patch.append(en1); ko_patch.append(ko1)

# ---------------- CH 2 ----------------
e1415 = ("Since we're all just regular people, it made sense for Jesus to become one of us. He did it to save us by "
         "dying himself. By facing death head-on, he totally wrecked the devil's power over it. He freed everyone "
         "who was basically living in fear of dying.")
e1618 = ("It's pretty clear he didn't do all this for the angels. He did it for us, for Abraham's crew. That's why "
         "he had to go through everything we go through. So when he stands before God as our High Priest to wipe "
         "our sins clean, he knows exactly what it feels like. He's been through the pain and the struggles, so "
         "he's the perfect one to help us when we need it.")
k59 = K(2, 3) + ' ' + K(2, 4) + ' ' + K(2, 5)
k1013 = K(2, 6) + ' ' + K(2, 7) + ' ' + K(2, 8) + ' ' + K(2, 9) + ' ' + K(2, 10) + ' ' + K(2, 11)
en2, ko2 = chap(2,
  [(E(2, 1), '1-4'),
   ('§The Salvation Pioneer', '5-9'),
   (E(2, 2), '5-9'),
   (E(2, 3), '10-13'),
   (e1415, '14-15'),
   (e1618, '16-18')],
  [(K(2, 1), '1-4'),
   ('§구원의 개척자', '5-9'),
   (k59, '5-9'),
   (k1013, '10-13'),
   (K(2, 12), '14-15'),
   (K(2, 13), '16-18')],
  changes=[
    'Ch2: badges corrected to MSG (1-4 / 5-9 / 10-13 / 14-15 / 16-18)',
    'Ch2: removed EN-added §Don\'t Drift Away (MSG has no header before 2:1-4); added MSG own header §The Salvation Pioneer (badged 5-9)',
    'Ch2: split EN merged 15-18 para into MSG\'s 14-15 (flesh and blood, devil\'s hold on death) and 16-18 (for Abraham\'s crew, high priest) paras',
    'Ch2: removed KO-only headers §흘러가지 말라 / "구원의 개척자이신 예수" / "다음 말씀도 자신을 그들과 한 가족으로 여기신다는 뜻임" / "또 이렇게도 말씀하셨음"; consolidated KO verse-level paras into MSG 5-9 and 10-13 paras 1:1 with EN'])
en_patch.append(en2); ko_patch.append(ko2)

# ---------------- CH 3 ----------------
k611 = K(3, 3) + '\n' + K(3, 4)
k1214 = K(3, 5) + '\n' + K(3, 6)
s3 = [{'msg_range': '6', 'paras': [1, 2],
       'note': 'MSG 1-6 and 6-11 overlap on v6; badges kept as printed in MSG'}]
en3, ko3 = chap(3,
  [('§The Centerpiece of All We Believe', '1-6'),
   (E(3, 1), '1-6'),
   (E(3, 2), '6-11'),
   (E(3, 3), '12-14'),
   (E(3, 4), '15-19')],
  [('§우리 믿음의 중심', '1-6'),
   (K(3, 2), '1-6'),
   (k611, '6-11'),
   (k1214, '12-14'),
   (K(3, 7), '15-19')],
  splits=s3,
  changes=[
    'Ch3: badges corrected to MSG (1-6 / 6-11 / 12-14 / 15-19); declared v6 overlap of 1-6 and 6-11 in splits',
    'Ch3: replaced EN-added §Jesus Our High Priest with MSG own header §The Centerpiece of All We Believe (badged 1-6)',
    'Ch3: consolidated KO: single §우리 믿음의 중심 header (badged 1-6), merged 6-7+7-11 into 6-11, merged echo 15 into 12-14 per MSG layout'])
en_patch.append(en3); ko_patch.append(ko3)

# ---------------- CH 4 ----------------
s4 = [{'msg_range': '3', 'paras': [1, 2],
       'note': 'MSG 1-3 and 3-7 overlap on v3; badges kept as printed in MSG'}]
en4, ko4 = chap(4,
  [('§When the Promises Are Mixed with Faith', '1-3'),
   (E(4, 1), '1-3'),
   (E(4, 2), '3-7'),
   (E(4, 3), '8-11'),
   (E(4, 4), '12-13'),
   ('§The High Priest Who Cried Out in Pain', '14-16'),
   (E(4, 5), '14-16')],
  [('§약속이 믿음과 섞일 때', '1-3'),
   (K(4, 2), '1-3'),
   (K(4, 3), '3-7'),
   (K(4, 4), '8-11'),
   (K(4, 5), '12-13'),
   ('§고통 가운데 부르짖으신 대제사장', '14-16'),
   (K(4, 7), '14-16')],
  splits=s4,
  changes=[
    'Ch4: badges corrected to MSG (1-3 / 3-7 / 8-11 / 12-13 / 14-16); declared v3 overlap of 1-3 and 3-7 in splits',
    'Ch4: replaced EN-added §A Sabbath Rest with MSG own header §When the Promises Are Mixed with Faith (badged 1-3)',
    'Ch4: added MSG own header §The High Priest Who Cried Out in Pain (badged 14-16) in EN and KO',
    'Ch4: removed KO-only lines §안식일의 쉼 / "믿음으로 약속을 받아들일 때"'])
en_patch.append(en4); ko_patch.append(ko4)

# ---------------- CH 5 ----------------
en5, ko5 = chap(5,
  [(E(5, 1), '1-3'),
   (E(5, 2), '4-6'),
   (E(5, 3), '7-10'),
   ('§Re-Crucifying Jesus', '11-14'),
   (E(5, 4), '11-14')],
  [(K(5, 1), '1-3'),
   (K(5, 2), '4-6'),
   (K(5, 3), '7-10'),
   ('§예수님을 다시 십자가에 못 박다', '11-14'),
   (K(5, 5), '11-14')],
  changes=[
    'Ch5: badges already match MSG (1-3 / 4-6 / 7-10 / 11-14)',
    'Ch5: removed EN-added §Jesus the Great High Priest (MSG has no header before 5:1-3); added MSG own header §Re-Crucifying Jesus (badged 11-14)',
    'Ch5: replaced KO-only headers §위대한 대제사장 예수님 / "그리스도 안에서 쑥쑥 자라가자" with §예수님을 다시 십자가에 못 박다 (badged 11-14)'])
en_patch.append(en5); ko_patch.append(ko5)

# ---------------- CH 6 ----------------
e48 = E(6, 2) + ' ' + E(6, 3)
e1318 = E(6, 5).replace("saying, \"I'm gonna bless you like crazy.\"",
                        "saying, \"I'm gonna bless you like crazy—bless and bless and bless!\"")
e1820 = ("So for us, who are running to God for safety, we can grab onto that hope and never let go. It's like a "
         "spiritual lifeline that goes past all appearances right into the very presence of God, where Jesus, "
         "running on ahead of us, has taken up his permanent post as our High Priest in the order of Melchizedek.")
s6 = [{'msg_range': '18', 'paras': [4, 5],
       'note': 'MSG 13-18 and 18-20 overlap on v18; badges kept as printed in MSG'}]
en6, ko6 = chap(6,
  [(E(6, 1), '1-3'),
   (e48, '4-8'),
   (E(6, 4), '9-12'),
   ('§God Gave His Word', '13-18'),
   (e1318, '13-18'),
   (e1820, '18-20')],
  [(K(6, 1), '1-3'),
   (K(6, 2), '4-8'),
   (K(6, 3), '9-12'),
   ('§하나님이 말씀을 주셨다', '13-18'),
   (K(6, 5), '13-18'),
   (K(6, 6), '18-20')],
  splits=s6,
  changes=[
    'Ch6: badges corrected to MSG (1-3 / 4-8 / 9-12 / 13-18 / 18-20); declared v18 overlap of 13-18 and 18-20 in splits',
    'Ch6: merged EN over-split 4-8 + 7-8 paras into single MSG 4-8 para (re-crucified + parched-ground field)',
    'Ch6: removed EN-added §Warning Against Falling Away (MSG has no header before 6:1-3); added MSG own header §God Gave His Word (badged 13-18)',
    'Ch6: restored "bless and bless and bless!" in EN 13-18; restored "past all appearances... in the order of Melchizedek" in EN 18-20',
    'Ch6: removed KO-only headers §타락에 대한 경고 / "변치 않는 하나님의 약속"; rebadged KO 19-20 to 18-20'])
en_patch.append(en6); ko_patch.append(ko6)

# ---------------- CH 7 ----------------
en7, ko7 = chap(7,
  [('§Melchizedek, Priest of God', '1-3'),
   (E(7, 1), '1-3'),
   (E(7, 2), '4-7'),
   (E(7, 3), '8-10'),
   ('§A Permanent Priesthood', '11-14'),
   (E(7, 4), '11-14'),
   (E(7, 5), '15-19'),
   (E(7, 6), '20-22'),
   (E(7, 7), '23-25'),
   (E(7, 8), '26-28')],
  [('§하나님의 제사장, 멜기세덱', '1-3'),
   (K(7, 2), '1-3'),
   (K(7, 3), '4-7'),
   (K(7, 4), '8-10'),
   ('§영원한 제사장직', '11-14'),
   (K(7, 6), '11-14'),
   (K(7, 7), '15-19'),
   (K(7, 8), '20-22'),
   (K(7, 9), '23-25'),
   (K(7, 10), '26-28')],
  changes=[
    'Ch7: badges corrected to MSG (1-3 / 4-7 / 8-10 / 11-14 / 15-19 / 20-22 / 23-25 / 26-28)',
    'Ch7: replaced EN-added §Melchizedek with MSG own header §Melchizedek, Priest of God (badged 1-3)',
    'Ch7: added MSG own header §A Permanent Priesthood (badged 11-14) in EN and KO',
    'Ch7: replaced KO-only headers §멜기세덱 / §영원한 제사장이신 예수 with §하나님의 제사장, 멜기세덱 (1-3) and §영원한 제사장직 (11-14)'])
en_patch.append(en7); ko_patch.append(ko7)

# ---------------- CH 8 ----------------
e613 = E(8, 3) + ' ' + E(8, 4)
k613 = K(8, 4) + ' ' + K(8, 5) + ' ' + K(8, 6) + ' ' + K(8, 7)
en8, ko8 = chap(8,
  [('§A New Plan with Israel', '1-2'),
   (E(8, 1), '1-2'),
   (E(8, 2), '3-5'),
   (e613, '6-13')],
  [('§이스라엘과의 새 계획', '1-2'),
   (K(8, 2), '1-2'),
   (K(8, 3), '3-5'),
   (k613, '6-13')],
  changes=[
    'Ch8: badges corrected to MSG (1-2 / 3-5 / 6-13)',
    'Ch8: replaced EN-added §The New Covenant with MSG own header §A New Plan with Israel (badged 1-2)',
    'Ch8: merged EN split 6-10 + 13 paras into single MSG 6-13 para (new covenant poem + old plan on the shelf)',
    'Ch8: replaced KO-only headers §새 언약 / "새로운 약속" with §이스라엘과의 새 계획 (badged 1-2); merged KO 7-8+8-9+10-12+13 into single 6-13 para'])
en_patch.append(en8); ko_patch.append(ko8)

# ---------------- CH 9 ----------------
e15 = E(9, 1) + " We don't have time to get into all the details right now, though."
en9, ko9 = chap(9,
  [('§A Visible Parable', '1-5'),
   (e15, '1-5'),
   (E(9, 2), '6-10'),
   ('§Pointing to the Realities of Heaven', '11-15'),
   (E(9, 3), '11-15'),
   (E(9, 4), '16-17'),
   (E(9, 5), '18-22'),
   (E(9, 6), '23-26'),
   (E(9, 7), '27-28')],
  [('§눈에 보이는 비유', '1-5'),
   (K(9, 2), '1-5'),
   (K(9, 3), '6-10'),
   ('§하늘의 진짜를 가리키는 단서', '11-15'),
   (K(9, 5), '11-15'),
   (K(9, 6), '16-17'),
   (K(9, 7), '18-22'),
   (K(9, 8), '23-26'),
   (K(9, 9), '27-28')],
  changes=[
    'Ch9: badges corrected to MSG (1-5 / 6-10 / 11-15 / 16-17 / 18-22 / 23-26 / 27-28)',
    'Ch9: replaced EN-added §The Heavenly Tabernacle with MSG own header §A Visible Parable (badged 1-5)',
    'Ch9: added MSG own header §Pointing to the Realities of Heaven (badged 11-15) in EN and KO',
    'Ch9: restored "We don\'t have time to comment on these now" in EN 1-5',
    'Ch9: replaced KO-only headers §하늘의 성막 / "§눈에 보이는 비유, 성소" with §눈에 보이는 비유 (badged 1-5)'])
en_patch.append(en9); ko_patch.append(ko9)

# ---------------- CH 10 ----------------
e3239 = E(10, 9) + ' ' + E(10, 10)
s10 = [{'msg_range': '1-10', 'paras': [1, 2, 3],
        'note': 'MSG prints 1-10 as one paragraph block (incl. Christ prophecy); kept as 3 teen paragraphs sharing the badge'},
       {'msg_range': '11-18', 'paras': [4, 5],
        'note': 'MSG prints 11-18 as one paragraph block (incl. Holy Spirit confirmation); kept as 2 teen paragraphs sharing the badge'}]
en10, ko10 = chap(10,
  [('§The Sacrifice of Jesus', '1-10'),
   (E(10, 1), '1-10'),
   (E(10, 2), '1-10'),
   (E(10, 3), '1-10'),
   (E(10, 4), '11-18'),
   (E(10, 5), '11-18'),
   ("§Don't Throw It All Away", '19-21'),
   (E(10, 6), '19-21'),
   (E(10, 7), '22-25'),
   (E(10, 8), '26-31'),
   (e3239, '32-39')],
  [('§예수님의 희생', '1-10'),
   (K(10, 2), '1-10'),
   (K(10, 3), '1-10'),
   (K(10, 4), '1-10'),
   (K(10, 5), '11-18'),
   (K(10, 6), '11-18'),
   ('§다 버리지 마라', '19-21'),
   (K(10, 8), '19-21'),
   (K(10, 9), '22-25'),
   (K(10, 10), '26-31'),
   (K(10, 11), '32-39')],
  splits=s10,
  changes=[
    'Ch10: badges corrected to MSG (1-10 / 11-18 / 19-21 / 22-25 / 26-31 / 32-39); declared shared-badge splits for 1-10 and 11-18',
    'Ch10: replaced EN-added §Christ\'s Perfect Sacrifice with MSG own header §The Sacrifice of Jesus (badged 1-10)',
    'Ch10: added MSG own header §Don\'t Throw It All Away (badged 19-21) in EN and KO',
    'Ch10: merged EN over-split 32-35 + 36-39 paras into single MSG 32-39 para',
    'Ch10: removed KO-only lines §그리스도의 완전한 희생 / "예수님의 희생, 이건 진짜 굉장한 거임" / "확신을 가지고 나아가라!"'])
en_patch.append(en10); ko_patch.append(ko10)

# ---------------- CH 11 ----------------
e20 = "Isaac, with faith, blessed his sons Jacob and Esau for the future."
e21 = "Jacob, on his deathbed, blessed each of Joseph's sons."
e22 = "And Joseph, as he was dying, told everyone that Israel would leave Egypt and even planned his own burial."
e23 = ("Moses' parents hid him for three months after he was born because they saw he was a special kid and "
       "weren't scared of the king's orders.")
e2428 = ("When Moses grew up, he refused to be called a prince of Egypt. He chose to suffer with God's people rather "
         "than live a cushy life of sin. He knew that sticking with the Messiah was worth more than all the treasure "
         "in Egypt. He wasn't scared of the king's rage because he kept his eyes on the God no one can see. And by "
         "faith, he kept the Passover Feast and sprinkled the Passover blood on each house, so the destroyer of the "
         "firstborn wouldn't touch them.")
e29 = "By faith, the Israelites walked right through the Red Sea on dry land. The Egyptians tried to follow and got totally wiped out."
e30 = "By faith, the Israelites marched around Jericho for seven days and the walls just fell down."
e31 = ("And Rahab, a prostitute in Jericho, had faith and welcomed the spies, so she was saved when everyone else "
       "who didn't trust God was destroyed.")
e3238 = E(11, 13) + ' ' + E(11, 14)
en11, ko11 = chap(11,
  [('§Faith in What We Don\'t See', '1-2'),
   (E(11, 1), '1-2'),
   (E(11, 2), '3'),
   (E(11, 3), '4'),
   (E(11, 4), '5-6'),
   (E(11, 5), '7'),
   (E(11, 6), '8-10'),
   (E(11, 7), '11-12'),
   (E(11, 8), '13-16'),
   (E(11, 9), '17-19'),
   (e20, '20'), (e21, '21'), (e22, '22'),
   (e23, '23'), (e2428, '24-28'),
   (e29, '29'), (e30, '30'), (e31, '31'),
   (e3238, '32-38'),
   (E(11, 15), '39-40')],
  [('§보이지 않는 것을 믿는 믿음', '1-2'),
   (K(11, 2), '1-2'),
   (K(11, 3), '3'),
   (K(11, 4), '4'),
   (K(11, 5), '5-6'),
   (K(11, 6), '7'),
   (K(11, 7), '8-10'),
   (K(11, 8), '11-12'),
   (K(11, 9), '13-16'),
   (K(11, 10), '17-19'),
   (K(11, 11), '20'), (K(11, 12), '21'), (K(11, 13), '22'),
   (K(11, 14), '23'), (K(11, 15), '24-28'),
   (K(11, 16), '29'), (K(11, 17), '30'), (K(11, 18), '31'),
   (K(11, 19), '32-38'),
   (K(11, 20), '39-40')],
  changes=[
    'Ch11: badges corrected to MSG granularity (1-2 / 3 / 4 / 5-6 / 7 / 8-10 / 11-12 / 13-16 / 17-19 / 20 / 21 / 22 / 23 / 24-28 / 29 / 30 / 31 / 32-38 / 39-40)',
    'Ch11: replaced EN-added §The Faith Hall of Fame with MSG own header §Faith in What We Don\'t See (badged 1-2); removed KO-only §믿음의 명예의 전당',
    'Ch11: split EN merged 20-22 para into MSG\'s 20 (Isaac), 21 (Jacob), 22 (Joseph) paras',
    'Ch11: split EN merged 23-26 para into 23 (Moses\' parents) and 24-28 (Moses grown)',
    'Ch11: restored omitted Passover in EN 24-28 ("kept the Passover Feast and sprinkled the Passover blood on each house, so the destroyer of the firstborn wouldn\'t touch them")',
    'Ch11: split EN merged 29-31 para into MSG\'s 29 (Red Sea), 30 (Jericho), 31 (Rahab) paras',
    'Ch11: merged EN over-split 32-34 + 35-38 paras into single MSG 32-38 para'])
en_patch.append(en11); ko_patch.append(ko11)

# ---------------- CH 12 ----------------
e411 = ("And for real, in this battle against sin, you haven't even come close to what others have gone through, let "
        "alone the ultimate sacrifice Jesus made. So, no feeling sorry for yourself. Think of it like this: God is "
        "your dad, and he's training you. When you get disciplined, don't just shrug it off, but don't get totally "
        "crushed by it either. It's because he loves you that he corrects you. This isn't a punishment; it's a "
        "training montage to make you stronger. It might be rough at the moment, but later on, you'll see the payoff. "
        "You'll be spiritually jacked and have a solid connection with God.")
e1213 = ("So, no more slacking! Get up, get moving, and clear the path for the long-distance runners — help your "
         "friends out so nobody gets left behind or twists an ankle. And run for it!")
e1821 = ("Remember, you're not dealing with the old-school, scary version of meeting God — like your ancestors at "
         "that terrifying, fiery mountain.")
e2224 = ("Nah, you've got an invite to something way better. You've come to Mount Zion, the city of the living God. "
         "It's a massive party with tons of angels and all the other followers of Christ. You've come to Jesus, the "
         "guy who hooked us up with a brand-new deal with God. His death wasn't a call for revenge; it was a "
         "shout-out of pure grace.")
s12 = [{'msg_range': '1-3', 'paras': [1, 2],
        'note': 'MSG 1-3 kept as 2 teen paragraphs sharing the badge (cheering crowd + keep eyes on Jesus/adrenaline)'}]
en12, ko12 = chap(12,
  [('§Discipline in a Long-Distance Race', '1-3'),
   (E(12, 1), '1-3'),
   (E(12, 2), '1-3'),
   (e411, '4-11'),
   (e1213, '12-13'),
   (E(12, 5), '14-17'),
   ('§An Unshakable Kingdom', '18-21'),
   (e1821, '18-21'),
   (e2224, '22-24'),
   (E(12, 7), '25-27'),
   (E(12, 8), '28-29')],
  [('§장거리 경주에서의 훈련', '1-3'),
   (K(12, 2), '1-3'),
   (K(12, 3), '1-3'),
   (K(12, 5) + ' ' + K(12, 6) + ' ' + K(12, 7), '4-11'),
   (K(12, 8), '12-13'),
   (K(12, 9), '14-17'),
   ('§흔들리지 않는 나라', '18-21'),
   (K(12, 11), '18-21'),
   (K(12, 12), '22-24'),
   (K(12, 13), '25-27'),
   (K(12, 14), '28-29')],
  splits=s12,
  changes=[
    'Ch12: badges corrected to MSG (1-3 / 4-11 / 12-13 / 14-17 / 18-21 / 22-24 / 25-27 / 28-29); 1-3 shared by 2 teen paras (split declared)',
    'Ch12: replaced EN-added §Running the Race with MSG own header §Discipline in a Long-Distance Race (badged 1-3)',
    'Ch12: removed EN-added §God\'s Discipline (MSG has no header there); split EN merged 4-13 para into 4-11 (discipline) and 12-13 (clear the path) paras',
    'Ch12: added MSG own header §An Unshakable Kingdom (badged 18-21) in EN and KO',
    'Ch12: split EN merged 18-24 para into 18-21 (Sinai) and 22-24 (Zion) paras',
    'Ch12: removed KO-only headers §달려야 할 경주 / §절대 포기하지 마 / §하나님의 훈련 / §은혜의 말씀을 무시한 자들에게 주는 경고; merged KO 1-2+3 into shared 1-3 paras and KO 4+5-6+7-11 into 4-11'])
en_patch.append(en12); ko_patch.append(ko12)

# ---------------- CH 13 ----------------
e9 = (E(13, 4) + " Those knockoff 'Christian' products don't do much for anyone who buys them.")
e1012 = ("The altar where God gives us the gift of himself isn't some buffet for insiders to grab and loot. In the "
        "old system, the animals were killed and their bodies disposed of outside the camp, while the blood was "
        "brought inside to the altar as a sacrifice for sin. It's the same with Jesus — he was crucified outside the "
        "city gates, and that's where he poured out the sacrificial blood that was brought to God's altar to cleanse "
        "his people.")
e1315 = ("So let's go outside, where Jesus is, where the action is — not trying to be privileged insiders, but taking "
         "our share of the heat along with Jesus. This insider world isn't our home; we've got our eyes peeled for "
         "the City that's coming. Let's take our place outside with Jesus, pouring out sacrificial praises from our "
         "lips to God in Jesus' name instead of animal blood.")
e16 = ("And don't slack on working for the common good — keep doing good stuff and sharing what you have. God takes "
       "particular pleasure in that kind of 'sacrifice,' the kind that happens in the kitchen, at work, and on the "
       "streets.")
e2021 = ("May the God of peace, who brought back Jesus our Great Shepherd from the dead through the blood sacrifice "
         "that sealed the eternal covenant, hook you up with everything you need to please him. May he work in us "
         "what gives him most pleasure, through Jesus the Messiah. All glory to Jesus forever and always! "
         "Oh, yes, yes, yes.")
e2223 = ("P.S. I kept this short and sweet, so take it seriously. Good news! Timothy's out of jail. If he's quick, "
         "I'll bring him with me when I visit.")
e24 = "Say hi to all your leaders and everyone else. The crew from Italy says 'sup."
k1012 = K(13, 6) + ' ' + K(13, 7) + ' ' + K(13, 8)
k1315 = K(13, 9) + ' ' + K(13, 10) + ' ' + K(13, 11)
en13, ko13 = chap(13,
  [('§Jesus Doesn\'t Change', '1-4'),
   (E(13, 1), '1-4'),
   (E(13, 2), '5-6'),
   (E(13, 3), '7-8'),
   (e9, '9'),
   (e1012, '10-12'),
   (e1315, '13-15'),
   (e16, '16'),
   (E(13, 7), '17'),
   (E(13, 8), '18-19'),
   (e2021, '20-21'),
   (e2223, '22-23'),
   (e24, '24'),
   (E(13, 11), '25')],
  [('§예수님은 변하지 않으신다', '1-4'),
   (K(13, 2), '1-4'),
   (K(13, 3), '5-6'),
   (K(13, 4), '7-8'),
   (K(13, 5), '9'),
   (k1012, '10-12'),
   (k1315, '13-15'),
   (K(13, 12), '16'),
   (K(13, 13), '17'),
   (K(13, 14), '18-19'),
   (K(13, 15), '20-21'),
   (K(13, 16), '22-23'),
   (K(13, 17), '24'),
   (K(13, 18), '25')],
  changes=[
    'Ch13: badges corrected to MSG (1-4 / 5-6 / 7-8 / 9 / 10-12 / 13-15 / 16 / 17 / 18-19 / 20-21 / 22-23 / 24 / 25)',
    'Ch13: replaced EN-added §Final Instructions with MSG own header §Jesus Doesn\'t Change (badged 1-4)',
    'Ch13: restored "Products named after Christ don\'t seem to do much for those who buy them" in EN 9',
    'Ch13: restored omitted 10-12 content in EN (altar not for insider exploitation; blood brought inside to the altar to cleanse)',
    'Ch13: restored omitted 13-15 content in EN ("go outside, where Jesus is, where the action is"; insider world not our home; eyes peeled for the coming City)',
    'Ch13: restored omitted 16 content in EN (common good; sacrifices in kitchen, workplace, streets)',
    'Ch13: restored "through the blood sacrifice that sealed the eternal covenant" and "Oh, yes, yes, yes" in EN 20-21',
    'Ch13: split EN merged 22-24 para into MSG\'s 22-23 and 24 paras; rebadged 24-25 to 25',
    'Ch13: removed KO-only headers §마지막 지시 / "하나님이 기뻐하시는 제사"; merged KO 10+11+12 into 10-12 and KO 13+14+15 into 13-15'])
en_patch.append(en13); ko_patch.append(ko13)

outdir = os.path.join(BASE, 'fixes')
json.dump(en_patch, open(os.path.join(outdir, 'en_Hebrews.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(ko_patch, open(os.path.join(outdir, 'ko_Hebrews.json'), 'w'), ensure_ascii=False, indent=1)
print('written:', len(en_patch), 'chapters')
r = subprocess.run([sys.executable, os.path.join(BASE, 'validate_translation.py'),
                    os.path.join(outdir, 'en_Hebrews.json'),
                    os.path.join(outdir, 'ko_Hebrews.json')],
                   capture_output=True, text=True)
print(r.stdout, r.stderr)
sys.exit(r.returncode)
