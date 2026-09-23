#!/usr/bin/env python3
"""1 Corinthians MSG 재감사 빌더.
- EN: allBibleData.json의 기존 1Corinthians 텍스트를 MSG 158문단 구조로 재배열/배지 수정/내용 복원.
- KO: gospelDataKo.ts 추출본(ko_1cor_source.json)을 MSG 구조로 정리 (§ 헤더 MSG 원문으로 교체, 추가 헤더 제거).
- 최종 EN/KO 모두 MSG 문단 구조와 1:1 일치. merges 없음. splits는 MSG 자체 중첩 3건만 선언.
"""
import json

SRC = '/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json'
KO_SRC = '/home/hatch/workspace/teenz-bible-review/ko_1cor_source.json'
OUT_EN = '/home/hatch/workspace/teenz-bible-review/fixes/en_1Corinthians.json'
OUT_KO = '/home/hatch/workspace/teenz-bible-review/fixes/ko_1Corinthians.json'

en_data = {c['num']: c for c in json.load(open(SRC))['1 Corinthians']}
ko_data = {c['num']: c for c in json.load(open(KO_SRC))}

def EP(ch, i):
    return en_data[ch]['paragraphs'][i]

def KP(ch, i):
    return ko_data[ch]['paragraphs'][i]

def split_after(text, marker):
    """marker 포함 앞부분 / 뒷부분으로 분리. marker가 없으면 AssertionError."""
    assert marker in text, f"MARKER NOT FOUND: {marker[:60]!r}"
    a, b = text.split(marker, 1)
    return (a + marker).strip(), b.strip()

def fix(text, old, new):
    assert old in text, f"FIX TARGET NOT FOUND: {old[:60]!r}"
    return text.replace(old, new, 1)

en_chapters = []
ko_chapters = []

def add_en(num, title, paras, badges, changes, splits=None):
    assert len(paras) == len(badges), f"ch{num}: paras {len(paras)} != badges {len(badges)}"
    assert all(b for b in badges), f"ch{num}: null badge"
    en_chapters.append({
        'book': '1 Corinthians', 'chapter': num, 'title': title,
        'review_status': 'msg_audited',
        'paragraphs': paras, 'verseRanges': badges, 'msg_ranges': list(badges),
        'changes': changes, 'merges': [], 'splits': splits or [],
        'confirmations_needed': [],
    })

def add_ko(num, paras, badges, changes, splits=None):
    assert len(paras) == len(badges), f"ch{num}: KO paras {len(paras)} != badges {len(badges)}"
    assert all(b for b in badges), f"ch{num}: KO null badge"
    ko_chapters.append({
        'book': '1 Corinthians', 'chapter': num,
        'review_status': 'msg_audited',
        'paragraphs': paras, 'verseRanges': badges, 'msg_ranges': list(badges),
        'changes': changes, 'merges': [], 'splits': splits or [],
        'confirmations_needed': [],
    })

SPLIT_OVERLAP_NOTE = ('MSG 자체 중첩 범위: MSG 원문에서 두 문단의 절 범위가 겹침. '
                      '배지는 MSG 원문 그대로 유지.')

# ---------------- CH1 ----------------
e5a, e5b = split_after(EP(1, 5), "You've gotta stop fighting. Seriously.")
e5b1, e5b2 = split_after(e5b, '"I\'m only on Team Messiah!"')
e6a, e6b = split_after(EP(1, 6), "would make the cross seem like no big deal.")
p1_3 = fix(EP(1, 2), "our main man, Jesus", "Jesus our Master")
add_en(1, "Don't Be a Bunch of Fanboys",
    [EP(1, 1), p1_3, EP(1, 3), EP(1, 4),
     "§The Cross: The Irony of God's Wisdom",
     e5a, e5b1, e5b2, e6a, e6b + " " + EP(1, 7), EP(1, 8), EP(1, 9)],
    ['1-2', '3', '4-6', '7-9', '10', '10', '11-12', '13-16', '17', '18-21', '22-25', '26-31'],
    ["잘못된 위치의 '§Divisions in the Church' 헤더 제거 → MSG § 'The Cross: The Irony of God's Wisdom'를 7-9 뒤(10절 앞)에 배치",
     "기존 10-15 병합 문단을 MSG 구조대로 10 / 11-12 / 13-16 세 문단으로 분리",
     "기존 17-18 문단을 17과 18-21로 분리하고, 기존 20-22 문단을 18-21에 통합 (MSG 18-21 한 문단 복원)",
     "배지 수정: 1-3→1-2, 4-5→4-6, 27-31→26-31 (MSG 기준)",
     "'our main man, Jesus' → 'Jesus our Master'로 교정"])
