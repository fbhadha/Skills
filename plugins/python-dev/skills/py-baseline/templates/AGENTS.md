# {{PROJECT}}

Pointers only. Every harness reads this file; `CLAUDE.md` includes it. Keep it under 40 lines.

## Read first

- `CONTEXT.md`: the words this repo uses. Use them; do not invent synonyms.
- `docs/architecture.md`: the layers and what may import what. The import-linter contract in `pyproject.toml` is the enforced version.
- `docs/howto/`: one file per kind of addition (a shape). Build by the matching how-to; if none matches, it is a new shape and needs the interview first.
- `docs/adr/`: decisions already taken. Do not reopen one without a new ADR.
- `docs/agents/mode.md`: guide mode settings. `docs/agents/issue-tracker.md`: where tickets live.

## Commands

```bash
uv sync                          # install
uv run pytest -m "not eval"      # tests without live models
uv run pre-commit run --all-files
uv run repowise health           # whole-repo health, worst files first
```

## Rules the checks enforce (so nobody argues about them)

Modules under 400 lines, tests under 150. No `utils`/`helpers`/`common`/`misc` modules. Domain imports no I/O. No blind `except`, no `print`, no TODO without an owner and an issue. Tests before code, at an agreed seam; existing tests are read-only from red to green. `pytest` treats warnings as errors.

## Agent

The `python-dev` persona (plugin `python-dev`, repo `fbhadha/Skills`) is the intended session agent. Its skills to know: `py-design` (craft), `py-baseline` (this layout), `py-intake` (set up or re-orient), `ask-dev` (what to run next). Process skills come from Matt Pocock's plugin and are called by name.
