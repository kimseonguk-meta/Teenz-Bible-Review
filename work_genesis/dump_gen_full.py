#!/usr/bin/env python3
"""Regenerate /tmp/gen_full/chXX.txt dumps: full MSG units, full Teen EN, KO first 200 chars."""
import json, os, sys
sys.path.insert(0, '/home/hatch/workspace/teenz-bible-review/gdocs_build')
os.chdir('/home/hatch/workspace/teenz-bible-review')
import build_gdocs as bg

units = bg.parse_msg_txt('msg_Genesis.txt')
by_ch = {}
for u in units:
    by_ch.setdefault(u['chapter'], []).append(u)
en = json.load(open('fixes/en_Genesis.json'))
ko = json.load(open('fixes/ko_Genesis.json'))
os.makedirs('/tmp/gen_full', exist_ok=True)

def vr_of(verses):
    vs = sorted(verses)
    return f"{vs[0]}-{vs[-1]}" if len(vs) > 1 else str(vs[0])

start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
end = int(sys.argv[2]) if len(sys.argv) > 2 else 50
for ch in range(start, end + 1):
    out = []
    us = by_ch.get(ch, [])
    out.append(f"===== MSG ch{ch}: {len(us)} units =====\n")
    for i, u in enumerate(us):
        t = ' '.join(u['blocks'])
        out.append(f"--- M{i} [{vr_of(u['verses'])}] ---\n{t}\n")
    ech = en[ch - 1]; evrs = ech.get('verseRanges', [])
    out.append(f"\n===== Teen EN ch{ch}: {len(ech['paragraphs'])} paragraphs =====\n")
    for i, p in enumerate(ech['paragraphs']):
        vr = evrs[i] if i < len(evrs) else '?'
        out.append(f"--- T{i} [{vr}] ---\n{p}\n")
    kch = ko[ch - 1]; kvrs = kch.get('verseRanges', [])
    out.append(f"\n===== Teen KO ch{ch}: {len(kch['paragraphs'])} paragraphs (first 200 chars) =====\n")
    for i, p in enumerate(kch['paragraphs']):
        vr = kvrs[i] if i < len(kvrs) else '?'
        out.append(f"--- K{i} [{vr}] ---\n{p[:200]}\n")
    open(f'/tmp/gen_full/ch{ch:02d}.txt', 'w', encoding='utf-8').write('\n'.join(out))
    print(f"ch{ch}: MSG {len(us)}u, EN {len(ech['paragraphs'])}p, KO {len(kch['paragraphs'])}p")
