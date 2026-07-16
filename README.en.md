<div align="center">

<img src="assets/icon.png" alt="Supervisor-Skills" height="240" />

</div>

# Supervisor-Skills: Ten years of PhD-advisor research experience, distilled into your AI co-advisor.

> From idea conception to paper submission, covering the full research lifecycle.

English · [中文](README.md)

<p align="center">
  <a href="https://github.com/HKUSTDial/Supervisor-Skills/stargazers"><img src="https://img.shields.io/github/stars/HKUSTDial/Supervisor-Skills?style=flat-square&logo=github" alt="GitHub stars"></a>
  <a href="https://github.com/HKUSTDial/Supervisor-Skills/network/members"><img src="https://img.shields.io/github/forks/HKUSTDial/Supervisor-Skills?style=flat-square&logo=github" alt="GitHub forks"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square" alt="License"></a>
</p>

## 📰 News

> - **[2026-07-15]** 🤝 In partnership with **Doubao**, Supervisor-Skills has been officially deployed as the core research skill suite of **Doubao Office Mode**, powering its "**Research Evaluation**" and "**Academic Writing**" capabilities and bringing this project's research methodology to a massive user base.
> - **[2026-07-10]** 🚀 **v2.1**: three new skills, `paper-writer` (evidence-gated paper drafting), `paper-polish` (meaning-preserving polishing), and `deep-research` (survey-grade literature investigation); `intro-drafter` now outputs prose; paradigm-aware routing lands in the evaluation and review skills. See the [CHANGELOG](CHANGELOG.md).
> - **[2026-07-03]** 🎤 Invited talk at the Skill session of the **2026 China Agent Conference**.
> - **[2026-07-03]** 🧩 New skill `drawio-reconstruction`: rebuild reference figures into editable Draw.io.
> - **[2026-05-21]** ⭐ Crossed **1,000** GitHub stars, 32 days after release.
> - **[2026-04-19]** 🎉 Project released: seven anchor skills covering the paper lifecycle, together with the systematic handbook curriculum.

---

## Why this project?

Hi, I'm [Yuyu Luo](https://luoyuyu.vip/), Assistant Professor at The Hong Kong University of Science and Technology (Guangzhou). From my own PhD journey to mentoring students, I keep seeing the same scene: talented graduate students, as they step into research, are trapped by very similar struggles:

*   **Theory-practice gap**: After reading countless "research primers", when it is time to tackle one's own topic, one still does not know how to start.
*   **Scarce mentoring bandwidth**: The advisor is busy, and cannot give timely, careful feedback on every idea that pops up.
*   **Pre-submission fog**: The paper is drafted, yet it is unclear whether the logic is tight, whether the figures meet top-venue aesthetics, or whether a "rookie mistake" is hiding in the text.
*   **The "capability gap" in the AI era**: Large models are powerful, but without judgement and academic taste, AI is just a "high-end toy". **Relying solely on "prompting" cannot produce outstanding research.**

Together, these challenges form the **"Last-Mile Problem" of research**. It is about more than method — it is about experience, taste, and confidence.

That is why I started this project. We take ten years of accumulated publishing, reviewing experience and academic intuition at top venues in data science and AI (SIGMOD, VLDB, ICML, NeurIPS), and we "distil" and "forge" them into a set of structured **AI Skills** that large language models (Claude, GPT-4, etc.) can precisely execute.

This repository is **not merely a theoretical guide**. Its core is a first attempt to turn the **tacit knowledge** that sits in the minds of top researchers, but is difficult to articulate, into **directly-callable productivity**.

Our vision is simple: **Let AI become your true, always-on research co-advisor.**

## Community

**WeChat Discussion Group**

The group has exceeded 200 members and can no longer be joined via QR code. Please scan to add the admin on WeChat (`xyp619`) with the remark **"Supervisor-Skills + your name"** to be invited in.

You can also follow the official WeChat account of the **Data Intelligence and Analytics Lab (DIAL)** and **Xie Bro Talks Research** for research news, paper-writing tips, AI frontier updates, and research tool sharing.

By joining, you get:
- 🔔 First-hand updates on new Skills and Handbook releases
- 💬 Exchange paper writing and AI-assisted research tips with peers
- 🎙️ Join occasional online Q&A and experience-sharing sessions

