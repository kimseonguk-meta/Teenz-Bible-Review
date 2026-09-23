#!/usr/bin/env python3
"""Worker F (continuation coordinator wave): OT Google Docs 업로드.

Usage: python3 upload_ot_f.py Leviticus [Numbers ...]

- 신규 책: 폴더 1I7rLOsUgbr5Ewyq7-IEshCk20scIBtPn에
  '{한글이름} ({영어이름}): MSG + Teen EN + KO' 제목으로 Doc 생성
  (주의: 제목에 'Final'을 넣지 않는다 — 2026-09-23 코디네이터 지시)
- 기존 Doc이 있는 책(Jeremiah/Lamentations/Ezekiel/Daniel):
  기존 Doc ID에 내용만 업데이트 (제목 유지), 링크 불변
- API 테이블 수 == 장 수 검증 + export-back 검증
- 결과는 gdocs_build/upload_results_workerF.json에 upsert (공유 파일 동결 — 절대 쓰지 않음)
"""
import json
import subprocess
import sys
import time
import os

GDIR = '/home/hatch/workspace/teenz-bible-review/gdocs_build'
REVIEW = '/home/hatch/workspace/teenz-bible-review'
sys.path.insert(0, GDIR)
from reupload import run, verify_exported  # noqa: E402

FOLDER = '1I7rLOsUgbr5Ewyq7-IEshCk20scIBtPn'

# (key, 한글이름, 영어이름, 장수)
BOOKS_F = [
    ('Leviticus', '레위기', 'Leviticus', 27),
    ('Numbers', '민수기', 'Numbers', 36),
    ('Deuteronomy', '신명기', 'Deuteronomy', 34),
    ('Judges', '사사기', 'Judges', 21),
    ('1Samuel', '사무엘상', '1Samuel', 31),
    ('2Samuel', '사무엘하', '2Samuel', 24),
    ('1Kings', '열왕기상', '1Kings', 22),
    ('2Kings', '열왕기하', '2Kings', 25),
    ('1Chronicles', '역대기상', '1Chronicles', 29),
    ('2Chronicles', '역대기하', '2Chronicles', 36),
    ('Ezra', '에스라', 'Ezra', 10),
    ('Nehemiah', '느헤미야', 'Nehemiah', 13),
    ('Psalms', '시편', 'Psalms', 150),
    ('Proverbs', '잠언', 'Proverbs', 31),
    ('Ecclesiastes', '전도서', 'Ecclesiastes', 12),
    ('Isaiah', '이사야', 'Isaiah', 66),
    ('Jeremiah', '예레미야', 'Jeremiah', 52),
    ('Lamentations', '예레미야애가', 'Lamentations', 5),
    ('Ezekiel', '에스겔', 'Ezekiel', 48),
    ('Daniel', '다니엘', 'Daniel', 12),
]
BOOK_MAP = {k: (ko, en, n) for k, ko, en, n in BOOKS_F}

# 기존 Doc ID (worker E2 등록분) — 이 책들은 업데이트만
EXISTING_IDS = {
    'Jeremiah': '1_9YRCZ8ECbgNbHbAz2F',
    'Lamentations': '1XPly-2mqmpBcIZjqb40',
    'Ezekiel': '1KlzFNz99jYhYusNHSzl',
    'Daniel': '1i7uLZ_e2hfRYobUrQne',
}

RES_PATH = os.path.join(GDIR, 'upload_results_workerF.json')


