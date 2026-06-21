---
type: ground-truth-capture
created: 2026-06-19
updated: 2026-06-21
status: draft
confidence: verified
owner: Orfeas Delis
source: interview (the tracer, 2026-06-19)
source_draft: "Downloads/Order Lifecycle — Ground-Truth Capture (Tracer v0.1).md"
related:
  - "[[Order Workflow 0-4]]"
  - "[[Database Master Schema]]"
  - "[[Cost & Quote Build]]"
---

# Order Lifecycle — Ground-Truth Capture

> [!abstract] What this note is
> The vault's **first real operational ground-truth** — how one real order actually moves through Afoi Deli, captured live from Orfeas in the tracer interview (2026-06-19), Skintzi as the spine. It is **not** an SOP and **not** a schema — it's the *input* both feed on. Where this note and [[Order Workflow 0-4]] (the prior prose ideal) disagree, **this note wins** (it's read from reality).
>
> **Status: in progress.** Batches A + B + C + D are interview-settled below. **E–G remain open** (see the open list) — **resume at batch E** (D settled 2026-06-21). The final landing — full S1–S15 merge with Orfeas's Tracer v0.1 draft, the formal schema-diff against the 11 CSVs, repointing the draft's dangling `[[order-fulfillment-workflow-normalized]]` ref to [[Order Workflow 0-4]], and exhibits into `_exhibits/tracer/` — happens once the interview is done.

> [!info] Source draft
> This supersedes/extends Orfeas's reconstruction `Order Lifecycle — Ground-Truth Capture (Tracer v0.1)` (in `Downloads`, drafted 2026-06-19 from the real workbooks + email artifacts). That draft did the **artifact-reading half**; this note adds the **interview half** — the answers only Orfeas holds.

---

## 1. The system landscape (discovered in interview)

Two layers, not one:

- **Operational layer = a constellation of Excel files + email PDFs.** The order sheets (one `.xlsx` per client), **ΚΟΥΒΑΣ** (the cross-order procurement pool — 1 master + 107 supplier subsheets), the **rebate sheet** (`person – project – amount`), and inbound/outbound email artifacts (proformas, ELXIS loading updates). The order **lines live in exactly one place — the Excel.**
- **Accounting layer = MEGASOFT** (external invoicing platform). Holds **only accounting records** — issued invoices, registered bank payments, delivery notes — keyed by **client code**. The OS's `client_invoices` / payments are therefore a **mirror/integration of MEGASOFT, not an independent source of truth**, with a built-in reconciliation point (Excel payment rows vs MEGASOFT registered payments).

---

## 2. Resolved — Batch A (the order sheet, S1)

| # | Settled truth | Model implication |
|---|---|---|
| **A1 · Acceptance** | No single marker — a *cluster* of signals: file → `00.DAILY`, title cell toggles `ΠΡΟΣΦΟΡΑΣ→ΠΑΡΑΓΓΕΛΙΑΣ`, client verbal/email yes, and *sometimes* a downpayment. Ideally a **separate quote file**, but often one sheet that changes state. | "Accepted" is a **derived/soft state**, not a flag. Quote and order stay one logical object; cleanest machine-marker = "entered DAILY / first line being ordered," optionally + downpayment. |
| **A2 · Price** | **list → supplier discount cascade → net cost**, then **+ transport + pallet** (tiles) → landed, then **+ target margin → sell**. When a supplier gives only net prices (no list), cost = net, no derivation. | Confirms the **profitability join (S14)**: cost lives *off-sheet* (price list / proforma), which is exactly why `ΑΡΧΙΚΗ ΤΙΜΗ` is blank. Margin = sell − (net + allocated transport + pallet). Ties to [[Cost & Quote Build]]. |
| **A3 · Payments** | Date = **received**. Default deposit **~40%**, but flexible and **merchant-sized** — to cover the supplier's prepayment demand *and* to stay ahead of partial deliveries (→ intermediate payments). Payment **gates delivery** (full payment before full delivery; sometimes before loading). Good-faith **future-dated agreements** also exist. | Two concepts: **payment_received** (the negative dated rows) vs **payment_agreement** (a promised future date). Cashflow invariant: `paid ≥ delivered/owed`. Release-for-delivery is payment-gated → feeds S11. |
| **A4 · `ΠΑΡΑΤΗΡΗΣΕΙΣ`** | `Π` suffix = **delivery date**. `ΑΝΑΜΟΝΗ` = **sales-hold** (salesperson must finalize something before ordering). Plus free-form notes. | `remarks` = free text **+** extracted events: `delivered_date` (`Π`), `sales_hold` (`ΑΝΑΜΟΝΗ`; owner = sales; **blocks 0→1**). Maps onto the WAIT rule in [[Order Workflow 0-4]]. |
| **A5 · The blue cell** | **Not an order number — it's the client's MEGASOFT code.** Points to the client's sheet there (bank payments, invoices, delivery notes). | Field is `megasoft_client_code`, lives on the **client**, not the order. Corrects the draft's `order_number`. |
| **A6 · `ΟΝΟΜΑ` ≠ client** | `ΕΚΘΕΣΗ ΠΕΡΙΣΤΕΡΙ` = ordered **for us**: showroom/client samples (usually *free* from suppliers) **and stock** (faucets, mechanisms, stock tiles/sanitaryware). | Line needs `destination = client \| showroom_sample \| stock`. An "order" is sometimes **not a client order** (stock procurement, no client) → ORDERS must allow null client. |

---

## 3. Resolved — Batch B (folders & ΚΟΥΒΑΣ)

- **Macro-state (folder) lifecycle — core set:**
  - `00.DAILY` — blocking line at 0, **actionable** (needs ordering now)
  - `01.ΠΡΩΤΟ` — blocking line at 0, **held** (= the order-level face of a line's `ΑΝΑΜΟΝΗ` sales-hold)
  - `02.ΔΕΥΤΕΡΟ` — blocking line at 1 (on order)
  - `03.ΠΡΟΣ ΠΑΡΑΔΟΣΗ` — all received, some ready to deliver
  - **Derivation:** least-advanced blocking line + *why* it's stuck (actionable → DAILY, held → ΠΡΩΤΟ).
  - **Deferred special cases:** `ΤΡΙΤΟ` (delivered-unpaid), `05.ΒΑΛΤΟΣ` (stalled "swamp"). Utility folders (comms, inventory, factory, delivery-schedule) are **not** order macro-states.
- **Channel:** agent is the **default (~90%)**, factory the exception, per-supplier override (captured later in the supplier dossiers' two-channel contact fields).
- **Orders desk:** POs are sent from **`orders@afoideli.gr`** by **2 actors — Dimitris / Vicky** — a distinct role from the salesperson who built the sheet.
- **ΚΟΥΒΑΣ = universal procurement funnel + cross-order pool.** *All* procurement (client / stock / sample) passes through it ("central machine of control"). Stock/showroom still gets an order sheet but may carry **different discounts + credit periods**. A line lives in **two places** while on order (home order sheet + supplier subsheet); removed at status 2. Subsheet tracks **4 dates**: order_sent → proforma_received → proforma_confirmed → **released_for_loading**.

---

## 4. Resolved — Batch C (the proforma, S7)

- **Verification checklist (the crux):** on receipt, before `proforma_confirmed_date`, check **codes · quantities · price-vs-agreed · availability · lead time · payment terms · weight**. The two that actually catch problems: **availability** and **price discrepancy** — the procurement control's real teeth.
- **Wrong proforma = a modeled exception** (price ≠ agreed / qty / wrong code / availability surprise → renegotiate or re-issue). **Relatively rare but high-impact** — a moment of **margin protection** *and* **mandatory client communication** (brand reliability; ties to [[The Heart]]'s never-over-promise). Model it as an exception event (→ `issues_exceptions` + a client-notification trigger), not just a confirmed/not flag.
- **Split decision = judgment** — client readiness to receive + urgency vs the extra cost of split loadings. **Speed usually wins**; the not-ready item is handled independently.
- **Line interdependency (new):** lines aren't always independent. Items can be chosen to **coordinate with a quantity-lead code**; if that lead item is the unavailable one, the coordinated satellites may be **re-selected** → the **whole proforma/order** can be flagged, not just the line. Schema needs a lead-line / coordinated-satellite notion.

> [!warning] `needs_check` — availability code legend unverified
> The `DA/AC/TR/PR/OR` availability-code legend in the Tracer v0.1 draft is **not confirmed** — Orfeas does not recognize it (it was inferred by whatever produced the draft, from the proforma PDF). The *concept* (availability is a top problem) is verified; the **two-letter codes are not**. Verify against the actual `Fattura Proforma 2475340000698.pdf` exhibit; the agent (Filonike) layer may use them.

---

## 5. Resolved — Batch D (loading / arrival, S8–S10)

- **The inbound logistics chain (the physical spine, supplier → us):** **ELXIS** (our freight forwarder) works with an **Italian correspondent forwarder** who collects our materials into a **central consolidation centre** in Italy. From there: **loaded → sea freight → Patras** (the usual port of entry) → **truck to ELXIS's Aspropyrgos warehouse** → **truck to our warehouse, Larnakos 11, 121 35 Peristeri.** Two notification paths, either fires: **(a)** the factory/conduit sends *us* the loading details and we forward them to ELXIS, or **(b)** the conduit notifies ELXIS directly on our behalf.
- **The inbound channel splits by item:** heavy goods (tiles, sanitaryware) ride the **ELXIS sea-consolidation** route above; **taps usually arrive by courier — UPS / DHL — direct.** "Loading" is therefore not one path — light/express items bypass the consolidation chain entirely.
- **Consolidation economics = a core margin lever — flagged for a dedicated deep-dive.** Whether to load a line **alone vs. wait to consolidate** depends on how the forwarder charges us. A small load is punishing: a **~5 m² order** carries **~€120 pallet + transport**, which alone makes a sellable margin impossible. Rule of thumb: **don't load alone below ~5–10 m²**; ideally wait for more orders from the **same factory** to load together. When an order is too small and can't wait, the two levers are **(i) add extra transport cost to the client**, or **(ii) wait longer and notify a later arrival.** Orfeas: *"one of the most basic parts of our profitability."* **Deep-dive parked** for a future session (the quote/margin ↔ transport-allocation mechanics) — it overlaps batch F's transport-allocation question.
- **`09.ΠΡΟΓΡΑΜΜΑ ΠΑΡΑΔΟΣΕΩΝ` = the outbound delivery schedule, not an inbound ETA.** Just an Excel sheet of **client name · delivery day · estimated time-of-day** — last-mile scheduling *to* clients. (Corrects the batch-D assumption that `est_warehouse_arrival_date` lives here; it does not — arrival ETA comes off the loading/lead-time side.)
- **Arrival = the receive event (status 2):** the moment goods **arrive at the warehouse and are checked**, the line is marked **status 2**, **deleted from ΚΟΥΒΑΣ**, and a **sticker with the client's name** goes on top of the client's **"assembled" pallets** (staging/picking by client). The *check* at this step is where batch-E discrepancies (short / over / wrong / broken) surface. Confirms batch B's "removed at status 2."
- **Lead times + the under-promise buffer — precise table parked for a future session.** Lead time is item-driven: **standard chrome tap 15–30 days** (courier); **special-colour / PVD taps 6–8 weeks**; **coloured sanitaryware ~6 weeks prep + ~1 week to us**; **standard tiles (non-special décors, e.g. *not* Kronos Baguette 3D) 15–20 days.** A **missed loading** (missed ship schedule, or truck full / no factory pickup) **rolls to the next loading**, so a **5–7-day buffer** absorbs the bad case. To the client Orfeas quotes a **range** — **good case ~12–15 d / bad case ~15–20 d** for standard tiles — never a single date (the Heart's *never over-promise* / *create the circumstances*). **Deep-dive parked:** a precise per-category lead-time table.

> [!warning] `needs_check` — Mercareon role unconfirmed
> Batch D was scoped as **ELXIS + Mercareon**; Orfeas described ELXIS end-to-end but did **not** mention Mercareon. Its role (delivery-slot booking for big retail destinations? inbound? unused now?) is **open** — confirm at the start of the next batch.

---

## 6. Discoveries (not in the artifact reconstruction)

1. **MEGASOFT** — the second system of record (accounting only; see §1).
2. **The architect/designer rebate** — fires on **full payment** of the order; calc varies case-by-case (% of value / % of margin / per-deal); tracked on a **separate sheet** as `person – project – amount`. Project-keyed → hangs off [[Projects Schema|PROJECTS]]; the architect is a `PERSON` (ERD `PEOPLE` gap).

---

## 7. Running schema-corrections (against the 11 CSVs + existing notes)

1. `clients.megasoft_code` — new field; FK to MEGASOFT. (Corrects draft's order-level `order_number`.)
2. **MEGASOFT** = external AR source of truth → `client_invoices`/payments are a mirror; reconciliation point vs Excel rows. Touches [[Database Master Schema]] ERD `PAYMENTS` gap + [[Invoices and Payments Schema]].
3. `order_line.destination` enum `client | showroom_sample | stock`; samples often €0 (free → `is_sample`); ORDERS must allow null client (stock procurement); stock lines may carry different discount + credit terms.
4. **Margin model (S14):** sell = landed + target margin; landed = net + transport + pallet/packaging; net = list × supplier cascade *or* net-direct. Cost off-sheet → profitability needs the proforma join. Touches [[Cost & Quote Build]] / [[Profitability Engine]].
5. **Payments:** split `payment_received` (negative rows, date=received) vs `payment_agreement` (promised future date). ~40% default deposit, merchant-sized; invariant `paid ≥ delivered/owed`; payment gates release. Touches [[Credit and Due Date Calendar]].
6. **`rebates`** new table `{person, project, amount, calc_method, trigger = order fully paid}`. Project-keyed; person → ERD `PEOPLE`.
7. **`ΠΑΡΑΤΗΡΗΣΕΙΣ` → `remarks`** free text + extracted `delivered_date` (`Π`), `sales_hold` (`ΑΝΑΜΟΝΗ`, blocks 0→1). Maps to WAIT rule in [[Order Workflow 0-4]].
8. **Macro-state model** — derive folder from least-advanced blocking line + reason (DAILY/ΠΡΩΤΟ/ΔΕΥΤΕΡΟ/ΠΡΟΣ ΠΑΡΑΔΟΣΗ); ΤΡΙΤΟ/ΒΑΛΤΟΣ deferred as special states.
9. **ΚΟΥΒΑΣ** — model as the universal procurement funnel (4 dates; two-place membership; removed at status 2); supplier two-channel contact `{agent (primary), factory (exception)}`.
10. **Actors/roles** — orders desk (`orders@afoideli.gr`; Dimitris, Vicky) owns PO-send. New people for [[People and Roles Map]].
11. **Proforma verification** — checklist confirmed (codes · qty · price-vs-agreed · availability · lead time · terms · weight); top catch-points = **availability + price**.
12. **Proforma discrepancy = exception** (rare, high-impact) → margin-protection (renegotiate) + **mandatory client communication**. Links `issues_exceptions` + client-notification. Doctrine: client comms is a must ([[The Heart]] — never over-promise).
13. **Split decision** = judgment (client readiness + urgency vs split-loading cost); speed usually wins.
14. **Line interdependency** — lead/quantity-major code + coordinated satellites; lead unavailability can cascade to re-selection → whole-proforma flag. New concept the line model needs.
15. **Availability code legend (`DA/AC/TR/PR/OR`) — `needs_check`/unverified** (from the draft, not recognized by Orfeas). Verify against the proforma exhibit.
16. **Inbound logistics = its own entity.** A `loading` / `shipment` distinct from the order: carrier **ELXIS** + an Italian correspondent forwarder + a consolidation centre; route Italy → sea (**Patras**) → ELXIS **Aspropyrgos** → our **Peristeri** warehouse; two notification paths (we-forward vs. conduit-notifies-ELXIS). **Many lines per loading** (the join that makes consolidation possible). New to the model.
17. **Transport/consolidation = a margin input, not a flat add-on.** Load-alone threshold **~5–10 m²**; small-load penalty (~€120 on ~5 m²); resolve by **charging the client extra transport** *or* **waiting to consolidate** (later ETA). Transport allocates **per-loading across the pooled lines** → feeds the **S14 margin model** / [[Cost & Quote Build]] / [[Profitability Engine]]. **Future deep-dive** (overlaps batch F).
18. **`09.ΠΡΟΓΡΑΜΜΑ ΠΑΡΑΔΟΣΕΩΝ` = the outbound client delivery schedule** (`client · delivery_day · est_time_of_day`) — a last-mile utility, **not** the inbound warehouse-arrival ETA. Corrects the batch-D assumption.
19. **Receive event** — **arrival + check** → line **status 2**, **ΚΟΥΒΑΣ removal**, **client-name sticker on the assembled/staged pallet**. Defines `received_date` + a **staging/assembly** step; the check is the batch-E discrepancy gate.
20. **Lead-time taxonomy** (chrome tap **15–30 d** courier · special/PVD tap **6–8 wk** · coloured sanitaryware **~6 wk + 1** · standard tiles **15–20 d**) + **missed-loading roll-forward** (~5–7 d buffer). Client is quoted a **good/bad range**, never a single date → feeds `est_arrival` + the **under-promise buffer** ([[The Heart]]). **Future deep-dive: a precise per-category table.**
21. **Inbound channel splits by item** — **courier (UPS/DHL)** for taps vs. **ELXIS sea-consolidation** for tiles/sanitaryware; channel drives both lead time *and* transport cost. The line/supplier model likely needs an **inbound-channel** attribute.

---

## 8. Open — remaining interview batches

- [x] **A · Order sheet** — settled 2026-06-19 (§2).
- [x] **B · Folders & ΚΟΥΒΑΣ** — settled 2026-06-19 (§3).
- [x] **C · Proforma** — settled 2026-06-19 (§4).
- [x] **D · Loading / arrival** — settled 2026-06-21 (§5). **Two deep-dives parked for future sessions:** (1) transport/consolidation economics ↔ margin (overlaps F); (2) a precise per-category lead-time table. **Open thread:** Mercareon role (`needs_check`, §5 warning).
- [ ] **E · Receipt / delivery** `← NEXT (resume here)` — discrepancy handling (short/over/wrong/broken) · delivery vs pickup · partial delivery.
- [ ] **F · Payment / invoice / margin** — payment terms + gating detail · missing-invoice payable · where payable is tracked · transport allocation (the margin math: markup vs margin, transport before/after) · the rebate calc · is margin reviewed today.
- [ ] **G · Special cases** — returns · breakages · backorder sub-state.

---
*Spine order: Skintzi (`ΣΚΙΝΤΖΗ ΕΛΠΙΔΑ.xlsx`). Buy-side numbers stay confidential (CLAUDE §4).*
