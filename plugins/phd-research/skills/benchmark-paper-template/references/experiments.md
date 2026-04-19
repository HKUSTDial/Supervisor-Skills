# Experiment & Insight Design

Design experiments that go beyond leaderboard numbers to reveal deep insights about model capabilities. In a Benchmark paper, the experiment section is NOT about "proving our method is best", it is about **revealing where and why models fail, and what this means for future research.**

## 1. Baseline Model Selection

Cover multiple axes for comprehensive comparison. Minimum 10-15 models:

| Axis | Categories | Purpose |
|------|-----------|---------|
| **Open vs. Closed** | GPT-4o, Claude, Gemini vs. LLaMA, Qwen, Mistral, DeepSeek | Capability gap between proprietary and accessible models |
| **Model Scale** | 7B → 13B → 70B → 100B+ | How capability scales with parameters |
| **Architecture** | Decoder-only vs. Encoder-Decoder; text-only vs. multimodal | Architecture-specific strengths/weaknesses |
| **Specialization** | General vs. domain-specific (code, math, vision, etc.) | Whether specialized training transfers |

Ask the user: "Which models will be evaluated? Do they cover all four axes above?"

## 2. Evaluation Protocol

### 2.1 Evaluation Settings

Define how models interact with the benchmark:

| Element | Key Questions | Guidance |
|---------|-------------|----------|
| **Input format** | How does the model receive input? What context is provided? | Specify prompt template, input structure, and any special formatting |
| **Output extraction** | How is model output parsed and scored? | Define extraction rules, parsing logic, and edge case handling |
| **Prompting strategies** | Zero-shot, Few-shot (1/3/5), CoT, Domain knowledge prompting, Tool-use | Test multiple; report which helps/hurts |
| **Evaluation method** | Auto metrics, LLM-as-Judge, Human eval | Use ≥2 methods; validate LLM-judge against human |
| **Metrics selection** | What metrics and why? (e.g., Accuracy, F1@K, MAE, Correlation) | Justify metric choices; prefer ONE headline metric for main ranking, with breakdowns as secondary |
| **Repetitions** | 1-5 runs per model | Report mean ± std for non-deterministic setups; report intra-model variance |
| **Temperature** | 0 for reproducibility, >0 for diversity analysis | Document the choice |

### 2.2 Human Baseline Experiment

If conducting human evaluation, specify:

| Element | Details |
|---------|---------|
| **Participant profile** | How many? Background/expertise? Recruitment criteria? |
| **Experiment protocol** | Task instructions, time limit, annotation interface |
| **Inter-rater reliability** | Agreement metric (Cohen's κ, Fleiss' κ, ICC) and threshold |
| **Comparison design** | Same samples evaluated by both humans and models |

### 2.3 Baseline Fairness

Document the optimization effort for each baseline equally. Reviewers are increasingly aware of "baseline nerfing", under-optimizing competitor hyperparameters. Each baseline should use the best known configuration.

## 3. RQ-driven Experiment Structure

Organize ALL experiments around your Research Questions. Each RQ drives one analysis subsection:

### RQ Analysis Template

For each RQ, specify:

```
RQ[N]: [The question]
├── Hypothesis: [What you expect to find]
├── Experiment: [Specific comparison or analysis]
├── Variables: [What you vary vs. control]
├── Metrics: [What you measure]
├── Visualization: [Figure or Table type]
└── Expected Finding: [What insight this yields]
```

### Common Analysis Types

| Analysis | What It Reveals | Visualization | Priority |
|----------|----------------|---------------|----------|
| **Overall Performance** | General capability landscape | Large table: all models × all metrics | MUST |
| **Category Breakdown** | Per-taxonomy performance | Grouped bar chart or heatmap | MUST |
| **Difficulty Gradient** | How performance degrades with difficulty | Line chart (x=difficulty, y=score) | MUST |
| **Error Taxonomy** | WHAT types of mistakes models make | Stacked bar chart, pie chart + error examples | HIGH |
| **Model Behavioral Bias** | Whether models have systematic tendencies (e.g., score inflation, over-conservatism, preference for certain answer types) | Distribution density curves, calibration plots | HIGH |
| **Human vs. Model** | Where AI matches/exceeds/falls behind | Radar chart or paired comparison bars | HIGH |
| **Prompting Impact** | How strategy affects performance | Ablation table (rows=models, cols=strategies) | MEDIUM |
| **Scale Effect** | How model size affects capability | Line chart (x=params, y=score) | MEDIUM |
| **Cross-dim Correlation** | Which capabilities are linked | Correlation heatmap | OPTIONAL |

