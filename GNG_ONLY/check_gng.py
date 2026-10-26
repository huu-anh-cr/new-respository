from pathlib import Path
import ast, sys, warnings

def main():
    root = Path(__file__).resolve().parent
    failed = 0
    for i in range(1,9):
        path = root / ('gng%d.py' % i)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', SyntaxWarning)
            tree = ast.parse(path.read_text(encoding='utf-8-sig'))
        paths = []
        for node in ast.walk(tree):
            if isinstance(node,ast.Assign):
                for target in node.targets:
                    if isinstance(target,ast.Name) and target.id in ('target_script','candidates'):
                        try: value = ast.literal_eval(node.value)
                        except (ValueError,TypeError): continue
                        if isinstance(value,str): paths.append(value)
                        elif isinstance(value,list): paths.extend(v for v in value if isinstance(v,str))
        ok = any(Path(p).is_file() for p in paths)
        print('gng%d: %s' % (i,'TARGET FOUND' if ok else 'TARGET MISSING'))
        for p in paths: print('  '+p)
        if not ok: failed += 1
    print('Path checks only. No model calls. Missing standalone engines must be supplied separately.')
    return int(failed > 0)

if __name__=='__main__': sys.exit(main())
