# -*- coding: utf-8 -*-
# 수동 override: (장, EN para idx) 기준. idx는 원본 fixes/en_{book}.json 기준.
NULL_BADGES = {
    # ('Luke', 2, 3): '...',
}
REWRITES = {
    (1, 2): "That messenger was John the Baptist. He showed up in the desert with a bold message: \"Turn your life around, get baptized, and God will forgive your sins.\"",
    (1, 11): "Walking down the beach, Jesus saw two brothers, Simon (Peter) and Andrew, throwing their fishing nets into the water. Fishing was their everyday job. Jesus called out, \"Come follow me! I'll teach you how to fish for actual people instead of perch and bass.\" They dropped their nets on the spot and followed him. A little further down, he saw James and John, the sons of Zebedee, fixing nets in their boat. He called them too, and right away they left their dad Zebedee in the boat with the hired workers and joined the crew.",
    (1, 14): "Jesus didn't flinch. \"Be quiet and get out of him!\" he commanded. The evil spirit violently threw the man into a spasm, shrieked, and left.",
    (1, 15): "Everyone there was spellbound, buzzing with curiosity. \"What's going on? A new teaching—and it actually works! He shuts up unclean spirits and tells them to get lost!\" News about Jesus spread like wildfire through the whole region of Galilee.",
    (1, 16): "After that, Jesus went to Simon and Andrew's house, with James and John along. Simon's mother-in-law was in bed, burning up with fever. They told Jesus about her. He went to her, took her hand, and helped her up—and the fever left her instantly. She got right up and started making dinner for them. That evening, after sunset, the whole town crowded at the door, bringing everyone who was sick or tormented by evil spirits. Jesus healed their sick bodies and freed their troubled minds. The demons knew exactly who he was, so he shut them up—no talking.",
    (1, 18): "Jesus said, \"Let's head to the nearby villages. I need to preach there too—that's exactly why I came.\"",
    (1, 19): "So he traveled all through Galilee, preaching in their meeting places and driving out demons.",
}
DROPS = {}
INSERTS = {}
BADGE_FIX = {
    (1, 14): '25-26',
    (1, 15): '27-28',
}
CHANGES_EXTRA = {
    1: [
        "EN 4번 문단(배지 '4'): MSG 7-8 내용(세례 요한의 '내 뒤에 오시는 분' 선포)이 중복 포함되어 있어 4절 내용만 남기고 삭제 — 7-8절은 7번 문단에 그대로 유지",
        "EN 12번 문단(배지 '16-20'): MSG의 '제베대' 이름, '품꾼들' 언급 복원",
        "EN 14번 문단 배지 '25-27'→'25-26', 15번 문단 배지 '28'→'27-28': MSG 문단 구분(25-26/27-28)에 맞춤. 15번 문단에 27절 군중 반응('새로운 가르침' 언급) 복원",
        "EN 16번 문단(배지 '29-34'): MSG 29-31의 야고보·요한 동행, 손 잡고 일으킴, 저녁 식사 준비 및 32-34의 귀신 입막음 이유('자기 정체를 알았기 때문') 복원",
        "EN 18번 문단(배지 '38'): 39절 내용('갈릴리 전역 전도')이 중복 포함되어 있어 38절만 남김. 19번 문단(배지 '39')은 39절만 유지",
    ],
}

REWRITES.update({
    (2, 5): "The guy stood right up, grabbed his mat, and walked out while everyone stared in total shock, praising God. They said, \"We've never seen anything like this!\"",
    (2, 8): "Later, Jesus saw Levi, the son of Alphaeus, sitting at his tax booth. Jesus said, \"Follow me,\" and Levi got up and followed him.",
    (2, 17): "Jesus shut them down: \"Did you ever read what King David did when his guys were starving? He walked right into the sanctuary and ate the holy bread off the altar—with Chief Priest Abiathar standing right there watching! That bread was only for priests, but David shared it with his companions too. Listen to me: The Sabbath was made to help people; people weren't made to be slaves to the Sabbath. The Son of Man doesn't take orders from the Sabbath—he's in charge of it!\"",
})
CHANGES_EXTRA.update({
    2: [
        "EN 6번 문단(배지 '10-12'): MSG 12절 군중 반응 직접 인용(\"We've never seen anything like this!\") 복원",
        "EN 9번 문단(배지 '14'): MSG에 없는 '(마태)' 표기 삭제, MSG의 '알패오의 아들 레위'로 정정",
        "EN 17번 문단(배지 '25-28'): MSG의 '아비아달 대제사장' 언급과 '동료들에게 나눠줌' 복원. 'I'm the boss of the Sabbath'를 MSG 뉘앙스('안식일의 종이 아니라 주인')에 맞춰 보강",
    ],
})

