# 🔄 Auto-fill your recipes from your save

Instead of ticking boxes by hand, run this little tool once after a play session. It reads your
local Windrose save, works out which **gear recipes** (armor, jewelry, weapons, ship gear) you've
unlocked, and prints a **SYNC CODE**. Paste that into the sheet and your column fills itself in.

- **Read-only & private.** It only *reads* the save — it never edits the game and never sends
  anything anywhere. The code you paste is created locally on your PC.
- **Safe import.** In the sheet it only ever *adds* checkmarks — it never unticks anything you or
  a crewmate already marked.

---

## One-time setup (Windows)
1. Install **Python 3** from [python.org](https://www.python.org/downloads/) — tick **“Add Python to PATH”** during install.
2. Download this **`sync`** folder (keep `windrose_sync.py` and `windrose_map.json` together).
3. Open **Command Prompt** and install the two libraries:
   ```
   pip install rocksdict pymongo
   ```

## Each time you want to sync
1. **Close Windrose** (the save is locked while the game runs).
2. In Command Prompt, go to the folder and run it:
   ```
   cd path\to\sync
   python windrose_sync.py
   ```
3. It prints your character name, how many gear recipes it found, and a **SYNC CODE**. Copy the whole code line.
4. In the Google Sheet: **🧭 Windrose ▸ Import my recipes** → paste the code → type your name (`Eze`, `Cowy`, `Nick`, or `Cheese`). Done — your column fills in.

Re-run any time; importing again just tops up your column.

---

## Troubleshooting
- **“No Windrose save found”** → pass your save path directly:
  ```
  python windrose_sync.py "%LOCALAPPDATA%\R5\Saved\SaveProfiles"
  ```
- **Multiple characters?** It automatically picks the one with the most unlocked recipes.
- **“Missing dependencies”** → run `pip install rocksdict pymongo` again (step 3).

## How it works (for the curious)
Windrose saves are a **RocksDB** database; each character's state is a **BSON** document whose
`PlayerMetadata.UnlockedRecipes` lists every learned recipe (as `DA_RD_*` asset paths). The tool
maps those onto the tracker's gear recipes via [`windrose_map.json`](./windrose_map.json) using two
strategies — exact recipe-ID match plus an item-token match — to stay accurate across game-version
naming changes, and skips disassemble recipes. Food/potions/resources are ignored (they're not tracked).
