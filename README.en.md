<div align="center">

<img src="assets/images/icon-example.png" alt="Supervisor-Skills" height="140" />

</div>

# Supervisor-Skills: Ten years of PhD-advisor research experience distilled into directly-callable AI skills. From ideation to submission, your always-on AI research co-advisor.

English · [中文](README.md)

## Why this project?

Many graduate students hit the same pain points when they first step into research:

- They have read plenty of "research primers", yet still do not know how to start on their own topic.
- Their advisor is busy and cannot sit with every idea on the spot.
- Once the paper is drafted, they are unsure whether the logic flows, whether the figures meet top-venue aesthetics, or whether a "rookie mistake" is hiding in the text.

This is the **Last Mile Problem** of the Vibe Research era.

We distilled ten years of research and writing experience from the Data+AI area (SIGMOD, VLDB, ICML, NeurIPS, and similar venues) into structured **Research Skills** that large language models (Claude, DeepSeek, etc.) can directly read and execute.

This repository is not only a **theory guide**; it is an early attempt in the agent era to turn the **tacit knowledge and writing habits** of senior advisors and top-venue reviewers into **directly-callable AI Skills**.
**Let AI become your always-on research co-advisor!**

## Repository layout

The curriculum follows a dual-track architecture: **Guide (theory) + Skills (executable AI skills)**.

```
Supervisor-Skills/
├── README.md                          # Chinese root README
├── README.en.md                       # this file
│
├── handbook/                          # 📖 research-and-writing handbook (Chinese, canonical)
│   ├── 01_Preliminary/                # Chapter 1: macro perspective
│   │   ├── 1.1_如何评价一篇论文的质量.md
│   │   └── 博士生科研入门辅导_2023年8月.pdf   # 📄 companion slides
│   ├── 02_Idea_Generation/            # Chapter 2: idea generation
│   │   ├── 2.1_Idea的生命周期与能力匹配.md
│   │   ├── 2.2_想Idea的思路_更高更快更强.md
│   │   └── 2.3_进阶_如何做颠覆式创新.md
│   ├── 03_Paper_Writing/              # Chapter 3: paper writing
│   │   ├── 3.1_完成一篇科研论文你需要做几件事情.md
│   │   ├── 3.2_Introduction写作的思考模型.md
│   │   ├── 3.3_技术类Full_Paper思考模板.md
│   │   ├── 3.4_Benchmark与Evaluation类论文思考模板.md
│   │   └── 3.5_写作细节与Checklist.md
│   ├── 04_Scientific_Plotting/        # Chapter 4: scientific plotting
│   │   ├── 4.1_Motivated_Example_Figure.md
│   │   ├── 4.2_Solution_Overview_Figure.md
│   │   ├── 4.3_Experimental_Results_Figure.md
│   │   └── 4.4_绘图Checklist与工具速查表.md
│   ├── 05_Vibe_Research/              # Chapter 5: Vibe Research in practice
│   │   ├── 5.1_Vibe_Research与Vibe_Coding入门.md
│   │   └── 5.2_李伯岩实战经验分享与会议纪要.md
│   └── 06_Case_Studies/               # Chapter 6: top-venue case studies
│       ├── 6.1_ICML_2025_Alpha-SQL写作剖析.md
│       ├── 6.2_ICLR_2025_AFlow写作剖析.md
│       └── 6.3_VLDB_2026_LEAD写作剖析.md
│
├── docs/en/handbook/                  # 📖 English mirror of the handbook
│
├── plugins/phd-research/skills/       # 🛠️ seven executable AI Skills
│   ├── idea-evaluator/                # multi-dimension idea evaluation
│   ├── vibe-research-workflow/        # AI-assisted research workflow
│   ├── intro-drafter/                 # Introduction drafting
│   ├── tech-paper-template/           # technical-paper logical skeleton
│   ├── benchmark-paper-template/      # benchmark-paper logical skeleton
│   ├── figure-designer/               # design of the three core figures
│   └── pre-submission-reviewer/       # reviewer-style pre-submission audit
│
└── assets/images/                     # figures shared by the handbook
```

### 📖 handbook: research-and-writing system guide

> **📄 Companion slides**: [博士生科研入门辅导.pdf](handbook/01_Preliminary/博士生科研入门辅导_2023年8月.pdf) — a printable PDF of the introductory lecture, optimized for an iPad or paper handout.

The handbook preserves the systematic theoretical framework for deep reading. Mastering the *way* makes the *tool* much sharper.

