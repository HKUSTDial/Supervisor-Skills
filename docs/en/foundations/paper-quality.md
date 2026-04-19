# Paper quality: the 4N framework

Many incoming PhD students want to publish fast, yet they have not
internalised what a good paper actually looks like from the reviewer's side
of the table. The result is months spent on ideas that no top-venue reviewer
would have accepted. The answer is a simple, memorable rubric that a
student can apply before starting a project and revisit at each writing
milestone: the 4N framework.

A strong paper scores well on all four dimensions; a weak paper fails on at
least one. Reviewers use a version of this rubric silently, even when they
do not spell it out. Students who learn it explicitly save themselves from
predictable rejection patterns and also from a worse fate: spending a year
on an idea that is not going to produce a paper anyone wants to read.

The four dimensions are deliberately memorable: four words that each begin
with N. Novel Problem, Novel Method, Nice Story, Nice Presentation. A
student should be able to run the rubric in their head in under a minute on
any idea an advisor proposes and on their own drafts at each milestone.

## Novel Problem

### Definition

The paper defines a problem that is genuinely useful and that the community
has not already solved. It is not a repackaging of a solved problem under a
new name, and it is not a problem that exists only because the author wants
to apply a specific technique.

### Positive indicators

- The problem statement makes sense to a practitioner, not only to a
  researcher chasing publications. If a domain expert (industry DBA,
  working data scientist, experienced software engineer) hears the problem
  and says "yes, I hit that", the problem is probably real.
- There is a concrete real-world setting where this problem currently causes
  pain, for example schema linking on databases with thousands of tables, or
  long-horizon agent planning under realistic cost constraints. A problem
  with no setting is a problem without stakes.
- A knowledgeable peer reading the problem statement cannot immediately
  point at a published paper that already addresses it. If the peer can,
  the problem is solved; if the peer is uncertain, a literature check is
  required before commitment.

### Antipatterns

- "Old school" problems recast with surface-level novelty (slightly
  different input format, same core task). Reviewers recognise these
  instantly.
- Problems that exist only because the author wants to apply a specific
  technique (the technique looking for a problem). If you invented the
  technique first and are now shopping for a problem it could fit,
  reviewers will feel the mismatch.
- Problem definitions so narrow they fit exactly one dataset and one
  hyperparameter setting. Generalisation is part of what makes a problem
  worth solving.

## Novel Method

### Definition

The method solves the problem in a way that is not an obvious combination of
existing techniques. A peer reading the method should have to think before
they can say "I could have written that".

### Positive indicators

- The method exploits a non-obvious property of the problem: data
  distribution, hardware feature, new tool capability, or an asymmetry
  between inputs and outputs the field has overlooked.
- At least one core mechanism is new to the venue's literature, not merely
  new to the author. Borrowing from sibling subfields is legitimate when
  the adaptation is substantive; a direct import without adaptation is not.
- Removing the novel mechanism causes a measurable performance drop in the
  ablation, demonstrating it carries its weight. If ablating the "novel
  core" produces no performance change, it was not the core.

### Antipatterns