<table align="center">
  <tr>
    <td align="center" width="360">
      <strong>Discussion Group</strong>
    </td>
    <td align="center" width="360">
      <strong>Official Account</strong>
    </td>
    <td align="center" width="360">
      <strong>Research Updates</strong>
    </td>
  </tr>
  <tr>
    <td align="center" valign="middle" height="360">
      <img src="assets/wechat-admin.JPG" height="300" />
    </td>
    <td align="center" valign="middle" height="360">
      <img src="assets/wechat-official-account.jpg" height="280" />
    </td>
    <td align="center" valign="middle" height="360">
      <img src="assets/wechat-xiebro-research.jpg" height="280" />
    </td>
  </tr>
  <tr>
    <td align="center">
      <sub>Add admin xyp619 to join the group</sub>
    </td>
    <td align="center">
      <sub>Data Intelligence and Analytics Lab (DIAL)</sub>
    </td>
    <td align="center">
      <sub>Xie Bro Talks Research: AI, papers, and research tools</sub>
    </td>
  </tr>
</table>

## Tutorial structure

The tutorial follows a dual-track architecture of **Guide (theoretical handbook) + Skills (executable AI skills)**:

```
Supervisor-Skills/
├── README.md                          # Chinese root README
├── README.en.md                       # this file
│
├── handbook/                          # 📖 Research and writing handbook (Chinese, canonical)
│   ├── 01_Preliminary/                # Chapter 1: macro perspective
│   │   ├── 1.1_如何评价一篇论文的质量.md
│   │   └── 博士生科研入门辅导.pdf         # 📄 companion slides
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
├── handbook-en/                       # 📖 English mirror of the handbook
│
├── skills/                            # 🛠️ Executable AI Skills
│   ├── idea-evaluator/
│   ├── deep-research/
│   ├── vibe-research-workflow/
│   ├── tech-paper-template/
│   ├── write-top-tier-ml-paper/
│   ├── intro-drafter/
│   ├── paper-writer/
│   ├── benchmark-paper-template/
│   ├── paper-polish/
│   ├── pre-submission-reviewer/
│   ├── figure-designer/
│   └── drawio-reconstruction/
│
└── assets/                            # Image assets
```

### 📖 handbook: Research and writing system guide

> **📄 Companion slides**: [博士生科研入门辅导.pdf](handbook/01_Preliminary/博士生科研入门辅导.pdf) — the companion PDF to this guide, suitable for printing or reading on an iPad. It captures the complete framework for getting started in research.

This section preserves the systematic theoretical framework for deep reading and study. Only by grasping the *way* can one better use the *tools*.

