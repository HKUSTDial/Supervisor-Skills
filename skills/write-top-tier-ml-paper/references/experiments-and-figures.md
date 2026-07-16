# Experiment evidence and figure design

## Table of contents

1. Design from reviewer questions
2. Minimum evidence package
3. Experiments by contribution type
4. Fair-comparison protocol
5. Ablation design
6. Efficiency evaluation
7. Main-paper visual storyboard
8. Result-paragraph contract
9. Main paper versus appendix
10. Frequent evidence failures

## 1. Design from reviewer questions

Convert every contribution into a falsifiable claim before choosing a
benchmark.

| Claim type | Reviewer question | Preferred evidence | Insufficient alone |
|---|---|---|---|
| problem | Does the old approach really fail? | distribution, intervention, counterexample, scale curve | one selected example |
| diagnosis | Is the proposed cause correct? | controlled variable, perturbation, high-score versus low-score removal | a better final score |
| effectiveness | Is the method better at equal cost? | multi-budget table, Pareto curve, multiple seeds | comparison only to the original model |
| component | Is each design necessary? | principle-aligned and interaction ablations | full model versus no method |
| efficiency | Is it faster and smaller in practice? | wall-clock, memory, throughput, overhead | FLOPs only |
| generality | Is it a single-setting trick? | architecture, task, scale, and budget transfer | several similar datasets |
| mechanism | Does it work as intended? | intermediate state, allocation, error, or mask visualization | final metrics only |

## 2. Minimum evidence package

An empirical efficiency, compression, or inference-acceleration paper usually
needs the following main-paper evidence:

1. **Failure evidence**: expose the old paradigm's limitation directly.
2. **Main benchmark**: compare with strong baselines over multiple budgets.
3. **Pareto evidence**: show quality against token count, FLOPs, or latency.
4. **Real efficiency**: report end-to-end latency, memory, throughput, and
   added scoring cost.
5. **Component evidence**: test each core design principle.
6. **Mechanism evidence**: show intermediate behavior consistent with the
   motivation.
7. **Generality evidence**: cover at least two meaningful transfer axes.
8. **Qualitative evidence**: organize successes and failures by error type.
9. **Boundary evidence**: show sensitivity, extreme budgets, and a failure
   regime.

Prefer coverage of distinct reviewer questions over many redundant datasets.

## 3. Experiments by contribution type

### Paradigm replacement or forecasting

Use these experiments when the method replaces reuse, holding, or another
zero-order operation with prediction:

- Plot the target trajectory and its first- and higher-order differences.
- Measure prediction error against horizon or cache interval.
- Compare old and new paradigms over the quality-acceleration curve.
- Run an order by interval grid to expose saturation and failure.
- Test whether the theoretical error trend appears in practice.
- Fix refresh positions and real-computation counts when comparing estimators.

### Adaptive budget allocation

Use these experiments when the method allocates computation among tokens,
layers, crops, frames, or timesteps:

- Show that unit importance or risk is non-uniform.
- Compare uniform, random, adaptive, and feasible oracle or upper-bound rules.
- Remove high-score versus low-score units to connect the score to task impact.
- Visualize the final budget distribution and check for starvation.
- Evaluate low, medium, and high budgets to locate the largest benefit.

### Global and local information fusion

- Compare local-only, global-only, and combined scoring.
- Select metrics that separately depend on global context and local detail.
- Visualize how the global signal changes local budgets or masks.
- Reverse crop or token order to test content-agnostic positional bias.

### Plug-and-play or training-free methods

- Apply the method to different architectures and untouched checkpoints.
- State whether hyperparameters transfer without per-model tuning.
- Report training, search, auxiliary-model, and preprocessing costs.
- Test compatibility with efficient attention, quantization, compilation, or
  another inference optimization.
- Add the core component to another method when composability is claimed.

## 4. Fair-comparison protocol

### Align the budget

Choose and justify one or more matching rules:

- equal token retention or equivalent token count
- equal FLOPs or MACs
- equal end-to-end latency
- equal sampling steps or full-computation calls
- equal peak-memory limit

When methods compress at different model locations, a single retention ratio
may be misleading. Add equivalent compute and wall-clock comparisons.

### Fix intervention schedules

Hold checkpoint, input, prompt, seed, resolution, sampler, steps, guidance,
batch, precision, and hardware constant. For caching or forecasting methods,
also fix refresh positions, real-computation calls, and visible history. This
isolates the estimator or allocation rule from a more expensive schedule.

### Select baselines

Include at least:

- the unmodified upper bound
- the simplest naive policy, such as random, uniform, or reduced steps
- the nearest method by mechanism
- the strongest current baseline
- one alternative route at similar cost

### Report uncertainty

Use enough samples and seeds for the metric's variance. Report mean and
standard deviation or confidence intervals when the data permit it. Avoid
calling a difference meaningful when it is smaller than run-to-run variation.

Before using `lossless`, `almost lossless`, or `accuracy-preserving`, define a
non-inferiority margin relative to the unmodified model. Use confidence
intervals or a paired test to determine whether the degradation stays within
that margin. "No observed drop on one benchmark" is not strict losslessness.

## 5. Ablation design

### Test decisions, not switches

Prefer interpretable alternatives:

