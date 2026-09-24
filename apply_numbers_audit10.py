#!/usr/bin/env python3
"""Apply Numbers ch29-32 audit fixes."""
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

# ==================== CHAPTER 29 ====================
title(29, 'en', "Trumpets, Atonement, and Tabernacles")
rep(29, 'en', 0, '"Okay, so on the first day of the seventh month, everyone needs to gather for a special worship service. No regular work, got it? This is the Day of Trumpet Blasts.',
    '"On the first day of the seventh month, hold a sacred assembly and do no regular work. It is a day for you to sound the trumpets.')
rep(29, 'en', 4, 'Next up, on the fifteenth day of the seventh month, get together for a holy meeting.',
    'On the fifteenth day of the seventh month, hold a sacred assembly.')
rep(29, 'en', 5, 'just like the recipe says.', 'as prescribed.')
rep(29, 'en', 9, 'following the recipe.', 'as prescribed.')
rep(29, 'en', 11, 'a burnt offering of one bull, one ram, and seven one-year-old male lambs, all healthy.',
    'a burnt offering of one bull, one ram and seven male lambs a year old, all without defect.')
log(29, 'en', 'Bull counts 13-7, 2 rams, 14 lambs, quart measures verified; slang cleaned')

# ==================== CHAPTER 30 ====================
title(30, 'en', "Vows and Promises")
rep(30, 'en', 0, 'Moses laid it all out for the leaders of Israel\'s tribes: “Here’s the command from God: If a guy makes a serious promise',
    'Moses said to the heads of the tribes of Israel: “This is what God commands: When a man makes a vow')
rep(30, 'en', 0, 'he can’t just back out. He has to do exactly what he said he would.',
    'he must not break his word but must do everything he said.')
rep(30, 'en', 1, '“Now, if a young woman, still living at her dad\'s place, makes a promise to God, and her dad hears about it but doesn’t say anything, then she’s locked in.',
    '“When a young woman still living in her father\'s household makes a vow to God, and her father hears about it but says nothing, then all her vows stand.')
rep(30, 'en', 2, 'and her husband finds out but is cool with it, then she has to keep her word.',
    'and her husband hears about it but says nothing, then her vows stand.')
rep(30, 'en', 2, 'But if her husband hears it and is like, ‘Uh, I don’t think so,’ he cancels it right then and ther',
    'But if her husband hears about it and objects, then he nullifies the vow')
rep(30, 'en', 3, '“For widows or divorced women, any promise they make is 100% on them. It’s binding.',
    '“Any vow or obligation made by a widow or divorced woman is binding on her.')
log(30, 'en', 'Vow regulations verified; slang cleaned')

# ==================== CHAPTER 31 ====================
title(31, 'en', "Victory Over Midian and the Loot")
badge(31, 'en', 2, '5-6'); badge(31, 'ko', 2, '5-6')
badge(31, 'en', 27, '48-50'); badge(31, 'ko', 27, '48-50')
badge(31, 'en', 28, '51-54'); badge(31, 'ko', 28, '51-54')
rep(31, 'en', 0, 'God hit up Moses and said, “Alright, it’s time to get payback on the Midianites',
    'God said to Moses, “Take vengeance on the Midianites')
rep(31, 'en', 1, 'So Moses told the people, “Gear up. We’re picking guys to go to war against Midian and give them God’s payback.',
    'So Moses said to the people, “Arm some of your men to go to war against the Midianites so that they may carry out God\'s vengeance on them.')
rep(31, 'en', 2, 'They ended up with a squad of twelve thousand soldiers, a thousand from each tribe in Israel.',
    'Twelve thousand men armed for battle, a thousand from each tribe, were supplied from the clans of Israel.')
rep(31, 'en', 3, 'They rolled up on Midian, just like God told Moses to, and they didn’t leave a single man alive.',
    'They fought against Midian, as God commanded Moses, and killed every man.')
rep(31, 'en', 3, 'Oh, and they got Balaam, son of Beor, with a sword too.',
    'They also killed Balaam son of Beor with the sword.')
rep(31, 'en', 4, 'But Moses was lowkey furious with the army officers, the commanders of thousands and hundreds. He was like, “Seriously? You let the women live?',
    'But Moses was angry with the officers of the army, the commanders of thousands and commanders of hundreds. He said, “Have you allowed all the women to live?')
rep(31, 'en', 27, '“Sir, we counted all the soldiers under our command, and not a single one is missing.',
    '“Your servants have counted the soldiers under our command, and not one is missing.')
rep(31, 'en', 27, 'from the gold stuff we found—armlets, bracelets, rings, earrings, all of it—to make things right',
    'from what we took—armlets, bracelets, signet rings, earrings and necklaces—to make atonement')
log(31, 'en', 'All loot numbers verified (675k/72k/61k/32k; 337.5k/36k/30.5k/16k; 675/72/61/32; ~600 lbs); added necklaces; badges fixed; slang cleaned')

# ==================== CHAPTER 32 ====================
title(32, 'en', "Reuben, Gad, and Half of Manasseh Settle East")
rep(32, 'en', 0, 'So, the Reuben and Gad families had, like, a crazy amount of animals.',
    'The Reubenites and Gadites had very large herds and flocks.')
rep(32, 'en', 0, 'They scoped out the lands of Jazer and Gilead and were like, "Whoa, this place is prime real estate for our herds."',
    'They saw that the lands of Jazer and Gilead were suitable for livestock.')
rep(32, 'en', 0, 'So they rolled up to Moses, Eleazar the priest, and the other leaders and',
    'So they came to Moses, Eleazar the priest, and the leaders and')
rep(32, 'en', 2, 'Moses was not having it. He shot back at the Gad and Reuben families, "Hold up. Are you seriously saying you\'re gonna chill here while your brothers go off to fight?',
    'Moses said to the Gadites and Reubenites, "Should your fellow Israelites go to war while you sit here?')
rep(32, 'en', 5, 'They got closer to him and said, "Look, all we wanna do is build some pens',
    'They came up to him and said, "We would like to build pens')
log(32, 'en', 'Tribal negotiations verified; slang cleaned')

print("FAILED:", FAILED if FAILED else "none")
json.dump(en, open(f'{REVIEW}/fixes/en_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("written")
