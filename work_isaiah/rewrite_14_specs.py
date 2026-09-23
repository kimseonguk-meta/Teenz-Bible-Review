#!/usr/bin/env python3
"""14개 잘못된 Isaiah 스펙을 라이브 MSG 구조에 맞춰 재작성.

원칙:
- spec['badges'] = 라이브 MSG 섹션 라벨 (검증된 manifest)
- spec['msg'] = 라이브 MSG 섹션 라벨 (build.py가 verseRanges/msg_ranges로 사용)
- 읽기 전용 원본 문단은 keep/join으로만 재구성, MSG 문단 병합은 merges[] + confirmations_needed[] 기록
- split verse (ch10 v13, v27)는 splits[] 선언
- 확인된 텍스트 수정만 'new'로 적용, 잘못된 old 변경은 원본 keep으로 복원
"""
import json, glob, os, copy

BASE = os.path.dirname(os.path.abspath(__file__))
en_src = {c['num']: c for c in json.load(open(os.path.join(BASE, 'en_isaiah.json')))}
ko_src = {c['num']: c for c in json.load(open(os.path.join(BASE, 'ko_isaiah.json')))}

specs = {}
spec_files = {}
for f in sorted(glob.glob(os.path.join(BASE, 'specs_*.json'))):
    for c in json.load(open(f)):
        specs[c['chapter']] = c
        spec_files[c['chapter']] = f

# 라이브 MSG 섹션 manifest (2026-09-22 BibleGateway 대조 검증)
LIVE = {
    1:  ['1','2-4','5-9','10','11-12','13-17','18-20','21-23','24-31'],
    2:  ['1-5','6-9','10','11-17','18','19','20-21','22'],
    3:  ['1-7','8-9','10-11','12','13-15','16-17','18-23','24','25-26'],
    4:  ['1','2-4','5-6'],
    5:  ['1-2','3-4','5-6','7','8-10','11-17','18-19','20','21-23','24','25-30'],
    6:  ['1-8','9-10','11-13'],
    10: ['1-4','5-11','12-13','13-14','15-19','20-23','24-27','27-32','33-34'],
    13: ['1','2-3','4-5','6-8','9-16','17-22'],
    14: ['1-2','3-6','7-10','11','12','13-14','15-17','18-20','21','22-23','24-27','28-31','32'],
    18: ['1-2','3','4-6','7'],
    20: ['1-2','3-6'],
    23: ['1-4','5','6-12','13','14','15-16','17-18'],
    33: ['1','2-4','5-6','7-9','10-12','13-14','15-16','17-19','20-22','23','24'],
    34: ['1','2-4','5-7','8-15','16-17'],
}

def keeps(n):
    return [{'keep': i} for i in range(n)]

def base_spec(ch):
    """기존 spec의 title/ko_title/changes를 유지하고 구조 필드만 갈아끼울 틀."""
    old = specs[ch]
    return {
        'chapter': ch,
        'title': old.get('title', en_src[ch]['title']),
        'ko_title': old.get('ko_title', ko_src[ch]['title']),
        'changes': [],
        'ko_changes': [],
    }

def set_live(ch, spec, en_ops, ko_ops, merges=None, confirmations=None,
             splits=None, changes=None, ko_changes=None):
    spec['badges'] = LIVE[ch]
    spec['msg'] = LIVE[ch]
    spec['en_ops'] = en_ops
    spec['ko_ops'] = ko_ops
    spec['merges'] = merges or []
    spec['confirmations_needed'] = confirmations or []
    spec['splits'] = splits or []
    spec['changes'] = changes or []
    spec['ko_changes'] = ko_changes or spec.get('ko_changes', [])
    n_en = len(en_ops); n_ko = len(ko_ops); n_b = len(LIVE[ch])
    assert n_en == n_b, f'ch{ch}: EN ops {n_en} != badges {n_b}'
    assert n_ko == n_b, f'ch{ch}: KO ops {n_ko} != badges {n_b}'
    return spec

def merge_entry(scope, rng, reason):
    return {'scope': scope, 'msg_ranges': [rng], 'reason': reason}

def conf(ch, text):
    return f'ch{ch}: {text} (MSG 문단 합병)'

