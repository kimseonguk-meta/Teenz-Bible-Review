#!/usr/bin/env python3
"""Upload remaining 26 books: create Google Doc in folder, upload DOCX (convert in place), verify."""
import json, subprocess, sys, time, os

FOLDER = '1I7rLOsUgbr5Ewyq7-IEshCk20scIBtPn'
GDIR = '/home/hatch/workspace/teenz-bible-review/gdocs_build'
BOOKS = [
    ('Matthew', '마태복음', 'Matthew', 28),
    ('Mark', '마가복음', 'Mark', 16),
    ('Luke', '누가복음', 'Luke', 24),
    ('John', '요한복음', 'John', 21),
    ('Romans', '로마서', 'Romans', 16),
    ('1Corinthians', '고린도전서', '1 Corinthians', 16),
    ('2Corinthians', '고린도후서', '2 Corinthians', 13),
    ('Galatians', '갈라디아서', 'Galatians', 6),
    ('Ephesians', '에베소서', 'Ephesians', 6),
    ('Philippians', '빌립보서', 'Philippians', 4),
    ('Colossians', '골로새서', 'Colossians', 4),
    ('1Thessalonians', '데살로니가전서', '1 Thessalonians', 5),
    ('2Thessalonians', '데살로니가후서', '2 Thessalonians', 3),
    ('1Timothy', '디모데전서', '1 Timothy', 6),
    ('2Timothy', '디모데후서', '2 Timothy', 4),
    ('Titus', '디도서', 'Titus', 3),
    ('Philemon', '빌레몬서', 'Philemon', 1),
    ('Hebrews', '히브리서', 'Hebrews', 13),
    ('James', '야고보서', 'James', 5),
    ('1Peter', '베드로전서', '1 Peter', 5),
    ('2Peter', '베드로후서', '2 Peter', 3),
    ('1John', '요한일서', '1 John', 5),
    ('2John', '요한이서', '2 John', 1),
    ('3John', '요한삼서', '3 John', 1),
    ('Jude', '유다서', 'Jude', 1),
    ('Revelation', '요한계시록', 'Revelation', 22),
]

def run(args):
    r = subprocess.run(args, capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        raise RuntimeError(f'CMD FAILED: {" ".join(args[:6])}...\nSTDERR: {r.stderr[:500]}')
    return json.loads(r.stdout)

results = []
for key, ko, en, exp_tables in BOOKS:
    title = f'{ko} ({en}) — Final: MSG + Teen EN + KO'
    docx = os.path.join(GDIR, f'{key}.docx')
    assert os.path.exists(docx) and os.path.getsize(docx) > 0, f'missing {docx}'
    try:
        # 1. create doc in folder
        c = run(['hatch_gws_cli', 'drive', 'files', 'create',
                 '--params', '{"ignoreDefaultVisibility":true}',
                 '--json', json.dumps({'name': title,
                                       'mimeType': 'application/vnd.google-apps.document',
                                       'parents': [FOLDER]})])
        doc_id = c['id']
        time.sleep(1)
        # 2. upload docx -> converts in place
        run(['hatch_gws_cli', 'drive', 'files', 'update',
             '--params', json.dumps({'fileId': doc_id}), '--upload', docx])
        time.sleep(2)
        # 3. verify
        g = run(['hatch_gws_cli', 'docs', 'documents', 'get',
                 '--params', json.dumps({'documentId': doc_id,
                                         'fields': 'title,body(content(paragraph,table))'})])
        content = g.get('body', {}).get('content', [])
        n_tables = sum(1 for x in content if 'table' in x)
        ok = (g.get('title') == title and n_tables == exp_tables)
        # webViewLink
        f = run(['hatch_gws_cli', 'drive', 'files', 'get',
                 '--params', json.dumps({'fileId': doc_id,
                                         'fields': 'id,name,webViewLink,parents'})])
        results.append({'key': key, 'title': title, 'id': doc_id,
                        'webViewLink': f.get('webViewLink'),
                        'tables': n_tables, 'expected': exp_tables,
                        'status': 'OK' if ok else 'MISMATCH'})
        print(f'{key}: {n_tables}/{exp_tables} tables -> {"OK" if ok else "MISMATCH"}', flush=True)
    except Exception as e:
        results.append({'key': key, 'title': title, 'status': 'FAILED', 'error': str(e)[:300]})
        print(f'{key}: FAILED - {str(e)[:200]}', flush=True)
    time.sleep(1)

json.dump(results, open('/home/hatch/workspace/teenz-bible-review/gdocs_build/upload_results.json', 'w'),
          ensure_ascii=False, indent=1)
n_ok = sum(1 for r in results if r['status'] == 'OK')
print(f'\nDONE: {n_ok}/{len(BOOKS)} OK')
