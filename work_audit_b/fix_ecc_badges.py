#!/usr/bin/env python3
"""Ecclesiastes fixes: badge corrections, ch9 structural repair, slang cleanup.
Applies to both EN and KO. Run from ~/workspace/teenz-bible-review.
"""
import json, os

REVIEW = os.path.expanduser('~/workspace/teenz-bible-review')
EN_P = os.path.join(REVIEW, 'fixes/en_Ecclesiastes.json')
KO_P = os.path.join(REVIEW, 'fixes/ko_Ecclesiastes.json')

en = json.load(open(EN_P))
ko = json.load(open(KO_P))
en_by = {c['chapter']: c for c in en}
ko_by = {c['chapter']: c for c in ko}

def set_badges(ch, badges):
    e = en_by[ch]; k = ko_by[ch]
    assert len(badges) == len(e['paragraphs']) == len(k['paragraphs']), f'ch{ch} len mismatch'
    e['verseRanges'] = list(badges)
    k['verseRanges'] = list(badges)
    print(f'ch{ch}: badges -> {badges}')

# --- Badge corrections (content-verified against MSG txt) ---
set_badges(2,  ['1','2-3','4-8','9-10','11','12-14','15-16','17','18-19','20-23','24-26'])
set_badges(5,  ['1','2','3','4-5','6','7','8-9','10','11','12','13-17','18-20'])
set_badges(6,  ['1','2','3-5','6','7','8-9','10','11-12'])
set_badges(10, ['1','2','3','4','5-7','8','9','10','11','12-13','14','15','16-17','18','19','20'])
set_badges(11, ['1','2','3-4','5','6','7-8','9','10'])
set_badges(12, ['1-2','3-5','6-7','8','9-10','11','12','13','14'])

# --- ch9 structural repair ---
# Problems: EN p4 truncated v11 fragment; EN p5 duplicate full v11; KO p6 v13-intro
# duplicated by KO p7 full v13-15; badges [10],[11],[12] don't match content.
e9 = en_by[9]; k9 = ko_by[9]
assert len(e9['paragraphs']) == 11 and len(k9['paragraphs']) == 11

# New EN p4 [11]: restore full v11 from truncated fragment + duplicate
en_p4_full = ("I was walking around the other day and had this realization about how things "
              "are on Earth\u2014 the fastest runner doesn't always win, the strongest fighter "
              "doesn't always come out on top, the smartest person isn't always happy, the "
              "cleverest person isn't always rich, and the most talented person doesn't always "
              "get the praise. Sooner or later, we all get hit with bad luck.")
# New EN p5 [12]: old p6 (v12). New EN p6 [13-15]: old p7 (v13-15).
new_en_paras = (e9['paragraphs'][:4] + [en_p4_full, e9['paragraphs'][6], e9['paragraphs'][7]]
                + e9['paragraphs'][8:])
# New KO: p4 keep (v11), p5 keep (v12), p6 = old p7 (full v13-15, drops redundant intro p6)
new_ko_paras = (k9['paragraphs'][:4] + [k9['paragraphs'][4], k9['paragraphs'][5], k9['paragraphs'][7]]
                + k9['paragraphs'][8:])
assert len(new_en_paras) == 10 and len(new_ko_paras) == 10
e9['paragraphs'] = new_en_paras
k9['paragraphs'] = new_ko_paras
new_badges_9 = ['1-2','3','4-6','7-10','11','12','13-15','16','17','18']
e9['verseRanges'] = list(new_badges_9)
k9['verseRanges'] = list(new_badges_9)
print('ch9: structural repair -> 10 paras, badges', new_badges_9)

json.dump(en, open(EN_P, 'w'), ensure_ascii=False, indent=2)
json.dump(ko, open(KO_P, 'w'), ensure_ascii=False, indent=2)
print('saved.')
