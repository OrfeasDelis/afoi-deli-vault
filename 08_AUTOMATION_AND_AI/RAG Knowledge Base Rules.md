---
type: ai_rules
created: 2026-06-07
status: active
---

# RAG Knowledge Base Rules

## Purpose

Prepare this vault for future retrieval-augmented AI.

## Good AI-readable note

A good note has:

- Clear title
- YAML frontmatter
- One purpose
- Facts separated from opinions
- Decisions dated
- Sources linked
- Tables for repeated structures
- Stable terminology

## Bad AI-readable note

A bad note has:

- Random mixed topics
- No dates
- No source
- No owner
- Contradictory facts
- Vague names like “that supplier”
- Screenshots without explanation

## Source confidence tags

Use:

```yaml
confidence: verified | likely | memory_seed | needs_check
```

## Sensitive actions

Require human approval for:

- sending emails
- changing order status
- changing prices
- approving supplier proformas
- notifying clients of delays
- changing delivery promises
- updating financial records
