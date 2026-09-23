#!/usr/bin/env python3
"""Align EN paragraphs to MSG sections per chapter using content similarity.
Usage: python3 align_book.py Joshua -> align_Joshua.json
Output per chapter: [{en: idx, msg: [section_idx...], sim: float, badge: str}]
"""
import json, sys, re
from difflib import SequenceMatcher

STOP = set('''the a an and or of to in on for with is are was were be been being it its they them their this that these those you your he she his her we our him her as at by from but not no so if then than when where which who whom what how all any each every more most other some such only own same too very can will just don should now out up down over under again once here there their their'''.split())

def words(t):
    t = re.sub(r'[^a-zA-Z ]', ' ', t.lower())
    return [w for w in t.split() if len(w) > 4 and w not in STOP]

def sim(a, b):
    wa, wb = words(a), words(b)
    if not wa or not wb: return 0.0
    # containment-leaning similarity: how much of MSG's key content appears in EN
    sa, sb = set(wa), set(wb)
    inter = len(sa & sb)
    # jaccard-ish + recall of msg words
    return 0.5 * (inter / len(sa | sb)) + 0.5 * (inter / len(sa))

def align_chapter(msg_secs, en_paras):
    """Greedy sequential alignment. Returns list of (en_idx, [msg_idx...], sim)."""
    n, m = len(en_paras), len(msg_secs)
    res = []
    mi = 0
    for ei in range(n):
        ep = en_paras[ei]
        best = None
        # try matching 1 or 2 consecutive MSG sections starting at mi (merge case)
        for k in (1, 2, 3):
            if mi + k > m: break
            combined = ' '.join(s['text'] for s in msg_secs[mi:mi+k])
            s = sim(combined, ep)
            # slight preference for fewer sections
            s_adj = s - 0.03 * (k - 1)
            if best is None or s_adj > best[0]:
                best = (s_adj, k, s)
        s_adj, k, s = best
        # also consider: this EN para might be a SPLIT (shares MSG section with next EN para).
        # We handle splits in a second pass: if next EN para is more similar to the same
        # MSG section than to the following one, they share it.
        res.append({'en': ei, 'msg': list(range(mi, mi + k)), 'sim': round(s, 3), 'k': k})
        mi += k
        if mi >= m:
            # remaining EN paras: attach to last MSG section (likely splits)
            for ej in range(ei + 1, n):
                res.append({'en': ej, 'msg': [m - 1], 'sim': 0.0, 'k': 1, 'overflow': True})
            break
    return res

def main():
    book = sys.argv[1]
    slug = book.replace(' ', '')
    en = json.load(open('/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json'))[book]
    msg = json.load(open(f'msg_{slug}_parsed.json'))['chapters']
    out = {}
    for ch in en:
        num = ch['num']
        msecs = msg[str(num)]
        al = align_chapter(msecs, ch['paragraphs'])
        out[str(num)] = {
            'title': ch.get('title', ''),
            'en_badges': ch['verseRanges'],
            'msg_ranges': [s['range'] for s in msecs],
            'align': al,
        }
    json.dump(out, open(f'align_{slug}.json', 'w'), ensure_ascii=False, indent=1)
    # summary
    low = []
    for num, a in out.items():
        for e in a['align']:
            if e['sim'] < 0.25:
                low.append((num, e['en'], e['sim'], e['msg']))
    print(f'{book}: {len(out)} chapters aligned')
    print(f'low-sim pairs (<0.25): {len(low)}')
    for num, ei, s, mi in low[:40]:
        print(f'  ch{num} en{ei} sim={s} msg={mi}')

if __name__ == '__main__':
    main()
