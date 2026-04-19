# Tech Paper Template

## Why this matters

Before any prose is drafted, a technical paper needs a full logical
skeleton: research background, specific limitations of prior work, the key
idea or research goal, the technical challenges that prevent a naive
solution, the methodology modules that address each challenge, and the
contributions the paper will claim. Students who skip this step end up
with methodology modules that do not fix the limitations they named, or
with contributions that over-promise results the paper does not deliver.

Both of those failures are expensive. A mismatched methodology forces the
author to rewrite either the limitations or the methodology once the
mismatch becomes obvious, usually late in the writing process. An over-
promised contribution is even worse: it usually survives drafting because
the author believes their own claims, and it dies in review when the
reviewer points out that the experiments do not support the contribution.

The Tech Paper Template skill fills the skeleton via a standardised
thinking-template table, positions the paper as Technique or New Problem
or Setting, and runs four self-consistency checks on the logic chain. The
output is suitable for advisor-student brainstorming sessions, weekly
progress meetings, and the final planning step before writing begins.

## The framework

### The thinking-template table

The template has seven cell categories, filled in order. Each cell has a
specific content contract that distinguishes a strong entry from a weak
one. The template is the single source of truth for the paper's logic
during the planning phase.

| Stage | What to fill in |
|---|---|
| Research background | Scenario, importance, motivation. One tight paragraph, not a page of generic buzzwords |
| Limitation 1 | Specific capability gap in a named prior method |
| Limitation 2 | Distinct from Limitation 1; targets a different axis (cost, robustness, data) |
| Limitation 3 (optional) | Additional gap if present; two is acceptable, more than three is not |
| Key Idea or Our Goal | One sentence a reviewer could quote. Technique paper: Key Idea. New Problem paper: Our Goal |
| Challenge 1 | Explains why a naive implementation of the Key Idea or Goal fails |
| Challenge 2 | Distinct challenge, different axis |
| Challenge 3 (optional) | Additional challenge if the problem is genuinely three-dimensional |
| Methodology topic sentence | One sentence setting up the module list |
| Module A (addresses Challenge 1) | Named mechanism with one-sentence summary |
| Module B (addresses Challenge 2) | Named mechanism with one-sentence summary |
| Module C (addresses Challenge 3) | Named mechanism with one-sentence summary |
| Contribution 1 | Problem formulation or framework (Section X) |
| Contribution 2 | Primary technical point (Section Y) |
| Contribution 3 | Secondary technical point or evaluation (Section Z) |

A cell that lives only in the author's head has not been filled; the
skill flags it with severity. Running a weekly-meeting cycle that
reviews the template surface-level tracks which cells mature as the
project progresses. Early in the project, many cells will be empty or
tentative; by the writing phase, every cell should be concrete.

### Paper-type positioning

The template is used two different ways depending on paper type:

- **Technique Paper.** The narrative axis is Key Idea or Mechanism. Our
  Goal gets one sentence in passing. Contributions emphasise the method
  and its evidence. Alpha-SQL and AFlow are both this type.
- **New Problem or Setting Paper.** The narrative axis is Our Goal or
  Problem Formulation, which is itself a contribution. The Key Idea
  supports "why this definition is reasonable and feasible".
  Contributions emphasise the formulation and its implications. LEAD is
  this type.

Positioning changes how the cells are weighted. In a Technique paper, Our
Goal is a short transition; in a New Problem paper, Our Goal is load-
bearing and the Key Idea becomes the justification. A paper that
straddles the two positions reads as confused; reviewers will ask whether
the primary contribution is the method or the problem, and the author
will have no clear answer.

### The four self-consistency checks

After the template is filled, four checks verify the logic chain. Every
failure is CRITICAL: the paper cannot be written coherently until it is
fixed.

**Check 1: Limitations to Key Idea.** Does the Key Idea or Goal address
the stated Limitations? If the Key Idea solves problems the Limitations
never named, the Limitations section is wrong, the Key Idea is
misaligned, or both. A frequent failure: Limitations describe efficiency
gaps, but the Key Idea is about accuracy. The paper cannot then claim
the Key Idea solves the Limitations.

**Check 2: Key Idea to Challenges.** Do the Challenges arise naturally
from implementing the Key Idea? If the Challenges feel invented, they
probably are. A common failure: the Key Idea is "use MCTS for Text-to-
SQL", but the listed Challenges are "how to parse SQL" and "how to access
databases", which are generic concerns unrelated to the MCTS choice. The
genuine MCTS challenges (search space design, reward function, rollout
budget) are absent.

**Check 3: Challenges to Methodology.** Does each methodology module
address one Challenge? A one-to-one mapping is the target. A module
without a matching challenge either is not justified or is solving a
different problem than the paper claims. A challenge without a module is
an unresolved gap. Many-to-one or one-to-many mappings are warning
signs.

