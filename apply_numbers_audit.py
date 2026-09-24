#!/usr/bin/env python3
"""Apply Numbers MSG audit fixes. Run once. Verifies each replacement."""
import json, sys

REVIEW = '/home/hatch/workspace/teenz-bible-review'
en = json.load(open(f'{REVIEW}/fixes/en_Numbers.json', encoding='utf-8'))
ko = json.load(open(f'{REVIEW}/fixes/ko_Numbers.json', encoding='utf-8'))

FIXES = []   # (ch, lang, para, old, new)
BADGES = []  # (ch, lang, para, new_badge)
TITLES = []  # (ch, lang, new_title)
LOGS = []    # (ch, lang, text)
FAILED = []

def F(ch, lang, para, old, new):
    FIXES.append((ch, lang, para, old, new))

def apply():
    books = {'en': en, 'ko': ko}
    # KO ch1: delete 13 duplicated leader-list paras (indices 2-14)
    kc1 = ko[0]
    assert len(kc1['paragraphs']) == 33, f"KO ch1 paras {len(kc1['paragraphs'])}"
    del kc1['paragraphs'][2:15]
    del kc1['verseRanges'][2:15]
    assert len(kc1['paragraphs']) == 20, f"KO ch1 after delete {len(kc1['paragraphs'])}"
    assert kc1['verseRanges'][1] == '6-15', kc1['verseRanges'][1]
    for (ch, lang, para, old, new) in FIXES:
        bk = books[lang]
        c = bk[ch - 1]
        assert c['chapter'] == ch, f"chapter mismatch {ch}"
        p = c['paragraphs'][para]
        if old not in p:
            FAILED.append((ch, lang, para, old[:60]))
            continue
        c['paragraphs'][para] = p.replace(old, new, 1)
    for (ch, lang, para, nb) in BADGES:
        books[lang][ch - 1]['verseRanges'][para] = nb
    for (ch, lang, nt) in TITLES:
        books[lang][ch - 1]['title'] = nt
    for (ch, lang, t) in LOGS:
        books[lang][ch - 1].setdefault('changes', []).append(t)

# ==================== CHAPTER 1 ====================
TITLES.append((1, 'en', "God's Army Census"))
F(1, 'en', 0, 'God hit up Moses in the Sinai Wilderness.', 'God spoke to Moses in the Sinai Wilderness.')
F(1, 'en', 0, 'two years after the Israelites bounced from Egypt.', 'two years after the Israelites left Egypt.')
F(1, 'en', 0, 'God said, “Yo, I need a headcount', 'God said, “I need a headcount')
F(1, 'en', 0, 'get the name of every single guy.', 'get the name of every single male.')
F(1, 'en', 0, 'every dude who is 20 or older', 'every man who is twenty years and older')
F(1, 'en', 1, "From Reuben, you've got Elizur", 'from Reuben: Elizur')
F(1, 'en', 2, 'These were the guys hand-picked', 'These were the men hand-picked')
F(1, 'en', 3, 'got these chosen dudes together', 'gathered these chosen men')
F(1, 'en', 3, 'listing all the guys who were 20 or older', 'listing all the men who were twenty years and older')
BADGES.append((1, 'en', 1, '6-15'))
LOGS.append((1, 'en', 'MSG 1-5 split into paras 0-1 (declared); badges 1-5/6-15; slang cleaned'))
LOGS.append((1, 'ko', 'REMOVED 13 duplicated leader-list paras (indices 2-14); kept combined 6-15 para'))

# ==================== CHAPTER 2 ====================
TITLES.append((2, 'en', "Israel's Camp Layout"))
BADGES.append((2, 'en', 0, '1-2'))
F(2, 'en', 0, 'God hit up Moses and Aaron and was like, “Yo, here’s the deal.', 'God spoke to Moses and Aaron. He said, “Here’s the deal.')
F(2, 'en', 1, 'Judah’s crew sets up', 'Judah’s division sets up')
F(2, 'en', 1, 'His squad is massive, like 74,600 troops.', 'His division numbers 74,600 troops.')
F(2, 'en', 4, 'is a wild 186,400', 'is 186,400')
F(2, 'en', 9, 'smack in the middle of everyone, you have', 'in the middle, there is')
F(2, 'en', 9, 'each repping their own flag', 'each under their own flag')
F(2, 'en', 19, 'No cap.', '')
LOGS.append((2, 'en', 'Badge 1-3->1-2 (MSG unit 1-2); slang cleaned'))

