# Romans 의미 감사 리포트 (MSG 기준 대조)

- 감사일: Sep 22, 2026
- 방법: `build_gdocs.py`의 `parse_msg_romans()` + `match_msg_for_teen()`으로 16장 전체 175개 Teen 문단을 MSG unit에 매칭한 덤프(`/tmp/romans_audit/ch01–ch16.txt`)를 문단별로 직접 대조.
- 기준: ① Teen EN이 MSG의 사실·인명·지명·인용·논리·조건·경고·명령·숫자를 축약 없이 보존했는지 ② KO가 같은 위치 EN을 1:1 번역했는지. Teen-friendly 표현 변경은 허용, 의미 생략·축소·임의 요약은 불허. § 헤더 문단은 감사 대상 제외.
- JSON 원본은 수정하지 않음. 리포트만 작성.
- 심각도: [심각] 문단 전체 또는 핵심 논리 통째 누락 / [중간] 핵심 결론·경고·인용 누락 또는 의미 왜곡·근거 없는 추가 / [경미] 세부 축소·완화·일반화.

---

## Romans 1

### 이슈 1-1 [중간] KO 1절: 인사말이 EN과 전혀 다르고 로마 수신자 정보 누락
- 절 범위: 1
- MSG: "I, Paul, am a devoted slave of Jesus Christ on assignment, authorized as an apostle to proclaim God's words and acts. **I write this to all of you in Rome who are loved by God and called to belong to Jesus Christ.**"
- 현행 Teen EN: "This is Paul, and I'm on a mission for Jesus Christ. He's the real MVP, and I'm his hand-picked messenger, chosen to spread the word about God's awesome power. **I'm writing this to all of you in Rome who are on God's team—you belong to Jesus because he called you.**"
- 현행 Teen KO: "안녕, 얘들아? 나 바울임, 너네 친구이자 예수 그리스도의 종임. 사도로 직접 뽑혔고, 내 일은 하나님의 메시지를 모두랑 나누는 거임."
- 누락/문제: KO가 EN의 "로마에 있는 너네 모두에게 (하나님의 팀, 예수께 부름받아 속함)" 수신자 지정을 통째로 빼고, 대신 MSG/EN 어디에도 없는 "너네 친구이자"라는 정체성을 추가함. "안녕, 얘들아?"도 EN에 없음.
- 수정 방향: KO를 EN 문단과 1:1로 맞추기. "너네 친구이자" 삭제, "로마에 있는 너네 모두에게—하나님의 팀, 예수가 부르셔서 그분께 속한" 복원.

### 이슈 1-2 [심각] KO 문단 한 칸 밀림 → 26–27절 EN 내용 전체 누락
- 절 범위: 26–27
- MSG: "Worse followed. Refusing to know God, they soon didn't know how to be human either—women didn't know how to be women, men didn't know how to be men. Sexually confused, they abused and defiled one another. ... They paid for it, boy did they ever—God-forsaken, hard-hearted, and pointless."
- 현행 Teen EN: "And it got even worse. Since they refused to acknowledge God, they forgot how to be human. They got all mixed up, and their relationships became a total mess. It was all about lust, not love. And they paid the price for it, big time. They were empty, without God and without love—just a bunch of sad, lonely people."
- 누락/문제: KO 배지는 [18–23 / 1 / 2–7 / 8–12 / 13–15 / 16–17 / 18–23 / 24–25 / 26–27 / 28–32]인데, 실제 내용은 한 문단씩 밀려 있음. 배지 '24–25'인 KO 문단은 실제로 18–23 후반부 내용("그들은 하나님에 대해 알았지만, 하나님으로 대하지도 않았고 감사하지도 않았음…"), 배지 '26–27'인 KO 문단은 실제로 24–25 내용("그래서 하나님은 basically '그래, 니들 맘대로 해'라고 하시고…"). 결과적으로 26–27절의 EN 내용(관계의 혼란, lust not love, 대가 지불, godless/loveless)이 KO 어디에도 없음.
- 수정 방향: KO 문단을 EN과 같은 위치로 재정렬하고, 26–27절 KO 번역을 EN 기준으로 새로 추가.

### 이슈 1-3 [경미] EN 1절: "devoted slave" 정체성 축소
- 절 범위: 1
- MSG: "I, Paul, am a **devoted slave of Jesus Christ** on assignment, authorized as an apostle to proclaim God's words and acts."
- 현행 Teen EN: "This is Paul, and I'm on a mission for Jesus Christ. He's the real MVP, and I'm his hand-picked messenger…"
- 누락/문제: '사도'(hand-picked messenger)는 살렸지만 '예수 그리스도의 헌신된 종(slave)' 정체성이 빠짐.
- 수정 방향: "I'm his hand-picked messenger" 앞에 "a devoted servant of Jesus Christ" 뉘앙스 추가 검토.

### 이슈 1-4 [경미] EN 13–15절: 수신자 범위 일반화
- 절 범위: 13–15
- MSG: "I have an obligation to all, **Greeks and barbarians, the learned and the unlearned**…"
- 현행 Teen EN: "I feel like I owe it to everyone—no matter who they are—to share this message."
- 누락/문제: '예의 바른 자든 무례한 자든, 똑똑한 자든 단순한 자든'이라는 MSG의 구체적 범위가 "no matter who they are"로 일반화됨. 허용 가능한 teen-friendly 범위로 보이나 기록용으로 표기.
- 수정 방향: 유지 가능. 필요시 "smart or not, from the city or not" 정도로 구체성 보강.

---

## Romans 2

### 이슈 2-1 [중간] KO 1–2절: "하나님이 smoke screen을 꿰뚫으심" 결론 누락
- 절 범위: 1–2
- MSG: "…you are actually condemning yourself… **God sees right through that. He's not falling for your smoke and mirrors; he knows what you've been up to.**"
- 현행 Teen EN: "…You're just trying to distract from your own mess, **but God sees right through that. He's not falling for your smoke and mirrors; he knows what you've been up to.**"
- 현행 Teen KO: "자, 솔직해지자. 남들한테 손가락질하고 다니면, 넌 변명할 수 없음. 다른 사람을 판단할 때, basically 너 자신을 판단하는 거임, 너도 똑같은 짓을 하고 있으니까. 그 있잖아, '똥 묻은 개가 겨 묻은 개 나무란다'는 거."
- 누락/문제: EN의 마지막 결론 두 문장(하나님이 smoke screen을 꿰뚫고 네 행적을 아심)이 KO에 없음.
- 수정 방향: KO 문단 끝에 EN 결론 두 문장 번역 추가.

### 이슈 2-2 [중간] KO 3–4절 배지-내용 불일치: 4절 핵심 결론이 다른 문단에 있음
- 절 범위: 3–4
- MSG: "**God's kindness is meant to take you by the hand and lead you into a radical life-change.**"
- 현행 Teen EN (3–4): "You didn't actually think you could fool God, did you? … God is kind, for sure, but he's not soft. **He'll grab your hand and pull you into an amazing change, a complete life change.**"
- 현행 Teen KO (배지 3–4): "그런 짓 하는 사람들한테 하나님의 심판이 정당하다는 건 우리도 앎. 그래서, 진짜로 네가 빠져나갈 수 있다고 생각함? 남이 나쁜 짓 한다고 판단하면서, 너는 가서 똑같은 짓을 함? 그건 안 통함."
- 누락/문제: 배지 3–4인 KO 문단은 3절(심판 회피 불가)만 담고, 4절의 핵심 결론("친절이 급진적 삶의 변화로 이끄심")은 배지 5–8인 KO 문단에 있음("하나님의 친절은 너를 바꾸고 싶게 만들려는 거지…"). EN과 문단별 1:1이 깨짐.
- 수정 방향: KO 문단을 EN 위치에 맞게 재정렬. 4절 결론("친절→급진적 변화")은 배지 3–4 문단 안에.

### 이슈 2-3 [중간] EN 25–29절: 할례 역전 논리("지키지 않는 할례보다 지키는 무할례") 누락
- 절 범위: 25–29
- MSG: "…**Better to keep God's law uncircumcised than break it circumcised.** … The uncircumcised who keep God's ways are as good as the circumcised—in fact, better."
- 현행 Teen EN: "Being circumcised is a big deal if you're living God's way. But if you're not, it's meaningless. And if someone who isn't circumcised lives God's way, that's better than being circumcised and not. …"
- 누락/문제: EN은 "무할례자가 낫다"까지는 있으나, MSG의 명시적 명제 "할례받고 율법을 어기는 것보다 무할례로 율법을 지키는 게 낫다"와 '무할례자가 너를 판단할 것'이라는 역전 논리가 약화됨. 참고로 KO는 이 부분을 오히려 잘 살림("그러니까, 할례받지 않고 규칙을 지키는 사람들이 너를 판단할 거임").
- 수정 방향: EN에 "Better to keep God's law uncircumcised than break it circumcised" 뉘앙스 명시.

