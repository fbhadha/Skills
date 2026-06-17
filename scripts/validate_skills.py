#!/usr/bin/env python3
"""Validate every skills/*/SKILL.md against the Agent Skills standard.

Checks, per skill:
  - SKILL.md exists and starts with YAML frontmatter
  - frontmatter parses and validates against schema/skill.schema.json
  - `name` matches the parent folder name exactly
  - `name` does not contain the reserved words 'anthropic' or 'claude'

Exit code is non-zero if any skill fails, so CI can block the merge.

Usage: python scripts/validate_skills.py [skills_dir]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

try:
    import jsonschema
except ImportError:
    sys.exit("jsonschema is required: pip install jsonschema")

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "skills"
SCHEMA_PATH = ROOT / "schema" / "skill.schema.json"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
RESERVED = ("anthropic", "claude")


def load_frontmatter(skill_md: Path):
    text = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("SKILL.md must begin with YAML frontmatter delimited by ---")
    return yaml.safe_load(match.group(1)) or {}


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft7Validator(schema)

    skill_dirs = sorted(p for p in SKILLS_DIR.glob("**/SKILL.md"))
    if not skill_dirs:
        print(f"No SKILL.md files found under {SKILLS_DIR}")
        return 0

    failures: list[str] = []
    for skill_md in skill_dirs:
        folder = skill_md.parent.name
        rel = skill_md.relative_to(ROOT)
        try:
            fm = load_frontmatter(skill_md)
        except ValueError as exc:
            failures.append(f"{rel}: {exc}")
            continue

        errors = [e.message for e in validator.iter_errors(fm)]
        name = fm.get("name", "")
        if name and name != folder:
            errors.append(f"name '{name}' must match folder name '{folder}'")
        if any(word in str(name).lower() for word in RESERVED):
            errors.append(f"name '{name}' must not contain 'anthropic' or 'claude'")

        if errors:
            failures.extend(f"{rel}: {e}" for e in errors)
        else:
            print(f"ok  {rel}")

    if failures:
        print("\nVALIDATION FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1

    print(f"\nAll {len(skill_dirs)} skill(s) valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
