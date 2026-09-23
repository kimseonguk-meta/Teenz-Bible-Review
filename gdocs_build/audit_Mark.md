# Teenz Bible 의미 감사 리포트 — 마가복음 (Mark)

- 감사일: 2026-09-22
- 감사 범위: 마가복음 1~16장 전 장, § 헤더 제외 본문 문단 전수
- 기준: MSG(The Message, Eugene Peterson) → Teen EN (의미 요소 축약/생략 금지) → Teen KO (EN의 1:1 번역)
- 방법: `gdocs_build/build_gdocs.py`의 `parse_msg_txt()` + `match_msg_for_teen()` 매칭을 그대로 사용해 MSG–Teen 문단 pairing 후 대조. 1~2장은 직접 감사, 3~16장은 동일 기준의 분할 감사 후 핵심 이슈(특히 [중요])를 원문/소스 JSON에서 직접 재검증.
- **소스 JSON 수정 없음 (감사 리포트만 작성)**

## 정정 사항 (중요)

감사 과정에서 내가 보고했던 "막 2:23-24 KO 깨진 문자(U+FFFD)"는 **오보**다. 터미널 출력 렌더링 아티팩트였고, `ko_Mark.json`을 코드포인트 단위로 전수 검사한 결과 깨진 문자는 0건이며 해당 구절은 정상 바이트("당신 제자들이")임을 확인했다. EN/KO 전 파일 U+FFFD 검사 결과도 0건이다.

## 요약

| 장 | [중요] | [경미] | [정보] | 비고 |
|---|---|---|---|---|
| 1 | 0 | 2 | 1 | |
| 2 | 0 | 2 | 0 | |
| 3 | 1 | 6 | 1 | [중요] 1건 = 3:28-30 성령 모독 경고 요약 |
| 4 | 0 | 5 | 2 | |
| 5 | 0 | 5 | 2 | |
| 6 | 0 | 0 | 1(괄호 5개 묶음) | 의미 손실 없음 |
| 7 | 0 | 1 | 3 | |
| 8 | 0 | 3 | 0 | |
| 9 | 0 | 2 | 0 | |
| 10 | 0 | 0 | 0 | 이슈 없음 |
| 11 | 0 | 0 | 0 | 이슈 없음 (v26은 MSG 원문에 없음) |
| 12 | 0 | 5 | 3 | |
| 13 | 0 | 3 | 1 | |
| 14 | 0 | 12 | 1 | 이슈 최다 |
| 15 | 0 | 4 | 1 | |
| 16 | 0 | 2 | 1 | |
| **합계** | **1** | **52** | **17** | |

---

## [중요] 1건

### 막 3:28-30 — 성령 모독 경고의 핵심 설명(3중 비유)과 경고 이유 통째 누락

- MSG 원문: `"Listen to this carefully. I'm warning you. There's nothing done or said that can't be forgiven. But if you persist in your slanders against God's Holy Spirit, you are repudiating the very One who forgives, sawing off the branch on which you're sitting, severing by your own perversity all connection with the One who forgives." He gave this warning because they were accusing him of being in league with Evil.`
- 현행 Teen EN: `Then he gave them a hardcore warning: "You can be forgiven for almost any sin or trash-talk. But if you deliberately trash-talk the Holy Spirit and call the work of God the work of the devil, that is unforgivable. You carry that guilt forever."`
- 현행 Teen KO: `"잘 들어보세요. 제가 경고하는데, 용서 못 받을 말이나 행동은 없어요. 근데 여러분이 성령을 끝까지 욕하면, 그건 여러분을 용서해주는 바로 그분을 거부하는 거예요. 그건 자기가 앉은 나뭇가지를 톱으로 자르는 거랑 똑같아요. 용서해주는 분과의 모든 관계를 스스로 끊어버리는 짓이라고요." 예수님이 이렇게까지 경고하신 건, 그 사람들이 예수님을 악마랑 한패라고 몰아갔기 때문이에요.`
- 문제: EN이 '왜 용서받지 못하는지'를 설명하는 MSG의 3중 비유(용서하시는 바로 그분을 거부함 / 자기가 앉은 나뭇가지를 톱으로 자름 / 용서하시는 분과의 모든 연결을 스스로 끊음)를 전부 삭제하고 결론("unforgivable… carry that guilt forever")만 남김 — 의도적 요약에 해당. "He gave this warning because they were accusing him of being in league with Evil"(경고 이유) 문장도 EN에 없음. KO는 둘 다 살려 EN과 실질 불일치. 참고로 EN의 "and call the work of God the work of the devil"은 MSG에 없는 EN의 해석적 추가.
- 수정 방향: EN에 3중 비유와 경고 이유 문장을 teen-friendly한 표현으로 복원하고 KO와 일치시킬 것.

---

## 장별 이슈

### 1장 — 경미 2, 정보 1

**1-1. [경미] 막 1:7-8 — EN에서 MSG "will change your life" 누락 (KO는 있음)**
- MSG: `"The real action comes next: The star in this drama, to whom I'm a mere stagehand, will change your life. I'm baptizing you here in the river, turning your old life in for a kingdom life. His baptism—a holy baptism by the Holy Spirit—will change you from the inside out."`
- EN: `John preached, "The real action comes next. The one coming after me is way stronger than I am. I'm not even worthy to bend down and untie his sandals. I baptize you with water, but he will baptize you with the Holy Spirit."`
- 문제: "will change your life"(다가오는 분이 삶을 바꾸신다는 약속)가 EN에 없음. KO("이 드라마의 주인공은 여러분의 삶을 완전히 바꿔놓으실 분이에요")에는 있어 EN/KO 불일치. 또한 EN의 "from the inside out"도 빠져 KO만 "찐으로 변화시킬 거예요"로 살림.
- 수정 방향: EN에 "will change your life" / "from the inside out" 뉘앙스 복원.

**1-2. [정보] 막 1:7-8 — EN에 MSG에 없는 타 복음서 이미지 추가**
- EN: `"I'm not even worthy to bend down and untie his sandals."`
- 문제: "샌들 끈을 풀 자격도 없다"는 마가복음 MSG에 없는 다른 복음서(요한복음 계열) 이미지의 유입. 의미상 틀리진 않으나 MSG 기준 원칙상 외부 추가.
- 수정 방향: 유지 여부 정책 판단 (유지 시 주석 권장).

**1-3. [경미] 막 1:40-42 — EN에서 "his skin smooth and healthy" 누락, KO는 없는 비유 추가**
- MSG: `Then and there the leprosy was gone, his skin smooth and healthy.`
- EN: `Instantly, the leprosy vanished.`
- KO: `그러자 바로 나병이 싹 나았고, 그의 피부는 아기 피부처럼 부드러워졌어요.`
- 문제: EN이 "피부가 매끄럽고 건강해졌다"를 빠뜨림. KO는 살렸으나 "아기 피부처럼"이라는 MSG/EN에 없는 비유를 추가 — KO 불일치.
- 수정 방향: EN에 "his skin smooth and healthy" 복원, KO의 "아기 피부처럼"은 삭제하고 EN에 맞춤.

