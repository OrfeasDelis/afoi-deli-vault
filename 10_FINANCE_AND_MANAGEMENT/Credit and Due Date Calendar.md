---
type: finance_system
created: 2026-06-07
status: draft
automation_priority: medium
---

# Credit and Due Date Calendar

## Purpose

Prevent supplier/client payment surprises.

## Fields

```yaml
party:
party_type: supplier | client
invoice_number:
invoice_date:
amount:
due_date:
payment_status:
related_order:
responsible_person:
notes:
```

## Supplier credit terms (known)

The payment window per supplier — drives `due_date` (= invoice_date + term) and supplier credit-exposure.

| Supplier | Standard orders | Stock orders | Source |
|---|---|---|---|
| [[Supplier - Kronos\|Kronos]] | **90 days** | **120 days** | verified, Orfeas 2026-06-17 |

*Add each house as its terms are confirmed (via [[Supplier Enrichment Queue]]). Cost-side derivation of the invoice amounts: [[Cost & Quote Build]].*

## Views to create later

- Due this week
- Overdue
- Large upcoming payments
- Supplier credit exposure
- Client balances before delivery
- 15-day accounting export
