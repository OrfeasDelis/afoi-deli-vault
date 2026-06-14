# CLAUDE.md — Operating Instructions for This Vault

This is the **AFOI DELI SECOND BRAIN**: the unified knowledge + operating system for both **Afoi Deli Floor + Bath** and **Orfeas Delis as a person**. Business and personal are one fabric here, not two vaults. Read this at the start of every session.

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

Then briefly confirm current state and proposed focus with Orfeas before acting. Full workflow: [[Session Protocol]].

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
- Confidence: `verified | likely | memory_seed | needs_check`. Mark uncertainty — never guess silently.
- Naming `Entity - Name`; numbered folders; `[[wikilinks]]`, link aggressively.
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

## 6. End every session

1. Update `14_AI_COLLABORATION/Vault State Memory.md`.
2. Write a session log from [[Template - Session Log]] into `14_AI_COLLABORATION/Sessions/`.
3. Update Roadmap / Open Questions / ADRs if they changed.
4. Commit + push:
   ```bash
   git add -A && git commit -m "<type>: <summary>" && git push
   ```
   Types: feat, fix, docs, chore, refactor. Repo: private `afoi-deli-vault` (account `OrfeasDelis`).

---

## 7. Freshness flags — read before trusting old doctrine

> [!warning] Known stale areas (verify, don't inherit blindly)
> - **`08_AUTOMATION_AND_AI` and the "5-layer model" in Vault State Memory still name .** The settled architecture is **Supabase Postgres + Python worker, no n8n** (see the Afoi Deli OS Builder's Manual). Treat the n8n workflow map and any n8n references as superseded until those notes are updated. Don't route automation planning through them.
> - Several supplier notes remain `memory_seed`. [[Supplier - Kronos]] is now populated from Orfeas directly (`likely`). Promote others as they're verified.

---

## 8. Start here in Obsidian

[[Collaboration Home]] is the working hub. `README_START_HERE.md` covers vault philosophy. Root: [[The Heart]].
