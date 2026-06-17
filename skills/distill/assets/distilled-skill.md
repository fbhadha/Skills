# Template: a distilled skill's SKILL.md

Stamp this for every skill you write. The frontmatter triggers it conversationally. The body is a machine spec, so write and audit it with the machine-spec skill. The apply protocol lives as the first steps, so it survives on a small model. Fill the angle-bracket slots and delete this header.

## Frontmatter

```
---
name: <method-name-in-lowercase-with-dashes>
description: <What this skill produces or works through, then the conversational phrases that trigger it. Cover the natural ways the user would start this task, like "I want to write a blog" or "I'm thinking about buying X." Be pushy. Trigger even when the user does not name the skill.>
license: MIT
metadata:
  distilled: true
---
```

The metadata flag is the marker, and the only thing distill needs to add. `distilled: true` is how groom mode tells its own skills from the user's hand-made ones and the ones Anthropic ships. Keep it under `metadata`, since a bare top-level key fails packaging. There is no date field, because the file's own modification time already carries recency and survives install.

## Body

```
# <NAME>
TASK: <one imperative line. what to produce or work through, from the user's new request, following the captured method.>

## INPUT
request: <the user's new task in this domain>
<other fields the method needs, one per line, with type>

## DIMENSIONS
<one line per choice point. name, then the options.>
<tone: formal | informal>
<length: short | thorough>

## OUTPUT
<the literal target. for a structured artifact, paste the skeleton or point at assets/<file>. for prose, describe the shape and the gates it must pass.>

## STEPS
1. Present each DIMENSIONS choice to the user. IF reference/provenance.md is readable THEN show the call made last time and one supporting quote for each dimension. Ask the user to keep that path or adjust it.
2. Set each dimension from the user's answer.
3. <first method step. atomic. one action.>
   IF <dimension condition> THEN <action> ELSE <action>
4. <next method step.>
5. Run CHECK before presenting.

## RULES
- <each guardrail and quality gate, atomic, positive, testable. one per line.>

## EXAMPLES
INPUT:
<a real input>
OUTPUT:
<the exact output for that input, matching the OUTPUT contract>

## CHECK
- [ ] <one pass/fail line per quality gate>
- [ ] <output matches the OUTPUT contract>
```

Drop DIMENSIONS only if the method truly had no choice points, which is rare. Never drop OUTPUT, EXAMPLES, or CHECK. Those three carry the most weight for a small model.

## Filled example

The blog capture from the extraction guide, written out.

```
---
name: opinion-blog-post
description: Write an opinion blog post in my voice on a work-related topic, ready to publish. Trigger when I say "I want to write a blog," "help me write a post about," "draft a blog on," or otherwise start an opinion piece meant to go out under my name. Trigger even when I do not say the word blog.
license: MIT
metadata:
  distilled: true
---
```

```
# opinion-blog-post
TASK: Write a publish-ready opinion blog post in the user's voice from the user's raw take.

## INPUT
request: the topic and the user's rough take on it

## DIMENSIONS
tone: formal | informal
length: short | thorough

## OUTPUT
A blog post in prose. Opening that earns the read in the first two lines. Body that holds one clear argument. No filler. Sounds like the user, not like a model.

## STEPS
1. Present the tone and length choices. IF reference/provenance.md is readable THEN show that informal and short were the calls last time and the one-line reason for each. Ask the user to keep that or adjust.
2. Set tone and length from the answer.
3. Draft the post at the chosen tone and length from the user's take.
4. Cut every line that reads as filler.
5. Tighten the opening until the first two lines earn the read.
6. Run CHECK before presenting.

## RULES
- Use Canadian spelling.
- Use no em or en dashes.
- Use no invented jargon.
- Hold to one argument across the post.

## EXAMPLES
INPUT:
topic: why most AI rollouts at work stall, take: it's never the tech, it's that nobody owns the change
OUTPUT:
<a short informal post that opens on the ownership point, holds that one argument, and closes on it, in Canadian spelling with no dashes>

## CHECK
- [ ] a busy reader would not skim it
- [ ] it sounds like the user, not a model
- [ ] Canadian spelling, no em or en dashes
- [ ] one argument held across the whole post
```
