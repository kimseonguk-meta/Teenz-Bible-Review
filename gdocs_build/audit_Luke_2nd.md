# 누가복음 2차 심층 재검토 감사 리포트 (2026-09-25)

기준: 2026-09-25. 대조 기준은 오직 Eugene Peterson의 The Message(MSG).
원칙: "축약하지 마라" — MSG의 모든 문장·인명·부칭·숫자·인용구를 Teen EN에 살린다.
EN이 primary, KO는 EN과 내용·톤·구조 일치.

## 범위
- 누가복음 1–24장 MSG–EN–KO 전장 직접 판독 완료.
- 1차 감사 리포트(audit_Luke.md)의 이슈 32건은 현행 JSON에 이미 반영되어 있음.
- 1차 completeness_fp_Luke.md는 "축약 허용" 전제로 19건을 오탐 판정 → **2차 기준에서 5건을 실제 누락으로 번복 복원**.

## EN 복원 6건
1. 1:8-12 — `the main Temple sanctuary` → `the main sanctuary of God` (MSG "sanctuary of God"; KO "하나님의 성소"에는 있음)
2. 1:15-17 — `even before he's born` → `from the moment he's born` (MSG "from the moment he leaves his mother's womb"; 사실관계 오류 — 탄생 시점이 아니라 탄생 전이던 것을 수정)
3. 1:29-33 — `God will give him the throne` → `the Lord God will give him the throne` (MSG "The Lord God"; KO "주 하나님께서"에는 있음)
4. 2:1-5 — `hiked from Nazareth all the way to Bethlehem, David's town` → `hiked up from the Galilean town of Nazareth all the way to Bethlehem in Judah, David's town` (MSG "the Galilean town of Nazareth up to Bethlehem in Judah"; KO "갈릴리 나사렛 ... 유대 베들레헴 ... 올라갔어요"에는 있음)
5. 2:15-18 — `"Let's go to Bethlehem right now and see this!"` → `"Let's go to Bethlehem right now and see what God has revealed to us!"` (MSG "see for ourselves what God has revealed to us"; KO "하나님이 우리한테 보여주신 거"에는 있음)
6. 24:4-8 — `They remembered his words.` → `They remembered Jesus' words.` (MSG "they remembered Jesus' words"; KO "예수님이 하셨던 말씀"에는 있음)

## KO 수정 15건
1. 1:15-17 — `태어나기도 전부터 성령으로 충만할 거예요` → `태어나는 순간부터 성령으로 충만할 거예요` (EN과 함께 사실관계 수정)
2. 1:80 — `공식적으로 나타날 때까지` → `하나님의 예언자로 ... 공식적으로 나타날 때까지` (MSG "prophetic debut"; EN "as God's prophet" — `예언자` 의미 복원)
3. 6:43-45 — `사과를 보면 그 나무가 건강한지 알 수 있죠.` 뒤에 삽입: `여러분 자신의 생명을 살리는 삶부터 시작하세요.` (MSG/EN "You must begin with your own life-giving lives." 누락 복원)
4. 7:11-15 — `전설급…` 삭제 (MSG/EN에 없는 첨가)
5. 7:16-17 — `믿기 힘든!` 삭제 (MSG/EN에 없는 첨가)
6. 7:21-23 — `하나님의 엄청난 사랑이랑 구원이 막 쏟아지고` → `하나님의 구원의 환대가 베풀어지고` (EN "God's salvation hospitality extended to them"에 맞춤)
7. 8:25 — `너무 무서워서 어쩔 줄 몰라 하면서` → `엄청난 경외감에 휩싸여서 말을 더듬으면서` (EN/MSG "absolute awe ... staggered and stammering"; 공포로 이동된 의미 수정)
8. 9:23-27 — `고난을 피하려고 애쓰지 마세요.` 뒤에 복원: `오히려 고난을 받아들이세요. 저를 따라오세요. 제가 어떻게 하는지 보여드릴게요.` (MSG/EN "Don't run from suffering; embrace it. Follow me and I'll show you how." 누락 복원)
9. 9:42-43 — `고개를 끄덕이며` → `놀라서 고개를 흔들며` (EN/MSG "shook their heads in wonder"; 동작 의미 수정)
10. 3:7 — `빽 쓰면` → `우기면` (과도한 슬랭 정리)
11. 3:16 — `셔틀` → `조연` (과도한 슬랭 정리)
12. 3:16 — `진짜배기는` → `진짜인 것들은` (과도한 슬랭 정리)
13. 4:1 — `성령으로 풀충전해서` → `성령으로 가득 차서` (과도한 슬랭 정리)
14. 4:18 — `꿀소식을 전하게` → `기쁜 소식을 전하게` (과도한 슬랭 정리)
15. 6:20 — `꿀팁이 있습니다` → `팁이 있습니다` (과도한 슬랭 정리)
유지 판정: 9:58-59 "Follow me" 위치 이동은 내용 온전·EN/KO 일치의 순수 구조 차이. ch9 "5성급 호텔"은 "best inns"의 teen 표현으로 유지.

## checker 재판정 (completeness_fp_Luke.md 갱신)
- 1차 FAIL 19건 중 2차에서 실제 누락 5건 복원 (ch1 idx3 god, ch1 idx12 lord, ch2 idx1 galilean, ch2 idx7 god + 판독 발견 ch24 idx2 jesus).
- 잔여 FAIL 15건 전부 오탐: Zachariah/Zechariah 철자 변형 11건, "this message" 1건, "He unrolled it" 1건, "One guy" 1건, "the Bible" 1건.

## 게이트
- `validate_translation.py`: 24장 PASS
- `build_gdocs.py Luke`: VERIFY_DROPPED=0, msg_orphans=0, teen_without_msg=0, PAIRING_MISMATCHES=0, ALL VERIFY OK
- docx 실물 확인: 수정 20개 문자열 전부 Luke.docx 표 셀에서 PASS
- Google Doc 재업로드: ID 1w6syxHOSkDDIYhv9MRHKqqW79WjZayhrXA4MFHIPa_k, API tables 24/24, export-back deep-verify 통과

## 커밋
- (기록 예정)
