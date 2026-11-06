# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `rebuttal-guidance`: per-concern peer-review rebuttal guidance built on
  a conditional persuasion model (reviewer mindset X, strategy Y). It
  plans each response rather than writing rebuttal prose.

### Fixed

- Skill docs now cover all twelve skills under `skills/`:
  `skills/README.md`, `skills/README.en.md`, `README.en.md`, `llms.txt`,
  and `CONTRIBUTING.md` list `rebuttal-guidance` and no longer say eleven.

## [2.1.0] - 2026-07-10

### Added

- Added `drawio-reconstruction`, an MIT-licensed skill adapted from
  `sxy1499894281/drawio-reconstruction-skill`, for reconstructing
  reference images into editable Draw.io files with PNG previews and
  visual audits.
- Three skills ported back from our Doubao adaptation practice, where
  they were built and field-tested (all original content):
  - `paper-writer`: evidence-gated drafting of any section or a full
    manuscript. Factual claims trace to the user's materials, verified
    retrieval, or field common knowledge; model memory is never a
    source; delivered prose carries zero placeholder tags; citations
    pass an independent verification ladder (fresh-context sub-agent,
    same-context API grounding, or closed book with disclosure).
  - `paper-polish`: meaning-preserving language polish with a hard
    faithfulness rule (meaning-risk edits are flagged, never silent),
    AI-tone removal, claim calibration, and Chinese-to-English
    rewriting.
  - `deep-research`: survey-grade literature investigation with frozen
    research questions, multi-perspective search, per-citation
    verification (grey zone means unused), MECE synthesis with
    in-sentence cross-comparison, and six internal quality gates.
- `idea-evaluator`: substitute evaluation frameworks for non-STEM
  paradigms (`references/domain-evaluation-frameworks.md`), scoring
  discipline (data-or-mechanism grounds, mechanism-based high scores
  with a named validation experiment), attribution discipline, a
  retrieval-grounded novelty check, and a data-refuted-mechanism
  short-circuit rule.
- `scripts/check_shared_sync.py`: shared reference files are duplicated
  per consuming skill with a canonical header; this checker enforces
  parity.

### Changed

- Repository layout flattened: skills moved from
  `plugins/phd-research/skills/` to top-level `skills/` (the plugin
  nesting was vestigial; no plugin manifest ever existed), the English
  handbook mirror moved from `docs/en/handbook/` to top-level
  `handbook-en/`, and images moved from `assets/images/` to `assets/`.
  All links, the linter, and the sync checker updated; the
  handbook-resync image-rewrite convention now targets `../../assets/`.
- `intro-drafter` now outputs six paragraphs of Introduction prose by
  default (the flowchart becomes an internal scaffold; the classic
  outline remains available on explicit request), never fabricates
  running examples, and inherits the shared evidence discipline.
- `pre-submission-reviewer` gains a paradigm-and-venue-fit step
  (review emphasis switches across STEM, humanities, empirical social
  science, finance/economics, and law), retrieval-grounded novelty and
  citation-completeness checks, an attribution-isolation check, and a
  severity-honesty rule; the integrity gate runs silently.
- `vibe-research-workflow` stance precisified: fabrication is
  forbidden, drafting is not. Drafting requests route to the drafting
  skills under the shared evidence discipline, with disclosure and
  author-verification duties restated.
- Delivery philosophy across evaluator skills: integrity gates run
  silently and surface as findings instead of printed gate reports.

### Fixed

- Restored `## Integrity gate` sections in six SKILL.md files
  (`intro-drafter`, `pre-submission-reviewer`, `figure-designer`,
  `idea-evaluator`, `tech-paper-template`, `vibe-research-workflow`)
  byte-for-byte from commit `6527860~1`; forward references from each
  Step body now resolve.
- Removed orphan closing triple-backtick at EOF of those six files.
- Neutralised eleven references to the nonexistent
  `disruptive-innovation-scout` skill by redirecting to
  `handbook/02_Idea_Generation/2.3`.
- Corrected three stale `../../1_Guide/...` hyperlinks in
  `handbook/03_Paper_Writing/3.2` to use relative `../06_Case_Studies/`.

## [2.0.1] - 2026-04-20

Curriculum re-sync per upstream methodology author. The `handbook/` tree
is re-aligned with the current `HKUSTDial/PhD.Skills/1_Guide/` master,
which had drifted since v2.0.0 (new passages, new figures, renamed PDF).

### Changed

- All 18 handbook MD files re-synced verbatim from upstream. The only
  local edit is an image-path rewrite `../../images/` ->
  `../../assets/images/` to preserve the Supervisor `assets/` layout;
  chapter-local refs (`./assets/5.1_vibe_research/...`,
  `./assets/5.2_meeting_notes/...`) remain as upstream.