| Chapter | Content | English mirror |
|---|---|---|
| **Chapter 1: Macro perspective** | Evaluating paper quality from a reviewer's perspective (Novel Problem, Novel Method, Nice Story, Nice Presentation) | [1.1 How to evaluate paper quality](docs/en/handbook/01_Preliminary/1.1_how-to-evaluate-paper-quality.md) |
| **Chapter 2: Idea generation** | Idea lifecycle, five-dimension thinking (Higher / Faster / Stronger / Cheaper / Broader), disruptive innovation | [2.1 Idea lifecycle](docs/en/handbook/02_Idea_Generation/2.1_idea-lifecycle-and-capability-matching.md) / [2.2 Higher-faster-stronger](docs/en/handbook/02_Idea_Generation/2.2_higher-faster-stronger.md) / [2.3 Disruptive innovation](docs/en/handbook/02_Idea_Generation/2.3_disruptive-innovation.md) |
| **Chapter 3: Paper writing** | Full paper lifecycle, Introduction flowchart, technical / benchmark paper templates, writing checklist | [3.1 Essentials](docs/en/handbook/03_Paper_Writing/3.1_the-essentials-of-a-research-paper.md) / [3.2 Intro flowchart](docs/en/handbook/03_Paper_Writing/3.2_introduction-writing-flowchart.md) / [3.3 Technical template](docs/en/handbook/03_Paper_Writing/3.3_technical-paper-template.md) / [3.4 Benchmark template](docs/en/handbook/03_Paper_Writing/3.4_benchmark-paper-template.md) / [3.5 Writing checklist](docs/en/handbook/03_Paper_Writing/3.5_writing-details-and-checklist.md) |
| **Chapter 4: Scientific plotting** | Motivated / overview / results figures and a drawing checklist | [4.1 Motivated example](docs/en/handbook/04_Scientific_Plotting/4.1_motivated-example-figure.md) / [4.2 Solution overview](docs/en/handbook/04_Scientific_Plotting/4.2_solution-overview-figure.md) / [4.3 Experimental results](docs/en/handbook/04_Scientific_Plotting/4.3_experimental-results-figure.md) / [4.4 Checklist](docs/en/handbook/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md) |
| **Chapter 5: Vibe Research** | Vibe Research / Coding / Figure / Writing in practice | [5.1 Intro](docs/en/handbook/05_Vibe_Research/5.1_vibe-research-and-vibe-coding.md) / [5.2 Practitioner notes](docs/en/handbook/05_Vibe_Research/5.2_liboyan-practical-notes.md) |
| **Chapter 6: Top-venue case studies** | Alpha-SQL (ICML'25), AFlow (ICLR'25), LEAD (VLDB'26) Introduction analyses | [6.1 Alpha-SQL](docs/en/handbook/06_Case_Studies/6.1_icml2025-alpha-sql-analysis.md) / [6.2 AFlow](docs/en/handbook/06_Case_Studies/6.2_iclr2025-aflow-analysis.md) / [6.3 LEAD](docs/en/handbook/06_Case_Studies/6.3_vldb2026-lead-analysis.md) |

The Chinese originals live at [`handbook/`](handbook/) with the same chapter structure.

### 🛠️ plugins/phd-research/skills: executable AI Skills

The core of this repository. The theoretical experience above is distilled into structured Prompt / Skill files. Install the whole repository as an MCP plugin into any MCP-aware AI client (Claude Code, Cursor, Codex, etc.), or open a specific SKILL.md and hand its content to a general-purpose LLM (Claude, DeepSeek, Kimi, etc.).

| Skill | What it does | Link |
|---|---|---|
| **Idea Evaluator** | Given your idea, scores it on the five-dimension framework (Higher / Faster / Stronger / Cheaper / Broader) plus lifecycle-capability matching, fatal-flaws audit, and paradigm-shift probing. | [Use skill](plugins/phd-research/skills/idea-evaluator/SKILL.md) |
| **Vibe Research Workflow** | End-to-end AI-assisted research guidance covering Vibe Coding, Vibe Figure, and Vibe Writing, together with six behavioural rules. | [Use skill](plugins/phd-research/skills/vibe-research-workflow/SKILL.md) |
| **Introduction Drafter** | Given a structured research motivation, generates a six-paragraph Introduction outline following the flowchart. | [Use skill](plugins/phd-research/skills/intro-drafter/SKILL.md) |
| **Tech Paper Template** | Technical-paper thinking template that walks you through the full logical chain, with four consistency checks. | [Use skill](plugins/phd-research/skills/tech-paper-template/SKILL.md) |
| **Benchmark Paper Template** | Companion template for benchmark / evaluation papers, covering the evaluation framework and experimental design. | [Use skill](plugins/phd-research/skills/benchmark-paper-template/SKILL.md) |
| **Pre-Submission Reviewer** | Reviewer-style pre-submission audit based on the writing checklist and common grammar pitfalls. | [Use skill](plugins/phd-research/skills/pre-submission-reviewer/SKILL.md) |
| **Figure Designer** | Tell the AI what you want to express; it returns a design recommendation based on the motivated / overview / results paradigms. | [Use skill](plugins/phd-research/skills/figure-designer/SKILL.md) |

## Quick start

Paste the following prompt into any MCP-aware AI assistant (Claude Code, Cursor, Codex, and similar). It will clone the repository, register the skills into your agent's skill directory, and run the install verification.

```
Help me install Supervisor-Skills from https://github.com/HKUSTDial/Supervisor-Skills with MCP and Skills.
```

Once installed, the seven skills trigger automatically from natural-language requests such as "help me evaluate this idea", "draft my Introduction", or "review this paper before submission". If you prefer to read the curriculum end-to-end, start at [`docs/en/handbook/`](docs/en/handbook/) (or the Chinese original at [`handbook/`](handbook/)).

## Contributing & feedback

This is an open-source AI-skill project for research methodology. Issues, pull requests, and discussions are welcome, as are stories of papers that used these skills en route to a top-venue acceptance. A star in the upper-right corner is the easiest way to say thanks and the biggest reason we keep shipping updates.

Contact: Yuyu Luo (yuyuluo [AT] hkust-gz.edu.cn).

##

Thanks to [Boyan Li](https://liboyan.vip/), [Yin Wu](https://openreview.net/profile?id=%7EYin_WU2), and [Yupeng Xie](https://xypkent.github.io/) for helping compile this repository and for their invaluable suggestions.

## TODO

**Guide**
- How to write a strong rebuttal, and what to do when reviewers ignore your response.
- How to collaborate effectively on academic work.

**Skills**
- MCP Development.

## License

This project is released under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Non-commercial sharing and adaptation are welcome; please preserve attribution.
