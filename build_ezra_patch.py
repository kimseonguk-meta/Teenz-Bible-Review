#!/usr/bin/env python3
"""Ezra EN/KO patch builder — MSG 직접 대조 기반 (2026-09-22).
Ground truth: ~/workspace/teenz-fix/client/src/data/allBibleData.json (EN),
               ~/workspace/teenz-fix/client/src/data/gospelDataKo.ts (KO).
/tmp에 의존하지 않고 소스에서 직접 읽는다.
Writes: fixes/en_Ezra.json, fixes/ko_Ezra.json

MSG 문단 경계 (BibleGateway 직접 확인):
  ch1: 1-4 / 5-6 / 7-10 / 11
  ch2: 1-58 / 59-60 / 62-63 / 64-67 / 68-69 / 70
  ch3: 1-2 / 3-5 / 6 / 7 / 8-9 / 10-11 / 11-13   (10-11과 11-13은 v11 공유)
  ch4: 1-2 / 3 / 4-5 / 6 / 7 / 8-16 / 17-22 / 23 / 24
  ch5: 1-2 / 3-4 / 5 / 6-7 / 8 / 9-10 / 11-12 / 13-16 / 17
  ch6: 1-3 / 3-5 / 6-7 / 8-10 / 11-12 / 13 / 14-15 / 16-18 / 19 / 20 / 21-22
       (1-3과 3-5는 v3 공유)
  ch7: 1-5 / 6-7 / 8-10 / 11 / 12-20 / 21-23 / 24 / 25 / 26 / 27-28
  ch8: 1-14 / 15-17 / 18-20 / 21-22 / 23 / 24-27 / 28-29 / 30 / 31 / 32-34 / 35 / 36
  ch9: 1-2 / 3 / 4-6 / 6-7 / 8-9 / 10-12 / 13-15   (4-6과 6-7은 v6 공유)
  ch10: 1 / 2-3 / 4 / 5 / 6 / 7-8 / 9 / 10-11 / 12 / 13-14 / 15-17 /
        18-19 / 20 / 21 / 22 / 23 / 24 / 25 / 26 / 27 / 28 / 29 / 30 /
        31-32 / 33 / 34-37 / 38-42 / 43 / 44
"""
import json, re

SRC = '/home/hatch/workspace/teenz-fix/client/src/data'

# ---------- EN (from allBibleData.json) ----------
_est = json.load(open(f'{SRC}/allBibleData.json'))['Ezra']
EN_TITLES = {c['num']: c['title'] for c in _est}
EN = {c['num']: list(c['paragraphs']) for c in _est}

# ---------- KO (from gospelDataKo.ts, read-only parse) ----------
_txt = open(f'{SRC}/gospelDataKo.ts').read()
_est_start = _txt.index('  "Ezra": [')
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

FE = {}  # chapter -> (paragraphs, verseRanges, msg_ranges, splits, changes)
FK = {}


def fin_en(ch, p, vr, mr, splits, changes):
    FE[ch] = {
        'chapter': ch, 'title': EN_TITLES[ch], 'paragraphs': p, 'verseRanges': vr,
        'msg_ranges': mr, 'merges': [], 'splits': splits, 'changes': changes,
        'confirmations_needed': [],
    }


def fin_ko(ch, p, vr, mr, splits, changes):
    FK[ch] = {
        'chapter': ch, 'title': EN_TITLES[ch], 'paragraphs': p, 'verseRanges': vr,
        'msg_ranges': mr, 'merges': [], 'splits': splits, 'changes': changes,
        'confirmations_needed': [],
    }


# ================= ch1 =================
p = EN[1]
vr = ["1-4", "1-4", "5-6", "7-10", "7-10", "11"]
mr = ["1-4", "5-6", "7-10", "11"]
splits = [{"msg_range": "1-4", "paras": [0, 1]},
          {"msg_range": "7-10", "paras": [3, 4]}]
changes = ["배지 수정: 3-5→1-4, 6-7→5-6, 7-10(기물 목록)→7-10 split (MSG 문단 기준)"]
fin_en(1, p, vr, mr, splits, changes)

k = KP[1]
k[3] = k[3].replace("미드르닷은 유다 총독 세스바살한테",
                    "미드르닷은 유다의 왕자 세스바살한테")
