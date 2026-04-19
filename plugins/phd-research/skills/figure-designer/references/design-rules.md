# Universal figure design rules

## Table of contents

1. Format rules
2. Typography rules
3. Colour rules
4. Caption rules
5. Axis rules
6. Decoration rules

## 1. Format rules

- **Vector format only**. Export figures as PDF, EPS, or SVG.
  Never insert PNG or JPG into a LaTeX paper; they pixelate when
  the reader zooms in. Raster is the "amateur" tell reviewers
  notice first.
- **PDF is the default**. It travels well across LaTeX distros and
  journals.
- **Avoid embedded bitmap inside vector**. A PDF generated from
  matplotlib with `format='pdf'` is preferable to a PDF that
  wraps a screenshot.
- **Compatibility**. If the target conference requires EPS, export
  in EPS directly; do not convert PDF to EPS via intermediate
  raster.

## 2. Typography rules

- **Font size at least 8pt post-scaling**. The figure will be
  scaled down when inserted into a two-column paper; design with
  the final inserted size in mind.
- **Canvas small, fonts proportional**. In Matplotlib, set the
  figure to approximately 150 by 100 points rather than a large
  canvas with small fonts. Big canvases with tiny fonts are a
  common mistake.
- **Match paper font family**. If the paper uses Times-like serif
  text, avoid sans-serif figure labels.
- **Bold sparingly**. Bold the series or data point the figure is
  arguing for; do not bold every label.

## 3. Colour rules

- **Colour-blind safe**. Roughly 8 percent of men and 0.5 percent
  of women have colour-vision deficiencies. Use palettes designed
  for colour-blind readers. ColorBrewer qualitative palettes are
  a safe default.
- **Dual encoding**. Do not rely on colour alone to distinguish
  series. Colour plus line style or colour plus marker shape
  ensures the figure works in black and white.
- **Limit palette size**. Above six distinct colours, humans lose
  track. If the figure compares seven methods, group into two
  tiers (Ours in a highlight colour, others in neutral grey).
- **Contrast for the key item**. If Ours dominates, use a bold
  contrasting colour against grey baselines. If Ours does not
  dominate, do not artificially highlight it.

## 4. Caption rules

- **Self-contained**. A reader looking only at the figure and its
  caption should understand what the figure shows and what it
  claims.
- **First sentence states the finding**, not just the setup.
  Example to avoid: "Figure 5: Results on BIRD." Example to use:
  "Figure 5: Our method consistently outperforms all baselines on
  BIRD across model sizes, with the largest gains on complex
  multi-table queries."
- **Define abbreviations** used inside the figure, in the caption
  or in a figure legend.
- **Reasonable length**. Two to five sentences. Extremely long
  captions indicate the figure is trying to do too much.

## 5. Axis rules

- **Label all axes**. Axis name and unit.
- **Honest Y axis minimum**. Do not start at zero if differences
  are in the top quintile; do not start just below the lowest
  value if differences are small.
- **Log scales labelled**. If a log scale is used, mark it.
- **Ticks at meaningful intervals**. Do not use Matplotlib default
  ticks if they produce cluttered or uninformative intervals.
- **Error bars when possible**. If the experiment was run multiple
  times, show the variance. Error bars build trust.

## 6. Decoration rules

- **No 3D**. Never use 3D bar charts, 3D pie charts, or 3D scatter
  unless the data is genuinely three-dimensional.
- **No drop shadows** on bars or points.
- **No gradient fills** unless the gradient encodes a continuous
  variable.
- **Minimal grid**. Subtle grey grid lines, not dark heavy lines.
- **No cross-hatching** for decoration; use it only if colour
  alternatives are inadequate.
- **No chart title when the caption serves the same role**. In
  academic figures, the caption is the title.

Every violation adds noise and reduces credibility. Reviewers may
not articulate the reason for their discomfort, but chartjunk
signals amateurism.
