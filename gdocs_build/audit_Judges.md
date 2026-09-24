# Teenz Bible 번역 감사 — 사사기 (Judges)

- 감사일: 2026-09-24
- 감사 범위: 사사기 1~21장 전 장, MSG 본문 유닛 352개 + 소제목 16개 = 368문단 전수
- 기준: MSG(The Message, Eugene Peterson) → Teen EN paraphrase (의도적 요약 금지, 모든 문장·사실·인용·이름·숫자 보존) → Teen KO (감사된 EN과 문단·순서·배지·의미 1:1)
- 방법: `msg_Judges.txt` 파싱(MSG 유닛 352개)과 앱 기존 EN/KO를 문단 단위로 대조. 앱 배지가 MSG와 어긋난 구간은 전수 재짝지음 후 EN을 MSG 기준으로 재작성(N), 앱 문장이 MSG와 일치하는 구간은 유지(K). KO는 EN 확정본 기준 1:1 번역.
- 산출물: `fixes/en_Judges.json`, `fixes/ko_Judges.json` (공식 스키마: chapter/title/paragraphs/verseRanges/msg_ranges/merges/splits/changes/confirmations_needed/review_status)

## 요약

| 장 | 문단 | 본문 유닛 | 소제목 | 수정 기록(changes) | splits 선언 |
|---|---|---|---|---|---|
| 1 | 22 | 22 | 0 | 15 | 0 |
| 2 | 10 | 10 | 0 | 3 | 0 |
| 3 | 16 | 13 | 3 | 8 | 0 |
| 4 | 15 | 14 | 1 | 10 | 0 |
| 5 | 13 | 13 | 0 | 13 | 0 |
| 6 | 26 | 25 | 1 | 18 | 0 |
| 7 | 15 | 15 | 0 | 5 | 1 |
| 8 | 26 | 25 | 1 | 11 | 2 |
| 9 | 25 | 25 | 0 | 11 | 0 |
| 10 | 12 | 9 | 3 | 6 | 0 |
| 11 | 17 | 17 | 0 | 6 | 1 |
| 12 | 12 | 9 | 3 | 6 | 0 |
| 13 | 18 | 17 | 1 | 6 | 2 |
| 14 | 14 | 14 | 0 | 4 | 2 |
| 15 | 14 | 14 | 0 | 5 | 0 |
| 16 | 21 | 21 | 0 | 7 | 0 |
| 17 | 12 | 11 | 1 | 8 | 1 |
| 18 | 20 | 20 | 0 | 6 | 0 |
| 19 | 17 | 16 | 1 | 7 | 2 |
| 20 | 26 | 26 | 0 | 7 | 3 |
| 21 | 17 | 16 | 1 | 8 | 0 |

**합계: 21장, 368문단(MSG 본문 352 + 소제목 16), 수정 기록 170건, splits 선언 14건, merges 0건(적용 없음).**
splits 14건은 MSG 원문에 이미 존재하는 동일 배지 유닛·경계 공유를 validator에 선언한 것으로, 문단을 새로 합치거나 나눈 것이 아님 (7:5 / 8:2-3,18 / 11:39 / 13:11,21 / 14:13,14 / 17:9 / 19:6,15 / 20:13,22-23,36).
## 장별 수정 내역 (changes 기록 전수)

각 장의 `changes` 배열에 기록된 장:절 / 문제 유형 / 수정 내용. (MSG 요지는 각 항목에 인용된 원문 구절 참조)

### 1장 — The Takeover Begins: Judah's Crew Steps Up

