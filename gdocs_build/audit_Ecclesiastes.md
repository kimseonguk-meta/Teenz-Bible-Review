# Ecclesiastes 12장 감사 보고서

**기준**: Eugene Peterson, The Message (MSG) — `msg_Ecclesiastes.txt` (BibleGateway, 2026-09-22 수집)
**범위**: Ecclesiastes 12장, Teen EN / Teen KO 전수 대조
**일자**: Sep 24, 2026

## 결론

127개 틴즈 문단(EN/KO 동일 구조)을 MSG 원문과 문장 단위로 전부 대조했다. 기존 패치(슬랭/배지 정리된 상태)에서 **실질 이슈 15건**을 발견·수정했다. 그중 가장 심각했던 것은 KO 4장의 **배지-내용 불일치**(내용이 한 단락씩 밀려 잘못된 배지 아래 들어감 + 비MSG 삽입 3건)와 3장의 **비MSG 구절 삽입 3건**("scatter stones", "put eternity in the human heart", "call the past to account" — 모두 다른 번역본에서 유입). merge 후보는 없다(성욱 컨펌 필요한 병합 없음). 의도적 split 5건(1, 2, 6, 9, 12장)은 splits 메타데이터로 선언만 했다.

## 발견 이슈 및 수정 (게이트 1→2)

| 장:절 | MSG 요지 | 유형 | 수정 |
|---|---|---|---|
| 3:2-8 | "A right time to make love and another to abstain" (14쌍 중 7번째) | 비MSG 삽입 + MSG 쌍 누락 | "scatter stones/gather them" 삭제 → EN "A time to be close and a time to hold back" / KO "사랑을 나눌 때가 있고 자제할 때가 있고" |
| 3:9-13 | "he's left us in the dark, so we can never know what God is up to" | 비MSG 삽입 | "put eternity in the human heart" 삭제 → EN/KO 모두 MSG 기준 재작성 |
| 3:15 | "Whatever was, is. Whatever will be, is. That's how it always is with God." | 비MSG 삽입 | "God will call the past to account" 삭제 → EN/KO "That's how it always is with God" |
| 4:7-8 | MSG 단일 단위 7-8 | 인위적 분할 + 중복 인트로 + 내용 없는 파편 단락 | EN/KO 모두 단일 7-8 단락으로 복원, splits 선언 제거 |
| 4:9-16 (KO) | 배지 아래 내용이 한 칸씩 밀림: [8] 끝에 9-10 내용, [9-10]에 11절, [11]에 12절, [12]·[13-16]에 13-16 | 배지-내용 불일치 | KO 4장 [8]-[13-16] 전면 재배정 (EN 구조와 1:1) |
| 4:13-16 (KO) | MSG: rags-to-riches 청년, 열기 식음 | 비MSG 삽입 | "감옥에서 나와 왕좌에" / "흙수저" / "나중에 오는 세대가 기뻐하지 않을 것" 삭제 → MSG 기준 재작성 |
| 5:2 (EN) | "Don't be too quick to tell God what you think he wants to hear" | 의미 반전 | "tell God all your grand plans" → "don't be too quick to tell God stuff just because you think it's what he wants to hear" (KO는 원래 정확했음) |
| 7:5 (EN/KO) | "the rebuke of a sage vs the song and dance of fools" | 의미 변경 | "praised by a bunch of fools" → "a wise person's straight call-out vs the noise and hype of fools" |
| 7:9 (EN/KO) | "You can spot a fool by the lumps on his head" | 의미 변경 | "drama they're always in" → "the lumps on his head—his own anger put them there" |
| 7:19 (EN) | "ten strong men give to a city" | 의미 변경 | "ten powerful leaders" → "ten strong men give their city" (KO는 원래 정확) |
| 8:2-7 (EN) | "You're serving his pleasure, not yours" | 의미 반전 | "You're on their team, not the other way around" → "You're there to serve his pleasure, not yours" (+sacred oath, promptly and accurately 복원; KO는 원래 정확) |
| 9:1-3 (EN) | R1 금지 슬랭 + 6쌍 중 righteous/wicked 누락 + "obsessed with evil" 약화 | 슬랭/누락/약화 | "here's the tea" 삭제, 6쌍 전부 복원, "obsessed with evil" 복원 (KO는 원래 6쌍·evil 유지) |
| 9:11 (EN) | "The race is not always to the swift..." | — | 확인됨, 변경 없음 |
| 12:1-2 (EN) | "Honor and enjoy your Creator" | 누락 | "remember"만 있던 것을 "honor, enjoy, and remember"로 복원 (KO는 "기억하고 즐겨야"로 원래 정확) |
| 12:8-10 (EN) | MSG "the Quester" | 호칭 불일치 | "The Teacher" 3곳 → "the Quester" (1장의 "Quester"와 통일) |
| 8:16-17 (KO) | "내가 지혜��� 마스터하고" | 깨진 문자 | "내가 지혜를 파고들기로 마음먹고"로 수정 |
| 12:6-7 (KO) | "Life, lovely while it lasts, is soon over" (서술) | 의미 반전 | "인생은 즐거울 때 즐겨야 돼"(처방) → "인생은 아름답긴 한데, 금방 끝나버려" |
| 슬랭 | R1 "here's the tea" (EN 9장), R4 "대박" 2회 (KO 2장) | 금지 슬랭 | 전부 교체. 전수 스캔 결과 나머지 6-Rule 위반 없음 |

