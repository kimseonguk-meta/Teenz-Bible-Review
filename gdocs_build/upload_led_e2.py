#!/usr/bin/env python3
"""Worker E2: Upload Lamentations, Ezekiel, Daniel DOCX to Google Docs.
Appends to upload_results_workerE2.json (NOT the frozen upload_results.json).
"""
import json, subprocess, time, os

FOLDER = '1I7rLOsUgbr5Ewyq7-IEshCk20scIBtPn'
GDIR = '/home/hatch/workspace/teenz-bible-review/gdocs_build'
OUT = os.path.join(GDIR, 'upload_results_workerE2.json')

BOOKS = [
    ('Lamentations', '예레미야애가', 'Lamentations', 1),
    ('Ezekiel', '에스겔', 'Ezekiel', 1),
    ('Daniel', '다니엘', 'Daniel', 1),
]

def run(args):
    r = subprocess.run(args, capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        raise RuntimeError(f'CMD FAILED: {" ".join(args[:6])}...\nSTDERR: {r.stderr[:500]}')
    return json.loads(r.stdout)

# Load existing E2 results
if os.path.exists(OUT):
    results = json.load(open(OUT, encoding='utf-8'))
else:
    results = []

for key, ko, en, exp_tables in BOOKS:
    title = f'{ko} ({en}) — MSG + Teen EN + KO'
    docx = os.path.join(GDIR, f'{key}.docx')
    assert os.path.exists(docx) and os.path.getsize(docx) > 0, f'missing {docx}'
    try:
        c = run(['hatch_gws_cli', 'drive', 'files', 'create',
                 '--params', '{"ignoreDefaultVisibility":true}',
                 '--json', json.dumps({'name': title,
                                       'mimeType': 'application/vnd.google-apps.document',
                                       'parents': [FOLDER]})])
        doc_id = c['id']
        time.sleep(1)
        run(['hatch_gws_cli', 'drive', 'files', 'update',
             '--params', json.dumps({'fileId': doc_id}), '--upload', docx])
        time.sleep(2)
        g = run(['hatch_gws_cli', 'docs', 'documents', 'get',
                 '--params', json.dumps({'documentId': doc_id,
                                         'fields': 'title,body(content(paragraph,table))'})])
        content = g.get('body', {}).get('content', [])
        n_tables = sum(1 for x in content if 'table' in x)
        ok = (g.get('title') == title and n_tables == exp_tables)
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

json.dump(results, open(OUT, 'w'), ensure_ascii=False, indent=1)
n_ok = sum(1 for r in results if r['status'] == 'OK')
print(f'\nSaved to {OUT}: {n_ok}/{len(results)} OK')