---

## Romans 3

### 이슈 3-1 [중간] EN 2–6절: 성경 인용 + 단호한 'No' 답변 + "하나님이 바로잡으심" 누락
- 절 범위: 2–6
- MSG: "…**Depend on it: God keeps his word even when the whole world is lying through its teeth. Scripture says the same: Your words stand fast and true; Rejection doesn't faze you.** But if our wrongdoing only underlines and confirms God's rightdoing, shouldn't we be commended for helping out? … These questions come up. **The answer to such questions is *no*, a most emphatic *No!* How else would things ever get straightened out if *God* didn't do the straightening?**"
- 현행 Teen EN: "They were the ones who got to be the keepers of God's message. But seriously, does our messing up make God unfaithful? Not at all. God's truth doesn't depend on us being good. But wait, if our misfits make God's goodness shine even brighter, then why are we in trouble for messing up? That's like saying it's our fault God looks good."
- 누락/문제: ① 성경 인용("Your words stand fast and true; Rejection doesn't faze you") 전체 누락 ② 질문에 대한 MSG의 단호한 답변("No, a most emphatic No!") 누락 ③ "'하나님'이 바로잡지 않으시면 어떻게 바로잡히겠는가" 결론 누락.
- 수정 방향: EN 문단에 인용구 복원 + "'No, a most emphatic No! How else would things get straightened out if God didn't do the straightening?" 뉘앙스 추가.

### 이슈 3-2 [중간] EN 7–8절: MSG에 없는 처벌 결론 추가 + 첫 번째 궤변 누락
- 절 범위: 7–8
- MSG: "**It's simply perverse to say, 'If my lies serve to show off God's truth all the more gloriously, why blame me? I'm doing God a favor.'** Some people are actually trying to put such words in our mouths, claiming that we go around saying, 'The more evil we do, the more good God does, so let's just do it!' **That's pure slander, as I'm sure you'll agree.**"
- 현행 Teen EN: "Some people have the audacity to claim that we go around saying, 'Let's do more bad stuff so God can do more good!' Uh, that's a terrible take and some pure hater energy. **Those people are gonna get exactly what's coming to them.**"
- 누락/문제: ① MSG의 첫 번째 궤변("내 거짓말이 하나님의 진리를 돋보이게 하니 오히려 하나님께 호의를 베푸는 것")이 빠짐 ② MSG에 없는 "그런 사람들은 받을 거 제대로 받을 거임"이라는 처벌 결론이 추가됨 (MSG는 "pure slander"라는 평가만 함).
- 수정 방향: 첫 번째 궤변 복원, 근거 없는 처벌 결론 삭제 또는 MSG 평가("pure slander")로 한정.

### 이슈 3-3 [심각] KO 21–24절: "모두가 죄지어 미치지 못함·순전한 선물·구출과 회복·예수를 통한 실행" 대거 누락
- 절 범위: 21–24
- MSG: "…**Since we've compiled this long and sorry record as sinners (both us and them) and proved that we are utterly incapable of living the glorious lives God wills for us, God did it for us. Out of sheer generosity he put us in right standing with himself. A pure gift. He got us out of the mess we're in and restored us to where he always wanted us to be. And he did it by means of Jesus Christ.**"
- 현행 Teen EN: "…We've all messed up and fallen short of God's glorious plan for our lives. But God, in his amazing generosity, decided to give us a fresh start. It's a total gift. He rescued us from the mess we were in and put us back on track. And he did it all through Jesus Christ."
- 현행 Teen KO: "근데 이제, 하나님이 일을 바로잡는 완전히 새 계획을 갖고 계심. 규칙 잔뜩 지키는 게 아님; 그분을 신뢰하는 거임. 옛 성경도 이 얘기를 했음. 하나님이 우리를 바르게 만드시는 길은 예수 그리스도를 믿는 믿음을 통하는 거고, 믿는 모든 사람을 위한 거임. 예외 없음."
- 누락/문제: EN의 ① "우리 모두 망쳤고 하나님의 영광스러운 계획에 미치지 못함" ② "놀라운 관대하심" ③ "완전한 선물" ④ "엉망에서 구출해 원래 자리로 회복" ⑤ "예수 그리스도를 통해 실행"이 KO에 없음.
- 수정 방향: KO를 EN 문장에 1:1로 번역. 다섯 요소 전부 복원.

### 이슈 3-4 [중간] KO 27–28절: "하나님은 우리가 하는 일에 반응하지 않으시고, 우리는 하나님이 하시는 일에 반응한다" 누락
- 절 범위: 27–28
- MSG: "What we've learned is this: **God does not respond to what *we* do; we respond to what *God* does.** We've finally figured it out."
- 현행 Teen EN: "We've learned that **God doesn't care about what we do; he cares about what he does.** We finally get it."
- 현행 Teen KO: "그래서, 이걸로 자랑할 수 있음? 없음. 그런 생각 자체가 취소됨. 규칙을 지켰기 때문임? 아님, 하나님을 신뢰했기 때문임. 우리가 알아낸 건 행동이 중요한 게 아님; 하나님이 우리를 바르게 만들어주실 거라고 신뢰하는 게 중요함. 그분이 이끄시게 하고, 우리는 따르면 됨."
- 누락/문제: EN/MSG의 핵심 명제("하나님은 우리가 하는 일에 반응하지 않으시고, 우리는 하나님이 하시는 일에 반응한다")가 KO에 없음. KO는 다른 말("행동이 중요한 게 아님; 신뢰가 중요함")로 대체.
- 수정 방향: KO에 핵심 명제 문장 복원.

### 이슈 3-5 [중간] KO 31절: "율법의 중요성을 드러내고 제자리에 둠" 누락
- 절 범위: 31
- MSG: "…Are we abolishing the law? **Absolutely not! We're putting the law in its proper place and showing how important it is.**"
- 현행 Teen EN: "…When we focus on what God has done, **we're actually showing how important those rules are. We're putting them in their proper place and showing that they all point to him.**"
- 현행 Teen KO: "그래서, 하나님을 신뢰한다는 건 규칙을 그냥 버려도 된다는 거임? 전혀 아님. 사실, 하나님을 신뢰하는 게 규칙을 이해하게 만드는 거임."
- 누락/문제: EN의 "율법이 얼마나 중요한지 드러내고, 제자리에 두며, 다 그분을 가리킨다는 것을 보임"이 KO에서 "신뢰하는 게 규칙을 이해하게 만듦"으로 축소·대체됨.
- 수정 방향: KO에 "율법의 중요성을 드러내고 제자리에 두며 그분을 가리킴" 복원.

---

## Romans 4

### 이슈 4-1 [심각] EN/KO 6–9절 인용문: "용서받은 죄인"이 "바르게 사는 사람"으로 왜곡
- 절 범위: 6–9
- MSG: "**Fortunate those whose crimes are whisked away, whose sins are wiped clean from the slate.** Fortunate the person against whom the Lord does not keep score."
- 현행 Teen EN: "> **Lucky are the people who do the right thing,** who get their bad stuff erased, who have their sins forgiven. Lucky is the person whose sin God doesn't even count."
- 누락/문제: MSG 인용의 주어는 '범죄가 휩쓸려 가고 죄가 깨끗이 지워진' **용서받은 죄인**인데, EN 첫 줄이 "do the right thing(바르게 사는 사람)"으로 바뀌어 축복의 대상이 선행으로 의로워지는 사람처럼 읽힘. 의미 반전 수준의 왜곡. KO도 동일하게 따름.
- 수정 방향: EN/KO 첫 줄을 "Lucky are the people whose crimes are whisked away" / "범죄가 휩쓸려 가버린 사람들은 운이 좋음" 뉘앙스로 정정.

