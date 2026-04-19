# Per-section writing guides

## Table of contents

1. Abstract
2. Introduction
3. Problem Formulation
4. Framework or Methodology
5. Experiments
6. Related Work
7. Conclusion

## 1. Abstract

Five-sentence formula.

| Sentence | Content |
|---|---|
| 1 | What problem does the paper solve? Context plus significance |
| 2 | Why is it worth solving? Nobody has done it, or existing methods fail |
| 3 | What are the challenges? Must be concrete; challenges of the problem, not of the method |
| 4 | How is the problem solved? Method name and the key components, matched to the challenges |
| 5 | How well does the method perform? Real datasets, concrete numbers, code link if available |

Common failures:

- Too abstract on what and why.
- Missing challenges sentence.
- Results sentence without specific numbers.
- Hype words (revolutionary, groundbreaking) in the first
  sentence; these read as defensive.

## 2. Introduction

Six-paragraph formula matching the Introduction Flowchart.

| Paragraph | Content |
|---|---|
| 1 | The problem; a concrete motivating example |
| 2 | Existing approaches and their limitations; highly condensed, at most three limitations |
| 3 | The problem's essence and hard constraints; the paper's goal or key idea |
| 4 | Key challenges; the challenges of the problem, not the method |
| 5 | Solution overview; one-to-one mapping with challenges |
| 6 | Summary of contributions, three or four, each mapped to a section |

Key constraints:

- Attracts the reviewer. Mostly decides acceptance.
- Highlights novelty and technical depth.
- States the difference from existing work explicitly.
- Writes the paper's own ideas; other work belongs in Related
  Work.
- Terms are precise; the reader should grasp the paper's core
  quickly.

## 3. Problem Formulation

Three steps:

1. Describe the problem in prose so the reader understands the
   scope.
2. Present the formal definition with notation and equations.
3. Use a concrete example to anchor understanding.

Key constraint: a paper should solve one problem, not several.
A strong running example is worth more than additional formal
machinery.

## 4. Framework or Methodology

Organising principle: overall-to-detail. The section starts with
an architecture and then drills into components; each component's
subsection repeats the pattern.

| Part | Content |
|---|---|
| Architecture overview | Overall picture; after reading this part, the reader understands the technique at a high level |
| Workflow walkthrough | Traces inputs through the system end-to-end |
| Simple components | Described in-line in the Framework section |
| Complex components | Covered at high level here; full detail deferred to a dedicated subsection or section |

Must-have:

- Novelty and contribution explicitly stated.
- Overall architecture figure.
- If a component has no novelty, minimise coverage; long
  descriptions of known techniques add noise.
- Later subsections order by novelty: strongest first.
- Self-contained; well-illustrated; leading text per subsection.

Avoid:

- Explaining why alternative methods were rejected in detail;
  that belongs in Related Work or an ablation.
- Prior-work notation fragments mixed with the paper's notation.
- Symbol drift across subsections; define once and use
  consistently.

## 5. Experiments

Tense: past.

Setup requirements:

- Experimental goals stated first.
- At least three datasets.
- Evaluation metrics named and justified.
- Baselines selected carefully; obvious baselines must not be
  omitted. If the paper cites work proving A beats B and C, only A
  is required, with explanation.

Overall comparison:

- End-to-end comparison against all baselines first.
- State the metric before analysing results.
- State the gain, explain the reason, extract findings.

Ablation study:

- Evaluate the contribution of each proposed component.
- For three components A, B, C: report All, -A, -B, -C.
- Vary key hyperparameters.

Must-have:

- Real datasets and persuasive baselines.
- Conclusions stated explicitly. What did the experiments
  demonstrate? Why?

## 6. Related Work

Position:

- Section 2 if the paper depends on prior frameworks, models, or
  methods for understanding.
- Penultimate section if the paper is self-contained. The
  penultimate position is the preferred default for strong papers.

Do:

- Summarise in the author's own words. No copying of sentences.
- Fair crediting; do not over-criticise.
- Focus on high-level summary, not minor details.
- Self-contained; explain how the paper differs from related
  work.
- Group by method category, then state differences. Criticise
  closest-related work directly; less-related work gets less
  critique and more acknowledgement.
- Citations use conference abbreviations (SIGMOD, VLDB, ICDE,
  TKDE). Pull bibtex from DBLP.

Do not:

- Copy sentences from related work, ever. Plagiarism is a red
  line.

## 7. Conclusion

Tense: present perfect (we have shown, we have proposed).

Purpose: summarise contributions and significance. Do not duplicate
the Introduction.

- Introduction addresses readers who have not yet read the paper.
- Conclusion addresses readers who have finished the paper; they
  know the technical details.

Close with implications or future directions in one to two
sentences. Avoid vague claims about "impact".
