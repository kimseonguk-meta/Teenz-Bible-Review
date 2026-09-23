#!/usr/bin/env python3
"""2 Corinthians MSG audit build script. Generates fixes/en_2Corinthians.json and fixes/ko_2Corinthians.json."""
import json

EN_CH = []
KO_CH = []

# ============ CHAPTER 1 ============
EN_CH.append({
"chapter": 1, "title": "God's Got Your Back",
"paragraphs": [
"Hey, it's Paul, on a special mission from Jesus himself, all part of God's master plan. I'm writing this to all the believers in Corinth and the whole Achaia area. Hope you're getting all the awesome perks from God our Father and our main man, Jesus. And Timothy, someone you know and trust, is here with me too.",
"§The Rescue",
"Shout-out to the God and Father of our Lord, Jesus Christ! He's the Father of mercy and the God of all comfort. When we're going through tough times, he's right there with us. And then, before we even realize it, he brings us alongside someone else who's going through hard times, so we can be there for that person just like God was there for us. Following Jesus can be rough, for sure, but the good times he gives us, the healing and comfort, are just as real. We get a full dose of that too.",
"When we have a hard time, it's actually for your benefit, so you can be saved. And when we're doing good, that's for you too, to keep you going and not give up. Your struggles are our struggles. When we see you guys sticking it out through the hard times, just like you enjoy the good times, we know you're gonna be alright. No doubt.",
"We gotta tell you, it was rough for us in Asia. We seriously thought we were done for, like we were on death row. But it turned out to be a good thing. Instead of relying on ourselves, we had to put all our trust in God. And since he's the one who can raise the dead, that's a pretty solid plan. He saved us from what looked like certain doom, and he'll do it again, as many times as we need. And you guys were a part of it too, with your prayers. We don't want you to forget that. We can just imagine you all, cheering for us and thanking God for getting us through it. Your prayers were a huge part of our rescue mission.",
"Now that we're through the worst of it, we're glad to say we came out with our faith and integrity intact. We can look you in the eye and be proud. But it wasn't because of anything we did. It was God who kept us on track. Don't try to read between the lines in this letter. We're telling you the straight-up truth. We hope you can see the whole picture now, not just bits and pieces. We want you to be as proud of us as we are of you when we all stand before Jesus.",
"I was so sure you guys would be cool with it, I was planning to visit you twice. Once on my way to Macedonia, and then again on my way back. We could've had a big send-off party before I went to Judea. That was the plan, anyway.",
"So now you're gonna say I'm a flip-flopper because things changed? You think I say one thing and do another? Nah, that's not me. I try to be as real as God is. We didn't give you a half-hearted 'yes' and then a 'whatever' 'no'. When Silas, Timothy, and I told you about Jesus, was there any doubt? It was a solid 'yes'!",
"Everything God has ever promised is a 'yes' in Jesus. That's what we preach, and that's what we pray. It's God's 'yes' and our 'yes' all together. God makes us strong in Christ and puts his 'yes' inside of us. He's put his Spirit in us as a down payment on everything he's promised to do.",
"So, you wanna know the real reason I didn't come to Corinth? I swear to God, it was to spare you any more drama. I was trying to be cool, not a bully.",
"We're not trying to be your bosses and tell you how to live your faith. We're in this with you, and we're excited to see what God does. We know you've got your own faith, and that's what matters.",
],
"verseRanges": ["1-2","3-5","3-5","6-7","8-11","12-14","15-16","17-19","20-22","23","24"],
"msg_ranges": ["1-2","3-5","6-7","8-11","12-14","15-16","17-19","20-22","23","24"],
"merges": [], "splits": [],
"changes": [
"Header renamed: invented §Comfort in Suffering → MSG's §The Rescue, moved to MSG position between v2 and v3, sharing badge 3-5 with the following body paragraph",
"Badge fix: 15-17 → 15-16 (MSG groups 15-16)",
"Badge fix: 23-24 → 24 (MSG 24)",
"Restored 3-5: 'the good times of his healing comfort — we get a full measure of that, too' (was softened to 'way better')",
],
"confirmations_needed": [],
})
KO_CH.append({
"chapter": 1, "title": "네 편이 돼주시는 하나님",
"paragraphs": [
"안녕, 나 바울이야. 예수님이 직접 주신 특별 미션을 받고 온 거야, 하나님이 직접 계획하신. 고린도에 있는 하나님의 교회랑 아가야 지방에 있는 모든 믿는 친구들한테 이 편지를 써. 우리 아버지 하나님이랑 주 예수 그리스도가 주시는 모든 선물과 은혜가 다 너희 거 되길 바랄게! 너희도 잘 알고 믿는 디모데가 나랑 같이 있어.",
"§구출 작전",
"우리 주 예수 그리스도의 아버지이신 하나님을 찬양하자! 자비로우신 아버지! 모든 위로의 하나님이셔! 우리가 힘든 시간을 보낼 때 그분이 우리 곁에 와주시고, 어느새 우리도 힘든 시간을 보내는 다른 사람 곁에 서서, 하나님이 우리에게 해주신 것처럼 그 사람을 위해 곁에 있어 주게 하셔. 메시아를 따르면서 힘든 일이 많긴 하지만, 그분의 치유와 위로가 주는 좋은 시간도 그만큼 많아. 우리도 그걸 완전 넉넉하게 받고 있거든.",
"우리가 예수님 때문에 고생하는 건 결국 너희가 치유받고 구원받게 하려는 거야. 우리가 잘 대접받고 도움의 손길이랑 격려의 말을 받는 것도 너희한테 좋은 일이야. 그게 너희가 앞만 보고 흔들리지 않고 나아가게 해주거든. 너희가 힘든 건 우리도 힘든 거야. 너희가 좋은 시간을 누리는 것처럼 힘든 시간도 기꺼이 견뎌내는 걸 보면, 너희가 분명 잘 해낼 거라는 걸 알 수 있어. 의심할 여지가 없어.",
"친구들아, 아시아에서 우리한테 닥친 일이 얼마나 힘들었는지 솔직히 말해줄게. 진짜 못 버티겠다 싶을 정도였어. 사형선고를 받은 것 같았고, 모든 게 끝난 줄 알았지. 근데 알고 보니까 그게 일어날 수 있는 최고의 일이었어. 우리 힘과 지혜로 빠져나오려고 애쓰는 대신, 하나님을 완전히 신뢰할 수밖에 없게 됐거든. 죽은 사람을 살리시는 하나님이시니까 나쁜 선택은 아니지! 그분이 실제로 해주셨어. 확실한 죽음에서 우리를 구해주신 거야. 그리고 앞으로도 또 해주실 거야. 우리가 구원이 필요할 때마다 몇 번이든 구해주실 거야. 너희와 너희 기도도 그 구출 작전의 일부야. 그 점도 알아줬으면 좋겠어. 우리를 구해주신 하나님께 찬양을 올리는 너희 얼굴이 지금도 눈에 선해. 너희 기도가 우리 구출에 그렇게 중요한 역할을 했어.",
"이제 최악은 지났으니까, 양심이랑 믿음을 깨끗하게 지키고 이 상황을 빠져나왔다는 걸 기쁘게 보고할 수 있어. 세상을 마주할 수 있고, 더 중요한 건 너희를 고개 들고 당당하게 마주할 수 있어. 근데 그게 우리가 뭘 잘해서 된 게 아냐. 하나님이 우리를 그분께 집중하게 해주시고 타협하지 않게 지켜주신 거야. 이 편지에서 행간을 읽거나 숨은 뜻을 찾으려 하지 마. 우리는 꾸밈없이 솔직한 진실만 쓰고 있어. 너희가 디테일을 본 것처럼 이제 전체 그림도 보길 바라. 우리가 너희를 자랑스러워하는 것처럼, 너희도 우리를 자랑스러워해주길 바라. 우리 주 예수님 앞에 함께 설 때 말야.",
"너희가 날 환영해줄 거라 확신해서, 원래 너희를 두 번 방문할 멋진 계획을 세웠었어. 마케도니아로 가는 길에 들렀다가, 돌아오는 길에 또 들르는 거지. 그러면 너희가 나를 유대로 배웅해주는 환송 파티도 할 수 있었을 텐데. 그게 원래 계획이었어.",
"일이 계획대로 안 됐다고 이제 와서 내가 약속을 뒤집는 변덕쟁이라고 비난할 거야? 내가 한 입으로 두 말 하는 사람이라고 생각해? 이랬다 저랬다 하는 가벼운 '응'이랑 '아니'라고? 틀렸어. 나는 하나님이 자기 말씀에 신실하신 것처럼 내 말에 신실하려고 노력해. 너희에게 한 우리 말이 경솔한 '응'을 무심한 '아니'로 취소한 게 아냐. 그럴 리가 없지. 실라랑 디모데랑 내가 너희 가운데 하나님의 아들을 전했을 때, 왔다 갔다 하는 모호함을 느꼈어? 깨끗하고 확실한 '응' 아니었어?",
"하나님이 약속하신 모든 건 예수의 '응'으로 도장이 찍혀 있어. 그분 안에서 우리가 전하고 기도하는 게 바로 그거야. 위대한 아멘, 하나님의 '응'과 우리의 '응'이 함께, 눈부시게 분명하게. 하나님이 우리를 확증하시고 그리스도 안에서 우리를 확실한 존재로 만드시며, 그분의 '응'을 우리 안에 새겨 넣으셔. 그분의 영으로 우리에게 영원한 약속을 도장으로 찍어주셨어. 그분이 완성하실 일의 확실한 시작인 거지.",
"자, 내가 고린도에 안 간 진짜 이유 들을 준비 됐어? 하나님을 증인으로 걸고 말하는데, 내가 안 간 유일한 이유는 너희 고통을 덜어주려고였어. 너희를 배려한 거지, 무관심해서도 아니고 조종하려고 그런 것도 아냐.",
"우리는 너희가 신앙을 어떻게 살아내는지 관리하는 사람이 아냐. 어깨 너머로 의심스럽게 감시하는 사람도 아니고. 우리는 너희와 함께 일하는 동료야, 기쁘게 기대하면서. 너희는 우리의 믿음이 아니라 너희 자신의 믿음으로 서 있다는 걸 알아.",
],
"verseRanges": ["1-2","3-5","3-5","6-7","8-11","12-14","15-16","17-19","20-22","23","24"],
"msg_ranges": ["1-2","3-5","6-7","8-11","12-14","15-16","17-19","20-22","23","24"],
"merges": [], "splits": [],
"changes": [
"EN 구조 반영: 헤더를 MSG 위치(2절과 3절 사이)로 이동, §구출 작전",
"배지 수정: 15-16, 24 (EN과 동일)",
"3-5 복원: '치유와 위로가 주는 좋은 시간도 그만큼 많아'",
],
"confirmations_needed": [],
})

