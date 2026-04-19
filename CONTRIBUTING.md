# Contributing

This repository welcomes issues, pull requests, and discussions. Please read this guide before opening a PR.

## Scope

The v1.0 skill set contains seven anchor skills under `plugins/phd-research/skills/`: `idea-evaluator`, `vibe-research-workflow`, `intro-drafter`, `tech-paper-template`, `benchmark-paper-template`, `figure-designer`, `pre-submission-reviewer`. Adding a new skill requires:

1. Discussion via issue first; confirm the skill fills a real gap and is not covered by an existing skill.
2. Clear attribution for any content not derived from `archive/v1-source/`.
3. Adherence to the SKILL.md conventions below.

## Authoring a skill

Each skill directory at `plugins/phd-research/skills/<name>/` contains:

- `SKILL.md`, English, under 500 lines, with YAML frontmatter (`name`, `description`, optional `license`).
- `references/*.md`, on-demand depth. Files over 100 lines must begin with a table of contents.
- Optional `scripts/*.py` for deterministic helpers and `assets/*` for templates.

## Hard rules (enforced by CI)

- SKILL.md body under 500 lines.
- `description` between 40 and 80 words, written in third person, contains at least one "Use when..." clause.
- No em-dash (U+2014) in `SKILL.md` or `references/*.md`; use commas or periods.
- No Chinese characters in SKILL.md (bilingual content lives in `docs/zh/`).
- All `See: references/X.md` pointers must resolve to existing files.
- No nested references (`SKILL.md -> refs/a.md -> refs/b.md` is illegal).
- Commits must not contain "Claude", "Co-Authored-By: Claude", or Anthropic attribution.

## Running the linter

```bash
python scripts/lint_skills.py
```

The linter exits non-zero on any violation and is invoked by `.github/workflows/lint.yml` on every PR.

## Bilingual content

Canonical `docs/en/` is authored first; `docs/zh/` mirrors the structure and content. CI blocks merges that leave the two trees asymmetric.

## License

All contributions are licensed under CC BY 4.0. By submitting a PR you agree to license your contribution under these terms and to provide attribution consistent with the original repository's convention.

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
