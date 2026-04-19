# Pre-Submission Reviewer

## 为什么重要

投稿截止前三到五天，认真的外部审核效益最高。此时论文结构已经锁定，实验已经完成，还有时间做一次最终审核，但已经没有时间大规模重写。在这个窗口内进行结构化审核，能捕捉到那些会把本来很强的论文击垮的问题：Introduction Flowchart 断裂、大多数段落缺少主题句、引用命令缺少不间断空格、图表失真，以及把论文打上 AI 代笔标签的违禁 AI 语气词汇。

pre-submission-reviewer 技能接收完整论文或关键章节，对五个维度（宏观逻辑、写作细节、英文语法、LaTeX 格式、图表质量）进行结构化审核，每条发现都附有严重性标签和具体的修改建议。它强制执行原版课程的写作细节核查清单中的机械性规则（不用 em-dash、不用违禁 AI 语气词、段落引导纪律、主题句纪律、引用格式统一），并指出非母语英文作者最常见的问题模式。

输出的不是重写稿，而是一份有优先级的问题列表，作者决定修哪些，CRITICAL 问题会阻止投稿。作者保留编辑控制权；技能标记问题、建议修改，但不代劳重写。

## 核心框架

### 五维审核

审核从五个角度依次检查论文，每个维度有自己的核查清单，产出独立的发现。

**维度一：宏观逻辑。** Introduction 的六段式 Flowchart 是否完整？贡献点是否与方法模块和章节编号一一对应？实验是否验证了论文的主要主张而不是边缘主张？Related Work 是否完整？运行示例从 Introduction 到实验是否保持一致？每一处链断裂都是 CRITICAL。

**维度二：写作细节。** 每个段落是否有主题句（"段落引导文"）？段落之间是否有流畅的过渡？是否有段落超过十行需要拆分？Abstract 是否覆盖了问题、方法和结果？孤立段落（与前后没有联系）和缺少主题句是 MAJOR 问题。审稿人读到一个没有主题句的段落，需要从上下文中重建这段话的目的，这是高认知成本的操作。

**维度三：英文语法。** 非母语作者的常见陷阱：冠词用法（a、an、the），主谓一致（尤其是第三人称单数），时态一致（Related Work 用过去式，方法用现在式，实验用过去式），被动语态过度使用，which 与 that 的混用，以及中式英语模式。长句应该在"Specifically,"处拆分。

**维度四：LaTeX 格式。** 公式连续编号且每个有编号的公式都被引用。图表和表格有详细的图注。引用使用正确的命令加不间断空格（例如 `ResNet~\cite{X}` 而不是 `ResNet \cite{X}`）。标签使用下划线，不用空格或连字符（`\label{fig:system_overview}` 而不是 `\label{system overview}`）。图表使用矢量格式。页数合规。

**维度五：图表质量。** 矢量格式。缩放后字体足够大。对色盲友好的配色加双重编码。图注自成一体且第一句话说明发现。无图表垃圾（3D 效果、过多网格线、繁杂背景）。动机示例图具体且能揭示失败。方案概览图的标签与章节标题一致。

### 严重性分类

每条发现都附有标签：

- **CRITICAL**：阻止投稿。例如：贡献点与章节不对应；Introduction Flowchart 断裂；运行示例缺失；最终稿中出现栅格图；关键基线缺失；超出页数限制。
- **MAJOR**：审稿人在第一轮会提出。例如：三个及以上段落缺少主题句；五处及以上出现 em-dash；三处及以上出现某个违禁 AI 语气词；Table 1 对比缺失；图表类型与数据不匹配。
- **MINOR**：打磨层面。例如：两个可以拆分的长句；默认 Matplotlib 样式；单个冠词错误。

CRITICAL 问题应该在提交之前解决。MAJOR 问题应该在时间允许的情况下修复。MINOR 问题由作者自行判断。这套分类是审稿人风格的：在第一轮就会导致拒稿意见的问题是 CRITICAL 或 MAJOR；审稿人会作为次要打磨意见提出的是 MINOR。

### 违禁词汇与 em-dash 扫描

专项扫描覆盖了将专业学术文章与 AI 代笔稿件区分开来的机械性写作规则。这是硬规则检查；作者不能因为喜欢某个被禁词就绕过它。

**em-dash 用作句子连接词按项目约定是被禁止的**（见 [CONTRIBUTING.md](/CONTRIBUTING.md)）。替换方式是逗号、冒号或句号分断。一篇论文中出现五处及以上 em-dash 是 MAJOR。

**违禁 AI 语气词汇**，来自审稿人经验整理：

- 创新描述词：innovative、pioneering、revolutionary paradigm、transformative framework。
- 性能对比词：superior、surpass、excel、remarkable、unprecedented、achieves SOTA、breakthrough performance。
- 贡献概括词：general-purpose、is capable of。
- 逻辑连接词：notably、yet、yielding、at its essence。
- 动词：encompass、differentiate、reveal、underscore、surpass、show great potential、exhibit superior capability、exceed、pave the way for、highlight the potential of。
- 短语：profound challenges（非自然的英语搭配）、stems from。
- 形容词：rigid。
- 动词：impede。

