#!/usr/bin/env python3
"""Worker B2: SongOfSongs meaning audit fixes (MSG 2026-09-22 source).
Applies EN+KO edits, records 'changes' notes. Run once. All strings literal UTF-8."""
import json

R = '/home/hatch/workspace/teenz-bible-review'
en = json.load(open(f'{R}/fixes/en_SongOfSongs.json'))
ko = json.load(open(f'{R}/fixes/ko_SongOfSongs.json'))

def ch(d, n):
    return [x for x in d if x['chapter'] == n][0]

def note(d, n, s):
    ch(d, n).setdefault('changes', []).append(s)

def _norm(s):
    return s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')

def rep(lst, i, old_frag, new):
    tgt = _norm(lst[i])
    assert _norm(old_frag) in tgt, f'FRAG NOT FOUND ch-idx{i}: {old_frag[:70]}'
    # replace on normalized copy, then write back (keeps file's original quote style elsewhere)
    lst[i] = tgt.replace(_norm(old_frag), new, 1)

# ================= CH1 =================
c = ch(en, 1); p = c['paragraphs']
rep(p, 0, "The ultimate song, Solomon's banger of a song!",
    "The ultimate song — Solomon's greatest hit of all!")
rep(p, 1, "Your love hits different, way better than any drink.",
    "Your love is on another level, way better than any drink.")
rep(p, 2, "singing and making amazing memories.",
    "singing and making the best music.")
p[3] = ("Hey, girls of Jerusalem, I know I look a little weathered, but I'm still "
        "beautiful — sun-burnt like those desert tents of Kedar, yet soft like "
        "Solomon's Temple hangings. Don't look down on me because I'm dark; the sun "
        "did this to me. My brothers were jerks and sent me to work the fields all day, "
        "so I had to take care of the farm instead of myself.")
note(en, 1, "1:5-6 restored 'soft like Solomon's Temple hangings' + \"don't look down on me because I'm dark\"; "
     "1:4 'making great music' fixed (was 'making amazing memories'); 1:1 'banger'->'greatest hit'; 1:2-3 'hits different'->'on another level'")
k = ch(ko, 1); q = k['paragraphs']
rep(q, 2, "신나게 놀자.", "신나는 음악을 만들자.")
note(ko, 1, "1:4 '신나게 놀자'->'신나는 음악을 만들자' (MSG \"we'll make great music\")")

# ================= CH2 (restructure 8 -> 10 paras) =================
c = ch(en, 2)
c['paragraphs'] = [
 "I’m just a wildflower from the plains of Sharon, a regular lotus from the valley pools.",
 "He says, “A lotus blooming in a swamp of weeds—that’s you, my girl, compared to everyone else.”",
 "And my man? He’s like an apricot tree standing out in a forest of ordinary trees — he just stands out from all the other guys. All I want is to sit in his shade and soak up his delicious love. He brought me home for a festive meal, but honestly? His eyes were feasting on me!",
 "Oh! Give me something refreshing to eat — and quick! Apricots, raisins, anything! I’m about to faint with love! His left hand cradles my head, and his right arm wraps around my waist!",
 "Oh, let me warn you, sisters in Jerusalem — by the gazelles, yes, by all the wild deer: don’t wake love up, don’t stir it up, until the time is right and you’re ready.",
 "Oh! Do you hear that? It’s my love coming! Look! He’s jumping over mountains, leaping over hills. My man is like a graceful gazelle, a young stag full of energy. He’s right there, on tiptoe at the gate, all ears and eyes — ready! My lover is here, and he’s talking to me!",
 "He says, “Get up, my beautiful love, let’s go! Look around — winter is finally over, the rain is gone! Flowers are blooming everywhere. The whole world is like a choir, singing! The birds are filling the forest with their sweet songs. The lilacs are purple and fragrant, and the cherry trees are full of blossoms. So get up, my dear, my beautiful love — come with me! My shy dove, stop hiding. Come out so I can see your face and hear your voice. Your voice is so calming, and your face is truly stunning.”",
 "And then I’m like, “You gotta protect us from the foxes, the sneaky foxes trying to get into our flowering garden.”",
 "My love is mine and I’m his. He hangs out in our garden at night, enjoying the flowers, until dawn breathes its light and the night slips away.",
 "Turn to me, my love! Come like a gazelle, leap like a young stag over those beautiful mountains!",
]
c['verseRanges'] = ['1','2','3-4','5-6','7','8-10','11-14','15','16','17']
note(en, 2, "2:5-6 restored (apricots/raisins, faint with love, his arms around her); 2:7 warning restored (was dropped); "
     "2:16 restored 'until dawn breathes its light and night slips away'; 2:8-10 restored 'My lover is here, and he's talking to me'; "
     "badge fixes [3-7]->[3-4]/[5-6]/[7], [8-9]->[8-10], [10-14]->[11-14]; slang: lowkey/OMG/no cap/popping off removed")