### 2장 — 경미 2

**2-1. [경미] 막 2:1-2 — EN에서 "He was teaching the Word" 누락 (KO는 있음)**
- MSG: `A crowd gathered, jamming the entrance so no one could get in or out. He was teaching the Word.`
- EN: `A few days later, Jesus was back in Capernaum. Word got out, and the house he was in got packed so tight nobody could even get through the front door.`
- KO: `집에 계신다는 소문이 쫙 퍼져서, 사람들이 문 앞까지 꽉 차서 아무도 들어갈 수가 없었어요. 예수님은 말씀을 가르치고 계셨고요.`
- 문제: "He was teaching the Word"(말씀을 가르치심)가 EN에 없음. KO는 있어 불일치.
- 수정 방향: EN에 "He was teaching the Word" 복원.

**2-2. [경미] 막 2:15-16 — EN에서 "had become followers" 누락 (KO는 있음)**
- MSG: `Later Jesus and his disciples were at home having supper with a collection of disreputable guests. Unlikely as it seems, more than a few of them had become followers.`
- EN: `Levi threw a massive dinner party at his house with Jesus, his disciples, and a ton of other shady tax collectors and "sinners." The religious leaders saw this and asked his disciples, "Why does he eat with outcasts?"`
- KO: `나중에 예수님이랑 제자들이 집에서 저녁을 먹는데, 세리들이랑 죄인이라고 손가락질받던 사람들이 많이 있었어요. 사실 그중에는 예수님을 따르는 사람들도 꽤 있었거든요.`
- 문제: "그들 중 꽤 여러 명이 이미 제자가 되어 있었다"는 MSG 의미가 EN에 없음. KO는 살려 불일치. (EN의 "at Levi's house" 특정은 MSG의 모호한 "at home"에 대한 해석적 추가이나 문맥상 용인 가능.)
- 수정 방향: EN에 "quite a few of them had already become his followers" 뉘앙스 복원.

### 3장 — 중요 1, 경미 6, 정보 1

**3-1. [경미] 막 3:1-2 — EN이 "체포하려"로 격상, KO와 불일치**
- MSG: `The Pharisees had their eyes on Jesus to see if he would heal him, hoping to catch him in a Sabbath violation.`
- EN: `...waiting to see if he would heal the guy on the Sabbath so they could arrest him.`
- KO: `안식일 어긴다고 시비 걸려고 말이에요.`
- 문제: MSG의 "안식일 위반으로 걸리게 하려는 의도"가 EN에서 "체포하려"로 격상. KO는 MSG에 가까워 불일치.
- 수정 방향: EN을 "so they could accuse him of breaking the Sabbath" 수준으로 되돌릴 것.

**3-2. [경미] 막 3:3-4 — 질문 대상이 "무리"에서 "지도자들"로 변경**
- MSG: `Then he spoke to the people: "What kind of action suits the Sabbath best? ..."`
- EN: `Then Jesus asked the leaders, "Is it legal to do good on the Sabbath, or to do evil? ..."`
- KO: `그러고 나서 사람들에게 물으셨어요.`
- 문제: MSG는 무리(the people)에게 말했는데 EN은 지도자들(the leaders)로 대상 변경. KO는 MSG를 따라 불일치.
- 수정 방향: EN의 "asked the leaders"를 "asked the people"로 수정.

**3-3. [경미] 막 3:5 — EN에 "deeply heartbroken" 추가, "one after another" 누락**
- MSG: `He looked them in the eye, one after another, angry now, furious at their hard-nosed religion.`
- EN: `Jesus looked around at them, absolutely furious and deeply heartbroken by how stubborn and cold they were.`
- KO: `예수님은 그 사람들이 인정머리 없는 거에 완전 화가 나서, 한 명씩 쫙 째려보셨어요.`
- 문제: EN이 MSG에 없는 감정 "deeply heartbroken"을 추가했고 "one after another"(한 명씩)는 사라짐. KO는 MSG를 살려 불일치.
- 수정 방향: EN에서 "deeply heartbroken" 삭제, "looked them in the eye, one after another" 뉘앙스 복원.

**3-4. [경미] 막 3:6 — "Herod's followers"가 EN에서 "corrupt politicians"로 대체**
- MSG: `...how they would join forces with Herod's followers and ruin him.`
- EN: `...held a secret meeting with corrupt politicians to figure out how to assassinate Jesus.`
- KO: `헤롯당 사람들이랑 ... 작당모의를 시작했대요.`
- 문제: 구체적 집단 "Herod's followers"가 일반명사 "corrupt politicians"로 대체되어 누구인지 식별 불가 + "corrupt" 평가적 형용사 추가. KO는 MSG를 살려 불일치.
- 수정 방향: EN을 "Herod's followers" 계열 표현으로 되돌릴 것.

**3-5. [경미] 막 3:7-10 — EN에서 개시 행위("제자들과 바다로 피하심") 누락**
- MSG: `Jesus went off with his disciples to the sea to get away. But a huge crowd from Galilee trailed after them...`
- EN: `The crowds following Jesus were getting dangerously huge. People from Galilee, Judea, Jerusalem... came to see for themselves. ...`
- KO: `예수님은 거기를 피해서 제자들이랑 바닷가로 가셨어요. 근데 갈릴리에서 또 엄청난 사람들이 따라왔고...`
- 문제: EN에 "제자들과 함께 바다로 피했다"는 개시 행위가 없고 군중 묘사부터 시작. KO는 포함되어 불일치.
- 수정 방향: EN 첫머리에 "Jesus went off with his disciples to the sea to get away" 의미 복원.

**3-6. [정보] 막 3:13-19 — EN에서 "later" 누락 (KO는 있음)**
- MSG: `Simon (Jesus later named him Peter, meaning "Rock"),`
- EN: `Simon—Jesus named him Peter, meaning "Rock";` / KO: `시몬 (나중에 예수님이 '바위'라는 뜻으로 베드로라는 이름을 지어주심)`
- 수정 방향: EN에 "later" 삽입.

**3-7. [경미] 막 3:22 — EN에 MSG에 없는 "Beelzebul (Satan)" 추가, "impress them" 동기 누락**
- MSG: `...spreading rumors that he was working black magic, using devil tricks to impress them with spiritual power.`
- EN: `"He's possessed by Beelzebul (Satan). He's only kicking out demons because he's getting his power from the boss of the demons."`
- 문제: (1) MSG에 없는 고유명 "Beelzebul (Satan)" 추가 (배경지식 기반). (2) MSG의 "to impress them with spiritual power"는 EN/KO 모두에서 사라짐.
- 수정 방향: "Beelzebul" 유지 여부는 정책 판단. "to impress them with spiritual power" 의미는 EN에 복원 검토.

**3-8. [중요]** — 본 리포트 상단 [중요] 섹션 참조 (막 3:28-30).

