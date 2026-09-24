#!/usr/bin/env python3
"""Apply Numbers ch8-12 audit fixes."""
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

# ==================== CHAPTER 8 ====================
title(8, 'en', "Setting Apart the Levites")
for i, nb in enumerate(['1-2','3-4','5-7','8-11','12-14','15-19','20-22','23-26']):
    badge(8, 'en', i, nb); badge(8, 'ko', i, nb)
rep(8, 'en', 0, 'God hit up Moses and said,', 'God spoke to Moses:')
rep(8, 'en', 2, 'get them cleaned up and ready to serve me.', 'purify them.')
rep(8, 'en', 2, "Then they'll be officially clean.", 'Then they will be clean.')
rep(8, 'en', 3, "a 'we're-sorry' offering", 'a sin offering')
rep(8, 'en', 4, "One bull is for the 'we're-sorry' offering", 'One bull is for the sin offering')
rep(8, 'en', 7, 'God then told Moses, “Okay, here are the rules', 'God told Moses: “Here are the rules')
rep(8, 'en', 7, 'When they turn twenty-five, they start working', 'From twenty-five years old, they start working')
rep(8, 'en', 7, 'When they hit fifty, they have to retire.', 'At fifty, they must retire.')
rep(8, 'en', 7, 'They can still help out their buddies with tasks', 'They may assist their brothers with tasks')
log(8, 'en', 'Badges realigned to MSG units; slang cleaned')

# ==================== CHAPTER 9 ====================
title(9, 'en', "Passover and the Cloud")
for i, nb in enumerate(['1-3','4-5','6-7','8','9-12','13','14','15-16','17-23']):
    badge(9, 'en', i, nb); badge(9, 'ko', i, nb)
rep(9, 'en', 0, 'So, God hit up Moses in the Sinai Wilderness.', 'God spoke to Moses in the Sinai Wilderness.')
rep(9, 'en', 0, 'after they bounced from Egypt.', 'after they left Egypt.')
rep(9, 'en', 0, "He was like, 'Tell the Israelites to celebrate Passover on the exact day. No excuses.", "'Tell the Israelites to celebrate Passover at the appointed time.")
rep(9, 'en', 2, 'But, plot twist. Some guys couldn\'t celebrate', 'But some men could not celebrate')
rep(9, 'en', 2, "were like, 'Yo, we're unclean because of a corpse, but why do we have to miss out",
    "said, 'We are unclean because of a corpse, but why should we miss out")
rep(9, 'en', 3, "Moses was like, 'Hold up, let me ask God what to do in your situation.'",
    "Moses said, 'Wait here; let me find out what God commands concerning you.'")
rep(9, 'en', 4, "Then God told Moses, 'Alright, tell the Israelites this:", "God told Moses: 'Tell the Israelites:")
rep(9, 'en', 4, "or you're on a long road trip,", 'or are on a journey,')
rep(9, 'en', 6, 'can totally do it, but they have to follow', 'may do it, but they must follow')
log(9, 'en', 'Badges realigned to MSG units; slang cleaned')

# ==================== CHAPTER 10 ====================
title(10, 'en', "The March Begins")
newb = ['1-3','4-7','8-10','11-13','14-17','18-21','22-24','25-27','28','29','30','31-32','33-35','35','36','36']
for i, nb in enumerate(newb):
    badge(10, 'en', i, nb); badge(10, 'ko', i, nb)
rep(10, 'en', 0, 'God hit up Moses and was like:', 'God spoke to Moses:')
rep(10, 'en', 4, 'First up, the flag for the camp of Judah led the way, squad by squad,',
    'The divisions of the camp of Judah went first,')
rep(10, 'en', 9, '“Yo, we’re heading to the place God promised', '“We are going to the place God promised')
rep(10, 'en', 9, 'we’ll make sure you’re good.', 'we will treat you well.')
rep(10, 'en', 9, 'God has promised awesome things for Israel.', 'God has promised good things for Israel.')
rep(10, 'en', 10, 'But Hobab was like, “Nah, I’m not coming.', 'But Hobab said, “No, I will not go.')
rep(10, 'en', 10, 'I’m going back to my own country and my own family.', 'I am going back to my own land and my own people.')
rep(10, 'en', 11, 'Moses shot back, “Please, don’t leave us.', 'Moses said, “Please do not leave us.')
rep(10, 'en', 11, 'You’re like our GPS.', 'You can be our eyes.')
rep(10, 'en', 11, 'we’ll make sure you get a piece of all the good stuff God does for us.',
    'we will share with you whatever good things God does for us.')
rep(10, 'en', 13, 'Make the haters run for the hills!', 'Make your enemies flee!')
log(10, 'en', 'Badges realigned to MSG units; Hobab dialogue restored; slang cleaned')

print("FAILED:", FAILED if FAILED else "none")
json.dump(en, open(f'{REVIEW}/fixes/en_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("written")
