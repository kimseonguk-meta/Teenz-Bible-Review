#!/usr/bin/env python3
"""Repair truncated chapters 9-12 in en/ko 2Corinthians fix files + ch13 benediction duplication."""
import json

EN = {}
KO = {}

# ---------------- EN CHAPTER 9 ----------------
EN[9] = {
"chapter": 9, "title": "Generous Giving Pays Off",
"paragraphs": [
"Hey, I don't even need to write any more about this relief offering for the poor Christians. I'd just be repeating myself. I know you're on board and ready to go. I've been bragging about you all through Macedonia, telling them, \"Achaia has been ready to go on this since last year.\" Your enthusiasm has spread to most of them by now.",
"Now I'm sending the brothers to make sure you're ready, just like I said you would be, so my bragging doesn't turn out to be just hot air. If some Macedonians happened to drop in with me and found you weren't prepared, we'd all be red-faced\u2014you and us\u2014for acting so sure of ourselves.",
"So to make sure there's no slipup, I've recruited these brothers as an advance team to get you and your promised offering all ready before I get there. I want you to have all the time you need to make this offering in your own way. I don't want anything forced or hurried at the last minute.",
"Remember: A stingy planter gets a stingy crop; a lavish planter gets a lavish crop. I want each of you to take plenty of time to think it over and make up your own mind what you'll give. That'll protect you from sob stories and arm-twisting. God loves it when the giver delights in the giving.",
"God can pour on the blessings in astonishing ways so that you're ready for anything and everything\u2014more than ready to do what needs to be done. As one psalmist puts it, \"He throws caution to the winds, giving to the needy in reckless abandon. His right-living, right-giving ways never run out, never wear out.\" This most generous God who gives seed to the farmer that becomes bread for your meals is more than extravagant with you. He gives you something you can then give away, which grows into full-formed lives, robust in God, wealthy in every way, so that you can be generous in every way, producing with us great praise to God.",
"Carrying out this social relief work is about way more than just meeting the basic needs of poor Christians. It also produces abundant, overflowing thanksgiving to God. This relief offering pushes you to live at your very best, showing your gratitude to God by openly obeying the plain meaning of the Message of Christ. You show your gratitude through your generous offerings to your needy brothers and sisters\u2014and really, toward everyone. Meanwhile, moved by the extravagance of God in your lives, they'll respond by praying for you in passionate intercession for whatever you need. Thank God for this gift, his gift. No language can praise it enough!",
],
"verseRanges": ["1-2","3-5","3-5","6-7","8-11","12-15"],
"msg_ranges": ["1-2","3-5","6-7","8-11","12-15"],
"merges": [],
"splits": [
{"msg_range": "3-5", "paras": [1,2], "note": "MSG 3-5: the red-faced/hot-air part and the advance-team part"},
],
"changes": [
"Badge fix: 1-5 -> 1-2 (MSG 1-2)",
"Badge fix: 5-8 -> 6-7 (MSG 6-7)",
"Badge fix: 8-10 -> 8-11 (MSG 8-11)",
"Restructured MSG 3-5: two paras badged 3-5 with splits declaration",
"Restored 6-7: 'A stingy planter gets a stingy crop; a lavish planter gets a lavish crop'",
"Restored 8-11: the psalmist quote and 'more than extravagant with you'",
"Restored 12-15: 'Carrying out this social relief work... No language can praise it enough!'",
],
"confirmations_needed": [],
}

# ---------------- EN CHAPTER 10 ----------------
EN[10] = {
"chapter": 10, "title": "Not Your Average Apostle",
"paragraphs": [
"\u00a7Tearing Down Barriers",
"And now a personal but most urgent matter. I write in the gentle but firm spirit of Christ. I hear I'm being painted as cringing and wishy-washy when I'm with you, but harsh and demanding when I'm at a safe distance writing letters. Please don't force me to take a hard line when I'm with you. Don't think I'll hesitate for a single minute to stand up to those who say I'm an unprincipled opportunist. Then they'll have to eat their words.",
"The world is unprincipled. It's dog-eat-dog out there! The world doesn't fight fair. But we don't live or fight our battles that way\u2014never have and never will. The tools of our trade aren't for marketing or manipulation, but they are for demolishing that entire massively corrupt culture. We use our powerful God-tools for smashing warped philosophies, tearing down barriers erected against the truth of God, fitting every loose thought and emotion and impulse into the structure of life shaped by Christ. Our tools are ready at hand for clearing the ground of every obstruction and building lives of obedience into maturity.",
"You stare and stare at the obvious, but you can't see the forest for the trees. If you're looking for a clear example of someone on Christ's side, why do you so quickly cut me out? Believe me, I'm quite sure of my standing with Christ. You may think I overstate the authority he gave me, but I'm not backing off. Every bit of my commitment is for building you up, after all, not tearing you down.",
"And what's this talk about me bullying you with my letters? \"His letters are brawny and potent, but in person he's a weakling and mumbles when he talks.\" Such talk won't survive scrutiny. What we write when away, we do when present. We're the exact same people, absent or present, in letter or in person.",
"We're not, understand, putting ourselves in a league with those who boast that they're our superiors. We wouldn't dare do that. But in all this comparing and grading and competing, they quite miss the point.",
"We aren't making outrageous claims here. We're sticking to the limits of what God has set for us. But there's no question those limits reach to and include you. We're not moving into someone else's territory. We were already there with you, weren't we? We were the first ones to get there with the Message of Christ, right? So how can there be any question of overstepping our bounds by writing or visiting you?",
"We're not barging in on the rightful work of others, interfering with their ministries, demanding a place in the sun with them. What we're hoping for is that as your lives grow in faith, you'll play a part within our expanding work. And we'll all still be within the limits God sets as we proclaim the Message in countries beyond Corinth. But we have no intention of moving in on what others have done and taking credit for it. \"If you want to claim credit, claim it for God.\" What you say about yourself means nothing in God's work. It's what God says about you that makes the difference.",
],
"verseRanges": ["1-2","1-2","3-6","7-8","9-11","12","13-14","15-18"],
"msg_ranges": ["1-2","3-6","7-8","9-11","12","13-14","15-18"],
"merges": [],
"splits": [
{"msg_range": "1-2", "paras": [0,1], "note": "MSG 1-2: header + the 'cringing when present, harsh in letters' opener"},
],
"changes": [
"Badge fix: 4-6 -> 3-6 (MSG 3-6)",
"Badge fix: 8-9 -> 7-8 (MSG 7-8; restores 'you can't see the forest for the trees')",
"Badge fix: 10-12 -> 9-11 (MSG 9-11)",
"Badge fix: 12-13 -> 12 (MSG 12; restores 'comparing and grading and competing, they quite miss the point')",
"Badge fix: 14-15 -> 13-14 (MSG 13-14; restores 'We were the first ones to get there with the Message of Christ')",
"Restored 15-18 as its own para: 'We're not barging in on the rightful work of others...'",
"Header replaced: invented \u00a7Paul's Authority -> MSG's \u00a7Tearing Down Barriers at chapter top, badge 1-2",
],
"confirmations_needed": [],
}

