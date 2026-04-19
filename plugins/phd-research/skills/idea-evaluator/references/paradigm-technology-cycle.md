# Technology Cycle Foresight

## Table of contents

1. Core idea
2. Technique A: hardware or platform shift adoption
3. Technique B: unlimited-resource thought experiment
4. Worked example: non-volatile memory databases
5. Worked example: free-token large language models
6. How to tell a real shift from hype

## 1. Core idea

Disruptive innovation often coincides with a generational shift in
the underlying hardware or platform. The wrong response to such a
shift is to port the old algorithms onto the new hardware. The right
response is to ask what architectural assumption the shift
invalidates, and design from scratch for a world where that
assumption no longer holds.

The method has two working techniques: watch for the shift that has
just happened, and imagine the shift that would happen if resources
became unbounded.

## 2. Technique A: hardware or platform shift adoption

### Procedure

1. Identify two or three technology shifts in the last 18 months
   that touch the subfield. Shifts can be hardware (GPU, NVM, RDMA),
   software (foundation models, serverless), or cost-curve
   (inference cost, storage cost).
2. For each shift, list the architectural assumptions it changes.
3. For each assumption, ask: does the current best method in the
   subfield still depend on this assumption?
4. If yes, the current method is due for a paradigm refresh. Propose
   a redesign that treats the shift as the new baseline.

### Signals a shift is generational

- Cost curve changes by an order of magnitude, not a factor.
- New capability emerges that was impossible before (not just more
  of the same).
- Production deployments start adopting the shift before academia
  publishes on it.
- At least two major vendors or open-source projects converge on the
  new technology.

## 3. Technique B: unlimited-resource thought experiment

### Procedure

1. Pick a specific resource: compute, memory, bandwidth, inference
   tokens, annotation budget.
2. Imagine the resource becoming 10000 times cheaper at zero latency.
3. Ask: how does the subfield's dominant paradigm change?
4. Look for the design decisions in current paradigms that only make
   sense because that resource was expensive.
5. Propose a reframing that treats the resource as free.

### What this surfaces

- Algorithms that exist only to save the now-abundant resource.
- Pipeline stages that exist only to compress intermediate data.
- Carefully engineered features that exist only because learning
  from raw input was prohibitive.

The classic precedent: deep learning's explosion after GPUs made
abundant compute available. Feature engineering, which was once
central, became peripheral.

## 4. Worked example: non-volatile memory databases

- **Shift**: byte-addressable non-volatile memory (NVM) arrives;
  storage is now persistent and byte-level addressable at near-DRAM
  speeds.
- **Port approach (wrong)**: run traditional disk-oriented databases
  on NVM with minor tuning.
- **First-principles approach (right)**: if storage is persistent and
  byte-addressable, does the database still need a Buffer Pool? Does
  it still need Write-Ahead Logging in its traditional form?
- **Reframing**: a new generation of databases designed for
  persistent memory, collapsing the page-based I/O model and
  rethinking crash recovery.

## 5. Worked example: free-token large language models

- **Thought experiment**: assume LLM tokens cost nothing and context
  windows are unbounded. What changes in data processing?
- **Consequences**:
  - Pre-processing pipelines that exist to fit data into limited
    context become unnecessary.
  - Fine-tuning becomes optional; prompting can absorb the role
    played by fine-tuning datasets.
  - Retrieval systems become simpler; the model can just read the
    corpus.
  - Evaluation pipelines can become interactive rather than batch.
- **Reframing**: research on unified, prompt-first data analysis
  frameworks; agent-driven analysis where the agent reads the whole
  corpus.

## 6. How to tell a real shift from hype

- **Real shift**: cost curve has actually moved; production systems
  have deployed the new capability for at least six months; multiple
  independent teams are exploring it.
- **Hype**: cost curve has moved in one vendor's roadmap slides;
  production systems have tried and reverted; exploration is
  concentrated in a single research group.
- **Premature shift**: the capability exists but at scale that only
  very large labs can access. Reframing is valid on paper but
  unpublishable by a typical student without institutional backing.
  Record on the Hamming's list.
- **Late shift**: the shift happened three or more years ago and the
  subfield has already absorbed it. Reframing opportunity is closed;
  focus on incremental gains within the new paradigm instead.
