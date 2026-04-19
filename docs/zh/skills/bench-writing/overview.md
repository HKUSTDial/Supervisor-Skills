# Benchmark 写作编排器

## 为什么重要

博士生为 NeurIPS Datasets and Benchmarks、ICLR、ICML、ACL、EMNLP 或 CVPR
撰写 Benchmark 论文时，面对的问题形态与写技术论文截然不同。技术论文推销一个方法，
审稿人关注方法是否超越基线、消融实验是否诚实。Benchmark 论文推销的是一个新的评估维度、
一套系统性的测量基础设施，以及一批关于模型能力的实证发现。审稿人问的是：评估盲区是否真实、
构建流程是否可复现、发现是否足够令人意外、未来工作是否能在此基础上继续推进。
把两类论文混为一谈，会产生典型的拒稿模式：Benchmark 论文读起来像数据集发布公告，
没有可辩护的评估盲区；流程描述压缩到两段话，缺少审稿人期待的 Figure 2；
实验章节满是排行榜数字，却没有令 Benchmark 论文具有可引用性的 "Finding X" 提炼。

bench-writing 编排器是整个工作流的入口。它检测当前项目所处阶段（评估盲区分析、设计、
数据构建、实验、论文结构、提交检查），然后将用户路由至对应的子技能，而不是试图在
单次响应中处理全部阶段。每个子技能都有独立的强制门禁，阻止跳过前置阶段。
这个顺序是经过深思熟虑的：跳过评估盲区分析直接开始流程设计，是新手 Benchmark
作者最常见的失败模式，而门禁就是为了在学生耗费三个月构建出一条找不到可辩护盲区的流水线之前，
提前截住这个错误。

## 核心框架

### 叙事主轴：Benchmark 论文对比技术论文

两类论文的核心理念在几乎每个维度上都存在差异。Benchmark 论文不是"弱化版的技术论文"，
而是针对不同审稿人问题、进行了完全不同叙事优化的论文形态。

| 维度 | 技术论文 | Benchmark 论文 |
|---|---|---|
| 核心主张 | 我的方法更好 | 这个评估维度被忽视了 |
| 问题定义的角色 | 一句话陈述目标 | 问题定义本身即贡献（定义评什么、如何量化、能揭示什么洞察） |
| 引言主轴 | 关键思路或机制 | 评估盲区加 Benchmark 设计理由 |
| 主体章节 | 方法（最大章节） | 构建流程是核心；配套方法是加分项 |
| 实验目标 | 证明 SOTA | 揭示模型能力边界，为未来研究提供深层洞察 |
| 关键图表 | 架构图 | Benchmark 对比表、构建流程图、多维分析图 |
| 核心贡献 | 新技术 | 新评估范式加实证发现 |

Benchmark 论文的核心不在于"我们提出了一个数据集"，而在于定义新的评估维度、提供系统性
测量基础设施、揭示模型能力的深层洞察。评估盲区与动机必须在引言中明确阐述。论文需要
用自己的声音，清晰地说明这个 Benchmark 或这篇评估论文为何需要存在。

### 五大支柱

每篇可发表的 Benchmark 论文都必须覆盖这五个要素。前四个是必须的，第五个可选但强烈推荐。

1. **Research Gap（评估盲区）。** 清晰、可辩护、使用三种已验证盲区模式之一来命名。
   没有真实盲区，论文就没有核心论点。
2. **Construction Pipeline（构建方法）。** 系统性、可扩展、可复现的数据构建流程，
   附带明确的质量门控。
3. **Evaluation Framework（评估框架）。** 多维分类学加细粒度指标，实现诊断而不仅仅是排名。
4. **Empirical Findings（实证发现）。** 标志性的 Finding X 加粗总结模式，赋予论文可复用、
   可引用的输出。
5. **Companion Method（配套方法，可选）。** 一个利用 Benchmark 数据提升模型能力的训练方案
   或模型，将评估贡献转化为"评估加提升"双重贡献。

每个支柱对应一个或多个子技能，编排器按顺序路由。

### 阶段检测与路由

编排器首先询问一个问题：项目目前处于哪个阶段？用户根据下表自行定位，或由编排器从上下文
推断阶段并确认后再路由。

| 阶段 | 条件 | 调用技能 | 核心问题 |
|---|---|---|---|
| 1. 评估盲区分析 | 仍在探索这个 Benchmark 为何需要存在 | `bench-gap-analysis` | 这个 Benchmark 为什么需要存在？ |
| 2. Benchmark 设计 | 盲区已确认，正在设计 Benchmark 体系 | `bench-design` | Benchmark 长什么样？ |
| 3. 数据构建流程 | 设计已锁定，正在规划数据构建流水线 | `bench-construction` | 数据怎么构建出来？ |
| 4. 实验设计 | 数据已就绪或构建中，需要设计实验 | `bench-experiments` | 什么实验能产出最深的洞察？ |
| 5. 论文结构 | 实验已完成，正在写论文 | `bench-paper-structure` | 怎么组织和撰写这篇论文？ |
| 6. 提交前检查 | 初稿已完成，进行提交前审核 | `bench-checklist` | 论文准备好提交了吗？ |

