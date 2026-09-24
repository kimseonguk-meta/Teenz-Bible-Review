import json, sys
sys.path.insert(0, '/home/hatch/workspace/teenz-bible-review/gdocs_build')
from build_gdocs import parse_msg_txt
units = parse_msg_txt('/home/hatch/workspace/teenz-bible-review/msg_Ezekiel.txt')
en = json.load(open('/home/hatch/workspace/teenz-bible-review/fixes/en_Ezekiel.json'))
ch = int(sys.argv[1])
print(f"=== CHAPTER {ch} ===")
mus=[u for u in units if u['chapter']==ch]
for u in mus:
    vs=sorted(u['verses']); vr=f"{vs[0]}-{vs[-1]}" if len(vs)>1 else f"{vs[0]}"
    blks=' | '.join(b[:65] for b in u['blocks'])
    print(f"MSG [{vr}]: {blks}")
print()
d=next(d for d in en if d['chapter']==ch)
print(f"Teen paras: {len(d['paragraphs'])}, msg_ranges={d['msg_ranges']}")
for i,p in enumerate(d['paragraphs']):
    t=p if isinstance(p,str) else p.get('text','')
    print(f"EN[{i}] ({d['msg_ranges'][i]}): {t[:100]}")
