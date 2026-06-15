---
type: memory_state
created: 2026-06-07
updated: 2026-06-15
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

- `00_COMMAND_CENTER` dashboards / priorities / decisions / inbox
- `01_COMPANY_CORE` identity, brand, business model, people, strategy — **+ [[Afoi Deli — Operating Doctrine]]**
- `02_OPERATIONS_OS` 12 SOPs (order flow, Kouvas, POs, warehouse, finance)
- `03_DATABASE_DESIGN` 11 schemas + ID conventions
- `04_SUPPLIERS_AND_BRANDS` indexes + supplier notes ([[Supplier - Kronos]] now populated)
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

- [x] Collaboration + memory layer established.
- [x] Git + private GitHub repo.
- [x] Foundation notes shipped: [[The Heart]], [[Afoi Deli — Operating Doctrine]], [[Supplier - Kronos]].
- [x] CLAUDE.md extended (Heart-first load, identity layer, personal-handling rule).
- [x] n8n removed; automation files rewritten to Python worker stack.
- [x] Personal folders created (15–18).
- [x] Supplier ingestion reframed to **public research** ([[Supplier Research Workflow]]); cross-reference machinery parked in [[Automation Backlog]]; [[Hermes Telegram Capture Queue]] rewritten so its drain runs research, not cross-check (2026-06-15).
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
- Supplier contacts / pricing / lead times (most supplier notes still `memory_seed`).
- Full Kouvas column definitions.

---
*Last session: 2026-06-15 ([[Session 2026-06-15b]]) — Hermes capture queue reframed to supplier research, cross-reference-workflow links consolidated, vault lint. Prior: the Kronos pilot ([[Session 2026-06-15]]) and the 2026-06-14 foundation build. Update this file at the end of every session before committing.*
