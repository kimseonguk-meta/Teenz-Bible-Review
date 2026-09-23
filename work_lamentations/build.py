#!/usr/bin/env python3
"""Lamentations MSG 재감사 스펙 -> fixes/en_Lamentations.json, fixes/ko_Lamentations.json 빌드."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
en_src = {c['num']: c for c in json.load(open(os.path.join(BASE, 'en_lamentations.json')))}
ko_src = {c['num']: c for c in json.load(open(os.path.join(BASE, 'ko_lamentations.json')))}

# 라이브 MSG 섹션 (2026-09-22 BibleGateway 대조)
LIVE = {
    1: [str(i) for i in range(1, 23)],
    2: [str(i) for i in range(1, 23)],
    3: ['1-3','4-6','7-9','10-12','13-15','16-18','19-21','22-24','25-27','28-30',
        '31-33','34-36','37-39','40-42','43-45','46-48','49-51','52-54','55-57',
        '58-60','61-63','64-66'],
    4: [str(i) for i in range(1, 23)],
    5: ['1-22'],
}

E = lambda ch, i: en_src[ch]['paragraphs'][i]
K = lambda ch, i: ko_src[ch]['paragraphs'][i]

def keeps(n):
    return [{'keep': i} for i in range(n)]

def merge_entry(scope, rng, reason):
    return {'scope': scope, 'msg_ranges': [rng], 'reason': reason}

def conf(ch, text):
    return f'ch{ch}: {text} (MSG 문단 합병)'

specs = []

# ch1, ch2: 원본 22문단이 라이브 MSG와 1:1 일치
for ch in (1, 2):
    specs.append({
        'chapter': ch, 'title': en_src[ch]['title'], 'ko_title': ko_src[ch]['title'],
        'badges': LIVE[ch], 'msg': LIVE[ch],
        'en_ops': keeps(22), 'ko_ops': keeps(22),
        'merges': [], 'splits': [], 'confirmations_needed': [],
        'changes': ['원본 22문단이 라이브 MSG 섹션과 1:1 일치함을 확인'],
        'ko_changes': [],
    })

# ch3: 원본 22문단(3절씩)이 라이브 MSG와 1:1 일치
specs.append({
    'chapter': 3, 'title': en_src[3]['title'], 'ko_title': ko_src[3]['title'],
    'badges': LIVE[3], 'msg': LIVE[3],
    'en_ops': keeps(22), 'ko_ops': keeps(22),
    'merges': [], 'splits': [], 'confirmations_needed': [],
    'changes': ['원본 22문단(3절씩 묶음)이 라이브 MSG 섹션과 1:1 일치함을 확인'],
    'ko_changes': [],
})

# ch4: 원본 20문단 -> MSG 22문단 (분할 2건 + 배지 정정 3건)
# EN 분할 텍스트 (원본 문장 경계 기준)
en_7 = "The leaders, who were once so healthy and looked so good, all strong and glowing."
en_8 = "But now they're covered in soot. You wouldn't even recognize them on the street. They're just skin and bones, their skin all dry and leathery."
assert E(4,6).startswith("The leaders, who were once so healthy") and "covered in soot" in E(4,6)
en_14 = "Now those same prophets and priests are just stumbling around the streets, all grimy and stained from their own corruption."
en_15 = "People yell at them, like, 'Get out of here, you're disgusting! Don't touch us!' They're total outcasts, and everyone knows they got kicked out of their own city."
assert E(4,12).startswith("Now those same prophets and priests") and "Get out of here" in E(4,12)
# KO 분할 텍스트
ko_7 = "원래는 왕족들이 진짜 뽀얗고 건강미 넘쳤거든? 몸도 탄탄하고, 완전 잘생겼었는데."
ko_8 = "지금은 시커먼 재를 뒤집어써서 길에서 아무도 못 알아본대. 뼈만 앙상하게 남고, 피부는 가죽처럼 바싹 말라버린 거임."
assert K(4,6).startswith("원래는 왕족들이") and "시커먼 재" in K(4,6)
ko_14 = "그 예언자들이랑 제사장들은 이제 눈먼 사람처럼 길거리를 헤매고 다니는데, 온몸이 더러운 죄로 얼룩져 있대."
ko_15 = "사람들이 '저리 가, 이 더러운 자들아! 만지지도 마!'라고 소리치고. 결국 쫓겨나서 떠돌이가 됐는데, 어딜 가도 다들 걔네가 자기 고향에서 쫓겨난 거 아는 거임."
assert K(4,12).startswith("그 예언자들이랑 제사장들은") and "저리 가" in K(4,12)

en_ops_4 = ([{'keep': i} for i in range(6)] + [{'new': en_7}, {'new': en_8}] +
            [{'keep': i} for i in range(7, 12)] + [{'new': en_14}, {'new': en_15}] +
            [{'keep': i} for i in range(13, 18)] + [{'keep': 18}, {'keep': 19}])
ko_ops_4 = ([{'keep': i} for i in range(6)] + [{'new': ko_7}, {'new': ko_8}] +
            [{'keep': i} for i in range(7, 11)] + [{'keep': 11}] +
            [{'new': ko_14}, {'new': ko_15}] +
            [{'keep': i} for i in range(13, 18)] + [{'keep': 18}, {'keep': 19}])
specs.append({
    'chapter': 4, 'title': en_src[4]['title'], 'ko_title': ko_src[4]['title'],
    'badges': LIVE[4], 'msg': LIVE[4],
    'en_ops': en_ops_4, 'ko_ops': ko_ops_4,
    'merges': [], 'splits': [], 'confirmations_needed': [],
    'changes': [
        "EN '7-8' 병합 문단을 v7/v8로 분할 (MSG는 개별 섹션)",
        "EN '14-15' 병합 문단을 v14/v15로 분할 (MSG는 개별 섹션)",
        "EN '20' 배지 2건 정정: [18]->'21' (에돔 연회, v21 내용), [19]->'22' (시온 회복, v22 내용)",
    ],
    'ko_changes': [
        "KO '7' 배지 문단(v7+v8 내용)을 v7/v8로 분할",
        "KO '12-13' 배지 정정 -> '13' (v13 내용만 있음, v12는 [10]에)",
        "KO '14-15' 병합 문단을 v14/v15로 분할",
        "KO '21-22' 배지 정정 -> '22' (v22 내용만 있음)",
    ],
})

# ch5: 원본 8문단 -> MSG 단일 '1-22' 섹션 병합
specs.append({
    'chapter': 5, 'title': en_src[5]['title'], 'ko_title': ko_src[5]['title'],
    'badges': LIVE[5], 'msg': LIVE[5],
    'en_ops': [{'join': list(range(8))}],
    'ko_ops': [{'join': list(range(8))}],
    'merges': [merge_entry('Lamentations 5:1-22', '1-22',
        "MSG '1-22'는 단일 섹션 (통회 기도 전체). 기존 8문단 분할('1-3'/'4-6'/...)은 MSG 1:1에 어긋나므로 병합.")],
    'splits': [],
    'confirmations_needed': [conf(5, "기존 '1-3'/'4-6'/'7-8'/'9-10'/'11-13'/'14-15'/'16-18'/'19-22' → MSG '1-22' 병합")],
    'changes': ["라이브 MSG ch5는 단일 '1-22' 섹션 — 8문단 병합"],
    'ko_changes': [],
})


def apply_ops(ops, src_paras, ch, lang):
    out = []
    for op in ops:
        if 'new' in op:
            out.append(op['new'])
        elif 'keep' in op:
            out.append(src_paras[op['keep']])
        elif 'join' in op:
            parts = []
            for i in op['join']:
                parts.append(i['new'] if isinstance(i, dict) and 'new' in i else src_paras[i])
            out.append(' '.join(parts))
        else:
            raise ValueError(f'ch{ch} {lang}: unknown op {op}')
    return out


en_out, ko_out = [], []
for spec in specs:
    ch = spec['chapter']
    en_paras = apply_ops(spec['en_ops'], en_src[ch]['paragraphs'], ch, 'EN')
    ko_paras = apply_ops(spec['ko_ops'], ko_src[ch]['paragraphs'], ch, 'KO')
    badges = spec['badges']
    assert len(en_paras) == len(badges), f'ch{ch} EN {len(en_paras)} != {len(badges)}'
    assert len(ko_paras) == len(badges), f'ch{ch} KO {len(ko_paras)} != {len(badges)}'
    en_out.append({'chapter': ch, 'title': spec['title'], 'paragraphs': en_paras,
                   'verseRanges': badges, 'msg_ranges': spec['msg'],
                   'merges': spec['merges'], 'splits': spec['splits'],
                   'changes': spec['changes'], 'confirmations_needed': spec['confirmations_needed']})
    ko_out.append({'chapter': ch, 'title': spec['ko_title'], 'paragraphs': ko_paras,
                   'verseRanges': badges, 'msg_ranges': spec['msg'],
                   'merges': spec['merges'], 'splits': spec['splits'],
                   'changes': spec['ko_changes'], 'confirmations_needed': spec['confirmations_needed']})

json.dump(en_out, open(os.path.join(BASE, '..', 'fixes', 'en_Lamentations.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(ko_out, open(os.path.join(BASE, '..', 'fixes', 'ko_Lamentations.json'), 'w'), ensure_ascii=False, indent=1)
print(f'built {len(en_out)} chapters -> fixes/en_Lamentations.json, fixes/ko_Lamentations.json')
