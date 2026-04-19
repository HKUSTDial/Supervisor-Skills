# Benchmark Pre-Submission Checklist

## Why this matters

The three-to-five-day window before a benchmark-paper submission
deadline is where structured review pays off the most. By then the
paper's structure is locked and the experiments are complete, but there
is still time for one last audit. A missing pipeline figure, absent
Finding summaries, missing benchmark comparison table, or missing
datasheet is individually fixable in hours; collectively they sink an
otherwise strong paper. NeurIPS Datasets and Benchmarks, ICLR, ICML,
ACL, EMNLP, and CVPR each have venue-specific requirements that
compound the general checklist, and 2025-2026 introduced new mandates
(NeurIPS Croissant metadata is now required; missing or invalid
Croissant is grounds for desk rejection).

This skill is the terminal node of the benchmark-writing DAG. It runs a
systematic four-dimension audit on the submitted draft, produces a
severity-classified finding list (Critical, Major, Minor), and routes
back to the specific sub-skill if a check fails. Critical items block
submission; Major items are strongly recommended; Minor items are
polish. The skill does not rewrite the paper; it flags issues and
routes remediation to the appropriate earlier sub-skill.

## The framework

The audit covers four check dimensions plus venue-specific requirements.
Each dimension runs through its checklist items, and every item gets
one of three marks: Pass, Needs Work, or Not Applicable (with reason).

### 1. Introduction checklist

Eight items cover the Introduction section:

- **Running Example (Figure 1)**: a carefully designed figure
  illustrating the evaluation gap with a concrete example.
- **Evaluation Gap**: key blind spots of existing benchmarks clearly
  stated (at most three points, specific not vague).
- **Benchmark Comparison (Table 1)**: comparison with at least five
  existing benchmarks across key dimensions.
- **Research Questions**: 2-3 RQs explicitly stated.
- **Design Considerations**: design rationale and key choices explained
  (WHY, not just WHAT).
- **Contributions**: 2-4 contributions listed, each aligned with an RQ
  and a paper section.
- **Narrative Flow**: Background -> Gap -> Our Solution -> Preview
  Findings -> Contributions.
- **Concrete Numbers**: scale, model count, and key metrics mentioned in
  the Introduction.

### 2. Benchmark section checklist

Nine items cover Section 2 of the paper:

- **Design Goals**: G1-G4 or custom goals explicitly stated with
  strategies.
- **Task Scope**: clear boundary of what IS and IS NOT evaluated, with
  reasons for exclusions.
- **Pipeline Figure (Figure 2)**: a clear construction-pipeline
  flowchart with steps, data counts, and quality gates.
- **Pipeline Steps**: every step has explicit input, operation, and
  output.
- **Quality Control**: QC strategy described (inter-annotator agreement,
  expert review, validation scores).
- **Dataset Statistics (Table 2)**: comprehensive statistics presented
  (total count, per-split, per-category).
- **Distribution Figures**: taxonomy distribution, difficulty
  distribution, length distribution visualised.
- **Data Examples**: 2-3 representative examples shown as a figure.
- **Taxonomy Coverage**: data distribution covers all taxonomy
  categories with reasonable balance.

### 3. Experiment section checklist

Eight items cover Section 4 of the paper:

- **Model Coverage**: baselines span open or closed source, multiple
  scales, different architectures (at least 10 models).
- **Overall Performance Table (Table 3)**: comprehensive table with all
  models times all metrics, best and second-best marked.
- **Fine-grained Analysis**: multi-dimensional analysis beyond overall
  scores, organised by RQ.
- **Error Taxonomy**: analysis of WHAT types of mistakes models make
  (not just accuracy numbers).
- **Human versus Model**: human performance baseline included. Marked
  Not Applicable with reason if genuinely not applicable.
- **Case Studies**: 2-4 qualitative examples showing concrete model
  success or failure.
- **Finding X Summaries**: key insights extracted and bold-highlighted
  after each major analysis.
