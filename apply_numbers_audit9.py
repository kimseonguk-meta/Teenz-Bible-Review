#!/usr/bin/env python3
"""Apply Numbers ch25-28 audit fixes."""
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

# ==================== CHAPTER 25 ====================
title(25, 'en', "Baal of Peor and Phinehas")
badge(25, 'en', 3, '6-9'); badge(25, 'ko', 3, '6-9')
rep(25, 'en', 0, 'So, the Israelites were chilling at a place called Shittim, and some of the guys started hooking up with Moabite girls.',
    'Israel was staying in Shittim, and the men began to indulge in sexual immorality with Moabite women.')
rep(25, 'en', 0, 'It all started when the girls invited them to these wild religious parties. They\'d eat together and then worship their gods. Before you know it, Israel was all in on worshiping this god called Baal of',
    'The women invited them to the sacrifices to their gods. The people ate and bowed down before these gods. So Israel joined in worshiping the Baal of')
rep(25, 'en', 1, 'That’s the only way to get my anger to chill out.”',
    'so that my fierce anger may turn away from Israel.”')
rep(25, 'en', 3, 'Phinehas, the grandson of Aaron the priest, saw it, grabbed his spear,',
    'Phinehas son of Eleazar, the son of Aaron the priest, saw this and grabbed a spear,')
rep(25, 'en', 4, 'God then said to Moses: “Phinehas, son of Eleazar, the priest, has turned my anger away',
    'God said to Moses: “Phinehas son of Eleazar, the son of Aaron the priest, has turned my anger away')
rep(25, 'en', 4, "So, tell him I'm making a peace treaty with him. He and his descendants will be priests forever,",
    "Tell him I am making my covenant of peace with him. He and his descendants will have a covenant of a lasting priesthood,")
rep(25, 'en', 6, 'They totally tricked you with that whole Peor situation,',
    'They treated you as enemies when they deceived you in the Peor incident')
log(25, 'en', 'Restored Phinehas son of Eleazar genealogy; Baal-Peor meaning preserved; badge 6-9 fixed')

# ==================== CHAPTER 26 ====================
title(26, 'en', "The Second Census")
rep(26, 'en', 0, 'Alright, so after that devastating plague, God hit up Moses and Eleazar, Aaron\'s priest son, and was like, “Yo, I need a headcount',
    'After the plague, God spoke to Moses and Eleazar son of Aaron the priest: “Take a census')
rep(26, 'en', 8, 'That was the whole Reubenite squad. They clocked in at 43,730 dudes.',
    'These were the clans of Reuben; those numbered were 43,730.')
rep(26, 'en', 10, '(Quick history refresh: Dathan and Abiram were those community leaders from Korah\'s crew who rebelled against Moses and Aaron. It was a whole thing against God, really.',
    '(Dathan and Abiram were the community leaders who rebelled against Moses and Aaron and were among Korah\'s followers when they rebelled against God.')
rep(26, 'en', 27, 'Judah’s sons Er and Onan had died way back in Canaan.',
    'Er and Onan, sons of Judah, died in Canaan.')
rep(26, 'en', 56, 'Their names were Mahlah, Noah, Hoglah, Milcah, and Tirzah. Total girl power moment.',
    'Their names were Mahlah, Noah, Hoglah, Milcah, and Tirzah.')
rep(26, 'en', 94, 'The grand total number of the People of Israel was a whopping 601,730.',
    'The total number of the Israelites was 601,730.')
rep(26, 'en', 110, 'And get this: not a single one of them was from the group',
    'Not one of them was among those')
log(26, 'en', 'All names and census numbers verified; slang cleaned in summary lines')

# ==================== CHAPTER 27 ====================
title(27, 'en', "Zelophehad's Daughters; Joshua Chosen")
rep(27, 'en', 0, 'So, these sisters, the daughters of a guy named Zelophehad, showed up. Their dad\'s family tree was pretty legit, tracing all the way back to Joseph\'s son Manasseh.',
    'The daughters of Zelophehad son of Hepher, son of Gilead, son of Makir, son of Manasseh, belonged to the clans of Manasseh son of Joseph.')
rep(27, 'en', 1, 'They were like, "Listen up. Our dad died out in the desert.',
    'They said, "Our father died in the wilderness.')
rep(27, 'en', 3, 'And God\'s verdict was: "Yo, Zelophehad\'s daughters have a totally valid point. No cap. Give them their own property,',
    'God said: "The daughters of Zelophehad are right. Give them property as an inheritance')
rep(27, 'en', 7, 'God told Moses, "Get Joshua, son of Nun—he\'s got the Spirit in him!—and lay your hand on him.',
    'God told Moses, "Take Joshua son of Nun, a man in whom is the spirit of leadership, and lay your hand on him.')
log(27, 'en', 'Restored Hepher/Gilead/Makir genealogy; slang cleaned')

# ==================== CHAPTER 28 ====================
title(28, 'en', "Daily, Sabbath, and Festival Offerings")
rep(28, 'en', 0, 'God hit up Moses and was like, "Alright, tell the People of Israel what\'s up. Let them know they\'re in charge of bringing my food—my Fire-Gifts that smell amazing—at the scheduled times.',
    'God spoke to Moses: "Command the Israelites: See that you present to me at the appointed time my food offerings as an aroma pleasing to me.')
rep(28, 'en', 10, 'And remember, the animals have to be healthy, for real.',
    'The animals must be without defect.')
log(28, 'en', 'All quart measurements and offering numbers verified; slang cleaned')

print("FAILED:", FAILED if FAILED else "none")
json.dump(en, open(f'{REVIEW}/fixes/en_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("written")
