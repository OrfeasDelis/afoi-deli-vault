---
type: programme_charter
created: 2026-07-19
status: active
confidence: verified
owner: Orfeas Delis
tags:
  - programme
  - governance
  - consolidation
---

# Consolidation and Enrichment Programme

> [!abstract] What this is
> The vault's standing **governed consolidation, enrichment and continuous-build programme** — the frame under which the vault is consolidated (one canonical home per truth), enriched (tacit knowledge extracted at depth), and grown (suppliers, products, cases) without losing momentum or history. Adopted **2026-07-19** via [[Architecture Decision Records|ADR-0007]] with four reconciliations (§ Reconciliations below). The raw external draft is immutable in `_sources/redoal — governed consolidation programme (external, 2026-07-19).md`; this charter is the working distillation. *This is a preservation-and-precision programme, not a destructive cleanup.*

## Standing mandate

Preserve and strengthen what works · remove genuine duplication without destroying history · one unmistakable canonical home per important truth · convert the completed tracer into corrected doctrine/schemas/examples · a repeatable programme for extracting Orfeas's tacit knowledge at depth · a reliable supplier/collection/product ingestion system · real operational instances without document-dump sprawl · better audits, skills, agents, templates and deterministic tools · knowledge compounding over time · the vault ready as the governed knowledge + policy layer of the future Afoi Deli OS.

## Non-negotiable principles

