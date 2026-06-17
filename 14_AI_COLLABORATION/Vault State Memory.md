---
type: memory_state
created: 2026-06-07
updated: 2026-06-17
status: active
confidence: verified
owner: Orfeas Delis
---

# Vault State Memory

> **Single source of truth for "where we are."**
> Read this AFTER [[The Heart]], at the start of every session; UPDATE it at the end.
> See [[Session Protocol]].

## 0. Read The Heart first

Before this file, read [[The Heart]] — the foundational note above the structure. It sets the voice, values, and lineage every session inherits. Business strategy descends from it via [[Afoi Deli — Operating Doctrine]].

## 1. What this vault is

Unified operating + knowledge system for **both** Afoi Deli Floor + Bath (ΑΦΟΙ ΔΕΛΗ Ε.Ε., Athens, founded 1986, afoideli.gr) **and Orfeas Delis as a person**. Business and personal are one fabric.

5-layer model: **Knowledge (Obsidian) → Data (Supabase Postgres) → Automation (Python worker) → Interface (future webapp) → AI Agent.** Core principle: *Obsidian is the memory; the agent is never the source of truth.* **No n8n** — settled stack is Supabase + Python worker, solo build via Claude Code.

## 2. Current structure (high level)

> [!note] The canonical folder index is [[Vault Map]].
> To kill the drift the [[2026-06-16-vault-audit|2026-06-16 audit]] caught (this section used to restate a divergent copy that named phantom folders), the taxonomy is now **maintained in one place — [[Vault Map]] —** and linked from here, not duplicated. **Audit P0-1 is reconciled:** `15_PERSONAL_LIFE` + `16_IDEAS_AND_VISION` are now real seed wings ([[Personal Life — Home]], [[Ideas and Vision — Home]]); `18_KNOWLEDGE` was deferred (see [[Studies and Subjects]]); `17_JOURNAL` is live; `_meta/` holds the audit reports.

In short: one unified vault — business folders `00`–`11`, the personal/operating wing `12`–`17`, system folders `97`–`99`, and `_meta/`. **Root:** [[The Heart]] — the foundational note, above structure. The full table with purposes lives in [[Vault Map]].

## 3. Conventions to always honor

- YAML frontmatter on every note: `type`, `created`, `status`, plus `confidence` where facts are involved.
- Confidence tags: `verified | likely | memory_seed | needs_check`.
- Naming: `Entity - Name`, numbered folders, `[[wikilinks]]`.
- One note = one purpose. Link aggressively. Mark uncertainty.
- **Human approval** required for: sending emails, changing order status, changing prices, approving proformas, notifying clients of delays, changing delivery promises, updating financial records.
- **Personal half:** read/reason freely; [[Journal]] and wellness are author-by-invitation — don't write into them unprompted. See [[CLAUDE]] §5.

## 4. Infrastructure state

- **Git:** repo on branch `master`. Identity: Orfeas Delis. Private repo `afoi-deli-vault` under `OrfeasDelis`.
- **Obsidian plugins:** Dataview, Templater, Obsidian Git, Minimal/Style Settings — installed.
- **Afoi Deli OS build:** Supabase Postgres + Python worker, bilingual, solo via Claude Code. Builder's Manual exists (R0–R3 roadmap). n8n removed from vault doctrine 2026-06-14.
- **PDF ingestion — UNBLOCKED (2026-06-17b).** This machine now has **real Python 3.12** (not the MS Store stub) + **PyMuPDF (fitz) 1.26.7**, which rasterizes PDF pages to PNGs the Read tool views; `pdftotext` (Xpdf) covers the text layer. **poppler / `pdftoppm` is NOT needed** — PyMuPDF replaces it. Proven end-to-end on the Pierre Vive catalogue. All future supplier catalogue/TDS ingestion uses this path. *(Supersedes the earlier "install Python + poppler" tooling gap.)*

## 5. Active threads / in progress

