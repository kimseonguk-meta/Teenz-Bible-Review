#!/usr/bin/env python3
"""Normalize splits declarations in Leviticus fixes to validator dict format.
Removes string entries appended by apply_leviticus_fixes.py and writes proper
{'msg_range': ..., 'paras': [...]} dicts with correct para indices.
"""
import json

REVIEW = '/home/hatch/workspace/teenz-bible-review'
en = json.load(open(f'{REVIEW}/fixes/en_Leviticus.json'))
ko = json.load(open(f'{REVIEW}/fixes/ko_Leviticus.json'))
E = {c['chapter']: c for c in en}
K = {c['chapter']: c for c in ko}

def clean(ch):
    for c in (E[ch], K[ch]):
        c['splits'] = [s for s in c.get('splits', []) if isinstance(s, dict)]

def add(ch, entries, langs=('EN', 'KO')):
    for lang in langs:
        c = E[ch] if lang == 'EN' else K[ch]
        c.setdefault('splits', []).extend(entries)

# --- ch3: MSG structural overlap v16 (12-16 / 16-17) ---
clean(3)
add(3, [{'msg_range': '16', 'paras': [2, 3],
         'note': 'MSG overlap: v16 closes 12-16 and opens 16-17; Teen mirrors MSG'}])

# --- ch4 ---
clean(4)
add(4, [{'msg_range': '1-12', 'paras': [0, 1]},
        {'msg_range': '32-35', 'paras': [7, 8]}])
# existing dicts 22-26->[3,4], 27-31->[5,6] already correct

# --- ch10: consolidate v3 entries ---
clean(10)
add(10, [{'msg_range': '3', 'paras': [1, 2, 3]},
         {'msg_range': '6-7', 'paras': [5, 6]}])

# --- ch12 ---
clean(12)
add(12, [{'msg_range': '6-7', 'paras': [1, 2]}])

# --- ch13 ---
clean(13)
add(13, [{'msg_range': '1-3', 'paras': [0, 1]}])

# --- ch18 ---
clean(18)
add(18, [{'msg_range': '23', 'paras': [18, 19]}])

# --- ch19: rewrite with post-split indices; EN gets the v18 parity split ---
clean(19)
base19 = [{'msg_range': '3', 'paras': [1, 2]},
          {'msg_range': '11', 'paras': [6, 7]},
          {'msg_range': '11', 'paras': [6, 8]},
          {'msg_range': '13', 'paras': [10, 11]},
          {'msg_range': '16', 'paras': [14, 15]},
          {'msg_range': '19', 'paras': [19, 20]},
          {'msg_range': '19', 'paras': [19, 21]},
          {'msg_range': '19', 'paras': [19, 22]},
          {'msg_range': '26', 'paras': [25, 26]},
          {'msg_range': '28', 'paras': [28, 29]}]
add(19, base19, langs=('EN', 'KO'))
add(19, [{'msg_range': '18', 'paras': [17, 18],
          'note': 'Teen-side parity split (EN), not MSG: matches KO two-para v18'}],
    langs=('EN',))

# --- ch20 ---
clean(20)
add(20, [{'msg_range': '1-5', 'paras': [0, 1]},
         {'msg_range': '24-26', 'paras': [18, 19]}])

json.dump(en, open(f'{REVIEW}/fixes/en_Leviticus.json', 'w'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Leviticus.json', 'w'), ensure_ascii=False, indent=1)
print('splits normalized')
for ch in [3, 4, 10, 12, 13, 18, 19, 20]:
    print(f'ch{ch} EN splits:', E[ch]['splits'])
