---
type: schema_contract
created: 2026-06-16
status: active
confidence: verified
aliases:
  - Materials Schema
  - Material Schema Contract
  - Materials Ingestion Contract
tags:
  - materials-vault
  - afoi-deli
  - schema
---

# Materials Schema

> [!important] This is the load-bearing note of the materials layer.
> It defines the **typed frontmatter** every `Material - <Name>` note carries, the **controlled vocabularies** both Obsidian and Postgres must enforce, and the **mapping to the Supabase `materials` table**. A Python worker reads *this* as the ingestion contract. Change a field here → change it everywhere; do not let a note invent a field this note doesn't list.

## What this governs

The materials layer is the **stable, controlled vocabulary** the whole [[Afoi Deli — Materials Intelligence|materials system]] points back to — every product SKU, quote line and project spec will reference a material. Because it is dual-purpose (a human-readable Obsidian note **and** a row the OS database ingests), it has to satisfy two masters at once:

1. **The vault** — frontmatter obeys [[CLAUDE|CLAUDE.md §3]] and [[Obsidian Usage Rules]]. Navigation is numbered folders + `[[wikilinks]]`, uncertainty is marked with `confidence`.
2. **The OS database** — Supabase Postgres, `org_id` on every table, dashboards as SQL views (see [[Database Master Schema]] for the precedence rule: **the stored contract is canonical; the `.md` annotates it**).

> [!note] Reconciliation with the source research prompt
> The deep-research brief proposed `verification_status: verified | asserted | open` and `tags: [materials-vault, afoi-deli]` as the trust + nav fields. **The vault overrides both:** uncertainty is the four-value `confidence` enum (CLAUDE.md §3 makes it exhaustive), and tags are *not* the navigation system. We keep one vocabulary in the notes (`confidence`) and document the DB-facing `verification_status` column as a **derived mapping** below — so Postgres still gets its enum without the vault carrying two competing trust fields (the exact dual-vocabulary the [[2026-06-16-vault-audit]] killed in [[Database Master Schema]]).

## `material_id` — the join key

> [!example] The single most important field
> `material_id` is a **stable, kebab-case slug** (e.g. `porcelain-stoneware`, `large-format-porcelain-slab`, `saphirkeramik`). It is the **primary key** of the `materials` table and the **join key** between the vault and the DB.
> - Lowercase, ASCII, hyphen-separated, derived from the English `title`.
> - **It never changes** once assigned — renaming the display title is fine, renaming the slug breaks every downstream join. Treat it like a database primary key, because it is one.
> - One slug = one material note = one DB row.

## Frontmatter field reference

Every `Material - <Name>` note carries these keys. `Base` = usable as an Obsidian Bases / Dataview facet.

