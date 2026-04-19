# Benchmark Experiments and Insight Design

## Why this matters

The experiment section of a benchmark paper has a fundamentally different
goal than the experiment section of a technique paper. A technique paper
proves that one method beats baselines; a benchmark paper reveals where
and why models fail, and what that means for future research. Writing a
benchmark experiment section with a technique-paper mindset produces the
second-most-common rejection pattern at NeurIPS Datasets and Benchmarks,
ICLR, ICML, and CVPR: a large leaderboard table with no insights
extracted. Reviewers look at the leaderboard, nod that one frontier
model beats another on average, and ask "so what?" The benchmark paper without the
"Finding X" extraction pattern has no quotable findings that future
papers can cite.

This skill designs the experiment section around research questions and
around the Finding X pattern, the signature writing technique of
benchmark papers. It covers baseline coverage across four axes, the
evaluation protocol (including LLM-as-Judge validation and human
baseline), RQ-driven analysis structure, the overall-performance table,
the Finding extraction pattern, case-study selection, the optional
companion-method experiments, and research-opportunities outline. A hard
gate enforces the shift in mindset: do not design experiments to prove
superiority; design experiments to diagnose model behaviour and generate
actionable insights.

## The framework

The skill runs eight sequential sections, each corresponding to a
section of the paper's experimental material.

### 1. Baseline model selection across four axes

Reviewers check whether the baseline set is representative. Cover
multiple axes for comprehensive comparison; minimum 10-15 models.

| Axis | Categories | Purpose |
|---|---|---|
| Open versus closed | Closed-source frontier models versus LLaMA, Qwen, Mistral, DeepSeek | Capability gap between proprietary and accessible models |
| Model scale | 7B -> 13B -> 70B -> 100B+ | How capability scales with parameters |
| Architecture | Decoder-only versus Encoder-Decoder; text-only versus multimodal | Architecture-specific strengths and weaknesses |
| Specialisation | General versus domain-specific (code, math, vision) | Whether specialised training transfers |

A baseline set that covers all four axes pre-empts the reviewer question
"why didn't you test X?" because every major direction is represented.

### 2. Evaluation protocol

**2.1 Evaluation settings.** Define how models interact with the
benchmark:

| Element | Key questions | Guidance |
|---|---|---|
| Input format | How does the model receive input? What context is provided? | Specify prompt template, input structure, any special formatting |
| Output extraction | How is model output parsed and scored? | Define extraction rules, parsing logic, edge-case handling |
| Prompting strategies | Zero-shot, Few-shot (1/3/5), CoT, domain-knowledge prompting, tool-use | Test multiple; report which helps or hurts |
| Evaluation method | Auto metrics, LLM-as-Judge, human eval | Use at least two methods; validate LLM-judge against human |
| Metrics selection | What metrics and why? | Justify metric choices; prefer one headline metric, with breakdowns as secondary |
| Repetitions | 1-5 runs per model | Report mean plus or minus std for non-deterministic setups |
| Temperature | 0 for reproducibility, above 0 for diversity analysis | Document the choice |

**2.2 Human baseline experiment.** If human evaluation is included,
specify participant profile (how many, background, recruitment criteria),
experiment protocol (task instructions, time limit, annotation
interface), inter-rater reliability (agreement metric plus threshold),
and comparison design (same samples evaluated by both humans and
models).

**2.3 Baseline fairness.** Document the optimisation effort for each
baseline equally. Reviewers are increasingly aware of "baseline
nerfing", the practice of under-optimising competitor hyperparameters.
Each baseline should use the best known configuration.

### 3. RQ-driven experiment structure

Organise every experiment around a research question. Each RQ drives one
analysis subsection in the paper:

```
RQ[N]: [The question]
 ├── Hypothesis: [What you expect to find]
 ├── Experiment: [Specific comparison or analysis]
 ├── Variables: [What you vary versus control]
 ├── Metrics: [What you measure]
 ├── Visualisation: [Figure or table type]
 └── Expected Finding: [What insight this yields]
```

A table of common analysis types with priority and visualisation:

