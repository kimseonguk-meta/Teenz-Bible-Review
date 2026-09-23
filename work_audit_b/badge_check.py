#!/usr/bin/env python3
"""Badge-accuracy check: for each EN paragraph, find the MSG unit its content
best matches (token overlap) and compare with its badge.
Flags paras where badge doesn't match content's MSG unit.
Usage: python3 badge_check.py <BookKey> [ch_from] [ch_to]
"""
import json, os, re, sys

REVIEW = '/home/hatch/workspace/teenz-bible-review'
sys.path.insert(0, os.path.join(REVIEW, 'gdocs_build'))
import build_gdocs as bg

STOP = set(('the','a','an','and','of','to','in','is','you','your','i','my','me','we','our',
            'it','he','his','she','her','they','their','them','that','this','for','with','on',
            'at','as','by','from','be','are','was','were','will','would','not','no','but','or',
            'so','do','does','did','have','has','had','what','when','how','why','who','whom',
            'all','up','out','down','over','under','into','then','than','just','like','god','lord',
            'said','say','says','there','their','what','with','this','that','from','have','were'))

def expand(s):
    vs = set()
    for part in str(s).split(','):
        part = part.strip()
        if not part: continue
        if '-' in part:
            a, b = part.split('-'); vs.update(range(int(a), int(b)+1))
        else: vs.add(int(part))
    return vs

def toks(t):
    return set(w for w in re.findall(r"[A-Za-z']+", (t or '').lower())
               if w not in STOP and len(w) > 3)

def main():
    key = sys.argv[1]
    cf = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    ct = int(sys.argv[3]) if len(sys.argv) > 3 else 9999
    en_chs = bg.load_teen('en', key)
    units = bg.parse_msg_txt(os.path.join(REVIEW, f'msg_{key}.txt'))
    by_ch = {}
    for u in units:
        by_ch.setdefault(u['chapter'], []).append(u)
    for ce in en_chs:
        ch = ce['chapter']
        if ch < cf or ch > ct: continue
        msg_us = by_ch.get(ch, [])
        mtexts = [' '.join(u.get('blocks', [])) for u in msg_us]
        mtoks = [toks(t) for t in mtexts]
        msets = [u['verses'] if isinstance(u['verses'], set) else expand(u['verses']) for u in msg_us]
        for i, p in enumerate(ce['paragraphs']):
            if p.lstrip().startswith('§'): continue
            pt = toks(p)
            badge = expand(ce['verseRanges'][i])
            # best matching MSG unit by token overlap
            scores = []
            for j in range(len(msg_us)):
                inter = pt & mtoks[j]
                # jaccard-ish: prefer high overlap relative to unit size
                s = len(inter) / max(1, len(mtoks[j])) if mtoks[j] else 0
                scores.append((s, len(inter), j))
            scores.sort(reverse=True)
            (bs, bi, bj) = scores[0]
            mset = msets[bj]
            # OK if badge matches the best unit (allowing badge to be a subset when MSG unit was split,
            # or badge to span multiple units when merged)
            if not (badge & mset):
                # badge has zero overlap with best-match unit -> definite problem
                print(f'{key} ch{ch} para{i} badge=[{ce["verseRanges"][i]}] content_matches_MSG{sorted(mset)} (overlap {bi} toks, score {bs:.2f})')
            elif not (badge <= mset or mset <= badge):
                # partial overlap: possible split/merge boundary issue - report as info
                # only flag if the best unit is substantially better than badge-overlapping units
                badge_units = [j for j in range(len(msg_us)) if msets[j] & badge]
                bscore = max((len(pt & mtoks[j]) for j in badge_units), default=0)
                if bi >= bscore + 4:
                    print(f'{key} ch{ch} para{i} badge=[{ce["verseRanges"][i]}] PARTIAL: content best matches MSG{sorted(mset)} (badge-unit overlap only {bscore} vs {bi})')

if __name__ == '__main__':
    main()
