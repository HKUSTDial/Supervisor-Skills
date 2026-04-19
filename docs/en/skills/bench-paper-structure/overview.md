# Benchmark Paper Structure and Writing

## Why this matters

The Introduction of a benchmark paper is the compressed version of the
entire paper, and its narrative axis is not "key idea or mechanism"
(the axis for a technique paper) but "evaluation gap plus benchmark
design rationale". Writing a benchmark paper's Introduction with a
technique-paper axis produces systematic reviewer confusion at NeurIPS
Datasets and Benchmarks, ICLR, ICML, ACL, EMNLP, and CVPR. The common
failure patterns include an Introduction that reads like a dataset
release (no Gap paragraph, no Design Considerations paragraph), missing
Figure 1 (the Running Example), missing Table 1 (the Benchmark
Comparison), a Pipeline description without Figure 2, an experiments
section that skips the Finding X bolded summaries, and a Contributions
list that does not map to sections. Each of these is individually
fixable, but the cumulative weight sinks the paper.

This skill organises completed research into a submission-ready paper.
It specifies the six-part Introduction framework, the main body section
structure with page budget, the figure and table placement guide, the
signature writing techniques for benchmark papers, and the appendix
plan. A hard gate at the top confirms that the prerequisites exist
(gap statement, design document, pipeline specification, experiment plan)
before any writing begins. Without the prerequisites, the paper has
nothing to organise.

## The framework

### Introduction: the six-part framework

The Introduction follows a specific logical chain. Each part maps to
approximately one paragraph, and the ordering is not negotiable.

**Part 1: Background and Core Scenario (~1 paragraph).** Establish the
importance of the broader task or domain in real-world scenarios. Show
the field has made rapid progress, citing recent advances. Use a
carefully designed Running Example (Figure 1) to illustrate the task's
complexity and how human experts handle it. Figure 1 is one of the most
important figures in the paper; it must be meticulously crafted. Tone:
authoritative, citing well-known work.

Reference: StatQA uses a complete statistical-analysis workflow;
nvBench 2.0 shows multiple valid interpretations of an ambiguous query;
VisJudge-Bench contrasts positive and negative examples across Fidelity,
Expressiveness, and Aesthetics.

**Part 2: Limitations of Existing Benchmarks, The Gap (~1 paragraph).**
Survey what existing benchmarks measure, acknowledging their
contributions fairly. Identify the implicit assumption they all share
and make it explicit. Articulate the evaluation blind spot in at most
three points, specific not vague. Strongly recommended: provide a
Benchmark Comparison Table (Table 1) that compares feature dimensions
item by item to make the gap self-evident. This is the most important
paragraph in the paper. It should make the reader think: "I never
considered that, but it is obviously important."

Reference: nvBench 2.0 Table 1 compares seven benchmarks across six
dimensions; VisJudge-Bench Table 1 compares seven benchmarks across
three evaluation dimensions.

**Part 3: Research Questions (~1 paragraph).** Transform the gap into
2-3 concrete research questions. RQ coverage should span: (1) how to
build an appropriate benchmark, (2) where the capability boundaries of
current models lie, (3) what the gap between models and human experts
is. RQs anchor the entire experiment section.

Reference: StatQA uses Q1 How to evaluate? Q2 How capable are LLMs?
Q3 Human versus LLM?

**Part 4: Design Considerations (~1 paragraph).** This paragraph is
unique to benchmark papers. Before introducing the solution, first
articulate what properties a good benchmark in this area should have.
This provides the rationale for the design choices that follow. State
design requirements explicitly (diverse coverage, fine-grained
diagnostics, scalability, quality assurance). This is the logical
foundation for why the benchmark is designed the way it is.

Reference: nvBench 2.0 states: "This benchmark should include diverse
ambiguous queries, multiple valid outputs, reasoning paths, and broad
domain coverage."

**Part 5: Our Benchmark plus Key Findings Preview (~1-2 paragraphs).**
Formally introduce the benchmark name, scale, and key design choices.
Highlight construction-methodology innovation in one or two sentences.
Reference Figure 1 and Table 1. Summarise 2-3 of the most surprising
empirical findings to entice the reader. Use concrete numbers: "We
evaluate 15 models across 6 dimensions." Tone: confident but precise.

Reference: StatQA states its key idea as "reversing this process by
synthesising the question Q based on target answers A."

**Part 6: Contributions (~1 paragraph, bulleted list).** Typically 3-4
contributions, each mapping to a paper section:

1. We identify [the gap] and propose [Name], the first benchmark for
   [capability]. (-> Section 1-2)
2. We design [pipeline innovation] that achieves [quality or scale
   metric]. (-> Section 2)
3. We conduct comprehensive evaluation of [N] models and reveal [key
   finding]. (-> Section 4)
