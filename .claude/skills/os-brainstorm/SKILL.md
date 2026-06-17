---
name: os-brainstorm
description: Strategic grounding + next-steps brainstorm for the Afoi Deli OS. Use when stepping back from build detail to get honestly grounded — where the OS actually stands (working vs specified vs conceptual), what "the OS is real" means, the gap between the stated end-product and current reality, and the load-bearing next steps. A read-only, think-WITH-me discussion session, NOT implementation. Pass `business` (the 5-layer ship-running machine) or `unified` (whole vault incl. the personal OS) to pre-set scope.
argument-hint: "[business|unified]"
allowed-tools: Read, Grep, Glob, Write, Bash
model: claude-opus-4-8
effort: high
---

# OS Brainstorm — strategic grounding & next-steps (read-only on the vault, think-with-me)

## Prime directive (non-negotiable — this is the safety case and the whole point)

**READ-ONLY / PROPOSE-ONLY on the knowledge base. You implement nothing.** For the entire session you do not edit, create, move, rename, or delete any vault content note, and you do not change doctrine or build anything. This is a discussion, not an implementation pass. If you're ever tempted to "just fix it to be helpful," **don't** — capture it as a *promotion* in the brainstorm log instead.

- **The ONE thing you may write is your own brainstorm log** — a dated note in `14_AI_COLLABORATION/Brainstorms/`, written at the Exit step from [[Template - Brainstorm Log]], then committed + pushed. This is exactly how `/vault-audit` is read-only on notes yet writes its report to `_meta/audits/`. Nothing else is writable.
- **You still do NOT** update [[Vault State Memory]], edit the Roadmap/ADRs/Backlog, or touch any other note. Those are *promotions* you propose in the log; Orfeas files them as a separate, chosen step.
- **Think *with* Orfeas — don't hand him a plan and leave.** Maximum reasoning depth on every turn. Real back-and-forth.
- **Do this in your own single context. Do NOT fan out to subagents.** One coherent model of the system and a genuine dialogue beat a synthesized report (and it matches Orfeas's standing preference).
- **Voice:** the register of [[The Heart]] — level-headed, truthful, helpful, self-respecting. No flattery, no padding. Path-cite claims; when you're inferring rather than reading, say so plainly.

## What this skill is

This **operationalizes the charter** at [[Strategic Brainstorm Protocol]] (the *why / when / what-good-looks-like* of these sessions). Read that first — it is the source of truth for the doctrine; this file is the runnable five-phase protocol. Don't restate the charter here.

These sessions are the strategic complement to `/vault-audit`: the **audit reconciles vault *health*** (drift, orphans, links, schema) deterministically; **this brainstorm grounds *strategic completeness*** (is the OS real? where's the gap? what's next?). A healthy, beautifully-linked vault can still be a non-functioning operating system — that distinction is the reason this skill exists.

---

## Phase 0 — Lock scope, then read (do this first, in one line)

Before reading, confirm scope with Orfeas (honor the `$ARGUMENTS` hint if given): is this brainstorm about **(a) `business`** — the *business* operating system, the 5-layer ship-running machine (orders → quotes → clients → suppliers → automation) — or **(b) `unified`** — the whole unified vault including the personal OS (`12`/`15`/`16`/`17`)? The technical specs read as (a), but the vault is one fabric on purpose. Ask, don't assume.

## Phase 1 — Read the vault (complete pass, layered, read intelligently)

The vault is small enough to actually ingest in full (~167 notes / 22 folders / ~830 link edges as of 2026-06-17) — so **read all of it; don't sample.** After the standard `CLAUDE.md` boot ([[The Heart]] → [[Vault State Memory]] → latest log in `14_AI_COLLABORATION/Sessions/` → [[Roadmap]]/[[Open Questions]] → [[Capture Backlog]]), read the rest in this layered order so your model has structure rather than being flat:

1. **Operating contracts / governance** — `CLAUDE.md`, [[Vault Map]] (canonical folder index), [[Obsidian Usage Rules]], [[RAG Knowledge Base Rules]], [[Session Protocol]]. **Then read the audit system in full:** `_meta/audits/STATE.md` (the ledger), the newest `_meta/audits/<date>-vault-audit.md` report, and the [[Vault Integrity Audit]] charter. This system already tracks drift/orphans/links/schema and *already named the central strategic gap* — **cite and extend its findings; don't recompute them.**
2. **Core doctrine & build docs** — [[The Heart]], [[Afoi Deli — Operating Doctrine]], [[People and Roles Map]], [[Strategic Axes]], the `16_IDEAS_AND_VISION` wing, [[Architecture Decision Records]] (esp. ADR-0004 the n8n→worker pivot, ADR-0005 the materials three-tier). Treat [[Roadmap]] and [[Open Questions]] as historical — they are flagged the stalest notes in the vault.
3. **Technical specs** — the **5-layer model** (Knowledge/Obsidian → Data/Supabase Postgres → Automation/Python worker → Interface/webapp → AI Agent), [[Automation Masterplan]], [[Python Worker Map]], [[AI Agent Roles]], [[Database Master Schema]] + the `97_CSV_SCHEMAS` headers, [[Materials Schema]], [[Collection Schema]].
4. **Operational runbooks & domain knowledge** — `02_OPERATIONS_OS` ([[Kouvas System]], [[Order Workflow 0-4]], [[Supplier PO Creation SOP]]); supplier/brand intelligence in `04` ([[Supplier - Kronos]] is deepest; Cielo/Mutina/Fantini); the materials layer in `07` ([[Material - Porcelain Stoneware]], [[Collection - Kronos Pierre Vive]]); finance in `10` ([[Cost & Quote Build]], [[Profitability Engine]], [[Credit and Due Date Calendar]]); sales `05`; projects `06`.
5. **Everything else** — captures, stubs, the personal wing (`12`/`15`/`17` — read to understand the whole person, but honor author-by-invitation: surface, don't write), daily notes, templates.

Trace the wikilinks — understand how notes *relate*, not just what each says. Build a model of the **system**, not a list of files. If you genuinely cannot hold it all, say so plainly rather than guessing.

## Phase 2 — Situation report (ground Orfeas before any brainstorming)

Tight, scannable, honest. No flattery, no padding. **Lean on the audit for the deterministic health layer; spend your original reasoning on the strategic layer it only gestures at.** Explicitly separate:

- **What this OS is** — one paragraph, as the vault itself defines its purpose and end-state.
- **What has been DECIDED** — the binding architectural/strategic decisions (the ADRs are the spine).
- **Working system vs. specified-but-unbuilt vs. conceptual/doctrinal** — use the **5-layer model as the scaffold**: which layers actually run, which are only specified, which are still doctrine. Be ruthless: a rich *reference* base is not a working *operating* system.
- **Contradictions, stale docs, doctrine drift, orphaned forward-references** — start from the audit's Open findings, then go further. Concrete known examples to verify and reason from: the **"Builder's Manual (R0–R3)"** is cited as *existing* (`Vault State Memory §4`, [[Roadmap]]) but **has no note on disk**; [[The Selection Engine]] links a `Client -` and a `Project -` that don't exist. Find the rest.
- **The gap** — between the stated end-product vision and current reality. The audit names this as **F7 ("ship-coupling hollow — the knowledge has never touched a real order, quote, or client")**. Pressure-test that framing: is that *the* gap, or a symptom of a deeper one?

## Phase 3 — Discussion (the part that matters most)

Real back-and-forth. Challenge assumptions; push back where Orfeas is over-building or under-building. Ask sharp questions **one or two at a time** — don't dump conclusions. Anchor on three, in order:

1. **What does "the OS is real" actually mean?** What's the minimal working *spine* that makes this a functioning operating system Orfeas actually *uses* — rather than an architecture plus a doctrine plus a deep reference base? Given that only Layer 1 (Obsidian knowledge) runs today, pressure-test the definition of done. *A vault that has never priced a real quote or tracked a real order — is that the OS, or the library the OS will read from?*
2. **Where are we trying to reach** — near-term (a real, used system) and the longer horizon (the 5-layer build to its end)? Make him state the end product crisply enough that steps can be sequenced toward it.
3. **Given the gap, what are the load-bearing next steps?** Not everything — the essential ones the rest depend on. Specifically interrogate the sequencing tension: does closing the ship-coupling gap (real client/project/order/quote notes, then the data layer) come *before* widening reference depth (more suppliers, the materials class-tier batch)? Or is there a real reason to build reference first?

If he's reaching for the cathedral before the foundation is poured, tell him.

## Phase 4 — Converge (only after you've actually talked)

Once the discussion is genuine, help him converge on a **skeleton**: the essential next steps, sequenced, with the dependency logic explicit (what unblocks what). Keep it a skeleton, not a full plan. Let it emerge — don't front-load it.

> [!note] You are surfacing, not deciding
> Honor the authorship line (`CLAUDE.md` "authorship line"; the audit's "you are surfacing, not deciding"): you sequence options, expose dependencies, and sharpen the choices — but the strategic decisions and the framing stay **Orfeas's** to author. If converging would mean writing his position for him, stop and hand it back.

## Exit — capture the brainstorm log (the one write, like a session)

When the discussion has actually settled (don't rush this — only when Orfeas signals we're done), capture it:

1. **Write the log** to `14_AI_COLLABORATION/Brainstorms/Brainstorm <YYYY-MM-DD>.md` from [[Template - Brainstorm Log]] (add a `b`/`c` suffix if there's already one today, exactly like the session logs). Record: scope, the situation-report snapshot, **the real discussion turns** (what got challenged, what moved), the converged skeleton, and the **proposed promotions** (ADR / Roadmap / Capture Backlog / Open Questions — proposed, not filed). Keep Orfeas's framing in *his* words, not yours.
2. **Commit + push it** like a session: `git add` the new log, `git commit -m "brainstorm: <topic> (<date>)"`, `git push`. (PowerShell here has no `&&` — separate lines; or use the Bash tool.) Record the hash in the log's Commit-ref line.
3. **Do not** update [[Vault State Memory]] or file the promotions yourself — those are Orfeas's to act on at the next build session. The log is the record; promotion is his call.

The dated logs accumulate in `Brainstorms/` and are auto-listed (newest first) in [[Strategic Brainstorm Protocol]] — the brainstorm trail, just like the session trail in [[Collaboration Home]].

**Begin with Phase 0 (one-line scope check), then Phase 1.** When you've finished reading, give the Phase 2 situation report, then ask your first question.
