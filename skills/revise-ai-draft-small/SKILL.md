---
name: revise-ai-draft-small
description: Executable spec for a small or local model (Qwen, Llama, Gemma, Phi class, 3B to 14B, via Ollama or ADK) that revises any AI-written draft so its structure and wording read as human-written. Deletes announced previews, recap endings, stated morals, old-versus-new framing, unsourced statistics, metaphors, body-sensation emotion, and AI vocabulary, using only facts already in the draft. Use for an automated cleanup pass on AI output in a local pipeline, or whenever a deterministic rule-only revision is wanted. Ships with scripts/revise.py, which runs these rules through Ollama as one-sentence steps a 3B model can follow, and scripts/lint_output.py. For judgement-heavy rewrites with Claude, use revise-ai-draft instead.
---

# revise-ai-draft-small
TASK: Rewrite draft so it reads as written by a person, using only facts from draft and facts.

## INPUT
draft: the text to revise
facts: names, dates, numbers, sources, or quotes from the author, or "none"

## OUTPUT
<the revised text, in the same language and the same person (I, we, you, he, she) as draft>

## STEPS
1. Set GENRE to FICTION if draft tells a story with characters and scenes. Otherwise set GENRE to NONFICTION.
2. Delete every sentence that matches a row of the DELETE table.
3. IF GENRE is FICTION THEN apply every row of the FICTION table.
4. IF facts is not "none" THEN place each fact in the sentence about the same subject.
5. Apply every row of the REWRITE table.
6. Replace words with the WORDS table.
7. Remove bold marks, emojis, and "The End".
8. IF GENRE is NONFICTION and draft has fewer than 800 words THEN turn headings and bullet points into plain sentences.
9. Output the revised text.

## DELETE
| sentence type | examples |
|---|---|
| says what the text will cover | "In this post, we'll cover", "Let's explore", "Here's what you need to know", "This guide walks you through" |
| opens on the state of the world | "In today's fast-paced world", "Now more than ever", "In an era of" |
| sets the topic against an old way | "Gone are the days", "built for a slower era", "Traditional X no longer works", "next-generation", "modern teams need" |
| repeats or explains the sentence before it | "This shows that", "In other words", "This highlights", "That's the power of" |
| states a lesson, moral, or general truth about life | "It was a reminder that", "The lesson is", "He realized that power is", "In the end, it was never about" |
| warns the reader of loss | "fall behind", "can't afford to ignore", "get left behind" |
| cites an unnamed source or a number with no source | "Studies show", "Experts agree", "Research suggests", "73% of companies" |
| closing summary or pep talk | "In conclusion", "In short", "Ultimately", "The bottom line", "Ready to", "Start today", "The future is" |

## FICTION
| find | do |
|---|---|
| emotion shown as a body sensation: chest tightened, throat closed, stomach dropped, heart pounded, breath caught | replace with the emotion word: afraid, angry, ashamed, relieved, sad, happy |
| sentence only about a smell, the weather, or the light | delete |
| character speech that explains the story's theme | delete |
| paragraph after the climax that jumps ahead in time: "Years later", "In the weeks that followed" | delete |
| last sentence that only describes the setting: sky, city, sea, lights | delete |

## REWRITE
| find | rewrite as |
|---|---|
| metaphor or simile: "like a", "as if", "as though", "the way a man calls a dog", "a galaxy of" | the plain literal statement |
| "not X but Y", "It's not X, it's Y", "less X than Y" | a plain statement of Y |
| list of three abstract words: "clarity, confidence, and connection" | the single most precise word |
| repeated words or clauses for rhythm: "burns, and burns, and burns" | one plain clause |
| weak verb plus a noun made from a verb: "achieved an optimization of", "made a decision", "conducted an analysis of" | the plain verb: "optimized", "decided", "analyzed" |
| passive voice with the actor after "by": "It has been observed by management that" | active voice with the actor first: "Management saw that" |
| paragraph of one sentence with 6 words or fewer and no quotation marks | join it to the paragraph before |
| sentence longer than 35 words | two sentences |
| em dash (—) or en dash (–) | a comma, a period, or parentheses |

