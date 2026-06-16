---
name: materials-research
description: Turn a material class into a verified, production-grade atomic note inside the Afoi Deli materials layer — typed frontmatter + sourced specs + the exact Afoi Deli supplier brands that make it. Use when Orfeas says "build the <material> note", "do the materials treatment for <material>", "research <material>", "continue the materials layer", or names a material class to document (porcelain stoneware, glass mosaic, SaphirKeramik, solid surface, brass & finishes, sintered stone…). Produces a `Material - <Name>.md` note in 07_PRODUCT_KNOWLEDGE/Materials/, governed by [[Materials Schema]], indexed by [[Afoi Deli — Materials Intelligence]]. Verifies brand→material mappings against manufacturer TDS/EPD; never fabricates a number.
type: workflow
status: active
created: 2026-06-16
updated: 2026-06-16
aliases:
  - Materials Research Workflow
  - materials-research
tags:
  - workflow
  - skill
  - materials
  - research
  - ingestion
---

# Materials Research Workflow

> [!info] What this is
> The repeatable pipeline that turns a **material class** into a verified atomic note in the materials layer — to the depth of the [[Material - Porcelain Stoneware]] pilot. It is the materials-side sibling of [[Supplier Research Workflow]]: where that documents a *house*, this documents a *material*, and the two meet at `key_suppliers` (closing the **product → supplier → material** graph).
>
> This note is written as a **SKILL.md**. To make it a callable skill, copy it to `<vault>/.claude/skills/materials-research/SKILL.md` keeping the YAML above. It also stands alone as the human runbook.
>
> **Trigger phrases:** "build the <material> note", "continue the materials layer", "do the materials treatment for <material>", "research <material>", "next materials batch".

> [!note] Provenance — the raw inputs, preserved
> This workflow was distilled from a deep-research brief + a strong seed draft, both kept verbatim (immutable) in `Materials/_sources/`:
> - **`Materials Deep-Research Prompt (source).md`** — the original brief (ROLE/MISSION, the four jobs, deliverables A–F, the target schema shape).
> - **`Materials Intelligence — Seed Draft (source).md`** — the 16-section seed with the `Reading the specs` primer and the Brand → Material appendix.
>
> The seed became the live index [[Afoi Deli — Materials Intelligence]]. **Re-run this workflow, not the raw prompt** — the prompt was written for a blank Opus chat; this note carries the vault reconciliations the prompt doesn't know about (below). The raw files are there if you ever want to re-derive from scratch.

---

## The principle behind the depth

The same public/verification spine as the supplier workflow, pointed at materials:

- **Sourced, not asserted.** Every composition / standard / performance claim traces to a citable source — a standards body (ISO/EN/DIN/ANSI/NSF) or, preferably, the **supplier's own TDS / EPD / Declaration of Performance**. Manufacturer documentation beats third-party summaries.
- **The brand→material mapping is the part to scrutinise.** The material science is stable; *which Afoi Deli house actually supplies this material, under which proprietary line name* is where the value and the error-risk both live. Confirm or correct every mapping; resolve every `To verify` and ⚠️ from the seed appendix.
- **Proprietary / trademarked names are the gold.** SaphirKeramik (Laufen) · Ceramilux (Cielo) · Cristalplant + Flumood (Antonio Lupi) · Kerlite (Cotto d'Este) · Slimtech (Lea) · Bisazza smalti / Le Gemme / Oro / Gloss / Glow / Opera · Geberit (flush/installation systems — **not** a ceramic body; classify correctly) · QuadroDesign (verify stainless steel). Verify what each *actually is*, who owns it, and which material note it belongs under.
- **Never fabricate a number, brand, or proprietary name.** If a spec varies by line and you can't pin it, give the **range and label it typical-not-confirmed**. Stock-specific questions only Orfeas can answer stay `needs_check` — never silently upgraded.
- **Distinguish material *form* from *chemistry*.** Large-format slab shares porcelain chemistry but is its own engineered form → its own linked note. Same for sintered stone vs porcelain.

## Vault reconciliations — how this differs from the raw prompt

> [!important] These overrides are non-negotiable — they are why we re-run *this*, not the raw brief.
> | The raw prompt said | The vault requires | Why |
> |---|---|---|
> | `verification_status: verified \| asserted \| open` | `confidence: verified \| likely \| memory_seed \| needs_check` | [[CLAUDE\|CLAUDE.md §3]] makes the `confidence` enum exhaustive. The DB still gets `verification_status` via the **deterministic mapping** in [[Materials Schema]] — one trust field in the note, not two. |
> | `tags: [materials-vault, afoi-deli]` as nav | Tags are **light/descriptive only** | Navigation is numbered folders + `[[wikilinks]]`, not tags. |
> | (omitted) | Add `created` + `status` (vault-required frontmatter) | Every note carries them; `status` from `active\|draft\|seed\|idea\|complete\|backlog`. |
> | Bare `[[Porcelain Stoneware]]` | Filename `Material - <Name>`, link `[[Material - <Name>\|<Name>]]` | The [[Vault Map\|Entity-Name]] convention (like `Supplier - Kronos`). `material_id` stays the bare kebab slug. |
> | Deliverable E: `.base` only | **Dataview now + `.base` ready** | Dataview is installed and used today; Bases is enabled later. Ship both. |
> Everything else in the prompt (the spec primer, the ~22-material decomposition, the deepest-first order, the verification ledger) is kept intact.

## Inputs the operator provides

- The material to build (e.g. "glass mosaic"), or "next batch" → take the next deepest un-built material from the index.
- Optional emphasis (a client question this should answer, a brand to prioritise).

## Source hierarchy (best-first)

1. **Standards bodies** — ISO 13006 / EN 14411 (classification), ISO 10545 series (test methods), DIN 51130 / 51097 + ANSI A326.3 (slip), EN 12150 (safety glass), NSF/ANSI 61 & 372 (low-lead). `verified` for what they define.
2. **The supplier's own TDS / EPD / DoP** — the manufacturer's technical data sheet, Environmental Product Declaration, Declaration of Performance, catalogue. Authoritative for that line's real numbers and for the proprietary-name truth. `verified`.
3. **Manufacturer technology pages** — e.g. RAK tile-technology, Laufen SaphirKeramik, Cotto d'Este Kerlite, Bisazza technical pages. `verified`/`likely`.
4. **Reputable technical references** — Confindustria Ceramica, peer-reviewed material studies, Archiproducts material taxonomy. `likely`.
5. **General web** — last; scope every query with the ceramics/bath context (brand names collide). `needs_check` unless corroborated.

## The deliverables (A–F → vault form)

- **A · Index/MOC** — [[Afoi Deli — Materials Intelligence]]: keep the Category→material map, the spec primer, and the Brand→Material appendix; repoint each material to its atomic note as it's built; keep the appendix's ✅/⚠️ flags honest.
- **B · Atomic material notes** — `Material - <Name>.md`, one per material (~20–22), the body contract from [[Materials Schema]].
- **C · Schema contract** — [[Materials Schema]] (already built; update if a field/vocab changes).
- **D · Supplier links** — **enrich the existing dossier**, don't duplicate. 13 already exist (Kronos, Cielo, Mutina, Fantini, Scavolini, Atlas Concorde, Florim, Emilgroup, Sant'Agostino, ABK, 41zero42, Antonio Lupi, Fima Carlo Frattini). Add the material wikilink + proprietary line names to the dossier; for houses with no note yet, leave the intended-graph link and add to [[Supplier Master Index]]. New dossiers run via [[Supplier Research Workflow]].
- **E · Query layer** — a Dataview "Materials Index" note that works today, **plus** a `.base` YAML file ready to enable. Filterable by `class`, `category`, `iso_group`, `application`, `key_suppliers`; columns: water absorption, PEI, slip, frost, thickness.
- **F · Verification ledger** — one table: `material | claim | status (verified/corrected/open) | source | note`. The audit trail for promoting the layer to canonical.

