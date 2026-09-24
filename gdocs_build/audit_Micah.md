# 미가 (Micah) MSG 전수 감사 보고서

- 감사일: 2026-09-24
- 기준: Eugene Peterson The Message (MSG) — `msg_Micah.txt` (BibleGateway 표본 대조 완료)
- 범위: 미가 1–7장 전수 (MSG 40개 행 ↔ Teen EN 43문단)
- 상태: 구약 — production 앱 미반영

## 게이트 결과

| 게이트 | 결과 |
|---|---|
| MSG 원문 품질 | 7장 전부 존재, 40행, 절 커버리지 완전 (누락 장 없음) |
| validate_translation.py | PASS (7개 장 모두 통과) |
| completeness_check.py (고유명사·이름·인용구) | PASS (43문단, 이름 토큰 63개, 인용구 4개) — 1건 적발 후 수정 |
| build_gdocs.py | rows=43, msg_units=40, VERIFY_DROPPED=0 |
| verify_pairing_content.py | 43 data rows, 7 tables — PAIRING CONTENT OK |
| Google Docs 업로드 | OK — 제목 `미가 (Micah): MSG + Teen EN + KO` (Final 없음), API tables 7/7, export-back VERIFIED OK |
| workerA JSON 기록 | 확인됨 (`upload_results_workerA.json`, id `1Cb3LK9L7epH8rxIhaajSNWQOIpdcfVI_pvtJvPsbUUg`) |

## 수정 건수 (시드 대비 실제 변경)

- EN: 31개 문단 변경 + 배지 세트 1건 변경(ch5)
  - ch1: 4 / ch2: 3 / ch3: 2 / ch4: 6 / ch5: 6 (10→6 구조 재구성) / ch6: 4 / ch7: 6
- KO: 22개 문단 변경, 배지 변경 0건
  - ch1: 4 / ch2: 2 / ch3: 2 / ch4: 5 / ch5: 4 / ch6: 1 / ch7: 4

## 주요 복원 내용

- ch1 3-5: "rock mountains crumble into gravel / river valleys leak like sieves" 복원 (MSG "Mountains sink" 반영)
- ch1 6-7: "vacant lot littered with garbage", "carved and cast gods and goddesses → stove wood and scrap metal", "sacred fertility groves" 복원. 욕설 `whore` → `prostitute` 순화 (의미 보존, validator 금칙어 회피)
- ch1 8-9: "rags", "pack of coyotes", "punishing wounds", "must face the charges" 복원
- ch1 10-16: MSG 지명 말장난 전수 복원 (Telltown, Dustville, Alarmtown, Exitburgh, Last-Stand City, Bittertown, Peace City, Chariotville, Good-byeville, Miragetown, Inheritance City, Glorytown)
- ch2 1-5: "interbreeding evil", "before God and his jury" 복원
- ch2 6-7: "help those who help themselves" 복원
- ch2 12-13: "burst all confinements", "a milling throng of homebound people" 복원 (completeness 적발 후 수정)
- ch3 5-7: "don't pay up and jump on their bandwagon", "'God bless you' → 'God damn you'" (MSG 원문 인용 유지), "The sun has set on you prophets" 복원
- ch3 9-12: "selling their verdicts to the highest bidder", "He'll protect us from disaster", "a few scraggly scrub pines" 복원
- ch4 1-4: "firmly fixed", "swords for shovels / spears for rakes and hoes", "each woman in safety will tend her own garden" 복원
- ch4 6-7: "bruised or banished", "showcase exhibit of God's rule in action" 복원
- ch4 8: "eking out a living in shantytowns" 복원
- ch4 11-12: "Kick her when she's down! Violate her!", "the making of God's people", "wheat being threshed, gold being refined" 복원
- ch4 13: "Be threshed of chaff, be refined of dross", "God's juggernaut" 복원 (KO는 저거너트(무적의 파괴자)로 풀이 병기)
- ch5: MSG 6단락 구조로 재구성 (기존 EN 10문단 임의 분할 → `1`, `2-4`, `5-6`, `7`, `8-9`, `10-15`). EN/KO pairing 정상화. "shepherd-rule", "foster homes", "Nimrod-bullies", "purged and select company of Jacob", "island in the sea of peoples", "dew / summer showers", "young lion loose in a flock of sheep", "no more war. None.", "Asherah poles", "sacred sex-and-power centers", "make a clean sweep" 복원
- ch6 6-7: "show proper respect to the high God", "buckets and barrels of olive oil" 복원
- ch6 8: "what God is looking for in men and women" 복원
- ch6 10-16: "obscene wealth", "down to your last cent", "hollow stomachs, empty hearts", "You'll make jelly but never spread it on your bread", "slavishly followed their fashions" 복원
- ch7 1-2: "cabbages and carrots and corn", "nothing for soup or sandwich or salad" 복원
- ch7 3-6: "The best and brightest are thistles. The top of the line is crabgrass.", "It's exam time", "sons, daughters, in-laws" 복원
- ch7 8-10: "Don't crow over me, enemy", "God's punishing rage", "trash in the gutter" 복원
- ch7 11-13: "a day for stretching your arms, spreading your wings!" 복원
- ch7 14-17: "grove of trees / lotus land", "lush Bashan / green Gilead", "slink like snakes, crawl like cockroaches", "holy fear and trembling" 복원
- ch7 18-20: "turning a blind eye, a deaf ear", "don't nurse your anger", "Father Jacob / Grandfather Abraham" 복원

## 스탠딩 승인 split (내용 손실 없음, EN/KO 일치, 가독성 목적 — fixes JSON의 `splits`에 선언)

1. ch3: MSG 1-3 → 앱 `1`(도입부 "Then I said:") + `2-3`(본문)
2. ch6: MSG 1-2 → 앱 `1`(도입부 "Listen now, listen to God:") + `1-2`(법정 소환 본문)
3. ch7: MSG 1-6 → 앱 `1-2`(절망 묘사) + `3-6`(부패 묘사)

## 적용된 판단 (차단 아님, 기록용)

- ch1 6-7 / ch3 5-7: MSG의 `whore` → `prostitute` 순화 (원칙 5). 단 ch3 5-7의 "God damn you"는 MSG 직접 인용이므로 유지 (validator 금칙어에 없음).
- ch5 10-15: MSG "phallic posts" → EN "Asherah poles" / KO "아세라 목상들" (순화 + EN/KO 1:1 일치). "sacred sex-and-power centers"에서 성적 숭배 의미 보존됨.
- ch5 KO 10-15: 시드 문단이 MSG에 충실하여 그대로 유지.

## 승인 필요

없음. 모든 수정은 MSG 복원·순화 원칙·스탠딩 split 범위 내.

## 검증 범위와 미확인 경계

- MSG 원문 40행과 수정 EN 43문단을 문장 단위로 전수 대조함.
- EN↔KO는 43문단 전수 의미 1:1 대조함.
- Google Docs 렌더링은 API 테이블 수(7/7) + export-back 검증 + pairing content 검증으로 확인. 성욱의 실제 화면(기기) 확인은 이 환경에서 불가.
