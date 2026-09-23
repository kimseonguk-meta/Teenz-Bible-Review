#!/usr/bin/env python3
"""Teenz Bible 번역 검증 게이트 — 5대 원칙 자동 검사.

사용법:
  python3 validate_translation.py fixes/en_matthew_01-14.json fixes/ko_matthew_01-14.json

검사 항목:
  1. 모든 문단에 null이 아닌 배지가 있는가 (원칙 2)
  2. 배지가 MSG 전 절을 커버하는가 — 커버 기준은 패치의 msg_ranges 합집합 (원칙 1)
  3. splits로 선언되지 않은 배지 중복이 없는가 (원칙 2)
  4. EN과 KO의 문단 수·배지가 일치하는가 (원칙 4)
  5. merges가 모두 confirmations_needed에 있는가 (원칙 2)
  6. review_status가 'carried_over'인 장은 감사 주장을 하지 않는가
     (msg_ranges/merges/splits 금지, 미감사 명시 note 필수)
     - 'carried_over' = MSG 재감사 범위 밖의 장을 앱 기존 데이터에서 verbatim으로 옮긴 것.
       내용 검증을 통과한 것이 아니므로 1-5번 검사를 적용하지 않는 대신,
       감사로 오인될 수 있는 어떤 주장도 금지한다.
     - review_status가 없는 구 형식 파일은 'msg_audited'로 간주 (하위 호환).
  7. EN/KO 본문에 욕설·비속어가 없는가 (원칙 5)
종료 코드 0 = 통과, 1 = 실패.
"""
import json, re, sys


# 원칙 5 — 욕설·비속어 목록.
# '보지'/'자지'는 제외: '보지 못한' 같은 정상 표현과 철자가 같아 자동 판별 불가 → 사람 검수에서 처리.
# substring 매칭: 조사 결합형('씨발이', '병신들')까지 검출. 목록 단어는 정상 문맥에서
# substring으로 등장할 일이 없어 오탐 위험이 없음 (회귀 테스트로 검증).
PROFANITY_KO = ['씨발', '시발', '좆', '좃', '병신', '개새끼', '지랄', '염병',
                '씹새끼', '미친새끼', '엿먹']
PROFANITY_EN = ['fuck', 'shit', 'bitch', 'cunt', 'asshole', 'dickhead']


def check_profanity(paras, label, ch, errors):
    for i, p in enumerate(paras):
        text = p if isinstance(p, str) else ''
        low = text.lower()
        for w in PROFANITY_KO:
            if w in text:
                errors.append(f"ch{ch}: {label} para{i}에 비속어 '{w}' (원칙 5)")
                break
        for w in PROFANITY_EN:
            if re.search(r'(?<![a-z])' + re.escape(w) + r'(?![a-z])', low):
                errors.append(f"ch{ch}: {label} para{i}에 비속어 '{w}' (원칙 5)")
                break


def expand(vr):
    out = set()
    for part in str(vr).split(','):
        part = part.strip()
        if not part:
            continue
        if '-' in part:
            a, b = part.split('-')
            out.update(range(int(a), int(b) + 1))
        elif part.isdigit():
            out.add(int(part))
    return out


def load(path):
    data = json.load(open(path))
    return {c['chapter']: c for c in (data if isinstance(data, list) else [data])}


def check_carried_over(en, ko, errors):
    """review_status='carried_over' 장: 감사 주장을 금지하고 정직성만 검사한다."""
    ch = en['chapter']
    # 6a. 감사 주장 금지 — MSG 커버리지·merge·split을 주장하면 안 됨
    if en.get('msg_ranges'):
        errors.append(f"ch{ch}: carried_over 장에 msg_ranges가 있으면 안 됨 (MSG 커버리지 주장 금지)")
    if en.get('merges'):
        errors.append(f"ch{ch}: carried_over 장에 merges가 있으면 안 됨 (감사 주장 금지)")
    if en.get('splits'):
        errors.append(f"ch{ch}: carried_over 장에 splits가 있으면 안 됨 (감사 주장 금지)")
    # 6b. 미감사 명시 note 필수 — 빠지면 감사 완료로 오인될 수 있음
    if not en.get('note'):
        errors.append(f"ch{ch}: carried_over 장에 note(MSG 미감사 명시)가 필요")
    # 6c. 기본 형태 (verbatim 전달이므로 내용 검사는 하지 않음)
    paras, vrs = en.get('paragraphs'), en.get('verseRanges')
    if not isinstance(paras, list) or not isinstance(vrs, list):
        errors.append(f"ch{ch}: carried_over 장의 paragraphs/verseRanges가 리스트가 아님")
    elif len(paras) != len(vrs):
        errors.append(f"ch{ch}: carried_over paragraphs({len(paras)}) != verseRanges({len(vrs)})")
    # 6d. KO도 carried_over로 함께 표기되어야 함
    if ko is None:
        errors.append(f"ch{ch}: KO 패치 없음")
        return
    if ko.get('review_status') != 'carried_over':
        errors.append(f"ch{ch}: EN은 carried_over인데 KO review_status가 '{ko.get('review_status')}'")
    kparas, kvrs = ko.get('paragraphs'), ko.get('verseRanges')
    if not isinstance(kparas, list) or not isinstance(kvrs, list):
        errors.append(f"ch{ch}: KO carried_over 장의 paragraphs/verseRanges가 리스트가 아님")
    elif len(kparas) != len(kvrs):
        errors.append(f"ch{ch}: KO carried_over paragraphs({len(kparas)}) != verseRanges({len(kvrs)})")
    if not ko.get('note'):
        errors.append(f"ch{ch}: KO carried_over 장에 note(MSG 미감사 명시)가 필요")
    # 7. carried_over라도 욕설·비속어는 검사 (원칙 5)
    check_profanity(paras if isinstance(paras, list) else [], 'EN', ch, errors)
    check_profanity(kparas if isinstance(kparas, list) else [], 'KO', ch, errors)