## 4. The Overall Performance Table

The largest and most important table in the paper (typically Table 2 or 3):

```
| Model | Size | Overall | [Dim1] | [Dim2] | [Dim3] | [SubDim1.1] | [SubDim1.2] | ... |
|-------|------|---------|--------|--------|--------|-------------|-------------|-----|
| GPT-4o | - | XX.X | XX.X | XX.X | XX.X | XX.X | XX.X | |
| Claude | - | XX.X | XX.X | XX.X | XX.X | XX.X | XX.X | |
| LLaMA-70B | 70B | XX.X | XX.X | XX.X | XX.X | XX.X | XX.X | |
| ... | | | | | | | | |
| Human | - | XX.X | XX.X | XX.X | XX.X | XX.X | XX.X | |
```

Design guidelines:
- **Bold** the best result per column; **underline** second-best
- Group models by category (closed-source / open-source / specialized)
- Include human performance as upper bound (if applicable)
- Add average and worst-case rows if insightful

## 5. The "Finding X" Pattern

<EXTREMELY-IMPORTANT>
This is the SIGNATURE writing technique of Benchmark papers. After each major analysis, extract and bold-highlight a numbered Finding:

**Finding 1.** Few-shot learning and domain knowledge inclusion help LLMs, whereas Chain-of-Thought tends to slightly degrade performance in smaller models.

**Finding 2.** All tested models perform below random baseline on [specific sub-category], revealing a fundamental capability gap in [specific skill].

**Finding 3.** Model scale improves [Dimension A] performance monotonically, but has no significant effect on [Dimension B], suggesting these capabilities have different scaling properties.

Each Finding MUST be:
- **Surprising or non-obvious**, not just "bigger models are better"
- **Specific**, names concrete models, categories, or conditions
- **Actionable**, implies what future research should address
- **Supported by data**, directly backed by the analysis above it

**Micro-structure template** for each Finding:

```
[Analysis paragraph with data...]

**Finding N.** [Lead sentence: the key result in one sentence.]
[Evidence: specific numbers, models, conditions.]
[Qualification: scope and boundary conditions.]
[Forward pointer: what this implies for future work.]
```
</EXTREMELY-IMPORTANT>

## 6. Case Study Design

Include 2-4 case studies for qualitative depth:

| Type | Purpose | Format |
|------|---------|--------|
| **Success case** | Show benchmark discriminates capability | Strong model vs. weak model on same input |
| **Failure case** | Reveal specific model limitation | Model output + annotation of where/why it fails |
| **Surprising case** | Highlight counter-intuitive behavior | Setup expectation → show unexpected result |
| **Edge case** | Test capability boundary | Minimal change that flips correct → incorrect |

## 7. Companion Method Experiments (If Applicable)

If proposing a companion method (from bench-design):

- Comparison with baselines on the new benchmark
- Ablation study of method components
- Per-category improvement analysis (WHERE does the method help most?)
- Generalization test (does improvement transfer to other benchmarks?)
- **Downstream application validation** (can the benchmark/method be used to improve real-world performance? e.g., VisJudge-Bench validated through downstream visualization quality improvement)

## 8. Research Opportunities

Derive 3-5 future directions from your Findings. Typical directions:

- How to enhance model capability on [the gap area]
- Human-AI collaboration patterns for [the task]
- Benchmark extension (new modalities, languages, domains, difficulty levels)
- Training methodology improvements inspired by the findings
- Theoretical understanding of why [specific Finding] occurs
