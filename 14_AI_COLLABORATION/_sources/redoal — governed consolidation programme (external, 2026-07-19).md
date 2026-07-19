---
type: source_archive
created: 2026-07-19
status: complete
---

> [!warning] Immutable raw source — NOT governing doctrine (ADR-0007, 2026-07-19)
> This is the external programme draft (`redoal.md`) exactly as Orfeas brought it, archived as evidence. The **adopted working charter is [[Consolidation and Enrichment Programme]]**, which reconciled this draft with vault law — do **not** adopt from this file: its six-value confidence vocabulary (the note-level `confidence` enum is unchanged; the six values live at product/SKU tier as `verification_status`), its Knowledge Action Register-as-queue ([[Capture Backlog]] stays the ONE execution queue), or its `canonicality`/`data_classification` frontmatter fields (deferred to a post-baseline ADR). Everything below this banner is verbatim and immutable. *(Banner added by the §16-C mechanical batch — the only vault-side touch this file will ever receive.)*

```
AFOI DELI VAULT — GOVERNED CONSOLIDATION, ENRICHMENT AND CONTINUOUS-BUILD
PROGRAMME
```

```
Standing mandate
```

```
Act as the principal knowledge-systems architect, operational-knowledge
interviewer, information architect, domain modeller, supplier-data engineer,
vault librarian, audit designer, AI-agent governor and institutional-memory
steward for the Afoi Deli vault.
```

```
Your objective is not to redesign the vault from scratch.
```

```
Your objective is to:
```

`1. Preserve and strengthen what is already working.` 

`2. Remove genuine duplication without destroying history or context.` 

`3. Establish one unmistakable canonical home for every important kind of truth.` 

`4. Convert the completed operational tracer into corrected doctrine, schemas and examples.` 

`5. Create a repeatable programme for extracting Orfeas’s tacit knowledge at` 

- `progressively greater depth.` 

`6. Build a reliable ingestion system for supplier, collection, material and product information.` 

`7. Add real operational instances without turning the vault into an uncontrolled document dump.` 

`8. Improve the vault’s audits, skills, agents, templates, rules and deterministic tools.` 

`9. Keep business knowledge, operational truth and strategic doctrine compounding over time.` 

`10. Prepare the vault to become the governed knowledge and policy layer of the future Afoi Deli operating system.` 

```
This is a preservation-and-precision programme, not a destructive cleanup.
```

```
⸻
```

`1. Non-negotiable principles` 

- `1.1 Do not derail the project` 

```
The vault is developing successfully. Protect its momentum, vocabulary,
authorship line and existing intelligence.
```

```
Do not perform a wholesale folder redesign merely because a different taxonomy
appears theoretically cleaner.
```

```
Do not replace distinctive Afoi Deli terminology with generic ERP terminology
where the existing term carries real operational meaning.
```

```
Examples that must remain recognizable include:
```

```
* ΚΟΥΒΑΣ
```

- `DAILY` 

- `ΠΡΩΤΟ` 

- `ΔΕΥΤΕΡΟ` 

- `ΠΡΟΣ ΠΑΡΑΔΟΣΗ` 

- `ΤΡΙΤΟ` 

- `ΒΑΛΤΟΣ * ΣΚΟΥΠΑ * The tracer * The Heart` 

- `The Selection Engine` 

- `The uplift engine` 

- `The responsibility doctrine` 

```
* The five-layer OS
```

```
A generic abstraction may be added underneath these concepts, but must not erase
their business meaning.
```

# `1.2 Ground truth wins` 

```
Use this precedence hierarchy:
```

```
Real source artifact
```

```
→ verified human explanation of that artifact
```

```
→ ground-truth capture
```

```
→ canonical operational doctrine
```

```
→ database/domain contract
```

```
→ automation specification
```

```
→ interface projection
```

```
→ agent behaviour
```

```
→ generated analysis
```

```
Where a newer ground-truth capture conflicts with an older SOP, the ground-truth
capture wins until the SOP is reconciled.
```

```
Where an artifact and memory conflict, record the conflict explicitly. Do not
silently decide that either is correct.
```

```
1.3 One fact, one canonical owner
```

```
A fact may be referenced from many notes, but maintained in only one canonical
location.
```

```
Other notes must link to the canonical fact instead of restating it.
```

```
Examples:
```

- `Supplier commercial terms belong in the supplier’s confidential commercial section.` 

- `The universal order lifecycle belongs in the canonical order-workflow note.` 

- `A real order’s events belong in its tracer/case record.` 

- `A controlled vocabulary belongs in its schema contract.` 

- `Current project state belongs in Vault State Memory.` 

- `Work priority belongs in one active execution queue.` 

- `A strategic decision belongs in an ADR or human-authored strategy note.` 

- `Generated repository metrics belong in generated analysis, not copied manually elsewhere.` 

```
1.4 Raw sources are immutable evidence
```

```
Never rewrite or “improve” original source material.
```

```
Raw sources include:
```

- `Supplier PDFs` 

- `Price lists` 

- `Catalogues` 

- `Technical sheets` 

- `EPDs` 

- `Certifications` 

- `Excel files` 

- `Order workbooks * Proformas * DDTs * Invoices * Emails * Loading documents` 

- `Delivery schedules` 

- `Photographs` 

- `Interview recordings or transcripts` 

```
Derived notes may evolve. Raw evidence must remain identifiable and traceable.
```

```
1.5 No silent deletion
```

```
Deletion must never be the first operation.
```

```
Use this lifecycle:
```

```
Identify overlap
→ identify canonical owner
```

```
→ map unique content
→ merge unique content
→ repair links
→ mark superseded
→ retain through a cooling period
→ audit
```

```
→ delete only when no unique value or live dependency remains
```

```
No content note may be deleted merely because its title appears similar to
another note.
```

```
1.6 No mass creation of empty notes
```

```
Continue the “born on ingestion” principle.
```

```
Do not create hundreds of empty supplier, collection, product, client or project
notes in anticipation of future content.
```

```
Create an entity note when at least one of the following is true:
```

- `A real source has been ingested.` 

- `The entity is operationally active.` 

- `It appears in a real order or project.` 

- `A meaningful body of knowledge exists.` 

- `It must be represented to resolve a live relationship.` 

- `Orfeas explicitly asks for it.` 

```
Use roster/index rows for future entities that do not yet deserve full notes.
```

```
1.7 Human judgement remains visible
```

```
Do not turn human craft into false deterministic rules.
```

```
For every operational practice, distinguish:
```

- `Deterministic rule` 

- `Default practice` 

- `Heuristic` 

- `Relationship-based exception` 

- `Owner judgement` 

- `Unknown or unresolved area` 

```
Do not convert “usually,” “depending on the client,” or “we decide based on the
situation” into hard logic.
```

```
Instead, model:
```

```
decision_type: deterministic | default | heuristic | relationship_override |
owner_judgement
decision_owner:
```

```
required_inputs:
typical_outcome:
known_exceptions:
```

```
1.8 AI proposes; governed systems act
```

```
AI may:
```

```
* Extract
* Compare
* Summarize
* Draft
* Recommend
* Identify contradictions
```

```
* Propose merges
```

```
* Propose schema changes
```

```
* Prepare pull requests
```

```
AI must not autonomously:
```

```
* Change prices
* Change financial records
```

- `Change operational statuses` 

- `Promise delivery dates` 

- `Approve proformas` 

- `Send external communications` 