def check_chapter(en, ko, errors):
    ch = en['chapter']
    status = en.get('review_status', 'msg_audited')  # 구 형식 파일 하위 호환
    if status == 'carried_over':
        check_carried_over(en, ko, errors)
        return
    if status != 'msg_audited':
        errors.append(f"ch{ch}: 알 수 없는 review_status '{status}'")
        return
    paras, vrs = en['paragraphs'], en['verseRanges']
    declared_splits = set()
    for s in en.get('splits', []):
        declared_splits.update(expand(s['msg_range']))

    # 1. null 배지 금지
    if len(paras) != len(vrs):
        errors.append(f"ch{ch}: paragraphs({len(paras)}) != verseRanges({len(vrs)}) 길이 불일치")
    for i, b in enumerate(vrs):
        if not b:
            errors.append(f"ch{ch} EN para{i}: null/빈 배지")

    # 2. MSG 전 절 커버 (msg_ranges 합집합 기준)
    expected = set()
    for r in en.get('msg_ranges', []):
        expected.update(expand(r))
    covered = set()
    for b in vrs:
        covered.update(expand(b))
    missing = expected - covered
    if missing:
        errors.append(f"ch{ch}: MSG 절 누락 커버 {sorted(missing)}")

    # 3. 미선언 배지 중복 금지
    seen = {}  # verse -> (para_index, badge)
    for i, b in enumerate(vrs):
        for v in expand(b):
            if v in seen and v not in declared_splits:
                # § 헤더 공유는 허용: 둘 중 하나라도 헤더 문단이면 스킵
                pi, pb = seen[v]
                hdr = paras[i].lstrip().startswith('§') or paras[pi].lstrip().startswith('§')
                if not hdr:
                    errors.append(f"ch{ch}: {v}절이 para{pi}('{pb}')와 para{i}('{b}')에 중복 (splits 미선언)")
            else:
                seen[v] = (i, b)

    # 4. EN/KO 구조 일치
    if ko is None:
        errors.append(f"ch{ch}: KO 패치 없음")
        return
    kparas, kvrs = ko['paragraphs'], ko['verseRanges']
    if len(kparas) != len(paras):
        errors.append(f"ch{ch}: EN 문단 {len(paras)}개 vs KO 문단 {len(kparas)}개 불일치 (원칙 4)")
    if list(kvrs) != list(vrs):
        errors.append(f"ch{ch}: EN/KO 배지 불일치\n  EN: {vrs}\n  KO: {kvrs}")

    # 5. merges는 컨펌 목록에 (컨펌 문구는 자유형식이므로, merge의 각 절 범위가
    # 컨펌 텍스트 안에 전부 언급되어 있는지 토큰 단위로 확인)
    confirmed = ' '.join(ko.get('confirmations_needed', []) + en.get('confirmations_needed', []))
    conf_norm = re.sub(r'\s+', '', confirmed)
    for m in en.get('merges', []) + ko.get('merges', []):
        tokens = m.get('msg_ranges', [])
        missing_tok = [t for t in tokens
                       if not re.search(r'(?<![0-9])' + re.escape(t) + r'(?![0-9])', conf_norm)]
        if missing_tok:
            errors.append(f"ch{ch}: merge {','.join(tokens)}의 구간 {missing_tok}가 confirmations_needed에 언급되지 않음")

    # 7. 욕설·비속어 검사 (원칙 5)
    check_profanity(paras, 'EN', ch, errors)
    check_profanity(kparas, 'KO', ch, errors)


def main():
    en_patches, ko_patches = {}, {}
    for path in sys.argv[1:]:
        name = path.lower()
        target = en_patches if '/en_' in name or 'en_matthew' in name else ko_patches
        target.update(load(path))
    errors = []
    for ch in sorted(set(en_patches) | set(ko_patches)):
        en = en_patches.get(ch)
        if not en:
            errors.append(f"ch{ch}: EN 패치 없음")
            continue
        check_chapter(en, ko_patches.get(ch), errors)
    if errors:
        print(f"FAIL: {len(errors)}건")
        for e in errors:
            print(' -', e)
        sys.exit(1)
    print(f"PASS: {len(set(en_patches) | set(ko_patches))}개 장 모두 통과")


if __name__ == '__main__':
    main()
