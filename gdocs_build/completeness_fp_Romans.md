# Romans 기계적 완전성 검사 — FAIL 35건 판정 근거

검사: `python3 gdocs_build/completeness_check.py fixes/en_Romans.json`
결과: 16장 156문단, 이름 토큰 245개·숫자 토큰 32개 중 FAIL 35건.
판정: **실제 누락 1건(EN 수정 완료)**, 나머지 34건은 전부 문서화된 오탐.

오탐 클래스:
- A. 대명사/관용구 one의 숫자 오인 ("the one", "each one", "at one time or another")
- B. 서수·열거 paraphrase ("first father"→"founding father", "the first thing"→생략)
- C. 관용구·숙어 paraphrase ("second-guess"→"question", "seven seas"→"all over the world", "two birds with one stone"→두 결과 풀어쓰기, "in the first place"→"where they belong")
- D. 동일 지시대상 호칭 교체 (Jesus↔Christ↔Messiah, Lord→God, God's Word→God's plan)
- E. 지명 형용사→지명 ("Macedonians"→"Macedonia", "Achaians"→"Achaia")
- F. 문장 첫머리 부사 오인 ("Insofar"를 이름으로 추출)
- G. checker 규칙 아티팩트 ("the one man"의 one은 TEEN에도 그대로 있으나 비숫자로 분류돼 union_nums에서 탈락)

---

## 실제 누락 1건 — 수정 완료

### FAIL 1 — ch1 idx3 [badge 8-12] name: jesus, son → EN 수정함
- MSG 8-12: "I thank God **through Jesus** for every one of you… God, whom I so love to worship and serve by spreading the good news of **his Son**—the Message!—knows…"
- 수정 전 EN: "First off, I gotta thank God for every single one of you… God knows I'm not faking it. I'm constantly praying for you guys…" — "through Jesus"와 "spreading the good news of his Son"이 통째로 없음 (paraphrase로도 복원 불가).
- KO에는 둘 다 있었음 ("예수 그리스도를 통해…", "그분의 아들에 대한 좋은 소식을 전하면서 가진 모든 걸 다해 그분을 섬기고") → EN/KO 의미 비대칭까지 발생.
- 조치: EN에 "I gotta thank God—through Jesus—for every single one of you… I worship and serve him by spreading the good news about his Son." 복원. 감사 리포트에는 없던 추가 발견.
- 판정: **실제 누락 → 수정 완료**

---

## 오탐 34건

### ch2 idx6 [14-16] name: christ — 오탐 (D)
- MSG: "…This is my Gospel according to Jesus Christ, taking it all into account."
- EN: "The message I'm spreading through Jesus takes all of that into account."
- "Christ"→"Jesus" 동일 지시대상. 의미 완전 보존.

### ch2 idx8 [17-24] name: word — 오탐 (D)
- MSG: "…because you know God's revealed Word inside and out…"
- EN: "Don't get cocky because you know all the right answers."
- "God's revealed Word"(성경 지식)→"all the right answers" paraphrase. 문맥 의미(아는 체하는 교만) 보존.

### ch3 idx0 [1-2] number: 1 — 오탐 (B)
- MSG: "**First**, there's the matter of being put in charge of writing down and caring for God's revelation…"
- EN: "Okay, so what makes Jewish people special? …It matters, big time." + 다음 문단 [2-6] "They were the ones who got to be the keepers of God's message."
- "First"는 답변 열거 표지. 답변 내용(하나님의 메시지 수탁자)은 두 문단에 걸쳐 보존.

### ch4 idx1 [1-3] number: 1 — 오탐 (B)
- MSG: "…Abraham, our **first** father in the faith…"
- EN: "…Abraham, like, the founding father of our whole faith thing."
- 서수 "first"→"founding" 정당한 teen paraphrase.

### ch4 idx3 [6-9] name: lord — 오탐 (D)
- MSG: "Fortunate the person against whom the **Lord** does not keep score."
- EN: "Lucky is the person whose sin God doesn't even count."
- "Lord"→"God" 동일 지시대상.

### ch4 idx3 [6-9] number: 1 — 오탐 (A)
- MSG: "…saying that **the one** who trusts God…"
- EN: "…the person who trusts God…"
- "the one"=대명사. "the person" 치환은 의미 동일.

### ch4 idx8 [13-15] number: 1 — 오탐 (C)
- MSG: "…if there is no contract in **the first place**, simply a promise…"
- EN: "But with a promise, especially one from God, you can't break it."
- "in the first place"(애초에)는 관용구. "first"가 숫자 1이 아님.

