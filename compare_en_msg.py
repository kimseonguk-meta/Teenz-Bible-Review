#!/usr/bin/env python3
"""Compare existing EN (allBibleData.json) against parsed MSG paragraphs.
Prints per-chapter structural diff + side-by-side content snippets.
Usage: python3 compare_en_msg.py msg_paras_Job.json Job [ch_from ch_to]
"""
import json, re, sys


def expand(vr):
    out = set()
    for part in str(vr).split(','):
        part = part.strip()
        if not part:
            continue
        if '-' in part:
            a, b = part.split('-')
            out.update(range(int(a), int(b) + 1))
        elif part.isdigit():
            out.add(int(part))
    return out


BOOK = sys.argv[2]
msg = json.load(open(sys.argv[1], encoding='utf-8'))
en_data = json.load(open('/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json',
                         encoding='utf-8'))
en_ch = {c['num']: c for c in en_data[BOOK]}
ch_from = int(sys.argv[3]) if len(sys.argv) > 3 else 1
ch_to = int(sys.argv[4]) if len(sys.argv) > 4 else max(int(k) for k in msg)

for ch in range(ch_from, ch_to + 1):
    ms = msg.get(str(ch), [])
    en = en_ch.get(ch)
    if en is None:
        print(f'=== ch{ch}: NO EN CHAPTER ==='); continue
    msg_set, en_set = set(), set()
    for s in ms:
        msg_set |= expand(s['range'])
    for b in en['verseRanges']:
        en_set |= expand(b)
    missing = sorted(msg_set - en_set)
    extra = sorted(en_set - msg_set)
    npara = len(en['paragraphs'])
    nmsg = len(ms)
    flag = ''
    if missing or extra:
        flag = '  <<< COVERAGE DIFF'
    print(f'=== ch{ch} "{en["title"]}" msg_paras={nmsg} en_paras={npara} '
          f'msg=[{",".join(s["range"] for s in ms)}] '
          f'en=[{",".join(en["verseRanges"])}]{flag}')
    if missing:
        print(f'    MISSING in EN: {missing}')
    if extra:
        print(f'    EN badges outside MSG: {extra}')
    # side-by-side content snippets
    for s in ms:
        rng = s['range']
        hdr = f' §{s["header"]}' if s['header'] else ''
        print(f'  MSG {rng}{hdr}: {s["text"][:190]}')
    for i, p in enumerate(en['paragraphs']):
        print(f'  EN  {en["verseRanges"][i]}: {p[:150]}')
    print()
