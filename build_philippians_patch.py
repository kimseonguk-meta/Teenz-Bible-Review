#!/usr/bin/env python3
"""Build MSG-audited EN/KO patches for Philippians (4 chapters).

Reads chapter titles verbatim from allBibleData.json.
Writes fixes/en_Philippians.json and fixes/ko_Philippians.json.
"""
import json

SRC = "/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json"
src = json.load(open(SRC))
titles = {ch["num"]: ch["title"] for ch in src["Philippians"]}

# ---------------------------------------------------------------- EN chapters
en = {}

en[1] = {
    "paragraphs": [
        "What's up, Philippi crew! It's Paul and Tim \u2014 just a couple of guys serving Jesus, hitting you up. This is for everyone following Jesus in Philippi, pastors and ministers included. Grace and peace to you from God our Father and our Master, Jesus Christ.",
        "\u00a7A Love That Will Grow",
        "Every time I even *think* about you guys, I'm like, 'Thank you, God!' Seriously, every single time, it makes me want to pray for you, and I'm not even mad about it. I'm so stoked that you've been all-in with us, spreading the good news about Jesus since day one. I'm 100% sure that God, who started this awesome thing in you, is gonna see it through and give you a miraculous transformation on the day Jesus comes back.",
        "And for real, I'm not just gassing you up. You guys are my ride-or-dies. You stuck with me when I was in jail, when I was on trial, and when I got out. You've been there for the whole crazy ride, and God's been super generous to us through it all. He knows I miss you guys like crazy. Sometimes I feel like I'm on the same wavelength as Jesus about you.",
        "So, here's what I'm praying for you: that your love for each other just keeps leveling up. And not just that you love a lot, but that you love *smart*. You gotta use your brain and check your feelings so your love is the real deal, not just some mushy, fake stuff. Live like you're in love \u2014 careful and on-point, a life that makes Jesus proud. A life that's producing all kinds of good stuff, making Jesus look good to everyone and getting them all in on praising God.",
        "\u00a7They Can't Imprison the Message",
        "Hey, so I gotta tell you, being in jail has had the total opposite effect of what my haters wanted. Instead of shutting me down, the message about Jesus has blown up! All the guards here, and pretty much everyone else, found out I'm locked up because of Jesus. That made them curious, and now they're learning all about him. And get this: most of the other Jesus followers here are way more confident than ever, and they're not afraid to talk about God and Jesus.",
        "Now, it's true that some people are preaching about Jesus just because they see me out of the way and they want the spotlight. But the others are doing it with the best heart in the world. One group is all about love; they know I'm here defending the message and they want to help. The other group is just being greedy, trying to get something for themselves now that I'm not around. Their motives are wrong. They see me as competition, so they think the worse it is for me, the better it is for them.",
        "So what do I do? I've decided I don't really care what their motives are. Whether they're good, bad, or whatever, every time they open their mouths, they're talking about Jesus, so I'm just gonna cheer them on!",
        "And I'm gonna keep on cheering, because I know how this is all gonna end. With your prayers and the help of Jesus's Spirit, everything he wants to do in me and through me is gonna get done. I can't wait to see what's next. I'm not worried about being embarrassed at all. In fact, everything that's happening to me in here is just making Jesus more famous, whether I live or die. They didn't shut me up; they gave me a bigger stage! If I'm alive, I'm Jesus's messenger; if I'm dead, I'm his prize. It's a win-win. I can't lose.",
        "As long as I'm alive, I've got good work to do. If I had to choose right now, I don't know what I'd pick. It's a tough call! The thought of leaving this life and being with Jesus is awesome. Some days, that's all I want. But most days, because of what you guys are going through, I know it's better for me to stick around. So, I'm planning on being here for a while, to help you grow and be joyful in your faith. You can look forward to a big reunion when I come visit you again. We'll be praising Jesus and having a great time together.",
        "In the meantime, live in a way that makes the message of Jesus look good. Don't let your actions depend on whether I'm there or not. You've got to be the same whether I'm there to see it myself or I hear about it from far away. Stand together, have one goal, and fight for people to trust in the good news. Don't back down or get scared by the opposition. Your courage and unity will show them that they're going to lose and you're going to win\u2014and it's all because of God. There's more to this life than just trusting in Jesus. There's also suffering for him. And the suffering is just as much a gift as the trust. You're in the same fight you saw me go through, and you're getting an update on it in this letter.",
    ],
    "verseRanges": ["1-2", "3-6", "3-6", "7-8", "9-11", "12-14", "12-14", "15-17", "18", "19-21", "22-26", "27-30"],
    "splits": [{"msg_range": "18-21", "paras": [9, 10],
                "note": "MSG \ub2e8\uc77c \ubb38\ub2e8(18-21)\uc744 EN \uac00\ub3c5\uc131\uc744 \uc704\ud574 2\uac1c \ubb38\ub2e8\uc73c\ub85c \ubd84\ub9ac"}],
    "changes": [
        "1\uc7a5: MSG \ubb38\ub2e8 \uad6c\uc870 \uae30\uc900\uc73c\ub85c \ubc30\uc9c0 \uc7ac\uad6c\uc131 \ubc0f \u00a7 \ud5e4\ub354\ub97c MSG \uc139\uc158 \uc81c\ubaa9\uc73c\ub85c \uad50\uccb4 ('A Love That Will Grow', 'They Can\\'t Imprison the Message') \u2014 \uae30\uc874 \ucc3d\uc791 \ud5e4\ub354 '\u00a7Joy in Chains' \uc0ad\uc81c",
        "\uae30\uc874 \ubc30\uc9c0 '3-5'\u2192'3-6' (6\uc808 \ub0b4\uc6a9 \ud3ec\ud568), '6-8'\u2192'7-8', '22-25'\u2192'22-26', '26-30'\u2192'27-30' (MSG \ubb38\ub2e8 \uad6c\ubd84\uc5d0 \ub9de\ucda4)",
        "\uae30\uc874 \ubc30\uc9c0 '17' \ubb38\ub2e8 \u2192 '18'\uc73c\ub85c \uc218\uc815 (17\uc808 \ub0b4\uc6a9\uc740 \uc55e \ubb38\ub2e8\uc5d0 \uc788\uc74c). '18'/'19-21' \ub450 \ubb38\ub2e8\uc740 MSG 18-21 \ub2e8\uc77c \ubb38\ub2e8\uc758 \uac00\ub3c5\uc131 \ubd84\ud560 \u2192 splits \uc120\uc5b8",
        "9-11\uc808 \ubb38\ub2e8: MSG 'circumspect and exemplary' \ubcf5\uc6d0 ('careful and on-point')",
        "1-2\uc808 \ubb38\ub2e8: MSG 'grace and peace', 'pastors and ministers' \ud45c\ud604 \uc815\ub9ac",
    ],
}

