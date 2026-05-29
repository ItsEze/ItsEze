# 🧭 Windrose Recipe Tracker

A shared, color-coded **Google Sheet** for the crew (**Eze · Cowy · Nick · Cheese**) to track
which Windrose recipes each of you has unlocked — so nobody wastes coin or a single-use
**Recipe Paper** on something a crewmate can already copy to you.

Built from the community **WindrosePlus** catalogue: **167 shareable gear recipes** — armour,
weapons & jewellery — each with its real in-game icon, rarity, crafting station, ingredients,
and (where it applies) the merchant that sells it.

> **Why only gear?** The tracker deliberately holds only recipes worth coordinating: ones you
> *deliberately unlock* and can *hand a copy of* to a crewmate. **Food & potions** auto-unlock
> the moment you pick up their ingredients, and **ships** can't be handed over — so those, plus
> refined materials and buildables, are intentionally left out. (The full 331-recipe set lives in
> this repo's git history if you ever want it back.)

---

## ⚡ Set it up (about 2 minutes, one time)

1. Make a new blank Google Sheet — easiest is to go to **[sheet.new](https://sheet.new)**.
2. **Extensions ▸ Apps Script**.
3. Select everything in the editor, delete it, then paste **all** of [`Code.gs`](./Code.gs).
4. Click **Save** (💾), then **Run ▸ `buildWindroseTracker`**.
5. Click **Review permissions ▸ Allow**. *(The script only edits **this** sheet — nothing else.)*
6. Switch back to the sheet. It's built. Hit **Share** (top-right) and add the crew as **Editors**.

A **🧭 Windrose** menu appears after the first run — use it to rebuild any time. Your ticks
live in the sheet, so rebuilding never wipes them.

---

## 📋 What you get

| Tab | What it does |
|-----|--------------|
| **Dashboard** | Live scoreboard — recipes known per crew member, % complete, a Type × crew matrix (Armor / Ring / Necklace / Backpack / Melee / Range / Tool / Ammo), and how many recipes nobody has yet. |
| **Recipes** | One row per recipe: icon, name, category, type, rarity (color-coded), unlock, station, ingredients, merchant, a checkbox for each of the 4 of you, **Owned** count, and **Who has it**. Every column filters. |
| **How to use** | The day-to-day workflow, in the sheet itself. |

### The core workflow
- Tick **your** column when you learn a recipe.
- **Who has it** instantly tells you who can hand you a copy.
- **Buy from Merchant** (highlighted yellow) means a vendor sells it — only buy if no crewmate has it.
- Filter **Owned = 0** to find recipes nobody has unlocked yet.

### Filters & color
- Native column filters (the ▾ arrows): slice by **Category**, **Rarity**, **Station**, or by a
  crew member's checkbox (TRUE = has it / FALSE = still needs it).
- Rarity is color-coded **Common → Uncommon → Rare → Epic → Legendary**.
- **Owned** is a red→green heat scale (0 of 4 → all 4).

---

## 🛠️ Extend it
- Add your own rows at the bottom — fill the columns and tick boxes as usual.
- Want a picture on a custom row? Drop `=IMAGE("https://…")` into its Icon cell.
- Re-run **🧭 Windrose ▸ Build / Rebuild tracker** to refresh formatting.

---

## 🔧 How it's wired (for the curious)
- Icons are real game textures (WebP → PNG) committed under [`icons/items/`](./icons/items) and
  referenced from the Recipes sheet via `=IMAGE("https://raw.githubusercontent.com/…")`.
- The full dataset lives in [`data.json`](./data.json) (regenerate the script from it if you tweak it).
- Data/icon source: the community **WindrosePlus** project's bundled catalogue snapshot.
