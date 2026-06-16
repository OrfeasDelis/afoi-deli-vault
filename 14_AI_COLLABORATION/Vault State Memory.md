---
type: memory_state
created: 2026-06-07
updated: 2026-06-16
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

> [!warning] Known drift — flagged by the [[2026-06-16-vault-audit|2026-06-16 audit]]; remediation is next session's Priority 0.
> The list below still names `15_PERSONAL_LIFE` / `16_IDEAS_AND_VISION` / `18_KNOWLEDGE`, which **do not exist on disk** — only `17_JOURNAL` does — and it predates `_meta/`. Treat it as *pending reconciliation*, not source of truth, until the audit P0s are cleared. The canonical folder index will be [[Vault Map]] once corrected.

- `00_COMMAND_CENTER` dashboards / priorities / decisions / inbox
- `01_COMPANY_CORE` identity, brand, business model, people, strategy — **+ [[Afoi Deli — Operating Doctrine]]**
- `02_OPERATIONS_OS` 12 SOPs (order flow, Kouvas, POs, warehouse, finance)
- `03_DATABASE_DESIGN` 11 schemas + ID conventions
- `04_SUPPLIERS_AND_BRANDS` indexes + supplier notes (Kronos, Cielo, Mutina, Fantini, Scavolini populated) + conduit hubs [[Conduit - Plus Interiors]] / [[Conduit - Filon IKE]]
- `05_SALES_AND_CLIENT_EXPERIENCE` client journey + comms
- `06_PROJECTS_AND_CASES` dashboard + 4 projects
- `07_PRODUCT_KNOWLEDGE` 9 knowledge maps
- `08_AUTOMATION_AND_AI` masterplan, **Python Worker Map**, agent roles, RAG rules, Hermes interface
- `09_WEBSITE_MARKETING_AND_CONTENT` web/SEO/content
- `10_FINANCE_AND_MANAGEMENT` dashboards, profitability, credit
- `11_EXPANSION_AND_VENTURES` growth initiatives
- `12_PERSONAL_OS` personal-leadership notes (focus, health, learning, leadership)
- `13_DAILY_NOTES` daily template (work capture)
- **`14_AI_COLLABORATION` (this layer)** memory + protocol + roadmap + sessions
- **`15_PERSONAL_LIFE`** relationships / finance / wellness *(new)*
- **`16_IDEAS_AND_VISION`** Mnemonic Atelier, Material Atelier, Circles, future bets *(new)*
- **`17_JOURNAL`** life log, YYYY-MM-DD, Orfeas's own voice *(new)*
- **`18_KNOWLEDGE`** Italian, coffee, history, philosophy — things studied *(new)*
- `97_CSV_SCHEMAS` 10 import headers (no data yet)
- `98_TEMPLATES` 11+ note templates
- `99_SYSTEM` vault map + usage rules
- `_meta/audits` vault audit reports + the [[Vault Integrity Audit]] charter *(new, 2026-06-16)*
- **Root:** [[The Heart]] — foundational note, above structure.

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

## 5. Active threads / in progress

