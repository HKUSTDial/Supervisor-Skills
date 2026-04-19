# Pre-Submission Reviewer

## Why this matters

The three-to-five-day window before a submission deadline is where
careful external review pays off the most. By then the paper's structure
is locked, the experiments are complete, and there is time for one last
audit but not for a rewrite. Running a structured review in this window
catches the problems that sink otherwise-strong papers: a broken
Introduction flowchart, topic sentences missing from most paragraphs,
citations without non-breaking tildes, figures that pixelate, and banned
AI-tone vocabulary that marks the paper as AI-drafted.

The Pre-Submission Reviewer skill takes a full paper or key sections and
produces a structured review across five dimensions (macro logic,
writing details, English grammar, LaTeX formatting, figure quality),
each with severity-tagged findings and concrete rewrite suggestions. It
enforces the mechanical rules from the writing-detail checklist
(no em-dashes, no banned AI-tone vocabulary, leading-text discipline,
topic-sentence discipline, citation-format uniformity) and surfaces the
patterns that non-native English authors most commonly violate.

The output is not a rewrite. It is a prioritised list of findings that
the author decides which to fix, with CRITICAL items blocking
submission. The author retains editorial control; the skill flags
issues and suggests fixes but does not rewrite prose.

## The framework

### The five-dimension audit

The review examines the paper from five angles in sequence. Each
dimension has its own checklist and produces independent findings.

**Dimension 1: Macro logic.** Is the Introduction's six-paragraph
flowchart intact? Do Contributions map one-to-one to Methodology modules
and Section numbers? Do the Experiments validate the paper's main
claims rather than tangential ones? Is the Related Work complete? Does
the running example stay consistent from Introduction through
Experiments? Every break in the chain is CRITICAL.

**Dimension 2: Writing details.** Does every paragraph have a topic
sentence ("leading text")? Do paragraphs transition smoothly? Are any
paragraphs over ten lines and needing a split? Does the Abstract cover
problem, method, and result? Orphan paragraphs (no connection to
neighbours) and missing topic sentences are MAJOR issues. A reviewer
reading a topic-sentence-less paragraph has to reconstruct the
paragraph's purpose from context, which is expensive cognitive work.

**Dimension 3: English grammar.** The usual non-native-author pitfalls:
article use (a, an, the), subject-verb agreement (especially third-
person singular), tense consistency (Related Work past, method present,
experiments past), passive-voice overuse, which-versus-that confusion,
and Chinglish patterns. Long sentences should be split at "Specifically,".

**Dimension 4: LaTeX formatting.** Equation numbering contiguous and
every numbered equation referenced. Figures and tables have detailed
captions. Citations use the correct command plus the non-breaking tilde
(for example, `ResNet~\cite{X}` rather than `ResNet \cite{X}`). Labels
use underscores, not spaces or hyphens (`\label{fig:system_overview}`
rather than `\label{system overview}`). Figures use vector format.
Page-limit compliance.

**Dimension 5: Figure quality.** Vector format. Font size large enough
post-scaling. Colour-blind-safe palette with dual encoding. Self-
contained caption with a finding in the first sentence. No chartjunk
(3D effects, excessive grids, busy backgrounds). The Motivated Example
is concrete and failure-revealing. The Solution Overview uses labels
that match section titles.

### Severity taxonomy

Every finding is tagged:

- **CRITICAL**: blocks submission. Examples: Contributions do not map to
  Sections; Introduction flowchart broken; running example absent;
  raster figure in final draft; missing key baseline; page-limit
  violation.
- **MAJOR**: reviewers will flag in first round. Examples: topic
  sentence absent from three or more paragraphs; em-dash in five or more
  places; banned AI-tone word in three or more places; Table 1
  comparison missing; chart type mismatched with data.
- **MINOR**: polish. Examples: two long sentences that could be split;
  default Matplotlib styling; a single article error.

CRITICAL items should block submission until addressed. MAJOR items
should be fixed if time allows. MINOR items are author's call. The
taxonomy is reviewer-style: findings that would cause a reject-worthy
comment in round one are CRITICAL or MAJOR; findings that a reviewer
would mention as minor polish are MINOR.

### Banned-vocabulary and em-dash scan

A dedicated scan covers the mechanical writing rules that distinguish
professional academic prose from AI-generated drafts. This is a hard-
rule check; the author cannot negotiate around a banned word just
because they like it.

**Em-dashes used as sentence connectors are banned** by project
convention (see [CONTRIBUTING.md](/CONTRIBUTING.md)). The replacement is commas,
colons, or a period break. An em-dash in five or more places in a paper
is MAJOR.

**Banned AI-tone vocabulary**, compiled from reviewer experience,
includes:

- Innovation descriptors: innovative, pioneering, revolutionary
  paradigm, transformative framework.
- Performance comparisons: superior, surpass, excel, remarkable,
  unprecedented, achieves SOTA, breakthrough performance.
- Contribution summaries: general-purpose, is capable of.
- Logical connectives: notably, yet, yielding, at its essence.
- Verbs: encompass, differentiate, reveal, underscore, surpass, show
  great potential, exhibit superior capability, exceed, pave the way
  for, highlight the potential of.