en[2] = {
    "paragraphs": [
        "\u00a7He Took on the Status of a Slave",
        "So, if you've gotten anything good out of following Jesus, if His love has actually changed you, if being part of this Spirit-filled community means anything to you, and if you guys have any heart at all \u2014 do me a solid. Get on the same page, love each other, and be true ride-or-die friends. Don't be that person who's always trying to be the main character. Don't try to sweet-talk your way to the top. Instead, be humble and hype up your friends. Don't just look out for number one. Forget about yourself for a minute and help someone else out.",
        "Think of yourselves the way Jesus thought of Himself. He was literally on the same level as God, but He didn't think so much of Himself that He had to cling to His top-tier status no matter what. Not at all. When the time was right, He gave up all His perks and took on the status of a servant \u2014 He became human! And He stayed human, which was a total glow-down for Him. He didn't claim special treatment. He just lived a selfless, obedient life and then died a selfless, obedient death \u2014 the worst kind of death, too: crucifixion.",
        "Because He was so obedient, God lifted Him high and honored Him more than anyone or anything, ever. So now, everyone in heaven, on earth, and even the ghosts of people long gone, will bow down and worship Jesus. They'll all shout out that He's the boss, bringing major props to God the Father.",
        "\u00a7Rejoicing Together",
        "So, my friends, here's the deal. Just keep doing what you've been doing. When I was with you, you were all about listening and obeying. Now that I'm gone, you gotta step it up even more. Go hard in your faith, and be respectful and aware of God. That power you feel? That's God's own energy deep inside you \u2014 God Himself willing it and working it, going after what makes Him happiest.",
        "Do everything gladly and willingly \u2014 no bickering, no second-guessing allowed! Go out into the world and stay clean, a breath of fresh air in this messed-up, polluted society. Show people what good living looks like and who the living God is. Carry the light-giving Message into the night, so when Jesus comes back, I'll have good reason to be proud of you. You'll be living proof that all my hard work wasn't for nothing.",
        "Even if I get executed here and now, I'll rejoice to be part of the offering of your faith that you lay on Christ's altar \u2014 a part of your celebration too. But turnabout's fair play: you've got to join me in my rejoicing. Whatever you do, don't feel sorry for me.",
        "I'm planning \u2014 according to Jesus' plan \u2014 to send Timothy to you guys really soon, so he can bring back all the news about you he can gather. Oh, that would do my heart so much good! There's no one else like Timothy. He's loyal and genuinely cares about you. Most people around here are just looking out for themselves, with barely any concern for what Jesus cares about. But you know yourselves that Timothy's the real thing. He's been like a devoted son to me as we've delivered the Message together. As soon as I see how things are going to turn out for me here, I'll send him your way. And I'm hoping and praying I'll be right on his heels.",
        "But for right now, I'm dispatching Epaphroditus, my good friend and companion in the work. You sent him to help me out; now I'm sending him to help you out. He's been wanting in the worst way to get back with you \u2014 especially since he recovered from that illness you heard about, he's been wanting to get back and reassure you that he's just fine. He nearly died, as you know, but God had mercy on him. And not only on him \u2014 He had mercy on me too. His death would have been one huge grief piled on top of all the others.",
        "So you can see why I'm so delighted to send him on to you. When you see him again, strong and strapping, how you'll rejoice \u2014 and how relieved I'll be. Give him a grand welcome, a joyful embrace! People like him deserve the best you can give. Remember the ministry to me that you started but weren't able to finish? Well, in the process of finishing up that work, he put his life on the line and nearly died doing it.",
    ],
    "verseRanges": ["1-4", "1-4", "5-8", "9-11", "12-13", "12-13", "14-16", "17-18", "19-24", "25-27", "28-30"],
    "splits": [],
    "changes": [
        "2\uc7a5: \u00a7 \ud5e4\ub354\ub97c MSG \uc139\uc158 \uc81c\ubaa9\uc73c\ub85c \uad50\uccb4 ('He Took on the Status of a Slave', 'Rejoicing Together') \u2014 \uae30\uc874 \ucc3d\uc791 \ud5e4\ub354 '\u00a7Think Like Jesus', '\u00a7God Lifted Him Up' \uc0ad\uc81c",
        "\uae30\uc874 \ubc30\uc9c0 '25-28'\u2192'25-27' (28-30\uc808\uc740 \ub2e4\uc74c \ubb38\ub2e8; MSG \ubb38\ub2e8 \uad6c\ubd84 25-27/28-30\uc5d0 \ub9de\ucda4)",
        "1-4\uc808: MSG 'community of the Spirit' \ubcf5\uc6d0",
        "5-8\uc808: MSG 'Think of yourselves the way Christ Jesus thought of himself', 'selfless' \ubcf5\uc6d0",
        "9-11\uc808: MSG 'God lifted him high' \ubcf5\uc6d0",
        "12-13\uc808: MSG 'God himself willing and working' \ubcf5\uc6d0",
        "14-16\uc808: MSG 'readily and cheerfully', 'uncorrupted' \ubcf5\uc6d0",
        "17-18\uc808: MSG 'on Christ\\'s altar', 'a part of your rejoicing' \ubcf5\uc6d0",
        "19-24\uc808: MSG 'according to Jesus\\' plan', 'you know yourselves', 'hoping and praying' \ubcf5\uc6d0",
        "25-27\uc808: MSG 'wanting in the worst way', 'one huge grief piled on top of all the others' \ubcf5\uc6d0",
        "28-30\uc808: MSG 'strong and strapping', 'a grand welcome, a joyful embrace', 'put his life on the line' \ubcf5\uc6d0",
    ],
}

en[3] = {
    "paragraphs": [
        "\u00a7To Know Him Personally",
        "And that's about it, friends \u2014 be glad in God! I don't mind repeating what I already wrote in earlier letters, and I hope you don't mind hearing it again. Better safe than sorry, so here goes.",
        "Steer clear of the barking dogs \u2014 those religious busybodies who are all bark and no bite. They're obsessed with appearances \u2014 knife-happy circumcisers, I call them. The real believers are the ones led by God's Spirit, working hard at this ministry and filling the air with Christ's praise. We know we could never pull this off on our own \u2014 even though some people flash what look like impressive credentials. You know my pedigree: born legit, circumcised on the eighth day, an Israelite from the elite tribe of Benjamin, a strict and hardcore follower of God's law, so fired up about keeping my religion pure that I even went after the church, and a meticulous keeper of everything written in God's law book.",
        "All the credentials these people keep waving around like they're something special? I'm ripping them up and tossing them in the trash \u2014 right along with everything else I used to take credit for. And why? Because of Christ. Yes, everything I once thought was so important is gone from my life. Compared to the epic privilege of knowing Christ Jesus as my Master, firsthand, everything I once had going for me is insignificant \u2014 total trash. I've dumped it all so I could grab onto Christ and be grabbed by Him. I don't want some weak, rule-based 'goodness.' I want the real, powerful kind that comes from trusting Christ \u2014 God's righteousness.",
        "I ditched all that lame stuff so I could really know Christ, feel His resurrection power, be a partner in His suffering, and go all the way with Him \u2014 even to death itself. If there's any way to get in on the ultimate comeback \u2014 the resurrection from the dead \u2014 I'm all in.",
        "\u00a7Focused on the Goal",
        "Look, I'm not saying I've got this all together or that I've made it. But I'm well on my way, reaching out for Christ, who so amazingly reached out for me first. Friends, don't get me wrong: I'm no expert in any of this. But I've got my eye on the goal, where God is calling us onward \u2014 to Jesus. I'm off and running, and I'm not turning back.",
        "So let's keep focused on that goal \u2014 those of us who want everything God has for us. If any of you have something else in mind, something less than total commitment, God will clear your blurred vision \u2014 you'll see it yet! Now that we're on the right track, let's stay on it.",
        "Stick with me, friends. Keep track of the people you see running this same course, headed for this same goal. There are plenty of people out there on different paths, chasing different goals, trying to pull you along with them. I've warned you about them plenty of times, and sadly I've got to do it again. All they want is easy street. They hate Christ's cross. But easy street is a dead-end street. The people who live there worship their own bellies \u2014 burps are their praise songs \u2014 and all they can think about is their appetites.",
        "But there's way more to life for us. We're citizens of high heaven! We're waiting for the arrival of the Savior, the Master, Jesus Christ, who will transform our earthy bodies into glorious bodies like His own. He'll make us beautiful and whole with the same powerful skill He uses to put everything as it should be, under and around Him.",
    ],
    "verseRanges": ["1", "1", "2-6", "7-9", "10-11", "12-14", "12-14", "15-16", "17-19", "20-21"],
    "splits": [],
    "changes": [
        "3\uc7a5: \u00a7 \ud5e4\ub354\ub97c MSG \uc139\uc158 \uc81c\ubaa9\uc73c\ub85c \uad50\uccb4 ('To Know Him Personally', 'Focused on the Goal') \u2014 \uae30\uc874 \ucc3d\uc791 \ud5e4\ub354 '\u00a7Knowing Christ Is Everything' \uc0ad\uc81c",
        "\uae30\uc874 1\ubc88 \ubb38\ub2e8(\ubc30\uc9c0 '1-4')\uc744 MSG \ubb38\ub2e8 \uad6c\ubd84\uc5d0 \ub530\ub77c \ubd84\ub9ac: 1\uc808 \ubb38\ub2e8 + 2-6\uc808 \ubb38\ub2e8 \uc2e0\uc124 (\uae30\uc874 \ubc30\uc9c0\ub294 MSG 1/2-6 \uacbd\uacc4 \ubb34\uc2dc)",
        "\uae30\uc874 \ubc30\uc9c0 '13-14'\u2192'12-14' (MSG \ubb38\ub2e8 \uad6c\ubd84\uc5d0 \ub9de\ucda4)",
        "2-6\uc808: MSG \ubb38\ub2e8 \uc804\uccb4 \ubcf5\uc6d0 (\uac1c \uacbd\uace0\u00b7'knife-happy circumcisers'\u00b7\uc2e4\uc81c \ubbff\ub294 \uc790\u00b7\uc871\ubcf4 \uc804\uccb4 \u2014 \uae30\uc874 EN\uc740 1\uc808 \ubb38\ub2e8\uc5d0 \uc77c\ubd80\ub9cc \uc555\ucd95 \ud3ec\ud568)",
        "10-11\uc808: MSG 'even to death itself' \ubcf5\uc6d0",
        "17-19\uc808: MSG 'belches are their praise' \ubcf5\uc6d0 ('burps are their praise songs')",
        "20-21\uc808: MSG 'beautiful and whole' \ubcf5\uc6d0",
    ],
}

