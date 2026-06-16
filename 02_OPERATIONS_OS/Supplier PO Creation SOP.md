---
type: sop
area: operations
created: 2026-06-07
status: draft
automation_priority: high
---

# Supplier PO Creation SOP

## Trigger

Lines are ready in Kouvas for a supplier order.

## Required data

- Supplier
- Client/order reference
- Product code
- Description
- Quantity
- Unit
- Requested delivery/loading timing
- Special notes
- Commercial terms if relevant

## Email structure

Subject:

```text
Order Request - [Supplier] - [Client/Project] - [Date]
```

Body:

```text
Dear [Name],

Please proceed with the following order:

[table of product code / description / quantity / unit / notes]

Kindly send us your proforma confirmation and estimated loading date.

Best regards,
Afoi Deli Floor + Bath
```

## Attachments

- Order file if needed
- Quote PDF if supplier requires
- Technical drawings if relevant
- Kitchen/layout files if relevant

## After sending

Update:

```yaml
po_sent: true
po_sent_date:
po_email_thread:
order_line_status: 1
awaiting: proforma | loading_date | confirmation
```

## Future automation

The Python worker can:

1. Read supplier-ready rows.
2. Generate draft email.
3. Attach relevant files.
4. Save Gmail draft.
5. Wait for human approval.
6. Update status after sending.
