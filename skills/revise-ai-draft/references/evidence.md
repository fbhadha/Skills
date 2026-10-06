# Evidence behind revise-ai-draft and revise-ai-draft-small

Author-facing. This is the rationale layer. The small-model spec carries none of it.

## Sources

- **StoryScope.** Russell, Rajendhran, Pham, Iyyer, Wieting. "StoryScope: Investigating idiosyncrasies in AI fiction." COLM 2026. [arXiv:2604.03136](https://arxiv.org/abs/2604.03136). Code and data: [github.com/jenna-russell/storyscope](https://github.com/jenna-russell/storyscope). 10,272 prompts reverse-engineered from human short stories (Books3 anthologies), each written by the human author and by Claude Sonnet 4.6, GPT-5.4, Gemini 3 Flash, DeepSeek V3.2, Kimi K2.5. 61,608 stories, about 4,750 words each, scored on 304 features by Gemini 3 Flash (human validation kappa 0.84).
- **SlopShape.** Madler. "SlopShape: Identifying AI-Generated Commercial Web Content." [arXiv:2609.15369](https://arxiv.org/abs/2609.15369) (v3, 28 Sep 2026). Replication of StoryScope on 2,250 pre-ChatGPT B2B company blog posts (268 domains, 2008 to 2022) plus 11,250 mirrors from the same five models. 203 features, 176 structural (human-model kappa 0.951).
- **LAMP.** Chakrabarty, Laban, Wu. "Can AI writing be salvaged?" CHI 2025. [arXiv:2409.14509](https://arxiv.org/abs/2409.14509). Seven edit categories from professional writers: cliché, unnecessary or redundant exposition, purple prose, poor sentence structure, lack of specificity and detail, awkward word choice and phrasing, tense inconsistency. 74% of expert edits were span replacements, 18% deletions, 8% insertions.

## Headline results

| result | fiction (StoryScope) | blogs (SlopShape) |
|---|---|---|
| human vs AI, structure only, macro-F1 | 93.2 | 97.0 |
| same, after span-level LAMP rewording | 93.9 (278 Gemini stories) | 96.1 (all 1,450 test mirrors, self-rewritten) |
| six-way attribution accuracy, structure only | 68.4% | 68.6% |
| mean rarity percentile, human vs AI | 0.71 vs 0.49 (d 0.83) | 0.835 vs 0.436 (d 1.80) |
| human text rarest of its six versions | 57.8% | 85.6% |

Reading: the signal sits in decisions about content, order, ending, and stance. Word-level editing leaves it in place. The five models converge on one region of feature space; human texts are spread out.

## Fiction features (StoryScope released data, 61,575 scored stories)

Computed from `data/storyscope_features.parquet`. Human share vs pooled AI share, or mean. Every row below is consistent across all five models (each model sits on the same side of the human value). d is Cohen's d.

| feature -> value | human | AI | leans |
|---|---|---|---|
| figurative device density (1-5) | 3.00 | 3.66 | AI, d 1.18, the largest of all 304 |
| figurative language in character depiction (1-5) | 3.06 | 3.78 | AI |
| sentence structures: frequent parallel or list-like | 70% | 99% | AI |
| thematic explicitness and moralizing (1-5) | 3.28 | 3.94 | AI |
| extended conceit present | 40% | 83% | AI |
| emotion conveyed by environmental mirroring | 47% | 87% | AI |
| emotion conveyed mainly by embodied sensations and metaphors | 39% | 81% | AI |
| sound patterning prominence (alliteration, assonance) | 1.55 | 1.91 | AI |
| post-climax denouement length | 1.02 | 1.47 | AI |
| lexical register: mixed, frequent code switching | 56% | 19% | human |
| rhythmic markedness (1-5) | 3.17 | 3.61 | AI |
| recurrent metaphorical motif present | 69% | 96% | AI |
| thematic unity (1-5) | 4.41 | 4.74 | AI |
| register consistently elevated or literary | 11% | 40% | AI |
| irony and humour | 1.07 | 0.68 | human |
| tone earnest or lyrical | 40% | 71% | AI |
| setting as psychological mirror (1-5) | 3.58 | 4.07 | AI |
| allusions to pop culture or brand names | 40% | 13% | human |
| emotion conveyed by action and behaviour | 86% | 60% | human |
| smell among dominant senses | 57% | 82% | AI |
| emotion named with explicit labels | 29% | 8% | human |
| tone ironic or wry | 36% | 13% | human |
| Latinate vocabulary (1-5) | 2.51 | 2.83 | AI |
| narrator comments on themes | 51% | 76% | AI |
| dialogue used for philosophical debate | 34% | 59% | AI |
| protagonist growth or enlightenment | 43% | 68% | AI |
| resolution by protagonist's choice | 46% | 69% | AI |
| explicit named reference to texts or authors | 46% | 24% | human |
| no subplots | 57% | 79% | AI |
| sentence fragments stylistically significant | 67% | 85% | AI |
| frequent loose multi-clause chains | 76% | 55% | human |
| mostly paratactic | 30% | 14% | human |
| central character introduced by external description | 30% | 52% | AI |
| atmosphere built from weather and light | 73% | 90% | AI |
| 7 or more named characters | 35% | 16% | human |
| reader expectations set up and fulfilled | 53% | 73% | AI |
| reader expectations set up and subverted | 41% | 24% | human |
| no significant internal change in protagonist | 28% | 11% | human |
| resolved through internal understanding or acceptance | 27% | 47% | AI |
| protagonist morally mixed | 58% | 38% | human |
| red herrings used | 33% | 16% | human |
| ends at or just after the climax, no forward jump | 69% | 51% | human |
| ambiguous or interpretive ending | 34% | 19% | human |
| mostly chronological with rare flashbacks | 55% | 72% | AI |
| character knows more than the reader | 32% | 18% | human |
| direct address to the reader present | 11% | 2% | human (minority move) |

Per-model notes from the same data:
- **Claude Sonnet 4.6.** Lowest figurative density of the five (3.18), but sentences run long: 85% of stories sit in the 21 to 35 word band vs 46% human. Flat event escalation (3.19 vs 3.63 human), low event variety, conflict by avoidance or silence (45% vs 21%), 12 em dashes per 1,000 words in the released dev stories, and frequent "the way" comparisons.
- **GPT-5.4.** Most rhythmically marked prose (3.81) and the most conventional figures of speech; endings that jump to a distant vantage and sum up a life (51% vs 25% human); heavy "as if", "as though", "perhaps", "not X but Y".
- **Gemini, DeepSeek, Kimi.** Highest simile rates ("like a") and the most smell and gold or amber light in the dev stories. The paper adds that Gemini has the bleakest settings and the tidiest, longest endings, and Kimi sits at the generic centre of the AI cluster.

## Commercial features (SlopShape, as published)

Core values, v3 (Table 6). Share gap = difference in share of posts.

| feature -> value | leans | gap |
|---|---|---|
| conclusion restates thesis or reframes | AI | 0.650 |
| functional stages include summary or synthesis | AI | 0.609 |
| external participation pathway absent | AI | 0.592 |
| legacy-versus-modern contrast: no | human | 0.497 |
| thesis before first section: no | human | 0.419 |
| freshness signalling: modern or next-generation framing | AI | 0.360 |
| credibility basis: confident institutional explanation | AI | 0.347 |
| functional stages include mechanism explanation | AI | 0.285 |
| temporal references: historical date or period | human | 0.283 |
| article length: short, under 800 words | human | 0.274 |

v1 and v2 also listed: payoff promised in the title (AI, 0.624), stakes escalation absent (human, 0.362), editorial explainer voice (AI, 0.308). v3 dropped features that responded to formatting (titles, headings, lists) after finding human posts and AI posts reached the scorer in different formats.

The paper's own example of the AI shape: "In this post, we'll cover why onboarding stalls, three fixes that work, and how to measure the difference." / "Paper checklists were built for a slower era." / "In short, structured onboarding saves time."

## Limits

1. **Brief lossiness.** Every AI text was written from a prompt reverse-engineered from the human text. The human author had full context. Part of the human advantage in named references, dates, and side threads is information the model never had. Supplying real material is the largest fix, and a post-hoc pass cannot create it.
2. **Human is not the same as good.** The fiction corpus is published anthology fiction, much of it older. The blog corpus is 2008 to 2022 content marketing. The skills keep only rules where the human direction is also defensible writing practice.
3. **Model drift.** The measured models are 2026 versions. Surface habits shift between releases (GPT-5.4 already cut its em dash rate). Structural habits were more stable across all five models, which is why the skills weight them.
4. **SlopShape release.** The paper states a public release at github.com/pulse-energyeu/slopshape. That URL returned 404 on 5 Oct 2026, so the full instrument and its answer distributions cannot be checked. Between v1 and v3 the author removed format-sensitive features and attribution fell from 79.3% to 68.6%. The author runs Sitefire, a company that produces AI-optimized web content (declared in the paper).
5. **Unknown directions.** SlopShape's top-20 includes second-person address density, reader naming explicitness, effort framing, ownership assignment, and definition form, with no published direction. The skills do not use them.
6. **A misreport in StoryScope's text.** Section 4.1 says humans break the fourth wall in "67% vs 39%" of stories and address the reader in "28% vs 7%". Both are ordinal means (0 = never). The released data shows direct reader address in 11% of human stories vs 2% of AI. The skills treat reader address as allowed, not as a target.
7. **LLM annotation.** All features were assigned by an LLM. Agreement with humans was high (kappa 0.84 and 0.951) but every number inherits that scorer's judgement.
8. **Averages.** Each number describes a corpus. Any single human text can show AI-leaning values. The aim is to remove the defaults a model adds without a reason, not to hit a profile.

## Rule to evidence map (small-model spec)

| spec row | evidence |
|---|---|
| DELETE preview, world opener | thesis before first section, gap 0.419; LAMP unnecessary exposition |
| DELETE old way vs new | legacy-versus-modern gap 0.497; freshness signalling gap 0.360 |
| DELETE restatement, lesson | narrator thematic commentary 51% vs 76%; thematic explicitness 3.28 vs 3.94 |
| DELETE loss warning | stakes escalation (SlopShape v1 core) |
| DELETE unnamed source, unsourced number | GPT numeric density and claim sourcing fingerprints; humanizer vague attributions |
| DELETE closing summary | conclusion restates thesis gap 0.650; summary stage gap 0.609 |
| FICTION body sensation to emotion word | embodied 39% vs 81%; explicit labels 29% vs 8% |
| FICTION smell, weather, light | smell 57% vs 82%; weather and light 73% vs 90%; environmental mirroring 47% vs 87% |
| FICTION post-climax and setting coda | ends at climax 69% vs 51%; denouement 1.02 vs 1.47 |
| REWRITE metaphor, simile | figurative density d 1.18; extended conceit 40% vs 83% |
| REWRITE not X but Y, triads, repetition | parallel or list-like structures 70% vs 99%; rhythmic markedness 3.17 vs 3.61 |
| REWRITE one-line paragraph (dialogue exempt) | stylized fragments 67% vs 85%; one paragraph per speaker is normal fiction layout |
| RULES keep a concrete next step | external participation pathway absent leans AI, gap 0.592 |
| REWRITE sentence over 35 words | Claude 21 to 35 word band 85% vs 46% |
| WORDS table | Wikipedia "Signs of AI writing" vocabulary; Latinate register 2.51 vs 2.83 |

## Left out on purpose

- Adding time jumps, subplots, moral ambiguity, or reader address in the small spec. A small model can only add these by inventing content.
- Second-person density and reader naming in blogs. Direction not published.
- Title rewriting. SlopShape v3 removed title features as format artifacts.
- "Vary sentence length with short punchy lines." The StoryScope data shows that move is now more common in AI fiction than in human fiction.


## Validation runs (October 2026)

Model: Qwen2.5-3B-Instruct, Q4_K_M, llama.cpp on one CPU core, temperature 0. Draft A: a 313-word AI-style bookkeeping blog post, with two facts supplied. Draft B: the last nine paragraphs of a Claude Sonnet 4.6 story from the StoryScope dev set (the Ciro's prompt). Hard hits come from scripts/lint_output.py, which checks surface patterns only, so 0 hits does not mean the text reads as human.

| run | draft | hard hits in draft | hard hits in output | output words / draft words |
|---|---|---|---|---|
| SKILL.md as one system prompt | A | 15 | 16 | 1.07 |
| code pass only | A | 15 | 3 | 0.59 |
| step mode (revise.py) | A | 15 | 0 | 0.61 |
| code pass only | B | 11 | 6 | 0.98 |
| step mode (revise.py) | B | 11 | 0 | 0.71 |

- SKILL.md as a single prompt failed at 3B. The model copied the draft and only appended the facts. Use step mode below 14B. Single-prompt mode on 14B is untested.
- Step mode on A took 82 seconds and placed the facts after the right sentence. One rewrite stayed weak ("It's important to understand your business, not just about compliance"), and one triad cut dropped "over your finances".
- Step mode on B split every long sentence and deleted the simile sentence. It kept the extended sun metaphor, because a metaphor without "like" or "as if" matches no pattern. That needs a larger model or revise-ai-draft.
- During these runs the repetition check never fired (its backreference pointed at the wrong regex group). It was fixed afterwards and has not been re-run on the model.


## Style-guide rules checked against the evidence (October 2026)

Source: an internal scriptwriting guide modelled on Kurzgesagt, Veritasium, and Vsauce, merged on request. Each rule was kept, added, or rejected against the two studies.

| guide rule | decision | reason |
|---|---|---|
| open on what the reader came for; never "In this document, I will" | already covered | DELETE preview row; SlopShape thesis-before-first-section gap 0.419 |
| cut every word that does not move the idea | already covered | human posts shorter; 18% of LAMP expert edits are deletions |
| visual metaphors ("an atom is like a crowded solar system") | rejected | figurative density 3.00 vs 3.66, d = 1.18, the largest StoryScope separator; extended conceits 40% vs 83% |
| a long sentence, then a short one, for rhythm | rejected | stylized fragments 67% human vs 85% AI |
| paradox hook; each paragraph ends on a question | rejected as added lines; kept as reordering only (large skill step 2) | not measured; adding hooks means writing lines the author did not |
| strict chronological breadcrumbs | not added | mostly chronological 55% human vs 72% AI (fiction) |
| "you" and "we", active voice | added | SlopShape confident institutional voice leans AI (gap 0.347); active voice itself not measured |
| strong verbs over weak verb plus noun | added | not measured in either study; plain-language rule that does not conflict with them |
| jargon purge | added to the large skill, from material only | not measured; named concrete references lean human (46% vs 24%) |
| read-aloud test | added to the large skill check | not measured |
| bracketed visual notes in scripts | added: kept unchanged in both skills and the runner | format convention outside both studies |
