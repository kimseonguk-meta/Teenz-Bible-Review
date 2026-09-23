#!/usr/bin/env python3
"""Detect KO paragraph misalignment: for each chapter, check whether KO para[i]
actually corresponds to the MSG content of EN para[i]'s badge (vs a shifted unit).
Prints chapters where KO content seems shifted relative to badges.
Usage: python3 detect_shift.py <BookKey>
"""
import json, os, re, sys

REVIEW = '/home/hatch/workspace/teenz-bible-review'
sys.path.insert(0, os.path.join(REVIEW, 'gdocs_build'))
import build_gdocs as bg

STOP = set(('the','a','an','and','of','to','in','is','you','your','i','my','me','we','our',
            'it','he','his','she','her','they','their','them','that','this','for','with','on',
            'at','as','by','from','be','are','was','were','will','would','not','no','but','or',
            'so','do','does','did','have','has','had','what','when','how','why','who','whom',
            'all','up','out','down','over','under','into','then','than','just','like','god','lord'))

def expand(s):
    vs = set()
    for part in str(s).split(','):
        part = part.strip()
        if not part: continue
        if '-' in part:
            a, b = part.split('-'); vs.update(range(int(a), int(b)+1))
        else: vs.add(int(part))
    return vs

def content_words(t):
    return set(w for w in re.findall(r"[A-Za-z']+", (t or '').lower())
               if w not in STOP and len(w) > 3)

def ko_content_words(t):
    # Korean: extract noun-ish stems; also keep english loanwords
    ws = set(re.findall(r"[A-Za-z]+", (t or '').lower()))
    kr = re.findall(r"[가-힣]{2,}", t or '')
    # crude stemming: strip common particles
    stems = set()
    for w in kr:
        for suf in ('에서','으로','로','을','를','이','가','은','는','의','에','와','과','도','만','에게','한테','처럼','같이','보다','까지','부터','라고','이라고','야','아','어','네','지','고','면','며','며','써','줘','줘서'):
            if w.endswith(suf) and len(w) > len(suf) + 1:
                w = w[:-len(suf)]; break
        stems.add(w)
    return ws | stems

# rough EN->KO gloss map for distinctive MSG words (Song/Ps/Prov/Ecc common)
GLOSS = {
 'jerusalem':'예루살렘','solomon':'솔로몬','david':'다윗','israel':'이스라엘','zion':'시온',
 'lebanon':'레바논','tirzah':'디르사','kedar':'게달','gedi':'엔게디','sharon':'사론','shulammite':'술람미',
 'pharaoh':'파라오','gazelle':'가젤','apricot':'살구','myrrh':'몰약','frankincense':'유향',
 'wisdom':'지혜','fool':'바보','righteous':'의인','wicked':'악인','oath':'맹세',
 'vineyard':'포도밭','garden':'정원','foxes':'여우','doves':'비둘기','lily':'백합','lotus':'연꽃',
}

def main():
    key = sys.argv[1]
    en_chs = bg.load_teen('en', key)
    ko_chs = bg.load_teen('ko', key)
    ko_by_ch = {c['chapter']: c for c in ko_chs}
    units = bg.parse_msg_txt(os.path.join(REVIEW, f'msg_{key}.txt'))
    by_ch = {}
    for u in units:
        by_ch.setdefault(u['chapter'], []).append(u)

    for ce in en_chs:
        ch = ce['chapter']
        ck = ko_by_ch[ch]
        msg_us = by_ch.get(ch, [])
        mtexts = [' '.join(u.get('blocks', [])) for u in msg_us]
        msets = [u['verses'] if isinstance(u['verses'], set) else expand(u['verses']) for u in msg_us]
        problems = []
        for i, ep in enumerate(ce['paragraphs']):
            if ep.lstrip().startswith('§'):
                continue
            kp = ck['paragraphs'][i] if i < len(ck['paragraphs']) else ''
            if kp.lstrip().startswith('§'):
                problems.append(f'para{i}: KO is §-header but EN is body')
                continue
            vset = expand(ce['verseRanges'][i])
            # expected MSG content = units overlapping badge
            exp_words = set()
            for j in range(len(msg_us)):
                if msets[j] & vset:
                    exp_words |= content_words(mtexts[j])
            # translate expected EN words to KO glosses where known
            exp_ko = set(GLOSS.get(w, w) for w in exp_words)
            kwords = ko_content_words(kp)
            hit = len(exp_ko & kwords)
            # also check: does KO para match a DIFFERENT msg unit better?
            best_j, best_hit = -1, 0
            for j in range(len(msg_us)):
                uw = content_words(mtexts[j])
                uko = set(GLOSS.get(w, w) for w in uw)
                h = len(uko & kwords)
                if h > best_hit:
                    best_hit, best_j = h, j
            if hit <= 1 and best_hit >= 3 and best_j >= 0:
                exp_v = sorted(set().union(*[msets[j] for j in range(len(msg_us)) if msets[j] & vset])) if vset else []
                problems.append(f'para{i} badge={ce["verseRanges"][i]}: KO matches MSG unit {sorted(msets[best_j])} instead (hit {hit} vs {best_hit})')
            elif hit <= 1 and len(exp_ko) > 4:
                problems.append(f'para{i} badge={ce["verseRanges"][i]}: KO has almost no overlap with expected MSG content (hit {hit})')
        if problems:
            print(f'== {key} ch{ch} ==')
            for p in problems:
                print('  ', p)

if __name__ == '__main__':
    main()
