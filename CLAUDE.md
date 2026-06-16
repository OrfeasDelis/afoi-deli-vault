# CLAUDE.md — Operating Instructions for This Vault

This is the **AFOI DELI SECOND BRAIN**: the unified knowledge + operating system for both **Afoi Deli Floor + Bath** and **Orfeas Delis as a person**. Business and personal are one fabric here, not two vaults. Read this at the start of every session.

This vault follows the **LLM-Wiki pattern** (Karpathy): immutable raw sources → an LLM-maintained, interlinked wiki → this schema file that governs how the wiki is built and kept current. Knowledge is *compiled once and kept current*, not re-derived from scratch on every query. See §6 for the operating loop.

---

## 0. Read The Heart FIRST

Before anything else — before business memory — read [[The Heart]].

It is the foundational note, above the folder structure. It holds the doctrine, the lineage, the two maxims, and the voice. Every draft, every client message, every decision this vault helps with inherits its register: **level-headed, truthful, helpful, self-respecting; create the circumstances rather than ask.** A session that hasn't read The Heart doesn't yet know who it's working for.

---

## 1. Then load memory

After The Heart, read in this order:

1. `14_AI_COLLABORATION/Vault State Memory.md` — source of truth for current state.
2. The latest log in `14_AI_COLLABORATION/Sessions/`.
3. `14_AI_COLLABORATION/Roadmap.md` and `14_AI_COLLABORATION/Open Questions.md`.
4. `00_COMMAND_CENTER/Capture Backlog.md` — what to work on next.

Then briefly confirm current state and proposed focus with Orfeas before acting. Full workflow: [[Session Protocol]].

> [!warning] These boot notes drift — sanity-check before trusting them
> [[Roadmap]] and [[Open Questions]] are the stalest notes in the vault (pre-pivot); treat any n8n reference in them as superseded per §7. Before trusting [[Vault State Memory]]'s structure section, confirm it against [[Vault Map]] (the canonical folder index) and the actual folders on disk. `18_KNOWLEDGE` is intentionally **deferred** — not on disk; studies live in `12_PERSONAL_OS` via [[Studies and Subjects]].

---

## 2. Identity & context

- **Who:** Orfeas Delis — second-generation successor to Afoi Deli, son of [[The Heart|Kostas]] (founder, the merchant's nerve and intuition) and Chrysoula (the closer). Brother Ektoras; partner Eleni. The full picture lives in [[The Heart]] and [[People and Roles Map]].
- **The arc:** competence → stewardship. The work is holding the whole — business, self, relationships — at a standard, not just doing the work well.
- **Working principle to honor:** *nothing in this vault is final.* Notes are living; revise and enrich freely. Don't treat foundations as monuments.
- **Voice for any drafted output:** see [[The Heart]] and [[Premium Human Email Tone]]. Discreet, earned, never over-promising.
- **Business strategy frame:** the moat is the **uplift engine**, not the brand portfolio — see [[Afoi Deli — Operating Doctrine]].

---

## 3. Conventions (always)

- Every note: YAML frontmatter `type`, `created`, `status`; add `confidence` for factual notes.
- **Confidence (exhaustive set):** `verified | likely | memory_seed | needs_check`. No other value is valid — templates and workflows must emit only these. Mark uncertainty with `needs_check`; never guess silently.
- **Status (allowed set):** `active | draft | seed | idea | complete | backlog` (plus `living` for continuously-revised foundation notes like [[The Heart]]). Use `seed` for an intentionally-empty scaffold so it's distinguishable from abandoned work. (`completed` is a deprecated spelling of `complete` — don't use it.)
- `type` is a free-text human label, **not** a query facet — don't try to normalize it. The real navigation system is **numbered folders + `[[wikilinks]]`** (tags are not used here).
- Naming `Entity - Name`; numbered folders; link by **bare note name** (`[[Supplier - Kronos]]`, not `[[04_SUPPLIERS_AND_BRANDS/...]]`) so links survive renames. Link aggressively.
- **Inbound-link rule:** every new content note must earn at least one **inbound** link — from its folder index/MOC or a relevant hub — in the same session it's created. Outbound links alone don't count; a note with zero inbound links is unfinished.
- One note = one purpose; keep facts separate from opinions.
- Full rules: [[Obsidian Usage Rules]] and [[RAG Knowledge Base Rules]].

---

## 4. Approval gates — business (never act autonomously)

Claude may DRAFT, but a human must APPROVE: sending emails, changing order status, changing prices, approving supplier proformas, notifying clients of delays, changing delivery promises, updating financial records.

**Obsidian is the memory; the agent is never the source of truth.**

---

## 5. Handling the personal half

The vault holds genuinely personal material (`15_PERSONAL_LIFE`, `17_JOURNAL`, and anything linked from The Heart). The rule:

> [!important] Open to read and reason, reserved to write
> **Read, link, and reason across personal material freely** — it's here to be used, and the vault is unified on purpose. Treat it with the same seriousness as business knowledge.
> **But the [[Journal]] and wellness notes are author-by-invitation.** Surface them, discuss them, reference them — do **not** write into them unprompted. The journal is Orfeas's own voice; an AI appending to it without being asked would corrupt the one place meant to be his.
> Some things are deliberately **held in reserve** (see the note at the foot of [[The Heart]]). Don't press them into files because they came up. Let them be lived first.

