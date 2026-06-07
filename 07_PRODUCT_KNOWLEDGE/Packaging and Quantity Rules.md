---
type: operational_knowledge
created: 2026-06-07
status: active
automation_priority: very_high
---

# Packaging and Quantity Rules

## Why this matters

Packaging mismatches create order, price, and delivery errors.

Example risk from past discussions:

- Client quantity may be calculated in m².
- Supplier packaging may force different box quantity.
- Order quantity must sometimes round to full boxes.

## Fields to capture per product

```yaml
supplier:
product_code:
unit:
sqm_per_box:
pieces_per_box:
minimum_order:
rounding_rule:
supplier_quantity_unit:
notes:
```

## Automation idea

Before supplier PO, system checks:

```text
client_quantity ÷ sqm_per_box = valid full box quantity?
```

If not, flag:

- required supplier quantity
- difference from quote
- extra cost
- salesperson approval needed
