---
type: moc
created: 2026-06-07
status: active
---

# Collaboration Home

The control room for how **Orfeas + Claude** build this vault and the future apps together. This is the protected space for dialogue, decisions, memory, and roadmap.

## Start here every session
- [[Vault State Memory]] — the source of truth for current state (read first).
- [[Session Protocol]] — how each session starts, runs, and ends.

## Planning & decisions
- [[Consolidation and Enrichment Programme]] — the standing consolidation/enrichment frame (ADR-0007): baseline → review → execute; interviews, ingestion, cases, audit v2.
- [[Roadmap]] — phased plan from memory -> git -> automation -> data -> interface.
- [[Open Questions]] — live list of decisions to resolve.
- [[Architecture Decision Records]] — dated record of system choices.

## Working modes
How a session runs depends on what it's for:
- **Build** — the default working session · [[Session Protocol]].
- **Health check** — reconcile vault drift/orphans/links/schema (read-only) · [[Vault Integrity Audit]] → `/vault-audit`.
- **Strategic brainstorm** — step back and think *with* Orfeas about where the OS really stands and what's next (read-only, discuss-only) · [[Strategic Brainstorm Protocol]] → `/os-brainstorm`.
- **Repo analysis** — regenerate the living repository profile (`docs/REPO_ANALYSIS.md` + README summary; architecture, business model, workflow trees, relationship map as Mermaid) · runs on every push/pull per `CLAUDE.md §8` → `/repo-analysis`.

## Craft & infrastructure
- [[Afoi Deli — The Realm]] — a star-map of the whole vault (the architecture, workflow & logic as a cosmos; interactive HTML + embedded SVG).
- [[Afoi Deli — Operations Cockpit]] — a picture of the OS **interface** (Layer 4): "the bridge" where the ship is run day to day (interactive HTML; The Realm's register applied to a working product).
- [[Obsidian Tips and Tricks]] — interconnecting knowledge and notes.
- [[Obsidian Plugin Setup]] — Dataview, Templater, Obsidian Git.

## Session history

One dated log per working session, in `Sessions/` (auto-listed, newest first — self-maintaining via Dataview):

```dataview
LIST
FROM "14_AI_COLLABORATION/Sessions"
SORT file.name DESC
```

## How to use this space
1. Talk freely here about future plans — this layer is the protected environment.
2. Anything we decide gets captured (ADR / Open Questions / Roadmap).
3. At session end, memory is updated and pushed to GitHub.
4. Next session, Claude reloads memory and we continue without losing context.

## Related (existing vault)
- `08_AUTOMATION_AND_AI/Hermes Obsidian Codex Interface`
- `08_AUTOMATION_AND_AI/RAG Knowledge Base Rules`
- `99_SYSTEM/Vault Map`
- `99_SYSTEM/Obsidian Usage Rules`
