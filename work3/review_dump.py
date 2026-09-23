#!/usr/bin/env python3
"""검토용 덤프: MSG 문단(전문) + 새 EN 문단(전문)을 절 겹침 기준으로 나란히 출력."""
import json, sys

REVIEW = '/home/hatch/workspace/teenz-bible-review/'

def expand(vr):
    out = set()
    if vr is None: return out
    for part in str(vr).split(','):
        part = part.strip()
        if not part: continue
        if '-' in part:
            a, b = part.split('-'); out.update(range(int(a), int(b) + 1))
        elif part.isdigit(): out.add(int(part))
    return out

def dump(book, ch):
    msg = {c['chapter']: c for c in json.load(open(f'{REVIEW}msg_parsed_{book}.json'))}[ch]
    new = json.load(open(f'{REVIEW}staging/en_{book}_ch{ch}.json'))
    eparas, eb = new['paragraphs'], new['verseRanges']
    print(f'############ {book} ch{ch} (EN {len(eparas)} paras) ############')
    for mp in msg['paras']:
        mset = expand(mp['badge'])
        hdr = f' [§{mp["header"]}]' if mp['header'] else ''
        print(f'--- MSG [{mp["badge"]}]{hdr}')
        print(f'    {mp["text"]}')
        for i, (b, p) in enumerate(zip(eb, eparas)):
            if expand(b) & mset:
                pre = '§ ' if p.lstrip().startswith('§') else ''
                print(f'    EN{i+1} [{b}] {pre}{p[:700]}')
        print()

if __name__ == '__main__':
    dump(sys.argv[1], int(sys.argv[2]))
