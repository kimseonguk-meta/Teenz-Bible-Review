# 아가 (Song of Songs) 의미 감사 리포트 — 2026-09-23

감사 기준: Eugene Peterson MSG 영어 원문(2026-09-22 수집본). 8장 전수 대조.

## 결론
- EN·KO 모두 MSG 대비 실제 누락·변형이 다수 확인되어 전수 수정함.
- 가장 심각했던 것은 6장 KO의 '춤춰라' 문단 6회 반복 데이터 오류와, 8장 후반(6-12절)에 다른 번역(KJV식) 내용이 MSG 대신 들어가 있던 점.

## 이슈 목록 (장:절 / MSG 요지 / 문제 유형 / 수정 내용)

### 1장
- 1:2-3 / aromatic oils — 향유 언급 누락 → "headier than your aromatic oils" 반영 ("on another level" 표현도 슬랭 정리)
- 1:4 / "we'll make great music" — "making amazing memories/신나게 놀자"로 변형 → EN "making the best music", KO "신나는 음악을 만들자"
- 1:5-6 / "soft like Solomon's Temple hangings" + "darkened by the sun" — 축약 → 복원
- 1:1 / "banger of a song" — 슬랭 → "greatest hit"

### 2장
- 2:5-6 / apricots, raisins, faint with love, 왼손·오른팔 — 통째 누락 → 복원
- 2:7 / 사랑을 억지로 깨우지 말라는 경고 — 통째 누락 → 복원
- 2:8-10 / "My lover is here, and he's talking to me" — 누락 → 복원
- 2:16 / "until dawn breathes its light and night slips away" — 누락 → 복원
- 배지 오류: [3-7]→[3-4]/[5-6]/[7], [8-9]→[8-10], [10-14]→[11-14], [15]→[15]/[16]/[17] 분리 (EN·KO 동일)
- 슬랭: lowkey/OMG/no cap/popping off/대박/난리 났어 정리

### 3장
- 3:6-10 / carriage 묘사 (cedar/silver/gold/purple cushions/tooled leather) — 통째 누락 → 복원
- 3:6-10 / "armed to the teeth, trained for battle" — 누락 → 복원
- 3:11 / "garlanded" — 누락 → "화관까지 썼어"
- 배지: [1-5]/[6-8]/[9-11] → [1-4]/[5]/[6-10]/[11] (EN·KO 동일)
- "King Solomon" 명칭 누락 → 복원 (completeness checker 지적)

### 4장
- EN title "Lowkey Obsessed" — 슬랭 → "Completely Captivated"

### 5장
- 5:2 / "my dove, my dearest love... soaked with the night dew, freezing and shivering" — MSG 호칭·묘사 변형 → 복원
- 5:10-16 / raven curls, "eyes like doves...like wells of water", sage, "hard and smooth as ivory", "like a cedar, strong and deep-rooted", "delights me and thrills me through and through" — 축약·변형 → 복원
- 슬랭: Yo/lowkey/sickest/bounced/"Jerusalem crew"/obsessed 정리; title 클릭베이트 완화

### 6장
- 6:8 / MSG "There's no one like her on earth...She's a woman beyond compare"가 KJV식 "sixty queens/eighty concubines"로 대체되어 있었음 → MSG 기준 전면 재작성 (EN·KO)
- 6장 KO / '춤춰라' 문단 6회 반복 + 배지 대량 어긋남 — 심각한 데이터 오류 → 중복 제거, 배지 전면 정정 ([2]→[2-3], [3]→[4], [4]→[8], [8]→[11-12], [9]→[13])
- EN 배지: [2]→[2-3], [3](헤더)→[4], [11]/[12]→[11-12]; [2]+[3] 분리된 것을 MSG [2-3]으로 재결합
- EN title "She's a Total Knockout" → "There's No One Like Her"

### 7장
- 7:13 / "Love-apples drench us with their fragrance" — "vibe of new life"로 축약 → 복원
- EN title "Whipped" → "Head Over Heels"
- 슬랭: Dang/straight-up/vibe/babe/crash/여왕님 포스/여성미 대폭발 정리

