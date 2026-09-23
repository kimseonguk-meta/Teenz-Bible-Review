# completeness_check 오탐 기록 — 2Corinthians (2026-09-23)

검사: `python3 gdocs_build/completeness_check.py fixes/en_2Corinthians.json`
결과: 90문단 / 134 name tokens / 20 number tokens 검사 → FAIL 5건.
그 중 1건(고유명사 messiah)은 실제 문제였고 EN ch3 P6에서 복원 완료
(수정 후 재검사에서 사라짐). 아래 4건은 검사기 한계로 인한 오탐이므로
FP로 문서화한다.

## 1. ch1 P6 [15-16] number: 2 (오탐)
- MSG: "I had originally planned **two** great visits with you"
- TEEN: "I was planning to visit you **twice**."
- 근거: 수는 문장 안에 그대로 존재. 검사기가 숫자 "2" 자릿수만 찾고
  영단어 형태("twice")를 인식하지 못하는 한계. 실제 의미 손실 없음.

## 2. ch2 P2 [5-8] number: 1 (오탐)
- MSG: "regarding the **one** who started all this" / "I am not the **one** injured"
- TEEN: "About the **guy** who started all this mess" / "He didn't just hurt me"
- 근거: "one"은 수량이 아니라 대명사(그 사람/나). 10대 영어에서
  "the guy"가 자연스러운 표현. 수량 의미가 아님.

## 3. ch4 P5 [13-15] number: 1 (오탐)
- MSG: "the **One** who raised up the Master Jesus"
- TEEN: "the same **God** who brought Jesus back to life"
- 근거: "One"은 하나님을 가리키는 대명사. TEEN이 "God"으로 풀어씀.
  수량 의미가 아님.

## 4. ch5 P3 [11-14] number: 1 (오탐)
- MSG: "His love has the **first** and last word in everything we do"
- TEEN: "His love is the **boss** of everything we do."
- 근거: "first"는 순서가 아니라 관용 표현("the first and last word" = 최종 권위).
  TEEN "the boss"가 의미를 정확히 전함. 수량 의미가 아님.

## 결론
4건 모두 검사기 오탐. 재수정 불필요. (1Cor audit FP 패턴과 동일한 유형)