# ==================== CHAPTER 3 ====================
TITLES.append((3, 'en', "God's Special Team: The Levites"))
BADGES.append((3, 'en', 2, '5-10'))
BADGES.append((3, 'en', 11, '27-32'))
BADGES.append((3, 'en', 18, '44-48'))
F(3, 'en', 1, 'messed up big time', 'made a serious mistake')
F(3, 'en', 1, 'got zapped, dying right there', 'died right there')
F(3, 'en', 2, 'God hit up Moses and was like, “Yo, bring the tribe of Levi over to Aaron.', 'God spoke to Moses: “Bring the tribe of Levi to Aaron.')
F(3, 'en', 2, 'They’re gonna be his support crew.', 'They will assist him.')
F(3, 'en', 2, 'doing all the hands-on work', 'doing the work')
F(3, 'en', 2, 'Their whole gig is to manage', 'Their job is to manage')
F(3, 'en', 2, 'basically running the place while the Israelites come to do their thing.', 'running the operations for the Israelites.')
F(3, 'en', 2, "they're the designated full-time crew.", 'they are the designated crew.')
F(3, 'en', 2, 'Anyone else who tries to jump in on that action will be taken out. For real.', 'Anyone else who tries to do priest work will be put to death.')
F(3, 'en', 3, 'Listen up. I’ve picked', 'I’ve picked')
F(3, 'en', 4, 'count every guy who is a month old or older', 'count every male a month old or older')
F(3, 'en', 9, 'So yeah, those are the clans of Levi, family by family.', 'Those are the clans of Levi, family by family.')
F(3, 'en', 10, 'All the guys a month or older added up to 7,500.', 'All the males a month or older added up to 7,500.')
F(3, 'en', 11, 'All the guys a month or older in these Kohathite clans numbered 8,600.', 'All the males a month or older in these Kohathite clans numbered 8,600.')
F(3, 'en', 12, 'he was the big boss over all of them.', 'he supervised them all.')
F(3, 'en', 13, 'The guys a month or older in these Merarite clans numbered 6,200.', 'The males a month or older in these Merarite clans numbered 6,200.')
F(3, 'en', 13, 'you know, all that structural stuff.', 'all the structural elements.')
F(3, 'en', 14, 'And the rule was, anyone else who tried to do their job would be put to death. Seriously.', 'Anyone else who tried to do their job would be put to death.')
F(3, 'en', 15, 'all the guys one month and older, was 22,000.', 'all the males one month and older, was 22,000.')
F(3, 'en', 16, 'Then God told Moses, “Okay, now count', 'Then God told Moses, “Now count')
F(3, 'en', 17, 'The total number of firstborn guys a month or older', 'The total number of firstborn males a month or older')
F(3, 'en', 18, 'you need to collect five shekels for each of them. Use the official Sanctuary shekel.', 'collect five shekels for each one, using the Sanctuary shekel.')
F(3, 'en', 18, 'Now, to buy back the 273 extra firstborn Israelites who outnumber the Levites,', 'To redeem the 273 extra firstborn who outnumber the Levites,')
F(3, 'en', 19, 'From those 273 guys, he collected 1,365 shekels of silver.', 'For the 273, he collected 1,365 shekels.')
# MSG 44-48: "twenty gerahs" - check if present
LOGS.append((3, 'en', 'Badges 6-10->5-10, 27-31->27-32, 44-51->44-48 per MSG units; slang cleaned'))
LOGS.append((3, 'ko', 'NEEDS APPROVAL: split KO para 11 (27-32) into 27-31 + 32 (Eleazar supervision); content prepared but NOT applied'))

# ==================== CHAPTER 4 ====================
TITLES.append((4, 'en', "God's Holy Moving Crew"))
BADGES.append((4, 'en', 3, '7-8'))
F(4, 'en', 0, 'God hit up Moses and Aaron and was like, “Yo, count up', 'God spoke to Moses and Aaron: “Count')
F(4, 'en', 0, 'from the Levite crew, but only the dudes between thirty and fifty', 'from the Levites, men between thirty and fifty')
F(4, 'en', 8, 'But, and this is a big deal, they must not touch', 'They must not touch')
F(4, 'en', 9, 'He’s basically the manager of the whole Dwelling', 'He manages the whole Dwelling')
F(4, 'en', 10, 'get wiped out from the Levite tribe', 'be cut off from the Levites')
F(4, 'en', 10, 'when they get near the super holy stuff', 'when they approach the most holy things')
F(4, 'en', 10, 'assign each guy his specific job', 'assign each man his specific job')
LOGS.append((4, 'en', 'Badge 6-8->7-8 (MSG unit 7-8); slang cleaned'))

