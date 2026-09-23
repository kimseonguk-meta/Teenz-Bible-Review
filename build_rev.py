#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — Revelation (22장)."""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))
KO_SRC = json.load(open('/tmp/ko_15books.json'))
BOOK = 'Revelation'
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
kchant1 = ('"거룩, 거룩, 거룩하신 우리 주 하나님, 전능하신 분, 전에도 계셨고, 지금도 계시고, 앞으로 오실 분!"')
kchant2 = ('"주님! 맞습니다, 우리 하나님! 영광을! 존귀를! 능력을 받으소서! '
           '주님이 모든 걸 만드셨고, 주님이 원하셔서 만들어진 거니까요!"')

# ---------------- CH 1 ----------------
en1, ko1 = chap(1,
  [(E(1, 1), '1-2'),
   (E(1, 2), '3'),
   ('§His Eyes Pouring Fire-Blaze', '4-7'),
   (E(1, 3), '4-7'),
   (E(1, 4), '8'),
   (E(1, 5) + ' ' + E(1, 6), '9-17'),
   (E(1, 7), '17-20')],
  [(K(1, 1), '1-2'),
   (K(1, 2), '3'),
   ('§눈에서 쏟아지는 불꽃', '4-7'),
   (K(1, 3) + ' ' + K(1, 4), '4-7'),
   (K(1, 5), '8'),
   (K(1, 6) + ' ' + K(1, 7) + ' ' + K(1, 8), '9-17'),
   (K(1, 9), '17-20')],
  merges=[{'msg_range': '4-7', 'paras': [3], 'note': 'KO doxology folded into MSG 4-7 block'},
          {'msg_range': '9-17', 'paras': [5], 'note': 'folded over-splits into MSG 9-17 block'}],
  splits=[{'msg_range': '17', 'paras': [5, 6], 'note': 'MSG 9-17 and 17-20 overlap on v17; badges kept as printed'}],
  changes=[
    'Ch1: replaced EN-added §The Revelation of Jesus with MSG own header §His Eyes Pouring Fire-Blaze (badged 4-7)',
    'Ch1: folded over-splits back into MSG 9-17 block (merges recorded); fixed all badges to MSG (4-7 / 8 / 9-17 / 17-20)',
    'Ch1: removed KO-only header §예수님의 계시'])
en_patch.append(en1); ko_patch.append(ko1)

# ---------------- CH 2 ----------------
en2, ko2 = chap(2,
  [('§To Ephesus', '1'),
   (E(2, 1), '1'), (E(2, 2), '2-3'), (E(2, 3), '4-5'), (E(2, 4), '6'), (E(2, 5), '7'),
   ('§To Smyrna', '8'),
   (E(2, 6), '8'), (E(2, 7), '9'), (E(2, 8), '10'), (E(2, 9), '11'),
   ('§To Pergamum', '12'),
   (E(2, 10), '12'), (E(2, 11), '13'), (E(2, 12), '14-15'), (E(2, 13), '16'), (E(2, 14), '17'),
   ('§To Thyatira', '18'),
   (E(2, 15), '18'), (E(2, 16), '19'), (E(2, 17), '20-23'), (E(2, 18), '24-25'), (E(2, 19), '26-28'), (E(2, 20), '29')],
  [('§에베소에 보내는 말씀', '1'),
   (K(2, 2), '1'), (K(2, 3), '2-3'), (K(2, 4), '4-5'), (K(2, 5), '6'), (K(2, 6), '7'),
   ('§서머나에 보내는 말씀', '8'),
   (K(2, 8), '8'), (K(2, 9), '9'), (K(2, 10), '10'), (K(2, 11), '11'),
   ('§버가모에 보내는 말씀', '12'),
   (K(2, 13), '12'), (K(2, 14), '13'), (K(2, 15), '14-15'), (K(2, 16), '16'), (K(2, 17), '17'),
   ('§두아디라에 보내는 말씀', '18'),
   (K(2, 19), '18'), (K(2, 20), '19'), (K(2, 21), '20-23'), (K(2, 22), '24-25'), (K(2, 23), '26-28'), (K(2, 24), '29')],
  changes=[
    'Ch2: content complete; replaced EN-added §Letters to the Churches (Part 1) with MSG headers §To Ephesus / §To Smyrna / §To Pergamum / §To Thyatira',
    'Ch2: added § to KO church labels; fixed all badges to MSG'])
en_patch.append(en2); ko_patch.append(ko2)