### 이슈 4-2 [심각] KO 13–15절: 약속-계약/fine print 논리 통째 누락, 다른 논리로 대체
- 절 범위: 13–15
- MSG: "…**If those who get what God gives them only get it by doing everything they are told to do and filling out all the right forms properly signed, that eliminates personal trust completely and turns the promise into an ironclad *contract*! That's not a holy promise; that's a business deal. A contract drawn up by a hard-nosed lawyer and with plenty of fine print only makes sure that you will never be able to collect. But if there is no contract in the first place, simply a *promise*—and God's promise at that—you can't break it.**"
- 현행 Teen EN: "…If getting God's gifts was all about following a long list of rules and filling out paperwork, it would kill the whole trust thing and turn it into a business deal. That's not a promise; that's a contract with a bunch of fine print designed to trip you up. But with a promise, especially one from God, you can't break it."
- 현행 Teen KO: "아브라함에게 하신 하나님의 약속은 규칙 잔뜩 지키는 것에 대한 게 아니었음. 아브라함이 하나님을 신뢰하고, 하나님이 그를 바르게 만드시는 것에 대한 거였음. 약속이 규칙을 완벽하게 지키는 사람들만의 거였다면, 믿음은 무의미하고 약속은 가치없어졌을 거임. **규칙은 우리가 어디서 망치는지만 보여줌; 오히려 더 어기고 싶게 만듦.**"
- 누락/문제: KO가 EN의 핵심 논리(계약 vs 약속, fine print로 못 받게 만드는 계약, 약속은 깰 수 없음)를 통째로 빼고, 다른 장(7장)의 논리인 "율법이 실패를 보여주고 더 어기고 싶게 만든다"를 대신 넣음. EN 논리와 무관한 대체.
- 수정 방향: KO 마지막 두 문장을 삭제하고 EN의 계약/fine print/깰 수 없는 약속 논리로 1:1 번역.

### 이슈 4-3 [중간] KO 17–18절: "nobody→somebody", "아버지라 먼저 불림" 등 대거 축약
- 절 범위: 17–18
- MSG: "…**Abraham was first named 'father' and then *became* a father because he dared to trust God to do what only God could do: raise the dead to life, with a word make something out of nothing.**"
- 현행 Teen EN: "We call Abraham 'father' **not because he was some perfect saint, but because God took a nobody and made him a somebody.** … **Abraham was called a father *before* he even had kids because he dared to believe God could do the impossible,** like bringing the dead back to life or creating something out of nothing. **When everything looked hopeless, Abraham still believed. He chose to focus on what God *said* he would do, not on what he *couldn't* do. And that's how he became the father of a massive family.**"
- 현행 Teen KO: "성경이 말한 것처럼: '너를 많은 민족의 아버지로 만들었음.' 아브라함은 죽은 것을 살리시고 없는 것에서 만드시는 하나님을 신뢰했음. 하나님이 '네 후손이 엄청 많아질 거야'라고 말씀하셨을 때, 불가능해 보였는데도 아브라함은 믿었음."
- 누락/문제: EN의 ① "완벽한 성인이어서가 아니라 nobody를 somebody로 만드셨기 때문" ② "아이도 없을 때 먼저 아버지라 불림" ③ "절망적 상황에서도 믿고, 하나님이 말씀하신 것에 집중함" ④ "그렇게 대가족의 아버지가 됨"이 KO에 없음.
- 수정 방향: KO를 EN 문장별로 1:1 번역. 네 요소 전부 복원.

### 이슈 4-4 [경미] EN 16절: "not our ancestor" — 문맥상 허용 가능하나 기록
- 절 범위: 16
- MSG: "…That's the only way everyone can be sure to get in on it, those who keep the religious traditions *and* those who never heard of them. **For Abraham is father of us all.**"
- 현행 Teen EN: "…**Abraham is the father of our faith, not our ancestor.**"
- 누락/문제: 문장 전체로 읽으면 '혈통이 아닌 믿음의 아버지' 취지가 전달되어 허용 가능한 teen-friendly 표현으로 판정. 단독 인용 시 오해 소지가 있어 기록용으로 표기.
- 수정 방향: 유지 가능. 필요시 "not our ancestor by blood"로 명확화.

---

## Romans 5

### 이슈 5-1 [중간] KO 1–2절: "서로 열린 문·넓은 은혜의 공간·서서 찬양" 비유 축소
- 절 범위: 1–2
- MSG: "…**we throw open our doors to God and discover at the same moment that he has already thrown open his door to us. We find ourselves standing where we always hoped we might stand—out in the wide open spaces of God's grace and glory, standing tall and shouting our praise.**"
- 현행 Teen EN: "…We can now just walk right up to God, and **he's already there with open arms. We're out in the wide-open spaces of God's grace and glory, standing tall and shouting out his praises.**"
- 현행 Teen KO: "자, 이제 그분을 신뢰해서 하나님과 잘 됐으니, 편하게 있을 수 있음. 예수 그리스도를 통해 하나님과 평화를 얻었음. **하나님의 은혜로 가는 문이 열려 있고, 우리가 그 안에 서 있음. 그냥 서 있는 게 아님; 뭐가 올지 아니까 축하하고 있음. 하나님의 영광을 가까이서 보게 될 거임.**"
- 누락/문제: EN의 ① "하나님이 이미 열린 팔로 계심"(상호 열린 문) ② "넓은 은혜와 영광의 공간에 우뚝 서서 찬양을 외침"이 KO에서 "문이 열려 있고 서 있음… 축하하고 있음… 영광을 가까이서 보게 될 거임"으로 약화.
- 수정 방향: KO에 "열린 팔로 계신 하나님", "우뚝 서서 찬양을 외침" 복원.

### 이슈 5-2 [중간] KO 3–5절: "고난 중 찬양"→"문제 때문에 설렘" 변경, patience→virtue→expectancy 논리 재구성
- 절 범위: 3–5
- MSG: "**We continue to shout our praise even when we're hemmed in with troubles, because we know how troubles can develop passionate patience in us, and how that patience in turn forges the tempered steel of virtue, keeping us alert for whatever God will do next.** In alert expectancy such as this, we're never left feeling shortchanged. **Quite the contrary—we can't round up enough containers to hold everything God generously pours into our lives through the Holy Spirit!**"
- 현행 Teen EN: "But wait, there's more. **We even shout praises when we're going through tough times.** Why? Because we know that **our struggles help us build up some serious patience. And that patience? It forges us into people with real character, always ready for what God's gonna do next.** And with that kind of attitude, we're never let down. …"
- 현행 Teen KO: "그리고 그게 다가 아님. **우리는 사실 문제들 때문에 설렘.** 이상하게 들리지? 근데 **문제는 계속 나아가게 가르쳐주고, 계속 나아가는 건 우리를 더 강하게 만듦. 그리고 강해지는 건 실망시키지 않는 소망을 줌.** 실망하지 않을 거임, 하나님의 사랑이 우리 위에 가득하니까. **성령님은 우리 마음에 터진 하나님의 사랑 폭탄 같은 거임.**"
- 누락/문제: ① "고난 중에도 찬양을 외침"이 "문제들 때문에 설렘"으로 변경 (고난 자체를 즐기는 것처럼 읽힘) ② patience→virtue(단련된 강철 같은 덕)→expectancy(하나님이 다음에 하실 일을 향한 깨어 있음) 논리가 "문제→계속 나아감→강해짐→소망"으로 재구성되어 virtue와 expectancy 탈락 ③ "성령을 통해 하나님이 우리 삶에 관대하게 부으시는 모든 것"이 "우리 마음에 터진 하나님의 사랑 폭탄"으로 바뀌어 성령의 부으심 주체성 약화.
- 수정 방향: KO를 EN 문장별로 1:1 번역. "고난 중에도 찬양", "patience→품성→기대" 논리, "성령을 통해 부으심" 복원.

### 이슈 5-3 [중간] KO 9–11절: "부활 생명으로 삶이 확장·심화" → 일반적 "구원"으로 변경
- 절 범위: 9–11
- MSG: "If, when we were at our worst, we were put on friendly terms with God **by the sacrificial death of his Son**, now that we're at our best, **just think of how our lives will expand and deepen by means of his resurrection life!**"
- 현행 Teen EN: "If we became friends with God **when we were at our absolute worst**, just imagine **how much our lives are gonna change now that we're on his team!** …"
- 현행 Teen KO: "우리가 최악일 때 하나님과 친구가 됐다면, 이제 친구가 된 게 어떨지 상상해 봐. **구원받을 거임, 의심 없음.** 그냥 구원받는 게 아님; 메시아 예수님을 통해 하나님께 찬양을 노래하고 외칠 거임! 그분이 이 우정을 만들어주신 분임."
- 누락/문제: ① "아들의 희생적 죽음으로" 화목케 됨이 빠짐 ② "부활 생명으로 삶이 확장되고 깊어진다"가 "구원받을 거임, 의심 없음"이라는 일반적 구원 진술로 변경.
- 수정 방향: KO에 "아들의 희생적 죽음으로", "부활 생명으로 삶이 확장·심화" 복원.

---

## Romans 6

