---
type: memory_state
created: 2026-06-07
updated: 2026-06-07
status: active
confidence: verified
owner: Orfeas Delis
---

# Vault State Memory

> **This is the single source of truth for "where we are."**
> Claude reads this FIRST at the start of every session and UPDATES it at the end.
> See [[Session Protocol]].

## 1. What this vault is
Operating + knowledge system for **Afoi Deli Floor + Bath** (ΑΦΟΙ ΔΕΛΗ Ε.Ε.), Athens-based premium distributor of architectural materials (tiles, bathrooms, faucets, surfaces, large slabs, outdoor, Scavolini kitchens). Founded 1986. Website afoideli.gr. Owner: Orfeas Delis.

Designed as a 5-layer model: **Knowledge (Obsidian) -> Data (future Postgres) -> Automation (n8n) -> Interface (future webapp) -> AI Agent**. Core principle: *Obsidian is the memory; the agent is never the source of truth.*

## 2. Current structure (high level)
- `00_COMMAND_CENTER` dashboards / priorities / decisions / inbox
- `01_COMPANY_CORE` identity, brand, business model, people, strategy
- `02_OPERATIONS_OS` 12 SOPs (order flow, Kouvas, POs, warehouse, finance)
- `03_DATABASE_DESIGN` 11 schemas + ID conventions
- `04_SUPPLIERS_AND_BRANDS` indexes + 12 supplier notes
- `05_SALES_AND_CLIENT_EXPERIENCE` client journey + comms
- `06_PROJECTS_AND_CASES` dashboard + 4 projects
- `07_PRODUCT_KNOWLEDGE` 9 knowledge maps
- `08_AUTOMATION_AND_AI` masterplan, n8n map, agent roles, RAG rules, Hermes interface
- `09_WEBSITE_MARKETING_AND_CONTENT` web/SEO/content
- `10_FINANCE_AND_MANAGEMENT` dashboards, profitability, credit
- `11_EXPANSION_AND_VENTURES` 7 growth initiatives
- `12_PERSONAL_OS` 7 personal-leadership notes
- `13_DAILY_NOTES` daily template
- **`14_AI_COLLABORATION` (this layer)** memory + protocol + roadmap + sessions
- `97_CSV_SCHEMAS` 10 import headers (no data yet)
- `98_TEMPLATES` 11+ note templates
- `99_SYSTEM` vault map + usage rules

## 3. Conventions to always honor
- YAML frontmatter on every note: `type`, `created`, `status`, plus `confidence` where facts are involved.
- Confidence tags: `verified | likely | memory_seed | needs_check`.
- Naming: `Entity - Name` (e.g. `Supplier - Florim`), numbered folders, `[[wikilinks]]`.
- One note = one purpose. Link aggressively. Mark uncertainty.
- **Human approval required** for: sending emails, changing order status, changing prices, approving proformas, notifying clients of delays, changing delivery promises, updating financial records.

## 4. Infrastructure state
- **Git:** repo initialized 2026-06-07. Identity (repo-local): Orfeas Delis / OrfeasDelis@users.noreply.github.com.
- **GitHub:** private repo `afoi-deli-vault` under account `OrfeasDelis`.
- **Obsidian plugins:** Dataview, Templater, Obsidian Git — planned/configured; binaries installed via UI (see [[Obsidian Plugin Setup]]).

## 5. Active threads / in progress
- [x] Establish collaboration + memory layer (`14_AI_COLLABORATION`).
- [x] Initialize git + private GitHub repo.
- [ ] User installs the 3 community plugins in Obsidian UI (see [[Obsidian Plugin Setup]]).
- [ ] Next focus per [[Roadmap]]: confirm memory loop, then move toward automation planning.

## 6. Key open questions
See [[Open Questions]] for the live list.

## 7. Memory-seed facts needing verification
- Company revenue (~€15m+, `needs_check`).
- Supplier contacts / pricing / lead times (most supplier notes are `memory_seed`).
- Full Kouvas column definitions.

---
*Last session: [[Session 2026-06-07]]. Update this file at the end of every session before committing.*
