from pathlib import Path
import hashlib, json, sys

def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root/'MANIFEST_SHA256.json').read_text(encoding='utf-8'))
    expected = {row['path']:row['sha256'] for row in manifest['files']}
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST_SHA256.json' and '__pycache__' not in p.parts and '.venv' not in p.parts}
    errors=[]
    if actual!=set(expected): errors.append('File inventory differs from original package')
    for rel,digest in expected.items():
        p=root/rel
        if not p.is_file(): errors.append('Missing: '+rel)
        elif hashlib.sha256(p.read_bytes()).hexdigest()!=digest: errors.append('Changed: '+rel)
    for e in errors: print(e)
    print('PASS' if not errors else 'FAIL',len(expected),'payload files')
    return int(bool(errors))

if __name__=='__main__': sys.exit(main())