# ==================== CHAPTER 5 ====================
TITLES.append((5, 'en', "Purity Laws and the Jealousy Test"))
BADGES.append((5, 'en', 0, '1-3'))
BADGES.append((5, 'en', 6, '23-28'))
BADGES.append((5, 'ko', 5, '22'))
BADGES.append((5, 'ko', 7, '29-31'))
F(5, 'en', 0, 'God hit up Moses and said,', 'God spoke to Moses:')
F(5, 'en', 0, 'kick anyone out of the camp', 'send out of the camp anyone')
F(5, 'en', 0, "Doesn't matter if they're a guy or a girl, send them out.", 'Whether male or female, send them out.')
F(5, 'en', 0, "I'm living in your camp, and I don't want it getting all defiled.", 'I live among you in the camp; do not defile it.')
F(5, 'en', 2, 'messes up and sins, they\'ve basically broken God\'s trust.', 'sins, breaking faith with God.')
F(5, 'en', 3, 'Let\'s say a guy\'s wife cheats on him', 'If a man’s wife goes astray')
F(5, 'en', 3, "he's lowkey convinced his wife is impure", 'he suspects his wife is impure')
F(5, 'en', 3, 'two quarts of barley flour', 'two quarts of barley flour')
F(5, 'en', 4, 'he\'ll un-tie her hair', 'he will loosen her hair')
F(5, 'en', 6, 'cause some serious pain', 'cause pain')
F(5, 'en', 6, 'it will enter her and cause intense pain', 'it will enter her and cause pain')
F(5, 'en', 7, 'or when a husband is just consumed by jealousy and suspects his wife.', 'or when a husband feels jealous and suspects his wife.')
LOGS.append((5, 'en', 'Badges 1-4->1-3, 23-29->23-28 per MSG; KO badges 22, 29-31 aligned; slang cleaned'))

# ==================== CHAPTER 6 ====================
TITLES.append((6, 'en', "The Nazirite Vow"))
BADGES.append((6, 'en', 6, '18'))
BADGES.append((6, 'ko', 0, '1-4'))
F(6, 'en', 0, 'God hit up Moses and was like, "Yo, tell the Israelites,', 'God spoke to Moses: “Tell the Israelites,')
F(6, 'en', 0, 'like a full-on commitment to God, here\'s the deal.', 'as a dedication to God:')
F(6, 'en', 0, 'For real, you can\'t even eat grapes or raisins.', 'You cannot even eat grapes or raisins.')
F(6, 'en', 4, 'if someone just drops dead right next to you', 'if someone dies suddenly beside you')
F(6, 'en', 4, 'You basically have to start over', 'You must start over')
F(6, 'en', 5, 'Okay, so when your special time', 'When your time')
F(6, 'en', 10, 'Then God told Moses, "Tell Aaron and his sons, this is how you should bless', 'God told Moses: “Tell Aaron and his sons: This is how you are to bless')
F(6, 'en', 11, 'May God bless you and keep you safe,', 'May God bless you and keep you,')
F(6, 'en', 11, 'May God\'s face shine on you and be super gracious to you,', 'May God smile on you and be gracious to you,')
F(6, 'en', 11, 'May God look you right in the eye and give you peace.', 'May God look you in the eye and give you peace.')
F(6, 'en', 12, 'By doing this, they will put my name on the people of Israel—and I\'ll make it happen by blessing them."', 'In this way they will put my name on the People of Israel, and I will bless them."')
LOGS.append((6, 'en', 'Badge 13-21 para 6 split: 18 fixed; blessing restored to MSG wording; slang cleaned'))

apply()

print(f"Applied {len(FIXES)} fixes, {len(BADGES)} badge changes, {len(TITLES)} title changes")
if FAILED:
    print(f"FAILED ({len(FAILED)}):")
    for f in FAILED:
        print(" ", f)
else:
    print("All replacements matched.")

json.dump(en, open(f'{REVIEW}/fixes/en_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("Files written.")
