# -*- coding: utf-8 -*-
"""Build ch15-18 EN patch fragments. Run from /home/hatch/workspace/teenz-bible-review."""
import json, os

OUT = '/home/hatch/workspace/teenz-bible-review/fixes/parts'
os.makedirs(OUT, exist_ok=True)

# ---------------- Chapter 15 ----------------
p15 = [
 "§What Pollutes Your Life",
 "Some religious experts came from Jerusalem to complain about Jesus's crew: \"Why don't your disciples follow the tradition of doing the special ceremonial hand-washing before they eat?\"",
 "Jesus fired back, \"Why do you guys break God's actual commandments just to keep your own made-up traditions? God clearly says, 'Respect your father and mother,' and, 'Anyone who curses father or mother should be put to death.' But you weasel out of it by saying, 'Whatever I owed you, I've given to God instead.' That can hardly be called respecting a parent — you cancel God's command with your own rules.\"",
 "He pulled the crowd close and said, \"Listen and understand this: It's not the food you put into your mouth that makes you dirty or toxic. It's the garbage that comes out of your mouth — the lies, the trash-talk, the hate — that proves you're toxic on the inside.\"",
 "Jesus wasn't done. \"Frauds!\" Isaiah's prophecy about you hit the bull's-eye: \"These people put on a big show, saying all the right things — but their hearts are nowhere near Me. They act like they worship Me, but it's fake. They ditch God's actual commands and just teach whatever's trending.\"",
 "Later, the disciples came to Him: \"Uh, did You notice how upset the Pharisees were when You said that?\"",
 "Jesus just shrugged it off: \"Any tree my Father in heaven didn't plant is getting yanked out by the roots. Forget them — they're blind guides leading blind people. And when a blind person leads a blind person, they both end up in the ditch.\"",
 "Peter said, \"I don't get it. Put it in plain language.\"",
 "Jesus replied, \"You too? Are you being willfully stupid? Don't you get that whatever you swallow just works its way through your gut and out the other end? But what comes out of your mouth starts in your heart — that's where evil schemes, murders, adultery, sleeping around, theft, lies, and cussing all come from. That's what actually pollutes you. Eating with unwashed hands? That's neither here nor there.\"",
 "§A Mother Won't Take No for an Answer",
 "Jesus headed to the region of Tyre and Sidon. They'd hardly arrived when a Canaanite woman came down from the hills, pleading, \"Mercy, Master, Son of David! My daughter is cruelly tortured by an evil spirit!\"",
 "Jesus didn't answer her at all. The disciples came over and complained, \"She's driving us crazy — would you please just take care of her?\"",
 "Jesus told them, \"I've got my hands full dealing with the lost sheep of Israel.\"",
 "But the woman came right back, dropped to her knees in front of Jesus, and begged, \"Master, help me.\"",
 "He said, \"It's not right to take bread out of children's mouths and throw it to dogs.\"",
 "She was quick: \"You're right, Master. But even beggar dogs get scraps from the master's table.\"",
 "Jesus gave in. \"Woman, your faith is something else! What you want is what you get!\" Right then, her daughter became well.",
 "After Jesus returned, He walked along Lake Galilee, climbed a mountain, and took His place, ready for visitors. They came — tons of them — dragging along the paraplegic, the blind, the maimed, the mute, all sorts of people in need, and threw them down at Jesus's feet to see what He'd do. He healed every one of them. When the crowd saw mutes talking, cripples walking, and blind people seeing, they were blown away — everyone could see God was blazingly alive right there among them.",
 "But Jesus wasn't finished with them. He called His disciples over: \"I hurt for these people. They've been with Me for three days straight, and now they have nothing to eat. I can't send them away hungry — they'd probably collapse on the road.\"",
 "The disciples said, \"But we're in the middle of nowhere — where are we supposed to dig up enough food for all these people?\"",
 "Jesus asked, \"How much bread do you have?\" \"Seven loaves,\" they said, \"plus a few fish.\" Jesus told the crowd to sit down. He took the seven loaves and the fish, gave thanks, broke them apart, and handed them out. Everyone ate until they were stuffed. They collected seven huge baskets of leftovers. Over four thousand people ate their fill at that meal. After Jesus sent them home, He climbed into the boat and crossed over to the Magadan hills.",
]
r15 = ["1-2","1-2","3-6","10-11","7-9","12","13-14","15","16-20","21-22","21-22",
       "23","24","25","26","27","28","29-31","32","33","34-39"]