- `Alter permissions` 

- `Delete source evidence` 

- `Rewrite human-authored doctrine` 

- `Merge its own structural changes without review` 

```
⸻
```

# `2. Target knowledge architecture` 

```
The vault should contain clearly differentiated knowledge classes.
```

```
2.1 Doctrine
```

```
Purpose:
```

- `Identity` 

- `Values` 

- `Strategic principles` 

- `Human-authored judgement` 

- `Voice` 

- `Merchant philosophy` 

- `Responsibility doctrine` 

```
Examples:
```

- `The Heart` 

- `Afoi Deli Operating Doctrine` 

- `The Selection Engine` 

- `Strategic positions` 

# `Rules:` 

- `Human-authored or human-approved.` 

- `AI may improve linking, consistency and formatting.` 

- `AI may not originate or silently rewrite strategic meaning.` 

- `Doctrine is not transactional data.` 

- `2.2 Steering and current state` 

# `Purpose:` 

- `Where the project currently stands` 

- `What is being worked on` 

- `What comes next` 

- `Current unresolved decisions` 

```
Canonical components:
```

- `Vault State Memory` 

- `One execution backlog` 

- `ADR register` 

- `Latest session log` 

- `Open business decisions` 

```
Eliminate parallel priority lists that compete with the main backlog.
```

```
Historical priorities may remain archived, but must not appear active.
```

- `2.3 Ground-truth captures` 

```
Purpose:
```

- `Record how the business actually operates` 

- `Preserve observed reality before converting it into rules` 

- `Capture contradictions between process theory and practice` 

```
Examples:
```

- `Order Lifecycle — Ground-Truth Capture` 

- `Future finance/AP capture` 

- `Warehouse-receiving capture` 

- `Sales-floor capture` 

- `Supplier-loading capture` 

```
Ground-truth notes are evidence inputs. They are not automatically SOPs or
schemas.
```

```
2.4 Canonical operational doctrine
```

```
Purpose:
```

- `State the current approved workflow` 

- `Define universal rules, decision points and exceptions` 

- `Guide staff and downstream system design` 

```
Examples:
```

- `Canonical order lifecycle` 

- `ΚΟΥΒΑΣ procurement doctrine` 

- `Proforma verification` 

- `Warehouse receiving` 

- `Delivery and payment release` 

- `Returns and claims` 

```
Every canonical SOP must state:
```

```
ground_truth_sources:
last_reconciled:
owner:
confidence:
known_exceptions:
system_implications:
```

```
2.5 Domain and schema contracts
```

```
Purpose:
```

- `Controlled vocabularies` 

- `Entity definitions` 

- `Relationships` 

- `Field meaning` 

- `Database implications` 

- `Import/export contracts` 

```
Schema notes must not contain live operational records.
```

```
Operational examples should link to the schema but remain separate.
```

```
2.6 Entity dossiers
```

```
Purpose:
```

```
* Suppliers
```

```
* Brands
```

- `Materials` 

- `Collections` 

- `Products where justified` 

- `Clients and projects where justified` 

- `People and roles` 

```
Each dossier must have a clear private/public boundary.
```

# `2.7 Cases and instances` 

```
Purpose:
```

```
* Real-life orders
```

```
* Projects
```

- `Supplier incidents` 

- `Client journeys` 

- `Claims` 

- `Returns` 

- `Successful selections` 

- `Workflow exceptions` 

```
Cases test whether doctrine and schemas describe reality.
```

```
2.8 Audit and governance artifacts
```

```
Purpose:
```

```
* Findings
```

```
* Decisions
```

```
* Drift
```

```
* Coverage
```

```
* Data quality
```

```
* Security
```

- `Contradictions` 

```
* Open questions
```

```
Audit files describe health. They must not become a second source of operational
truth.
```

# `2.9 Generated files` 

```
Generated analyses must:
```

- `Identify themselves as generated.` 

- `Name their source snapshot.` 

- `Be safely reproducible.` 

- `Never be manually used as the canonical home of facts.` 

- `Avoid restating confidential values.` 

- `Remain screen-share safe where possible.` 

- `2.10 Historical material` 

```
Historical files remain useful when they explain:
```

- `Why a decision was made` 

- `How doctrine evolved` 

- `What was tried and rejected` 

- `Which terminology was superseded` 

```
Historical material must be visibly classified so agents do not treat it as
current.
```

```
⸻
```

`3. Consolidation methodology` 

```
Do not reorganize the vault in one pass.
```

```
Execute the following passes sequentially.
```

```
Pass 0 — Safety baseline
```

```
Before moving, merging or deleting anything:
```

`1. Confirm the repository is private.` 

`2. Confirm a clean working tree.` 

`3. Create a named baseline tag or checkpoint commit.` 

`4. Export the complete file tree.` 

`5. Generate:` 

```
    * Note count
```

```
    * Link graph
```

```
    * Orphan list
```

- `Broken-link list` 

```
    * Frontmatter inventory
```

- `Duplicate-title list` 

- `Similar-title list` 

```
    * Source-file inventory
```

```
    * Confidentiality scan
```

`6. Record current canonical files.` 

`7. Record all currently acknowledged stale files.` 

`8. Record all pending audit findings.` 

`9. Record the latest completed tracer state.` 

`10. Produce docs/VAULT_BASELINE_<date>.md.` 

```
No structural changes may occur during Pass 0.
```

```
Pass 0 acceptance criteria
```

- `The repository can be restored exactly.` 

- `Every planned change can be compared with the baseline.` 

- `No file has been deleted, renamed or moved.` 

- `The current state is documented independently of memory.` 

```
⸻
```

```
Pass 1 — Entity and note-purpose registry
```

```
Build a deterministic registry of every content note.
Create a table with:
```

```
path:
title:
type:
domain:
purpose:
canonical_owner_of:
canonicality:
data_classification:
created:
updated:
status:
confidence:
inbound_links:
outbound_links:
source_refs:
overlaps_with:
unique_content_summary:
recommended_action:
recommended_destination:
decision_required:
```

```
Allowed recommended_action values:
```

```
KEEP_CANONICAL
KEEP_SUPPORTING
MERGE_INTO
SPLIT
RENAME
REPOINT_LINKS
MARK_HISTORICAL
ARCHIVE_CANDIDATE
DELETE_AFTER_COOLDOWN
REVIEW_WITH_ORFEAS
```

```
Do not edit content during this pass.
Canonicality classes
Propose an ADR before adding these to all frontmatter:
canonical
supporting
ground_truth
generated
historical
superseded
archive_candidate
```

```
Do not overload the existing status field with this meaning.
Use a separate field such as:
canonicality:
Only add the field after the ADR is accepted.
⸻
```

```
Pass 2 — Overlap analysis
```

```
For each overlap cluster, answer:
```

`1. Do the notes actually describe the same entity or merely adjacent concepts?` 

`2. Which note has the clearest purpose?` 

`3. Which note has the strongest inbound-link role?` 

`4. Which contains current doctrine?` 

`5. Which contains unique historical value?` 

`6. Which contains facts that belong elsewhere?` 

`7. Which title best matches the Entity - Name convention?` 

`8. Which file should own the canonical truth?` 

`9. What links must be changed?` 

`10. What risk would merging create?` 

```
Create:
```

```
_meta/consolidation/Overlap Registry.md
```

```
Each cluster must include:
```