REWRITES.update({
    (3, 5): "The crowds following Jesus were getting dangerously huge. People from Galilee, Judea, Jerusalem, Idumea, across the Jordan, and around Tyre and Sidon had heard the reports and came to see for themselves. He had healed so many people that everyone who had something wrong was pushing and shoving just to touch him. He had to have his disciples keep a small boat ready so he wouldn't get trampled by the crowd.",
    (3, 7): "Jesus hiked up a mountain and called up the specific guys he wanted on his core team. He appointed twelve of them to be his official \"apostles\" (messengers). The plan was that they would be with him, and he would send them out to proclaim the Word and give them authority to banish demons. They were: Simon\u2014Jesus named him Peter, meaning \"Rock\"; James son of Zebedee and his brother John\u2014Jesus nicknamed the brothers Boanerges, meaning \"Sons of Thunder\"; Andrew, Philip, Bartholomew, Matthew, Thomas, James son of Alphaeus, Thaddaeus, Simon the Canaanite, and Judas Iscariot (who betrayed him).",
    (3, 9): "Jesus went home, but the crowd was so crazy he and his guys couldn't even eat. The people closest to him heard what was going on and came to take charge of him, by force if necessary\u2014they thought he was losing it.",
    (3, 11): "Jesus called them over and exposed how clueless that logic was: \"Does it make sense to send a devil to catch a devil\u2014to use Satan to get rid of Satan? A constantly squabbling family disintegrates. If Satan were fighting Satan, there soon wouldn't be any Satan left. And do you think you can walk into the house of a strong, wide-awake man in broad daylight and walk off with his stuff unless you tie him up first? Tie him up, though, and you can clean him out.\"",
    (3, 13): "Then Jesus' mother and brothers showed up. They stood outside and sent someone in to tell Jesus they needed to talk. Jesus was surrounded by a crowd when he heard, \"Your mother and brothers and sisters are outside looking for you.\"",
})
CHANGES_EXTRA.update({
    3: [
        "EN 6번 문단(배지 '7-10'): MSG의 지역 목록(갈릴리·유대·예루살렘·이두매·요단 건너편·두로와 시돈) 복원",
        "EN 8번 문단(배지 '13-19'): 열두 사도 임명 목적(함께 있게 하고 말씀 전파·귀신 쫓는 권위) 복원. '베드로(반석)' 뜻, '보아너게(우레의 아들들)' 별명, '가나안인 시몬' 복원",
        "EN 10번 문단(배지 '20-21'): MSG의 '친구들'(가족이 아님)과 'by force if necessary' 뉘앙스 복원",
        "EN 12번 문단(배지 '23-27'): MSG의 '다투는 가정은 무너진다', '사탄이 사탄과 싸우면 사탄이 남지 않는다', 대낮에 강한 자 집에 들어가는 비유 복원",
        "EN 15번 문단(배지 '31-32'): MSG의 '누이와 형제들'('sisters') 언급 복원",
    ],
})