add_ko(1,
    [KP(1, 1), KP(1, 2), KP(1, 3), KP(1, 4),
     "§십자가, 하나님의 역설적인 지혜",
     KP(1, 6), KP(1, 7), KP(1, 8), KP(1, 9), KP(1, 10), KP(1, 11), KP(1, 12)],
    ['1-2', '3', '4-6', '7-9', '10', '10', '11-12', '13-16', '17', '18-21', '22-25', '26-31'],
    ["장 시작의 추가 헤더 '§교회 안의 분열' 제거 (MSG 1장에는 해당 § 없음)",
     "중간의 무배지 헤더 '십자가, 하나님의 역설적인 지혜' → MSG § 헤더로 승격, 10절 배지 공유"])

# ---------------- CH2 ----------------
add_en(2, "God's Secret Plan",
    [EP(2, 1), EP(2, 2), EP(2, 3), EP(2, 4), EP(2, 5)],
    ['1-2', '3-5', '6-10', '10-13', '14-16'],
    ["MSG에 없는 추가 헤더 '§God's Wisdom vs. World's Wisdom' 제거",
     "배지 수정: 3-4→3-5, 6-8→6-10 (MSG 기준)"],
    splits=[{'msg_range': '6-10', 'paras': [2, 3], 'note': SPLIT_OVERLAP_NOTE}])
add_ko(2,
    [KP(2, 1), KP(2, 2), KP(2, 3), KP(2, 4), KP(2, 5)],
    ['1-2', '3-5', '6-10', '10-13', '14-16'],
    ["장 시작의 추가 헤더 '§하나님의 지혜 vs. 세상의 지혜' 제거 (MSG 2장에는 § 없음)"],
    splits=[{'msg_range': '6-10', 'paras': [2, 3], 'note': SPLIT_OVERLAP_NOTE}])

# ---------------- CH3 ----------------
p3_19 = fix(EP(3, 5), "He roasts the fakes", "He catches the fakes")
add_en(3, "Quit Acting Like Babies",
    [EP(3, 1), EP(3, 2), EP(3, 3), EP(3, 4), p3_19, EP(3, 6)],
    ['1-4', '5-9', '9-15', '16-17', '18-20', '21-23'],
    ["MSG에 없는 추가 헤더 '§Spiritual Maturity' 제거",
     "배지 수정: 6-9→5-9, 10-15→9-15, 17-18→16-17, 19-21→18-20 (MSG 기준)",
     "'He roasts the fakes' → 'He catches the fakes' (MSG 3:19 'He catches the wise in their craftiness')"],
    splits=[{'msg_range': '5-9', 'paras': [1, 2], 'note': SPLIT_OVERLAP_NOTE}])
add_ko(3,
    [KP(3, 1), KP(3, 2), KP(3, 3), KP(3, 4), KP(3, 5), KP(3, 6)],
    ['1-4', '5-9', '9-15', '16-17', '18-20', '21-23'],
    ["장 시작의 추가 헤더 '§영적 성숙' 제거 (MSG 3장에는 § 없음)"],
    splits=[{'msg_range': '5-9', 'paras': [1, 2], 'note': SPLIT_OVERLAP_NOTE}])

