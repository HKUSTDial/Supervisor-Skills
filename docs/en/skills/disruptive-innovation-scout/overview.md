# Disruptive Innovation Scout

## Why this matters

The five-dimension framework (Higher, Faster, Stronger, Cheaper, Broader)
teaches a student how to write a paper that gets accepted at a top venue,
because it runs faster along an axis the community already agrees is worth
running along. What it cannot teach is how to become the researcher whose
paper gets written into future textbooks. That kind of work defines a new
axis rather than running faster along an existing one.

Richard Hamming called this choosing important problems; others call it
paradigm shift. Incremental and disruptive are not opposites, they are
complements. A PhD student who never tries the disruptive register will
publish safely and forgettably. A student who only tries the disruptive
register will publish nothing. The scout helps a researcher already engaged
in incremental work find the disruptive reframing latent in it.

The scout is not a replacement for the [idea-evaluator](../idea-evaluator/overview.md).
The evaluator gives a fast yes-or-no paradigm signal; the scout turns a yes
signal into candidate reframings with risk-reward scores. A student who
used the evaluator and got "disruptive candidate" as the verdict should run
the scout next.

## The framework

Four principles, each corresponding to a distinct style of disruption. The
scout runs each principle as an independent scan and then consolidates the
candidate reframings.

### First Principles thinking

Do not start from what the field does now. Start from the physical or
mathematical essence of the problem itself. Most current solutions rest on
assumptions inherited from earlier technology eras; some of those
assumptions are no longer valid, but the community keeps using them because
changing is expensive.

Two working techniques operationalise this principle:

- **Assumption audit.** Name the three most widely-held assumptions in the
  subfield. State each as a one-sentence declarative. Ask: is this
  assumption still true given the last three years of technology shift? If
  an assumption is shakier than its community adoption suggests, propose
  the reframing "what if this assumption is false?" Example: traditional
  database query optimisation assumed data distribution and workload were
  static, so the query plan must be fully determined before execution.
  Dropping that assumption opened the Adaptive Query Processing research
  direction.
- **Return to purpose.** Ask "what is this task ultimately for?", not "how
  does the community currently do it?". Example: traditional data cleaning
  was a set of rule-based scripts that fix missing values, remove noise,
  and so on. The purpose of data cleaning is to help the downstream task,
  not to be a clean pipeline in isolation. Asking this purpose-first
  question yields Agent-driven Adaptive Data Cleaning as a new direction.

Good output from this scan is at most two candidate reframings, each with
a named assumption and a plausible research programme. More than two is
usually a signal that the student is brainstorming rather than filtering.

### Elephant-in-the-Room hunting

Every subfield has hard problems everyone knows about and nobody wants to
touch, usually because they are messy, too unglamorous for a clean
benchmark, or too hard to reduce into a publishable unit. These are the
elephants. Naming them is part of the intellectual work; solving them is
optional.

Two hunting techniques:

- **Real-world pain-point extraction.** Academic benchmarks are clean;
  practitioner pain is messy. Example: the academic Text-to-SQL community
  has long optimised single-table, well-schema'd accuracy. Industrial
  practitioners face databases with thousands of tables where even the DBA
  cannot recall which one to query. Formalising that as large-scale schema
  linking opens a genuinely valuable research line.
- **Corner-case cataloguing.** Where does the field's current best method
  actually fail? The single-agent LLM approach works for short tasks but
  breaks on long-horizon, multi-modal, cross-departmental workflows.
  Rather than patch the single-agent pattern with prompt engineering, the
  failure motivates multi-agent collaboration or SOP-driven agentic
  workflows as new paradigms.

### Technology Cycle Foresight

Disruptive innovation often rides a generational shift in hardware or
platform. When the substrate changes, the old architecture assumptions
stop holding, and entirely new systems become possible. A researcher who
treats the new substrate as "just faster hardware" misses the opportunity;
a researcher who rebuilds the architecture for the new substrate catches
it.

Two scouting techniques:

- **Hardware or platform shift adoption.** Do not ask "how do I port the
  old algorithm to the new hardware?". Ask "if storage is now persistent
  and byte-addressable (non-volatile memory), does the database still need
  a buffer pool at all? Does it still need traditional write-ahead
  logging?". That kind of question produces entirely new system
  architectures rather than optimised ports.
- **Unlimited-resource thought experiment.** If compute or storage suddenly
  became ten thousand times cheaper, how would the field's current
  solutions look? Deep learning took off because compute cost collapsed.
  If LLM tokens drop to near zero and context windows become effectively
  unlimited, how does the data-processing paradigm change?

### Hamming's Rule

