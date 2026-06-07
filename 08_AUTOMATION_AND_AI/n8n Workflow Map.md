---
type: workflow_map
tool: n8n
created: 2026-06-07
status: draft
---

# n8n Workflow Map

## Workflow 1 — Gmail proforma collector

Trigger:

- New Gmail email with attachment
- Keywords: proforma, invoice, order confirmation, conferma ordine

Actions:

1. Save attachment.
2. Identify supplier.
3. Link to order if possible.
4. Create task: proforma_check.
5. Notify operations.

## Workflow 2 — Loading/DTS parser

Trigger:

- Email from agency/supplier with DTS/loading keywords.

Actions:

1. Extract loading date.
2. Extract supplier.
3. Extract orders/products if possible.
4. Update supplier loading table.
5. Notify warehouse.

## Workflow 3 — Daily folder scanner

Trigger:

- New or modified order file.

Actions:

1. Read file metadata.
2. Create order record.
3. Extract rows if possible.
4. Flag missing required fields.
5. Notify operations.

## Workflow 4 — Ready for delivery

Trigger:

- Order lines all status 2.

Actions:

1. Check payment status.
2. Create delivery task.
3. Draft client email.
4. Await human approval.

## Workflow 5 — Weekly management summary

Trigger:

- Every Friday or Saturday.

Actions:

1. Count orders by status.
2. List stuck orders.
3. List supplier delays.
4. List delivery-ready orders.
5. List payment risks.
6. Send summary to management.
