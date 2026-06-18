---
type: backlog
created: 2026-06-14
updated: 2026-06-17
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

- [x] **✅ First `/vault-audit` run — DONE (2026-06-17).** Verdict **healthy, no P0**; 7/7 findings critic-confirmed, 0 false-positives ([[2026-06-17-vault-audit]] · ledger [[STATE]]). **Settled the Contested n8n question → sweep COMPLETE** (no live note prescribes n8n). Applied **F1** — softened the inverted `CLAUDE.md §7` freshness flag (it described finished work as pending). New P2 polish (F2/F3/F4) folded into the P2 line below. **Materials (Priority 0.5) is now un-gated** — resume it next.
- [x] **P0 — reconcile structure to disk** *(2026-06-16)*: [[Vault Map]] is now the single canonical folder index, corrected to disk; phantom-folder fork decided (**hybrid**) — `15_PERSONAL_LIFE` + `16_IDEAS_AND_VISION` created as seed wings ([[Personal Life — Home]] / [[Ideas and Vision — Home]]), `18_KNOWLEDGE` deferred ([[Studies and Subjects]]); [[Vault State Memory]] §2 now links the map instead of restating it.
- [x] **P0 — one source of truth for the data contract** *(2026-06-16)*: [[Database Master Schema]] now declares the CSV the canonical stored contract (`.md` annotates) + carries an entity↔CSV pairing table; Orders' 4 derived fields annotated (not stored); invoices split into `supplier_invoices.csv` (AP) + `client_invoices.csv` (AR) per the two-table decision; all 10 entity pairs verified in sync.
- [x] **P0 — fix the contract's self-contradictions** *(2026-06-16)*: applied the drop-in `CLAUDE.md §9 / §3 / §7 / §1 / §6` + [[Session Protocol]] `cd`-path edits from the audit Appendix. (§5 needed no change — creating `15_PERSONAL_LIFE` made its reference true.)
- [x] **P1 sweep** *(2026-06-16)*: n8n→Python-worker done across all 10 live-prescription notes (no live n8n remains) · orphans wired ([[The Selection Engine]] ← Doctrine + Sales Map · [[Order Workflow 0-4]] ← Operations Map · [[Profitability Engine]] + [[Credit and Due Date Calendar]] ← Management Dashboard · [[Strategic Axes]] ← Home Dashboard · [[SEO Topic Map]] ← Strategic Axes) + [[The Material Atelier]] created (seed) · frontmatter governance fixed at source + all existing instances · cold notes refreshed not retired ([[Roadmap]], [[Open Questions]], ADR-0004, [[Collaboration Home]] Dataview) · async capture shipped ([[Research Queue]]) + [[Circles]] written + [[Inbox]] dormant.
- [ ] **P2 polish (audit, remaining):** [[Weekly Review]] + daily notes → mark dormant until the data layer exists · tag question ([[Obsidian Tips and Tricks]] dead tag-search) · `created`/`updated` on every dossier for [[Supplier Enrichment Queue]] · ERD `PEOPLE`/`PAYMENTS` gap · remaining orphans beyond the named set · full [[README_START_HERE]] rewrite · [[Vault Integrity Audit]] TODO — ✅ `/vault-audit` skill + `audit-critic` shipped *(2026-06-17)*; **write-time lint rules/hooks still pending**.
- [ ] **P2 polish (2026-06-17 audit — F2/F3/F4):** **F2** — `Template - ADR` frontmatter `status: proposed` → set to a valid value (`idea`/`seed`) · **F3** — `Template - Project` emits an empty `status:` → default it (`idea`) or Templater-prompt · **F4** — wire orphan `AI Agent Roles` (08) from [[Automation Masterplan]]/[[Python Worker Map]] + resolve duplicate `Supplier Note System` (04) (merge into `Template - Supplier` or relocate to `98_TEMPLATES`). Full list: [[2026-06-17-vault-audit]].

## Priority 0.1 — Make the operational spine real (Root A — the tracer) `[#1 · NEXT SESSION via /goal]`
*From the first `/os-brainstorm` ([[Brainstorm 2026-06-17]]). Orfeas decided the spine is **Root A — the operational everyday** ("Definitely A… do best what I currently do better — the everyday workflow"), and converged on one rule: **"I need to explain reality. Everything else is derived and adjusted to this."** This now leads; Materials (Root B, below) is the deferred fast-follow. **Refined 2026-06-18 ([[Session 2026-06-18]]): unit + method decided below; this is the #1 action for the next session, to be run via the `/goal` command.***

