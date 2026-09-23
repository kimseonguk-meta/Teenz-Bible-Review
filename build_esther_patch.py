#!/usr/bin/env python3
"""Esther EN/KO patch builder v2 — MSG 직접 대조 기반 (2026-09-22).
Ground truth: ~/workspace/teenz-fix/client/src/data/allBibleData.json (EN),
               ~/workspace/teenz-fix/client/src/data/gospelDataKo.ts (KO).
/tmp에 의존하지 않고 소스에서 직접 읽는다.
Writes: fixes/en_Esther.json, fixes/ko_Esther.json
"""
import json, re

SRC = '/home/hatch/workspace/teenz-fix/client/src/data'

# ---------- EN (from allBibleData.json) ----------
_est = json.load(open(f'{SRC}/allBibleData.json'))['Esther']
EN_TITLES = {c['num']: c['title'] for c in _est}
EN = {c['num']: list(c['paragraphs']) for c in _est}

# ---------- KO (from gospelDataKo.ts, read-only parse) ----------
_txt = open(f'{SRC}/gospelDataKo.ts').read()
_est_start = _txt.index('  "Esther": [')
_seg = _txt[_est_start:]
_st = _seg.index('[')
_depth, _in, _esc = 0, False, False
for _j, _ch in enumerate(_seg[_st:], _st):
    if _in:
        if _esc: _esc = False
        elif _ch == '\\': _esc = True
        elif _ch == '"': _in = False
    else:
        if _ch == '"': _in = True
        elif _ch == '[': _depth += 1
        elif _ch == ']':
            _depth -= 1
            if _depth == 0:
                _arr = _seg[_st:_j + 1]; break
_arr = re.sub(r',(\s*[\]\}])', r'\1', _arr)
KOJ = {c['num']: c for c in json.loads(_arr)}
assert len(KOJ) == 10, f"KO chapters: {len(KOJ)}"
KP = {n: list(KOJ[n]['paragraphs']) for n in KOJ}

F = {}

# ================= ch1 =================
p = EN[1]
p[4] = p[4].replace(
    "told his seven personal servants to go get Queen Vashti",
    "told his seven personal servants \u2014 Mehuman, Biztha, Harbona, Bigtha, Abagtha, Zethar, and Carcas \u2014 to go get Queen Vashti")
assert "Mehuman" in p[4], "ch1[4] name restore failed"
F[1] = (p, ["1-3", "1-3", "4-7", "8-9", "10-11", "12-15", "16-18", "19-20", "21-22"],
        [{"msg_range": "1-3", "paras": [0, 1]}],
        ["\ubc30\uc9c0 \uc218\uc815: 4-8\u21924-7, 16-19\u219216-18, 20-21\u219219-20 (MSG \ubb38\ub2e8 \uae30\uc900)",
         "\uc77c\uacf1 \ub0b4\uc2dc \uc774\ub984 \ubcf5\uc6d0 (Mehuman, Biztha, Harbona, Bigtha, Abagtha, Zethar, Carcas) \u2014 MSG 1:10-11"])

# ================= ch2 (12 -> 11 paras) =================
e2 = EN[2]
n0 = e2[0].replace("let's find some amazing, beautiful young women for the king",
                   "let's find some beautiful young virgins for the king")
n0 = n0.replace("to bring all the beautiful, single ladies to the palace in Susa",
                "to bring every beautiful young virgin to the palace in Susa")
n0 = n0 + " " + e2[1]
assert "virgins" in n0 and "single ladies" not in n0
n1 = ("Now, there was this Jewish guy named Mordecai living in the palace complex at Susa. "
      "He was the son of Jair, the grandson of Shimei, the great-grandson of Kish \u2014 a Benjaminite. "
      "His family had been carried off from Jerusalem into exile in Babylon with King Jehoiachin of Judah "
      "when King Nebuchadnezzar of Babylon took them captive. "
      "Mordecai had raised his cousin, Hadassah, who everyone called Esther, because her parents had passed away. "
      "She was seriously stunning, with a great figure and a beautiful face. "
      "After her parents died, Mordecai basically adopted her.")
