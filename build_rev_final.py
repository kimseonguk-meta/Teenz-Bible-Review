#!/usr/bin/env python3
"""Build en_Revelation.json and ko_Revelation.json — MSG-audited final.
Each chapter: explicit verseRanges + independently extracted msg_ranges.
"""
import json

# (badge, text) per paragraph. '§' headers carry the badge of the following paragraph.
EN = {}
KO = {}
META = {}  # chapter -> {title, msg_ranges, merges, splits, changes, confirmations_needed}

def ch(n, title, paras, msg_ranges, merges=None, splits=None, changes=None, confs=None):
    EN[n] = paras
    META[n] = {
        "title": title,
        "msg_ranges": msg_ranges,
        "merges": merges or [],
        "splits": splits or [],
        "changes": changes or [],
        "confirmations_needed": confs or [],
    }

# ============================== CHAPTER 1 ==============================
ch(1, "The Ultimate Transformation",
[
("4-7", "§His Eyes Pouring Fire-Blaze"),
("1-2", "Alright, so here's the deal. This is the big reveal of Jesus, the Messiah. God gave it to make it crystal clear to his servants what's about to go down. He published it and delivered it by Angel to his servant John. And John told everything he saw: God's Word\u2014the witness of Jesus Christ!"),
("3", "How blessed the reader! How blessed the hearers and keepers of these oracle words, all the words written in this book! Time is just about up."),
("4-7", "What up, it's your boy John, writing to the seven churches out in Asia province. All the best to you from the God Who Is, the God Who Was, and the God About to Arrive, from the Seven Spirits assembled before his throne, and from Jesus Christ\u2014the totally loyal Witness, the Firstborn from the dead, the Ruler of all earthly kings. Glory and strength to Christ, who loves us, who blood-washed our sins from our lives, who made us a Kingdom, Priests for his Father, forever\u2014and yes, he's on his way! Riding the clouds, he'll be seen by every eye, even those who mocked and killed him. People from all nations and all times will tear their clothes in grief. Oh, yes."),
("8", "The Master declares, \u201cI'm A to Z. I'm the God Who Is, the God Who Was, and the God About to Arrive. I'm the Sovereign-Strong.\u201d"),
("9-17", "I, John, with you all the way in the trial and the Kingdom and the passion of patience in Jesus, was on the island called Patmos because of God's Word, the witness of Jesus. It was Sunday and I was in the Spirit, praying. I heard a loud voice behind me, trumpet-clear and piercing: \u201cWrite what you see into a book. Send it to the seven churches: to Ephesus, Smyrna, Pergamum, Thyatira, Sardis, Philadelphia, Laodicea.\u201d I turned and saw the voice. I saw a gold menorah with seven branches, and in the center, the Son of Man, in a robe and gold breastplate, hair a blizzard of white, eyes pouring fire-blaze, both feet furnace-fired bronze, his voice a roar, right hand holding the Seven Stars, his mouth a sharp-biting sword, his face a blinding sun. I saw this and fainted dead at his feet. His right hand pulled me upright, his voice reassured me:"),
("17-20", "\u201cDon't fear: I am First, I am Last, I'm Alive. I died, but I came to life, and my life is now forever. See these keys in my hand? They open and lock Death's doors, they open and lock Hell's gates. Now write down everything you see: things that are, things about to be. The Seven Stars you saw in my right hand and the seven-branched gold menorah\u2014do you want to know what's behind them? The Seven Stars are the Angels of the seven churches; the menorah's seven branches are the seven churches.\u201d"),
],
msg_ranges=["1-2","3","4-7","8","9-17","17-20"],
merges=[
 {"para":3,"msg_ranges":["4-7"],"note":"MSG prints 4-7 as two paragraphs (greeting + doxology); kept as one EN paragraph"},
 {"para":5,"msg_ranges":["9-17"],"note":"MSG prints 9-17 as three paragraphs (Patmos vision, the Son of Man, fainting); kept as one EN paragraph"},
],
splits=[{"msg_range":"17","paras":[5,6],"note":"MSG-native overlap: v17 closes the vision (9-17) and opens the commission (17-20)"}],
changes=[
 "Restored MSG 1 'He published and delivered it by Angel' (was 'sent an angel')",
 "Restored MSG 3 'How blessed the reader! How blessed the hearers and keepers' (was generic 'blessed')",
 "Restored MSG 4-7 doxology 'Glory and strength to Christ, who blood-washed our sins' and 'tear their clothes in grief'",
 "Restored MSG 8 'Sovereign-Strong' (was 'ultimate powerhouse')",
 "Restored MSG 9-17 'trumpet-clear and piercing', 'gold breastplate', 'hair a blizzard of white', 'His voice a roar', 'His mouth a sharp-biting sword'",
 "Restored MSG 17-20 'See these keys in my hand? They open and lock Death's doors, they open and lock Hell's gates'",
 "Replaced invented header with MSG 'His Eyes Pouring Fire-Blaze'",
 "Removed invented 'spilling all the tea'; fixed badges to MSG paragraph ranges",
],
confs=[
 "Ch1 para 3 merges MSG 1:4-7 (two printed paragraphs: greeting + doxology) — confirm one paragraph is OK",
 "Ch1 para 5 merges MSG 1:9-17 (three printed paragraphs) — confirm one paragraph is OK",
],
)

# ============================== CHAPTER 2 ==============================
ch(2, "A Few Pep Talks and a Major Roasting",
[
("1", "\u00a7To Ephesus"),
("1", "Write this to Ephesus, to the Angel of the church. The One with Seven Stars in his right-fist grip, striding through the golden seven-lights' circle, speaks:"),
("2-3", "\u201cI see what you've done\u2014your hard, hard work, your refusal to quit. I know you can't stomach evil, that you weed out apostolic pretenders. I know your persistence, your courage in my cause, that you never wear out."),
("4-5", "\u201cBut you walked away from your first love\u2014why? What's going on with you, anyway? Do you have any idea how far you've fallen? A Lucifer fall! Turn back! Recover your dear early love. No time to waste, for I'm well on my way to removing your light from the golden circle."),
("6", "\u201cYou do have this to your credit: you hate the Nicolaitan business. I hate it, too."),
("7", "\u201cAre your ears awake? Listen. Listen to the Wind Words, the Spirit blowing through the churches. I'm about to call each conqueror to dinner. I'm spreading a banquet of Tree-of-Life fruit, a supper plucked from God's orchard.\u201d"),
("8", "\u00a7To Smyrna"),
("8", "Write this to Smyrna, to the Angel of the church. The Beginning and Ending, the First and Final One, the Once Dead and Then Come Alive, speaks:"),
("9", "\u201cI can see your pain and poverty\u2014constant pain, dire poverty\u2014but I also see your wealth. And I hear the lie in the claims of those who pretend to be good Jews, who in fact belong to Satan's crowd."),
("10", "\u201cFear nothing in the things you're about to suffer\u2014but stay on guard! Fear nothing! The Devil is about to throw you in jail for a time of testing\u2014ten days. It won't last forever. Don't quit, even if it costs you your life. Stay there believing. I have a Life-Crown sized and ready for you."),
("11", "\u201cAre your ears awake? Listen. Listen to the Wind Words, the Spirit blowing through the churches. Christ-conquerors are safe from Devil-death.\u201d"),
("12", "\u00a7To Pergamum"),
("12", "Write this to Pergamum, to the Angel of the church. The One with the sharp-biting sword draws from the sheath of his mouth\u2014out come the sword words:"),
("13", "\u201cI see where you live, right under the shadow of Satan's throne. But you continue boldly in my Name; you never once denied my Name, even when the pressure was worst, when they martyred Antipas, my witness who stayed faithful to me on Satan's turf."),
("14-15", "\u201cBut why do you indulge that Balaam crowd? Don't you remember that Balaam was an enemy agent, seducing Balak and sabotaging Israel's holy pilgrimage by throwing unholy parties? And why do you put up with the Nicolaitans, who do the same thing?"),
("16", "\u201cEnough! Don't give in to them; I'll be with you soon. I'm fed up and about to cut them to pieces with my sword-sharp words."),
("17", "\u201cAre your ears awake? Listen. Listen to the Wind Words, the Spirit blowing through the churches. I'll give the sacred manna to every conqueror; I'll also give a clear, smooth stone inscribed with your new name, your secret new name.\u201d"),
("18", "\u00a7To Thyatira"),
("18", "Write this to Thyatira, to the Angel of the church. God's Son, eyes pouring fire-blaze, standing on feet of furnace-fired bronze, says this:"),
("19", "\u201cI see everything you're doing for me. Impressive! The love and the faith, the service and persistence. Yes, very impressive! You get better at it every day."),
("20-23", "\u201cBut why do you let that Jezebel who calls herself a prophet mislead my dear servants into Cross-denying, self-indulging religion? I gave her a chance to change her ways, but she has no intention of giving up a career in the god-business. I'm about to lay her low, along with her partners, as they play their sex-and-religion games. The children of their idol-cheating I'll kill. Then every church will know that appearances don't impress me. I x-ray every motive and make sure you get what's coming to you."),
("24-25", "\u201cThe rest of you Thyatirans, who have nothing to do with this outrage, who scorn this playing around with the Devil that gets paraded as profundity, be assured I'll not make life any harder for you than it already is. Hold on to the truth you have until I get there."),
("26-28", "\u201cHere's the reward I have for every conqueror, everyone who keeps at it, refusing to give up: You'll rule the nations, your Shepherd-King rule as firm as an iron staff, their resistance fragile as clay pots. This was the gift my Father gave me; I pass it along to you\u2014and with it, the Morning Star!"),
("29", "\u201cAre your ears awake? Listen. Listen to the Wind Words, the Spirit blowing through the churches.\u201d"),
],
msg_ranges=["1","2-3","4-5","6","7","8","9","10","11","12","13","14-15","16","17","18","19","20-23","24-25","26-28","29"],
changes=[
 "Replaced invented headers with MSG 'To Ephesus/Smyrna/Pergamum/Thyatira'",
 "Restored MSG 1 'Seven Stars in his right-fist grip, striding through the golden seven-lights circle'",
 "Restored MSG 4-5 'removing your light from the golden circle' (was 'pull the plug')",
 "Restored MSG 7 'banquet of Tree-of-Life fruit, a supper plucked from God's orchard'",
 "Restored MSG 8 'The Beginning and Ending, the First and Final One, the Once Dead and Then Come Alive'",
 "Restored MSG 10 'stay on guard', 'It won't last forever', 'Stay there believing', 'Life-Crown sized and ready'",
 "Restored MSG 11 'Christ-conquerors are safe from Devil-death'",
 "Restored MSG 12 'draws from the sheath of his mouth—out come the sword words'",
 "Restored MSG 14-15 'enemy agent, seducing Balak and sabotaging Israel's holy pilgrimage by throwing unholy parties'",
 "Restored MSG 16 'cut them to pieces with my sword-sharp words'",
 "Restored MSG 17 'sacred manna', 'clear, smooth stone'",
 "Restored MSG 18 'eyes pouring fire-blaze, standing on feet of furnace-fired bronze'",
 "Restored MSG 20-23 'mislead my dear servants', 'career in the god-business', 'sex-and-religion games', 'bastard offspring of their idol-whoring', 'I x-ray every motive'",
 "Restored MSG 24-25 'scorn this playing around with the Devil that gets paraded as profundity'",
 "Restored MSG 26-28 'Shepherd-King rule as firm as an iron staff, their resistance fragile as clay pots'",
 "Restored 'Are your ears awake? Listen to the Wind Words' refrain in all four letters",
 "Fixed badges to MSG paragraph ranges",
],
)

# ============================== CHAPTER 3 ==============================
ch(3, "God Roasts the Fakers",
[
("1", "\u00a7To Sardis"),
("1", "Write this to Sardis, to the Angel of the church. The One holding the Seven Spirits of God in one hand, a firm grip on the Seven Stars with the other, speaks: \u201cI see right through your work. You have a reputation for vigor and zest, but you're dead, stone-dead."),
("2-3", "\u201cUp on your feet! Take a deep breath! Maybe there's life in you yet. But I wouldn't know it by looking at your busywork; nothing of *God's* work has been completed. Your condition is desperate. Think of the gift you once had in your hands, the Message you heard with your ears\u2014grasp it again and turn back to God. If you pull the covers back over your head and sleep on, oblivious to God, I'll return when you least expect it, break into your life like a thief in the night."),
("4", "\u201cYou still have a few followers of Jesus in Sardis who haven't ruined themselves wallowing in the muck of the world's ways. They'll walk with me on parade! They've proved their worth!"),
("5", "\u201cConquerors will march in the victory parade, their names indelible in the Book of Life. I'll lead them up and present them by name to my Father and his Angels."),
("6", "\u201cAre your ears awake? Listen. Listen to the Wind Words, the Spirit blowing through the churches.\u201d"),
("7", "\u00a7To Philadelphia"),
("7", "Write this to Philadelphia, to the Angel of the church. The Holy, the True\u2014David's key in his hand, opening doors no one can lock, locking doors no one can open\u2014speaks:"),
("8", "\u201cI see what you've done. Now see what *I've* done. I've opened a door before you that no one can slam shut. You don't have much strength, I know that; you used what you had to keep my Word. You didn't deny me when times were rough."),
("9", "\u201cAnd watch as I take those who call themselves true believers but are nothing of the kind, pretenders whose true membership is in the club of Satan\u2014watch as I strip off their pretensions and they're forced to acknowledge it's you that I've loved."),
("10", "\u201cBecause you kept my Word in passionate patience, I'll keep you safe in the time of testing that will be here soon, and all over the earth, every man, woman, and child put to the test."),
("11", "\u201cI'm on my way; I'll be there soon. Keep a tight grip on what you have so no one distracts you and steals your crown."),
("12", "\u201cI'll make each conqueror a pillar in the sanctuary of my God, a permanent position of honor. Then I'll write names on you, the pillars: the Name of my God, the Name of God's City\u2014the new Jerusalem coming down out of Heaven\u2014and my new Name."),
("13", "\u201cAre your ears awake? Listen. Listen to the Wind Words, the Spirit blowing through the churches.\u201d"),
("14", "\u00a7To Laodicea"),
("14", "Write to Laodicea, to the Angel of the church. God's Yes, the Faithful and Accurate Witness, the First of God's creation, says:"),
("15-17", "\u201cI know you inside and out, and find little to my liking. You're not cold, you're not hot\u2014far better to be either cold or hot! You're stale. You're stagnant. You make me want to vomit. You brag, 'I'm rich, I've got it made, I need nothing from anyone,' oblivious that in fact you're a pitiful, blind beggar, threadbare and homeless."),
("18", "\u201cHere's what I want you to do: Buy your gold from me, gold that's been through the refiner's fire. Then you'll be rich. Buy your clothes from me, clothes designed in Heaven. You've gone around half-naked long enough. And buy medicine for your eyes from me so you can see, *really* see."),
("19", "\u201cThe people I love, I call to account\u2014prod and correct and guide so that they'll live at their best. Up on your feet, then! About face! Run after God!"),
("20-21", "\u201cLook at me. I stand at the door. I knock. If you hear me call and open the door, I'll come right in and sit down to supper with you. Conquerors will sit alongside me at the head table, just as I, having conquered, took the place of honor at the side of my Father. That's my gift to the conquerors!"),
("22", "\u201cAre your ears awake? Listen. Listen to the Wind Words, the Spirit blowing through the churches.\u201d"),
],
msg_ranges=["1","2-3","4","5","6","7","8","9","10","11","12","13","14","15-17","18","19","20-21","22"],
changes=[
 "Replaced invented/generic headers with MSG 'To Sardis/Philadelphia/Laodicea'; removed null-badge headers",
 "Restored MSG 1 'The One holding the Seven Spirits of God in one hand, a firm grip on the Seven Stars with the other'",
 "Restored MSG 2-3 'nothing of *God's* work has been completed', 'break into your life like a thief in the night'",
 "Restored MSG 4 'followers of Jesus in Sardis who haven't ruined themselves wallowing in the muck of the world's ways'",
 "Restored MSG 5 'their names indelible in the Book of Life'",
 "Restored MSG 7 'The Holy, the True\u2014David's key in his hand, opening doors no one can lock, locking doors no one can open'",
 "Restored MSG 8 'Now see what *I've* done'",
 "Restored MSG 9 'pretenders whose true membership is in the club of Satan', 'forced to acknowledge it's you that I've loved'",
 "Restored MSG 10 'kept my Word in passionate patience', 'every man, woman, and child put to the test'",
 "Restored MSG 11 'Keep a tight grip on what you have so no one distracts you and steals your crown'",
 "Restored MSG 12 'a pillar in the sanctuary of my God, a permanent position of honor', 'the Name of God's City\u2014the new Jerusalem coming down out of Heaven'",
 "Restored MSG 14 'God's Yes, the Faithful and Accurate Witness, the First of God's creation'",
 "Restored MSG 15-17 'You're stale. You're stagnant. You make me want to vomit', 'pitiful, blind beggar, threadbare and homeless'",
 "Restored MSG 18 'gold that's been through the refiner's fire', 'clothes designed in Heaven', 'so you can see, *really* see'",
 "Restored MSG 19 'The people I love, I call to account\u2014prod and correct and guide'",
 "Restored MSG 20-21 'I'll come right in and sit down to supper with you', 'took the place of honor at the side of my Father'",
 "Restored 'Are your ears awake?' refrain in all three letters",
 "Fixed badges to MSG paragraph ranges",
],
)

# ============================== CHAPTER 4 ==============================
ch(4, "The Ultimate Sneak Peek",
[
("1", "\u00a7A Door into Heaven"),
("1", "Then I looked, and, oh!\u2014a door open into Heaven. The trumpet-voice, the first voice in my vision, called out, \u201cAscend and enter. I'll show you what happens next.\u201d"),
("2-6", "I was caught up at once in deep worship and, oh!\u2014a Throne set in Heaven with One Seated on the Throne, suffused in gem hues of amber and flame with a nimbus of emerald. Twenty-four thrones circled the Throne, with Twenty-four Elders seated, white-robed, gold-crowned. Lightning flash and thunder crash pulsed from the Throne. Seven fire-blazing torches fronted the Throne (these are the Sevenfold Spirit of God). Before the Throne it was like a clear crystal sea."),
("6-8", "Prowling around the Throne were Four Animals, all eyes. Eyes to look ahead, eyes to look behind. The first Animal like a lion, the second like an ox, the third with a human face, the fourth like an eagle in flight. The Four Animals were winged, each with six wings. They were all eyes, seeing around and within. And they chanted night and day, never taking a break: Holy, holy, holy Is God our Master, Sovereign-Strong, The Was, The Is, The Coming."),
("9-11", "Every time the Animals gave glory and honor and thanks to the One Seated on the Throne\u2014the age-after-age Living One\u2014the Twenty-four Elders would fall prostrate before the One Seated on the Throne. They worshiped the age-after-age Living One. They threw their crowns at the foot of the Throne, chanting, Worthy, O Master! Yes, our God! Take the glory! the honor! the power! You created it all; It was created because you wanted it."),
],
msg_ranges=["1","2-6","6-8","9-11"],
splits=[{"msg_range":"6","paras":[1,2],"note":"MSG-native overlap: v6 closes the throne vision (2-6) and opens the Four Animals (6-8)"}],
changes=[
 "Replaced invented header with MSG 'A Door into Heaven'",
 "Restored MSG 1 'The trumpet-voice, the first voice in my vision, called out, Ascend and enter'",
 "Restored MSG 2-6 'suffused in gem hues of amber and flame with a nimbus of emerald', 'Seven fire-blazing torches (these are the Sevenfold Spirit of God)'",
 "Restored MSG 6-8 'Prowling around the Throne were Four Animals, all eyes. Eyes to look ahead, eyes to look behind', 'They were all eyes, seeing around and within'",
 "Restored MSG 6-8 chant 'Holy, holy, holy Is God our Master, Sovereign-Strong, The Was, The Is, The Coming'",
 "Restored MSG 9-11 'the age-after-age Living One', 'They threw their crowns at the foot of the Throne'",
 "Restored MSG 9-11 chant 'Worthy, O Master! Yes, our God! Take the glory! the honor! the power! You created it all; It was created because you wanted it'",
 "Fixed badges to MSG ranges 2-6, 6-8 (was 2-4, 6-7, 8)",
],
)

# ============================== CHAPTER 5 ==============================
ch(5, "The Ultimate Unboxing",
[
("1-2", "\u00a7The Lion Is a Lamb"),
("1-2", "I saw a scroll in the right hand of the One Seated on the Throne. It was written on both sides, fastened with seven seals. I also saw a powerful Angel, calling out in a voice like thunder, \u201cIs there anyone who can open the scroll, who can break its seals?\u201d"),
("3", "There was no one\u2014no one in Heaven, no one on earth, no one from the underworld\u2014able to break open the scroll and read it."),
("4-5", "I wept and wept and wept that no one was found able to open the scroll, able to read it. One of the Elders said, \u201cDon't weep. Look\u2014the Lion from Tribe Judah, the Root of David's Tree, has conquered. He can open the scroll, can rip through the seven seals.\u201d"),
("6-10", "So I looked, and there, surrounded by Throne, Animals, and Elders, was a Lamb, slaughtered but standing tall. Seven horns he had, and seven eyes, the Seven Spirits of God sent into all the earth. He came to the One Seated on the Throne and took the scroll from his right hand. The moment he took the scroll, the Four Animals and Twenty-four Elders fell down and worshiped the Lamb. Each had a harp and each had a bowl, a gold bowl filled with incense, the prayers of God's holy people. And they sang a new song: Worthy! Take the scroll, open its seals. Slain! Paying in blood, you bought men and women, bought them back from all over the earth, bought them back for God. Then you made them a Kingdom, Priests for our God, Priest-kings to rule over the earth."),
("11-14", "I looked again. I heard a company of Angels around the Throne, the Animals, and the Elders\u2014ten thousand times ten thousand their number, thousand after thousand after thousand in full song: The slain Lamb is worthy! Take the power, the wealth, the wisdom, the strength! Take the honor, the glory, the blessing! Then I heard every creature in Heaven and earth, in underworld and sea, join in, all voices in all places, singing: To the One on the Throne! To the Lamb! The blessing, the honor, the glory, the strength, for age after age after age. The Four Animals called out, \u201cOh, Yes!\u201d The Elders fell to their knees and worshiped."),
],
msg_ranges=["1-2","3","4-5","6-10","11-14"],
merges=[
 {"para":3,"msg_ranges":["6-10"],"note":"MSG prints 6-10 as two paragraphs (Lamb takes scroll + new song); kept as one EN paragraph"},
 {"para":4,"msg_ranges":["11-14"],"note":"MSG prints 11-14 as three paragraphs (angels' song, every creature, Amen); kept as one EN paragraph"},
],
changes=[
 "Replaced invented header with MSG 'The Lion Is a Lamb'",
 "Restored MSG 1-2 'It was written on both sides' (was omitted)",
 "Restored MSG 4-5 'the Lion from Tribe Judah, the Root of David's Tree, has conquered. He can open the scroll, can rip through the seven seals'",
 "Restored MSG 6-10 'a Lamb, slaughtered but standing tall', 'the Seven Spirits of God sent into all the earth', 'the prayers of God's holy people'",
 "Restored MSG 6-10 song 'Slain! Paying in blood, you bought men and women', 'Priest-kings to rule over the earth'",
 "Restored MSG 11-14 'ten thousand times ten thousand', 'every creature in Heaven and earth, in underworld and sea', 'for age after age after age'",
 "Removed invented 'super-exclusive drop', 'taken out'; fixed badges to MSG ranges",
],
confs=[
 "Ch5 para 3 merges MSG 5:6-10 (two printed paragraphs) \u2014 confirm one paragraph is OK",
 "Ch5 para 4 merges MSG 5:11-14 (three printed paragraphs) \u2014 confirm one paragraph is OK",
],
)

# ============================== CHAPTER 6 ==============================
ch(6, "The Apocalypse Horsemen Drop In",
[
("1-2", "\u00a7Unsealing the Scroll"),
("1-2", "I watched while the Lamb ripped off the first of the seven seals. I heard one of the Animals roar, \u201cCome out!\u201d I looked\u2014I saw a white horse. Its rider carried a bow and was given a victory garland. He rode off victorious, conquering right and left."),
("3-4", "When the Lamb ripped off the second seal, I heard the second Animal cry, \u201cCome out!\u201d Another horse appeared, this one red. Its rider was off to take peace from the earth, setting people at each other's throats, killing one another. He was given a huge sword."),
("5-6", "When he ripped off the third seal, I heard the third Animal cry, \u201cCome out!\u201d I looked. A black horse this time. Its rider carried a set of scales in his hand. I heard a message (it seemed to issue from the Four Animals): \u201cA quart of wheat for a day's wages, or three quarts of barley, but don't lay even a finger on the oil and wine.\u201d"),
("7-8", "When he ripped off the fourth seal, I heard the fourth Animal cry, \u201cCome out!\u201d I looked. A colorless horse, sickly pale. Its rider was Death, and Hell was close on its heels. They were given power to destroy a fourth of the earth by war, famine, disease, and wild beasts."),
("9-11", "When he ripped off the fifth seal, I saw the souls of those killed because they had held firm in their witness to the Word of God. They were gathered under the Altar, and cried out in loud prayers, \u201cHow long, Strong God, Holy and True? How long before you step in and avenge our murders?\u201d Then each martyr was given a white robe and told to sit back and wait until the full number of martyrs was filled from among their servant companions and friends in the faith."),
("12-17", "I watched while he ripped off the sixth seal: a bone-jarring earthquake, sun turned black as ink, moon all bloody, stars falling out of the sky like figs shaken from a tree in a high wind, sky snapped shut like a book, islands and mountains sliding this way and that. And then pandemonium, everyone and his dog running for cover\u2014kings, princes, generals, rich and strong, along with every commoner, slave or free. They hid in mountain caves and rocky dens, calling out to mountains and rocks, \u201cRefuge! Hide us from the One Seated on the Throne and the wrath of the Lamb! The great Day of their wrath has come\u2014who can stand it?\u201d"),
],
msg_ranges=["1-2","3-4","5-6","7-8","9-11","12-17"],
changes=[
 "Replaced invented header with MSG 'Unsealing the Scroll'",
 "Restored MSG 1-2 'was given a victory garland. He rode off victorious, conquering right and left'",
 "Restored MSG 3-4 'setting people at each other's throats, killing one another. He was given a huge sword'",
 "Restored MSG 5-6 'A quart of wheat for a day's wages, or three quarts of barley, but don't lay even a finger on the oil and wine'",
 "Restored MSG 7-8 'A colorless horse, sickly pale', 'Hell was close on its heels', 'destroy a fourth of the earth by war, famine, disease, and wild beasts'",
 "Restored MSG 9-11 'How long, Strong God, Holy and True?', 'until the full number of martyrs was filled from among their servant companions and friends in the faith'",
 "Restored MSG 12-17 'a bone-jarring earthquake, sun turned black as ink', 'sky snapped shut like a book', 'everyone and his dog running for cover', 'Refuge! Hide us from the One Seated on the Throne and the wrath of the Lamb!'",
 "Fixed badges to MSG ranges",
],
)

