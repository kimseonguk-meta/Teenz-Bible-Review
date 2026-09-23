
# ================= LUKE 24 =================
luke_en_paras = [
"§Looking for the Living in a Cemetery",
"Very early on Sunday morning, the women took the spices they had prepared to the tomb.",
"They found the massive stone rolled completely away from the entrance! They walked in, but the body of the Lord Jesus was gone.",
"While they were standing there totally confused, two men wearing clothes that literally flashed like lightning suddenly stood beside them. The women were terrified and dropped face-down to the dirt.",
'The glowing men said to them: "Why are you looking for the living among the dead? He isn\'t here; he has risen! Remember what he told you back in Galilee: The Son of Man had to be handed over to sinners, be crucified, and on the third day rise again."',
"Then it clicked. They remembered his words.",
"They sprinted back from the tomb and told the eleven apostles and everyone else what happened. (It was Mary Magdalene, Joanna, Mary the mother of James, and a few others).",
"But the guys thought the women were talking absolute nonsense and didn't believe a word of it. Peter, however, jumped up and literally sprinted to the tomb. He bent over, looked in, and saw only the strips of linen lying there. He walked away completely mind-blown, wondering what in the world had happened.",
"§Undercover on the Road to Emmaus",
"That exact same day, two of Jesus's followers were walking to a village called Emmaus, about seven miles outside Jerusalem. They were talking about the insane events of the weekend.",
"While they were debating, Jesus himself walked up and started traveling with them, but God kept them from recognizing him.",
'Jesus asked, "What are you guys arguing about?"',
'They stopped dead in their tracks, looking absolutely devastated. One guy, Cleopas, said, "Are you the only visitor in Jerusalem who doesn\'t know what just happened?"',
'"What things?" Jesus asked.',
'"About Jesus of Nazareth!" they replied. "He was a man of God, a prophet \u2014 insanely powerful in everything he said and did, and both God and the people loved him. We totally thought he was the one who was going to rescue Israel. But the chief priests handed him over, got him sentenced to death, and they crucified him. And get this \u2014 today is already the third day since it all went down. But now, some women from our group totally blew our minds. They went to the tomb this morning, couldn\'t find his body, and claimed they saw angels who said he was alive! Some of our guys went to check, and the tomb was empty just like the women said, but they didn\'t see him."',
'Jesus essentially said, "You guys are so slow to catch on! Didn\'t the Messiah have to suffer all these things before entering his glory?" Then, starting all the way back with Moses and the prophets, Jesus explained exactly how the entire Old Testament pointed straight to him.',
'When they got to Emmaus, Jesus acted like he was going to keep walking. But they begged him, "Stay with us, it\'s getting dark!" So he went in.',
"When they sat down at the table, Jesus took the bread, gave thanks, broke it, and handed it to them.",
"Instantly, their eyes were opened, and they realized it was him! And the second they recognized him, he literally vanished into thin air.",
'They looked at each other. "Weren\'t our hearts burning inside us when he was explaining the Scriptures on the road?!"',
"§The Final Boss Move",
'They didn\'t even care that it was dark; they got up immediately and ran all seven miles back to Jerusalem. They burst into the room where the Eleven and their friends were gathered and yelled, "It\'s true! The Lord has risen \u2014 Simon saw him with his own eyes!"',
"Then the two told them the whole story \u2014 everything that happened on the road, and how they recognized him when he broke the bread.",
'While they were still telling the story, Jesus himself suddenly materialized right in the middle of the room. "Peace be with you," he said.',
"They absolutely lost their minds with terror, thinking they were seeing a ghost.",
'"Why are you so freaked out? Why are you doubting? Look at my hands and my feet. It\'s really me! Touch me and see. Ghosts don\'t have flesh and bones like I do." He showed them his hands and his feet.',
"They were so full of joy and shock they still couldn't process it \u2014 it seemed too good to be true.",
'So Jesus asked, "Do you guys have anything to eat here?" They handed him a piece of broiled fish, and he ate it right in front of them.',
"§You're the Witnesses",
'He looked at his team. "This is exactly what I told you when I was still with you: Everything written about me in the Law, the Prophets, and the Psalms had to be fulfilled." Then he opened their minds so they could finally fully understand the Bible.',
'"This is what is written: The Messiah will suffer and rise from the dead on the third day. Now, forgiveness of sins will be preached in his name to all nations, starting right here in Jerusalem. You are my official witnesses. I am going to send you what my Father promised; but stay in the city until you are completely clothed with power from heaven."',
"Jesus led them out to the vicinity of Bethany. He lifted his hands and blessed them. While he was blessing them, he physically left them and was taken straight up into heaven.",
"His disciples fell down and worshipped him, and then returned to Jerusalem with massive, unstoppable joy. They stayed continually at the Temple, praising God.",
]
luke_en_vr = ['1-3','1-3','1-3','4-8','4-8','4-8','9-11','9-12','13-16','13-16','13-16',
 '17-18','17-18','19-24','19-24','25-27','28-31','28-31','28-31','32','33-34','33-34',
 '35','36-41','36-41','36-41','36-41','41-43','44','44-49','45-49','50-51','52-53']
