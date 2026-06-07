# AFOI DELI — Knowledge & Operating Vault

Private Obsidian vault and operating system for **Afoi Deli Floor + Bath** (Athens). Knowledge layer for operations, suppliers, products, projects, automation, and future apps.

> **Private repository.** Contains supplier, client, and financial knowledge. Do not make public.

## Where to start
- **In Obsidian:** open `README_START_HERE.md` (vault philosophy) and `14_AI_COLLABORATION/Collaboration Home.md` (working hub).
- **For Claude / AI sessions:** `CLAUDE.md` (root) defines operating instructions; memory lives in `14_AI_COLLABORATION/Vault State Memory.md`.

## Structure
Numbered folders by domain (`00_COMMAND_CENTER` … `14_AI_COLLABORATION`, `97_CSV_SCHEMAS`, `98_TEMPLATES`, `99_SYSTEM`). See `99_SYSTEM/Vault Map.md`.

## Sync workflow
```bash
git add -A
git commit -m "<type>: <summary>"   # feat | fix | docs | chore | refactor
git push
```
Full routine and session memory protocol: `14_AI_COLLABORATION/Session Protocol.md`.

## Plugins
Dataview, Templater, Obsidian Git — see `14_AI_COLLABORATION/Obsidian Plugin Setup.md`.

## Principle
Obsidian is the memory. Structured files/data are the source of truth — never the AI. Humans approve all external/risky actions.
