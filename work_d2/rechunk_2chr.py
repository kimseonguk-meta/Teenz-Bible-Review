#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""D2 2Chronicles MSG 문단 경계 재청킹 (2026-09-23).
batch 초벌 unit 배지를 MSG 원문(parse_msg_txt) unit 배지와 1:1로 맞춤.
- split: EN/KO 앵커 문장으로 실제 절단 (배지만 바꾸지 않음)
- merge: 임의 merge/split이 아니라 MSG unit 복원용 결합
- 내용 수정: ch25 고용비 4톤->4.5톤, ch21 '10-11' KO 주어 오류(여호사밧->여호람),
  ch33:20 누락 문장 추가
"""
import importlib.util, copy, sys

WORK = '/home/hatch/workspace/teenz-bible-review/work_d2'

def load_batch(name):
    spec = importlib.util.spec_from_file_location(name, f'{WORK}/{name}.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.CHAPTERS

def get(units, badge):
    for u in units:
        if u['badge'] == badge: return u
    raise KeyError(badge)

def split_unit(u, new_badges, en_anchors, ko_anchors):
    """en_anchors[i]/ko_anchors[i] = i번째 새 piece의 시작 문장. 0번은 None(맨 앞부터)."""
    n = len(new_badges)
    assert len(en_anchors) == len(ko_anchors) == n
    assert en_anchors[0] is None and ko_anchors[0] is None
    en_txt, ko_txt = u['en'], u['ko']
    en_bounds, ko_bounds = [0], [0]
    for i in range(1, n):
        ea, ka = en_anchors[i], ko_anchors[i]
        ie = en_txt.find(ea, en_bounds[-1])
        ik = ko_txt.find(ka, ko_bounds[-1])
        assert ie > 0, (u['badge'], ea[:50])
        assert ik > 0, (u['badge'], ka[:30])
        en_bounds.append(ie); ko_bounds.append(ik)
    en_bounds.append(len(en_txt)); ko_bounds.append(len(ko_txt))
    out = []
    for i, b in enumerate(new_badges):
        nu = copy.deepcopy(u)
        nu['badge'] = b; nu['mr'] = b
        nu['en'] = en_txt[en_bounds[i]:en_bounds[i+1]].strip()
        nu['ko'] = ko_txt[ko_bounds[i]:ko_bounds[i+1]].strip()
        assert nu['en'] and nu['ko'], (u['badge'], b)
        if i > 0:
            nu['header_en'] = None; nu['header_ko'] = None
        out.append(nu)
    return out

def merge_units(units_list, new_badge):
    base = copy.deepcopy(units_list[0])
    base['badge'] = new_badge; base['mr'] = new_badge
    base['en'] = ' '.join(x['en'].strip() for x in units_list).strip()
    base['ko'] = ' '.join(x['ko'].strip() for x in units_list).strip()
    return base

def note(C, ch, msg):
    C[ch]['changes'].append(msg)

B1 = load_batch('batch1_13_16')
B2 = load_batch('batch2_17_20')
B3 = load_batch('batch3_21_25')
B4 = load_batch('batch4_26_29')
B5 = load_batch('batch5_30_33')
B6 = load_batch('batch6_34_36')

# ---------- ch13 ----------
C = B1; ch = 13
units = C[ch]['units']
u = get(units, '3'); u['badge'] = '2-3'; u['mr'] = '2-3'
note(C, ch, 'MSG 문단 경계 재청킹: [3] -> [2-3] (2026-09-23)')

# ---------- ch21 ----------
C = B3; ch = 21
units = C[ch]['units']
nu = []
for u in units:
    b = u['badge']
    if b == '1-4':
        nu += split_unit(u, ['1','2-4'],
            [None, 'He had brothers, sons of Jehoshaphat:'],
            [None, '여호사밧의 아들인 형제들이 있었어.'])
    elif b == '5-6':
        u2 = get(units, '7')
        nu.append(merge_units([u, u2], '5-7'))
    elif b == '7':
        continue
    elif b == '8-11':
        parts = split_unit(u, ['8-9','10-11'],
            [None, 'Edom continues in revolt against Judah right up to the present.'],
            [None, '에돔은 지금까지도 유다에 대한 반역을 계속하고 있어.'])
        parts[1]['ko'] = parts[1]['ko'].replace(
            '여호사밧이 세운 동네 음란 종교 산당도 하나.',
            '여호람이 세운 동네 음란 종교 산당도 하나.')
        nu += parts
    elif b == '16-18':
        u2 = get(units, '19'); u3 = get(units, '20')
        nu.append(merge_units([u, u2, u3], '16-20'))
    elif b in ('19','20'):
        continue
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 1-4분할, 5-6+7병합, 8-11분할, 16-18+19+20병합 (2026-09-23)')

# ---------- ch22 ----------
C = B3; ch = 22
units = C[ch]['units']
nu = []
for u in units:
    if u['badge'] == '10':
        u2 = get(units, '11-12')
        nu.append(merge_units([u, u2], '10-12'))
    elif u['badge'] == '11-12':
        continue
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 10+11-12병합 (2026-09-23)')

# ---------- ch23 ----------
C = B3; ch = 23
units = C[ch]['units']
nu = []
for u in units:
    b = u['badge']
    if b == '4-7':
        u['badge'] = '3-7'; u['mr'] = '3-7'; nu.append(u)
    elif b == '12-15':
        nu += split_unit(u, ['12-13','14-15'],
            [None, 'The priest Jehoiada gave orders to the captains who were in charge of the army'],
            [None, '제사장 여호야다가 군대를 맡은 지휘관들에게 명령했어.'])
    elif b == '16-17':
        nu += split_unit(u, ['16','17'],
            [None, 'The people poured into the temple of Baal'],
            [None, '백성이 바알 신전으로 몰려가'])
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 4-7->3-7, 12-15분할, 16-17분할 (2026-09-23)')

# ---------- ch24 ----------
C = B3; ch = 24
units = C[ch]['units']
nu = []
p11a = p12a = p14b = None
for u in units:
    b = u['badge']
    if b == '1-3':
        nu += split_unit(u, ['1','2-3'],
            [None, 'Taught and trained by Jehoiada the priest'],
            [None, '여호야다 제사장에게 가르침과 훈련을 받은 요아스는'])
    elif b == '4-7':
        nu += split_unit(u, ['4-6','7'],
            [None, 'The king called for Jehoiada, the chief priest'],
            [None, '왕이 대제사장 여호야다를 불러 말했어.'])
    elif b == '8-11':
        parts = split_unit(u, ['8-9','10','11x'],
            [None, 'People were delighted to do it', 'Every time the chest was full'],
            [None, '백성은 기쁘게 했어.', '궤가 찰 때마다 레위인들이 왕의 관리들에게 가져왔지.'])
        nu += parts[:2]; p11a = parts[2]
    elif b == '12-14':
        parts = split_unit(u, ['12-14x','14y'],
            [None, "During Jehoiada's lifetime, they continued to offer Whole-Burnt-Offerings at The Temple of God."],
            [None, '여호야다가 살아 있는 동안 하나님의 성전에서 번제를 계속 드렸어.'])
        p12a, p14b = parts
    elif b == '15-16':
        u1114 = merge_units([p11a, p12a], '11-14')
        u1416 = merge_units([p14b, u], '14-16')
        nu += [u1114, u1416]
    elif b == '20-22':
        nu += split_unit(u, ['20','21-22'],
            [None, 'But they conspired against him'],
            [None, '하지만 그들이 공모했어.'])
    elif b == '25':
        u2 = get(units, '26-27')
        nu.append(merge_units([u, u2], '25-27'))
    elif b == '26-27':
        continue
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 1-3/4-7/8-11/12-14/20-22 분할, 11-14·14-16 재결합, 25+26-27병합 (2026-09-23)')

# ---------- ch25 ----------
C = B3; ch = 25
units = C[ch]['units']
nu = []
p14a = None
for u in units:
    b = u['badge']
    if b == '1-4':
        nu.append(u)
    elif b == '5-8':
        parts = split_unit(u, ['5-6','7-8','9','10'],
            [None, 'A holy man showed up and said,',
             'Amaziah said to the holy man,',
             'So Amaziah dismissed the hired soldiers and sent them home.'],
            [None, '한 성자가 나타나 말했어.',
             '아마샤가 성자에게 말했어.',
             '그래서 아마샤가 고용병들을 해산시키고 집으로 보냈어.'])
        parts[0]['en'] = parts[0]['en'].replace('about four tons of silver', 'about four and a half tons of silver')
        parts[0]['ko'] = parts[0]['ko'].replace('은 4톤 정도를', '은 4.5톤 정도를')
        nu += parts
    elif b == '9-10':
        u['badge'] = '11-12'; u['mr'] = '11-12'; nu.append(u)
    elif b == '11-12':
        u['badge'] = '13'; u['mr'] = '13'; nu.append(u)
    elif b == '13':
        p14a = u; p14a['badge'] = '14a'; p14a['mr'] = '14a'
    elif b == '14-16':
        parts = split_unit(u, ['15x','16'],
            [None, 'The prophet was still speaking when Amaziah interrupted:'],
            [None, '선지자가 말하고 있는데 아마샤가 끼어들었어.'])
        nu.append(merge_units([p14a, parts[0]], '14-15'))
        nu.append(parts[1])
    elif b == '17-19':
        nu += split_unit(u, ['17','18-19'],
            [None, 'Jehoash, king of Israel, replied to Amaziah, king of Judah:'],
            [None, '이스라엘 왕 여호아스가 유다 왕 아마샤에게 답했어.'])
    elif b == '20-21':
        u['badge'] = '20-22'; u['mr'] = '20-22'; nu.append(u)
    elif b == '22-24':
        u['badge'] = '23-24'; u['mr'] = '23-24'; nu.append(u)
    elif b == '25-28':
        nu += split_unit(u, ['25-26','27-28'],
            [None, 'From the time Amaziah stopped following God, there was a conspiracy to get rid of him in Jerusalem.'],
            [None, '아마샤가 하나님 따르기를 그만둔 때부터 예루살렘에서 그를 제거하려는 음모가 있었어.'])
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 5-8 4분할(고용비 4.5톤 수정), 9-10->11-12, 11-12->13, 13+14-16->14-15+16, 17-19분할, 20-21->20-22, 22-24->23-24, 25-28분할 (2026-09-23)')

# ---------- ch26 ----------
C = B4; ch = 26
units = C[ch]['units']
nu = []
for u in units:
    b = u['badge']
    if b == '1-5':
        nu += split_unit(u, ['1-2','3-5'],
            [None, 'Uzziah was sixteen years old when he became king and ruled in Jerusalem for fifty-two years.'],
            [None, '웃시야는 왕이 될 때 16살이었고 예루살렘에서 52년 동안 다스렸어.'])
    elif b == '9-15':
        nu += split_unit(u, ['9-10','11-15'],
            [None, 'Uzziah had a well-trained army ready to fight'],
            [None, '웃시야에게는 잘 훈련된 싸울 준비된 군대가 있었어.'])
    elif b == '16-21':
        nu += split_unit(u, ['16-18','19-21'],
            [None, 'They grabbed him and rushed him out of there.'],
            [None, '그를 붙잡아 서둘러 내보냈지.'])
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 1-5/9-15/16-21 분할 (2026-09-23)')

# ---------- ch28 ----------
C = B4; ch = 28
units = C[ch]['units']
nu = []
for u in units:
    b = u['badge']
    if b == '5-7':
        nu.append(u)  # 아래 8-15 분할과 결합
    elif b == '8-15':
        parts = split_unit(u, ['8x','9-11','12-15'],
            [None, 'A prophet of God named Oded was in the neighborhood.',
             'Some of the leaders of the tribe of Ephraim'],
            [None, '오뎃이라는 하나님의 선지자가 근처에 있었지.',
             '에브라임 지파의 지도자 몇 명'])
        prev = nu.pop()  # 5-7
        assert prev['badge'] == '5-7'
        nu.append(merge_units([prev, parts[0]], '5-8'))
        nu.append(parts[1])
        nu += split_unit(parts[2], ['12-13','14-15'],
            [None, 'So the soldiers returned the captives and the plunder to the leaders and the congregation.'],
            [None, '그래서 병사들이 포로들과 전리품을 지도자들과 회중에게 돌려줬어.'])
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 5-7+8-15 -> 5-8+9-11+12-13+14-15 (2026-09-23)')

# ---------- ch29 ----------
C = B4; ch = 29
units = C[ch]['units']
nu = []
p1217 = None
for u in units:
    b = u['badge']
    if b == '12-15':
        p1217 = u
    elif b == '16-19':
        parts = split_unit(u, ['17x','18-19'],
            [None, 'They reported to Hezekiah the king:'],
            [None, '히스기야 왕에게 보고했지.'])
        nu.append(merge_units([p1217, parts[0]], '12-17'))
        nu.append(parts[1])
    elif b == '25-30':
        nu += split_unit(u, ['25-26','27-30'],
            [None, 'The Levites formed the orchestra'],
            [None, '레위인들이 오케스트라를 이뤄'])
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 12-15+16-19 -> 12-17+18-19, 25-30분할 (2026-09-23)')

# ---------- ch29 ----------
C = B4; ch = 29
units = C[ch]['units']
nu = []
for u in units:
    if u['badge'] == '31-36':
        nu += split_unit(u, ['31-35','36'],
            [None, 'Hezekiah and the people were overjoyed'],
            [None, '히스기야와 백성이 크게 기뻐했어.'])
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 31-36분할 (2026-09-23)')

# ---------- ch30 ----------
C = B5; ch = 30
units = C[ch]['units']
nu = []
p1317 = None
for u in units:
    b = u['badge']
    if b == '13-14':
        p1317 = u
    elif b == '15-20':
        parts = split_unit(u, ['17x','18-19','20'],
            [None, "Many in the congregation hadn't consecrated themselves",
             'And God listened to Hezekiah and healed the people.'],
            [None, '회중 중 많은 이가 자신을 거룩하게 하지 못했기에',
             '하나님이 히스기야의 말을 들으시고 백성을 고치셨어.'])
        nu.append(merge_units([p1317, parts[0]], '13-17'))
        nu += parts[1:]
    elif b == '23-27':
        nu += split_unit(u, ['22-23','24-26','27'],
            [None, 'Hezekiah king of Judah gave the congregation a thousand bulls',
             'The priests and Levites got up and blessed the people.'],
            [None, '유다 왕 히스기야가 회중에게 제물로 수소 1,000마리와 양 7,000마리를 줬고',
             '제사장들과 레위인들이 일어나 백성을 축복했어.'])
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 13-14+15-20 -> 13-17+18-19+20, 23-27 -> 22-23+24-26+27 (2026-09-23)')

# ---------- ch31 ----------
C = B5; ch = 31
units = C[ch]['units']
nu = []
for u in units:
    b = u['badge']
    if b == '2-4':
        nu += split_unit(u, ['2','3','4'],
            [None, 'He also designated his own personal contribution',
             'In addition, he asked the people'],
            [None, '또 번제를 위한 자기 개인 헌금을 지정했지.',
             '게다가 예루살렘에 사는 백성에게'])
    elif b == '5-10':
        nu += split_unit(u, ['5-7','8-9','10'],
            [None, 'When Hezekiah and his leaders came',
             'Hezekiah asked the priests and Levites about the heaps'],
            [None, '히스기야와 지도자들이 와서',
             '히스기야가 제사장들과 레위인들에게 헌금 더미에 대해 묻자'])
    elif b == '11-19':
        nu += split_unit(u, ['11-18','19'],
            [None, 'The priests, the descendants of Aaron, were allotted portions'],
            [None, '제사장들, 곧 아론 자손에게는'])
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 2-4/5-10/11-19 분할 (2026-09-23)')

# ---------- ch32 ----------
C = B5; ch = 32
units = C[ch]['units']
nu = []
u20 = u2122a = None
u2223 = None
for u in units:
    b = u['badge']
    if b == '1-8':
        nu += split_unit(u, ['1','2-4','5-6','6-8'],
            [None, 'When Hezekiah realized that Sennacherib had come',
             'Hezekiah also went to work repairing every part of the wall',
             'He gave them this speech of encouragement:'],
            [None, '히스기야가 산헤립이 예루살렘을 치려는 의도로 온 걸 깨닫고',
             '히스기야는 또 손상된 성벽 곳곳을 수리하고',
             '이렇게 격려 연설을 했어.'])
    elif b == '16-19':
        nu += split_unit(u, ['16','17','18-19'],
            [None, 'Sennacherib also wrote letters cursing',
             'The Assyrians then shouted in Hebrew'],
            [None, '산헤립은 또 편지를 써서',
             '앗수르 사람들이 성벽 위에 있는 예루살렘 백성에게 히브리어로 외쳤어.'])
    elif b == '20':
        u20 = u
    elif b == '21-22':
        parts = split_unit(u, ['21x','22a'],
            [None, 'God saved Hezekiah and Jerusalem from Sennacherib'],
            [None, '하나님이 히스기야와 예루살렘을 앗수르 왕 산헤립과 다른 모든 이에게서 구하셨어.'])
        u2122a = parts[0]; u2223 = parts[1]
    elif b == '23-26':
        parts = split_unit(u, ['22b','24','25-26'],
            [None, 'Some time later, Hezekiah became deathly sick.',
             'But Hezekiah became proud'],
            [None, '얼마 후 히스기야가 죽을병에 걸렸어.',
             '하지만 히스기야가 교만해져'])
        nu.append(merge_units([u20, u2122a], '20-21'))
        nu.append(merge_units([u2223, parts[0]], '22-23'))
        nu += parts[1:]
    elif b == '27-29':
        nu.append(u)
    elif b == '30':
        prev = nu.pop(); assert prev['badge'] == '27-29'
        nu.append(merge_units([prev, u], '27-29x'))
    elif b == '31':
        prev = nu.pop(); assert prev['badge'] == '27-29x'
        nu.append(merge_units([prev, u], '27-31'))
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 1-8 4분할, 16-19 3분할, 20+21-22+23-26 재배합, 27-29+30+31병합 (2026-09-23)')

# ---------- ch33 ----------
C = B5; ch = 33
units = C[ch]['units']
nu = []
p9 = q10 = None
for u in units:
    b = u['badge']
    if b == '1-9':
        parts = split_unit(u, ['1-6','7-8','9x'],
            [None, "He put the sex-and-religion idol he had made in God's Temple",
             'But Manasseh led Judah and the citizens of Jerusalem off the beaten path'],
            [None, '자기가 만든 음란 종교 우상을 하나님의 성전에 두었어.',
             '하지만 므낫세는 유다와 예루살렘 주민들을 바른 길에서 벗어나'])
        nu += parts[:2]; p9 = parts[2]
    elif b == '10-13':
        parts = split_unit(u, ['10x','11-13'],
            [None, 'Then God directed the leaders of the troops of the king of Assyria'],
            [None, '그러자 하나님이 앗수르 왕의 군대 지휘관들을'])
        q10 = parts[0]
        nu.append(merge_units([p9, q10], '9-10'))
        nu.append(parts[1])
    elif b == '14':
        nu.append(u)
    elif b == '15-17':
        prev = nu.pop(); assert prev['badge'] == '14'
        nu.append(merge_units([prev, u], '14-17'))
    elif b == '18-20':
        u['badge'] = '18-19'; u['mr'] = '18-19'
        nu.append(u)
        nu.append({'badge': '20', 'mr': '20', 'header_en': None, 'header_ko': None,
            'en': 'When Manasseh died, they buried him in the palace garden. His son Amon was the next king.',
            'ko': '므낫세가 죽자 궁전 정원에 장사했어. 아들 아몬이 다음 왕이 되었지.'})
    elif b == '21-25':
        nu += split_unit(u, ['21-23','24-25'],
            [None, 'The officers in his court plotted against him'],
            [None, '궁중 신하들이 공모해 집에서 그를 죽였어.'])
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 1-9 3분할+9-10재결합, 14+15-17병합, 18-20->18-19+20(20절 누락 복원), 21-25분할 (2026-09-23)')

# ---------- ch34 ----------
C = B6; ch = 34
units = C[ch]['units']
nu = []
for u in units:
    b = u['badge']
    if b == '1-7':
        nu += split_unit(u, ['1-2','3-7'],
            [None, 'When he was still a young man — in the eighth year of his reign — he started out on the path to God, the God of David his ancestor.'],
            [None, '아직 젊은 청년일 때 — 왕이 된 지 8년째 — 조상 다윗의 하나님께로 향하는 길을 걷기 시작했어.'])
    elif b == '14-18':
        nu += split_unit(u, ['14-17','18'],
            [None, 'Then Shaphan the secretary told the king, \u201cHilkiah the priest gave me a book.\u201d'],
            [None, '그리고 서기관 사반이 왕에게 말했어.'])
    elif b == '19':
        nu.append(u)
    elif b == '20-22':
        prev = nu.pop(); assert prev['badge'] == '19'
        nu.append(merge_units([prev, u], '19-21'))
    elif b == '23-28':
        nu += split_unit(u, ['22-25','26-28'],
            [None, 'And also tell the king of Judah who sent you to pray to God:'],
            [None, '그리고 하나님께 기도하라고 너희를 보낸 유다 왕에게도 전하라.'])
    elif b == '32-33':
        nu += split_unit(u, ['32','33'],
            [None, 'Josiah did a thorough job of cleaning up the place'],
            [None, '요시야가 그곳을 철저히 청소했어.'])
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 1-7분할, 14-18분할, 19+20-22병합, 23-28분할, 32-33분할 (2026-09-23)')

# ---------- ch35 ----------
C = B6; ch = 35
units = C[ch]['units']
nu = []
p2425a = None
for u in units:
    b = u['badge']
    if b == '1-6':
        nu += split_unit(u, ['1-4','5-6'],
            [None, 'Take your place in the Sanctuary based on your family divisions among your brothers, the laypeople'],
            [None, '평신도 형제들 중 가문 구분에 따라 성전에 자리를 잡아.'])
    elif b == '10-14':
        nu += split_unit(u, ['10-13','14','15'],
            [None, 'Afterward, the Levites got what was due to them',
             'The singers, the sons of Asaph, were all in their places'],
            [None, '그 후 레위인들이 자기들과 제사장들 — 아론의 아들들 — 의 몫을 챙겼어.',
             '노래하는 이들, 아삽 자손은 모두 자기 자리에 있었어.'])
    elif b == '15-19':
        u['badge'] = '16-19'; u['mr'] = '16-19'; nu.append(u)
    elif b == '20-24':
        parts = split_unit(u, ['20','21','22-23','24-25x'],
            [None, 'Neco sent messengers to Josiah:',
             'But Josiah was stubborn.',
             'So his servants took him out of the chariot and laid him in the second chariot.'],
            [None, '느고가 요시야에게 전령을 보냈어.',
             '하지만 요시야는 고집이 셌어.',
             '그래서 신하들이 그를 전차에서 내려 두 번째 전차에 눕혔어.'])
        nu += parts[:3]; p2425a = parts[3]
    elif b == '25':
        nu.append(merge_units([p2425a, u], '24-25'))
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 1-6분할, 10-14 3분할, 15-19->16-19, 20-24 4분할+25병합 (2026-09-23)')

# ---------- ch36 ----------
C = B6; ch = 36
units = C[ch]['units']
nu = []
u1516 = None
for u in units:
    b = u['badge']
    if b == '1-4':
        nu += split_unit(u, ['1-3','4'],
            [None, 'Then Neco king of Egypt made Eliakim'],
            [None, '그러자 이집트 왕 느고가 여호아하스의 형 엘리야김을'])
    elif b == '5-8':
        nu += split_unit(u, ['5','6-7','8'],
            [None, 'Nebuchadnezzar king of Babylon attacked him',
             'The rest of the life and times of Jehoiakim'],
            [None, '느부갓네살이 그를 쳐서 쇠사슬로 묶어 바빌론으로 끌고 갔어.',
             '여호야김의 나머지 생애와 치세'])
    elif b == '11-14':
        nu += split_unit(u, ['11-13','14'],
            [None, 'The evil mindset spread to the leaders'],
            [None, '악한 사고방식이 지도자들과 제사장들에게 퍼져'])
    elif b == '15-16':
        u1516 = u
    elif b == '17-21':
        parts = split_unit(u, ['17x','18-20','21'],
            [None, 'He also took into Babylon all the furnishings',
             "This is exactly the message of God's word that Jeremiah had preached"],
            [None, '또 하나님의 성전의 대소 기구와',
             '이건 예레미야가 전한 하나님의 말씀 그대로야.'])
        nu.append(merge_units([u1516, parts[0]], '15-17'))
        nu += parts[1:]
    else:
        nu.append(u)
C[ch]['units'] = nu
note(C, ch, 'MSG 문단 경계 재청킹: 1-4분할, 5-8 3분할, 11-14분할, 15-16+17-21 재배합 (2026-09-23)')

# ---------- 검증: MSG parse 배지와 1:1 ----------
sys.path.insert(0, '/home/hatch/workspace/teenz-bible-review/gdocs_build')
import build_gdocs as bg
units = bg.parse_msg_txt('/home/hatch/workspace/teenz-bible-review/msg_2Chronicles.txt')
def badge(u):
    v = sorted(u['verses']); return f"{v[0]}-{v[-1]}" if len(v) > 1 else str(v[0])
msg_map = {}
for u in units:
    msg_map.setdefault(u['chapter'], []).append(badge(u))

ALL = {}
for name, B in [('batch1_13_16',B1),('batch2_17_20',B2),('batch3_21_25',B3),
                ('batch4_26_29',B4),('batch5_30_33',B5),('batch6_34_36',B6)]:
    ALL.update(B)

bad = 0
for ch in sorted(ALL):
    mine = [u['badge'] for u in ALL[ch]['units']]
    want = msg_map.get(ch)
    if mine != want:
        bad += 1
        print(f'ch{ch} MISMATCH\n  mine={mine}\n  want={want}')
print('badge check:', 'ALL MATCH' if bad == 0 else f'{bad} chapters mismatch')

# ---------- 파일 기록 ----------
import io
def dump(name, B):
    path = f'{WORK}/{name}.py'
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write('# -*- coding: utf-8 -*-\n')
        f.write('"""2Chronicles teen EN/KO (작업자 D2, MSG 문단 경계 재청킹 2026-09-23)."""\n')
        f.write('CHAPTERS = ')
        f.write(repr(B))
        f.write('\n')

# 원본 백업
import shutil, os
os.makedirs(f'{WORK}/backup_pre_rechunk', exist_ok=True)
for n in ['batch1_13_16','batch2_17_20','batch3_21_25','batch4_26_29','batch5_30_33','batch6_34_36']:
    shutil.copy(f'{WORK}/{n}.py', f'{WORK}/backup_pre_rechunk/{n}.py')
print('backup done')
for n, B in [('batch1_13_16',B1),('batch2_17_20',B2),('batch3_21_25',B3),
             ('batch4_26_29',B4),('batch5_30_33',B5),('batch6_34_36',B6)]:
    dump(n, B)
print('dump done')
