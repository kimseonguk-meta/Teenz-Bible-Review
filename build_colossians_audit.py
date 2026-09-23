#!/usr/bin/env python3
"""Colossians MSG-based re-audit — builds fixes/en_Colossians.json and fixes/ko_Colossians.json."""
import json

EN = [
 {
  "chapter": 1,
  "title": "Jesus is the GOAT",
  "paragraphs": [
   "Hey, what up? It's Paul, on a special mission from Jesus, part of God's epic master plan. Me and my bro Timothy are sending a shout-out to all the Christians in Colosse \u2014 the real ones who actually follow Christ. Hope you're getting all the good stuff from God our Father.",
   "\u00a7Working in His Orchard",
   "We're always hitting up God, our Father, and Jesus, the Messiah, to say thanks for you guys. Seriously, we can't stop. We keep hearing about your solid faith in Jesus and how you're always showing love to all the other Christians. You guys are totally focused on your future in heaven, and that hope keeps you going strong.",
   "The message you heard is the real deal, just as legit as the first day you heard it. It's not some trend that fades away; it's blowing up all over the world, getting bigger and stronger, just like it is with you. From the moment you heard and got what God is doing, you've been hungry for more. And it's still going strong, just like when our boy Epaphras taught you. He's a super-reliable worker for Christ \u2014 I can always count on him. He's the one who told us how the Spirit has made love a huge part of your lives.",
   "So for real, since we first heard about you, we haven't stopped praying for you. We're asking God to give you the smarts and the right vibe to totally get his plan. We're praying you'll live in a way that makes the Boss proud, working hard in his orchard. The more you learn how God operates, the better you'll get at your own stuff. We're praying you'll have the strength to hang in there when things get tough\u2014not just gritting your teeth, but that awesome power-up God gives. It's the kind of strength that helps you handle anything and still be stoked, thanking the Father who made us worthy to be part of his awesome, bright future.",
   "God totally saved us. He pulled us out of some dead-end situations and dark places. He put us in the kingdom of his Son, who he loves like crazy. This is the Son who rescued us from the mess we were in and wiped our slate clean from all the sins we were stuck repeating.",
   "\u00a7Christ Holds It All Together",
   "When we look at this Son, we're basically seeing the invisible God. We see God's original blueprint for everything. Because everything, and I mean *everything*\u2014in the sky, on the ground, stuff you can see and stuff you can't, even all the different levels of angels\u2014it all started with him and is all about him. He was there before anything else existed, and he's the one holding it all together, even right now. And when it comes to the church, he's the one who organizes it and keeps it together, like a head on a body.",
   "He was the top dog from the very beginning, and he's supreme in the end, leading the resurrection parade. From start to finish, he's the main event, way above everyone and everything. He's so huge that all of God fits perfectly in him with room to spare. And here's the thing: all the broken, messed-up parts of the universe \u2014 people, things, animals, atoms, you name it \u2014 get fixed and put back together in perfect harmony because of his death, because of the blood he shed on the cross.",
   "You guys are a perfect example of what he does. You used to have your backs to God, thinking rebellious stuff about him and causing trouble all the time. But now, because Christ went all in for you on the cross and literally died for you, he brought you back to God's side. He put your lives back together, making you whole and holy in his eyes. You don't just walk away from a gift like that! You stay grounded and solid in that trust, always tuned in to the message, and don't get sidetracked. There's no other message but this one. Every single person on earth gets this same message. And me, Paul? I'm one of the messengers.",
   "I want you to know I'm actually glad I'm the one in jail right now and not you. There's a lot of suffering in the world that needs to be dealt with, the kind of stuff Christ takes on. I'm happy to take my share of that for the church. When I became a servant of the church, I saw this suffering as a gift, God's way of helping me serve you and lay out the whole truth.",
   "This big secret has been under wraps for a long time, but now it's out in the open. God wanted everyone, not just the Jews, to know this amazing and glorious secret, no matter who they are or what their background is. The secret is basically this: Christ is in you, so you can be sure you'll share in God's glory. It's that simple. That's what our message is all about. We preach Christ, and we warn people not to add a bunch of extra stuff to it. We teach with a lot of common sense so we can help everyone grow up and be mature. And being mature is just about one thing: Christ. Nothing more, nothing less. That's what I'm working my butt off for, day after day, year after year, using the awesome energy God gives me.",
  ],
  "verseRanges": ["1-2","3-5","3-5","5-8","9-12","13-14","15-18","15-18","18-20","21-23","24-25","26-29"],
  "msg_ranges": ["1-2","3-5","5-8","9-12","13-14","15-18","18-20","21-23","24-25","26-29"],
  "merges": [],
  "splits": [
   {"msg_range": "5", "paras": [2, 3], "note": "MSG 원문이 5절을 3-5와 5-8 두 문단에 걸쳐 사용 \u2014 EN도 MSG 문단 구분 그대로 따름"},
   {"msg_range": "18", "paras": [7, 8], "note": "MSG 원문이 18절을 15-18과 18-20 두 문단에 걸쳐 사용 \u2014 EN도 MSG 문단 구분 그대로 따름"}
  ],
  "changes": [
   "MSG 문단 구조 기준으로 배지 재구성: 3-4\u21923-5, 5-6\u21925-8, 9-11\u21929-12, 12-14\u219213-14, 15-17\u219215-18, 17-20\u219218-20, 25-29\u219226-29",
   "MSG에 없는 임의 \u00a7헤더 '\u00a7The Supremacy of Christ' 삭제 \u2014 MSG 섹션 헤더 2개를 \u00a7헤더로 복원: '\u00a7Working in His Orchard'(\u00a73-5), '\u00a7Christ Holds It All Together'(\u00a715-18)",
   "EN 1-2: MSG 'Christians and stalwart followers of Christ' 복원",
   "EN 5-8: MSG 'you've been hungry for more', 'I could always depend on him'(Epaphras) 복원",
   "EN 9-12: MSG 'work hard in his orchard' 복원",
   "EN 18-20: MSG 'people and things, animals and atoms' 복원 ('animals, atoms' 추가)",
   "EN 26-29: MSG 'day after day, year after year' 복원"
  ],
  "confirmations_needed": [],
  "review_status": "msg_audited"
 },
 {
  "chapter": 2,
  "title": "Don't Get Played",
  "paragraphs": [
   "Hey, I want you to know I'm going hard in the paint for you guys and the crew over in Laodicea. Most of you have never even seen my face, but it doesn't matter. I'm in your corner, for real. You're not flying solo in this.",
   "I want you all woven together into a tapestry of love, in touch with everything there is to know of God. I want your minds confident and at rest, focused on Christ, God's great mystery. All the richest treasures of wisdom and knowledge are packed into that mystery and nowhere else. And we've been shown the mystery! I'm telling you this so you don't get faked out by people trying to sell you some other \u201csecret\u201d or \u201cmystery.\u201d",
   "Yeah, I'm far away, and you might never meet me in person, but believe me, I'm right there with you. I'm stoked to hear that you're living right and that your faith in Christ is rock solid.",
   "\u00a7From the Shadows to the Substance",
   "So here's the deal: you've got Christ Jesus, the Master. Now live like it. You're rooted in him, built on him. You know the playbook, so get out there and play! School's out \u2014 quit studying the subject and start living it. And let your living spill over into thanks.",
   "Watch out for people who try to impress you with big words and philosophical nonsense. They're just trying to drag you into pointless arguments. They're peddling man-made traditions and superstitions about spirits and stuff. That's not how Christ rolls. Everything about God is in him, plain and simple \u2014 you can see and hear him clearly. You don't need a telescope, a microscope, or a horoscope to see how awesome Christ is and how empty everything else is without him. When you're with him, you're complete. He's the head honcho over everything and everyone.",
   "And you don't get in on this by following a bunch of rules or getting circumcised. Nah, you're already in. You got in through what Christ did for you when he wrecked the power of sin. Your baptism was like a funeral for your old life and a resurrection to a new one. God raised you from the dead, just like he did with Christ. When you were dead in your sins, you couldn't do anything for God. But God made you alive with Christ! Think about it! All your sins are gone, the slate is clean. That old arrest warrant against you was canceled and nailed to the cross. He stripped the universe's spiritual bullies of their fake authority at the Cross and marched them, totally humiliated, through the streets.",
   "So don't let anyone give you a hard time about what you eat or drink, or about religious festivals or holidays. That stuff is just a shadow of the real thing, and the real thing is Christ.",
   "Don't put up with people who try to control you, telling you to bow down to angels and have visions. They're just full of hot air. They're not connected to the source of life, who is Christ. He's the one who holds us all together in one piece \u2014 his very breath and blood flow through us. He's the head, and we're the body. We can only grow up healthy in God if we're getting our life from him.",
   "So if you've left all that fake, childish religion behind with Christ, why do you let people push you around with rules like, \u201cDon't touch this! Don't taste that! Don't go near this!\u201d? Do you really think that stuff that's here today and gone tomorrow is that important? It might sound impressive in a deep voice \u2014 all pious and humble and hardcore \u2014 but it's just another way of showing off and making yourself look good.",
  ],
  "verseRanges": ["1","2-4","5","6-7","6-7","8-10","11-15","16-17","18-19","20-23"],
  "msg_ranges": ["1","2-4","5","6-7","8-10","11-15","16-17","18-19","20-23"],
  "merges": [],
  "splits": [],
  "changes": [
   "MSG 문단 구조 기준으로 배지 재구성: 1-3\u21921(본문이 1절만 다룸), 2-3\u21922-4, 6-8\u21926-7",
   "MSG에 없는 임의 \u00a7헤더 '\u00a7Alive in Christ' 삭제 \u2014 MSG 섹션 헤더 'From the Shadows to the Substance'를 \u00a7헤더로 복원 (\u00a76-7)",
   "EN 2-4: MSG 'woven into a tapestry of love', 'in touch with everything there is to know of God', 'minds confident and at rest' 복원",
   "EN 6-7: MSG 'School's out; quit studying the subject and start living it!' 복원",
   "EN 8-10: MSG 'a microscope', 'so you can see and hear him clearly' 복원",
   "EN 11-15: MSG 'stripped of their sham authority', 'marched them naked through the streets' 복원 ('totally humiliated')",
   "EN 18-19: MSG 'puts us together in one piece, whose very breath and blood flow through us' 복원",
   "EN 20-23: MSG 'sound impressive if said in a deep enough voice', 'pious and humble and austere' 복원"
  ],
  "confirmations_needed": [],
  "review_status": "msg_audited"
 },
 {
  "chapter": 3,
  "title": "Level Up Your Life",
  "paragraphs": [
   "\u00a7He Is Your Life",
   "Hey, so if you're for real about this new life with Christ, you gotta act like it. Start chasing the stuff that matters, the stuff Christ is in charge of. Don't just stare at your feet, obsessed with what's right in front of you. Look up! See what's happening with Christ, 'cause that's where the real action is. Get on his level.",
   "Your old self? Dead and gone. Your new life, your *real* life, is with Christ in God's crew, even if nobody else sees it. He's your whole life. And when Christ, your real life, shows up again on Earth, you're gonna show up too\u2014the real you, the awesome you. Until then, just chill and be cool with not being the center of attention, just like Christ was.",
   "So, you gotta drop everything connected to that old, dead life. All that horrible stuff: being unfaithful, being impure, always wanting more, doing whatever you want whenever you want, and just grabbing whatever looks good. That's a life run by things and feelings, not by God. And that's the kind of stuff that makes God want to just blow up in anger. You used to be all about that stuff, but you didn't know any better. Now you do, so get rid of it for good: getting mad all the time, being cranky, being mean, cussing, and talking trash.",
   "And don't lie to each other. You're done with that. It's like taking off a set of filthy, old clothes that don't even fit and throwing them in a fire. Now you've got a whole new wardrobe, a total transformation. Every piece is custom-made by God, with his name on it. All the old trends are out. Words like 'Jew' or 'non-Jew,' 'religious' or 'not religious,' 'insider' or 'outsider,' 'savage' or 'lame,' 'slave' or 'free'\u2014they don't mean anything anymore. Now, everyone's all about Christ. Everyone's in the crew.",
   "So, since you're chosen by God for this new life of love, you gotta dress the part. God picked out this outfit for you: be compassionate, be kind, be humble, be strong but quiet, and have self-control. Be chill, be cool with not being first, and be quick to forgive when someone messes up. Forgive them as fast and as completely as the Boss forgave you. And no matter what else you wear, always wear love. It's your go-to, everyday gear. Never leave home without it.",
   "Let the peace of Christ keep you all on the same page, working together. No more going off and doing your own thing. And be thankful. Let the Word of Christ, the Message, just take over your whole house. Give it tons of space in your lives. Teach and help each other out with good advice. And sing! Sing your hearts out to God! Everything you do, every single detail\u2014what you say, what you do, whatever\u2014do it all for the Boss, for Jesus. And thank God the Father every step of the way.",
   "Wives, you gotta support your husbands and submit to them in a way that honors the Boss.",
   "Husbands, love your wives like crazy. Don't take advantage of them.",
   "Kids, listen to your parents. The Boss loves to see that.",
   "Parents, don't be too hard on your kids, or you'll break their spirits.",
   "And for all you workers out there, do what your bosses tell you. Don't just do the bare minimum to get by. Do your best. Work from the heart for your real Boss, for God. You can be sure you'll get paid in full when you get your inheritance. Always remember, the ultimate Boss you're serving is Christ. The lazy worker who does a bad job will be held responsible. Being a follower of Jesus isn't an excuse for bad work.",
  ],
  "verseRanges": ["1-2","1-2","3-4","5-8","9-11","12-14","15-17","18","19","20","21","22-25"],
  "msg_ranges": ["1-2","3-4","5-8","9-11","12-14","15-17","18","19","20","21","22-25"],
  "merges": [],
  "splits": [],
  "changes": [
   "MSG 문단 구조 기준으로 배지 재구성: 5-9\u21925-8",
   "MSG에 없는 임의 \u00a7헤더 3개 ('\u00a7Put On the New You', '\u00a7Ditch the Old You', '\u00a7At Home and at Work') 삭제 \u2014 MSG 섹션 헤더 'He Is Your Life'를 \u00a7헤더로 복원 (\u00a71-2)",
   "EN 22-25: MSG 'Work from the heart' 복원"
  ],
  "confirmations_needed": [],
  "review_status": "msg_audited"
 },
 {
  "chapter": 4,
  "title": "The Final Shout-Outs",
  "paragraphs": [
   "Alright, so if you're a boss, don't be harsh to your employees. Be cool and treat them right. Remember, you've got a boss too \u2014 the big guy upstairs, God.",
   "\u00a7Pray for Open Doors",
   "Always be praying. Like, for real. Stay sharp, and be thankful for everything. And hey, while you're at it, pray for us. Pray that God opens up opportunities for us to talk about the big secret of Jesus, even though I'm stuck in jail. Pray that I can explain it all super clearly to everyone.",
   "Be smart about how you live and work around people who don't know Jesus \u2014 don't miss a trick. Make every moment count. When you talk, be cool and build people up; don't roast them or cut them out.",
   "My boy Tychicus is coming to you, and he'll give you the full scoop on me. He's a solid guy and a great helper in God's work. I'm sending him so you know what's up with us and so he can get you hyped about your faith. I'm also sending Onesimus with him. He's one of your own, and he's become a super trustworthy and awesome bro. They'll tell you everything that's been going down here.",
   "Aristarchus, my cellmate, says 'sup. So does Mark, Barnabas's cousin. You got a letter about him, so if he rolls through, give him a warm welcome. Jesus, the one they call Justus, also sends a shout-out. These are the only guys from the old crew who are still with me, working for God's kingdom. They've been a huge help, for real.",
   "Epaphras, who's from your town, says hi. That guy is a beast! He's always praying hard for you guys, that you'll stand firm, all grown up and confident in what God wants for you. I've seen him grind for you and the people in Laodicea and Hierapolis.",
   "Luke, the awesome doctor, and Demas both say what's up.",
   "Tell our friends in Laodicea we said hi. Same to Nympha and the church that meets at her place.",
   "After you read this letter, make sure the church in Laodicea reads it too. And get the letter that went to Laodicea and read that one as well.",
   "Oh, and tell Archippus to get on it and crush the job the Boss gave him. Like, totally own it.",
   "I'm signing this myself \u2014 Paul. Don't forget to pray for me while I'm in here. Grace out.",
  ],
  "verseRanges": ["1","2-4","2-4","5-6","7-9","10-11","12-13","14","15","16","17","18"],
  "msg_ranges": ["1","2-4","5-6","7-9","10-11","12-13","14","15","16","17","18"],
  "merges": [],
  "splits": [],
  "changes": [
   "MSG에 없는 임의 \u00a7헤더 2개 ('\u00a7Final Instructions', '\u00a7**Prayer Requests & Spreading the Word**') 삭제 \u2014 MSG 섹션 헤더 'Pray for Open Doors'를 \u00a7헤더로 복원 (\u00a72-4)",
   "EN 5-6: MSG 'Don't miss a trick' 복원; MSG에 없는 부연 'Don't be weird' 삭제",
   "EN 12-13: MSG 'stand firm' 복원",
   "EN 16: MSG 'the letter that went to Laodicea'로 정정 ('the letter I sent to them'이라는 임의 해석 삭제)"
  ],
  "confirmations_needed": [],
  "review_status": "msg_audited"
 }
]