REWRITES.update({
    (4, 3): "Some fell on the walking path, and birds ate them immediately.",
    (4, 4): "Some fell on gravel. They sprouted fast but burned up in the sun because they had no roots.",
    (4, 5): "Some fell in the weeds, which choked the plants so they couldn't produce anything.",
    (4, 6): "But some fell in good, rich dirt and came up with a flourish, producing a harvest way beyond the farmer's wildest dreams!\"",
    (4, 17): "\"Listen carefully to what I'm saying\u2014and watch out for the slick advice that tells you how to get ahead in life on your own. Giving, not getting, is the way. Generosity creates generosity. Stinginess just makes you poor.\"",
    (4, 20): "Jesus also said: \"What is God's kingdom like? What kind of story can we use? It's like an acorn. When it lands on the ground it's tiny as seeds go, but once it's planted it grows into a huge oak tree with thick branches. Eagles nest in it.\"",
})
CHANGES_EXTRA.update({
    4: [
        "EN 3~6번 문단(배지 '4'/'5-6'/'7'/'8', MSG 3-8 씨 뿌리는 비유): MSG 3-8에는 없는 해석 괄호(괄호 안 인물 유형 풀이) 삭제 — MSG 3-8은 이야기만 있고 해석은 14-20절에 있음. 8절 문단에 MSG 20절 내용('thirty, sixty, or a hundred')이 섞여 있어 MSG 3-8 표현('a flourish, beyond wildest dreams')으로 정정",
        "EN 17번 문단(배지 '24-25'): MSG 마가 4:24-25에 없는 'measuring stick' 문장(다른 복음서 내용) 삭제, MSG 본문('be wary of the shrewd advice... Giving, not getting')으로 교체",
        "EN 20번 문단(배지 '30-32'): MSG의 'acorn(도토리)→huge oak tree→Eagles'를 KJV식 'mustard seed'로 바꾼 것을 MSG 원문대로 정정",
    ],
})

FULL_CHAPTERS = {5: {'paras': [
("§The Madman", "1-5"),
("They landed on the other side of the lake in the country of the Gerasenes. The moment Jesus stepped out of the boat, a madman from the cemetery who was tormented by an evil spirit came up to him. He lived there among the tombs and graves. No one could restrain him\u2014he couldn't be chained, couldn't be tied down. He had been tied up many times with chains and ropes, but he broke the chains and snapped the ropes. No one was strong enough to tame him. Night and day he roamed through the graves and the hills, screaming out and slashing himself with sharp stones.", "1-5"),
("When he saw Jesus a long way off, he ran and bowed in worship before him\u2014then howled in protest, \"What business do you have, Jesus, Son of the High God, messing with me? I swear to God, don't give me a hard time!\" (Jesus had just commanded the tormenting evil spirit, \"Out! Get out of the man!\")", "6-8"),
("Jesus asked him, \"Tell me your name.\" The demon replied, \"My name is Mob\u2014I'm a rioting mob. There's an entire army of us inside this guy.\" Then he desperately begged Jesus not to banish them from the country.", "9-10"),
("A large herd of pigs was grazing and rooting on a nearby hill. The demons begged him, \"Send us to the pigs so we can live in them.\" Jesus gave the order. But it was even worse for the pigs than for the man. Crazed, they stampeded over a cliff into the sea and drowned.", "11-13"),
("Those tending the pigs, scared to death, bolted and told their story in town and country. Everyone wanted to see what had happened. They came up to Jesus and saw the madman sitting there wearing decent clothes and making sense, no longer a walking madhouse of a man.", "14-15"),
("Those who had seen it told the others what had happened to the demon-possessed man and the pigs. At first they were in awe\u2014and then they were upset, upset over the drowned pigs. They demanded that Jesus leave and not come back.", "16-17"),
("As Jesus was getting into the boat, the demon-delivered man begged to go along, but he wouldn't let him. Jesus said, \"Go home to your own people. Tell them your story\u2014what the Master did, how he had mercy on you.\" The man went back and began to preach in the Ten Towns area about what Jesus had done for him. He was the talk of the town.", "18-20"),
("§A Risk of Faith", "21-24"),
("After Jesus crossed over by boat, a large crowd met him at the seaside. One of the meeting-place leaders named Jairus came. When he saw Jesus, he fell to his knees, beside himself as he begged, \"My dear daughter is at death's door. Come and lay hands on her so she will get well and live.\" Jesus went with him, the whole crowd tagging along, pushing and jostling him.", "21-24"),
("A woman who had suffered a condition of hemorrhaging for twelve years\u2014a long succession of physicians had treated her, and treated her badly, taking all her money and leaving her worse off than before\u2014had heard about Jesus. She slipped in from behind and touched his robe. She was thinking to herself, \"If I can put a finger on his robe, I can get well.\" The moment she did it, the flow of blood dried up. She could feel the change and knew her plague was over and done with.", "25-29"),
("At the same moment, Jesus felt energy discharging from him. He turned around to the crowd and asked, \"Who touched my robe?\"", "30"),
("His disciples said, \"What are you talking about? With this crowd pushing and jostling you, you're asking, 'Who touched me?' Dozens have touched you!\"", "31"),
("But he went on asking, looking around to see who had done it. The woman, knowing what had happened, knowing she was the one, stepped up in fear and trembling, knelt before him, and gave him the whole story.", "32-33"),
("Jesus said to her, \"Daughter, you took a risk of faith, and now you're healed and whole. Live well, live blessed! Be healed of your plague.\"", "34"),
("While he was still talking, some people came from the leader's house and told him, \"Your daughter is dead. Why bother the Teacher any more?\"", "35"),
("Jesus overheard what they were talking about and said to the leader, \"Don't listen to them; just trust me.\"", "36"),
("He permitted no one to go in with him except Peter, James, and John. They entered the leader's house and pushed their way through the gossips looking for a story and neighbors bringing in casseroles. Jesus was abrupt: \"Why all this busybody grief and gossip? This child isn't dead; she's sleeping.\" Provoked to sarcasm, they told him he didn't know what he was talking about.", "37-40"),
("But when he had sent them all out, he took the child's father and mother, along with his companions, and entered the child's room. He clasped the girl's hand and said, \"Talitha koum,\" which means, \"Little girl, get up.\" At that, she was up and walking around! This girl was twelve years of age. They, of course, were all beside themselves with joy. He gave them strict orders that no one was to know what had taken place in that room. Then he said, \"Give her something to eat.\"", "40-43"),
]}}

