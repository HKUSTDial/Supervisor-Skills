---
name: write-top-tier-ml-paper
description: >-
  Builds reviewer-auditable argument structures for empirical machine
  learning, computer vision, and multimodal method papers. It maps diagnostic
  observations to design principles, method components, falsifiable claims,
  experiments, and figures, then produces paragraph-level section contracts
  and an evidence-gap audit. Use when a paper reads like a module inventory,
  when experiments do not close the contribution loop, or when efficiency,
  losslessness, and generality claims need calibration.
license: CC-BY-NC-SA-4.0
---

# Write Top-Tier ML Paper

## Overview

Turn a research idea or partial result set into one verifiable argument. Make
the reader able to answer five questions without reconstructing the logic:

1. Where does the existing approach fail in an important regime?
2. What evidence identifies the claimed failure mechanism?
3. Which design principle follows from that evidence?
4. How does each method component implement that principle?
5. Which experiment proves effectiveness, mechanism, efficiency, robustness,
   and boundary conditions?

This skill plans and audits an empirical method paper. It does not fabricate
results, replace literature verification, or write unsupported prose.

## Source basis and boundaries

Use the four public arXiv papers below as structural case studies, not as prose
templates:

- TaylorSeer: https://arxiv.org/html/2503.06923v1
- ToCa: https://arxiv.org/html/2410.05317
- VidCom2: https://arxiv.org/html/2505.14454
- GlobalCom2: https://arxiv.org/html/2501.05179

The workflow is an original synthesis of their argument patterns. Paraphrase
all source ideas, distinguish correlation from causation, and never imply that
an arXiv version has a particular conference status. For the full case-study
decomposition, see: references/paper-patterns.md.

## Collect the minimum inputs

Extract the following before planning. Mark missing items as evidence gaps
instead of inventing them:

- task, real-world cost, and target use regime
- closest method family and its default assumption
- one reproducible failure case
- observation, hypothesis, or theory that supports the new method
- intervention and smallest defensible component set
- available datasets, models, baselines, metrics, hardware, and results
- intended contribution boundary, known failure cases, and target venue

## Stage 1: Write the research spine

Write one sentence before any section outline:

> Because [old paradigm] fails in [important regime] through [mechanism], we
> exploit [verifiable observation] and apply [core intervention] to obtain
> [measurable benefit] while preserving [constraint].

Reject a spine that needs more than one primary failure mechanism or one
primary intervention. Move secondary ideas to implementation details or
future work.

## Stage 2: Build the claim ladder

Build six claim levels in order:

1. **Problem**: the cost or failure matters.
2. **Diagnosis**: the existing approach fails in the target regime.
3. **Principle**: the observation implies a concrete design rule.
4. **Mechanism**: the proposed component changes the intended behavior.
5. **Outcome**: the method improves quality and real cost under fair budgets.
6. **Generality**: the result holds across meaningful settings and has stated
   limits.

Assign at least one evidence item to every claim. If evidence is missing,
weaken the claim or mark the experiment as required. Do not compensate with
stronger adjectives.

## Stage 3: Choose one narrative archetype

Pick one primary archetype. Combine patterns only when the research truly
requires both.

### Paradigm replacement

Use this when the existing method has a structural ceiling. Show the ceiling,
establish a new exploitable property, and replace the old operation. TaylorSeer
uses this pattern by moving from feature reuse to feature forecasting.

### Heterogeneous allocation

Use this when average treatment hides large differences among units. Prove
that tokens, layers, crops, frames, or timesteps have different importance or
risk, then allocate computation or retention adaptively. ToCa, GlobalCom2,
and VidCom2 use variants of this pattern.

### Hierarchical coordination

Use this when local decisions lack global context. Prove that global and local
signals are complementary, then use global context to guide local allocation.

Create a separate Analysis section when the problem redefinition or diagnostic
observation is itself a contribution. Keep a compact diagnostic in the
Introduction and Method opening when it is only supporting motivation.

## Stage 4: Build the claim-evidence ledger

Create this table before promising contributions:

| Claim | Reviewer question | Minimum evidence | Main-paper location | Status |
|---|---|---|---|---|
| C1: the problem exists | Is the failure real? | distribution, probe, or intervention | Figure 1 / Analysis | missing or available |
| C2: the diagnosis is correct | Why does it fail? | controlled mechanism test | Figure 2 | missing or available |
| C3: the method works | Is it better at equal cost? | multi-budget table or Pareto curve | Table 1 / Figure 4 | missing or available |
| C4: components are necessary | What causes the gain? | principle-aligned ablation | Table 2 | missing or available |
| C5: it is practically efficient | Do FLOPs become real savings? | latency, memory, throughput, overhead | Table 3 | missing or available |
| C6: it generalizes | Is it a single-setting trick? | model, task, scale, or budget transfer | Table 4 | missing or available |