### 이슈 6-1 [심각] KO 6–11절: EN 후반부 전체 누락
- 절 범위: 6–11
- MSG: "**We know that when Jesus was raised from the dead it was a signal of the end of death-as-the-end. Never again will death have the last word. When Jesus died, he took sin down with him, but alive he brings God down to us.** From now on, think of it this way: **Sin speaks a dead language that means nothing to you; God speaks your mother tongue, and you hang on every word. You are dead to sin and alive to God. That's what Jesus did.**"
- 현행 Teen EN: "…We know that when Jesus came back from the dead, **it was the ultimate mic drop on death itself. Death doesn't get the final say anymore. When Jesus died, he took sin down with him. But now that he's alive, he connects us directly to God.** So from now on, think of it like this: **sin is a dead language, it's totally irrelevant to you. But God? He's speaking your language, and you should be hanging on every word. You're done with sin and totally alive for God.** That's the life Jesus gives you—dead to sin and alive to God."
- 현행 Teen KO: "이거 완전 당연한 거 아님? 우리의 옛 삶은 그리스도와 함께 십자가에 못 박혔음. 그 비참하고 죄로 가득한 삶은 끝났음. 더 이상 죄한테 휘둘리지 않음! 우리는 믿음. 그리스도의 죽음은 죄를 이긴 죽음이라는 걸. 우리가 그 죽음에 동참했다면, 당연히 그분의 부활, 생명을 구원하는 그 부활에도 동참하는 거임."
- 누락/문제: KO가 EN 전반부(옛 삶이 십자가에 못 박힘)까지만 번역하고, "죽음이 마지막 말을 하지 못함 / 예수가 죄를 끌어내리고 살아나서 하나님을 우리에게 가져옴 / 죄의 죽은 언어 vs 하나님의 모국어 / 죄에 대해 죽고 하나님께 살아 있음" 전체가 빠짐.
- 수정 방향: KO 후반부를 EN 기준으로 전부 번역 추가.

### 이슈 6-2 [중간] EN 15–18절: "새 주인의 명령이 자유롭게 한다" 결론 축소
- 절 범위: 15–18
- MSG: "…**But thank God you've started listening to a new master, one whose commands set you free to live openly in his freedom!**"
- 현행 Teen EN: "…If you hand yourself over to sin, it becomes your boss. But if you follow God, you get freedom that never runs out."
- 누락/문제: MSG의 핵심 결론 "새 주인을 듣기 시작했는데, 그분의 명령이 너를 자유롭게 하여 그분의 자유 안에서 활짝 살게 한다"가 "하나님을 따르면 절대 안 떨어지는 자유를 얻음"으로 축소. "명령이 자유롭게 한다"는 역설적 포인트 소실.
- 수정 방향: EN에 "새 주인의 명령이 너를 자유롭게 해서 활짝 살게 한다" 뉘앙스 복원.

### 이슈 6-3 [중간] EN 19절: "타인·하나님께 끼친 피해" + "이기적 습관의 노예" 누락
- 절 범위: 19
- MSG: "…**how at one time the more you did just what you felt like doing—not counting the cost, the damage wrought to others and to God—you actually became less and less free? Or how you gradually became a slave to your own selfish habits**—not thinking about how they hurt others or God—**and so lost the ability to live free?**"
- 현행 Teen EN: "Think about it: back when you did whatever you felt like, you thought you were free, but your freedom shrank. And look at you now. You're a totally different person, and your life is wide open."
- 누락/문제: "타인과 하나님께 끼친 피해를 헤아리지 않음", "이기적 습관의 노예가 되어 자유롭게 살 능력을 잃음"이 빠짐.
- 수정 방향: EN에 두 요소 복원.

### 이슈 6-4 [경미] EN 20–21절: "right thinking/right living", "부끄러움" 압축
- 절 범위: 20–21
- MSG: "As long as you did what you felt like doing, ignoring God, **you didn't have to bother with right thinking or right living, or right *anything* for that matter.** But do you call that a free life? What did you get out of it? **Nothing you're proud of now.** Where did it get you? A dead end."
- 현행 Teen EN: "What did all that wild living get you? What was the payoff? Nothing. It was a dead end."
- 누락/문제: "바른 생각·바른 삶·바른 그 무엇에도 신경 안 씀", "지금 자랑스러워할 만한 게 하나도 없음(부끄러움)"이 빠짐.
- 수정 방향: EN에 "right thinking/right living" 나열과 "nothing you're proud of" 뉘앙스 보강.

---

## Romans 7

### 이슈 7-1 [중간] EN/KO 1–3절: 결혼 비유의 전반부(간음 조항) 누락
- 절 범위: 1–3
- MSG: "…For instance, a wife is legally bound to her husband while he's alive, but if her husband dies, she is set free from that law. **If she marries another man while her husband is still alive, she is called an adulteress;** but if her husband dies, she is free of that law, and if she marries another man, she is not an adulteress."
- 현행 Teen EN: "Okay, real talk. You know how rules only apply to the living, right? Like, if a married woman's husband dies, she's not bound by the marriage rules anymore. She's free."
- 누락/문제: 비유의 전반부(남편이 살아 있는데 다른 남자와 살면 간음)가 빠지고 후반부(남편 사망 시 자유)만 있음. 4절 적용("율법에 대해 죽고 다른 이에게 속함")을 이해하는 데 필요한 대비 구조가 반쪽.
- 수정 방향: EN/KO에 "남편이 살아 있을 때 다른 남자와 살면 간음이라 불림" 전반부 복원.

### 이슈 7-2 [중간] EN/KO 8–12절: "율법 없이는 죄가 무기력해 보였음" 누락
- 절 범위: 8–12
- MSG: "…**Without all the paraphernalia of the law code, sin looked pretty dull and lifeless, and I went along without paying much attention to it.** But once sin got its hands on the law code and decked itself out in all that finery, I was fooled, and fell for it."
- 현행 Teen EN: "But sin is sneaky. It used that good rule and turned it into a temptation, like a 'forbidden fruit' situation. So the rule that was supposed to help me ended up tripping me up. Sin was having a party, and I was basically dead inside. The rules themselves are good, though. They're like God's common sense."
- 누락/문제: "율법의 장식 없이 죄는 따분하고 무기력해 보였고, 나도 별 신경 안 썼다"는 대비 요소가 빠짐. 죄가 율법을 차려입고 속였다는 MSG의 핵심 묘사 약화.
- 수정 방향: EN/KO에 해당 대비 문장 복원.

### 이슈 7-3 [중간] EN/KO 14–16절: "죄의 감옥에 오래 있었음" + "하나님 명령이 필요하다는 결론" 누락
- 절 범위: 14–16
- MSG: "…**Yes. I'm full of myself—after all, I've spent a long time in sin's prison.** What I don't understand about myself is that I decide one way, but then I act another, doing things I absolutely despise. **So if I can't be trusted to figure out what is best for myself and then do it, it becomes obvious that God's command is necessary.**"
- 현행 Teen EN: "I know God's commands are the real deal, but I'm just...not. I'm a mess. I decide to do one thing, and then I do the complete opposite. I do stuff I totally hate. There's like a glitch in my system."
- 누락/문제: ① "죄의 감옥에 오래 있었다"는 자기 진단 빠짐 ② "내 판단을 믿을 수 없으니 하나님의 명령이 필요하다"는 결론 빠짐.
- 수정 방향: EN/KO에 두 요소 복원.

### 이슈 7-4 [중간] EN/KO 17–20절: "My choices don't even matter" 의미 왜곡 + "도움이 필요함" 결론 누락
- 절 범위: 17–20
- MSG: "**But I need something *more*! For if I know the law but still can't keep it, and if the power of sin within me keeps sabotaging my best intentions, I obviously need help!** I realize that I don't have what it takes. I can will it, but I can't *do* it. … **My decisions, such as they are, don't result in actions.** Something has gone wrong deep within me and gets the better of me every time."
- 현행 Teen EN: "It's not really me; it's the sin living inside me. I want to do good, but I just can't. **My choices don't even matter.** Something deep inside me is sabotaging me every single time."
- 누락/문제: ① MSG의 "결정이 행동으로 이어지지 않는다"가 "내 선택은 아무 의미도 없음"으로 과도하게 확장되어 허무주의적으로 읽힘 (의미 왜곡) ② "나는 뭔가 *더* 필요해! … 분명히 도움이 필요해!"라는 결론 빠짐.
- 수정 방향: "My choices don't even matter"를 "My decisions don't result in actions" 취지로 정정하고, "I obviously need help" 결론 복원. KO도 동일 수정.

