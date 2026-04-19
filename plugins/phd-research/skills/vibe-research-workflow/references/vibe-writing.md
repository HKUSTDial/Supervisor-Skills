# Vibe Writing: red-line rules and recommended flow

## Table of contents

1. The resolved contradiction
2. Red-line rules
3. Recommended flow
4. What AI does well
5. What AI does badly
6. Integration with pre-submission-reviewer

## 1. The resolved contradiction

The project's v1 content contains a surface contradiction: section
3.5 strictly forbids AI-generated content; section 5.1 embraces
Vibe Writing. The v2 resolution is:

- AI-assisted writing is permitted for mechanical acceleration
  (grammar, phrasing, structure suggestions).
- AI-generated drafts are not acceptable as final submitted text
  unless verified sentence by sentence by the user.
- The mechanical writing rules in section 3.5 (no em-dashes, no
  banned AI-tone vocabulary, no Chinglish) are enforced by the
  `pre-submission-reviewer` skill.
- The behavioural rules in section 5.1 govern the process.

In practical terms: write first in the user's own words; polish
with AI; verify after polish; scan for banned patterns before
submitting.

## 2. Red-line rules

Do not:

- Copy AI-generated paragraphs verbatim into the paper. Rewrite
  in the user's own words.
- Let AI fabricate or pre-fill citations. Every reference is the
  user's own confirmed read.
- Send a partial prompt and accept whatever AI returns; context
  must include the paper's method, problem, background, and
  relevant experimental data.
- Use AI to hide plagiarism or to paraphrase another group's
  work.
- Submit AI-assisted prose to a venue that forbids AI-assisted
  content without disclosure.

Violations of any red-line rule are academic misconduct. See
`references/behavior-guidelines.md` for the full context.

## 3. Recommended flow

### Step A: write the core claim and logic in the user's own words

- Produce the paragraph skeleton: topic sentence, evidence
  sentences, closing sentence.
- Do this first; do not outsource it.
- The skeleton encodes the user's thinking, which is the
  contribution.

### Step B: polish with AI (correct-by-construction)

- Paste the user's paragraph to AI with an explicit polish
  prompt that inlines the banned-vocabulary and punctuation
  rules. This prevents drift at the polish step rather than
  relying on a downstream reviewer to catch violations. Template:

```
Polish the language in the paragraph below. Hard rules:

1. Preserve every technical claim exactly. Do not add content,
   do not remove content, do not add citations.
2. Do not use any of these banned words or phrases: innovative,
   pioneering, revolutionary paradigm, transformative framework,
   superior, surpass, excel, remarkable, unprecedented, achieves
   SOTA, breakthrough performance, general-purpose, is capable
   of, notably, yet, yielding, at its essence, encompass,
   differentiate, reveal, underscore, pave the way for, highlight
   the potential of, profound challenges, stems from, rigid,
   impede.
3. Do not use em-dashes as sentence connectors or parenthetical
   breaks. Use commas, colons, or periods instead.
4. Use logical quotation punctuation: punctuation goes inside
   quotation marks only if it is part of the quoted material.
5. Prefer short sentences, active voice, and concrete technical
   verbs (propose, introduce, design, show, demonstrate, report,
   observe).
6. Keep the paragraph length roughly equal to the input.

Paragraph to polish:
<paste paragraph here>
```

- AI returns a polished version that is already style-compliant
  at submission time, not merely grammatical.
- The user still compares word by word in Step C to catch any
  content drift, but the banned-vocabulary and em-dash checks
  in Step D should now return empty sets in the common case.

### Step C: verify sentence by sentence

- For each sentence in the polished version, ask: does this match
  the user's intended claim?
- Replace any drift with the user's phrasing.
- Flag any hallucinated content and remove.

### Step D: scan for banned patterns (backstop)

Step B's inlined rules prevent most violations at the polish step.
Step D is the backstop for anything that slipped through.

- Run the banned-vocabulary scan (see
  `pre-submission-reviewer`'s `references/forbidden-patterns.md`
  for the canonical list and severity heuristics).
- Remove any AI-tone word that survived Step B.
- Remove any em-dash used as a sentence connector; replace with
  comma, colon, or period.
- Verify punctuation follows logical (not American) quotation
  conventions.

If Step D finds significant violations, the Step B polish prompt
template was under-specified; update the prompt rather than
accepting repeated Step D cleanup.

### Step E: final integrity check

- Read the full paragraph aloud. Does it sound like the user?
- If the voice has drifted, rewrite.
- The final text should be the user's voice, not an AI-polished
  version that loses the user's style.

## 4. What AI does well

- Grammar correction: article usage, subject-verb agreement,
  tense consistency.
- Sentence length and splitting long sentences.
- Paragraph flow: suggesting transitions.
- Translation between idiomatic English and user's first
  language.
- Finding overly long passive constructions.
- Suggesting phrasing for a known concept.

For these tasks, AI is a net positive; sentence-by-sentence
verification is still required but rarely surfaces issues.

## 5. What AI does badly

- Technical accuracy: AI may subtly misrepresent the user's
  method.
- Citations: AI confidently invents references.
- Novelty framing: AI defaults to generic inflation language.
- Voice: AI smooths the user's voice into a neutral register
  that lacks personality and distinguishability.
- Section-appropriate tense: AI mixes tenses within a paragraph.
- Avoiding AI-tone vocabulary: AI gravitates to its own banned
  words.

For these tasks, AI is a net negative; the user must catch and
correct at verification time.

## 6. Integration with pre-submission-reviewer

Vibe Writing and pre-submission-reviewer are complementary:

- Vibe Writing governs the drafting process.
- pre-submission-reviewer audits the final draft.

Typical sequence:

1. User drafts Section X in own voice.
2. User polishes with AI (Vibe Writing Step B).
3. User verifies sentence by sentence (Step C).
4. User runs `pre-submission-reviewer` on the completed section.
5. User fixes any MAJOR findings before submission.
6. Before final submission, `pre-submission-reviewer` runs on the
   full paper with banned-vocabulary and em-dash scan enabled.

Running pre-submission-reviewer without the Vibe Writing discipline
tends to produce many findings that require rewriting the section
from scratch; running Vibe Writing without pre-submission-reviewer
leaves some issues (banned vocabulary, em-dash misuse) for reviewers
to find first.
