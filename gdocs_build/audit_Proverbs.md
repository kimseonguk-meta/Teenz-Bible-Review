# Teenz Bible 번역 감사 — 잠언 (Proverbs)

- 기준: Eugene Peterson, The Message (MSG) 영어 원문. EN이 primary, KO는 EN의 1:1 번역.
- 범위: 1-31장 전수, MSG 609 유닛 ↔ EN 616 문단 ↔ KO 616 문단 대조.
- 원칙: 의도적 요약 금지. Teen-friendly 표현 축소는 허용, MSG의 핵심 이미지·숫자·고유명사·인용구 누락은 복원.
- 금지 슬랭: R1(썰·스포·티·바이브·노캡 등) / R2(고스트·쌩까·왕따 남용 등) / R3(유령·고스트 동사형 남용) / R4(레전드·찐·핫해·꿀잼 등) / R5(한심·또라이·미친 등) / R6(ㅇㅋ·ㄱㄱ·ㅈㅅ 등). `chill`/`bro`는 사용자 지시로 유지.
- "완료"·"final" 표현은 성욱 선언 전까지 사용하지 않음.

## 게이트 결과

| 게이트 | 결과 |
|---|---|
| 1. MSG 전수 대조 이슈 보고 | 43건 EN 이슈 + KO 슬랭 20건 확정 (아래 표) |
| 2. 수정 반영 | EN 44건(스크립트 43 + 후속 1), KO 20건 적용 |
| 3. validate_translation.py | PASS: 31개 장 모두 통과 |
| 4. completeness_check.py | 32건 → 30건 → 29건 (잔여 29건은 대문자·관용구·서수 오탐, 전부 대조 확인) |
| 5. build_gdocs.py (VERIFY_DROPPED=0) | 616행 / MSG 유닛 609 / teen_without_msg=0 / msg_orphans=0 |
| 6. verify_pairing_content.py | 616행, PAIRING CONTENT OK |
| 7. upload_ot_f.py | 신규 Doc 생성, 테이블 31/31, export-back VERIFIED OK (잠언 (Proverbs): MSG + Teen EN + KO) |

## 수정 내역 (장:절 | MSG 요지 | 유형 | 수정)

### EN 수정

