# Provenance: my-voice

Distilled from a personal voice-assistance skill and generalized into a reusable template on 2026-06-19. The original was calibrated to one writer's corpus; this version ships empty templates plus an onboarding guide so any writer can configure it for themselves. No personal corpus or identifying data is included.

## Purpose

This skill turns a writer's corpus into a reusable voice specification that an AI assistant can apply to drafts, edits, and rewrites. The method captures the DNA of how someone writes and makes it repeatable.

## The capture method: three dimensions

### 1. Corpus analysis
**What:** Extract a quantitative profile from the writer's existing body of work.
**How:** Collect 30+ pieces across different contexts; analyze for reading level, sentence-length distribution, vocabulary ceiling, emphasis tools, discourse markers, and platform-specific patterns; record the numbers in `voice-profile.md`.
**Why it matters:** Numbers don't lie. A writer who believes they're terse but averages long sentences will have a different profile than they expect. The corpus gives the real shape.

### 2. Example selection
**What:** Extract real writing samples that show the voice in action.
**How:** Pull 5-8 informal/short-form samples (Bank 1) and 4-8 formal/long-form excerpts (Bank 2); annotate each with the move it demonstrates.
**Why it matters:** Rules are abstractions. "Be opinionated" doesn't teach rhythm. Real examples show what the voice actually looks like in the writer's own hands.

### 3. Rules extraction
**What:** Identify the hard constraints and signature habits.
**How:** Note what the writer never does (banned tools) and always does (signature moves), plus stance and reading level; write them as enforceable, checkable rules.
**Why it matters:** "Be warm" is useless. "Never use em dashes, but use parenthetical asides freely" is actionable.

## Dimensions of the design and the calls made

### generalization_level
Options weighed: ship person-specific (calibrated to one writer) vs. ship a generic template (slots any writer fills).
The call: generic template with an onboarding guide.
Why: the skill should be publishable and reusable without exposing any individual's writing or personal data. Each writer fills in their own profile, examples, and rules at first use.

### onboarding_method
Options weighed: interview-driven, corpus-driven, or manual configuration.
The call: corpus-driven, guided by `references/onboarding.md`, with interview as a fallback for small corpora.
Why: a short corpus analysis beats a long interview, because writers' self-perception rarely matches their actual patterns.

### reference_files
Options weighed: inline everything in SKILL.md vs. separate reference files.
The call: separate files — `voice-profile.md` (template), `examples.md` (template), `humanizer-patterns.md` (the stable engine), and `onboarding.md` (the setup guide).
Why: the humanizer engine is large and stable; separating it keeps SKILL.md focused on the workflow, and the templates can be filled without touching the operator logic.

## Quality gates and the reasoning

### corpus size
The standard: minimum 30 pieces, 100+ preferred, across a mix of contexts.
Why it matters: a small corpus is statistical noise; a large, varied one shows patterns that hold across audiences.

### example annotation
The standard: every example tagged with the move it demonstrates.
Why it matters: unannotated examples look good but don't teach. The model needs to know which feature to copy, or it copies the wrong one.

### rule precision
The standard: enforceable, checkable rules, not vague guidance.
Why it matters: vague rules produce inconsistent output. Bright lines are what keep the voice consistent.

### humanizer engine
The standard: the 30-pattern engine runs on every draft, non-negotiable.
Why it matters: even a well-calibrated voice can slip into em-dash-heavy or promotional prose. The humanizer is the safety rail that a per-writer profile can't replace.

## Branches tried and dropped

- **Shipping the original writer's corpus:** dropped because it exposes personal data and ties the skill to one person. A public skill must ship empty and onboard each user.
- **Interview-based capture as the primary method:** dropped because self-perception doesn't match the corpus. Writers will claim habits the data contradicts. Corpus beats interview; interview is the fallback only.
- **Single-context corpus:** dropped because writing changes by platform and audience. Variety in the corpus is what captures the range.
- **Rules-first approach:** dropped because rules are abstractions. Examples teach texture; rules only handle edge cases and hard constraints.

## Notes for future updates

The humanizer engine is stable and does not need updates. A writer's `voice-profile.md` and `examples.md` should be refreshed roughly yearly if their corpus stays large, because voice evolves. The key insight to preserve: **examples scale better than rules.** Treat the writer's own samples as the source of truth and use rules only for bright-line constraints.
