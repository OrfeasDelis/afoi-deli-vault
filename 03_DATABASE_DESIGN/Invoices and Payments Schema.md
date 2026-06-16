---
type: schema
entity: finance
status: active
---

# Invoices and Payments Schema

> [!note] Two tables, two CSVs (audit P0-2 decision, 2026-06-16)
> Invoices are modelled as **two separate tables** — supplier-side (accounts payable) and client-side (accounts receivable), because the two flows differ. Each maps to its own canonical stored contract in `97_CSV_SCHEMAS`: **`supplier_invoices.csv`** (AP) and **`client_invoices.csv`** (AR). The CSVs are the stored columns; this note annotates them. (Replaces the earlier single unified `invoices_payments.csv`.)

## Supplier invoice fields → `supplier_invoices.csv` (accounts payable)

```yaml
supplier_invoice_id:
supplier:
invoice_number:
invoice_date:
due_date:
amount:
vat:
related_orders:
payment_status:
credit_terms:
attachment:
```

## Client invoice/payment fields → `client_invoices.csv` (accounts receivable)

```yaml
client_invoice_id:
client:
order_id:
invoice_number:
invoice_date:
amount:
balance_due:
due_date:
payment_status:
notes:
```
