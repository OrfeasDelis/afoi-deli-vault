---
type: sop
area: operations
created: 2026-06-07
status: draft
automation_priority: very_high
owner_role: operations
---

# Daily Order Processing SOP

## Purpose

Standardize the daily order flow before automating it.

## Trigger

A salesperson saves or updates an accepted order file in the **Daily** folder.

## Step 1 — Open order file

Check:

- Client name
- Project/site
- Salesperson
- Date
- Supplier per line
- Product codes
- Descriptions
- Quantities
- Units
- Prices
- Deposit/payment information
- Architect/designer reference
- Delivery notes

## Step 2 — Health check

Mark order as unsafe if any of the following are missing:

- Supplier
- Product code
- Quantity
- Unit
- Client name
- Payment/deposit status
- Required technical detail
- Special finish / color / size confirmation

## Step 3 — Line classification

For each row:

| Condition | Action |
|---|---|
| Ready to order | Paste into Kouvas supplier sheet |
| WAIT on row | Keep row excluded and note reason |
| Missing code | Return to salesperson |
| Unclear quantity | Check packaging |
| Deposit missing | Flag finance |
| Supplier unknown | Escalate |

## Step 4 — Paste into Kouvas

For each supplier:

- Go to supplier sheet.
- Paste the relevant lines.
- Add order date.
- Add client/order reference.
- Keep status 0 until PO is sent/confirmed according to current policy.

## Step 5 — Create supplier PO email

Use [[02_OPERATIONS_OS/Supplier PO Creation SOP]].

## Step 6 — Update file/folder state

- If any relevant line remains 0 → move/keep in **Prwto**.
- If all relevant lines are status 1 → move to **Deftero**.
- If all relevant lines are status 2 → move to **Pros Paradosi**.

## Step 7 — Record exceptions

Every exception should become either:

- a note in the order file
- a row note in Kouvas
- an item in [[02_OPERATIONS_OS/Exception Handling Rules]]
- a future automation entry in [[08_AUTOMATION_AND_AI/Automation Backlog]]

## Minimum automation fields

```yaml
order_id:
source_file:
client:
salesperson:
created_date:
processed_date:
contains_wait: true/false
all_lines_ordered: true/false
all_lines_received: true/false
folder_state:
next_action:
next_action_owner:
```