# ---------------- EN CHAPTER 11 ----------------
EN[11] = {
"chapter": 11, "title": "Don't Get Played by Fakes",
"paragraphs": [
"\u00a7Pseudo-Servants of God",
"Will you put up with a little foolish aside from me? Please, just for a moment. The thing that has me so upset is that I care about you so much\u2014this is the passion of God burning inside me! I promised your hand in marriage to Christ, presented you as a pure virgin to her husband. And now I'm afraid that exactly as the Snake seduced Eve with his smooth tongue, you are being lured away from the simple purity of your love for Christ.",
"It seems that if someone shows up preaching quite another Jesus than we preached\u2014different spirit, different message\u2014you put up with him quite nicely. But if you put up with these big-shot \"apostles,\" why can't you put up with simple me? I'm as good as they are. It's true I don't have their voice; I haven't mastered that smooth eloquence that impresses you so much. But when I do open my mouth, I at least know what I'm talking about. We haven't kept anything back. We let you in on everything.",
"I wonder, did I make a bad mistake proclaiming God's Message to you without asking for anything in return, serving you free of charge so you wouldn't be inconvenienced by me? It turns out the other churches paid my way so you could have a free ride. Not once during my time among you did anyone have to lift a finger to help me out. My needs were always supplied by the believers from Macedonia. I was careful never to be a burden to you, and I never will be\u2014you can count on it. With Christ as my witness, it's a point of honor with me, and I'm not going to keep it quiet just to protect you from what the neighbors will think. It's not that I don't love you; God knows I do. I'm just trying to keep things open and honest between us.",
"\u00a7Many a Long and Lonely Night",
"And I'm not changing my position on this. I'd die before taking your money. I'm giving nobody grounds for lumping me in with those money-grubbing \"preachers,\" vaunting themselves as something special. They're a sorry bunch\u2014pseudo-apostles, lying preachers, crooked workers\u2014posing as Christ's agents but sham to the core. And no wonder! Satan does it all the time, dressing up as a beautiful angel of light. So it shouldn't surprise us when his servants masquerade as servants of God. But they're not getting by with anything. They'll pay for it in the end.",
"Let me come back to where I started\u2014and don't hold it against me if I continue to sound a little foolish. Or if you'd rather, just accept that I am a fool and let me rant on a little. I didn't learn this kind of talk from Christ. Oh no, it's a bad habit I picked up from the three-ring preachers that are so popular these days. Since you sit there in the judgment seat observing all these shenanigans, you can afford to humor an occasional fool who happens along. You have such admirable tolerance for impostors who rob your freedom, rip you off, steal you blind, put you down\u2014even slap your face! I shouldn't admit it to you, but our stomachs aren't strong enough to tolerate that kind of stuff.",
"Since you admire the egomaniacs of the pulpit so much (remember, this is your old friend, the fool, talking), let me try my hand at it. Do they brag of being Hebrews, Israelites, the pure race of Abraham? I'm their match. Are they servants of Christ? I can go them one better. (I can't believe I'm saying these things. It's crazy to talk this way! But I started, and I'm going to finish.)",
"I've worked much harder, been jailed more often, beaten up more times than I can count, and at death's door time after time. I've been flogged five times with the Jews' thirty-nine lashes, beaten by Roman rods three times, pummeled with rocks once. I've been shipwrecked three times, and immersed in the open sea for a night and a day. In hard traveling year in and year out, I've had to ford rivers, fend off robbers, struggle with friends, struggle with foes. I've been at risk in the city, at risk in the country, endangered by desert sun and sea storm, and betrayed by those I thought were my brothers. I've known drudgery and hard labor, many a long and lonely night without sleep, many a missed meal, blasted by the cold, naked to the weather.",
"And that's not the half of it, when you throw in the daily pressures and anxieties of all the churches. When someone gets to the end of his rope, I feel the desperation in my bones. When someone is duped into sin, an angry fire burns in my gut.",
"If I have to \"brag\" about myself, I'll brag about the humiliations that make me like Jesus. The eternal and blessed God and Father of our Master Jesus knows I'm not lying. Remember the time I was in Damascus and the governor of King Aretas posted guards at the city gates to arrest me? I crawled through a window in the wall, was let down in a basket, and had to run for my life.",
],
"verseRanges": ["1-3","1-3","4-6","7-12","12-15","12-15","16-21","21-23","23-27","28-29","30-33"],
"msg_ranges": ["1-3","4-6","7-12","12-15","16-21","21-23","23-27","28-29","30-33"],
"merges": [],
"splits": [
{"msg_range": "12", "paras": [3,5], "note": "MSG overlaps v12 between 7-12 and 12-15"},
{"msg_range": "21", "paras": [6,7], "note": "MSG overlaps v21 between 16-21 and 21-23"},
{"msg_range": "23", "paras": [7,8], "note": "MSG overlaps v23 between 21-23 and 23-27"},
],
"changes": [
"Restored all MSG paragraphs: old file had no paras for MSG 1-3, 4-6, 7-12, 12-15 (4 missing paragraphs restored)",
"Badge fix: 30-31 -> 30-33 (MSG 30-33; v32-33 Damascus basket escape now properly badged)",
"Badge fix: hardship list now badged 23-27 (MSG 23-27); 28-29 its own para",
"Headers replaced: invented \u00a7True Apostles vs Fake Ones -> MSG's \u00a7Pseudo-Servants of God (badge 1-3) and MSG's \u00a7Many a Long and Lonely Night (badge 12-15) at MSG positions",
"Restored 21-23: 'Do they brag of being Hebrews, Israelites, the pure race of Abraham? I'm their match'",
"Restored 23-27: full hardship list ('flogged five times with the Jews' thirty-nine lashes... naked to the weather')",
"Restored 28-29: 'When someone gets to the end of his rope, I feel the desperation in my bones'",
],
"confirmations_needed": [],
}

