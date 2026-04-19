# Contribution-paragraph patterns

## Table of contents

1. Canonical structure
2. Strong contribution phrasing
3. Weak contribution phrasing
4. Anti-patterns
5. Section-number mapping
6. Pre-submission contribution audit

## 1. Canonical structure

A typical Introduction Paragraph 6 contains three or four numbered
contributions:

- **C1**: Problem formulation or setting (only for New Problem/Setting
  Papers) or a system or framework design (for Technique Papers).
- **C2**: One or two key technical contributions. These are the
  specific algorithms, data structures, or theoretical results the
  paper introduces.
- **C3**: Empirical evaluation with specific highlights.
- **C4** (optional): A secondary contribution such as an open-source
  release, a specialised model, or a cross-domain transfer result.

Each contribution should be:

- One to two sentences long.
- Specific enough that removing it changes the paper's claim.
- Mapped to a section number or set of section numbers.

## 2. Strong contribution phrasing

Strong contributions name the specific mechanism or result, cite a
section, and are defensible against a reviewer who asks "where in
the paper do you deliver this?".

Examples:

- "We propose `<framework name>`, the first system to do X under
  constraint Y, described in Section 3."
- "We introduce `<algorithm name>`, which reduces Z from O(n^2) to
  O(n log n), with proofs in Section 4."
- "We evaluate on `<benchmark>` against 12 baselines and show <gain>
  point gains on <metric>, with fine-grained analysis in Section 5."
- "We release `<dataset name>`, the first dataset to contain
  <property>, available at <url>. See Section 6."

## 3. Weak contribution phrasing

Weak contributions are vague, unfalsifiable, or are expected work
that should not count as a contribution.

Examples of weak phrasing to avoid:

- "Extensive experiments demonstrate the effectiveness of our
  method." (Expected; not a contribution.)
- "We provide a comprehensive analysis." (Vague; describes every
  paper ever written.)
- "Our approach is state-of-the-art." (Claim, not contribution.)
- "We improve on prior work." (By how much, on what?)
- "We propose a new method." (Which? What does it do?)

## 4. Anti-patterns

- **Padded contribution count**: using four contributions when the
  paper only has three. The last slot is a vague phrase. Cut it.
- **Overlapping contributions**: contribution 2 and contribution 3
  describe the same mechanism from different angles. Merge them.
- **Contribution-section mismatch**: contribution cites Section 5 but
  Section 5 does not deliver it. Reviewers will quote this in major
  revisions.
- **Promise-and-forget**: contribution promises a specific result
  (say, "10x speedup") that the experiments section does not
  support.
- **Retrofit**: contributions written after the experiments succeeded
  that cherry-pick only what worked. Discipline: write contributions
  before running experiments.
- **Marketing-style inflation**: "revolutionary", "paradigm-shifting",
  "breakthrough" as adjectives. Cut these; let the evidence speak.

## 5. Section-number mapping

Every contribution references at least one section. Typical mapping:

- C1 (problem formulation or framework design) -> Section 2 or 3.
- C2 (key technical contribution) -> Section 3 or 4.
- C3 (empirical evaluation) -> Section 5.
- C4 (optional: dataset, release, cross-domain transfer) -> Section 6
  or appendix.

The mapping is explicit in the Introduction, for example
"(Section 3.2)" or "(Sections 4-5)". If a contribution does not map
to a section, either the section is missing or the contribution is
overreach; fix accordingly.

## 6. Pre-submission contribution audit

Before submitting, run this quick audit on the Contributions
paragraph.

- [ ] Contribution count is 3 or 4.
- [ ] Each contribution fits one to two sentences.
- [ ] Each contribution names a specific mechanism, result, or
  artefact.
- [ ] Each contribution cites a section.
- [ ] No contribution uses only vague phrases.
- [ ] Every challenge from Paragraph 4 is addressed by a
  contribution.
- [ ] Every claim in a contribution is delivered by the cited
  section.
- [ ] No contribution overclaims beyond what the paper's experiments
  show.

Failing any item is a MAJOR gap. Missing section-mapping for even
one contribution is CRITICAL.
