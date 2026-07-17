---
type: ground-truth-capture
created: 2026-06-19
updated: 2026-07-18
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
> **Status: interview complete (A–G).** All seven batches are interview-settled below (G settled 2026-07-18); the running schema-corrections list stands at **49**. **What remains is the final landing** — the full S1–S15 merge with Orfeas's Tracer v0.1 draft, the formal schema-diff turning those 49 corrections into concrete `.md` / CSV edits against the 11 CSVs, repointing the draft's dangling `[[order-fulfillment-workflow-normalized]]` ref to [[Order Workflow 0-4]], and exhibits into `_exhibits/tracer/`.

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

---

## 6. Resolved — Batch E (receipt / delivery, S10–S12)

- **The receipt check is a verification *chain*, and it rarely fails.** Warehouse staff **count the boxes** and **match the pallet stickers against the delivery note**, then cross-check **box codes ↔ proforma ↔ delivery note**, having already confirmed the **order-sheet code itself is right against the supplier's catalogue / price list**. Discrepancies are **rare** — pallets arrive **factory-pre-built, wrapped and closed** (automated), so a *single* missing box is unlikely; a **whole missing pallet** is the likelier failure. Fault is **located along the chain before it is assigned.**

- **Liability routes by failure type:**
  - **Broken in transit** → a **note to the transport company to credit us**, **notify the client**, **re-order if needed**. The **carrier** carries it.
  - **Wrong item** → back to the **supplier** — but only *after* confirming the transporter **picked up the right material from the logistics centre** (rule the forwarder out first).
  - **Short but not broken** → almost always **our own proforma-confirmation error** (the proforma listed fewer boxes than the order and we confirmed it) — it traces **upstream to batch C's quantity check-point**, not to a logistics loss. Usually **let be** (rare).

- **The "separation" mechanic — order lines are not atomic.** On a partial problem the line's quantity **splits**: the **good boxes settle at status 2** (received, ΚΟΥΒΑΣ-removed) while the **missing/broken quantity is deducted, re-ordered as status 1, and re-entered into ΚΟΥΒΑΣ**. A discrepancy therefore **forks a line into a received part + a child back-order.**

- **The transport credit-owed is an uncaptured receivable.** A **post-it** holds the amount owed back by the transporter — and that post-it is the **only** record; it is **not reconciled into any system** (not MEGASOFT, no claims list). Money *we're owed*, tracked on paper until the carrier issues the credit note. **SOP≠reality: there is no system here at all** — a prime OS-systematization target (protect-the-craft: mechanical money-tracking, not the selling craft).

- **Delivery vs pickup = a judgment on volume × urgency × relationship.**
  - **Client pickup** from Peristeri when **time is crucial and we can't schedule delivery immediately and the volume permits**, or when **volume is too low to justify a whole truck** (we suggest it).
  - We **combine** a delivery with another in the **same general area** — a **service** so as not to bother the client (and an efficiency lever).
  - We **deliver regardless** when it's **time-pressuring, the client is important, and/or we made a prior mistake** — delivery-as-service / reputation repair ([[The Heart]]: *create the circumstances*, earned standing).
  - Governing rule: **"obey client needs — but only if it doesn't harm the business."**

- **A delivery is marked in two places:** registered in **`09.ΠΡΟΓΡΑΜΜΑ ΠΑΡΑΔΟΣΕΩΝ`** (client · delivery day · est. time-of-day) **and** the **order-sheet cell is marked (blue marker) with the exact materials to deliver** — i.e. a delivery selects a **subset of the order's lines.**

- **Partial delivery is first-class and common** — driven by the **project life-cycle** and **client need** (e.g. **technicians scheduled on site → deliver what unblocks the trade**; it also acts as a **buffer** against the rest still arriving). **Honesty first:** deliver what's ready and be straight about the rest; otherwise **wait and deliver together.** So a delivery references **a subset of lines** (many deliveries per order), and the `03.ΠΡΟΣ ΠΑΡΑΔΟΣΗ` macro-state ("all received, some ready to deliver") is exactly this partial-ready condition.

> [!note] Carried to batch F (money-adjacent)
> Whether the **delivery note (Δελτίο Αποστολής)** issues from **MEGASOFT** at the delivery moment, and how a **partial delivery** interacts with **partial invoicing** and the **payment gate** (full payment before full delivery — §2 A3), fold into **batch F**.

