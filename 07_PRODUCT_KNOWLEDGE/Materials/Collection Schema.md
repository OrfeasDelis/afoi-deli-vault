---
type: schema_contract
created: 2026-06-17
status: active
confidence: verified
aliases:
  - Collection Schema
  - Collection Ingestion Contract
tags:
  - materials-vault
  - afoi-deli
  - schema
---

# Collection Schema

> [!important] The instance-tier contract — sibling of [[Materials Schema]].
> A **material** is the stable class (porcelain stoneware). A **collection** is a specific supplier line made *from* that class (Kronos **Pierre Vive**, Florim **Authentic Luxe**) — with its own real formats, thicknesses, finish wording and TDS values, which differ line-to-line and are often **far more** than the class note carries. This note defines the typed frontmatter every `Collection - <Supplier> <Name>` note carries, and how it maps to a Supabase `collections` table.

## The three tiers

```
material  (class · ~22 · controlled vocabulary)     → [[Materials Schema]] · Material - <Name>
   ▲  material_id   (1 : N)
collection (instance · hundreds · born on ingestion) → THIS contract · Collection - <Supplier> <Name>
   ▲  collection_id (1 : N)
product / SKU (orderable · size × finish × colour)   → OS Postgres `products` (the legacy catalogue)
```

The vault owns the **material** and **collection** tiers (the dimension). The **SKU/product** tier lives in the OS database (the 386-product catalogue). Every quote line and project spec resolves **SKU → collection → material** — that join chain is the operating system's backbone.

> [!note] Why one shared schema, never per-supplier
> Forking the schema per supplier would destroy the one thing that makes this layer valuable: a **shared, queryable vocabulary** every line points back to. Inda's furniture and Antonio Lupi's furniture are *different collections of the same material classes* — same fields, different values. The differences live in the **values and the raw-wording fields**, not in a different schema.

## `collection_id` — the join key

