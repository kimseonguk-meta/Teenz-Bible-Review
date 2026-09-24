#!/usr/bin/env python3
"""Populate splits metadata for existing Teen paragraph splits (documentation only, no structural changes)."""
import json
from collections import defaultdict

REVIEW = '/home/hatch/workspace/teenz-bible-review'
en = json.load(open(f'{REVIEW}/fixes/en_Numbers.json', encoding='utf-8'))
ko = json.load(open(f'{REVIEW}/fixes/ko_Numbers.json', encoding='utf-8'))

for bk in [en, ko]:
    for ch in bk:
        # Find badges that appear on multiple paragraphs
        badge_to_paras = defaultdict(list)
        for i, b in enumerate(ch['verseRanges']):
            badge_to_paras[b].append(i)
        
        # Build splits list (only for badges on 2+ paras)
        splits = []
        for badge in sorted(badge_to_paras.keys()):
            paras = badge_to_paras[badge]
            if len(paras) > 1:
                splits.append({'msg_range': badge, 'paras': paras})
        
        ch['splits'] = splits

json.dump(en, open(f'{REVIEW}/fixes/en_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("splits metadata populated")
