# Five-dimension scoring framework

## Table of contents

1. Origin and purpose
2. Dimension 1: Higher (Effectiveness)
3. Dimension 2: Faster (Efficiency)
4. Dimension 3: Stronger (Robustness and Generalisation)
5. Dimension 4: Cheaper (Data or Solution Cost)
6. Dimension 5: Broader (Cross-Domain and Unification)
7. Scoring rubric
8. Summary table
9. Common scoring failures

## 1. Origin and purpose

This framework comes from the methodology for generating
incremental research ideas given a strong baseline. The insight is:
do not hunt for new problems with a solution in hand; instead, take a
well-defined baseline and ask on which of five axes it can be
improved. Each axis has canonical entry strategies and concrete
examples.

The same framework flips naturally into an evaluation lens: given an
idea, score how strongly it advances each axis versus the current
baseline. Strong ideas usually dominate on one axis and hold their own
on at least one more. Weak ideas are vague on four or more axes.

## 2. Dimension 1: Higher (Effectiveness)

### Definition

Improves accuracy, quality, or effectiveness metrics over the
strongest current baseline.

### Canonical entry strategies

- **Information or modality augmentation**. Does the baseline ignore
  an input signal that would help? Example: Text-to-SQL models using
  only schema plus query may improve significantly when fed data
  distribution or domain documents.
- **Feedback-driven refinement**. Can execution feedback (compiler
  errors, runtime exceptions, test failures) drive iterative
  self-correction? Example: LLM code-generation success rates jump
  when errors from the execution environment are returned to the
  agent for self-reflection.
- **Error-driven root-cause analysis**. Run the baseline, cluster
  failures, identify the dominant failure mode, and build a module
  that targets it. Example: if Text-to-SQL failures concentrate on
  complex JOIN operations, design a sub-agent that decomposes JOIN
  logic.

### How to score

- 9-10: the idea proposes a principled new input signal or feedback
  loop that no prior work exploits, with a plausible path to
  multi-point accuracy gains.
- 6-8: the idea combines known signals or applies a known feedback
  mechanism in a new setting; expected gains are modest but real.
- 3-5: the idea is a standard prompt-engineering or fine-tuning
  variant; gains will likely be within noise of stronger baselines.
- 1-2: the idea does not obviously advance effectiveness at all.

### Grounded example

Alpha-SQL (ICML 2025): introduces MCTS-based inference-time search
for Text-to-SQL. Higher score: 8. Evidence: principled search
mechanism that no prior open-source Text-to-SQL work had applied;
multi-point accuracy gains on BIRD. Lift: pair with schema
augmentation for additional signal.

## 3. Dimension 2: Faster (Efficiency)

### Definition

Reduces wall-clock time, token cost, memory footprint, or compute
budget while preserving effectiveness.

### Canonical entry strategies

- **Caching and experience reuse**. Cache successful trajectories so
  repeated tasks do not replan from scratch. Example: an LLM agent
  that retrieves and reuses past successful plans for similar tasks.
- **Parallelisation and decoupling**. Break a long serial pipeline into
  independent sub-tasks handled by specialised agents running in
  parallel. Example: a multi-agent data-analysis framework with one
  agent per step (ingestion, transformation, visualisation).
- **Early exit and dynamic routing**. Route simple cases to cheap
  models, escalate only hard cases. Example: a cascade that uses a
  small model for filtering and only invokes a large model on
  ambiguous instances.

### How to score

- 9-10: the idea identifies a large, well-quantified efficiency gap
  and proposes a principled mechanism that closes it (more than 3x
  speedup with no accuracy loss).
- 6-8: the idea targets a known efficiency bottleneck with a plausible
  mechanism; gains are 1.5x-3x.
- 3-5: the idea mentions efficiency but lacks a specific mechanism;
  gains will likely be marginal.
- 1-2: the idea does not address efficiency.

### Grounded example

LEAD (VLDB 2026): eliminates per-iteration full-dataset inference in
iterative instruction-tuning data selection. Faster score: 9.
Evidence: zero-additional-inference overhead is a principled gap
closed; replaces expensive utility-score computation with training-
loss signal already computed.

## 4. Dimension 3: Stronger (Robustness and Generalisation)

### Definition

Maintains performance under noise, out-of-distribution inputs, or
cross-domain transfer.

### Canonical entry strategies

- **Noise tolerance and fault tolerance**. Handle malformed or
  ambiguous inputs gracefully. Example: intent-clarification modules
  that ask users for disambiguation instead of failing silently.
- **Exception recovery**. Detect API failures, unexpected outputs, or
  tool crashes and retry with alternatives. Example: an agent that
  falls back to a simpler tool when the primary one returns an
  unexpected response.
- **Decoupled representations**. Separate general reasoning from
  domain-specific knowledge so the same reasoning module transfers
  zero-shot to new domains.

