# 역대기상 (1Chronicles) MSG 전수 감사 기록 — 2026-09-24

기준: Eugene Peterson The Message(MSG)만이 최종 기준. EN이 primary, KO는 EN과 문단 수·순서·배지·의미 1:1.
구약 수정본은 production 앱에 반영하지 않는다.

## 수정 건수 (백업 20260924 대비)
- EN 본문: 66문단 수정 / 배지: 1건 수정 (ch22 '4-6'→'5-6')
- KO 본문: 39문단 수정 / 배지: 27건 수정
- EN 총 367문단, KO 총 367문단

## 주요 복원 (MSG 대비 누락·오역)
- ch1: Keturah를 "concubine"으로 정정 (기존 "other wife")
- ch1: "three main family lines" (three 복원)
- ch3: "Second was Daniel" (second 복원)
- ch4: Ir Nahash('City of Smiths'), Ge Harashim('Colony of Artisans') 이름 복원
- ch5: Senir (Mount Hermon) 복원 — KO는 이미 "스닐" 보유
- ch10: "all four of them" (four 복원)
- ch12: the Gibeathite / the Anathothite / Gadites 명칭 복원
- ch13: "Egypt's Pond of Horus in the southwest" ~ "Pass of Hamath in the northeast" 복원
- ch14: "two steps ahead of you" 복원
- ch18: Aram-Damascus, Great Bronze Sea, Ahilud(오기 Ahilod 정정), Hamath, "Hadadezer king of Zobah" 복원
- ch19: "a thousand talents of silver (thirty-seven and a half tons!)", Naharaim·Zobah 복원
- ch21→ch22: "From now on, this is the site for the worship of God..." 선언문을 ch21 끝에서 제거하고 ch22 첫 문단 앞으로 이동 (MSG 원문 구조 정정)
- ch21: "Araunah the Jebusite" ×2, "pray to God" 복원
- ch22: Sidonians and Tyrians 명칭 복원, "100,000 talents of gold (3,775 tons) / 1,000,000 talents of silver (37,750 tons)" 원수+환산 병기, "God's Revelation" 복원
- ch23: "Meal Offerings", "Whole-Burnt-Offerings" 명칭 복원
- ch26: "one of the sons of Asaph" 복원
- ch27: "twelve months" 복원
- ch29: 3,000/7,000 talents, 5,000 talents+10,000 darics, 10,000/18,000/100,000 talents 원수+톤수 병기, "Jehiel the Gershonite", "drink offerings" 복원
- KO ch12(7): "지휘관들 밑에 배정" → "습격 부대의 지휘관으로 삼았대" (MSG 12:18 정정)

## 검증 후 원복한 오수정 (MSG 재확인 결과)
- ch25 "zither"→"harp" 변경 원복 (MSG는 "playing the zither")
- ch25 "cymbals, lyres, and harps" 추가 철회 (MSG 25:1-7에 해당 목록 없음)
- ch26 "Jehieli, his son Zetham, and his brother Joel" → 원문 "Jehieli, and his sons Zetham and his brother Joel"로 원복
- ch27 "Pirathonite/Hakmoni" → MSG 정본 "Pirathomite/Hacmoni"로 원복
- ch28 "dishes" 추가 철회 (MSG 28:17에 없음)

## 과도한 슬랭 정리 (뜻 보존)
here's the tea, no cap, lowkey, worked my butt off, smoked, W's, hit up, squad, dudes/dude, crazy, GOATs, pulled up, ghost, bestie(찐친), chilling, totally owned, wrecked, booking it, 'Bet' 등 → teen voice를 유지하는 중립 표현으로 교체. EN/KO 양쪽 적용.

## 구조 선언 (순수 구조 차이, 내용 변경 없음 — 원칙 4)
- KO ch10: 1문단 → 2문단 분할 (EN 7문단과 일치)
- KO ch12: 1문단 → 2문단 분할 (EN 12문단과 일치)
- KO ch25: 2문단 → 1문단 병합 (EN 4문단과 일치)
- baseline 구조 오류 6개 장(ch1, 5, 8, 10, 12, 25) 전부 해소

## Pairing 참고
- ch21: MSG 원문 라벨 "28-29"와 teen 배지 "28" 불일치 1건. MSG 해당 유닛의 실제 내용은 28절 문장만이며, 29-30절은 다음 문단이 커버. 내용 누락 없음 (원문 라벨 아티팩트).

## 게이트 결과
- validate_translation.py: PASS (29개 장 모두 통과)
- completeness_check.py: 39건 → 26건, 26건 전부 오탐 (근거: gdocs_build/completeness_fp_1Chronicles.md)
- build_gdocs.py: 367행, VERIFY_DROPPED=0, PAIRING_MISMATCH 1건(상기 ch21, 내용 이상 없음)
- verify_pairing_content.py: PAIRING CONTENT OK (367 rows, 29 tables)
- Google Docs 업로드: "역대기상 (1Chronicles): MSG + Teen EN + KO" — 테이블 29/29, export-back VERIFIED OK
  - https://docs.google.com/document/d/1-UU6TifGyxWZcVaR49gu0CMj4rGaB4fpxPtYS_uQ-XU/edit?usp=drivesdk

## 승인 필요 항목
- 없음. 내용 누락·오역은 모두 복원했고, 구조 차이는 순수 가독성 수준으로 선언했다.
- ch3 MSG "Shecaniah... six of them" (이름은 다섯) — 정본 자체 표현이므로 그대로 둠.

## 검증 범위와 미확인 경계
- MSG 29장 전체 유닛(290유닛)과 Teen EN 367문단을 문장 단위로 대조. KO는 최종 EN 기준 전수 대조.
- 이름 검사기 후보 중 일반명사성 항목(Canaanite, Judean, Holy of Holies, Pastures, Royal Annals, Benjaminite, Levitical 등)은 의미가 보존되어 있어 원형 복원하지 않음.
- 구약은 production 앱에 반영하지 않음 (사용자 지시).

## 2nd re-audit (Sep 24)
- 기준: MSG 원문 문장 단위 대조 ("축약하지 마라" 엄격 적용). 족보 이름·호칭("son of X") 전수 확인. completeness_check 26건 → 2건 실제 누락 복원, 잔여 24건은 오탐(동의어·단복수·문단 분할)으로 판정.
- 복원 2건 (EN; KO는 이미 보유):
  - ch18 [12-13]: "He set up a puppet government in Edom" — EN "there"로 축약 → "a government in Edom" 복원 (KO는 이미 "에돔에도" 보유)
  - ch29 [6-8]: "the treasury for the building of The Temple of God" — EN "the temple treasury"로 축약 → "the treasury of the Temple of God" 복원 (KO는 이미 "하나님의 성전 창고" 보유; 느헤미야 2차 기준과 일치)
- 게이트: STRUCT OK, build VERIFY_DROPPED=0 / teen_without_msg=0 / msg_orphans=0, docx pairing 2건 육안 확인, GDocs 29/29 VERIFIED OK.
- PAIRING_MISMATCHES=1 (ch21 idx15, MSG_SUPERSET): msg_1Chronicles.txt 원본이 29절을 [28,29]·[29,30] 두 유닛에 중복 귀속시킨 artifact. Teen 분할(idx15 badge 28 / idx16 badge 29-30)은 내용상 정확하고 양쪽 MSG 유닛 모두 대응됨. 내용 손실 없음 — 수정 없이 기록.
- 판단 보류(성욱용): "Holy of Holies" → "Most Holy Place" (ch6/ch23, 표준 동의어로 보고 유지), "Royal Annals" → "official records" (ch9, 의미 동등으로 보고 유지).
