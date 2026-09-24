# Zechariah completeness_check 오탐(False Positive) 기록

- 대상: `fixes/en_Zechariah.json` (MSG = `msg_Zechariah.txt`, parsed 113 units, 14장)
- 검사일: 2026-09-24
- 검사기: `gdocs_build/completeness_check.py`
- 최종 상태: 검사 중 발견된 FAIL 11건 중 7건은 실제 누락으로 판정해 직접 복원함 (아래 "복원한 FAIL" 참조).
  복원 후 재검사 결과 잔여 FAIL 4건은 모두 오탐으로 판정 (검사 로직의 기계적 한계).
- validator: `PASS: 14개 장 모두 통과`

## 복원한 FAIL (오탐 아님)

1. ch1 idx16 [badge 21] `number: 4`
   - MSG: "...used their horns to scatter Judah to the four winds."
   - TEEN (수정 전): "...used their horns to scatter Judah everywhere."
   - 복원: "...used their horns to scatter Judah to the four winds."
   - KO도 동일 반영: "유다를 사방으로 흩어버리려고..." (KO는 원래 "사방으로"가 있었음)
2. ch6 idx5 [badge 9-12] `name: zephaniah, jehozadak`
   - MSG: "...at the home of Josiah son of Zephaniah..." / "Place one on the head of Joshua son of Jehozadak, the high priest..."
   - TEEN (수정 전): "You'll find them at Josiah's house." / "Put one on the head of Joshua, the high priest,"
   - 복원: "Josiah son of Zephaniah's house" / "Joshua son of Jehozadak, the high priest"
   - KO는 원래 두 이름 모두 있었음 ("스바냐의 아들 요시아", "여호사닥의 아들인 대제사장 여호수아") — EN만 복원
3. ch6 idx7 [badge 14] `name: zephaniah`
   - MSG: "...Helem, Tobiah, Jedaiah, and Hen son of Zephaniah."
   - TEEN (수정 전): "...and Helem, Tobiah, Jedaiah, and Hen will be in charge of it."
   - 복원: "...and Hen son of Zephaniah will be in charge of it."
   - KO는 원래 "스바냐의 아들 헨"이 있었음 — EN만 복원
4. ch7 idx3 [badge 7-10→7-8] `name: negev, shephelah`
   - MSG: "...the outlying countryside, the Negev and Shephelah, was populated?"
   - TEEN (수정 전): "...the whole area was full of people?"
   - 복원: "...the whole area—the Negev and Shephelah—was full of people?"
   - KO도 1:1 반영: "...외곽 지방이랑 네게브, 스벨라까지 사람 바글바글할 때..."
5. ch7 idx6 [badge 13-14] `number: 4`
   - MSG: "I scattered them to the four winds."
   - TEEN (수정 전): "He scattered them all over the place..."
   - 복원: "He scattered them to the four winds..."
   - KO는 원래 "사방으로 다 흩어버렸음"이 있었음 — EN만 복원
6. ch9 idx3 [badge 9-10] `number: 4, 7`
   - MSG: "...a peaceful rule worldwide, from the four winds to the seven seas."
   - TEEN (수정 전): "...a peaceful rule over the whole world, from sea to shining sea."
   - 복원: "...from the four winds to the seven seas."
   - KO도 1:1 반영: "...사방의 바람에서 일곱 바다까지 온 세상을 평화롭게 다스릴 거야."
7. 배지 정정 (검사기 FAIL은 아니었으나 MSG 기준 오배지 — pairing 정확도 위해 수정)
   - ch1: para5/6/7 `[10],[11],[12]` → `[9],[10],[11]` (MSG v9b/v10/v11 내용)
   - ch4: para2 `[2]` → `[2-3]` (MSG v2-3 문답)
   - ch6: para1 `[2]` → `[2-3]` (MSG v2-3)
   - ch7: para3 `[7-10]` → `[7-8]`, para4 `[10]` → `[9-10]` (MSG 7-10 한 단락을 intro/인용구로 분할)
   - ch11: para5 `[10]` → `[10-11]` (MSG v10-11)
   - ch12: para1 `[2-3]` → `[1-2]`, para2 `[4]` → `[3]`, para3 `[5-6]` → `[4-5]`, para7 `[10-12]` → `[10-11]`, para8 `[10-14]` → `[12-14]`
   - msg_ranges도 동일하게 정정 (validator 커버리지는 msg_ranges 합집합 기준)

## 오탐 판정 목록

1. ch1 idx0 [badge 1-4] `number: 8`
   - MSG "In the eighth month of the second year..." → TEEN "in the second year that Darius was king, around October"
   - "eighth month"를 "around October"로 의역한 것으로 내용 손실 없음. 히브리력 8월(Cheshvan)=양력 10~11월. 오탐.
2. ch5 idx3 [badge 3-4] `number: 1, 2`
   - MSG "The first half of the book...; the second half..." → TEEN "One side of the scroll is for the thieves, and the other side is for the liars."
   - "first/second half" → "one side/the other side" 의역, 양쪽 모두 지칭하므로 내용 손실 없음. 오탐.
3. ch10 idx3 [badge 6-12] `name: assyrian`
   - MSG "round them up from the Assyrian east" → TEEN "gather them from Assyria in the east"
   - 형용사(Assyrian)→명사(Assyria) 변환일 뿐 앗수르 지칭 유지. 오탐.
4. ch10 idx3 [badge 6-12] `quote: brimming, leafy, brash`
   - MSG 시적 대구 "their lives brimming with joy" → "their lives just filled with good vibes",
     "back to sweet Gilead, back to leafy Lebanon" → "the good land of Gilead and Lebanon",
     "brush aside brash ocean waves" → "pushing past any obstacle"
   - teen paraphrase에서 시적 수식어를 압축한 것으로 의미 보존. 검사기의 quote 키워드 휴리스틱 한계. 오탐.
