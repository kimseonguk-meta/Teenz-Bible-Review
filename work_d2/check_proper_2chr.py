#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""D2 게이트 4: MSG 2Chronicles(13-36) 고유명사·숫자 vs Teen EN 기계적 완전성 검사.
   대문자 토큰/숫자를 MSG에서 추출해 EN 본문에 등장하는지 확인.
   paraphrase로 정당하게 바뀐 경우는 수동 판정용 리포트로 출력."""
import json, re

TXT = '/home/hatch/workspace/teenz-bible-review/msg_2Chronicles.txt'
EN = json.load(open('/home/hatch/workspace/teenz-bible-review/fixes/en_2Chronicles.json', encoding='utf-8'))

pat_full = re.compile(r'^(\d{1,2})\s+(\d{1,3}(?:-\d{1,3})?)\s')
pat_single = re.compile(r'^(\d{1,3})\s')
pat_range = re.compile(r'^(\d{1,3})-(\d{1,3})\s')
EXC = {272}
txt = open(TXT, encoding='utf-8').read().split('\n')
ch_text, cur = {}, None
for i, line in enumerate(txt):
    ln = i + 1; s = line.strip()
    if not s or s.startswith('###') or s == '* * *': continue
    m = pat_full.match(line)
    if m:
        n = int(m.group(1))
        if cur is None or n == cur + 1: cur = n
        ch_text.setdefault(cur, []).append(line[m.end():]); continue
    if pat_range.match(line):
        m2 = pat_range.match(line); ch_text.setdefault(cur, []).append(line[m2.end():]); continue
    m = pat_single.match(line)
    if m:
        n = int(m.group(1))
        if ln in EXC: ch_text.setdefault(cur, []).append(line[m.end():]); continue
        if cur is None or n == cur + 1: cur = n; ch_text.setdefault(cur, []).append(line[m.end():]); continue
        ch_text.setdefault(cur, []).append(line[m.end():]); continue
    if cur: ch_text[cur].append(line)

STOP = {'The','And','But','Then','When','He','She','It','They','His','Her','Their','God','Lord',
        'Israel','Judah','Jerusalem','King','So','Now','For','With','From','That','This','You',
        'Your','We','Our','All','As','At','In','Of','On','To','By','A','An','I','My','Me','No',
        'Yes','If','Or','Up','Out','Don','Did','Was','Were','Had','Has','Have','Will','Would',
        'Can','Could','What','Why','How','Who','Which','There','Here','O','Ah','Alright','After',
        'Before','Because','Even','Just','Like','Let','Listen','Look','Make','Not','One','Some',
        'Take','Tell','Well','Yet','Still','Also','Every','Meanwhile','Finally','Later','First',
        'Second','Third','Meanwhile','Meanwhile'}
# 단, God/Lord/Israel/Judah/Jerusalem/King은 고유명사지만 너무 흔해 제외(의미상 핵심은 별도 수동 확인)

en_map = {c['chapter']: ' '.join(c['paragraphs']) for c in EN}
report = []
for ch in sorted(ch_text):
    msg = ' '.join(ch_text[ch])
    en = en_map.get(ch, '')
    en_low = en.lower()
    en_digits = re.sub(r'[^0-9]', '', en)
    # 고유명사 후보: 대문자로 시작하는 2자 이상 단어
    names = set(re.findall(r'\b[A-Z][a-zA-Z]{1,}(?:[\'-][A-Za-z]+)?\b', msg))
    # 숫자: 1,000 / 400000 / 7,700 등
    nums = set(re.findall(r'\b\d[\d,]*\b', msg))
    miss_names = sorted(n for n in names if n not in STOP and n.lower() not in en_low and n not in en)
    miss_nums = []
    for nm in nums:
        digits = nm.replace(',', '')
        if digits not in en_digits and nm not in en:
            # 연도/나이 등은 문장으로 풀어쓸 수 있어 수동 확인
            miss_nums.append(nm)
    if miss_names or miss_nums:
        report.append((ch, miss_names, sorted(miss_nums, key=lambda x: int(x.replace(',','')))))

for ch, nn, nums in report:
    print(f'--- ch{ch} ---')
    if nn: print('  NAMES:', ', '.join(nn))
    if nums: print('  NUMS:', ', '.join(nums))
print(f'\n총 {len(report)}개 장에서 후보 누락')
