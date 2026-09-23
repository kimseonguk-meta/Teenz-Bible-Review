# Acts 기계적 완전성 검사 — FAIL 23건 판정 근거

검사: `python3 gdocs_build/completeness_check.py fixes/en_Acts.json` (2026-09-23)
결과: 28장 407문단(헤더 제외), 이름 토큰 649개·숫자 토큰 152개 중 FAIL 23건.
판정: **실제 누락 1건(EN 수정 완료)**, 나머지 22건은 전부 문서화된 오탐.

오탐 클래스 (5권 감사와 동일 기준):
- A. 대명사/관용구 one의 숫자 오인 ("the one", "one of the council")
- B. 서수·관용구 paraphrase ("first thing in the morning"→"tomorrow morning", "the first time"→"at the very beginning")
- C. 관용구·숙어 paraphrase ("fear of God"→"scared half to death", "four winds and seven seas"→"ends of the earth")
- D. 동일 지시대상 호칭 교체 ("O God"→"Lord", "God's Law"→"the Law", "Word"→"News")
- E. 지명 형용사→지명/설명 풀어쓰기 ("Cyrenians"→"from Cyrene", "Areopagite"→"a member of the Areopagus")
- F. 동의어 치환 ("Potentates"→"rulers", "Milling"→"Crawling", "Calluses"→"calloused")
- G. checker 규칙 아티팩트 ("four hundred"를 MSG에서만 4+400으로 이중 파싱, "the One" 대시 앞뒤 절 분리 차이)

---

## 실제 누락 1건 — 수정 완료

### FAIL ch13 idx22 [badge 50-52] number: 2 → EN 수정함
- MSG 50-52: "...brimming with joy and the Holy Spirit, **two happy disciples**."
- 수정 전 EN: "...moved on to the next town, Iconium — filled with joy and the Holy Spirit." — "two" 없음.
- KO에는 있었음 ("행복한 **두** 제자였습니다") → EN/KO 비대칭까지 발생.
- 조치: EN에 ", two happy disciples" 복원. decisions_Acts.json ch13 changes에 기록.
- 판정: **실제 누락 → 수정 완료**

---

## 오탐 22건

### ch1 idx13 [23-26] name: god — 오탐 (D)
- MSG: "You, **O God**, know every one of us inside and out."
- EN: "**Lord**, you know every one of us inside and out."
- "O God"→"Lord" 동일 지시대상(기도의 수신자). 의미 완전 보존.

### ch3 idx0 [1-5] number: 1 — 오탐 (A)
- MSG: "the **one** named Beautiful"
- EN: "the Temple gate called Beautiful"
- "the one"=대명사. 삭제가 아니라 관계절 축약. 의미 동일.

### ch3 idx1 [6-8] number: 1 — 오탐 (A)
- MSG: "the **one** who sat begging at the Temple's Gate Beautiful"
- EN (idx2, badge 8-10, union): "this was the guy who used to sit and beg at the Beautiful Gate"
- "the one"→"the guy" 대명사 치환. 의미 동일.

### ch4 idx9 [23-26] name: potentates — 오탐 (F)
- MSG (시편 2 인용): "**Potentates** meet for summit talks"
- EN: "**rulers** meet for summit talks"
- "Potentates"→"rulers" 정당한 teen 동의어. 의미 동일.

### ch5 idx18 [33-37] number: 1, 4 — 오탐 (A + G)
- "1": MSG "**one** of the council members stood up" → EN "a council member stood up". 대명사 one.
- "4": MSG/EN 둘 다 "**four hundred**" 그대로 있음. checker가 MSG 쪽만 4+400으로 이중 파싱한 아티팩트.

### ch6 idx5 [8-10] name: cyrenians, alexandrians — 오탐 (E)
- MSG: "**Cyrenians**, **Alexandrians**, and some others from Cilicia and Asia"
- EN: "people from **Cyrene**, **Alexandria**, Cilicia, and Asia"
- 형용사→지명 전치사구. 전원 보존.

