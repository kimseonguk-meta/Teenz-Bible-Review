# 창세기 (Genesis) — MSG 기준 전수 감사 리포트

- 감사일: 2026-09-24
- 기준: Eugene Peterson, The Message (MSG) 영어 원문
- 대상: 창세기 1–50장, Teen EN + Teen KO
- 원칙: 의도적 요약 금지 / EN이 primary, KO는 EN과 내용·톤·구조 1:1 / 고유명사·숫자·인용 반복 보존 / 과도한 슬랭 순화

## 0. MSG 원문 파일 복구 (감사용 소스)

`msg_Genesis.txt`에 아래 구간이 빠져 있어 공개 MSG 페이지와 대조 후 복구함.
Teen EN에는 해당 내용이 이미 있었으므로 Teen 누락이 아니라 감사용 원문 파일의 누락이었음.

- 34:25–30 — 시므온·레위 공격, 하몰·세겜 살해, 디나 구출, 도시 약탈(25–29), 야곱의 책망(30). 출처: https://bible-history.com/msg/genesis-34
- 35:27–29 — 야곱이 이삭에게 돌아옴, 이삭 180세, 사망·매장. 출처: https://bible-history.com/msg/genesis-35
- 복구 후 `parse_msg_txt()`로 1–50장 전 장 파싱 확인, 표준 장별 마지막 절과 비교해 절 범위 missing/extra 없음.

## 1. EN 수정 내역 (MSG 대조, 의미 보존)

### 1–10장
| 장:절 | MSG 요지 | 오류 유형 | 수정 |
|---|---|---|---|
| 6:4 | "(and also later)" — 거인 시대가 그때뿐 아니라 이후에도 | 누락 | "Back then—and also later—there were actual giants…" |
| 10:8–12 | "a great hunter before God" 본문+인용 반복 2회 | 누락 | "He was a great hunter before God—so good that people would say, 'You're like Nimrod, a great hunter before God!'" |

### 11–22장
| 장:절 | MSG 요지 | 오류 유형 | 수정 |
|---|---|---|---|
| 11:1–2 | "as they moved out of the east" | 오역(방향 반대) | "moved eastward" → "moved out of the east" |
| 12:8 | "between Bethel to the west and Ai to the east" | 누락 | "between Bethel on the west side and Ai on the east side" 추가 |
| 14:5–7 | "In the fourteenth year" + 지명 7곳 (Ashteroth Karnaim, Ham, Shaveh Kiriathaim, Seir, El Paran, En Mishpat/Kadesh, Hazazon Tamar) | 누락·요약 | 14년째 및 지명 전부 복원 |
| 14:8–9 | 왕·나라 이름 반복 (4 kings against 5) | 의도적 요약 | 왕 이름 전체 반복으로 복원 |
| 14:17–20 | "defeating Kedorlaomer and his allied kings", "the Valley of Shaveh, the King's Valley" | 누락 | 복원 |
| 21:31–32 | "went back to Philistine territory" | 일반화 | "their own territory" → "Philistine territory" |
| 21:33 | "planted a tamarisk tree" | 일반화 | "special tree" → "tamarisk tree" |
| 22:14 | "God-Yireh (God-Sees-to-It)" / "On the mountain of God, he sees to it" | 오역 | "Yahweh-Yireh / The Lord Will Provide" → MSG 명칭으로 복원 |

### 23–34장
| 장:절 | MSG 요지 | 오류 유형 | 수정 |
|---|---|---|---|
| 23:7–9 | "bowed respectfully to the people of the land, the Hittites" | 누락 | 절 대상 명시 |
| 23:16 | "before the town council of Hittites" | 누락 | 추가 |
| 23:17–20 | "the field of Machpelah… next to Mamre, present-day Hebron" | 누락 | "Machpelah", "present-day Hebron" 복원 |
| 24:22–23 | 코걸이 "a little over a quarter of an ounce", 팔찌 "about four ounces" | 누락 | 무게 복원 |
| 24:59–60 | "You're our sister—live bountifully! And your children, triumphantly!" | 오역(MSG 이탈) | MSG 축복문으로 복원 |
| 25:7–11 | "the field of Ephron son of Zohar the Hittite, next to Mamre" | 누락 | 복원 |
| 25:19–20 | "Bethuel the Aramean of Paddan Aram" | 누락 | "of Paddan Aram" 복원 |
| 26:34–35 | "Judith, daughter of Beeri the Hittite, and Basemath, daughter of Elon the Hittite" | 누락 | 아버지 계보 복원 |
| 28:10–12 | "angels of God" | 누락 | "of God" 복원 |
| 30:16–21 | "She named him Issachar (Bartered)" | 오역 | "'Reward'" → "'Bartered'" |
| 31:22–24 | "God came to Laban the Aramean in a dream" | 누락 | "the Aramean" 복원 |
| 31:31–32 | "Jacob answered Laban" | 누락 | "Laban" 반복 복원 |
| 32:1–2 | "Mahanaim (Campground)" | 오역 | "'Two Camps'" → "'Campground'" |
| 32:28 | "you've wrestled with God and you've come through" | 추가(MSG에 없음) | "and with humans" 제거 |
| 33:18–20 | "El-Elohe-Israel (Mighty Is the God of Israel)" | 오역 | "freaking awesome" → "Mighty Is the God of Israel" |

