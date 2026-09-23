#!/usr/bin/env python3
"""전 권 파일 빌드 — 감사 완료 장 + 나머지 장 verbatim 포장.

배경: fixes/en_Mark.json 등은 감사 대상 마지막 장(Mark 16, Luke 24, John 21)만
담고 있었으나, 작업실 규칙상 권 파일은 해당 권의 전 장을 포함해야 한다.
감사 범위 밖의 장은 앱 기존 데이터를 verbatim으로 옮기고
review_status='carried_over' + MSG 미감사 명시 note를 강제한다.
감사 완료로 오인될 수 있는 msg_ranges/merges/splits 주장은 validator가 금지한다.

입력:
  - 감사 완료 단일 장: fixes/en_Mark.json 등 (현재 파일; 재실행 시 전 권 파일에서
    review_status='msg_audited'인 장을 찾아 재사용하므로 idempotent)
  - EN 기존 데이터: teenz-fix/client/src/data/allBibleData.json (읽기만)
  - KO 기존 데이터: teenz-fix/client/src/data/gospelDataKo.ts (읽기만)
출력: fixes/en_Mark.json, fixes/ko_Mark.json, fixes/en_Luke.json,
      fixes/ko_Luke.json, fixes/en_John.json, fixes/ko_John.json (전 장)
주의: work3/build_fixes.py, build_luke.py, build_john.py를 재실행하면
      단일 장 파일로 덮어쓰므로, 그 뒤에는 이 스크립트를 다시 실행할 것.
"""
import json
import os
import shutil
import subprocess

REVIEW = '/home/hatch/workspace/teenz-bible-review/'
FIXES = REVIEW + 'fixes/'
WORK3 = REVIEW + 'work3/'
TEENZ_FIX_DATA = '/home/hatch/workspace/teenz-fix/client/src/data/'

BOOKS = {
    # book: (total_chapters, audited_chapter)
    'Mark': (16, 16),
    'Luke': (24, 24),
    'John': (21, 21),
}

EN_NOTE = ("MSG 미대조 장: 2026-09-22 MSG 재감사 범위는 {book} {aud}장이며, "
           "이 장({ch}장)은 범위에 포함되지 않아 MSG 대조를 거치지 않았다. "
           "앱 기존 데이터(teenz-fix/client/src/data/allBibleData.json)의 "
           "title·paragraphs·verseRanges를 그대로 옮긴 것으로, "
           "감사 완료로 취급하지 말 것.")

KO_NOTE = ("MSG 미대조 장: 2026-09-22 MSG 재감사 범위는 {book} {aud}장이며, "
           "이 장({ch}장)은 범위에 포함되지 않아 MSG 대조를 거치지 않았다. "
           "앱 기존 데이터(teenz-fix/client/src/data/gospelDataKo.ts)의 "
           "paragraphs·verseRanges를 그대로 옮긴 것으로, "
           "감사 완료로 취급하지 말 것.")