**Check 4: Methodology to Contributions.** Do the Contributions cover
each module or experimental result? Contributions vague enough to apply
to any paper ("novel framework", "extensive experiments") fail this
check. Contributions that promise results the experiments do not
support fail this check. Every contribution should point at a specific
methodological or empirical delivery.

### Methodology outline as a by-product

Once all checks pass, the template produces a methodology outline: topic
sentence, per-module subsection names, per-module one-sentence
summaries. This becomes the skeleton for the paper's Methodology
section. Running it before prose drafting saves rewrites later: writers
who skip the outline stage tend to discover mid-Section-3 that their
modules do not actually match their challenges.

## Key checks

- **Paper-type positioning** is consistent with the actual contribution
  (Technique paper is not shoehorned into New Problem framing, or vice
  versa).
- **Limitations are specific and cite-able**, not vague generalities.
- **Key Idea or Goal is a single sentence** a reviewer could quote
  directly.
- **Challenges derive from implementing the Key Idea**; they are not
  invented to justify modules.
- **Methodology modules map one-to-one with Challenges.**
- **Contributions map to methodology modules and to specific sections**,
  each with a Section-X pointer.
- **All four self-consistency checks pass**, or the chain break is
  surfaced as CRITICAL.

## Worked example

Consider Alpha-SQL (ICML 2025) filled into the template. The full
analysis lives in [case-studies/alpha-sql](../../case-studies/alpha-sql.md);
here is the template-level summary.

| Stage | Alpha-SQL content |
|---|---|
| Research background | Text-to-SQL democratises database access; LLMs enabled rapid progress |
| Limitation 1 | Trained methods require extensive labelled data and repeated fine-tuning as base models change |
| Limitation 2 | Zero-shot methods face the challenge of transferring general LLM knowledge to the structured SQL task without supervision |
| Key Idea | Use MCTS to dynamically generate and explore SQL construction actions guided by LLM reasoning |
| Challenge | (Folded into methodology at AI-venue page limits) |
| Methodology topic sentence | Alpha-SQL leverages an MCTS framework with two novel techniques |
| Module A | LLM-as-Action-Model: invokes the LLM to produce Chain-of-Thought reasoning after each action, stored per-node |
| Module B | Self-supervised reward function: computes self-consistency across sampled SQL queries per reasoning path |
| Contribution 1 | Fine-tuning-free, plug-and-play Text-to-SQL framework |
| Contribution 2 | LLM-as-Action-Model within MCTS (Section 3) |
| Contribution 3 | Self-supervised reward function based on execution self-consistency (Section 3) |
| Contribution 4 | 69.7% BIRD development-set accuracy with open-source LLMs, significantly outperforming existing zero-shot baselines (Section 4) |

Running the four checks:

- Check 1 (Limitations to Key Idea): Limitation 1 is training cost; the
  Key Idea avoids training entirely. Limitation 2 is zero-shot knowledge
  transfer; the Key Idea uses MCTS plus Chain-of-Thought to guide
  transfer. Both pass.
- Check 2 (Key Idea to Challenges): formally unresolved because the paper
  does not enumerate challenges. The implicit challenges (MCTS reward
  without ground-truth SQL, action-space design for SQL construction,
  reasoning-continuity across search states) are handled inside the
  methodology section.
- Check 3 (Challenges to Methodology): Modules A and B correspond to
  implicit challenges of reasoning-continuity and reward design. A
  reviewer would prefer an explicit Challenges paragraph, but the
  methodology does cover both.
- Check 4 (Methodology to Contributions): Contributions 1-3 map to
  framework and modules; Contribution 4 reports results. All pass.

The template exercise surfaces that Alpha-SQL made a page-limit trade-off
by folding challenges into methodology. For a database-venue submission
(SIGMOD, VLDB), the student would be advised to restore the challenges
paragraph before submitting.

## Try it with the plugin

Install the plugin per the
[root README](../../../../README.md#quick-install) and invoke naturally.
The skill self-triggers on phrases like "paper skeleton", "paper logic
chain", "thinking template", or "paper-structure planning". Typical
usage: run [idea-evaluator](../idea-evaluator/overview.md) first to
confirm the idea is worth pursuing, then run tech-paper-template to lock
the skeleton, then run [intro-drafter](../intro-drafter/overview.md) to
convert the skeleton into the Introduction outline.

## Source

Adapted from:

- [archive/v1-source/1_Guide/03_Paper_Writing/3.3_技术类Full_Paper思考模板.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.3_技术类Full_Paper思考模板.md)
- Plugin SKILL.md:
  [/plugins/phd-research/skills/tech-paper-template/SKILL.md](/plugins/phd-research/skills/tech-paper-template/SKILL.md)
- Plugin reference:
  [/plugins/phd-research/skills/tech-paper-template/references/thinking-template.md](/plugins/phd-research/skills/tech-paper-template/references/thinking-template.md)

---

[English] | [中文](../../../zh/skills/tech-paper-template/overview.md)