## WORDS
| replace | with |
|---|---|
| delve into | look at |
| leverage, utilize | use |
| crucial, pivotal, vital | important, or delete |
| robust | strong |
| seamless, seamlessly | delete |
| landscape (not land) | field, market |
| navigate (not travel) | handle |
| foster | build |
| enhance | improve |
| showcase, underscore, highlight (verb) | show |
| a testament to | shows |
| journey (not travel) | process, or delete |
| unlock, empower | let, help |
| embark on | start |
| realm | area |
| Moreover, Furthermore, Additionally (first word) | delete the word |
| It's worth noting that, It's important to note that | delete the phrase |

## RULES
- Keep every name, date, quote, link, and sourced number that is not in a deleted sentence.
- Keep every opinion and claim of the author that is not in a deleted sentence.
- Keep a last sentence that gives a concrete next step: a link, an email address, a phone number, a sign-up.
- Keep each line of dialogue as its own paragraph.
- Keep every bracketed note, such as [Graphic: a red balloon], unchanged.
- Add a name, date, number, quote, or event only when it appears in facts.
- Write in plain words a 15-year-old knows.
- Output only the revised text, with no notes, labels, or explanations.

## EXAMPLES
INPUT:
draft:
How to Cut Onboarding Time in Half

In today's fast-paced business landscape, onboarding is more crucial than ever. In this post, we'll cover why onboarding stalls, three fixes that work, and how to measure the difference.

Paper checklists were built for a slower era. Studies show that 69% of employees stay longer after a great onboarding experience. The real problem isn't paperwork — it's ownership. When nobody owns day one, new hires wait for laptops, logins, and answers.

Assign one owner per hire. Ship the laptop before the start date. Schedule the first week before the person arrives, so they feel clarity, confidence, and connection.

In short, structured onboarding saves time. Ready to transform your onboarding? Start today.
facts:
In 2021 our ops lead tracked 40 hires. The ones whose laptop arrived on day one finished training four days sooner.
OUTPUT:
How to Cut Onboarding Time in Half

The problem is ownership. When nobody owns day one, new hires wait for laptops, logins, and answers. In 2021 our ops lead tracked 40 hires, and the ones whose laptop arrived on day one finished training four days sooner.

Assign one owner per hire. Ship the laptop before the start date. Schedule the first week before the person arrives, so they feel confident.

INPUT:
draft:
He paused just inside the doorway, gloved hand resting a moment on the polished frame, and let the place resolve around him. The mirrored walls doubled and redoubled the room until Ciro's seemed less a single chamber than a glittering galaxy. White-jacketed waiters shot through it in elliptical paths, bearing silver trays of cocktails that flashed like wandering comets.

He understood it.

His chest tightened when the maître d' said the call was for him. The air smelled of gardenias and money. Power, he realized, was never owned — only rented.
facts:
none
OUTPUT:
He stopped inside the doorway, one gloved hand on the frame, and looked over the room. Mirrors on every wall made Ciro's look twice its size. Waiters in white jackets carried trays of cocktails between the tables, and he knew how all of it worked.

He was afraid when the maître d' said the call was for him.

## CHECK
- [ ] No sentence says what the text will cover.
- [ ] The last paragraph adds information that no earlier paragraph states.
- [ ] No sentence states a lesson, moral, or general truth about life.
- [ ] No sentence sets the topic against an old way.
- [ ] No metaphor or simile.
- [ ] No — and no –.
- [ ] No word from the left column of the WORDS table.
- [ ] Every name, date, number, and quote appears in draft or facts.
- [ ] Output is shorter than draft.
- [ ] Every bracketed note from draft appears unchanged.
- [ ] Output is only the revised text.
