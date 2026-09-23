#!/usr/bin/env python3
"""Worker E2: Jeremiah name/place restorations.

EN dropped several specific names/places that KO retained (and MSG has).
Restore in EN; restore in both where both dropped.
"""
import json

REVIEW = '/home/hatch/workspace/teenz-bible-review'
en = json.load(open(f'{REVIEW}/fixes/en_Jeremiah.json', encoding='utf-8'))
ko = json.load(open(f'{REVIEW}/fixes/ko_Jeremiah.json', encoding='utf-8'))
en_by = {c['chapter']: c for c in en}
ko_by = {c['chapter']: c for c in ko}


def fix(ch, lang, idx, old, new, note):
    d = en_by[ch] if lang == 'en' else ko_by[ch]
    t = d['paragraphs'][idx]
    assert old in t, f'ch{ch} idx{idx} [{lang}]: not found: {old[:60]}'
    d['paragraphs'][idx] = t.replace(old, new, 1)
    d['changes'].append(note)


# --- EN only (KO already has these) ---
fix(2, 'en', 4, "Go check the islands in the west, or the deserts in the east.",
    "Go check the islands in the west, or the Kedar wilderness in the east.",
    "복원: Kedar (KO/MSG 기준)")
fix(2, 'en', 6, "Even the Egyptians have crushed you.",
    "Even the Egyptians from Memphis and Tahpanhes have crushed you.",
    "복원: Memphis, Tahpanhes (KO/MSG 기준)")
fix(2, 'en', 7, "A drink from their rivers?",
    "A drink from the Nile or the Euphrates?",
    "복원: Nile, Euphrates (KO/MSG 기준)")
fix(2, 'en', 9, "I haven't chased after false gods",
    "I haven't chased after the Baal gods",
    "복원: Baal (KO/MSG 기준)")
fix(24, 'en', 0, "had dragged King Jehoiachin, the leaders of Judah",
    "had dragged King Jehoiachin son of Jehoiakim, the leaders of Judah",
    "복원: son of Jehoiakim (KO/MSG 기준)")
fix(26, 'en', 14, "sent a guy named Elnathan with a squad",
    "sent Elnathan son of Achbor with a squad",
    "복원: son of Achbor (KO/MSG 기준)")
fix(39, 'en', 2, "dragged him to King Nebuchadnezzar in Riblah.",
    "dragged him to King Nebuchadnezzar in Riblah in the land of Hamath.",
    "복원: in Hamath (KO/MSG 기준)")
fix(52, 'en', 5, "dragged him to the king of Babylon at Riblah, who put him on trial",
    "dragged him to the king of Babylon at Riblah in Hamath, who put him on trial",
    "복원: in Hamath (KO/MSG 기준)")

# --- Both EN and KO ---
fix(21, 'en', 0, "King Zedekiah sent two guys, Pashur and Zephaniah,",
    "King Zedekiah sent two guys, Pashur son of Malkijah and Zephaniah son of Maaseiah,",
    "복원: son of Malkijah, son of Maaseiah (MSG 기준)")
fix(21, 'ko', 0, "시드기야 왕이 파스훌이랑 스바냐라는 신하를",
    "시드기야 왕이 말기야의 아들 파스훌이랑 마아세야의 아들 스바냐라는 신하를",
    "복원: son of Malkijah, son of Maaseiah (KO, MSG 기준)")

fix(26, 'en', 12, "Did King Hezekiah or anyone in Judah kill Micah for that sermon?",
    "Did King Hezekiah or anyone in Judah kill Micah of Moresheth for that sermon?",
    "복원: of Moresheth (MSG 기준)")
fix(26, 'ko', 12, "히스기야 왕이나 유다 백성이 그 설교 때문에 미가를 죽였어?",
    "히스기야 왕이나 유다 백성이 그 설교 때문에 모레셋 사람 미가를 죽였어?",
    "복원: of Moresheth (KO, MSG 기준)")

fix(35, 'en', 5, "We've followed every single thing our ancestor Jonadab commanded.",
    "We've followed every single thing our ancestor Jonadab son of Recab commanded.",
    "복원: son of Recab (MSG 기준)")
fix(35, 'ko', 5, "요나답 할아버지가 시키신 거 다 지켰다고요.",
    "레갑의 아들 요나답 할아버지가 시키신 거 다 지켰다고요.",
    "복원: son of Recab (KO, MSG 기준)")

fix(37, 'en', 0, "He replaced King Jehoiachin.",
    "He replaced King Jehoiachin son of Jehoiakim.",
    "복원: son of Jehoiakim (MSG 기준)")
fix(37, 'ko', 0, "원래 있던 여호야긴 왕 대신에 왕이 된 거임.",
    "원래 있던 여호야김의 아들 여호야긴 왕 대신에 왕이 된 거임.",
    "복원: son of Jehoiakim (KO, MSG 기준)")

fix(39, 'en', 1, "You had guys like Nergal-sharezer, Nebushazban the Rabsaris,",
    "You had guys like Nergal-sharezer of Simmagar, Nebushazban the Rabsaris,",
    "복원: of Simmagar (MSG 기준)")
# KO ch39 idx1: check text
k39 = ko_by[39]
print('KO39 idx1:', k39['paragraphs'][1][:200])

fix(52, 'en', 9, "Nebuzaradan marched them all to the king of Babylon at Riblah.",
    "Nebuzaradan marched them all to the king of Babylon at Riblah in Hamath.",
    "복원: in Hamath (MSG 기준)")

json.dump(en, open(f'{REVIEW}/fixes/en_Jeremiah.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Jeremiah.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('name/place fixes applied')