def parse_ko_ts():
    """gospelDataKo.ts에서 Mark/Luke/John KO 데이터를 JSON으로 추출."""
    out_path = WORK3 + 'ko_gospels_MLJ.json'
    node_code = (
        "const fs=require('fs');"
        "let src=fs.readFileSync(process.argv[1],'utf8');"
        "const m=src.match(/export const gospelDataKo[^=]*=\\s*(\\{[\\s\\S]*\\})\\s*;\\s*$/);"
        "if(!m){console.error('TS PARSE FAIL');process.exit(1);}"
        "const data=eval('('+m[1]+')');"
        "fs.writeFileSync(process.argv[2],JSON.stringify({Mark:data.Mark,Luke:data.Luke,John:data.John}));"
        "console.log('ko chapters:',data.Mark.length,data.Luke.length,data.John.length);"
    )
    r = subprocess.run(['node', '-e', node_code,
                        TEENZ_FIX_DATA + 'gospelDataKo.ts', out_path],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError('KO TS parse failed: ' + r.stderr)
    print(r.stdout.strip(), '->', out_path)
    return json.load(open(out_path, encoding='utf-8'))


def find_audited(path, aud_ch):
    """현재 파일에서 감사 완료 장 dict를 찾는다 (단일 장 또는 전 권 모두 대응)."""
    data = json.load(open(path, encoding='utf-8'))
    chs = data if isinstance(data, list) else [data]
    for c in chs:
        if c.get('review_status') == 'msg_audited':
            return dict(c)
    if len(chs) == 1:
        return dict(chs[0])
    for c in chs:
        if c.get('chapter') == aud_ch:
            d = dict(c)
            d.pop('review_status', None)  # carried_over였다면 감사본이 아님 → 아래에서 검증
            return d
    raise RuntimeError(f'{path}: 감사 완료 장(ch{aud_ch})을 찾지 못함')


def main():
    os.makedirs(WORK3 + 'backups', exist_ok=True)
    ko_data = parse_ko_ts()
    en_data = json.load(open(TEENZ_FIX_DATA + 'allBibleData.json', encoding='utf-8'))

    for book, (n_ch, aud_ch) in BOOKS.items():
        en_path = f'{FIXES}en_{book}.json'
        ko_path = f'{FIXES}ko_{book}.json'
        # 백업 (덮어쓰기 전)
        for p in (en_path, ko_path):
            bkp = f"{WORK3}backups/{os.path.basename(p)}.bak"
            shutil.copy2(p, bkp)

        aud_en = find_audited(en_path, aud_ch)
        aud_ko = find_audited(ko_path, aud_ch)
        assert aud_en['chapter'] == aud_ch, f"EN 감사 장 번호 불일치: {aud_en['chapter']}"
        assert aud_ko['chapter'] == aud_ch, f"KO 감사 장 번호 불일치: {aud_ko['chapter']}"
        if aud_en.get('review_status') == 'carried_over':
            raise RuntimeError(f'{book} ch{aud_ch}: carried_over를 감사본으로 사용하려 함 — 중단')
        aud_en['review_status'] = 'msg_audited'
        aud_ko['review_status'] = 'msg_audited'

        en_src = {c['num']: c for c in en_data[book]}
        ko_src = {c['num']: c for c in ko_data[book]}
        assert set(en_src) == set(range(1, n_ch + 1)), f'{book} EN 장 누락'
        assert set(ko_src) == set(range(1, n_ch + 1)), f'{book} KO 장 누락'

        en_out, ko_out = [], []
        for ch in range(1, n_ch + 1):
            if ch == aud_ch:
                en_out.append(aud_en)
                ko_out.append(aud_ko)
                continue
            ec, kc = en_src[ch], ko_src[ch]
            en_out.append({
                'chapter': ch,
                'title': ec.get('title'),
                'paragraphs': list(ec['paragraphs']),
                'verseRanges': list(ec['verseRanges']),
                'review_status': 'carried_over',
                'note': EN_NOTE.format(book=book, aud=aud_ch, ch=ch),
                'merges': [],
                'splits': [],
                'changes': [],
                'confirmations_needed': [],
            })
            ko_ch = {
                'chapter': ch,
                'paragraphs': list(kc['paragraphs']),
                'verseRanges': list(kc['verseRanges']),
                'review_status': 'carried_over',
                'note': KO_NOTE.format(book=book, aud=aud_ch, ch=ch),
                'merges': [],
                'splits': [],
                'changes': [],
                'confirmations_needed': [],
            }
            if kc.get('title'):
                ko_ch['title'] = kc['title']
            ko_out.append(ko_ch)

        json.dump(en_out, open(en_path, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        json.dump(ko_out, open(ko_path, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        print(f'{book}: {n_ch}장 기록 (감사 완료: ch{aud_ch}, carried_over: {n_ch - 1}장)')

    print('DONE')


if __name__ == '__main__':
    main()
