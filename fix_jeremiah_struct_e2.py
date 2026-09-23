#!/usr/bin/env python3
"""Worker E2: Jeremiah structural badge fixes (validator failures).

Applies badge corrections + paragraph split/merge reconciliations so
EN/KO badges match and reflect the MSG units the text actually covers.
Records every change in the chapter's changes[] list.
"""
import json
import sys

sys.path.insert(0, '/home/hatch/workspace/teenz-bible-review')
from validate_translation import expand  # noqa: E402

REVIEW = '/home/hatch/workspace/teenz-bible-review'
en = json.load(open(f'{REVIEW}/fixes/en_Jeremiah.json', encoding='utf-8'))
ko = json.load(open(f'{REVIEW}/fixes/ko_Jeremiah.json', encoding='utf-8'))
en_by = {c['chapter']: c for c in en}
ko_by = {c['chapter']: c for c in ko}


def set_badge(ch, lang, idx, new):
    d = en_by[ch] if lang == 'en' else ko_by[ch]
    old = d['verseRanges'][idx]
    d['verseRanges'][idx] = new
    d['msg_ranges'][idx] = new
    d['changes'].append(f"배지 수정: {old}→{new} (p{idx}, MSG 문단 기준)")


def set_ko_badges_to_en(ch):
    e, k = en_by[ch], ko_by[ch]
    assert len(e['paragraphs']) == len(k['paragraphs']), f'ch{ch} count'
    k['verseRanges'] = list(e['verseRanges'])
    k['msg_ranges'] = list(e['msg_ranges'])
    k['changes'].append('KO 배지를 EN(MSG 문단 기준)과 일치시킴')


def rebuild_splits(ch):
    for d in (en_by[ch], ko_by[ch]):
        vrs = d['verseRanges']
        n = len(vrs)
        sets = [expand(b) for b in vrs]
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(n):
            for j in range(i + 1, n):
                if sets[i] & sets[j]:
                    ri, rj = find(i), find(j)
                    if ri != rj:
                        parent[ri] = rj
        comps = {}
        for i in range(n):
            comps.setdefault(find(i), []).append(i)
        splits = []
        for comp in comps.values():
            if len(comp) < 2:
                continue
            u = set()
            for i in comp:
                u |= sets[i]
            lo, hi = min(u), max(u)
            splits.append({'msg_range': f'{lo}-{hi}' if lo != hi else str(lo),
                           'paras': sorted(comp)})
        d['splits'] = splits


# ---- ch1: badges 1-3/4-5 -> 1-4/5 (text covers MSG 1-4 / 5) ----
for lang in ('en', 'ko'):
    set_badge(1, lang, 0, '1-4')
    set_badge(1, lang, 1, '5')

# ---- ch2: KO badges -> EN (MSG unit ranges) ----
set_ko_badges_to_en(2)

# ---- ch9: split EN p2 [7-9] into intro [7] + quote [7-9] (match KO) ----
e9 = en_by[9]
old_p2 = e9['paragraphs'][2]
assert old_p2.startswith("So, the God of Heaven's Armies is like, 'Alright, watch this."), old_p2[:60]
new_intro = "So, the God of Heaven's Armies says:"
new_quote = "'Alright, watch this." + old_p2.split("'Alright, watch this.", 1)[1]
e9['paragraphs'][2:3] = [new_intro, new_quote]
e9['verseRanges'][2:3] = ['7', '7-9']
e9['msg_ranges'][2:3] = ['7', '7-9']
e9['changes'].append("p2 분할: [7] 도입부 / [7-9] 인용부 (KO 구조와 일치, MSG 7-9 split)")

# ---- ch22 ----
set_badge(22, 'en', 9, '20-23')
set_badge(22, 'en', 10, '24-26')
set_badge(22, 'ko', 12, '28-30')

# ---- ch23: EN p9 intro of MSG 16-17 -> [16] ----
set_badge(23, 'en', 9, '16')

# ---- ch24: KO p5 -> [8-10] ----
set_badge(24, 'ko', 5, '8-10')

