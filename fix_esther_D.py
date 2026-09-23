#!/usr/bin/env python3
"""Esther 재감사 수정 적용 (2026-09-23, 작업자 D).
- EN: MSG 8:11 의미 정정 + 슬랭 6-Rule + 타이틀 정리
- KO: 홀/지팡이 오역, 8:11, 9:22 선물 오역, 슬랭 정리
"""
import json

REVIEW = '/home/hatch/workspace/teenz-bible-review'
en_p = f'{REVIEW}/fixes/en_Esther.json'
ko_p = f'{REVIEW}/fixes/ko_Esther.json'
en = {c['chapter']: c for c in json.load(open(en_p))}
ko = {c['chapter']: c for c in json.load(open(ko_p))}

EN_CHANGES = []  # (chapter, desc)
KO_CHANGES = []

def en_fix(ch, idx, old, new, desc):
    c = en[ch]
    p = c['paragraphs'][idx]
    assert old in p, f'EN ch{ch}[{idx}] not found: {old[:60]}'
    c['paragraphs'][idx] = p.replace(old, new, 1)
    EN_CHANGES.append((ch, desc))

def en_title(ch, old, new, desc):
    c = en[ch]
    assert c['title'] == old, f'EN ch{ch} title mismatch: {c["title"]}'
    c['title'] = new
    EN_CHANGES.append((ch, desc))

def ko_fix(ch, idx, old, new, desc):
    c = ko[ch]
    p = c['paragraphs'][idx]
    assert old in p, f'KO ch{ch}[{idx}] not found: {old[:60]}'
    c['paragraphs'][idx] = p.replace(old, new, 1)
    KO_CHANGES.append((ch, desc))

# ---------------- EN ----------------
en_title(1, 'King Throws Wild Party, Gets Ghosted By The Queen',
         'King Throws Wild Party, Gets Rejected By The Queen',
         "타이틀 'Ghosted'→'Rejected' (슬랭 6-Rule 3)")
en_fix(1, 0, 'this king named Xerxes. This dude was the ruler of a massive empire',
       'this king named Xerxes. This king ruled a massive empire', "'dude'→'king' 순화")
en_fix(1, 2, 'he was just flexing, showing off all the crazy rich stuff',
       'he was just showing off all the crazy rich stuff', "'flexing'→'showing off' (Rule 2)")
en_fix(1, 2, 'After that massive flex-fest, the king threw another party',
       'After that massive display, the king threw another party', "'flex-fest'→'display' (Rule 2)")
en_title(2, 'The Royal Glow-Up: From Zero to Hero',
         'The Royal Rise: From Unknown to Queen',
         "타이틀 'Glow-Up'→'Rise' (Rule 1 인터넷 유행어)")
en_fix(2, 0, 'the girl who the king vibes with the most would become',
       'the girl who pleases the king the most would become', "'vibes with'→'pleases' (Rule 2)")
en_fix(3, 1, 'So, they snitched to Haman, thinking something had to be done.',
       'So, they told Haman, thinking something had to be done.', "'snitched'→'told' (Rule 2)")
en_fix(4, 1, 'The queen was shook.', 'The queen was shocked.', "'shook'→'shocked' (Rule 2)")
en_fix(5, 1, '"What\'s up, Queen Esther? What do you want?',
       '"What do you desire, Queen Esther? What do you want?', "'What's up'→MSG식 표현 (Rule 2)")
en_title(6, "The King's Sleepless Night Leads to Haman's Epic Fail",
         "The King's Sleepless Night Leads to Haman's Humiliation",
         "타이틀 'Epic Fail'→'Humiliation' (Rule 1)")
en_fix(6, 8, 'Haman\'s thinking to himself, "OMG, he\'s talking about me! Who else could it be?"',
       'Haman\'s thinking to himself, "He\'s talking about me! Who else could it be?!"',
       "'OMG' 제거 (Rule 4)")
en_title(7, "Haman's Epic Fail at the Dinner Party",
         "Haman's Downfall at the Dinner Party",
         "타이틀 'Epic Fail'→'Downfall' (Rule 1)")
en_fix(7, 4, '\u201cAn enemy. A hater. This evil Haman,\u201d said Esther.',
       '\u201cAn enemy. An adversary. This evil Haman,\u201d said Esther.',
       "'hater'→'adversary' (MSG 7:6, Rule 2)")
en_fix(8, 7, 'Mordecai walked out of the king\'s presence looking like a total boss in a royal robe',
       'Mordecai walked out of the king\'s presence looking magnificent in a royal robe',
       "'total boss'→'magnificent' (Rule 2)")
en_fix(8, 0, 'To top it off, Esther put Mordecai in charge of Haman\'s entire estate. Talk about a major glow-up.',
       'To top it off, Esther put Mordecai in charge of Haman\'s entire estate. What a rise to power!',
       "'glow-up'→'rise to power' (Rule 1)")
en_fix(8, 5, 'They could kill any armed attackers who came after them, and take the attackers\' wives, children, and belongings as spoil.',
       'They could kill anyone who threatened them or their wives and children, and take for themselves anything owned by their enemies.',
       "MSG 8:11 의미 정정 — MSG는 '유대인들·그들의 처자를 위협하는 자를 죽이고 원수들의 소유물을 전리품으로'")
en_fix(9, 1, 'were lowkey helping the Jews because they were scared of Mordecai',
       'were quietly helping the Jews because they were scared of Mordecai',
       "'lowkey'→'quietly' (Rule 1)")