REWRITES.update({
    (6, 2): "But then, in the very next breath, they started tearing him down. \"Isn't this just the carpenter? Mary's son? We've known him since he was a little kid! We know his brothers, James, Justus, Jude, and Simon, and his sisters. Who does he think he is, anyway?\" They completely stumbled over the limited stuff they thought they knew about him, and that was it. They couldn't move past it.",
    (6, 6): "\"Don't think you need a lot of extra gear for this. You guys are the gear! No special fundraising appeals. Keep it simple.\"",
    (6, 32): "But when they saw him walking on the sea, they thought it was a ghost and screamed, scared to death.",
    (6, 33): "Jesus was quick to comfort them: \"Courage! It's me. Don't be afraid.\" As soon as he climbed into the boat, the wind completely died down. They were totally stunned, shaking their heads, wondering what in the world was going on. They hadn't really understood what he had done at the supper. None of this had truly sunk into their hearts yet.",
})
BADGE_FIX.update({(6, 6): "8-9", (6, 32): "49", (6, 33): "50-52"})
INSERTS.setdefault(6, []).append((6, "10", "\"And no luxury inns. Find a modest place and be cool with staying there until you move on.\""))
CHANGES_EXTRA.update({
    6: [
        "EN 7번 문단(배지 '8-10'): MSG [8-9]+[10] 2개 문단을 합쳐 있던 것을 MSG 문단 구분에 맞춰 '8-9'와 '10' 2개 문단으로 분리",
        "EN 32~33번 문단(배지 '49-50'/'51-52'): MSG [47-49]+[50-52]를 넘나들던 것을 MSG 문단 경계에 맞춰 '49'와 '50-52'로 재구성",
        "EN 3번 문단(배지 '3'): MSG에 없는 'and his sisters are all right here with us'의 'are all right here with us' 삭제",
    ],
})

