---
name: repo-analysis
description: Regenerate the living repository analysis (docs/REPO_ANALYSIS.md + the README summary block) — evidence-grounded architecture/business-model/workflow profile with Mermaid diagrams. Run after every git pull that brings note changes and before every end-of-session push (CLAUDE.md §8). Default is a delta run against the last recorded snapshot commit; pass `deep` for the full multi-agent regeneration.
argument-hint: "[deep|delta]"
allowed-tools: Read, Grep, Glob, Bash, Write, Edit, Agent, Workflow
effort: high
---

# Repo Analysis — the living repository profile

You are a **Principal Knowledge-Systems Analyst** holding three lenses at once: PKM/Obsidian architect, business strategist, and process engineer. You regenerate `docs/REPO_ANALYSIS.md` so it always matches the vault as it is **now** — rigorous, specific to THIS repository, rendering correctly on GitHub.

This document is **Claude-maintained reference layer** (CLAUDE.md §6 authorship line): connective tissue, not doctrine. It describes; it never decides. The Heart, the Journal, and strategic framing stay Orfeas's.

## Outputs (stable paths — every run overwrites cleanly)

1. `docs/REPO_ANALYSIS.md` — the full profile.
2. **The tree suite** — `docs/WORKFLOW_TREE.md` (hierarchical workflow tree; the sequential flowcharts stay in REPO_ANALYSIS §6 — never duplicate them), `docs/FAMILY_TREE.md` (the house of Deli + the lineage of ideas; role-level only), `docs/RELATIONSHIP_TREES.md` (supply ecosystem · people · data contracts · memory spine; numbers stay in REPO_ANALYSIS §2).
3. `docs/VISION.md` — vision · workflow · novelties · end goal · roadmap, compiled strictly from Orfeas-authored doctrine with citations (it synthesizes, never originates).
4. `README.md` — ONLY the block between `<!-- REPO-ANALYSIS:BEGIN -->` and `<!-- REPO-ANALYSIS:END -->` markers is regenerated. The block leads the repo front page and carries, in order: **"The vision, in brief"** (a condensed vision · workflow · novelties · end goal · roadmap, kept in sync with `docs/VISION.md`, figure-free), then the **At a glance** snapshot table, then the links to the full suite. **Never touch a byte outside the markers** — the surrounding README text is human-authored.

On delta runs, revise a suite file only where the underlying vault actually changed (e.g. a new supplier → supply-ecosystem tree; a tracer batch → workflow tree + roadmap; a people note → family tree). An untouched domain leaves its file byte-identical.

## Mode selection

- **`delta` (default):** regenerate against what actually changed since the last run.
- **`deep`:** full re-read of the vault (multi-agent). Use on explicit request, after structural shifts (folders added/retired, a re-architecture), or if the previous analysis is missing/corrupt.

## Procedure

### Step 0 — Anchor
1. Read the previous `docs/REPO_ANALYSIS.md` **first**. Extract: the recorded snapshot commit SHA (line `**Snapshot commit:**`), the Analysis version, and the full Changelog section (history is preserved verbatim — you only prepend).
2. `git rev-parse HEAD` → the new snapshot SHA. `git diff --name-status <recorded-sha>..HEAD` → the change set. If the diff fails (rebase, missing sha), fall back to a `deep`-style review and write "delta undetermined — full regeneration" in the changelog.

