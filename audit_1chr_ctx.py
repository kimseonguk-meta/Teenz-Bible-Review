#!/usr/bin/env python3
"""Show MSG sentence context for each flagged token, chapter by chapter."""
import json, re, sys

sys.path.insert(0, 'gdocs_build')
from build_gdocs import parse_msg_txt

msg = parse_msg_txt('msg_1Chronicles.txt')
en = {c['chapter']: c for c in json.load(open('fixes/en_1Chronicles.json'))}

def norm(s):
    return s.replace('\u2019', "'").replace('\u2018', "'").lower()

SKIP = {'Some','Many','Draw','Stay','Courage','Bless','Play','Broadcast','Revel',
        'Study','Remember','Seed','Publish','Stand','Master','Somebody','Canvass',
        'Pull','Charge','Stretched','Singlehandedly','Mighty','Hardly','Pond',
        'Levitical','Concerning','Nobody',
        'Administrators','Both','Furthermore','Great','Sea','Thus','Revelation',
        'Canaanite','Judean','Twenty-four'}

ch = int(sys.argv[1])
tokens = [t for t in sys.argv[2].split(',')]
msg_units = [(u, b) for u in msg if u['chapter'] == ch for b in u['blocks']]
en_low = norm(' '.join(en[ch]['paragraphs']))
for t in tokens:
    if t in SKIP:
        continue
    key = t.split("'")[0].lower()
    variants = {key, key.replace('-', ''), key.replace('-', ' ')}
    variants |= {key[:-1]} if key.endswith('s') else {key + 's'}
    if any(v in en_low for v in variants):
        print(f'--- {t}: present (variant) ---')
        continue
    print(f'=== {t} ===')
    for u, b in msg_units:
        if t.split("'")[0] in b or key in norm(b):
            vs = sorted(u['verses'])
            print(f'  MSG [{vs[0]}-{vs[-1]}]: {b[:340]}')