# ============ CHAPTER 2 ============
EN_CH.append({
"chapter": 2, "title": "No Drama, Just Love",
"paragraphs": [
"Hey, so I decided not to roll through again and make things awkward for everyone. Like, if I showed up and it was all tense, how could you guys even make me feel better?",
"That's why I sent that letter instead of just showing up. I didn't want to have a bummer of a time with the very people I was hoping would hype me up. I was sure that what was good for me was good for you. Honestly, writing that letter was rough. More tears than ink, for real. But I wasn't trying to start drama. I wrote it so you'd know how much I've got your backs. For real, it's all love.",
"About the guy who started all this mess... you know who I'm talking about. He didn't just hurt me, he hurt pretty much all of you. So I'm not gonna go all hard on him. The punishment you guys decided on is enough. It's time to forgive him and help him get back up. If you just keep piling on the guilt, you're gonna crush him. My advice? Show him some love.",
"My letter wasn't about getting revenge on the guy. It was about you guys stepping up and taking care of our crew. So if you forgive him, I forgive him. I'm not holding any grudges. I'm on your team with this forgiveness thing, and Christ is with us, showing us the way. We don't want to give the enemy an opening to cause more trouble. We're not clueless, we know his tricks.",
"§An Open Door",
"When I got to Troas to spread the word about Jesus, it was wide open. God had opened the door for me. But when I didn't see my boy Titus there with an update on you guys, I couldn't chill. I was worried about you, so I bounced and went to Macedonia to find him and get some good news. And I did, thank God!",
"In Jesus, God leads us in a never-ending victory parade. Through us, he spreads the knowledge of Christ. Everywhere we go, people breathe in the amazing fragrance. Because of Christ, we give off a sweet scent rising to God. To those on the way to salvation, it's an aroma full of life. But to those on the way to destruction, we smell like a rotting corpse.",
"That's a huge responsibility. Who's good enough for that? Nobody, but at least we're not watering down God's word and selling it cheap on the street. We stand in Christ's presence when we speak; God looks us in the face. We get what we say straight from God and say it as honestly as we can.",
],
"verseRanges": ["1-2","3-4","5-8","9-11","12-14","12-14","14-16","16-17"],
"msg_ranges": ["1-2","3-4","5-8","9-11","12-14","14-16","16-17"],
"merges": [],
"splits": [
{"msg_range": "14", "paras": [5,6], "note": "MSG overlaps v14 between 12-14 and 14-16"},
{"msg_range": "16", "paras": [6,7], "note": "MSG overlaps v16 between 14-16 and 16-17"},
],
"changes": [
"Split old [1-4] para into separate [1-2] and [3-4] paras (MSG groups them as separate paragraphs)",
"Badge fix: 12-13 → 12-14 (MSG 12-14)",
"Split old [14-17] para into [14-16] and [16-17] (MSG separate paragraphs; v16 overlaps in MSG)",
"Header replaced: invented §Paul Changes Plans → MSG's §An Open Door at MSG position, badge 12-14",
"Restored 14-16: 'Through us, he spreads the knowledge of Christ' (was 'he flexes his power')",
"Restored 16-17: 'We get what we say straight from God and say it as honestly as we can'",
],
"confirmations_needed": [],
})
KO_CH.append({
"chapter": 2, "title": "드라마 말고, 사랑으로",
"paragraphs": [
"그래서 나는 우리 둘 다 괴롭게만 할 방문은 다시 안 하기로 결정했어. 내가 그냥 나타나기만 해도 너희를 민망하고 고통스럽게 만들 텐데, 그러면 너희가 어떻게 날 응원하고 기운 나게 해주겠어?",
"그래서 직접 가는 대신 편지를 쓴 거야. 나를 응원해줄 거라 기대했던 친구들을 실망시키면서 괴로운 시간을 보내고 싶지 않았거든. 그 편지를 쓸 때만 해도 나한테 좋은 게 너희한테도 좋을 거라고 확신했어. 근데 알고 보니 그 편지를 쓰는 것만으로도 충분히 고통스러웠어. 종이에 잉크보다 눈물이 더 많았거든. 하지만 고통 주려고 쓴 게 아냐. 내가 너희를 얼마나 아끼는지, 아끼는 걸 넘어 얼마나 사랑하는지 알게 하려고 쓴 거야!",
"이제 이 모든 일을 일으킨 그 사람, 그 문제의 인물에 대해 말해볼게. 상처받은 게 나 혼자만이 아니라, 몇 명 빼고는 너희 모두라는 걸 알아줬으면 좋겠어. 그래서 너무 심하게 몰아붙이고 싶진 않아. 너희 대부분이 동의한 처벌이면 충분해. 이제는 그 사람을 용서하고 다시 일어설 수 있게 도와줄 시간이야. 죄책감만 계속 들이부으면 그를 익사시킬 수도 있어. 내 조언은 사랑을 들이부으라는 거야.",
"내 편지의 초점은 그 사람을 벌주는 게 아니라, 너희가 교회의 건강을 위해 책임을 지게 하는 거였어. 그러니까 너희가 그를 용서하면 나도 용서할게. 내가 개인적인 원한 리스트를 들고 다닌다고 생각하지 마. 그리스도가 우리와 함께 우리를 이끄시는 것처럼, 나도 용서하는 너희와 함께할 거야. 결국 사탄이 몰래 더 큰 장난을 칠 틈을 주고 싶지 않거든. 우린 사탄의 교활한 수법을 잘 알고 있잖아!",
"§열린 문",
"메시아의 메시지를 전하러 드로아에 도착했을 때, 그곳은 완전히 열려 있었어. 하나님이 문을 열어두신 거야. 나는 그냥 그 문으로 걸어 들어가기만 하면 됐지. 근데 너희 소식을 들고 기다리고 있던 디도를 못 만나서 마음이 편하지 않았어. 너희가 걱정돼서 떠나 마케도니아로 갔어. 디도를 찾아서 너희에 대한 든든한 소식을 듣고 싶었거든. 그리고 들었어, 하나님께 감사하게도!",
"메시아, 곧 그리스도 안에서 하나님은 우리를 이곳저곳으로 데리고 다니시며 끝없는 승리의 행진에 참여시키셔. 우리를 통해 그분은 그리스도를 아는 지식을 전하셔. 우리가 가는 곳마다 사람들은 그윽한 향기를 맡게 돼. 그리스도 덕분에 우리는 하나님께 올라가는 달콤한 향기를 풍기고, 구원의 길에 있는 사람들은 그 향기를 알아봐. 그건 생명의 향기야. 하지만 멸망의 길에 있는 사람들은 우리를 썩은 시체 냄새처럼 여겨.",
"이건 엄청난 책임이야. 이걸 감당할 만한 사람이 누가 있겠어? 없어. 하지만 적어도 우리는 하나님의 말씀을 물 타서 싸구려로 팔아넘기진 않아. 우리는 그리스도 앞에 서서 말해. 하나님이 우리 얼굴을 보고 계시거든. 우리는 하나님께 받은 말을 그대로, 최대한 정직하게 전하는 거야.",
],
"verseRanges": ["1-2","3-4","5-8","9-11","12-14","12-14","14-16","16-17"],
"msg_ranges": ["1-2","3-4","5-8","9-11","12-14","14-16","16-17"],
"merges": [],
"splits": [
{"msg_range": "14", "paras": [5,6], "note": "MSG overlaps v14 between 12-14 and 14-16"},
{"msg_range": "16", "paras": [6,7], "note": "MSG overlaps v16 between 14-16 and 16-17"},
],
"changes": [
"EN 구조 반영: [1-4] 분리, [14-17] 분리, §열린 문 (MSG 위치)",
"배지 수정: 12-14, 14-16, 16-17 (EN과 동일)",
"14-16 복원: '그리스도를 아는 지식을 전하셔'",
],
"confirmations_needed": [],
})

# ============ CHAPTER 3 ============
EN_CH.append({
"chapter": 3, "title": "The Ultimate Transformation",
"paragraphs": [
"Hey, are we trying to flex on you? Like we're bragging about how awesome we are? Nah, that's not it at all. We don't need some fancy recommendation letter to prove we're legit. You guys are our living proof. Your lives are like an open book that anyone can read, and Christ himself is the author. He didn't write on paper, but on your hearts with the Spirit of God. That's the real deal.",
"For real, we're super confident about this. You are our letter of recommendation, written by Christ for God. We could never write something like that about ourselves. Only God can do that. He's the one who gave us the hookup to this new way of life. It's not some boring rulebook that kills your vibe. It's a spiritual upgrade, a total life-changer.",
"§Lifting the Veil",
"The old way, the law of Moses, was like the OG rules. When Moses brought down the stone tablets, his face had an incredible glow. It was so bright that people couldn't even look at him. But that was just a temporary glow. The new way, the way of the Spirit, is a permanent, next-level change.",
"If the old system of condemnation was impressive, how much more impressive is this new system of affirmation? As bright as the old one was, it looks totally dull next to the new one. If a temporary setup impressed us, how much more will this bright, shining, forever government?",
"Because we have this awesome hope, we're not holding anything back. We're not like Moses who had to hide his fading glory. We're putting it all out there. The people back then were clueless. They couldn't see that the old way was losing its power. Even now, when they read the old rules, it's like they're wearing a blindfold. Only Christ can take off the blindfold and show them that the old way is obsolete.",
"But whenever someone turns to God, He takes away the blindfold and they can see Him face-to-face. They realize that God is not some distant, angry guy, but a living, personal God. And when you're in His presence, the old rules don't matter anymore. We're free! There's nothing between us and God. Our faces are shining with His glory. We're going through a powerful shift, becoming more and more like Jesus as God works in our lives.",
],
"verseRanges": ["1-3","4-6","7-8","7-8","9-11","12-15","16-18"],
"msg_ranges": ["1-3","4-6","7-8","9-11","12-15","16-18"],
"merges": [], "splits": [],
"changes": [
"Split old [7-8] para: 9-11 content ('Government of Affirmation... brightly shining government installed for eternity') restored as its own para badged 9-11 (was merged under 7-8 badge)",
"Badge fix: 12-13 → 12-15 (MSG 12-15)",
"Badge fix: 15-16 → 16-18 (MSG 16-18)",
"Header replaced: invented §Forgiveness → MSG's §Lifting the Veil at MSG position, badge 7-8",
],
"confirmations_needed": [],
})
KO_CH.append({
"chapter": 3, "title": "궁극의 변화",
"paragraphs": [
"이게 우리가 자화자찬하는 것처럼 들려? 자격증이라도 있는 양 권위를 내세우는 것 같아? 전혀 아냐. 우리는 너희에게 줄 추천서도, 너희에게 받을 추천서도 필요 없어. 너희 자체가 우리가 필요한 추천서거든. 너희 삶 자체가 누구나 보기만 해도 읽을 수 있는 편지야. 그리스도께서 직접 쓰신 거지. 잉크가 아니라 살아계신 하나님의 영으로, 돌에 새긴 게 아니라 사람의 삶에 새기셨어. 그리고 우리는 그 편지를 배달하는 사람들이야.",
"우리는 이걸 완전 확신해. 그리스도께서 하나님을 위해 직접 쓰신 너희야말로 우리의 추천서야. 우리 스스로는 이런 편지를 쓸 생각도 못 했을 거야. 오직 하나님만이 이런 편지를 쓰실 수 있어. 그분의 편지가 우리에게 이 새로운 계획을 실행할 권한을 준 거야. 그 계획은 종이에 잉크로 쓴 것도 아니고, 페이지마다 법률 주석을 잔뜩 달아 너희 영혼을 죽이는 것도 아냐. 성령으로 영혼에, 그분의 생명으로 우리 삶에 쓰신 거야!",
"§베일을 걷다",
"옛 방식, 모세의 율법은 완전 구시대 룰 같은 거야. 모세가 돌판을 가져왔을 때, 그의 얼굴은 엄청나게 빛났어. 사람들이 그를 똑바로 쳐다볼 수 없을 정도였지. 근데 그건 잠깐의 빛이었어. 새 방식, 성령의 방식은 영원한 차원이 다른 변화야.",
"정죄의 옛 제도가 인상적이었다면, 긍정의 새 제도는 얼마나 더 인상적이겠어? 옛 제도가 눈부셨다고 하지만, 새 제도 옆에 서면 완전 흐릿해 보여. 잠깐 있다 사라질 제도가 그렇게 인상적이었다면, 영원히 세워진 이 빛나는 통치는 얼마나 더 대단하겠어?",
"이런 멋진 희망이 있으니까, 우리는 아무것도 숨기지 않아. 영광이 사라져 가는 걸 가려야 했던 모세와는 달라. 우리는 모든 걸 다 드러내. 그때 사람들은 몰랐어. 옛 방식이 힘을 잃어가고 있다는 걸 보지 못했지. 지금도 옛 규칙을 읽을 때는 눈가리개를 한 것처럼 못 봐. 오직 그리스도만이 그 눈가리개를 벗겨서 옛 방식이 쓸모없다는 걸 보여주실 수 있어.",
"하지만 누군가 하나님께로 돌아서기만 하면, 그분이 눈가리개를 벗겨주셔서 얼굴과 얼굴을 마주하게 돼. 그들은 하나님이 멀리 계신 화난 분이 아니라, 살아계신 인격적인 분이라는 걸 깨닫게 돼. 그분 앞에 있으면 옛 규칙은 더 이상 중요하지 않아. 우리는 자유야! 우리와 하나님 사이에 아무것도 없어. 우리 얼굴은 그분의 영광으로 환하게 빛나. 하나님이 우리 삶에 들어오시고 우리가 그분을 닮아가면서, 우리는 예수님을 닮아가는 강력한 변화를 겪고 있어.",
],
"verseRanges": ["1-3","4-6","7-8","7-8","9-11","12-15","16-18"],
"msg_ranges": ["1-3","4-6","7-8","9-11","12-15","16-18"],
"merges": [], "splits": [],
"changes": [
"EN 구조 반영: [7-8] 분리(9-11 복원), §베일을 걷다",
"배지 수정: 9-11, 12-15, 16-18 (EN과 동일)",
"9-11 복원: '영원히 세워진 이 빛나는 통치'",
],
"confirmations_needed": [],
})

