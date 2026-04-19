# Benchmark 论文结构与写作

## 为什么重要

Benchmark 论文的引言是整篇论文的压缩版本，其叙事主轴不是"关键思路或机制"（技术论文
的主轴），而是"评估盲区加 Benchmark 设计理由"。用技术论文的主轴来写 Benchmark 论文
的引言，会在 NeurIPS Datasets and Benchmarks、ICLR、ICML、ACL、EMNLP 和 CVPR
上产生系统性的审稿人困惑。常见的失败模式包括：引言读起来像数据集发布公告（缺少
"The Gap"段落和"Design Considerations"段落），缺少 Figure 1（Running Example），
缺少 Table 1（Benchmark Comparison），流程描述没有 Figure 2，实验章节跳过了
Finding X 加粗总结，贡献列表没有映射到具体章节。这些问题各自都能单独修复，
但累积的重量会让论文沉没。

这个技能将已完成的研究组织成一篇可提交的论文。它规定了六段式引言框架、正文章节
结构和页面预算、图表放置指南、Benchmark 论文的标志性写作技法，以及附录规划。
顶部的强制门禁在任何写作开始之前确认前置条件已就位（Gap Statement、设计文档、
流程规格、实验计划）。没有前置条件，论文就没有可组织的内容。

## 核心框架

### 引言：六段式框架

引言遵循特定的逻辑链。每个部分对应大约一段话，顺序不可颠倒。

**第一段：背景与核心场景（约 1 段）。** 建立更广泛任务或领域在真实场景中的重要性。
展示该领域已取得快速进展，引用近期进展。使用精心设计的 Running Example（Figure 1）
来展示任务的复杂性及人类专家如何处理它。Figure 1 是论文中最重要的图之一，
必须精心打磨。语气：权威，引用知名工作。

参考：StatQA 使用完整的统计分析工作流；nvBench 2.0 展示同一歧义查询的多种有效解释；
VisJudge-Bench 在信达雅三个维度上对比正反例。

**第二段：现有 Benchmark 的局限与评估盲区（约 1 段）。** 调研现有 Benchmark 测量什么，
公平地承认其贡献。识别它们共享的隐含假设并将其明确化。将评估盲区表述为至多三点，
具体而非模糊。强烈推荐：提供 Benchmark Comparison Table（Table 1），逐项对比特征
维度，让盲区不言而喻。这是论文中最重要的段落。它应该让读者心想："我从未想到这一点，
但显然很重要。"

参考：nvBench 2.0 Table 1 从六个维度对比了七个 Benchmark；VisJudge-Bench Table 1
从三个评估维度对比了七个 Benchmark。

**第三段：研究问题（约 1 段）。** 将盲区转化为 2-3 个具体的研究问题。RQ 覆盖范围
应包括：（1）如何构建合适的 Benchmark，（2）当前模型的能力边界在哪里，（3）模型
与人类专家的差距是什么。RQ 锚定整个实验章节。

参考：StatQA 使用 Q1 如何评估？Q2 LLM 能力如何？Q3 人类 vs. LLM？

**第四段：设计考量（约 1 段）。** 这一段是 Benchmark 论文独有的。在介绍解决方案之前，
先阐明该领域一个好的 Benchmark 应具备什么属性。这为后续设计选择提供了理由。
明确陈述设计要求（多样覆盖、细粒度诊断、可扩展性、质量保证）。这是解释 Benchmark
为何如此设计的逻辑基础。

参考：nvBench 2.0 陈述："This benchmark should include diverse ambiguous queries,
multiple valid outputs, reasoning paths, and broad domain coverage."

**第五段：我们的 Benchmark 加关键发现预览（约 1-2 段）。** 正式介绍 Benchmark 的名称、
规模和关键设计选择。用一到两句话突出构建方法创新。引用 Figure 1 和 Table 1。
概述 2-3 个最令人意外的实证发现，以吸引读者。使用具体数字："我们评估了 15 个模型，
覆盖 6 个维度。"语气：自信但精准。

参考：StatQA 将其核心思路表述为"reversing this process by synthesising the
question Q based on target answers A."

**第六段：贡献（约 1 段，项目列表）。** 通常 3-4 条贡献，每条对应一个论文章节：

1. 我们识别了 [盲区] 并提出了 [名称]，首个用于 [能力] 的 Benchmark。（-> §1-2）
2. 我们设计了 [流程创新]，实现了 [质量或规模指标]。（-> §2）
3. 我们对 [N] 个模型进行了全面评估，揭示了 [关键发现]。（-> §4）
4. （可选）我们提出了 [配套方法]，将 [指标] 提升了 [幅度]。（-> §3）

### 引言必须有的图表

