---
type: adr_log
created: 2026-06-07
status: active
---

# Architecture Decision Records

Dated record of system/architecture decisions for the vault and future apps. Newest first. Use [[Template - ADR]] for new entries. (Business/ops decisions are recorded in ADR **Consequences**, the dated session logs, and [[Capture Backlog]] annotations — the [[Decision Log]] was retired 2026-07-19, baseline §17-4.)

---

## ADR-0007 — Governed consolidation & enrichment programme adopted (charter + reconciliations)
- **Date:** 2026-07-19
- **Status:** accepted
- **Context:** Orfeas brought an externally-drafted programme document (`redoal.md`, vault root) — a full governed consolidation / enrichment / continuous-build mandate (preservation principles, knowledge classes, sequential consolidation passes, the tracer landing as highest-priority knowledge action, a 12-layer interview programme, supplier-source ingestion with manifests, audit v2, agent contracts, skills/scripts backlog, a 90-day arc). Assessment: ~70% formalizes what the vault already practises; the rest is genuinely new machinery. Same arrival pattern as ADR-0006's meta-prompt. Per the authorship line (`CLAUDE.md §6`) an external draft cannot become governing doctrine silently, and it carried real frictions: a six-value product-confidence vocabulary conflicting with the exhaustive `confidence` enum (`CLAUDE.md §3`), a Knowledge Action Register that could become a second execution queue beside [[Capture Backlog]], and new frontmatter fields/folders proposed without their ADRs.
- **Options considered:** (A) adopt the raw document wholesale as the standing mandate; (B) file as advisory reference and cherry-pick per session; (C) keep the raw immutable in `_sources/`, derive a vault-idiomatic working charter, and record adoption plus explicit reconciliations in an ADR.
- **Decision:** (C). Raw draft → `14_AI_COLLABORATION/_sources/redoal — governed consolidation programme (external, 2026-07-19).md` (immutable evidence); working charter → [[Consolidation and Enrichment Programme]] (`status: active`). **Reconciliations:** (1) note-level `confidence` enum unchanged — the draft's six-value set becomes `verification_status` at the product/collection tier (precedent: [[Materials Schema]] mapping, ADR-0005); (2) [[Capture Backlog]] remains the single ranked execution queue — the future Knowledge Action Register coordinates knowledge gaps only; (3) `canonicality` + `data_classification` frontmatter deferred to a dedicated post-baseline ADR (fields only after ADR, as the draft itself requires); (4) new homes (`_meta/consolidation/`, `02_OPERATIONS_OS/Cases/`, the Register, governance-manual docs) are born on ingestion, never as empty placeholders. **First execution:** the read-only baseline (Pass 0–2, deep multi-agent) on 2026-07-19; **Pass 4 — the tracer final landing — remains the #1 content action.**
- **Consequences:** The vault gains one governing frame for consolidation and enrichment, with the hard sequence *baseline → Orfeas review → execute* and destructive operations locked behind the no-silent-deletion lifecycle and the stopping conditions. Same day, the unlogged/uncommitted 2026-07-13 ΕΡΓΟΣΤΑΣΙΑ supplier sweep (~44 seed dossiers) was **discarded at Orfeas's decision** ("delete the whole concept, we will redo it") — held in a git stash as the cooling period, to be redone through the programme's §5 ingestion pipeline with a proper source manifest. Governance rules A–J and the new frontmatter fields enter `CLAUDE.md` only after the baseline review.

## ADR-0006 — Living repo analysis regenerated on every push/pull
- **Date:** 2026-07-02
- **Status:** accepted
- **Context:** Orfeas brought a "Living Repository Analysis" meta-prompt and asked for it to run recurringly on every git push/pull. The vault had no generated, evidence-grounded profile of itself (architecture, business model, workflow trees, relationship map), and the README front door had drifted (audit-flagged). A recurrence mechanism was needed that actually fires — the vault's rituals are otherwise prose-enforced (`CLAUDE.md §6`).
- **Options considered:** (A) GitHub Action running Claude Code in CI on push — needs an API-key secret, cloud spend, runs outside local auth; (B) a synchronous LLM call inside git hooks — multi-minute hooks, and a pre-push regeneration cannot join the push's own commit; (C) a project skill as the engine + a layered recurrence contract around the existing session ritual.
- **Decision:** (C). The engine is the **`/repo-analysis` skill** (`.claude/skills/repo-analysis/`, delta by default, `deep` on demand) with a deterministic UTF-8-safe metrics script; output is `docs/REPO_ANALYSIS.md` + a marker-delimited README block. Recurrence is three layers: (1) `CLAUDE.md §8` step 4 — refresh before the end-of-session commit so the analysis rides the same push; (2) a **Claude-harness guard** (`.claude/hooks/git-sync-guard.mjs`, wired in `.claude/settings.json`) that blocks an in-session `git push` whose commits change notes without a refreshed analysis and nudges after pulls that bring note changes; (3) warn-only **`.githooks/`** (`pre-push`, `post-merge`, via `core.hooksPath`) for git use outside Claude Code.
- **Consequences:** The analysis stays current commit-by-commit and the ritual gains its first hook-backed (not prose-only) enforcement. Costs one delta pass per session. Fresh clones must run `git config core.hooksPath .githooks`. The analysis is Claude-maintained **reference layer** — it describes, never decides (authorship line, `CLAUDE.md §6`).

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
