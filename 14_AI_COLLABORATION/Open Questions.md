---
type: open_questions
created: 2026-06-07
updated: 2026-06-07
status: active
---

# Open Questions

Live list of decisions to resolve about the vault, collaboration, and future apps. (Operational/business questions live in `00_COMMAND_CENTER/Questions To Resolve`.)

## Open
| # | Question | Context | Owner | Status |
|---|----------|---------|-------|--------|
| 1 | Backup cadence — manual commits only, or enable Obsidian Git auto-push timer? | See [[Obsidian Plugin Setup]] | Orfeas | open |
| 2 | Which data is too sensitive to ever commit (even to a private repo)? | Define a no-commit list; extend `.gitignore` if needed | Orfeas | open |
| 3 | n8n hosting — self-hosted (Docker) or n8n cloud? | Needed before Phase 3 | Orfeas | open |
| 4 | Postgres hosting — local, Supabase, or managed? | Needed before Phase 4 | Orfeas | open |
| 5 | Verify company revenue and other `needs_check` facts | See [[Vault State Memory]] §7 | Orfeas | open |

## Resolved
| # | Question | Decision | Date |
|---|----------|----------|------|
| R1 | Where should cross-session memory live? | In-vault `14_AI_COLLABORATION` folder | 2026-06-07 |
| R2 | GitHub repo visibility? | Private repo `afoi-deli-vault` | 2026-06-07 |
| R3 | Which Obsidian plugins? | Dataview, Templater, Obsidian Git | 2026-06-07 |
| R4 | Git commit identity? | Orfeas Delis / GitHub noreply email | 2026-06-07 |

*Move rows from Open to Resolved when decided; record the rationale in [[Architecture Decision Records]].*