# ---------------- CH4 ----------------
add_en(4, "Who Do You Think You Are?",
    [EP(4, 1), EP(4, 2), EP(4, 3), EP(4, 4), EP(4, 5), EP(4, 6), EP(4, 7), EP(4, 8), EP(4, 9)],
    ['1-4', '5', '6', '7-8', '9-13', '14-16', '17', '18-20', '21'],
    ["MSG에 없는 추가 헤더 '§Servants of Christ' 제거",
     "배지 수정: 1-2→1-4, 5-6→5, 6-7→6, 8-10→7-8, 18-19→18-20 (MSG 기준, 내용과 배지 일치)"])
add_ko(4,
    [KP(4, 1), KP(4, 2), KP(4, 3), KP(4, 4), KP(4, 5), KP(4, 6), KP(4, 7), KP(4, 8), KP(4, 9)],
    ['1-4', '5', '6', '7-8', '9-13', '14-16', '17', '18-20', '21'],
    ["장 시작의 추가 헤더 '§그리스도의 종' 제거 (MSG 4장에는 § 없음)"])

# ---------------- CH5 ----------------
e5_3a, e5_3b = split_after(EP(5, 3), "so let's keep it honest—no shady stuff, just truth.")
p5_35 = fix(EP(5, 2), "flexing His power", "showing his power")
add_en(5, "Time to Clean House",
    ["§The Mystery of Sex", EP(5, 1), p5_35, e5_3a, e5_3b],
    ['1-2', '1-2', '3-5', '6-8', '9-13'],
    ["잘못된 헤더 '§Dealing with Sin in the Church' → MSG § 'The Mystery of Sex'로 교체 (1-2 배지 공유)",
     "기존 6-13 병합 문단을 MSG 구조대로 6-8 / 9-13 두 문단으로 분리",
     "배지 수정: 1-4→1-2, 5-10→3-5 (MSG 기준)",
     "'Jesus will be there flexing His power' → 'showing his power'로 교정"])
add_ko(5,
    ["§성의 신비", KP(5, 2), KP(5, 3), KP(5, 4), KP(5, 5)],
    ['1-2', '1-2', '3-5', '6-8', '9-13'],
    ["'§교회 안의 죄를 다루다' → MSG § '성의 신비'로 교체 (1-2 배지 공유)",
     "중간의 무배지 추가 헤더 '너네 몸으로 하나님한테 영광을 돌리셈' 제거 (6:20 문구 오배치)"])

# ---------------- CH6 ----------------
p6_911 = fix(EP(6, 4),
    "The people who just use and abuse others, who are messed up with sex, and trash the planet—they're not on the guest list for God's kingdom.",
    "The people who are messed up with sex, worship idols, cheat on their partners, steal, get wasted, trash-talk others, and scam people—they're not on the guest list for God's kingdom.")
p6_1415 = fix(EP(6, 7), "God flexed his power", "God showed his power")
p6_1620 = fix(EP(6, 8), "like God's crib", "like God's temple")
add_en(6, "Don't Be a Court-Tattler",
    [EP(6, 1), EP(6, 2), EP(6, 3), p6_911, EP(6, 5), EP(6, 6), p6_1415, p6_1620],
    ['1-4', '5-6', '7-8', '9-11', '12', '13', '14-15', '16-20'],
    ["MSG에 없는 추가 헤더 '§Lawsuits and Your Body' 제거",
     "배지 수정: 1-3→1-4, 4-5→5-6, 9-10→9-11, 11-12→12 (MSG 기준)",
     "9-11의 죄 목록을 MSG(우상숭배·간음·도둑·탐욕·술취함·욕설·사기)에 맞게 복원 ('trash the planet' 삭제)",
     "'God flexed his power' → 'God showed his power', \"God's crib\" → \"God's temple\"로 교정"])