# ---------------- EN CHAPTER 12 (full rewrite) ----------------
EN[12] = {
"chapter": 12, "title": "God's Power in Our Weakness",
"paragraphs": [
"\u00a7Strength from Weakness",
"You've forced me to talk this way, and I do it against my better judgment. But now that we're at it, I may as well bring up the matter of visions and revelations that God gave me. For instance, I know a man who, fourteen years ago, was seized by Christ and swept in ecstasy to the heights of heaven. I really don't know if this took place in the body or out of it; only God knows. I also know that this man was hijacked into paradise\u2014again, whether in or out of the body, I don't know; God knows. There he heard the unspeakable spoken, but was forbidden to tell what he heard. This is the man I want to talk about. But about myself, I'm not saying another word apart from the humiliations.",
"If I had a mind to brag a little, I could probably do it without looking ridiculous, and I'd still be speaking plain truth all the way. But I'll spare you. I don't want anyone imagining me as anything other than the fool you'd encounter if you saw me on the street or heard me talk.",
"Because of the extravagance of those revelations, and so I wouldn't get a big head, I was given the gift of a handicap to keep me in constant touch with my limitations. Satan's angel did his best to get me down; what he in fact did was push me to my knees. No danger then of walking around high and mighty! At first I didn't think of it as a gift, and begged God to remove it. Three times I did that, and then he told me, \"My grace is enough; it's all you need. My strength comes into its own in your weakness.\" Once I heard that, I was glad to let it happen. I quit focusing on the handicap and began appreciating the gift. It was a case of Christ's strength moving in on my weakness. Now I take limitations in stride, and with good cheer, these limitations that cut me down to size\u2014abuse, accidents, opposition, bad breaks. I just let Christ take over! And so the weaker I get, the stronger I become.",
"Well, now I've done it! I've made a complete fool of myself by going on like this. But it's not all my fault; you put me up to it. You should have been doing this for me, sticking up for me and commending me instead of making me do it for myself. You know from personal experience that even if I'm a nobody, a nothing, I wasn't second-rate compared to those big-shot apostles you're so taken with. All the signs that mark a true apostle were in evidence while I was with you through both good times and bad: signs of portent, signs of wonder, signs of power. Did you get less of me or of God than any of the other churches? The only thing you got less of was less responsibility for my upkeep. Well, I'm sorry. Forgive me for depriving you.",
"Everything is in readiness now for this, my third visit to you. But don't worry about it; you won't have to put yourselves out. I'll be no more of a bother to you this time than on the other visits. I have no interest in what you have\u2014only in you. Children shouldn't have to look out for their parents; parents look out for the children. I'd be most happy to empty my pockets, even mortgage my life, for your good. So how does it happen that the more I love you, the less I'm loved?",
"And why is it that I keep coming across these whiffs of gossip about how my self-support was a front behind which I worked an elaborate scam? Where's the evidence? Did I cheat or trick you through anyone I sent? I asked Titus to visit, and sent some brothers along. Did they swindle you out of anything? And haven't we always been just as aboveboard, just as honest?",
"I hope you don't think that all along we've been making our defense before you, the jury. You're not the jury; God is the jury\u2014God revealed in Christ\u2014and we make our case before him. And we've gone to all the trouble of supporting ourselves so that we won't be in the way or get in the way of your growing up.",
"I do admit that I have fears that when I come you'll disappoint me and I'll disappoint you, and in frustration with each other everything will fall to pieces\u2014quarrels, jealousy, flaring tempers, taking sides, angry words, vicious rumors, swelled heads, and general bedlam. I don't look forward to a second humiliation by God among you, compounded by hot tears over that crowd that keeps sinning over and over in the same old ways, who refuse to turn away from the pigsty of evil, sexual disorder, and indecency in which they wallow.",
],
"verseRanges": ["1-5","1-5","6","7-10","11-13","14-15","16-18","19","20-21"],
"msg_ranges": ["1-5","6","7-10","11-13","14-15","16-18","19","20-21"],
"merges": [],
"splits": [],
"changes": [
"Badge fix: 1-4 -> 1-5 (MSG 1-5)",
"Restored v5: 'There he heard the unspeakable spoken, but was forbidden to tell what he heard'",
"Restored v6: 'I don't want anyone imagining me as anything other than the fool you'd encounter if you saw me on the street'",
"Badge fix: 12-14 -> 11-13 (MSG 11-13)",
"Badge fix: 14-16 -> 14-15 (MSG 14-15; restores 'I'd be most happy to empty my pockets, even mortgage my life, for your good')",
"Badge fix: 17-18 -> 16-18 (MSG 16-18; restores 'Did they swindle you out of anything?')",
"Restored v19: 'You're not the jury; God is the jury\u2014God revealed in Christ'",
"Restored v20-21: 'quarrels, jealousy, flaring tempers... the pigsty of evil, sexual disorder, and indecency'",
"Header replaced: invented \u00a7Thorn in the Flesh -> MSG's \u00a7Strength from Weakness at chapter top, badge 1-5",
],
"confirmations_needed": [],
}