n6 = e2[7].replace(
    "When it was Esther's turn to go see the king, she didn't ask for anything extra.",
    "When it was Esther's turn to go see the king \u2014 Esther, the daughter of Abihail (Mordecai's uncle), "
    "whom Mordecai had adopted as his own daughter \u2014 she didn't ask for anything extra.")
n7 = e2[8].replace("in the tenth month, which was the seventh year of his reign",
                   "in the tenth month, the month of Tebeth, in the seventh year of his reign")
assert "Tebeth" in n7
np2 = [n0, n1, e2[3], e2[4], e2[5], e2[6], n6, n7, e2[9], e2[10], e2[11]]
F[2] = (np2, ["1-4", "5-7", "8", "9-10", "11", "12-14", "15", "16", "17-18", "19-20", "21-23"], [],
        ["12\u219211 \ubb38\ub2e8 \uc7ac\uc815\ub82c (MSG \ubb38\ub2e8\uacfc 1:1) \u2014 [0]+[1]\uc744 v1-4 \ud558\ub098\ub85c \ud569\uc800",
         "\ubaa8\ub974\ub4dc\uac1c \uacc4\ubcf4 \ubcf5\uc6d0 (Jair\uc758 \uc544\ub4e4, Shimei\uc758 \uc190\uc790, Kish\uc758 \uc99d\uc190\uc790, \ubca0\ub0d0\ubbfc, \uc5ec\ud638\uc57c\uae34/\ub290\ubd80\uac13\ub124\uc0b4 \ud3ec\ub85c) \u2014 MSG 2:5-6",
         "'beautiful, single ladies'\u2192'beautiful young virgins' (\uc758\ubbf8 \ubcc0\uacbd \uc218\uc815) \u2014 MSG 2:2-3",
         "'great personality'\u2192'great figure' (\uc624\uc5ed \uc218\uc815) \u2014 MSG 2:7",
         "'\uc544\ube44\ud558\uc77c\uc758 \ub538 \uc5d0\uc2a4\ub354' \ubcf5\uc6d0 \u2014 MSG 2:15",
         "'\ub370\ubcb3\uc6d4(Tebeth)' \ubcf5\uc6d0 \u2014 MSG 2:16"])

# ================= ch3 =================
e3 = EN[3]
p3 = list(e3)
p3[5] = p3[5].replace("handed it to Haman, the Agagite who was the number one enemy of the Jews",
                      "handed it to Haman son of Hammedatha, the Agagite, the number one enemy of the Jews")
assert "Hammedatha" in p3[5]
p3[8] = p3[8].replace("young, old, women, and children", "young, old, men, women, and children")
assert "men, women" in p3[8]
F[3] = (p3, ["1-2", "2-4", "5-6", "7", "8-9", "10", "11", "12", "13-14", "15"],
        [{"msg_range": "2", "paras": [0, 1], "note": "MSG \ubb38\ub2e8 \ubc94\uc704 1-2\uc640 2-4\uac00 v2\ub97c \uacf5\uc720"}],
        ["\ubc30\uc9c0 \uc218\uc815: 8-10\u21928-9, 11\u219210, 12\u219211, 13-14\u219212",
         "'son of Hammedatha' \ubcf5\uc6d0 \u2014 MSG 3:10",
         "v13 '\ub0a8\uc790(men)' \ub204\ub77d \ubcf5\uc6d0 \u2014 MSG 3:13"])

# ================= ch4 =================
p4 = list(EN[4])
p4[1] = p4[1].replace("Esther\u2019s maids and personal assistants came", "Esther\u2019s maids and eunuchs came")
p4[1] = p4[1].replace("one of the king\u2019s assistants assigned to her", "one of the king\u2019s eunuchs assigned to her")
assert "eunuchs came" in p4[1] and "eunuchs assigned" in p4[1]
F[4] = (p4, ["1-3", "4-8", "9-11", "12-14", "15-16", "17"], [],
        ["\ubc30\uc9c0 \uc218\uc815: 1-4\u21921-3, 5-9\u21924-8, 10-12\u21929-11, 13-15\u219212-14",
         "Hathach '\uc870\uc218(assistants)'\u2192'\ub0b4\uc2dc(eunuchs)' \u2014 MSG 4:5"])

