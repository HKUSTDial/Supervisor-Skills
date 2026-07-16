# Argument patterns from four arXiv papers

## Table of contents

1. Scope and attribution
2. TaylorSeer
3. ToCa
4. GlobalCom2
5. VidCom2
6. Cross-paper comparison
7. Transferable writing patterns
8. Patterns not to copy mechanically

## 1. Scope and attribution

This reference is an original structural synthesis of four public arXiv
papers. It analyzes argument design, not acceptance status, scientific
correctness, or final venue versions. It paraphrases the papers and does not
reproduce their prose.

Sources:

- TaylorSeer, arXiv:2503.06923v1:
  https://arxiv.org/html/2503.06923v1
- ToCa, arXiv:2410.05317:
  https://arxiv.org/html/2410.05317
- VidCom2, arXiv:2505.14454:
  https://arxiv.org/html/2505.14454
- GlobalCom2, arXiv:2501.05179:
  https://arxiv.org/html/2501.05179

All four are empirical method papers. Their strongest shared pattern is not a
standard section order. It is the treatment of each method component as a
direct response to diagnostic evidence.

## 2. TaylorSeer

### 2.1 One-sentence story

Directly reusing an old feature becomes inaccurate across large diffusion
timestep intervals, while feature values and differences follow structured
trajectories. Forecasting future features with finite differences and Taylor
expansion can therefore retain generation quality at higher acceleration.

### 2.2 Narrative archetype

The paper uses a structural-ceiling story:

`old paradigm limit -> new predictable property -> paradigm replacement`

The title foregrounds the conceptual shift from reusing to forecasting before
naming the acceleration task and method.

### 2.3 Abstract contract

1. Diffusion Transformers are effective but expensive.
2. Feature caching is attractive because it is training-free.
3. Large timestep intervals reduce feature similarity and increase error.
4. Future features can be predicted from historical features.
5. Finite differences approximate derivatives for Taylor prediction.
6. Image, video, and class-conditional results emphasize high acceleration.

The key writing move is precision. The gap is not "caching remains
challenging." It is the structural limit of direct reuse as the interval
grows.

### 2.4 Introduction roles

- P1: generation progress and computational cost
- P2: acceleration as the broader research response
- P3: caching mechanism, practicality, and adoption
- P4: similarity decay over distant timesteps, supported by feature distance
- P5: smooth feature and derivative trajectories, supporting predictability
- P6: cache-then-forecast and its Taylor implementation
- P7: high-acceleration results, where the distinction is strongest
- P8: contributions as paradigm, method, and evidence

### 2.5 Method logic

`continuous process -> smoothness assumption -> naive caching error -> linear
prediction -> higher-order prediction -> error bound`

The method hierarchy doubles as an ablation hierarchy. Order zero corresponds
to direct reuse, order one to linear forecasting, and higher order to
nonlinear trajectory approximation. This gives the later order experiment a
clear theoretical role.

### 2.6 Evidence design

- Cover text-to-image, text-to-video, and class-conditional generation.
- Report latency and FLOPs together with quality metrics.
- Concentrate the main claim on the high-acceleration regime.
- Organize qualitative errors by text corruption, object omission, color, and
  motion detail.
- Cross interval with prediction order to show failure, improvement, and
  saturation.
- Visualize feature and higher-order difference trajectories to support the
  forecasting premise.

### 2.7 Figure roles

- Feature and derivative trajectories answer why forecasting is plausible.
- A high-acceleration comparison answers why a paradigm shift matters.
- A zero-, first-, second-, and general-order overview unifies baseline and
  method.
- Order and compute curves expose where higher order helps and saturates.

### 2.8 Transferable lesson and risk

Lesson: define the paper around the regime where the old assumption breaks,
not around a small average improvement.

Risk: smooth low-dimensional trajectories do not automatically establish
final generation quality. State the error-bound assumptions and connect local
prediction error to downstream outcomes with controlled experiments.

## 3. ToCa

### 3.1 One-sentence story

Whole-layer caching treats tokens and layers as equally safe to reuse, but
their temporal redundancy and error propagation differ substantially.
Selecting tokens and allocating layer budgets at finer granularity can reduce
quality loss under the same acceleration budget.

### 3.2 Narrative archetype

The paper uses:

`average treatment hides heterogeneity -> two probes quantify it -> adaptive
fine-grained decisions`

Its distinctive conceptual addition is not only token-wise operation. It
introduces error propagation as a cache-selection concern.

### 3.3 Abstract contract

1. Diffusion Transformers are effective and expensive.
2. Feature caching reuses features across neighboring timesteps.
3. Tokens differ strongly in sensitivity to caching.
4. Token-wise caching chooses reusable tokens and varies layer ratios.
5. Image, video, and class-conditional tasks test the design.
6. Representative acceleration numbers summarize the bounded scope.

### 3.4 Introduction roles

- P1: task success, cost, and acceleration routes
- P2: practical appeal of caching and architecture-transfer gap
- P3: temporal-redundancy probe across tokens
- P4: equal perturbations cause different final errors across tokens
- P5: synthesis into cache-sensitivity heterogeneity
- P6: four low-cost scores and layer-aware ratios
- P7: cross-task headline evidence
- P8: framework, scoring, allocation, and empirical contributions