assert "유다의 왕자 세스바살" in k[3], "ch1 KO[3] fix failed"
k[4] = k[4].replace("비슷한 은 대접 410개", "똑같은 은 대접 410개")
assert "똑같은 은 대접 410개" in k[4], "ch1 KO[4] fix failed"
changes_k = ["배지 수정: 1-2→1-4, 3-5→1-4, 6-7→5-6, 8-9→7-10, 10→7-10 (MSG 문단 기준)",
             "KO: '유다 총독 세스바살'→'유다의 왕자 세스바살' (MSG 'the prince of Judah')",
             "KO: '비슷한 은 대접 410개'→'똑같은 은 대접 410개' (MSG 'duplicate silver bowls')"]
fin_ko(1, k, vr, mr, splits, changes_k)

# ================= ch2 =================
# [2] prose 명단은 [3]-[20] line-item과 완전 중복 → 삭제, [3]의 반복 안내 문구 제거
p = EN[2]
assert p[2].startswith("From Parosh's crew: 2,172"), "ch2 EN[2] duplicate check failed"
del p[2]
p[2] = p[2].replace("(List repeated for clarity)\n", "")
assert p[2] == "Parosh, 2,172", f"ch2 EN[2->] fix failed: {p[2]!r}"
p[1] = p[1].replace("by their fam line:", "by their family line:")
assert "by their family line:" in p[1], "ch2 EN[1] fix failed"
assert len(p) == 73, f"ch2 EN paras: {len(p)}"
vr = ["1-58"] * 65 + ["59-60"] * 2 + ["61"] * 2 + ["62-63", "64-67", "68-69", "70"]
assert len(vr) == 73
mr = ["1-58", "59-60", "61", "62-63", "64-67", "68-69", "70"]
splits = [{"msg_range": "1-58", "paras": list(range(65))},
          {"msg_range": "59-60", "paras": [65, 66]},
          {"msg_range": "61", "paras": [67, 68]}]
changes = ["문단 삭제: EN[2] prose 명단 — [3]-[20] line-item과 이름·숫자 완전 중복 (모든 항목은 line-item에 보존)",
           "EN[3]: '(List repeated for clarity)' 안내 문구 제거",
           "EN[1]: 'by their fam line'→'by their family line'",
           "배지 수정: null 헤더 9건→1-58/59-60/61 (뒤 본문과 공유), 59-60=[Tel Melah 귀환자·652명], 61=[제사장 가문 Hobaiah·Hakkoz·Barzillai] (MSG 문단 기준)",
           "MSG 2:61은 별도 문단 (제사장 가문) — 59-60과 분리"]
fin_en(2, p, vr, mr, splits, changes)

k = KP[2]
assert k[2].startswith("바로스 자손이 2,172명"), "ch2 KO[2] duplicate check failed"
del k[2]
k[2] = k[2].replace("(다시 한번 명단 공개)\n", "")
assert k[2] == "바로스, 2,172명", f"ch2 KO[2->] fix failed: {k[2]!r}"
assert len(k) == 73, f"ch2 KO paras: {len(k)}"
changes_k = ["문단 삭제: KO[2] prose 명단 — [3]-[20] line-item과 이름·숫자 완전 중복 (모든 항목은 line-item에 보존)",
             "KO[3]: '(다시 한번 명단 공개)' 안내 문구 제거",
             "배지 수정: null 헤더 9건→1-58/59-60/61 (뒤 본문과 공유), 59-60=[델멜라 귀환자·652명], 61=[제사장 가문 호바야·학고스·바르실래] (MSG 문단 기준)",
             "MSG 2:61은 별도 문단 (제사장 가문) — 59-60과 분리"]
fin_ko(2, k, vr, mr, splits, changes_k)

# ================= ch3 =================
p = EN[3]
p[7] = p[7].replace("started weeping loudly when they saw the foundation",
                    "started weeping loudly for joy when they saw the foundation")
assert "weeping loudly for joy" in p[7], "ch3 EN[7] fix failed"
p[1] = p[1].replace("they were lowkey terrified of what their non-Israelite neighbors might pull",
                    "they were scared of what their non-Israelite neighbors might pull")
