# Four self-consistency checks

## Table of contents

1. Why check consistency
2. Check 1: Limitations to Key Idea
3. Check 2: Key Idea to Challenges
4. Check 3: Challenges to Methodology
5. Check 4: Methodology to Contributions
6. Common chain breaks

## 1. Why check consistency

A technical paper with a clean logic chain feels inevitable to a
reviewer: each stage flows naturally from the previous one. A paper
with a broken chain feels patchwork, even if every individual stage
is strong. The four consistency checks below catch the patchwork
pattern before drafting begins, saving weeks of rewriting later.

Each check detects a specific class of failure. Running all four in
sequence catches most chain breaks.

## 2. Check 1: Limitations to Key Idea

### Procedure

For each limitation, ask: does the Key Idea or Our Goal address
this limitation, directly or indirectly?

### Detection of failure

- A limitation has no corresponding response in the Key Idea or
  Goal. The limitation is either wrong (it is not actually a
  limitation of the prior work, or it is a limitation the paper
  cannot address) or the Key Idea is misaligned.
- The Key Idea addresses a problem that is not in any Limitation
  cell. The paper is actually solving a different problem from the
  one it motivates in the Introduction.

### Fix

- Remove limitations that the paper does not address.
- Add limitations that justify the Key Idea if they are missing.
- In rare cases, change the Key Idea to align with the motivation.

### Example of failure

Limitation: "prior methods cannot scale to large schemas."
Key Idea: "we introduce chain-of-thought prompting for schema
linking."
Chain break: the Key Idea does not address scale, only accuracy.
Fix: either add a scale mechanism to the Key Idea, or replace the
limitation with "prior methods have low accuracy".

## 3. Check 2: Key Idea to Challenges

### Procedure

For each challenge, ask: does this challenge arise naturally from
implementing the Key Idea?

### Detection of failure

- A challenge has no connection to the Key Idea. It may be a
  generic challenge copied from another paper or a challenge
  invented to justify a module.
- The Key Idea, if implemented naively, would not surface this
  challenge. The challenge is unrelated.

### Fix

- Remove invented challenges.
- If a real challenge is missing, add it.
- Sometimes the Key Idea itself is weaker than thought: the naive
  implementation works and the challenges are artificial. In that
  case, strengthen the Key Idea or accept that the paper's
  contribution is smaller than imagined.

### Example of failure

Key Idea: "use MCTS search at inference time for SQL generation."
Challenge: "labelling data is expensive."
Chain break: MCTS inference-time search is label-free; data labelling
is unrelated to the Key Idea.
Fix: drop the labelling challenge; keep only challenges derived from
MCTS inference (for example, reward design, search-depth trade-off).

## 4. Check 3: Challenges to Methodology

### Procedure

For each methodology module, ask: does this module address one
specific challenge? For each challenge, ask: is there a module that
addresses it?

### Detection of failure

- Module without a challenge (the module addresses a problem the
  paper did not motivate).
- Challenge without a module (the paper complains about a problem
  it does not solve).
- One-to-many mapping (one module addresses multiple challenges)
  without explicit justification. Sometimes this is fine; usually
  it suggests the challenges collapse into one.

### Fix

- Cut modules with no challenge.
- Add modules for orphan challenges, or drop the challenge if the
  paper does not address it.
- Collapse redundant challenges.

### Example of failure

Challenge 1: "reward signal is sparse."
Challenge 2: "search space is exponential."
Module A: "bias the search using prior-learned reward shapes."
Module B: none for Challenge 2.
Chain break: Challenge 2 is orphan.
Fix: either add a module for Challenge 2 (perhaps a pruning
heuristic) or drop Challenge 2.

## 5. Check 4: Methodology to Contributions

### Procedure

For each module, ask: is this module represented in the
Contributions cell? For each contribution, ask: is there a module
or experimental result that delivers it?

### Detection of failure

- A module is not represented in the contributions. The paper does
  the work but forgets to claim credit.
- A contribution is not backed by a module or experiment. The paper
  claims credit without delivery. This is the most dangerous chain
  break; reviewers quote it in reviews.

### Fix

- Add missing contribution entries.
- Remove overclaimed contributions.

### Example of failure

Contribution 3: "theoretical analysis of convergence."
Module: none; no theoretical subsection in the paper.
Chain break: contribution claims theory the paper does not provide.
Fix: either add a theoretical module and subsection or drop
contribution 3.

## 6. Common chain breaks

- **Invented challenges** (fails Check 2).
- **Orphan modules** (fails Check 3).
- **Vague contributions that do not map to modules** (fails Check 4).
- **Key Idea drift**: the Key Idea as filled in the template is
  different from the Key Idea the paper actually develops in the
  methodology. Catch by re-reading the Key Idea cell after the
  Methodology cell is filled.
- **Limitation-Contribution short-circuit**: a contribution that
  does not address any limitation; the paper solves a different
  problem from the one it motivates.

All of the above are CRITICAL gaps. Fix them before running
`intro-drafter` or writing any Introduction prose.