# ---------------- KO CHAPTER 9 ----------------
KO[9] = {
"chapter": 9, "title": "관대한 나눔의 결실",
"paragraphs": [
"이 가난한 성도들을 위한 구제 헌금에 대해 더 쓰면 그냥 반복이 될 거야. 너희가 찬성이고 준비됐다는 걸 아니까. 나는 마케도니아 전역에서 너희를 자랑했어. '아가야는 작년부터 이 일에 준비됐어'라고 말하면서 말야. 너희 열정은 이제 대부분에게 퍼졌어.",
"이제 이 형제들을 보내서 너희가 준비됐는지 확인하려는 거야. 내가 말한 대로 말야. 내 자랑이 그냥 허풍으로 드러나지 않게 하려고. 마케도니아 사람들이 나랑 같이 갑자기 들렀는데 너희가 준비 안 돼 있으면, 우리 모두 얼굴이 빨개질 거야. 너희도 나도. 그렇게 확신에 차 있었는데 말야.",
"실수가 없게 하려고, 이 형제들을 선발대로 뽑아서 내가 가기 전에 너희와 약속한 헌금을 다 준비하게 했어. 너희 방식대로 헌금할 충분한 시간을 갖길 바라. 마지막 순간에 억지로 급하게 하는 건 원하지 않아.",
"기억해. 인색하게 뿌리는 사람은 인색하게 거두고, 아낌없이 뿌리는 사람은 아낌없이 거둬. 너희 각자가 충분히 시간을 갖고 생각해서, 얼마를 줄지 스스로 정하길 바라. 그러면 눈물겨운 사연이나 팔 비틀기에서 보호받을 수 있어. 하나님은 주는 사람이 기쁘게 주는 걸 사랑하셔.",
"하나님은 놀라운 방식으로 복을 쏟아부으셔서 너희가 어떤 일이든, 모든 일에 준비되게, 아니 넘치게 준비되게 하실 수 있어. 한 시편 기자가 말했듯이 말야. '그는 조심성을 바람에 날려버리고, 궁핍한 사람들에게 무모할 정도로 나눠준다. 그의 올바르게 살고 올바르게 주는 방식은 절대 마르지 않고, 절대 닳지 않는다.' 농부에게 씨를 주셔서 너희 식탁의 빵이 되게 하시는 이 가장 관대하신 하나님이 너희에게는 더욱 넘치게 주셔. 그분이 너희에게 주신 걸 너희가 다시 나눠줄 수 있게 하시는데, 그게 자라서 완전한 삶이 돼. 하나님 안에서 튼튼하고, 모든 면에서 부유해서, 모든 면에서 관대할 수 있게. 그래서 우리와 함께 하나님께 큰 찬양을 올려드리는 거야.",
"이 사회 구제 일을 하는 건 가난한 성도들의 기본적인 필요를 채우는 것보다 훨씬 더 큰 의미가 있어. 하나님께 풍성하고 넘치는 감사를 만들어내거든. 이 구제 헌금은 너희가 최선을 다해 살게 하는 자극이야. 그리스도의 메시지라는 분명한 뜻에 공개적으로 순종하면서 하나님께 감사하는 걸 보여주는 거지. 너희는 궁핍한 형제자매들에게, 아니 사실 모든 사람에게 관대하게 나누면서 감사함을 보여. 그러는 동안 그들은 너희 삶에 나타난 하나님의 넘치는 모습을 보고 감동받아, 너희에게 필요한 모든 걸 위해 열정적으로 중보 기도하며 응답할 거야. 이 선물, 그분의 선물에 하나님께 감사하자. 어떤 말로도 충분히 찬양할 수 없어!",
],
"verseRanges": ["1-2","3-5","3-5","6-7","8-11","12-15"],
"msg_ranges": ["1-2","3-5","6-7","8-11","12-15"],
"merges": [],
"splits": [
{"msg_range": "3-5", "paras": [1,2], "note": "MSG 3-5: 얼굴 빨개지는 부분과 선발대 부분"},
],
"changes": [
"EN 구조 반영: 3-5 분리",
"배지 수정: 1-2, 6-7, 8-11 (EN과 동일)",
"6-7 복원: '인색하게 뿌리는 사람은 인색하게 거두고'",
"8-11 복원: 시편 인용과 '더욱 넘치게 주셔'",
"12-15 복원: '어떤 말로도 충분히 찬양할 수 없어!'",
],
"confirmations_needed": [],
}