en[4] = {
    "paragraphs": [
        "My dear, dear friends! I love you guys so much, and I want the absolute best for you. You fill me with joy and make me so proud. Don't waver. Stay on track, steady in God.",
        "\u00a7Pray About Everything",
        "I urge Euodia and Syntyche to iron out their differences and make up. God doesn't want His kids holding grudges.",
        "And, oh yes \u2014 Syzygus, since you're right there with them, do your best to help them work things out. These women worked for the Message hand in hand with me and Clement and the other veterans \u2014 they worked just as hard as any of us. Remember, their names are in the Book of Life too.",
        "Celebrate God all day, every day \u2014 I mean, really revel in Him! Make it crystal clear to everyone you meet that you're on their side, working with them and not against them. Help them see that the Master is about to arrive \u2014 He could show up any minute!",
        "Don't fret or worry. Instead of worrying, pray. Let petitions and praises shape your worries into prayers, letting God know your concerns. Before you know it, a sense of God's wholeness \u2014 everything coming together for good \u2014 will come and settle you down. It's amazing what happens when Christ pushes worry out of the center of your life.",
        "Summing it all up, friends \u2014 fill your minds and meditate on things that are true, noble, reputable, authentic, compelling, gracious. Think the best, not the worst; the beautiful, not the ugly; things to praise, not things to curse. Put into practice what you learned from me \u2014 what you heard and saw and figured out. Do that, and God, who makes everything work together, will work you into His most excellent harmonies.",
        "\u00a7Content Whatever the Circumstances",
        "I'm glad in God \u2014 way happier than you'd ever guess \u2014 happy that you're showing such strong concern for me again. Not that you ever quit praying and thinking about me. You just had no chance to show it. Actually, I don't need anything personally. I've learned by now to be totally content whatever my circumstances. I'm just as happy with little as with much, with much as with little. I've found the recipe for being happy whether full or hungry, hands full or hands empty. Whatever I have, wherever I am, I can make it through anything in the One who makes me who I am. Don't get me wrong \u2014 your help meant a lot to me. It did. It was a beautiful thing that you came alongside me in my troubles.",
        "You Philippians know the deal \u2014 and I'll never forget it: when I first left Macedonia, heading out with the Message, not one church joined in the give-and-take of this work except you. You were the only ones. Even while I was in Thessalonica, you helped out \u2014 not just once, but twice. Not that I'm looking for handouts. I just want you to experience the blessing that comes from generosity.",
        "And now I've got it all \u2014 and more keeps coming! The gifts you sent with Epaphroditus were more than enough \u2014 like a sweet-smelling sacrifice roasting on the altar, filling the air with fragrance, pleasing God to no end. You can be sure that God will take care of everything you need, His generosity going way beyond yours in the glory that pours from Jesus. Our God and Father overflows with glory that just pours out into eternity. Yes!",
        "Give my regards to every follower of Jesus you meet. Our friends here say hello. All the Christians here \u2014 especially the believers who work in Caesar's palace \u2014 want to be remembered to you.",
        "Receive and experience the amazing grace of the Master, Jesus Christ, deep, deep inside you.",
    ],
    "verseRanges": ["1", "2", "2", "3", "4-5", "6-7", "8-9", "10-14", "10-14", "15-17", "18-20", "21-22", "23"],
    "splits": [],
    "changes": [
        "4\uc7a5: \u00a7 \ud5e4\ub354\ub97c MSG \uc139\uc158 \uc81c\ubaa9\uc73c\ub85c \uad50\uccb4 ('Pray About Everything', 'Content Whatever the Circumstances') \u2014 \uae30\uc874 \ucc3d\uc791 \ud5e4\ub354 '\u00a7Rejoice Always', '\u00a7Think About These Things' \uc0ad\uc81c",
        "\uae30\uc874 1\ubc88 \ubb38\ub2e8(\ubc30\uc9c0 '1-3')\uc744 MSG \ubb38\ub2e8 \uad6c\ubd84\uc5d0 \ub530\ub77c 3\uac1c\ub85c \ubd84\ub9ac: 1\uc808 / 2\uc808 / 3\uc808",
        "\uae30\uc874 2\ubc88 \ubb38\ub2e8(\ubc30\uc9c0 '4-7')\uc744 MSG \ubb38\ub2e8 \uad6c\ubd84\uc5d0 \ub530\ub77c \ubd84\ub9ac: 4-5\uc808 / 6-7\uc808 (merge \uc544\ub2d8 \u2014 MSG \uad6c\uc870 \ubcf5\uc6d0)",
        "1\uc808: MSG 'I love you so much. I do want the very best for you' \ubcf5\uc6d0",
        "2\uc808: MSG 'God doesn\\'t want his children holding grudges' \ubcf5\uc6d0 (\uae30\uc874 EN \ub204\ub77d)",
        "3\uc808: MSG \uc778\uba85 'Syzygus'\u00b7'Clement', '\u2018worked as hard as any of us\\'' \ubcf5\uc6d0",
        "8-9\uc808: MSG \ubbf8\ub355 \ubaa9\ub85d \uc804\uccb4 \ubcf5\uc6d0 (true, noble, reputable, authentic, compelling, gracious / things to curse / and realized)",
        "10-14\uc808: MSG 'far happier than you would ever guess', 'praying and thinking about me', 'the One who makes me who I am' \ubcf5\uc6d0",
        "\uae30\uc874 \ubc30\uc9c0 '15-16'\u2192'15-17', MSG 'Macedonia', 'I\\'ll never forget it', 'not just once, but twice', 'in the give-and-take of this work' \ubcf5\uc6d0",
        "\uae30\uc874 \ubc30\uc9c0 '17-20'\u2192'18-20', MSG 'and keep getting more!' \ubcf5\uc6d0",
        "21-22\uc808: MSG\uc5d0 \uc5c6\ub294 \ud574\uc11d \ucca8\uac00('the government headquarters') \uc0ad\uc81c",
        "23\uc808: MSG \uba85\ub839\ud615 'Receive and experience' \ubcf5\uc6d0",
    ],
}

# ---------------------------------------------------------------- KO chapters
ko = {}
ko_titles = {1: "\uac10\uc625\uc5d0\uc11c \ubcf4\ub0b4\ub294 \ubc14\uc6b8\uc758 \ud3b8\uc9c0",
             2: "\uc9c4\uc9dc MVP \ub418\ub294 \ubc95",
             3: "\uc2b9\ub9ac\ub97c \ud5a5\ud55c \uc62c\uc778",
             4: "\uc2a4\ud2b8\ub808\uc2a4 \uc81c\ub85c \uc778\uc0dd \uac00\uc774\ub4dc"}

