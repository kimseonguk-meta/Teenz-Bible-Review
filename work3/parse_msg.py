#!/usr/bin/env python3
"""MSG 캐시(txt)를 장별 문단 구조로 파싱.
출력: [{chapter, sections:[{title}], paras:[{badge, header, text}]}]
- '### Title' -> section header (다음 문단에 §로 공유)
- 문단 시작 'N-M ...' 또는 'N ...' -> badge; 'C N-M ...' (C=장번호) -> 장 전환
- 배지 없는 문단(시·대화 이어짐·'* * *') -> 직전 문단에 병합(시/대화), '* * *'은 분리 마커로만 기록
"""
import json, re, sys

def parse(path):
    raw = open(path, encoding='utf-8').read()
    lines = raw.split('\n')
    chapters = {}  # chno -> list of paras
    cur_ch = 1
    cur_header = None
    cur_para = None  # [badge, header, [text parts]]
    seps = []

    def flush():
        nonlocal cur_para
        if cur_para is not None:
            badge, header, parts = cur_para
            text = ' '.join(p.strip() for p in parts if p.strip())
            # 배지 없는 이어짐 문단(시·대화)은 직전 문단에 병합
            if badge is None and chapters.get(cur_ch):
                chapters[cur_ch][-1]['text'] += ' ' + text
            else:
                chapters.setdefault(cur_ch, []).append({'badge': badge, 'header': header, 'text': text})
            cur_para = None

    ch_re = re.compile(r'^(\d+)\s+(\d+(?:-\d+)?)\s+(.*)$')
    badge_re = re.compile(r'^(\d+(?:-\d+)?)\s+(.*)$')
    # bare-number 장 마커 (예외 2건 — 그 외 ^N [A-Z] 형태는 모두 절 배지)
    bare_ch_markers = {
        ('Luke', '11 One day he was praying in a certain place.'): (11, '1'),
        ('John', '18 Jesus, having prayed this prayer, left with his disciples and crossed over the brook Kidron'): (18, '1'),
    }
    book = path.split('msg_')[-1].split('.txt')[0]

    for line in lines:
        s = line.strip()
        if not s:
            flush(); continue
        if s.startswith('# Luke') or s.startswith('# '):
            flush(); continue
        if s == '* * *':
            flush(); seps.append(cur_ch); continue
        if s.startswith('### '):
            flush(); cur_header = s[4:].strip(); continue
        hit = None
        for k, v in bare_ch_markers.items():
            if k[0] == book and s.startswith(k[1]):
                hit = v; break
        if hit:
            flush(); cur_ch, badge = hit
            # § 헤더 유지: 장 마커 앞에 나온 ### 섹션은 새 장의 첫 문단에 속함
            cur_para = [badge, cur_header, [s]]
            continue
        m = ch_re.match(s)
        if m and int(m.group(1)) == cur_ch and not chapters.get(cur_ch) and cur_para is None:
            # 파일 시작 '1 1-4 ...' 형태 — 첫 문단 배지는 group2 (§ 헤더 유지)
            cur_para = [m.group(2), cur_header, [m.group(3)]]
            continue
        if m and int(m.group(1)) == cur_ch + 1 and int(m.group(2).split('-')[0]) <= 5:
            # 장 전환 (예: '2 1-5') — 다음 장 번호와 일치할 때만 (§ 헤더 유지)
            flush(); cur_ch = int(m.group(1))
            cur_para = [m.group(2), cur_header, [m.group(3)]]
            continue
        m = badge_re.match(s)
        if m:
            flush(); cur_para = [m.group(1), cur_header, [m.group(2)]]
            continue
        # 배지 없는 이어짐 (시·대화) -> 직전 문단에 병합
        if cur_para is not None:
            cur_para[2].append(s)
        else:
            # 문단 시작 전 이어짐 (드묾) -> 새 문단, 배지는 이어서 채움
            flush()
            cur_para = [None, cur_header, [s]]

    flush()
    return chapters

if __name__ == '__main__':
    for book in sys.argv[1:]:
        chs = parse(f'/home/hatch/workspace/teenz-bible-review/msg_{book}.txt')
        out = [{'chapter': c, 'paras': chs[c]} for c in sorted(chs)]
        json.dump(out, open(f'/home/hatch/workspace/teenz-bible-review/msg_parsed_{book}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(book, 'chapters:', sorted(chs), 'total paras:', sum(len(chs[c]) for c in chs))
