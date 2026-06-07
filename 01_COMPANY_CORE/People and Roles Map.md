---
type: org_map
created: 2026-06-07
status: draft
---

# People and Roles Map

## Purpose

Document who does what so future automations and dashboards can route tasks correctly.

## Core roles

| Role | Responsibilities | Automation relevance |
|---|---|---|
| Sales | Quotes, client communication, selections | Quote intake, client notes |
| Operations | Order processing, Kouvas, supplier POs | Status changes, supplier emails |
| Warehouse | Receiving, checking, delivery prep | Status 2, photos, missing items |
| Delivery / logistics | Scheduling, transport coordination | Client notifications, route planning |
| Finance / accounting | Invoices, payments, credit periods | Due alerts, invoice matching |
| Management | Strategy, exceptions, supplier relationships | Dashboards, decisions |

## Future role clarity

Each workflow note should specify:

```yaml
owner_role:
backup_role:
approval_required:
escalation_person:
```

## Questions

- Who owns supplier PO creation?
- Who owns proforma approval?
- Who owns loading date entry?
- Who owns warehouse receipt update?
- Who owns client ready-to-deliver notification?
- Who owns payment/credit follow-up?