k = ch(ko, 2)
k['paragraphs'] = [
 "나는 샤론 평야에 핀 그냥 들꽃이고, 골짜기의 수련 같은 평범한 여자애일 뿐이래.",
 "근데 오빠가 그러는 거임. “다른 여자애들은 그냥 잡초인데, 너는 그 속에서 피어난 수련 같아”라고.",
 "내 남친은 숲속에서 눈에 띄는 살구나무 같아. 다른 남자애들이랑은 차원이 다르지. 그냥 그 사람 그늘에 앉아서 달달한 사랑을 음미하고 싶어. 그 사람이 날 잔치에 데려갔는데, 다른 건 안 보고 나만 뚫어지게 쳐다보는 거 있지!",
 "아, 진짜 사랑에 취해서 쓰러질 것 같으니까 빨리 뭐 좀 줘! 살구든 건포도든 아무거나! 그 사람이 왼손으로 내 머리를 받쳐주고 오른손으로 내 허리를 감싸 안고 있었거든.",
 "예루살렘 여자들아, 내가 경고하는데, 들판의 노루와 사슴을 걸고 맹세해. 사랑이라는 감정은 억지로 깨우는 게 아니야. 때가 될 때까지, 너희가 진짜 준비될 때까지 기다려.",
 "와, 들려? 내 사랑하는 사람이 오는 소리야! 저기 봐봐! 산을 넘고 언덕을 뛰어다니면서 오고 있어. 내 남친은 우아한 가젤 같고, 힘 넘치는 젊은 사슴 같아. 저기 문 앞에서 까치발로 서서 귀 쫑긋 눈 땡글, 완전 준비하고 있네! 드디어 내 님이 와서 나한테 말을 거는 거야!",
 "“내 사랑, 내 예쁜아, 일어나! 나랑 같이 가자! 봐봐, 겨울은 이제 끝났고, 비도 그쳤어! 온 세상에 꽃이 피고, 온 세상이 합창단처럼 노래하고 있어. 새들이 숲에서 아름다운 노래를 부르고, 라일락은 보랏빛으로 향긋하고, 벚나무에는 꽃향기가 가득해. 그러니까 일어나, 내 사랑, 내 예쁜아! 나랑 가자! 부끄러워 숨어있지 말고, 이리 나와봐. 네 얼굴 좀 보여주고 목소리도 들려줘. 네 목소리는 너무 부드럽고, 네 얼굴은 정말 매혹적이야.”",
 "그래서 내가 말했지. “우리 꽃밭에 들어오려는 저 여우들, 저 못된 여우들로부터 우리를 지켜줘야 해.”",
 "내 사랑은 내 거고, 나는 그 사람 거야. 밤마다 우리 정원을 거닐면서 동이 트고 밤이 사라질 때까지 꽃을 감상한대.",
 "내 사랑, 나한테 돌아와 줘. 저 아름다운 산 위를 뛰어노는 가젤처럼, 어린 사슴처럼 빨리 와줘!",
]
k['verseRanges'] = ['1','2','3-4','5-6','7','8-10','11-14','15','16','17']
note(ko, 2, "badge 전면 정정 ([3-7]->[3-4]/[5-6]/[7], [8-9]->[8-10], [10-14]->[11-14], [15]->[15]/[16]/[17] 분리); "
     "2:16 '동이 트고 밤이 사라질 때까지' 복원; 슬랭 정리 (대박->와, 난리 났어->아름다운 노래, 진동을 해->향긋하고)")