# ============ CHAPTER 4 ============
EN_CH.append({
"chapter": 4, "title": "Seriously, We're Legit",
"paragraphs": [
"§Trial and Torture",
"Hey, so God's been super generous and let us in on his master plan. So, no way are we just gonna quit when things get a little rough. We're not about being fake or playing games. We don't do sneaky stuff behind the scenes, and we're not twisting God's words to make ourselves look good. Nah, we're all about keeping it 100. Everything we do is out in the open for everyone to see, so you can see for yourself that we're legit in God's eyes.",
"If our message seems confusing, it's not 'cause we're hiding anything. It's 'cause some people are just looking in the wrong direction and aren't even trying to get it. They're all about the trendy \"god of darkness,\" thinking he'll give them whatever they want without having to believe in something real. They're totally blind to the awesome light of the message about Jesus, who's like the ultimate picture of God.",
"Just to be clear, this whole thing isn't about us. We're here to tell you about Jesus, the real MVP. We're just the delivery guys, the messengers sent by Jesus for you. It all started when God was like, \"Let there be light!\" and BAM, our lives lit up when we finally got who God was by looking at Jesus. It was a life-changing moment.",
"If you only look at us, you might miss the main event. We're just ordinary guys, like clay pots holding this amazing treasure. That's so nobody gets it twisted and thinks we're the ones with the power. And let's be real, there's no chance of that. We get roughed up and surrounded by problems, but we don't give up. We get confused, but we know God's got the answers. We've been scared out of our minds, but God never ghosted us. We get knocked down, but we're not out. They're doing the same stuff to us that they did to Jesus—roasting us, trying to cancel us—but the same power that raised Jesus is alive in us. We're constantly in danger for Jesus, which just makes his life shine even brighter through us. So while we're going through it, you're getting the benefits.",
"We're not keeping this a secret. Just like the guy in the Psalms who said, \"I believed it, so I said it,\" we're shouting what we believe from the rooftops. And we believe that the same God who brought Jesus back to life will do the same for us, and we'll all be together. Everything that happens is for your benefit and for God's glory. More grace, more people, more praise!",
"So, we're not giving up. No way! Even though it looks like we're falling apart on the outside, on the inside, God is giving us an incredible renewal every single day. These tough times are nothing compared to the epic party that's waiting for us. There's so much more going on than what you can see. The stuff we see now is temporary, but the stuff we can't see is forever.",
],
"verseRanges": ["1-2","1-2","3-4","5-6","7-12","13-15","16-18"],
"msg_ranges": ["1-2","3-4","5-6","7-12","13-15","16-18"],
"merges": [], "splits": [],
"changes": [
"Badge fix: 13-14 → 13-15 (MSG 13-15; v15 'Every detail works to your advantage and to God's glory' now properly badged)",
"Header replaced: invented §The New Covenant → MSG's §Trial and Torture at chapter top, badge 1-2",
],
"confirmations_needed": [],
})
KO_CH.append({
"chapter": 4, "title": "진짜야, 우린 찐이야",
"paragraphs": [
"§시련과 고난",
"하나님이 자기 일을 우리에게 이렇게 넉넉하게 알려주셨는데, 가끔 힘든 일이 생긴다고 해서 손들고 일을 때려칠 생각은 전혀 없어. 우리는 가면 쓰고 장난치는 거 거부해. 뒤에서 꼼수 부리고 조종하는 짓 안 해. 하나님의 말씀을 우리 입맛에 맞게 비틀지도 않아. 오히려 우리가 하고 말하는 모든 걸 사람들 앞에 다 드러내. 진실을 전부 공개해서, 원하는 사람은 하나님 앞에서 보고 스스로 판단할 수 있게 하는 거야.",
"우리 메시지가 헷갈려 보인다면, 그건 우리가 뭘 숨겨서가 아냐. 어떤 사람들이 엉뚱한 데를 보거나 잘못된 길로 가면서 진지하게 들으려 하지 않기 때문이야. 걔네 관심은 온통 유행하는 어둠의 신한테 쏠려 있어. 그 신이 자기가 원하는 걸 줄 거라 생각하고, 눈에 안 보이는 진리를 믿으려 하지 않는 거지. 걔네는 예수님에 대한 메시지의 눈부신 빛을 못 봐. 예수님은 우리가 얻을 수 있는 하나님의 가장 완벽한 모습이거든.",
"분명히 말할게, 이 모든 건 우리 자신에 대한 게 아냐. 우리는 예수 그리스도, 진짜 최고를 선포하고 있어. 우리는 그냥 배달원야, 예수님이 너희에게 보낸 메신저지. 이 모든 건 하나님이 '어둠을 밝혀라!' 하고 말씀하셨을 때 시작됐어. 그리스도의 얼굴에서 밝고 아름답게 빛나는 하나님을 보고 깨달으면서, 우리 삶이 빛으로 가득 찼어. 인생이 바뀐 순간이었지.",
"우리만 보면 그 빛을 놓칠 수도 있어. 우리는 이 귀한 메시지를 우리 평범한 일상이라는 수수한 질그릇에 담아 다니거든. 그건 아무도 하나님의 비교할 수 없는 능력을 우리 능력으로 착각하지 않게 하려는 거야. 사실 그럴 가능성은 거의 없어. 너희도 알다시피 우리는 별 볼 일 없으니까. 우리는 고난에 둘러싸여 얻어맞았지만 낙심하지 않았어. 어떻게 해야 할지 몰라도, 하나님은 어떻게 해야 할지 아신다는 걸 알았지. 영적으로 위협받았지만 하나님은 우리 곁을 떠나지 않으셨어. 넘어뜨려졌지만 꺾이진 않았어. 사람들이 예수님에게 했던 짓, 곧 재판과 고문, 조롱과 살해를 우리에게도 하고 있어. 하지만 예수님이 그들 가운데 하셨던 일을 우리 안에서도 하고 계셔. 그분은 살아계셔! 우리 삶은 예수님 때문에 계속 위험에 처해 있어. 그래서 예수님의 생명이 우리 안에서 더 분명하게 드러나는 거야. 우리가 최악을 겪는 동안, 너희는 최고를 누리고 있는 거야!",
"우리는 이걸 조용히 묻어두지 않아, 절대. '나는 믿었다, 그래서 말했다'라고 쓴 시편 기자처럼, 우리는 믿는 바를 외쳐. 우리가 믿는 건, 주 예수를 다시 살리신 분이 너희와 함께 우리도 반드시 다시 살리실 거라는 거야. 모든 디테일이 너희 유익과 하나님의 영광을 위한 거야. 더 많은 은혜, 더 많은 사람, 더 많은 찬양!",
"그래서 우리는 포기하지 않아. 절대! 겉으로는 우리 일이 무너져 가는 것처럼 보여도, 안에서는 하나님이 하루도 빼놓지 않고 은혜를 베푸시며 새 생명을 만들고 계셔. 지금 힘든 시간은 앞으로 올 좋은 시간에 비하면 아무것도 아냐. 우리를 위해 준비된 풍성한 잔치에 비하면 말야. 눈에 보이는 게 전부가 아냐. 지금 보이는 건 오늘 있다 내일 사라지지만, 보이지 않는 건 영원히 계속될 거야.",
],
"verseRanges": ["1-2","1-2","3-4","5-6","7-12","13-15","16-18"],
"msg_ranges": ["1-2","3-4","5-6","7-12","13-15","16-18"],
"merges": [], "splits": [],
"changes": [
"EN 구조 반영: §시련과 고난",
"배지 수정: 13-15 (EN과 동일)",
"기존 KO의 '꿀잼 메시지' 헤더 삭제 (원칙 5 과도 슬랭)",
],
"confirmations_needed": [],
})

# ============ CHAPTER 5 ============
EN_CH.append({
"chapter": 5, "title": "Level Up Your Life",
"paragraphs": [
"Hey, so check it. We know that our bodies are basically like old, beat-up tents. One day, we're gonna pack 'em up and trade 'em in for brand-new resurrection bodies in heaven. These aren't some cheap, handmade things; they're custom-built by God himself, and we'll never have to move again. It's like upgrading from a leaky tent to a sick mansion. Sometimes we can't wait to move out, and we get super frustrated with our current setup. Living here is like crashing in a bare-bones shack compared to what's coming. We're over it! God's given us a sneak peek of the real deal, our forever home, and these awesome new bodies. The Holy Spirit is like a trailer for the new life that gets us hyped for what's next. He's put a little bit of heaven in our hearts so we'll never settle for less.",
"That's why we're always in a good mood. You won't see us moping around or dragging our feet. The lame conditions here don't get us down because they just remind us of the epic life that's waiting for us. We're all in on what we can't see yet, and that's what keeps us going. You think a few bumps in the road are gonna stop us? No way. When it's time, we'll be totally ready to ditch this place and head home.",
"But it's not just about getting to heaven. The main thing is making God happy, no matter what's going on. Sooner or later, we're all gonna have to stand before God for a final review. We'll show up in front of Christ and get what we deserve for everything we've done, good or bad.",
"Knowing that keeps us on our toes, for real. It's a big deal to know that we'll all be in that judgment spot one day. That's why we're working like crazy to get everyone we meet ready to face God. Only God knows how well we're doing, but I hope you guys see how much we care. We're not just saying this to look good. We want you to be proud that we're on your team and not just being fake-nice to your face like so many people are. If I've been acting wild, it's for God. If I've been super serious, it's for you. Christ's love makes me do crazy things. His love is the boss of everything we do.",
"§A New Life",
"Our new mission is to live like this: one man died for everyone, so we're all in the same boat. He included everyone in his death so that we could all be part of his new life—a resurrection life that's way better than anything we could've managed on our own.",
"So now, we don't judge people by what they have or how they look. We used to look at the Messiah that way and got it all wrong. We're not making that mistake again. Now we look at what's inside, and we see that anyone who's with the Messiah gets an amazing change. They're a new creation. The old life is gone, and a new life has started! Look at it! This is all from God, who made things right between us and him, and then gave us the job of helping everyone else get right with each other. God put the world right with himself through the Messiah, giving everyone a fresh start by forgiving their sins. And now, he's given us the job of telling everyone what he's up to. We're like Christ's ambassadors. God uses us to convince people to drop their issues and join in on his work of making things right. We're speaking for Christ himself when we say: become friends with God; he's already friends with you.",
"How? It's all through Christ. God put all the wrong on him, who never did anything wrong, so that we could be made right with God. He took the fall for us so we could be put right with God.",
],
"verseRanges": ["1-5","6-8","9-10","11-14","14-15","14-15","16-20","21"],
"msg_ranges": ["1-5","6-8","9-10","11-14","14-15","16-20","21"],
"merges": [], "splits": [],
"changes": [
"Badge fix: 10-11 → 11-14 (MSG 11-14)",
"Badge fix: 16-19 → 16-20 (MSG 16-20; v20 'Become friends with God; he's already a friend with you' now properly badged)",
"Header replaced: invented §Ambassadors for Christ → MSG's §A New Life at MSG position, badge 14-15",
],
"confirmations_needed": [],
})
KO_CH.append({
"chapter": 5, "title": "인생 레벨업",
"paragraphs": [
"자, 들어봐. 우리 몸은 기본적으로 낡고 해진 텐트 같은 거라는 걸 우리는 알아. 언젠가는 그걸 접어서 하늘에 있는 새 부활 몸으로 갈아탈 거야. 싸구려 수제품이 아냐. 하나님이 직접 맞춤 제작하신 거고, 다시는 이사 안 해도 돼. 새는 텐트에서 끝내주는 저택으로 업그레이드하는 거지. 가끔은 이사 가고 싶어서 미칠 것 같고, 지금 상태에 완전 좌절하기도 해. 앞으로 올 것에 비하면 지금 사는 건 가구도 없는 오두막에 잠깐 얹혀사는 것 같거든. 완전 지긋지긋해! 하나님이 진짜배기, 우리 영원한 집, 이 멋진 새 몸들을 살짝 보여주셨거든. 성령님은 앞으로 올 새 삶을 미리 보여주는 예고편 같은 분이야. 그분이 우리 마음에 천국을 조금 넣어두셔서, 우리가 어설픈 것에 만족하지 않게 하시는 거야.",
"그래서 우리는 항상 기분 좋게 살아. 고개 숙이거나 질질 끄는 모습은 절대 못 볼 거야. 여기가 좀 별로라고 해서 우리를 쓰러뜨리진 못해. 오히려 앞으로 올 끝내주는 삶을 떠올리게 할 뿐이지. 우리가 아직 보지 못하는 걸 완전 믿고 있고, 그게 우리를 계속 나아가게 해. 길에 파인 구덩이나 돌멩이 따위가 우리를 막을 것 같아? 절대 안 돼. 때가 되면 우리는 여기를 떠나 집으로 갈 준비를 단단히 할 거야.",
"하지만 천국 가는 것만이 다가 아냐. 핵심은 어떤 상황에서든 하나님을 기쁘시게 하는 거야. 그게 우리가 노리는 거야. 조만간 우리는 어떤 처지든 하나님을 마주하게 될 거야. 우리는 그리스도 앞에 나타나서, 우리가 한 일대로 좋은 것이든 나쁜 것이든 받게 될 거야.",
"그걸 아는 게 우리를 정신 차리게 해, 진짜로. 우리 모두 언젠가 그 심판의 자리에 서게 된다는 걸 아는 건 절대 가벼운 일이 아냐. 그래서 우리는 만나는 모든 사람과 열심히 일하면서 그들이 하나님을 만날 준비를 하게 해. 우리가 이걸 얼마나 잘하는지는 하나님만 아시겠지만, 우리가 얼마나 신경 쓰는지는 너희가 알아줬으면 좋겠어. 잘난 척하려고 이러는 게 아냐. 너희가 기분 좋아하고 자랑스러워했으면 좋겠어서 그래. 우리는 너희 편이고, 많은 사람들처럼 너희 앞에서만 친한 척하는 게 아니니까. 내가 미친 듯이 굴었다면 하나님을 위해서였고, 너무 진지하게 굴었다면 너희를 위해서였어. 그리스도의 사랑이 나를 이렇게까지 몰아간 거야. 그분의 사랑이 우리가 하는 모든 일의 처음이자 마지막이야.",
"§새로운 삶",
"우리의 새로운 미션은 이렇게 사는 거야. 한 사람이 모두를 위해 죽으셨어. 그래서 우리는 모두 같은 배를 탄 거야. 그분은 모두를 그분의 죽음에 포함시키셔서, 모두가 그분의 새 생명, 곧 부활의 생명에 포함되게 하셨어. 우리가 혼자 살던 삶보다 훨씬 더 나은 삶이지.",
"그래서 이제 우리는 사람을 가진 것이나 외모로 판단하지 않아. 예전에 메시아를 그렇게 보고 완전히 틀렸던 거 너희도 알잖아. 그 실수 다시 안 할 거야. 이제는 속을 봐. 우리가 보는 건, 메시아와 함께 있는 사람은 누구나 놀라운 변화를 겪는다는 거야. 새로운 피조물이 되는 거지. 옛 삶은 갔어. 새 삶이 시작됐어! 봐! 이 모든 건 우리와 그분 사이의 관계를 바로잡으시고, 우리에게 서로의 관계도 바로잡는 일을 맡기신 하나님에게서 온 거야. 하나님이 메시아를 통해 세상을 자기와 화해시키시고, 죄를 용서해주심으로 모두에게 새로운 시작을 주셨어. 그리고 이제 하나님은 지금 하고 계신 일을 모든 사람에게 알리는 일을 우리에게 맡기셨어. 우리는 그리스도의 대사 같은 거야. 하나님은 우리를 사용해서 사람들이 문제를 내려놓고 서로 화해하게 하는 하나님의 일에 동참하라고 설득하셔. 우리는 지금 그리스도를 대신해서 말하고 있어. 하나님과 친구가 돼. 그분은 이미 너희와 친구시니까.",
"어떻게냐고? 전부 그리스도를 통해서야. 하나님은 아무 잘못도 하지 않은 그분에게 모든 잘못을 뒤집어씌우셨어. 그래서 우리가 하나님과 바르게 될 수 있게 말야. 그분이 우리 대신 뒤집어쓰셔서 우리가 하나님과 바르게 될 수 있게 된 거야.",
],
"verseRanges": ["1-5","6-8","9-10","11-14","14-15","14-15","16-20","21"],
"msg_ranges": ["1-5","6-8","9-10","11-14","14-15","16-20","21"],
"merges": [], "splits": [],
"changes": [
"EN 구조 반영: §새로운 삶 (MSG 위치)",
"배지 수정: 11-14, 16-20 (EN과 동일)",
],
"confirmations_needed": [],
})

