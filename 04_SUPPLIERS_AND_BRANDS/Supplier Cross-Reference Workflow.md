---
name: supplier-cross-reference
description: Ingest a tile/bath supplier's website, build a collections reference in the Afoi Deli vault, and cross-reference each collection against our own catalogue at afoideli.gr (WooCommerce Store API). Use when the user says "do the same for <supplier>", "ingest <supplier>", "cross-reference <supplier> against my site", or names a manufacturer to document. Produces: a supplier folder, a Collections Reference note, an afoideli.gr presence column, and a catalogue/asset ingestion plan.
type: workflow
status: active
created: 2026-06-15
updated: 2026-06-15
tags:
  - workflow
  - skill
  - suppliers
  - cross-reference
---

# Supplier Cross-Reference Workflow

> [!info] What this is
> A repeatable pipeline to document any supplier's collections and cross-reference them against our own range on afoideli.gr. Built from the Kronos pilot (2026-06-15). This note is written as a **SKILL.md** — to make it a callable skill, copy this file to `<vault>/.claude/skills/supplier-cross-reference/SKILL.md` or your skills directory, keeping the YAML frontmatter above. It also stands alone as the human runbook.
>
> **Trigger phrases:** "ingest <supplier>", "do the Kronos treatment for <supplier>", "cross-reference <supplier> against my site", "library/documentation for <supplier>".

## Inputs the operator provides

- Supplier name (e.g. "Cielo") and its website URL.
- (Optional) the rep/agency, if known — for the supplier note's commercial section.

## The afoideli.gr verification engine (the robust path)

afoideli.gr is a **JavaScript WooCommerce store**. Static fetch and web-search both give unreliable results (search yields true positives but false negatives; the on-site search needs JS). The **authoritative source is the WooCommerce Store API**, which is unauthenticated and returns clean JSON:

```
https://afoideli.gr/wp-json/wc/store/v1/products?search=<term>&per_page=20
```

Each hit returns `name`, `slug`, `permalink`, `sku`, `prices`, `images`, `categories`, and (where set) brand. `permalink` is the exact product URL to record.

> [!warning] Where this must run
> Claude's hosted `web_fetch` is blocked from arbitrary `/wp-json/` URLs (only URLs surfaced by a prior search are fetchable). So the Store API call runs from **your side**:
> - **Python worker** (preferred — already in the stack): loop the collection names, GET the endpoint, dump JSON. See snippet below.
> - **Browser / curl**: paste the JSON back into chat and Claude parses it.
> - **Claude in Chrome** (fallback for sites with no open API): drive the live site search, read rendered results.
>
> Search-only is the **last resort** and its negatives must be written as `unverified`, never `absent`.

### Python worker snippet (the engine)

```python
import requests, json, time

BASE = "https://afoideli.gr/wp-json/wc/store/v1/products"

def check(term):
    r = requests.get(BASE, params={"search": term, "per_page": 20}, timeout=20)
    r.raise_for_status()
    return [{"name": p["name"], "slug": p["slug"],
             "url": p["permalink"], "sku": p.get("sku", "")}
            for p in r.json()]

collections = ["Materia", "Nativa", "Pierre Vive", "..."]  # from the reference note
results = {}
for c in collections:
    try:
        results[c] = check(c)
    except Exception as e:
        results[c] = {"error": str(e)}
    time.sleep(0.5)  # be polite

print(json.dumps(results, ensure_ascii=False, indent=2))
```

Match rule: a result whose `name`/`slug` contains the collection name (case-insensitive, accent-folded) is a **match**. Record its `url`.

## Match-classification rules (operator chose: flag fuzzy, don't guess)

For each manufacturer collection, classify and label in the reference note:

- **✅ present** — exact or near-exact name match in Store API. Record the `permalink`. Note if our site appends the brand ("Nativa Kronos") or renames it.
- **🟡 possible match — verify** — a product exists with a *different* name but same brand + look + likely the same range (our site renames things). Record **both names** and the URL, and leave it for human confirmation. Never silently equate them.
- **⬜ unverified** — not found by the method used. Means "not found", NOT "absent". Only ever downgrade to a true "not carried" after a clean Store API pass returns nothing.

## Full procedure (run order)

1. **Read the supplier note** (`Suppliers/<Name>/Supplier - <Name>.md`). If none exists, note it — the reference note can still be created and linked.
2. **Fetch the manufacturer's collections index** (e.g. `/collections/`). List every collection + URL.
3. **Fetch each collection page** at summary depth (use `defuddle` skill or `web_fetch` with a ~4-5k token limit; the body's description + colour names + catalogue/technical PDF links are the payload — nav menu eats budget, so cap it). Capture: look/material (from the page's own text, not the homepage slider — those mislabel), one-line character, colours/structures, catalogue PDF, technical PDF, page URL.
4. **Cross-reference afoideli.gr** for each collection via the Store API engine above. Classify per the rules.
5. **Write `Suppliers/<Name>/<Name> — Collections Reference.md`** — frontmatter (`type: reference`, `parent: "[[Supplier - <Name>]]"`), an intro callout, the confidence warning, one entry per collection with: look, description, `Page:`, `Catalogue:`, `Technical:`, `On afoideli.gr:`.
6. **Write `Suppliers/<Name>/<Name> — Catalogue & Asset Ingestion.md`** — the Drive-tree + binaries-in-Drive/links-in-Obsidian plan (clone the Kronos one; swap names and the manifest pointer).
7. **Wire backlinks**: add a Product-range section + links in the supplier note; add the asset job to [[Automation Backlog]]; add a deferred line in [[Capture Backlog]] if not live yet.
8. **Folder discipline**: everything lives under `Suppliers/<Name>/`. Create the folder first (`create_directory`) — `move_file` won't make parents.

## Output artifacts (the definition of done)

- `Suppliers/<Name>/Supplier - <Name>.md` (exists or flagged)
- `Suppliers/<Name>/<Name> — Collections Reference.md` (with afoideli column)
- `Suppliers/<Name>/<Name> — Catalogue & Asset Ingestion.md`
- Backlinks updated in the supplier note + automation/capture backlogs.

## Gotchas learned on the Kronos pilot

- **Homepage sliders mislabel looks** (Kronos showed Pierre Vive as "metal"; it's stone). Always classify from the collection's own page.
- **Generic collection names collide** ("Essence", "Materia" exist across many brands and at other retailers). Always scope the match to *our* site + the right brand.
- **Brand-as-suffix**: afoideli product names often append the manufacturer ("Woodside Kronos"). Search the bare collection name, then confirm the brand in the result.
- **The supplier's brand name itself can be search-polluted** ("Kronos" → Greek mythology, a death-metal band, a gyro company). Don't rely on web search for presence; use the Store API.
- **Cap fetch token limits** on manufacturer pages (~4-5k) — the shared nav menu otherwise consumes the whole budget before the body.

## Links

- Pilot output → [[Kronos — Collections Reference]] · [[Kronos — Catalogue & Asset Ingestion]] · [[Supplier - Kronos]]
- Pipeline home → [[Automation Backlog]] · [[Python Worker Map]]
- Indexes → [[Supplier Master Index]] · [[Brand Master Index]]
