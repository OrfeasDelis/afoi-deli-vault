---
type: sop
area: warehouse
created: 2026-06-07
status: draft
automation_priority: high
---

# Warehouse Receiving SOP

## Purpose

Turn physical receipt into reliable digital truth.

## Trigger

Goods arrive in warehouse.

## Check

- Supplier
- Pallet / package count
- Client/order labels
- Product codes
- Quantities
- Damages
- Missing items
- Mixed-client pallets
- Repackaging needs

## Update

For each received line:

```yaml
received_date:
received_quantity:
status: 2
warehouse_note:
damage_note:
missing_quantity:
photo_reference:
ready_for_delivery: true/false
```

## Photos

Use WhatsApp or future upload form to attach:

- pallet label
- product label
- damaged pieces
- quantity proof
- delivery grouping

## Future automation

A warehouse mobile form should allow:

- scan / search order
- mark received
- upload photos
- note missing/damage
- notify operations
- trigger client ready-to-deliver draft
