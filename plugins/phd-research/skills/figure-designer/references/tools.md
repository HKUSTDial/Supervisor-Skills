# Figure tool matrix

## Table of contents

1. Decision heuristic
2. PowerPoint and Keynote
3. Figma
4. draw.io (diagrams.net)
5. Matplotlib and Seaborn
6. TikZ and PGFPlots
7. Plotly
8. OmniGraffle
9. What to avoid

## 1. Decision heuristic

| Figure type | Primary tool | Alternative | Reason |
|---|---|---|---|
| Motivated Example (Figure 1) | PowerPoint | Figma | Mixed content: text, icons, code, arrows |
| Solution Overview (pipeline, architecture, multi-layer) | draw.io | PowerPoint, TikZ | Need clear modular layout, aligned grids |
| Experimental Results (bar, line, heatmap, scatter, etc.) | Matplotlib + Seaborn | TikZ + PGFPlots | Reproducible, scriptable, versioned |
| Schema or relation diagrams | draw.io | TikZ | Standard database diagram conventions |
| Icons and logos | Figma | Iconfont, Flaticon | Clean vector editing |

Decide the figure type first; each tool shines on a specific type.
Do not try to make one tool do all jobs.

## 2. PowerPoint and Keynote

- Fast iteration on layout.
- Export as PDF preserves vector.
- Font and alignment controls are reasonable.
- Free on most institutional licenses.

Best for early drafts, Figure 1 designs, and any figure with mixed
content (text blocks, icons, arrows, embedded code snippets).

Weakness: not reproducible from data; every edit is manual.

## 3. Figma

- Component-based; build reusable elements across figures.
- Collaboration on a shared canvas.
- Cleanest output for polished camera-ready Figure 1.
- Web-based; no local install required.

Best for polishing a Motivated Example or Solution Overview after
the layout is stable.

Weakness: browser-only; offline editing is limited.

## 4. draw.io (diagrams.net)

- Free, cross-platform, offline-capable.
- Grid snapping keeps pipeline and architecture diagrams aligned.
- Shape libraries cover typical computer-science diagramming needs.
- Export as PDF or SVG.

Best for Solution Overview figures that are pipelines or system
architectures.

Weakness: visual polish is lower than Figma or OmniGraffle.

## 5. Matplotlib and Seaborn

- Code-generated; fully reproducible from data.
- Scriptable; regenerate all experiment figures after each
  experiment re-run.
- Scales to dozens of figures with shared styling.
- Python-native; integrates with experiment scripts.

Best for every experimental results figure.

Weakness: defaults are ugly; always import a shared `plot_utils.py`
for consistent styling.

## 6. TikZ and PGFPlots

- Native LaTeX; exact typography match with paper text.
- Vector-perfect output.
- Highest effort and steepest learning curve.

Best for camera-ready figures in journals that expect TikZ-quality
typography.

Weakness: high cost for early drafts; switch to TikZ only after the
figure design is stable.

## 7. Plotly

- Interactive; good for supplementary material or HTML appendices.
- Export to static PNG or PDF for paper inclusion.

Best for exploratory analysis and supplementary interactive
figures.

Weakness: default typography differs from academic norms; static
export quality is below Matplotlib for paper inclusion.

## 8. OmniGraffle

- Professional diagram quality.
- Native macOS only.
- Paid.

Best for polished Solution Overview figures if the author already
uses macOS and has an OmniGraffle license.

Weakness: macOS-only limits collaboration with Windows or Linux
co-authors.

## 9. What to avoid

- **Excel charts inserted as images**. Poor quality, inconsistent
  styling, difficult to regenerate.
- **Hand-edited Matplotlib output in Illustrator**. One-off
  result; breaks on every data update.
- **Generic online diagram generators** with non-academic
  conventions. The figure will look out of place in a top-venue
  paper.
- **Procreate, GoodNotes, Notability** for anything beyond early
  hand sketches. Freehand drawing lacks alignment discipline.
- **AI image generators** for paper figures. They cannot produce
  the structured content academic figures require.