# ---- ch26: split KO p10 [17-18] into [17] + [18] (match EN) ----
k26 = ko_by[26]
old = k26['paragraphs'][10]
assert '만군의 여호와께서 이렇게 말씀하셨다.' in old
intro = '그 땅의 원로 몇 사람이 일어나서 모든 백성한테 말했음. "유다 왕 히스기야 시대에 모레셋 사람 미가가 유다 모든 백성한테 이렇게 예언했어. \'만군의 여호와께서 이렇게 말씀하셨다.\'"'
quote = '"\'시온은 밭처럼 갈아엎어질 거고, 예루살렘은 돌무더기가 되며, 성전이 서 있는 산은 숲의 언덕처럼 될 거다.\'"'
k26['paragraphs'][10:11] = [intro, quote]
k26['verseRanges'][10:11] = ['17', '18']
k26['msg_ranges'][10:11] = ['17', '18']
k26['changes'].append("p10 분할: [17] 도입부 / [18] 인용부 (EN 구조와 일치, MSG 17-18 split)")

# ---- ch31: EN badge fixes; KO -> EN ----
for idx, new in [(2, '2-6'), (18, '29'), (21, '31-32'), (22, '33-34'),
                 (23, '35'), (24, '36'), (25, '37'), (26, '37'), (27, '38-39')]:
    set_badge(31, 'en', idx, new)
set_ko_badges_to_en(31)

# ---- ch32: EN badge fixes; KO -> EN ----
set_badge(32, 'en', 9, '26-30')
set_badge(32, 'en', 10, '31-35')
set_ko_badges_to_en(32)

# ---- ch33: KO -> EN ----
set_ko_badges_to_en(33)

# ---- ch34: EN badge fixes; KO -> EN ----
for idx, new in [(4, '8-10'), (5, '11'), (6, '12-14'), (7, '15-16'), (8, '17-20')]:
    set_badge(34, 'en', idx, new)
set_ko_badges_to_en(34)

# ---- ch35: EN badge fixes; KO -> EN ----
for idx, new in [(5, '8-10'), (6, '11'), (7, '12-15')]:
    set_badge(35, 'en', idx, new)
set_ko_badges_to_en(35)

# ---- ch36: EN p8 -> [10]; KO -> EN ----
set_badge(36, 'en', 8, '10')
set_ko_badges_to_en(36)

# ---- ch37: KO badges ----
set_badge(37, 'ko', 6, '14-16')
set_badge(37, 'ko', 7, '17')

# ---- ch38: EN p1 -> [2]; KO -> EN ----
set_badge(38, 'en', 1, '2')
set_ko_badges_to_en(38)

# ---- ch39: KO -> EN ----
set_ko_badges_to_en(39)

# ---- ch41: KO restructure p0/p1 -> [1-2]/[3] (match EN) ----
k41 = ko_by[41]
new_p0 = ("그해 7월에, 엘리사마의 손자고 느다냐의 아들인 이스마엘이라는 사람이 나타났대. "
          "이 사람이 왕족 출신에 왕의 최측근 중 한 명이었던 거임. "
          "그가 부하 열 명을 데리고 미스바에 있는 아히감의 아들 그달랴를 찾아왔어. "
          "근데 다 같이 밥 먹고 있는데, 갑자기 이스마엘이랑 그 부하들이 일어나서 그달랴를 쳐서 죽여버린 거야. "
          "바빌론 왕이 이 땅의 총독으로 임명한 사람을 말이야.")
new_p1 = ("그리고 이스마엘은 미스바에서 그달랴와 함께 있던 모든 유다 사람들과 "
          "거기 주둔하고 있던 바빌론 군인들까지 다 죽여버렸대.")
assert k41['paragraphs'][1].startswith('근데 다 같이 밥 먹고 있는데')
k41['paragraphs'][0:2] = [new_p0, new_p1]
k41['verseRanges'][0:2] = ['1-2', '3']
k41['msg_ranges'][0:2] = ['1-2', '3']
k41['changes'].append("p0/p1 재구조: [1-2]/[3] (EN 구조와 일치, MSG 1-3 split)")

# ---- ch48: EN p15 -> [40] ----
set_badge(48, 'en', 15, '40')

# ---- rebuild splits for all touched chapters ----
for ch in [1, 2, 9, 22, 23, 24, 26, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 48]:
    rebuild_splits(ch)

json.dump(en, open(f'{REVIEW}/fixes/en_Jeremiah.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Jeremiah.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('structural fixes applied')