assert "lowkey" not in p[1], "ch3 EN[1] fix failed"
vr = ["1-2", "3-5", "6", "7", "8-9", "10-11", "10-11", "11-13"]
mr = ["1-2", "3-5", "6", "7", "8-9", "10-11", "11-13"]
splits = [{"msg_range": "10-11", "paras": [5, 6]},
          {"msg_range": "11", "paras": [6, 7], "kind": "boundary_share",
           "note": "MSG 10-11과 11-13이 v11을 공유 — 인접 MSG 문단 경계 공유, split 아님"}]
changes = ["배지 수정: 3-5→6, 6→7, 7-8→8-9, 9-10→10-11, 10-11→10-11(찬양가, split), 11-13 (MSG 문단 기준)",
           "MSG 10-11과 11-13은 v11 공유 (인접 범위 경계 공유, split 아님) — splits[]에 boundary_share로 별도 표기",
           "EN[7]: 'wept loudly for joy' 복원 (MSG 3:12 — 기쁨의 눈물)",
           "EN[1]: 'lowkey terrified'→'scared' 순화"]
fin_en(3, p, vr, mr, splits, changes)

k = KP[3]
k[1] = k[1].replace("좀 쫄렸는데", "좀 무섭긴 했는데")
assert "무섭긴 했는데" in k[1], "ch3 KO[1] fix failed"
k[2] = k[2].replace("대박인 건,", "놀라운 건,")
assert "놀라운 건," in k[2], "ch3 KO[2] fix failed"
k[5] = k[5].replace("예복을 쫙 빼입고", "예복을 갖춰 입고")
assert "예복을 갖춰 입고" in k[5], "ch3 KO[5] fix failed"
changes_k = ["배지 수정: 8-9→8-9(유지), 12→10-11(찬양가, split), 13→11-13 (MSG 문단 기준)",
             "KO 순화: '쫄렸는데'→'무섭긴 했는데', '대박인 건'→'놀라운 건', '예복을 쫙 빼입고'→'예복을 갖춰 입고' (의미 유지)"]
fin_ko(3, k, vr, mr, splits, changes_k)

# ================= ch4 =================
p = EN[4]
p[6] = ("'From: Rehum the commanding officer and Shimshai the secretary, backed by the rest of "
        "their associates—the judges and officials over the people from Tripolis, Persia, Erech, "
        "and Babylon, the Elamites from Susa, and all the others whom the great and honorable "
        "Ashurbanipal deported and settled in the city of Samaria and other places across the Euphrates.")
p[11] = ("'Peace be with you. The letter you sent has been translated and read to me. I gave orders "
         "to search the records, and sure enough, this city has revolted against kings time and again—"
         "rebellion is an old story there. I found out they've had their share of strong kings who took "
         "over beyond the Euphrates and exacted taxes, tribute, and duty. So do this: order these men to "
         "stop work immediately—not a lick of rebuilding in that city unless I order it. Act quickly and "
         "firmly; they've done enough damage to kings!'\"")
assert "great and honorable Ashurbanipal" in p[6]
assert "Peace be with you" in p[11] and "Act quickly and firmly" in p[11]
vr = ["1-2", "3", "4-5", "6", "7", "8-16", "8-16", "8-16", "8-16", "8-16",
      "17-22", "17-22", "23", "24"]
mr = ["1-2", "3", "4-5", "6", "7", "8-16", "17-22", "23", "24"]
splits = [{"msg_range": "8-16", "paras": [5, 6, 7, 8, 9]},
          {"msg_range": "17-22", "paras": [10, 11]}]
changes = ["배지 수정: 3-4→3, 5-6→4-5, 7→6, 8-16→7, 15-20→8-16, 17-22 유지, 21→17-22, 22→17-22 (MSG 문단 기준)",
           "EN[6]: 'all their boys'→'the rest of their associates', 'GOAT Ashurbanipal'→'the great and honorable Ashurbanipal' (MSG 4:9-10)",
           "EN[11]: ''Sup'→'Peace be with you', 'Get on it ASAP'→'Act quickly and firmly', 'taxes'→'taxes, tribute, and duty' (MSG 4:17-22)"]
fin_en(4, p, vr, mr, splits, changes)

k = KP[4]
k[11] = k[11].replace("걔네가 왕들한테 끼친 피해는 이미 충분하니까!",
                      "그 사람들이 왕들한테 끼친 피해는 이미 충분하니까!")
