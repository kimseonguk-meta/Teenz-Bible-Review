# Esther 10장 감사 보고서

**기준**: Eugene Peterson, The Message (MSG) — 최종 진실의 원천. KJV는 후보 선별용으로만 사용.
**범위**: Esther 1–10장 (Teen EN / Teen KO, 각 94문단)
**일자**: Sep 24, 2026
**상태**: MSG 전수 대조 완료, 7개 게이트 전부 수행. "완료" 선언은 성욱만 가능 — 본 보고서는 수행 결과 기록.

## 결론

- **MSG 원문 품질**: `msg_Esther.txt` 파싱 결과 80개 유닛, 10장 전부 정상. 장별 유닛 수 8, 11, 10, 6, 6, 9, 8, 8, 12, 2. 정경 절 범위 전부 커버, 중간 누락 없음. **단, ch5:9–13에 추출 중복 조각(만찬 초대 문장과 "But I can't enjoy…" 시퀀스 중복)이 있어 중복 1건을 원문에서 직접 삭제 후 재파싱(여전히 80유닛).** 재수집 불필요.
- **핵심 발견 1 — 배지 체계 붕괴**: 10장 중 9개 장(ch10 제외)의 EN/KO 배지가 MSG 실제 문단 경계와 어긋나 있었음. 전형 패턴은 1유닛씩 밀림(ch2·3·4·6·7·9) 및 EN/KO 상호 불일치(전 장). 10장 전체 배지를 MSG 유닛 기준으로 재정렬하고 split 13건을 선언함. merge 0건.
- **핵심 발견 2 — 내용 누락 다수**: 내시 7명 이름(1:10), 모르드개 족보+포로 경위(2:5-6), good figure 오역(2:5), Haman 신분(3:1 "highest-ranking official"→"second most powerful" 왜곡), 금식·통곡(4장 "lost it/화난" 왜곡), Haman the Agagite·공문 3건(8:3, 8:5), 부림절 금식·애곡 조항(9:31) 등 복원.
- **핵심 발견 3 — 구 감사 로그(루트 `audit_Esther.md`, 2026-09-23) 폐기**: "감사 완료"를 주장했으나 실제 파일에는 배지 붕괴·누락·슬랭·깨진 문자가 그대로 남아 있었고, ch7:8을 MSG와 정반대로 기록했다("신하들이 하만의 얼굴을 가렸다" — MSG 원문은 "all the blood drained from Haman's face"이므로 기존 'Haman went pale/핏기가 싹 가셨다'가 맞다). 해당 파일은 본 보고서로 대체되며, 루트 파일은 은퇴 안내문으로 교체했다.
- **수정 규모**: EN 본문 38/94문단·배지 40/94, KO 본문 35/94문단·배지 62/94, EN/KO 제목 5건. validator PASS 유지.

## 수정 이슈 표 (주요 복원 — 전체 변경은 JSON `changes` 필드 참조)

