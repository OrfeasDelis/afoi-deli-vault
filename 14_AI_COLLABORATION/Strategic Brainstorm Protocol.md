---
type: protocol
created: 2026-06-17
status: active
confidence: verified
owner: Orfeas Delis
aliases:
  - Brainstorming Guidance
  - Strategic Brainstorm
  - OS Brainstorm
---

# Strategic Brainstorm Protocol

> [!abstract] What this is
> The standing practice for **stepping back from build detail to think *with* Orfeas about the vault and the Afoi Deli OS as a whole** — where it actually stands, what "the OS is real" means, the gap between the stated end-product and current reality, and the load-bearing next steps. This note is the **charter** (the *why / when / what-good-looks-like*); the runnable five-phase version is the **`/os-brainstorm` skill** (`.claude/skills/os-brainstorm/SKILL.md`). Together they mirror the audit system's split: [[Vault Integrity Audit]] (charter) + `/vault-audit` (runner).

## Why this exists

The vault accretes — sources ingested, dossiers deepened, schemas extended. That is healthy, but it has a failure mode: **building reference depth and beautiful documents while mistaking them for a working system.** Periodically the build needs to stop and get honestly grounded — not "what shall we add next," but *"what is this actually, where are we really, and what is the one foundation the rest depends on?"*

This is the strategic complement to the health audit:

|                      | Reconciles                                                 | Asks                                           | Runner                    |
| -------------------- | ---------------------------------------------------------- | ---------------------------------------------- | ------------------------- |
| **`/vault-audit`**   | vault **health** — drift, orphans, links, schema, ritual   | *Is the record true, findable, durable?*       | [[Vault Integrity Audit]] |
| **`/os-brainstorm`** | strategic **completeness** — vision vs reality, sequencing | *Is the OS real, and what makes it real next?* | this note                 |

A vault can pass the audit (healthy, coherent, well-linked) and still fail the brainstorm (a rich library that has never run a real order). Keep the two questions separate.

## When to run it

- At an **inflection point** — before committing to a build phase, or when the next move isn't obvious.
- When the **gap between the vision and the reality** has gone fuzzy and needs naming out loud.
- When you feel the **cathedral-before-the-foundation** pull — lots of elegant structure, no load-bearing spine yet.
- As a **periodic re-grounding**, the way the audit is a periodic health check.

It is a *discussion*, not a deliverable. Don't run it to produce a document — run it to think.

## The mode (guardrails — non-negotiable)

1. **Read-only / propose-only on the knowledge base.** The session edits, creates, or deletes **no vault content note** and implements nothing. Its *one* write is its own **dated brainstorm log** in `14_AI_COLLABORATION/Brainstorms/` — committed and pushed like a session — exactly as `/vault-audit` stays read-only on notes yet writes its report to `_meta/audits/`. It does **not** auto-update [[Vault State Memory]] or file decisions into the Roadmap/ADRs/Backlog; those are *promotions* Orfeas acts on separately (see the trail below). This is the only respect in which it departs from `CLAUDE.md §8` — it writes its log, not the build-session state.
2. **Think *with* him, not *for* him.** Real back-and-forth, maximum reasoning depth, questions one or two at a time — not a wall of conclusions.
3. **Lean on the audit; don't re-derive it.** The deterministic health layer (drift, orphans, links, schema) is already tracked in `_meta/audits/STATE.md` — cite and extend it. Spend original reasoning on the *strategic* layer the audit only gestures at (its **F7 — ship-coupling**).
4. **Use the 5-layer model as the reality scaffold** (Knowledge/Obsidian → Data/Supabase → Automation/Python worker → Interface/webapp → AI Agent). "What exists vs. what is specified" is largely "which layers actually run." Today: Layer 1.
5. **The voice of [[The Heart]]** — level-headed, truthful, helpful, self-respecting. No flattery. Path-cite; flag inference.
6. **No subagent fan-out.** One coherent interlocutor, not a synthesized report (also Orfeas's standing preference).
7. **You are surfacing, not deciding.** The **authorship line** holds hardest here: you sequence options, expose dependencies, and sharpen the choices — but the strategic decisions and the framing stay Orfeas's to author. This is exactly the soul/connective-tissue split in `CLAUDE.md §6`. If converging would mean writing his position for him, stop and hand it back.

## The five phases (full version in the skill)

0. **Lock scope** — `business` (the 5-layer ship-running machine) or `unified` (whole vault incl. the personal OS). Ask, don't assume.
1. **Read the vault** — complete, layered pass (contracts → doctrine → specs → runbooks → the rest), tracing links into a model of the system.
2. **Situation report** — what the OS *is*; what's DECIDED; working vs specified vs conceptual (on the 5-layer scaffold); contradictions / stale docs / orphaned forward-references; **the gap**.
3. **Discussion** — anchored on three questions in order: *what does "real" mean → where are we reaching → what are the load-bearing next steps?*
4. **Converge** — a sequenced **skeleton** of essential next steps with explicit dependency logic. Emerges from the talk; not front-loaded.

## The brainstorm trail (like the session trail)

We will brainstorm often, so each run leaves a dated **brainstorm log** in `14_AI_COLLABORATION/Brainstorms/` — the brainstorm equivalent of a session log. They accumulate and are auto-listed here, newest first:

```dataview
LIST
FROM "14_AI_COLLABORATION/Brainstorms"
SORT file.name DESC
```

Each log (from [[Template - Brainstorm Log]]) records: scope, the situation-report snapshot, **the real discussion turns** (what got challenged, what moved), the converged skeleton, and the **proposed promotions**. The log is written and committed by the `/os-brainstorm` skill at Exit; the folder is born on the first run. *(Empty above until then.)*

## Where the outcomes go (promotions — deliberately, afterward)

The log *captures* the thinking; **filing binding outcomes is a separate, chosen step** Orfeas takes — the brainstorm never does it itself. The log proposes; he disposes:

- A binding decision → a new row in [[Architecture Decision Records]].
- A re-sequenced plan → [[Roadmap]] (and retire what it supersedes).
- A concrete next action → [[Capture Backlog]].
- A new live question → [[Open Questions]].
- The state shift → [[Vault State Memory]] at the next *build* session.

That separation is the point: the brainstorm is where the thinking is free and the trail is kept; promotion into doctrine is a decision Orfeas makes with the thinking already done.

---

*Linked: [[Collaboration Home]] (hub) · [[Session Protocol]] (sibling ritual) · [[Vault Integrity Audit]] (the health counterpart) · [[The Heart]] · [[Vault State Memory]]. Runner: `/os-brainstorm`. Trail: `14_AI_COLLABORATION/Brainstorms/`. Nothing here is final.*