### ch4 idx10 [17-18] number: 1 — 오탐 (B)
- MSG: "Abraham was **first** named 'father' and then became a father…"
- EN: "Abraham was called a father *before* he even had kids…"
- 서수 "first"→"before" 정당한 paraphrase.

### ch5 idx4 [9-11] name: son — 오탐 (문맥상 동일 지시, KO와 parity 유지)
- MSG: "…we were put on friendly terms with God by the sacrificial death of **his Son**…"
- EN: "Now that we're good with God because of this ultimate sacrifice…"
- 직전 문단 [6-8]에서 "Christ showed up… He took one for the team and died for us"로 희생 주체가 그리스도임이 명시됨. "this ultimate sacrifice"가 그것을 지시. KO는 "그분의 아들의 희생적인 죽음으로"로 더 명시적이나 의미 동등. EN/KO 의미 1:1 유지.

### ch5 idx7 [15-17] number: 1 — 오탐 (G)
- MSG: "…what God's gift, given through one man… all provided by Jesus Christ" (파싱 텍스트: "the **one** man Jesus Christ provides").
- EN: "…given through **one man, Jesus Christ**… all provided by Jesus Christ."
- 토큰 "one"이 EN 텍스트에 그대로 존재. checker가 MSG의 "the one"은 숫자로, EN의 "one man"은 비숫자로 분류한 규칙 아티팩트.

### ch7 idx2 [4-6] name: christ — 오탐 (D)
- MSG: "When **Christ** died he took that entire rule-dominated way of life down with him…"
- EN: "When **Jesus** died, he basically ghosted that whole system."
- 동일 지시대상.

### ch8 idx6 [15-17] name: christ — 오탐 (D)
- MSG: "…We go through exactly what **Christ** goes through…"
- EN: "We'll go through the tough stuff with **Jesus**, but we'll also get to share in the good times with him."
- 동일 지시대상.

### ch8 idx11 [31-39] number: 1 — 오탐 (C)
- MSG: "…they pick us off **one by one**."
- EN: "Even when it feels like we're being taken out, none of it matters because Jesus loves us." (KO: "하나하나 잡아감"으로 보존)
- "one by one"은 양태 부사구. 핵심 의미(죽임을 당함)는 보존. teen 축소 허용 범위.

### ch9 idx2 [6-9] name: word — 오탐 (D)
- MSG: "…that God's **Word** has malfunctioned in some way or other."
- EN: "…think God's **plan** glitched or something."
- "God's Word"(하나님의 약속/말씀)→"God's plan" paraphrase. 문맥(9:6 이스라엘 혈통≠하나님 백성) 의미 보존.

### ch9 idx6 [20-33] number: 2 — 오탐 (C)
- MSG: "…to **second**-guess God?"
- EN: "…who are you to question God?"
- "second-guess"는 동사(따지다). "second"가 숫자 2가 아님.

### ch10 idx2 [4-10] name: messiah — 오탐 (D)
- MSG: "…get us ready for the **Messiah**, who then puts everything right…"
- EN: "…get everyone ready for **Jesus**. He's the one who makes everything right…"
- 동일 지시대상 (Jesus = the Messiah).

### ch10 idx4 [14-17] name: christ, word — 오탐 (D)
- MSG: "…unless **Christ's Word** is preached, there's nothing to listen to."
- EN: "And there's no message to hear unless someone is talking about **Jesus**."
- "Christ"→"Jesus" 동일 지시대상, "Word"→"message" paraphrase.

### ch10 idx4 [14-17] number: 1 — 오탐 (A/C)
- MSG: "Isaiah asked what we all ask at **one** time or another…"
- EN: "The prophet Isaiah even asked, 'God, is anyone even listening?'"
- "at one time or another"(언젠가는)는 관용구. 숫자 아님.

### ch10 idx5 [18-21] number: 7 — 오탐 (C)
- MSG: "Their message to earth's **seven seas**."
- EN: "The good news has been preached all over the world."
- "seven seas"=온 세상 관용구. 의미 완전 보존.

### ch11 idx1 [1-2] name: semitic — 오탐 (D)
- MSG: "…I, the one writing these things, am **Semitic** to the core, a pure-blooded descendant of Abraham…"
- EN: "Don't forget, I'm an **Israelite** myself, a descendant of Abraham from the tribe of Benjamin."
- 민족 서술 paraphrase. 의미 완전 보존.

### ch11 idx1 [1-2] number: 1 — 오탐 (A)
- MSG: "…I, **the one** writing these things…"
- EN: "Don't forget, **I'm** an Israelite myself…"
- "the one"=대명사(바울). "I'm"으로 지시대상 보존.

