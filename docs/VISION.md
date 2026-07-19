# Afoi Deli Vault — Vision & Approach

**Generated 2026-07-19 · snapshot 6bdac9f** by the `/repo-analysis` skill — regenerated at every session end (`CLAUDE.md` §8, ADR-0006). **Do not hand-edit.**

> The authorship line, stated up front: everything below is **compiled from Orfeas-authored doctrine and decisions** — `The Heart.md`, the Operating Doctrine, the strategic axes, the recorded brainstorms and ADRs. This document synthesizes and cites; it does not originate vision. Where it interprets, it says so.

---

## The vision

Afoi Deli Floor + Bath is a second-generation Athens family merchant of premium architectural surfaces and bath — and this repository is the attempt to give that business, and the person inheriting it, a **second brain that compounds**. The stated north star: *"to become the most intelligent, design-aware, operationally precise architectural material distributor in Greece — and then turn that intelligence into a platform, content engine, and potentially a new category of construction/material operating system"* (`01_COMPANY_CORE/Afoi Deli Master Profile.md`).

Two convictions shape everything:

1. **The moat is the uplift engine, not the brand portfolio** (`01_COMPANY_CORE/Afoi Deli — Operating Doctrine.md`). Brands are abundant; the scarce asset is the house's capacity — staging plus conversion — to make any carried brand more premium than it is alone. The vault therefore hoards *what only this house knows*: supplier truth, selection craft, process reality, relationship history.
2. **Business and personal are one fabric** (`The Heart.md`, `CLAUDE.md`). The vault holds the company and the successor in one graph, on the premise that "your company will only become as clear, disciplined, and powerful as your own operating system" (`12_PERSONAL_OS/Personal Operating System.md`). The succession arc — competence → stewardship — is itself an engineering requirement here: the system must make the whole holdable at a standard.

## The workflow

The machine runs on three engines and one ritual (full trees: `docs/WORKFLOW_TREE.md`; stage-level flowcharts: `docs/REPO_ANALYSIS.md` §6):

- **Revenue engine** — the sample-wall selection craft (a documented, deliberately high walk-in conversion rate; the figure lives in `05_SALES_AND_CLIENT_EXPERIENCE/The Selection Engine.md`) feeds the order spine (statuses 0–4, ΚΟΥΒΑΣ procurement pool, proforma and payment gates) through ELXIS consolidation logistics to delivery and collection.
- **Knowledge engine** — supplier dossiers built in two strata (public research by Claude, private commercial truth enriched by Orfeas), a three-tier materials layer (class → collection → SKU, ADR-0005), and the standing ingest/query/lint loop (`CLAUDE.md` §6) that turns every source and every good answer into a linked, confidence-graded note.
- **Governance engine** — a session ritual (boot from The Heart and the state note; close with state update, session log, this docs/ suite, commit+push), periodic read-only integrity audits (`_meta/audits/`), strategic brainstorms with a deliberate promotion step, and hard **approval gates**: Claude drafts, a human approves anything external or financial (`CLAUDE.md` §4).

The collaboration model is explicit: **Obsidian is the memory; the agent is never the source of truth** (`CLAUDE.md` §4).

## The novelties in the approach

What is genuinely non-standard here, stated plainly (interpretation — but each item is traceable):

1. **An LLM-Wiki with an authorship line.** The vault follows the pattern *immutable sources → LLM-maintained wiki → governing schema file*, but overrides its default: Claude maintains the reference layer and the connective tissue; **the soul — doctrine, journal, decisions, framing — stays human-authored** (`CLAUDE.md` §6). The continuity remains Orfeas's.
2. **Instance-first, not schema-first.** After a full specification existed, the recorded pivot (`14_AI_COLLABORATION/Brainstorms/Brainstorm 2026-06-17.md`) was to *stop building and walk one real order end-to-end* — the tracer — on the rule "explain reality first; everything else is derived and adjusted to this." Ground truth explicitly wins over idealized SOPs.
3. **The drudgery/craft line.** Automation targets mechanical work (ΚΟΥΒΑΣ copy-paste, proforma checks, date-chasing) and is **forbidden from the selection craft** — the conversion gift is deliberately kept human (`00_COMMAND_CENTER/Capture Backlog.md`).
4. **Confidence-graded merchant intelligence.** Every factual note carries `verified | likely | memory_seed | needs_check`, with a deterministic mapping into the future database's `verification_status` — trust is a first-class, machine-readable dimension (`07_PRODUCT_KNOWLEDGE/Materials/Materials Schema.md`).
5. **An enrichment contract.** Private knowledge gaps are not invisible: every blank a human must fill is a labelled, searchable prompt — "(your knowledge)" — swept by a queue (`04_SUPPLIERS_AND_BRANDS/Supplier Enrichment Queue.md`).
6. **Status-honest artifacts.** The vault's own visualizations encode build state by color so the unbuilt OS reads as unlit space — the system is designed to resist its own mythology (`99_SYSTEM/Afoi Deli — The Realm.md`).
7. **A self-describing, self-enforcing repo.** This docs/ suite regenerates on every push/pull, and a git-sync guard blocks any push whose commits change notes without refreshed analysis (ADR-0006) — the first hook-backed ritual in an otherwise prose-enforced system.
8. **An immune system with memory.** Audits write findings to a ledger (`_meta/audits/STATE.md`) that carries Open/Done/Rejected state across runs, so false positives die once and drift cannot be re-litigated silently.