Richard Hamming argued that every scientist should maintain a mental list
of ten to twenty most important problems in their field. The purpose is
not to solve them immediately. The purpose is to be ready: when a new
algorithm, dataset, or platform appears, the prepared mind instantly asks
"can this help with any of my top problems?".

- **Prepared mind.** Read adjacent fields with the list actively in memory.
  New transformer architecture appears; does it unlock any problem on the
  list? New dataset released; does it make any problem newly tractable?
- **Willingness to invest.** If a researcher only attacks problems they
  are already sure they can solve, they will never make a disruptive
  contribution. Reserve some fraction of time for problems that might fail
  but would transform the field if they succeed.

Most PhD students do not yet have a top-10 list. Part of the scout's work,
especially on first invocation, is to help build one: solicit 10-15
candidates, filter to 10, revisit in every major research decision.

## Named heuristics

- **First Principles thinking**: start from problem essence, not field
  convention.
- **Elephant in the Room**: name what everyone sees and nobody touches.
- **Technology Cycle Foresight**: watch substrate shifts (hardware,
  platform, LLM capability) and reframe rather than port.
- **Hamming's Rule**: maintain a personal top-10 problem list, feed it with
  everything read.
- **Spectrum positioning**: pure incremental (0-2 signals), incremental
  with seeds (3-4), disruptive candidate (5+), paradigm-shift contender
  (7+).
- **Research programme, not single paper**: a disruptive reframing should
  be large enough to support a multi-paper research line. A reframing that
  produces only one paper is probably incremental work rebranded.
- **Portfolio caution**: a student with no prior incremental papers is
  usually better served continuing the incremental project and banking the
  disruptive reframing for later. Credibility to pursue a landmark project
  is usually earned after one or two incremental successes.

## Worked example

Consider the Transformer paper (Vaswani et al. 2017, "Attention Is All You
Need") through the four principles.

First Principles: the dominant assumption in 2017 sequence modelling was
that sequential dependencies required recurrence (RNN, LSTM) or
convolution. The Transformer authors asked whether the actual mathematical
purpose of capturing long-range dependencies required recurrent structure
at all, or whether self-attention alone could do it. The assumption turned
out to be false, and attention-only became feasible. The First Principles
move was the heart of the paper.

Elephant: everyone knew RNNs could not train efficiently on long sequences
because of sequential dependency. Most of the community patched this with
tricks (gradient clipping, better gating) rather than removing the
dependency entirely. The Transformer authors treated the dependency as
the elephant and removed it rather than patching it.

Technology Cycle: GPU parallelism had advanced to the point where massive-
batch attention computation became cheap. An architecture that fully
exploited parallelism, rather than fighting against the recurrent
bottleneck, became practical at exactly that moment.

Hamming's Rule: machine translation quality had been the field's top
problem for years. The Transformer addressed it and in the process
redefined almost every other NLP problem.

The scout skill, applied to a researcher in 2016 working on RNN-based
machine translation, would have flagged First Principles (is sequentiality
really necessary?) and Technology Cycle (GPU parallelism is the dominant
compute axis now) as the two strongest reframings. Whether the researcher
would have followed the reframing or not depends on portfolio timing, risk
tolerance, and advisor backing, which is exactly why the skill surfaces
these as candidates rather than prescribing action.

## Try it with the plugin

Install the plugin per the
[root README](../../../../README.md#quick-install) and invoke naturally.
The skill self-triggers on "find a disruptive angle", "what is the
paradigm shift here", "break the assumption", "go bolder". It is also
recommended automatically when [idea-evaluator](../idea-evaluator/overview.md)'s
paradigm-shift probe scores two or more yes answers. Provide the current
research context (area, active project, key assumptions, recent technology
shifts noticed) and the skill returns candidate reframings with risk-reward
assessments and a single recommendation.

## Source

Adapted from:

- [archive/v1-source/1_Guide/02_Idea_Generation/2.3_进阶_如何做颠覆式创新.md](/archive/v1-source/1_Guide/02_Idea_Generation/2.3_进阶_如何做颠覆式创新.md)
- Plugin SKILL.md:
  [/plugins/phd-research/skills/disruptive-innovation-scout/SKILL.md](/plugins/phd-research/skills/disruptive-innovation-scout/SKILL.md)
- Plugin reference:
  [/plugins/phd-research/skills/disruptive-innovation-scout/references/first-principles-thinking.md](/plugins/phd-research/skills/disruptive-innovation-scout/references/first-principles-thinking.md)

---

[English] | [中文](../../../zh/skills/disruptive-innovation-scout/overview.md)