**Figure 1：Running Example（必须有）。** 论文中最重要的图。要求：用一个具体示例
说明评估盲区；展示现有评估遗漏了什么与新 Benchmark 捕获了什么；自包含（读者仅凭
这张图就能把握论文的核心思想）；尽可能放在第 1-2 页的显眼位置。三种常见设计模式：
分裂视图（左边"现有评估" vs. 右边"我们的评估"）、流程视图（一个输入，高亮多个
评估维度）、对比视图（同一模型输出在旧标准和新标准下的评分对比）。

**Table 1：Benchmark Comparison（必须有）。** 与 5-8 个现有 Benchmark 对比。
最右列是关键区分项：

```
| Benchmark | 年份 | 规模 | 维度1 | 维度2 | 维度3 | 我们的关键特性 |
|-----------|------|------|-------|-------|-------|--------------|
| Prior-1   | 20XX | N    | 是    | 否    | 是    | 否            |
| Prior-2   | 20XX | N    | 是    | 是    | 否    | 否            |
| Ours      | 2025 | N    | 是    | 是    | 是    | 是            |
```

### 正文章节结构

**第 2 章：所提出的 Benchmark（3-4 页，核心章节）。**

```
2.1 设计目标与任务范围
    - 明确陈述 G1-G4
    - 定义范围内 vs. 范围外

2.2 Benchmark 构建流程
    - 流程概述段落
    - Figure 2：流程图（必须有）
    - 附输入、操作、输出的详细步骤
    - 质量控制措施
    - 标注协议（如涉及人工标注）

2.3 Benchmark 特征描述
    - Table 2：数据集统计（划分、类别、规模）
    - Figures 3-4：分布图（分类学、难度、长度）
    - Figure 5：数据示例（2-3 个有代表性样本）
    - 与现有 Benchmark 在规模和覆盖度上的对比
```

**第 3 章：专用模型（1-2 页，可选）。**

```
3.1 动机：Benchmark 如何支持模型改进
3.2 方法：训练信号加优化技术
3.3 实现细节
```

**第 4 章：实验与实证发现（4-5 页）。**

```
4.1 实验设置
    - 模型（按类型分组）、指标、提示、实现

4.2 整体性能
    - Table 3：所有模型 × 所有指标（论文中最大的表）
    - 最佳加粗，次优加下划线
    - 分析后的 Finding 1

4.3 细粒度分析（按 RQ 组织）
    - RQ1 分析 -> Finding 2
    - RQ2 分析 -> Finding 3
    - RQ3 分析 -> Finding 4
    - 每个分析附支撑图表

4.4 案例研究
    - 2-4 个附定性分析的示例
    - 成功案例、失败案例、令人意外的案例
```

**第 5 章：讨论与研究机会（约 1 页）。** 基于 Finding，讨论如何提升模型在已识别
盲区上的能力、人机协作模式、Benchmark 扩展方向（新模态、语言、领域），以及当前
Benchmark 的局限性。

**第 6 章：相关工作（约 1 页）。** 组织为 2-3 个子节：[任务特定] Benchmark、[领域]
评估方法论、大型语言模型中的 [相关能力]。包含一张对比表，可以是扩展的 Table 1
或专注于方法论差异的新表。放置位置说明：相关工作可以在实验前或实验后。在实验前
（如 VisJudge-Bench）强调定位；在实验后（如 StatQA 和 nvBench 2.0）让发现先说话。

**第 7 章：结论（约 0.5 页）。** 用 1-2 句话重述盲区和 Benchmark。总结关键发现，
引用 Finding 编号。重述开放问题和未来方向。

### 图表放置指南

| 项目 | 位置 | 用途 | 优先级 |
|---|---|---|---|
| Figure 1 | 第 1-2 页 | Running Example | 必须 |
| Table 1 | 第 2-3 页 | Benchmark Comparison | 必须 |
| Figure 2 | 第 3-4 页（§2.2） | 构建流程 | 必须 |
| Table 2 | 第 4-5 页（§2.3） | 数据集统计 | 必须 |
| Figures 3-4 | 第 4-5 页（§2.3） | 分布图 | 高 |
| Figure 5 | 第 5 页（§2.3） | 数据示例 | 高 |
| Table 3 | 第 6-7 页（§4.2） | 整体性能 | 必须 |
| Figures 6+ | 第 7-8 页（§4.3） | 分析图表 | 高 |

### Benchmark 论文关键写作技法

1. **Finding X 总结**：每次主要分析后加粗高亮（完整模板见
   [bench-experiments](../bench-experiments/overview.md)）。
2. **设计理由优先于描述**：对每个选择，解释为什么，而不仅仅是做了什么。
   审稿人始终追问原因；主动阐明，预先化解。