add_ko(6,
    [KP(6, 2), KP(6, 3), KP(6, 4), KP(6, 5), KP(6, 6), KP(6, 7), KP(6, 8), KP(6, 9)],
    ['1-4', '5-6', '7-8', '9-11', '12', '13', '14-15', '16-20'],
    ["장 시작의 추가 헤더 '§소송과 몸의 성전' 제거 (MSG 6장에는 § 없음)",
     "깨진 마크다운 잔재 '_고린도전서 6장_' 제거"])

# ---------------- CH7 ----------------
e7_1a, e7_1b = split_after(EP(7, 1), "being single is a good way to go,")
e7_1a = e7_1a[:-1] + "."
e7_1b = "B" + e7_1b[1:]  # 문단 시작으로 대문자화
add_en(7, "Single, Married, or It's Complicated?",
    ["§To Be Married, to Be Single . . .", e7_1a, e7_1b,
     EP(7, 2), EP(7, 3), EP(7, 4), EP(7, 5), EP(7, 6), EP(7, 7), EP(7, 8),
     EP(7, 9), EP(7, 10), EP(7, 11), EP(7, 12), EP(7, 13), EP(7, 14), EP(7, 15)],
    ['1', '1', '2-6', '7', '8-9', '10-11', '12-14', '15-16', '17', '18-19',
     '20-22', '23-24', '25-28', '29-31', '32-35', '36-38', '39-40'],
    ["잘못된 헤더 '§On Marriage and Singleness' → MSG § 'To Be Married, to Be Single . . .'로 교체 (1절 배지 공유)",
     "기존 1-2 병합 문단을 MSG 구조대로 1 / 2-6 두 문단으로 분리",
     "배지 수정: 7-8→7, 20-21→20-22, 23→23-24 (MSG 기준, 내용과 배지 일치)"])
add_ko(7,
    ["§결혼할까, 솔로로 살까...", KP(7, 2), KP(7, 3), KP(7, 4), KP(7, 5), KP(7, 6),
     KP(7, 7), KP(7, 8), KP(7, 9), KP(7, 10), KP(7, 11), KP(7, 12), KP(7, 13),
     KP(7, 14), KP(7, 15), KP(7, 16), KP(7, 17)],
    ['1', '1', '2-6', '7', '8-9', '10-11', '12-14', '15-16', '17', '18-19',
     '20-22', '23-24', '25-28', '29-31', '32-35', '36-38', '39-40'],
    ["'§결혼과 독신에 대하여' → MSG § '결혼할까, 솔로로 살까...'로 교체 (1절 배지 공유)",
     "중간의 무배지 추가 헤더 '결혼 vs 솔로, 어떻게 해야 함?' 제거"])

# ---------------- CH8 ----------------
p8_46 = fix(EP(8, 2), "our main man Jesus", "Jesus our Master")
add_en(8, "To Eat or Not to Eat the Idol Meat",
    ["§Freedom with Responsibility", EP(8, 1), p8_46, EP(8, 3), EP(8, 4), EP(8, 5), EP(8, 6)],
    ['1-3', '1-3', '4-6', '7', '8-9', '10', '11-13'],
    ["잘못된 헤더 '§Food Offered to Idols' → MSG § 'Freedom with Responsibility'로 교체 (1-3 배지 공유)",
     "배지 수정: 10-11→10 (MSG 10절 단독 문단)",
     "'our main man Jesus' → 'Jesus our Master'로 교정"])
add_ko(8,
    ["§자유에는 책임이 따르는 거임", KP(8, 2), KP(8, 3), KP(8, 4), KP(8, 5), KP(8, 6), KP(8, 7)],
    ['1-3', '1-3', '4-6', '7', '8-9', '10', '11-13'],
    ["'§우상에게 바친 음식' → MSG § '자유에는 책임이 따르는 거임'으로 교체 (1-3 배지 공유)",
     "중복된 무배지 헤더 '자유에는 책임이 따르는 거임' 제거"])

