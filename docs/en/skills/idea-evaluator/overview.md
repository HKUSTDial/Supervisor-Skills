# Idea Evaluator

## Why this matters

Most failed PhD papers fail at the idea stage, not the writing stage. A
student commits three or six months to a topic without a reviewer-grade
check on novelty, feasibility, or fit against their actual capability and
timeline. The cost of this unchecked commitment is huge: months of effort
on an idea a peer could have flagged as dominated by prior work in five
minutes, or on an idea that fits a four-month lifecycle but does not fit
the student's two-hours-per-day reality.

The reviewer-grade check is not a mystery. Experienced advisors run it
silently whenever a student proposes an idea. They match the idea against
prior work, estimate the feasibility under the student's resources, and
issue a verdict. Students without direct advisor access, or students whose
advisors run the check implicitly rather than explicitly, miss the
mechanism. The Idea Evaluator skill externalises that check into a
structured rubric so students can run it themselves before the commitment,
and so advisors can debug where an idea fails rather than issuing a vague
"this will not work".

## The framework

The skill combines four layers of checking, applied in a specific order.
The ordering matters. A short-circuit at any layer can save the remaining
work.

### Layer 1: Fatal-flaws audit (early gate)

Runs first. Ten canonical flaws cover the most common rejection patterns,
from "no novelty versus the closest prior work" to "lifecycle mismatch so
severe the student cannot finish in time". If any flaw is tagged CRITICAL
under the severity taxonomy, the skill short-circuits: the rest of the
evaluation would be decoration on a rejection verdict. The user gets the
flaw name, the defense prescription, and a Reject and Pivot recommendation.

This ordering is deliberate. A seven-out-of-ten "Higher" score does not
matter if the idea is a rebrand of a 2023 paper. Running the scoring
before the fatal-flaws audit produces false comfort: a student sees the
strong Higher score and commits, not realising the fatal flaw invalidates
the score.

The CRITICAL versus MAJOR versus MINOR taxonomy is reviewer-style. CRITICAL
means the idea is rejectable on this one factor alone. MAJOR means
reviewers will flag it in round one and the paper will need substantial
revision. MINOR means polish.

### Layer 2: Lifecycle and capability matching

Every idea has a lifecycle measured in months: how long before the field
moves past it. A trending LLM-agent application topic has a 3-to-6-month
lifecycle; a foundational-theory topic has a 12+ month lifecycle. If the
student's execution window is longer than the lifecycle, the idea is
probably stale by submission time.

Layer 2 maps the idea onto one of six categories (Application, Foundational
Theory, Cross-Disciplinary, Frontier Exploration, Data-Intensive,
Innovative Technique) and checks whether the user's declared capability
(effective hours per week, skill depth, theoretical versus applied
strength) matches the category's execution demands.

| Idea type | Lifecycle | Fits students who are |
|---|---|---|
| Application research | Short (3-6 months) | Fast coders, fast experimenters, comfortable under time pressure |
| Foundational theory | Long (6-12 months) | Mathematically strong, patient, willing to sit with hard proofs |
| Cross-disciplinary | Medium (6-9 months) | Coming from another field, able to bridge conventions |
| Frontier exploration | Short to medium (3-9 months) | Balanced theory and implementation, high self-study bandwidth |
| Data-intensive | Medium (6-12 months) | Strong data engineering, able to handle large-scale pipelines |
| Innovative technique | Long (12+ months) | Deep foundations, willing to challenge existing assumptions |

A student with two effective hours per day who proposes a
frontier-exploration idea on a four-month timeline triggers a lifecycle
mismatch. The skill flags it and proposes scope trimming or capability
upgrade. Neither of these is a value judgment on the student; they are
structural observations that preserve the student's time.

### Layer 3: Five-dimension scoring (Higher, Faster, Stronger, Cheaper, Broader)

The core novelty axis. Each dimension asks a different question of the
idea, and strong ideas usually dominate on two or three dimensions rather
than being mediocre on all five.

| Dimension | Core target | Entry strategies |
|---|---|---|
| Higher | Accuracy, effectiveness gains | Information or modality augmentation, feedback-driven refinement, error-driven analysis |
| Faster | Efficiency, cost reduction | Caching and experience reuse, parallelisation and decoupling, early exit and dynamic routing |
| Stronger | Robustness, generalisation | Noise and fault tolerance, exception recovery, decoupled representation |
| Cheaper | Data or deployment cost reduction | LLM-based data synthesis, active learning with human in the loop, knowledge distillation |
| Broader | Cross-domain transplantation, unification | Cross-domain transplantation, generalisation and unification |

Each dimension is scored 1 to 10 with evidence drawn from the user's
stated contribution. The highest-ceiling two or three dimensions become the
paper's emphasis in the Introduction. The weaker dimensions are not
hidden; they are acknowledged as limitations or left for future work.

A key anti-pattern the scoring surfaces: claiming strength on all five
dimensions. No real idea is genuinely strong across all five. A paper that
claims so is almost certainly over-claiming.

### Layer 4: Paradigm-shift probe and feasibility check

