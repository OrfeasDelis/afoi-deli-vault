---
type: automation_backlog
created: 2026-06-07
status: active
---

# Automation Backlog

## Scoring

Score every idea:

```yaml
impact: 1-5
difficulty: 1-5
risk: 1-5
frequency: daily | weekly | monthly
human_approval_required: true/false
```

## Priority automation candidates

### 1. Kouvas read-only dashboard

- **Impact:** 5
- **Difficulty:** 3
- **Risk:** 2
- **Why:** Gives visibility without breaking current process.

### 2. Daily order intake scanner

- **Impact:** 5
- **Difficulty:** 4
- **Risk:** 3
- **Why:** Captures new accepted orders and creates structured order records.

### 3. Proforma mismatch checker

- **Impact:** 5
- **Difficulty:** 4
- **Risk:** 3
- **Why:** Prevents expensive mistakes.

### 4. DTS/loading date parser

- **Impact:** 4
- **Difficulty:** 3
- **Risk:** 2
- **Why:** Improves arrival estimates and client communication.

### 5. Ready-for-delivery draft email

- **Impact:** 4
- **Difficulty:** 2
- **Risk:** 2
- **Why:** Saves repetitive communication.

### 6. Supplier follow-up alerts

- **Impact:** 4
- **Difficulty:** 2
- **Risk:** 1
- **Why:** Prevents forgotten confirmations/loading dates.

### 7. Packaging checker

- **Impact:** 5
- **Difficulty:** 4
- **Risk:** 2
- **Why:** Prevents quantity and cost mismatches.

### 8. Client order status page

- **Impact:** 4
- **Difficulty:** 5
- **Risk:** 4
- **Why:** Powerful, but should happen after internal data is trusted.

## Add new ideas below

### Idea — Hermes Telegram capture queue (asset inbox)
```yaml
impact: 4
difficulty: 2
risk: 1
frequency: event
owner: solo
next_step: add /add command + file handler to the Circles bot host, writing to a queue (SQLite/file); reply "queued #N". See [[Hermes Telegram Capture Queue]]
```
Text Hermes a collection name/URL or forward a PDF → appended to an ingestion queue → worker later fetches into the Drive tree, writes the reference-note entry, cross-checks afoideli.gr, links back. Earlier/simpler than the monthly auto-diff; same pattern works for price lists. Reuse the Circles bot host.

### Idea — Supplier ↔ afoideli.gr cross-reference (Store API)
```yaml
impact: 4
difficulty: 2
risk: 1
frequency: monthly
owner: solo
next_step: run the Store API loop in [[Supplier Cross-Reference Workflow]] over the Kronos collection list; fill the "On afoideli.gr" column
```
Query `afoideli.gr/wp-json/wc/store/v1/products?search=<collection>` per collection to get authoritative presence + permalink (the JS store can't be checked by fetch/search reliably). Powers the supplier-vs-own-range "cross-reference machine". Unauthenticated, returns JSON. Pair with the asset-ingestion job.

### Idea — Supplier catalogue & asset ingestion (Kronos pilot → template)
```yaml
impact: 3
difficulty: 3
risk: 1
frequency: monthly
owner: solo
next_step: see [[Kronos — Catalogue & Asset Ingestion]] — confirm Drive account, pick index-notes vs Base
```
Pull each collection's catalogue PDF, technical sheet and photos into a Google Drive tree; link back from Obsidian (binaries in Drive, links+metadata in vault). Kronos first, then reused for Cielo/Mutina/Fantini. Source URLs already captured in [[Kronos — Collections Reference]].

### Idea — 
```yaml
impact:
difficulty:
risk:
frequency:
owner:
next_step:
```