- **Research Opportunities**: future directions discussed, grounded in
  the Findings.

### 4. Structure and completeness checklist

Fifteen items cover overall paper quality and submission readiness:

- **Logical Thread**: paper follows Gap -> Benchmark -> Evaluation ->
  Insights -> Opportunities.
- **Open Source**: code and data released or will be. Link in Abstract
  or Contributions.
- **Data Hosting**: dataset hosted on a dedicated platform (Hugging
  Face, Kaggle, OpenML, Dataverse) accessible without emailing authors.
- **License**: explicit license specified for both code and data.
- **Limitations**: honest discussion of benchmark limitations and scope
  restrictions.
- **Ethics**: discussion of potential harms, biases, PII exposure,
  informed consent, and responsible-use guidelines.
- **Datasheet or Data Card**: structured documentation of collection
  process, intended use, and limitations (in appendix or supplementary).
- **Related Work**: systematic comparison with existing work, including
  a comparison table.
- **Appendix**: supplementary material includes full results, annotation
  guidelines, more examples, prompts used.
- **Reproducibility**: enough detail for another team to reproduce
  construction and experiments. Executable evaluation script provided.
- **Statistical Rigor**: multiple evaluation runs reported with
  mean plus or minus std. Statistical significance tests where
  appropriate.
- **Contamination Mitigation**: strategy to prevent training data
  leakage documented.
- **Maintenance Plan**: who will maintain the benchmark, feedback
  channels, update or retirement criteria.
- **Page Budget**: paper fits within the venue's page limit (main body).
- **References**: all cited works verified and formatted per venue
  style.

### 5. Venue-specific checks

**NeurIPS (Evaluations and Datasets track, renamed from D&B in 2026):**

- Evaluations and Datasets track selected (double-blind by default
  since 2026).
- NeurIPS paper checklist completed.
- **Croissant metadata file** included and validated. Mandatory since
  2025; missing or invalid Croissant is grounds for desk rejection.
- Data and code submitted in final form alongside the paper, not as
  supplementary material since 2026.
- Supplementary material within size limits.
- Anonymous submission (no author-identifying information).

**ICLR and ICML:**

- Reproducibility form or checklist completed.
- Supplementary material within size limits.
- Anonymous submission.

**ACL, EMNLP, NAACL:**

- Limitations section present (mandatory).
- Ethics statement present.
- ARR submission format followed.

### Severity classification

After checking all items, classify each open issue:

| Severity | Definition | Action |
|---|---|---|
| **Critical** | Missing core element (no pipeline figure, no Finding summaries, no comparison table, missing Croissant metadata at NeurIPS) | MUST fix before submission |
| **Major** | Present but insufficient (too few baselines, weak QC description, vague gap) | Strongly recommended to fix |
| **Minor** | Polish-level (figure aesthetics, word choice, appendix order) | Fix if time permits |

Final summary format:

```
Pre-submission Verdict: [READY | NOT READY]

Critical issues: [count], [list]
Major issues:    [count], [list]
Minor issues:    [count], [list]
```

### Remediation routing

If critical issues remain, the skill routes the user back to the
appropriate earlier sub-skill:

- Missing or weak gap statement ->
  [bench-gap-analysis](../bench-gap-analysis/overview.md).
- Incomplete design goals or taxonomy ->
  [bench-design](../bench-design/overview.md).
- Missing Figure 2 or pipeline description ->
  [bench-construction](../bench-construction/overview.md).
- Missing Finding summaries or narrow baselines ->
  [bench-experiments](../bench-experiments/overview.md).
- Introduction missing a part or sections misaligned with contributions
  -> [bench-paper-structure](../bench-paper-structure/overview.md).

## Key checks

- **Four must-have figures and tables**: Figure 1 Running Example,
  Table 1 Benchmark Comparison, Figure 2 Pipeline, Table 3 Overall
  Performance. Missing any is Critical.
- **Finding X presence**: at least one bolded Finding per major
  analysis. Absent Findings is Major at minimum.
