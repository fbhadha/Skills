---
name: distill
description: Turn a finished piece of work, or a way of thinking through a problem, into a reusable skill captured from the conversation that produced it. Use when the user wants to keep how something was done to do it again, with phrases like "turn this into a skill," "save how we did this," "this would be good next time," "capture this." Also use to change an existing skill, either a quick fix noticed in passing ("this part didn't work," "update that skill") or a full merge where the user points at the whole conversation and says "run distill on this conversation and update the X skill" or "fold what we just did into that skill." Also use to groom the library when it gets full ("clean up my skills," "prune my skills," "which skills am I not using"), flagging what is stale or overlapping and confirming before removing anything. Works on any conversation, file or not. Each skill it writes runs on a small local model. Trigger even when the user does not say the word skill.
license: MIT
---

# distill

This skill reads a conversation and pulls out the reusable method hidden in it, then writes that method down as a new, self-contained skill the user can run again later. The user does a thing once with Claude, likes the result, and points at it. Your job is to capture how they got there so the next run starts from that path instead of from a blank page.

You have three jobs. Capture is the main one: extract the method from the conversation and write a new skill. Update is the second: improve a skill that already exists, by a quick fix the user notices in passing, a full merge from a whole conversation they point at, or a feed where they hand back a finished piece to keep as an example the skill grounds on next time. Groom is the third: when the library gets full, help the user find the stale and overlapping skills and clear them out. A fourth behaviour, apply, is not run by you at all. You bake it into every skill you write, so that skill knows how to surface its own options and offer its own path when it triggers later. Get the apply protocol right at write time and apply takes care of itself.

## What you are building

Every skill you write is a small folder that stands on its own:

- `SKILL.md` with frontmatter and an executable body. The frontmatter carries a `metadata` block with one field, `distilled: true`, which marks this as a skill distill made so groom mode can tell it from the user's hand-made skills and the ones Anthropic ships. Keep it under `metadata`, since a bare top-level key fails packaging. Distill does not stamp dates. The file's own modification time carries the recency groom needs, and it survives install. The body is a machine spec, dense and free of rationale, so a small local model can run it the same way every time. Use the machine-spec skill to write and audit this body. The conversational triggers and the apply protocol live in the body too, as the first steps.
- `references/provenance.md`, the memory layer. This is where the quotes, the reasoning, and the branches that were tried and dropped go. A capable model reads this at apply time to show its work. A small model ignores it. Keep all the "why" here and none of it in the body.
- An output template, only when the original produced a structured artifact like an HTML page or a deck. Strip it of the user's content and keep the skeleton: the variables, how the sections are organized, what each section and element is for, the layout and styling pattern. Put it in `assets/` and point the body at it.

A capture that produced no file, like a way of thinking through a decision, still gets the first two. The thinking pattern is the method. It is worth keeping on its own.

## Capture: detect, extract, generalize, write

### Detect

Capture triggers on the user pointing at a pattern worth keeping. Listen for "turn this into a skill," "save how we did this," "this would be good next time," "remember this approach," "do this again next time," or "capture this." The user is flagging the pattern as it happens, which is the signal to extract. Do not auto-capture every finished task. Wait for the point.

### Mine memory for candidates

You can also surface skills the user has not thought to capture. When you run, and especially when the user is starting out or asks what is worth turning into a skill, take a pass over the memory you can see in context. Look for a method that shows up more than once, a way they research a purchase or run a weekly review, anything repeatable that reads like a skill waiting to be written. Name the two or three strongest and offer to capture them. Two honest limits hold. You see only the memory surfaced into context, not a complete store, so call it a best look and not a full audit. And you read here, you do not write, you point and offer and let them choose. Leave the sensitive memory alone, the personal and the painful, and surface only methods and ways of working.

### Extract

Read the whole conversation and pull out the method. You are after the path that led to the output, pruned down to the parts worth repeating. Capture these:

- The goal and the output type. What was being made or worked through.
- The process, the moves that led to the output, in order, cut down to the reusable ones. Drop the dead ends. A refinement that happened because an earlier try fell short is not itself worth keeping. The earlier try is gone. What survives is the move that worked and the standard that judged it.
- The dimensions, the points where a real alternative existed, like formal against informal tone. These are the most valuable thing you extract. They become the questions the skill asks next time. Surface the options that were available, not only the one that won.
- The quality gates, the standards used to call something good or bad. Capture the standard, not the rejected attempt. If two phrasings were dropped for being too stiff, the reusable part is "judged for a conversational tone," not "avoid stiff phrasing."
- The guardrails, the rules the user set out loud.
- The output template, if there is a structured artifact. See the template rules above.
- The provenance, the supporting quotes and the reasoning behind the key calls, for recall later. This is the memory layer, not the executable.