# ---------------- KO CHAPTER 10 ----------------
KO[10] = {
"chapter": 10, "title": "평범하지 않은 사도",
"paragraphs": [
"\u00a7장벽을 허물다",
"이제 개인적이지만 아주 긴급한 얘기를 할게. 그리스도의 온유하지만 단호한 영으로 쓰는 거야. 내가 너희랑 같이 있을 때는 굽실거리고 우유부단한 것처럼 그려지지만, 안전하게 멀리서 편지 쓸 때는 가혹하고 요구가 많다는 얘기를 들었어. 내가 너희랑 같이 있을 때 강경하게 나오게 만들지 마. 내가 원칙 없는 기회주의자라고 말하는 사람들에게 한순간도 주저하지 않고 맞설 거라고 생각하지 마. 그러면 걔네는 자기 말을 주워담아야 할 거야.",
"세상은 원칙이 없어. 완전 약육강식이야! 세상은 정정당당하게 싸우지 않아. 하지만 우리는 그렇게 살지도 싸우지도 않아. 예전에도 안 그랬고 앞으로도 안 그럴 거야. 우리 도구는 마케팅이나 조종을 위한 게 아니라, 완전히 부패한 그 거대한 문화를 통째로 무너뜨리는 거야. 우리는 하나님의 강력한 도구를 써서 뒤틀린 철학을 박살 내고, 하나님의 진리에 맞서 세워진 장벽을 허물고, 제멋대로인 모든 생각과 감정과 충동을 그리스도가 만드신 삶의 구조에 끼워 맞추는 거야. 우리의 도구는 모든 장애물을 치우고 순종의 삶을 성숙하게 세우는 일에 언제든 준비돼 있어.",
"너희는 뻔한 것만 뚫어져라 보면서, 나무만 보고 숲을 못 봐. 그리스도 편에 선 사람의 분명한 예를 찾는다면, 왜 나를 그렇게 빨리 제외시켜? 믿어줘, 나는 그리스도와의 관계에 완전 확신해. 그분이 주신 권위를 과장한다고 생각할지 몰라도, 나는 물러서지 않아. 내 헌신의 모든 부분은 결국 너희를 세우기 위한 거야. 무너뜨리기 위한 게 아니야.",
"내가 편지로 너희를 괴롭힌다는 얘기는 뭐야? '편지는 근육질이고 강력하지만, 실제로 만나면 완전 약골이고 말할 때 웅얼거려.' 그런 얘기는 검증을 버티지 못해. 우리가 멀리서 쓰는 걸 가까이서도 해. 우리는 같은 사람이야. 있든 없든, 편지든 직접이든 말야.",
"알아둬, 우리는 자기가 우리보다 우월하다고 자랑하는 사람들과 같은 리그에 두지 않아. 감히 그러지 않아. 하지만 온갖 비교와 등급 매기기와 경쟁 속에서, 걔네는 핵심을 완전히 놓치고 있어.",
"우리는 터무니없는 주장을 하는 게 아냐. 하나님이 정해주신 한계 안에 머물고 있어. 하지만 그 한계가 너희까지 포함한다는 건 의심의 여지가 없어. 우리는 남의 영역으로 들어가는 게 아냐. 우리는 이미 너희와 함께 있었잖아, 맞지? 그리스도의 메시지를 들고 제일 먼저 도착한 게 우리였잖아, 맞지? 그러니까 편지를 쓰거나 방문한다고 해서 선을 넘는다는 얘기가 어떻게 나올 수 있어?",
"우리는 다른 사람의 정당한 일을 가로채거나, 그들의 사역을 방해하거나, 그들과 함께 햇볕 아래 자리를 요구하지 않아. 우리가 바라는 건 너희 삶이 믿음 안에서 자라면서, 우리의 확장되는 일 안에서 너희가 역할을 하게 되는 거야. 그리고 우리는 모두 하나님이 정하신 한계 안에서 고린도를 넘어선 나라들에 메시지를 전할 거야. 하지만 다른 사람이 한 일에 끼어들어 공을 가로챌 생각은 없어. '자랑하고 싶으면 하나님을 자랑하라.' 하나님의 일에서 네가 스스로 말하는 건 아무 의미가 없어. 하나님이 너에 대해 말씀하시는 게 차이를 만들어.",
],
"verseRanges": ["1-2","1-2","3-6","7-8","9-11","12","13-14","15-18"],
"msg_ranges": ["1-2","3-6","7-8","9-11","12","13-14","15-18"],
"merges": [],
"splits": [
{"msg_range": "1-2", "paras": [0,1], "note": "MSG 1-2: 헤더 + '함께 있을 땐 굽실, 편지에서는 가혹' 오프너"},
],
"changes": [
"EN 구조 반영: \u00a7장벽을 허물다, 1-2 분리",
"배지 수정: 3-6, 7-8, 9-11, 12, 13-14, 15-18 (EN과 동일)",
"12 복원: '비교와 등급 매기기와 경쟁 속에서, 걔네는 핵심을 완전히 놓치고 있어'",
"13-14 복원: '그리스도의 메시지를 들고 제일 먼저 도착한 게 우리였잖아'",
],
"confirmations_needed": [],
}

