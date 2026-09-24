#!/usr/bin/env python3
"""Triage completeness_check FAILs: show MSG unit text vs Teen paragraph."""
import json, re, sys

REVIEW = '/home/hatch/workspace/teenz-bible-review'
en = json.load(open(f'{REVIEW}/fixes/en_Leviticus.json'))
E = {c['chapter']: c for c in en}

# parse msg units (chapter number appears only on first unit of each chapter)
t = open(f'{REVIEW}/msg_Leviticus.txt').read()
units = {}  # (ch, badge) -> text
cur_ch = None
for m in re.finditer(r'(?m)^(?:(\d+) )?(\d+(?:-\d+)?) (.*)$', t):
    if m.group(1):
        cur_ch = int(m.group(1))
    badge = m.group(2)
    # skip section headers like '1 ' etc. — badge must look like a verse range and text non-empty
    if cur_ch and re.fullmatch(r'\d+(?:-\d+)?', badge):
        units[(cur_ch, badge)] = m.group(3)

# which FAILs to show: from argv as ch:idx
targets = []
for a in sys.argv[1:]:
    ch, idx = a.split(':')
    targets.append((int(ch), int(idx)))

for ch, idx in targets:
    c = E[ch]
    badge = c['verseRanges'][idx]
    msg = units.get((ch, badge), '[unit not found]')
    print(f'===== ch{ch} idx{idx} badge {badge} =====')
    print('MSG :', msg[:1200])
    print('TEEN:', c['paragraphs'][idx][:1200])
    print()
