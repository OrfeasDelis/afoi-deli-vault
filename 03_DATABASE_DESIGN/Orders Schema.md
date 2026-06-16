---
type: schema
entity: orders
status: active
---

# Orders Schema

## Purpose

Parent object for client orders.

## Fields

> [!note] Source of truth (audit P0-2, 2026-06-16)
> `orders.csv` (`97_CSV_SCHEMAS`) is the **canonical stored contract** — the columns that physically exist as data. This note annotates it: the *derived* fields below are computed by the Python worker and are **not** stored in the CSV. If a stored column changes, change `orders.csv` first, then mirror it here.

**Stored columns** — match `orders.csv` exactly:

```yaml
order_id:
order_date:
client:
project:
salesperson:
source_file:
folder_state:        # materialized from line statuses (worker recomputes)
overall_status:      # materialized from order lines (worker recomputes)
payment_status:
deposit_received:
balance_due:
total_sell_value:
estimated_cost:
estimated_margin:
contains_wait:
next_action:
owner:
```

**Derived only** — computed at read time, NOT stored in `orders.csv`:

```yaml
ready_for_supplier_order:   # all active lines ready to order
ready_for_delivery:         # all active lines status 2 + payment check
invoice_status:             # rolled up from client_invoices
delivery_status:            # rolled up from line statuses / supplier loadings
```

## Derived logic

- `overall_status` should be derived from order lines.
- `folder_state` should be derived from line statuses.
- `ready_for_delivery` requires all active lines status 2 plus payment check.

## Relationships

- Links to [[03_DATABASE_DESIGN/Order Lines Schema]]
- Links to [[03_DATABASE_DESIGN/Clients Schema]]
- Links to [[03_DATABASE_DESIGN/Projects Schema]]