# ================= CH3 =================
c = ch(en, 3)
c['title'] = "I Searched All Night for My Lost Love"
c['paragraphs'] = [
 "I was just tossing and turning all night, couldn’t sleep. I was missing my guy like crazy. It actually hurt that he wasn’t there. So I got up and started wandering around the city, checking every street and alley. I was desperate to find him! I looked everywhere, but he was nowhere. Then the night guards found me while they were on patrol. I asked them, ‘Have you guys seen the one I love?’ And you won’t believe it — right after I left them, I found him! I found my love. I just grabbed him and hugged him so tight, and I wasn’t letting go until I got him home again, safe and sound by the fire.",
 "So girls of Jerusalem, promise me this — swear it by the gazelles and the wild deer: don’t wake love up or stir it up until the time is right and you’re ready.",
 "Then I saw something wild — a cloud of dust rising out of the desert, with sweet smells and spicy perfume filling the air! It was Solomon’s carriage, carried and guarded by sixty soldiers, sixty of Israel’s finest — armed to the teeth, trained for battle, ready for anything, anytime. Solomon had this carriage built from fine Lebanon cedar, framed with silver and roofed with gold, with purple fabric cushions and the inside lined with tooled leather.",
 "Come on, girls of Jerusalem, you have to see this! Everyone in Zion, don’t miss out! It’s my king, my love, all dressed up and garlanded for his wedding. His heart is full, bursting with joy!",
]
c['verseRanges'] = ['1-4','5','6-10','11']
note(en, 3, "3:9-10 carriage description restored (cedar/silver/gold/purple cushions/tooled leather — was dropped); "
     "3:6-10 restored 'armed to the teeth, trained for battle, ready for anything, anytime'; 3:11 restored 'garlanded'; "
     "badge restructure [1-5]/[6-8]/[9-11] -> [1-4]/[5]/[6-10]/[11]; title clickbait caps toned down")

k = ch(ko, 3)
k['paragraphs'] = [
 "밤에 잠도 안 오고 뒤척이는데, 내 님이 너무 보고 싶은 거임. 없으니까 막 마음이 아프더라고. 그래서 벌떡 일어나서 온 동네를 다 돌아다녔지. 길거리랑 골목이랑 다 뒤지고 다녔어. 진짜 너무너무 보고 싶었거든! 근데 아무리 찾아도 없는 거야. 그러다가 순찰 돌던 경비 아저씨들이 날 발견했어. 내가 “혹시 제 사랑 못 보셨어요?” 하고 물어봤지. 근데 그 아저씨들 지나치자마자 바로 찾았어, 내 사랑을! 보자마자 꽉 껴안고 절대 안 놔줬지. 우리 집에 다시 데려와서, 화로 옆에 안전하게 둘 때까지 말이야.",
 "예루살렘 여자들아, 약속해줘. 가젤과 들사슴을 걸고 맹세해. 사랑은 때가 되기 전에는 억지로 깨우지 마.",
 "저기 사막에서부터 먼지 구름 일으키면서 오는 게 뭐지? 막 달콤하고 톡 쏘는 향기가 진동을 하는데? 저거 솔로몬 왕의 가마잖아! 이스라엘에서 제일 잘나가는 군인 육십 명이 호위하고 있대. 다들 완전 무장하고, 실전 훈련 받은 최정예래. 언제 어디서든 싸울 준비가 되어있는 거지. 솔로몬 왕이 레바논 백향목으로 특별히 만들게 한 가마인데, 프레임은 은이고 지붕은 금으로 만들었대. 쿠션은 보라색 천이고, 안쪽은 가죽으로 장식되어 있다더라.",
 "예루살렘 여자들아, 이리 와서 구경해봐! 시온의 딸들아, 이거 절대 놓치면 안 돼! 우리 왕, 내 사랑이 결혼식 때문에 쫙 빼입고 화관까지 썼어. 마음이 벅차서 기쁨이 터져나오고 있잖아!",
]
k['verseRanges'] = ['1-4','5','6-10','11']
note(ko, 3, "badge 정정 ([1-5]->[1-4], [6-8]->[5], [9-11]->[6-10]/[11]); 3:1-4 '화로 옆에' 복원 (MSG 'safe at home beside the fire')")

