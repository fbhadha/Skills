<!-- Thanks for contributing a skill! Complete the checklist so review is fast. -->

## What does this skill do?

<!-- One or two sentences. -->

## Type of change

- [ ] New skill
- [ ] Update to an existing skill
- [ ] Repo tooling / docs

## Acceptance checklist

- [ ] The skill lives in `skills/<name>/` and `<name>` matches the `name` in frontmatter exactly
- [ ] `name` is lowercase letters/numbers/hyphens, ≤64 chars, and does **not** contain `anthropic` or `claude`
- [ ] `description` says **what** the skill does **and when** to use it (≤1024 chars, third person)
- [ ] `SKILL.md` body is a procedure (not narration) and under ~500 lines
- [ ] Bundled `scripts/` (if any) are documented and contain no obfuscated/remote-execution code
- [ ] The skill is reasonably portable: the body references capabilities, not Claude-only tool names, where practical
- [ ] `python scripts/validate_skills.py` passes locally
- [ ] I certify the DCO: I have the right to submit this under the repo license (`git commit -s`)

## Security

- [ ] I have reviewed the skill (and any scripts) for anything that exfiltrates data, runs remote code, or modifies the user's system unexpectedly

## Notes for reviewers

<!-- Anything that helps review: prior art, why it's useful, edge cases. -->
