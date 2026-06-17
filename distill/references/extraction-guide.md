# Extraction guide

Author-facing. Read this before your first capture. It explains what to pull out of a conversation, how to decide what survives the prune, how to split specific from general, how to build the interview, and shows one full capture so the shape is clear.

## The extraction schema

A capture pulls seven things out of the conversation. The first six feed the executable body. The seventh is the memory layer.

1. **Goal and output type.** One line on what was being made or worked through. A blog post, a purchase decision, an HTML field guide, a way of reframing a worry. This becomes the TASK line of the spec.

2. **Process.** The ordered moves that led to the result, pruned to the reusable ones. This becomes the STEPS of the spec. See the prune rubric below for what to cut.

3. **Dimensions.** The points where a real alternative was on the table. Tone, depth, format, scope, audience, level of risk. These are the most valuable thing you extract, because they are what the skill asks about next time. A dimension has at least two named options and a choice that was actually made between them. Capture both the options and the choice. The options go into the apply steps as a question. The choice goes into the provenance as the default the user can keep or change.

4. **Quality gates.** The standards the user applied to judge good from bad. Capture the standard, never the rejected attempt. "Read for whether a busy reader would skim it" is a gate. "The third draft was too long" is not, it is a dead end. Gates become RULES and CHECK items.

5. **Guardrails.** Hard rules the user set out loud. "No company names." "Keep it under two pages." "Canadian spelling." These become RULES, written in positive form.

6. **Output template.** Only when the original produced a structured artifact. Capture the skeleton, stripped of the user's content: the variables, how the sections are organized, what each section and element is for, the layout and styling pattern. For an HTML or CSS artifact that means the section structure, the named variables or tokens, the grid or layout approach, and a one-line note on what each block does. This becomes an asset the body points at, plus an OUTPUT contract.

7. **Provenance.** The supporting quotes and the reasoning behind the key calls. This is the memory layer. It holds the "why" that the executable body is not allowed to carry, and the quotes a capable model surfaces at apply time so the user sees the evidence behind a path. It also records the branches that were tried and dropped, so a later update does not re-suggest something already ruled out.

## The prune rubric

Most of a conversation is not worth keeping. The skill of capture is knowing what to drop.

Keep:

- The move that worked.
- The standard that judged it.
- The choice points where a real alternative existed.
- The guardrails set out loud.

Drop:

- Dead ends. A try that was abandoned because it fell short. The information that mattered is the standard that rejected it, which you already kept as a gate.
- Restatement and back-and-forth that did not change the direction.
- Anything specific to this one situation that has no general form. If it cannot be turned into a variable and would not recur, it is context, not method.

The test for a move: would the user want to do this again on a different version of the same task. If yes, keep it. If it only made sense because of where this particular conversation had gone wrong, drop it and keep the gate instead.

The test for a dimension: was there a named alternative, and was a choice made. A step with no fork is a step. A step with a fork is a dimension, and the fork becomes a question.

## The generalization rubric

After you have the method, split specific from general.

Run automatically, no question asked, when you are at least ninety five percent sure:

- Domain-agnostic method and universal structure: keep and generalize.
- Named companies, projects, products, people, and one-off facts: strip to a variable. "Acme" becomes `{{company}}`. "the VIA scorecard" becomes `{{artifact}}`. The method survives, the context does not.

Below that bar, ask. And ask regardless: every capture carries at least three questions. The bar is not an excuse to skip the interview. If the automatic pass left fewer than three genuine doubts, surface the three most consequential generalization calls anyway and put them to the user. Go hunting for the edge cases. The cost of a question is small. The cost of a skill that is silently locked to one company, or silently too generic to be useful, is the whole point of the tool lost.

## Building the interview

The questions target the calls the automatic pass cannot judge. Three reliable shapes:

- **Specific or general.** "Is this part specific to this situation, or do you want it generalized so it carries to another company or topic?" Use it on anything that looks like context but might be method, or method that might be context.
- **Step or branch.** "Was this a fixed step, or a point where you would want a choice next time?" Use it when you are unsure whether a move is always done or was one option among several. This is how you find dimensions the user did not name out loud.
- **Keep or strip.** "In the template, what do you want kept and what stripped?" Use it on every output template, because the line between skeleton and content is a judgment call.

Ask one at a time where the interface allows it. Where the interface offers tappable options, use them, since the user is often on mobile. Keep the wording plain.

## Worked capture

A short illustration. The user spent a long conversation with Claude writing a blog post about how they think about AI at work. Here is what a capture pulls out.

**Goal and output type.** Write an opinion blog post on a work-related AI topic, in the user's voice, ready to publish.

**Process, pruned.** Start from the user's raw take in chat. Draft. Read the draft against the user's standards. Cut anything that reads as filler. Tighten the opening so it earns the read. The two earlier drafts that were dropped for sounding generic do not survive. The standard that dropped them does.

**Dimensions.** Tone, with two options that were weighed in the conversation, a formal register and an informal one, and informal was chosen. Length, with a short punchy option and a longer thorough one. These become the first questions the blog skill asks.

**Quality gates.** Read for whether a busy reader would skim it. Read for whether it sounds like the user and not like a model. Both become CHECK items.

**Guardrails.** Canadian spelling. No em dashes. No invented jargon.

**Output template.** None here, since a blog post is prose. If the same user later built an HTML field guide, that capture would carry the section skeleton and the design tokens as an asset.

**Provenance.** The quote where the user said why informal won, kept so the skill can show it next time. The note that formal was considered and dropped, so a later update does not re-propose it. The two gates, with the line of reasoning behind each.

The executable body that comes out of this asks tone and length up front, drafts, then runs the two gates as a CHECK before presenting. The provenance file holds the quotes and the reasoning. Next time the user says "I want to write a blog," the skill triggers, shows that informal was the call last time and why, offers the choice to keep it or switch, and starts from there.
