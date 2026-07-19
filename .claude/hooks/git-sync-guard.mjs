#!/usr/bin/env node
/**
 * git-sync-guard — keeps the generated docs/ suite living (see .claude/skills/repo-analysis/SKILL.md).
 *
 * Wired in .claude/settings.json:
 *   PreToolUse(Bash)  -> `node .claude/hooks/git-sync-guard.mjs pre`
 *     Blocks a `git push` whose outgoing commits change vault notes but do not
 *     include a regenerated docs/REPO_ANALYSIS.md. Exit 2 = block, stderr -> Claude.
 *   PostToolUse(Bash) -> `node .claude/hooks/git-sync-guard.mjs post`
 *     After a `git pull` that brought note changes, nudges Claude to run /repo-analysis.
 *
 * Fail-open by design: any internal error exits 0 so git work is never wedged.
 * Bypass: SKIP_REPO_ANALYSIS_GUARD=1
 */
import { execSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const REPO_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..");
// The full generated suite — every analysis-bearing push must refresh all of it.
// (Checking only REPO_ANALYSIS.md let the companions go stale: baseline 2026-07-19 §13.)
const SUITE = [
  "docs/REPO_ANALYSIS.md",
  "docs/WORKFLOW_TREE.md",
  "docs/FAMILY_TREE.md",
  "docs/RELATIONSHIP_TREES.md",
  "docs/VISION.md",
];
// Meta paths whose changes alone do not make the analysis stale.
const EXEMPT = [/^docs\//, /^README\.md$/, /^\.obsidian\//, /^\.claude\//, /^\.githooks\//];

function git(args) {
  return execSync(`git ${args}`, { cwd: REPO_ROOT, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] }).trim();
}

function contentNotes(paths) {
  return paths.filter((p) => p.endsWith(".md") && !EXEMPT.some((re) => re.test(p)));
}

function main() {
  const mode = process.argv[2];
  if (process.env.SKIP_REPO_ANALYSIS_GUARD === "1") return 0;

  let input;
  try {
    input = JSON.parse(readFileSync(0, "utf8"));
  } catch {
    return 0;
  }
  if (input.tool_name !== "Bash") return 0;
  const command = String(input.tool_input?.command ?? "");

  if (mode === "pre" && /\bgit\b[^\n]*?\bpush\b/.test(command) && !/--dry-run/.test(command)) {
    let changed;
    try {
      const upstream = git("rev-parse --abbrev-ref --symbolic-full-name @{u}");
      changed = git(`diff --name-only ${upstream}..HEAD`).split("\n").filter(Boolean);
    } catch {
      return 0; // no upstream / detached — nothing to judge, fail open
    }
    const stale = contentNotes(changed);
    const missing = SUITE.filter((f) => !changed.includes(f));
    if (stale.length > 0 && missing.length > 0) {
      console.error(
        `[repo-analysis guard] Push blocked: the outgoing commits change ${stale.length} vault note(s) ` +
          `but the generated suite was not fully refreshed (missing: ${missing.join(", ")}).\n` +
          `Run the /repo-analysis skill (delta) — it refreshes every suite file's header each run — ` +
          `commit the refreshed suite, then push.\n` +
          `Changed notes include: ${stale.slice(0, 5).join(", ")}${stale.length > 5 ? ", …" : ""}\n` +
          `Emergency bypass: SKIP_REPO_ANALYSIS_GUARD=1 git push`
      );
      return 2;
    }
    return 0;
  }

  if (mode === "post" && /\bgit\b[^\n]*?\bpull\b/.test(command)) {
    const responseText = JSON.stringify(input.tool_response ?? "");
    if (/Already up to date/i.test(responseText)) return 0;
    let changed;
    try {
      changed = git("diff --name-only ORIG_HEAD..HEAD").split("\n").filter(Boolean);
    } catch {
      return 0;
    }
    const notes = contentNotes(changed);
    if (notes.length > 0 && SUITE.some((f) => !changed.includes(f))) {
      console.error(
        `[repo-analysis guard] The pull brought ${notes.length} changed vault note(s) — ` +
          `run the /repo-analysis skill (delta) to refresh the docs/ suite before further work.`
      );
      return 2; // PostToolUse: non-blocking, stderr is surfaced to Claude
    }
    return 0;
  }

  return 0;
}

try {
  process.exit(main());
} catch {
  process.exit(0);
}
