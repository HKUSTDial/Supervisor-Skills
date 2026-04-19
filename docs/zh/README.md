# Supervisor-Skills 课程体系

本目录是技能包的人类读者镜像，将"博士生科研技能"系列课程整理为以技能为索引的中文导读，独立于任何 AI 助手即可使用。本目录中的每一章，都与 `plugins/phd-research/skills/` 下的某个 SKILL.md 文件一一对应：导读章节讲解方法论，SKILL.md 负责执行。

课程覆盖技术论文与 Benchmark 论文两类的完整生命周期，以 NeurIPS、ICML、ICLR、VLDB、SIGMOD、KDD 及同类顶会为目标。技术类与立场类论文走一条线：idea 验证、颠覆式创新探测、论文框架搭建、图表设计、投稿前审核。Benchmark 与 Evaluation 类论文走另一条线：评估盲区分析、Benchmark 架构设计、数据构建、实验规划、论文结构、投稿前核对。两条路径在同一插件中并存，阶段彼此独立，`bench-writing` 作为 Benchmark 路径的编排器管理自身的阶段 DAG。

## 推荐阅读路径

正在写第一篇顶会论文的博士生，建议按以下顺序阅读：

- [基础篇：论文质量评判（4N 框架）](foundations/paper-quality.md)，整套课程的评判基准。
- [Idea Evaluator](skills/idea-evaluator/overview.md)，在投入数月精力之前，先淘汰弱 idea、打磨有潜力的想法。
- [Disruptive Innovation Scout](skills/disruptive-innovation-scout/overview.md)，当 idea-evaluator 的范式探测信号为"颠覆候选"时使用。
- [Tech Paper Template](skills/tech-paper-template/overview.md)，在动笔写任何段落之前，先锁定完整的论文逻辑骨架。
- [Intro Drafter](skills/intro-drafter/overview.md)，将骨架转化为六段式 Introduction 大纲。
- [Figure Designer](skills/figure-designer/overview.md)，规划承载论文叙事重量的三张核心图。
- [Pre-Submission Reviewer](skills/pre-submission-reviewer/overview.md)，投稿截止前三到五天的最终审核。
- [案例研究](#案例研究)，在真实发表的论文中观察上述框架的实际应用。

AI 辅助工作流的使用方式，请阅读 [Vibe Research Workflow](skills/vibe-research-workflow/overview.md)。这个技能与写作流水线正交，而非串行：无论是在写代码、画图，还是在写文字，相关规则和工具选择都适用。

如果写的是 Benchmark 或 Evaluation 论文，阅读顺序不同。Benchmark 管线比技术论文更强调阶段先后顺序，每一步都必须在下一步开始前完成；编排器会在入口先把整条管线呈现给用户：

- [Bench Writing 编排器](skills/bench-writing/overview.md)，识别当前阶段并路由到正确的子技能。
- [Bench Gap Analysis](skills/bench-gap-analysis/overview.md)，定位驱动 Benchmark 存在的评估盲区。
- [Bench Design](skills/bench-design/overview.md)，设计 Benchmark 架构：目标、范围、分类学、评估框架、可选配套方法。
- [Bench Construction](skills/bench-construction/overview.md)，设计带质量门控与统计特征的数据构建管道。
- [Bench Experiments](skills/bench-experiments/overview.md)，以 Finding-X 式洞察为中心规划实验。
- [Bench Paper Structure](skills/bench-paper-structure/overview.md)，搭建 Introduction 六段式与章节结构。
- [Bench Checklist](skills/bench-checklist/overview.md)，投稿前的把关闸门。

已经遇到具体瓶颈的读者，可以跳过阅读顺序，直接跳到对应章节。例如，Introduction 逻辑链断了，直接去 [Intro Drafter](skills/intro-drafter/overview.md)；纠结用哪种图表工具，直接去 [Figure Designer](skills/figure-designer/overview.md)；不确定 Benchmark 的 gap 究竟在哪，直接去 [Bench Gap Analysis](skills/bench-gap-analysis/overview.md)。

## 快速索引

### 基础篇

- [论文质量：4N 框架](foundations/paper-quality.md)

### 技术论文技能

- [Idea Evaluator](skills/idea-evaluator/overview.md)
- [Disruptive Innovation Scout](skills/disruptive-innovation-scout/overview.md)
- [Intro Drafter](skills/intro-drafter/overview.md)
- [Tech Paper Template](skills/tech-paper-template/overview.md)
- [Figure Designer](skills/figure-designer/overview.md)
- [Pre-Submission Reviewer](skills/pre-submission-reviewer/overview.md)
- [Vibe Research Workflow](skills/vibe-research-workflow/overview.md)

### Benchmark 论文技能

- [Bench Writing（编排器）](skills/bench-writing/overview.md)
- [Bench Gap Analysis](skills/bench-gap-analysis/overview.md)
- [Bench Design](skills/bench-design/overview.md)
- [Bench Construction](skills/bench-construction/overview.md)
- [Bench Experiments](skills/bench-experiments/overview.md)
- [Bench Paper Structure](skills/bench-paper-structure/overview.md)
- [Bench Checklist](skills/bench-checklist/overview.md)

### 案例研究

- [ICML 2025，Alpha-SQL 写作剖析](case-studies/alpha-sql.md)
- [ICLR 2025，AFlow 写作剖析](case-studies/aflow.md)
- [VLDB 2026，LEAD 写作剖析](case-studies/lead.md)

## 如何与 AI 助手配合使用

每个技能的 SKILL.md 文件都是自包含的结构化指令，可直接接入 AI 助手执行。安装方式见顶层 [README](../../README.md#快速开始)。文档树与 SKILL.md 保持同步更新：导读章节讲解方法，SKILL.md 负责执行。典型的工作方式是：读一遍对应章节，然后用自然语言（例如"帮我评估这个 idea"、"起草 Introduction"、"投稿前审核一下"）触发对应技能。

导读章节不能替代 SKILL.md 文件。SKILL.md 是技能行为的权威规范，包含完整的完整性核查、输出格式和模式选项。导读章节为人类读者精炼了方法论，并附有示例和教学性说明，而这些内容是 SKILL.md 所容纳不下的。

偏好阅读英文的读者，可以随时通过每个文件底部的语言切换链接切换到英文版。

---

[English](../en/README.md) | [中文]
