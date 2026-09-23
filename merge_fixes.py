#!/usr/bin/env python3
"""Merge per-chapter teen drafts into fixes/en_<Key>.json / fixes/ko_<Key>.json.

Reads fixes/work_<Key>/en_ch<NN>.json and ko_ch<NN>.json, sorts by chapter,
verifies chapter sequence continuity, writes merged list JSON.
Usage: python3 merge_fixes.py Exodus 40
"""
import json, os, sys

BOOKS = {'exodus': 'Exodus', 'leviticus': 'Leviticus', 'numbers': 'Numbers',
         'deuteronomy': 'Deuteronomy', 'judges': 'Judges',
         '1samuel': '1Samuel', '2samuel': '2Samuel'}

def main():
    key = BOOKS[sys.argv[1].lower()]
    nch = int(sys.argv[2])
    root = os.path.dirname(os.path.abspath(__file__))
    wdir = os.path.join(root, 'fixes', f'work_{key}')
    out = {}
    for lang in ('en', 'ko'):
        items = []
        for ch in range(1, nch + 1):
            fn = os.path.join(wdir, f'{lang}_ch{ch:02d}.json')
            if not os.path.exists(fn):
                raise SystemExit(f'MISSING: {fn}')
            d = json.load(open(fn, encoding='utf-8'))
            if d['chapter'] != ch:
                raise SystemExit(f'{fn}: chapter field {d["chapter"]} != {ch}')
            items.append(d)
        out[lang] = items
    for lang, items in out.items():
        opath = os.path.join(root, 'fixes', f'{lang}_{key}.json')
        json.dump(items, open(opath, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'{lang}: {len(items)} chapters -> {opath}')

if __name__ == '__main__':
    main()