# ================= CH4 =================
c = ch(en, 4)
c['title'] = "He's Completely Captivated by Her Beauty"
note(en, 4, "title: 'Lowkey Obsessed'->'Completely Captivated' (slang 6-rule)")
# KO ch4 verified faithful; no changes.

# ================= CH5 =================
c = ch(en, 5)
c['title'] = "I Messed Up and Lost My Love"
p = c['paragraphs']
rep(p, 1, "Yo, let’s celebrate, everyone! Cheers to life and love!",
    "Hey everyone, let’s celebrate! Cheers to life and love!")
rep(p, 2, "I was totally knocked out, but my dream felt so real. Then I heard my guy knocking and calling for me!",
    "I was sound asleep, but in my dream I was wide awake. Then I heard my lover knocking and calling for me!")
rep(p, 3, "“Babe, let me in! You’re my everything. I’m out here freezing and soaking wet from the night.”",
    "“My dove, my dearest love, let me in! I’m out here soaked with the night dew, freezing and shivering.”")
rep(p, 5, "He’d gotten tired of waiting and bounced. My heart, like, actually broke.",
    "He’d gotten tired of waiting and left. My heart actually broke.")
rep(p, 8, "My man is lowkey glowing, he’s so healthy and radiant!",
    "My man is glowing with health — so radiant!")
rep(p, 8, "with the sickest black curls.",
    "with raven-black curls tumbling across his shoulders.")
rep(p, 8, "His eyes are like, soft and bright, but super deep, you know? Like you could get lost in them.",
    "His eyes are like doves, soft and bright, but deep-set and full of meaning, like wells of water.")
rep(p, 8, "his beard smells like fresh herbs.",
    "his beard smells like sage.")
rep(p, 8, "He’s tall and stands strong, like a huge tree.",
    "He stands tall like a cedar, strong and deep-rooted,")
rep(p, 8, "His body is like a work of art, so smooth and strong.",
    "His body is like a work of art, hard and smooth as ivory.")
rep(p, 8, "Everything about him is just... wow. He’s amazing.",
    "Everything about him delights me and thrills me through and through!")
rep(p, 9, "That’s my man, that’s my guy, my Jerusalem crew.",
    "That’s my lover, that’s my man, dear sisters in Jerusalem.")
note(en, 5, "5:2 restored MSG endearments (dove/dearest love) + 'soaked with the night dew, freezing and shivering'; "
     "5:10-16 restored 'raven-black curls', 'eyes like doves...like wells of water', 'sage', 'hard and smooth as ivory', "
     "'like a cedar, strong and deep-rooted', 'delights me and thrills me through and through'; "
     "slang: Yo/lowkey/sickest/bounced/'like, actually'/'Jerusalem crew' fixed; title clickbait toned down")

# ================= CH6 =================
c = ch(en, 6); p = c['paragraphs']
c['paragraphs'] = [
 p[0],
 p[1].replace("So, like, where did your boyfriend go", "So where did your boyfriend go"),
 "§He's In His Garden",
 "Oh, don’t even worry about it. My guy is already headed to his garden, just chilling among the flowers, checking out all the cool colors and shapes. I totally belong to my lover, and he totally belongs to me. He’s probably just gently touching all those awesome, fragrant flowers.",
 "§The Man's Praise",
 p[6], p[7], p[8],
 "There’s no one like her anywhere on earth — never has been, never will be. She’s a woman beyond compare.",
 p[10].replace("totally freaked out and admired her", "was amazed and admired her"),
 p[11], p[12],
 "§Carried Away",
 p[14], p[15],
 "§Dance, Shulammite!",
 p[17],
]
c['verseRanges'] = ['1','1','2-3','2-3','4','4','5','6-7','8','9','9','10','11-12','11-12','11-12','13','13']
note(en, 6, "6:8 rewritten to MSG ('There's no one like her...She's a woman beyond compare' — old text used KJV 'sixty queens and eighty concubines'); "
     "badge fixes [2]->[2-3], [3](header)->[4], [11]/[12]->[11-12]; merged split [2]+[3] back to MSG [2-3]; "
     "slang: 'like,' filler, 'freaked out'->'amazed'")

