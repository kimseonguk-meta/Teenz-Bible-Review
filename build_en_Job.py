#!/usr/bin/env python3
"""Build fixes/en_Job.json from existing EN + parsed MSG + review decisions."""
import json

REVIEW = '/home/hatch/workspace/teenz-bible-review/'
msg = json.load(open(REVIEW + 'msg_paras_Job.json', encoding='utf-8'))
en_data = json.load(open('/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json',
                         encoding='utf-8'))
en_ch = {c['num']: c for c in en_data['Job']}

# para_idx -> new badge
BADGE_FIX = {
    1: {3: '6-7'},
    3: {0: '1-2', 1: '3-10'},
    5: {0: '1-7', 1: '8-16', 2: '17-19'},
    6: {5: '28-30'},
    27: {1: '2-6'},
    32: {1: '6-10'},
    33: {6: '23-25'},
    37: {2: '6-8', 3: '8-13'},
    38: {0: '1-11'},
}

# chapter -> list of split dicts
SPLITS = {
    1: [{'msg_range': '6-7', 'paras': [2, 3]}],
    2: [{'msg_range': '1-3', 'paras': [0, 1, 2, 3]},
        {'msg_range': '10', 'paras': [8, 9]}],
    4: [{'msg_range': '1-6', 'paras': [0, 1]}],
    6: [{'msg_range': '1-7', 'paras': [0, 1]}],
    27: [{'msg_range': '1-6', 'paras': [0, 1]},
         {'msg_range': '13-23', 'paras': [4, 5]}],
    29: [{'msg_range': '1-6', 'paras': [0, 1]}],
    32: [{'msg_range': '6-10', 'paras': [1, 2]}],
    31: [{'msg_range': '38-40', 'paras': [11, 12],
           'note': 'para 12 is the closing narrative line (MSG unnumbered); shares 38-40 badge'}],
    37: [{'msg_range': '1-13', 'paras': [0, 1, 2, 3],
           'note': 'v8 ice image spans paras 2-3'}],
    38: [{'msg_range': '1-11', 'paras': [0, 1]}],
    40: [{'msg_range': '3-5', 'paras': [2, 3]},
         {'msg_range': '6-7', 'paras': [4, 5]}],
}

REWRITES = {
    31: {
        4: ("Have I ignored the poor or let them starve while I ate good? No! "
            "My home was always open to them\u2014they were always welcome at my table."),
        9: ("Didn\u2019t my workers say, \u2018He fed us well\u2014there were always second helpings\u2019? "
            "And no stranger ever had to sleep on the street; my doors were always open to travelers. "
            "Did I hide my sin like Adam did, burying my guilt behind closed doors, because I was scared "
            "of what people would say\u2014scared of the neighbors\u2019 gossip\u2014turning myself into a recluse? "
            "You know good and well that I didn\u2019t."),
        10: ("Oh, if only someone would hear me out! I\u2019ve signed my name to my defense\u2014"
             "now let the Almighty answer. I want to see my indictment in writing. "
             "Anyone\u2019s welcome to read my defense\u2014I\u2019ll write it on a poster and carry it around town. "
             "I\u2019m ready to account for every move I\u2019ve ever made\u2014to anyone and everyone, prince or pauper."),
        11: ("If the very ground I farm accuses me, if even the furrows fill with tears from my abuse, "
             "if I\u2019ve ever ripped off the earth for my own profit or kicked its rightful owners off their land"
             "\u2014then let thistles grow instead of wheat, and weeds instead of barley."),
    }
}

CHANGES = {
    1: ["Ch1: badge 7 -> 6-7 (Satan's reply is part of MSG 6-7); split declared"],
    2: ["Ch2: MSG 1-3 split into 4 EN paras; MSG 10 split into 2 EN paras; splits declared"],
    3: ["Ch3: badges fixed 1 -> 1-2, 2-10 -> 3-10 (EN para2 covers MSG 3-10 curse content)"],
    4: ["Ch4: split declared for MSG 1-6 (intro + body)"],
    5: ["Ch5: badges fixed 1-8 -> 1-7, 9-16 -> 8-16, 8-27 -> 17-19 (content already matched MSG)"],
    6: ["Ch6: badge 29-30 -> 28-30 (EN para covers MSG 28-30 fully)"],
    27: ["Ch27: badge 2-4 -> 2-6 (EN para1 covers MSG 2-6 incl. 'never regret it'); splits for 1-6 and 13-23"],
    29: ["Ch29: split declared for MSG 1-6 (intro + body)"],
    31: ["Ch31: restored 4 omitted MSG details in teen voice - 'welcome at my table' (16-18), Adam-hiding + neighbors' gossip + recluse (31-34), signed name + indictment in writing + poster around town + prince or pauper (35-37), ground accuses + furrows' tears + thistles/barley (38-40)",
         "Ch31: closing narrative line shares badge 38-40 via split (was '40' duplicating v40)"],
    32: ["Ch32: badge 6 -> 6-10 (speech intro is part of MSG 6-10); split declared"],
    33: ["Ch33: badge 23-26 -> 23-25 (para content is MSG 23-25 angel passage only)"],
    37: ["Ch37: badges fixed 6-10 -> 6-8, 10-13 -> 8-13 (v8 ice image spans both paras); split declared for 1-13"],
    38: ["Ch38: badge 1 -> 1-11 (intro line is part of MSG 1-11); split declared"],
    40: ["Ch40: splits declared for MSG 3-5 and 6-7"],
}

out = []
for ch in range(1, 43):
    ec = en_ch[ch]
    paras = list(ec['paragraphs'])
    badges = list(ec['verseRanges'])
    for idx, nb in BADGE_FIX.get(ch, {}).items():
        badges[idx] = nb
    for idx, txt in REWRITES.get(ch, {}).items():
        paras[idx] = txt
    ms = msg[str(ch)]
    msg_ranges = [s['range'] for s in ms]
    out.append({
        'chapter': ch,
        'title': ec['title'],
        'paragraphs': paras,
        'verseRanges': badges,
        'msg_ranges': msg_ranges,
        'merges': [],
        'splits': SPLITS.get(ch, []),
        'changes': CHANGES.get(ch, []),
        'confirmations_needed': [],
    })

json.dump(out, open(REVIEW + 'fixes/en_Job.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('wrote fixes/en_Job.json:', len(out), 'chapters')
