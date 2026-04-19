# Logic and structure rules

## Table of contents

1. Logic First rule
2. Self-contained rule
3. Leading Text rule
4. Running Example rule
5. Paragraph discipline
6. Section-level consistency
7. Failure patterns

## 1. Logic First rule

Every sentence has a purpose. Every two consecutive sentences have
a connection. Every claim carries evidence. Every critique cites
a ground.

When reviewing a paragraph, ask for each sentence: what is this
sentence trying to do? If the answer is vague, the sentence is a
candidate for cutting or rewriting. When reviewing two consecutive
sentences, ask: how does sentence 2 advance the point made by
sentence 1? If the link is not apparent, a transitional phrase or
a restructure is needed.

Logic First is the highest-priority writing rule. A paper can
recover from many writing weaknesses if its logic is airtight;
strong prose cannot compensate for broken logic.

## 2. Self-contained rule

The paper should be readable without referencing external material
for basic understanding. A reader without access to prior work
should be able to follow the paper's contribution; external
citations are for context and credit, not for load-bearing
content.

Self-containment checks:

- Every abbreviation defined on first use.
- Every symbol defined on first use.
- Every cited method explained in one sentence before use.
- Figure captions readable without the body text.

## 3. Leading Text rule

Every framework section, every subsection, every paragraph should
begin with a leading sentence that says what the reader is about
to read. The leading text is the reader's navigation anchor.

Leading text does three things:

- States the goal of the upcoming content.
- Previews the structure (if the section or paragraph has
  internal structure).
- Connects to what came before.

A paper without leading texts reads as a succession of claims
without context. Reviewers sense this as disorganisation.

## 4. Running Example rule

The running example established in Introduction Paragraph 1 should
reappear:

- In the Methodology as a walkthrough of how the method handles
  it.
- In the Experiments as a case study or example in an analysis
  figure.
- In the Conclusion optionally, as a closing reference.

A running example that appears only in the Introduction signals
that the author did not structure the narrative around a single
concrete anchor; reviewers struggle to follow the paper's story.

## 5. Paragraph discipline

Each paragraph:

- Opens with a topic sentence that states the paragraph's point.
- Contains three to eight sentences; significantly more usually
  indicates the paragraph is trying to cover two topics.
- Closes with a sentence that either concludes the point or
  bridges to the next paragraph.
- Contains only one topic; do not mix unrelated points in one
  paragraph.

Common paragraph failures:

- No topic sentence; the point only emerges in the middle.
- Topic sentence buried; the reader must infer the point.
- Too long; the paragraph covers two topics that should be split.
- Too short; a two-sentence paragraph rarely earns its own line
  break, fold into a neighbour.

## 6. Section-level consistency

Beyond the paragraph level, sections are expected to follow the
framework laid out in the Introduction:

- Methodology sections mention the module names introduced in
  the Introduction.
- Experiments evaluate the claims made in the Contributions.
- Related Work is consistent with the Limitations cited in the
  Introduction.

Inconsistency between sections is among the most common review
findings. Check that every module name in the Introduction appears
verbatim as a subsection title in the Methodology. Check that
every contribution cited in the Introduction has a corresponding
experiment that validates it.

## 7. Failure patterns

| Pattern | Detection | Severity |
|---|---|---|
| Broken flowchart (Introduction) | One of the six paragraphs missing | CRITICAL |
| Orphan contribution | Contribution has no section | CRITICAL |
| Running example abandoned after Introduction | Search the Methodology and Experiments for the example; not found | MAJOR |
| Leading text missing | A section or subsection opens with a dense paragraph | MAJOR |
| Topic sentence absent | Random paragraph sampled; the point is not in the first sentence | MAJOR |
| Module name mismatch | Methodology subsection titles differ from Introduction module names | MAJOR |
| Related Work contradicts Limitations | Methods criticised in Introduction appear without critique in Related Work | MAJOR |
| Paragraph over 10 lines | Length check | MINOR |
| Paragraph under 2 sentences | Length check | MINOR |
