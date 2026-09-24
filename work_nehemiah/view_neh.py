#!/usr/bin/env python3
"""Side-by-side MSG vs Teen EN vs Teen KO viewer for Nehemiah audit."""
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'gdocs_build'))
from build_gdocs import parse_msg_txt
from collections import defaultdict

REVIEW = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MSG = parse_msg_txt(os.path.join(REVIEW, 'msg_Nehemiah.txt'))
by_ch = defaultdict(list)
for u in MSG:
    by_ch[u['chapter']].append(u)
en = json.load(open(os.path.join(REVIEW, 'fixes', 'en_Nehemiah.json')))
ko = json.load(open(os.path.join(REVIEW, 'fixes', 'ko_Nehemiah.json')))
en_by_ch = {e['chapter']: e for e in en}
ko_by_ch = {k['chapter']: k for k in ko}

def fmt_vset(u):
    vs = sorted(u['verses'] or [])
    return f"{min(vs)}-{max(vs)}" if vs else "?"

def show(ch, en_only=False):
    print(f"########## Nehemiah {ch} ##########")
    ce, ck = en_by_ch[ch], ko_by_ch[ch]
    print("EN verseRanges:", ce['verseRanges'])
    print("KO verseRanges:", ck['verseRanges'])
    print("msg_ranges EN:", ce.get('msg_ranges'))
    print()
    print("=== MSG UNITS ===")
    for ui, u in enumerate(by_ch[ch]):
        blocks = '\n'.join(u['blocks'])
        print(f"[MSG {ui}] vset={fmt_vset(u)} verses={sorted(u['verses'] or [])}")
        print(blocks)
        print('---')
    print()
    print("=== TEEN EN ===")
    for i, p in enumerate(ce['paragraphs']):
        vr = ce['verseRanges'][i] if i < len(ce['verseRanges']) else '?'
        print(f"[EN {i}] badge={vr}")
        print(p)
        if not en_only:
            print(f"[KO {i}] badge={ck['verseRanges'][i] if i < len(ck['verseRanges']) else '?'}")
            print(ck['paragraphs'][i])
        print('---')

if __name__ == '__main__':
    ch = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    show(ch, en_only=('--en' in sys.argv))
