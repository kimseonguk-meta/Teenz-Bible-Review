#!/usr/bin/env python3
"""Leviticus MSG audit fixes — ch1-27.
Applies badge corrections, content restorations, slang cleanup, and records
declared splits / pending confirmations. Does NOT apply the ch16 KO merge
(needs explicit approval).
"""
import json, copy

REVIEW = '/home/hatch/workspace/teenz-bible-review'
en = json.load(open(f'{REVIEW}/fixes/en_Leviticus.json'))
ko = json.load(open(f'{REVIEW}/fixes/ko_Leviticus.json'))
E = {c['chapter']: c for c in en}
K = {c['chapter']: c for c in ko}

log = []

def set_badges(ch, badges, langs=('EN', 'KO')):
    for lang in langs:
        c = E[ch] if lang == 'EN' else K[ch]
        assert len(c['paragraphs']) == len(badges), f'ch{ch} {lang}: para/badge count {len(c["paragraphs"])} vs {len(badges)}'
        old = c['verseRanges']
        c['verseRanges'] = list(badges)
        changed = [(i, a, b) for i, (a, b) in enumerate(zip(old, badges)) if a != b]
        if changed:
            log.append(f'ch{ch} {lang} badges: ' + '; '.join(f'para{i} {a}->{b}' for i, a, b in changed))

def rep(ch, lang, idx, old, new):
    c = E[ch] if lang == 'EN' else K[ch]
    p = c['paragraphs'][idx]
    assert old in p, f'ch{ch} {lang} para{idx}: needle not found: {old[:60]}'
    assert p.count(old) == 1, f'ch{ch} {lang} para{idx}: needle not unique'
    c['paragraphs'][idx] = p.replace(old, new)
    log.append(f'ch{ch} {lang} para{idx} edit: [{old[:50]}...] -> [{new[:50]}...]')

def title(ch, lang, new):
    c = E[ch] if lang == 'EN' else K[ch]
    log.append(f'ch{ch} {lang} title: [{c["title"]}] -> [{new}]')
    c['title'] = new

def declare(ch, kind, desc, langs=('EN', 'KO')):
    for lang in langs:
        c = E[ch] if lang == 'EN' else K[ch]
        c.setdefault('splits', []).append(desc) if kind == 'split' else c.setdefault('merges', []).append(desc)
    log.append(f'ch{ch} declared {kind}: {desc}')

def confirm(ch, desc):
    for c in (E[ch], K[ch]):
        c.setdefault('confirmations_needed', []).append(desc)
    log.append(f'ch{ch} CONFIRM NEEDED: {desc}')

# ---------------- ch3 ----------------
set_badges(3, ['1-5', '6-11', '12-16', '16-17'])

# ---------------- ch4 ----------------
set_badges(4, ['1-2', '3-12', '13-21', '22-25', '26', '27-30', '31', '32-34', '35'])
declare(4, 'split', 'MSG 1-12 -> Teen (1-2, 3-12)')
declare(4, 'split', 'MSG 22-26 -> Teen (22-25, 26)')
declare(4, 'split', 'MSG 27-31 -> Teen (27-30, 31)')
declare(4, 'split', 'MSG 32-35 -> Teen (32-34, 35)')

# ---------------- ch5 (slang) ----------------
rep(5, 'EN', 1, 'Wild, right?', 'Intense, right?')
rep(5, 'EN', 7, 'Lowkey a pretty good deal.', "Honestly, that's a pretty good deal.")
rep(5, 'EN', 13, 'No cap.', 'Seriously.')
rep(5, 'KO', 1, '대박이지?', '황당하지?')
rep(5, 'KO', 7, '완전 진짜 이득 아니냐?', '꽤 좋은 거래 아니야?')

# ---------------- ch6 ----------------
set_badges(6, ['1-6', '7', '8-13', '14-18', '19-23', '24-30'])

# ---------------- ch7 ----------------
set_badges(7, ['1-6', '7-10', '11-15', '16-21', '22-27', '28-34', '35-36', '37-38'])

# ---------------- ch8 ----------------
set_badges(8, ['1-4', '5', '6-9', '10-12', '13', '14-17', '18-21', '22-29', '30', '31-35', '36'])
rep(8, 'EN', 7, 'he takes one loaf, one cake made with oil, and one wafer,',
    'he takes one loaf made with oil and one wafer,')
rep(8, 'KO', 7, '빵 한 개, 기름 섞은 빵 한 개, 과자 한 개를 꺼내서',
    '기름 섞은 무교병 한 개와 과자 한 개를 꺼내서')

# ---------------- ch9 ----------------
set_badges(9, ['1-2', '3-4', '5-6', '7', '8-11', '12-14', '15-21', '22-24'])

# ---------------- ch10 ----------------
rep(10, 'EN', 4, 'So they came and carried them out, still in their clothes, outside the camp, just like Moses said.',
    'So they came and carried them out of the camp, just like Moses said.')
