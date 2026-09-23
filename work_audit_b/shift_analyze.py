#!/usr/bin/env python3
"""For chapters where badges != msg_ranges, determine if content matches badge
(legitimate re-split) or if there's a systematic badge error.
Usage: python3 shift_analyze.py <BookKey>
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
    en_chs = bg.load_teen('en', key)
    units = bg.parse_msg_txt(os.path.join(REVIEW, f'msg_{key}.txt'))
    by_ch = {}
    for u in units:
        by_ch.setdefault(u['chapter'], []).append(u)
    for ce in en_chs:
        ch = ce['chapter']
        badges = ce['verseRanges']
        msg = ce.get('msg_ranges', [])
        if not msg or badges == msg:
            continue
        msg_us = by_ch.get(ch, [])
        if not msg_us:
            continue
        mtexts = [' '.join(u.get('blocks', [])) for u in msg_us]
        mtoks = [toks(t) for t in mtexts]
        msets = [u['verses'] if isinstance(u['verses'], set) else expand(u['verses']) for u in msg_us]
        match_badge = 0
        total = 0
        details = []
        for i, p in enumerate(ce['paragraphs']):
            if p.lstrip().startswith('§'):
                continue
            total += 1
            pt = toks(p)
            badge = expand(badges[i])
            # find best MSG unit
            best_j, best_s, best_n = -1, 0, 0
            for j in range(len(msg_us)):
                inter = pt & mtoks[j]
                s = len(inter) / max(1, len(mtoks[j]))
                if len(inter) > best_n or (len(inter) == best_n and s > best_s):
                    best_j, best_s, best_n = j, s, len(inter)
            mset = msets[best_j]
            # does badge match the best unit?
            if badge & mset and (badge <= mset or mset <= badge or len(badge & mset) >= len(badge) * 0.5):
                match_badge += 1
            else:
                details.append(f'p{i}[{badges[i]}]->MSG{sorted(mset)}')
        frac = match_badge / max(1, total)
        status = "OK(resplit)" if frac >= 0.7 else "CHECK"
        print(f'{key} ch{ch}: {match_badge}/{total} match badge -> {status}')
        if status == "CHECK" and details:
            for d in details[:6]:
                print(f'    {d}')

if __name__ == '__main__':
    main()
