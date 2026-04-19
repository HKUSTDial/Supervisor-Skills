# Vibe Research Workflow

## Why this matters

In 2025, Andrej Karpathy's tweet introducing "Vibe Coding" triggered a
shift that has since extended across the entire research workflow. For
PhD students targeting top venues, AI assistance is not optional, but the
boundary between acceptable use (mechanical acceleration) and academic
misconduct (outsourced reasoning, fabricated citations) is not obvious.

Students who use AI without discipline accumulate three failure modes:
hidden factual errors in AI-generated prose, fabricated or misattributed
citations that make the paper unreviewable, and a drift where the student
no longer owns the research judgment. Each failure is more dangerous than
the last. A factual error can be corrected; a fabricated citation can
sink a paper at review; a research-judgment drift quietly hollows out the
student's own capability.

The Vibe Research Workflow skill operationalises the original curriculum's Vibe Research section
Boyan's guidance: AI handles mechanical tasks (implementation, figure
rendering, language polish) while the researcher retains full ownership
of research direction, problem framing, experimental design, and factual
accuracy. The goal is a two-to-five times productivity gain on routine
tasks without compromising integrity.

## The framework

### The three sub-flows

Vibe Research is made up of three complementary sub-flows.

- **Vibe Coding** (AI-assisted code). Covers the implementation phase:
  writing baselines, running experiments, building MVPs, debugging.
  Tools: Cursor (IDE-native), Claude Code (agentic CLI), Codex.
- **Vibe Figure** (AI-assisted figure production). Covers the figure-
  drafting phase after experiments complete: a four-step workflow from
  layout ideation to vectorisation.
- **Vibe Writing** (AI-assisted prose polish). Covers the writing phase:
  language polish, structure suggestions, grammar correction. Explicitly
  does not include drafting paper content from scratch, which remains
  the researcher's job.

### The six behavioural rules

Non-negotiable. These draw the hard line between acceptable use and
academic misconduct.

1. **AI is permitted as an auxiliary tool**, including literature search
   and organisation, code and debugging support, and language polish.
2. **Research ideas, problem framing, experimental design, technical
   paths, core conclusions, and novelty claims must be owned by the
   student or advisor**, fully understood. AI can suggest; the researcher
   decides.
3. **Every AI-generated or AI-assisted passage is verified by the
   student** against the actual research process, experimental results,
   and facts. No error, exaggeration, or inconsistency introduced
   because AI wrote it.
4. **No fabricated citations.** References come from the student's own
   reading and confirmation, accessible on DBLP, arXiv, or the venue's
   proceedings.
5. **No academic misconduct of any kind**, including fabricated data,
   experimental results, or plagiarism concealment.
6. **Venue or institutional AI-disclosure rules are honoured.** If the
   venue requires a statement about AI use, the student provides one.
   When in doubt, consult the advisor before submission.

### Vibe Coding: from Coder to Commander

The core shift: writing code becomes expressing requirements clearly and
judging whether the output is correct.

What changes:

| Before | Now |
|---|---|
| Memorise syntax | Describe requirements clearly |
| Write code by hand | Judge whether the output is correct |
| Debug line by line | Describe the error, let AI fix |
| Read documentation | Know when to ask and when to search |

What does not change: the researcher still needs to know what they want,
judge output quality, and have a troubleshooting method when problems
arise.

Six techniques operationalise this:

1. **Plan first, then execute.** Use the IDE's Plan Mode. Confirm the AI
   understood the goal before switching to execution mode. Avoids large-
   scale rework when the AI misread the intent.
2. **Clear requirements.** Clear requirements mean less rework and fewer
   errors. State the function, input, output, constraints, and preferred
   libraries. Example: "Implement module X with this structure, using
   Loguru for logging, supporting multi-threaded parallelism with a
   configurable parallel count."
3. **Small steps over large leaps.** Each AI interaction implements one
   minimum functional unit. Immediate code review and testing after each
   unit prevents unreviewed code from accumulating.
4. **Context is king.** "Garbage in, garbage out". When the AI forgets
   earlier constraints or hallucinates, add back the context or start a
   fresh chat session.
5. **Provide enough error context.** Not "my code is broken, fix it",
   but "here is the file, here is the command, here is the full
   traceback".
6. **Version control discipline.** Use git for every minimum functional
   unit. AI can break working code; version control restores it.

### Vibe Figure: the four-step workflow

1. **Step 1: Design discussion.** Tell the AI the paper's logic,
   propose several candidate figure layouts, discuss the trade-offs,
   pick one.
2. **Step 2: Sketch generation.** Convert the chosen layout into a
   prompt meeting venue standards (English text, 8K resolution,
   specified font). Send to a strong text-to-image model (Gemini, Nano
   Banana Pro).
3. **Step 3: Raster sketch.** The model produces a PNG sketch. If the
   prompt was good, quality is acceptable as a starting point.
4. **Step 4: Vectorise by hand.** Draft-quality rasters are not
   submission-ready. Use Figma, OmniGraffle, or PowerPoint to redraw the
   figure in vector format, matching the sketch but with cleaner
   typography and icons.

For Experimental Results figures specifically, the sketch stage is often
skipped; the data goes straight into Matplotlib via a reusable plotting
script.

### Vibe Writing: the red lines

Vibe Writing is the strictest sub-flow because the risks are highest:

- **Copying AI-generated paper content directly is forbidden.** The
  student must verify every sentence's factual accuracy and rewrite any
  passages that feel AI-voiced.
- **Citing references produced by AI without verification is
  forbidden.** Every reference must be checked on DBLP or arXiv.
- **AI provides assistance on writing ideas; the student writes the
  final prose.**

The acceptable pattern is: the student drafts the first version from
their own understanding, then asks AI for suggested rewrites of specific
sentences or paragraphs, then accepts or rejects each suggestion sentence
by sentence with full awareness of what changed.

### Tool selection

| Phase | Primary tool | Alternative | Why |
|---|---|---|---|
| Coding | Cursor | Claude Code, Codex | IDE-native agent with strong context handling |
| Figure sketching | Gemini web, Nano Banana Pro | ChatGPT with image tools | Strong text-to-image for draft figures |
| Figure vectorisation | Figma | OmniGraffle, PowerPoint | Clean SVG output, icon library |
| Experimental plotting | Matplotlib + Seaborn | TikZ, PGFPlots | Reproducibility, reusable script |
| Prose polish | Claude, ChatGPT | Grammarly | Sentence-level suggestions with style control |
| LaTeX | Overleaf | Local TeX distribution | Collaborative with grammar plugin |

## Named heuristics

- **Three sub-flows**: Vibe Coding, Vibe Figure, Vibe Writing.
- **Six behavioural rules**: AI as auxiliary, researcher owns judgment,
  verify everything, no fabricated citations, no misconduct, disclose
  when required.
- **AI can do, you do not do**: do not manually do what AI can do well
  (boilerplate, language polish), but do manually do what AI cannot do
  (frame the research).
- **Context is king**: clear requirements, fresh chat sessions when
  needed, explicit error traces.
- **Small steps over large leaps**: minimum functional unit, immediate
  review, git after each unit.
- **Red lines for writing**: no direct copy of AI-generated paper
  content, no AI-generated citations without verification.
- **Four-step figure workflow**: discuss, prompt, sketch, vectorise.

## Worked example

Consider a four-day block for a PhD student preparing a Text-to-SQL
submission. Four effective hours per day, four days total.

**Day 1 and Day 2 (Vibe Coding).** The student needs a baseline
implementation of a published method. Plan Mode first: describe the
method, the paper section, the expected input and output. AI proposes
an implementation outline. The student confirms the outline, then
switches to execution mode. The AI implements in small steps: first the
data loader, reviewed and tested; then the model forward pass, reviewed
and tested; then the evaluation loop, reviewed and tested. Each step is
committed to git with a clear message. By end of Day 2, the baseline
runs and reproduces the published numbers within a reasonable margin.

**Day 3 (Vibe Figure).** The student needs a Motivated Example figure
and three experimental-results figures. For the Motivated Example, they
describe the story to Claude: "Text-to-SQL, BIRD benchmark, show that
current methods miss a JOIN condition on this query." Claude proposes
three layout variants, the student picks the Running Example + Failure
Case variant. Claude generates a Gemini-style prompt; Gemini produces a
raster sketch. The student opens Figma, redraws the sketch in vector,
and exports PDF. For the three experimental-results figures, the
student writes a shared plotting script in Python with unified palette,
font, and line widths; all three figures regenerate from the script if
any data changes.

**Day 4 (Vibe Writing).** The student drafts the Methodology section
from their own understanding, referring to the
[tech-paper-template](../tech-paper-template/overview.md) outline. They
then ask Claude to review each paragraph for topic-sentence discipline
and transition flow. Claude suggests rewrites for several sentences;
the student accepts some, rejects others, rewrites the rest in their
own voice. The final draft goes through
[pre-submission-reviewer](../pre-submission-reviewer/overview.md) which
flags any remaining AI-voiced passages for a second cleanup.

At no point does AI write a full paragraph that enters the paper
without review. At no point is a citation used that the student has
not read. The productivity gain is real (a week of implementation
compressed into two days), and integrity is intact.

## Try it with the plugin

Install the plugin per the
[root README](../../../../README.md#quick-install) and invoke naturally.
The skill self-triggers on phrases like "how to use AI for research",
"Vibe Coding tips", "AI-assisted writing workflow", or "which AI tool
for this". It is also appropriate when starting a new AI-assisted work
block (a morning of coding, a figure day, a writing session). The
skill returns a workflow plan, per-phase tool recommendations, red-
line reminders for Vibe Writing, and an integrity checklist.

## Source

Adapted from:

- [archive/v1-source/1_Guide/05_Vibe_Research/5.1_Vibe_Research与Vibe_Coding入门.md](/archive/v1-source/1_Guide/05_Vibe_Research/5.1_Vibe_Research与Vibe_Coding入门.md)
- [archive/v1-source/1_Guide/05_Vibe_Research/5.2_李伯岩实战经验分享与会议纪要.md](/archive/v1-source/1_Guide/05_Vibe_Research/5.2_李伯岩实战经验分享与会议纪要.md)
- Plugin SKILL.md:
  [/plugins/phd-research/skills/vibe-research-workflow/SKILL.md](/plugins/phd-research/skills/vibe-research-workflow/SKILL.md)

---

[English] | [中文](../../../zh/skills/vibe-research-workflow/overview.md)
