# Benchmark Architecture Design

## Contents

- [Element 1: Design Goals](#element-1-design-goals)
- [Element 2: Task Scope](#element-2-task-scope)
- [Element 3: Taxonomy Design](#element-3-taxonomy-design)
- [Element 4: Evaluation Framework](#element-4-evaluation-framework)
- [Element 5: Companion Method (Optional but Highly Recommended)](#element-5-companion-method-optional-but-highly-recommended)
- [Element 6: Contamination Mitigation Strategy](#element-6-contamination-mitigation-strategy)
- [Element 7: Difficulty Calibration](#element-7-difficulty-calibration)
- [Design Document Template](#design-document-template)

Design the conceptual blueprint of a benchmark, its goals, scope, taxonomy, evaluation framework, and optional companion method. This is the architectural plan before any data is built.

## Element 1: Design Goals

Every benchmark should explicitly state its design goals. Use the G1-G4 standard framework, plus custom goals as needed:

| Goal | Description | Typical Strategy |
|------|-------------|-----------------|
| **G1: Coverage** | Benchmark covers the breadth of the target capability | Systematic taxonomy, diverse sources, stratified sampling |
| **G2: Fine-grained Diagnostics** | Can pinpoint WHERE models fail, not just IF | Multi-dimensional taxonomy with sub-categories and difficulty levels |
| **G3: Scalability** | Construction is reproducible and extensible at low cost | Automated/semi-automated pipeline, minimal manual annotation |
| **G4: Quality** | Annotations are accurate and evaluation is reliable | Multi-stage QC, inter-annotator agreement, expert validation |

Ask the user: "How will the benchmark address each of these four goals? Are there any additional design goals to add?"

## Element 2: Task Scope

Clearly define the boundary. This pre-empts the reviewer question "why didn't you include X?"

```
Evaluates:
- [Capability 1]: [brief description]
- [Capability 2]: [brief description]
- ...

Does NOT evaluate (out of scope, with reason):
- [Excluded capability 1]: [why excluded, different research question, existing benchmarks already cover it, etc.]
- ...
```

## Element 3: Taxonomy Design

The taxonomy is the backbone of fine-grained evaluation. Choose from three proven patterns:

### Pattern 1: Capability × Difficulty Matrix (StatQA)

```
Categories:  [Cat1] [Cat2] [Cat3] [Cat4] [Cat5]
                    ×
Difficulty:  [Easy] [Hard]
             ──────────
             = 10 evaluation cells
```

**Best for**: Tasks where capabilities are naturally categorical with clear difficulty gradients.

### Pattern 2: Phenomenon Type × Severity Spectrum (nvBench 2.0)

```
Types:    [Type1] [Type2] [Type3] [Type4]
                  ×
Severity: [Lv1] [Lv2] [Lv3] [Lv4] [Lv5]
          ──────────
          = 20 evaluation cells
```

**Best for**: Tasks studying a specific phenomenon (ambiguity, noise, bias) across intensity levels.

### Pattern 3: Multi-dimensional Quality Framework (VisJudge-Bench)

```
Top Dimensions:    [Fidelity] [Expressiveness] [Aesthetics]
                         ↓              ↓                  ↓
Sub-dimensions:    [Sub1.1] [Sub1.2] [Sub2.1] [Sub2.2] [Sub3.1] [Sub3.2]
                   ──────────
                   = 6 measurable sub-dimensions
```

**Best for**: Tasks where quality has multiple independent facets that interact.

Ask the user: "Which taxonomy pattern best fits the evaluation dimensions? List the initial taxonomy."

## Element 4: Evaluation Framework

Beyond taxonomy, define HOW each dimension is measured:

| Sub-dimension | Metric | Scoring Method | Range | Automation |
|--------------|--------|---------------|-------|-----------|
| [SubDim 1] | e.g., Accuracy | Exact match | 0-1 | Fully auto |
| [SubDim 2] | e.g., Relevance | LLM-as-Judge | 1-5 | Semi-auto |
| [SubDim 3] | e.g., Naturalness | Human rating | 1-7 | Manual |

Key design decisions to discuss with the user:

| Decision | Options | Trade-off |
|----------|---------|-----------|
| **Auto vs. Human eval** | Automatic metrics / LLM-as-Judge / Human | Scale vs. reliability |
| **Single vs. Multi-answer** | One correct answer / Multiple valid answers | Simplicity vs. real-world fidelity |
| **LLM-as-Judge validation** | Correlation with human / Agreement rate | MUST validate if using LLM eval |
| **Scoring granularity** | Binary / Ordinal / Continuous | Discriminability vs. annotation difficulty |

## Element 5: Companion Method (Optional but Highly Recommended)

A companion method answers: "This benchmark not only evaluates, it also helps IMPROVE model capability."

| Component | Question | Example |
|-----------|----------|---------|
| **Training signal** | What data does the benchmark uniquely provide? | Step-wise reasoning paths, preference pairs, fine-grained scores |
| **Optimization technique** | How is the signal used? | SFT, DPO, GRPO, RLHF, curriculum learning |
| **Value proposition** | Why is this better than training without the benchmark? | Targeted improvement on the specific blind spot |

Reference implementations:

| Paper | Training Signal | Method | Technique |
|-------|----------------|--------|-----------|
| nvBench 2.0 | Step-wise reasoning paths | Step-Text2Vis | Step-DPO preference optimization |
| VisJudge-Bench | Fine-grained quality scores | VisJudge | GRPO reinforcement learning |

**This element significantly strengthens the paper.** Even a simple fine-tuning experiment showing improvement on the benchmark's target capability adds substantial value.

## Element 6: Contamination Mitigation Strategy

Reviewers increasingly care about data contamination. Specify how you prevent:

| Contamination Type | Risk | Mitigation |
|-------------------|------|------------|
| **Training contamination** | Benchmark data appears in model training sets | Time-gated construction, synthetic generation, novel data sources |
| **Prompt contamination** | Evaluation prompts leak into training | Unique prompt templates, private evaluation scripts |
| **Contamination laundering** | Using synthetic data from contaminated models to generate "new" data | Verify data provenance, cross-validate with non-LLM sources |
| **Benchmark saturation** | Models overfit to benchmark style over time | Design for extensibility, include version-control plan |

## Element 7: Difficulty Calibration

Top models should achieve only **~0.1-9% accuracy** on the hardest subset at launch (Ofir Press guideline). If top models score >50%, the benchmark may already be too easy. Include a difficulty sanity check:

- What do you expect top models to score? If too high, add harder subsets.
- Plan for benchmark longevity: include difficulty levels that challenge future models.

## Design Document Template

Help the user fill in this structured template:

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
  Pattern: [1/2/3]
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
  Expected top-model accuracy: [X%]
  Hardest subset target: [Y%]
```
