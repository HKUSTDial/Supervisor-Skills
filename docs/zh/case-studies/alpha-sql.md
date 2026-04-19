# ICML 2025：Alpha-SQL 写作剖析

## 论文背景

- **会议**：ICML 2025（[OpenReview 链接](https://openreview.net/pdf?id=kGg1ndttmI)）
- **标题**：Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search
- **解决的问题**：零样本 Text-to-SQL 生成。已有的训练类方法需要昂贵的标注数据，且每次出现新的基础模型都要重复微调；已有的零样本方法则难以在不需要任务特定监督的情况下，将通用 LLM 知识迁移到结构化 SQL 生成任务上。
- **核心贡献**：一个无需微调的即插即用框架，将 Monte Carlo Tree Search（MCTS）与搜索节点内的链式推理结合，并设计了一种基于多样本查询执行自洽性的自监督奖励函数。

Alpha-SQL 是 [tech-paper-template](../skills/tech-paper-template/overview.md) 术语中的技术类论文（Technique Paper）：它用一种新方法（MCTS 引导的零样本生成）解决一个已有问题（Text-to-SQL）。叙事轴是 Key Idea 或机制，Our Goal 只需一句话过渡。

## 写作技艺：哪些地方做得好，为什么

### Introduction 结构

![Alpha-SQL Introduction Flowchart](/assets/images/intro_flowchart_alpha_sql.png)

图：Alpha-SQL 的 Introduction 映射到六段式 Flowchart 上。由于 ICML 的页数预算紧张，论文将挑战段和贡献段折叠进了方案总览段。

Introduction 遵循了 [intro-drafter](../skills/intro-drafter/overview.md) 的六段式 Flowchart，并做了两处刻意的页数预算压缩。

**第一段（研究背景）。** 用一句话定义 Text-to-SQL，并说明其重要性（"simplifying access to relational databases and enabling both lay and expert users to derive insights effectively"）。立刻将读者落地到真实世界的价值，而不是技术本身。

**第二段（局限性）。** Alpha-SQL 用了两条局限性，而不是三条，每条对应一类已有工作：

- *训练类方法。* 在任务特定数据集上预训练或微调是有效的，但需要标注数据和计算成本，且每次出现更强的新基础模型，训练过程就需要重复。
- *零样本方法。* 成本更低，但遇到了一个根本性障碍：在不使用监督的情况下，将 LLM 的通用知识迁移到 SQL 生成这个特定的结构化任务上很难。

分类干净。审稿人能清楚地看到论文的定位（走零样本路线），以及它在回应什么问题（知识迁移的困难）。

**第三段（问题本质）。** 轻量桥接段：零样本 Text-to-SQL 的本质挑战，就是局限性 2 识别出的迁移困难。因为 Alpha-SQL 是技术类论文，这一段只有一句过渡，不是承重的段落。

**第四段（关键挑战）。** 作为单独的段落缺失。在 ICML 的页数预算下，挑战被折叠进了方案总览，通过 justify 每个技术选择来内联说明非平凡性。数据库顶会的投稿通常需要还原这一段。

**第五段（方案总览）和第六段（贡献点）。** 合并。总览介绍 MCTS 作为搜索骨干，然后呈现两个技术点（LLM-as-Action-Model、自监督奖励函数），每个都附有非平凡性的论证。贡献通过语言来传达（"we introduce the following novel techniques"），而不是单独列一个编号清单。

### 方法论的表述框架

Alpha-SQL 的框架选择值得研究。论文没有先把 MCTS 当作通用搜索技术介绍，再特化到 SQL，而是从第一次提到起就将 MCTS 落地在 Text-to-SQL 领域：节点对应部分 SQL 状态，动作对应 SQL 构造步骤，推理对应动作之间的链式推理，奖励对应执行自洽性。审稿人从不需要在心里把"通用 MCTS"翻译成"SQL-specific MCTS"，每个 MCTS 元素都紧挨着它在 SQL 中的含义。

LLM-as-Action-Model 的框架解决了一个真实的表述问题。MCTS 传统上用策略网络来生成动作，用价值函数来评估它们。零样本 Text-to-SQL 两者都训练不起。Alpha-SQL 的洞见是把现成的 LLM 同时当作两者：LLM 提出下一步动作（加上存储在节点的链式推理），一个单独的自洽性检查（多个采样查询，执行结果对比）充当奖励。两者都不需要训练。

### 图表设计

Figure 1 展示了 Alpha-SQL 与 BIRD 基准上零样本基线之间的性能差距。设计遵循了 [figure-designer](../skills/figure-designer/overview.md) 中的性能预告图范式：分组柱状图，Alpha-SQL 用饱和色突出，基线用低饱和灰色或淡色。由于差距很大（约 69.7% 对零样本基线的 50 多），性能预告图是合适的；这张图比"运行示例加失败案例"能做更多叙事工作。

Figure 3（方案概览图）使用了系统架构范式：MCTS 框架作为中心系统，LLM-as-Action-Model 和自监督奖励作为交互组件，箭头展示推理如何在节点之间流动以及奖励反馈如何传播。每个模块名称都与方法章节的标题一致。

### 贡献点的表述

在页数限制的会议上，贡献点折叠进了方法论文字。在通常会出现编号清单的地方，Alpha-SQL 嵌入了"we propose"、"we introduce the following novel techniques"、"this ensures"、"this helps"这样的信号词。扫描贡献的审稿人仍然能提取出四条清晰的贡献：（1）无需微调的即插即用框架，（2）MCTS 中的 LLM-as-Action-Model，（3）基于执行自洽性的自监督奖励函数，（4）用开源 LLM 在 BIRD 执行准确率达到 69.7% 的实验验证。表述具体，每条贡献都指向一个章节，没有凑数的内容。

## 用到的关键技巧

- **两条局限性而非三条**，覆盖两类已有工作（训练类和零样本类）。比强行加第三条更干净。
- **明确的分类定位。** 审稿人立刻看到论文在哪条赛道上竞争。
- **短小的问题本质段落**，因为这是技术类论文。重量留给方案总览。
- **内联挑战 justify**，折叠进方案总览，因为 ICML 的页数预算。
- **从第一次提到起就做领域特化的 MCTS 框架**，而不是先介绍抽象 MCTS 再特化。
- **LLM 重新利用**（同时作为策略和通过自洽性提供隐性价值来源），在保持 MCTS 结构的同时避免了训练。
- **方法论与贡献段合并**，用强信号动词（"we propose"、"we introduce"、"this ensures"、"this helps"）。
- **性能预告图作为 Figure 1**，因为相对于基线的差距足够大，值得以结果开篇。

## 对你的论文的启发

**将 Introduction 的挑战段落与目标会议匹配。** 在 AI 顶会（ICML、NeurIPS、ICLR），挑战可以折叠进方案总览。在数据库顶会（SIGMOD、VLDB、ICDE），挑战通常需要单独的段落。在起草 Introduction 之前就决定好目标会议，并据此安排结构。为 ICML 写的 Text-to-SQL 论文移植到 VLDB 时，通常需要把挑战段落加回来。

**当两个类别能覆盖所有已有工作时，用两条局限性。** 为了满足"三条是标准"的启发式规则而强行加第三条，会削弱论证。如果你的领域确实有两条主线（训练类 vs 零样本类，离线 vs 在线，规则类 vs 神经类），用两条覆盖这两条主线，比三条模糊分类的局限性更清晰。

**从第一次提到起就将抽象技术落地到你的领域。** MCTS 是通用的；SQL 的 MCTS 是具体的。当你的论文借用其他领域的技术时，立刻把这项技术的每个元素翻译成你的领域词汇。审稿人不应该需要在脑子里把通用 MCTS 映射到 SQL-specific MCTS。

**当算力或数据是瓶颈时，寻找重新利用而不是新的训练。** Alpha-SQL 的洞见是，LLM 可以充当动作模型，它的采样输出可以提供奖励，不需要任何微调。当你的论文目标是一个成本受限的场景时，问问自己，哪些现有组件可以承担意想不到的角色。

**当差距确实很大时，性能预告图作为 Figure 1 是可以接受的。** 如果你的方法提升幅度很小，展示具体失败案例的动机示例图更有说服力。如果差距很大，一张干净的柱状图可以率先开篇。

## 出处

[archive/v1-source/1_Guide/06_Case_Studies/6.1_ICML_2025_Alpha-SQL写作剖析.md](/archive/v1-source/1_Guide/06_Case_Studies/6.1_ICML_2025_Alpha-SQL写作剖析.md)

---

[English](../../en/case-studies/alpha-sql.md) | [中文]
