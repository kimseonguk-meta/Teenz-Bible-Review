#!/usr/bin/env python3
"""Assemble per-chapter cleaned MSG page texts into msg_<Key>.txt.

Reads msg_work/<slug>_ch<NN>.txt, concatenates in chapter order, validates
sequential chapters and that each chapter file starts with a verse marker
'<ch> <range> ...' (matching the canonical msg_*.txt format).
Usage: python3 assemble_msg_book.py leviticus 27
"""
import os, re, sys

def main():
    slug, nch = sys.argv[1], int(sys.argv[2])
    key = {'leviticus': 'Leviticus', 'numbers': 'Numbers',
           'deuteronomy': 'Deuteronomy', '1samuel': '1Samuel',
           '2samuel': '2Samuel', '1kings': '1Kings', '2kings': '2Kings',
           '1chronicles': '1Chronicles', 'ezra': 'Ezra', 'nehemiah': 'Nehemiah',
           'isaiah': 'Isaiah', 'lamentations': 'Lamentations',
           'ezekiel': 'Ezekiel', 'daniel': 'Daniel'}.get(slug, slug)
    wdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'msg_work')
    out = []
    for ch in range(1, nch + 1):
        fn = os.path.join(wdir, f'{slug}_ch{ch:02d}.txt')
        if not os.path.exists(fn):
            raise SystemExit(f'MISSING chapter file: {fn}')
        text = open(fn, encoding='utf-8').read().strip()
        if not text:
            raise SystemExit(f'EMPTY chapter file: {fn}')
        first_line = text.split('\n', 1)[0].strip()
        # first content line must be '<ch> <verse-range>' or a '###' header
        # followed by the chapter marker; find the chapter marker line
        m = re.search(rf'^{ch} (\d+(?:-\d+)?) ', text, re.M)
        if not m:
            raise SystemExit(f'{fn}: no chapter-{ch} verse marker found (first line: {first_line[:60]!r})')
        out.append(text)
    result = '\n\n\n'.join(out) + '\n'
    opath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'msg_{key}.txt')
    open(opath, 'w', encoding='utf-8').write(result)
    print(f'OK: {nch} chapters -> {opath} ({len(result)} chars)')

if __name__ == '__main__':
    main()