# ---------- 텍스트 수정 (원본에서 파생) ----------
E = lambda ch, i: en_src[ch]['paragraphs'][i]
K = lambda ch, i: ko_src[ch]['paragraphs'][i]

# ch1: 1:20 MSG 복원 + 거친 표현 완화
ch1_en6 = E(1,6).replace('you\u2019ll be devoured by the sword', "you'll die like dogs")
assert 'die like dogs' in ch1_en6 and 'devoured' not in ch1_en6
ch1_ko6 = K(1,6).replace('칼에 삼켜질 거야', '개처럼 죽을 거야')
assert '개처럼 죽을 거야' in ch1_ko6 and '칼에 삼켜' not in ch1_ko6
ch1_ko1 = K(1,1).replace('엇나간 놈들', '엇나간 녀석들').replace('죄책감에 쩔어서', '죄책감에 짓눌려서')
assert '놈들' not in ch1_ko1 and '쩔어서' not in ch1_ko1
ch1_ko8 = K(1,8).replace('억압하는 놈들', '억압하는 녀석들')
assert '억압하는 놈들' not in ch1_ko8

# ch10: 기존 KO 따옴표/재물 수정 유지 (파일 관용 = straight quotes)
ch10_ko3_new = None
for op in specs[10]['ko_ops']:
    if isinstance(op, dict) and 'new' in op and '재물' in op['new']:
        ch10_ko3_new = op['new']
assert ch10_ko3_new, 'ch10 old KO fix not found'

# ch14: 바벨론 -> 바빌론 (파일 관용, 16:3)
ch14_ko10 = K(14,10).replace('바벨론의 이름', '바빌론의 이름')
assert '바빌론의 이름' in ch14_ko10
ch14_ko1 = K(14,1).replace('바벨론 왕', '바빌론 왕')
ch14_ko3 = K(14,4).replace('바벨론, 너', '바빌론, 너')
ch14_ko4 = K(14,5).replace('바벨론아!', '바빌론아!')
for t in (ch14_ko1, ch14_ko3, ch14_ko4):
    assert '바벨론' not in t

# ch18: 개많은 -> 바글바글한
ch18_ko0 = K(18,0).replace('개많은', '바글바글한')
assert '바글바글한' in ch18_ko0

# ch33: 닫는 따옴표 복원
ch33_en4 = E(33,4) + '"'
ch33_ko4 = K(33,4) + '"'

# ch34: KO v8 두 문장을 [2] -> [3]으로 이동
V8 = '야생 동물이든 가축이든 가리지 않는 대량 학살이 벌어질 거래. 온 땅은 피로 흥건하고, 땅바닥은 지방으로 미끌미끌해질 거임.'
assert V8 in K(34,2)
ch34_ko2 = K(34,2).replace(' ' + V8, '').replace(V8, '')
assert V8 not in ch34_ko2 and ch34_ko2.endswith('도살장이 될 판임.')
ch34_ko3 = V8 + ' ' + K(34,3)

# ---------- 14개 장 스펙 재작성 ----------
new_specs = {}

# ch1: 원본 9문단이 이미 라이브 MSG 구조. 텍스트 수정 4건만 적용.
s = base_spec(1)
en_ops = keeps(9); en_ops[6] = {'new': ch1_en6}
ko_ops = keeps(9); ko_ops[1] = {'new': ch1_ko1}; ko_ops[6] = {'new': ch1_ko6}; ko_ops[8] = {'new': ch1_ko8}
new_specs[1] = set_live(1, s, en_ops, ko_ops,
    changes=["1:20 MSG 'you'll die like dogs' 복원 (KJV 'devoured by the sword' 잔재 수정)",
             "원본 9문단이 라이브 MSG 섹션과 1:1 일치함을 확인 — old spec의 잘못된 재절단('1-3'/'4-9'/...) 폐기"],
    ko_changes=["1:20 '칼에 삼켜질 거야' -> '개처럼 죽을 거야' (MSG 'die like dogs')",
                "거친 표현 완화: '엇나간 놈들'->'엇나간 녀석들', '죄책감에 쩔어서'->'죄책감에 짓눌려서', '억압하는 놈들'->'억압하는 녀석들'"])