msg15 = ["1-2","1-2","3-9","10-11","3-9","12","13-14","15","16-20","21-22","21-22",
         "23","24","25","26","27","28","29-31","32","33","34-39"]
ch15 = {
 "chapter": 15,
 "title": "Fake Rules and a Savage Faith",
 "paragraphs": p15,
 "verseRanges": r15,
 "msg_ranges": msg15,
 "merges": [],
 "splits": [{"msg_range": "3-9", "paras": [2, 4],
             "note": "MSG 단일 문단(3-9)을 EN 가독성을 위해 3-6(코르반 전통 비판)과 7-9(이사야 인용)로 분리"}],
 "changes": [
   "15: None 배지였던 §헤더(인덱스 6→신규 9)에 뒤따르는 본문 배지 '21-22' 부여; 신규 §헤더 '§What Pollutes Your Life'(MSG 섹션 제목) 추가",
   "15: 12절과 13-14절 분리 — MSG 13-14절의 'Father가 심지 않은 나무는 뿌리째 뽑힌다' 누락 복원",
   "15: 15절과 16-20절 분리 — 악 목록에 'adultery, sleeping around'(MSG fornications) 누락 복원",
   "15: 23-27절 병합 해제 → 23(무시+제자 불평, '시험하려 했다'는 MSG에 없는 해석 삭제), 24(이스라엘 잃은 양), 25(무릎 꿇고 'Master, help me' 복원), 26(개 떡 비유) 분리",
   "15: 29-39절 병합 해제 → 29-31(산 위 치유 사역·'God was blazingly alive' 복원), 32(삼 일째 긍휼), 33(제자 질문), 34-39(일곱 바구니·4천 명 이상·Magadan 복원; 'men (plus families)'는 MSG에 없어 'Over four thousand people'로 정정)",
   "15: 21-22절에 MSG 지명 Tyre and Sidon 복원",
   "15: 3-6절에 MSG의 'Respect your father and mother' 직접 인용 복원",
 ],
 "confirmations_needed": [],
}