- Companion PDF renamed
  `handbook/01_Preliminary/博士生科研入门辅导_2023年8月.pdf` ->
  `博士生科研入门辅导.pdf` to match upstream. All references in
  `README.md` and `README.en.md` updated.
- `assets/images/intro_flowchart_board.png` updated to the current
  upstream revision.

### Added

- 10 image assets under `assets/images/`: `aflow_existing_vs_ours.png`,
  `alpha_sql_solution_overview.png`, `dense_body_layout_example.png`,
  `experiment_canvas_bad.png`, `experiment_canvas_good.png`,
  `lead_solution_overview.png`, `performance_teaser_example.png`, plus
  `.webp` variants for `aflow_solution_overview`,
  `intro_flowchart_alpha_sql`, `intro_flowchart`.
- 11 chapter-local assets for Chapter 5:
  `handbook/05_Vibe_Research/assets/5.1_vibe_research/image1..10.png`
  and `handbook/05_Vibe_Research/assets/5.2_meeting_notes/foundation_agents_vibe_research_overview.png`.

### Unchanged

- `plugins/phd-research/skills/` (seven anchor skills, per v2.0.0
  Guide/Skill decoupling rule).
- `docs/en/handbook/` (English mirror; content-level re-translation
  tracked separately).
- `scripts/`, `.claude-plugin/`, `CONTRIBUTING.md`, `LICENSE`, `llms.txt`.

## [2.0.0] - 2026-04-20

Structural reset per upstream methodology author. The human-readable
curriculum is restored to the original wording and layout from
`HKUSTDial/PhD.Skills` (master branch); the rewritten intermediate docs
shipped in v1.0.0 are removed.

### Changed

- `README.md` reverted to the master-branch narrative of PhD.Skills, with
  a project logo added and the file tree updated to reflect the new
  Supervisor-Skills layout.
- Chinese curriculum promoted from `archive/v1-source/1_Guide/` to the
  top-level `handbook/` directory, preserved verbatim.
- English curriculum re-translated from the restored Chinese handbook
  into `docs/en/handbook/`, replacing the v1.0.0 English overviews.
- License changed from CC BY 4.0 to **CC BY-NC-SA 4.0** to match the
  upstream methodology.

### Removed

- `docs/zh/foundations/`, `docs/zh/skills/*/overview.md`,
  `docs/zh/case-studies/`, `docs/zh/README.md` (intermediate Chinese
  documentation rewritten by the v1.0.0 maintainers).
- `docs/en/foundations/`, `docs/en/skills/*/overview.md`,
  `docs/en/case-studies/`, `docs/en/README.md` (English mirror of the
  removed Chinese docs).
- `archive/v1-source/` (content promoted to `handbook/` or obsolete).
- `README.en.md` v1.0.0 version (replaced by a new English mirror of the
  restored root README).

### Unchanged

- `plugins/phd-research/skills/` (seven anchor skills and their
  `references/`, `SKILL.md`, `HOW-TO-USE.md`).
- `scripts/lint_skills.py`.
- `.claude-plugin/` manifests.

## [1.0.0] - 2026-04-19

Initial public release of `Supervisor-Skills · 博导科研技能包`.

### Included

- Seven anchor skills under `plugins/phd-research/skills/` covering the full
  paper lifecycle:
  - `idea-evaluator`: five-dimension potential analysis, lifecycle-capability
    matching, fatal-flaws audit, paradigm-shift probing.
  - `vibe-research-workflow`: Vibe Coding / Figure / Writing tool choice and
    six behavioural rules.
  - `intro-drafter`: six-paragraph Introduction outline.
  - `tech-paper-template`: technical-paper thinking table plus four
    consistency checks.
  - `benchmark-paper-template`: five-pillar audit, six-part Introduction
    logic chain, Section 2-7 skeleton, and pre-submission checklist.
  - `figure-designer`: paradigm guidance for motivated, overview, and
    experimental figures, plus a universal quality checklist.
  - `pre-submission-reviewer`: five-dimension reviewer self-check with
    severity-tagged findings.
- Bilingual reader guides under `docs/en/` and `docs/zh/` covering paper
  quality foundations, per-skill long-form overviews, and three accepted-paper
  case studies (Alpha-SQL at ICML 2025, AFlow at ICLR 2025, LEAD at VLDB 2026).
- Preserved original Chinese curriculum at `archive/v1-source/`.
- SKILL.md structural linter at `scripts/lint_skills.py`.
- Chinese-primary `README.md` with English mirror `README.en.md`.
- CC BY 4.0 license.