# ============================== CHAPTER 7 ==============================
ch(7, "The Honored List",
[
("1", "\u00a7The Servants of God"),
("1", "Immediately I saw Four Angels standing at the four corners of earth, standing steady with a firm grip on the four winds so no wind would blow on earth or sea, not even rustle a tree."),
("2-3", "Then I saw another Angel rising from where the sun rose, carrying the seal of the Living God. He thundered to the Four Angels assigned the task of hurting earth and sea, \u201cDon't hurt the earth! Don't hurt the sea! Don't so much as hurt a tree until I've sealed the servants of our God on their foreheads!\u201d"),
("4-8", "I heard the count of those who were sealed: 144,000! They were sealed out of every Tribe of Israel: 12,000 sealed from Judah, 12,000 from Reuben, 12,000 from Gad, 12,000 from Asher, 12,000 from Naphtali, 12,000 from Manasseh, 12,000 from Simeon, 12,000 from Levi, 12,000 from Issachar, 12,000 from Zebulun, 12,000 from Joseph, 12,000 sealed from Benjamin."),
("9-12", "I looked again. I saw a huge crowd, too huge to count. Everyone was there\u2014all nations and tribes, all races and languages. And they were *standing*, dressed in white robes and waving palm branches, standing before the Throne and the Lamb and heartily singing: Salvation to our God on his Throne! Salvation to the Lamb! All who were standing around the Throne\u2014Angels, Elders, Animals\u2014fell on their faces before the Throne and worshiped God, singing: Oh, Yes! The blessing and glory and wisdom and thanksgiving, the honor and power and strength, to our God forever and ever and ever! Oh, Yes!"),
("13-14", "Just then one of the Elders addressed me: \u201cWho are these dressed in white robes, and where did they come from?\u201d Taken aback, I said, \u201cO Sir, I have no idea\u2014but you must know.\u201d"),
("14-17", "Then he told me, \u201cThese are those who come from the great tribulation, and they've washed their robes, scrubbed them clean in the blood of the Lamb. That's why they're standing before God's Throne. They serve him day and night in his Temple. The One on the Throne will pitch his tent there for them: no more hunger, no more thirst, no more scorching heat. The Lamb on the Throne will shepherd them, will lead them to spring waters of Life. And God will wipe every last tear from their eyes.\u201d"),
],
msg_ranges=["1","2-3","4-8","9-12","13-14","14-17"],
merges=[
 {"para":3,"msg_ranges":["9-12"],"note":"MSG prints 9-12 as two paragraphs (crowd's song + angels' worship); kept as one EN paragraph"},
],
splits=[{"msg_range":"14","paras":[4,5],"note":"MSG-native overlap: v14 closes the elder's question (13-14) and opens the answer (14-17)"}],
changes=[
 "Replaced invented header with MSG 'The Servants of God'",
 "Restored MSG 1 'standing steady with a firm grip on the four winds', 'not even rustle a tree'",
 "Restored MSG 2-3 'rising from where the sun rose', 'He thundered', 'Don't so much as hurt a tree'",
 "Restored MSG 9-12 'too huge to count', 'Salvation to our God on his Throne! Salvation to the Lamb!', 'Oh, Yes! The blessing and glory and wisdom and thanksgiving'",
 "Restored MSG 13-14 'Taken aback, I said, O Sir, I have no idea\u2014but you must know'",
 "Restored MSG 14-17 'come from the great tribulation', 'washed their robes, scrubbed them clean in the blood of the Lamb', 'The One on the Throne will pitch his tent there for them', 'The Lamb on the Throne will shepherd them, will lead them to spring waters of Life', 'wipe every last tear from their eyes'",
 "Fixed EN para 1 badge 1-3 to 1 (was duplicating 2-3); fixed badges to MSG ranges",
],
confs=[
 "Ch7 para 3 merges MSG 7:9-12 (two printed paragraphs) \u2014 confirm one paragraph is OK",
],
)

# ============================== CHAPTER 8 ==============================
ch(8, "The Trumpet Squad Brings the Pain",
[
("1", "When the Lamb ripped off the seventh seal, Heaven fell quiet\u2014complete silence for about half an hour."),
("2-4", "\u00a7Blowing the Trumpets"),
("2-4", "I saw the Seven Angels who are always in readiness before God handed seven trumpets. Then another Angel, carrying a gold censer, came and stood at the Altar. He was given a great quantity of incense so that he could offer up the prayers of all the holy people of God on the Golden Altar before the Throne. Smoke billowed up from the incense-laced prayers of the holy ones, rose before God from the hand of the Angel."),
("5", "Then the Angel filled the censer with fire from the Altar and heaved it to earth. It set off thunders, voices, lightnings, and an earthquake."),
("6-7", "The Seven Angels with the trumpets got ready to blow them. At the first trumpet blast, hail and fire mixed with blood were dumped on earth. A third of the earth was scorched, a third of the trees, and every blade of green grass\u2014burned to a crisp."),
("8-9", "The second Angel trumpeted. Something like a huge mountain blazing with fire was flung into the sea. A third of the sea turned to blood, a third of the living sea creatures died, and a third of the ships sank."),
("10-11", "The third Angel trumpeted. A huge Star, blazing like a torch, fell from Heaven, wiping out a third of the rivers and a third of the springs. The Star's name was Wormwood. A third of the water turned bitter, and many people died from the poisoned water."),
("12", "The fourth Angel trumpeted. A third of the sun, a third of the moon, and a third of the stars were hit, blacked out by a third, both day and night in one-third blackout."),
("13", "I looked hard; I heard a lone eagle, flying through Middle-Heaven, crying out ominously, \u201cDoom! Doom! Doom to everyone left on earth! There are three more Angels about to blow their trumpets. Doom is on its way!\u201d"),
],
msg_ranges=["1","2-4","5","6-7","8-9","10-11","12","13"],
changes=[
 "Replaced invented header with MSG 'Blowing the Trumpets' (badge 2-4)",
 "Restored MSG 1 'Heaven fell quiet\u2014complete silence for about half an hour' (was 'you could hear a pin drop')",
 "Restored MSG 2-4 'who are always in readiness before God', 'a gold censer', 'the prayers of all the holy people of God', 'Smoke billowed up from the incense-laced prayers'",
 "Restored MSG 5 'filled the censer with fire from the Altar and heaved it to earth. It set off thunders, voices, lightnings, and an earthquake'",
 "Restored MSG 6-7 'hail and fire mixed with blood were dumped on earth', 'every blade of green grass\u2014burned to a crisp'",
 "Restored MSG 8-9 'Something like a huge mountain blazing with fire was flung into the sea', 'a third of the living sea creatures died'",
 "Restored MSG 10-11 'wiping out a third of the rivers and a third of the springs', 'A third of the water turned bitter'",
 "Restored MSG 12 'blacked out by a third, both day and night in one-third blackout'",
 "Restored MSG 13 'a lone eagle, flying through Middle-Heaven, crying out ominously', 'Doom to everyone left on earth!'",
 "Removed invented 'super-powered DM', 'Major L'; fixed badges to MSG ranges",
],
)

# ============================== CHAPTER 9 ==============================
ch(9, "The Monster Apocalypse Gets Real",
[
("1-2", "The fifth Angel trumpeted. I saw a Star plummet from Heaven to earth. The Star was handed a key to the Well of the Abyss. He unlocked the Well of the Abyss\u2014smoke poured out of the Well, billows and billows of smoke, sun and air in blackout from smoke pouring out of the Well."),
("3-6", "Then out of the smoke crawled locusts with the venom of scorpions. They were given their orders: \u201cDon't hurt the grass, don't hurt anything green, don't hurt a single tree\u2014only men and women, and then only those who lack the seal of God on their foreheads.\u201d They were ordered to torture but not kill, torture them for five months, the pain like a scorpion sting. When this happens, people are going to prefer death to torture, look for ways to kill themselves. But they won't find a way\u2014death will have gone into hiding."),
("7-11", "The locusts looked like horses ready for war. They had gold crowns, human faces, women's hair, the teeth of lions, and iron breastplates. The sound of their wings was the sound of horse-drawn chariots charging into battle. Their tails were equipped with stings, like scorpion tails. With those tails they were ordered to torture the human race for five months. They had a king over them, the Angel of the Abyss. His name in Hebrew is *Abaddon*, in Greek, *Apollyon*\u2014\u201cDestroyer.\u201d"),
("12", "The first doom is past. Two dooms yet to come."),
("13-14", "The sixth Angel trumpeted. I heard a voice speaking to the sixth Angel from the horns of the Golden Altar before God: \u201cLet the Four Angels loose, the Angels confined at the great River Euphrates.\u201d"),
("15-19", "The Four Angels were untied and let loose, Four Angels all prepared for the exact year, month, day, and even hour when they were to kill a third of the human race. The number of the army of horsemen was twice ten thousand times ten thousand. I heard the count and saw both horses and riders in my vision: fiery breastplates on the riders, lion heads on the horses breathing out fire and smoke and brimstone. With these three weapons\u2014fire and smoke and brimstone\u2014they killed a third of the human race. The horses killed with their mouths and tails; their serpentlike tails also had heads that wreaked havoc."),
("20-21", "The remaining men and women who weren't killed by these weapons went on their merry way\u2014didn't change their way of life, didn't quit worshiping demons, didn't quit centering their lives around lumps of gold and silver and brass, hunks of stone and wood that couldn't see or hear or move. There wasn't a sign of a change of heart. They plunged right on in their murderous, occult, promiscuous, and thieving ways."),
],
msg_ranges=["1-2","3-6","7-11","12","13-14","15-19","20-21"],
changes=[
 "Removed invented header 'The Fifth and Sixth Trumpets' (MSG has no header here)",
 "Restored MSG 1-2 'The Star was handed a key to the Well of the Abyss', 'billows and billows of smoke, sun and air in blackout'",
 "Restored MSG 3-6 'locusts with the venom of scorpions', 'only those who lack the seal of God on their foreheads', 'death will have gone into hiding'",
 "Restored MSG 7-11 'gold crowns, human faces, women's hair, the teeth of lions, and iron breastplates', 'His name in Hebrew is *Abaddon*, in Greek, *Apollyon*\u2014Destroyer'",
 "Restored MSG 12 'The first doom is past. Two dooms yet to come' (was 'first round of awfulness')",
 "Restored MSG 13-14 'from the horns of the Golden Altar', 'the Angels confined at the great River Euphrates'",
 "Restored MSG 15-19 'prepared for the exact year, month, day, and even hour', 'twice ten thousand times ten thousand', 'their serpentlike tails also had heads that wreaked havoc'",
 "Restored MSG 20-21 'went on their merry way', 'lumps of gold and silver and brass, hunks of stone and wood that couldn't see or hear or move', 'murderous, occult, promiscuous, and thieving ways'",
 "Fixed badges to MSG ranges",
],
)

# ============================== CHAPTER 10 ==============================
ch(10, "The Angel and the Snack-Sized Scroll",
[
("1-4", "I saw another powerful Angel coming down out of Heaven wrapped in a cloud. There was a rainbow over his head, his face was sun-radiant, his legs pillars of fire. He had a small book open in his hand. He placed his right foot on the sea and his left foot on land, then called out thunderously, a lion roar. When he called out, the Seven Thunders called back. When the Seven Thunders spoke, I started to write it all down, but a voice out of Heaven stopped me, saying, \u201cSeal with silence the Seven Thunders; don't write a word.\u201d"),
("5-7", "Then the Angel I saw astride sea and land lifted his right hand to Heaven and swore by the One Living Forever and Ever, who created Heaven and everything in it, earth and everything in it, sea and everything in it, that time was up\u2014that when the seventh Angel blew his trumpet, which he was about to do, the Mystery of God, all the plans he had revealed to his servants, the prophets, would be completed."),
("8-11", "The voice out of Heaven spoke to me again: \u201cGo, take the book held open in the hand of the Angel astride sea and earth.\u201d I went up to the Angel and said, \u201cGive me the little book.\u201d He said, \u201cTake it, then eat it. It will taste sweet like honey, but turn sour in your stomach.\u201d I took the little book from the Angel's hand and it was sweet honey in my mouth, but when I swallowed, my stomach curdled. Then I was told, \u201cYou must go back and prophesy again over many peoples and nations and languages and kings.\u201d"),
],
msg_ranges=["1-4","5-7","8-11"],
changes=[
 "Replaced invented header with MSG 'The Little Book' (was already correct; kept)",
 "Restored MSG 1-4 'wrapped in a cloud', 'a rainbow over his head', 'his face was sun-radiant, his legs pillars of fire', 'He had a small book open in his hand', 'Seal with silence the Seven Thunders; don't write a word'",
 "Restored MSG 5-7 'astride sea and land', 'swore by the One Living Forever and Ever', 'the Mystery of God, all the plans he had revealed to his servants, the prophets, would be completed'",
 "Restored MSG 8-11 'the book held open in the hand of the Angel astride sea and earth', 'It will taste sweet like honey, but turn sour in your stomach', 'my stomach curdled', 'prophesy again over many peoples and nations and languages and kings'",
 "Removed invented 'jacked angel', 'crazy sound system'; fixed badges to MSG ranges",
],
)

# ============================== CHAPTER 11 ==============================
ch(11, "God's Two-Man Temple Guards vs. The Beast",
[
("1-2", "\u00a7The Two Witnesses"),
("1-2", "I was given a stick for a measuring rod and told, \u201cGet up and measure God's Temple and Altar and everyone worshiping in it. Exclude the outside court; don't measure it. It's been handed over to non-Jewish outsiders. They'll desecrate the Holy City for forty-two months."),
("3-6", "\u201cMeanwhile, I'll provide my two Witnesses. Dressed in sackcloth, they'll prophesy for 1,260 days. These are the two Olive Trees, the two Lampstands, standing at attention before God on earth. If anyone tries to hurt them, a blast of fire from their mouths will incinerate them\u2014burn them to a crisp just like that. They'll have power to seal the sky so that it doesn't rain for the time of their prophesying, power to turn rivers and springs to blood, power to hit earth with any and every disaster as often as they want."),
("7-10", "\u201cWhen they've completed their witness, the Beast from the Abyss will emerge and fight them, conquer and kill them, leaving their corpses exposed on the street of the Great City spiritually called Sodom and Egypt, the same City where their Master was crucified. For three and a half days they'll be there\u2014exposed, prevented from getting a decent burial, stared at by the curious from all over the world. Those people will cheer at the spectacle, shouting 'Good riddance!' and calling for a celebration, for these two prophets pricked the conscience of all the people on earth, made it impossible for them to enjoy their sins."),
("11", "\u201cThen, after three and a half days, the Living Spirit of God will enter them\u2014they're on their feet!\u2014and all those gloating spectators will be scared to death.\u201d"),
("12-13", "I heard a strong voice out of Heaven calling, \u201cCome up here!\u201d and up they went to Heaven, wrapped in a cloud, their enemies watching it all. At that moment there was a gigantic earthquake\u2014a tenth of the city fell to ruin, seven thousand perished in the earthquake, the rest frightened to the core of their being, frightened into giving honor to the God-of-Heaven."),
("14", "The second doom is past, the third doom coming right on its heels."),
("15-18", "\u00a7The Last Trumpet Sounds"),
("15-18", "The seventh Angel trumpeted. A crescendo of voices in Heaven sang out, The kingdom of the world is now the Kingdom of our God and his Messiah! He will rule forever and ever! The Twenty-four Elders seated before God on their thrones fell to their knees, worshiped, and sang, We thank you, O God, Sovereign-Strong, Who Is and Who Was. You took your great power and took over\u2014reigned! The angry nations now get a taste of *your* anger. The time has come to judge the dead, to reward your servants, all prophets and saints, Reward small and great who fear your Name, and destroy the destroyers of earth."),
("19", "The doors of God's Temple in Heaven flew open, and the Ark of his Covenant was clearly seen surrounded by flashes of lightning, loud shouts, peals of thunder, an earthquake, and a fierce hailstorm."),
],
msg_ranges=["1-2","3-6","7-10","11","12-13","14","15-18","19"],
merges=[
 {"para":7,"msg_ranges":["15-18"],"note":"MSG prints 15-18 as two paragraphs (heaven's crescendo + elders' song); kept as one EN paragraph"},
],
changes=[
 "Replaced invented header with MSG 'The Two Witnesses' and 'The Last Trumpet Sounds'",
 "Restored MSG 1-2 'I was given a stick for a measuring rod', 'Exclude the outside court', 'handed over to non-Jewish outsiders', 'desecrate the Holy City for forty-two months'",
 "Restored MSG 3-6 'Dressed in sackcloth', 'standing at attention before God on earth', 'a blast of fire from their mouths will incinerate them\u2014burn them to a crisp just like that', 'power to seal the sky', 'power to turn rivers and springs to blood'",
 "Restored MSG 7-10 'spiritually called Sodom and Egypt' (was omitted), 'prevented from getting a decent burial, stared at by the curious from all over the world', 'shouting Good riddance!', 'pricked the conscience of all the people on earth, made it impossible for them to enjoy their sins'",
 "Restored MSG 11 'the Living Spirit of God will enter them\u2014they're on their feet!\u2014and all those gloating spectators will be scared to death'",
 "Restored MSG 12-13 'wrapped in a cloud, their enemies watching it all', 'a tenth of the city fell to ruin, seven thousand perished', 'frightened into giving honor to the God-of-Heaven'",
 "Restored MSG 14 'The second doom is past, the third doom coming right on its heels'",
 "Restored MSG 15-18 'A crescendo of voices', 'Sovereign-Strong, Who Is and Who Was', 'The angry nations now get a taste of *your* anger', 'Reward small and great who fear your Name, and destroy the destroyers of earth'",
 "Restored MSG 19 'The doors of God's Temple in Heaven flew open, and the Ark of his Covenant was clearly seen surrounded by flashes of lightning, loud shouts, peals of thunder, an earthquake, and a fierce hailstorm'",
 "Fixed badges to MSG ranges",
],
confs=[
 "Ch11 para 7 merges MSG 11:15-18 (two printed paragraphs) \u2014 confirm one paragraph is OK",
],
)

# ============================== CHAPTER 12 ==============================
ch(12, "The Cosmic Throwdown: Dragon vs. a Super Mom",
[
("1-2", "\u00a7The Woman, Her Son, and the Dragon"),
("1-2", "A great Sign appeared in Heaven: a Woman dressed all in sunlight, standing on the moon, and crowned with Twelve Stars. She was giving birth to a Child and cried out in the pain of childbirth."),
("3-4", "And then another Sign alongside the first: a huge and fiery Dragon! It had seven heads and ten horns, a crown on each of the seven heads. With one flick of its tail it knocked a third of the Stars from the sky and dumped them on earth. The Dragon crouched before the Woman in childbirth, poised to eat up the Child when it came."),
("5-6", "The Woman gave birth to a Son who will shepherd all nations with an iron rod. Her Son was seized and placed safely before God on his Throne. The Woman herself escaped to the desert to a place of safety prepared by God, all comforts provided her for 1,260 days."),
("7-12", "War broke out in Heaven. Michael and his Angels fought the Dragon. The Dragon and his Angels fought back, but were no match for Michael. They were cleared out of Heaven, not a sign of them left. The great Dragon\u2014ancient Serpent, the one called Devil and Satan, the one who led the whole earth astray\u2014thrown out, and all his Angels thrown out with him, thrown down to earth. Then I heard a strong voice out of Heaven saying, Salvation and power are established! Kingdom of our God, authority of his Messiah! The Accuser of our brothers and sisters thrown out, who accused them day and night before God. They defeated him through the blood of the Lamb and the bold word of their witness. They weren't in love with themselves; they were willing to die for Christ. So rejoice, O Heavens, and all who live there, but doom to earth and sea, For the Devil's come down on you with both feet; he's had a great fall; He's wild and raging with anger; he hasn't much time and he knows it."),
("13-17", "When the Dragon saw he'd been thrown to earth, he went after the Woman who had given birth to the Man-Child. The Woman was given wings of a great eagle to fly to a place in the desert to be kept in safety and comfort for a time and times and half a time, safe and sound from the Serpent. The Serpent vomited a river of water to swamp and drown her, but earth came to her help, swallowing the water the Dragon spewed from its mouth. Helpless with rage, the Dragon raged at the Woman, then went off to make war with the rest of her children, the children who keep God's commands and hold firm to the witness of Jesus."),
],
msg_ranges=["1-2","3-4","5-6","7-12","13-17"],
merges=[
 {"para":3,"msg_ranges":["7-12"],"note":"MSG prints 7-12 as two paragraphs (war in heaven + victory song); kept as one EN paragraph"},
],
changes=[
 "Replaced invented header with MSG 'The Woman, Her Son, and the Dragon'",
 "Restored MSG 1-2 'A great Sign appeared in Heaven', 'dressed all in sunlight', 'crowned with Twelve Stars', 'cried out in the pain of childbirth'",
 "Restored MSG 3-4 'another Sign alongside the first', 'a crown on each of the seven heads', 'With one flick of its tail it knocked a third of the Stars from the sky and dumped them on earth', 'poised to eat up the Child when it came'",
 "Restored MSG 5-6 'who will shepherd all nations with an iron rod', 'Her Son was seized and placed safely before God on his Throne', 'all comforts provided her for 1,260 days'",
 "Restored MSG 7-12 'They were cleared out of Heaven, not a sign of them left', 'the one who led the whole earth astray', 'The Accuser of our brothers and sisters thrown out, who accused them day and night before God', 'They defeated him through the blood of the Lamb and the bold word of their witness. They weren't in love with themselves; they were willing to die for Christ', 'doom to earth and sea, For the Devil's come down on you with both feet; he's had a great fall'",
 "Restored MSG 13-17 'who had given birth to the Man-Child', 'wings of a great eagle', 'for a time and times and half a time', 'The Serpent vomited a river of water to swamp and drown her', 'Helpless with rage', 'the children who keep God's commands and hold firm to the witness of Jesus'",
 "Fixed badges to MSG ranges",
],
confs=[
 "Ch12 para 3 merges MSG 12:7-12 (two printed paragraphs) \u2014 confirm one paragraph is OK",
],
)

# ============================== CHAPTER 13 ==============================
ch(13, "The Ultimate Boss Fight",
[
("1-2", "\u00a7The Beast from the Sea"),
("1-2", "And the Dragon stood on the shore of the sea. I saw a Beast rising from the sea. It had ten horns and seven heads\u2014on each horn a crown, and each head inscribed with a blasphemous name. The Beast I saw looked like a leopard with bear paws and a lion's mouth. The Dragon turned over its power to it, its throne and great authority."),
("3-4", "One of the Beast's heads looked as if it had been struck a deathblow, and then healed. The whole earth was agog, gaping at the Beast. They worshiped the Dragon who gave the Beast authority, and they worshiped the Beast, exclaiming, \u201cThere's never been anything like the Beast! No one would dare go to war with the Beast!\u201d"),
("5-8", "The Beast had a loud mouth, boastful and blasphemous. It could do anything it wanted for forty-two months. It yelled blasphemies against God, blasphemed his Name, blasphemed his Church, especially those already dwelling with God in Heaven. It was permitted to make war on God's holy people and conquer them. It held absolute sway over all tribes and peoples, tongues and races. Everyone on earth whose name was not written from the world's foundation in the slaughtered Lamb's Book of Life will worship the Beast."),
("9-10", "Are you listening to this? They've made their bed; now they must lie in it. Anyone marked for prison goes straight to prison; anyone pulling a sword goes down by the sword. Meanwhile, God's holy people passionately and faithfully stand their ground."),
("11-12", "\u00a7The Beast from Under the Ground"),
("11-12", "I saw another Beast rising out of the ground. It had two horns like a lamb but sounded like a dragon when it spoke. It was a puppet of the first Beast, made earth and everyone in it worship the first Beast, which had been healed of its deathblow."),
("13-17", "This second Beast worked magical signs, dazzling people by making fire come down from Heaven. It used the magic it got from the Beast to dupe earth dwellers, getting them to make an image of the Beast that received the deathblow and lived. It was able to animate the image of the Beast so that it talked, and then arrange that anyone not worshiping the Beast would be killed. It forced all people, small and great, rich and poor, free and slave, to have a mark on the right hand or forehead. Without the mark of the name of the Beast or the number of its name, it was impossible to buy or sell anything."),
("18", "Solve a riddle: Put your heads together and figure out the meaning of the number of the Beast. It's a human number: 666."),
],
msg_ranges=["1-2","3-4","5-8","9-10","11-12","13-17","18"],
changes=[
 "RESTORED MSG 13:9-10 (was completely missing): 'Are you listening to this? They've made their bed; now they must lie in it. Anyone marked for prison goes straight to prison; anyone pulling a sword goes down by the sword. Meanwhile, God's holy people passionately and faithfully stand their ground.'",
 "Replaced single invented header with MSG 'The Beast from the Sea' and 'The Beast from Under the Ground'",
 "Restored MSG 1-2 'And the Dragon stood on the shore of the sea', 'on each horn a crown, and each head inscribed with a blasphemous name', 'looked like a leopard with bear paws and a lion's mouth'",
 "Restored MSG 3-4 'looked as if it had been struck a deathblow, and then healed', 'The whole earth was agog, gaping at the Beast', 'There's never been anything like the Beast! No one would dare go to war with the Beast!'",
 "Restored MSG 5-8 'blasphemed his Church, especially those already dwelling with God in Heaven', 'It was permitted to make war on God's holy people and conquer them', 'It held absolute sway over all tribes and peoples, tongues and races'",
 "Restored MSG 11-12 'It was a puppet of the first Beast'",
 "Restored MSG 13-17 'worked magical signs, dazzling people by making fire come down from Heaven', 'dupe earth dwellers', 'It was able to animate the image of the Beast so that it talked', 'small and great, rich and poor, free and slave'",
 "Restored MSG 18 'Solve a riddle: Put your heads together' (was 'Put on your thinking caps')",
 "Fixed badges to MSG ranges",
],
)

# ============================== CHAPTER 14 ==============================
ch(14, "God's Honored Ones and the Final Smackdown",
[
("1-2", "\u00a7A Perfect Offering"),
("1-2", "I saw\u2014it took my breath away!\u2014the Lamb standing on Mount Zion, 144,000 standing there with him, his Name and the Name of his Father inscribed on their foreheads. And I heard a voice out of Heaven, the sound like rapids, like the crash of thunder."),
("2-5", "And then I heard music, harp music and the harpists singing a new song before the Throne and the Four Animals and the Elders. Only the 144,000 could learn to sing the song. They were bought from earth, lived without compromise, virgin-fresh before God. Wherever the Lamb went, they followed. They were bought from humankind, firstfruits of the harvest for God and the Lamb. Not a false word in their mouths. A perfect offering."),
("6-7", "\u00a7Voices from Heaven"),
("6-7", "I saw another Angel soaring in Middle-Heaven. He had an Eternal Message to preach to all who were still on earth, every nation and tribe, every tongue and people. He preached in a loud voice, \u201cFear God and give him glory! His hour of judgment has come! Worship the Maker of Heaven and earth, salt sea and fresh water!\u201d"),
("8", "A second Angel followed, calling out, \u201cRuined, ruined, Great Babylon ruined! She made all the nations drunk on the wine of her unfaithfulness!\u201d"),
("9-11", "A third Angel followed, shouting, warning, \u201cIf anyone worships the Beast and its image and takes the mark on forehead or hand, that person will drink the wine of God's wrath, prepared unmixed in his chalice of anger, and suffer torment from fire and brimstone in the presence of Holy Angels, in the presence of the Lamb. Smoke from their torment will rise age after age. No respite for those who worship the Beast and its image, who take the mark of its name.\u201d"),
("12", "Meanwhile, the saints stand passionately patient, keeping God's commands, staying faithful to Jesus."),
("13", "I heard a voice out of Heaven, \u201cWrite this: Blessed are those who die in the Master from now on; how blessed to die that way!\u201d \u201cYes,\u201d says the Spirit, \u201cand blessed rest from their hard, hard work. None of what they've done is wasted; God blesses them for it all in the end.\u201d"),
("14-16", "\u00a7Harvest Time"),
("14-16", "I looked up, I caught my breath!\u2014a white cloud and one like the Son of Man sitting on it. He wore a gold crown and held a sharp sickle. Another Angel came out of the Temple, shouting to the Cloud-Enthroned, \u201cSwing your sickle and reap. It's harvest time. Earth's harvest is ripe for reaping.\u201d The Cloud-Enthroned gave a mighty sweep of his sickle, began harvesting earth in a stroke."),
("17-18", "Then another Angel came out of the Temple in Heaven. He also had a sharp sickle. Yet another Angel, the one in charge of tending the fire, came from the Altar. He thundered to the Angel who held the sharp sickle, \u201cSwing your sharp sickle. Harvest earth's vineyard. The grapes are bursting with ripeness.\u201d"),
("19-20", "The Angel swung his sickle, harvested earth's vintage, and heaved it into the winepress, the giant winepress of God's wrath. The winepress was outside the City. As the vintage was trodden, blood poured from the winepress as high as a horse's bridle, a river of blood for two hundred miles."),
],
msg_ranges=["1-2","2-5","6-7","8","9-11","12","13","14-16","17-18","19-20"],
splits=[{"msg_range":"2","paras":[1,2],"note":"MSG-native overlap: v2 closes the Mount Zion vision (1-2) and opens the new song (2-5)"}],
changes=[
 "Replaced invented header with MSG 'A Perfect Offering', 'Voices from Heaven', 'Harvest Time'",
 "Restored MSG 1-2 'it took my breath away!', 'his Name and the Name of his Father inscribed on their foreheads' (was 'His and the Lamb's names')",
 "Restored MSG 2-5 'lived without compromise, virgin-fresh before God', 'Wherever the Lamb went, they followed', 'firstfruits of the harvest for God and the Lamb', 'Not a false word in their mouths. A perfect offering'",
 "Restored MSG 6-7 'soaring in Middle-Heaven', 'He had an Eternal Message', 'Worship the Maker of Heaven and earth, salt sea and fresh water!'",
 "Restored MSG 8 'Ruined, ruined, Great Babylon ruined! She made all the nations drunk on the wine of her whoring!'",
 "Restored MSG 9-11 'prepared unmixed in his chalice of anger', 'in the presence of Holy Angels, in the presence of the Lamb', 'Smoke from their torment will rise age after age. No respite'",
 "Restored MSG 12 'the saints stand passionately patient, keeping God's commands, staying faithful to Jesus'",
 "Restored MSG 13 'Blessed are those who die in the Master from now on', 'blessed rest from their hard, hard work. None of what they've done is wasted'",
 "Restored MSG 14-16 'I caught my breath!', 'the Cloud-Enthroned', 'Swing your sickle and reap. It's harvest time. Earth's harvest is ripe for reaping'",
 "Restored MSG 17-18 'the one in charge of tending the fire', 'The grapes are bursting with ripeness'",
 "Restored MSG 19-20 'as high as a horse's bridle' (was 'horse's head'), 'a river of blood for two hundred miles'",
 "Fixed badges to MSG ranges",
],
)

