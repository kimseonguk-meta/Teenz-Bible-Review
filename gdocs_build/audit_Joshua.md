# Joshua(여호수아) 재확인 리포트 (2026-09-24, 재확인 작업자)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1.
방법: 처음부터 재감사가 아닌 독립 재검증 — 7개 게이트 직접 재실행 + 기계적 FAIL 43건 전수 수동 분류.
이전 상태: OT_CHECKPOINT에 "게이트 PASS는 재확인 필요"로 기록됨 (1차 감사의 게이트 통과 미확정).

## 1. 발견된 실제 문제 및 수정

### (가) build_gdocs.py MSG 파서 버그 — 14:15/15:1 장 경계 오짝지음 (근본 원인 수정)
- 현상: `msg_Joshua.txt`에서 14장 마지막 절이 단일 번호 "15 The name of Hebron used to be Kiriath Arba..."이고, 15장이 "15 The lot for the people of Judah..."(장번호=1절 형태)로 열리는데, 파서의 모호성 분기(`nn == cur_ch+1`)가 첫 번째 "15"를 15장 1절로 오판.
- 결과: Google Doc에서 MSG 셀 "The name of Hebron used to be Kiriath Arba..." ↔ 틴 "유다 지파 땅 경계(Edom·Zin)" 행이, MSG 셀 "The lot for the people of Judah..." ↔ 틴 "Caleb이 Anakim을 쫓아냄" 행이 서로 바뀌어 표시됨 (게이트 6 위반 — 읽는 사람 눈에 명백히 틀림).
- 수정: `parse_msg_lines()`에 `next_single_num()` 헬퍼 추가. `nn == cur_ch+1` 모호 상황에서 다음 절-번호 행이 같은 번호의 단일 번호("N <text>")이면 현재 행은 구 장의 마지막 절로 판정 (장 마커 뒤에는 같은 번호가 다시 올 수 없다는 구조적 근거).
- 안전성 검증: 수정 전/후 58개 msg_*.txt + Matthew + Romans 파싱 전체 비교 → 변경된 책은 Joshua 1권뿐, 변경된 단위는 (14,[15])·(15,[15]→[1]) 2건뿐. 나머지 중복 번호 패턴(Joshua 2:1→2:2, Ruth 2:1→2:2, SongOfSongs)은 기존 분기가 정상 처리하므로 영향 없음.
- docx 재빌드 후 ch14:15/ch15:1 행 짝지음 정상 확인.

### (나) 내용 누락 2건 수정 (EN/KO)
| 장:절 | MSG 요지 | 문제 | 수정 |
|---|---|---|---|
| 20:7 | "Kedesh in Galilee in the hills of Naphtali" | EN에서 "in the hills of Naphtali" 누락 (KO는 보존 → EN-KO 불일치까지) | EN: "Kedesh in Galilee, in the hills of Naphtali, Shechem in the hills of Ephraim, ..." |
| 22:32-33 | "left the Reubenites, Gadites, and the half-tribe of Manasseh (from Gilead)" | EN·KO 모두 "half-tribe of Manasseh" 누락 ("the Reubenites and Gadites"만) | EN: "...left the Reubenites, Gadites, and the half-tribe of Manasseh in Gilead..." / KO: "길르앗에 있던 르우벤, 갓 지파와 므낫세 반 지파를 떠나" |

### (다) 슬랭 6 Rule 위반 8건 수정
- EN ch6: "Marching and trumpets, that was the vibe!" → "that was the whole scene!" (R1 vibe)
- KO 대박 5건 → 순화: ch3 "진짜 대박적인 일들"→"진짜 놀라운 일들", ch3 "대박이지"→"진짜 대단하지", ch6 "대박 큰 소리"→"엄청 큰 소리", ch12 "완전 대박이지"→"완전 대단하지", ch22 "대박 큰 제단"→"엄청 큰 제단" (R4)
- KO 멘탈 2건 → 순화: ch2 "멘탈 나갔다"→"넋이 나갔다", ch7 "멘탈이 완전 나갔어"→"완전히 얼어붙었어" (R5)
- 오탐으로 유지: R6 chill(4건)·bro(1건, 변경 금지), "woke up"은 해당 없음(Joshua).

