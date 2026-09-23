
# ================= JOHN 21 =================
john_en_paras = [
"§The Fishing Trip",
"After all that, Jesus appeared to his guys again \u2014 this time at the Sea of Tiberias, also known as the Sea of Galilee. Here's how it went down: Simon Peter, Thomas (nicknamed \"Twin\"), Nathanael from Cana in Galilee, the Zebedee brothers, and two other disciples were hanging out together. Simon Peter announced, \"I'm going fishing.\"",
'The rest of the guys said, "We\'re coming with you." They headed out and climbed into the boat \u2014 and caught absolutely nothing all night. As the sun came up, Jesus was standing on the beach, but they had no clue it was him.',
'Jesus called out to them, "Good morning! Did you catch anything for breakfast?" "Nope, nothing," they shouted back.',
'He said, "Throw your net off the right side of the boat and see what happens." They did, and suddenly there were so many fish they weren\'t strong enough to haul the net in!',
'Then the disciple Jesus loved turned to Peter and said, "It\'s the Master!" The second Simon Peter realized it was the Master, he threw on his outer clothes (he\'d stripped down for work) and dove straight into the sea. The other disciples came in by boat \u2014 they weren\'t far from shore, maybe a hundred yards \u2014 towing the net full of fish. When they got out of the boat, they saw a charcoal fire already going, with fish and bread cooking on it.',
'Jesus said, "Bring some of the fish you just caught." Simon Peter jumped in and dragged the net ashore \u2014 153 huge fish! And even with all those fish, the net didn\'t rip.',
'"Breakfast is ready," Jesus said. Not one of the disciples dared to ask, "Who are you?" \u2014 they knew it was the Master.',
"Jesus walked over, took the bread, and handed it to them. He did the same with the fish. This was now the third time Jesus had shown himself alive to the disciples since rising from the dead.",
"§Do You Love Me?",
'After breakfast, Jesus said to Simon Peter, "Simon, son of John, do you love me more than these?" "Yes, Master," Peter said, "you know I love you." Jesus said, "Feed my lambs."',
'He asked a second time, "Simon, son of John, do you love me?" "Yes, Master, you know I love you." Jesus said, "Shepherd my sheep."',
'Then, a third time: "Simon, son of John, do you love me?" Peter was upset that Jesus asked a third time. "Master," he said, "you know everything \u2014 you\'ve got to know I love you." Jesus said, "Feed my sheep. I\'m telling you the straight-up truth: when you were young, you dressed yourself and went wherever you wanted. But when you\'re old, you\'ll stretch out your hands, and someone else will dress you and take you where you don\'t want to go." (He said this to hint at the kind of death that would bring glory to God.) Then he gave the command: "Follow me."',
'Peter turned and spotted the disciple Jesus loved following right behind them. "Master," Peter asked, "what\'s going to happen to him?"',
'Jesus said, "If I want him to stay alive until I come back, what\'s that to you? You \u2014 follow me." Naturally, a rumor spread among the believers that this disciple wouldn\'t die. But that\'s not what Jesus said at all \u2014 he only said, "If I want him to stay alive until I come back, what\'s that to you?"',
"This is the disciple who saw it all with his own eyes and wrote it down \u2014 and we know his account is the real deal, totally reliable. And that's not even half of it: Jesus did so many other things, if every single one were written down, the whole world couldn't hold all the books.",
]
john_en_vr = ['1-3','1-3','3-4','5','6','7-9','10-11','12','13-14','15','15','16','17-19','20-21','22-23','24-25']
john_en_merges = [
 {"para": 15, "msg_ranges": ["24","25"], "note": "MSG 24절(목격자 증언의 신뢰성)과 25절(기록되지 않은 수많은 일들)을 요한복음 결론 문단으로 합침"},
]
john_en_splits = [
 {"msg_range": "3", "paras": [1,2], "note": "MSG 원문에서 1-3절과 3-4절 문단이 3절을 공유하는 구조를 그대로 유지"},
]
john_en_confirms = [
 "21장 15번 문단: MSG [24, 25] 2개 문단을 하나의 EN 문단(배지 '24-25')으로 합침 — 컨펌 필요",
]
john_en_changes = [
 "21: MSG '### Fishing' 구획에 §헤더 '§The Fishing Trip' 추가; MSG '### Do You Love Me?' 구획에 §헤더 추가(기존 'The Restoration of The Rock' 대체)",
 "21: 1-3절 'Thomas (nicknamed Twin)', 'Nathanael from Cana in Galilee', 'the brothers Zebedee' 고유 디테일 복원(기존 EN의 'James, John' 자의적 특정 수정)",
 "21: 5절 'Good morning! Did you catch anything for breakfast?' MSG 표현 복원(기존 'Friends, haven't you caught any fish?' 수정)",
 "21: 7-9절 'a hundred yards or so'(해안에서 백 야드쯤) 누락 복원",
 "21: 10-11절 '153 big fish / net didn't rip'을 기존 EN 1번 문단에서 MSG 위치(10-11 문단)로 이동",
 "21: 15절 앞 헤더 문단의 MSG 외부 해석('숯불 앞에서의 부인' 연결, '두려워하면서도 간절히 필요했던 순간') 제거",
 "21: 17-19절 '세 번의 사랑 고백으로 세 번의 부인을 청산·공식 리더로 복권' 등 MSG 외부 해석 2문장 제거",
 "21: 20-23절 'mind his own business' 의역을 MSG 뉘앙스('what's that to you? You — follow me')에 가깝게 정리",
]

