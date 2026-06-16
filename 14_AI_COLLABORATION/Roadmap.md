---
type: roadmap
created: 2026-06-07
updated: 2026-06-16
status: active
---

# Roadmap

Phased plan for building the vault and the future apps. Mirrors the 5 phases in [[Hermes Obsidian Codex Interface]].

> [!note] Refreshed 2026-06-16 (audit P1-D)
> Updated to the settled **Supabase Postgres + Python worker** stack — n8n removed (see Phase 3). This is the *vault/phases* roadmap; the Afoi Deli **OS build** has its own R0–R3 plan in the Builder's Manual (see [[Vault State Memory]] §4).

## Phase 0 — Foundation (IN PROGRESS, 2026-06-07)
- [x] Collaboration + memory layer (`14_AI_COLLABORATION`).
- [x] Git repo + private GitHub `afoi-deli-vault`.
- [x] Session protocol + templates.
- [x] User installs Obsidian plugins (Dataview, Templater, Obsidian Git).
- [ ] Confirm full memory loop across a fresh session.

## Phase 1 — Obsidian discipline
- Populate `memory_seed` supplier notes with verified data.
- Fill product knowledge maps.
- Build Dataview dashboards (e.g. suppliers by status, open questions, draft notes).
- Verify company facts flagged `needs_check`.

## Phase 2 — Scripts (Obsidian + code)
- Scripts read markdown/YAML and generate/update CSV in `97_CSV_SCHEMAS`.
- Validate frontmatter consistency across notes.

## Phase 3 — Automation (Python worker)
- Build first jobs on the **Python worker** (Supabase Postgres) — see [[Python Worker Map]] / [[Automation Masterplan]]:
  - Gmail proforma collector.
  - Daily folder scanner.
  - Ready-for-delivery drafter (human-approved).
- Connect Google Drive / Gmail watchers.

## Phase 4 — Data layer (Postgres)
- Migrate Kouvas + CSV schemas into Postgres using `03_DATABASE_DESIGN` schemas + ID conventions.
- Keep Obsidian as knowledge, Postgres as structured truth.

## Phase 5 — Interface + Agent cockpit
- Webapp views for orders / clients / suppliers.
- AI agents (per `08_AUTOMATION_AND_AI/AI Agent Roles`) over knowledge + data, with approval gates.

## Working principle
Each phase only begins when the previous layer is stable. Document first, structure second, automate third.
