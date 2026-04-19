# Figure Designer

## 为什么重要

在顶会论文（SIGMOD、VLDB、ICML、NeurIPS）中，图表质量直接影响审稿人的第一印象。三张图承载了几乎全部的叙事重量：动机示例图（Figure 1，在第一页或第二页顶部）、方案概览图（在方法章节内）、实验结果图（在实验章节内）。审稿人在一分钟以内扫过这三张图，决定论文是否值得细读；图表质量差的论文，会在方法本身很强的情况下被拉下去。

设计一张好图，往往需要一到两天，这是正常且合理的投入。赶工一小时的学生，通常会产出一张字体极小的栅格截图，没有双重编码，图注写着"Figure 5: results comparison"。审稿人一眼就能看出来，论文的工艺信号急剧下降。把图表设计当作论文承重部分来对待、花数小时认真打磨的学生，产出的图表会让审稿人想继续读下去。

figure-designer 技能接收用户的叙事意图和上下文（研究领域、方法名称、目标会议），返回正确的设计范式、布局草图、标注指引、工具建议，以及针对通用规则集的质量控制审核。也支持审核模式：用户粘贴已有图表，技能对照规则进行审核。

## 核心框架

### 通用规则

五条规则适用于每一张图，不论类型。

| 规则 | 为什么重要 |
|---|---|
| 矢量格式导出 | PDF、EPS 或 SVG。栅格图（PNG、JPG）缩放后会失真，立刻把论文打上业余标签 |
| 缩放后字体不小于 8pt | Matplotlib 默认设置产出大画布上的微小字体；收小画布（例如 150x100pt）让字体随之放大到可读大小 |
| 对色盲友好的配色加双重编码 | 约 8% 的男性有色觉障碍；此外论文经常被黑白打印。永远不要只靠颜色区分，要将颜色与线型或标记形状配对 |
| 图注自成一体 | 第一句话说明核心发现，而不是说明图的类型。"Figure 5：我们的方法在 BIRD 上持续优于所有基线"比"Figure 5：性能对比"更有力 |
| Y 轴范围诚实 | 不要把 Y 轴从 59% 开始，来夸大一个 5 个百分点的差距；从 55% 或 50% 开始，加清晰标注，既诚实又能展示差异 |

违反其中任何一条规则，都是审稿人级别的红旗。技能在批准一个设计之前，会对每条规则进行审核。一篇有多处通用规则违规的论文，很少能在评审中挽回局面；审稿人的第一印象已经形成，内容需要付出加倍的努力来扭转。

### 范式一：动机示例图

动机示例图（Figure 1）是论文中最重要的单张图。它的任务是在 30 秒内传达：论文解决了什么问题，以及现有方法为何不够。它位于第一页或第二页顶部，紧接在 Introduction 的局限性段落之后。

三种经典范式：

- **运行示例加失败案例（最推荐）。** 给出一个具体的真实场景，展示现有方法如何在这个场景上失败。Text-to-SQL 的例子：一个具体的自然语言查询（"找出所有 2024 年发表了至少三篇论文的教授及其所在系"），当前方法输出的缺少 GROUP BY 并用红色标出的 SQL，以及用绿色标出的正确 SQL。失败很直观：审稿人看到了痛点。
- **现有方法与我们的方法对比。** 两列或两行布局：左侧展示现有方法的工作方式及其局限，右侧展示新方法及其优势。直接的视觉对比让读者瞬间看出区别。
- **性能预告图。** Figure 1 本身就是一张精心设计的性能图表，一眼看出新方法相对于基线的优势。只有在方法性能差距足够大、值得以结果开篇时才适用。

工具：PowerPoint 或 Figma。动机示例图通常混合文字、图标、箭头和代码片段，这在 Matplotlib 中很别扭，在 TikZ 中很痛苦。PowerPoint 最快；Figma 产出更精细的效果。图标可以来自 iconfont.cn 或类似资源。

### 范式二：方案概览图

方案概览图是方法章节的"灵魂"。它位于第 3 节或第 4 节开头，让直接跳到图表的审稿人能理解系统的架构和数据流。读到后面章节的审稿人应该能回来看这张图来找到方向。

![AFlow 方案概览图，三层架构含数据面、Agent 面和协调面](/assets/images/aflow_solution_overview.png)