assert "그 사람들이 왕들한테" in k[11], "ch4 KO[11] fix failed"
k[3] = k[3].replace("진짜 아하수에로(크세르크세스) 왕 때는", "진짜 크세르크세스 왕 때는")
assert "크세르크세스 왕 때는" in k[3] and "아하수에로" not in k[3], "ch4 KO[3] fix failed"
k[6] = ("\"발신: 지휘관 르훔과 서기관 심새, 그리고 나머지 동료들 — 트리폴리, 페르시아, 에렉, 바빌론 출신 백성들을 "
        "다스리는 재판관들과 관리들, 수사의 엘람 사람들, 그리고 위대하고 존경받는 아슈르바니팔 왕이 사마리아 성과 "
        "유프라테스 강 너머 다른 지역으로 이주시켜 정착시킨 모든 사람들이 올립니다.\"")
assert "위대하고 존경받는 아슈르바니팔" in k[6]
changes_k = ["배지 수정: 3-4→3, 5-6→4-5, 7→6, 8-9→7, 10→8-16, 11-12→8-16, 13→8-16, 14→8-16, 15-20→8-16, 21→17-22, 22→17-22 (MSG 문단 기준)",
             "KO[3]: '아하수에로(크세르크세스)'→'크세르크세스' (왕 이름 통일)",
             "KO[6]: EN 확정문에 맞춰 재번역 ('the great and honorable Ashurbanipal'→'위대하고 존경받는 아슈르바니팔')",
             "KO[11]: '걔네'→'그 사람들이' 순화"]
fin_ko(4, k, vr, mr, splits, changes_k)

# ================= ch5 =================
p = EN[5]
p[0] = p[0].replace("the prophets Haggai and Zechariah were preaching",
                    "the prophets Haggai and Zechariah son of Iddo were preaching")
assert "Zechariah son of Iddo" in p[0], "ch5 EN[0] fix failed"
vr = ["1-2", "3-4", "5", "6-7", "6-7", "8", "9-10", "11-12", "13-16", "17"]
mr = ["1-2", "3-4", "5", "6-7", "8", "9-10", "11-12", "13-16", "17"]
splits = [{"msg_range": "6-7", "paras": [3, 4]}]
changes = ["배지 수정: 1-3→1-2, 4-5→3-4, 6-7→5, 6-7→6-7(편지 서두, split), 8→6-7(인사말), 9-10→8 (MSG 문단 기준)",
           "EN[0]: 'Zechariah son of Iddo' 복원 (MSG 5:1)"]
fin_en(5, p, vr, mr, splits, changes)

k = KP[5]
k[0] = k[0].replace("선지자 학개랑 스가랴가 유다랑",
                    "선지자 학개랑 잇도의 아들 스가랴가 유다랑")
assert "잇도의 아들 스가랴" in k[0], "ch5 KO[0] fix failed"
k[1] = k[1].replace("다드래가 자기 부하들이랑 같이", "다드래랑 스달보스내가 자기 부하들이랑 같이")
assert "스달보스내" in k[1], "ch5 KO[1] fix failed"
k[3] = k[3].replace("총독 다드래랑 그 부하들이", "총독 다드래랑 스달보스내랑 그 부하 관리들이")
k[4] = k[4].replace("평안하셈!", "평안하십시오!")
assert "평안하십시오!" in k[4], "ch5 KO[4] fix failed"
changes_k = ["배지 수정: 1-3→1-2, 4-5→3-4, 6→5, 7→6-7(편지 서두, split), 8→6-7(인사말), 9→8, 10→9-10 (MSG 문단 기준)",
             "KO[0]: '잇도의 아들 스가랴' 복원 (MSG 5:1)",
             "KO[1]·KO[3]: '스달보스내(Shethar-Bozenai)' 이름 복원 (MSG 5:3, 5:6 — 기존 누락)",
             "KO[4]: '평안하셈'→'평안하십시오' 순화"]
fin_ko(5, k, vr, mr, splits, changes_k)

# ================= ch6 =================
p = EN[6]
p[8] = ("I'm also making a decree that if anyone messes with this order, they're to be impaled on a "
        "timber torn out of their own house, and the house itself gets turned into a manure pit. "
        "And may the God who made that place special take down any king or people who try to stop "
        "this and destroy the Temple in Jerusalem.")
