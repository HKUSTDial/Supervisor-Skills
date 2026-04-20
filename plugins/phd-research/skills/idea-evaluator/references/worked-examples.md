# Worked evaluations

## Table of contents

1. How to read these examples
2. Example A: Alpha-SQL (ICML 2025), incremental, Strong Accept
3. Example B: AFlow (ICLR 2025), cross-domain, Strong Accept
4. Example C: LEAD (VLDB 2026), new problem, Strong Accept
5. What each example illustrates

## 1. How to read these examples

Each example below is a retrospective evaluation of a published paper
as if the idea had been submitted for evaluation at the pre-writing
stage. The format matches the skill's output contract. The examples
ground the scoring rubric and the paradigm-shift probe in concrete
work. They are not predictions; the papers are already published and
accepted at their venues.

Sources: `handbook/06_Case_Studies/6.1_ICML_2025_Alpha-SQL*.md`,
`handbook/06_Case_Studies/6.2_ICLR_2025_AFlow*.md`,
`handbook/06_Case_Studies/6.3_VLDB_2026_LEAD*.md`.

## 2. Example A: Alpha-SQL (ICML 2025), incremental, Strong Accept

### Input (as if submitted for evaluation)

- Research area: Text-to-SQL with large language models.
- Core idea: introduce MCTS-style inference-time search to improve
  SQL generation accuracy on complex queries, without fine-tuning.
- Resources: strong coder, access to several A100 GPUs, 25 effective
  hours per week, five-month lifecycle target.

### Evaluation

**1. First impression.** Novel Method. One-sentence story: bring
search into the inference-time loop for an open-source Text-to-SQL
agent. Compelling for ICML because LLM agents are in scope and SQL
generation is a hot evaluation target.

**2. Lifecycle and capability match.**

| Aspect | Input | Assessment |
|---|---|---|
| Idea category | Application research | Lifecycle 3-6 months, fits five-month target |
| Weekly hours | 25 | Adequate for aggressive scope |
| Compute | Several A100 | Adequate for inference-only search |
| Fit | | Green |

**3. Five-dimension radar.**

| Dimension | Score | Evidence | Lift |
|---|---|---|---|
| Higher | 8 | MCTS is a principled search mechanism not used in open-source Text-to-SQL | Combine with schema augmentation |
| Faster | 3 | Search costs more tokens than direct generation | Add an early-exit for simple queries |
| Stronger | 5 | Search helps on hard queries but not on noisy inputs | Add intent-clarification |
| Cheaper | 4 | No new training data; but search adds inference cost | Cache search trajectories |
| Broader | 6 | Idea transfers to other constrained-generation tasks | Mention extensions |

**4. Paradigm-shift probe.**

| Principle | Answer | Rationale |
|---|---|---|
| First Principles | Partial | Challenges "more fine-tuning is the only way" |
| Elephant in the Room | No | Inference-time search is known in other contexts |
| Technology Cycle | Partial | Depends on instruction-tuned base models |
| Hamming's Rule | No | Important to SQL subfield but not community top-three |

Probe score: 2. Pure incremental; frame as Novel Method.

**5. Feasibility.** All risks green.

**6. Fatal flaws.** None at the fatal level. One MAJOR item: baseline
must include the latest closed-source model (otherwise F3).

**7. Integrity gate.** Pass.

**8. Verdict.** Strong Accept. Emphasise Higher and Broader in the
Introduction; preregister the Faster cost as a known limitation.

## 3. Example B: AFlow (ICLR 2025), cross-domain, Strong Accept

### Input

- Research area: LLM agent workflow generation.
- Core idea: cast workflow construction for code-generation agents as
  a search problem over symbolic-operator graphs, borrowing ideas
  from search-based neural architecture search.
- Resources: strong coder, GPU access, 30 hours per week, six-month
  lifecycle target.

### Evaluation

**1. First impression.** Novel Method with cross-domain framing. A
search-based view of agent workflows has not appeared in ICLR before.

**2. Lifecycle and capability match.** Green across all axes.

**3. Five-dimension radar.**