---

## 7. Resolved — Batch F (payment / invoice / margin, S13–S15)

### Money-in (client side)
- **The payment gate is soft and relationship-mediated — the hard rule is the cashflow invariant `paid ≥ delivered`.** Ideal is pay-before-release, but it bends constantly: payment **pre-arranged**, **paid after the invoice is emailed**, a client **credit line** (no payment expected at delivery), or the **partial drop already covered by the deposit** (don't ask for more). It is *tact*. Underneath, the line that never bends: **never deliver ahead of cash — the ~40% deposit is a running buffer keeping cumulative paid ≥ cumulative delivered** ("a deposit against the goods not delivered"). **Confirmed by Orfeas as *the* invariant.**
- **Delivery documents split by client type, both from MEGASOFT:** **individuals → a combined `ΔΑ-ΤΙΜΟΛΟΓΙΟ`** (delivery-note-invoice fused, at delivery); **companies → a `ΔΕΛΤΙΟ ΑΠΟΣΤΟΛΗΣ` (ΔΑ) at delivery, later coupled/converted to a `ΤΙΜΟΛΟΓΙΟ`.** The **ΔΑ is mandatory for goods to move**; the **τιμολόγιο lags** (same day → a few days). AR therefore trails the physical delivery: **ΔΑ → τιμολόγιο → payment.**

### Money-out (supplier payable)
- **Supplier AP lives in Kostas's Excel — *not* MEGASOFT.** The ledger's two sides run on different systems of record: **client AR mirrors MEGASOFT; supplier AP mirrors Kostas's personal Excel.** Cadence: every **~15 days**, invoices gathered from the delivery receipts go to **Kostas**, who **schedules payments in the Excel by each invoice's terms** — and **bends the periods to cashflow** (the merchant's nerve, [[The Heart]]; **parked deep-dive**).
- **Supplier documents mirror the client side:** the **transport document (DDT)** arrives with the goods → **checked, stored, matched to a later invoice**; **one invoice can consolidate several delivery notes** (1 invoice : N DDTs). The invoice may arrive **printed, emailed, or not at all.**
- **The payable clock:** **due-date = invoice date + terms**, and the **invoice is issued the moment goods leave the supplier (ex-works)** — independent of when our forwarder picks up. (So Kronos's 90 d runs from the supplier's invoice, not from loading or our receipt.)
- **Missing-invoice control = the unpaired delivery receipt.** The DDT is the anchor; every invoice should pair to ≥1 DDT → a **DDT with no matching invoice = a missing invoice**, chased from the **Greek agent or the supplier directly.**

### The margin close
- **Pricing is intuition, not a formula.** No fixed markup/margin — flexed by **willingness to take the job · effort spent winning it · how favourable the materials are to sell · negotiation headroom · the month's break-even-vs-payables position.** Working band **~40–60% markup**, bent to need. *"Things get easier once you've cleared break-even against payables"* — margin held harder early-month, bent more freely once payables are covered.
- **Transport is folded *into* the cost and marked up** — not a transparent pass-through; margin is earned on the freight too. Markup base = transport-inclusive landed cost (`net + transport + pallet`).
- **Realized per-order margin is NOT computed today (audit F7 — verified from the inside).** Priced by feel at quote time; **no post-close reconciliation** of actual sell − actual landed (real transport + rebate). → The single highest-value analytical output the OS can add: **true realized margin per order** — *inform* the intuition that sets the price, **don't** automate it (protect-the-craft; [[The Selection Engine]] / [[Profitability Engine]]).

### The rebate (architect / designer / referrer)
- Fires on **full payment**; **calc is genuinely case-by-case** across **% of order value · % of margin · flat per-deal**.
- **Placement varies by the architect↔end-client relationship:** sometimes **encapsulated inside our margin** (a cost to us — reduces realized margin), sometimes **on top of the arranged margin** (the client bears it, our margin intact). *This placement is a required input to the realized-margin computation.*
- **Recipient = anyone who steered the client** (architect, designer, referrer). **Settlement = cash · a services invoice · credit against a next job · or netted against the recipient's own orders** (their home/office). The **services-invoice route is preferred** — its VAT is **deducted from Afoi Deli's monthly VAT liability** (Greek law, input-VAT offset). "Netted against their own orders" ⇒ **a person can be both a rebate-payee and a client.**

> [!note] Parked deep-dives (fold into future sessions)
> (1) **Kostas's period-bending** — how AP payment timing is flexed to cashflow (the treasury art; a Kostas people-note seed). (2) A **precise per-category lead-time table** (from batch D). (3) The **monthly break-even-vs-payables signal** as an OS pricing aid. Transport↔margin economics is now largely captured (folded-in + marked-up + F7); the remaining piece is the per-loading allocation math, which folds into (1)/(3).

---

## 8. Resolved — Batch G (special cases)

### Returns & breakages
- **Client returns are conditional, not a right.** **Over-ordered imported-to-order goods → not taken back** (barring relationship exceptions). **Stock items → taken back only if packaging is intact.** **Defects → accepted only after *dual* verification (us + supplier); the supplier then credits us.**
- **The stock / inventory ledger (Excel) — new to the model — tags stock by origin:** **`frequent`** (deliberate stock buys) · **`excess`** · **`returns/defects`** · **`cancellations/mistakes` = "ΣΚΟΥΠΑ"** (the "broom" — the sweepings). This is the inventory layer the 11 CSVs lacked; it's where returns and `destination = stock` lines (corr. 3) land.
- **Suppliers are mostly inelastic on returns.** The Kronos "≤80% return / 20% ready-order cancellation" listino terms are **formal policy, not operating reality** — returns are **not pushed back up the chain**; they're **handled directly with the client** (→ stock / credit / accommodation). Afoi Deli absorbs most returns.
- **Post-transit breakage is a grey area Afoi Deli usually absorbs.** Mitigation: **dispatch photos** (goods photographed leaving the warehouse — best-effort proof of intact dispatch). Late-surfacing breakage (days–weeks on, no probable proof) is **unattributable → we ingest it and replace/credit the client** (reputation-first, [[The Heart]]). Distinct from *transit* breakage (batch E → carrier credit).

### The stalled / unfulfilled states
- **ΤΡΙΤΟ (delivered-unpaid) = the AR-risk state where `paid ≥ delivered` is broken** — composed of **certain-to-pay · payment agreements · our mistakes** (delivered without securing payment), **monitored closely and continuously.** Governance ideal: **only deliberate *agreements* belong in ΤΡΙΤΟ**; a mistake landing here is a process failure. (Ties to the invariant, corr. 28.)
- **ΒΑΛΤΟΣ (05, "the swamp") = aged ΤΡΙΤΟ** — "time has passed ΤΡΙΤΟ" — a **staleness bucket** for long-overdue delivered-unpaid, and **largely irrelevant nowadays.** Model it as an **age/stale flag on ΤΡΙΤΟ**, not a separate workflow.
- **Backorder is handled by avoidance-then-substitution, rarely refund.** **Discontinuations are tracked and pulled from the showroom + catalogues.** Production-unavailability → **notify the client early** → **substitute** (another dimension / colour / material) or **cancel / dismiss** (refund if already paid). **Early availability pre-check + notification is the main defence** (ties batch C's availability catch-point + the coordinated-satellite re-selection). Refund is the fallback, not the default.

> [!success] The interview is complete — A through G captured.
> What remains is the **final landing**: the full **S1–S15 merge** with the Tracer v0.1 draft, the formal **schema-diff** turning the **49** running corrections into concrete `.md` / CSV edits, repointing the draft's dangling `[[order-fulfillment-workflow-normalized]]` ref to [[Order Workflow 0-4]], and filing exhibits into `_exhibits/tracer/`.

---

## 9. Discoveries (not in the artifact reconstruction)

1. **MEGASOFT** — the second system of record (accounting only; see §1).
2. **The architect/designer rebate** — fires on **full payment** of the order; calc varies case-by-case (% of value / % of margin / per-deal); tracked on a **separate sheet** as `person – project – amount`. Project-keyed → hangs off [[Projects Schema|PROJECTS]]; the architect is a `PERSON` (ERD `PEOPLE` gap). *(Batch F: placement `inside_margin | on_top`; settlement incl. a preferred VAT-offsetting services invoice.)*
3. **Supplier AP = Kostas's personal Excel** — a **second, human system of record** wholly separate from MEGASOFT (which is client-AR / accounting only). A **~15-day cycle**: invoices gathered from delivery receipts → Kostas → he schedules payments by terms, **bending the periods to cashflow** by intuition. The merchant's nerve ([[The Heart]]) sitting in the treasury. *(Batch F — parked deep-dive.)*
4. **The stock / inventory ledger + the "ΣΚΟΥΠΑ" taxonomy** — a stocked-items Excel tagging stock by **origin** (`frequent | excess | returns/defects | cancellations-mistakes = ΣΚΟΥΠΑ`). The **inventory layer the 11 CSVs never modeled**; the landing place for returns and stock-destination lines. *(Batch G.)*

---

## 10. Running schema-corrections (against the 11 CSVs + existing notes)

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
22. **Line quantity is splittable (the "separation" mechanic).** A receipt discrepancy **forks a line**: received qty → **status 2**; missing/broken qty → **deducted, re-ordered as status 1, re-entered in ΚΟΥΒΑΣ**. Order lines are **not atomic in quantity** — a partial problem spawns a **child back-order line**. Extends the line/status model (corrections 3 / 8 / 9).
23. **Carrier / transport credit-due = an uncaptured receivable.** Broken-in-transit → we issue a note to the transport company for a **credit to us**, tracked **only as a physical post-it** (no system, no reconciliation). A financial claim **we're owed**, distinct from client AR and supplier AP → new object `transport_claim {loading, amount, status}`. Prime OS-systematization target. Links `issues_exceptions` (corr. 12) + inbound-logistics entity (corr. 16).
24. **Receipt discrepancy diagnosis = fault-location *before* fault-assignment.** Verification chain: box count · pallet stickers ↔ delivery note · box codes ↔ proforma ↔ delivery note · order-sheet code ↔ supplier catalogue/price list. Liability by type: **broken → carrier**; **wrong → supplier** (after ruling out the forwarder picked up the right material); **short-not-broken → almost always an internal proforma-confirmation error** (confirmed a proforma with fewer boxes than the order). Pallets are **factory-pre-built / wrapped** → a *whole missing pallet* is likelier than a single missing box. Reinforces batch C's quantity check-point.
25. **Delivery vs pickup = a judgment (volume × urgency × relationship).** Pickup when time is crucial + volume permits, or volume too low to justify a truck; deliveries **combined by geographic area** as a service; **always deliver when time-pressuring / important client / we made a prior mistake** (delivery-as-remedy — [[The Heart]], earned standing). Governing rule: **"obey client needs, but only if it doesn't harm the business."** New: a `delivery` event with `mode {pickup | own-delivery | combined-route}`.
26. **A delivery references a *subset* of an order's lines** — recorded twice: in **`09.ΠΡΟΓΡΑΜΜΑ ΠΑΡΑΔΟΣΕΩΝ`** (client · day · est. time) **and** an order-sheet **blue-marker** flag on the exact materials to deliver. Confirms corr. 18 (09 = outbound schedule) and makes **partial delivery first-class** (many deliveries per order).
27. **Partial delivery is first-class and common** — driven by project life-cycle / client need (technicians on site → deliver what unblocks the trade; also a buffer). Doctrine: **honesty first** — deliver what's ready, be straight about the rest; else wait and deliver together. Feeds the `03.ΠΡΟΣ ΠΑΡΑΔΟΣΗ` macro-state. *(Answered in F: each physical move needs its own ΔΑ; invoices consolidate — corr. 29/33.)*
28. **The payment gate is soft and relationship-mediated, not a hard pay-on-delivery.** Release is governed by pre-arrangement, **client credit lines** (no payment expected at delivery), deposit-coverage of the partial drop, and **tact** — often paid **after the invoice is emailed**. The hard rule underneath is the **cashflow invariant: never deliver ahead of cash — the ~40% deposit is a running buffer keeping cumulative `paid ≥ delivered`** ("a deposit against the goods not delivered"). **Orfeas-confirmed.** Refines corr. 5 / §2 A3.
29. **`clients.type {individual | company}` drives the delivery-document flow.** **Individuals → a combined `ΔΑ-ΤΙΜΟΛΟΓΙΟ`** (fused, at delivery). **Companies → a `ΔΕΛΤΙΟ ΑΠΟΣΤΟΛΗΣ` (ΔΑ) at delivery, later coupled/converted to a `ΤΙΜΟΛΟΓΙΟ`.** All from **MEGASOFT**. New `documents` model: types `{delivery_note, invoice, delivery_invoice}` + a customer-type issuance rule.
30. **The ΔΑ is mandatory before goods move; the τιμολόγιο can lag T+0…T+few days.** So the AR/invoice record (MEGASOFT) is **decoupled from the physical delivery** → reconciliation triple **ΔΑ issued (goods moved) → τιμολόγιο issued (AR booked) → payment received.** Touches [[Invoices and Payments Schema]] / the MEGASOFT-mirror (corr. 2).
31. **Client credit line** — some (company) clients carry a **credit line**, so **no payment is expected at delivery** (AR runs on terms, not cash-against-goods). New `clients.credit_line {limit, terms}`; feeds [[Credit and Due Date Calendar]]; interacts with the soft gate (corr. 28).
32. **Supplier AP lives in Kostas's Excel — NOT MEGASOFT.** The ledger's two sides have **different systems of record: client AR = MEGASOFT-mirror (corr. 2); supplier AP = Kostas's personal Excel.** Cadence: every **~15 days** invoices gathered from delivery receipts go to **Kostas**, who **schedules payments in the Excel by each invoice's terms** (and **bends the periods to cashflow** — an intuition art, **parked**). So `supplier_invoices.csv` mirrors **Kostas's Excel**, not MEGASOFT. New actor: **Kostas owns AP scheduling** → [[People and Roles Map]] / [[The Heart]]. Touches [[Database Master Schema]] / [[Invoices and Payments Schema]] / [[Credit and Due Date Calendar]].
33. **Supplier document flow mirrors the client side: DDT (transport doc) → later invoice.** On receipt we **check goods, store the transport document, and match it to a later-issued invoice**; **one invoice can consolidate several delivery notes** (1 : N). The invoice may come **printed, emailed, or not at all.** Reconciliation unit = the DDT.
34. **AP due-date = invoice_date + terms; invoice_date = ex-works (goods leave the supplier), independent of our forwarder's pickup.** The payment-term clock (e.g. Kronos 90 d) runs from the **supplier's invoice/ex-works moment**, not loading or our receipt. Corrects any loading-date assumption. Feeds [[Credit and Due Date Calendar]].
35. **Missing-invoice control = the unpaired delivery receipt.** The DDT is the AP anchor; every invoice pairs to ≥1 DDT. A **DDT with no matching invoice = a missing invoice** → chase the **Greek agent** or the **supplier directly.** AP-side analog of the AR reconciliation point (corr. 2).
36. **Pricing = intuition within a ~40–60% markup band — not a formula.** No fixed markup/margin %; the number flexes by **willingness to take the job · effort/time to win it · how favourable the materials are to sell · negotiation headroom · the month's break-even-vs-payables position** ("things get easier once you've cleared break-even vs payables"). → The OS must **inform** the pricing judgment (surface cost, landed, comparable margins, break-even state), **not replace** it — pricing is selling-craft (protect-the-craft; [[The Selection Engine]] / [[The Heart]]). Refines [[Cost & Quote Build]] ("margin policy left to Orfeas").
37. **Transport is folded *into* the cost, then marked up — not a transparent pass-through.** The client is marked up on transport too (a margin lever, not just a recovery). Markup base = **transport-inclusive landed cost** (`net + transport + pallet`), confirming the batch-A/D chain. (The batch-D small-load case — sometimes charged as an explicit extra — is the deviation, not the default.)
38. **Realized per-order margin is NOT computed today (audit F7 — verified).** Pricing is by feel at quote time; **no post-close reconciliation** of actual sell − actual landed (real transport + rebate). *The* profitability gap the tracer exists to prove — and the **single highest-value analytical output the OS can add**: true per-order margin, which the business currently flies without. Headline for [[Profitability Engine]] / the OS vision.
39. **Monthly break-even-vs-payables modulates pricing aggressiveness.** Before the month's break-even (covering payables — Kostas's Excel) is cleared, margin is held harder; after, pricing bends more freely to close. A **monthly break-even signal** (payables-due vs margin-booked) is a candidate OS surface that would directly inform corr. 36. Links cluster-2 AP (corr. 32) ↔ pricing.
40. **Rebate calc is genuinely case-by-case across all three bases** — % of order value · % of margin · flat per-deal (confirms discovery 2 / corr. 6). Store as `{amount, calc_method ∈ (pct_value|pct_margin|flat), basis}`; no normalization.
41. **Rebate placement = `{inside_margin | on_top}`, set by the architect↔end-client relationship.** *Inside* → reduces our realized margin (a cost to us); *on top* → added over our arranged margin (the client bears it). **A required input to the realized-margin computation (corr. 38)** — the rebate is only our cost when it's inside. New attribute on the rebate.
42. **Rebate settlement = `{cash | services_invoice | credit_next_job | netted_vs_their_own_orders}`; the services-invoice route is preferred** because the recipient's **services-invoice VAT is deducted from Afoi Deli's monthly VAT liability** (Greek law — input-VAT offset). "Netted vs their own orders" ⇒ **a PERSON can be both a rebate-payee and a client** (their home/office) → entity overlap in [[People and Roles Map]] / the PEOPLE↔CLIENTS model; adds a VAT/accounting tie to the MEGASOFT layer.
43. **Client-return acceptance is conditional, not a right.** **Over-ordered *imported-to-order* goods → not taken back** (save relationship exceptions); **stock items → taken back only if packaging is intact**; **defects → accepted only after *dual* verification (us + supplier), then the supplier credits us.** New `returns` flow: acceptance rule = `(is_stock_item AND packaging_intact) OR (defect AND dual_verified)`; verified defects carry a supplier-credit path.
44. **A stock / inventory ledger (Excel) exists, tagged by provenance.** Returned/leftover goods become **stock** in a stocked-items Excel, origin-tagged: **`frequent` (deliberate buys) · `excess` · `returns/defects` · `cancellations/mistakes` = "ΣΚΟΥΠΑ"** (the broom). New entity **`stock_items {sku, qty, origin ∈ (frequent|excess|returns_defects|skoupa)}`** — the inventory layer the 11 CSVs lack; links the `destination = stock` line type (corr. 3).
45. **Suppliers are mostly inelastic on returns — Kronos's "≤80% / 20% cancellation" listino terms are formal policy, not operating reality.** Returns are **not pushed back up the chain**; they're **handled directly with the client** (→ stock / credit / accommodation). Contextualizes [[Supplier - Kronos]] commercial terms; Afoi Deli absorbs most returns.
46. **Post-transit breakage is a grey area Afoi Deli usually absorbs.** Mitigation: **dispatch photos** (goods photographed leaving the warehouse — best-effort intact-dispatch proof). Late-surfacing, unprovable breakage → **unattributable → ingest + replace/credit the client** (reputation-first, [[The Heart]]). New: a `dispatch_photo` evidence step + an `unattributable_loss` outcome on `issues_exceptions` (corr. 12); distinct from *transit* breakage (batch E → carrier).
47. **`ΤΡΙΤΟ` (delivered-unpaid) = the AR-risk sub-state where `paid ≥ delivered` is broken.** Composition: **certain-to-pay · payment agreements · our mistakes**; **monitored continuously**; governance ideal = **only deliberate agreements belong there** (a mistake here is a process failure). Promotes the batch-B deferred special state; ties to corr. 28 + [[Credit and Due Date Calendar]].
48. **`ΒΑΛΤΟΣ` (05, "the swamp") = aged `ΤΡΙΤΟ`** ("time has passed ΤΡΙΤΟ") — a **staleness bucket** for long-overdue delivered-unpaid, **largely irrelevant nowadays.** Model as an **age/stale flag on ΤΡΙΤΟ**, not a separate state. Resolves the batch-B ΤΡΙΤΟ/ΒΑΛΤΟΣ deferral.
49. **Backorder = avoidance-then-substitution, rarely refund.** Discontinuations **tracked + pulled from showroom/catalogues** (catalogue hygiene); production-unavailability → **notify early** → **substitute (dimension/colour/material)** or **cancel/dismiss** (refund if pre-paid). **Early availability pre-check + notification is the main defence** (ties batch C's availability catch-point + the coordinated-satellite re-selection). New: a `discontinuation`/`availability` process + a `substitution` line-outcome; refund is fallback, not default.

---

## 11. Interview batches — all settled

- [x] **A · Order sheet** — settled 2026-06-19 (§2).
- [x] **B · Folders & ΚΟΥΒΑΣ** — settled 2026-06-19 (§3).
- [x] **C · Proforma** — settled 2026-06-19 (§4).
- [x] **D · Loading / arrival** — settled 2026-06-21 (§5). **Two deep-dives parked for future sessions:** (1) transport/consolidation economics ↔ margin (overlaps F); (2) a precise per-category lead-time table.
- [x] **E · Receipt / delivery** — settled 2026-07-18 (§6). The receipt **verification chain** + rarity (factory-prebuilt/wrapped pallets); **liability routing** (broken→carrier · wrong→supplier · short→our proforma-confirm error); the **line-split / "separation"** mechanic; the **uncaptured transport-credit post-it**; **delivery vs pickup** judgment (volume × urgency × relationship, combined routes, deliver-on-our-mistake); the **blue-marker + `09.ΠΡΟΓΡΑΜΜΑ ΠΑΡΑΔΟΣΕΩΝ`** delivery marking; **partial delivery** as first-class.
- [x] **F · Payment / invoice / margin** — settled 2026-07-18 (§7). **Money-in:** the soft, tact-mediated payment gate over the hard `paid ≥ delivered` invariant; documents split by client type (**individual → ΔΑ-ΤΙΜΟΛΟΓΙΟ · company → ΔΑ then coupled ΤΙΜΟΛΟΓΙΟ**, ΔΑ mandatory for movement, invoice lags), client credit lines. **Money-out:** **supplier AP lives in Kostas's Excel** (not MEGASOFT), a ~15-day scheduling cycle; DDT→invoice pairing (1:N); **ex-works invoice-date drives the due-date**; unpaired-DDT = missing-invoice control. **Margin:** **pricing is intuition (~40–60% markup band)**, transport folded-in-and-marked-up, **realized margin uncomputed today (F7 verified)**, monthly break-even-vs-payables modulates it. **Rebate:** case-by-case (%value/%margin/flat), placement `inside_margin | on_top`, settlement `cash | services_invoice | credit | netted`, services-invoice preferred (VAT offset). **Parked deep-dives** (§7 note): Kostas's period-bending · per-category lead-time table · the break-even signal.
- [x] **G · Special cases** — settled 2026-07-18 (§8). **Returns** conditional (imported-to-order not taken back · stock only if intact · defects dual-verified → supplier credit); the **`ΣΚΟΥΠΑ` stock ledger** + origin taxonomy; **suppliers inelastic on returns** (Kronos terms are formal, not real); **post-transit breakage absorbed** (dispatch photos, else eat + replace/credit). **States:** `ΤΡΙΤΟ` = delivered-unpaid AR-risk (only agreements *should* live there); `ΒΑΛΤΟΣ` = aged ΤΡΙΤΟ (largely dead); **backorder = avoidance-then-substitution**, refund is fallback.

> [!success] Interview complete — next is the final landing
> All seven batches (A–G) are settled. The remaining work is **not** more interview — it's the **final landing**: (1) merge with the Tracer v0.1 draft into the full **S1–S15** narrative; (2) the **schema-diff** — turn the **49** corrections into concrete `.md` / CSV edits against the 11 CSVs (headline gaps: the **inventory/`stock_items`** entity, **`transport_claim`**, the **documents** model, **Kostas-Excel AP** as its own source, the **realized-margin** join); (3) repoint the draft's dangling `[[order-fulfillment-workflow-normalized]]` ref to [[Order Workflow 0-4]]; (4) file exhibits into `_exhibits/tracer/`. **Parked deep-dives** (own sessions): Kostas's period-bending · per-category lead-time table · the break-even-vs-payables pricing signal.

---
*Spine order: Skintzi (`ΣΚΙΝΤΖΗ ΕΛΠΙΔΑ.xlsx`). Buy-side numbers stay confidential (CLAUDE §4).*