# ---------------- Chapter 16 ----------------
p16 = [
 "§Some Bad Yeast",
 "Some Pharisees and Sadducees teamed up to test Jesus again, pressing him to prove himself with a sign. He told them, \"You've got this saying: 'Red sky at night, sailor's delight; red sky at morning, sailors take warning.' You can read the weather just fine — so why can't you read the signs of the times? A wicked, faithless generation is always hunting for signs and wonders. The only sign you're getting is the Jonah sign.\" Then he spun around and walked away.",
 "On their way to the other side of the lake, the disciples discovered they'd forgotten to bring bread. In the middle of all that, Jesus said to them, \"Keep a sharp eye out for Pharisee-Sadducee yeast.\"",
 "Thinking he was calling them out for forgetting the bread, they started whispering about what to do. Jesus knew exactly what they were thinking: \"Why all these worried whispers about forgetting the bread? Baby believers! Haven't you caught on yet? Don't you remember the five loaves that fed five thousand — and how many baskets of leftovers you picked up? Or the seven loaves that fed four thousand — and how many baskets you collected? Haven't you realized yet that bread isn't the problem? The problem is the yeast — Pharisee-Sadducee yeast.\" Then it clicked: he wasn't talking about food at all. He was talking about their teaching.",
 "When Jesus arrived in the villages of Caesarea Philippi, he asked his disciples, \"What are people saying about who the Son of Man is?\"",
 "They replied, \"Some think he's John the Baptist, some say Elijah, others Jeremiah or one of the prophets.\"",
 "He pressed them: \"And what about you? Who do you say I am?\"",
 "Simon Peter spoke up: \"You're the Christ, the Messiah, the Son of the living God.\"",
 "Jesus said, \"God bless you, Simon, son of Jonah! You didn't get that answer from books or teachers — my Father in heaven let you in on the secret of who I really am. And now let me tell you who you really are: you are Peter, a rock. And on this rock I'm going to build my church — a church so full of energy that not even the gates of hell will be able to keep it out.\"",
 "And that's not all. I'm giving you the keys to God's kingdom — complete, free access, no more barriers between heaven and earth. A yes on earth is a yes in heaven; a no on earth is a no in heaven.",
 "Then Jesus swore the disciples to secrecy — they had to promise not to tell anyone that he was the Messiah.",
 "§You're Not in the Driver's Seat",
 "Then Jesus made it clear to his disciples: it was now necessary to go to Jerusalem, suffer at the hands of the religious leaders, be killed — and then on the third day be raised up alive. Peter grabbed him, protesting, \"Impossible, Master! That can never be!\"",
 "But Jesus didn't swerve. \"Peter, get out of my way. Satan, get lost. You have no idea how God works.\"",
 "Then Jesus went to work on his disciples. \"Anyone who intends to come with me has to let me lead. You're not in the driver's seat — I am. Don't run from suffering; embrace it. Follow me and I'll show you how. Self-help is no help at all. Self-sacrifice is the way — my way — to finding yourself, your true self. What kind of deal is it to get everything you want but lose yourself? What could you ever trade your soul for?\"",
 "\"Don't be in such a hurry to go into business for yourself. Before you know it, the Son of Man will arrive with all the splendor of his Father, backed by an army of angels. You'll get everything that's coming to you — a personal gift. This isn't some pie-in-the-sky someday thing. Some of you standing here are going to see it take place — see the Son of Man in kingdom glory.\"",
]
r16 = ["1-4","1-4","5-6","7-12","13","14","15","16","17-18","19","20",
       "21-22","21-22","23","24-26","27-28"]
msg16 = list(r16)
ch16 = {
 "chapter": 16,
 "title": "The Ultimate Question and a Brutal Wake-Up Call",
 "paragraphs": p16,
 "verseRanges": r16,
 "msg_ranges": msg16,
 "merges": [],
 "splits": [],
 "changes": [
   "16: 1-4절에 'the Jonah sign' + 'spun around and walked away' 누락 복원",
   "16: 5-12절 병합 해제 → 5-6(누룩 경고)과 7-12(오천/사천 기적 회상·'Then they got it: teaching' 복원) 분리; 'A tiny bit of it will infect your whole life'는 MSG에 없는 비유라 삭제",
   "16: 13-16절 병합 해제 → 13(가이사랴 빌립보 질문), 14(무리 대답), 15('너희는 나를 누구라 하느냐'), 16(베드로 고백) 분리",
   "16: 17-18절에 'God bless you, Simon, son of Jonah'·'not from books or teachers'·'who you really are' 복원",
   "16: 19절과 20절 분리 (열쇠 / 침묵 명령)",
   "16: 21-23절 병합 해제 → 21-22(예루살렘 수난 예고·베드로 만류)와 23('Peter, get out of my way. Satan, get lost. You have no idea how God works.' MSG 표현으로 정정) 분리",
   "16: 24절 대상 오류 수정 — 'to the crowd' → 'his disciples'(MSG: 'went to work on his disciples')",
   "16: 24-26절에 'You're not in the driver's seat — I am'·'Don't run from suffering; embrace it'·'Self-help is no help at all. Self-sacrifice is the way' 누락 복원",
   "16: 27-28절에 'You'll get everything that's coming to you — a personal gift'·'This isn't pie in the sky' 누락 복원",
   "16: 기존 24절 겹침 버그 수정 (구 verseRanges '24'와 '24-26' 중복 → 단일 24-26)",
   "16: §헤더 2개 추가 — '§Some Bad Yeast'(1-4), '§You're Not in the Driver's Seat'(21-22, MSG 제목 그대로)",
 ],
 "confirmations_needed": [],
}