| Dimension | Score | Evidence | Lift |
|---|---|---|---|
| Higher | 7 | Accuracy gains on HumanEval when workflow is optimised | Add LiveCodeBench |
| Faster | 6 | Search overhead, but amortised over repeated tasks | Cache workflows |
| Stronger | 6 | Transfers across code-gen benchmarks | Test cross-model |
| Cheaper | 5 | No new data required | Use smaller operator library |
| Broader | 9 | Cross-domain transplantation from NAS to agent workflow design | Unify with tool-use agents |

**4. Paradigm-shift probe.**

| Principle | Answer | Rationale |
|---|---|---|
| First Principles | Partial | Challenges "prompt engineering is enough for agents" |
| Elephant in the Room | Partial | Workflow fragmentation is a known pain point |
| Technology Cycle | Yes | LLMs make operator-graph search meaningful |
| Hamming's Rule | Partial | Important for agent research |

Probe score: 5. Disruptive seeds present. Recommend
`disruptive-innovation-scout` for deepening the framing around
"workflow as a first-class object".

**5. Feasibility.** Green.

**6. Fatal flaws.** None. One MAJOR item: overclaim risk if the
operator library is too narrow (F10). Defense: preregister two
failure modes on unseen operator types.

**7. Integrity gate.** Pass.

**8. Verdict.** Strong Accept. Lead with Broader in the Introduction;
consider reframing as a new subfield (workflow-as-a-search-space).

## 4. Example C: LEAD (VLDB 2026), new problem, Strong Accept

### Input

- Research area: efficient LLM instruction tuning via data selection.
- Core idea: iterative data selection without any additional
  full-dataset inference, using the training loss already computed in
  the fine-tuning loop.
- Resources: strong coder, limited GPU budget, 20 hours per week, six-
  month target.

### Evaluation

**1. First impression.** Novel Problem / New Setting. The paper
defines the setting "zero-additional-inference iterative selection"
as the contribution, and provides the method.

**2. Lifecycle and capability match.**

| Aspect | Input | Assessment |
|---|---|---|
| Idea category | Data-intensive | Lifecycle 6-12 months; fits six-month tight |
| Weekly hours | 20 | Adequate if scope disciplined |
| Compute | Limited | This is fine because the method avoids full inference |
| Fit | | Green, slightly aggressive |

**3. Five-dimension radar.**

| Dimension | Score | Evidence | Lift |
|---|---|---|---|
| Higher | 7 | Matches or beats iterative selection baselines | Add safety-tuning benchmarks |
| Faster | 9 | Zero-extra-inference is an order-of-magnitude cost win | Quantify in wall-clock time |
| Stronger | 6 | Robust across instruction-tuning corpora | Add cross-domain test |
| Cheaper | 8 | Reuses training signal already computed | Release the selection code |
| Broader | 6 | Transfers to RLHF and safety tuning | Note in Discussion |

**4. Paradigm-shift probe.**

| Principle | Answer | Rationale |
|---|---|---|
| First Principles | Yes | Challenges "iterative methods require full inference" |
| Elephant in the Room | Partial | Selection cost is a known pain, not widely addressed |
| Technology Cycle | Partial | Instruction tuning only recently became a bottleneck |
| Hamming's Rule | Partial | Important to scale efficiency |

Probe score: 5. Disruptive seeds. Recommend
`disruptive-innovation-scout` for deepening the First Principles
framing.

**5. Feasibility.** Yellow on timeline; six months is aggressive for
a Data-intensive paper. Mitigation: preregister the main claim and
cut scope if experiments overrun at the four-month mark.

**6. Fatal flaws.** None at fatal level. One MAJOR: the central
training-loss-as-utility-signal claim must be rigorously tested
(F6). Defense: design the decisive ablation upfront.

**7. Integrity gate.** Pass.

**8. Verdict.** Strong Accept. Frame as Novel Problem in the
Introduction; lead with the First Principles probe result.

## 5. What each example illustrates

- Alpha-SQL is the canonical incremental pattern: high Higher score,
  low probe, Strong Accept with tight scope.
- AFlow shows the Broader-dominant pattern: a cross-domain
  transplant that earns its top-venue slot on novelty of framing.
- LEAD shows the New Problem pattern: a paradigm-shift probe at 5
  that is best served by a separate framing exercise before writing.

None of the three examples is Reject. A realistic evaluation corpus
includes many Reject outcomes, often driven by F1 (no novelty) or F5
(capability mismatch). Those examples are intentionally not
published; no archive source exists for them.