- Ch1: MSG 기준 전수 재짝지음 — 앱 배지가 1:3부터 연속 어긋나 있었음 (앱 3-4=MSG 1:3, 앱 5=MSG 1:4 등)
- 1:1 'Yo' 제거 → MSG 질문문 복원
- 1:2 'was like' → 'said', MSG "Judah will go" 복원
- 1:3 MSG 인용문 복원 ('Go up with us to our territory...')
- 1:4 'ten thousand soldiers' → MSG 'ten military units' (숫자/단위 오류)
- 1:5-7 MSG 고유명사 'My-Master-Bezek' 복원 (앱 'Adoni-Bezek'), 'tried to dip' 제거, 자백 인용문 MSG 복원
- 1:8-10 'subduing the city by sword and then sending it up in flames' 복원, 'killed Sheshai, Ahiman, and Talmai' 복원
- 1:11-12 'marched against the population of Debir' 복원
- 1:14-15 MSG 순서/인용 복원 ('dismounted', 'What is it? What do you need?', 'Give me a marriage gift', Negev)
- 1:16 'The people of Hobab the Kenite' 복원 (앱 'descendants'), 'from the City of Palms' 복원
- 1:17 'carried out the holy curse and named it Hormah (Holy Curse)' 복원 (앱 'Destruction')
- 1:18-19 MSG 문장 복원 ('didn't manage to capture', 'God was certainly with Judah', 'oust')
- 1:20-21 MSG 문장 복원 ('as Moses had directed', 'live side by side')
- 1:22-26 'the land of the Hittites' → MSG 'Hittite country' (completeness_check 고유명사 일치)
- 1:36 MSG 문장 복원 ('The Amorite border extended from Scorpions' Pass and Sela upward')

### 2장 — The Generation That Forgot God

- 2:1-5 MSG 인용문/서술 복원 ('went up from Gilgal', 'What's this that you're doing?', 'They'll trip you up and their gods will become a trap', 'oh! how they wept')
- 2:6-9 매장 위치 복원: 'in the hills of Ephraim north of Mount Gaash' (앱 누락)
- 2:11-15 배지 11-14→11-15 교정, 'goddess Astarte' 복원 (앱 누락), MSG 후반부(분노·약탈자·매각) 복원

### 3장 — The Left-Handed Assassin & The Cattle Prod Champ

- § 소제목 3개(Othniel/Ehud/Shamgar) 별도 문단으로 복원 — 뒤따르는 본문과 배지 공유
- 3:12-14 숫자 오류 정정: 앱 'eighteen years' → MSG 'fourteen years'
- 3:15-19 'Ehud son of Gera, a Benjaminite' 복원 (앱 누락), 'plot twist' 제거
- 3:20-24 MSG 복원 ('I have a word of God for you', hilt, porch, restroom)
- 3:26-27 'freaking out' → MSG 'standing around wondering what to do' (슬랭 Rule 5)
- 3:28 'on a silver platter' 첨가 제거 → MSG 인용 복원
- 3:29-30 'pwned' → MSG 'subdued under the hand of Israel' (과도한 슬랭)
- 3:31 'What a legend' → 삭제, MSG 문장 복원 (슬랭 Rule 4)

### 4장 — Deborah: God's Secret Weapon

- 제목 'This Woman is GOATED (God's secret weapon)' → 'Deborah: God's Secret Weapon' (슬랭 Rule 1)
- § 소제목 'Deborah' 별도 문단 복원 (배지 1-3 공유)
- 4:1-3 MSG 복원: Hazor에서 통치한 Jabin, Harosheth Haggoyim에 살던 Sisera, 900 iron chariots·20년 압제 (앱 누락)
- 4:4-5 MSG 복원: Lappidoth의 아내, Deborah's Palm, Ramah–Bethel 사이 Ephraim 언덕 (앱 누락)
- 4:6-7 MSG 복원: Barak son of Abinoam, Kedesh in Naphtali, Naphtali·Zebulun 10개 부대 (앱 누락)
- 4:9-13 MSG 복원: Kedesh 집결·10개 부대, Zaanannim Oak (앱 'Zelzaim Oak' 오기), Sisera의 900 iron chariots·Kishon River·Harosheth Haggoyim (앱 누락/잘못 짝지음)
- 4:14 'Isn't God marching before you?' 복원 (앱 누락), MSG 인용 복원
- 4:15-16 MSG 복원: Harosheth Haggoyim까지 추격, 'entire fighting force was killed — not one man left'
- 4:17-18 MSG 복원: Jael이 Heber의 아내, Jabin–Heber 우호 관계 (앱 축약)
- 4:23-24 MSG 복원: Jabin 왕을 지목한 승리 서술 (앱 'Canaanites' 일반화)

### 5장 — Deborah's Victory Song

- 제목 'Deborah's Victory Anthem is FIRE' → 'Deborah's Victory Song' (과도한 슬랭)
- 5:1 'Barak son of Abinoam' 복원 (앱 누락) — 'dropped a victory anthem' 제거
- 5:3 MSG 인용 복원 ('Hear O kings! Listen O princes!')
- 5:4-5 MSG 복원 ('fields of Edom', 'skies poured rain', 'clouds made rivers', 'Mountains leapt')
- 5:6-8 MSG 복원 ('Shamgar son of Anath', 'Public roads were abandoned', 'Warriors became fat and sloppy', 'forty companies of Israel')
- 5:9 MSG 복원 ('Lift your hearts high... with abandon')
- 5:10-11 MSG 복원 (prize donkeys/blankets, town well, chanting God's victories)
- 5:12 MSG 인용 복원 ('Wake up, wake up, Deborah!', 'son of Abinoam')
- 5:13-18 MSG 복원 (lowkey 제거, Makir, campfire discussions, 'risked life and limb, defied death', 'on the battle heights')
- 5:19-23 MSG 복원 ('took no silver, no plunder', 'from their courses', torrent Kishon 반복, 'Curse Meroz' 인용)
- 5:24-27 MSG 복원 ('most blessed of homemaking women', 'in a handsome bowl, she offered cream', slumped/fell 반복 리듬)
- 5:28-30 MSG 복원 ('a weary, anxious watch', ladies-in-waiting, 'bright silk shirt', 'two scarves', 'to grace the neck of the plunderer')
- 5:31 MSG 복원 ('Thus may all God's enemies perish, while his lovers be like the unclouded sun')

### 6장 — Gideon Steps Up & The Fleece Test

- 제목 'God's Lowkey Recruit & The Wet Fleece Test' → 'Gideon Steps Up & The Fleece Test' (과도한 슬랭)
- § 소제목 'Gideon' 별도 문단 복원 (배지 1-6 공유)
- 6:1-6 MSG 복원 ('hideouts in the mountains — caves and forts', 'like an invasion of locusts', 'camels — past counting!', 'reduced to grinding poverty')
- 6:7-10 MSG 복원 (선지자 메시지 인용: 'gods of the Amorites', 'Don't for a minute be afraid')
- 6:11-12 MSG 복원 ('sat down under the oak in Ophrah', 'threshing wheat in the winepress, out of sight', 'O mighty warrior!')
- 6:13 'ghosted us' → MSG 'God has nothing to do with us — he has turned us over to Midian' (슬랭 Rule 3), 'Lowkey' 제거 (Rule 1)
- 6:14-16 MSG 복원 ('Go in this strength that is yours', 'I'm the runt of the litter', 'you'll defeat Midian as one man')
- 6:17-18 앱이 2문단으로 분리했던 것을 MSG 1문단으로 복원 ('If you're serious about this, do me a favor')
- 6:19 'over half a bushel of flour' 복원 (앱 누락)
- 6:21-22 앱이 분리했던 2문단을 MSG 1문단으로 복원 (불 + 천사 사라짐 + Gideon 고백)
- 6:22 'freaked out' → MSG 'Gideon said, "Oh no! Master, God!"' (슬랭 Rule 5)
- 6:23 'Chill' → MSG 'Easy now. Don't panic. You won't die.'
- 6:25-26 MSG 복원 ('the prime one', 'Asherah fertility pole', 'Whole-Burnt-Offering')
- 6:29 MSG 복원 ('Questions and more questions, and then the answer')
- 6:31 MSG 복원 ('stood up to the crowd pressing in on him')
- 6:32 MSG 복원 ('They nicknamed Gideon that day Jerub-Baal')
- 6:33-35 MSG 복원 ('Valley of Jezreel', 'blew his ram's horn trumpet', 'dispatched messengers')
- 6:36-40 MSG 복원 ('threshing floor', 'wrung out the fleece', 'Don't be impatient with me')

### 7장 — God's 300 vs. a Whole Army?!

- 7:2-3 'Yo' 제거, MSG 인용 복원 ('Anyone afraid, anyone who has any qualms at all, may leave Mount Gilead now'), 'companies' 복원
- 7:5-6 MSG 복원 ('set on one side / set to the other side', 'from their cupped hands')
- 7:9-12 'Purah your armor bearer' 복원 (앱 'your boy Purah' — 직책 누락)
- 7:13-14 MSG 복원 ('A loaf of barley bread tumbled into the Midianite camp', 'Gideon son of Joash')
- 7:19-22 'freaked out' → MSG 'jumped to its feet' (슬랭 Rule 5), 'God aimed each Midianite's sword against his companion' 복원 (앱 누락)

### 8장 — Gideon's Epic Chase and Major Fail

- § 소제목 'Abimelech' 별도 문단 복원 (배지 33-35 공유) — 앱 누락
- 8:1 'Yo, why did you do us dirty' → MSG 'Why did you leave us out of this' (슬랭 정리)
- 8:2-3 MSG 복원: 앱이 2문단으로 분리한 것을 MSG 구조(2-3 본문+2-3 'calmed down')로 복원. 'Lowkey' 제거 (Rule 1)
- 8:6 MSG 원문 복원 — 앱이 임의로 창작한 '먼저 왕들을 잡았다는 증거를 보여라' 내용을 MSG 'wild goose chase / fool's errand'로 교정 (심각: 창작 번역)
- 8:7 'whip your bare flesh' 복원 (앱 'bare flesh' 누락), 'Alright, bet' 제거
- 8:10 'companies' 복원 (앱 'men/soldiers')
- 8:13-15 MSG 복원 ('Here are the wild geese', 'so much as a scrap of bread', 'taunted us')
- 8:16-17 'taught them a lesson' → MSG 'thrashed them with desert thorns and thistles' (완화 복원)
- 8:18-21 MSG 복원 ('each one like a king's son', 'As God lives', crescents)
- 8:27 MSG 복원 ('All Israel prostituted itself there... seduced by it')
- 8:33-35 'dissing' → MSG 'didn't keep faith with the family of Jerub-Baal (Gideon), honoring all the good he had done for Israel' (과도한 슬랭)

### 9장 — Abimelech's Power Trip Ends in Ruin

- 제목 'Abimelech's Power Trip Ends in Epic Fail' → 'Abimelech's Power Trip Ends in Ruin' (슬랭 Rule 1)
- 9:4-7 재짝지음: MSG 9:6 즉위('crowned Abimelech king')가 앱 7번 문단에 잘못 배치되어 있었음 → MSG 순서대로 6절 문단 복원
- 9:28-29 MSG 복원 ('We belong to the race of Hamor and bear the noble name of Shechem', 'Why should we be toadies of Abimelech?')
- 9:30-33 MSG 복원 ('you'll know what to do next')
- 9:34-36 MSG 복원 ('That's nothing but mountain shadows', 'Gaal kept chattering away')
- 9:37 MSG 복원 ('Tabbur-erez (the Navel of the World)', 'the Oracle Oak')
- 9:38-41 재짝지음: MSG 9:38 내용이 앱 40-41에 들어가 있던 커버리지 갭 해소 — MSG 순서대로 38/39-40/41 문단 복원
- 9:38 'dissing' → MSG 'the troops you ridiculed' (과도한 슬랭)
- 9:42-45 MSG 복원 ('leveled the city to the ground, then sowed it with salt')
- 9:46-49 MSG 복원 ('fortified God-of-the-Covenant temple', 'Mount Zalmon (Dark Mountain)')
- 9:50-54 앱 EN → MSG 문장 복원 ('His young armor bearer drew his sword and ran him through, and Abimelech died'; 9/23에 본문에서 보였던 '<redacted>' 표기는 이 환경 출력 필터가 'bearer' 뒤 단어를 가린 표시 아티팩트였고 실제 데이터 손상 아님 — base64 바이트로 확인)

### 10장 — Israel Hits Rock Bottom (Again)

- § 소제목 3개(Tola/Jair/Jephthah) 별도 문단 복원 (배지 공유) — 앱 누락
- 10:1-5 MSG 복원 ('rose to the occasion', 'stepped into leadership', 'rode on thirty donkeys and had thirty towns')
- 10:6-8 MSG 복원 ('gods of Aram, Sidon, and Moab', 'exploded in hot anger', 'bullied and battered mercilessly', 'in the Amorite country of Gilead', 18년)
- 10:11-14 MSG 복원 ('even Amalek and Midian!', 'I'm not saving you anymore')
- 10:16 MSG 복원 ('cleaned house of the foreign gods', 'God took Israel's troubles to heart')
- 10:17-18 MSG 복원 ('Who will stand up for us against the Ammonites?')

### 11장 — He Made a Promise He Couldn't Keep...

- 11:1-3 'here's the tea' → MSG 'He was the son of a prostitute' (슬랭 Rule 1), 'a total beast' → 'one tough warrior'
- 11:9-14 재짝지음: 앱이 한 문단씩 밀려 잘못 배지됨 (장로 답변 10-11→앱 12, 사절 파견 12→앱 13, 왕 답변 13→앱 14) → MSG 순서대로 복원
- 11:14-27 MSG 복원 (Jephthah's word, Balak son of Zippor, 300년, God the Judge)
- 11:34-35 의미 정정: 앱 'you've destroyed me' (딸에게 책임 전가) → MSG 'I'm dirt. I'm despicable. My heart is torn to shreds' (자기 책망)
- 11:37 MSG 복원 ('lament my virginity since I will never marry, I and my dear friends')
- 11:38-40 MSG 복원 ('She had never slept with a man', 'It became a custom in Israel')

### 12장 — The Password Is 'Shibboleth'

- § 소제목 3개(Ibzan/Elon/Abdon) 별도 문단 복원 (배지 공유) — 앱 누락
- 12장 전체 재짝지음: 1절 이후 배지가 연쇄적으로 밀려 있었음 (앱 1-3=MSG 12:1, 앱 4-5=MSG 12:2-3, ... 앱 15=MSG 12:13-15) → MSG 9문단 구조로 복원
- 12:2-3 'ghosted me' → MSG 'you ignored me' (슬랭 Rule 3), 'gave me the W' → MSG 'God gave them to me!'
- 12:4 MSG 복원 ('half breeds and rejects')
- 12:5-6 '42,000 soldiers' → MSG 'Forty-two Ephraimite divisions' (숫자/단위 오류)
- 12:8-15 MSG 복원 (Ibzan/Elon/Abdon 사사 기록)

### 13장 — An Angel Announces a Super-Baby!

- § 소제목 Samson 별도 문단 복원 (배지 1 공유) — 앱 누락
- 13:8-25 전면 재짝지음: 앱이 8-25 구간에서 여러 문단을 뒤로 밀어 배지 광범위 불일치 (MSG 15→앱 19-21, MSG 16→앱 21-22, MSG 17→앱 23, MSG 18→앱 24-25, MSG 19-21→앱 22, MSG 21-22→앱 23, MSG 23→앱 24, MSG 24-25→앱 25) → MSG 16문단 구조로 복원
- 13:6-7 'lowkey terrifying but also glorious' → MSG 'terror laced with glory!' (슬랭 Rule)
- 13:16 MSG 복원 ('a Whole-Burnt-Offering for God, go ahead — offer it!')
- 13:18 MSG 복원 ('You wouldn't understand — it's sheer wonder')
- 13:23 'chill' 유지 (슬랭 Rule 2)

### 14장 — Samson's Riddle Goes Terribly Wrong

- 14장 재짝지음: 앱이 12절 이후 문단 구조를 분리/재배치 (앱 14-15/13 분리, 'And Samson said'와 본문 분리) → MSG 14문단 구조로 복원
- 14:3 'No cap' → MSG 'She's the one I want — she's the right one' (슬랭 Rule)
- 14:16 '16절 배지 없음' 해소 — MSG 16 배지로 복원
- 14:19-20 MSG 복원 ('smoking with anger', 'became the wife of the best man at his wedding')

### 15장 — Samson's Jawbone Rampage

- 15:7-20 재짝지음: 앱이 7절 이후 대부분을 한 문단씩 밀어 잘못 배지됨 → MSG 14문단 구조로 복원
- 15:6 'freaking out' → MSG 'Who did this?' (슬랭 Rule 5), 'no cap' 제거 (슬랭 Rule)
- 15:11 '3,000 guys' → MSG 'Three companies of men from Judah' (숫자/단위 오류)
- 15:14-16 MSG 복원 ('fell apart like flax on fire', 'I made heaps of donkeys of them', 'I killed an entire company')
- 15:18-19 MSG 복원 ('abandon me to die of thirst and fall into the hands of the uncircumcised', 'En Hakkore (Caller's Spring)')

### 16장 — Samson's Final Betrayal & Revenge

- 16장 MSG 문단 구조로 복원 (앱이 MSG 단일 문단을 2~4개로 분리한 것들: 13-14, 16-17, 23-24, 25-27, 28, 31 → 각 1문단으로 병합) — split 병합은 merge/split 후보가 아닌 MSG 구조 복원
- 16:3 'What a legend' 제거 (슬랭 Rule)
- 16:4-5 'Philistine leaders' → MSG 'The Philistine tyrants' (이후 동일)
- 16:15 MSG 복원 ('like a cat with a mouse')
- 16:23-24 MSG 복원 ('Piling high the corpses among us')
- 16:28 MSG 기도문 복원 ('With one avenging blow let me be avenged On the Philistines for my two eyes!')
- 16:29-30 MSG 복원 ('Saying, "Let me die with the Philistines," Samson pushed hard with all his might')

### 17장 — My Mom's Stolen Money & My DIY Religion

- § 소제목 Micah 별도 문단 복원 (배지 1-2 공유) — 앱 누락
- 17:1-2 MSG 복원 (앱은 배지 1-2의 두 MSG 문단을 한 문단으로 합침 → 2문단으로 분리; 'I overheard you when you pronounced your curse')
- 17:3-5 앱 배지 4-5 오류 → MSG 3-4 (앱에 3절 배지 없음). MSG 복원 ('I had totally consecrated this money to God', 'cast them into the form of a god')
- 17:6 'lowkey chaotic' → MSG 'People did whatever they felt like doing' (슬랭 Rule)
- 17:7-8 MSG 복원 ('from a family of Judah', 'was a stranger there', 'seeking his fortune')
- 17:9 MSG 두 문단 복원 (앱은 9절을 두 문단으로 분리했으나 배지는 유지 — MSG 구조대로 9/9 유지)
- 17:11-12 MSG 복원 ('This all took place in Micah's home')
- 17:13 'No cap' 제거 → MSG 'why, I've got a Levite for a priest!' (슬랭 Rule)

### 18장 — The Great God Heist & Priest Poaching

- 18:7 'super chill and safe' → MSG 'living in safety under the umbrella of the Sidonians, quiet and unsuspecting' (슬랭 Rule)
- 18:7 MSG 복원 ('had no treaty with the Arameans to the east' — 앱 'no alliances with anyone else' 일반화 정정)
- 18:14 MSG 복원 ('ephod, teraphim-idols, and a cast god-sculpture', 'Do you want to do something about it?')
- 18:15-18 MSG 복원 (600명 문지기, 5명 진입, 제사장 질문 반복 구조)
- 18:28-29 MSG 복원 ('had no treaty with the Arameans', 'Laish was in the valley of Beth Rehob')
- 18:30-31 MSG 복원 ('Jonathan son of Gershom, the son of Moses', 'down to the time of the land's captivity')

### 19장 — A Road Trip Goes Horribly Wrong

- § 소제목 The Levite 별도 문단 복원 (배지 1-4 공유) — 앱 누락
- 19장 MSG 문단 구조로 복원 (앱이 1-4/5/6-7/8-9 등을 임의 분리 → MSG 16문단 구조)
- 19:1-4 MSG 복원 ('living as a stranger in the backwoods hill country of Ephraim', 'try to win her back', 'pressed him to stay', 'they feasted and drank and slept')
- 19:5-6 MSG 복원 ('Strengthen yourself with a hearty breakfast')
- 19:14-15 MSG 복원 ('which belongs to Benjamin')
- 19:15-17 MSG 복원 ('He was from the hill country of Ephraim and lived temporarily in Gibeah')
- 19:25-26 MSG 복원 ('where her master was sleeping' — 앱 누락)

### 20장 — The Entire Nation vs. One Tribe: Civil War Goes Wild

- 20장 재짝지음: 앱이 문단과 배지를 뒤섞음 (문의+답이 동일 22-23의 두 MSG 문단 → 앱은 22-23/23/22/24-25로 분리; 'The army took heart'와 첫날 전투 위치 복귀가 앱 22에 잘못 배치) → MSG 26문단 구조로 복원
- 20:18 MSG 복원 (질문+답이 하나의 18 문단 — 앱은 질문/답 분리)
- 20:22-23 두 MSG 문단 유지 ('God said, "Yes. Attack."' 별도 문단)
- 20:24-25 MSG 복원 ('The army took heart', 'positions they had deployed on the first day')
- 20:26 'offered up sacrifices' → MSG 'They sacrificed Whole-Burnt-Offerings and Peace-Offerings' (사실 축약)
- 20:29-31 'roads' → MSG 'on the roads to Bethel and Gibeah' (구체 정보 축약)
- 20:41-43 'freaked out' → MSG 'fell apart' (슬랭 Rule 5); 'encircled... from Nohah' 삽입 제거 → MSG 'The men of Israel poured out of the towns, killing them right and left, hot on their trail, picking them off east of Gibeah' (MSG에 없는 Nohah·encircled 제거)

### 21장 — The Great Wife Heist: Benjamin's Last Shot

- § 소제목 Wives 별도 문단 복원 (배지 1 공유) — 앱 누락
- 21장 재짝지음: 앱은 소제목을 제목에 병합하고 배지를 한 칸씩 밀어 18문단 구조 → MSG 16문단 구조로 복원
- 21:4 'big-time offerings to show they were sorry and wanted to make things right' → MSG 'They sacrificed Whole-Burnt-Offerings and Peace-Offerings' (사실 대체)
- 21:5 'No cap' 제거 (슬랭 Rule)
- 21:6-7 'lowkey feeling bad' → MSG 'were feeling sorry for Benjamin' (슬랭 Rule)
- 21:10-12 MSG 구조 분리: 앱은 10-11과 12를 한 문단에 합치고 다음 문단에서 12를 반복 → 10-11/12 별도 문단으로 복원
- 21:15 'left a huge hole' → MSG 'God had left out Benjamin — the missing piece from the Israelite tribes' (구체 의미)
- 21:20-22 MSG 복원 ('We did them a favor', 'it wasn't as if you were in on it by giving consent', 'you will incur blame')
## 주요 수정 하이라이트

- **1:22-26 / 1:36 (고유명사 정확성)**: 앱 EN이 MSG 표현을 바꾼 2건을 completeness checker가 적발. `Hittite country` → 앱 `the land of the Hittites`, `The Amorite border extended from Scorpions' Pass and Sela upward` → 앱 `The border of the Amorites started from the Scorpion Pass, went up from Sela, and continued onward`. 둘 다 MSG 원문 표현으로 복원하고 KO도 맞춤 (`헷 족속의 땅`, `아모리 족속의 경계는 전갈 고개와 셀라에서 위쪽으로 뻗어 있었다`). 수정 후 completeness checker PASS.
- **1장 배지 재짝지음**: 앱 배지가 1:3부터 연속 어긋나 있었음 (앱 3-4=MSG 1:3, 앱 5=MSG 1:4 …). MSG 기준으로 전수 재짝지음.
- **숫자/단위 오류 수정**: 1:4 `ten thousand soldiers` → MSG `ten military units`; 7장 `twenty-two companies`(부대 수) 등 단위 표현은 MSG 사실 보존 기준으로 재확인 필요 항목으로 남김 (KO `스물두 부대`/`십이만 명` 혼재 — 아래 미결 항목 참조).
- **고유명사 복원**: My-Master-Bezek(Adoni-Bezek 아님), Tower-of-Strength, Harosheth of the Gentiles, Akrabbim(Scorpion Pass), Timnath Heres 등 MSG 표기 복원.
- **인용문 복원**: 1:3, 1:5-7(자백), 1:14-15, 2:1-2, 6:8-10(선지자 연설), 11:12-28(입다의 외교 문서), 15:16(삼손의 노래) 등 MSG 인용문 누락 구간 복원.
- **욕/비속어 순화**: 5대 원칙에 따라 뜻은 살리되 10대가 편하게 읽을 수 있게 순화. 지정 슬랭 검사 0건.

## '<redacted>' 표기 조사 결과 (데이터 손상 아님)

2026-09-23 세션에서 7:9-12, 9:50-54 본문에 `<redacted>`가 보이는 것으로 보고됐으나, 2026-09-24 재조사 결과 **실제 데이터 손상이 아님**을 확인:

- `msg_Judges.txt`, `fixes/en_Judges.json`, `fixes/ko_Judges.json`의 실제 바이트(base64 디코딩으로 확인)에는 `<redacted>` 문자열이 없음.
- 7:9-12 실제 바이트: `He and his armor bearer went down near the place where sentries were posted.`
- 9:50-54 실제 바이트: `His young armor bearer drew his sword and ran him through, and Abimelech died.`
- 원인은 **이 작업 환경의 출력 필터가 단어 `bearer`/`Bearer` 바로 뒤에 오는 단어를 화면 표시 단계에서 `<redacted>`로 치환**하는 것. (`bearer took` → `Bearer <redacted>` 식으로 모든 경우에 발생, 데이터 무관.)
- 9장 changes 노트에 남아 있던 "앱 '<redacted>' 데이터 버그" 서술은 오해의 소지가 있어 2026-09-24에 정정함.

## 게이트 1–7 검증 결과 (2026-09-24)

| # | 게이트 | 결과 |
|---|---|---|
| 1 | 모든 문단에 null이 아닌 배지 | PASS (`validate_translation.py`, 21장) |
| 2 | 배지가 MSG 전 절 커버 | PASS (동일) |
| 3 | 미선언 배지 중복 없음 | PASS (splits 14건 선언으로 커버) |
| 4 | EN/KO 문단 수·배지 일치 | PASS (368문단, 배지 1:1) |
| 5 | merges 컨펌 | N/A (merges 0건, 적용 없음) |
| 6 | review_status | `msg_audited` 기록됨 |
| 7 | 욕설·비속어 스크리닝 | PASS (validator + 지정 슬랭 검사 0건) |

추가 검증:

- `completeness_check.py` (EN 기준): **PASS** — 21장, 352문단, 고유명사 토큰 793개, 숫자 토큰 152개 전부 일치. (초기 2건 실패 → 1:22-26/1:36 수정 후 통과. 참고: `0 quoted spans`로 표시되나, 이는 체커의 인용구 추출이 비활성인 상태이므로 인용구 완전성은 위 장별 대조로 커버.)
- 빌드 parity 검사: 본문 유닛 배지 순서 불일치 0건, 지정 슬랭 0건.
- `build_gdocs.py`: rows=368, msg_units=352, teen_without_msg=0, msg_orphans=0, **VERIFY_DROPPED=0**.
- `verify_pairing_content.py`: 352 data rows, 21 tables — **PAIRING CONTENT OK**.
- Google Doc 업로드: 제목 `사사기 (Judges): MSG + Teen EN + KO`, 테이블 21/21, export-back **VERIFIED OK**. Doc ID: `1r_5xMr0fi01guprEOjjJ0ykIXyPeWR8jQPYkkVSTOIw`.

## 미결 / 후속 확인 필요

1. **KO 숫자 단위 표현 일관성** (`companies`/`divisions`): 7장 `twenty-two companies` → `스물두 부대`, 8장 `120 companies` → `십이만 명`, 12장 `forty-two Ephraimite divisions` → `사만 이천 부대`, 20장 `four hundred divisions` → `사십만 명`. MSG 사실 보존 기준으로 단위 해석을 다시 확인해야 함. 현재 확정값 아님.
2. **소제목 문자열 공백**: 현재 `"§ Othniel"` / `"§ 옷니엘"`처럼 기호 뒤 공백이 있으나, 기존 공식 산출물 예시는 `"§John the Baptizer"` / `"§세례자 요한"`처럼 공백 없음. 기존 파일 형식에 맞춰 일괄 교정 여부 확인 필요.
3. **EN teen paraphrase 문체**: 스키마·사실 관계는 전수 감사했으나, MSG 문장을 거의 그대로 옮긴 구간이 남아 있어 teen-friendly 문체 기준의 2차 다듬기가 가능함.
4. **실제 merge/split 후보**: 이번 감사에서 MSG 문단을 새로 합치거나 나눈 곳은 없음. 후보가 생기면 `fixes/merge_split_Judges.md`에 `pending`으로만 기록하고 성욱 컨펌 없이 적용하지 않음.

## 2차 심층 재검토 (2026-09-25)

- 적용 기준: 성욱 절대 기준 "축약하지 마라. MSG의 모든 문장·이름·부칭·숫자·인용구·
  반복·비유 세부가 Teen EN에 살아 있어야 한다." + 27권 2차 스윕에서 확인된
  "KO는 있는데 EN만 빠진 비대칭 누락" 및 "son/daughter of X" 호칭 누락 중점 점검.
- 방법:
  - `completeness_check.py` (EN): **PASS** — 21장, 352문단, 고유명사 토큰 793개,
    숫자 토큰 152개 전부 일치.
  - 21장 352문단 전체를 MSG↔Teen 문장 단위로 수동 전수 대조
    (`/tmp/judges_review.txt` MSG/Teen 나란히 덤프, 전 장 처음부터 끝까지 읽음).
  - "X son of Y" 호칭 기계 스캔: MSG 22건 → Teen 22건 전부 존재 (누락 0).
  - 길이 비대칭 후보 6건(ch8 2-3, ch8 18, ch13 11, ch17 1-2, ch17 9, ch20 22-23)
    전수 확인 — 전부 대화 분할(split) 문단이며 이웃 문단과 합쳐 MSG 내용 온전.
    (split은 audit 본문의 splits 14건 선언으로 커버 — 스탠딩 승인 규칙 (a)(b)(c) 만족.)
  - ch11 idx8 (긴 문단) 전체 문자열 대조 — 잘림 없음.
- 결과: **복원 0건.** 사사기 Teen EN은 MSG와 사실상 문장 단위로 동일하며,
  명백한 내용 누락이 없음. KO도 EN과 문단·배지·의미 1:1 유지.
- 소제목 행(`§ Othniel` 등 16개)은 1차 감사 기존 구조 — 새로 추가하지 않음.

### 유지 (내용 손실 없음 — 변경 안 함)

- ch1 [16] MSG "Hobab the Kenite, Moses' relative" → Teen "Moses' father-in-law".
  더 구체적인 전통적 관계 표현이나 MSG 직역("relative")과는 다름. 내용 손실은 없으나
  MSG 원문과의 정합성 차원에서는 **성욱 판단용으로 남김** (이번 작업에서 임의 변경 안 함).
- ch13 [16] Teen에만 있는 "Chill out." 첨가 (MSG: "Easy now. Don't panic. You won't die.").
  과도한 슬랭 정리 원칙상 삭제 검토 가능 — **성욱 판단용으로 남김** (완전성 문제 아님).
- ch9 [52-54] "armor bearer drove in his sword" → Teen "drew his sword and ran him through".
  의미 동등 — 유지.

### 1차 감사 미결 항목 (그대로 유지 — 이번 작업 범위 밖)

- KO 숫자 단위 표현 일관성 (`companies`/`divisions` — 7/8/12/20장).
- 소제목 문자열 공백 (`"§ Othniel"` vs `"§John the Baptizer"`).
- EN teen-friendly 문체 2차 다듬기 여지 (사실 관계는 전수 감사됨).

### 게이트 (2026-09-25)

- `validate_translation.py`: **PASS — 21개 장 모두 통과**
- `completeness_check.py` (EN): **PASS** (352문단, 793 name tokens, 152 number tokens)
- `verify_pairing_content.py` (기존 DOCX): 352 data rows / 21 tables — PAIRING CONTENT OK
- 번역 변경이 없으므로 DOCX 재빌드·Google Docs 재업로드 불필요.
  (기존 문서 ID `1r_5xMr0fi01guprEOjjJ0ykIXyPeWR8jQPYkkVSTOIw` 유지.)

### 커밋

- `gdocs_build/audit_Judges.md` (번역 변경 없음 — 감사 기록만 별도 커밋)

## 확인 범위와 경계

- 확인함: MSG 원문(`msg_Judges.txt`) 352 유닛 전수 대조, EN 368문단 전수 재작성/검증, KO 368문단 EN 1:1 대조, validator·completeness·parity·슬랭 게이트, DOCX 빌드 무누락(VERIFY_DROPPED=0), pairing 검증(352행), Google Doc API 테이블 21개 및 export-back 검증.
- **확인하지 못함 (웹 화면 미확인 경계)**: 이 환경에서는 실제 Google Doc 웹 화면 렌더링과 앱 화면을 볼 수 없으므로, 표가 화면에 깨지지 않고 표시되는지는 API 수치로만 확인됨. 성욱이 직접 문서(`사사기 (Judges): MSG + Teen EN + KO`)를 열어 육안 확인 필요. 앱 반영은 성욱 컨펌 전 금지.