图：AFlow 的方案概览图（ICLR 2025）。三面板流水线（搜索空间、AFlow 搜索、搜索结果）展示了经典的流水线范式。

三种经典范式：

- **流水线（最常用）。** 各阶段从左到右或从上到下流动：输入、阶段 1、阶段 2、……、输出。每个阶段是一个有标签的框，内部有子模块。AFlow 的 Figure 3（上图）是教科书式的例子：左侧搜索空间，中间 AFlow 搜索，右侧搜索结果。
- **系统架构图。** 系统边界作为大框，内部是交互组件，箭头显示控制流和数据流。Alpha-SQL 的 Figure 3 使用这种模式，展示 LLM-as-Action-Model、MCTS 搜索树展开和自监督奖励反馈的交互。
- **多层或多视角。** 竖向或横向分割，用于分层或双阶段架构。LEAD 的 Figure 3 将离线和在线阶段竖向分开，在线阶段的输出反馈进训练循环。

设计原则：模块化（每个核心组件都是有标签的框，没有无标签区域），数据流清晰（箭头除非不可避免否则不交叉），层次感（颜色、大小和位置传达层级），图文对应（模块名称与章节标题一致），输入输出明确（第一次阅读就能清楚看到方法的输入和输出）。

工具：draw.io 或 PowerPoint 起草，Figma 或 TikZ 精修。

### 范式三：实验结果图

实验结果图支撑具体的实证主张。根据数据形态选择图表类型，而不是根据美观程度。

| 图表类型 | 最适合 | 设计注意事项 |
|---|---|---|
| 分组柱状图 | 多方法、多数据集的整体性能对比 | 用饱和色突出自己的方法；基线用浅灰色 |
| 折线图 | 灵敏度分析、训练曲线、连续变量上的趋势 | 使用线型加标记形状加颜色（三重编码），黑白打印也能区分 |
| 热力图 | 相关矩阵、注意力权重、各方法各样本的性能 | 连续色阶（蓝-白-红，Viridis）；每个格子都标注数值 |
| 散点图 | 效率与效果的权衡 | X 轴效率，Y 轴效果；自己的方法应该落在右上角 |
| 箱线图 | 多次运行结果的分布 | 比只报均值更诚实；展示方差 |
| 雷达图 | 多维度方法对比 | 在比较 3-5 种方法、跨 5-6 个轴时有用 |

实验图专用设计规则：自成一体（图注第一句话说明发现），避免图表垃圾（不用 3D、不用不必要的阴影、不用繁忙背景），突出我们的方法（饱和色表示自己的方法，灰色或低饱和色表示基线），Y 轴范围诚实。

工具：Matplotlib 加 Seaborn，放在可复用的绘图脚本（如 `plot_utils.py`）中，统一管理配色、字体和线宽默认值。数据流水线用 Pandas 或 Excel。避免手绘图表；实验结果图必须能从代码再现。统一默认值也确保了全文图表的视觉一致性，这是 Nice Presentation 的重要加分项。

### 工具选型矩阵

| 图表类型 | 首选 | 备选 | 原因 |
|---|---|---|---|
| 动机示例图 | PowerPoint、Figma、OmniGraffle | draw.io | 混合文字、图标、箭头、代码片段；需要灵活布局 |
| 方案概览图 | draw.io、PowerPoint | Figma、TikZ | 流程图和架构图；需要清晰的模块框和箭头 |
| 实验结果图 | Matplotlib + Seaborn | TikZ、PGFPlots | 必须从代码生成以确保可复现性 |
| 数学示意图 | TikZ | Matplotlib | 优先 native LaTeX 集成 |

## 核心原则

- **矢量格式必须**：PDF、EPS 或 SVG。栅格图立刻扣分。
- **小画布大字体**：收小画布（150x100pt）让字体变大，而不是默认大画布上的微小字体。
- **双重编码保可及性**：颜色加线型加标记形状。
- **图注自成一体、发现在前**：图注第一句话说明这张图证明了什么。
- **运行示例贯穿全文**：Figure 1 的动机示例在方法和实验中复现。
- **突出我们的方法**：饱和色表示新方法，灰色或低饱和色表示基线。
- **Y 轴诚实**：不要从 59% 开始来夸大 5 个百分点的差距。
- **流水线、架构图、多层图**是方案概览图的三种范式，根据方法的结构选择。
- **运行示例加失败案例、现有方法 vs 我们的方法、性能预告图**是动机示例图的三种范式，根据叙事选择。

