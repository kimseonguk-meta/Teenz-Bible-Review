#!/usr/bin/env python3
"""Mark 16 / Luke 24 / John 21 MSG 대조 fixes JSON 생성."""
import json, os

OUT = '/home/hatch/workspace/teenz-bible-review/fixes'
os.makedirs(OUT, exist_ok=True)

def save(name, chapter_dict):
    p = os.path.join(OUT, name)
    json.dump([chapter_dict], open(p, 'w'), ensure_ascii=False, indent=1)
    print('wrote', p)

# ================= MARK 16 =================
mark_en_paras = [
"§The Resurrection",
"""Very early on Sunday morning, Mary Magdalene, Mary the mother of James, and Salome bought spices to anoint Jesus's body. They were walking to the tomb, wondering, "Who is going to help us roll that massive stone away?\"""",
"""But when they got there, the stone was already rolled back — and it was a huge stone! They walked right into the tomb and saw a young man sitting on the right side, dressed all in white. They were completely taken aback, totally stunned.""",
"""He said, "Don't be afraid. I know you're looking for Jesus of Nazareth, the one they nailed to the cross. He's been raised up — he's not here anymore! See for yourselves, the place is empty. Now get going: tell his disciples, and Peter, that he's going ahead of you to Galilee. You'll see him there, exactly like he said.\"""",
"""The women ran out of the tomb as fast as they could, totally freaked out, their heads spinning. They were so stunned they didn't say a word to anyone.""",
"""[Heads up: the oldest copies of Mark end at verse 8 — the rest (verses 9-20) comes from later copies. Here's how that longer ending tells it:] After rising from the dead, Jesus appeared early on Sunday morning, first to Mary Magdalene — the same Mary he had freed from seven demons. She ran to his heartbroken friends, who were weeping and carrying on, and told them the news. But when they heard she had seen him alive and well, they didn't believe her one bit.""",
"""Later, he appeared in a totally different form to two of them as they were walking out in the countryside. They rushed back and told the rest, but no one believed them either.""",
"""Still later, he appeared to the Eleven themselves while they were eating supper — and he called them out hard for their stubborn refusal to believe the people who had seen him risen. Then he said, "Go into the entire world and preach the Good News to absolutely everyone. Anyone who believes and is baptized will be saved — but anyone who refuses to believe will be condemned.\"""",
""""And these insane signs will follow everyone who believes: they'll drive out demons in my name, they'll speak in brand-new languages, they'll pick up snakes with their bare hands, they'll drink poison and walk away totally fine, and they'll lay hands on sick people and heal them.\"""",
"""After briefing them, the Master Jesus was taken up into heaven and sat down at the right hand of God, the place of honor. The disciples went out and preached everywhere, and the Master worked right alongside them, backing up the message with undeniable miracles. (Note: Mark 16:9-20 — the part in brackets — isn't found in the earliest handwritten copies of Mark.)""",
]
mark_en_vr = ['1-3','1-3','4-5','6-7','8','9-11','12-13','14-16','17-18','19-20']
mark_en_changes = [
 "16: 기존 EN 1번(돌 굴러감)과 EN 2번 전반부(무덤 진입·흰옷 청년)를 MSG 문단(4-5)에 맞춰 하나의 문단으로 합침; '(an angel)' 삽입 해석 제거",
 "16: 기존 EN 2번 후반부 천사 발언에 MSG 'Jesus of Nazareth' 명칭 복원",
 "16: 기존 EN 4번(8절 반복 + 사본 주석 문단) 삭제 — 8절 중복 서술 제거, MSG의 대괄호 주석은 9-11 문단 앞 안내와 19-20 문단 끝 주석으로 MSG 위치에 배치",
 "16: 기존 EN 5번(9-16절 요약 문단) 삭제 — '의도적 요약' 금지 원칙 위반. MSG 9-11(막달라 마리아 발현·일곱 귀신·통곡하는 동료들·불신), 12-13(시골길 두 제자·다른 모습·불신), 14-16(열한 제자·책망·선교 명령) 전문 복원",
 "16: 기존 EN 6번 선교 명령을 MSG 위치(14-16) 문단으로 이동",
 "16: §헤더 '§The Resurrection' 추가(MSG '### The Resurrection' 구획)",
]
mark_ko_paras = [
"§그분은 다시 살아나셨다",
"""안식일이 끝나고, 막달라 마리아, 야고보 엄마 마리아, 그리고 살로메가 예수님 몸에 발라드릴 향료를 샀어. 그리고 일요일 완전 이른 새벽, 해가 막 뜰 때쯤 무덤으로 갔지. 가면서 "아, 그 큰 돌을 누가 굴려주지?" 하고 자기들끼리 걱정했대.""",
"""근데 딱 고개를 들어보니까, 그 완전 큰 돌이 이미 굴려져 있는 거야. 그래서 바로 안으로 들어갔는데, 웬 젊은 사람이 흰 옷을 입고 오른쪽에 앉아 있는 게 보였어. 완전 깜놀해서 어쩔 줄 몰라 했지.""",
"""그 사람이 말했어. "무서워하지 마세요. 너희가 십자가에 못 박히셨던 나사렛 예수님 찾는 거 다 알아. 근데 그분 다시 살아나셨음. 여기 안 계셔. 봐봐, 이 자리 비었잖아. 자, 이제 빨리 가서 제자들이랑 베드로한테 전해. 예수님이 너희보다 먼저 갈릴리로 가신다고. 전에 말씀하셨던 그대로 거기서 예수님을 만날 거라고 말이야.\"""",
"""여자들은 완전 멘붕 상태로 무덤에서 뛰쳐나왔어. 너무 정신없고 놀라서 아무한테도 말을 못 할 정도였대.""",
"""[알려줄게: 마가복음 제일 오래된 사본들은 8절에서 끝나. 9~20절은 나중 사본에 추가된 '긴 결말'이야. 내용은 이래:] 예수님이 부활하신 후, 일요일 아침 일찍 막달라 마리아한테 처음 나타나셨어. 이 마리아가 바로 예수님이 전에 일곱 귀신 쫓아내준 그 사람이거든. 마리아는 예수님 따르던 사람들이 슬퍼서 울고 있는 곳으로 달려가서 이 소식을 전했지. 근데 사람들은 마리아가 진짜 살아있는 예수님을 봤다는 말을 믿지 않았어.""",
"""그 후에 제자 중 두 명이 시골길을 걷고 있었는데, 예수님이 완전 다른 모습으로 그들 앞에 나타나셨어. 이 두 사람이 돌아가서 나머지 제자들한테 말해줬는데, 역시나 아무도 안 믿었대.""",
"""그러고 나서, 11명의 제자들이 저녁 먹고 있는데 예수님이 딱 나타나셨어. 그리고는 부활하신 예수님을 본 사람들의 말을 안 믿은 제자들을 엄청나게 혼내셨지. "여러분은 진짜 믿음이 없군요!" 하시면서. 그리고 말씀하셨어요. "이제 세상으로 나가세요. 어디를 가든지 모든 사람에게 이 기쁜 소식, 바로 하나님의 메시지를 전파하세요. 이것을 믿고 세례받는 사람은 구원받을 것이고, 안 믿는 사람은 심판받을 거예요.\"""",
""""믿는 사람들에게는 이런 대단한 일들이 일어날 거예요. 내 이름으로 귀신을 쫓아내고, 새로운 언어로 말하고, 손으로 뱀을 집어도 괜찮고, 독을 마셔도 멀쩡하고, 아픈 사람에게 손을 얹으면 낫게 될 것입니다.\"""",
"""이 말씀을 마치고, 주 예수님은 하늘로 올라가셔서 하나님 옆 영예의 자리에 앉으셨어. 제자들은 사방으로 흩어져서 메시지를 전했지. 주님은 항상 그들과 함께 일하시면서, 확실한 증거들로 그들의 메시지가 찐이라는 걸 보여주셨어. (참고: 마가복음 16장 9~20절 — 대괄호 부분 — 은 제일 오래된 사본들에는 없어.)""",
]
mark_ko_vr = ['1-3','1-3','4-5','6-7','8','9-11','12-13','14-16','17-18','19-20']
mark_ko_changes = [
 "16: KO 5번 배지 '9-13' → MSG 기준 '9-11'로 수정",
 "16: KO 6번 배지 '13-14' → MSG 기준 '12-13'으로 수정",
 "16: KO 7번(14-16) 말풍선 닫는 따옴표 누락 수정; KO 8번(17-18) 여는 따옴표 누락 수정",
 "16: KO 9번 '하나님의 가장 높은 자리' → MSG 'sat down beside God in the place of honor'에 맞춰 '하나님 옆 영예의 자리'로 수정",
 "16: EN과 동일하게 9-11 문단 앞 대괄호 안내 + 19-20 문단 끝 사본 주석 추가(EN/KO parity)",
 "16: KO 0번 §헤더는 기존 유지, null 배지 → 뒤따르는 본문과 같은 '1-3' 부여",
]

save('en_Mark.json', {
 "chapter": 16, "title": "The Empty Tomb and the Ultimate Comeback",
 "paragraphs": mark_en_paras, "verseRanges": mark_en_vr, "msg_ranges": mark_en_vr,
 "merges": [], "splits": [], "changes": mark_en_changes, "confirmations_needed": [],
})
save('ko_Mark.json', {
 "chapter": 16, "title": "",
 "paragraphs": mark_ko_paras, "verseRanges": mark_ko_vr, "msg_ranges": mark_ko_vr,
 "merges": [], "splits": [], "changes": mark_ko_changes, "confirmations_needed": [],
})
print('Mark done:', len(mark_en_paras), len(mark_ko_paras))

exec(open('/home/hatch/workspace/teenz-bible-review/work3/build_luke.py').read())
exec(open('/home/hatch/workspace/teenz-bible-review/work3/build_john.py').read())
