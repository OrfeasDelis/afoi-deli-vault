---
type: plan
parent: "[[Supplier - Kronos]]"
status: backlog
created: 2026-06-15
updated: 2026-06-15
tags:
  - kronos
  - ingestion
  - assets
  - google-drive
  - backlog
---

# Kronos — Catalogue & Asset Ingestion

> [!abstract] Purpose
> A repeatable way to pull each Kronos collection's **catalogue PDF, technical sheet, and photography** into cold storage (Google Drive), and link those assets back from Obsidian — without bloating the vault with binaries. Designed as the **template** for every other supplier afterwards (Cielo, Mutina, Fantini…). Generalises the earlier Cielo 2026 catalogue import.

## Principle (fits the agent-OS layer contract)

Per the agent OS design: **Obsidian = canonical knowledge (text/links), Google Drive = cold asset storage (binaries).** Obsidian never stores the heavy files; it stores the *record of* and *link to* them. Single-writer-per-layer holds: assets are written to Drive, the index note is written in Obsidian.

So the artifact this produces is **not** copied PDFs in the vault — it's (a) an organised Drive folder tree and (b) an Obsidian index note per collection (or a Dataview/Base over them) whose links resolve to Drive.

## Proposed Google Drive structure

```
Afoi Deli / Suppliers / Kronos /
  _catalogues/        ← collection catalogue PDFs (Materia.pdf, NATIVA.pdf, …)
  _technical/         ← scheda tecnica PDFs (materia-st.pdf, …)
  Collections /
    Materia /
      catalogue.pdf
      technical.pdf
      photos/         ← location + colour swatch images
    Nativa / …
    Pierre Vive / …
    (one folder per collection)
```

Naming: `kronos__<collection>__<type>.pdf` so files are self-describing if they ever leave the tree. Keep a stable Drive folder ID per collection so links don't break on rename.

## Source URLs already captured

All catalogue + technical PDF links per collection are in [[Kronos — Collections Reference]]. That note is the manifest — the ingestion job reads URLs from there. Plus per-collection "Locations" galleries and colour swatches on each `/collections/<slug>/` page, and a configurator route for per-finish images (same approach used for Cielo).

## How it could run (options, lightest first)

1. **Manual-assisted (now):** download the ~26 PDFs from the reference note, drop into the Drive tree, paste back the Drive share links into each collection's index note. Zero infra. Good enough for a one-off.
2. **Telegram capture queue (early win):** text Hermes a collection name/URL/PDF → it queues → worker drains into the Drive tree + reference note. See [[Hermes Telegram Capture Queue]]. Ships before the auto-diff because *you* are the trigger.
3. **Scripted fetch (Python worker):** a small script reads URLs from [[Kronos — Collections Reference]], downloads PDFs + listed images, writes them to a local `staging/` dir, then the Drive client uploads into the tree and returns file IDs. Emits a JSON manifest (collection → {catalogue_id, technical_id, photo_ids}) that an Obsidian note or Base renders. Mirrors the Cielo openpyxl/JSON import pattern.
4. **Hermes (recurring):** once stable, Hermes re-checks the collections index monthly for new/changed PDFs (the pages carry `article:modified_time`) and flags diffs. Low priority until the OS exists. **Note:** the [[Hermes Telegram Capture Queue]] is the earlier, simpler sibling — manual capture feeding the same Drive/vault pipeline; the monthly diff later becomes a second feeder into that same queue.

## Obsidian linking pattern

- Each collection gets a short index note (or a row in a [[obsidian-bases|Base]]) with: look, Drive catalogue link, Drive technical link, Drive photos folder link, last-synced date.
- Vault stores **links + metadata only**; binaries stay in Drive.
- Optionally embed one hero thumbnail per collection (small JPG) for visual scanning — that's the only binary worth keeping local.

## Open questions

- [ ] Confirm the Drive account/shared-drive this should live under (personal vs. company).
- [ ] Decide: per-collection index notes, or a single Base over a `kronos_assets.json` manifest? (Base scales better to other suppliers.)
- [ ] Photo scope: catalogue + technical only, or also scrape the location galleries and per-finish configurator images? (The latter is the heavier Cielo-style job.)
- [ ] Whether to also archive the 195-row-style SKU data per collection (separate from this asset job — that's a CSV/Supabase import, not Drive).

## Why deferred

The vault↔Drive link is only frictionless once the live MCP/Drive write path is solid (see the NEXT ACTION in [[Capture Backlog]]). Until then, option 1 (manual) is fine for the collections you actually quote most.

## Links

- Manifest of source URLs → [[Kronos — Collections Reference]]
- Parent supplier → [[Supplier - Kronos]]
- Pipeline home → [[Automation Backlog]] · [[Python Worker Map]]
- Storage doctrine → [[Hermes Obsidian Codex Interface]]