# ============================== CHAPTER 15 ==============================
ch(15, "The Seven Angels and the Final Smackdown",
[
("1", "\u00a7The Song of Moses, the Song of the Lamb"),
("1", "I saw another Sign in Heaven, huge and breathtaking: seven Angels with seven disasters. These are the final disasters, the wrap-up of God's wrath."),
("2-4", "I saw something like a sea made of glass, the glass all shot through with fire. Carrying harps of God, triumphant over the Beast, its image, and the number of its name, the saved ones stood on the sea of glass. They sang the Song of Moses, servant of God; they sang the Song of the Lamb: Mighty your acts and marvelous, O God, the Sovereign-Strong! Righteous your ways and true, King of the nations! Who can fail to fear you, God, give glory to your Name? Because you and you only are holy, all nations will come and worship you, because they see your judgments are right."),
("5-8", "Then I saw the doors of the Temple, the Tent of Witness in Heaven, open wide. The Seven Angels carrying the seven disasters came out of the Temple. They were dressed in clean, bright linen and wore gold vests. One of the Four Animals handed the Seven Angels seven gold bowls, brimming with the wrath of God, who lives forever and ever. Smoke from God's glory and power poured out of the Temple. No one was permitted to enter the Temple until the seven disasters of the Seven Angels were finished."),
],
msg_ranges=["1","2-4","5-8"],
merges=[
 {"para":2,"msg_ranges":["2-4"],"note":"MSG prints 2-4 as two paragraphs (sea of glass + song); kept as one EN paragraph"},
],
changes=[
 "Replaced invented header with MSG 'The Song of Moses, the Song of the Lamb'",
 "Restored MSG 1 'I saw another Sign in Heaven, huge and breathtaking' (was 'wild sight, totally mind-blowing')",
 "Restored MSG 2-4 'the glass all shot through with fire', 'They sang the Song of Moses, servant of God; they sang the Song of the Lamb', 'Mighty your acts and marvelous, O God, the Sovereign-Strong!', 'Righteous your ways and true, King of the nations!', 'give glory to your Name'",
 "Restored MSG 5-8 'the doors of the Temple, the Tent of Witness in Heaven, open wide', 'wore gold vests', 'who lives forever and ever', 'No one was permitted to enter the Temple until the seven disasters of the Seven Angels were finished'",
 "Removed invented 'No more messing around', 'looking like they meant business'; fixed badges to MSG ranges",
],
confs=[
 "Ch15 para 2 merges MSG 15:2-4 (two printed paragraphs) \u2014 confirm one paragraph is OK",
],
)

# ============================== CHAPTER 16 ==============================
ch(16, "The Seven Bowls of Epic Ownage",
[
("1", "\u00a7Pouring Out the Seven Disasters"),
("1", "I heard a shout of command from the Temple to the Seven Angels: \u201cBegin! Pour out the seven bowls of God's wrath on earth!\u201d"),
("2", "The first Angel stepped up and poured his bowl out on earth: Loathsome, stinking sores erupted on all who had taken the mark of the Beast and worshiped its image."),
("3", "The second Angel poured his bowl on the sea: The sea coagulated into blood, and everything in it died."),
("4-7", "The third Angel poured his bowl on rivers and springs: The waters turned to blood. I heard the Angel of Waters say, Righteous you are, and your judgments are righteous, The Is, The Was, The Holy. They poured out the blood of saints and prophets so you've given them blood to drink\u2014 they've gotten what they deserve! Just then I heard the Altar chime in, Yes, O God, the Sovereign-Strong! Your judgments are true and just!"),
("8-9", "The fourth Angel poured his bowl on the sun: Fire blazed from the sun and scorched men and women. Burned and blistered, they cursed God's Name, the God behind these disasters. They refused to repent, refused to honor God."),
("10-11", "The fifth Angel poured his bowl on the throne of the Beast: Its kingdom fell into sudden eclipse. Mad with pain, men and women bit and chewed their tongues, cursed the God-of-Heaven for their torment and sores, and refused to repent and change their ways."),
("12-14", "The sixth Angel poured his bowl on the great Euphrates River: It dried up to nothing. The dry riverbed became a fine roadbed for the kings from the East. From the mouths of the Dragon, the Beast, and the False Prophet I saw three foul demons crawl out\u2014they looked like frogs. These are demon spirits performing signs. They're after the kings of the whole world to get them gathered for battle on the Great Day of God, the Sovereign-Strong."),
("15", "\u201cKeep watch! I come unannounced, like a thief. You're blessed if, awake and dressed, you're ready for me. Too bad if you're found running through the streets, naked and ashamed.\u201d"),
("16", "The frog-demons gathered the kings together at the place called in Hebrew *Armageddon*."),
("17-21", "The seventh Angel poured his bowl into the air: From the Throne in the Temple came a shout, \u201cDone!\u201d followed by lightning flashes and shouts, thunder crashes and a colossal earthquake\u2014a huge and devastating earthquake, never an earthquake like it since time began. The Great City split three ways, the cities of the nations toppled to ruin. Great Babylon had to drink the wine of God's raging anger\u2014God remembered to give her the cup! Every island fled and not a mountain was to be found. Hailstones weighing close to a hundred pounds plummeted, crushing and smashing men and women as they cursed God for the hail, the epic disaster of hail."),
],
msg_ranges=["1","2","3","4-7","8-9","10-11","12-14","15","16","17-21"],
merges=[
 {"para":4,"msg_ranges":["4-7"],"note":"MSG prints 4-7 as two paragraphs (Angel of Waters + Altar); kept as one EN paragraph"},
],
changes=[
 "Replaced invented header with MSG 'Pouring Out the Seven Disasters'; removed invented 'The Bowls Keep Coming'",
 "Restored MSG 1 'a shout of command from the Temple', 'Begin! Pour out the seven bowls of God's wrath on earth!'",
 "Restored MSG 2 'Loathsome, stinking sores erupted'",
 "Restored MSG 3 'The sea coagulated into blood, and everything in it died'",
 "Restored MSG 4-7 'Righteous you are, and your judgments are righteous, The Is, The Was, The Holy', 'Yes, O God, the Sovereign-Strong! Your judgments are true and just!'",
 "Restored MSG 8-9 'Fire blazed from the sun and scorched men and women. Burned and blistered, they cursed God's Name, the God behind these disasters. They refused to repent, refused to honor God'",
 "Restored MSG 10-11 'Its kingdom fell into sudden eclipse. Mad with pain, men and women bit and chewed their tongues'",
 "Restored MSG 12-14 'It dried up to nothing. The dry riverbed became a fine roadbed', 'three foul demons crawl out', 'demon spirits performing signs', 'the Great Day of God, the Sovereign-Strong'",
 "Restored MSG 15 'Keep watch! I come unannounced, like a thief. You're blessed if, awake and dressed'",
 "Restored MSG 17-21 'lightning flashes and shouts, thunder crashes and a colossal earthquake\u2014a huge and devastating earthquake, never an earthquake like it since time began', 'The Great City split three ways, the cities of the nations toppled to ruin', 'Hailstones weighing close to a hundred pounds plummeted, crushing and smashing men and women'",
 "Fixed badge 15-16 to 15 (was overlapping 16); removed invented 'Super horrible', 'Total fail'; fixed badges to MSG ranges",
],
confs=[
 "Ch16 para 4 merges MSG 16:4-7 (two printed paragraphs) \u2014 confirm one paragraph is OK",
],
)

# ============================== CHAPTER 17 ==============================
ch(17, "The Shady Queen and the Monster Beast",
[
("1-2", "\u00a7Great Babylon, Mother of Prostitutes"),
("1-2", "One of the Seven Angels who carried the seven bowls came and invited me, \u201cCome, I'll show you the judgment of the great Prostitute who sits enthroned over many waters, the Prostitute with whom the kings of the earth have been unfaithful, show you the judgment on earth dwellers drunk on her seductive lust.\u201d"),
("3-6", "In the Spirit he carried me out in the desert. I saw a woman mounted on a Scarlet Beast. Stuffed with blasphemies, the Beast had seven heads and ten horns. The woman was dressed in purple and scarlet, festooned with gold and gems and pearls. She held a gold chalice in her hand, brimming with defiling obscenities, her foul fornications. A riddle-name was branded on her forehead: great babylon, mother of prostitutes and abominations of the earth. I could see that the woman was drunk, drunk on the blood of God's holy people, drunk on the blood of the martyrs of Jesus."),
("6-8", "Astonished, I rubbed my eyes. I shook my head in wonder. The Angel said, \u201cDoes this surprise you? Let me tell you the riddle of the woman and the Beast she rides, the Beast with seven heads and ten horns. The Beast you saw once was, is no longer, and is about to ascend from the Abyss and head straight for Hell. Earth dwellers whose names weren't written in the Book of Life from the foundation of the world will be dazzled when they see the Beast that once was, is no longer, and is to come."),
("9-11", "\u201cBut don't drop your guard. Use your head. The seven heads are seven hills; they are where the woman sits. They are also seven kings: five dead, one living, the other not yet here\u2014and when he does come his time will be brief. The Beast that once was and is no longer is both an eighth and one of the seven\u2014and headed for Hell."),
("12-14", "\u201cThe ten horns you saw are ten kings, but they're not yet in power. They will come to power with the Scarlet Beast, but won't last long\u2014a *very* brief reign. These kings will agree to turn over their power and authority to the Beast. They will go to war against the Lamb but the Lamb will defeat them, proof that he is Lord over all lords, King over all kings, and those with him will be the called, chosen, and faithful.\u201d"),
("15-18", "The Angel continued, \u201cThe waters you saw on which the Prostitute was enthroned are peoples and crowds, nations and languages. And the ten horns you saw, together with the Beast, will turn on the Prostitute\u2014they'll hate her, violate her, strip her naked, rip her apart with their teeth, then set fire to her. It was God who put the idea in their heads to turn over their rule to the Beast until the words of God are completed. The woman you saw is the great city, tyrannizing the kings of the earth.\u201d"),
],
msg_ranges=["1-2","3-6","6-8","9-11","12-14","15-18"],
splits=[
 {"msg_range":"6","paras":[1,2],"note":"MSG-native overlap: v6 closes the woman's description (3-6) and opens the angel's riddle (6-8)"},
],
changes=[
 "Replaced invented header with MSG 'Great Babylon, Mother of Whores'",
 "Restored MSG 1-2 'who sits enthroned over many waters', 'the Whore with whom the kings of the earth have gone whoring', 'drunk on her whorish lust'",
 "Restored MSG 3-6 'In the Spirit he carried me out in the desert', 'Stuffed with blasphemies', 'festooned with gold and gems and pearls', 'brimming with defiling obscenities, her foul fornications', 'A riddle-name was branded on her forehead: great babylon, mother of prostitutes and abominations of the earth', 'drunk on the blood of God's holy people, drunk on the blood of the martyrs of Jesus'",
 "Restored MSG 6-8 'Astonished, I rubbed my eyes. I shook my head in wonder', 'is about to ascend from the Abyss and head straight for Hell'",
 "Restored MSG 9-11 'But don't drop your guard. Use your head. The seven heads are seven hills', 'five dead, one living, the other not yet here', 'is both an eighth and one of the seven\u2014and headed for Hell'",
 "Restored MSG 12-14 'a *very* brief reign', 'proof that he is Lord over all lords, King over all kings, and those with him will be the called, chosen, and faithful'",
 "Restored MSG 15-18 'are peoples and crowds, nations and languages', 'they'll hate her, violate her, strip her naked, rip her apart with their teeth, then set fire to her', 'It was God who put the idea in their heads', 'tyrannizing the kings of the earth'",
 "Removed invented 'tattoo', 'shady queen'; fixed badges to MSG ranges",
],
)

# ============================== CHAPTER 18 ==============================
ch(18, "The Ultimate Takedown",
[
("1-8", "\u00a7Doom to the City of Darkness"),
("1-8", "Following this I saw another Angel descend from Heaven. His authority was immense, his glory flooded earth with brightness, his voice thunderous: Ruined, ruined, Great Babylon, ruined! A ghost town for demons is all that's left! A garrison of carrion spirits, garrison of loathsome, carrion birds. All nations drank the wild wine of her unfaithfulness; kings of the earth were unfaithful with her; entrepreneurs made millions exploiting her. Just then I heard another shout out of Heaven: Get out, my people, as fast as you can, so you don't get mixed up in her sins, so you don't get caught in her doom. Her sins stink to high Heaven; God has remembered every evil she's done. Give her back what she's given, double what she's doubled in her works, double the recipe in the cup she mixed; Bring her flaunting and wild ways to torment and tears. Because she gloated, \u201cI'm queen over all, and no widow, never a tear on my face,\u201d In one day, disasters will crush her\u2014 death, heartbreak, and famine\u2014 Then she'll be burned by fire, because God, the Strong God who judges her, has had enough."),
("9-10", "\u201cThe kings of the earth will see the smoke of her burning, and they'll cry and carry on, the kings who went night after night to her brothel. They'll keep their distance for fear they'll get burned, and they'll cry their lament: Doom, doom, the great city doomed! City of Babylon, strong city! In one hour it's over, your judgment come!"),
("11-17", "\u201cThe traders will cry and carry on because the bottom dropped out of business, no more market for their goods: gold, silver, precious gems, pearls; fabrics of fine linen, purple, silk, scarlet; perfumed wood and vessels of ivory, precious woods, bronze, iron, and marble; cinnamon and spice, incense, myrrh, and frankincense; wine and oil, flour and wheat; cattle, sheep, horses, and chariots. And slaves\u2014their terrible traffic in human lives. Everything you've lived for, gone! All delicate and delectable luxury, lost! Not a scrap, not a thread to be found! The traders who made millions off her kept their distance for fear of getting burned, and cried and carried on all the more: Doom, doom, the great city doomed! Dressed in the latest fashions, adorned with the finest jewels, in one hour such wealth wiped out!"),
("17-19", "\u201cAll the ship captains and travelers by sea, sailors and toilers of the sea, stood off at a distance and cried their lament when they saw the smoke from her burning: 'Oh, what a city! There was never a city like her!' They threw dust on their heads and cried as if the world had come to an end: Doom, doom, the great city doomed! All who owned ships or did business by sea got rich on her getting and spending. And now it's over\u2014wiped out in one hour!"),
("20", "\u201cO Heaven, celebrate! And join in, saints, apostles, and prophets! God has judged her; every wrong you suffered from her has been judged.\u201d"),
("21-24", "A strong Angel reached for a boulder\u2014huge, like a millstone\u2014and heaved it into the sea, saying, Heaved and sunk, the great city Babylon, sunk in the sea, not a sign of her ever again. Silent the music of harpists and singers\u2014 you'll never hear flutes and trumpets again. Artisans of every kind\u2014gone; you'll never see their likes again. The voice of a millstone grinding falls dumb; you'll never hear that sound again. The light from lamps, never again; never again laughter of bride and groom. Her traders robbed the whole earth blind, and by black-magic arts deceived the nations. The only thing left of Babylon is blood\u2014 the blood of saints and prophets, the murdered and the martyred."),
],
msg_ranges=["1-8","9-10","11-17","17-19","20","21-24"],
merges=[
 {"para":1,"msg_ranges":["1-8"],"note":"MSG prints 1-8 as one paragraph (angel's dirge + heaven's shout); kept as one EN paragraph (old EN split it into five)"},
],
splits=[
 {"msg_range":"17","paras":[2,3],"note":"MSG-native overlap: v17 closes the traders' lament (11-17) and opens the sailors' lament (17-19)"},
],
changes=[
 "Replaced invented header with MSG 'Doom to the City of Darkness'",
 "Merged old EN 1-2/3/4-5/6-7/8 into one MSG 1-8 paragraph",
 "Restored MSG 1-8 'His authority was immense, his glory flooded earth with brightness, his voice thunderous', 'A ghost town for demons', 'A garrison of carrion spirits, garrison of loathsome, carrion birds', 'entrepreneurs made millions exploiting her', 'Her sins stink to high Heaven', 'double what she's doubled in her works, double the recipe in the cup she mixed', 'Bring her flaunting and wild ways to torment and tears', 'In one day, disasters will crush her\u2014 death, heartbreak, and famine\u2014', 'God, the Strong God who judges her, has had enough'",
 "Restored MSG 9-10 'the kings who went night after night to her brothel', 'Doom, doom, the great city doomed! City of Babylon, strong city!'",
 "Restored MSG 11-17 full cargo list 'fabrics of fine linen, purple, silk, scarlet; perfumed wood and vessels of ivory', 'cinnamon and spice, incense, myrrh, and frankincense', 'And slaves\u2014their terrible traffic in human lives', 'Not a scrap, not a thread to be found!'",
 "Restored MSG 17-19 'travelers by sea, sailors and toilers of the sea', 'They threw dust on their heads', 'Got rich on her getting and spending'",
 "Restored MSG 20 'O Heaven, celebrate! And join in, saints, apostles, and prophets! God has judged her; every wrong you suffered from her has been judged'",
 "Restored MSG 21-24 'reached for a boulder\u2014huge, like a millstone\u2014and heaved it into the sea', 'Silent the music of harpists and singers', 'Artisans of every kind\u2014gone', 'The voice of a millstone grinding falls dumb', 'never again laughter of bride and groom', 'Her traders robbed the whole earth blind, and by black-magic arts deceived the nations', 'the blood of saints and prophets, the murdered and the martyred'",
 "Fixed badges to MSG ranges",
],
confs=[
 "Ch18 para 1 merges MSG 18:1-8 (one printed paragraph; old EN had split it into five) \u2014 confirm one paragraph is OK",
],
)

# ============================== CHAPTER 19 ==============================
ch(19, "The Ultimate Comeback",
[
("1-3", "\u00a7The Sound of Hallelujahs"),
("1-3", "I heard a sound like massed choirs in Heaven singing, Hallelujah! The salvation and glory and power are God's\u2014 his judgments true, his judgments just. He judged the great Prostitute who corrupted the earth with her lust. He avenged on her the blood of his servants. Then, more singing: Hallelujah! The smoke from her burning billows up to high Heaven forever and ever and ever."),
("4", "The Twenty-four Elders and the Four Animals fell to their knees and worshiped God on his Throne, praising, Amen! Yes! Hallelujah!"),
("5", "From the Throne came a shout, a command: Praise our God, all you his servants, All you who fear him, small and great!"),
("6-8", "Then I heard the sound of massed choirs, the sound of mighty rapids, the sound of strong thunder: Hallelujah! The Master reigns, our God, the Sovereign-Strong! Let us celebrate, let us rejoice, let us give him the glory! The Marriage of the Lamb has come; his Wife has made herself ready. She was given a bridal gown of bright and shining linen. The linen is the righteousness of the saints."),
("9", "The Angel said to me, \u201cWrite this: 'Blessed are those invited to the Wedding Supper of the Lamb.'\u201d He added, \u201cThese are the true words of God!\u201d"),
("10", "I fell at his feet to worship him, but he wouldn't let me. \u201cDon't do that,\u201d he said. \u201cI'm a servant just like you, and like your brothers and sisters who hold to the witness of Jesus. The witness of Jesus is the spirit of prophecy.\u201d"),
("11-16", "\u00a7A White Horse and Its Rider"),
("11-16", "Then I saw Heaven open wide\u2014and oh! a white horse and its Rider. The Rider, named Faithful and True, judges and makes war in pure righteousness. His eyes are a blaze of fire, on his head many crowns. He has a Name inscribed that's known only to himself. He is dressed in a robe soaked with blood, and he is addressed as \u201cWord of God.\u201d The armies of Heaven, mounted on white horses and dressed in dazzling white linen, follow him. A sharp sword comes out of his mouth so he can subdue the nations, then rule them with a rod of iron. He treads the winepress of the raging wrath of God, the Sovereign-Strong. On his robe and thigh is written, King of kings, Lord of lords."),
("17-18", "I saw an Angel standing in the sun, shouting to all flying birds in Middle-Heaven, \u201cCome to the Great Supper of God! Feast on the flesh of kings and captains and champions, horses and their riders. Eat your fill of them all\u2014free and slave, small and great!\u201d"),
("19-21", "I saw the Beast and, assembled with him, earth's kings and their armies, ready to make war against the One on the horse and his army. The Beast was taken, and with him, his puppet, the False Prophet, who used signs to dazzle and deceive those who had taken the mark of the Beast and worshiped his image. They were thrown alive, those two, into Lake Fire and Brimstone. The rest were killed by the sword of the One on the horse, the sword that comes from his mouth. All the birds held a feast on their flesh."),
],
msg_ranges=["1-3","4","5","6-8","9","10","11-16","17-18","19-21"],
merges=[
 {"para":1,"msg_ranges":["1-3"],"note":"MSG prints 1-3 as two paragraphs (first hallelujah + second hallelujah); kept as one EN paragraph (old EN split it into 1-2 and 3)"},
 {"para":4,"msg_ranges":["6-8"],"note":"MSG prints 6-8 as two paragraphs (massed choirs + marriage song); kept as one EN paragraph"},
],
changes=[
 "Replaced wrong first header with MSG 'The Sound of Hallelujahs' and 'A White Horse and Its Rider'",
 "Merged old EN 1-2 + 3 into one MSG 1-3 paragraph",
 "Restored MSG 1-3 'a sound like massed choirs', 'his judgments true, his judgments just', 'He avenged on her the blood of his servants', 'The smoke from her burning billows up to high Heaven forever and ever and ever'",
 "Restored MSG 4 'The Twenty-four Elders' (was '24 bosses'), 'Amen! Yes! Hallelujah!'",
 "Restored MSG 5 'From the Throne came a shout, a command: Praise our God, all you his servants, All you who fear him, small and great!'",
 "Restored MSG 6-8 'the sound of mighty rapids, the sound of strong thunder', 'The Master reigns, our God, the Sovereign-Strong!', 'The Marriage of the Lamb has come; his Wife has made herself ready. She was given a bridal gown of bright and shining linen. The linen is the righteousness of the saints'",
 "Restored MSG 9 'Blessed are those invited to the Wedding Supper of the Lamb', 'These are the true words of God!'",
 "Restored MSG 10 'I'm a servant just like you, and like your brothers and sisters who hold to the witness of Jesus. The witness of Jesus is the spirit of prophecy'",
 "Restored MSG 11-16 'named Faithful and True, judges and makes war in pure righteousness', 'He has a Name inscribed that's known only to himself', 'dressed in a robe soaked with blood', 'addressed as Word of God', 'dressed in dazzling white linen', 'rule them with a rod of iron', 'He treads the winepress of the raging wrath of God, the Sovereign-Strong', 'On his robe and thigh is written, King of kings, Lord of lords' (was 'tattoo on his leg')",
 "Restored MSG 17-18 'shouting to all flying birds in Middle-Heaven', 'Come to the Great Supper of God! Feast on the flesh of kings and captains and champions'",
 "Restored MSG 19-21 'his puppet, the False Prophet, who used signs to dazzle and deceive', 'They were thrown alive, those two, into Lake Fire and Brimstone', 'All the birds held a feast on their flesh'",
 "Fixed badges to MSG ranges",
],
confs=[
 "Ch19 para 1 merges MSG 19:1-3 (two printed paragraphs) \u2014 confirm one paragraph is OK",
 "Ch19 para 4 merges MSG 19:6-8 (two printed paragraphs) \u2014 confirm one paragraph is OK",
],
)

# ============================== CHAPTER 20 ==============================
ch(20, "The Final Boss Battle",
[
("1-3", "\u00a7A Thousand Years"),
("1-3", "I saw an Angel descending out of Heaven. He carried the key to the Abyss and a chain\u2014a huge chain. He grabbed the Dragon, that old Snake\u2014the very Devil, Satan himself!\u2014chained him up for a thousand years, dumped him into the Abyss, slammed it shut and sealed it tight. No more trouble out of him, deceiving the nations\u2014until the thousand years are up. After that he has to be let loose briefly."),
("4-6", "I saw thrones. Those put in charge of judgment sat on the thrones. I also saw the souls of those beheaded because of their witness to Jesus and the Word of God, who refused to worship either the Beast or his image, refused to take his mark on forehead or hand\u2014they lived and reigned with Christ for a thousand years! The rest of the dead did not live until the thousand years were up. This is the first resurrection\u2014and those involved most blessed, most holy. No second death for them! They're priests of God and Christ; they'll reign with him a thousand years."),
("7-10", "When the thousand years are up, Satan will be let loose from his cell, and will launch again his old work of deceiving the nations, searching out victims in every nook and cranny of earth, even Gog and Magog! He'll talk them into going to war and will gather a huge army, millions strong. They'll stream across the earth, surround and lay siege to the camp of God's holy people, the Beloved City. They'll no sooner get there than fire will pour out of Heaven and burn them up. The Devil who deceived them will be hurled into Lake Fire and Brimstone, joining the Beast and False Prophet, the three in torment around the clock for ages without end."),
("11-15", "\u00a7Judgment"),
("11-15", "I saw a Great White Throne and the One Enthroned. Nothing could stand before or against the Presence, nothing in Heaven, nothing on earth. And then I saw all the dead, great and small, standing there\u2014before the Throne! And books were opened. Then another book was opened: the Book of Life. The dead were judged by what was written in the books, by the way they had lived. Sea released its dead, Death and Hell turned in their dead. Each man and woman was judged by the way he or she had lived. Then Death and Hell were hurled into Lake Fire. This is the second death\u2014Lake Fire. Anyone whose name was not found inscribed in the Book of Life was hurled into Lake Fire."),
],
msg_ranges=["1-3","4-6","7-10","11-15"],
changes=[
 "Added missing MSG header 'Judgment' (badge 11-15)",
 "Restored MSG 1-3 'a chain\u2014a huge chain', 'that old Snake\u2014the very Devil, Satan himself!', 'slammed it shut and sealed it tight', 'No more trouble out of him, deceiving the nations'",
 "Restored MSG 4-6 'those beheaded because of their witness to Jesus' (was 'taken out'), 'This is the first resurrection\u2014and those involved most blessed, most holy. No second death for them!'",
 "Restored MSG 7-10 'will launch again his old work of deceiving the nations, searching out victims in every nook and cranny of earth, even Gog and Magog!', 'millions strong', 'surround and lay siege to the camp of God's holy people, the Beloved City', 'fire will pour out of Heaven and burn them up', 'the three in torment around the clock for ages without end'",
 "Restored MSG 11-15 'Nothing could stand before or against the Presence, nothing in Heaven, nothing on earth', 'by the way they had lived', 'Sea released its dead, Death and Hell turned in their dead', 'This is the second death\u2014Lake Fire'",
 "Fixed badge 12-15 to 11-15",
],
)