| Key | Type | Controlled? | Base | → DB column | PG type | Null? |
|---|---|---|---|---|---|---|
| `title` | string | no | ✓ | `title_en` | `text` | no |
| `material_id` | string (kebab) | no | ✓ | `material_id` **PK** | `text` | no |
| `name_el` | string | no | ✓ | `name_el` | `text` | no |
| `aliases` | list<string> | no | ✓ | `aliases` | `text[]` | yes |
| `class` | string | **yes** | ✓ | `class` | `text` (enum) | no |
| `category` | list<string> | **yes** | ✓ | `category` | `text[]` (enum) | no |
| `iso_group` | string | **yes** | ✓ | `iso_group` | `text` (enum) | yes |
| `water_absorption_pct_max` | number | no | ✓ | `water_absorption_pct_max` | `numeric` | yes |
| `forming_method` | string | **yes** | ✓ | `forming_method` | `text` (enum) | yes |
| `pei_rating` | list<int> | no | ✓ | `pei_rating` | `int[]` | yes |
| `deep_abrasion_mm3_max` | number | no | ✓ | `deep_abrasion_mm3_max` | `numeric` | yes |
| `slip_din51130` | list<string> | **yes** | ✓ | `slip_din51130` | `text[]` (enum) | yes |
| `slip_din51097` | list<string> | **yes** | ✓ | `slip_din51097` | `text[]` (enum) | yes |
| `dcof_min` | number | no | ✓ | `dcof_min` | `numeric` | yes |
| `breaking_strength_nmm2_min` | number | no | ✓ | `breaking_strength_nmm2_min` | `numeric` | yes |
| `mohs` | number | no | ✓ | `mohs` | `numeric` | yes |
| `standards` | list<string> | no | ✓ | `standards` | `text[]` | yes |
| `frost_resistant` | boolean | no | ✓ | `frost_resistant` | `boolean` | yes |
| `thickness_mm` | list<number> | no | ✓ | `thickness_mm` | `numeric[]` | yes |
| `formats_mm` | list<string> | no | ✓ | `formats_mm` | `text[]` | yes |
| `finishes` | list<string> | **yes** | ✓ | `finishes` | `text[]` (enum) | yes |
| `applications` | list<string> | **yes** | ✓ | `applications` | `text[]` (enum) | yes |
| `key_suppliers` | list<wikilink> | no | ✓ | `key_suppliers` | `text[]` | yes |
| `proprietary_names` | list<string> | no | ✓ | `proprietary_names` | `text[]` | yes |
| `research_depth` | string | **yes** | ✓ | `research_depth` | `text` (enum) | no |
| `type` | string | no | — | *(not ingested — vault facet)* | — | — |
| `created` | date | no | — | `created_at` | `date` | no |
| `status` | string | **yes** | — | *(vault lifecycle — not ingested)* | — | — |
| `confidence` | string | **yes** | ✓ | → `verification_status` (mapped) | `text` (enum) | no |
| `sources` | list<url> | no | — | `sources` | `text[]` | yes |
| `tags` | list<string> | no | — | *(not ingested — descriptive only)* | — | — |

> [!info] DB-side additions the worker injects (not in frontmatter)
> `org_id` (every table carries it), `id` (surrogate uuid if needed beyond `material_id`), `verification_status` (derived from `confidence`, below), `updated_at`.

## Controlled vocabularies

Both the Base and the DB enforce these. Never emit a value outside the set; if a new value is genuinely needed, **add it here first**, then use it.

- **`class`** — `vitrified-ceramic` · `large-format-vitrified-ceramic` · `glazed-ceramic` · `glass-mosaic` · `sanitary-ceramic` · `engineered-sanitary-ceramic` · `solid-surface-composite` · `brass-alloy` · `stainless-steel` · `timber` · `safety-glass` · `mirror-glass` · `sintered-stone` · `engineered-quartz` · `natural-stone` · `panel-composite` · `heat-emitter-metal` · `technical-fabric` · `mixed`
- **`category`** (Afoi Deli product categories) — `tiles` · `sanitaryware` · `faucets` · `bathroom-furniture` · `mirrors` · `shower-enclosures` · `wellness` · `radiators` · `shading` · `kitchens` · `parquet`
- **`iso_group`** (tiles only; `N/A` otherwise) — `BIa` · `BIb` · `BIIa` · `BIIb` · `BIII` · `AIa` · `AIIa` · `AIIb` · `AIII` · `N/A`
- **`forming_method`** — `A` (extruded) · `B` (dry-pressed) · `N/A`
- **`slip_din51130`** (shod ramp) — `R9` · `R10` · `R11` · `R12` · `R13`
- **`slip_din51097`** (barefoot ramp) — `A` · `B` · `C`
- **`finishes`** — `matte` · `polished` · `lappato` · `structured` · `anti-slip` · `bush-hammered` · `satin` · `glossy` · `crackle` · `hand-decorated` · `brushed` · `oiled` · `lacquered` · `pvd` · `chrome` · `powder-coat`
- **`applications`** — `floor` · `wall` · `outdoor` · `facade` · `worktop` · `pool` · `splashback` · `furniture` · `basin` · `wc` · `bathtub` · `shower-tray` · `enclosure` · `mirror` · `radiator` · `sauna` · `steam-room` · `pergola`
- **`research_depth`** — `deep` · `medium` · `light`
- **`confidence`** (vault law, [[CLAUDE|CLAUDE.md §3]]) — `verified` · `likely` · `memory_seed` · `needs_check`
- **`status`** (vault lifecycle) — `active` · `draft` · `seed` · `idea` · `complete` · `backlog`

