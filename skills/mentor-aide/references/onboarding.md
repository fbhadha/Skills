# Onboarding: set up mentor-aide for your workplace

The mentor-aide skill guides mentors through a TPM or technical-to-business career transition, but it needs to know how career paths work at *your* company. Before you use the skill, run this onboarding. It takes about 20-30 minutes and produces a single file that teaches the skill your workplace's career system.

## What we're collecting

You know how people move up in your organization. When do they move? What titles are on the path? What do people actually need to do to get from here to there? That knowledge is what the skill uses to coach mentees. If you do not fill this in, the skill will fall back to generic career advice, which rarely fits.

## Step 1 — Gather your input

Take 15 minutes and answer these questions in your head (or jot notes):

1. **The career path itself.** What are the stops a person takes from where they start to where you are now? What comes after? What are the actual names of the titles, levels, or roles?

2. **What people do to move up.** You have watched people make this move. What did they actually do? Not what the handbook says, but what worked. Did they do the job before they had the title? Did they need to find a sponsor? Did they change teams? What got them visible? What got them trusted?

3. **The obstacles.** What trips people up? What do people get wrong? When does someone hit a ceiling? What do people misunderstand about the move?

4. **The timeline.** How long does it take? Is it always the same, or does it vary? Does the timeline depend on the team, the person, the market, or the luck of having an opening?

5. **The sponsor and opening problem.** Can someone do everything right and still not move? Do they need a sponsor lined up first? Do they need an opening to exist? When did you make the move, and what had to be in place?

6. **What you wish you knew.** Looking back on your own move or watching others, what would have helped? What would you tell someone starting out?

These are conversation-starters, not a form. The skill will ask you to riff on them.

## Step 2 — Have the interview

You are going to talk through this with Claude in a structured way. Claude will ask you one question at a time and listen. Expect 8-12 exchanges. This is a deliberate pace on purpose — you cannot download what you know in a paragraph, and the skill cannot learn it from one big lump. Claude will:

1. Ask each question above, one at a time.
2. Listen to your answer and ask one follow-up if something is missing or unclear.
3. Repeat, with a short summary between sections so you can course-correct.
4. At the end, show you a draft of what the skill will use. You will correct it, sharpen it, or expand it until it rings true.

Do not prepare a speech. Just answer the questions as they come.

## Step 3 — Validate and finalize

Claude will produce a file called `references/workplace-career-paths.md`. Read it. Does it sound right? Does it capture how career moves work at your place? If something feels wrong, off-key, or missing, say so, and Claude will fix it.

The file becomes part of the skill. The skill will read it at the start of every mentor engagement and use it to coach. If your workplace changes (new structure, new paths, new obstacles), regenerate this about once a year. The rest of the skill is stable and does not need updates.

## What happens next

Once this file exists, mentor-aide is ready to use. When you run a new engagement, the skill will ask whether the mentee is making the jump (working toward the title) or already has it. From there, it coaches differently. Throughout, it will pull on this file to stay grounded in how moves *actually* work at your company, not in generic best practices.

Your workplace is not like other workplaces. This file is what makes the skill useful.
