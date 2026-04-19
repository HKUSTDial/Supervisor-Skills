# Experimental Results figure design

## Table of contents

1. Chart-type decision matrix
2. Self-containment rule
3. Scientific encoding rule
4. Highlight Ours rule
5. Honest axes rule
6. Canvas sizing and style consistency
7. Tool recommendations

## 1. Chart-type decision matrix

| Chart type | When to use | Design notes |
|---|---|---|
| Grouped bar | Multi-method comparison on multi-benchmark results | Ours in a bold dark colour; baselines in neutral grey; value labels on top of bars |
| Line | Parameter sensitivity, training curves, trends over time or scale | Distinct colour + line style + marker combination per method (for example solid-circle, dashed-square, dotted-triangle); works in black and white |
| Heatmap | Correlation matrices, attention visualisation, method-per-benchmark matrices | Continuous colour scale such as Viridis or Blue-White-Red; label each cell with the numeric value |
| Scatter | Efficiency versus effectiveness trade-off | X axis efficiency metric, Y axis effectiveness metric; annotate each point with the method name; Ours in upper-right if the trade-off favours the paper |
| Box plot | Distribution of results across multiple runs | More honest than reporting only the mean; shows variance |
| Radar | Multi-dimensional capability comparison | Useful when comparing methods across several capability axes simultaneously |

If none of these match the story, step back and ask whether the
experiment is well-designed; a story that fits no chart type often
has no clear conclusion.

## 2. Self-containment rule

Every experimental figure must be readable without the paper
surrounding it. This means:

- Every axis has a label with units.
- Legend names every series that appears.
- Caption's first sentence states the figure's main finding, not
  just the setup. Example: "Figure 5: Performance comparison on
  BIRD benchmark. Our method consistently outperforms all baselines
  across model sizes."
- Abbreviations used inside the figure are defined either in the
  caption or inline.

## 3. Scientific encoding rule

Avoid chartjunk. Do not use:

- 3D bar charts.
- Background gradients.
- Cross-hatch patterns for decoration.
- Multiple overlapping legend keys.
- Distorted aspect ratios that exaggerate small differences.

Use dual encoding. Every series is distinguished by at least two
visual channels (colour and shape, or colour and line style). A
reader who prints the paper in black and white should still be
able to tell curves apart.

## 4. Highlight Ours rule

If Ours dominates the baselines, distinguish it visually:

- Dark or saturated colour versus neutral grey for baselines.
- Bold outline or marker size larger than baselines.
- Always appear in a consistent position (for example rightmost
  column in bar charts, top of the legend).

If Ours does not dominate (for example if the paper is a benchmark
or evaluation paper where the point is that no method dominates),
do not artificially highlight one method; let the reader see the
parity.

## 5. Honest axes rule

- Y axis minimum should be chosen honestly. If all methods score
  between 60 and 80 percent accuracy, starting at 0 makes
  differences invisible; starting at 59 exaggerates them.
  Reasonable start: 55 or 50 percent, with an axis break
  explicitly shown if necessary.
- Never truncate the top of the Y axis without indication.
- Log scales are appropriate when dynamic range spans multiple
  orders of magnitude; always label the scale as log.
- Error bars or confidence intervals should appear when multiple
  runs exist; report the methodology in the caption.

## 6. Canvas sizing and style consistency

### Canvas sizing

Matplotlib defaults are designed for standalone viewing, not for
LaTeX papers. Use a small canvas (roughly 150x100 points) so that
fonts and lines scale up to readable size when inserted into a
column.

### Style consistency

Create a `plot_utils.py` script early in the project. Define:

- A palette (for example a 6-colour ColorBrewer qualitative scheme
  with Ours = index 0).
- Line widths (for example 1.5pt for data, 0.8pt for grid).
- Font sizes (for example 9pt title, 8pt tick labels).
- Figure dimensions per figure type.

Every experimental figure imports from this script. The result is
visual consistency across the paper, which reviewers register
subconsciously as professionalism.

## 7. Tool recommendations

### Primary: Matplotlib or Seaborn

- Code-generated; fully reproducible; version-controllable.
- Can be scripted from experiment outputs without manual editing.
- Scales to many figures with consistent styling.

### Secondary: TikZ or PGFPlots

- LaTeX-integrated; matches paper typography exactly.
- Higher initial cost but cleanest visual integration.
- Preferred by journals that expect LaTeX-native figures.

### Avoid

- Excel charts inserted as images. Quality is poor; styling is
  inconsistent; impossible to regenerate from updated data.
- Hand-edited plots (open the Matplotlib output in Illustrator and
  edit). One-off success, zero reproducibility; the next reviewer
  round will require regeneration from scratch.