### 이슈 7-5 [경미] EN/KO 21–23절: "하나님의 명령을 진심으로 기뻐함" 누락
- 절 범위: 21–23
- MSG: "…**I truly delight in God's commands,** but it's pretty obvious that not all of me joins in that delight. Parts of me covertly rebel, and just when I least expect it, they take charge."
- 현행 Teen EN: "It's so predictable. Every time I want to do the right thing, something inside me wants to do the opposite. It's like there's a secret rebel living in me that takes over when I least expect it."
- 누락/문제: "나는 하나님의 명령을 진심으로 기뻐한다"는 내적 갈등의 한 축이 빠지고 반란만 남음.
- 수정 방향: EN/KO에 "I truly delight in God's commands" 복원.

---

## Romans 8

### 이슈 8-1 [심각] KO 문단 밀림 → 9–11절 내용 통째 누락
- 절 범위: 9–11
- MSG: "**If someone doesn't have the Spirit of Christ, they're not on the team. But for you who have the Spirit, even though your body is dead because of sin, you're living on God's terms. And if the same God who brought Jesus back from the dead is living in you, he's going to give you a powerful shift and bring you to life too.**"
- 현행 Teen EN: "But if God is living in you, you're not thinking about yourself all the time. **If someone doesn't have the Spirit of Christ, they're not on the team.** But for you who have the Spirit, even though you still mess up, you're living on God's terms. **And if the same God who brought Jesus back from the dead is living in you, he's going to give you a powerful shift and bring you to life too. With his Spirit in you, you're as alive as Christ!**"
- 누락/문제: KO 배지는 9–11이지만 실제 내용은 5–8절 것("혼자 할 수 있다고 생각하는 사람들은 자기 도덕적 근육 재는 데 집착…"). KO 어디에도 9–11절 내용(그리스도의 영이 없으면 팀이 아님 / 죽은 몸이지만 하나님의 조건으로 삶 / 예수를 살리신 하나님이 너도 살리심)이 없음.
- 수정 방향: KO 문단 재정렬(배지 5–8 문단은 5–8 내용, 배지 9–11 문단은 9–11 내용) 후 9–11절 KO 번역 추가.

### 이슈 8-2 [심각] KO 29–30절: 예정·부르심·의롭다 하심·영화롭게 하심 통째 누락
- 절 범위: 29–30
- MSG: "**God knew what he was doing from the very beginning. He decided from the outset to shape the lives of those who love him along the same lines as the life of his Son. The Son stands first in the line of humanity he restored. We see the original and intended shape of our lives there in him. After God made that decision of what his children should be like, he followed it up by calling people by name. After he called them by name, he set them on a solid basis with himself. And then, after getting them established, he stayed with them to the end, gloriously completing what he had begun.**"
- 현행 Teen EN: "God had a plan from the beginning. He decided to make us like his Son, Jesus. Jesus is the first in a new line of awesome humans. After God chose us, he called us, made us right with him, and he'll stick with us to the end. He's going to finish the amazing work he started in us."
- 현행 Teen KO (배지 29–30): "그래서 우리는 하나님을 사랑하는 우리 삶의 모든 디테일이 선한 것으로 만들어진다는 걸 확신할 수 있음."
- 누락/문제: 배지 29–30인 KO 문단이 실제로는 28절 꼬리("모든 디테일이 선으로 만들어진다")만 담고, 29–30절 내용(처음부터 계획, 아들의 모습으로 빚으심, 이름으로 부르심, 바르게 세우심, 끝까지 완성하심)이 KO 어디에도 없음.
- 수정 방향: KO 29–30 문단을 EN 기준으로 새로 번역.

### 이슈 8-3 [중간] KO 26–28절: "하나님을 사랑하는 자들에게 모든 것이 선으로" 결론 누락
- 절 범위: 26–28
- MSG: "…**That's why we can be so sure that every detail in our lives of love for God is worked into something good.**"
- 현행 Teen EN: "…He knows us better than we know ourselves and makes sure we're good with God. **That's why we can be sure that God works everything out for the best for those who love him.**"
- 현행 Teen KO: "한편, 기다리다 지치는 순간, 하나님의 영이 바로 옆에서 우리를 도와주심. … 그분은 우리가 우리 자신을 아는 것보다 우리를 훨씬 더 잘 아시고, 우리의 임신한 상태를 아시고, 우리를 하나님 앞에 있게 하심."
- 누락/문제: 28절의 유명한 결론("하나님을 사랑하는 우리 삶의 모든 디테일이 선으로 엮인다")이 KO에 없음. KO는 EN의 마지막 문장을 통째로 빼먹음.
- 수정 방향: KO 문단 끝에 해당 결론 번역 추가.

### 이슈 8-4 [중간] EN 18–21절: 피조물의 억제·동시 해방 설명 과도 축약
- 절 범위: 18–21
- MSG: "…**The created world itself can hardly wait for what's coming next. Everything in creation is being more or less held back. God reins it in until both creation and all the creatures are ready and can be released at the same moment into the glorious times ahead.**"
- 현행 Teen EN: "Honestly, the hard times we're going through now are nothing compared to the awesome future that's coming. **All of creation is waiting for it.**"
- 누락/문제: "피조물이 (하나님께) 억제되어 있다가, 피조물과 사람들이 함께 영광의 때에 풀려난다"는 설명이 "All of creation is waiting" 한 문장으로 축소.
- 수정 방향: EN에 "held back / reined in / released together into the glorious times" 뉘앙스 복원.

### 이슈 8-5 [중간] EN 22–25절: "성령이 우리 안에서 깨우심" + "메마른 몸의 해방 갈망" 누락
- 절 범위: 22–25
- MSG: "…**The Spirit of God is arousing us within. We're also feeling the birth pangs. These sterile and barren bodies of ours are yearning for full deliverance.** That is why waiting does not diminish us, it enlarges us."
- 현행 Teen EN: "It's like the whole world is pregnant and about to give birth to something amazing. And we feel it too. We're waiting for our own life-changing moment, to be totally free. Waiting doesn't make us weaker; it makes us stronger and more excited."
- 누락/문제: "하나님의 영이 우리 안에서 우리를 깨우심", "불임의 메마른 몸이 완전한 해방을 갈망함"이 빠짐.
- 수정 방향: EN에 두 요소 복원.

### 이슈 8-6 [경미] EN/KO 3–4절: Band-Aid 비유 후반부 KO 배지 밀림 (8-1과 연계)
- 절 범위: 3–4
- MSG: "…**The law always ended up being used as a Band-Aid on sin instead of dealing with sin. But now what the law code asked for but we couldn't deliver is accomplished as we, instead of redoubling our own efforts, simply embrace what the Spirit is doing in us.**"
- 현행 Teen EN: "…The old rules were like a weak Band-Aid on a massive wound – they just couldn't fix the deep problem of sin. **But now, the Spirit is doing for us what we could never do for ourselves. We just have to trust him.**"
- 누락/문제: EN은 완전하나, KO는 "성령이 우리를 위해 하심" 결론이 배지 5–8인 문단에 들어가 있어 배지-내용 불일치. 이슈 8-1의 문단 재정렬 시 함께 해결.
- 수정 방향: KO 문단 재정렬로 해결.

---

## Romans 9

### 이슈 9-1 [심각] EN/KO 20–33절: 이사야의 "소돔과 고모라 유령 도시" 인용 전체 누락
- 절 범위: 29
- MSG: "**Isaiah had looked ahead and spoken the truth: If our powerful God had not provided us a legacy of living children, we would have ended up like ghost towns, like Sodom and Gomorrah.**"
- 현행 Teen EN (20–33 세 문단 전체): 이사야 인용으로 "God can take a bunch of nobodies and make them somebodies… 'children of the living God'"(호세아), "even if a ton of Israelites were chosen, only a few would actually be saved. God doesn't just count heads; He calls us by name"(이사야 27–28), "Watch out, I'm putting a huge stone in your path…"(이사야 33)만 있고, 29절의 "살아 있는 자녀들의 유산 / 소돔과 고모라 같은 유령 도시" 인용이 세 문단 어디에도 없음.
- 누락/문제: MSG unit [20–33]의 인용문 하나가 통째로 빠짐. Teen 세 문단을 합쳐도 복원 불가.
- 수정 방향: EN 두 번째 문단(이사야 인용 부분)에 29절 인용 추가. KO도 동일.