ko[1] = {
    "paragraphs": [
        "\ube4c\ub9bd\ubcf4 \uce5c\uad6c\ub4e4, \uc798 \uc9c0\ub0b4? \ubc14\uc6b8\uc774\ub791 \ub514\ubaa8\ub370\uc57c. \uc608\uc218\ub2d8 \ud300\uc5d0\uc11c \ub6f0\ub294 \ud3c9\ubc94\ud55c \ub450 \uc0ac\ub78c\uc774 \ud3b8\uc9c0 \ubcf4\ub0b8\ub2e4. \ube4c\ub9bd\ubcf4\uc5d0 \uc788\ub294 \uc608\uc218\ub2d8 \ub530\ub974\ub294 \ubaa8\ub4e0 \uc0ac\ub78c\ub4e4, \ubaa9\uc0ac\ub2d8\ub4e4\uc774\ub791 \uc0ac\uc5ed\uc790\ub4e4\uae4c\uc9c0 \ub2e4 \ud3ec\ud568\ud574\uc11c. \ud558\ub098\ub2d8 \uc544\ubc84\uc9c0\uc640 \uc6b0\ub9ac \uc8fc\uc778\uc774\uc2e0 \uc608\uc218 \uadf8\ub9ac\uc2a4\ub3c4\uac00 \uc8fc\uc2dc\ub294 \uc740\ud61c\uc640 \ud3c9\ud654\uac00 \ub108\ud76c\uc5d0\uac8c \uc788\uae30\ub97c!",
        "\u00a7\uc790\ub77c\ub098\ub294 \uc0ac\ub791",
        "\ub108\ud76c \uc0dd\uac01\ub9cc \ud558\uba74 \ub098\ub3c4 \ubaa8\ub974\uac8c '\ud558\ub098\ub2d8, \uac10\uc0ac\ud569\ub2c8\ub2e4!' \uc18c\ub9ac\uac00 \ub098\uc640. \uc9c4\uc9dc \ub9e4\ubc88 \uadf8\ub798. \uadf8\ub7ec\ub2e4 \ubcf4\uba74 \uae30\uc05c \ub9c8\uc74c\uc73c\ub85c \ub108\ud76c\ub97c \uc704\ud574 \uae30\ub3c4\ud558\uac8c \ub3fc. \ub108\ud76c\uac00 \ucc98\uc74c \ubcf5\uc74c\uc744 \ub4e4\uc740 \uadf8\ub0a0\ubd80\ud130 \uc9c0\uae08\uae4c\uc9c0, \ud558\ub098\ub2d8\uc758 \uba54\uc2dc\uc9c0\ub97c \ubbff\uace0 \uc804\ud558\ub294 \uc77c\uc5d0 \uc6b0\ub9ac\ub791 \ud568\uaed8\ud574 \uc918\uc11c \uc5bc\ub9c8\ub098 \uae30\uc05c\uc9c0 \ubab0\ub77c. \ub108\ud76c \uc548\uc5d0\uc11c \uc774 \uba4b\uc9c4 \uc77c\uc744 \uc2dc\uc791\ud558\uc2e0 \ud558\ub098\ub2d8\uc774, \uc608\uc218 \uadf8\ub9ac\uc2a4\ub3c4\uaed8\uc11c \ub098\ud0c0\ub098\uc2dc\ub294 \uadf8\ub0a0\uae4c\uc9c0 \uacc4\uc18d \ubd99\ub4e4\uace0 \uacc4\uc154\uc11c \uc644\uc804 \uba4b\uc9c0\uac8c \ub9c8\ubb34\ub9ac\ud574\uc8fc\uc2e4 \uac70\ub77c\uace0 1\ub3c4 \uc758\uc2ec \uc548 \ud574.",
        "\ub0b4\uac00 \ub108\ud76c\ub97c \uc774\ub807\uac8c \uc0dd\uac01\ud558\ub294 \uac70, \uadf8\ub0e5 \ud558\ub294 \ube48\ub9d0 \uc544\ub2c8\uc57c. \ub0b4 \uae30\ub3c4\ub791 \ubc14\ub78c\uc740 \ub2e4 \ud604\uc2e4\uc5d0 \ub2e8\ub2e8\ud788 \ubfcc\ub9ac\ubc15\uace0 \uc788\uac70\ub4e0. \ub0b4\uac00 \uac10\uc625\uc5d0 \uac07\ud614\uc744 \ub54c, \uc7ac\ud310\ubc1b\uc744 \ub54c, \uadf8\ub9ac\uace0 \ubb34\uc0ac\ud788 \ud480\ub824\ub0ac\uc744 \ub54c\uae4c\uc9c0 \ub108\ud76c\ub294 \ucc98\uc74c\ubd80\ud130 \ub05d\uae4c\uc9c0 \ub0b4 \uacc1\uc744 \uc9c0\ucf30\uc796\uc544. \uadf8 \ubaa8\ub4e0 \uacfc\uc815\uc5d0\uc11c \ud558\ub098\ub2d8\uc758 \ub118\uce58\ub294 \ub3c4\uc6b0\uc2ec\uc744 \uc6b0\ub9ac \ud568\uaed8 \uacbd\ud5d8\ud588\uc9c0. \uc9c0\uae08 \ub0b4\uac00 \ub108\ud76c\ub97c \uc5bc\ub9c8\ub098 \uc0ac\ub791\ud558\uace0 \uadf8\ub9ac\uc6cc\ud558\ub294\uc9c0 \ud558\ub098\ub2d8\uc740 \ub2e4 \uc544\uc154. \uac00\ub054\uc740 \uc608\uc218\ub2d8\uc774 \ub108\ud76c\ub97c \uc0dd\uac01\ud558\ub294 \uac83\ub9cc\ud07c\uc774\ub098 \ub098\ub3c4 \ub108\ud76c\uac00 \uac04\uc808\ud558\uac8c \uc0dd\uac01\ub098.",
        "\uadf8\ub798\uc11c \ub0b4\uac00 \ub108\ud76c\ub97c \uc704\ud574 \uae30\ub3c4\ud558\ub294 \uac74 \uc774\uac70\uc57c. \ub108\ud76c\uc758 \uc0ac\ub791\uc774 \uc4f1\uc4f1 \uc790\ub77c\ub098\uae30\ub97c. \uadf8\uac83\ub3c4 \uadf8\ub0e5 \ub9ce\uc774 \uc0ac\ub791\ud558\ub294 \uac8c \uc544\ub2c8\ub77c, \uc81c\ub300\ub85c \uc0ac\ub791\ud558\uae30\ub97c. \uc0ac\ub791\ub3c4 \ub611\ub611\ud558\uac8c \ud558\ub294 \ubc95\uc744 \ubc30\uc6cc\uc57c \ud574. \uba38\ub9ac\ub97c \uc4f0\uace0 \uac10\uc815\ub3c4 \uc810\uac80\ud574\uc11c, \ub108\ud76c \uc0ac\ub791\uc774 \ub290\ub07c\ud55c \uac10\uc131\ud314\uc774\uac00 \uc544\ub2c8\ub77c \uc9c4\uc9dc\ubc30\uae30 \uc9c0\uc801\uc778 \uc0ac\ub791\uc774 \ub418\uac8c. \uc0ac\ub791\ud558\ub294 \uc0ac\ub78c\ub2f5\uac8c, \uc2e0\uc911\ud558\uace0 \ubaa8\ubc94\uc801\uc73c\ub85c \uc0b4\uc544. \uc608\uc218\ub2d8\uc774 \uc790\ub791\uc2a4\ub7ec\uc6cc\ud558\uc2e4 \ub9cc\ud55c \uc0b6\uc73c\ub85c. \uc601\ud63c\uc758 \uc5f4\ub9e4\ub97c \ud48d\uc131\ud558\uac8c \ub9fa\uace0, \uc608\uc218 \uadf8\ub9ac\uc2a4\ub3c4\ub97c \ubaa8\ub4e0\uc774\uc5d0\uac8c \ub9e4\ub825\uc801\uc73c\ub85c \ub9cc\ub4e4\uace0, \ubaa8\ub4e0 \uc0ac\ub78c\uc774 \ud558\ub098\ub2d8\uc758 \uc601\uad11\uacfc \ucc2c\uc1a1\uc5d0 \ub3d9\ucc38\ud558\uac8c \ud558\ub294 \uadf8\ub7f0 \uc0b6 \ub9d0\uc774\uc57c.",
        "\u00a7\uac00\ub458 \uc218 \uc5c6\ub294 \uba54\uc2dc\uc9c0",
        "\uce5c\uad6c\ub4e4\uc544, \uaf2d \uc54c\ub824\uc8fc\uace0 \uc2f6\uc740 \uac8c \uc788\uc5b4. \ub0b4\uac00 \uc5ec\uae30 \uac07\ud78c \uac8c \uc624\ud788\ub824 \ubc18\ub300 \uacb0\uacfc\ub97c \ub0b3\uc558\uc5b4. \uba54\uc2dc\uc9c0\uac00 \ub20c\ub9ac\uae30\ub294\ucee8\ub155 \uc624\ud788\ub824 \ub354 \ud765\ud588\uac70\ub4e0. \uc5ec\uae30 \ubaa8\ub4e0 \uad70\uc778\ub4e4\uc774\ub791 \ub2e4\ub978 \uc0ac\ub78c\ub4e4\uae4c\uc9c0, \ub0b4\uac00 \uba54\uc2dc\uc544 \ub54c\ubb38\uc5d0 \uac10\uc625\uc5d0 \uc788\ub2e4\ub294 \uac78 \ub2e4 \uc54c\uac8c \ub410\uc5b4. \uadf8\uac8c \uc0ac\ub78c\ub4e4 \ud638\uae30\uc2ec\uc744 \uc790\uadf9\ud574\uc11c \uc774\uc81c\ub294 \uc608\uc218\ub2d8\uc5d0 \ub300\ud574 \ub2e4 \uc54c\uac8c \ub410\uc9c0. \uac8c\ub2e4\uac00 \uc5ec\uae30 \uc788\ub294 \uc608\uc218\ub2d8 \ub530\ub974\ub294 \uc0ac\ub78c\ub4e4 \ub300\ubd80\ubd84\uc774 \uc804\ubcf4\ub2e4 \ud6e8\uc52c \ubbff\uc74c\uc5d0 \ud655\uc2e0\uc774 \uc0dd\uaca8\uc11c, \ud558\ub098\ub2d8\uacfc \uba54\uc2dc\uc544\uc5d0 \ub300\ud574 \ucac4\uc9c0 \uc54a\uace0 \ub2f9\ub2f9\ud558\uac8c \ub9d0\ud558\uace0 \uc788\uc5b4.",
        "\ubb3c\ub860 \uc5b4\ub5a4 \uc0ac\ub78c\ub4e4\uc740 \ub0b4\uac00 \ube60\uc9c4 \ud2c8\uc744 \ud0c0\uc11c \uc2a4\ud3ec\ud2b8\ub77c\uc774\ud2b8 \uc880 \ubc1b\uc544\ubcf4\ub824\uace0 \uadf8\ub9ac\uc2a4\ub3c4\ub97c \uc804\ud558\uae30\ub3c4 \ud574. \uadfc\ub370 \ub2e4\ub978 \uc0ac\ub78c\ub4e4\uc740 \uc138\uc0c1\uc5d0\uc11c \uac00\uc7a5 \uc88b\uc740 \ub9c8\uc74c\uc73c\ub85c \uc804\ud558\uace0 \uc788\uc5b4. \ud55c \uadf8\ub8f9\uc740 \uc21c\uc218\ud55c \uc0ac\ub791\uc73c\ub85c \uc6c0\uc9c1\uc5ec. \ub0b4\uac00 \uc5ec\uae30\uc11c \uba54\uc2dc\uc9c0\ub97c \uc9c0\ud0a4\uace0 \uc788\ub2e4\ub294 \uac78 \uc54c\uace0 \ub3d5\uc544\uc8fc\uace0 \uc2f6\uc5b4 \ud558\uc9c0. \ub2e4\ub978 \uadf8\ub8f9\uc740 \ub0b4\uac00 \uc0ac\ub77c\uc9c4 \uae40\uc5d0 \ubb54\uac00 \ucc59\uaca8\ubcf4\ub824\ub294 \uc695\uc2ec\uc73c\ub85c \ud574. \ub3d9\uae30\uac00 \ub098\ube60. \ub098\ub97c \uacbd\uc7c1\uc790\ub85c \ubcf4\uace0, \ub098\ud55c\ud14c \uc548 \uc88b\uc744\uc218\ub85d \uc790\uae30\ub4e4\ud55c\ud14c\ub294 \uc88b\ub2e4\uace0 \uc0dd\uac01\ud558\ub294 \uac70\uc57c.",
        "\uadf8\ub7fc \ub098\ub294 \uc5b4\ub5bb\uac8c \ubc18\uc751\ud574\uc57c \ud560\uae4c? \uac40\ub4e4 \ub3d9\uae30\uac00 \uc11e\uc600\ub4e0, \ub098\uc058\ub4e0, \uc560\ub9e4\ud558\ub4e0 \uc2e0\uacbd \uc548 \uc4f0\uae30\ub85c \ud588\uc5b4. \uac40\ub4e4 \uc911 \ub204\uad6c\ub77c\ub3c4 \uc785\ub9cc \uc5f4\uba74 \uadf8\ub9ac\uc2a4\ub3c4\uac00 \uc804\ud30c\ub418\ub2c8\uae4c, \uadf8\ub0e5 \uc751\uc6d0\ud560 \ubfd0\uc774\uc57c!",
        "\uadf8\ub9ac\uace0 \uc774 \uc751\uc6d0\uc740 \uacc4\uc18d\ub420 \uac70\uc57c. \uc77c\uc774 \uc5b4\ub5bb\uac8c \ub420\uc9c0 \uc544\ub2c8\uae4c. \ub108\ud76c\uc758 \uc2e0\uc2e4\ud55c \uae30\ub3c4\uc640 \uc608\uc218 \uadf8\ub9ac\uc2a4\ub3c4\uc758 \uc601\uc774 \uc544\ub08c\uc5c6\uc774 \ub3c4\uc6b0\uc2dc\ub294 \ub355\ubd84\uc5d0, \uadf8\ubd84\uc774 \ub0b4 \uc548\uc5d0\uc11c, \ub098\ub97c \ud1b5\ud574 \ud558\uc2dc\ub824\ub294 \ubaa8\ub4e0 \uc77c\uc774 \uc774\ub8e8\uc5b4\uc9c8 \uac70\ub4e0. \uacc4\uc18d \ub0b4 \uae38\uc744 \uac00\ub294 \uac8c \ub108\ubb34 \uae30\ub300\ub3fc. \ubd80\ub044\ub7ec\uc6b8 \uac83 \ud558\ub098\ub3c4 \uc5c6\uc5b4. \uc624\ud788\ub824 \uac10\uc625\uc5d0 \uc788\ub294 \ub098\ud55c\ud14c \uc77c\uc5b4\ub098\ub294 \ubaa8\ub4e0 \uc77c\uc774, \uc0b4\ub4e0\uc9c0 \uc8fd\ub4e0\uc9c0, \uadf8\ub9ac\uc2a4\ub3c4\ub97c \ub354 \uc815\ud655\ud558\uac8c \uc54c\ub9ac\ub294 \ub370 \uc4f0\uc774\uace0 \uc788\uc73c\ub2c8\uae4c. \uac40\ub4e4\uc740 \ub0b4 \uc785\uc744 \ub9c9\uae30\ub294\ucee8\ub155 \uc624\ud788\ub824 \ub098\ud55c\ud14c \ubb34\ub300\ub97c \ub9cc\ub4e4\uc5b4\uc900 \uc148\uc774\uc9c0! \uc0b4\uc544 \uc788\uc73c\uba74 \ub098\ub294 \uadf8\ub9ac\uc2a4\ub3c4\uc758 \uba54\uc2e0\uc800, \uc8fd\uc73c\uba74 \uadf8\ubd84\uc758 \ud2b8\ub85c\ud53c. \uc9c0\uae08 \uc0b6\ub3c4, \ud6e8\uc52c \ub354 \uc88b\uc740 \ub2e4\uc74c \uc0b6\ub3c4, \uc5b4\ub290 \ucabd\uc774\ub4e0 \ub098\ub294 \uc644\uc804 \uc774\ub4dd!",
        "\uc774 \ubab8\uc73c\ub85c \uc0b4\uc544 \uc788\ub294 \ud55c, \ub0b4\uac00 \ud560 \uc88b\uc740 \uc77c\uc774 \uc788\uc5b4. \uc9c0\uae08 \ub2f9\uc7a5 \uace0\ub974\ub77c\uba74 \ubb58 \uace8\ub77c\uc57c \ud560\uc9c0 \ubaa8\ub974\uaca0\uc5b4. \uc9c4\uc9dc \uc5b4\ub824\uc6b4 \uc120\ud0dd\uc774\uc57c! \uc5ec\uae30\uc11c \ud150\ud2b8 \uac77\uace0 \uadf8\ub9ac\uc2a4\ub3c4\ub791 \ud568\uaed8 \uc788\uace0 \uc2f6\uc740 \ub9c8\uc74c\uc774 \uac15\ub82c\ud574. \uc5b4\ub5a4 \ub0a0\uc740 \uadf8\ubcf4\ub2e4 \uc88b\uc740 \uac8c \uc5c6\uc5b4. \uadfc\ub370 \ub300\ubd80\ubd84\uc740 \ub108\ud76c\uac00 \uacaa\ub294 \uc77c\uc744 \uc0dd\uac01\ud558\uba74, \ub0b4\uac00 \uc5ec\uae30\uc11c \ubc84\ud2f0\ub294 \uac8c \ub354 \ub0ab\ub2e4\ub294 \ud655\uc2e0\uc774 \ub4e4\uc5b4. \uadf8\ub798\uc11c \ud55c\ub3d9\uc548\uc740 \uc5ec\uae30 \uc788\uc73c\uba74\uc11c, \ud558\ub098\ub2d8\uc744 \ubbff\ub294 \uc0b6\uc5d0\uc11c \ub108\ud76c\uc758 \uc131\uc7a5\uacfc \uae30\uc068\uc774 \uacc4\uc18d\ub418\ub3c4\ub85d \ub3d9\ub8cc\ub85c \ud568\uaed8\ud560 \uacc4\ud68d\uc774\uc57c. \ub0b4\uac00 \ub2e4\uc2dc \ub108\ud76c\ub97c \ucc3e\uc544\uac08 \ub54c \uba4b\uc9c4 \uc7ac\ud68c\ub97c \uae30\ub300\ud574\ub3c4 \uc88b\uc544. \uadf8\ub0a0 \uc6b0\ub9ac\ub294 \uadf8\ub9ac\uc2a4\ub3c4\ub97c \ucc2c\uc591\ud558\uba74\uc11c \uc11c\ub85c \uc5c4\uccad \uae30\ubed0\ud560 \uac70\uc57c.",
        "\uadf8\ub54c\uae4c\uc9c0 \uadf8\ub9ac\uc2a4\ub3c4\uc758 \uba54\uc2dc\uc9c0\uc5d0 \uc5b4\uc6b8\ub9ac\ub294, \uba85\uc608\ub85c\uc6b4 \uc0b6\uc744 \uc0b4\uc544. \ub108\ud76c \ud589\ub3d9\uc774 \ub0b4\uac00 \uc624\ub290\ub0d0 \uc548 \uc624\ub290\ub0d0\uc5d0 \ub530\ub77c \ub2ec\ub77c\uc9c0\uba74 \uc548 \ub3fc. \ub0b4\uac00 \uc9c1\uc811 \uc640\uc11c \ubcf4\ub4e0, \uba40\ub9ac\uc11c \uc18c\uc2dd\ub9cc \ub4e3\ub4e0, \ub108\ud76c \ud589\ub3d9\uc740 \ud55c\uacb0\uac19\uc544\uc57c \ud574. \ud558\ub098\uac00 \ub418\uc5b4, \ud55c \ube44\uc804\uc73c\ub85c \uad73\uac8c \uc11c\uc11c, \uc0ac\ub78c\ub4e4\uc774 \uba54\uc2dc\uc9c0, \uace7 \ubcf5\ub41c \uc18c\uc2dd\uc744 \ubbff\ub3c4\ub85d \ud798\uc368 \uc2f8\uc6cc. \uc801\ub4e4 \uc55e\uc5d0\uc11c \ucac4\uc9c0\ub098 \ud53c\ud558\uc9c0 \ub9c8. \ub108\ud76c\uc758 \uc6a9\uae30\uc640 \ud558\ub098 \ub428\uc774 \uac40\ub4e4\ud55c\ud14c \ubcf4\uc5ec\uc904 \uac70\uc57c. \uac40\ub4e4\ud55c\ud14c\ub294 \ud328\ubc30, \ub108\ud76c\ud55c\ud14c\ub294 \uc2b9\ub9ac\ub77c\ub294 \uac78. \ub458 \ub2e4 \ud558\ub098\ub2d8\uc5d0\uac8c\uc11c \uc624\ub294 \uac70\uc57c. \uc774 \uc0b6\uc5d0\ub294 \uadf8\ub9ac\uc2a4\ub3c4\ub97c \ubbff\ub294 \uac83 \ub9d0\uace0\ub3c4 \ub354 \uc788\uc5b4. \uadf8\ubd84\uc744 \uc704\ud574 \uace0\ub09c\ubc1b\ub294 \uac83\ub3c4 \uc788\uc9c0. \uace0\ub09c\uc740 \ubbff\uc74c\ub9cc\ud07c\uc774\ub098 \uac12\uc9c4 \uc120\ubb3c\uc774\uc57c. \ub108\ud76c\ub294 \ub0b4\uac00 \uc5b4\ub5a4 \uc2f8\uc6c0\uc744 \uc2f8\uc6cc\uc654\ub294\uc9c0 \ubd24\uace0, \uc9c0\uae08 \uc774 \ud3b8\uc9c0\ub97c \ud1b5\ud574 \uc5c5\ub370\uc774\ud2b8\ub41c \uc18c\uc2dd\uc744 \ub4e3\uace0 \uc788\ub294 \uac70\uc57c. \ub108\ud76c\ub3c4 \ub611\uac19\uc740 \uc2f8\uc6c0\uc5d0 \ud568\uaed8\ud558\uace0 \uc788\uc5b4.",
    ],
    "verseRanges": ["1-2", "3-6", "3-6", "7-8", "9-11", "12-14", "12-14", "15-17", "18", "19-21", "22-26", "27-30"],
    "splits": [{"msg_range": "18-21", "paras": [9, 10],
                "note": "MSG \ub2e8\uc77c \ubb38\ub2e8(18-21)\uc744 KO \uac00\ub3c5\uc131\uc744 \uc704\ud574 2\uac1c \ubb38\ub2e8\uc73c\ub85c \ubd84\ub9ac"}],
    "changes": [
        "1\uc7a5: EN \uad6c\uc870(MSG \ubb38\ub2e8 \uae30\uc900)\uc5d0 \ub9de\ucdb0 KO \ubb38\ub2e8\u00b7\ubc30\uc9c0 \uc7ac\uad6c\uc131 \ubc0f \u00a7 \ud5e4\ub354(MSG \uc139\uc158 \uc81c\ubaa9) \ubc88\uc5ed \ucd94\uac00 ('\uc790\ub77c\ub098\ub294 \uc0ac\ub791', '\uac00\ub458 \uc218 \uc5c6\ub294 \uba54\uc2dc\uc9c0') \u2014 \uae30\uc874 \ucc3d\uc791 \ud5e4\ub354('\uc0ac\uc2ac \uc18d\uc758 \uae30\uc068', '\uc608\uc218\ub2d8\uc774 \uc644\uc804 \uc790\ub791\uc2a4\ub7ec\uc6cc\ud560 \ub9cc\ud55c \uc0b6', '\uc544\ubb34\ub3c4 \uac00\ub458 \uc218 \uc5c6\ub294 \uba54\uc2dc\uc9c0') \uc0ad\uc81c",
        "KO \ubc30\uc9c0 '3-5'\u2192'3-6', '6-8'\u2192'7-8', '22-25'\u2192'22-26', '26-30'\u2192'27-30' (EN\uacfc \ub3d9\uc77c)",
        "KO \ubc30\uc9c0 '17' \ubb38\ub2e8 \u2192 '18' (EN\uacfc \ub3d9\uc77c), 18-21\uc808 splits \uc120\uc5b8",
        "KO \uc804\uccb4\ub97c \ucd5c\uc885 EN \uae30\uc900\uc73c\ub85c 1:1 \uc7ac\ubc88\uc5ed (\uae30\uc874 KO\ub294 EN\uacfc \ubb38\ub2e8 \uc218\u00b7\ubc30\uc9c0 \ubd88\uc77c\uce58 \u2014 1\uc7a5 KO 12\ubb38\ub2e8 vs EN 11\ubb38\ub2e8)",
    ],
}

