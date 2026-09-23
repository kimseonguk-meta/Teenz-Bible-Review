#!/usr/bin/env python3
"""Side-by-side audit dump: MSG unit | teen EN | teen KO per chapter.
Flags: word-count ratio, missing distinctive tokens (numbers, proper nouns, quotes).
Usage: python3 dump_sidebyside.py Psalms [start_ch] [end_ch]
"""
import json, os, re, sys

REVIEW = '/home/hatch/workspace/teenz-bible-review'
sys.path.insert(0, os.path.join(REVIEW, 'gdocs_build'))
import build_gdocs as bg

def expand_range(s):
    vs = set()
    for part in str(s).split(','):
        part = part.strip()
        if not part: continue
        if '-' in part:
            a, b = part.split('-')
            vs.update(range(int(a), int(b) + 1))
        else:
            vs.add(int(part))
    return vs

def words(t):
    return len(re.findall(r"[A-Za-z가-힣]+", t or ''))

STOP = set(('the','a','an','and','of','to','in','is','you','your','i','my','me','we','our',
            'it','he','his','she','her','they','their','them','that','this','for','with','on',
            'at','as','by','from','be','are','was','were','will','would','not','no','but','or',
            'so','do','does','did','have','has','had','what','when','how','why','who','whom',
            'all','up','out','down','over','under','into','then','than','just','like','god','lord',
            'god\'s','verse','chapter'))

def distinct_tokens(msg_text):
    toks = set()
    # numbers
    for m in re.findall(r'\b\d{1,3}(?:,\d{3})*\b', msg_text):
        toks.add('NUM:' + m)
    # quoted strings -> content words
    for q in re.findall(r'"([^"]{4,})"', msg_text):
        for w in re.findall(r"[A-Za-z']+", q.lower()):
            if w not in STOP and len(w) > 3:
                toks.add('Q:' + w)
    # proper nouns (capitalized non-sentence-start words)
    for m in re.findall(r'(?<![.!?]\s)(?<!^)\b([A-Z][a-z]{3,})\b', msg_text):
        if m.lower() not in STOP:
            toks.add('PN:' + m.lower())
    return toks

def main():
    key = sys.argv[1]
    ch_from = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    ch_to = int(sys.argv[3]) if len(sys.argv) > 3 else 9999

    en_chs = bg.load_teen('en', key)
    ko_chs = bg.load_teen('ko', key)
    ko_by_ch = {c['chapter']: c for c in ko_chs}
    units = bg.parse_msg_txt(os.path.join(REVIEW, f'msg_{key}.txt'))
    by_ch = {}
    for u in units:
        by_ch.setdefault(u['chapter'], []).append(u)

    out = []
    for ce in en_chs:
        ch = ce['chapter']
        if ch < ch_from or ch > ch_to:
            continue
        ck = ko_by_ch[ch]
        out.append(f'{"="*100}\nCHAPTER {ch}  EN_title="{ce.get("title","")}"  KO_title="{ck.get("title","")}"')
        out.append(f'  EN paras={len(ce["paragraphs"])} KO paras={len(ck["paragraphs"])} msg_units={len(by_ch.get(ch, []))}')
        # align by verse ranges
        msg_us = by_ch.get(ch, [])
        msg_verse_sets = [u['verses'] if isinstance(u['verses'], set) else expand_range(u['verses']) for u in msg_us]
        msg_texts = [' '.join(u.get('blocks', []) or [u.get('text', '')]) for u in msg_us]
        # for each EN para, find overlapping msg units
        for i, p in enumerate(ce['paragraphs']):
            ko_p = ck['paragraphs'][i] if i < len(ck['paragraphs']) else '[KO MISSING PARA]'
            ko_vr = ck['verseRanges'][i] if i < len(ck['verseRanges']) else '?'
            vset = expand_range(ce['verseRanges'][i])
            ovj = [j for j in range(len(msg_us)) if msg_verse_sets[j] & vset]
            out.append(f'\n--- ch{ch} para{i} EN_badge=[{ce["verseRanges"][i]}] KO_badge=[{ko_vr}] ---')
            for j in ovj:
                out.append(f'  MSG[{sorted(msg_verse_sets[j])}]: {msg_texts[j][:500]}')
            out.append(f'  EN : {p[:900]}')
            out.append(f'  KO : {ko_p[:900]}')
            # flags
            msgw = sum(words(msg_texts[j]) for j in ovj)
            enw = words(p)
            ratio = enw / msgw if msgw else 1.0
            flags = []
            if ratio < 0.45:
                flags.append(f'LOW_RATIO {ratio:.2f}')
            # distinctive token check
            msg_all = ' '.join(msg_texts[j] for j in ovj)
            missing = []
            for t in distinct_tokens(msg_all):
                kind, val = t.split(':', 1)
                blob = p.lower()
                if kind == 'NUM':
                    if val not in blob and not re.search(r'\b' + val + r'\b', blob):
                        missing.append(t)
                else:
                    if val not in blob:
                        # allow quote words to appear in ko? no, EN check
                        missing.append(t)
            if missing:
                flags.append('MISSING_TOKENS: ' + ', '.join(sorted(missing)[:12]))
            if flags:
                out.append('  !! FLAGS: ' + ' | '.join(flags))
        # KO extra paragraphs
        if len(ck['paragraphs']) > len(ce['paragraphs']):
            for i in range(len(ce['paragraphs']), len(ck['paragraphs'])):
                out.append(f'  KO EXTRA para{i}: {ck["paragraphs"][i][:300]}')

    path = os.path.join(REVIEW, 'work_audit_b', f'dump_{key}_{ch_from}-{ch_to}.txt')
    open(path, 'w').write('\n'.join(out))
    print('wrote', path, len('\n'.join(out)), 'chars')

if __name__ == '__main__':
    main()
