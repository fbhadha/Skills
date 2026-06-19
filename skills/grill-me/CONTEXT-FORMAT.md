# CONTEXT.md format

`CONTEXT.md` is the glossary for one context. It records what words mean inside this part of the system, and nothing else. No implementation notes, no decision logs, no to-do lists. If you're tempted to write down how something is built, that's an ADR or code comment, not this file.

## Why it's a glossary and nothing else

The value of a glossary is that you can trust every word in it to mean exactly one thing. The moment it also holds implementation details, the meanings get tangled up with the mechanics, the file goes stale the instant the code changes, and people stop trusting it. Keep it pure and it stays true for years. A term's definition should still be correct after three rewrites of the code beneath it.

## Structure

A short intro line naming the context, then one entry per term. Keep entries alphabetical so they're easy to scan and easy to merge.

```markdown
# Ordering — Glossary

The language of the ordering context. Definitions here govern this context only;
the same word may mean something different in billing.

## Cancellation
Voiding an entire Order before it has been fulfilled. Releases any held stock and
reverses the authorisation. Cancelling part of an order is not a Cancellation — see
Line Removal.

## Line Removal
Taking a single item off an Order that is still open, leaving the rest of the order
intact. Distinct from Cancellation, which voids the whole thing.

## Order
A customer's confirmed request for one or more items at agreed prices. An Order
exists from confirmation until it is fulfilled or cancelled.

## Customer
The party who pays for an Order. Not necessarily the person who receives the goods —
that's the Recipient.
```

## Rules for a good entry

Write the definition in plain prose, at the same grade 10 level as the rest of the grilling. Define the term as a noun or a thing in the domain, not as a function or a database table.

When two terms are easy to confuse, say so inside both entries and point at each other. The "Cancellation is not Line Removal" cross-reference above is doing the most important work in the file — it stops the two ideas from collapsing back into one.

Never include: class names, table names, API endpoints, file paths, library choices, or any sentence that describes how the thing is implemented. Those belong in code or in an ADR. If you delete every implementation detail from an entry and nothing of the meaning is lost, you wrote it right.

When you resolve a term mid-grilling, add or update its entry immediately, in the glossary for the correct context. If a `CONTEXT-MAP.md` exists, make sure you're editing the glossary that owns the term, not a sibling context that merely borrows it.
