#!/usr/bin/env python3
"""Apply Numbers ch11-12 audit fixes."""
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

# ==================== CHAPTER 11 ====================
title(11, 'en', "Complaints, Manna, and Quail")
for i, nb in enumerate(['1-3','4-6','7-9','10','11-15','16-17','18-20','21-22','23','24-25','26','27','28','29','30-34','35']):
    badge(11, 'en', i, nb); badge(11, 'ko', i, nb)
rep(11, 'en', 0, 'started complaining big time about their tough life.', 'started complaining about their hardships.')
rep(11, 'en', 0, "God heard it, and let's just say He wasn't thrilled.", 'God heard it and his anger was kindled.')
rep(11, 'en', 0, 'The people freaked out and screamed for Moses to help.', 'The people cried out to Moses for help.')
rep(11, 'en', 1, 'this group of troublemakers who were hanging around got a major craving,',
    'the rabble among them had a strong craving,')
rep(11, 'en', 1, "'Ugh, can't we get some meat?", "'Oh, for meat!")
rep(11, 'en', 4, "So Moses just unloads on God, 'Why are you doing this to me?",
    "Moses said to God, 'Why are you treating me this way?")
rep(11, 'en', 7, "Moses was like, 'Dude, I'm standing here with 600,000 guys,",
    "Moses said, 'I am among 600,000 men,")
rep(11, 'en', 8, "God shot back at Moses, 'So, you think my arm is too short?",
    "God said to Moses, 'Is my arm too short?")
rep(11, 'en', 12, "was like, 'Moses, my dude, you gotta stop them!'",
    "said, 'Moses, my lord, stop them!'")
rep(11, 'en', 13, "'Are you getting jealous for my sake? Man, I wish all of God's people were prophets.",
    "'Are you jealous for my sake? I wish all of God's people were prophets.")
log(11, 'en', 'Badges realigned to MSG units; slang cleaned; 600,000/70/three feet/sixty bushels verified present')

# ==================== CHAPTER 12 ====================
title(12, 'en', "Miriam Challenges Moses")
for i, nb in enumerate(['1-2','1-2','1-2','3-8','3-8','3-8','3-8','9','10','11-12','13','13','14-16','14-16']):
    badge(12, 'en', i, nb)
# KO has 13 paras; map KO badges to match EN content
kob = ['1-2','1-2','1-2','3-8','3-8','3-8','9','10','11-12','13','13','14-16','14-16']
for i, nb in enumerate(kob):
    badge(12, 'ko', i, nb)
rep(12, 'en', 0, 'started lowkey talking smack about Moses behind his back because he’d married a Cushite woman.',
    'spoke against Moses because he had married a Cushite woman.')
rep(12, 'en', 1, 'They were like, “For real? Is Moses the ONLY one God talks through? Doesn’t He talk through us too?”',
    'They said, “Has God only spoken through Moses? Hasn’t he also spoken through us?”')
rep(12, 'en', 2, 'And yeah, God totally overheard them.', 'God heard this.')
rep(12, 'en', 3, 'Quick side note: Moses was a super humble guy, probably the most humble person on Earth, no cap.',
    'Now Moses was very humble, more humble than anyone else on earth.')
rep(12, 'en', 4, 'Then God just suddenly dropped in on Moses, Aaron, and Miriam, saying, “You three, get over to the Tent of Meeting. Now.”',
    'God said to Moses, Aaron, and Miriam, “Come out to the Tent of Meeting, all three of you.”')
rep(12, 'en', 6, '“Listen up, I’m being for real.', '“Listen to my words:')
rep(12, 'en', 6, 'I talk to him directly, like, face-to-face, in plain English, no riddles. He literally sees the form of God.',
    'I speak to him face to face, clearly and not in riddles. He sees the form of God.')
rep(12, 'en', 6, 'So why weren’t you scared to talk against my servant, against Moses?',
    'Why then were you not afraid to speak against my servant Moses?')
rep(12, 'en', 9, '“Please, my guy, please don’t hold this stupid, thoughtless sin against us.',
    '“Please, my lord, do not hold against us the sin we have so foolishly committed.')
log(12, 'en', 'Badges realigned to MSG units; title/slang cleaned')
log(12, 'ko', 'NEEDS APPROVAL: split KO para 4 (5-6) into 5+6 to match EN 14/13-para structure; NOT applied')

print("FAILED:", FAILED if FAILED else "none")
json.dump(en, open(f'{REVIEW}/fixes/en_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("written")
