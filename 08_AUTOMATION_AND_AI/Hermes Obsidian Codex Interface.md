---
type: interface_strategy
created: 2026-06-07
status: draft
---

# Hermes / Obsidian / Codex Interface

## Core idea

Obsidian is the memory.  
Codex/Claude-style tools can edit/build.  
The Python worker (on Supabase Postgres) moves events.  
A future webapp becomes the cockpit.

## Pilot interface options

### Phase 1 — Obsidian only

Use dashboards, templates, search, links, and daily notes.

### Phase 2 — Obsidian + scripts

Scripts read markdown/YAML and generate CSV/database updates.

### Phase 3 — Obsidian + Python worker

The Python worker watches folders/Gmail and creates tasks/notes. See [[Python Worker Map]].

### Phase 4 — Database + web dashboard

Postgres stores structured truth.  
Webapp shows order/client/supplier views.

### Phase 5 — Agent cockpit

A custom assistant can answer:

- What orders are stuck?
- Which suppliers need follow-up?
- Which products are risky?
- What should I do today?
- Draft the supplier email.
- Check this proforma.
- Create a client update.
- Build a website page from this collection.

## Rule

Do not let the agent become the source of truth.  
The source of truth must be structured files/data.