# ---------------- KO CHAPTER 11 ----------------
KO[11] = {
"chapter": 11, "title": "가짜한테 속지 마",
"paragraphs": [
"\u00a7가짜 하나님의 종들",
"내 바보 같은 얘기 좀 들어줄래? 잠깐만. 나를 이렇게 화나게 하는 건 너희를 너무 아끼기 때문이야. 이건 내 안에서 타오르는 하나님의 열정이야! 나는 너희를 그리스도께 시집보내기로 약속했어. 순결한 신부를 신랑에게 바치듯이 말야. 그런데 지금 걱정돼. 뱀이 매끈한 혀로 하와를 유혹했던 것처럼, 너희가 그리스도를 향한 단순하고 순수한 사랑에서 벗어나 유혹받고 있는 게 아닐까 해서 말야.",
"누군가 나타나서 우리가 전한 것과는 완전히 다른 예수를 전하는데, 다른 영, 다른 메시지인데도 너희는 그를 아주 잘 받아들이는 것 같아. 그런데 이 잘난 척하는 '사도'들은 받아들이면서, 평범한 나는 왜 못 받아줘? 나도 걔네만큼 잘해. 걔네처럼 말은 잘 못 해. 너희를 감동시키는 그 매끈한 말솜씨는 못 배웠어. 하지만 내가 입을 열 때는 적어도 아는 얘기를 해. 우리는 아무것도 숨기지 않았어. 모든 걸 다 알려줬어.",
"내가 하나님의 메시지를 전하면서 대가를 바라지 않고, 너희에게 폐 끼치지 않으려고 공짜로 섬긴 게 큰 실수였을까? 알고 보니 다른 교회들이 내 여비를 대줘서 너희가 공짜로 혜택을 본 거야. 너희와 함께 살던 동안 단 한 번도 누구 하나 손가락 하나 까딱할 필요가 없었어. 내 필요는 항상 마케도니아의 믿는 사람들이 채워줬거든. 나는 너희에게 절대 부담 주지 않으려고 조심했고, 앞으로도 그럴 거야. 장담해. 그리스도를 증인으로 걸고 말하는데, 이건 내 자존심이 걸린 문제야. 이웃들이 뭐라고 할까 봐 조용히 넘어가지 않을 거야. 내가 너희를 사랑하지 않아서가 아냐. 하나님이 아셔, 사랑해. 나는 그냥 너희와 솔직하고 열린 관계를 유지하려는 거야.",
"\u00a7길고 외로운 많은 밤",
"그리고 이 입장은 바꾸지 않을 거야. 너희 돈을 받느니 죽겠어. 나를 그 돈 밝히는 '설교자'들, 자기를 대단한 것처럼 뽐내는 사람들과 같은 부류로 묶을 구실을 누구에게도 주지 않을 거야. 걔네는 한심한 무리야. 가짜 사도, 거짓말쟁이 설교자, 비뚤어진 일꾼. 그리스도의 대리인인 척하지만 속은 완전히 가짜지. 놀랄 것도 없어! 사탄은 항상 그래. 아름다운 빛의 천사로 변장하거든. 그러니 그 종들이 하나님의 종으로 변장한다고 놀라지 마. 하지만 걔네는 아무것도 빠져나가지 못해. 결국 대가를 치르게 될 거야.",
"처음으로 돌아가서 얘기할게. 계속 바보처럼 들려도 너무 뭐라 하지 마. 아니면 그냥 내가 바보라고 인정하고 잠깐 헛소리하게 내버려둬. 이런 말투는 그리스도에게서 배운 게 아냐. 요즘 인기 많은 서커스 설교자들에게서 배운 나쁜 버릇이야. 너희는 심판석에 앉아서 이 모든 소동을 지켜보니까, 가끔 지나가는 바보 하나쯤은 봐줄 여유가 있잖아. 너희는 사기꾼들에 대한 감탄할 만한 관용을 가졌어. 걔네는 너희 자유를 빼앗고, 돈을 뜯고, 홀랑 털어가고, 깔보고, 뺨까지 때리잖아! 인정하기 부끄럽지만, 우리 속은 그런 걸 견딜 만큼 강하지 않아.",
"너희가 강단의 자아도취자들을 그렇게 좋아하니까 (기억해, 이건 너희 옛 친구, 바보가 하는 말이야), 나도 한번 해볼게. 걔네가 히브리인, 이스라엘 사람, 아브라함의 순수 혈통이라고 자랑해? 나도 뒤지지 않아. 걔네가 그리스도의 종이야? 나는 한 수 위야. (이런 말을 하고 있다는 게 믿기지 않아. 이렇게 말하는 건 미친 짓이야! 하지만 시작했으니까 끝까지 가겠어.)",
"나는 훨씬 더 열심히 일했고, 더 자주 갇혔고, 셀 수 없이 많이 맞았고, 죽음의 문턱에 여러 번 섰어. 유대인의 서른아홉 대 매를 다섯 번 맞았고, 로마 몽둥이로 세 번 맞았고, 돌로 한 번 맞았어. 세 번 배가 난파됐고, 밤낮으로 탁 트인 바다에 잠겼었어. 해마다 이어진 험난한 여정에서 강을 건너야 했고, 강도를 막아야 했고, 친구와도 싸우고 적과도 싸웠어. 도시에서도 위험했고, 시골에서도 위험했고, 사막의 태양과 바다의 폭풍에 목숨을 걸었고, 형제라고 생각했던 사람들에게 배신당했어. 고된 노동과 힘든 일을 알았고, 잠 못 이룬 길고 외로운 밤도 많았고, 밥을 거른 적도 많았고, 추위에 얼었고, 비바람에 헐벗었어.",
"그리고 모든 교회에 대한 매일의 압박과 걱정을 더하면, 그건 절반도 안 돼. 누군가 벼랑 끝에 서면, 나는 뼛속까지 절박함을 느껴. 누군가 속아서 죄에 빠지면, 내 속에서 화난 불이 타올라.",
"나를 '자랑'해야 한다면, 나를 예수님처럼 만드는 굴욕을 자랑할게. 우리 주 예수의 영원하고 복되신 하나님 아버지가 내가 거짓말 안 한다는 걸 아셔. 다마스쿠스에 있던 때 기억해? 아레타 왕의 총독이 나를 잡으려고 성문에 경비병을 세웠잖아. 나는 성벽의 창문으로 기어 나가 바구니에 담겨 내려졌고, 목숨 걸고 도망쳐야 했어.",
],
"verseRanges": ["1-3","1-3","4-6","7-12","12-15","12-15","16-21","21-23","23-27","28-29","30-33"],
"msg_ranges": ["1-3","4-6","7-12","12-15","16-21","21-23","23-27","28-29","30-33"],
"merges": [],
"splits": [
{"msg_range": "12", "paras": [3,5], "note": "MSG 7-12와 12-15 사이 v12 겹침"},
{"msg_range": "21", "paras": [6,7], "note": "MSG 16-21과 21-23 사이 v21 겹침"},
{"msg_range": "23", "paras": [7,8], "note": "MSG 21-23과 23-27 사이 v23 겹침"},
],
"changes": [
"EN 구조 반영: MSG 헤더 2개(\u00a7가짜 하나님의 종들, \u00a7길고 외로운 많은 밤)",
"배지 수정: 30-33 (EN과 동일)",
"누락 복원: 1-3, 4-6, 7-12, 12-15, 21-23, 23-27 고난 목록, 28-29, 30-33 다마스쿠스 바구니 탈출",
],
"confirmations_needed": [],
}

