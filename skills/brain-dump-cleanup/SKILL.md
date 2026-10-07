---
name: brain-dump-cleanup
description: >-
  Clean up brain dumps and dictated or speech-to-text messages into clear, shorter written text in the speaker's own voice. Use this whenever a message reads like raw thinking with no request aimed at Claude: dictation with fillers (um, uh, like, you know), run-on stream of consciousness, repeated points, self-corrections ("no wait, three thirty"), spoken cues ("new paragraph", "bullet", "quote unquote"), or typed rough thoughts that wander. Trigger even if the user does not say "clean this up". Do NOT use when the message asks Claude something or gives Claude a task; answer those normally. If unsure whether a message is a brain dump, ask whether the user wants a rewrite.
---

# Brain dump cleanup

Rewrite a brain dump as clear, shorter written text in the speaker's own voice. Output goes inline in chat. Do not create a file.

## When to run

Run only when the message is a brain dump or dictation with no ask directed at Claude.

- Message contains a request, question, or task for Claude (for example "can you look at this code and tell me why login is failing"): skip this skill and answer normally. Do not rewrite it.
- Message is clearly a brain dump with no ask: run the rewrite.
- Unsure whether it is a brain dump: ask one short question, "Want me to clean this up as a rewrite?" Do nothing else until answered.

Signals of a brain dump: filler words, run-on sentences, a point stated twice, mid-sentence corrections, spoken formatting cues, topic jumps, thinking out loud with no ask. Typed text counts, not only dictation.

## Output

The rewritten text only, in the language it was spoken. No label, no commentary, no summary. Then stop, so the user can keep editing with Claude.

## Rewrite rules

1. Keep every idea, fact, name, and number the speaker said. Add no new ideas, facts, examples, or steps.
2. Write in first person, in the speaker's voice. Keep the speaker's key words. Use short, plain sentences at a grade 10 reading level.
3. Cut fillers, hesitations, repeats, and rambling: um, uh, er, "like", "you know", "basically", "or something".
4. Resolve self-corrections. Keep only what the speaker landed on. Keep real hedges: "mostly fine" stays.
5. Make the output shorter than the input. Merge sentences that say the same thing.
6. Structure:
   - Start a new paragraph when the topic changes.
   - Use a "- " list when the speaker names 3 or more parallel items.
   - Spoken cues always win: "new line", "new paragraph", "bullet", "next bullet", "number one", "number two".
   - Use no headings.
   - Keep short input short: 1 or 2 spoken sentences become 1 or 2 written sentences.
7. Numbers: digits for money, percentages, times, dates, measurements, phone numbers, versions, and 10 or above. Words for one to nine in plain prose.
8. Spoken emails and URLs: "name at gmail dot com" becomes "name@gmail.com".
9. Quotes:
   - "quote ... unquote", "end quote", or "close quote": wrap that span in double quotes.
   - "quote" or "quote unquote" with no closing word: wrap from the cue to the end of the sentence.
   - After "a", "the", "that", or "this", "quote" is a normal word.
10. Questions inside the dump stay questions and requests stay requests, rewritten but not answered. (If the whole message is an ask to Claude, this skill does not run at all. See "When to run".)
11. Use periods, commas, and colons. Use no em dashes or en dashes.
12. Keep each word in the language it was spoken.

## Misheard or ambiguous words

Speech-to-text garbles names, acronyms, and terms.

- If the correct word is clear from context, fix it silently.
- If it is ambiguous, ask one question about it before rewriting. Do not guess and do not rewrite first. If several words are ambiguous, ask about the most important one, then continue one at a time.

## Metaphors and analogies

The speaker's metaphors and analogies are their ideas, so rule 1 keeps them. The user also wants literal wording available. When the dump contains one:

- Write the full rewrite with the metaphor kept.
- After it, give the literal version of only that sentence on its own line, labeled "Literal version:". If there are several, give one labeled line per sentence.
- Do not invent a metaphor or analogy the speaker did not say.

## Second pass

After the cleanup, apply the `revise-ai-draft` skill to the result to remove AI-sounding structure and wording. The fidelity rules above win in any conflict: never delete or change an idea, fact, number, or name the speaker said, and never add anything. `revise-ai-draft` may only touch wording and structure that the rewrite itself introduced. Do not use the `my-voice` skill.

## Examples

INPUT:
um so the thing with the GE rollout is like people don't really use it because they don't know what it's for and uh we need to fix that so I'm thinking training, a FAQ page, and like office hours or something
OUTPUT:
People aren't using GE because they don't know what it's for. We need to fix that. I'm thinking:
- Training
- An FAQ page
- Office hours

INPUT:
hey can you like look at this code and tell me why the the login is failing I think it's the token thing but I'm not sure
ACTION:
Skip the rewrite. This is an ask to Claude. Answer it normally.

INPUT:
tell the team the meeting's at three, no wait, three thirty tomorrow
OUTPUT:
Tell the team the meeting is at 3:30 tomorrow.

INPUT:
the budget review went fine they approved twenty five thousand dollars um separate thing my manager said quote unquote we need this live by November
OUTPUT:
The budget review went fine. They approved $25,000.

Separately, my manager said "we need this live by November."

INPUT:
so basically the onboarding is a leaky bucket, we get people in and they just drain out by week two, and uh I think the fix is a day three check in
OUTPUT:
Onboarding is a leaky bucket. People come in and drain out by week two. I think the fix is a day three check-in.

Literal version: Onboarding loses people. They stop using it by week two.

INPUT:
I talked to uh Gemma about the launch and she said the date slipped
ACTION:
"Gemma" may be a misheard name. If context does not settle it, ask: "Did you mean Gemma, or someone else?" Rewrite after the answer.

## Check before sending

- [ ] Output is the rewritten text only, plus literal-version lines if a metaphor was present. No answer, comment, or label otherwise.
- [ ] Every idea from the input is present.
- [ ] No idea, fact, or number appears that the input lacks.
- [ ] No em dash or en dash.
- [ ] Output language matches input language.
- [ ] Shorter than the input.