每个被禁词或短语的出现都附有行号引用。某个被禁词出现三次及以上触发 MAJOR；低于三次是 MINOR。一篇积累了若干个 MAJOR 违禁词汇标记的论文，即使作者确实自己写了内容，读起来也像 AI 代笔；去掉这些词汇能还原论文的人声。

### 逐节审核

每个章节都有自己的标准结构，审核会把提交的章节与对应指南进行核对：

- **Abstract**：五句公式（问题、为什么、挑战、方法、结果）。最后一句有具体数据集和数字。
- **Introduction**：六段（见 [intro-drafter](../intro-drafter/overview.md)）。每条主张都有对应的交付。
- **问题定义**：文字描述、正式定义、示例，依此顺序。
- **框架或方法**：先架构，再工作流，再组件细节。每个模块必须是新颖的或至少是必要的。
- **实验**：过去式。至少三个数据集。整体对比在前，消融实验在后，可扩展性或灵敏度分析最后。每个主张都有数据支撑。
- **Related Work**：先总结类别，再与当前论文对比。直接相关工作点名其局限；间接相关工作给予适当尊重。不复制粘贴。
- **结论**：现在完成时。总结贡献，不重复 Introduction。

## 关键核查项

- **宏观逻辑完整**：Introduction 六段完整且逻辑连贯；贡献点对应章节。
- **运行示例前后一致**：贯穿 Introduction、方法、实验。
- **每段有主题句**；没有段落超过十行。
- **英文准确性**：冠词、时态、主谓一致、which 与 that 的区分、被动语态。
- **LaTeX 合规**：引用中的不间断空格、下划线标签、矢量图、引用格式符合会议要求。
- **图表质量通用规则**（矢量、字体大小、双重编码、图注自成一体、无图表垃圾、Y 轴诚实）。
- **不用 em-dash 作为连接词。**
- **违禁 AI 语气词汇不出现三次及以上。**
- **章节结构符合标准指南**：Abstract 五句，Introduction 六段，实验用过去式且至少三个数据集。

## 示例

考虑一篇假设的投稿 VLDB 的 Text-to-SQL 论文。审核发现：

- **维度一（宏观逻辑）**：Introduction 有研究背景、局限性和方案总览，但没有挑战段落。在 VLDB 这是 CRITICAL；作者必须在提交前插入挑战段落。
- **维度二（写作细节）**：第 2、4、5 段缺少主题句。MAJOR；作者应该为每段加一句引导句。
- **维度三（语法）**：实验章节时态混用（现在式和过去式交替）。MAJOR；统一改为过去式。
- **维度四（LaTeX）**：第 3 节的引用在 14 处缺少不间断空格。MAJOR；做查找替换。标签"fig:solution-overview"使用了连字符。MINOR；改为下划线。
- **维度五（图表）**：Figure 5 是栅格 PNG，打印后会失真。CRITICAL；重新生成为 PDF。Figure 1 只用了红色和绿色，没有双重编码。MAJOR；加上叉号和勾号图标。
- **违禁词汇扫描**："surpass"出现 6 次，"revolutionary"出现 1 次，"achieves SOTA"出现 3 次。"surpass"和"achieves SOTA"是 MAJOR；"revolutionary"是 MINOR。
- **em-dash**：7 处用作句子连接词。MAJOR；改为逗号或句号分断。

最终得分：6/10。投稿建议：还需要一到两天的工作。作者先修 CRITICAL 问题（插入挑战段落、重新生成 Figure 5 为 PDF），再修 MAJOR 问题（补主题句、统一时态、修引用空格、Figure 1 双重编码、删违禁词汇、清理 em-dash）。MINOR 问题视时间允许再处理。

## 用插件实操

按照 [顶层 README](../../../../README.md#快速安装) 安装插件后，自然语言即可触发。技能会在 "review this paper"、"audit before submission"、"check the draft"、"find issues"、"proofread"，或者投稿截止前一周内自动触发。提供论文正文（粘贴、LaTeX 源码或 PDF 提取），技能返回五维审核结果、最终得分和投稿建议。

工作流建议：在截止前三到五天运行这个技能，修复 CRITICAL 问题和时间允许范围内的 MAJOR 问题，然后考虑在修完之后再运行一次确认没有回归。与此并行的技能是 [figure-designer](../figure-designer/overview.md)（图表专项审核细节）和 [vibe-research-workflow](../vibe-research-workflow/overview.md)（AI 辅助润色纪律）。

## 出处

改编自：

- [archive/v1-source/1_Guide/03_Paper_Writing/3.5_写作细节与Checklist.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.5_写作细节与Checklist.md)
- 插件 SKILL.md：[/plugins/phd-research/skills/pre-submission-reviewer/SKILL.md](/plugins/phd-research/skills/pre-submission-reviewer/SKILL.md)

---

[English](../../../en/skills/pre-submission-reviewer/overview.md) | [中文]