luke_en_merges = [
 {"para": 7, "msg_ranges": ["9-11","12"], "note": "MSG 9-11 후반부(사도들의 불신)와 12절(베드로의 무덤 방문)을 하나의 EN 문단으로 합침"},
 {"para": 29, "msg_ranges": ["44","45-49"], "note": "MSG 44절(율법·예언서·시편 성취 선언)과 45-49 전반부(제자들의 마음 열기)를 하나의 EN 문단으로 합침"},
]
luke_en_splits = [
 {"msg_range": "1-3", "paras": [1,2], "note": "MSG 단일 문단(1-3)을 EN 가독성을 위해 2개 문단으로 분리"},
 {"msg_range": "4-8", "paras": [3,4,5], "note": "MSG 단일 문단(4-8)을 EN 가독성을 위해 3개 문단으로 분리"},
 {"msg_range": "9-11", "paras": [6,7], "note": "MSG 9-11이 EN 6번 문단(전반부: 보고)과 7번 문단(후반부: 불신 + 12절 병합)에 나뉨"},
 {"msg_range": "13-16", "paras": [9,10], "note": "MSG 단일 문단(13-16)을 EN 가독성을 위해 2개 문단으로 분리"},
 {"msg_range": "17-18", "paras": [11,12], "note": "MSG 단일 문단(17-18)을 EN 가독성을 위해 2개 문단으로 분리"},
 {"msg_range": "19-24", "paras": [13,14], "note": "MSG 단일 문단(19-24)을 EN 가독성을 위해 2개 문단으로 분리"},
 {"msg_range": "28-31", "paras": [16,17,18], "note": "MSG 단일 문단(28-31)을 EN 가독성을 위해 3개 문단으로 분리"},
 {"msg_range": "36-41", "paras": [23,24,25,26], "note": "MSG 단일 문단(36-41)을 EN 가독성을 위해 4개 문단으로 분리"},
 {"msg_range": "45-49", "paras": [29,30], "note": "MSG 45-49가 EN 29번 문단(전반부: 마음 열기 + 44절 병합)과 30번 문단(후반부: 기록된 말씀 선포)에 나뉨"},
]
luke_en_confirms = [
 "24장 7번 문단: MSG [9-11, 12] 2개 문단을 하나의 EN 문단(배지 '9-12')으로 합침 — 컨펌 필요",
 "24장 29번 문단: MSG [44, 45-49] 2개 문단을 하나의 EN 문단(배지 '44-49')으로 합침 — 컨펌 필요",
]
luke_en_changes = [
 "24: 19-24절 'dynamic in work and word, blessed by both God and all the people'(말과 행동에 능력 있고 하나님과 백성에게 인정받음) 누락 복원",
 "24: 19-24절 'it is now the third day since it happened'(사건 발생 3일째) 누락 복원",
 "24: 33-34절 'Simon saw him!'(시몬이 주님을 목격) 누락 복원",
 "24: 35절(엠마오 두 제자의 예루살렘 보고) 누락 문단 복원 — 기존 EN에 없던 문단",
 "24: 36-41절 'He showed them the nail scars' → MSG 원문대로 'He showed them his hands and his feet'로 수정",
 "24: 41-43절 'Do you have anything to eat here?' 질문을 MSG 위치(41-43 문단)로 이동",
 "24: MSG 36-41/41-43의 41절 겹침은 MSG 원문 구조 그대로 유지(splits 선언으로 커버)",
 "24: §헤더 추가 — 1-3절 앞 '§Looking for the Living in a Cemetery', 44절 앞 \"§You're the Witnesses\" (MSG 섹션 구획); 기존 '§The Final Boss Move'를 MSG 구획 위치(33-34절 앞)로 이동",
]