### 4장 — 경미 5, 정보 2

**4-1. [경미] 막 4:3 — "What do you make of this?" EN/KO 모두 누락**
- MSG: `"Listen. What do you make of this? A farmer planted seed."`
- EN: `"Listen up! A farmer went out to plant seeds."` / KO: `"자, 들어보세요. 어떤 농부가 씨를 뿌리러 나갔어요."`
- 문제: 해석 유도 질문 "What do you make of this?"가 양쪽 모두에서 사라짐.
- 수정 방향: EN/KO에 "What do you make of this?" 계열 문장 복원.

**4-2. [경미] 막 4:13 — EN이 MSG 문장을 다른 문장으로 교체 (KO는 MSG 유지)**
- MSG: `"Do you see how this story works? All my stories work this way."`
- EN: `"Do you get how this story works? Because if you don't get this one, how are you going to understand any of the others?"`
- KO: `"이 이야기가 무슨 뜻인지 아시겠어요? 제가 하는 모든 이야기가 다 이런 식이에요."`
- 문제: EN이 MSG의 "All my stories work this way"를 MSG에 없는 다른 문장으로 교체. KO는 MSG를 따라 불일치.
- 수정 방향: EN을 MSG 기준으로 되돌릴 것.

**4-3. [경미] 막 4:16-17 — "when the emotions wear off" EN 누락, "nothing to show for it" 변경**
- MSG: `...when the emotions wear off and some difficulty arrives, there is nothing to show for it.`
- EN: `...As soon as trouble or pushback comes because of the Word, they bail.`
- KO: `...감정이 식거나 힘든 일이 생기면 바로 나가떨어지는 거죠.`
- 문제: (1) "when the emotions wear off"(감정이 식을 때)가 EN에 없음 (KO는 있음 → 불일치). (2) "there is nothing to show for it"(아무 열매 없음)가 "they bail"(떠남)으로 변경.
- 수정 방향: EN에 "when the emotions wear off" 복원, "nothing to show for it" 의미 반영.

**4-4. [정보] 막 4:20 — EN에 MSG에 없는 "thirty, sixty, a hundred times" 숫자 추가**
- MSG: `"...produce a harvest beyond their wildest dreams."` (숫자 없음, msg_Mark.txt 141행 확인)
- EN: `...produce a harvest way beyond their wildest dreams—thirty, sixty, a hundred times what was planted.`
- 문제: MSG에 없는 구체적 숫자 추가 (배경지식 기반). KO에는 없어 EN/KO 불일치.
- 수정 방향: 추가 유지 여부 정책 판단. 유지 시 KO에도 동일 숫자 반영 필요.

**4-5. [정보] 막 4:35-36 — EN에 MSG에 없는 "left the crowd behind" 추가, 2개 문단 중복**
- MSG: `Late that day he said to them, "Let's go across to the other side." They took him in the boat as he was.`
- EN(p23): `...They left the crowd behind.` / EN(p24): `...leaving the crowd behind.`
- 문제: MSG에 없는 구절이 EN에 추가되어 두 문단에 중복. KO에는 없음.
- 수정 방향: 중복 중 하나 삭제. 추가 유지 여부는 정책 판단.

**4-6. [경미] 막 4:40 — EN에서 "reprimanded"(꾸짖다) 순화, KO는 있음**
- MSG: `Jesus reprimanded the disciples: "Why are you such cowards? ..."`
- EN: `He looked at his crew and said, "Why are you such cowards? ..."`
- KO: `예수님이 제자들을 꾸짖으셨어요.`
- 문제: EN이 "reprimanded"를 "looked at his crew and said"로 순화 → 꾸짖는 어조 소실. KO는 유지되어 불일치.
- 수정 방향: EN에 "reprimanded/scolded" 뉘앙스 복원.

**4-7. [경미] 막 4:41 — "in absolute awe"가 "absolutely terrified of him"으로 감정 전환**
- MSG: `They were in absolute awe, staggered. "Who is this, anyway?" ... "Wind and sea at his beck and call!"`
- EN: `The disciples were absolutely terrified of him. They whispered to each other, "Who is this guy?! ..."`
- KO: `제자들은 완전 놀라서 어쩔 줄 몰라했어요.`
- 문제: MSG의 "in absolute awe"(경외감)가 EN에서 순수 공포로 바뀜. KO는 EN과 다름.
- 수정 방향: EN을 "in awe / amazed and afraid" 계열로 조정.

### 5장 — 경미 5, 정보 2

**5-1. [경미] 막 5:1-5 — EN에 MSG에 없는 "tormented by an evil spirit" 선행 추가**
- MSG: `As Jesus got out of the boat, a madman from the cemetery came up to him.` (8절에서야 "tormenting evil spirit" 등장)
- EN: `...a madman from the cemetery who was tormented by an evil spirit came up to him.`
- 문제: MSG 서사 순서보다 앞서 귀신들림을 단정. KO에는 없어 불일치.
- 수정 방향: 추가 유지 시 KO에도 반영, 삭제 시 EN에서 삭제.

**5-2. [정보] 막 5:9-10 — EN에 MSG에 없는 "There's an entire army of us inside this guy" 추가**
- MSG: `"My name is Mob. I'm a rioting mob."`
- EN: `"My name is Mob—I'm a rioting mob. There's an entire army of us inside this guy."` (KO도 동일 추가 — EN/KO 일치)
- 문제: 'Legion' 배경지식 기반 추가. 의미상 틀리진 않으나 MSG 기준상 추가.
- 수정 방향: 유지 여부 정책 판단.

**5-3. [경미] 막 5:11-13 — KO에 EN에 없는 문장 추가**
- EN: `Jesus gave the order. But it was even worse for the pigs than for the man. ...`
- KO: `예수님이 허락하셨어요. 그러자 귀신들이 그 사람에게서 나와 돼지들 속으로 들어갔어요. 근데 돼지들한테는 그 사람보다 상황이 더 안 좋았어요. ...`
- 문제: KO에 "그러자 귀신들이 그 사람에게서 나와 돼지들 속으로 들어갔어요." 추가 — EN/MSG에 없는 문장(암시된 내용의 명시화). EN/KO 불일치.
- 수정 방향: KO에서 해당 문장 삭제, 또는 EN에도 동일 문장 추가.

**5-4. [경미] 막 5:16-17 — KO에 해설성 추가**
- MSG: `At first they were in awe—and then they were upset, upset over the drowned pigs. They demanded that Jesus leave and not come back.`
- EN: 위 MSG와 동일한 구조로 충실.
- KO: `...근데 사람들 반응이 좀 이상했어요. 처음엔 경외감을 느끼더니, 나중에는 기분 나빠하는 거예요. 왜냐면 자기들 돼지 떼가 몰살당한 것 때문에 화난 거지요. 그래서 예수님한테...`
- 문제: KO에 "근데 사람들 반응이 좀 이상했어요"(평가성 서술), "왜냐면 자기들 돼지 떼가 몰살당한 것 때문에 화난 거지요"(원인 해설) 추가. MSG는 "upset over the drowned pigs"까지만 서술.
- 수정 방향: KO의 해설성 추가 삭제/축소.