# ch2: '1'+'2-5' -> '1-5' 병합. old의 'moles and bats' 오역은 원본('toss them into a ditch') 유지로 복원.
s = base_spec(2)
new_specs[2] = set_live(2, s,
    [{'join': [0,1]}, {'keep':2}, {'keep':3}, {'keep':4}, {'keep':5}, {'keep':6}, {'keep':7}, {'keep':8}],
    [{'join': [0,1]}, {'keep':2}, {'keep':3}, {'keep':4}, {'keep':5}, {'keep':6}, {'keep':7}, {'keep':8}],
    merges=[merge_entry('Isaiah 2:1-5', '1-5',
        "MSG '1-5'는 단일 섹션 ('The Message Isaiah got regarding Judah and Jerusalem' 표제 + 본문). 기존 '1'/'2-5' 분리는 MSG 1:1에 어긋나므로 병합.")],
    confirmations=[conf(2, "기존 '1'/'2-5' → MSG '1-5' 병합")],
    changes=["2:20-21 old patch의 'fields for the moles and bats'는 라이브 MSG('dump them in any ditch or gully')와 불일치 — 원본 'toss them into a ditch' 유지로 복원",
             "old spec의 과도한 5문단 병합 폐기 — '6-9' 이후 문단은 원본 구조가 라이브 MSG와 일치"],
    ko_changes=["2:20-21 KO 원본 '아무 도랑에나 던져버릴 거임' 유지 (MSG 일치)"])

# ch3: 원본 9문단이 라이브 MSG와 일치
s = base_spec(3)
new_specs[3] = set_live(3, s, keeps(9), keeps(9),
    changes=["원본 9문단이 라이브 MSG 섹션과 1:1 일치함을 확인 — old spec의 과도한 병합 폐기"])

# ch4: 원본 3문단이 라이브 MSG와 일치
s = base_spec(4)
new_specs[4] = set_live(4, s, keeps(3), keeps(3),
    changes=["원본 3문단이 라이브 MSG 섹션과 1:1 일치함을 확인 — old spec의 '1-3'/'4-6' 병합 폐기"])

# ch5: 원본 11문단이 라이브 MSG와 일치 ('25-30' 단일 문단)
s = base_spec(5)
new_specs[5] = set_live(5, s, keeps(11), keeps(11),
    changes=["원본 11문단이 라이브 MSG 섹션과 1:1 일치함을 확인 — old spec의 '25-27'/'28-30' 분할 및 과도 병합 폐기 (MSG '25-30'은 단일 문단)"])

# ch6: EN 10문단 / KO 11문단 -> MSG 3문단 병합
s = base_spec(6)
new_specs[6] = set_live(6, s,
    [{'join': [0,1,2,3,4,5,6]}, {'join': [7,8]}, {'keep': 9}],
    [{'join': [0,1,2,3,4,5,6,7]}, {'join': [8,9]}, {'keep': 10}],
    merges=[
        merge_entry('Isaiah 6:1-8', '1-8', "MSG '1-8'은 단일 섹션 (소명 환상 전체). 기존 절별 분리('1-3'/'3'/'4'/...)는 MSG 1:1에 어긋나므로 병합."),
        merge_entry('Isaiah 6:9-10', '9-10', "MSG '9-10'은 단일 섹션 (하나님의 답변). 기존 '9'/'9-10' 분리는 MSG 1:1에 어긋나므로 병합.")],
    confirmations=[conf(6, "기존 '1-3'/'3'/'4'/'5'/'6'/'7'/'8' → MSG '1-8' 병합"),
                   conf(6, "기존 '9'/'9-10' → MSG '9-10' 병합")],
    changes=["라이브 MSG는 3문단('1-8','9-10','11-13'). KO의 '2'/'4'/'5'... 배지는 오기입(내용은 v2/v3/v4...) — 내용 경계 기준 병합"],
    ko_changes=["KO 배지 오기입('4' 배지에 v3 내용 등)은 병합으로 해소 — 내용 경계 기준 '1-8'/'9-10'/'11-13'"])