REWRITES.update({
    (7, 8): "Jesus then called the crowd back together and said, \"Listen up, everyone\u2014really pay attention to this.\"",
    (7, 9): "\"It's not what you eat or swallow that makes your life messed up; it's what comes *out* of you\u2014that's the real pollution.\"",
    (7, 18): "Jesus said to her, \"Hold on, take your turn. The children get fed first. If there's any food left over, then the dogs get it.\"",
})
CHANGES_EXTRA.update({
    7: [
        "EN 10~11번 문단(배지 '14-15'): 여는 따옴표가 닫히지 않던 것을 각 문단에서 따옴표 완성",
        "EN 19번 문단(배지 '27'): MSG에 없는 해석 삽입 '(meaning the Jewish people)', '(a term sometimes used for Gentiles)' 삭제",
    ],
})

REWRITES.update({
    (8, 5): "The crowd ate until they were stuffed. They even collected seven baskets of leftovers! Over four thousand people had eaten that day. Then he sent them all home. Jesus himself immediately got into the boat with his disciples and headed off for Dalmanoutha.",
    (8, 20): "Peter immediately answered, \"You are the Christ, the Messiah.\"",
    (8, 21): "Jesus warned them to keep it on the down-low, not to breathe a word of it to anyone. He then started explaining things to them: \"It's necessary that the Son of Man go through a really tough time of suffering, be tried and found guilty by the elders, high priests, and religion scholars. He'll be killed, and then after three days, he'll rise up alive.\" He said this simply and clearly so they couldn't miss it.",
    (8, 22): "But Peter grabbed him in protest. Turning and seeing his disciples wavering, wondering what to believe, Jesus confronted Peter. \"Peter, get out of my way! Satan, get lost! You have no idea how God works.\"",
})
CHANGES_EXTRA.update({
    8: [
        "EN 6번 문단(배지 '7-10'): MSG에 없는 강조 'huge' 삭제('seven huge baskets'→'seven baskets')",
        "EN 21번 문단(배지 '29'): MSG에 없는 해석 삽입 '(the Anointed One, the promised Deliverer)' 삭제",
        "EN 22번 문단(배지 '30-32'): MSG에 없는 해석 삽입 '(a title Jesus used for himself)' 삭제. MSG [30-32] 끝 문장('He said this simply and clearly...')을 EN 23번에서 EN 22번 끝으로 이동",
        "EN 23번 문단(배지 '32-33'): MSG [32-33] 내용에 맞춰 정리",
    ],
})

REWRITES.update({
    (9, 31): "\"If your hand or your foot gets in God's way, chop it off and throw it away! You're better off maimed or lame and alive than having two hands and two feet and ending up godless in a furnace of eternal fire. And if your eye distracts you from God, pull it out and throw it away! You're better off one-eyed and alive than having perfect vision and ending up in the fire of hell.\"",
    (9, 32): "\"Everyone's going through a refining fire sooner or later, but you'll be well-preserved, protected from the eternal flames. Be preservatives yourselves. Preserve the peace.\"",
})
CHANGES_EXTRA.update({
    9: [
        "EN 33번 문단(배지 '43-48'): MSG에 없는 해석 삽입 '(causes you to sin)', '(spiritually)' 삭제",
        "EN 34번 문단(배지 '49-50'): MSG에 없는 해석 삽입 '(a tough time that purifies them)' 삭제",
    ],
})

REWRITES.update({
    (10, 18): "Jesus looked him right in the eye\u2014and loved him! He said, \"There's just one more thing you need to do: Go sell everything you own and give the money to the poor. All that wealth will then be like treasure stored up in heaven. And then, come follow me.\"",
    (10, 31): "\"They will sentence him to death. Then they'll hand him over to the Romans, who will mock him, spit on him, give him the third degree, and kill him. But after three days, he will rise alive.\"",
    (10, 36): "Jesus said, \"You have no idea what you're even asking for. Are you capable of drinking the cup I drink, or being baptized in the baptism I'm about to be plunged into?\"",
    (10, 42): "\"That's exactly what the Son of Man has done: He didn't come to be served, but to serve others\u2014and then to give away his life as a ransom for many.\"",
})
CHANGES_EXTRA.update({
    10: [
        "EN 19번 문단(배지 '21'): MSG에 없는 해석 삽입 'for his sincerity' 삭제",
        "EN 32번 문단(배지 '32-34'): MSG에 없는 해석 'torture him' 삭제('give him the third degree' 원문 유지)",
        "EN 37번 문단(배지 '38'): MSG에 없는 해석 'the bitter cup of suffering', 'the same kind of difficult experience' 삭제",
        "EN 43번 문단(배지 '45'): MSG에 없는 해석 삽입 '(payment to free someone held hostage)' 삭제",
    ],
})

