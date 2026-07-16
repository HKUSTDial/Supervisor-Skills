# Skills: a reader's guide to the twelve executable skills

English · [中文](README.md)

If you clicked into this folder, you probably want to know what the "executable core" of Supervisor-Skills actually is. This README is written for you: **use it as a structured research checklist without the plugin, and as a map to what each skill does, when to trigger it, and how the skills chain together when you do install the plugin.**

## Where this README sits in the project

Supervisor-Skills is layered by audience:

| Entry point | Audience | Purpose |
|---|---|---|
| Top-level [`README.en.md`](../README.en.md) | First-time visitors | Why the project exists, tutorial structure, how to install |
| [`handbook/`](../handbook/) (Chinese, canonical) / [`handbook-en/`](../handbook-en/) (English mirror) | Readers who want the methodology | Six chapters of research and writing handbook (the theoretical spine) |
| **This file** | Readers who want the skills directly | **What each of the 12 skills is, when to use it, how it chains with the others** |
| `SKILL.md` (inside each skill directory) | The plugin / LLMs | Executable spec: integrity gates, output formats, mode options — machine-readable, not optimised for human browsing |

In one line: **the handbook teaches the way, SKILL.md runs the tool, this README is the bridge between them.**

## Two narrative tracks: technical paper vs benchmark paper

The twelve skills are not isolated tools. They map to two complete lifecycles of a top-venue paper and add survey-grade research, evidence-gated argument planning, drafting and polishing, and an execution-oriented Draw.io reconstruction capability. Locate yourself on the right track first, then pick the skill you need.

### Track 1: technical / position paper (new method for an existing problem)

Following the natural order a PhD student takes for their first top-venue paper:

1. **[idea-evaluator](idea-evaluator/SKILL.md)** — before committing months to an idea, run the reviewer-grade vetting; cut weak ideas early and sharpen the promising ones
2. **[tech-paper-template](tech-paper-template/SKILL.md)** — before writing any prose, lock the full logical skeleton of the paper
3. **[write-top-tier-ml-paper](write-top-tier-ml-paper/SKILL.md)** — map observations, principles, components, claims, experiments, and figures into a reviewer-auditable evidence plan
4. **[intro-drafter](intro-drafter/SKILL.md)** — write the skeleton straight into six paragraphs of Introduction prose with retrieval-verified citations (outline mode on request)
5. **[paper-writer](paper-writer/SKILL.md)** — evidence-gated drafting for every other section, from one paragraph to the full manuscript, with nothing fabricated
6. **[figure-designer](figure-designer/SKILL.md)** — design the three load-bearing figures: Motivated Example, Solution Overview, Experimental Results
7. **[drawio-reconstruction](drawio-reconstruction/SKILL.md)** — when a reference image, draft, or screenshot already exists, rebuild it as editable Draw.io
8. **[paper-polish](paper-polish/SKILL.md)** — meaning-preserving language polish: AI-tone removal, claim calibration, Chinese-to-English rewriting
9. **[pre-submission-reviewer](pre-submission-reviewer/SKILL.md)** — the 3-to-5-day deadline-window audit

**Two cross-cutting tools**, orthogonal to the nine steps above:

- [deep-research](deep-research/SKILL.md) — survey-grade literature investigation, usable before topic selection or at any point while writing: multi-perspective search, per-citation verification, a report that answers explicit research questions
- [vibe-research-workflow](vibe-research-workflow/SKILL.md) — whether you are coding, drawing, or writing at any stage, it gives you AI-collaboration rules and tool picks

### Track 2: benchmark / evaluation paper

The benchmark pipeline is more strictly sequential than the technical-paper track: each stage gates the next. **[benchmark-paper-template](benchmark-paper-template/SKILL.md)** is the orchestrator for this track: a single skill bundles the full six-stage workflow (Gap → Design → Construction → Experiments → Paper Structure → Checklist) and produces the five-pillar framework (Research Gap, Construction Pipeline, Evaluation Framework, Empirical Findings, optional Companion Method).

For a benchmark paper, the starting and ending point are both this one skill; the two core figures additionally need figure-designer, existing reference images or screenshots can be executed with drawio-reconstruction, and the pre-submission audit still lands on pre-submission-reviewer.