| 장:절 | MSG 근거 | 유형 | 수정 내용 |
|---|---|---|---|
| 1:4-7 | cotton curtains, linen/purple cords, porphyry/marble/mother-of-pearl/colored stones, one-of-a-kind chalices | EN 세부 누락 | flex/flex-fest→showing off/display; 커튼·끈·돌 4종·"one of a kind" 복원 |
| 1:8-9 | King Xerxes's royal palace | EN/KO 누락 | 왕궁 소유격 복원 |
| 1:10 | Mehuman, Biztha, Harbona, Bigtha, Abagtha, Zethar, Carcas | EN 이름 7명 누락 | 7 내시 이름 전원 복원 |
| 1:12-15 | seven princes of Persia and Media; King Xerxes's summons | EN 세부 누락 | 왕자들·소환장 복원 |
| 1:16-18 | Persian and Mede officials; "King Xerxes ordered her..." (인용구) | EN 누락 | officials 복원; 인용구 속 King Xerxes 복원 |
| 1:19-20 | laws of the Persians and Medes; banned from King Xerxes' presence | EN/KO 누락 | Persians and Medes·King Xerxes' presence 복원 (배지 16-19→16-18, 20-21→19-20 정정 후 올바른 문단에 귀속) |
| 1 (제목) | — (슬랭) | 슬랭 | Gets Ghosted→Gets Rejected |
| 2:1-4 | second thoughts | EN 누락 | "second thoughts about what Vashti had done..." 복원 |
| 2:5-7 | son of Jair, son of Shimei, son of Kish—a Benjaminite; exiles with King Jehoiachin of Judah by Nebuchadnezzar of Babylon; good figure | EN 족보·경위 누락, 오역 | 족보 3대·여호야긴·느부갓네살 복원; "great personality"→"great figure" 정정; a Benjaminite 복원 |
| 2:15 | daughter of Abihail, Mordecai's uncle | EN 누락 | 아비하일의 딸(모르드개의 삼촌) 복원 |
| 2:16 | the month of Tebeth | EN 누락 | Tebeth 복원 |
| 2 (제목) | — (슬랭) | 슬랭 | Glow-Up→Rise |
| 3:1-2 | highest-ranking official; Haman son of Hammedatha the Agagite | EN 의미 왜곡 | "second most powerful"→"highest-ranking official" 정정 |
| 3:10 | Haman son of Hammedatha the Agagite | EN 부칭 누락 | 부칭 복원 |
| 3:13 | Bulletins | EN 누락 | Bulletins 복원 |
| 4:1-3 | sackcloth and ashes, fasting, weeping, wailing | EN/KO 의미 왜곡 | "lost it/화난"→애도(옷 찢고 재 뒤집어씀·대성통곡) 정정 |
| 4:9-11 | a single rule; The one exception; thirty days | EN/KO 누락 | single fate/rule·one exception·thirty days 복원 |
| 4:12-14 | help and deliverance | EN 누락 | help and deliverance 복원 |
| 5:1-3 | gold scepter | KO 오역 | 지팡이→홀 |
| 5:14 | seventy-five feet | KO 오역 | 23미터→75피트 |
| 6:2 | Bigthana and Teresh, entrance guards, plot to assassinate King Xerxes | EN 세부 누락 | 경위 복원 |
| 6:6-9 | royal crown on horse's head; one of the king's most noble princes | EN 세부 누락 | 왕관·귀족 복원; OMG 삭제 |
| 6:12-13 | his knowledgeable friends and Zeresh; no chance | EN 세부 누락 | knowledgeable friends 복원; toast→finished |
| 6 (제목) | — (슬랭) | 슬랭 | Epic Fail→Downfall |
| 7:6 | An enemy. An adversary. | EN 슬랭 | hater→adversary (MSG 원문) |
| 7:8 | "all the blood drained from Haman's face" | 구 감사 오판 정정 | went pale/핏기가 싹 가셨다 유지 (구 로그의 "얼굴을 가렸다"는 오판) |
| 7:9 | Harbona, one of the king's eunuchs; 75 feet | EN 세부 누락 | 하르보나 신분 복원; Yo, check it out→Look at this |
| 7 (제목) | — (슬랭) | 슬랭 | Epic Fail→Downfall |
| 8:3, 8:5 | Haman the Agagite; the bulletins authorizing the plan of Haman son of Hammedatha the Agagite | EN 3건 누락 | 전원 복원 |
| 8:10 | bulletins | EN 누락 | official notices→bulletins |
| 8:13 | in all King Xerxes' provinces | EN 누락 | 복원 |
| 8:15 | fine linen; magnificent | EN 누락·슬랭 | fine linen 복원; total boss→magnificent |
| 9:2 | fear made cowards of them all | EN 슬랭 | shook→fear made cowards of them all (MSG 원문) |
| 9:10 | Haman son of Hammedatha, the archenemy of the Jews | EN 부칭 누락 | 복원 (열 아들 이름은 기존 유지) |
| 9:20-22 | the sending and receiving of presents | KO 오역 | 음식을 나눠 먹고→선물을 주고받고 |
| 9:29-32 | Esther's full queenly authority; calming and reassuring letters; 127 provinces; dates set by Mordecai; fasting and mourning | EN/KO 압축·누락 | fasting and mourning 조항·127 provinces 복원 |
| 10:1-2 | The Chronicles of the Kings of Media and Persia | EN/KO 명칭 | 역대기 원제 유지·정정 |
| 10:3 | peace and prosperity | EN/KO | peace and prosperity 복원; glow-up→rise |
| 10 (제목) | — (슬랭) | 슬랭 | Epic Glow-Up→Epic Rise |
| 전장 | 아하수에로→크세르크세스; 유다/유다인→유대인; 깨진 문자(�) | KO 표기 | 전수 통일 |

## Split / Merge 선언

전부 순수 구조 분할(내용 온전·EN/KO 일치·가독성 목적)이며, 성욱 승인 없이 선언하고 진행했다. merge 0건.

