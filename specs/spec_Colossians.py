#!/usr/bin/env python3
"""Colossians spec — built 2026-09-22 from MSG cache msg_Colossians.txt.

MSG structure:
  ch1: 1-2, 3-5, 5-8, 9-12, 13-14, 15-18, 18-20, 21-23, 24-25, 26-29 (10)
  ch2: 1, 2-4, 5, 6-7, 8-10, 11-15, 16-17, 18-19, 20-23 (9)
  ch3: 1-2, 3-4, 5-8, 9-11, 12-14, 15-17, 18, 19, 20, 21, 22-25 (11)
  ch4: 1, 2-4, 5-6, 7-9, 10-11, 12-13, 14, 15, 16, 17, 18 (11)
"""
BOOK = 'Colossians'
SLUG = 'Colossians'

CHAPTERS = {
    1: {
        'en_ops': [
            ('keep', 1),
            ('new', '3-5', '§Working in His Orchard'),
            ('new', '3-5',
             "We're always hitting up God, our Father, and Jesus, the Messiah, to say thanks for you guys. "
             "Seriously, we can't stop. We keep hearing about your solid faith in Jesus and how you're always "
             "showing love to all the other Christians. The lines of purpose in your lives never grow slack — "
             "they're tightly tied to your future in heaven, kept taut by hope."),
            ('keep', 3, '5-8'),
            ('keep', 4, '9-12'),
            ('keep', 5, '13-14'),
            ('new', '15-18', '§Christ Holds It All Together'),
            ('keep', 6, '15-18'),
            ('keep', 7),
            ('keep', 8),
            ('keep', 9),
            ('keep', 10, '26-29'),
        ],
        'ko_title': '골로새서 1장',
        'ko_ops': [
            ('keep', 1),
            ('new', '§그분의 과수원에서 일하기'),
            ('keep', 3),
            ('keep', 4),
            ('keep', 5),
            ('keep', 6),
            ('new', '§모든 것을 붙드시는 그리스도'),
            ('keep', 8),
            ('keep', 9),
            ('keep', 10),
            ('keep', 11),
            ('keep', 12),
        ],
        'changes': [
            'EN 배지 수정: 3-4→3-5, 5-6→5-8, 9-11→9-12, 12-14→13-14, 15-17→15-18, 25-29→26-29',
            'EN: null 헤더 §The Supremacy of Christ 제거, MSG 소제목 §Working in His Orchard / §Christ Holds It All Together 삽입',
            'EN 3-5 복원: "lines of purpose never grow slack, tightly tied to your future in heaven, kept taut by hope"',
            'KO: null 헤더 §그리스도의 최고 권위 제거, §그분의 과수원에서 일하기 / §모든 것을 붙드시는 그리스도로 교체, 문단 선두 배지 중복 라인 제거',
            'KO 내용은 MSG 전 절 커버 확인됨 — 추가 복원 없음',
        ],
    },
    2: {
        'en_ops': [
            ('new', '1',
             "Hey, I gotta tell you, I'm going hard in the paint for you guys and the crew over in Laodicea. "
             "A lot of you have never even seen my face, but it doesn't matter. I'm in your corner, for real. "
             "You're not flying solo in this."),
            ('new', '2-4',
             "I want you woven into a tapestry of love, in touch with everything there is to know of God. "
             "Then you will have minds confident and at rest, focused on Christ, God's great mystery. "
             "All the richest treasures of wisdom and knowledge are embedded in that mystery and nowhere else. "
             "And we've been shown the mystery! I'm telling you this so you don't get led off on some "
             "wild-goose chase after other so-called mysteries, or \"the Secret.\""),
            ('new', '5',
             "Yeah, I'm far away, and you might never meet me in person, but believe me, I'm right there with you. "
             "I'm stoked to hear of the careful, orderly way you handle your business, and impressed with the solid "
             "substance of your faith in Christ."),
            ('new', '6-7', '§From the Shadows to the Substance'),
            ('new', '6-7',
             "So here's my simple, straight-up counsel: just go ahead with what you've been given. You've got "
             "Christ Jesus, the Master — now live him. You're deeply rooted in him, well constructed upon him. "
             "You know your way around the faith, so now do what you've been taught. School's out; quit studying "
             "the subject and start living it! And let your living spill over into thanksgiving."),
            ('new', '8-10',
             "Watch out for people who try to dazzle you with big words and intellectual double-talk. They want "
             "to drag you off into endless arguments that never amount to anything. They spread their ideas through "
             "the empty traditions of human beings and the empty superstitions of spirit beings. But that's not "
             "the way of Christ. Everything about God gets expressed in him, so you can see and hear him clearly. "
             "You don't need a telescope, a microscope, or a horoscope to realize the fullness of Christ and the "
             "emptiness of the universe without him. When you come to him, that fullness comes together for you, "
             "too. His power extends over everything."),
            ('keep', 6),
            ('keep', 7),
            ('new', '18-19',
             "Don't tolerate people who try to run your life, ordering you to bow and scrape, insisting you join "
             "their obsession with angels and seek out visions. They're a lot of hot air, that's all they are. "
             "They're completely out of touch with the source of life, Christ, who puts us together in one piece, "
             "whose very breath and blood flow through us. He is the Head and we are the body. We can only grow "
             "up healthy in God as he nourishes us."),
            ('new', '20-23',
             "So, then, if with Christ you've put all that puffed-up and childish religion behind you, why do you "
             "let yourselves be bullied by it? \"Don't touch this! Don't taste that! Don't go near this!\" Do you "
             "think things that are here today and gone tomorrow are worth that kind of attention? Such things "
             "sound impressive if said in a deep enough voice. They even give the illusion of being pious and "
             "humble and austere. But they're just another way of showing off, making yourselves look important."),
        ],
        'ko_title': '골로새서 2장',
        'ko_ops': [
            ('keep', 1),
            ('new',
             "내가 바라는 건, 너네가 사랑의 태피스트리처럼 촘촘하게 엮여서, 하나님을 알아가는 모든 경지에 이르는 거야. "
             "그러면 너네 마음이 확신과 평안을 얻고, 하나님의 개대단한 비밀, 바로 그리스도한테 딱 꽂히게 될 거임. "
             "모든 지혜랑 지식의 보물이 그 비밀 안에 다 들어있거든. 다른 데서는 절대 못 찾음. "
             "이제 그 비밀이 우리한테 환하게 공개됐음! 내가 이 말을 왜 하냐면, 누가 너네 꼬드겨서 다른 가짜 비밀이나 "
             "\"그 비밀\" 같은 거 쫓아다니지 못하게 하려고 그러는 거임."),
            ('keep', 3),
            ('new', '§그림자에서 실체로'),
            ('keep', 5),
            ('keep', 6),
            ('keep', 7),
            ('keep', 8),
            ('keep', 9),
            ('keep', 10),
        ],
        'changes': [
            'EN 배지 수정: 1-3→1, 2-3→2-4, 6-8→6-7',
            'EN: null 헤더 §Alive in Christ 제거, MSG 소제목 §From the Shadows to the Substance를 6-7 앞으로 이동',
            'EN 2-4 복원: tapestry of love, minds confident and at rest (기존 "minds blown" 오역 수정)',
            'EN 5 복원: careful and orderly ways you conduct your affairs',
            'EN 6-7 복원: "Just go ahead with what you\'ve been given", "School\'s out; quit studying the subject and start living it!"',
            'EN 8-10 복원: microscope 누락',
            'EN 18-19 복원: "whose very breath and blood flow through us"',
            'EN 20-23 복원: "illusion of being pious and humble and austere"',
            'KO: null 헤더 §그리스도 안에서 살아 있음 제거, "실체이신 그리스도" → §그림자에서 실체로, 2-4에 태피스트리 이미지 복원, 문단 선두 배지 중복 라인 제거',
        ],
    },
    3: {
        'en_ops': [
            ('new', '1-2', '§He Is Your Life'),
            ('keep', 1),
            ('keep', 2),
            ('keep', 3, '5-8'),
            ('keep', 4, '5-8'),
            ('keep', 5),
            ('keep', 6),
            ('keep', 7),
            ('keep', 8, '18'),
            ('keep', 9),
            ('keep', 10),
            ('keep', 11),
            ('keep', 12),
            ('new', '22-25',
             "And for all you workers out there, do what your bosses tell you. Don't just do the bare minimum "
             "to get by. Do your best. Work from the heart for your real Boss, for God. You can be sure you'll "
             "get paid in full when you get your inheritance. Always remember, the ultimate Boss you're serving "
             "is Christ. The lazy worker who does a bad job will be held responsible. Being a follower of Jesus "
             "isn't an excuse for bad work."),
        ],
        'ko_title': '골로새서 3장',
        'ko_ops': [
            ('new', '§그분이 바로 너네 생명이심'),
            ('keep', 2),
            ('keep', 3),
            ('keep', 4),
            ('keep', 5),
            ('keep', 6),
            ('keep', 7),
            ('keep', 8),
            ('keep', 10),
            ('keep', 9),
            ('keep', 11),
            ('keep', 12),
            ('keep', 13),
            ('keep', 14),
        ],
        'changes': [
            'EN 배지 수정: 5-9→5-8; null 헤더 3개에 뒤따르는 본문 배지 부여 (§Ditch the Old You→5-8, §At Home and at Work→18)',
            'EN 상단 헤더 §Put On the New You → MSG 소제목 §He Is Your Life로 교체',
            'EN 22-25 복원: "Work from the heart" 누락',
            'KO: §새로운 너를 입어라 → §그분이 바로 너네 생명이심, "참된 생명이신 그리스도" 중복 헤더 제거, §가정과 직장에서를 18절 앞으로 이동(EN과 위치 일치), 문단 선두 배지 중복 라인 제거',
            'KO 내용은 MSG 전 절 커버 확인됨 — 추가 복원 없음',
        ],
    },
    4: {
        'en_ops': [
            ('keep', 1),
            ('new', '2-4', '§Pray for Open Doors'),
            ('keep', 3),
            ('keep', 4),
            ('keep', 5),
            ('keep', 6),
            ('keep', 7),
            ('keep', 8),
            ('keep', 9),
            ('keep', 10),
            ('keep', 11),
            ('keep', 12),
        ],
        'ko_title': '골로새서 4장',
        'ko_ops': [
            ('keep', 1),
            ('new', '§열린 문을 위해 기도하라'),
            ('keep', 4),
            ('keep', 5),
            ('new',
             "내 착한 친구 두기고가 내 소식 다 알려줄 거야. 그는 주님 섬기는 일에 완전 믿음직한 동료거든. "
             "내가 걔를 보낸 건 너네한테 우리 사정 알리고 너네 믿음 응원해주려는 거임. "
             "그와 함께 오네시모도 보냈는데, 걔는 너네랑 같은 고향 사람이고 완전 믿음직한 형제가 됐어! "
             "걔네가 여기서 있었던 일 전부 다 말해줄 거다."),
            ('keep', 8),
            ('keep', 9),
            ('keep', 10),
            ('keep', 11),
            ('keep', 12),
            ('keep', 13),
            ('keep', 14),
        ],
        'merges': [
            {'para': 4, 'msg_ranges': ['7-8', '9'],
             'note': 'MSG 7-9는 한 문단. 기존 KO가 7-8(두기고)과 9(오네시모)로 분리한 것을 EN과 구조 일치 위해 병합'},
        ],
        'confirmations': [
            '골로새서 4장: 기존 KO가 7-8과 9로 나누었던 두 문단을 MSG 구조(7-9 한 문단)에 맞춰 병합(7-8, 9) — 컨펌 필요',
        ],
        'changes': [
            'EN: null 헤더 §Final Instructions 제거, §**Prayer Requests & Spreading the Word** → MSG 소제목 §Pray for Open Doors로 교체',
            'KO: null 헤더 §마지막 지시 제거, 중복 헤더 §메시지의 비밀을 전하도록 기도해 줘 제거, §기도 부탁과 말씀 전파 → §열린 문을 위해 기도하라',
            'KO 7-8/9 병합 → 7-9 (MSG 구조 일치, EN과 parity)',
            'KO 배지 수정: 7-8→7-9 (병합)',
        ],
    },
}
