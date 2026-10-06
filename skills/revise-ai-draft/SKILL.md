---
name: revise-ai-draft
description: Revise any AI-written draft (blog post, essay, story, email, LinkedIn post, report, speech) so it reads as human-written in the places readers and detectors notice (what is included, in what order, how it ends, who is speaking, what gets named), then fix the words. Built from two 2026 studies (StoryScope on fiction, SlopShape on company blog posts) that found AI text stays identifiable from its structure after the wording is changed. Use as the last pass after any AI drafting, whenever the user asks to humanize, de-AI, clean up, tighten, or make an AI draft sound natural, and before presenting long-form writing Claude produced. Use even when the user only says "make this sound less like AI". Works alongside my-voice. This skill fixes structure; my-voice sets the voice.
---

# revise-ai-draft

## What the research found

StoryScope (Russell et al., COLM 2026) and SlopShape (Madler, 2026) reverse-engineered a brief from each human-written text, gave it to five models (Claude Sonnet 4.6, GPT-5.4, Gemini 3 Flash, DeepSeek V3.2, Kimi K2.5), and had an LLM score every version on hundreds of structural features, validated against human annotators.

- Structure alone identifies AI text: 93.2 macro-F1 on 61,608 stories, 97.0 on 13,500 company blog posts, with all word-level style features removed.
- Rewording barely changes that. After span-level edits that removed clichés and purple prose, detection held at 93.9 (fiction) and 96.1 (blogs). Swapping words does not fix an AI draft.
- The five models make the same choices. Human texts are spread out and sit in rarer configurations (rarity percentile 0.71 vs 0.49 for fiction, 0.83 vs 0.44 for blogs).

So revise the decisions first and the words last. Numbers below are human vs AI, as share of texts or as a mean on a 1 to 5 scale.

## Hard rules

- Add nothing that is not in the material. No invented names, numbers, quotes, studies, customers, places, or experiences. When the piece needs a specific that does not exist, ask the author one question, or list it after the text as `NEEDS: <what>`.
- Keep the author's position and every sourced fact.
- Cut freely. Paragraph count and length are not preserved. Human blog posts were shorter, and under 800 words leans human.
- Do not fake human mess (typos, random tangents, invented asides). Every structural change needs a reason that is in the material.

## Advice this skill overrides
Many writing guides recommend vivid metaphors, a short sentence after a long one for rhythm, and paradox or cliffhanger hooks. The first two are among the strongest AI markers in the data: figurative density is the largest single separator in StoryScope (3.00 vs 3.66, d = 1.2), and stylized fragments appear in 85% of AI stories vs 67% of human ones. Hooks and teasers were not measured, and adding them means writing lines the author did not. When a house style guide asks for these, follow this skill and tell the user which rule you overrode.

## Procedure

### 1. Gather the material
List what is real: names, dates, places, titles, numbers with their sources, quotes, what went wrong, what the author is unsure about. Take it from the draft, the conversation, and the author's notes. This list is the only source for anything you add. Much of the human advantage in both studies came from this: the human author knew things the model's brief did not contain.

### 2. Reverse-outline and cut
Write one word for each paragraph's job: preview, context, claim, case, mechanism, evidence, lesson, summary, pep talk, next step. Delete every preview, lesson, summary, and pep talk, and every last sentence of a paragraph that restates the paragraph.
- A closing that restates the thesis was the largest single gap in SlopShape (0.65 share gap). A summary stage: 0.61.
- Human posts mostly did not state a thesis or announce their structure before the first section (0.42 share gap).
- The narrator states the theme or lesson in 52% of human stories vs 77% of AI stories. Thematic explicitness 3.28 vs 3.94.

Then read the outline in order. Each paragraph should answer a question the one before it raises. Where one does not, reorder the paragraphs. Do not add teaser lines to create the question.

### 3. Choose the entry
Open on material, not on the thesis and not on the state of the world: a dated event, a quote, a number with its source, a scene already moving, a question the author actually has.
Exception: emails, memos, status updates, and instructions open with the ask or the answer in the first sentence. They still get no preview and no recap.

### 4. Change one default the material justifies
AI takes the most common option at every decision, and the sum of those choices is what gets detected. Name the defaults in the draft and change at least one where the material gives a reason:
- One causal line, no side threads (no subplots 57% vs 79%): keep a side thread the material contains even if it does not serve the thesis.
- Straight chronology (mostly chronological 55% vs 72%): start at the moment that matters, then go back.
- Every element serves one theme (thematic unity 4.41 vs 4.74): keep one detail that is only true.
- Problem, mechanism, fix, summary (blogs): drop the mechanism section or the fix list when a real case already shows it.
- The protagonist chooses, learns, and grows (growth 43% vs 68%, no internal change 28% vs 11%): let events decide the ending, or let the character stay the same.
- Every expectation set up is paid off (53% vs 73%): let one go unpaid or turn.

