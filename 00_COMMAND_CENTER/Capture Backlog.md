---
type: backlog
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - command-center
  - backlog
---

# Capture Backlog

> [!tip] How to use this
> This is the answer to *"what do I work on with Claude?"* — you never start from a blank page.
> **Before a session:** open this, pick the top unchecked item, capture it into a note.
> **A topic is done** when it has produced a findable note (not when everything's been said).
> **After a session:** tick what you shipped, add anything new that surfaced.
> Rank by **value × perishability**: capture what only you know and would lose if forgotten. Generic, lookup-able things don't belong here.

---

## Priority 1 — The people
*Highest value: the heart of both business and life, entirely in your head, irreplaceable.*

- [ ] **Kostas (father)** — the founder, the maxims, the merchant's nerve and intuition. The model. → note in `01_COMPANY_CORE` / linked from [[The Heart]] and [[People and Roles Map]].
- [ ] **Chrysoula (mother)** — the closer, the human gift. Her role in the uplift engine.
- [ ] **Ektoras (brother)** — role in the business and the family. (Currently a placeholder.)
- [ ] **Eleni (partner)** — her own note in `15_PERSONAL_LIFE/Relationships`. Begins as a named presence; fill in over time.

## Priority 2 — Core suppliers (identity brands)
*Perishable, commercially load-bearing. Same treatment as [[Supplier - Kronos]].*

- [ ] **Cielo** — sanitary ware; the founding Tzanidis story; flagship.
- [ ] **Mutina** — identity brand, premium tile.
- [ ] **Fantini** — taps/faucets, through Plus Interiors.
- [ ] Then the rest of the heavy houses as they earn pages (Salvatori, Antonio Lupi, Atlas Concorde, Florim…).

## Priority 3 — Open the personal rooms
*So `15_PERSONAL_LIFE` isn't just empty folders.*

- [ ] One real note in **Relationships**, **Wellness**, or **Finance** — whichever is most alive.
- [ ] Keep the [[Journal]] going — the habit matters more than the structure.

## Priority 4 — Ideas & Vision
*Give the creative/venture work proper homes in `16_IDEAS_AND_VISION`.*

- [ ] **Mnemonic Atelier** — the doctrine (Lineage Art, Archive Equity, Seven Operations).
- [ ] **The Material Atelier** — the architect-facing B2B brand/platform.
- [ ] **Circles** — the prediction-market concept.

## Priority 5 — Operational truth
*Where the SOPs describe the ideal vs. how the business actually runs.*

- [ ] Audit the SOPs in `02_OPERATIONS_OS` for aspirational-vs-real, mark with confidence tags.
- [ ] Sweep remaining incidental `n8n` mentions via VS Code find-replace.
- [ ] **Decide on a [[CLAUDE]] update** — add a "Reusable workflows (don't reinvent)" pointer to §6 so future sessions follow [[Supplier Cross-Reference Workflow]] and the Drive/[[Hermes Telegram Capture Queue]] asset pattern instead of improvising. Draft wording proposed 2026-06-15; held for review (CLAUDE.md is framing-layer — author's call).

## Hermes Capture Queue — registry
*The Telegram → queue → worker inbox. Full design: [[Hermes Telegram Capture Queue]]. This registry tracks build state; the queue itself (once built) holds the actual items to ingest.*

- [ ] **v0 — capture works.** Add `/add <supplier> <collection>`, `/add <url>`, and a file handler to the [[Circles]] bot host; write rows to a queue (bot SQLite or a vault file); reply "queued #N". *Useful even before draining is automated.*
- [ ] **v0.5 — manual drain.** Process pending rows by running [[Supplier Cross-Reference Workflow]] by hand; mark `done`.
- [ ] **v1 — worker `/drain` job.** Automate fetch → Drive tree → reference-note entry → afoideli Store-API cross-check → write links back → flip to `done`.
- [ ] **v2 — second feeder.** The monthly collections-index auto-diff (`article:modified_time`) appends to the *same* queue.
- Open decisions: queue store (lean: bot SQLite); Drive auth (service account vs OAuth); confirm Circles bot can host a second command set.

## Future / when the OS exists
*Captured, deliberately deferred — do NOT pull these forward.*

- [ ] **Kronos catalogue & asset ingestion** — pull collection PDFs/photos into Google Drive, link back from Obsidian; pilot for an all-suppliers template. Plan ready: [[Kronos — Catalogue & Asset Ingestion]]. Blocked on **Google Drive write access for the worker** (service-account vs OAuth decision). Manual option works now for top-quoted collections.
- [ ] **Loop engineering** — revisit only when Afoi Deli OS has a test suite and automated verification (the 14-step loop doc). Premature until then.
- [ ] **QMD search layer** — add as the retrieval layer only once the index file stops being enough (vault grows past a few hundred dense pages). Karpathy names it as the documented option.

---

## Done (shipped)

- [x] **Live vault connection set up** (Claude + filesystem MCP) — sources can now be written directly to disk; unblocked the frictionless ingest workflow *(2026-06-15)*
- [x] [[The Heart]] — foundational doctrine note *(2026-06-14)*
- [x] [[Afoi Deli — Operating Doctrine]] *(2026-06-14)*
- [x] [[Supplier - Kronos]] — first populated supplier *(2026-06-14)*
- [x] [[CLAUDE]] extended + ingest/query/lint loop added *(2026-06-14)*
- [x] [[Vault State Memory]] rewritten *(2026-06-14)*
- [x] Personal folders created; n8n removed; git repaired *(2026-06-14)*
- [x] Journal begun — template + first entry *(2026-06-14)*
- [x] [[Session 2026-06-14]] detailed session log *(2026-06-14)*
- [x] Kronos supplier doc filled from website + all 18 collections — [[Kronos — Collections Reference]] *(2026-06-15)*
- [x] [[Supplier Cross-Reference Workflow]] — reusable supplier-ingestion skill *(2026-06-15)*
- [x] [[Kronos — Catalogue & Asset Ingestion]] + [[Hermes Telegram Capture Queue]] concepts *(2026-06-15)*
- [x] `Suppliers/` restructured to one folder per supplier *(2026-06-15)*
- [x] [[Session 2026-06-15]] session log *(2026-06-15)*

---
*Linked: [[The Heart]] · [[Vault State Memory]] · [[Session 2026-06-15]]*
