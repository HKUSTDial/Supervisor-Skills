# Section and paragraph blueprints

## Table of contents

1. Whole-paper logic
2. Title
3. Abstract
4. Introduction
5. Related Work
6. Analysis or Motivation
7. Method
8. Experiments
9. Conclusion and limitations
10. Paragraph microstructures
11. Drafting order

## 1. Whole-paper logic

Build three closed loops.

### Problem loop

`important regime -> existing solution -> precise failure -> controlled evidence -> bounded diagnosis`

Do not turn a correlation into a causal diagnosis. When the probe is not
causal, describe the result as an observation or a pattern.

### Design loop

`observation -> design principle -> component -> intermediate behavior`

For every component, answer three questions: which observation motivates it,
which decision it changes, and which measurable behavior should change when
the component is enabled.

### Evidence loop

`claim -> experiment -> metric -> result -> interpretation -> boundary`

Make each experiment answer one primary reviewer question. A claim may need
multiple complementary experiments, but an experiment should not be justified
by several unrelated claims.

## 2. Title

Prefer one of these structures:

- `[old operation] to [new operation]: [benefit] with [method]`
- `[core mechanism] for [target task or system]`
- `[method]: [property] [method family] for [task]`

Check whether the title communicates both difference and purpose. Lead with
the mechanism when the method name is not memorable. Lead with the method name
only when it helps identification.

## 3. Abstract

Use six sentence slots. Merge the observation and method sentences only when
space is tight.

| Slot | Job | Include | Avoid |
|---|---|---|---|
| 1 | Context and cost | task value, bottleneck, use regime | field history |
| 2 | Existing solution | current paradigm and its attraction | long taxonomy |
| 3 | Precise gap | failure condition, consequence, scale | "challenges remain" |
| 4 | Observation | verifiable fact that enables the method | immediate method naming |
| 5 | Mechanism | decision unit, signal, action, constraint | "novel framework" alone |
| 6 | Evidence | multiple settings, real cost, key numbers | one best-case point |

Template:

> [System] performs strongly on [task], but [cost] limits [regime]. Existing
> [paradigm] reduces the cost by [operation]. We find that it fails under
> [condition] because [bounded diagnosis], producing [consequence]. Our
> analysis shows [observation], which suggests [design principle]. We propose
> [method], which uses [component A] and [component B] while preserving
> [constraint]. Across [models, tasks, or datasets], it obtains [quality] at
> [budget] and improves [real efficiency metric].

## 4. Introduction

Use seven or eight paragraphs. Each paragraph should have one job.

### Paragraph 1: establish importance and real cost

- Name the task or system and why it matters.
- Move quickly to latency, memory, throughput, token count, or deployment cost.
- End with the concrete optimization problem.

A useful closing move is: "This raises the question of how to reduce X while
preserving Y in regime Z."

### Paragraph 2: explain why the existing solution is attractive

- Introduce only the nearest method family.
- Explain its operation and practical attraction, such as training-free or
  plug-and-play use.
- Surface its implicit assumption so the next paragraph can test it.

### Paragraph 3: define the failure regime

- Name the stress condition, such as long intervals, extreme compression,
  long videos, multiview input, or shallow-layer error propagation.
- Name the failure type, such as quality loss, semantic inconsistency, detail
  loss, memory overhead, or operator incompatibility.
- End with one magnitude or pattern that points to a main-paper figure.

Use numbered problems only when the problems are independent and every one
later maps to a design principle.

### Paragraph 4: present diagnostic evidence

- Describe the probe before announcing the method.
- Name the measured unit, controlled variables, and size of the observed
  difference.
- Compress the result into one reusable statement, such as "tokens differ in
  error propagation" or "feature trajectories remain locally predictable."

### Paragraph 5: derive the design principle

- State "therefore, a method should..." explicitly.
- Explain why the rule bypasses the old limitation.
- Map each principle to one preceding problem.

Do not introduce components before the principle that justifies them.

### Paragraph 6: give the method overview

- State the paradigm-level distinction first.
- Describe two or three actions: what is measured, what is allocated, and what
  is selected, reused, or predicted.
- State practical constraints such as no training, fixed average budget, or
  efficient-operator compatibility.
- Point to the overview figure.

### Paragraph 7: preview discriminative evidence

- Report cross-model or cross-task results, not a single dataset.
- Pair quality with actual efficiency.
- Highlight the stress regime in which the old assumption is weakest.
- Copy numbers exactly from the main tables.

### Paragraph 8: list contributions

Organize contributions as understanding, method, and evidence:

1. **Understanding**: identify or quantify a neglected structure or failure.
2. **Method**: formulate the principle and its implementation.
3. **Evidence**: establish the quality-cost trade-off over a bounded scope.

Use falsifiable verbs such as `identify`, `quantify`, `formulate`, and
`demonstrate`. Use `first`, `novel`, and `significant` only with appropriate
search or statistical evidence.

## 5. Related Work

### Opening: define the classification axis

Choose an axis that helps position the paper, such as sampling-step reduction
versus denoiser acceleration, pre-LLM versus intra-LLM compression, or
single-view versus multiview processing.

### Each topic paragraph

1. State the route's shared objective.
2. Group representative methods by mechanism.
3. End with the route's shared limit in the target regime.

Avoid chronological paper-by-paper summaries.

### Final paragraph: align the nearest work

Compare the nearest methods on:

- decision granularity: model, layer, token, crop, frame, or timestep
- required information: historical feature, attention, global representation,
  or text signal
- cost: training, search, auxiliary model, explicit attention, or sorting
- boundary: architecture, operator, budget, input length, and task