completeness_check에서 추가로 걸린 MSG 어휘 11건(quester ×2, inane, "a day or two", overwork/overtalk, "in the first place", "the one", immaturity, felling, "safety first", hikes, adorning)은 모두 실제 MSG 단어/이미지이므로 틴즈 문체 유지 범위에서 복원했다.

## 구조 (MSG 단위 → 틴즈 문단)

- 1장: MSG 6단위 → 7문단 (2-11을 [2-3]/[4-11]로 split, 선언됨)
- 2장: MSG 10단위 → 11문단 (1-3을 [1]/[2-3]으로 split, 선언됨)
- 3장: 7단위 → 7문단 1:1
- 4장: MSG 9단위 → 9문단 1:1 (인위적 분할 해제 후)
- 5장: 12단위 → 12문단 1:1
- 6장: MSG 7단위 → 8문단 (1-2를 [1]/[2]로 split, 선언됨)
- 7장: 20단위 → 20문단 1:1
- 8장: 10단위 → 10문단 1:1
- 9장: MSG 9단위 → 10문단 (1-3을 [1-2]/[3]으로 split, 선언됨)
- 10장: 16단위 → 16문단 1:1
- 11장: 8단위 → 8문단 1:1
- 12장: MSG 8단위 → 9문단 (12-13을 [12]/[13]으로 split, 선언됨)

merge 없음. § 헤더 없음.

## 게이트 상태

- [x] 게이트 1: MSG 전수 대조 → 위 이슈 리포트
- [x] 게이트 2: 수정 반영 (merge/split 적용 없음)
- [x] 게이트 3: `validate_translation.py` PASS (12장)
- [x] 게이트 4: `completeness_check.py` PASS (127문단)
- [x] 게이트 5: `build_gdocs.py` 재빌드, VERIFY_DROPPED=0 (127 rows, 122 MSG units)
- [x] 게이트 6: `verify_pairing_content.py` PAIRING CONTENT OK (12 tables, 127 rows 실제 렌더링 기준)
- [x] 게이트 7: Google Docs 신규 업로드 OK — "전도서 (Ecclesiastes): MSG + Teen EN + KO", 테이블 12/12, export-back VERIFIED OK (doc id: `1CzWMUfRDjlY-7qG_uE2f029lOU4K1woKa3taHpujlS0`)

## 검증 범위 vs 미확인 경계

- 확인한 것: MSG txt 12장 전체 문장 대조, EN/KO 127문단 배지·내용·슬랭·호칭 일치, validator·completeness·빌드·짝지음·업로드 후 테이블 수(12)·export-back.
- 확인하지 못한 것: Google Docs에 실제 렌더링된 화면을 눈으로 보지 못함(export-back 텍스트 검증만 수행). msg_Ecclesiastes.txt 자체가 BibleGateway MSG 정본과 1:1인지는 이 작업 범위 밖(2026-09-22 수집본을 그대로 신뢰).

## 2차 심층 재검토 (2026-09-25)
- 범위: MSG 122 유닛 ↔ EN 127 문단 ↔ KO 127 문단 전수 문장 단위 대조 (1~12장). completeness 체커 PASS.
- EN 복원 2건 (전부 비대칭 누락 — KO는 이미 MSG 내용 보유):
  - 5:11 EN이 5:10 반복 복제본이었던 치명 오류 수정 — MSG "The more loot you get, the more looters show up. And what fun is that—to be robbed in broad daylight?" 복원: "The more stuff you have, the more people show up to take it from you. And what's the fun in that—getting robbed in broad daylight?" (KO "네가 가진 게 많아질수록, 그걸 노리는 사람들도 많아져. 대낮에 다 털리는 게 재밌냐?" 보유)
  - 7:21-22 EN이 7:19 복제본으로 오배치됐던 오류 수정 — MSG "Don't eavesdrop on the conversation of others. What if the gossip's about you and you'd rather not hear it? You've done that a few times, haven't you—said things behind someone's back you wouldn't say to his face?" 복원 (KO "남들 대화 엿듣지 마..." 보유)
- EN 전수 중복 스캔: 위 2건 외 중복/오배치 없음.
- 게이트: validate PASS 12/12, build 12 tables / VERIFY_DROPPED=0 / msg_orphans=0 / teen_without_msg=0, verify_pairing PAIRING CONTENT OK, completeness PASS.
- GDocs: doc ID 1CzWMUfRDjlY-7qG_uE2f029lOU4K1woKa3taHpujlS0, API 12/12 tables, export-back VERIFIED OK.