### 35–50장
| 장:절 | MSG 요지 | 오류 유형 | 수정 |
|---|---|---|---|
| 35:8 | "Allon-Bacuth (Weeping Oak)" | 누락 | 고유명사 복원 |
| 35:9–10 | "Jacob (Heel)" | 오역 | "Heel-grabber" → "Heel" |
| 36:18 | "Oholibamah, daughter of Anah" | 누락 | 반복 복원 |
| 36:29–30 | Horite 족장 7명 이름 | 누락 | 전원 복원 |
| 36:31–39 | "Mehetabel, daughter of Matred, daughter of Me-Zahab" | 누락 | 계보 복원 |
| 37:36 | "the manager of his household affairs" | 오역 | "captain of the guard" → MSG 직책으로 수정 |
| 38:12, 20–21 | "Hirah of Adullam" | 누락 | 2회 반복 복원 |
| 39:1 | "bought him from the Ishmaelites", "an Egyptian… the manager of his household" | 누락·오역 | 복원 |
| 39:8–9 | "He treats me as an equal" | 누락 | 복원 |
| 40:12–15 | "the land of the Hebrews" | 누락 | 복원 |
| 41:5–7, 22–24, 25–27 | "dried out by the east wind" | 누락 | 3회 반복 복원 |
| 41:45 | "Potiphera, the priest of On (Heliopolis)" | 누락 | 복원 |
| 41:50–52 | "Asenath, the daughter of Potiphera" | 누락 | 반복 복원 |
| 43:11–14 | "The Strong God… give you grace" | 저속 표현 | "the big man upstairs" → MSG 표현으로 수정 |
| 47:11–12 | "Rameses—that is, Goshen" | 누락 | 복원 |
| 47:29–30 | 손을 허벅지 아래에 넣는 맹세 행위 | 누락 | 복원 |
| 48:3–7 | "on our way back from Paddan" | 누락 | 복원 |

### 기계적 완전성 검사(completeness_check.py) 추가 발견 3건
| 장:절 | MSG 요지 | 오류 유형 | 수정 |
|---|---|---|---|
| 14:5 | "In the fourteenth year" | 누락("A year later"로 뭉뚱김) | "In the fourteenth year"로 수정 |
| 50:11 | "at the Atad Threshing Floor" | 누락 | 복원 |
| 50:22–23 | "Ephraim's sons into the third generation" | 누락("great-grandkids"로 뭉뚱김) | "into the third generation"으로 수정 |

## 2. KO 수정 내역 (수정된 EN 기준 1:1)

EN에서 복원한 고유명사·숫자·반복 정보를 KO에 동일 반영 (총 44건).
EN에만 있던 누락 3건(40장 "히브리 땅", 43장 "전능하신 하나님", 48장 "밧단")은 KO에 이미 있어 수정 불필요했음.

주요 항목:
- 6:4 "—그리고 나중에도—", 10:8–12 "하나님 앞에서 위대한 사냥꾼" 2회, 11:1–2 "동쪽에서 나와", 12:8 "서쪽의 벧엘과 동쪽의 아이 사이"
- 14:5–7 지명 7곳(아스드롯 가르나임, 함, 사웨 기랴다임, 세일 산지, 엘바란, 엔미스밧/가데스, 하사손 다말), 14:8–9 왕 이름 반복, 14:17–20 "사웨 골짜기, 즉 왕의 골짜기", 14:5 "14년째"
- 21:32 "블레셋 땅", 21:33 "에셀 나무(타마리스크)", 22:14 "하나님-이레 / 하나님께서 보살피신다"
- 23:7–9 "그 땅의 백성, 헷 족속", 23:16 "헷 족속 의회 앞에서", 23:17–20 "현재의 헤브론인 막벨라 밭"
- 24:22–23 무게, 24:59–60 "풍성하게 살아라! …승리하라!", 25:7–11 "소할의 아들 에브론… 마므레 옆", 25:19–20 "밧단아람의", 26:34–35 "브에리의 딸 유딧… 엘론의 딸 바스맛"
- 30:16–21 "'물물교환'", 31:22–24 "아람 사람 라반", 31:31–32 "야곱이 라반에게 대답했음", 32:1–2 "'진지(야영지)'", 32:28 "사람과도" 제거, 33:18–20 "'이스라엘의 하나님은 강하시다'"
- 35–50장 EN 수정 17건에 대응하는 KO 17건 (알론바굿, '발꿈치', 아나의 딸 오홀리바마, 호리 족장 7명, 마트렛/메사합 계보, 보디발 직책, 아둘람 사람 히라 2회, 이스마엘 사람들, "동등하게", 동풍 3회, 온/헬리오폴리스, 보디베라 반복, 라메세스 곧 고센, 넓적다리 맹세)
- 50:11 "아닷 타작 마당", 50:22–23 "3대째까지"

