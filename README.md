<div align="center">

<img src="assets/images/icon.png" alt="Supervisor-Skills" height="240" />

</div>

# Supervisor-Skills: 将博导十年科研经验，炼化为你的 AI 副导师。

> 从 Idea 构思到论文投稿，覆盖科研全流程。

[English](README.en.md) · 中文

## 为什么做这个项目？

大家好，我是[骆昱宇](https://luoyuyu.vip/)，香港科技大学（广州）的助理教授。从自己读博到指导学生，我反复看到一个场景：许多才华横溢的研究生，在踏入科研大门时，常常被相似的困境所困扰：

*   **理论与实践脱节**：读了再多"科研指南"，面对自己的课题时，依旧不知如何下笔。
*   **指导资源稀缺**：导师日程繁忙，无法对你萌生的每一个想法进行及时、细致的评估。
*   **投稿前的迷茫**：论文写完，却不确定逻辑是否严密、图表是否符合顶会审美、行文是否暗含"低级错误"。
*   **AI时代的"能力鸿沟"**：大模型很强大，但若缺乏判断力与学术品味，AI也只是"高级玩具"。**仅仅依赖一味地"Prompt"，无法催生卓越的科研成果。**

这些挑战，共同构成了科研的 **"最后一公里问题" (The Last-Mile Problem)**。它不仅是方法论的缺失，更是经验、品味与判断力的综合考验。

为此，我发起了 Supervisor-Skills 项目。我们将过去十年在数据科学与人工智能顶级会议（如 SIGMOD, VLDB, ICML, NeurIPS）中积累的发表、审稿经验与学术直觉，进行"蒸馏"与"锻造"，最终封装成一套结构化的、可被大语言模型（如 Claude, GPT-4）精确执行的 **AI技能 (AI Skills)**。 我们的愿景很简单：**将资深科研者的隐性知识，转化为人人可用的 AI 工具，让 AI 成为你真正的、全天候在线的科研副导师**

这个项目仍处在早期阶段，我们正努力将自己能力范围内的认知与见解毫无保留地呈现出来，希望能为初入科研领域的探索者提供一份实用的操作指南。我们更热切地期待，能与各位同行者一起，共同建设、完善这个知识库，让科研之路不再孤单。谢谢！

## 教程结构

本教程采用 **Guide（理论指南） + Skills（可执行AI技能）** 的双轨制架构：

```
Supervisor-Skills/
├── README.md                          # 本文件
│
├── handbook/                          # 📖 科研与写作系统指南
│   ├── 01_Preliminary/                # 第一章：宏观认识与评价
│   │   ├── 1.1_如何评价一篇论文的质量.md
│   │   └── 博士生科研入门辅导_2023年8月.pdf   # 📄 配套讲义（可下载）
│   ├── 02_Idea_Generation/            # 第二章：Idea的诞生与升华
│   │   ├── 2.1_Idea的生命周期与能力匹配.md
│   │   ├── 2.2_想Idea的思路_更高更快更强.md
│   │   └── 2.3_进阶_如何做颠覆式创新.md
│   ├── 03_Paper_Writing/              # 第三章：论文写作方法论
│   │   ├── 3.1_完成一篇科研论文你需要做几件事情.md
│   │   ├── 3.2_Introduction写作的思考模型.md
│   │   ├── 3.3_技术类Full_Paper思考模板.md
│   │   ├── 3.4_Benchmark与Evaluation类论文思考模板.md
│   │   └── 3.5_写作细节与Checklist.md
│   ├── 04_Scientific_Plotting/        # 第四章：科研作图指南
│   │   ├── 4.1_Motivated_Example_Figure.md
│   │   ├── 4.2_Solution_Overview_Figure.md
│   │   ├── 4.3_Experimental_Results_Figure.md
│   │   └── 4.4_绘图Checklist与工具速查表.md
│   ├── 05_Vibe_Research/              # 第五章：Vibe Research前沿实战
│   │   ├── 5.1_Vibe_Research与Vibe_Coding入门.md
│   │   └── 5.2_李伯岩实战经验分享与会议纪要.md
│   └── 06_Case_Studies/               # 第六章：顶会论文写作剖析案例
│       ├── 6.1_ICML_2025_Alpha-SQL写作剖析.md
│       ├── 6.2_ICLR_2025_AFlow写作剖析.md
│       └── 6.3_VLDB_2026_LEAD写作剖析.md
│
├── plugins/phd-research/skills/       # 🛠️ 提炼出的可执行 AI Skills
│   ├── idea-evaluator/                # 构思阶段技能
│   ├── vibe-research-workflow/
│   ├── intro-drafter/                 # 写作阶段技能
│   ├── tech-paper-template/
│   ├── benchmark-paper-template/
│   ├── pre-submission-reviewer/       # 自查与润色技能
│   └── figure-designer/
│
└── assets/images/                     # 图片资源
```

### 📖 handbook：科研与写作系统指南

> **📄 配套讲义**：[博士生科研入门辅导.pdf](handbook/01_Preliminary/博士生科研入门辅导_2023年8月.pdf) — 本指南的配套 PDF 讲义，适合打印或在 iPad 上阅读，包含完整的科研入门思路框架。

这里保留了系统性的理论框架，供你深入阅读和系统学习。只有理解了"道"，才能更好地使用"器"。

| 章节 | 内容 | 链接 |
|---|---|---|
| **第一章：宏观认识** | 从审稿人视角看论文质量（Novel Problem, Novel Method, Nice Story, Nice Presentation） | [1.1 如何评价一篇论文的质量](handbook/01_Preliminary/1.1_如何评价一篇论文的质量.md) / [博士生科研入门辅导](handbook/01_Preliminary/博士生科研入门辅导_2023年8月.pdf)|
| **第二章：Idea构思** | Idea的生命周期、5维思考框架（更高更快更强更省更广）、颠覆式创新 | [2.1 Idea生命周期](handbook/02_Idea_Generation/2.1_Idea的生命周期与能力匹配.md) / [2.2 更高更快更强](handbook/02_Idea_Generation/2.2_想Idea的思路_更高更快更强.md) / [2.3 颠覆式创新](handbook/02_Idea_Generation/2.3_进阶_如何做颠覆式创新.md) |
| **第三章：论文写作** | 科研论文全流程、Introduction思考模型、技术类/Benchmark类论文模板、写作Checklist | [3.1 全流程](handbook/03_Paper_Writing/3.1_完成一篇科研论文你需要做几件事情.md) / [3.2 Intro模型](handbook/03_Paper_Writing/3.2_Introduction写作的思考模型.md) / [3.3 技术类模板](handbook/03_Paper_Writing/3.3_技术类Full_Paper思考模板.md) / [3.4 Benchmark模板](handbook/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md) / [3.5 Checklist](handbook/03_Paper_Writing/3.5_写作细节与Checklist.md) |
| **第四章：科研作图** | 动机图、总览图、实验图的设计范式与绘图Checklist | [4.1 动机图](handbook/04_Scientific_Plotting/4.1_Motivated_Example_Figure.md) / [4.2 总览图](handbook/04_Scientific_Plotting/4.2_Solution_Overview_Figure.md) / [4.3 实验图](handbook/04_Scientific_Plotting/4.3_Experimental_Results_Figure.md) / [4.4 Checklist](handbook/04_Scientific_Plotting/4.4_绘图Checklist与工具速查表.md) |
| **第五章：前沿实战** | Vibe Research/Coding/Figure/Writing 入门与实战经验 | [5.1 入门指南](handbook/05_Vibe_Research/5.1_Vibe_Research与Vibe_Coding入门.md) / [5.2 实战经验](handbook/05_Vibe_Research/5.2_李伯岩实战经验分享与会议纪要.md) |
| **第六章：顶会案例** | Alpha-SQL (ICML'25)、AFlow (ICLR'25)、LEAD (VLDB'26) 写作思路剖析 | [6.1 Alpha-SQL](handbook/06_Case_Studies/6.1_ICML_2025_Alpha-SQL写作剖析.md) / [6.2 AFlow](handbook/06_Case_Studies/6.2_ICLR_2025_AFlow写作剖析.md) / [6.3 LEAD](handbook/06_Case_Studies/6.3_VLDB_2026_LEAD写作剖析.md) |

### 🛠️ Skills：提炼出的可执行 AI Skills

这里是本仓库的核心卖点！我们将上述理论经验蒸馏成了结构化的 Prompt/Skill 文件。你可以直接复制这些内容，导入到你的 AI 助手中（Claude、DeepSeek、Kimi 等均可）。

| 技能名称 | 功能描述 | 链接 |
|---|---|---|
| **Idea Evaluator** | 输入你的 Idea，AI 将根据"更高更快更强"5维框架和能力匹配表进行客观评估与打分 | [使用技能](plugins/phd-research/skills/idea-evaluator/SKILL.md) |
| **Vibe Research Guide** | AI 辅助科研全流程指导：Vibe Coding / Vibe Figure / Vibe Writing | [使用技能](plugins/phd-research/skills/vibe-research-workflow/SKILL.md) |
| **Introduction Drafter** | 基于 Introduction 的 Flowchart 思考模型，输入研究动机，自动生成高质量的 Intro 大纲 | [使用技能](plugins/phd-research/skills/intro-drafter/SKILL.md) |
| **Tech Paper Template** | 基于"技术类Full Paper思考模板"，辅助你一步步梳理论文的完整逻辑链 | [使用技能](plugins/phd-research/skills/tech-paper-template/SKILL.md) |
| **Benchmark Paper Template** | 专为 Benchmark/Evaluation 类论文设计，辅助梳理评估逻辑和实验设计 | [使用技能](plugins/phd-research/skills/benchmark-paper-template/SKILL.md) |
| **Pre-Submission Reviewer** | 顶会审稿人视角！基于写作 Checklist 和英语语法易错点，对草稿进行全面审查 | [使用技能](plugins/phd-research/skills/pre-submission-reviewer/SKILL.md) |
| **Figure Design Advisor** | 告诉 AI 你想表达什么，它会根据动机图/总览图/实验图的设计范式给出专业作图建议 | [使用技能](plugins/phd-research/skills/figure-designer/SKILL.md) |

## 快速开始 (Quick Start)

把下方这段 Prompt 发给你的 AI 助手（Claude Code、Cursor、Codex，或任意支持 MCP 的客户端）即可完成安装：

```
Help me install Supervisor-Skills from https://github.com/HKUSTDial/Supervisor-Skills with MCP and Skills.
```

## 贡献与反馈

这是一款创新的开源 AI Skill 项目。期待能够解决智能体在科研辅助落地中"好用+合规"的问题。

欢迎大家试用、提 PR、开 Issue，或者分享你基于这些 Skill 写出的顶会论文！

如果你觉得这个项目对你有帮助，请点亮右上角的 Star！你的支持是我们持续更新的最大动力。

邮件联系：Yuyu Luo (yuyuluo [AT] hkust-gz.edu.cn).

##

感谢[吴垠](https://openreview.net/profile?id=%7EYin_WU2)、[李伯岩](https://liboyan.vip/)、[谢宇鹏](https://xypkent.github.io/)协助整理该仓库并提供宝贵的建议！

## TODO
**Guide**
- 如何写好Rebuttal？审稿人不理我的Rebuttal，怎么办？
- 如何与他人进行高效的学术合作？

**Skills**
- MCP Development

## License

本项目采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 协议开源。欢迎非商业用途的分享与改编，但请注明出处。
