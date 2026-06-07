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

## Views to create later

- Due this week
- Overdue
- Large upcoming payments
- Supplier credit exposure
- Client balances before delivery
- 15-day accounting export