# ============================== CHAPTER 21 ==============================
ch(21, "The Ultimate Transformation",
[
("1", "\u00a7Everything New"),
("1", "I saw Heaven and earth new-created. Gone the first Heaven, gone the first earth, gone the sea."),
("2", "I saw Holy Jerusalem, new-created, descending resplendent out of Heaven, as ready for God as a bride for her husband."),
("3-5", "I heard a voice thunder from the Throne: \u201cLook! Look! God has moved into the neighborhood, making his home with men and women! They're his people, he's their God. He'll wipe every tear from their eyes. Death is gone for good\u2014tears gone, crying gone, pain gone\u2014all the first order of things gone.\u201d The Enthroned continued, \u201cLook! I'm making everything new. Write it all down\u2014each word dependable and accurate.\u201d"),
("6-8", "Then he said, \u201cIt's happened. I'm A to Z. I'm the Beginning, I'm the Conclusion. From Water-of-Life Well I give freely to the thirsty. Conquerors inherit all this. I'll be God to them, they'll be sons and daughters to me. But for the rest\u2014the feckless and faithless, degenerates and murderers, sex peddlers and sorcerers, idolaters and all liars\u2014for them it's Lake Fire and Brimstone. Second death!\u201d"),
("9-12", "\u00a7The City of Light"),
("9-12", "One of the Seven Angels who had carried the bowls filled with the seven final disasters spoke to me: \u201cCome here. I'll show you the Bride, the Wife of the Lamb.\u201d He took me away in the Spirit to an enormous, high mountain and showed me Holy Jerusalem descending out of Heaven from God, resplendent in the bright glory of God."),
("12-14", "The City shimmered like a precious gem, light-filled, pulsing light. She had a wall majestic and high with twelve gates. At each gate stood an Angel, and on the gates were inscribed the names of the Twelve Tribes of the sons of Israel: three gates on the east, three gates on the north, three gates on the south, three gates on the west. The wall was set on twelve foundations, the names of the Twelve Apostles of the Lamb inscribed on them."),
("15-21", "The Angel speaking with me had a gold measuring stick to measure the City, its gates, and its wall. The City was laid out in a perfect square. He measured the City with the measuring stick: fifteen hundred miles, its length, width, and height all equal. Using the standard measure, the Angel measured the thickness of its wall: seventy-two yards. The wall was jasper, the color of Glory, and the City was pure gold, translucent as glass. The foundations of the City walls were garnished with every precious gem imaginable: the first foundation jasper, the second sapphire, the third agate, the fourth emerald, the fifth onyx, the sixth carnelian, the seventh chrysolite, the eighth beryl, the ninth topaz, the tenth chrysoprase, the eleventh jacinth, the twelfth amethyst. The twelve gates were twelve pearls, each gate a single pearl."),
("21-27", "The main street of the City was pure gold, translucent as glass. But there was no sign of a Temple, for the Lord God\u2014the Sovereign-Strong\u2014and the Lamb are the Temple. The City doesn't need sun or moon for light. God's Glory is its light, the Lamb its lamp! The nations will walk in its light and earth's kings bring in their splendor. Its gates will never be shut by day, and there won't be any night. They'll bring the glory and honor of the nations into the City. Nothing dirty or defiled will get into the City, and no one who defiles or deceives. Only those whose names are written in the Lamb's Book of Life will get in."),
],
msg_ranges=["1","2","3-5","6-8","9-12","12-14","15-21","21-27"],
splits=[
 {"msg_range":"12","paras":[4,5],"note":"MSG-native overlap: v12 closes the Bride vision (9-12) and opens the wall description (12-14)"},
 {"msg_range":"21","paras":[6,7],"note":"MSG-native overlap: v21 closes the measurements (15-21) and opens the street/Temple (21-27)"},
],
changes=[
 "Replaced invented headers with MSG 'Everything New' and 'The City of Light'",
 "Split old EN 1-2 into MSG 1 and 2; fixed shifted badges",
 "Restored MSG 1 'new-created. Gone the first Heaven, gone the first earth, gone the sea'",
 "Restored MSG 2 'descending resplendent out of Heaven, as ready for God as a bride for her husband'",
 "Restored MSG 3-5 'a voice thunder from the Throne', 'making his home with men and women', 'Death is gone for good\u2014tears gone, crying gone, pain gone\u2014all the first order of things gone', 'each word dependable and accurate'",
 "Restored MSG 6-8 'It's happened. I'm A to Z. I'm the Beginning, I'm the Conclusion', 'From Water-of-Life Well I give freely to the thirsty', 'they'll be sons and daughters to me', 'the feckless and faithless, degenerates and murderers, sex peddlers and sorcerers, idolaters and all liars'",
 "Restored MSG 9-12 'who had carried the bowls filled with the seven final disasters', 'He took me away in the Spirit to an enormous, high mountain', 'resplendent in the bright glory of God'",
 "Restored MSG 12-14 'shimmered like a precious gem, light-filled, pulsing light', 'She had a wall majestic and high', 'inscribed the names of the Twelve Tribes of the sons of Israel'",
 "Restored MSG 15-21 'seventy-two yards' (was converted to 216 feet), 'the color of Glory', 'translucent as glass', full gem order with 'the first foundation jasper, the second sapphire...'",
 "Restored MSG 21-27 'the Lord God\u2014the Sovereign-Strong\u2014and the Lamb are the Temple', 'God's Glory is its light, the Lamb its lamp!', 'earth's kings bring in their splendor', 'Nothing dirty or defiled will get into the City, and no one who defiles or deceives'",
 "Fixed badges to MSG ranges",
],
)

# ============================== CHAPTER 22 ==============================
ch(22, "The Epic Finale",
[
("1-5", "Then the Angel showed me Water-of-Life River, crystal bright. It flowed from the Throne of God and the Lamb, right down the middle of the street. The Tree of Life was planted on each side of the River, producing twelve kinds of fruit, a ripe fruit each month. The leaves of the Tree are for healing the nations. Never again will anything be cursed. The Throne of God and of the Lamb is at the center. His servants will offer God service\u2014worshiping, they'll look on his face, their foreheads mirroring God. Never again will there be any night. No one will need lamplight or sunlight. The shining of God, the Master, is all the light anyone needs. And they will rule with him age after age after age."),
("6-7", "\u00a7Don't Put It Away on the Shelf"),
("6-7", "The Angel said to me, \u201cThese are dependable and accurate words, every one. The God and Master of the spirits of the prophets sent his Angel to show his servants what must take place, and soon. And tell them, 'Yes, I'm on my way!' Blessed be the one who keeps the words of the prophecy of this book.\u201d"),
("8-9", "I, John, saw all these things with my own eyes, heard them with my ears. Immediately when I heard and saw, I fell on my face to worship at the feet of the Angel who laid it all out before me. He objected, \u201cNo you don't! I'm a servant just like you and your companions, the prophets, and all who keep the words of this book. Worship God!\u201d"),
("10-11", "The Angel continued, \u201cDon't seal the words of the prophecy of this book; don't put it away on the shelf. Time is just about up. Let evildoers do their worst and the dirty-minded go all out in pollution, but let the righteous maintain a straight course and the holy continue on in holiness.\u201d"),
("12-13", "\u201cYes, I'm on my way! I'll be there soon! I'm bringing my payroll with me. I'll pay all people in full for their life's work. I'm A to Z, the First and the Final, Beginning and Conclusion."),
("14-15", "\u201cHow blessed are those who wash their robes! The Tree of Life is theirs for good, and they'll walk through the gates to the City. But outside for good are the filthy curs: sorcerers, fornicators, murderers, idolaters\u2014all who love and live lies."),
("16", "\u201cI, Jesus, sent my Angel to testify to these things for the churches. I'm the Root and Branch of David, the Bright Morning Star.\u201d"),
("17", "\u201cCome!\u201d say the Spirit and the Bride. Whoever hears, echo, \u201cCome!\u201d Is anyone thirsty? Come! All who will, come and drink, Drink freely of the Water of Life!"),
("18-19", "I give fair warning to all who hear the words of the prophecy of this book: If you add to the words of this prophecy, God will add to your life the disasters written in this book; if you subtract from the words of the book of this prophecy, God will subtract your part from the Tree of Life and the Holy City that are written in this book."),
("20", "He who testifies to all these things says it again: \u201cI'm on my way! I'll be there soon!\u201d Yes! Come, Master Jesus!"),
("21", "The grace of the Master Jesus be with all of you. Oh, Yes!"),
],
msg_ranges=["1-5","6-7","8-9","10-11","12-13","14-15","16","17","18-19","20","21"],
changes=[
 "Replaced invented header with MSG 'Don't Put It Away on the Shelf'",
 "Split old EN 12-13 (which contained 14-15) into MSG 12-13 and 14-15",
 "Restored MSG 1-5 'Water-of-Life River, crystal bright', 'right down the middle of the street', 'a ripe fruit each month', 'The leaves of the Tree are for healing the nations', 'their foreheads mirroring God', 'And they will rule with him age after age after age'",
 "Restored MSG 6-7 'These are dependable and accurate words, every one. The God and Master of the spirits of the prophets sent his Angel'",
 "Restored MSG 8-9 'saw all these things with my own eyes, heard them with my ears', 'He objected, No you don't! I'm a servant just like you and your companions, the prophets'",
 "Restored MSG 10-11 'Don't seal the words of the prophecy of this book; don't put it away on the shelf', 'Let evildoers do their worst and the dirty-minded go all out in pollution, but let the righteous maintain a straight course and the holy continue on in holiness'",
 "Restored MSG 12-13 'I'm bringing my payroll with me. I'll pay all people in full for their life's work. I'm A to Z, the First and the Final, Beginning and Conclusion'",
 "Restored MSG 14-15 'How blessed are those who wash their robes!' (was 'cleaned up their act'), 'But outside for good are the filthy curs: sorcerers, fornicators, murderers, idolaters\u2014all who love and live lies' (was omitting sorcerers/fornicators)",
 "Restored MSG 16 'testify to these things for the churches. I'm the Root and Branch of David, the Bright Morning Star'",
 "Restored MSG 17 'Whoever hears, echo, Come! Is anyone thirsty? Come! All who will, come and drink, Drink freely of the Water of Life!'",
 "Restored MSG 18-19 full warning (was badge 18 only)",
 "Merged MSG 20 into one paragraph: 'I'm on my way! I'll be there soon!' + 'Yes! Come, Master Jesus!' (old EN wrongly split response into separate 21)",
 "Kept MSG 21 as grace sentence only: 'The grace of the Master Jesus be with all of you. Oh, Yes!'",
 "Removed invented 'Talk about a miraculous transformation'; fixed badges to MSG ranges",
],
)

# ============================== KO CHAPTERS ==============================
# KO mirrors EN 1:1 in paragraph count and badges. Based on KO extract, restructured.

def koch(n, paras):
    KO[n] = paras

# Ch1 KO (7 paras)
koch(1, [
("4-7", "\u00a7\ubd88\uaf43 \ub208\ub3d9\uc790"),
("1-2", "\uc790, \uc774\uc57c\uae30 \uc798 \ub4e4\uc5b4\ubd10. \uc774 \ucc45\uc740 \uc608\uc218 \uadf8\ub9ac\uc2a4\ub3c4\uc758 \uacc4\uc2dc\uc57c. \ud558\ub098\ub2d8\uc774 \uc55e\uc73c\ub85c \uc77c\uc5b4\ub0a0 \uc77c\ub4e4\uc744 \uc790\uae30 \uc885\ub4e4\ud55c\ud14c \ud655\uc2e4\ud788 \ubcf4\uc5ec\uc8fc\ub824\uace0 \uc774 \uacc4\uc2dc\ub97c \uc8fc\uc2e0 \uac70\uc57c. \ud558\ub098\ub2d8\uc740 \uc774\uac78 \ucd9c\ud310\ud558\uc154\uc11c \ucc9c\uc0ac\ub97c \ud1b5\ud574 \uc790\uae30 \uc885\uc778 \uc694\ud55c\ud55c\ud14c \uc804\ub2ec\ud574\uc8fc\uc168\uc5b4. \uadf8\ub9ac\uace0 \uc694\ud55c\uc740 \uc790\uae30\uac00 \ubcf8 \ubaa8\ub4e0 \uac78 \ub2e4 \ub9d0\ud588\uc5b4. \ud558\ub098\ub2d8\uc758 \ub9d0\uc500, \uc989 \uc608\uc218 \uadf8\ub9ac\uc2a4\ub3c4\uc758 \uc99d\uc5b8\uc744 \ub9d0\uc774\uc57c!"),
("3", "\uc774\uac78 \uc77d\ub294 \uc0ac\ub78c\uc740 \uc9c4\uc9dc \ubcf5 \ubc1b\uc740 \uac70\uc57c! \uc774 \uc608\uc5b8\uc758 \ub9d0\uc500\uc744 \ub4e3\uace0 \uc9c0\ud0a4\ub294 \uc0ac\ub78c\ub4e4\ub3c4 \uc644\uc804 \ubcf5 \ubc1b\uc740 \uac70\uc57c! \uc65c\ub0d0\ud558\uba74 \ub54c\uac00 \uc9c4\uc9dc \ucf54\uc55e\uc73c\ub85c \ub2e4\uac00\uc654\uac70\ub4e0."),
("4-7", "\ub098 \uc694\ud55c\uc740 \uc544\uc2dc\uc544\uc5d0 \uc788\ub294 \uc77c\uacf1 \uad50\ud68c\uc5d0 \uc774 \ud3b8\uc9c0\ub97c \uc368. \uc9c0\uae08\ub3c4 \uacc4\uc2dc\uace0 \uc804\uc5d0\ub3c4 \uacc4\uc168\uace0 \uc55e\uc73c\ub85c \uc624\uc2e4 \ud558\ub098\ub2d8, \uadf8\ub9ac\uace0 \uadf8\ubd84 \ubcf4\uc88c \uc55e\uc5d0 \uc788\ub294 \uc77c\uacf1 \uc601, \ub610 \ucda9\uc131\uc2a4\ub7ec\uc6b4 \uc99d\uc778\uc774\uc790 \uc8fd\uc740 \uc0ac\ub78c\ub4e4 \uc911\uc5d0\uc11c \ucc98\uc74c\uc73c\ub85c \uc0b4\uc544\ub098\uc2e0 \ubd84, \uadf8\ub9ac\uace0 \uc774 \ub545\uc758 \ubaa8\ub4e0 \uc655\ub4e4\uc744 \ub2e4\uc2a4\ub9ac\uc2dc\ub294 \uc608\uc218 \uadf8\ub9ac\uc2a4\ub3c4\uaed8\uc11c \ub108\ud76c\ud55c\ud14c \uc628\uac16 \uc88b\uc740 \uac78 \ub0b4\ub824\uc8fc\uc2dc\uae38 \ubc14\ub798. \uc6b0\ub9ac\ub97c \uc0ac\ub791\ud574\uc11c \uc6b0\ub9ac \uc8c4\ub97c \uc790\uae30 \ud53c\ub85c \uc53b\uc5b4\uc8fc\uc2dc\uace0, \uc6b0\ub9ac\ub97c \ud55c \ub098\ub77c\ub85c, \uc790\uae30 \uc544\ubc84\uc9c0\ub97c \uc704\ud55c \uc81c\uc0ac\uc7a5\uc73c\ub85c \uc0bc\uc544\uc8fc\uc2e0 \uadf8\ub9ac\uc2a4\ub3c4\uaed8 \uc601\uad11\uacfc \ub2a5\ub825\uc774 \uc601\uc6d0\ud558\uae38! \uc544\uba58. \uadf8\ubd84\uc774 \uc9c0\uae08 \uc624\uace0 \uacc4\uc154! \uad6c\ub984 \ud0c0\uace0 \uc624\uc2dc\ub294\ub370, \ubaa8\ub4e0 \uc0ac\ub78c\ub4e4\uc774 \ub2e4 \ubcf4\uac8c \ub420 \uac70\uc57c. \uadf8\ubd84\uc744 \ub180\ub9ac\uace0 \uc8fd\uc600\ub358 \uc0ac\ub78c\ub4e4\uae4c\uc9c0\ub3c4 \ub9d0\uc774\uc57c. \ubaa8\ub4e0 \ub098\ub77c, \ubaa8\ub4e0 \uc2dc\ub300\uc758 \uc0ac\ub78c\ub4e4\uc774 \uadf8\uac78 \ubcf4\uace0 \uc2ac\ud37c\ud558\uba74\uc11c \uc790\uae30 \uc637\uc744 \ucc22\uc744 \uac70\uc57c. \uc624, \uc9c4\uc9dc \uadf8\ub807\uac8c \ub420 \uac70\uc57c!"),
("8", "\uc8fc\ub2d8\uc774 \ub531 \uc120\uc5b8\ud558\uc168\uc5b4. \u201c\ub098\ub294 A\ubd80\ud130 Z\uae4c\uc9c0\uc57c. \ub098\ub294 \uc9c0\uae08\ub3c4 \uc788\uace0, \uc804\uc5d0\ub3c4 \uc788\uc5c8\uace0, \uc55e\uc73c\ub85c \uc62c \ud558\ub098\ub2d8\uc774\uc57c. \ub098\ub294 \ubb34\uc18c\ubd88\uc704\uc758 \uac15\ud55c \uc655\uc774\uc57c.\u201d"),
("9-17", "\uc608\uc218\ub2d8 \uc548\uc5d0\uc11c \ub108\ud76c\ub791 \uac19\uc774 \uc2dc\ub828\ub3c4 \uacaa\uace0, \uadf8 \ub098\ub77c\ub791 \ub73b\uac70\uc6b4 \uc778\ub0b4\uc5d0\ub3c4 \ud568\uaed8\ud558\uace0 \uc788\ub294 \ub098 \uc694\ud55c\uc740, \ud558\ub098\ub2d8\uc758 \ub9d0\uc500, \uadf8\ub7ec\ub2c8\uae4c \uc608\uc218\ub2d8\uc758 \uc99d\uc5b8 \ub54c\ubb38\uc5d0 \ubc27\ubaa8\ub77c\ub294 \uc12c\uc5d0 \uc640 \uc788\uc5b4. \uadf8\ub0a0\uc740 \uc8fc\uc77c\uc774\uc5c8\uace0, \ub098\ub294 \uc131\ub839 \uc548\uc5d0\uc11c \uae30\ub3c4\ud558\uace0 \uc788\uc5c8\uc5b4. \uadf8\ub54c \ub4a4\uc5d0\uc11c \ub098\ud314 \uc18c\ub9ac\ucc98\ub7fc \uc644\uc804 \ud06c\uace0 \uc9f8\ub801\uc9f8\ub801\ud55c \ubaa9\uc18c\ub9ac\uac00 \ub4e4\ub824\uc654\uc5b4. \u201c\ub124\uac00 \ubcf4\ub294 \uac78 \ucc45\uc73c\ub85c \uc368. \uadf8\ub9ac\uace0 \uadf8 \uae30\ub85d\uc744 \uc5d0\ubca0\uc18c, \uc11c\uba38\ub098, \ubc84\uac00\ubaa8, \ub450\uc544\ub514\ub77c, \uc0ac\ub370, \ube4c\ub77c\ub378\ube44\uc544, \ub77c\uc624\ub514\uac8c\uc544, \uc774\ub807\uac8c \uc77c\uacf1 \uad50\ud68c\uc5d0 \ubcf4\ub0b4.\u201d \ub098\ub294 \uadf8 \ubaa9\uc18c\ub9ac\uac00 \ub204\uad70\uc9c0 \ubcf4\ub824\uace0 \ub3cc\uc544\uc130\uc5b4. \ubcf4\ub2c8\uae4c \uae08\uc73c\ub85c \ub41c \ucd1b\ub300\uac00 \uc77c\uacf1 \uac1c \uc788\uace0, \uadf8 \uac00\uc6b4\ub370\uc5d0 \uc0ac\ub78c\uc758 \uc544\ub4e4 \uac19\uc740 \ubd84\uc774 \uacc4\uc168\uc5b4. \uae34 \uc637\uc5d0 \uae08\ube44\ub97c \uac00\uc2b4\uc5d0 \ub450\ub974\uace0, \uba38\ub9ac\ub294 \uc644\uc804 \uc0c8\ud558\uc580 \ub208\ucc98\ub7fc \ud76c\uace0, \ub208\uc5d0\uc11c\ub294 \ubd88\uaf43\uc774 \ubfdc\uc5b4\uc838 \ub098\uc624\ub294 \uac83 \uac19\uc558\uc5b4. \ub450 \ubc1c\uc740 \uc6a9\uad11\ub85c\uc5d0\uc11c \ub2ec\uad88\uc9c4 \ub53f\uc1e0 \uac19\uc558\uace0, \ubaa9\uc18c\ub9ac\ub294 \uc6b0\ub808\ucc98\ub7fc \uc6c5\uc7a5\ud588\uc5b4. \uc624\ub978\uc190\uc5d0\ub294 \uc77c\uacf1 \uac1c\uc758 \ubcc4\uc744 \uc950\uace0 \uacc4\uc168\uace0, \uc785\uc5d0\uc11c\ub294 \ub0a0\uce74\ub85c\uc6b4 \uce7c\uc774 \ub098\uc654\uace0, \uc5bc\uad74\uc740 \ubc14\ub85c \uc55e\uc5d0\uc11c \ubcf4\ub294 \ud0dc\uc591 \uac19\uc558\uc5b4. \uc774\uac78 \ubcf8 \ub098\ub294 \uc8fd\uc740 \uc0ac\ub78c\ucc98\ub7fc \uadf8\ubd84 \ubc1c \uc55e\uc5d0 \uc4f0\ub7ec\uc84c\uc5b4. \uadf8\ubd84\uc758 \uc624\ub978\uc190\uc774 \ub098\ub97c \ubd99\uc7a1\uc544 \uc77c\uc73c\ud0a4\uc2dc\uba74\uc11c, \uadf8\ubd84\uc758 \ubaa9\uc18c\ub9ac\uac00 \ub098\ub97c \uc548\uc2ec\uc2dc\ucf1c \uc8fc\uc168\uc5b4."),
("17-20", "\u201c\uc324\uc9c0 \ub9c8. \ub098\ub294 \ucc98\uc74c\uc774\uace0 \ub9c8\uc9c0\ub9c9\uc774\uc57c. \ub098\ub294 \uc0b4\uc544\uc788\uc5b4. \uc8fd\uc5c8\uc9c0\ub9cc \ub2e4\uc2dc \uc0b4\uc544\ub0ac\uace0, \uc774\uc81c \ub0b4 \uc0dd\uba85\uc740 \uc601\uc6d0\ud574. \ub0b4 \uc190\uc5d0 \uc788\ub294 \uc774 \uc5f4\uc1e0\ub4e4 \ubcf4\uc774\uc9c0? \uc774\uac74 \uc8fd\uc74c\uc758 \ubb38\uc744 \uc5f4\uace0 \uc7a5\uadf8\uace0, \uc9c0\uc625\uc758 \ubb38\uc744 \uc5f4\uace0 \uc7a5\uadf8\ub294 \uc5f4\uc1e0\ub4e4\uc774\uc57c. \uc774\uc81c \ub124\uac00 \ubcf4\ub294 \uac78 \uc804\ubd80 \ub2e4 \uae30\ub85d\ud574. \uc9c0\uae08 \uc77c\uc5b4\ub098\ub294 \uc77c\ub4e4\uc774\ub791 \uc55e\uc73c\ub85c \uc77c\uc5b4\ub0a0 \uc77c\ub4e4\uc744 \ub2e4 \uae30\ub85d\ud558\ub77c\ub294 \uac70\uc57c. \ub124\uac00 \ub0b4 \uc624\ub978\uc190\uc5d0\uc11c \ubcf8 \uadf8 \uc77c\uacf1 \ubcc4\uc774\ub791 \uc77c\uacf1 \uae08 \ucd1b\ub300\uc758 \ube44\ubc00\uc774 \ubb54\uc9c0 \uc54c\uace0 \uc2f6\uc5b4? \uc77c\uacf1 \ubcc4\uc740 \ubc14\ub85c \uc77c\uacf1 \uad50\ud68c\uc758 \ucc9c\uc0ac\ub4e4\uc774\uace0, \uc77c\uacf1 \ucd1b\ub300\ub294 \ubc14\ub85c \uadf8 \uc77c\uacf1 \uad50\ud68c\uc57c.\u201d"),
])