Four probing questions test whether the idea is incremental (the normal
case) or carries disruptive potential:

1. Does it challenge a hidden assumption the field takes for granted?
2. Does it address an elephant-in-the-room problem everyone sees but nobody
   wants to touch?
3. Does it ride a technology-cycle shift (LLMs, new hardware, new
   platforms)?
4. If this problem solved itself, would the field change meaningfully
   (Hamming's Rule)?

Two or more yes answers means the user should switch to
[disruptive-innovation-scout](../disruptive-innovation-scout/overview.md)
for depth. The probe here gives the signal; the scout explores it. The two
skills are complementary by design: the evaluator is fast and broad, the
scout is deep and slow.

A feasibility pass then checks compute risk, data risk, engineering risk,
and timeline risk against the user's actual resources. Every risk gets a
level (low, medium, high) and a mitigation. The feasibility check is
deliberately grounded in the user's stated resources rather than generic
assumptions; "four-GPU RTX 3090" is different from "unrestricted compute
budget", and the evaluation should reflect that.

## Named heuristics

- **Higher, Faster, Stronger, Cheaper, Broader**, the five improvement
  dimensions, each memorable in one word.
- **Fatal-flaws audit runs first**, to avoid decorating a rejection with
  scoring.
- **Strong Accept, Accept with Revisions, Reject and Pivot**, the three
  verdicts, each with explicit thresholds (Strong Accept requires two
  dimensions at 8+ and zero CRITICAL flaws).
- **Lifecycle-capability match**, with six categories and a self-assessment
  on effective hours per week.
- **Hamming's Rule**, as the fourth paradigm-shift probe: if this problem
  solved itself, would the field change?
- **CRITICAL / MAJOR / MINOR severity**, reviewer-style, used for both
  fatal flaws and feasibility risks.

## Worked example

Consider a student with four-GPU RTX 3090 hardware, two effective hours per
day, strong PyTorch and weak C++, proposing a tree-search based MCTS
approach for zero-shot Text-to-SQL on BIRD, targeting a five-point accuracy
lift in four months.

The fatal-flaws audit notes that Alpha-SQL (ICML 2025) already occupies
exactly this design space, so the CRITICAL flaw "dominated by closest
prior work" might fire unless the student can name a specific axis along
which the new proposal differentiates. Suppose the student responds that
their angle is a new self-consistency reward based on execution-equivalence
clustering rather than the sampled-query ensemble Alpha-SQL uses. That is
a defensible differentiation; the fatal flaw downgrades from CRITICAL to
MAJOR.

The lifecycle check tags this as frontier exploration: a short-to-medium
lifecycle of 3-9 months. A four-month plan fits, but only if the student
can sustain at least three effective hours per day across the window. At
two hours per day, the skill flags a yellow lifecycle risk and suggests
either scope reduction (target one dataset rather than three) or capability
upgrade (block protected time, reduce other commitments).

The five-dimension scoring likely produces a strong Higher (accuracy-
focused method), moderate Stronger (self-consistency should help noisy
queries), weak Faster, weak Cheaper, weak Broader. The recommendation is to
emphasise Higher and Stronger in the Introduction and to treat Faster as a
secondary discussion rather than a claim the paper makes. Writing about
Faster without empirical support would backfire in review.

The paradigm-shift probe scores 1 yes (Technology Cycle: LLM-based
Text-to-SQL was infeasible three years ago). That is below the disruptive
threshold. The skill issues Accept with Revisions: proceed, but tighten
scope to two datasets and confirm the self-consistency reward's novelty is
honest before the first experiment. Honesty here means the student has
read Alpha-SQL carefully enough to articulate exactly where their reward
differs.

## Try it with the plugin

Install the plugin per the
[root README](../../../../README.md#quick-install) and ask naturally. The
skill self-triggers on phrases like "evaluate this idea", "score this
idea", "assess feasibility", "novelty check", or "is this a good research
direction". Phrase the idea as a short paragraph covering the problem, the
proposed approach, target venue, hardware, effective hours per week, and
timeline; the skill will fill in what it can and ask for missing inputs.

## Source

Adapted from:

- [archive/v1-source/1_Guide/02_Idea_Generation/2.1_Idea的生命周期与能力匹配.md](/archive/v1-source/1_Guide/02_Idea_Generation/2.1_Idea的生命周期与能力匹配.md)
- [archive/v1-source/1_Guide/02_Idea_Generation/2.2_想Idea的思路_更高更快更强.md](/archive/v1-source/1_Guide/02_Idea_Generation/2.2_想Idea的思路_更高更快更强.md)
- [archive/v1-source/1_Guide/02_Idea_Generation/2.3_进阶_如何做颠覆式创新.md](/archive/v1-source/1_Guide/02_Idea_Generation/2.3_进阶_如何做颠覆式创新.md)
  (paradigm-shift probe only; depth lives in the scout skill)
- Plugin SKILL.md:
  [/plugins/phd-research/skills/idea-evaluator/SKILL.md](/plugins/phd-research/skills/idea-evaluator/SKILL.md)

---

[English] | [中文](../../../zh/skills/idea-evaluator/overview.md)
