#!/usr/bin/env python3
"""Side-by-side viewer: MSG sections vs EN paragraphs per chapter.
Usage: python3 compare_book.py Joshua [chapter] [--full]
"""
import json, sys, re, textwrap

def load_ko(book):
    """Extract KO chapters for book from gospelDataKo.ts"""
    import subprocess
    # parse the TS file with a simple state machine
    text = open('/home/hatch/workspace/teenz-fix/client/src/data/gospelDataKo.ts').read()
    # find the book's array: "<Book>": [
    m = re.search(r'"' + re.escape(book) + r'"\s*:\s*\[', text)
    if not m:
        return {}
    start = m.end()
    # crude: find matching closing bracket by scanning; chapters are {...} objects
    # Instead, extract chapter objects one by one
    chapters = {}
    pos = start
    # find all {num: N, ...} blocks at depth 1
    depth = 1
    i = start
    cur_start = None
    while i < len(text) and depth > 0:
        c = text[i]
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                break
        i += 1
    block = text[start:i]
    # split into chapter objects by '},' at top level of this block
    objs = []
    d = 0
    s = None
    instr = False
    esc = False
    for j, c in enumerate(block):
        if instr:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == '"': instr = False
            continue
        if c == '"': instr = True
        elif c == '{':
            if d == 0: s = j
            d += 1
        elif c == '}':
            d -= 1
            if d == 0 and s is not None:
                objs.append(block[s:j+1]); s = None
    for o in objs:
        nm = re.search(r'"num"\s*:\s*(\d+)', o)
        if not nm: continue
        num = int(nm.group(1))
        # extract paragraphs array strings
        pm = re.search(r'"paragraphs"\s*:\s*\[(.*)\]\s*,\s*"verseRanges"', o, re.S)
        paras = re.findall(r'"((?:[^"\\]|\\.)*)"', pm.group(1), re.S) if pm else []
        paras = [p.encode().decode('unicode_escape') if '\\' in p else p for p in paras]
        vm = re.search(r'"verseRanges"\s*:\s*\[(.*?)\]', o, re.S)
        vrs = []
        if vm:
            vrs = [x.strip().strip('"') if x.strip() not in ('null','') else None
                   for x in re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', vm.group(1))]
            vrs = [None if x in ('null', '') else x for x in vrs]
        chapters[num] = {'paragraphs': paras, 'verseRanges': vrs}
    return chapters

def main():
    book = sys.argv[1]
    slug = book.replace(' ', '')
    only = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else None
    full = '--full' in sys.argv
    en = json.load(open('/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json'))[book]
    msg = json.load(open(f'msg_{slug}_parsed.json'))['chapters']
    ko = load_ko(book)
    W = 100 if full else 88
    for ch in en:
        n = ch['num']
        if only and n != only: continue
        print(f'########## {book} {n}: {ch.get("title","")}')
        print(f'  EN paras: {len(ch["paragraphs"])}, MSG sections: {len(msg[str(n)])}, KO paras: {len(ko.get(n, {}).get("paragraphs", []))}')
        msecs = msg[str(n)]
        eparas = ch['paragraphs']
        ebadges = ch['verseRanges']
        kparas = ko.get(n, {}).get('paragraphs', [])
        for i in range(max(len(msecs), len(eparas))):
            ms = msecs[i] if i < len(msecs) else None
            ep = eparas[i] if i < len(eparas) else None
            eb = ebadges[i] if i < len(ebadges) else None
            kp = kparas[i] if i < len(kparas) else None
            if ms:
                hdr = f'[{ms["header"]}] ' if ms['header'] else ''
                print(f'  MSG {ms["range"]:>6} {hdr}{ms["text"][:W]}')
            else:
                print('  MSG ------ (none)')
            if ep is not None:
                mark = ''
                print(f'  EN  {str(eb):>6} {ep[:W]}{mark}')
            else:
                print('  EN  ------ (none)')
            if kp is not None and full:
                print(f'  KO  {"":>6} {kp[:W]}')
            print()
        print()

if __name__ == '__main__':
    main()