- [ ] **Materials knowledge layer — Batch 1 shipped, PAUSED for Orfeas's steer (2026-06-16d).** Built [[Materials Schema]] (typed-frontmatter ingestion contract; `confidence→verification_status` mapping) + [[Material - Porcelain Stoneware]] (deep, verified, 5 sources); filed the index [[Afoi Deli — Materials Intelligence]]; made it re-runnable via [[Materials Research Workflow]] (SKILL.md sibling of [[Supplier Research Workflow]]) + archived the raw prompt/seed in `07_PRODUCT_KNOWLEDGE/Materials/_sources/`. **CHECK FIRST next session** ([[Session 2026-06-16d]]): (1) approve the Schema+Porcelain pattern; (2) batch size; (3) the ~22 split (Countertop→sintered/quartz/natural, +stainless note off Brass). Next deep batch: Large-Format Slab → Glass Mosaic → Sanitary Ceramic → SaphirKeramik. Still to build: Dataview "Materials Index" + `.base`, verification ledger, supplier cross-links, per-material migration out of the MOC. **Extended 2026-06-17 → three tiers ([[Architecture Decision Records|ADR-0005]]):** added [[Collection Schema]] (instance tier — real per-line specifics, born-on-ingestion, raw+normalized capture) + the [[Materials Research Workflow]] specifics clause + ingestion modes (URL / fed PDF / future Drive feeder). Editorial cluster added to [[Collection Schema]] (`aesthetic`/mood/`seo_keywords` → feeds [[SEO Topic Map]] / content engine). **Pierre Vive pilot — SHIPPED + VERIFIED (2026-06-17b, [[Session 2026-06-17b]]).** PDF blocker cleared (real Python 3.12 + PyMuPDF; **poppler not needed**, §4). Built the vault's **first collection note** — [[Collection - Kronos Pierre Vive]] (born-on-ingestion; [[Collection Schema]] validated end-to-end), catalogue archived in `Kronos/_sources/`, roster reframed to ✅/⬚, ran a 3-lens adversarial verification and fixed every finding. **Contract evolved:** added a `graphic_versions` field to [[Collection Schema]] (Noble/Ancienne face axis). Still open: line `needs_check` (slip/DCOF/PEI — no scheda tecnica published; pull from price list/rep), exact PV-code↔format mapping, afoideli.gr presence, and the selling voice (Orfeas's to sharpen). **Finished top-to-bottom (2026-06-17b):** full SKU matrix (PV001–PV214, colourway +0/+1/+2/+3 rule), SKE 2.0-sourced technical data (R10/R11 · A+B+C · DCOF > 0.42 · frost/fire · 53 N/mm²; verified for SKE 2.0, `likely` for the line), afoideli.gr confirmed **not** listing it (→ add to site). **Class-tier deep batch still gated** on the 3 paused decisions. **Deferred (Orfeas, "save for later", [[Capture Backlog]]):** (1) a fine-tunable **voice/communication profile** (living note + skill; authorship his); (2) **cost as a collection facet** — decided as option 1 (derived `price_tier` + `price_band`; real prices stay at the SKU/price-list tier), build after a digital price list exists.
- [x] **Acted on the [[2026-06-16-vault-audit|2026-06-16 vault audit]] — all three P0s cleared (2026-06-16).** P0-1: structure reconciled to disk (`15`/`16` seed wings, `18` deferred, [[Vault Map]] is now the single canonical index, §2 links it). P0-2: schema-vs-CSV precedence declared in [[Database Master Schema]] (CSV = stored contract, `.md` annotates) + entity↔CSV pairing table; Orders' 4 derived fields annotated; invoices split into `supplier_invoices.csv` (AP) + `client_invoices.csv` (AR) per the two-table decision; all 10 entity pairs verified in sync. P0-3: contract fixes applied (`CLAUDE.md §9/§3/§7/§1/§6` + [[Session Protocol]] `cd` path; §5 needed none).
- [x] **Audit P1 sweep — done (2026-06-16).** n8n→Python-worker across all 10 live-prescription notes (no live n8n reference remains); orphans wired ([[The Selection Engine]], [[Order Workflow 0-4]], [[Profitability Engine]], [[Credit and Due Date Calendar]], [[Strategic Axes]], [[SEO Topic Map]]) + [[The Material Atelier]] created (seed); frontmatter governance fixed at source (templates + [[Supplier Research Workflow]]) and across all existing notes (`confirmed`→`verified`, `completed`→`complete`); cold notes refreshed not retired ([[Roadmap]], [[Open Questions]], **ADR-0004** logs the n8n pivot, [[Collaboration Home]] session list now Dataview); async capture shipped ([[Research Queue]]); [[Circles]] written; [[Inbox]] marked dormant. Recurring practice: [[Vault Integrity Audit]].
- [ ] **Audit P2 polish (remaining — the only audit work left):** mark [[Weekly Review]] + the daily-note system dormant until the data layer exists; resolve the tag question ([[Obsidian Tips and Tricks]] teaches a dead tag-search); add `created`/`updated` to every dossier for the [[Supplier Enrichment Queue]] Dataview; the ERD `PEOPLE`/`PAYMENTS` gap; remaining orphans beyond the named set; a full [[README_START_HERE]] rewrite. Plus the [[Vault Integrity Audit]] TODO — a `/vault-audit` skill + write-time lint rules.
- [x] Collaboration + memory layer established.
- [x] Git + private GitHub repo.
- [x] Foundation notes shipped: [[The Heart]], [[Afoi Deli — Operating Doctrine]], [[Supplier - Kronos]].
- [x] CLAUDE.md extended (Heart-first load, identity layer, personal-handling rule).
- [x] n8n removed; automation files rewritten to Python worker stack.
- [x] Personal folders reconciled (audit P0-1, 2026-06-16): `15_PERSONAL_LIFE` + `16_IDEAS_AND_VISION` are now real seed wings; `18_KNOWLEDGE` deferred into [[Studies and Subjects]]; `17_JOURNAL` live. (Supersedes the earlier "created 15–18" tick, which described empty git-invisible shells.)
- [x] Supplier ingestion reframed to **public research** ([[Supplier Research Workflow]]); cross-reference machinery parked in [[Automation Backlog]]; [[Hermes Telegram Capture Queue]] rewritten so its drain runs research, not cross-check (2026-06-15).
- [x] **Supplier stack — Cielo, Mutina, Fantini** built to Kronos depth (dossier + collections reference each); two conduit hubs created ([[Conduit - Plus Interiors]], [[Conduit - Filon IKE]]); the Kronos conduit section consolidated into the Plus Interiors hub; Supplier/Brand indexes + Bathroom/Tile knowledge maps wired (2026-06-16).
- [x] **Supplier enrichment scaffolding** — standing *Famous for & specializations* section added to all full dossiers + the [[Supplier Research Workflow]] template; [[Supplier Enrichment Queue]] created (surfaces every blank still to fill: `(your knowledge)` / `(to populate)` / `needs_check`); dossiers treated as living, enriched over passes (2026-06-16).
- [x] **Scavolini ingested** — kitchen dossier (overwrote stub) + collections reference; Orfeas's expansion rationale captured in [[Scavolini Kitchen Expansion]]; countertop cross-sell wired to [[Supplier - Kronos]] / [[Kitchen Knowledge Map]]; our dealer arrangement left as enrichment prompt (Greek Store OMETRY ≠ our channel) (2026-06-16).
- [x] Cross-reference-workflow link graph consolidated — ~12 dangling wikilinks across 6 notes repointed (2026-06-15).
- [x] First [[Journal]] entry (begins with the night of 2026-06-14).
- [x] **n8n sweep complete (2026-06-16, audit P1-A)** — every live n8n prescription replaced with the Python-worker stack; the dead `n8n Workflow Map` link repointed to [[Python Worker Map]]. Only negations + historical session/audit references remain.
- [x] [[Roadmap]] refreshed (2026-06-16) — Phase 3 is now the Python worker; points to the Builder's Manual R0–R3 for the OS build.
- [ ] Decide: Kronos "On afoideli.gr" column — keep as parked pilot data or strip for consistency.
- [x] [[The Material Atelier]] page created as a seed in `16_IDEAS_AND_VISION` (2026-06-16) — scaffold + the merge-vs-differentiate question vs [[AI Construction Materials Platform]]; framing left to Orfeas.
- [ ] Continue interview: more suppliers, the people ([[People and Roles Map]]), personal domains.

## 6. Key open questions

See [[Open Questions]].

## 7. Memory-seed facts needing verification

- Company revenue (~€15m+, `needs_check`).
- Supplier **private** fields (contacts / pricing / terms / lead times / loading) pending for all houses. Kronos + Cielo/Mutina/Fantini now carry full **public** dossiers (`likely`) with private fields as labelled `[!question]` prompts; the other 9 suppliers are still `memory_seed` stubs.
- Full Kouvas column definitions.

---
*Last session: 2026-06-17b ([[Session 2026-06-17b]]) — **cleared the PDF blocker (real Python 3.12 + PyMuPDF, no poppler) and shipped + verified the vault's first collection note, [[Collection - Kronos Pierre Vive]] — [[Collection Schema]] validated end-to-end; added a `graphic_versions` field; roster reframed to ✅/⬚.** Prior: 2026-06-17 ([[Session 2026-06-17]]) — **extended the materials layer to three tiers (class → collection → SKU), [[Architecture Decision Records|ADR-0005]]; added the editorial cluster (aesthetic/mood/SEO).** Created [[Collection Schema]] (born-on-ingestion, raw+normalized, editorial fields), updated [[Materials Research Workflow]] with the specifics clause + ingestion modes (URL / fed PDF / future Drive). Pierre Vive pilot blocked on tooling (no Python/poppler — §4). Next: install Python + poppler, then build `Collection - Kronos Pierre Vive`. Prior: 2026-06-16d ([[Session 2026-06-16d]]) — **started the materials knowledge layer (Batch 1) + made it repeatable, then paused for steer.** Built [[Materials Schema]] + [[Material - Porcelain Stoneware]], filed the [[Afoi Deli — Materials Intelligence]] index, codified [[Materials Research Workflow]], archived raw sources. Resume by checking the 3 open decisions in [[Session 2026-06-16d]] (pattern / batch size / ~22 split). Prior: 2026-06-16c ([[Session 2026-06-16c]]) — **acted on the [[2026-06-16-vault-audit]]: all three P0s + the full P1 sweep cleared.** P0s: structure reconciled to disk (15/16 seed wings, 18 deferred, [[Vault Map]] canonical), data-contract precedence + invoices split, CLAUDE.md/Session Protocol contract fixes. P1: n8n→Python-worker sweep, orphans wired + [[The Material Atelier]] created, frontmatter governance at source, cold-notes refresh + ADR-0004, [[Research Queue]] capture surface + [[Circles]] written + [[Inbox]] dormant. Only audit **P2 polish** remains. Prior same day: 2026-06-16b ([[Session 2026-06-16b]]) — the deep audit + [[Vault Integrity Audit]] charter; 2026-06-16 ([[Session 2026-06-16]]) — supplier stack (Cielo/Mutina/Fantini + Scavolini). Earlier: [[Session 2026-06-15b]], [[Session 2026-06-15]], the 2026-06-14 foundation build. Update this file at the end of every session before committing.*
