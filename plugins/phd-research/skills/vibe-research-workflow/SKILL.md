---
name: vibe-research-workflow
description: >-
  Guides AI-assisted research across three sub-flows, Vibe Coding,
  Vibe Figure, and Vibe Writing, with behavioural rules that keep the
  user in charge of academic judgment while delegating mechanical
  work to AI. Recommends the right tool (Cursor, Claude Code, Codex,
  Figma, Gemini) for the current stage. Use when the user asks 'how
  to use AI for research', 'Vibe Coding tips', 'AI-assisted writing
  workflow', 'which AI tool for this', or starts an AI-assisted work
  session.
license: CC-BY-4.0
---

# Vibe Research Workflow

## Overview

Vibe Research is the modern research workflow where large language
models and AI coding tools handle mechanical tasks (implementation,
figure rendering, language polish) while the researcher retains
full ownership of research direction, problem framing, experimental
design, and factual accuracy. The goal is a two-to-five times
productivity gain on routine tasks without compromising academic
integrity.

The skill has three sub-flows: **Vibe Coding** (AI-assisted code),
**Vibe Figure** (AI-assisted figure production), **Vibe Writing**
(AI-assisted prose polish). Each is governed by six behavioural
rules that draw a hard line between acceptable use (mechanical
acceleration, auxiliary suggestions, style correction) and
academic misconduct (fabricated citations, outsourced scientific
judgment, hidden AI authorship).

This skill is a meta-skill that orchestrates tool selection, flow
design, and integrity enforcement across a research session. It
consolidates the the curriculum's Vibe Research section into a
single invocable procedure.

## When to use this skill

- Starting a new AI-assisted work block (a morning of coding, a
  figure day, a writing session).
- The user asks 'how to use AI for research', 'Vibe Coding tips',
  'AI-assisted writing workflow', 'which AI tool for this'.
- The user is choosing between Cursor, Claude Code, Codex, Figma,
  Gemini, or other tools.
- The user wants a workflow plan for a multi-day project
  involving AI.
- The user suspects AI output has drifted into unacceptable
  territory (fabricated citations, outsourced reasoning).

## When NOT to use this skill

- The user wants AI to generate the paper directly. Reject
  politely; the integrity rules forbid it. Redirect to
  `intro-drafter`, `tech-paper-template`, or
  `pre-submission-reviewer` depending on intent.
- The user wants a code implementation done. This skill guides
  the process; it does not replace the implementation itself.
- The user wants to evaluate research direction. Use
  `idea-evaluator` or `disruptive-innovation-scout`.

## Core procedure

### Step 1: Phase classification

Decide which phase the user is in: coding, figure, writing, or
mixed.

### Step 2: Behavioural rules recap

See: references/behavior-guidelines.md for the full six-rule set.

State the six rules succinctly at the start of the session:

1. AI-assisted work is permitted for literature search and
   organisation, code and debugging support, language and
   expression polish.
2. Research ideas, problems, designs, technical paths,
   experimental plans, core conclusions, and novelty must be the
   user's own and fully understood.
3. Every AI-generated or AI-assisted passage is verified by the
   user against the actual research process, experimental
   results, and facts.
4. No fabricated citations; references come from the user's own
   reading and confirmation.
5. No academic misconduct, including fabricated data,
   experimental results, or plagiarism concealment.
6. Venue or school AI-disclosure requirements are honoured.

These rules are non-negotiable and enforced in the integrity
gate.

### Step 3: Phase-specific procedure

For Vibe Coding, see: references/vibe-coding.md.

For Vibe Figure, see: references/vibe-figure.md.

For Vibe Writing, see: references/vibe-writing.md.

Each phase has its own core techniques (Plan Mode, Small Steps,
Clear Requirements for coding; four-step figure workflow; red-line
rules for writing).

### Step 4: Tool selection

See: references/tool-selection.md for the tool matrix.

Match tool to phase:

- Coding: Cursor (IDE-native) or Claude Code (agentic CLI) or
  Codex.
- Figure: PowerPoint plus Figma for static figures; Matplotlib
  plus Seaborn for experimental results; Gemini for first-draft
  sketches.
- Writing: Claude or ChatGPT for language polish; Grammarly for
  grammar; Overleaf for LaTeX.

### Step 5: Integrity gate

Before closing the session, run the checks in the Integrity gate
section below.

### Step 6: Output

Emit the workflow plan in the Output format below.

## 1. Phase
- Primary phase: <coding or figure or writing or mixed>
- Secondary phases: <list>

## 2. Behavioural rules recap
- Rule 1-6 (see references/behavior-guidelines.md): acknowledged

## 3. Workflow plan
| Time block | Phase | Activity | Tool | User check |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## 4. Tool recommendations
| Phase | Primary tool | Alternative | Reason |
|---|---|---|---|
| Coding | ... | ... | ... |
| Figure | ... | ... | ... |
| Writing | ... | ... | ... |

## 5. Red-line reminders
- ... (from references/vibe-writing.md)

## 6. Integrity gate plan
- Verification points: ...
- AI-disclosure requirements for the target venue: ...
```
