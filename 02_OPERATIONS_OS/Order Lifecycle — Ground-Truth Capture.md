---
type: ground-truth-capture
created: 2026-06-19
updated: 2026-06-19
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
> **Status: in progress.** Batches A + B + C are interview-settled below. **D–G remain open** (see the open list) — **paused 2026-06-19, resume at batch D.** The final landing — full S1–S15 merge with Orfeas's Tracer v0.1 draft, the formal schema-diff against the 11 CSVs, repointing the draft's dangling `[[order-fulfillment-workflow-normalized]]` ref to [[Order Workflow 0-4]], and exhibits into `_exhibits/tracer/` — happens once the interview is done.

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

## 5. Discoveries (not in the artifact reconstruction)

1. **MEGASOFT** — the second system of record (accounting only; see §1).
2. **The architect/designer rebate** — fires on **full payment** of the order; calc varies case-by-case (% of value / % of margin / per-deal); tracked on a **separate sheet** as `person – project – amount`. Project-keyed → hangs off [[Projects Schema|PROJECTS]]; the architect is a `PERSON` (ERD `PEOPLE` gap).

---

## 6. Running schema-corrections (against the 11 CSVs + existing notes)

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

---

## 7. Open — remaining interview batches

- [x] **A · Order sheet** — settled 2026-06-19 (§2).
- [x] **B · Folders & ΚΟΥΒΑΣ** — settled 2026-06-19 (§3).
- [x] **C · Proforma** — settled 2026-06-19 (§4).
- [ ] **D · Loading / arrival** `← NEXT (resume here)` — ELXIS/Mercareon roles + consolidation · `09.ΠΡΟΓΡΑΜΜΑ ΠΑΡΑΔΟΣΕΩΝ` link to `est_warehouse_arrival_date` · client-facing arrival buffer (the under-promise instinct). *(Release-timing is already mostly answered by C3.)*
- [ ] **E · Receipt / delivery** — discrepancy handling (short/over/wrong/broken) · delivery vs pickup · partial delivery.
- [ ] **F · Payment / invoice / margin** — payment terms + gating detail · missing-invoice payable · where payable is tracked · transport allocation (the margin math: markup vs margin, transport before/after) · the rebate calc · is margin reviewed today.
- [ ] **G · Special cases** — returns · breakages · backorder sub-state.

---
*Spine order: Skintzi (`ΣΚΙΝΤΖΗ ΕΛΠΙΔΑ.xlsx`). Buy-side numbers stay confidential (CLAUDE §4).*
