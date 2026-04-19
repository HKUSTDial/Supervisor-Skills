# Benchmark Construction Pipeline

## Contents

- [Pipeline Design Principles](#pipeline-design-principles)
- [Three Proven Construction Paradigms](#three-proven-construction-paradigms)
- [Pipeline Stages Specification](#pipeline-stages-specification)
- [Quality Control Strategies](#quality-control-strategies)
- [Statistical Characteristics (Section 2.3 Content)](#statistical-characteristics-section-23-content)
- [Pipeline Figure (Figure 2)](#pipeline-figure-figure-2)

Design a systematic, reproducible, and scalable data construction pipeline. The pipeline is the core technical contribution of a benchmark paper, equivalent to the "Method" section of a technique paper.

## Pipeline Design Principles

Every construction pipeline must satisfy three properties:

1. **Reproducibility**, another team can follow the same steps and get comparable data
2. **Scalability**, the pipeline can generate more data without proportionally more human effort
3. **Quality Assurance**, every data point passes explicit quality gates

## Three Proven Construction Paradigms

Choose the paradigm that best fits your task, or combine elements from multiple paradigms.

### Paradigm 1: Reverse Synthesis

**StatQA approach**, Fix the answer first, then generate the question.

```
Define answer space → Generate matching conditions → Compose questions → Validate uniqueness
     (enumerate)          (scenarios)                   (NL wrap)         (one correct answer)
```

**When to use:** The answer space is enumerable (e.g., statistical methods, chart types, code patterns). You need precise control over difficulty distribution and category balance.

**Key advantage:** Guarantees unambiguous ground truth by construction.

### Paradigm 2: Controlled Injection

**nvBench 2.0 approach**, Start from clean seeds, systematically inject the target phenomenon.

```
Collect clean seeds → Define injection types → Inject at calibrated levels → Validate naturalness
    (unambiguous)        (e.g., 4 types)         (e.g., 5 severity levels)    (human check)
```

**When to use:** You study a specific phenomenon (ambiguity, noise, bias, adversarial perturbation) and need controlled severity gradients across the phenomenon.

**Key advantage:** Isolates the variable of interest; enables severity-stratified analysis.

### Paradigm 3: Adaptive Generation plus Expert Annotation

**VisJudge-Bench approach**, Use LLMs to generate candidate data, then apply multi-stage human annotation.

```
LLM generates candidates → Stage-1 screening → Stage-2 fine-grained scoring → Stage-3 cross-validation
   (adapted to content)      (expert filter)       (multi-dimension)            (disagreement resolution)
```

**When to use:** The task requires nuanced human judgment that cannot be fully automated. Quality depends on expert assessment across multiple subjective dimensions.

**Key advantage:** Combines LLM scalability with human judgment quality.

Ask the user: "Which construction paradigm fits this project? Describe the data source and rough pipeline."

## Pipeline Stages Specification

<EXTREMELY-IMPORTANT>
The construction pipeline is what reviewers scrutinize most intensely. Every step must have explicit input, output, and key operations described in detail. Vague pipeline descriptions are a top rejection reason.
</EXTREMELY-IMPORTANT>

Regardless of paradigm, document every stage with this template:

| Stage | Input | Operation | Output | Quality Gate |
|-------|-------|-----------|--------|-------------|
| **1. Source Selection** | Raw data sources | Filtering, licensing, dedup | Clean source corpus | Coverage audit, license check |
| **2. Seed Generation** | Source corpus | [Paradigm-specific method] | Initial samples | Format validation, uniqueness |
| **3. Enrichment** | Initial samples | Add metadata, labels, tags | Annotated samples | Taxonomy coverage balance |
| **4. Quality Control** | Annotated samples | Human review / auto validation | Validated samples | IAA ≥ threshold |
| **5. Splitting** | Validated samples | Stratified train/dev/test split | Final dataset | Distribution balance check |

For each stage, be explicit about:
- **Who performs it** (automated script / LLM / human annotator / domain expert)
- **How long it takes** (per sample and total)
- **What can go wrong** and how you handle failures

## Quality Control Strategies

Document at least three strategies. Reviewers scrutinize this heavily:

| Strategy | Method | When to Use |
|----------|--------|------------|
| **Inter-Annotator Agreement** | Multiple annotators on same samples; report Cohen's κ, Fleiss' κ, or ICC (Intraclass Correlation Coefficient) | Any human annotation task |
| **Expert Spot-Check** | Domain expert reviews random ≥10% subset | Semi-automated pipelines |
| **Adversarial Validation** | Test if a classifier can distinguish synthetic vs. real data | Synthetic data generation |
| **Automated Sanity Checks** | Rule-based validation: format, range, consistency, deduplication | All pipelines |
| **Pilot Study** | Small-scale trial run (50-100 samples) before full construction | Complex multi-stage pipelines |
| **LLM Cross-Validation** | Use a different LLM family to verify LLM-generated data | LLM-in-the-loop pipelines |

## Statistical Characteristics (Section 2.3 Content)

After construction, present comprehensive statistics:

**Must-have (typically Table 2 + Figure 3-4):**
- Total sample count by split (train/dev/test)
- Distribution across taxonomy categories (bar chart or pie chart)
- Difficulty distribution (histogram)
- Text length / complexity distribution
- Scale comparison with existing benchmarks

**Recommended:**
- Word cloud or topic distribution
- Source diversity metrics
- 2-3 representative data examples as a Figure
- Annotation time and cost statistics

## Pipeline Figure (Figure 2)

The pipeline MUST be visualized. Design guidelines:

- **Left-to-right or top-to-bottom flow** with clear directionality
- **Each step**: labeled box with brief description
- **Between steps**: arrows annotated with data count (e.g., "10K → filtering → 8.5K")
- **Quality gates**: visually distinct (diamond shapes, colored borders, or gate icons)
- **Concrete example**: show one sample flowing through the entire pipeline
- **Paradigm label**: indicate which construction paradigm is used
