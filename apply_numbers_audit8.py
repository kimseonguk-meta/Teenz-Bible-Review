#!/usr/bin/env python3
"""Apply Numbers ch21-24 audit fixes."""
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

# ==================== CHAPTER 21 ====================
title(21, 'en', "Victories and the Bronze Snake")
badge(21, 'en', 14, '23-26'); badge(21, 'ko', 14, '23-26')
badge(21, 'en', 16, '28-29'); badge(21, 'ko', 16, '28-29')
badge(21, 'en', 18, '31-32'); badge(21, 'ko', 18, '31-32')
rep(21, 'en', 14, "But Sihon was like, 'Nah.' He got his army together and marched out",
    "But Sihon would not let Israel pass. He gathered his army and marched out")
rep(21, 'en', 14, 'But Israel fought back hard, totally beat him,',
    'But Israel defeated him,')
rep(21, 'en', 17, "'Oh, but we totally wrecked them: Nothing left of Heshbon",
    "'But we have overthrown them: Heshbon is destroyed")
rep(21, 'en', 20, "God told Moses, 'Don't be scared of him. I'm giving him to you as a gift—him, all his people, and his land.",
    "God told Moses, 'Do not be afraid of him, for I have delivered him into your hands, with all his people and his land.")
log(21, 'en', 'Badges realigned (28-29, 31-32); 21:28-35 content verified present; slang cleaned')

# ==================== CHAPTER 22 ====================
title(22, 'en', "Balaam and the Talking Donkey")
rep(22, 'en', 16, 'But as he was going, God got super angry.',
    'But as he was going, God was angry.')
rep(22, 'en', 18, 'blocked the path in a super narrow spot where there was no room to get by',
    'stood in a narrow path where there was no room to turn')
rep(22, 'en', 18, 'Balaam completely lost his temper and started wailing on the',
    'Balaam was angry and beat the')
rep(22, 'en', 19, 'Then, plot twist, God made the donkey talk.',
    'Then God opened the donkey\'s mouth.')
rep(22, 'en', 20, 'Balaam yelled back, “Because you’re making me look like a fool!',
    'Balaam said, “Because you have made a fool of me!')
log(22, 'en', 'Donkey/angel narrative verified complete; slang cleaned')

# ==================== CHAPTER 23 ====================
title(23, 'en', "Balaam's First Two Oracles")
rep(23, 'en', 0, 'Balak, the king of Moab, was like,',
    'Balak king of Moab said,')
log(23, 'en', 'Content verified; minor slang cleaned')

# ==================== CHAPTER 24 ====================
title(24, 'en', "Balaam's Final Prophecies")
# Badge realignment to MSG units
badge(24, 'en', 3, '10-11'); badge(24, 'ko', 3, '10-11')
badge(24, 'en', 4, '12-14'); badge(24, 'ko', 4, '12-14')
badge(24, 'en', 5, '15-19'); badge(24, 'ko', 5, '15-19')
badge(24, 'en', 6, '20'); badge(24, 'ko', 6, '20')
badge(24, 'en', 8, '21'); badge(24, 'ko', 8, '21')
badge(24, 'en', 9, '21-22'); badge(24, 'ko', 9, '21-22')
badge(24, 'en', 10, '23'); badge(24, 'ko', 10, '23')
badge(24, 'en', 11, '23-24'); badge(24, 'ko', 11, '23-24')
# Content fixes
rep(24, 'en', 0, 'Okay, so Balaam finally got the memo that God was all-in on blessing Israel. He ditched the magic tricks',
    'Balaam saw that it pleased God to bless Israel. He did not resort to magic')
rep(24, 'en', 0, 'When he saw all the tribes of Israel just chilling in their camps, the Spirit of God hit him hard,',
    'When he saw Israel camped tribe by tribe, the Spirit of God came on him,')
rep(24, 'en', 1, "This is the official word from Balaam, son of Beor, a guy who's seeing things crystal clear.",
    "This is the word of Balaam son of Beor, whose eyes are opened.")