ko[2] = {
    "paragraphs": [
        "§종의 자리로 내려오신 분",
        "그러니까, 예수님을 따르면서 얻은 게 조금이라도 있거나, 그분의 사랑이 너희 삶을 조금이라도 바꿨거나, 성령님의 공동체에 속한 게 의미가 있거나, 마음이랑 배려심이 조금이라도 있다면, 부탁 하나만 들어줘. 서로 마음을 맞추고, 서로 사랑하고, 속 깊은 찐친이 되라는 거야. 앞으로 나서려고 밀지 말고, 말로 포장해서 위로 올라가려고도 하지 마. 나 자신은 내려놓고, 다른 사람이 앞서가게 도와줘. 내 이익 챙기느라 정신 팔지 말고, 나를 잊을 만큼 남을 도와줘.",
        "예수 그리스도가 자기를 어떻게 생각했는지, 너희도 그렇게 생각해 봐. 그분은 하나님과 동등한 자리였는데, 잘난 체하면서 그 자리의 혜택을 어떻게든 붙잡고 있어야 한다고 생각 안 하셨어. 전혀. 때가 되자 신으로서의 특권을 내려놓고 종의 자리를 택하셨어. 사람이 되신 거야! 사람이 되신 뒤로도 계속 사람으로 사셨어. 어마어마하게 자신을 낮추는 과정이었지. 특권 같은 건 하나도 주장 안 하시고, 그냥 이타적이고 순종하는 삶을 사시다가, 이타적이고 순종하는 죽음을 맞으셨어. 그것도 최악의 죽음, 십자가에서 말이야.",
        "그 순종 때문에 하나님이 그분을 높이 들어 올리시고, 그 누구도, 그 무엇도 받아본 적 없는 영광으로 높여주셨어. 그래서 하늘과 땅의 모든 피조물, 심지어 오래전에 죽어 묻힌 사람들까지도 이 예수 그리스도 앞에 무릎 꿇고 경배하며, 그분이 만물의 주인이시라고 찬양하게 하신 거야. 하나님 아버지께 큰 영광을 돌리면서.",
        "§함께 기뻐하기",
        "내가 하고 싶은 말은 이거야, 친구들아. 처음부터 해오던 대로 그냥 계속하라는 거야. 내가 너희랑 같이 살 때 너희는 순종하며 살았잖아. 지금은 내가 떨어져 있지만, 계속 그렇게 해. 아니, 더 열심히 해. 구원받은 사람답게 힘차게 살고, 하나님 앞에서 경건하고 조심스럽게. 그 힘은 하나님의 힘이야. 너희 안에 깊이 박혀 있는 힘. 하나님 자신이 원하시고, 일하시면서, 자기를 가장 기쁘게 할 일을 이루어가시는 거야.",
        "무슨 일이든 기쁘고 흔쾌히 해. 말다툼하거나 따지지 말고! 깨끗하게 세상 속으로 들어가서, 이 더럽고 썩은 사회에 신선한 공기를 불어넣어 줘. 사람들에게 착하게 사는 게 뭔지, 살아 계신 하나님이 어떤 분인지 보여줘. 어둠 속에 빛을 비추는 메시지를 전하라고. 그러면 그리스도께서 다시 오시는 날, 내가 너희를 자랑할 이유가 생길 거야. 너희는 내가 한 모든 수고가 헛되지 않았다는 살아 있는 증거가 될 거라고.",
        "내가 지금 여기서 처형당한다 해도, 너희가 그리스도의 제단에 믿음으로 바치는 제물에 내가 한 조각으로 포함되고, 너희 기쁨의 일부가 된다면 기뻐할 거야. 근데 공평하게, 너희도 내 기쁨에 동참해야 돼. 무슨 일이 있어도 나를 불쌍히 여기지 마.",
        "나는 (예수님의 계획에 따라) 조만간 디모데를 너희에게 보내서, 너희 소식을 최대한 알아오게 할 계획이야. 아, 그러면 내 마음이 얼마나 기쁘겠어! 나한테 디모데만 한 사람이 없어. 걔는 충성스럽고, 너희를 진심으로 걱정해. 여기 대부분 사람들은 자기 일만 챙기고 예수님의 일에는 관심이 별로 없거든. 근데 너희도 알다시피 디모데는 진짜야. 우리가 함께 메시지를 전하는 동안, 걔는 나한테 헌신적인 아들이었어. 여기서 내 일이 어떻게 될지 보이는 대로 걔를 보낼게. 그리고 나도 기도하면서 걔 바로 뒤따라가길 바라고 있어.",
        "근데 지금 당장은 내 좋은 친구이자 동역자인 에바브로디도를 보낼게. 너희가 걔를 보내서 나를 돕게 했으니까, 이제는 내가 걔를 보내서 너희를 돕게 하는 거야. 걔는 너희에게 돌아가고 싶어서 안달이 났었어. 너희도 들었겠지만 아팠다가 나은 뒤로는 더더욱, 자기는 멀쩡하다고 너희를 안심시켜주고 싶어서 돌아가고 싶어 했거든. 너희도 알다시피 걔는 죽을 뻔했는데, 하나님이 불쌍히 여겨주셨어. 걔한테만이 아니라 나한테도 자비를 베풀어주신 거지. 걔가 죽었으면 다른 모든 슬픔 위에 엄청난 슬픔이 하나 더 얹히는 거였어.",
        "그러니까 내가 걔를 너희에게 보내는 게 왜 이렇게 기쁜지 알겠지? 걔가 다시 건강하고 늠름한 모습으로 나타나면 너희는 얼마나 기쁘겠어. 나는 또 얼마나 안심이 되겠고. 성대하게 환영해주고 기쁘게 안아줘! 걔 같은 사람은 너희가 줄 수 있는 최고의 대접을 받을 자격이 있어. 너희가 나를 위해 시작했다가 마무리하지 못한 그 일 기억나? 걔는 그 일을 마무리하려고 목숨까지 걸었고, 그 일 하다가 죽을 뻔했어.",
    ],
    "verseRanges": ["1-4", "1-4", "5-8", "9-11", "12-13", "12-13", "14-16", "17-18", "19-24", "25-27", "28-30"],
    "splits": [],
    "changes": [
        "2장: EN 구조에 맞춰 KO 문단·배지 재구성 및 § 헤더(MSG 섹션 제목) 번역 ('종의 자리로 내려오신 분', '함께 기뻐하기') — 기존 창작 헤더('그리스도 찬가', '별처럼 빛나라', '함께 기뻐해라') 삭제 (기존 KO 13문단 → 11문단)",
        "KO 배지 '25-28'→'25-27' (EN과 동일)",
        "KO 전체를 최종 EN 기준으로 1:1 재번역",
    ],
}

