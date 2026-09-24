#!/usr/bin/env python3
"""Apply Numbers ch17-20 audit fixes."""
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

# ==================== CHAPTER 17 ====================
title(17, 'en', "Aaron's Staff Blooms")
rep(17, 'en', 0, "So God hit up Moses and was like, 'Yo, talk to the Israelites.",
    "God spoke to Moses: 'Speak to the Israelites.")
rep(17, 'en', 0, "Make sure to write each guy's name on his own staff.",
    "Write each man's name on his staff.")
rep(17, 'en', 1, 'Moses told the Israelites what was up.',
    'Moses spoke to the Israelites.')
rep(17, 'en', 1, "and yeah, Aaron's was in the mix.",
    "and Aaron's staff was among them.")
rep(17, 'en', 2, 'and, no cap, Aaron\'s staff—the one for the Levi tribe—had totally sprouted.',
    "Aaron's staff, for the tribe of Levi, had sprouted.")
rep(17, 'en', 2, 'It had buds, flowers, and even actual almonds on it! Wild.',
    'It had budded, blossomed, and produced almonds!')
rep(17, 'en', 5, "The Israelites freaked out and said to Moses, 'We're dead.",
    "The Israelites said to Moses, 'We are dying.")
log(17, 'en', 'Slang cleaned; badges already match MSG')

# ==================== CHAPTER 18 ====================
title(18, 'en', "Priests, Levites, and Offerings")
rep(18, 'en', 0, "Alright, so God tells Aaron, 'Look, you, your sons, and your whole fam are on duty for any mess-ups",
    "God said to Aaron, 'You, your sons, and your family are responsible for any offenses")
rep(18, 'en', 0, "So, grab your cousins from the Levi tribe, they're gonna be your crew.",
    "Bring your brothers from the tribe of Levi to join you and assist you.")
rep(18, 'en', 1, 'Your main gig is to manage the Sanctuary and the Altar.',
    'You are in charge of the Sanctuary and the Altar.')
rep(18, 'en', 1, "I've hand-picked your bros, the Levites, from everyone in Israel. Think of them as a gift from me, a God-gift,",
    "I have taken your brothers, the Levites, from the Israelites as a gift to you,")
rep(18, 'en', 2, "Then God said to Aaron, 'Yo, I'm making you the manager of all the stuff people give to me",
    "God said to Aaron, 'I am giving you charge of all the sacred offerings")
rep(18, 'en', 3, "I'm also giving you the best of the best: the finest olive oil, the top-shelf new wine,",
    "I am giving you the best: the finest olive oil, the new wine,")
rep(18, 'en', 4, "When a firstborn baby is a month old, they have to be bought back for five silver shekels, based on the official Sanctuary weight.",
    "When a firstborn is a month old, he must be redeemed for five shekels, using the Sanctuary shekel, which is twenty gerahs.")
rep(18, 'en', 6, "God told Aaron, 'You're not getting any land as an inheritance, not even a tiny piece. I am your inheritance, your plot of ground among the Israelites.'",
    "God told Aaron, 'You will have no inheritance in their land. I am your share and your inheritance among the Israelites.'")
rep(18, 'ko', 4, "아기가 태어난 지 한 달이 되면 성소의 기준으로 은 다섯 세겔을 내고 되사 가야 해.",
    "아기가 태어난 지 한 달이 되면 성소 세겔(한 세겔은 스무 게라)로 은 다섯 세겔을 내고 되사 가야 해.")
log(18, 'en', 'Restored twenty gerahs (MSG 18:16); slang cleaned')
log(18, 'ko', 'Restored twenty gerahs')

# ==================== CHAPTER 19 ====================
title(19, 'en', "The Red Cow and Cleansing Water")
for i, nb in enumerate(['1-4','5-8','9','10','11-13','14-15','16-21','21','22']):
    badge(19, 'en', i, nb); badge(19, 'ko', i, nb)
rep(19, 'en', 0, "God hit up Moses and Aaron with a new rule. He was like, 'Alright, tell the Israelites to find a perfect red cow.",
    "God spoke to Moses and Aaron: 'Tell the Israelites to bring a red heifer without defect.")
rep(19, 'en', 1, 'the whole cow gets burned—skin, meat, blood, even its poop.',
    'the whole heifer is burned—skin, meat, blood, and offal.')
rep(19, 'en', 1, 'and chucks them onto the fire.', 'and throw them onto the fire.')
rep(19, 'en', 1, 'and take a good bath.', 'and bathe himself.')
rep(19, 'en', 2, 'which is like a spiritual reset button.', 'for purification from sin.')
log(19, 'en', 'Badges realigned to MSG units; slang cleaned')

# ==================== CHAPTER 20 ====================
title(20, 'en', "Water from the Rock; Aaron Dies")
for i, nb in enumerate(['1','1','2-5','6','7-8','9-10','11','12','13','14-16','17','18','19','20-21','22','23-26','27-29']):
    badge(20, 'en', i, nb); badge(20, 'ko', i, nb)
rep(20, 'en', 0, 'the whole crew of Israelites rocked up to the Zin Desert',
    'the whole Israelite community arrived at the Desert of Zin')
rep(20, 'en', 2, "Everyone totally ganged up on Moses and Aaron. They went off on Moses, like,",
    "The people quarreled with Moses and said,")
rep(20, 'en', 3, 'Moses and Aaron dipped from the crowd, went to the Tent of Meeting, and just fell on their faces.',
    'Moses and Aaron went from the assembly to the entrance of the Tent of Meeting and fell facedown.')
rep(20, 'en', 5, '“Listen up, you rebels! Do we have to get water from this rock for you?”',
    '“Listen, you rebels! Must we bring you water out of this rock?”')
rep(20, 'en', 6, 'Moses lifted his arm and smacked the rock with his staff—not once, but twice.',
    'Moses raised his arm and struck the rock twice with his staff.')
rep(20, 'en', 11, '“No way. If you even step one foot in my country, I’ll come out and kill you.”',
    '“You may not pass through. If you try, I will come out against you with the sword.”')
rep(20, 'en', 13, 'He shot back again: “No. You can’t come through.”',
    'He said: “You may not pass through.”')
log(20, 'en', 'Badges realigned to MSG units; slang cleaned')

print("FAILED:", FAILED if FAILED else "none")
json.dump(en, open(f'{REVIEW}/fixes/en_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("written")
