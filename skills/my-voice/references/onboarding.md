# Onboarding: set up my-voice for a new user

The my-voice skill matches a specific person's writing. Out of the box it ships with empty templates. Before the skill can draft in someone's voice, three files have to be filled in for that user:

- `references/voice-profile.md` — the quantitative fingerprint
- `references/examples.md` — real writing samples (the most important file)
- the "Voice rules" and "Hard rules" sections of `SKILL.md` — the bright-line constraints

Run this onboarding the first time the skill is used, or whenever the user wants to recalibrate. It takes about 15-30 minutes and is mostly interview plus light analysis.

## What you need from the user

Ask the user to gather a corpus of their own writing:

- **Minimum 30 pieces, 100+ is better.** More signal, less noise.
- **A mix of contexts.** Casual (comments, DMs, posts), professional (emails, LinkedIn), and long-form (essays, articles, reports) if they write it. Voice shifts by audience, so single-context corpora miss the range.
- **Real, sent writing.** Not drafts they polished for this exercise. The goal is how they actually write.

If they can't produce a corpus, you can still onboard from a smaller set (5-10 pieces) plus an interview — just mark the profile as estimated and widen it later.

## Step 1 — Build the voice profile

Work through `references/voice-profile.md` field by field. For each, either measure it from the corpus or infer it and mark it as estimated.

- **Readability and sentence rhythm.** Run the corpus through a readability tool (textstat, or any Flesch-Kincaid calculator) for reading level and sentence-length distribution. If no tool is available, sample 10 pieces and estimate.
- **Vocabulary.** Are the words plain or specialized? What share is one-syllable? Where does complexity come from — argument and rhythm, or vocabulary?
- **Confidence.** Count boosters (literally, totally, never, always, CAPS) against hedges (probably, might, I think). The ratio reveals whether they assert or qualify.
- **Emphasis fingerprint.** This is the visible signature. Scan for ALL CAPS, scare quotes, parentheticals, ellipses, em dashes, exclamations, questions, profanity, emoji. Record the frequency and any context where one goes to zero (e.g. no exclamations on professional platforms).
- **Pronouns and structure.** Do they write from "I"? Address the reader as "you"? Think in systems ("they/their") or individuals? How do pieces open and close?
- **Per-context blocks.** Fill one platform block per context they write for, capturing how the voice shifts.

Fill the file, delete the template comment, and save.

## Step 2 — Collect and annotate examples

This is the most important step. Work through `references/examples.md`.

- **Bank 1 (informal / short-form):** pull 5-8 real samples across the casual-to-composed gradient.
- **Bank 2 (formal / long-form):** pull 4-8 real excerpts — openings, a plain thesis, and closes especially.
- **Annotate each** with a one-line "what to take" naming the move it demonstrates (a rhythm, an emphasis habit, a characteristic phrase, a structural arc). Unannotated examples look good but don't teach; the note tells the model what feature to copy.
- **Normalize em dashes** in the samples to commas or periods so the file never teaches the banned pattern. Keep everything else as their real words.

## Step 3 — Extract the hard rules

Read the corpus and the examples, then fill the "Voice rules" and "Hard rules" sections of `SKILL.md` with enforceable, bright-line constraints. The test: a rule is good if it can be checked. "Be authentic" cannot. "Zero em dashes," "always open with a person or a specific," "use a specific spelling variant," "never reverse the author's stance" all can.

Capture, at minimum:
- **Banned tools** — what this writer never does (em dashes? questions in formal contexts? hedging language? emoji?).
- **Signature moves** — what they always do (an emphasis tool, characteristic phrases, a closing style).
- **Stance and values** — political framing, optimism vs. cynicism, evidence-driven vs. intuitive — so drafts never reverse who they are.
- **Reading-level ceiling and spelling variant.**

## Step 4 — Confirm and test

- Show the user the filled profile and a couple of example annotations. Let them correct anything that doesn't sound right — self-perception and reality often differ, and the corpus wins, but the user should sign off.
- Draft one short piece and one longer piece. Run the humanizer pass and the voice self-check. Ask the user: "Does this read like you?" Tune the rules and examples based on what they flag.

## Maintenance

Voice evolves. If the corpus stays above ~100 pieces, regenerate the profile and refresh the examples about once a year. A ratio that was 2:1 boosters-to-hedges five years ago might be 1.5:1 now. The humanizer engine (`references/humanizer-patterns.md`) is stable and does not need updates.