# ---------------- Chapter 17 ----------------
p17 = [
 "§Sunlight Poured from His Face",
 "Six days later, Jesus took his three closest guys — Peter, James, and John — hiking up a massive mountain.",
 "Right in front of them, Jesus changed from the inside out. Sunlight poured from his face, and his clothes were filled with light. Then they realized Moses and Elijah — two Old Testament legends — were right there too, deep in conversation with him.",
 "Peter broke in: \"Master, this is an amazing moment! What if I built three memorials here on the mountain — one for you, one for Moses, one for Elijah?\"",
 "While he was still babbling, a light-radiant cloud wrapped around them, and a voice spoke from deep inside the cloud: \"This is my Son, marked by my love, the focus of my delight. Listen to him.\"",
 "When the disciples heard that voice, they fell flat on their faces, scared to death. But Jesus came over and touched them. \"Don't be afraid.\" When they opened their eyes and looked around, all they saw was Jesus — only Jesus.",
 "Coming down the mountain, Jesus swore them to secrecy. \"Don't breathe a word of what you've seen. After the Son of Man is raised from the dead, you're free to talk.\"",
 "Meanwhile the disciples were asking questions. \"Why do the religion scholars say that Elijah has to come first?\"",
 "Jesus answered, \"Elijah does come, and he gets everything ready. But I'm telling you — Elijah already came, and they didn't recognize him. They treated him like dirt — the same way they're about to treat the Son of Man.\" That's when the disciples realized he'd been talking about John the Baptist all along.",
 "§With a Mere Kernel of Faith",
 "At the bottom of the mountain, they were met by a crowd of waiting people. A man came out of the crowd, fell to his knees, and begged, \"Master, have mercy on my son. He goes out of his mind and suffers terribly — he falls into seizures and keeps getting pitched into the fire, other times into the river. I brought him to your disciples, but they couldn't do anything for him.\"",
 "Jesus said, \"What a generation! No sense of God! No focus to your lives! How many times do I have to go over these things? How much longer do I have to put up with this? Bring the boy here.\" He ordered the afflicting demon out — and it was out, gone. From that moment on, the boy was well.",
 "Later, when the disciples had Jesus off to themselves, they asked, \"Why couldn't we throw it out?\"",
 "\"Because you're not yet taking God seriously,\" Jesus said. \"Here's the simple truth: if you had a mere kernel of faith — a poppy seed, say — you could tell this mountain, 'Move!' and it would move. There is nothing you wouldn't be able to tackle.\"",
 "As they were regrouping in Galilee, Jesus told them, \"The Son of Man is about to be betrayed to some people who want nothing to do with God. They will murder him — and three days later he will be raised alive.\" The disciples were scared to death.",
 "When they arrived at Capernaum, the tax men came to Peter and asked, \"Does your teacher pay taxes?\"",
 "Peter said, \"Of course.\" But as soon as they were in the house, Jesus confronted him. \"Simon, what do you think? When a king levies taxes, who pays — his children or his subjects?\"",
 "He answered, \"His subjects.\" Jesus said, \"Then the children get off free, right? But so we don't upset them needlessly, go down to the lake, cast a hook, and pull in the first fish that bites. Open its mouth and you'll find a coin. Take it and give it to the tax men. It will be enough for both of us.\"",
]
r17 = ["1-3","1","2-3","4","5","6-8","9","10","11-13",
       "14-16","14-16","17-18","19","20","22-23","24","25","26-27"]