k = ch(ko, 6)
ko6_p5 = k['paragraphs'][5]  # MSG 4-7 content, split into [4]/[5]/[6-7]
part4 = ko6_p5.split("네 머리카락은")[0]
part57 = "네 머리카락은" + ko6_p5.split("네 머리카락은")[1]
part5 = part57.split("네 미소는")[0]
part67 = "네 미소는" + part57.split("네 미소는")[1]
k['paragraphs'] = [
 k['paragraphs'][0],
 k['paragraphs'][1],
 "§그는 자기 정원에 있어",
 k['paragraphs'][3],
 "§남자의 칭찬",
 part4, part5, part67,
 "진짜 이 세상에 그녀 같은 여자는 없어. 전에도 없었고, 앞으로도 없을 거야. 그녀는 비교할 수 없는 여자야.",
 "나의 비둘기는 완벽 그 자체고, 태어난 날처럼 순수하고 순결해. 그녀의 어머니는 기쁨 속에서 그녀를 안았지. 그녀를 보러 온 모든 사람들이 감탄하고 칭찬했어.",
 "모든 아버지와 어머니, 이웃과 친구들이 그녀를 축복하고 칭찬했지.",
 k['paragraphs'][7],
 "§휩쓸린 마음",
 "어느 날 나는 과수원을 거닐고 있었어. 봄기운을 찾아서 말이야. 막 터지려는 꽃봉오리를 찾고, 모든 것이 준비되고 익기를 기대하면서.",
 "그러다 나도 모르게 내 마음이 황홀경에 빠져서, 고상한 생각에 사로잡혀 버렸어.",
 "§춤춰라, 술람미 여인아!",
 "'춤춰라, 춤춰라, 사랑하는 술람미 여인아, 천사 같은 공주님아! 춤을 춰라, 우리가 네 우아한 모습을 눈에 담을 수 있도록! 모두가 술람미 여인이 사랑과 평화의 승리의 춤을 추는 것을 보고 싶어 해.'",
]
k['verseRanges'] = ['1','1','2-3','2-3','4','4','5','6-7','8','9','9','10','11-12','11-12','11-12','13','13']
note(ko, 6, "중복 문단 버그 수정 ('춤춰라' 6회 반복 제거); badge 전면 정정 ([2]->[2-3], [3]->[4], [4](8-9내용)->[8], [8]->[11-12], [9]->[13], 중복제거); "
     "6:8 MSG 기준 재작성 ('진짜 이 세상에 그녀 같은 여자는 없어...')")

# ================= CH7 =================
c = ch(en, 7)
c['title'] = "He's Head Over Heels and He Knows It"
p = c['paragraphs']
rep(p, 0, "Dang, you’re so fine from head to toe.",
    "Wow, you’re so beautiful from head to toe.")
rep(p, 0, "The way you move is straight-up queenly.",
    "The way you move is so queenly.")
rep(p, 0, "Your whole vibe just makes everyone turn their heads and pay attention.",
    "Your whole look just makes everyone turn their heads and pay attention.")
rep(p, 1, "C’mon, babe—let’s just get out of here and wander through the countryside. We can crash at some random little inn,",
    "Come on, my love — let’s just get out of here and wander through the countryside. We can sleep at some little roadside inn,")
rep(p, 2, "The smell of love is all around us, like we’re surrounded by this vibe of new life and growth.",
    "Love-apples drench us with their fragrance; new life and growth surround us everywhere.")
