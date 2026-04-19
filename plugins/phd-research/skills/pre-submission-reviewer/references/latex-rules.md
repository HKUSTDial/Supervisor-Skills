# LaTeX format rules

## Table of contents

1. File organisation
2. Macro definitions
3. Citations
4. Labels and references
5. Figures and tables
6. Equations
7. Quotation marks and dashes
8. Revision conventions

## 1. File organisation

A multi-section paper should split content into files under a
`sections/` directory, with `main.tex` using `\input{sections/...}`.
Typical structure:

```
sections/
figs/
exps/
algs/
main.tex
commands.tex
bibfile.bib
```

A monolithic `main.tex` with everything inline is acceptable for
very short papers but harder to version-control across multiple
authors.

## 2. Macro definitions

Define macros for recurring strings: system names, method names,
commonly misspelled words, or frequently used highlighting.

Example in `commands.tex`:

```latex
\newcommand{\sys}{\texttt{Alpha-SQL}\xspace}
\newcommand{\hi}[1]{\vspace{.25em}\noindent \textbf{#1}}
\newcommand{\lgl}[1]{\textcolor{blue}{LGL: #1}}
\newcommand{\revision}[1]{\textcolor{blue}{#1}}
```

Renaming becomes a one-line change rather than a find-and-replace
across dozens of sections. When a system name changes mid-
revision, the macro is the only edit required.

## 3. Citations

Rule L1: always use the non-breaking tilde between a word and its
citation, to prevent awkward line breaks.

| Bad | Good |
|---|---|
| `ResNet\cite{X}` | `ResNet~\cite{X}` |
| `ResNet \cite{X}` | `ResNet~\cite{X}` |

Multiple citations go inside one command:

```latex
Artificial Intelligence~\cite{xxxx, yyyy, zzzz}
```

Rule L2: follow the venue's citation style. ACL uses natbib with
`\citep` for parenthetical and `\citet` for textual. Data
management venues (SIGMOD, VLDB) use IEEE or ACM numeric styles.
Convert before submission.

Rule L3: bib entries must include conference name, year, pages,
authors, title. Pull from DBLP for correctness.

## 4. Labels and references

Rule L4: labels use underscores and a prefix for readability.

- `\label{fig:system_overview}` (good).
- `\label{sec:intro}` (good).
- `\label{system overview}` (bad; contains a space).
- `\label{system-overview}` (bad; hyphens break some references).

Rule L5: references also use the non-breaking tilde.

```latex
as shown in Figure~\ref{fig:system_overview}
discussed in Section~\ref{sec:intro}
```

## 5. Figures and tables

Rule L6: every figure and table must have a caption. Captions
describe the finding, not just the setup, especially for
experimental figures.

Rule L7: default placement is top of page (`[t!]`). If the figure
does not fit at the top, `[b!]` (bottom) is acceptable. Inline
`[h]` placement rarely works; let LaTeX decide.

Rule L8: figures use vector formats (PDF, EPS, SVG). Never insert
PNG or JPG screenshots in the final paper; pixelation appears on
zoom.

Rule L9: always reference the figure or table in prose before it
appears. "Figure 2 shows..." is the canonical pattern.

## 6. Equations

Rule L10: every numbered equation should be referenced in the
prose at least once. If an equation is not referenced, either
reference it or remove the numbering with `\begin{equation*}`.

Rule L11: equation numbering should be contiguous within a
section. Use `\label` on each numbered equation to allow
rearranging without renumbering manually.

## 7. Quotation marks and dashes

Rule L12: use the LaTeX convention for quotation marks.

- Double quotes: use `` `` `` for open, `` '' `` for close.
- Single quotes: use `` ` `` for open, `` ' `` for close.
- Never use the straight ASCII typewriter `"` character.

Rule L13: dashes have three types in LaTeX; use each correctly.

- Hyphen `-`: compound adjectives (high-efficiency, zero-shot).
- En-dash `--`: number ranges (pages 10--15, 2024--2026).
- Em-dash `---`: semantic break. Project rule: do not use em-
  dashes in the body. Use commas, colons, or periods instead.

## 8. Revision conventions

For revision submissions, preserve the review history in
dedicated files.

```
responses/
  meta.tex
  r1.tex
  r2.tex
  r3.tex
```

Mark revised text with `\revision{...}` (defined as a blue color
macro). Mark revision pointers in the margins with `\marginpar`:

```latex
\marginpar[]{\revision{R1.W1}}{\revision{text}}
\marginpar[\revision{R3.W2}]{}{\revision{text}}
```

Each `r<n>.tex` file opens with a summary table of the reviewer's
comments and the sections that respond to them. Make the summary
table the first content in the response file so reviewers can see
at a glance what was done.