4. (Optional) We propose [companion method] that improves [metric] by
   [amount]. (-> Section 3)

### Critical Introduction figures and tables

**Figure 1: Running Example (must-have).** The most important figure in
the paper. Requirements: illustrates the evaluation gap with one
concrete example; shows what existing evaluation misses versus what the
new benchmark captures; self-contained (a reader should grasp the
paper's core idea from this figure alone); placed on page 1-2, above
the fold if possible. Three common design patterns: split view
("existing evaluation" left versus "our evaluation" right), walkthrough
(one input, multiple evaluation dimensions highlighted), and contrast
(same model output scored by old criteria versus new criteria).

**Table 1: Benchmark Comparison (must-have).** Compare with 5-8
existing benchmarks. The rightmost column is the key differentiator:

```
| Benchmark | Year | Scale | Dim1 | Dim2 | Dim3 | Your Key Feature |
|-----------|------|-------|------|------|------|------------------|
| Prior-1   | 20XX | N     | yes  | no   | yes  | no               |
| Prior-2   | 20XX | N     | yes  | yes  | no   | no               |
| Ours      | 2025 | N     | yes  | yes  | yes  | yes              |
```

### Main body section structure

**Section 2: The Proposed Benchmark (3-4 pages, the core chapter).**

```
2.1 Design Goals and Task Scope
    - State G1-G4 explicitly
    - Define in-scope versus out-of-scope

2.2 Benchmark Construction Pipeline
    - Pipeline overview paragraph
    - Figure 2: pipeline flowchart (must-have)
    - Detailed steps with input, operation, output
    - Quality-control measures
    - Annotation protocol (if human annotation involved)

2.3 Benchmark Characteristics
    - Table 2: dataset statistics (splits, categories, scale)
    - Figures 3-4: distribution charts (taxonomy, difficulty, length)
    - Figure 5: data examples (2-3 representative samples)
    - Comparison with existing benchmarks on scale and coverage
```

**Section 3: Specialised Model (1-2 pages, optional).**

```
3.1 Motivation: how the benchmark enables model improvement
3.2 Method: training signal plus optimisation technique
3.3 Implementation details
```

**Section 4: Experiments and Empirical Findings (4-5 pages).**

```
4.1 Experimental Setup
    - Models (grouped by type), metrics, prompting, implementation

4.2 Overall Performance
    - Table 3: ALL models times ALL metrics (largest table in paper)
    - Bold best, underline second-best
    - Finding 1 after analysis

4.3 Fine-grained Analysis (organised by RQ)
    - RQ1 analysis -> Finding 2
    - RQ2 analysis -> Finding 3
    - RQ3 analysis -> Finding 4
    - Each with supporting figure or table

4.4 Case Studies
    - 2-4 examples with qualitative analysis
    - Success case, failure case, surprising case
```

**Section 5: Discussion and Research Opportunities (~1 page).** Based on
the Findings, discuss how to enhance model capability on the identified
gap, human-AI collaboration patterns, benchmark extension directions
(new modalities, languages, domains), and limitations of the current
benchmark.

**Section 6: Related Work (~1 page).** Organised into 2-3 subsections:
[Task-specific] Benchmarks, [Domain] Evaluation Methodologies, [Related
capability] in Large Language Models. Include a comparison table, either
an expanded Table 1 or a new table focused on methodology differences.
Placement note: Related Work can go before or after Experiments. Before
Experiments (as in VisJudge-Bench) emphasises positioning; after
Experiments (as in StatQA and nvBench 2.0) lets the findings speak
first.

**Section 7: Conclusion (~0.5 page).** Restate the gap and benchmark in
1-2 sentences. Summarise key findings, referencing Finding numbers.
Restate open problems and future directions.

### Figure and table placement guide

| Item | Position | Purpose | Priority |
|---|---|---|---|
| Figure 1 | Page 1-2 | Running Example | MUST |
| Table 1 | Page 2-3 | Benchmark Comparison | MUST |
| Figure 2 | Page 3-4 (Section 2.2) | Construction Pipeline | MUST |
| Table 2 | Page 4-5 (Section 2.3) | Dataset Statistics | MUST |
| Figures 3-4 | Page 4-5 (Section 2.3) | Distribution Charts | HIGH |
| Figure 5 | Page 5 (Section 2.3) | Data Examples | HIGH |
| Table 3 | Page 6-7 (Section 4.2) | Overall Performance | MUST |
| Figures 6+ | Page 7-8 (Section 4.3) | Analysis Charts | HIGH |

### Key writing techniques for benchmark papers

1. **Finding X summaries**: bold-highlight after each major analysis
   (see [bench-experiments](../bench-experiments/overview.md) for the
   full template).
2. **Design rationale over description**: for every choice, explain
   WHY, not just WHAT. Reviewers ask why constantly; pre-empt by
   stating it.
3. **Concrete numbers**: "We evaluate 15 models across 6 dimensions",
   not "many models". Concrete numbers are more credible than vague
   phrasing.
4. **Active positioning**: "the FIRST benchmark to..." or "Unlike prior
   work, we...". Do not bury the contribution in passive voice.
5. **Example-driven arguments**: always pair abstract claims with
   concrete examples. One example is worth three paragraphs of
   description.
6. **Appendix strategy**: move detailed content to the appendix (full
   results, annotation guidelines, more examples, prompts used). The
   main body should be readable in one pass.

### Appendix planning

Standard appendix sections for benchmark papers: A (full experimental
results, unabridged), B (annotation guidelines and interface
screenshots), C (additional data examples), D (prompts used for
evaluation), E (extended related work or taxonomy details), F (ethical
considerations and datasheet).

## Named heuristics

- **Six-part Introduction framework**: Background, Limitations,
  Research Questions, Design Considerations, Our Benchmark plus
  Findings Preview, Contributions. No skipping parts.
- **Design Considerations paragraph**: unique to benchmark papers.
  Articulate what a good benchmark should have, then show yours meets
  the bar.
- **Five must-have figures and tables**: Figure 1 Running Example,
  Table 1 Benchmark Comparison, Figure 2 Pipeline, Table 2 Statistics,
  Table 3 Overall Performance. Missing any one is a flagged issue in
  pre-submission review.
- **Finding X bolded summaries**: signature writing technique of
  benchmark papers. One Finding per major analysis.
- **Contribution-section mapping**: each contribution in the
  Introduction maps to a section number. No orphan contributions.
- **Related Work placement choice**: before experiments to emphasise
  positioning, after experiments to let findings speak first. Both
  are valid; pick based on the paper's strongest angle.

## Worked example

Consider VisJudge-Bench after experiments. The paper structure comes
together as follows.

**Introduction.** Part 1 establishes that visualisation evaluation is
important for both AI-generated chart applications and human analyst
tools, with Figure 1 showing a chart that is accurate but visually
misleading alongside a chart that is beautiful but factually wrong.
Part 2 surveys seven existing chart-evaluation benchmarks, identifies
the shared assumption that quality is either aesthetic or factual
(never both), and presents Table 1 comparing seven benchmarks across
three evaluation dimensions with every prior benchmark missing at
least two dimensions. Part 3 states three research questions around
building a multi-dimensional benchmark, measuring current model
performance, and comparing models against human experts. Part 4 states
that a good chart-evaluation benchmark requires Fidelity,
Expressiveness, and Aesthetics together, plus fine-grained
sub-dimensions. Part 5 names the benchmark (VisJudge-Bench), states
the scale (fifteen thousand candidate charts across six sub-dimensions),
previews three Findings. Part 6 lists four contributions each mapped to
a section.

**Main body.** Section 2 presents the design goals, scope, pipeline
(Figure 2 showing Adaptive Generation plus Expert Annotation flow with
data counts on every arrow), and statistics (Table 2 dataset
statistics, Figures 3-4 distribution charts, Figure 5 data examples).
Section 3 presents the VisJudge companion method (GRPO-trained
evaluator). Section 4 presents experiments, starting with Table 3
overall performance, then Sections 4.2-4.4 organised by research
question with Findings 1-4 bolded after each major analysis. Section 5
discusses research opportunities. Section 6 related work. Section 7
conclusion referencing the Findings by number.

**Figures and tables.** All five must-have items present: Figure 1
Running Example on page 2, Table 1 Benchmark Comparison on page 3,
Figure 2 Pipeline on page 4, Table 2 Statistics on page 5, Table 3
Overall Performance on page 7. Four additional figures support the
fine-grained analyses.

**Appendix.** A through F per the standard layout, with full
experimental results in A, annotation interface screenshots in B, fifty
additional data examples in C, all evaluation prompts in D, extended
taxonomy details in E, and ethical considerations including datasheet
in F.

StatQA and nvBench 2.0 follow the same structure with their own gap,
taxonomy, pipeline, and findings.

## Try it with the plugin

Install the plugin per the [root README](../../../../README.md) and
invoke naturally. The skill self-triggers on phrases from its SKILL.md
description such as "gap analysis, benchmark design, construction, and
experiment planning are ready", "organise them into a submission-ready
paper", or "Introduction structure, section organisation, figure and
table placement". Provide the prior-stage deliverables, and the skill
walks through the six-part Introduction, main body structure, figure
placement, and Contributions alignment.

## Source

Adapted from
[archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md)
and the live plugin file
[/plugins/phd-research/skills/bench-paper-structure/SKILL.md](/plugins/phd-research/skills/bench-paper-structure/SKILL.md).

---

[English] | [中文](../../../zh/skills/bench-paper-structure/overview.md)
