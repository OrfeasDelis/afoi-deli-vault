---
type: overlap_registry
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

# Overlap Registry

> [!abstract] What this is
> The [[Consolidation and Enrichment Programme]]'s Pass-2 register: every **genuine** overlap cluster found by the 2026-07-19 baseline (8 domain readers + audit-critic verification; evidence pack in `_meta/consolidation/data/`). Each cluster names its canonical owner and the merge/repair steps — **all proposal-only**. Nothing here executes until Orfeas approves the cluster's `orfeas_decision`, and deletion is never the first operation (cooling period per the programme's no-silent-deletion lifecycle). Companion: [[Canonical Note Registry]] · report: `docs/VAULT_BASELINE_2026-07-19.md`.

Legend — `overlap_type: exact | partial | naming | stale-copy | generated-copy | historical`. "Merge only when the same purpose or fact-ownership is genuinely duplicated — never to reduce note count."

---

## OV-01 · Supplier Note System ≡ Template - Supplier
- **notes:** `04_SUPPLIERS_AND_BRANDS/Supplier Note System.md` · `98_TEMPLATES/Template - Supplier.md`
- **overlap_type:** exact (diff = table-cell whitespace only; 0 inbound links on the content-wing copy — audit finding F3, open since 2026-06-17)
- **canonical_note:** [[Template - Supplier]] (templates belong in `98_TEMPLATES`)
- **unique_content_to_preserve:** none found
- **merge_steps:** none needed (no unique content) → mark `Supplier Note System` superseded
- **link_repair_steps:** none (zero inbound)
- **deletion_eligible_after:** one audit cycle post-supersession
- **orfeas_decision:** ✅ **approved retire (2026-07-19, §17-8) — EXECUTED same day:** supersession banner + `status: complete` applied to `Supplier Note System`; deletion eligible after one audit cycle. Both copies remain stale vs [[Supplier Research Workflow]] §A — OV-12 folds the vocabulary at Pass 4.

## OV-02 · The folder↔status derivation, stated three ways (two wrong the same way)
- **notes:** `02_OPERATIONS_OS/Folder State Machine.md` · `02_OPERATIONS_OS/Order Workflow 0-4.md` (§automation interpretation) · `02_OPERATIONS_OS/Operations Map.md` (§folders + §status)
- **overlap_type:** partial (same derivation logic restated; FSM + Ops Map versions contradict tracer corr. 8 — no DAILY in the formula)
- **canonical_note:** [[Order Workflow 0-4]] owns **status semantics** · [[Folder State Machine]] owns **folder derivation** · [[Operations Map]] reduces to summary + pointer (it already defers at :46)
- **unique_content_to_preserve:** FSM state diagram + edge cases; Order Workflow required-fields gates + WAIT rule; Ops Map end-to-end chain + SOP index
- **merge_steps:** Pass 4 Layer B rewrites the derivation ONCE (in FSM, per corr. 8: actionable→DAILY / held→ΠΡΩΤΟ + ΤΡΙΤΟ/ΒΑΛΤΟΣ) — the other two point
- **link_repair_steps:** repoint Daily SOP step 6 (see OV-03)
- **deletion_eligible_after:** n/a (all three stay; ownership split only)
- **orfeas_decision:** ✅ approved (2026-07-19, §17-8) — ownership split executes inside the tracer landing (Pass 4 Layer B)

## OV-03 · Daily Order Processing restates FSM + ΚΟΥΒΑΣ mechanics
- **notes:** `02_OPERATIONS_OS/Daily Order Processing SOP.md` (steps 3-4, 6) · [[Folder State Machine]] · [[Kouvas System]]
- **overlap_type:** partial (step 6 = verbatim-equivalent folder formula; steps 3-4 = paste-into-ΚΟΥΒΑΣ mechanics)
- **canonical_note:** FSM for derivation; Kouvas System for file mechanics; Daily SOP keeps only the daily routine
- **unique_content_to_preserve:** Daily SOP's classification table; its routine sequence
- **merge_steps:** at Layer B, replace restated logic with links
- **link_repair_steps:** internal links only
- **deletion_eligible_after:** n/a (note stays)
- **orfeas_decision:** ✅ approved (2026-07-19, §17-8) — rides the tracer landing (Pass 4 Layer B)

## OV-04 · The payment gate encoded three times — all as the model the tracer overturned
- **notes:** `02_OPERATIONS_OS/Delivery Scheduling SOP.md` (:18, :44-46) · `02_OPERATIONS_OS/Exception Handling Rules.md` (:28 CLIENT_BALANCE) · `02_OPERATIONS_OS/Finance and Credit Terms SOP.md` (:51)
- **overlap_type:** stale-copy (three hard-gate statements vs the soft, relationship-mediated gate over `paid ≥ delivered` — tracer corr. 28/31, Orfeas-confirmed)
- **canonical_note:** reconciled [[Finance and Credit Terms SOP]] owns the gate rule after Layer B; the other two reference
- **unique_content_to_preserve:** Delivery SOP's notification tone (on-doctrine); Exception rule's escalation slot
- **merge_steps:** Layer B rewrites the rule once (soft gate + invariant + credit-line exception), others point
- **link_repair_steps:** add references from the two non-owners
- **deletion_eligible_after:** n/a
- **orfeas_decision:** ✅ approved (2026-07-19, §17-8) — owner = the reconciled [[Finance and Credit Terms SOP]]; rewrite at Pass 4 Layer B

## OV-05 · SOP yaml field-blocks vs the CSV contract
- **notes:** 7 SOPs carrying pre-CSV yaml sketches (`Daily Order Processing SOP.md:93-108` · `Supplier PO Creation SOP.md:59-67` · `DTS and Loading Date SOP.md:19-34` · `Warehouse Receiving SOP.md:33-44` · `Finance and Credit Terms SOP.md:29-44` · `Order Workflow 0-4.md:25-71` · `Exception Handling Rules.md:33-42`) vs `97_CSV_SCHEMAS/*.csv` (the canonical stored contract per audit P0-2)
- **overlap_type:** stale-copy (the yaml predates the CSVs and now competes; ISS↔EHR vocabulary already drifted: `related_order_line` vs `affected_line`)
- **canonical_note:** the CSV headers (contract) + `03_DATABASE_DESIGN` notes (annotation); SOPs keep **procedure**, point to CSV for **fields**
- **unique_content_to_preserve:** any yaml field the CSVs lack becomes schema-diff input (most already covered by the 49-correction matrix)
- **merge_steps:** at Layer B, replace each yaml block with a link + keep procedure text
- **link_repair_steps:** SOP → schema-note links
- **deletion_eligible_after:** n/a (blocks replaced in place)
- **orfeas_decision:** ✅ approved pattern (2026-07-19, §17-8) — yaml blocks → links at Pass 4 Layer B; CSV stays the field contract

## OV-06 · Porcelain Stoneware prose: MOC residue vs atomic note (drifted copies)
- **notes:** `07_PRODUCT_KNOWLEDGE/Afoi Deli — Materials Intelligence.md:102-124` · `07_PRODUCT_KNOWLEDGE/Materials/Material - Porcelain Stoneware.md:84-152`
- **overlap_type:** stale-copy (MOC's own banner rule: prose stays only until split+verified — porcelain IS split, so the MOC section is residue; copies have drifted; the "To verify" list additionally lives in 3 homes incl. [[Capture Backlog]]:68)
- **canonical_note:** [[Material - Porcelain Stoneware]] (per the MOC's own rule + [[Materials Research Workflow]])
- **unique_content_to_preserve:** the MOC's separate "Decoration." paragraph (:114) — merge into the atomic note before thinning
- **merge_steps:** fold the MOC deltas into PS → cut MOC:102-124 to a pointer row; backlog row references PS's needs_check callout
- **link_repair_steps:** none expected (links target the atomic note already)
- **deletion_eligible_after:** n/a (section thinning, not file deletion)
- **orfeas_decision:** ✅ approved (2026-07-19, §17-8) — **gate cleared same review: Materials decision 1 = pattern approved (§17-12)**; the porcelain fold executes when Root B resumes (or at a convenient consolidation slot); the other 15 MOC sections are NOT overlaps (only home of that prose — protected)

## OV-07 · Pierre Vive facts triplicated (list prices · range shape · site absence)
- **notes:** `Collection - Kronos Pierre Vive.md` (:250-258 · :108 · :285) · `Supplier - Kronos.md` (:67-68 worked example · :86) · `Kronos — Collections Reference.md` (:35 · :38) · [[Vault State Memory]]:58 · [[Capture Backlog]]:66
- **overlap_type:** partial (derived restatements, not competing ownership — but copy-drift surface)
- **canonical_note:** list prices + range shape → the collection note; site-presence → the roster's "On afoideli.gr" column (its keep-or-strip is an existing open decision, VSM:77); backlog holds only the action
- **unique_content_to_preserve:** Kronos dossier's worked example (mark as derived-from-PV, don't delete)
- **merge_steps:** annotate derivations; thin VSM:58 to a pointer (also a confidentiality row — see OV-08)
- **link_repair_steps:** pointer links to the collection note
- **deletion_eligible_after:** n/a
- **orfeas_decision:** ✅ approved canonical assignments (2026-07-19, §17-8; VSM:58 thinned to a pointer same day) + ✅ roster column **KEPT** as the canonical site-presence surface, pilot-scope (§17-11 — settled-line added to the roster; VSM open-decision ticked)

## OV-08 · Kronos confidential commercial terms outside their canonical home
- **notes (locations only — values not restated here):** canonical `Supplier - Kronos.md:52-78` §Pricing → restated at `Supplier Enrichment Queue.md:53` · `10_FINANCE_AND_MANAGEMENT/Cost & Quote Build.md:43-59` · `10_FINANCE_AND_MANAGEMENT/Credit and Due Date Calendar.md:35` · `Vault State Memory.md:58 + :88 + :92` · historical session logs (2026-06-17c — historical class, acceptable)
- **overlap_type:** partial (confidentiality-duplication — programme governance rule B + F; move-never-copy)
- **canonical_note:** [[Supplier - Kronos]] §Pricing (danger-classified)
- **unique_content_to_preserve:** Cost & Quote Build's cost-chain **method** (legitimate derived home — the question is restate-vs-reference)
- **merge_steps:** redact Enrichment Queue :53 + VSM rows to pointers; Cost & Quote Build → REVIEW (reference-not-restate, or declare it a second controlled home)
- **link_repair_steps:** pointers to §Pricing
- **deletion_eligible_after:** n/a (redaction, not deletion)
- **orfeas_decision:** ✅ **ruled reference-only (2026-07-19, §17-6) — EXECUTED same day:** CQB's worked figures, the Enrichment Queue :53 restatement, and the VSM rows (:58 entry · §7 revenue line · the 2026-06-17c footer fragment) all redacted to existence-naming pointers; [[Supplier - Kronos]] §Pricing is the sole holder. The revenue figure single-sourced to [[Afoi Deli Master Profile]].

## OV-09 · Current Priorities vs Capture Backlog (the banned parallel queue)
- **notes:** `00_COMMAND_CENTER/Current Priorities.md` (frozen 2026-06-07, `review_frequency: weekly` never honored, 1 inbound from historical README_START_HERE) · [[Capture Backlog]] (the ONE queue, ADR-0007 rec. 2)
- **overlap_type:** historical (a day-one steering voice frozen in time)
- **canonical_note:** [[Capture Backlog]]
- **unique_content_to_preserve:** any theme not already in the backlog (its Priority 6 personal-operator strand overlaps [[Strategic Axes]] + backlog Priority 3 — diff before merging)
- **merge_steps:** MERGE_INTO(Capture Backlog) surviving themes → mark residual historical
- **link_repair_steps:** repoint the README_START_HERE reference on its rewrite
- **deletion_eligible_after:** one audit cycle post-merge
- **orfeas_decision:** ✅ ruled (2026-07-19, §17-3): **careful line-by-line diff** — surviving themes merge into [[Capture Backlog]]; anything reading authored comes back to Orfeas before absorbing; residual marked historical. Executes at Pass 3.

## OV-10 · Question registers: Open Questions vs Questions To Resolve vs the future Knowledge Action Register
- **notes:** `14_AI_COLLABORATION/Open Questions.md` (vault/collab; stale-but-functional) · `00_COMMAND_CENTER/Questions To Resolve.md` (business; dead — holds tracer-answered rows :20/:22 unmarked) · Knowledge Action Register (to be born per the charter, gaps-only)
- **overlap_type:** partial (declared split, one side unmaintained, a third surface coming)
- **canonical_note:** [[Open Questions]] for vault/collaboration questions; the **Knowledge Action Register** (at birth) for operational knowledge gaps
- **unique_content_to_preserve:** QTR's still-open rows (several are answered by the tracer — annotate which)
- **merge_steps:** annotate tracer-answered rows now → MERGE_INTO(Knowledge Action Register) at its birth → mark QTR historical
- **link_repair_steps:** Home Dashboard :44-47 repoint (see OV-13)
- **deletion_eligible_after:** one audit cycle after the Register absorbs it
- **orfeas_decision:** ✅ disposition approved (2026-07-19, §17-8); the row-by-row confirmation of tracer-answered QTR items happens with Orfeas during the Pass 3 annotation (still owed — deliberately not guessed)

## OV-11 · The session ritual defined in three places
- **notes:** `CLAUDE.md` §§1/6/8 (canonical, hook-backed) · `14_AI_COLLABORATION/Session Protocol.md` (drifted mirror: START omits The Heart + Capture Backlog; END omits the /repo-analysis refresh; :46 carries the challenged waterfall) · `README_START_HERE.md:35-46` (historical parallel boot path)
- **overlap_type:** stale-copy (Protocol) + historical (README_START_HERE)
- **canonical_note:** CLAUDE.md
- **unique_content_to_preserve:** Session Protocol's working-modes callout (:13, current)
- **merge_steps:** sync Protocol to CLAUDE §1/§8 **or** slim it to a pointer; README_START_HERE handled by its planned rewrite (F5)
- **link_repair_steps:** none
- **deletion_eligible_after:** n/a
- **orfeas_decision:** ✅ ruled **slim pointer** (2026-07-19, §17-5): CLAUDE.md §§1/6/8 is the one authoritative ritual text; Session Protocol slims to a pointer keeping only its unique working-modes callout. Executes at Pass 3.

## OV-12 · The dossier slot vocabulary defined three ways
- **notes:** `Supplier Master Index.md:55-77` (18-item checklist) · `Supplier Enrichment Queue.md:32-39` (6 dimensions) · `Supplier Research Workflow.md:86-99` (the contract the 5 live dossiers actually follow)
- **overlap_type:** partial (role separation otherwise clean: roster / blank-finder / authoring pipeline)
- **canonical_note:** [[Supplier Research Workflow]] §A owns the slot contract
- **unique_content_to_preserve:** Master Index's intelligence checklist (superset items fold into the workflow)
- **merge_steps:** fold definitional lists into the workflow; index + queue keep pointers
- **link_repair_steps:** pointers
- **deletion_eligible_after:** n/a
- **orfeas_decision:** ✅ approved (2026-07-19, §17-8) — [[Supplier Research Workflow]] §A owns the slot contract; folds at Pass 4 (settles OV-01's reconciliation direction)

## OV-13 · Hub links routing to dead surfaces
- **notes:** `00_COMMAND_CENTER/Home Dashboard.md:44-47` (routes exclusively to Weekly Review [to-be-dormant] · Decision Log [empty] · Questions To Resolve [stale] · Inbox [dormant]; links neither the backlog nor the programme) · `14_AI_COLLABORATION/Collaboration Home.md` (omits Capture Backlog; :46 names Roadmap a capture surface)
- **overlap_type:** stale-copy (navigation pointing at superseded steering)
- **canonical_note:** n/a (link repair, not merge)
- **merge_steps:** none
- **link_repair_steps:** Home Dashboard → point at Capture Backlog + the programme; Collaboration Home → add the queue link, correct :17/:46
- **deletion_eligible_after:** n/a
- **orfeas_decision:** ✅ approved (2026-07-19, §17-8) — **EXECUTED same day** (§16-C): Home Dashboard's dead block → "Queue & review" (Capture Backlog + programme + VSM, dormant surfaces footnoted); Collaboration Home gained the queue in "Start here", corrected :17 (Roadmap pre-pivot flag) + :46 (capture surfaces).

## OV-14 · Sequencing voices: Roadmap vs the programme's arc vs the backlog
- **notes:** `14_AI_COLLABORATION/Roadmap.md` (waterfall phases, phantom Builder's Manual :13, Phase 0 "IN PROGRESS" contradicted by 19 sessions) · [[Consolidation and Enrichment Programme]] (90-day arc) · [[Capture Backlog]] (ranked queue)
- **overlap_type:** historical (Roadmap frozen pre-pivot)
- **canonical_note:** [[Capture Backlog]] (execution) + the programme charter (arc); Roadmap's fate is the open fork
- **unique_content_to_preserve:** Roadmap's phase framing IF Orfeas wants it rewritten instance-first
- **merge_steps:** file the instance-first ADR (due — filing condition arrived 2026-07-18) → then rewrite Roadmap or MARK_HISTORICAL
- **link_repair_steps:** CLAUDE §1 + Session Protocol boot-reads adjust on whichever fork
- **deletion_eligible_after:** never (historical value); archival only
- **orfeas_decision:** ✅ ruled **REWRITE instance-first** (2026-07-19, §17-2), after ADR-0008 files. Roadmap stays a live boot note; phantom Builder's-Manual claim struck same day (§16-C); a "rewrite pending" banner marks the interim. Executes at Pass 3.

## OV-15 · "Architecture. Surfaces. Quiet precision." — dual ownership
- **notes:** `01_COMPANY_CORE/Afoi Deli Master Profile.md:19` · `01_COMPANY_CORE/Brand DNA.md:12+35` (no cross-link either way; both zero-wikilink notes) · echoed `11_EXPANSION_AND_VENTURES/Personal Brand and Thought Leadership.md:29`
- **overlap_type:** exact (the same positioning line, two claimed owners)
- **canonical_note:** proposed [[Brand DNA]] (voice/positioning is its purpose)
- **unique_content_to_preserve:** n/a (identical line)
- **merge_steps:** gated on the 2026-06-07-stratum decision (adopt vs archive — see baseline report §Decisions)
- **link_repair_steps:** cross-link the two notes regardless
- **deletion_eligible_after:** n/a
- **orfeas_decision:** ✅ ruled under the stratum split (2026-07-19, §17-1): [[Brand DNA]] is the canonical home (ownership callout + cross-links applied same day); the line itself awaits Orfeas's re-authoring or explicit claim (voice layer of the split).

## OV-16 · Customer-type criteria — contested framing
- **notes:** `01_COMPANY_CORE/Business Model Map.md` ("Customer types" table — marketing framing) · `05_SALES_AND_CLIENT_EXPERIENCE/The Selection Engine.md` §4 (real reads; itself flags the Map as "marketing copy, not real selection rules" :99/:154; its suggested reconciliation link :162 never applied)
- **overlap_type:** partial (adjacent concepts, contested authority)
- **canonical_note:** [[The Selection Engine]] for how clients are actually read; Business Model Map for public-facing segmentation IF retained after the stratum decision
- **unique_content_to_preserve:** both framings until Orfeas rules
- **merge_steps:** none until the stratum decision; then apply Selection Engine :162's own reconciliation
- **link_repair_steps:** add the missing Map→Engine link either way
- **deletion_eligible_after:** n/a
- **orfeas_decision:** ✅ ruled under the stratum split (2026-07-19, §17-1): [[The Selection Engine]] canonical for how clients are actually read; the Map's table stays as facts-layer public-facing segmentation; the missing Map→Engine link + Engine :162's own reconciliation apply at Pass 3/4.

## OV-17 · Conduit relationship facts retold in dossiers
- **notes:** `Conduit - Plus Interiors.md:46-48` (founding-act story) vs `Supplier - Cielo.md:26+30` (detailed retelling) · `Conduit - Filon IKE.md:36-37` (character) vs `Supplier - Mutina.md:37+40+83`
- **overlap_type:** partial (the power-geometry warning pattern elsewhere is compliant reference-summary — these two retell with detail)
- **canonical_note:** the conduit notes
- **unique_content_to_preserve:** dossier-side detail not in the conduit note (fold up before trimming)
- **merge_steps:** trim dossier retellings to linked lines
- **link_repair_steps:** links already exist
- **deletion_eligible_after:** n/a
- **orfeas_decision:** ✅ approved **with reservation** (2026-07-19, §17-8): trims proceed at execution time, but the **Cielo founding-act passage goes back to Orfeas first** — if it is deliberate doctrine-echo, it stays. Nothing trimmed yet.

---

## Explicitly NOT overlaps (charitable-read clearances)
- The 15 un-migrated MOC material sections — only home of that prose (working-draft state by design).
- `_sources/` seed drafts duplicating their MOC — immutable evidence, by design.
- Power-geometry warning restated as summary-plus-link across 4 dossiers + index — compliant "reference from many, maintain in one."
- [[Inbox]] — dormant by decision, correctly bannered (the model for Weekly Review).
- Generated `docs/` restating note content — that IS generation (the two figure/name leaks are a generator-policy defect, not overlap).
- `Kronos — Catalogue & Asset Ingestion` vs backlog pointer — plan-note + queue-pointer, correct hierarchy.
- Brand Master Index vs MOC brand→material appendix — zero material content in the index; no overlap.

*Registry born 2026-07-19 from the baseline run. Maintained by consolidation sessions; every executed cluster gets its decision + date recorded here.*
