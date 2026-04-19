# Benchmark Gap Analysis

## Why this matters

The single most common rejection pattern for a benchmark paper at NeurIPS
Datasets and Benchmarks, ICLR, ICML, ACL, EMNLP, or CVPR is reviewer
confusion about why the benchmark needs to exist. A reviewer opens the
Introduction and finds a paragraph explaining that the authors "built a
new benchmark for X because current evaluation is limited", but the
limitation is left vague or described only in quantitative terms (more
samples, wider coverage). The reviewer has seen dozens of these papers
and rejects on the grounds that the contribution is incremental, a bigger
dataset rather than a new evaluation paradigm. A defensible gap statement,
named, specific, and surprising, is what separates an accepted benchmark
paper from a rejected one.

A gap statement is not free-form creative writing. It follows a template,
and the reasoning behind it follows one of three validated patterns. This
skill externalises the pattern-matching that senior advisors run silently
so that a PhD student without direct advisor access can run it themselves
before committing to a construction pipeline. Running gap analysis before
design is not optional: the rest of the paper (design goals, taxonomy,
experiments, findings) depends on the gap. A weak gap produces a weak
paper no matter how well the pipeline is built.

## The framework

The skill runs in five steps, with a hard gate blocking forward motion to
benchmark design until the user confirms a clear gap statement and
research questions.

### Step 1: Survey the evaluation landscape

The first step is not writing, it is cataloguing. The user builds a
comparison table covering the 5+ most relevant existing benchmarks in the
target area. The table becomes Table 1 of the final paper, so the effort
has immediate downstream payoff.

| Dimension | Benchmark A | Benchmark B | Benchmark C | ... | Gap |
|---|---|---|---|---|---|
| Task scope | ... | ... | ... | | |
| Data scale | ... | ... | ... | | |
| Evaluation dimensions | ... | ... | ... | | |
| Granularity level | ... | ... | ... | | |
| Real-world alignment | ... | ... | ... | | |
| Key differentiator | absent | absent | absent | | **Ours** |

The guiding questions at this stage:

- What mainstream benchmarks already exist in this area, and what does
  each one evaluate?
- What implicit assumption do they share, and does that assumption hold
  in realistic scenarios?
- If a model scored perfectly on every existing benchmark, would it
  really have mastered the underlying capability?

The last question is the most important. If the answer is yes, there is
no gap worth a paper. If the answer is no, the missing element is the
start of a gap statement.

### Step 2: Identify the blind spot using one of three patterns

A real gap is a structural limitation of existing evaluation, not a call
for more data or a bigger dataset. The skill uses three validated gap
patterns, each with a reference benchmark as a worked example.

**Pattern A: Dimension Blindness.** Existing benchmarks measure capability
X but completely ignore a related capability Y. The model that scores
high on existing benchmarks may have mastered X but not Y, and nobody has
detected this because nobody is measuring Y. StatQA uncovered this
pattern in math reasoning: existing math benchmarks score whether the
model computes the correct answer, but ignore whether the model selected
the appropriate statistical method. A model that applies the wrong test
but computes correctly scores perfectly, yet its reasoning is
fundamentally flawed.

**Pattern B: Assumption Violation.** Existing benchmarks share an implicit
assumption that does not hold in real-world scenarios. A model that
scores high is optimising for the simplifying assumption, not for the
real task. nvBench 2.0 uncovered this in text-to-visualisation: existing
benchmarks assume each natural-language query maps to exactly one correct
visualisation. In practice, real queries are inherently ambiguous. A
query like "show sales trends" could reasonably produce a line chart, a
bar chart, or an area chart, depending on context. Current benchmarks
penalise valid alternative interpretations, which is exactly backward.

**Pattern C: Granularity Mismatch.** Existing evaluation is too coarse to
diagnose specific failure modes. Benchmarks produce a single aggregate
score, but the score hides which sub-capability the model actually lacks.
VisJudge-Bench uncovered this in visualisation evaluation: existing
evaluation checks surface aesthetics OR information accuracy in
isolation, but real quality requires the interplay of Fidelity,
Expressiveness, and Aesthetics. A chart can be beautiful but misleading,
or accurate but incomprehensible. A coarse binary "good chart / bad
chart" score cannot distinguish these failure modes.

The skill asks the user to name which pattern the observed blind spot
most resembles, and to cite a concrete failure case where existing
evaluation misses the real problem. A user who cannot name the pattern or
cite a concrete case is not yet ready to write a benchmark paper.

### Step 3: Validate the gap against four checks

A gap is only worth a paper if it passes all four checks. A single failed
check means the gap needs refinement.

- **Practical impact**: real users or applications encounter this
  problem. Not a theoretical gap; a gap whose absence causes harm.
- **Measurable**: the gap can be quantified with concrete metrics, not
  just described qualitatively. If the gap is "models lack common sense",
  the check fails because there is no obvious metric.
- **Non-trivial**: existing benchmarks cannot be trivially extended to
  cover the gap (adding a few samples is not enough). If the gap can be
  closed by a simple extension, the gap is not structural.
- **Actionable**: identifying the gap opens concrete research directions
  for model improvement. If the gap is interesting but nobody can act on
  it, the paper generates no follow-ups.

The four checks are a short-circuit. If any one fails, the skill helps
the user iterate before moving on. Moving forward on a gap that fails one
check wastes months.

### Step 4: Articulate the gap statement

The gap statement is the single most important sentence in the paper. It
follows a structured template:

> Existing benchmarks for [TASK] focus on [WHAT THEY MEASURE], operating
> under the assumption that [IMPLICIT ASSUMPTION]. However, in real-world
> scenarios, [WHY THE ASSUMPTION FAILS]. This creates a critical
> evaluation blind spot: [SPECIFIC CAPABILITY THAT CANNOT BE EVALUATED],
> meaning that [CONSEQUENCE, what can go wrong with models that appear
> to perform well].

The statement must be specific (names the exact blind spot, not a vague
limitation), surprising (challenges a common assumption the community
takes for granted), and consequential (shows real harm from the blind
spot, not just theoretical incompleteness).

### Step 5: Derive two or three research questions

The gap maps directly to 2-3 research questions that will drive the
experiment section. Each RQ becomes a subsection in the paper's
experiments chapter.

| Coverage area | RQ template | Purpose |
|---|---|---|
| Benchmark construction | How should we design a benchmark to systematically evaluate [the blind spot]? | Justify design choices |
| Model capability boundary | To what extent do current models fail on [the blind spot], and what sub-capabilities differentiate strong from weak models? | Establish severity and enable diagnosis |
| Human-model gap | How do models compare with human experts on [this dimension], and what factors (scale, prompting, domain knowledge) affect the gap? | Ground truth plus actionable insights |

## Named heuristics

- **Three gap patterns**: Dimension Blindness, Assumption Violation,
  Granularity Mismatch. Every publishable benchmark gap fits one of
  these. A gap that fits none is usually a dataset-release in disguise.
- **Four validation checks**: practical impact, measurable, non-trivial,
  actionable. All four must pass.
- **Gap statement template**: structured five-clause form. Specific,
  surprising, consequential.
- **RQ three-area coverage**: construction, model boundary, human-model
  comparison. Missing any of the three usually means the paper will feel
  thin on insight.
- **Hard gate before design**: no benchmark design until the user can
  articulate the gap in 2-3 sentences and confirms it passes all four
  checks.

## Worked example

Consider a PhD student proposing a benchmark for evaluating text-to-SQL
systems on business-intelligence queries. The initial framing is "current
text-to-SQL benchmarks have limited query complexity, so we build a
harder one". This framing fails the skill immediately: it matches no gap
pattern, fails the non-trivial check (the existing BIRD benchmark could
be extended with more complex queries), and has no clear RQ coverage.

The skill pushes the student to survey existing benchmarks: Spider, BIRD,
Spider 2.0, AmbigSQL, KaggleDBQA. In mapping these across dimensions, the
student notices that every benchmark evaluates a single-turn query with a
single correct SQL output. Real business-intelligence work involves
multi-turn conversations where the analyst iteratively refines the query,
and where the same question might produce multiple valid SQL outputs
depending on schema interpretation.

That is a Pattern B gap (Assumption Violation): all existing benchmarks
share the implicit assumption that text-to-SQL is single-turn and
unambiguous. The student passes the four validation checks: real BI
analysts work multi-turn (practical impact), conversation quality can be
measured (measurable), existing benchmarks cannot be trivially extended
because they lack the conversational structure (non-trivial), and the
gap suggests new training paradigms for conversational text-to-SQL
(actionable).

The gap statement becomes: "Existing text-to-SQL benchmarks for
business intelligence focus on single-turn accuracy, operating under the
assumption that analyst queries are complete and unambiguous at first
pass. However, in real-world BI workflows, analysts iteratively refine
queries through multi-turn dialogue with ambiguous schema references.
This creates a critical evaluation blind spot: the ability to maintain
schema grounding, track reference resolution, and update query
semantics across turns, meaning that a model scoring perfectly on
single-turn benchmarks may still fail catastrophically when deployed
into a real BI dashboard."

Research questions: RQ1 (how to build a multi-turn ambiguous
text-to-SQL benchmark), RQ2 (which sub-capabilities, schema tracking,
reference resolution, semantic updating, differentiate strong from weak
models), RQ3 (how do models compare with human analysts, and does
domain knowledge help close the gap). The student can now advance to
[bench-design](../bench-design/overview.md) with a locked gap.

StatQA, nvBench 2.0, and VisJudge-Bench each exemplify one pattern, and
the skill uses them as templates for the student's own work. StatQA
(Dimension Blindness) took math reasoning from "compute correctness" to
"method selection plus compute correctness". nvBench 2.0 (Assumption
Violation) took text-to-visualisation from "one correct chart" to
"multiple valid interpretations with preference". VisJudge-Bench
(Granularity Mismatch) took visualisation evaluation from "accuracy or
aesthetics in isolation" to "Fidelity plus Expressiveness plus
Aesthetics as an interacting triple".

## Try it with the plugin

Install the plugin per the [root README](../../../../README.md) and
invoke naturally. The skill self-triggers on phrases from its SKILL.md
description such as "starting a new benchmark project", "analysing what
existing benchmarks miss", or "I want to build a benchmark for X".
Describe the target area in a paragraph covering what benchmarks already
exist, what you think is missing, and why that matters. The skill will
map the proposed gap to one of the three patterns, run the four
validation checks, and help draft the gap statement and research
questions.

## Source

Adapted from
[archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md)
and the live plugin file
[/plugins/phd-research/skills/bench-gap-analysis/SKILL.md](/plugins/phd-research/skills/bench-gap-analysis/SKILL.md).

---

[English] | [中文](../../../zh/skills/bench-gap-analysis/overview.md)
