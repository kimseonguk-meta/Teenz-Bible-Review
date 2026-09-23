#!/usr/bin/env python3
"""Side-by-side MSG vs EN (+KO) view for auditing one chapter.
Usage: view_ch.py <BookEN> <chapter>   (BookEN: Psalms|Proverbs|Ecclesiastes|'Song of Solomon')
Prints MSG paras with ranges, then EN paras with badges, then KO paras.
"""
import json, sys, textwrap

BOOK = sys.argv[1]
CH = int(sys.argv[2])
SLUG = {'Psalms':'Psalms','Proverbs':'Proverbs','Ecclesiastes':'Ecclesiastes',
        'Song of Solomon':'SongOfSongs'}[BOOK]

msg = {c['chapter']: c['paras'] for c in json.load(open(f'msg_paras_{SLUG}.json'))}
en_all = json.load(open('/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json'))
en = {c['num']: c for c in en_all[BOOK]}[CH]

ko = None
try:
    import re
    ts = open('/home/hatch/workspace/teenz-fix/client/src/data/gospelDataKo.ts', encoding='utf-8').read()
    # find book block: "<Book>": [ ... ]  - crude: locate '"Song of Solomon"' etc.
    key = f'"{BOOK}"'
    i = ts.find(key)
    # not robust; fallback: skip KO
except Exception as e:
    pass

print(f'=== {BOOK} ch{CH}: {en["title"]}')
print(f'--- MSG ({len(msg[CH])} paras) ---')
for r, t in msg[CH]:
    print(f'[{r}] {t[:220]}')
print(f'--- EN ({len(en["paragraphs"])} paras) ---')
for b, p in zip(en['verseRanges'], en['paragraphs']):
    print(f'[{b}] {p[:220]}')
