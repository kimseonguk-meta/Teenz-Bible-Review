#!/usr/bin/env python3
"""Extract KO chapters for a book from gospelDataKo.ts -> ko_<slug>_raw.json
Usage: python3 ko_extract.py Joshua
"""
import json, re, sys

def extract_ko(book):
    text = open('/home/hatch/workspace/teenz-fix/client/src/data/gospelDataKo.ts', encoding='utf-8').read()
    m = re.search(r'"' + re.escape(book) + r'"\s*:\s*\[', text)
    if not m:
        raise SystemExit(f'book {book} not found')
    start = m.end()
    depth = 1; i = start
    while depth > 0:
        c = text[i]
        if c == '[': depth += 1
        elif c == ']': depth -= 1
        i += 1
    block = text[start:i]
    objs = []
    d = 0; s = None; instr = False; esc = False
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
    chaps = {}
    for o in objs:
        nm = re.search(r'"num"\s*:\s*(\d+)', o)
        if not nm: continue
        num = int(nm.group(1))
        pm = re.search(r'"paragraphs"\s*:\s*\[(.*?)\]\s*,\s*"verseRanges"', o, re.S)
        raw = pm.group(1) if pm else ''
        paras = []; cur = ''; instr2 = False; esc2 = False
        for c in raw:
            if instr2:
                if esc2: cur += c; esc2 = False
                elif c == '\\': esc2 = True; cur += c
                elif c == '"': instr2 = False; paras.append(cur); cur = ''
                else: cur += c
            else:
                if c == '"': instr2 = True; cur = ''
        paras = [p.replace('\\"', '"').replace('\\\\', '\\').replace('\\n', '\n') for p in paras]
        vm = re.search(r'"verseRanges"\s*:\s*\[(.*?)\]\s*\}', o, re.S)
        vrs = []
        if vm:
            for x in re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', vm.group(1)):
                x = x.strip()
                if x in ('null', ''): vrs.append(None)
                else: vrs.append(x.strip('"'))
        chaps[num] = {'paragraphs': paras, 'verseRanges': vrs}
    return chaps

if __name__ == '__main__':
    book = sys.argv[1]
    slug = book.replace(' ', '')
    chaps = extract_ko(book)
    json.dump(chaps, open(f'ko_{slug}_raw.json', 'w'), ensure_ascii=False)
    print(f'{book}: {len(chaps)} chapters -> ko_{slug}_raw.json')
