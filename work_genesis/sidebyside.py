import json, sys
sys.path.insert(0, 'gdocs_build')
import build_gdocs as bg
ch = int(sys.argv[1])
units = [u for u in bg.parse_msg_txt('msg_Genesis.txt') if u['chapter'] == ch]
teen = json.load(open('fixes/en_Genesis.json'))[ch-1]
vrs = teen.get('verseRanges', [])
ko = json.load(open('fixes/ko_Genesis.json'))[ch-1]
print(f"### MSG ch{ch} ({len(units)} units):")
for i,u in enumerate(units):
    vs = sorted(u['verses'])
    vr = f"{vs[0]}-{vs[-1]}" if len(vs)>1 else str(vs[0])
    t = ' '.join(u['blocks'])
    print(f"  M{i} [{vr}] {t[:300]}")
print(f"\n### Teen EN ch{ch}:")
for i,p in enumerate(teen['paragraphs']):
    vr = vrs[i] if i < len(vrs) else '?'
    print(f"  T{i} [{vr}]: {p[:300]}")
print(f"\n### Teen KO ch{ch} (first 60 chars):")
kvrs = ko.get('verseRanges', [])
for i,p in enumerate(ko['paragraphs']):
    vr = kvrs[i] if i < len(kvrs) else '?'
    print(f"  K{i} [{vr}]: {p[:80]}")