## The trust mapping — `confidence` → `verification_status`

The note carries `confidence` (vault). The worker derives the DB `verification_status` column on ingest:

| Vault `confidence` | DB `verification_status` | Meaning |
|---|---|---|
| `verified` | `verified` | Traced to a citable source (standards body / manufacturer TDS/EPD). |
| `likely` | `asserted` | Well-grounded but the supplier-specific or stock detail isn't pinned. |
| `needs_check` | `open` | An unresolved item — never silently upgraded; carries a reason. |
| `memory_seed` | `open` | Seeded from memory, not yet sourced. |

> The DB enum is therefore `verified | asserted | open`, exactly as the OS expects — produced by a deterministic mapping, not a second field maintained by hand.

## Body structure contract

Every material note follows the seed's proven section order (so the layer reads consistently and a parser can find sections):

1. **Snapshot** — `> [!example]` callout: class · AKA (incl. Greek) · category · ISO group · research depth · key suppliers.
2. **Composition & manufacture**
3. **Sub-types** — the distinctions clients actually ask about.
4. **Properties** — a table mirroring the frontmatter (human-readable form of the typed fields).
5. **Formats & finishes**
6. **Applications**
7. **Care**
8. **Suppliers** — the exact, verified Afoi Deli brands, each `[[wikilinked]]`, proprietary line names noted.
9. **Sources** — specific TDS/EPD/standard URLs the claims rest on.
10. **Links** + any **open items** (`> [!question]` / `needs_check`).

## Naming & location

- **Filename:** `Material - <English Name>` (the [[Vault Map|Entity-Name]] convention, like `Supplier - Kronos`). Link as `[[Material - Porcelain Stoneware|Porcelain Stoneware]]`.
- **Folder:** `07_PRODUCT_KNOWLEDGE/Materials/`.
- **`material_id`** is the kebab slug of the English name, and is the only identifier the DB joins on.

## How the worker ingests (future)

1. Read every `Material - *.md` under `07_PRODUCT_KNOWLEDGE/Materials/`.
2. Parse frontmatter; validate each controlled field against the vocabularies above (reject on unknown enum value).
3. Map `confidence → verification_status`; inject `org_id`, `updated_at`.
4. Upsert into `materials` on `material_id`.
5. `key_suppliers` wikilinks resolve to the `suppliers` dimension by brand name → closes the **product → supplier → material** graph.

## The collection tier (where line specifics live)

This contract governs the **class** tier. A material's `formats_mm` / `thickness_mm` / `finishes` here are **typical examples, not the authoritative catalogue** — the real, divergent per-line specifics (Kronos Pierre Vive's exact formats, finish wording, TDS values) live one tier down in [[Collection Schema]] (`Collection - <Supplier> <Name>` notes), which reference a material via `material_id`. Three tiers: **class → collection → SKU**. See [[Architecture Decision Records|ADR-0005]].

## Links

- Instance-tier contract → [[Collection Schema]]
- The index this contract serves → [[Afoi Deli — Materials Intelligence]]
- DB side → [[Database Master Schema]] · stack → [[Python Worker Map]] · [[Automation Masterplan]]
- Vault law → [[CLAUDE]] · [[Obsidian Usage Rules]] · [[RAG Knowledge Base Rules]]
- Product layer → [[Product Knowledge Map]] · [[Tile Knowledge Map]] · [[Bathroom Knowledge Map]] · [[Kitchen Knowledge Map]]