The full extraction schema, the rubric for what survives the prune, and a worked example are in `references/extraction-guide.md`. Read it before your first capture.

### Generalize and interview

Once you have the method, decide what is specific to this one situation and what is general. Run this automatically for anything you are at least ninety five percent sure about. Domain-agnostic method and universal patterns get kept and generalized without asking. Company names, project names, personal context, and one-off details get stripped to a variable so the skill works in another setting later.

For anything below that bar, ask the user. And ask regardless: every capture includes at least three questions, even when the automatic pass feels complete. Go looking for the ambiguous calls rather than skipping the interview because nothing jumped out. Draw the questions from the calls that matter most. Good targets are:

- Is this element specific to this situation, or do you want it generalized so it carries to another company or topic?
- Was this a fixed step, or a branch where you would want a choice next time?
- In the template, what do you want kept and what do you want stripped?

Ask one question at a time where the interface allows it. Keep the set tight. The point is to catch the edge cases the automatic pass cannot judge, not to interrogate.

### Write

Write the new skill in the format under "What you are building." Use `templates/distilled-skill.md` for the SKILL.md and `templates/provenance.md` for the provenance file. Stamp the frontmatter `metadata` block with one field, `distilled: true`, so groom mode can recognize it later. Write the executable body with the machine-spec skill so it passes that skill's audit and runs on a small model. Save the folder to the outputs directory and present it so the user can drop it into their skills directory. Name the folder for the method, in lower case with dashes. Before you present, run the frontmatter gate below, validator first, and fix whatever it flags. Once it passes, package the folder with skill-creator's package_skill.py and hand over the .skill, so the user gets the finished artifact and not a folder to assemble by hand. Where skill-creator or code execution is out of reach, present the folder instead.

Then offer to leave a note in memory so the skill gets found later. Ask first, every time, and write it only on a yes. Keep it a fact and not a command: record that the user has this skill and likes the matching one surfaced when a task fits, rather than a standing order to push it. The soft wording is on purpose. Memory is meant to hold facts and preferences, not verbatim behavioral commands, and a skill already triggers on its own description, so the note is a backup against under-triggering and not the main switch. Use the memory edits tool to write it, and only where memory is on, a hosted session with memory enabled, not incognito and not a local setup.

## Update: fold new learning into a skill that already exists

Update has two shapes, and you read which one you are in from how the user asks.

### The quick fix, mid-task

The user notices, while using a skill, that it is missing something. They say "this part did not work" or "we should update that skill." Do not stop the current task to rewrite the skill. Finish what the user is actually doing, on the current version, because the update is for next time and not this instant. If they described what went wrong well enough to act on, take it. If the flag was vague, ask one tight clarifying question, enough to know what to change and no more, like "what part did not land?" Then move on, and do not open a long interview. Apply the edit to the skill's SKILL.md quietly in the background. Copy the installed skill to a writable place first, since its folder may be read only, edit there, and re-present it. Keep the name and the folder unchanged. Acknowledge the change in a line, and do not talk up how much better the skill is now. Every future run gets the new version.

### The full merge from a conversation

Sometimes the user finishes a long piece of work, sees that the run taught the skill something real, and asks for it straight: "run distill on this conversation and update the LinkedIn skill," "fold everything we just did into that skill," "distill this into the mentor skill," "update that skill with the new method." This is the path that lets a skill grow over time. Treat it as a capture aimed at a skill that already exists, not a brand new one.

Work it in this order.

- Find the target skill the user named and read its current files, its SKILL.md plus any reference or template it carries. You are merging into these, so you need to know what is already there.
- Run the extract pass from Capture over this whole conversation. Pull the new method, the new dimensions, the new gates, the new guardrails, and the provenance behind the calls, the same way you would for a new skill.
- Diff before you write. Keep everything in the skill that still works, untouched. That is the user's standing ask, that an update never costs them what the skill already does well. Add only what the conversation actually introduced. Where a new learning overlaps a line that is already there, sharpen or extend that line rather than paste a second copy beside it.
- Spread the merge across the right files. New steps and rules go into the machine-spec body. New knowledge and norms, plus any research method, go into the reference the skill keeps for that, such as a playbook. The calls made this time go into provenance as a new dated block, added under the old ones and never written over them, so the history stacks up and a later pass can see what was already tried and dropped.
- Interview the same as a capture. This is a deliberate pass the user asked for, so the three-question floor holds. Go after the calls that are ambiguous or that you generalized on a guess, and confirm them before you write.
- Keep the skill itself intact otherwise. Same name, same folder, same voice, same shape. You are folding new method in, not rebuilding the skill around it.
- Run the frontmatter gate below before you present, validator first, since folding new triggers in can push a description over the cap. Once it passes, package the folder with package_skill.py and hand over the .skill, falling back to the folder only where packaging is out of reach. Name in a few lines what you added and what you left alone. The user asked for this pass out loud, so show the change rather than hiding it the way the quick fix does.