---

## 6. The operating loop — ingest / query / lint

The vault is a *compounding artifact*, not a static archive. Three operations keep it growing and current. (Adapted from the LLM-Wiki pattern.)

### Ingest — a new source enters
When Orfeas drops a source (a catalog, an email thread, an article, a transcript, a set of notes) and asks to process it:
1. Read it. Discuss the key takeaways with Orfeas first — don't file silently.
2. Write a summary/entity page in the right folder, with frontmatter + confidence.
3. **Update the affected existing pages**, not just the new one — a single source often touches several (a supplier note, a project, an index, a knowledge map). Strengthen or challenge what's already there; flag where new data contradicts old.
4. Append an entry to the current session log.
- Default to ingesting **one source at a time, with Orfeas involved** (he reads summaries, guides emphasis). Batch only when he asks.

### Query — a question is asked
When Orfeas asks a question against the vault:
1. Read the relevant index/MOC pages first, then drill into the specific notes. (At this scale the index is enough — no embedding search needed yet. QMD is the documented future option if the vault outgrows the index.)
2. Answer with citations to the notes used.
3. **File good answers back into the vault as new pages.** A comparison, an analysis, a connection worth keeping should become a note — not vanish into chat history. This is how explorations compound like sources do. Ask Orfeas where it should live if unclear.

### Lint — a periodic health check
When asked to lint (or at natural milestones):
- Find contradictions between pages, stale claims newer sources have superseded, orphan pages with no inbound links, concepts mentioned but lacking their own page, missing cross-references, and gaps a web search could fill.
- Surface them as a list for Orfeas to act on — don't silently auto-resolve. (The freshness flags in §7 are standing lint items.)

> [!warning] The authorship line — this overrides the pattern's default
> The LLM-Wiki pattern's default is "you never write the wiki yourself." For the **reference layer** (suppliers, products, operations) that's correct — Claude writes and maintains it. **But for the parts that are *Orfeas* — [[The Heart]], the [[Journal]], decisions, framing, the strategic positions — authorship stays with him.** Claude maintains the connective tissue (links, summaries, consistency); Orfeas authors the soul. If the LLM writes the framing and the decisions, the continuity quietly stops being his. Maintain this split deliberately.

> [!important] Non-negotiable vs best-effort
> This loop is **prose-enforced** — no slash commands or hooks back it, so adherence depends on you reading it each session. Never skip: (1) read [[The Heart]] + [[Vault State Memory]] at start; (2) honor the §4 approval gates; (3) at session end, update [[Vault State Memory]] and commit + push. Best-effort (do when there's room): full lint sweep, ADR logging, [[Roadmap]]/[[Open Questions]] pruning. If you skip a best-effort step, say so in the session log.

---

## 7. Freshness flags — read before trusting old doctrine

> [!warning] Known stale areas (verify, don't inherit blindly)
> - **n8n is still named as the *current* automation layer in ~15 live notes** — live prescriptions an implementer would follow, not incidental mentions: [[Roadmap]] Phase 3, [[Home Dashboard]] axis 5, [[Strategic Axes]] axis 5, the automation sections of [[Kouvas System]] / [[Supplier PO Creation SOP]] / [[Order Workflow 0-4]], [[Database Master Schema]]'s target line, and [[Hermes Obsidian Codex Interface]]. The settled architecture is **Supabase Postgres + Python worker, no n8n** (see [[Automation Masterplan]] and [[Python Worker Map]]). Replace every n8n prescription with the worker. Tracked as one owned task in [[Capture Backlog]] (P1) — scoped work, not a perpetual flag.
> - Several supplier notes remain `memory_seed`. [[Supplier - Kronos]] is `likely`. Promote others as they're verified.

---

## 8. End every session

1. Update `14_AI_COLLABORATION/Vault State Memory.md`.
2. Write a session log from [[Template - Session Log]] into `14_AI_COLLABORATION/Sessions/`.
3. Update Roadmap / Open Questions / Capture Backlog / ADRs if they changed.
4. Commit + push:
   ```bash
   git add -A
   git commit -m "<type>: <summary>"
   git push
   ```
   Types: feat, fix, docs, chore, refactor. Repo: private `afoi-deli-vault` (account `OrfeasDelis`).
   Note: PowerShell on this machine does NOT accept `&&` — run git commands on separate lines.

---

## 9. Start here in Obsidian

[[Collaboration Home]] is the working hub. The canonical philosophy + current state are **[[The Heart]]** (the soul, the voice, the doctrine) and **[[Vault State Memory]]** (where the build actually is); the canonical folder index is **[[Vault Map]]**. Root: [[The Heart]].

> [!warning] `README_START_HERE.md` is a historical onboarding artifact — pre-pivot (it still names n8n and a now-retired "4-layer" model). Do not treat it as current doctrine until rewritten. Use The Heart + Vault State Memory instead.