### Already stuck somewhere?

Readers with a specific bottleneck can skip the reading order and jump straight to the relevant skill:
- No concrete idea yet, need the lay of the land first → **deep-research**
- Not confident about greenlighting an idea → **idea-evaluator**
- Introduction reads like a set of disconnected claims, or you want the Intro prose directly → **intro-drafter**
- Methodology section will not flow → **tech-paper-template**
- The skeleton exists, but contributions, experiments, and figures do not form a defensible evidence loop → **write-top-tier-ml-paper**
- Idea and results in hand, want a section written → **paper-writer**
- Prose is stiff, AI-flavored, or a Chinese draft needs submission English → **paper-polish**
- Figures look clumsy, not sure which tool to use → **figure-designer**
- Have a reference figure, paper figure, architecture diagram, or screenshot and need editable Draw.io → **drawio-reconstruction**
- Pre-submission panic, unclear what to check → **pre-submission-reviewer**
- Cannot articulate the benchmark gap or organise evaluation dimensions → **benchmark-paper-template**
- Unsure how to delegate to AI without diluting academic judgment → **vibe-research-workflow**

## The twelve skill cards

Each card translates the SKILL.md spec into plain-reader language, adds the matching handbook chapters, and notes the upstream/downstream skills.

### idea-evaluator — pre-submission vetting for your idea

- **Positioning**: externalises the implicit check that experienced advisors run silently when a student proposes an idea, into four layers of reviewable gates.
- **When to trigger**:
  - Student proposes an idea and wants to know, before committing months, whether it is worth pursuing
  - Reviewer-style self-audit: is this already covered by prior work; does it land cleanly on Higher / Faster / Stronger / Cheaper / Broader; does the student's capability and timeline fit
  - Rough-filter a list of ideas, keep the top three, cut the rest
- **Four layers**: fatal-flaws audit (early short-circuit) → idea lifecycle and student capability matching → five-dimension scoring (Higher, Faster, Stronger, Cheaper, Broader) → paradigm-shift probe plus feasibility. The order matters — a seven-out-of-ten "Higher" score means nothing if a CRITICAL fatal flaw is sitting underneath it.
- **Output**: evidence-grounded scores on every axis, severity tagging (CRITICAL / MAJOR / MINOR), and a verdict of "Reject and Pivot" or "Proceed with Guardrails".
- **Matching handbook chapters**: [2.1 Idea lifecycle](../handbook-en/02_Idea_Generation/2.1_idea-lifecycle-and-capability-matching.md) · [2.2 Higher-Faster-Stronger](../handbook-en/02_Idea_Generation/2.2_higher-faster-stronger.md) · [2.3 Disruptive innovation](../handbook-en/02_Idea_Generation/2.3_disruptive-innovation.md)
- **Downstream**: once the idea passes, hand off to **tech-paper-template** to lock the skeleton. When the paradigm probe flags disruptive potential, read handbook 2.3 first.

### deep-research — survey-grade literature investigation

- **Positioning**: investigates a research direction the way a real survey paper is written: freeze two or three explicit research questions, search independently from three to five perspectives (mainstream, critics, adjacent fields, methodology, application and policy), verify every citation, synthesize into a MECE taxonomy with in-sentence cross-comparison, and answer the research questions one by one.
- **When to trigger**:
  - No concrete idea yet; you need the field's key works, debates, and gaps mapped first
  - idea-evaluator or a drafting skill reveals the literature map is missing
  - You need a reliable, judgment-bearing survey report, not a list of search results
- **Key discipline**: zero tolerance for invented citations (grey zone means unused); contradictions presented with condition analysis, never averaged; claim strength capped by evidence strength; six internal quality gates (angle, coverage, citation, taxonomy, calibration, weaving) send failures back for targeted re-scouting.
- **Output**: a survey-structured report: abstract, research questions, methodology, taxonomy, branch analyses with comparison tables, cross-branch synthesis, open problems, conclusions answering each RQ, verified references.
- **Downstream**: **idea-evaluator** (evaluate a specific idea once the landscape is clear) or **paper-writer** (the literature pool for Related Work).

