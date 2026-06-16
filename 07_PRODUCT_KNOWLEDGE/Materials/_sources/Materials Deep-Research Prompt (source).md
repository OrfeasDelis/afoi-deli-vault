# Deep Research Prompt — Afoi Deli Materials Knowledge Layer

> Paste everything below the line into a fresh Opus 4.8 conversation with **deep research enabled**, and attach `Afoi_Deli___Materials_Intelligence.md` to that message.
> Bracketed `[[ ... ]]` items near the top marked **DECIDE** are the only knobs you may want to set before running.

---

## ROLE & MISSION

You are a materials scientist and information architect embedded with **Afoi Deli Floor + Bath**, a second-generation Athens tile-and-bath distributor (founded 1986, ~70 European manufacturers weighted to Italian premium brands). I am giving you an attached draft, `Afoi_Deli___Materials_Intelligence.md`. Your mission is to turn that draft into a **verified, production-grade materials knowledge layer** — a set of Obsidian notes that become the canonical material vocabulary inside the **Afoi Deli OS** (a Supabase/Postgres + Python worker + Next.js operating system replacing the legacy Excel/Gmail workflow).

The output is not an essay. It is **infrastructure**: atomic, typed, cross-linked notes plus a schema contract, designed so that (a) Obsidian can query them as a Base, and (b) the OS database can ingest them into a `materials` dimension that every product SKU, quote line, and project spec references. Materials are the **stable, controlled vocabulary** the whole system points back to.

## CONTEXT YOU MUST HOLD

- **The business:** Two showrooms (Peristeri operational flagship, Kolonaki premium atelier). A parallel B2B brand, *The Material Atelier*, sells material literacy to architects and designers — so the technical precision here is also a sales asset, not just internal plumbing.
- **The OS:** Postgres with `org_id` on every table, dashboards as SQL views, a quote tool already validated against real data (106 suppliers, 386 products, 156 clients, 450 order lines). The materials layer must join cleanly to this.
- **The vault:** Obsidian, Obsidian Flavored Markdown, wikilink graph, Bases for queries. The notes you produce live here and are the human-readable source of truth; the DB ingests from them.
- **Market specifics that change which specs matter:** Athens — hard water (limescale/etch on polished and glass surfaces is a real spec driver), mild but real winter frost (frost resistance matters for exterior/façade/outdoor paver lines), strong demand for the seamless/large-format/full-body architectural look.

## YOUR SINGLE SOURCE SEED

The attached file is a strong draft, **not** a blank brief. **Preserve its strengths and build on them — do not regenerate from scratch.** Specifically:

- The **`## Reading the specs` primer** (ISO 13006 / EN 14411 two-axis classification, ISO 10545 test-method series, PEI vs deep abrasion, the three slip systems DIN 51130 / DIN 51097 / ANSI A326.3 DCOF, breaking strength, Mohs) is high quality. Keep it as the shared standards reference and refine only where you can verify an improvement.
- The **`Category → material map`** table and the **`APPENDIX — Brand → Material index`** (every Afoi Deli brand grouped by material, flagged ✅ well-documented / ⚠️ verify) are your authoritative supplier roster. **Treat the appendix's brand list as the canonical set of suppliers to specify against — do not invent or omit brands.**
- Every **`> [!question] To verify`** callout and every **⚠️** flag in the appendix is an **open work item you must resolve** (verify, correct, or mark as genuinely unverifiable with reason).

## THE FOUR JOBS (in order)

**1. Read and deeply understand.** Internalize every material class, the spec primer, the structure, and the verification posture. Build a mental model of how the eleven product categories decompose into ~22 material classes.