### 5. End early
Stop at the last new thing.
- Fiction: end at or just after the climax (69% vs 51%). Delete epilogues, forward time jumps ("Years later"), closing images of sky, city, or lights, and closing aphorisms.
- Nonfiction: no restated thesis, no "Ultimately". End on the last point, or on a concrete next step the author has: a link, an address, the next post. Human posts kept a way for the reader to take part; AI posts dropped it (0.59 share gap).

### 6. Set the stance
- Replace the confident institutional explainer with a person who saw something, or with a flat report (institutional voice leans AI, 0.35 share gap).
- Delete old-versus-new framing and "modern" or "next-generation" claims (0.50 and 0.36 share gaps), and stakes aimed at the reader ("or fall behind").
- Write as a person talking to a person: "I", "we", and "you" where the author would use them, in active voice with the actor named ("Management saw", not "It has been observed by management").
- Show uncertainty where it is real. Keep dry humour and irony where the author has them (wry tone 36% vs 13%).
- Fiction: allow a morally mixed protagonist (59% vs 38%) and characters who know more than the reader (32% vs 18%).

### 7. Name things
Replace vague allusions with named references from the material: titles, authors, brands, places, dates, people (explicit named references 47% vs 24%; brand and pop-culture references 40% vs 13%; historical dates and periods lean human in blogs). Delete statistics credited to unnamed sources. In fiction, use more named secondary characters and places where the story has room (7 or more named characters 35% vs 16%).

### 8. Sentences
- Literal by default. Delete metaphors, similes, extended conceits, and recurring images. Figurative density is the strongest of all 304 StoryScope features (3.00 vs 3.66, d = 1.2). Extended conceits 40% vs 83%. Recurring metaphor motif 69% vs 96%.
- Remove rhetorical patterning: parallel and list-like structures (70% vs 99%), triads, alliteration (79% vs 98%), repeated words for cadence, and stylized one-line fragments (67% vs 85%). Do not add short punchy fragments for rhythm. That is now an AI pattern.
- Let sentences run the way people write them: loose chains joined by and, but, so (76% vs 55%). Plain and formal words can sit side by side (mixed register 56% vs 19%). Drop the uniformly elevated register (11% vs 40%).
- Turn nouns made from verbs back into verbs: "achieved an optimization of the metric" becomes "optimized the metric", "conducted an analysis" becomes "analyzed".
- Emotion: name it, or show an action or a line of dialogue (named emotions 29% vs 8%; behaviour 86% vs 60%). Delete body sensations such as chest, throat, breath, stomach (embodied emotion 39% vs 81%) and weather or light that mirrors a mood (47% vs 87%).
- Cut smell, light, and weather unless they change what happens (smell 57% vs 82%).
- Introduce people by what they say or do before what they look like (description first 30% vs 52%).
- Claude drafts: split long, heavily subordinated sentences (a typical sentence of 21 to 35 words in 85% of Claude stories vs 46% of human ones); cut "the way a man does X" comparisons and "a kind of".
- GPT drafts: cut "as if", "as though", "perhaps", "not X but Y", and endings that jump to a distant future and sum up a life (51% of GPT stories vs 25% of human ones).

### 9. Words and format
Last pass: no em or en dashes; none of delve, leverage, utilize, crucial, pivotal, robust, seamless, landscape, navigate, foster, enhance, showcase, underscore, testament, tapestry, unlock, empower, journey; no "It's not X, it's Y"; no -ing tails that claim significance ("highlighting the importance of"); no "In today's"; no signposting; no bold inside prose; no headings or bullets under 800 words unless the reader needs to scan; no "The End". Replace jargon and buzzwords with the concrete thing they refer to, taken from the material; when the material does not say, list it under NEEDS. In scripts, keep bracketed visual notes such as [Graphic: ...] unchanged. If my-voice is installed, run its humanizer pass here, but skip any of its rules that conflict with this skill.

### 10. Check
- Can any paragraph go without losing a fact, a case, or a step? Delete it.
- Would a listener need to hear any sentence twice? Rewrite it.
- Does the last paragraph say something new?
- Is any sentence a preview, a restatement, or a moral?
- Is every name, number, and quote in the material?
- Did at least one structural default change, for a reason the material gives?
- Zero dashes and zero figurative language, unless the author asked for figures?

## Output
When this runs as the last step of another task, output only the revised text. When the user asked for the revision, give at most three lines on what changed structurally and any `NEEDS:` items, then the revised text.

## Reference
`references/evidence.md`: sources, every number used here with its feature definition, rules that were left out, and the limits of the evidence. Read it when a rule needs defending or a genre is not covered here.