# ================= ch5 =================
F[5] = (list(EN[5]), ["1-3", "1-3", "4", "5-6", "5-6", "7-8", "9-13", "14", "14"],
        [{"msg_range": "1-3", "paras": [0, 1]}, {"msg_range": "5-6", "paras": [3, 4]},
         {"msg_range": "14", "paras": [7, 8]}],
        ["\ubc30\uc9c0 \uc218\uc815: [1] 4\u21921-3, [2] 5-6\u21924, [4] 7-8\u21925-6, [7] 9-13\u219214",
         "MSG \ubb38\ub2e8 split 3\uac74 \uc120\uc5b8 (1-3, 5-6, 14)"])

# ================= ch6 =================
F[6] = (list(EN[6]), ["1-2", "3", "3", "4", "4", "5", "5", "6-9", "6-9", "10", "11", "12-13", "14"],
        [{"msg_range": "3", "paras": [1, 2]}, {"msg_range": "4", "paras": [3, 4]},
         {"msg_range": "5", "paras": [5, 6]}, {"msg_range": "6-9", "paras": [7, 8]}],
        ["\ubc30\uc9c0 \uc218\uc815: [2] 4\u21923, [3] 5\u21924, [4] 6-9\u21924, [5][6] 6-9\u21925, [7] 6-9\u21926-9, [8] 10\u21926-9, [9] 11\u219210, [10] 12-13\u219211",
         "MSG \ubb38\ub2e8 split 4\uac74 \uc120\uc5b8 (3, 4, 5, 6-9)"])

# ================= ch7 =================
F[7] = (list(EN[7]), ["1-2", "3", "4", "5", "6", "6", "7-8", "7-8", "7-8", "9", "9", "10"],
        [{"msg_range": "6", "paras": [4, 5]}, {"msg_range": "7-8", "paras": [6, 7, 8]},
         {"msg_range": "9", "paras": [9, 10]}],
        ["\ubc30\uc9c0 \uc218\uc815: [10] 9-10\u21929",
         "MSG \ubb38\ub2e8 split 3\uac74 \uc120\uc5b8 (6, 7-8, 9)"])

# ================= ch8 =================
p8 = list(EN[8])
p8[5] = ("The king's new order gave the Jews in every city the green light to arm themselves and fight back to the "
         "death. They could kill any armed attackers who came after them, and take the attackers' wives, children, "
         "and belongings as spoil. The day this was all supposed to go down was the 13th day of the twelfth month, "
         "Adar. The order was posted publicly in every province so everyone knew what was up, and the Jews could "
         "get ready to get even with their enemies.")
F[8] = (p8, ["1-2", "3-6", "7-8", "9", "10", "11-13", "14", "15-17"], [],
        ["\ubc30\uc9c0 \uc218\uc815: [2] 6-7\u21927-8, [3] 8-9\u21929",
         "v11 \uc758\ubbf8 \uc624\uc5ed \uc218\uc815 \u2014 MSG\ub294 '\ubb34\uc7a5 \uacf5\uaca9\uc790\ub97c \uc8fd\uc774\uace0 \uacf5\uaca9\uc790\uc758 \uc544\ub0b4\u00b7\uc790\ub140\ub97c \uc804\ub9ac\ud488\uc73c\ub85c'\uc778\ub370 EN\uc774 \ubc14\ub010\ub3c8 \uac83\uc744 \ubc14\ub85c\uc7a1\uc74c"])

# ================= ch9 =================
p9 = list(EN[9])
p9[12] = ("Then Queen Esther\u2014Abihail's daughter\u2014and Mordecai the Jew put their full authority behind a "
          "second letter about Purim to make it official. They sent letters to all the Jews in all 127 provinces, "
          "with words of peace and truth, locking in these days of Purim on the dates Mordecai had set \u2014 dates "
          "they had agreed on for themselves and their descendants, along with the fasting and mourning they had "
          "taken on. Esther's decree sealed the deal, and the whole thing was written down in the records.")
