# Supervisor-Skills, reader curriculum

This tree is the human-facing counterpart to the skill package. It distils
a PhD-level academic research curriculum into a skill-indexed set of English
reader guides that stand on their own, independent of any AI assistant.
Every chapter in this tree maps to a SKILL.md file under
`plugins/phd-research/skills/`; the guides teach the methodology, the
SKILL.md files execute it.

The curriculum covers the full lifecycles of both technical and benchmark
papers targeted at NeurIPS, ICML, ICLR, VLDB, SIGMOD, KDD, or a similar top
venue. Technical and position papers walk from idea vetting and disruptive
innovation scouting, through paper structuring and figure design, to
pre-submission review. Benchmark and evaluation papers walk from evaluation
gap analysis, through benchmark design, data construction, experiments,
paper structure, and a pre-submission checklist. Both lifecycles live in
the same skill package; the two pipelines stay distinct, and `bench-writing`
orchestrates the benchmark stages as a DAG.

## Recommended reading path

A PhD student starting their first top-venue paper should read in this order:

- [Foundations: paper quality (4N)](foundations/paper-quality.md), the rubric
  the rest of the curriculum sits on.
- [Idea Evaluator](skills/idea-evaluator/overview.md), to kill weak ideas
  early and shape promising ones before committing months.
- [Disruptive Innovation Scout](skills/disruptive-innovation-scout/overview.md),
  when the evaluator's paradigm probe flags disruptive potential.
- [Tech Paper Template](skills/tech-paper-template/overview.md), to lock the
  full logical skeleton before drafting any prose.
- [Intro Drafter](skills/intro-drafter/overview.md), to turn the skeleton
  into a six-paragraph Introduction outline.
- [Figure Designer](skills/figure-designer/overview.md), to plan the three
  figures that carry the paper's storytelling weight.
- [Pre-Submission Reviewer](skills/pre-submission-reviewer/overview.md), for
  the three-to-five-day deadline window audit.
- [Case studies](#case-studies), to see the framework applied to real
  published work.

For AI-assisted workflow at any stage, read
[Vibe Research Workflow](skills/vibe-research-workflow/overview.md). It is
orthogonal to the writing pipeline rather than sequential: the rules and
tool selections apply whether a student is coding, drawing, or writing.

For a benchmark or evaluation paper, the reading order is different. The
benchmark pipeline is more tightly sequential than the technical-paper
track, with each stage gated on its predecessor, and the orchestrator
surfaces the whole pipeline up front:

- [Bench Writing orchestrator](skills/bench-writing/overview.md), which
  detects the current stage and routes to the right sub-skill.
- [Bench Gap Analysis](skills/bench-gap-analysis/overview.md), to locate
  the evaluation blind spot that motivates the benchmark.
- [Bench Design](skills/bench-design/overview.md), for the architecture:
  goals, scope, taxonomy, evaluation framework, optional companion method.
- [Bench Construction](skills/bench-construction/overview.md), for the
  data pipeline with quality gates and statistical profiling.
- [Bench Experiments](skills/bench-experiments/overview.md), for the
  experiment plan centred on Finding-X style insights.
- [Bench Paper Structure](skills/bench-paper-structure/overview.md), for
  the Introduction six-part flowchart and section layout.
- [Bench Checklist](skills/bench-checklist/overview.md), for the
  pre-submission gate.

Readers who already have a specific bottleneck can skip the reading order and
jump directly to the matching chapter. For example, a student whose
Introduction flowchart is broken should go straight to
[Intro Drafter](skills/intro-drafter/overview.md); a student debating which
figure tool to use should go straight to
[Figure Designer](skills/figure-designer/overview.md); a student unsure
where the benchmark gap actually lies should go straight to
[Bench Gap Analysis](skills/bench-gap-analysis/overview.md).

## Jump-to index

### Foundations

- [Paper quality: the 4N framework](foundations/paper-quality.md)

### Technical paper skills

- [Idea Evaluator](skills/idea-evaluator/overview.md)
- [Disruptive Innovation Scout](skills/disruptive-innovation-scout/overview.md)
- [Intro Drafter](skills/intro-drafter/overview.md)
- [Tech Paper Template](skills/tech-paper-template/overview.md)
- [Figure Designer](skills/figure-designer/overview.md)
- [Pre-Submission Reviewer](skills/pre-submission-reviewer/overview.md)
- [Vibe Research Workflow](skills/vibe-research-workflow/overview.md)

### Benchmark paper skills

- [Bench Writing (orchestrator)](skills/bench-writing/overview.md)
- [Bench Gap Analysis](skills/bench-gap-analysis/overview.md)
- [Bench Design](skills/bench-design/overview.md)
- [Bench Construction](skills/bench-construction/overview.md)
- [Bench Experiments](skills/bench-experiments/overview.md)
- [Bench Paper Structure](skills/bench-paper-structure/overview.md)
- [Bench Checklist](skills/bench-checklist/overview.md)

### Case studies

- [ICML 2025, Alpha-SQL writing analysis](case-studies/alpha-sql.md)
- [ICLR 2025, AFlow writing analysis](case-studies/aflow.md)
- [VLDB 2026, LEAD writing analysis](case-studies/lead.md)

## How to use this alongside an AI assistant

Each skill's SKILL.md file is a self-contained structured instruction that
plugs directly into any AI assistant. Install details live in the top-level
[README](../../README.md#quick-start). The two faces of the project stay in
lock-step: the reader guides teach the method, the SKILL.md files run it. A
typical session reads the relevant guide once, then uses natural-language
prompts (for example "evaluate this idea", "draft the Introduction", "audit
the paper before submission") to let the matching skill execute.

The reader guides are not a substitute for the SKILL.md files. The SKILL.md
files are the canonical specification of each skill's behaviour, including
the full integrity gates, output formats, and mode options. The reader
guides condense the methodology for human consumption, with worked examples
and pedagogical framing the SKILL.md cannot afford.

Chinese-speaking readers can switch at any time using the language footer at
the bottom of every file.

---

[English] | [中文](../zh/README.md)