### tech-paper-template — the logical skeleton before you write

- **Positioning**: forces alignment across Background, Limitations, Key Idea / Goal, Challenges, Methodology Modules, and Contributions, via a thinking-template table.
- **When to trigger**:
  - The idea has passed evaluation; before any prose, you want the story straight
  - Co-authors disagree on whether module X belongs — let the table arbitrate
  - Halfway through drafting you notice the method does not actually respond to the motivation — come back to the table and reshuffle
- **Key discipline**: choose the paper's **positioning type** once (technical / position paper vs new-problem / new-setting paper); enforce the challenge-to-module one-to-one mapping with at most three entries; every contribution bullet must cite the section that delivers it.
- **Output**: a completed thinking-template table + self-consistency audit (the "challenge—module—contribution" three-way interlock) + structured input ready for intro-drafter.
- **Matching handbook chapters**: [3.1 Essentials of a research paper](../handbook-en/03_Paper_Writing/3.1_the-essentials-of-a-research-paper.md) · [3.3 Technical paper template](../handbook-en/03_Paper_Writing/3.3_technical-paper-template.md)
- **Up- and downstream**: upstream is **idea-evaluator**; downstream is **write-top-tier-ml-paper** when the contribution-evidence plan needs a stress test, then **intro-drafter** and **figure-designer**.

### write-top-tier-ml-paper — the claim-evidence architect

- **Positioning**: turns a technical-paper skeleton or partial result set into a reviewer-auditable argument. It connects diagnostic observations to design principles, method components, bounded contributions, experiments, and main-paper figures.
- **When to trigger**:
  - The paper reads like a list of modules rather than one coherent argument
  - Introduction claims, method sections, and experiments do not align
  - You need a paragraph-level plan for what every section should prove
  - Claims such as lossless, general, plug-and-play, or mechanism-grounded need evidence calibration
- **Key discipline**: every contribution enters a claim-evidence ledger; every component must follow from an observation or constraint; experiments are selected by reviewer question rather than benchmark availability; unsupported claims are weakened instead of decorated.
- **Output**: a research spine, bounded contribution list, claim-evidence matrix, section-by-section and paragraph-by-paragraph blueprint, prioritized experiment plan, figure and table storyboard, and dangerous reviewer questions.
- **Source basis**: an original structural synthesis of TaylorSeer, ToCa, GlobalCom2, and VidCom2, with the four arXiv sources attributed in the skill. The papers are writing case studies, not prose templates or acceptance evidence.
- **Up- and downstream**: upstream is **tech-paper-template**; downstream is **intro-drafter**, **paper-writer**, and **figure-designer** once the evidence plan closes.

### intro-drafter — six paragraphs of Introduction prose

- **Positioning**: uses the six-paragraph flowchart (Background, Limitations, Goal, Challenges, Solution Overview, Contributions) as an **internal scaffold** and delivers six paragraphs of flowing Introduction prose; the five cross-paragraph chains are checked silently before writing, and no scaffolding appears in the output.
- **When to trigger**:
  - The tech-paper-template skeleton is done; you want the Introduction written
  - You have a paragraph of research thinking and want finished prose, not bullets
  - You only want the skeleton: say "just the outline" and the classic outline mode returns
- **Key discipline**: search before writing (a full Introduction typically weaves 15-25 verified references); running examples are never fabricated (absent a real case from the user, the background paragraph stays abstract and the closing note asks for one); the shared evidence discipline with paper-writer applies (zero placeholder tags, no invented specifics).
- **Output**: six paragraphs of Introduction prose + a References list matched bidirectionally + at most three lines of closing notes.
- **Matching handbook chapter**: [3.2 Introduction writing flowchart](../handbook-en/03_Paper_Writing/3.2_introduction-writing-flowchart.md)
- **Up- and downstream**: upstream is **tech-paper-template** and, when evidence alignment is needed, **write-top-tier-ml-paper**; downstream is **figure-designer** and **paper-writer**.

### paper-writer — evidence-gated paper drafting

