# 사무엘상 (1Samuel) 감사 보고서 — 2026-09-24

## 범위
- 책: 사무엘상 / 1Samuel (구약 5/27)
- 파일: `msg_1Samuel.txt` (MSG 원문), `fixes/en_1Samuel.json` (Teen EN), `fixes/ko_1Samuel.json` (KO)
- 규모: 31장, EN/KO 각 530문단, MSG 438 유닛

## 1. MSG 원문 소스 정정 (중대 — 반드시 공개)
- 작업 시작 시 "MSG 428유닛 완성"이라는 전제가 **사실이 아니었음**을 발견.
- 원인: `fetch_msg_bg.py`의 passage 추출 정규식이 첫 번째 중첩 `</div><div>`에서 멈추는 바람에 **2장 2~36절 전체가 누락**되어 있었음.
- 근본 수정: passage 추출 종료 조건을 `passage-scroller` 경계 기준으로 변경.
- 결과: 2장 전체(2:1–36, 29개 정경 행) 복원 → **MSG 428유닛 → 438유닛**.
- 이후 모든 대조는 438유닛 기준으로 수행됨.

## 2. 구조 정정 (배지/스플릿)
- 기존 Teen 배지들이 실제 MSG 분할 관계를 가리고 있었음. `msg_ranges`를 파싱된 MSG 유닛 기준으로 재구축하고, 형식적인 최상위 `splits` 선언을 추가 (29개 장).
- EN/KO 문단 수·순서·`verseRanges`·`splits` 전 책 일치 확인 (병합 없음).
- **28장 배지 오정렬 발견 및 수정** (EN/KO 동일): 7~11절 구간에서 배지가 한 절씩 밀려 있었음.
  `7→'8', 8→'9', 9→'10', 10→'11', 11a→'12'` 를 `7→'7', 8→'8', 9→'9', 10→'10', 11a→'11'` 로 정정, split `7` 선언 추가.
- **23장 배지 오정렬 발견 및 수정** (EN/KO 동일): 13절 후반("사울이 그일라 탈출 보고를 받고 공격 취소")이 배지 `14-15`로, 14–15절(십 광야) 내용이 배지 `16-18`로 잘못 표기되어 있었음.
  `[11]→'13', [12]→'14-15'` 로 정정, split `16-18` 선언 제거 → split `13` 선언 추가.
- "Geba (Gibeah)" — MSG의 병기 그대로 `Geba (Gibeah)` / `게바(기브아)` 로 EN/KO 통일 (13:2, 13:11, 14:1, 14:5, 14:9).

## 3. 본문 복원 — 주요 누락 (EN 기준, KO 1:1 미러)
- 9:1–2 족보 복원: **Becorath, Aphiah** ("and so on"으로 뭉뚱그려져 있었음) + Benjaminite.
- 17:55 아브넬의 대답 통째 누락 → "'Honestly, O King, I have no idea.'" 복원.
- 17:58 다윗의 대답 후반 누락 → "I'm the son of your servant Jesse—the one who lives in Bethlehem." 복원.
- 14:1 "at Geba" 지명 누락 복원. 14:42 "the one God points to", "Urim and Thummim" 제비 명칭 복원.
- 19:23–24 "in Ramah" 누락 복원.
- 21:2 "Ahimelech", 22:5/22:13 "son of Ahitub", 22:4 "prayed to God for him" 복원.
- 23:19–20 / 26:1–3 "Ziphites", 26:6 "Abishai son of Zeruiah", 26:13–14 "Abner son of Ner" 복원.
- 24:2 "three companies", 24:17 "You're the one in the right, not me" 복원.
- 25:43–44 "Palti (Paltiel) son of Laish" 복원.
- 26:16 "As God lives, (aren't you the one in charge?)" 복원.
- 27:8 "Shur", 27:10–11 "the Negev of Judah / of Jerahmeel / of the Kenites" 복원 (지명 의역이 빠져 있었음).
- 18:6–9 / 29:4–5 승전가 숫자: "thousands / ten thousands" → MSG 원문 그대로 **"by the thousand / by the ten thousand"** ("천 명씩 / 만 명씩").
- 30:24–25 "The one who stays behind … the one who goes out" 복원.
- 20:11 "When the two of them were out in the field", 20:42 "The two of us have vowed friendship" 복원.
- 1:12 "praying **before God**", 2:5 "second helpings", 5:4 "in one piece", 9:8 "the one we call a 'Prophet'", 9:23 "the one I told you to set aside", 16:5 "the worship **of God**" 복원.
- 26:8 "I won't need a second one" (MSG "I won't need a second!" 충실).

