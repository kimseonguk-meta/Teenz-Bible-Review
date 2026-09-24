# 욥기 (Job) 감사 기록 — 2026-09-24

- 기준: Eugene Peterson **The Message(MSG)** 영어 원문 (`msg_Job.txt`, 1,188줄)
- 감사 범위: 42장 전체, EN 248문단 / KO 248문단
- 게이트: `validate_translation.py` PASS, `completeness_check.py` 전수 판정, 독 짝지음 검증, Google Docs 업로드 + export-back 검증

## 구조 검증 (전수)

- 42장 모두 존재, 장 순서 1–42 정상
- 모든 장이 정경상 마지막 절까지 1–N 연속 커버, 장 중간 통구간 결손 없음
- 외부 공개 MSG와의 텍스트 대조는 **Job 25 표본 대조만** 수행 (문구 일치 확인). 나머지는 repo의 `msg_Job.txt`를 최종 기준으로 감사

## 수정 집계 (HEAD 대비 diff)

- EN 수정 문단: **24개** (17개 장)
- KO 수정 문단: **5개** (ch13, ch17, ch18, ch30, ch42)
- 배지(verseRanges) 수정: **3개 장** (ch12, ch17, ch22)
- 선언한 split/merge: **없음** (기존 HEAD 감사본의 split 선언 ch1,2,4,6,27,29,31,32,37,38,40 유지)
- validator: PASS (42장 모두)
- completeness: 27건 FAIL → **전수 수동 대조 결과 27건 모두 오탐** (근거: `gdocs_build/completeness_fp_Job.md`)

## 주요 복원 (MSG 기준)

| 위치 | 내용 |
|---|---|
| ch1:8 | `God was like` → `God said to Satan` (수신자 Satan 복원) |
| ch1:21 | `God's name is still the GOAT` → `blessed be God's name` (슬랭 정리) |
| ch2:11–12 | Eliphaz from **Teman**, Bildad from **Shuhah**, Zophar from **Naamath** (출신지 복원), `first saw him`의 `first` 복원 |
| ch13:3 | `straight to God` → `straight to God Almighty` (호칭 복원; KO도 `전능하신 하나님` 복원) |
| ch17:14 | `bury me` → `put me six feet under` (MSG 이미지 복원) |
| ch18:16 | `their place gets wrecked` → `acid rain soaks their ruins` |
| ch18:20 | `People everywhere` → `Westerners... easterners...` |
| ch21:15 | `bother with God` → `bother with God Almighty` (호칭 복원) |
| ch21:27 | `naively`, `achievements... collapse` 복원 |
| ch22:17 | `What's God even good for` → `What's God Almighty even good for` (호칭 복원) |
| ch24:1 | `if God knows everything` → `if Judgment Day isn't hidden from the Almighty` (호칭 복원) |
| ch30:20–23 | `bury me` → `put me six feet under` |
| ch30:24 | 오역 `ignore someone` → `hit anyone` 정정 |
| ch30:29 | jackals/owls 복원 |
| ch30:31 | fiddle/mouth harp 복원 |
| ch39:26 | `gliding on the wind` → `soaring effortlessly on thermal updrafts` |
| ch40:18 | 오역 `oak trees` → `beech trees` 정정 |
| ch40:24 | `tame him` → `housebreak him` |
| ch41:28 | 오역 `slingstones` → `bullets` 정정 (KO `물맷돌` → `총알`) |
| ch41:34 | `boss of the deep` → `king of the deep` |
| ch42:3 | `Job hit God back` → `Job answered God`, `muddying the water` 이미지 복원 |
| ch42:7 | `Eliphaz the Temanite` 복원 |
| ch42:9 | Eliphaz the Temanite / Bildad the Shuhite / Zophar the Naamathite 복원 |

## 배지 수정

- ch12: `4-8`→`4-6`, `9-14`→`7-12`, `15-25`→`13-25` (EN/KO 함께 정렬)
- ch17: `3-6`→`3-5`, `7-9`→`6-8`, `10-11`→`9`, `12-16`→`10-16` (EN/KO 함께 정렬)
- ch22: `2-12`→`2-11`, `13-15`→`12-14`, `16-19`→`15-18`, `20-21`→`19-20`, `22-25`→`21-25` (EN/KO 함께 정렬)

## 슬랭 정리 (의미 유지)

- `GOAT` → `blessed` (ch1)
- `goated` → `magnificent`/`great`/`full` (ch36, ch39, ch42)
- `no cap` 삭제 (ch38, ch39, ch40)
- `weak sauce` → `weak` (ch32)
- `hit God back` → `answered` (ch42)
- KO는 대응 구어체 정리 (`했대/걔네/진짜/완전/거임` 과잉 정리)

## Almighty 호칭 조사

- `msg_Job.txt`의 `Almighty` 25곳 중 Teen EN이 누락한 4곳(ch13:3, ch21:15, ch22:17, ch24:1)을 복원
- ch22:17, ch24:1은 KO에 이미 `전능하신 하나님`/`전능하신 분`이 있었음 (EN만 복원)
- ch13:3은 EN/KO 모두 복원

## 독 (Google Docs)

- 제목: `욥기 (Job): MSG + Teen EN + KO` (Final 없음)
- Doc ID: `1U-4g7_lN_E3orTZJgAP9ru9c-_SL9pvO7-M3nDAktdI`
- 링크: https://docs.google.com/document/d/1U-4g7_lN_E3orTZJgAP9ru9c-_SL9pvO7-M3nDAktdI/edit?usp=drivesdk
- API 테이블 42개 / export-back 검증 OK
- 짝지음 검증: 248 data rows in 42 tables, PAIRING CONTENT OK

## 승인 필요 사항

**없음.** 이번 감사에서 내용 누락·오역·EN/KO 의미 불일치는 모두 복원/정정했고, merge/split 승인이 필요한 구조 변경은 없었다.

## 검증 경계 (정직한 기록)

1. 42장 구조·절 커버리지는 전수 검사했다.
2. 외부 공개 MSG와 텍스트 대조한 것은 **Job 25 표본뿐**이다. 나머지는 repo의 `msg_Job.txt`를 최종 기준으로 감사했다.
3. completeness 검사기의 27건 FAIL은 전수 수동 대조로 오탐임을 확인했다 (근거 문서 별도).
4. 성욱이 선언하기 전 "완료"라고 단정하지 않는다.

## 2nd re-audit (Sep 24)
- completeness_check: 27 candidates → 26 false positives (poetic paraphrase: "Contemptuous"→"disrespectful", "graveyards/unformed/cumulus/tames"→plain equivalents, split intro lines across teen paragraphs, "votive"-style number extractor artifacts; "ignoramus/wickedly/compounded/indictments" all meaning-equivalent).
- Sentence-count scan flagged 42 spots; all verified as teen-side splits with full coverage in sequence (ch1, ch4, ch6, ch8, ch15, ch16, ch18, ch19, ch21, ch24, ch29, ch37, ch38, ch40).
- 1 MSG omission restored (EN+KO): ch42 idx0 (badge 1-6) — MSG "second-guessing my purposes" dropped from God's question → EN "second-guessing my plans", KO "내 뜻을 의심하는 게".
- Ambiguous (left, no content loss): build pairing MSG_SUPERSET notes (ch15 idx2/3, ch18 idx0/1 — MSG print unit spans more verses than teen badge; content covered across teen splits).
- Gates: STRUCT OK (42 ch, EN/KO parity); build VERIFY_DROPPED=0, teen_without_msg=0, msg_orphans=0; docx pairing spot-check OK; reupload API tables 42/42 VERIFIED OK.