msg17 = list(r17)
ch17 = {
 "chapter": 17,
 "title": "The Mountaintop Transformation",
 "paragraphs": p17,
 "verseRanges": r17,
 "msg_ranges": msg17,
 "msg_skipped_verses": [21],
 "merges": [],
 "splits": [{"msg_range": "1-3", "paras": [1, 2],
             "note": "MSG 단일 문단(1-3)을 EN 가독성을 위해 1(산행)과 2-3(변화)으로 분리; §헤더는 두 조각과 배지 공유"}],
 "changes": [
   "17: 14-20절 병합 해제 + 순서 정정(MSG 순서: 14-16 → 17-18 → 19 → 20; 기존 EN은 22-27을 앞에 배치) → 14-16(불·물에 던져짐 복원), 17-18('What a generation! No sense of God!' 책망·즉시 치유 복원), 19(제자 질문), 20(겨자씨가 아닌 MSG 표현 'poppy seed'·'not yet taking God seriously' 복원) 분리",
   "17: 4-8절 병합 해제 → 4(세 장막 제안), 5(구름·음성 'marked by my love, focus of my delight' 복원), 6-8(엎드림·'Don't be afraid'·오직 예수) 분리",
   "17: 9-13절 병합 해제 → 9(비밀 유지), 10(엘리야 질문), 11-13(세례 요한 깨달음) 분리",
   "17: 22-27절 병합 해제 → 22-23(갈릴리 재결집·수난 예고), 24(성전세 질문), 25(자녀 vs 백성), 26-27(물고기 동전) 분리",
   "17: §헤더 2개 추가 — '§Sunlight Poured from His Face'(1-3), '§With a Mere Kernel of Faith'(14-16, MSG 제목 그대로)",
   "17: 21절은 MSG 원문 자체에 없음(raw 확인) — 커버리지 예외 처리",
 ],
 "confirmations_needed": [],
}

# ---------------- Chapter 18 ----------------
p18 = [
 "§Whoever Becomes Simple Again",
 "Around the same time, the disciples came to Jesus asking, \"Who gets the highest rank in God's kingdom?\"",
 "For an answer, Jesus called a little kid over and stood him right in the middle of the room. \"I'm telling you, once and for all: unless you return to square one and start over like children, you're not even going to get a look at the kingdom, let alone get in. Whoever becomes simple and elemental again, like this child, will rank high in God's kingdom. And here's more: when you welcome the childlike because of me, it's the same as welcoming me.\"",
 "\"But if you give these little ones a hard time — bullying them or taking advantage of their simple trust — you'll soon wish you hadn't. You'd be better off dropped in the middle of the lake with a millstone around your neck. Doom to the world for giving these God-believing kids a hard time! Hard times are inevitable, but you don't have to make it worse — and it's doomsday for you if you do.\"",
 "\"If your hand or your foot gets in the way of God, chop it off and throw it away. You're better off maimed or lame and alive than owning two hands and two feet and ending up godless in a furnace of eternal fire. And if your eye distracts you from God, pull it out and throw it away. You're better off one-eyed and alive than seeing perfectly from inside the fire of hell.\"",
 "\"Watch that you don't look down on a single one of these childlike believers. You realize, don't you, that their personal angels are constantly in touch with my Father in heaven?\"",
 "§Work It Out Between You",
 "\"Look at it this way: if someone has a hundred sheep and one of them wanders off, doesn't he leave the ninety-nine and go after the one? And if he finds it, isn't he way more thrilled over that one than over the ninety-nine that stayed put? Your Father in heaven feels the same way — he doesn't want to lose even one of these simple believers.\"",
 "\"If a fellow believer hurts you, go and tell him — work it out between the two of you. If he listens, you've made a friend. If he won't listen, take one or two others along so the witnesses keep things honest, and try again. If he still won't listen, tell the church. And if he won't listen to the church either, you'll have to start over from scratch — confront him with the need to turn around, and offer him God's forgiving love again.\"",
 "\"Take this most seriously: a yes on earth is a yes in heaven; a no on earth is a no in heaven. What you say to one another is eternal — I mean this. When two of you get together on anything at all on earth and make a prayer of it, my Father in heaven goes into action. And when two or three of you are together because of me, you can be sure that I'll be there.\"",
 "At that point Peter got up the nerve to ask, \"Master, how many times do I forgive a brother or sister who hurts me? Seven?\"",
 "Jesus replied, \"Seven! Hardly. Try seventy times seven. Stop keeping score.\"",
 "§A Story About Forgiveness",
 "\"God's kingdom is like a king who decided to square accounts with his servants. As he got under way, they brought him a servant who had run up a debt of a hundred thousand dollars. He couldn't pay up, so the king ordered the man — along with his wife, children, and goods — to be auctioned off at the slave market.\"",
 "\"The poor wretch threw himself at the king's feet and begged, 'Give me a chance and I'll pay it all back.' Touched by his plea, the king let him off — erasing the debt.\"",
 "\"The servant was no sooner out of the room when he came upon one of his fellow servants who owed him ten dollars. He seized him by the throat and demanded, 'Pay up. Now!'\"",
 "\"The poor wretch threw himself down and begged, 'Give me a chance and I'll pay it all back.' But he wouldn't do it — he had him arrested and put in jail until the debt was paid. When the other servants saw this going on, they were outraged and brought a detailed report to the king.\"",
 "\"The king summoned the man and said, 'You evil servant! I forgave your entire debt when you begged me for mercy. Shouldn't you be compelled to be merciful to your fellow servant who asked for mercy?' The king was furious and put the screws to the man until he paid back his entire debt. And that's exactly what my Father in heaven is going to do to each one of you who doesn't forgive — unconditionally — anyone who asks for mercy.\"",
]
r18 = ["1","1","2-5","6-7","8-9","10",
       "12-14","12-14","15-17","18-20","21","22",
       "23-25","23-25","26-27","28","29-31","32-35"]
