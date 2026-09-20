# Design proposal: the Python developer agent

Status: draft for grilling. Nothing here is decided until you say so.

Built from [matt-pocock-skills.md](../research/matt-pocock-skills.md) and [python-craft-and-llm-faults.md](../research/python-craft-and-llm-faults.md), and your answers on 2026-09-20.

## 1. What it is, in one paragraph

A Claude Code agent (a `CLAUDE.md` persona plus a small set of skills in this repo) that behaves like a senior Python engineer pairing with you. It runs Matt Pocock's workflow verbatim through his plugin, uses Google's own ADK skills for framework knowledge, and adds one layer they both lack: Python craft and the deterministic checks that stop LLM faults at the commit. It has two modes chosen at intake, **guide** (you are vibe coding; it explains, recommends, and asks before anything hard to reverse) and **partner** (you are a pro; it moves faster and argues). Both modes produce a repo a human could pick up cold: same layout, same checks, same glossary, same ADRs.

## 2. The three sources and the seam between them

| Layer | Who maintains it | What it owns | How we get it |
|---|---|---|---|
| **Process** | Matt Pocock | grill → spec → tickets → implement → review; domain modelling; diagnosing bugs; architecture surveys; writing-for-agents | `claude plugins install mattpocock-skills`. Never fork. Auto-updates. |
| **Framework** | Google (adk-python repo) | building ADK agents, tools, workflows, HITL, eval, ADK style and review | Vendored copy of `adk-python/.agents/skills/` refreshed by a script; or a pointer that tells the agent to read them from the installed package source. Apache-2.0. |
| **Craft** | Us, in this repo | Python design rules, the repo baseline, the fault gates, intake, the two modes, the router | Written here, validated by this repo's CI, shipped as `python-dev` in this marketplace. |

The seam: our skills call his by name (`Call the Skill tool with "grilling"`), never copy his text. Where his skill has a TypeScript assumption (`setup-ts-deep-modules`, Effect, barrels) we write the Python counterpart and our router sends you to ours. Where a skill of his has a known hole (the `tdd` gap on glue code, `implement` never closing tickets, `code-review` sub-agents recursing), our wrapper carries the one-line fix in the invocation rather than editing his file, so updates never overwrite it.

**Licences.** His repo is MIT: copy, modify, redistribute freely; keep his copyright line in anything copied. Google's ADK skills are Apache-2.0: same freedoms, keep the notice and record changes. This repo's skills are Apache-2.0 already. All compatible.

## 3. The skills we write (first cut)

User-invoked unless marked.

| Skill | Job | Calls |
|---|---|---|
| `py-intake` | Run once per repo, or when re-entering after a long gap. Detects greenfield vs brownfield, git remote (GitHub / GitLab / none), existing tooling, ADK presence, `CONTEXT.md`/ADRs. Asks the mode question. Runs `setup-matt-pocock-skills` with the tracker answer pre-filled. Installs or verifies the baseline (section 4). Writes `docs/agents/mode.md` and the `## Agent skills` block. For brownfield: produces a one-page **orientation** (what the repo does, its seams, its hot spots from git log, the top three smells) and offers `improve-codebase-architecture` next. | `setup-matt-pocock-skills`, `domain-modeling`, `codebase-design` |
| `py-baseline` (model-invoked) | The reference for section 4: layout, pyproject, ruff/mypy/import-linter/pytest config, pre-commit hooks including the file-size, no-assert-less-test, and prompt-in-comment gates. Idempotent; merges into existing config, never overwrites. | none |
| `py-design` (model-invoked) | The Python craft reference: when a class earns its keep, Protocols at seams, composition over inheritance, parse-at-the-edge, exceptions as interface, one composition root, the adapter → normalised model → writer shape, the fault catalogue. Consulted by grilling, implement, and review. | `codebase-design` for vocabulary |
| `py-implement` | Thin wrapper over his `implement`: adds "search `CONTEXT.md` terms before writing a new function", "tests are read-only during red→green", "run ruff/mypy/single test file after every slice", "close or update the ticket", "commit with the decision in the message". | `implement`, `tdd`, `py-design` |
| `py-review` | His two-axis `code-review` plus a third axis, **Craft**, that runs the fault catalogue as labelled judgement calls and cites `py-design`. Guard line against sub-agent recursion. Report first; fix on request (ADK posture). In guide mode, each finding carries a one-sentence "why this matters". | `code-review`, `py-design` |
| `py-test-audit` | Point it at a test directory: classifies every test as behavioural / tautological / instruction-shaped / mock-only / trivial, and proposes deletions and rewrites at the right seam. The direct answer to "my tests aren't real tests". | `tdd`, `py-design` |
| `adk-build` | Router into Google's ADK skills with our baseline applied: agent package layout, prompts in a file, tools as typed functions, unit tests with a faked model, evals as a separate tier. | vendored `adk-agent-builder`, `adk-style`, `py-baseline` |
| `ask-dev` | The router, like `ask-matt` but aware of all three layers and of your mode. In guide mode it also explains *why* the recommended next step is next. Answers "what do I type now?" | reads `ask-matt` |

