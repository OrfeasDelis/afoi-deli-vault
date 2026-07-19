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

**Last update:** 2026-07-19 — **consolidation baseline (Pass 0–2) + Orfeas's §17 review + the §16-C mechanical batch** ran under ADR-0007 (a [[Consolidation and Enrichment Programme]] instrument, *not* a `/vault-audit` run — its findings live in `docs/VAULT_BASELINE_2026-07-19.md` + `_meta/consolidation/`). Ledger effects this date: **F1/F2 fixed** (template emitters) · **F3 superseded-marked** (OV-01) · **F4 re-armed** as the schema-diff trigger (Pass 4 Layer C) · **F5 rides Pass 3** · **F6 pointed at Pass 4** (the tracer landing). Prior: 2026-06-19 — routine `/vault-audit` ([[2026-06-19-vault-audit]]), mid-tracer: **healthy, no P0/P1**; two prior findings closed (the inverted §7 n8n flag → fixed; `AI Agent Roles` → wired); 4/6 critic-confirmed, 1 deflated, 0 false-positives. Prior: 2026-06-17 — first `/vault-audit`, healthy, settled the Contested n8n item.

---

## Snapshot — 2026-06-19 (routine run)

> UTF-8-correct PowerShell scan; excludes `.git`/`.obsidian`/`.claude` and the audit instrument under `_meta/audits/`.

| Metric | 2026-06-17 | 2026-06-19 |
|---|---|---|
| Content notes (`.md`, excl `_meta`) | 167 | **176** (+9: tracer note, 2 session logs, brainstorm…) |
| Top-level folders | 22 | **22** (`00`–`17`, `97`–`99`, `_meta`) — match [[Vault Map]] on disk |
| Unique link edges | 834 | **956** |
| Orphan content notes | 11 (2 genuine) | **10 (~1 genuine — `Supplier Note System`)** |
| "Broken" targets | 42 distinct | **48 distinct** — genuinely-missing ≈ 0 (clusters are materials-MOC seed + doc placeholders + brand stubs, all exempt) |
| `confidence` | all valid | **all valid** (22 verified · 12 memory_seed · 10 likely · 3 needs_check) |
| `status` invalid | 3 | **3** — `proposed` (F1) · empty (F2) · `draft-for-verification` (a `_sources` archive — exempt) |
| Notes lacking frontmatter | 3 | **3** — `CLAUDE.md`, `README.md`, one `_sources` prompt (operating files; exempt) |
| Top hubs (inbound) | The Heart (30) | **The Heart (37) · Kronos (27) · Capture Backlog (27) · Vault State Memory (26) · Doctrine (24)** |

---

## Open
*Confirmed findings awaiting Orfeas's action. Labels from [[2026-06-19-vault-audit]].*

