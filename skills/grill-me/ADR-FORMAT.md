# ADR format

An Architecture Decision Record captures one hard decision, the forces behind it, and what it commits you to. One decision per file. Records are numbered in order and never deleted — when a decision is overturned, you write a new ADR that supersedes the old one and mark the old one accordingly. The trail of superseded decisions is part of the value; it shows a future reader how the thinking moved.

## When a decision earns an ADR

Only write one when all three hold: the decision is hard to reverse, it would surprise a future reader who lacks the context, and it came out of a real trade-off between genuine alternatives. If any one is missing, skip it. Most decisions don't clear this bar, and that's fine — an ADR directory full of trivia hides the handful that matter.

## File naming

`docs/adr/NNNN-short-kebab-title.md`, where `NNNN` is the next number in sequence, zero-padded to four digits. Examples: `0001-event-sourced-orders.md`, `0002-postgres-for-write-model.md`. The number is permanent even if the decision is later superseded.

## Structure

```markdown
# 0003-soft-delete-for-orders

## Status
Accepted
<!-- One of: Proposed, Accepted, Superseded by 0009, Deprecated -->

## Context
What's true in the world that forced a decision. The pressures, the constraints,
the thing that wasn't working. Written so someone with no memory of this week can
understand why a decision was even needed. State the forces honestly, including the
ones that pulled toward the option you didn't pick.

## Decision
The choice, stated plainly and in the active voice. "We will soft-delete Orders by
setting a cancelled_at timestamp rather than removing the row." One decision. If you
find yourself writing "and we will also...", that's probably a second ADR.

## Alternatives considered
The real options you weighed and why each lost. This is the heart of the record —
it's what stops a future reader from re-running the same debate. Be specific about
what each alternative would have cost.

## Consequences
What this commits you to, good and bad. The capabilities it unlocks and the doors it
closes. Name the downsides you're accepting, not just the upsides — an ADR that only
lists benefits is selling, not recording.
```

## Rules for a good ADR

Write the Context before you know the Decision is "obvious." The point is to capture the world as it looked at decision time, while the alternatives still feel live. An ADR written after the fact, with the losing options quietly trimmed out, teaches a future reader nothing.

Keep it to one decision. The numbering is cheap; splitting two entangled decisions into two records is almost always right.

Status is a fact, not a hope. A decision is Proposed until it's actually been accepted. When a later ADR overturns this one, change the status to "Superseded by NNNN" and leave the rest of the file untouched — you don't edit history, you append to it.

Don't write the ADR yourself and present it as done. Offer it, and when the user agrees, write it from what the two of you actually resolved during the grilling — the alternatives you genuinely weighed and the reasoning the user gave, not a tidied-up version that makes the choice look more inevitable than it was.
