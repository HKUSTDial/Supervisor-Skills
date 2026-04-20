<div align="center">

<img src="assets/images/icon-example.png" alt="Supervisor-Skills" height="140" />

</div>

# Supervisor-Skills: Ten years of PhD-advisor research experience distilled into directly-callable AI skills. From ideation to submission, your AI research co-advisor.

English · [中文](README.md)

## Why this project?

Graduate students entering research often hit the same pain points:

- Plenty of "research primers" are on hand, yet once faced with one's own topic, one still does not know how to start.
- The advisor is busy and cannot sit with every new idea on the spot.
- Once the paper is drafted, it is unclear whether the logic is coherent, whether the figures meet top-venue aesthetics, or whether a fatal "rookie mistake" is hiding in the text.

This is the **Last Mile Problem** of the Vibe Research era.

We distilled ten years of research and writing experience in the Data+AI area (SIGMOD, VLDB, ICML, NeurIPS, and similar top venues) into structured **Research Skills** that large language models (Claude, DeepSeek, etc.) can directly read and execute.

This repository is not only a **theoretical guide** — it is an early attempt in the agent era to distill the **tacit knowledge and writing habits** of senior advisors and top-venue reviewers into **directly-callable AI Skills**.
**Let AI become your always-on research co-advisor!**

## Repository structure

The repository follows a dual-track architecture of **Guide (theoretical handbook) + Skills (executable AI skills)**:

```
Supervisor-Skills/
├── README.md                          # Chinese root README
├── README.en.md                       # this file
│
├── handbook/                          # 📖 Research and writing handbook (Chinese, canonical)
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
├── plugins/phd-research/skills/       # 🛠️ Executable AI Skills
│   ├── idea-evaluator/
│   ├── vibe-research-workflow/
│   ├── intro-drafter/
│   ├── tech-paper-template/
│   ├── benchmark-paper-template/
│   ├── pre-submission-reviewer/
│   └── figure-designer/
│
└── assets/images/                     # Image assets
```

### 📖 handbook: Research and writing system guide

> **📄 Companion slides**: [博士生科研入门辅导.pdf](handbook/01_Preliminary/博士生科研入门辅导_2023年8月.pdf) — the companion PDF to this guide, suitable for printing or reading on an iPad. It captures the complete framework for getting started in research.

The handbook preserves the systematic theoretical framework for deep reading and study. Only by grasping the *way* can one better use the *tools*.

