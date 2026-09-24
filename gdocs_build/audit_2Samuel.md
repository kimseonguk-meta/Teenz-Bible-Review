# 사무엘하 (2Samuel) 감사 기록

감사 기준: Eugene Peterson The Message (MSG) 원문
감사 일자: Sep 24, 2026

## 구조

- 24장, EN 460문단 / KO 460문단
- MSG 347개 원문 단위, Teen 460개 행
- splits 선언: 67개 (순수 가독성 목적 구조 차이)
- VERIFY_DROPPED=0, orphans=0

## 주요 수정

### MSG 원문 복원
- ch1: 22, 23, 24-25, 26, 27 단위 복원
- ch14: MSG 특이 순서(15-17 후 8절) 확인 및 8절 복원
- ch22: 4~47-51 10개 단위 복원
- ch23: 2-7~24-39 9개 단위 복원 (39절까지)

### EN/KO 배지 정렬
- ch2, ch5, ch21: KO 문단 수 EN에 맞춤
- ch1, ch3, ch8-ch19, ch24: KO 배지를 EN/MSG에 맞춤
- ch15: P0[1-3]→[1-2], P1[4]→[1-2] (MSG v1-2 내용)
- ch16: P0[1-2]→[1] (v1 내용만)
- ch23: Thirty 명단 KO 배지 1절씩 밀림 현상 수정
- ch24: EN P3[4-9]→[10], P4[10]→[11-12], P5[11-13]→[13]

### 호칭/족보 복원
- ch2: Abner son of Ner, Joab son of Zeruiah
- ch3, ch21: Rizpah daughter of Aiah
- ch9: Makir son of Ammiel
- ch20: Sheba son of Bicri

### 슬랭 순화
- EN: Spill the tea, goated, lowkey, no cap, shanked, trash-talked, dipped, OMG 등
- KO: 박살, 털렸, 머리끄덩이, 미친 듯이, 비열한 놈들, 폭력배들 등

### msg_ranges 재구축
- 전 장의 msg_ranges를 실제 MSG 원문 단위로 재구축 (Teen verseRanges 복사 아님)
- splits를 원문 단위 기준으로 선언

## 게이트

- validate_translation.py: PASS (24장)
- build_gdocs.py: 24 tables, 460 rows, VERIFY_DROPPED=0
- verify_pairing_content.py: PAIRING CONTENT OK

## 2차 재검토 (Sep 24, 2026)
- completeness_check 69건 후보 전수 분류 → 실제 누락 59건 복원 (EN 46+13, KO 14+3)
- 주요 복원: ch2 추격전 후반부(암마 언덕·기아·기브온 변두리), ch11:25 다윗의 분노+아비멜렉/데벳/우리야 보고, ch13:34 호로나임길 보초, ch21:7-9 아드리엘 족보, ch24 인구조사 경로 전체+9개월 20일, ch13:15 암논 강간 명시 복원, ch1 THe 오타 수정
- 호칭 복원: son of Ner(6건), son of Zeruiah(4건), the Gittite, the Gilonite, the Arkite, son of Bicri(2건), son of Laish, son of Ammiel, son of Rehob+king of Zobah, Talmai son of Ammihud, daughter of Aiah, Ammonite Rabbah, Benjaminite, the Jebusite, Dan to Beersheba(3건), the Benjaminite Shimei son of Gera, Barzillai the Gileadite from Rogelim, Jonathan son of Shimeah
- 잔여 16건은 의미 동등 오탐으로 확정 (faster/swifter, Bicrites, Hagrite army 후단락 등)
- KO ch11:16 여룹베셋의 아들 아비멜렉 EN/KO 패리티 수정
- 게이트: validate_translation PASS (24장), completeness 16 오탐만 잔류, build 24 tables/460 rows/347 MSG/VERIFY_DROPPED=0
- pairing 셀 직접 확인 (ch2:17-19, ch11:25, ch24:4-9 등)
- Google Docs 기존 문서 업데이트: API 24/24, export-back VERIFIED OK