# ---------------- CH9 ----------------
add_en(9, "Why I Don't Get Paid for This Gig",
    [EP(9, 1), EP(9, 2), EP(9, 3), EP(9, 4), EP(9, 5), EP(9, 6), EP(9, 7), EP(9, 8)],
    ['1-2', '3-7', '8-12', '12-14', '15-18', '19-23', '24-25', '26-27'],
    ["MSG에 없는 추가 헤더 \"§Paul's Rights as an Apostle\" 제거",
     "배지 수정: 1-3→1-2, 3-5→3-7, 8-11→8-12, 12-15→12-14, 16-19→15-18, 20-24→19-23, 25-26→24-25, 27→26-27 (MSG 기준, 내용과 배지 일치)"],
    splits=[{'msg_range': '8-12', 'paras': [2, 3], 'note': SPLIT_OVERLAP_NOTE}])
add_ko(9,
    [KP(9, 1), KP(9, 2), KP(9, 3), KP(9, 4), KP(9, 5), KP(9, 6), KP(9, 7), KP(9, 8)],
    ['1-2', '3-7', '8-12', '12-14', '15-18', '19-23', '24-25', '26-27'],
    ["장 시작의 추가 헤더 '§사도로서 바울의 권리' 제거 (MSG 9장에는 § 없음)"],
    splits=[{'msg_range': '8-12', 'paras': [2, 3], 'note': SPLIT_OVERLAP_NOTE}])

# ---------------- CH10 ----------------
add_en(10, "Don't Get Cocky",
    [EP(10, 1), EP(10, 2), EP(10, 3), EP(10, 4), EP(10, 5), EP(10, 6),
     EP(10, 7), EP(10, 8), EP(10, 9), EP(10, 10), EP(10, 11)],
    ['1-5', '6-10', '11-12', '13', '14', '15-18', '19-22', '23-24', '25-28', '29-30', '31-33'],
    ["MSG에 없는 추가 헤더 '§Warnings from History' 제거",
     "배지 수정: 1-4→1-5, 5-8→6-10, 9-11→11-12, 12-13→13, 19-21→19-22, 22-23→23-24, 24-28→25-28 (MSG 기준, 내용과 배지 일치)"])
add_ko(10,
    [KP(10, 1), KP(10, 2), KP(10, 3), KP(10, 4), KP(10, 5), KP(10, 6),
     KP(10, 7), KP(10, 8), KP(10, 9), KP(10, 10), KP(10, 11)],
    ['1-5', '6-10', '11-12', '13', '14', '15-18', '19-22', '23-24', '25-28', '29-30', '31-33'],
    ["장 시작의 추가 헤더 '§역사에서 배우는 교훈' 제거 (MSG 10장에는 § 없음)"])

# ---------------- CH11 ----------------
p11_2728 = fix(EP(11, 11), "Check yourself before you wreck yourself.", "Take a good look at yourself before you eat.")
add_en(11, "Don't Be That Guy at the Lord's Supper",
    ["§To Honor God", EP(11, 1), EP(11, 2), EP(11, 3), EP(11, 5), EP(11, 6),
     EP(11, 7), EP(11, 8) + " " + EP(11, 9) + " " + EP(11, 10),
     p11_2728, EP(11, 12), EP(11, 13) + " " + EP(11, 14)],
    ['1-2', '1-2', '3-9', '10-12', '13-16', '17-19', '20-22', '23-26', '27-28', '29-32', '33-34'],
    ["잘못된 헤더 '§Worship Guidelines' → MSG § 'To Honor God'로 교체 (1-2 배지 공유)",
     "중간의 추가 헤더 '§Head Coverings' 제거",
     "기존에 3개로 쪼개진 23-26(빵/잔/기념)을 MSG 한 문단으로 복원",
     "기존 31-32 + 33-34(마지막 문장)를 MSG 33-34 한 문단으로 복원",
     "배지 수정: 4-5→3-9, 7-10→10-12, 11-13→13-16, 14-16→17-19, 17-20→20-22, 26-27→27-28, 28-30→29-32 (MSG 기준)",
     "'Check yourself before you wreck yourself.' → 'Take a good look at yourself before you eat.'로 교정"])