**2. Specify against my exact suppliers.** For each material, go to the **actual technical documentation of the Afoi Deli brands that supply it** — manufacturer technical data sheets (TDS), EPDs/Declare sheets, catalogues, declaration-of-performance documents. Confirm or correct each brand → material mapping. Resolve every `To verify` and ⚠️. Pay special attention to **proprietary / trademarked material names**, which are the highest-value specificity points; verify what each actually is, who owns it, and which note it belongs under:
   - Laufen **SaphirKeramik** · Cielo **Ceramilux** · Antonio Lupi **Cristalplant / Flumood** · Cotto d'Este **Kerlite** · Lea **Slimtech** · Laminam-class slabs · Bisazza **smalti / aventurine (Le Gemme) / Oro gold-leaf / Gloss / Glow / Opera** · Geberit (flush/installation systems — **not** a ceramic body; classify correctly) · QuadroDesign (likely stainless tapware — verify).
   - Where a brand's offer spans materials (e.g. Provenza wood-look **porcelain** that is *not* timber; Cesi furniture vs accessories), disambiguate explicitly.

**3. Pinpoint specific properties / attributes.** For each material, extract the **precise, measurable** technical attributes and render them in two forms: (a) a human-readable **properties table** in the note body, and (b) **typed frontmatter fields** (the queryable/ingestable form). Attributes to capture where applicable: ISO group, water absorption %, forming method, PEI class, deep-abrasion mm³, slip ratings (all three systems), DCOF, breaking strength / modulus of rupture, Mohs, relevant ISO 10545 / EN / DIN / ANSI / NSF standards, frost resistance, thickness ranges, formats, finishes, applications, care/maintenance notes. **Never fabricate a number.** If a value is range-typical rather than verified for a specific stocked line, say so.

**4. Build the knowledge infrastructure.** Produce the deliverables below, formatted for direct drop-in to the Obsidian vault and ready for DB ingestion.

## DELIVERABLES

Produce all of the following. Where deep research can't fully complete a material, deliver it at the depth you reached and flag the gap — do not silently drop it.

**A — Canonical Materials MOC** (revise the attached file). Keep it as the *index and bridge*: the `Category → material map`, the spec primer, and a now-**verified** Brand → Material appendix with updated confidence flags. Every material name links to its atomic note via `[[material_id|Display Name]]`.

**B — Atomic material notes** (one note per material, ~22 notes). Each note carries the typed frontmatter schema (Section: *Schema Contract*) plus this body structure, reusing the attached file's proven section pattern:
   - **Snapshot** callout (class · AKA incl. Greek · category · group · research depth · key suppliers)
   - **Composition & manufacture**
   - **Sub-types** (the distinctions clients actually ask about)
   - **Properties** — a clean attribute table mirroring the frontmatter
   - **Formats & finishes**
   - **Applications**
   - **Care**
   - **Suppliers** — the exact, verified Afoi Deli brands supplying this material, each `[[wikilinked]]`, with proprietary line names noted
   - **Sources** — specific TDS/EPD/standard URLs the claims rest on

**C — Schema Contract note** (`Materials Schema`). This is the load-bearing deliverable. Document **every frontmatter field**: its key, data type, whether it's a controlled vocabulary (and the allowed values), Obsidian-Base usability, and **how it maps to a Supabase `materials` table** (column name, Postgres type, nullability). Define `material_id` as a **stable kebab-case slug that is the primary join key** between the vault and the DB. State the controlled vocabularies explicitly (e.g. `class`, `iso_group`, `forming_method`, `application`, `finish`, `verification_status`) so both the Base and the DB enforce the same enums. Treat this note as the ingestion contract a Python worker would read.

**D — Supplier notes** (one per brand on the roster, concise). Each links to the material(s) that brand supplies and records its **proprietary material names**, country, segment (premium/mid), and Afoi Deli category. These form the brand layer that links back to materials, closing the graph (product → supplier → material).

**E — Obsidian Base definition** (`.base` YAML). At least one Base view that surfaces materials filterable by `class`, `category`, `iso_group`, `application`, and `key_suppliers`, with sensible columns (water absorption, PEI, slip, frost, thickness). Provide the raw `.base` file content.