assert "manure pit" in p[8] and "sharpen" not in p[8], "ch6 EN[8] fix failed"
p[11] = p[11].replace("with the prophets Haggai and Zechariah cheering them on",
                      "with the prophets Haggai and Zechariah son of Iddo preaching and cheering them on")
assert "Zechariah son of Iddo" in p[11], "ch6 EN[11] fix failed"
# MSG 19/20 분리 (merge 회피)
p13a = "On the fourteenth day of the first month, the exiles celebrated Passover."
p13b = ("The priests and Levites had all made sure they were spiritually clean, no exceptions. "
        "The Levites sacrificed the Passover lamb for everyone who had returned from exile, "
        "for their brother priests, and for themselves.")
assert p[13].startswith("On the fourteenth day"), "ch6 EN[13] split anchor failed"
p = p[:13] + [p13a, p13b] + p[14:]
assert len(p) == 16, f"ch6 EN paras: {len(p)}"
vr = ["1-3", "1-3", "1-3", "3-5", "6-7", "8-10", "8-10", "8-10",
      "11-12", "11-12", "13", "14-15", "16-18", "19", "20", "21-22"]
mr = ["1-3", "3-5", "6-7", "8-10", "11-12", "13", "14-15", "16-18", "19", "20", "21-22"]
splits = [{"msg_range": "1-3", "paras": [0, 1, 2]},
          {"msg_range": "3", "paras": [2, 3], "kind": "boundary_share",
           "note": "MSG 1-3과 3-5가 v3을 공유 — 인접 MSG 문단 경계 공유, split 아님"},
          {"msg_range": "8-10", "paras": [5, 6, 7]},
          {"msg_range": "11-12", "paras": [8, 9]}]
changes = ["배지 수정: 4-6→3-5, 7-8→6-7, 8-10 유지, 11-12→8-10(2항목), 13-14→11-12, 14-15→11-12(칙령 끝), 16-18→13, 16-18→14-15, 19-20→16-18, 21-22 유지→19/20 분리, 21-22 (MSG 문단 기준)",
           "MSG 1-3과 3-5는 v3 공유 (인접 범위 경계 공유, split 아님) — splits[]에 boundary_share로 별도 표기",
           "EN[13] 분리: MSG 19와 20 합침 → 두 문단으로 분리 (merge 회피)",
           "EN[8]: 'sharpen it' 창작 삭제, 'public toilet. Seriously.'→'manure pit' (MSG 6:11)",
           "EN[11]: 'Zechariah son of Iddo' 복원 (MSG 6:14)"]
fin_en(6, p, vr, mr, splits, changes)

k = KP[6]
k[4] = k[4].replace("다드내랑 스달보스내", "다드래랑 스달보스내")
assert "다드래랑" in k[4], "ch6 KO[4] fix failed"
k[8] = ("그리고 내가 또 명령하는데, 누구든지 이 명령을 어기면 그 사람 집에서 들보를 뽑아다가 거기에 꿰어 죽일 것이다. "
        "그리고 그 집은 거름더미가 될 것이다. 그리고 여기에 자기 이름을 두신 하나님이 이 명령을 어기고 "
        "예루살렘 성전을 파괴하려는 왕이나 백성은 누구든지 다 쓸어버리시길 바란다.")
k[10] = k[10].replace("다드내랑 스달보스내랑", "다드래랑 스달보스내랑")
assert "다드래랑" in k[10], "ch6 KO[10] fix failed"
k[11] = k[11].replace("선지자 학개랑 스가랴가 막 설교하면서 응원해주니까",
                      "선지자 학개랑 잇도의 아들 스가랴가 설교하면서 응원해주니까")
assert "잇도의 아들 스가랴" in k[11], "ch6 KO[11] fix failed"
k13a = "첫째 달 14일에는 포로 생활에서 돌아온 사람들이 유월절을 지켰대."
k13b = ("제사장들이랑 레위인들은 다 예외 없이 몸을 정결하게 하고, 레위인들이 포로 생활에서 돌아온 동족들과 "
        "형제 제사장들, 그리고 자기 자신을 위해서 유월절 양을 잡았어.")