> [!example] Stable, supplier-namespaced kebab slug
> `collection_id = <supplier-slug>-<collection-slug>` → `kronos-pierre-vive`, `florim-authentic-luxe`.
> - **Namespaced by supplier on purpose** — collection names collide across brands ("Essence", "Materia" exist at many houses; see the [[Supplier Research Workflow]] gotchas). The supplier prefix guarantees uniqueness.
> - **Never changes** once assigned (it's the DB primary key + the join from `products`). Rename the display title freely; never the slug.

## The raw + normalized rule (the finish-wording solution)

> [!important] Capture the brand's literal word AND a controlled value — both, always.
> Every house words surfaces and looks differently ("Naturale", "Soft", "Lappato", "Bocciardato" all describe surfaces that normalize to a handful of enums). So each relevant field is stored **twice**:
> - `*_raw` — the **verbatim** brand term, preserved exactly (a sales/▪Material Atelier asset — the brand's own language).
> - the **normalized** controlled-vocab value (the DB facet — queryable, comparable across brands).
>
> Example: `finishes_raw: ["Naturale", "Bocciardato"]` → `finishes: [matte, bush-hammered]`. Same for formats (`formats_raw: ["60x120"]` → parsed `formats_mm`). **Never discard the raw term**; never query on it.

## Frontmatter field reference

| Key | Type | Controlled? | → DB column | PG type | Null? |
|---|---|---|---|---|---|
| `title` | string | no | `title` | `text` | no |
| `collection_id` | string (kebab) | no | `collection_id` **PK** | `text` | no |
| `name_el` | string | no | `name_el` | `text` | yes |
| `aliases` | list<string> | no | `aliases` | `text[]` | yes |
| `supplier` | wikilink | no | `supplier_id` (resolved) | `text` **FK** | no |
| `material_id` | string | **yes** (must exist in `materials`) | `material_id` **FK** | `text` | no |
| `material` | wikilink | no | *(display; join is `material_id`)* | — | — |
| `look` | list<string> | **yes** | `look` | `text[]` (enum) | yes |
| `formats_raw` | list<string> | no | `formats_raw` | `text[]` | yes |
| `thickness_mm` | list<number> | no | `thickness_mm` | `numeric[]` | yes |
| `finishes_raw` | list<string> | no | `finishes_raw` | `text[]` | yes |
| `finishes` | list<string> | **yes** | `finishes` | `text[]` (enum) | yes |
| `rectified` | boolean | no | `rectified` | `boolean` | yes |
| `colors` | list<string> | no | `colors` | `text[]` | yes |
| `slip_din51130` | list<string> | **yes** | `slip_din51130` | `text[]` (enum) | yes |
| `slip_din51097` | list<string> | **yes** | `slip_din51097` | `text[]` (enum) | yes |
| `dcof_min` | number | no | `dcof_min` | `numeric` | yes |
| `pei_rating` | list<int> | no | `pei_rating` | `int[]` | yes |
| `water_absorption_pct_max` | number | no | `water_absorption_pct_max` | `numeric` | yes |
| `breaking_strength_nmm2_min` | number | no | `breaking_strength_nmm2_min` | `numeric` | yes |
| `frost_resistant` | boolean | no | `frost_resistant` | `boolean` | yes |
| `applications` | list<string> | **yes** | `applications` | `text[]` (enum) | yes |
| `aesthetic` | list<string> | **yes** | `aesthetic` | `text[]` (enum) | yes |
| `seo_keywords` | list<string> | no | `seo_keywords` | `text[]` | yes |
| `price_tier` | string | **yes** (internal) | `price_tier` | `text` (enum) | yes |
| `catalogue_url` | url | no | `catalogue_url` | `text` | yes |
| `technical_url` | url | no | `technical_url` | `text` | yes |
| `source_files` | list<string> | no | `source_files` | `text[]` | yes |
| `research_depth` | string | **yes** | `research_depth` | `text` (enum) | no |
| `type` | string | no | *(vault facet)* | — | — |
| `created` | date | no | `created_at` | `date` | no |
| `status` | string | **yes** | *(vault lifecycle)* | — | — |
| `confidence` | string | **yes** | → `verification_status` (mapped, see [[Materials Schema]]) | `text` (enum) | no |
| `sources` | list<url/string> | no | `sources` | `text[]` | yes |

> Reused vocabularies (`finishes`, `applications`, `slip_*`, `research_depth`, `confidence`, `status`) are the **same enums** defined in [[Materials Schema]] — one set, enforced in both tiers. New ones below.
> - **`look`** — `wood` · `stone` · `marble` · `concrete` · `metal` · `terrazzo` · `resin` · `solid-colour` · `fabric` · `decor` · `mosaic`
> - **`aesthetic`** — `mineral` · `raw` · `refined` · `warm` · `cool` · `natural` · `organic` · `tactile` · `weathered` · `brutalist` · `classic` · `contemporary` · `minimal` · `dramatic` · `serene` · `luxe` · `industrial` · `mediterranean` · `nordic` · `monastic` · `earthy` · `timeless` · `bold` · `soft` *(extensible — add deliberately, like the other vocabs)*
> - **`price_tier`** (internal) — `entry` · `mid` · `premium` · `icon` *(usually `needs_check` until you set it)*

## Per-finish / per-format detail → the note body

Flat frontmatter holds the **union** (every slip rating the line offers, every finish). The **per-finish breakdown** (where R-rating / DCOF / format availability vary *by finish*) lives in a **Properties matrix table in the body** — e.g. finish × {slip, DCOF, formats}. For the DB this becomes a child table `collection_finishes (collection_id, finish_raw, finish, slip_din51130, dcof, …)`; the worker can derive it from the body matrix later. Keep the contract pragmatic: **frontmatter = collection-level typed union; body = the matrices.**

## Editorial cluster — aesthetics, mood, SEO (content's half of the layer)

The materials layer isn't only operational — it feeds the content/SEO engine ([[SEO Topic Map]], `09_WEBSITE_MARKETING_AND_CONTENT`), Instagram/meta copy, and The Material Atelier. Same **raw + normalized** logic, applied to *feel*:

- **`aesthetic`** (controlled, queryable) — mood/style tags, so a campaign can pull "every `mediterranean` + `warm` stone-look line" in one filter.
- **`seo_keywords`** (free) — search/meta phrases for articles, meta descriptions, alt text.
- **Body — "Aesthetic, mood & narrative"** — the design story / philosophy in prose, drawn from the catalogue's **inspiration pages** (a porcelain catalogue's front matter is pure editorial gold that's otherwise lost). This is *generative seed material* an article or caption is drafted from — not a queryable field. Keep the brand's own evocative wording (the raw side) and our positioning voice on top.
- **Body — a `> [!tip] Content & SEO` callout** — the ready handoff: keywords + 2–3 angle hooks + the settings it photographs into (spa, boutique-hotel lobby, Mediterranean villa).

> [!note] Authorship line ([[CLAUDE|CLAUDE.md §6]])
> The typed tags + factual narrative are Claude's to maintain. The *positioning voice* — how we'd sell this line to an architect — stays Orfeas's: Claude drafts, he sharpens.

## Born on ingestion (not pre-stubbed)

> [!warning] A collection note exists only when there's real content for it.
> Created the moment you **feed a source** (catalogue/TDS) or it's **used in a project** — never pre-generated as an empty stub. Until then a collection is just a **roster entry** in `<Supplier> — Collections Reference`, which is now the **index/checklist** (every collection that exists, marked ingested ✅ / not-yet ⬚), not the home of the specs. This is what keeps the granular per-collection model from drowning the vault in empty notes. (See [[Session 2026-06-17]] / [[Architecture Decision Records|ADR-0005]].)

## Naming & location

- **Filename:** `Collection - <Supplier> <Name>.md` (supplier-namespaced, like the slug). Link `[[Collection - Kronos Pierre Vive|Pierre Vive]]`.
- **Folder:** `04_SUPPLIERS_AND_BRANDS/Suppliers/<Supplier>/Collections/`.
- **Links up:** `[[Material - <Class>]]` (+ `material_id`) and `[[Supplier - <Name>]]`. **Links down from:** the supplier's Collections Reference roster.

## How the worker ingests (future)

1. Read every `Collection - *.md` under each supplier's `Collections/`.
2. Validate `material_id` exists in `materials` (reject orphans); validate controlled fields against the shared enums.
3. Map `confidence → verification_status`; inject `org_id`, `updated_at`.
4. Upsert into `collections` on `collection_id`; resolve `supplier` → `supplier_id`.
5. Optional: parse the body matrix into `collection_finishes`. `products` (SKUs) join up via `collection_id`.

## Links

- Class-tier contract → [[Materials Schema]] · class notes → [[Afoi Deli — Materials Intelligence]]
- How collections get built/fed → [[Materials Research Workflow]] · supplier dossiers → [[Supplier Research Workflow]]
- DB side → [[Database Master Schema]] · [[Python Worker Map]]
- Decision record → [[Architecture Decision Records|ADR-0005]]
