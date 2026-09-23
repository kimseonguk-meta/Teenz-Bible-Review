#!/usr/bin/env python3
import json
books = ['Joshua','Judges','Ruth','1 Samuel','2 Samuel','1 Kings','2 Kings']
en_all = json.load(open('/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json'))
for book in books:
    slug = book.replace(' ','')
    ko = json.load(open(f'ko_{slug}_raw.json'))
    en = {c['num']: c for c in en_all[book]}
    bad = []
    for n in sorted(en.keys()):
        e = len(en[n]['paragraphs'])
        k = len(ko[str(n)]['paragraphs'])
        if e != k:
            bad.append((n, 'EN %d vs KO %d' % (e, k)))
        nulls = [i for i, v in enumerate(ko[str(n)]['verseRanges']) if v is None]
        if nulls:
            bad.append((n, 'KO null badges at %s' % nulls))
    print(book, 'chapters:', len(en), '| MISMATCHES:', bad if bad else 'none')
