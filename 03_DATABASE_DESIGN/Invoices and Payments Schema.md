---
type: schema
entity: finance
status: active
---

# Invoices and Payments Schema

## Supplier invoice fields

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

## Client invoice/payment fields

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