# Ch2 KO (24 paras) - mirrors EN
koch(2, [
("1", "\u00a7\uc5d0\ubca0\uc18c\uc5d0\uac8c"),
("1", "\uc5d0\ubca0\uc18c \uad50\ud68c\uc758 \ucc9c\uc0ac\ud55c\ud14c \uc774\ub807\uac8c \uc368\ub77c. \uc624\ub978\uc190\uc5d0 \uc77c\uacf1 \ubcc4\uc744 \uaf2d \uc950\uace0, \ud669\uae08 \uc77c\uacf1 \ucd1b\ubd88 \uc0ac\uc774\ub97c \uac70\ub2c8\ub294 \ubd84\uc774 \ub9d0\uc500\ud558\uc2e0\ub2e4."),
("2-3", "\u201c\ub098\ub294 \ub108\ud76c\uac00 \ud55c \uc77c\uc744 \ub2e4 \uc54c\uc544. \uc5b4\ub824\uc6b4 \uc77c\ub3c4 \ub9c8\ub2e4\ud558\uc9c0 \uc54a\uace0, \ud3ec\uae30\ud558\ub294 \ubc95\ub3c4 \uc5c6\uc5c8\uc9c0. \uc545\ud55c \uac74 \uadf8\ub0e5 \ubabb \ubcf4\uace0, \uc0ac\ub3c4\uc778 \ucc99\ud558\ub294 \uc0ac\ub78c\ub4e4\uc744 \ub2e4 \uc7a1\uc544\ub0b8 \uac83\ub3c4 \uc54c\uc544. \ub108\ud76c\uc758 \ub04c\uae30\uc640 \ub0b4 \uc77c\uc5d0 \ubcf4\uc5ec\uc900 \uc6a9\uae30, \uc808\ub300 \uc548 \uc9c0\uce58\ub294 \uac83\ub3c4 \ub2e4 \uc54c\uc544."),
("4-5", "\u201c\uadf8\ub7f0\ub370 \ub108\ud76c\ub294 \uccab\uc0ac\ub791\uc744 \ubc84\ub838\uc5b4. \uc5b4\uca4c\ub2e4 \uadf8\ub807\uac8c \ub410\uc5b4? \ub108\ud76c\uac00 \uc5bc\ub9c8\ub098 \uba40\ub9ac \uac14\ub294\uc9c0 \uc54c\uc544? \uc644\uc804 \ub8e8\uc2dc\ud37c\uae09\uc73c\ub85c \ucd94\ub77d\ud588\ub2e4\uace0! \ube68\ub9ac \ub3cc\uc544\uc640! \uadf8 \uc18c\uc911\ud588\ub358 \uccab\uc0ac\ub791\uc744 \ub2e4\uc2dc \ucc3e\uc544\uc57c \ud574! \uafc8\ubb3c\uac70\ub9b4 \uc2dc\uac04\uc740 \uc5c6\uc5b4. \uc548 \uadf8\ub7ec\uba74 \ub0b4\uac00 \uadf8 \ud669\uae08 \ucd1b\ub300\uc5d0\uc11c \ub108\ud76c\uc758 \ube5b\uc744 \uaebc\ubc84\ub9b4 \uac70\uc57c."),
("6", "\u201c\uadf8\ub798\ub3c4 \uc774\uac74 \uc798\ud588\uc5b4. \ub108\ud76c\uac00 \ub2c8\uace8\ub77c\ud30c\uac00 \ud558\ub294 \uc9d3\uc744 \uc2eb\uc5b4\ud558\ub294 \uac70 \ub9d0\uc774\uc57c. \ub098\ub3c4 \uadf8\uac78 \uc644\uc804 \uc2eb\uc5b4\ud558\uac70\ub4e0."),
("7", "\u201c\uadc0 \uc788\ub294 \uc0ac\ub78c\uc740 \uc798 \ub4e4\uc5b4. \uc131\ub839\ub2d8\uc774 \uad50\ud68c\ub4e4\uc5d0\uac8c \ud558\uc2dc\ub294 \ub9d0\uc500\uc744 \ub4e4\uc5b4\uc57c \ud574. \uc774\uae30\ub294 \uc0ac\ub78c\uc740 \ub0b4\uac00 \ud558\ub098\ub2d8\uc758 \uacfc\uc218\uc6d0\uc5d0\uc11c \ub530\uc628 \uc0dd\uba85\ub098\ubb34 \uc5f4\ub9e4\ub85c \ucc28\ub9b0 \uc794\uce58\uc5d0 \ucd08\ub300\ud560 \uac70\uc57c.\u201d"),
("8", "\u00a7\uc11c\uba38\ub098\uc5d0\uac8c"),
("8", "\uc11c\uba38\ub098 \uad50\ud68c \ucc9c\uc0ac\ud55c\ud14c \uc774\ub807\uac8c \uc368\ub77c. \ucc98\uc74c\uc774\uc790 \ub9c8\uc9c0\ub9c9\uc774\uc2e0 \ubd84, \uc8fd\uc5c8\ub2e4\uac00 \ub2e4\uc2dc \uc0b4\uc544\ub098\uc2e0 \ubd84\uc774 \ub9d0\uc500\ud558\uc2e0\ub2e4."),
("9", "\u201c\ub098\ub294 \ub108\ud76c\uc758 \uace0\ud1b5\uc774\ub791 \uac00\ub09c\uc744 \ub2e4 \uc54c\uc544. \uc9c4\uc9dc \ub05d\ub3c4 \uc5c6\ub294 \uace0\ud1b5\uc5d0 \uc644\uc804 \uac00\ub09c\ud55c \uac70 \ub9d0\uc774\uc57c. \uadfc\ub370 \uc0ac\uc2e4 \ub108\ud76c\ub294 \uc644\uc804 \ubd80\uc790\uc778 \uac83\ub3c4 \uc54c\uc544. \uc790\uce6d \uc720\ub300\uc778\uc774\ub77c\uace0 \uc798\ub09c \ucc99\ud558\ub294 \uc0ac\ub78c\ub4e4, \uc0ac\uc2e4\uc740 \uc0ac\ud0c4\uc758 \ub620\ub9c8\ub2c8\ub4e4\uc778\ub370, \uac50\ub124\uac00 \ud558\ub294 \uac70\uc9d3\ub9d0\ub3c4 \ub2e4 \uc54c\uc544."),
("10", "\u201c\uc55e\uc73c\ub85c \uacaa\uc744 \uc77c \ubb34\uc11c\uc6cc\ud558\uc9c0 \ub9c8. \uc815\uc2e0 \ubc14\uc9dd \ucc28\ub824! \ub9c8\uadc0\uac00 \ub108\ud76c\ub97c \uac10\uc625\uc5d0 \ub358\uc838 \ub123\uc744 \uac74\ub370, \uadf8 \uc2dc\ud5d8\uc740 \uc5f4\ud750\uc774\uba74 \ub05d\ub098. \ubaa9\uc228\uc744 \uc783\ub354\ub77c\ub3c4 \uc808\ub300 \ud3ec\uae30\ud558\uc9c0 \ub9c8. \ubbff\uc74c\uc73c\ub85c \ub05d\uae4c\uc9c0 \ubc84\ud2f0\uba74, \ub0b4\uac00 \ub108\ud76c\uc5d0\uac8c \uc8fc\ub824\uace0 \uc900\ube44\ud55c \uc0dd\uba85\uc758 \uba74\ub958\uad00\uc774 \uc788\uc5b4."),
("11", "\u201c\uadc0 \uc788\ub294 \uc0ac\ub78c\uc740 \uc798 \ub4e4\uc5b4. \uc131\ub839\ub2d8\uc774 \uad50\ud68c\ub4e4\uc5d0\uac8c \ud558\uc2dc\ub294 \ub9d0\uc500\uc744 \ub4e4\uc5b4\uc57c \ud574. \uadf8\ub9ac\uc2a4\ub3c4\uc5d0\uac8c \ubd99\uc5b4\uc11c \uc774\uae30\ub294 \uc0ac\ub78c\uc740 \ub9c8\uadc0\ub791 \uc8fd\uc74c\uc5d0\uac8c\uc11c \uc548\uc804\ud574.\u201d"),
("12", "\u00a7\ubc84\uac00\ubaa8\uc5d0\uac8c"),
("12", "\ubc84\uac00\ubaa8 \uad50\ud68c \ucc9c\uc0ac\ud55c\ud14c \uc774\ub807\uac8c \uc368\ub77c. \ub0a0\uce74\ub85c\uc6b4 \uce7c\uc744 \uac00\uc9c0\uc2e0 \ubd84\uc774 \uce7c\uc744 \ube7c \ub4e4\uace0 \ub9d0\uc500\ud558\uc2e0\ub2e4. \uadf8 \uc785\uc5d0\uc11c \uce7c \uac19\uc740 \ub9d0\uc500\uc774 \ub098\uc634."),
("13", "\u201c\ub098\ub294 \ub108\ud76c\uac00 \uc5b4\ub514 \uc0ac\ub294\uc9c0 \uc54c\uc544. \uc644\uc804 \uc0ac\ud0c4\uc758 \ubcf8\uac70\uc9c0 \ubc14\ub85c \ubc11\uc5d0 \uc0b4\uace0 \uc788\uc794\uc544. \uadfc\ub370\ub3c4 \ub108\ud76c\ub294 \uc6a9\uac10\ud558\uac8c \ub0b4 \uc774\ub984\uc744 \ubd99\ub4e4\uace0 \uc788\uc5c8\uc5b4. \ucd5c\uc545\uc758 \uc0c1\ud669\uc5d0\uc11c\ub3c4, \uc0ac\ud0c4 \uad6c\uc5ed\uc5d0\uc11c \ub0b4 \ucda9\uc2e4\ud55c \uc99d\uc778 \uc548\ub514\ubc14\uac00 \uc8fd\uc784\ub2f9\ud560 \ub54c\ub3c4, \ub108\ud76c\ub294 \ud55c \ubc88\ub3c4 \ub0b4 \uc774\ub984\uc744 \ubaa8\ub978 \ucc99\ud558\uc9c0 \uc54a\uc558\uc9c0."),
("14-15", "\u201c\uadfc\ub370 \uc65c \ubc1c\ub78c\uc744 \ub530\ub974\ub294 \uc0ac\ub78c\ub4e4\uc744 \ubc1b\uc544\uc918? \ubc1c\ub78c\uc774 \uc6b0\ub9ac \uc6d0\uc218\uc600\ub358 \uac70 \uae30\uc5b5 \uc548 \ub098? \uadf8\uac00 \ubc1c\ub77d\uc744 \uc720\ud639\ud574\uc11c \ub098\uc05c \uc794\uce58\ub97c \uc5f4\uace0 \uc774\uc2a4\ub77c\uc5d8 \ubc31\uc131\ub4e4\uc744 \ub9dd\ud558\uac8c \ud558\ub824 \ud588\ub358 \uac70 \ub9d0\uc774\uc57c. \uc65c \ub611\uac19\uc740 \uc9d3\uc744 \ud558\ub294 \ub2c8\uace8\ub77c\ud30c\ub97c \ub0c5\ub46c?"),
("16", "\u201c\uc774\uc81c \uadf8\ub9cc\ud574! \ub354 \uc774\uc0c1 \uac50\ub124\ub97c \ub0c5\ub450\uc9c0 \ub9c8. \ub0b4\uac00 \uace7 \uac08 \uac70\uc57c. \uac50\ub124\ub294 \uc9c4\uc9dc \ub108\ubb34 \uc2eb\uc5b4. \ub0b4 \ub9d0\uc500\uc758 \uce7c\ub85c \ub2e4 \ucc22\uc5b4\ubc84\ub9b4 \uac70\uc57c."),
("17", "\u201c\uadc0 \uc788\ub294 \uc0ac\ub78c\uc740 \uc798 \ub4e4\uc5b4. \uc131\ub839\ub2d8\uc774 \uad50\ud68c\ub4e4\uc5d0\uac8c \ud558\uc2dc\ub294 \ub9d0\uc500\uc744 \ub4e4\uc5b4\uc57c \ud574. \uc774\uae30\ub294 \uc0ac\ub78c\uc5d0\uac8c\ub294 \ub0b4\uac00 \uac70\ub8e9\ud55c \ub9cc\ub098\ub97c \uc904 \uac70\uc57c. \uadf8\ub9ac\uace0 \uc0c8 \uc774\ub984, \ub108\ud76c\ub9cc\uc758 \ube44\ubc00 \uc0c8 \uc774\ub984\uc774 \uc0c8\uaca8\uc9c4 \uae68\ub057\ud558\uace0 \ubd80\ub4dc\ub7ec\uc6b4 \ub3cc\ub3c4 \uc904\uac8c.\u201d"),
("18", "\u00a7\ub450\uc544\ub514\ub77c\uc5d0\uac8c"),
("18", "\ub450\uc544\ub514\ub77c \uad50\ud68c \ucc9c\uc0ac\ud55c\ud14c \uc774\ub807\uac8c \uc368\ub77c. \ub208\uc740 \ubd88\uaf43 \uac19\uace0 \ubc1c\uc740 \uc6a9\uad11\ub85c\uc5d0\uc11c \ub2ec\uad6c \ub53f \uac19\uc740 \ud558\ub098\ub2d8\uc758 \uc544\ub4e4\uc774 \ub9d0\uc500\ud558\uc2e0\ub2e4."),
("19", "\u201c\ub098\ub294 \ub108\ud76c\uac00 \ub098\ub97c \uc704\ud574 \ud558\ub294 \uc77c\uc744 \ub2e4 \uc54c\uc544. \uadf8 \uc0ac\ub791, \ubbff\uc74c, \ubd09\uc0ac, \ub04c\uae30 \uc644\uc804 \uc778\uc0c1\uc801\uc774\uc57c! \uc9c4\uc9dc \ub300\ub2e8\ud574! \uac8c\ub2e4\uac00 \ub0a0\uc774 \uac08\uc218\ub85d \ub354 \uc5f4\uc2ec\ud788 \ud558\ub354\ub77c."),
("20-23", "\u201c\uadfc\ub370 \uc65c \uc790\uce6d \uc608\uc5b8\uc790\ub77c\ub294 \uc774\uc138\ubca8\uc774 \ub0b4 \uc18c\uc911\ud55c \uc885\ub4e4\uc744 \uc720\ud639\ud574\uc11c \uc2ed\uc790\uac00\ub97c \ubc30\uc2e0\ud558\uace0 \uc790\uae30\ub4e4 \uc88b\uc740 \ub300\ub85c \ubbff\uac8c \ub9cc\ub4dc\ub294 \uac78 \ubcf4\uace0\ub9cc \uc788\uc5b4? \ub0b4\uac00 \uadf8 \uc5ec\uc790\uc5d0\uac8c \ub3cc\uc544\uc62c \uae30\ud68c\ub97c \uc92c\ub294\ub370, \uc790\uae30 \uc2e0 \uc7a5\uc0ac\ub97c \uadf8\ub9cc\ub458 \uc0dd\uac01\uc774 \uc5c6\uc5b4. \uadf8 '\uc139\uc2a4 \uc885\uad50' \ub180\uc774\ub97c \ud558\ub294 \uadf8 \uc5ec\uc790\uc640 \uadf8 \uc5ec\uc790\uc758 \ub3d9\ub8cc\ub4e4\uc744 \ub2e4 \ubcd1\ub4e4\uac8c \ud560 \uac70\uc57c. \uadf8 \uc6b0\uc0c1\uc22d\ubc30 \uc74c\ud589\uc73c\ub85c \ud0dc\uc5b4\ub09c \uc544\uc774\ub4e4\ub3c4 \ub2e4 \uc8fd\uc77c \uac70\uc57c. \uadf8\ub7ec\uba74 \ub0b4\uac00 \uac89\ubaa8\uc2b5\ub9cc \ubcf4\uace0 \ud310\ub2e8 \uc548 \ud55c\ub2e4\ub294 \uac78 \ubaa8\ub4e0 \uad50\ud68c\uac00 \uc54c\uac8c \ub418\uaca0\uc9c0. \ub098\ub294 \ub9c8\uc74c\uc18d\uc744 \ub2e4 \uaff0\ub6ab\uc5b4 \ubcf4\uace0, \ub108\ud76c\uac00 \ubfcc\ub9b0 \ub300\ub85c \uac70\ub450\uac8c \ud560 \uac70\uc57c."),
("24-25", "\u201c\ub108\ud76c \ub098\uba38\uc9c0 \ub450\uc544\ub514\ub77c \uc0ac\ub78c\ub4e4, \uc774\ub7f0 \ubd88\ubc95\uc801\uc778 \uc9d3\uc774\ub791 \uc0c1\uad00\uc5c6\uace0, \ubb50 \ub300\ub2e8\ud55c \uac83\ucc98\ub7fc \ud3ec\uc7a5\ud558\ub294 \ub9c8\uadc0 \uc7a5\ub09c\uc9c8\uc744 \uc2eb\uc5b4\ud558\ub294 \ub108\ud76c\ub294 \uc548\uc2ec\ud574\ub3c4 \ub3fc. \ub0b4\uac00 \ub108\ud76c\uc758 \uc0b6\uc744 \uc9c0\uae08\ubcf4\ub2e4 \ub354 \ud798\ub4e4\uac8c \ud558\uc9c0\ub294 \uc54a\uc744\uac8c. \ub0b4\uac00 \uac08 \ub54c\uae4c\uc9c0 \ub108\ud76c\uac00 \uac00\uc9c4 \uadf8 \uc9c4\ub9ac\ub97c \uaf49 \ubd99\ub4e4\uace0 \uc788\uc5b4."),
("26-28", "\u201c\uc774\uae30\ub294 \ubaa8\ub4e0 \uc0ac\ub78c, \ub05d\uae4c\uc9c0 \ud3ec\uae30 \uc548 \ud558\ub294 \ubaa8\ub4e0 \uc0ac\ub78c\uc5d0\uac8c \ub0b4\uac00 \uc904 \ubcf4\uc0c1\uc740 \uc774\uac70\uc57c. \ub108\ud76c\ub294 \ubbfc\uc871\ub4e4\uc744 \ub2e4\uc2a4\ub9ac\uac8c \ub420 \uac70\uace0, \ubaa9\uc790\ub791 \uc655\ucc98\ub7fc \uc1e0 \uc9c0\ud321\uc774 \uac19\uc740 \uad73\uac74\ud55c \ud1b5\uce58\ub97c \ud560 \uac70\uc57c. \uadf8\ub4e4\uc758 \uc800\ud56d\uc740 \uc9c8\uadf8\ub987\ucc98\ub7fc \uc27d\uac8c \uae68\uc9c8 \uac70\uc57c. \uc774\uac74 \ub0b4 \uc544\ubc84\uc9c0\uac00 \ub098\ud55c\ud14c \uc8fc\uc2e0 \uc120\ubb3c\uc778\ub370, \ub0b4\uac00 \ub108\ud76c\uc5d0\uac8c \ub118\uaca8\uc8fc\ub294 \uac70\uc57c. \uadf8\ub9ac\uace0 \uc0c8\ubcbd\ubcc4\ub3c4 \ub364\uc73c\ub85c \uc904\uac8c!\u201d"),
("29", "\u201c\uadc0 \uc788\ub294 \uc0ac\ub78c\uc740 \uc798 \ub4e4\uc5b4. \uc131\ub839\ub2d8\uc774 \uad50\ud68c\ub4e4\uc5d0\uac8c \ud558\uc2dc\ub294 \ub9d0\uc500\uc744 \ub4e4\uc5b4\uc57c \ud574.\u201d"),
])

# Ch3 KO (14 paras)
# Ch3 KO (21 paras) - mirrors EN
koch(3, [
("1", "\u00a7\uc0ac\ub370\uc5d0\uac8c"),
("1", "\uc0ac\ub370\uc5d0, \uad50\ud68c\uc758 \ucc9c\uc0ac\ud55c\ud14c \uc774\ub807\uac8c \uc368\ub77c. \ud558\ub098\ub2d8\uc758 \uc77c\uacf1 \uc601\uc744 \ud55c \uc190\uc5d0 \uac00\uc9c0\uace0, \uc77c\uacf1 \ubcc4\uc744 \ub2e4\ub978 \uc190\uc73c\ub85c \uaf2d \uc7a1\uace0 \uacc4\uc2e0 \ubd84\uc774 \ub9d0\uc500\ud558\uc2e0\ub2e4."),
("2-3", "\u201c\ub0b4\uac00 \ub108\ud76c \uc77c\uc744 \ub2e4 \ud6e4\ub744\uc5b4\ubcf4\uace0 \uc788\uc5b4. \ud65c\uae30\ucc28\uace0 \uc5f4\uc815\uc801\uc774\ub77c\ub294 \uc18c\ubb38은 \ub0ac\uc9c0\ub9cc, \uc0ac\uc2e4\uc740 \uc8fd\uc5b4\uc788\uc5b4, \uc644\uc804\ud788 \uc8fd\uc5b4\uc788\ub2e4\uace0! \u201c\uc77c\uc5b4\ub098! \uae52\uac8c \uc228\uc26c\uc5b4! \uc544\uc9c1 \uc0b6\uc774 \ub0a8\uc544\uc788\uc744\uc9c0\ub3c4 \ubaa8\ub984. \uadf8\ub7f0\ub370 \ub108\ud76c \ubc14\ube60\ub300\ub294 \uac83\ub9cc \ubcf4\uba74 \uc0b6\uc744 \ub290\ub084\uc9c0 \ubabb\ud558\uaca0\uc5b4. \ud558\ub098\ub2d8\uc758 \uc77c\uc740 \uc544\ubb34\uac83\ub3c4 \uc644\uc131\ub418\uc9c0 \ubabb\ud588\uc5b4. \ub108\ud76c \uc0c1\ud669\uc740 \uc808\ubc15\ud574. \uc608\uc804\uc5d0 \uc190\uc5d0 \uc950\uc5c8\ub358 \uc120\ubb3c, \uadc0\ub85c \ub4e3\uc5c8\ub358 \ub9d0\uc500\uc744 \uc0dd\uac01\ud574\ubd10\u2014\ub2e4\uc2dc \uaf2d \uc7a1\uace0 \ud558\ub098\ub2d8\uaed8 \ub3cc\uc544\uac00. \uc774\ubd88\uc744 \uba38\ub9ac\uae4c\uc9c0 \ub4e4\uc5b4\uc4f0\uace0 \uc790\uba74\uc11c, \ud558\ub098\ub2d8\uc744 \ubab0\ub77c\ub294 \ucc99\ud558\uba74, \ub0b4\uac00 \ub108\ud76c\uac00 \uac00\uc7a5 \uc608\uc0c1 \ubabb\ud560 \ub54c \ub3cc\uc544\uc640\uc11c, \uc0bc\uacbd\uc5d0 \ub3c4\ub451\ucc98\ub7fc \ub108\ud76c \uc0b6\uc5d0 \uce68\uc785\ud560 \uac70\uc57c.\u201d"),
("4", "\u201c\uadf8\ub7f0\ub370 \uc0ac\ub370\uc5d0\ub294 \uc544\uc9c1 \uc608\uc218\ub2d8\uc744 \ub530\ub974\ub294 \uc0ac\ub78c\ub4e4\uc774 \uba87 \uba87 \uc788\uc5b4. \uc138\uc0c1\uc758 \ub354\ub7ec\uc6b4 \ubc29\uc2dd\uc5d0 \ube60\uc838\uc11c \uc790\uae30\ub97c \ub9dd\uce58\uc9c0 \uc54a\uc740 \uc0ac\ub78c\ub4e4\uc774\uc57c. \uadf8 \uc0ac\ub78c\ub4e4\uc740 \ub098\uc640 \ud568\uaed8 \ud37c\ub808\uc774\ub4dc\uc5d0\uc11c \uac77\uc744 \uac70\uc57c! \uadf8\ub9cc\ud55c \uac00\uce58\uac00 \uc788\ub2e4\ub294 \uac78 \uc99d\uba85\ud588\uc5b4!\u201d"),
("5", "\u201c\uc774\uae30\ub294 \uc0ac\ub78c\uc740 \uc2b9\ub9ac \ud37c\ub808\uc774\ub4dc\uc5d0\uc11c \ud589\uc9c4\ud560 \uac70\uc57c. \uadf8 \uc774\ub984\uc740 \uc0dd\uba85\ucc45\uc5d0 \uc9c0\uc6cc\uc9c0\uc9c0 \uc54a\uace0 \ub0a8\uc744 \uac70\uc57c. \ub0b4\uac00 \uadf8\ub4e4\uc744 \ub370\ub9ac\uace0 \uc62c\ub77c\uac00\uc11c \ub0b4 \uc544\ubc84\uc9c0\uc640 \ucc9c\ucaac\ub4e4 \uc55e\uc5d0\uc11c \uc774\ub984\uc744 \ubd88\ub7ec\uc904 \uac70\uc57c.\u201d"),
("6", "\u201c\uadc0 \uc788\ub294 \uc0ac\ub78c\uc740 \uae68\uc5b4\uc788\ub098? \ub4e4\uc5b4. \ubc14\ub78c \ub9d0\uc500, \uad50\ud68c\ub4e4\uc744 \ud5a5\ud574 \ubd80\ub294 \uc131\ub839\ub2d8\uc758 \ub9d0\uc500\uc744 \ub4e4\uc5b4\ubd10.\u201d"),
("7", "\u00a7\ube4c\ub77c\ub378\ube44\uc544\uc5d0\uac8c"),
("7", "\ube4c\ub77c\ub378\ube44\uc544\uc5d0, \uad50\ud68c\uc758 \ucc9c\uc0ac\ud55c\ud14c \uc774\ub807\uac8c \uc368\ub77c. \uac70\ub8e9\ud558\uace0 \uc9c4\uc2e4\ud558\uc2e0 \ubd84\u2014\ub2e4\uc787\uc758 \uc5f4\uc1e0\ub97c \uc190\uc5d0 \uac00\uc9c0\uace0, \uc5f4\uba74 \uc544\ubb34\ub3c4 \ub2eb\uc9c0 \ubabb\ud558\uace0, \ub2eb\uc73c\uba74 \uc544\ubb34\ub3c4 \uc5f4\uc9c0 \ubabb\ud558\ub294 \ubd84\uc774 \ub9d0\uc500\ud558\uc2e0\ub2e4."),
("8", "\u201c\ub0b4\uac00 \ub108\ud76c\uac00 \ubb34\uc5c7\uc744 \ud588\ub294\uc9c0 \ubcf4\uc558\uc5b4. \uc774\uc81c \ub0b4\uac00 \ubb34\uc5c7\uc744 \ud588\ub294\uc9c0 \ubcf4\uc544. \ub0b4\uac00 \ub108\ud76c \uc55e\uc5d0 \ubb38\uc744 \uc5f4\uc5b4\ub208\uace0, \uc544\ubb34\ub3c4 \uadf8 \ubb38\uc744 \ub2eb\uc9c0 \ubabb\ud574. \ub108\ud76c\ub294 \ud798\uc774 \uc5c6\uc5b4\ub3c4 \ub0b4 \ub9d0\uc500\uc744 \uc9c0\ucf30\uace0, \ud798\ub4e4 \ub54c \ub0b4 \uc774\ub984\uc744 \ubd80\uc778\ud558\uc9c0 \uc54a\uc558\uc5b4.\u201d"),
("9", "\u201c\uadf8\ub9ac\uace0 \ubcf4\uc544. \uc790\uae30\ub4e4\uc744 \ucc38 \ubbff\uc74c\uc758 \uc0ac\ub78c\uc774\ub77c\uace0 \ub9d0\ud558\uc9c0\ub9cc \uc804\ud600 \uadf8\ub807\uc9c0 \uc54a\uc740 \uc0ac\ub78c\ub4e4, \uc2e4\uc81c \uc18c\uc18d\uc740 \uc0ac\ud0c4\uc758 \ubaa8\uc784\uc5d0 \uc788\ub294 \uac00\uc9dc\ub4e4\u2014\ub0b4\uac00 \uadf8\ub4e4\uc758 \uac00\uba74\uc744 \ubc97\uae38 \uac70\uc57c. \uadf8\ub4e4\uc774 \uc5b4\쩔 \uc218 \uc5c6\uc774 \uc778\uc815\ud558\uac8c \ub420 \uac70\uc57c. \ub0b4\uac00 \ub108\ud76c\ub97c \uc0ac\ub791\ud588\ub2e4\ub294 \uac78.\u201d"),
("10", "\u201c\ub108\ud76c\uac00 \uc5f4\uc815\uc801\uc778 \uc778\ub0b4\ub85c \ub0b4 \ub9d0\uc500\uc744 \uc9c0\ucf30\uc73c\ub2c8, \ub0b4\uac00 \ub108\ud76c\ub97c \uc9c0\ucf1c\uc904 \uac70\uc57c. \uace7 \uc62c \uadf8 \uc2dc\ud5d8\uc758 \uc2dc\uac04, \uc628 \uc138\uc0c1\uc5d0 \uc62c \uadf8 \ud070 \uc2dc\ud5d8\uc5d0\uc11c, \ubaa8\ub4e0 \ub0a8\uc790, \uc5ec\uc790, \uc544\uc774\uac00 \uc2dc\ud5d8\ubc1b\uc744 \ub54c, \ub0b4\uac00 \ub108\ud76c\ub97c \uc548\uc804\ud558\uac8c \uc9c0\ucf1c\uc904\uac8c.\u201d"),
("11", "\u201c\ub0b4\uac00 \uace7 \uac00! \uadf8\uac8c \uc624\uae30 \uc804\uc5d0 \ub108\ud76c\uac00 \uc9c0\uae08 \uac00\uc9c0\uace0 \uc788\ub294 \uac83\uc744 \ub2e8\ub2e8\ud788 \uc7a1\uc544. \uadf8\ub798\uc57c \ub204\uad6c\ub3c4 \ub108\ud76c\uc758 \uba74\ub958\uad00\uc744 \ubed0\uc557\uc9c0 \ubabb\ud574.\u201d"),
("12", "\u201c\uc774\uae30\ub294 \uc0ac\ub78c\uc744 \ub0b4 \ud558\ub098\ub2d8\uc758 \uc131\uc804\uc5d0 \uae30\ub465\ucc98\ub7fc \uc138\uc6b8 \uac70\uc57c. \uc601\uc6d0\ud55c \uba85\uc608\uc758 \uc790\ub9ac\uc57c. \uadf8\ub9ac\uace0 \ub0b4\uac00 \uadf8 \uae30\ub465\uc5d0 \uc774\ub984\ub4e4\uc744 \uc0c8\uae38 \uac70\uc57c. \ub0b4 \ud558\ub098\ub2d8\uc758 \uc774\ub984, \ud558\ub098\ub2d8\uc758 \ub3c4\uc2dc\uc758 \uc774\ub984\u2014\ud558\ub298\uc5d0\uc11c \ub0b4\ub824\uc624\ub294 \uc0c8 \uc608\ub8e8\uc0b4\ub818\u2014\uadf8\ub9ac\uace0 \ub098\uc758 \uc0c8 \uc774\ub984.\u201d"),
("13", "\u201c\uadc0 \uc788\ub294 \uc0ac\ub78c\uc740 \uae68\uc5b4\uc788\ub098? \ub4e4\uc5b4. \ubc14\ub78c \ub9d0\uc500, \uad50\ud68c\ub4e4\uc744 \ud5a5\ud574 \ubd80\ub294 \uc131\ub839\ub2d8\uc758 \ub9d0\uc500\uc744 \ub4e4\uc5b4\ubd10.\u201d"),
("14", "\u00a7\ub77c\uc624\ub514\uac8c\uc544\uc5d0\uac8c"),
("14", "\ub77c\uc624\ub514\uac8c\uc544\uc5d0, \uad50\ud68c\uc758 \ucc9c\uc0ac\ud55c\ud14c \uc774\ub807\uac8c \uc368\ub77c. \ud558\ub098\ub2d8\uc758 \uc608\uc2a4, \ubbff\uc744 \uc218 \uc788\uace0 \uc815\ud655\ud55c \uc99d\uc778, \ud558\ub098\ub2d8\uc774 \ucc3d\uc870\ud558\uc2e0 \ubaa8\ub4e0 \uac83\uc758 \uccab\uc5f4\ub9e4\uac00 \ub9d0\ud55c\ub2e4."),
("15-17", "\u201c\ub0b4\uac00 \ub108\ud76c\ub97c \uc18d\uc18d\ub4e4\uc774 \ub2e4 \uc54c\uc544. \uadf8\ub9ac\uace0 \ub9c8\uc74c\uc5d0 \ub4e0 \uac83\uc774 \uac70\uc758 \uc5c6\uc5b4. \ub108\ud76c\ub294 \ucc28\uac11\uc9c0\ub3c4 \uc54a\uace0, \ub728\uac81\uc9c0\ub3c4 \uc54a\uc544. \ucc28\uac11\uac70\ub098 \ub728\uac81\uac70\ub098 \ud558\uba74 \uc5bc\ub9c8\ub098 \uc88b\uc744\uae4c! \ub108\ud76c\ub294 \uc2e0\uc120\ud558\uace0, \uace0\uc774\uace0 \uc788\uc5b4. \ub098\ub97c \ud1a0\ud560 \uac83 \uac19\uc544. \ub108\ud76c\ub294 \uc790\ub791\ud574, \u2018\ub0b4\uac00 \ubd80\uc790\uc57c, \ub09c \uc644\ubcbd\ud574, \uc544\ubb34\ud55c\ud14c\ub3c4 \uc544\uc26c\uc6b4 \uac83 \uc5c6\uc5b4\u2019\ub77c\uace0 \ub9d0\ud558\uc9c0\ub9cc, \uc0ac\uc2e4\uc740 \ubd88\uc30d\ud55c \uac70\uc9c0, \ub208\uba3c \uac70\uc9c0\uc57c. \uac70\uc9c0\uc774\uace0, \ubc97\uace0 \ub2e4\ub2cc \uac70\uc57c.\u201d"),
("18", "\u201c\ub0b4\uac00 \ub108\ud76c\ud55c\ud14c \ud558\uace0 \uc2f6\uc740 \ub9d0이 \uc788\uc5b4. \ub0b4\ud55c\ud14c\uc11c \uae08\uc744 \uc0ac. \uc81c\ub828\uc18c\uc758 \ubd88\uc744 \uac70\uce5c \uae08\uc73c\ub85c. \uadf8\ub7ec\uba74 \ub108\ud76c\uac00 \ubd80\uc720\ud574\uc9c8 \uac70\uc57c. \ub0b4\ud55c\ud14c\uc11c \uc637\uc744 \uc0ac. \ud558\ub298\uc5d0\uc11c \ub514\uc790\uc778\ud55c \uc637\uc73c\ub85c. \ub108\ud76c\uac00 \ubc18\ubc8c\uac70\ub9ac\ub85c \ub2e4\ub2cc \uc9c0 \uc624\ub798\ub410\uc796\uc544. \uadf8\ub9ac\uace0 \ub0b4\ud55c\ud14c\uc11c \ub208\uc57d\uc744 \uc0ac\uc11c \ub208\uc5d0 \ubc1c\ub77c. \uadf8\ub7ec\uba74 \ubcfc \uc218 \uc788\uc744 \uac70\uc57c, \uc9c4\uc9dc\ub85c \ubcfc \uc218 \uc788\uac8c \ub420 \uac70\uc57c.\u201d"),
("19", "\u201c\ub0b4\uac00 \uc0ac\ub791\ud558\ub294 \uc0ac\ub78c\uc740, \ub098\ub294 \uadf8 \uc0ac\ub78c\uc744 \ucc45\uc784\uc9c0\uace0\u2014\uc7a0\uc7a0\ud558\uace0 \ubc14\ub85c\uc7a1\uace0 \uc778\ub3c4\ud574\uc11c \uadf8 \uc0ac\ub78c\uc774 \ucd5c\uace0\uc758 \uc0b6\uc744 \uc0b4\uac8c \ud574. \uc790, \uc77c\uc5b4\ub098! \ubc29\ud5a5\uc744 \ud2ad! \ud558\ub098\ub2d8\uc744 \ucad3\uc544\uac00!\u201d"),
("20-21", "\u201c\ub0b4\uac00 \ubb38 \uc55e\uc5d0 \uc11c \uc788\ub2e4\uace0 \uc0c1\uc0c1\ud574\ubd10. \ub0b4\uac00 \ubb38\uc744 \ub450\ub4dc\ub824. \ub204\uad6c\ub4e0\uc9c0 \ub0b4 \ubaa9\uc18c\ub9ac\ub97c \ub4e3\uace0 \ubb38\uc744 \uc5f4\uba74, \ub0b4\uac00 \ub4e4\uc5b4\uac00\uc11c \uadf8 \uc0ac\ub78c\uacfc \ud568\uaed8 \uc800\ub141\uc744 \uba39\uc744 \uac70\uc57c. \uc774\uae30\ub294 \uc0ac\ub78c\uc740 \ub0b4 \uc606\uc5d0 \uc549\uc544\uc11c \uba54\uc778 \ud14c\uc774\ube14\uc5d0\uc11c \uba39\uac8c \ub420 \uac70\uc57c. \ub0b4\uac00 \uc774\uae30\uace0 \ub0b4 \uc544\ubc84\uc9c0 \uc606\uc5d0 \uba85\uc608\uc758 \uc790\ub9ac\uc5d0 \uc549\uc740 \uac83\ucc98\ub7fc \ub9d0\uc774\uc57c. \uadf8\uac8c \ub0b4\uac00 \uc774\uae30\ub294 \uc790\ub4e4\ud55c\ud14c \uc8fc\ub294 \uc120\ubb3c\uc774\uc57c!\u201d"),
("22", "\u201c\uadc0 \uc788\ub294 \uc0ac\ub78c\uc740 \uae68\uc5b4\uc788\ub098? \ub4e4\uc5b4. \ubc14\ub78c \ub9d0\uc500, \uad50\ud68c\ub4e4\uc744 \ud5a5\ud574 \ubd80\ub294 \uc131\ub839\ub2d8\uc758 \ub9d0\uc500\uc744 \ub4e4\uc5b4\ubd10.\u201d"),
])

