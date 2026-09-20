# Python developer agent

The shared language for the Python developer agent designed in `docs/design/python-dev-agent.md`.

## Language

**Junior reader**:
The person the agent's output is judged against: can read Python but not write it fluently, has never seen the repo, and cannot ask the author anything. Success means they can understand and modify the code from the docs alone.
_Avoid_: junior dev, human reviewer, senior engineer (the bar is lower and stricter than a senior pick-up)

**Fresh-eyes test**:
The check for the junior reader bar: a brand-new agent session given only the repo's README and docs, no conversation history, is asked to add a small feature; the pass is zero questions back to the user.
_Avoid_: onboarding test, docs test

**Shape**:
A recurring kind of addition the repo already knows how to make (another source adapter, another agent tool, another writer), described by one how-to and backed by one working example. A ticket that matches a shape is built by template; one that matches no shape triggers a grilling session and produces a new shape.
_Avoid_: pattern (overloaded with GoF design patterns), template (the how-to is the template; the shape is the thing it describes)

**How-to**:
One of the repo's human-facing docs, `docs/howto/add-a-<thing>.md`, describing one shape as steps that mirror a real example package. Executed or compiled in CI so it cannot drift.
_Avoid_: guide, tutorial, playbook
