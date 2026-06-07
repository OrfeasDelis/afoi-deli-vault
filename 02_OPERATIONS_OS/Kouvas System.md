---
type: system_note
area: operations
created: 2026-06-07
status: active
automation_priority: very_high
---

# Kouvas System

## What Kouvas is

Kouvas is the current operational master file where product lines from accepted orders are grouped by supplier.

It is effectively the pre-database.

## Current logic

- One sheet per supplier.
- Lines are copied/pasted from accepted order files.
- Supplier buckets help batching.
- Statuses track ordering/receiving.
- Loading dates/DTS information are manually updated.
- Used to communicate with agencies/suppliers and manage arrivals.

## Why it matters

Kouvas contains the operational truth that the future database must learn from.

## Future database equivalents

| Kouvas concept | Future database table |
|---|---|
| Supplier sheet | suppliers |
| Client order row | order_lines |
| Status F column | order_line_status |
| Loading date | supplier_loadings |
| Product code | products |
| Client order file | orders |
| Notes | order_line_notes |
| WAIT | exceptions |

## Migration strategy

### Phase 1 — Document
Document every column and rule.

### Phase 2 — Read-only extraction
Use scripts or n8n to read Kouvas and create snapshots.

### Phase 3 — Validation
Compare extracted data with manual reality.

### Phase 4 — Dashboard
Create order status dashboard from Kouvas.

### Phase 5 — Write-back only after confidence
Do not allow automation to edit Kouvas until the read-only dashboard is trusted.

## Fields to document

- Sheet name
- Supplier
- Client/order name
- Order date
- Product code
- Description
- Unit
- Quantity
- Status
- Loading date
- Notes
- Proforma reference
- Invoice reference
- Transport reference

## Risks

- Human copy/paste errors
- Different suppliers using different packaging units
- Duplicate rows
- Partially received orders
- WAIT notes misunderstood
- File naming inconsistencies
- Manual overwrites
