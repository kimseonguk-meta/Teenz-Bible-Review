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
