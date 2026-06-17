---
type: ledger
created: 2026-06-17
status: active
confidence: verified
owner: Orfeas Delis
aliases:
  - Audit State
  - Vault Audit Ledger
tags:
  - audit
  - meta
  - vault-health
---

# Audit State — the ledger

> [!abstract] What this is
> The **forward-looking ledger** of the vault audit system. It complements its two siblings: [[Vault Integrity Audit]] holds the *why/how* (charter: the 8 checks + method), the dated `_meta/audits/<date>-vault-audit.md` reports hold *each run*, and **this file holds the running account** — the latest snapshot and the live state of every finding (Open / Done / Rejected / Deferred). The `/vault-audit` skill reads this first (to avoid re-litigating Rejected findings) and updates it last.

**Last session:** 2026-06-17 — audit system installed (skill + critic + settings + this ledger) via Phase-0 read-only recon. **No `/vault-audit` run yet** — the working sections below populate on the first run.

---

## Snapshot — 2026-06-17 (Phase-0 recon baseline)

> Read-only inventory taken while installing the system. Counts use UTF-8-correct file reading (see the Rejected note on the em-dash bug). Baseline for drift tracking.

| Metric | Value |
|---|---|
| Notes (`.md`) | **169** — pre-install baseline; excludes `.git`/`.obsidian`/`.claude` and the audit system's own ledger/reports under `_meta/audits/` (don't count the instrument as vault content) |
| Top-level folders | **22** (`00`–`17`, `97`–`99`, `_meta`) — all real on disk; match [[Vault Map]] |
| Resolved wikilinks | **730** unique source→target edges (≈1,199 raw occurrences incl. repeats) |
| Orphans (0 inbound) | **50** total → **~36** genuine content orphans after excluding 11 `98_TEMPLATES` + `README` + 2 `_sources` (mostly SOPs / projects / personal-OS notes not yet linked from a MOC — read as "young, not abandoned") |
| "Broken" link targets | **111 distinct / 162 instances** — decomposed below |
| ↳ full-path-style links | ~69 — *resolve in Obsidian*, but violate the bare-name convention (rename-fragile); **not dead** |
| ↳ doc placeholders / examples | 7 (`[[Supplier - <Name>]]`, `[[wikilinks]]`…) — exempt |
| ↳ genuinely-missing notes | ~20 (material classes, brands: Laufen/Mutina/Florim/Atlas Concorde/SaphirKeramik; 1–2 client/project) — lint backlog, mostly intentional future stubs |
| Frontmatter — `confidence` | all values valid (21 verified · 12 memory_seed · 10 likely · 3 needs_check); 120 notes omit it (allowed — only factual notes require it) |
| Frontmatter — `status` | **3 invalid**: `draft-for-verification`, `proposed`, one parse artifact (`budget:`); rest valid |
| Notes lacking frontmatter | 3 — `CLAUDE.md`, `README.md`, one `_sources` research prompt (operating files; exempt) |
| Dead / unwired OS artifacts | **11 of 14** templates in `98_TEMPLATES` have 0 inbound links; `.claude/` had no skills/agents before this install |
| Top hubs (inbound) | The Heart (32) · Supplier - Kronos (26) · Afoi Deli — Operating Doctrine (24) · Capture Backlog (22) · Vault State Memory (21) |
| Platform / tooling | Windows 11 · `claude` v2.1.178 · recurrence = Windows Task Scheduler (on-demand chosen; command documented, not registered) |

---

## Open
*Confirmed findings awaiting Orfeas's action. Populated by the first `/vault-audit` run — empty until then.*

- _— none yet —_

## Done
*Findings resolved (with the date + how).*

- **2026-06-16 audit P0 (structure↔index drift) — cleared.** Per [[Vault State Memory]] and verified on disk: phantom `15/16/18` resolved, 22 folders match [[Vault Map]], canonical index consolidated, schema governance settled. *(Pre-seed from recon; confirm against the [[2026-06-16-vault-audit]] report on next run.)*

## Contested — reconcile on first run
*Sources disagree; the audit exists to settle these. Not yet Done, not a confirmed Open finding.*

- **n8n → Python-worker sweep: COMPLETE or still live?** [[Vault State Memory]] reports the sweep *complete* (n8n removed 2026-06-14); but `CLAUDE.md §7` and the [[2026-06-16-vault-audit]] still flag n8n as *prescribed* in ~15 live notes. This is precisely the source-of-truth / doctrine-freshness conflict checks #2–#3 exist to catch. The first `/vault-audit` run should grep the vault, decide which source is true, and move this to Done or Open.

## Rejected
*False positives — do not resurface. Each names why it is not real.*

- **"122 broken links" (em-dash mojibake) — 2026-06-17.** A `Get-Content -Raw` read mis-decoded UTF-8 em-dashes (`—`, char 8212) into mojibake, so every note whose name contains `—` (e.g. `Afoi Deli — Operating Doctrine`) appeared as both a broken target and an orphan. Reading with `[System.IO.File]::ReadAllText($p,[Text.Encoding]::UTF8)` resolves them all. **The links are fine; the script was wrong.** Always read UTF-8.

## Deferred
*Acknowledged, intentionally not acting now.*

- **`18_KNOWLEDGE` wing — deferred** (2026-06-16 audit P0-1). Subjects studied for their own sake live in `12_PERSONAL_OS` via [[Studies and Subjects]] until volume justifies a dedicated wing. Not a gap.

---

*Linked: [[Vault Integrity Audit]] (charter) · [[2026-06-16-vault-audit]] (first report) · [[The Heart]] · [[Vault State Memory]]. Nothing here is final.*
