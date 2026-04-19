# PhD.Skills: 将博导十年科研经验炼化为可直接调用的 AI 技能。从 Idea 构思到论文投稿，你的 AI 科研副导师。

## 为什么做这个项目？

很多研究生在刚踏入科研大门时，往往会面临这些痛点：

- 看了很多"科研入门指南"，但面对自己的具体课题时，依然不知道怎么下笔。
- 导师很忙，无法随时帮你评估每一个 Idea 的价值。
- 论文写完了，不确定逻辑是否连贯、图表是否符合顶会审美、是否存在致命的"低级错误"。

这就是Vibe Research时代的 **Last Mile Problem（最后一公里问题）**。

我们决定把在 Data+AI 领域（如 SIGMOD, VLDB, ICML, NeurIPS 等顶会）积累的十年科研与写作经验，转化为结构化的、可被大模型（如 Claude, DeepSeek）直接理解和执行的 **Research Skills**。

这个仓库不仅仅是一份**理论指南**，更是首个尝试在智能体时代，将资深导师和顶会审稿人的**隐性知识（Tacit Knowledge）和写作习惯**，蒸馏并"炼化"为 **可直接调用的 AI Skills（AI技能）** 的开源项目。
**让 AI 成为你的全天候科研副导师！**

## 仓库结构

本仓库采用 **Guide（理论指南） + Skills（可执行AI技能）** 的双轨制架构：

```
PhD.Skills/
├── README.md                          # 本文件
├── QuickStart.md                      # 快速上手指南
│
├── 1_Guide/                           # 📖 科研与写作系统指南
│   ├── 01_Preliminary/                # 第一章：宏观认识与评价
│   │   └── 1.1_如何评价一篇论文的质量.md
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
│   └── 博士生科研入门辅导.pdf                 # 📄 配套讲义（可下载）
│
├── 2_Skills/                          # 🛠️ 提炼出的可执行 AI Skills
│   ├── Idea_Generation/               # 构思阶段技能
│   │   ├── Idea_Evaluator.skill.md
│   │   └── Vibe_Research_Guide.skill.md
│   ├── Paper_Writing/                 # 写作阶段技能
│   │   ├── Introduction_Drafter.skill.md
│   │   ├── Tech_Paper_Template.skill.md
│   │   └── Benchmark_Paper_Template.skill.md
│   └── Review_and_Check/              # 自查与润色技能
│       ├── Pre_Submission_Reviewer.skill.md
│       └── Figure_Design_Advisor.skill.md
│
└── images/                            # 图片资源
```

### 📖 1_Guide：科研与写作系统指南

> **📄 配套讲义**：[博士生科研入门辅导.pdf](1_Guide/博士生科研入门辅导.pdf) — 本指南的配套 PDF 讲义，适合打印或在 iPad 上阅读，包含完整的科研入门思路框架。

这里保留了系统性的理论框架，供你深入阅读和系统学习。只有理解了"道"，才能更好地使用"器"。

