# Elephant-in-the-Room hunting

## Table of contents

1. Core idea
2. Technique A: real-world pain-point extraction
3. Technique B: corner-case cataloguing
4. Worked example: large-scale schema linking
5. Worked example: multi-agent collaboration for complex tasks
6. What to ignore

## 1. Core idea

Every research community has problems it knows are important but
systematically avoids. Sometimes the problems are too hard for the
current toolset. Sometimes they do not fit the publication conventions.
Sometimes everyone assumes someone else will eventually solve them. If
a researcher can formalise one of these elephants into a tractable
academic problem, the reframing often becomes a new subfield.

The hunting technique is to look outside the academic-benchmark bubble
and inside the corner cases where current methods fail silently.

## 2. Technique A: real-world pain-point extraction

### Procedure

1. Identify three practitioners (industry engineers, deployed-system
   operators, or domain experts) who use the field's outputs in
   production.
2. Ask them: what is the single biggest pain-point they hit every
   week that the academic literature does not address?
3. For each pain-point, ask whether it is a research problem or an
   engineering detail.
4. For research-grade pain-points, ask: can this be formalised as a
   benchmark, a new problem setting, or a measurable task?

### Signals a pain-point is research-grade

- Multiple practitioners independently raise it.
- Current academic work implicitly assumes the problem does not
  exist.
- A rigorous formalisation would require new evaluation metrics, not
  just a new dataset in an existing format.
- The pain-point has been stable for at least two years; it is not a
  passing artefact of one tool version.

## 3. Technique B: corner-case cataloguing

### Procedure

1. Run the field's current best method on inputs drawn from the long
   tail of real-world data.
2. Catalogue the failure modes: classify each failure by root cause.
3. Identify failure modes that are common, systematic, and not
   addressed in the literature.
4. For each, ask: is this a Prompt-Engineering patch problem, or a
   fundamental limitation of the current paradigm?
5. For fundamental limitations, propose a reframing that addresses
   the root cause.

### Signals a corner case is an elephant

- Frequent: appears in at least 10 percent of real-world inputs.
- Systematic: the same class of input consistently fails.
- Unaddressed: searching the literature surfaces no direct work on
  this failure mode.
- Root-level: quick fixes do not stick; each patch exposes the next
  layer of the same failure.

## 4. Worked example: large-scale schema linking

- **Academic benchmark focus**: Text-to-SQL evaluation on single-
  table or small-schema problems with clean column names.
- **Practitioner pain-point**: real databases have thousands of
  tables with inconsistent or cryptic naming; even DBAs do not know
  which tables to use for a given question.
- **Formalisation**: large-scale schema linking or schema retrieval
  as a first-class research problem, with its own benchmarks and
  methods.
- **Impact**: an entire subfield of retrieval-augmented Text-to-SQL
  opens up, previously invisible under the clean-schema assumption.

## 5. Worked example: multi-agent collaboration for complex tasks

- **Academic focus**: single-agent LLMs judged on short, well-bounded
  tasks.
- **Practitioner pain-point**: complex real business workflows need
  coordination across specialist roles; single agents spiral into
  long chains, hallucinations, or loops.
- **Corner-case analysis**: failure is not random; it correlates with
  tasks requiring sustained state, cross-function expertise, or
  rollback recovery.
- **Formalisation**: multi-agent collaboration frameworks or Standard
  Operating Procedure driven agent workflows, each with their own
  evaluation protocols.
- **Impact**: a new class of papers around agent orchestration rather
  than agent intelligence.

## 6. What to ignore

- **Engineering pain-points**: "my deployment tool is slow" is
  valuable to the practitioner but is not research-grade.
- **One-off failures**: a single viral bug is not an elephant.
- **Already-formalised problems**: if the literature already has a
  subfield for this, the elephant has been captured. Move on.
- **Pain-points that are solvable by the next model release**: if
  scaling alone is expected to solve it, the reframing is premature.
- **Elephants outside the user's reach**: some elephants require
  institutional infrastructure (industry partnerships, proprietary
  data) a PhD student cannot access alone. Record on the Hamming's
  list and defer.
