---
type: index
created: 2026-06-16
updated: 2026-06-16
status: active
tags:
  - suppliers
  - enrichment
  - backlog
---

# Supplier Enrichment Queue

> [!tip] What this is
> The single answer to *"what have I left blank to fill in later?"* Every supplier dossier is a **living document**: public facts are filled, private/commercial facts are left as **visible prompts**. This note is how you find and clear those prompts — nothing is silently lost. See [[Supplier Research Workflow]] for the enrichment contract.

## The three markers — search these

Open Obsidian search (top-left 🔍) and run each query; they work across the whole vault:

| Search | Surfaces |
|---|---|
| `"(your knowledge)"` | Every **private** field waiting on you — payment terms, discount ceiling, loading/packaging, hero SKUs, specialization, relationship truth. |
| `"(to populate)"` | **Stub** fields — mostly the *Automation potential* blocks. |
| `"needs_check"` | **Public facts to verify** — VAT/addresses, certifications, the Fantini Greek-importer confirmation, etc. |

> [!note] Tip
> Every dossier's open private fields live in `> [!question] (your knowledge)` callouts. The search `"(your knowledge)"` is the fastest way to walk them brand by brand.

## What each brand needs filled (the dimensions)

Per supplier, over repeated passes (the standing slots in every dossier):

- [ ] **Lead times** — normal vs. special, per hero line
- [ ] **Famous for / hero products** — what the market knows them for; our best-sellers / high-margin / difficult lines
- [ ] **Payment terms** + real **discount ceiling**
- [ ] **Specializations / technical niche** — where they're the right call (and where they aren't)
- [ ] **Loading habits, packaging quirks, common proforma mistakes**
- [ ] **Relationship status & power geometry** — lives in the conduit note ([[Conduit - Plus Interiors]] / [[Conduit - Filon IKE]])

## Dossiers (full = carries the prompts; stub = needs research first)

```dataview
TABLE confidence, status, updated
FROM "04_SUPPLIERS_AND_BRANDS/Suppliers"
WHERE type = "supplier"
SORT updated DESC
```

The `memory_seed` stubs (Florim, Atlas Concorde, Antonio Lupi, ABK, Emilgroup, 41zero42, Sant'Agostino, Fima Carlo Frattini) need the **public research first** — run the [[Supplier Research Workflow]]. The full dossiers (Kronos, Cielo, Mutina, Fantini, Scavolini) are ready for your private enrichment now.

> [!success] Enrichment progress
> - **[[Supplier - Kronos\|Kronos]]** — first private pass landed (2026-06-17): **discount cascade** (base −70 / module −60−10 / decor −60−10−5), **payment & credit** (90 d standard / 120 d stock), **sale conditions**, and the **2026 price list** archived (`_sources/`). Cost-to-quote chain seeded in [[Cost & Quote Build]]. *Still open for Kronos `(your knowledge)`:* hero SKUs / our best-sellers, lead-time-per-hero-line, loading & packaging habits, common proforma mistakes.

## Links
- [[Supplier Master Index]] · [[Supplier Research Workflow]] · [[Capture Backlog]]
- Conduits → [[Conduit - Plus Interiors]] · [[Conduit - Filon IKE]]
