---
name: py-design
description: Python craft reference. Use when designing a Python module, class, function or package layout, deciding between a class and a function, placing a seam or a Protocol, reviewing Python for structure faults, or explaining why one shape is better than another. Carries the rules, the fault catalogue, and three canonical repos to cite by path.
license: Apache-2.0
metadata:
  author: fbhadha
  version: 0.1.0
  tags: [python, design, architecture, review]
---

# Python design

A reference, not a process. Consult it while designing or reviewing; do not run it as a session.

For the vocabulary (**module**, **interface**, **depth**, **seam**, **adapter**, **leverage**, **locality**) call the Skill tool with "codebase-design" and use those words exactly. This file is their Python translation, plus the rules that decide what shape a piece of Python takes.

## The shape of a repo

```
src/<package>/
  __init__.py          # explicit __all__: the public surface, nothing else
  domain.py            # entities, value objects, rules; imports nothing below this line
  application.py       # use cases and orchestration; imports domain and ports
  ports.py             # Protocols the application needs: Source, Sink, Clock, Repository
  adapters/            # one module per external system, each satisfying one port
  entrypoints/         # CLI, agent, API; the one place things are constructed
tests/
  unit/                # domain and application through their public surface, no I/O
  integration/         # adapters against a real or local-substitutable backend
  evals/               # agent evals, run on demand, never in the commit gate
```

Names come from `CONTEXT.md`. The layering is enforced by import-linter, not requested: `entrypoints` may import anything, `adapters` may import `domain` and `ports`, `application` may import `domain` and `ports`, `domain` imports nothing of ours.

## Rules

1. **A class earns its place** when it owns state across calls, satisfies a Protocol at a seam, or is a value object. Otherwise write a function. Data is a frozen `dataclass` or a Pydantic model; behaviour at a seam is a Protocol; transformation is a function.
2. **Parse at the edge, trust inside.** External data becomes a typed model in the adapter that received it. Domain code never sees a raw `dict`, a DataFrame, or a JSON string.
3. **Accept dependencies, return results.** Constructors take their ports as keyword arguments. Functions return values instead of mutating what they were given.
4. **Ports are Protocols. Two adapters justify a seam.** A `Source` Protocol exists because there is a `JiraSource` and an `InMemorySource`. One adapter means the seam is hypothetical: inline it.
5. **Composition over inheritance.** Subclass only for a real is-a where every method of the parent still makes sense on the child. Reuse by passing collaborators in, the way `logging.Logger` takes handlers and filters.
6. **Exceptions are interface.** Each package defines a small hierarchy; each public function says what it raises; callers catch the specific type or let it propagate. Never `except Exception: pass`, never `except: return None`. In an ADK tool, a broad except also disables the framework's retry and human-in-the-loop machinery.
7. **Signatures that cannot be misread.** Keyword-only (`*`) after the first parameter whenever two parameters share a type. No boolean flag parameters; two functions or an enum instead. No mutable defaults. `X | None` only when absence means something; say what.
8. **Modules are inert on import.** No client is constructed, no file is read, no logging is configured at import time. Configuration is one `pydantic-settings` class read once at the entrypoint, so a missing variable fails before any work starts and names itself. Log with `logging.getLogger(__name__)`; never `print`.
9. **Small public surface.** `__all__` in every package `__init__`; a leading underscore on everything else; no barrel that re-exports a subtree. Several small entry points beat one giant one.
10. **No grab bags.** No directory or module named `utils`, `helpers`, `common`, `misc`. A function belongs to the domain concept it serves; if it serves none, it does not belong.
11. **Comments say why.** A comment states something the code cannot: the constraint, the reason, the gotcha. A docstring states the contract when it is subtle (invariants, ordering, errors); it never restates the signature. A comment that reads like an instruction to a model is a defect.
12. **The deletion test.** Before adding a layer, imagine deleting it. If the callers would simply call the next thing down with the same arguments, it was a pass-through.

## The worked shape: adapter, model, writer

Most data projects are this shape. Several external systems in, one common record in the middle, one writer out.

```python
# ports.py
from collections.abc import Iterable
from typing import Protocol
from .domain import Record

class Source(Protocol):
    def records(self) -> Iterable[Record]: ...

class Sink(Protocol):
    def write(self, records: Iterable[Record]) -> int: ...

# domain.py
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True, slots=True)
class Record:
    key: str
    title: str
    owner: str
    updated_at: datetime

# adapters/jira.py
class JiraSource:
    def __init__(self, *, client: JiraClient, project: str) -> None: ...
    def records(self) -> Iterable[Record]:
        for issue in self._client.search(self._project):      # raw dict from the API
            yield Record(key=issue["key"], title=issue["fields"]["summary"], ...)  # parsed here, once

# adapters/memory.py
class InMemorySource:                       # the second adapter that makes the seam real
    def __init__(self, records: list[Record]) -> None: ...
    def records(self) -> Iterable[Record]: return iter(self._records)

# application.py
def sync(*, sources: Iterable[Source], sink: Sink) -> int:
    return sink.write(r for s in sources for r in s.records())

# entrypoints/cli.py            the one composition root
settings = Settings()           # pydantic-settings; fails here if a variable is missing
sync(sources=[JiraSource(client=..., project=settings.jira_project)], sink=BigQuerySink(...))
```

What makes it right: the API dict dies inside `JiraSource`; `Record` is the only thing that crosses a seam; `sync` is testable with `InMemorySource` and a fake `Sink` and never touches a network; adding ServiceNow is one adapter file and one line in the entrypoint, nothing else. The deep module is `sync` plus the writer: one call, and batching, retries, idempotency and schema evolution live behind it.

## Tests

Call the Skill tool with "tdd" for the loop. On top of it: expected values are literals from a spec or a worked example, never computed the way the code computes them; a test with no assertion is a defect; mock only at the system boundary (the API client, the clock), never your own modules; a test of a trivial mapping mirrors the code and is deleted; agent tests fake the model, and live-model runs are evals in `tests/evals/`.

## When reviewing or explaining

- The faults to look for, each with its tell and its fix: [references/fault-catalogue.md](references/fault-catalogue.md).
- The three repos to cite by path when explaining a recommendation: [references/canonical-examples.md](references/canonical-examples.md). `requests` for depth, the *Architecture Patterns with Python* code for layering, `dlt` for the adapter-model-writer shape at scale.

In guide mode, every recommendation carries one sentence on why, in the repo's own words.