Related Work must establish that the same problem has not already been solved
under the same assumptions and evidence protocol.

## 6. Analysis or Motivation

Create this section when a new observation is the method's foundation.

### 6.1 Problem setup

- Define the minimal system and notation.
- State the diagnostic question.
- Explain why an aggregate final metric cannot answer that question.

### 6.2 Probe 1: establish heterogeneity or trajectory structure

- Define the measurement, such as distance, error propagation, uniqueness, or
  attention.
- Hold other variables constant.
- Show a distribution and representative examples.
- State `Observation 1` in reproducible terms.

### 6.3 Probe 2: connect the structure to task consequences

- Intervene by removing high-score versus low-score units, injecting equal
  perturbations, changing only the interval, or reversing input order.
- Compare final task outcomes.
- State `Observation 2` without exceeding the causal strength of the design.

### 6.4 Derive design implications

| Observation | Design principle | Method action |
|---|---|---|
| units differ in sensitivity | allocate budget non-uniformly | adaptive ratio |
| global and local signals complement | combine perspectives | holistic score |
| a trajectory is smooth and predictable | forecast rather than hold | state prediction |
| early errors propagate more strongly | vary budgets by depth | layer schedule |

## 7. Method

### 7.1 Preliminaries

Include only the model flow, symbols, and baseline formula needed to understand
the contribution. End by identifying the precise missing term or invalid
assumption in the baseline.

### 7.2 Overview

- Restate inputs, outputs, budget, and stages in one paragraph.
- Use one overview figure for data flow and decision points.
- Let prose explain why and pseudocode explain execution.

### 7.3 Component paragraph pattern

Use six moves for each component:

1. State the local problem.
2. Explain why the direct approach fails.
3. Refer to the matching observation.
4. Define the representation, score, budget, or predictor.
5. Explain direction, extrema, normalization, and constraints.
6. State the output, next-stage use, and additional cost.

### 7.4 Theory, error, or complexity

- Prove only a property on which the method or claim depends.
- State assumptions and scope.
- Explain what the result predicts about hyperparameters or stress regimes.
- Report implementation cost in addition to asymptotic complexity.

### 7.5 Architecture variants

When a core signal is absent from some models, such as a class token, define a
replacement and test it across architectures. Do not hide compatibility that
is essential to a plug-and-play claim in the appendix.

## 8. Experiments

### 8.1 Experimental setting

Report, in order:

1. tasks, datasets, and sample counts
2. models and checkpoints
3. baselines and why they are included
4. budget alignment rule
5. quality and efficiency metrics
6. hardware, precision, batch, input size, steps, and seeds
7. default hyperparameters and selection procedure

### 8.2 Main comparison

Write by conclusion, not table order:

1. overall Pareto advantage
2. representative matched-budget result
3. stress regime and exceptions
4. interpretation bounded by the experiment

### 8.3 Efficiency

Report end-to-end latency, target-module latency, peak memory, throughput,
scoring or sorting overhead, and theoretical compute. State compatibility with
efficient attention, compilation, quantization, or other relevant operators.

### 8.4 Ablation

Test design decisions rather than code switches:

- uniform versus adaptive allocation
- local-only versus global-only versus combined information
- zero-, first-, and higher-order prediction
- random versus proposed scoring
- shared versus depth-aware or type-aware budgets
- component by stress-budget interaction

### 8.5 Mechanism analysis

Show whether intermediate behavior changes as predicted. Useful visuals
include selection masks, frame or crop budgets, error curves, feature
trajectories, cache frequency, and positional bias.

### 8.6 Robustness and generality

Choose at least two meaningful axes: architecture, scale, task, dataset,
resolution, video length, sampler, budget, or hardware. State whether the same
hyperparameters transfer or each setting is tuned.

### 8.7 Qualitative results

Select cases by error type: text corruption, object omission, color shift,
motion discontinuity, detail loss, or hallucination. Fix input, prompt, seed,
and budget. Include representative failures, at least in the appendix.

## 9. Conclusion and limitations

Use three or four sentences: old limitation, key observation, method change,
and evidence scope. State concrete limitations such as untested scales,
required signals, memory or ranking overhead, extreme budgets, and streaming
settings.

## 10. Paragraph microstructures

### Claim-Evidence-Reasoning-Link

> Adaptive allocation becomes more important at extreme compression. At a
> 10 percent retention budget, it improves the matched score by X over uniform
> allocation, while the gap is Y at 50 percent. Low budgets amplify the cost of
> allocating tokens to redundant units, which is consistent with the proposed
> heterogeneity diagnosis. The next analysis tests whether the selected units
> follow that diagnosis.

### Result paragraph

> The method forms a stronger quality-cost frontier over all tested budgets.
> At 25 percent retention, it changes the task score from A to B relative to
> the strongest matched baseline while reducing end-to-end latency by C. The
> gain is concentrated in fine-detail tasks, which is consistent with the
> preserved-region analysis. The evidence does not cover untested model sizes.

### Negative result paragraph

> The method does not improve over the baseline in setting X. This setting
> lacks signal Y on which the method depends, so the supported scope is Z. The
> paper therefore does not extend its claim to the uncovered regime.

## 11. Drafting order

1. Write the research spine and bounded contributions.
2. Build the claim-evidence ledger.
3. Draw empty tables, Pareto axes, and the overview figure.
4. Write Analysis and Method subsection topic sentences.
5. Draft result paragraphs from real evidence.
6. Write the Introduction backward from supported claims.
7. Compress the story into Abstract and title.
8. Finish Related Work, Conclusion, limitations, and appendix routing.
