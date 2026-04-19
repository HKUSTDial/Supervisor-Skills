# Benchmark Writing Orchestrator

## Why this matters

A PhD student writing a benchmark paper for NeurIPS Datasets and Benchmarks,
ICLR, ICML, ACL, EMNLP, or CVPR faces a different problem shape than the
student writing a technique paper. A technique paper sells a method;
reviewers ask whether the method beats baselines and whether the ablations
are honest. A benchmark paper sells a new evaluation dimension, a systematic
measurement, and a set of findings about model capability. Reviewers ask
whether the gap is real, whether the pipeline is reproducible, whether the
findings are surprising enough to matter, and whether a future paper can
build on top. Conflating the two paper shapes produces common rejection
patterns: a benchmark paper that reads as a dataset release without
justified gap, a pipeline described in two paragraphs without the Figure 2
reviewers expect, an experiment section full of leaderboard numbers without
the "Finding X" extraction that makes a benchmark paper quotable.

The bench-writing orchestrator is the entry point for this workflow. It
detects which stage the current project is at (gap analysis, design,
construction, experiments, paper structure, checklist) and routes the user
to the matching sub-skill, rather than attempting to handle every stage in
a single response. Each sub-skill has its own hard gate that prevents
skipping ahead. The ordering is deliberate: skipping gap analysis to start
pipeline design is the single most common failure mode across novice
benchmark authors, and the gate is there to catch that failure before the
student spends three months on a pipeline that serves no defensible gap.

## The framework

### Narrative axis: benchmark paper versus technique paper

The core philosophy differs on almost every axis. A benchmark paper is not
a weaker technique paper; it is a different paper shape that optimises for
different reviewer questions.

| Dimension | Technique paper | Benchmark paper |
|---|---|---|
| Core claim | Our method is better | This evaluation dimension is overlooked |
| Role of problem definition | Goal stated in one sentence | Problem definition is the contribution (defining what to evaluate, how to measure, what insights emerge) |
| Introduction axis | Key idea or mechanism | Evaluation gap plus benchmark design rationale |
| Main chapter | Method or Approach (largest section) | Construction pipeline is core; companion method is bonus |
| Experiment goal | Prove SOTA | Reveal model capability boundaries plus deep insights for future research |
| Key figures and tables | Architecture diagram | Benchmark comparison table, construction pipeline figure, multi-dimensional analysis charts |
| Key contribution | Novel technique | New evaluation paradigm plus empirical findings |

A benchmark paper's core is not "we propose a dataset"; it is defining a
new evaluation dimension, providing systematic measurement infrastructure,
and revealing deep insights about model capability. The Gap and the
Motivation must be made explicit in the Introduction. The paper needs to
state plainly, in its own voice, exactly why this benchmark or this
evaluation paper needs to exist.

### The Five Pillars

Every publishable benchmark paper addresses these five elements. Four are
required; the fifth is optional but strongly recommended.

1. **Research Gap** (evaluation blind spot). Clear, defensible, named using
   one of three validated gap patterns. Without a real gap, the paper has
   no thesis.
2. **Construction Pipeline** (construction methodology). Systematic,
   scalable, reproducible data creation with explicit quality gates.
3. **Evaluation Framework** (measurement detail). Multi-dimensional
   taxonomy plus fine-grained metrics that enable diagnosis, not just
   ranking.
4. **Empirical Findings** (insights beyond leaderboard numbers). The
   signature Finding X bold-summary pattern that gives the paper its
   reusable, quotable outputs.
5. **Companion Method** (optional). A model or training recipe that uses
   the benchmark's data to improve capability on the identified gap. Turns
   an evaluation contribution into an evaluation-plus-improvement
   contribution.

Each pillar maps to one or more sub-skills, which the orchestrator routes
to in sequence.

### Stage detection and routing

The orchestrator asks one question first: which stage is this project at?
The user self-identifies using the following table, or the orchestrator
infers the stage from context and confirms before routing.

| Stage | Condition | Invoke skill | Key question answered |
|---|---|---|---|
| 1. Gap Analysis | Still exploring why this benchmark needs to exist | `bench-gap-analysis` | Why does this benchmark need to exist? |
| 2. Benchmark Design | Gap confirmed, designing the benchmark system | `bench-design` | What does the benchmark look like? |
| 3. Construction Pipeline | Design locked, planning the data construction pipeline | `bench-construction` | How is the data built? |
| 4. Experiment Design | Data ready or under construction, experiments to design | `bench-experiments` | What experiments reveal the deepest insights? |
| 5. Paper Structure | Experiments complete, writing the paper | `bench-paper-structure` | How to organise and write the paper? |
| 6. Pre-submission Checklist | First draft complete, running pre-submission checks | `bench-checklist` | Is the paper ready to submit? |

