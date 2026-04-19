# Vibe Coding: mindset and techniques

## Table of contents

1. Core shift: from Coder to Commander
2. Mindset (心法): six principles
3. Technique 1: Plan Before Execute
4. Technique 2: Clear Requirements
5. Technique 3: Small Steps
6. Technique 4: Context Management
7. Technique 5: Error Handling
8. Technique 6: Git Discipline

## 1. Core shift: from Coder to Commander

What changes:

| Old role | New role |
|---|---|
| Memorise syntax rules | Describe requirements clearly |
| Hand-write code | Judge whether code is correct |
| Debug manually | Describe the problem and ask AI to fix |
| Read technical documentation | Know what to ask and what to look up |

What stays the same:

- The user must know what they want.
- The user must judge whether results are good.
- The user must have problem-solving intuition.

Without these, AI-assisted coding accelerates mistakes.

## 2. Mindset (心法): six principles

- **Do what AI cannot, delegate what AI can**.
- **Ask AI first**.
- **Purpose-driven**: every action in the development process
  serves a specific purpose.
- **Context is king**: context quality determines AI output
  quality. Garbage in, garbage out.
- **Occam's razor**: do not add unnecessary code; less irrelevant
  context keeps AI focused.
- **Subtractive MVP thinking**: minimum visible product. Validate
  the core assumption with the smallest effort, then expand.

## 3. Technique 1: Plan Before Execute

For Cursor, use Plan Mode (Shift+Tab toggle) before switching to
Agent Mode. For Claude Code, ask for a plan explicitly before
allowing implementation.

Value:

- Confirm AI understands the goal, the implementation, and the
  objective.
- Detect misinterpretation early rather than after hundreds of
  wasted lines.
- Let the user evaluate the planned approach before code runs.

When plan and goal diverge, the plan is wrong and the user
corrects before execution, not after.

## 4. Technique 2: Clear Requirements

Clear requirements mean less rework and fewer bugs.

For each code task, specify:

- What functionality is needed.
- Inputs and outputs (types, formats, sample values).
- Style or framework constraints (for example, use the official
  OpenAI SDK rather than LangChain, parallelise where possible).
- What the task does not include (to prevent scope creep).

Template:

```
I want to implement <module name>. It does <function description>.
Input: <format and structure>.
Output: <format and structure>.

Constraints:
- ...
- ...

Non-requirements:
- ...
```

## 5. Technique 3: Small Steps

Break the task into the smallest verifiable units. For each unit:

- Write a one-paragraph requirement.
- Have AI implement it.
- Run it.
- Verify the output.
- Commit.
- Move to the next unit.

Large monolithic asks (make the whole system) produce brittle
output. Small verified steps compound into working systems.

## 6. Technique 4: Context Management

Context is the set of files, documentation, and conversation
history the AI sees when producing its response.

Good context management:

- Load only relevant files into the conversation. Do not dump an
  entire repository.
- When switching topics, start a new conversation.
- Feed AI the exact error messages and stack traces when
  debugging.
- Avoid loading auto-generated files (compiled code, caches) into
  the context.

Bad context management:

- Leaving dozens of unrelated files attached.
- Switching topics without clearing context, so AI conflates
  unrelated requests.
- Pasting Markdown tables without the schema AI needs to
  interpret them.

## 7. Technique 5: Error Handling

When AI-generated code fails:

- Run the code first, capture the full error output, paste the
  error message back to AI with context ("this was the code, this
  was the error").
- Do not assume AI knows; explicit trumps implicit.
- If AI patches incorrectly, describe the actual symptom
  precisely.
- For persistent failures (three tries), step back and re-plan.
  Loop spirals are a signal that the plan is wrong.

## 8. Technique 6: Git Discipline

AI-assisted coding produces a higher rate of bad commits than
hand-written code. Git discipline catches this.

- Commit frequently (project memory
  `feedback_git_versioning`); each small verified unit is a
  commit.
- Run the code before committing.
- Use meaningful commit messages; do not accept AI's suggestion
  if it obscures the change.
- Never push AI-generated code without testing; "it compiles" is
  not a test.
- Rollback is cheap; use it when AI-generated changes break
  things. A bad AI commit rarely rewards being salvaged.
