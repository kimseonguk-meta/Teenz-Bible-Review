# Teenz Bible 의미 감사 리포트 — 마태복음 (Matthew)

- **감사 일시:** 2026-09-22
- **감사 범위:** 마태복음 28장 전체, § 헤더를 제외한 본문 문단 454개 전수 (ch1 14 / ch2 13 / ch3 8 / ch4 11 / ch5 25 / ch6 28 / ch7 20 / ch8 23 / ch9 25 / ch10 27 / ch11 13 / ch12 24 / ch13 39 / ch14 17 / ch15 19 / ch16 14 / ch17 16 / ch18 15 / ch19 21 / ch20 7 / ch21 8 / ch22 9 / ch23 11 / ch24 9 / ch25 10 / ch26 10 / ch27 12 / ch28 6)
- **감사 방법:** 각 Teen 본문 문단에 `build_gdocs.py`의 `match_msg_for_teen()`으로 매칭된 MSG 단위 원문을 가져와서 (1) Teen EN이 MSG의 모든 의미 요소(사실, 인명/지명, 인용문, 논리 연결/원인-결과/조건, 경고, 예언, 명령, 숫자)를 보존하는지, (2) KO가 EN의 1:1 번역(의미 동등, 임의 추가/삭제 없음)인지 대조. § 헤더 행은 감사 제외.
- **MSG 소스:** `msg_matthew_raw.json` (+ `msg_raw_1.txt`, `msg_raw_3.txt`) → `parse_msg_matthew()`.
- **소스 파일 수정:** 없음 (읽기 전용 감사).

## 요약

| 구분 | 건수 |
|---|---|
| 🔴 수정 필요 — 실질 이슈 (의미 누락/변형/원칙 위반) | 16건 |
| 🟡 경미 — 뉘앙스 약화/임의 추가 등 | 17건 |
| 👀 관찰 — MSG 없는 EN/KO 임의 gloss (부모 판단용 기록) | 12건 |
| ✅ 이슈 없음 (454개 중) | 409개 문단 |

**가장 심각한 이슈:** Ch 23:23-24 — KO가 EN의 1:1 번역이 아니라 개역개정식 텍스트를 붙여넣은 것으로 보임 (원칙 4 위반). Ch 21:44 경고문 전체 누락, Ch 8:20 MSG에 없는 문장 전체 삽입, Ch 2:13 꿈 현현→실제 깨움 변형.

---

## 🔴 수정 필요 — 실질 이슈

### ISSUE-1 — Ch 2, vr 13: MSG의 "꿈에 나타남"이 EN에서 "한밤중에 깨움"으로 변형
- **MSG 원문:** "God's angel **showed up again in Joseph's dream** and commanded, 'Get up…'"
- **현행 Teen EN:** "After the scholars left, **an angel woke Joseph up in the middle of the night**: 'Get up! Take the baby and his mom and run to Egypt…'"
- **문제 내용:** MSG는 세 번째 **꿈 속** 천사 현현("showed up again in Joseph's dream")인데, EN은 천사가 실제로 요셉을 한밤중에 깨운 것처럼 서술 → '꿈' 요소와 "again"(다시) 모두 소실. 의미 변형.
- **수정 방향:** EN을 teen voice로 "꿈" 복원 — 예: "After the scholars left, an angel showed up in Joseph's dream again in the middle of the night." KO는 수정된 EN의 1:1 번역.

### ISSUE-2 — Ch 2, vr 14-15: 예언자 이름 "호세아" 누락
- **MSG 원문:** "This Egyptian exile fulfilled what **Hosea** had preached: 'I called my son out of Egypt.'"
- **현행 Teen EN:** "that made the prophet's words come true: 'Out of Egypt I called my son.'"
- **문제 내용:** MSG가 명시한 인명 "Hosea"가 EN에서 일반명사 "the prophet"로 축소.
- **수정 방향:** EN에 "Hosea" 복원 — 예: "that made what the prophet Hosea had preached come true." KO 1:1 반영 ("호세아 예언자").

### ISSUE-3 — Ch 2, vr 14-15: "날이 밝기 전 성을 빠져나감" 누락
- **MSG 원문:** "They were **out of town and well on their way by daylight**."
- **현행 Teen EN:** "Joseph didn't ask questions; he packed up and they fled under the cover of darkness."
- **문제 내용:** "날이 밝을 무렵엔 이미 성을 벗어나 멀리 가고 있었다"는 사실 요소가 EN 어디에도 없음.
- **수정 방향:** EN에 teen voice로 추가 — 예: "…and by sunrise they were already long gone, well out of town." KO 1:1 번역.

### ISSUE-4 — Ch 2, vr 17-18: 예레미야 인용 끝 "dead and buried" 누락
- **MSG 원문:** "Rachel weeping for her children, Rachel refusing all solace, Her children gone, **dead and buried.**"
- **현행 Teen EN:** "…Rachel weeping for her children, refusing to be comforted, because her children are gone."
- **문제 내용:** 인용문 끝의 "dead and buried"(죽어 묻혔다)가 탈락. "gone"만으로는 죽음이 명시되지 않아 인용의 강도 약화.
- **수정 방향:** EN 인용 끝에 복원 — 예: "…because her children are gone — dead and buried." KO 1:1 번역.