- Phrases: profound challenges (not a natural English collocation),
  stems from.
- Adjectives: rigid.
- Verbs: impede.

Each banned word or phrase occurrence is flagged with a line reference.
Three or more occurrences of any banned word triggers a MAJOR severity;
under three is MINOR. A paper that accumulates several MAJOR banned-
vocabulary flags often reads as AI-drafted even if the author wrote the
content themselves; removing the vocabulary restores the paper's
human voice.

### Section-by-section review

Each section has its own canonical structure, and the audit checks the
submitted section against its guide:

- **Abstract**: five-sentence formula (problem, why, challenges, how,
  results). Concrete datasets and numbers in the last sentence.
- **Introduction**: six paragraphs (see
  [intro-drafter](../intro-drafter/overview.md)). Every claim has a
  deliverable.
- **Problem Formulation**: text description, formal definition,
  illustrative example, in that order.
- **Framework or Method**: architecture first, workflow next, component
  details last. Every module must be novel or at least necessary.
- **Experiments**: past tense. At least three datasets. Overall
  comparison first, then ablations, then scalability or sensitivity.
  Every claim grounded in data.
- **Related Work**: summarise categories first, then contrast with the
  current paper. Directly related work gets its limitations named;
  indirectly related work gets respect. Never copy prose.
- **Conclusion**: present-perfect tense. Summarise contributions without
  repeating the Introduction.

## Key checks

- **Macro logic intact**: Introduction six paragraphs present and
  connected; contributions map to sections.
- **Running example consistent** across Introduction, Methodology,
  Experiments.
- **Topic sentence per paragraph**; no paragraph over ten lines.
- **English correctness**: articles, tense, subject-verb agreement,
  which-versus-that, passive voice.
- **LaTeX compliance**: non-breaking tildes in citations, underscored
  labels, vector figures, citation format matched to venue.
- **Figure quality universal rules** (vector, font size, dual encoding,
  self-contained caption, no chartjunk, honest axis).
- **No em-dashes as connectors.**
- **No banned AI-tone vocabulary** in three or more places.
- **Section structures match canonical guides**: Abstract five
  sentences, Introduction six paragraphs, Experiments past tense with at
  least three datasets.

## Worked example

Consider a hypothetical Text-to-SQL paper submitted to VLDB. The audit
identifies:

- **Dimension 1 (Macro logic)**: the Introduction has Background,
  Limitations, and Solution Overview, but no Challenges paragraph. At
  VLDB this is CRITICAL; the author must insert a Challenges paragraph
  before submission.
- **Dimension 2 (Writing details)**: paragraphs 2, 4, and 5 lack topic
  sentences. MAJOR; the author should add a one-sentence lead to each.
- **Dimension 3 (Grammar)**: mixed tense in the Experiments section
  (present and past alternating). MAJOR; unify to past tense.
- **Dimension 4 (LaTeX)**: citations in Section 3 miss the non-breaking
  tilde in 14 places. MAJOR; run a find-and-replace. Labels
  "fig:solution-overview" use a hyphen. MINOR; change to underscore.
- **Dimension 5 (Figures)**: Figure 5 is a raster PNG, which would
  pixelate in print. CRITICAL; regenerate as PDF. Figure 1 uses red and
  green only, with no dual encoding. MAJOR; add cross and check icons.
- **Banned-vocabulary scan**: "surpass" appears 6 times, "revolutionary"
  once, "achieves SOTA" 3 times. "Surpass" and "achieves SOTA" are
  MAJOR; "revolutionary" is MINOR.
- **Em-dashes**: 7 occurrences as sentence connectors. MAJOR; convert to
  commas or period-break.

Final score: 6 of 10. Submission recommendation: Needs one to two days
more work. The author fixes CRITICAL items first (insert Challenges
paragraph, regenerate Figure 5 as PDF), then MAJOR items (topic
sentences, tense unification, citation tildes, Figure 1 dual encoding,
banned-vocabulary removal, em-dash cleanup). MINOR items can be
addressed if time allows.

## Try it with the plugin

Install the plugin per the
[root README](../../../../README.md#quick-install) and invoke naturally.
The skill self-triggers on phrases like "review this paper", "audit
before submission", "check the draft", "find issues", "proofread", or
within a week of a submission deadline. Provide the paper's text
(pasted, or the LaTeX source, or a PDF extract) and the skill returns
the five-dimension review plus the final score and submission
recommendation.

For workflow: run this skill three to five days before the deadline,
fix CRITICAL items and MAJOR items where time allows, then consider
running the skill one more time after fixes to confirm no regressions.
Orthogonal companion skills are
[figure-designer](../figure-designer/overview.md) for figure-specific
audit detail and [vibe-research-workflow](../vibe-research-workflow/overview.md)
for AI-assisted polish discipline.

## Source

Adapted from:

- [archive/v1-source/1_Guide/03_Paper_Writing/3.5_写作细节与Checklist.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.5_写作细节与Checklist.md)
- Plugin SKILL.md:
  [/plugins/phd-research/skills/pre-submission-reviewer/SKILL.md](/plugins/phd-research/skills/pre-submission-reviewer/SKILL.md)

---

[English] | [中文](../../../zh/skills/pre-submission-reviewer/overview.md)