assert "fasting and mourning" in p9[12] and "\\u" not in repr(p9[12])
F[9] = (p9, ["1-4", "1-4", "5-9", "10-12", "13", "14", "15", "16-19", "20-22", "23", "24-26", "26-28", "29-32"],
        [{"msg_range": "1-4", "paras": [0, 1]},
         {"msg_range": "26", "paras": [10, 11], "note": "MSG \ubb38\ub2e8 \ubc94\uc704 24-26\uacfc 26-28\uc774 v26\uc744 \uacf5\uc720"}],
        ["\ubc30\uc9c0 \uc218\uc815: [1] 2-5\u21921-4, [2] 6-10\u21925-9, [4] 13-14\u219213",
         "v29-32 \ub204\ub77d \ubcf5\uc6d0 (\ubaa8\ub974\ub4dc\uac1c\uac00 \uc815\ud55c \ub0a0\uc9dc, \uae08\uc2dd\uacfc \uc560\ub3c4) \u2014 MSG 9:29-32",
         "MSG \ubb38\ub2e8 split 1\uac74 \uc120\uc5b8 (1-4)"])

# ================= ch10 =================
F[10] = (list(EN[10]), ["1-2", "3"], [], ["\ubcc0\uacbd \uc5c6\uc74c (MSG \ub300\uc870 \ud655\uc778)"])

# ================= KO =================
KF = {}
# KO ch1 과도 표현 순화 (teen voice 유지)
_k1 = list(KP[1])
_k1[2] = _k1[2].replace("자랑질을 했대. 완전 플렉스 해버린 거지", "자랑을 엄청 했대. 완전 플렉스 모드였던 거지")
_k1[4] = _k1[4].replace("실제로도 왕비는 존예였다고 함", "실제로도 왕비는 진짜 예뻤다고 함")
_k1[5] = _k1[5].replace("그냥 쌩깠어", "그냥 무시해버렸어")
_k1[6] = _k1[6].replace("오라고 했는데 쌩깠대!", "오라고 했는데 안 간대!")
for _i, _old in [(2, "자랑질"), (4, "존예"), (5, "쌩깠"), (6, "쌩깠")]:
    assert _old not in _k1[_i], "KO ch1 tone-down failed"
KF[1] = (_k1, ["1-3", "1-3", "4-7", "8-9", "10-11", "12-15", "16-18", "19-20", "21-22"],
         ["배지만 EN과 동일하게 수정",
          "과도 표현 순화: 자랑질→자랑을 엄청, 존예→진짜 예뻤다, 쌩깠어/쌩깠대→무시/안 간대"])

kp2 = KP[2]
nk2 = [kp2[0] + " " + kp2[1]]
nk2.append(
    "\uadf8\ub54c \uc218\uc0ac \uad81\uc5d0 \ubaa8\ub974\ub4dc\uac1c\ub77c\ub294 \uc720\ub300\uc778\uc774 \uc0b4\uace0 \uc788\uc5c8\ub294\ub370, "
    "\uc57c\uc77c\uc758 \uc544\ub4e4\uc774\uace0 \uc2dc\ubbc0\uc774\uc758 \uc190\uc790, \uae30\uc2a4\uc758 \uc99d\uc190\uc790\ub85c \ubca0\ub0d0\ubbfc \uc9c0\ud30c \uc0ac\ub78c\uc774\uc5c8\uc74c. "
    "\ubc14\ube4c\ub860 \uc655 \ub290\ubd80\uac13\ub124\uc0b4\uc774 \uc720\ub2e4 \uc655 \uc5ec\ud638\uc57c\uae34\uc774\ub791 \uc0ac\ub78c\ub4e4\uc744 \uc608\ub8e8\uc0b4\ub818\uc5d0\uc11c \ud3ec\ub85c\ub85c \uc7a1\uc544\uac08 \ub54c, "
    "\ubaa8\ub974\ub4dc\uac1c\uc758 \uc870\uc0c1\ub4e4\ub3c4 \ud568\uaed8 \ub04c\ub824\uac14\ub358 \uac70\uc9c0. "
    "\ubaa8\ub974\ub4dc\uac1c\ub294 \ubd80\ubaa8\ub2d8\uc774 \uc548 \uacc4\uc2e0 \uc0ac\ucd0c \ub3d9\uc0dd \ud558\ub2f7\uc0ac, \ub2e4\ub978 \uc774\ub984\uc73c\ub85c\ub294 \uc5d0\uc2a4\ub354\ub97c \ub538\ucc98\ub7fc \ud0a4\uc6e0\ub300. "
    "\uc5d0\uc2a4\ub354\ub294 \ubab8\ub9e4\ub3c4 \uc88b\uace0 \uc5bc\uad74\ub3c4 \uc9c4\uc9dc \uc608\ubee4\ub358 \uac70\uc784. "
    "\ubd80\ubaa8\ub2d8\uc774 \ub3cc\uc544\uac00\uc2e0 \ud6c4\uc5d0 \ubaa8\ub974\ub4dc\uac1c\uac00 \uc785\uc591\ud55c \uac70\uc9c0.")