1. **Do not derail the project.** Protect momentum, vocabulary, the authorship line. No wholesale folder redesign for theoretical cleanliness. Afoi Deli terminology stays recognizable (ΚΟΥΒΑΣ · DAILY/ΠΡΩΤΟ/ΔΕΥΤΕΡΟ/ΠΡΟΣ ΠΑΡΑΔΟΣΗ/ΤΡΙΤΟ · ΒΑΛΤΟΣ · ΣΚΟΥΠΑ · the tracer · [[The Heart]] · [[The Selection Engine]] · the uplift engine · the five-layer OS); generic abstractions may sit underneath, never erase.
2. **Ground truth wins.** Precedence: real source artifact → verified human explanation → ground-truth capture → canonical operational doctrine → schema/domain contract → automation spec → interface projection → agent behaviour → generated analysis. Newer ground truth beats older SOP until reconciled; artifact-vs-memory conflicts are recorded, never silently resolved.
3. **One fact, one canonical owner.** Reference from many notes; maintain in one. (Commercial terms → the supplier dossier's private section · lifecycle → the canonical order-workflow note · state → [[Vault State Memory]] · priority → [[Capture Backlog]] · decisions → ADRs/Decision Log · metrics → generated analysis.)
4. **Raw sources are immutable evidence** (PDFs, price lists, proformas, DDTs, emails, workbooks, photos, transcripts — the `_sources/` layer). Derived notes evolve; evidence stays identifiable and traceable.
5. **No silent deletion.** Lifecycle: identify overlap → identify canonical owner → map unique content → merge → repair links → mark superseded → cooling period → audit → delete only when no unique value or live dependency remains.
6. **No mass creation of empty notes** — born on ingestion (already doctrine, [[Architecture Decision Records|ADR-0005]]). Entity notes exist when a real source landed, the entity is operationally active, it appears in a real order/project, a body of knowledge exists, a live relationship needs it, or Orfeas asks. Rosters/index rows hold the rest.
7. **Human judgement remains visible.** Never convert "usually / depends on the client" into hard logic. Model: `decision_type: deterministic | default | heuristic | relationship_override | owner_judgement` + owner, inputs, typical outcome, known exceptions.
8. **AI proposes; governed systems act** (= `CLAUDE.md §4`). AI extracts, compares, drafts, recommends, flags contradictions, proposes merges/schemas/PRs. AI never autonomously: changes prices/financial records/statuses, promises dates, approves proformas, sends external comms, alters permissions, deletes evidence, rewrites human-authored doctrine, or merges its own structural changes without review.

## The knowledge classes

| Class | What it holds | Canonical home today |
|---|---|---|
| Doctrine | identity, values, strategy, voice — human-authored | [[The Heart]] · [[Afoi Deli — Operating Doctrine]] · [[The Selection Engine]] |
| Steering | current state, work queue, decisions | [[Vault State Memory]] → [[Capture Backlog]] → [[Architecture Decision Records]] → session logs |
| Ground-truth captures | how the business actually operates, pre-rules | [[Order Lifecycle — Ground-Truth Capture]] (first; more to come per interview) |
| Canonical operational doctrine | approved workflows, rules, exceptions | `02_OPERATIONS_OS` SOPs (to reconcile with the tracer) |
| Domain & schema contracts | vocabularies, entities, fields | `03_DATABASE_DESIGN` + `97_CSV_SCHEMAS` (CSV = stored contract) · [[Materials Schema]] · [[Collection Schema]] |
| Entity dossiers | suppliers, brands, materials, collections, people | `04_SUPPLIERS_AND_BRANDS` · `07_PRODUCT_KNOWLEDGE` · [[People and Roles Map]] |
| Cases & instances | real orders, incidents, claims, journeys | `02_OPERATIONS_OS/Cases/` (to be born with the golden tracer case) |
| Audit & governance | findings, drift, coverage, contradictions | `_meta/audits/` (+ `_meta/consolidation/` once born) |
| Generated files | self-identified, snapshot-named, reproducible | `docs/` (REPO_ANALYSIS + tree suite + VISION; README block) |
| Historical material | why decisions happened, superseded terms | session logs, ADRs, superseded notes — visibly classified, never presented as current |

Every canonical SOP must state: `ground_truth_sources · last_reconciled · owner · confidence · known_exceptions · system_implications`.

## The consolidation passes (sequential, never one big bang)

| Pass | What | Status |
|---|---|---|
| 0 — Safety baseline | clean tree · baseline snapshot · file tree, link graph, orphan/broken/frontmatter/duplicate inventories, source + confidentiality scan → `docs/VAULT_BASELINE_<date>.md`. No structural changes. | **First run 2026-07-19** |
| 1 — Entity & note-purpose registry | deterministic registry of every content note (purpose, canonical_owner_of, overlaps, recommended_action from the controlled set KEEP_CANONICAL … REVIEW_WITH_ORFEAS). Read-only. | with Pass 0 |
| 2 — Overlap analysis | cluster genuine overlaps; canonical recommendation + merge/link-repair/archive steps per cluster → `_meta/consolidation/Overlap Registry.md`. Merge only when fact-ownership genuinely duplicates — never to reduce note count. | with Pass 0 |
| 3 — Steering consolidation | one hierarchy: [[Vault State Memory]] → [[Capture Backlog]] → ADRs → open business decisions → session logs. Review [[Roadmap]], [[Open Questions]], `00_COMMAND_CENTER` priority files, [[README_START_HERE]] — decide current vs historical vs retire. No competing roadmaps. | after baseline review |
| 4 — **Final tracer landing** (highest-priority knowledge action) | Layer A ground-truth narrative (S1–S15) · Layer B SOP reconciliation (Order Workflow 0-4, ΚΟΥΒΑΣ, proforma, receiving, delivery, finance, exceptions — each changed rule links its tracer evidence) · Layer C formal schema-diff of the 49 corrections (correction_id → current model → required model → migration implication → open decision; CSVs not edited before the diff is reviewed) · Layer D one anonymized golden-tracer example package. | after baseline review — the #1 content action |

## Knowledge enrichment

- **Knowledge-depth ladder** — explore every important topic through 12 layers: description → trigger → normal path → decision inputs → rule-vs-judgement → exceptions → failure modes → economics → relationship dimension → evidence → system implication → automation boundary. Never stop at the first three.
- **Truth capsules** — important findings carry structure (claim · truth_type `fact|rule|default|heuristic|judgement|exception` · source · owner · confidence · validity · exceptions · financial/relationship effect · confidentiality · schema/automation effect · public_safe), embedded in domain notes, not one-note-per-claim.
- **Interview procedure** — one narrow domain, one real artifact; reconstruct the timeline; three counterfactuals; hidden decisions; financial consequences; relationship overrides; novice misunderstandings vs expert tells; memory-only knowledge; factual summary → contradictions → confirmation → only then update canonical notes; schema/automation implications separately; follow-up actions registered.
- **Interview sequence (in order):** 1 ΚΟΥΒΑΣ as procurement control · 2 supplier AP + Kostas's payment calendar · 3 realized margin · 4 warehouse receipt & staging · 5 deliveries & payment gating · 6 returns, breakage & claims · 7 architect/referrer economics · 8 sales & selection craft · 9 supplier relationship intelligence · 10 product & material expertise per category.
- **Coordination:** a **Knowledge Action Register** (`00_COMMAND_CENTER`) coordinates knowledge questions across domains (id · domain · question · why it matters · owner · artifact/interview required · confidence · target output · downstream files · implications · priority · status). Born at baseline time with real content. *It is a gap register, not a second execution queue — see Reconciliations.*

## Supplier & product ingestion

- **Manifest before bulk.** `04_SUPPLIERS_AND_BRANDS/Supplier Source Manifest.md` governs every source: id, supplier/brand, controlled `source_type` (commercial_price_list … loading_document), language, years, location, `sha256`, rights, confidentiality, supersedes/superseded_by, extraction + review status, linked entities.
- **Priority order:** **A** commercial/operational truth (price lists, discounts, terms, packaging, lead times — confidential) → **B** orderable product structure (collections, SKUs, formats, finishes) → **C** technical truth (class, slip, absorption, certifications) → **D** editorial/public content. Commercial and public information never share an uncontrolled projection.
- **Pipeline per supplier:** verify identity → manifest → hash + archive immutable originals → classify confidentiality → extract public then private facts → update dossier → collections roster → ingest one representative collection → validate schema → record open questions → Orfeas enrichment → audit → expand.
- **Representative pilots first** (tile matrix · tap configuration · sanitaryware/furniture components · parquet grading · Scavolini modular kitchens) — scale only once category problems are understood.
- **Category adapters** over a shared product core (`product_id … verification_status`) — tile/slab, tap, sanitaryware, furniture, parquet, kitchen extensions; never force every category into the tile schema.
- **Product-tier verification** uses `verification_status` (`source_verified | supplier_asserted | human_verified | derived | needs_check | deprecated`) at the schema/product tier — see Reconciliations. A marketing catalogue never makes a product "technically verified."
- The discarded 2026-07-13 ΕΡΓΟΣΤΑΣΙΑ sweep is **redone through this pipeline** when its turn comes.

## Case library

`02_OPERATIONS_OS/Cases/` — anonymized unless a real identity is operationally necessary and approved. Ten initial archetypes: normal multi-supplier order · WAIT line · mixed client/stock/sample procurement · proforma mismatch · urgency split-loading · partial receipt with child backorder · partial delivery with intermediate payment · transport breakage + carrier claim · client return/defect into stock-ΣΚΟΥΠΑ · architect rebate with non-trivial settlement. Case contract: id, type, anonymized, period, participants, timeline, decision points, exceptions, quantities, documents, financial events, outcome, lessons, doctrine/schema/automation implications, confidence. Cases test whether doctrine and schemas describe reality — never client biographies.

## Audit system v2 (extends [[Vault Integrity Audit]], never replaces)

- **Session-close lint** (fast, deterministic): frontmatter enums · new orphans · broken links · missing inbound links · unregistered open questions · unclassified sensitive files · missing `updated` · unmanifested sources · generated freshness · state/backlog updated.
- **Weekly delta audit** (changed files only): duplicated facts? new canonical competitor? confidential values copied? empty scaffolds? source → all downstream updates? inbound links? vocabulary violations? ground truth changed without SOP review, or SOP without evidence?
- **Monthly structural audit:** registries, overlap clusters, stale steering, orphans, links, frontmatter, manifests, review dates, gap coverage, unresolved tracer findings, schema-example coverage, confidentiality duplication, historical-as-current.
- **Quarterly adversarial audit** — independent critic lenses: information architecture · operational domain · database/schema · source/provenance · security/privacy · agent governance · public-leakage · human-authorship. Findings classified: confirmed defect / meaningful risk / acceptable trade-off / intentional design choice / false positive / requires Orfeas.
- **Metrics as trends** (canonical vs supporting vs historical counts, unresolved overlaps, verified-fact %, stale needs_check, notes-without-sources and sources-without-notes, case count, schema-example coverage, confidential duplication, orphan/broken rates, freshness, enrichment coverage). Audits propose; mechanical auto-fixes only when unambiguous, meaning-preserving, test-verified, logged.

## Agent contracts

| Agent | Purpose | Today |
|---|---|---|
| Vault Steward | structure, canonical ownership, session coordination; no deletion outside protocol, no doctrine rewrites | the main-session role (Session Protocol) |
| Ground-Truth Interviewer | narrow artifact-grounded questions, counterfactuals, rule-vs-judgement; never interview→doctrine without review | the tracer method, to formalize |
| Supplier/Product Ingestion | manifest, extraction, confidence, dossier/collection updates; stops on ambiguity, outdated sources, rights, leaks | [[Supplier Research Workflow]] + [[Materials Research Workflow]], to extend |
| Schema Reconciliation | ground truth → current model / required model / example / constraint / migration / open decision; no elegance-driven change | to build (Pass 4 Layer C) |
| Contradiction Critic | conflicting facts/doctrine/terminology; distinguishes context, era, supplier-specific vs genuine contradiction | to build |
| Audit Critic | adversarial verification of findings | **exists** — `.claude/agents/audit-critic.md` |
| Security Classifier | PII, commercial secrets, personal content, unsafe projection | to build (baseline runs a heuristic scan) |
| Domain Compiler | export approved knowledge to the future app repo; validates, versions, rejects restricted; never exposes the whole vault | future (OS build) |
| Session Closer | state, backlog, log, questions, manifest, analysis, lint, commit hygiene | `CLAUDE.md §8` + git-sync guard, to extend with lint |

## Skills & deterministic tools (one canonical implementation each)

Exists: `/vault-audit` (+ ledger `_meta/audits/STATE.md`) · `/repo-analysis` (+ `vault_metrics.py`) · `/os-brainstorm`. Planned (build when their pass needs them, not before): `/vault-baseline` · `/overlap-registry` · `/canonicalize-note` · `/knowledge-interview` (plan/interview/summarize/verify/land — never one uncontrolled op) · `/tracer-land` · `/source-manifest` · `/supplier-ingest` · `/collection-ingest` · `/product-ingest` · `/case-build` · `/schema-diff` · `/source-audit` · `/sensitivity-audit` · `/vault-lint` · `/knowledge-gap-report`. Script backlog (`scripts/`): inventory · frontmatter validate · link graph · duplicate candidates · canonical fact registry · source manifest · hash inventory · sensitivity scan · supersession validate · knowledge-gap report · schema-example coverage · tracer-correction tracker · vocab validate · generated freshness · domain export. Every script: UTF-8-correct, JSON + Markdown out, read-only by default, `--check`/`--apply`, non-zero exit on CI failure, fixtures/tests, no confidential values in logs.

## Cadence

- **Every session:** The Heart → state → latest log → backlog → one bounded goal → work only that → register ambiguities → update canonical notes → session lint → state + log → regenerate analysis → one coherent commit. (= `CLAUDE.md §8`, extended with the lint.)
- **Weekly:** review Knowledge Action Register, consolidation candidates, new sources, stale needs_check, tracer-correction burn-down, ingestion progress, classification issues; run the delta audit.
- **Monthly:** structural audit · one deep knowledge domain · one new case · one ingestion pilot · review canonical vs historical · retire one steering duplication · check the tools still earn their keep.
- **Quarterly:** adversarial audit · taxonomy review · agent permissions · public/private separation · source-storage strategy · coverage vs business priorities · is the vault feeding the OS cleanly.

## The 90-day arc

Days 1–14 stabilize & map (baseline, registries, canonical map, ADRs, one steering hierarchy — no destructive deletion) → 15–30 **land the tracer** (narrative, 49-correction register, reconciled SOPs, schema-diff, golden case) → 31–45 deep operational knowledge (interviews 1–5) → 46–60 ingestion pilots (tile, tap, sanitaryware/furniture) → 61–75 case library + audit v2 → 76–90 agent/tooling hardening (contracts, canonical skills source, tested scripts, governance manual, v2 baseline). **Knowledge-depth scorecard** per domain, 0 (absent) → 10 (continuously maintained, system-ready), across sales/quotes/orders/ΚΟΥΒΑΣ/POs/proformas/loadings/receipts/inventory/deliveries/AR/AP/payments/credit/profitability/rebates/returns/breakage/claims/supplier-intelligence/materials/collections/products/projects/architect-CRM/public content. Note quantity ≠ knowledge depth.

## Governance rules (proposed for CLAUDE.md after baseline review)

**A** no destructive reorganization without baseline + overlap registry + link-impact report + approved plan + post-audit · **B** one source of truth per maintained fact · **C** ground truth isn't complete until landed (SOPs reconciled, schema implications recorded, decisions registered, one real example) · **D** source ingestion is a transaction (manifest + derived note + dossier + confidence + questions + log) · **E** no bulk empty entities — rosters first · **F** confidentiality travels downstream (no public note from a confidential source without field-level sanitization) · **G** generated files describe, humans + ADRs decide · **H** every automation needs fixtures (3 normal + 3 exception + abstention + approval boundary + eval criteria) · **I** every schema entity needs a real instance · **J** every important judgement names its owner (who decides, on what inputs, when they escalate, what can't be automated).

