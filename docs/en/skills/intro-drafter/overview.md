# Intro Drafter

## Why this matters

The Introduction is the first page and a half a reviewer reads, and the
decision of whether to keep reading is made there. If the six-paragraph
logical chain is broken, the reviewer scores down even if the later
sections are strong. The Introduction is also the part of the paper that
takes the longest to debug: a weak methodology section can often be
rescued by rewriting the content, but a weak Introduction requires
rethinking the story.

Most PhD-student Introductions fail for one of three reasons: paragraphs
are missing or out of order, limitations do not connect to challenges, or
contributions do not map one-to-one to methodology modules. Each of these
failures is structural rather than prose-level, which means they cannot be
fixed by polishing. They must be fixed by rebuilding the skeleton.

The Intro Drafter skill takes a small set of structured inputs (area,
limitations, hard constraints, key idea, challenges, solution overview)
and produces a six-paragraph outline with an explicit purpose, writing
points, and severity-tagged gaps for every paragraph. It enforces the
alignment rules that separate a Nice Story from a disjointed list of
claims. The output is an outline, not prose. The student writes the prose
with the outline in front of them.

## The framework

### The six-paragraph flowchart

The Introduction is the compressed version of the entire paper: the
research object, why the problem matters, why existing work falls short,
what the paper contributes, and how the contribution maps to section
numbers, all in one and a half to two pages. Six paragraphs in strict
order carry that argument.

![Introduction flowchart](/assets/images/intro_flowchart.png)

Figure: the six-paragraph Introduction flowchart: Background and Running
Example, Existing Limitations, Problem Essence and Goal, Key Challenges,
Solution Overview, Contributions.

The six paragraphs, with their canonical purpose:

| # | Paragraph | Core purpose |
|---|---|---|
| 1 | Background and Motivation | Introduce the research object via a specific running example; ground the paper in a real application |
| 2 | Limitations of existing work | At most three, each framed as "prior work X does not handle Y" |
| 3 | Problem essence and Our Goal | Make the hard constraints (scale, dynamism, heterogeneity, end-to-end cost) explicit; derive the Goal or Problem Formulation |
| 4 | Key Challenges | At most three, each explaining why a naive extension of prior work fails |
| 5 | Solution Overview | Each module addresses one challenge; one-to-one mapping with Paragraph 4 |
| 6 | Contributions | Three or four numbered bullets, each mapped to a section reference |

Every arrow must hold. If any arrow breaks, the Introduction reads as a
list of disjointed claims rather than a single argument. A reviewer who
has read fifty submissions in a batch will notice a broken arrow within
the first read-through.

### Paper-type positioning

Before drafting, the skill positions the paper into one of two narrative
axes:

- **Technique Paper** (new method solving an existing problem). The Key
  Idea or mechanism carries the narrative. The Goal gets one sentence in
  passing. Paragraph 3 is a short bridge rather than a load-bearing
  paragraph. Alpha-SQL at ICML 2025 is the canonical example; see
  [case-studies/alpha-sql](../../case-studies/alpha-sql.md).
- **New Problem or Setting Paper** (new problem formulation). Our Goal or
  Problem Formulation is the contribution. The Key Idea supports "why
  this definition is reasonable and feasible". Paragraph 3 is load-
  bearing. LEAD at VLDB 2026 is the canonical example; see
  [case-studies/lead](../../case-studies/lead.md).

Positioning changes where weight lands in the outline and how
Contributions are phrased. Technique-paper contributions emphasise the
mechanism and its evidence; new-problem-paper contributions emphasise the
formulation and its implications.

A paper that mixes the two positions (load-bearing Paragraph 3 with
Technique-Paper Contributions, or vice versa) reads as muddled. The
positioning decision should happen once, at the outline stage, and then
propagate through every paragraph.

### Running-example discipline

A running example is the paper's anchor. It appears in Paragraph 1 as a
concrete failure case or side-by-side comparison, reappears in the
methodology as a walk-through of the approach, and reappears in the
experiments as a case study. Reviewers reading only the figures should
still understand the paper's story.

Design principles: real and specific (from real data or a real scenario,
not invented), simple but complete (enough complexity to show why the
problem is hard, not so much that the reader drowns), and recurring
throughout the paper. An abstract statement like "LLMs hallucinate on
complex queries" is weak; a specific failure case, a natural-language
query that leads to an SQL missing a critical JOIN and therefore
thousands of duplicate records, is strong.

A running example is not decoration. It is a load-bearing narrative
device. Abandoning it after Paragraph 1 breaks the through-line of the
paper and leaves the methodology floating disconnected from motivation.

### Contribution alignment

Every contribution bullet must satisfy three checks:

1. It maps to a challenge in Paragraph 4, a module in Paragraph 5, or a
   specific experiment result.
2. It is specific, not vague ("comprehensive evaluation" on its own is
   not a contribution).
3. It cites the section number that delivers it.

Failure modes are easy to spot: "we propose a novel framework" is too
generic for any top venue; "we show extensive experiments" does not
ground in a result; a fourth contribution that does not map to anything
is padding. Reviewers have seen all of these thousands of times.

### Flowchart consistency

Five cross-paragraph links must hold:

- Paragraph 1's running example is referenced in Paragraph 5 or a case
  study forecast.
- Paragraph 2's limitations motivate Paragraph 4's challenges.
- Paragraph 3's goal aligns with Paragraph 6's contribution 1.
- Paragraph 4's challenges map one-to-one with Paragraph 5's modules.
- Paragraph 5's modules appear in Paragraph 6's contributions 2 or 3.

