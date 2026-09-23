#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""D2 게이트 4 수정 반영 2차: checker 잔여 후보 중 실제 누락 확정분 수정."""
import io, os
os.chdir('/home/hatch/workspace/teenz-bible-review')

FIXES = [
 # ch21 12-15: 엘리야 편지에서 여호사밧/아사/북이스라엘/아합 길 누락 -> 복원
 ('work_d2/batch3_21_25.py',
  "says: You've led your family and Judah badly \\u2014 like Ahab and his family. You've killed your own brothers, your own family \\u2014 better men than you!",
  "says: You haven't kept to the ways of your father Jehoshaphat and your grandfather Asa, kings of Judah. Instead you've taken up the ways of the kings of Israel in the north, leading Judah and Jerusalem away from God \\u2014 going step by step down the apostate path of Ahab and his crew. You've killed your own brothers, your own family \\u2014 better men than you!"),
 ('work_d2/batch3_21_25.py',
  "이렇게 말씀하신다. 네 가족과 유다를 나쁘게 이끌었다. 아합과 그 집안처럼. 네 형제들,",
  "이렇게 말씀하신다. 네 아버지 여호사밧과 네 할아버지 아사, 유다 왕들의 길을 지키지 않았다. 대신 북쪽 이스라엘 왕들의 길을 따라 유다와 예루살렘을 하나님에게서 떠나게 했다 \\u2014 아합과 그 무리의 배도 길을 한 걸음씩 따라가며. 네 형제들,"),
 # ch21 16-18: MSG는 Ethiopians
 ('work_d2/batch3_21_25.py',
  "the Arabs who lived near the Cushites against Jehoram",
  "the Arabs who lived near the Ethiopians against Jehoram"),
 ('work_d2/batch3_21_25.py',
  "구스 사람들 근처에 살던 블레셋 사람과 아라비아 사람",
  "에티오피아 사람들 근처에 살던 블레셋 사람과 아라비아 사람"),
 # ch30 15-20: The Revelation of Moses 복원
 ('work_d2/batch5_30_33.py',
  "They confirmed the customary order of worship, following the instructions of Moses the man of God, and the priests sprinkled",
  "Ready now, they stood at their posts as set out in The Revelation of Moses the man of God, and the priests sprinkled"),
 ('work_d2/batch5_30_33.py',
  "하나님의 사람 모세의 지시대로 예배의 관례적 순서를 확인했고,",
  "하나님의 사람 모세의 계시에 정해진 대로 자기 자리에 섰고,"),
 # ch31 20-21: Commandments 복원
 ('work_d2/batch5_30_33.py',
  "whether in worship of God or in obedience to the law, he did with all his heart",
  "whether in worship of God or in obedience to his law and commandments, he did with all his heart"),
 ('work_d2/batch5_30_33.py',
  "하나님 예배든 율법 순종이든 맡은 모든 일을 전심으로 했고, 성공했어.",
  "하나님 예배든 율법과 계명 순종이든 맡은 모든 일을 전심으로 했고, 성공했어."),
 # ch32 32-33: Royal Annals 복원
 ('work_d2/batch5_30_33.py',
  "is written in the vision of the prophet Isaiah son of Amoz in the Book of the Kings of Judah and Israel.",
  "is written in the vision of the prophet Isaiah son of Amoz in the Royal Annals of the Kings of Judah and Israel."),
 ('work_d2/batch5_30_33.py',
  "유다와 이스라엘 열왕기에 있는 아모스의 아들 선지자 이사야의 환상에 기록되어 있어.",
  "유다와 이스라엘 왕들의 왕실 연대기에 있는 아모스의 아들 선지자 이사야의 환상에 기록되어 있어."),
 # ch35 26: txt 경계대로 여호아하스 즉위 문장을 35장 마지막에 배치
 ('work_d2/batch6_34_36.py',
  "are written in the Royal Annals of the Kings of Israel and Judah.",
  "are written in the Royal Annals of the Kings of Israel and Judah. By popular choice, Jehoahaz son of Josiah was made king at Jerusalem, succeeding his father."),
 ('work_d2/batch6_34_36.py',
  "이스라엘과 유다 왕들의 왕실 연대기에 기록되어 있어.",
  "이스라엘과 유다 왕들의 왕실 연대기에 기록되어 있어. 백성의 선택으로 요시야의 아들 여호아하스가 예루살렘에서 왕이 되어 아버지를 이었어."),
 # ch36 1-4: 위 문장 이동에 따라 중복 제거
 ('work_d2/batch6_34_36.py',
  "The people of the land took Jehoahaz son of Josiah and made him king in Jerusalem, succeeding his father. Jehoahaz was twenty-three",
  "Jehoahaz was twenty-three"),
 ('work_d2/batch6_34_36.py',
  "그 땅 백성이 요시야의 아들 여호아하스를 데려와 예루살렘에서 왕으로 세웠어. 아버지를 이어서. 여호아하스는 왕이 될 때 23살이었고",
  "여호아하스는 왕이 될 때 23살이었고"),
 # ch36 5-8: Royal Annals 복원
 ('work_d2/batch6_34_36.py',
  "are written in the Book of the Kings of Israel and Judah. Jehoiachin his son",
  "are written in the Royal Annals of the Kings of Israel and Judah. Jehoiachin his son"),
 ('work_d2/batch6_34_36.py',
  "이스라엘과 유다 열왕기에 기록되어 있어. 아들 여호야긴이",
  "이스라엘과 유다 왕들의 왕실 연대기에 기록되어 있어. 아들 여호야긴이"),
 # ch36 17-21: unkept Sabbaths 복원
 ('work_d2/batch6_34_36.py',
  "the desolate land put in its sabbath years, lying desolate till the seventy years were fulfilled.",
  "the desolate land put to an extended sabbath rest \\u2014 a seventy-year Sabbath rest making up for all the unkept Sabbaths."),
 ('work_d2/batch6_34_36.py',
  "황폐한 땅이 안식년을 채우고, 70년이 찰 때까지 황폐하게 누워 있는.",
  "황폐한 땅이 긴 안식을 맞아 \\u2014 지키지 않은 모든 안식년을 갚는 70년 안식. 70년이 찰 때까지 황폐하게 누워 있는."),
]

failed = []
for path, old, new in FIXES:
    s = io.open(path, encoding='utf-8').read()
    if old not in s:
        failed.append((path, old[:60])); continue
    s = s.replace(old, new, 1)
    io.open(path, 'w', encoding='utf-8').write(s)
if failed:
    print('FAILED:')
    for p, o in failed: print(' ', p, '::', o)
else:
    print(f'OK: {len(FIXES)} replacements applied')
