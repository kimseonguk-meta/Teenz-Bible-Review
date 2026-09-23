import json

msg = {c['chapter']: c['paras'] for c in json.load(open('msg_paras_Ecclesiastes.json'))}
en_all = json.load(open('/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json'))
en = {c['num']:c for c in en_all['Ecclesiastes']}
ko = {c['num']: c for c in json.load(open('msg_work/ko_Ecclesiastes.json'))}

ko_titles = {
    1: '헛되고 헛되도다', 2: '쾌락의 헛됨', 3: '때가 있나니', 4: '압제와 외로움',
    5: '하나님을 경외하라', 6: '부의 헛됨', 7: '지혜의 가치', 8: '왕에게 순종',
    9: '지혜와 어리석음', 10: '어리석음의 위험', 11: '젊을 때 심으라', 12: '창조주를 기억하라',
}

# Badge fixes determined from audit
badge_fixes = {
    1: [(1,'2-11'), (2,'2-11')],  # split MSG 2-11
    4: [(4,'7-8'), (5,'7-8'), (6,'9-10'), (9,'13-16')],
    5: [(6,'8-9'), (10,'13-17'), (11,'18-20')],
    6: [(0,'1-2'), (1,'1-2')],  # split MSG 1-2
    10: [(5,'5-7')],  # partial, need full
    11: [(2,'3-4'), (5,'7-8'), (6,'9')],
}

splits = {
    1: [('2-11', [1, 2])],
    4: [('7-8', [4, 5])],
    6: [('1-2', [0, 1])],
}

# Build fixes
en_fixes = []
for ch in range(1, 13):
    e = en[ch]
    m = msg[ch]
    msg_ranges = [r for r,_ in m]
    
    new_ranges = e['verseRanges'][:]
    ch_splits = []
    changes = []
    
    if ch in badge_fixes:
        for idx, badge in badge_fixes[ch]:
            if idx < len(new_ranges):
                new_ranges[idx] = badge
        changes.append(f'Corrected {len(badge_fixes[ch])} verse badges to match MSG')
    
    if ch in splits:
        for msg_range, idxs in splits[ch]:
            ch_splits.append({
                'msg_range': msg_range,
                'paragraphs': idxs,
                'note': f'MSG {msg_range} split into {len(idxs)} paragraphs'
            })
        changes.append(f'Declared {len(splits[ch])} MSG splits')
    
    en_fixes.append({
        'chapter': ch,
        'title': e['title'],
        'paragraphs': e['paragraphs'],
        'verseRanges': new_ranges,
        'msg_ranges': msg_ranges,
        'merges': [],
        'splits': ch_splits,
        'changes': changes,
        'confirmations_needed': []
    })

json.dump(en_fixes, open('fixes/en_Ecclesiastes.json','w'), ensure_ascii=False, indent=2)
print(f"EN Ecclesiastes: {len(en_fixes)} chapters")