| Chapter | Content | English mirror |
|---|---|---|
| **Chapter 1: Macro perspective** | Evaluating paper quality from a reviewer's perspective (Novel Problem, Novel Method, Nice Story, Nice Presentation) | [1.1 How to evaluate paper quality](handbook-en/01_Preliminary/1.1_how-to-evaluate-paper-quality.md) |
| **Chapter 2: Idea generation** | Idea lifecycle, five-dimension thinking framework (Higher / Faster / Stronger / Cheaper / Broader), disruptive innovation | [2.1 Idea lifecycle](handbook-en/02_Idea_Generation/2.1_idea-lifecycle-and-capability-matching.md) / [2.2 Higher-faster-stronger](handbook-en/02_Idea_Generation/2.2_higher-faster-stronger.md) / [2.3 Disruptive innovation](handbook-en/02_Idea_Generation/2.3_disruptive-innovation.md) |
| **Chapter 3: Paper writing** | Full paper lifecycle, Introduction flowchart, technical / benchmark paper templates, writing checklist | [3.1 Essentials](handbook-en/03_Paper_Writing/3.1_the-essentials-of-a-research-paper.md) / [3.2 Intro flowchart](handbook-en/03_Paper_Writing/3.2_introduction-writing-flowchart.md) / [3.3 Technical template](handbook-en/03_Paper_Writing/3.3_technical-paper-template.md) / [3.4 Benchmark template](handbook-en/03_Paper_Writing/3.4_benchmark-paper-template.md) / [3.5 Writing checklist](handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md) |
| **Chapter 4: Scientific plotting** | Motivated / overview / results figures and a drawing checklist | [4.1 Motivated example](handbook-en/04_Scientific_Plotting/4.1_motivated-example-figure.md) / [4.2 Solution overview](handbook-en/04_Scientific_Plotting/4.2_solution-overview-figure.md) / [4.3 Experimental results](handbook-en/04_Scientific_Plotting/4.3_experimental-results-figure.md) / [4.4 Checklist](handbook-en/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md) |
| **Chapter 5: Vibe Research** | Vibe Research / Coding / Figure / Writing in practice | [5.1 Intro](handbook-en/05_Vibe_Research/5.1_vibe-research-and-vibe-coding.md) / [5.2 Practitioner notes](handbook-en/05_Vibe_Research/5.2_liboyan-practical-notes.md) |
| **Chapter 6: Top-venue case studies** | Alpha-SQL (ICML'25), AFlow (ICLR'25), LEAD (VLDB'26) Introduction analyses | [6.1 Alpha-SQL](handbook-en/06_Case_Studies/6.1_icml2025-alpha-sql-analysis.md) / [6.2 AFlow](handbook-en/06_Case_Studies/6.2_iclr2025-aflow-analysis.md) / [6.3 LEAD](handbook-en/06_Case_Studies/6.3_vldb2026-lead-analysis.md) |

The Chinese originals live at [`handbook/`](handbook/) with the same chapter structure.

### 🛠️ Skills: Executable AI Skills

This is the core of the repository. The theoretical experience above is distilled into structured Prompt/Skill files. You can copy the content directly into any AI assistant (Claude, DeepSeek, Kimi, etc.).

| Skill | Description | Link |
|---|---|---|
| **Idea Evaluator** | Feed in your idea, and the AI scores it on the "Higher / Faster / Stronger" five-dimension framework and the capability-matching table. | [Use skill](skills/idea-evaluator/SKILL.md) |
| **Vibe Research Guide** | AI-assisted research across the full lifecycle: Vibe Coding / Vibe Figure / Vibe Writing. | [Use skill](skills/vibe-research-workflow/SKILL.md) |
| **Introduction Drafter** | Based on the Introduction Flowchart thinking model, feed in your research motivation and receive six paragraphs of Introduction prose with retrieval-verified citations (outline mode on request). | [Use skill](skills/intro-drafter/SKILL.md) |
| **Paper Writer** | Evidence-gated paper drafting from a single paragraph to a full manuscript: every factual claim traces to your materials or verified literature, citations pass an independent check, nothing is fabricated. | [Use skill](skills/paper-writer/SKILL.md) |
| **Paper Polish** | Meaning-preserving language polishing: grammar, AI-tone removal, claim calibration, and Chinese-to-English rewriting at submission quality, with meaning-risk edits flagged for your confirmation. | [Use skill](skills/paper-polish/SKILL.md) |
| **Deep Research** | Survey-grade literature investigation: multi-perspective search, per-citation verification, MECE synthesis with cross-comparison, delivered as a survey report that answers explicit research questions. | [Use skill](skills/deep-research/SKILL.md) |
| **Tech Paper Template** | Based on the "Technical Full Paper thinking template", walks you through the full logical chain of your paper. | [Use skill](skills/tech-paper-template/SKILL.md) |
| **Top-Tier ML Paper Planner** | Turns diagnostic observations, design principles, components, claims, experiments, and figures into a reviewer-auditable claim-evidence loop with paragraph-level section contracts. | [Use skill](skills/write-top-tier-ml-paper/SKILL.md) |
| **Benchmark Paper Template** | Designed for Benchmark/Evaluation papers, helping you structure evaluation logic and experimental design. | [Use skill](skills/benchmark-paper-template/SKILL.md) |
| **Pre-Submission Reviewer** | Reviewer's perspective at a top venue — runs a full review over your draft based on the writing checklist and common English grammar pitfalls. | [Use skill](skills/pre-submission-reviewer/SKILL.md) |
| **Figure Design Advisor** | Tell the AI what you want to express; it returns professional drawing advice based on the motivated / overview / experimental figure paradigms. | [Use skill](skills/figure-designer/SKILL.md) |
| **Draw.io Reconstruction** | Rebuild reference images, paper figures, architecture diagrams, slide diagrams, or UI screenshots into editable `.drawio` files with PNG previews and visual audits. | [Use skill](skills/drawio-reconstruction/SKILL.md) |

## Quick Start

Paste the following prompt into your AI assistant (Claude Code, Cursor, Codex, and similar) to complete the installation:

```
Help me install Supervisor-Skills from https://github.com/HKUSTDial/Supervisor-Skills with Skills.
```

## Contributing & feedback

This is an open-source AI-skill project that tries to solve the "easy to use + compliant" problem for agent-driven research assistance.

Issues, pull requests, and stories about papers that used these skills on the way to a top-venue acceptance are all welcome.

If this project helped you, a star in the upper-right corner is the easiest way to say thanks and the biggest reason we keep shipping updates.

Contact: Yuyu Luo (yuyuluo [AT] hkust-gz.edu.cn).

##

Thanks to [Yin Wu](https://openreview.net/profile?id=%7EYin_WU2), [Boyan Li](https://liboyan.vip/), and [Yupeng Xie](https://xypkent.github.io/) for helping compile this repository and for their invaluable suggestions.

## TODO
**Guide**
- How to write a strong rebuttal, and what to do when reviewers ignore your response.
- How to collaborate effectively on academic work.

## License

This project is released under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Non-commercial sharing and adaptation are welcome; please preserve attribution.