luke_ko_paras = [
"§무덤에서 살아 계신 분 찾기",
"일요일 새벽, 여자들이 미리 준비해둔 향료를 들고 무덤으로 갔어.",
"가보니까 무덤 입구를 막던 돌이 굴려져 있네? 그래서 안으로 들어갔지. 근데 들어가보니까 예수님 시신이 없는 거야.",
"완전 어리둥절하고 있는데, 갑자기 눈뽕 장난 아닌 두 사람이 나타나서 옆에 딱 서는 거임. 여자들은 너무 무서워서 얼굴을 땅에 박았지.",
'그 사람들이 말했어. "왜 살아있는 분을 무덤에서 찾고 있어? 여기 안 계셔. 다시 살아나셨다고. 갈릴리에 계실 때, 죄인들 손에 넘겨져서 십자가에 못 박히고 3일 만에 다시 살아나야 한다고 말씀하셨던 거 기억 안 나?"',
"그제서야 여자들은 예수님이 하셨던 말씀이 생각났어.",
"걔네들, 무덤에서 돌아와서 이 모든 일을 11명의 제자랑 다른 사람들한테 다 말해줬지. (막달라 마리아, 요안나, 야고보의 엄마 마리아, 그리고 다른 여자들도 같이 얘기했어.)",
"근데 사도들은 하나도 안 믿는 거야. 여자애들이 그냥 하는 소리라고 생각했대. 베드로는 벌떡 일어나서 무덤으로 뛰어갔어. 몸을 숙여서 안을 들여다보니까 진짜 수의밖에 없는 거야. 베드로는 '이게 뭔 일이지?' 하면서 고개를 갸우뚱하며 돌아갔지.",
"§엠마오행 언더커버",
"그날 바로 그날, 예수님의 제자 두 명이 예루살렘에서 11킬로쯤 떨어진 엠마오라는 마을로 걸어가고 있었어. 주말에 있었던 미친 사건들에 대해 열띤 토론 중이었지.",
"토론이 한창일 때 예수님이 직접 걸어오셔서 동행하기 시작하셨는데, 하나님께서 그들이 예수님을 알아보지 못하게 하셨대.",
'예수님이 물으셨어. "여러분, 걸으면서 무슨 이야기를 그렇게 열심히 하시나요?"',
'그러자 걔네들은 세상에서 제일 친한 친구라도 잃은 것처럼 슬픈 얼굴로 딱 멈춰 섰어. 그중에 글로바라는 사람이 말했지. "지난 며칠 동안 예루살렘에서 있었던 일을 당신만 혼자 모른다는 게 말이나 되나요?"',
'예수님이 "무슨 일인데요?" 하고 물으셨어.',
'걔네들이 말했지. "나사렛 예수님한테 일어난 일이요. 그분은 말이나 행동에 능력이 넘치고, 하나님이랑 모든 백성한테 인정받는 하나님의 사람이자 예언자셨거든요. 근데 대제사장이랑 지도자들이 그분을 넘겨서 사형 선고받게 하고 십자가에 못 박아버렸어요. 우리는 그분이야말로 이스라엘을 구할 찐 희망이라고 믿고 있었는데… 그 일이 있은 지 벌써 3일이나 지났네요. 근데 더 대박인 건, 우리 쪽 여자 몇 명이 우리를 완전 멘붕에 빠뜨렸어요. 오늘 아침 일찍 무덤에 갔는데 예수님 시신을 못 찾았다는 거예요. 돌아와서는 천사들을 봤는데, 그 천사들이 예수님이 살아계시다고 했다는 거 있죠. 우리 친구 몇 명도 무덤에 가서 확인해봤는데, 여자들 말대로 무덤은 비어 있었지만 예수님은 못 봤대요."',
'그러자 예수님이 말씀하셨어. "아, 정말 답답하고 꽉 막힌 사람들이네요! 왜 예언자들이 말한 것을 그냥 그대로 믿지를 못하나요? 메시아가 이런 고난을 겪고 나서 자기의 영광으로 들어가야 한다는 것을 정말 몰랐나요?" 그러고는 모세의 책부터 시작해서 모든 예언서를 훑으면서, 자기에 대해 나온 성경 구절을 하나하나 다 짚어주셨어.',
'그들은 목적지인 마을 입구에 거의 다 왔어. 예수님이 계속 가려고 하시니까, 걔네들이 붙잡았지. "저희랑 같이 저녁 드시고 가세요. 벌써 날도 저물었잖아요." 그래서 예수님은 그 집에 같이 들어가셨어.',
"식탁에 같이 앉아서 빵을 들어 축복하시고, 떼어서 그들에게 주셨지.",
"바로 그 순간, 그들의 눈이 번쩍 뜨였어. 깜짝 놀라서 눈이 동그래진 그들이 예수님을 알아본 거야. 근데 바로 그 순간 예수님이 사라지셨어.",
'걔네들이 서로 말했지. "그분이 길에서 우리랑 얘기하면서 성경 풀어주실 때, 우리 마음속이 막 뜨거워지지 않았나요?"',
"§최종 보스의 한 수",
'그들은 1초도 지체하지 않고 바로 일어나서 예루살렘으로 다시 달려갔어. 가보니까 11명의 제자랑 친구들이 다 같이 모여서 얘기하고 있더라고. "이거 실화임! 주님이 진짜 살아나셨대. 시몬이 주님을 직접 봤대!"',
"그러자 그 두 명도 길에서 있었던 일이랑, 예수님이 빵을 떼어주실 때 그분을 알아봤던 얘기를 전부 다 해줬어.",
'막 그런 얘기를 하고 있는데, 갑자기 예수님이 그들 한가운데 나타나서 말씀하셨어. "여러분, 평안하세요."',
"걔네들은 유령 보는 줄 알고 완전 쫄았지.",
'예수님이 말씀하셨어. "왜 이렇게 당황하세요? 의심 좀 그만하세요. 제 손이랑 발을 보세요. 진짜 저 맞잖아요. 만져보세요. 머리부터 발끝까지 잘 보세요. 유령은 이런 살이랑 뼈가 없어요." 이렇게 말씀하시면서 자기 손이랑 발을 보여주셨어.',
"걔네들은 눈으로 보면서도 믿기지가 않았어. 너무 좋아서 오히려 현실감이 없었던 거지.",
'예수님이 물으셨어. "여기 먹을 거 좀 있나요?" 그들은 구운 생선 한 토막을 드렸어. 예수님은 그걸 받아서 그들이 보는 앞에서 드셨지.',
"§너희가 증인이다",
'예수님이 말씀하셨어. "제가 여러분과 같이 있을 때 말했었죠? 모세의 율법, 예언서, 시편에 저에 대해 기록된 모든 것이 다 이루어져야 한다고요." 예수님은 계속해서 그들이 하나님의 말씀을 깨달을 수 있도록 이해력을 넓혀주시고, 성경을 어떻게 읽어야 하는지 설명해주셨어.',
'그분이 말씀하셨지. "성경에 이렇게 쓰여 있는 거 여러분도 아시죠? 메시아가 고난을 받고 3일째 되는 날에 죽은 사람들 가운데서 살아나고, 죄를 용서받고 삶이 완전히 바뀌는 복음이 예루살렘에서부터 시작해서 모든 민족에게 그분의 이름으로 전파될 거라고 말이에요. 여러분은 이 모든 것을 보고 들은 첫 번째 증인들이에요. 이제부터가 정말 중요해요! 제 아버지께서 약속하신 선물을 제가 여러분에게 보내줄게요. 여러분은 그분이 오셔서 위로부터 오는 능력을 받을 때까지 이 성에 머물러 계세요."',
"예수님은 그들을 데리고 성 밖으로 나가 베다니로 가셨어. 손을 들어 그들을 축복하시고, 그들을 떠나 하늘로 올라가셨지.",
"그들은 무릎을 꿇고 예수님께 경배하고, 터질듯한 기쁨을 안고 예루살렘으로 돌아왔어. 그리고는 하나님을 찬양하면서 모든 시간을 성전에서 보냈대!",
]
luke_ko_vr = list(luke_en_vr)
luke_ko_merges = [
 {"para": 7, "msg_ranges": ["9-11","12"], "note": "MSG 9-11 후반부(사도들의 불신)와 12절(베드로의 무덤 방문)을 하나의 KO 문단으로 합침"},
 {"para": 29, "msg_ranges": ["44","45-49"], "note": "MSG 44절(율법·예언서·시편 성취 선언)과 45-49 전반부(제자들의 마음 열기)를 하나의 KO 문단으로 합침"},
]
luke_ko_splits = [
 {"msg_range": "1-3", "paras": [1,2], "note": "MSG 단일 문단(1-3)을 KO 가독성을 위해 2개 문단으로 분리"},
 {"msg_range": "4-8", "paras": [3,4,5], "note": "MSG 단일 문단(4-8)을 KO 가독성을 위해 3개 문단으로 분리"},
 {"msg_range": "9-11", "paras": [6,7], "note": "MSG 9-11이 KO 6번 문단(전반부: 보고)과 7번 문단(후반부: 불신 + 12절 병합)에 나뉨"},
 {"msg_range": "13-16", "paras": [9,10], "note": "MSG 단일 문단(13-16)을 KO 가독성을 위해 2개 문단으로 분리(기존 KO에 누락되어 있던 내용 복원)"},
 {"msg_range": "17-18", "paras": [11,12], "note": "MSG 단일 문단(17-18)을 KO 가독성을 위해 2개 문단으로 분리"},
 {"msg_range": "19-24", "paras": [13,14], "note": "MSG 단일 문단(19-24)을 KO 가독성을 위해 2개 문단으로 분리"},
 {"msg_range": "28-31", "paras": [16,17,18], "note": "MSG 단일 문단(28-31)을 KO 가독성을 위해 3개 문단으로 분리"},
 {"msg_range": "36-41", "paras": [23,24,25,26], "note": "MSG 단일 문단(36-41)을 KO 가독성을 위해 4개 문단으로 분리"},
 {"msg_range": "45-49", "paras": [29,30], "note": "MSG 45-49가 KO 29번 문단(전반부: 마음 열기 + 44절 병합)과 30번 문단(후반부: 기록된 말씀 선포)에 나뉨"},
]
luke_ko_confirms = [
 "24장 7번 문단: MSG [9-11, 12] 2개 문단을 하나의 KO 문단(배지 '9-12')으로 합침 — 컨펌 필요",
 "24장 29번 문단: MSG [44, 45-49] 2개 문단을 하나의 KO 문단(배지 '44-49')으로 합침 — 컨펌 필요",
]
luke_ko_changes = [
 "24: 기존 KO에 MSG 13-16절(엠마오로 가는 두 제자·예수님의 동행·알아보지 못함) 전체 누락 → 9번·10번 문단으로 복원",
 "24: 기존 KO 5번('엠마오로 가는 길', § 없음)과 KO 6번('§엠마오로 가는 길') 중복 헤더 → '§엠마오행 언더커버' 하나로 정리",
 "24: 기존 KO 0번·12번·17번 헤더에 § 누락 → '§무덤에서 살아 계신 분 찾기', '§최종 보스의 한 수', '§너희가 증인이다'로 수정(EN/KO parity)",
 "24: 기존 KO 배지 오류 수정 — '17-19'→'19-24', '19-25'→'25-27', '25-28'→'28-31', '33-35'→'33-34', '36-40'→'36-41' 등",
 "24: 기존 KO 11번이 28-31 후반부+32절을 합쳐놓은 것을 분리(18번 '28-31', 19번 '32')",
 "24: 기존 KO 20번 '§최후의 결정적 순간' 헤더 삭제 — MSG에 해당 구획 없음, EN 구조와 일치시킴",
 "24: KO 23번 '안심하세요' → MSG 'Peace be with you'에 맞춰 '평안하세요'로 수정",
 "24: EN과 동일한 문단 수(33개)·배지로 재구성",
]

save('en_Luke.json', {
 "chapter": 24, "title": "The Empty Tomb and The Epic Comeback",
 "paragraphs": luke_en_paras, "verseRanges": luke_en_vr, "msg_ranges": luke_en_vr,
 "merges": luke_en_merges, "splits": luke_en_splits,
 "changes": luke_en_changes, "confirmations_needed": luke_en_confirms,
})
save('ko_Luke.json', {
 "chapter": 24, "title": "",
 "paragraphs": luke_ko_paras, "verseRanges": luke_ko_vr, "msg_ranges": luke_ko_vr,
 "merges": luke_ko_merges, "splits": luke_ko_splits,
 "changes": luke_ko_changes, "confirmations_needed": luke_ko_confirms,
})
print('Luke done:', len(luke_en_paras), len(luke_ko_paras))
