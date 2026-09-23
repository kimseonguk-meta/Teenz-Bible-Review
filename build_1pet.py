#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — 1 Peter (5장)."""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))
KO_SRC = json.load(open('/tmp/ko_15books.json'))
BOOK = '1 Peter'
EN_CH = {c['num']: c for c in EN_SRC[BOOK]}
KO_CH = {c['num']: c for c in KO_SRC[BOOK]}
EN_TITLE = {c['num']: c.get('title', '') for c in EN_SRC[BOOK]}

def E(ch, i): return EN_CH[ch]['paragraphs'][i]
def K(ch, i):
    s = KO_CH[ch]['paragraphs'][i].replace('\\n', '\n')
    return re.sub(r'^\d+(-\d+)?(절)?\.?::?\s*', '', s)

def flat_poem(s):
    return ' '.join(l.lstrip('> ').strip() for l in s.split('\n') if l.strip())

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
e2225 = E(1, 9) + ' ' + ' '.join(flat_poem(E(1, i)) for i in (10, 11, 12, 13)) + ' ' + E(1, 14)
en1, ko1 = chap(1,
  [(E(1, 1), '1-2'),
   ('§A New Life', '3-5'),
   (E(1, 2), '3-5'),
   (E(1, 3), '6-7'),
   (E(1, 4), '8-9'),
   (E(1, 5), '10-12'),
   ('§A Future in God', '13-16'),
   (E(1, 6), '13-16'),
   (E(1, 7), '17'),
   (E(1, 8), '18-21'),
   (e2225, '22-25')],
  [(K(1, 1), '1-2'),
   ('§새 생명', '3-5'),
   (K(1, 3), '3-5'),
   (K(1, 4), '6-7'),
   (K(1, 5), '8-9'),
   (K(1, 6), '10-12'),
   ('§하나님의 생명으로 만들어진 라이프스타일', '13-16'),
   (K(1, 8), '13-16'),
   (K(1, 9), '17'),
   (K(1, 10), '18-21'),
   (flat_poem(K(1, 11)), '22-25')],
  changes=[
    'Ch1: badges already match MSG (1-2 / 3-5 / 6-7 / 8-9 / 10-12 / 13-16 / 17 / 18-21 / 22-25)',
    'Ch1: removed EN-added §A Living Hope (MSG has no header before 1:1-2); added MSG own header §A New Life (badged 3-5)',
    'Ch1: added MSG own header §A Future in God (badged 13-16) in EN and KO',
    'Ch1: merged EN over-split 22-25 prose + 4 poem lines + closing into single MSG 22-25 para',
    'Ch1: removed KO-only headers §살아있는 소망'])
en_patch.append(en1); ko_patch.append(ko1)

# ---------------- CH 2 ----------------
e1112 = ("Friends, this world is not your home, so don't make yourselves cozy in it. Don't indulge your ego at the "
         "expense of your soul. Live an exemplary life in your neighborhood so that your actions will refute their "
         "prejudices. Then they'll be won over to God's side and be there to join in the celebration when he arrives.")
k1820 = ("종으로 일하는 너네, 주인한테 착한 종이 되어줘. 좋은 주인한테만 그런 게 아니라 나쁜 주인한테도 그래야 함. "
         "억울하게 나쁜 대우를 받아도 하나님 때문에 참고 견디는 게 진짜 중요한 거임. 잘못해서 벌받는 걸 참는 건 별로 "
         "대단한 거 아님. 근데 착하게 행동하다가 나쁜 대우를 받아도 계속 착한 종으로 살면, 그게 하나님한테 인정받는 거임.")
k48 = flat_poem(K(2, 2)) + ' ' + flat_poem(K(2, 3)) + ' ' + flat_poem(K(2, 4))
k2125 = flat_poem(K(2, 10)) + ' ' + flat_poem(K(2, 11)) + ' ' + flat_poem(K(2, 12))
en2, ko2 = chap(2,
  [(E(2, 1), '1-3'),
   ('§The Stone', '4-8'),
   (E(2, 2), '4-8'),
   (E(2, 3), '9-10'),
   (e1112, '11-12'),
   (E(2, 4), '13-17'),
   ('§The Kind of Life He Lived', '18-20'),
   (E(2, 5), '18-20'),
   (E(2, 6), '21-25')],
  [(K(2, 1), '1-3'),
   ('§돌', '4-8'),
   (k48, '4-8'),
   (K(2, 5), '9-10'),
   (K(2, 6), '11-12'),
   (K(2, 7), '13-17'),
   ('§그리스도가 사셨던 삶', '18-20'),
   (k1820, '18-20'),
   (k2125, '21-25')],
  changes=[
    'Ch2: badges already match MSG (1-3 / 4-8 / 9-10 / 11-12 / 13-17 / 18-20 / 21-25)',
    'Ch2: removed EN-added §Living Stones (MSG has no header before 2:1-3); added MSG own header §The Stone (badged 4-8)',
    'Ch2: restored omitted 11-12 in EN ("this world is not your home"; exemplary life refutes prejudices; won over when he arrives)',
    'Ch2: added MSG own header §The Kind of Life He Lived (badged 18-20) in EN; added § to KO "그리스도가 사셨던 삶"',
    'Ch2: restored omitted 18-20 in KO (servants and masters; suffering unjustly for God counts)',
    'Ch2: removed KO-only header §살아있는 돌; merged KO 4-8 prose+poem and 21-25 prose+poem into single paras'])
en_patch.append(en2); ko_patch.append(ko2)

# ---------------- CH 3 ----------------
e812 = (E(3, 4) + ' Whoever wants to embrace life and see good days, here\'s what to do: say nothing evil or hurtful; '
        'snub evil and cultivate good; run after peace for all you\'re worth. God looks on all this with approval, '
        'listening and responding well to what he\'s asked; but he turns his back on those who do evil things.')
