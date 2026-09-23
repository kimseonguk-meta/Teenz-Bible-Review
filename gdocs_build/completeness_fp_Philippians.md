# Philippians completeness_check 오탐 문서 (2026-09-23)

checker: gdocs_build/completeness_check.py on fixes/en_Philippians.json
결과: 4장 38문단(헤더 제외), 77 name tokens, 5 number tokens, 0 quoted spans — FAIL 10건.
전수 수동 대조 결과 10건 전부 오탐. 클래스: D(호칭 교체) 9건, C(관용구) 1건.

## 오탐 목록

| # | 위치 | 토큰 | MSG | Teen EN | 판정 |
|---|---|---|---|---|---|
| 1 | ch1 idx3 [7-8] | christ | "I feel as strongly about you as **Christ** does!" | "on the same wavelength as **Jesus** about you" | D: Christ→Jesus 호칭 교체. 의미 동일 |
| 2 | ch1 idx4 [9-11] | christ | "making **Jesus Christ** attractive to all" | "making **Jesus** look good to everyone" | D: 호칭 교체 |
| 3 | ch1 idx6 [12-14] | messiah | "because of this **Messiah**… about the **Messiah**" | "because of **Jesus**… about God and **Jesus**" | D: Messiah→Jesus 호칭 교체 |
| 4 | ch1 idx7 [15-17] | christ | "some here preach **Christ**" | "preaching about **Jesus**" | D: 호칭 교체 |
| 5 | ch1 idx8 [18] | christ | "**Christ** is proclaimed" | "they're talking about **Jesus**" | D: 호칭 교체 |
| 6 | ch1 idx8 [18] | number 1 | "Every time **one of them** opens his mouth" | "every time **they** open their mouths" | C: "one of them"은 관용적 표현, 숫자 콘텐츠 아님. 의미 보존 |
| 7 | ch1 idx10 [22-26] | christ, god | "be with **Christ**… praising **Christ**… this life of trusting **God**" | "being with **Jesus**… praising **Jesus**… joyful in **your faith**" | D+F: 호칭 교체 + "trusting God"→"your faith" paraphrase. 의미 보존 |
| 8 | ch1 idx11 [27-30] | christ | "the Message of **Christ**… trusting in **Christ**" | "the message of **Jesus**… trusting in **Jesus**" | D: 호칭 교체 |
| 9 | ch2 idx1 [1-4] | christ | "following **Christ**" | "following **Jesus**" | D: 호칭 교체 |
| 10 | ch2 idx6 [14-16] | christ | "on the day that **Christ** returns" | "when **Jesus** comes back" | D: 호칭 교체 |

실제 누락 0건. 수정 없음.