add_ko(11,
    ["§하나님의 영광을 위하여", KP(11, 2), KP(11, 4), KP(11, 6), KP(11, 7), KP(11, 8),
     KP(11, 9), KP(11, 10), KP(11, 11), KP(11, 12), KP(11, 13)],
    ['1-2', '1-2', '3-9', '10-12', '13-16', '17-19', '20-22', '23-26', '27-28', '29-32', '33-34'],
    ["'§예배 지침' → MSG § '하나님의 영광을 위하여'로 교체 (1-2 배지 공유)",
     "중복 헤더 '하나님의 영광을 위하여'(무배지), '모든 진짜 권위는 그리스도한테서 오는 거임.', '§자유와 책임' 제거"])

# ---------------- CH12 ----------------
e12_7a, e12_7b = split_after(EP(12, 7), "And when one part is doing great, everyone celebrates.")
add_en(12, "The Ultimate Superpower",
    ["§Spiritual Gifts", EP(12, 1), EP(12, 2), EP(12, 4), EP(12, 5), EP(12, 6), e12_7a, e12_7b],
    ['1-3', '1-3', '4-11', '12-13', '14-18', '19-24', '25-26', '27-31'],
    ["기존 § 헤더 '§Spiritual Gifts'는 MSG 원문과 일치 → 유지, 1-3 배지 부여",
     "MSG에 없는 추가 헤더 '§One Body, Many Parts' 제거",
     "기존 26-31 병합 문단을 MSG 구조대로 25-26 / 27-31 두 문단으로 분리",
     "배지 수정: 5-11→4-11, 12-15→12-13, 16-19→14-18, 20-25→19-24 (MSG 기준)"])
add_ko(12,
    ["§영적 은사", KP(12, 2), KP(12, 3), KP(12, 5), KP(12, 6), KP(12, 7), KP(12, 8),
     KP(12, 9) + " " + KP(12, 10)],
    ['1-3', '1-3', '4-11', '12-13', '14-18', '19-24', '25-26', '27-31'],
    ["'§영적 은사'는 MSG 원문과 일치 → 유지, 1-3 배지 부여",
     "장 설명 헤더 '고린도전서 12장 - 성령님이 주시는 선물들' 제거",
     "오배치된 '§주의 만찬' 헤더 제거 (12장에 주의 만찬 없음)",
     "27-28 / 29-31 두 문단을 MSG 27-31 한 문단으로 복원"])

# ---------------- CH13 ----------------
e13_7a, e13_7b = split_after(EP(13, 7), "But when you grow up, you leave all that kid stuff behind.")
add_en(13, "Love is the Real MVP",
    ["§The Way of Love", EP(13, 1), EP(13, 2), EP(13, 3) + " " + EP(13, 5),
     EP(13, 6), e13_7a, e13_7b, EP(13, 8)],
    ['1', '1', '2', '3-7', '8-10', '11', '12', '13'],
    ["잘못된 헤더 '§The Love Chapter' → MSG § 'The Way of Love'로 교체 (1절 배지 공유)",
     "추가 헤더 '§What Love Looks Like' 제거",
     "기존에 분리된 3절과 4-7을 MSG 3-7 한 문단으로 복원",
     "기존 11절 문단에 섞인 12절 내용을 분리해 MSG 11 / 12 두 문단으로 복원",
     "배지 수정: 12-13→13 (MSG 기준)"])
