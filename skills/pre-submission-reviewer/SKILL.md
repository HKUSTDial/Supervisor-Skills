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
license: CC-BY-NC-SA-4.0
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

## Core procedure

### Step 0: paradigm and venue fit

Before the dimensional review, settle two things.

**Paradigm**, judged by research method, because what counts as a
severe problem differs by paradigm:

- **STEM / technical** (CS, engineering, materials, chemistry): weight
  the Introduction chain, contribution-to-section mapping, baseline
  coverage, ablation-based attribution, figure quality. Benchmark
  papers additionally get coverage, reproducibility, and
  contamination checks; chemistry and materials get characterization
  completeness, purity, controls, replicates.
- **Humanities** (literature, history, philosophy, discourse
  analysis): weight whether the thesis is explicit and defensible,
  core concepts pinned down and stable across sections, the
  literature genuinely engaged, and the material (texts, archives,
  cases) able to carry the claims. Do **not** demand baselines or
  ablations here; check instead whether sub-arguments build on each
  other rather than sit in parallel, and whether conclusions outrun
  the material.
- **Empirical social science**: weight operationalized research
  questions, sampling and data-source justification, statistics
  matched to data types, conclusions bounded by the sample. For
  theory papers, "experiments" reads as "proofs": check the proofs,
  and never call the evidence thin merely because there is no results
  table.
- **Finance / economics**: weight identification credibility,
  endogeneity handling, robustness checks (their absence is a
  first-round flag), and economic versus merely statistical
  significance.
- **Law**: weight the accuracy of statutes, case numbers, and
  holdings (an invented or wrong citation is rejection-level), the
  clarity of the interpretive approach, and whether comparative
  arguments state their scope.

When the paradigm is unclear, ask the author before reviewing with
the wrong ruler.

**Venue fit**: if the stated target venue's scope visibly mismatches
the paper's topic or contribution type, that is a real rejection
risk, not a taste note. Flag it as a finding and suggest two or three
better-fitting venues.

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
- The headline result's attribution is isolated: an ablation
  separates the core mechanism from peripheral factors (a routing
  step, post-processing, a stronger base model, favorable samples).
  No such ablation: flag "attribution unverified" as MAJOR.
- Claims match their evidence: "solves" is stronger than most papers
  earn (usually "improves"); "state-of-the-art" needs the benchmark
  and conditions; "we are the first" gets checked or flagged.

Every break in the chain is CRITICAL.

**Retrieval-grounded checks** (when the environment has a
literature-search capability: a scholarly tool, web search over
scholarly indexes, or shell access to public APIs):

1. **Novelty verification**: extract two or three keyword groups from
   the paper's core method and problem setting, retrieve, and identify
   the three to five closest published works. If Related Work already
   covers them, the paper's positioning stands; a highly relevant
   uncovered work is a MAJOR finding ("missed X, Author et al.,
   Year"). Compare on difference axes; a similar title alone proves
   nothing.
2. **Citation completeness**: retrieve the field's recent
   representative works and its canonical ones, and compare against
   the reference list; a missing canonical baseline, founding paper,
   or recent survey is MAJOR.

Retrieval results support metadata-level judgments only; never quote
numbers or method details from search snippets. Without any retrieval
capability, skip these two checks and say so in the summary.

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

Severity honesty cuts both ways. A review that lists a dozen MINOR
items while missing the one rejection-level flaw sends the author to
submission with false confidence; a review that inflates taste issues
into CRITICAL destroys trust. The overall recommendation must match
the findings: any unresolved CRITICAL forbids "ready to submit", and
a near-ready verdict requires zero CRITICAL and at most two MAJOR.

## Integrity gate

Each bullet is tagged [inspection] (LLM verifies from the paper
text) or [attestation] (LLM runs the procedure and states it has
done so; user remains responsible for confirming completeness).

Before emitting the review:

1. **[inspection]** Every finding quotes specific text (sentence,
   phrase, figure name); no "the Introduction is unclear" without
   a quoted line.
2. **[inspection]** Every CRITICAL finding has a concrete fix
   suggestion, not "rewrite entirely".
3. **[inspection]** No fabricated quotes: only text actually
   present in the submitted material.
4. **[inspection]** Severity assignments follow the taxonomy;
   nothing is marked CRITICAL for taste reasons.
5. **[inspection]** Dimension 3 (grammar) findings cite the
   specific grammar rule from `references/grammar-rules.md`.
6. **[attestation]** Dimension 6 banned-vocabulary scan is run in
   full on the entire paper, not sampled. The skill attests the
   full scan; if the paper is extremely long, the skill states it
   chunked the input and describes the chunking strategy.
7. **[inspection]** Final score matches the CRITICAL + MAJOR
   count; a score of 9 or 10 requires zero CRITICAL and at most
   two MAJOR items.

If any [inspection] check fails, mark the output as "needs user
attention". For [attestation] bullets, the skill states the scope
of its scan and the user confirms completeness.

Run the gate silently. Do not print a per-gate pass or fail report;
a failure surfaces as a concrete finding in the affected dimension,
and the delivered review stays free of internal checking rituals.

## Output format

### Summary
- CRITICAL: <n>
- MAJOR: <m>
- MINOR: <k>
- Top three fixes first: ...

### Dimension 1: Macro logic
| # | Finding | Severity | Suggested fix |
|---|---|---|---|
| 1 | <quoted text> | CRITICAL or MAJOR or MINOR | <fix> |

### Dimension 2: Writing details
<same table shape>

### Dimension 3: English grammar
<same table shape, citing grammar-rule ID>

### Dimension 4: LaTeX format
<same table shape>

### Dimension 5: Figure quality
<same table shape>

### Banned-vocabulary and em-dash scan
<list with line references>

### Final score (1-10)
<score>

### Submission recommendation
- <Ready to submit | Needs 1-2 days more work | Needs major revision before submission>