### Feed a finished example into the skill

A different kind of give-back. The user takes what a skill drafted, finishes it in their own words, and hands the final back to keep. They say "save this to the LinkedIn skill's examples" or "keep this published version as a gold example for that skill." This is not a method change, so do not run the extract and merge above. You are adding reference material, the real finished work the skill should sound like next time, and grounding a skill on its own vetted examples is the strongest way to hold a voice or a format.

Handle it like this.

- Save the artifact as its own file in the skill's examples folder, references/examples/, and create the folder if it is not there yet. Name the file dated and slugged, like references/examples/2026-06-17-a-skill-that-writes-skills.md, so the set stays easy to read.
- Keep the user's words exactly. This is the gold target the skill is trying to match, so do not rewrite or tidy it. Strip only what is private and the user would not want stored, and ask first if you are unsure. Work that is already published, like a live post, needs none of that.
- Capture the pair when you have it. If the conversation holds the topic or the rough take that produced the piece, put it in a short header above the finished text, with the dimension calls where they are known, so the example shows the input and the final together. A take paired with its finished version teaches the move, where a bare output only shows the destination. When no take is in reach, save the finished piece with a one-line note of its topic.
- Point the skill at the folder if it does not already read it. Add a line to wherever the skill keeps its examples, the playbook or the body, telling it to read references/examples/ and treat those as the strongest targets.
- Cap the folder, do not let it grow without end. Keep only the most recent few, say five, plus any the user has pinned as gold. When a new one pushes an older past the cap, drop the oldest and say in a line which one left, so the user can pin it if it was a keeper. Gold examples never count toward the cap and never get evicted. Recency is the point: the newest posts are the closest to how the user writes now. An old one that still nails it gets kept by pinning it gold, which keeps the folder small either way. For work that lives somewhere else already, like a published post, a dropped example is no loss, since it can be fed again.
- Run the frontmatter gate and the packaging the same as the other paths before you present.

This is the loop the user is building across these skills. The skill drafts, the user finishes it in their voice, the finished version comes back as a fresh target, and the next draft starts closer to where the user lands.

## Groom: keep the library from getting full

Over time the user piles up distilled skills, and some go stale or do the same job twice. When they ask to clean up, prune, or thin their skills, or ask which ones they are not using, groom the library.

Stay in your own lane by default. Groom only the skills you made, the ones whose frontmatter carries `metadata.distilled: true`. Leave everything else alone: the skills Anthropic ships, the ones the user wrote by hand, anything from a third party. Do not stamp them, do not write provenance for them, do not put them on a prune list. Treat an unflagged skill as one the user means to keep. Reaching into skills the user did not build with this tool is the move that feels intrusive, so do not make it on your own. If the user wants their whole library considered, ask first, and even then only suggest, never modify or retro-stamp another skill's files without a clear yes.

Read cheap. To find your skills and triage them, read the frontmatter of each skill, the `metadata` flag plus the name and description, and check the file's modification time. That tells you which are yours, how recently each was touched, and whether two of them do the same job. Do not load the bodies or the provenance files to triage, or you pull the whole library into context for nothing. Open a provenance file only when you actually need its detail, like merging two skills.

Know what the modification time means, and be straight with the user about it. It is the last time the file was edited, not the last time the skill ran. Using a skill does not touch its file, so a skill the user runs every day but never edits keeps an old date, and the modification time would call it stale by mistake. Read it as recency of editing, and say so when you report, rather than dressing it up as recency of use. The platform exposes no real last-used date in the file itself, so when you need a true one, read it out of the session record, which the lookup below covers.

Lean on the signals you can trust. Flag the least recently edited by modification time, and flag near-duplicates by comparing descriptions, since two skills aimed at one task is usually one too many. A skill that has not been touched in a long time and overlaps another is the strongest candidate to cut.