nk2 += [kp2[3], kp2[4], kp2[5], kp2[6], kp2[7], kp2[8], kp2[9], kp2[10], kp2[11]]
assert len(nk2) == 11
KF[2] = (nk2, ["1-4", "5-7", "8", "9-10", "11", "12-14", "15", "16", "17-18", "19-20", "21-23"],
         ["EN \uc7ac\uc815\ub82c\uc5d0 \ub9de\ucdb0 12\u219211 \ubb38\ub2e8",
          "\ubaa8\ub974\ub4dc\uac1c \uacc4\ubcf4 \uc774\ub984 \ubcf5\uc6d0 (\uc57c\uc77c/\uc2dc\ubbc0\uc774/\uae30\uc2a4, \ubca0\ub0d0\ubbfc, \uc5ec\ud638\uc57c\uae34 \ud3ec\ub85c) \u2014 EN\uacfc \ub3d9\uc77c",
          "'\uc131\uaca9\ub3c4 \uc88b\uace0'\u2192'\ubab8\ub9e4\ub3c4 \uc88b\uace0' (\uc624\uc5ed \uc218\uc815) \u2014 MSG 2:7"])

nk3 = list(KP[3])
nk3[8] = nk3[8].replace("\uc80a\uc740\uc774, \ub178\uc778, \uc5ec\uc790, \uc5b4\ub9b0\uc544\uc774 \ud560 \uac83 \uc5c6\uc774",
                        "\uc80a\uc740\uc774, \ub178\uc778, \ub0a8\uc790, \uc5ec\uc790, \uc5b4\ub9b0\uc544\uc774 \ud560 \uac83 \uc5c6\uc774")
assert "\ub0a8\uc790, \uc5ec\uc790" in nk3[8]
nk3[2] = nk3[2].replace("걔 하나만 조지는 건 좀 아깝다고", "걔 하나만 혼내는 건 좀 아깝다고")
assert "조지는" not in nk3[2], "KO ch3 tone-down failed"
KF[3] = (nk3, ["1-2", "2-4", "5-6", "7", "8-9", "10", "11", "12", "13-14", "15"],
         ["\ubc30\uc9c0\ub9cc EN\uacfc \ub3d9\uc77c\ud558\uac8c \uc218\uc815", "v13 '\ub0a8\uc790(men)' \ub204\ub77d \ubcf5\uc6d0 \u2014 EN\uacfc \ub3d9\uc77c"])

KF[4] = (KP[4], ["1-3", "4-8", "9-11", "12-14", "15-16", "17"],
         ["\ubc30\uc9c0\ub9cc EN\uacfc \ub3d9\uc77c\ud558\uac8c \uc218\uc815 (\ub0b4\uc6a9 \ubcc0\uacbd \uc5c6\uc74c)"])
