# The six-paragraph Introduction flowchart

## Table of contents

1. Chain of reasoning
2. Paragraph 1: Background and Motivation
3. Paragraph 2: Limitations of existing work
4. Paragraph 3: Problem essence and Our Goal
5. Paragraph 4: Key challenges
6. Paragraph 5: Solution overview
7. Paragraph 6: Contributions
8. Pitfalls at each stage

## 1. Chain of reasoning

```
Background + Running Example
   -> Limitations (at most 3)
      -> Problem Essence + Our Goal
         -> Key Challenges (at most 3)
            -> Solution Overview (one module per challenge)
               -> Contributions (3 to 4, each mapped to a section)
```

Every arrow must hold. If any arrow breaks, the Introduction reads as
a list of disjointed claims rather than a single argument. Reviewers
notice this and score down.

## 2. Paragraph 1: Background and Motivation

### Purpose

Introduce the research object, motivate why the problem matters in
the real world, and ground the rest of the paper in a concrete
running example.

### Writing points

- Open with the task, not the technique. The reader should care
  about the problem before hearing about the solution.
- Include a specific running example, ideally with an accompanying
  figure (Figure 1). The example should be self-contained and show
  the problem's complexity in under 30 seconds of reading.
- Cite three to five recent real applications or deployments as
  evidence of importance.
- One paragraph, approximately 150-200 words.

### Common failures

- Opening with a technique ("we introduce X for Y").
- Generic motivation ("deep learning is important").
- No running example; the paper never becomes tangible.

## 3. Paragraph 2: Limitations of existing work

### Purpose

Identify what prior work does not address, in at most three
limitations.

### Writing points

- Each limitation is framed as "prior work X does not handle Y".
- Each limitation is specific enough that a reader can name the
  capability that is missing.
- Limitations motivate the challenges in Paragraph 4. There should
  be a visible link: each challenge addresses a limitation.
- Two limitations is acceptable; do not pad to three artificially.
- One paragraph, approximately 150-200 words.

### Common failures

- Vague limitations ("existing work is insufficient").
- Too many limitations; after three, the paper loses focus.
- Limitations that have nothing to do with the challenges in
  Paragraph 4; the reader cannot see why they were raised.

## 4. Paragraph 3: Problem essence and Our Goal

### Purpose

Characterise the problem's intrinsic properties and hard constraints,
then state the research goal or key idea.

### Writing points

- Hard constraints are explicit: scale, dynamicity, heterogeneity,
  end-to-end latency, correctness, or consistency requirements.
- For a Technique Paper, the Goal is a one-sentence bridge: "Our
  goal is to handle Y with better accuracy." Key Idea carries the
  weight.
- For a New Problem / Setting Paper, the Goal is the paper's core
  contribution: "Our goal is to handle Y under constraint Z, a
  setting that has not been studied." Key Idea supports "why this
  definition is reasonable".
- If a Research Question is better than a Goal, state it as a
  question.
- One paragraph, approximately 100-150 words for Technique papers,
  200-250 words for New Problem papers.

### Common failures

- Skipping hard constraints; Paragraph 4 challenges then have no
  grounding.
- Stating the goal as a list of sub-goals; reviewers lose focus.
- For New Problem papers, underweighting this paragraph as if it
  were a Technique Paper.

## 5. Paragraph 4: Key challenges

### Purpose

Enumerate the two or three obstacles that prevent a naive extension
of prior work from solving the problem.

### Writing points

- Each challenge is one sentence naming the obstacle plus one to
  two sentences explaining why naive methods fail.
- Challenges address the limitations from Paragraph 2 or the hard
  constraints from Paragraph 3.
- Common challenge categories:
  - Search-space explosion.
  - Efficiency or latency ceilings.
  - End-to-end closed-loop difficulty.
  - Theoretical or engineering conflict.
- At most three challenges. Four or more signals scope issues.
- One paragraph, approximately 150-200 words.

### Common failures

- Vague challenge statements ("it is hard").
- Challenges that do not map to modules in Paragraph 5.
- Pre-announcing solutions inside challenge statements.

## 6. Paragraph 5: Solution overview

### Purpose

Present the paper's methodology at a high level, with a one-to-one
mapping between the challenges in Paragraph 4 and the modules or
components introduced here.

### Writing points

- Start with a one-sentence topic sentence naming the solution
  framework.
- For each challenge, name the module that addresses it.
- Explicit one-to-one mapping; if a module addresses two challenges,
  say so.
- Methodology section numbers are forward-referenced in parentheses.
- One paragraph, approximately 150-200 words.

### Common failures

- Over-detail that belongs in Section 3 (Methodology).
- No explicit mapping; reviewers must infer which module handles
  which challenge.
- Module count mismatches challenge count without explanation.

## 7. Paragraph 6: Contributions

### Purpose

Summarise the paper's contributions in three or four numbered bullets,
each mapped to a section or set of sections.

### Writing points

- Canonical structure:
  - C1: Problem definition or problem-setting contribution (if the
    paper is a New Problem / Setting Paper).
  - C2: System or framework design, or a specific methodological
    innovation.
  - C3: One or two key technical contributions (specific algorithms,
    theoretical results, or data structures).
  - C4: Comprehensive experimental evaluation with specific
    highlights (not vague claims).
- Each contribution cites a section: "(Section 3.2)" or "(Sections
  4-5)".
- No single contribution is a vague phrase like "extensive
  experiments".
- One paragraph or a numbered list; approximately 100-150 words.

### Common failures

- Vague phrases as contributions.
- Contributions that the paper does not actually deliver.
- More than four contributions; focus erodes.

## 8. Pitfalls at each stage

- **Stage 1 pitfall**: running example is an abstraction (graph, LLM,
  system); not tangible enough.
- **Stage 2 pitfall**: limitations list is longer than three or
  padded.
- **Stage 3 pitfall**: goal is unclear; reader cannot say in one
  sentence what the paper tries to do.
- **Stage 4 pitfall**: more challenges than modules, or challenges
  invented to justify modules rather than derived from the problem.
- **Stage 5 pitfall**: module names do not appear in Paragraph 6's
  contributions, so the reader loses track.
- **Stage 6 pitfall**: contributions include items the paper does not
  deliver; in major revisions, reviewers quote these.
