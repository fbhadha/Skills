# python-dev

A senior Python engineer as a selectable agent. It builds by your repo's own how-tos, explains every step in plain words, pushes back on scope creep, and keeps deterministic checks green. Process comes from Matt Pocock's skills (called by name, never copied), framework knowledge from Google's ADK skills, craft and checks from here.

Design and evidence: `docs/design/python-dev-agent.md` and `docs/research/` in this repository.

## Install

Prerequisites in every harness: `uv`, Python 3.11 or newer, Matt Pocock's skills, and Repowise (`pip install repowise` or `uv tool install repowise`, plus its agent plugin: `/plugin marketplace add repowise-dev/repowise` then `/plugin install repowise@repowise` on Claude Code; `repowise agents add --target=codex` or `--target=vscode` elsewhere). Repowise is the agent's only store for everything derived from the code (ADR 0005 in this repo).

| Harness | Install | Select the persona |
|---|---|---|
| Claude Code | `/plugin marketplace add fbhadha/Skills` then `/plugin install python-dev@community-skills`; also `/plugin install mattpocock-skills@mattpocock` (his marketplace) | `claude --agent python-dev`, or set `"agent": "python-dev"` in the repo's `.claude/settings.json` (py-intake offers to) |
| GitHub Copilot | `npx skills@latest add fbhadha/Skills --all` and `npx skills@latest add mattpocock/skills --all` | py-intake writes `.github/agents/python-dev.agent.md`; pick it from the agent picker |
| OpenAI Codex | same two `npx skills` commands | no persona picker; py-intake writes the persona into `AGENTS.md`, skills are `$py-intake`, `$ask-dev` |

Then, in the target repo, run `py-intake` once. It applies the baseline (`skills/py-baseline`), sets up the tracker, writes the three human docs, and on an existing repo orients itself and grills you about the undocumented decisions.

## What is in the box

| Path | What |
|---|---|
| `agents/python-dev.md` | the persona: identity, guide voice, two-tier pushback, the ask-first and never lists |
| `agents/py-reviewer.md` | read-only craft reviewer used by `py-review` |
| `skills/ask-dev` | which command comes next, from the repo's state |
| `skills/py-design` | the craft rules, the fault catalogue, three canonical repos to cite |
| `skills/py-baseline` | the layout, tool tables, commit gate, CI, docs every repo gets, plus templates |
| `hooks/hooks.json` | in-session guards (below) |
| `scripts/hooks/` | the hook scripts |

Coming in the next releases (see design §15): `py-intake`, `py-implement`, `py-review`, `py-test-audit`, `py-health`, `adk-build`, `adk-migrate`, and the `adk-skills` plugin.

## Hooks (Claude Code)

Best effort. Pre-commit and CI in the target repo are the enforcement; the hooks just shorten the loop.

| Event | Script | Does |
|---|---|---|
| `PreToolUse` on Bash | `guard_command.py` | denies force-push, hard reset, rebase, amend, filter-branch, `--no-verify`, `branch -D`. Fails open on any parse error. |
| `Stop` | `stop_gate.py` | blocks the turn ending while `ruff check` is red on the `.py` files changed this session. Only in repos with the baseline; never blocks twice in a row. |

Copilot and Codex get the same guards as repo-level hook files written by `py-intake`; Copilot's hooks fail open on timeout, Codex's hook contract is unverified, so treat both as advisory.

## Checks the baseline installs in a target repo

One read path and one write path per kind of knowledge. Everything derived from the code (structure, callers, blast radius, why, health, dead code, change risk, doc drift) is read from Repowise through its six skills. Humans and the agent write only ADRs, `CONTEXT.md`, how-tos and tool tables; `scripts/adr_sync.py` binds each ADR to the paths it governs so Repowise warns whoever edits them.

Line-level at commit: ruff (bugbear, blind except, security, print, commented-out code, prompt-shaped TODOs and docstrings, complexity, boolean flags, banned grab-bag modules), mypy strict on `src/`, import-linter layers, pylint module length, detect-secrets. Whole-repo and per-change: [Repowise](https://github.com/repowise-dev/repowise) health score, duplication, dead code, assertion-free tests, and a CI gate that fails when a diff makes a touched file worse. On demand: mutmut, bandit. Why this split: `docs/research/repowise.md`.

Repowise is AGPL-3.0 and is used as a development tool only. Set `DO_NOT_TRACK=1` (the templates do) to switch off its telemetry.

## Licence

Apache-2.0. See `NOTICE` for what is called or vendored from elsewhere.