| Analysis | What it reveals | Visualisation | Priority |
|---|---|---|---|
| Overall Performance | General capability landscape | Large table: all models times all metrics | MUST |
| Category Breakdown | Per-taxonomy performance | Grouped bar chart or heatmap | MUST |
| Difficulty Gradient | How performance degrades with difficulty | Line chart (x=difficulty, y=score) | MUST |
| Error Taxonomy | WHAT types of mistakes models make | Stacked bar, pie chart plus error examples | HIGH |
| Model Behavioural Bias | Whether models have systematic tendencies (score inflation, over-conservatism, preference for certain answer types) | Distribution density curves, calibration plots | HIGH |
| Human versus Model | Where AI matches, exceeds, or falls behind | Radar chart or paired comparison bars | HIGH |
| Prompting Impact | How strategy affects performance | Ablation table (rows=models, cols=strategies) | MEDIUM |
| Scale Effect | How model size affects capability | Line chart (x=parameters, y=score) | MEDIUM |
| Cross-dimension Correlation | Which capabilities are linked | Correlation heatmap | OPTIONAL |

### 4. The overall-performance table

The largest and most important table in the paper (typically Table 3).
Design guidelines:

- Bold the best result per column; underline second-best.
- Group models by category (closed-source, open-source, specialised).
- Include human performance as an upper bound if applicable.
- Add average and worst-case rows if insightful.

### 5. The Finding X pattern (signature technique)

After each major analysis, extract and bold-highlight a numbered
Finding. Examples of well-formed Findings:

> **Finding 1.** Few-shot learning and domain-knowledge inclusion help
> LLMs, whereas Chain-of-Thought tends to slightly degrade performance
> in smaller models.

> **Finding 2.** All tested models perform below random baseline on
> [specific sub-category], revealing a fundamental capability gap in
> [specific skill].

> **Finding 3.** Model scale improves [Dimension A] performance
> monotonically, but has no significant effect on [Dimension B],
> suggesting these capabilities have different scaling properties.

Each Finding must be surprising or non-obvious (not just "bigger models
are better"), specific (names concrete models, categories, or
conditions), actionable (implies what future research should address),
and supported by data (directly backed by the analysis above it).

**Micro-structure template** for each Finding:

```
[Analysis paragraph with data.]

**Finding N.** [Lead sentence: the key result in one sentence.]
[Evidence: specific numbers, models, conditions.]
[Qualification: scope and boundary conditions.]
[Forward pointer: what this implies for future work.]
```

The Finding pattern is what makes benchmark papers quotable and citable
by downstream research. A benchmark paper that produces no Findings
produces no follow-on work.

### 6. Case-study design

Include 2-4 case studies for qualitative depth:

| Type | Purpose | Format |
|---|---|---|
| Success case | Show benchmark discriminates capability | Strong model versus weak model on same input |
| Failure case | Reveal specific model limitation | Model output plus annotation of where and why it fails |
| Surprising case | Highlight counter-intuitive behaviour | Setup expectation, then show unexpected result |
| Edge case | Test capability boundary | Minimal change that flips correct to incorrect |

### 7. Companion-method experiments (if applicable)

If a companion method was proposed in
[bench-design](../bench-design/overview.md), the experiments section
also reports its evaluation: comparison with baselines on the new
benchmark, ablation study of method components, per-category improvement
analysis (where does the method help most), generalisation test (does
the improvement transfer to other benchmarks), and downstream
application validation (can the benchmark or method improve real-world
performance, as VisJudge-Bench validated through downstream
visualisation quality improvement).

### 8. Research opportunities

Derive 3-5 future directions from the Findings. Typical directions: how
to enhance model capability on the identified gap, human-AI
collaboration patterns for the task, benchmark extension (new
modalities, languages, domains, difficulty levels), training
methodology improvements inspired by the findings, theoretical
understanding of why a specific Finding occurs.

## Named heuristics

- **Four baseline axes**: open versus closed, scale, architecture,
  specialisation. Cover all four or pre-empt the reviewer question.
- **RQ-driven structure**: every analysis subsection corresponds to one
  research question. No orphan analyses.
- **Finding X pattern**: bold-highlighted, numbered, surprising,
  specific, actionable, and data-supported. The signature writing
  technique of benchmark papers.
- **Baseline fairness discipline**: document optimisation effort for
  each baseline equally. No "baseline nerfing".
