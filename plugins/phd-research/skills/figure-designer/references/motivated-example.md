# Motivated Example (Figure 1) design

## Table of contents

1. Why Figure 1 matters
2. Paradigm A: Running Example plus Failure Case
3. Paradigm B: Existing vs Ours
4. Paradigm C: Performance Teaser
5. Design principles
6. Tool recommendations

## 1. Why Figure 1 matters

Figure 1 is the single most important figure in the paper. It
appears on page 1 or at the top of page 2, immediately after the
Limitations paragraph in the Introduction. Its job is to convey in
under 30 seconds (a) what problem the paper tackles and (b) why
current methods do not solve it. Reviewers decide whether to read
the rest of the paper partly based on this figure.

Budget one to two working days on Figure 1. This is not excessive;
it pays back across the entire review cycle.

## 2. Paradigm A: Running Example plus Failure Case (recommended)

The most persuasive paradigm. Show a real, specific scenario and
then show what goes wrong under the current method.

### Layout

A two-panel or three-panel figure:

- Panel 1 (top or left): the real input. Natural language query,
  image, sensor trace, or whatever the task takes.
- Panel 2 (middle or centre): what a current method produces. The
  incorrect output. Highlight the error with red.
- Panel 3 (optional, right or bottom): what the paper's method
  produces or promises. The correct output. Highlight with green.

### When to use

- The problem is concrete and the failure is easy to show.
- Text-to-SQL, code generation, visualisation, agent workflows.
- Any case where a side-by-side output comparison exists.

### Canonical example

Text-to-SQL: show a natural-language query such as "find all
professors who published at least 3 papers in 2024 and their
departments", then show the current-method SQL missing a GROUP BY,
yielding thousands of duplicated rows; then the correct SQL.

## 3. Paradigm B: Existing vs Ours

The figure splits into two side-by-side panels. Left shows how the
existing method works and why it fails; right shows how the paper's
method works and why it succeeds.

### Layout

Two vertical columns. Each column has:

- A schematic of the method's internal structure.
- An annotated failure or success indicator.
- A one-line caption inside the panel naming the method.

### When to use

- The contribution is a structural change to the method's internal
  architecture rather than a failure on a specific input.
- Visualisation is possible at the mechanism level (operator graph,
  data flow, component layout).

### Canonical example

AFlow (ICLR 2025) Figure 2 shows Node, Operator, Edge concepts
side-by-side against traditional workflow representations.

## 4. Paradigm C: Performance Teaser

A carefully designed performance figure placed inside the
Introduction as a preview of results.

### Layout

A compact chart (grouped bar, scatter, or radar) showing the
paper's method clearly dominating baselines. The chart is paired
with a one-sentence text annotation explaining what the reader is
seeing.

### When to use

- The method's performance gain is the headline contribution and
  is large enough to speak for itself.
- Benchmark-style results are available.
- The paper is short (conference style) and needs to hook the
  reader with numbers.

### When to avoid

- Gains are marginal; a teaser shows this weakness unkindly.
- The paper's value is qualitative (ambiguity handling, robustness)
  and does not fit a single metric.

## 5. Design principles

- **Draft on paper first**. Sketch the figure by hand or on a
  whiteboard. Show it to an advisor or collaborator. Iterate the
  sketch before opening any software.
- **Real entities only**. Name real queries, real datasets, real
  outputs. Placeholder names ("Entity1", "X") undermine credibility.
- **30-second test**. Show the figure to someone unfamiliar with the
  paper. If they cannot describe the problem in 30 seconds, the
  figure is not doing its job.
- **Appears once, referenced throughout**. The same example in
  Figure 1 should reappear in the Methodology (as a walkthrough)
  and Experiments (as a case study).

## 6. Tool recommendations

### Primary: PowerPoint

- Fast to iterate on layout.
- Export as PDF preserves vector.
- Fonts and alignment are easy to control.
- Icons from free libraries (Iconfont, Flaticon) compose well.

### Secondary: Figma

- Collaborative editing.
- Component-based design, reusable across figures.
- More polished output for camera-ready.

### Code snippets

Generate syntax-highlighted code as a raster screenshot, then
import into PowerPoint or Figma. Most code-highlighting tools
(pygments-based, Carbon) export clean images.
