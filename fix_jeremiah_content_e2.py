#!/usr/bin/env python3
"""Worker E2: Jeremiah real-omission restorations + ch49 badge realignment.

Fixes objective content loss / errors found by completeness check:
- truncated paragraphs (ch6:27, ch10:1, ch30:18, ch31:15)
- partial omissions (ch13:18-20, ch37:14-16 protest, ch50:33-34/44-46, ch52:30)
- number error (ch38:10 thirty->three)
- ch49 badge realignment to MSG units
"""
import json

REVIEW = '/home/hatch/workspace/teenz-bible-review'
en = json.load(open(f'{REVIEW}/fixes/en_Jeremiah.json', encoding='utf-8'))
ko = json.load(open(f'{REVIEW}/fixes/ko_Jeremiah.json', encoding='utf-8'))
en_by = {c['chapter']: c for c in en}
ko_by = {c['chapter']: c for c in ko}


def set_para(ch, lang, idx, new_text, note):
    d = en_by[ch] if lang == 'en' else ko_by[ch]
    d['paragraphs'][idx] = new_text
    d['changes'].append(note)


# ---- ch6 idx16 [27]: restore truncated MSG 27 ----
set_para(6, 'en', 16,
         "God gave me this job: \"I've made you the examiner of my people, to check out their lives and see what's really going on. They're a stubborn, hard-headed bunch, rotten to the core, every single one of them. I've cranked up the refining fire to max heat, but they're still just a lump of ore that won't change. It's pointless to keep trying. Nothing can burn the evil out of them. People will give up and call them 'slag,' tossed on the trash heap by me, their God.\"",
         "복원: MSG 27 후반부 누락 복원 (검사자 임무)")
set_para(6, 'ko', 16,
         "하나님이 나한테 이런 임무를 주셨어. \"내가 널 내 백성의 감별사로 세웠어. 그들의 삶을 살펴보고 진짜 속을 파악해봐. 걔네는 고집 세고 뻔뻔한 애들이야, 속까지 썩었어, 하나도 빠짐없이. 내가 제련 불을 최고로 올려봤는데도 걔네는 변하지 않는 쇳덩어리일 뿐이야. 더 해봤자 소용없어. 어떤 것도 걔네 안의 악을 태워 없앨 수 없어. 사람들은 포기하고 걔네를 '찌꺼기'라고 부를 거야. 나, 그들의 하나님이 쓰레기 더미에 던져버린 찌꺼기라고.\"",
         "복원: MSG 27 후반부 누락 복원 (KO)")

# ---- ch10 idx0 [1]: restore truncated MSG 1 ----
set_para(10, 'en', 0,
         "Yo, Israel, listen up! God's got a message for you, so pay attention. Don't copy the godless nations. Don't be impressed by their glamour and glitz, no matter how impressed they are with themselves. Their religion is nothing but smoke. An idol is just a tree chopped down and shaped by a woodsman's ax. They decorate it with tinsel and ornaments, use hammer and nails to keep it standing straight. It's like a scarecrow in a field\u2014can't talk! It's deadwood that has to be carried\u2014can't walk! Don't be impressed by that junk. It's useless, can't do good or evil.",
         "복원: MSG 1 우상 단락 누락 복원")
set_para(10, 'ko', 0,
         "이스라엘 백성들아, 주목! 하나님이 너희한테 할 말 있대. 잘 들어봐. 하나님 없는 나라들 따라 하지 마. 걔네가 아무리 자기들한테 반해도, 그 화려함이랑 반짝이에 감동받지 마. 걔네 종교는 그냥 연기일 뿐이야. 우상이라는 건 나무 베어다가 목수가 도끼로 깎아 만든 거야. 반짝이랑 장식으로 꾸미고, 망치랑 못으로 똑바로 세워놓지. 밭에 세워둔 허수아비 같은 거야\u2014말도 못 해! 들어서 옮겨야 하는 고목이야\u2014걷지도 못 해! 그런 쓰레기에 감동받지 마. 쓸모없어, 선도 악도 못 행해.",
         "복원: MSG 1 우상 단락 누락 복원 (KO)")

# ---- ch13 idx9 [18-20]: prepend missing king/queen-mother + Negev ----
e13 = en_by[13]; k13 = ko_by[13]
e13['paragraphs'][9] = ("Tell the king and the queen-mother, \"Get down off your high horses. Your dazzling crowns are about to tumble off your heads.\" The villages in the Negev will be surrounded, everyone trapped, and Judah will be dragged off to exile, the whole country wiped out. " + e13['paragraphs'][9])
e13['changes'].append("복원: MSG 18-20 왕/대비/네게브 누락 복원")
k13['paragraphs'][9] = ("왕이랑 대비한테 전해. \"그 잘난 체하는 거 그만 내려와. 너희 화려한 왕관이 곧 머리에서 떨어질 거야.\" 네게브 지방 마을들은 포위당해서 아무도 못 빠져나가고, 유다는 끌려가서 온 나라가 초토화될 거야. " + k13['paragraphs'][9])
k13['changes'].append("복원: MSG 18-20 왕/대비/네게브 누락 복원 (KO)")