## 3. 오탐 판정 (수정하지 않음)

- 3:7 "the two of them" → "they": 의미 보존
- 3:12 하나님의 질문: 이미 존재
- 7장 600년·둘째 달·17일·40일: 모두 보존 (checker의 word-form 숫자 한계로 FAIL 표시됐으나 직접 확인)
- 11:6–9 "one people, one language": 보존
- 11:29 두 딸 Milcah와 Iscah: 보존
- 16:14 "God-Alive-Sees-Me": 의미 보존
- 18:17–19, 19:29, 21:27–32: 의미 보존
- 21:5 "Abraham was 100 years old": ch21[1]에 존재 (checker 배지 대응 어긋남)
- 22:20–23 나홀의 8아들: 전원 존재
- 22:15–18 "a second time": 존재
- 30:6 "Vindicated": "'Vindicated'"로 존재
- 34:25–26 "third day… two sons… Hamor and Shechem": 전부 존재
- 42장, 44장, 45장, 46장, 49장: 직접 읽기 결과 수정 없음
- completeness_check.py 잔여 FAIL 60여 건: word-form 숫자("twelve" vs "12"), 일반 토큰("god"/"son"/"father"), 소제목 행으로 인한 배지 대응 어긋남, 형태소 불일치("Canaanites"/"Canaanite") 등 — 전수 트리아지 후 실제 누락 없음 확인

## 4. 슬랭 순화 (의미 손실 없이)

### EN (95건)
- "Yo," → "Hey," / "Listen," (문맥별), "Nah," → "No,"
- "OMG" → "Wow", "dude" → "man/guy", "chilling" → "resting/staying/sitting"
- "freaking out" → "panicking/terrified", "insane" → "intense/massive/amazing/terrible"
- "dumpster fire" → "disaster", "huge beef" → "deep hatred", "work your butt off" → "work hard"
- "legit" → "really/seriously", "Epic" → "Big/amazing", "Spills the Tea" → "Tells His Dreams"
- "the OG" → "the first", "living nightmare" → "absolutely miserable", "total beast" → "a wild one"
- 소제목 6건 포함 (§ God's Epic Promise → § God's Big Promise 등)

### KO (54건)
- "대박" → "놀라운/대단한/기쁜/놀라운" (문맥별), "전설급" → "대단한/엄청난/놀라운"
- "ㅇㅋ" → "알겠어/알겠다고", "ㄴㄴ" → "아니야/걱정하지 마세요", "쫄" → "겁먹"
- "쩔게" → "정말 잘", "빡빡하게" → "열심히/무리하게", "튀어" → "도망가"
- "멘붕" → "당황", "썰 품" → "꿈 이야기를 하다", "짱 먹고" → "최고 권력자"
- "극혐" → "질색", "빅픽처" → "큰 그림", "행님들" → "여러분", "저주받을 각" → "저주받을 판"
- 소제목 7건 포함 (§ 하나님의 대박 약속 → § 하나님의 큰 약속 등)

## 5. 게이트 결과

1. 의미 감사 리포트: 본 문서
2. 수정 반영: EN 48건(내용) + KO 44건(내용), 슬랭 EN 95건 + KO 54건
3. validator (`validate_translation.py`): PASS — 50개 장 모두 통과
4. 기계적 완전성 (`completeness_check.py`): 실제 누락 3건 발견·수정 완료, 잔여는 오탐으로 판정
5. DOCX 빌드: `gdocs_build/Genesis.docx` — teen_ch=50, msg_chapters=50, rows=986, VERIFY_DROPPED=0
6. `verify_pairing_content.py`: 776 data rows in 50 tables — PAIRING CONTENT OK
7. Google Docs: 신규 문서 "창세기 (Genesis) — MSG + Teen EN + KO" 생성, API table 50/50 확인
   - https://docs.google.com/document/d/1tLTAwHwZhBzVh4Dsq7VRjOh_Gwfdu2OrYCUnH9CSkUU/edit?usp=drivesdk
   - PAIRING_MISMATCHES 20건은 전부 MSG_SUPERSET(병합 구조 차이, 내용 누락 아님) — merge/split 구조 변경은 승인 없이 하지 않음

## 6. 검증 범위와 미확인 경계

- MSG↔Teen EN: 1–50장 전 문단 직접 읽기 완료
- KO: 수정된 EN 기준 전수 대조 완료 (문단별 전체 문장)
- Google Docs: API로 table 수·제목 확인. 실제 화면 렌더링(브라우저)은 이 환경에서 불가 — 성욱 기기에서 육안 확인 필요
- 앱 반영: 하지 않음 (성욱 컨펌 전 앱 데이터 수정 금지 원칙)