| 장 | msg_range | 문단 | 비고 |
|---|---|---|---|
| 1 | 1-3 | [0, 1] | 왕 소개 / 3년차 연회 — 장면 전환 |
| 2 | 1-4 | [0, 1] | 왕의 후회·신하 제안 / 왕의 승인 |
| 5 | 1-3 | [0, 1] | 에스더 등장·홀 / 왕의 질문 |
| 5 | 5-6 | [3, 4] | 하만 소환 명령 / 만찬 중 왕의 질문 |
| 5 | 14 | [7, 8] | 교수대 제안 / 하만의 실행 |
| 6 | 3 | [1, 2] | 왕의 질문 / 신하 답변 |
| 6 | 4 | [3, 4] | 왕의 질문 / 하만 등장 |
| 6 | 5 | [5, 6] | 신하 보고 / 왕의 "들여보내라" |
| 6 | 6-9 | [7, 8] | 왕의 질문·하만 속생각 / 하만의 제안 |
| 7 | 6 | [4, 5] | 에스더의 지목 / 하만의 공포 |
| 7 | 7-8 | [6, 7, 8] | 왕 퇴장 / 하만 애원·왕 귀환 / 왕의 질책 |
| 7 | 9 | [9, 10] | 하르보나의 보고 / 왕의 명령 |
| 9 | 1-4 | [0, 1] | 날짜·역전 선언 / 성읍 집결·관리 지원 |

## 승인 필요

없음. 내용 모호·오역 미해결·EN/KO 의미 불일치 잔존 없음. split 13건은 전부 순수 구조 분할로 선언 완료.

## 게이트 결과

1. **validate_translation.py**: `PASS: 10개 장 모두 통과` (배지 null/커버리지/중복/EN-KO parity 검사)
2. **completeness_check.py** (기계적 완전성): 94문단·이름 190토큰·숫자 63토큰·인용 1건 검사. 수정 후 잔여 FAIL 3건은 전부 검사기 오탐으로 판정 → `gdocs_build/completeness_fp_Esther.md`에 근거 기록.
   - ch1 `seething`: 문두 일반 형용사를 고유명사로 오인 (Teen "fuming"으로 의미 존재)
   - ch9 `27`: "thirteenth and fourteenth"를 13+14=27로 합산하는 파서 버그 (Teen에 13th·14th 개별 존재)
   - ch9 `29`: "fourteenth and fifteenth"를 14+15=29로 합산하는 파서 버그 (Teen에 14th·15th 개별 존재)
   - 검사기가 잡아낸 실제 누락 5건은 전부 수정: one-of-a-kind(1:6), 인용구 속 King Xerxes(1:17), Persians and Medes·King Xerxes' presence(1:19), second thoughts(2:1), a Benjaminite(2:5)
3. **build_gdocs.py**: `rows=94 msg_units=80 teen_without_msg=0 msg_orphans=0 VERIFY_DROPPED=0`, "ALL VERIFY OK"
4. **verify_pairing_content.py**: `checked 94 data rows in 10 tables / PAIRING CONTENT OK`
5. **Google Docs 업로드**: 기존 Doc(2026-09-23 생성, 구 제목에 "Final" 포함) 내용 갱신 → API 테이블 10/10 확인 → export-back `VERIFIED OK` → 제목을 `에스더 (Esther): MSG + Teen EN + KO`로 정정(Drive API 확인). "Final" 없음.
   - Doc ID: `1tuVsF6HDNB_s6o9wFI3oVqtrptK_WxgSDeJA4CKW-Lg`
   - 링크: https://docs.google.com/document/d/1tuVsF6HDNB_s6o9wFI3oVqtrptK_WxgSDeJA4CKW-Lg/edit?usp=drivesdk

## 검증 범위와 경계

- **검증됨**: MSG 원문 파싱(80유닛·정경 커버리지), EN/KO 전 문단(94개) MSG 직접 대조, 이름·숫자·인용구 기계 검사, validator PASS, 빌드 행수·pairing·10 테이블·export-back.
- **미검증 경계**: 공개 페이지(Bible Gateway MSG HTML) 재대조는 ch1·ch5(중복 조각 확인)·ch10만 spot-check. 10장 전체를 공개 페이지와 독립 재대조하지는 않았다. ch5의 중복 조각은 원문 파일에서 직접 제거하고 재파싱으로 확인했다.
- **앱 미반영**: 성욱 컨펌 전이므로 앱에는 반영하지 않았다.

## 수정 건수 (baseline 대비)

- EN: 본문 38/94문단 변경, 배지 40/94 변경, 제목 5건
- KO: 본문 35/94문단 변경, 배지 62/94 변경, 제목 5건(EN과 동일)
- split 선언 13건, merge 0건
- 변경 내역은 각 JSON의 `changes` 필드와 `/tmp/est_audit/apply_esther_audit.py`, `/tmp/est_audit/apply_esther_followup.py`에 기록