ko[3] = {
    "paragraphs": [
        "§그분을 직접 알기",
        "우리 이야기는 이쯤 하고. 친구들아, 하나님 안에서 기뻐해! 전에 편지로 쓴 말을 또 하는 거, 나는 하나도 귀찮지 않아. 너희도 다시 듣는다고 짜증내지 않았으면 좋겠어. 나중에 후회하느니 안전하게 가는 게 낫잖아. 그래서 다시 쓴다.",
        "왈왈 짖어대는 개들, 그러니까 맨날 참견하는 종교인들, 시끄럽기만 하고 알맹이는 없는 그런 사람들은 피해 다녀. 걔네는 겉모습에만 목숨 거는 애들이야. 나는 걔네를 '할례 수술 매니아'라고 부른다. 진짜 믿는 사람은 하나님의 영이 이끄시는 대로 이 사역을 열심히 하고, 우리가 늘 하듯이 그리스도 찬양으로 세상을 가득 채우는 사람들이야. 우리 힘만으로는 절대 못 할 일이라는 거 우리 다 알잖아. 사람들이 아무리 대단해 보이는 스펙을 들이밀어도 말이야. 너희 내 배경 알지? 합법적으로 태어나서 여드레 만에 할례 받았고, 명문 베냐민 지파 출신 이스라엘 사람. 하나님의 율법을 엄격하고 열심히 지켰고, 우리 종교의 순수성을 지키겠다고 교회를 박해하기까지 했어. 하나님의 율법책에 적힌 건 하나도 빠짐없이 다 지켰다고.",
        "걔네가 뭔가 대단한 것처럼 흔들어대는 그 스펙들? 나는 찢어서 쓰레기통에 버렸어. 내가 예전에 내세우던 다른 모든 것들도 마찬가지고. 왜? 그리스도 때문이야. 응. 내가 한때 그렇게 중요하게 생각했던 모든 게 내 인생에서 사라졌어. 예수 그리스도를 내 주인으로 직접 아는 이 엄청난 특권에 비하면, 내가 예전에 도움 된다고 생각했던 모든 건 그냥 하찮은 쓰레기야. 다 버렸다니까. 내가 그리스도를 붙잡고, 그분께 붙잡히고 싶었거든. 규칙 목록 지키면서 얻는 그 시시하고 하찮은 의로움 말고, 그리스도를 믿어서 얻는 그 탄탄한 의로움, 곧 하나님의 의로움을 갖고 싶었어.",
        "그 모든 하찮은 것들을 버린 건, 그리스도를 직접 알고, 그분의 부활 능력을 경험하고, 그분의 고난에 동참하면서, 죽음에 이르기까지 그분과 끝까지 함께 가고 싶어서야. 죽은 사람들 가운데서 살아나는 부활에 동참할 방법이 있다면, 나는 그 길을 가고 싶었어.",
        "§목표를 향해",
        "내가 이 모든 걸 다 얻었다거나 다 이뤘다는 말이 아니야. 나는 그냥 잘 가고 있는 중이야. 놀라울 정도로 나를 붙잡아주신 그리스도를 붙잡으려고 손을 뻗고 있는 거지. 친구들아, 오해하지 마. 내가 이 모든 일에 전문가라고 생각하는 건 절대 아니야. 근데 목표는 확실히 보고 있어. 하나님이 우리를 부르시는 그곳, 바로 예수님을 향해. 나는 출발해서 달리는 중이고, 뒤돌아보지 않을 거야.",
        "그러니까 하나님이 우리를 위해 준비해두신 모든 걸 원하는 사람들은, 그 목표에 계속 집중하자. 너희 중에 100% 헌신이 아니라 다른 생각이 있는 사람이 있다면, 하나님이 그 흐릿한 시야를 깨끗하게 해주실 거야. 결국 보게 될 거라고! 이제 우리가 올바른 길에 들어섰으니까, 이 길에서 벗어나지 말자.",
        "친구들아, 나만 따라와. 같은 목표를 향해 우리랑 같은 코스를 달리는 사람들을 놓치지 마. 세상에는 다른 길을 가고 다른 목표를 선택하면서 너희를 끌어들이려는 사람들이 많아. 걔네 조심하라고 여러 번 경고했는데, 안타깝지만 또 경고해야겠어. 걔네는 그냥 편한 길만 원해. 그리스도의 십자가는 싫어한다고. 근데 편한 길은 막다른 길이야. 거기 사는 사람들은 자기 배를 신으로 섬겨. 트림이 걔들의 찬양이고, 머릿속에는 온통 먹을 생각뿐이야.",
        "하지만 우리에게는 훨씬 더 큰 삶이 있어. 우리는 높은 하늘의 시민이거든! 구원자이신 주인, 예수 그리스도가 오시기를 기다리고 있어. 그분이 우리의 이 흙 같은 몸을 그분 자신의 몸처럼 영광스러운 몸으로 바꿔주실 거야. 그분은 모든 것을 제자리에, 그분 아래와 주변에 두시는 그 강력한 능력으로 우리를 아름답고 온전하게 만들어주실 거야.",
    ],
    "verseRanges": ["1", "1", "2-6", "7-9", "10-11", "12-14", "12-14", "15-16", "17-19", "20-21"],
    "splits": [],
    "changes": [
        "3장: EN 구조에 맞춰 KO 문단·배지 재구성 ('1-4' 합본 → 1절 + 2-6절 분리, '13-14'→'12-14') 및 § 헤더(MSG 섹션 제목) 번역 ('그분을 직접 알기', '목표를 향해') — 기존 창작 헤더('그리스도를 아는 것이 전부다', '목표를 향해 달리기') 삭제 (기존 KO 11문단 → 10문단)",
        "기존 KO 2-6/4-6절 중복 배지 해소 — MSG 문단(2-6) 하나로 정리",
        "KO 전체를 최종 EN 기준으로 1:1 재번역",
    ],
}

