# James 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG(5장 43개 유닛) vs EN vs KO 문단별 전수 대조 (5장, EN/KO 각각 53행). 3개 워커(ch1-2/ch3-4/ch5)가 전수 대조 후 지적 사항을 MSG·EN·KO 실제 텍스트로 다시 직접 확인하고 최종 판정.
결과: 텍스트 수정 7건(모두 KO). merge/split 신규 후보 0건.

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| ch1·2 타이틀 | — | KO 타이틀 키 자체 누락 (5장 전부) | KO 1장 "최고의 변화", 2장 "가짜 믿음은 그만" 부여 (EN: "The Ultimate Transformation" / "Don't Be a Poser"). ch3 "입조심!", ch4 "시기 질투는 그만", ch5 "부자들의 문제, 그리고 진짜 MVP 되는 법"도 함께 부여. |
| 2:5-7 | "And here you are **abusing** these same citizens!" | KO 의미 축소 | KO "무시하고 있어" → "괴롭히고 있어". "학대/괴롭힘"이 "무시"로 약해졌던 것을 복원. |
| 1:19-21 | "So throw all **spoiled virtue** and cancerous evil in the garbage." | KO EN 드리프트 | KO "썩은 습관" → "썩은 덕". "virtue(덕/선행)"이 "습관"으로 바뀐 것을 정정. |
| 2:1-4 | "...**haven't you** segregated God's children and proved that you are judges who can't be trusted?" | KO 구조 이탈 | KO 평서문 "…믿을 수 없는 재판관임을 증명한 거야." → 의문형 "…믿을 수 없는 재판관임을 증명한 거 아니야?" 복원 (EN은 의문 유지). |
| 4:16-17 | "In fact, if you know the right thing to do…" | KO 창작 추가 | KO "그리고 결정타는 이거야." → "사실은,". EN의 담화 표지 "In fact"가 수사적 강조 문장으로 부풀려진 것을 정정. |
| 4:16-17 | "…that, for you, *is* **evil**." | KO 의미 드리프트 | KO "그게 너희에게는 *바로 죄*야." → "그게 너희에게는 *바로 악한 거*야." 바로 앞 문장에서 "evil"을 "악"으로 옮겨놓고 이 문장에서만 "죄"로 바뀐 것을 정정. |
| 3:17-18 | "You can… enjoy its results ***only*** if you do the hard work…" | KO 논리 요소 누락 | KO에 배타적 조건 *only* 복원: "…수고를 할 때*만*, 하나님과 바르게 사는 건강하고 튼튼한 공동체를 만들고…". |

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)
- § 헤더 8개 전부 MSG 공식 헤더와 1:1 ("Faith Under Pressure", "Act on What You Hear", "The Royal Rule of Love", "Faith in Action", "When You Open Your Mouth", "Live Well, Live Wisely", "Get Serious", "Nothing but a Wisp of Fog", "Destroying Your Life from Within", "Prayer to Be Reckoned With"). 창작 헤더 0.
- 이미 선언된 split 3건이 MSG 구조와 정확히 일치: ch3 3-6(v5 공유), ch3 7-12(v10 공유), ch4 1-3(v2 공유). EN/KO 모두 선언됨.
- ch4 EN 챕터 타이틀 "Quit Being a Salty Hater": "salty"는 mild teen slang, 과도한 슬랭 예시에 해당하지 않음. 유지.
- KO 2:19-20 "마귀들"(Demons), 2:25-26 "창녀"(harlot): MSG 원어 그대로 유지, 순화 대상 아님.
- KO 1:1 "다들 잘 지내지?" 추가, KO 1:19-21 앞 "§들은 대로 행하라", KO 2:1-4 "이런 상황을 상상해봐" 등 담화 표지: teen voice 범위. 유지.
- MSG "* * *" 장식 구분선(4-6↔7-8 사이) 미포함: 내용 없는 장식 기호. 유지.
- 욕설/과도한 슬랭 스캔: EN/KO 모두 0건.

## 2. 구조 검사
- EN/KO 문단 수·순서·배지 1:1 (5장 53행). null 배지 0.
- `verseRanges == msg_ranges` 일치 (선언된 split 3건 포함).
- 고유명사 전수: James, twelve tribes, Abraham, Isaac, Rahab, Jericho, Job, Elijah, Jesus, Christian 전부 등장. 숫자·인용: "three and a half years"→"3년 반", "I swear to God"→"하나님께 맹세하는데", Master Avenger→"복수하시는 주님".

## 3. merge/split 후보
- 신규 후보: **0건**.
- 기존 선언분: ch3 3-6, ch3 7-12, ch4 1-3 (splits, MSG 구조와 일치 확인).

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (5장 43 MSG 유닛 전수, 직접 대조) |
| ② 이슈 리포트 | PASS (위 7건) |
| ③ 수정 | PASS (KO 7건 적용) |
| ④ validator | PASS (5개 장 모두 통과) |
| ⑤ 기계적 완전성 | PASS (43문단 FAIL 0 — 오탐 문서 불필요) |
| ⑥ Docs 재빌드 | PASS (VERIFY_DROPPED=0, 53 rows, 5 tables) |
| ⑦ 실제 내용 짝지음 검증 | PASS (43 data rows, PAIRING CONTENT OK) |
| ⑧ Google Docs 재업로드/API+export-back 검증 | PASS (API table 5/5, export-back VERIFIED OK) |