### 3.5 Method logic

`naive cache baseline -> token-wise cache lifecycle -> token scores ->
layer-wise budget`

The token signals address influence on other tokens, condition relevance,
staleness from repeated caching, and spatial concentration. Layer ratios then
address depth and operation-type differences.

### 3.6 Evidence design

- Test image, video, and class-conditional generation models.
- Compare with both same-route cache methods and reduced sampling steps.
- Use different metrics for visual quality and condition alignment.
- Break video results into multiple dimensions.
- Ablate token scores, depth-aware ratios, and type-aware ratios.
- Visualize cached-token locations and frequency distributions.
- Put hyperparameter sensitivity and complexity analysis in the appendix.

### 3.7 Figure roles

- Token-distance distribution establishes temporal heterogeneity.
- Equal-noise perturbation establishes error-propagation heterogeneity.
- The overview shows initialization, selection, computation, and update.
- A score diagram makes four heuristics interpretable.
- Depth and type probes justify layer-specific ratios.
- Cache heatmaps connect a control component to visible behavior.
- A FLOPs-quality Pareto curve prevents a favorable single-point comparison.

### 3.8 Transferable lesson and risk

Lesson: use complementary probes. One shows that approximation errors differ;
another shows that equal local errors have different downstream impact. The
combination makes fine-grained selection appear necessary rather than merely
available.

Risk: many scores and hyperparameters can look heuristic-heavy. Use
principle-level ablations, sensitivity, and measured overhead to justify the
complexity. Avoid absolute claims of zero additional cost.

## 4. GlobalCom2

### 4.1 One-sentence story

High-resolution vision-language models use a global thumbnail and local crops.
Single-view compression ignores their complementary roles, crop information
density, and positional bias. A global view can guide per-crop budgets and
combine global with local token evidence.

### 4.2 Narrative archetype

The paper uses:

`system structure invalidates old assumptions -> dedicated analysis reframes
the problem -> global-to-local principle`

Unlike a compact motivation paragraph, the problem analysis is substantial
enough to become its own section and contribution.

### 4.3 Abstract contract

1. Long multimodal contexts make high-resolution models expensive.
2. Token compression works but was designed for single-view processing.
3. Dynamic cropping creates a hierarchy that uniform treatment ignores.
4. Thumbnail and crops are complementary, and crops differ in information.
5. A global commander allocates crop budgets and guides token selection.
6. Extreme-compression results report performance, compute, and memory.

### 4.4 Introduction roles

- P1: dynamic cropping, token cost, and hierarchical context
- P2: value of token compression and its single-view origin
- P3: global neglect, crop-information disparity, and positional bias
- P4: two analysis observations
- P5: global-to-local mechanism and composability
- P6: analysis, method, and trade-off contributions

### 4.5 Analysis logic

1. Compare thumbnail-only with crop-only input to show complementary task
   strengths.
2. Use a vision-encoder signal to estimate crop information.
3. Remove the highest- and lowest-score crops to connect the score to task
   impact.
4. Name the observations and map them directly to method components.

The deletion intervention is important. A score distribution alone would not
show that the difference matters to the task.

### 4.6 Method logic

`global crop richness -> adaptive per-crop ratio -> local and global token
scores -> holistic selection -> fallback without class token`

Separating "how much to retain" from "which units to retain" gives each
observation one component and one later ablation.

### 4.7 Evidence design

- Test architectures with different visual encoders.
- Evaluate multiple retention ratios, including extreme compression.
- Distinguish high-resolution tasks from general perception tasks.
- Compare uniform, top-k, max-based, and aggregate adaptive allocation.
- Compare local-only, global-only, and combined token scores.
- Add the allocation strategy to other methods to test composability.
- Report memory and throughput, including efficient-attention compatibility.
- Visualize masks to show uniform over-compression and positional bias.

### 4.8 Figure roles

- A global-to-local teaser communicates the design philosophy.
- Thumbnail-only versus crop-only results establish complementarity.
- High- versus low-information crop removal establishes task impact.
- Input-order reversal exposes positional bias.
- The method overview separates allocation from selection.
- Token masks show what competing compression rules discard.
- Combination results support composability.

### 4.9 Transferable lesson and risk

Lesson: when the new way of viewing the system is a contribution, put Analysis
before Method and reference each named observation from the matching component.

Risk: attention or similarity is not automatically ground-truth information.
Interventions, task decomposition, architecture variants, stability tests, and
failure examples are needed.

## 5. VidCom2

### 5.1 One-sentence story

Video frames differ in uniqueness, so uniform compression can remove a rare
critical frame while retaining repeated content. Allocate a per-frame budget
from video-level uniqueness, then select tokens using within-frame and
across-video evidence while preserving efficient-operator compatibility.

### 5.2 Narrative archetype

The paper combines heterogeneous allocation with global and local evidence. It
also elevates implementation constraints to the same importance as algorithmic
quality.

### 5.3 Abstract contract

1. Video understanding is effective but token-heavy.
2. Existing compression overlooks frame uniqueness and faces implementation
   constraints.
