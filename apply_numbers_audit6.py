#!/usr/bin/env python3
"""Apply Numbers ch15-16 audit fixes."""
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

# ==================== CHAPTER 15 ====================
title(15, 'en', "Offerings, Sabbath, and Tassels")
for i, nb in enumerate(['1-5','6-7','8-10','11-12','13-16','17-21','22-26','27-28','29','30-31','32-35','36','37-41']):
    badge(15, 'en', i, nb); badge(15, 'ko', i, nb)
rep(15, 'en', 0, 'God hit up Moses and was like, "Speak to the Israelites. Tell them, when you finally roll into the homeland I\'m giving you',
    'God spoke to Moses: "Speak to the Israelites. Tell them, When you enter the land I am giving you')
rep(15, 'en', 0, 'a burnt offering or whatever from your herd or flock for a vow or just because',
    'a burnt offering or a sacrifice for a vow or a freewill offering from your herd or flock')
rep(15, 'en', 1, 'For a ram, you gotta bring', 'For a ram, bring')
rep(15, 'en', 2, 'When you prep a young bull', 'When you prepare a young bull')
rep(15, 'en', 3, 'You gotta do this for each one, no matter how many you\'re preparing.',
    'Do this for each one, no matter how many you prepare.')
rep(15, 'en', 9, 'who sins defiantly, straight-up blaspheming God, must be cut off',
    'who sins defiantly, blaspheming God, must be cut off')
rep(15, 'en', 9, 'That person must be kicked out of the community, totally ostracized, and left alone in their wrongdoing.',
    'That person must be cut off from the community and bear the guilt.')
rep(15, 'en', 10, 'Then God told Moses: "The man gets the death penalty. For real, kill him.',
    'Then God told Moses: "The man must be put to death.')
log(15, 'en', 'Badges realigned to MSG units; quarts verified (check KO liters); slang cleaned')

# ==================== CHAPTER 16 ====================
title(16, 'en', "Korah's Rebellion")
# Content restoration (critical): full genealogies
rep(16, 'en', 0,
    'So one day, this guy Korah, who was a Levite, got all full of himself and decided to start a rebellion against Moses. He got a few guys from the Reubenite tribe—Dathan, Abiram, and On—to join him.',
    'Korah son of Izhar, son of Kohath, son of Levi, started a rebellion against Moses. He took with him Dathan and Abiram, sons of Eliab, and On son of Peleth, from the tribe of Reuben.')
rep(16, 'en', 0, 'And get this, he also convinced 250 other well-known leaders',
    'He also gathered 250 well-known leaders')
rep(16, 'en', 0, "They all ganged up on Moses and Aaron and said, 'You guys have gone too far!",
    "They came together against Moses and Aaron and said, 'You have gone too far!")
rep(16, 'en', 1, 'When Moses heard this, he just fell flat on his face on the ground.',
    'When Moses heard this, he fell facedown.')
rep(16, 'en', 3, "'Now, Korah, this is what I want you and your whole gang to do: Tomorrow, each of you grab a censer.",
    "'Now, Korah, you and all your followers do this: Tomorrow, each of you take a censer.")
rep(16, 'en', 3, "Seriously, you sons of Levi are the ones who have gone too far!'",
    "You sons of Levi have gone too far!'")
rep(16, 'en', 4, "Moses kept going, talking to Korah, 'Listen up, sons of Levi. Isn't it a big enough deal",
    "Moses said to Korah, 'Listen, sons of Levi. Isn't it enough")
rep(16, 'en', 4, "You're not just ganging up on us; you're gangin",
    "You are not just opposing us; you are opposing God")
rep(16, 'en', 5, "Then Moses sent for Dathan and Abiram, but they were like, 'Nah, we're not coming. Isn't it bad enough that you dragged us from a land that was awesome, with plenty of food and water, just to let us die out here in the desert?",
    "Then Moses sent for Dathan and Abiram, but they said, 'We will not come! Isn't it enough that you brought us out of a land flowing with milk and honey to kill us in the wilderness?")
rep(16, 'en', 5, "Let's be real, you failed. You didn't bring us to some amazing new land,",
    "You haven't brought us to a land flowing with milk and honey,")
rep(16, 'en', 6, 'Moses got super angry.', 'Moses became very angry.')
rep(16, 'en', 15, "if the ground splits open and swallows them and all their stuff, and they go down to the grave alive—then you'll kn",
    "if the ground opens its mouth and swallows them and all their belongings, and they go down alive to the grave—then you will know")
# Badge fixes for clear misalignments
for i, nb in enumerate(['1-3','4','5','6-7','8-11','12-14','15','16-17','18','19','20-21','22','23-24','25-26','27','28-30','31-33','34','35','36-38','39-40','41','42','43-45','45','46','47-48','49-50']):
    badge(16, 'en', i, nb); badge(16, 'ko', i, nb)
log(16, 'en', 'Restored Korah/Izhar/Kohath/Levi, Dathan/Abiram sons of Eliab, On son of Peleth, milk-and-honey land; badges realigned; slang cleaned')

print("FAILED:", FAILED if FAILED else "none")
json.dump(en, open(f'{REVIEW}/fixes/en_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("written")
