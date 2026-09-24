#!/usr/bin/env python3
"""Apply Numbers ch33-36 audit fixes."""
import json

REVIEW = '/home/hatch/workspace/teenz-bible-review'
en = json.load(open(f'{REVIEW}/fixes/en_Numbers.json', encoding='utf-8'))
ko = json.load(open(f'{REVIEW}/fixes/ko_Numbers.json', encoding='utf-8'))
FAILED = []
def rep(ch, lang, para, old, new):
    bk = en if lang == 'en' else ko
    p = bk[ch-1]['paragraphs'][para]
    if old not in p:
        FAILED.append((ch, lang, para, old[:60])); return
    bk[ch-1]['paragraphs'][para] = p.replace(old, new, 1)
def badge(ch, lang, para, nb):
    (en if lang=='en' else ko)[ch-1]['verseRanges'][para] = nb
def title(ch, lang, nt):
    (en if lang=='en' else ko)[ch-1]['title'] = nt
def log(ch, lang, t):
    (en if lang=='en' else ko)[ch-1].setdefault('changes', []).append(t)

# ==================== CHAPTER 33 ====================
title(33, 'en', "The Journey from Egypt to Moab")
rep(33, 'en', 0, "Alright, so here's the complete travel log of every single place the Israelites camped after they bounced from Egypt. Moses and Aaron were leading the squad, military-style.",
    "Here is the record of the Israelites' journey after they came out of Egypt, marching out by divisions under Moses and Aaron.")
rep(33, 'en', 1, 'They rolled out of Rameses on the fifteenth day of the first month, right after Passover. They left with their heads held high, super confident.',
    'They set out from Rameses on the fifteenth day of the first month, the day after the Passover. The Israelites marched out defiantly.')
log(33, 'en', 'All 40+ journey stops verified; Aaron age 123 verified; slang cleaned')

# ==================== CHAPTER 34 ====================
title(34, 'en', "Borders and Land Leaders")
rep(34, 'en', 0, "Alright, so God hits up Moses and is like, 'Yo, tell the Israelites the deal. When you roll into Canaan, this is the land you're inheriting. Peep the borders:'",
    "God said to Moses, 'Command the Israelites: When you enter Canaan, this is the land that will be allotted to you as an inheritance. These are its boundaries:")
rep(34, 'en', 1, "'Your southern border is gonna include a piece of the Zin Desert next to Edom. It kicks off east of the Dead Sea, dips south of Scorpion Pass to Zin, keeps going south of Kadesh Barnea, then hits up Hazar Addar and Azmon.",
    "'Your southern border will include part of the Desert of Zin along Edom. It will start in the east from the southern end of the Dead Sea, cross south of Scorpion Pass, continue to Zin, and go south of Kadesh Barnea to Hazar Addar and Azmon.")
rep(34, 'en', 3, "keep it moving to Ziphron, and finish at Hazar Enan. Boom, that's your northern line.'",
    "continue to Ziphron and end at Hazar Enan. This will be your northern border.'")
rep(34, 'en', 4, 'and cruises along the hills east of the Sea of Galilee.',
    'and continue along the slopes east of the Sea of Galilee.')
log(34, 'en', 'All border place names verified; tribal leader names verified; slang cleaned')

# ==================== CHAPTER 35 ====================
title(35, 'en', "Levite Towns and Cities of Refuge")
badge(35, 'en', 9, '22-24'); badge(35, 'ko', 9, '22-24')
rep(35, 'en', 0, 'So, God hit up Moses on the Plains of Moab, right by the Jordan near Jericho, and was like, “Tell the Israelites they need to give the Levites some towns',
    'God spoke to Moses on the plains of Moab by the Jordan near Jericho: “Command the Israelites to give the Levites towns')
rep(35, 'en', 1, 'with the town smack in the middle.',
    'with the town in the center.')
rep(35, 'en', 4, '“But, for real, if the killer used something made of iron, that’s straight-up murder. He’s a murderer, for real, and he has to be executed.',
    '“If anyone strikes someone with an iron object so that they die, they are a murderer; the murderer is to be put to death.')
rep(35, 'en', 9, '“BUT, if someone just randomly pushes another person without any bad history between them, or they just, like, impulsively threw something,',
    '“But if without enmity someone suddenly pushes another or throws something unintentionally,')
rep(35, 'en', 10, '“So, it’s super important that he stays in his sanctuary city until the High Priest dies.',
    '“They must stay in their city of refuge until the death of the high priest.')
log(35, 'en', '48 towns, 6 refuges, measurements verified; badge 22-24 fixed; slang cleaned')

# ==================== CHAPTER 36 ====================
title(36, 'en', "Zelophehad's Daughters Marry")
rep(36, 'en', 0, 'So, the leaders of the Gilead family clan, who were descendants of Joseph, went up to Moses',
    'The family heads of the clan of Gilead son of Makir, son of Manasseh, who were from the clans of the descendants of Joseph, came to Moses')
rep(36, 'en', 1, 'They said, "Look, God told you to give out the land to the Israelites by lottery,',
    'They said, "God commanded you to give the land as an inheritance to the Israelites by lot,')
rep(36, 'en', 2, 'Moses, following God\'s command, gave this order to the Israelites: "The tribe of Joseph has a good point.',
    'Moses commanded the Israelites according to God\'s word: "What the tribe of Joseph is saying is right.')
log(36, 'en', 'Restored Gilead son of Makir, son of Manasseh genealogy; slang cleaned')

print("FAILED:", FAILED if FAILED else "none")
json.dump(en, open(f'{REVIEW}/fixes/en_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("written")
