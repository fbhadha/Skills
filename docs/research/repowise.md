# Repowise: what it is and which checks it owns

Verified 2026-09-20 against `repowise` 0.52.0 from PyPI, installed in a scratch venv and run on `psf/requests` and on a scratch repo seeded with the faults in `plugins/python-dev/skills/py-design/references/fault-catalogue.md`. Source read from `github.com/repowise-dev/repowise` (main).

## What it is

A local codebase-intelligence engine. `repowise init` parses the repo with tree-sitter, builds a dependency graph, indexes git history, and scores every file 1 to 10 from 49 deterministic markers. It then exposes all of that to an agent through an MCP server and to a human through a CLI and a dashboard. Everything in the analysis layers runs with no model and no network; a model is only used if you ask it to write wiki prose.

| Fact | Value |
|---|---|
| Licence | AGPL-3.0, commercial licence sold for embedding. Internal use by a team is free and unencumbered. |
| Python | 3.11 or newer |
| Index time | 9.8 s on `requests` (140 files, 500 commits); 3.7 s on a 5-file repo |
| Languages | Python is full tier (graph, health, dead code, assertion detection all implemented) |
| Harness tiers | Claude Code and Codex: full (MCP, hooks, skills). VS Code / Copilot: MCP only. Our skills call the CLI, so the three harnesses get the same checks. |
| Telemetry | On by default. `DO_NOT_TRACK=1` or `REPOWISE_TELEMETRY_DISABLED=1` turns it off. A history security scan also tried to reach `api.repowise.dev`; CI must not depend on that call succeeding. |
| Writes outside `.repowise/` | By default `init` writes `.mcp.json`, `.vscode/mcp.json`, `.claude/CLAUDE.md`, a post-commit hook, and edits `~/.claude/settings.json`. `--no-editor-setup` confines it to `.repowise/`. |

## What fired on the seeded faults

| Fault planted | Repowise | Established tool |
|---|---|---|
| 60 near-identical functions in one 842-line `utils.py` | `dry_violation` (100% duplicated) | pylint `duplicate-code` |
| 7-deep nesting | `nested_complexity` critical, per function | ruff `C901`, `PLR1702` |
| `except Exception: pass` | `error_handling`, one finding per occurrence | ruff `BLE001`, `S110` |
| Class with 7 methods sharing no state | `low_cohesion` (LCOM4=6) | nothing established |
| `db.execute` inside a `for` | `io_in_loop` (N+1), also across function boundaries | nothing established |
| Test that asserts nothing | `assertion_free_test` (advisory, zero score impact, must be asked for) | nothing established |
| `assert True` | not caught | not caught |
| Orphan module nothing imports | `unreachable_file` | vulture |
| Public function nothing imports | `unused_export` (noisy: every public function in a library-style package) | vulture |
| `PASSWORD = "hunter2"`, f-string SQL | security scan (16 regex patterns; its own doc says run a real SAST) | bandit, detect-secrets |
| Module over 400 lines | no marker for file length | pylint `too-many-lines` |
| `# TODO: implement`, "This function" docstrings, `# Make sure to` | not caught | ruff `TD002`, `FIX002`, `D401`, `ERA001` |
| Mutable default, `print` | not caught | ruff `B006`, `T201` |
| Boolean flag parameter | `primitive_obsession` fires on some | ruff `FBT` |

Change-level: after adding a 5-deep function to a clean file, the Python API `ChangeReviewService.review()` returned `status: review_required`, `introduced_total: 1`, naming the function and lines. The `repowise risk` CLI does **not** carry that health delta; only the API and the `get_change_risk` MCP tool do. `repowise health` has no threshold flag and always exits 0. The only Repowise command that exits non-zero on findings is `repowise workspace check` (multi-repo architecture rules).

## The split

Repowise owns what needs the whole graph or git history. Per-line linters own the commit gate, because they are line-precise, run in milliseconds on staged files, and every Python developer already knows their output.

| Repowise owns | Why |
|---|---|
| The repo health score, ranking, and `--refactoring-targets` (`py-health`) | Calibrated against a defect corpus; replaces radon/xenon and the ad hoc "score per axis" idea. |
| Duplication and dead code | Replaces pylint `duplicate-code` and vulture. Gate only on `--safe-only` unreachable files; unused exports are review input, never a failure. |
| Assertion-free tests | Resolves the open Q18: no custom gate. Read via `repowise health --format json` and the `advisory` dimension. |
| The change gate in CI: "this diff introduced no new health finding on the files it touched" | A 40-line script over `ChangeReviewService`; the CLI cannot do it. |
| Brownfield orientation (`py-intake`, `py-orient`) | `init --no-prose`, `context`, `why`, `risk -t`, `dead-code`, the structural wiki, and the "does the score find the bugs?" callout as evidence for the user. |
| Decision records | `repowise decision` stores accepted decisions in `.repowise/decisions.yaml` (tracked) and links them to graph nodes; our ADRs stay the human-readable form and intake imports one into the other. |

| Stays with established tools | Why |
|---|---|
| ruff (`B`, `BLE`, `S`, `T20`, `D401`, `TD`, `FIX`, `ERA`, `C901`, `PLR`, `FBT`, `TID251`) | Line-level, instant, autofixable; Repowise has no equivalent for prompt-shaped comments, prints, or mutable defaults. |
| pylint `too-many-lines` | Repowise has no file-length marker. |
| mypy strict | No overlap. |
| import-linter | Per-commit layering on one repo; Repowise's `workspace check` is for multi-repo conformance. |
| bandit, detect-secrets | Repowise's security layer is a 16-pattern floor and says so. |
| mutmut | Mutation testing is the only thing that catches a test that asserts the wrong thing. |

## Constraints for `py-baseline`

- `.repowise/` is gitignored except `decisions.yaml`. Each developer and CI indexes locally.
- CI runs `DO_NOT_TRACK=1 repowise init --no-prose --no-editor-setup -y` then the gate script. Index time is under the test suite's on every repo tried.
- The gate script imports `repowise.core`, which is AGPL. It is a development script in the target repo, run in CI, never shipped inside a product. If the user's repo is itself distributed as a product, swap the script for the CLI's `risk` percentile and lose the health delta; record that in an ADR.
- Never `repowise init` with editor setup from a skill: it edits `~/.claude/settings.json` and repoints its single MCP entry at whichever repo ran last. Offer it as a separate, explicit step.
