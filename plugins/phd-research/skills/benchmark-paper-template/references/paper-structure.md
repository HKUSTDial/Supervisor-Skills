# Benchmark Paper Structure & Writing

## Contents

- [Introduction: 6-Part Framework](#introduction-6-part-framework)
- [Critical Introduction Figures & Tables](#critical-introduction-figures--tables)
- [Main Body Section Structure](#main-body-section-structure)
- [Figure & Table Placement Guide](#figure--table-placement-guide)
- [Key Writing Techniques for Benchmark Papers](#key-writing-techniques-for-benchmark-papers)
- [Appendix Planning](#appendix-planning)

Organize and write a Benchmark/Evaluation paper. The Introduction is the "compressed version" of the entire paper, its narrative axis is NOT "Key Idea / Mechanism" but **"Evaluation Gap + Benchmark Design Rationale."**

## Introduction: 6-Part Framework

The Introduction is the "compressed version" of the entire paper. Its narrative axis is NOT "Key Idea / Mechanism" but **"Evaluation Gap + Benchmark Design Rationale."**

The Introduction should follow this exact logical chain. Each part maps to approximately one paragraph:

### Part 1: Background & Core Scenario (~1 paragraph)
- Establish importance of the broader task/domain in real-world scenarios
- Show the field has made rapid progress (cite recent advances)
- Use a carefully designed **Running Example (Figure 1)** to illustrate the task's complexity and how human experts handle it
- **Figure 1 is one of the most important figures in the entire paper, it must be meticulously crafted**
- **Tone**: Authoritative, citing well-known work

> **Reference**: StatQA uses a complete statistical analysis workflow; nvBench 2.0 shows multiple valid interpretations of an ambiguous query; VisJudge-Bench contrasts positive/negative examples across Fidelity/Expressiveness/Aesthetics.

### Part 2: Limitations of Existing Benchmarks, The Gap (~1 paragraph)
- Survey what existing benchmarks measure, acknowledge their contributions fairly
- Identify the IMPLICIT ASSUMPTION they all share, make it explicit
- Articulate the evaluation blind spot (≤3 points, specific not vague)
- **Strongly recommended**: provide a Benchmark Comparison Table (Table 1), comparing feature dimensions item by item to make the gap self-evident
- **This is the most important paragraph.** It should make the reader think: "I never considered that, but it's obviously important."

> **Reference**: nvBench 2.0 Table 1 compares 7 benchmarks across 6 dimensions; VisJudge-Bench Table 1 compares 7 benchmarks across 3 evaluation dimensions.

### Part 3: Research Questions (~1 paragraph)
- Transform the gap into 2-3 concrete Research Questions
- RQ coverage should span: (1) How to build an appropriate benchmark? (2) Where are the capability boundaries of current models? (3) What is the gap between models and human experts?
- RQs anchor the entire experiment section

> **Reference**: StatQA: Q1 How to evaluate? Q2 How capable are LLMs? Q3 Human vs. LLM?

### Part 4: Design Considerations (~1 paragraph)

<EXTREMELY-IMPORTANT>
This is a paragraph UNIQUE to Benchmark papers. Before introducing your solution, first articulate "what properties should a good benchmark have", this provides the rationale for your design choices.
</EXTREMELY-IMPORTANT>

- State design requirements explicitly (e.g., diverse coverage, fine-grained diagnostics, scalability, quality assurance)
- This provides the logical foundation for why your benchmark is designed the way it is

> **Reference**: nvBench 2.0: "This benchmark should include diverse ambiguous queries, multiple valid outputs, reasoning paths, and broad domain coverage."

### Part 5: Our Benchmark + Key Findings Preview (~1-2 paragraphs)
- Formally introduce: benchmark name, scale, key design choices
- Highlight construction methodology innovation in 1-2 sentences
- Reference Figure 1 and Table 1
- Summarize 2-3 most surprising empirical findings to entice the reader
- Use concrete numbers: "We evaluate 15 models across 6 dimensions"
- **Tone**: Confident but precise

> **Reference**: StatQA: "Our key idea is to reverse this process by synthesizing the question Q based on target answers A."

### Part 6: Contributions (~1 paragraph, bulleted list)
Typically 3-4 contributions, each mapping to a paper section:

1. We identify [the gap] and propose [Name], the first benchmark for [capability]. (→ §1-2)
2. We design [pipeline innovation] that achieves [quality/scale metric]. (→ §2)
3. We conduct comprehensive evaluation of [N] models and reveal [key finding]. (→ §4)
4. (Optional) We propose [companion method] that improves [metric] by [amount]. (→ §3)

## Critical Introduction Figures & Tables

### Figure 1: Running Example (MUST HAVE)
The most important figure in the paper. Requirements:

- Illustrates the evaluation gap with ONE concrete example
- Shows what existing evaluation misses vs. what yours captures
- Self-contained, a reader should grasp the paper's core idea from this figure alone
- Placed on page 1-2 (above the fold if possible)

**Design patterns:**
- **Split view**: "Existing evaluation" (left) vs. "Our evaluation" (right)
- **Walkthrough**: One input → multiple evaluation dimensions highlighted
- **Contrast**: Same model output scored by old criteria vs. new criteria

### Table 1: Benchmark Comparison (MUST HAVE)
Compare with 5-8 existing benchmarks. The rightmost column should be your key differentiator:

```
| Benchmark | Year | Scale | [Dim1] | [Dim2] | [Dim3] | [Your Key Feature] |
|-----------|------|-------|--------|--------|--------|--------------------|
| Prior-1   | 20XX | N     | ✓      | ✗      | ✓      | ✗                  |
| Prior-2   | 20XX | N     | ✓      | ✓      | ✗      | ✗                  |
| **Ours**  | 2025 | N     | **✓**  | **✓**  | **✓**  | **✓**              |
```

## Main Body Section Structure

### Section 2: The Proposed Benchmark (3-4 pages)

```
2.1 Design Goals & Task Scope
    - State G1-G4 explicitly
    - Define in-scope vs. out-of-scope

2.2 Benchmark Construction Pipeline
    - Pipeline overview paragraph
    - Figure 2: Pipeline flowchart (MUST HAVE)
    - Detailed steps with input → operation → output
    - Quality control measures
    - Annotation protocol (if human annotation involved)

2.3 Benchmark Characteristics
    - Table 2: Dataset statistics (splits, categories, scale)
    - Figure 3-4: Distribution charts (taxonomy, difficulty, length)
    - Figure 5: Data examples (2-3 representative samples)
    - Comparison with existing benchmarks on scale and coverage
```

### Section 3: Specialized Model (1-2 pages, optional)

```
3.1 Motivation, how the benchmark enables model improvement
3.2 Method, training signal + optimization technique
3.3 Implementation details
```

**This section answers**: "This benchmark not only evaluates, it helps improve models."

### Section 4: Experiments & Empirical Findings (4-5 pages)

```
4.1 Experimental Setup
    - Models (grouped by type), metrics, prompting, implementation

4.2 Overall Performance
    - Table 3: ALL models × ALL metrics (largest table in paper)
    - Bold best, underline second-best
    - Finding 1 after analysis

4.3 Fine-grained Analysis (organized by RQ)
    - RQ1 analysis → Finding 2
    - RQ2 analysis → Finding 3
    - RQ3 analysis → Finding 4
    - Each with supporting figure/table

4.4 Case Studies
    - 2-4 examples with qualitative analysis
    - Success case, failure case, surprising case
```

### Section 5: Discussion & Research Opportunities (~1 page)

Based on Findings, discuss:
- How to enhance model capability on the identified gap
- Human-AI collaboration patterns
- Benchmark extension directions (new modalities, languages, domains)
- Limitations of the current benchmark

### Section 6: Related Work (~1 page)

Organize into 2-3 subsections:
- [Task-specific] Benchmarks
- [Domain] Evaluation Methodologies
- [Related capability] in Large Language Models

**Include a comparison table** (can be expanded Table 1 or a new table focused on methodology differences).

**Placement note**: Related Work can go before or after Experiments. Before Experiments (like VisJudge-Bench) emphasizes positioning; after Experiments (like StatQA, nvBench 2.0) lets findings speak first.

### Section 7: Conclusion (~0.5 page)
- Restate the gap and benchmark in 1-2 sentences
- Summarize key findings (reference Finding numbers)
- Restate open problems and future directions

## Figure & Table Placement Guide

| Item | Position | Purpose | Priority |
|------|----------|---------|----------|
| Figure 1 | Page 1-2 | Running Example | MUST |
| Table 1 | Page 2-3 | Benchmark Comparison | MUST |
| Figure 2 | Page 3-4 (§2.2) | Construction Pipeline | MUST |
| Table 2 | Page 4-5 (§2.3) | Dataset Statistics | MUST |
| Figure 3-4 | Page 4-5 (§2.3) | Distribution Charts | HIGH |
| Figure 5 | Page 5 (§2.3) | Data Examples | HIGH |
| Table 3 | Page 6-7 (§4.2) | Overall Performance | MUST |
| Figure 6+ | Page 7-8 (§4.3) | Analysis Charts | HIGH |

## Key Writing Techniques for Benchmark Papers

1. **"Finding X" summaries**: Bold-highlight after each major analysis (see bench-experiments)
2. **Design rationale over description**: For every choice, explain WHY, not just WHAT
3. **Concrete numbers**: "We evaluate 15 models across 6 dimensions" not "many models"
4. **Active positioning**: "the FIRST benchmark to..." / "Unlike prior work, we..."
5. **Example-driven arguments**: Always pair abstract claims with concrete examples
6. **Appendix strategy**: Move detailed content to appendix (full results, annotation guidelines, more examples, prompts used)

## Appendix Planning

Standard appendix sections for benchmark papers:
- A: Full experimental results (all models × all metrics, unabridged)
- B: Annotation guidelines and interface screenshots
- C: Additional data examples
- D: Prompts used for evaluation
- E: Extended related work or taxonomy details
- F: Ethical considerations and datasheet
