---
name: tech-paper-template
description: >-
  Structures a technical paper's full logical skeleton using a
  thinking-template table (research background, limitations, key idea
  or goal, challenges, methodology modules, contributions), positions
  the paper as Technique or New Problem/Setting, and runs a four-point
  self-consistency check. Use when the user is brainstorming a paper,
  discussing progress with an advisor, or planning the paper before
  drafting. Also use for 'paper skeleton', 'paper logic chain',
  'thinking template', 'paper-structure planning'.
license: CC-BY-4.0
---

# Tech Paper Template

## Overview

Before drafting any prose, a technical paper needs a full logical
skeleton: the research background, the specific limitations of prior
work, the key idea or research goal, the technical challenges that
prevent a naive solution, the methodology modules that address each
challenge, and the contributions that the paper will claim. This
skill fills in that skeleton via a standardised thinking-template
table, positions the paper type, and runs four self-consistency
checks on the logic chain.

The output is a filled-in thinking template plus a consistency
report. It is suitable for advisor-student brainstorming sessions,
weekly progress meetings, and the final planning step before writing
begins. It does not draft Introduction prose (use `intro-drafter` for
that); it operates at the logical-skeleton layer.

## When to use this skill

- Early brainstorming of a paper project.
- Weekly progress meeting with an advisor or collaborator.
- Pre-drafting planning after `idea-evaluator` returns Strong Accept.
- The paper's logic chain feels incoherent and needs an audit.
- The user asks for 'paper skeleton', 'paper logic chain', 'thinking
  template', or 'paper-structure planning'.
- The user is unsure whether their paper is Technique or New
  Problem/Setting.

## When NOT to use this skill

- The paper is a benchmark paper. Use `benchmark-paper-template` (separate plugin).
- The user needs an Introduction-specific paragraph outline. Use
  `intro-drafter` (typically run this skill first, then
  `intro-drafter`).
- The user has a written draft and wants review feedback. Use
  `pre-submission-reviewer`.
- The idea itself is not yet vetted. Use `idea-evaluator` first.

## Core procedure

### Step 1: Paper-type positioning

See: references/paper-types.md for the positioning criteria and
worked examples.

Decide Technique versus New Problem/Setting. In Technique, the Key
Idea carries the narrative and Our Goal is a short bridge. In New
Problem/Setting, Our Goal is the contribution and the Key Idea
justifies feasibility.

If the user's inputs describe a benchmark, stop and redirect to
`benchmark-paper-template` (separate plugin).

### Step 2: Fill the thinking template

See: references/thinking-template.md for each template cell's content
contract, what a strong cell looks like, and common failure modes.

Fill the seven cells:

1. Research background. Scenario, importance, motivation.
2. Limitations 1 through 3 (2 is acceptable; more than 3 is not).
3. Key idea or Our Goal. One sentence.
4. Challenges 1 through 3 (similar cap).
5. Methodology modules. One module per challenge.
6. Contributions (3 or 4, each mapped to a section).

If a cell is incomplete given the user's inputs, mark it as a gap
with severity.

### Step 3: Run four self-consistency checks

See: references/consistency-checks.md for the detailed checking
procedure and examples of chain breaks.

Run each check:

1. **Limitations to Key Idea**: does the Key Idea or Goal address
   the stated Limitations? If not, either the Limitations are
   wrong or the Key Idea is misaligned.
2. **Key Idea to Challenges**: do the Challenges arise naturally
   from implementing the Key Idea? If not, the challenges are
   invented to justify modules rather than derived from the idea.
3. **Challenges to Methodology**: does each methodology module
   address one challenge? If not, there is a module without
   justification or a challenge without a fix.
4. **Methodology to Contributions**: do the contributions cover
   each module or experimental result? If not, contributions are
   vague or promising more than the paper delivers.

Every failure is CRITICAL.

### Step 4: Generate methodology outline

See: references/thinking-template.md for the methodology-outline
template.

From the challenges, derive a methodology outline: topic sentence,
per-module subsection names, and per-module one-sentence summary.
This becomes the skeleton for Section 3 or 4 of the paper.

### Step 5: Integrity gate

Before emitting, run the checks in the Integrity gate section
below.

### Step 6: Output

Emit the filled template plus the consistency report in the Output
format below.

## 1. Paper-type positioning
- Type: <Technique Paper or New Problem/Setting Paper>
- Rationale: <one sentence>

## 2. Thinking template

| Stage | Your content |
|---|---|
| Research background | ... |
| Limitation 1 | ... |
| Limitation 2 | ... |
| Limitation 3 (if applicable) | ... |
| Key Idea / Our Goal | ... |
| Challenge 1 | ... |
| Challenge 2 | ... |
| Challenge 3 (if applicable) | ... |
| Methodology topic sentence | ... |
| Module A (addresses Challenge 1) | ... |
| Module B (addresses Challenge 2) | ... |
| Module C (addresses Challenge 3) | ... |
| Contribution 1 | ... (Section <X>) |
| Contribution 2 | ... (Section <Y>) |
| Contribution 3 | ... (Section <Z>) |

## 3. Self-consistency checks
- Check 1 Limitations -> Key Idea: <pass or fail>
- Check 2 Key Idea -> Challenges: <pass or fail>
- Check 3 Challenges -> Methodology: <pass or fail>
- Check 4 Methodology -> Contributions: <pass or fail>

## 4. Severity summary
- <n> CRITICAL, <m> MAJOR, <k> MINOR.
- Top three fixes first: ...

## 5. Next suggested skill
- If all checks pass: `intro-drafter` to produce the Introduction
  paragraph outline.
- If checks fail: address the flagged chain breaks first.
```