assert k[13].startswith("첫째 달 14일에는"), "ch6 KO[13] split anchor failed"
k = k[:13] + [k13a, k13b] + k[14:]
assert len(k) == 16, f"ch6 KO paras: {len(k)}"
changes_k = ["배지 수정: 1→1-3, §메모→1-3(뒤 본문 공유), 3→1-3, 4-6→3-5, 7-8→6-7, 9→8-10, 10→8-10, 11-12→8-10(2항목), 13-14→11-12, 15→11-12(칙령 끝), 16→13, 17-18→14-15, 19-20→16-18, 21→19/21 분리, 22→20/21-22 (MSG 문단 기준)",
             "KO[13] 분리: MSG 19와 20 합침 → 두 문단으로 분리 (merge 회피)",
             "KO[4]·KO[10]: '다드내'→'다드래' (Tattenai 표기 통일)",
             "KO[8]: '뾰족하게 만들어서 꿰뚫어 죽여버려. 진짜' 순화 (의미 유지 — MSG 6:11)",
             "KO[11]: '잇도의 아들 스가랴' 복원 (MSG 6:14)"]
fin_ko(6, k, vr, mr, splits, changes_k)

# ================= ch7 =================
p = EN[7]
p[0] = ("So, after all that went down, this guy Ezra shows up. This was when Artaxerxes was king of "
        "Persia. Ezra's family tree was seriously stacked: he was the son of Seraiah, son of Azariah, "
        "son of Hilkiah, son of Shallum, son of Zadok, son of Ahitub, son of Amariah, son of Azariah, "
        "son of Meraioth, son of Zerahiah, son of Uzzi, son of Bukki, son of Abishua, son of Phinehas, "
        "son of Eleazar, son of Aaron the high priest. Talk about a legendary bloodline.")
assert "son of Meraioth" in p[0] and "OG high priest" not in p[0], "ch7 EN[0] fix failed"
p[5] = p[5].replace("What's up. I'm officially saying", "Peace. I'm officially saying")
assert p[5].startswith("Peace."), "ch7 EN[5] fix failed"
p[6] = p[6].replace(" And there's no limit on the salt. No cap.", " And there's no limit on the salt.")
assert "No cap" not in p[6], "ch7 EN[6] fix failed"
vr = ["1-5", "6-7", "8-10", "11", "12-20", "12-20", "21-23", "24", "25", "26", "27-28"]
mr = ["1-5", "6-7", "8-10", "11", "12-20", "21-23", "24", "25", "26", "27-28"]
splits = [{"msg_range": "12-20", "paras": [4, 5]}]
changes = ["배지 수정: 1-5→1-5(유지), 1-5→6-7, 6-8→8-10, 8-10→11, 8-10→12-20(편지 머리), 11-18→12-20(칙령 본문), 19-21→21-23, 21-23→24, 23-24→25, 25→26, 26-28→27-28 (MSG 문단 기준)",
           "EN[0]: 에스라 계보 요약('and on and on...') → MSG 7:1-5 전 계보 복원 (Seraiah→Aaron)",
           "EN[0]: 'OG high priest'→'the high priest', 'ancestry was goated' 삭제",
           "EN[5]: 'What's up'→'Peace' (MSG 7:12)", "EN[6]: 'No cap' 삭제"]
fin_en(7, p, vr, mr, splits, changes)

k = KP[7]
changes_k = ["배지 수정: 1-2→1-5, 3-5→6-7, 6-8→8-10, 9→11, 10→12-20(편지 머리), 11-18→12-20(칙령 본문), 19-21→21-23, 22→24, 23-24→25, 25→26, 26-28→27-28 (MSG 문단 기준)",
             "KO[0]: 계보 이미 전체 포함 — 확정 EN과 일치 확인"]
fin_ko(7, k, vr, mr, splits, changes_k)

# ================= ch8 =================
p = EN[8]
p[4] = p[4].replace("from the family of Mahli, who was a descendant of Levi, the son of Israel",
                    "from the family of Mahli son of Levi, the son of Israel")
assert "Mahli son of Levi" in p[4], "ch8 EN[4] fix failed"
p[8] = ("It was a wild amount: 25 tons of silver, 100 silver vessels valued at three and "
        "three-quarter tons of gold, 20 gold bowls that weighed about eighteen and a half pounds, "
        "and 2 vessels made of a bright red copper that was as valuable as gold.")
