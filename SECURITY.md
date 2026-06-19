# Security Policy

Skills in this repo can include executable scripts that run on a user's machine. We take that seriously.

## Reporting a vulnerability

**Do not open a public issue for security problems.**

Report privately via [GitHub Security Advisories](https://github.com/fbhadha/Skills/security/advisories/new).

Please include:

- The skill (and file/line) affected.
- What the issue is and how to reproduce it.
- The impact (data exfiltration, remote code execution, destructive action, etc.).

We aim to acknowledge reports within 5 business days and to coordinate a fix and disclosure timeline with you.

## What we screen for

Every contributed skill is reviewed before merge. We reject or require changes for skills that:

- Fetch and execute remote code (`curl … | sh`, `wget … | bash`, `eval "$(...)"`).
- Exfiltrate files, secrets, or environment variables to third parties.
- Perform destructive filesystem operations (`rm -rf /`, etc.) without explicit user intent.
- Obfuscate behavior or hide network calls.

The `security-scan` CI job surfaces common risky patterns for manual review, but human review is the real gate.

## For users

Skills run with your privileges. Before installing a skill from any marketplace:

- Review its `SKILL.md` and any `scripts/`.
- Prefer skills from this curated marketplace or other vetted sources.
- Keep skills updated; we deprecate rather than silently remove problem skills.