### ISSUE-5 — Ch 2, vr 1-2: "Judah territory" 누락
- **MSG 원문:** "After Jesus was born in Bethlehem village, **Judah territory**…"
- **현행 Teen EN:** "Jesus was born in the town of Bethlehem during the rule of King Herod."
- **문제 내용:** MSG의 지명 수식어 "Judah territory"(유대 지역)가 EN·KO 모두에서 소실.
- **수정 방향:** EN에 복원 — 예: "Jesus was born in the town of Bethlehem, in Judah territory, during the rule of King Herod." KO 1:1 번역.

### ISSUE-6 — Ch 8, vr 20: MSG에 없는 문장 전체 삽입
- **MSG 원문:** "Jesus was curt: 'Are you ready to rough it? **We're not staying in the best inns, you know.**'" (MSG 소스 원문 직접 확인 — 여우/새 문장 없음)
- **현행 Teen EN:** "Jesus was pretty direct: 'Are you ready to rough it? We're not staying in five-star hotels, you know. **Foxes have dens, and birds have nests, but the Son of Man (that's Jesus referring to himself) doesn't even have a place to crash.**'"
- **문제 내용:** EN이 MSG 원문에 전혀 없는 문장 전체("여우의 굴·새의 둥지·인자는 머리 둘 곳조차 없음" 개념)를 전통 본문에서 가져와 삽입. 생략이 아니라 반대 방향의 원칙 위반.
- **수정 방향:** EN에서 "Foxes have dens… a place to crash." 문장 삭제 ("(that's Jesus referring to himself)" 부연도 함께 제거). "five-star hotels" teen 표현은 유지. KO는 EN의 1:1이라 EN 수정에 연동.

### ISSUE-7 — Ch 10, vr 24-25: KO가 EN의 'Dungface'를 일반화
- **MSG 원문:** "If they call me, the Master, **'Dungface,'** what can the workers expect?"
- **현행 Teen EN:** "If they call me, the Master, 'Dungface', what do you think the workers can expect?" (EN은 OK)
- **현행 Teen KO:** "주인인 저에게 **모욕적인 별명을 붙여 욕하는데**, 팀원인 여러분은 뭘 기대하겠어요?"
- **문제 내용:** EN의 특정 모욕 표현 'Dungface'가 KO에서 "모욕적인 별명"으로 일반화되어 1:1 번역 깨짐. 원칙 5(욕·비속어 순화)는 "뜻은 살리되" 순화인데, 뜻 자체가 사라짐.
- **수정 방향:** KO를 EN의 특정 표현을 살린 1:1 번역으로 수정 — 예: "'똥얼굴'이라고 나를 욕하는데, 일꾼인 여러분은 뭘 기대하겠어요?" (수위 조정 필요 시 별도 판단.)

### ISSUE-8 — Ch 11, vr 2-3: 요한이 제자를 보낸 동기(인과절) 누락 + 창작 심리 묘사 삽입
- **MSG 원문:** "John, meanwhile, had been locked up in prison. **When he got wind of what Jesus was doing**, he sent his own disciples to ask, 'Are you the One we've been expecting, or are we still waiting?'"
- **현행 Teen EN:** "John the Baptist had been locked up in prison, **and sitting in a dark cell was messing with his head**. He sent his own crew to ask Jesus, 'Are you really the Messiah we've been waiting for, or should we keep looking?'"
- **문제 내용:** MSG의 인과절 "When he got wind of what Jesus was doing"(예수님의 사역 소식을 듣고)가 통째로 빠지고, MSG에 없는 창작 심리 묘사("어두운 감옥방이 머리를 복잡하게 만들었다")로 대체 → 요한이 제자를 보낸 동기가 바뀜.
- **수정 방향:** EN을 teen voice로 복원 — 예: "John had been locked up in prison. When he heard what Jesus was up to, he sent his own crew to ask…". 창작 심리 묘사 삭제. KO는 수정된 EN의 1:1 번역.

### ISSUE-9 — Ch 11, vr 28-30: "Get away with me and you'll recover your life" 약속 누락
- **MSG 원문:** "'Are you tired? Worn out? Burned out on religion? Come to me. **Get away with me and you'll recover your life.** I'll show you how to take a real rest…'"
- **현행 Teen EN:** "'Are you tired? Worn out? Exhausted from trying to follow all the religious rules perfectly? **Come hang with me.** I'll show you how to take a real rest…'"
- **문제 내용:** MSG의 약속 "Get away with me and **you'll recover your life**"(나와 함께 떠나면 네 삶을 되찾을 것이다)가 EN에서 완전히 누락. '쉼'은 남았지만 '삶의 회복' 요소 소실.
- **수정 방향:** EN에 teen voice로 복원 — 예: "Come hang out with me — get away with me and you'll get your life back." KO는 수정된 EN의 1:1 번역.

