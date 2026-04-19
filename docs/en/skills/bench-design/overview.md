# Benchmark Architecture Design

## Why this matters

After a locked gap statement, the next failure mode is a design document
that reads as an ad-hoc collection of choices rather than a principled
architecture. A reviewer at NeurIPS Datasets and Benchmarks, ICLR, or
CVPR will flag this quickly: why these categories and not others, why
this difficulty split, why LLM-as-Judge rather than human, why this
companion method. Without explicit design goals and defensible taxonomy
choices, every design decision becomes an attack surface. The paper
accumulates minor criticisms until the collective weight pushes it below
the acceptance threshold, even when the underlying gap was defensible.

This skill turns a gap statement into a complete architectural blueprint
before any data is built. It covers design goals, task scope, taxonomy
patterns, evaluation framework, the optional companion method,
contamination mitigation, and difficulty calibration. The design
document that comes out of this stage serves as the specification for
[bench-construction](../bench-construction/overview.md): without it, the
pipeline has no target to build toward. A hard gate at the top of
bench-construction refuses to start pipeline work without this document.

## The framework

Seven elements make up a complete benchmark design. Four are required
(goals, scope, taxonomy, evaluation framework); three are strongly
recommended (companion method, contamination mitigation, difficulty
calibration).

### Element 1: Design goals (G1-G4)

Every benchmark should explicitly state its design goals. The four
standard goals cover the most common reviewer expectations:

| Goal | Description | Typical strategy |
|---|---|---|
| **G1: Coverage** | Benchmark covers the breadth of the target capability | Systematic taxonomy, diverse sources, stratified sampling |
| **G2: Fine-grained Diagnostics** | Can pinpoint WHERE models fail, not just IF | Multi-dimensional taxonomy with sub-categories and difficulty levels |
| **G3: Scalability** | Construction is reproducible and extensible at low cost | Automated or semi-automated pipeline, minimal manual annotation |
| **G4: Quality** | Annotations are accurate and evaluation is reliable | Multi-stage QC, inter-annotator agreement, expert validation |

