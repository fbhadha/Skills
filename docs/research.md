# Research: building an open-source community skills repo for Claude

This document records the research and design decisions behind this repository's structure. It was produced via a multi-source, fact-checked research pass (five parallel search angles, ~70 sources, confidence-rated).

## Summary of decisions

| Decision | Choice | Why |
|---|---|---|
| Format | Agent Skills open standard (`SKILL.md` + frontmatter) | Now an open standard (agentskills.io, Dec 2025) adopted across Claude Code, Codex, Gemini CLI, Copilot, Cursor — the format itself is the portability layer. |
| Distribution | Be a Claude Code marketplace (`.claude-plugin/marketplace.json`) | Native, zero-custom-tooling install via `/plugin marketplace add` + `/plugin install`. |
| Layout | Flat `skills/<name>/`; categorize past ~50 | Matches anthropics/skills (flat to ~20); large community repos add categories + a catalog file. |
| Skill license | Apache-2.0 (per-skill override allowed) | Patent grant + retaliation clause over MIT; per-item independence preserved via frontmatter `license`. |
| Index license | CC0 (intended for catalog/index) | A code license is the wrong tool for a list; awesome-list standard. |
| Contributor IP | DCO (`git commit -s`) | Lowest friction for a high-volume community repo; no CLA signing flow blocking first PRs. |
| Validation | JSON-Schema frontmatter check in CI, required status | Mechanically blocks malformed skills; lowest-effort highest-leverage gate. |
| Security | Mandatory review + advisory script scan + SECURITY.md | Backdoored skills exist in the wild; vetting is the key differentiator. |
| Versioning | Per-skill SemVer via `metadata.version`; deprecate, don't delete | Independent item lifecycle without breaking installs. |
| Governance | BDFL → maintainer ladder; Contributor Covenant | Standard OSS maturity path. |

## The format (Agent Skills standard)

- A skill is a directory; `SKILL.md` = YAML frontmatter + Markdown body.
- **Required:** `name` (≤64 chars, lowercase/numbers/hyphens, must match folder, no `anthropic`/`claude`) and `description` (≤1024 chars, what + when, third person).
- **Optional:** `license` (SPDX), `metadata` (author/version/tags), `allowed-tools`, `compatibility`.
- **Progressive disclosure:** L1 name+description (~100 tokens, always loaded) → L2 body (on trigger, keep <500 lines) → L3 bundled files/scripts (on demand, ~free until read).
- Official folder names: `scripts/`, `reference/`. (`assets/` is a common community convention.)

## Distribution mechanics

- `.claude-plugin/marketplace.json` (name, owner, plugins[]) makes a repo installable.
- Plugins aggregate skills; skills listed via a `skills[]` array of relative paths.
- Install copies to a versioned cache; skills invoked as `/plugin-name:skill-name`.
- `version` in a plugin/skill pins it — bump to ship updates.
- Anthropic's own marketplaces: `anthropic-agent-skills` (the `anthropics/skills` repo), `claude-plugins-official`, `claude-plugins-community`. Web catalog: `claude.com/plugins`. (`anthropic-agent-skills`/`agent-skills` are reserved names.)

## Prior art surveyed

- **anthropics/skills** — flat layout, IS a marketplace, *no CONTRIBUTING / no contribution path*, dual-licensed, "educational" disclaimer. Leaves the community-contribution niche open.
- **ComposioHQ/awesome-claude-skills** — hosts 1000+ skill files, PR submission.
- **jeremylongshore/claude-code-plugins-plus-skills** — 2,810 skills, 100-point PR validation rubric, own package manager.
- **trailofbits/skills-curated** — security-vetted marketplace created *because skills with backdoors were found*; mandatory code review. Strongest governance model in the wild and the template for this repo's security stance.

## Official tooling we leverage

- **`skill-creator`** (Anthropic, in `example-skills`) — scaffolds individual skills.
- **`claude plugin init <name>`** — CLI scaffold for a skill/plugin.
- **`mcp-builder`** — for MCP servers.
- No official skill builds the repo/governance/marketplace layer — that is this repo's contribution.

## Portability across LLMs

- Write bodies referencing capabilities, not Claude-only tool names.
- Use MCP (Linux Foundation standard; adopted by OpenAI, Google, Microsoft) for tool access.
- Optional `AGENTS.md` shim (60k+ projects; Agentic AI Foundation) for non-skill-aware agents.

## Confidence & caveats

- **High confidence:** SKILL.md fields/limits, progressive disclosure, marketplace mechanics, prior-art structures, OSS governance practices.
- **Verify before quoting:** exact optional-field casing in the standard (`agentskills.io` blocked automated fetch; sourced via search index); some cross-model adoption breadth claims (vendor-flavored).
- **Unverified:** a third-party blog's claims of `marketplace.anthropic.com/skills`, a `claude skills search` CLI, and "~600 skills." Official docs only reference `claude.com/plugins` + the in-app `/plugin` Discover tab.

## Key sources

- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/plugin-marketplaces
- https://code.claude.com/docs/en/discover-plugins
- https://agentskills.io/specification
- https://github.com/anthropics/skills
- https://github.com/trailofbits/skills-curated
- https://opensource.guide/leadership-and-governance/
- https://github.com/sindresorhus/awesome/blob/main/awesome.md
- https://github.com/mheap/frontmatter-json-schema-action
- https://en.wikipedia.org/wiki/Model_Context_Protocol