### Pipeline DAG

The sub-skills form a directed acyclic graph. Sub-skills have explicit
terminal states that name the next skill in the chain, and hard gates that
block proceeding without prerequisite deliverables.

```
START
 |
 v
bench-gap-analysis
 |  (gap statement plus RQs)
 v
bench-design
 |  (design document)
 v
bench-construction
 |  (pipeline spec plus QC)
 v
bench-experiments
 |  (RQ-driven experiment plan)
 v
bench-paper-structure
 |  (Introduction, sections, figure and table plan)
 v
bench-checklist
 (final gate; routes back on critical issues)
```

### Reference exemplars

Three published benchmark papers thread through all sub-skills as recurring
case studies, one per gap pattern:

| Paper | Venue | Domain | Gap pattern | Construction paradigm |
|---|---|---|---|---|
| StatQA | NeurIPS 2024 | Math and statistics | Dimension Blindness | Reverse synthesis |
| nvBench 2.0 | NeurIPS 2025 | Text-to-visualisation | Assumption Violation | Controlled injection |
| VisJudge-Bench | ICLR 2026 | Visualisation evaluation | Granularity Mismatch | Adaptive generation plus expert annotation |

Each sub-skill grounds its guidance in the matching exemplar so that the
advice translates from abstract template to concrete paper.

## Named heuristics

- **Five Pillars**: Research Gap, Construction Pipeline, Evaluation
  Framework, Empirical Findings, Companion Method (optional). Every
  publishable benchmark paper addresses these.
- **Narrative axis discipline**: a benchmark paper sells an evaluation
  dimension, not a method. Writing a benchmark paper with a technique
  paper's axis produces systematic reviewer confusion.
- **Stage gating**: every sub-skill has a hard gate at its top that blocks
  proceeding without the previous stage's deliverable. Gates exist to
  catch the skip-ahead failure mode before it wastes months.
- **Single-entry orchestration**: users new to benchmark writing should
  enter through this orchestrator; experienced users can call sub-skills
  directly when they know exactly which stage they are at.

## Worked example

Consider a user who messages the orchestrator saying "I want to build a
benchmark for evaluating LLMs on high-school math Olympiad problems, can
you help?"

The orchestrator does not immediately start drafting design goals. Its
first move is stage detection. The user has a topic area and a vague aim
but no explicit gap statement (what specifically is missing from existing
math benchmarks), no taxonomy, no pipeline sketch. The orchestrator
confirms: "Before we design the benchmark architecture, we need to
articulate exactly what evaluation blind spot this fills. Let us start
with the gap analysis stage." It then routes to
[bench-gap-analysis](../bench-gap-analysis/overview.md).

Inside bench-gap-analysis, the user surveys existing math benchmarks
(GSM8K, MATH, AIME, OlympiadBench, MATH-L5, and so on), identifies the
common implicit assumption they share (for example, that correctness is
binary: either the final numeric answer matches or it does not), and
proposes a gap: existing benchmarks do not evaluate proof elegance or the
ability to distinguish between multiple valid solution strategies. That
gap matches the Dimension Blindness pattern. The gap passes the four
validation checks (practical impact for competition grading, measurable
via rubric, non-trivial to add to existing benchmarks, actionable for
training feedback). The user drafts a gap statement and two research
questions.

Only after the gap is locked does the orchestrator route forward to
[bench-design](../bench-design/overview.md), which turns the gap into
design goals (G1-G4), task scope, taxonomy, and evaluation framework. Had
the user tried to skip the gap analysis and go straight to design, the
hard gate at the top of bench-design would have caught it and routed
back. The gate is not a bureaucratic obstacle; it is a safeguard against
the most common benchmark-paper failure, building a dataset that has no
defensible reason to exist.

## Try it with the plugin

Install the plugin per the [root README](../../../../README.md) and invoke
naturally. The orchestrator self-triggers on phrases from its SKILL.md
description such as "starting a new benchmark paper", "resuming work on a
benchmark project", or "how do I write a benchmark paper". Describe the
current project state in a sentence or two, and the orchestrator detects
the stage and routes to the matching sub-skill. For direct invocation of
a specific stage, name the sub-skill by its published name (for example
`bench-gap-analysis`) when you already know which stage you are at.

## Source

Adapted from
[archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md)
and the live plugin file
[/plugins/phd-research/skills/bench-writing/SKILL.md](/plugins/phd-research/skills/bench-writing/SKILL.md).

---

[English] | [中文](../../../zh/skills/bench-writing/overview.md)
