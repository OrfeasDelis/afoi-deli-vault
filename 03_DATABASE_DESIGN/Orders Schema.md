---
type: schema
entity: orders
status: active
---

# Orders Schema

## Purpose

Parent object for client orders.

## Fields

```yaml
order_id:
order_date:
client:
project:
salesperson:
source_file:
folder_state:
overall_status:
payment_status:
deposit_received:
balance_due:
total_sell_value:
estimated_cost:
estimated_margin:
contains_wait:
ready_for_supplier_order:
ready_for_delivery:
invoice_status:
delivery_status:
next_action:
owner:
```

## Derived logic

- `overall_status` should be derived from order lines.
- `folder_state` should be derived from line statuses.
- `ready_for_delivery` requires all active lines status 2 plus payment check.

## Relationships

- Links to [[03_DATABASE_DESIGN/Order Lines Schema]]
- Links to [[03_DATABASE_DESIGN/Clients Schema]]
- Links to [[03_DATABASE_DESIGN/Projects Schema]]
