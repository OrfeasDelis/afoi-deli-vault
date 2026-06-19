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

**Last session:** 2026-06-19 — **routine `/vault-audit` run executed** ([[2026-06-19-vault-audit]]), mid-tracer. Verdict: **healthy, no P0/P1.** Two prior findings closed (the inverted §7 n8n flag → fixed; `AI Agent Roles` → wired). 4 carried P2 polish remain + 1 new deferred watch-item (the MEGASOFT schema-diff). 4/6 critic-confirmed, 1 deflated, 0 false-positives. Prior: 2026-06-17 — first `/vault-audit`, healthy, settled the Contested n8n item.

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
*Confirmed findings awaiting Orfeas's action. Labels from [[2026-06-19-vault-audit]] (4 confirmed P2, 0 false-positives).*

- **F1 (P2) — `98_TEMPLATES/Template - ADR.md` L4** emits `status: proposed` (invalid). Set YAML to `status: idea`/`seed`. *(Carried from 2026-06-17.)* Effort: XS.
- **F2 (P2) — `98_TEMPLATES/Template - Project.md` L12** emits an empty `status:`. Default it (`status: idea`) or make it a Templater prompt. *(Carried.)* Effort: XS.
- **F3 (P2) — `04_SUPPLIERS_AND_BRANDS/Supplier Note System.md`** is a genuine content orphan (0 inbound) + redundant `{supplier_name}` skeleton duplicating `Template - Supplier`. Merge into / delete in favour of the real template, or relocate to `98_TEMPLATES`. *(Carried — the `AI Agent Roles` half of the prior 2-orphan finding is now Done.)* Effort: S.
- **F5 (P2, carried) — `README_START_HERE.md` rewrite** still pending (pre-pivot 4-layer framing; mitigated by its banner + `CLAUDE.md §9`). Already a [[Capture Backlog]] P2. Effort: M.
- **F6 (standing gap, Orfeas's call — not a defect) — ship-coupling still structurally open but now *actively being worked*.** 11 CSVs hold zero rows; no structured `Client -`/`Order -` record notes; [[The Selection Engine]] L164 dangles `Client - Kaliontzis Fotis` + `Project - Igeiasi Offices`. **But the tracer ([[Capture Backlog]] Priority 0.1) is the live effort closing it** — first ground-truth landed 2026-06-19. Decision: spin the Skintzi order into real records, or keep capturing process first.

## Watch (deferred — not a defect)
*Tracked, intentionally not acting now.*

- **F4 (2026-06-19) — MEGASOFT + rebate ground-truth not yet in the `03` schemas.** [[Order Lifecycle — Ground-Truth Capture]] §6 lists 15 schema-corrections (incl. MEGASOFT as external AR system-of-record + a `rebates` table) absent from `Invoices and Payments Schema` / `Database Master Schema` / `People and Roles Map`, with no back-pointer. **Deliberately deferred** to the tracer's "final landing" (post-interview; D–G still open) — tracked, not drift. The critic deflated it from P2 to a watch-item. No action now; the schema-diff closes it when the interview lands. Optional: a one-line back-pointer banner on the 3 schema notes while in flight.

## Done
*Findings resolved (with the date + how).*

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