### ISSUE-10 — Ch 12, vr 11-14: 안식일 논쟁 핵심 논점 이동
- **MSG 원문:** "'Is there a person here who, **finding one of your lambs** fallen into a ravine, wouldn't, even though it was a Sabbath, pull it out? **Surely kindness to people is as legal as kindness to animals!**'"
- **현행 Teen EN:** "'Is there anyone here who, **if their one and only lamb** fell into a ditch, wouldn't pull it out, even if it was the Sabbath? Of course, you would! So, **isn't being kind to people just as important, or even more important, than being kind to animals?**'"
- **문제 내용:** ① "one of your lambs"(네 양 떼 중 한 마리) → "their one and only lamb"(유일한 양 한 마리)로 이미지 변경. ② 핵심: 안식일 논쟁의 핵심 논점인 **"as legal as"(법적으로 허용된다)**가 **"just as important"(중요하다)**로 바뀜. MSG는 "사람에게 친절한 것도 동물에게 친절한 것만큼 안식일에 합법하다"는 법적 결론인데, EN은 중요도 비교로 논점 이동.
- **수정 방향:** EN 결론부를 teen voice로 법적 허용 의미 복원 — 예: "So being kind to a person on the Sabbath is just as legit as being kind to an animal, right?" KO는 수정된 EN의 1:1 번역.

### ISSUE-11 — Ch 15, vr 16-20: MSG 병렬 요소 한 축("certain foods") 누락
- **MSG 원문:** "That's what pollutes. **Eating or not eating certain foods, washing or not washing your hands—that's neither here nor there.**"
- **현행 Teen EN:** "Jesus replied, 'You too? Are you being willfully stupid? Don't you get that whatever you swallow just works its way through your gut and out the other end? But what comes out of your mouth starts in your heart — that's where evil schemes, murders, adultery, sleeping around, theft, lies, and cussing all come from. That's what actually pollutes you. **Eating with unwashed hands? That's neither here nor there.**'"
- **문제 내용:** MSG 마지막 문장에 병렬된 두 요소 "certain foods 먹기/안 먹기"와 "손 씻기/안 씻기" 중 첫 번째가 EN에서 완전히 빠짐. MSG의 "neither here nor there" 판결이 손 씻기뿐 아니라 음식 규정(정결법)에도 적용되는데, EN은 손 씻기 하나로 축소.
- **수정 방향:** EN을 teen voice로 두 축 모두 복원 — 예: "Eating with unwashed hands — or eating this or that food? That's neither here nor there." KO는 수정된 EN의 1:1 번역.

### ISSUE-12 — Ch 15, vr 29-31: 치유 목록 한 그룹("the maimed healthy") 누락
- **MSG 원문:** "When the people saw **the mutes speaking, the maimed healthy, the paraplegics walking around, the blind looking around**"
- **현행 Teen EN:** "When the crowd saw mutes talking, cripples walking, and blind people seeing"
- **현행 Teen KO:** "말 못하던 사람이 말하고, 절름발이가 걷고, 눈먼 사람이 보는 걸 보고"
- **문제 내용:** MSG의 4개 그룹(mutes / the maimed / paraplegics / blind) 중 "the maimed healthy"(불구자·훼손된 이들의 온전한 회복)가 EN에서 빠지고 3개로 축소. "cripples walking"은 paraplegics를 커버할 뿐 maimed의 회복은 담지 않음. KO도 EN을 따라가며 함께 누락.
- **수정 방향:** EN에 "cripples healed and walking" 등으로 maimed healthy 요소 복원. KO는 수정된 EN의 1:1 번역 ("불구였던 사람이 멀쩡해지고, 절름발이가 걷고…").

### ISSUE-13 — Ch 20, vr 24-28: "godless rulers"를 "the Romans"로 좁힘 + 분노 동기 추론 삽입
- **MSG 원문:** "When the ten others heard about this, they lost their tempers, **thoroughly disgusted with the two brothers**. … 'You've observed how **godless rulers** throw their weight around, how quickly a little power goes to their heads.'"
- **현행 Teen EN:** "they were absolutely furious at James and John **for trying to bypass them for the best jobs**" / "'You guys know how **the Romans** do leadership—they boss people around, flex their power, and make everyone serve them.'"
- **문제 내용:** (a) MSG의 일반적 표현 "godless rulers"가 EN에서 "the Romans"로 특정됨 — MSG는 로마라고 명시하지 않음. (b) MSG에 없는 분노 동기 설명("최고 자리를 가로채려 해서") 삽입 — 해석적 추론.
- **수정 방향:** EN의 "Romans"를 teen voice로 "godless rulers"에 가깝게 되돌리고, "for trying to bypass them for the best jobs" 동기 설명은 삭제 또는 MSG 수준("thoroughly disgusted with the two brothers")으로 축소. KO 연동.