Not written, because his are used as-is: `grill-with-docs`, `to-spec`, `to-tickets`, `wayfinder`, `diagnosing-bugs`, `prototype`, `research`, `handoff`, `wait-what`, `improve-codebase-architecture`, `domain-modeling`, `codebase-design`, `writing-for-agents`, `triage`, `resolving-merge-conflicts`, `wizard`.

## 4. The baseline `py-intake` guarantees

See research §3 for the full list. Non-negotiables: `uv` + committed lock; `ruff` with the fault-catalogue rule set; strict type checking; `pytest` with the assertion gate; `import-linter` layers contract; `pre-commit`; one CI workflow; `pydantic-settings`; `.env.example`; `CONTEXT.md`; `docs/adr/`; a `CLAUDE.md` that is pointers only. On brownfield repos the baseline is proposed as tickets, applied one at a time, each green before the next, because turning on strict mypy over 10k lines in one commit is the horizontal slice Matt warns about.

## 5. The two modes

| | Guide (vibe coder) | Partner (pro) |
|---|---|---|
| Grilling | Same rounds, but each question carries a plain-English "what this decides" line and the recommendation is chosen for safety. | His format unchanged. |
| Decisions | Anything hard to reverse (schema, public interface, dependency, deletion) stops and asks, with the one-way/two-way door named. | Asks only where the spec is silent. |
| Explanations | Every review finding and every ADR offer explains why in one sentence. | Terse. |
| AFK | Allowed only for tickets labelled by a grilled spec; the run ends in a PR with before/after evidence, never a merge. | Same rule; the user may widen it in `docs/agents/mode.md`. |
| Vocabulary | `wait-what` is suggested proactively when jargon density rises. | Never. |

Mode is a line in `docs/agents/mode.md`, set at intake, changeable any time. It is prose the skills read, not a config schema; Matt's "config is death" applies.

## 6. Issue tracker

GitHub Issues is free on all plans. Still, the default is **local markdown** under `.scratch/`, because it works with no account, no network, and no public planning noise. Matt's `setup-matt-pocock-skills` already supports GitHub, GitLab, and local, and the ticket format is the same on all three. We add one thing: `py-intake` offers a **migration** ("push these local tickets to the remote tracker") that reads `.scratch/<feature>/issues/*.md` and creates issues with the blocking edges, so starting local costs nothing later. Intake detects the remote from `git remote -v` and proposes accordingly.

## 7. How a session looks

**Greenfield, guide mode.** `/py-intake` → mode question, tracker (local), baseline installed, empty `CONTEXT.md` → `/grill-with-docs` on the idea (the agent proposes the adapter → model → writer shape from `py-design` when it fits) → `/to-spec` → `/to-tickets` → `/py-implement` per ticket in a fresh window → `/py-review` → you read the PR evidence.

**Brownfield, a 10k-line file.** `/py-intake` → orientation page → `/improve-codebase-architecture` finds the seams → grill one candidate → `/to-spec` (a refactor spec leaning on implementation decisions, not user stories) → `/to-tickets` as expand→migrate→contract → implement per ticket, each green → `/py-test-audit` on the old tests.

**Bug.** `/diagnosing-bugs` unchanged; `py-review` afterwards.

## 8. Decisions taken on 2026-09-20

| Question | Decision |
|---|---|
| Where the agent lives | This repo, shipped as a second plugin (`python-dev`) installed next to `mattpocock-skills`. (See §9 for what "plugin" means.) |
| Gate strictness on existing repos | Strict and blocking, on changed lines only, from day one. |
| Brownfield intake | Deep read of the repo, then an automatic grilling session about every decision the code makes that no `CONTEXT.md` or ADR explains. The agent acts as a senior engineer mentoring a junior: names the alternative, says why it may be better, and always pushes for the better design. |
| Deterministic bad-code detection | Ship a `py-health` suite (§10). Yes, this exists in the wild; it is several tools, not one. |
| Canonical example codebases | `psf/requests` for a deep module, `cosmicpython/code` for ports-and-adapters layering, `dlt-hub/dlt` for the data-engineering extract → normalise → load shape (§11). |
| ADK version | 2.x only for new code. A separate `adk-migrate` skill turns 1.x repos into 2.x, using Google's own migration notes. |

## 9. What "this repo as a plugin" means

Claude Code can load skills from a folder on your machine, or from a **plugin**. A plugin is just a Git repository with a small manifest file (`.claude-plugin/plugin.json`) that lists which skill folders it contains. When you run `claude plugins install <name>`, Claude Code downloads that repository, reads the manifest, and makes every listed skill available as a slash command. When the repository changes, the plugin updates itself.

