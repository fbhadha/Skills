---
name: py-baseline
description: The baseline every Python repo gets. Use when setting up or checking a Python repo's layout, tooling, checks, CI, and agent docs (pyproject tool tables, ruff, mypy, import-linter, pytest, pre-commit, Repowise, the CI change gate, AGENTS.md, CONTEXT.md, ADRs, how-tos, mode). Idempotent; merges into what exists and never overwrites.
license: Apache-2.0
metadata:
  author: fbhadha
  version: 0.1.0
  tags: [python, tooling, ci, pre-commit, setup]
---

# Python baseline

The skeleton every repo this agent touches ends up with, so a junior reader can pick up any of them the same way. `py-intake` applies it; anything else consults it.

## Files

| File | Purpose | Template |
|---|---|---|
| `pyproject.toml` `[tool.*]` tables | ruff, ruff-format, mypy strict, import-linter layers, pytest, coverage | `templates/pyproject-tools.toml` |
| `uv.lock`, `.python-version` | committed; CI installs with `uv sync --frozen` | created by `uv` |
| `.pre-commit-config.yaml` | ruff, ruff-format, mypy on changed files, import-linter, pylint too-many-lines, detect-secrets | `templates/pre-commit-config.yaml` |
| `.github/workflows/ci.yml` (or the GitLab equivalent) | pre-commit on the files the PR changed, the whole test suite, then the Repowise change gate | `templates/ci.yml`, `templates/gitlab-ci.yml` |
| `scripts/repowise_gate.py` | the CI change gate over Repowise's Python API | `templates/repowise_gate.py` |
| `.repowise/decisions.yaml` | Repowise decision records, tracked; the rest of `.repowise/` is gitignored | created by `repowise decision export` |
| `.env.example` | every key the code reads, with a comment, no values | `templates/env.example` |
| `AGENTS.md` | pointers only, under 40 lines; every harness reads it | `templates/AGENTS.md` |
| `CLAUDE.md` | one line: `@AGENTS.md` | `templates/CLAUDE.md` |
| `CONTEXT.md` | the glossary, Matt Pocock's format, created lazily | `templates/CONTEXT.md` |
| `docs/adr/` | decisions that pass the three gates, one to three sentences each | `templates/adr-template.md` |
| `docs/agents/mode.md` | the mode line the skills read | `templates/mode.md` |
| `docs/howto/add-a-<shape>.md` | one per shape, mirrors an `example/` that compiles | `templates/howto-template.md` |
| `docs/architecture.md` | the layers and what talks to what, kept consistent with the import-linter contract | `templates/architecture.md` |
| `README.md` | run, test, where to start reading; commands in ```bash ci``` blocks are executed in CI | `templates/README-skeleton.md` |

## The gates

Two layers. Line-level tools run at commit on the changed files. Repowise (`docs/research/repowise.md` in this repo) runs whole-repo in `py-health` and once per CI pipeline as the change gate. Custom code: one script, the change gate, because Repowise's CLI cannot do it and its Python API can.

| Fault | Tool | Where it runs |
|---|---|---|
| Module over 400 lines (tests 150) | `pylint --disable=all --enable=too-many-lines --max-module-lines=400` | commit |
| `utils`, `helpers`, `common`, `misc` modules | ruff `TID251` banned imports plus an import-linter `forbidden` contract | commit |
| Prompt-shaped docstrings and comments | ruff `D401` (non-imperative docstring), `TD002`/`TD003` (a TODO must name an author and an issue), `FIX002` (no TODO left in code), `ERA001` (commented-out code) | commit |
| Swallowed exceptions, mutable defaults, prints, string SQL, secrets | ruff `BLE`, `B`, `T20`, `S`; `detect-secrets` | commit |
| Complexity, flags, too many parameters | ruff `C901`, `PLR091x`, `FBT` | commit |
| Layering | `import-linter` layers contract | commit |
| Types | `mypy --strict` on `src/` | commit |
| A change made a touched file worse (new nesting, god class, I/O in a loop, duplication, swallowed exception) | `scripts/repowise_gate.py`: `ChangeReviewService.review()` on `origin/main..HEAD`, fails when `introduced_total > 0` | CI |
| Health score, ranking, what to refactor first | `repowise health`, `--refactoring-targets`, `--trend`; score ratcheted in `docs/health/` | health |
| Duplication | `repowise health` (`dry_violation`) | health |
| Dead code | `repowise dead-code --safe-only` fails on unreachable files; unused exports are listed, never fail | health |
| Test with no assertion, mock-saturated test | `repowise health --format json`, advisory dimension (`assertion_free_test`, `mock_saturated_test`); listed in the health report | health; review |
| Security | `bandit` (Repowise's 16-pattern scan is a floor, not a scanner) | health |
| Fake tests (pass on any mutation) | `mutmut`, score ratcheted in `docs/health/` | health |
| Weakened test (assertion loosened, test deleted, skip added) | mutation-score ratchet, `py-review` in a fresh context, and a `CODEOWNERS` line on `tests/` requiring the owner's approval | health; review; platform |

Repowise rules: every scripted call is `DO_NOT_TRACK=1 repowise <cmd> --no-editor-setup` where the flag exists; `.repowise/` is gitignored except `decisions.yaml`; the index is rebuilt in CI with `repowise init --no-prose --no-editor-setup -y` (under ten seconds on the repos tried). The editor wiring (`.mcp.json`, hooks in `~/.claude/settings.json`) is offered to the user as a separate step, never done by a skill.

## Decisions baked into the templates

- **Docstrings are not required** (`D1xx` ignored). Requiring them produces the signature-restating docstrings the prompt-comment gate exists to catch. When a docstring is present it must follow the Google convention.
- **Tests are exempt** from `S101` (assert), `PLR2004` (magic values), `D`, `ARG` (fixtures), `FBT`.
- **Strict from day one, changed lines only.** Pre-commit runs on staged files; CI runs pre-commit with `--from-ref origin/main --to-ref HEAD`, so old mess is tolerated and no new mess gets in. Whole-repo numbers come from `py-health`, not from the commit gate.
- **`filterwarnings = ["error"]`** in pytest. A deprecation is a failing test, so it gets fixed while it is one line.
- **mypy strict on `src/`, not on `tests/`.** With the Pydantic plugin when Pydantic is a dependency.
- **`uv run` for everything.** No activated virtualenvs in docs or scripts.
- **Repowise is a dev dependency, never a runtime one.** It is AGPL-3.0; the gate script imports it in CI and nowhere else. `DO_NOT_TRACK=1` is set in CI and listed in `.env.example`.

## Applying it (rules for `py-intake`)

1. Never overwrite. Merge missing keys into existing tables; leave existing values; report every difference as a proposed change and let the user accept or decline each.
2. Fill placeholders (`{{PACKAGE}}`, `{{PYDEV_REV}}`, `{{PYTHON}}`) from the repo, never by guessing.
3. Brownfield: propose the baseline as tickets, one file group at a time, each green before the next.
4. Prove each gate bites before finishing: make a violation on a scratch file, watch the gate fail, revert, watch it pass.
