#!/usr/bin/env python3
"""
Windrose -> Recipe Tracker sync.

Reads your local Windrose save, figures out which GEAR recipes (armor, jewelry,
weapons, ship gear) you've unlocked, and prints a SYNC CODE to paste into the
shared Google Sheet (🧭 Windrose ▸ Import my recipes).

USAGE (Windows, game CLOSED):
    1) Install Python 3 from python.org (tick "Add to PATH").
    2) Open Command Prompt and run:
           pip install rocksdict pymongo
    3) Run:
           python windrose_sync.py
       (Optional: pass a save path,  python windrose_sync.py "C:\\path\\to\\Players")

It only READS the save. Nothing is written to the game or sent anywhere.
"""
import os, sys, glob, json, re, base64

HERE = os.path.dirname(os.path.abspath(__file__))
ACTIONS = {'craft', 'upgrade', 'recraft', 'ascend', 'recipe', 'disassemble',
           'base', 'advanced', 'default', 'stock'}
TYPEPFX = {'eid', 'cid', 'did', 'aid', 'bid', 'rd'}


def token(s):
    s = s.split('/')[-1].split('.')[0]
    s = s.replace('DA_RD_', '').replace('DA_', '')
    out = []
    for i, p in enumerate(s.split('_')):
        pl = p.lower()
        if i == 0 and pl in TYPEPFX: continue
        if pl in ACTIONS: continue
        if re.fullmatch(r't\d+', pl): continue
        out.append(pl)
    return '_'.join(out)


def load_map():
    with open(os.path.join(HERE, "windrose_map.json"), encoding="utf-8") as f:
        return json.load(f)


def candidate_roots(argv):
    if len(argv) > 1:
        return [argv[1]]
    la = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
    return [os.path.join(la, "R5", "Saved", "SaveProfiles")]


def find_player_dbs(roots):
    found = set()
    for root in roots:
        if os.path.isfile(os.path.join(root, "CURRENT")):
            found.add(root)
        for cur in glob.glob(os.path.join(root, "**", "CURRENT"), recursive=True):
            d = os.path.dirname(cur)
            if os.path.basename(os.path.dirname(d)).lower() == "players":
                found.add(d)
    return sorted(found)


def read_unlocked(db_path):
    from rocksdict import Rdict, Options, AccessType
    import bson
    cfs = Rdict.list_cf(db_path)
    db = Rdict(db_path, options=Options(raw_mode=True),
               column_families={c: Options(raw_mode=True) for c in cfs},
               access_type=AccessType.read_only())
    try:
        h = db.get_column_family("R5BLPlayer")
    except Exception:
        return None, []
    for _k, v in h.items():
        doc = bson.decode(bytes(v))
        pm = doc.get("PlayerMetadata") or {}
        return doc.get("PlayerName", "?"), (pm.get("UnlockedRecipes") or [])
    return None, []


def recipe_paths(unlocked):
    for e in unlocked:
        rd = (e.get("Recipe") or {}).get("RecipeData") if isinstance(e, dict) else e
        if isinstance(rd, str):
            yield rd


def main():
    try:
        m = load_map()
    except Exception as e:
        sys.exit("Could not read windrose_map.json next to this script: %s" % e)
    EXACT, TOKEN = m["exact"], m["token"]

    try:
        import rocksdict, bson  # noqa
    except ImportError:
        sys.exit("Missing dependencies. Run:  pip install rocksdict pymongo")

    roots = candidate_roots(sys.argv)
    dbs = find_player_dbs(roots)
    if not dbs:
        sys.exit("No Windrose save found under:\n  " + "\n  ".join(roots) +
                 "\nClose the game, or pass the path to your Players folder as an argument.")

    best = None  # (count, name, names_set, db)
    for db in dbs:
        try:
            name, unlocked = read_unlocked(db)
        except Exception as e:
            print("  (skip %s: %s)" % (db, str(e)[:60]))
            continue
        matched = set()
        for rd in recipe_paths(unlocked):
            if "/Disassemble/" in rd:
                continue
            b = rd.split("/")[-1].split(".")[0]
            nm = EXACT.get(b) or TOKEN.get(token(rd))
            if nm:
                matched.add(nm)
        if best is None or len(matched) > len(best[2]):
            best = (len(unlocked), name, matched, db)

    if not best or not best[2]:
        sys.exit("Found a save but no recognizable gear recipes. Is the game updated?")

    _cnt, name, names, db = best
    payload = {"v": 1, "recipes": sorted(names)}
    code = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")

    print("\nCharacter : %s" % name)
    print("Save      : %s" % db)
    print("Gear recipes detected: %d" % len(names))
    print("\n================  SYNC CODE  (copy the whole line)  ================\n")
    print(code)
    print("\n===================================================================")
    print("Paste it into the sheet:  🧭 Windrose ▸ Import my recipes")


if __name__ == "__main__":
    main()