- uniform versus max-based versus mean- or sum-based allocation
- random versus self-attention versus cross-attention scoring
- local versus global versus combined information
- direct reuse versus linear versus higher-order forecasting
- shared versus depth-aware versus type-aware budgets

### Align ablations with motivations

| Motivation | Ablation | Expected pattern |
|---|---|---|
| unit heterogeneity | uniform versus adaptive | larger gap at low budgets |
| complementary views | local, global, combined | different task strengths, best overall combination |
| long-range nonlinearity | orders 0, 1, 2, 3, 4 | higher order helps at longer intervals, then saturates |
| stale-cache prevention | with versus without frequency control | more balanced allocation and fewer over-cached regions |
| positional bias | normal versus reversed order | content score stays stable while position score changes |

### Test interactions

A component may matter only under aggressive compression. Test at least the
core component by budget interaction so an average does not hide its purpose.

## 6. Efficiency evaluation

Report each metric with a clear user-facing question:

| Metric | Question answered |
|---|---|
| FLOPs or MACs | How much theoretical compute is removed? |
| target-module latency | Does the optimized component run faster? |
| end-to-end latency | Does the user wait less? |
| peak memory | Can a larger model or input run? |
| throughput | Is batch processing faster? |
| scoring or preprocessing overhead | Does adaptation consume the savings? |
| training, search, and parameter cost | Is the method truly plug-and-play? |

State GPU model and count, software environment, precision, batch size, input
length or resolution, warm-up, repetition count, and synchronization method.

Do not conflate:

- FLOPs speedup with latency speedup
- retaining 10 percent of tokens with reducing 10 percent of tokens
- preserving 90 percent of original performance with an absolute score of 90

## 7. Main-paper visual storyboard

### Figure 1: problem and core intuition

Show the shortest path from old operation to failure to new principle. A useful
layout is old method and failure on the left, diagnostic evidence in the
middle, and the new design rule on the right. Do not place the full pipeline in
the teaser.

### Figure 2: diagnostic evidence

Choose one form:

- distribution or heatmap for unit heterogeneity
- trajectory or low-dimensional projection for temporal predictability
- controlled perturbation curve for error propagation
- high-score versus low-score removal for task impact
- normal versus reversed order for position bias

The caption must define the measurement, fixed variables, sample count, and
take-away.

### Figure 3: method overview

Label inputs, decision units, information signals, budget allocation,
selection or prediction action, and outputs. Reuse colors consistently across
the paper. Include only the equations needed to orient the reader.

### Figure 4: Pareto frontier

Use cost on the horizontal axis and task quality on the vertical axis. Connect
multiple budgets from the same method. Mark the unmodified upper bound and
strong matched baselines. Use separate panels for different model families.

### Figure 5: mechanism visualization

Show score maps, masks, frame or crop ratios, cache frequency, prediction
error, or feature differences. The figure must prove that the method changes
the intended behavior, not merely decorate the paper.

### Figure 6: qualitative comparison

Fix inputs, seeds, and layouts. Annotate text errors, missing objects, motion
artifacts, detail loss, or hallucinations. Include a representative method
failure in the appendix if main-paper space is tight.

### Table roles

- **Table 1**: main quality-budget comparison
- **Table 2**: second task or cross-model generality
- **Table 3**: practical efficiency
- **Table 4**: ablation and mechanism

Do not make two tables answer the same question. Use captions and footnotes to
explain unmatched budgets, reproduced values, and incompatible settings.

## 8. Result-paragraph contract

Use four moves:

1. **Take-away**: state the trend.
2. **Evidence**: give a matched comparison and representative numbers.
3. **Stress point**: identify the extreme budget, long input, or high-speed
   regime.
4. **Interpretation**: connect to the design with evidence-bounded language.

Template:

> [Method] forms a stronger quality-cost frontier across the tested budgets.
> At [matched budget], it changes [metric] from A to B relative to [baseline]
> while reducing [end-to-end cost] by C. The advantage increases in [stress
> regime], where the old method's assumption is weakest. This trend is
> consistent with [design principle]; it does not establish behavior in
> [untested setting].

Use `consistent with` or `suggests` when the test is observational. Reserve
`demonstrates` for a direct claim test and `proves` for a valid proof.

## 9. Main paper versus appendix

Keep in the main paper:

- core diagnostic
- method overview
- strongest matched main table
- real efficiency
- key principle-aligned ablation
- one mechanism visual
- representative qualitative result

Move to the appendix:

- complete hyperparameters and algorithms
- full complexity derivations
- additional datasets and models
- complete metric breakdowns
- sensitivity and multiple seeds
- more visualizations and failure cases
- video or interactive links

Never move the only evidence for a core claim or a reproduction-critical
condition to the appendix.

## 10. Frequent evidence failures

- The paper proves that the method works but not that the motivation is right.
- It compares only at the budget that favors the proposed method.
- It uses reduced steps as the only baseline and omits strong same-route work.
- It treats attention or cosine similarity as ground-truth importance without
  an intervention.
- It reports FLOPs but hides ranking, caching, or explicit-attention overhead.
- It reports only relative retention and hides absolute quality loss.
- An ablation gain is below variance but is described as stable.
- Qualitative examples use different seeds or no error taxonomy.
- Several similar benchmarks are presented as architecture generality.
- The Introduction promises real-time, universal, or lossless behavior that
  the experiment scope does not support.