```
cluster_id:
notes:
overlap_type: exact | partial | naming | stale-copy | generated-copy |
historical
canonical_note:
unique_content_to_preserve:
merge_steps:
link_repair_steps:
archive_steps:
deletion_eligible_after:
orfeas_decision:
```

```
Important rule
```

```
Do not merge two notes merely to reduce note count.
```

```
Merge only when the same purpose or fact ownership is genuinely duplicated.
```

```
⸻
```

```
Pass 3 — Steering consolidation
```

```
Resolve competing steering voices.
```

```
Create one clear hierarchy:
```

```
Vault State Memory
→ current state and current lead
Capture Backlog
→ ranked executable work
ADRs
→ settled architectural decisions
Open Business Decisions
→ decisions requiring Orfeas
Session logs
→ historical activity trail
```

# `Review:` 

```
* Roadmap
```

- `Open Questions` 

- `Current Priorities` 

- `Questions to Resolve` 

- `Weekly Review` 

- `README_START_HERE` 

- `Builder’s Manual references` 

- `Any other files that claim to define the current sequence` 

```
For each, decide:
```

- `Current canonical role` 

- `Historical role` 

- `Content to merge` 

- `Links to update` 

- `Whether it should be retired` 

```
Do not maintain multiple current roadmaps.
```

```
⸻
```

```
Pass 4 — Final tracer landing
```

```
This is the highest-priority knowledge action.
```

```
Take the completed A–G tracer and convert its 49 schema corrections into
explicit changes across four layers.
```

```
Layer A — Ground-truth narrative
```

```
Complete the tracer as a coherent end-to-end narrative.
```

```
Preserve:
```

- `Artifact evidence` 

- `Interview-derived knowledge` 

- `Unknowns` 

- `Exceptions` 

- `Financial implications` 

- `Relationship-mediated decisions` 

- `System implications` 

```
Layer B — Canonical SOP reconciliation
```

```
Update only the SOPs affected by verified tracer findings.
```

```
At minimum review:
```

- `Order Workflow 0–4` 

- `ΚΟΥΒΑΣ System` 

- `Folder State Machine` 

- `Daily Order Processing` 

- `Supplier PO Creation` 

- `Proforma Checking` 

- `DTS and Loading` 

- `Warehouse Receiving` 

- `Delivery Scheduling` 

- `Finance and Credit Terms` 

- `Exception Handling` 

- `Operations Map` 

```
Every changed rule must link back to its tracer evidence.
```

```
Layer C — Domain/schema reconciliation
```

```
Produce a formal schema-diff report.
```

```
For every correction record:
```

```
correction_id:
ground_truth:
affected_entity:
affected_field_or_relationship:
current_model:
required_model:
reason:
example:
constraint:
migration_implication:
open_business_decision:
```

```
Do not directly modify all CSV contracts before the schema-diff has been
reviewed.
```

```
Layer D — Example dataset
```

```
Create one anonymized golden-tracer package with:
```

```
* Parties
* Project
* Quote/order relationship
* Order lines
* Supplier procurement
* Proforma
* Loading
* Receipt
* Partial line split
* Delivery subset
* Delivery documentation
* Invoice
* Payment
* Supplier DDT/invoice relationship
* Rebate, claim or return where relevant
* Timeline
* Source manifest
```

```
The tracer should test the model, not be simplified to fit it.
```

```
⸻
```

```
4. Knowledge-enrichment programme
```

```
Create a master knowledge queue:
```

```
00_COMMAND_CENTER/Knowledge Action Register.md
```

```
This must not replace domain-specific queues such as Supplier Enrichment Queue.
It should coordinate them.
```

```
Each knowledge action should contain:
```

```
knowledge_action_id:
domain:
question:
why_it_matters:
knowledge_owner:
artifact_required:
interview_required:
current_confidence:
target_output:
downstream_files:
schema_implication:
automation_implication:
```

```
priority:
status:
```

# `4.1 Knowledge-depth ladder` 

```
Every important topic should be explored through these layers:
```

```
Layer 1 — Description
```

```
What happens?
```

```
Layer 2 — Trigger
```

```
What causes the process or decision to begin?
```

```
Layer 3 — Normal path
```

```
What normally occurs, step by step?
```

```
Layer 4 — Decision inputs
```

```
What information does the person consider?
```

```
Layer 5 — Rule versus judgement
```

- `Which decisions are deterministic, and which rely on experience?` 

- `Layer 6 — Exceptions` 

```
When does the normal path change?
```

```
Layer 7 — Failure modes
```

```
What goes wrong, how is it detected, and who bears the consequence?
```

```
Layer 8 — Economics
```

```
What effect does the decision have on cash, margin, time, service or risk?
```

```
Layer 9 — Relationship dimension
```

- `How does client, supplier, architect or project importance change the decision?` 

```
Layer 10 — Evidence
```

- `Which artifacts prove or illustrate the process?` 

- `Layer 11 — System implication` 

```
What entities, events, relationships or controls must a future system represent?
Layer 12 — Automation boundary
```

```
What can safely become deterministic, and what must remain human?
```

```
Do not conclude a deep-dive after capturing only the first three layers.
```

# `4.2 Truth capsule` 

```
Each important operational finding should be recorded as a structured truth
capsule:
```

```
claim:
```

```
domain:
```

```
truth_type: fact | rule | default | heuristic | judgement | exception
source_kind:
source_reference:
knowledge_owner:
confidence:
valid_from:
valid_until:
known_exceptions:
financial_effect:
relationship_effect:
confidentiality:
schema_effect:
automation_effect:
public_safe:
```

```
Truth capsules may be embedded in domain notes rather than created as separate
notes for every claim.
```

# `4.3 Interview procedure` 

```
For every deep knowledge interview:
```

`1. Select one narrow domain.` 

`2. Select one real artifact or real case.` 

`3. Ask Orfeas to explain what occurred.` 

`4. Reconstruct the timeline.` 

`5. Ask what would have happened under three alternative scenarios.` 

`6. Identify hidden decisions.` 

`7. Identify financial consequences.` 

`8. Identify relationship overrides.` 

`9. Identify common novice misunderstandings.` 

`10. Identify what experienced staff notice immediately.` 

`11. Identify what currently lives only in memory.` 

`12. Produce a factual summary.` 

`13. Present contradictions and open questions.` 

`14. Obtain correction or confirmation.` 

`15. Update affected canonical notes only after confirmation.` 

`16. Create schema and automation implications separately.` 

`17. Add follow-up knowledge actions.` 

- `4.4 High-priority interview sequence` 

```
Conduct these deep-dives in order.
```

```
Interview 1 — ΚΟΥΒΑΣ as the procurement control system
```

```
Explore:
```

- `Every column` 

- `Every supplier-sheet variation` 

- `The four dates` 

- `Duplicate detection` 

- `Stock/sample/client procurement` 

- `Partial quantity handling` 

- `Re-entry after discrepancy` 

- `Removal at receipt` 

- `Packaging conversions` 

- `Owners and handoffs` 

- `Failure modes` 

- `How Dimitris and Vicky actually use it` 

- `Which decisions are invisible in the file` 

```
Interview 2 — Supplier AP and Kostas’s payment calendar
```

```
Explore:
```

```
* Every source document
* Invoice capture
* DDT matching
* Missing invoices
* Credit periods
* Payment scheduling
* Cashflow bending
* Exceptions
* Supplier importance
* Disputes
* Credit notes
* Who confirms payment
```

