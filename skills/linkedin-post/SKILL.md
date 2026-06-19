---
name: linkedin-post
description: Write a LinkedIn post in the user's voice, ready to publish, tuned to how LinkedIn reads right now. Use whenever the user wants a LinkedIn post or says "write a LinkedIn," "draft a post for LinkedIn," "turn this into a LinkedIn post," or otherwise starts a piece meant to go out under their name on LinkedIn. When this skill is active it governs the LinkedIn voice and supersedes the general my-voice skill for LinkedIn output, so do not also defer to my-voice. Trigger even when they do not name the platform, as long as the destination is LinkedIn. Requires a one-time voice setup at first use (see references/linkedin-playbook.md and the my-voice onboarding).
license: MIT
metadata:
  distilled: true
---

# linkedin-post
TASK: Write a publish-ready LinkedIn post in the user's voice, from their topic or their take.

## INPUT
request: the topic and the user's rough take, or an existing draft to rework

## DIMENSIONS
length: feed post about 200 words | article about 450 words
close: bookend back to the open | broader provocative line | personal-choices ending
edge: measured for a watching employer | sharper

## OUTPUT
A LinkedIn post in prose. The first two lines are a hook that sparks curiosity read cold and survives the see-more fold, about 210 characters. One clear argument. Personal disclosure that drives into a structural point. Lands on a concrete image or a plain position, not a slogan. No em dashes, no questions, no exclamations. Then a short set of recommended hashtags, about three niche and on-topic, researched for this topic rather than pulled from a fixed list, for the end of the post.

## SETUP (first use)
This skill matches the user's writing. The voice section of `references/linkedin-playbook.md` ships as a template and must be filled from the user's own LinkedIn corpus before drafts will sound like them. Use the my-voice onboarding method (`skills/my-voice/references/onboarding.md`) to capture the LinkedIn slice: word count, sentence rhythm, emphasis moves, characteristic phrases, and real published examples. Until it is filled, the skill applies the generic LinkedIn norms and the AI-tell pass only.

## STEPS
1. Read references/linkedin-playbook.md for the voice, the current LinkedIn norms, the AI-tell list, and the hashtag method. Read references/provenance.md if it is there.
2. Find the real angle before you draft. State back the one argument you think the post is actually about. IF the user's take wanders across several points OR the surface framing is weaker than a point sitting under it THEN ask which is the true angle, one question at a time, until they confirm it. Do not draft the surface take when a sharper point is underneath.
3. Show the call made last time for each DIMENSIONS choice with one supporting line from references/provenance.md, then ask the user to keep that path or change it.
4. Set the dimensions from their answer. Default length to the feed post unless they say otherwise.
5. Check the date on the playbook's norms section. IF it is more than a few months old THEN search current LinkedIn writing, formatting, and algorithm norms, rewrite what changed in the playbook, and date it, before drafting.
6. Draft from the playbook examples, not from generic AI writing. Open on a person, a specific, or a flat claim that doubles as the hook. Drive it into the one confirmed argument. Carry one extended analogy only if it fits. Land the close in the chosen style.
7. Run the AI-tell pass from the playbook over the draft. Cut every hit.
8. Run the voice check from the playbook. Fix every miss.
9. Research hashtags for this post. Search the current LinkedIn hashtag norms, then search tags for this post's topic. Recommend about three niche on-topic tags for the end of the post, skip the broad generic ones, and flag it when the body never names the terms the classifier needs. Never paste a fixed tag list from memory.
10. Present the draft first, then the recommended tags, then any feedback. Run CHECK before presenting.

## RULES
- This skill governs LinkedIn voice. When it is active, apply these rules and do not defer to the general my-voice skill for LinkedIn output.
- Open with a person, a specific, or a flat claim, never an abstraction or a wish.
- Keep the first two lines a real hook, curiosity read cold, under about 210 characters.
- Use zero em or en dashes.
- Use zero questions and zero exclamations.
- Include at least one ellipsis and at least one parenthetical aside.
- Include at least one signature beat: a CAPS emphasis, a scare quote, or a characteristic phrase from the user's profile.
- Hold one argument across the whole post.
- Keep specifics specific. A real number stays a number.
- Keep the user's stance intact. Never reverse or soften their position inside the draft.
- Match the user's reading level, spelling variant, and register from their voice profile.
- Vary sentence length, short lines next to long ones.
- Use no three-beat list rhythm. Write two items or four instead.
- Find the one real argument before drafting. When the rough take and the strongest point differ, ask which is the true angle rather than drafting the surface version.
- Refresh the playbook norms by search when they are stale, before drafting.
- Research hashtags fresh for each post, the current norms and the topic both, and recommend about three niche tags over broad ones. Never reuse a baked tag list.
- Place hashtags at the end, and never stuff brand names into the body just to feed the classifier.

## EXAMPLES
INPUT:
topic: AI rollouts at work, take: it's never the tech, it's that nobody owns the change
OUTPUT:
Most AI rollouts at work don't fail on the tech. They fail because nobody owns the change.

I've watched it happen... a tool lands, a memo goes out, and everyone waits for someone else to make it real. Six months later it's shelfware, and the postmortem blames the model.

The model was fine. What was missing was ONE person whose job was to drag a single real workflow through it and prove the before and after (the unglamorous part nobody wants).

Buy the tool if you want. But if you don't name the owner, you didn't buy adoption. You bought a license.

Recommended tags (researched for the topic, not baked): #AIAdoption #ChangeManagement #AITransformation

## CHECK
- [ ] the first two lines work as a hook read cold, under about 210 characters
- [ ] zero em or en dashes
- [ ] zero questions, zero exclamations
- [ ] at least one ellipsis and one parenthetical present
- [ ] at least one signature beat present
- [ ] no three-beat list rhythm
- [ ] one argument held throughout
- [ ] reading level, spelling, and register match the user's profile, sentence length varies
- [ ] the user's stance intact, specifics kept specific
- [ ] the close is a position or a concrete image, not a slogan
- [ ] reads like the playbook examples, not generic AI
- [ ] the post argues the one angle the user confirmed, not the surface take
- [ ] the playbook norms were current or refreshed this run
- [ ] hashtags are researched for this topic, about three, niche over broad
- [ ] the body-keyword gap is flagged when the post does not name what the classifier needs