rep(10, 'KO', 4, '걔네가 와서 모세가 시킨 대로 옷 입은 채로 진영 밖으로 메고 나갔지.',
    '걔네가 와서 모세가 시킨 대로 진영 밖으로 메고 나갔지.')
declare(10, 'split', 'MSG 3 -> Teen (3, 3, 3)')
declare(10, 'split', 'MSG 6-7 -> Teen (6-7, 7)')

# ---------------- ch11 ----------------
set_badges(11, ['1-2', '3-8', '9-12', '13-19', '20-23', '24-25', '26-28', '27-28', '29-38', '39-40', '41-43', '44-45', '46-47'], langs=('KO',))
set_badges(11, ['1-2', '3-8', '9-12', '13-19', '20-23', '24-25', '26', '27-28', '29-38', '39-40', '41-43', '44-45', '46-47'], langs=('EN',))
rep(11, 'KO', 3, '독수리, 솔개, 물수리, 매 종류,', '독수리, 솔개, 물수리, 연, 매 종류,')

# ---------------- ch12 ----------------
declare(12, 'split', 'MSG 6-7 -> Teen (6-7, 7)')

# ---------------- ch13 ----------------
set_badges(13, ['1-2', '3', '4-8', '9-17', '18-23', '24-28', '29-37', '38-39', '40-44', '45-46', '47-58', '59'])
declare(13, 'split', 'MSG 1-3 -> Teen (1-2, 3)')

# ---------------- ch14 ----------------
set_badges(14, ['1-9', '10-18', '19-20', '21-22', '23-29', '30-31', '32', '33-42', '43-47', '48-53', '54-57'])

# ---------------- ch15 ----------------
set_badges(15, ['1-3', '4-7', '8-11', '12', '13-15', '16-18', '19-23', '24', '25-27', '28-30', '31', '32-33'])
title(15, 'EN', "God's Rules on Bodily Fluids")

# ---------------- ch16 ----------------
c = E[16]
assert c['verseRanges'][8] == '26'
c['verseRanges'][8] = '26-28'
log.append('ch16 EN badges: para8 26->26-28')
rep(16, 'EN', 1, "Then, he'll get two male goats from the Israelites for a sin offering and a burnt offering.",
    "Then, he'll get two male goats from the Israelites for a sin offering, and a ram for a burnt offering.")
rep(16, 'KO', 4, '속죄판 동쪽에 뿌리고', '속죄판 앞면에 뿌리고')
confirm(16, 'KO paras 0-1 (badges 1, 2) merge into single 1-2 para to match EN 17-para structure (MSG paragraph merge needs approval)')

# ---------------- ch17 ----------------
set_badges(17, ['1-7', '8-9', '10-12', '13-14', '15-16'])
title(17, 'EN', 'The #1 Rule About Sacrifices')

# ---------------- ch18 ----------------
c = E[18]
assert c['verseRanges'][0] == '1-4'
c['verseRanges'][0] = '1-5'
log.append('ch18 EN badges: para0 1-4->1-5')
declare(18, 'split', 'MSG 23 -> Teen (23, 23)')

# ---------------- ch19 ----------------
# EN parity split of v18 to match KO's two paras
c = E[19]
exp17 = '\u0027Don\u2019t try to get revenge or hold a grudge. Love your neighbor as yourself. I am God.\u0027'
assert c['paragraphs'][17] == exp17, repr(c['paragraphs'][17])
c['paragraphs'][17] = '\u0027Don\u2019t try to get revenge or hold a grudge.'
c['paragraphs'].insert(18, 'Love your neighbor as yourself. I am God.\u0027')
c['verseRanges'].insert(18, '18')
c.setdefault('splits', []).append('EN parity split: v18 -> (18, 18) to match KO paragraphing (Teen-side split, not MSG)')
log.append('ch19 EN: split para17 [18] into two paras (18, 18) for EN/KO parity')
rep(19, 'EN', 5,
    '\u0027When you\u2019re harvesting your crops, don\u2019t be greedy and take everything. Leave some for the poor and for foreigners. I\u2019m your God.\u0027',
    '\u0027When you harvest your crops, don\u2019t harvest right up to the edges of your field, and don\u2019t pick up the fallen grain. Don\u2019t strip your vineyard bare or go back for the fallen grapes. Leave them for the poor and the foreigner. I am God, your God.\u0027')
