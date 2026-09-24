# Amos 기계적 완전성 검사 — FAIL 판정 근거

검사: `python3 gdocs_build/completeness_check.py fixes/en_Amos.json` (Sep 24)
결과: 9장 106문단(헤더 제외), 이름 토큰 117개·숫자 토큰 33개 중 FAIL 7건.
판정: **실제 누락 3건(EN 수정 완료)**, 나머지 4건은 전부 문서화된 오탐.

오탐 클래스 (Acts 5권 감사와 동일 기준):
- C. 관용구·숙어 paraphrase
- D. 동일 지시대상 호칭 교체
- F. 동의어 치환

---

## 실제 누락 3건 — 수정 완료

### FAIL ch2 idx0 [1-3] name: kerioth → EN 수정함
- MSG: "For that, I'm burning down Moab, **burning down the forts of Kerioth**."
- 수정 전 EN: "I'm sending a fire to destroy Moab and **its strongest forts**." — "Kerioth" 없음 (고유명사 삭제).
- KO에는 있었음 ("케리옷의 요새들을") → EN/KO 비대칭까지 발생.
- 조치: EN을 "For that, I'm burning down Moab, burning down the forts of Kerioth."로 복원.

### FAIL ch7 idx0 [1-2] number: 2 → EN 수정함
- MSG: "the **second** crop was just sprouting."
- 수정 전 EN: "the **next round** of crops was just starting to grow." — 서수 "second" 누락.
- KO에는 있었음 ("두 번째 작물") → EN/KO 비대칭.
- 조치: EN을 "the **second round** of crops was just starting to grow."로 복원.

### FAIL ch9 idx2 [7] name: qir → EN 수정함
- MSG 9:8 (BibleGateway 실시간 대조 확인, Sep 24): "the Arameans from **Qir**".
- 수정 전 EN: "the Arameans from **Kir**".
- 참고: MSG 1:5에서는 "to **Kir**"로 표기 — MSG 원문 자체가 장별로 철자가 다름 (Kir vs Qir). EN은 MSG 각 구절의 철자를 그대로 따름 (1:5 "Kir", 9:8 "Qir"). KO는 한국어 표기 관용상 두 곳 모두 "기르"로 통일.
- 조치: EN 9:8을 "the Arameans from **Qir**"로 수정. EN/KO 음역 차이(로마자 K/Q vs 한글 기르)는 내용 차이가 아니므로 유지.

---

## 오탐 4건

### ch1 idx9 [11-12] quote: rampages, meanness, timeout — 오탐 (C/F)
- MSG: "Her anger **rampages** day and night. Her **meanness** never takes a **timeout**."
- EN: "Their anger is just **non-stop, 24/7**. Their **cruelty** never takes a **break**."
- "rampages"→"non-stop, 24/7", "meanness"→"cruelty", "timeout"→"break". 의미 완전 보존된 paraphrase.

### ch5 idx2 [3] name: word — 오탐 (D)
- MSG: "This is the Message, **God's Word**."
- EN: "This is the real deal, **from God himself**:"
- 동일 지시대상(하나님의 말씀). 의미 완전 보존.

### ch6 idx3 [8] name: word — 오탐 (D)
- MSG: "has sworn, and solemnly **stands by his Word**."
- EN: "has sworn it, and **He's not backing down**."
- 동일 지시대상(하나님의 말씀에 대한 신실함). 의미 완전 보존.

### ch7 idx18 [16] name: word — 오탐 (D)
- MSG: "**So listen to God's Word**."
- EN: "**'So listen to what God is saying**."
- 동일 지시대상. 의미 완전 보존.