# ============ CHAPTER 6 ============
EN_CH.append({
"chapter": 6, "title": "Don't Team Up With Fakers",
"paragraphs": [
"§Staying at Our Post",
"Hey, since we're on the same team doing God's work, we're begging you, don't let this awesome life God gave you go to waste. Seriously. God's basically saying, \"I heard you when you called, and I had your back right when you needed it.\" Well, now is the right time to listen, the day to be helped. Don't put it off; don't frustrate God's work by showing up late, throwing a question mark over everything we're doing.",
"Our work as God's servants gets judged—or not—in the details. People are watching us stay at our post, alert and steady... through hard times, tough times, bad times; getting beaten up, thrown in jail, mobbed; working hard, working late, working with no food; with pure hearts, clear minds, steady hands; in gentleness, holiness, and honest love; when we're telling the truth, and when God shows his power; when we're doing our best to make things right; whether we're praised or blamed; slandered or honored; true to our word, though distrusted; ignored by the world, but recognized by God; insanely alive, though rumored to be dead; beaten within an inch of our lives, but refusing to die; drowning in tears, yet filled with deep joy; living on handouts, yet making many rich; having nothing, but having it all.",
"For real, my Corinthian bros, I'm trying to tell you that you can have this big, awesome life too. We're not the ones holding you back. You're holding yourselves back. Your lives are meant to be huge, but you're living small. I'm just being straight with you because I care. Open up your lives! Live big!",
"And for real, don't team up with people who don't mess with God. How can you mix good and bad? That's not a team, that's a war. Can light and darkness be best friends? Does Jesus hang out with the Devil? Can you trust someone who doesn't trust in God? You wouldn't put a fake idol in God's temple, right? Well, you are God's temple. God lives in you. He said it himself:",
"\"I'll live in them, move into them; I'll be their God and they'll be my people. So leave the corruption and compromise; leave it for good,\" says God. \"Don't link up with those who will pollute you. I want you all for myself. I'll be a Father to you; you'll be sons and daughters to me.\" The Word of the Master, God.",
],
"verseRanges": ["1-10","1-10","1-10","11-13","14-18","14-18"],
"msg_ranges": ["1-10","11-13","14-18"],
"merges": [],
"splits": [
{"msg_range": "1-10", "paras": [1,2], "note": "MSG 1-10 is one long paragraph; split for readability (call-to-listen part + the servants' list), both badged 1-10"},
{"msg_range": "14-18", "paras": [4,5], "note": "dialogue/question part and God's quoted promise; both badged 14-18"},
],
"changes": [
"Restructured MSG 1-10: merged old overlapping [1-2]+[2-4]+[6-10] paras into two paras both badged 1-10 with splits declaration; restored the full v3-10 servants' list sequence",
"Removed invented § headers §Don't Be Mismatched and §Through Thick and Thin; added MSG's §Staying at Our Post at chapter top, badge 1-10",
"Restructured MSG 14-18: old [13-15]+[16-18] → two paras both badged 14-18 (question/dialogue part + God's quoted promise)",
"The '* * *' separator between 11-13 and 14-18 kept as a paragraph break (no invented header)",
],
"confirmations_needed": [],
})
KO_CH.append({
"chapter": 6, "title": "가짜들이랑 팀 먹지 마",
"paragraphs": [
"§우리의 자리",
"너희와 함께 이 일을 하는 동료로서 부탁할게. 하나님이 주신 이 놀라운 인생을 조금도 낭비하지 마. 진심이야. 하나님이 기본적으로 이렇게 말씀하셔. '딱 좋은 타이밍에 내가 너의 부르짖음을 들었다. 네가 나를 필요로 하던 바로 그날, 내가 널 도우려고 거기 있었다.' 자, 지금이 들을 때야, 도움받을 날이야. 미루지 마. 늦게 나타나거나 우리가 하는 모든 일에 물음표를 던지면서 하나님의 일을 방해하지 마.",
"하나님의 종으로서 우리 일은 디테일에서 인정받거나, 못 받거나야. 사람들이 우리를 지켜보고 있어. 우리가 자리를 지키는지, 깨어 있고 흔들림 없이. 힘든 때, 고된 때, 나쁜 때에도. 얻어맞고, 감옥 가고, 몰매 맞을 때도. 열심히 일하고, 밤늦게까지 일하고, 밥도 못 먹고 일할 때도. 깨끗한 마음, 맑은 정신, 성실한 손으로. 온유함과 거룩함, 정직한 사랑으로. 진리를 말할 때도, 하나님이 능력을 보이실 때도. 최선을 다해 바로잡을 때도. 칭찬받을 때도, 비난받을 때도. 비방받을 때도, 존경받을 때도. 의심받지만 말은 진실하게. 세상에는 무시받지만 하나님께는 인정받으며. 죽었다는 소문이 돌지만 엄청나게 살아 있게. 거의 죽도록 맞았지만 죽지 않고. 눈물에 잠겼지만 깊은 기쁨으로 가득 차서. 얻어먹고 살지만 많은 사람을 부자로 만들며. 가진 게 없지만, 모든 걸 가진 채로.",
"진짜로, 고린도 친구들아, 너희도 이 크고 멋진 삶을 누릴 수 있다는 걸 말해주고 싶어. 우리가 너희를 막는 게 아냐. 너희가 스스로를 막고 있는 거야. 너희 삶은 크게 살라고 있는 건데, 너희는 작게 살고 있어. 너희를 아끼니까 솔직하게 말하는 거야. 너희 삶을 열어! 크게 살아!",
"그리고 진짜로, 하나님 안 믿는 사람들이랑 팀 먹지 마. 옳은 것과 그른 게 어떻게 섞이겠어? 그건 팀이 아니라 전쟁이야. 빛이 어둠이랑 베프가 될 수 있어? 예수님이 악마랑 어울려 다녀? 하나님을 안 믿는 사람을 믿을 수 있어? 하나님의 성전에 가짜 우상을 갖다 놓진 않겠지? 근데 그게 바로 너희 모습이야. 너희가 하나님의 성전이거든. 하나님이 너희 안에 사셔. 그분이 직접 말씀하셨어.",
"'내가 그들 안에 살며, 그들 가운데로 들어갈 것이다. 나는 그들의 하나님이 되고, 그들은 내 백성이 될 것이다. 그러니 부패와 타협에서 떠나라. 영원히 떠나라'고 하나님이 말씀하셔. '너희를 더럽힐 사람들과 엮이지 마. 나는 너희를 다 내 것으로 원한다. 내가 너희에게 아버지가 되고, 너희는 나에게 아들딸이 될 것이다.' 주 하나님이 하신 말씀이야.",
],
"verseRanges": ["1-10","1-10","1-10","11-13","14-18","14-18"],
"msg_ranges": ["1-10","11-13","14-18"],
"merges": [],
"splits": [
{"msg_range": "1-10", "paras": [1,2], "note": "MSG 1-10은 하나의 긴 문단; 가독성을 위해 둘로 나눔, 둘 다 1-10 배지"},
{"msg_range": "14-18", "paras": [4,5], "note": "질문/대화 부분과 하나님의 약속 인용; 둘 다 14-18 배지"},
],
"changes": [
"EN 구조 반영: §우리의 자리, 1-10 분리, 14-18 분리",
"기존 KO의 임의 헤더 2개(§짝이 맞지 않는 관계, '하나님이 사시는 성전') 정리",
"1-10 종의 목록 전체 복원",
],
"confirmations_needed": [],
})

# ============ CHAPTER 7 ============
EN_CH.append({
"chapter": 7, "title": "The Ultimate Comeback",
"paragraphs": [
"Hey, with God promising us all this awesome stuff, we gotta ditch anything that messes with our lives, inside or out. Let's level up and make our lives a place where God would actually want to hang out.",
"§More Passionate, More Responsible",
"Seriously, trust us. We've never scammed or taken advantage of anyone. I'm not trying to call you out. I've told you before, I'm your biggest fan, ride or die. I'm so proud of you guys it's not even funny. Even with all the drama we've been through, thinking about you just makes me happy.",
"When we first rolled into Macedonia, we were totally stressed. There was drama in the church, and we were panicking. We couldn't chill because we had no idea what was going to happen. But then God, who's the ultimate hype man for anyone feeling down, sent Titus to us, and it was a total game-changer. Just seeing him was cool, but the real W was hearing what he said about you guys: how you were all-in, how you felt bad about the situation, and how you had my back. I went from being a wreck to totally chill in like, five seconds.",
"Look, I know my last letter was harsh and probably made you feel terrible. I felt bad about it for a minute, but now I see it was for the best. It was a wake-up call. I'm not glad you were upset, but I'm stoked that it made you turn things around and get right with God. It was a total win.",
"Feeling bad in a way that pushes you toward God is a good thing. It's a powerful shift for your soul. You never regret that kind of pain. But when you let tough times push you away from God, you just end up with a life full of regrets, which is a dead end.",
"And now, isn't it wonderful all the ways this whole mess pushed you closer to God? You're more alive, more concerned, more sensitive, more reverent, more human, more passionate, more responsible. From every angle, you came out of this with a pure heart. That's what I was hoping for when I wrote that letter in the first place. My main concern wasn't about who did the wrong or who got hurt—it was about you, that you'd realize and act on the deep, deep connection between us before God. That's what happened—and we felt amazing.",
"And then, when we saw how Titus felt—his excitement over your response—our joy doubled. It was amazing to see how refreshed and revived he was by everything you did. If I went out on a limb telling Titus how great you were, you didn't cut off that limb. Turns out I hadn't exaggerated one bit. Titus saw for himself that everything I'd said about you was true. He can't stop talking about it, going over again and again the story of your quick obedience and the dignity and sensitivity of your hospitality. He was completely blown away! And I couldn't be more pleased—I'm so confident and proud of you.",
],
"verseRanges": ["1","2-4","2-4","5-7","8-9","10","11-13","13-16"],
"msg_ranges": ["1","2-4","5-7","8-9","10","11-13","13-16"],
"merges": [],
"splits": [
{"msg_range": "13", "paras": [6,7], "note": "MSG overlaps v13 between 11-13 and 13-16"},
],
"changes": [
"Badge fix: 2-3 → 2-4 (MSG 2-4)",
"Badge fix: 10-11 → 10 (MSG 10)",
"Restored 11-13: all seven descriptors 'more alive, more concerned, more sensitive, more reverent, more human, more passionate, more responsible' (old text had only four) + 'the deep, deep connection between us before God'",
"Restored 13-16: 'your quick obedience, and the dignity and sensitivity of your hospitality' (was reduced to 'major respect')",
"Header replaced: invented §Paul's Joy → MSG's §More Passionate, More Responsible at MSG position, badge 2-4",
],
"confirmations_needed": [],
})
KO_CH.append({
"chapter": 7, "title": "궁극의 컴백",
"paragraphs": [
"하나님이 우리에게 이렇게 멋진 걸 약속해주셨으니까, 우리 삶을 망치는 것들은 다 끊어버리자. 안팎으로 말야. 레벨업해서 우리 삶을 하나님이 진짜 머물고 싶어하는 곳으로 만들자.",
"§더 뜨겁게, 더 책임감 있게",
"진짜로, 우리를 믿어줘. 우리는 아무도 속이거나 이용한 적 없어. 너희 흠 잡으려는 게 아냐. 전에 말했듯이 나는 너희 열혈 팬이야, 끝까지 함께할 거야. 너희가 너무 자랑스러워서 말로 다 못 해. 온갖 드라마를 겪었는데도, 너희 생각만 하면 기뻐.",
"마케도니아에 처음 갔을 때, 우리는 완전 스트레스였어. 교회 안에 드라마가 있었고, 우리는 패닉 상태였거든. 무슨 일이 일어날지 몰라서 쉴 수가 없었지. 그러다 낙심한 사람의 최고의 응원자인 하나님이 디도를 보내주셨어. 완전 게임 체인저였지. 디도를 보는 것만으로도 좋았지만, 진짜 승리는 그가 전한 너희 소식이었어. 너희가 얼마나 올인했는지, 상황을 얼마나 안타까워했는지, 나를 얼마나 지켜줬는지 말야. 나는 5초 만에 멘붕에서 완전 평온으로 바뀌었어.",
"봐, 내 지난 편지가 독했고 너희를 힘들게 했을 거라는 거 알아. 잠깐은 미안했지만, 이제 보니 최선이었어. 정신 차리게 하는 일격이었지. 너희가 괴로워서 기쁜 게 아니라, 그걸로 방향을 틀고 하나님과 바로잡게 돼서 신나. 완전 승리였어.",
"너희를 하나님께로 이끄는 괴로움은 좋은 거야. 영혼의 강력한 전환점이지. 그런 아픔은 절대 후회하지 않아. 하지만 힘든 시간이 하나님에게서 멀어지게 두면, 후회로 가득 찬 인생으로 끝나. 그건 막다른 길이야.",
"그런데 이 모든 난리가 너희를 하나님께 더 가까이 이끈 모든 모습이 얼마나 놀라워? 너희는 더 생생하고, 더 신경 쓰고, 더 섬세하고, 더 경건하고, 더 인간적이고, 더 열정적이고, 더 책임감 있게 됐어. 어느 각도에서 봐도, 너희는 마음이 깨끗해진 채로 이 일을 빠져나왔어. 그게 바로 내가 그 편지를 쓸 때 처음부터 바랐던 거야. 내 첫 관심사는 누가 잘못했는지, 누가 상처받았는지가 아니라 바로 너희였어. 너희가 하나님 앞에서 우리 사이의 깊고 깊은 유대를 깨닫고 행동하길 바랐던 거지. 그렇게 됐고, 우리는 완전 기뻤어.",
"그리고 디도가 너희 반응에 얼마나 들떠 있는지 보고 우리 기쁨은 두 배가 됐어. 너희가 한 모든 일로 그가 새로워지고 기운 차린 걸 보는 게 놀라웠어. 내가 디도에게 너희가 얼마나 대단한지 말하면서 무리수를 뒀다면, 너희는 그 무리수를 꺾지 않았어. 알고 보니 나는 조금도 과장하지 않았던 거야. 디도는 내가 너희에 대해 한 말이 모두 진짜라는 걸 직접 봤어. 그는 너희의 빠른 순종과, 너희 환대의 품위와 섬세함에 대한 이야기를 계속 반복해서 해. 완전히 압도됐던 거야! 나는 더 기쁠 수 없어. 너희가 완전 든든하고 자랑스러워.",
],
"verseRanges": ["1","2-4","2-4","5-7","8-9","10","11-13","13-16"],
"msg_ranges": ["1","2-4","5-7","8-9","10","11-13","13-16"],
"merges": [],
"splits": [
{"msg_range": "13", "paras": [6,7], "note": "MSG overlaps v13 between 11-13 and 13-16"},
],
"changes": [
"EN 구조 반영: §더 뜨겁게, 더 책임감 있게 (MSG 위치)",
"배지 수정: 2-4, 10, 11-13 (EN과 동일)",
"11-13 복원: 일곱 가지 묘사 전부 ('더 생생하고, 더 신경 쓰고, 더 섬세하고, 더 경건하고, 더 인간적이고, 더 열정적이고, 더 책임감 있게')",
"13-16 복원: '너희의 빠른 순종과, 너희 환대의 품위와 섬세함'",
],
"confirmations_needed": [],
})

