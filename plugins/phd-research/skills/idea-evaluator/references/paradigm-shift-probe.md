# Paradigm-shift probe

## Table of contents

1. Incremental versus disruptive
2. The four probing principles
3. Scoring the probe
4. When to delegate to disruptive-innovation-scout
5. Risk and reward trade-off
6. Portfolio strategy for a PhD

## 1. Incremental versus disruptive

Most published ideas are incremental: they take an existing baseline
and push it on one or two of the Higher, Faster, Stronger, Cheaper,
Broader dimensions. Incremental work is the backbone of a PhD career
and can absolutely reach top venues.

Disruptive work reshapes the problem itself rather than its solution
it challenges a hidden assumption, surfaces a previously ignored
problem, or rides a technology-cycle shift that makes a new approach
possible. Disruptive ideas carry higher reward (a strong disruptive
paper defines the subfield for years) and higher risk (most disruptive
attempts fail or take years to pay off).

The probe is not a gate. Even a strictly incremental idea can justify
a top-venue paper. The probe's purpose is twofold:

- Identify disruptive potential early, so the student can choose to
  pursue it consciously rather than accidentally reducing it to
  incremental work mid-project.
- Flag ideas that look disruptive but are actually incremental (or
  vice versa), so the Introduction framing matches the reality.

## 2. The four probing principles

### 2.1 First Principles

Does the idea challenge an assumption the field takes for granted?

Signal that yes: the idea starts with "everybody assumes X, but what
if X is wrong" and produces a specific X. Examples of X include
assumptions like "iterative methods require full-dataset inference
every round" (LEAD broke this), or "visualisation quality reduces to
aesthetics or correctness alone" (VisJudge-Bench broke this).

Signal that no: the idea starts with a known technique and proposes a
variant. No assumption is challenged, only a hyperparameter or a
training recipe is tweaked.

### 2.2 Elephant in the Room

Does the idea address a problem the community sees but avoids?

Signal that yes: the paper includes a section that says "this problem
has been known for years but nobody has touched it because X", and
the paper provides a path past X. Examples: agent evaluation beyond
toy tasks; reproducibility of RLHF across labs; domain shift in
production deployment.

Signal that no: the problem is new and small, rather than old and
large.

### 2.3 Technology Cycle

Does a recent technology shift enable this idea to work now, when it
could not before?

Signal that yes: the idea depends on capability that did not exist
two years ago. Example: LLM agents only became practical after
instruction-tuned base models matured; reinforcement-learning from
execution feedback only became tractable after cheap-inference
infrastructure. An idea that could have been done five years ago but
was not, is usually incremental.

Signal that no: the idea could have been attempted at any point in
the last decade with minor modifications.

### 2.4 Hamming's Rule

If this idea succeeded, would it change the community's top priority
list?

Signal that yes: the idea is a top-three problem in the student's
advisor's list; colleagues light up when they hear it; reviewers would
call it a landmark paper if done well.

Signal that no: the idea is niche, or its success improves a metric
that only a handful of people care about.

## 3. Scoring the probe

Answer each of the four principles as Yes, Partial, or No. Count Yes
as 2, Partial as 1, No as 0. Total score 0-8.

- **0-2**: pure incremental. Frame as incremental in the Introduction;
  emphasise Higher or Faster.
- **3-4**: incremental with disruptive seeds. Explicitly call out the
  disruptive aspect in the Introduction to capture reader attention.
- **5-6**: disruptive potential. Consider running
  `disruptive-innovation-scout` to deepen the framing.
- **7-8**: genuine paradigm-shift candidate. Definitely run
  `disruptive-innovation-scout`; the Introduction should lead with
  First Principles framing.

## 4. When to delegate to disruptive-innovation-scout

Recommend the user switch to `disruptive-innovation-scout` when:

- Probe score is 5 or higher.
- Probe score is lower but the user explicitly wants to pursue a
  disruptive angle.
- The idea has a First Principles signal with a concrete hidden
  assumption that the user can state in one sentence.
- The paper is targeting a venue that rewards paradigm-shift framing
  (ICLR Outstanding, NeurIPS Spotlight, VLDB Best Paper).

Do not delegate when the idea is genuinely incremental; forcing
disruptive framing on incremental work weakens the paper.

## 5. Risk and reward trade-off

Disruptive work has three distinct risk categories:

- **Execution risk**: the idea is right but the experiments fail. Higher
  for disruptive because the mechanism is unproven.
- **Reception risk**: the idea is right and the experiments succeed,
  but reviewers do not recognise the contribution. High for early
  disruptive work.
- **Timeline risk**: the idea requires more iterations than an
  incremental project; lifecycle fit tightens.

Against these, the rewards of a successful disruptive paper:

- Career-defining impact on a single paper.
- A new research programme around the framing.
- Citation compounding over 5+ years.

Rule of thumb: if the student has already published at least one
incremental top-venue paper, they have earned the credibility to
attempt a disruptive project. If not, anchor the first paper in
incremental territory and let disruptive come second.

## 6. Portfolio strategy for a PhD

A healthy PhD research portfolio across 3-5 years usually has:

- 60-70 percent incremental work: steady publications, builds the
  student's technical depth and writing muscle.
- 20-30 percent cross-disciplinary or Broader work: transplants a
  known idea to a new context; lower risk than disruptive, higher
  reward than incremental.
- 10-20 percent disruptive work: one or two ambitious projects over
  the PhD; not every one will land, but a single success pays for
  several failed attempts.

Use the paradigm-shift probe to classify each candidate project and
balance the portfolio explicitly. The worst outcome is four disruptive
projects that all fail to publish; the second worst is four
incremental projects that publish but fail to differentiate the
student from their peers.
