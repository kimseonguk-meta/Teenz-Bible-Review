# OT 작업 중단 체크포인트 (2026-09-22 11:32 SGT — 성욱 우선순위 변경으로 신약 우선, 구약 중단)

## 완료 (게이트 PASS, 검증됨)
- Genesis (50장), Job (42장)
- 소선지서 12권 전부 (Hosea~Malachi, 67장)
- Joshua, Ruth (역사서1 작업자가 완료, 게이트 PASS는 재확인 필요)

## 부분 산출물 (fixes/에 en_*.json 존재 — 구약 재개 시 검증 후 이어서 사용)
- en_Psalms.json, en_Proverbs.json, en_Ecclesiastes.json, en_SongOfSongs.json (부분)
- en_Ezra.json, en_Esther.json (부분)
- en_Isaiah.json (부분)

## Nehemiah MSG 문단 구조 (역사서2 작업자가 수집, ch1-10 확정)
| 장 | MSG 문단 범위 | 비고 |
|---|---|---|
| 1 | 1-2 / 3 / 4 / 5-6 / 7-9 / 10-11 | |
| 2 | 1-2 / 2-3 / 4-5 / 6 / 7-8 / 8-9 / 10 / 11-12 / 13-16 / 17-18 / 19 / 20 | v2·v8 경계 공유; "Come—Let's Build the Wall of Jerusalem" 헤더는 11-12 본문과 같은 배지 |
| 3 | 1-2 / 3-5 / 6-8 / 9-10 / 11-12 / 13 / 14 / 15 / 16 / 17-18 / 19-23 / 24-27 / 28-30 / 31-32 | MSG 14문단 = 앱 14문단 |
| 4 | 1-2 / 3 / 4-5 / 6 / 7-9 / 10 / 11-12 / 13-14 / 15-18 / 19-20 / 21 / 22 / 23 | MSG 13문단 vs 앱 14문단 — split 분석 필요 |
| 5 | 1-2 / 3 / 4-5 / 6-7 / 7-8 / 9 / 10-11 / 12-13 / 14-16 / 17-18 / 19 | v7 경계 공유 |
| 6 | 1-2 / 2-3 / 4 / 5-6 / 6-7 / 8 / 9 / 10 / 11 / 12-13 / 14 / 15-16 / 17-19 | v2·v6 경계 공유 |
| 7 | 1-2 / 3 / 4 / 5 / 6-60 / 61-63 / 64-65 / 66-69 / 70-72 / 73 | MSG 7:61-63은 Tel Melah 명단 + 제사장 가문을 한 문단으로 묶음 |
| 8 | 1 / 2-3 / 4 / 5-6 / 7-8 / 9 / 10 / 11 / 12 / 13-15 / 16-17 / 18 | MSG 12문단 = 앱 12문단 |
| 9 | 1-3 / 4-5 / 5-6 / 7-8 / 9-15 / 16-19 / 20-23 / 24-25 / 26-31 / 32-37 / 38 | v5 경계 공유 |
| 10 | 1-8 / 9-13 / 14-27 / 28-30 / 31 / 32-33 / 34 / 35-36 / 37-39 | 혼인 서원은 28-30 내 "Thus:" 포함, 31절(안식일·7년 휴경)은 별도 문단 |
- Nehemiah 11·12·13 MSG 구조 미수집 → 재개 시 `https://bible-history.com/msg/nehemiah-11` (-12, -13) 을 browser.open으로 수집
- Ezra: 이전에 지정된 5가지 누락 수정 + 최종 재점검 미착수 → 재개 시 처리
- MSG 소스: bible-history.com/msg/<book>-<chapter> 패턴도 사용 가능 (Nehemiah 7-10 수집에 사용됨)

## 미착수 (구약 재개 시 처리)
- Judges, 1 Samuel, 2 Samuel, 1 Kings, 2 Kings (역사서1 잔여)
- Exodus, Leviticus, Numbers, Deuteronomy (오경 잔여)
- Psalms, Proverbs, Ecclesiastes, Song of Songs (시가서 잔여 — 부분 파일 있음)
- 1 Chronicles, 2 Chronicles, Ezra, Nehemiah, Esther (역사서2 잔여 — Ezra/Esther 부분 파일 있음)
- Isaiah, Jeremiah, Lamentations, Ezekiel, Daniel (대선지서 — Isaiah 부분 파일 있음)

## 주의
- 부분 파일(en_*.json)은 감사 미완료 상태일 수 있음. 구약 재개 시 각 파일을 validator로 돌리고, carried_over/audit 상태를 확인한 뒤 이어서 작업할 것.
- msg_ranges는 MSG 원문에서 독립 추출 (verseRanges 복사 금지 — tautology 문제).