# note: after the insert above, para22 (20-22) shifted to index 23
rep(19, 'EN', 23,
    '\u0027If a man sleeps with a slave girl who\u2019s engaged to someone else but hasn\u2019t been freed yet, there needs to be an investigation. But they won\u2019t be put to death because she wasn\u2019t free. The man has to bring a special offering to God, and the priest will perform a ritual to atone for his sin. Then he\u2019ll be forgiven.\u0027',
    '\u0027If a man sleeps with a slave girl who\u2019s engaged to someone else but hasn\u2019t been freed or ransomed yet, there has to be an investigation. But they won\u2019t be put to death because she wasn\u2019t free. The man has to bring a Compensation-Offering to God at the entrance of the Tent of Meeting\u2014a ram. The priest will perform the atonement ritual for him before God with the ram for the sin he committed. Then he\u2019ll be forgiven for the sin he committed.\u0027')

# ---------------- ch20 ----------------
set_badges(20, ['1-2', '3-5', '6', '7-8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22-23', '24-25', '26', '27'])
declare(20, 'split', 'MSG 1-5 -> Teen (1-2, 3-5)')
declare(20, 'split', 'MSG 24-26 -> Teen (24-25, 26)')
title(20, 'EN', "God's Rules: These Are Serious")
rep(20, 'EN', 0, 'The whole community has to take you out by stoning. No cap.',
    'The whole community has to take you out by stoning. This is serious.')
rep(20, 'EN', 1, 'I\u2019ll be looking at that person sideways and will cut them off from everyone.',
    'I\u2019ll straight-up reject that person and cut them off from everyone.')
rep(20, 'EN', 2, 'I\u2019m also gonna give the side-eye to anyone messing with psychics or mediums,',
    'I\u2019m also going to reject anyone messing with psychics or mediums,')
rep(20, 'KO', 17, '걔네가 온갖 더러운 짓을 해서 내가 완전 극혐했거든.',
    '걔네가 온갖 더러운 짓을 해서 내가 진짜 싫어했거든.')

# ---------------- ch21 ----------------
set_badges(21, ['1-4', '5-6', '7-8', '9', '10-12', '13-15', '16-23', '24'])
rep(21, 'EN', 2, "he can't marry a woman who's been a prostitute or is divorced.",
    "he can't marry a woman who's been a prostitute, a shrine prostitute, or is divorced.")
rep(21, 'KO', 2, '창녀였던 여자나 이혼한 여자랑 결혼하면 안 된대.',
    '창녀였던 여자나 신전 창기, 이혼한 여자랑 결혼하면 안 된대.')

# ---------------- ch22 ----------------
set_badges(22, ['1-2', '3', '4-8', '9', '10-13', '14', '15-16', '17-25', '26-30', '31', '32-33'])

# ---------------- ch23 ----------------
c = E[23]; assert c['verseRanges'][13] == '43-44'; c['verseRanges'][13] = '44'
c = K[23]; assert c['verseRanges'][13] == '43-44'; c['verseRanges'][13] = '44'
log.append('ch23 EN/KO badges: para13 43-44->44')
rep(23, 'KO', 1, '그냥 완전 쉬는 날, ㅇㅋ?', '그냥 완전히 쉬는 날이야.')
rep(23, 'KO', 4, '역시나 일은 노노."', '역시나 일은 하면 안 돼."')
rep(23, 'KO', 6, '향기가 대박임.', '향기가 진짜 좋음.')
rep(23, 'KO', 6, '어린 수소 한 마리', '수소 한 마리')

# ---------------- ch24 ----------------
rep(24, 'EN', 1, 'Then, take fine flour and bake twelve loaves of bread. Arrange them in two rows,',
    'Then, take fine flour and bake twelve loaves of bread, using about four quarts of flour for each loaf. Arrange them in two rows,')
rep(24, 'KO', 1, '그리고 고운 밀가루로 빵 열두 개를 만들어라.',
    '그리고 고운 밀가루로 빵 열두 개를 만들어라. 빵 하나당 고운 가루 약 4리터씩 넣어.')
set_badges(24, ['1-4', '5-9', '10-12', '13-16', '17-22', '23'])

# ---------------- ch25 ----------------
set_badges(25, ['1-7', '8-12', '13', '14-17', '18-22', '23-24', '25-28', '29-31', '32-34', '35-38', '39-43', '44-46', '47-53', '54-55'])

# ---------------- ch26 ----------------
set_badges(26, ['1', '2', '3-5', '6-10', '11-13', '14-17', '18-20', '21-22', '23-26', '27-35', '36-39', '40-42', '43-45', '46'])

# ---------------- ch27 ----------------
set_badges(27, ['1-8', '9-13', '14-15', '16-21', '22-25', '26-27', '28', '29', '30-33', '34'])
rep(27, 'EN', 5, "Also, lowkey, you can't dedicate the firstborn of an animal.",
    "Also, you can't dedicate the firstborn of an animal.")

json.dump(en, open(f'{REVIEW}/fixes/en_Leviticus.json', 'w'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Leviticus.json', 'w'), ensure_ascii=False, indent=1)

print('\n'.join(log))
print(f'\nTotal operations: {len(log)}')
