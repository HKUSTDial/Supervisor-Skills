# Filled thinking templates

## Table of contents

1. How to read these examples
2. Example A: Alpha-SQL, Technique
3. Example B: AFlow, Technique with cross-domain framing
4. Example C: LEAD, New Problem/Setting
5. Cross-example observations

## 1. How to read these examples

Each example below is a retrospective filling of the thinking
template for a published paper. Ratings reflect what a strong
pre-submission filling looks like. Sources are
`handbook/06_Case_Studies/6.1`, `6.2`, and
`6.3`.

## 2. Example A: Alpha-SQL, Technique

### Paper-type positioning

Technique Paper. Text-to-SQL is well-established; contribution is a
new inference-time mechanism (MCTS search).

### Filled template

| Stage | Content |
|---|---|
| Research background | Text-to-SQL for enterprise analytics. Production use by analysts who do not know SQL. Recent work: OpenAI Codex, DIN-SQL, DailySQL |
| Limitation 1 | Single-pass prompting fails on complex multi-table JOIN queries |
| Limitation 2 | Fine-tuning on each schema is expensive and does not generalise |
| Key Idea | Use Monte Carlo Tree Search at inference time to explore SQL candidates and score them via execution feedback |
| Challenge 1 | SQL candidate space is combinatorial; naive search is intractable |
| Challenge 2 | No trained critic is available for inference-time reward |
| Methodology topic sentence | Alpha-SQL combines structured MCTS search over SQL parse trees with self-supervised reward from execution feedback |
| Module A (Challenge 1) | MCTS-guided SQL generation with learned expansion priors |
| Module B (Challenge 2) | Self-supervised reward via execution-based validation |
| Contribution 1 | MCTS-based Text-to-SQL inference framework (Section 3) |
| Contribution 2 | Self-supervised reward design (Section 4) |
| Contribution 3 | Experiments on BIRD and Spider with N-point gains (Section 5) |

### Consistency checks

- Check 1 (Limitations -> Key Idea): pass. Both limitations addressed
  by MCTS-at-inference.
- Check 2 (Key Idea -> Challenges): pass. Both challenges arise from
  MCTS.
- Check 3 (Challenges -> Methodology): pass. One-to-one mapping.
- Check 4 (Methodology -> Contributions): pass.

## 3. Example B: AFlow, Technique with cross-domain framing

### Paper-type positioning

Technique Paper, Mixed cross-domain. Operator-graph search
transplanted from NAS to agent workflow.

### Filled template

| Stage | Content |
|---|---|
| Research background | LLM agents for code generation; HumanEval and MBPP benchmarks; recent work on agent workflows |
| Limitation 1 | Prompt engineering alone yields brittle workflows |
| Limitation 2 | Single-agent architectures do not capture operator composition |
| Limitation 3 | Hand-designed workflows do not generalise across task families |
| Key Idea | Formulate agent-workflow design as search over operator graphs, borrowing from neural architecture search |
| Challenge 1 | Operator-graph search space is combinatorial |
| Challenge 2 | Reward signal for a workflow is discrete and sparse |
| Methodology topic sentence | AFlow combines operator-graph search guided by execution-based rewards |
| Module A (Challenge 1) | Operator-graph search with learned priors |
| Module B (Challenge 2) | Structured reward via code execution |
| Contribution 1 | Formulate workflow design as operator-graph search (Section 2) |
| Contribution 2 | AFlow search algorithm (Section 3) |
| Contribution 3 | Experiments on HumanEval, MBPP with consistent gains over hand-designed workflows (Section 4) |

### Consistency checks

- All four pass.
- Cross-domain framing is reflected in Contribution 1.

## 4. Example C: LEAD, New Problem/Setting

### Paper-type positioning

New Problem/Setting Paper. Goal carries the narrative.

### Filled template

| Stage | Content |
|---|---|
| Research background | Instruction tuning of LLMs; data quality beats quantity; recent work on iterative data selection |
| Limitation 1 | Non-iterative selection does not adapt to model evolution |
| Limitation 2 | Iterative methods require expensive full-dataset inference per round |
| Key Idea / Our Goal | (Goal) Iterative data selection without any additional inference overhead. (Key Idea) Use the training loss already computed inside the fine-tuning loop as a zero-overhead utility signal |
| Challenge 1 | Extract a reliable utility signal from noisy training-loss trajectories |
| Challenge 2 | Integrate the selection signal into the training loop without disturbing convergence |
| Methodology topic sentence | LEAD uses Instance-level Dynamic Uncertainty as a utility signal and defers selection to a cadence that preserves convergence |
| Module A (Challenge 1) | Instance-level Dynamic Uncertainty signal with statistical denoising |
| Module B (Challenge 2) | Deferred selection integrated into the fine-tuning loop |
| Contribution 1 | Problem formulation: iterative data selection without additional inference (Section 2) |
| Contribution 2 | Instance-level Dynamic Uncertainty with theoretical analysis (Sections 3, 4) |
| Contribution 3 | LEAD framework design (Section 3) |
| Contribution 4 | Extensive experiments (Section 5) |

### Consistency checks

- All four pass.
- Contribution 1 directly encodes the Goal.

## 5. Cross-example observations

- All three examples use 2 or 3 limitations, 2 challenges, 2 methodology
  modules. The consistency of these counts is not accidental.
- All three examples pass the four consistency checks. This is the
  minimum bar for a strong top-venue submission.
- The New Problem/Setting example (LEAD) has four contributions
  because the problem formulation takes one contribution slot,
  leaving three for the method and experiments.
- The Mixed case (AFlow) leads with the cross-domain framing in
  Contribution 1. This is the canonical pattern for cross-domain
  Technique papers.
- None of the three examples contains a vague contribution. Every
  contribution is specific and maps to a section.
