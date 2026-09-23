#!/usr/bin/env python3
"""Ephesians spec — built 2026-09-22 from MSG cache msg_Ephesians.txt.

MSG structure:
  ch1: 1-2, 3-6, 7-10, 11-12, 13-14, 15-19, 20-23 (7)
  ch2: 1-6, 7-10, 11-13, 14-15, 16-18, 19-22 (6)
  ch3: 1-3, 4-6, 7-8, 8-10, 11-13, 14-19, 20-21 (7)
  ch4: 1-3, 4-6, 7-13, 14-16, 17-19, 20-24, 25, 26-27, 28, 29, 30, 31-32 (12)
  ch5: 1-2, 3-4, 5, 6-7, 8-10, 11-16, 17, 18-20, 21, 22-24, 25-28, 29-33 (12)
  ch6: 1-3, 4, 5-8, 9, 10-12, 13-18, 19-20, 21-22, 23-24 (9)

KO 베이스는 이미 MSG 구조로 정렬되어 있음 (EN이 뒤처짐). EN을 MSG/KO에 맞춤.
"""
BOOK = 'Ephesians'
SLUG = 'Ephesians'

CHAPTERS = {
    1: {
        'en_ops': [
            ('keep', 1),
            ('new', '3-6', '§The God of Glory'),
            ('keep', 2),
            ('keep', 3),
            ('keep', 4),
            ('keep', 5),
            ('keep', 6),
            ('keep', 7),
        ],
        'ko_title': '에베소서 1장',
        'ko_ops': [
            ('keep', 1),
            ('new', '§영광의 하나님'),
            ('keep', 3),
            ('keep', 4),
            ('keep', 5),
            ('keep', 6),
            ('keep', 7),
            ('keep', 8),
        ],
        'changes': [
            'EN: null 헤더 §Spiritual Blessings 제거, MSG 소제목 §The God of Glory를 3-6 앞으로 이동',
            'KO: null 헤더 §영적 축복 제거, §영광의 하나님에 배지 3-6 부여',
            'EN/KO 모두 MSG 전 절 커버 확인됨 — 배지 수정·복원 없음',
        ],
    },
    2: {
        'en_ops': [
            ('new', '1-6', '§He Tore Down the Wall'),
            ('new', '1-6',
             "Hey, remember not too long ago when you were basically a zombie, just stuck in a loop of messing up? "
             "You were letting the world, which is totally clueless, tell you how to live. It was like you were "
             "breathing in toxic doubt and breathing out straight-up rebellion. Let's be real, we were all on that "
             "same struggle bus, just doing whatever we wanted, whenever we wanted. It's kinda wild God didn't just "
             "get fed up and delete us all. But instead, God, who's loaded with mercy and has this insane love for "
             "us, just pulled us into a huge hug. He took our dead-end lives and gave us an amazing change in "
             "Christ. And here's the thing—He did it all himself. We didn't do a thing to help! Then He gave us "
             "the ultimate upgrade, raising us up and seating us with Jesus in the best spot in heaven."),
            ('new', '7-10',
             "Now, God has us exactly where He wants us. He's got all the time in this world and the next to just "
             "shower us with non-stop kindness and grace because of Jesus. Saving us was 100% his idea and all his "
             "work. All we have to do is trust him to handle it. It's a free gift, from start to finish! We're not "
             "the main characters here. If we were, we'd probably be flexing on everyone about how we saved "
             "ourselves. But nah, we don't make or save ourselves. God does it all. He's crafting each of us "
             "through Christ to team up with him on the awesome stuff he's already planned for us to do — work we "
             "had better be doing."),
            ('new', '11-13',
             "But don't get it twisted and start taking this for granted. It feels like just yesterday you were on "
             "the outside looking in, with no clue about God's ways. You didn't know the first thing about how God "
             "operates, and you'd probably never even heard of Christ. You were totally in the dark about all the "
             "cool history and promises God made with his people, and you had no clue what God was doing in the "
             "wider world. But now, because of what Christ did—dying on the cross—you've gone from being totally "
             "out of the loop to having an all-access pass."),
            ('keep', 5, '14-15'),
            ('keep', 6, '16-18'),
            ('new', '19-22',
             "So, it's pretty simple, right? You're not homeless wanderers anymore. This kingdom of faith is your "
             "home turf now. You're not strangers or outcasts. You belong here, and you've got every right to be "
             "called a Christian. God is building a new house, and he's using all of us—no matter our backstory—to "
             "build it. He used the apostles and prophets as the foundation. Now he's using you, fitting you in "
             "brick by brick, stone by stone, with Christ Jesus as the main cornerstone holding everything "
             "together. We can see it coming together day by day—a holy temple built by God, with all of us as a "
             "part of it, a place where God can chill and feel right at home."),
        ],
        'ko_title': '에베소서 2장',
        'ko_ops': [
            ('new', '§예수님이 벽을 부숴버리심'),
            ('keep', 2),
            ('new',
             "지금도 하나님은 우리를 자기가 원하는 곳에 두시고, 이 세상이든 저 세상이든 예수님 안에서 은혜랑 사랑을 "
             "계속 부어주고 계심. 구원은 전부 하나님 아이디어고, 하나님이 다 하신 일임. 우리가 할 일은 그냥 하나님이 "
             "그 일을 하시도록 믿는 것뿐이야. 구원은 처음부터 끝까지 하나님의 선물인 거야! 주인공은 우리가 아님. "
             "만약 우리가 주인공이었으면, 우리가 다 했다고 여기저기 자랑하고 다녔을걸! 근데 아니거든. 우리는 우리 "
             "자신을 만들 수도, 구할 수도 없음. 만들고 구하는 건 다 하나님이 하시는 일이야. 하나님이 예수님을 통해서 "
             "우리 한 명 한 명을 만드셨어. 왜 그렇게 하셨냐면, 자기가 하시는 일, 그러니까 우리를 위해 준비해놓은 착한 "
             "일에 우리도 같이 참여하게 하려고 그러신 거래. 우리가 꼭 해야 할 일이야."),
            ('keep', 4),
            ('keep', 5),
            ('keep', 6),
            ('keep', 7),
        ],
        'splits': [],
        'merges': [
            {'para': 1, 'msg_range': '1-6', 'base_paras': [1, 2],
             'note': '기존 EN의 1-3/4-5 두 문단을 MSG 구조(1-6 한 문단)로 통합 — MSG 원문 그대로 복원'},
        ],
        'confirmations': [
            'ch2: 기존 EN 1-3/4-5 분할을 MSG 1-6 단일 문단으로 통합 (base_paras 1,2) — MSG 원문 구조와 일치함을 컨펌 필요',
        ],
        'changes': [
            'EN: 기존 1-3/4-5 분할을 MSG 구조(1-6 한 문단)로 병합 — KO와 parity',
            'EN 배지 수정: 13-15→14-15, 16-17→16-18, 18-22→19-22',
            'EN: null 헤더 §Made Alive in Christ → MSG 소제목 §He Tore Down the Wall (1-6 앞으로)',
            'EN 7-10 복원: "in this world and the next", "work we had better be doing"',
            'EN 11-13 복원: "hadn\'t a clue about what God was doing in the world at large"',
            'EN 19-22 복원: "brick by brick, stone by stone"',
            'KO: null 헤더 §그리스도 안에서 살아나다 제거, "예수님이 벽을 부숴버리심" → §예수님이 벽을 부숴버리심 (배지 1-6)',
            'KO 7-10 복원: "work we had better be doing" ("우리가 꼭 해야 할 일이야")',
        ],
    },
    3: {
        'en_ops': [
            ('new', '1-3', '§The Secret Plan of God'),
            ('keep', 1, '1-3'),
            ('keep', 2),
            ('new', '7-8',
             "This is my life's work now — helping people understand and respond to this message. It came as a sheer "
             "gift to me, a total surprise, God handling all the details. When it came to presenting the message to "
             "people who had zero background in God's way, I was the least qualified Christian available. God made "
             "sure I was equipped, but trust me, it had nothing to do with my natural abilities."),
            ('new', '8-10',
             "And so here I am, preaching and writing about things that are way over my head — the inexhaustible "
             "riches and generosity of Christ. My task is to bring out into the open and make plain what God, who "
             "created all this in the first place, has been doing in secret and behind the scenes all along. "
             "Through followers of Jesus like you guys gathered in churches, this extraordinary plan of God is "
             "becoming known and talked about even among the angels!"),
            ('keep', 4, '11-13'),
            ('new', '14-19',
             "So, I'm on my knees, praying to the Father, this magnificent Father who parcels out all heaven and "
             "earth. I'm asking him to strengthen you by his Spirit — not a brute strength but a glorious inner "
             "strength — so that Christ can really live in you as you open the door and invite him in. I pray that "
             "with both feet planted firmly on love, you'll be able to take in, together with all followers of "
             "Jesus, the extravagant dimensions of Christ's love. Reach out and experience the breadth! Test its "
             "length! Plumb the depths! Rise to the heights! Live full lives, full in the fullness of God."),
            ('new', '20-21',
             "And get this: God can do anything, you know — far more than you could ever imagine or guess or "
             "request in your wildest dreams! He does it not by pushing us around but by working within us, his "
             "Spirit deeply and gently within us. Glory to God in the church! Glory to God in the Messiah, in "
             "Jesus! Glory down all the generations! Glory through all millennia! Oh, yes!"),
        ],
        'ko_title': '에베소서 3장',
        'ko_ops': [
            ('new', '§하나님의 비밀 계획'),
            ('keep', 2),
            ('keep', 3),
            ('keep', 4),
            ('keep', 5),
            ('keep', 6),
            ('keep', 7),
            ('keep', 8),
        ],
        'splits': [
            {'msg_range': '8', 'paras': [3, 4],
             'note': 'MSG 8절이 7-8과 8-10 문단에 걸쳐 있음 (MSG 원문 구조 그대로)'},
        ],
        'changes': [
            'EN: 기존 7-13 병합 문단을 MSG 구조(7-8, 8-10)로 재분할 — 11-13은 기존 para 유지',
            'EN 배지 수정: 1-4→1-3, 11-12→11-13',
            'EN: null 헤더 §God\'s Big Plan → MSG 소제목 §The Secret Plan of God',
            'EN 14-19 복원: "as you open the door and invite him in", "together with all followers of Jesus"',
            'EN 20-21 복원: 4연속 영광송 전체 ("Glory to God in the church! ... Oh, yes!")',
            'KO: null 헤더 §하나님의 큰 계획 제거, "하나님의 구원 비밀, 완전 진짜 대단한" → §하나님의 비밀 계획 (배지 1-3)',
            'KO는 MSG 전 절 커버 확인됨 — 추가 복원 없음',
        ],
    },
    4: {
        'en_ops': [
            ('new', '1-3', '§To Be Mature'),
            ('new', '1-3',
             "Alright, listen up. In light of all this, here's what I want you to do. While I'm locked up here, a "
             "prisoner for the Master, I want you to get out there and walk — better yet, run! — on the road God "
             "called you to travel. I don't want any of you sitting around on your hands. I don't want anyone "
             "strolling off down some path that goes nowhere. And mark this: do it with humility and discipline — "
             "not in fits and starts, but steadily — pouring yourselves out for each other in acts of love, alert "
             "at noticing differences and quick at mending fences."),
            ('new', '4-6',
             "You were all called to travel on the same road and in the same direction, so stay together, both "
             "outwardly and inwardly. You have one Master, one faith, one baptism, one God and Father of all, who "
             "rules over all, works through all, and is present in all. Everything you are and think and do is "
             "permeated with Oneness."),
            ('new', '7-13',
             "But that doesn't mean you have to be clones. Out of the generosity of Christ, each of us is given his "
             "own gift. The text for this is: He climbed the high mountain, he captured the enemy and seized the "
             "plunder, he handed it all out in gifts to the people. Is it not true that the One who climbed up also "
             "climbed down, down to the valley of earth? And the One who climbed down is the One who climbed back "
             "up, up to highest heaven. He handed out gifts above and below, filled heaven with his gifts, filled "
             "earth with his gifts. He handed out gifts of apostle, prophet, evangelist, and pastor-teacher to "
             "train Christ's followers in skilled servant work, working within Christ's body, the church, until "
             "we're all moving rhythmically and easily with each other, efficient and graceful in response to God's "
             "Son — fully mature adults, fully developed within and without, fully alive like Christ."),
            ('new', '14-16',
             "No prolonged infancies among us, please. We'll not tolerate babes in the woods, small children who "
             "are easy prey for predators. God wants us to grow up, to know the whole truth and tell it in love — "
             "like Christ in everything. We take our lead from Christ, who is the source of everything we do. He "
             "keeps us in step with each other. His very breath and blood flow through us, nourishing us so that "
             "we will grow up healthy in God, robust in love."),
            ('new', '17-19', '§The Old Way Has to Go'),
            ('new', '17-19',
             "And so I insist — and God backs me up on this — that there be no going along with the crowd, the "
             "empty-headed, mindless crowd. They've refused for so long to deal with God that they've lost touch "
             "not only with God but with reality itself. They can't think straight anymore. Feeling no pain, they "
             "let themselves go in sexual obsession, addicted to every sort of perversion."),
            ('new', '20-24',
             "But that's no life for you. You learned Christ! I'm assuming you've paid careful attention to him and "
             "been well instructed in the truth, precisely as we have it in Jesus. Since we don't have the excuse "
             "of ignorance, everything — and I do mean everything — connected with that old way of life has to go. "
             "It's rotten through and through. Get rid of it! And then take on an entirely new way of life — a "
             "God-fashioned life, a life renewed from the inside and working itself into your conduct as God "
             "accurately reproduces his character in you."),
            ('new', '25',
             "What this adds up to, then, is this: no more lies, no more pretense. Tell your neighbor the truth. "
             "In Christ's body we're all connected to each other, after all. When you lie to others, you end up "
             "lying to yourself."),
            ('new', '26-27',
             "Go ahead and be angry. You do well to be angry — but don't use your anger as fuel for revenge. And "
             "don't stay angry. Don't go to bed angry. Don't give the Devil that kind of foothold in your life."),
            ('new', '28',
             "Did you used to make ends meet by stealing? Well, no more! Get an honest job so you can help others "
             "who can't work."),
            ('new', '29',
             "Watch the way you talk. Let nothing foul or dirty come out of your mouth. Say only what helps, each "
             "word a gift."),
            ('new', '30',
             "Don't grieve God. Don't break his heart. His Holy Spirit, moving and breathing in you, is the most "
             "intimate part of your life, making you fit for himself. Don't take such a gift for granted."),
            ('new', '31-32',
             "Make a clean break with all cutting, backbiting, profane talk. Be gentle with one another, "
             "sensitive. Forgive one another as quickly and thoroughly as God in Christ forgave you."),
        ],
        'ko_title': '에베소서 4장',
        'ko_ops': [
            ('new', '§성숙해지기'),
            ('keep', 2),
            ('keep', 3),
            ('keep', 5),
            ('keep', 6),
            ('new', '§낡은 생활방식은 가라'),
            ('keep', 8),
            ('keep', 9),
            ('keep', 10),
            ('keep', 11),
            ('keep', 12),
            ('keep', 13),
            ('keep', 14),
            ('keep', 15),
        ],
        'changes': [
            'EN: 기존 1-6 병합 → MSG 구조(1-3, 4-6)로 분할; 기존 17-24 병합 → (17-19, 20-24)로 분할; 기존 25-32 병합 → (25, 26-27, 28, 29, 30, 31-32)로 분할',
            'EN 배지 수정: 7-10→7-13',
            'EN: null 헤더 §Unity in the Body → MSG 소제목 §To Be Mature; §New Life Rules(위치 오류) 제거 후 §The Old Way Has to Go를 17-19 앞으로 이동',
            'EN 1-3 복원: "walk — better yet, run! — on the road God called you to travel", "pouring yourselves out for each other in acts of love"',
            'EN 7-13 복원: "the One who climbed up also climbed down...", "He handed out gifts above and below, filled heaven with his gifts, filled earth with his gifts", "fully mature adults, fully developed within and without, fully alive like Christ"',
            'EN 14-16 복원: "who is the source of everything we do", "His very breath and blood flow through us"',
            'EN 17-19 복원: "Feeling no pain, they let themselves go in sexual obsession, addicted to every sort of perversion"',
            'EN 20-24 복원: "paid careful attention... well instructed in the truth precisely as we have it in Jesus", "as God accurately reproduces his character in you"',
            'EN 25 복원: "no more pretense"',
            'EN 30 복원: "Don\'t break his heart", "moving and breathing in you... the most intimate part of your life, making you fit for himself"',
            'EN 31-32 복원: "as quickly and thoroughly"',
            'KO: null 헤더 §몸의 하나됨 제거, "한 주님, 한 믿음, 한 하나님" → §성숙해지기 (배지 1-3); §새로운 삶의 규칙(위치 오류) 제거, "낡은 생활방식을 버려" → §낡은 생활방식은 가라 (배지 17-19)',
            'KO는 MSG 전 절 커버 확인됨 — 추가 복원 없음',
        ],
    },
    5: {
        'en_ops': [
            ('new', '1-2', '§Wake Up from Your Sleep'),
            ('keep', 1),
            ('new', '3-4',
             "Don't allow love to turn into lust, setting off a downhill slide into sexual promiscuity, filthy "
             "practices, or bullying greed. Though some tongues just love the taste of gossip, those who follow "
             "Jesus have better uses for language than that. Don't talk dirty or silly. That kind of talk doesn't "
             "fit our style. Thanksgiving is our dialect."),
            ('new', '5',
             "You can be sure that using people or religion or things just for what you can get out of them — the "
             "usual variations on idolatry — will get you nowhere, and certainly nowhere near the kingdom of "
             "Christ, the kingdom of God."),
            ('new', '6-7',
             "Don't let yourselves get taken in by religious smooth talk. God gets furious with people who are full "
             "of religious sales talk but want nothing to do with him. Don't even hang around people like that."),
            ('keep', 4),
            ('new', '11-16',
             "Don't waste your time on useless work, mere busywork, the barren pursuits of darkness. Expose these "
             "things for the sham they are. It's a scandal when people waste their lives on things they must do in "
             "the darkness where no one will see. Rip the cover off those frauds and see how attractive they look "
             "in the light of Christ. Wake up from your sleep, climb out of your coffins — Christ will show you "
             "the light! So watch your step. Use your head. Make the most of every chance you get. These are "
             "desperate times!"),
            ('new', '17',
             "Don't live carelessly, unthinkingly. Make sure you understand what the Master wants."),
            ('new', '18-20',
             "Don't drink too much wine. That cheapens your life. Drink the Spirit of God, huge drafts of him. "
             "Sing hymns instead of drinking songs! Sing songs from your heart to Christ. Sing praises over "
             "everything, any excuse for a song to God the Father in the name of our Master, Jesus Christ."),
            ('new', '21', '§Relationships'),
            ('new', '21',
             "Out of respect for Christ, be courteously reverent to one another."),
            ('new', '22-24',
             "Wives, understand and support your husbands in ways that show your support for Christ. The husband "
             "provides leadership to his wife the way Christ does to his church, not by domineering but by "
             "cherishing. So just as the church submits to Christ as he exercises such leadership, wives should "
             "likewise submit to their husbands."),
            ('new', '25-28',
             "Husbands, go all out in your love for your wives, exactly as Christ did for the church — a love "
             "marked by giving, not getting. Christ's love makes the church whole. His words evoke her beauty. "
             "Everything he does and says is designed to bring the best out of her, dressing her in dazzling white "
             "silk, radiant with holiness. And that is how husbands ought to love their wives. They're really "
             "doing themselves a favor — since they're already \"one\" in marriage."),
            ('new', '29-33',
             "No one abuses his own body, does he? No, he feeds and pampers it. That's how Christ treats us, the "
             "church, since we are part of his body. And this is why a man leaves father and mother and cherishes "
             "his wife. No longer two, they become \"one flesh.\" This is a huge mystery, and I don't pretend to "
             "understand it all. What is clearest to me is the way Christ treats the church. And this provides a "
             "good picture of how each husband is to treat his wife, loving himself in loving her, and how each "
             "wife is to honor her husband."),
        ],
        'ko_title': '에베소서 5장',
        'ko_ops': [
            ('new', '§잠에서 깨어나라'),
            ('keep', 2),
            ('keep', 3),
            ('keep', 4),
            ('keep', 5),
            ('keep', 6),
            ('keep', 7),
            ('keep', 8),
            ('keep', 9),
            ('new', '§그리스도 안에서의 관계들'),
            ('keep', 11),
            ('keep', 12),
            ('keep', 13),
            ('keep', 14),
        ],
        'changes': [
            'EN: 기존 3-7/5-7 중복 병합 → MSG 구조(3-4, 5, 6-7)로 재분할; 11-14에서 17절 분리; 18-21에서 21절 분리',
            'EN 배지 수정: 11-14→11-16, 18-21→18-20, 22→21 (21절 본문), 25-27→25-28, 28-33→29-33',
            'EN: null 헤더 §Walk in Love and Light → MSG 소제목 §Wake Up from Your Sleep; §Relationships 삽입 (21 앞으로)',
            'EN 3-4 복원: "sexual promiscuity, filthy practices"',
            'EN 5 복원: "the usual variations on idolatry"',
            'EN 11-16 복원: "Rip the cover off those frauds and see how attractive they look in the light of Christ"',
            'EN 18-20 복원: "huge drafts of him", "any excuse for a song"',
            'EN 22-24 복원: "understand and support"',
            'EN 25-28 복원: "a love marked by giving, not getting", "dressing her in dazzling white silk, radiant with holiness"',
            'EN 29-33 복원: "loving himself in loving her"',
            'KO: null 헤더 §사랑과 빛 안에서 걸으라 제거, "잠에서 깨어나라" → §잠에서 깨어나라 (배지 1-2), "그리스도 안에서의 관계들" → §그리스도 안에서의 관계들 (배지 21)',
            'KO는 MSG 전 절 커버 확인됨 — 추가 복원 없음',
        ],
    },
    6: {
        'en_ops': [
            ('keep', 1),
            ('keep', 2),
            ('keep', 3),
            ('keep', 4),
            ('new', '10-12', '§A Fight to the Finish'),
            ('keep', 5, '10-12'),
            ('new', '13-18',
             "So be ready. You're facing something way bigger than you can handle on your own. Grab every piece of "
             "armor God gives you, so when the dust settles, you're the one left standing. We're talking about "
             "Truth, Righteousness, Peace, Faith, and Salvation. These aren't just words; they're your weapons. "
             "Learn how to use them, because you'll need them every day. And God's Word? That's your ultimate "
             "weapon. In the same way, prayer is essential in this ongoing warfare. Pray hard and long. Pray for "
             "your brothers and sisters. Keep your eyes open. Keep each other hyped up so no one falls behind or "
             "drops out."),
            ('keep', 7),
            ('keep', 8),
            ('keep', 9),
        ],
        'ko_title': '에베소서 6장',
        'ko_ops': [
            ('keep', 1),
            ('keep', 2),
            ('keep', 3),
            ('keep', 4),
            ('new', '§마귀랑 끝까지 싸워라'),
            ('keep', 6),
            ('new',
             "단단히 준비하셈. 너네는 지금 혼자서는 감당하기 힘든 상대를 만난 거임. 도움 될 만한 건 뭐든지 다 챙기고, "
             "하나님이 주신 모든 무기로 풀템 장착하셈. 그러면 싸움이 끝나도 너네는 승리의 함성을 지르면서 여전히 두 "
             "발로 서 있을 거임. 진리, 의로움, 평화, 믿음, 구원은 그냥 말이 아니야. 사용법을 잘 익히셈. 살아가는 내내 "
             "그 무기들이 필요할 거임. 하나님의 말씀이야말로 진짜 필수템임. 마찬가지로 이 계속되는 전쟁에서 기도는 "
             "완전 필수임. 열심히, 오래 기도하셈. 친구들을 위해 기도하셈. 계속 정신 바짝 차리셈. 서로 으쌰으쌰해서 "
             "아무도 뒤처지거나 포기하는 사람 없게 하셈."),
            ('keep', 8),
            ('keep', 9),
            ('keep', 10),
        ],
        'changes': [
            'EN 배지 수정: 10-13→10-12, 14-18→13-18',
            'EN: null 헤더 §The Armor of God 제거, MSG 소제목 §A Fight to the Finish를 10-12 앞으로 이동',
            'EN 13-18 복원: "Keep your eyes open" (기존 EN에는 누락), "no one falls behind or drops out"',
            'KO: null 헤더 §하나님의 전신갑주 제거, "마귀랑 끝까지 싸워라" → §마귀랑 끝까지 싸워라 (배지 10-12)',
            'KO 13-18 복원: "진리, 의로움, 평화, 믿음, 구원은 그냥 말이 아니야" (전신갑주 목록 누락)',
        ],
    },
}