| Chapter | Content | English mirror |
|---|---|---|
| **Chapter 1: Macro perspective** | Evaluating paper quality from a reviewer's perspective (Novel Problem, Novel Method, Nice Story, Nice Presentation) | [1.1 How to evaluate paper quality](docs/en/handbook/01_Preliminary/1.1_how-to-evaluate-paper-quality.md) |
| **Chapter 2: Idea generation** | Idea lifecycle, five-dimension thinking framework (Higher / Faster / Stronger / Cheaper / Broader), disruptive innovation | [2.1 Idea lifecycle](docs/en/handbook/02_Idea_Generation/2.1_idea-lifecycle-and-capability-matching.md) / [2.2 Higher-faster-stronger](docs/en/handbook/02_Idea_Generation/2.2_higher-faster-stronger.md) / [2.3 Disruptive innovation](docs/en/handbook/02_Idea_Generation/2.3_disruptive-innovation.md) |
| **Chapter 3: Paper writing** | Full paper lifecycle, Introduction flowchart, technical / benchmark paper templates, writing checklist | [3.1 Essentials](docs/en/handbook/03_Paper_Writing/3.1_the-essentials-of-a-research-paper.md) / [3.2 Intro flowchart](docs/en/handbook/03_Paper_Writing/3.2_introduction-writing-flowchart.md) / [3.3 Technical template](docs/en/handbook/03_Paper_Writing/3.3_technical-paper-template.md) / [3.4 Benchmark template](docs/en/handbook/03_Paper_Writing/3.4_benchmark-paper-template.md) / [3.5 Writing checklist](docs/en/handbook/03_Paper_Writing/3.5_writing-details-and-checklist.md) |
| **Chapter 4: Scientific plotting** | Motivated / overview / results figures and a drawing checklist | [4.1 Motivated example](docs/en/handbook/04_Scientific_Plotting/4.1_motivated-example-figure.md) / [4.2 Solution overview](docs/en/handbook/04_Scientific_Plotting/4.2_solution-overview-figure.md) / [4.3 Experimental results](docs/en/handbook/04_Scientific_Plotting/4.3_experimental-results-figure.md) / [4.4 Checklist](docs/en/handbook/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md) |
| **Chapter 5: Vibe Research** | Vibe Research / Coding / Figure / Writing in practice | [5.1 Intro](docs/en/handbook/05_Vibe_Research/5.1_vibe-research-and-vibe-coding.md) / [5.2 Practitioner notes](docs/en/handbook/05_Vibe_Research/5.2_liboyan-practical-notes.md) |
| **Chapter 6: Top-venue case studies** | Alpha-SQL (ICML'25), AFlow (ICLR'25), LEAD (VLDB'26) Introduction analyses | [6.1 Alpha-SQL](docs/en/handbook/06_Case_Studies/6.1_icml2025-alpha-sql-analysis.md) / [6.2 AFlow](docs/en/handbook/06_Case_Studies/6.2_iclr2025-aflow-analysis.md) / [6.3 LEAD](docs/en/handbook/06_Case_Studies/6.3_vldb2026-lead-analysis.md) |

The Chinese originals live at [`handbook/`](handbook/) with the same chapter structure.

### 🛠️ Skills: Executable AI Skills

This is the core of the repository. The theoretical experience above is distilled into structured Prompt/Skill files. You can copy the content directly into any AI assistant (Claude, DeepSeek, Kimi, etc.).

| Skill | Description | Link |
|---|---|---|
| **Idea Evaluator** | Feed in your idea, and the AI scores it on the "Higher / Faster / Stronger" five-dimension framework and the capability-matching table. | [Use skill](plugins/phd-research/skills/idea-evaluator/SKILL.md) |
| **Vibe Research Guide** | AI-assisted research across the full lifecycle: Vibe Coding / Vibe Figure / Vibe Writing. | [Use skill](plugins/phd-research/skills/vibe-research-workflow/SKILL.md) |
| **Introduction Drafter** | Based on the Introduction Flowchart thinking model, feed in your research motivation and receive a high-quality Intro outline. | [Use skill](plugins/phd-research/skills/intro-drafter/SKILL.md) |
| **Tech Paper Template** | Based on the "Technical Full Paper thinking template", walks you through the full logical chain of your paper. | [Use skill](plugins/phd-research/skills/tech-paper-template/SKILL.md) |
| **Benchmark Paper Template** | Designed for Benchmark/Evaluation papers, helping you structure evaluation logic and experimental design. | [Use skill](plugins/phd-research/skills/benchmark-paper-template/SKILL.md) |
| **Pre-Submission Reviewer** | Reviewer's perspective at a top venue — runs a full review over your draft based on the writing checklist and common English grammar pitfalls. | [Use skill](plugins/phd-research/skills/pre-submission-reviewer/SKILL.md) |
| **Figure Design Advisor** | Tell the AI what you want to express; it returns professional drawing advice based on the motivated / overview / experimental figure paradigms. | [Use skill](plugins/phd-research/skills/figure-designer/SKILL.md) |

## Quick Start

Paste the following prompt into any MCP-aware AI assistant (Claude Code, Cursor, Codex, and similar) to complete the installation:

```
Help me install Supervisor-Skills from https://github.com/HKUSTDial/Supervisor-Skills with MCP and Skills.
```

## Contributing & feedback

This is an open-source AI-skill project that tries to solve the "easy to use + compliant" problem for agent-driven research assistance.

Issues, pull requests, and stories about papers that used these skills on the way to a top-venue acceptance are all welcome.

If this project helped you, a star in the upper-right corner is the easiest way to say thanks and the biggest reason we keep shipping updates.

Contact: Yuyu Luo (yuyuluo [AT] hkust-gz.edu.cn).

## License

This project is released under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Non-commercial sharing and adaptation are welcome; please preserve attribution.