# ---------------- KO ----------------
ko_fix(1, 0, '크세르크세스 왕 시절에 있었던 썰임.', '크세르크세스 왕 시절에 있었던 얘기임.',
       "'썰'→'얘기' (Rule 2)")
ko_fix(1, 2, '완전 플렉스 모드였던 거지.', '완전 자랑 모드였던 거지.',
       "'플렉스 모드'→'자랑 모드' (Rule 2)")
ko_fix(1, 2, '완전 인스타 감성으로 꾸며져 있었대.', '완전 화려하게 꾸며져 있었대.',
       "'인스타 감성'→'화려하게' (Rule 1)")
ko_fix(2, 0, '와쉬티한테 했던 일이랑 자기가 내린 명령에 대해 현타가 온 거임.',
       '와쉬티한테 했던 일이랑 자기가 내린 명령을 후회하게 된 거임.',
       "'현타'→'후회' (Rule 1)")
ko_fix(2, 5, '12달 동안 정해진 뷰티 프로그램을 다 마쳐야',
       '12달 동안 정해진 피부 관리 프로그램을 다 마쳐야', "'뷰티'→'피부 관리'")
ko_fix(4, 0, '왕궁 문으로 들어갈 수 없다는 룰이 있었거든.',
       '왕궁 문으로 들어갈 수 없다는 규칙이 있었거든.', "'룰'→'규칙'")
ko_fix(4, 4, '그러다 죽으면, 죽는 거죠 뭐.', '그러다 죽으면, 죽는 거예요.',
       "MSG 4:16 'If I die, I die' — 가벼운 '뭐' 제거")
ko_fix(5, 0, '손에 있던 금으로 된 지팡이를 쫙 내밀었어. 에스더가 다가가서 그 지팡이 끝을 만졌지.',
       '손에 있던 금 홀을 내밀었어. 에스더가 다가가서 그 홀 끝을 만졌지.',
       "MSG 5:2 'scepter' 오역 정정 (지팡이→홀)")
ko_fix(5, 7, '높이가 한 23미터 되는 교수대를 세워요.',
       '75피트(약 23미터) 높이의 교수대를 세워요.',
       "MSG 5:14 'seventy-five feet' — EN과 일치 (75피트)")
ko_fix(6, 4, '타이밍 엄청난.', '타이밍이 절묘했지.', "비문 슬랭 문장 정리")
ko_fix(6, 8, "'대박, 이거 내 얘기네? 왕이 나 말고 또 누굴 이렇게 챙겨주겠어?'",
       "'어? 이거 나 얘기잖아? 왕이 나 말고 또 누굴 이렇게 챙겨주겠어?'",
       "'대박'→평이한 표현 (Rule 2)")
ko_fix(6, 11, '하만은 완전 쪽팔려서 얼굴도 못 들고 자기 집으로 도망쳤대.',
       '하만은 너무 창피해서 얼굴도 못 들고 자기 집으로 도망쳤대.',
       "'쪽팔려'→'창피해서' (Rule 5)")
ko_fix(8, 1, '왕이 에스더한테 금으로 된 지팡이를 내미니까,',
       '왕이 에스더한테 금 홀을 내미니까,', "'scepter' 오역 정정 (지팡이→홀)")
ko_fix(8, 5, '무장하고 공격해오는 자들은 죽이고, 그 공격자들의 아내와 자녀, 재산은 전리품으로 가져가도 된다는 내용이었지.',
       '자신들이나 자기 아내와 자녀를 위협하는 자는 죽이고, 원수들의 소유물은 전리품으로 가져가도 된다는 내용이었지.',
       "MSG 8:11 의미 정정")
ko_fix(9, 1, '다들 무서워서 쫄았던 거지.', '다들 무서워서 벌벌 떨었던 거지.',
       "'쫄다'→'벌벌 떨다' (Rule 2)")
ko_fix(9, 1, '왕 밑에서 일하는 모든 애들이 모르드개를 두려워해서',
       '왕 밑에서 일하는 모든 사람들이 모르드개를 두려워해서', "'애들'→'사람들'")
ko_fix(9, 3, '나머지 지방에서는 얼마나 더 많이 죽였겠어? 대단하네. 이제 또 뭐 원하는 거 있어?',
       '나머지 지방에서는 얼마나 더 많이 죽였겠어? 이제 또 뭐 원하는 거 있어?',
       "MSG 9:12에 없는 '대단하네' 삭제")
ko_fix(9, 8, '잔치를 열고 즐기면서 서로 음식을 나눠 먹고 가난한 사람들에게 선물을 주라고 했대.',
       '잔치를 열고 즐기면서 서로 선물을 주고받고 가난한 사람들에게 선물을 주라고 했대.',
       "MSG 9:22 'sending and receiving of presents' 오역 정정")
ko_fix(10, 1, '유다 사람들 사이에서 완전 인기 짱이었고, 다들 엄청 존경했대.',
       '유다 사람들한테 아주 인기가 많았고, 다들 엄청 존경했대.',
       "'인기 짱'→평이한 표현 (Rule 2)")

for ch, desc in EN_CHANGES:
    en[ch].setdefault('changes', []).append(f'재감사(작업자 D): {desc}')
for ch, desc in KO_CHANGES:
    ko[ch].setdefault('changes', []).append(f'재감사(작업자 D): {desc}')

json.dump(list(en.values()), open(en_p, 'w'), ensure_ascii=False, indent=1)
json.dump(list(ko.values()), open(ko_p, 'w'), ensure_ascii=False, indent=1)
print(f'EN fixes: {len(EN_CHANGES)}, KO fixes: {len(KO_CHANGES)}')
