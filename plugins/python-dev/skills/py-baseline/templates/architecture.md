# Architecture

The layers, top to bottom. An arrow means "may import". The import-linter contract in `pyproject.toml` enforces this; when the two disagree, the contract is the truth and this file is out of date.

```
entrypoints   (CLI, HTTP, schedulers, ADK agents)   -> application, adapters, domain
application   (use cases, the transaction boundary) -> domain, ports
adapters      (one module per external system)      -> domain, ports
domain        (entities, value objects, rules)      -> nothing in this repo
```

## The shape most work takes

Source adapter -> normalised domain record -> sink adapter. Every source produces the same domain shape; every sink consumes it. A new source or sink is one new module, not a change to the others. See `docs/howto/`.

## Composition root

`src/{{PACKAGE}}/entrypoints/bootstrap.py` is the one place real adapters are wired to the application. Tests wire in-memory adapters there. Nothing else constructs an adapter.

## Where things live

| Question | Look in |
|---|---|
| What does this term mean? | `CONTEXT.md` |
| Why was it built this way? | `docs/adr/` |
| How do I add another X? | `docs/howto/add-a-x.md` |
| Which file is the risky one? | `uv run repowise health` |
| What do the checks enforce? | `AGENTS.md`, `pyproject.toml` `[tool.*]` |
