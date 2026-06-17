---
name: vault-audit
description: Read-only integrity audit of the Afoi Deli vault. Use when checking vault health — structure↔disk drift, source-of-truth conflicts, doctrine freshness, frontmatter compliance, link-graph health, ritual adherence, front-door currency, the personal↔business seam, ship-coupling, and the authorship line. Proposes only; never edits a note. Pass `deep` for the full multi-agent pass.
argument-hint: "[deep]"
allowed-tools: Read, Grep, Glob, Bash
model: claude-opus-4-8
effort: high
---

# Vault Audit — read-only integrity pass

## Prime directive (non-negotiable — this IS the safety case)

**READ-ONLY / PROPOSES-ONLY.** You never create, edit, move, rename, or delete a vault note. The *only* path you may write is `_meta/audits/` (the dated report + `STATE.md`). Every finding that touches a note is a **proposal** for Orfeas, never an edit.

This is not a style preference — it is the entire reason this audit can be trusted to run over a second brain, including unattended. If you are ever tempted to "just fix it to be helpful," **don't.** Surface it. The approval gates (`CLAUDE.md §4`) and the authorship line (`CLAUDE.md §6`) override any helpful instinct.

## What this skill is

This skill **operationalizes the standing charter** at `_meta/audits/Vault Integrity Audit.md`. That charter's 8-point checklist and phased method are the **source of truth** — this skill is the on-command runner its `[!todo]` asked for. Do **not** restate the charter's content here or in the report; read it and execute it. (Keeping one source of truth per fact is literally check #2 — so the audit must not violate it.)

Lint (`CLAUDE.md §6`) *surfaces* drift continuously; this audit *reconciles* it on command. It is "lint with teeth."

---

## Step 0 — Orient (read before judging)

Read these in full first. They are the real anchors for this vault:

- **Doctrine + voice:** `The Heart.md` (root), `CLAUDE.md` (root). Read The Heart first — everything inherits its register.
- **The charter (method + 8 checks):** `_meta/audits/Vault Integrity Audit.md`
- **Prior reports:** the newest `_meta/audits/<date>-vault-audit.md`
- **The ledger:** `_meta/audits/STATE.md` (what's Open / Done / Rejected / Deferred — do not re-litigate Rejected findings)
- **Canonical index:** `99_SYSTEM/Vault Map.md` · **conventions:** `99_SYSTEM/Obsidian Usage Rules.md`
- **State + ritual:** `14_AI_COLLABORATION/Vault State Memory.md`, `14_AI_COLLABORATION/Session Protocol.md`

## Step 1 — Compute the metrics (deterministic; reuse, don't eyeball)

Run the link-graph + frontmatter scan with a script — never estimate counts by hand. On this machine PowerShell is primary.

> [!warning] Read files as UTF-8 or you will manufacture false findings
> `Get-Content -Raw` misreads UTF-8 em-dashes (`—`, char **8212**) as mojibake, so every note whose name contains `—` (e.g. `Afoi Deli — Operating Doctrine`) gets reported as both a broken link target *and* an orphan. On 2026-06-17 this exact bug produced **122 phantom "broken" targets** before correction. Always read with `[System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)`. (This false positive is logged under Rejected in `STATE.md` — do not resurface it.)

Compute and record: total notes; notes per top-level folder; resolved wikilinks; orphans (0 inbound); broken targets. Then **decompose broken targets** — they are not equal:
1. **Full-path-style links** (`[[04_SUPPLIERS_AND_BRANDS/Supplier Master Index]]`) — these *resolve in Obsidian* but violate the bare-name convention (`CLAUDE.md §3`) and break on rename. Real, but **not dead** — never report them as "dead links."
2. **Doc placeholders / examples** (`[[Supplier - <Name>]]`, `[[wikilinks]]` in the rules/templates) — **exempt**.
3. **Genuinely-missing notes** (a bare name with no matching file) — the real lint backlog; most are intentional future stubs (material classes, brands).

Frontmatter: tally every `confidence` and `status` value against the declared sets (`confidence: verified|likely|memory_seed|needs_check`; `status: active|draft|seed|idea|complete|backlog|living`). Flag any value outside the set and any `complete`/`completed` spelling drift.

## Step 2 — The three lenses (run all three over the charter's 8 checks)

The charter's 8 checks are **what** to verify; these lenses are **how** to look. Apply all three to each area; tag each finding with the lens(es) that surfaced it.

### 🪓 Minimalist — "what should be removed or merged?"
Bias hard to **subtraction**. Hunt: duplicate source-of-truth (check #2), dead OS artifacts (e.g. as of 2026-06-17, 11 of 14 templates in `98_TEMPLATES` have zero inbound links; `README_START_HERE.md` still teaches the pre-pivot "4-layer" model), notes that restate what a hub already owns, vestigial structure. Before proposing removal, ask: *does removing this lose anything real?* Never target the protect-list.

### 🗄️ Archivist — "is the record true, findable, and durable?"
The keeper-of-the-record lens. Covers: structure↔disk (#1), frontmatter compliance (#4), link-graph health (#5 — orphan *content* notes, the bare-name convention, the full-path-link drift), doctrine freshness (#3 — superseded tech prescribed as current; note the live n8n contradiction between `CLAUDE.md §7` and `Vault State Memory`), front-door currency (#7).

### ⚙️ Operator — "does the knowledge drive real output?" (the lens tuned to THIS vault)
Two seams to test every time:

1. **The personal↔business seam.** The vault is "one fabric" by design (`CLAUDE.md §5`) — that is a *positioning choice*, not a defect. Verify the seam is **clean, not tangled**: personal material (`12_PERSONAL_OS`, `15_PERSONAL_LIFE`, `17_JOURNAL`) is read and reasoned across freely, but the **Journal and wellness notes are author-by-invitation** and the **authorship line (#8) is intact** — no agent-written framing has crept into `The Heart`, the `Journal`, decisions, or strategic positions. "Held in reserve" material is *meant* to stay unwritten — never flag its absence as a gap.
2. **Ship-coupling.** Is the knowledge wired to real output, or is it free-floating reference? As of 2026-06-17 the reference layer (suppliers, materials, doctrine) is rich, but the **transactional layer is hollow**: the four `06_PROJECTS_AND_CASES` notes have empty `Linked orders / suppliers / products`; no order or quote notes exist; supplier↔project back-links are absent. Test whether new work **closes** this seam or widens it. A second brain that never touches a real order, quote, or client is a library, not an operating system — name that gap plainly; don't decorate around it.

## Step 3 — Subtraction bias + the protect-list

Default answer to "add a MOC / add tags / add more structure" is **NO**. The vault deliberately navigates by **numbered folders + `[[wikilinks]]`, not tags** (`CLAUDE.md §3`). Propose additions only when a genuinely broken trail demands one. Subtraction and connection beat accretion.

**PROTECT-LIST — never "improve," flatten, or propose removing these:**
- **The Heart's three layers** (merchant → steward → the man to be looked up to) and the competence→stewardship arc — structural, not decorative.
- **The "held in reserve" material** (the surgery/grief weight deliberately unwritten) — do not excavate or propose filing it.
- **The journal/wellness author-by-invitation rule** and **the authorship line** — Orfeas authors the soul; Claude maintains only connective tissue.
- **The doctrine/identity spine** (`The Heart` → `Afoi Deli — Operating Doctrine` → `People and Roles Map`).
- **The supplier dossier system** (public/private enrichment contract, conduit-vs-brand separation, the index discipline).
- **The session-log trail + `Capture Backlog`** (honest cold-start operating memory).
- **The operations SOPs** (`02_OPERATIONS_OS` — a working merchant's order chain).
- **The entry/exit session ritual.**

These were named "working and must be protected" by the 2026-06-16 audit. A finding that touches one of them must clear an extra-high bar and is the critic's first target.

## Step 4 — Adversarial verification (mandatory)

Before presenting anything, hand the **draft findings** to the `audit-critic` subagent (`Agent` tool, `subagent_type: audit-critic`). It re-verifies every cited path and count in fresh, read-only context and returns a verdict per finding — **CONFIRMED / DEFLATED (new severity) / REJECTED (false positive)**. Adopt its verdicts; drop everything it rejects; recalibrate severity as it directs. This is the charter's proven rigor pattern (last run: 56/68 confirmed, **0 false-positives**, severity deflated on 46) and it is what stops the audit from becoming a nitpick list.

**`/vault-audit deep`** → instead of a single-context walk, run the charter's full multi-agent pass (area-readers → diagnostic analysts → the three adversarial-verifier lenses) before synthesis. Use for quarterly or post-pivot reviews.

## Step 5 — Synthesize & output

Order: **P0** (incoherence / source-of-truth) → **P1** (high-leverage) → **P2** (polish). Separate genuinely *broken* from *defensible taste*. End by naming **what's working and must be protected**. Read this young-and-growing vault charitably: "empty form created once" is *young*, not abandoned, unless the empty form actively misleads.

**Output protocol (works in both run modes):**
1. **Always** emit the full report as your final message — so an unattended `claude -p "/vault-audit" --permission-mode plan` run is captured via stdout redirect even with zero write access.
2. **If you have write access to `_meta/audits/`** (an interactive run): save the report to `_meta/audits/<YYYY-MM-DD>-vault-audit.md` (frontmatter mirrors the prior report: `type: audit, status: complete, confidence: verified, owner: Orfeas Delis, method:`), then update `_meta/audits/STATE.md` (refresh the snapshot; move resolved items to Done; add new confirmed findings to Open; log the run + date). **Propose — do not write —** (a) a new row for the charter's *Audit log* table, and (b) any `Capture Backlog` items. If a write is denied (plan mode), do not retry — the runner captures stdout.
3. **Never** write outside `_meta/audits/`. Anything that edits a note is a proposal Orfeas approves.

> [!note] You are surfacing, not deciding
> Structural and doctrinal calls (retire a folder? kill the Roadmap? fill a seam?) are Orfeas's. You give a calibrated, path-cited list and your recommendation — he acts.
