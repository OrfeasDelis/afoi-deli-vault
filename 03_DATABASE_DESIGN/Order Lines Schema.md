---
type: schema
entity: order_lines
status: active
---

# Order Lines Schema

## Purpose

The atomic unit of operations.

## Fields

```yaml
order_line_id:
order_id:
line_number:
supplier:
brand:
product_code:
description:
collection:
finish:
size:
unit:
quantity:
supplier_quantity:
packaging_unit:
status_0_4:
wait_type:
wait_reason:
cancelled:
po_sent_date:
proforma_status:
loading_date:
expected_arrival:
received_date:
received_quantity:
delivered_date:
invoice_status:
notes:
```

## Why order lines matter

A parent order can hide operational truth.  
Order lines reveal what is actually blocking progress.
