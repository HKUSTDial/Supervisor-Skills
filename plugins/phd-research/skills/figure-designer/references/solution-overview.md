# Solution Overview (Methodology) figure design

## Table of contents

1. Why the Overview matters
2. Paradigm A: Pipeline
3. Paradigm B: System Architecture
4. Paradigm C: Multi-layer
5. Design principles
6. Tool recommendations

## 1. Why the Overview matters

The Solution Overview figure sits at the top of the Methodology
section (typically Figure 2 or the first figure of Section 3). Its
job is to give a reader who skips prose a complete mental map of
the method: what the inputs are, what the stages are, what the
outputs are, and how components interact.

A reader should be able to consult this figure at any point while
reading the subsequent technical subsections and re-locate where
they are in the method.

## 2. Paradigm A: Pipeline

The most common paradigm. A left-to-right (or top-to-bottom)
sequence of stages: input to stage 1 to stage 2 to output. Each
stage is a named box; sub-modules fit inside the box.

### Layout

- Canvas: wide, two to three times as wide as tall.
- Three to five large stage boxes from left to right.
- Each stage box contains sub-modules as small boxes.
- Arrows between stages indicate data flow; labelled arrows
  indicate specific data types.
- Inputs on the far left; outputs on the far right.

### When to use

- The method is a multi-stage data transformation.
- Each stage is independent of the others and can be understood
  separately.
- Text-to-SQL methods, data cleaning pipelines, agent workflows.

### Canonical example

AFlow (ICLR 2025) Figure 3: three columns (Search Space; Search
via AFLOW; Search Result) with clear left-to-right flow.

## 3. Paradigm B: System Architecture

Used when the method is a system with interacting components rather
than a linear pipeline. A large outer box represents the system
boundary; internal boxes represent components; arrows show data
flow and control flow within the system.

### Layout

- Canvas: square or slightly wider than tall.
- Outer rectangle labelled with the system name.
- Four to eight internal component boxes, arranged by
  responsibility (front-end, back-end, data store, orchestrator).
- Arrows indicate message passing or data flow.
- Colour-code by component category (data, compute, interface).

### When to use

- The paper presents a system with multiple interacting agents,
  modules, or services.
- Components run concurrently rather than sequentially.
- Feedback loops matter (the output of one component feeds back to
  another).

### Canonical example

Alpha-SQL (ICML 2025) Figure 3: shows the MCTS framework including
the LLM-as-action-model, the search tree expansion process, and
the self-supervised reward feedback loop.

## 4. Paradigm C: Multi-layer

Used when the method has hierarchical structure or multiple phases
that differ fundamentally (offline versus online, training versus
inference, macro versus micro).

### Layout

- Canvas: vertically divided into two or three horizontal layers.
- Each layer represents one phase or abstraction level.
- Arrows between layers show how outputs of one layer feed into
  another.
- Layers are labelled (for example, "Offline" and "Online", or
  "Training" and "Inference").

### When to use

- The method separates preprocessing from runtime execution.
- Different components run at different frequencies.
- The method has a training phase and an inference phase with
  different behaviours.

### Canonical example

LEAD (VLDB 2026) Figure 3: upper row shows Offline setup; lower
row shows Online selection integrated with training. Cross-layer
arrows show data flow.

## 5. Design principles

- **Modular**: each component is a named box. Users can trace a
  component into its corresponding subsection.
- **Clear data flow**: arrows are explicit and do not cross where
  crossing can be avoided.
- **Hierarchy visible**: colour, size, or position distinguishes
  levels (primary components larger; auxiliary components smaller
  or grey).
- **Names match prose**: every component's name in the figure
  appears verbatim in a methodology subsection title. If the figure
  says "Hotspot Detector", the paper says "Section 3.2 Hotspot
  Detector".
- **Inputs and outputs explicit**: the figure shows the overall
  input and output of the method at its boundary.

## 6. Tool recommendations

### Primary: draw.io (also called diagrams.net) or PowerPoint

- Grid snapping keeps alignment clean.
- Shape libraries cover typical architecture components.
- Exports to PDF as vector.

### Secondary: Figma or TikZ

- Figma for polish and team collaboration.
- TikZ for LaTeX-integrated styling consistency; higher initial
  investment but yields the cleanest look.

### Avoid

- Freehand drawing tools (Procreate, GoodNotes) for anything beyond
  early sketches. The output lacks alignment and looks unprofessional
  in a paper.
- Generic diagram auto-generators; they do not understand paper-
  figure conventions.