### Step 1 — Metrics (deterministic; never eyeball counts)
Run `python .claude/skills/repo-analysis/scripts/vault_metrics.py .` from the vault root and use ONLY its numbers for the snapshot table: note count, folder count, links, top hubs, orphans, frontmatter tallies, off-set `status`/`confidence` values. (The script reads UTF-8 — do not substitute PowerShell `Get-Content`, which manufactures phantom em-dash orphans; see the vault-audit skill's warning.)

### Step 2 — Focus the read
- **delta:** Read every changed/added note in the diff plus its immediate link neighbors when meaning shifted. If the change set touches only meta files (`docs/`, `README.md`, `.obsidian/`, `.claude/`, `.githooks/`, session logs alone), refresh metrics + changelog and revise no prose — say so in the changelog entry.
- **deep:** fan out domain readers with the Workflow tool — one reader per folder group (00, 01, 02, 03+97, 04, 05+06, 07, 08, 09–11, 12–17 personal, 14, 98+99+_meta+root), structured output, `zero hallucination / cite exact paths / stated-vs-inferred` rules. Reuse the reader prompt pattern from the first run (Session 2026-07-02).

### Step 3 — Regenerate `docs/REPO_ANALYSIS.md`
Stable section order (do not reorder between runs):
1. **At a glance** — 3–5 precise sentences.
2. **Snapshot metrics** — table incl. last-analyzed date + snapshot commit SHA.
3. **Architecture** — prose + Mermaid `graph TD` (subgraph zones/layers).
4. **Knowledge model & taxonomy** — frontmatter schema, status/confidence sets, MOC register.
5. **Business model** — synthesis prose + Mermaid map (canvas-style subgraphs).
6. **Workflow catalog** — each major workflow as a Mermaid `flowchart TD` (trigger, decisions, outputs, owner).
7. **Relationship map** — Mermaid `graph LR` at MOC/domain level + legend.
8. **Strengths, risks & next steps** — prioritized, evidence-anchored.
9. **Changelog** — reverse-chronological; each entry: date · commit SHA · added/removed/renamed notes, new MOCs/workflows, structural shifts, risks surfaced/resolved. Bump the `Analysis vN` line on material change.
10. **Methodology & provenance** — how generated, what was inferred vs stated.

### Step 4 — Refresh the README block
Regenerate only the marker-delimited block: what the vault is (3 sentences), the snapshot table (compact), link to `docs/REPO_ANALYSIS.md`.

### Step 5 — Self-check (all mandatory)
- [ ] Every cited path exists — verify deterministically: extract backtick-quoted `.md` paths from the doc and test existence with a short python check; remove or fix any miss.
- [ ] Every Mermaid block parses on GitHub: labels with spaces/punctuation wrapped in `["..."]`; no raw `()`:`;`#`{}` inside labels; short ASCII node IDs; ≤ 25 nodes per diagram (abstract to MOC/domain level above that); legend line per diagram (solid `-->` explicit link · dashed `-.->` inferred · thick `==>` primary flow).
- [ ] Explicit vs inferred relationships visually distinguished; interpretation labeled as such in prose.
- [ ] Changelog history preserved; snapshot SHA + date refreshed.
- [ ] Idempotent: an unchanged vault re-run would produce a near-identical file (stable ordering — alphabetical or by degree).
- [ ] No generic filler; every section says something true and specific to this vault.

## Hard rules (override any instinct to be complete)

- **Confidentiality:** never restate concrete commercial figures — discount cascades, net prices, credit terms, revenue, margins. Name the note that holds them (e.g. "commercial terms live in the Kronos dossier's private fields") and move on. The repo is private but this doc is its front door — keep it clean enough to screen-share.
- **Personal wing (12/13/15/16/17):** describe structure and system design only. Never quote the Journal or wellness notes; no intimate details. The seam between the halves IS worth describing; its contents are not.
- **Zero hallucination:** never reference a file, link, tag, or count you have not verified this run. When unsure, omit or flag.
- **Voice:** use the vault's own vocabulary (ΚΟΥΒΑΣ, conduits, the tracer, the 5-layer OS). If you overlay an external frame (e.g. Business Model Canvas), say so explicitly.

## Recurrence wiring (how this stays living)

Three layers keep the analysis current — this skill is the engine they all call:

1. **CLAUDE.md §8** — every session ends by running this skill (delta) *before* the commit, so the refreshed analysis rides the same push.
2. **Claude-harness guard** (`.claude/hooks/git-sync-guard.mjs`, wired in `.claude/settings.json`): blocks an in-session `git push` whose outgoing commits touch vault notes but not `docs/REPO_ANALYSIS.md`; nudges after an in-session `git pull` that brings note changes. Bypass for emergencies: set `SKIP_REPO_ANALYSIS_GUARD=1`.
3. **Git hooks** (`.githooks/pre-push`, `.githooks/post-merge` — warn-only, never block): cover pushes/pulls made outside Claude Code, including Obsidian Git. Fresh clone setup: `git config core.hooksPath .githooks`.

At session end, report in one paragraph what changed in this run's analysis.
