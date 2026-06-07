# CLAUDE.md — Operating Instructions for This Vault

This is the **AFOI DELI** Obsidian vault: the knowledge + operating system for Afoi Deli Floor + Bath. Read this at the start of every session.

## 1. Load memory FIRST
Before doing anything, read in this order:
1. `14_AI_COLLABORATION/Vault State Memory.md` — the source of truth for current state.
2. The latest log in `14_AI_COLLABORATION/Sessions/`.
3. `14_AI_COLLABORATION/Roadmap.md` and `14_AI_COLLABORATION/Open Questions.md`.

Then briefly confirm the current state and proposed focus with Orfeas before acting. Full workflow: `14_AI_COLLABORATION/Session Protocol.md`.

## 2. Conventions (always)
- Every note has YAML frontmatter: `type`, `created`, `status`; add `confidence` for factual notes.
- Confidence values: `verified | likely | memory_seed | needs_check`. Mark uncertainty — never guess silently.
- Naming: `Entity - Name` (e.g. `Supplier - Florim`). Numbered folders. Use `[[wikilinks]]` and link aggressively.
- One note = one purpose. Keep facts separate from opinions.
- See `99_SYSTEM/Obsidian Usage Rules.md` and `08_AUTOMATION_AND_AI/RAG Knowledge Base Rules.md`.

## 3. Human-approval gates (never act autonomously)
Claude may DRAFT, but a human must APPROVE: sending emails, changing order status, changing prices, approving supplier proformas, notifying clients of delays, changing delivery promises, updating financial records.
**Obsidian is the memory; the agent is never the source of truth.**

## 4. End every session
1. Update `14_AI_COLLABORATION/Vault State Memory.md`.
2. Write a session log from `98_TEMPLATES/Template - Session Log.md` into `14_AI_COLLABORATION/Sessions/`.
3. Update Roadmap / Open Questions / ADRs if they changed.
4. Commit + push:
   ```bash
   git add -A && git commit -m "<type>: <summary>" && git push
   ```
   Commit types: feat, fix, docs, chore, refactor. Repo: private `afoi-deli-vault` (account `OrfeasDelis`).

## 5. Start here in Obsidian
`14_AI_COLLABORATION/Collaboration Home.md` is the hub for working together. `README_START_HERE.md` covers vault philosophy.
