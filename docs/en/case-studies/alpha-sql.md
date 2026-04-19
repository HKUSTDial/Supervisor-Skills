# ICML 2025: Alpha-SQL writing analysis

## Paper context

- **Venue**: ICML 2025 ([OpenReview link](https://openreview.net/pdf?id=kGg1ndttmI))
- **Title**: Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree
  Search
- **Problem addressed**: Zero-shot Text-to-SQL generation. Prior trained
  methods need expensive labelled data and repeat fine-tuning whenever a
  new base model appears; prior zero-shot methods struggle to transfer
  general LLM knowledge to the structured task of SQL generation.
- **Core contribution**: A fine-tuning-free, plug-and-play framework that
  combines Monte Carlo Tree Search (MCTS) with Chain-of-Thought-style
  reasoning inside search nodes, plus a self-supervised reward function
  based on execution self-consistency across sampled queries.

Alpha-SQL is a Technique Paper in the terminology of
[tech-paper-template](../skills/tech-paper-template/overview.md): it
solves a known problem (Text-to-SQL) with a new method (MCTS-guided
zero-shot generation). The narrative axis is Key Idea or Mechanism, and
Our Goal gets one sentence in passing.

## Writing craft: what works and why

### Introduction structure

![Alpha-SQL Introduction flowchart](/assets/images/intro_flowchart_alpha_sql.png)

Figure: Alpha-SQL's Introduction mapped onto the six-paragraph
flowchart. The paper collapses Challenges and Contributions into the
Solution Overview because of ICML's tight page budget.

The Introduction follows the six-paragraph flowchart from
[intro-drafter](../skills/intro-drafter/overview.md), with two
deliberate page-budget compressions.

**Paragraph 1 (Background).** Opens with a one-sentence definition of
Text-to-SQL and a statement of why it matters ("simplifying access to
relational databases and enabling both lay and expert users to derive
insights effectively"). Immediately grounds the reader in the real-world
value proposition, not the technique.

**Paragraph 2 (Limitations).** Rather than three limitations, Alpha-SQL
uses two, each corresponding to a family of prior work:

- *Trained methods.* Pre-training or fine-tuning on task-specific
  datasets works but costs labelled data and compute, and the investment
  repeats every time a newer base model appears.
- *Zero-shot methods.* Cheaper to run, but hit a fundamental barrier:
  transferring LLM general knowledge to the specific structured task of
  SQL without supervision is hard.

The categorisation is clean. Reviewers know exactly where the paper
sits (zero-shot track) and what it is reacting to (transfer difficulty).

**Paragraph 3 (Problem essence).** Short bridge: the essential challenge
in zero-shot Text-to-SQL is the transfer difficulty identified in
Limitation 2. Because Alpha-SQL is a Technique Paper, this paragraph is
kept to a single transition sentence rather than carrying narrative
weight.

**Paragraph 4 (Challenges).** Absent as a separate paragraph. At ICML's
tight page budget, challenges are folded into the Solution Overview by
justifying each technical choice inline. A database-venue submission
would be expected to restore this paragraph.

**Paragraph 5 (Solution Overview) and Paragraph 6 (Contributions).**
Merged. The overview introduces MCTS as the search backbone, then
presents two technical points (LLM-as-Action-Model, self-supervised
reward function), each with a justification for non-triviality.
Contributions are communicated through the language ("we introduce the
following novel techniques"), not a separate numbered list.

### Methodology framing

Alpha-SQL's framing choice is worth studying. Rather than abstracting
MCTS as a generic search technique and then specialising to SQL, the
paper grounds MCTS in the Text-to-SQL domain from the first mention:
nodes correspond to partial SQL states, actions to SQL-construction
steps, reasoning to Chain-of-Thought between actions, reward to
execution self-consistency. A reviewer never has to translate "generic
MCTS" into "SQL-specific MCTS". Every MCTS element has its SQL meaning
beside it.

The LLM-as-Action-Model framing solves a real framing problem. MCTS
traditionally uses a policy network to generate actions and a value
function to evaluate them. Zero-shot Text-to-SQL cannot afford training
either one. The Alpha-SQL insight is to repurpose the off-the-shelf LLM
as both: the LLM proposes the next action (plus Chain-of-Thought
reasoning stored at the node), and a separate self-consistency check
(multiple sampled queries, execution comparison) serves as the reward.
Neither requires training.

### Figure design

Figure 1 illustrates the performance gap between Alpha-SQL and zero-
shot baselines on the BIRD benchmark. The design follows the
Performance Teaser paradigm from
[figure-designer](../skills/figure-designer/overview.md): a grouped bar
chart with Alpha-SQL highlighted in a saturated colour and baselines in
muted grey or pastel tones. Because the gap is large (roughly 69.7% vs
mid-50s for zero-shot baselines), a performance teaser is appropriate;
the figure does more work than a motivated-example-plus-failure-case
would here.

Figure 3 (Solution Overview) uses the System Architecture paradigm: the
MCTS framework as the central system, LLM-as-Action-Model and self-
supervised reward as interacting components, with arrows showing how
reasoning flows between nodes and how reward feedback propagates. Every
module name matches a methodology-section heading.

### Contribution phrasing

The contributions collapse into the methodology text at page-limit
conferences. Where an explicit list would normally appear, Alpha-SQL
embeds signals like "we propose", "we introduce the following novel
techniques", "this ensures", "this helps". A reviewer scanning for
contributions can still extract four clear ones: (1) fine-tuning-free
plug-and-play framework, (2) LLM-as-Action-Model, (3) self-supervised
reward function, (4) empirical validation at 69.7% BIRD execution
accuracy. The phrasing is specific, each contribution points at a
section, and nothing is padding.

## Key techniques used

- **Two limitations, not three**, covering the two natural categories of
  prior work (trained and zero-shot). Cleaner than forcing a third.
- **Explicit taxonomic positioning.** Reviewers see immediately which
  track the paper competes in.
- **Short Problem Essence paragraph** because this is a Technique Paper.
  Weight is saved for the Solution Overview.
- **Inline challenge justification** inside the Solution Overview,
  chosen because of ICML's page budget.
- **Domain-specific MCTS framing** from the first mention, rather than
  abstract MCTS followed by specialisation.
- **LLM repurposing** (as both policy and implicit value source via
  self-consistency) avoids training while preserving the MCTS structure.
- **Merged methodology and contributions paragraph** with strong
  signalling verbs ("we propose", "we introduce", "this ensures", "this
  helps").
- **Performance Teaser as Figure 1**, because the gap over baselines is
  large enough to justify leading with a result.

## Lessons for your paper

**Match the Introduction's Challenges paragraph to the venue.** At AI
conferences (ICML, NeurIPS, ICLR), Challenges can fold into the
Solution Overview. At database venues (SIGMOD, VLDB, ICDE), Challenges
typically need their own paragraph. Decide which venue you target
before you draft the Introduction, and structure accordingly. A Text-
to-SQL paper written for ICML and then ported to VLDB usually needs a
new Challenges paragraph added back in.

**Use two limitations when two categories cover the prior work.**
Forcing a third limitation to meet a "three is standard" heuristic
weakens the argument. If your field genuinely has two branches of prior
work (trained vs zero-shot, offline vs online, rule-based vs neural),
two limitations covering those two branches is clearer than three that
blur the categorisation.

**Ground abstract techniques in your domain from the first mention.**
MCTS is generic; MCTS for SQL is specific. When your paper borrows a
technique from elsewhere, translate every element of the technique into
your domain vocabulary immediately. Reviewers should never need to map
generic MCTS to SQL MCTS in their heads.

**When compute or data is the bottleneck, look for repurposing rather
than new training.** Alpha-SQL's insight is that an LLM can act as
action model and its sampled outputs can provide reward, without any
fine-tuning. When your paper targets a cost-constrained setting, ask
which existing components can serve unexpected roles.

**Performance Teaser as Figure 1 is acceptable when the gap is
genuinely large.** If your method has a small-percentage gain, a
Motivated Example showing a concrete failure case is more persuasive.
If the gap is substantial, a clean bar chart can lead the Introduction.

## Source

[archive/v1-source/1_Guide/06_Case_Studies/6.1_ICML_2025_Alpha-SQL写作剖析.md](/archive/v1-source/1_Guide/06_Case_Studies/6.1_ICML_2025_Alpha-SQL写作剖析.md)

---

[English] | [中文](../../zh/case-studies/alpha-sql.md)
