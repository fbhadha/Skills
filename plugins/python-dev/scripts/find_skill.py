#!/usr/bin/env python3
"""Print the path of an installed skill's SKILL.md, by name.

The Skill tool refuses skills marked `disable-model-invocation: true`, and Codex
and Copilot have no Skill tool at all. Reading the file is refused nowhere, so
the persona locates the file with this script, reads it, and follows it. The
door check uses it too: a skill is installed when this finds it.

Usage:
    python3 find_skill.py grill-with-docs
    python3 find_skill.py grilling tdd code-review      # one path per line

Exit codes: 0 every name was found; 1 at least one was not (the missing names
and the directories searched go to stderr).

Search order, first hit wins: Claude Code's installed plugin cache (the version
marked in use), then project and user skill directories for Claude Code, the
Agent Skills standard, Copilot and Codex, then Claude Code's marketplace clones.
A match is a directory named <name>, or any SKILL.md whose frontmatter `name:`
is <name> (some skills live in a directory named differently).
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

HOME = Path.home()
CWD = Path.cwd()
ROOTS: list[Path] = [
    HOME / ".claude" / "plugins" / "cache",
    CWD / ".claude" / "skills",
    HOME / ".claude" / "skills",
    CWD / ".agents" / "skills",
    HOME / ".agents" / "skills",
    CWD / ".github" / "skills",
    HOME / ".copilot" / "skills",
    CWD / ".codex" / "skills",
    HOME / ".codex" / "skills",
    HOME / ".claude" / "plugins" / "marketplaces",
]
NAME_RE = re.compile(r"^name:\s*['\"]?([^'\"\n]+)", re.MULTILINE)
SKIP_DIRS = {"node_modules", ".git"}


def frontmatter_name(skill_md: Path) -> str:
    try:
        head = skill_md.read_text(encoding="utf-8", errors="replace")[:2000]
    except OSError:
        return ""
    if not head.startswith("---"):
        return ""
    m = NAME_RE.search(head.split("\n---", 1)[0])
    return m.group(1).strip() if m else ""


def in_use_rank(path: Path) -> int:
    """0 when the containing plugin version is the one Claude Code marks in use, else 1."""
    for parent in path.parents:
        if (parent / ".in_use").exists():
            return 0
        if parent.name == "cache":
            break
    return 1


def candidates(root: Path) -> list[Path]:
    if not root.is_dir():
        return []
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        if "SKILL.md" in filenames:
            found.append(Path(dirpath) / "SKILL.md")
    return found


def find(name: str) -> Path | None:
    for root in ROOTS:
        hits = [p for p in candidates(root) if p.parent.name == name or frontmatter_name(p) == name]
        if hits:
            hits.sort(key=lambda p: (in_use_rank(p), str(p)))
            return hits[0]
    return None


def main(names: list[str]) -> int:
    if not names:
        print(__doc__, file=sys.stderr)
        return 1
    missing: list[str] = []
    for name in names:
        path = find(name)
        if path is None:
            missing.append(name)
            continue
        print(path)
    if missing:
        print(f"not found: {', '.join(missing)}", file=sys.stderr)
        print("searched: " + ", ".join(str(r) for r in ROOTS), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