# ch10: 원본 9문단이 라이브 MSG와 일치 ('27-32' 라벨, v13/v27 splits)
s = base_spec(10)
ko_ops = keeps(9); ko_ops[3] = {'new': ch10_ko3_new}
new_specs[10] = set_live(10, s, keeps(9), ko_ops,
    splits=[{'msg_range': '13', 'note': "MSG 원문 라벨 ('12-13'/'13-14') — v13이 두 섹션에 걸침"},
            {'msg_range': '27', 'note': "MSG 원문 라벨 ('24-27'/'27-32') — v27 본문('On that day, Assyria will be pulled off your back...')은 '24-27' 끝에 있음. 라벨 중복이므로 splits 선언"}],
    changes=["마지막 문단 배지는 라이브 MSG 라벨 그대로 '27-32' (old spec의 '28-32' 수정)",
             "v13 split 유지 ('12-13'/'13-14')"],
    ko_changes=["KO 따옴표 정리(꺾쇠→straight quotes, 파일 관용) 및 '보물'->'재물' 유지"])

# ch13: '17-21'+'22' -> '17-22' 병합
s = base_spec(13)
new_specs[13] = set_live(13, s,
    keeps(5) + [{'join': [5,6]}],
    keeps(5) + [{'join': [5,6]}],
    merges=[merge_entry('Isaiah 13:17-22', '17-22',
        "MSG '17-22'는 단일 섹션 (메대 심판 선언). 기존 '17-21'/'22' 분리는 MSG 1:1에 어긋나므로 병합.")],
    confirmations=[conf(13, "기존 '17-21'/'22' → MSG '17-22' 병합")])

# ch14: 16문단 -> MSG 13문단 (병합 3건), KO 바빌론 오타 수정
s = base_spec(14)
en_ops = [{'keep':0},{'join':[1,2]},{'keep':3},{'keep':4},{'keep':5},{'keep':6},{'keep':7},
          {'keep':8},{'keep':9},{'keep':10},{'join':[11,12]},{'join':[13,14]},{'keep':15}]
ko_ops = copy.deepcopy(en_ops); ko_ops[9] = {'new': ch14_ko10}
# KO 바빌론 표기 통일 (원본 '바벨론' 3건)
ko_ops[1] = {'join': [{'new': ch14_ko1}, 2]}
ko_ops[3] = {'new': ch14_ko3}
ko_ops[4] = {'new': ch14_ko4}
new_specs[14] = set_live(14, s, en_ops, ko_ops,
    merges=[
        merge_entry('Isaiah 14:3-6', '3-6', "MSG '3-6'은 단일 섹션 (바벨론 왕 조롱 노래 시작). 기존 '3-4'(서론)/'4-6'(노래) 분리는 MSG 1:1에 어긋나므로 병합."),
        merge_entry('Isaiah 14:24-27', '24-27', "MSG '24-27'은 단일 섹션. 기존 '24'/'25-27' 분리는 MSG 1:1에 어긋나므로 병합."),
        merge_entry('Isaiah 14:28-31', '28-31', "MSG '28-31'은 단일 섹션 (블레셋 경고). 기존 '28'/'29-31' 분리는 MSG 1:1에 어긋나므로 병합.")],
    confirmations=[conf(14, "기존 '3-4'/'4-6' → MSG '3-6' 병합"),
                   conf(14, "기존 '24'/'25-27' → MSG '24-27' 병합"),
                   conf(14, "기존 '28'/'29-31' → MSG '28-31' 병합")],
    ko_changes=["'바벨론' -> '바빌론' 표기 통일 4건 ('3-6'의 바벨론 왕, '11'의 바벨론, '12'의 바벨론아, '22-23'의 바벨론의 이름 — 파일 관용 16:3)"])

