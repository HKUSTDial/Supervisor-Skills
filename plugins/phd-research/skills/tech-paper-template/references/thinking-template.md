# Thinking template: cell-by-cell content contract

## Table of contents

1. How to read this reference
2. Cell: Research background
3. Cell: Limitations 1, 2, 3
4. Cell: Key Idea or Our Goal
5. Cell: Challenges 1, 2, 3
6. Cell: Methodology topic sentence and modules
7. Cell: Contributions
8. Methodology-outline derivation

## 1. How to read this reference

Each cell in the thinking template has a content contract: what
belongs in the cell, what a strong filling looks like, what a weak
filling looks like, and how to detect trouble.

The template is a thinking tool, not a drafting tool. Each cell
should be fillable in one to four sentences. If a cell fights to
expand beyond that, either the paper has too much ambition for one
paper or the writer does not yet have clarity on that cell.

## 2. Cell: Research background

### Content contract

One paragraph equivalent. Names the research scenario, explains why
it matters in the real world, cites 3 to 5 recent representative
works in the subfield.

### Strong filling

- Specific scenario (not "AI is important").
- Real-world stakes named (a user, a deployed system, a decision
  that changes).
- Two or three canonical recent works cited by name.
- Roughly 60 to 100 words.

### Weak filling

- Generic motivation.
- "Deep learning has revolutionised ..." as the opening line.
- No named prior works.

### Detection rule

If the filling does not name at least one specific prior work or
one concrete real-world stakes element, the cell is weak.

## 3. Cell: Limitations 1, 2, 3

### Content contract

At most three limitations. Each limitation is a specific gap in
prior work, framed as "prior work X does not handle Y".

### Strong filling

- Each limitation names a specific capability.
- Each limitation corresponds to a challenge or design decision
  later in the template.
- Two limitations is acceptable; do not pad.

### Weak filling

- "Existing work is insufficient".
- Four or more limitations.
- Limitations with no connection to any challenge.

### Detection rule

If any limitation does not map to a challenge, either the
limitation is noise or the challenge is missing. Resolve before
proceeding.

## 4. Cell: Key Idea or Our Goal

### Content contract

One sentence. For Technique: the core mechanism (Key Idea). For
New Problem/Setting: the goal or problem formulation.

### Strong filling

- A sentence a reviewer could quote.
- Specific enough that the reader could re-derive the method
  sketch.
- Free of marketing language ("revolutionary", "breakthrough").

### Weak filling

- Vague phrases ("we propose a new method").
- Multiple sentences trying to compress the whole paper.
- Restating the research question without an answer.

### Detection rule

If the cell spans more than two sentences, the writer has not yet
committed to a single framing. Force the choice.

## 5. Cell: Challenges 1, 2, 3

### Content contract

At most three challenges. Each challenge is a specific obstacle
that blocks a naive extension of prior work from solving the
problem.

### Strong filling

- Each challenge is grounded in implementing the Key Idea or
  realising the Goal.
- Each challenge cites the specific mechanism-level difficulty.
- Each challenge maps one-to-one to a methodology module.

### Weak filling

- "The problem is hard".
- Challenges pre-announcing their solutions.
- More than three challenges; the scope is too wide.

### Detection rule

If the challenge is stated without explanation of why a naive
approach fails, the challenge is probably invented to justify a
module. Re-derive from the Key Idea.

## 6. Cell: Methodology topic sentence and modules

### Content contract

One topic sentence naming the framework or system plus one
sub-cell per methodology module. Each module addresses one
challenge.

### Strong filling

- Topic sentence names the framework and hints at the overall
  mechanism in under 25 words.
- Each module is named and has a one-sentence summary.
- One-to-one correspondence with challenges.

### Weak filling

- Topic sentence is a cliche ("we propose a novel framework").
- Modules without names ("a module").
- Module count exceeds challenge count without explanation.

### Detection rule

If the module count and challenge count do not match, one side is
wrong. Fix before proceeding.

## 7. Cell: Contributions

### Content contract

3 or 4 numbered contributions. Each maps to a section.

### Strong filling

- Each contribution is specific and citable.
- Each contribution is mapped to a section or set of sections.
- Contributions cover the main mechanism, the main result, and
  either the problem framing (New Problem) or the system design
  (Technique).

### Weak filling

- "Extensive experiments".
- "Comprehensive analysis".
- Four-plus contributions.
- Contributions without section mapping.

### Detection rule

Run the contribution-patterns audit from the `intro-drafter` skill's
`references/contribution-patterns.md` (cited cross-skill in prose,
not as a reference pointer).

## 8. Methodology-outline derivation

Once the template is filled, derive a methodology-section outline
by:

1. Using the methodology topic sentence as Section 3's opening.
2. Making each module a numbered subsection.
3. For each subsection, copying the module summary as the opening
   sentence and listing three to five sub-points to expand.

This skeleton is what the author uses to draft the methodology
section; it is handed off to the writer after this skill completes.