| 章节 | 内容 | 链接 |
|---|---|---|
| **第一章：宏观认识** | 从审稿人视角看论文质量（Novel Problem, Novel Method, Nice Story, Nice Presentation） | [1.1 如何评价一篇论文的质量](1_Guide/01_Macro_Understanding/1.1_如何评价一篇论文的质量.md) |
| **第二章：Idea构思** | Idea的生命周期、5维思考框架（更高更快更强更省更广）、颠覆式创新 | [2.1 Idea生命周期](1_Guide/02_Idea_Generation/2.1_Idea的生命周期与能力匹配.md) / [2.2 更高更快更强](1_Guide/02_Idea_Generation/2.2_想Idea的思路_更高更快更强.md) / [2.3 颠覆式创新](1_Guide/02_Idea_Generation/2.3_进阶_如何做颠覆式创新.md) |
| **第三章：论文写作** | 科研论文全流程、Introduction思考模型、技术类/Benchmark类论文模板、写作Checklist | [3.1 全流程](1_Guide/03_Paper_Writing/3.1_完成一篇科研论文你需要做几件事情.md) / [3.2 Intro模型](1_Guide/03_Paper_Writing/3.2_Introduction写作的思考模型.md) / [3.3 技术类模板](1_Guide/03_Paper_Writing/3.3_技术类Full_Paper思考模板.md) / [3.4 Benchmark模板](1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md) / [3.5 Checklist](1_Guide/03_Paper_Writing/3.5_写作细节与Checklist.md) |
| **第四章：科研作图** | 动机图、总览图、实验图的设计范式与绘图Checklist | [4.1 动机图](1_Guide/04_Scientific_Plotting/4.1_Motivated_Example_Figure.md) / [4.2 总览图](1_Guide/04_Scientific_Plotting/4.2_Solution_Overview_Figure.md) / [4.3 实验图](1_Guide/04_Scientific_Plotting/4.3_Experimental_Results_Figure.md) / [4.4 Checklist](1_Guide/04_Scientific_Plotting/4.4_绘图Checklist与工具速查表.md) |
| **第五章：前沿实战** | Vibe Research/Coding/Figure/Writing 入门与实战经验 | [5.1 入门指南](1_Guide/05_Vibe_Research/5.1_Vibe_Research与Vibe_Coding入门.md) / [5.2 实战经验](1_Guide/05_Vibe_Research/5.2_李伯岩实战经验分享与会议纪要.md) |
| **第六章：顶会案例** | Alpha-SQL (ICML'25)、AFlow (ICLR'25)、LEAD (VLDB'26) 写作思路剖析 | [6.1 Alpha-SQL](1_Guide/06_Case_Studies/6.1_ICML_2025_Alpha-SQL写作剖析.md) / [6.2 AFlow](1_Guide/06_Case_Studies/6.2_ICLR_2025_AFlow写作剖析.md) / [6.3 LEAD](1_Guide/06_Case_Studies/6.3_VLDB_2026_LEAD写作剖析.md) |

### 🛠️ 2_Skills：提炼出的可执行 AI Skills

这里是本仓库的核心卖点！我们将上述理论经验蒸馏成了结构化的 Prompt/Skill 文件。你可以直接复制这些内容，导入到你的 AI 助手中（Claude、DeepSeek、Kimi 等均可）。

| 技能名称 | 功能描述 | 链接 |
|---|---|---|
| **Idea Evaluator** | 输入你的 Idea，AI 将根据"更高更快更强"5维框架和能力匹配表进行客观评估与打分 | [使用技能](2_Skills/Idea_Generation/Idea_Evaluator.skill.md) |
| **Vibe Research Guide** | AI 辅助科研全流程指导：Vibe Coding / Vibe Figure / Vibe Writing | [使用技能](2_Skills/Idea_Generation/Vibe_Research_Guide.skill.md) |
| **Introduction Drafter** | 基于 Introduction 的 Flowchart 思考模型，输入研究动机，自动生成高质量的 Intro 大纲 | [使用技能](2_Skills/Paper_Writing/Introduction_Drafter.skill.md) |
| **Tech Paper Template** | 基于"技术类Full Paper思考模板"，辅助你一步步梳理论文的完整逻辑链 | [使用技能](2_Skills/Paper_Writing/Tech_Paper_Template.skill.md) |
| **Benchmark Paper Template** | 专为 Benchmark/Evaluation 类论文设计，辅助梳理评估逻辑和实验设计 | [使用技能](2_Skills/Paper_Writing/Benchmark_Paper_Template.skill.md) |
| **Pre-Submission Reviewer** | 顶会审稿人视角！基于写作 Checklist 和英语语法易错点，对草稿进行全面审查 | [使用技能](2_Skills/Review_and_Check/Pre_Submission_Reviewer.skill.md) |
| **Figure Design Advisor** | 告诉 AI 你想表达什么，它会根据动机图/总览图/实验图的设计范式给出专业作图建议 | [使用技能](2_Skills/Review_and_Check/Figure_Design_Advisor.skill.md) |

## 快速开始 (Quick Start)

想要知道如何将这些 `.skill` 文件导入并使用吗？请查看 [QuickStart.md](QuickStart.md)。

## 贡献与反馈

这是一款创新的开源 AI Skill 项目。期待能够解决智能体在科研辅助落地中"好用+合规"的问题。

欢迎大家试用、提 PR、开 Issue，或者分享你基于这些 Skill 写出的顶会论文！

如果你觉得这个项目对你有帮助，请点亮右上角的 Star！你的支持是我们持续更新的最大动力。

邮件联系：Yuyu Luo (yuyuluo [AT] hkust-gz.edu.cn).

## License

本项目采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 协议开源。欢迎非商业用途的分享与改编，但请注明出处。