msg18 = list(r18)
ch18 = {
 "chapter": 18,
 "title": "How to Handle Conflict and Forgive Like a Boss",
 "paragraphs": p18,
 "verseRanges": r18,
 "msg_ranges": msg18,
 "msg_skipped_verses": [11],
 "merges": [],
 "splits": [],
 "changes": [
   "18: 1-2절 분리 — '제자들이 다퉜다'는 MSG에 없는 해석을 'came to Jesus asking'으로 정정(MSG: 'the disciples came to Jesus asking')",
   "18: 2-9절 병합 해제 → 2-5('when you receive the childlike on my account, it's the same as receiving me' 누락 복원), 6-7(맷돌 경고·'Doom to the world' 전체 누락 복원), 8-9(손·발·눈 잘라내기 전체 누락 복원) 분리",
   "18: 10절 독립 분리 — 'their personal angels are constantly in touch with my Father in heaven' 누락 복원",
   "18: 10-13/14-20 범위 겹침 버그 수정 (구 '10-13'와 '14-20'이 14절 텍스트 중복 → 12-14·15-17·18-20으로 재정렬)",
   "18: 15-17절에 'start over from scratch, confront him with the need for repentance, and offer again God's forgiving love' 누락 복원",
   "18: 21-22절 분리 (베드로 질문 / seventy times seven)",
   "18: 23-35절 병합 해제 → 23-25(빚 'a hundred thousand dollars' MSG 금액으로 정정 — 기존 'millions of dollars' 수정), 26-27(애원·탕감), 28(멱살·'Pay up. Now!'), 29-31(투옥·다른 종들의 분노와 보고 복원), 32-35('put the screws to the man until he paid back his entire debt'·'anyone who asks for mercy' 복원) 분리",
   "18: §헤더 3개 추가 — '§Whoever Becomes Simple Again'(1), '§Work It Out Between You'(12-14), '§A Story About Forgiveness'(23-25, MSG 제목 그대로)",
   "18: 11절은 MSG 원문 자체에 없음(raw 확인) — 커버리지 예외 처리",
 ],
 "confirmations_needed": [],
}

for ch in (ch15, ch16, ch17, ch18):
    assert len(ch["paragraphs"]) == len(ch["verseRanges"]) == len(ch["msg_ranges"]), ch["chapter"]
    assert all(r is not None for r in ch["verseRanges"]), ch["chapter"]
    path = os.path.join(OUT, f'ch{ch["chapter"]}.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(ch, f, ensure_ascii=False, indent=2)
    # round-trip validation
    with open(path, encoding='utf-8') as f:
        back = json.load(f)
    assert back == ch, ch["chapter"]
    print(f'ch{ch["chapter"]}.json written + validated: {len(ch["paragraphs"])} paragraphs')
