---
type: protocol
created: 2026-06-07
status: active
confidence: verified
---

# Session Protocol

How every working session with Claude runs, so memory is never lost and the repo stays clean.

> [!note] Session modes — two read-only variants skip the END writes
> This protocol governs **build** sessions. Two variants are deliberately **read-only / discuss-only** and **override the END-of-session writes below** (no Vault State Memory update, no log, no commit as an automatic tail): the **health check** ([[Vault Integrity Audit]] → `/vault-audit`) and the **strategic brainstorm** ([[Strategic Brainstorm Protocol]] → `/os-brainstorm`). Their outcomes are filed afterward as a separate, chosen step.

## START of session (Claude does this first)
1. Read [[Vault State Memory]] (the source of truth for "where we are").
2. Read the latest note in `Sessions/` (most recent `Session YYYY-MM-DD`).
3. Skim [[Roadmap]] and [[Open Questions]].
4. Briefly confirm to the user the current state + proposed focus before acting.

## DURING the session
- Follow vault conventions (see [[Vault State Memory]] section 3 and `99_SYSTEM/Obsidian Usage Rules`).
- Log any meaningful architectural/system choice in [[Architecture Decision Records]].
- Add newly surfaced questions to [[Open Questions]].
- Respect human-approval gates — Claude drafts, human approves external/risky actions.

## END of session (before stopping)
1. Update [[Vault State Memory]] (structure, infra state, active threads, seed facts).
2. Create a session log from [[Template - Session Log]] in `Sessions/Session YYYY-MM-DD`.
3. Update [[Roadmap]] / [[Open Questions]] if they changed.
4. Commit + push (see below). Record the commit ref in the session log.

## Commit + push routine
```bash
# You are already in the vault root — no cd needed.
git add -A
git commit -m "<type>: <short summary>"   # types: feat, fix, docs, chore, refactor
git push
```
- PowerShell on this machine does NOT accept `&&` — run the git commands on separate lines.
- Commit types follow the user's git-workflow rule (feat/fix/docs/chore/refactor/...).
- If Obsidian Git plugin is enabled, routine commits can also happen automatically on a timer; manual commits remain the norm for meaningful checkpoints.

## Golden rules
- Obsidian is the memory. The agent is never the source of truth.
- Document first, structure second, automate third.
- If unsure, mark `confidence: needs_check` rather than guessing.
