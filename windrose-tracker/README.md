# 🧭 Windrose Recipe Tracker

A shared, color-coded **Google Sheet** for the crew (**Eze · Cowy · Nick · Cheese**) that doubles
as a full crafting reference *and* a recipe tracker. Built from the community **WindrosePlus**
catalogue: **295 recipes** with real in-game icons, rarity, crafting station, ingredients, and
(where it applies) the merchant that sells them. Exact-duplicate names are merged to one row each.

**One tab per category.** Click into whichever you want — and only the **gear** tabs carry a
checkbox per player, because those are the recipes worth coordinating.

| Tab | Contents | Player checkboxes? |
|-----|----------|:--:|
| **Dashboard** | Crew scoreboard + per-tab breakdown, totals across the gear tabs | — |
| **Armor** | Armor + backpacks (39) | ✅ trackable |
| **Jewelry** | Rings + necklaces (57) | ✅ trackable |
| **Weapons** | Melee, ranged, tools, ammo (47) | ✅ trackable |
| **Ship Gear** | Cannons + hull mods (18) | ✅ trackable |
| **Consumables** | Food, potions, medicine (53) | 📖 reference |
| **Resources** | Refined materials (39) | 📖 reference |
| **Misc** | Buildables (42) | 📖 reference |
| **How to use** | The workflow, in the sheet | — |

> **Why only gear is trackable:** food & potions **auto-unlock** the moment you pick up their
> ingredients — everyone gets them, nothing to coordinate. **Gear** (armour, weapons, jewellery,
> ship cannons) is unlocked deliberately and can be **copied to a crewmate**, so those tabs get the
> checkboxes. Consumables/Resources/Misc are kept as a browseable catalogue only.

---

## ⚡ Set it up (about 2 minutes, one time)

1. Make a new blank Google Sheet — go to **[sheet.new](https://sheet.new)**.
2. **Extensions ▸ Apps Script**.
3. Select everything in the editor, delete it, then paste **all** of [`Code.gs`](./Code.gs).
4. Click **Save** (💾), then **Run ▸ `buildWindroseTracker`**.
5. Click **Review permissions ▸ Allow**. *(The script only edits **this** sheet.)*
6. **Switch back to the Google Sheets browser tab** — the tabs build themselves and a “🧭 Windrose
   ready” toast pops. Hit **Share** (top-right) and add the crew as **Editors**.

A **🧭 Windrose** menu appears after the first run — rebuild any time; your ticks survive.

---

## 📋 The workflow
- On a **gear tab**, tick **your** column when you learn a recipe.
- **Who has it** shows who can hand you a copy; **Owned** = how many of you have it.
- **Buy from Merchant** (yellow) means a vendor sells it — only buy if no crewmate has it.
- The **Dashboard** totals everyone across all the gear tabs.

### Filters & color
- Native column filters (the ▾ arrows): slice any tab by **Type**, **Rarity**, **Station**, or by a
  crew member's checkbox (TRUE = has it / FALSE = still needs it).
- Rarity is color-coded **Common → Uncommon → Rare → Epic → Legendary**.
- On gear tabs, **Owned** is a red→green heat scale (0 of 4 → all 4).

---

## 🛠️ Extend it
- Add rows at the bottom of any tab — fill the columns and tick boxes as usual.
- Want a picture on a custom row? Drop `=IMAGE("https://…")` into its Icon cell.
- Re-run **🧭 Windrose ▸ Build / Rebuild tracker** to refresh formatting.

---

## 🔧 How it's wired (for the curious)
- Icons are real game textures (WebP → PNG) committed under [`icons/items/`](./icons/items) and
  referenced via `=IMAGE("https://raw.githubusercontent.com/…")` (pinned to a commit, so they're stable).
- The full dataset lives in [`data.json`](./data.json); regenerate the script from it if you tweak it.
- Tab layout & which tabs are trackable are configured in the `TABS` array at the top of `Code.gs`.
- Data/icon source: the community **WindrosePlus** project's bundled catalogue (840 items indexed).