### ISSUE-14 — Ch 21, vr 40-46: MSG 21:44 경고문 전체 누락
- **MSG 원문:** "…God's kingdom will be taken back from you and handed over to a people who will live out a kingdom life. **Whoever stumbles on this Stone gets shattered; whoever the Stone falls on gets smashed.**"
- **현행 Teen EN:** "'Exactly. And you've read the scripture: > The stone the builders rejected has become the cornerstone. This is the Lord's doing, and it is marvelous in our eyes. Therefore I tell you that the kingdom of God will be taken away from you and given to a people who will produce its fruit.' When the religious leaders heard his stories, …"
- **문제 내용:** MSG v44 상당 경고(모퉁잇돌에 대한 심판 경고: 넘어지는 자 깨지고, 돌이 떨어지는 자 부서진다)가 EN에서 완전히 빠짐. KO도 EN을 따라 같은 누락.
- **수정 방향:** EN에 teen voice로 복원 — 예: "Trip over this Stone and you'll get shattered; let it fall on you and you'll get crushed." KO는 수정된 EN의 1:1 번역으로 추가.

### ISSUE-15 — Ch 23, vr 23-24: KO가 EN의 번역이 아니라 다른 원문 기반
- **MSG/EN 원문:** "'You're hopeless, you religion scholars and Pharisees! Frauds! You keep meticulous account books, tithing on every nickel and dime you get, but on the meat of God's Law, things like fairness and compassion and commitment — the absolute basics! — you carelessly take it or leave it. Careful bookkeeping is commendable, but the basics are required. Do you have any idea how silly you look, writing a life story that's wrong from start to finish, nitpicking over commas and semicolons?'"
- **현행 Teen KO:** "율법학자들이랑 바리새파 사람들이여, 사기꾼들이여, 답이 없어요! 여러분은 박하, 회향, 근채 같은 향신료의 십일조는 꼬박꼬박 바치면서, 정작 율법에서 더 중요한 정의, 자비, 신실함은 아예 내팽개쳤어요. 그것들도 해야 하지만, 이것도 놓치면 안 되죠. 눈먼 안내자들이여! 하루살이는 걸러내면서 낙타는 통째로 삼키는군요."
- **문제 내용:** KO가 EN의 1:1 번역이 아니라 개역개정식 번역체("박하, 회향, 근채… 하루살이는 걸러내면서 낙타는 통째로"는 MSG/EN 어디에도 없음)를 붙여넣은 것으로 보임. 원칙 4(EN-KO 구조/의미 일치) 위반 — 가장 심각한 KO 이슈.
- **수정 방향:** KO를 현행 EN의 1:1 번역으로 전면 교체 — 예: "여러분은 꼼꼼한 장부 정리로 1원짜리 십일조까지 다 바치면서, 율법의 핵심인 공정함과 자비와 헌신 — 진짜 기본인데! — 은 대충 넘겨버리잖아요. 장부 정리는 잘했어. 근데 기본은 필수라고요. 처음부터 끝까지 틀린 인생 스토리를 쓰면서 쉼표랑 세미콜론에 집착하는 게 얼마나 우스워 보이는지 알아요?"

### ISSUE-16 — Ch 26, vr 6-13: KO에 MSG/EN에 없는 "머리에" 추가
- **MSG 원문:** "a woman came up to him as he was eating dinner and anointed him with a bottle of very expensive perfume"
- **현행 Teen EN:** "She poured a whole bottle of super expensive perfume on him." (부위 미지정)
- **현행 Teen KO:** "엄청 비싼 향수 한 병을 통째로 예수님의 **머리에** 부은 거야."
- **문제 내용:** MSG와 EN 어디에도 '머리' 지정 없음(마태복음 26장은 부위를 명시하지 않음). KO 임의 추가 — EN-KO 1:1 원칙 위반.
- **수정 방향:** KO에서 "머리에" 삭제 → "엄청 비싼 향수 한 병을 통째로 예수님께 부은 거야." (참고: 같은 문단 KO의 "내 몸에 향유를 부은 건 내 장례를 준비한 거야"는 MSG "When she poured this perfume on my body"에 근거가 있어 정상.)

---

## 🟡 경미 — 뉘앙스 약화/임의 추가

### M-1 — Ch 1, vr 1: EN의 해석적 추가 2건
- **MSG 원문:** "The family tree of Jesus Christ, David's son, Abraham's son:"
- **현행 Teen EN:** "Think of this as Jesus's ancestry report. **It proves he has the royal bloodline of King David** and traces his roots all the way back to Abraham, **the father of the Jewish faith**."
- **문제 내용:** MSG에 없는 "proves(증명)" 프레임과 "father of the Jewish faith" 수식어가 추가됨. 의미 반전은 아니나 MSG에 없는 해석 삽입.
- **수정 방향:** 유지한다면 MSG 근거 명시 수준으로 완화하거나 삭제. KO는 EN에 연동.

