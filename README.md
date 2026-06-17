# Community Skills for Claude

A curated, security-vetted marketplace of [Agent Skills](https://agentskills.io) for Claude. Skills are **Claude-first** but authored to keep the underlying method portable across LLMs.

> Agent Skills are folders containing a `SKILL.md` (instructions + metadata) plus optional scripts and references. Claude loads a skill's name and description always, and the rest only when it's relevant — so a large library stays cheap on context.

## Install

This repo is a Claude Code plugin marketplace. Add it, then install:

```
/plugin marketplace add fbhadha/Skills
/plugin install community-skills@community-skills
```

Skills are then available as `/community-skills:<skill-name>`.

## Catalog

| Skill | What it does |
|-------|--------------|
| [`distill`](skills/distill/) | Turns a finished piece of work — or a way of thinking through a problem — into a reusable skill, captured from the conversation that produced it. |
| [`mentor-aide`](skills/mentor-aide/) | A chief-of-staff style assistant for running a structured one-on-one mentoring engagement, keeping a per-mentee record across a long engagement. |
| [`company-explainer`](skills/company-explainer/) | Produces a sourced, plain-language explainer of how a company makes money and what its strategy is, as an HTML page and PDF field guide. |

<!-- Add a row per skill. When the catalog grows past ~50, switch to category folders + a generated index. -->

## Repository layout

```
.
├── .claude-plugin/marketplace.json   # makes this repo installable; lists skills
├── skills/<name>/                    # one folder per skill (SKILL.md + extras)
├── schema/skill.schema.json          # frontmatter contract, enforced in CI
├── scripts/validate_skills.py        # local + CI validator
├── .github/                          # workflows, CODEOWNERS, templates
├── CONTRIBUTING.md                   # how to add a skill
├── SECURITY.md                       # private vulnerability disclosure
└── docs/research.md                  # design rationale & sources
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: scaffold with Anthropic's `skill-creator` (or copy `skills/distill/`), add your folder under `skills/`, register it in `marketplace.json`, run `python scripts/validate_skills.py`, and open a DCO-signed PR. Every skill is reviewed for quality **and security** before merge.

## Licensing

- **Skill code** is licensed under [Apache-2.0](LICENSE) unless a skill declares otherwise in its frontmatter.
- Individual skills may carry their own SPDX `license` field; that license governs that skill.

## Design notes

The structure here follows current Anthropic guidance and the Agent Skills open standard, with governance patterns borrowed from npm (scoping, non-destructive deprecation), Obsidian/Raycast (PR-based registry + validation bot), and Trail of Bits' security-vetted skills marketplace. Full rationale and sources: [docs/research.md](docs/research.md).
