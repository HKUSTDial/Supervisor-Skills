# Benchmark Construction Pipeline

## Why this matters

The construction pipeline is the technical contribution of a benchmark
paper, the equivalent of the Method section in a technique paper. Reviewers
scrutinise this section most intensely because a pipeline that is vague,
unreproducible, or weakly quality-controlled cannot support the
downstream findings. A benchmark built on a pipeline that reviewers
cannot trust produces findings that reviewers will not cite. Common
failure modes at NeurIPS Datasets and Benchmarks, ICLR, and CVPR include
a two-paragraph pipeline description without a flowchart, inter-annotator
agreement numbers missing or undefended, and synthetic data generation
described without adversarial validation to check that the synthetic
data resembles real data.

This skill turns the design document from
[bench-design](../bench-design/overview.md) into a complete pipeline
specification: the construction paradigm, per-stage input/operation/
output with explicit quality gates, a documented quality control
strategy, a statistical characterisation plan for Section 2.3 of the
paper, and a pipeline figure (Figure 2) that reviewers can read in under
a minute. A hard gate at the top of this skill refuses to start pipeline
work without a complete design document, because the pipeline operates
against the design's taxonomy and evaluation framework as its target.

## The framework

The skill's structure mirrors the reviewer checklist for construction
pipelines: choose a paradigm, specify stages, document QC strategies,
plan statistical characterisation, and design the pipeline figure.

### Pipeline design principles

Every construction pipeline must satisfy three properties:

1. **Reproducibility**: another team can follow the same steps and get
   comparable data. All prompts, scripts, and annotation guidelines are
   released.
2. **Scalability**: the pipeline can generate more data without
   proportionally more human effort. Bottlenecks are explicit.
3. **Quality assurance**: every data point passes explicit quality gates.
   No data enters the benchmark without gate approval.

### Three validated construction paradigms

Three paradigms cover the common benchmark shapes, each matched to a
reference paper and an intended use case.

**Paradigm 1: Reverse Synthesis (StatQA approach).** Fix the answer first,
then generate the question.

```
Define answer space -> Generate matching conditions ->
Compose questions -> Validate uniqueness
(enumerate)           (scenarios)
(NL wrap)             (one correct answer)
```

Use when the answer space is enumerable (statistical methods, chart
types, code patterns), and when you need precise control over difficulty
distribution and category balance. The key advantage is unambiguous
ground truth by construction: the answer is known before the question
exists, so there is no ambiguity about what "correct" means.

**Paradigm 2: Controlled Injection (nvBench 2.0 approach).** Start from
clean seeds, systematically inject the target phenomenon.

```
Collect clean seeds -> Define injection types ->
Inject at calibrated levels -> Validate naturalness
(unambiguous)          (e.g., 4 types)
(e.g., 5 severity levels)   (human check)
```

Use when you study a specific phenomenon (ambiguity, noise, bias,
adversarial perturbation) and need controlled severity gradients across
the phenomenon. The key advantage is variable isolation: the target
phenomenon can be studied independently of confounds because the clean
seeds serve as the control condition.

**Paradigm 3: Adaptive Generation plus Expert Annotation
(VisJudge-Bench approach).** LLMs generate candidate data, humans
annotate across multiple stages.

```
LLM generates candidates -> Stage-1 screening ->
Stage-2 fine-grained scoring -> Stage-3 cross-validation
(adapted to content)         (expert filter)
(multi-dimension)            (disagreement resolution)
```

Use when the task requires nuanced human judgment that cannot be fully
automated, and quality depends on expert assessment across multiple
subjective dimensions. The key advantage is combining LLM scalability
with human judgment quality: neither alone produces data that reviewers
trust for subjective tasks.

The skill asks the user to choose one paradigm (or justify combining
elements from multiple), and to describe the data source and rough
pipeline sketch.

### Pipeline stages specification

Regardless of paradigm, every stage is documented with this template:

| Stage | Input | Operation | Output | Quality gate |
|---|---|---|---|---|
| **1. Source Selection** | Raw data sources | Filtering, licensing, dedup | Clean source corpus | Coverage audit, license check |
| **2. Seed Generation** | Source corpus | [Paradigm-specific method] | Initial samples | Format validation, uniqueness |
| **3. Enrichment** | Initial samples | Add metadata, labels, tags | Annotated samples | Taxonomy coverage balance |
| **4. Quality Control** | Annotated samples | Human review, auto validation | Validated samples | IAA at or above threshold |
| **5. Splitting** | Validated samples | Stratified train/dev/test split | Final dataset | Distribution balance check |

For each stage, the skill pushes the user to specify who performs it
(automated script, LLM, human annotator, domain expert), how long it
takes per sample and in total, and what can go wrong and how failures
are handled. Vague pipeline descriptions are a top rejection reason.

### Quality control strategies

Document at least three strategies. Reviewers scrutinise this heavily
because weak QC means untrusted findings.

| Strategy | Method | When to use |
|---|---|---|
| Inter-Annotator Agreement | Multiple annotators on same samples; report Cohen's kappa, Fleiss' kappa, or ICC | Any human annotation task |
| Expert Spot-Check | Domain expert reviews random 10 percent or more subset | Semi-automated pipelines |
| Adversarial Validation | Test if a classifier can distinguish synthetic from real data | Synthetic data generation |
| Automated Sanity Checks | Rule-based validation: format, range, consistency, deduplication | All pipelines |
| Pilot Study | Small-scale trial run (50-100 samples) before full construction | Complex multi-stage pipelines |
| LLM Cross-Validation | Use a different LLM family to verify LLM-generated data | LLM-in-the-loop pipelines |

