# Contributing

Thanks for helping build this skills library. This repo is a **curated, security-vetted marketplace** of Agent Skills for Claude. We optimize for *quality over quantity* — a smaller set of skills that reliably work beats a large set that doesn't.

## Quick start

The fastest way to author a well-formed skill is Anthropic's official `skill-creator`:

```
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
```

Then ask Claude to use `skill-creator` to scaffold your skill, or scaffold by hand using `skills/distill/` as a worked example.

## What a skill looks like

Each skill is a self-contained folder under `skills/`:

```
skills/<name>/
├── SKILL.md          # required: YAML frontmatter + a procedure
├── reference/        # optional: deeper docs loaded on demand
├── scripts/          # optional: executable helpers
└── assets/           # optional: templates / output skeletons
```

`SKILL.md` frontmatter must follow the [Agent Skills open standard](https://agentskills.io):

```yaml
---
name: weekly-review            # must equal the folder name
description: >                 # what it does AND when to use it (third person)
  Runs a structured weekly review. Use when the user asks to "do my weekly
  review", reflect on the week, or plan the next one.
license: Apache-2.0            # optional, SPDX
metadata:
  author: your-handle
  version: 0.1.0
  tags: [productivity, planning]
---
```

### Rules (these are CI-enforced)

- `name`: lowercase letters/numbers/hyphens, ≤64 chars, **must match the folder name**, must **not** contain `anthropic` or `claude`.
- `description`: non-empty, ≤1024 chars, states **what** and **when**.
- Body: a procedure (workflows/checklists), not narration. Keep it under ~500 lines; push depth into `reference/`.

### Portability

Skills here are Claude-first but should stay conceptually portable:

- Write the body referencing **capabilities** ("read the file", "run the tests"), not Claude-only tool names, where practical.
- Prefer **MCP** for tool access over hard-coded tool IDs.
- Optional: ship an `AGENTS.md` shim so non-skill-aware agents still pick up the instructions.

## Submission workflow

1. Fork and branch.
2. Add your skill under `skills/<name>/`.
3. Register it in `.claude-plugin/marketplace.json` (add the path to a plugin's `skills` array).
4. Run validation locally: `pip install pyyaml jsonschema && python scripts/validate_skills.py`.
5. Open a PR and complete the checklist. Sign your commits (DCO, below).
6. A maintainer reviews for quality **and security** before merge.

### Acceptance criteria

- Solves a real, repeatable task; not a near-duplicate of an existing skill.
- Passes automated validation.
- Passes a security review (see below).
- Has a clear, trigger-rich description.

PRs with no activity for 14 days are marked stale and closed after a further 7. Comment to keep yours open.

## Security

Skills can carry executable scripts, and malicious skills have been found in the wild. Therefore:

- Bundled scripts must not exfiltrate data, fetch-and-execute remote code (`curl … | sh`), or modify the user's system unexpectedly.
- Reviewers eyeball every script. The `security-scan` CI job flags risky patterns for manual review.
- Found a vulnerability? See [SECURITY.md](SECURITY.md) — report privately, never in a public issue.

## Developer Certificate of Origin (DCO)

We use the [DCO](https://developercertificate.org/) instead of a CLA. Sign off each commit to certify you have the right to submit it:

```
git commit -s -m "Add weekly-review skill"
```

This appends a `Signed-off-by:` line to your commit.

## Versioning

Skills are versioned independently via `metadata.version` (SemVer). Bump it when you change a skill. Removed/retired skills are **deprecated, not deleted** — flagged with a warning and kept reachable so installs don't break.

## Code of Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). By participating you agree to uphold it.

## Changing the `python-dev` agent

The agent lives under `plugins/python-dev/`. Its rules are stricter than the library's, because a target repo depends on them:

- **One persona file.** `agents/python-dev.md` is the only copy; `py-intake` renders the Copilot and Codex forms in the target repo. Keep it about a page: identity, voice, rules and pointers. Knowledge goes in skills.
- **Skills are model-invoked** and carry `agents/openai.yaml`. `scripts/check_invocation_sync.py` fails when the two switches disagree.
- **Call upstream skills by name, never copy them.** Add the name to `upstream.json` with the invocation you assume; `scripts/check_upstream_skills.py` verifies it against the pinned commit in CI. Bump the pin deliberately, in its own commit, after reading the upstream changelog.
- **One read path and one write path per kind of knowledge** (ADR 0005). Anything derived from the code comes from Repowise; do not add a second store, report file or orientation page.
- **No custom gates.** A check goes in as an established tool's rule in `skills/py-baseline/templates/pyproject-tools.toml`; the only scripts we maintain are the change gate, the ADR binder and the README block runner, and they must pass the baseline's own ruff rules.
- **Verify before you write.** Every claim about a tool or an upstream skill is checked by running it; `docs/research/` records what was verified and when.
- **A knowledge pack** is `skills/pack-<domain>/` in the shape of `packs/TEMPLATE.md`, reference only.
- Before a release: `python scripts/validate_skills.py`, `python scripts/check_invocation_sync.py`, `python scripts/check_upstream_skills.py`, `claude plugin validate --strict plugins/python-dev`, a `claude --agent python-dev --plugin-dir plugins/python-dev -p` smoke test, then bump `version` in `plugin.json` and add a `CHANGELOG.md` entry.
