#!/usr/bin/env python3
"""Coverage heatmap: for each chapter, MSG verse-set vs EN verseRanges-set.
Usage: python3 heatmap.py msg_paras_<Slug>.json <BookKey>
"""
import json, sys


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


msg = json.load(open(sys.argv[1], encoding='utf-8'))
BOOK = sys.argv[2]
en_data = json.load(open('/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json',
                         encoding='utf-8'))
en_ch = {c['num']: c for c in en_data[BOOK]}
bad = 0
for chs in sorted(msg, key=int):
    ch = int(chs)
    ms = msg[chs]
    en = en_ch.get(ch)
    if en is None:
        print(f'ch{ch}: MISSING EN CHAPTER'); bad += 1; continue
    msg_set = set().union(*[expand(s['range']) for s in ms]) if ms else set()
    en_set = set().union(*[expand(b) for b in en['verseRanges'] if b]) if en['verseRanges'] else set()
    missing = sorted(msg_set - en_set)
    extra = sorted(en_set - msg_set)
    nulls = [i for i, b in enumerate(en['verseRanges']) if not b]
    dup = len(en['paragraphs']) != len(en['verseRanges'])
    nmsg, nen = len(ms), len(en['paragraphs'])
    if missing or extra or nulls or dup or abs(nmsg - nen) > 2:
        bad += 1
        print(f'ch{ch}: msg={nmsg} en={nen} missing={missing or "-"} '
              f'extra={extra or "-"} nulls={nulls or "-"} lendiff={dup}')
print(f'--- {bad} chapters flagged')