ko[4] = {
    "paragraphs": [
        "사랑하는 내 친구들아! 너희를 진짜 많이 사랑해. 너희에게 최고로 좋은 것만 주고 싶어. 너희는 내 기쁨이고, 내 자랑이야. 흔들리지 마. 하나님 안에서 한 길로 쭉 가.",
        "§모든 것을 기도로",
        "유오디아랑 순두게에게 부탁해. 서로 의견 차이를 풀고 화해하라고. 하나님은 자기 자녀들이 서로 앙금 품는 거 원하지 않으셔.",
        "그리고, 어, 그래. 시지고스, 너는 지금 걔네 곁에 있으니까 걔네가 잘 풀어가도록 최선을 다해줘. 이 여성들은 글레멘드랑 나랑 다른 베테랑들이랑 손잡고 복음을 위해 열심히 일했던 사람들이야. 우리 중 누구 못지않게 열심히 했어. 걔네 이름도 생명책에 적혀 있다는 거 잊지 마.",
        "매일매일 하루 종일 하나님을 찬양해. 진짜 그분께 푹 빠져보라고! 만나는 모든 사람에게 너희가 자기들 편이라는 걸, 같이 일하고 싶지 반대편이 아니라는 걸 확실하게 보여줘. 주인께서 곧 오신다는 것도 알려줘. 진짜 언제 나타나실지 몰라!",
        "쫄거나 걱정하지 마. 걱정 대신 기도해. 걱정거리를 기도와 찬양으로 바꿔서 하나님께 너희 사정을 다 말씀드려봐. 그러면 너희도 모르는 사이에 하나님의 온전하심, 모든 게 선하게 합력된다는 그 느낌이 와서 너희 마음을 가라앉혀줄 거야. 그리스도가 너희 삶의 중심에서 걱정을 밀어내실 때 일어나는 일은 정말 대단해.",
        "정리하자면, 친구들아. 진짜인 것, 고귀한 것, 존경할 만한 것, 진실한 것, 마음을 끄는 것, 은혜로운 것들로 너희 마음을 채우고 묵상하는 게 제일 좋아. 최악 말고 최선을, 추한 거 말고 아름다운 걸, 저주할 거 말고 칭찬할 것들을 생각해. 나한테서 배운 걸 실천해. 너희가 듣고 보고 깨달은 것들을. 그렇게 하면 모든 것을 합력해서 선을 이루시는 하나님이 너희를 그분의 멋진 하모니 속으로 빚어주실 거야.",
        "§어떤 상황에서도 만족",
        "나는 하나님 안에서 기뻐. 너희가 상상하는 것보다 훨씬 행복해. 너희가 다시 나를 이렇게 신경 써줘서 기쁜 거야. 너희가 지금까지 나를 위해 기도 안 했거나 생각 안 했다는 게 아니야. 그냥 보여줄 기회가 없었을 뿐이지. 사실 나 개인적으로 필요한 건 없어. 이제 어떤 상황에서도 만족하는 법을 터득했거든. 적은 것으로도 많은 것으로도 똑같이 행복해. 배부르든 굶주리든, 손에 가득 쥐었든 빈손이든 행복하게 사는 비결을 찾았어. 뭘 가졌든 어디에 있든, 지금의 나를 만들어주신 그분 안에서 나는 모든 걸 해낼 수 있어. 그렇다고 너희 도움이 별거 아니었다는 뜻은 아냐. 진짜 컸어. 내가 힘들 때 함께해 준 거, 정말 아름다운 일이었어.",
        "빌립보 사람들아, 너희도 잘 알지? 그리고 나는 절대 안 잊을 거야. 내가 처음 마케도니아를 떠나서 복음을 전하러 다닐 때, 이 일의 주고받음에 함께한 교회는 너희밖에 없었어. 너희가 유일했지. 데살로니가에 있을 때도 도와줬잖아. 한 번만이 아니라 두 번이나. 내가 뭘 바라는 게 아니라, 너희가 베풂에서 나오는 복을 경험했으면 하는 마음이야.",
        "그리고 지금은 필요한 게 다 있고, 계속 더 생기고 있어! 너희가 에바브로디도를 통해 보내준 선물은 차고 넘쳤어. 제단에서 타오르며 향기를 가득 채우는 향기로운 제물 같았지. 하나님을 끝없이 기쁘시게 했어. 하나님이 너희에게 필요한 모든 것을 채워주실 거라고 확신해. 예수님에게서 흘러나오는 영광 안에서 그분의 씀씀이는 너희의 씀씀이를 훨씬 뛰어넘으니까. 우리 하나님 아버지는 영광이 넘쳐서 영원토록 흘러넘쳐. 진짜야.",
        "만나는 모든 예수님 따르는 사람들에게 안부 전해줘. 여기 있는 우리 친구들도 인사 전해. 여기 모든 그리스도인들, 특히 카이사르 궁전에서 일하는 믿는 사람들이 너희에게 안부를 전해.",
        "주인이신 예수 그리스도의 놀라운 은혜를 너희 마음 깊은 곳에서 받아들이고 경험하길 바래.",
    ],
    "verseRanges": ["1", "2", "2", "3", "4-5", "6-7", "8-9", "10-14", "10-14", "15-17", "18-20", "21-22", "23"],
    "splits": [],
    "changes": [
        "4장: EN 구조에 맞춰 KO 문단·배지 재구성 ('1-3' 합본 → 1/2/3절 분리, '4-7' 합본 → 4-5/6-7절 분리, '15-16'→'15-17', '17-20'→'18-20') 및 § 헤더(MSG 섹션 제목) 번역 ('모든 것을 기도로', '어떤 상황에서도 만족') — 기존 창작 헤더('항상 기뻐하라', '이런 것들을 생각하라', '빌립보 교인들의 향기로운 선물') 삭제 (기존 KO 14문단 → 13문단)",
        "1절 KO에 있던 6-7절 내용('걱정할 시간에 기도 하자')을 6-7절 문단으로 이동 — MSG 구조 정합",
        "KO 전체를 최종 EN 기준으로 1:1 재번역",
    ],
}