The user must state concretely how the benchmark addresses each goal. A
generic "we use inter-annotator agreement" is not enough; the strategy
should be specific to the task (for example, "Cohen's kappa across three
PhD-level annotators on a stratified random sample"). Custom goals can be
added when the task has domain-specific requirements, for instance G5 for
multilingual coverage or G6 for temporal validity.

### Element 2: Task scope

The task scope paragraph pre-empts the reviewer question "why didn't you
include X?" by stating explicitly what is in scope and what is
deliberately excluded, with reasons:

```
Evaluates:
- [Capability 1]: [brief description]
- [Capability 2]: [brief description]
- ...

Does NOT evaluate (out of scope, with reason):
- [Excluded capability 1]: [why excluded, different research question,
  existing benchmarks already cover it, etc.]
- ...
```

The skill pushes the user to list at least two deliberately-excluded
capabilities and justify each. A benchmark that claims to evaluate
everything usually evaluates nothing well.

### Element 3: Taxonomy design, three validated patterns

The taxonomy is the backbone of fine-grained evaluation. Three validated
patterns cover the common benchmark shapes.

**Pattern 1: Capability times Difficulty Matrix (StatQA).** Tasks where
capabilities are naturally categorical with clear difficulty gradients.
StatQA uses five statistical-method categories crossed with two
difficulty levels for ten evaluation cells total.

```
Categories:   [Cat1]  [Cat2]  [Cat3]  [Cat4]  [Cat5]
                              x
Difficulty:   [Easy]  [Hard]
              ----------
              = 10 evaluation cells
```

**Pattern 2: Phenomenon Type times Severity Spectrum (nvBench 2.0).**
Tasks studying a specific phenomenon (ambiguity, noise, bias) across
intensity levels. nvBench 2.0 uses four ambiguity types crossed with
five severity levels for twenty evaluation cells.

```
Types:    [Type1]  [Type2]  [Type3]  [Type4]
                           x
Severity: [Lv1]  [Lv2]  [Lv3]  [Lv4]  [Lv5]
          ----------
          = 20 evaluation cells
```

**Pattern 3: Multi-dimensional Quality Framework (VisJudge-Bench).**
Tasks where quality has multiple independent facets that interact.
VisJudge-Bench uses three top-level dimensions (Fidelity,
Expressiveness, Aesthetics) with two sub-dimensions each for six
measurable sub-dimensions.

```
Top dimensions:  [Fidelity]  [Expressiveness]  [Aesthetics]
                     v              v                v
Sub-dimensions:  [Sub1.1] [Sub1.2] [Sub2.1] [Sub2.2] [Sub3.1] [Sub3.2]
                 ----------
                 = 6 measurable sub-dimensions
```

The user picks the pattern that best fits the evaluation dimensions. The
skill refuses patterns that do not fit and pushes back when the user
tries to combine all three without justification.

### Element 4: Evaluation framework

Beyond taxonomy, define HOW each dimension is measured. Each sub-dimension
gets a row specifying metric, scoring method, range, and level of
automation:

| Sub-dimension | Metric | Scoring method | Range | Automation |
|---|---|---|---|---|
| [SubDim 1] | e.g., Accuracy | Exact match | 0-1 | Fully auto |
| [SubDim 2] | e.g., Relevance | LLM-as-Judge | 1-5 | Semi-auto |
| [SubDim 3] | e.g., Naturalness | Human rating | 1-7 | Manual |

Four key design decisions recur across benchmarks:

| Decision | Options | Trade-off |
|---|---|---|
| Auto versus human eval | Automatic metrics, LLM-as-Judge, human | Scale versus reliability |
| Single versus multi-answer | One correct answer, multiple valid answers | Simplicity versus real-world fidelity |
| LLM-as-Judge validation | Correlation with human, agreement rate | Must validate if using LLM eval |
| Scoring granularity | Binary, ordinal, continuous | Discriminability versus annotation difficulty |

LLM-as-Judge choices in particular attract reviewer scrutiny. Any paper
using LLM-as-Judge without reporting correlation with human annotation
will be flagged in round one.

### Element 5: Companion method (optional but strongly recommended)

A companion method answers: "This benchmark not only evaluates, it also
helps IMPROVE model capability." The element has three components:

| Component | Question | Example |
|---|---|---|
| Training signal | What data does the benchmark uniquely provide? | Step-wise reasoning paths, preference pairs, fine-grained scores |
| Optimisation technique | How is the signal used? | SFT, DPO, GRPO, RLHF, curriculum learning |
| Value proposition | Why is this better than training without the benchmark? | Targeted improvement on the specific blind spot |

Reference implementations:

| Paper | Training signal | Method | Technique |
|---|---|---|---|
| nvBench 2.0 | Step-wise reasoning paths | Step-Text2Vis | Step-DPO preference optimisation |
| VisJudge-Bench | Fine-grained quality scores | VisJudge | GRPO reinforcement learning |

A companion method is optional but strengthens the paper significantly.
Even a simple fine-tuning experiment showing improvement on the
benchmark's target capability turns the paper from an evaluation
contribution into an evaluation-plus-improvement contribution.

### Element 6: Contamination mitigation

Reviewers in 2024-2026 increasingly test for training-data contamination.
Any benchmark without an explicit contamination-mitigation plan will be
flagged.

| Type | Risk | Mitigation |
|---|---|---|
| Training contamination | Benchmark data appears in model training sets | Time-gated construction, synthetic generation, novel data sources |
| Prompt contamination | Evaluation prompts leak into training | Unique prompt templates, private evaluation scripts |
| Contamination laundering | Using synthetic data from contaminated models to generate "new" data | Verify data provenance, cross-validate with non-LLM sources |
| Benchmark saturation | Models overfit to benchmark style over time | Design for extensibility, include version-control plan |

### Element 7: Difficulty calibration

Top models should achieve only roughly 0.1-9 percent accuracy on the
hardest subset at launch. If top models already score above 50 percent,
the benchmark is probably too easy to have longevity. The design document
should state expected top-model accuracy and include a sanity check
against at least one top model before locking the design.

### Design document template

The skill helps fill this structured template:

```
Benchmark Name: [Name]
Gap Statement: [From bench-gap-analysis]
Research Questions: [RQ1, RQ2, RQ3]

Design Goals:
  G1 (Coverage): [Strategy]
  G2 (Diagnostics): [Strategy]
  G3 (Scalability): [Strategy]
  G4 (Quality): [Strategy]

Task Scope:
  In-scope: [List]
  Out-of-scope: [List with reasons]

Taxonomy:
  Pattern: [1, 2, or 3]
  Dimensions: [List]
  Sub-dimensions: [List]
  Total evaluation cells: [N]

Evaluation Framework:
  [Table of metrics per dimension]

Companion Method (optional):
  Training signal: [What]
  Technique: [How]

Contamination Mitigation:
  Strategy: [How you prevent data leakage]

Difficulty Calibration:
  Expected top-model accuracy: [X percent]
  Hardest subset target: [Y percent]
```

## Named heuristics

- **G1-G4 standard framework**: Coverage, Diagnostics, Scalability,
  Quality. Stated explicitly with concrete strategies per goal.
- **Three taxonomy patterns**: Capability times Difficulty, Phenomenon
  Type times Severity, Multi-dimensional Quality. Pick one; do not
  combine all three.
- **LLM-as-Judge validation rule**: any paper using LLM-as-Judge without
  reporting correlation with human annotation is flagged in round one.
- **Ofir Press guideline**: top models should score roughly 0.1-9 percent
  on the hardest subset at launch. Higher than 50 percent means the
  benchmark is already too easy.
- **In-scope plus out-of-scope discipline**: list at least two
  deliberately-excluded capabilities with reasons. A benchmark that
  claims to evaluate everything evaluates nothing well.

## Worked example

Consider the StatQA team after gap analysis. The gap is Dimension
Blindness: existing math benchmarks test compute correctness but not
statistical method selection. The design stage must produce an
architecture.

**Design goals.** G1 (Coverage): five families of statistical methods
(descriptive, inferential, regression, categorical, time-series) to
cover the breadth of undergraduate statistics. G2 (Diagnostics): two
difficulty levels (easy and hard) per category to diagnose where models
fail. G3 (Scalability): reverse-synthesis pipeline that generates
questions from fixed answers, enabling low-cost expansion. G4 (Quality):
PhD-level annotator review with Cohen's kappa reported.

**Task scope.** In-scope: undergraduate-level statistical reasoning,
method selection plus compute. Out of scope: graduate-level topics like
Bayesian hierarchical modelling (different research question) and
purely-computational tasks like large-scale simulation (existing math
benchmarks already cover this adequately).

**Taxonomy.** Pattern 1 (Capability times Difficulty Matrix): five
categories times two difficulties for ten evaluation cells. The product
of these two dimensions gives the fine-grained diagnostic structure.

**Evaluation framework.** Two metrics per cell: method-selection
accuracy (exact match against gold method, scored 0/1, fully automated)
and final-answer accuracy (numerical match within tolerance, scored 0/1,
fully automated). Both metrics can be computed without LLM-as-Judge, so
the validation rule does not apply.

**Companion method.** Not included in the original StatQA paper; this is
a place where a future extension could add value. A DPO-trained model
that prioritises method selection over final-answer correctness could
demonstrate the benchmark's utility for training.

**Contamination mitigation.** Generate questions using templates that
post-date the frontier models' training cutoffs, and use statistical
scenarios drawn from post-2023 textbooks and journal papers. Run a
perplexity check on a subset to confirm low overlap with model training
distributions.

**Difficulty calibration.** Expected top-model accuracy on hardest
subset: under 20 percent. Confirmed against GPT-4o before locking the
design.

The student advances to [bench-construction](../bench-construction/overview.md)
with a complete design document. The hard gate at the top of the next
skill checks that all seven elements are in place before pipeline work
begins.

## Try it with the plugin

Install the plugin per the [root README](../../../../README.md) and
invoke naturally. The skill self-triggers on phrases from its SKILL.md
description such as "the research gap is clear and you need to define
design goals", "define design goals, task scope, evaluation taxonomy",
or "What does the benchmark look like?". Provide the gap statement and
research questions from the previous stage, and the skill walks through
the seven elements in order, producing the complete design document.

## Source

Adapted from
[archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md)
and the live plugin file
[/plugins/phd-research/skills/bench-design/SKILL.md](/plugins/phd-research/skills/bench-design/SKILL.md).

---

[English] | [中文](../../../zh/skills/bench-design/overview.md)
