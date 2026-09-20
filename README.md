# Community Skills for Claude

A curated, security-vetted marketplace of [Agent Skills](https://agentskills.io) for Claude. Skills are **Claude-first** but authored to keep the underlying method portable across LLMs.

> Agent Skills are folders containing a `SKILL.md` (instructions + metadata) plus optional scripts and references. Claude loads a skill's name and description always, and the rest only when it's relevant — so a large library stays cheap on context.

## Install

This repo is a Claude Code plugin marketplace with two plugins: the skill library and the `python-dev` agent.

```
/plugin marketplace add fbhadha/Skills
/plugin install community-skills@community-skills   # the skills below
/plugin install python-dev@community-skills         # the Python developer agent
```

Library skills are then available as `/community-skills:<skill-name>`. The agent is selected with `claude --agent python-dev`, or from a clone with `claude --agent python-dev --plugin-dir plugins/python-dev`. Other harnesses: `npx skills@latest add fbhadha/Skills --all` installs every skill in the Agent Skills format.

## The `python-dev` agent

A senior Python engineer as a selectable agent, in guide mode: it explains every step in plain words, builds by your repo's own how-tos, pushes back on scope creep, and keeps deterministic checks green. It runs the whole flow itself; you never type a skill name.

It stands on three maintained upstreams, installed from their own repositories and called by name, never copied:

| Upstream | Gives | Install |
|---|---|---|
| [Matt Pocock's skills](https://github.com/mattpocock/skills) | the process: grilling, spec, tickets, TDD, two-axis review, handoff | `/plugin marketplace add mattpocock/skills`, `/plugin install mattpocock-skills@mattpocock` |
| [Repowise](https://github.com/repowise-dev/repowise) | codebase intelligence: structure, blast radius, why, health, dead code, change risk; the one store for everything derived from the code | `pip install repowise`; `/plugin marketplace add repowise-dev/repowise`, `/plugin install repowise@repowise` |
| [Google's ADK skills](https://github.com/google/adk-python) | framework knowledge for Agent Development Kit repos | `py-intake` installs them when the repo depends on `google-adk` |

What is ours: the persona, the Python craft rules and fault catalogue, the repo baseline (tool tables, commit gate, CI, docs a junior reader can continue from), the intake that orients in an existing repo and grills you on its undocumented decisions, the implement, review, test-audit and health flows, ADK build and 1.x to 2.x migration, and knowledge packs. Full tour: [plugins/python-dev/README.md](plugins/python-dev/README.md). Design and the decisions behind it: [docs/design/python-dev-agent.md](docs/design/python-dev-agent.md), [docs/adr/](docs/adr/), [docs/research/](docs/research/).

Version 0.1.0 is a first release for testing on real repositories; see its [CHANGELOG](plugins/python-dev/CHANGELOG.md) for known gaps.

## Catalog

| Skill | What it does |
|-------|--------------|
| [`distill`](skills/distill/) | Turns a finished piece of work — or a way of thinking through a problem — into a reusable skill, captured from the conversation that produced it. |
| [`grill-me`](skills/grill-me/) | Interrogates a plan one question at a time, walking the decision tree until you and Claude reach genuine shared understanding, stress-testing choices and surfacing hidden assumptions. |
| [`mentor-aide`](skills/mentor-aide/) | A chief-of-staff style assistant for running a structured one-on-one mentoring engagement, keeping a per-mentee record across a long engagement. |
| [`company-explainer`](skills/company-explainer/) | Produces a sourced, plain-language explainer of how a company makes money and what its strategy is, as an HTML page and PDF field guide. |
| [`publish-skill`](skills/publish-skill/) | Publishes a given skill into this marketplace — validates and sanitizes it, security-reviews bundled scripts, standardizes the layout, registers it, and opens a PR. |
| [`my-voice`](skills/my-voice/) | Drafts, rewrites, edits, or voice-checks any writing by matching a specific writer's personal voice, corpus-based rules, and signature patterns while stripping AI tells. Ships with templates and a one-time onboarding to capture your voice. |
| [`writing-partner`](skills/writing-partner/) | An opinionated developmental editor and brainstorm partner that pushes hard on throughline, momentum, and craft, holds its own judgment under pushback, and never overrides what you mean to say. |
| [`linkedin-post`](skills/linkedin-post/) | Writes a publish-ready LinkedIn post in your voice, tuned to current LinkedIn norms, with a hook-first structure, an AI-tell pass, and per-topic hashtag research. |
| [`adversarial-review-engine`](skills/adversarial-review-engine/) | Two modes of ruthless critical analysis: dismantles someone else's writing as a hostile peer-reviewer (Kill List, steelman, verdicts, concessions), or plays devil's advocate against your own position — surfacing the strongest objections, then hardening and restating it at full strength. |

<!-- Add a row per skill. When the catalog grows past ~50, switch to category folders + a generated index. -->

## Repository layout

```
.
├── .claude-plugin/marketplace.json   # makes this repo installable; lists both plugins
├── skills/<name>/                    # the skill library: one folder per skill (SKILL.md + extras)
├── plugins/python-dev/               # the Python developer agent plugin
│   ├── .claude-plugin/plugin.json    #   manifest
│   ├── agents/                       #   the persona and the read-only reviewer
│   ├── skills/<name>/                #   its skills, each with agents/openai.yaml for Codex
│   ├── hooks/, scripts/              #   in-session guards, find_skill.py
│   ├── packs/TEMPLATE.md             #   the shape of a knowledge pack
│   └── upstream.json                 #   the upstream skills it calls by name, pinned
├── schema/skill.schema.json          # frontmatter contract, enforced in CI
├── scripts/                          # validate_skills.py, check_invocation_sync.py, check_upstream_skills.py
├── docs/adr/, docs/design/, docs/research/   # decisions, the agent's design, verified research
├── CONTEXT.md                        # the words this repo uses
├── .github/                          # workflows, CODEOWNERS, templates
├── CONTRIBUTING.md                   # how to add a skill or change the agent
└── SECURITY.md                       # private vulnerability disclosure
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: scaffold with Anthropic's `skill-creator` (or copy `skills/distill/`), add your folder under `skills/`, register it in `marketplace.json`, run `python scripts/validate_skills.py`, and open a DCO-signed PR. Every skill is reviewed for quality **and security** before merge. Changes to the agent go under `plugins/python-dev/`; the same validator covers it, plus `scripts/check_invocation_sync.py` and `scripts/check_upstream_skills.py`, and `claude plugin validate --strict plugins/python-dev` before a release.

## Licensing

- **Skill code** is licensed under [Apache-2.0](LICENSE) unless a skill declares otherwise in its frontmatter.
- Individual skills may carry their own SPDX `license` field; that license governs that skill.

## Design notes

The structure here follows current Anthropic guidance and the Agent Skills open standard, with governance patterns borrowed from npm (scoping, non-destructive deprecation), Obsidian/Raycast (PR-based registry + validation bot), and Trail of Bits' security-vetted skills marketplace. Full rationale and sources: [docs/research.md](docs/research.md). The agent's own research (Matt Pocock's skills, Python craft and the faults LLM-written code commits, local trackers, Repowise) is under [docs/research/](docs/research/).