> [!important] The move is an instance, not more knowledge
> Root A does not advance by pouring in more knowledge (materials / schema / soul are all either Root B, already-guessed, or already-done). It advances by running **one real thing** through the vault. The vault is currently a *specification with no instance* — schemas + SOPs written without a real order in hand (audit **F7**; [[Database Master Schema]] CSVs hold zero rows).

- [ ] **The tracer — walk ONE real order end-to-end, by hand, in Obsidian.** Real client → order lines (status 0→4, [[Order Workflow 0-4]]) → supplier PO → proforma check → loading date → delivery notification → payable → profitability ([[Cost & Quote Build]]). One instance simultaneously tests the **database** (what [[Database Master Schema]] is missing), the **process** (where the SOP ideal ≠ reality — supersedes the abstract Priority 5 audit), and surfaces the **real bottlenecks/mistakes** in situ — and produces the vault's **first real operational records**. No Postgres, no worker, no AI.
- [ ] **Protect the craft.** Systematize the mechanical drudgery (Kouvas copy/paste, proforma checks, loading-date chasing, payables, notifications); **don't** systematize the selection/close craft that runs the 80% conversion ([[The Selection Engine]] §6). Orfeas's instinct already: *"proforma checking, not necessarily automated with AI."*
- [x] **Unit — DECIDED (2026-06-18): the order.** It *subsumes* the quote — the sample-wall/quote moment is stage 1 — so one order tracer exercises the full spine **and** the quote/cost chain in a single pass. Use a **recent, closed, ordinary-with-a-wrinkle order**: *closed* so every artifact already exists (zero hypotheticals), *with a wrinkle* because a perfectly smooth order hides the failure modes. Still open — **which specific instance**: Orfeas picks one at the start of the run.
- [ ] **Method — DECIDED (2026-06-18): the guided walk** (artifacts paired with narration; **never** an unlabelled file-dump — that is the only mode that dilutes). **(1)** Orfeas narrates the chosen order once, top-to-bottom, ~5–10 sentences (client → quote → order → supply → delivery → payment, + the wrinkle) — spine + meaning *before* any file. **(2)** Then walk it **stage by stage**: at each stage Orfeas drops the real artifact for *that* stage (quote Excel / supplier proforma / loading doc / invoice — PDF, or a screenshot/paste of the rows), Claude reads it for ground truth, reflects back + asks 1–2 questions *only* where file ≠ story, then writes the real record — flagging every spot the schema is **missing/wrong** or the **SOP-ideal ≠ reality**. **(3)** Output: the vault's first real order record + a schema-corrections list + an SOP↔reality-gaps list + bottlenecks/mistakes in situ. Buy-side numbers stay **confidential** (CLAUDE §4).
- [ ] **Executor — the `/goal` command.** Run the tracer via `/goal` next session (its first use for this). *If `/goal` isn't a registered skill/command when we start, fall back to a manual staged walk — the method above stands either way.*
- [ ] **Sequencing note (proposed promotions in the log):** the [[Roadmap]] "document → structure → automate" waterfall is challenged in favour of **instance-first** (validate against one real transaction *before* building the data/automation layers) → candidate ADR. Also resolve the **Builder's Manual R0–R3 phantom** (cited as existing in [[Vault State Memory]] §4 / [[Roadmap]] L13 but **no note on disk**).

## Priority 0.5 — Materials knowledge layer (Root B — deferred fast-follow)
> [!note] Reframed 2026-06-17 ([[Brainstorm 2026-06-17]]): materials is the **Root B** content/merchandising branch — the fast-follow *behind* the operational spine (Priority 0.1 above), not the lead thread. Decided with Orfeas: the spine (Root A) and reference depth (Root B) *don't have to move together* — the spine comes first. Don't pull this ahead of the tracer.

*Batch 1 shipped 2026-06-16d, then paused for steer. Architecture extended 2026-06-17 to three tiers ([[Architecture Decision Records|ADR-0005]]). Run [[Materials Research Workflow]]. Context: [[Session 2026-06-16d]] · [[Session 2026-06-17]] · index: [[Afoi Deli — Materials Intelligence]].*