| 장:절 | MSG 요지 | 유형 | 수정 내용 |
|---|---|---|---|
| 1:8-19 | 노상 강도들의 꼬드김: 늙은이 구타·강탈·장례식·전리품 싹쓸이·트럭 운반·인생 최고·똑같이 나누기 | 누락 | "beat up old man, mug old woman / funerals / truckload / share alike / time of your life" 복원 |
| 1:22-24 | Wisdom의 부름: "불렀는데 무시하고, 손 내밀었는데 외면" | 축소/슬랭 | "ghosted me"→"you've been ignoring me" / "shut me out" |
| 4:3-9 | 아버지의 훈계: "절대 지혜를 버리지 마라" | 축소 | "don't ghost Wisdom"→"never walk away from Wisdom" |
| 5:15-16 | rain barrel / spring-fed well 비유 | 임의 변경 | water bottle 비유 철회, "rain barrel... well" 복원 |
| 5:17-20 | 배우자 사랑: 아내를 기뻐하는 것 멈추지 마라 | 축소 | "Never stop taking delight in her, and never take her love for granted" 복원 |
| 9:13-18 | 매춘부의 집 초대받는 자들은 지옥에 | 축소 | "a real bad place"→"end up in hell" |
| 10:2 | 정직한 삶은 영원하다 | 슬랭 | "legend"→"lasts forever" |
| 10:19 | 말이 많을수록 진실은 줄어든다 | 의미 변경 | "you're probably lying"→"the less truth comes out" |
| 11:11 | 가십꾼은 비밀을 흘린다 | 슬랭 | "spill secrets"→"will never spill secrets"→"절대 비밀을 어기지 않음"에 맞춰 "will never spill secrets" (유지 확인) |
| 11:28 | 그루터기 vs 하나님 중심의 삶 | 누락 | "dead—a stump / a God-shaped life" 복원 |
| 12:28 | 죄의 길은 지옥으로 직행 | 축소 | "destruction"→"straight to hell" |
| 13:6 | 하나님을 향한 삶이 바른 길로 인도 | 축소 | "Living right"→"Living God's way" |
| 15:2 | 모든 것을 보시는 하나님 | 슬랭 | "No cap" 삭제 |
| 15:3 | 상처 주는 말은 사람을 망가뜨린다 | 슬랭 | "Woke? No." 삭제 |
| 15:5 | 하나님께 충성하는 자 | 슬랭 | "ride-or-die for God"→"fully committed to God" |
| 15:6 | 악한 자의 재물은 금방 파산 | 슬랭 | "total broke-broke energy"→"it'll all fall apart so fast" |
| 15:23 | 마음 맞는 대화의 기쁨 | 슬랭 | "such a vibe"→"such a pleasure" |
| 15:24 | 생각 깊은 자의 삶은 계속 상승 | 슬랭 | "leveling up"→"keeps rising higher" |
| 16:25 | 겉보기엔 멀쩡한 길이 사실은 지옥행 | 축소 | "destruction"→"leading straight to hell" |
| 16:29 | 자기 할머니 등도 칠 인간들 | 누락 | "they'd stab even their own grandmothers in the back" 복원 |
| 17:3 | 남 헐뜯는 대화·더러운 소문 사냥 | 슬랭 | "spill/listening for/That tea"→"putting others down / hunting for dirty gossip" |
| 17:5 | 가난한 자 조롱·남의 불행 즐김의 결과 | 문법 파손 | 깨진 문장 재작성 ("you're gonna face the consequences") |
| 18:17 | 법정에서 먼저 말하는 자 vs 반대 심문 | 축소 | "argument"→"in court... until the other person starts asking questions" |
| 19:7 | 가족마저 피하는 가난한 자 | 슬랭 | "family ghosts you"→"even your own family avoids you" |
| 20:10 | 하나님이 미워하시는 두 가지 (가격표 조작·경비 부풀리기) | 축소 | "these two things God hates" 구조 복원 |
| 20:15 | 지식의 잔 vs 금·보석 치장 | 슬랭 | "ultimate flex"→"Hands down, it's the real treasure" |
| 20:26 | 농부의 키질, 선별 | 슬랭 | "pro-gamer move"→"a farmer who knows exactly what he's doing" |
| 20:29 | 흰머리는 영광의 면류관 | 슬랭 | "ultimate crown"→"crown of glory" |
| 20:30 | 매로 악을 정화 | 오타 | "A good a good beating"→"A good beating" |
| 21:16 | 바른 길에서 벗어나면 유령들 모임행 | 슬랭 | "No cap" 삭제 (유령 자체는 MSG 원문이라 유지) |
| 22:5 | 막사는 길의 가시·함정 | 슬랭 | "booby traps"→"traps" |
| 22:14 | 매춘부의 입은 바닥없는 구덩이 | 의미 변경 | "shady person/black hole"→"prostitute... bottomless pit" |
| 23:23 | 진리를 사랑으로도 돈으로도 팔지 마라 | 누락 | "not for love or money" 복원 |
| 24:28-29 | "네가 한 대로 갚아주겠다, 대가를 치르게 하겠다" | 누락 | "I'll make you pay!" 복원 |
| 25:6 | 왕 앞에서 잘난 척 금지 | 슬랭 | "Peep those people"→"Watch those people" |
| 25:9-10 | 다툼 중 비밀 폭로 금지, 소문 확산 | 슬랭 | "That tea will spread everywhere"→"That news will spread everywhere" |
| 26:12 | 스스로 똑똑하다고 생각하는 자보다 바보가 낫다 | 슬랭 | "no cap" 삭제 |
| 27:6 | 적의 달콤한 말은 망친다 | 슬랭 | "no cap" 삭제 |
| 29:20 | 생각보다 말이 앞서는 자 | 슬랭 | "Peep those people"→"Watch those people" |
| 30:20 | 간음한 여자의 "Who's next?" | 의미 변경 | "What's the big deal?"→"Who's next?" |
| 30:21-23 | 매춘부가 '올해의 여성상'을 받을 때 | 의미 변경 | "착한 남자와 결혼"→"prostitute gets voted 'woman of the year'" 복원 |
| 31:2-3 | "내가 낳은 아이, 하나님께 바친 아들" | 누락 | "the child I bore, the son I dedicated to God!" 복원 |

### KO 수정

