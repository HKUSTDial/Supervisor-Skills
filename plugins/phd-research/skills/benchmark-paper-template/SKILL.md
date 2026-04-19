---
name: benchmark-paper-template
description: Structures Benchmark and Evaluation papers using the five-pillar framework (Research Gap, Construction Pipeline, Evaluation Framework, Empirical Findings, optional Companion Method). Returns a completeness audit, a six-part Introduction logic chain, a Section 2-7 skeleton, and a pre-submission checklist. Use when writing a benchmark paper, structuring a benchmark paper, checking whether a benchmark idea is substantive, drafting a benchmark Introduction, or planning the data-construction pipeline or experiments.
license: CC-BY-4.0
---

# Benchmark Paper Template

## Overview

A Benchmark paper does not win by proposing a new algorithm. It wins by defining a new evaluation dimension and shipping a construction pipeline that makes the measurement high-quality, scalable, and reproducible. This skill scaffolds the five pillars a reviewer checks, then gives you a six-part Introduction chain, a Section 2-7 skeleton, and a pre-submission checklist. Stage-specific depth lives in seven reference files under `references/`.

## Core capabilities

1. **Five-pillar completeness audit**: is the Research Gap articulated? Is the Construction Pipeline principled? Is the Evaluation Framework fine-grained? Do the Empirical Findings reveal capability boundaries? Is a Companion Method warranted?
2. **Introduction six-part logic chain**: Background + Running Example, Existing-Benchmark Limitations (no more than three), Research Questions, Design Considerations, Our Proposal, Contributions.
3. **Section skeleton for §2 to §7**: Task and Design Goals, Construction Pipeline, Optional Companion Method, Experiments organized by RQ, Discussion and Research Opportunities, Related Work with benchmark comparison table, Conclusion.
4. **Pre-submission self-check**: four-category reviewer checklist (Introduction, Benchmark section, Experiments, Overall) with Critical, Major, Minor severity.

## Benchmark paper vs technical paper

| Dimension | Technical paper | Benchmark paper |
|---|---|---|
| Main contribution | Novel algorithm or method | Novel evaluation dimension or dataset |
| Introduction axis | Key Idea or Mechanism | Evaluation Gap and Benchmark Design Rationale |
| Problem definition | One-sentence goal | The problem definition IS the contribution |
| Heaviest chapter | Method | Construction Pipeline + Evaluation Framework |
| Experiments purpose | Prove "my method beats baselines" | Reveal "where model capability boundaries sit" |
| Canonical Figure 1 | Method framework diagram | Running example + pipeline diagram |

For technical and position papers, use the `tech-paper-template` skill. For the Introduction outline in isolation, use `intro-drafter`.

## The five pillars

1. **Research Gap**. What dimension of evaluation does existing work miss? Ground the gap in a concrete failure case and cite at least three prior benchmarks whose limitations you are addressing (no more than three). Exemplars: StatQA highlights missing statistical-method appropriateness; nvBench 2.0 highlights query-ambiguity blindness; VisJudge-Bench highlights the fidelity-expressiveness-aesthetics trinity in visualization evaluation.
2. **Construction Pipeline**. How do you build high-quality, scalable, reproducible data? Three common paradigms: Reverse Synthesis (seed knowledge then instantiate), Controlled Injection (seed queries then inject targeted ambiguity or error), Adaptive Generation with Expert Validation. Specify source selection, generation, annotation, quality control, split strategy, and statistical profile. Deep dive: `references/construction-pipeline.md`.
3. **Evaluation Framework**. Beyond a single overall score: difficulty tiers, error taxonomy, per-dimension rubrics. Explain why this taxonomy diagnoses what the gap pointed at. Deep dive: `references/benchmark-design.md`.
4. **Empirical Findings**. Multi-angle comparisons (Human vs LLM, architecture families, error distributions) condensed into bolded *Finding X:* sentences that read like lemmas. Each Finding must be actionable for future research. Deep dive: `references/experiments.md`.
5. **Companion Method (optional)**. A specialized model tuned for this benchmark signals that the community can act on the findings. Examples: Step-Text2Vis, VisJudge. Not mandatory, but strongly recommended for benchmarks targeting mature tasks.

## Introduction six-part flowchart

1. **Research Background + Running Example (Figure 1)**. Establish the task, why it matters, and one concrete example that threads through the entire paper.
2. **Existing-Benchmark Limitations**. At most three, each specific and traceable to an evaluation blind spot. Avoid vague "is limited" phrasing.
3. **Research Questions**. Two or three RQs covering construction quality, capability boundaries, and the human-AI gap.
4. **Design Considerations**. What should a good benchmark for this dimension have? Quality, scale, coverage, reproducibility, contamination resistance.
5. **Our Proposal**. One paragraph: the benchmark plus the companion method if any.
6. **Contributions**. Typically four items: benchmark + pipeline innovation + systematic evaluation + findings or companion method.

## Section skeleton