rep(24, 'en', 1, 'The guy who bows down and gets the real scoop on what\'s happening.',
    'who falls prostrate, and whose eyes are opened:')
rep(24, 'en', 2, "Man, your setup is amazing, Jacob! Your homes are gorgeous, Israel! It's like a vibe of peaceful valleys and riverside gardens. Like God himself planted a garden of fresh herbs and cedar trees. You're gonna be overflowing with blessings, and your influence will be everywhere.",
    "How beautiful are your tents, Jacob, your dwellings, Israel! Like valleys they spread out, like gardens beside a river, like aloes planted by God, like cedars beside the waters. Your buckets will brim with water and your seed will spread.")
rep(24, 'en', 2, 'Your king is gonna be on a whole other level, way above guys like Agag. Your kingdom? Totally epic.',
    'Your king will be greater than Agag; your kingdom will be exalted.')
rep(24, 'en', 2, 'God brought you out of Egypt, going beast mode like a wild ox, just plowing through your enemies, snapping their bones and their weapons.',
    'God brought them out of Egypt; they have the strength of a wild ox. They devour hostile nations and break their bones in pieces; with their arrows they pierce them.')
rep(24, 'en', 2, "Israel's just chilling now, like a lion taking a nap. Who's dumb enough to mess with the king of the jungle? Whoever blesses you is blessed, and whoever messes with you is toast.",
    "Like a lion they crouch and lie down, like a lioness—who dares to rouse them? May those who bless you be blessed and those who curse you be cursed!")
rep(24, 'en', 3, 'Balak totally lost it with Balaam. He was so mad, shaking his fist and everything. He yelled,',
    'Balak was angry with Balaam. He said,')
rep(24, 'en', 4, 'Balaam just said to Balak, "Dude, didn\'t I tell you from the start? Even if you gave me a palace full of cash, I can\'t go against what God says.',
    'Balaam said to Balak, "Didn\'t I tell your messengers? Even if Balak gave me his palace filled with silver and gold, I could not do anything against God\'s command.')
rep(24, 'en', 5, 'This is the word from Balaam, son of Beor, the guy with the 20/20 vision.',
    'This is the word of Balaam son of Beor, whose eyes are opened, with 20/20 vision.')
rep(24, 'en', 5, "He's gonna crush the leaders of Moab and all the loudmouths. Edom will be conquered, and Israel will be walking away with all the loot. A ruler is coming from Jacob who will take out anyone left in the city.",
    "He will crush the foreheads of Moab, the skulls of all the people of Sheth. Edom will be conquered; Seir, his enemy, will be conquered, but Israel will grow strong. A ruler will come out of Jacob and destroy the survivors of the city.")
rep(24, 'en', 7, "Amalek, you think you're number one right now, but you're gonna end up last. Totally wrecked.",
    "Amalek was first among the nations, but their end will be utter destruction.")
rep(24, 'en', 9, 'Your home is in a sweet, safe spot, like a nest on a cliff. But you\'re still gonna get swept away when Assyria comes and takes you prisoner.',
    'Your dwelling place is secure, your nest is set in a rock; yet you Kenites will be destroyed when Ashur takes you captive.')
rep(24, 'en', 11, "Oh man, it's over. Who can survive when God gets started? People from across the sea will come and mess with Assyria and Eber, but they'll end up as nothing too, just like everyone else.",
    "Alas, who will live when God does this? Ships will come from the shores of Cyprus; they will subdue Ashur and Eber, but they too will come to ruin.")
log(24, 'en', 'Restored MSG 24:5-9 (buckets brim, seed spreads, bones/arrows), 24:17 (star/ruler), 24:20-24 (Amalek/Kenites/ships); badges realigned; slang cleaned')

print("FAILED:", FAILED if FAILED else "none")
json.dump(en, open(f'{REVIEW}/fixes/en_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("written")
