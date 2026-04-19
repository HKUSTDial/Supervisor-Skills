# Figure Designer

## Why this matters

In top-venue papers (SIGMOD, VLDB, ICML, NeurIPS), figure quality directly
shapes a reviewer's first impression. Three figures in particular carry
almost all the storytelling weight: the Motivated Example (Figure 1, on
page 1 or the top of page 2), the Solution Overview (inside the
Methodology section), and the Experimental Results figures (inside the
Experiments section). Reviewers scan these three in under a minute to
decide whether the paper is worth reading in detail; weak figures sink
otherwise-strong papers.

Designing a single good figure often takes one or two days, which is a
normal and appropriate investment. A student who rushes a figure in an
hour typically produces a raster screenshot with tiny fonts, no dual
encoding, and a caption like "Figure 5: results comparison". Reviewers
notice, and the paper's craft-signal drops sharply. A student who treats
figure design as a load-bearing part of the paper, worthy of hours of
careful work, produces figures that make reviewers want to continue
reading.

The Figure Designer skill takes the user's storytelling intent plus
context (research area, method name, target venue) and returns the right
design paradigm, a layout sketch, labelling guidance, tool suggestion,
and a quality-control audit against a universal rule set. It also
supports an audit mode where the user paste an existing figure and the
skill reviews it against the rules.

## The framework

### Universal rules

Five rules apply to every figure, regardless of type.

| Rule | Why it matters |
|---|---|
| Vector format for export | PDF, EPS, or SVG. Raster figures (PNG, JPG) pixelate under scaling and immediately mark the paper as amateur |
| Font size at least 8pt after scaling | Matplotlib defaults produce huge canvases with tiny fonts; shrink the canvas (e.g. 150x100pt) so fonts scale up to legible size |
| Colour-blind-safe palette with dual encoding | About 8% of men have colour vision deficiencies; also, papers are often printed in black and white. Never rely on colour alone; pair colour with line style or marker shape |
| Self-contained caption | First sentence states the core finding, not the figure type. "Figure 5: our method consistently outperforms all baselines on BIRD" is stronger than "Figure 5: performance comparison" |
| Honest axis ranges | Do not start the Y-axis at 59% to dramatise a 5-point gap; 55% or 50% with clear labelling is honest and still shows the difference |

Violating any of these rules is a reviewer-grade red flag. The skill
audits against each one before approving a design. A paper with
multiple universal-rule violations rarely recovers in review; the
reviewer's first impression is already set, and the content has to
work twice as hard to overcome it.

### Paradigm 1: Motivated Example Figure

The Motivated Example (Figure 1) is the single most important figure in
the paper. Its job is to convey, in 30 seconds of reading, what problem
the paper solves and why existing methods fall short. It lives on page 1
or the top of page 2, immediately after the Introduction's Limitations
paragraph.

Three canonical paradigms:

- **Running Example + Failure Case (most recommended).** Give a concrete,
  real scenario and show how an existing method fails on it. Example for
  Text-to-SQL: a specific natural-language query ("find all professors
  who published at least three papers in 2024 and their departments"),
  the current method's SQL output with a missing GROUP BY highlighted in
  red, and the correct SQL in green. The failure is visceral: reviewers
  see the pain.
- **Existing vs Ours comparison.** Two-column or two-row layout: left
  shows how existing methods work and their limitation, right shows the
  new method and its advantage. The direct visual contrast lets the
  reader spot the difference instantly.
- **Performance Teaser.** A Figure 1 that is itself a carefully designed
  performance chart, showing the new method's gain over baselines at a
  glance. Only appropriate when the method's performance is dramatic
  enough to justify leading with the result.

Tool: PowerPoint or Figma. Motivated examples typically mix text, icons,
arrows, and code fragments, which are awkward in Matplotlib and painful
in TikZ. PowerPoint is fastest; Figma produces cleaner polish. Icons can
come from iconfont.cn or similar.

### Paradigm 2: Solution Overview Figure

The Solution Overview is the Methodology section's "soul". It lives at
the start of Section 3 or 4 and lets a reviewer who skipped straight to
the figures understand the system's architecture and data flow. A
reviewer reading later sections should be able to return to this figure
to orient.

![AFlow solution overview figure, three-layer architecture with data, agent, and coordination planes](/assets/images/aflow_solution_overview.png)

Figure: AFlow's Solution Overview (ICLR 2025). The three-panel pipeline
(Search Space, Search via AFlow, Search Result) demonstrates the
canonical Pipeline paradigm.

Three canonical paradigms:

- **Pipeline (most common).** Stages flow left to right or top to bottom:
  input, stage 1, stage 2, ..., output. Each stage is a labelled box with
  submodules inside. AFlow's Figure 3 (above) is a textbook example:
  Search Space on the left, Search via AFlow in the middle, Search
  Result on the right.
- **System Architecture.** System boundary as a large box, interacting
  components inside, arrows showing control and data flow. Alpha-SQL's
  Figure 3 uses this pattern, showing LLM-as-Action-Model, MCTS search
  tree expansion, and self-supervised reward feedback as interacting
  components.
- **Multi-layer or Multi-view.** Vertical or horizontal split for layered
  or dual-phase architectures. LEAD's Figure 3 splits offline from online
  phases vertically, with the online phase's output feeding back into
  the training loop.

Design principles: modularity (each core component is a labelled box, no
unlabelled regions), data-flow clarity (arrows never cross unless
unavoidable), hierarchy (colour, size, and position convey level), text-
figure alignment (module names match section titles), and input-output
explicitness (a first-time reader should immediately see the method's
input and output).

Tool: draw.io or PowerPoint for the draft, Figma or TikZ for polish.

### Paradigm 3: Experimental Results Figure

Experimental Results figures support specific empirical claims. Choose
the chart type by data shape, not by prettiness.

| Chart type | Best for | Design notes |
|---|---|---|
| Grouped Bar Chart | Multi-method, multi-dataset overall performance comparison | Highlight your method with a saturated colour; baselines in light grey |
| Line Chart | Sensitivity analysis, training curves, trends over a continuous variable | Use line style plus marker shape plus colour (triple encoding) so black-and-white printing still works |
| Heatmap | Correlation matrices, attention weights, per-method per-case performance | Continuous colour scale (blue-white-red, Viridis); annotate every cell |
| Scatter Plot | Efficiency-effectiveness trade-off | X-axis efficiency, Y-axis effectiveness; your method should land top-right |
| Box Plot | Distribution of results across runs | More honest than a mean; shows variance |
| Radar Chart | Multi-dimensional method comparison | Useful when comparing 3-5 methods across 5-6 axes |

Design rules specific to experimental figures: self-contained (caption's
first sentence states the finding), avoid chartjunk (no 3D, no
unnecessary shadows, no busy backgrounds), highlight Ours (saturated
colour for your method, grey or pastel for baselines), and honest axis
ranges.

Tool: Matplotlib plus Seaborn, in a reusable plotting script like
`plot_utils.py` that centralises palette, font, and line-width defaults.
Pandas or Excel for the data pipeline. Avoid hand-drawn charts;
experimental figures must be reproducible from code. Centralising
defaults also ensures visual consistency across the paper's figures,
which is a significant Nice Presentation gain.

### Tool matrix

| Figure type | First choice | Alternative | Why |
|---|---|---|---|
| Motivated Example | PowerPoint, Figma, OmniGraffle | draw.io | Mixed text, icons, arrows, code snippets; needs flexible layout |
| Solution Overview | draw.io, PowerPoint | Figma, TikZ | Flowchart and architecture diagrams; needs clean module boxes and arrows |
| Experimental Results | Matplotlib + Seaborn | TikZ, PGFPlots | Must be code-generated for reproducibility |
| Mathematical diagram | TikZ | Matplotlib | Native LaTeX integration preferred |

## Named heuristics

- **Vector format mandatory**: PDF, EPS, or SVG. Raster figures lose
  points immediately.
- **Small canvas, big fonts**: shrink canvas (150x100pt) so fonts scale
  up, rather than the default large canvas with tiny fonts.
- **Dual encoding for accessibility**: colour plus line style plus marker
  shape.
- **Self-contained caption, finding first**: the caption's first sentence
  states what the figure proves.
- **Running example throughout**: Figure 1's motivated example reappears
  in methodology and experiments.
- **Highlight Ours**: saturated colour for the new method, grey or pastel
  for baselines.
- **Honest Y-axis**: do not start at 59% to dramatise a 5-point gap.
- **Pipeline, Architecture, Multi-layer** are the three Solution Overview
  paradigms; pick by the method's structure.
- **Running Example + Failure Case, Existing vs Ours, Performance
  Teaser** are the three Motivated Example paradigms; pick by the story.

## Worked example

Consider Alpha-SQL's Figure 1 (the Motivated Example) as designed through
the skill.

- **Type identification**: Motivated Example.
- **Paradigm**: Running Example + Failure Case. Alpha-SQL's claim is that
  zero-shot LLMs fail on complex Text-to-SQL without structured search; a
  concrete failure case makes this claim visceral.
- **Layout sketch**: three-panel vertical arrangement. Top panel: the
  natural-language query ("List all professors who..."). Middle panel:
  the current method's SQL output with missing JOIN highlighted in red,
  plus the wrong query results. Bottom panel: Alpha-SQL's SQL output
  with the correct JOIN highlighted in green, plus the correct results.
- **Labels**: real entity names (actual database table and column names),
  not placeholders. Real query, real output.
- **Colour palette**: ColorBrewer qualitative for the three panels; red
  for the failure highlight, green for the success highlight.
- **Tool**: PowerPoint for draft, export to PDF.
- **Universal rule audit**: vector (pass, after PDF export), font (pass
  if set to 10pt), colour-blind-safe (caution, the red-green pair is the
  worst case for colour blindness; pair each colour with an icon such as
  a cross and a check for dual encoding).

The audit catches the red-green problem. The fix is dual encoding: red
box with an explicit "wrong" label or cross icon, green box with a
"correct" label or check icon. The figure now reads correctly in black-
and-white printing and for colour-blind readers.

## Try it with the plugin

Install the plugin per the
[root README](../../../../README.md#quick-install) and invoke naturally.
The skill self-triggers on phrases like "design a figure", "draw Figure
1", "plot experiment results", "choose the right chart type", "which
figure tool to use", or "figure looks unprofessional". Provide the
intent (what the figure should communicate), context (research area,
method name, target venue), and if possible an image of a draft; the
skill returns a paradigm recommendation, a layout sketch, labelling
guidance, a tool suggestion, and an audit against the universal rules.

For figure audits specifically, the skill supports both a vision path
(paste an image or provide a path to a PNG, PDF, or SVG) and a text
path (describe the figure in prose). The vision path checks font
legibility, palette, and chartjunk directly; the text path marks those
rules as "user must verify".

## Source

Adapted from:

- [archive/v1-source/1_Guide/04_Scientific_Plotting/4.1_Motivated_Example_Figure.md](/archive/v1-source/1_Guide/04_Scientific_Plotting/4.1_Motivated_Example_Figure.md)
- [archive/v1-source/1_Guide/04_Scientific_Plotting/4.2_Solution_Overview_Figure.md](/archive/v1-source/1_Guide/04_Scientific_Plotting/4.2_Solution_Overview_Figure.md)
- [archive/v1-source/1_Guide/04_Scientific_Plotting/4.3_Experimental_Results_Figure.md](/archive/v1-source/1_Guide/04_Scientific_Plotting/4.3_Experimental_Results_Figure.md)
- [archive/v1-source/1_Guide/04_Scientific_Plotting/4.4_绘图Checklist与工具速查表.md](/archive/v1-source/1_Guide/04_Scientific_Plotting/4.4_绘图Checklist与工具速查表.md)
- Plugin SKILL.md:
  [/plugins/phd-research/skills/figure-designer/SKILL.md](/plugins/phd-research/skills/figure-designer/SKILL.md)
- Plugin references:
  [/plugins/phd-research/skills/figure-designer/references/motivated-example.md](/plugins/phd-research/skills/figure-designer/references/motivated-example.md),
  [/plugins/phd-research/skills/figure-designer/references/solution-overview.md](/plugins/phd-research/skills/figure-designer/references/solution-overview.md),
  [/plugins/phd-research/skills/figure-designer/references/experimental-results.md](/plugins/phd-research/skills/figure-designer/references/experimental-results.md)

---

[English] | [中文](../../../zh/skills/figure-designer/overview.md)
