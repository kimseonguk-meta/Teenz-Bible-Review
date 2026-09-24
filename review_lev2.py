#!/usr/bin/env python3
"""Leviticus 감사 리뷰 덤퍼 v2: 배지 기준 MSG/EN/KO side-by-side + 숫자 기계 검사.
Usage: python3 review_lev2.py <ch>
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
W2N = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
       'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'twenty':20,'thirty':30,
       'forty':40,'fifty':50,'hundred':100,'thousand':1000,'half':0.5,'third':3,'tenth':10,
       'seventh':7,'fifth':5,'double':2,'triple':3}


def num_present(token, teen):
    t = teen.lower()
    tok = token.lower()
    if tok in W2N:
        n = W2N[tok]
        names = [k for k, v in W2N.items() if v == n]
        pat = re.compile(r'\b(' + '|'.join(names) + r'|' + (str(int(n)) if n == int(n) else str(n)) + r')\b', re.I)
        return bool(pat.search(t))
    digits = re.sub(r'(st|nd|rd|th)$', '', tok)
    try:
        n = float(digits)
    except ValueError:
        return tok in t
    names = [k for k, v in W2N.items() if v == n]
    pat = re.compile(r'\b(' + (str(int(n)) if n == int(n) else str(n)) + (('|'+'|'.join(names)) if names else '') + r')\b', re.I)
    return bool(pat.search(t))


def main():
    ch = int(sys.argv[1])
    en, ko = en_all[ch], ko_all[ch]
    mus = msg_by_ch[ch]
    print(f'########## LEVITICUS {ch} ##########')
    print(f'EN title: {en["title"]}\nKO title: {ko["title"]}')
    print(f'MSG units: {[vr_str(u["verses"]) for u in mus]}')
    print(f'EN badges: {en["verseRanges"]}')
    print(f'KO badges: {ko["verseRanges"]}')
    print('=' * 110)
    np_ = max(len(en['paragraphs']), len(ko['paragraphs']))
    for i in range(np_):
        b = en['verseRanges'][i] if i < len(en['verseRanges']) else '?'
        vs = expand(b) if b != '?' else set()
        print(f'\n----- EN para {i} [{b}] -----')
        rel = [u for u in mus if set(u['verses']) & vs]
        for u in rel:
            txt = ' '.join(u['blocks'])
            print(f'[MSG {vr_str(u["verses"])}] {txt[:1400]}')
            if len(txt) > 1400:
                print('   [...truncated]')
            flags = []
            for m in NUM_RE.finditer(txt):
                if not num_present(m.group(), en['paragraphs'][i] if i < len(en['paragraphs']) else ''):
                    flags.append(m.group())
            for m in WORD_NUMS.finditer(txt):
                if not num_present(m.group(), en['paragraphs'][i] if i < len(en['paragraphs']) else ''):
                    flags.append(m.group())
            if flags:
                print(f'  !! numbers possibly missing in EN: {sorted(set(flags))}')
        if i < len(en['paragraphs']):
            print(f'[EN] {en["paragraphs"][i][:1600]}')
        if i < len(ko['paragraphs']):
            kvr = ko['verseRanges'][i] if i < len(ko['verseRanges']) else '?'
            print(f'[KO {kvr}] {ko["paragraphs"][i][:1600]}')


if __name__ == '__main__':
    main()
