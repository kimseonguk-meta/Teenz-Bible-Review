#!/usr/bin/env python3
"""Esther 기계적 완전성 검사(completeness_check) 잔여 이슈 수정 (작업자 D, 2026-09-23).
checker artifact(27/29 합산 버그, seething 문두 형용사, 직접화법 your)는 수정 대상 아님."""
import json

REVIEW = '/home/hatch/workspace/teenz-bible-review'
p = f'{REVIEW}/fixes/en_Esther.json'
en = {c['chapter']: c for c in json.load(open(p))}
CH = []

def fix(ch, idx, old, new, desc):
    c = en[ch]
    t = c['paragraphs'][idx]
    assert old in t, f'ch{ch}[{idx}] NOT FOUND: {old[:60]}'
    c['paragraphs'][idx] = t.replace(old, new, 1)
    CH.append((ch, desc))

fix(1, 2, 'every single cup was unique.', 'every single cup was one of a kind.',
    "MSG 1:7 'one-of-a-kind' — 숫자 1 복원")
fix(1, 3, 'inside the main palace.', "inside King Xerxes's main palace.",
    "MSG 1:9 'King Xerxes'' — 이름 복원")
fix(1, 5, 'ignoring his direct order.', "ignoring King Xerxes's direct order.",
    "MSG 1:14 'King Xerxes'' — 이름 복원")
fix(1, 6, 'The second the wives of all the important officials hear what the queen did',
    'The second the wives of the Persian and Mede officials hear what the queen did',
    "MSG 1:18 'Persian and Mede officials' — 민족명 복원")
fix(2, 0, "He was kinda rethinking the whole situation and what he'd ordered.",
    "He started having second thoughts about the whole situation and what he'd ordered.",
    "MSG 2:1 'second thoughts' — 숫자 2 복원")
fix(2, 5, 'Each girl had to go through a whole year of beauty prep',
    'Each girl had to go through twelve months of beauty prep',
    "MSG 2:12 'twelve months' — 숫자 12 복원")
fix(2, 5, "she'd move to a different harem, this one run by Shaashgaz",
    "she'd move to a second harem, this one run by Shaashgaz",
    "MSG 2:14 'a second harem' — 숫자 2 복원")
fix(2, 9, 'One time, when the virgins were all being gathered,',
    'On one of the occasions when the virgins were being gathered together,',
    "MSG 2:19 'On one of the occasions' — 숫자 1 복원")
fix(3, 8, 'Official notices were sent out by messengers',
    'Official bulletins were sent out by messengers',
    "MSG 3:13 'Bulletins' — 용어 복원")
fix(4, 2, 'There\u2019s one rule for any man or woman',
    'There\u2019s a single rule for any man or woman',
    "MSG 4:11 'a single fate' — 숫자 1 복원")
fix(4, 2, 'it\u2019s been a whole month since I was last called to see the king.',
    'it\u2019s been thirty days since I was last called to see the king.',
    "MSG 4:11 'thirty days' — 숫자 30 복원")
fix(6, 0, 'by exposing the assassination plot from Bigthana and Teresh,',
    "by exposing Bigthana and Teresh's plot to assassinate King Xerxes,",
    "MSG 6:2 'assassinate King Xerxes' — 대상/이름 복원")
fix(8, 1, 'begging him to undo the evil plan Haman had cooked up to destroy the Jews.',
    'begging him to undo the evil of Haman the Agagite and cancel his plan to destroy the Jews.',
    "MSG 8:3 'Haman the Agagite' — 칭호 복원")
fix(8, 1, "can you send out an official order to cancel Haman's plan to annihilate the Jews everywhere?",
    'can you send out an official order to cancel the bulletins authorizing the plan of Haman son of Hammedatha the Agagite to annihilate the Jews everywhere?',
    "MSG 8:5 'bulletins authorizing / Haman son of Hammedatha the Agagite' — 인용구 복원")
fix(8, 5, 'The day this was all supposed to go down was the 13th day of the twelfth month, Adar.',
    "The day set for this in all King Xerxes' provinces was the 13th day of the twelfth month, Adar.",
    "MSG 8:13 'in all King Xerxes\\' provinces' — 이름 복원")
fix(9, 2, "They also killed the ten sons of Haman, the Jews' number one hater:",
    "They also killed the ten sons of Haman son of Hammedatha, the Jews' number one hater:",
    "MSG 9:10 'Haman son of Hammedatha' — 이름 복원")
fix(9, 12, 'They sent letters to all the Jews in all 127 provinces,',
    "They sent letters to all the Jews in all 127 provinces of Xerxes' kingdom,",
    "MSG 9:30 '127 provinces of Xerxes\\' kingdom' — 이름 복원")

for ch, desc in CH:
    en[ch].setdefault('changes', []).append(f'완전성 검사(작업자 D): {desc}')
json.dump(list(en.values()), open(p, 'w'), ensure_ascii=False, indent=1)
print(f'applied {len(CH)} fixes')
