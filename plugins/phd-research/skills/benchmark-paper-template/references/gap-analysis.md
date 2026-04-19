# Benchmark Gap Analysis

Systematically identify and articulate an evaluation gap, the foundational question every benchmark paper must answer: **"What critical capability is NOT being evaluated, and why does that matter?"**

## Step 1: Survey the Evaluation Landscape

Help the user map what ALREADY exists. Build a comparison table (this becomes **Table 1** in the paper):

| Dimension | Benchmark A | Benchmark B | Benchmark C | ... | Gap |
|-----------|------------|------------|------------|-----|-----|
| Task scope | | | | | |
| Data scale | | | | | |
| Evaluation dimensions | | | | | |
| Granularity level | | | | | |
| Real-world alignment | | | | | |
| [Key differentiator] | ✗ | ✗ | ✗ | | **Ours** |

Guide the user with these questions:
- What mainstream benchmarks already exist in this area, and what does each one evaluate?
- What implicit assumption do they share, and does that assumption hold in realistic scenarios?
- If a model scored perfectly on every existing benchmark, would it really have mastered the underlying capability?

## Step 2: Identify the Blind Spot

The gap must be a **structural limitation** of existing evaluation, not "we need more data" or "we need a bigger dataset." Three proven gap patterns:

### Pattern A: Dimension Blindness
Existing benchmarks measure capability X but completely ignore related capability Y.

> **StatQA example**: Math reasoning benchmarks test whether models can compute correct answers, but completely ignore whether models can select the appropriate statistical method. A model that applies the wrong test but computes correctly would score perfectly, yet its reasoning is fundamentally flawed.

### Pattern B: Assumption Violation
Existing benchmarks share an implicit assumption that does not hold in real-world scenarios.

> **nvBench 2.0 example**: All Text-to-Visualization benchmarks assume each natural language query maps to exactly one correct visualization. In practice, real queries are inherently ambiguous, "show sales trends" could reasonably produce a line chart, bar chart, or area chart. Current benchmarks penalize valid alternative interpretations.

### Pattern C: Evaluation Granularity Mismatch
Existing evaluation is too coarse to diagnose specific failure modes.

> **VisJudge-Bench example**: Existing visualization evaluation checks surface aesthetics OR information accuracy in isolation. But real quality requires the interplay of Fidelity, Expressiveness, and Aesthetics. A chart can be beautiful but misleading, or accurate but incomprehensible.

**Ask the user:**
- Which gap pattern does the observed blind spot most resemble? (Dimension Blindness, Assumption Violation, or Granularity Mismatch)
- Can the user cite a concrete failure case where existing evaluation misses the real problem?

## Step 3: Validate the Gap

A gap is only worth a paper if it passes ALL four checks:

- [ ] **Practical impact**: Real users or applications encounter this problem
- [ ] **Measurable**: The gap can be quantified with concrete metrics, not just described qualitatively
- [ ] **Non-trivial**: Existing benchmarks cannot be trivially extended to cover it (adding a few samples is not enough)
- [ ] **Actionable**: Identifying this gap opens concrete research directions for model improvement

If any check fails, the gap needs refinement. Help the user iterate.

## Step 4: Articulate the Gap Statement

Draft a 2-3 sentence gap statement using this structure:

> **Existing benchmarks for [TASK] focus on [WHAT THEY MEASURE], operating under the assumption that [IMPLICIT ASSUMPTION]. However, in real-world scenarios, [WHY THE ASSUMPTION FAILS]. This creates a critical evaluation blind spot: [SPECIFIC CAPABILITY THAT CANNOT BE EVALUATED], meaning that [CONSEQUENCE, what can go wrong with models that appear to perform well].**

The gap statement must be:
- **Specific**, names the exact blind spot, not a vague "limitation"
- **Surprising**, challenges a common assumption the community takes for granted
- **Consequential**, shows real harm from the blind spot (not just theoretical incompleteness)

## Step 5: Derive Research Questions

Map the gap directly to 2-3 Research Questions. RQs should cover three areas:

| Coverage Area | RQ Template | Purpose |
|--------------|-------------|---------|
| **Benchmark construction** | How should we design a benchmark to systematically evaluate [the blind spot]? | Justify design choices |
| **Model capability boundary** | To what extent do current models fail on [the blind spot], and what sub-capabilities differentiate strong vs. weak models? | Establish severity + enable diagnosis |
| **Human-model gap** | How do models compare with human experts on [this dimension], and what factors (scale / prompting / domain knowledge) affect the gap? | Ground truth + actionable insights |

Typical RQ examples:

| RQ | Template | Maps to |
|----|----------|---------|
| RQ1 | To what extent do current models fail on [the blind spot]? | §4.2 Overall Performance |
| RQ2 | What specific sub-capabilities differentiate strong vs. weak models in [this dimension]? | §4.3 Fine-grained Analysis |
| RQ3 | How does [factor: model scale / prompting / domain knowledge] affect performance, and how do models compare with human experts? | §4.3 + Human vs. Model |

These RQs will drive the experiment design (bench-experiments) and structure the paper. Each RQ should correspond to a subsection in the experiments chapter.