```
* What MEGASOFT does and does not hold
```

```
* Which decisions must remain Kostas’s judgement
```

```
Interview 3 — Realized margin
```

```
Explore:
```

```
* Quoted sell value
* List and net cost
* Transport
* Pallets
* Freight allocation
* Currency effects
* Rebates
* Claims
* Returns
* Breakage
* Free samples
* Stock origins
```

```
* Actual versus estimated cost
```

- `Order-level versus line-level margin` 

```
* When an order is considered financially closed
```

```
Interview 4 — Warehouse receipt and staging
```

```
Explore:
```

```
* Pallets
* Box counts
* Codes
* Documents
* Client stickers
* Staging areas
* Mixed-client pallets
* Partial receipts
* Damage
* Photographic evidence
* Stock destination
* Location truth
* Repacking
* Delivery preparation
```

```
Interview 5 — Deliveries and payment gating
```

```
Explore:
```

```
* Delivery subsets
* Client pickup
* Combined routes
```

```
* Project urgency
```

```
* Important clients
* Service recovery
* Payment agreements
* Credit clients
* Delivery documents
* Partial invoice timing
* Failed delivery
* Site constraints
* Proof of delivery
```

```
Interview 6 — Returns, breakages and claims
```

```
Explore:
```

```
* Client returns
* Supplier returns
* Stock eligibility
* Defects
* Transit breakage
* Post-transit breakage
* Transport claims
* Supplier claims
* Credits
* Reorders
* Reputation decisions
* Evidence burden
```

- `Who absorbs each loss` 

```
Interview 7 — Architect, designer and referrer economics
```

```
Explore:
```

```
* Identification of the referrer
* Project relationship
* Rebate type
* Placement inside or on top of margin
* Accrual
* Full-payment trigger
* Settlement
* Services invoices
```

- `Credits against orders` 

- `Cases where the referrer is also the client` 

- `Exceptions and confidentiality` 

```
Interview 8 — Sales and selection craft
```

```
Explore:
```

- `First five minutes with a client` 

- `How client type is read` 

- `How options are reduced` 

- `How equivalent materials are found` 

- `How technical constraints alter taste` 

- `How budget is inferred` 

- `When not to follow up` 

- `How architects differ from retail clients` 

- `What cannot be automated` 

- `What can be supported by product intelligence` 

```
Interview 9 — Supplier relationship intelligence
Explore:
```

```
* Direct versus conduit relationships
```

```
* Reliability
```

```
* Strategic importance
```

```
* Negotiation elasticity
* Loading behaviour
* Availability truth
* Common proforma mistakes
* Communication style
* Escalation routes
* Hero products
* Hidden operational advantages
* Warning signals
```

```
Interview 10 — Product and material expertise
```

```
Explore separately for:
```

```
* Tiles and slabs
* Sanitaryware
* Taps
* Bathroom furniture
* Parquet
* Kitchens
* Countertops
* Shower enclosures
* Wellness products
```

```
For each category identify:
```

```
* Selection variables
* Technical variables
* Installation constraints
* Common mistakes
* Compatibility rules
* Sales language
* After-sales risks
```

```
* Supplier-specific differences
```

```
⸻
```

```
5. Supplier and product ingestion programme
```

```
5.1 Do not “download everything” without a manifest
```

```
Build a source manifest before bulk ingestion.
```

```
Create:
```

```
04_SUPPLIERS_AND_BRANDS/Supplier Source Manifest.md
```

```
The actual manifest may be CSV, JSON or a generated table, but must be governed
by a documented schema.
```

```
Each source record should include:
```

```
source_id:
supplier_id:
brand_id:
source_type:
title:
language:
publication_year:
effective_from:
effective_until:
url:
```

```
local_location:
sha256:
downloaded_at:
rights_status:
confidentiality:
supersedes:
superseded_by:
extraction_status:
review_status:
linked_entities:
notes:
```

```
5.2 Source categories
```

```
Use controlled source types:
```

```
commercial_price_list
commercial_discount_terms
commercial_payment_terms
general_catalogue
collection_catalogue
technical_data_sheet
installation_manual
maintenance_guide
warranty
certificate
declaration_of_performance
epd
leed_document
voc_document
safety_data_sheet
packaging_table
sku_matrix
stock_file
availability_file
bim_file
cad_file
texture_asset
image_asset
press_release
brand_story
project_reference
email_evidence
proforma_example
invoice_example
loading_document
```

```
5.3 Priority order
```

```
Priority A — Commercial and operational truth
```

```
* Price lists
* Discount rules
* Payment terms
* Packaging
* Loading
* Lead times
* Contacts
* Channels
* Common mistakes
```

```
Keep these confidential.
```

```
Priority B — Orderable product structure
```

```
* Collections
* SKUs
* Codes
* Colours
* Formats
* Finishes
* Units
* Packaging
* Product variants
```

```
Priority C — Technical truth
```

```
* Material class
* Thickness
* Slip resistance
* Water absorption
* Certifications
* Installation
* Suitability
* Performance
```

```
Priority D — Editorial and public content
```

```
* Design story
* Aesthetic
* Projects
* Photography
```

- `Product narratives` 

- `Public downloads` 

- `SEO angles` 

```
Commercial and public information must never share the same uncontrolled
projection.
```

```
5.4 Supplier ingestion pipeline
```

```
For each supplier:
```

```
Create/verify supplier identity
→ create source manifest
```

```
→ download and hash sources
```

```
→ classify confidentiality
→ archive immutable originals
```

```
→ extract public facts
→ extract private operational facts
```

```
→ update supplier dossier
```

```
→ create/update collections roster
```

```
→ ingest one representative collection
→ validate schema
→ record unresolved questions
→ obtain Orfeas enrichment
→ audit
→ expand to further collections
```

- `5.5 Representative-pilot strategy` 

```
Do not begin with all suppliers.
```

```
Pilot with suppliers representing different complexity:
```

`1. A tile manufacturer with extensive format and finish matrices.` 

`2. A tap manufacturer with finish/colour and configuration variants.` 

`3. A sanitaryware or furniture manufacturer with component families.` 

`4. A parquet supplier with grading, dimensions and finish variables.` 

`5. Scavolini or another kitchen supplier with modular systems and complex configuration.` 

```
Only scale once category-specific problems are understood.
```

- `5.6 Category adapters` 

```
Do not force every product category into the tile schema.
```

```
Maintain a shared product core:
```

```
product_id:
supplier_id:
brand_id:
collection_id:
product_code:
name:
category:
unit:
active:
source_refs:
verification_status:
```

```
Then category-specific extensions.
```

```
Tile/slab extension
```

```
* Dimensions
* Thickness
* Finish
* Colour
* Rectification
* Slip
* Water absorption
* Box quantity
* m² per box
* Faces/graphics
* Shade variation
* Indoor/outdoor
* Pool suitability
```

```
Tap extension
```

```
* Installation type
* Mixer type
* Cartridge
* Thermostatic
* Outlets
* Finish
* Flow
* Pressure requirements
* Components
* Compatible rough-in body
```

```
* Lead-time class
```

```
Sanitaryware extension
```

```
* Product type
* Dimensions
* Installation
* Trap/outlet
* Seat compatibility
```

```
* Flush system
```

```
* Colour
* Material
```

```
* Fixing kit
* Accessibility
```

```
Furniture extension
```

```
* Module dimensions
* Material
* Front finish
```

```
* Handle system
```

- `Basin compatibility` 