# Ch4 KO - REPLACED BELOW

# Ch5 KO - REPLACED BELOW

# Ch6 KO - REPLACED BELOW

# Ch7 KO (8 paras)
koch(7, [
("1", "\u00a7\uc778\uce5c \ud558\ub098\ub2d8"),
("1", "\uadf8\ub9ac\uace0 \ub0b4\uac00 \ubcf4\uc558\uc5b4. \ub124 \ucc9c\uc0ac\uac00 \ub545\uc758 \ub124 \ubaa8\ud29c\uae30\uc5d0 \uc11c \uc788\uc5c8\uc5b4. \uadf8\ub4e4\uc740 \ub545\uc758 \ub124 \ubc14\ub78c\uc744 \uc7a1\uace0 \uc788\uc5c8\uc5b4. \ubc14\ub78c\uc774 \ub545\uc5d0\ub3c4, \ubc14\ub2e4\uc5d0\ub3c4, \ub098\ubb34\uc5d0\ub3c4 \ubd88\uc9c0 \uc54a\uac8c \ud558\ub824\uace0 \ub9d0\uc774\uc57c."),
("2-3", "\uadf8\ub9ac\uace0 \ub2e4\ub978 \ucc9c\uc0ac\uac00 \ud574 \ub728\ub294 \uacf3\uc5d0\uc11c \uc62c\ub77c\uc624\ub294 \uac78 \ubcf4\uc558\uc5b4. \uadf8 \ucc9c\uc0ac\ub294 \uc0b4\uc544\uacc4\uc2e0 \ud558\ub098\ub2d8\uc758 \ub3c4\uc7a5\uc744 \uac00\uc9c0\uace0 \uc788\uc5c8\uc5b4. \uadf8 \ucc9c\uc0ac\uac00 \ub545\uacfc \ubc14\ub2e4\ub97c \ud574\ud558\ub3c4\ub85d \uad8c\uc138\ub97c \ubc1b\uc740 \ub124 \ucc9c\uc0ac\ud55c\ud14c \ud070 \ubaa9\uc18c\ub9ac\ub85c \ub9d0\ud588\uc5b4. \u201c\uc6b0\ub9ac\uac00 \uc6b0\ub9ac \ud558\ub098\ub2d8\uc758 \uc885\ub4e4\uc758 \uc774\ub9c8\uc5d0 \ub3c4\uc7a5\uc744 \ucc0d\uae30\uae4c\uc9c0\ub294 \ub545\uc774\ub098 \ubc14\ub2e4\ub098 \ub098\ubb34\ub97c \ud574\ud558\uc9c0 \ub9c8\ub77c!\u201d"),
("4-8", "\uadf8\ub9ac\uace0 \ub0b4\uac00 \ub4e4\uc5c8\uc5b4. \ub3c4\uc7a5 \ucc0d\uc740 \uc0ac\ub78c\uc758 \uc218\uac00 \uc2ed\uc0ac\ub9cc \uc0ac\ucc9c\uba85\uc774\uc57c. \uc774\uc2a4\ub77c\uc5d8\uc758 \ubaa8\ub4e0 \uc9c0\ud30c\uc5d0\uc11c \ub3c4\uc7a5 \ucc0d\uc740 \uc0ac\ub78c\ub4e4\uc774\uc57c. \uc720\ub2e4 \uc9c0\ud30c\uc5d0\uc11c \uc2ed\uc774\ub9cc \uc774\ucc9c\uba85, \ub974\uc6b4 \uc9c0\ud30c\uc5d0\uc11c \uc2ed\uc774\ub9cc \uc774\ucc9c\uba85, \uac13 \uc9c0\ud30c\uc5d0\uc11c \uc2ed\uc774\ub9cc \uc774\ucc9c\uba85, \uc544\uc154 \uc9c0\ud30c\uc5d0\uc11c \uc2ed\uc774\ub9cc \uc774\ucc9c\uba85, \ub0a9\ub2ec\ub9ac \uc9c0\ud30c\uc5d0\uc11c \uc2ed\uc774\ub9cc \uc774\ucc9c\uba85, \ubbf8\ub0ab\uc138 \uc9c0\ud30c\uc5d0\uc11c \uc2ed\uc774\ub9cc \uc774\ucc9c\uba85, \uc2dc\ubbc0\uc628 \uc9c0\ud30c\uc5d0\uc11c \uc2ed\uc774\ub9cc \uc774\ucc9c\uba85, \ub808\uc704 \uc9c0\ud30c\uc5d0\uc11c \uc2ed\uc774\ub9cc \uc774\ucc9c\uba85, \uc789\uc0ac\uac08 \uc9c0\ud30c\uc5d0\uc11c \uc2ed\uc774\ub9cc \uc774\ucc9c\uba85, \uc2a4\ube14\ub860 \uc9c0\ud30c\uc5d0\uc11c \uc2ed\uc774\ub9cc \uc774\ucc9c\uba85, \uc694\uc149 \uc9c0\ud30c\uc5d0\uc11c \uc2ed\uc774\ub9cc \uc774\ucc9c\uba85, \ubca0\ub0d0\ubbfc \uc9c0\ud30c\uc5d0\uc11c \uc2ed\uc774\ub9cc \uc774\ucc9c\uba85\uc774\ub77c\uace0 \ub4e4\uc5c8\uc5b4."),
("9-12", "\uadf8\ub9ac\uace0 \ub0b4\uac00 \ubcf4\uc558\uc5b4. \uc544\ubb34\ub3c4 셀 \uc218 \uc5c6\uc744 \ub9cc\ud07c \ud070 \ubb34\ub9ac\uac00 \uc788\uc5c8\uc5b4. \uac01 \ub098\ub77c\uc640 \uc871\uc871\uacfc \ubc31\uc131\uacfc \uc5b8\uc5b4\uc5d0\uc11c \uc628 \uc0ac\ub78c\ub4e4\uc774\uc57c. \uadf8\ub4e4\uc740 \ubcf4\uc88c\uc640 \uc591 \uc55e\uc5d0 \uc11c \uc788\uc5c8\uc5b4. \ud770 \ub450\ub8e8\ub9c8\uae30\ub97c \uc785\uace0, \uc190\uc5d0\ub294 \uc885\ub824\ub098\ubb34 \uac00\uc9c0\ub97c \ub4e4\uace0 \uc788\uc5c8\uc5b4. \uadf8\ub4e4\uc740 \ud070 \ubaa9\uc18c\ub9ac\ub85c \uc678\ucce4\uc5b4. \u201c\uad6c\uc6d0\uc740 \ubcf4\uc88c\uc5d0 \uc549\uc73c\uc2e0 \uc6b0\ub9ac \ud558\ub098\ub2d8\uacfc \uc591\ud55c\ud14c \uc788\ub2e4!\u201d \ubaa8\ub4e0 \ucc9c\uc0ac\uac00 \ubcf4\uc88c\uc640 \uc7a5\ub85c\ub4e4\uacfc \ub124 \uc0dd\ubb3c \uc8fc\uc704\uc5d0 \uc11c\uc11c, \ubcf4\uc88c \uc55e\uc5d0 \uc5e4\ub4dc\ub824 \ud558\ub098\ub2d8\uaed8 \uacbd\ubc30\ud588\uc5b4. \u201c\uc544\uba58! \ucc2c\uc591\uacfc \uc601\uad11\uacfc \uc9c0\ud61c\uc640 \uac10\uc0ac\uc640 \uc874\uadc0\uc640 \ub2a5\ub825\uacfc \ud798\uc774 \uc6b0\ub9ac \ud558\ub098\ub2d8\uaed8 \uc601\uc6d0\ud558\uae38!\u201d"),
("13-14", "\uadf8\ub54c \uc7a5\ub85c \uc911\uc5d0 \ud55c \ubd84\uc774 \ub098\ud55c\ud14c \ubb3c\uc5c8\uc5b4. \u201c\ud770 \ub450\ub8e8\ub9c8\uae30\ub97c \uc785\uc740 \uc774 \uc0ac\ub78c\ub4e4\uc740 \ub204\uad6c\uc9c0? \uc5b4\ub514\uc11c \uc654\uc9c0?\u201d \ub0b4\uac00 \ub300\ub2f5\ud588\uc5b4. \u201c\uc7a5\ub85c\ub2d8, \ub2f9\uc2e0\uc774 \uc54c\uc796\uc544\uc694.\u201d \uadf8\ubd84\uc774 \ub9d0\ud588\uc5b4. \u201c\uc774 \uc0ac\ub78c\ub4e4\uc740 \ud070 \ud658\ub09c\uc744 \uacaa\uc5b4\ub0b8 \uc0ac\ub78c\ub4e4\uc774\uc57c. \uadf8\ub4e4\uc740 \uc591\uc758 \ud53c\ub85c \uc790\uae30\ub4e4\uc758 \ub450\ub8e8\ub9c8\uae30\ub97c \ube68\uc557\uc5b4.\u201d"),
("14-17", "\u201c\uadf8\ub798\uc11c \uadf8\ub4e4\uc740 \ud558\ub098\ub2d8\uc758 \ubcf4\uc88c \uc55e\uc5d0 \uc788\uace0, \uadf8\ubd84\uc758 \uc131\uc804\uc5d0\uc11c \ubc24\ub0ae \uadf8\ubd84\uc744 \uc12c\uae30\ub294 \uac83\uc774\uc57c. \ubcf4\uc88c\uc5d0 \uc549\uc73c\uc2e0 \ubd84\uc774 \uadf8\ub4e4 \uc704\uc5d0 \uc7a5\ub9c9\uc744 \ud3bc \uac83\uc774\uc57c. \uadf8\ub4e4\uc740 \ub2e4\uc2dc\ub294 \uc8fc\ub9ac\uc9c0 \uc54a\uace0, \ubaa9\ub9c8\ub974\uc9c0\ub3c4 \uc54a\uc744 \uac83\uc774\uc57c. \ud574\ub3c4, \uadf8 어떤 \ubb34b더\uc704\ub3c4 \uadf8\ub4e4\uc744 \ub364\uce58\uc9c0 \uc54a\uc744 \uac83\uc774\uc57c. \uc65c\ub0d0\ud558\uba74 \ubcf4\uc88c \uac00\uc6b4\ub370\uc5d0 \uc788\ub294 \uc591\uc774 \uadf8\ub4e4\uc758 \ubaa9\uc790\uac00 \ub418\uc5b4, \uc0dd\uba85\uc758 \ubb3c \uc0d8\uc73c\ub85c \uadf8\ub4e4\uc744 \uc778\ub3c4\ud560 \uac83\uc774\uae30 \ub54c\ubb38\uc774\uc57c. \uadf8\ub9ac\uace0 \ud558\ub098\ub2d8\uc774 \uadf8\ub4e4 \ub208\uc5d0\uc11c \ubaa8\ub4e0 \ub208\ubb3c\uc744 b2�\uc544\uc8fc\uc2e4 \uac83\uc774\uc57c.\u201d"),
])

# Ch8 KO - REPLACED BELOW

# Ch9 KO - REPLACED BELOW

# Ch10 KO - REPLACED BELOW

# Ch11 KO - REPLACED BELOW

# Ch12 KO - REPLACED BELOW

# Ch13 KO - REPLACED BELOW

# Ch14 KO - REPLACED BELOW

# Ch11 KO (10 paras) - CORRECTED
koch(11, [
("1-2", "§두 증인"),
("1-2", "나한테 지팡이 같은 측정 막대가 주어졌어. “일어나서 하나님의 성전과 제단과 그 안에서 경배하는 사람들을 재. 그런데 성전 밖에 있는 뜰은 재지 말고 내버려둬. 그건 이방인들한테 주어졌거든. 그들이 거룩한 도시를 마흔두 달 동안 짓밟을 거야.”"),
("3-6", "“한편, 내가 내 두 증인을 내세울 거야. 굵은 베옷을 입고, 천이백육십 일 동안 예언할 거야.” 이 두 사람은 두 감람나무이자 두 촛대야. 땅의 주 앞에 서 있는 사람들이지. 누가 그들을 해하려 하면, 입에서 불이 나와서 원수들을 삼켜버려. 누가 그들을 해하려 하면, 꼭 이렇게 죽어야 해. 이 사람들한테는 하늘이 닫혀서 예언하는 동안 비가 오지 않게 할 권세가 있어. 또 물을 피로 바꾸고, 원하는 만큼 땅을 온갖 재앙으로 칠 권세도 있어."),
("7-10", "“그들이 증언을 마치면, 무저갱에서 올라오는 짐승이 그들과 싸워서 이기고 그들을 죽일 거야. 그들의 시체는 큰 도시의 대로에 버려질 거야. 영적으로 소돔과 이집트라고 불리는 그 도시야. 바로 거기서 그들의 주도 십자가에 못 박히셨지. 여러 백성과 족속과 언어와 나라에서 온 사람들이 사흘 반 동안 그들의 시체를 구경하고, 무덤에 묻는 걸 허락하지 않을 거야. 땅에 사는 사람들은 그 두 사람이 죽었다고 파티를 열고 선물을 주고받을 거야. 이 두 예언자가 땅에 사는 사람들을 너무 괴롭혔거든.”"),
("11", "“그런데 사흘 반이 지나자, 하나님의 생명의 영이 그들 안에 들어갔어. 그들이 벌떡 일어섰지. 그걸 본 사람들은 혼비백산했어.”"),
("12-13", "하늘에서 우렁찬 목소리가 들렸어. “여기로 올라와!” 그래서 그들이 구름을 타고 하늘로 올라갔어. 원수들이 그걸 지켜보고 있었어. 바로 그 순간 큰 지진이 일어났어. 도시의 10분의 1이 무너졌고, 칠천 명이 죽었어. 살아남은 사람들은 벌벌 떨면서 하늘의 하나님께 영광을 돌렸어."),
("14", "둘째 재앙이 지나갔어. 셋째 재앙이 바로 코앞이야."),
("15-18", "§마지막 나팔"),
("15-18", "일곱째 천사가 나팔을 불었어. 하늘에서 우렁찬 목소리들이 합창했어. “세상의 왕국이 우리 주와 그분의 그리스도의 왕국이 되었다! 그분이 영원히 다스리실 거야!” 보좌 앞에 앉아 있던 스물네 장로가 엎드려 하나님께 경배했어. “지금 계시고 전에 계셨던 전능하신 주 하나님이시여, 감사합니다! 당신이 큰 권세를 잡으시고 왕이 되셨기 때문입니다. 민족들이 분노했지만, 당신의 진노가 임했고, 죽은 자들을 심판할 때가 왔고, 당신의 종 예언자들과 거룩한 백성과 당신의 이름을 두려워하는 작은 자와 큰 자에게 상 주실 때가 왔고, 땅을 망치는 자들을 망하게 하실 때가 왔습니다!”"),
("19", "하늘에 있는 하나님의 성전 문이 활짝 열렸어. 그분의 성전 안에 언약궤가 보였어. 번개가 번쩍이고, 목소리가 나고, 우레가 울리고, 지진이 일어나고, 큰 우박이 쏟아졌어."),
])

# Ch12 KO (6 paras) - CORRECTED
koch(12, [
("1-2", "§여자와 그녀의 아들과 용"),
("1-2", "하늘에서 큰 표적이 나타났어. 온통 햇빛으로 옷 입은 여자였어. 발 아래에는 달이 있었고, 머리에는 열두 별로 된 면류관이 있었어. 그 여자는 임신 중이었고, 해산의 고통으로 비명을 지르고 있었어."),
("3-4", "그리고 첫 번째 표적 옆에 또 다른 표적이 나타났어. 크고 불타는 용이었어! 일곱 머리와 열 뿔이 있었고, 머리들에는 일곱 면류관이 있었어. 용의 꼬리가 하늘 별들의 3분의 1을 쓸어다가 땅에 던졌어. 용이 해산하려는 여자 앞에 자리 잡았어. 아이가 태어나자마자 삼키려고."),
("5-6", "여자가 아들을 낳았어. 쇠지팡이로 모든 민족을 다스릴 사내아이야. 그 아이는 하나님과 그분의 보좌로 들려 올라갔어. 여자는 광야로 도망갔어. 하나님이 준비해 두신 피난처가 있었거든. 거기서 천이백육십 일 동안 돌봄을 받을 거야."),
("7-12", "하늘에서 전쟁이 터졌어. 미가엘과 그분의 천사들이 용과 싸웠어. 용과 그분의 천사들도 맞섰지만, 당해내지 못했어. 하늘에서 그들의 자리도 사라졌어. 큰 용이 내쫓겼어. 옛 뱀, 마귀라고도 하고 사탄이라고도 불리는 자, 온 세상을 속이는 자야. 땅으로 내쫓겼고, 그분의 천사들도 함께 내쫓겼어. 하늘에서 우렁찬 목소리를 들었어. “이제 구원이 왔어! 우리 하나님의 권세와 나라와 그분의 그리스도의 권위가 임했어! 우리 형제들을 고소하던 자가 쫓겨났거든. 밤낮 우리 하나님 앞에서 그들을 고소하던 자야. 그들이 어린 양의 피와 자기들의 증언의 말씀으로 그를 이겼어. 그들은 죽음 앞에서도 자기 목숨을 아끼지 않았어. 그러니 하늘아, 하늘에 사는 자들아, 기뻐하라! 하지만 땅과 바다야, 조심해! 마귀가 너희에게 내려갔거든. 자기 때가 얼마 남지 않은 걸 알고 펄펄 뛰면서.”"),
("13-17", "용이 자기가 땅으로 내쫓긴 걸 보고, 사내아이를 낳은 여자를 쫓아갔어. 여자에게 큰 독수리의 두 날개가 주어졌어. 광야에 있는 자기 처소로 날아가려고. 거기서 뱀을 피해 한 때와 두 때와 반 때 동안 돌봄을 받을 거야. 뱀이 입에서 물을 강처럼 여자 뒤에 쏟았어. 여자를 물에 떠내려가게 하려고. 그런데 땅이 여자를 도왔어. 땅이 입을 벌려서 용이 입에서 쏟은 강을 삼켰어. 용이 여자에게 격분해서, 여자의 남은 자손과 싸우러 갔어. 하나님의 계명을 지키고 예수의 증언을 굳게 잡은 사람들이야."),
])

# Ch13 KO (9 paras) - CORRECTED
koch(13, [
("1-2", "§바다에서 나온 짐승"),
("1-2", "용이 바다 해변에 섰어. 내가 봤어. 바다에서 짐승이 올라오는 걸. 열 뿔과 일곱 머리가 있었어. 뿔들에는 열 면류관이 있었고, 머리들에는 신성모독의 이름들이 있었어. 내가 본 짐승은 표범 같았고, 발은 곰의 발 같았고, 입은 사자의 입 같았어. 용이 자기 권세와 보좌와 큰 권위를 짐승에게 주었어."),
("3-4", "짐승의 머리 중 하나가 치명상을 입은 것 같았는데, 그 치명상이 나았어. 온 땅이 놀라서 짐승을 따랐어. 사람들이 용에게 경배했어. 용이 짐승에게 권세를 주었기 때문이야. 또 짐승에게 경배하면서 말했어. “누가 이 짐승과 같으냐? 누가 그와 맞서 싸울 수 있느냐?”"),
("5-8", "짐승에게 큰소리치고 신성모독하는 입이 주어졌어. 마흔두 달 동안 제멋대로 할 권세가 주어졌어. 짐승이 입을 벌려 하나님을 모독했어. 그분의 이름과 그분의 처소와 하늘에 사는 사람들을 모독했어. 거룩한 백성과 싸워서 이길 권세도 주어졌어. 모든 족속과 백성과 언어와 민족을 다스릴 권세도 주어졌어. 땅에 사는 모든 사람이 짐승에게 경배할 거야. 세상이 창조된 이후로 죽임당한 어린 양의 생명책에 이름이 기록되지 않은 사람들이야."),
("9-10", "이 말 듣고 있니? 자업자득이야. 남을 잡아가는 사람은 자기도 잡혀갈 거야. 칼로 죽이는 사람은 자기도 칼로 죽을 거야. 하나님의 백성은 인내와 믿음으로 버텨야 해."),
("11-12", "§땅 밑에서 나온 짐승"),
("11-12", "내가 봤어. 또 다른 짐승이 땅에서 올라오는 걸. 어린 양처럼 두 뿔이 있었는데, 용처럼 말했어. 첫째 짐승의 모든 권세를 첫째 짐승 앞에서 행사했어. 땅과 그 안에 사는 사람들로 하여금 첫째 짐승에게 경배하게 했어. 첫째 짐승은 치명상을 입었다가 나았거든."),
("13-17", "이 둘째 짐승이 마술 같은 표적들을 일으켰어. 사람들 앞에서 하늘에서 불이 땅으로 내려오게 해서 사람들을 홀렸어. 첫째 짐승 앞에서 행하도록 허락받은 표적들로 땅에 사는 사람들을 속였어. 땅에 사는 사람들한테 말했어. 칼에 상처를 입었다가 살아난 짐승을 위해 우상을 만들라고. 그 짐승의 우상에게 숨을 불어넣어서 말도 하게 하고, 그 우상에게 경배하지 않는 사람은 다 죽이게 할 권세가 주어졌어. 그리고 모든 사람—작은 자와 큰 자, 부자와 가난한 자, 자유인과 종—에게 오른손이나 이마에 표를 받게 했어. 그 표가 있는 사람, 곧 짐승의 이름이나 그 이름의 수를 가진 사람 외에는 아무도 사고팔지 못하게 했어."),
("18", "수수께끼를 풀어봐. 머리를 맞대고 이 숫자의 뜻을 알아내 봐. 짐승의 수야. 사람의 수거든. 그 수는 666이야."),
])