## 2. 기계적 완전성 검사 잔여 FAIL 40건 — 전수 수동 분류 결과
수정 2건 반영 후 41→40건. 40건 전부 검토 완료:
- 38건은 오탐 (단복수·동의어·대명사·호칭): Reubenites→"tribes of Reuben", God→"LORD", Shinar→"Babylonia"(동일 지명), Arabah Sea→"Dead Sea"(동일 지명), "a second time"→"again", "the first"→"last time", "Not one town"→"Not a single town", "the third"→"The third one", crusts/tatters→"hard and moldy"/"wrecked", glean 계열→"leftovers", designate→"set up", obediently→"Obey", sanctify→"Get yourselves ready and be respectful", "said to Reuben, Gad, and Manasseh"→"said to them"(직전 문단 지시 대상 명확) 등.
- "son of Zerah"(7:24): ch7 idx0에서 "son of Carmi, son of Zabdi, son of Zerah"로 이미 확립 → 생략 허용.
- "son of Eleazar"(22:33): idx7 "son of the priest Eleazar"·idx20 "Priest Phinehas, son of Eleazar"에서 확립 → 생략 허용.
- 경계선상 허용 2건 (판정 기록): "the valley (the Arabah)"(11:18)→"the valley" (MSG 괄호 부연, 지시 대상 동일), "Sihon king of Heshbon"(12:5)→"King Sihon's land" (Heshbon 지명은 ch13 틴에 등장, 경계 표현의 핵심=누구의 경계인지는 보존).
- 결론: 기계적 FAIL 40건 중 실제 누락은 0건 (2건은 위 (나)에서 수정済).

## 3. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사(이슈 리포트) | 위 1항 (파서 버그 1 + 누락 2 + 슬랭 8 = 11건 수정) |
| ② 수정 반영 | PASS (merge/split 없음 — 컨펌 불필요) |
| ③ validate_translation.py | PASS (24장, exit 0) |
| ④ 기계적 완전성 검사 | 조건부 PASS — 40건 전수 수동 분류, 실제 누락 0건 (2건 수정済). 체커 자체는 FAIL을 뱉지만 전부 문서화된 오탐/허용 의역 |
| ⑤ build_gdocs.py 재빌드 | PASS (VERIFY_DROPPED=0, rows=340, msg_units=304, orphans=0) |
| ⑥ verify_pairing_content.py | PASS (340행). 파서 수정 전에는 ch15 2행이 오짝지음 → 수정 후 정상. MSG_SUPERSET 4건(ch14:1-2, ch19:8-9, ch22:7-8)은 MSG 한 문단이 절 경계를 가로질러 틴이 분리한 구조적 artifact — 내용 누락 없음, 공유 MSG 블록이 양 행에 표시됨 |
| ⑦ Google Docs 재업로드 + API 검증 | 미실시 — 텍스트 변경(11건) 있어 재업로드 필요. upload_ot_f.py가 Joshua를 모르므로 코디네이터에게 보고 (직접 업로드 금지 지시 준수) |

## 4. 검증 범위 및 미확인 경계
- 검증한 것: 7개 게이트 재실행, 파서 수정 전/후 60개 소스 전체 파싱 diff, 기계적 FAIL 43건 전수 대조(MSG 원문↔틴), 슬랭 6 Rule 전수 재검색(정규식+수동 문맥 판정), docx 실제 셀 렌더링 확인(ch14:15/ch15:1, ch14:1-2 공유 블록).
- 미확인: Google Docs 웹 화면 직접 확인 불가(이 환경). production 앱 미접촉. ⑦은 코디네이터 재업로드 후 API 검증 필요.
- "완료" 선언은 성욱만 가능 — 본 리포트는 완료 선언이 아님.

---

# Joshua 2차 심층 재검토 기록 (2026-09-25)

기준 변경: 9-24 재확인의 "초출에서 확립 → 생략 허용" 판정을 폐기. "축약하지 마라" + 부칭(모든 "son of X") 전부 보존 + KO에만 있고 EN에 빠진 비대칭 특별 검사 기준 적용. (2사무엘 2차 스윕에서 son of Ner 6건·son of Zeruiah 4건을 반복 출현마다 복원한 선례와 동일 기준.)