- `Worktop compatibility` 

- `Internal accessories` 

```
* Configuration constraints
```

```
Parquet extension
```

- `Species * Grade * Pattern * Board dimensions` 

- `Thickness` 

- `Surface treatment` 

- `Finish` 

- `Installation method` 

- `Underfloor-heating suitability` 

- `Moisture requirements` 

```
Kitchen extension
```

```
* Programme
```

- `Cabinet module` 

- `Front system` 

- `Finish` 

- `Handle/opening system` 

- `Worktop` 

- `Internal equipment` 

- `Appliance integration` 

- `Configuration dependency` 

# `5.7 Product-ingestion confidence` 

```
Distinguish:
```

```
source_verified
supplier_asserted
human_verified
derived
needs_check
deprecated
```

```
Do not mark a product technically verified because a marketing catalogue
mentions it.
```

```
5.8 Source storage
```

```
The vault should retain:
```

- `Source manifests` 

- `Extracted knowledge` 

- `Provenance` 

- `Links` 

- `Review state` 

```
Large or sensitive binaries should gradually move to governed private object
storage or a dedicated private source archive.
```

```
Do not perform a disruptive source migration before the manifest and access
model exist.
```

```
⸻
```

`6. Real-life example library` 

```
Create:
```

```
02_OPERATIONS_OS/Cases/
```

```
or an equivalent approved location.
```

```
Each case should be anonymized unless a real identity is operationally necessary
and explicitly approved.
```

# `6.1 Required initial cases` 

```
Build at least these ten case archetypes:
```

`1. Normal multi-supplier client order.` 

`2. Order containing a WAIT line.` 

`3. Mixed client, stock and showroom-sample procurement.` 

`4. Proforma price or availability mismatch.` 

`5. Split loading caused by urgency.` 

`6. Partial receipt with child backorder.` 

`7. Partial delivery with intermediate payment.` 

`8. Transport breakage and carrier claim.` 

`9. Client return or defect entering stock/ΣΚΟΥΠΑ.` 

`10. Architect rebate with non-trivial settlement.` 

# `6.2 Case contract` 

```
Every case should include:
```

```
case_id:
case_type:
anonymized:
time_period:
participants:
project:
source_manifest:
timeline:
decision_points:
exceptions:
quantities:
documents:
financial_events:
outcome:
lessons:
doctrine_implications:
schema_implications:
automation_implications:
confidence:
```

```
6.3 Case body
```

```
Use this structure:
```

`1. Why this case matters` 

`2. Initial conditions` 

`3. Timeline` 

`4. Source artifacts` 

`5. Order and quantity flow` 

`6. Document flow` 

`7. Financial flow` 

`8. Decisions and judgement` 

`9. Exceptions` 

`10. Outcome` 

`11. What the existing SOP got right` 

`12. What the existing SOP missed` 

`13. Required schema support` 

`14. Safe automation candidates` 

`15. Open questions` 

```
Cases must not become client biographies. Capture only what serves operational
understanding.
```

```
⸻
```

# `7. Markdown contract improvements` 

```
Do not add excessive frontmatter indiscriminately.
```

```
Create a small universal core and domain-specific extensions.
```

```
7.1 Universal factual-note core
```

```
Propose through ADR:
```

```
type:
created:
updated:
status:
confidence:
owner:
canonicality:
data_classification:
source_refs:
related:
review_due:
```

# `7.2 Optional lifecycle fields` 

```
Use only where relevant:
```

```
supersedes:
superseded_by:
valid_from:
valid_until:
archive_reason:
```

# `7.3 Data-classification values` 

```
Propose:
```

```
public
internal
confidential
restricted
restricted_personal
```

```
Definitions:
```

- `public: approved for external use.` 

- `internal: ordinary company knowledge.` 

- `confidential: commercial terms, internal operations or sensitive supplier data.` 

- `restricted: client, financial, legal, employee or security-sensitive data.` 

- `restricted_personal: Orfeas’s personal material.` 

```
No generated public-facing file may draw from restricted classifications.
```

```
7.4 Factual-note body contract
```

```
Use when relevant:
```

`1. Purpose` 

`2. Current verified truth` 

`3. Sources and evidence` 

`4. Rules and defaults` 

`5. Human judgement` 

`6. Exceptions` 

`7. Examples` 

`8. Open questions` 

`9. Downstream implications` 

`10. Related entities` 

`11. Revision notes` 

- `7.5 Decision notes` 

```
Every ADR should include:
```

```
decision_id:
status:
date:
decision_owner:
context:
options:
decision:
rationale:
consequences:
revisit_trigger:
affected_files:
```

# `7.6 Open-question contract` 

```
Do not scatter unresolved questions through long notes without registration.
```

```
Important open questions should also enter a central decision register:
```

```
question_id:
domain:
question:
why_it_matters:
owner:
evidence_needed:
decision_deadline:
blocked_work:
status:
resolution:
```

```
The domain note may contain the context, but the decision register tracks
closure.
```

```
⸻
```

```
8. Audit system version 2
```

```
The current audit system is valuable. Extend it rather than replace it.
8.1 Session-close lint
```

```
Run after every meaningful session.
```

```
Check:
```

- `Valid frontmatter values` 

- `New orphan notes` 

- `Broken links` 

- `Missing inbound links` 

- `Unregistered open questions` 

- `Unclassified sensitive files` 

- `Notes edited without updated` 

- `New sources absent from manifest` 

- `Generated analysis freshness` 

- `Session state and backlog updates` 

```
This pass should be fast and mostly deterministic.
```

# `8.2 Weekly delta audit` 

```
Check only files changed during the week.
```

```
Questions:
```

- `Was a fact duplicated?` 

- `Was a new canonical competitor created?` 

- `Were any confidential values copied?` 

- `Did an agent create empty scaffolds?` 

- `Did a source produce all necessary downstream updates?` 

- `Did a new note receive an inbound link?` 

- `Did a schema value appear outside its controlled vocabulary?` 

- `Did ground truth change without SOP review?` 

- `Did an SOP change without evidence?` 

# `8.3 Monthly structural audit` 

```
Check:
```

- `Canonical note registry` 

- `Overlap clusters` 

- `Stale steering files` 

- `Orphans` 

- `Broken links` 

- `Frontmatter compliance` 

- `Source manifests` 

- `Review dates` 

- `Knowledge-gap coverage` 

- `Unresolved tracer findings` 

- `Schema-to-example coverage` 

- `Confidentiality duplication` 

- `Historical files presented as current` 

# `8.4 Quarterly adversarial audit` 

```
Use independent agent roles.
```

```
Required lenses:
```

`1. Information architecture critic` 

`2. Operational-domain critic` 

`3. Database/schema critic` 

`4. Source/provenance critic` 

`5. Security/privacy critic` 

`6. AI-agent governance critic` 

`7. Public-content leakage critic` 

`8. Human-authorship critic` 

```
Each finding must be classified:
```

```
confirmed defect
meaningful risk
acceptable trade-off
intentional design choice
false positive
requires Orfeas decision
```

# `8.5 Audit metrics` 

```
Track trends, not only absolute counts:
```

```
* Canonical notes
* Supporting notes
* Historical notes
* Overlap clusters
* Unresolved overlaps
* Verified-fact percentage
* Memory-seed percentage
* Stale needs_check items
* Notes without sources
* Source files without derived notes
* Derived notes without sources
* Tracer/case count
* Schema entities with real examples
* Confidential facts duplicated outside canonical homes
* Open decisions blocking work
* Average review age
* Orphan rate
* Broken-link rate
```

