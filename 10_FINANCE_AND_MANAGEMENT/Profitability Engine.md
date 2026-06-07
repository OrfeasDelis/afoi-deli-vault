---
type: finance_system
created: 2026-06-07
status: draft
automation_priority: high
---

# Profitability Engine

## Purpose

See profit before operational mistakes consume it.

## Per order fields

```yaml
sell_total:
supplier_cost_total:
discount_given:
transport_cost:
installation_cost:
other_cost:
gross_margin_amount:
gross_margin_percent:
payment_risk:
delivery_risk:
```

## Margin risks

- Discount too high
- Supplier cost changed
- Transport not included
- Installation not included
- Packaging quantity changed
- Credit terms create cash pressure
- Partial delivery increases logistics cost

## Future automation

At quote acceptance, system should flag:

- Low-margin order
- Unknown supplier cost
- Missing transport cost
- Deposit below threshold
- High-value client with unclear payment
