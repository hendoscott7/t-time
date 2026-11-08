# T-Time

A tiny dinner spinner for a fussy toddler. Spin for something to try, tick what he eats, nope what he won't, and plan the week.

Open `index.html` in a browser — it's a single self-contained page.

## Using it

- **Spin** — picks a dinner or food. Untried things come up more often; recent picks rarely repeat.
- **✕** — nope. Takes it out of the hat and spins again. Undo appears for a few seconds.
- **✓** — he ate it. Tap again to untick.
- **Dot above a name** — it has a recipe. Tap the name to see it.
- **List icon** (top right) — yes and nope lists. Tap a yes to make it tonight's pick; bin or ✕ to remove.
- **Calendar** — the week. Fill days one at a time with **+**, fill the rest with **↻**, or clear with the bin. Tap a dinner to expand its recipe.
- **Hold Spin** — fills the whole week in one go.

Follows the device's light or dark mode. Choices are saved in the browser (`localStorage`).

## Editing the food library

The page is generated from `src/`:

- `src/lib.py` — every dinner and food, tagged savoury/sweet and dinner/food, plus extra recipes
- `src/recipes_base.txt` — the main dinner recipes (`"Name":"ingredient;… | step;…"`)
- `src/template.html` — the page itself

After editing, rebuild:

```sh
python3 src/assemble.py
```