```
* Generated-file freshness
```

```
* Supplier-enrichment coverage
* Collection-ingestion coverage
```

# `8.6 Audit behaviour` 

```
Audits propose; they do not silently restructure.
```

```
Mechanical corrections may be applied automatically only when:
```

- `The intended result is unambiguous.` 

- `No meaning changes.` 

- `A test verifies the result.` 

```
* The change is logged.
```

```
⸻
```

# `9. Agent architecture improvements` 

```
Use Fable as an orchestrator but preserve distinct roles.
```

```
9.1 Vault Steward
```

```
Purpose:
```

```
* Maintain structure
```

- `Enforce canonical ownership` 

- `Coordinate sessions` 

- `Protect project direction` 

```
May:
```

- `Create plans` 

- `Link notes` 

- `Update reference files` 

- `Propose consolidations` 

```
May not:
```

- `Delete without the deletion protocol` 

- `Rewrite doctrine` 

- `resolve business ambiguity alone` 

- `9.2 Ground-Truth Interviewer` 

```
Purpose:
```

- `Extract tacit operational knowledge from Orfeas` 

```
Required behaviour:
```

- `Ask narrow, artifact-grounded questions` 

- `Challenge vague wording` 

- `Explore counterfactuals` 

- `Separate rule from judgement` 

- `Record contradictions` 

- `Return schema implications separately` 

# `May not:` 

- `Convert interview statements directly into universal doctrine without review` 

- `9.3 Supplier and Product Ingestion Agent` 

```
Purpose:
```

- `Process supplier sources` 

```
Required outputs:
```

- `Source manifest update` 

- `Extracted facts` 

- `Confidence` 

- `Supplier dossier changes` 

- `Collection changes` 

- `Product candidates` 

- `Open questions` 

- `Public/private classification` 

```
Must stop when:
```

- `A code, format, price or technical value is ambiguous` 

- `The source appears outdated` 

- `A source conflicts with another source` 

- `Image or publication rights are unclear` 

- `A commercial value could leak into public notes` 

- `9.4 Schema Reconciliation Agent` 

```
Purpose:
```

```
* Translate ground truth into domain changes
```

```
Must produce:
```

- `Current model` 

- `Required model` 

- `Example` 

- `Constraint` 

- `Migration implication` 

- `Open decision` 

```
May not:
```

- `Alter the schema solely for theoretical elegance` 

- `Add an entity without a real use case or approved future requirement` 

- `collapse human judgement into a status enum` 

# `9.5 Contradiction Critic` 

# `Purpose:` 

- `Search for conflicting facts, doctrine and terminology` 

```
Must distinguish:
```

- `Different context` 

- `Different time period` 

- `Different supplier rule` 

- `Genuine contradiction` 

- `Historical evolution` 

# `May not:` 

- `Treat all differences as errors` 

# `9.6 Audit Critic` 

# `Purpose:` 

- `Adversarially verify proposed findings` 

```
Must challenge:
```

- `Inflated severity` 

- `False duplication` 

- `Incorrect orphan findings` 

- `Broken-link false positives` 

- `Context removed from quotations` 

- `Proposed “cleanups” that destroy meaning` 

- `9.7 Security Classifier` 

# `Purpose:` 

- `Detect PII, commercial secrets, personal content and unsafe projection` 

```
Must review:
```

- `Every new source` 

- `Generated README/front-door content` 

- `Public-content drafts` 

- `Agent-access packages` 

- `Example fixtures` 

- `Repository history during formal audits` 

- `9.8 Domain Compiler` 

```
Purpose:
```

- `Export approved knowledge to the future application repository` 

```
May read only approved domains and classifications.
```

```
Must:
```

- `Validate schemas` 

- `Resolve IDs` 

- `Produce a versioned manifest` 

- `Reject restricted material` 

- `Open a proposed change` 

- `Never expose the entire vault to coding agents` 

```
9.9 Session Closer
```

```
Purpose:
```

- `Close every session cleanly` 

```
Required checks:
```

- `State updated` 

- `Backlog updated` 

- `Session log written` 

- `New open questions registered` 

- `Sources manifested` 

- `Analysis regenerated` 

- `Audit/lint passed` 

- `Commit message accurate` 

- `No accidental confidential duplication` 

```
⸻
```

# `10. Skills and deterministic tools to build` 

```
Maintain one canonical implementation for each skill. Do not allow a vault note,
.claude/skills copy and .agents/skills copy to diverge independently.
```

```
Create a canonical skills source or explicitly nominate one home.
```

```
10.1 /vault-baseline
```

```
Produces:
```

```
* File tree
```

- `Note registry` 

- `Link graph` 

- `Frontmatter inventory` 

- `Source inventory` 

- `Sensitivity summary` 

- `Baseline report` 

```
Read-only.
```

```
10.2 /overlap-registry
```

```
Produces:
```

- `Similar-note clusters` 

- `Unique-content comparison` 

- `Canonical recommendation` 

- `Merge and link-repair plan` 

```
Read-only unless explicitly placed in execution mode.
```

```
10.3 /canonicalize-note
```

```
Given an approved overlap decision:
```

- `Merges unique material` 

- `Adds provenance` 

- `Repairs links` 

- `Marks predecessor as superseded` 

- `Runs tests` 

- `Never deletes immediately` 

```
10.4 /knowledge-interview
```

```
Runs the twelve-layer knowledge-depth method.
```

```
Modes:
```

```
plan
interview
summarize
verify
land
```

```
Do not combine interview and landing into one uncontrolled operation.
```

```
10.5 /tracer-land
```

```
Processes approved tracer corrections in batches.
```

```
Outputs:
```

- `SOP diff` 

- `Schema diff` 

- `Example-data diff` 

- `Remaining ambiguities` 

```
10.6 /source-manifest
```

- `Hashes files` 

- `Extracts metadata` 

- `Classifies source type` 

- `Finds likely duplicates and superseded editions` 

- `Links sources to supplier/collection/material entities` 

# `10.7 /supplier-ingest` 

```
Modes:
```

```
public_research
source_ingest
private_enrichment
full_review
```

# `10.8 /collection-ingest` 

- `Validates collection schema` 

- `Preserves raw and normalized values` 

- `Extracts technical matrices` 

- `Creates open questions` 

- `Verifies source citations` 

```
10.9 /product-ingest
```

- `Extracts SKU candidates` 

- `Applies category adapter` 

- `Validates units and packaging` 

- `Links product → collection → material` 

- `Produces a review queue` 

- `Does not create unchecked production records` 

# `10.10 /case-build` 

```
Builds an anonymized operational case from a guided set of artifacts and
narration.
```

```
10.11 /schema-diff
```

```
Compares:
```

- `Ground truth` 

- `Canonical SOP` 

- `Current schema` 

- `CSV contracts` 

- `Real examples` 

```
10.12 /source-audit
```

```
Finds:
```

- `Missing sources` 

- `Dead URLs` 

- `Duplicate files` 

- `Superseded editions` 

- `Unhashed binaries` 

- `Sources with no derived knowledge` 

- `Notes citing unavailable evidence` 

# `10.13 /sensitivity-audit` 

```
Finds likely:
```

- `Personal data` 

- `Client data` 

- `Employee data` 

- `Financial data` 

