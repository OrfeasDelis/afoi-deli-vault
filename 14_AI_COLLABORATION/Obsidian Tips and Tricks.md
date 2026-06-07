---
type: guide
created: 2026-06-07
status: active
---

# Obsidian Tips and Tricks

Practical techniques to interconnect knowledge and notes. Complements `99_SYSTEM/Obsidian Usage Rules` (the rules); this note is the how-to.

## Linking & connection
- **Link aggressively.** Every entity mention should be a `[[link]]`. Connections are the value, not the folders.
- **Aliases** in frontmatter let one note be linked by many names:
  ```yaml
  aliases: [Florim, Floor Gres, FLORIM SpA]
  ```
- **Backlinks panel** (right sidebar) shows what references the current note — your "who depends on this" view.
- **Unlinked mentions** (bottom of backlinks) surfaces text matches you haven't linked yet; convert them.
- **Link to headings/blocks** for precision: `[[Orders Schema#Fields]]`, `[[note^block-id]]`.

## Maps of Content (MOCs)
- A MOC is a hub note that links a topic's notes (e.g. [[Collaboration Home]], `07_PRODUCT_KNOWLEDGE/Product Knowledge Map`).
- Rule of thumb: when a folder has ~7+ notes, give it a MOC.

## Tags vs links
- **Links** = strong, navigable relationships (prefer these).
- **Tags** = lightweight cross-cutting status/filters: `#draft`, `#needs_check`, `#automation/high`.
- Keep a small, stable tag vocabulary. Nested tags (`#supplier/core`) group nicely.

## Frontmatter as data
- Consistent frontmatter turns notes into a queryable database (via Dataview).
- Always include `type`, `created`, `status`; add `confidence` for factual notes.

## Dataview quick wins (after plugin install)
- All draft notes:
  ````
  ```dataview
  table status, confidence, file.mtime as "Updated"
  from "" where status = "draft"
  sort file.mtime desc
  ```
  ````
- Suppliers needing data:
  ````
  ```dataview
  table country, confidence
  from "04_SUPPLIERS_AND_BRANDS/Suppliers"
  where confidence = "memory_seed"
  ```
  ````
- Open questions across the vault: search `confidence: needs_check`.

## Templater quick wins (after plugin install)
- Auto-insert `created:` date, titles, and section scaffolds when creating from `98_TEMPLATES`.
- Dynamic dates: `<% tp.date.now("YYYY-MM-DD") %>`.

## Graph hygiene
- Use **local graph** (depth 1–2) to spot orphaned or under-linked notes.
- Color groups by folder or tag to see structure at a glance.

## Daily capture
- Use `13_DAILY_NOTES` for fast capture; link out to the real home note instead of writing facts in the daily note.

## Search operators
- `path:`, `tag:`, `line:()`, and `/regex/` make search powerful — e.g. `path:Suppliers confidence: memory_seed`.