This repository already has that manifest (`.claude-plugin/marketplace.json` and the skills under `skills/`). So "this repo as a plugin" means: we add the new Python skills as folders under `skills/`, add their names to the manifest, and you install this repository the same way you install Matt's. Two install commands, one machine, everything current. You never copy files by hand.

## 10. `py-health`: the deterministic bad-code suite

Nothing published does this as one tool, but the pieces are mature and each is a pass/fail command. `py-health` wires them together, runs them, and writes one report with a score per axis and the worst offenders by file. It is the numeric half of the brownfield orientation and the thing the mentor persona points at when it says "this file is the problem".

| Axis | Tool | What it catches |
|---|---|---|
| Lint, style, common bugs, security smells | `ruff` with the fault-catalogue rule set (`B`, `S`, `BLE`, `C90`, `PL`, `T20`, `ERA`, `D`, `PT`, `SIM`, `RET`, `ARG`) | Mutable defaults, blind excepts, prints, commented-out code, complexity, unused arguments, test smells. |
| Complexity and maintainability | `radon` (cyclomatic complexity, maintainability index) gated by `xenon` | The 10k-line file scores as F; functions over a threshold fail. |
| Dead code | `vulture` | Unused functions, classes, imports, variables. |
| Duplication | `pylint --disable=all --enable=duplicate-code` or `jscpd` | Near-duplicate blocks across files. |
| Security | `bandit` | Hard-coded secrets, injection, unsafe deserialisation. |
| Architecture | `import-linter` layers contract | Domain importing adapters, cycles, entrypoints bypassing the application layer. |
| Types | `mypy --strict` error count | `Any` leakage, untyped surfaces. |
| Test strength | `mutmut` (mutation testing) | The direct answer to fake tests: it edits the code (flips a `<` to `<=`, deletes a line) and re-runs the suite. A test that still passes never tested anything. Survivor rate is the score. |
| Test hygiene | custom gate | Tests with no assertion, assertion-free `pass` bodies, `skip` markers without a reason, prompt-shaped comments in test bodies. |
| Size | custom gate | Modules over N lines, functions over M lines, files named `utils`/`helpers`/`common`/`misc`. |

Mutation testing is slow, so it runs on demand and on a schedule, not on every commit. Everything else runs in pre-commit on changed files and in CI on the whole repo.

## 11. The canonical examples, and why these three

| Repo | Stars (order of magnitude) | What it demonstrates | Where it lives in `py-design` |
|---|---|---|---|
| `psf/requests` | ~50k, universally known | A **deep module**: eight public functions in `api.py` (`get`, `post`, ...) hiding ~6,000 lines of sessions, adapters, auth, cookies, retries. Callers learn one function; the implementation absorbs everything. Its `adapters.py` is also a textbook adapter seam (`HTTPAdapter` behind `BaseAdapter`). | The "what depth looks like" section. |
| `cosmicpython/code` | ~1k, but the reference implementation of the O'Reilly book *Architecture Patterns with Python* | **Ports and adapters** in plain Python: `domain/` (models, commands, events, imports nothing), `service_layer/` (handlers, unit of work, message bus), `adapters/` (repository, ORM, notifications, Redis), `entrypoints/` (Flask, Redis consumer), `bootstrap.py` as the one composition root, and tests split `unit/` `integration/` `e2e/`. This is exactly the layering the import-linter contract enforces. | The layout template and the layering rules. |
| `dlt-hub/dlt` | several thousand, production data-engineering library | The **extract → normalise → load** shape you described, at scale: `sources/` (one package per external system), `extract/` (resources, incremental state), `normalize/` (one place that turns raw items into a typed schema), `load/` and `destinations/` (one writer contract, many backends behind `common/destination/reference.py`). Adapter in, common shape in the middle, one writer out. | The worked example for data projects, and the counter-example for "each source has its own writer". |

The agent quotes these by path when it explains a recommendation, so a human can go and read the real thing.

## 12. Additional skills from these decisions

| Skill | Job |
|---|---|
| `py-health` | Run the suite in §10; write `docs/health/<date>.md`; feed the orientation and the mentor's first grilling round. |
| `py-orient` (part of `py-intake` on brownfield) | Read everything; produce the orientation page; list every undocumented decision found in the code; start a grilling round on them; record answers as `CONTEXT.md` terms and ADRs; propose the first three improvement tickets. |
| `adk-migrate` | Detect ADK 1.x patterns (`SequentialAgent`/`LoopAgent`/`ParallelAgent`, `_run_async_impl` overrides, direct `session.events.append`, broad `except` inside tools, rigid custom session tables) and rewrite them to 2.x (`Workflow` graphs, callbacks, yielded events, narrow excepts, schema update), as expand → migrate → contract tickets with the eval suite green at each step. |
