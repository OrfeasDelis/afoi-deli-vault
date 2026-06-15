---
name: supplier-research
description: Produce best-in-depth public research on a tile/bath supplier and write it into the Afoi Deli vault as a structured supplier dossier, ready for Orfeas to enrich with non-public commercial and relationship knowledge. Use when Orfeas says "ingest <supplier>", "research <supplier>", "do the Kronos treatment for <supplier>", "build a dossier for <supplier>", or names a manufacturer to document. Produces a supplier folder with a populated supplier note and a collections reference note. Does NOT touch afoideli.gr or any cross-reference — public research only.
type: workflow
status: active
created: 2026-06-15
updated: 2026-06-15
supersedes: Supplier Cross-Reference Workflow
tags:
  - workflow
  - skill
  - suppliers
  - research
  - ingestion
---

# Supplier Research Workflow

> [!info] What this is
> The repeatable pipeline for documenting a supplier from **public sources only** — the manufacturer's own site first, then the wider web — to the depth of the [[Supplier - Kronos]] pilot. The output is a dossier you can read in one sitting and then **enrich with what only you know**: the rep, the discount ceiling, the loading habits, the forgiven lateness, the relationship truth. Public research is the floor; your knowledge is the value on top.
>
> This note is written as a **SKILL.md**. To make it a callable skill, copy it to `<vault>/.claude/skills/supplier-research/SKILL.md` keeping the YAML above. It also stands alone as the human runbook.
>
> **Trigger phrases:** "research <supplier>", "ingest <supplier>", "do the Kronos treatment for <supplier>", "build a dossier for <supplier>", "document <supplier>".

> [!note] Relationship to the old workflow
> This supersedes the earlier **cross-reference workflow**. The afoideli.gr Store-API cross-reference is deliberately removed — we research suppliers first and leave our own site alone. The cross-reference machinery is parked, not deleted: its spec now lives in [[Automation Backlog]] (the *Supplier ↔ afoideli.gr cross-reference (Store API)* idea), to revive if and when matching against our range becomes the goal. Until then, no `On afoideli.gr` column appears in any note this workflow produces (the Kronos pilot reference predates this and keeps its column as parked data).

---

## The principle behind the depth

The split between **public** and **private** knowledge is the spine of this workflow.

- **Public** = anything on the manufacturer's site, distributor sites, the trade press, LinkedIn, registries. Claude can get all of it. It is necessary but commoditised — a competitor can read the same pages.
- **Private** = the rep's name and character, the real discount ceiling, payment terms, loading habits, which collections actually sell, where lateness is forgiven, the power geometry of the conduit. **Only you have this**, and it is where the real value of a supplier note lives.

So the dossier is built in two strata, visibly marked:
1. Claude fills the **public** strata as deeply and accurately as the web allows, flagging confidence honestly.
2. Every **private** field is left as an explicit, labelled prompt — `> [!question] (your knowledge) …` — so enrichment is a guided fill-in, never a blank page. The Kronos note shows the destination: public range + projects + K-LAB on top, your commercial truth and the Plus Interiors power-geometry callout underneath.

Never silently guess a private fact. A clean public dossier with honest gaps beats a plausible-looking one with invented terms.

## Inputs the operator provides

- Supplier name (e.g. "Cielo") and, if known, the website URL (Claude will search for it otherwise).
- Optional one-liner of why they matter / how they reach us — Claude folds it into the strategic section and turns the rest into enrichment prompts.

## Source hierarchy (best-first)

Work down this list; prefer primary sources and mark confidence by tier.

