# Provenance: publish-skill

Captured from a conversation on 2026-06-17. Source task: building an open source skills marketplace repo for Claude and adding several packaged skills to it.

## Dimensions and the calls made

### folder_convention
Options weighed: standardize to the spec folders, preserve the author folders.
The call last time: standardize to the spec.
Why: the user wants every published skill to use the same scripts, references, and assets layout so the repo stays consistent and installs cleanly everywhere.
In their words: "Standardize to spec".

### delivery
Options weighed: open a pull request, commit and push straight to a branch.
The call last time: open a pull request.
Why: a public repo takes outside contributions, so a pull request gives a review gate before anything lands.
In their words: "Open a pull request".

## Quality gates and the reasoning behind them

### sanitization
The standard: no personal or sensitive data goes public. Emails, keys, secrets, real names, and internal company or project names all come out first.
Why it mattered: the repo is open source, so anything left in a skill is published to the world and cannot be pulled back once it is indexed.

### security review
The standard: bundled scripts are read and cleared before the skill is added, with anything that fetches and runs remote code or sends out data rejected.
Why it mattered: skills carry executable code and backdoored skills have turned up in the wild, so the review is the real gate, and the frontmatter check is not enough on its own.

### frontmatter validity
The standard: name and description follow the Agent Skills rules and the name matches the folder, or the skill will not load.
Why it mattered: a skill that breaks the platform limits cannot be installed, so this is the last gate before it ships.

## Branches tried and dropped

- Standardizing the reference folder to the singular name: dropped after checking the source, since the Anthropic skill and the standard both use references in the plural. A guess on a convention cost a round trip, so check the source before renaming.
- Packaging as a plain zip with SKILL.md at the archive root: dropped because the skill own convention and the installer expect a .skill built by package_skill.py, which nests everything under the skill folder.
- Preserving the author folders as the default: weighed because it is the safe move for someone else content, but the user chose standardize so the repo stays uniform. Honour the dimension and ask when unsure.

## Notes for future updates

The sanitization step is the one to keep sharp. As skills come from more sources, the kinds of sensitive data will grow, so widen the scan over time. The folder_convention default is standardize here, but the preserve path still matters for skills where a rename would break internal references, so keep both alive.
