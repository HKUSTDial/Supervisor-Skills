# Pre-submission Checklist

## Contents

- [1. Introduction Checklist](#1-introduction-checklist)
- [2. Benchmark Section Checklist](#2-benchmark-section-checklist)
- [3. Experiment Section Checklist](#3-experiment-section-checklist)
- [4. Structure & Completeness Checklist](#4-structure--completeness-checklist)
- [5. Venue-Specific Checks](#5-venue-specific-checks)
- [Severity Classification](#severity-classification)
- [After the Checklist](#after-the-checklist)

The final quality gate before submission. A single missing element, a forgotten pipeline figure, absent Finding summaries, or no benchmark comparison table, can cost a paper its acceptance at top venues.

## 1. Introduction Checklist

- [ ] **Running Example (Figure 1)**: A carefully designed figure illustrating the evaluation gap with a concrete example?
- [ ] **Evaluation Gap**: Key blind spots of existing benchmarks clearly stated (≤3 points, specific not vague)?
- [ ] **Benchmark Comparison (Table 1)**: Comparison with ≥5 existing benchmarks across key dimensions?
- [ ] **Research Questions**: 2-3 RQs explicitly stated?
- [ ] **Design Considerations**: Design rationale and key choices explained (WHY, not just WHAT)?
- [ ] **Contributions**: 2-4 contributions listed, each aligned with an RQ and a paper section?
- [ ] **Narrative Flow**: Background → Gap → Our Solution → Preview Findings → Contributions?
- [ ] **Concrete Numbers**: Scale, model count, and key metrics mentioned in the Introduction?

## 2. Benchmark Section Checklist

- [ ] **Design Goals**: G1-G4 (or custom goals) explicitly stated with strategies?
- [ ] **Task Scope**: Clear boundary of what IS and IS NOT evaluated, with reasons for exclusions?
- [ ] **Pipeline Figure (Figure 2)**: A clear construction pipeline flowchart with steps, data counts, and quality gates?
- [ ] **Pipeline Steps**: Every step has explicit input, operation, and output?
- [ ] **Quality Control**: QC strategy described (inter-annotator agreement, expert review, validation scores)?
- [ ] **Dataset Statistics (Table 2)**: Comprehensive statistics presented (total count, per-split, per-category)?
- [ ] **Distribution Figures**: Taxonomy distribution, difficulty distribution, length distribution visualized?
- [ ] **Data Examples**: 2-3 representative examples shown as a figure?
- [ ] **Taxonomy Coverage**: Data distribution covers all taxonomy categories with reasonable balance?

## 3. Experiment Section Checklist

- [ ] **Model Coverage**: Baselines span open/closed source, multiple scales, different architectures (≥10 models)?
- [ ] **Overall Performance Table (Table 3)**: Comprehensive table with all models × all metrics, best/second-best marked?
- [ ] **Fine-grained Analysis**: Multi-dimensional analysis beyond overall scores, organized by RQ?
- [ ] **Error Taxonomy**: Analysis of WHAT types of mistakes models make (not just accuracy numbers)?
- [ ] **Human vs. Model**: Human performance baseline included? (Mark N/A with reason if genuinely not applicable)
- [ ] **Case Studies**: 2-4 qualitative examples showing concrete model success/failure?
- [ ] **Finding X Summaries**: Key insights extracted and bold-highlighted after each major analysis?
- [ ] **Research Opportunities**: Future directions discussed, grounded in the Findings?

## 4. Structure & Completeness Checklist

- [ ] **Logical Thread**: Paper follows Gap → Benchmark → Evaluation → Insights → Opportunities?
- [ ] **Open Source**: Code and data released (or will be)? Link in Abstract or Contributions?
- [ ] **Data Hosting**: Dataset hosted on a dedicated platform (Hugging Face, Kaggle, OpenML, Dataverse), accessible without emailing authors?
- [ ] **License**: Explicit license specified for both code and data?
- [ ] **Limitations**: Honest discussion of benchmark limitations and scope restrictions?
- [ ] **Ethics**: Discussion of potential harms, biases, PII exposure, informed consent, and responsible-use guidelines?
- [ ] **Datasheet / Data Card**: Structured documentation of collection process, intended use, and limitations included (in appendix or supplementary)?
- [ ] **Related Work**: Systematic comparison with existing work, including a comparison table?
- [ ] **Appendix**: Supplementary material includes full results, annotation guidelines, more examples, prompts used?
- [ ] **Reproducibility**: Enough detail for another team to reproduce construction and experiments? Executable evaluation script provided?
- [ ] **Statistical Rigor**: Multiple evaluation runs reported with mean ± std? Statistical significance tests where appropriate?
- [ ] **Contamination Mitigation**: Strategy to prevent training data leakage documented?
- [ ] **Maintenance Plan**: Who will maintain the benchmark? Feedback channels? Update/retirement criteria?
- [ ] **Page Budget**: Paper fits within the venue's page limit (main body)?
- [ ] **References**: All cited works verified and formatted per venue style?

## 5. Venue-Specific Checks

### NeurIPS (Evaluations & Datasets track, renamed from D&B in 2026)
- [ ] Evaluations & Datasets track selected (double-blind by default since 2026)?
- [ ] NeurIPS paper checklist completed?
- [ ] **Croissant metadata file** included and validated? (Mandatory since 2025, missing/invalid Croissant is grounds for desk rejection)
- [ ] Data and code submitted in final form alongside the paper (NOT supplementary material since 2026)?
- [ ] Supplementary material within size limits?
- [ ] Anonymous submission (no author-identifying information)?

### ICLR / ICML
- [ ] Reproducibility form / checklist completed?
- [ ] Supplementary material within size limits?
- [ ] Anonymous submission?

### ACL / EMNLP / NAACL
- [ ] Limitations section present (mandatory)?
- [ ] Ethics statement present?
- [ ] ARR submission format followed?

## Severity Classification

After checking all items, classify issues:

| Severity | Definition | Action |
|----------|-----------|--------|
| **Critical** ✗✗ | Missing core element (no pipeline figure, no Finding summaries, no comparison table) | MUST fix before submission |
| **Major** ✗ | Present but insufficient (too few baselines, weak QC description, vague gap) | Strongly recommended to fix |
| **Minor** ~ | Polish-level (figure aesthetics, word choice, appendix order) | Fix if time permits |

Present a summary:
```
Pre-submission Verdict: [READY / NOT READY]

Critical issues: [count], [list]
Major issues:    [count], [list]
Minor issues:    [count], [list]
```

## After the Checklist

- **If critical issues remain**: Help the user fix them by routing back to the relevant sub-skill (e.g., missing pipeline figure → bench-construction concepts)
- **If all clear**: Confirm readiness and remind about:
  - Venue-specific formatting and templates
  - Supplementary material preparation
  - Co-author review before final submission
  - Camera-ready preparation timeline (if accepted)