- **Positioning**: turns ideas and materials into submittable paper prose, one paragraph or a full manuscript; every written word must trace to evidence. The substance (ideas, designs, results, conclusions) belongs to the author; the skill owns only its linguistic realization.
- **When to trigger**:
  - "Write this idea into a Discussion / Methods / Related Work paragraph"
  - "Draft the full first version of the paper" (STEM Introductions route to intro-drafter automatically)
  - Non-STEM sections (humanities, social science, economics, law), planned paragraph by paragraph on a CER skeleton
- **Key discipline**: factual claims have exactly three legitimate origins (user materials, this session's verified retrieval, or field common knowledge with no numbers, names, or comparisons), never model memory; zero placeholder tags, the only resolution path is search, rewrite, or delete; full papers, final mode, or three-plus citations trigger the **independent citation verification** (a fresh-context sub-agent checks every entry, with honest degradation and disclosure when the environment lacks sub-agents).
- **Output**: clean section or manuscript prose + a bidirectionally matched References list + at most three lines of notes; full-paper runs keep an evidence map and chapter blueprint as separate working files.
- **Matching handbook chapters**: [3.1 Essentials](../handbook-en/03_Paper_Writing/3.1_the-essentials-of-a-research-paper.md) · [3.3 Technical paper template](../handbook-en/03_Paper_Writing/3.3_technical-paper-template.md) · [3.5 Writing details](../handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md)
- **Up- and downstream**: upstream is **tech-paper-template**, **write-top-tier-ml-paper** (claim-evidence plan), and **intro-drafter**; downstream is **paper-polish** and **pre-submission-reviewer**.

### benchmark-paper-template — the all-in-one orchestrator for benchmark papers

- **Positioning**: built specifically for benchmark / evaluation papers; bundles the five-pillar framework (Research Gap, Construction Pipeline, Evaluation Framework, Empirical Findings, optional Companion Method) plus the six-stage workflow into a single skill.
- **When to trigger**:
  - Starting a benchmark project, thinking from "why does this benchmark need to exist"
  - Data has been collected, but the evaluation dimensions are fuzzy
  - Experiments are done; unclear whether each Finding-X insight is deep enough
  - Working through the benchmark-paper checklist before submission
- **Six stages**: Gap Analysis → Design → Construction Pipeline → Experiments → Paper Structure → Checklist. The skill **first detects the current stage**, then routes to the relevant thinking support.
- **Output**: per-stage deliverables + a six-part Introduction logic chain + a Section 2-7 skeleton + a pre-submission checklist.
- **Matching handbook chapters**: [3.4 Benchmark and evaluation paper template](../handbook-en/03_Paper_Writing/3.4_benchmark-paper-template.md) · [6.3 LEAD writing analysis](../handbook-en/06_Case_Studies/6.3_vldb2026-lead-analysis.md)
- **Cross-link**: figure-designer (the two core figures) · pre-submission-reviewer (final audit).

### figure-designer — the design advisor for the three load-bearing figures

- **Positioning**: focuses on the three figures that carry the narrative weight of a technical paper — Motivated Example (Figure 1), Solution Overview (methodology), and Experimental Results — with design paradigms, layout rules, and tool-selection guidance.
- **When to trigger**:
  - Introduction outline is locked; you need to turn paragraph 1's Running Example into Figure 1
  - Before writing the methodology, decide how the Solution Overview figure should partition the module graph
  - Experiments are done, the main table is crowded, and a figure would tell the story better
  - Torn between PowerPoint, TikZ, and Inkscape
- **Key principles**: one figure says one thing; axis / legend / palette at top-venue aesthetic standards; the Experimental Results figure must speak directly back to the Introduction's motivation.
- **Output**: per-figure design notes, common anti-patterns, tool picks, and reusable layout templates.
- **Matching handbook chapters**: [4.1 Motivated example figure](../handbook-en/04_Scientific_Plotting/4.1_motivated-example-figure.md) · [4.2 Solution overview figure](../handbook-en/04_Scientific_Plotting/4.2_solution-overview-figure.md) · [4.3 Experimental results figure](../handbook-en/04_Scientific_Plotting/4.3_experimental-results-figure.md) · [4.4 Plotting checklist](../handbook-en/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md)
- **Up- and downstream**: upstream is **intro-drafter** (running example locks Figure 1) and **tech-paper-template** (module graph locks the Solution Overview figure); downstream is **pre-submission-reviewer** (figure quality is part of the final audit).

### drawio-reconstruction — rebuild reference figures as editable Draw.io

- **Positioning**: an execution-oriented figure skill that reconstructs reference images, paper figures, architecture diagrams, slide diagrams, UI screenshots, or image folders into `.drawio` files with PNG previews and audit notes.
- **When to trigger**:
  - A target-style reference image already exists and the user needs an editable Draw.io version
  - Multiple figures need batch reconstruction into `.drawio`, each with visual-consistency checks
  - Text and structure should stay editable, while complex icons, screenshots, visual metaphors, and dense artwork should use faithful crops or transparent PNGs
- **Key discipline**: visual fidelity beats semantic approximation; script checks only prove XML and export validity, while final quality requires visual comparison against the reference.
- **Output**: `.drawio` source files, PNG previews, audit files for complex or batch tasks, and explicit notes for unresolved visual differences.
- **Attribution and license**: adapted from [drawio-reconstruction-skill](https://github.com/sxy1499894281/drawio-reconstruction-skill), retaining the MIT License.
- **Up- and downstream**: upstream can be a **figure-designer** plan or any user-provided reference image; downstream is **pre-submission-reviewer** for figure-quality review.

### paper-polish — meaning-preserving language polish

- **Positioning**: helps the author say **what the author means**, better, instead of replacing it with what the editor would have said. Grammar, word order, AI-tone removal, claim calibration, and Chinese-to-English rewriting at submission quality.
- **When to trigger**:
  - "Polish this passage / make it sound natural / strip the AI flavor"
  - "I wrote this in Chinese; turn it into submission-ready English"
  - "Is this claim too strong?"
- **Key discipline**: no edit that might change scientific meaning is ever made silently; such edits ship as a before/after list for the author to confirm; nothing absent from the original is added (no data, equations, citations, or mechanisms); conservative by default; when working on files, the edits land in the files and the version diff is the change record.
- **Output**: clean polished prose + three to five change notes, meaning-risk items listed side by side.
- **Matching handbook chapter**: [3.5 Writing details and checklist](../handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md)
- **Up- and downstream**: upstream is **paper-writer** / **intro-drafter** (drafts to polish); problems beyond language (broken logic, a doubtful core claim) route to **paper-writer** for redrafting or **pre-submission-reviewer** for a verdict.

### pre-submission-reviewer — the top-venue reviewer's final audit

- **Positioning**: simulates a top-venue reviewer and audits a draft across five dimensions: macro logic, writing details, English grammar, LaTeX formatting, figure quality.
- **When to trigger**:
  - 3 to 5 days before the submission deadline, running the final pass
  - Co-authors have stopped making suggestions; you need a cold-eyed full audit
  - Rebuttal is drafted; you want another sweep against the "things reviewers will flag" catalogue
- **Methodology**: severity tagging (CRITICAL / MAJOR / MINOR) + reviewer-style writing checklist + high-frequency English pitfalls + common LaTeX formatting mistakes.
- **Output**: a severity-ranked defect list, each item paired with an actionable fix, with a clear **subset that is realistically fixable in 72 hours** called out.
- **Matching handbook chapters**: [3.5 Writing details and checklist](../handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md) · [1.1 How to evaluate paper quality](../handbook-en/01_Preliminary/1.1_how-to-evaluate-paper-quality.md)
- **Upstream**: the endpoint of the technical-paper track; also the endpoint of the benchmark-paper track.

### vibe-research-workflow — the always-on rules for AI-assisted research

- **Positioning**: a full-lifecycle guide for AI-assisted research, covering three sub-flows: Vibe Coding, Vibe Figure, Vibe Writing.
- **When to trigger**:
  - First time using Claude / Cursor / Codex to help with research code, unclear where the human-AI boundary is
  - Drawing a figure and torn between "let AI generate it" and "draw it yourself"
  - Worried the LLM is ghost-writing away your academic taste
  - The output feels like "the AI is winging it" — usually the behavioural rules are not aligned
- **Core principle**: **keep academic judgment in the human's hands, delegate mechanical labour to AI**; every AI output must come with checkable evidence; tool picks are per task type with a concrete shortlist.
- **Output**: a recommended tool chain for the current scenario, a human-AI division-of-labour sketch, and a common-failure-mode catalogue.
- **Matching handbook chapters**: [5.1 Vibe Research and Vibe Coding primer](../handbook-en/05_Vibe_Research/5.1_vibe-research-and-vibe-coding.md) · [5.2 Practitioner notes](../handbook-en/05_Vibe_Research/5.2_liboyan-practical-notes.md)
- **How it fits**: **orthogonal** to the other eleven skills. It is not step N; it is a rulebook you pull up at any step. Drafting requests are legitimate: they route to paper-writer / intro-drafter, whose evidence discipline forbids fabricated substance; disclosure and per-passage verification duties stay with the author.

## How to actually use these skills

### With the Claude plugin installed (recommended)

Follow the [Quick Start](../README.en.md#quick-start) in the top-level README. Once installed, natural language triggers are enough, no commands to memorise. The following phrasings route to the matching skill:

- "survey this direction for me / literature review" → `deep-research`
- "help me evaluate this idea" → `idea-evaluator`
- "lock the paper's logical skeleton for me" → `tech-paper-template`
- "turn my claims and results into a reviewer-auditable paper plan" → `write-top-tier-ml-paper`
- "draft the Introduction / I want to write the intro" → `intro-drafter`
- "write this idea into a Discussion / draft the paper" → `paper-writer`
- "polish this / strip the AI flavor / turn my Chinese draft into submission English" → `paper-polish`
- "how should I draw this figure / what tool should I use" → `figure-designer`
- "rebuild this reference image as draw.io / generate editable drawio" → `drawio-reconstruction`
- "review the paper before I submit / final pass" → `pre-submission-reviewer`
- "I am writing a benchmark paper / I am doing an evaluation paper" → `benchmark-paper-template`
- "how do I use AI to assist my research" → `vibe-research-workflow`

### Without the plugin

Every `SKILL.md` is itself a readable, structured thinking checklist. You can:
- Paste SKILL.md into any AI assistant you use (Claude, GPT, DeepSeek, Kimi, and similar) as a system prompt
- Or treat it as a **static checklist** — no AI needed; pen, paper, and the section list are enough

Each skill's `references/` directory carries on-demand depth. For example, `idea-evaluator/references/five-dimensions.md` is the full expansion of the Higher-Faster-Stronger-Cheaper-Broader framework.

## Skill-to-handbook cross reference

| Skill | Main handbook chapters |
|---|---|
| deep-research | 2.1 (pre-topic reconnaissance; largely new research-side capability) |
| idea-evaluator | 2.1 / 2.2 / 2.3 |
| tech-paper-template | 3.1 / 3.3 |
| write-top-tier-ml-paper | 3.1 / 3.3 / 3.5 plus four attributed arXiv case studies |
| intro-drafter | 3.2 |
| paper-writer | 3.1 / 3.3 / 3.5 |
| paper-polish | 3.5 |
| benchmark-paper-template | 3.4 / 6.3 |
| figure-designer | 4.1 / 4.2 / 4.3 / 4.4 |
| drawio-reconstruction | 4.4 / VCG-Bench |
| pre-submission-reviewer | 3.5 / 1.1 |
| vibe-research-workflow | 5.1 / 5.2 |

**Recommended reading order: read the handbook once to build intuition about the "way", then come back to this README to pick the skill for your scenario; leave execution to SKILL.md.**

## Contributing and feedback

New skills, SKILL.md revisions, reference additions, or top-venue papers you wrote with these skills are all welcome. Please read the top-level [CONTRIBUTING.md](../CONTRIBUTING.md) first; the hard rules for new skills live there.

For questions, feedback, or to bring Supervisor-Skills to your own lab, please email Yuyu Luo at yuyuluo [AT] hkust-gz.edu.cn.

---

[English] | [中文](README.md)
