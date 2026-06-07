---
type: sop
area: operations
created: 2026-06-07
status: draft
automation_priority: very_high
---

# Proforma Checking SOP

## Purpose

Prevent costly mistakes before supplier order confirmation.

## Check every proforma against

- Client/order file
- Kouvas row
- Supplier price list
- Payment terms
- Product code
- Product description
- Finish/color
- Size
- Quantity
- Unit
- Packaging
- Discount
- VAT / tax context
- Loading date
- Transport terms
- Special notes

## Common risks

- Wrong product code
- Wrong finish
- Supplier packaging changes quantity
- Wrong discount
- Wrong client/order reference
- Missing item
- Extra item
- Wrong lead time
- Wrong delivery terms
- Price list outdated

## Check table

| Check | OK? | Notes |
|---|---|---|
| Supplier correct | | |
| Product codes match | | |
| Quantities match | | |
| Units match | | |
| Prices match expectation | | |
| Discount correct | | |
| Packaging acceptable | | |
| Lead time acceptable | | |
| Payment terms clear | | |
| Transport/loading clear | | |

## Future AI role

A future agent should compare proforma PDF/Excel to Kouvas and flag:

- mismatched codes
- quantity deltas
- price deltas
- missing lines
- unexpected lead times
- supplier terms requiring approval
