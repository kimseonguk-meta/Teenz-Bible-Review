#!/usr/bin/env python3
"""Leviticus 감사 리뷰 덤퍼: 장별 MSG/EN/KO side-by-side + 숫자 기계 검사.
Usage: python3 review_leviticus.py <ch> [--full]
"""
import json, re, sys

REVIEW = '/home/hatch/workspace/teenz-bible-review'
sys.path.insert(0, f'{REVIEW}/gdocs_build')
from build_gdocs import parse_msg_lines


def vr_str(vs):
    vs = sorted(vs)
    return f'{vs[0]}-{vs[-1]}' if len(vs) > 1 else f'{vs[0]}'


def expand(vr):
    if '-' in vr:
        a, b = vr.split('-')
        return set(range(int(a), int(b) + 1))
    return {int(vr)}


en_all = {c['chapter']: c for c in json.load(open(f'{REVIEW}/fixes/en_Leviticus.json'))}
ko_all = {c['chapter']: c for c in json.load(open(f'{REVIEW}/fixes/ko_Leviticus.json'))}
units = parse_msg_lines(open(f'{REVIEW}/msg_Leviticus.txt', encoding='utf-8').read())
msg_by_ch = {}
for u in units:
    msg_by_ch.setdefault(u['chapter'], []).append(u)

NUM_RE = re.compile(r"\b\d+(?:\.\d+)?(?:st|nd|rd|th)?\b")
WORD_NUMS = re.compile(r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|twenty|thirty|forty|fifty|hundred|thousand|half|third|tenth|seventh|fifth|double|triple)\b", re.I)

# english words -> canonical digit for comparison
W2N = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
       'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'twenty':20,'thirty':30,
       'forty':40,'fifty':50,'hundred':100,'thousand':1000,'half':0.5,'third':3,'tenth':10,
       'seventh':7,'fifth':5,'double':2,'triple':3}


def msg_numbers(text):
    out = []
    for m in NUM_RE.finditer(text):
        out.append((m.group(), m.start()))
    for m in WORD_NUMS.finditer(text):
        out.append((m.group(), m.start()))
    return out


def num_present(token, teen):
    t = teen.lower()
    tok = token.lower()
    if tok in W2N:
        n = W2N[tok]
        # accept digit or word
        pat = re.compile(r'\b(' + '|'.join(k for k, v in W2N.items() if v == n) + r'|' + str(int(n) if n==int(n) else n) + r')\b', re.I)
        return bool(pat.search(t))
    digits = re.sub(r'(st|nd|rd|th)$', '', tok)
    try:
        n = float(digits)
    except ValueError:
        return tok in t
    pat = re.compile(r'\b(' + str(int(n) if n == int(n) else n) + r'|' + '|'.join(k for k, v in W2N.items() if v == n) + r')\b', re.I)
    return bool(pat.search(t))


def main():
    ch = int(sys.argv[1])
    full = '--full' in sys.argv
    en, ko = en_all[ch], ko_all[ch]
    mus = msg_by_ch[ch]
    print(f'########## LEVITICUS {ch} — EN {len(en["paragraphs"])}p / KO {len(ko["paragraphs"])}p ##########')
    print(f'EN title: {en["title"]}\nKO title: {ko["title"]}')
    print(f'MSG units: {[vr_str(u["verses"]) for u in mus]}')
    print(f'EN badges: {en["verseRanges"]}')
    print(f'KO badges: {ko["verseRanges"]}')
    print('=' * 100)
    n = max(len(en['paragraphs']), len(ko['paragraphs']), len(mus))
    for i in range(n):
        print(f'\n----- para {i} -----')
        if i < len(mus):
            txt = ' '.join(mus[i]['blocks'])
            print(f'[MSG {vr_str(mus[i]["verses"])}] {txt}')
            # number flags vs EN para i (if badge overlaps)
            if i < len(en['paragraphs']):
                vs = set()
                for v in expand(en['verseRanges'][i]):
                    vs.add(v)
                mu_vs = set(mus[i]['verses'])
                if vs & mu_vs:
                    flags = []
                    for tok, _ in msg_numbers(txt):
                        if not num_present(tok, en['paragraphs'][i]):
                            # context snippet
                            flags.append(tok)
                    if flags:
                        print(f'  !! MSG numbers possibly missing in EN: {sorted(set(flags))}')
        if i < len(en['paragraphs']):
            print(f'[EN {en["verseRanges"][i]}] {en["paragraphs"][i]}')
        if i < len(ko['paragraphs']):
            kvr = ko['verseRanges'][i] if i < len(ko['verseRanges']) else '?'
            print(f'[KO {kvr}] {ko["paragraphs"][i]}')


if __name__ == '__main__':
    main()