john_ko_paras = [
"§고기잡이 여행",
"그 후에 예수님이 제자들한테 또 나타나셨는데, 이번엔 디베랴 바다(갈릴리 호수)에서였어요. 예수님이 나타나신 건 이런 스토리예요. 시몬 베드로, '쌍둥이'라고 불리는 도마, 갈릴리 가나 사람 나다나엘, 세베대의 아들 둘, 그리고 다른 제자 두 명이 같이 있었죠. 시몬 베드로가 말했어요. \"나 고기 잡으러 가야겠다.\"",
'나머지 애들도 "우리도 같이 감" 하고 대답했어요. 그래서 다 같이 나가서 배를 탔죠. 근데 그날 밤, 한 마리도 못 잡은 거예요. 해 뜰 때쯤 예수님이 바닷가에 서 계셨는데, 제자들은 그분이 예수님인 줄 몰라봤어요.',
'예수님이 그들한테 말했어요. "좋은 아침! 아침으로 먹을 거 좀 잡았나요?" 그들이 대답했죠. "아뇨, 하나도 못 잡았어요."',
'예수님이 말했어요. "그물을 배 오른쪽에 던져보세요. 어떻게 되나 한번 보자고요." 그들은 예수님이 시키는 대로 했죠. 그랬더니 순식간에 물고기가 엄청나게 그물에 걸려든 거예요. 와, 힘이 딸려서 그물을 못 끌어올릴 정도였대요.',
'그때 예수님이 아끼던 제자가 베드로한테 말했어요. "주님이시다!" 시몬 베드로는 그분이 주님인 걸 알고, 일하느라 벗어뒀던 옷을 후다닥 챙겨 입고 바다로 뛰어들었어요. 다른 제자들은 배에 탄 채로 물고기 가득한 그물을 끌고 나왔죠. 걔네는 육지에서 한 90미터 정도밖에 안 떨어진 곳에 있었거든요. 배에서 내려보니까 숯불이 피워져 있고, 그 위에 생선이랑 빵이 익고 있었어요.',
'예수님이 말했어요. "여러분들이 방금 잡은 생선 몇 마리 가져와 보세요." 시몬 베드로가 다른 제자들이랑 힘 합쳐서 그물을 바닷가로 끌어올렸는데, 세상에, 큰 물고기가 153마리나 들어있는 거예요! 그렇게 많이 잡혔는데도 그물이 안 찢어지다니, 진짜 신기했어요.',
'예수님이 말했어요. "아침밥 준비됐어요. 와서 드세요." 제자들 중에는 "누구세요?" 하고 감히 묻는 사람이 아무도 없었어요. 다들 그분이 주님인 걸 알고 있었거든요.',
"예수님이 빵을 들어서 그들한테 주시고, 생선도 나눠주셨어요. 예수님이 죽었다가 살아나신 뒤에 제자들한테 나타나신 건 이번이 세 번째였대요.",
"§나를 사랑하느냐?",
'아침밥 다 먹고 나서 예수님이 시몬 베드로한테 물어봤어요. "요한의 아들 시몬아, 네가 이 사람들보다 저를 더 사랑하나요?" "네, 주님. 제가 주님 사랑하는 거 주님이 아시잖아요." 예수님이 말했어요. "제 어린 양들을 잘 먹이세요."',
'그러고 나서 예수님이 두 번째로 물어봤어요. "요한의 아들 시몬아, 네가 저를 사랑하나요?" "네, 주님. 제가 주님 사랑하는 거 주님이 아시잖아요." 예수님이 말했어요. "제 양들을 잘 돌보세요."',
'예수님이 세 번째로 물어봤어요. "요한의 아들 시몬아, 네가 저를 사랑하나요?" 예수님이 "네가 저를 사랑하나요?" 하고 세 번이나 물어보니까 베드로는 맘이 좀 그랬죠. "주님, 주님은 모든 걸 아시잖아요. 제가 주님 사랑하는 거 당연히 아시죠." 예수님이 말했어요. "제 양들을 잘 먹이세요. 이제 여러분에게 진짜 중요한 거 알려드릴게요. 여러분이 젊었을 때는 여러분 스스로 옷 입고 가고 싶은 데 막 다녔잖아요. 근데 여러분이 늙으면 두 팔을 벌리게 될 거고, 다른 사람이 여러분에게 옷을 입히고 여러분이 원하지 않는 곳으로 여러분을 데려갈 거예요." 예수님이 이렇게 말한 건, 베드로가 어떤 죽음으로 하나님께 영광을 돌릴지 알려주신 거였어요. 이 말을 하시고 예수님이 명령했죠. "저를 따라오세요."',
'베드로가 고개를 돌려보니까 예수님이 아끼던 제자가 바로 뒤에서 따라오고 있었어요. 베드로가 그를 보고 예수님한테 물었죠. "주님, 그럼 쟤는 어떻게 돼요?"',
'예수님이 말했어요. "제가 다시 올 때까지 그를 살려둔다고 해도, 그게 여러분과 무슨 상관인데요? 여러분은 그냥 저나 따라오세요." 그래서 제자들 사이에서 그 제자는 안 죽을 거라는 소문이 쫙 퍼진 거예요. 근데 예수님이 한 말은 그런 뜻이 아니었어요. 예수님은 그냥 "제가 다시 올 때까지 걔를 살려둔다고 해도 그게 여러분과 뭔 상관이에요?" 라고 말했을 뿐이에요.',
"이 모든 걸 직접 보고 기록한 사람이 바로 그 제자예요. 우리 모두는 그의 증언이 찐이고 정확하다는 걸 알고 있어요. 이거 말고도 예수님은 진짜 많은 일을 하셨어요. 그걸 하나도 안 빼놓고 다 기록한다면, 아마 이 세상에 그 책들을 다 놔둘 공간도 부족할 걸.",
]
john_ko_vr = list(john_en_vr)
john_ko_merges = [
 {"para": 15, "msg_ranges": ["24","25"], "note": "MSG 24절(목격자 증언의 신뢰성)과 25절(기록되지 않은 수많은 일들)을 요한복음 결론 문단으로 합침"},
]
john_ko_splits = [
 {"msg_range": "3", "paras": [1,2], "note": "MSG 원문에서 1-3절과 3-4절 문단이 3절을 공유하는 구조를 그대로 유지"},
]
john_ko_confirms = [
 "21장 15번 문단: MSG [24, 25] 2개 문단을 하나의 KO 문단(배지 '24-25')으로 합침 — 컨펌 필요",
]
john_ko_changes = [
 "21: MSG '### Fishing' 구획에 §헤더 '§고기잡이 여행' 추가; MSG '### Do You Love Me?' 구획에 '§나를 사랑하느냐?' 추가",
 "21: 기존 KO 배지 오류 수정 — '1-2'→'1-3', '3-5'→'3-4', '7-8'→'7-9', '17'→'17-19', '20-23'→'20-21'(9번)",
 "21: 기존 KO 2번(5-6절 병합)을 3번 '5'·4번 '6'으로 분리; 기존 KO 5번(12+13-14절 병합)을 7번 '12'·8번 '13-14'로 분리(MSG 문단 구조 일치)",
 "21: KO 2번 끝 '믿기 힘든.', KO 4번 끝 '놀라운.' 등 어색한 조각 문장 정리",
 "21: EN과 동일한 문단 수(16개)·배지로 재구성",
]

save('en_John.json', {
 "chapter": 21, "title": "Breakfast on the Beach and The Comeback",
 "paragraphs": john_en_paras, "verseRanges": john_en_vr, "msg_ranges": john_en_vr,
 "merges": john_en_merges, "splits": john_en_splits,
 "changes": john_en_changes, "confirmations_needed": john_en_confirms,
})
save('ko_John.json', {
 "chapter": 21, "title": "",
 "paragraphs": john_ko_paras, "verseRanges": john_ko_vr, "msg_ranges": john_ko_vr,
 "merges": john_ko_merges, "splits": john_ko_splits,
 "changes": john_ko_changes, "confirmations_needed": john_ko_confirms,
})
print('John done:', len(john_en_paras), len(john_ko_paras))