- **LLM-as-Judge validation rule**: any LLM-as-Judge protocol must
  report correlation with human annotation. No validation, no
  acceptance.
- **Case-study four-type coverage**: success, failure, surprising, and
  edge. 2-4 cases total.

## Worked example

Consider VisJudge-Bench after construction. The gap is Granularity
Mismatch: existing visualisation evaluation checks aesthetics OR
accuracy in isolation. The taxonomy is three top-level dimensions
(Fidelity, Expressiveness, Aesthetics) with two sub-dimensions each.

**Baselines.** Fifteen models across four axes. Closed-source frontier
models from multiple vendors. Open-source at multiple scales:
LLaMA-3-8B, LLaMA-3-70B, Qwen2.5-7B, Qwen2.5-72B, DeepSeek-V3,
Mistral-Large. Multimodal specifically: GPT-4V, InternVL, LLaVA-NeXT
plus two other vision-language models. Domain specialised: a proprietary
visualisation model plus two vision-language models trained on chart
datasets.

**Evaluation protocol.** Two evaluation methods: automatic metrics for
Fidelity (BLEU-style overlap between generated and ground-truth chart
specs) and LLM-as-Judge for Expressiveness and Aesthetics. LLM-as-Judge
validated against human PhD-student rater with Pearson correlation
reported per sub-dimension. Baseline fairness documented in the
appendix: each model evaluated with its best-published prompting
strategy, same number of shots across models.

**RQ structure.** RQ1 (how do models perform on each of the six
sub-dimensions independently?) drives the Overall Performance and
Category Breakdown analyses. RQ2 (how does performance change across
difficulty levels?) drives the Difficulty Gradient analysis. RQ3 (where
do models systematically fail, and what types of errors dominate?)
drives the Error Taxonomy and Case Studies.

**Findings.** Finding 1: closed-source models outperform open-source by
a large margin on Aesthetics, but the gap narrows on Fidelity (open
models catch up when the task is factual rather than subjective).
Finding 2: no model exceeds 60 percent on the Expressiveness
sub-dimension, revealing a fundamental gap in chart-level
communication-clarity reasoning. Finding 3: vision-language models
specialised on chart data underperform GPT-4V on Aesthetics despite
outperforming on Fidelity, suggesting that specialisation trades
aesthetic judgment for factual accuracy.

**Case studies.** Four cases: a success where GPT-4o correctly
identifies a misleading axis scale; a failure where every tested model
misses a colour-blind-accessibility issue; a surprising case where a
smaller model outperforms a larger one on a subtle aesthetic judgment;
an edge case where minor layout changes flip the model's evaluation
from positive to negative.

**Companion-method experiments.** The VisJudge model (GRPO-trained on
the benchmark's fine-grained scores) is evaluated against GPT-4o on
held-out data. Per-sub-dimension improvement analysis shows where GRPO
helps most. Generalisation test to ChartQA and MiniVQA confirms the
improvements transfer. Downstream application validation shows the
VisJudge model improves the final chart quality by a measurable
percentage in an end-to-end chart-generation pipeline.

**Research opportunities.** Three directions: extend to interactive
dashboards (current benchmark is static charts only), extend to
low-resource language chart titles, study aesthetic-factual trade-offs
as a general VLM training problem.

StatQA's experiment design follows the same structure with different
RQs and findings. nvBench 2.0's follows the same structure with its
controlled-injection severity gradient driving a distinct Difficulty
Gradient analysis.

## Try it with the plugin

Install the plugin per the [root README](../../../../README.md) and
invoke naturally. The skill self-triggers on phrases from its SKILL.md
description such as "the benchmark data exists or is being built and
you need to plan baselines", "plan baselines, evaluation protocols,
fine-grained analyses", or "What experiments yield the deepest
insights?". Provide the research questions from
[bench-gap-analysis](../bench-gap-analysis/overview.md) and the design
from [bench-design](../bench-design/overview.md), and the skill walks
through baseline selection, protocol, RQ-driven analyses, and the
Finding extraction plan.

## Source

Adapted from
[archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md)
and the live plugin file
[/plugins/phd-research/skills/bench-experiments/SKILL.md](/plugins/phd-research/skills/bench-experiments/SKILL.md).

---

[English] | [中文](../../../zh/skills/bench-experiments/overview.md)