**5-5. [정보] 막 5:18-20 — KO에 "(열 개의 도시라는 뜻)" 부연 추가**
- KO: `...예수님이 자기한테 해주신 일을 데가볼리(열 개의 도시라는 뜻) 근처에 다 알리고 다녔어요.`
- 문제: KO에만 부연. 도움은 되나 EN/KO 불일치.
- 수정 방향: 유지 시 EN에도 동일 부연 추가 고려, 또는 용어집으로 이동.

**5-6. [경미] 막 5:25-29 — KO에서 "from behind" 누락, "treated her badly" 축소**
- MSG: `A woman who had suffered a condition of hemorrhaging for twelve years—a long succession of physicians had treated her, and treated her badly, taking all her money and leaving her worse off than before—... She slipped in from behind and touched his robe.`
- EN: MSG 구조 그대로 충실 (12년, 여러 의사, 잘못된 치료, 뒤에서 슬쩍).
- KO: `거기 12년 동안 혈루증으로 몹시 고생한 한 여자가 있었는데... 이 여자는 의사들한테 돈만 엄청 쓰고, 몸은 더 나빠졌었어요. 여자가 사람들 사이에 슬쩍 껴서 예수님 옷을 만졌어요.`
- 문제: KO에서 (1) "from behind"(뒤에서) 누락 → "사람들 사이에 슬쩍 껴서"로 변경. (2) "treated her badly"(잘못된 치료)가 "돈만 엄청 쓰고"로 축소. (3) "a long succession of physicians"가 "의사들한테"로 축소.
- 수정 방향: KO에 "뒤에서" 복원, "여러 의사에게 잘못된 치료를 받고" 뉘앙스 보강.

**5-7. [경미] 막 5:37-40 — KO에서 "neighbors bringing in casseroles" 디테일 누락**
- MSG: `They entered the leader's house and pushed their way through the gossips looking for a story and neighbors bringing in casseroles.`
- EN: MSG 그대로 충실.
- KO: `회당장 집에 들어가니까, 구경하러 온 수다쟁이들과 이웃들이 와서 막 시끄럽게 울고불고 하고 있었어요.`
- 문제: KO에서 MSG 특유의 디테일 "neighbors bringing in casseroles"(음식을 가져오는 이웃들)와 "pushed their way through"(헤치고 들어감)가 사라지고 "시끄럽게 울고불고"로 대체.
- 수정 방향: KO에 "이웃들이 음식을 가져오고" 디테일 복원.

### 6장 — 이슈 없음 ([정보] 설명성 괄호 5개)

전 본문(vr 1–56) 감사 완료. MSG 의미 요소(사실관계, 인명, 인용문, 인과·조건 논리, 명령, 숫자)가 EN·KO에 모두 보존됨. [중요]/[경미] 0건.
- [정보] MSG에 없는 설명성 괄호 5개 (의미 변경 없음, 수정 불필요): "his crew (disciples)", "the synagogue (their meeting place for worship and teaching)", "(demons and spiritual forces)", "anointing their bodies with oil (a traditional practice for healing)", "spend a fortune (a huge amount of money)".

### 7장 — 경미 1, 정보 3

**7-1. [경미] 막 7:29-30 — KO "impressed" → "감동받으셨어요" 뉘앙스 이동**
- MSG: `Jesus was impressed. 'You're right! On your way!'`
- EN: `Jesus was really impressed. 'You're right! Go on home! ...'`
- KO: `예수님은 정말 감동받으셨어요.`
- 문제: "impressed"(감탄/인상 깊다)가 KO에서 "감동받으셨어요"(마음이 움직이다)로 이동.
- 수정 방향: "예수님은 정말 감탄하셨어요"로 조정.
- 참고: 7:16은 MSG 원문 자체에 없음 (누락 아님).

**7-2. [정보]** 막 7:9-13 고르반 제도 설명 괄호 추가 (`(This was a way to dedicate money or property to God...)`) — 내용 정확, 유지 가능하나 원문 충실 원칙상 각주 분리 검토.
**7-3. [정보]** 막 7:24-26 — EN이 MSG의 "disturbed daughter"를 "struggling with a demon"으로 서사 순서보다 앞서 단정 (v29에서야 귀신들림을 밝힘). 모순은 아니나 해석 선행.
**7-4. [정보]** 막 7:24-26 — EN에 "(a Gentile, not Jewish)" 부연 추가. 내용 정확.

### 8장 — 경미 3

**8-1. [경미] 막 8:1-3 — "breaking my heart"(연민) 뉘앙스 약화**
- MSG: `'This crowd is breaking my heart. They have stuck with me for three days, and now they have nothing to eat.'`
- EN: `'This crowd is really getting to me. They've been hanging out with me for three days straight, ...'`
- KO: `아, 이 사람들 보니까 마음이 좀 그렇습니다.`
- 문제: MSG의 강한 연민 표현이 EN "really getting to me"(짜증으로도 읽힘), KO "마음이 좀 그렇습니다"(모호)로 약화.
- 수정 방향: EN은 "I feel so bad for these people" 계열, KO는 "이 사람들이 너무 안쓰러워요" 계열로 조정.

**8-2. [경미] 막 8:13-15 — KO에서 "contaminating" 뉘앙스 약화**
- MSG/EN: `Keep a sharp eye out for the contaminating yeast of the Pharisees and Herod's followers.`
- KO: `바리새인이랑 헤롯 당원들의 이상한 가르침(누룩) 진짜 조심해야 합니다.`
- 문제: "contaminating(오염시키는)"이 "이상한"으로 약화. (섹션 헤더 "오염시키는 누룩"에는 보존됨.)
- 수정 방향: KO를 "오염시키는 누룩(잘못된 가르침)" 계열로 조정.

**8-3. [경미] 막 8:30-32 — KO에서 "found guilty" 누락**
- MSG/EN: `...be tried and found guilty by the elders, high priests, and religion scholars. ...`
- KO: `장로랑 대제사장이랑 종교 학자들한테 재판받고 죽게 될 거예요.`
- 문제: "found guilty(유죄 판결)" 요소가 KO에 명시되지 않음.
- 수정 방향: KO를 "재판받고 유죄 판결을 받고" 계열로 보완.

### 9장 — 경미 2

**9-1. [경미] 막 9:43-48 — KO에서 EN의 "godless" 삭제**
- MSG: `...godless in a furnace of eternal fire.`
- EN: `...ending up godless in a furnace of eternal fire.`
- KO: `두 손 두 발 멀쩡히 가지고 영원히 불타는 불구덩이에 있는 것보다 훨씬 나아요.`
- 문제: "godless"(하나님 없는 상태) 수식어가 KO에 없음.
- 수정 방향: "하나님 없이 영원히 불타는 불구덩이에" 식으로 복원.