KF[5] = (KP[5], ["1-3", "1-3", "4", "5-6", "5-6", "7-8", "9-13", "14", "14"],
         ["\ubc30\uc9c0\ub9cc EN\uacfc \ub3d9\uc77c\ud558\uac8c \uc218\uc815 (\ub0b4\uc6a9 \ubcc0\uacbd \uc5c6\uc74c)"])
KF[6] = (KP[6], ["1-2", "3", "3", "4", "4", "5", "5", "6-9", "6-9", "10", "11", "12-13", "14"],
         ["\ubc30\uc9c0\ub9cc EN\uacfc \ub3d9\uc77c\ud558\uac8c \uc218\uc815 (\ub0b4\uc6a9 \ubcc0\uacbd \uc5c6\uc74c)"])
KF[7] = (KP[7], ["1-2", "3", "4", "5", "6", "6", "7-8", "7-8", "7-8", "9", "9", "10"],
         ["\ubc30\uc9c0\ub9cc EN\uacfc \ub3d9\uc77c\ud558\uac8c \uc218\uc815 (\ub0b4\uc6a9 \ubcc0\uacbd \uc5c6\uc74c)"])

nk8 = list(KP[8])
nk8[5] = ("\uc655\uc758 \uba85\ub839\uc740 \ubaa8\ub4e0 \ub3c4\uc2dc\uc5d0 \uc788\ub294 \uc720\ub300\uc778\ub4e4\uc774 \ubb34\uc7a5\ud558\uace0 \uc2a4\uc2a4\ub85c\ub97c \uc9c0\ud0ac \uc218 \uc788\uac8c \ud5c8\ub77d\ud558\ub294 \uac70\uc600\uc74c. "
           "\ubb34\uc7a5\ud558\uace0 \uacf5\uaca9\ud574\uc624\ub294 \uc790\ub4e4\uc740 \uc8fd\uc774\uace0, \uadf8 \uacf5\uaca9\uc790\ub4e4\uc758 \uc544\ub0b4\uc640 \uc790\ub140, \uc7ac\uc0b0\uc740 "
           "\uc804\ub9ac\ud488\uc73c\ub85c \uac00\uc838\uac00\ub3c4 \ub41c\ub2e4\ub294 \ub0b4\uc6a9\uc774\uc5c8\uc9c0. "
           "\uc774 \ub0a0\uc740 \ud06c\uc138\ub974\ud06c\uc138\uc2a4 \uc655\uc758 \ubaa8\ub4e0 \uc9c0\ubc29\uc5d0\uc11c \uc5f4\ub450\uc9f8 \ub2ec, \uc989 \uc544\ub2ec\uc6d4 13\uc77c\ub85c \uc815\ud574\uc84c\uc74c. "
           "\uc774 \uba85\ub839\uc740 \ubaa8\ub4e0 \uc9c0\ubc29\uc5d0 \uacf5\uac1c\uc801\uc73c\ub85c \ubd99\uc5b4\uc11c \ubaa8\ub450\uac00 \uc77d\uc744 \uc218 \uc788\uac8c \ud588\uace0, "
           "\uc720\ub300\uc778\ub4e4\uc774 \uadf8\ub0a0 \uc801\ub4e4\uc5d0\uac8c \ubcf5\uc218\ud560 \uc900\ube44\ub97c \ud560 \uc218 \uc788\ub3c4\ub85d \ud588\ub300.")
KF[8] = (nk8, ["1-2", "3-6", "7-8", "9", "10", "11-13", "14", "15-17"],
         ["\ubc30\uc9c0 [2] 6-7\u21927-8, [3] 8-9\u21929 \uc218\uc815",
          "v11 \uc758\ubbf8 \uc624\uc5ed \uc218\uc815 \u2014 EN\uacfc \ub3d9\uc77c"])

nk9 = list(KP[9])
nk9[12] = nk9[12].replace(
    "이 두 번째 부림절 편지에 왕비의 모든 권한을 사용해서 그가 쓴 내용을 확증하고 지지했음.",
    "이 두 번째 부림절 편지에 둘의 모든 권한을 사용해서 이 편지의 내용을 확증하고 지지했음.")