- `Supplier commercial terms` 

- `Internal email addresses` 

- `Authentication material` 

- `Public/private projection leaks` 

```
Must report findings without restating sensitive values unnecessarily.
```

```
10.14 /vault-lint
```

```
Deterministic checks:
```

```
* Frontmatter
* Enums
* Links
* Inbound links
```

```
* Dates
```

```
* Duplicate IDs
```

- `Missing source references` 

- `Supersession loops` 

- `Invalid canonicality` 

- `Invalid classification` 

```
10.15 /knowledge-gap-report
```

```
Produces a prioritized list of questions based on:
```

- `Important entities with low confidence` 

- `Schema fields lacking examples` 

- `SOP rules lacking source evidence` 

- `Suppliers lacking operational enrichment` 

- `Collections lacking technical documentation` 

- `Agents lacking evaluation examples` 

# `⸻` 

# `11. Deterministic script backlog` 

```
Build small scripts before relying on agent memory.
```

```
Recommended utilities:
```

```
scripts/vault_inventory.py
scripts/frontmatter_validate.py
scripts/link_graph.py
scripts/duplicate_note_candidates.py
scripts/canonical_fact_registry.py
scripts/source_manifest.py
scripts/file_hash_inventory.py
scripts/sensitivity_scan.py
scripts/supersession_validate.py
scripts/knowledge_gap_report.py
scripts/schema_example_coverage.py
scripts/tracer_correction_tracker.py
scripts/controlled_vocab_validate.py
scripts/generated_file_freshness.py
scripts/domain_export.py
```

```
Every script should:
```

- `Read UTF-8 correctly.` 

- `Produce machine-readable JSON and human-readable Markdown.` 

- `Avoid writing by default.` 

- `Support --check and --apply where appropriate.` 

- `Return a non-zero exit code for CI failures.` 

- `Include fixtures and tests.` 

- `Avoid embedding confidential values in logs.` 

# `⸻` 

# `12. Execution cadence` 

```
Every session
```

`1. Read The Heart.` 

`2. Read Vault State Memory.` 

`3. Read the latest session log.` 

`4. Read the active execution backlog.` 

`5. Declare one bounded goal.` 

`6. Work only within that goal.` 

`7. Register new ambiguities.` 

`8. Update affected canonical notes.` 

`9. Run session lint.` 

`10. Update state and session log.` 

`11. Regenerate analysis where required.` 

`12. Commit one coherent unit.` 

# `Every week` 

- `Review Knowledge Action Register.` 

- `Review consolidation candidates.` 

- `Review new sources.` 

- `Review unresolved needs_check.` 

- `Review the tracer-correction burn-down.` 

- `Review supplier-ingestion progress.` 

- `Review data-classification issues.` 

- `Run weekly delta audit.` 

# `Every month` 

- `Run structural audit.` 

- `Select one deep knowledge domain.` 

- `Select one new operational case.` 

- `Complete one supplier/collection ingestion pilot.` 

- `Review canonical notes and historical competitors.` 

- `Review whether current tools are producing real value.` 

- `Retire one source of steering duplication.` 

# `Every quarter` 

- `Run adversarial deep audit.` 

- `Review the taxonomy.` 

- `Review agent permissions.` 

- `Review public/private separation.` 

- `Review source-storage strategy.` 

- `Review knowledge coverage against business priorities.` 

- `Review whether the vault is feeding the future operating system cleanly.` 

```
⸻
```

```
13. Ninety-day vault programme
```

```
Days 1–14 — Stabilize and map
```

```
Deliver:
```

- `Baseline` 

- `Entity registry` 

- `Overlap registry` 

- `Current canonical map` 

- `Data-classification ADR` 

- `Canonicality ADR` 

- `One steering hierarchy` 

- `No destructive deletion` 

```
Success criteria:
```

- `Every note has a known purpose.` 

- `Every genuine overlap has a proposed owner.` 

- `No active plan has two competing current homes.` 

- `Confidential and restricted areas are identified.` 

```
Days 15–30 — Land the tracer
```

```
Deliver:
```

```
* Completed tracer narrative
```

- `Formal 49-item correction register` 

- `Reconciled priority SOPs` 

- `Proposed domain/schema changes` 

- `Golden tracer case` 

- `Remaining business-decision list` 

```
Success criteria:
```

- `No known tracer fact exists only in a session log.` 

```
* Every schema correction has a disposition.
```

```
* Canonical SOPs no longer contradict verified ground truth without a visible
warning.
```

```
Days 31–45 — Deep operational knowledge
```

```
Complete:
```

- `ΚΟΥΒΑΣ interview` 

- `Supplier AP interview` 

- `Realized-margin interview` 

- `Warehouse interview` 

- `Delivery/payment interview` 

```
Deliver:
```

- `Ground-truth captures` 

- `Canonical updates` 

- `Knowledge actions` 

- `Case candidates` 

- `Schema implications` 

```
Days 46–60 — Supplier/product ingestion pilot
```

```
Complete representative pilots for:
```

- `One tile supplier` 

- `One tap supplier` 

- `One sanitaryware/furniture supplier` 

```
Deliver:
```

- `Source manifests` 

- `Supplier dossier enrichment` 

- `Collection notes` 

- `Product candidates` 

- `Category-specific schema lessons` 

- `Ingestion audit` 

```
Do not optimize for supplier count. Optimize for a repeatable, trustworthy
method.
```

```
Days 61–75 — Case library and audits
```

```
Deliver:
```

- `Five operational cases` 

- `Audit system v2` 

- `Updated deterministic lint` 

- `Sensitivity audit` 

- `Source audit` 

- `Schema-example coverage report` 

```
Days 76–90 — Agent and tooling hardening
```

```
Deliver:
```

```
* Formal agent contracts
```

- `Canonical skills source` 

- `Tested scripts` 

- `Agent evaluation fixtures` 

- `Domain-export prototype` 

- `Vault Governance Manual` 

- `Version-2 baseline` 

```
⸻
```

`14. Knowledge-enrichment scorecard` 

```
Track each major domain against:
```

```
0 — absent
```

```
1 — seed from memory
```

```
2 — basic description
```

```
3 — artifacts identified
```

```
4 — normal workflow captured
```

```
5 — exceptions captured
```

```
6 — financial and relationship effects captured
```

```
7 — real cases attached
```

```
8 — schema implications reconciled
```

- `9 — canonical and audited` 

```
10 — continuously maintained and system-ready
```

```
Initial domains:
```

```
* Sales and selection
* Quotes
* Client acceptance
* Orders
* ΚΟΥΒΑΣ
* Supplier POs
* Proformas
* Loadings
* Warehouse receipts
* Inventory
* Deliveries
* Client AR
* Supplier AP
* Payments
* Credit
* Profitability
* Rebates
* Returns
* Breakages
* Claims
* Supplier intelligence
* Materials
* Collections
* Products
* Projects
* Architect CRM
* Website/public content
```

```
Do not equate note quantity with knowledge depth.
```

```
⸻
```

```
15. Governance rules to add to operating instructions
```

```
Add or propose these rules in CLAUDE.md after review.
```

```
Rule A — No destructive reorganization
```

```
No delete, bulk move or large rename without:
```

- `Baseline` 

- `Overlap registry` 

- `Link-impact report` 

- `Approved change plan` 

- `Post-change audit` 

```
Rule B — One source of truth per maintained fact
```

```
The same fact must not be manually maintained in multiple notes.
```