assert "valued at three and three-quarter tons of gold" in p[8], "ch8 EN[8] fix failed"
vr = ["1-14", "1-14", "15-17", "15-17", "18-20", "21-22", "23", "24-27", "24-27",
      "28-29", "30", "31", "32-34", "35", "36"]
mr = ["1-14", "15-17", "18-20", "21-22", "23", "24-27", "28-29", "30", "31",
      "32-34", "35", "36"]
splits = [{"msg_range": "1-14", "paras": [0, 1]},
          {"msg_range": "15-17", "paras": [2, 3]},
          {"msg_range": "24-27", "paras": [7, 8]}]
changes = ["배지 수정: 14-18→18-20, 19-21→21-22, 21-22→23, 23-24→24-27, 24-27 유지, 27-28→28-29, 28-29→30, 30→31, 31-33→32-34, 34-35→35 (MSG 문단 기준)",
           "EN[4]: 'descendant of Levi'→'Mahli son of Levi' (MSG 8:18)",
           "EN[8]: 재물 목록 관계 복원 — '100 silver vessels valued at three and three-quarter tons of gold' (MSG 8:25-27)"]
fin_en(8, p, vr, mr, splits, changes)

k = KP[8]
k[4] = k[4].replace("레위의 증손이자 이스라엘의 손자인 말리 자손 중에서",
                    "레위의 아들이자 이스라엘의 손자인 말리의 자손 중에서")
assert "레위의 아들이자" in k[4], "ch8 KO[4] fix failed"
k[8] = ("양이 진짜 어마어마했는데, 은이 25톤, 금으로 치면 3.75톤어치인 은그릇 100개, "
        "18.5파운드 나가는 금그릇 20개, 그리고 금처럼 귀한 빛나는 놋그릇 2개였어.")
assert "3.75톤어치인 은그릇 100개" in k[8], "ch8 KO[8] fix failed"
changes_k = ["배지 수정: 1→1-14, 2-8→1-14, 9-10→15-17, 11-13→15-17, 14-18→18-20, 19-21→21-22, 22→23, 23-24→24-27, 25-26→24-27, 27-28→28-29, 29→30, 30→31, 31-33→32-34, 34-35→35 (MSG 문단 기준)",
             "KO[4]: '레위의 증손'→'레위의 아들' (MSG 8:18 — Mahli는 Levi의 아들)",
             "KO[8]: 확정 EN에 맞춰 재물 목록 관계 복원"]
fin_ko(8, k, vr, mr, splits, changes_k)

# ================= ch9 =================
p = EN[9]
p[0] = p[0].replace("And lowkey, our leaders were the ones who started this whole mess.",
                    "And our leaders were the ones who started this whole mess.")
assert "lowkey" not in p[0], "ch9 EN[0] fix failed"
vr = ["1-2", "3", "4-6", "6-7", "8-9", "10-12", "13-15"]
mr = ["1-2", "3", "4-6", "6-7", "8-9", "10-12", "13-15"]
splits = [{"msg_range": "6", "paras": [2, 3], "kind": "boundary_share",
           "note": "MSG 4-6과 6-7이 v6을 공유 — 인접 MSG 문단 경계 공유, split 아님"}]
changes = ["배지 수정: 1-3→1-2, 4-6→3, 4-6 유지, 7-8→6-7, 9-10→8-9, 11-13→10-12, 13-15 유지 (MSG 문단 기준)",
           "MSG 4-6과 6-7은 v6 공유 (인접 범위 경계 공유, split 아님) — splits[]에 boundary_share로 별도 표기",
           "EN[0]: 'lowkey' 삭제 순화"]
fin_en(9, p, vr, mr, splits, changes)

k = KP[9]
changes_k = ["배지 수정: 1-3→1-2, 4→3, 5-6→4-6, 7-8→6-7, 9-10→8-9, 11-13→10-12, 14-15→13-15 (MSG 문단 기준)",
             "MSG 4-6과 6-7은 v6 공유 — splits[]에 boundary_share로 별도 표기"]
fin_ko(9, k, vr, mr, splits, changes_k)

# ================= ch10 =================
p = EN[10]
p[5] = p[5].replace("telling all the exiles to get to Jerusalem, like, ASAP.",
                    "telling all the exiles to get to Jerusalem right away.")
