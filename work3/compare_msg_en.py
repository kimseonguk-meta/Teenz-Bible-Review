#!/usr/bin/env python3
"""장별 MSG 구조 vs EN carried_over 구조 비교 리포트."""
import json, re, sys

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

REVIEW = '/home/hatch/workspace/teenz-bible-review/'

def report(book):
    msg = {c['chapter']: c for c in json.load(open(f'{REVIEW}msg_parsed_{book}.json'))}
    en = {c['chapter']: c for c in json.load(open(f'{REVIEW}fixes/en_{book}.json'))}
    print(f'########## {book} ##########')
    for ch in sorted(set(msg) | set(en)):
        e = en.get(ch)
        if not e or e.get('review_status') != 'carried_over':
            continue
        m = msg.get(ch)
        mb = [p['badge'] for p in m['paras']]
        eb = [(b if b is not None else 'null') for b in e['verseRanges']]
        mset = set().union(*[expand(b) for b in mb]) if mb else set()
        eset = set().union(*[expand(b) for b in eb]) if eb else set()
        miss = sorted(mset - eset)   # MSG엔 있는데 EN에 없음
        extra = sorted(eset - mset)  # EN엔 있는데 MSG에 없음
        hdr = sum(1 for p in e['paragraphs'] if p.lstrip().startswith('§'))
        flag = ''
        if miss: flag += f' MISS{miss}'
        if extra: flag += f' EXTRA{extra}'
        if len(mb) != len(e['paragraphs']): flag += f' NPARA(msg{len(mb)}/en{len(e["paragraphs"])})'
        if mb != eb: flag += ' BADGESEQ'
        print(f' ch{ch}: msg[{",".join(mb)}]')
        print(f'      en [{",".join(eb)}] hdr={hdr}{flag}')

if __name__ == '__main__':
    for b in sys.argv[1:]:
        report(b)