def verify_doc(key, doc_id, exp_tables, title_must=None):
    """API 테이블 수 + export-back 검증. (problems 리스트 반환)"""
    problems = []
    time.sleep(3)
    g = run(['hatch_gws_cli', 'docs', 'documents', 'get',
             '--params', json.dumps({'documentId': doc_id,
                                     'fields': 'title,body(content(table))'})])
    n_tables = sum(1 for x in g.get('body', {}).get('content', []) if 'table' in x)
    if n_tables != exp_tables:
        problems.append(f'table count {n_tables} != expected {exp_tables}')
    if title_must is not None and g.get('title') != title_must:
        problems.append(f'title mismatch: {g.get("title")!r}')
    exp_path = f'/tmp/gverify_{key}.docx'
    r = subprocess.run(
        ['hatch_gws_cli', 'drive', 'files', 'export',
         '--params', json.dumps({'fileId': doc_id,
                                 'mimeType': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'}),
         '--output', exp_path],
        capture_output=True, text=True, timeout=300)
    if r.returncode != 0:
        problems.append('export failed: ' + r.stderr[:200])
    else:
        problems.extend(verify_exported(key, exp_path))
    return problems, n_tables


def main():
    keys = sys.argv[1:]
    assert keys and all(k in BOOK_MAP for k in keys), \
        'usage: upload_ot_f.py <Key...>  keys: ' + ','.join(BOOK_MAP)
    results = json.load(open(RES_PATH, encoding='utf-8')) if os.path.exists(RES_PATH) else []
    id_by_key = {r['key']: r for r in results}
    summary = []
    for key in keys:
        ko, en, exp_tables = BOOK_MAP[key]
        docx = os.path.join(GDIR, f'{key}.docx')
        assert os.path.exists(docx) and os.path.getsize(docx) > 0, f'missing {docx}'
        try:
            if key in EXISTING_IDS:
                doc_id = EXISTING_IDS[key]
                print(f'[{key}] updating existing doc {doc_id} ...', flush=True)
                run(['hatch_gws_cli', 'drive', 'files', 'update',
                     '--params', json.dumps({'fileId': doc_id}), '--upload', docx])
                problems, n_tables = verify_doc(key, doc_id, exp_tables)
                title = None
                link = None
            else:
                title = f'{ko} ({en}): MSG + Teen EN + KO'
                assert 'Final' not in title
                print(f'[{key}] creating doc "{title}" ...', flush=True)
                c = run(['hatch_gws_cli', 'drive', 'files', 'create',
                         '--params', '{"ignoreDefaultVisibility":true}',
                         '--json', json.dumps({'name': title,
                                               'mimeType': 'application/vnd.google-apps.document',
                                               'parents': [FOLDER]})])
                doc_id = c['id']
                time.sleep(1)
                run(['hatch_gws_cli', 'drive', 'files', 'update',
                     '--params', json.dumps({'fileId': doc_id}), '--upload', docx])
                problems, n_tables = verify_doc(key, doc_id, exp_tables, title_must=title)
                f = run(['hatch_gws_cli', 'drive', 'files', 'get',
                         '--params', json.dumps({'fileId': doc_id,
                                                 'fields': 'id,name,webViewLink,parents'})])
                link = f.get('webViewLink')
            ok = not problems
            entry = {'key': key, 'title': title, 'id': doc_id,
                     'webViewLink': link,
                     'tables': n_tables, 'expected': exp_tables,
                     'status': 'OK' if ok else 'MISMATCH',
                     'export_problems': problems[:10],
                     'export_back': 'VERIFIED OK' if ok else 'ISSUES'}
            if key in id_by_key:
                results[results.index(id_by_key[key])] = entry
            else:
                results.append(entry)
            id_by_key[key] = entry
            print(f'[{key}] -> {entry["status"]}' + ('' if ok else f' {problems[:5]}'),
                  flush=True)
            summary.append((key, ok))
        except Exception as e:
            print(f'[{key}] FAILED: {str(e)[:300]}', flush=True)
            summary.append((key, False))
        time.sleep(1)
    json.dump(results, open(RES_PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    n_ok = sum(1 for _, ok in summary if ok)
    print(f'\nDONE: {n_ok}/{len(summary)} OK')
    if n_ok != len(summary):
        sys.exit(1)


if __name__ == '__main__':
    main()
