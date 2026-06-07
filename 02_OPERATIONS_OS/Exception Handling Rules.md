---
type: exception_rules
area: operations
created: 2026-06-07
status: active
automation_priority: high
---

# Exception Handling Rules

## Why this matters

Automations fail where exceptions are not named.

## Exception categories

| Code | Exception | Action |
|---|---|---|
| WAIT_ROW | One product row must wait | Exclude row only |
| WAIT_ORDER | Whole order must wait | Keep order in Prwto |
| MISSING_CODE | Product code missing | Return to salesperson |
| QTY_PACKAGING | Quantity conflicts with packaging | Check supplier rules |
| PRICE_DELTA | Price differs from expectation | Escalate before PO |
| PROFORMA_MISMATCH | Supplier proforma mismatch | Hold order |
| PARTIAL_RECEIPT | Some goods received | Keep line-level truth |
| DAMAGE | Damaged goods | Photo + supplier/client action |
| CANCELLED_LINE | Line cancelled | Exclude from active status |
| CLIENT_BALANCE | Payment not settled | Hold delivery |
| SUPPLIER_DELAY | Loading delayed | Notify internal/client if needed |

## Exception note format

```yaml
exception_code:
affected_line:
description:
owner:
created_date:
deadline:
resolved: false
resolution:
```

## Rule

Every repeated exception becomes:

1. A rule.
2. A checklist.
3. A future automation.
