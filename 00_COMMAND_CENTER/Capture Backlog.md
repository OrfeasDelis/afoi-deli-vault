---
type: backlog
created: 2026-06-14
updated: 2026-06-16
status: active
tags:
  - command-center
  - backlog
---

# Capture Backlog

> [!tip] How to use this
> This is the answer to *"what do I work on with Claude?"* — you never start from a blank page.
> **Before a session:** open this, pick the top unchecked item, capture it into a note.
> **A topic is done** when it has produced a findable note (not when everything's been said).
> **After a session:** tick what you shipped, add anything new that surfaced.
> Rank by **value × perishability**: capture what only you know and would lose if forgotten. Generic, lookup-able things don't belong here.

---

## Priority 0 — Vault integrity (do this first, next session)
*The [[2026-06-16-vault-audit|2026-06-16 audit]] found the vault's account of itself has drifted from disk. Reconcile the source-of-truth before stacking more knowledge on top. Recurring practice: [[Vault Integrity Audit]].*

- [x] **P0 — reconcile structure to disk** *(2026-06-16)*: [[Vault Map]] is now the single canonical folder index, corrected to disk; phantom-folder fork decided (**hybrid**) — `15_PERSONAL_LIFE` + `16_IDEAS_AND_VISION` created as seed wings ([[Personal Life — Home]] / [[Ideas and Vision — Home]]), `18_KNOWLEDGE` deferred ([[Studies and Subjects]]); [[Vault State Memory]] §2 now links the map instead of restating it.
- [x] **P0 — one source of truth for the data contract** *(2026-06-16)*: [[Database Master Schema]] now declares the CSV the canonical stored contract (`.md` annotates) + carries an entity↔CSV pairing table; Orders' 4 derived fields annotated (not stored); invoices split into `supplier_invoices.csv` (AP) + `client_invoices.csv` (AR) per the two-table decision; all 10 entity pairs verified in sync.
- [x] **P0 — fix the contract's self-contradictions** *(2026-06-16)*: applied the drop-in `CLAUDE.md §9 / §3 / §7 / §1 / §6` + [[Session Protocol]] `cd`-path edits from the audit Appendix. (§5 needed no change — creating `15_PERSONAL_LIFE` made its reference true.)
- [x] **P1 sweep** *(2026-06-16)*: n8n→Python-worker done across all 10 live-prescription notes (no live n8n remains) · orphans wired ([[The Selection Engine]] ← Doctrine + Sales Map · [[Order Workflow 0-4]] ← Operations Map · [[Profitability Engine]] + [[Credit and Due Date Calendar]] ← Management Dashboard · [[Strategic Axes]] ← Home Dashboard · [[SEO Topic Map]] ← Strategic Axes) + [[The Material Atelier]] created (seed) · frontmatter governance fixed at source + all existing instances · cold notes refreshed not retired ([[Roadmap]], [[Open Questions]], ADR-0004, [[Collaboration Home]] Dataview) · async capture shipped ([[Research Queue]]) + [[Circles]] written + [[Inbox]] dormant.
- [ ] **P2 polish (audit, remaining):** [[Weekly Review]] + daily notes → mark dormant until the data layer exists · tag question ([[Obsidian Tips and Tricks]] dead tag-search) · `created`/`updated` on every dossier for [[Supplier Enrichment Queue]] · ERD `PEOPLE`/`PAYMENTS` gap · remaining orphans beyond the named set · full [[README_START_HERE]] rewrite · [[Vault Integrity Audit]] TODO (`/vault-audit` skill + write-time lint rules).

## Priority 0.5 — Materials knowledge layer (ACTIVE — resume next session)
*Batch 1 shipped 2026-06-16d, then paused for your steer. Run [[Materials Research Workflow]]. Full context: [[Session 2026-06-16d]] · index: [[Afoi Deli — Materials Intelligence]].*

- [ ] **Decide 3 things first** — (1) approve the [[Materials Schema]] + [[Material - Porcelain Stoneware]] pattern before it's replicated ~20×; (2) batch size; (3) the **~22 split** (Countertop → sintered-stone / engineered-quartz / natural-stone; split a `stainless-steel` note off Brass).
- [ ] **Next deep batch** — Large-Format Porcelain Slab → Glass Mosaic → Sanitary Ceramic → SaphirKeramik (then the medium/light materials).
- [ ] **Still to build** — Dataview "Materials Index" + `.base`; the verification ledger; cross-link materials into the 13 supplier dossiers; migrate each material's prose out of the MOC into its atomic note.
- [ ] **Resolve the `needs_check`** on [[Material - Porcelain Stoneware]] — which stocked brands are full-body vs glazed; which 20 mm outdoor ranges are carried.

## Priority 1 — The people
*Highest value: the heart of both business and life, entirely in your head, irreplaceable.*

- [ ] **Kostas (father)** — the founder, the maxims, the merchant's nerve and intuition. The model. → note in `01_COMPANY_CORE` / linked from [[The Heart]] and [[People and Roles Map]].
- [ ] **Chrysoula (mother)** — the closer, the human gift. Her role in the uplift engine.
- [ ] **Ektoras (brother)** — role in the business and the family. (Currently a placeholder.)
- [ ] **Eleni (partner)** — her own note in `15_PERSONAL_LIFE/Relationships`. Begins as a named presence; fill in over time.

## Priority 2 — Core suppliers (identity brands)
*Perishable, commercially load-bearing. Same treatment as [[Supplier - Kronos]].*

- [x] **Cielo** — sanitary ware; the founding Tzanidis story; flagship. → [[Supplier - Cielo]] + [[Cielo — Collections Reference]] *(2026-06-16)*
- [x] **Mutina** — identity brand, premium tile. → [[Supplier - Mutina]] + [[Mutina — Collections Reference]]; conduit [[Conduit - Filon IKE]] *(2026-06-16)*
- [x] **Fantini** — taps/faucets, through Plus Interiors. → [[Supplier - Fantini]] + [[Fantini — Collections Reference]] *(2026-06-16)*
- [ ] Then the rest of the heavy houses as they earn pages (Salvatori, Antonio Lupi, Atlas Concorde, Florim…).
- [ ] **Enrich the five full dossiers** (Kronos · Cielo · Mutina · Fantini · Scavolini) — fill the private `[!question]` fields: lead times, famous-for / hero products, payment terms, discount ceilings, specializations, loading/packaging, common proforma mistakes. Walk them via [[Supplier Enrichment Queue]].
- [ ] **Resolve supplier `needs_check` facts** — Cielo VAT/P.IVA + registered address; Mutina registered-office change; **Fantini Greek importer** (confirm Plus Interiors vs. the food-company namesake); certifications for all three.
- [ ] **Filon IKE — full subbrand roster** + Plus Interiors relationship specifics ([[Conduit - Filon IKE]] · [[Conduit - Plus Interiors]]).

## Priority 3 — Open the personal rooms
*So `15_PERSONAL_LIFE` isn't just empty folders.*

- [ ] One real note in **Relationships**, **Wellness**, or **Finance** — whichever is most alive.
- [ ] Keep the [[Journal]] going — the habit matters more than the structure.

## Priority 4 — Ideas & Vision
*Give the creative/venture work proper homes in `16_IDEAS_AND_VISION`.*

- [ ] **Mnemonic Atelier** — the doctrine (Lineage Art, Archive Equity, Seven Operations).
- [ ] **The Material Atelier** — the architect-facing B2B brand/platform.
- [ ] **Circles** — the prediction-market concept.

## Priority 5 — Operational truth
*Where the SOPs describe the ideal vs. how the business actually runs.*

- [ ] Audit the SOPs in `02_OPERATIONS_OS` for aspirational-vs-real, mark with confidence tags.

## Hermes Capture Queue — registry
*The Telegram → queue → worker inbox. Full design: [[Hermes Telegram Capture Queue]]. This registry tracks build state; the queue itself (once built) holds the actual suppliers/collections for Hermes to research.*

- [ ] **v0 — capture works.** Add `/add <supplier> <collection>`, `/add <url>`, and a file handler to the [[Circles]] bot host; write rows to a queue (bot SQLite or a vault file); reply "queued #N". *Useful even before draining is automated.*
- [ ] **v0.5 — manual drain.** Process pending rows by running the [[Supplier Research Workflow]] by hand — feed each supplier/collection to Hermes, save the dossier, mark `done`.
- [ ] **v1 — worker `/drain` job.** Automate Hermes deep research → write the dossier (supplier note + collections reference) → flip to `done`. *Public research only — no afoideli.gr cross-check.*
- [ ] **v2 — second feeder.** The monthly collections-index auto-diff (`article:modified_time`) appends changed collections to the *same* queue, so Hermes re-researches them and refreshes the dossier.
- Open decisions: queue store (lean: bot SQLite); dossier depth (defined in [[Supplier Research Workflow]]); Drive auth — only if research source assets are filed to Drive, else drop (service account vs OAuth); confirm Circles bot can host a second command set.

## Future / when the OS exists
*Captured, deliberately deferred — do NOT pull these forward.*

- [ ] **Kronos catalogue & asset ingestion** — pull collection PDFs/photos into Google Drive, link back from Obsidian; pilot for an all-suppliers template. Plan ready: [[Kronos — Catalogue & Asset Ingestion]]. Blocked on **Google Drive write access for the worker** (service-account vs OAuth decision). Manual option works now for top-quoted collections.
- [ ] **Cielo / Mutina / Fantini catalogue & asset ingestion** — catalogue + technical PDFs already linked in [[Cielo — Collections Reference]], [[Mutina — Collections Reference]], [[Fantini — Collections Reference]]; pull into Drive when worker write-access lands (same pattern as [[Kronos — Catalogue & Asset Ingestion]]).
- [ ] **Loop engineering** — revisit only when Afoi Deli OS has a test suite and automated verification (the 14-step loop doc). Premature until then.
- [ ] **QMD search layer** — add as the retrieval layer only once the index file stops being enough (vault grows past a few hundred dense pages). Karpathy names it as the documented option.

---

## Done (shipped)

- [x] **Live vault connection set up** (Claude + filesystem MCP) — sources can now be written directly to disk; unblocked the frictionless ingest workflow *(2026-06-15)*
- [x] [[The Heart]] — foundational doctrine note *(2026-06-14)*
- [x] [[Afoi Deli — Operating Doctrine]] *(2026-06-14)*
- [x] [[Supplier - Kronos]] — first populated supplier *(2026-06-14)*
- [x] [[CLAUDE]] extended + ingest/query/lint loop added *(2026-06-14)*
- [x] [[Vault State Memory]] rewritten *(2026-06-14)*
- [x] Personal folders created; n8n removed; git repaired *(2026-06-14)*
- [x] Journal begun — template + first entry *(2026-06-14)*
- [x] [[Session 2026-06-14]] detailed session log *(2026-06-14)*
- [x] Kronos supplier doc filled from website + all 18 collections — [[Kronos — Collections Reference]] *(2026-06-15)*
- [x] [[Supplier Research Workflow]] — reusable supplier-research skill (shipped 2026-06-15 as the cross-reference workflow, since reframed to public research) *(2026-06-15)*
- [x] [[Kronos — Catalogue & Asset Ingestion]] + [[Hermes Telegram Capture Queue]] concepts *(2026-06-15)*
- [x] `Suppliers/` restructured to one folder per supplier *(2026-06-15)*
- [x] [[Session 2026-06-15]] session log *(2026-06-15)*
- [x] Hermes capture queue reframed to supplier research; cross-reference-workflow links consolidated (6 notes); vault lint — [[Session 2026-06-15b]] *(2026-06-15)*
- [x] **Supplier stack** — Cielo, Mutina, Fantini dossiers + collections refs; conduit hubs [[Conduit - Plus Interiors]] / [[Conduit - Filon IKE]]; standing *Famous for & specializations* slot + [[Supplier Enrichment Queue]] — [[Session 2026-06-16]] *(2026-06-16)*
- [x] **Scavolini ingested** — dossier + [[Scavolini — Collections Reference]]; kitchen-expansion rationale ([[Scavolini Kitchen Expansion]]) + countertop cross-sell pathway wired *(2026-06-16)*

---
*Linked: [[The Heart]] · [[Vault State Memory]] · [[Session 2026-06-15]]*