### M-2 — Ch 3, vr 7-10: KO가 EN에 없는 "열매 맺고" 추가
- **현행 Teen EN:** "Is it green and flourishing?"
- **현행 Teen KO:** "너네 삶이 지금 파릇파릇 **열매 맺고** 있어?"
- **문제 내용:** KO가 EN에 없는 "열매 맺고"를 추가 — EN↔KO 1:1 원칙 위반(경미한 의미 확장).
- **수정 방향:** KO를 "너네 삶이 지금 파릇파릇 살아 있어?" 수준으로 EN에 맞춤.

### M-3 — Ch 4, vr 1-3: EN이 MSG에 없는 "세례 직후" 추가
- **MSG 원문:** "Next Jesus was taken into the wild by the Spirit for the Test."
- **현행 Teen EN:** "**Immediately after his baptism**, the Spirit led Jesus deep into the wilderness to be tested by the devil."
- **문제 내용:** MSG는 "Next"일 뿐 "세례 직후" 명시 없음. MSG에 없는 사실 추가.
- **수정 방향:** EN에서 "Immediately after his baptism," 삭제하고 "Next" 수준으로. KO의 "세례를 받자마자"도 함께 삭제.

### M-4 — Ch 4, vr 4: "steady stream" 뉘앙스 약화
- **MSG 원문:** "It takes a **steady stream** of words from God's mouth."
- **현행 Teen EN:** "they need the words of God."
- **문제 내용:** "steady stream"(꾸준히 흘러나오는) 뉘앙스가 빠지고 밋밋한 표현으로 약화. 신명기 8:3 인용의 핵심 이미지 일부 손실.
- **수정 방향:** EN을 teen voice로 복원 — 예: "they need a steady stream of words coming from God's mouth." KO도 "하나님의 입에서 꾸준히 흘러나오는 말씀" 뉘앙스로 재번역.

### M-5 — Ch 5, vr 1-2: EN의 편집자 논평 추가
- **MSG 원문:** "Arriving at a quiet place, he sat down and taught his climbing companions. This is what he said:"
- **현행 Teen EN:** "…This is what he said: **the greatest speech ever given, where Jesus flips the world's rulebook** on how God's kingdom actually works."
- **문제 내용:** MSG에 전혀 없는 편집자 논평("역대 최고의 설교", "세상의 룰북을 뒤집는다") 삽입.
- **수정 방향:** EN에서 해당 부가 문장 삭제. KO("역대 최고의 설교…")도 함께 삭제.

### M-6 — Ch 5, vr 43-47: "supple moves" → "energies" 뉘앙스 변경
- **MSG 원문:** "respond with the **supple moves** of prayer"
- **현행 Teen EN:** "respond with the **energies** of prayer"
- **문제 내용:** "supple moves"(유연하고 부드럽게 대응하는 몸짓) → "energies"(힘)로 변경. 원수에게 기도로 '유연하게' 응한다는 의미가 '힘으로' 응한다는 식으로 바뀜.
- **수정 방향:** EN을 teen-friendly하게 복원 — 예: "respond with the supple, flexible moves of prayer." KO("기도의 힘으로 응답하세요")는 수정된 EN에 맞춰 1:1 재번역.

### M-7 — Ch 7, vr 6: 단정적 경고를 "might"로 완화
- **MSG 원문:** "In trying to be relevant, **you're only being cute and inviting sacrilege.**"
- **현행 Teen EN:** "When you try too hard to make it 'relevant' or 'cute,' **you might actually end up** inviting disrespect for what's holy."
- **문제 내용:** MSG의 단정적 진술("~할 뿐이다")이 EN에서 "~할 수도 있다"로 완화 → 경고의 강도 약화.
- **수정 방향:** EN의 "might actually end up"를 단정 표현으로 복원 — 예: "you're just being cute, and you're inviting disrespect for what's holy." KO도 단정 어조로 재번역.

### M-8 — Ch 7, vr 15-20: MSG에 없는 "metaphorically speaking" 주석 삽입
- **MSG 원문:** "These diseased trees with their bad apples **are going to be** chopped down and burned."
- **현행 Teen EN:** "These 'diseased trees' with their 'bad apples' are **eventually** going to be chopped down and burned, **metaphorically speaking**."
- **문제 내용:** MSG에 없는 해석("metaphorically speaking" — 비유적으로 말해서)과 "eventually"가 EN에 추가. 원문에 없는 주석적 개입.
- **수정 방향:** EN에서 ", metaphorically speaking" 삭제 ("eventually"도 삭제 권장). KO의 "비유적으로 말해서요"도 함께 삭제.

### M-9 — Ch 9, vr 9: EN 부연 "(which most people hated)" 추가
- **MSG 원문:** "Jesus saw a man at his work collecting taxes. His name was Matthew."
- **현행 Teen EN:** "he spotted a guy named Matthew at his job, collecting taxes **(which most people hated)**."
- **문제 내용:** MSG에 없는 부연 설명 추가.
- **수정 방향:** 괄호 부연 삭제. KO도 함께 수정.

