---
type: guide
created: 2026-06-07
status: active
---

# Obsidian Plugin Setup

One-time setup for the core power set: **Dataview**, **Templater**, **Obsidian Git**. Plugin binaries must be installed from the Obsidian UI (they can't be reliably installed from the command line). `.obsidian/community-plugins.json` is pre-seeded so they activate once installed.

## Step 1 — Enable community plugins
1. Obsidian -> Settings -> **Community plugins** -> turn off Restricted Mode.
2. Click **Browse**.

## Step 2 — Install the three plugins
Search and install each, then click **Enable**:
- **Dataview** (`blacksmithgu/obsidian-dataview`) — live queries/dashboards from frontmatter.
- **Templater** (`SilentVoid13/Templater`) — dynamic templates.
- **Obsidian Git** (`Vinzent03/obsidian-git`) — commit/push from inside Obsidian.

## Step 3 — Recommended settings

### Templater
- Settings -> Templater -> **Template folder location** = `98_TEMPLATES`.
- (Optional) Enable "Trigger Templater on new file creation".

### Dataview
- Settings -> Dataview -> enable **Enable JavaScript Queries** only if needed (off by default is fine).
- Enable "Automatic view refresh".

### Obsidian Git
- **Vault backup interval (minutes):** decide per [[Open Questions]] #1. Suggested: `0` (manual) to start, or `30` for auto-backup.
- **Auto pull on startup:** on (keeps multi-device in sync).
- **Commit message:** `vault backup: {{date}}` (Obsidian Git's own format).
- Note: Obsidian Git relies on your system git + the existing `origin` remote. No extra auth needed since `gh` already configured https + token.

## Step 4 — Verify
- Open [[Obsidian Tips and Tricks]] and confirm the Dataview code blocks render as tables (not raw text).
- Create a note from a template in `98_TEMPLATES` and confirm Templater fills the date.
- In Obsidian Git: run "Commit all changes" then "Push" from the command palette.

## Notes
- Manual command-line commits (see [[Session Protocol]]) remain the canonical checkpoint method. The Git plugin is a convenience layer.
- If a plugin doesn't appear after editing `community-plugins.json`, install it via the UI first — the JSON only enables already-installed plugins.