## 示例

以 Alpha-SQL 的 Figure 1（动机示例图）通过技能设计为例。

- **类型识别**：动机示例图。
- **范式**：运行示例加失败案例。Alpha-SQL 的主张是，零样本 LLM 在没有结构化搜索的情况下无法完成复杂的 Text-to-SQL；一个具体的失败案例让这个主张变得直观。
- **布局草图**：三面板竖向排列。顶部面板：自然语言查询（"列出所有……"）。中间面板：当前方法的 SQL 输出，缺失 JOIN 用红色标出，加上错误的查询结果。底部面板：Alpha-SQL 的 SQL 输出，正确的 JOIN 用绿色标出，加上正确的结果。
- **标注**：使用真实实体名称（真实的数据库表名和列名），而不是占位符。真实查询，真实输出。
- **配色方案**：ColorBrewer 定性配色用于三个面板；红色用于失败标注，绿色用于成功标注。
- **工具**：PowerPoint 起草，导出为 PDF。
- **通用规则审核**：矢量（通过，PDF 导出后）；字体（通过，若设为 10pt）；对色盲友好（警告，红绿配色是色盲最糟糕的情况；需要给每种颜色配上图标，例如叉号和勾号，实现双重编码）。

审核发现了红绿问题。修复方式是双重编码：红色框加显式"错误"标注或叉号图标，绿色框加"正确"标注或勾号图标。这样这张图在黑白打印和色盲读者场景下都能正确阅读。

## 用插件实操

按照 [顶层 README](../../../../README.md#快速安装) 安装插件后，自然语言即可触发。技能会在 "design a figure"、"draw Figure 1"、"plot experiment results"、"choose the right chart type"、"which figure tool to use"、"figure looks unprofessional" 等短语上自动触发。提供意图（这张图要传达什么）、上下文（研究领域、方法名称、目标会议），以及如果可能的话一张草图的图片；技能返回范式建议、布局草图、标注指引、工具建议，以及对通用规则的审核。

对于图表审核，技能同时支持视觉路径（粘贴图片或提供 PNG、PDF 或 SVG 的路径）和文字路径（用文字描述图表）。视觉路径直接检查字体可读性、配色和图表垃圾；文字路径则将这些规则标记为"用户需自行核验"。

## 出处

改编自：

- [archive/v1-source/1_Guide/04_Scientific_Plotting/4.1_Motivated_Example_Figure.md](/archive/v1-source/1_Guide/04_Scientific_Plotting/4.1_Motivated_Example_Figure.md)
- [archive/v1-source/1_Guide/04_Scientific_Plotting/4.2_Solution_Overview_Figure.md](/archive/v1-source/1_Guide/04_Scientific_Plotting/4.2_Solution_Overview_Figure.md)
- [archive/v1-source/1_Guide/04_Scientific_Plotting/4.3_Experimental_Results_Figure.md](/archive/v1-source/1_Guide/04_Scientific_Plotting/4.3_Experimental_Results_Figure.md)
- [archive/v1-source/1_Guide/04_Scientific_Plotting/4.4_绘图Checklist与工具速查表.md](/archive/v1-source/1_Guide/04_Scientific_Plotting/4.4_绘图Checklist与工具速查表.md)
- 插件 SKILL.md：[/plugins/phd-research/skills/figure-designer/SKILL.md](/plugins/phd-research/skills/figure-designer/SKILL.md)
- 插件参考资料：[/plugins/phd-research/skills/figure-designer/references/motivated-example.md](/plugins/phd-research/skills/figure-designer/references/motivated-example.md)、[/plugins/phd-research/skills/figure-designer/references/solution-overview.md](/plugins/phd-research/skills/figure-designer/references/solution-overview.md)、[/plugins/phd-research/skills/figure-designer/references/experimental-results.md](/plugins/phd-research/skills/figure-designer/references/experimental-results.md)

---

[English](../../../en/skills/figure-designer/overview.md) | [中文]
