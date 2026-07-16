<div align="center">

<img src="assets/icon.png" alt="Supervisor-Skills" height="240" />

</div>

# Supervisor-Skills: 将博导十年科研经验，炼化为你的 AI 副导师。

[English](README.en.md) · 中文

<p align="center">
  <a href="https://github.com/HKUSTDial/Supervisor-Skills/stargazers"><img src="https://img.shields.io/github/stars/HKUSTDial/Supervisor-Skills?style=flat-square&logo=github" alt="GitHub stars"></a>
  <a href="https://github.com/HKUSTDial/Supervisor-Skills/network/members"><img src="https://img.shields.io/github/forks/HKUSTDial/Supervisor-Skills?style=flat-square&logo=github" alt="GitHub forks"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square" alt="License"></a>
</p>

## 📰 News

> - **[2026-07-15]** 🤝 团队与**豆包**达成合作，Supervisor-Skills 正式作为**豆包·办公模式**的核心科研技能完成部署，驱动「**科研评估**」与「**学术创作**」两大官方能力，将本项目沉淀的科研方法论带给亿级用户。
> - **[2026-07-10]** 🚀 **v2.1**：新增 `paper-writer`（证据门控的论文正文写作）、`paper-polish`（忠于原意的语言润色）、`deep-research`（综述级文献调研）三个技能；`intro-drafter` 升级为正文输出；评估与评审技能引入学科范式路由。详见 [CHANGELOG](CHANGELOG.md)。
> - **[2026-07-03]** 🎤 受邀在 **2026 中国智能体大会** Skill 会场进行分享。
> - **[2026-07-03]** 🧩 新增 `drawio-reconstruction` 技能：参考图一键重建为可编辑 Draw.io。
> - **[2026-05-21]** ⭐ GitHub Star 突破 **1,000**（发布第 32 天）。
> - **[2026-04-19]** 🎉 项目发布：七个锚点技能覆盖论文全生命周期，配套 handbook 系统课程。

---

## 为什么做这个项目？