note(en, 7, "title 'Whipped'->'Head Over Heels' (slang); 7:13 restored 'Love-apples drench us with fragrance'; "
     "slang: Dang/straight-up/vibe/babe/crash fixed")
k = ch(ko, 7); q = k['paragraphs']
rep(q, 0, "움직임은 완전 여왕님 포스야.", "움직임은 정말 여왕처럼 우아해.")
rep(q, 0, "완전 여성미 대폭발!", "정말 여성미의 결정체야!")
note(ko, 7, "7:1-9 슬랭 정리 (여왕님 포스->여왕처럼 우아해, 여성미 대폭발->여성미의 결정체)")

# ================= CH8 =================
c = ch(en, 8)
c['title'] = "Love is Unstoppable"
p = c['paragraphs']
rep(p, 0, "I’d give you my special spiced wine to drink and kiss your cheeks.",
    "I’d give you my best wine to drink and kiss your cheeks.")
rep(p, 1, "But yo, a little PSA for all my girls in Jerusalem: Don’t try to force love or stir it up before it’s time. You gotta wait until it’s ripe and you’re actually ready.",
    "But listen, my girls in Jerusalem: don’t try to force love or stir it up before it’s time. You gotta wait until it’s ripe and you’re actually ready.")
rep(p, 3, "I woke you up under the apricot tree, right where your mom went into labor with you. Yeah, under that exact tree, she gave birth to you.",
    "I found you under the apricot tree and woke you up to love, right where your mom went into labor with you — under that very tree she gave birth to you.")
rep(p, 4, "Because love is as strong as death, and passion is as intense as the grave. It’s a blazing fire, a legit flame from God. No amount of water can quench love; no floods can sweep it away. If someone tried to buy love with all their money, they’d be totally laughed at.",
    "Because love is as strong as death, and passion is as intense as the grave. The fire of love stops at nothing — it sweeps everything before it. Flood waters can’t drown love; torrents of rain can’t put it out. Love can’t be bought and it can’t be sold — you won’t find it in any marketplace.")
rep(p, 5, "‘Our little sister, she hasn’t developed yet. What are we gonna do with her when guys start asking her out? She’s like a wall, so we’ll build a silver tower to protect her. She’s like a door, so we’ll board her up with cedar planks.’",
    "‘Our little sister hasn’t grown up yet. What are we going to do with her when guys start asking for her? She’s young and vulnerable, and we’ll protect her. If she’s a wall, we’ll top it with barbed wire. If she’s a door, we’ll barricade it.’")
rep(p, 6, "Well, dear brothers, I am a wall, but now my breasts are like towers.",
    "Well, dear brothers, I am a wall, and I’ve grown up — my breasts are full.")
rep(p, 7, "Solomon has a vineyard at Baal Hamon, and he rents it out to others. Each one has to bring in a thousand silver coins. But my own vineyard is all mine, and I’m in charge of it. You can have your thousand coins, Solomon, and let the renters keep their two hundred!",
    "Solomon may have huge vineyards in rich, fertile country, where he hires others to work the land. People would pay anything to get a share of that harvest. But my vineyard is all mine, and I’m keeping it to myself. You can keep your huge vineyards, Solomon — you and your greedy guests!")
rep(p, 8, "Hey you, chilling in the gardens, my friends are listening for your voice. Let me hear it too!",
    "Hey, lady of the gardens — my friends are here listening. Let me hear your voice too!")
note(en, 8, "8:5 restored 'I found you under the apricot tree and woke you up to love'; 8:6-7 rewritten to MSG (fire stops at nothing/can't be bought — KJV 'thousand coins/Baal Hamon/flame from God' removed); "
     "8:9 rewritten to MSG ('young and vulnerable...barbed wire/barricade' — KJV 'silver tower/cedar planks' removed); 8:10 'my breasts are full' (MSG); 8:13 restored 'lady of the gardens'; "
     "slang: yo/PSA/legit fixed; title 'No Cap' removed")

