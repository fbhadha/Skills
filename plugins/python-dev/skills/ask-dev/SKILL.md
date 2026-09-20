---
name: ask-dev
description: Route the user to the next command. Use when the user asks what to do next, what to type, which skill fits, how to start on a repo, or when a session begins with python-dev as the agent. Reads the repo's mode, glossary, tracker and health, checks the upstream skills are installed, and recommends one next step with the reason. Recommends and stops; never starts the work.
license: Apache-2.0
metadata:
  author: fbhadha
  version: 0.1.0
  tags: [python, router, workflow]
---

# Ask dev

You don't remember every skill, so ask. This is the router over four layers: Matt Pocock's process skills, Repowise's codebase-intelligence skills, Google's ADK skills, and this plugin's craft skills. It answers one question, "what do I type now?", and stops.

## 1. Read the state

- `docs/agents/mode.md`. Missing means the repo is not set up: the answer is `py-intake`, nothing else.
- `CONTEXT.md`, `docs/agents/issue-tracker.md`, the Repowise section of `AGENTS.md` (health line, last-indexed commit), the `docs/howto/` listing, and any open ticket the user names.
- The door check: confirm Matt Pocock's `grilling`, `domain-modeling`, `tdd`, `code-review`, `codebase-design`, `diagnosing-bugs`, `prototype`, `research` and Repowise's `codebase-exploration`, `pre-modification-check`, `architectural-decisions`, `code-health`, `change-review`, `dead-code-cleanup` are installed under those names. Report any that are missing and how to install them (`mattpocock-skills` and `repowise` plugins on Claude Code; `npx skills@latest add mattpocock/skills` and `repowise agents add` elsewhere). Do not improvise a missing skill's behaviour.

## 2. Place the user on a flow

| The situation | Type this | Then |
|---|---|---|
| Repo not set up (no `docs/agents/mode.md`) | `py-intake` | It asks the mode question, detects the tracker, installs the baseline, writes the docs. |
| An idea or feature, in a repo | `grill-with-docs` (Matt's) | Small enough for one session: `py-implement`. Bigger: `to-spec`, then `to-tickets`, then `py-implement` per ticket in a fresh window, then `py-review`. |
| A ticket already exists | `py-implement <ticket>` | It names the shape, checks scope, builds test-first, runs `py-review`, commits. |
| A branch to review | `py-review <fixed-point>` | Standards, Spec and Craft axes, report first, fixes on request. |
| Something is broken | describe the bug; the agent reaches for `diagnosing-bugs` | It builds a red-capable loop before any theory. |
| Tests you don't trust | `py-test-audit tests/` | Classifies every test; proposes deletions and rewrites at the right seam. |
| "Where is this repo ugly?" | `py-health` | Repowise health, dead code, doc drift and the mutation score in one report, then `improve-codebase-architecture` (Matt's) on the worst file. |
| "Why is this built this way?" | describe the file; the agent reaches for `architectural-decisions` (Repowise) | ADRs, `# WHY:` comments and commit archaeology for that path. |
| A decision was just made in conversation | write the ADR from `docs/adr/` template, then `scripts/adr_sync.py` | The only way a decision is recorded. |
| Working on an ADK agent | `adk-build` | Google's ADK skills with this plugin's baseline applied. |
| ADK 1.x patterns found at intake | `adk-migrate` | Detects all, forces what breaks on 2.x, tickets the rest as `later`. |
| Too big and foggy for one session | `wayfinder` (Matt's) | A map of decision tickets; merges back at `to-spec`. |
| Issues arriving from other people | `triage` (Matt's) | Only for work you did not create. |
| Mid merge conflict | `resolving-merge-conflicts` (Matt's, model-invoked) | Resolves by intent, never aborts. |
| A step only a human can do (credentials, dashboards) | `wizard` (Matt's, model-invoked) | Generates the walkthrough script. |
| The last message didn't land | `wait-what` (Matt's) | Re-pitched in plain English with the glossary's words. |
| Review the "not now" list | `py-intake later` | Shows the `later` tickets and asks what to kill. |

Skills marked "Matt's" come from `mattpocock-skills`; those marked "Repowise" from the `repowise` plugin. The user-invoked ones must be typed by the user; this skill never calls them.

## 3. Answer

One recommendation, in this shape, then stop:

```
Type: <command, in this harness's syntax>
Why: <one sentence, plain English, using the repo's own words>
It will ask you: <the first thing that command needs from you, or "nothing">
```

Harness syntax: Claude Code `/python-dev:<name>` (bare `/<name>` when unambiguous) and Matt's as `/mattpocock-skills:<name>` or bare; GitHub Copilot `/<name>`; OpenAI Codex `$<name>`. If the harness has no Skill tool, say "open `.agents/skills/<name>/SKILL.md` and follow it" for model-invoked skills.

Recommend, don't run. If the user's situation matches nothing above, say so and recommend `grill-with-docs`, because an unmatched situation is an unexamined one.
