# First Principles thinking

## Table of contents

1. Core idea
2. Technique A: assumption audit
3. Technique B: return to purpose
4. Worked example: Adaptive Query Processing
5. Worked example: Agent-driven data cleaning
6. Common misuses

## 1. Core idea

Do not start from the literature. Start from the physical or
mathematical essence of the problem. Existing solutions inherit
assumptions from the moment they were designed, and those assumptions
may have quietly stopped being true. First Principles thinking
strips a problem back to what is intrinsically required and asks
whether the path from requirement to current solution still holds.

The technique is deceptively simple: identify an assumption, test
whether it still holds, and, if it does not, propose a new solution
that does not require it.

## 2. Technique A: assumption audit

### Procedure

1. Write down the three most widely-held assumptions in the subfield.
   State each as a single declarative sentence.
2. For each assumption, write its original justification (why was it
   adopted in the first place?).
3. For each assumption, ask what has changed since that justification
   was established.
4. Rank the assumptions by fragility. An assumption whose justification
   depends on a condition that no longer holds is a candidate.
5. Pick the most fragile assumption and imagine a system that does
   not make it. What becomes possible?

### What a good assumption looks like

- Specific. "Data distribution is static" is better than "things are
  fixed".
- Historical. The audit names when and why the assumption was
  adopted.
- Testable. You can point to a concrete paper or system that still
  relies on it.
- Fragile. A recent technology or context shift weakens the
  justification.

## 3. Technique B: return to purpose

### Procedure

1. Ask: what is the user-facing goal of this task? Not the metric,
   the goal.
2. Ask: what are the intermediate steps the field has built to reach
   the goal?
3. Ask: for each intermediate step, is it required, or is it an
   accident of how the field grew?
4. Collapse any intermediate step that is not strictly required and
   ask what the result looks like.

### What return-to-purpose surfaces

- Steps that exist because they were needed under the old hardware
  regime, but are not needed now.
- Steps that exist because the original tools could only produce
  outputs at a certain level of abstraction.
- Steps that exist because specialist roles historically split the
  task.

## 4. Worked example: Adaptive Query Processing

- **Assumption**: "Database query plans must be fully determined
  before execution." Justification: the cost model expects static
  statistics and static workloads. Originally adopted in the 1970s.
- **What changed**: workloads and data distributions became dynamic;
  modern storage can observe intermediate results cheaply.
- **Reframing**: what if the query plan can change during execution
  based on observed data? This breaks the static-plan assumption and
  creates the Adaptive Query Processing research programme.
- **Impact**: decades of downstream work on runtime re-optimisation,
  parametric query plans, learned cardinality.

## 5. Worked example: Agent-driven data cleaning

- **Goal revisit**: the actual goal is to make downstream analysis or
  modelling correct. Data cleaning is an intermediate step.
- **Step audit**: traditional cleaning writes scripts independent of
  the downstream task. This was necessary when downstream tasks could
  not observe cleaning decisions.
- **Reframing**: what if an LLM agent observes the downstream
  task's feedback and iteratively rewrites cleaning strategies? The
  intermediate step collapses into a closed loop with the downstream
  task.
- **Impact**: Agent-driven Data Cleaning becomes a new direction
  rather than a tweak to existing cleaning pipelines.

## 6. Common misuses

- **Assumption theatre**: naming an assumption and pretending to
  break it, while the reframing still secretly relies on the same
  assumption. Check whether your reframing depends on the assumption
  anywhere in its pipeline.
- **Straw assumptions**: auditing assumptions that nobody in the
  field still holds. The audit should target live consensus, not
  historical views.
- **Unbounded reframing**: proposing a reframing that requires
  technology that does not exist yet. If the reframing needs
  something we will have in five years, record it on the Hamming's
  Rule list and move on; do not treat it as actionable today.
- **Skipping the justification audit**: if you cannot state why the
  assumption was originally adopted, you cannot judge whether the
  justification still holds.
