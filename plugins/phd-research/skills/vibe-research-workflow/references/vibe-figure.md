# Vibe Figure: four-step workflow

## Table of contents

1. Why Vibe Figure works
2. Step 1: Discuss with AI
3. Step 2: Select and prompt
4. Step 3: Generate first sketch
5. Step 4: Vectorise by hand
6. What AI cannot do
7. Integration with figure-designer

## 1. Why Vibe Figure works

Figures combine conceptual design (what to show) with craft (how
to render it cleanly). AI helps most on conceptual brainstorming
and first-draft layouts; craft still belongs to the user plus
their vector-graphics tool of choice.

The four-step workflow separates the AI-accelerated phases from
the hand-polished phases.

## 2. Step 1: Discuss with AI

Before drawing anything, describe the figure's purpose to the AI
and ask for design alternatives.

Prompt template:

```
I'm designing Figure 1 for a paper on <topic>.
The figure should communicate <the single message>.
The figure appears in <section, position>.
Target venue: <name>, two-column format.

Please propose three layout alternatives. For each, describe:
- Panel structure
- Colour use
- Key annotations
- Tradeoffs compared with the other alternatives
```

AI returns three alternatives; the user discusses with an advisor
or collaborator; the best alternative is chosen.

## 3. Step 2: Select and prompt

Given the selected alternative, refine the prompt with specific
details.

Prompt refinement:

- Specific entity names (real queries, real datasets, not
  placeholders).
- Concrete failure or success indicators (exact wrong output
  versus correct output).
- Colour specifics (Ours in a specific ColorBrewer index;
  baselines in grey).
- Annotations with concrete text.
- Canvas dimensions targeting the paper's column width.

Avoid:

- Vague requests ("make it look professional").
- Asking for things the tool cannot produce (AI sketch tools
  cannot produce Matplotlib-quality scientific charts).
- Letting AI invent data; data comes from the user's experiments.

## 4. Step 3: Generate first sketch

Tool choice by figure type:

- Motivated Example (Figure 1): Gemini with Nano Banana or a
  similar tool can produce first sketches of conceptual figures.
  The output is a visual reference, not a paper-ready figure.
- Solution Overview: draw.io, Excalidraw, or hand-sketching on
  paper, then photographed and iterated.
- Experimental Results: Matplotlib prototypes run by the user
  from experiment output; AI scaffolds the `plot_utils.py`
  helper.

The first sketch is diagnostic, not final. It answers "does the
design work visually?" Not "is this ready for the paper?"

## 5. Step 4: Vectorise by hand

Take the first sketch and produce the final paper-ready figure
by hand in a vector tool:

- Motivated Example and Solution Overview: PowerPoint (draft) or
  Figma (polish). Do not trust AI sketches as final; they lack
  typographic discipline.
- Experimental Results: Matplotlib or Seaborn scripted from the
  actual experiment outputs. The script lives in the repository
  and regenerates on data updates.

Quality control (see `figure-designer`'s `design-rules.md`):

- Vector format export.
- Font size at least 8pt post-scaling.
- Colour-blind-safe palette, dual encoding.
- Self-contained caption.
- No chartjunk.

## 6. What AI cannot do

AI-generated figures in their current state cannot:

- Produce paper-quality scientific charts with correct
  statistical conventions.
- Generate vector output that is editable at the object level.
- Maintain visual consistency across a paper's figure set.
- Guarantee correct annotation of data points or entities.
- Handle typography at the level expected for academic figures.

Plan for AI-assistance in ideation and drafting, not in final
production. Every final figure is the user's work.

## 7. Integration with figure-designer

This skill orchestrates the workflow; `figure-designer` handles
the individual figure design decision.

Typical sequence:

1. `vibe-research-workflow` (this skill, figure-mode): plan the
   figure-production session.
2. `figure-designer`: for each figure, decide paradigm, layout,
   labelling, tool, and run the audit.
3. Execute the four-step flow above for each figure.
4. Integrate back into the paper.
