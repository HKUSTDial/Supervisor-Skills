---
name: rebuttal-guidance
description: >-
  Provides actionable peer-review rebuttal guidance (not full rebuttal prose)
  using conditional persuasion P(Z|X,Y): match reviewer mindset X, recommend
  strategy Y, optionally ground in manuscript evidence and similar successful
  historical (review, rebuttal) pairs. Use when the user pastes reviewer
  comments, asks for rebuttal help, rebuttal guidance, response to reviewers,
  how to reply to R1.W2, OpenReview rebuttal, or the reviewer ignored the rebuttal.
---

# Rebuttal Guidance

## Overview

This skill delivers **executable rebuttal guidance per concern**: structured plans,
evidence pointers, tone and strategy priorities. It does **not** produce
ready-to-paste rebuttal prose; the author writes the final text.

The core model is **conditional persuasion P(Z=1 | X, Y)**:

- **X**: reviewer mindset (behavior cluster inferred from review text)
- **Y**: rebuttal strategy vector (which tactics to emphasize)
- **Z**: success (score increase or paper accepted)

## When to use

- User pastes Weaknesses / Questions from ICLR, NeurIPS, ICML, EMNLP, etc.
- User asks how to respond to a specific reviewer comment.
- User wants a structured plan before writing rebuttal prose.
- User asks which tone or evidence strategy fits a harsh vs. open reviewer.
- User says "reviewer ignored my rebuttal" and wants to recalibrate.

## When NOT to use

- User wants full rebuttal text copied verbatim → output guidance first; warn
  against blind LLM paste.
- User asks to evaluate a research idea → use `idea-evaluator`.
- User asks for pre-submission paper review → use `pre-submission-reviewer`.
- No review text provided → ask for it first.

---

## Core procedure

### Step 1: Inventory concerns

Extract every numbered Weakness and Question from the pasted review. If the
user pasted only one reviewer's block, ask whether other reviewers exist.

Output a short table:

| ID | Type | One-line summary |
|----|------|-----------------|
| R1.W1 | W | ... |
| R1.Q1 | Q | ... |

### Step 2: Classify each concern

See: [references/concern-classification.md](references/concern-classification.md)

Tag each item as one of:
`misunderstanding | evidence_gap | novelty | baseline_fairness | scope_claim |
writing_clarity | theory | efficiency | other`

### Step 3: Match reviewer mindset (X)

See: [references/mindset-matching-heuristics.md](references/mindset-matching-heuristics.md)

Score the review on 5–7 behavior signals (openness, severity, constructiveness,
specificity, skepticism, harshness, actionability). Map scores to a cluster in
[references/mindset-library.md](references/mindset-library.md).

State: **matched cluster name**, confidence (high / medium / low), and the
specific phrases that triggered the match.

### Step 4: Strategy priorities for this mindset (Y)

From the matched cluster in [references/mindset-library.md](references/mindset-library.md), read:

- **Historical up-rate**: calibrate how likely a score increase is.
- **Rule-stat diffs** (success vs. failure %): boost tactics with positive diff.
- **Cohen's d effects**: highlight dimensions with d > 0.8 in success group.
- **Success / failure patterns**: concrete do's and don'ts from data.
- **Key strategy**: one-sentence summary for this cluster.

Cross-check dimensions in [references/strategy-dimensions.md](references/strategy-dimensions.md).

### Step 5: Per-concern guidance

For each concern, emit a guidance block (not final prose):

```
### R?.W?: [short title]
- **Concern type**: ...
- **Mindset-aware strategy**: ...
- **Recommended structure**: Acknowledge → Response → Evidence → Revision note
- **Clarify from paper?**: yes/no: where to look (section, table, appendix)
- **New experiment needed?**: yes/no: what exactly (no fabricated numbers)
- **Tone note**: ...
- **Template**: A / B / C: see references/response-templates.md
- **Avoid**: ...
```

Do **not** fabricate experimental numbers. Mark anything unverified as
`[TO VERIFY]`.

### Step 6: Integrity gate

Before finalizing, run through [references/checklist.md](references/checklist.md).

Key flags:
- Every W/Q has a guidance block.
- No fabricated numbers.
- Defensive phrases (e.g., "you misunderstood") flagged.
- Overpromise risk flagged for scope_claim and evidence_gap types.

### Step 7: Output format

Deliver a `## Rebuttal Guidance` section containing:

1. **Reviewer mindset summary**: cluster name, confidence, identifying phrases.
2. **Global strategy priorities**: 3–5 bullets from mindset data.
3. **Per-concern guidance**: Step 5 blocks for each W/Q.
4. **Checklist highlights**: pass/fail on key integrity items.

---

## Reference map

| Purpose | File |
|---------|------|
| Concern type → response priority | [concern-classification.md](references/concern-classification.md) |
| Reviewer signal → mindset cluster | [mindset-matching-heuristics.md](references/mindset-matching-heuristics.md) |
| Mindset clusters with stats & patterns | [mindset-library.md](references/mindset-library.md) |
| 10 strategy dimensions (Y) | [strategy-dimensions.md](references/strategy-dimensions.md) |
| Response templates A / B / C | [response-templates.md](references/response-templates.md) |
| Pre-submit integrity checklist | [checklist.md](references/checklist.md) |
