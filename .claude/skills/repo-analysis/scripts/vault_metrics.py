"""Deterministic vault metrics for the /repo-analysis skill.

Computes note counts, folder counts, frontmatter tallies, the wikilink graph
(hubs / orphans / broken targets), and attachment inventory. Prints stable,
sorted JSON to stdout so repeated runs on an unchanged vault are byte-identical.

CRITICAL: all files are read as UTF-8. PowerShell/cp1252 misreads em-dashes
(char 8212) in note names and manufactures phantom broken links + orphans
(see the vault-audit skill's warning, 2026-06-17: 122 false positives).

Usage: python vault_metrics.py [vault_root]
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

EXCLUDED_DIRS = {".git", ".obsidian", ".claude", ".githooks", "docs", "node_modules"}
WIKILINK_RE = re.compile(r"(!?)\[\[([^\[\]]+)\]\]")
MDLINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
PLACEHOLDER_RE = re.compile(r"[<>]|^(wikilinks|their-name|name|note title)$", re.IGNORECASE)


def is_excluded(path: Path, root: Path) -> bool:
    return any(part in EXCLUDED_DIRS for part in path.relative_to(root).parts)


def parse_frontmatter(text: str) -> dict:
    """Minimal zero-dependency YAML frontmatter parse (scalars + simple lists)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fm, current_key = {}, None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if re.match(r"^\s+-\s+", line) and current_key:
            fm.setdefault(current_key, [])
            if isinstance(fm[current_key], list):
                fm[current_key].append(line.split("-", 1)[1].strip().strip("\"'"))
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m:
            key, value = m.group(1), m.group(2).strip()
            current_key = key
            if value.startswith("[") and value.endswith("]"):
                fm[key] = [v.strip().strip("\"'") for v in value[1:-1].split(",") if v.strip()]
            elif value == "":
                fm[key] = []
            else:
                fm[key] = value.strip("\"'")
    return fm


ATTACHMENT_SUFFIXES = (".html", ".svg", ".png", ".jpg", ".jpeg", ".pdf", ".csv", ".base", ".canvas")


def normalize_target(raw: str) -> str:
    # Obsidian tables escape the alias pipe as \| — split on both forms.
    target = re.split(r"\\\||\|", raw)[0].split("#")[0].split("^")[0].strip().rstrip("\\")
    if "/" in target:
        target = target.rsplit("/", 1)[1]
    if target.lower().endswith(".md"):
        target = target[:-3]
    return target


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    notes, attachments = [], Counter()
    for path in sorted(root.rglob("*")):
        if path.is_dir() or is_excluded(path, root):
            continue
        if path.suffix.lower() == ".md":
            notes.append(path)
        else:
            attachments[path.suffix.lower() or "(none)"] += 1

    folders = sorted(
        {str(p.relative_to(root).parts[0]) for p in notes if len(p.relative_to(root).parts) > 1}
    )

    name_to_note = {}
    alias_to_note = {}
    meta = {}
    for path in notes:
        rel = str(path.relative_to(root)).replace("\\", "/")
        text = path.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        meta[rel] = {"fm": fm, "text": text}
        name_to_note[path.stem.lower()] = rel
        aliases = fm.get("aliases", [])
        if isinstance(aliases, str):
            aliases = [aliases]
        for alias in aliases:
            alias_to_note.setdefault(alias.lower(), rel)

    out_links = defaultdict(set)
    in_links = defaultdict(set)
    totals = Counter()
    broken = Counter()
    for rel, info in meta.items():
        body = FENCE_RE.sub("", info["text"])
        body = INLINE_CODE_RE.sub("", body)
        for embed_mark, raw in WIKILINK_RE.findall(body):
            totals["wikilinks_total"] += 1
            if embed_mark:
                totals["embeds"] += 1
            target = normalize_target(raw)
            if not target:
                continue
            resolved = name_to_note.get(target.lower()) or alias_to_note.get(target.lower())
            if resolved:
                totals["wikilinks_resolved"] += 1
                if resolved != rel:
                    out_links[rel].add(resolved)
                    in_links[resolved].add(rel)
            elif target.lower().endswith(ATTACHMENT_SUFFIXES):
                totals["attachment_links"] += 1
            elif PLACEHOLDER_RE.search(target):
                totals["placeholder_links"] += 1
            else:
                broken[target] += 1
        for target in MDLINK_RE.findall(body):
            if not target.startswith(("http://", "https://", "mailto:")):
                totals["markdown_internal_links"] += 1

    fm_tallies = {"type": Counter(), "status": Counter(), "confidence": Counter()}
    tags = Counter()
    missing_fm = []
    for rel, info in meta.items():
        fm = info["fm"]
        if not fm:
            missing_fm.append(rel)
        for key in fm_tallies:
            value = fm.get(key)
            if isinstance(value, str) and value:
                fm_tallies[key][value] += 1
        note_tags = fm.get("tags", [])
        if isinstance(note_tags, str):
            note_tags = [note_tags]
        for tag in note_tags:
            tags[tag] += 1

    degree = {
        rel: {"in": len(in_links.get(rel, ())), "out": len(out_links.get(rel, ()))}
        for rel in meta
    }
    hubs = sorted(
        ({"note": rel, **d, "degree": d["in"] + d["out"]} for rel, d in degree.items()),
        key=lambda h: (-h["degree"], h["note"]),
    )[:10]
    no_inbound = sorted(rel for rel, d in degree.items() if d["in"] == 0)
    strict_orphans = sorted(rel for rel, d in degree.items() if d["in"] == 0 and d["out"] == 0)

    result = {
        "note_count": len(notes),
        "folder_count": len(folders),
        "notes_per_folder": dict(
            sorted(Counter(str(p.relative_to(root).parts[0]) if len(p.relative_to(root).parts) > 1 else "(root)" for p in notes).items())
        ),
        "attachments": dict(sorted(attachments.items())),
        "links": dict(sorted(totals.items())),
        "unique_edges": sum(len(v) for v in out_links.values()),
        "broken_targets": dict(sorted(broken.items(), key=lambda kv: (-kv[1], kv[0]))),
        "frontmatter": {
            key: dict(sorted(counter.items(), key=lambda kv: (-kv[1], kv[0])))
            for key, counter in fm_tallies.items()
        },
        "tags": dict(sorted(tags.items(), key=lambda kv: (-kv[1], kv[0]))),
        "notes_missing_frontmatter": sorted(missing_fm),
        "top_hubs": hubs,
        "no_inbound_count": len(no_inbound),
        "no_inbound": no_inbound,
        "strict_orphans": strict_orphans,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