**9-2. [경미] 막 9:49-50 — KO 따옴표 불균형 (소스 JSON 직접 확인)**
- KO: `곧 모든 사람이 불로 단련되는 과정을 거치겠지만, ... 평화를 지키는 사람이 되세요."` — 닫는 `"`만 있고 여는 `"` 없음.
- 문제: 의미 손실은 없으나 텍스트 결함.
- 수정 방향: 문단 맨 앞에 여는 따옴표 `"` 추가.

### 10장 — 이슈 없음

v1–52 전 절 감사 완료. 이혼 질문, 어린아이 축복, 부자 청년, 세 번째 수난 예고, 야고보·요한의 요청, 바디매오 등 전 문단 EN/MSG 의미 보존, KO/EN 동등.

### 11장 — 이슈 없음

v1–25, v27–33 감사 완료 (v26은 MSG 원문 자체에 없음 — 누락 아님). 나귀 새끼, 호산나, 무화과나무, 성전 정화, 권위 논쟁 등 전 문단 이상 없음.

### 12장 — 경미 5, 정보 3

**12-1. [경미] 막 12:3-5 — KO에 MSG/EN에 없는 "주인이 화가 나서" 추가 (소스 확인)**
- MSG: `They grabbed him, beat him up, and sent him off empty-handed. So he sent another servant.`
- EN: `...So the owner sent another servant.`
- KO: `...빈손으로 쫓아낸 거야. 주인이 화가 나서 다른 종을 보냈더니...`
- 문제: MSG/EN에 없는 주인의 감정 묘사 추가.
- 수정 방향: "주인이 화가 나서" 삭제하고 EN대로 "그래서 주인이 다른 종을 보냈더니"로 수정.

**12-2. [경미] 막 12:30 — KO의 4중 사랑 표현이 EN과 다름**
- EN: `...love the Lord God with absolutely everything you've got—all your passion, all your prayer, all your intelligence, and all your energy.`
- KO: `네 마음과 영혼과 생각과 힘을 다해서 주 너의 하나님을 사랑하세요.`
- 문제: 의미(온전한 헌신)는 동등하나 KO가 EN의 4중 표현을 번역하지 않고 기존 한국어 성경식 표현(마음/영혼/생각/힘)으로 대체 — EN primary 원칙 위반.
- 수정 방향: "네 열정과 기도와 지성과 힘을 다해서" 식으로 EN의 4개 항목을 그대로 옮길 것.

**12-3. [경미] 막 12:32-33 — 12-2와 동일 패턴**
- EN: `And loving him with all your passion, intelligence, and energy...`
- KO: `그리고 마음과 지혜와 힘을 다해서 하나님을 사랑하고...`
- 수정 방향: "너의 열정과 지성과 힘을 다해서" 식으로 통일.

**12-4. [경미] 막 12:38-40 — KO에 MSG/EN에 없는 구체 표현 2건 추가**
- MSG/EN: `soaking up all the public praise ... taking advantage of people who are weak and helpless.`
- KO: `시장에서 인사받는 것을 아주 좋아하고, ... 힘없는 과부들의 재산을 낼름 집어삼키고...`
- 문제: (1) "시장에서" — MSG/EN에 없는 장소 특정 (개역식 "시장에서 문안" 회귀). (2) "과부들의 재산" — MSG/EN의 "the weak and helpless"를 "과부들"로 좁힘.
- 수정 방향: EN 기준으로 "사람들한테 칭찬받는 것을", "약하고 힘없는 사람들을 이용해 먹으면서"로 수정.

**12-5. [경미] 막 12:37 — KO 문단 끝 stray 닫는 `"` (소스 확인)**
- KO: `다윗이 메시아를 '내 주님'이라고 부르는데, 어떻게 메시아가 다윗의 '자손'이 될 수 있겠어요?"` — 여는 `"` 없이 닫는 `"` 하나가 문단 끝에 붙어 있음.
- 수정 방향: 문단 끝의 stray `"` 삭제.

**12-6. [정보]** 막 12:19-23 — EN에 MSG에 없는 부연 "to continue the family name" 추가 (KO는 "형의 대를 이어줘야"로 병행 — KO/EN은 일치). 엄격한 MSG 기준 적용 시 삭제 검토.
**12-7. [정보]** 막 12:9-11 — "read it in Scripture" 문장이 EN p5 끝 → KO p6 앞으로 이동·재구성. 내용 손실은 없으나 문단 경계 이동.
**12-8. [정보]** 막 12:1-8 — 포도밭 비유 KO 따옴표가 p1에서 열려 p4에서 닫힘 (EN은 문단별 개폐). 전체 균형은 맞으나 스타일 불일치.

### 13장 — 경미 3, 정보 1

**13-1. [경미] 막 13:5 — KO가 따옴표 안에 해설 괄호 추가**
- EN: `...claiming, 'I'm the One.' They'll fool a ton of people.`
- KO: `'내가 그 사람이야'(즉, '내가 메시아다' 또는 '내가 선택받은 지도자다'라는 뜻)라고 주장할 거야`
- 문제: EN/MSG에 없는 해설 괄호가 KO에만 추가. KO/EN 불일치.
- 수정 방향: 괄호 해설 삭제하고 EN 그대로 번역.

**13-2. [경미] 막 13:14 — KO가 '더럽게 만드는 괴물'에 해설 괄호 추가**
- EN: `...when you see 'the monster of desecration' set up where it should never be...`
- KO: `'더럽게 만드는 괴물'(끔찍하고 거룩하지 않은 것)이 있어서는 안 될 곳에...`
- 문제: EN/MSG에 없는 `(끔찍하고 거룩하지 않은 것)`이 KO에만 추가.
- 수정 방향: 괄호 삭제하고 EN 그대로 번역.

**13-3. [경미] 막 13:3-4 — KO가 "coming to a head"를 "끝장나는"으로 뉘앙스 이동**
- EN: `...What kind of sign should we look for that things are totally coming to a head?`
- KO: `모든 일이 완전히 끝장나는 징조는 어떤 걸까요?`
- 문제: "coming to a head"(절정에 이름)가 "끝장나는"(파멸/종결)으로 이동.
- 수정 방향: `모든 일이 절정에 이르는 징조` 등으로 수정.

**13-4. [정보]** 막 13:19-20 — EN이 MSG "intervened"를 "to shorten that time"으로 구체화. 앞 문맥상 논리적 의미와 부합하고 KO도 EN을 따르므로 의미 오류는 아니나 MSG 기준으로는 추가 설명. 현행 유지 가능.

### 14장 — 경미 12, 정보 1 (이슈 최다)

**14-1. [경미] 막 14:3-5 — KO "열다" → "깨다" 변경**
- MSG/EN: `Opening the bottle, she poured it on his head.` / `She opened it up and poured it right on his head!`
- KO: `병을 깨서 예수님 머리에 부어버리는 거임.`
- 문제: "열다"가 "깨다(부수다)"로 변경. KO/EN 불일치.
- 수정 방향: `병을 열어서`로 수정.

