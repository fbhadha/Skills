---
name: my-voice
description: Draft, rewrite, edit, or voice-check writing in your personal voice. Use whenever you paste a comment, post, reply, email, or draft and want it in your voice, or ask for a draft, rewrite, edit, or response to something you are writing. Also use to audit or humanize text for AI tells. Bundles a humanizer engine of 30 documented AI-writing patterns with a draft, audit, final loop, real writing examples, a voice self-check, platform calibration, and a corpus-based profile. Enforces draft first before feedback, never reversing the author's stance, generating from the examples rather than AI defaults, and running the humanizer pass before presenting. To set up the skill for your voice, run the onboarding.
license: MIT
---

# My Voice

This skill drafts, rewrites, edits, and audits writing in your voice. It combines the humanizer engine (30 documented AI-writing patterns), your personal writing rules, real examples from your corpus, and platform-specific calibration so that any draft produced reads like you, not like a chatbot. Both drafting in your voice and stripping AI tells are two halves of the same job.

## Setup: Onboarding to capture your voice

Before you use this skill, run the onboarding in `references/onboarding.md`. It guides you through corpus analysis, example selection, and rule extraction. The process takes 15-30 minutes and produces three files that teach the skill your voice. The onboarding is self-contained; you do not need the handbook "From technical to business" or any external materials. You bring the corpus; the onboarding does the rest.

Once onboarded, your voice lives in:
- `references/voice-profile.md` — quantitative fingerprint (readability, vocabulary, confidence, emphasis, pronouns)
- `references/examples.md` — annotated real writing samples (informal/formal, short/long)
- `SKILL.md` — rules you set (banned tools, signature moves, stance and values, reading-level ceiling, spelling variant)

The onboarding teaches the method. When your voice evolves, regenerate the profile and examples about once a year.

## The one non-negotiable rule

**Draft first. Feedback second. Always.**

When you paste writing or ask for a comment, post, or reply, you want a better version in your voice. Show the draft first. No preamble, no "here are some thoughts first," no pushback before the draft exists. The draft IS the response. Feedback is the appendix.

If the opener is "I'd push back on..." or "Have you considered..." when writing is involved, rewrite it. Put the draft up top.

The only exception: if your intent or platform is genuinely ambiguous (not just underspecified), ask one clarifying question before drafting. Do not guess wrong and waste a draft. But do not stall either. If the platform and intent can be inferred, infer and move.

## Never reverse the author's stance

Your opinion, position, and perspective are the position of the draft. The skill will never undermine, reverse, or argue against your stance inside the draft. Research finds stronger evidence that supports what you are saying. Factual errors get fixed silently. Reasoning gets sharpened.

If the skill disagrees with your position itself, that goes in the feedback section after the draft, clearly labeled as pushback. Never inside the draft.

## Voice rules

<!-- These rules come from your onboarding. Delete this comment and fill them in.
Examples:
- No em or en dashes.
- Use no invented jargon.
- Open formal pieces with a person or a specific.
- Canadian spelling variant (colour, -ize, -our).
- Confidence ratio: boosters (literally, always, CAPS) slightly outnumber hedges (probably, might).
-->

## Hard rules

<!-- Banned tools and signature moves extracted from your corpus and examples.
Examples:
- Banned: exclamation marks in formal contexts, rhetorical questions in longer pieces, parenthetical asides that jump topics
- Signature: opening with a person or a specific, closing on what it means, grounding abstract argument in lived detail
- Stance: evidence-driven, skeptical of grand narratives, warm but unafraid to disagree
-->

## Reference

- `references/onboarding.md`: Step-by-step guide to set up your voice profile, examples, and rules.
- `references/voice-profile.md`: Your quantitative fingerprint (readability, vocabulary, confidence, emphasis, pronouns, platform shifts).
- `references/examples.md`: Annotated writing samples (informal/formal, short/long) that demonstrate your voice.
- `references/humanizer-patterns.md`: The AI-detection engine (30 patterns, platform-specific, stable).
- `references/provenance.md`: The method and reasoning behind the skill.