# ---- ch30 idx9 [18]: restore truncated MSG 18 ----
set_para(30, 'en', 9,
         "Again, God's message: \"I'll turn things around for Jacob. I'll come in with compassion and rebuild homes. The town will be rebuilt on its old foundations; the mansions will be splendid again. Thanksgivings will pour out of the windows; laughter will spill through the doors. Things will get better and better. Depression days are over. They'll thrive, they'll flourish. The days of contempt will be over. They'll look forward to having children again, to being a community I'm proud of. I'll punish anyone who hurts them, and their prince will come from their own people. One of their own will be their leader. Their ruler will come from their own ranks. I'll give him free and easy access to me. Would anyone dare to do that on their own, to come into my presence uninvited?\" That's God's decree.",
         "복원: MSG 18 후반부 누락 복원")
set_para(30, 'ko', 9,
         "다시 한번, 하나님의 메시지임: \"내가 야곱의 운명을 바꿔줄 거야. 긍휼히 여겨서 집들을 다시 세워줄 거고. 성읍은 옛터 위에 다시 세워지고, 대궐도 다시 화려해질 거야. 창문으로는 감사가 넘쳐나고, 문으로는 웃음이 새어나올 거야. 점점 좋아질 거야. 우울한 날들은 끝났어. 걔네는 번성하고 형통할 거야. 멸시받던 날들도 끝이야. 다시 아이 낳는 걸 기대하고, 내가 자랑스러워하는 공동체가 될 거야. 걔네를 해치는 놈은 내가 응징할 거고, 걔네 지도자는 걔네 중에서 나올 거야. 자기 백성 중 한 사람이 지도자가 될 거야. 통치자도 자기들 중에서 나올 거고. 내가 걔한테는 자유롭게 내 앞에 나아올 수 있게 해줄 거야. 누가 감히 자기 맘대로, 초대받지도 않고 내 앞에 나아오겠어?\" 하나님의 칙령이야.",
         "복원: MSG 18 후반부 누락 복원 (KO)")

# ---- ch31 idx9 [15]: restore truncated MSG 15 ----
set_para(31, 'en', 9,
         "Again, God's Message: \"Listen to this! Laments coming out of Ramah, wild and bitter weeping. It's Rachel weeping for her children, Rachel refusing to be comforted. Her children are gone, gone\u2014long gone into exile.\" But God says, \"Stop your constant weeping, hold back your tears. You'll get paid for your grief work.\" That's God's decree. \"They'll be coming back home! There's hope for your children.\" That's God's decree.",
         "복원: MSG 15 라헬 애곡 누락 복원")
set_para(31, 'ko', 9,
         "또 하나님의 메시지야. \"이거 들어봐! 라마에서 애곡이 터져나오고 있어, 처절하고 쓰라린 울음이야. 라헬이 자기 자식들 때문에 울고 있어, 위로도 거부하면서. 자식들은 갔어, 갔어\u2014먼 곳으로 끌려갔어.\" 근데 하나님이 말씀하셔. \"그만 울어, 눈물을 거둬들여. 네 수고한 만큼 품삯을 받을 거야.\" 하나님의 칙령이야. \"걔네가 집으로 돌아올 거야! 네 자식들한테 희망이 있어.\" 하나님의 칙령이야.",
         "복원: MSG 15 라헬 애곡 누락 복원 (KO)")

# ---- ch38 idx7 [10]: thirty -> three ----
e38 = en_by[38]; k38 = ko_by[38]
e38['paragraphs'][7] = e38['paragraphs'][7].replace("Take thirty men", "Take three men")
e38['changes'].append("오류 수정: thirty→three (MSG 38:10)")
k38['paragraphs'][7] = k38['paragraphs'][7].replace("부하 30명", "부하 3명")
k38['changes'].append("오류 수정: 30명→3명 (MSG 38:10, KO)")
# ---- ch38 idx8 [11-12]: restore 'three' ----
e38['paragraphs'][8] = e38['paragraphs'][8].replace("Ebed-melek took the men", "Ebed-melek took three men")
e38['changes'].append("복원: 'three men' (MSG 38:11)")
k38['paragraphs'][8] = k38['paragraphs'][8].replace("에벳멜렉은 부하 30명을 데리고", "에벳멜렉은 부하 3명을 데리고")
k38['changes'].append("복원: '3명' (MSG 38:11, KO)")

