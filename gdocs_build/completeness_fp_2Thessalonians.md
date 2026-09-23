# completeness_check 오탐 기록 — 2Thessalonians (2026-09-23)

검사: `python3 gdocs_build/completeness_check.py fixes/en_2Thessalonians.json`
결과: 3장 19문단 검사, FAIL 3건 → 전부 오탐으로 판정 (아래). 잔여 FAIL 0.

## FP-1: ch1 idx0 [badge 1-2] name 'thessalonian'
- MSG: "greet the church of the **Thessalonian** Christians"
- TEEN: "giving a shout-out to our crew in **Thessalonica**"
- 판정: 오탐. 지명 "Thessalonica"가 문단에 존재. 형용사형("Thessalonian") 미사용은 teen-voice 자연스러움 — 의미·지시 대상 동일.

## FP-2: ch2 idx1 [badge 1-3] name 'apostasy'
- MSG (unit 3-5): "First, the **Apostasy**"
- TEEN (P2, badge 3-5): "First, a bunch of people are gonna totally ghost God — a massive **falling away**"
- 판정: 오탐. 전문 용어 "Apostasy"를 정의로 푼 teen paraphrase ("massive falling away"). 개념 완전 보존.

## FP-3: ch2 idx1 [badge 1-3] name 'almighty'
- MSG (unit 3-5): 'set himself up in God\'s Temple as **"God Almighty"**' (인용구)
- TEEN (P2, badge 3-5): 'walk into God\'s own Temple and set himself up, declaring, **"I am God Almighty"**' (2차 감사에서 복원됨 — 수정 전에는 "I'm God now"였음)
- 판정: 오탐 (수정 후 해소). 자칭 신격화 주장이 인용구 형태로 보존됨.

## FP-4: ch2 idx1 [badge 1-3] number '2'
- MSG (unit 3-5): "a couple of things… **First**… **Second**…"
- TEEN (P2, badge 3-5): "a couple of things have to happen first. **First**, … **Then**, the ultimate enemy shows up"
- 판정: 오탐. "First…Then"으로 2단계 순서가 명시됨. 서수 "Second"의 토큰 부재는 teen-voice 범위.

## 검사기 수정 기록
- `gdocs_build/completeness_check.py`: badge 정렬 로직 수정. 기존에는 `msg_ranges` 길이가 checkable 문단 수와 다르면 장 전체를 건너뜀 (ch3의 10-13→2문단 split 때문에 ch3 10문단 미검사). 이제 `msg_ranges` → `verseRanges` 순서로 정렬 가능한 목록을 선택. 1Thessalonians 회귀 PASS 확인.
