#!/usr/bin/env python3
"""MSG 문단 ↔ EN 문단 내용 겹침 분석. 낮은 점수 문단을 수동 검토 대상으로 플래그."""
import json, re, sys

STOP = set('''the and for with that this from they have had were was are his her she him you your our their its who what when where which while with all any can had has have out not but are was were been being than then than them those these there here into over under again once also just even ever never always only very much more most such than too also will would could should shall may might must upon between through during before after above below unto'''.split())

def toks(text):
    ws = re.findall(r"[A-Za-z']+", text.lower())
    return [w for w in ws if len(w) > 4 and w not in STOP]

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

REVIEW = '/home/hatch/workspace/teenz-bible-review/'

def analyze(book, ch):
    msg = {c['chapter']: c for c in json.load(open(f'{REVIEW}msg_parsed_{book}.json'))}[ch]
    en = {c['chapter']: c for c in json.load(open(f'{REVIEW}fixes/en_{book}.json'))}[ch]
    eparas = en['paragraphs']; eb = en['verseRanges']
    print(f'===== {book} {ch} =====')
    for mi, mp in enumerate(msg['paras']):
        mset = expand(mp['badge'])
        mt = toks(mp['text'])
        # 겹치는 EN 문단들 (절 범위 겹침 기준)
        aligned = [i for i, b in enumerate(eb) if expand(b) & mset]
        etext = ' '.join(eparas[i] for i in aligned)
        et = set(toks(etext))
        hit = sum(1 for w in mt if w in et)
        score = hit / max(1, len(mt))
        flag = '  <<<' if score < 0.35 else ''
        print(f'  MSG[{mp["badge"]}] nEN={len(aligned)} score={score:.2f} {mp["text"][:75]}{flag}')
    # EN 문단 중 MSG 어디에도 안 겹치는 것
    msets = [expand(p['badge']) for p in msg['paras']]
    munion = set().union(*msets) if msets else set()
    for i, b in enumerate(eb):
        if not (expand(b) & munion) and not eparas[i].lstrip().startswith('§'):
            print(f'  EN para{i} [{b}] 겹침 없음: {eparas[i][:80]}  <<<')
    # null 배지
    for i, b in enumerate(eb):
        if b is None and not eparas[i].lstrip().startswith('§'):
            print(f'  EN para{i} null 배지: {eparas[i][:80]}')

if __name__ == '__main__':
    book = sys.argv[1]
    for ch in [int(x) for x in sys.argv[2:]]:
        analyze(book, ch)