- **F5 (P2, carried) — `README_START_HERE.md` rewrite** still pending (pre-pivot 4-layer framing; mitigated by its banner + `CLAUDE.md §9`). **Now scheduled: rides Pass 3 of the consolidation sequence (baseline §16-E), gated on ADR-0008.** Effort: M.
- **F6 (standing gap, Orfeas's call — not a defect) — ship-coupling still structurally open but now *actively being worked*.** 11 CSVs hold zero rows; no structured `Client -`/`Order -` record notes; [[The Selection Engine]] L164 dangles `Client - Kaliontzis Fotis` + `Project - Igeiasi Offices`. The tracer interview **completed A–G 2026-07-18**; **closure = Pass 4, the tracer final landing** (Layer D births the golden case + `Cases/`) — the landing matrix is staged in `docs/VAULT_BASELINE_2026-07-19.md` §7.

## Watch (deferred — not a defect)
*Tracked, intentionally not acting now.*

- **F4 (2026-06-19, re-armed 2026-07-19) — tracer ground-truth not yet in the `03` schemas / CSVs.** The interview completed A–G (2026-07-18); the correction set grew from 15 to **49**, now fully staged as the landing matrix in `docs/VAULT_BASELINE_2026-07-19.md` §7 (9 new tables · 24 gating decisions · 1 blocked item). **Trigger: Pass 4 Layer C** — the schema-diff executes there, after ADR-0011 declares the external-system boundaries (MEGASOFT = AR · Kostas-Excel = AP · stock Excel = inventory). Until then the CSV headers stay frozen (baseline §18). Closes when the diff lands.

## Done
*Findings resolved (with the date + how).*

- **F1 (Template - ADR `status: proposed`) — FIXED 2026-07-19** (§16-C mechanical batch): YAML now emits `status: seed`. (The body's `proposed | accepted | superseded` ADR-lifecycle prose stays — legitimate, per the 2026-06-19 report.)
- **F2 (Template - Project empty `status:`) — FIXED 2026-07-19**: defaults to `status: idea`. Same-class fix applied to `13_DAILY_NOTES/Daily Note Template.md` (empty status → `seed`), found by the baseline scanner.
- **F3 (Supplier Note System orphan/duplicate) — SUPERSEDED-MARKED 2026-07-19** per Overlap Registry **OV-01** (approved in the §17 review): warning banner + `status: complete`; canonical = [[Template - Supplier]], with both stale vs [[Supplier Research Workflow]] §A (OV-12 folds the vocabularies at Pass 4). **Deletion eligible after one audit cycle** (no-silent-deletion lifecycle).
- **Inverted `CLAUDE.md §7` n8n freshness flag (2026-06-17 F1) — FIXED, verified 2026-06-19.** §7 now reads as a settled pointer ("settled stack: Supabase Postgres + Python worker … a settled pointer, not an open task — if you ever find a note prescribing n8n as current, it's a regression: flag it"). The last source-of-truth conflict between the two most-read contract files is gone.
- **`08_AUTOMATION_AND_AI/AI Agent Roles.md` orphan (half of 2026-06-17 F4) — WIRED, verified 2026-06-19.** Now carries a resolving inbound `[[AI Agent Roles]]` edge; no longer an orphan. *(The other half, `Supplier Note System`, remains — now Open F3.)*
- **2026-06-16 audit P0 (structure↔index drift) — cleared.** Per [[Vault State Memory]] and verified on disk: phantom `15/16/18` resolved, 22 folders match [[Vault Map]], canonical index consolidated, schema governance settled. *(Re-confirmed clean 2026-06-17 and 2026-06-19.)*
- **Contested n8n question — SETTLED 2026-06-17 in favor of [[Vault State Memory]]: the sweep is COMPLETE.** Zero live notes prescribe n8n as current — all occurrences are negations, historical records (ADR-0004), or freshness guards. *(The residual inverted §7 flag is now also Done — see above.)*

## Contested — reconcile on next run
*Sources disagree; the audit exists to settle these. Not yet Done, not a confirmed Open finding.*

- _— none open. The n8n item was settled 2026-06-17 (moved to Done above). —_

## Rejected
*False positives — do not resurface. Each names why it is not real.*

- **"122 broken links" (em-dash mojibake) — 2026-06-17.** A `Get-Content -Raw` read mis-decoded UTF-8 em-dashes (`—`, char 8212) into mojibake, so every note whose name contains `—` (e.g. `Afoi Deli — Operating Doctrine`) appeared as both a broken target and an orphan. Reading with `[System.IO.File]::ReadAllText($p,[Text.Encoding]::UTF8)` resolves them all. **The links are fine; the script was wrong.** Always read UTF-8.

## Deferred
*Acknowledged, intentionally not acting now.*

- **`18_KNOWLEDGE` wing — deferred** (2026-06-16 audit P0-1). Subjects studied for their own sake live in `12_PERSONAL_OS` via [[Studies and Subjects]] until volume justifies a dedicated wing. Not a gap.

---

*Linked: [[Vault Integrity Audit]] (charter) · [[2026-06-16-vault-audit]] (first report) · [[The Heart]] · [[Vault State Memory]]. Nothing here is final.*