# ============ CHAPTER 8 ============
EN_CH.append({
"chapter": 8, "title": "The Ultimate Flex of Giving",
"paragraphs": [
"§The Offering",
"Hey, check it out. I gotta tell you about the Macedonian churches. They've been going through some majorly tough times, like, seriously pushed to their limits. But it's in the middle of all that chaos that their true colors showed, and man, did they shine. They were super happy, even though they were broke. And here's the thing—the pressure made them do something totally unexpected. They started giving like crazy, just pure, generous hearts. I was there, I saw it. They gave everything they could, and then some, begging for the chance to help out other Christians who were struggling.",
"This wasn't some planned thing; it was all them. They totally caught us off guard. The secret? They gave themselves to God first, and then to us. The rest of the giving just flowed from that. That's why we hit up Titus to get you guys in on it, to finish what you started. You're already killing it in so many ways—you've got major faith, you're great with words, you're smart, you're passionate, and you love us. So, let's see you crush this, too.",
"I'm not trying to boss you around or anything. But seeing how hyped the Macedonians are, I'm hoping it'll light a fire under you and bring out your best. You already know how generous our main man, Jesus, was. He was loaded, but he gave it all up for us. In one move, he became poor so we could become rich. That's the ultimate sacrifice.",
"So here's the deal: finish what you started last year. Don't let those good intentions grow stale. Your hearts were in the right place from the start. You've got what it takes to finish it, so get it done. Once the commitment is clear, you do what you can, not what you can't. The heart regulates the hands. This isn't so others can take it easy while you sweat it out. No—you're shoulder to shoulder with them all the way, your surplus matching their deficit, their surplus matching your deficit. In the end you come out even. As it is written: Nothing left over to the one with the most, nothing lacking to the one with the least.",
"I thank God for giving Titus the same devoted concern for you that I have. He was considerate of how we felt, but his eagerness to come to you and help out with this relief offering is his own idea. We're sending a companion along with him, someone super popular in the churches for preaching the Message. But he's way more than popular—he's rock-solid trustworthy. The churches handpicked him to travel with us doing this work of sharing God's gifts, to honor God as well as we can, taking every precaution against scandal.",
"We don't want anyone suspecting us of taking one penny of this money for ourselves. We're being as careful with our reputation before people as before God. That's why we're sending another trusted friend along. He's proved his dependability over and over, and he's as energetic as ever. He's heard great things about you and liked what he heard—so much that he can't wait to get there.",
"I don't even need to hype up Titus. We've been a team for a long time, serving you guys. The bros traveling with him are sent by the churches, a total credit to Christ. So show them what you're made of. Show them that love I've been bragging about to the other churches. Let them see it for themselves!",
],
"verseRanges": ["1-4","1-4","5-7","8-9","10-20","10-20","20-22","23-24"],
"msg_ranges": ["1-4","5-7","8-9","10-20","20-22","23-24"],
"merges": [],
"splits": [
{"msg_range": "10-20", "paras": [4,5], "note": "MSG 10-20 is long; split into the finish-the-offering part (v10-15) and the Titus/companion part (v16-20), both badged 10-20"},
{"msg_range": "20", "paras": [5,6], "note": "MSG overlaps v20 between 10-20 and 20-22"},
],
"changes": [
"Badge fix: 1-5 → 1-4 (MSG 1-4)",
"Badge fix: 6-9 → 5-7 (MSG 5-7)",
"Badge fix: 8-10 → 8-9 (MSG 8-9)",
"Restructured MSG 10-20: old incomplete [10-12] para + mis-badged [16-19] para → two paras both badged 10-20 (v10-15 finish-the-offering + v16-20 Titus and the handpicked companion)",
"Restructured MSG 20-22: badge fix 18-22 → 20-22",
"Header replaced: invented §Generous Giving → MSG's §The Offering at chapter top, badge 1-4",
],
"confirmations_needed": [],
})
KO_CH.append({
"chapter": 8, "title": "나눔의 끝판왕",
"paragraphs": [
"§구제 헌금",
"자, 들어봐. 마케도니아 교회들 얘기를 해줘야겠어. 걔네가 진짜 힘든 시기를 겪고 있어. 말 그대로 한계까지 몰렸지. 근데 그 혼돈 한가운데서 걔네 진짜 모습이 드러났어. 완전 빛났지. 엄청 가난했는데도 엄청 기뻐했어. 그리고 포인트는 이거야. 그 압박이 완전히 예상 밖의 일을 만들어냈어. 순수하고 관대한 마음으로 미친 듯이 나누기 시작한 거야. 내가 거기서 직접 봤어. 할 수 있는 건 다 내놓고, 그 이상까지 내놓으면서, 힘든 크리스천들을 돕는 일에 참여할 기회를 달라고 애원했어.",
"이건 누가 시켜서 한 게 아냐. 전부 걔네 생각이었어. 우리는 완전히 기습당했지. 비결은? 걔네가 먼저 자신을 하나님께 드렸고, 그 다음 우리에게 드린 거야. 나머지 나눔은 그냥 거기서 흘러나온 거였어. 그래서 우리는 디도에게 부탁해서 너희도 이 일에 동참하게 한 거야. 시작한 걸 마무리하려고 말야. 너희는 이미 많은 걸 잘하고 있잖아. 믿음도 크고, 말도 잘하고, 똑똑하고, 열정적이고, 우리를 사랑하지. 그러니까 이것도 끝내주게 해봐.",
"너희 뜻에 반해서 명령하려는 게 아냐. 다만 마케도니아 사람들의 열정을 보고 너희 안에 불을 지펴서 너희 최고를 끌어내고 싶은 거야. 너희는 우리 주 예수 그리스도가 얼마나 관대하신지 잘 알잖아. 부자셨던 그분이 우리를 위해 모든 걸 다 내어주셨어. 한 번에 그분은 가난해지셨고, 우리는 부자가 됐어. 그게 궁극의 희생이야.",
"내 생각은 이래. 작년에 시작한 걸 마무리해. 그 좋은 마음이 식게 두지 마. 너희 마음은 처음부터 올바른 곳에 있었어. 마무리할 능력도 충분하니까, 어서 해. 결심이 확실해지면, 할 수 있는 만큼 하는 거야, 못 하는 만큼이 아니라. 마음이 손을 다스려. 이건 다른 사람은 편히 쉬고 너희만 고생하라는 게 아냐. 아니, 너희는 그들과 끝까지 어깨를 나란히 하는 거야. 너희 남는 게 그들의 모자란 걸 채우고, 그들의 남는 게 너희 모자란 걸 채우는 거지. 결국 공평해져. 기록된 대로야. 가장 많이 거둔 사람도 남는 게 없고, 가장 적게 거둔 사람도 모자람이 없었다고.",
"너희를 향한 나와 같은 헌신적인 마음을 디도에게 주신 하나님께 감사해. 그는 우리 마음을 배려해줬지만, 너희에게 가서 이 구제 헌금을 돕고 싶은 열정은 그 자신의 생각이야. 우리는 그와 함께 동료 한 명을 보내. 그는 메시지 전하는 일로 교회들에서 아주 인기 있는 사람이야. 하지만 인기 그 이상이야. 바위처럼 단단하고 믿음직스러워. 여러 교회가 직접 그를 뽑아서, 하나님의 선물을 나누는 이 일을 우리와 함께하게 했어. 하나님께 최대한 영광 돌리고, 스캔들에 대한 모든 예방을 다 하려는 거야.",
"우리는 이 돈에서 한 푼이라도 우리가 챙긴다는 의심을 받고 싶지 않아. 하나님 앞에서처럼 사람들 앞에서도 평판에 조심하고 있어. 그래서 믿을 만한 친구 한 명을 더 보내는 거야. 그는 여러 번 자기 믿음직함을 증명했고, 처음 시작했을 때처럼 지금도 열정적으로 일해. 그는 너희에 대한 좋은 소식을 많이 듣고 마음에 들어 했어. 그래서 너희에게 가는 걸 완전 기대하고 있어.",
"디도에 대해서는 더 말할 필요 없어. 우리는 너희를 섬기는 이 일에서 오랫동안 한 팀이었어. 그와 함께 가는 형제들은 교회들이 보낸 사람들이고, 그리스도의 완전한 자랑거리야. 그러니까 너희가 뭘로 만들어졌는지 보여줘. 내가 여러 교회에 자랑했던 그 사랑을 보여줘. 직접 보게 해줘!",
],
"verseRanges": ["1-4","1-4","5-7","8-9","10-20","10-20","20-22","23-24"],
"msg_ranges": ["1-4","5-7","8-9","10-20","20-22","23-24"],
"merges": [],
"splits": [
{"msg_range": "10-20", "paras": [4,5], "note": "MSG 10-20은 긴 문단; 헌금 마무리 부분과 디도/동료 부분으로 나눔, 둘 다 10-20 배지"},
{"msg_range": "20", "paras": [5,6], "note": "MSG overlaps v20 between 10-20 and 20-22"},
],
"changes": [
"EN 구조 반영: §구제 헌금, 10-20 분리",
"배지 수정: 1-4, 5-7, 8-9, 10-20, 20-22 (EN과 동일)",
"기존 KO의 장식 헤더('고린도후서 8장 - 십대 버전 😎🙏', '§구제 헌금' 중복) 정리",
],
"confirmations_needed": [],
})