### ch11 idx6 [13-15] name: israelite, god — 오탐 (D)
- MSG: "…when I'm among my **Israelite** kin, the so-called insiders, hoping they'll realize what they're missing and want to get in on what **God** is doing."
- EN: "…my own people, the insiders, will see what's happening and want back in."
- "Israelite kin"→"my own people", "what God is doing"→"what's happening" paraphrase. 핵심(그들이 돌아오길 바람) 보존.

### ch11 idx6 [13-15] number: 1 — 오탐 (B)
- MSG: "If the **first** thing the Jews did, even though it was wrong for them, turned out for your good…"
- EN: "If them messing up led to something good for you…"
- "the first thing" 열거 표현 축소. 핵심 대비(그들의 실패→너희 유익) 보존.

### ch11 idx10 [23-24] number: 1 — 오탐 (C)
- MSG: "…grafting branches back into the tree they grew from in the **first** place."
- EN: "…put the original branches back where they belong."
- "in the first place"(원래 자리) 관용구→"where they belong" paraphrase.

### ch12 idx3 [4-6] name: christ — 오탐 (D)
- MSG: "The body we're talking about is **Christ's** body of chosen people."
- EN: "That body is Team Jesus."
- 동일 지시대상.

### ch12 idx5 [9-10] number: 2 — 오탐 (B)
- MSG: "…practice playing **second** fiddle."
- EN: "…it's cool to let someone else be the star sometimes." (KO: "2인자 역할을 연습해")
- 서수 관용구 "second fiddle"(2인자) paraphrase. 의미 완전 보존.

### ch13 idx1 [1-3] name: insofar — 오탐 (F)
- MSG: "**Insofar** as there is peace and order, it's God's order."
- EN: "As long as things are peaceful and not totally chaotic, that's God's doing."
- 문장 첫머리 부사 "Insofar"를 checker가 이름으로 오추출. 의미 완전 보존.

### ch14 idx7 [15-16] name: christ — 오탐 (D)
- MSG: "These, remember, are persons for whom **Christ** died."
- EN: "Remember, **Jesus** died for them too."
- 동일 지시대상.

### ch14 idx8 [17-18] number: 2 — 오탐 (C)
- MSG: "…you'll kill **two** birds with one stone: pleasing the God above you and proving your worth to the people around you."
- EN: "If you do that, you'll be good with God and people will respect you."
- "two birds with one stone" 관용구. 두 결과(하나님 기쁘심+사람들 인정) 모두 풀어쓰기로 보존.

### ch15 idx0 [1-2] number: 1 — 오탐 (A)
- MSG: "**Each one** of us needs to look after the good of the people around us…"
- EN: "We should all be looking out for each other…"
- "each one"=대명사. "we all" 치환 의미 동등.

### ch15 idx1 [3-6] name: father — 오탐 (D, 칭호 생략)
- MSG: "…a stunning anthem to the God and **Father** of our Master Jesus!"
- EN: "…our lives singing a fire anthem to God."
- "Father of our Master Jesus"는 "God"의 동격 칭호. 지시대상(God) 보존, 송영 기능 보존.

### ch15 idx8 [25-29] name: jesus, macedonians, achaians — 오탐 (D/E)
- MSG: "…deliver a relief offering to the followers of **Jesus** there. The Greeks—all the way from the **Macedonians** in the north to the **Achaians** in the south…"
- EN: "…drop off some donations for the believers there. The Greeks, from **Macedonia** to **Achaia**, all pitched in…"
- "followers of Jesus"→"the believers"(문맥상 동일 집단), "Macedonians"→"Macedonia", "Achaians"→"Achaia" 지명형 paraphrase. 의미 완전 보존.

### ch16 idx7 [11] name: lord — 오탐 (D)
- MSG: "Hello to those who belong to the **Lord** from the family of Narcissus."
- EN: "And to all the believers in Narcissus's household."
- "belong to the Lord"→"believers" 동일 지시대상.

### ch16 idx13 [17-18] name: christ — 오탐 (D)
- MSG: "…it is most certainly not serving **Christ** the Master."
- EN: "They're not serving our main man, **Jesus**…"
- 동일 지시대상.

---

## 결론
- 35건 중 실제 누락 1건(ch1 8-12 "through Jesus"/"his Son") → EN 수정 완료, 재검사 필요.
- 나머지 34건은 오탐 (클래스 A 4건, B 5건, C 6건, D 17건, F 1건, G 1건). 실제 누락·요약·의미 반전 0건.
