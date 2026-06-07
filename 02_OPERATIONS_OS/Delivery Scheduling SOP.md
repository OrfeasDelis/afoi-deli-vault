---
type: sop
area: logistics
created: 2026-06-07
status: draft
automation_priority: medium
---

# Delivery Scheduling SOP

## Trigger

Order or order lines reach status 2 / received.

## Required checks before client notification

- Full order received or partial delivery approved
- Payment status checked
- Delivery address confirmed
- Site readiness confirmed
- Special unloading needs checked
- Large slab / fragile item handling checked
- Warehouse has grouped items correctly

## Client notification tone

Premium, calm, human, direct.

Example:

```text
Καλησπέρα σας,

Σας ενημερώνουμε ότι η παραγγελία σας έχει παραληφθεί στην αποθήκη μας και μπορούμε να προχωρήσουμε στον προγραμματισμό της παράδοσης.

Παρακαλώ ενημερώστε μας για τη διαθεσιμότητά σας και την ετοιμότητα του χώρου, ώστε να συντονίσουμε αντίστοιχα.

Με εκτίμηση,
Αφοί Δελή Floor + Bath
```

## Future automation

- When all active lines are status 2, create draft email.
- Check payment status first.
- If balance due, route to finance before delivery confirmation.
- Add delivery scheduling task.