add_ko(13,
    ["§사랑의 길", KP(13, 2), KP(13, 3), KP(13, 4) + " " + KP(13, 6),
     KP(13, 7), KP(13, 8), KP(13, 9),
     KP(13, 10) + " " + KP(13, 11) + " " + KP(13, 12)],
    ['1', '1', '2', '3-7', '8-10', '11', '12', '13'],
    ["'§사랑의 장' → MSG § '사랑의 길'로 교체 (1절 배지 공유)",
     "추가 헤더 '사랑, 이게 진짜 굉장함', '§한 몸, 여러 지체' 제거",
     "3절과 4-7을 MSG 3-7 한 문단으로 복원",
     "3개로 쪼개진 13절을 MSG 13 한 문단으로 복원"])

# ---------------- CH14 ----------------
e14_2a, e14_2b = split_after(EP(14, 2), "you're letting the whole squad in on it.")
p14_3738 = EP(14, 11).replace(" Sorry, not sorry.", "")
assert p14_3738 != EP(14, 11), "sorry-not-sorry fix failed"
add_en(14, "Superpowers in Church: Who Gets the Mic?",
    ["§Prayer Language", EP(14, 1) + " " + e14_2a, e14_2b + " " + EP(14, 3),
     EP(14, 4), EP(14, 5), EP(14, 6), EP(14, 7), EP(14, 8), EP(14, 9),
     EP(14, 10), p14_3738, EP(14, 12)],
    ['1-3', '1-3', '4-5', '6-8', '9-12', '13-17', '18-19', '20-25', '26-33', '34-36', '37-38', '39-40'],
    ["잘못된 헤더 '§Prophecy vs. Tongues' → MSG § 'Prayer Language'로 교체 (1-3 배지 공유)",
     "기존 1-2 / 2-4 문단을 MSG 구조대로 1-3 / 4-5로 재배치",
     "배지 수정: 6-9→6-8, 9-11→9-12, 26-31→26-33, 33-35→34-36 (MSG 기준)",
     "'Sorry, not sorry.' 삭제"])
add_ko(14,
    ["§기도의 언어", KP(14, 2) + " " + KP(14, 3), KP(14, 4), KP(14, 5), KP(14, 6),
     KP(14, 7), KP(14, 8), KP(14, 9), KP(14, 10), KP(14, 11), KP(14, 12), KP(14, 13)],
    ['1-3', '1-3', '4-5', '6-8', '9-12', '13-17', '18-19', '20-25', '26-33', '34-36', '37-38', '39-40'],
    ["'§예언 vs. 방언' → MSG § '기도의 언어'로 교체 (1-3 배지 공유)",
     "중복된 무배지 헤더 '기도의 언어' 제거",
     "1-2 / 3-4 두 문단을 MSG 1-3 한 문단으로 복원"])

# ---------------- CH15 ----------------
p15_38 = (EP(15, 10) + " But God gives every seed exactly the body he planned—"
          "each kind of seed gets its own body.")
p15_1215 = fix(EP(15, 4), "God flexed his power", "God used his power")
p15_1620 = EP(15, 5)
p15_5157 = " ".join(EP(15, i) for i in (15, 16, 17, 18, 19))
add_en(15, "The Ultimate Transformation",
    ["§Resurrection", EP(15, 1), EP(15, 2), EP(15, 3), p15_1215, EP(15, 5),
     EP(15, 6), EP(15, 7), EP(15, 8), EP(15, 9), p15_38, EP(15, 11),
     EP(15, 12), EP(15, 13), EP(15, 14), p15_5157, EP(15, 20)],
    ['1-2', '1-2', '3-9', '10-11', '12-15', '16-20', '21-28', '29', '30-33', '34',
     '35-38', '39-41', '42-44', '45-49', '50', '51-57', '58'],
    ["헤더 '§The Resurrection' → MSG 원문 '§Resurrection'으로 교정 (1-2 배지 공유)",
     "누락된 38절 내용 복원 ('But God gives every seed exactly the body he planned—each kind of seed gets its own body.')",
     "기존에 5개로 쪼개진 51-57(죽음에 대한 승리의 노래)을 MSG 한 문단으로 복원",
     "배지 수정: 3-7→3-9, 9-11→10-11, 16-19→16-20, 20-25→21-28, 30-32→30-33, 33-34→34, 35-37→35-38, 38-40→39-41, 41-44→42-44, 45-46→45-49, 57-58→58 (MSG 기준)",
     "'God flexed his power' → 'God used his power'로 교정"])
