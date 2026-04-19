# Running example design

## Table of contents

1. What a running example is
2. Why it matters
3. Design principles
4. Two design patterns
5. Worked examples
6. Common failures

## 1. What a running example is

A running example is a specific, concrete scenario that appears in
the Introduction (typically as Figure 1), in the Problem Formulation
or Methodology to illustrate the definition and the method's
operation, and in the Experiments as a case study. It is the same
example throughout, not different examples per section.

A strong running example turns an abstract research claim into a
tangible story the reader can follow in 30 seconds.

## 2. Why it matters

Reviewers read 10 to 30 papers per cycle; their attention is finite.
An Introduction that opens with abstract claims loses the reader's
interest before the contribution lands. A running example gives the
reader something concrete to hold on to, and later sections can
refer back to it instead of reintroducing new examples.

Running examples also help the writer. The discipline of fitting the
method to a single example exposes vague steps that look fine in
prose but break in practice.

## 3. Design principles

- **Real**. The example is drawn from real data or a real deployment,
  not fabricated.
- **Specific**. The example names concrete entities: tables,
  queries, datasets, file paths, measurements. Abstractions come
  later.
- **Simple yet complete**. The example is small enough to fit on one
  figure, and complete enough to exhibit the problem's full
  complexity.
- **Recurring**. The same example appears in Introduction, Problem
  Formulation, Methodology (worked through), and Experiments (as a
  case study). The reader should experience a closed narrative loop.
- **Failure-revealing**. The example clearly shows where existing
  methods fail. A generic example that everyone would solve
  correctly is not useful.

## 4. Two design patterns

### Pattern A: Real scenario plus concrete failure

The example shows a concrete real scenario and then shows what goes
wrong under the prior method. This is the most versatile pattern.

Template:

1. Describe the scenario concretely (entity names, measurements).
2. Show what a user expects.
3. Show what the prior method produces, and name the specific
   failure (wrong result, missed case, wrong decision).
4. Foreshadow how the paper's method handles it.

### Pattern B: Side-by-side good versus bad

The example places a correct output next to an incorrect one,
emphasising the single dimension where current methods break.

Template:

1. Show two outputs for the same input, labelled Correct and
   Incorrect.
2. Annotate the single dimension where they differ.
3. State that prior methods produce the Incorrect output; your paper
   aims to produce the Correct output.

This pattern works well when the contribution is evaluation-
oriented (a judge, a scorer, a corrector) rather than
generation-oriented.

## 5. Worked examples

### Text-to-SQL running example (Pattern A)

Scenario: a user asks "Which products in the last quarter had the
highest sales growth compared to the quarter before?" on a retail
database with Orders, Products, and Stores tables.

Expected: a SQL query that joins the three tables, groups by
product, windows over the two quarters, and computes growth.

Prior method failure: the generated SQL omits the JOIN between
Orders and Stores, causing the result to include products from
stores the user did not care about, inflating the output by
thousands of rows.

Paper's method: introduces schema-level JOIN-reasoning that detects
the missing JOIN and inserts it. The example reappears in Section 3
as the walkthrough, and in Section 5 as Case Study 1.

### Visualisation-quality example (Pattern B)

Side-by-side: two charts showing the same data. The Correct chart
uses a log scale that makes small differences visible and labels the
axis in meaningful units. The Incorrect chart uses a linear scale
and unlabelled units, making the data appear uniform.

Prior method: scores both charts similarly on aesthetics; ignores
the fidelity difference.

Paper's method: decomposes quality into Fidelity and Aesthetics axes
and scores the log-scale chart higher on Fidelity. Example reappears
in Section 3's scoring-rubric explanation and in Section 5.

## 6. Common failures

- **Generic running example**: a toy dataset or a textbook query.
  Reviewers infer the method only works on toys.
- **Non-failing running example**: the example is specific but any
  prior method would handle it correctly. The reader cannot see why
  the paper is needed.
- **Running example abandoned after Introduction**: appears in
  Figure 1 and never returns. Reviewers lose the narrative thread.
- **Multiple running examples**: one per section. Readers get
  confused about which is canonical.
- **Running example too complex**: fits only with extensive
  explanation. The 30-second test fails.
- **Running example with contrived details**: entities named Entity1,
  Entity2 rather than real names. Reviewers infer the example is
  fabricated.
