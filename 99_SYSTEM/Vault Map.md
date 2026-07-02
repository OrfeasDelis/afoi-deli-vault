---
type: system_index
created: 2026-06-07
updated: 2026-07-02
status: active
confidence: verified
aliases:
  - Vault Map
---

# Vault Map

> [!important] This is the single canonical folder index.
> Every other note that needs the taxonomy should **link here**, not restate it — that restating is exactly what drifted (see the [[2026-06-16-vault-audit|2026-06-16 audit]] P0-1). Add, rename, or retire a folder → update *this table* and nothing else needs to duplicate it. The list below matches the folders on disk as of 2026-06-16.

## Folder logic

| Folder | Purpose |
|---|---|
| `00_COMMAND_CENTER` | Dashboards, priorities, decisions, inbox, reviews · [[Capture Backlog]] |
| `01_COMPANY_CORE` | Company identity, strategy, business model, people · [[Afoi Deli — Operating Doctrine]] |
| `02_OPERATIONS_OS` | Core workflows and SOPs (order flow, Kouvas, POs, warehouse, finance) |
| `03_DATABASE_DESIGN` | ERP/database schema notes (`.md`) — see [[Database Master Schema]]. Source-of-truth precedence vs. the `97_CSV_SCHEMAS` headers is being settled (audit P0-2). |
| `04_SUPPLIERS_AND_BRANDS` | Supplier/brand intelligence — the gravity center · [[Supplier Master Index]] / [[Brand Master Index]] |
| `05_SALES_AND_CLIENT_EXPERIENCE` | Client journey, quotes, emails |
| `06_PROJECTS_AND_CASES` | Projects, cases, hospitality, kitchens |
| `07_PRODUCT_KNOWLEDGE` | Product/material knowledge maps |
| `08_AUTOMATION_AND_AI` | Automation & AI — **Supabase Postgres + Python worker** stack, agent roles, RAG rules (no n8n) · [[Automation Masterplan]] / [[Python Worker Map]] |
| `09_WEBSITE_MARKETING_AND_CONTENT` | Website, SEO, editorial engine |
| `10_FINANCE_AND_MANAGEMENT` | KPIs, profitability, credit |
| `11_EXPANSION_AND_VENTURES` | Growth initiatives (Scavolini, outdoor, hotel, platform ideas) |
| `12_PERSONAL_OS` | Personal operating discipline — focus, health, leadership, learning · [[Personal Operating System]] |
| `13_DAILY_NOTES` | Daily work capture |
| `14_AI_COLLABORATION` | Cross-session memory, session logs, protocol, roadmap, ADRs · [[Vault State Memory]] |
| `15_PERSONAL_LIFE` | *(seed)* Personal life outside the business — relationships, wellness, finance · [[Personal Life — Home]] |
| `16_IDEAS_AND_VISION` | *(seed)* Creative/venture bets — Mnemonic Atelier, Material Atelier, Circles · [[Ideas and Vision — Home]] |
| `17_JOURNAL` | Life log, `YYYY-MM-DD`, Orfeas's own voice · [[Journal]] |
| `97_CSV_SCHEMAS` | Database import headers (`.csv`). Precedence vs. the `03` schema notes: audit P0-2. |
| `98_TEMPLATES` | Reusable note templates |
| `99_SYSTEM` | Vault rules and maps (this note, [[Obsidian Usage Rules]]) |
| `_meta` | Vault audit reports + the [[Vault Integrity Audit]] charter |
| `docs` | Generated repo profile — `REPO_ANALYSIS.md`, the living analysis (Claude-regenerated on every push/pull via `/repo-analysis`; don't hand-edit — see `CLAUDE.md §8`) |

> [!note] Deliberately not present
> `18_KNOWLEDGE` was **deferred** (audit P0-1): subjects studied for their own sake live in `12_PERSONAL_OS` for now — see [[Studies and Subjects]] — until the volume justifies its own wing.

## How to use

Start with the dashboards ([[Capture Backlog]]) and [[Vault State Memory]]. Don't try to perfect everything before using it. The canonical philosophy and voice are [[The Heart]]; where the build actually is, is [[Vault State Memory]].

> [!tip] See it as a cosmos
> For a visual overview of the whole vault — folders, the order workflow, and the 5-layer OS as a dark star-map — see [[Afoi Deli — The Realm]]. This table is the canonical *index*; The Realm is its *picture*.
> And for a picture of the **interface itself** (Layer 4) — the operations cockpit / "the bridge" where the ship is run — see [[Afoi Deli — Operations Cockpit]].
