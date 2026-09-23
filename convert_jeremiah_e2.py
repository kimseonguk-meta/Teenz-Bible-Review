#!/usr/bin/env python3
"""Worker E2: work_jeremiah draft JSON -> fixes/en|ko_Jeremiah.json canonical format.

- chapter: num -> chapter
- verseRanges/msg_ranges: draft badges (as-is; badge fixes applied during audit)
- splits: auto-declared for any verse appearing in 2+ paragraph badges
  (connected components of the badge-overlap graph)
- merges: [] (no MSG merges applied; pending candidates go to merge-split-candidates.md)
- changes/confirmations_needed: [] (audit appends)
"""
import json
import re
import sys

sys.path.insert(0, '/home/hatch/workspace/teenz-bible-review')
from validate_translation import expand  # noqa: E402


def badge_set(b):
    return expand(b)


def build_splits(vrs):
    n = len(vrs)
    sets = [badge_set(b) for b in vrs]
    # overlap graph -> connected components
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for i in range(n):
        for j in range(i + 1, n):
            if sets[i] & sets[j]:
                union(i, j)
    comps = {}
    for i in range(n):
        comps.setdefault(find(i), []).append(i)
    splits = []
    for comp in comps.values():
        if len(comp) < 2:
            continue
        u = set()
        for i in comp:
            u |= sets[i]
        lo, hi = min(u), max(u)
        rng = f"{lo}-{hi}" if lo != hi else str(lo)
        splits.append({'msg_range': rng, 'paras': sorted(comp)})
    return splits


def convert(src, lang):
    data = json.load(open(src, encoding='utf-8'))
    out = []
    for ch in data:
        vrs = list(ch['verseRanges'])
        out.append({
            'chapter': ch['num'],
            'title': ch['title'],
            'paragraphs': list(ch['paragraphs']),
            'verseRanges': vrs,
            'msg_ranges': list(vrs),
            'merges': [],
            'splits': build_splits(vrs),
            'changes': [],
            'confirmations_needed': [],
        })
    return out


if __name__ == '__main__':
    en = convert('work_jeremiah/en_jeremiah.json', 'en')
    ko = convert('work_jeremiah/ko_jeremiah.json', 'ko')
    json.dump(en, open('fixes/en_Jeremiah.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    json.dump(ko, open('fixes/ko_Jeremiah.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('wrote fixes/en_Jeremiah.json:', len(en), 'chapters,',
          sum(len(c['paragraphs']) for c in en), 'paragraphs')
    print('wrote fixes/ko_Jeremiah.json:', len(ko), 'chapters,',
          sum(len(c['paragraphs']) for c in ko), 'paragraphs')
    print('total splits declared (en):', sum(len(c['splits']) for c in en))