### 流程 DAG

子技能构成有向无环图。每个子技能都有明确的终止态，指向链路中的下一个技能，
以及阻止缺少前置交付物就继续前进的强制门禁。

```
START
 |
 v
bench-gap-analysis
 |  （Gap Statement 加研究问题）
 v
bench-design
 |  （设计文档）
 v
bench-construction
 |  （流程规格加质量控制）
 v
bench-experiments
 |  （RQ 驱动实验计划）
 v
bench-paper-structure
 |  （引言、各章节、图表规划）
 v
bench-checklist
 （终点门禁；发现严重问题时路由回相应子技能）
```

### 参考案例论文

三篇已发表的 Benchmark 论文贯穿所有子技能，作为循环出现的案例，每篇对应一种盲区模式：

| 论文 | 会议 | 领域 | 盲区模式 | 构建范式 |
|---|---|---|---|---|
| StatQA | NeurIPS 2024 | 数学与统计 | 维度缺失 | 逆向合成 |
| nvBench 2.0 | NeurIPS 2025 | Text-to-Visualisation | 假设违背 | 可控注入 |
| VisJudge-Bench | ICLR 2026 | 可视化评估 | 粒度不足 | 自适应生成加专家标注 |

每个子技能将指导建立在对应案例上，使建议从抽象模板落地到具体论文。

## 核心原则

- **五大支柱**：Research Gap、Construction Pipeline、Evaluation Framework、Empirical Findings、
  Companion Method（可选）。每篇可发表的 Benchmark 论文都必须覆盖这五项。
- **叙事主轴纪律**：Benchmark 论文推销的是评估维度，而非方法。用技术论文的叙事主轴写
  Benchmark 论文，会造成审稿人系统性的困惑。
- **阶段门控**：每个子技能顶部都有强制门禁，阻止在没有前一阶段交付物的情况下继续前进。
  门禁的存在是为了在跳跃式前进导致浪费数月之前提前截住失败。
- **单入口编排**：不熟悉 Benchmark 写作的用户应从此编排器进入；有经验的用户在确知自己
  处于哪个阶段时，可以直接调用对应子技能。

## 示例

假设一个用户向编排器发出消息："我想构建一个用于评估 LLM 在高中数学奥林匹克题目上
表现的 Benchmark，能帮我吗？"

编排器不会立即开始起草设计目标。第一步是阶段检测。用户有一个话题方向和一个模糊目标，
但没有明确的 Gap Statement（现有数学 Benchmark 具体缺失什么），没有分类学，没有流程草图。
编排器确认："在设计 Benchmark 架构之前，我们需要准确阐明它填补了哪个评估盲区。
让我们从评估盲区分析阶段开始。"然后路由至
[bench-gap-analysis](../bench-gap-analysis/overview.md)。

在 bench-gap-analysis 阶段，用户调研现有数学 Benchmark（GSM8K、MATH、AIME、
OlympiadBench、MATH-L5 等），识别它们共享的隐含假设（例如，正确性是二元的：最终
数值答案匹配则正确，否则错误），并提出一个盲区：现有 Benchmark 不评估证明的优雅性，
也不评估区分多种有效解题策略的能力。该盲区符合维度缺失模式。盲区通过四重验证
（对竞赛评分有实际影响、可通过评分标准量化、无法轻易添加到现有 Benchmark 中、
可为训练反馈提供可操作方向）。用户起草了 Gap Statement 和两个研究问题。

只有在盲区锁定之后，编排器才会向前路由至
[bench-design](../bench-design/overview.md)，将盲区转化为设计目标（G1-G4）、
任务范围、分类学和评估框架。如果用户试图跳过评估盲区分析直接进入设计，
bench-design 顶部的强制门禁会截住并路由回去。门禁不是官僚障碍，
而是防止最常见的 Benchmark 论文失败模式的保护机制：构建一个找不到可辩护存在理由的数据集。

## 用插件实操

按照 [顶层 README](../../../../README.md) 安装插件后，自然语言即可触发。编排器会在
"starting a new benchmark paper"、"resuming work on a benchmark project"、
"how do I write a benchmark paper" 等短语上自动触发。用一两句话描述当前项目状态，
编排器会检测阶段并路由至对应子技能。如果已知自己处于哪个阶段，可以直接用发布名称
（例如 `bench-gap-analysis`）调用对应子技能。

## 出处

改编自
[archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md](/archive/v1-source/1_Guide/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md)
及插件文件
[/plugins/phd-research/skills/bench-writing/SKILL.md](/plugins/phd-research/skills/bench-writing/SKILL.md)。
---

[English](../../../en/skills/bench-writing/overview.md) | [中文]