- Stacking existing techniques with no principled justification ("we
  combine A, B, and C, so it works better"). Reviewers call this a grab-bag
  paper and reject it.
- Reusing a well-known technique from a sibling subfield with no adaptation
  to the target problem's structure. Someone already published "MCTS for X";
  publishing "MCTS for Y" without a principled adaptation is delta work.
- "Delta work" that patches an existing paper by one or two percent and
  claims a new contribution. The improvement may be real but is not
  enough to anchor a top-venue paper.

## Nice Story

### Definition

The paper reads as a single argument, not a list of claims. The Introduction
tells the reader what problem is being solved, why it is hard, what the key
insight is, and how the contribution maps to the sections. The methodology,
experiments, and conclusion all land on that same argument.

### Positive indicators

- The Introduction follows the six-paragraph flowchart (Background,
  Limitations, Goal or Key Idea, Challenges, Solution Overview,
  Contributions) with no broken links between paragraphs.
- A running example is introduced in the Introduction and reappears in the
  methodology and experiments. Reviewers reading only the figures should
  still understand the paper's story.
- Contributions map one-to-one to methodology modules or experimental
  results; the reader never wonders what a specific contribution refers to.

### Antipatterns

- Introduction that skips directly from background to methodology with no
  limitations or challenges paragraph. The reader cannot tell why the
  method is needed.
- Contribution bullets that could belong to any paper in the subfield ("we
  propose a novel framework", "we show extensive experiments"). These are
  empty signifiers; reviewers discount them.
- Running example introduced in Paragraph 1 of the Introduction and then
  abandoned, never reappearing in the methodology or experiments. The
  example's purpose is the story's through-line, not decoration.

## Nice Presentation

### Definition

Figures, tables, formatting, typography, and grammar are professional. A
reviewer scanning the paper for one minute should already respect its craft.
Presentation is not superficial; it is the reviewer's first evidence that
the authors care about the work.

### Positive indicators

- Figures are vector format (PDF, EPS, SVG), with fonts legible at 8pt after
  scaling, colour-blind-safe palettes, and self-contained captions whose
  first sentence states the figure's finding.
- Equations are numbered contiguously and every numbered equation is
  referenced somewhere in the text.
- No em-dashes used as sentence connectors; no banned AI-tone vocabulary
  (see [pre-submission-reviewer](../skills/pre-submission-reviewer/overview.md)
  for the canonical list).
- Citations use the correct command with non-breaking tildes (for example,
  `ResNet~\cite{X}` rather than `ResNet \cite{X}`). Labels use underscores,
  not spaces or hyphens.

### Antipatterns

- Raster figures (PNG, JPG) scaled up until they pixelate. This is the most
  common immediate mark of an amateur paper.
- Mixed quote styles, mixed typography, inconsistent section numbering.
  Reviewers notice even when the authors do not.
- Chinglish phrasing, missing articles, tense drift, and overuse of passive
  voice. Non-native authors are the most exposed to these.
- Chartjunk (3D bars, unnecessary backgrounds, excessive grid lines).
  Chartjunk produces visual noise at the cost of signal.

## How to use this rubric before and during writing

Before starting a project, score the proposed paper on each of the four Ns
on a 1-to-3 scale (weak, adequate, strong). Any dimension scoring weak
deserves a direct conversation with an advisor: is the project really ready,
or does it need a pivot first? A project weak on Novel Problem is probably
not salvageable by working harder; a project weak on Nice Presentation is
fixable with effort.

During writing, revisit the rubric at each milestone:

- After idea vetting, reconfirm Novel Problem and Novel Method. The
  [idea-evaluator](../skills/idea-evaluator/overview.md) skill
  operationalises this check with an explicit five-dimension scoring plus a
  fatal-flaws audit.
- After locking the skeleton, score Nice Story via the self-consistency
  checks in [tech-paper-template](../skills/tech-paper-template/overview.md).
  Every chain break in the skeleton is a Nice Story failure in waiting.
- After drafting the Introduction, run
  [intro-drafter](../skills/intro-drafter/overview.md) to verify the
  six-paragraph flowchart. The flowchart is the most visible part of Nice
  Story.
- Three to five days before submission, run
  [pre-submission-reviewer](../skills/pre-submission-reviewer/overview.md)
  to stress-test Nice Presentation against the mechanical rules (figures,
  LaTeX, grammar, banned vocabulary, em-dashes).

The rubric is not a one-time gate. It is a recurring check that catches
different failures at different stages. A strong Novel Problem at the idea
stage can still be betrayed by a weak Nice Story at the writing stage, and
a strong Nice Story can still be punished by a careless Nice Presentation.

## Source

Adapted from
[archive/v1-source/1_Guide/01_Preliminary/1.1_如何评价一篇论文的质量.md](/archive/v1-source/1_Guide/01_Preliminary/1.1_如何评价一篇论文的质量.md).

---

[English] | [中文](../../zh/foundations/paper-quality.md)