### 이슈 9-2 [경미] EN 20–22절: "angry displeasure" → "power" 완화
- 절 범위: 20–22
- MSG: "If God needs one style of pottery **especially designed to show his angry displeasure** and another style carefully crafted to show his glorious goodness, isn't that all right?"
- 현행 Teen EN: "He can use some people to **show his power** and others to show his amazing goodness."
- 누락/문제: "진노(angry displeasure)를 보여주기 위한 그릇"이 "능력을 보여주기 위한"으로 완화됨.
- 수정 방향: "show his power"를 "show his anger/wrath" 뉘앙스로 정정 검토.

(예비 후보였던 "27–28절 numbers not names 표현 변경"은 재확인 결과 EN이 MSG를 충실히 살림 — 이슈 없음.)

---

## Romans 10

### 이슈 10-1 [중간] KO 1–3절: DIY 구원 상점 비유·결론 누락
- 절 범위: 1–3
- MSG: "…**Right across the street they set up their own salvation shops and noisily hawk their wares.** Instead of following God's way of getting right with God, they insist on setting up their own get-right-with-God shop. … **How can they think that such a do-it-yourself program, this so-called 'I'm doing my best' religion, is ever going to bring them any good? They go through all the motions, but they don't get anywhere.**"
- 현행 Teen EN: "…**They've set up their own little 'salvation stores' selling fakes, when God's got the real deal right there. They've been trying to do it their own way for ages, and they've got nothing to show for it.**"
- 현행 Teen KO: "형제자매들아, 내 마음의 소원은 이스라엘 사람들이 구원받는 거임. 그들을 위해 항상 하나님께 기도함. 그들이 하나님에 대해 엄청 열정적인 건 알지만, 포인트를 놓치고 있음. 하나님이 사람들을 어떻게 바르게 만드시는지 이해 못 함. 하나님의 길 대신 자기들 방식대로 하려고 함."
- 누락/문제: EN의 ① "가짜 파는 구원 상점" 비유 ② "하나님께는 진짜가 바로 거기 있음" ③ "오랫동안 자기 방식대로 했지만 남은 게 없음" 결론이 KO에 없음.
- 수정 방향: KO에 세 요소 번역 추가.

### 그 외 4–21절: 이슈 없음
- EN/KO 모두 MSG의 모세 인용, "Jesus is the boss" 고백, "No one who trusts God will ever regret it", "Everyone who calls gets help", 믿음-들음-전함 사슬, 이사야 인용들을 충실히 보존. KO도 EN과 1:1 대응.

---

## Romans 11

### 이슈 11-1 [중간] EN 25–29절 꼬리 + 30–32절 병합: MSG 두 unit이 Teen 한 문단에 합쳐짐 (성욱 컨펌 필요)
- 절 범위: 25–29 꼬리, 30–32
- MSG [25–29] 꼬리: "**From your point of view as you hear and embrace the good news, they look like God enemies, which they are. But from God's point of view in terms of the big picture, they are old friends of his, loved because of the big promise made to their ancestors. God's gifts and his call are irrevocable.**"
- MSG [30–32]: "In the past the outsiders were on the outside of God, but now, because of the Jews' rejection, they are on the inside. … Now the Jews are on the outside, but because the door is wide open to you, they have a way back in. … God makes sure that everyone experiences the outsider condition so that he can be the one to welcome them all back in."
- 현행 Teen EN (배지 30–32): "**From your perspective, it might look like the Jews are God's enemies. But from God's long-term view, they're still his oldest friends. God's gifts and his call are for life—no take-backs.** Not long ago, you were the ones on the outs with God. But then the Jews slammed the door on him, and that opened things up for you. Now they're on the outs, but because the door is wide open for you, they have a way back in. God makes sure everyone knows what it's like to be on the outside so he can be the one to welcome us all back in."
- 누락/문제: MSG의 25–29 꼬리("원수처럼 보이지만 장기적으로는 오래된 친구, 선물과 부르심은 취소 불가")가 배지 25–29인 EN 문단에는 없고, 배지 30–32인 문단에 30–32 내용과 병합되어 있음. 번역 5대 원칙상 MSG 문단 병합(merge)은 성욱 컨펌이 필요하므로, 이 구조는 컨펌 대상으로 별도 표시해야 함.
- 수정 방향: 현 구조 유지 시 성욱 컨펌 필요. 또는 25–29 꼬리를 배지 25–29 문단으로 이동하고 30–32 문단은 30–32만 담도록 분리.

### 이슈 11-2 [심각] KO 30–32절: 30–32절 내용 전체 누락 (25–29 꼬리만 있음)
- 절 범위: 30–32
- MSG [30–32]: (위 인용 참조) — "과거 비유대인이 밖에 있었음 / 유대인의 거절로 문이 열림 / 지금 유대인이 밖에 있지만 돌아올 길이 있음 / 모두가 밖에 있음을 경험하고 하나님이 환영하심"
- 현행 Teen EN (배지 30–32): (위 인용 참조 — 25–29 꼬리 + 30–32 전체 포함)
- 현행 Teen KO (배지 30–32): "좋은 소식에 관한 한, 그들은 너네를 위해 원수임. 근데 하나님의 선택에 관한 한, 족장들 때문에 사랑받음. 하나님의 선물과 부르심은 취소될 수 없음."
- 누락/문제: KO는 EN 문단의 앞부분(25–29 꼬리)만 번역하고, 정작 배지가 가리키는 30–32절 내용("너네가 밖에 있었음→문이 열림→그들도 돌아올 길이 있음→모두를 환영하심")이 통째로 없음.
- 수정 방향: KO에 EN 후반부(30–32 내용) 번역 추가.

### 그 외 1–24, 33–36절: 이슈 없음
- 엘리야 7천 명, 남은 자, 올리브 접붙이기, "온 이스라엘이 구원받을 것", 시온의 구원자 인용, 33–36절 송영 모두 EN/KO 충실.

---

## Romans 12

### 이슈 12-1 [심각] KO 3절: "선함은 우리가 하나님께 가져가는 게 아님" 핵심 명제 통째 누락
- 절 범위: 3
- MSG: "…**it's important that you not misinterpret yourselves as people who are bringing this goodness to God. No, God brings it all to you. The only accurate way to understand ourselves is by what God is and by what he does for us, not by what we are and what we do for him.**"
- 현행 Teen EN: "…don't get it twisted and think you're the one doing all the good stuff. **Nah, that's all God. The only way to really get who you are is to see who God is and what He does for you, not what you do for Him.**"
- 현행 Teen KO: "하나님이 내게 주신 모든 것에 대한 깊은 감사로, 특히 대조를 위해 너네한테 말함. 너네 각자가 하나님이 주신 걸 잘 들여다봤으면 좋겠음. 막 드라마틱하게 굴 필요 없음. 네가 누군지에 대해 솔직해져. 하나님이 우리 각자에게 다른 선물을 주셨으니, 아닌 척하지 말자."
- 누락/문제: EN/MSG의 핵심 명제("네가 하나님께 선을 가져가는 게 아니라 하나님이 네게 가져오심; 자기를 이해하는 유일한 정확한 방법은 하나님이 누구시고 무엇을 하시는지")가 KO에 없고, 전혀 다른 내용("네가 누군지 솔직해져, 아닌 척하지 말자")으로 대체됨.
- 수정 방향: KO를 EN에 1:1로 다시 번역. 핵심 명제 두 문장 복원.

### 이슈 12-2 [심각] KO 4–6절: 몸 비유 전반부 누락 + 은사 목록을 앞당김
- 절 범위: 4–6
- MSG: "**In this way we are like the various parts of a human body. Each part gets its meaning from the body as a whole, not the other way around.** The body we're talking about is Christ's body of chosen people. … **But as a chopped-off finger or cut-off toe we wouldn't amount to much, would we?** So since we find ourselves fashioned into all these excellently formed and marvelously functioning parts in Christ's body, **let's just go ahead and be what we were made to be, without enviously or pridefully comparing ourselves with each other, or trying to be something we aren't.**"
- 현행 Teen EN: "Think of it like this: we're all different parts of a body. Each part is important, but only because it's part of the whole body. That body is Team Jesus. … **A finger or a toe by itself is pretty useless, right?** … let's just be who we were made to be. **No need to get jealous or braggy, or try to be someone you're not.**"
- 현행 Teen KO: "이렇게 생각해 봐: 우리는 모두 한 몸의 일부지만, 모두 같은 부분은 아님. 할 일이 다름. 그러니까, 하나님이 주신 선물을 쓰자. 하나님의 메시지를 전하는 선물이 있으면, 네 믿음에 맞게 써. 돕는 선물이 있으면, 도와. 선생이면, 가르쳐."
- 누락/문제: KO가 EN의 몸 비유 핵심(부분은 전체로부터 의미를 얻음, 잘린 손가락·발가락은 무용지물, 비교하지 말고 만들어진 대로 살자)을 빼고, 다음 문단(6–8절)의 은사 목록을 앞당겨 넣음. 문단 경계 붕괴.
- 수정 방향: KO 4–6 문단은 EN 몸 비유로 1:1 번역. 은사 목록은 6–8 문단으로.

