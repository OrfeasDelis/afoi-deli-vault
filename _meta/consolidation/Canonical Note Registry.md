---
type: canonical_registry
created: 2026-07-19
updated: 2026-07-19
status: active
confidence: verified
owner: Orfeas Delis
tags:
  - consolidation
  - registry
  - meta
---

# Canonical Note Registry

> [!abstract] What this is
> The map of **which note owns which truth** — the [[Consolidation and Enrichment Programme]]'s "one fact, one canonical owner" principle made explicit, from the 2026-07-19 baseline. A fact may be *referenced* from many notes; it is *maintained* in exactly one. `state` marks the domain's health: **clean** (owner settled, references compliant) · **duplicated** (restatements to repair — see [[Overlap Registry]]) · **contested** (two claimants — Orfeas decides) · **no-owner** (truth exists, no canonical home) · **hollow** (declared owner is empty of the promised content). Proposal-only; companion: [[Overlap Registry]] · report: `docs/VAULT_BASELINE_2026-07-19.md`.

## Steering & governance

| Truth domain | Canonical owner | Competitors / restatements | State |
|---|---|---|---|
| Current state ("where we are") | [[Vault State Memory]] | internal defects only (phantom claim :46, overgrown tail) | clean* |
| Execution priority — the ONE queue | [[Capture Backlog]] | `Current Priorities` (frozen 2026-06-07) · [[Roadmap]] phase voice | duplicated (OV-09, OV-14) |
| Session ritual | `CLAUDE.md` §§1/6/8 | [[Session Protocol]] (drifted mirror) · `README_START_HERE` §boot (historical) | duplicated (OV-11) |
| Architecture decisions | [[Architecture Decision Records]] | — | clean |
| Business decisions | [[Decision Log]] (declared) | practice: ADR Consequences · session logs · backlog annotations | hollow — activate or retire (Orfeas) |
| Vault/collaboration open questions | [[Open Questions]] | `Questions To Resolve` (dead) · future Knowledge Action Register | duplicated (OV-10) |
| Consolidation/enrichment frame | [[Consolidation and Enrichment Programme]] | raw redoal draft in `_sources/` (immutable, subordinated) | clean |
| Folder index | [[Vault Map]] | — (`scripts/` row pending) | clean |
| Working hub | [[Collaboration Home]] | [[Home Dashboard]] (00-wing hub, dead links) | duplicated (OV-13) |
| Repo front page (generated) | `README.md` marker block via `/repo-analysis` | — | clean |
| History | `Sessions/` + `Brainstorms/` logs | VSM §5 tail (overgrown digest) | duplicated (thin the tail) |

*clean as owner; carries fix-in-place defects (baseline report §4).

## Operations

| Truth domain | Canonical owner | Competitors / restatements | State |
|---|---|---|---|
| Order-lifecycle ground truth | [[Order Lifecycle — Ground-Truth Capture]] | — (evidence class; wins over SOPs until reconciled) | clean |
| Line status 0–4 semantics | [[Order Workflow 0-4]] | Operations Map · FSM · Daily SOP · Orders/Order Lines Schemas (annot.) | duplicated (OV-02) |
| Folder/macro-state semantics (DAILY/ΠΡΩΤΟ/ΔΕΥΤΕΡΟ/ΠΡΟΣ ΠΑΡΑΔΟΣΗ/ΤΡΙΤΟ/ΒΑΛΤΟΣ) | [[Folder State Machine]] (proposed, post-reconciliation) | Order Workflow §automation · Operations Map | no-owner today → FSM after Layer B (OV-02) |
| ΚΟΥΒΑΣ mechanics | [[Kouvas System]] | Operations Map :34 · Daily SOP · PO SOP | duplicated (OV-03) |
| Proforma verification | [[Proforma Checking SOP]] | Exception Rules :23-24 echo | clean owner, wrong content (P1 debt) |
| Payment gate / release rule | [[Finance and Credit Terms SOP]] (proposed, post-reconciliation) | Delivery Scheduling SOP · Exception Rules — all three currently state the overturned hard gate | no-owner today (OV-04) |
| Inbound logistics chain (ELXIS, consolidation, channels) | — | nearest surface: DTS and Loading Date SOP | no-owner — Layer B decides (absorb vs new note) |
| Exception taxonomy | [[Exception Handling Rules]] (meanings) + `issues_exceptions.csv` (values) | vocabulary drift between the two | contested — declare split at Layer B |
| Stored data contract (fields) | `97_CSV_SCHEMAS/*.csv` (contract) + `03_DATABASE_DESIGN/*` (annotation) | 7 SOP yaml blocks (pre-CSV sketches) | duplicated (OV-05) |
| Supplier commercial terms | supplier dossiers, private sections ([[Supplier - Kronos]] §Pricing) | Enrichment Queue :53 · Cost & Quote Build · Credit Calendar · VSM | duplicated + confidential (OV-08) |
| Cost-to-quote method | [[Cost & Quote Build]] | — (its *figures* belong to the dossier — OV-08) | clean method / contested figures |
| Margin policy | Orfeas (deliberately un-encoded; [[Cost & Quote Build]] holds the frame) | — | clean (by design) |