# ============ CHAPTER 9 ============
EN_CH.append({
"chapter": 9, "title": "Generous Giving Pays Off",
"paragraphs": [
"Hey, I don't even need to say anything about collecting money for the believers in Jerusalem. I know you're totally in, and I've already been hyping you up to the Macedonians, saying that you guys in Achaia were ready to roll a year ago. Your enthusiasm has been contagious, and it's got most of them pumped too. Now, I'm sending these brothers so you can back up my words and make sure you're really ready to give, just like I said. I don't want them to show up and catch you off guard.",
"You know how it is—if some Macedonians come with me and find out you're not ready, it'd be a bad look for us. It'd be awkward. We're not saying you have to give a crazy amount, just make sure you're ready to follow through on what you promised.",
"So, I figured it was a good idea to ask these brothers to go ahead of me and get the offering ready. That way, it's a legit, generous gift, not some last-minute scramble. You've already shown that you're the type to give generously, so keep that momentum going. Just keep this in mind: The person who plants a few seeds gets a small crop; the one who plants a lot gets a big crop. Each of you should give what you feel in your heart, not because someone's twisting your arm or you feel guilty. God loves a cheerful giver. And God can shower you with blessings so that you'll have everything you need, and then some, to be generous in every way.",
"As the Scriptures say: \"The one who goes around giving to the poor, with compassion and generosity, will have his good deeds live on forever.\" This generous, giving God is going to keep giving you what you need. He's going to provide for you, grow your good deeds, and make you rich enough to be generous at every turn. Every time we deliver your gifts, you're going to see God getting the thanks and the glory. You're not just helping out some believers who are in a tough spot; you're making sure that God's getting the love and respect he deserves. Your giving proves that you're for real about your faith, and it's going to inspire a lot of praise for God. And those people you're helping? They're going to be praying for you and cheering you on because of the incredible way God is working through you. Thank God for this gift that's so amazing it's beyond words!",
],
"verseRanges": ["1-2","3-5","3-5","6-7","8-11","12-15"],
"msg_ranges": ["1-2","3-5","6-7","8-11","12-15"],
"merges": [],
"splits": [
{"msg_range": "3-5", "paras": [1,2], "note": "MSG 3-5: the awkward/Macedonians part and the brothers-getting-the-offering-ready part"},
],
"changes": [
"Badge fix: 1-5 → 1-2 (MSG 1-2; the 'Macedonians might find you unprepared' content is v3-5, not v1-2)",
"Badge fix: 5-8 → 6-7 (MSG 6-7)",
"Badge fix: 8-10 → 8-11 (MSG 8-11)",
"Restructured MSG 3-5: old [2-4] para → two paras badged 3-5 with splits declaration",
"Old [11-13] para content ('Your giving proves...') merged into the 12-15 paragraph per MSG grouping (no merge since MSG 12-15 is one paragraph)",
],
"confirmations_needed": [],
})
KO_CH.append({
"chapter": 9, "title": "관대한 나눔의 결실",
"paragraphs": [
"예루살렘의 성도들을 위한 모금에 대해서는 더 말할 필요가 없어. 너희가 완전 찬성이라는 걸 아니까. 나는 이미 마케도니아 사람들에게 너희를 자랑했어. 아가야 지방의 너희가 일 년 전부터 준비됐다고 말했지. 너희 열정이 전염돼서 걔네 대부분이 들떴거든. 이제 나는 이 형제들을 보내서, 너희가 내 말을 뒷받침하고 내가 말한 대로 정말 나눌 준비가 돼 있는지 확인하려는 거야. 걔네가 갑자기 나타나서 너희가 허둥대는 걸 보고 싶지 않거든.",
"너희도 알잖아. 마케도니아 사람들이 나랑 같이 가서 너희가 준비 안 됐다는 걸 알게 되면, 우리 입장이 곤란해져. 완전 어색해지지. 미친 듯이 많이 내라는 게 아냐. 약속한 건 지킬 준비가 돼 있으라는 거야.",
"그래서 이 형제들에게 미리 가서 헌금을 준비해달라고 부탁하는 게 좋은 생각 같았어. 그러면 마지막 순간에 허둥대며 긁어모은 게 아니라, 진짜 관대한 선물이 되잖아. 너희는 이미 관대하게 주는 스타일이라는 걸 보여줬으니까, 그 흐름을 이어가. 이걸 명심해. 씨를 적게 뿌리는 사람은 적게 거두고, 많이 뿌리는 사람은 많이 거둬. 너희 각자는 마음에 느끼는 대로 줘. 누가 팔을 비틀어서도, 죄책감 때문도 아니야. 하나님은 기쁘게 주는 사람을 사랑하시거든. 그리고 하나님은 너희에게 복을 쏟아부으셔서, 필요한 모든 게 있고 남을 만큼 주실 수 있어. 그래서 온갖 방식으로 관대하게 나눌 수 있게 말야.",
"성경이 말하듯이 말야. '가난한 사람들에게 자비와 관대함으로 나누는 사람은, 그의 선행이 영원히 살 것이다.' 이 관대하고 주시는 하나님이 너희에게 필요한 걸 계속 주실 거야. 그분이 너희를 돌보시고, 너희 선행을 자라게 하시고, 모든 일에 관대할 만큼 부유하게 하실 거야. 우리가 너희 선물을 전달할 때마다, 너희는 하나님께 감사와 영광이 돌아가는 걸 보게 될 거야. 너희는 힘든 성도들을 돕는 것뿐만 아니라, 하나님이 받으셔야 할 사랑과 존경을 확실히 받게 하고 있는 거야. 너희 나눔은 너희 믿음이 진짜라는 걸 증명하고, 하나님께 많은 찬양을 불러일으킬 거야. 그리고 너희가 돕는 그 사람들? 하나님이 너희를 통해 놀라운 일을 하시는 걸 보고 너희를 위해 기도하고 응원할 거야. 말로 다 못할 정도로 놀라운 이 선물에 하나님께 감사하자!",
],
"verseRanges": ["1-2","3-5","3-5","6-7","8-11","12-15"],
"msg_ranges": ["1-2","3-5","6-7","8-11","12-15"],
"merges": [],
"splits": [
{"msg_range": "3-5", "paras": [1,2], "note": "MSG 3-5: 마케도니아 사람들이 올 때 준비 안 된 부분과 형제들이 헌금을 미리 준비하는 부분"},
],
"changes": [
"EN 구조 반영: 3-5 분리",
"배지 수정: 1-2, 6-7, 8-11 (EN과 동일)",
],
"confirmations_needed": [],
})

# ============ CHAPTER 10 ============
EN_CH.append({
"chapter": 10, "title": "Not Your Average Apostle",
"paragraphs": [
"§Tearing Down Barriers",
"Hey, it's Paul again. You know, the guy who seems all chill and humble when he's with you, but totally savage in his letters? Yeah, that's me. Let me be real with you. Some of you are saying that when I'm with you, I'm all meek and mild, but when I write, I'm super tough. But seriously, when I come to visit, I don't want to have to go all tough-guy on anyone. I'm trying to be cool and not confrontational. I get that some people think I'm just doing my own thing, playing by the world's rules. But that's not true.",
"The world is unprincipled. It's dog-eat-dog out there! The world doesn't fight fair. But we don't live or fight our battles that way—never have and never will. The tools of our trade aren't for marketing or manipulation, but they are for demolishing that entire massively corrupt culture. We use our powerful God-tools for smashing warped philosophies, tearing down barriers erected against the truth of God, fitting every loose thought and emotion and impulse into the structure of life shaped by Christ. Our tools are ready at hand for clearing the ground of every obstruction and building lives of obedience into maturity.",
"Some of you are hung up on seeing things only from the surface. If someone steps up and says, \"I'm totally with Christ,\" let them say it again after looking at the evidence. We're just as much in Christ as they are. You know, I do have the authority to build you up, not tear you down. And I'm not afraid to use it. I'm not ashamed of it. I don't want you to think I'm just trying to scare you with my letters.",
"Someone's probably thinking, \"His letters are heavy and powerful, but in person, he's a total pushover.\" Well, let me tell you, I'm the same person in person as I am in my letters. When I do show up, you'll see that I'm not messing around. I'm going to call it like it is. I'm not going to pretend to be someone I'm not.",
"We don't try to rank ourselves with these self-appointed experts or compare ourselves to them. They play these little games, comparing themselves to each other, and it's just pathetic. But we're not going to go around bragging about what we can't do. We're going to stick to the job God gave us, and that includes you. We're not overstepping our boundaries by coming to you, because we were the first ones to bring you the message of Christ. It's not like we're taking credit for someone else's work.",
"We're not trying to take credit for what others have done. We're just hoping that as your faith grows, our work among you will grow too. Then we can take the message to places that haven't heard it yet, without stepping on anyone else's toes or trying to claim their work as our own. If you want to claim credit, do what the Scriptures say: \"If you want to brag, brag about the Master.\" What counts is not bragging about yourself, but letting the Master commend you.",
],
"verseRanges": ["1-2","1-2","3-6","7-8","9-11","12","13-14","15-18"],
"msg_ranges": ["1-2","3-6","7-8","9-11","12","13-14","15-18"],
"merges": [],
"splits": [
{"msg_range": "1-2", "paras": [1,2], "note": "MSG 1-2: the 'meek when present, bold in letters' opener and Paul's appeal to be gentle (v1-2 continuation)"},
],
"changes": [
"Badge fix: 4-6 → 3-6 (MSG 3-6)",
"Badge fix: 8-9 → 7-8 (MSG 7-8; v7 'see things only from the surface' content restored to this para)",
"Badge fix: 10-12 → 9-11 (MSG 9-11)",
"Badge fix: 12-13 → 12 (MSG 12)",
"Badge fix: 14-15 → 13-14 (MSG 13-14)",
"Badge fix: 16-18 → 15-18 (MSG 15-18)",
"Restructured MSG 1-2: old [1-3] para → two paras badged 1-2 with splits declaration",
"Header replaced: invented §Paul's Authority → MSG's §Tearing Down Barriers at chapter top, badge 1-2",
],
"confirmations_needed": [],
})
KO_CH.append({
"chapter": 10, "title": "평범하지 않은 사도",
"paragraphs": [
"§장벽을 허물다",
"자, 다시 나 바울이야. 알잖아, 너희랑 같이 있을 때는 조용하고 겸손해 보이는 사람 말야. 근데 편지에서는 완전 쎄 보이지? 응, 그게 나야. 솔직하게 말할게. 너희 중 몇 명은 내가 너희랑 같이 있을 때는 온순하고 말랑하다가, 편지 쓸 때는 완전 강하게 나온다고 하더라. 근데 진짜로, 방문했을 때 누구한테든 강하게 나올 필요 없길 바라. 나는 쿨하게, 대립하지 않게 하려고 노력 중이야. 어떤 사람들은 내가 그냥 내 멋대로 세상의 룰대로 논다고 생각하는 거 알아. 근데 그건 사실이 아냐.",
"세상은 원칙이 없어. 완전 약육강식이야! 세상은 정정당당하게 싸우지 않아. 하지만 우리는 그렇게 살지도 싸우지도 않아. 예전에도 안 그랬고 앞으로도 안 그럴 거야. 우리 도구는 마케팅이나 조종을 위한 게 아니라, 완전히 부패한 그 거대한 문화를 통째로 무너뜨리는 거야. 우리는 하나님의 강력한 도구를 써서 뒤틀린 철학을 박살 내고, 하나님의 진리에 맞서 세워진 장벽을 허물고, 제멋대로인 모든 생각과 감정과 충동을 그리스도가 만드신 삶의 구조에 끼워 맞추는 거야. 우리의 도구는 모든 장애물을 치우고 순종의 삶을 성숙하게 세우는 일에 언제든 준비돼 있어.",
"너희 중 몇 명은 겉모습만 보고 판단하는 데 집착하더라. 누군가 나서서 '나는 완전 그리스도와 함께 있어'라고 말하면, 증거를 보고 나서 한 번 더 말하게 해. 그들도 우리만큼 그리스도 안에 있어. 알아둬, 나는 너희를 세우는 권위, 무너뜨리는 권위가 아니야. 그걸 쓸 거고, 부끄럽지 않아. 내 편지로 너희를 겁주려는 게 아니라는 걸 알아줬으면 좋겠어.",
"누군가는 이렇게 생각하겠지. '편지는 무겁고 강력하지만, 실제로 만나면 완전 호구야.' 자, 말해줄게. 나는 실제로 만나도 편지에서와 같은 사람이야. 내가 나타나면 장난 안 친다는 걸 알게 될 거야. 있는 그대로 말할 거야. 아닌 척 안 할 거야.",
"우리는 스스로를 임명한 전문가들과 순위를 매기거나 비교하려 하지 않아. 걔네는 서로 비교하는 유치한 게임을 하고, 그건 그냥 불쌍해. 하지만 우리는 못 하는 걸 자랑하고 다니진 않을 거야. 하나님이 주신 일에 충실할 거야. 그 일에는 너희도 포함돼. 우리가 너희에게 온다고 해서 선을 넘는 게 아냐. 그리스도의 메시지를 너희에게 처음 가져온 사람이 우리였으니까. 남의 일을 가로채는 게 아니야.",
"우리는 다른 사람이 한 일을 가로채려 하지 않아. 너희 믿음이 자라면 우리 일도 너희 가운데 자라길 바랄 뿐이야. 그러면 아직 듣지 못한 곳에 메시지를 전할 수 있어. 남의 발을 밟거나 남의 일을 우리 일이라고 주장하지 않고 말야. 자랑하고 싶으면 성경이 말한 대로 해. '자랑하고 싶으면 주를 자랑하라.' 중요한 건 스스로 자랑하는 게 아니라, 주님이 너희를 인정해주시게 하는 거야.",
],
"verseRanges": ["1-2","1-2","3-6","7-8","9-11","12","13-14","15-18"],
"msg_ranges": ["1-2","3-6","7-8","9-11","12","13-14","15-18"],
"merges": [],
"splits": [
{"msg_range": "1-2", "paras": [1,2], "note": "MSG 1-2: '함께 있을 땐 온순, 편지에서는 강하게' 오프너와 바울의 온유한 호소"},
],
"changes": [
"EN 구조 반영: §장벽을 허물다, 1-2 분리",
"배지 수정: 3-6, 7-8, 9-11, 12, 13-14, 15-18 (EN과 동일)",
],
"confirmations_needed": [],
})