- **§2 Task + Design Goals**: problem formulation, goals (G1 coverage, G2 fine-grained diagnostics, G3 reproducibility, G4 contamination resistance). See `references/benchmark-design.md`.
- **§3 Construction Pipeline**: sources, generation, annotation protocol, QC, statistical profile. Figure 2 is the canonical pipeline diagram. See `references/construction-pipeline.md`.
- **§4 Companion Method (optional)**: a specialized model whose training set is this benchmark.
- **§5 Experiments**: organized by RQ. Include the Overall Performance table (typically the largest table in the paper), fine-grained analysis, a human baseline when available, and bolded *Finding X:* summaries. See `references/experiments.md`.
- **§6 Discussion + Research Opportunities**: what the findings reveal and what comes next.
- **§7 Related Work**: a benchmark comparison table (often labelled Table 1) is essential, either here or at the end of §1.

The full section-by-section writing guide with page budgets and figure placement is in `references/paper-structure.md`.

## Prompt template

Paste the block below into your AI assistant with the input slots filled.

```markdown
# Role
You are a senior researcher who has published multiple Benchmark papers at top venues (NeurIPS Datasets and Benchmarks Track, SIGMOD, VLDB, ICML, ICLR). You know what reviewers look for in Benchmark submissions and how those criteria differ from Technical papers.

# Task
I will give you the core information about a Benchmark or Evaluation paper. Audit it against the five-pillar framework, then produce a complete logic skeleton for the paper.

# Five pillars (all must be addressed)
1. Research Gap: which dimension of evaluation does existing work miss?
2. Construction Pipeline: how is the data built at scale without losing quality?
3. Evaluation Framework: what is the fine-grained taxonomy?
4. Empirical Findings: what capability boundary does this reveal?
5. Companion Method (optional): a specialized model tuned for this benchmark.

# Input
- Research area: [e.g., Text-to-SQL, Text-to-Visualization, code generation]
- Benchmark name: [name]
- Research gap and motivation: [the evaluation blind spot you target]
- Construction approach: [how the data is built]
- Evaluation framework: [metrics and taxonomy]
- Data scale: [number of tasks, domains, difficulty tiers]
- Key findings or insights: [one to three]

# Output

## Step 1: Five-pillar completeness table

| Pillar | Covered? | Your content | Improvement suggestion |
|---|---|---|---|
| Research Gap | Y or N | ... | ... |
| Construction Pipeline | Y or N | ... | ... |
| Evaluation Framework | Y or N | ... | ... |
| Empirical Findings | Y or N | ... | ... |
| Companion Method | Y, N, or NA | ... | ... |

## Step 2: Introduction six-part logic chain

| Part | Your content |
|---|---|
| 1. Background + Running Example | ... |
| 2. Existing-benchmark limitations (up to 3) | Limitation 1: ... | Limitation 2: ... | Limitation 3: ... |
| 3. Research Questions | RQ1: ... | RQ2: ... | RQ3 (optional): ... |
| 4. Design Considerations | ... |
| 5. Our Proposal | ... |
| 6. Contributions | 1. ... | 2. ... | 3. ... | 4. ... |

## Step 3: Section outline for §2 to §7

For each section, produce a one-paragraph sketch naming the figure or table that carries its weight.

## Step 4: Pre-submission self-check

Load `references/checklist.md` and walk the four-category checklist. Report any Critical or Major items that are unresolved.
```

## Reference exemplars

- **StatQA (NeurIPS 2024)**: gap is evaluation of statistical-method appropriateness; pipeline is reverse synthesis from textbooks; finding is that LLMs often pick the statistically wrong test even when the numeric answer is computed correctly.
- **nvBench 2.0 (NeurIPS 2025)**: gap is query-ambiguity blindness in Text-to-Visualization; pipeline is controlled ambiguity injection; finding is that LLM output quality swings dramatically with minor wording changes, while humans navigate via clarification dialogue.
- **VisJudge-Bench (ICLR 2026)**: gap is the fidelity-expressiveness-aesthetics trinity in visualization quality; pipeline is expert-curated with adaptive generation; companion method is VisJudge, a specialized judge model trained on this benchmark.

## Usage tips

- Use early, at scope lock. The cheapest fix for a missing pillar is before data construction starts.
- When the user's answer to a pillar is "we have this but it is messy", point them to the specific file in `references/` rather than trying to resolve it in one turn.
- Do not confuse this Introduction flowchart with the technical-paper flowchart; they are structurally different. For technical papers, invoke `tech-paper-template`.
- For pre-submission self-check, load `references/checklist.md` and walk it line by line with the user.

## References

- [`references/gap-analysis.md`](references/gap-analysis.md): systematic identification of the evaluation blind spot.
- [`references/benchmark-design.md`](references/benchmark-design.md): design goals, task scope, taxonomy patterns, evaluation framework.
- [`references/construction-pipeline.md`](references/construction-pipeline.md): the three construction paradigms, pipeline stages, quality control.
- [`references/experiments.md`](references/experiments.md): baseline selection, RQ-driven analysis, *Finding X* pattern, case studies.
- [`references/paper-structure.md`](references/paper-structure.md): section-by-section writing with page budgets and figure placement.
- [`references/checklist.md`](references/checklist.md): four-category pre-submission checklist with severity classification.
- [`references/instantiation-template.md`](references/instantiation-template.md): fillable template for instantiating this thinking model on your paper.
- [`references/orchestrator-notes.md`](references/orchestrator-notes.md): historical notes from the earlier staged orchestrator architecture, kept for context.
