#!/usr/bin/env python3
"""Index-aligned viewer: MSG sections vs EN paragraphs (full text).
Usage: python3 view2.py Joshua 1 3   (chapters 1..3)
"""
import json, sys

def main():
    book = sys.argv[1]
    slug = book.replace(' ', '')
    c0, c1 = int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else int(sys.argv[2])
    en = {c['num']: c for c in json.load(open('/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json'))[book]}
    msg = json.load(open(f'msg_{slug}_parsed.json'))['chapters']
    for n in range(c0, c1 + 1):
        ch = en[n]
        print(f'========== {book} {n}: {ch.get("title","")}')
        msecs = msg[str(n)]
        eparas, eb = ch['paragraphs'], ch['verseRanges']
        print(f'--- MSG ({len(msecs)} sections) ---')
        for i, s in enumerate(msecs):
            hdr = f'[{s["header"]}] ' if s['header'] else ''
            print(f'  m{i} [{s["range"]}] {hdr}{s["text"]}')
        print(f'--- EN ({len(eparas)} paras) ---')
        for i, (p, b) in enumerate(zip(eparas, eb)):
            print(f'  e{i} [{b}] {p}')
        print()

if __name__ == '__main__':
    main()
