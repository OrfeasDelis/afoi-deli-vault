#!/usr/bin/env python3
"""Vault baseline registry pack — Pass 0/1 deterministic layer.

Read-only over the vault; writes JSON only to _meta/consolidation/data/.
Outputs: note_registry.json, link_graph.json, title_collisions.json,
frontmatter_violations.json, sources_inventory.json, sensitivity_locations.json,
summary.json (+ a human summary on stdout).

Sensitivity scan reports path+line+category ONLY — never the matched value.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parents[1]
OUT_DIR = VAULT / "_meta" / "consolidation" / "data"

EXCLUDE_DIRS = {".git", ".obsidian", ".claude", ".githooks", ".trash", "scripts", "node_modules"}
ALLOWED_STATUS = {"active", "draft", "seed", "idea", "complete", "backlog", "living"}
ALLOWED_CONFIDENCE = {"verified", "likely", "memory_seed", "needs_check"}
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WIKILINK = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
PERSONAL_PREFIXES = ("12_PERSONAL_OS", "15_PERSONAL_LIFE", "17_JOURNAL")

SENSITIVITY_PATTERNS = [
    ("commercial_terms", re.compile(r"(?i)(?:discount|sconto|cascade|εκπτω)\S*.*(?:%|−\s?\d{1,2}|-\s?\d{1,2}\b)")),
    ("payment_terms", re.compile(r"(?i)\b(?:30|60|90|120)\s?(?:d|gg|days|ημέρες|ημερών)\b")),
    ("price_figure", re.compile(r"€\s?\d|\d\s?€|\beuro\b.{0,4}\d")),
    ("contact_email", re.compile(r"[\w.+-]+@[\w-]+\.\w{2,}")),
    ("contact_phone", re.compile(r"\+30\s?\d{9,10}|\b69\d{8}\b|\b21\d{8}\b")),
    ("financial_id", re.compile(r"(?i)\bIBAN\b|\bGR\d{2}\s?\d{4}|\bΑΦΜ\b|\bP\.?\s?IVA\b|\bVAT\b")),
    ("client_identity", re.compile(r"(?i)Skintzi|Kaliontzis|Igeiasi")),
    ("revenue_figure", re.compile(r"(?i)€\s?\d+\s?m\b|revenue")),
]


def rel(p: Path) -> str:
    return p.relative_to(VAULT).as_posix()


def zone_of(relpath: str) -> str:
    parts = relpath.split("/")
    if "_sources" in parts:
        return "sources"
    if parts[0] == "_meta":
        return "meta"
    if parts[0] == "docs":
        return "generated"
    if parts[0].startswith(("97_", "98_", "99_")):
        return "system"
    if parts[0].startswith(PERSONAL_PREFIXES):
        return "personal"
    if len(parts) == 1:
        return "root"
    return "content"


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    lines = text.split("\n")
    fm: dict = {}
    key = None
    for line in lines[1:]:
        if line.strip() in ("---", "..."):
            break
        if re.match(r"^\s+-\s", line) and key:
            fm.setdefault(key, [])
            if isinstance(fm[key], list):
                fm[key].append(line.strip()[1:].strip().strip('"'))
            continue
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip().strip('"')
            fm[key] = val if val else []
    return {k: v for k, v in fm.items()}


def normalize_title(stem: str) -> str:
    s = unicodedata.normalize("NFKD", stem).casefold()
    return re.sub(r"[^a-z0-9α-ω]", "", s)


def walk_files():
    for p in sorted(VAULT.rglob("*")):
        if p.is_dir():
            continue
        if any(part in EXCLUDE_DIRS for part in p.relative_to(VAULT).parts):
            continue
        if OUT_DIR in p.parents:
            continue
        yield p


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    md_files, other_files = [], []
    for p in walk_files():
        (md_files if p.suffix.lower() == ".md" else other_files).append(p)

    # --- note registry -------------------------------------------------
    registry: dict[str, dict] = {}
    stem_index: dict[str, list[str]] = {}
    fullname_index: dict[str, list[str]] = {}
    for p in md_files:
        r = rel(p)
        text = p.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        h1 = next((ln[2:].strip() for ln in text.split("\n") if ln.startswith("# ")), "")
        links = [t.strip() for t in WIKILINK.findall(text)]
        registry[r] = {
            "path": r,
            "zone": zone_of(r),
            "title": h1 or p.stem,
            "stem": p.stem,
            "type": fm.get("type", ""),
            "status": fm.get("status", ""),
            "confidence": fm.get("confidence", ""),
            "created": fm.get("created", ""),
            "updated": fm.get("updated", ""),
            "has_frontmatter": bool(fm),
            "words": len(text.split()),
            "outbound": links,
            "inbound": 0,
            "inbound_from": [],
        }
        stem_index.setdefault(p.stem, []).append(r)
    for p in other_files:
        fullname_index.setdefault(p.name, []).append(rel(p))

    # --- link resolution ----------------------------------------------
    # Bare-name links are the vault convention (CLAUDE.md §3); Obsidian also
    # resolves path-style targets, so count those as edges but report them
    # separately as convention violations.
    relpath_noext = {r[:-3]: r for r in registry}
    broken: list[dict] = []
    path_style: list[dict] = []
    edges = 0
    for r, note in registry.items():
        for target in set(note["outbound"]):
            tpaths = stem_index.get(target)
            if not tpaths and "/" in target:
                hit = relpath_noext.get(target)
                tpaths = [hit] if hit else stem_index.get(target.rsplit("/", 1)[1])
                if tpaths:
                    path_style.append({"from": r, "target": target})
            if tpaths:
                edges += 1
                for tp in tpaths:
                    if tp != r:
                        registry[tp]["inbound"] += 1
                        registry[tp]["inbound_from"].append(r)
            elif target in fullname_index or (target + ".md") in fullname_index:
                edges += 1
            else:
                broken.append({"from": r, "zone": note["zone"], "target": target})

    orphans = [
        {"path": r, "zone": n["zone"], "type": n["type"], "words": n["words"]}
        for r, n in registry.items()
        if n["inbound"] == 0 and n["zone"] in ("content", "root", "personal")
    ]

    # --- title collisions ---------------------------------------------
    dup_stems = {s: ps for s, ps in stem_index.items() if len(ps) > 1}
    norm_map: dict[str, list[str]] = {}
    for s in stem_index:
        norm_map.setdefault(normalize_title(s), []).append(s)
    exact_norm = {k: v for k, v in norm_map.items() if len(v) > 1}
    stems = list(stem_index)
    similar = []
    for i, a in enumerate(stems):
        na = normalize_title(a)
        for b in stems[i + 1 :]:
            nb = normalize_title(b)
            if not na or not nb or a == b:
                continue
            if abs(len(na) - len(nb)) > max(len(na), len(nb)) * 0.4:
                continue
            ratio = difflib.SequenceMatcher(None, na, nb).ratio()
            if ratio >= 0.82:
                similar.append({"a": a, "b": b, "ratio": round(ratio, 3)})

    # --- frontmatter compliance ---------------------------------------
    violations = []
    for r, n in registry.items():
        if n["zone"] in ("meta", "generated", "sources"):
            continue
        if r in ("CLAUDE.md", "README.md"):
            continue
        if not n["has_frontmatter"]:
            violations.append({"path": r, "field": "frontmatter", "value": "(missing)"})
            continue
        if n["status"] and n["status"] not in ALLOWED_STATUS:
            violations.append({"path": r, "field": "status", "value": n["status"]})
        if not n["status"]:
            violations.append({"path": r, "field": "status", "value": "(empty)"})
        if n["confidence"] and n["confidence"] not in ALLOWED_CONFIDENCE:
            violations.append({"path": r, "field": "confidence", "value": n["confidence"]})
        for f in ("created", "updated"):
            if n[f] and not ISO_DATE.match(str(n[f])):
                violations.append({"path": r, "field": f, "value": str(n[f])})

    # --- sources inventory ---------------------------------------------
    sources = []
    for p in other_files:
        r = rel(p)
        size = p.stat().st_size
        entry = {"path": r, "zone": zone_of(r), "ext": p.suffix.lower(), "bytes": size}
        if "_sources" in r.split("/") and size <= 50 * 1024 * 1024:
            entry["sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
        sources.append(entry)
    csv_rows = {}
    for p in sorted((VAULT / "97_CSV_SCHEMAS").glob("*.csv")):
        lines = [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]
        csv_rows[p.name] = max(0, len(lines) - 1)

    # --- sensitivity locations (path+line+category only) ---------------
    sensitivity = []
    for r, n in registry.items():
        if n["zone"] in ("personal", "meta", "sources"):
            continue
        text = (VAULT / r).read_text(encoding="utf-8")
        for i, line in enumerate(text.split("\n"), 1):
            for cat, pat in SENSITIVITY_PATTERNS:
                if pat.search(line):
                    sensitivity.append({"path": r, "line": i, "category": cat, "zone": n["zone"]})
    personal_files = [r for r in registry if registry[r]["zone"] == "personal"]

    # --- summary --------------------------------------------------------
    try:
        head = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"], cwd=VAULT, capture_output=True, text=True
        ).stdout.strip()
    except Exception:
        head = "(unknown)"
    hubs = sorted(registry.values(), key=lambda n: -n["inbound"])[:10]
    sens_by_cat: dict[str, int] = {}
    for s in sensitivity:
        sens_by_cat[s["category"]] = sens_by_cat.get(s["category"], 0) + 1
    summary = {
        "generated": date.today().isoformat(),
        "head": head,
        "md_files": len(md_files),
        "other_files": len(other_files),
        "zones": {z: sum(1 for n in registry.values() if n["zone"] == z) for z in
                  ("content", "root", "personal", "system", "meta", "generated", "sources")},
        "link_edges": edges,
        "broken_targets": len(broken),
        "path_style_links": len(path_style),
        "orphans": len(orphans),
        "duplicate_stems": len(dup_stems),
        "exact_normalized_collisions": len(exact_norm),
        "similar_title_pairs": len(similar),
        "frontmatter_violations": len(violations),
        "csv_rows": csv_rows,
        "sources_hashed": sum(1 for s in sources if "sha256" in s),
        "sensitivity_by_category": sens_by_cat,
        "personal_files_inventoried_not_scanned": len(personal_files),
        "top_hubs": [{"path": h["path"], "inbound": h["inbound"]} for h in hubs],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dumps = {
        "note_registry.json": list(registry.values()),
        "link_graph.json": {"broken": broken, "orphans": orphans,
                            "path_style_links": path_style},
        "title_collisions.json": {"duplicate_stems": dup_stems,
                                  "exact_normalized": exact_norm, "similar": similar},
        "frontmatter_violations.json": violations,
        "sources_inventory.json": {"files": sources, "csv_rows": csv_rows,
                                   "personal_files": personal_files},
        "sensitivity_locations.json": sensitivity,
        "summary.json": summary,
    }
    for name, data in dumps.items():
        (OUT_DIR / name).write_text(
            json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8"
        )

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
