#!/usr/bin/env python3
"""Triage completeness FAILs using the checker's own MSG unit loader."""
import json, re, sys
sys.path.insert(0, '/home/hatch/workspace/teenz-bible-review/gdocs_build')
import completeness_check as cc

REVIEW = '/home/hatch/workspace/teenz-bible-review'
units = cc.load_msg_units('Leviticus')
by_ch = {}
for u in units:
    by_ch.setdefault(u['chapter'], []).append(u)

en = json.load(open(f'{REVIEW}/fixes/en_Leviticus.json'))
E = {c['chapter']: c for c in en}

def parse_badge(s):
    m = re.match(r'(\d+)(?:-(\d+))?$', s)
    a, b = int(m.group(1)), int(m.group(2) or m.group(1))
    return set(range(a, b+1))

targets = [tuple(map(int, a.split(':'))) for a in sys.argv[1:]]
for ch, idx in targets:
    c = E[ch]
    badge = c['verseRanges'][idx]
    vset = parse_badge(badge)
    # find MSG units whose verses intersect
    mtexts = []
    for u in by_ch.get(ch, []):
        attr = set(u['verses'])
        if attr & vset:
            mtexts.append(' '.join(u['blocks']))
    print(f'===== ch{ch} idx{idx} badge {badge} =====')
    for mt in mtexts:
        print('MSG :', mt[:1500].replace('\n', ' '))
    print('TEEN:', c['paragraphs'][idx][:1500].replace('\n', ' '))
    print()