# Ch14 KO (13 paras) - CORRECTED
koch(14, [
("1-2", "§완벽한 제물"),
("1-2", "내가 봤어—숨이 멎을 것 같았어!—어린 양이 시온 산에 서 계셨어. 그분과 함께 십사만 사천 명이 있었어. 그들의 이마에는 어린 양의 이름과 아버지의 이름이 새겨져 있었어. 하늘에서 소리를 들었어. 폭포 소리 같았고, 우레 소리 같았어. 내가 들은 소리는 거문고를 타는 사람들이 거문고를 타는 것 같았어."),
("2-5", "그들이 보좌 앞과 네 생물 앞과 장로들 앞에서 새 노래를 불렀어. 땅에서 구속받은 십사만 사천 명 외에는 아무도 그 노래를 배울 수 없었어. 이 사람들은 여자와 더불어 자신을 더럽히지 않았어. 순결한 사람들이거든. 어린 양이 가는 곳이면 어디든 따라가는 사람들이야. 사람들 중에서 구속받아서 하나님과 어린 양에게 첫 열매가 된 사람들이야. 그들의 입에는 거짓이 없었고, 흠잡을 데가 없었어."),
("6-7", "§하늘에서 온 목소리들"),
("6-7", "내가 봤어. 또 다른 천사가 하늘 한가운데를 날아가는 걸. 땅에 사는 사람들—모든 나라와 족속과 언어와 백성—에게 전할 영원한 기쁜 소식을 가지고 있었어. 큰 목소리로 말했어. “하나님을 두려워하고 그분께 영광을 돌려라! 그분의 심판 시간이 왔거든. 하늘과 땅과 바다와 물의 샘을 만드신 분께 경배하라!”"),
("8", "둘째 천사가 뒤따라 외쳤어. “무너졌다, 무너졌다, 큰 바벨론이 무너졌다! 모든 나라에게 자기 음행의 진노의 포도주를 마시게 한 도시야!”"),
("9-11", "셋째 천사가 뒤따라 큰 목소리로 외치며 경고했어. “누구든지 짐승과 그 우상에게 경배하고 이마나 손에 표를 받으면, 그 사람도 하나님의 진노의 포도주를 마실 거야. 그분의 진노의 잔에 희석하지 않고 부은 포도주야. 거룩한 천사들과 어린 양 앞에서 불과 유황으로 고통받을 거야. 그 고통의 연기가 영원히 올라갈 거야. 짐승과 그 우상에게 경배하고 그 이름의 표를 받는 사람은 밤낮 쉼을 얻지 못할 거야.”"),
("12", "한편, 성도들은 열정적인 인내로 서 있어. 하나님의 계명을 지키고, 예수에 대한 믿음을 굳게 잡고."),
("13", "하늘에서 목소리를 들었어. “기록하라. 지금부터 주 안에서 죽는 사람들은 복이 있어.” 성령이 말씀하셔. “그래, 그들이 수고에서 쉬게 될 거야. 그들의 행위가 그들을 따를 거야.”"),
("14-16", "§추수 때"),
("14-16", "내가 올려다봤어. 숨이 멎었어!—흰 구름과 구름 위에 인자 같은 분이 앉아 계셨어. 머리에는 금 면류관을 쓰고, 손에는 날카로운 낫을 들고 계셨어. 또 다른 천사가 성전에서 나와서 구름 위에 앉으신 분께 큰 목소리로 외쳤어. “낫을 휘둘러 거둬들여라! 거둘 때가 왔거든. 땅의 곡식이 익었어.” 그래서 구름 위에 앉으신 분이 낫을 땅에 휘둘렀어. 땅이 거두어졌어."),
("17-18", "또 다른 천사가 하늘에 있는 성전에서 나왔어. 그 천사도 날카로운 낫을 가지고 있었어. 불을 다스리는 권세를 가진 또 다른 천사가 제단에서 나와서, 날카로운 낫을 가진 천사에게 큰 목소리로 외쳤어. “날카로운 낫을 휘둘러 땅의 포도송이를 거둬들여라! 포도가 익었어.”"),
("19-20", "천사가 낫을 땅에 휘둘러 땅의 포도를 거두어 하나님의 진노의 큰 포도주 틀에 던졌어. 포도주 틀이 성 밖에서 밟혔어. 틀에서 피가 흘러나왔어. 말의 고삐까지 찼어. 천육백 스타디온에 퍼졌어."),
])

# Ch15 KO (6 paras)
koch(15, [
("1", "§마지막 일곱 재앙"),
("1", "하늘에서 또 다른 크고 놀라운 표적을 봤어. 일곱 천사가 마지막 일곱 재앙을 가지고 있었어. 이걸로 하나님의 진노가 끝나거든."),
("2-4", "불이 섞인 유리 바다 같은 걸 봤어. 짐승과 그 우상과 그 이름의 수를 이긴 사람들이 유리 바다 위에 서 있었어. 하나님의 거문고를 가지고 있었어. 모세의 노래와 어린 양의 노래를 불렀어. “전능하신 주 하나님이시여, 당신의 행위는 크고 놀랍습니다! 만국의 왕이시여, 당신의 길은 의롭고 참되십니다! 주여, 누가 당신을 두려워하지 않고 당신의 이름에 영광을 돌리지 않겠습니까? 당신만이 거룩하십니다. 모든 나라가 와서 당신 앞에 경배할 겁니다. 당신의 의로운 심판이 드러났기 때문입니다!”"),
("5-8", "그 후에 내가 봤어. 하늘에 있는 증거의 장막 성전이 열렸어. 일곱 재앙을 가진 일곱 천사가 성전에서 나왔어. 깨끗하고 빛나는 세마포를 입었고, 가슴에는 금 띠를 둘렀어. 네 생물 중 하나가 일곱 천사에게 일곱 금 대접을 주었어. 영원히 사시는 하나님의 진노가 가득했어. 성전이 하나님의 영광과 권세에서 나오는 연기로 가득 찼어. 일곱 천사의 일곱 재앙이 끝나기까지는 아무도 성전에 들어갈 수 없었어."),
])

# Ch16 KO - REPLACED BELOW

# Ch17 KO - REPLACED BELOW

# Ch18 KO (11 paras)
koch(18, [
("1-8", "§바벨론의 멸망"),
("1-8", "그 후에 내가 봤어. 다른 천사가 하늘에서 내려오는 걸. 큰 권세를 가지고 있었어. 땅이 그분의 영광으로 빛났어. 큰 목소리로 외쳤어. “무너졌다! 큰 바벨론이 무너졌다! 귀신들의 처소, 모든 더러운 영의 소굴, 모든 더럽고 미운 새의 소굴이 되었어! 모든 나라가 그 여자의 음행의 진노의 포도주를 마셨고, 땅의 왕들이 그 여자와 음행했고, 땅의 상인들이 그 여자의 사치의 권세로 부자가 되었거든.” 하늘에서 또 다른 목소리를 들었어. “내 백성아, 거기서 나와라! 그 여자의 죄에 참여하지 말고, 그 여자가 받을 재앙을 받지 않게 하라. 그 여자의 죄가 하늘에 닿았고, 하나님이 그 여자의 불의를 기억하셨거든. 그 여자가 너희에게 한 대로 갚아줘라! 그 행위의 두 배를 갚아줘라! 그 여자가 섞은 잔에 두 배를 섞어줘라! 그 여자가 영광과 사치를 누린 만큼, 괴로움과 슬픔을 줘라! 그 여자가 마음속으로 말했거든. ‘나는 여왕으로 앉아 있어. 과부가 아니야. 슬픔을 겪지 않을 거야.’ 그러니 하루에 그 여자의 재앙이 임할 거야. 죽음과 슬픔과 기근이야. 불에 태워질 거야. 그 여자를 심판하시는 주 하나님은 강하시거든.”"),
("9-10", "그 여자와 음행하고 사치하던 땅의 왕들이 그 여자를 위해 울고 가슴을 칠 거야. 그 여자가 타는 연기를 볼 때 말이야. 그 여자의 고통이 두려워서 멀리 서서 말할 거야. “화가 있다, 화가 있다, 큰 도시여! 강한 도시 바벨론이여! 한 시간에 네 심판이 임했구나!”"),
("11-17", "땅의 상인들이 그 여자를 위해 울고 슬퍼할 거야. 그들의 상품을 사는 사람이 아무도 없거든. 금, 은, 보석, 진주, 세마포, 자주색 천, 비단, 주홍색 천, 모든 향나무, 상아로 만든 온갖 물건, 값진 나무와 놋과 철과 대리석으로 만든 온갖 물건, 계피, 향료, 향, 몰약, 유향, 포도주, 기름, 고운 밀가루, 밀, 소, 양, 말, 수레, 종들, 사람들의 영혼까지. “네 영혼이 탐하던 열매가 너를 떠났고, 모든 맛있고 화려한 것들이 너를 떠났어. 사람들이 다시는 그것들을 찾지 못할 거야.” 이런 것들을 팔아 부자가 된 상인들이 그 여자의 고통이 두려워서 멀리 서서 울고 슬퍼하며 말할 거야. “화가 있다, 화가 있다, 큰 도시여! 세마포와 자주색과 주홍색 옷을 입고, 금과 보석과 진주로 치장했던 도시여! 한 시간에 이렇게 큰 부가 사라졌구나!”"),
("17-19", "모든 선장과 항해자와 선원들과 바다에서 일하는 사람들이 멀리 서서, 그 여자가 타는 연기를 보고 외쳤어. “어떤 도시가 이 큰 도시와 같았느냐?” 그들이 머리에 먼지를 뿌리고 울고 슬퍼하며 외쳤어. “화가 있다, 화가 있다, 큰 도시여! 바다에 배를 가진 모든 사람이 그 여자의 보물로 부자가 되었는데, 한 시간에 망했구나!”"),
("20", "하늘아, 그 여자를 두고 기뻐하라! 성도들과 사도들과 예언자들아, 기뻐하라! 하나님이 너희를 위해 그 여자를 심판하셨거든!"),
("21-24", "강한 천사 하나가 맷돌 같은 큰 돌을 들어 바다에 던지며 말했어. “큰 도시 바벨론이 이렇게 세차게 던져질 거야. 다시는 찾을 수 없을 거야. 거문고 타는 사람들과 노래하는 사람들과 피리 부는 사람들과 나팔 부는 사람들의 소리가 다시는 네 안에서 들리지 않을 거야. 어떤 기술자도 다시는 네 안에서 찾지 못할 거야. 맷돌 소리가 다시는 네 안에서 들리지 않을 거야. 등불 빛이 다시는 네 안에서 비치지 않을 거야. 신랑과 신부의 목소리가 다시는 네 안에서 들리지 않을 거야. 네 상인들이 땅의 큰 자들이었고, 네 마술로 모든 나라가 속았거든. 예언자들과 성도들과 땅에서 죽임당한 모든 사람들의 피가 그 여자 안에서 발견되었어.”"),
])

# Ch19 KO (10 paras)
koch(19, [
("1-3", "§할렐루야 소리"),
("1-3", "그 후에 내가 들었어. 하늘에서 큰 무리의 우렁찬 목소리가 있었어. “할렐루야! 구원과 영광과 권세가 우리 하나님께 있다! 그분의 심판은 참되고 의롭다! 음행으로 땅을 망하게 한 큰 음녀를 심판하셨고, 그 여자의 손에 있는 자기 종들의 피를 갚아주셨거든.” 그들이 두 번째로 말했어. “할렐루야! 그 여자가 타는 연기가 영원히 올라간다!”"),
("4", "스물네 장로와 네 생물이 엎드려 보좌에 앉으신 하나님께 경배했어. “아멘! 할렐루야!”"),
("5", "보좌에서 목소리가 났어. “우리 하나님을 찬양하라! 그분의 모든 종들아, 그분을 두려워하는 작은 자와 큰 자들아!”"),
("6-8", "큰 무리의 목소리 같은 것, 많은 물소리 같은 것, 큰 우레소리 같은 것을 들었어. “할렐루야! 전능하신 주 우리 하나님이 다스리신다! 기뻐하고 즐거워하자! 그분께 영광을 돌리자! 어린 양의 혼인 잔치가 왔고, 그분의 신부가 준비했거든!” 신부에게 빛나고 깨끗한 세마포를 입게 허락하셨어. 그 세마포는 성도들의 의로운 행위야."),
("9", "천사가 나한테 말했어. “기록하라. 어린 양의 혼인 잔치에 초대받은 사람들은 복이 있어.” 또 나한테 말했어. “이것은 하나님의 참된 말씀이다.”"),
("10", "내가 그 천사의 발 앞에 엎드려 경배하려고 했어. 그런데 천사가 나한테 말했어. “그러지 마! 나도 너와 같은 종이야. 예수의 증언을 가진 네 형제들과 같은 종이라고. 하나님께 경배하라! 예수의 증언은 예언의 영이거든.”"),
("11-16", "§흰 말과 그 말을 타신 분"),
("11-16", "하늘이 열린 걸 봤어. 흰 말이 있었어! 그 말을 타신 분은 신실하고 참되시다고 불리셔. 의로 심판하고 싸우셔. 그분의 눈은 불꽃 같고, 머리에는 많은 면류관이 있으셔. 그분만이 아시는 이름이 새겨져 있으셔. 피에 적신 옷을 입으셨어. 그분의 이름은 하나님의 말씀이라고 불리셔. 하늘의 군대들이 흰 말을 타고, 깨끗하고 흰 세마포를 입고 그분을 따랐어. 그분의 입에서는 날카로운 검이 나와. 그걸로 민족들을 치고, 쇠지팡이로 다스리실 거야. 전능하신 하나님의 맹렬한 진노의 포도주 틀을 밟으셔. 그분의 옷과 넓적다리에는 이름이 쓰여 있어. “만왕의 왕, 만주의 주.”"),
("17-18", "천사가 해 안에 서 있는 걸 봤어. 하늘 한가운데를 나는 모든 새에게 큰 목소리로 외쳤어. “와서 하나님의 큰 잔치에 모여라! 왕들의 살과 장수들의 살과 용사들의 살과 말들과 그 말을 탄 사람들의 살을 먹어라! 자유인과 종, 작은 자와 큰 자, 모든 사람의 살을 먹어라!”"),
("19-21", "짐승과 땅의 왕들과 그들의 군대들이 모여서 말 타신 분과 그분의 군대와 싸우려는 걸 봤어. 짐승이 잡혔어. 그 앞에서 표적을 행하던 거짓 예언자도 함께 잡혔어. 그 표적들로 짐승의 표를 받은 사람들과 그 우상에게 경배하는 사람들을 속였거든. 이 둘이 산 채로 불과 유황으로 타는 못에 던져졌어. 나머지는 말 타신 분의 입에서 나오는 검으로 죽임을 당했어. 모든 새가 그들의 살로 배불리 먹었어."),
])

# Ch20 KO (6 paras)
koch(20, [
("1-3", "§천 년"),
("1-3", "천사가 하늘에서 내려오는 걸 봤어. 무저갱의 열쇠와 큰 쇠사슬을 가지고 있었어. 용을 잡았어. 옛 뱀, 곧 마귀고 사탄이야! 천 년 동안 결박해서 무저갱에 던지고 닫고 봉인했어. 천 년이 끝날 때까지 민족들을 속이지 못하게 하려고. 그 후에는 잠시 풀려나야 해."),
("4-6", "보좌들을 봤어. 심판할 권세를 받은 사람들이 그 보좌에 앉았어. 예수의 증언과 하나님의 말씀 때문에 목 베임을 당한 사람들의 영혼도 봤어. 짐승이나 그 우상에게 경배하지 않고, 이마나 손에 표를 받지 않은 사람들이야. 그들이 살아서 그리스도와 함께 천 년 동안 왕 노릇 했어. 나머지 죽은 사람들은 천 년이 끝날 때까지 살지 못했어. 이것이 첫째 부활이야. 첫째 부활에 참여하는 사람은 복이 있고 거룩해. 둘째 사망이 그들을 다스릴 권세가 없어! 그들은 하나님과 그리스도의 제사장이 되어 천 년 동안 그분과 함께 왕 노릇 할 거야."),
("7-10", "천 년이 끝나면 사탄이 감옥에서 풀려날 거야. 민족들을 속이려고 나갈 거야. 땅의 네 모퉁이에 있는 곡과 마곡을 속여서 전쟁을 위해 모으려고. 그들의 수는 바다의 모래 같아. 그들이 땅의 넓은 곳으로 올라와서 성도들의 진과 사랑받는 도시를 에워쌌어. 그런데 하늘에서 불이 내려와서 그들을 삼켰어. 그들을 속이던 마귀가 불과 유황 못에 던져졌어. 짐승과 거짓 예언자도 있는 곳이야. 거기서 밤낮 영원히 괴로움을 받을 거야."),
("11-15", "§심판"),
("11-15", "큰 흰 보좌와 그 위에 앉으신 분을 봤어. 그분의 낯을 피해서 하늘과 땅이 사라졌어. 그들을 둘 곳이 없었어. 죽은 사람들, 큰 자와 작은 자가 보좌 앞에 서 있는 걸 봤어. 책들이 펴졌어. 또 다른 책이 펴졌어. 생명책이야. 죽은 사람들이 책에 기록된 대로, 자기들의 행위대로 심판을 받았어. 바다가 그 안에 있는 죽은 사람들을 내주었고, 사망과 지옥도 그 안에 있는 죽은 사람들을 내주었어. 각 사람이 자기들의 행위대로 심판을 받았어. 사망과 지옥이 불못에 던져졌어. 이것이 둘째 사망이야—불못 말이야. 생명책에 이름이 기록되지 않은 사람은 불못에 던져졌어."),
])

# Ch21 KO (10 paras)
koch(21, [
("1", "§모든 것이 새로워지다"),
("1", "새 하늘과 새 땅을 봤어. 처음 하늘과 처음 땅이 사라졌고, 바다도 없었어."),
("2", "거룩한 도시 새 예루살렘이 하늘에서 하나님께로부터 내려오는 걸 봤어. 남편을 위해 단장한 신부처럼 준비되어 있었어."),
("3-5", "보좌에서 큰 목소리를 들었어. “봐! 봐! 하나님이 사람들 사이에 이사 오셔서 함께 사셔! 그들은 그분의 백성이 되고, 그분은 그들의 하나님이 되실 거야. 그분이 그들의 눈에서 모든 눈물을 닦아주실 거야. 죽음이 영원히 사라질 거야—눈물도, 울음도, 아픔도 사라질 거야—처음 것들이 다 사라졌거든.” 보좌에 앉으신 분이 말씀하셨어. “봐! 내가 모든 것을 새롭게 해. 다 기록해—한 마디 한 마디 믿을 수 있고 정확하거든.”"),
("6-8", "그분이 말씀하셨어. “다 이루었다. 나는 A부터 Z까지야. 나는 시작이고, 나는 끝이야. 목마른 사람에게 생명수 샘에서 공짜로 줄 거야. 이기는 사람은 이 모든 것을 상속받을 거야. 내가 그들에게 하나님이 되고, 그들은 내 아들과 딸이 될 거야. 하지만 나머지—비겁하고 믿음 없는 자, 타락한 자와 살인자, 음행하는 자와 마술하는 자, 우상 숭배자와 모든 거짓말쟁이—그들에게는 불과 유황 못이야. 둘째 사망!”"),
("9-12", "§빛의 도시"),
("9-12", "마지막 일곱 재앙이 가득한 일곱 대접을 가졌던 일곱 천사 중 하나가 나한테 말했어. “이리 와. 신부, 어린 양의 아내를 보여줄게.” 천사가 성령 안에서 나를 크고 높은 산으로 데려갔어. 거룩한 도시 예루살렘이 하늘에서 하나님께로부터 내려오는 걸 보여주었어. 하나님의 밝은 영광으로 빛나고 있었어."),
("12-14", "그 도시는 값진 보석처럼 빛났어. 빛으로 가득 차서 빛이 뛰고 있었어. 크고 높은 성벽이 있었고, 열두 문이 있었어. 각 문에는 천사가 서 있었고, 문들에는 이스라엘 자손 열두 지파의 이름이 새겨져 있었어. 동쪽에 세 문, 북쪽에 세 문, 남쪽에 세 문, 서쪽에 세 문이었어. 성벽은 열두 주춧돌 위에 세워졌고, 그 주춧돌들에는 어린 양의 열두 사도의 이름이 새겨져 있었어."),
("15-21", "나와 말하던 천사가 도시와 그 문들과 성벽을 잴 금 갈대를 가지고 있었어. 도시는 정사각형으로 놓여 있었어. 천사가 그 갈대로 도시를 재었어. 일천오백 마일, 길이와 너비와 높이가 모두 같았어. 표준 자로 천사가 성벽의 두께를 재었어. 일흔두 야드였어. 성벽은 벽옥이었고, 영광의 색이었고, 도시는 순금이었어. 유리처럼 투명했어. 도시 성벽의 주춧돌들은 상상할 수 있는 모든 값진 보석으로 장식되어 있었어. 첫째 주춧돌은 벽옥, 둘째는 사파이어, 셋째는 마노, 넷째는 에메랄드, 다섯째는 오닉스, 여섯째는 카넬리언, 일곱째는 크리솔라이트, 여덟째는 베릴, 아홉째는 토파즈, 열째는 크리소프레이즈, 열한째는 히아신스, 열두째는 자수정이었어. 열두 문은 열두 진주였어. 각 문이 하나의 진주였어."),
("21-27", "도시의 큰 거리는 순금이었고, 유리처럼 투명했어. 그런데 성전은 보이지 않았어. 주 하나님—전능하신 분—과 어린 양이 성전이시기 때문이야. 도시는 빛을 위해 해나 달이 필요 없었어. 하나님의 영광이 그 빛이고, 어린 양이 그 등불이야! 민족들이 그 빛 가운데 걸을 거고, 땅의 왕들이 자기들의 영광을 가져올 거야. 그 문들은 낮에는 절대 닫히지 않을 거야. 밤이 없을 거거든. 민족들의 영광과 존귀를 도시 안으로 가져올 거야. 더럽거나 역겨운 것은 도시에 들어가지 못할 거야. 속이거나 거짓말하는 사람도 못 들어가. 어린 양의 생명책에 이름이 기록된 사람들만 들어갈 거야."),
])

# Ch22 KO (13 paras)
koch(22, [
("1-5", "천사가 생명수 강을 보여주었어. 수정처럼 맑았어. 하나님과 어린 양의 보좌에서 흘러나와서 거리 한가운데로 흘렀어. 생명나무가 강 양쪽에 심어져 있었어. 열두 가지 열매를 맺고, 매달 익은 열매를 냈어. 그 나무의 잎사귀는 민족들을 치유하기 위한 거야. 다시는 저주가 없을 거야. 하나님과 어린 양의 보좌가 중심에 있을 거야. 그분의 종들이 하나님을 섬길 거야—경배하면서, 그분의 얼굴을 볼 거야. 그들의 이마에는 하나님을 비추고 있을 거야. 다시는 밤이 없을 거야. 아무도 등불이나 햇빛이 필요 없을 거야. 하나님, 주님의 빛이 필요한 모든 빛이거든. 그들이 그분과 함께 영원히 다스릴 거야."),
("6-7", "§선반에 두지 마"),
("6-7", "천사가 나한테 말했어. “이 말씀들은 믿을 수 있고 정확한 말씀들이야, 하나하나 다. 예언자들의 영의 하나님, 주님이 자기 천사를 보내셔서 자기 종들에게 곧 일어날 일을 보여주셨어. 그들에게 말해. ‘그래, 내가 가는 중이야!’ 이 책의 예언의 말씀을 지키는 사람은 복이 있어.”"),
("8-9", "나 요한이 이 모든 것을 내 눈으로 보고 내 귀로 들었어. 듣고 보자마자, 나한테 이 모든 것을 보여준 천사의 발 앞에 엎드려 경배했어. 천사가 반대했어. “안 돼! 나도 너와 같은 종이야. 네 동료 예언자들과 이 책의 말씀을 지키는 모든 사람과 같은 종이라고. 하나님께 경배하라!”"),
("10-11", "천사가 계속 말했어. “이 책의 예언의 말씀을 봉인하지 마. 선반에 두지 마. 때가 거의 다 됐어. 악한 자는 계속 악하게 하고, 더러운 마음을 가진 자는 계속 더럽게 하라. 하지만 의로운 자는 바른 길을 유지하고, 거룩한 자는 계속 거룩하게 하라.”"),
("12-13", "“그래, 내가 가는 중이야! 곧 갈 거야! 내 급료를 가지고 가. 모든 사람에게 자기 일한 대로 톡톡히 갚아줄 거야. 나는 A부터 Z까지, 처음이자 마지막, 시작이자 끝이야.”"),
("14-15", "“자기 두루마기를 빠는 사람들은 얼마나 복된지! 생명나무가 영원히 그들의 것이고, 문들을 통해 도시로 걸어 들어갈 거야. 하지만 영원히 밖에는 더러운 자들이 있어. 마술하는 자, 음행하는 자, 살인자, 우상 숭배자—거짓을 사랑하고 거짓대로 사는 모든 자.”"),
("16", "“나 예수가 내 천사를 보내서 교회들을 위해 이 일들을 증언하게 했어. 나는 다윗의 뿌리이자 가지, 밝은 새벽별이야.”"),
("17", "“와!” 성령과 신부가 말해. 듣는 사람도 “와!”라고 외쳐. 목마른 사람 있어? 와! 원하는 사람은 다 와서 마셔. 생명수를 공짜로 마셔!"),
("18-19", "이 책의 예언의 말씀을 듣는 모든 사람에게 공정하게 경고해. 이 예언의 말씀에 더하는 사람이 있으면, 하나님이 이 책에 기록된 재앙을 그 사람의 삶에 더하실 거야. 이 예언의 책의 말씀에서 빼는 사람이 있으면, 하나님이 이 책에 기록된 생명나무와 거룩한 도시에서 그 사람의 몫을 빼실 거야."),
("20", "이 모든 것에 대해 증언하시는 분이 다시 말씀하셔. “내가 가는 중이야! 곧 갈 거야!” 그래! 와, 주 예수여!"),
("21", "주 예수의 은혜가 너희 모두와 함께하길. 오, 그래!"),
])

# Ch4 KO (5 paras) - CORRECTED
koch(4, [
("1", "§하늘로 열린 문"),
("1", "그때 내가 봤어. 와!—하늘로 열린 문이 있었어. 나팔 소리 같았던 첫 번째 목소리, 내 환상에서 처음 들었던 그 목소리가 말했어. “올라와. 앞으로 일어날 일을 보여줄게.”"),
("2-6", "나는 바로 깊은 경배 중에 사로잡혔어. 와!—하늘에 보좌가 있었고, 보좌에 앉으신 분이 계셨어. 그분의 모습은 벽옥과 카넬리언 같았어. 보좌 주위에는 에메랄드 같은 무지개가 있었어. 보좌 주위에는 스물네 보좌가 있었고, 그 보좌들에는 스물네 장로가 앉아 있었어. 흰 옷을 입고 머리에는 금 면류관을 쓰고 있었어. 보좌에서는 번개가 치고, 목소리가 나고, 우레가 울렸어. 보좌 앞에는 일곱 횃불이 타오르고 있었어. 그게 하나님의 일곱 영이야. 보좌 앞에는 수정처럼 맑은 유리 바다가 있었어. 보좌 한가운데와 주위에는 네 생물이 있었어. 앞뒤로 눈이 가득했어."),
("6-8", "보좌 주위를 어슬렁거리는 네 동물이 있었어. 모두 눈이야. 앞을 보는 눈, 뒤를 보는 눈. 첫째 동물은 사자 같았고, 둘째는 송아지 같았고, 셋째는 사람 얼굴 같았고, 넷째는 날아가는 독수리 같았어. 네 동물은 각각 여섯 날개를 가졌고, 날개 안팎으로 눈이 가득했어. 밤낮 쉬지 않고 말했어. “거룩하다, 거룩하다, 거룩하다! 주 하나님, 전능하신 분! 전에 계셨고, 지금 계시고, 앞으로 오실 분!”"),
("9-11", "동물들이 보좌에 앉으신 분—영원히 사시는 분—께 영광과 존귀와 감사를 드릴 때마다, 스물네 장로가 보좌에 앉으신 분 앞에 엎드려 영원히 사시는 분께 경배했어. 자기들의 면류관을 보좌 앞에 던지며 말했어. “주여, 우리 하나님이시여! 영광과 존귀와 권세를 받으시기에 합당하십니다! 당신이 모든 것을 창조하셨고, 당신의 뜻으로 모든 것이 존재하고 창조되었습니다!”"),
])