### 이슈 12-3 [심각] KO 6–8절: 은사 목록 절반 + 태도 경고 전부 누락
- 절 범위: 6–8
- MSG: "**If you preach, just preach God's Message, nothing else; if you help, just help, don't take over; if you teach, stick to your teaching; if you give encouraging guidance, be careful that you don't get bossy; if you're put in charge, don't manipulate; if you're called to give aid to people in distress, keep your eyes open and be quick to respond; if you work with the disadvantaged, don't let yourself get irritated with them or depressed by them. Keep a smile on your face.**"
- 현행 Teen EN: "If your thing is to speak up for God, then just do that. **Don't add a bunch of your own stuff. If you're a helper, then just help, don't try to take over. If you're a teacher, then stick to teaching.** If you're good at giving advice, **don't be a bossy know-it-all.** If you're in charge, **don't be a manipulator.** If you're supposed to help people who are struggling, then **be ready to jump in and help.** If you're working with people who have it rough, **don't get all annoyed or bummed out by them. Just keep a smile on your face.**"
- 현행 Teen KO: "격려를 잘하면, 격려해. 주는 사람이면, 넉넉히 줘. 리더면, 가진 모든 걸 다해 이끌어. 자비를 잘 베풀면, 미소 지으면서 해."
- 누락/문제: KO가 ① 설교·도움·가르침 세 은사 자체를 빼먹고 ② 각 은사별 태도 경고(끼어들지 말기, 잘난 체 금지, 조종 금지, 신속 대응, 짜증·우울 금지) 전부 누락. EN 7개 항목 중 KO는 4개만, 그것도 경고 없이.
- 수정 방향: KO를 EN 7개 항목 × 태도 경고까지 1:1로 번역.

### 그 외: EN은 MSG 의미를 대체로 충실히 보존. 이슈 없음.

---

## Romans 13

### 이슈 13-1 [경미] EN/KO 11–14절: "sleeping around" 경고가 "사고 치기"로 일반화
- 절 범위: 11–14
- MSG: "…**don't get involved in sleeping around and dissipation, don't get involved in brawling and petty jealousies.** …"
- 현행 Teen EN: "…Don't spend your time just **messing around, getting into trouble,** fighting with people, and being greedy. Get up, get dressed in Christ, and let's get going!"
- 현행 Teen KO: "…그냥 놀고, **사고 치고,** 사람들이랑 싸우고, 탐욕 부리면서 시간 쓰지 마. 일어나, 그리스도로 옷 입고, 가자!"
- 누락/문제: MSG의 구체적 경고 "sleeping around"(성적 방탕)가 "getting into trouble/사고 치기"로 일반화되어 성적 경고의 명시성이 사라짐. 욕 순화 원칙과 충돌하지 않는 선에서 의미는 살려야 함.
- 수정 방향: "getting into trouble"을 성적 방탕을 포함하는 표현으로 구체화 (예: "hooking up and partying recklessly" / "막나가는 연애·파티"). 비속어 없이 의미 보존.

### 그 외: 이슈 없음
- 통치자·세금·사랑의 빚·이웃 사랑 문단 모두 EN/KO 충실.

---

## Romans 14

### 이슈 14-1 [경미] EN/KO 5절: "convictions of conscience" → "직감" 약화
- 절 범위: 5
- MSG: "…**let each be fully convinced in their own mind / follow the convictions of your conscience**…"
- 현행 Teen EN: "…**follow your gut**…"
- 현행 Teen KO: "…**직감을 따라**…"
- 누락/문제: MSG의 "양심의 확신(convictions of conscience)"이 감정적 "직감(gut)"으로 약화. 양심적 신념과 순간 직감은 다름.
- 수정 방향: "follow what your conscience tells you" / "양심이 확신하는 대로"로 정정.

### 이슈 14-2 [경미] EN/KO 6–9절: "삶에서 죽음까지 하나님께 책임, 예수의 생사부활로 온 영역의 주" 축약
- 절 범위: 6–9
- MSG: "**It's *God* we are answerable to—all the way from life to death and everything in between—not each other. That's why Jesus lived and died and then lived again: so that he could be our Master across the entire range of life and death,** and free us from the petty tyrannies of each other."
- 현행 Teen EN: "…It's not about you. We're all on God's team, and He's the coach. **That's why Jesus went through everything He did – so He could be the boss of our lives** and we wouldn't have to deal with each other's petty nonsense."
- 누락/문제: "삶에서 죽음까지 하나님께만 책임짐", "예수가 살고 죽고 다시 살아서 삶과 죽음 전 영역의 주가 됨"이 "went through everything / boss of our lives"로 크게 축약.
- 수정 방향: "lived and died and then lived again … Master across the entire range of life and death" 뉘앙스 복원.

### 이슈 14-3 [중간] EN/KO 15–16절: "지옥에 보낼 위험" 경고 완화
- 절 범위: 15–16
- MSG: "…**Would you risk sending them to hell over an item in their diet? Don't you dare let a piece of God-blessed food become an occasion of soul-poisoning!**"
- 현행 Teen EN: "…**Are you really going to risk messing up their faith over a slice of pizza?** Don't let something as small as food become a reason for someone to turn away from God."
- 현행 Teen KO: "…**피자 한 조각 때문에 그들의 믿음을 망칠 위험을 감수할 거임?** 음식 같은 작은 게 누군가 하나님에게서 돌아서는 이유가 되지 않게 해."
- 누락/문제: MSG의 강한 경고 "그들을 지옥에 보낼 위험을 감수하겠는가", "영혼을 중독시키는 일"이 "믿음을 망칠 위험", "하나님에게서 돌아서는 이유"로 완화됨. 경고의 강도가 떨어짐.
- 수정 방향: 경고 수위 복원 (예: "risk wrecking them completely / sending them away from God for good"). 비속어 없이 강도 유지.

### 이슈 14-4 [경미] EN/KO 13–14절: "everything is holy" → "basically good" 약화
- 절 범위: 13–14
- MSG: "…**everything in itself is holy**…"
- 현행 Teen EN: "…**everything is basically good**…"
- 누락/문제: "거룩하다(holy)"가 "basically good"으로 약화.
- 수정 방향: "holy / clean before God" 뉘앙스로 정정.

### 그 외: 이슈 없음

---

## Romans 15

### 이슈 15-1 [경미] EN 3–6절: "하나님의 꾸준한 부르심과 따뜻한 개인적 권면" 축소
- 절 범위: 3–6
- MSG: "…**God wants the combination of his steady, constant calling and warm, personal counsel in Scripture to come to characterize *us*,** keeping us alert for whatever he will do next."
- 현행 Teen EN: "…**God wants us to learn from it, to stay sharp and ready for whatever He's gonna do next.**"
- 누락/문제: "하나님의 꾸준하고 변함없는 부르심 + 따뜻하고 개인적인 권면이 우리를 특징짓기를 원하심"이 "그것에서 배우자"로 축소.
- 수정 방향: EN에 해당 표현 복원.

### 이슈 15-2 [경미] EN 7–13절: "소망으로 넘침"이 "성령의 능력으로 넘침"으로 변경
- 절 범위: 7–13
- MSG: "…so that your believing lives, **filled with the life-giving energy of the Holy Spirit, will brim over with hope!**"
- 현행 Teen EN: "…so much joy and peace that your lives are **basically overflowing with the Holy Spirit's power.**"
- 누락/문제: 넘침의 대상이 "소망(hope)"에서 "성령의 능력"으로 바뀜. MSG의 포인트는 기쁨·평화에 더해 삶이 소망으로 넘치는 것.
- 수정 방향: "overflowing with hope"로 정정.

### 이슈 15-3 [경미] EN 14–16절: "성령으로 온전하고 거룩하게 됨" 누락
- 절 범위: 14–16
- MSG: "…so they can be presented as an acceptable offering to God, **made whole and holy by God's Holy Spirit.**"
- 현행 Teen EN: "…so they can be a holy and acceptable offering to God."
- 누락/문제: "하나님의 성령으로 온전하고 거룩하게 되어"가 빠짐.
- 수정 방향: EN/KO에 복원.

