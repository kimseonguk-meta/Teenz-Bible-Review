#!/usr/bin/env python3
"""Apply Numbers ch13-16 audit fixes."""
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

# ==================== CHAPTER 13 ====================
title(13, 'en', "Scouting Canaan")
# Badges: scout list is MSG 3-15 split; mission 17-20; exploration 21-25; report 26-33
nb13 = ['1-2','3-15','3-15','3-15','3-15','3-15','3-15','3-15','3-15','3-15','3-15','3-15','3-15','3-15','3-15','16','17-20','21-25','26-27','27-29','30','31-33']
for i, nb in enumerate(nb13):
    badge(13, 'en', i, nb); badge(13, 'ko', i, nb)
rep(13, 'en', 0, 'God hit up Moses and was like, "Yo, send some guys to scout the land of Canaan,',
    'God spoke to Moses: "Send some men to scout the land of Canaan,')
rep(13, 'en', 0, "and make sure they're legit.", 'and make sure they are leaders.')
rep(13, 'en', 1, "So, following God's orders, Moses sent them out from the Paran Desert. All of them were the top dogs in Israel, one from each tribe. Here's the squad list:",
    "Following God's orders, Moses sent them out from the Desert of Paran. All of them were leaders in Israel, one from each tribe. Their names were:")
rep(13, 'en', 15, 'Those are the names of the dudes Moses sent to check out the land. Btw, Moses gave Hoshea son of Nun a new name—Joshua, which is pretty cool.',
    'Those are the names of the men Moses sent to scout the land. Moses gave Hoshea son of Nun the name Joshua.')
rep(13, 'en', 16, 'he gave them the mission briefing: "Head up through the Negev and into the hills. Get the full scoop on the land, see what it\'s like. Size up the people: are they tough or nah? Is it a huge population or just a few? Check if the land itself is a vibe or if it\'s trash. Peep their towns:',
    'he instructed them: "Go up through the Negev and into the hill country. See what the land is like. Examine the people: are they strong or weak? Are they many or few? Is the land good or bad? Look at their towns:')
rep(13, 'en', 18, 'Then they spilled the tea on their trip:', 'They reported:')
rep(13, 'en', 19, '"We went to the land you sent us to, and whoa, it\'s seriously flowing with milk and honey! Just look at this fruit!',
    '"We went to the land you sent us to, and it does flow with milk and honey! Here is its fruit.')
rep(13, 'en', 20, 'Caleb cut them off, telling everyone to chill and listen to Moses. He said, "Let\'s go up and take the land—right now. We can totally do it."',
    'Caleb silenced the people before Moses and said, "We should go up and take possession of the land, for we can certainly do it."')
rep(13, 'en', 21, 'But the other guys were like, "No way, we can\'t attack them; they\'re way stronger than us."',
    'But the men said, "We can\'t attack those people; they are stronger than we are."')
rep(13, 'en', 21, 'Bro, we even saw the Nephilim giants—the Anak giants are part of them. Next to them, we felt like grasshoppers.',
    'We even saw the Nephilim there. We seemed like grasshoppers in our own eyes, and we looked the same to them.')
log(13, 'en', 'Badges realigned (scout list=MSG 3-15 split); slang cleaned; Vophsi/Geuel names verified')

# ==================== CHAPTER 14 ====================
title(14, 'en', "Rebellion and Punishment")
rep(14, 'en', 0, 'The whole community basically had a meltdown, crying and complaining all night.',
    'The whole community wept and complained all night.')
rep(14, 'en', 0, 'Seriously, why don’t we just go back to Egypt? Like, right now!”',
    'Why don’t we just go back to Egypt?”')
rep(14, 'en', 3, 'The land we checked out is seriously amazing—like, no cap.',
    'The land we scouted is very good.')
rep(14, 'en', 3, 'Man, we’ll crush them. They have zero protection, and God is on our side.',
    'We will have them for lunch. They have no protection, and God is with us.')
rep(14, 'en', 5, 'Just then, the super bright Glory of God showed up',
    'The Glory of God appeared')
rep(14, 'en', 5, 'I’ve had it—I’m about to send a plague and wipe them out.',
    'I will strike them with a plague and destroy them.')
rep(14, 'en', 13, 'I am so done with the complaints from these grumbling Israelites.',
    'I have heard the complaints of these grumbling Israelites.')
rep(14, 'en', 16, 'who came back and spread fake news about it, making the whole community grumble against Moses—all those men died. They died in a plague right in front of God for spreading lies about the land.',
    'who came back and spread a bad report about the land, making the whole community grumble against Moses—those men died of a plague before God.')
rep(14, 'en', 19, 'But they went anyway. Super reckless and arrogant, they climbed up to the high hill country.',
    'But they went anyway and climbed up to the high hill country.')
rep(14, 'en', 19, 'and beat them badly, chasing them all the way down to a place called Hormah.',
    'and defeated them, chasing them all the way to Hormah.')
log(14, 'en', 'Slang cleaned; 40 years/40 days/ten times verified present')

print("FAILED:", FAILED if FAILED else "none")
json.dump(en, open(f'{REVIEW}/fixes/en_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("written")