### M-10 — Ch 9, vr 16-17: EN에 "new/old", "because they'll burst" 추가
- **MSG 원문:** "And you don't put your wine in cracked bottles."
- **현행 Teen EN:** "And you definitely don't put your **new wine in old**, cracked bottles, **because they'll burst!**"
- **문제 내용:** MSG에 없는 "new", "old", 원인-결과 설명 "because they'll burst" 추가 (KO: "다 터져버릴 테니까요").
- **수정 방향:** EN을 MSG 범위로 단순화 — 예: "And you definitely don't put your wine in cracked bottles." KO도 이에 맞춰 1:1 수정.

### M-11 — Ch 10, vr 26-27: EN 꼬리 "tell everyone the truth" 추가
- **MSG 원문:** "So don't hesitate to go public now."
- **현행 Teen EN:** "So don't hesitate to go public now, **tell everyone the truth**."
- **문제 내용:** MSG에 없는 꼬리 문구 추가.
- **수정 방향:** 꼬리 문구 삭제. KO도 함께 수정.

### M-12 — Ch 11, vr 1: "their" 소실 + "Galilee" 추가
- **MSG 원문:** "he went on to teach and preach **in their villages**."
- **현행 Teen EN:** "He headed off to teach and preach **in the towns around Galilee**."
- **문제 내용:** MSG의 "their"(제자들의) 소유격이 빠지고, MSG에 없는 "Galilee" 지명 추가.
- **수정 방향:** "their towns" 의미를 살려 "in the towns around them" 등으로 조정. KO 동반 수정.

### M-13 — Ch 12, vr 22-23: 확신의 감탄이 의심의 속삭임으로 톤 약화
- **MSG 원문:** "The people who saw it were impressed—'**This has to be the Son of David!**'"
- **현행 Teen EN:** "The people who saw it were blown away, **whispering, 'Could this actually be the Son of David (the Messiah)?'**"
- **문제 내용:** MSG의 확신에 찬 감탄(단언)이 EN에서는 의심스러운 속삭임(의문문)으로 톤 약화.
- **수정 방향:** EN을 단언형 감탄으로 복원 — 예: "This has to be the Son of David — the Messiah!" KO 동반 수정.

### M-14 — Ch 12, vr 41-42: "preacher" 수식어 누락
- **MSG 원문:** "**A far greater preacher than Jonah** is here, and you squabble about 'proofs.'"
- **현행 Teen EN:** "**Someone way greater than Jonah** is here, and you're still arguing about 'proofs.'"
- **문제 내용:** "preacher"(설교자) 수식어 누락 — 요나와의 대비점이 '설교자 vs 설교자'인데 EN은 막연한 '누군가'.
- **수정 방향:** "A way greater preacher than Jonah is here"로 복원. KO 동반 수정.

### M-15 — Ch 13, vr 44: "trespasser" 누락
- **MSG 원문:** "a treasure hidden in a field for years and then accidentally found **by a trespasser**."
- **현행 Teen EN:** "a treasure that's been hidden in a field for years, and then **someone** just accidentally stumbles upon it."
- **문제 내용:** "trespasser"(남의 밭에 들어간 사람) 누락 — 발견자가 밭 주인이 아니라서 밭을 사야 한다는 서사 논거 약화.
- **수정 방향:** teen voice로 복원 — 예: "some guy wandering onto someone else's field" 식. KO 동반 수정.

### M-16 — Ch 16, vr 19: "any and every door" 이미지 누락
- **MSG 원문:** "You will have complete and free access to God's kingdom, **keys to open any and every door**: no more barriers between heaven and earth, earth and heaven."
- **현행 Teen EN:** "I'm giving you the keys to God's kingdom — complete, free access, no more barriers between heaven and earth."
- **문제 내용:** "keys to open any and every door"(어떤 문이든 여는 열쇠)라는 MSG의 구체적 이미지가 EN에서 빠짐.
- **수정 방향:** EN에 "keys that open any and every door" 복원. KO는 수정된 EN에 맞춰 조정.

### M-17 — Ch 19, vr 11-12: KO의 "knack" 오역
- **MSG 원문:** "It requires a certain aptitude and grace."
- **현행 Teen EN:** "It takes a certain **knack** and a lot of grace." (EN은 MSG와 일치)
- **현행 Teen KO:** "특별한 은혜와 **준비**가 필요하죠."
- **문제 내용:** EN의 "a certain knack"(특별한 적성/소질)이 KO에서 "준비"(preparation)로 잘못 옮겨짐. "knack/aptitude"는 타고난 적성에 가깝고 "준비"는 다른 의미.
- **수정 방향:** KO를 "특별한 소질(적성)과 많은 은혜가 필요하죠" 식으로 정정. EN 변경 불필요.

---

## 👀 관찰 — EN/KO의 MSG 외 임의 gloss (부모 판단용, 의미 반전 아님)