## Stopping conditions — request an Orfeas decision when

Two notes express different strategic intent · a deletion would remove unique history · a rule depends on relationship judgement · a confidential fact's canonical home is unclear · a personal/business boundary is unclear · a schema change would redefine an operational status · a rule may be supplier-specific, not universal · an artifact conflicts with memory · a source is outdated/contradictory · public content may reveal private data · a consolidation would substantially change the taxonomy · an automation would act externally · a note may be Orfeas-authored doctrine · a new controlled-vocabulary value is needed · a real identity would enter a reusable fixture. **Do not improvise through these.**

## Reconciliations (ADR-0007 — where this charter deliberately diverges from the raw draft)

1. **Confidence vocabulary unchanged at note level.** `confidence: verified | likely | memory_seed | needs_check` stays exhaustive (`CLAUDE.md §3`). The draft's six-value product set becomes `verification_status` at the product/collection tier (precedent: [[Materials Schema]]'s mapping, [[Architecture Decision Records|ADR-0005]]).
2. **One execution queue.** [[Capture Backlog]] remains the single ranked queue; the Knowledge Action Register coordinates knowledge gaps and never ranks execution — otherwise it becomes the parallel priority list the programme itself bans.
3. **`canonicality` + `data_classification` frontmatter deferred** to a dedicated ADR after the baseline is reviewed — fields only after ADR, exactly as the draft requires.
4. **New homes born on ingestion.** `_meta/consolidation/`, `02_OPERATIONS_OS/Cases/`, the Knowledge Action Register and the governance-manual docs enter [[Vault Map]] when real content lands — no empty placeholders.

Operating note: the programme runs **inside** the existing session ritual — one bounded goal per session, Orfeas in the loop, artifacts paired with narration. The tracer landing (Pass 4) remains the #1 content action; consolidation never displaces it.

## Links

- Raw source (immutable): `_sources/redoal — governed consolidation programme (external, 2026-07-19).md`
- Adoption: [[Architecture Decision Records|ADR-0007]] · state: [[Vault State Memory]] · queue: [[Capture Backlog]]
- Instruments: [[Vault Integrity Audit]] · `_meta/audits/STATE.md` ledger · `/repo-analysis` · [[Strategic Brainstorm Protocol]]
- First output: `docs/VAULT_BASELINE_2026-07-19.md` + `_meta/consolidation/` registries
- Doctrine above all of it: [[The Heart]]