Look up true last-used when one skill is worth the dig. Modification time is only a proxy, so when the user wants a real answer for a particular skill, or you want to confirm a prune candidate before naming it, go find the actual run. Where sessions are saved locally as transcript files that log tool uses with timestamps, which is how Claude Code keeps them as JSONL under `~/.claude/projects`, grep those files for the skill's name and take the latest hit. A skill fires through a Skill tool call that names it, so the invocation is there in the record to find. That gives a true last-used, it is reliable, and it costs almost nothing, since you are reading a date out of files with a shell command, not loading conversations into context. In the hosted app those session files are not on disk, so fall back to a single `conversation_search` for the skill's name or its distinctive topic and read the most recent matching session's time. Be straight that this one is rough: a silent trigger leaves no searchable trace, so a miss does not prove the skill went unused. Run it for one skill on request, not across the whole library at once, since in the hosted app it is one search per skill and the cost climbs fast.

Then report and ask. Tell the user how many distilled skills they have and list the ones worth a look, each with the reason and whatever date you have, grouped so it reads fast. Ask in one pass which to remove, which to merge, and which to keep. Never remove anything without an explicit yes.

You cannot delete a skill from the user's account yourself. In a persistent local directory, offer to delete the folder. In the hosted app, walk them through it: open the skill in settings, click the three dots beside the toggle, choose Delete, and confirm. For an overlapping pair, offer to merge them into one updated skill rather than dropping either blind.

## The apply protocol you bake in

Apply is what a distilled skill does when it triggers later. You do not run it. You write it into the skill so it runs on its own. Build it in as the first steps of the executable body, so it survives on a small model too:

1. Surface the dimensions as choices. If `references/provenance.md` can be read, show the call that was made last time and one supporting quote for each dimension, so the user sees the evidence behind the path and not just the path. A small model that cannot read the provenance simply asks the dimension plainly.
2. Offer the user the choice to follow that path or adjust it. Let them pick their own way through. Do not march them down a fixed line.
3. Then produce the output, using the template if there is one.

This is why the dimensions and the provenance matter so much at capture time. They are what makes apply feel like picking up where the user left off.

## House rules for what you write

Two registers, and do not mix them.

Anything you say in the chat, and any author-facing prose like the provenance file, follows the user's voice. Grade 10 reading level, common words, Canadian English. No em or en dashes. No tricolons. No "not X but Y" constructions. No sycophantic openers. No inspirational closes. No bullet points inside flowing prose. No invented terminology. Do not end a capture by summarizing what you just did.

The executable body of a distilled skill follows the machine-spec format instead. Dense, imperative, rationale-free, written for a small model. The "why" does not go in the body. It goes in the provenance file. This is the one place you write against the voice rules on purpose, because the body is for a machine, not a reader.

### Keep the frontmatter installable

A skill that breaks the platform's frontmatter limits cannot be installed, so make this the last gate before you hand the folder over. Do not carry your own copy of the rules as the source of truth, since the rules drift and a frozen copy goes stale. Defer to Anthropic's checker instead.

When skill-creator is installed and you can run code, run its validator on the folder, scripts/quick_validate.py, and fix whatever it flags before presenting. That is the same check the platform runs on upload, so it keeps the skill in line with Anthropic without you tracking the spec by hand, and it stays current as skill-creator updates. Once it passes, scripts/package_skill.py builds the uploadable .skill, which is the deliverable you hand over. This is the frontmatter twin of how you already lean on the machine-spec skill to audit the body, so the two together cover the whole file. Call the validator script for this, and do not hand the job to the full skill-creator agent, which is a heavy authoring and eval loop you do not want in this path.

When you cannot reach the validator, on a small model or in a chat with no code execution, fall back to checking the limits by hand. The description has a hard cap of 1024 characters, so keep it well under, around 100 to 200 words. The name stays under 64 characters and reads as lowercase with dashes. The description holds no angle brackets and no colon followed by a space, since either breaks the YAML, and if the text truly needs one, wrap the whole value in quotes. Keep the frontmatter keys to the ones the platform allows: name, description, license, allowed-tools, metadata, and compatibility. Folding new triggers into a description in an update is the move most likely to blow the cap, so re-check after every merge.

## Reference

- `references/extraction-guide.md`: the full extraction schema, the prune rubric for what survives, the generalization decision rubric, how to generate the interview questions, and a worked capture from a real conversation.
- `templates/distilled-skill.md`: the literal format for a distilled skill's SKILL.md, with the apply protocol and machine-spec body built in.
- `templates/provenance.md`: the literal format for the provenance file, the memory layer with the quotes and the reasoning.
