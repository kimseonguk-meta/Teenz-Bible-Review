#!/usr/bin/env python3
"""Build fixes/ko_Job.json from existing KO + en_Job.json (EN primary)."""
import json

REVIEW = '/home/hatch/workspace/teenz-bible-review/'
en = {c['chapter']: c for c in json.load(open(REVIEW + 'fixes/en_Job.json', encoding='utf-8'))}
ko_src = json.load(open(REVIEW + 'msg_work/ko_Job.json', encoding='utf-8'))
ko_ch = {c['num']: c for c in ko_src}

KO_TITLES = {
    1: "욥의 인생, 최고에서 최악으로... 그래도 믿음은 지켰다",
    2: "욥의 궁극 테스트: 2라운드",
    3: "욥의 인생 한탄 대폭발",
    4: "친구의 조언이... 완전 잔인함",
    5: "나쁜 일은 왜 생기고 어떻게 대처할까",
    6: "욥의 반격: 내 고통은 바다 모래보다 무거워",
    7: "하나님, 제발 숨 좀 쉬게 해주세요",
    8: "하나님은 실수 안 하셔, 형",
    9: "하나님 파워 앞에서 나는 아무것도 아님",
    10: "하나님, 질문 몇 개만요...",
    11: "하나님의 지혜는 차원이 다름",
    12: "욥의 반박: 하나님의 파워는 장난 아님",
    13: "내 사건, 하나님께 직접 가져간다",
    14: "인생은 버그투성이, 그리고 끝",
    15: "'현명한' 친구에게 디스당하는 친구",
    16: "친구들은 최악, 하나님은 잠수 중",
    17: "나 끝났어. 희망도 죽었어",
    18: "친구의 조언이 알고 보니 디스전",
    19: "하나님한테 읽씹 당했어",
    20: "악한 자들은 왜 번영하지 못하는가",
    21: "욥이 하나님께: 나쁜 놈들은 왜 항상 이기나요?",
    22: "하나님은 네 완벽한 성적표에 관심 없으셔",
    23: "하나님, 어디 계세요?!",
    24: "나쁜 놈들은 왜 항상 이길까?",
    25: "하나님의 파워는 차원이 다름",
    26: "욥이 친구들에게: '와, 진짜 도움 많이 된다... 아님 말고'",
    27: "욥의 마이크 드롭: 인생 꼬여도 진실하게",
    28: "사실상 불가능한 궁극의 보물찾기",
    29: "내가 전설이었던 그 시절로",
    30: "내 인생은 지금 완전 폐허임",
    31: "나 진짜 솔직했어, 맹세해",
    32: "인턴의 폭발: 새로운 챌린저 등장",
    33: "하나님이 DM 보내셨는데 못 봄?",
    34: "엘리후의 팩트 폭격: 하나님은 실수 안 하셔",
    35: "하나님이 네가 착한지 관심 있으실까?",
    36: "하나님은 불리가 아님 (그리고 다른 팩트 폭탄들)",
    37: "하나님의 날씨 컨트롤은 차원이 다름",
    38: "하나님이 드디어 욥에게 반격하시다",
    39: "하나님의 야생 왕국은 레전드",
    40: "하나님의 마이크 드롭과 궁극의 괴수",
    41: "하나님이 바다 괴물의 GOAT로 플렉스하심",
    42: "욥의 전설 귀환과 하나님의 마이크 드롭",
}

out = []
for ch in range(1, 43):
    e = en[ch]
    kc = ko_ch[ch]
    paras = list(kc['paragraphs'])
    changes = []
    if ch == 42:
        # merge KO0 (intro) + KO1 (quote) to match EN's single 1-6 paragraph
        paras = [paras[0] + ' ' + paras[1]] + paras[2:]
        changes.append("Ch42: KO 문단 0+1 병합 — EN 문단 구조(1-6 단일 문단)에 맞춤")
    old_badges = list(kc.get('verseRanges') or [])
    new_badges = list(e['verseRanges'])
    if old_badges != new_badges:
        changes.append(f"Ch{ch}: 배지를 EN 확정 배지로 통일 "
                       f"({', '.join(old_badges)} -> {', '.join(new_badges)})")
    out.append({
        'chapter': ch,
        'title': KO_TITLES[ch],
        'paragraphs': paras,
        'verseRanges': new_badges,
        'msg_ranges': list(e['msg_ranges']),
        'merges': [],
        'splits': [dict(s) for s in e['splits']],
        'changes': changes,
        'confirmations_needed': [],
    })

json.dump(out, open(REVIEW + 'fixes/ko_Job.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('wrote fixes/ko_Job.json:', len(out), 'chapters')
