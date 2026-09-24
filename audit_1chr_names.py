#!/usr/bin/env python3
"""Extract MSG proper names / numbers per chapter and check presence in Teen EN."""
import json, re, sys

sys.path.insert(0, 'gdocs_build')
from build_gdocs import parse_msg_txt

msg = parse_msg_txt('msg_1Chronicles.txt')
en = {c['chapter']: c for c in json.load(open('fixes/en_1Chronicles.json'))}

STOP = {'The','A','An','And','But','Then','When','So','As','Of','To','In','For',
        'He','She','They','It','His','Her','Their','Its','This','That','These',
        'Those','With','Without','From','By','On','At','Israel','Israelites',
        'God','David','King','Lord','City','Temple','Ark','Chest','Covenant',
        'Sons','Son','Daughter','Wife','Brother','Sister','Father','Mother',
        'Men','Man','People','War','Day','Night','House','Land','Country',
        'Priest','Priests','Levite','Levites','Army','Battle','King','Queen',
        'All','Every','Each','One','Two','Three','Four','Five','Six','Seven',
        'Eight','Nine','Ten','First','Second','Third','Last','Next','Other',
        'My','Your','Our','No','Not','Yes','Now','Here','There','Who','What',
        'How','Why','Don','Didn','Wasn','Weren','Isn','Aren','Can','Could',
        'Would','Should','Will','Just','Even','Still','Also','Well','Like',
        'Made','Had','Has','Have','Were','Was','Are','Be','Being','Been',
        'Do','Did','Does','Get','Got','Give','Gave','Take','Took','Make',
        'Said','Say','Told','Tell','Went','Were','Came','Come','Put','Set',
        'Called','Named','Became','Blessed','Cursed','Killed','Died','Fought',
        'Ran','Sat','Stood','Fell','Rose','Built','Sent','Brought','Led',
        'Met','Left','Turned','Asked','Answered','Heard','Saw','Knew','Thought'}

def norm(s):
    return s.replace('\u2019', "'").replace('\u2018', "'").lower()

def names(text):
    # capitalized tokens (incl. hyphenated), 3+ letters, not sentence-initial common words
    toks = re.findall(r"[A-Z][a-z]+(?:[-'][A-Z]?[a-z]+)*", text)
    out = []
    for t in toks:
        base = t.split('-')[0].split("'")[0]
        if t in STOP or base in STOP or len(t) < 3:
            continue
        out.append(t)
    return out

ch = int(sys.argv[1])
msg_text = ' '.join(b for u in msg if u['chapter'] == ch for b in u['blocks'])
en_text = ' '.join(en[ch]['paragraphs'])
en_low = norm(en_text)

seen = set()
for n in names(msg_text):
    core = n.split("'")[0]  # strip possessive
    key = core.lower()
    if key in seen: continue
    seen.add(key)
    # check presence: full token, singular/plural variants, hyphen variants
    variants = {key, key.replace('-', ''), key.replace('-', ' ')}
    if key.endswith('s'): variants.add(key[:-1])
    else: variants.add(key + 's')
    if not any(v in en_low for v in variants):
        print(f'MISSING NAME? ch{ch}: {n}')
print('--- numbers in MSG ---')
nums = sorted(set(re.findall(r'\b\d[\d,]*\b', msg_text)))
en_nums = set(re.findall(r'\b\d[\d,]*\b', en_text))
wordnums = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7',
            'eight':'8','nine':'9','ten':'10','eleven':'11','twelve':'12','twenty':'20',
            'thirty':'30','forty':'40','fifty':'50','sixty':'60','seventy':'70',
            'eighty':'80','ninety':'90','hundred':'100','thousand':'1000'}
for n in nums:
    if n not in en_nums:
        # check word form
        w = [k for k,v in wordnums.items() if v == n.replace(',','')]
        if not any(k in en_low for k in w):
            print(f'MISSING NUM? ch{ch}: {n}')
