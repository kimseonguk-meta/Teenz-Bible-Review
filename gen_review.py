#!/usr/bin/env python3
"""Generate per-chapter review files: MSG vs EN vs KO side-by-side full text.
Usage: python3 gen_review.py Acts
Output: /tmp/review_Acts/ch01.txt ... ch28.txt
"""
import json, os, sys


def expand(vr):
    out = set()
    for part in str(vr).split(','):
        part = part.strip()
        if not part:
            continue
        if '-' in part:
            a, b = part.split('-')
            out.update(range(int(a), int(b) + 1))
        elif part.isdigit():
            out.add(int(part))
    return out


def main():
    book = sys.argv[1]
    slug = book.replace(' ', '')
    msg = json.load(open(f'msg_{slug}_parsed.json', encoding='utf-8'))['chapters']
    en_all = json.load(open('/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json',
                            encoding='utf-8'))
    ko_all = json.load(open(f'msg_work/ko_{slug}.json', encoding='utf-8'))
    en_ch = {c['num']: c for c in en_all[book]}
    outdir = f'/tmp/review_{slug}'
    os.makedirs(outdir, exist_ok=True)
    for n in sorted(en_ch.keys()):
        ms = msg.get(str(n), [])
        en = en_ch[n]
        ko = ko_all.get(str(n), {})
        L = []
        L.append(f'=== {book} ch{n} "{en["title"]}" ===')
        msg_set, en_set, ko_set = set(), set(), set()
        for s in ms:
            msg_set |= expand(s['range'])
        for b in en['verseRanges']:
            if b:
                en_set |= expand(b)
        for b in ko.get('verseRanges', []):
            if b:
                ko_set |= expand(b)
        L.append(f'MSG paras={len(ms)} ranges=[{",".join(s["range"] for s in ms)}]')
        L.append(f'EN  paras={len(en["paragraphs"])} ranges=[{",".join(str(b) for b in en["verseRanges"])}]')
        L.append(f'KO  paras={len(ko.get("paragraphs", []))} ranges=[{",".join(str(b) for b in ko.get("verseRanges", []))}]')
        miss = sorted(msg_set - en_set)
        extra = sorted(en_set - msg_set)
        komiss = sorted(msg_set - ko_set)
        if miss:
            L.append(f'!! MSG verses missing from EN badges: {miss}')
        if extra:
            L.append(f'!! EN badges outside MSG: {extra}')
        if komiss:
            L.append(f'!! MSG verses missing from KO badges: {komiss}')
        L.append('')
        L.append('--- MSG ---')
        for s in ms:
            hdr = f' [HDR: {s["header"]}]' if s['header'] else ''
            L.append(f'[{s["range"]}]{hdr}')
            L.append(s['text'])
            L.append('')
        L.append('--- EN ---')
        for i, p in enumerate(en['paragraphs']):
            L.append(f'[para{i} badge={en["verseRanges"][i]}]')
            L.append(p)
            L.append('')
        L.append('--- KO ---')
        for i, p in enumerate(ko.get('paragraphs', [])):
            L.append(f'[para{i} badge={ko.get("verseRanges", ["?"]*99)[i]}]')
            L.append(p)
            L.append('')
        open(f'{outdir}/ch{n:02d}.txt', 'w', encoding='utf-8').write('\n'.join(L))
    print(f'{book}: review files in {outdir}')


if __name__ == '__main__':
    main()
