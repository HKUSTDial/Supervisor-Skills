# Forbidden patterns

## Table of contents

1. Em-dash misuse
2. Banned AI-tone vocabulary
3. Chartjunk patterns
4. Overclaim patterns
5. Plagiarism red lines
6. Detection heuristics

## 1. Em-dash misuse

Em-dashes used as sentence connectors are banned in this
project's writing conventions. Two common misuse patterns:

### Misuse A: connecting two independent clauses

- Bad: "... closes the research loop, from literature analysis to
  deployment."
- Good (using comma plus subordinate clause): "... closes the
  research loop, covering literature analysis, hypothesis
  generation, simulation, validation, and deployment."

### Misuse B: inserting a parenthetical

- Bad: "This approach, though simple, is highly effective."
- Good (using a subordinate clause): "Although simple, this
  approach is highly effective."

Acceptable em-dash uses are rare in academic writing. When in
doubt, do not use them. Commas, colons, or periods handle nearly
every case.

Detection: grep for the Unicode em-dash character. Every
occurrence in the body is a MAJOR finding unless explicitly in a
code sample or preserved quotation.

## 2. Banned AI-tone vocabulary

The following vocabulary signals AI-authored or AI-assisted prose
to experienced reviewers and should be avoided. Seeing three or
more uses in a paper is a MAJOR finding.

### Innovation hyperbole

innovative, pioneering, revolutionary paradigm, transformative
framework

### Performance hyperbole

superior, surpass, excel, remarkable, unprecedented, achieves
SOTA, breakthrough performance

### Contribution-summary markers

general-purpose, is capable of

### Logical connective markers

notably, yet, yielding, at its essence

### Overused verbs

encompass, differentiate, reveal, underscore, surpass, exhibit
superior capability, exceed, pave the way for, highlight the
potential of

### Overused phrases

profound challenges (this collocation does not exist in standard
writing), stems from

### Overused adjectives and verbs

rigid, impede

Replace with neutral technical verbs from the section-guides
reference: propose, introduce, design, present, show, demonstrate,
report, observe.

## 3. Chartjunk patterns

Chart elements that add visual noise without information:

- 3D bar charts, 3D pie charts.
- Drop shadows on bars or points.
- Gradient fills except where a gradient encodes a continuous
  variable.
- Heavy grid lines.
- Cross-hatching for decoration.
- Chart titles duplicating the caption.
- Legend keys with more than six entries (try grouping instead).

Each chartjunk instance is a MINOR or MAJOR finding depending on
severity.

## 4. Overclaim patterns

Overclaims common in draft papers:

- "Our method is state-of-the-art" without qualification. State
  state-of-the-art on which benchmark, under which conditions.
- "Comprehensive experiments" as a contribution. Experiments are
  expected; what was specifically shown?
- "Extensive analysis". Name what the analysis found, not that
  analysis exists.
- "We solve the problem of X". Solving is a strong claim; usually
  the paper improves on X rather than solves.
- "We are the first to". Verify carefully; if the claim is wrong,
  reviewers will find and quote it.

Each overclaim is a MAJOR finding. Reviewers keep a running
grudge against papers that overclaim in the Introduction; the
cost compounds over the review cycle.

## 5. Plagiarism red lines

Never copy sentences from other papers, including the author's
own prior papers without explicit reuse acknowledgement. This
applies to:

- Related Work summaries of prior methods.
- Introduction references to prior work.
- Method descriptions that resemble baseline papers' own
  descriptions.

Plagiarism detection is a CRITICAL finding that blocks submission.
When the paper's Related Work or Introduction paraphrases prior
work too closely, rewrite in the author's own words.

## 6. Detection heuristics

For the banned-vocabulary scan:

- Case-insensitive substring search for each banned term.
- Count occurrences per term.
- Three or more occurrences of any single banned term is MAJOR.
- Single occurrence is MINOR.

For em-dash scan:

- Search for the Unicode em-dash character.
- Every occurrence is a finding.
- Severity is MAJOR if in body; MINOR if in preserved quotations.

For chartjunk scan:

- Cannot be done automatically; the skill relies on the user's
  figure description or on an uploaded figure.

For overclaim scan:

- Look for unconditional superlatives: "is state-of-the-art", "is
  superior", "beats all".
- Flag each occurrence with a request to qualify or substantiate.

For plagiarism:

- Random sentence-level search of the Related Work and
  Introduction against public texts is not feasible inside the
  skill. Recommend an external plagiarism checker for final
  submission.