### 이슈 15-4 [경미] EN 30–33절: "성부께·주 예수의 능력으로·성령의 사랑으로" 기도 틀 누락
- 절 범위: 30–33
- MSG: "**Pray strenuously with and for me—to God the Father, through the power of our Master Jesus, through the love of the Spirit**—that I will be delivered from the lions' den of unbelievers in Judea."
- 현행 Teen EN: "Please pray for me, guys. **Pray hard** that I'll be safe from the haters in Judea."
- 누락/문제: "하나님 아버지께, 우리 주 예수의 능력을 통해, 성령의 사랑을 통해"라는 삼위일체적 기도 틀이 빠짐.
- 수정 방향: EN/KO에 복원.

### 그 외: 이슈 없음

---

## Romans 16

### 이슈 16-1 [경미] EN 1–2절: 뵈뵈 추천·"받을 자격" 누락
- 절 범위: 1–2
- MSG: "Be sure to welcome our friend Phoebe in the way of the Master, with all the generous hospitality we Christians are famous for. **I heartily endorse both her and her work. She's a key representative of the church at Cenchrea.** Help her out in whatever she asks. **She deserves anything you can do for her.** She's helped many a person, including me."
- 현행 Teen EN: "Hey, check it out. First up, I want you to give a massive welcome to our friend Phoebe. **She's a total rockstar from the church over in Cenchrea.** Roll out the red carpet for her, show her some major love, and help her with whatever she needs. Seriously, she's the real deal and has been a huge help to a ton of people, including me."
- 누락/문제: ① "그녀와 그녀의 일을 진심으로 추천함" ② "겐그레아 교회의 핵심 대표자" → "rockstar"로 직분 의미 약화 ③ "그녀는 네가 해줄 수 있는 무엇이든 받을 자격이 있음" 누락.
- 수정 방향: EN에 "I fully vouch for her and her work", "She deserves whatever help you can give" 복원. "key representative" 뉘앙스 유지.

### 그 외: 이슈 없음
- 3–23절 인사 명단, 17–18절 거짓 교사 경고, 19–20절 사탄 짓밟힘, 25–27절 송영 모두 EN/KO 충실. 참고: MSG 원문에 16:24절이 없음(초기 사본에 없는 절로 현대 역본 공통 생략) — Teen 누락 아님.

---

## 종합

- **심각**: 1-2, 3-3, 4-1, 4-2, 6-1, 8-1, 8-2, 9-1, 11-2, 12-1, 12-2, 12-3 (12건) — 대부분 KO 문단 밀림·통째 누락 또는 EN 인용 왜곡.
- **중간**: 1-1, 2-1, 2-2, 2-3, 3-1, 3-2, 3-4, 3-5, 4-3, 5-1, 5-2, 5-3, 6-2, 6-3, 7-1, 7-2, 7-3, 7-4, 8-3, 8-4, 8-5, 10-1, 11-1, 14-3 (24건).
- **경미**: 1-3, 1-4, 4-4, 6-4, 7-5, 8-6, 9-2, 13-1, 14-1, 14-2, 14-4, 15-1, 15-2, 15-3, 15-4, 16-1 (16건).
- 패턴: KO가 EN 문단과 1:1로 대응하지 않고 한 칸씩 밀리면서 특정 절 범위의 내용이 통째로 사라지는 경우가 반복됨 (1장 26–27, 8장 9–11·29–30, 11장 30–32). KO 전수 재정렬이 필요.
- 9-3은 예비 후보였으나 재확인 결과 이슈 없음으로 판정.
- 소스 JSON은 수정하지 않음.
---

## 부록: 2026-09-23 미묘한 슬랭 일괄 수정 (번역 원칙 5)

- 배경: 신약 27권 EN/KO 전수 검사에서 자동 욕설 목록 밖의 미묘한 슬랭·저속 표현 발견. 성욱 지시("B 기준 정하고 한 번에 해")에 따라 아래 확정 6개 Rule로 일괄 수정.
- Rule: ① 채팅 약어·유행 은어(ㅇㅋ·here's the tea·woke·throw shade·GOAT·FOMO·fam·vibe) ② 원칙 5 명시 슬랭(썰·꿀잼·쌩까·드립·뇌절·어그로·인싸춤·뿅·텐션·뇌정지·가오·찢길각) ③ ghosting 계열(ghost·고스팅) ④ 신성한 대상 경량화(찐·대박·인싸/아싸·레전드·흑역사·맛집·핫해·좋아요·게임 체인저·That loser is gone) ⑤ 저속·모욕·첨가 강화 순화(관종·lame·freaking out·working my butt off·맛이 갔네·한심·일진/꼽준다·멘붕·멘탈·올인) ⑥ 유지(chill·bro·왕따 — 변경 없음)
- 수정 원칙: EN primary(MSG 의미 유지), KO는 수정된 EN의 의미·톤 1:1, 의미 축소·본문 구조 변경 금지, 해당 표현만 최소 수정.

- 본 권 수정: **EN 13건, KO 10건** (합계 23건). Rule ⑥(chill·bro·왕따) 변경 없음.

| 장 | 위치 | 언어 | Rule | 기존 | 수정 |
|---|---|---|---|---|---|
| 1 | p4 | EN | ③ | don't think I've been ghosting you | don't think I've been ignoring you |
| 2 | p3 | EN | ③ | Every time you ghost God | Every time you walk away from God |
| 6 | p1 | EN | ③ | you basically ghosted your old life of sin | you basically walked away from your old life of sin |
| 6 | p4 | EN | ⑤ | You're not living under its lame dictatorship. | You're not living under its miserable dictatorship. |
| 7 | p2 | EN | ③ | he basically ghosted that whole system | he basically walked away from that whole system |
| 8 | p3 | EN | ③ | you're basically ghosting God | you're basically running off from God |
| 9 | p3 | EN | ③ | I'm ghosting Esau | I'm walking away from Esau |
| 10 | p5 | EN | ③ | all he got was ghosted | all he got back was silence |
| 11 | p1 | EN | ③ | he's ghosting them for good | he's walking away from them for good |
| 11 | p5 | EN | ① | starting to get a little FOMO | starting to feel a little jealous |
| 12 | p1 | EN | ⑤ | That's lame. | That's no way to live. |
| 14 | p2 | EN | ⑤ | It would be super lame to start hating on | It would be terrible to start hating on |
| 15 | p1 | EN | ③ | He didn't just ghost everyone's problems | He didn't just walk away from everyone's problems |
| 1 | p4 | KO | ③ | 자, 내가 너네를 고스팅했다고 생각하지 않았으면 좋겠음. | 자, 내가 너네를 무시했다고 생각하지 않았으면 좋겠음. |
| 2 | p3 | KO | ③ | 하나님을 고스팅할 때마다, | 하나님한테서 등을 돌릴 때마다, |
| 6 | p4 | KO | ⑤ | 하나님의 길에 올인해야 함. | 하나님의 길에 모든 걸 걸어야 함. |
| 6 | p4 | KO | ⑤ | 하나님의 길에 올인함. | 하나님의 길에 모든 걸 걸고 있음. |
| 7 | p10 | KO | ⑤ | 마음으로는 하나님의 규칙에 완전 올인인데, | 마음으로는 하나님의 규칙을 완전히 따르고 싶은데, |
| 8 | p3 | KO | ④ | 그게 완전 게임 체인저임. | 그게 완전히 판도를 바꾸는 일임. |
| 8 | p3 | KO | ③ | basically 하나님을 고스팅하는 거고, | basically 하나님한테서 도망치는 거고, |
| 9 | p8 | KO | ⑤ | 규칙에 올인하고 모든 걸 바르게 하려고 했던 | 규칙 지키는 데만 매달리고 모든 걸 바르게 하려고 했던 |
| 15 | p1 | KO | ③ | 모두의 문제를 그냥 고스팅하지 않으셨음; | 모두의 문제를 그냥 외면하지 않으셨음; |
| 16 | p2 | KO | ④ | 완전 레전드임! | 정말 대단한 분이세요! |

**8개 게이트 전부 PASS (2026-09-23)**
- ①수정반영: 부록 23건 old→new 쌍 JSON 반영 확인 (신규 문자열 존재·구 문자열 소멸 grep 검증). ②validator: 16장 전부 통과. ③완전성: git HEAD 대비 FAIL 집합 byte-identical — 슬랭 수정으로 인한 신규 이슈 0건 (기존 35건 FAIL 라인은 감사 시 문서화된 오탐 + 수정 완료된 실제 누락 1건). ④Docs재빌드: rows=176, teen_without_msg=0, msg_orphans=0. ⑤짝지음: 156 data rows / 16 tables PAIRING CONTENT OK. ⑥재업로드: 기존 Doc ID 유지. ⑦API 테이블 수: 16/16. ⑧export-back: VERIFIED OK.