# ch18: '1'+'2'->'1-2', '4'+'5-6'->'4-6' 병합. KO 개많은 완화.
s = base_spec(18)
en_ops = [{'join':[0,1]}, {'keep':2}, {'join':[3,4]}, {'keep':5}]
ko_ops = [{'join':[{'new': ch18_ko0}, 1]}, {'keep':2}, {'join':[3,4]}, {'keep':5}]
new_specs[18] = set_live(18, s, en_ops, ko_ops,
    merges=[
        merge_entry('Isaiah 18:1-2', '1-2', "MSG '1-2'는 단일 섹션. 기존 '1'/'2' 분리는 MSG 1:1에 어긋나므로 병합."),
        merge_entry('Isaiah 18:4-6', '4-6', "MSG '4-6'은 단일 섹션. 기존 '4'/'5-6' 분리는 MSG 1:1에 어긋나므로 병합.")],
    confirmations=[conf(18, "기존 '1'/'2' → MSG '1-2' 병합"),
                   conf(18, "기존 '4'/'5-6' → MSG '4-6' 병합")],
    ko_changes=["'파리랑 모기가 개많은 땅' -> '파리랑 모기가 바글바글한 땅' (거친 표현 완화, MSG 'buzzing with bugs')"])

# ch20: '3-4'+'5-6' -> '3-6' 병합
s = base_spec(20)
new_specs[20] = set_live(20, s,
    [{'keep':0}, {'join':[1,2]}],
    [{'keep':0}, {'join':[1,2]}],
    merges=[merge_entry('Isaiah 20:3-6', '3-6',
        "MSG '3-6'은 단일 섹션 (이집트·에티오피아 수치 선언). 기존 '3-4'/'5-6' 분리는 MSG 1:1에 어긋나므로 병합.")],
    confirmations=[conf(20, "기존 '3-4'/'5-6' → MSG '3-6' 병합")],
    changes=["병합 후 인용부호가 자연스럽게 닫힘 (기존 [1] 끝의 닫는 따옴표 추가는 불필요해져 제외)"])

# ch23: '15'+'16' -> '15-16' 병합
s = base_spec(23)
new_specs[23] = set_live(23, s,
    keeps(5) + [{'join':[5,6]}, {'keep':7}],
    keeps(5) + [{'join':[5,6]}, {'keep':7}],
    merges=[merge_entry('Isaiah 23:15-16', '15-16',
        "MSG '15-16'은 단일 섹션 (두로 회복 후 창녀 노래). 기존 '15'/'16' 분리는 MSG 1:1에 어긋나므로 병합.")],
    confirmations=[conf(23, "기존 '15'/'16' → MSG '15-16' 병합")])

# ch33: 원본 11문단이 라이브 MSG와 일치. 닫는 따옴표 2건 복원.
s = base_spec(33)
en_ops = keeps(11); en_ops[4] = {'new': ch33_en4}
ko_ops = keeps(11); ko_ops[4] = {'new': ch33_ko4}
new_specs[33] = set_live(33, s, en_ops, ko_ops,
    changes=["원본 11문단이 라이브 MSG 섹션과 1:1 일치함을 확인 — old spec의 '14-16'/'20-21'+'22-23' 재절단 폐기",
             "EN/KO '10-12' 문단 끝 닫는 따옴표 복원 (인용부호 열고/닫음 정리)"],
    ko_changes=["KO '10-12' 문단 끝 닫는 따옴표 복원"])

# ch34: 원본 5문단이 라이브 MSG와 일치. KO v8 두 문장 이동.
s = base_spec(34)
new_specs[34] = set_live(34, s,
    keeps(5),
    [{'keep':0}, {'keep':1}, {'new': ch34_ko2}, {'new': ch34_ko3}, {'keep':4}],
    changes=["원본 5문단이 라이브 MSG 섹션과 1:1 일치함을 확인 — old spec의 '5-8'/'9-15' 재절단 폐기 (MSG '5-7'/'8-15')"],
    ko_changes=["v8 두 문장('야생 동물이든...'~'미끌미끌해질 거임.')을 '5-7' 문단 끝에서 '8-15' 문단 앞으로 이동 (MSG 절 경계)"])

# ---------- 파일에 쓰기 ----------
by_file = {}
for ch, f in spec_files.items():
    by_file.setdefault(f, {})[ch] = specs[ch]
for ch, spec in new_specs.items():
    by_file[spec_files[ch]][ch] = spec

for f, chmap in by_file.items():
    out = [chmap[ch] for ch in sorted(chmap)]
    json.dump(out, open(f, 'w'), ensure_ascii=False, indent=1)
    print(f'wrote {f} ({len(out)} chapters)')

print('rewrote chapters:', sorted(new_specs))