1. **The manufacturer's own website** — collections, company/about, sustainability, press/news, downloads (catalogue + technical PDFs), showroom/contact pages. The authoritative source for product and identity. `confidence: confirmed` for what it states directly.
2. **Official registries / legal** — the legal entity, VAT/P.IVA, registered address, group ownership (e.g. an Italian SpA inside a larger ceramics group). `confirmed` when from an official or the company's own imprint.
3. **Trade press & design media** — Cersaie coverage, Floor Daily, Domus/Dezeen/Archiproducts launches, group financials. Good for history, ownership moves, awards, design-director names. `likely`.
4. **LinkedIn / company profiles** — size, HQ, leadership, distribution footprint. `likely`.
5. **Distributor & spec sites** — other markets' distributor pages, architect spec libraries (Archello, Material Bank). Useful for formats/specs cross-checking. `likely`.
6. **General web search** — last, and treated with care: brand names collide and are search-polluted (the Kronos pilot hit a Greek titan, a death-metal band, and a gyro shop). Scope every query with the ceramics/bath context and the country. `needs_check` unless corroborated.

> [!tip] Fetch discipline (learned on Kronos)
> - **Classify looks/materials from each collection's own page**, never the homepage slider — sliders mislabel (Kronos showed a stone line as "metal").
> - **Cap fetch token limits (~4–5k) on collection pages** — the shared nav menu eats the budget before the body. Use the `defuddle` skill to strip clutter where useful.
> - Fetch the **collections index** once, then each collection page individually at summary depth: description, colour/structure names, catalogue PDF, technical PDF, page URL.
> - Capture **PDF links, don't download** during research — the binary-asset plan is a separate, deferred job (see step 7).

## Full procedure (run order)

