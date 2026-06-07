---
type: sop
area: operations
created: 2026-06-07
status: active
automation_priority: high
---

# Order Workflow 0–4

## Purpose

Create one canonical interpretation of order status so humans, Excel, Obsidian, n8n, and future dashboards speak the same language.

## Status 0 — Not ordered

A line is status 0 when:

- It has been accepted by the client but not yet ordered from supplier.
- It still needs checking.
- It is waiting for missing information.
- It has WAIT instructions.
- It cannot yet be sent due to deposit, code issue, quantity issue, or supplier uncertainty.

### Required fields before moving from 0 to 1

- Client/order name
- Supplier
- Product code
- Description
- Quantity
- Unit
- Selling price
- Supplier price if available
- Deposit/payment status
- Delivery/site notes
- Architect/designer if relevant

## Status 1 — Ordered / awaiting

A line is status 1 when:

- Supplier PO has been sent.
- Supplier has acknowledged or proforma is being handled.
- Loading or production is pending.
- Product is not yet physically received.

### Required fields

- Order date
- Supplier PO reference or email reference
- Proforma status
- Expected loading date if available
- Transport / agency if available

## Status 2 — Received

A line is status 2 when:

- Goods are physically received in warehouse.
- Quantity is checked.
- Damage/missing issues are recorded.
- Item is ready for delivery or client payment coordination.

### Required fields

- Received date
- Received quantity
- Warehouse note
- Damage/missing note if any
- Client notification status

## Status 3 — Delivered

A line/order is status 3 when:

- Goods have left warehouse and were delivered to client/site.
- Delivery note exists.
- Exceptions/damages are recorded.

## Status 4 — Invoiced / financially closed

A line/order is status 4 when:

- Invoice issued
- Payment or credit terms recorded
- Balance settled or due date tracked

## Automation interpretation

Future systems should treat `order_line_status` as the truth, not only the parent order status.

Parent order status should be derived from line statuses:

- If any active line = 0 → parent needs action.
- If all active lines = 1 → ordered / waiting.
- If all active lines = 2 → ready for delivery.
- If all active lines = 3 → delivered.
- If all active lines = 4 → closed.

## WAIT rule

A WAIT note applies only to the specific row/line unless explicitly marked as whole-order WAIT.

Fields:

```yaml
wait_type: row | order
wait_reason:
wait_owner:
wait_until:
```
