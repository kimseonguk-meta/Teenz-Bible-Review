#!/usr/bin/env python3
"""1Chronicles MSG vs Teen EN side-by-side audit view."""
import json, re, sys

sys.path.insert(0, 'gdocs_build')
from build_gdocs import parse_msg_txt

msg = parse_msg_txt('msg_1Chronicles.txt')
en = {c['chapter']: c for c in json.load(open('fixes/en_1Chronicles.json'))}

def fmt_badge(u):
    vs = sorted(u['verses'])
    if not vs: return '?'
    ranges = []
    s = p = vs[0]
    for v in vs[1:]:
        if v == p + 1: p = v
        else: ranges.append((s, p)); s = p = v
    ranges.append((s, p))
    return ','.join(str(a) if a == b else f'{a}-{b}' for a, b in ranges)

ch = int(sys.argv[1])
print(f'########## CHAPTER {ch} ##########')
print('== MSG UNITS ==')
for u in [u for u in msg if u['chapter'] == ch]:
    for b in u['blocks']:
        print(f'  [MSG {fmt_badge(u)}] {b[:260]}')
print('== EN PARAGRAPHS ==')
e = en[ch]
for i, (p, vr) in enumerate(zip(e['paragraphs'], e['verseRanges'])):
    print(f'  [EN {vr}] ({i}) {p[:260]}')
print('== EN msg_ranges ==')
print(' ', e['msg_ranges'])
print('== splits/merges ==')
print('  splits:', e.get('splits'))
print('  merges:', e.get('merges'))