**F — Verification ledger** (one table). Every claim you verified, corrected, or left open: `material | claim | status (verified / corrected / open) | source | note`. This is my audit trail for promoting the layer to canonical.

## SCHEMA CONTRACT — TARGET STARTING SHAPE

Finalize and normalize this; document it fully in Deliverable C. Starting target (adjust field names only with good reason):

```yaml
---
title: Porcelain Stoneware
material_id: porcelain-stoneware          # STABLE slug — primary DB join key
name_el: Γκρες Πορσελάνη                   # Greek canonical name
aliases: [Gres Porcellanato, Porcelain Tile, Πορσελάνη]
class: vitrified-ceramic                   # controlled vocab
category: [tiles]                          # maps to Afoi Deli product categories
iso_group: BIa                             # controlled vocab
water_absorption_pct_max: 0.5
forming_method: B                          # A | B
pei_rating: [3, 4, 5]                      # null where N/A (use deep abrasion)
deep_abrasion_mm3_max: 150                 # full-body only
slip_din51130: [R10, R11, R12]
slip_din51097: [A, B, C]
dcof_min: 0.42
breaking_strength_nmm2_min: 35
mohs: 7
standards: [ISO 13006, EN 14411, ISO 10545-3, ISO 10545-7]
frost_resistant: true
thickness_mm: [8.5, 9, 10, 20]
formats_mm: ["60x60", "60x120", "30x60"]
finishes: [matte, polished, structured, anti-slip]   # controlled vocab
applications: [floor, wall, outdoor, facade, worktop, pool]  # controlled vocab
key_suppliers: ["[[Atlas Concorde]]", "[[Mutina]]", "[[Florim]]"]
proprietary_names: []
research_depth: deep                       # deep | medium | light
verification_status: verified              # verified | asserted | open
sources: [https://..., https://...]
type: material
tags: [materials-vault, afoi-deli]
---
```

## BILINGUAL RULE (Greek + English, from day one)

The OS is bilingual by binding rule. Every material and supplier note must carry a Greek canonical name (`name_el`) and include the Greek term in `aliases`. Key spec vocabulary should appear in both languages where a Greek trade term exists. Body prose stays in English; names and key terms are bilingual.

## QUALITY & VERIFICATION BAR

- **Sourced, not asserted.** Composition / standards / performance claims must trace to a citable source (standards body, manufacturer TDS/EPD, reputable technical reference). Prefer the **supplier's own** documentation over third-party summaries.
- **Confidence is explicit.** Use `verification_status: verified | asserted | open` per note, and keep the ✅ / ⚠️ flags in the appendix honest. An unresolved item stays `open` with a reason — never quietly upgraded.
- **Never invent numbers, brands, or proprietary names.** If a spec varies by line and you can't pin it, give the range and label it typical-not-confirmed.
- **Distinguish material form from chemistry.** (E.g. large-format slab shares porcelain chemistry but is its own engineered form; keep them as separate linked notes, as the seed does.)

## OBSIDIAN FORMATTING RULES

- Obsidian Flavored Markdown. Use callouts (`> [!example]` snapshot, `> [!question]` open items, `> [!info]` standards), wikilinks `[[material_id|Display]]`, and typed YAML frontmatter (properties).
- Cross-reference materials and suppliers by wikilink so the graph is real.
- Deliver each note as a clearly labelled, copy-pasteable block with its intended filename, so I can drop them straight into the vault.

## HOW TO BEGIN

1. First read the attached file end to end and the live afoideli.gr brand/product pages.
2. Then post a short **plan**: your material list, the supplier-verification queue (which brands' TDS you'll hit), and the finalized schema field list — before mass-producing notes.
3. Then execute: schema contract → atomic notes (deepest/highest-traffic materials first: porcelain stoneware, large-format slab, glass mosaic, sanitary ceramic, SaphirKeramik) → supplier notes → Base → revised MOC → verification ledger.
4. Close with the verification ledger and a list of anything that needs my confirmation against current physical stock.