assert "ASAP" not in p[5], "ch10 EN[5] fix failed"
p[9] = p[9].replace("But they also said, 'But dude, look how many of us there are!",
                    "But they also said, 'But look how many of us there are!")
assert "But dude" not in p[9], "ch10 EN[9] fix failed"
vr = ["1", "2-3", "4", "5", "6", "7-8", "9", "10-11", "12", "13-14", "15-17",
      "18-19", "18-19", "20", "21", "22", "23", "24", "24", "25", "25",
      "26", "27", "28", "29", "30", "31-32", "33", "34-37", "38-42", "43", "44"]
mr = ["1", "2-3", "4", "5", "6", "7-8", "9", "10-11", "12", "13-14", "15-17",
      "18-19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
      "30", "31-32", "33", "34-37", "38-42", "43", "44"]
splits = [{"msg_range": "18-19", "paras": [11, 12]},
          {"msg_range": "24", "paras": [17, 18]},
          {"msg_range": "25", "paras": [19, 20]}]
changes = ["배지 수정: 1-3→1, 4-7→2-3, 7-8→4, 9-10→5, 11-12→6, 13-14→7-8, 15-17→9, 18-20→10-11, 21→12, 22→13-14, "
           "23→15-17, 24→18-19(서두, split), 25→18-19(Jeshua 가문), 26→20, 27→21, 28→22, 29→23, 30→24(노래하는 자), "
           "31-32→24(문지기), 31-32→25(서두), 33→25(Parosh), 34-37→26, 34-37→27, 34-37→28, 34-37→29, "
           "38-42→30, 38-42→31-32, 38-42→33, 38-42→34-37 유지, 38-42 유지, 43 유지, 44 유지 (MSG 문단 기준)",
           "EN[5]: 'like, ASAP'→'right away'",
           "EN[9]: 'But dude'→'But' 순화"]
fin_en(10, p, vr, mr, splits, changes)

k = KP[10]
k[7] = k[7].replace('"님들, 신뢰를 깨버렸음.', '"여러분, 신뢰를 깨뜨리셨습니다.')
k[7] = k[7].replace("그분이 원하시는 대로 하셈.", "그분이 원하시는 대로 하십시오.")
assert "여러분, 신뢰를 깨뜨리셨습니다." in k[7], "ch10 KO[7] fix failed"
assert "하셈" not in k[7], "ch10 KO[7] fix failed 2"
k[9] = k[9].replace("근데 여기 사람 많은 거 보셈.", "근데 여기 사람 많은 거 보세요.")
assert "보세요." in k[9], "ch10 KO[9] fix failed"
changes_k = ["배지 수정: 1-3→1, 4-7→2-3, 8→4, 9-10→5, 11-12→6, 13-14→7-8, 15-17→9, 18-20→10-11, 21→12, 22→13-14, "
             "23→15-17, 24→18-19(서두, split), 25→18-19(Jeshua 가문), 26→20, 27→21, 28→22, 29→23, 30→24(노래하는 자), "
             "31→24(문지기), 32→25(서두), 33→25(Parosh), 34→26, 35→27, 36→28, 37→29, 38→30, 39→31-32, 40→33, "
             "41→34-37, 42→38-42, 43 유지, 44 유지 (MSG 문단 기준)",
             "KO[7]: '님들, 신뢰를 깨버렸음'→'여러분, 신뢰를 깨뜨리셨습니다', '하셈'→'하십시오' 순화",
             "KO[9]: '보셈'→'보세요' 순화"]
fin_ko(10, k, vr, mr, splits, changes_k)

# ---------- write ----------
import os
os.makedirs('/home/hatch/workspace/teenz-bible-review/fixes', exist_ok=True)
with open('/home/hatch/workspace/teenz-bible-review/fixes/en_Ezra.json', 'w') as f:
    json.dump([FE[c] for c in sorted(FE)], f, ensure_ascii=False, indent=1)
with open('/home/hatch/workspace/teenz-bible-review/fixes/ko_Ezra.json', 'w') as f:
    json.dump([FK[c] for c in sorted(FK)], f, ensure_ascii=False, indent=1)
print("wrote en_Ezra.json / ko_Ezra.json")
for c in sorted(FE):
    print(f"ch{c}: EN {len(FE[c]['paragraphs'])} paras / KO {len(FK[c]['paragraphs'])} paras")
