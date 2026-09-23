#!/usr/bin/env python3
"""Rename docs: remove ' — Final' from titles. Reads rename_list.json, writes rename_log.json."""
import json, subprocess, sys, time, os

GDIR = '/home/hatch/workspace/teenz-bible-review/gdocs_build'

def run(args, timeout=120):
    r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    return r.returncode, r.stdout, r.stderr

def main():
    recs = json.load(open(os.path.join(GDIR, 'rename_list.json')))
    log = []
    for i, r in enumerate(recs):
        doc_id, new = r['id'], r['new']
        ok, msg = False, ''
        for attempt in range(3):
            rc, out, err = run(['hatch_gws_cli', 'drive', 'files', 'update',
                                '--params', json.dumps({'fileId': doc_id}),
                                '--json', json.dumps({'name': new})])
            if rc == 0:
                ok = True
                break
            msg = err[:200]
            time.sleep(5)
        log.append({'id': doc_id, 'old': r['old'], 'new': new,
                    'renamed': ok, 'err': msg})
        print(f"[{i+1}/{len(recs)}] {'OK' if ok else 'FAIL'} {new}", flush=True)
        time.sleep(2)
    json.dump(log, open(os.path.join(GDIR, 'rename_log.json'), 'w'),
              ensure_ascii=False, indent=1)
    fails = [x for x in log if not x['renamed']]
    print(f"DONE: {len(log)-len(fails)}/{len(log)} renamed, {len(fails)} failed")

if __name__ == '__main__':
    main()
