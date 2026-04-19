---
name: pre-submission-reviewer
description: >-
  Runs a pre-submission review of a technical paper across five
  dimensions: macro logic, writing details, English grammar, LaTeX
  formatting, and figure quality. Uses a reviewer-style severity
  taxonomy (CRITICAL / MAJOR / MINOR) and flags banned AI-tone
  vocabulary and em-dash misuse. Use when the user asks to 'review
  this paper', 'audit before submission', 'check the draft', 'find
  issues', 'proofread', or within one week of a submission
  deadline.
license: CC-BY-4.0
---

# Pre-Submission Reviewer

## Overview

Three to five days before a submission deadline is the window where
a careful external review pays off most. This skill takes a full
paper or key sections and produces a structured review across five
dimensions, each with severity-tagged findings and concrete
rewrite suggestions. It enforces the mechanical rules from the
writing-checklist section (no em-dashes, no banned AI-tone
vocabulary, leading text per paragraph, topic-sentence discipline,
citation-format uniformity) and surfaces the patterns that
non-native English-speaking authors most commonly violate
(articles, subject-verb agreement, tense consistency, which versus
that, Chinglish phrasing).

The output is not a rewrite. It is a prioritised list of findings
with severity tags; the author decides which to fix. CRITICAL items
should block submission until addressed.

## When to use this skill

- Three to five days before a submission deadline.
- The user asks to 'review this paper', 'audit before submission',
  'check the draft', 'find issues', 'proofread'.
- After a camera-ready revision, before sending the final version.
- After any major rewrite (rebuttal responses, Section 3 overhaul).
- When the user suspects AI-tone contamination in a section.

## When NOT to use this skill

- The paper is still being structured. Use `tech-paper-template`,
  `intro-drafter`, or `benchmark-paper-template` (separate plugin) first.
- The user wants structural advice rather than review. Use the
  drafting skills instead.
- The user needs a rebuttal. Use `rebuttal-drafter`.

## Core procedure

### Step 1: Dimension 1 Macro logic review

See: references/logic-and-structure.md for the Logic First rule,
Self-contained rule, Leading Text rule, and Running Example rule.

Check:

- Introduction flowchart is intact (Background, Limitations, Goal
  or Key Idea, Challenges, Methodology, Contributions).
- Contributions map one-to-one with methodology modules and with
  section numbers.
- Experiments validate the paper's main claims, not tangential
  ones.
- Related Work covers the necessary prior art.
- Running example is consistent across Introduction, Methodology,
  Experiments.

Every break in the chain is CRITICAL.

### Step 2: Dimension 2 Writing details review

See: references/logic-and-structure.md for paragraph-level rules.

Check:

- Every paragraph has a topic sentence.
- Paragraphs transition smoothly; no orphan paragraphs.
- Paragraphs are not over 10 lines; split if so.
- No repeated or redundant passages.
- Abstract covers problem, method, result.

### Step 3: Dimension 3 English grammar review

See: references/grammar-rules.md for the canonical list of errors
common to non-native English authors, with corrections and
examples.

Check the usual suspects:

- Article use (a, an, the).
- Subject-verb agreement (third-person singular).
- Tense consistency (Related Work past, method present).
- Passive-voice overuse.
- Which versus that.
- Sentence length; split long sentences at "Specifically,".
- Chinglish patterns.

### Step 4: Dimension 4 LaTeX format review

See: references/latex-rules.md for the canonical list of LaTeX-
specific issues.

Check:

- Equation numbering contiguous; every numbered equation
  referenced.
- Figures and tables have captions; captions are detailed.
- Citations use the correct command and the non-breaking tilde
  (for example, `ResNet~\cite{X}`, never `ResNet\cite{X}`).
- Labels use underscores, not spaces or hyphens.
- Vector figure format; no raster.
- Page-limit compliance.

### Step 5: Dimension 5 Figure quality review

See: references/forbidden-patterns.md for chartjunk patterns and
the full figure-quality checklist.

For each figure:

- Vector format.
- Font size large enough post-scaling.
- Colour-blind-safe palette; dual encoding.
- Self-contained caption with a finding in the first sentence.
- No chartjunk.
- Motivated example is concrete and failure-revealing.
- Solution overview has labels matching section titles.

### Step 6: Banned-vocabulary and em-dash scan

See: references/forbidden-patterns.md for the banned-word list.

Scan the full paper for:

- Em-dashes used as sentence connectors (banned; project rule).
- AI-tone words: innovative, pioneering, revolutionary paradigm,
  transformative framework, superior, surpass, excel, remarkable,
  unprecedented, breakthrough performance, general-purpose, is
  capable of, notably, yet, yielding, at its essence, encompass,
  differentiate, reveal, underscore, pave the way for, highlight
  the potential of, profound challenges, stems from, rigid,
  impede.

Flag each occurrence with a severity tag. Em-dashes are MAJOR by
default; banned AI-tone words are MAJOR if they appear three or
more times.

### Step 7: Section-by-section review

See: references/section-guides.md for the per-section writing
guides for Abstract, Introduction, Problem Formulation, Framework
or Method, Experiments, Related Work, and Conclusion.

For each section, check that the section's content matches the
guide's canonical structure (for example, Abstract's five-sentence
formula: what, why, challenges, how, results).

### Step 8: Integrity gate

Run the checks in the Integrity gate section below.

### Step 9: Output

Emit the review in the Output format below.

## Severity taxonomy

- **CRITICAL**: blocks submission. Example: contributions do not
  map to sections; introduction flowchart broken; no real-world
  running example; raster figure in final draft; missing key
  baseline; page-limit violation.
- **MAJOR**: reviewers will flag in first round. Example:
  topic-sentence absent from 3+ paragraphs; em-dash in 5+ places;
  banned AI-tone word in 3+ places; Table 1 comparison missing;
  chart type mismatched with data.
- **MINOR**: polish. Example: two long sentences that could be
  split; default Matplotlib styling; single article error.

## Summary
- CRITICAL: <n>
- MAJOR: <m>
- MINOR: <k>
- Top three fixes first: ...

## Dimension 1: Macro logic
| # | Finding | Severity | Suggested fix |
|---|---|---|---|
| 1 | <quoted text> | CRITICAL or MAJOR or MINOR | <fix> |

## Dimension 2: Writing details
<same table shape>

## Dimension 3: English grammar
<same table shape, citing grammar-rule ID>

## Dimension 4: LaTeX format
<same table shape>

## Dimension 5: Figure quality
<same table shape>

## Banned-vocabulary and em-dash scan
<list with line references>

## Integrity gate result
- Gate 1 through 7: <pass or fail>

## Final score (1-10)
<score>

## Submission recommendation
- <Ready to submit | Needs 1-2 days more work | Needs major revision before submission>
```