# ============ CHAPTER 11 ============
EN_CH.append({
"chapter": 11, "title": "Don't Get Played by Fakes",
"paragraphs": [
"§Pseudo-Servants of God",
"Hey, so can you guys just bear with me for a sec? I'm about to go full fool mode here. I hope you don't mind me being a little extra. I'm like, super passionate about you guys. It's like I'm trying to set you up with the perfect match—Jesus. I'm trying to keep you pure and ready for him, like a virgin bride. But I'm stressed. I'm worried you'll get played, like Eve got played by that sneaky snake. You know, getting led astray from the real deal and falling for some fake version of Jesus, some knockoff spirit, some watered-down gospel.",
"You seem totally fine with it when someone rolls up with a different Jesus than the one we told you about, or a different spirit, or a different gospel. You're like, \"Sure, come on in!\" and you're cool with it. And I don't think I'm any less legit than these so-called \"super-apostles\" who are all up in your business. Maybe I'm not the smoothest talker, but I know my stuff, and I've proven it to you over and over.",
"You know, I basically worked for free when I was with you, telling you about God's message. I didn't charge you a dime. Was that wrong? Did I mess up by not asking for payment and making myself look like a nobody so you could feel like somebody? I had to get financial support from other churches just to be able to serve you. It was like I was robbing them to pay for my time with you. And when I was with you and needed money, I didn't ask you for a single cent. My boys from Macedonia hooked me up with what I needed. I've always made sure not to be a burden to you, and I'm going to keep it that way. I'm telling you the truth, just as sure as I know Christ, I'm going to keep bragging about this all over Achaia. And why? Because I don't love you? You know that's not true. God knows I love you.",
"§Many a Long and Lonely Night",
"And I'll keep doing it, because I don't want to give those troublemakers any chance to claim they're on my level. They're not even in the same league. They're not real apostles; they're fakes, just trying to look like Christ's apostles. And it's no surprise, because even Satan can dress up like an angel of light. So it's no big deal if his minions dress up like ministers of righteousness. They'll get what's coming to them in the end.",
"Okay, I need you to hear me out, even if I sound like a total fool right now. Don't write me off as crazy, but just let me have my moment. What I'm about to say isn't exactly what the Lord would say—it's me talking, going full fool mode. Since everyone else is bragging about themselves, I guess I'll join in. You guys are so wise, but you're totally fine with putting up with fools. You let people boss you around, take your money, take advantage of you, act all high and mighty, and even slap you in the face, and you're okay with it. It's like you're saying, \"We're too weak to stand up for ourselves.\" Well, let me tell you, I'm not weak. I'm going to brag a little here, going full fool mode again.",
"Are they Hebrews? So am I. Are they Israelites? So am I. Are they descendants of Abraham? So am I. Are they servants of Christ? I'm going to sound crazy saying this, but I'm a better one. I've worked harder, been in prison more, been whipped more times than I can count, and I've faced death over and over. Five times I got the thirty-nine lashes from the Jews. Three times I was beaten with rods. Once I was stoned. Three times I was shipwrecked. I spent a night and a day adrift at sea. I've been on the road constantly, facing danger from rivers, robbers, my own people, and Gentiles. I've faced danger in the city, in the wilderness, at sea, and from fake believers. I've worked hard, gone without sleep, been hungry and thirsty, gone without food, been cold and naked. And that's not even counting the daily pressure of worrying about all the churches. Who's struggling? I feel it. Who's tripped up? I'm burning up inside.",
"If I have to brag, I'll brag about the things that show my weakness. The God and Father of the Lord Jesus, who is blessed forever, knows I'm telling the truth. When I was in Damascus, the governor under King Aretas had the city on lockdown trying to arrest me. I had to be lowered in a basket through a window in the wall to escape.",
],
"verseRanges": ["1-3","1-3","4-6","7-12","12-15","12-15","16-21","21-23","21-23","23-27","28-29","30-33"],
"msg_ranges": ["1-3","4-6","7-12","12-15","16-21","21-23","23-27","28-29","30-33"],
"merges": [],
"splits": [
{"msg_range": "12", "paras": [4,5], "note": "MSG overlaps v12 between 7-12 and 12-15; v12 sentence 'And I'll keep doing it...' continues into 12-15"},
{"msg_range": "21", "paras": [7,8], "note": "MSG overlaps v21 between 16-21 and 21-23"},
{"msg_range": "23", "paras": [8,9], "note": "MSG overlaps v23 between 21-23 and 23-27; the v23 line 'Are they servants of Christ?...I'm a better one' belongs to 21-23"},
],
"changes": [
"Restored all MSG paragraphs: old file had no paras for MSG 1-3, 4-6, 7-12, 12-15, 28-29, 30-33 (6 missing paragraphs restored)",
"Badge fix: 30-31 → 30-33 (MSG 30-33; v32-33 Damascus basket escape now properly badged)",
"Headers replaced: invented §True Apostles vs Fake Ones → MSG's §Pseudo-Servants of God (badge 1-3) and MSG's §Many a Long and Lonely Night (badge 12-15) at MSG positions",
"Restored 21-23: 'Five times I got the thirty-nine lashes... spent a night and a day adrift at sea' hardship list (was missing)",
"Restored 28-29: 'Who's struggling? I feel it. Who's tripped up? I'm burning up inside' (was missing)",
],
"confirmations_needed": [],
})
KO_CH.append({
"chapter": 11, "title": "가짜한테 속지 마",
"paragraphs": [
"§가짜 하나님의 종들",
"자, 잠깐만 나 좀 봐줘. 이제부터 완전 바보 모드 들어갈 거야. 내가 좀 오버하는 거 이해해줘. 나는 너희한테 완전 진심이거든. 너희를 완벽한 짝, 예수님께 소개해주려는 것 같아. 너희를 순결하게 지켜서 그분께 드리려는 거야. 순결한 신부처럼 말야. 근데 걱정돼. 너희가 속을까 봐 스트레스야. 하와가 그 교활한 뱀한테 속았던 것처럼 말야. 진짜배기에서 벗어나서 가짜 예수, 짝퉁 성령, 물 탄 복음에 넘어갈까 봐 말야.",
"너희는 우리가 전한 예수와 다른 예수를 들고 오는 사람, 다른 영, 다른 복음을 들고 오는 사람을 완전 쿨하게 받아들여. '어, 들어와!' 이러면서 말야. 그리고 나는 너희 일에 참견하는 소위 '슈퍼 사도'들보다 내가 덜 정통이라고 생각 안 해. 말은 좀 서툴지 몰라도, 아는 건 확실해. 그리고 너희에게 여러 번 증명했잖아.",
"봐, 너희랑 같이 있을 때 나는 기본적으로 공짜로 일했어. 하나님의 메시지를 전하면서 말야. 한 푼도 안 받았어. 그게 잘못이었어? 돈을 안 받고 나를 아무것도 아닌 사람처럼 만들어서 너희를 대단하게 만들었다고 내가 실수한 거야? 너희를 섬길 수 있게 다른 교회들에서 재정 지원을 받아야 했어. 너희와 함께한 시간을 위해 걔네를 털었다는 느낌이었지. 그리고 너희랑 같이 있으면서 돈이 필요했을 때도, 너희한테 한 푼도 달라고 안 했어. 마케도니아에서 온 내 친구들이 필요한 걸 챙겨줬거든. 나는 항상 너희에게 부담 주지 않으려고 했고, 앞으로도 그럴 거야. 그리스도를 아는 것만큼 확실하게 진실을 말하는데, 아가야 전역에서 이걸 계속 자랑할 거야. 왜냐고? 너희를 사랑하지 않아서? 그게 아니라는 거 너희도 알아. 하나님이 아셔. 나는 너희를 사랑해.",
"§길고 외로운 많은 밤",
"계속 그럴 거야. 그 말썽꾸러기들에게 나와 동급이라고 주장할 기회를 주고 싶지 않거든. 걔네는 나와 같은 리그가 아니야. 진짜 사도가 아냐. 가짜야. 그냥 그리스도의 사도인 척하는 거지. 놀랄 일도 아냐. 사탄도 빛의 천사로 변장할 수 있거든. 그 졸개들이 의의 일꾼으로 변장하는 건 별일도 아니야. 걔네는 결국 받을 걸 받게 될 거야.",
"좋아, 내가 지금 완전 바보처럼 들려도 내 말을 들어줘야겠어. 나를 미쳤다고 치부하지 말고, 잠깐만 내 시간을 가져. 지금부터 할 말은 주님이 하실 말씀이 정확히는 아냐. 내가 하는 말이야. 완전 바보 모드 들어가는 거지. 다른 사람들이 다 자랑하니까, 나도 끼어들게. 너희는 너무 똑똑한데, 바보들 참는 건 완전 잘해. 사람들이 너희를 부려먹고, 돈 뜯어가고, 이용하고, 잘난 체하고, 뺨까지 때려도 너희는 괜찮아해. '우리는 맞서 싸우기엔 너무 약해'라고 말하는 것 같아. 자, 말해줄게. 나는 약하지 않아. 여기서 좀 자랑할게. 다시 바보 모드 들어가는 거야.",
"걔네가 히브리인이야? 나도야. 이스라엘 사람이야? 나도야. 아브라함의 자손이야? 나도야. 그리스도의 종이야? 미친 소리처럼 들리겠지만, 내가 더 나아. 나는 더 열심히 일했고, 감옥도 더 많이 갔고, 셀 수 없이 많이 채찍질당했고, 죽음을 여러 번 마주했어. 유대인들에게 서른아홉 대 매를 다섯 번 맞았어. 몽둥이로 세 번 맞았어. 한 번은 돌에 맞았어. 세 번은 배가 난파됐어. 밤낮으로 바다에 떠다녔어. 계속 길을 가면서 강에서, 강도에게서, 내 민족에게서, 이방인에게서 위험을 마주했어. 도시에서, 광야에서, 바다에서, 가짜 믿는 사람들에게서 위험을 마주했어. 열심히 일했고, 잠도 못 잤고, 배고프고 목말랐고, 밥도 못 먹었고, 춥고 헐벗었어. 그리고 모든 교회를 걱정하는 매일의 압박은 빼고 말하는 거야. 누가 힘들어해? 나도 힘들어. 누가 넘어져? 내 속이 타들어가.",
"자랑해야 한다면, 내 약함을 보여주는 걸 자랑할게. 주 예수의 하나님 아버지, 영원히 찬양받으실 분이 내가 진실을 말한다는 걸 아셔. 내가 다마스쿠스에 있었을 때, 아레타 왕 아래 총독이 나를 잡으려고 도시를 봉쇄했어. 나는 성벽 창문을 통해 바구니에 담겨 내려가서 탈출해야 했어.",
],
"verseRanges": ["1-3","1-3","4-6","7-12","12-15","12-15","16-21","21-23","21-23","23-27","28-29","30-33"],
"msg_ranges": ["1-3","4-6","7-12","12-15","16-21","21-23","23-27","28-29","30-33"],
"merges": [],
"splits": [
{"msg_range": "12", "paras": [4,5], "note": "MSG 7-12와 12-15 사이 v12 겹침"},
{"msg_range": "21", "paras": [7,8], "note": "MSG 16-21과 21-23 사이 v21 겹침"},
{"msg_range": "23", "paras": [8,9], "note": "MSG 21-23과 23-27 사이 v23 겹침"},
],
"changes": [
"EN 구조 반영: MSG 헤더 2개(§가짜 하나님의 종들, §길고 외로운 많은 밤), 6개 누락 문단 복원",
"배지 수정: 30-33 (EN과 동일)",
"누락 복원: 1-3, 4-6, 7-12, 12-15, 21-23 고난 목록, 28-29, 30-33 다마스쿠스 바구니 탈출",
],
"confirmations_needed": [],
})