# ---------------- KO CHAPTER 12 (full rewrite) ----------------
KO[12] = {
"chapter": 12, "title": "약함 속 하나님의 능력",
"paragraphs": [
"\u00a7약함에서 오는 강함",
"너희가 날 이렇게 말하게 만든 거야. 내 본심은 아니지만 말야. 어차피 이렇게 된 거, 하나님이 주신 환상과 계시에 대해 얘기할게. 예를 들어, 나는 한 사람을 알아. 14년 전에 그리스도에게 붙들려 황홀경 가운데 하늘 높은 곳으로 휩쓸려 올라간 사람이야. 그게 몸으로 일어난 건지 몸 밖에서 일어난 건지 정말 몰라. 하나님만 아셔. 또 알아, 그 사람이 낙원으로 끌려갔다는 걸. 다시 말하지만 몸 안이었는지 밖이었는지 몰라. 하나님만 아셔. 거기서 그는 말로 할 수 없는 말을 들었는데, 들은 걸 말하는 게 금지됐어. 내가 얘기하고 싶은 사람은 바로 이 사람이야. 하지만 나 자신에 대해서는 굴욕 말고는 한마디도 안 할 거야.",
"자랑하고 싶다면, 우스꽝스러워 보이지 않고도 할 수 있을 거야. 처음부터 끝까지 솔직한 진실만 말할 테니까. 하지만 너희를 봐줄게. 길에서 보거나 말하는 걸 들은 그 바보 말고 다른 사람으로 날 상상하길 원하지 않거든.",
"그 계시들이 너무 엄청나서 내가 교만해지지 않게 하려고, 내 한계를 계속 느끼게 하는 핸디캡이라는 선물을 받았어. 사탄의 천사가 나를 쓰러뜨리려고 최선을 다했는데, 실제로 한 건 나를 무릎 꿇게 한 거야. 그러니 잘난 척하고 다닐 위험은 없지! 처음에는 그걸 선물이라고 생각 안 하고, 없애달라고 하나님께 빌었어. 세 번이나 그랬어. 그러자 그분이 말씀하셨어. '내 은혜가 충분해. 그게 네가 필요한 전부야. 내 능력은 네 약함에서 온전히 드러나.' 그 말을 듣자 기꺼이 그렇게 되게 내버려뒀어. 핸디캡에 집중하기를 그만두고 선물을 감사하기 시작했지. 그리스도의 능력이 내 약함에 들어온 거야. 이제는 나를 작아지게 하는 이런 한계들을 웃으면서 받아들여. 학대, 사고, 반대, 불운 같은 것들 말야. 그냥 그리스도께 맡기는 거야! 그래서 내가 약해질수록 강해지는 거야.",
"자, 해버렸네! 이렇게 말하면서 완전히 바보가 됐어. 근데 전부 내 잘못은 아냐. 너희가 날 부추긴 거야. 너희가 나를 위해 이걸 해줬어야 했어. 내가 직접 하지 않게 나를 지켜주고 칭찬해줬어야지. 너희도 직접 경험해서 알잖아. 내가 별 볼 일 없는 아무것도 아닌 사람이라도, 너희가 좋아하는 그 잘난 척하는 사도들보다 뒤지지 않았다는 걸. 진짜 사도를 보여주는 모든 표적이 너희와 함께 있던 동안 좋은 때나 나쁜 때나 다 나타났어. 예언의 표적, 기적의 표적, 능력의 표적 말야. 너희가 다른 교회들보다 나나 하나님을 덜 받은 게 있어? 너희가 덜 받은 건 딱 하나, 나를 부양할 책임을 덜 진 거야. 자, 미안해. 너희를 박탈한 거 용서해줘.",
"이제 너희에게 세 번째 방문할 모든 준비가 됐어. 근데 걱정 마. 너희가 애쓸 필요 없어. 이번에도 지난 방문 때처럼 너희에게 폐 끼치지 않을 거야. 나는 너희가 가진 게 아니라 너희가 필요해. 아이들이 부모를 돌봐야 하는 게 아니라, 부모가 아이들을 돌봐야지. 나는 기꺼이 주머니를 비우고, 심지어 내 인생을 저당 잡혀서라도 너희에게 잘해주고 싶어. 그런데 어떻게 된 거야? 내가 너희를 더 사랑할수록 덜 사랑받는 게?",
"그리고 왜 자꾸 이런 뒷소문이 들리는 거야? 내가 자립하는 게 정교한 사기의 앞잡이였다는 소문 말야. 증거가 어디 있어? 내가 보낸 사람을 통해 너희를 속이거나 뜯어낸 적 있어? 나는 디도에게 방문을 부탁하고, 몇 형제를 함께 보냈어. 걔네가 너희에게서 뭘 뜯어냈어? 그리고 우리는 항상 똑같이 떳떳하고, 똑같이 정직하지 않았어?",
"우리가 처음부터 너희 앞에서, 배심원 앞에서 변명해왔다고 생각하진 않길 바라. 너희는 배심원이 아냐. 하나님이 배심원이셔. 그리스도 안에 계시된 하나님 말야. 우리는 그분 앞에서 우리 주장을 펼쳐. 그리고 너희가 자라는 데 방해가 되거나 길을 막지 않으려고, 스스로 자립하느라 온갖 수고를 다 한 거야.",
"인정할게. 내가 가면 너희가 나를 실망시키고 내가 너희를 실망시킬까 봐 두려워. 서로에게 좌절해서 모든 게 산산조각 나는 거야. 다툼, 질투, 불같은 성질, 편 가르기, 화난 말, 악의적인 소문, 부풀린 자존심, 완전 난장판. 너희 가운데서 하나님께 두 번째로 낮아지는 건 기대 안 해. 같은 옛 방식으로 계속 죄를 짓는 그 무리 때문에 뜨거운 눈물을 흘리는 것도 말야. 악의 돼지우리, 성적 문란, 음란함에서 벗어나길 거부하는 사람들이야.",
],
"verseRanges": ["1-5","1-5","6","7-10","11-13","14-15","16-18","19","20-21"],
"msg_ranges": ["1-5","6","7-10","11-13","14-15","16-18","19","20-21"],
"merges": [],
"splits": [],
"changes": [
"EN 구조 반영: \u00a7약함에서 오는 강함",
"배지 수정: 1-5, 11-13, 14-15, 16-18, 19, 20-21 (EN과 동일)",
"v5 복원: '말로 할 수 없는 말을 들었는데, 들은 걸 말하는 게 금지됐어'",
"v6 복원: '길에서 보거나 말하는 걸 들은 그 바보'",
"v19 복원: '너희는 배심원이 아냐. 하나님이 배심원이셔'",
"v20-21 복원: '악의 돼지우리, 성적 문란, 음란함'",
],
"confirmations_needed": [],
}

# ---------------- RUNNER ----------------
def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

for lang, table in (("en", EN), ("ko", KO)):
    path = f"/home/hatch/workspace/teenz-bible-review/fixes/{lang}_2Corinthians.json"
    data = load(path)
    for i, ch in enumerate(data["chapters"]):
        if ch["chapter"] in table:
            data["chapters"][i] = table[ch["chapter"]]
    # ch13: remove duplicated benediction from the 11-13 paragraph
    for ch in data["chapters"]:
        if ch["chapter"] == 13:
            if lang == "en":
                p = ch["paragraphs"][4]
                cut = p.find("All the believers here say hello.")
                assert cut > 0, "EN ch13 para4 marker missing"
                ch["paragraphs"][4] = p[:cut] + "All the brothers and sisters here say hello."
            else:
                p = ch["paragraphs"][4]
                cut = p.find("여기 있는 모든 성도가 안부를 전해.")
                assert cut > 0, "KO ch13 para4 marker missing"
                ch["paragraphs"][4] = p[:cut] + "여기 있는 모든 형제자매가 안부를 전해."
    save(data, path)
    print("saved", path)

print("done")