방법:
- side-by-side 덤프 1–24장 전수 수동 독해 (2,007줄).
- completeness checker 39건 전수 분류 → 실제 6건 복원, 33건은 오탐(단복수·동의어·대명사·호칭·동일 지명·인용구 의역·뒤 문단 분산).
- MSG 전체 "X son/daughter/father of Y" 29건 전수 추출 → 대응 틴 문단에서 Y 이름 존재 여부 전수 확인 → 복원 후 잔여 0건.
- KO "X의 아들" 전수 추출 → EN 대응 확인 → possessive 오탐 제외하고 비대칭 실건 0건 추가.

## 복원 6건

| 장:절 | MSG | 문제 | 수정 |
|---|---|---|---|
| 7:24 | "Achan son of Zerah" | EN·KO 모두 "Achan/아간"만 (9-24 "확립→허용" 판정 폐기) | EN: "took Achan son of Zerah" / KO: "세라의 아들 아간" |
| 11:16-20 | "the valley (the Arabah)" | EN "the valley"만 — KO는 "아라바 골짜기" 보유 (비대칭) | EN: "the valley (the Arabah)" |
| 12:4-5 | "the border of Sihon king of Heshbon" | EN "King Sihon's land" — KO는 "헤스본 왕 시혼의 경계" 보유 (비대칭) | EN: "the border of Sihon, king of Heshbon" |
| 17:1 | "Makir, Manasseh's firstborn and father of Gilead" | EN에 "father of Gilead" 없음 — KO는 "길르앗의 아버지인 마길" 보유 (비대칭) | EN: "Makir, Manasseh's oldest, the father of Gilead, and a total beast in battle" |
| 22:31 | 'said to Reuben, Gad, and Manasseh' | EN "said to them" — KO는 "르우벤, 갓, 므낫세 지파한테" 보유 (비대칭) | EN: "said to Reuben, Gad, and Manasseh" |
| 22:32-33 | "Then Priest Phinehas son of Eleazar left" | EN "Then Phinehas" / KO "제사장 비느하스" — 부칭 전체 누락 (9-24 "확립→허용" 판정 폐기) | EN: "Then Priest Phinehas, son of Eleazar, and the chiefs left" / KO: "제사장 엘르아살의 아들 비느하스와 지도자들은" |

## 오탐으로 확정 (33건)
- Reubenites/Gadites→"tribes of Reuben, Gad"/"men of Reuben, Gad" (ch1,4,12,22 다수): 동등 호칭.
- God→"LORD", Levitical→"priests"(ch3:1-5 — 단, v33·ch8에서는 "Levitical priests" 유지), "Sanctify yourselves"→"Get yourselves ready and be respectful" (ch3:5): 틴 의역.
- Arabah Sea→"Dead Sea"(ch3:14-16), Shinar→"Babylonia"(ch7:20-21): 동일 지명.
- 숫자: "a second time"→"again"(ch5:2-3), "the first time"→"again"(ch10:7-8), "a second thought"→관용구(ch8:3-8), "Not one town"→"Not a single town"(ch11), "One of them"→"anyone"(ch2:17-20).
- Geshurites→"Geshurite areas"(ch13), Amorites/Ammonites/Geshur/Maacah→형용사형(ch13:9-13), Amorites/Midian→뒤 문단(v16-22) 분산(ch13:15), Anak→"Anakim"(ch15:13), Arkites/Japhletites→"Arkite territory/Japhletite area"(ch16:1-3), Ephraimites→"tribe of Ephraim"(ch17:7-10), Levites/Merarites→"Levite/Merarite families"(ch21), Canaanite→"Canaan"(ch22:9), Gilead→"Gilead and Bashan" 문맥(ch13:1-2).
- 인용구 "crusts, tatters"→"hard and moldy"/"wrecked" — 세부 전부 보존된 의역(ch9:12-13).
- "said to Reuben, Gad, and Manasseh"→"said to them" 판정은 22:31에서 복원으로 해결 (9-24 "직전 문단 명확" 판정 폐기 — 비대칭 기준 우선).
- designate→"set up"(ch20:1-3), obediently→"Obey"(ch23:6-8): 동등 동사형.

## 슬랭
- "hit up", "Yo", "Bro", "dudes", "lowkey", "chill" 등 과도한 슬랭 다수 관찰. 9-24 재확인에서 6 Rule 위반 8건 수정済. 잔여는 Rule 내 허용 범위 — 이번 2차에서는 추가 수정 없음.

## 성욱 판단용으로 남길 것
- 없음. 9-24 "경계선상 허용" 2건(Arabah, Heshbon)은 비대칭(KO 보유) 근거로 복원 확정.
