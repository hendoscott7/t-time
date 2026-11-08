import json, os, sys
from lib import entries, EXTRA_RECIPES
old = json.loads("{" + open(os.path.join(os.path.dirname(__file__), 'recipes_base.txt')).read().strip().rstrip(',') + "}")
rec = {**old, **EXTRA_RECIPES}
lib = entries()
names = {e[0] for e in lib}
missing = [k for k in rec if k not in names]
assert not missing, missing
state = sys.argv[1] if len(sys.argv) > 1 else '{"last":null,"items":[]}'
h = open(os.path.join(os.path.dirname(__file__), 'template.html')).read()
h = h.replace('__LIB__', json.dumps(lib, ensure_ascii=False)).replace('__RECIPES__', json.dumps(rec, ensure_ascii=False, indent=0)).replace('__STATE__', state)
open(os.path.join(os.path.dirname(__file__), '..', 'index.html'),'w').write(h)

print(len(lib), "items,", len(rec), "recipes")