# Ch5 KO (6 paras) - CORRECTED
koch(5, [
("1-2", "§사자는 어린 양이다"),
("1-2", "보좌에 앉으신 분의 오른손에 두루마리가 있는 걸 봤어. 앞뒤로 글이 쓰여 있었고, 일곱 도장으로 봉인되어 있었어. 힘센 천사가 큰 목소리로 외치는 걸 봤어. “누가 이 두루마리를 펴고 그 도장을 뗄 자격이 있느냐?”"),
("3", "하늘에도, 땅에도, 땅 밑에도, 그 두루마리를 펴거나 볼 수 있는 사람이 아무도 없었어."),
("4-5", "나는 울고 울고 울었어. 그 두루마리를 펴고 읽을 자격이 있는 사람이 아무도 없었거든. 장로 중 한 분이 나한테 말했어. “울지 마. 봐. 유다 지파의 사자, 다윗의 뿌리가 이겼어! 그분이 이 두루마리를 펴고 일곱 도장을 뗄 수 있어.”"),
("6-10", "그래서 내가 봤어. 보좌와 동물들과 장로들로 둘러싸인 곳에 어린 양이 서 계셨어. 죽임당했지만 서 있는 것 같았어. 일곱 뿔과 일곱 눈을 가지고 계셨어. 그게 온 땅에 보내진 하나님의 일곱 영이야. 어린 양이 가셔서 보좌에 앉으신 분의 오른손에서 두루마리를 받으셨어. 두루마리를 받으시자, 네 동물과 스물네 장로가 어린 양 앞에 엎드렸어. 각각 거문고와 향이 가득한 금 대접을 가지고 있었어. 그 향은 성도들의 기도야. 그들이 새 노래를 불렀어. “당신은 이 두루마리를 받고 그 도장을 뗄 자격이 있으십니다! 당신이 죽임당하셨고, 당신의 피로 사람들을 사서 하나님께 드리셨기 때문입니다. 각 족속과 언어와 백성과 나라에서 온 사람들이요. 당신은 그들을 나라와 제사장으로 삼으셨고, 그들이 땅에서 왕 노릇 할 겁니다!”"),
("11-14", "다시 봤어. 보좌와 동물들과 장로들 주위에 많은 천사들의 목소리를 들었어—만만의 만 배, 천의 천 배야. 큰 목소리로 말했어. “죽임당하신 어린 양은 권세와 부와 지혜와 힘과 존귀와 영광과 찬양을 받으시기에 합당하십니다!” 하늘에 있는 모든 피조물, 땅에 있는 모든 것, 땅 밑에 있는 것, 바다에 있는 것, 그 안에 있는 모든 것이 말하는 걸 들었어. “보좌에 앉으신 분과 어린 양에게 찬양과 존귀와 영광과 권세가 영원히 있기를!” 네 동물이 말했어. “아멘!” 장로들은 엎드려 경배했어."),
])

# Ch6 KO (7 paras) - CORRECTED
koch(6, [
("1-2", "§두루마리 봉인 해제"),
("1-2", "어린 양이 일곱 도장 중 첫째를 떼는 걸 지켜봤어. 네 동물 중 하나가 우레 같은 목소리로 말하는 걸 들었어. “와!” 그래서 내가 봤어. 흰 말이 있었어! 그 말을 탄 사람은 활을 가지고 있었어. 그에게 면류관이 주어졌고, 이기면서 나갔어."),
("3-4", "어린 양이 둘째 도장을 떼자, 둘째 동물이 외치는 걸 들었어. “와!” 다른 말이 나왔어. 붉은 말이었어. 그 말을 탄 사람에게는 땅에서 평화를 거두어가고 사람들이 서로 죽이게 할 권세가 주어졌어. 그에게 큰 칼이 주어졌어."),
("5-6", "어린 양이 셋째 도장을 떼자, 셋째 동물이 외치는 걸 들었어. “와!” 그래서 내가 봤어. 검은 말이 있었어! 그 말을 탄 사람은 손에 저울을 가지고 있었어. 네 동물 사이에서 목소리가 들렸어. “밀 한 되에 하루 품삯, 보리 세 되에 하루 품삯이야. 그런데 기름과 포도주는 해하지 마!”"),
("7-8", "어린 양이 넷째 도장을 떼자, 넷째 동물의 목소리를 들었어. “와!” 그래서 내가 봤어. 창백한 말이 있었어! 그 말을 탄 사람의 이름은 죽음이었고, 지옥이 그를 따랐어. 그들에게는 땅의 4분의 1을 다스릴 권세가 주어졌어. 칼과 기근과 질병과 땅의 들짐승으로 죽이게 할 권세야."),
("9-11", "어린 양이 다섯째 도장을 떼자, 하나님의 말씀과 예수의 증언 때문에 죽임당한 사람들의 영혼을 제단 아래서 봤어. 그들이 큰 목소리로 외쳤어. “거룩하고 참되신 주님이시여! 언제까지 심판하지 않으시고 우리 피의 원수를 갚아주지 않으시나요?” 그들 각자에게 흰 두루마기가 주어졌어. 그들에게 말했어. “조금 더 쉬어. 너희와 같이 죽을 동료 종들과 형제들의 수가 찰 때까지야.”"),
("12-17", "어린 양이 여섯째 도장을 떼는 걸 지켜봤어. 뼈를 흔드는 지진이 일어났어. 해가 거무스름한 자루처럼 검어졌고, 달이 피처럼 붉어졌어. 하늘의 별들이 땅에 떨어졌어. 무화과나무가 강한 바람에 흔들려 익지 않은 열매를 떨어뜨리는 것처럼 말이야. 하늘은 두루마리가 말리는 것처럼 사라졌고, 모든 산과 섬이 제자리에서 옮겨졌어. 땅의 왕들과 관리들과 장수들과 부자들과 강한 자들과 종들과 자유인들, 작은 자와 큰 자가 동굴과 바위 사이에 숨었어. 산들과 바위들에게 말했어. “우리 위에 무너져라! 보좌에 앉으신 분의 낯과 어린 양의 진노에서 우리를 숨겨다오! 그들의 진노의 큰 날이 왔어. 누가 감당할 수 있겠어?”"),
])

# Ch8 KO (9 paras) - CORRECTED
koch(8, [
("1", "어린 양이 일곱째 도장을 떼자, 하늘이 조용해졌어—완전한 침묵이야. 약 30분 동안."),
("2-4", "§나팔 불기"),
("2-4", "하나님 앞에 항상 대기하고 있는 일곱 천사가 일곱 나팔을 받는 걸 봤어. 또 다른 천사가 와서 제단 앞에 섰어. 금 향로를 가지고 있었어. 그 천사에게 많은 향이 주어졌어. 모든 성도들의 기도와 함께 보좌 앞 금 제단 위에 드리려고. 향의 연기가 성도들의 기도와 함께 천사의 손에서 하나님 앞으로 올라갔어."),
("5", "그때 천사가 향로를 가져다가 제단의 불을 담아서 땅에 던졌어. 우레와 목소리와 번개와 지진이 일어났어."),
("6-7", "나팔을 가진 일곱 천사가 나팔을 불 준비를 했어. 첫째 천사가 나팔을 불었어. 우박과 불이 피와 섞여서 땅에 던져졌어. 땅의 3분의 1이 타버렸고, 나무의 3분의 1이 타버렸고, 모든 푸른 풀도 타버렸어."),
("8-9", "둘째 천사가 나팔을 불었어. 불타는 큰 산 같은 것이 바다에 던져졌어. 바다의 3분의 1이 피가 되었고, 바다에 있는 피조물의 3분의 1이 죽었고, 배의 3분의 1이 파괴되었어."),
("10-11", "셋째 천사가 나팔을 불었어. 횃불처럼 타는 큰 별이 하늘에서 떨어졌어. 강의 3분의 1과 물의 샘에 떨어졌어. 그 별의 이름은 쑥이야. 물의 3분의 1이 쑥이 되었고, 많은 사람들이 그 물 때문에 죽었어. 물이 쓰게 되었거든."),
("12", "넷째 천사가 나팔을 불었어. 해의 3분의 1과 달의 3분의 1과 별들의 3분의 1이 쳐서, 그것들의 3분의 1이 어두워졌어. 낮의 3분의 1이 빛을 잃었고, 밤도 마찬가지였어."),
("13", "내가 자세히 보고 들었어. 한 독수리가 하늘 한가운데를 날아가면서 큰 목소리로 외치는 걸. “땅에 사는 사람들에게 화, 화, 화가 있을 거야! 아직 나팔을 불지 않은 세 천사의 나팔 소리 때문이야!”"),
])

# Ch9 KO (7 paras) - CORRECTED
koch(9, [
("1-2", "다섯째 천사가 나팔을 불었어. 하늘에서 땅에 떨어진 별을 봤어. 그 별에게 무저갱의 열쇠가 주어졌어. 그 별이 무저갱을 열었어. 큰 용광로의 연기 같은 연기가 구덩이에서 올라왔어. 해와 공기가 구덩이의 연기로 어두워졌어."),
("3-6", "그 연기에서 메뚜기들이 땅에 나왔어. 그들에게는 땅의 전갈의 권세 같은 권세가 주어졌어. 그들에게 말했어. 땅의 풀이나 푸른 것이나 나무를 해하지 말고, 오직 이마에 하나님의 도장을 받지 않은 사람들만 해하라고. 그들을 죽이지는 말고 다섯 달 동안 괴롭히라고. 그 괴롭힘은 전갈이 사람을 쏠 때의 괴롭힘 같았어. 그 날들에는 사람들이 죽음을 찾아도 찾지 못하고, 죽기를 원해도 죽음이 그들을 피할 거야."),
("7-11", "그 메뚜기들의 모양은 전쟁을 위해 준비된 말들 같았어. 머리에는 금 면류관 같은 것이 있었고, 얼굴은 사람의 얼굴 같았어. 머리카락은 여자의 머리카락 같았고, 이는 사자의 이 같았어. 철 흉갑 같은 흉갑을 입었어. 날개의 소리는 전쟁터로 달려가는 많은 말들과 병거의 소리 같았어. 꼬리는 전갈 같았고, 꼬리에는 쏘는 것이 있었어. 다섯 달 동안 사람들을 해할 권세가 꼬리에 있었어. 그들 위에 왕이 있었어. 무저갱의 천사야. 히브리어로 이름은 아바돈이고, 헬라어로는 아볼루온이야."),
("12", "첫째 화가 지나갔어. 아직 두 화가 더 남았어."),
("13-14", "여섯째 천사가 나팔을 불었어. 하나님 앞에 있는 금 제단의 네 뿔에서 나오는 목소리를 들었어. 나팔을 가진 여섯째 천사에게 말했어. “유프라테스 큰 강에 결박된 네 천사를 풀어줘.”"),
("15-19", "그래서 네 천사가 풀렸어. 년, 월, 일, 시를 위해 준비되었어. 사람들의 3분의 1을 죽이라고. 기병대의 수는 이만 만이야. 그 수를 들었어. 내가 본 말들과 그 말을 탄 사람들의 모습은 이랬어. 불빛과 자주빛과 유황빛 흉갑을 입었어. 말들의 머리는 사자의 머리 같았고, 입에서는 불과 연기와 유황이 나왔어. 이 세 재앙으로 사람들의 3분의 1이 죽었어. 입에서 나오는 불과 연기와 유황 때문이야. 말들의 권세는 입과 꼬리에 있었거든. 꼬리는 뱀 같았고, 머리가 있어서 그것으로 해를 끼쳤어."),
("20-21", "그런데 이 재앙들로 죽지 않고 남은 사람들은 자기 손으로 만든 일을 회개하지 않았어. 귀신들과 금, 은, 놋, 돌, 나무 우상에게 절하는 걸 그치지 않았어. 그 우상들은 보지도 못하고 듣지도 못하고 걷지도 못해. 또 살인과 마술과 음행과 도둑질도 회개하지 않았어."),
])

# Ch10 KO (3 paras) - CORRECTED
koch(10, [
("1-4", "또 다른 힘센 천사가 하늘에서 내려오는 걸 봤어. 구름을 입었고, 머리 위에는 무지개가 있었어. 얼굴은 해 같았고, 다리는 불기둥 같았어. 손에는 펴진 작은 책을 가지고 있었어. 오른발은 바다 위에, 왼발은 땅 위에 두고, 사자가 울부짖는 것처럼 큰 목소리로 외쳤어. 외치자 일곱 우레가 목소리를 냈어. 일곱 우레가 말했을 때, 내가 기록하려고 했어. 그런데 하늘에서 목소리가 들렸어. “일곱 우레가 말한 것을 봉인하고 기록하지 마.”"),
("5-7", "바다 위와 땅 위에 서 있는 걸 내가 본 그 천사가 오른손을 하늘로 들었어. 하늘과 그 안에 있는 것들과 땅과 그 안에 있는 것들과 바다와 그 안에 있는 것들을 창조하신 분, 영원히 사시는 분을 두고 맹세했어. “더 이상 지체하지 않을 거야. 일곱째 천사가 나팔을 불 때, 하나님의 비밀이 완성될 거야. 그분의 종 예언자들에게 전한 기쁜 소식대로 말이야.”"),
("8-11", "하늘에서 내가 들었던 그 목소리가 다시 나한테 말했어. “가서 바다 위와 땅 위에 서 있는 천사의 손에 펴진 작은 책을 가져와.” 그래서 내가 천사에게 가서 작은 책을 달라고 했어. 천사가 나한테 말했어. “가져다가 먹어. 네 배에는 쓰겠지만, 입에는 꿀처럼 달 거야.” 그래서 내가 천사의 손에서 작은 책을 가져다가 먹었어. 입에는 꿀처럼 달았는데, 먹고 나니까 배가 쓰더라. 그리고 나한테 말했어. “너는 다시 많은 백성과 민족과 언어와 왕에 대해 예언해야 해.”"),
])

# Ch16 KO (11 paras) - CORRECTED
koch(16, [
("1", "§진노의 일곱 대접"),
("1", "성전에서 큰 목소리를 들었어. 일곱 천사에게 말했어. “가서 하나님의 진노의 일곱 대접을 땅에 쏟으라.”"),
("2", "첫째 천사가 가서 자기 대접을 땅에 쏟았어. 짐승의 표를 받은 사람들과 그 우상에게 경배하는 사람들에게 악하고 독한 종기가 났어."),
("3", "둘째 천사가 자기 대접을 바다에 쏟았어. 바다가 죽은 사람의 피처럼 되었고, 바다에 있는 모든 생물이 죽었어."),
("4-7", "셋째 천사가 자기 대접을 강과 물의 샘에 쏟았어. 그것들이 피가 되었어. 물을 다스리는 천사가 말하는 걸 들었어. “지금 계시고 전에 계셨던 거룩하신 분이시여, 당신은 의로우십니다! 이렇게 심판하셨기 때문입니다. 그들이 성도들과 예언자들의 피를 흘렸기 때문에, 당신이 그들에게 피를 마시게 하셨습니다. 그들이 마땅히 받을 겁니다!” 제단에서 대답하는 걸 들었어. “그래, 전능하신 주 하나님이시여! 당신의 심판은 참되고 의롭습니다!”"),
("8-9", "넷째 천사가 자기 대접을 해에 쏟았어. 해에게 불로 사람들을 태울 권세가 주어졌어. 사람들이 맹렬한 열에 탔어. 이 재앙들을 다스릴 권세를 가지신 하나님의 이름을 모독했어. 회개하고 그분께 영광을 돌리지 않았어."),
("10-11", "다섯째 천사가 자기 대접을 짐승의 보좌에 쏟았어. 그 왕국이 어두워졌어. 사람들이 고통으로 혀를 깨물었어. 고통과 종기 때문에 하늘의 하나님을 모독했어. 자기들의 행위를 회개하지 않았어."),
("12-14", "여섯째 천사가 자기 대접을 큰 강 유프라테스에 쏟았어. 그 강물이 말랐어. 해 뜨는 곳에서 오는 왕들의 길을 준비하려고. 용의 입과 짐승의 입과 거짓 예언자의 입에서 개구리 같은 더러운 영 셋이 나오는 걸 봤어. 그 영들은 표적을 행하는 귀신의 영들이야. 온 세상 왕들에게 나가. 전능하신 하나님의 큰 날의 전쟁을 위해 그들을 모으려고."),
("15", "“봐, 내가 도둑처럼 와! 깨어서 자기 옷을 지키는 사람은 복이 있어. 벌거벗고 다니며 부끄러움을 드러내지 않게 하려고.”"),
("16", "그 영들이 왕들을 히브리어로 아마겟돈이라고 하는 곳에 모았어."),
("17-21", "일곱째 천사가 자기 대접을 공중에 쏟았어. 성전의 보좌에서 큰 목소리가 났어. “다 끝났다!” 번개와 목소리와 우레가 있었어. 큰 지진이 있었어. 사람이 땅에 생긴 이후로 이렇게 크고 강력한 지진은 없었어. 큰 도시가 세 부분으로 갈라졌어. 민족들의 도시들이 무너졌어. 큰 바벨론이 하나님 앞에 기억되어서, 그분의 맹렬한 진노의 포도주 잔을 받았어. 모든 섬이 도망쳤고, 산들도 찾을 수 없었어. 하늘에서 사람들에게 큰 우박이 떨어졌어. 한 달란트 정도 되는 우박이야. 사람들이 우박의 재앙 때문에 하나님을 모독했어. 그 재앙이 엄청 컸거든."),
])

# Ch17 KO (7 paras) - CORRECTED
koch(17, [
("1-2", "§위대한 바벨론, 음녀들의 어머니"),
("1-2", "일곱 대접을 가진 일곱 천사 중 하나가 와서 나한테 말했어. “이리 와. 많은 물 위에 앉은 위대한 음녀가 받을 심판을 보여줄게. 땅의 왕들이 그 여자와 음행했고, 땅에 사는 사람들이 그 여자의 음행의 포도주에 취했어.”"),
("3-6", "천사가 성령 안에서 나를 광야로 데려갔어. 거기서 여자가 주홍빛 짐승 위에 앉아 있는 걸 봤어. 그 짐승은 온통 신성모독의 이름들로 덮여 있었고, 일곱 머리와 열 뿔이 있었어. 여자는 자주빛과 주홍빛 옷을 입었고, 금과 보석과 진주로 치장했어. 손에는 금잔을 들고 있었어. 역겨운 것들과 자기 음행의 더러운 것들로 가득했어. 이마에는 이름이 쓰여 있었어. 비밀스러운 이름이야. “큰 바벨론, 땅의 음녀들과 역겨운 것들의 어미.” 여자가 성도들의 피와 예수의 증인들의 피에 취한 걸 봤어. 그 여자를 보고 나는 완전히 놀랐어."),
("6-8", "천사가 나한테 말했어. “왜 놀라? 내가 이 여자의 신비와 그 여자를 태운 짐승의 신비를 말해줄게. 일곱 머리와 열 뿔이 있는 짐승 말이야. 네가 본 짐승은 전에 있었다가 지금은 없고, 앞으로 무저갱에서 올라와 멸망으로 갈 거야. 땅에 사는 사람들, 세상이 창조된 이후로 생명책에 이름이 기록되지 않은 사람들은 놀랄 거야. 그 짐승이 전에 있었다가 지금은 없고 또 올 것이기 때문이야.”"),
("9-11", "“여기에 지혜로운 마음이 필요해. 일곱 머리는 여자가 앉은 일곱 산이야. 또 일곱 왕이야. 다섯은 쓰러졌고, 하나는 지금 있고, 다른 하나는 아직 오지 않았어. 오면 잠시 있어야 해. 전에 있었다가 지금은 없는 짐승은 여덟째 왕이야. 일곱 중 하나이면서 멸망으로 가.”"),
("12-14", "“네가 본 열 뿔은 열 왕이야. 아직 왕국을 받지 못했지만, 짐승과 함께 한 시간 동안 왕처럼 권세를 받을 거야. 이들은 한마음이야. 자기들의 권세와 권위를 짐승에게 줄 거야. 그들이 어린 양과 싸울 거야. 그런데 어린 양이 그들을 이길 거야. 어린 양은 만주의 주, 만왕의 왕이시거든. 그분과 함께 있는 사람들—부르심을 받고 택함을 받고 신실한 사람들—도 이길 거야.”"),
("15-18", "천사가 나한테 말했어. “네가 본 물, 음녀가 앉은 곳은 백성과 무리와 민족과 언어야. 네가 본 열 뿔과 짐승이 음녀를 미워할 거야. 그 여자를 벌거벗기고 황폐하게 하고, 살을 먹고, 불로 태울 거야. 하나님이 그들의 마음에 당신의 뜻을 이루려는 마음을 주셨거든. 한마음이 되어 자기들의 왕국을 짐승에게 줄 거야. 하나님의 말씀이 이루어질 때까지 말이야. 네가 본 여자는 땅의 왕들을 다스리는 큰 도시야.”"),
])


# ---- 2026-09-22 audit: undeclared merges recorded + principle-5 softenings ----
def _add_merge(n, para, rng, note):
    META[n]["merges"].append({"para": para, "msg_ranges": [rng], "note": note})
    META[n]["confirmations_needed"].append(
        "Ch%d: merge of MSG %s (multiple printed paragraphs) into one paragraph \u2014 confirm OK" % (n, rng))

_add_merge(1, 2, "3", "MSG prints v3 as two paragraphs ('How blessed the reader!...' + 'Time is just about up.'); kept as one EN paragraph")
_add_merge(2, 3, "4-5", "MSG prints 4-5 as two paragraphs ('But you walked away...' + 'Turn back! Recover...'); kept as one EN paragraph")
_add_merge(2, 9, "10", "MSG prints v10 as two paragraphs ('Fear nothing...' + 'Don't quit...'); kept as one EN paragraph")
_add_merge(3, 1, "1", "MSG prints v1 as two paragraphs (commission + 'I see right through your work'); kept as one EN paragraph")
_add_merge(3, 2, "2-3", "MSG prints 2-3 as two paragraphs ('Up on your feet!' + 'If you pull the covers...'); kept as one EN paragraph")
_add_merge(4, 3, "6-8", "MSG prints 6-8 as two paragraphs (Four Animals description + 'Holy, holy, holy' chant); kept as one EN paragraph")
_add_merge(4, 4, "9-11", "MSG prints 9-11 as two paragraphs (Elders fall prostrate + 'Worthy, O Master!' chant); kept as one EN paragraph")
_add_merge(14, 8, "13", "MSG prints v13 as two paragraphs (voice from Heaven + Spirit's 'Yes'); kept as one EN paragraph")
_add_merge(18, 2, "9-10", "MSG prints 9-10 as two paragraphs (kings' lament + 'Doom, doom'); kept as one EN paragraph")
_add_merge(18, 3, "11-17", "MSG prints 11-17 as four paragraphs (traders' cry, 'Everything you've lived for', traders at distance, 'Doom, doom'); kept as one EN paragraph")
_add_merge(18, 4, "17-19", "MSG prints 17-19 as two paragraphs (shipmasters' cry + 'Doom, doom'); kept as one EN paragraph")
_add_merge(18, 6, "21-24", "MSG prints 21-24 as two paragraphs (millstone + 'Heaved and sunk'); kept as one EN paragraph")
_add_merge(19, 2, "4", "MSG prints v4 as two paragraphs (Elders fall + 'Amen! Yes! Hallelujah!'); kept as one EN paragraph")
_add_merge(19, 3, "5", "MSG prints v5 as two paragraphs (shout from Throne + 'Praise our God'); kept as one EN paragraph")
_add_merge(22, 10, "20", "MSG prints v20 as two paragraphs (testifier's 'I'm on my way!' + 'Yes! Come, Master Jesus!'); kept as one EN paragraph")

META[1]["changes"].append("Principle 5: 'the ultimate ride-or-die' -> 'the totally loyal Witness' (MSG 'Loyal Witness')")
META[1]["changes"].append("Declared merge of MSG v3 two printed paragraphs (was undeclared)")
META[2]["changes"].append("Principle 5: 'The bastard offspring of their idol-whoring' -> 'The children of their idol-cheating'")
META[2]["changes"].append("Declared merges of MSG 4-5 and v10 two-paragraph printings (were undeclared)")
META[2]["changes"].append("KO principle 5: kkodeuyeo->yuhokhae(x2), gyal/gya->geu yeoja, noreum->nori, maechun->eumhaeng, kkyongddudeo->kkwettudeo(typo)")
META[3]["changes"].append("Declared merges of MSG v1 and 2-3 two-paragraph printings (were undeclared)")
META[4]["changes"].append("Declared merges of MSG 6-8 and 9-11 two-paragraph printings (were undeclared)")
META[7]["changes"].append("Folded MSG '* * *' scene-break marker (4-8) into surrounding paragraph (no content)")
META[8]["changes"].append("Folded MSG '* * *' scene-break marker (v13) into surrounding paragraph (no content)")
META[9]["changes"].append("Folded MSG '* * *' scene-break marker (20-21) into surrounding paragraph (no content)")
META[14]["changes"].append("Principle 5: 'wine of her whoring' -> 'wine of her unfaithfulness'")
META[14]["changes"].append("Declared merge of MSG v13 two printed paragraphs (was undeclared)")
META[17]["changes"].append("Principle 5: 'Whore/whoring/whorish lust' -> 'Prostitute/unfaithful/seductive lust'; header 'Mother of Whores' -> 'Mother of Prostitutes'")
META[17]["changes"].append("KO principle 5: changnyeo->eumnyeo throughout; header -> 'widaehan babelon, eumnyeodeurui eomeoni'")
META[18]["changes"].append("Declared merges of MSG 9-10, 11-17, 17-19, 21-24 multi-paragraph printings (were undeclared)")
META[18]["changes"].append("Principle 5: 'went whoring with her' -> 'were unfaithful with her'; 'wild wine of her whoring' -> 'wild wine of her unfaithfulness'")
META[19]["changes"].append("Declared merges of MSG v4 and v5 two-paragraph printings (were undeclared)")
META[19]["changes"].append("Principle 5: 'the great Whore' -> 'the great Prostitute'; KO keun changnyeo->keun eumnyeo")
META[21]["changes"].append("Folded MSG '* * *' scene-break marker (21-27) into surrounding paragraph (no content)")
META[22]["changes"].append("Declared merge of MSG v20 two printed paragraphs (was undeclared)")
META[22]["changes"].append("Folded MSG '* * *' scene-break marker (10-11) into surrounding paragraph (no content)")

# ============================== OUTPUT ==============================
import os
os.makedirs('/home/hatch/workspace/teenz-bible-review/fixes', exist_ok=True)

def build_json(lang_dict, lang):
    chapters = []
    for n in range(1, 23):
        paras = lang_dict[n]
        meta = META[n]
        # verseRanges: explicit list matching paragraphs
        verse_ranges = [badge for badge, _ in paras]
        paragraphs = [text for _, text in paras]
        chapters.append({
            "chapter": n,
            "title": meta["title"],
            "verseRanges": verse_ranges,
            "msg_ranges": meta["msg_ranges"],
            "paragraphs": paragraphs,
            "merges": meta["merges"],
            "splits": meta["splits"],
            "changes": meta["changes"],
            "confirmations_needed": meta["confirmations_needed"],
        })
    return {"book": "Revelation", "language": lang, "chapters": chapters}

en_out = build_json(EN, "en")
ko_out = build_json(KO, "ko")

# Validator expects a list of chapter objects (or single chapter), not wrapped
with open('/home/hatch/workspace/teenz-bible-review/fixes/en_Revelation.json', 'w', encoding='utf-8') as f:
    json.dump(en_out['chapters'], f, ensure_ascii=False, indent=2)
with open('/home/hatch/workspace/teenz-bible-review/fixes/ko_Revelation.json', 'w', encoding='utf-8') as f:
    json.dump(ko_out['chapters'], f, ensure_ascii=False, indent=2)

print("Generated fixes/en_Revelation.json and fixes/ko_Revelation.json")
print(f"EN chapters: {len(en_out['chapters'])}, KO chapters: {len(ko_out['chapters'])}")