# ---- ch37 idx6 [14-16]: restore Jeremiah's protest ----
e37 = en_by[37]; k37 = ko_by[37]
e37['paragraphs'][6] = ("\"That's a lie,\" Jeremiah protested. \"I wouldn't even think of deserting to the Babylonians.\" " + e37['paragraphs'][6])
e37['changes'].append("복원: MSG 37:14 예레미야 항변 누락 복원")
k37['paragraphs'][6] = ("\"거짓말이야!\" 예레미야가 항변했어. \"나 바빌론 편으로 넘어갈 생각도 안 했거든?\" " + k37['paragraphs'][6])
k37['changes'].append("복원: MSG 37:14 예레미야 항변 누락 복원 (KO)")

# ---- ch50 idx15 [33-38]: prepend MSG 33-34 first half ----
e50 = en_by[50]; k50 = ko_by[50]
e50['paragraphs'][15] = ("\"And here's more from God-of-the-Angel-Armies: The people of Israel are beaten down, the people of Judah along with them. Their oppressors have them in a stranglehold. They won't let go. But the Rescuer is strong: God-of-the-Angel-Armies. Yes, I will take their side, I'll come to their rescue. I'll bring peace to their land, but rough up the people of Babylon.\" " + e50['paragraphs'][15])
e50['changes'].append("복원: MSG 50:33-34 전반부(구원자) 누락 복원")
k50['paragraphs'][15] = ("\"그리고 만군의 하나님으로부터 또 있어. 이스라엘 백성은 짓밟혔고, 유다 백성도 마찬가지야. 압제자들이 걔네를 꽉 틀어쥐고 놓지를 않아. 근데 구원자는 강해. 만군의 하나님이야. 그래, 내가 걔네 편에 설 거야, 구하러 올 거야. 걔네 땅에는 평화를 주지만, 바빌론 사람들은 혼내줄 거야.\" " + k50['paragraphs'][15])
k50['changes'].append("복원: MSG 50:33-34 전반부(구원자) 누락 복원 (KO)")

# ---- ch50 idx19 [44-46]: prepend MSG 44-45 ----
e50['paragraphs'][19] = ("\"And now watch this: Like a lion coming up from the thick jungle of the Jordan, looking for prey in the mountain pastures, I'll take over and pounce. I'll pick the best of the flock\u2014and who's going to stop me? All the so-called shepherds are helpless against me.\" So, listen to this plan that God has worked out against Babylon, the blueprint of what he's prepared for dealing with Chaldea: " + e50['paragraphs'][19])
e50['changes'].append("복원: MSG 50:44-45 전반부(사자 비유/계획) 누락 복원")
k50['paragraphs'][19] = ("\"자, 이제 봐봐. 요단 강가의 울창한 정글에서 올라오는 사자처럼, 산 초원에서 먹이를 찾는 것처럼, 내가 덮쳐서 낚아챌 거야. 양 떼 중에 제일 좋은 걸로 골라잡을 거야\u2014누가 막겠어? 자칭 목자들이라는 놈들은 내 앞에서 무력해.\" 그러니까 하나님이 바빌론을 상대로 세운 이 계획, 갈대아를 처리하려고 준비한 청사진을 들어봐. " + k50['paragraphs'][19])
k50['changes'].append("복원: MSG 50:44-45 전반부(사자 비유/계획) 누락 복원 (KO)")

# ---- ch52 idx13 [30]: restore total 4,600; clarify Nebuchadnezzar's year (EN) ----
e52 = en_by[52]; k52 = ko_by[52]
e52['paragraphs'][13] = "Then in Nebuchadnezzar's twenty-third year, his chief deputy Nebuzaradan took 745 more people from Judah. The total number of exiles was 4,600."
e52['changes'].append("복원: MSG 52:30 총 4,600명 누락 복원 + 연도 주체 명확화")
k52['paragraphs'][13] = "느부갓네살의 23년에는 경호대장 느부사라단이 유다 사람 745명을 또 잡아갔어. 끌려간 사람 총합은 4,600명이었대."
k52['changes'].append("복원: MSG 52:30 총 4,600명 누락 복원 (KO)")

# ---- ch49: realign badges to MSG units ----
ch49_badges = ['1-6', '1-6', '7-11', '7-11', '12-13', '14', '15-16', '17', '18',
               '19', '20-22', '20-22', '23-27', '23-27', '28-33', '28-33',
               '34-39', '34-39']
for d in (en_by[49], ko_by[49]):
    assert len(d['paragraphs']) == 18, len(d['paragraphs'])
    d['verseRanges'] = list(ch49_badges)
    d['msg_ranges'] = list(ch49_badges)
    d['changes'].append("배지 재조정: MSG 문단 단위([1-6],[7-11],[12-13],[14],[15-16],[17],[18],[19],[20-22],[23-27],[28-33],[34-39])에 맞춤")
# rebuild splits for ch49
from validate_translation import expand
for d in (en_by[49], ko_by[49]):
    vrs = d['verseRanges']; n = len(vrs)
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

json.dump(en, open(f'{REVIEW}/fixes/en_Jeremiah.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Jeremiah.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('restorations applied')
