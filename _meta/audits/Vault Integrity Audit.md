---
type: protocol
created: 2026-06-16
status: active
confidence: verified
owner: Orfeas Delis
aliases:
  - Vault Integrity Audit
  - Vault Audit Protocol
tags:
  - meta
  - audit
  - vault-health
---

# Vault Integrity Audit

> [!abstract] What this is
> The **recurring** practice that keeps this vault honest about itself. A second brain compounds only if its account of itself stays true — and the [[2026-06-16-vault-audit|first audit]] showed how fast the structure, the operating contract, and the memory spine drift apart from what's actually on disk. This note is the standing charter: why we audit, when, how, and what we check every time. Individual audit reports live beside it as `_meta/audits/<date>-vault-audit.md`.

This note descends from [[The Heart]] (the vault exists to compound knowledge in service of the work) and from the **lint** operation in `CLAUDE.md §6`. The audit is lint with teeth: lint *surfaces* drift continuously; the audit *reconciles* it on a cadence.

---

## Why this exists

The vault's value is that it can be *trusted as memory*. The failure mode is silent drift: a folder gets renamed and the index doesn't; a tech decision is reversed but fifteen notes still prescribe the old one; the source-of-truth file starts describing folders that were never created. None of these throw an error. They just quietly make the vault lie. The audit's job is to catch that class of failure before it compounds.

> [!warning] The audit reconciles; it does not silently auto-fix
> Like lint (`CLAUDE.md §6`), an audit **surfaces a prioritized list for Orfeas to act on**. It may fix mechanical drift inline when asked, but structural and doctrinal decisions (retire a folder? maintain or kill the Roadmap?) are surfaced, not decided. And per the authorship line — Claude maintains the reference/connective layer; **Orfeas authors the soul** ([[The Heart]], [[Journal]], strategy, framing). An audit never rewrites those.

---

## Cadence (when to run)

**Proposed (confirm and adjust):**

- **Routine pass** — every ~10 working sessions, or monthly, whichever comes first. The lightweight [standing checklist](#the-standing-checklist) below; ~30 minutes.
- **Deep pass** — quarterly, or after any major structural change or doctrine pivot (e.g. the n8n→Python-worker pivot *should* have triggered one). The full [phased method](#the-method); the multi-agent workflow.
- **Always** — before onboarding a new tool/skill that reads the vault, and before any folder renumbering.

> [!todo] To formalize later (per Orfeas)
> Turn this into enforced tooling: a **`/vault-audit` skill** that runs the phased method on command, and **lint rules / hooks** that block the recurring drift classes at write-time (invalid `confidence`/`status` values, new orphan content notes, folder references that don't resolve). Until then this runs as a manual session against the checklist.

---

## The standing checklist

The durable integrity checks, each derived from a real failure the first audit found. A routine pass walks this list; anything that fails becomes a backlog item.

1. **Structure ↔ disk.** [[Vault Map]] and [[Vault State Memory]] §2 list **exactly** the folders that exist on disk — no phantom folders, no omissions. (First-audit failure: `15/16/18` referenced as live; `17_JOURNAL` missing from Vault Map.)
2. **One source of truth per fact.** Exactly one canonical folder index; one canonical data contract (schema `.md` vs `.csv`); no fact maintained in two places where the copies can drift. (Failure: two disagreeing indexes; Orders/Invoices schema-vs-CSV drift; Home Dashboard's axes vs [[Strategic Axes]].)
3. **Doctrine freshness.** No superseded technology is prescribed as *current* anywhere. Freshness flags (`CLAUDE.md §7`) are scoped to specific notes and owned as a task, not left perpetual. (Failure: n8n live in ~15 notes.)
4. **Frontmatter compliance.** Every `confidence` value ∈ the declared set; every `status` value ∈ the declared set; no spelling drift (`complete`/`completed`). Templates and workflows emit only valid values. (Failure: `confirmed`/`draft` manufactured by templates.)
5. **Link-graph health.** No orphan *content* notes (templates/READMEs exempt); no broken wikilinks; links use bare note names so they survive renames. (Failure: 16 orphans incl. [[The Selection Engine]]; `[[The Material Atelier]]` mandated but missing.)
6. **Ritual adherence.** Session logs show the entry/exit ritual was followed; the cold control notes ([[Roadmap]], [[Open Questions]], ADRs, [[Collaboration Home]]) are either maintained or **formally retired** — not silently rotting while the protocol still mandates them.
7. **Front door points to current doctrine.** `CLAUDE.md §9`, [[README_START_HERE]], and the READMEs route a new reader to *current* philosophy, not pre-pivot artifacts.
8. **Authorship line intact.** The soul notes are still authored by Orfeas; Claude has only maintained connective tissue. No agent-written framing has crept into [[The Heart]], the [[Journal]], or the strategic positions.

---

## The method (deep pass)

Run from the vault root, phased — read before judging:

0. **Orient** — map folders + note-counts; scan `git log` for edit-gravity (what's edited constantly vs. created once); inventory frontmatter keys/values; compute the link graph (hubs, orphans, broken links). Read every operating contract in full.
1. **Reconstruct philosophy** — from evidence (edit history + link patterns), not claims. Name explicit vs. revealed intent; the gap is the headline.
2. **Structure & coherence** — taxonomy, naming, frontmatter, tags-vs-folders-vs-links, single-source-of-truth, MOC freshness.
3. **Operating contract** — does `CLAUDE.md` make an agent behave well without re-explaining context? Stale rules, dead references, contradictions. Give *revised text*, not vague notes.
4. **Session workflows** — entry/exit rituals, the capture→process→file→retrieve loop, LLM-as-maintainer reality, periodic notes.
5. **Synthesize** — P0 (incoherence / source-of-truth) → P1 (high-leverage) → P2 (polish). Separate *broken* from *defensible taste*. Name what's working and must be protected. Write to `_meta/audits/<date>-vault-audit.md`.

> [!tip] Rigor pattern that worked the first time
> A multi-agent pass (area-readers → diagnostic analysts → **adversarial verifiers** that classify each finding broken-vs-defensible and recalibrate severity) caught real defects *and* deflated inflated ones — 56/68 findings confirmed, 0 false-positives, severity reduced on 46. Keep the adversarial-verification step: it's what stops an audit from becoming a nitpick list.

---

## Audit log

| Date | Scope | Headline verdict | Report |
|---|---|---|---|
| 2026-06-16 | Full structural + philosophical (first audit) | Healthy business-intel core; **P0 = source-of-truth drift** (two disagreeing indexes + phantom folders `15/16/18` + dual data contract). Doctrine spine + supplier system + session ritual are excellent and protected. | [[2026-06-16-vault-audit]] |

---

*Linked: [[The Heart]] · [[Vault State Memory]] · [[Session Protocol]] · [[CLAUDE]]. Nothing here is final — revise the cadence and checklist as the vault teaches us what actually drifts.*