| 장:절 | MSG 요지 / EN 대응 | 유형 | 수정 내용 |
|---|---|---|---|
| 1:22-24 | 불렀는데 무시, 손 내밀었는데 외면 | 슬랭(R2) | "쌩깠잖아"→"무시했잖아. ...외면했잖아" |
| 2:16-19 | 악을 게임처럼 즐기는 자들 | 슬랭(R5) | "한심한 애들"→"정말 어리석은 애들" |
| 8:1-11 | 가장 바쁜 교차로 / 정신 차려라 | 슬랭(R4) | "완전 핫플인 사거리"→"제일 번화한 사거리"; "레벨업 좀 하자"→"정신 좀 차리자" |
| 8:12-21 | 진짜 명예와 좋은 평판 | 슬랭(R4) | "찐 명예"→"진짜 명예" |
| 11:28 | 그루터기 같은 인생 | 누락 | "죽은 인생이나 마찬가지"→"죽은 인생이야, 그루터기 같은 거임" |
| 15:24 | 계속 높이 올라가는 삶 | 슬랭 | "계속 레벨업함"→"계속 높이 올라감" |
| 17:17 | 어떤 상황에서도 함께하는 진짜 친구 | 슬랭(R4) | "찐친"→"진짜 친구" |
| 18:2 | 삶을 막 대하는 어리석은 생각 | 슬랭(R5) | "진짜 한심한 생각"→"정말 어리석은 생각" |
| 18:24 | 가족처럼 곁에 붙어있는 진짜 친구 | 슬랭(R4) | "찐친"→"진짜 친구" |
| 20:15 | 지식은 진짜 확실한 보물 | 슬랭(R4) | "진짜 찐부자 플렉스지"→"진짜 확실한 보물임" |
| 20:17 | 처음에 크게 성공해도 끝 보장 없음 | 슬랭(R4) | "대박 터졌다고"→"크게 한탕했다고" |
| 20:27 | 하나님은 우리 속과 겉을 살피심 | EN 대비 부가 | EN에 없는 "이건 진짜 팩트임" 삭제 |
| 21:16 | 유령들 모임에 끼게 됨 | 슬랭(R4) | "이거 찐임" 삭제 |
| 22:14 | 매춘부의 입은 바닥없는 구덩이 | 의미 변경 | "말이 수상한 사람"→"매춘부" |
| 23:23 | 사랑이든 돈이든 그 무엇과도 바꾸지 마라 | 누락 | "절대 팔지 마"→"사랑이든 돈이든 그 무엇과도 바꾸지 마" |
| 25:3 | 진짜 리더의 넓고 깊은 이해심 | 슬랭(R4) | "찐 리더"→"진짜 리더" |
| 27:6 | 적의 달콤한 말은 널 망친다 | 슬랭 | ", 뻥 아냐" 삭제 |
| 30:20 | "다음은 누구?" | 의미 변경 | "'뭐가 문제야?'"→"'다음은 누구?'" |
| 30:21-23 | 매춘부가 '올해의 여성상'을 받을 때 | 의미 변경 | "간음한 여자가 착한 남자와 결혼"→"매춘부가 '올해의 여성상'을 받을 때" |

## 남은 경계 (미확인·오탐)

- completeness_check 잔여 29건은 전부 검사기 오탐(관용구 "a second look/a thing or two", 서수 "first", 대문자 호칭 "Temptress/Indolence" 등)으로 MSG와 대조해 확인함. 실제 누락은 없음.
- ch7:1-5 "who's always trying to come to you secretly"는 MSG에 없는 소규모 부가 표현. 의미 왜곡은 없으나 참고용으로 기록.
- merge/split: 본문에 새로 적용한 것 없음. 기존 split(6:16-19, 30:15-16·18-19·21-23·24-28·29-31)은 pending으로 `fixes/merge_split_Proverbs.md`에 기록.

## 2차 심층 재검토 (2026-09-25)
- 범위: MSG 609 유닛 ↔ EN 616 문단 ↔ KO 616 문단 전수 문장 단위 대조 (1~31장).
- EN 복원 5건 (전부 비대칭 누락 — KO는 이미 MSG 내용 보유):
  - 2:16-19 "every step she takes is one step closer to hell" — 'disaster' → 'hell' (KO 지옥 보유, MSG hell; 9:18·14:12·16:25·27:18에서 EN도 hell 유지 중)
  - 8:1-11 "My mouth chews and savors and relishes the truth—I can't stand even the taste of evil." — KO "진리만 씹고 맛보고 즐김" 보유, EN은 법률식 의역으로 희석돼 있었음
  - 19:12 "the good-natured ones are like fresh morning dew" — 'a refreshing morning' → 'fresh morning dew' (KO "아침 이슬" 보유)
  - 5:15-16 "draw water from your own spring-fed well" — 'well' → 'spring-fed well' (KO "네 샘에서 흐르는 물" 보유)
  - 2:9-15 "can't even tell a road from a tumbleweed" — EN·KO 둘 다 빠진 MSG 비유 복원 (EN "so lost they can't even tell a road from a tumbleweed", KO "길인지 덤불인지도 못 가리는")
- KO 복원 1건: 2:9-15 tumbleweed 비유 (위).
- 게이트: validate PASS 31/31, build 31 tables / VERIFY_DROPPED=0 / msg_orphans=0 / teen_without_msg=0, verify_pairing PAIRING CONTENT OK, completeness 29건 전수 분류 완료 (전부 의인화 호칭·관용구 오탐 — Lady Wisdom/Indolence/Slowness/Calloused climbers/Brash·Impudent·Blasphemer 등 의역 동등).
- GDocs: doc ID 1T-Gg7KS6-knAKKyoh20-sXaadzp8_3j18SIaR_mqbk0, API 31/31 tables, export-back VERIFIED OK.