A break in any link is a CRITICAL gap. The skill enforces these as
inspection-level integrity checks, meaning they can be verified from the
outline itself without requiring the user to attest anything.

The five links together form the Introduction's through-line: a reader
who follows the links from Paragraph 1 to Paragraph 6 arrives at a
complete, self-consistent argument for why the paper exists and what it
delivers. A reader who finds any link broken ends up with a list of
loosely-related claims rather than an argument, and the paper's "Nice
Story" score drops sharply.

## Named heuristics

- **Six-paragraph flowchart**: Background and Running Example, Limitations,
  Goal, Challenges, Solution Overview, Contributions, always in this order.
- **At most three limitations, at most three challenges**: exceed this and
  the Introduction feels cluttered rather than focused.
- **Technique Paper vs New Problem/Setting Paper**: positioning decides
  Paragraph 3's weight.
- **Running example throughout**: introduce once in Paragraph 1, reappear
  in methodology and experiments; do not abandon after Section 1.
- **Contributions map to sections**: every contribution cites the section
  that delivers it; vague contributions are rejected.
- **Challenge-module one-to-one**: each methodology module addresses
  exactly one challenge.
- **Severity taxonomy**: CRITICAL (chain broken), MAJOR (reviewers flag in
  round one), MINOR (polish).

## Worked example

Consider Alpha-SQL (ICML 2025), whose Introduction was analysed in
[case-studies/alpha-sql](../../case-studies/alpha-sql.md). The skill's
outline for this paper follows directly from the source analysis.

**Paragraph 1 (Background).** Text-to-SQL converts natural-language
queries into SQL, democratising database access for lay and expert users.
The explosion of LLMs accelerated the field. The running example is a
Text-to-SQL query on the BIRD benchmark where the baseline LLM generates a
query missing a critical JOIN condition.

**Paragraph 2 (Limitations).** Two limitations, not three. Trained methods
(pre-training or fine-tuning on task-specific data) require expensive
labelled data and repeated fine-tuning whenever a new base model appears.
Zero-shot methods avoid training but struggle to transfer the LLM's
general knowledge to SQL generation without task-specific supervision.

**Paragraph 3 (Problem essence and Goal).** Short bridge, because this is
a Technique Paper. The essential challenge in zero-shot Text-to-SQL is
the difficulty of transferring and generalising LLM knowledge to a
specific, structured task without training. The implicit goal: achieve
competitive zero-shot performance with off-the-shelf open-source LLMs.

**Paragraph 4 (Challenges).** Alpha-SQL skipped this paragraph explicitly,
justifying non-triviality inside the methodology instead. This is
acceptable at AI venues with tight page limits, though at SIGMOD or VLDB
a separate Challenges paragraph is expected.

**Paragraph 5 (Solution Overview).** Alpha-SQL uses MCTS (Monte Carlo
Tree Search) as the search backbone. First technical point: LLM-as-
Action-Model, invoking the LLM to generate Chain-of-Thought reasoning
after each search action, with reasoning stored at each node for context
continuity. Second technical point: a self-supervised reward function
that computes a self-consistency score across multiple sampled queries
per reasoning path, refining the exploration without requiring labelled
SQL.

**Paragraph 6 (Contributions).** Alpha-SQL folded contributions into the
methodology paragraph rather than listing them separately, again a page-
constrained choice. An explicit list would read: (1) fine-tuning-free,
plug-and-play Text-to-SQL framework; (2) LLM-as-Action-Model within an
MCTS search; (3) self-supervised reward function based on execution
self-consistency; (4) 69.7% BIRD development-set accuracy with open-
source LLMs, significantly outperforming existing zero-shot baselines.

The skill would flag this outline's one gap: Paragraph 4 is absent, so
the one-to-one challenge-module mapping cannot be verified by the reader.
At a tighter AI venue like ICML this is acceptable; at a database venue
it would be CRITICAL.

## Try it with the plugin

Install the plugin per the
[root README](../../../../README.md#quick-install) and invoke naturally.
The skill self-triggers on phrases like "draft the Introduction",
"outline the Introduction", "intro logic needs clarifying", or "help
structure the paper story". Provide the inputs it needs (research area,
limitations, hard constraints, key idea, challenges, solution overview)
and the skill returns the outline plus flowchart-consistency report.

The natural upstream skill is
[tech-paper-template](../tech-paper-template/overview.md): it produces the
full logical skeleton (thinking-template table plus self-consistency
checks), and the intro drafter converts that skeleton into the six-
paragraph outline. The natural downstream skill is
[figure-designer](../figure-designer/overview.md): once the outline is
locked, the motivated-example figure should illustrate the running
example from Paragraph 1.

## Source

Adapted from:

- [archive/v1-source/1_Guide/03_Paper_Writing/3.1_完成一篇科研论文你需要做几件事情.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.1_完成一篇科研论文你需要做几件事情.md)
- [archive/v1-source/1_Guide/03_Paper_Writing/3.2_Introduction写作的思考模型.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.2_Introduction写作的思考模型.md)
- Plugin SKILL.md:
  [/plugins/phd-research/skills/intro-drafter/SKILL.md](/plugins/phd-research/skills/intro-drafter/SKILL.md)
- Plugin reference:
  [/plugins/phd-research/skills/intro-drafter/references/flowchart.md](/plugins/phd-research/skills/intro-drafter/references/flowchart.md)

---

[English] | [中文](../../../zh/skills/intro-drafter/overview.md)