- [ ] **▶ NEXT SESSION — Priority 0: act on the [[2026-06-16-vault-audit|2026-06-16 vault audit]].** Source-of-truth drift is the headline: reconcile [[Vault Map]] + this file's §2 to disk (resolve the `15/16/18` phantom folders), declare one source of truth for the schema-vs-CSV data contract, and apply the drop-in `CLAUDE.md` + [[Session Protocol]] fixes from the audit Appendix. Then the P1 sweep. Recurring practice now charted in [[Vault Integrity Audit]].
- [x] Collaboration + memory layer established.
- [x] Git + private GitHub repo.
- [x] Foundation notes shipped: [[The Heart]], [[Afoi Deli — Operating Doctrine]], [[Supplier - Kronos]].
- [x] CLAUDE.md extended (Heart-first load, identity layer, personal-handling rule).
- [x] n8n removed; automation files rewritten to Python worker stack.
- [x] Personal folders created (15–18).
- [x] Supplier ingestion reframed to **public research** ([[Supplier Research Workflow]]); cross-reference machinery parked in [[Automation Backlog]]; [[Hermes Telegram Capture Queue]] rewritten so its drain runs research, not cross-check (2026-06-15).
- [x] **Supplier stack — Cielo, Mutina, Fantini** built to Kronos depth (dossier + collections reference each); two conduit hubs created ([[Conduit - Plus Interiors]], [[Conduit - Filon IKE]]); the Kronos conduit section consolidated into the Plus Interiors hub; Supplier/Brand indexes + Bathroom/Tile knowledge maps wired (2026-06-16).
- [x] **Supplier enrichment scaffolding** — standing *Famous for & specializations* section added to all full dossiers + the [[Supplier Research Workflow]] template; [[Supplier Enrichment Queue]] created (surfaces every blank still to fill: `(your knowledge)` / `(to populate)` / `needs_check`); dossiers treated as living, enriched over passes (2026-06-16).
- [x] **Scavolini ingested** — kitchen dossier (overwrote stub) + collections reference; Orfeas's expansion rationale captured in [[Scavolini Kitchen Expansion]]; countertop cross-sell wired to [[Supplier - Kronos]] / [[Kitchen Knowledge Map]]; our dealer arrangement left as enrichment prompt (Greek Store OMETRY ≠ our channel) (2026-06-16).
- [x] Cross-reference-workflow link graph consolidated — ~12 dangling wikilinks across 6 notes repointed (2026-06-15).
- [x] First [[Journal]] entry (begins with the night of 2026-06-14).
- [ ] **n8n sweep still pending** — [[Roadmap]] Phase 3 + [[Hermes Obsidian Codex Interface]] still name n8n and a non-existent `n8n Workflow Map`; contradicts settled doctrine. (Re-confirmed by lint 2026-06-15.)
- [ ] [[Roadmap]] refresh — still the pre-pivot 2026-06-07 5-phase plan; doesn't reflect Supabase + Python worker / Builder's Manual R0–R3.
- [ ] Decide: Kronos "On afoideli.gr" column — keep as parked pilot data or strip for consistency.
- [ ] [[The Material Atelier]] page — linked but no page yet (Capture Backlog Priority 4).
- [ ] Continue interview: more suppliers, the people ([[People and Roles Map]]), personal domains.

## 6. Key open questions

See [[Open Questions]].

## 7. Memory-seed facts needing verification

- Company revenue (~€15m+, `needs_check`).
- Supplier **private** fields (contacts / pricing / terms / lead times / loading) pending for all houses. Kronos + Cielo/Mutina/Fantini now carry full **public** dossiers (`likely`) with private fields as labelled `[!question]` prompts; the other 9 suppliers are still `memory_seed` stubs.
- Full Kouvas column definitions.

---
*Last session: 2026-06-16b ([[Session 2026-06-16b]]) — **deep vault audit** ([[2026-06-16-vault-audit]]) + recurring [[Vault Integrity Audit]] charter; next session's Priority 0 is acting on the audit. Prior same day: 2026-06-16 ([[Session 2026-06-16]]) — supplier stack built: Cielo, Mutina, Fantini dossiers + collections references, two conduit hubs ([[Conduit - Plus Interiors]], [[Conduit - Filon IKE]]), Kronos conduit consolidated, Supplier/Brand indexes + product maps wired; plus enrichment scaffolding (a standing *Famous for & specializations* slot + [[Supplier Enrichment Queue]]) and the **Scavolini** kitchen ingestion. Prior: Hermes capture-queue reframe + lint ([[Session 2026-06-15b]]), the Kronos pilot ([[Session 2026-06-15]]), the 2026-06-14 foundation build. Update this file at the end of every session before committing.*