- [x] **🔧 PDF tooling — DONE (2026-06-17b).** This machine has **real Python 3.12** + **PyMuPDF (fitz) 1.26.7**, which renders PDF pages to images the Read tool views (`pdftotext`/Xpdf covers the text layer). **poppler not needed** — PyMuPDF replaces `pdftoppm`. Proven on the Pierre Vive catalogue; all PDF/TDS ingestion unblocked.
- [ ] **Decide 3 things first** — (1) approve the [[Materials Schema]] + [[Material - Porcelain Stoneware]] pattern before it's replicated ~20×; (2) batch size; (3) the **~22 split** (Countertop → sintered-stone / engineered-quartz / natural-stone; split a `stainless-steel` note off Brass).
- [ ] **Next deep batch (class tier)** — Large-Format Porcelain Slab → Glass Mosaic → Sanitary Ceramic → SaphirKeramik (then the medium/light materials).
- [x] **Pilot the collection tier — DONE (2026-06-17b).** Built the vault's first collection note [[Collection - Kronos Pierre Vive]] against [[Collection Schema]] (incl. the editorial cluster); reframed [[Kronos — Collections Reference]] into the ✅/⬚ roster; ran a 3-lens adversarial verification and fixed every finding; **added a `graphic_versions` field** to the schema. **Finished top-to-bottom (2026-06-17b):** full SKU matrix (PV001–PV214, colourway +0/+1/+2/+3 rule), SKE 2.0-sourced slip/technical data (R10/R11 · A+B+C · DCOF > 0.42 · frost/fire · 53 N/mm², `likely` for the line), and afoideli.gr confirmed **not** carrying it. Remaining: price-list SKU confirmation; the **selling voice** (Orfeas's to sharpen).
- [ ] **Add Pierre Vive to afoideli.gr** — our newest hero Kronos stone line is not on our own site (confirmed 2026-06-17 via the WooCommerce Store API; other Kronos lines are present). Website/content task.
- [ ] **Still to build** — Dataview "Materials Index" + `.base`; the verification ledger; cross-link materials into the 13 supplier dossiers; migrate each material's prose out of the MOC into its atomic note.
- [ ] **Resolve the `needs_check`** on [[Material - Porcelain Stoneware]] — which stocked brands are full-body vs glazed; which 20 mm outdoor ranges are carried.

## Captured 2026-06-17b — voice & cost (Orfeas: save for later)
*Two capabilities raised this session, deferred deliberately. Designs recorded so they're ready to pick up.*

- [ ] **Voice & Communication profile (next session).** Build a living **Voice Profile note** (Orfeas authors the voice; Claude encodes + applies) covering principles, do/don't, rhythm, and **per-channel registers** (catalogue/editorial · client email · social · internal). `Premium Human Email Tone` becomes the "email" channel under it. Wire it into `CLAUDE.md` + the ingestion workflows (always-on) + a thin **skill** for *apply my voice* / *tune my voice*. **Seed method TBD** — Orfeas to choose (real samples / draft-from-The-Heart / guided interview). Authorship stays his per [[CLAUDE]] §6.
- [ ] **Cost as a collection classification facet — DECIDED (option 1), build deferred.** Real prices stay at the **SKU/price-list tier** (`products`: `buy_price`/`sell_price`/`discount`, approval-gated, volatile); each **collection** carries `price_tier` (exists) **+ a derived `price_band` (€/m²)** computed from its SKUs via the SKU→collection join. So cost is queryable at the collection level without copying live prices into notes. **Build when:** a digital price list exists / as collections expand. Add `price_band` to [[Collection Schema]] + document the derivation in [[Database Master Schema]]. (Asked 2026-06-17b; "finish Pierre Vive first, then expand.")

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
- [ ] **Google Drive collection feeder (uncertain — captured 2026-06-17)** — Orfeas uploads catalogue/TDS PDFs to the shared Drive folder; Claude (now) or the Python worker (later) ingests collections from there — **on prompt** ("ingest what's new in Drive") or on a **watch/auto** trigger. Depends on the worker's **Drive access** (service-account vs OAuth — the *same* parked decision as the asset-ingestion items above). Until decided, feed PDFs by **attaching them in chat** or **dropping them in the supplier's `_sources/`** — see the ingestion modes in [[Materials Research Workflow]]. Not yet decided; do not build unprompted.
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