### 8장
- 8:5 / "I found you under the apricot tree and woke you up to love" — 일부 누락 → 복원 (EN·KO)
- 8:6-7 / MSG "The fire of love stops at nothing...Love can't be bought and it can't be sold"가 KJV식 seal/"flame from God"/thousand coins로 대체 → MSG 기준 전면 재작성 (EN·KO)
- 8:9 / MSG "young and vulnerable...barbed wire/barricade"가 KJV식 silver tower/cedar planks로 대체 → 재작성 (EN·KO)
- 8:10 / MSG "I am a wall, and I've grown up — my breasts are full" — "breasts are like towers"로 축약 → "my breasts are full/이제 다 컸어"
- 8:11-12 / MSG에 없는 Baal Hamon/1,000/200 숫자가 다른 번역에서 유입 → MSG 기준 재작성 ("King Solomon may have huge vineyards...")
- 8:13 / "lady of the gardens" → "정원의 아가씨야" 복원
- EN title "No Cap" 제거 → "Love is Unstoppable"; 슬랭 yo/PSA/legit 정리

## merge-split 후보
- 6장 [2]+[3] 분리 → MSG [2-3]으로 재결합 적용 (MSG 문단 구조와 일치하므로 pending 아님)

## 게이트 결과
1. 의미 전수 감사: 8장 MSG 문장 단위 대조 완료
2. 수정 반영: 위 이슈 전부 반영
3. validate_translation.py: PASS (8개 장 모두 통과)
4. completeness_check.py: 잔여 5건(ch1[7] "1", ch2[8-10] "vaulting", ch2[16] "delighting", ch5[4-7] "desiring", ch7[1-9] "shapely/quintessentially") — 모두 MSG 의미가 틴 문장으로 커버된 오탐으로 분류
5. build_gdocs.py: ALL VERIFY OK (dropped 0)
6. verify_pairing_content.py: PAIRING CONTENT OK (65 data rows, 8 tables)
7. 실제 렌더링: docx 6장 테이블 18행(헤더+17) 직접 확인 — MSG↔EN↔KO 배지·셀 정상 짝지음

## Google Docs
- 폴더: 1I7rLOsUgbr5Ewyq7-IEshCk20scIBtPn
- 제목: 아가 (Song of Songs) — Final: MSG + Teen EN + KO
- 업로드: OK (API title 일치, 테이블 8/8, export-back VERIFIED OK)
- 기록: gdocs_build/upload_results_workerB2.json

## 순서 관련 기록
- 사용자 지정 순서(Psalms → Proverbs → Ecclesiastes → SongOfSongs)와 달리 SongOfSongs를 먼저 처리함 (세션 시작 전 착수된 작업 이어감).
  Psalms → Proverbs → Ecclesiastes 순으로 계속 진행.

## 2차 심층 재검토 (2026-09-25)
- 범위: MSG 원문 ↔ EN 65문단 ↔ KO 65문단 전수 문장 단위 대조 (1~8장). 5장·6장·8장 화자 분리로 배지 중복 구조(5: ['1','1','2','2',...], 6장 § 소제목 행 5개)는 EN/KO 대칭·1차 의도적 구조로 유지 (배지는 Docs 렌더링에서 제외, pairing/validation은 공유 배지로 동작).
- EN 복원 1건 (비대칭 누락 — KO는 이미 보유): 7:1-8 MSG "Shapely and graceful your sandaled feet"가 EN에서 빠져 있었음 ("Wow, you're so beautiful from head to toe..." 로 시작, sandaled feet 미언급) → "Wow, your sandaled feet are so shapely and graceful, and the way you move is so queenly." 복원. KO "와, 샌들 신은 네 발은 완전 예술이고..." 보유.
- EN 전수 중복 스캔: ch2[7]/ch3[5] ("don't stir love"), ch2[17]/ch8[14] ("come like a gazelle") 2건은 MSG 반복 레프라임으로 정당, 조치 없음.
- completeness 잔여 5건 전수 확인: ch1[7] "1"(MSG 'the one left out' 수관사가 아닌 한정 표현), ch2[8-10] "vaulting"(EN "jumping over mountains"), ch2[16] "delighting"(EN "enjoying the flowers"), ch5[4-7] "desiring"(EN "my heart started racing"), ch7[1-8] "quintessentially"(EN "the definition of feminine") — 모두 틴 문장으로 커버된 오탐.
- 게이트: validate PASS 8/8, build 8 tables 65 rows / VERIFY_DROPPED=0 / msg_orphans=0 / teen_without_msg=0, verify_pairing PAIRING CONTENT OK.
- GDocs: doc ID 1QcsY4tMhrBrv_wqu_D6ilM8lUde4yC_GQoYKRKLv5kE, API 8/8 tables, export-back VERIFIED OK.
- 부수 인프라 수정: gdocs_build/reupload.py BOOK_TABLES에 'Exodus':40, 'SongOfSongs':8 누락 항목 추가 (64→66권 근본 수정, export-back 게이트 사용 가능).
