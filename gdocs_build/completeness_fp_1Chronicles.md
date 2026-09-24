# completeness_check 오탐 근거 — 1Chronicles (2026-09-24)

공식 검사기 `gdocs_build/completeness_check.py` 실행 결과 26건 FAIL.
전수 대조 결과 26건 모두 오탐으로 판정. 의미·이름·숫자 모두 Teen EN에 존재하며,
검사기가 요구하는 것은 MSG의 원형 단어와 teen paraphrase의 자연스러운 표현 차이다.

## 판정 기준
- MSG의 이름·숫자·인용구 의미가 Teen EN에 남아 있으면 오탐
- 단수/복수, 하이픈, 어순, teen식 표현 변경은 오탐

## 오탐 목록 (26건)

| # | 위치 | 검사기 지적 | Teen EN 실제 | 판정 근거 |
|---|------|------------|--------------|-----------|
| 1 | ch2(1) | canaanite | "from Canaan" | 의미 동일 |
| 2 | ch4(0) | zorathites | "Zorathite families" | 복수형 변형 |
| 3 | ch4(11) | judean | "from Judah" | 의미 동일 |
| 4 | ch5(8) | hagrite | "the Hagrites" | 복수형 존재 |
| 5 | ch6(4) | kohathites | "Kohathite family" | 단수형 존재 |
| 6 | ch6(8) | holies | "Most Holy Place" | Holy of Holies의 teen 표현 |
| 7 | ch7(4) | number 1 | "during a raid" (MSG "one of their raids") | 사소한 관사 수준 |
| 8 | ch9(0) | annals | "official records" (MSG "Royal Annals") | 의미 동일 |
| 9 | ch9(2) | shilonites | "Shilonite crew" | 단수형 존재 |
| 10 | ch11(3) | singlehandedly | 검사기 오배정 (MSG 11:10-11에 해당 단어 없음) | 실제 단어는 EN(4)에 "single-handedly"로 존재 |
| 11 | ch11(7) | singlehandedly | "single-handedly" | 하이픈 표기 |
| 12 | ch11(8) | moabites | "Moabite warriors" | 단수형 존재 |
| 13 | ch11(9) | benjaminite | "from Gibeah of Benjamin" | 의미 동일 |
| 14 | ch15(3) | levitical | "Levite families" | 의미 동일 |
| 15 | ch15(5) | levites | "Levite leaders" | 존재 |
| 16 | ch18(6) | edom | "the Edomites" | 존재 |
| 17 | ch19(6) | number 2 | "from the front and the back" (MSG "two fronts") | 의미 동일 |
| 18 | ch23(4) | holies | "Most Holy Place" | 6번과 동일 |
| 19 | ch24(8) | number 1 | "was the top guy" (MSG "was the first") | 의미 동일 |
| 20 | ch26(6) | izharites, hebronites | "Izharite family", "Hebronite family" | 단수형 존재 |
| 21 | ch26(7) | hebronites, hebron, reubenites, gadites | "Hebronite family", "Hebronite family tree", "Reubenites", "Gadites" | 모두 존재 (단수/복수 변형) |
| 22 | ch27(13) | administrators | "the guys in charge of the tribes' business" | 의미 동일 |
| 23 | ch28(2) | number 1 | "all of God's commands" (MSG "every last one") | 의미 동일 |
| 24 | ch29(0) | quote: untested, varicolored, stockpiles, artisans | "still has a lot to learn", "colorful", "massive piles", "artists" | 모두 teen paraphrase로 존재 |
| 25 | ch29(2) | god | "the temple treasury" (MSG "treasury ... of The Temple of God") | 의미 동일 |
| 26 | ch29(6) | quote: shiftless, uncluttered | "aimless", "clear" | teen paraphrase로 존재 |

## 실제 누락으로 판정되어 복원한 항목 (검사기 지적 외 별도 대조에서 발견)
이들은 위 오탐 목록에 포함되지 않으며, 본문에 이미 복원 완료:
- ch1 Keturah "concubine", ch4 Ir Nahash / Ge Harashim / Gedor(Gerar)+east of valley,
  ch5 Senir, ch13 Pond of Horus+방위, ch18 Aram-Damascus / Great Bronze Sea / Ahilud / Hamath / king of Zobah,
  ch19 37.5 tons + Naharaim/Zobah, ch21-22 선언문 위치 정정, ch22 Sidonians and Tyrians / talent 원수+톤수 / God's Revelation,
  ch23 Meal/Whole-Burnt-Offerings, ch26 sons of Asaph, ch27 (원복), ch28 (원복),
  ch29 talent 원수+톤수 / Jehiel the Gershonite / drink offerings 등
- 검사기 지적 중 실제 복원: ch1 "three", ch3 "Second", ch10 "all four", ch12 Gibeathite/Anathothite/Gadites,
  ch14 "two steps ahead", ch21 Jebusite×2 + "pray to God", ch27 "twelve months"