1. **Locate & identify.** Confirm the official website. Pull the legal entity, registered address, VAT/P.IVA, and group/ownership from the imprint or a registry. Establish what the house *is* (category, country, district, segment).
2. **Company & identity.** From the about/company/press pages: founding year and history, ownership/group, design directors or notable collaborations, awards, manufacturing base, sustainability programme and certifications (LEED/EPD), distribution footprint, showrooms.
3. **Collections index.** Fetch the collections/products index. List every collection with its URL. Note product families/formats (large slabs, mosaic, decors, thicknesses, finishes) and any "look" taxonomy (wood / stone / concrete / metal).
4. **Per-collection pass.** Fetch each collection page at summary depth. Capture: look/material (from the page's own text), one-line character, colour/structure names, catalogue PDF, technical PDF, page URL. Correct any homepage mislabels.
5. **Distinctive services / strategic angle.** Identify what makes this house more than a catalogue — a bespoke-fabrication arm (Kronos's K-LAB), a signature technology, an architect programme, a hospitality/contract focus. Flag explicit relevance to our strategy ([[The Material Atelier]], the uplift engine, identity-brand status) where it exists.
6. **Reference projects.** List notable installations from their portfolio — especially anything in Greece or the Mediterranean premium/hospitality segment we target. Useful for inspiration and credibility.
7. **Write the two notes** (templates in the next section): the **supplier dossier** (`Supplier - <Name>.md`) and the **collections reference** (`<Name> — Collections Reference.md`). The supplier note carries the public profile + the labelled private-enrichment prompts; the reference note carries the per-collection detail with PDF links. **No afoideli column.**
8. **Defer the asset job.** Do NOT build the catalogue/asset-ingestion note as part of research. If Orfeas wants the binaries (catalogue/technical PDFs, photos) pulled into Drive later, that is a separate task — log a one-line deferred entry in [[Capture Backlog]] pointing at the PDF links already captured in the reference note.
9. **Wire backlinks.** Add the supplier to [[Supplier Master Index]] and its brands to [[Brand Master Index]]; link the conduit/rep note if one exists (e.g. Plus Interiors via [[Supplier - Fantini]]); cross-link any [[06_PROJECTS_AND_CASES]] cases that used the supplier.
10. **Folder discipline.** Everything lives under `Suppliers/<Name>/`. Create the folder first with `create_directory` — `move_file` won't make parents. Keep the supplier filename exactly `Supplier - <Name>.md` so short `[[wikilinks]]` resolve.

## The two output notes

### A. Supplier dossier — `Suppliers/<Name>/Supplier - <Name>.md`

Frontmatter: `type: supplier`, `supplier_name`, `country`, `category`, `representation_model`, `strategic_importance`, `status`, `created`, `updated`, `confidence`, `aliases`, `tags`. Body sections, in order:

- **What <Name> is to us** — the strategic frame. Claude drafts from public identity + Orfeas's one-liner; flag as `needs_check` for him to sharpen. (Identity-brand? Commercial volume brand? Aesthetic marker?)
- **Commercial profile** — a mix of public and private. Public, fill now: website, legal entity, address, VAT, showrooms, general lead-time reputation if stated. Private, leave as labelled prompts:
  > [!question] (your knowledge) Main contact / agency / conduit · payment terms · real discount ceiling · loading habits · packaging quirks · normal vs. special lead time · common mistakes on their proformas · relationship status & power geometry
- **Product range & collections** — public, summarised; detail lives in the reference note (link it). Include the look taxonomy and product families.
- **Distinctive service / strategic angle** — public (e.g. a K-LAB equivalent), with a note on strategic relevance.
- **Company, ownership & sustainability** — public: history, group, certifications, manufacturing.
- **Reference projects** — public.
- **Showrooms & distribution** — public.
- **The conduit / rep** — **private**, labelled prompt. If a rep note already exists (Plus Interiors), link it and carry the power-geometry warning pattern from the Kronos note.
- **Automation potential** — leave as `(to populate)` stubs; not a research deliverable.
- **Links** — doctrine, conduit, indexes.

> [!important] The enrichment contract
> Every private field is a visible, labelled `> [!question] (your knowledge)` callout — never a silent blank and never an invented value. The note should read as "here is everything public, and here are the exact questions only you can answer." That is what makes it ready for your specialised knowledge.

### B. Collections reference — `Suppliers/<Name>/<Name> — Collections Reference.md`

Frontmatter: `type: reference`, `parent: "[[Supplier - <Name>]]"`, `supplier`, `country`, `category`, `status`, `created`, `updated`, `confidence: confirmed`, `source: <collections index URL>`, `tags`. Body:

- Intro callout: what this is, depth (summary, not full SKU list), and that SKUs/sizes live in the PDFs and in real proforma/Kouvas data.
- One entry per collection: `### <Name> — *look*`, a 1–3 line character description with colour/structure names, then `Page:`, `Catalogue:`, `Technical:`. **No `On afoideli.gr:` line.**
- Group by indoor vs. outdoor/large-format where the house does.
- Notes & caveats: where looks were reclassified from slider labels; that sizes are representative not exhaustive; shared/technical-only PDFs.

## Output artifacts (definition of done)

- `Suppliers/<Name>/Supplier - <Name>.md` — public profile filled to Kronos depth; every private field a labelled enrichment prompt.
- `Suppliers/<Name>/<Name> — Collections Reference.md` — per-collection detail with PDF links, no cross-reference column.
- Backlinks updated: [[Supplier Master Index]], [[Brand Master Index]], rep/conduit note, relevant projects.
- (If requested) a single deferred line in [[Capture Backlog]] for the binary-asset ingestion — otherwise nothing.
- A session-log entry appended.

## Gotchas (carried from the Kronos pilot)

- **Homepage sliders mislabel looks** — classify from the collection's own page.
- **Brand names are search-polluted** — scope every web query with the ceramics/bath + country context; prefer the manufacturer's own site and registries over general search.
- **Generic collection names collide** ("Essence", "Materia" exist across many brands) — always attribute to the right manufacturer.
- **Cap fetch token limits** on collection/nav-heavy pages (~4–5k).
- **Mark confidence by source tier** — `confirmed` for the manufacturer's own statements and registries, `likely` for trade press / LinkedIn, `needs_check` for un-corroborated general search. Never launder a guess into a fact.

## Links

- Pilot output (the depth target) → [[Supplier - Kronos]] · [[Kronos — Collections Reference]]
- Parked cross-reference machinery (revival spec) → [[Automation Backlog]]
- Deferred asset pattern → [[Kronos — Catalogue & Asset Ingestion]] · [[Capture Backlog]]
- Indexes → [[Supplier Master Index]] · [[Brand Master Index]]
- Doctrine → [[Afoi Deli — Operating Doctrine]] · root → [[The Heart]]