REWRITES.update({
    (11, 6): "The crowd totally went wild, giving him an amazing welcome! Some people were throwing their coats on the street, while others were spreading out rushes they'd cut from the fields.",
    (11, 8): "\"Hosanna! Blessed is the one who comes in God's name! Blessed is the coming kingdom of our ancestor David! Hosanna in the highest heaven!\"",
})
CHANGES_EXTRA.update({
    11: [
        "EN 8번 문단(배지 '8-10'): MSG 원문('rushes')으로 복원('palm branches' 해석 삭제)",
        'EN 10번 문단: MSG에 없는 Hosanna 해석 삽입 삭제',
    ],
})

REWRITES.update({
    (12, 9): "After that, some Pharisees and followers of Herod sent people to try and trap Jesus. They hoped to catch him saying something that would get him in trouble. They came up to him and said, \"Teacher, we know you're legit. You're honest, you don't care what other people think, you don't just tell your students what they want to hear, and you teach God's truth accurately. So, tell us: Is it legal to pay taxes to Caesar (the Roman emperor) or not?\"",
})
CHANGES_EXTRA.update({
    12: [
        "EN 10번 문단(배지 '13-14'): MSG에 없는 해석 삽입 '(who were political enemies but united against Jesus)' 삭제",
    ],
})

REWRITES.update({
    (13, 4): "Jesus started by saying, \"Listen up, watch out for people who try to trick you with 'doomsday' prophecies. A lot of leaders are going to pop up with fake identities, claiming, 'I'm the One.' They'll fool a ton of people.\"",
    (13, 13): "\"But get ready to bolt when you see 'the monster of desecration' set up where it should never be. If you're reading this, make sure you understand what I'm talking about.\"",
    (13, 21): "\"After those hard times, the sun will start to fade out, the moon will get cloudy, stars will fall out of the sky, and even the cosmic powers will tremble.\"",
    (13, 22): "\"And then, everyone will see the Son of Man arrive in a super grand way, his coming filling the sky\u2014no one will miss it! He'll send out the angels; they will gather his chosen people from all four directions, from one end of the earth to the other.\"",
    (13, 24): "And it's the same with you. When you see all these things I've described, you'll know he is right at the door. Don't take this lightly.",
    (13, 26): "\"But the exact day and hour? No one knows that\u2014not even the angels in heaven, not even the Son. Only the Father knows. So stay super alert, because you don't know the exact schedule.\"",
})
BADGE_FIX.update({(13, 16): "19-20"})
CHANGES_EXTRA.update({
    13: [
        'EN 5번 문단: MSG에 없는 Messiah 해석 삽입 삭제',
        "EN 14번 문단(배지 '14'): MSG에 없는 해석 삽입 '(a terrible, unholy thing)' 삭제",
        "EN 17번 문단 배지 '18'→'19-20': MSG 문단 구분 기준('These are going to be hard days'는 MSG 19-20절 내용)에 맞춤",
        "EN 22번 문단(배지 '24-25'): MSG에 없는 해석 삽입 '(the spiritual forces that influence the universe)' 삭제",
        "EN 23번 문단(배지 '26-27'): MSG에 없는 해석 삽입 '(that's me)' 삭제",
        "EN 25번 문단(배지 '29-30'): MSG에 없는 해석 삽입 '(meaning me, or my coming)' 삭제",
        "EN 27번 문단(배지 '32'): MSG에 없는 해석 삽입 '(meaning me)' 삭제",
    ],
})

