---
name: figure-designer
description: >-
  Advises on the design of the three core figures in a technical paper:
  the Motivated Example (Figure 1), the Solution Overview
  (Methodology), and the Experimental Results figures. Recommends the
  right design paradigm, layout, labelling, and tool for each figure
  type, then runs a quality-control audit. Use when the user asks to
  'design a figure', 'draw Figure 1', 'plot experiment results',
  'choose the right chart type', 'which figure tool to use', or
  'figure looks unprofessional'.
license: CC-BY-4.0
---

# Figure Designer

## Overview

A top-venue paper typically carries six to eight figures, with three
carrying almost all the storytelling weight: the Motivated Example
(Figure 1, on page 1 or the top of page 2), the Solution Overview
(inside the Methodology section), and the Experimental Results
figures (inside the Experiments section). Reviewers scan these three
in under a minute to decide whether the paper is worth reading in
detail; weak figures sink otherwise-strong papers.

This skill takes the user's intent (what they want to communicate)
plus context (research area, method name, target venue) and returns
the recommended paradigm, a layout sketch, labelling guidance,
tool suggestion, and a quality-control audit against a universal
rule set (vector format, font size, colour-blind-safe encoding,
self-contained caption, honest axis ranges).

## When to use this skill

- Before drawing any figure in a paper.
- The user asks to 'design a figure', 'draw Figure 1', 'plot
  experiment results', 'choose the right chart type'.
- The user has drawn a figure and wants a design audit.
- The user is unsure which figure type or paradigm to choose.
- Preparing camera-ready figures before submission.

## When NOT to use this skill

- The user only wants generic plotting help (bar chart, line chart)
  outside a paper. Regular assistance suffices.
- The paper is not yet structured; use `intro-drafter` or
  `tech-paper-template` first to decide what figures the paper
  needs.
- The user wants a review of an already-finished paper. Use
  `pre-submission-reviewer`.

## Core procedure

### Step 1: Figure-type identification

Decide which of the three core types the figure is. If the user's
request does not match any, either it is a supporting figure (use
the experimental-results guidance as a base) or it does not belong
in the paper.

If the mode is `figure-audit` and the user has provided an image
path, load the image with the Read tool **before** proceeding to
Step 2. Vision-based inspection enables the universal rule audit
in Step 6 to check font legibility, colour palette, raster-vs-
vector tells, and chartjunk directly rather than relying on user
description. If no image is provided, continue in text-only mode
and mark vision-only rules (font size, raster detection, colour
palette) as "user must verify" in the final audit report.

### Step 2: Paradigm recommendation

See: references/motivated-example.md, references/solution-overview.md,
or references/experimental-results.md depending on figure type.

Each figure type has two to three canonical paradigms. Pick the one
that fits the user's storytelling need, and explain why the other
paradigms fit less well.

### Step 3: Layout sketch

Produce a text description of the layout: panel positions, element
placement, arrows, colour assignments. The goal is that the user
could draw the first draft from the sketch alone.

### Step 4: Labelling and annotation guidance

- Name every visible element concretely (no "Module A", "X", "Y").
- Annotate critical points (failure highlight, success highlight,
  comparison emphasis).
- Specify font sizes and colour palette. Default colour palette:
  ColorBrewer Qualitative or Viridis for sequential.

### Step 5: Tool suggestion

See: references/tools.md for the tool matrix and the decision
heuristic.

Default recommendations:

- Motivated Example and Solution Overview: PowerPoint (draft),
  Figma (polish).
- Experimental Results: Matplotlib or Seaborn in a reusable
  `plot_utils.py` script.
- LaTeX-integrated figures: TikZ or PGFPlots.

### Step 6: Universal rule audit

See: references/design-rules.md for the full universal rule set.

Verify every proposed or existing figure against:

- Vector format (PDF, EPS, SVG) for export.
- Font size at least 8pt post-scaling.
- Small canvas (not large canvas with small fonts).
- Colour-blind-safe palette; no colour-only encoding.
- Self-contained caption whose first sentence states the core
  finding.
- Honest axis ranges.
- No 3D effects, no chartjunk.

Flag every violation with severity.

### Step 7: Integrity gate

Run the checks in the Integrity gate section below.

### Step 8: Output

Emit the full design in the Output format below.

## 1. Figure type
- Type: <motivated-example or solution-overview or experimental-results>
- Reason: <one sentence>

## 2. Paradigm recommendation
- Paradigm: <name>
- Why this paradigm: <rationale>
- Alternatives considered and rejected: <list>

## 3. Layout sketch
- Canvas: <size>
- Panels: <list with positions and contents>
- Arrows and connections: <list>
- Colour assignment: <mapping>

## 4. Labelling and annotations
- Element names: <list>
- Critical highlights: <list>
- Font sizes: <target>
- Colour palette: <name>

## 5. Tool suggestion
- Primary: <tool>
- Alternative: <tool>
- Reason: <rationale>

## 6. Universal rule audit
- [ ] Vector format: <pass or fail>
- [ ] Font size: <pass or fail>
- [ ] Colour-blind safe: <pass or fail>
- [ ] Self-contained caption: <pass or fail>
- [ ] Honest axis range (if applicable): <pass or fail>
- [ ] No chartjunk: <pass or fail>

## 7. Integrity gate result
- Gate 1-7: <pass or fail>

## 8. Severity summary
- <n> CRITICAL, <m> MAJOR, <k> MINOR
- Top three actions first: ...
```
