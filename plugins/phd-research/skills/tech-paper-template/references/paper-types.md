# Paper-type positioning for technical papers

## Table of contents

1. Three paper-type categories
2. Technique Paper
3. New Problem/Setting Paper
4. Mixed case (cross-domain technique)
5. Positioning questions
6. How positioning affects the template

## 1. Three paper-type categories

Technical papers at top venues (SIGMOD, VLDB, ICML, NeurIPS, ICLR,
ACL) fall into three categories. Positioning the paper correctly is
the first planning decision.

- **Technique Paper**: new method or mechanism on an existing
  problem. Key Idea carries the narrative.
- **New Problem/Setting Paper**: a new problem formulation or a new
  setting within a known problem. Goal or Problem Formulation
  carries the narrative.
- **Cross-domain Technique Paper**: a Technique Paper whose
  contribution transplants an idea from one field to another. The
  Key Idea carries the narrative but the Broader dimension from the
  `idea-evaluator` framework is emphasised in the Introduction.

Benchmark papers are a separate category; use
`benchmark-paper-template` (separate plugin).

## 2. Technique Paper

Signals:

- The problem is well-established. A named benchmark exists; prior
  work is extensive.
- The contribution is "we do X better" for a specific X.
- Reviewers compare against the strongest existing method on the
  same problem.
- Experiments focus on dominating baselines on a shared metric.

Template implications:

- Key Idea cell is load-bearing.
- Goal is a short bridge, not a contribution.
- Challenges flow from implementing the Key Idea.
- Contribution 1 is usually the framework or method name.

## 3. New Problem/Setting Paper

Signals:

- The problem is a new framing the community has not studied as
  such.
- Prior work exists on adjacent problems but not this specific
  framing.
- The contribution is a new way to think about the space, not a
  new method on an existing problem.
- Experiments characterise the new problem rather than beating a
  leaderboard.

Template implications:

- Goal cell is load-bearing. Multiple sentences may be appropriate.
- Key Idea supports "why this definition is reasonable and
  feasible".
- Limitations paragraph shows why existing framings miss the
  problem.
- Contribution 1 is the problem formulation itself.

## 4. Mixed case: cross-domain technique

A paper transplanting a mature idea from one field to another is a
Technique Paper with a Broader-dimension framing.

Signals:

- The technique is mature in one subfield but new to another.
- The Introduction leans on "inspired by X from field A, we apply
  it to field B".
- The contribution is the transfer and the mechanism, not a new
  technique invented from scratch.

Template implications:

- Key Idea includes both the source-field technique and the
  transfer mechanism.
- Limitations emphasise the absence of field B from field A's
  literature.
- Challenges usually include "transferring idea X across the
  domain gap".
- Contribution 1 names the transfer.

Example: AFlow (ICLR 2025) transplants operator-graph search (from
neural architecture search) into agent-workflow design.

## 5. Positioning questions

Ask the following in order. First yes decides:

1. Is the paper's primary contribution a benchmark? If yes, stop
   and redirect to `benchmark-paper-template` (separate plugin).
2. Is the paper's primary contribution a new problem formulation
   that the community has not studied? If yes, New Problem/Setting.
3. Is the paper's primary contribution a technique transplanted
   from another field? If yes, Mixed (Technique with cross-domain
   framing).
4. Default: Technique Paper.

If the user's answers conflict with this order, investigate. A
paper can legitimately have two strong framings; see the mixed-case
discussion in the Introduction-drafter skill's paper-types
reference.

## 6. How positioning affects the template

| Cell | Technique | New Problem/Setting | Mixed Cross-domain |
|---|---|---|---|
| Background | Scenario that shows the problem | Scenario that shows the phenomenon | Scenario that shows both fields |
| Limitations | Specific to prior methods | Specific to prior framings | Specific to field B's absence from field A |
| Key Idea / Goal | Key Idea sentence dominant | Goal sentence dominant, often multiple sentences | Key Idea names the transfer |
| Challenges | Derived from implementing Key Idea | Derived from realising the new setting | Derived from domain gap |
| Methodology | Modules that realise Key Idea | Modules that realise the setting | Modules that realise the transfer |
| Contributions | C1 = framework or method; C2-C4 = techniques, evaluation | C1 = problem formulation; C2-C4 = framework, technique, evaluation | C1 = transfer framing; C2-C4 = method, evaluation |

Apply the row that matches the positioning when filling the
template in Step 2 of the skill's core procedure.