1. **Ch 15, vr 10-11:** EN이 MSG에 없는 구체 예시 추가 — "the garbage that comes out of your mouth — the lies, the trash-talk, the hate". MSG v10-11은 "what you vomit up"만. (KO는 EN의 1:1로 일치)
2. **Ch 15, vr 3-6:** KO가 EN에 없는 단어 추가 — EN "I've given to God instead" → KO "하나님께 **예물로** 드렸어요".
3. **Ch 17, vr 2-3:** EN이 MSG에 없는 설명 추가 — "two Old Testament legends".
4. **Ch 18, vr 22:** EN이 MSG에 없는 문장 추가 — "Try seventy times seven. **Stop keeping score.**" MSG는 "Try seventy times seven."까지. (KO "점수 세는 거 그만해"는 EN 1:1 일치)
5. **Ch 19, vr 3:** EN이 MSG v3("badgered him")에 없는 동기·설명 추가 — "trying to trap him", "(a religious group known for being super strict)". 바리새파를 함정 파기로 단정한 것은 MSG 본문을 넘어선 해석 추가.
6. **Ch 19, vr 13-15:** EN "some parents brought their kids" — MSG는 "children were brought to Jesus"로 데려온 주체 미상. "parents" 특정은 추론 추가.
7. **Ch 19, vr 28-30:** EN "(Jesus himself)" 삽입.
8. **Ch 20, vr 8-16:** EN "We worked twelve hours in the blistering heat" — MSG는 "slaved all day under a scorching sun"이며 "12시간"은 추론. 무해한 paraphrase로 판단.
9. **Ch 20, vr 20-23:** EN "Can you drink from the cup of suffering I'm about to drink from?" — MSG "the cup that I'm about to drink"에 해석적 수식어 "of suffering" 추가. 문맥상 허용 가능하나 기록.
10. **Ch 24, vr 1-3:** EN에 MSG에 없는 대사 추가 — "'Hey, Jesus, check out these buildings! So epic!'" (MSG: 제자들이 성전 건축물을 가리켰을 뿐). 무해한 dramatization.
11. **Ch 28, vr 5-7:** EN 추가 — "The women peeked inside, and sure enough, the tomb was empty." (MSG: "Come and look at the place where he was placed"만). 무해한 dramatization.
12. **Ch 20, vr 24-28:** EN/KO에 stray ">" 문자 — "It is not going to be like that with you. > Whoever wants to be a leader among you…" (표시 정리용, 의미 문제 아님).

---

## ✅ 이슈 없음 판정 장절 (핵심 커버리지 확인)

- **Ch 1:** 족보(2-17), 요셉의 고민과 천사 발언, 임마누엘 인용(20-25) — MSG 의미 완전 보존.
- **Ch 3:** 세례자 요한 설교 전문(7-12절) 완전 보존.
- **Ch 4:** 시험 이야기의 3대 유혹 + 신명기 인용 3회, 4:12-25 사역 시작 — 완전 보존.
- **Ch 5:** 팔복(3-10), 소금/빛, 율법 해석(17-20), 살인·간음·이혼·맹세·보복·원수 사랑 대조 가르침(21-48) — 완전 보존.
- **Ch 6:** 주기도문 7개 청원, 금식/재물/염려 가르침 — 완전 보존.
- **Ch 7:** 비판/구함/좁은 문/거짓 선지자/반석 비유 — 보존 (M-7, M-8 경미 제외).
- **Ch 8:** 백부장, 8:10-12 경고문("out in the cold…"), 이사야 인용(16-17), 귀신들린 자들, 풍랑 — 보존 (ISSUE-6 제외).
- **Ch 9:** 중풍병자, 마태 소명, "I'm after mercy, not religion" 인용(12-13), 야이로 딸, 소경들 — 보존 (M-9, M-10 경미 제외).
- **Ch 10:** 파송 지시 전체(5-42) 세부 명령·경고·약속 — 보존 (ISSUE-7, M-11 제외).
- **Ch 11:** 세례 요한 관련 가르침 — 보존 (ISSUE-8, ISSUE-9, M-12 제외).
- **Ch 12:** 말라기 인용(11:10), 이사야 인용(12:18-21), 안식일 논쟁의 다윗/제사장 예증, 바알세불 논증, 12:31-32 성령 모독 경고, 12:40 사흘 밤낮, 12:45 일곱 귀신 — 보존 (ISSUE-10, M-13, M-14 제외).
- **Ch 13:** 6개 비유(씨 뿌리는 자 4종 토양, 가라지, 겨자씨, 누룩, 보화, 진주, 그물)의 세부 묘사·해석 매핑 — 보존 (M-15 제외).
- **Ch 14:** 세례 요한 죽음, 오천 명(열두 광주리), 물 위 걷기 — 보존.
- **Ch 16:** 요나의 표적, 누룩=가르침, 베드로 고백·반석·지옥 문, 예루살렘 고난·사흘째 부활, "Satan, get lost", 자기 부인·영혼 거래 논리 — 보존 (M-16 경미 제외).
- **Ch 17:** 변화산(햇빛 쏟아지는 얼굴·빛 가득한 옷·모세와 엘리야의 대화), "This is my Son… Listen to him", 엘리야=세례 요한, 간질 아이 치유, 겨자씨 믿음, 성전세 물고기 동전 — 완전 보존.
- **Ch 18:** 어린아이·맷돌 경고·수호천사·잃은 양(100/99/1)·형제 권면 4단계·둘셋 기도, 일만 달란트 비유(십만 달러/십 달러 숫자, 아내·자녀·재산 경매, "begged me for mercy" vs "asked for mercy" 대조, 무조건 용서 결론) — 보존.
- **Ch 19:** 이혼 논쟁("한 몸", 모세 허용=마음 완악 때문, 간음 예외), 계명 목록, 부자 청년·낙타와 바늘귀·백 배 보상·대반전 — 보존 (M-17 제외).
- **Ch 20:** 포도원 품꾼 비유(1-16), 수난 예고(17-19) — 보존 (ISSUE-13, 관찰 8·9·12 제외).
- **Ch 21:** 예루살렘 입성·성전 정화, 권위 논쟁·두 아들/악한 농부 비유 — 보존 (ISSUE-14 제외).
- **Ch 22:** 혼인 잔치·가이사 세금·부활 논쟁·최대 계명 — 완전 보존.
- **Ch 23:** 화 있을진저 나머지 전 구간 — 보존 (ISSUE-15 제외).
- **Ch 24:** 종말 말씀 전 구간 — 보존 (관찰 10 제외).
- **Ch 25:** 열 처녀·달란트·양과 염소 — 완전 보존.
- **Ch 26:** 수난 서사 전 구간 — 보존 (ISSUE-16 제외). 26:26-28(성만찬)/26:29(포도주 서원) 분할 배치는 의도적 분할로 합산 커버리지 완전.
- **Ch 27:** 수난 서사 전 구간 — 완전 보존.
- **Ch 28:** 부활 서사 전 구간 — 보존 (관찰 11 제외).
- **KO vs EN:** 전 레코드에서 KO는 EN의 충실한 1:1 번역 (ISSUE-7, ISSUE-15, ISSUE-16, M-2, M-17 제외).

