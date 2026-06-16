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
- [[Roadmap]] — phased plan from memory -> git -> automation -> data -> interface.
- [[Open Questions]] — live list of decisions to resolve.
- [[Architecture Decision Records]] — dated record of system choices.

## Craft & infrastructure
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