## Doctrine & identity

| Truth domain | Canonical owner | Competitors / restatements | State |
|---|---|---|---|
| The code, maxims, lineage | [[The Heart]] | healthy hub-and-spoke (all cite it) | clean |
| Business expression of the code | [[Afoi Deli — Operating Doctrine]] | healthy | clean |
| Uplift-engine moat | [[Afoi Deli — Operating Doctrine]] :24-33 | 10+ compliant linked restatements | clean |
| Selection craft + conversion figure | [[The Selection Engine]] | generated suite existence-names only (correct) | clean |
| "Business and personal are one fabric" | `CLAUDE.md:3` (de facto) | 3 notes misattribute it to The Heart | contested — decide home (Orfeas) |
| North-star sentence | `Afoi Deli Master Profile:80` | quoted by README :132 + VISION :11 | contested — weakest-authorship note owns the most-quoted line (stratum decision) |
| Brand voice / positioning line | [[Brand DNA]] (proposed) | Master Profile :19 (dual owner, no cross-link) | contested (OV-15, stratum decision) |
| Customer-type reads | [[The Selection Engine]] §4 (real reads) | Business Model Map table (marketing framing) | contested (OV-16) |
| OS layer model (five-layer) | [[Vault State Memory]] §1 + charter | Strategic Axes :61-65 (stale 3-layer) | duplicated (fix Axes at stratum decision) |
| The people (Kostas, Chrysoula, Ektoras, Eleni) | [[People and Roles Map]] (declared by CLAUDE §2 + The Heart aliases) | — | hollow — only functional roles exist; people notes are backlog P1 |
| Journal / wellness | [[Journal]] + `15_PERSONAL_LIFE` | — | clean (author-by-invitation; opaque to consolidation) |
| Held-in-reserve material | *deliberate absence* (The Heart :96-97) | propagation ceiling: Session 2026-06-14 :51/:81 | clean — protect the absence |

## Knowledge layers

| Truth domain | Canonical owner | Competitors / restatements | State |
|---|---|---|---|
| Material-class knowledge | `Material - <Class>` atomic notes ([[Materials Schema]] contract) | MOC porcelain residue (drifted copy) | duplicated for porcelain (OV-06); 15 sections legitimately MOC-resident |
| Collection instances | `Collection - <Name>` notes ([[Collection Schema]]) | — (1 exists: Pierre Vive) | clean |
| Pierre Vive line facts | [[Collection - Kronos Pierre Vive]] | Kronos dossier worked example · roster row · VSM | duplicated (OV-07) |
| Brand → material mapping | Materials Intelligence MOC appendix | — (Brand Master Index carries none) | clean |
| Supplier dossier slot vocabulary | [[Supplier Research Workflow]] §A | Master Index checklist · Enrichment Queue dimensions · Template - Supplier | duplicated (OV-12, OV-01) |
| Supplier relationship / conduit truth | [[Conduit - Plus Interiors]] · [[Conduit - Filon IKE]] | dossier retellings (Cielo, Mutina) | duplicated (OV-17) |
| Site-presence per Kronos line | [[Kronos — Collections Reference]] "On afoideli.gr" column | PV note · backlog | duplicated (OV-07; column's fate = open decision VSM:77) |
| Source evidence | `_sources/` folders (immutable) + future Supplier Source Manifest | manifest does not exist yet | no-owner for source *metadata* (manifest is the programme's gate for the sweep redo) |
| Generated repo profile | `docs/` suite via `/repo-analysis` | two stale companions + two leak lines (generator-policy defects) | clean owner, defective instances |

## No-owner truths surfaced by the baseline (need homes, not files yet)

- The **inbound logistics chain** as an entity (ELXIS · consolidation centre · Patras → Aspropyrgos → Peristeri · channel split) — Layer B decides its home.
- **Source metadata** (hashes, editions, rights, confidentiality class) — the future `Supplier Source Manifest`.
- **Operational knowledge gaps** as a coordinated register — the future `Knowledge Action Register` (gaps only, never a second queue).
- The **ΕΡΓΟΣΤΑΣΙΑ archive census** (~123 supplier names, currently only as empty dirs + the stash) — belongs in the manifest/roster at sweep-redo time; capture before any dir cleanup.
- The **instance-first sequencing doctrine** — its ADR is due; until filed, the waterfall texts contradict practice.

*Registry born 2026-07-19 from the baseline run. Update rows as owners are decided; a row leaves "duplicated" only when the Overlap Registry cluster executes.*