k812 = flat_poem(K(3, 5)) + ' ' + flat_poem(K(3, 6))
s3 = [{'msg_range': '4', 'paras': [1, 2],
       'note': 'MSG 1-4 and 4-6 overlap on v4; badges kept as printed in MSG'}]
en3, ko3 = chap(3,
  [('§Cultivate Inner Beauty', '1-4'),
   (E(3, 1), '1-4'),
   (E(3, 2), '4-6'),
   (E(3, 3), '7'),
   ('§Suffering for Doing Good', '8-12'),
   (e812, '8-12'),
   (E(3, 5), '13-18'),
   (E(3, 6), '19-22')],
  [('§내면의 아름다움을 레벨업하자', '1-4'),
   (K(3, 2), '1-4'),
   (K(3, 3), '4-6'),
   (K(3, 4), '7'),
   ('§착한 일 하다가 고난받을 때', '8-12'),
   (k812, '8-12'),
   (K(3, 8), '13-18'),
   (K(3, 9), '19-22')],
  splits=s3,
  changes=[
    'Ch3: badges already match MSG (1-4 / 4-6 / 7 / 8-12 / 13-18 / 19-22); declared v4 overlap of 1-4 and 4-6 in splits',
    'Ch3: replaced EN-added §Submit for the Lord\'s Sake with MSG own header §Cultivate Inner Beauty (badged 1-4)',
    'Ch3: added MSG own header §Suffering for Doing Good (badged 8-12) in EN; added § to KO "착한 일 하다가 고난받을 때"',
    'Ch3: restored omitted Psalm 34 poem in EN 8-12 (embrace life; snub evil; God turns his back on evildoers)',
    'Ch3: removed KO-only header §주님을 위해 순종하라; merged KO 8-12 prose+poem into single para'])
en_patch.append(en3); ko_patch.append(ko3)

# ---------------- CH 4 ----------------
en4, ko4 = chap(4,
  [('§Learn to Think Like Him', '1-2'),
   (E(4, 1), '1-2'),
   (E(4, 2), '3-5'),
   (E(4, 3), '6'),
   (E(4, 4), '7-11'),
   ('§Glory Just Around the Corner', '12-13'),
   (E(4, 5), '12-13'),
   (E(4, 6), '14-16'),
   (E(4, 7), '17-19')],
  [('§예수님처럼 생각하기', '1-2'),
   (K(4, 2), '1-2'),
   (K(4, 3), '3-5'),
   (K(4, 4), '6'),
   (K(4, 5), '7-11'),
   ('§고난을 기쁘게 여기기', '12-13'),
   (K(4, 7), '12-13'),
   (K(4, 8), '14-16'),
   (K(4, 9), '17-19')],
  changes=[
    'Ch4: badges already match MSG (1-2 / 3-5 / 6 / 7-11 / 12-13 / 14-16 / 17-19)',
    'Ch4: replaced EN-added §Suffering for Doing Good with MSG own header §Learn to Think Like Him (badged 1-2)',
    'Ch4: added MSG own header §Glory Just Around the Corner (badged 12-13) in EN and KO',
    'Ch4: replaced KO-only headers §선을 행하며 고난받다 / "예수님처럼 생각하기" / "고난을 기쁘게 여기기" with § versions (badged 1-2 and 12-13)',
    'Ch4: EN 17-19 and KO 17-19 verified complete (incl. "If good people barely make it" poem) — no restoration needed'])
en_patch.append(en4); ko_patch.append(ko4)

# ---------------- CH 5 ----------------
e12 = E(5, 5) + ' ' + E(5, 6)
en5, ko5 = chap(5,
  [("§He'll Promote You at the Right Time", '1-3'),
   (E(5, 1), '1-3'),
   (E(5, 2), '4-5'),
   (E(5, 3), '6-7'),
   ('§He Gets the Last Word', '8-11'),
   (E(5, 4), '8-11'),
   (e12, '12'),
   (E(5, 7), '13-14')],
  [('§때가 되면 하나님이 높여주실 거야', '1-3'),
   (K(5, 2), '1-3'),
   (K(5, 3), '4-5'),
   (K(5, 4), '6-7'),
   ('§마지막 말씀은 하나님이 하신다', '8-11'),
   (K(5, 6), '8-11'),
   (K(5, 7), '12'),
   (K(5, 8), '13-14')],
  changes=[
    'Ch5: badges already match MSG (1-3 / 4-5 / 6-7 / 8-11 / 12 / 13-14)',
    'Ch5: replaced EN-added §Shepherding the Flock with MSG own header §He\'ll Promote You at the Right Time (badged 1-3)',
    'Ch5: added MSG own header §He Gets the Last Word (badged 8-11) in EN and KO',
    'Ch5: merged EN over-split v12 two paras into single MSG 12 para',
    'Ch5: replaced KO-only headers §양 떼를 돌보라 / "하나님의 양들을 돌보는 리더들" / "정신 바짝 차려" with § versions (badged 1-3 and 8-11)'])
en_patch.append(en5); ko_patch.append(ko5)

outdir = os.path.join(BASE, 'fixes')
json.dump(en_patch, open(os.path.join(outdir, 'en_1Peter.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(ko_patch, open(os.path.join(outdir, 'ko_1Peter.json'), 'w'), ensure_ascii=False, indent=1)
print('written:', len(en_patch), 'chapters')
r = subprocess.run([sys.executable, os.path.join(BASE, 'validate_translation.py'),
                    os.path.join(outdir, 'en_1Peter.json'),
                    os.path.join(outdir, 'ko_1Peter.json')],
                   capture_output=True, text=True)
print(r.stdout, r.stderr)
sys.exit(r.returncode)