3. **具体数字**："我们评估了 15 个模型，覆盖 6 个维度"，而非"多个模型"。
   具体数字比模糊表述更可信。
4. **主动定位**："the FIRST benchmark to..." 或 "Unlike prior work, we..."。
   不要把贡献埋在被动语态里。
5. **示例驱动论证**：抽象主张始终配具体示例。一个示例胜过三段描述。
6. **附录策略**：将详细内容移至附录（完整结果、标注指南、更多示例、使用的提示）。
   正文应能一遍读完。

### 附录规划

Benchmark 论文的标准附录章节：A（完整实验结果，未删减版），B（标注指南和界面截图），
C（额外数据示例），D（评估使用的提示），E（扩展相关工作或分类学详情），F（伦理
考量和数据表）。

## 核心原则

- **六段式引言框架**：背景、局限性、研究问题、设计考量、我们的 Benchmark 加发现
  预览、贡献。不跳过任何部分。
- **设计考量段落**：Benchmark 论文独有。先阐明好的 Benchmark 应有什么，然后展示
  你的满足了标准。
- **五个必须有的图表**：Figure 1 Running Example、Table 1 Benchmark Comparison、
  Figure 2 Pipeline、Table 2 Statistics、Table 3 Overall Performance。缺少任何
  一个都会在提交前审核中被标记。
- **Finding X 加粗总结**：Benchmark 论文的标志性写作技法。每次主要分析对应一个 Finding。
- **贡献-章节映射**：引言中的每条贡献都映射到一个章节编号。没有孤立的贡献。
- **相关工作放置选择**：在实验前强调定位，在实验后让发现先说话。两种都有效；
  根据论文最强的角度来选择。

## 示例

考虑 VisJudge-Bench 完成实验后的情况。论文结构如下组织。

**引言。** 第一段建立可视化评估对 AI 生成图表应用和人类分析工具都很重要，Figure 1
展示一张准确但视觉误导的图表，以及一张美观但事实错误的图表。第二段调研七个现有
图表评估 Benchmark，识别出共享假设：质量要么是审美的要么是事实性的（从来不同时
是），并呈现 Table 1 对比七个 Benchmark 的三个评估维度，每个先前 Benchmark 至少
缺失两个维度。第三段围绕构建多维 Benchmark、测量当前模型性能、对比模型与人类专家
提出三个研究问题。第四段指出好的图表评估 Benchmark 需要同时具备信、达、雅，
加上细粒度子维度。第五段命名 Benchmark（VisJudge-Bench），说明规模（跨六个子维度
的一万五千张候选图表），预告三个 Finding。第六段列出四条贡献，每条映射到一个章节。

**正文。** 第 2 章呈现设计目标、范围、流程（Figure 2 展示自适应生成加专家标注流程，
每个箭头标注数据量）和统计特征（Table 2 数据集统计，Figures 3-4 分布图，Figure 5
数据示例）。第 3 章呈现 VisJudge 配套方法（GRPO 训练的评估器）。第 4 章呈现实验，
从 Table 3 整体性能开始，然后按研究问题组织的 §4.2-4.4，每次主要分析后加粗标注
Finding 1-4。第 5 章讨论研究机会。第 6 章相关工作。第 7 章结论，按编号引用 Finding。

**图表。** 五个必须有的项目全部就位：Figure 1 Running Example 在第 2 页，Table 1
Benchmark Comparison 在第 3 页，Figure 2 Pipeline 在第 4 页，Table 2 Statistics
在第 5 页，Table 3 Overall Performance 在第 7 页。另有四张支撑细粒度分析的图表。

**附录。** 按标准结构 A-F 排列：完整实验结果在 A，标注界面截图在 B，五十个额外
数据示例在 C，所有评估提示在 D，扩展分类学详情在 E，包含数据表的伦理考量在 F。

StatQA 和 nvBench 2.0 遵循相同结构，各自有不同的盲区、分类学、流程和发现。

## 用插件实操

按照 [顶层 README](../../../../README.md) 安装插件后，自然语言即可触发。技能会在
"gap analysis, benchmark design, construction, and experiment planning are
ready"、"organise them into a submission-ready paper"、"Introduction structure,
section organisation, figure and table placement" 等短语上自动触发。提供前置阶段
的交付物，技能会引导完成六段式引言、正文结构、图表放置和贡献对齐。

## 出处

改编自
[archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md)
及插件文件
[/plugins/phd-research/skills/bench-paper-structure/SKILL.md](/plugins/phd-research/skills/bench-paper-structure/SKILL.md)。
---

[English](../../../en/skills/bench-paper-structure/overview.md) | [中文]
