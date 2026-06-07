---
type: sop
area: operations
created: 2026-06-07
status: draft
automation_priority: high
---

# DTS and Loading Date SOP

## Purpose

Track when supplier goods are loading so arrival estimates and client promises become reliable.

## Trigger

Supplier or agency sends loading date / DTS / transport confirmation.

## Required fields

```yaml
supplier:
loading_reference:
loading_date:
expected_arrival_date:
transport_company:
agency:
orders_included:
client_orders_affected:
pallets:
notes:
email_thread:
attachment:
```

## Actions

1. Record loading date in Kouvas.
2. Link loading to order lines.
3. Update expected arrival.
4. Notify internal team.
5. Prepare warehouse receiving expectation.
6. Notify clients only if policy allows and dates are reliable.

## Future automation

- Gmail watches for DTS/loading emails.
- Attachment is parsed.
- Supplier and order references are matched.
- Loading date is extracted.
- Dashboard updates affected orders.
- Warehouse receives expected arrival list.