大家好，我是[骆昱宇](https://luoyuyu.vip/)，香港科技大学（广州）的助理教授。从自己读博到指导学生，我反复看到一个场景：许多才华横溢的研究生，在踏入科研大门时，常常被相似的困境所困扰：

*   **理论与实践脱节**：读了再多"科研指南"，面对自己的课题时，依旧不知如何下笔。
*   **指导资源稀缺**：导师日程繁忙，无法对你萌生的每一个想法进行及时、细致的评估。
*   **投稿前的迷茫**：论文写完，却不确定逻辑是否严密、图表是否符合顶会审美、行文是否暗含"低级错误"。
*   **AI时代的"能力鸿沟"**：大模型很强大，但若缺乏判断力与学术品味，AI也只是"高级玩具"。**卓越的科研成果，无法仅靠“万能 Prompt”催生。**

这些挑战，共同构成了科研的 **"最后一公里问题" (The Last-Mile Problem)**。它不仅是方法论的缺失，更是经验、品味与判断力的综合考验。

为此，我发起了 Supervisor-Skills 项目。我们将过去十年在数据科学与人工智能顶级会议（如 SIGMOD, VLDB, ICML, NeurIPS）中积累的发表、审稿经验与学术直觉，进行"蒸馏"与"锻造"，最终封装成一套结构化的、可被大语言模型（如 Claude, GPT-4）精确执行的 **AI技能 (AI Skills)**。 我们的愿景很简单：**将资深科研者的隐性知识，转化为人人可用的 AI 工具，让 AI 成为你真正的、全天候在线的科研副导师**

这个项目仍处在早期阶段，我们正努力将自己能力范围内的认知与见解毫无保留地呈现出来，希望能为初入科研领域的探索者提供一份实用的操作指南。我们更热切地期待，能与各位同行者一起，共同建设、完善这个知识库，让科研之路不再孤单。如果你觉得这个项目对你有帮助，请点亮右上角的⭐️Star⭐️！谢谢！

## 社区与交流

**微信交流群**

群已超过 200 人，无法通过二维码直接入群。请扫码添加管理员微信 `xyp619`，备注 **"Supervisor-Skills + 姓名"**，由管理员邀请入群。

您也可以关注 **数据智能与分析实验室 DIAL 官方公众号** 与 **蟹哥聊科研**，获取科研资讯、论文写作经验、AI 前沿动态与科研工具分享。

加入后您可以：
- 🔔 第一时间获取 Skills 与 Handbook 的最新更新通知
- 💬 与同路人交流论文写作、AI 辅助科研心得
- 🎙️ 参与不定期的线上答疑与经验分享活动

<table align="center">
  <tr>
    <td align="center" width="360">
      <strong>微信交流群</strong>
    </td>
    <td align="center" width="360">
      <strong>官方公众号</strong>
    </td>
    <td align="center" width="360">
      <strong>科研分享号</strong>
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
      <sub>添加管理员 xyp619，邀请入群交流</sub>
    </td>
    <td align="center">
      <sub>数据智能与分析实验室 DIAL 官方公众号</sub>
    </td>
    <td align="center">
      <sub>蟹哥聊科研：AI 前沿、论文与科研工具分享</sub>
    </td>
  </tr>
</table>

## 教程结构

本教程采用 **Guide（理论指南） + Skills（可执行AI技能）** 的双轨制架构：

```
Supervisor-Skills/
├── README.md                          # 本文件
│
├── handbook/                          # 📖 科研与写作系统指南
│   ├── 01_Preliminary/                # 第一章：宏观认识与评价
│   │   ├── 1.1_如何评价一篇论文的质量.md
│   │   └── 博士生科研入门辅导.pdf         # 📄 配套讲义（可下载）
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
├── skills/                            # 🛠️ 提炼出的可执行 AI Skills
│   ├── idea-evaluator/                # 构思与调研阶段技能
│   ├── deep-research/
│   ├── vibe-research-workflow/
│   ├── tech-paper-template/           # 写作阶段技能
│   ├── write-top-tier-ml-paper/
│   ├── intro-drafter/
│   ├── paper-writer/
│   ├── benchmark-paper-template/
│   ├── paper-polish/                  # 自查与润色技能
│   ├── pre-submission-reviewer/
│   ├── figure-designer/
│   └── drawio-reconstruction/         # Draw.io 重建执行技能
│
└── assets/                            # 图片资源
```

### 📖 Handbook：科研与写作系统指南

> **📄 配套讲义**：[博士生科研入门辅导.pdf](handbook/01_Preliminary/博士生科研入门辅导.pdf) — 本指南的配套 PDF 讲义，适合打印或在 iPad 上阅读，包含完整的科研入门思路框架。

这里保留了系统性的理论框架，供你深入阅读和系统学习。只有理解了"道"，才能更好地使用"器"。

| 章节 | 内容 | 链接 |
|---|---|---|
| **第一章：宏观认识** | 从审稿人视角看论文质量（Novel Problem, Novel Method, Nice Story, Nice Presentation） | [1.1 如何评价一篇论文的质量](handbook/01_Preliminary/1.1_如何评价一篇论文的质量.md) / [博士生科研入门辅导](handbook/01_Preliminary/博士生科研入门辅导.pdf)|
| **第二章：Idea构思** | Idea的生命周期、5维思考框架（更高更快更强更省更广）、颠覆式创新 | [2.1 Idea生命周期](handbook/02_Idea_Generation/2.1_Idea的生命周期与能力匹配.md) / [2.2 更高更快更强](handbook/02_Idea_Generation/2.2_想Idea的思路_更高更快更强.md) / [2.3 颠覆式创新](handbook/02_Idea_Generation/2.3_进阶_如何做颠覆式创新.md) |
| **第三章：论文写作** | 科研论文全流程、Introduction思考模型、技术类/Benchmark类论文模板、写作Checklist | [3.1 全流程](handbook/03_Paper_Writing/3.1_完成一篇科研论文你需要做几件事情.md) / [3.2 Intro模型](handbook/03_Paper_Writing/3.2_Introduction写作的思考模型.md) / [3.3 技术类模板](handbook/03_Paper_Writing/3.3_技术类Full_Paper思考模板.md) / [3.4 Benchmark模板](handbook/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md) / [3.5 Checklist](handbook/03_Paper_Writing/3.5_写作细节与Checklist.md) |
| **第四章：科研作图** | 动机图、总览图、实验图的设计范式与绘图Checklist | [4.1 动机图](handbook/04_Scientific_Plotting/4.1_Motivated_Example_Figure.md) / [4.2 总览图](handbook/04_Scientific_Plotting/4.2_Solution_Overview_Figure.md) / [4.3 实验图](handbook/04_Scientific_Plotting/4.3_Experimental_Results_Figure.md) / [4.4 Checklist](handbook/04_Scientific_Plotting/4.4_绘图Checklist与工具速查表.md) |
| **第五章：前沿实战** | Vibe Research/Coding/Figure/Writing 入门与实战经验 | [5.1 入门指南](handbook/05_Vibe_Research/5.1_Vibe_Research与Vibe_Coding入门.md) / [5.2 实战经验](handbook/05_Vibe_Research/5.2_李伯岩实战经验分享与会议纪要.md) |
| **第六章：顶会案例** | Alpha-SQL (ICML'25)、AFlow (ICLR'25)、LEAD (VLDB'26) 写作思路剖析 | [6.1 Alpha-SQL](handbook/06_Case_Studies/6.1_ICML_2025_Alpha-SQL写作剖析.md) / [6.2 AFlow](handbook/06_Case_Studies/6.2_ICLR_2025_AFlow写作剖析.md) / [6.3 LEAD](handbook/06_Case_Studies/6.3_VLDB_2026_LEAD写作剖析.md) |

### 🛠️ Skills：提炼出的可执行 AI Skills

这里是本仓库的核心卖点！我们将上述理论经验蒸馏成了结构化的 Prompt/Skill 文件。你可以直接复制这些内容，导入到你的 AI 助手中（Claude、DeepSeek、Kimi 等均可）。

| 技能名称 | 功能描述 | 链接 |
|---|---|---|
| **Idea Evaluator** | 输入你的 Idea，AI 将根据"更高更快更强"5维框架和能力匹配表进行客观评估与打分 | [使用技能](skills/idea-evaluator/SKILL.md) |
| **Vibe Research Guide** | AI 辅助科研全流程指导：Vibe Coding / Vibe Figure / Vibe Writing | [使用技能](skills/vibe-research-workflow/SKILL.md) |
| **Introduction Drafter** | 基于 Introduction 的 Flowchart 思考模型，输入研究动机，直接产出六段式 Intro 正文（引用经真实检索核验；也可只要大纲） | [使用技能](skills/intro-drafter/SKILL.md) |
| **Paper Writer** | 证据门控的论文正文写作：从单段到整篇，每个事实性声明可溯源到你的材料或核验过的文献，引用经独立核查，绝不编造 | [使用技能](skills/paper-writer/SKILL.md) |
| **Paper Polish** | 忠于原意的语言润色：改语法、去 AI 腔、把握措辞分寸、中文稿改写为投稿级英文，可能动到含义的改动逐条标出请你确认 | [使用技能](skills/paper-polish/SKILL.md) |
| **Deep Research** | 综述级文献深度调研：多视角检索、逐条引用核验、MECE 分类综合与交叉对比，产出逐条回答研究问题的 survey 报告 | [使用技能](skills/deep-research/SKILL.md) |
| **Tech Paper Template** | 基于"技术类Full Paper思考模板"，辅助你一步步梳理论文的完整逻辑链 | [使用技能](skills/tech-paper-template/SKILL.md) |
| **Top-Tier ML Paper Planner** | 把诊断观察、设计原则、方法组件、贡献、实验和主图组织成可审稿的 claim-evidence 闭环，并给出逐节逐段蓝图 | [使用技能](skills/write-top-tier-ml-paper/SKILL.md) |
| **Benchmark Paper Template** | 专为 Benchmark/Evaluation 类论文设计，辅助梳理评估逻辑和实验设计 | [使用技能](skills/benchmark-paper-template/SKILL.md) |
| **Pre-Submission Reviewer** | 顶会审稿人视角！基于写作 Checklist 和英语语法易错点，对草稿进行全面审查 | [使用技能](skills/pre-submission-reviewer/SKILL.md) |
| **Figure Design Advisor** | 告诉 AI 你想表达什么，它会根据动机图/总览图/实验图的设计范式给出专业作图建议 | [使用技能](skills/figure-designer/SKILL.md) |
| **Draw.io Reconstruction** | 将参考图、论文图、架构图、幻灯片图或 UI 截图重建为可编辑 `.drawio` 文件，并导出 PNG 预览与视觉审计 | [使用技能](skills/drawio-reconstruction/SKILL.md) |

## 快速开始 (Quick Start)

把下方这段 Prompt 发给你的 AI 助手（Claude Code、Cursor、Codex 等）即可完成安装：

```
Help me install Supervisor-Skills from https://github.com/HKUSTDial/Supervisor-Skills with Skills.
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

## License

本项目采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 协议开源。欢迎非商业用途的分享与改编，但请注明出处。
