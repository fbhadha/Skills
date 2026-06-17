---
name: publish-skill
description: Take a finished skill and publish it into a public GitHub skills marketplace repo for Claude. Use when the user wants to add, contribute, open source, or share a skill, with phrases like publish this skill, add it to the marketplace, open source this skill, contribute this to the repo, or here is a .skill file to add. It unpacks the skill, validates the frontmatter against the Agent Skills standard, sanitizes out personal and sensitive information, runs a security review of any bundled scripts, standardizes the folder layout, registers the skill in marketplace.json and the README catalog, and opens a pull request. Trigger even when the user does not say publish, as long as they hand over a skill meant to go into a shared repo.
license: MIT
metadata:
  distilled: true
---

# publish-skill
TASK: Publish a given skill into a public GitHub skills marketplace repo, validated, sanitized, security-reviewed, and delivered as a pull request.

## INPUT
skill_source: a .skill or .zip file, a skill folder, or a path to one
repo: the target GitHub marketplace repo, as owner/name
branch: the base branch to target

## DIMENSIONS
folder_convention: standardize | preserve
delivery: pull-request | commit-push

## OUTPUT
The skill added under skills/<name>/ in the target repo, registered in .claude-plugin/marketplace.json and the README catalog, passing the repo validator, carrying no personal or sensitive data and no unsafe scripts, delivered as a pull request, or a pushed branch when delivery is commit-push.

## STEPS
1. Surface each DIMENSIONS choice to the user. IF references/provenance.md is readable THEN show the call made last time and one supporting quote for each. Ask the user to keep that path or adjust it. Set folder_convention and delivery from the answers.
2. Unpack skill_source. IF it is a .skill or .zip THEN extract it. Locate SKILL.md and treat its parent folder as the skill folder. Read every file in the folder.
3. Validate frontmatter against the Agent Skills standard. name is lowercase letters numbers and hyphens, 64 characters or fewer, contains neither anthropic nor claude, and equals the folder name. description is non-empty and 1024 characters or fewer. The value carries no angle brackets, and no colon followed by a space unless the whole value is quoted. Allowed keys are name, description, license, allowed-tools, metadata, compatibility. Fix what you can and stop on what you cannot.
4. Sanitize. Scan every file for personal and sensitive data: email addresses, phone numbers, real personal names, API keys, tokens, passwords, secrets, internal company or project names, and absolute paths that carry a username. Replace each with a variable or a placeholder, or remove it. Never publish a skill that still carries any of these. Where a removal would change the method, ask the user before cutting.
5. Security review. Scan scripts and any executable file for fetch-and-execute, meaning curl or wget piped into sh or bash, for eval of a command substitution, for rm -rf on a root path, and for any code that sends files or environment data to a third party. Reject obfuscated or remote-execution code. Require a clean pass before continuing.
6. Set the folder layout. IF folder_convention is standardize THEN rename non-spec folders to the spec names scripts, references, and assets, and update every path reference inside the files to match. ELSE keep the author folders and list each deviation for the reviewer.
7. Place the folder at skills/<name>/ in a clone of the target repo.
8. Register the skill. Add ./skills/<name> to the skills array of the plugin entry in .claude-plugin/marketplace.json. Confirm the file still parses as JSON.
9. Update the README catalog. Add one row with the skill name linked to its folder and a one-line description drawn from the frontmatter.
10. Run the repo validator if it is present, scripts/validate_skills.py, and fix what it flags.
11. Deliver. Create a branch. Stage the changes. Commit with a sign-off, git commit -s, and a clear message. Push the branch. IF delivery is pull-request THEN open a pull request against the base branch. ELSE leave the pushed branch.
12. Run CHECK before reporting.

## RULES
- Never publish a skill that still carries personal or sensitive data.
- name equals the folder name and contains neither anthropic nor claude.
- Sign every commit with git commit -s.
- Rename author folders only when folder_convention is standardize, and when you do, update every path reference too.
- Reject any script that fetches and executes remote code or sends out data.
- Sanitize only the sensitive data, never the method or the author voice.
- Do not open a pull request against a repo the user has not named as the target.

## EXAMPLES
INPUT:
skill_source: weekly-review.skill, repo: acme/skills, branch: main, folder_convention: standardize, delivery: pull-request
OUTPUT:
The weekly-review skill extracted, frontmatter validated, a contributor email and an internal project name replaced with variables, scripts reviewed clean, a templates folder renamed to assets with its path references fixed, the folder placed at skills/weekly-review/, registered in marketplace.json and the README, the validator passing, and a pull request opened against main from a signed commit.

## CHECK
- [ ] frontmatter valid, name matches the folder, no reserved words
- [ ] no personal or sensitive data remains in any file
- [ ] scripts reviewed, nothing fetches and executes or sends out data
- [ ] folder layout matches the chosen convention with path references intact
- [ ] registered in marketplace.json, which still parses as JSON, and in the README catalog
- [ ] repo validator passes
- [ ] delivered as a pull request, or a pushed branch when commit-push, from a signed commit