assert "둘의 모든 권한" in nk9[12], "KO ch9 fix failed"
KF[9] = (nk9, ["1-4", "1-4", "5-9", "10-12", "13", "14", "15", "16-19", "20-22", "23", "24-26", "26-28", "29-32"],
         ["\ubc30\uc9c0\ub9cc EN\uacfc \ub3d9\uc77c\ud558\uac8c \uc218\uc815 (\ub0b4\uc6a9 \ubcc0\uacbd \uc5c6\uc74c)"])
KF[10] = (KP[10], ["1-2", "3"], ["\ubcc0\uacbd \uc5c6\uc74c"])

# KO 고유명사 통일: EN이 Xerxes로 일관되므로 KO의 아하수에로 -> 크세르크세스
for _n in KF:
    _paras, _badges, _changes = KF[_n]
    _np = [q.replace("아하수에로", "크세르크세스") for q in _paras]
    if _np != _paras:
        _changes = _changes + ["고유명사 통일: 아하수에로→크세르크세스 (EN Xerxes와 일치)"]
    KF[_n] = (_np, _badges, _changes)

# ================= assemble & write =================
# KO는 EN과 동일한 구조이므로 splits도 동일하게 기록 (원칙 4: 구조 일치)
SPLITS_BY_CH = {
    1: [{"msg_range": "1-3", "paras": [0, 1]}],
    3: [{"msg_range": "2", "paras": [0, 1], "note": "MSG \ubb38\ub2e8 \ubc94\uc704 1-2\uc640 2-4\uac00 v2\ub97c \uacf5\uc720"}],
    5: [{"msg_range": "1-3", "paras": [0, 1]}, {"msg_range": "5-6", "paras": [3, 4]},
        {"msg_range": "14", "paras": [7, 8]}],
    6: [{"msg_range": "3", "paras": [1, 2]}, {"msg_range": "4", "paras": [3, 4]},
        {"msg_range": "5", "paras": [5, 6]}, {"msg_range": "6-9", "paras": [7, 8]}],
    7: [{"msg_range": "6", "paras": [4, 5]}, {"msg_range": "7-8", "paras": [6, 7, 8]},
        {"msg_range": "9", "paras": [9, 10]}],
    9: [{"msg_range": "1-4", "paras": [0, 1]},
        {"msg_range": "26", "paras": [10, 11], "note": "MSG \ubb38\ub2e8 \ubc94\uc704 24-26\uacfc 26-28\uc774 v26\uc744 \uacf5\uc720"}],
}
en_out, ko_out = [], []
for n in range(1, 11):
    paras, badges, splits, changes = F[n]
    assert len(paras) == len(badges), f"EN ch{n} length mismatch"
    en_out.append({"chapter": n, "title": EN_TITLES[n], "paragraphs": paras,
                   "verseRanges": badges, "msg_ranges": badges,
                   "merges": [], "splits": splits, "changes": changes,
                   "confirmations_needed": []})
    kparas, kbadges, kchanges = KF[n]
    assert len(kparas) == len(kbadges) == len(paras), f"KO ch{n} length mismatch"
    assert kbadges == badges, f"ch{n} EN/KO badge mismatch: {badges} vs {kbadges}"
    ko_out.append({"chapter": n, "title": KOJ[n]['title'], "paragraphs": kparas,
                   "verseRanges": kbadges, "msg_ranges": kbadges,
                   "merges": [], "splits": SPLITS_BY_CH.get(n, []),
                   "changes": kchanges, "confirmations_needed": []})

with open('/home/hatch/workspace/teenz-bible-review/fixes/en_Esther.json', 'w') as f:
    json.dump(en_out, f, ensure_ascii=False, indent=2)
with open('/home/hatch/workspace/teenz-bible-review/fixes/ko_Esther.json', 'w') as f:
    json.dump(ko_out, f, ensure_ascii=False, indent=2)
print("wrote fixes/en_Esther.json and fixes/ko_Esther.json")