k = ch(ko, 8); q = k['paragraphs']
rep(q, 0, "거기서 내가 만든 향긋한 와인도 주고 볼에 뽀뽀도 해줄게.",
    "거기서 내 와인을 마시게 하고 볼에 뽀뽀도 해줄게.")
rep(q, 3, "내가 살구나무 아래서 오빠를 깨웠어.",
    "내가 살구나무 아래서 오빠를 찾았고, 사랑으로 깨웠어.")
rep(q, 4, "사랑은 죽음처럼 강하고, 질투는 지옥처럼 잔인하거든. 사랑은 진짜 활활 타오르는 불길 같아서, 그 어떤 것도 막을 수 없어. 홍수가 나도 그 사랑을 끌 수 없고, 강물이 넘쳐도 휩쓸어가지 못해. 누가 자기 전 재산을 다 준다고 해도 사랑이랑은 절대 못 바꾸지. 그랬다간 진짜 비웃음만 살걸.",
    "사랑은 죽음처럼 강하고, 열정은 지옥의 공포도 비웃어. 사랑의 불길은 어떤 것도 막지 못해. 모든 것을 휩쓸어버려. 홍수도 그 사랑을 끌 수 없고, 빗물이 넘쳐도 지울 수 없어. 사랑은 살 수도 팔 수도 없어. 시장에서는 절대 찾을 수 없는 거야.")
rep(q, 5, "'우리 막내 여동생은 아직 가슴도 없는데. 남자들이 걔한테 관심 보이면 어떡하지? 걔는 성벽 같으니까 우리가 은으로 망대를 쌓아서 지켜주자. 문 같으니까, 백향목으로 빗장을 질러서 막아주자.'",
    "'우리 막내 여동생은 아직 어려. 남자들이 관심을 보이면 어떡하지? 걔는 아직 어리고 연약해서 우리가 지켜줘야 해. 걔가 성벽 같으면 위에 철조망을 쳐주고, 문 같으면 빗장을 질러 막아주자.'")
rep(q, 6, "오빠들, 나 이제 성벽 맞는데, 내 가슴은 망대 같아. 그래서 내 사랑이 나를 볼 때, 그는 완전한 만족감을 얻을 거야.",
    "오빠들, 나는 성벽이 맞지만 이제 다 컸어. 그래서 내 사랑이 나를 보면 완전하게 만족할 거야.")
rep(q, 7, "솔로몬 왕이 바알하몬에 포도밭이 있었는데, 그걸 농부들한테 빌려줬대. 각자 거기서 은 천 개씩 바쳐야 했지. 근데 내 포도밭은 완전 내 거고, 내가 알아서 다 해. 솔로몬, 그 천 개 너나 가져. 농부들은 이백 개나 챙기라 그래!",
    "솔로몬 왕은 비옥한 땅에 어마어마한 포도밭이 있을지 몰라도, 일꾼들을 고용해서 농사를 짓지. 누구나 그 풍성한 수확에 끼고 싶어 하겠지. 근데 내 포도밭은 완전 내 거고, 나 혼자 간직할 거야. 솔로몬, 그 넓은 포도밭은 너나 가져. 너랑 네 탐욕스러운 손님들이나!")
rep(q, 8, "정원에 있는 아가씨! 내 친구들이 네 목소리를 듣고 싶어 해. 나도 듣게 해줘!",
    "정원의 아가씨야, 내 친구들이랑 같이 네 목소리를 듣고 싶어 해. 네 목소리를 들려줘!")
note(ko, 8, "8:5 '살구나무 아래서 찾았고, 사랑으로 깨웠어' 복원; 8:6-7 MSG 기준 재작성 (질투->열정, '살 수도 팔 수도 없어'); "
     "8:9 MSG 기준 재작성 (철조망/빗장); 8:10 '이제 다 컸어'; 8:11-12 MSG 기준 재작성 (바알하몬/천 개 제거); 8:13 '정원의 아가씨야' 복원")

json.dump(en, open(f'{R}/fixes/en_SongOfSongs.json', 'w'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{R}/fixes/ko_SongOfSongs.json', 'w'), ensure_ascii=False, indent=1)
print('OK')