Inter-annotator agreement is the minimum for any benchmark involving
human annotation. Expert spot-check is strongly recommended for
semi-automated pipelines. Adversarial validation is necessary whenever
synthetic data is used because reviewers will ask whether the synthetic
data resembles real data.

### Statistical characterisation (Section 2.3 content)

After construction, present comprehensive statistics. The "must-have"
list corresponds to Table 2 and Figures 3-4 of the final paper:

- Total sample count by split (train/dev/test).
- Distribution across taxonomy categories (bar chart or pie chart).
- Difficulty distribution (histogram).
- Text length or complexity distribution.
- Scale comparison with existing benchmarks.

Recommended additions: word cloud or topic distribution, source
diversity metrics, 2-3 representative data examples as a Figure, and
annotation time and cost statistics for transparency.

### Pipeline figure (Figure 2)

The pipeline must be visualised. Design guidelines:

- Left-to-right or top-to-bottom flow with clear directionality.
- Each step is a labeled box with a brief description.
- Between steps, arrows annotated with data count (for example,
  "10K -> filtering -> 8.5K").
- Quality gates are visually distinct (diamond shapes, coloured borders,
  or gate icons).
- A concrete example shows one sample flowing through the entire
  pipeline.
- The paradigm label (Reverse Synthesis, Controlled Injection, or
  Adaptive Generation) appears at the top of the figure.

## Named heuristics

- **Three validated paradigms**: Reverse Synthesis, Controlled Injection,
  Adaptive Generation plus Expert Annotation. Pick one that matches the
  task shape, or justify a combination.
- **Five-stage template**: Source Selection, Seed Generation, Enrichment,
  Quality Control, Splitting. Every stage has explicit input, operation,
  output, and quality gate.
- **Minimum three QC strategies**: inter-annotator agreement plus two
  more matched to the pipeline's risk points.
- **Pipeline figure mandatory**: Figure 2 with data counts on arrows and
  quality gates visually distinct. Reviewers want to read the pipeline
  in under a minute.
- **Data-count annotations**: every arrow shows how much data flows
  through each stage, so the reader can trace retention rates.

## Worked example

Consider the nvBench 2.0 team after design. The gap pattern is
Assumption Violation: existing text-to-visualisation benchmarks assume
single correct output, but real queries are ambiguous. The design uses
Pattern 2 (Phenomenon Type times Severity Spectrum), with four ambiguity
types crossed with five severity levels.

**Paradigm choice.** Controlled Injection fits exactly. The team starts
from the existing nvBench 1.0 corpus of unambiguous query-chart pairs,
defines four ambiguity injection types (chart-type ambiguity, attribute
ambiguity, aggregation ambiguity, filter ambiguity), and injects these
at five calibrated severity levels. The clean seeds serve as the control
condition.

**Pipeline stages.** Stage 1 (Source Selection): take the 7,247
unambiguous pairs from nvBench 1.0, filter for quality. Stage 2 (Seed
Generation): for each clean seed, generate one ambiguous variant per
injection type and severity level using a rule-based plus LLM hybrid
pipeline. Stage 3 (Enrichment): annotate each ambiguous variant with the
set of valid chart interpretations, with preference rankings. Stage 4
(Quality Control): three annotators rate each ambiguous variant for
naturalness (does this read like a real user query?) and validity (are
the annotated interpretations all reasonable?). Reports Fleiss' kappa
across the three annotators. Stage 5 (Splitting): stratified split
across phenomenon types and severity levels.

**Quality control.** Three strategies documented: (1) Fleiss' kappa
across three annotators on naturalness and validity, with minimum
threshold of 0.6; (2) expert spot-check of 10 percent by visualisation
PhD students; (3) LLM cross-validation using a different LLM family to
regenerate chart alternatives and confirm overlap with the annotated
set.

**Statistical characterisation.** Total scale (ambiguous variants per
injection type and severity level), distribution across the twenty
evaluation cells, comparison with nvBench 1.0 on scale, length of
queries, and three representative examples showing an unambiguous seed
and its ambiguous variants.

**Pipeline figure.** A left-to-right flow with five stages, data counts
on every arrow (7,247 seeds produce roughly 36,000 variants at
1.25 variants per severity level times four types, then Stage 4 filters
to roughly 30,000 validated variants), quality gates drawn as diamonds
at the end of stages 2, 3, and 4, and a worked example traced through
every stage. Paradigm label "Controlled Injection" at the top.

StatQA (Reverse Synthesis) and VisJudge-Bench (Adaptive Generation plus
Expert Annotation) follow the same specification process with their own
paradigm-specific stages. The skill uses them as reference templates
when the user's pipeline is ambiguous or underspecified.

## Try it with the plugin

Install the plugin per the [root README](../../../../README.md) and
invoke naturally. The skill self-triggers on phrases from its SKILL.md
description such as "benchmark design is finalized and you need to plan
how to actually build the data", "source selection, generation strategy,
annotation protocol, quality control", or "How is the data built?".
Provide the design document from the previous stage, and the skill
walks through paradigm selection, stage specification, QC strategy
design, and pipeline figure sketch.

## Source

Adapted from
[archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md)
and the live plugin file
[/plugins/phd-research/skills/bench-construction/SKILL.md](/plugins/phd-research/skills/bench-construction/SKILL.md).

---

[English] | [中文](../../../zh/skills/bench-construction/overview.md)
