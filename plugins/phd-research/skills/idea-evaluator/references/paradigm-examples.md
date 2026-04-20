# Canonical disruptive examples

## Table of contents

1. How to read these examples
2. Example 1: Transformer architecture
3. Example 2: Adaptive Query Processing
4. Example 3: Agent-driven data cleaning
5. Example 4: Multi-agent collaboration workflows
6. Lessons across examples

## 1. How to read these examples

Each example below traces a published or widely-adopted line of work
back to the disruptive reframing at its root. For each example, the
relevant principle (First Principles, Elephant in the Room,
Technology Cycle, Hamming's Rule) is identified. The purpose is to
show what a disruptive reframing looks like in the wild and to
calibrate the scout skill's output against real precedents.

Examples 2, 3, and 4 appear in
`handbook/02_Idea_Generation/2.3` as
illustrations for the principle they anchor.

## 2. Example 1: Transformer architecture

- **Context**: circa 2017, the machine-translation community's
  strongest models used complex CNN or RNN/LSTM architectures with
  attention as a secondary mechanism.
- **Consensus assumption**: sequential recurrence is required to
  model long-range dependencies.
- **Reframing (First Principles)**: what if attention alone is
  sufficient? The Google team dropped all recurrence and offered a
  pure-attention architecture, the Transformer.
- **Outcome**: the basis of essentially all subsequent large language
  models and the dominant architecture across NLP, vision, and
  speech.
- **Principle**: First Principles (assumption audit on recurrence)
  plus Technology Cycle (GPU compute enabled large all-attention
  models).

## 3. Example 2: Adaptive Query Processing

- **Context**: traditional database query optimisation.
- **Consensus assumption**: a query plan must be fully determined
  before execution; the optimiser uses static statistics.
- **Reframing (First Principles)**: what if statistics change during
  execution? Let the plan adapt to observed intermediate cardinalities.
- **Outcome**: a multi-decade research programme on runtime re-
  optimisation, progressive cardinality estimation, parametric
  query plans.
- **Principle**: First Principles (assumption audit on static plans)
  plus Elephant in the Room (production systems always saw plan
  failures due to estimation errors; academic world avoided this).

## 4. Example 3: Agent-driven data cleaning

- **Context**: traditional data cleaning uses standalone scripts
  (rules, heuristics, small models) independently of downstream use.
- **Consensus assumption**: cleaning is a preprocessing step
  decoupled from downstream tasks.
- **Reframing (Return to Purpose)**: the goal of cleaning is correct
  downstream analysis. Let an LLM agent observe downstream task
  performance and iteratively rewrite cleaning strategies.
- **Outcome**: agent-driven data cleaning becomes a research
  direction separate from classical cleaning; task-conditioned
  cleaning collapses the preprocessing step into a feedback loop.
- **Principle**: First Principles (return-to-purpose) plus Technology
  Cycle (LLM agents make the feedback loop tractable).

## 5. Example 4: Multi-agent collaboration workflows

- **Context**: single-agent LLM systems for complex business tasks.
- **Corner-case observation**: single agents loop, hallucinate, or
  spiral on multi-role, long-horizon tasks such as building a full
  web application end-to-end.
- **Consensus assumption**: more prompt engineering or longer
  context will fix multi-step failures.
- **Reframing (Elephant in the Room)**: single-agent failure is not
  a prompt-tuning problem; it is a coordination problem. Design a
  multi-agent framework with role separation and standard operating
  procedures.
- **Outcome**: a research programme around agent orchestration,
  multi-agent frameworks, agentic workflows, coordination protocols.
- **Principle**: Elephant in the Room (avoided hard problem of long-
  horizon multi-role tasks) plus Technology Cycle (LLM agent
  availability).

## 6. Lessons across examples

- All four examples combine two of the four principles. Single-
  principle reframings are often weaker; the strongest disruptive
  work triangulates between assumptions, pain-points, technology
  shifts, and important problems.
- Three of the four required a Technology Cycle element to be
  actionable. Without the shift, the reframing is either premature
  (the technology does not yet exist) or too late (the community has
  already absorbed it).
- None of the four is a one-paper contribution. Each opened a
  research programme that spanned years. A scout skill's output
  should aim for programme-scale reframings, not individual-paper
  tweaks.
- All four were risky at the time. The Transformer paper faced
  scepticism; Adaptive Query Processing was initially dismissed as
  impractical; agent-driven cleaning is still debated; multi-agent
  frameworks are still proving their value. Disruptive work lives
  with reception risk.
