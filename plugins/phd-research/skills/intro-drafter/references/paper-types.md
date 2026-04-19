# Paper-type positioning: Technique versus New Problem/Setting

## Table of contents

1. Why positioning matters
2. Technique Paper profile
3. New Problem/Setting Paper profile
4. Positioning criteria
5. Worked examples: Alpha-SQL, AFlow, LEAD
6. Mixed cases

## 1. Why positioning matters

The paper-type positioning decides where the Introduction's weight
falls. A Technique Paper's narrative spine is the Key Idea; the Goal
gets a one-sentence bridge. A New Problem/Setting Paper's narrative
spine is the Goal or Problem Formulation; the Key Idea is subordinate
to "why this definition is reasonable and feasible".

Mis-positioning is a common Introduction failure. A New Problem paper
written as a Technique paper underweights its contribution. A
Technique paper written as a New Problem paper overclaims.

## 2. Technique Paper profile

A Technique Paper's core contribution is a new method or mechanism
solving an already-defined problem. The Key Idea carries the
narrative.

Signals:

- The problem is well-established (a named benchmark already exists,
  prior work is extensive).
- The contribution is a better way to do something, not a new thing
  to measure or a new setting to study.
- Reviewers will compare against the strongest existing method on
  the same problem.
- Experiments focus on "our method beats baselines".

Introduction weight distribution:

- Paragraph 1: 150-200 words (running example is essential).
- Paragraph 2: 150-200 words (specific limitations of prior methods).
- Paragraph 3: 100-150 words (Goal is a bridge; Key Idea takes the
  weight).
- Paragraph 4: 150-200 words (challenges).
- Paragraph 5: 150-200 words (solution modules).
- Paragraph 6: 100-150 words (contributions).

## 3. New Problem/Setting Paper profile

A New Problem/Setting Paper's core contribution is defining a problem
that the community has not yet studied as such, or a new setting
within a known problem. The Goal or Problem Formulation is the
contribution.

Signals:

- Prior work exists on adjacent problems but not this specific
  framing.
- The contribution is a new way to think about the space, not a new
  method on an existing problem.
- Experiments aim to characterise the new problem, not beat a
  pre-existing leaderboard.
- The Introduction contains a specific "Our Goal" or "Research
  Question" paragraph that is load-bearing.

Introduction weight distribution:

- Paragraph 1: 150-200 words.
- Paragraph 2: 150-200 words (limitations show why existing framings
  miss this problem).
- Paragraph 3: 200-250 words (Goal or Problem Formulation is the
  contribution; Key Idea supports "why this definition is
  reasonable").
- Paragraph 4: 100-150 words (challenges).
- Paragraph 5: 150-200 words (solution modules that realise the
  setting).
- Paragraph 6: 100-150 words (C1 is the problem formulation).

## 4. Positioning criteria

Ask the following in order. The first yes determines the type.

1. Does the paper define a problem or setting the community has not
   studied? If yes, New Problem/Setting.
2. Is the paper's main contribution a new method on an existing
   benchmark? If yes, Technique.
3. Is the paper's main contribution a new benchmark? If yes, use
   `benchmark-paper-template` (separate plugin) instead.
4. Does the paper propose a method that is also a problem
   reformulation? See Mixed cases below.

## 5. Worked examples

### Alpha-SQL (ICML 2025)

Type: Technique Paper.

Rationale: the Text-to-SQL problem is well-established; the paper
contributes an MCTS-based inference procedure for better SQL
generation. The Goal is a one-sentence bridge ("we improve SQL
generation accuracy on complex queries"). Key Idea (MCTS inference-
time search) carries the narrative.

Introduction paragraph weights match the Technique profile: Paragraph
3 is short; Paragraphs 4 and 5 carry detail.

### AFlow (ICLR 2025)

Type: Technique Paper with cross-domain framing.

Rationale: the problem of agent-workflow design exists, but has not
been formulated as a search problem over operator graphs. The paper
is arguably a mixed case. Its published Introduction leads with Key
Idea, not Goal, so the archive case-study classifies it as Technique
with Broader-dimension framing.

If the author had weighted Paragraph 3 more heavily to make
"workflow-as-a-search-space" the contribution, the paper could have
been positioned as New Problem. Either framing is defensible. The
choice affects which reviewers the paper resonates with.

### LEAD (VLDB 2026)

Type: New Problem/Setting Paper.

Rationale: prior work on iterative data selection assumes a full-
dataset inference per iteration. LEAD redefines the setting as
"iterative selection without additional inference". The new setting
is the core contribution; the method (instance-level dynamic
uncertainty from training loss) supports why the setting is
feasible.

Introduction paragraph 3 is load-bearing: the Goal and Research
Question "Can iterative benefits be kept while eliminating
repeated full-dataset inference?" is the headline contribution.

## 6. Mixed cases

A paper can legitimately contribute both a new method and a new
problem framing. When this happens:

- Pick the contribution the paper delivers best.
- State the secondary contribution in Paragraph 6 but do not fight
  for narrative space in Paragraph 3.
- Do not try to frame the paper as both simultaneously; the
  Introduction will lose focus.
- If both contributions are genuinely equal in strength, consider
  splitting into two papers or writing a journal version.

A mixed case cue: the author is unsure which framing is stronger. If
one framing consistently draws clearer reviewer excitement in
pre-submission discussions, pick that framing. If both framings draw
equal excitement, split the paper.