REWRITES.update({
    (14, 16): "He said, \"It's one of the Twelve, someone who dips his bread in the same bowl with me. In one way, it totally makes sense that the Son of Man is going through this betrayal, just like the Scriptures said\u2014no surprises there.\"",
    (14, 20): "Then he took the cup (chalice), thanked God, and gave it to them, and they all drank from it. He said, \"This is my blood, God's new covenant, poured out for many people.\"",
    (14, 31): "Going a little ahead, he fell to the ground and prayed for a way out: \"Papa, Father, you can\u2014can't you?\u2014get me out of this. Take this cup away from me. But please, don't do what I want\u2014do what you want.\"",
    (14, 35): "He came back a third time and said, \"Are you going to sleep all night? No\u2014you've slept long enough. Time's up. The Son of Man is about to be betrayed into the hands of sinners. Get up. Let's get going. My betrayer has arrived.\"",
    (14, 41): "\"What you've actually done is confirm what the prophetic writings said would happen.\" All the disciples ditched him and ran away.",
    (14, 52): "Some of them started spitting at him. They blindfolded his eyes, then hit him, saying, \"Who hit you? Prophesy!\" The guards, punching and slapping, took him away.",
    (14, 57): "After a little while, the bystanders brought it up again. \"You've gotta be one of them. You've got 'Galilean' written all over you.\"",
})
BADGE_FIX.update({(14, 38): "44-45", (14, 45): "55-56", (14, 55): "68", (14, 57): "70"})
CHANGES_EXTRA.update({
    14: [
        "EN 39번 문단 배지 '44'→'44-45': 입맞춤 내용(45절) 커버리지 반영",
        "EN 46번 문단 배지 '55'→'55-56': 56절 내용(거짓 증언 상쇄) 커버리지 반영",
        "EN 56번 문단 배지 '68-69'→'68': 내용은 68절만 해당 — 잘못된 merge 판정 제거",
        "EN 58번 문단 배지 '70-71'→'70': 내용은 MSG 69-70절 문단 꼬리(70절)만 해당 — 잘못된 merge 판정 제거",
        "EN 17번 문단(배지 '20'): MSG에 없는 해석 삽입 '(that's me)', '(ancient prophecies)' 삭제",
        "EN 21번 문단(배지 '23-24'): MSG에 없는 해석 삽입 '(a sacred agreement)' 삭제",
        "EN 32번 문단(배지 '35-36'): MSG에 없는 해석 삽입 '(suffering)' 삭제",
        "EN 36번 문단(배지 '41-42'): MSG에 없는 해석 삽입 '(that's me)' 삭제",
        "EN 42번 문단(배지 '49-50'): MSG에 없는 해석 삽입 '(Scriptures)' 삭제",
        "EN 53번 문단(배지 '65'): MSG에 없는 해석 삽입 '(tell the future)' 삭제",
        "EN 58번 문단(배지 '70'): MSG에 없는 해석 삽입 '(meaning he talked like people from Galilee)' 삭제",
    ],
})

REWRITES.update({
    (15, 14): "They divided up his clothes and threw dice to see who would get them.",
    (15, 19): "Some of the people standing nearby who heard him said, \"Listen, he's calling for Elijah.\" Someone quickly ran off, soaked a sponge in sour wine, put it on a stick, and held it up for him to drink, saying, \"Let's see if Elijah actually comes to take him down.\"",
    (15, 20): "But Jesus, with one last loud cry, took his final breath. At that exact moment, the huge curtain in the Temple ripped right down the middle. When the Roman captain who was standing guard right in front of him saw that Jesus had stopped breathing, he said, \"This guy absolutely had to be the Son of God!\"",
})
CHANGES_EXTRA.update({
    15: [
        "EN 16번 문단(배지 '24'): MSG에 없는 해석 삽입 '(gambled)' 삭제",
        "EN 21번 문단(배지 '35-36'): MSG에 없는 해석 삽입 '(a famous prophet)' 삭제",
        "EN 22번 문단(배지 '37-39'): MSG에 없는 해석 삽입 '(which separated the most sacred part)', 'from top to bottom' 삭제",
    ],
})
