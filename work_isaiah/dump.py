import json, sys
en=json.load(open('work_isaiah/en_isaiah.json'))
ko=json.load(open('work_isaiah/ko_isaiah.json'))
def show(n):
    e=next(c for c in en if c['num']==n); k=next(c for c in ko if c['num']==n)
    print(f'===== CH {n} | EN: {e["title"]} | KO: {k["title"]} =====')
    print(f'EN badges: {e["verseRanges"]}  ({len(e["paragraphs"])} paras)')
    print(f'KO badges: {k["verseRanges"]}  ({len(k["paragraphs"])} paras)')
    for i,(p,b) in enumerate(zip(e['paragraphs'],e['verseRanges'])):
        print(f'-- EN[{i}] ({b}): {p}')
    for i,(p,b) in enumerate(zip(k['paragraphs'],k['verseRanges'])):
        print(f'-- KO[{i}] ({b}): {p}')
    print()
for n in [int(x) for x in sys.argv[1:]]:
    show(n)