# ============ CHAPTER 12 ============
EN_CH.append({
"chapter": 12, "title": "God's Power in Our Weakness",
"paragraphs": [
"§Strength from Weakness",
"You know, I just have to keep bragging. It's not really helping anyone, but I can't help it. I'm going to talk about these crazy visions and revelations from the Lord. I know a guy—actually, it's me—who had this wild experience fourteen years ago. I was caught up to the third heaven. Whether it was my body or just my spirit, I don't know. Only God knows. And I know that this guy was taken up to paradise. I heard things that were so mind-blowing, I can't even repeat them. It's like, words can't even describe it.",
"That experience is something I can brag about. But when it comes to me, I'm not going to brag about anything except my weaknesses. If I did want to brag, I wouldn't be lying, because I'd be telling the truth. But I'm not going to do it, because I don't want anyone to think I'm more than what they see in me or hear from me.",
"Because of the extravagance of those revelations, and so I wouldn't get a big head, I was given the gift of a handicap to keep me in constant touch with my limitations. Satan's angel did his best to get me down; what he in fact did was push me to my knees. No danger then of walking around high and mighty! At first I didn't think of it as a gift, and begged God to remove it. Three times I did that, and then he told me, My grace is enough; it's all you need. My strength comes into its own in your weakness.",
"Once I heard that, I was glad to let it happen. I quit focusing on the handicap and began appreciating the gift. It was a case of Christ's strength moving in on my weakness. Now I take limitations in stride, and with good cheer, these limitations that cut me down to size—abuse, accidents, opposition, bad breaks. I just let Christ take over! And so the weaker I get, the stronger I become.",
"Hey, I'm back in fool mode again. But you made me do it! You should have been the ones praising me, not these fake \"super-apostles.\" I'm not saying I'm better than them, but I've got the receipts. I've done all the things a real apostle does, right in front of you, with patience and power. I did miracles, signs, and wonders. How were you guys any less blessed than the other churches? The only thing I didn't do was charge you for my services. I'm sorry about that! Please forgive me for not taking your money!",
"You're going to be seeing me for the third time now, and I'll still do what I've always done: I won't be a burden to you. I'm not after your money; I'm after you. It's the parents who are supposed to take care of the kids, not the other way around. So I'm going to be a parent to you, and I'm going to spend everything I have on you, even if it means I'm totally wiped out. If I love you more, does that mean you'll love me less?",
"Let me be honest: I never took advantage of you. But some people are saying that I was sneaky and tricked you into giving me money through Titus or someone else. Did I ever take advantage of you through any of the guys I sent? Did Titus take advantage of you? No way. We all did things the same way, with the same honest motives.",
"You're probably thinking I'm just trying to defend myself to you. But I'm not. I'm talking to God about this, and I'm telling you the truth because I love you. Everything I've done has been to help you grow stronger in your faith.",
"I have a feeling that when I come visit, I won't find you as I want you to be, and you won't find me as you want me to be. I'm afraid I'll find a lot of drama: fighting, jealousy, anger, selfishness, gossip, pride. I'm worried that when I come, God will humble me in front of you, and I'll be sad about all the people who are still stuck in their old ways, doing things they shouldn't be doing, like sleeping around, cheating, and living wild.",
],
"verseRanges": ["1-5","1-5","6","7-10","11-13","14-15","16-18","19","20-21"],
"msg_ranges": ["1-5","6","7-10","11-13","14-15","16-18","19","20-21"],
"merges": [], "splits": [],
"changes": [
"Badge fix: 1-4 → 1-5 (MSG 1-5)",
"Restored v5 content: 'I heard things that were so mind-blowing, I can't even repeat them' (was omitted)",
"Badge fix: 12-14 → 11-13 (MSG 11-13)",
"Badge fix: 14-16 → 14-15 (MSG 14-15)",
"Badge fix: 17-18 → 16-18 (MSG 16-18)",
"Badge fix: 19-20 → 19 (MSG 19)",
"Badge fix: 20-22 → 20-21 (MSG 20-21; restores v21 'God will humble me in front of you... sleeping around, cheating, and living wild')",
"Header replaced: invented §Thorn in the Flesh → MSG's §Strength from Weakness at chapter top, badge 1-5",
"Proverbs?/profanity cleanup: removed 'sucker punch', 'huge dump', 'lowkey', 'highkey' mocking slang",
],
"confirmations_needed": [],
})
KO_CH.append({
"chapter": 12, "title": "약함 속 하나님의 능력",
"paragraphs": [
"§약함에서 오는 강함",
"봐, 나는 계속 자랑할 수밖에 없어. 누구에게도 별 도움이 안 되지만, 어쩔 수 없어. 주님께 받은 이 미친 환상과 계시에 대해 말할 거야. 나는 한 사람을 알아. 사실 나야. 14년 전에 엄청난 경험을 했어. 셋째 하늘로 끌려 올라갔거든. 몸으로였는지 영으로였는지 몰라. 하나님만 아셔. 그리고 그 사람이 낙원으로 끌려 올라갔다는 걸 알아. 너무 충격적이어서 반복할 수도 없는 걸 들었어. 말로 표현할 수가 없어.",
"그 경험은 자랑할 만해. 하지만 나 자신에 대해서는 약함 말고는 자랑 안 할 거야. 자랑하고 싶다면 거짓말이 아니야. 진실을 말하는 거니까. 하지만 안 할 거야. 사람들이 나에게서 보거나 듣는 것보다 내가 더 대단하다고 생각하길 원하지 않거든.",
"그 계시들이 너무 엄청나서 내가 교만해지지 않게 하려고, 내 한계를 계속 느끼게 하는 핸디캡이라는 선물을 받았어. 사탄의 천사가 나를 쓰러뜨리려고 최선을 다했는데, 실제로 한 건 나를 무릎 꿇게 한 거야. 그러니 잘난 척하고 다닐 위험은 없지! 처음에는 그걸 선물이라고 생각 안 하고, 없애달라고 하나님께 빌었어. 세 번이나 그랬어. 그러자 그분이 말씀하셨어. '내 은혜가 충분해. 그게 네가 필요한 전부야. 내 능력은 네 약함에서 온전히 드러나.'",
"그 말을 듣자 기꺼이 그렇게 되게 내버려뒀어. 핸디캡에 집중하기를 그만두고 선물을 감사하기 시작했지. 그리스도의 능력이 내 약함에 들어온 거야. 이제는 나를 작아지게 하는 이런 한계들을 웃으면서 받아들여. 학대, 사고, 반대, 불운 같은 것들 말야. 그냥 그리스도께 맡기는 거야! 그래서 내가 약해질수록 강해지는 거야.",
"자, 다시 바보 모드야. 근데 너희가 날 이렇게 만든 거야! 너희가 나를 칭찬했어야 했어. 이 가짜 '슈퍼 사도'들이 아니라. 내가 걔네보다 낫다는 게 아니라, 증거는 있어. 진짜 사도가 하는 모든 일을 너희 앞에서 인내와 능력으로 다 했어. 기적과 표적과 기사를 행했지. 너희가 다른 교회들보다 어떻게 덜 복 받았어? 내가 안 한 건 딱 하나, 너희에게 돈을 안 받았다는 거야. 그거 미안해! 돈 안 받은 거 용서해줘!",
"이제 세 번째로 너희를 보게 될 텐데, 나는 항상 하던 대로 할 거야. 너희에게 부담 주지 않을 거야. 나는 너희 돈이 아니라 너희가 필요해. 아이들을 돌보는 건 부모의 몫이지, 반대가 아니야. 그러니까 나는 너희의 부모가 될 거야. 완전히 지쳐버리더라도 가진 걸 다 너희에게 쓸 거야. 내가 너희를 더 사랑하면, 너희는 나를 덜 사랑하게 되는 거야?",
"솔직히 말할게. 나는 너희를 절대 이용하지 않았어. 하지만 어떤 사람들은 내가 교활해서 디도나 다른 사람을 통해 너희 돈을 뜯어냈다고 말해. 내가 보낸 사람들을 통해 너희를 이용한 적 있어? 디도가 너희를 이용했어? 절대 아냐. 우리는 모두 같은 방식으로, 같은 정직한 동기로 일했어.",
"너희는 내가 너희에게 변명하려는 거라고 생각하겠지. 근데 아냐. 나는 하나님께 이걸 말씀드리고 있는 거야. 너희를 사랑하니까 진실을 말하는 거야. 내가 한 모든 건 너희 믿음이 더 강해지게 돕기 위한 거였어.",
"내가 방문할 때, 너희가 내가 원하는 모습이 아니고, 내가 너희가 원하는 모습이 아닐 것 같은 느낌이 들어. 가서 싸움, 질투, 분노, 이기심, 험담, 교만이 가득한 드라마를 보게 될까 봐 두려워. 내가 가면 하나님이 너희 앞에서 나를 겸손하게 하시고, 옛 방식에 갇혀 해서는 안 될 일을 하는 사람들 때문에 슬퍼하게 될까 봐 걱정이야. 문란하게 자고, 속이고, 방탕하게 사는 것들 말야.",
],
"verseRanges": ["1-5","1-5","6","7-10","11-13","14-15","16-18","19","20-21"],
"msg_ranges": ["1-5","6","7-10","11-13","14-15","16-18","19","20-21"],
"merges": [], "splits": [],
"changes": [
"EN 구조 반영: §약함에서 오는 강함",
"배지 수정: 1-5, 11-13, 14-15, 16-18, 19, 20-21 (EN과 동일)",
"v5 복원: '너무 충격적이어서 반복할 수도 없는 걸 들었어'",
"v21 복원: '문란하게 자고, 속이고, 방탕하게 사는 것들'",
],
"confirmations_needed": [],
})

# ============ CHAPTER 13 ============
EN_CH.append({
"chapter": 13, "title": "He's Alive and He's Got You",
"paragraphs": [
"§He's Alive Now!",
"Hey, this is gonna be my third visit to you guys. And you know what they say: \"Two or three witnesses are enough to prove something's true.\" I've already warned you twice, and I'm warning you again now. If I come back, I'm not going to go easy on anyone who's still living in sin. You want proof that Christ is speaking through me? You'll get it. He's not weak when he's dealing with you; he's powerful. He was crucified in weakness, but now he's alive by God's power. We're weak like he was, but we'll be alive with him by God's power, and we'll deal with you from a position of strength.",
"Here's a thought: test yourselves. Make sure you're really in the faith. Don't just take my word for it; check it out for yourselves. Do you realize that Jesus Christ is in you? Unless, of course, you're failing the test. But I hope you'll see that we're not failing. I'm praying to God that you won't do anything wrong, not to make us look good, but so you can do what's right, even if it looks like we've failed. We can't do anything against the truth; we can only do what's right. We're happy when we're weak and you're strong. And we're praying for you to become all that God wants you to be.",
"I'm writing this while I'm away so that when I come, I won't have to be harsh. The Lord gave me authority to build you up, not to tear you down.",
"And that's about it, friends. Be cheerful. Keep things in good repair. Keep your spirits up. Think in harmony. Be agreeable. Do all that, and the God of love and peace will be with you for sure. Greet one another with a holy embrace. All the believers here say hello. The amazing grace of the Master, Jesus Christ, the extravagant love of God, the intimate friendship of the Holy Spirit, be with all of you.",
"May the grace of the Lord Jesus Christ, the love of God, and the fellowship of the Holy Spirit be with you all.",
],
"verseRanges": ["1-4","1-4","5-9","10","11-13","14"],
"msg_ranges": ["1-4","5-9","10","11-13","14"],
"merges": [], "splits": [],
"changes": [
"Restored v4 content: 'He was crucified in weakness, but now he's alive by God's power. We're weak like he was, but we'll be alive with him by God's power' (was omitted from old 1-3 para)",
"Badge fix: 1-3 → 1-4 (MSG 1-4)",
"Badge fix: 4-8 → 5-9 (MSG 5-9; restores v9 'We're happy when we're weak and you're strong. And we're praying for you to become all that God wants you to be.')",
"Badge fix: 8-9 → 10 (MSG 10)",
"Badge fix: 10-13 → 11-13 (MSG 11-13; restores v12 'Greet one another with a holy embrace. All the believers here say hello.')",
"Restored v14 benediction as its own para (was omitted)",
"Header replaced: invented §Final Warnings → MSG's §He's Alive Now! at chapter top, badge 1-4",
"Restored 'Two or three witnesses are enough to prove something's true' (was omitted)",
],
"confirmations_needed": [],
})
KO_CH.append({
"chapter": 13, "title": "살아계시고 너희와 함께하셔",
"paragraphs": [
"§그분은 지금 살아계셔!",
"자, 이번이 너희에게 세 번째 방문이 될 거야. 속담도 있잖아. '두세 명의 증인이 있으면 진실이 증명된다.' 이미 두 번 경고했고, 지금 다시 경고하는 거야. 내가 돌아가면 죄 가운데 사는 사람에게 쉽게 넘어가지 않을 거야. 그리스도가 나를 통해 말씀하신다는 증거를 원해? 보여줄게. 그분은 너희를 다루실 때 약하지 않으셔. 강하셔. 그분은 약함 가운데 십자가에 못 박히셨지만, 이제 하나님의 능력으로 살아계셔. 우리도 그분처럼 약하지만, 하나님의 능력으로 그분과 함께 살게 될 거야. 그리고 강자의 자리에서 너희를 대할 거야.",
"생각해봐. 너희 자신을 시험해봐. 정말 믿음 안에 있는지 확인해. 내 말만 믿지 말고 직접 확인해봐. 예수 그리스도가 너희 안에 계시다는 걸 알아? 물론 시험에 떨어지는 게 아니라면 말야. 하지만 우리는 떨어지지 않는다는 걸 너희가 알게 되길 바라. 너희가 잘못된 일을 하지 않길 하나님께 기도해. 우리를 좋아 보이게 하려는 게 아니라, 우리가 실패한 것처럼 보여도 너희가 옳은 일을 할 수 있게 하려는 거야. 우리는 진리에 맞서 아무것도 할 수 없어. 옳은 일만 할 수 있지. 우리가 약하고 너희가 강할 때 기뻐. 그리고 너희가 하나님이 원하시는 모습이 되길 기도해.",
"내가 없는 동안 이걸 쓰는 건, 내가 갔을 때 엄하게 대하지 않으려는 거야. 주님이 나에게 주신 권위는 너희를 세우라고 주신 거지, 무너뜨리라고 주신 게 아냐.",
"그리고 대충 이게 전부야, 친구들. 기뻐해. 잘 정비해. 기운 내. 조화롭게 생각해. 잘 지내. 그걸 다 하면, 사랑과 평화의 하나님이 분명 너희와 함께하실 거야. 거룩한 포옹으로 서로 인사해. 여기 있는 모든 성도가 안부를 전해. 주 예수 그리스도의 놀라운 은혜, 하나님의 넘치는 사랑, 성령님의 친밀한 교제가 너희 모두와 함께하길.",
"주 예수 그리스도의 은혜와 하나님의 사랑과 성령님의 교제가 너희 모두와 함께하길.",
],
"verseRanges": ["1-4","1-4","5-9","10","11-13","14"],
"msg_ranges": ["1-4","5-9","10","11-13","14"],
"merges": [], "splits": [],
"changes": [
"EN 구조 반영: §그분은 지금 살아계셔!, v14 축도 복원",
"배지 수정: 1-4, 5-9, 10, 11-13 (EN과 동일)",
"v4 복원: '그분은 약함 가운데 십자가에 못 박히셨지만, 이제 하나님의 능력으로 살아계셔'",
"v9 복원: '우리가 약하고 너희가 강할 때 기뻐'",
"v12 복원: '거룩한 포옹으로 서로 인사해'",
],
"confirmations_needed": [],
})

# ============ WRITE FILES ============
def write_book(chapters, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"chapters": chapters}, f, ensure_ascii=False, indent=2)
        f.write("\n")

write_book(EN_CH, "/home/hatch/workspace/teenz-bible-review/fixes/en_2Corinthians.json")
write_book(KO_CH, "/home/hatch/workspace/teenz-bible-review/fixes/ko_2Corinthians.json")
print("chapters:", len(EN_CH), len(KO_CH))
print("EN paras:", sum(len(c["paragraphs"]) for c in EN_CH))
print("KO paras:", sum(len(c["paragraphs"]) for c in KO_CH))