**14-2. [경미] 막 14:5 — KO에 없는 행동 뉘앙스 "한마디 할 기세" 추가**
- EN: `They were absolutely fuming, practically exploding with anger over what she did.`
- KO: `완전 화가 나서 그 여자한테 한마디 할 기세였지.`
- 문제: 감정 묘사(분노 폭발)가 KO에서 행동(여자에게 말을 걸려는 기세)으로 뉘앙스 추가.
- 수정 방향: `완전 화가 나서 폭발할 것 같았지` 등으로 감정 묘사에 맞춤.

**14-3. [경미] 막 14:8-9 — KO에서 "when she could" 누락 + "최선"으로 강화**
- MSG/EN: `She did what she could when she could—she pre-anointed my body for burial.`
- KO: `이 여자는 자기가 할 수 있는 최선을 다한 거예요.`
- 문제: "when she could"(타이밍 요소) 누락, "did what she could"가 "최선을 다했다"로 강화.
- 수정 방향: `이 여자는 할 수 있을 때 할 수 있는 걸 다 한 거예요`로 수정.

**14-4. [경미] 막 14:17-18 — KO에서 "hand me over" 요소 누락**
- EN: `One of you is going to hand me over to the people who want to hurt me, one who is eating with me right now.`
- KO: `지금 저랑 같이 밥 먹는 여러분 중 한 명이 저를 배신할 거예요.`
- 문제: "hand me over"(넘긴다) 행위 요소가 단순 "배신"으로 축소.
- 수정 방향: `저를 팔아넘길 거예요` 등으로 수정.

**14-5. [경미] 막 14:21 — KO에 예수님 말씀에 없는 문장 추가**
- EN: `"But in another way, the guy who turns him in, who betrays the Son of Man—it would be better for him if he had never even been born!"`
- KO: `"그런데 인자를 팔아넘기는 그 사람은, 차라리 태어나지 않는 게 나았을 거예요. 정말 불쌍한 사람이지요.`
- 문제: `정말 불쌍한 사람이지요.`는 MSG/EN에 없는 KO 추가 문장 (예수님의 직접 말씀에 삽입).
- 수정 방향: 마지막 문장 삭제.

**14-6. [경미] 막 14:29 — KO "ashamed of you" → "주님 버려도" 의미 이동**
- EN: `"Even if everyone else is ashamed of you when things go completely wrong, I won't be!"`
- KO: `"다른 애들 다 멘탈 나가서 주님 버려도, 저는 절대 안 그럴 겁니다."`
- 문제: "ashamed of you"(부끄러워하다)가 "주님 버리다"(포기/배신)로 이동. 부끄러워함 ≠ 버림.
- 수정 방향: `"다른 애들 다 날 부끄러워해도, 저는 절대 안 그럴 겁니다"`로 수정.

**14-7. [경미] 막 14:35-36 — KO에 겟세마네 기도에 없는 문장 추가**
- EN: `"Papa, Father, you can—can't you?—get me out of this. Take this cup away from me. But please, don't do what I want—do what you want."`
- KO: `...그런데 제 뜻대로 하지 마시고, 아빠 뜻대로 해주세요. 아빠가 원하시는 게 뭐예요?"`
- 문제: `아빠가 원하시는 게 뭐예요?`는 MSG/EN 기도에 없는 KO 추가 문장 (예수님의 기도에 없는 말 삽입).
- 수정 방향: 마지막 문장 삭제.

**14-8. [경미] 막 14:37-38 — KO에 베드로 책망에 없는 문장 추가**
- EN: `"Simon, you went to sleep on me? Can't you stay awake with me for just one hour?"`
- KO: `"시몬, 자고 있나요? 어떻게 저에게 이럴 수 있어요? 한 시간도 못 버티겠어요?`
- 문제: `어떻게 저에게 이럴 수 있어요?`는 MSG/EN에 없는 KO 추가 문장.
- 수정 방향: 해당 문장 삭제하고 EN 문장 구조에 맞춤.

**14-9. [경미] 막 14:38 — KO에서 "Don't be naive" 경고 누락 + 두 부분 대조 뭉뚱그림**
- MSG: `"Stay alert, be in prayer, so you don't enter the danger zone without even knowing it. Don't be naive. Part of you is eager, ready for anything in God; but another part is as lazy as an old dog sleeping by the fire."`
- EN: MSG 구조 그대로 충실 (`"Stay alert, keep praying, ... Don't be naive. Part of you is super eager, ... but another part is as lazy as an old dog sleeping by the fire."`)
- KO: `"깨어서 기도하세요. 그래야 유혹에 안 빠지지요. 마음은 불타는데 몸이 안 따라주는군요."`
- 문제: (1) "Don't be naive." 경고 누락. (2) "eager / lazy as an old dog" 두 부분 대조가 한 문장으로 뭉뚱그려짐. (3) "danger zone"이 "유혹"으로 좁혀짐.
- 수정 방향: `"순진하게 굴지 마세요"` 경고 복원, 열심/게으름 두 부분 대조를 살려 번역.

**14-10. [경미] 막 14:43 — KO에서 무리 중 "leaders" 누락**
- MSG/EN: `...a bunch of thugs, sent by the high priests, religion scholars, and leaders, brandishing swords and clubs.`
- KO: `대제사장들이랑 율법학자들이 보낸 깡패들이 칼이랑 몽둥이 들고 같이 있었지.`
- 문제: 세 그룹 중 "지도자들(leaders)"이 KO에 빠짐.
- 수정 방향: `대제사장들이랑 율법학자, 지도자들이 보낸`으로 수정.

**14-11. [경미] 막 14:60-61 — KO가 대제사장 질문에 없는 질문 2개 추가**
- MSG/EN: `...asked Jesus, "What do you have to say to the accusation?" Jesus was silent.` / `"What do you have to say to these accusations?"`
- KO: `"이 사람들 말이 맞나요? 왜 아무 말도 안 하세요?" 예수님은 계속 침묵했음.`
- 문제: KO가 `이 사람들 말이 맞나요?`(사실 확인 질문 추가)와 `왜 아무 말도 안 하세요?`(침묵 이유 추궁 추가)라는 없는 질문 2개를 만듦.
- 수정 방향: `"이 고발들에 대해 할 말 없어요?"` 정도로 EN에 맞춤.

**14-12. [경미] 막 14:64 — KO "condemned" → "죽여야 한다고 외쳤음"으로 장면 변경**
- MSG/EN: `They condemned him, one and all. The sentence: death.`
- KO: `사람들은 다 같이 예수를 죽여야 한다고 외쳤음. 사형 확정.`
- 문제: "condemned"(공회가 정죄/선고함)가 "사람들이 죽여야 한다고 외쳤음"(군중의 외침)으로 바뀜 — 주체(의회→사람들)와 행위(선고→외침) 변경.
- 수정 방향: `그들은 모두 예수를 정죄했음. 사형 선고.`로 수정.

