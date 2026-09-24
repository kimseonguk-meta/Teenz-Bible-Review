# Isaiah Completeness Check — False Positive Analysis
**Date:** 2026-09-24 | **Book:** Isaiah (66 chapters, 429 MSG units)
**Baseline:** 90 flagged → **After fixes:** 67 flagged → **Real fixes applied:** 23 paragraphs

## Summary
The completeness checker flags mechanical mismatches (name/number/quote token absence).
Manual verse-by-verse review against MSG confirmed **23 paragraphs had real omissions**
(all fixed). The remaining 67 flags fall into the categories below — none are real
content losses.

## Category A: Normal synonym / morphological variation (not omissions)
| Flag | MSG | EN | Verdict |
|------|-----|-----|---------|
| ch1 villainous | "villainous" (adj) | "villains" (noun) | Same root, normal form change |
| ch2 clamber | "clamber" | "scramble" | Synonym |
| ch5 evicting | "Evicting" | "kick out" | Normal paraphrase |
| ch5 windbag | "windbag" | equivalent insult | Synonym |
| ch8 hurries | "Hurry-Up... Rush" (name) | conveyed in context | Name meaning rendered |
| ch12 joyfully | "joyfully" | "with joy" | Same meaning |
| ch22 jostling | "jostling" | equivalent | Synonym |
| ch24 corralled/shamefaced | — | equivalents | Synonyms |
| ch28 besotted | "besotted" | equivalent | Synonym |
| ch30 preferring/furiously | — | equivalents | Synonyms |
| ch32 underhanded/indulgent | — | equivalents | Synonyms |
| ch33 peacemaking/centering | — | equivalents | Synonyms |
| ch41 fearfully | — | equivalent | Synonym |

## Category B: MSG source-text concatenation artifacts (checker artifact, not translation issue)
The MSG source file has missing spaces at unit boundaries. The checker treats the
glued token as a "name" that must appear verbatim.
| Flag | MSG artifact | Correct reading |
|------|--------------|-----------------|
| ch2 housewill | "housewill" | "house will" |
| ch3 judahof | "judahof" | "judah of" |
| ch8 shiloahand | "shiloahand" | "shiloah and" |
| ch28 perazimand | "perazimand" | "perazim and" |
| ch45 sabeanswill | "sabeanswill" | "sabeans will" |
| ch55 youbecause | "youbecause" | "you because" |
| ch1 firethat | "firethat" | "fire that" |
| ch60 shipsreturning | "shipsreturning" | "ships returning" |

## Category C: Overlapping verse ranges — content preserved in adjacent paragraph
The checker compares each paragraph against its badge's full verse range, but some
paragraphs share verses with neighbors (declared splits). The "missing" content
is fully present in the adjacent paragraph.
| Paragraph | "Missing" per checker | Actually preserved in |
|-----------|----------------------|---------------------|
| ch10 idx2 (12-13) | king's boast quotes | ch10 idx3 (13-14) |
| ch10 idx6 (24-27) | Assyrian march place-names | ch10 idx7 (27-32) |
| ch16 idx1 (4-5) | Moab's plea | ch16 idx0 (1-4) |
| ch22 idx1 (4-8) | wall/arsenal/water/house details | ch22 idx2 (8-11) |
| ch24 idx3/5 | doom/terror/pit/trap | ch24 idx4 (16-20) |
| ch25 idx2 (9-10) | Moab judgment | ch25 idx3 (10-12) |
| ch48 idx0 | Redeemer message | ch48 idx1 (16-19) |
| ch59 idx3 | God's intervention | ch59 idx4 (15-19) |
| ch63 idx2 | "That's how you led..." | ch63 idx3 (14-19) |
| ch8 idx0/1 | son's name, "Daddy/Mamma" | ch8 idx2 (2-3) |
| ch14 idx2 | (declared merge 7-10) | — |

## Category D: Acceptable teen paraphrase (concept preserved, wording differs)
| Flag | MSG | EN rendering | Verdict |
|------|-----|--------------|---------|
| ch34 thistles/scavenging | creature list | "weeds", "vultures", "owls and crows" | List condensed, representative fauna kept |
| ch63 winepress/spurted/lifeblood | "tread the winepress alone" | "stomped on them like grapes... all by myself" | Winepress image + "alone" both conveyed |
| ch60 darkening/footstool | — | equivalents | Paraphrased |
| ch65 hundredth/confiscates | — | equivalents | Paraphrased |

## Category E: Number flags from paraphrased ordinals/cardinals
e.g. ch2 "3", ch5 "1", ch8 "2", ch11 "1, 4", ch19 "1"×3, ch24 "4, 7", ch33 "1",
ch36 "1", ch37 "1", ch40 "1, 2", ch41 "1", ch42 "1", ch48 "2", ch53 "2", ch66 "10".
All verified: the numbers appear in paraphrased form ("a couple", "second time",
"ten", etc.) or are structural (e.g. "first/second") rather than dropped facts.

## Real fixes applied (23 paragraphs)
See specs_*.json change logs. Categories:
- **Restored proper names:** Sinar (11:11), Ponderosa (14:8), Daystar/Son of Dawn (14:12),
  Mount Zaphon (14:13-14), Valley of Rephaim (17:5), Shihor (23:3), Euphrates (7:20),
  Chaldeans/Bedouins (13:19-20), cherubim-angels (37:16), Telassar (37:12),
  "son of Hilkiah"/"son of Asaph" (36:2, 36:22), "son of Amoz" (37:2, 37:21),
  "son of Remaliah" (7:1, 7:4, 7:9), "son of Tabeel" (7:6), "son of Jotham/son of Uzziah" (7:1),
  Rabshekah (36:11), "King Hezekiah's servants" (37:5)
- **Restored numbers/measures:** "fifty-pound sack"/"quart of grain" (5:10),
  "twelve years old" (7:15), "Davidic government"/"Ephraim" (7:2)
- **Rewrites:** 54:1-6 EN (barren woman/children/nations/abandoned cities restored to
  match KO+MSG), 55:13 "giant sequoias" (EN+KO)

## Declared structural merge
- ch14: MSG print ranges `3-4` and `4-6` overlap on v4; merged to single `3-6`
  paragraph with zero content loss (standing rule: content-complete merge, no approval needed).
