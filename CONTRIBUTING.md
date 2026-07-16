# Contributing

This repository welcomes issues, pull requests, and discussions. Please read this guide before opening a PR.

## Scope

The current skill set contains twelve anchor skills under `skills/`: `idea-evaluator`, `deep-research`, `vibe-research-workflow`, `intro-drafter`, `paper-writer`, `tech-paper-template`, `write-top-tier-ml-paper`, `benchmark-paper-template`, `paper-polish`, `figure-designer`, `drawio-reconstruction`, `pre-submission-reviewer`. Adding a new skill requires:

1. Discussion via issue first; confirm the skill fills a real gap and is not covered by an existing skill.
2. Clear attribution for any content not derived from `handbook/`.
3. Adherence to the SKILL.md conventions below.

## Authoring a skill

Each skill directory at `skills/<name>/` contains:

- `SKILL.md`, English, under 500 lines, with YAML frontmatter (`name`, `description`, optional `license`).
- `references/*.md`, on-demand depth. Files over 100 lines must begin with a table of contents.
- Optional `scripts/*.py` for deterministic helpers and `assets/*` for templates.

## Hard rules (enforced by CI)

- SKILL.md body under 500 lines.
- `description` between 40 and 80 words, written in third person, contains at least one "Use when..." clause.
- No em-dash (U+2014) in `SKILL.md` or `references/*.md`; use commas or periods.
- No Chinese characters in SKILL.md (the canonical Chinese curriculum lives at `handbook/`; English mirror at `handbook-en/`).
- All `See: references/X.md` pointers must resolve to existing files.
- No nested references (`SKILL.md -> refs/a.md -> refs/b.md` is illegal).
- Reference files shared across skills are duplicated per consuming skill (skills stay self-contained); each copy carries a header naming its canonical, and copies must stay byte-identical to the canonical below the header (`python scripts/check_shared_sync.py`).
- Commits must not contain "Claude", "Co-Authored-By: Claude", or Anthropic attribution.

## Running the linter

```bash
python scripts/lint_skills.py
python scripts/check_shared_sync.py
```

The linter exits non-zero on any violation and is invoked by `.github/workflows/lint.yml` on every PR.

## Bilingual content

The Chinese `handbook/` is the canonical curriculum, preserved verbatim from the methodology author. The `handbook-en/` directory is a faithful English mirror and follows the same chapter and file structure. Keep the two trees symmetric in any PR that edits the curriculum.

When re-syncing `handbook/` from upstream `HKUSTDial/PhD.Skills`, the only permitted local edit remains the image-path rewrite; its target is now `../../assets/` (images sit directly under `assets/`, no `images/` subfolder). Chapter-local asset references (`./assets/...`) stay as upstream.

## License

All contributions are licensed under CC BY-NC-SA 4.0. By submitting a PR you agree to license your contribution under these terms and to provide attribution consistent with the original repository's convention.

## Commit conventions

Conventional Commits:
- `feat(skill): <name> ...` for new skills
- `feat(<area>): ...` for new non-skill features
- `fix(<area>): ...` for bug fixes
- `docs(<area>): ...` for documentation
- `build: ...` for build system, CI, tooling
- `chore: ...` for routine maintenance
- `refactor(<area>): ...` for refactoring

Commits must not include any Claude or Anthropic attribution.