```
Rule C — Ground truth requires landing
```

```
A completed ground-truth capture is not complete until:
```

- `Affected SOPs are reconciled` 

- `Schema implications are recorded` 

- `Open decisions are registered` 

- `At least one real example exists` 

```
Rule D — Source ingestion is a transaction
```

```
Every source-ingestion session must update:
```

- `Source manifest` 

- `Derived note` 

- `Affected entity dossier` 

- `Confidence` 

- `Open questions` 

- `Session log` 

```
Rule E — No bulk empty entities
```

```
Use rosters before notes.
```

```
Rule F — Confidentiality travels downstream
```

```
A confidential source may not generate a public or internal-general note without
explicit field-level sanitization.
```

```
Rule G — Generated files do not decide
```

```
Generated analysis may identify risks and patterns. Human-authored doctrine and
approved ADRs decide.
```

```
Rule H — Every automation needs examples
```

```
No automation specification is considered ready until it has:
```

- `At least three normal fixtures` 

- `At least three exception fixtures` 

- `Explicit abstention behaviour` 

- `Human approval boundary` 

- `Evaluation criteria` 

```
Rule I — Every schema entity needs an instance
```

```
A schema entity should not be considered mature without at least one real or
anonymized example.
```

```
Rule J — Every important judgement names its owner
```

```
Do not hide judgement behind passive wording such as “it is decided.”
```

```
Name:
```

- `Who decides` 

- `What they consider` 

- `When they escalate` 

- `What cannot be automated` 

```
⸻
```

# `16. Mandatory outputs from this programme` 

```
Create and maintain:
```

```
docs/VAULT_GOVERNANCE_MANUAL.md
docs/CANONICAL_KNOWLEDGE_MAP.md
docs/KNOWLEDGE_ENRICHMENT_ROADMAP.md
docs/SOURCE_INGESTION_MANUAL.md
docs/CASE_LIBRARY_STANDARD.md
docs/AGENT_GOVERNANCE.md
docs/TOOLING_BACKLOG.md
_meta/consolidation/Overlap Registry.md
_meta/consolidation/Canonical Note Registry.md
_meta/consolidation/Supersession Ledger.md
00_COMMAND_CENTER/Knowledge Action Register.md
```

```
Do not create all of these as empty placeholders.
```

```
Create each only when the preceding work provides meaningful content.
```

# `⸻` 

# `17. Stopping conditions` 

```
Stop and request an Orfeas business decision when:
```

- `Two notes express different strategic intent.` 

- `A deletion would remove unique history.` 

- `A workflow rule depends on relationship judgement.` 

- `A confidential fact’s canonical location is unclear.` 

- `A personal/business boundary is unclear.` 

- `A schema change would redefine an operational status.` 

- `A supplier rule may be supplier-specific rather than universal.` 

- `An artifact conflicts with Orfeas’s memory.` 

- `A product source is outdated or contradictory.` 

- `A public-content field may reveal private commercial data.` 

- `A proposed consolidation would substantially change the vault taxonomy.` 

- `A proposed automation would act externally.` 

- `A note may be part of Orfeas-authored doctrine.` 

- `A new controlled-vocabulary value is required.` 

- `A real client or employee identity would enter a reusable test fixture.` 

```
Do not improvise through these conditions.
```

```
⸻
```

```
18. Immediate bounded task
```

```
Begin with the following task only.
```

```
Goal: Vault consolidation and enrichment baseline
```

# `Required reading` 

```
Read in this order:
```

`1. The Heart.md` 

`2. CLAUDE.md` 

`3. 14_AI_COLLABORATION/Vault State Memory.md` 

`4. Latest session log` 

`5. 00_COMMAND_CENTER/Capture Backlog.md` 

`6. 99_SYSTEM/Vault Map.md` 

`7. docs/REPO_ANALYSIS.md` 

`8. _meta/audits/STATE.md` 

`9. _meta/audits/Vault Integrity Audit.md` 

`10. 02_OPERATIONS_OS/Order Lifecycle — Ground-Truth Capture.md` 

`11. 03_DATABASE_DESIGN/Database Master Schema.md` 

`12. 07_PRODUCT_KNOWLEDGE/Materials/Materials Schema.md` 

`13. 07_PRODUCT_KNOWLEDGE/Materials/Collection Schema.md` 

# `Scope` 

# `Produce:` 

`1. Current canonical-knowledge map.` 

`2. Every note that currently claims to steer work.` 

`3. Every acknowledged stale file.` 

`4. Every genuine overlap candidate.` 

`5. Every file that contains facts duplicated from a more canonical home.` 

`6. Every historical file at risk of being mistaken as current.` 

`7. Every schema or SOP known to conflict with the tracer.` 

`8. Every unlanded tracer correction.` 

`9. Every known confidentiality duplication.` 

`10. Proposed ADRs required before structural execution.` 

`11. The first 20 ordered knowledge actions for Orfeas.` 

`12. The first three supplier-ingestion pilots.` 

`13. The first five operational-case candidates.` 

`14. The deterministic scripts that should be built before execution.` 

```
Constraints
```

- `Read-only.` 

- `Do not delete.` 

- `Do not move.` 

- `Do not rename.` 

- `Do not merge.` 

- `Do not rewrite doctrine.` 

- `Do not edit the current schemas.` 

- `Do not create empty entity notes.` 

- `Do not restate confidential values.` 

- `Do not classify two notes as duplicates without comparing their unique purposes.` 

- `Clearly separate confirmed findings from recommendations.` 

```
Checkpoints
```

```
Checkpoint 1:
```

- `Baseline and file-purpose map.` 

```
Checkpoint 2:
```

- `Overlap clusters and canonical recommendations.` 

```
Checkpoint 3:
```

- `Tracer-to-SOP/schema reconciliation matrix.` 

```
Checkpoint 4:
```

- `Knowledge enrichment and source-ingestion roadmap.` 

```
Checkpoint 5:
```

- `Proposed changes, dependencies, risks and stopping decisions.` 

```
Validation
```

```
Run or create deterministic checks for:
```

- `UTF-8-safe file inventory` 

- `Link resolution` 

- `Orphans` 

- `Frontmatter values` 

- `Duplicate IDs` 

- `Similar note titles` 

- `Canonical competitors` 

- `Source-file inventory` 

- `Sensitive-content locations` 

- `Generated-analysis freshness` 

```
Required final report structure
```

`1. Executive assessment` 

`2. What must be protected` 

`3. Current canonical map` 

`4. Steering conflicts` 

`5. Overlap registry` 

`6. Stale and historical files` 

`7. Tracer reconciliation debt` 

`8. Knowledge-depth gaps` 

`9. Supplier and product ingestion readiness` 

`10. Case-library readiness` 

`11. Audit improvements` 

`12. Agent improvements` 

`13. Tooling improvements` 

`14. Proposed ADRs` 

`15. First 20 knowledge actions` 

`16. Change sequence` 

`17. Decisions required from Orfeas` 

`18. Explicit list of files that must not yet be touched` 

```
Explicit stopping condition
```

```
Stop after producing the analysis and proposed execution plan.
```

```
Do not execute consolidation until Orfeas has reviewed:
```

- `The canonical map` 

- `The overlap decisions` 

- `The deletion candidates` 

- `The new governance fields` 

- `The sequence of tracer landing` 

- `The first knowledge-interview programme` 

```
The first run must improve understanding, not file structure.
```

