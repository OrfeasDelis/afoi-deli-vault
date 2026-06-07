---
type: sop
area: finance
created: 2026-06-07
status: draft
automation_priority: medium
---

# Finance and Credit Terms SOP

## Purpose

Connect operational status with money.

## Key moments

1. Quote accepted
2. Deposit received
3. Supplier PO sent
4. Supplier invoice/proforma due
5. Goods loaded
6. Goods received
7. Client delivery
8. Client invoice
9. Payment / credit due date
10. Closure

## Required fields

```yaml
client_total:
supplier_cost:
gross_margin:
transport_cost:
other_costs:
deposit_received:
balance_due:
supplier_payment_terms:
client_payment_terms:
invoice_issued:
invoice_date:
credit_due_date:
payment_status:
```

## Risks

- Order placed before safe deposit.
- Supplier invoice due before client cash timing.
- Delivery made before balance clarity.
- Profitability unclear after transport/logistics.
- Credit periods not monitored.

## Future automation

- Due date reminders
- Supplier credit calendar
- Client balance alerts before delivery
- Profitability dashboard
- 15-day accounting export preparation
