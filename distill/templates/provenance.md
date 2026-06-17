# Template: provenance.md

This is the memory layer for a distilled skill. It holds the "why" the executable body is not allowed to carry, the quotes a capable model surfaces at apply time, and the branches already ruled out so a later update does not re-propose them. A small model never reads it. Write it in the user's voice, plain prose. Stamp this skeleton, fill it, and delete this header.

```
# Provenance: <skill-name>

Captured from a conversation on <date>. Source task: <one line on what was being made or worked through>.

## Dimensions and the calls made

<one block per dimension. the options, the choice, and a supporting quote.>

### <dimension name>
Options weighed: <option A>, <option B>.
The call last time: <which option>.
Why: <one or two sentences in plain prose>.
In their words: "<short quote from the conversation that shows the reasoning>".

## Quality gates and the reasoning behind them

<one block per gate. the standard, and why it mattered here.>

### <gate name>
The standard: <what good looked like>.
Why it mattered: <one or two sentences>.

## Branches tried and dropped

<list the alternatives that were considered and ruled out, so a later update does not re-suggest them.>

- <branch>: dropped because <reason>.

## Notes for future updates

<anything a later update should know. context that is true now but might change. open threads.>
```

## Filled example

```
# Provenance: opinion-blog-post

Captured from a conversation on 2026-06-16. Source task: writing an opinion blog post about why AI rollouts at work stall.

## Dimensions and the calls made

### tone
Options weighed: formal, informal.
The call last time: informal.
Why: the piece was going on a personal channel and a formal register read as stiff and corporate, which worked against the point.
In their words: "I want it to sound like me talking, not like a press release".

### length
Options weighed: short, thorough.
The call last time: short.
Why: the argument was simple and a long version padded it out.

## Quality gates and the reasoning behind them

### skim test
The standard: a busy reader would read it through rather than skim.
Why it mattered: the audience scrolls fast, so a slow opening loses them.

### voice test
The standard: it sounds like the user and not like a model.
Why it mattered: the whole value of the piece is that it reads as a real person's take.

## Branches tried and dropped

- A formal register: dropped for reading stiff on a personal channel.
- A long thorough version: dropped for padding a simple argument.

## Notes for future updates

The voice test is the one most likely to need tuning as the user's writing shifts. If a future run produces something that passes the skim test but still sounds off, that is the gate to revisit.
```