- **Design Considerations paragraph**: unique to benchmark papers.
  Absent is Major.
- **NeurIPS Croissant metadata**: mandatory since 2025. Missing or
  invalid is Critical.
- **Datasheet or Data Card**: required for any dataset paper targeting
  a major venue.
- **Human baseline**: required unless there is a defensible
  Not-Applicable reason.
- **Severity taxonomy**: Critical blocks, Major strongly recommended,
  Minor is polish.

## Worked example

Consider a user submitting a nvBench 2.0-style paper two days before the
NeurIPS deadline. The checklist runs through four dimensions.

**Introduction (8 items).** Figure 1 present (runs through two
ambiguous query interpretations). Table 1 present, compares seven
benchmarks. RQs explicit (three of them). Design Considerations
paragraph present. Contributions list four items, mapped to sections.
Narrative flow intact. Concrete numbers present. Gap paragraph:
reviewer will want one more sentence explicitly calling out the
assumption. Minor.

**Benchmark section (9 items).** Design goals stated. Task scope
defined. Figure 2 present, shows Controlled Injection pipeline with
data counts. Every pipeline step documented. QC strategy described
(Fleiss' kappa at 0.68). Table 2 present. Figures 3-4 present. Data
examples present. Taxonomy coverage: the rarest severity level (Lv5
filter ambiguity) has only 41 samples, which is below the threshold for
statistically reliable per-cell analysis. Major: the user should either
inject more at this cell or note the limitation explicitly in Section
2.3.

**Experiment section (8 items).** 16 baselines across four axes. Table
3 present with bold and underline. Fine-grained analysis by RQ. Error
taxonomy present. Human versus Model present. Case studies present (3
cases). Finding X summaries: only two findings bolded across the entire
experiments section, but there are four major analyses. Major: user
should extract two more findings. Research Opportunities discussed.

**Structure and completeness (15 items).** All items pass except two:
Croissant metadata file not yet prepared (Critical, since this is a
NeurIPS submission and 2025-onward Croissant is mandatory), and
Datasheet in appendix present but missing the "intended use and
limitations" section (Major).

**Verdict.** NOT READY. Critical issues: 1 (Croissant metadata
missing). Major issues: 3 (under-populated Lv5 cell, two more Findings
needed, Datasheet intended-use section missing). Minor issues: 1 (Gap
paragraph could add one sentence). The user has 48 hours, which is
enough to fix all Critical and Major items in priority order: Croissant
first (blocks submission), then the Findings extraction and Datasheet
section, then the Lv5 explanatory sentence in Section 2.3. The Minor
gap-paragraph polish can wait.

The skill routes the user to
[bench-construction](../bench-construction/overview.md) for the Lv5
cell question and to
[bench-experiments](../bench-experiments/overview.md) for the Finding
extraction. Croissant is a mechanical fix outside the DAG; the skill
points the user to the NeurIPS documentation for the schema.

## Try it with the plugin

Install the plugin per the [root README](../../../../README.md) and
invoke naturally. The skill self-triggers on phrases from its SKILL.md
description such as "the paper draft is complete and you need
systematic verification before submission", "final quality gate before
submitting", or "pre-submission checklist". Provide the paper text or
section-by-section summaries, and the skill runs through all four check
dimensions plus the venue-specific checks, returning the final
severity-classified findings list and the Ready or Not Ready verdict.

For best results, run this skill three to five days before the
deadline, fix Critical items first and Major items where time allows,
then run the skill one more time to confirm no regressions. This skill
is complementary to the general
[pre-submission-reviewer](../pre-submission-reviewer/overview.md),
which covers technique papers and general writing mechanics; the bench
checklist is specialised for the benchmark-paper-specific items listed
above.

## Source

Adapted from
[archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md)
and the live plugin file
[/plugins/phd-research/skills/bench-checklist/SKILL.md](/plugins/phd-research/skills/bench-checklist/SKILL.md).

---

[English] | [中文](../../../zh/skills/bench-checklist/overview.md)
