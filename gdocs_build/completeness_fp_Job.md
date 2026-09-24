# Job completeness 검사 오탐 기록

- 검사일: 2026-09-24
- 대상: `fixes/en_Job.json` (EN 248문단, 42장)
- 검사기: `gdocs_build/completeness_check.py`
- 결과: 27건 FAIL → 전수 수동 대조 결과 **27건 모두 오탐**. 실제 누락 0건.

아래는 각 FAIL 항목이 오탐인 근거 (MSG ↔ Teen 대조).

## 이름(name) 오탐

| 위치 | MSG 토큰 | Teen 표현 | 근거 |
|---|---|---|---|
| ch1 idx8 | sabeans | "Sabean raiders" | 복수형 어미 변형. 의미·지칭 동일 |
| ch1 idx10 | chaldeans | "Chaldean raiders" | 복수형 어미 변형. 의미·지칭 동일 |
| ch11 idx3 | expansive | "living large, not a single worry" | MSG "expansive" → "여유롭게 크게 살다" 의미 보존 |
| ch15 idx0 | pitting | (speech intro 문단) | "Eliphaz from Teman had to say his piece again:" — 내용이 다음 문단에 있음. 구조 split |
| ch16 idx1 | contemptuous | "disrespectful" | 동의어. 의미 보존 |
| ch22 idx0 | temanite | "Eliphaz from Teman" | "Temanite" = "from Teman". 의미 동일 |
| ch27 idx4 | catastrophes, pummeled | (speech intro 문단) | "I'll just use your own words against you:" — 내용이 다음 문단에 있음. 구조 split |
| ch32 idx1 | almighty | (speech intro 문단) | "This is what Elihu... had to say:" — "Almighty"가 다음 문단 본문에 있음. 구조 split |
| ch34 idx8 | defiantly | "shaking your fist at Him" | MSG "Defiantly shaking your fist at God" → 의미 보존 |
| ch37 idx6 | unsurpassable | "unbeatable" | 동의어. 의미 보존 |
| ch38 idx5 | drenching | "soaking" | 동의어. 의미 보존 |
| ch40 idx7 | lazily | "chilling" | MSG "Lazily cool in the leafy shadows" → "Just chilling in the leafy shade". 의미 보존 |
| ch41 idx2 | sinewy | "pure muscle, perfectly sculpted" | MSG "Sinewy and lithe" → 의미 보존 |

## 숫자(number) 오탐

| 위치 | MSG 토큰 | Teen 표현 | 근거 |
|---|---|---|---|
| ch1 idx8 | 1 | "I'm the only one" | MSG "I'm the only one who made it out" → 의미 보존 |
| ch12 idx0 | 2 | (speech intro 문단) | MSG "second fiddle"의 내용이 다음 문단(idx1)에 있음. 구조 split |
| ch15 idx0 | 2 | (speech intro 문단) | MSG "spoke a second time"의 내용이 다음 문단에 있음. 구조 split |
| ch36 idx2 | 1 | 관용 표현 | 문맥상 숫자 아님 |
| ch37 idx0 | 1 | 관용 표현 | 문맥상 숫자 아님 |
| ch38 idx3 | 1 | "first thing" 관용 표현 | "Do you know the first thing about death?" → 숫자 아님 |
| ch42 idx0 | 1, 2 | 관용 표현 | 문맥상 숫자 아님 |

## 인용구(quote) 오탐 — 전부 paraphrase로 의미 보존

### ch12 idx4 [13-25] (8개)
MSG 12:13-25 ↔ Teen 대조:
- deceiver: "both deceived and deceiver" → "the person doing the playing" ✓
- vaunted: "vaunted credentials" → "so-called experts" ✓
- witless: "witless fools" → "total fools" ✓
- divests: "divests kings of royal garments" → "take a king's crown" ✓
- waists: "rag around their waists" → "wear rags" ✓
- deprives: "deprives elders of good sense" → "takes away good judgment" ✓
- disarms: "disarms the strong" → "makes the strong totally weak" ✓
- hauls: "hauls deepest darkness" → "brings deepest shadows into the open" ✓

### ch26 idx2 [5-14] (4개)
- graveyards, unformed, cumulus, tames: 각각 "grave", "shapeless", "clouds", "calms" 계열로 의미 보존

### ch30 idx4 [24-31] (2개)
- heartsick: "been heartsick" → "been heartbroken" ✓
- confronts: 문맥상 의미 보존 ✓

### ch34 idx8 [34-37] (4개)
- ignoramus → "clueless" ✓
- wickedly: 문맥상 의미 보존 ✓
- compounded: "compounded your sin" → "made things worse" ✓
- indictments → "accusations" ✓

### ch36 idx6 [27-33] (4개)
- distills → "purifies" ✓
- cisterns → "rain clouds" ✓
- illumining → "lights up" ✓
- hurls → "throws" ✓

### ch41 idx2 [18-34] (8개)
- erupts → "pours out" ✓
- seamless → "perfectly sculpted, no weak spots" ✓
- lithe → "flexible" ✓
- cowering → "run for cover" ✓
- harmlessly: 문맥상 의미 보존 ✓
- kindling: "splinter of wood" ✓
- inexorable: 문맥상 의미 보존 ✓
- roils → "churns up, whips" ✓

### ch42 idx0 [1-6] (3개)
- ignorantly: "muddying the water... when he doesn't know what he's talking about" ✓
- babbled: "running my mouth" ✓
- crusts: "like gossip", "what other people say" ✓

## 이번 감사에서 실제로 복원한 항목 (오탐 아님)

참고: 아래는 검사기가 잡아낸 것이 아니라 전수 대조에서 발견해 복원한 실제 누락/오역이다.

- ch1:8 "said to Satan" (수신자 이름)
- ch2:11 Teman/Shuhah/Naamath (친구 출신지 3곳)
- ch13:3, ch21:15, ch22:17, ch24:1 "God Almighty"/"the Almighty" (호칭)
- ch17:14, ch30:23 "six feet under"
- ch18:16 "acid rain soaks their ruins"
- ch18:20 "Westerners... easterners..."
- ch21:27 "naively"
- ch30:24 "hit" (오역 "ignore" 정정)
- ch30:29 jackals/owls, ch30:31 fiddle/mouth harp
- ch31:16-18 "welcome at my table", ch31:31-34 second helpings/travelers/Adam/neighbors' gossip/recluse, ch31:35-37 signed name/indictment/poster/prince or pauper, ch31:38-40 ground accuses/furrows' tears/rightful owners/thistles & barley (이미 커밋된 감사에서 복원)
- ch39:26 "thermal updrafts"
- ch40:18 "beech" (오역 "oak" 정정), ch40:24 "housebreak"
- ch41:28 "bullets" (오역 "slingstones" 정정), ch41:34 "king of the deep"
- ch42:3 "muddying the water", ch42:7 "the Temanite", ch42:9 세 호칭 (EN; KO는 이미 복원됨)
- 배지 재정렬: ch12, ch17, ch22 (내용-배지 불일치 정정)
- 슬랭 정리: "GOAT"→"blessed", "goated"→"magnificent/great", "no cap" 삭제, "weak sauce"→"weak", "hit God back"→"answered"
