---
type: workflow
parent: "[[Hermes Obsidian Codex Interface]]"
status: backlog
created: 2026-06-15
updated: 2026-06-15
tags:
  - hermes
  - telegram
  - ingestion
  - queue
  - assets
  - google-drive
---

# Hermes Telegram Capture Queue

> [!abstract] The idea in one line
> Text Hermes on Telegram when you spot a collection (or price list) worth adding; it drops it on a **queue**; a worker later fetches the PDFs into the Drive tree, writes the entry into the right [[Kronos — Collections Reference|Collections Reference]], cross-checks afoideli.gr, and links it all back. You are the trigger and the judgment; Hermes is the clerk.

## Why this before the monthly auto-diff

The earlier plan (Hermes scrapes each collections index monthly, diffs `article:modified_time`, flags changes) is *Hermes goes looking* — it needs reliable scraping, change detection and dedup before it's trustworthy. This is *you hand Hermes the thing* — it ships far earlier, because the hard part (deciding what's worth adding) is done by you in one text. The auto-diff can come later as a second feeder into the **same queue**.

Obeys the [[Hermes Obsidian Codex Interface|interface doctrine]]: the agent is never the source of truth — the **queue (a file or table) is**. Hermes only records and fetches.

## The loop

```
You (Telegram) ──▶ Hermes bot ──▶ ingestion_queue (status: pending)
                                        │
                        (you /drain, or scheduled pass)
                                        ▼
                                  Python worker
                     ├─ create Drive Collections/<name>/ folder
                     ├─ download catalogue.pdf + technical.pdf
                     ├─ write entry into <Supplier> — Collections Reference.md
                     ├─ run afoideli.gr Store-API cross-check
                     └─ flip row → done, attach Drive + Obsidian links
                                        ▼
                              Hermes replies "done ✅ <links>"
```

## What you can send

| You send | Hermes stores | Worker can later… |
|---|---|---|
| **Name** — "add Kronos Pierre Vive" | supplier + collection, `source: manual` | search the manufacturer site for the page + PDFs |
| **URL** — the collection page link | the URL (best — unambiguous) | fetch title, look, catalogue/technical PDF links directly |
| **Forwarded PDF / photo** | the file → Drive `_staging/` | file it into `Collections/<name>/` on processing |

Suggested bot commands: `/add <supplier> <collection>`, `/add <url>`, plain file upload = "stage this", `/queue` (list pending), `/drain` (process now), `/done <id>`.

## Queue record (shape)

```yaml
id: 7
created: 2026-06-15T18:22:00+03:00
source: telegram
type: collection            # collection | pricelist | photo | other
supplier: Kronos
collection: Pierre Vive
payload: "https://kronosceramiche.com/collections/pierre-vive/"  # or file ref
status: pending             # pending | processing | done | skipped
result_links:               # filled on completion
  drive_folder:
  obsidian_note:
notes:
```

## Where the queue lives (decision)

- **v0 (now-ready):** a single `ingestion-queue.md` or `.json` in the vault (or the bot's SQLite). Works the day you have a bot + a Drive folder, before Postgres exists. Zero infra.
- **v1 (when the OS exists):** an `ingestion_queue` table in Supabase Postgres, drained by the [[Python Worker Map|Python worker]] as just another job. Migrate v0 rows in.

Either way the queue is a structured artifact, not Hermes's memory.

## Reuse, don't duplicate

The [[Circles]] Telegram bot v0 spec (Python, SQLite, Railway/Fly.io) is the **same bot host**. Add an `/add` command + a file handler + one table here rather than standing up a second bot.

## Link-back pattern (generalises beyond catalogues)

Binary in Drive, **link + metadata in the vault**. Same mechanism for every asset type:

| Asset | Drive location | Written back into |
|---|---|---|
| Catalogue PDF | `Collections/<name>/catalogue.pdf` | `Catalogue:` line in the collection entry |
| Technical sheet | `Collections/<name>/technical.pdf` | `Technical:` line |
| Collection photos | `Collections/<name>/photos/` | `Photos:` link in the entry |
| **Price list** | `_pricelists/<file>` | **"Price list folder"** field in `Supplier - <Name>.md` (currently `(to populate)`) |

So the same Telegram queue can capture "new price list from the rep" exactly like a new collection — `type: pricelist` — and the worker writes the link into the supplier note's commercial profile.

## Build order (smallest shippable first)

1. Bot host up (reuse Circles bot) with `/add` + file handler writing to the queue file/table. Hermes replies "queued #N". **This alone is useful** — capture works even if draining is still manual.
2. Manual drain: you run the [[Supplier Cross-Reference Workflow]] over pending rows; mark done.
3. Worker `/drain` job: automates fetch → Drive → reference note → cross-check → links.
4. (Later) monthly auto-diff feeds the *same* queue as a second source.

## Open questions

- [ ] Queue in vault file vs. bot SQLite vs. Postgres for v0? (Lean: bot SQLite, since the bot's already there.)
- [ ] Drive auth for the worker (service account vs. OAuth) — same decision as [[Kronos — Catalogue & Asset Ingestion]].
- [ ] Confirm the Circles bot can host a second command set cleanly, or whether a tiny separate bot is simpler.

## Links

- Doctrine → [[Hermes Obsidian Codex Interface]] · worker → [[Python Worker Map]]
- Asset plan → [[Kronos — Catalogue & Asset Ingestion]] · cross-ref → [[Supplier Cross-Reference Workflow]]
- Bot reuse → [[Circles]]
- Pipeline → [[Automation Backlog]]
