---
type: finance_method
created: 2026-06-17
status: seed
confidence: verified
automation_priority: high
aliases:
  - Cost & Quote Build
  - Cost to Quote
  - Pricing Build
---

# Cost & Quote Build

> [!danger] Confidential — buy-side / never client- or public-facing
> This note documents how we get from a manufacturer's **list price** to our **net cost** and on to a **quote**. The net/discount layer is our cost structure — keep it out of every client- and public-facing surface (quotes show **sell** prices only). See `CLAUDE.md §4`.

> [!info] Status — seed (the chain is real; the calculator is the deferred build)
> Orfeas flagged the pricing policy as a **down-the-road** discussion (2026-06-17). This note captures the **mechanical chain** so it's ready; the **margin policy** (target bands, per-tier markups, project rules) is Orfeas's to author, and the actual calculator is a future build on the OS `products` tier. Today it holds the framework + the first worked supplier (Kronos).

## The chain

The price of a quoted line is built in five steps. Steps 1–2 are deterministic (we know the inputs); steps 3–5 are where judgement and policy enter.

| # | Step | From → To | Driver |
|---|---|---|---|
| 1 | **List** | manufacturer listino → €/m² (or €/pz) | the supplier price list (archived per supplier) |
| 2 | **Net** | list → **net buy cost** | the supplier's **discount cascade**, per item tier |
| 3 | **Landed** | net → **landed cost** | + pallet/packaging, transport, quantity effects |
| 4 | **Quote / sell** | landed → sell price | + **margin** *(policy — Orfeas)* |
| 5 | **Profitability** | sell − landed | gross margin €/% → [[Profitability Engine]] |

**Net (step 2)** = `list × Π(1 − dₖ)` over the cascade discounts `dₖ` for that item's tier. Discounts **compound** (each applies to the remainder).

**Landed (step 3)** = `net × m²` + allocated **pallet/packaging** + **transport** (per shipment, allocated by weight or m²) + any **quantity** adjustment (full-pallet vs. part, MOQ). The box/pallet/kg columns needed for this allocation are in each supplier's listino.

## Worked supplier — Kronos (first one wired)

> [!note] Figures redacted to their canonical home (OV-08 · baseline §17 decision 6, 2026-07-19)
> This note is **reference-only** for buy-side numbers: the per-tier discount cascade (and its net multipliers), the worked Pierre Vive net examples, and the credit terms live **only** in [[Supplier - Kronos]] §Pricing (danger-classified). What stays here is the method.

The Kronos shape, without figures: items are assigned a **tier** (base tiles · module configs · decors) by a rule consistent across all Kronos collections; each tier has its own **compounding cascade** (§The chain, step 2) off the *Listino Prezzi 2026* (archived in `Kronos/_sources/`); list prices per line live in the collection notes (e.g. [[Collection - Kronos Pierre Vive]]).

**Credit** (affects cash, not margin directly): terms in the dossier §Pricing → wiring in [[Credit and Due Date Calendar]].

## What's decided vs. open

- **Decided:** the 5-step chain; Kronos's cascade + tiers + credit (verified — figures in the dossier §Pricing). Real per-SKU prices stay at the OS `products` tier (`buy_price` = list × cascade), not copied into notes — see [[Database Master Schema]]. Collections carry a derived `price_band`, not live prices (the [[Capture Backlog]] "cost as a collection facet" decision, option 1). **This note is reference-only for figures** (baseline §17 decision 6).

> [!question] Open — Orfeas to author (the policy half)
> - **Margin policy** — target gross-margin band(s); do they differ by tier (base vs. decor) or by channel (retail vs. project/architect)?
> - **Transport & pallet allocation** — by weight, by m², or a flat per-order load fee? (Kronos sells only in full boxes; part-pallet handling.)
> - **Quantity rules** — when does a project size unlock the small negotiated extra-discount ceiling (figure in the dossier §Pricing), and does that pass to the client or hold as margin?
> - **The negotiation ceiling** vs. the standard cascade — keep separate in the model (cascade = cost basis; the ceiling = deal-by-deal).

## Links
- Margin tracking → [[Profitability Engine]] · credit/cash → [[Credit and Due Date Calendar]]
- First supplier → [[Supplier - Kronos]] · data tier → [[Database Master Schema]]
- Root → [[The Heart]] (*"never forget we are merchants — buy goods and sell them, carry the risk in between"*)
