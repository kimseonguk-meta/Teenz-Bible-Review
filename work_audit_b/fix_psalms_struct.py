#!/usr/bin/env python3
"""Psalms fixes: structural (ch6,20,47,116,143,104,105) + slang cleanup.
Run from ~/workspace/teenz-bible-review."""
import json, os, re

REVIEW = os.path.expanduser('~/workspace/teenz-bible-review')
EN_P = os.path.join(REVIEW, 'fixes/en_Psalms.json')
KO_P = os.path.join(REVIEW, 'fixes/ko_Psalms.json')

en = json.load(open(EN_P))
ko = json.load(open(KO_P))
en_by = {c['chapter']: c for c in en}
ko_by = {c['chapter']: c for c in ko}

# ============ STRUCTURAL FIXES ============

# ch6: split KO p4 (v6+v7 merged) -> [6],[7]
k6 = ko_by[6]
p4 = k6['paragraphs'][4]
split_at = '매트리스는 눈물로 다 젖어서 축축한 거 있죠. '
assert split_at in p4
a, b = p4.split(split_at)
new_p4 = a + split_at.strip()
new_p5 = b
k6['paragraphs'] = k6['paragraphs'][:4] + [new_p4, new_p5] + k6['paragraphs'][5:]
k6['verseRanges'] = ['1','2','3','4-5','6','7','8-9','10']
print('ch6: split KO p4 -> 8 paras')

# ch20: split KO p0 (v1+v2-4 merged) -> [1],[2-4]
k20 = ko_by[20]
p0 = k20['paragraphs'][0]
split_at = '야곱의 하나님의 이름이 너를 위험에서 건져주시길. '
assert split_at in p0
a, b = p0.split(split_at)
new_p0 = a + split_at.strip()
new_p1 = b
k20['paragraphs'] = [new_p0, new_p1] + k20['paragraphs'][1:]
k20['verseRanges'] = ['1','2-4','5','6','7-8','9']
print('ch20: split KO p0 -> 6 paras')

# ch47: move v4 from KO p2 to p1; split KO p3 (v7-8+v9 merged)
k47 = ko_by[47]
# p1 gets v4 sentences
v4_sents = '하나님이 우리를 최고로 뽑아주셨어. 당신이 가장 사랑하는 야곱의 자랑거리로 삼아주신 거임. '
p2 = k47['paragraphs'][2]
assert p2.startswith(v4_sents)
k47['paragraphs'][1] = k47['paragraphs'][1] + ' ' + v4_sents.strip()
k47['paragraphs'][2] = p2[len(v4_sents):]
# split p3
p3 = k47['paragraphs'][3]
split_at = '거룩한 보좌에 앉아계신 주권자이심. '
assert split_at in p3
a, b = p3.split(split_at)
new_p3 = a + split_at.strip()
new_p4 = b
k47['paragraphs'] = k47['paragraphs'][:3] + [new_p3, new_p4]
k47['verseRanges'] = ['1','2-4','5-6','7-8','9']
print('ch47: fixed merges -> 5 paras')

# ch116: split KO p0 (v1-4+v5-6) and p3 (v12-14+v15-19)
k116 = ko_by[116]
p0 = k116['paragraphs'][0]
split_at = "'라고 소리쳤지. "
assert split_at in p0
a, b = p0.split(split_at)
new_p0 = a + "'라고 소리쳤지."
new_p1 = b
p3 = k116['paragraphs'][3]
split_at2 = '그리고 그분의 백성들과 함께 할 거야. '
assert split_at2 in p3
c, d = p3.split(split_at2)
new_p4 = c + '그리고 그분의 백성들과 함께 할 거야.'
new_p5 = d
k116['paragraphs'] = [new_p0, new_p1, k116['paragraphs'][1], k116['paragraphs'][2], new_p4, new_p5]
k116['verseRanges'] = ['1-4','5-6','7-8','9-11','12-14','15-19']
print('ch116: split KO p0,p3 -> 6 paras')

# ch143: split KO p0 (v1+v2 merged)
k143 = ko_by[143]
p0 = k143['paragraphs'][0]
split_at = '저한테 옳은 대로 행해주세요. '
assert split_at in p0
a, b = p0.split(split_at)
new_p0 = a + '저한테 옳은 대로 행해주세요.'
new_p1 = b
k143['paragraphs'] = [new_p0, new_p1] + k143['paragraphs'][1:]
k143['verseRanges'] = ['1','2','3-6','7-10','11-12']
print('ch143: split KO p0 -> 5 paras')

# ch104, ch105: mark p0 as § header (shares badge with following content)
for ch in [104, 105]:
    e = en_by[ch]; k = ko_by[ch]
    if not e['paragraphs'][0].lstrip().startswith('§'):
        e['paragraphs'][0] = '§' + e['paragraphs'][0]
    if not k['paragraphs'][0].lstrip().startswith('§'):
        k['paragraphs'][0] = '§' + k['paragraphs'][0]
    print(f'ch{ch}: marked p0 as § header')

json.dump(en, open(EN_P, 'w'), ensure_ascii=False, indent=2)
json.dump(ko, open(KO_P, 'w'), ensure_ascii=False, indent=2)
print('structural fixes saved.')