### How to score

- 9-10: the idea directly addresses a known brittleness (ambiguity,
  OOD, domain shift) with a principled mechanism and plans
  cross-domain evaluation.
- 6-8: the idea mentions robustness with a concrete mechanism but
  evaluates on a single domain.
- 3-5: the idea pays lip service to robustness without a mechanism.
- 1-2: the idea does not address robustness.

### Grounded example

An agent framework that decouples planning from domain-specific APIs
and ships cross-domain evaluation: Stronger score 8. Evidence: clear
zero-shot transfer story and principled decoupling.

## 5. Dimension 4: Cheaper (Data or Solution Cost)

### Definition

Reduces data annotation cost, training cost, or deployment cost while
preserving effectiveness.

### Canonical entry strategies

- **LLM-based data synthesis**. Use a strong foundation model to
  synthesise labelled training data or simulate agent trajectories,
  reducing human annotation demand.
- **Active learning with human in the loop**. Select the smallest set
  of samples for human review that maximises model improvement,
  rather than annotating the whole corpus.
- **Knowledge distillation**. Distill a large model's reasoning paths
  into a small deployable model, preserving accuracy at lower
  inference cost.

### How to score

- 9-10: the idea produces a high-quality dataset at a fraction of
  naive-annotation cost, or deploys at an order-of-magnitude lower
  cost than the baseline.
- 6-8: the idea reduces cost by a factor of 2-5 through a known
  mechanism.
- 3-5: cost reduction is mentioned but not quantified.
- 1-2: the idea does not consider cost.

### Grounded example

StatQA's reverse-synthesis pipeline (NeurIPS 2024 D&B) reduced
annotation cost by generating questions from verified answers,
side-stepping manual question writing. Cheaper score 8.

## 6. Dimension 5: Broader (Cross-Domain and Unification)

### Definition

Transplants a mature idea from one domain to another, or unifies a
fragmented set of tasks under a single framework.

### Canonical entry strategies

- **Cross-domain transplantation**. Take a mature technique from one
  field and apply it to another. Example: database query optimisers
  bring cost estimation and plan caching to LLM-agent planning.
- **Generalisation and unification**. Unify a family of tasks (Text
  to SQL, Text to Python, Text to Chart) under a single data-agent
  framework with one shared underlying structure.

### How to score

- 9-10: transplants a mature technique in a non-obvious direction with
  a plausible mechanism; or unifies three or more previously
  fragmented task families.
- 6-8: transplants a known idea; or unifies two task families.
- 3-5: suggests a connection to another domain without concrete
  mechanism.
- 1-2: the idea is siloed.

### Grounded example

AFlow (ICLR 2025): transplanted search-based workflow generation from
neural-architecture-search-style methods to agent pipeline design.
Broader score 8. Evidence: crossed a domain boundary with a principled
mechanism.

## 7. Scoring rubric

For each dimension, assign an integer 1-10 based on the tiers above.
Then aggregate as follows:

- Top dimension at 8+ and a second dimension at 6+: this is the
  paper's thesis. Emphasise these two in the Introduction.
- Three or more dimensions at 5 or below: the idea is thin. Either
  find the dimension where the idea really shines and sharpen it, or
  pivot.
- All five dimensions at 4 or below: Reject and Pivot.
- No single dimension reaches 7: the idea is vague. Ask the user to
  name the single dominant axis before re-evaluating.

## 8. Summary table

| Dimension | Core goal | Entry strategies | Illustrative example |
|---|---|---|---|
| Higher | Accuracy and effectiveness gains | Information or modality augmentation; feedback-driven refinement; error-driven root-cause analysis | MCTS inference in Alpha-SQL |
| Faster | Efficiency and cost reduction | Caching and experience reuse; parallelisation and decoupling; early exit and dynamic routing | Zero-inference data selection in LEAD |
| Stronger | Robustness and generalisation | Noise and fault tolerance; exception recovery; decoupled representations | Intent-clarification agents |
| Cheaper | Data or solution cost | LLM-based synthesis; active learning; knowledge distillation | Reverse-synthesis in StatQA |
| Broader | Cross-domain and unification | Cross-domain transplantation; abstraction and unification | Workflow search in AFlow |

## 9. Common scoring failures

- **Inflation**: scoring every dimension 7 or 8 "to be generous"
  destroys the signal. Use 5 as the default and justify upward.
- **Deflation**: scoring every dimension 3 or 4 signals that you did
  not understand the idea; re-read.
- **Uncited evidence**: a score without a specific sentence from the
  user's idea pointing at why is not a real score.
- **Generic lift suggestions**: "try a different prompt" is not a
  lift. Name the entry strategy from this file.
- **Score and verdict mismatch**: a Strong Accept verdict with no
  dimension above 7 is incoherent. Realign.
