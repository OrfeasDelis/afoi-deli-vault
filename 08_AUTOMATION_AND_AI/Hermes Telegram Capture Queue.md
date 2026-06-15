---
type: workflow
parent: "[[Hermes Obsidian Codex Interface]]"
status: backlog
created: 2026-06-15
updated: 2026-06-15
tags:
  - hermes
  - telegram
  - research
  - suppliers
  - queue
  - ingestion
  - assets
  - google-drive
---

# Hermes Telegram Capture Queue

> [!abstract] The idea in one line
> Text Hermes on Telegram when you spot a supplier or collection worth documenting; it drops it on a **queue**; a worker later runs the [[Supplier Research Workflow]] on it — public deep research into a supplier dossier + collections reference — and links it all back. You are the trigger and the judgment; Hermes is the clerk. No afoideli.gr cross-check: public research only.

## Why this before the monthly auto-diff

The earlier plan (Hermes scrapes each collections index monthly, diffs `article:modified_time`, flags changes) is *Hermes goes looking* — it needs reliable scraping, change detection and dedup before it's trustworthy. This is *you hand Hermes the thing* — it ships far earlier, because the hard part (deciding what's worth adding) is done by you in one text. The auto-diff can come later as a second feeder into the **same queue**.

Obeys the [[Hermes Obsidian Codex Interface|interface doctrine]]: the agent is never the source of truth — the **queue (a file or table) is**. Hermes only records; the worker researches.

## The loop

```
You (Telegram) ──▶ Hermes bot ──▶ research_queue (status: pending)
                                        │
                        (you /drain, or scheduled pass)
                                        ▼
                                  Python worker
                     ├─ run Supplier Research Workflow (public sources)
                     ├─ write Supplier - <Name>.md (public profile + enrichment prompts)
                     ├─ write <Name> — Collections Reference.md (per-collection, PDF links)
                     ├─ wire backlinks (Supplier + Brand indexes, projects)
                     └─ flip row → done, attach Obsidian links
                                        ▼
                              Hermes replies "done ✅ <links>"
```

## What you can send

| You send | Hermes stores | Worker can later… |
|---|---|---|
| **Name** — "research Kronos" / "add Cielo" | supplier (+ optional collection), `source: manual` | run the [[Supplier Research Workflow]]: locate the site, research the house, capture collections + PDF links |
| **URL** — the manufacturer/collection page link | the URL (best — unambiguous) | seed research from that page: identity, collections, catalogue/technical PDF links |
| **Forwarded PDF / photo** | the file ref (optionally staged in Drive `_staging/`) | attach as a source for the dossier; pulling the binary into Drive is the deferred asset job |

Suggested bot commands: `/add <supplier> <collection>`, `/add <url>`, plain file upload = "stage this", `/queue` (list pending), `/drain` (process now), `/done <id>`.

## Queue record (shape)

```yaml
id: 7
created: 2026-06-15T18:22:00+03:00
source: telegram
type: supplier              # supplier | collection | pricelist | photo | other
supplier: Kronos
collection: Pierre Vive      # optional — omit to research the whole house
payload: "https://kronosceramiche.com/"  # or collection URL, or file ref
status: pending             # pending | processing | done | skipped
result_links:               # filled on completion
  supplier_note:
  collections_reference:
notes:
```

## Where the queue lives (decision)

- **v0 (now-ready):** a single `research-queue.md` or `.json` in the vault (or the bot's SQLite). Works the day you have a bot, before Postgres exists. Zero infra.
- **v1 (when the OS exists):** a `research_queue` table in Supabase Postgres, drained by the [[Python Worker Map|Python worker]] as just another job. Migrate v0 rows in.

Either way the queue is a structured artifact, not Hermes's memory.

## Reuse, don't duplicate

The [[Circles]] Telegram bot v0 spec (Python, SQLite, Railway/Fly.io) is the **same bot host**. Add an `/add` command + a file handler + one table here rather than standing up a second bot.

## Deferred: the binary-asset / Drive layer

> [!note] Not part of the research drain
> Research **captures PDF + photo links** into the notes; it does **not** download binaries (see [[Supplier Research Workflow]] step 8). Pulling catalogues/technical sheets/photos into a Google Drive tree is a **separate, deferred job** — [[Kronos — Catalogue & Asset Ingestion]]. When that job runs, the same link-back pattern applies: binary in Drive, link + metadata in the vault.

| Asset | Drive location | Written back into |
|---|---|---|
| Catalogue PDF | `Collections/<name>/catalogue.pdf` | `Catalogue:` line in the collection entry |
| Technical sheet | `Collections/<name>/technical.pdf` | `Technical:` line |
| Collection photos | `Collections/<name>/photos/` | `Photos:` link in the entry |
| **Price list** | `_pricelists/<file>` | **"Price list folder"** field in `Supplier - <Name>.md` (currently `(to populate)`) |

So the same Telegram queue can also capture "new price list from the rep" — `type: pricelist` — and the (deferred) asset worker writes the link into the supplier note's commercial profile.

## Build order (smallest shippable first)

1. Bot host up (reuse [[Circles]] bot) with `/add` + file handler writing to the queue file/table. Hermes replies "queued #N". **This alone is useful** — capture works even if draining is still manual.
2. Manual drain: you run the [[Supplier Research Workflow]] over pending rows; mark done.
3. Worker `/drain` job: automates the research workflow → supplier dossier + collections reference → backlinks. (Binary/Drive filing stays the separate deferred job above.)
4. (Later) monthly auto-diff feeds the *same* queue as a second source.

## Open questions

- [ ] Queue in vault file vs. bot SQLite vs. Postgres for v0? (Lean: bot SQLite, since the bot's already there.)
- [ ] Drive auth only matters once the *deferred* asset job runs (service account vs. OAuth) — same decision as [[Kronos — Catalogue & Asset Ingestion]]; not needed for the research drain.
- [ ] Confirm the [[Circles]] bot can host a second command set cleanly, or whether a tiny separate bot is simpler.

## Links

- Doctrine → [[Hermes Obsidian Codex Interface]] · worker → [[Python Worker Map]]
- Research workflow → [[Supplier Research Workflow]] · deferred asset plan → [[Kronos — Catalogue & Asset Ingestion]]
- Bot reuse → [[Circles]]
- Pipeline → [[Automation Backlog]]