**14-13. [정보]** KO 문체 불일치 + 닫는 따옴표 누락 2건 — 14장 KO는 서술부 반말("~했음") + 대화부 존댓말("~세요") 혼용 (15장은 -어요체 일관, 13장은 -야체 일관). 장별 문체 가이드 필요. 따옴표: ch14 p12 KO(`…'라고 말씀하세요.` 뒤 닫는 큰따옴표 없음), ch14 p33 KO(`…한 시간도 못 버티겠어요?` 뒤 닫는 큰따옴표 없음).

### 15장 — 경미 4, 정보 1

**15-1. [경미] 막 15:2-3 — KO에 "신나서" 감정 추가**
- EN: `Meanwhile, the head priests started throwing a ton of accusations at him, one after another.`
- KO: `그러자 대제사장들은 신나서 막 고발하기 시작했어요.`
- 문제: EN/MSG에 없는 `신나서`(즐거워서) 추가.
- 수정 방향: `신나서` 삭제.

**15-2. [경미] 막 15:25-27 — KO에서 "one to his right, the other to his left" 위치 정보 뭉뚱그림**
- MSG/EN: `Along with him, they crucified two criminals, one to his right, the other to his left.` / `...one on his right side and one on his left.`
- KO: `예수님 양쪽으로는 죄수 두 명도 같이 십자가에 달렸어요.`
- 문제: 좌/우 위치 정보가 "양쪽으로"로 뭉뚱그려짐.
- 수정 방향: `한 명은 오른쪽, 다른 한 명은 왼쪽에`로 수정.

**15-3. [경미] 막 15:29-30 — KO가 조롱 대사에 없는 문장 추가**
- EN: `"Hey, you bragged that you could tear down the Temple and then rebuild it in three days—so prove it! Save yourself! ..."`
- KO: `"성전을 허물고 3일 만에 다시 짓겠다고 잘난 척하더니 그 꼴이 말이 아니네요! 어디 한번 실력 발휘해서...`
- 문제: `그 꼴이 말이 아니네요!`는 MSG/EN 조롱 대사에 없는 KO 추가 문장.
- 수정 방향: 해당 문장 삭제.

**15-4. [경미] 막 15:46-47 — KO "linen shroud" → "깨끗한 천" 변경**
- MSG/EN: `Having already purchased a linen shroud, Joseph took him down, wrapped him in the shroud...` / `Joseph had already bought a linen shroud (a burial cloth). ...`
- KO: `요셉은 미리 사 둔 깨끗한 천으로 예수님을 십자가에서 내려서 잘 쌌어요.`
- 문제: "linen"(아마포, 재질)이 "깨끗한"(청결 상태)으로 변경.
- 수정 방향: `미리 사 둔 아마포 수의로`로 수정.

**15-5. [정보]** 막 15:21 — EN이 MSG "coming from work"를 "working in the fields"로 구체화. KO는 MSG를 따름("일 끝내고") → EN/KO 미세 불일치. 둘 중 하나로 통일.

### 16장 — 경미 2, 정보 1

**16-1. [경미] 막 16:1-3 — EN이 향료 구매 시점을 일요일 새벽으로 변경 (사실관계 변경)**
- MSG 원문 (msg_Mark.txt 793행): `When the Sabbath was over, Mary Magdalene, Mary the mother of James, and Salome bought spices so they could embalm him. Very early on Sunday morning, as the sun rose, they went to the tomb.`
- 현행 Teen EN: `Very early on Sunday morning, Mary Magdalene, Mary the mother of James, and Salome bought spices to anoint Jesus's body. They were walking to the tomb, wondering, "Who is going to help us roll that massive stone away?"`
- 현행 Teen KO: `안식일이 끝나고, 막달라 마리아, 야고보 엄마 마리아, 그리고 살로메가 예수님 몸에 발라드릴 향료를 샀어. 그리고 일요일 완전 이른 새벽, 해가 막 뜰 때쯤 무덤으로 갔지.`
- 문제: MSG는 향료를 "안식일이 끝나고"(토요일 저녁) 샀고 무덤은 "일요일 이른 새벽"에 간 순서인데, EN은 두 사건을 모두 "Very early on Sunday morning"으로 묶어 향료 구매 시점이 변경됨 — 사실관계 변경. KO는 MSG 순서를 정확히 유지 → EN/KO 불일치. [경미]로 분류하나 사실관계 변경이므로 수정 우선순위 높음.
- 수정 방향: EN을 MSG 순서대로 (`After the Sabbath was over, … bought spices … Very early on Sunday morning … they went to the tomb`) 수정하고 KO는 현행 유지.

**16-2. [경미] 막 16:14-16 — KO에 예수님 대사로 없는 인용 추가**
- EN: `...he called them out hard for their stubborn refusal to believe the people who had seen him risen. Then he said, "Go into the entire world and preach the Good News to absolutely everyone. ..."`
- KO: `...부활하신 예수님을 본 사람들의 말을 안 믿은 제자들을 엄청나게 혼내셨지. "여러분은 진짜 믿음이 없군요!" 하시면서. 그리고 말씀하셨어요. ...`
- 문제: `"여러분은 진짜 믿음이 없군요!"`는 MSG/EN에 없는 KO 추가 직접 인용 (예수님의 입에 없는 말 삽입).
- 수정 방향: 해당 인용 삭제하고 "엄청나게 혼내셨지" 서술로 충분.

**16-3. [정보]** 막 16:9-11 — EN이 마가복음 결말(9-20절) 편집자 주를 확장·전면 배치 (`[Heads up: the oldest copies of Mark end at verse 8 — ...]`). KO는 EN을 충실히 따름. 성경 본문 의미 변경은 아니나 편집층 추가이므로 참고용 기록. 현행 유지 가능.

---

## 반복 패턴 (수정 작업 시 참고)