### ch7 idx3 [4-7] name: chaldees — 오탐 (E)
- MSG: "the country of the **Chaldees**" → EN: "the land of the **Chaldeans**". 동일 민족, 복수형 변형.

### ch7 idx19 [51-53] name: calluses — 오탐 (F)
- MSG: "**Calluses** on your hearts" → EN: "Your hearts are **calloused**". 명사→형용사, 동일 어근.

### ch11 idx2 [4-6] name: milling — 오탐 (F)
- MSG: "**Milling** around on the blanket" → EN: "**Crawling** around on that blanket". 동의어.

### ch11 idx5 [15-17] number: 1 — 오탐 (B)
- MSG: "just as he did on us the **first** time" → EN: "exactly like he did on us at the very **beginning**"
- 서수 "first"→"beginning" 정당한 paraphrase.

### ch13 idx1 [1-2] name: cyrenian — 오탐 (E)
- MSG: "Lucius the **Cyrenian**" → EN: "Lucius from **Cyrene**". 동일인.

### ch13 idx8 [13-14] name: god — 오탐 (D)
- MSG v14: "the Scriptures—**God's** Law and the Prophets"
- EN (idx9, badge 14-15, union): "the Scripture reading — **the Law** and the Prophets"
- 회당 성경봉독 문맥에서 "the Law"=토라. 의미 보존.

### ch13 idx20 [46-47] number: 4, 7 — 오탐 (C)
- MSG: "You'll proclaim salvation to the **four** winds and **seven** seas"
- EN: "You will bring salvation to the **ends of the earth**!"
- MSG 특유의 시적 paraphrase→표준 관용구. 의미(전 세계 선포) 동일.

### ch17 idx7 [13-15] name: thessalonian — 오탐 (E)
- MSG: "the **Thessalonian** hard-line Jews" → EN: "the hard-line Jews in **Thessalonica**". 동일 집단.

### ch17 idx15 [32-34] name: areopagite — 오탐 (E)
- MSG: "Dionysius the **Areopagite**" → EN: "Dionysius, a member of the **Areopagus**". 설명 풀어쓰기, 더 명확.

### ch18 idx14 [27-28] name: ephesian — 오탐 (E)
- MSG: "his **Ephesian** friends" → EN: "his friends in **Ephesus**". 동일.

### ch20 idx1 [1-2] name: thessalonians — 오탐 (E)
- MSG v2: "Aristarchus and Secundus, both **Thessalonians**" (+동행자 7명 명단)
- EN (idx2, badge 2-4, union): "Aristarchus and Secundus, both from **Thessalonica**" — 7명 명단 전원 보존.

### ch22 idx4 [8-9] number: 1 — 오탐 (G)
- MSG/EN 둘 다 "**the One** you're hunting down/persecuting" 그대로 있음.
- checker가 MSG 절("the One you're hunting down")과 EN 절("the very One you're persecuting")의 대시 분리 차이로 한쪽만 숫자로 분류한 아티팩트.

### ch22 idx16 [29] name: god — 오탐 (C)
- MSG: "it put the **fear of God** into the captain"
- EN: "it scared the commander half to death"
- 관용구→관용구. 의미(극도의 공포) 동일.

### ch23 idx13 [20-21] number: 1 — 오탐 (B)
- MSG: "**first** thing in the morning" → EN: "**Tomorrow** morning"
- "first thing"=이른 아침 관용구. teen 문체에서 "tomorrow morning"으로 충분.

### ch28 idx2 [7-9] name: word — 오탐 (D)
- MSG: "**Word** of the healing got around fast" → EN: "**News** of the healing spread fast". 동의어.

### ch28 idx5 [12-14] name: appian — 오탐 (E)
- MSG: "as far as **Appian** Court" → EN (idx6, badge 14-16, union): "as far as the Forum of **Appius**"
- 실명 보존 (Appius), MSG보다 정확한 지명. "Three Taverns"도 보존됨.