## The end goal

The **Afoi Deli OS**: a five-layer control tower — Knowledge (Obsidian) → Data (Supabase Postgres) → Automation (Python worker) → Interface (the operations cockpit) → AI Agent (Hermes) — where every order, supplier, loading, proforma, invoice, delivery, and client promise is visible and actionable (`08_AUTOMATION_AND_AI/Automation Masterplan.md`). Today, honestly: **Layer 1 runs; the 11 data contracts hold zero rows.** The interface exists as a design mockup (`99_SYSTEM/Afoi Deli — Operations Cockpit.md`).

Beyond the internal OS, the stated long-horizon play: prove the intelligence internally, then turn it outward — an architect-facing material-intelligence platform / The Material Atelier — only after internal proof (`11_EXPANSION_AND_VENTURES/AI Construction Materials Platform.md`, `16_IDEAS_AND_VISION/The Material Atelier.md`). And beneath the business goal, the human one: a successor who holds the whole — business, self, the people — at a standard (`The Heart.md`).

## The roadmap

Sequencing as currently decided (Root A leads; `00_COMMAND_CENTER/Capture Backlog.md` Priority 0.1; the older phased `14_AI_COLLABORATION/Roadmap.md` is flagged stale and pending refresh):

1. **The tracer interview is complete (A–G, 2026-07-18)** — one real, closed order fully explained end-to-end. Remaining is its *final landing* into the schema.
2. **Reconcile the specification to reality (now the #1 action)** — fold the tracer's schema-corrections list (**49 items**) into the SOPs and the 11 CSV contracts; land the newly-surfaced entities in `03_DATABASE_DESIGN` — MEGASOFT + rebates, the inventory/`stock_items` (ΣΚΟΥΠΑ) ledger, a `transport_claim` receivable, the ΔΑ/τιμολόγιο documents model, and Kostas-Excel AP as a second source of truth. (Realized per-order margin is confirmed uncomputed today — the OS's highest-value analytical add.)
3. **First real rows** — the validated schema receives its first instance data; the ΚΟΥΒΑΣ 5-phase migration starts read-only (document → extract → validate → dashboard → write-back last) (`02_OPERATIONS_OS/Kouvas System.md`).
4. **Python worker, read-only first** — Kouvas snapshot/dashboard, then the five specified jobs (proforma collector, DTS parser, folder scanner, ready-for-delivery drafts, weekly summary), every external send behind human approval (`08_AUTOMATION_AND_AI/Python Worker Map.md`, `08_AUTOMATION_AND_AI/Automation Backlog.md`).
5. **Interface** — the cockpit mockup becomes the working Layer-4 surface; client-facing surfaces come deliberately last — the backlog defers them until "after internal data is trusted" (`08_AUTOMATION_AND_AI/Automation Backlog.md`).
6. **In parallel, the knowledge flywheel** — supplier dossiers to Kronos depth, the ~22 material class notes, collections on ingestion; Root B (the content/SEO output pipe) follows once the spine is real (`14_AI_COLLABORATION/Brainstorms/Brainstorm 2026-06-17.md`).
7. **The growth axes** stay staged behind the spine: Scavolini kitchens, outdoor showroom, stock-house e-shop (gated on clean data), hotels/real estate, platform, personal brand (`01_COMPANY_CORE/Strategic Axes.md`, `11_EXPANSION_AND_VENTURES/Expansion Map.md`).

*The tracer interview is complete (A–G); the #1 next action is now its final landing — the 49-correction schema-diff, mapped correction-by-correction in `docs/VAULT_BASELINE_2026-07-19.md` §7 — per `14_AI_COLLABORATION/Vault State Memory.md`. As of 2026-07-19 all of the above runs inside the **Consolidation & Enrichment Programme** (ADR-0007, `14_AI_COLLABORATION/Consolidation and Enrichment Programme.md`): baseline → Orfeas's review → execute, with the tracer landing as its Pass 4.*
