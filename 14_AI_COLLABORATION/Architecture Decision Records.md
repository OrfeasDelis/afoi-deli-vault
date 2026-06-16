---
type: adr_log
created: 2026-06-07
status: active
---

# Architecture Decision Records

Dated record of system/architecture decisions for the vault and future apps. Newest first. Use [[Template - ADR]] for new entries. (Business/ops decisions go in `00_COMMAND_CENTER/Decision Log`.)

---

## ADR-0001 — Cross-session memory lives inside the vault
- **Date:** 2026-06-07
- **Status:** accepted
- **Context:** Need to preserve knowledge + Claude's memory across sessions without losing context.
- **Decision:** Store memory in a new in-vault folder `14_AI_COLLABORATION` (notably [[Vault State Memory]]) rather than external Claude session files. A root `CLAUDE.md` instructs every session to load it first.
- **Consequences:** Memory is portable, version-controlled, RAG-readable, and visible in Obsidian. Requires discipline to update at session end (codified in [[Session Protocol]]).

## ADR-0002 — Private GitHub repo for the vault
- **Date:** 2026-06-07
- **Status:** accepted
- **Context:** Vault holds supplier, client, and financial knowledge.
- **Decision:** Initialize git and push to a **private** GitHub repo `afoi-deli-vault` (account `OrfeasDelis`). Repo-local git identity; `.gitignore` excludes Obsidian workspace cache.
- **Consequences:** Versioned history + offsite backup while keeping data private. Sensitive-data policy still to define (see [[Open Questions]] #2).

## ADR-0003 — Core Obsidian plugin set
- **Date:** 2026-06-07
- **Status:** accepted
- **Context:** Want stronger interconnection + automation inside Obsidian.
- **Decision:** Adopt Dataview (live queries), Templater (dynamic templates), Obsidian Git (in-app commit/push). Binaries installed via Obsidian UI; config pre-seeded.
- **Consequences:** Enables dashboards and smoother git flow. Adds a one-time manual install step (see [[Obsidian Plugin Setup]]).

## ADR-0004 — Automation stack: Supabase Postgres + Python worker (no n8n)
- **Date:** 2026-06-14
- **Status:** accepted
- **Context:** The early plan named **n8n** as the automation/workflow layer (the 5-phase roadmap, several SOPs). For a solo build, an external low-code workflow tool added a moving part, a hosting decision, and a vendor dependency without enough benefit over plain code.
- **Options considered:** (A) n8n (self-hosted or cloud) as the workflow engine; (B) a custom **Python worker** running against **Supabase Postgres**, orchestrated in code.
- **Decision:** Drop n8n. The automation layer is a **Python worker** — it polls/triggers, parses, writes to Postgres, and drafts outputs for human approval — on **Supabase Postgres**. Bilingual, solo build via Claude Code. See [[Automation Masterplan]] / [[Python Worker Map]].
- **Consequences:** One less external system to host and secure; automation lives in version-controlled code beside the vault. Required a doctrine sweep — ~15 notes still prescribed n8n, reconciled in the 2026-06-16 audit (P1-A). **Recorded late:** the pivot happened 2026-06-14 but was not logged as an ADR until 2026-06-16; the [[Vault Integrity Audit]] now names a "doctrine pivot" as a trigger to prevent recurrence.

## ADR-0005 — Materials knowledge layer is three-tier (class → collection → SKU)
- **Date:** 2026-06-17
- **Status:** accepted
- **Context:** The materials layer began with generic `Material - <Name>` class notes + one [[Materials Schema]]. But a class note cannot hold the real, divergent specifics of each supplier line — Kronos **Pierre Vive** ≠ Florim **Authentic Luxe**; Laufen **SaphirKeramik** ≠ Cielo's vitreous china — where formats, thicknesses, finish wording and TDS values differ line-to-line and are often *far more* than the class note carries. Cramming them into the class note makes it unmaintainable and self-contradictory.
- **Options considered:** (A) one tier — generic material notes only; (B) fork the schema per supplier; (C) three tiers — one shared material-class vocabulary, one shared collection (instance) schema, and the SKU/product tier in the OS database.
- **Decision:** (C). `material` (class · ~22 · controlled vocabulary · [[Materials Schema]]) → `collection` (instance · hundreds · [[Collection Schema]]) → `SKU` (orderable · OS Postgres `products`). **One shared Collection schema, never per-supplier** (forking would destroy the shared queryable vocabulary that makes the layer useful). Collections capture the brand's **raw** wording *and* a **normalized** enum (solves cross-brand finish/format wording). Collection notes are **born on ingestion, never pre-stubbed** (Option A) — created when a source is fed or a project uses the line; until then the line is a roster row in `<Supplier> — Collections Reference`. **Ingestion sources:** manufacturer URL · a fed/attached PDF/TDS (primary high-fidelity — read via the Read tool, archived under the supplier's `_sources/`) · or a future **Google Drive feeder** (depends on the worker's Drive access — parked in [[Capture Backlog]]).
- **Consequences:** A clean dimensional model the OS joins on (SKU → collection → material); brand language preserved as a sales asset while staying queryable; granular per-collection entities (projects/quotes link the exact line) **without** stub-sprawl, because notes are born on ingestion. Cost: file-count and graph density grow over time, and it takes discipline not to pre-stub. Encoded by the new [[Collection Schema]] + the [[Materials Research Workflow]] "specifics clause". Decided via brainstorming in [[Session 2026-06-17]]. **Next:** pilot the Collection schema on one real fed collection to validate it (as [[Material - Porcelain Stoneware]] piloted the class schema).