3. The analysis yields adaptability, frame uniqueness, and operator
   compatibility principles.
4. VidCom2 follows these principles.
5. It allocates frame budgets, then scores tokens within frame and video.
6. Results pair retained performance with generation latency and composability.

### 5.4 Introduction roles

- P1: video token count and long-video cost
- P2: pre-LLM and intra-LLM compression routes
- P3: design myopia, illustrated by redundant versus unique frame removal
- P4: missing class token and explicit-attention operator constraints
- P5: three derived design principles
- P6: two-stage method and human-perception intuition
- P7: analysis, framework, and performance-efficiency contributions

### 5.5 Method logic

`global video representation -> token video uniqueness -> frame uniqueness
density -> per-frame retention -> frame and video token uniqueness -> top-r
selection`

Stage 1 answers how many tokens each frame receives. Stage 2 answers which
tokens fill that budget. The allocation preserves the global average retention
constraint.

### 5.6 Evidence design

- Test multiple VideoLLM architectures.
- Cover short and long video benchmarks.
- Evaluate multiple retention ratios, including aggressive compression.
- Separate performance comparison from system efficiency.
- Report LLM, model, and end-to-end latency, memory, throughput, and overhead.
- Ablate frame-level, video-level, and combined uniqueness.
- Compare uniform and alternative frame aggregation strategies.
- Analyze local windows against global context.
- Add frame allocation to other compression methods.
- State untested large models and streaming video as limitations.

### 5.7 Figure roles

- Redundant-frame versus unique-frame removal creates a task-level teaser.
- A design-principle table distinguishes methods before performance results.
- The overview separates frame allocation from token selection.
- Frame-uniqueness bars connect scores to budget.
- A second model and long-video panel supports generality.
- A practical-efficiency table supports operator compatibility.
- Add-on results support modular value.

### 5.8 Transferable lesson and risk

Lesson: treat algorithmic benefit and system usability as separate gaps, then
verify operator compatibility, memory, and overhead rather than asserting them.

Risk: negative similarity to an average vector is a design proxy, not a truth
definition of uniqueness. Use local, global, and combined ablations, window
analysis, interventions, and human-alignment checks.

## 6. Cross-paper comparison

| Dimension | TaylorSeer | ToCa | GlobalCom2 | VidCom2 |
|---|---|---|---|---|
| decision unit | timestep feature | token and layer | thumbnail, crop, token | frame and token |
| old assumption | past feature can be reused | all units cache equally | single-view compression transfers | frames compress uniformly |
| diagnostic | feature and difference trajectories | redundancy and propagation | complementarity, crop disparity, position bias | frame uniqueness and compatibility |
| principle | forecast future state | cache by sensitivity | global guides local | budget by frame uniqueness |
| method structure | linear to higher-order prediction | four scores plus layer ratios | crop budget plus holistic score | frame budget plus token uniqueness |
| strongest regime | long interval, high acceleration | high cache ratio | extreme high-resolution compression | aggressive and long-video compression |
| mechanism test | order by interval | score, layer, cache heatmap | local, global, combined, reorder | score, window, composability |
| efficiency evidence | latency and FLOPs | latency and FLOPs | memory and throughput | multi-level latency, memory, throughput |

## 7. Transferable writing patterns

### Pattern 1: prove why average treatment is wrong before adapting

ToCa, GlobalCom2, and VidCom2 quantify unit differences before allocating
budgets. Without this probe, an adaptive method may look like an arbitrary
heuristic.

### Pattern 2: make the method the shortest implementation of the observation

- Smooth trajectories motivate forecasting.
- Different error propagation motivates token-wise scoring.
- Different crop information motivates per-crop ratios.
- Different frame uniqueness motivates per-frame ratios.

The method story becomes stronger as the implementation looks inevitable from
the evidence.

### Pattern 3: emphasize the structural stress regime

The papers highlight high acceleration, long cache intervals, very low token
retention, or long videos. Report how the gap changes with problem intensity,
not only the average score.

### Pattern 4: assign one reviewer question to each visual

- teaser: why the problem matters
- diagnostic: why the old approach fails
- overview: how the method acts
- Pareto: whether the trade-off is stronger
- mechanism: whether it acts as intended
- qualitative: which errors improve and remain

### Pattern 5: validate practical efficiency independently

Claims such as training-free, plug-and-play, and operator-compatible require
end-to-end latency, memory, throughput, overhead, hardware, and operator
details. They are not consequences of FLOPs alone.

### Pattern 6: choose transfer axes that test different assumptions

Prefer architecture, task type, input length, and budget transfer. Several
closely related datasets do not substitute for real generality.

## 8. Patterns not to copy mechanically

- Do not force every paper into exactly three contributions.
- Do not invent scores or stages to create a larger-looking method.
- Do not call projections, attention, or cosine similarity causal evidence.
- Do not reuse `plug-and-play`, `almost lossless`, or `state of the art`
  without defining the comparison and uncertainty protocol.
- Do not use one selected example as mechanism evidence.
- Do not apply this empirical efficiency template unchanged to a theory,
  dataset, or qualitative study paper.
