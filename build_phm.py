#!/usr/bin/env python3
"""Teenz Bible 재감사 패치 빌더 — Philemon."""
import json, re, subprocess, sys, os

BASE = os.path.expanduser('~/workspace/teenz-bible-review')
EN_SRC = json.load(open(os.path.expanduser('~/workspace/teenz-fix/client/src/data/allBibleData.json')))
KO_SRC = json.load(open('/tmp/ko_15books.json'))
BOOK = 'Philemon'
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

p13 = E(1, 1).replace("Hope God's dropping nothing but blessings on you.",
                      "Hope God's dropping nothing but blessings on you. Christ's blessings on you!")
en1, ko1 = chap(1,
  [(p13, '1-3'),
   (E(1, 2), '4-7'),
   ('§To Call the Slave Your Friend', '8-9'),
   (E(1, 3), '8-9'),
   (E(1, 4), '10-14'),
   (E(1, 5), '15-16'),
   (E(1, 6), '17-20'),
   (E(1, 7), '21-22'),
   (E(1, 8), '23-25')],
  [(K(1, 1), '1-3'),
   (K(1, 2), '4-7'),
   ('§종을 친구로 받아줘라', '8-9'),
   (K(1, 4), '8-9'),
   (K(1, 5), '10-14'),
   (K(1, 6), '15-16'),
   (K(1, 7), '17-20'),
   (K(1, 8), '21-22'),
   (K(1, 9), '23-25')],
  changes=[
    'Ch1: badges corrected to MSG (1-3 / 4-7 / 8-9 / 10-14 / 15-16 / 17-20 / 21-22 / 23-25)',
    'Ch1: moved MSG own header §To Call the Slave Your Friend to its MSG position (badged 8-9, after 4-7); removed EN-added §A Plea for Onesimus from the chapter start',
    'Ch1: replaced KO-only headers §오네시모를 위한 부탁 / §노예가 친구가 됨 with §종을 친구로 받아줘라 (badged 8-9)',
    'Ch1: restored "Christ\'s blessings on you!" in EN 1-3 (MSG "God\'s best to you! Christ\'s blessings on you!")'])

outdir = os.path.join(BASE, 'fixes')
json.dump([en1], open(os.path.join(outdir, 'en_Philemon.json'), 'w'), ensure_ascii=False, indent=1)
json.dump([ko1], open(os.path.join(outdir, 'ko_Philemon.json'), 'w'), ensure_ascii=False, indent=1)
print('written: 1 chapter')
r = subprocess.run([sys.executable, os.path.join(BASE, 'validate_translation.py'),
                    os.path.join(outdir, 'en_Philemon.json'),
                    os.path.join(outdir, 'ko_Philemon.json')],
                   capture_output=True, text=True)
print(r.stdout, r.stderr)
sys.exit(r.returncode)