Treat the ledger as the paper's contract. Remove any Introduction contribution
that has no evidence route.

## Stage 5: Design evidence before prose

Draw empty tables and figure storyboards first. Use the experiment reference
to select fair budgets, baselines, ablations, mechanism tests, efficiency
measurements, and boundary studies. See:
references/experiments-and-figures.md.

Draft in evidence-dependency order:

1. experiment questions, protocols, and table headers
2. method definitions, algorithms, and complexity
3. Introduction promises that the evidence can support
4. Related Work positioning against the nearest assumptions
5. Abstract, title, conclusion, and limitations

Do not call a method `lossless` or `accuracy-preserving` without a predefined
non-inferiority margin and uncertainty estimate relative to the unmodified
model.

## Stage 6: Enforce section contracts

Use the paragraph-level reference for complete contracts and drafting order.
See: references/section-paragraph-blueprints.md.

### Title

Express the conceptual change or mechanism and the target task or benefit.
Prefer an informative distinction over a stack of adjectives and acronyms.

### Abstract

Fill six slots: context and cost, existing solution, precise gap, diagnostic
observation, method mechanism, and cross-setting quantitative evidence. Use
only one to three discriminative numbers with their comparison condition.

### Introduction

Make consecutive paragraphs perform these roles: importance, attractive
existing solution, precise failure, diagnostic evidence, design principle,
method mechanism, result preview, and contributions. Merge adjacent roles
when appropriate, but never omit the bridge from evidence to design.

### Related Work

Group papers by solution route, not year. End each group with its shared limit.
Compare the closest work by decision unit, required signal, training or search
cost, operator compatibility, and target regime.

### Analysis or Motivation

State the setting, run a controlled probe, quantify the difference, name the
observation, and derive one design implication. Make each observation
reproducible and reference it explicitly from the matching method component.

### Method

Give only necessary preliminaries, then one overview. Write every component as
local problem, intuition, definition, algorithmic action, complexity, and link
to the motivating observation. Explain a formula before and after displaying
it. Never let notation substitute for reasoning.

### Experiments

Order the evidence as protocol, main comparison, real efficiency, component
ablation, mechanism validation, robustness or generality, and qualitative
cases. Start each result paragraph with the conclusion, then give matched
numbers and explain which claim they test. Describe causal mechanisms only
when the experiment identifies them.

### Conclusion and limitations

Close the problem, observation, method, evidence, and boundary loop. Add no new
contribution. State untested scales, dependencies, overhead, and failure
regimes concretely.

## Stage 7: Plan the main-paper visual narrative

Assign one primary conclusion to each visual:

1. **Teaser or failure figure**: why the old approach is insufficient.
2. **Diagnostic figure**: what structural evidence supports the new idea.
3. **Method overview**: inputs, decision units, signals, actions, and outputs.
4. **Main trade-off**: quality versus real cost over multiple budgets.
5. **Mechanism or ablation visual**: how intermediate behavior changes.
6. **Qualitative failure cases**: which task-relevant errors improve or remain.

Write self-contained captions that name the setting, comparison, visual
encoding, and take-away.

## Stage 8: Use claim-first paragraphs

Default to `C-E-R-L`:

- **Claim**: state the paragraph's only conclusion.
- **Evidence**: give setting, comparator, and key measurements.
- **Reasoning**: explain why the evidence supports the conclusion.
- **Link**: connect to the next paragraph or the paper-level claim.

Do not narrate table cells. Report the main trend, one representative number,
the stress regime or exception, and the evidence-bounded interpretation.

## Final audit

Check every item before delivery:

- Does every contribution have a named experiment?
- Does every method component follow from an observation or constraint?
- Are strong baselines compared at matched token, compute, or latency budgets?
- Are refresh schedules and real-computation counts fixed when estimators are
  compared?
- Are end-to-end latency, peak memory, throughput, and selection overhead
  reported alongside FLOPs?
- Do ablations test design judgments rather than only code switches?
- Are random seeds, sample counts, hardware, precision, input size, and key
  hyperparameters specified?
- Are negative regimes and representative failures visible?
- Do Abstract, Introduction, tables, and Conclusion use identical numbers?
- Is every use of `lossless`, `general`, or `plug-and-play` supported by the
  corresponding uncertainty, transfer, and integration evidence?

## Default output

Return these artifacts in order:

1. one-sentence research spine
2. three or four bounded contribution claims
3. claim-evidence ledger
4. section-by-section, paragraph-by-paragraph blueprint
5. prioritized experiment plan
6. main figure and table storyboard
7. missing evidence and the most dangerous reviewer questions
8. prose only when the user explicitly requests drafting
