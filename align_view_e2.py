#!/usr/bin/env python3
"""Worker E2: chapter alignment viewer — MSG units vs EN paras vs KO paras side by side."""
import json
import sys

sys.path.insert(0, '/home/hatch/workspace/teenz-bible-review/gdocs_build')
from build_gdocs import parse_msg_txt  # noqa: E402

REVIEW = '/home/hatch/workspace/teenz-bible-review'
units = parse_msg_txt(f'{REVIEW}/msg_Jeremiah.txt')
en = json.load(open(f'{REVIEW}/fixes/en_Jeremiah.json', encoding='utf-8'))
ko = json.load(open(f'{REVIEW}/fixes/ko_Jeremiah.json', encoding='utf-8'))


def vr_of(vset):
    v = sorted(vset)
    if not v:
        return '?'
    # compress to ranges
    out, s, p = [], v[0], v[0]
    for x in v[1:]:
        if x == p + 1:
            p = x
        else:
            out.append(str(s) if s == p else f'{s}-{p}')
            s, p = x, x
    out.append(str(s) if s == p else f'{s}-{p}')
    return ','.join(out)


def show(ch, width=100):
    print(f'================ CHAPTER {ch} ================')
    print('--- MSG units ---')
    for u in [x for x in units if x['chapter'] == ch]:
        txt = ' '.join(u['blocks'])
        print(f"  [{vr_of(u['verses'])}] {txt[:width]}")
    e = next(c for c in en if c['chapter'] == ch)
    k = next(c for c in ko if c['chapter'] == ch)
    print(f'--- EN ({len(e["paragraphs"])} paras) ---')
    for i, (b, p) in enumerate(zip(e['verseRanges'], e['paragraphs'])):
        print(f'  p{i} [{b}] {p[:width]}')
    print(f'--- KO ({len(k["paragraphs"])} paras) ---')
    for i, (b, p) in enumerate(zip(k['verseRanges'], k['paragraphs'])):
        print(f'  p{i} [{b}] {p[:width]}')


if __name__ == '__main__':
    for ch in [int(x) for x in sys.argv[1:]]:
        show(ch)
