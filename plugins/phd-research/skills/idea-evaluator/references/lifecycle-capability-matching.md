# Idea lifecycle and student capability matching

## Table of contents

1. Why lifecycle matters
2. The six-category lifecycle matrix
3. Capability self-assessment rubric
4. Matching logic
5. Mismatch detection and recovery
6. Worked examples

## 1. Why lifecycle matters

Every research idea has an expiry date. In fast-moving subfields like
LLM agents or Text-to-SQL, a purely applied idea may have a 3-to-6-
month lifecycle: if the student cannot finish coding, experiments,
writing, and submission in that window, another group likely will,
and the paper becomes hard to publish. In slower-moving subfields
like foundational theory, the lifecycle stretches past 12 months, but
the methodological depth required also stretches.

Lifecycle is not the same as difficulty. A short-lifecycle idea can be
executed by a skilled coder in 3 months; a long-lifecycle idea may
require 18 months of theoretical work before the first paper. The
mismatch question is always: can this student finish this idea within
its lifecycle?

The canonical rule: speed is not an excuse for low
quality. Fast iteration and submission means efficient work with full
quality control, not corner-cutting.

## 2. The six-category lifecycle matrix

| Category | Lifecycle | Suited student profile | Rationale |
|---|---|---|---|
| Application research | Short (3-6 months) | Strong coder, fast executor, can ship experiments quickly | Competitive, quickly obsolete fields; time-to-submission is decisive |
| Foundational theory | Long (6-12 months) | Strong mathematical base, deep thinker | Proofs and model building require sustained work |
| Cross-disciplinary | Medium (6-9 months) | Student with prior non-CS background | Domain expertise plus CS skills enables novel connections; often HCI venues |
| Frontier exploration | Short-to-medium (3-9 months) | Both theory and experiment capable, self-directed | New subfields require quick experiments and deep analysis |
| Data-intensive | Medium (6-12 months) | Strong data analysis, solid engineering | Data pipelines and model iteration are the critical path |
| Innovative technique | Long (12+ months) | Deep base, willing to challenge existing methods | Requires cross-field innovation; longer cycles are accepted |

## 3. Capability self-assessment rubric

Ask the user (or infer from their input) the following four inputs.
Record each on the scale shown.

### 3.1 Weekly effective hours

Effective hours mean focused, deep-work hours without meetings or
context switches. A rough calibration:

- Under 10 hours per week: top-venue publication is unlikely within a
  typical idea lifecycle unless execution is exceptional.
- 10-25 hours per week: feasible for medium-lifecycle ideas with
  disciplined scope management.
- 25-40 hours per week: feasible for short-lifecycle fast-moving
  ideas.
- 40+ hours per week: feasible for all lifecycles, but still bounded
  by the skill-depth axis below.

### 3.2 Skill depth

Rate strongest relevant skill on a 1-5 scale:

- Coding and experiment engineering (Python, PyTorch, deployment).
- Theoretical and mathematical maturity (proofs, derivations, model
  formulation).
- Data engineering (pipelines, annotation tools, cleaning at scale).
- Systems programming (low-level optimisation, concurrency).
- Domain knowledge (the target application area).

A student with 5 in coding and 2 in theory should prefer Application
or Data-intensive categories. A student with 2 in coding and 5 in
theory should prefer Foundational theory or Innovative technique.

### 3.3 Theoretical versus applied preference

On a 1-5 scale from pure-applied (1) to pure-theoretical (5). This is
a preference signal, not an ability signal: a student may be capable
of theory but happier shipping systems. Respect the preference; it
drives sustainability over the lifecycle.

### 3.4 Infrastructure access

Binary flags:

- Access to at least four large GPUs (A100 or equivalent): yes or no.
- Access to proprietary data or annotation budget: yes or no.
- Advisor or team weekly review cadence: yes or no.

Infrastructure access shortens lifecycle fit for certain categories
(large-GPU access is often required for data-intensive and
application research at the frontier).

## 4. Matching logic

Given a proposed idea and a capability profile:

1. Classify the idea into one of the six categories.
2. Look up the lifecycle range for that category.
3. Compute realistic execution time from capability:
   - coding + debugging time (estimate from scope)
   - experiment time (estimate from data and compute availability)
   - writing time (default: 3-6 weeks for a first draft)
   - revision time (default: 2-4 weeks)
4. Compare realistic execution time against lifecycle. If realistic
   time exceeds lifecycle, flag a mismatch.

## 5. Mismatch detection and recovery

### Detection flags

- **Lifecycle-short mismatch**: realistic execution exceeds 1.3x the
  lifecycle midpoint. High risk.
- **Capability-depth mismatch**: the category demands a skill at level
  4 or 5 that the student rates at 2 or below. Medium-to-high risk.
- **Infrastructure mismatch**: the category requires GPU or data
  access the student lacks. High risk.
- **Preference mismatch**: the category conflicts with the student's
  theoretical-applied preference. Medium risk; watch for drop-off.

### Recovery strategies

- **Narrow the scope**. Cut the idea to a well-scoped subproblem that
  fits the capability. Example: instead of a full Text-to-SQL Agent,
  tackle only schema-linking under ambiguity.
- **Partner with a collaborator**. Pair the student with someone whose
  skills complement the missing depth.
- **Change category**. Reframe the idea to fit a more compatible
  category. Example: reframe a foundational-theory idea as a
  data-intensive empirical study.
- **Extend the lifecycle**. Only feasible in slow-moving subfields;
  dangerous in fast-moving ones.
- **Switch the idea entirely**. If three or more mismatch flags
  exist, the idea is a poor fit. Better to pivot than to push.

## 6. Worked examples

### Example A: fit

- Idea: incremental improvement of Text-to-SQL accuracy via
  MCTS-based inference-time search.
- Category: Application research (short lifecycle, 3-6 months).
- Student capability: 5 in coding, 3 in theory, 20 weekly hours, four
  RTX 3090 GPUs available.
- Matching: coding (5) meets the demand; compute (four GPUs) is
  sufficient for BIRD-scale benchmarks; 20 weekly hours is tight but
  feasible with focused scope.
- Verdict: Green. Recommend a single-metric success criterion and a
  4-month timeline.

### Example B: mismatch

- Idea: a new theoretical framework for query-planner convergence
  under distribution shift.
- Category: Foundational theory (long lifecycle, 6-12 months).
- Student capability: 5 in coding, 2 in theory, 15 weekly hours,
  strong applied preference.
- Matching: theory (2) is below demand; preference is applied, not
  theoretical. Two mismatch flags.
- Verdict: Yellow. Reframe as an empirical study of planner behaviour
  under distribution shift, moving to Data-intensive category.
  Alternatively, partner with a theory-strong collaborator.

### Example C: high-risk fit

- Idea: a cross-disciplinary HCI study of how domain experts interact
  with AI-generated charts.
- Category: Cross-disciplinary (medium, 6-9 months).
- Student capability: background in statistics, 3 in coding,
  25 weekly hours, no IRB approval yet, no participant pool.
- Matching: coding (3) is adequate; infrastructure (no IRB, no pool)
  is blocking. One high-severity infrastructure mismatch.
- Verdict: Yellow. Secure IRB and recruit participants before writing
  any code; otherwise the 9-month window will be consumed by
  logistics.