## Full procedure (run order)

1. **Read the index + primer.** Open [[Afoi Deli — Materials Intelligence]] and the `Reading the specs` primer. Internalise the seed section for the target material and its `To verify` callout.
2. **Verify against suppliers.** Hit the manufacturer TDS/EPD for the Afoi Deli brands that supply this material. Confirm/correct each brand→material mapping. Resolve proprietary names (what it is, who owns it, which note it belongs under). Disambiguate brands whose offer spans materials (Provenza wood-look *porcelain* ≠ timber; Cesi furniture vs accessories).
3. **Pinpoint properties.** Extract precise, measurable attributes — ISO group, water absorption %, forming method, PEI / deep-abrasion mm³, the three slip systems, DCOF, breaking strength, Mohs, relevant standards, frost resistance, thicknesses, formats, finishes, applications, care. Render twice: the **typed frontmatter** + the human **Properties table**. Range-label anything not line-confirmed.
4. **Write the atomic note** — `07_PRODUCT_KNOWLEDGE/Materials/Material - <Name>.md`, frontmatter per [[Materials Schema]], body in the contract order (Snapshot → Composition → Sub-types → Properties → Formats & finishes → Applications → Care → Suppliers → Sources → Links + open items). Bilingual: `name_el` + Greek in `aliases` + key Greek trade terms inline.
5. **Wire the graph.** `key_suppliers` wikilinks to existing dossiers; add the material link back into each supplier note's range section; repoint the index entry to the atomic note; **earn an inbound link** (index/MOC or the relevant Knowledge Map) the same session — [[CLAUDE\|CLAUDE.md §3 inbound-link rule]].
6. **Log the ledger rows** for every claim verified/corrected/left open.
7. **Append a session-log entry**; if a `To verify` was resolved, flip the seed appendix flag ✅.

> [!tip] Fetch discipline (carried from the Kronos/supplier pilot)
> - Cap fetch token limits on nav-heavy manufacturer pages (~4–5k); the shared menu eats the budget.
> - Classify a material/finish from the **product/TDS page's own text**, never a homepage slider.
> - Capture **PDF/TDS links, don't download** — binary-asset ingestion is a separate deferred job.
> - Scope every web query with ceramics/bath + country context; brand names are search-polluted.

## Definition of done (per material)

- `Material - <Name>.md` written with full typed frontmatter + sourced Properties table + verified `key_suppliers`.
- Every `To verify` / ⚠️ for that material **resolved, corrected, or left `needs_check` with a reason**.
- Index entry repointed; at least one inbound link earned; supplier dossiers cross-linked.
- Ledger rows added; session-log entry appended.

## Gotchas

- **Geberit is not a ceramic body** — flush/cistern/installation systems. Classify correctly.
- **Wood-look porcelain (Provenza) is porcelain, not timber** — keep separate from [[Material - Wood Flooring & Parquet|parquet]].
- **Slip systems don't convert** — DIN 51130 (R), DIN 51097 (A/B/C), ANSI DCOF are three parallel scales; report all that apply, never interconvert.
- **Full-body has no PEI** — it uses deep abrasion (ISO 10545-6). Don't force a PEI number onto it.
- **Hard-water Athens** is a real spec driver — limescale/etch on polished/glass surfaces; frost resistance for exterior lines. Surface it in Care/Applications where relevant.

## Links

- Depth target (pilot) → [[Material - Porcelain Stoneware]]
- Field/ingestion contract → [[Materials Schema]]
- The index this feeds → [[Afoi Deli — Materials Intelligence]]
- Raw inputs (immutable) → `Materials/_sources/`
- Sibling workflow → [[Supplier Research Workflow]] · indexes → [[Supplier Master Index]] · [[Brand Master Index]]
- Product layer → [[Product Knowledge Map]] · [[Tile Knowledge Map]] · [[Bathroom Knowledge Map]] · [[Kitchen Knowledge Map]]
- Doctrine → [[Afoi Deli — Operating Doctrine]] · root → [[The Heart]]
