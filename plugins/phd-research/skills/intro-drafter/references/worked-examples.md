# Worked Introduction outlines

## Table of contents

1. How to read these examples
2. Example A: Alpha-SQL (ICML 2025), Technique
3. Example B: AFlow (ICLR 2025), Technique with cross-domain framing
4. Example C: LEAD (VLDB 2026), New Problem/Setting
5. What the examples teach

## 1. How to read these examples

Each example below reverse-engineers a published Introduction into
the six-paragraph outline this skill produces. The outlines are
faithful to the published papers, with some writing points
paraphrased. Sources are
`handbook/06_Case_Studies/6.1`, `6.2`, and
`6.3`.

The purpose is to show the outline at the level of detail this skill
should produce when given similar inputs.

## 2. Example A: Alpha-SQL (ICML 2025), Technique

### Type positioning

Technique Paper. Text-to-SQL is a long-established problem with
active benchmarks (Spider, BIRD). The contribution is a method:
MCTS-based inference-time search.

Paragraph 3 is a one-sentence bridge.

### Outline

1. **Background and Motivation**. Real-world Text-to-SQL applications
   in production analytics; running example: a multi-table aggregation
   query on a retail database. Existing open-source LLM-based SQL
   generators struggle on complex cases.
2. **Limitations of existing work**:
   - L1: prior open-source methods rely on single-pass generation and
     fail on complex JOIN reasoning.
   - L2: fine-tuning approaches are expensive and do not generalise
     across schemas.
   - L3 is not claimed; the paper uses only two limitations to keep
     focus.
3. **Problem essence and Goal**. Hard constraint: open-source
   deployable without fine-tuning. Goal bridge: "Our goal is to
   improve complex-query SQL generation on open-source LLMs without
   fine-tuning."
4. **Key challenges**:
   - Ch1: decision-space explosion when enumerating SQL candidates.
   - Ch2: reward modelling without a trained critic.
5. **Solution overview**. Alpha-SQL with MCTS-guided inference and
   self-supervised reward signals. Module A addresses Ch1 via
   structured search. Module B addresses Ch2 via execution feedback.
6. **Contributions**:
   1. MCTS-based inference search for Text-to-SQL (Section 3).
   2. Self-supervised reward design from execution feedback
      (Section 4).
   3. Experiments on BIRD and Spider, showing N-point accuracy gains
      over strong open-source baselines (Section 5).

## 3. Example B: AFlow (ICLR 2025), Technique with cross-domain framing

### Type positioning

Technique Paper, framed to emphasise Broader-dimension cross-domain
transplantation (operator search for agent workflows, borrowed from
neural architecture search).

Paragraph 3 bridges briefly; the Key Idea weight is in Paragraph 4
and 5.

### Outline

1. **Background and Motivation**. LLM agents for code generation;
   running example: an agent workflow for HumanEval tasks that fails
   when operators are mis-composed.
2. **Limitations of existing work**:
   - L1: prompt-engineering alone produces brittle workflows.
   - L2: single-agent architectures do not capture operator
     composition.
   - L3: hand-designed workflows do not generalise across task
     families.
3. **Problem essence and Goal**. Hard constraint: workflow design
   must generalise to unseen operators. Goal bridge: "Our goal is
   to automate workflow design for code-generation agents."
4. **Key challenges**:
   - Ch1: search space of operator graphs is combinatorial.
   - Ch2: evaluation signal for a workflow is discrete and sparse.
5. **Solution overview**. AFlow with operator-graph search (borrowed
   from NAS) and structured reward via code execution. Module A
   addresses Ch1; Module B addresses Ch2.
6. **Contributions**:
   1. Formulate agent-workflow design as operator-graph search
      (Section 2).
   2. AFlow algorithm with search guided by execution feedback
      (Section 3).
   3. Evaluation on HumanEval, MBPP, and adjacent benchmarks showing
      consistent gains over hand-designed and prompt-engineered
      workflows (Section 4).

## 4. Example C: LEAD (VLDB 2026), New Problem/Setting

### Type positioning

New Problem/Setting Paper. Paragraph 3 is load-bearing: the
contribution is the new setting "iterative data selection without
additional inference".

### Outline

1. **Background and Motivation**. LLM instruction tuning; data
   quality beats quantity. Running example: a 50k-sample instruction
   corpus where iterative selection improves tuning quality but
   incurs full-dataset inference per round.
2. **Limitations of existing work**:
   - L1: non-iterative selection does not adapt to model evolution.
   - L2: iterative methods require expensive full-dataset inference
     per round.
3. **Problem essence and Goal**. Hard constraint: no additional
   inference budget on top of the existing fine-tuning loop.
   Research question as the core contribution: "Can iterative
   selection benefits be preserved while eliminating repeated
   full-dataset inference?" Key Idea: use the training loss already
   computed inside the fine-tuning loop as a zero-overhead utility
   signal.
4. **Key challenges**:
   - Ch1: extract a reliable utility signal from noisy training-loss
     trajectories.
   - Ch2: integrate the selection signal into the training loop
     without disturbing convergence.
5. **Solution overview**. LEAD framework with Instance-level Dynamic
   Uncertainty (IDU) as the utility signal; selection runs inline
   with training. Module A addresses Ch1 via statistical
   denoising; Module B addresses Ch2 via deferred selection.
6. **Contributions**:
   1. Formulation of iterative data selection without additional
      inference as a new problem setting (Section 2).
   2. Instance-level Dynamic Uncertainty signal and its theoretical
      analysis (Sections 3, 4).
   3. LEAD framework design (Section 3).
   4. Extensive experiments on multiple instruction-tuning
      benchmarks, showing matched-or-better quality at an order-of-
      magnitude lower cost (Section 5).

## 5. What the examples teach

- Alpha-SQL shows a tight Technique Paper: three contributions, two
  limitations, two challenges. Focus wins.
- AFlow shows a Technique Paper with cross-domain framing: three
  contributions, three limitations, two challenges. The Broader-
  dimension framing earns the ICLR slot without changing type.
- LEAD shows a New Problem Paper: Paragraph 3 is load-bearing; the
  contributions include the problem setting itself as C1; the
  framework and method are C2-C4.
- All three have a one-to-one mapping between challenges and
  modules; none has more than three challenges. None has vague
  phrases as contributions.
- None reuses prior work in C1 without crediting prior limitations
  in Paragraph 2.