1. **"EN이 MSG 의미를 빠뜨렸는데 KO가 살린" 불일치** (3:28-30, 3-4, 3-5, 4-2, 4-3, 4-6, 1:7-8, 2:1-2, 2:15-16 등에서 반복) — EN과 KO가 서로 다른 기준(MSG vs EN)으로 작업된 정황. 수정 시 EN을 MSG 기준으로 먼저 바로잡은 뒤 KO를 EN에 맞추는 순서 권장.
2. **KO의 직접 인용부 창작** (14:35-36, 14:37-38, 14:60-61, 14:21, 15:29-30, 16:14-16) — 예수님·대제사장·군중의 대사에 MSG/EN에 없는 문장/질문 삽입. 직접 인용부는 특히 엄격히 1:1로.
3. **KO의 해설 괄호/해설성 추가** (13:5, 13:14, 5:16-17, 5:18-20) — EN에 없는 `(즉, …)` 식 괄호 해설과 평가성 서술.
4. **KO의 기존 한국어 성경(개역식) 표현 회귀** (12:30, 12:32-33, 12:38-40) — 의미는 동등하나 "EN이 primary, KO는 EN의 1:1 번역" 원칙 위반.
5. **KO의 뉘앙스 이동/요소 누락** (14:29 ashamed→버리다, 14:64 선고→외침, 15:46 linen→깨끗한, 14:38 Don't be naive 누락, 14:43 leaders 누락, 15:25-27 좌/우 뭉뚱그림).
6. **KO 따옴표 결함 4건** (9:49-50 여는 `"` 없음, 12:37 stray 닫는 `"`, 14장 p12·p33 닫는 `"` 누락) — 소스 JSON에서 직접 확인됨. 오타 수준이나 일괄 수정 필요.
7. **14·16장 KO 문체 혼용** (서술 반말 + 대화 존댓말; 13장은 -야체 일관, 15장은 -어요체 일관) — 장별 문체 가이드 필요.
8. **EN의 배경지식 기반 추가** (1:7-8 샌들 끈, 3:22 Beelzebul, 4:20 "thirty, sixty, a hundred times", 12:19-23 "to continue the family name" 등) — 의미상 틀리진 않으나 MSG 기준 원칙상 추가. 유지/삭제 정책 판단 필요.

## 커버리지 체크리스트

- [x] 1장: 전 절 감사 (경미 2, 정보 1)
- [x] 2장: 전 절 감사 (경미 2)
- [x] 3장: 본문 전수 감사 (중요 1, 경미 6, 정보 1)
- [x] 4장: 본문 전수 감사 (경미 5, 정보 2)
- [x] 5장: 본문 전수 감사 (경미 5, 정보 2)
- [x] 6장: vr 1–56 전절 감사 (이슈 없음, 정보 1)
- [x] 7장: vr 1–37 감사 (7:16은 MSG 원문에 없음 — 누락 아님) (경미 1, 정보 3)
- [x] 8장: vr 1–38 전절 감사 (경미 3)
- [x] 9장: v1–50 전절 감사 (경미 2)
- [x] 10장: v1–52 전절 감사 — **이슈 없음**
- [x] 11장: v1–25, v27–33 감사 (v26은 MSG 원문에 없음 — 누락 아님) — **이슈 없음**
- [x] 12장: v1–44 전절 감사 (경미 5, 정보 3)
- [x] 13장: 전 절 감사 (경미 3, 정보 1)
- [x] 14장: 전 절 감사 (경미 12, 정보 1)
- [x] 15장: 전 절 감사 (경미 4, 정보 1)
- [x] 16장: 전 절 감사 (경미 2, 정보 1)
- [x] 깨진 문자(U+FFFD): EN/KO 전 파일 코드포인트 단위 전수 검사 — 0건
- [x] 소스 JSON 수정 없음

## 작업 근거 파일

- MSG–Teen pairing 덤프: `/tmp/audit_mark_dump.txt`
- 분할 감사 리포트: `/tmp/audit_ch3-5.md`, `/tmp/audit_ch6-8.md`, `/tmp/audit_ch9-12.md`, `/tmp/audit_ch13-16.md`
---

## 부록: 2026-09-23 미묘한 슬랭 일괄 수정 (번역 원칙 5)

- 배경: 신약 27권 EN/KO 전수 검사에서 자동 욕설 목록 밖의 미묘한 슬랭·저속 표현 발견. 성욱 지시("B 기준 정하고 한 번에 해")에 따라 아래 확정 6개 Rule로 일괄 수정.
- Rule: ① 채팅 약어·유행 은어(ㅇㅋ·here's the tea·woke·throw shade·GOAT·FOMO·fam·vibe) ② 원칙 5 명시 슬랭(썰·꿀잼·쌩까·드립·뇌절·어그로·인싸춤·뿅·텐션·뇌정지·가오·찢길각) ③ ghosting 계열(ghost·고스팅) ④ 신성한 대상 경량화(찐·대박·인싸/아싸·레전드·흑역사·맛집·핫해·좋아요·게임 체인저·That loser is gone) ⑤ 저속·모욕·첨가 강화 순화(관종·lame·freaking out·working my butt off·맛이 갔네·한심·일진/꼽준다·멘붕·멘탈·올인) ⑥ 유지(chill·bro·왕따 — 변경 없음)
- 수정 원칙: EN primary(MSG 의미 유지), KO는 수정된 EN의 의미·톤 1:1, 의미 축소·본문 구조 변경 금지, 해당 표현만 최소 수정.

- 본 권 수정: **EN 2건, KO 9건** (합계 11건). Rule ⑥(chill·bro·왕따) 변경 없음.

| 장 | 위치 | 언어 | Rule | 기존 | 수정 |
|---|---|---|---|---|---|
| 2 | p14 | EN | ① | Who'd pour cold water on this vibe? | Who'd pour cold water on this joyful mood? |
| 11 | p18 | EN | ⑤ | They were freaking out, because the whole crowd was totally captivated by his teaching. | They were seriously rattled, because the whole crowd was totally captivated by his teaching. |
| 1 | p6 | KO | ④ | 여러분을 찐으로 변화시킬 거예요. | 여러분을 진짜로 변화시킬 거예요. |
| 4 | p6 | KO | ④ | 대박 수확을 거뒀어요! | 엄청난 수확을 거뒀어요! |
| 12 | p17 | KO | ④ | 완전 찐하고 기쁘게 지낼 거예요. | 완전 진하고 기쁘게 지낼 거예요. |
| 12 | p4 | KO | ④ | '대박 기회인데?' | '완전 기회인데?' |
| 13 | p1 | KO | ④ | 완전 대박이죠? | 정말 대단하죠? |
| 14 | p24 | KO | ⑤ | 여러분 모두 멘탈이 터질 일이 생길 텐데, | 여러분 모두 마음이 무너질 일이 생길 텐데, |
| 14 | p26 | KO | ⑤ | 다른 애들 다 멘탈 나가서 날 부끄러워해도, | 다른 애들 다 마음이 약해져서 날 부끄러워해도, |
| 16 | p4 | KO | ⑤ | 여자들은 완전 멘붕 상태로 무덤에서 뛰쳐나왔어. | 여자들은 완전히 당황한 상태로 무덤에서 뛰쳐나왔어. |
| 16 | p9 | KO | ④ | 그들의 메시지가 찐이라는 걸 보여주셨어. | 그들의 메시지가 진짜라는 걸 보여주셨어. |

**8개 게이트 결과 (2026-09-23)**: 8개 게이트 전부 PASS — 특이사항: ① 11/11 반영(새 문자열 존재·옛 문자열 소멸), ② validator 16장 모두 통과, ③ completeness FAIL 6건은 slang 적용 전 HEAD 실행 결과와 1:1 동일(오탐 클래스, 수정 문단 ch2 p14·ch11 p18과 무관), ④ 재빌드 Mark.docx에 11/11 반영·옛 문자열 0건, ⑤ PAIRING CONTENT OK(415행/16테이블), ⑥ 재업로드 완료, ⑦ API 테이블 16/16, ⑧ export-back VERIFIED OK.