## 4. 문체 순화 (뜻 축소 없이)
- EN: "lowkey shook / Bro" → "seriously rattled / Look", "gassed him up in God" → "encouraged him in God", "no cap" → "for real", "Chill" → "Come on", "lowkey mutiny" → "practically in mutiny", "lowkey trust" 완화, 19장 "dark vibe" → "dark mood sent by God".
- KO: "완전 꿀!" → "좋았어!", "와 미쳤다" → "와, 믿기지가 않네", "대박!" → "최고야!".

## 5. 완전성 검사기(completeness_check.py) 점검 및 근본 수정
- 27장·29장·18장에서 "split 문단이 개별 검사되는 것처럼 보인다"는 의심이 있었으나, 코드를 직접 점검한 결과 union semantics는 **정상 동작**하고 있었음. 해당 실패들의 진짜 원인은 **28장 배지 오정렬**과 **복수형 수량어("thousands") 미인식**이었으며, 배지를 바로잡고 MSG 원문 표현으로 되돌리자 해소됨. 내용을 중복 기재하는 식의 편법은 쓰지 않음.
- 실제 버그 1건 수정: `_parse_num_seq`가 "a second one"을 2+1=3으로 오판독 → 서수 뒤의 "one"은 대명사로 보고 중단하도록 수정 ("a second one"→2, "the one"→1, "twenty one"→21 정상).

## 6. 완전성 검사 최종 결과
- 최초 58건 → 수정 후 **19건**, 19건 전부를 개별 대조하여 아래와 같이 **오탐(false positive)** 으로 분류:
  - 부사/관용구: "additionally"(2:18–20), "a thing or two"→"something"(14:12)
  - 하나님의 호칭: "God"→"LORD"/"LORD's"(4:5–6, 22:17, 22:20–21) — 정당한 신명 표기
  - 복수형/의역된 이름: "Benjaminite"→"tribe of Benjamin", "Ammonites"→"Ammonite king", "Amalekite(s)"→"Amalekites", "Shemeshite"→"from Beth Shemesh", "Gibeah"→"Geba (Gibeah)" 병기 후 해소 외 잔여
  - 유의어: "first light"→"crack of dawn", "First thing"→"very next morning", "the one"→"who", "both", "you guys", "Deliverer?"→"This guy is gonna save us? Yeah, right.", 인용어 "beauticians/conscript/orchards/regimented"→"perfumers/take/olive groves/draft" (8:10–18 경고 전체가 한 문단에 완전 포함되어 있음)
- 진짜 누락 39건은 전부 위 3항과 같이 복원됨.

## 7. 파일 무결성
- 세 파일 모두 strict UTF-8 디코딩 성공, U+FFFD(�) 바이트 0개, "<redacted>" 리터럴 0개.
- 검사 출력에 "<redacted>"/"���"가 보였던 것은 **출력 렌더링 단계의 표시 문제**이며, 바이트 단위(codepoint) 직접 확인 결과 파일 내용은 정상 ("His armor bearer was like…", U+201C 인용부호 포함).

## 8. 게이트 결과 (2026-09-24)
1. `validate_translation.py fixes/en_1Samuel.json fixes/ko_1Samuel.json` → **PASS: 31개 장 모두 통과**
2. `completeness_check.py fixes/en_1Samuel.json` → 31장·530문단·661개 이름·145개 숫자 검사, **39건 복원 후 잔여 19건은 전수 검증된 오탐**
3. `build_gdocs.py 1Samuel` → teen_ch=31, rows=530, msg_units=438, teen_without_msg=0, msg_orphans=0, **VERIFY_DROPPED=0**
4. `verify_pairing_content.py gdocs_build/1Samuel.docx 1Samuel` → **checked 530 data rows in 31 tables, PAIRING CONTENT OK**

## 9. 수정 통계 (작업 전 원본 대비 diff)
- EN: 본문 67문단 수정, 배지 46건 정정, 29개 장에 splits 선언 추가
- KO: 본문 32문단 수정, 배지 79건 정정, 29개 장에 splits 선언 추가 (EN과 1:1 일치)

## 10. 미검증 경계 (정직한 한계)
- Google Docs 업로드 후 31개 장 테이블의 실제 렌더링은 성욱의 확인이 필요 (이 환경의 브라우저는 업로드 확인 불가).
- 19건 오탐 분류는 개별 대조에 근거하나, "beauticians→perfumers" 같은 의역 선택은 성욱의 최종 판단에 맡김.