KO = [
 {
  "chapter": 1,
  "title": "예수님은 진짜 최고",
  "paragraphs": [
   "안녕! 나 바울임. 예수님이 주신 특별한 미션을 받고, 하나님의 큰 그림을 따라 움직이고 있음. 나랑 내 친구 디모데가 골로새에 사는 크리스천들 \u2014 예수님을 진짜로 따르는 찐 팔로워들한테 인사 박음. 우리 아빠 하나님이 주시는 모든 좋은 것들이 너네한테 있기를 바람.",
   "\u00a7그분의 밭에서 일하기",
   "너네를 위해 기도할 때마다 완전 감사가 터져 나옴. 너네 덕분에 우리 아빠 하나님이랑 메시아 예수님한테 계속 감사하게 됨. 너네가 예수님을 향한 믿음이 완전 굳건하고, 모든 크리스천들한테 사랑을 막 퍼주고 있다는 소식이 계속 들려오거든. 너네 인생의 목표는 완전 튼튼한 밧줄 같아서 절대 느슨해지지 않음. 하늘에 있는 너네 미래랑 단단히 연결돼 있고, 희망으로 꽉 묶여 있거든.",
   "이 메시지는 너네가 처음 들었을 때랑 똑같이 지금도 진짜임. 시간이 지나도 절대 약해지지 않고, 세상 어디서나 똑같음. 이 메시지는 너네 안에서 그랬던 것처럼 열매를 맺고 점점 더 커지고 강해지고 있음. 하나님이 무슨 일을 하고 계신지 처음 듣고 깨달은 그날부터, 너네는 이 메시지를 더 원하게 됐음. 우리 친구이자 절친한 동료인 에바브라한테 배웠을 때처럼 지금도 활발하게 움직이고 있음. 에바브라는 그리스도의 완전 든든한 일꾼이고, 내가 항상 믿는 사람임! 그가 성령님이 너네 삶을 얼마나 사랑으로 가득 채우셨는지 우리한테 알려줬음.",
   "너네 소식 들은 날부터, 우리는 너네를 위해 한 번도 안 쉬고 기도했음. 하나님이 너네한테 그분의 뜻에 딱 맞는 지혜로운 마음이랑 영을 주시길, 그래서 하나님이 일하시는 방식을 완전히 이해하게 되길 기도했음. 우리는 너네가 주님의 밭에서 주님이 자랑스러워하실 만큼 열심히 일하면서, 주님을 위해 완전 멋지게 살기를 기도함. 하나님이 일하시는 방식을 알면 알수록, 너네도 너네 일을 어떻게 해야 할지 더 잘 알게 될 거임. 우리는 너네가 끝까지 버틸 수 있는 힘을 받기를 바람. 이를 악물고 버티는 그런 힘이 아니라, 하나님이 주시는 어마어마한 힘 말이야. 그건 견디기 힘든 것도 견디게 하고 기쁨이 넘치게 하는 힘임. 우리를 위해 준비해 두신 밝고 아름다운 모든 것에 참여할 만큼 우리를 강하게 만드시는 아빠께 감사하게 되는 그런 힘 말이야.",
   "하나님은 우리를 막다른 골목이랑 어두운 감옥에서 구해내서, 그분이 완전 아끼는 아들의 나라로 옮겨주셨음. 그 아들은 우리를 수렁에서 건져주시고, 계속 반복해서 지을 수밖에 없었던 죄에서 벗어나게 해주셨음.",
   "\u00a7모든 것을 하나로 묶는 그리스도",
   "우리는 이 아들을 보면서 보이지 않는 하나님을 보는 거임. 이 아들을 보면서 모든 창조물에 담긴 하나님의 원래 계획을 보는 거임. 위에 있는 거, 아래 있는 거, 보이는 거, 안 보이는 거, 천사 위의 천사 위의 천사까지 \u2014 진짜 모든 게 그분 안에서 시작됐고, 그분 안에서 자기 목적을 찾음. 그분은 모든 게 존재하기 전부터 계셨고, 지금 이 순간에도 모든 걸 하나로 묶고 계심. 교회도 마찬가지임. 머리가 몸을 하나로 묶어주듯이, 그분이 교회를 하나로 묶고 이끌어 주심.",
   "그분은 처음에도 최고셨고, 부활 행진의 맨 앞에서 마지막에도 최고이심. 처음부터 끝까지, 그분은 모든 것과 모든 사람 위에 우뚝 서 계심. 그분은 너무 넓고 커서, 하나님의 모든 것이 그분 안에서 자기 자리를 찾고도 전혀 좁지 않음. 그뿐만이 아님. 사람, 사물, 동물, 원자 할 것 없이, 깨지고 어긋난 우주의 모든 조각들이 그분의 죽음, 십자가에서 쏟으신 그분의 피 덕분에 제자리를 찾아서 생생한 조화를 이룸.",
   "바로 너네가 하나님이 하시는 일의 실제 사례임. 한때 너네는 하나님한테 등을 돌리고, 하나님을 반항하는 마음으로 생각하고, 기회만 있으면 하나님을 괴롭혔음. 근데 그리스도가 십자가에서 자기를 완전히 내어주고 너네를 위해 진짜 죽으심으로, 너네를 하나님의 편으로 데려오셨고, 너네 삶을 온전하고 거룩하게 하나님 앞에 세우셨음. 이런 선물은 그냥 버리고 떠나면 안 됨! 믿음의 끈을 꼭 잡고 흔들림 없이 서서, 계속 메시지에 주파수를 맞추고, 딴 데로 새거나 흐트러지지 않게 조심해야 함. 다른 메시지는 없음. 이 메시지뿐임. 하늘 아래 모든 피조물이 이 메시지를 받음. 나 바울은 이 메시지의 심부름꾼임.",
   "이 감옥에 너네가 아니라 내가 앉아 있는 게 얼마나 감사한지 알아줬으면 좋겠음. 이 세상에는 받아들여야 할 고난이 많음 \u2014 그리스도가 짊어지시는 그런 고난 말이야. 교회가 겪는 그 고난에 내가 동참할 기회를 기쁘게 환영함. 이 교회의 일꾼이 되면서, 나는 이 고난을 순수한 선물로 경험했음. 너네를 섬기고 온전한 진리를 전하게 하시는 하나님의 방법이 바로 이거였음.",
   "이 비밀은 오랫동안 어둠 속에 감춰져 있었지만, 지금은 환하게 드러났음. 하나님은 유대인뿐만 아니라 모든 사람이, 배경이나 종교가 어떻든 간에, 이 가득하고 영광스러운 비밀을 속속들이 알기를 원하셨음. 이 비밀을 한 줄로 말하면 이거임: 그리스도가 너네 안에 계시니까, 하나님의 영광에 참여할 것을 기대할 수 있다는 거. 이렇게 단순함. 이게 우리 메시지의 핵심임. 우리는 그리스도를 전하면서, 메시지에 뭘 더 보태지 말라고 사람들에게 경고함. 깊은 분별력으로 가르쳐서, 각 사람을 성숙하게 만듦. 성숙하다는 건 기본으로 돌아가는 거임. 그리스도! 그 이상도 그 이하도 아님. 내가 날마다, 해마다 그렇게 열심히 일하는 이유가 바로 그거임. 하나님이 넘치게 주시는 힘으로 최선을 다하는 거지.",
  ],
  "verseRanges": ["1-2","3-5","3-5","5-8","9-12","13-14","15-18","15-18","18-20","21-23","24-25","26-29"],
  "msg_ranges": ["1-2","3-5","5-8","9-12","13-14","15-18","18-20","21-23","24-25","26-29"],
  "merges": [],
  "splits": [
   {"msg_range": "5", "paras": [2, 3], "note": "MSG 원문이 5절을 3-5와 5-8 두 문단에 걸쳐 사용 \u2014 KO도 MSG 문단 구분 그대로 따름"},
   {"msg_range": "18", "paras": [7, 8], "note": "MSG 원문이 18절을 15-18과 18-20 두 문단에 걸쳐 사용 \u2014 KO도 MSG 문단 구분 그대로 따름"}
  ],
  "changes": [
   "EN 최종본을 1:1 번역 (12문단, 배지·§헤더 동일). MSG 섹션 헤더: '§그분의 밭에서 일하기'(3-5), '§모든 것을 하나로 묶는 그리스도'(15-18)",
   "MSG 복원 내용 반영: '예수님을 진짜로 따르는 찐 팔로워들'(1-2), '이 메시지를 더 원하게 됐음'(5-8), '내가 항상 믿는 사람'(Epaphras, 5-8), '주님의 밭'(9-12), '날마다, 해마다'(26-29)",
   "원칙 5: 비속어·과도한 슬랭 없이 teen-friendly 한국어로 순화"
  ],
  "confirmations_needed": [],
  "review_status": "msg_audited"
 },
 {
  "chapter": 2,
  "title": "놀아나지 마",
  "paragraphs": [
   "알아줬으면 좋겠어. 내가 너네랑 라오디게아에 있는 크리스천들을 위해 내가 할 수 있는 만큼 열심히 일하고 있다는 거. 너네 중에 나 직접 본 사람은 별로 없겠지만, 그건 하나도 중요하지 않아. 내가 너네 편이고 바로 옆에 있다는 것만 알아둬. 너네 혼자가 아님.",
   "내가 바라는 건, 너네가 사랑으로 촘촘히 하나로 엮여서, 하나님을 알아가는 모든 경지에 이르는 거야. 그러면 너네 마음이 확신과 평안을 얻고, 하나님의 위대한 비밀인 그리스도한테 딱 꽂히게 될 거임. 모든 지혜와 지식의 가장 값진 보물이 그 비밀 안에 다 들어 있거든. 다른 데서는 절대 못 찾음. 이제 그 비밀이 우리한테 환하게 공개됐음! 내가 이 말을 왜 하냐면, 누가 너네를 꼬드겨서 이상한 길로 끌고 다니며 다른 비밀 같은 거나 '비밀' 같은 걸 쫓게 하고 싶지 않아서야.",
   "나 멀리 떨어져 있고, 너네가 날 직접 못 볼 수도 있지만, 믿어줘. 난 너네 편이고 바로 옆에 있음. 너네가 조심스럽고 질서 있게 잘하고 있다는 소식 듣고 완전 기뻤고, 그리스도를 향한 너네 믿음이 완전 단단한 거에 감동했음.",
   "\u00a7그림자에서 실체로",
   "그냥 심플하게 말할게. 너네가 이미 받은 거 가지고 쭉 나아가. 너네는 그리스도 예수, 우리 주님을 받아들였잖아. 그러니까 이제 그분을 살아내는 거임. 너네는 그분 안에 깊이 뿌리 내렸고, 그분 위에 단단히 세워졌음. 믿음의 플레이북은 이미 알잖아. 이제 나가서 뛰어! 수업은 끝났어. 공부 그만하고 배운 대로 살아! 그리고 너네 삶이 감사로 넘치게 하라고.",
   "있어 보이는 척 어려운 말로 너네 꼬시려는 사람들 조심해. 걔네는 아무 결론도 안 나는 끝없는 논쟁에 너네를 끌어들이려고 함. 인간들이 만든 헛된 전통이나 영적인 존재에 대한 헛된 미신으로 자기 생각을 퍼뜨리는 애들임. 근데 그건 그리스도의 길이 아님. 하나님의 모든 게 그분 안에 표현돼 있어서, 너네는 그분을 완전 명확하게 보고 들을 수 있음. 그리스도의 충만함을 알고, 그분 없이는 우주가 텅 비었다는 걸 아는 데 망원경이나 현미경, 점성술 같은 건 하나도 필요 없음. 그분한테 다가가기만 하면 그 충만함이 너네한테도 모이는 거임. 그분의 능력은 모든 것 위에 미침.",
   "그 충만함에 들어가는 건 깨닫거나 해내서 되는 게 아님. 할례를 받거나 율법 조항들을 지키는 문제가 아님. 아니, 너네는 이미 들어와 있음 \u2014 안에 있는 사람들이라고. 무슨 비밀스러운 입회 의식을 통해서가 아니라, 그리스도가 너네를 위해 이미 겪으신 일, 죄의 권세를 파괴하신 일을 통해서 된 거임. 입회 의식 같은 걸 찾는다면, 너네는 이미 세례 받으면서 그 의식을 치렀음. 물속으로 들어간 건 옛날 삶을 장사 지낸 거고, 물에서 나온 건 부활한 거임. 하나님이 그리스도를 살리셨던 것처럼 너네를 죽은 자들 가운데서 살리셨음. 죄 때문에 죽은 옛날 삶에 묶여 있을 때는 하나님한테 반응할 수가 없었음. 근데 하나님이 너네를 그리스도랑 함께 살리셨다고! 생각해봐! 모든 죄가 용서받았고, 기록이 완전 깨끗해졌고, 너네를 체포하려던 옛 구속 영장은 취소돼서 그리스도의 십자가에 못 박혔음. 그분은 우주의 모든 영적 폭군들의 가짜 권위를 십자가에서 다 벗겨내고, 그들을 벌거벗겨 거리로 행진하게 하셨음.",
   "그러니까 음식, 예배 방식, 축일 같은 세세한 걸로 너네를 압박하는 사람들은 그냥 냅둬. 그런 건 다 앞으로 올 것의 그림자일 뿐임. 진짜 실체는 그리스도야.",
   "너네 삶을 조종하려고 굽실거리게 만들고, 천사에 빠져서 환상 같은 걸 쫓으라고 강요하는 사람들은 받아주지 마. 걔네는 허풍만 가득한 애들임. 그게 걔네 전부야. 걔네는 생명의 원천이신 그리스도랑은 아무 상관없음. 그분은 우리를 하나로 온전히 묶어주시고, 그분의 숨결과 피가 우리를 통해 흐르고 있음. 그분은 머리시고 우리는 몸임. 그분이 영양을 공급해주실 때만 우리는 하나님 안에서 건강하게 자랄 수 있음.",
   "그리스도랑 함께 저런 잘난 척하고 유치한 종교는 다 버렸잖아. 근데 왜 아직도 그런 거에 휘둘리고 있어? '이거 만지지 마! 저거 맛보지 마! 이 근처에도 오지 마!' 오늘 있다가 내일 사라질 것들이 그 정도로 신경 쓸 가치가 있다고 생각해? 한껏 목소리 깔고 말하면 좀 있어 보이긴 하지. 경건하고 겸손하고 금욕적인 것처럼 보이기도 하고. 근데 그건 다 자기를 과시하고 중요해 보이려는 또 다른 방법일 뿐임.",
  ],
  "verseRanges": ["1","2-4","5","6-7","6-7","8-10","11-15","16-17","18-19","20-23"],
  "msg_ranges": ["1","2-4","5","6-7","8-10","11-15","16-17","18-19","20-23"],
  "merges": [],
  "splits": [],
  "changes": [
   "EN 최종본을 1:1 번역 (10문단, 배지·§헤더 동일). MSG 섹션 헤더: '§그림자에서 실체로'(6-7)",
   "MSG 'spiritual tyrants' → '영적 폭군들'로 순화 번역 (원칙 5)",
   "MSG 복원 내용 반영: '수업은 끝났어. 공부 그만하고 배운 대로 살아'(6-7), '현미경'(8-10), '그분의 숨결과 피가 우리를 통해 흐르고 있음'(18-19), '경건하고 겸손하고 금욕적인'(20-23)",
   "원칙 5: 비속어·과도한 슬랭 없이 teen-friendly 한국어로 순화"
  ],
  "confirmations_needed": [],
  "review_status": "msg_audited"
 },
 {
  "chapter": 3,
  "title": "인생 레벨업",
  "paragraphs": [
   "\u00a7너의 생명이신 그분",
   "너네가 그리스도랑 함께하는 이 새로운 부활 라이프를 진심으로 살고 싶으면, 그렇게 살아. 그리스도가 다스리시는 것들을 추구해. 질질 끌려다니면서 땅만 쳐다보거나 눈앞에 있는 것들에 정신 팔지 마. 위를 보고 그리스도 주변에서 무슨 일이 일어나는지 주목해. 진짜 중요한 일은 바로 거기서 터지고 있거든. 그분의 시각으로 세상을 봐.",
   "너네 옛날 인생은 끝났어. 너네의 새로운 삶, 진짜배기 삶은 구경꾼들 눈에는 안 보이겠지만, 하나님 안에서 그리스도랑 함께하는 삶이야. 그분이 바로 너네 생명이야. 기억해. 너네 진짜 생명이신 그리스도가 이 세상에 다시 나타나실 때, 너네도 나타날 거야 \u2014 진짜 너, 완전 멋진 너로. 그때까지는 그리스도가 그랬던 것처럼 알려지지 않아도 만족하면서 살아.",
   "이건 죽음의 길과 관련된 모든 걸 끊어버리라는 뜻이야. 불륜, 더러운 짓, 욕정, 하고 싶은 대로 다 하려는 마음, 맘에 드는 건 다 가지려는 마음 같은 거 말이야. 그런 삶은 하나님이 아니라 물질과 감정이 만들어낸 삶이야. 하나님은 이런 것 때문에 완전 폭발하실 거야. 얼마 전까지만 해도 너네는 더 나은 걸 몰라서 그런 짓들을 하고 다녔지. 근데 이제 아니까, 그 모든 걸 영원히, 확실하게 버려. 분노, 욱하는 성격, 심술, 막말, 무례한 말 같은 거 다 버리라고.",
   "서로 거짓말하지 마. 너네는 그 옛날 삶이랑 끝냈잖아. 그건 안 맞는 더러운 옷 같아서 이미 벗어서 불 속에 던져버렸음. 이제 너네는 새 옷을 입었어. 너네의 새로운 생활 방식은 창조주가 하나하나 맞춤 제작해서 직접 라벨까지 붙여주신 거야. 이제 낡은 유행은 다 끝났어. 유대인, 이방인, 종교인, 비종교인, 인싸, 아싸, 야만인, 교양 없는 사람, 노예, 자유인 같은 단어들은 이제 아무 의미 없어. 이제부터 모든 사람은 그리스도로 정해지고, 그리스도 안에 속해 있는 거야.",
   "하나님이 새로운 사랑의 삶을 살라고 너네를 뽑았으니까, 하나님이 너네를 위해 골라주신 옷을 입어. 긍휼, 친절, 겸손, 조용한 힘, 절제. 평온한 마음을 유지하고, 2등도 만족하고, 기분 상하는 일이 있어도 바로 용서해줘. 주님이 너네를 용서하신 것처럼, 빠르고 완전하게 용서하라고. 그리고 뭘 입든지 간에 사랑을 입어. 사랑이야말로 너네가 어떤 상황에서든 기본으로 갖춰 입어야 할 옷이야. 사랑 없이 하는 일은 없게 해.",
   "그리스도의 평화가 너네를 조화롭게 하고 발맞추게 해줘. 딴 데로 새서 자기 일에만 빠지지 마. 그리고 감사하는 마음을 길러. 그리스도의 말씀, 곧 메시지가 너네 집안을 마음껏 휘젓고 다니게 해. 너네 삶에 충분한 자리를 내줘. 분별 있게 서로 가르치고 이끌어줘. 마음을 다해 하나님을 노래하고 찬양해! 살면서 말이나 행동이나 뭐든지 주 예수의 이름으로 하고, 한 걸음 뗄 때마다 하나님 아버지께 감사해.",
   "아내들아, 남편을 이해하고 지지해줘. 주님을 기쁘게 하는 방식으로 남편한테 순종해.",
   "남편들아, 아내를 진심으로 사랑해. 아내를 함부로 대하지 마.",
   "자녀들아, 부모님이 하시는 말씀 잘 들어. 그게 주님을 엄청 기쁘게 하는 일이야.",
   "부모들아, 자녀들을 너무 심하게 몰아붙이지 마. 애들 기죽일 수 있잖아.",
   "종으로 일하는 사람들은, 이 세상 주인이 시키는 대로 잘 따라. 대충 하지 말고, 최선을 다해. 마음을 다해서 일해. 너네 진짜 주인이신 하나님께 하듯 말이야. 유산을 상속받을 때 충분히 보상받을 거라고 믿어. 너네가 궁극적으로 섬기는 주인은 예수님이라는 걸 항상 기억해. 대충 일하는 불성실한 종은 그 책임을 지게 될 거야. 예수님 따른다고 해서 일 못해도 봐주는 거 없어.",
  ],
  "verseRanges": ["1-2","1-2","3-4","5-8","9-11","12-14","15-17","18","19","20","21","22-25"],
  "msg_ranges": ["1-2","3-4","5-8","9-11","12-14","15-17","18","19","20","21","22-25"],
  "merges": [],
  "splits": [],
  "changes": [
   "EN 최종본을 1:1 번역 (12문단, 배지·§헤더 동일). MSG 섹션 헤더: '§너의 생명이신 그분'(1-2)",
   "MSG 복원 내용 반영: '마음을 다해서 일해'(22-25, MSG 'Work from the heart')",
   "원칙 5: 비속어·과도한 슬랭 없이 teen-friendly 한국어로 순화"
  ],
  "confirmations_needed": [],
  "review_status": "msg_audited"
 },
 {
  "chapter": 4,
  "title": "마지막 인사들",
  "paragraphs": [
   "주인들아, 너네 밑에서 일하는 사람들한테 잘해줘. 공정하게 대해주라고. 너네도 하늘에 계신 주인, 하나님을 섬기고 있다는 거 절대 잊지 마.",
   "\u00a7열린 문을 위해 기도해",
   "기도 열심히 하고, 감사하는 마음으로 정신 바짝 차리고 있어. 내가 지금 감옥에 있긴 하지만, 하나님이 문을 활짝 열어주셔서 그리스도의 비밀을 전할 수 있게 기도해줘. 내가 입만 열면 사람들한테 그리스도가 완전 선명하게 드러나게 말이야.",
   "교회 밖 사람들하고 지낼 때는 머리를 잘 써. 절대 놓치는 거 없이, 모든 기회를 알차게 써먹어. 말할 때는 은혜롭게 하고, 대화에서는 남을 깎아내리거나 밀어내지 말고 상대의 좋은 점을 끌어내는 걸 목표로 삼아.",
   "내 착한 친구 두기고가 내 소식을 다 알려줄 거야. 그는 주님을 섬기는 일에 완전 믿음직한 동료거든. 내가 걔를 보낸 건 너네한테 우리 사정을 알리고 너네 믿음을 응원해주려는 거임. 오네시모도 걔랑 함께 보냈어. 걔는 너네 고향 사람이고 완전 믿음직한 형제가 됐음! 걔네가 여기서 있었던 일 전부 다 말해줄 거야.",
   "나랑 같이 감옥에 있는 아리스다고가 안부 전한다. 바나바 사촌 마가도 안부 전함 (전에 걔에 대한 편지 받았지? 걔가 너네한테 가면 잘 챙겨줘). 유스도라고 불리는 예수도 안부 전하고. 예전에 같이 일하던 사람들 중에 나 안 떠나고 남아서 하나님 나라를 위해 일한 사람은 얘네밖에 없음. 얘네가 얼마나 큰 힘이 됐는지 모른다니까!",
   "너네 고향 사람인 에바브라도 안부 전한다. 그는 진짜 대단한 용사임! 너네를 위해 계속 기도해 온 사람이거든. 너네가 굳게 서서 하나님이 원하시는 모든 일을 성숙하고 확신 있게 하기를 기도하고 있어. 내가 걔를 쭉 지켜봤는데, 너네랑 라오디게아, 히에라볼리에 있는 사람들을 위해 얼마나 열심히 일했는지 내가 증명할 수 있음.",
   "좋은 친구이자 의사인 누가랑 데마도 인사한다.",
   "라오디게아에 있는 우리 친구들한테 안부 전해줘. 눔바랑 그 집에서 모이는 교회에도 안부 전해주고.",
   "이 편지 다 읽고 나면 라오디게아 교회도 읽게 해줘. 그리고 라오디게아로 간 편지도 받아서 너네가 읽어봐.",
   "그리고 아킵보한테는 '주님한테 받은 임무, 진짜 최선을 다해서 해. 완전 진심으로!'라고 전해줘.",
   "나 바울이 직접 사인한다. 감옥에 갇힌 나를 위해 기도하는 거 잊지 마. 은혜가 너네랑 함께하길 바란다.",
  ],
  "verseRanges": ["1","2-4","2-4","5-6","7-9","10-11","12-13","14","15","16","17","18"],
  "msg_ranges": ["1","2-4","5-6","7-9","10-11","12-13","14","15","16","17","18"],
  "merges": [],
  "splits": [],
  "changes": [
   "EN 최종본을 1:1 번역 (12문단, 배지·§헤더 동일). MSG 섹션 헤더: '§열린 문을 위해 기도해'(2-4)",
   "MSG 7-9 단일 문단으로 통합 (기존 KO raw는 두기고/오네시모를 2문단으로 나누고 배지 누락이었음)",
   "MSG 복원 내용 반영: '절대 놓치는 거 없이'(5-6, MSG \"Don't miss a trick\"), '굳게 서서'(12-13, MSG 'stand firm'), '라오디게아로 간 편지'(16)",
   "원칙 5: 비속어·과도한 슬랭 없이 teen-friendly 한국어로 순화"
  ],
  "confirmations_needed": [],
  "review_status": "msg_audited"
 }
]

if __name__ == "__main__":
    with open("fixes/en_Colossians.json", "w", encoding="utf-8") as f:
        json.dump(EN, f, ensure_ascii=False, indent=1)
        f.write("\n")
    with open("fixes/ko_Colossians.json", "w", encoding="utf-8") as f:
        json.dump(KO, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("wrote fixes/en_Colossians.json and fixes/ko_Colossians.json")
