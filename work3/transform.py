#!/usr/bin/env python3
"""MSG 구조 기준 EN 장 자동 재구성 (staging 출력).
수동 override: work3/specs_{book}.py 의 NULL_BADGES/REWRITES/DROPS/INSERTS/BADGE_FIX
"""
import json, re, sys, os, importlib

REVIEW = '/home/hatch/workspace/teenz-bible-review/'

def expand(vr):
    out = set()
    if vr is None: return out
    for part in str(vr).split(','):
        part = part.strip()
        if not part: continue
        if '-' in part:
            a, b = part.split('-'); out.update(range(int(a), int(b) + 1))
        elif part.isdigit(): out.add(int(part))
    return out

def rng(s):
    s = sorted(s)
    return f'{s[0]}-{s[-1]}' if len(s) > 1 else f'{s[0]}'

def load_specs(book):
    import importlib.util
    path = f'{REVIEW}work3/specs_{book}.py'
    try:
        spec = importlib.util.spec_from_file_location(f'specs_{book}', path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except FileNotFoundError:
        return None


def declare_msg_overlaps(new_paras, new_vrs, splits):
    """MSG 원문 자체가 한 절을 여러 문단에 걸쳐 쓰는 경우(overlapping badges),
    EN이 MSG 구분을 그대로 따르면 validator 중복 규칙에 걸리므로 splits로 선언"""
    declared = set()
    for sp in splits:
        declared.update(expand(sp['msg_range']))
    seen = {}
    for idx, (t, b) in enumerate(zip(new_paras, new_vrs)):
        if t.lstrip().startswith('§'): continue
        for v in expand(b):
            seen.setdefault(v, []).append(idx + 1)
    for v in sorted(seen):
        if len(seen[v]) > 1 and v not in declared:
            splits.append({'msg_range': str(v), 'paras': seen[v],
                           'note': f'MSG 원문이 {v}절을 여러 문단에 걸쳐 사용 — EN도 MSG 문단 구분 그대로 따름'})
    return splits

def transform(book, ch):
    msg = {c['chapter']: c for c in json.load(open(f'{REVIEW}msg_parsed_{book}.json'))}[ch]
    # specs의 인덱스는 원본(pre-audit) 기준이므로 항상 원본에서 읽음
    src = f'{REVIEW}fixes/en_{book}.json.pre_audit_bak'
    if not os.path.exists(src):
        src = f'{REVIEW}fixes/en_{book}.json'
    en_all = json.load(open(src))
    en = [c for c in en_all if c['chapter'] == ch][0]
    specs = load_specs(book)
    NULL = getattr(specs, 'NULL_BADGES', {}) if specs else {}
    REWR = getattr(specs, 'REWRITES', {}) if specs else {}
    DROPS = getattr(specs, 'DROPS', {}) if specs else {}
    INSS = getattr(specs, 'INSERTS', {}) if specs else {}
    BFIX = getattr(specs, 'BADGE_FIX', {}) if specs else {}
    FULL = getattr(specs, 'FULL_CHAPTERS', {}) if specs else {}

    paras, vrs = en['paragraphs'], en['verseRanges']

    if ch in FULL:
        # 완전 재구성: (text, badge) 목록 그대로 사용
        msg_badges_all = [p['badge'] for p in msg['paras']]
        f = FULL[ch]
        new_paras = [t for t, b in f['paras']]
        new_vrs = [b for t, b in f['paras']]
        # merge/split 판정
        merges, splits, confs = [], [], []
        for idx, (t, b) in enumerate(f['paras']):
            if t.lstrip().startswith('§'): continue
            S = expand(b)
            overlapped = [mb for mb in msg_badges_all if expand(mb) & S]
            if len(overlapped) > 1 and not any(S <= expand(mb) for mb in overlapped):
                merges.append({'para': idx + 1, 'msg_ranges': overlapped,
                               'note': f'MSG {overlapped} 문단을 하나의 EN 문단으로 합침'})
                confs.append(f'{ch}장 {idx+1}번 문단: MSG {overlapped} {len(overlapped)}개 문단을 하나의 EN 문단(배지 \'{b}\')으로 합침 — 컨펌 필요')
        # splits: MSG 단일 문단의 절 집합이 2개 이상 EN 문단에 나뉘어 담긴 경우
        # (각 EN 문단의 절이 해당 MSG 문단에 완전히 포함될 때만)
        for mb in msg_badges_all:
            M = expand(mb)
            plist = [idx + 1 for idx, (t, b) in enumerate(f['paras'])
                     if not t.lstrip().startswith('§') and expand(b) and expand(b) <= M]
            if len(plist) > 1:
                splits.append({'msg_range': mb, 'paras': plist,
                               'note': f'MSG 단일 문단({mb})을 EN 가독성을 위해 {len(plist)}개 문단으로 분리'})
        splits = declare_msg_overlaps(new_paras, new_vrs, splits)
        new_ch = {
            'chapter': ch,
            'title': en.get('title', ''),
            'paragraphs': new_paras,
            'verseRanges': new_vrs,
            'msg_ranges': list(new_vrs),
            'merges': merges,
            'splits': splits,
            'changes': ([f'{book} {ch}장: MSG 문단 구조 기준으로 EN 전면 재구성']
                        + (getattr(specs, 'CHANGES_EXTRA', {}) if specs else {}).get(ch, [])),
            'confirmations_needed': confs,
            'review_status': 'msg_audited',
        }
        return new_ch, [f'FULL 재구성: {len(new_paras)} 문단']
    drops = set(DROPS.get(ch, []))
    # 1. 기존 § 헤더 제거, null 배지 처리, drops 제외 → 작업 문단 목록
    work = []  # (old_idx, badge, text)
    log = []
    for i, (b, p) in enumerate(zip(vrs, paras)):
        if i in drops:
            log.append(f'drop EN para{i}'); continue
        if p.lstrip().startswith('§'):
            log.append(f'drop old header EN para{i}: {p[:40]}'); continue
        if b is None:
            nb = NULL.get((ch, i))
            if not nb:
                log.append(f'!! null badge EN para{i} 미지정: {p[:60]}'); nb = '?'
            else:
                log.append(f'null badge EN para{i} -> {nb}')
            b = nb
        if (ch, i) in REWR:
            p = REWR[(ch, i)]; log.append(f'rewrite EN para{i}')
        if (ch, i) in BFIX:
            log.append(f'badge fix EN para{i}: {b} -> {BFIX[(ch,i)]}'); b = BFIX[(ch, i)]
        work.append([i, b, p])
    # inserts 적용 (after_old_idx 기준, work 순서에 삽입)
    for (after, nb, text) in sorted(INSS.get(ch, [])):
        pos = next((k for k, w in enumerate(work) if w[0] > after), len(work))
        work.insert(pos, [f'ins@{after}', nb, text]); log.append(f'insert after EN para{after} [{nb}]')

    # 2. 새 배지 계산 + merge/split 판정
    msg_badges = [p['badge'] for p in msg['paras']]
    new_paras, new_vrs = [], []
    merges, splits, confs = [], [], []
    split_map = {}  # msg_range -> [new para indices]
    for wpos, (oi, b, p) in enumerate(work):
        S = expand(b)
        if not S:
            log.append(f'!! empty verse set EN para{oi}'); new_paras.append(p); new_vrs.append(b); continue
        nb = rng(S)
        overlapped = [mb for mb in msg_badges if expand(mb) & S]
        # 경계 절 공유(MSG 문단끼리 절이 겹침)는 merge가 아님: EN 절 집합이 단일 MSG 문단에 완전히 포함되면 merge 아님
        if len(overlapped) > 1 and not any(S <= expand(mb) for mb in overlapped):
            merges.append({'para': None, 'msg_ranges': overlapped,
                           'note': f'MSG {overlapped} 문단을 하나의 EN 문단으로 합침'})
            confs.append(f'{ch}장 {len(new_paras)+1}번 문단: MSG {overlapped} {len(overlapped)}개 문단을 하나의 EN 문단(배지 \'{nb}\')으로 합침 — 컨펌 필요')
            log.append(f'merge EN para{oi} [{b}] -> [{nb}] MSG{overlapped}')
        elif len(overlapped) == 1 and S != expand(overlapped[0]):
            split_map.setdefault(overlapped[0], []).append(len(new_paras))
            log.append(f'split EN para{oi} [{b}] -> [{nb}] (MSG {overlapped[0]}의 일부)')
        new_paras.append(p); new_vrs.append(nb)
    for mr, plist in split_map.items():
        splits.append({'msg_range': mr, 'paras': [x + 1 for x in plist],
                       'note': f'MSG 단일 문단({mr})을 EN 가독성을 위해 {len(plist)}개 문단으로 분리'})

    # 3. § 헤더 삽입 (MSG 섹션 기준)
    # 섹션 첫 MSG 문단의 첫 절을 포함하는 EN 문단 앞에 삽입
    inserts = []  # (new_pos, title)
    seen_headers = set()
    for mp in msg['paras']:
        if not mp['header'] or mp['header'] in seen_headers: continue
        seen_headers.add(mp['header'])
        first_v = min(expand(mp['badge']))
        tgt = next((k for k, b in enumerate(new_vrs) if first_v in expand(b)), None)
        if tgt is None:
            log.append(f'!! header target 없음: {mp["header"]} (MSG {mp["badge"]})'); continue
        inserts.append((tgt, mp['header']))
        log.append(f'header §{mp["header"]} -> EN 새 문단{tgt+1} 앞')
    for pos, title in sorted(inserts, reverse=True):
        new_paras.insert(pos, '§' + title)
        new_vrs.insert(pos, new_vrs[pos])
    # merge/split para 번호 보정 (§ 삽입으로 밀림) — merges는 para None이므로 나중에 채움
    # splits para 번호: 삽입 위치 이전 것만 영향. 단순화를 위해 splits는 § 삽입 전 인덱스+1 기준 유지 → 재계산
    # → splits를 § 삽입 후에 다시 매핑: split_map의 new index에 삽입 offset 적용
    offset = [0] * (len(new_vrs))
    # (생략: 아래에서 최종 인덱스로 재기록)
    final_splits = []
    ins_sorted = sorted(p for p, _ in inserts)
    for s in splits:
        new_plist = []
        for pn in s['paras']:  # 1-based, §삽입 전 기준
            idx0 = pn - 1
            shift = sum(1 for ip in ins_sorted if ip <= idx0)
            new_plist.append(pn + shift)
        s['paras'] = new_plist
        final_splits.append(s)
    final_merges = []
    # merges para 번호 채우기: work index 중 merge된 것들을 순서대로
    merge_work_idx = []
    for k, (oi, b, p) in enumerate(work):
        if b == '?' or not expand(b): continue
        S = expand(b)
        overlapped = [mb for mb in msg_badges if expand(mb) & S]
        if len(overlapped) > 1:
            merge_work_idx.append(k)
    for mrec, k in zip(merges, merge_work_idx):
        shift = sum(1 for ip in ins_sorted if ip <= k)
        mrec['para'] = k + 1 + shift
        final_merges.append(mrec)
    # confirmations 문단 번호도 보정
    final_confs = []
    for mrec, c in zip(final_merges, confs):
        final_confs.append(f'{ch}장 {mrec["para"]}번 문단: ' + c.split('번 문단: ', 1)[1] if '번 문단: ' in c else c)

    final_splits = declare_msg_overlaps(new_paras, new_vrs, final_splits)
    new_ch = {
        'chapter': ch,
        'title': en.get('title', ''),
        'paragraphs': new_paras,
        'verseRanges': new_vrs,
        'msg_ranges': list(new_vrs),
        'merges': final_merges,
        'splits': final_splits,
        'changes': ([f'{book} {ch}장: MSG 문단 구조 기준으로 배지 재구성 및 § 헤더 추가']
                    + (getattr(specs, 'CHANGES_EXTRA', {}) if specs else {}).get(ch, [])),
        'confirmations_needed': final_confs,
        'review_status': 'msg_audited',
    }
    return new_ch, log

if __name__ == '__main__':
    book = sys.argv[1]
    chs = [int(x) for x in sys.argv[2:]]
    os.makedirs(f'{REVIEW}staging', exist_ok=True)
    for ch in chs:
        new_ch, log = transform(book, ch)
        json.dump(new_ch, open(f'{REVIEW}staging/en_{book}_ch{ch}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print(f'===== {book} ch{ch}: {len(new_ch["paragraphs"])} paras =====')
        for l in log: print(' ', l)