---

## 데이터 주의사항 (번역 이슈 아님 — 감사 과정에서 확인)

1. **Ch 1 idx 2 (vr=2-6)** 의 매칭 라벨이 `MSG[6-11]`로 표기되나 EN은 정확히 2-6절 내용("Abraham had Isaac…David became king")을 담고 있고, MSG 2-6절 원문은 idx 0의 msg 꼬리("2-6 Abraham had Isaac…")에 있음. 매칭/라벨 아티팩트이며 번역 자체는 정확 — 이슈 아님.
2. **Ch 23 v14 레코드 없음:** MSG 소스(`msg_matthew_raw.json`) 자체가 23:13 다음 23:15로 건너뛰며 **23:14를 포함하지 않음**. EN/KO에 23:14가 없는 것은 MSG 기준 정상 — 이슈 아님.
3. **MSG 소스 자체에 없는 절:** 17:21, 18:11 — MSG 번역본이 해당 절을 생략. EN/KO 누락 아님.
4. **MSG 본문 내 절 번호 표기**(예: "2-6 Abraham had Isaac")는 파서 아티팩트로 의미 비교에서 제외.
5. **의도적 split/merge 구조:** 6:22-23, 7:1-5, 11:28-30, 12:11-14, 13:3-8, 15:3-6+7-9, 17:1+2-3, 19:11-14, 26:26-28+29-35 등은 하나의 MSG 범위가 여러 문단으로 나뉜 것으로, 합치면 의미 완전 커버됨.

---

## 총평

마태복음 28장 454개 문단 중 **409개 문단은 MSG↔EN↔KO 의미 동등 정상**. 핵심 교리 구간(산상수훈, 주기도문, 비유들, 수난·부활 서사)은 대체로 충실.

**수정이 필요한 실질 이슈 16건:** Ch 2에서 5건이 집중(꿈 현현 변형, Hosea 명칭, 날 밝기 전 탈출, dead and buried 인용, Judah territory). 그 외 Ch 21:44 경고문 전체 누락, Ch 8:20 MSG 없는 문장 삽입, Ch 23:23-24 KO의 개역개정식 텍스트 혼입(원칙 4 위반 — 가장 시급), Ch 26:6-13 KO의 "머리에" 임의 추가, Ch 10:24-25 KO의 'Dungface' 일반화 등이 있음.

**경미 17건**은 뉘앙스 약화(steady stream→words, supple moves→energies, 단정→might 등)와 MSG 없는 EN의 임의 추가(gloss)로, 성욱 판단 하에 정리 권장.

*소스 JSON 파일은 일절 수정하지 않음. 수정 작업은 별도 승인 후 진행.*