add_ko(15,
    ["§부활", KP(15, 2), KP(15, 3), KP(15, 4), KP(15, 5), KP(15, 6), KP(15, 7),
     KP(15, 8), KP(15, 9), KP(15, 10), KP(15, 11), KP(15, 12), KP(15, 13),
     KP(15, 14), KP(15, 15), KP(15, 16), KP(15, 17)],
    ['1-2', '1-2', '3-9', '10-11', '12-15', '16-20', '21-28', '29', '30-33', '34',
     '35-38', '39-41', '42-44', '45-49', '50', '51-57', '58'],
    ["'§부활' 헤더 유지, 1-2 배지 부여",
     "중복된 무배지 헤더 '부활' 제거"])

# ---------------- CH16 ----------------
e16_9a, e16_9b = split_after(EP(16, 9), "all say what's up.")
p16_1314 = fix(EP(16, 6), "Be absolute units", "Be strong")
add_en(16, "Paul's Wrap-Up & Final Instructions",
    ["§Coming to See You", EP(16, 1), EP(16, 2), EP(16, 3), EP(16, 4),
     p16_1314, EP(16, 7), EP(16, 8), e16_9a, e16_9b,
     EP(16, 10), EP(16, 11), EP(16, 12), EP(16, 13)],
    ['1-4', '1-4', '5-9', '10-11', '12', '13-14', '15-16', '17-18', '19', '20',
     '21', '22', '23', '24'],
    ["잘못된 헤더 '§The Collection and Goodbyes' → MSG § 'Coming to See You'로 교체 (1-4 배지 공유)",
     "추가 헤더 '§Final Shout-Outs' 제거",
     "기존 19-20 병합 문단을 MSG 구조대로 19 / 20 두 문단으로 분리",
     "'Be absolute units' → 'Be strong'으로 교정"])
add_ko(16,
    ["§얘들아, 이제 곧 보러 갈게.", KP(16, 2), KP(16, 3), KP(16, 4), KP(16, 5),
     KP(16, 7), KP(16, 8), KP(16, 9), KP(16, 10), KP(16, 11),
     KP(16, 12), KP(16, 13), KP(16, 14), KP(16, 15)],
    ['1-4', '1-4', '5-9', '10-11', '12', '13-14', '15-16', '17-18', '19', '20',
     '21', '22', '23', '24'],
    ["'§헌금 모으기와 작별 인사' → MSG § '얘들아, 이제 곧 보러 갈게.'로 교체 (1-4 배지 공유)",
     "중복된 무배지 헤더 '얘들아, 이제 곧 보러 갈게.' 제거",
     "오배치된 '§우리의 미래 몸' 헤더 제거"])

# ---------------- write ----------------
# EN/KO 구조 일치 최종 검증
assert len(en_chapters) == 16 and len(ko_chapters) == 16
for e, k in zip(en_chapters, ko_chapters):
    assert e['chapter'] == k['chapter']
    assert len(e['paragraphs']) == len(k['paragraphs']), f"ch{e['chapter']} EN/KO 문단 수 불일치"
    assert e['verseRanges'] == k['verseRanges'], f"ch{e['chapter']} EN/KO 배지 불일치"

json.dump(en_chapters, open(OUT_EN, 'w'), ensure_ascii=False, indent=1)
json.dump(ko_chapters, open(OUT_KO, 'w'), ensure_ascii=False, indent=1)
print(f"wrote {OUT_EN} ({len(en_chapters)} chapters)")
print(f"wrote {OUT_KO} ({len(ko_chapters)} chapters)")
total_paras = sum(len(c['paragraphs']) for c in en_chapters)
print(f"total paragraphs: {total_paras} (MSG: 158)")