# ---------------------------------------------------------------- emit
def chapter_dict(store, ch):
    c = store[ch]
    return {
        "chapter": ch,
        "title": titles[ch] if store is en else ko_titles[ch],
        "paragraphs": c["paragraphs"],
        "verseRanges": c["verseRanges"],
        "msg_ranges": list(c["verseRanges"]),
        "merges": [],
        "splits": c["splits"],
        "changes": c["changes"],
        "confirmations_needed": [],
        "review_status": "msg_audited",
    }

# sanity: EN/KO paragraph counts and badges must match
for ch in (1, 2, 3, 4):
    assert len(en[ch]["paragraphs"]) == len(en[ch]["verseRanges"]), ch
    assert len(ko[ch]["paragraphs"]) == len(ko[ch]["verseRanges"]), ch
    assert len(en[ch]["paragraphs"]) == len(ko[ch]["paragraphs"]), ch
    assert en[ch]["verseRanges"] == ko[ch]["verseRanges"], ch

with open("fixes/en_Philippians.json", "w", encoding="utf-8") as f:
    json.dump([chapter_dict(en, ch) for ch in (1, 2, 3, 4)], f, ensure_ascii=False, indent=2)
with open("fixes/ko_Philippians.json", "w", encoding="utf-8") as f:
    json.dump([chapter_dict(ko, ch) for ch in (1, 2, 3, 4)], f, ensure_ascii=False, indent=2)
print("wrote fixes/en_Philippians.json and fixes/ko_Philippians.json")
