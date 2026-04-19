# Benchmark Paper Template Filler (Benchmark/Evaluation 类论文逻辑链构建器)

## 技能简介

**Benchmark Paper Template Filler** 基于骆昱宇老师提出的"Benchmark/Evaluation 类论文思考模板"，帮助研究人员系统性地梳理 Benchmark 类论文的完整逻辑链。与技术类论文不同，Benchmark 类论文的核心价值在于**数据集/评测体系的设计**，其写作逻辑和审稿标准有显著差异。

## 核心能力

1. **五大核心要素诊断**：检查你的 Benchmark 是否覆盖了"任务定义与动机"、"数据集构建方法论"、"评测指标设计"、"Baseline 实验"、"深度分析与洞见"五大核心要素。
2. **Introduction 逻辑链构建**：按照 Benchmark 类论文特有的 Introduction 写作逻辑，梳理从"为什么需要新 Benchmark"到"我们的 Benchmark 有什么独特价值"的完整论证链。
3. **主干章节结构规划**：帮助你规划 Section 2（Task Definition）、Section 3（Dataset Construction）、Section 4（Experiments）、Section 5（Analysis）等核心章节的内容。
4. **写作 Checklist 自查**：提供 Benchmark 类论文特有的自查清单，确保不遗漏关键内容。

## 提示词模板 (Prompt Template)

```markdown
# Role
你是一位在 SIGMOD/VLDB/NeurIPS Datasets & Benchmarks Track 等顶会上发表过多篇 Benchmark 论文的资深研究者。你深谙 Benchmark 类论文的审稿标准，知道审稿人最关注什么。

# Task
我将向你提供一个 Benchmark/Evaluation 类论文的核心信息，请你帮我按照以下框架，系统性地梳理论文的完整逻辑骨架。

# Benchmark 论文的五大核心要素
1. **任务定义与动机 (Task Definition & Motivation)**：为什么需要这个新的 Benchmark？现有 Benchmark 的不足是什么？
2. **数据集构建方法论 (Dataset Construction Methodology)**：数据从哪里来？如何保证质量？如何标注？
3. **评测指标设计 (Evaluation Metrics)**：为什么选择这些指标？它们能否全面反映模型能力？
4. **Baseline 实验 (Baseline Experiments)**：选择了哪些代表性方法？实验设置是否公平？
5. **深度分析与洞见 (In-depth Analysis & Insights)**：从实验结果中能得出什么有价值的洞见？对未来研究有什么启示？

# Input
- **研究领域**：[例如：Text-to-SQL / 代码生成 / 多模态理解]
- **Benchmark 名称**：[例如：BIRD / HumanEval]
- **核心动机（为什么需要新 Benchmark）**：[例如：现有 Benchmark 的数据库规模太小，无法反映真实场景]
- **数据规模**：[例如：包含 X 个数据库、Y 个问题、Z 种难度级别]
- **主要发现/洞见**：[例如：发现 LLM 在涉及多表 JOIN 的查询上准确率骤降]

# Output Format

## Step 1: 五大核心要素完整性检查

| 核心要素 | 是否覆盖 | 你的论文中对应的内容 | 改进建议 |
|---|---|---|---|
| 任务定义与动机 | 是/否 | [填写] | [填写] |
| 数据集构建方法论 | 是/否 | [填写] | [填写] |
| 评测指标设计 | 是/否 | [填写] | [填写] |
| Baseline 实验 | 是/否 | [填写] | [填写] |
| 深度分析与洞见 | 是/否 | [填写] | [填写] |

## Step 2: Introduction 逻辑链

| 逻辑阶段 | 你的论文内容 |
|---|---|
| **研究背景** | [填写：该任务/领域的重要性和研究现状] |
| **现有 Benchmark 的局限性** | |
| Limitation 1 | [填写] |
| Limitation 2 | [填写] |
| Limitation 3（如有） | [填写] |
| **Our Goal** | [填写：我们的 Benchmark 要解决什么问题？填补什么空白？] |
| **Benchmark 的独特价值** | [填写：与现有 Benchmark 相比，我们的独特贡献是什么？] |
| **贡献点** | [填写：3-4 个贡献点] |

## Step 3: 主干章节结构规划

为以下每个章节提供内容大纲：
- Section 2: Task Definition & Related Benchmarks
- Section 3: Dataset Construction（包括数据来源、清洗、标注、质量控制）
- Section 4: Experiments & Empirical Findings
- Section 5: Analysis & Discussion
- Section 6: Conclusion & Future Directions

## Step 4: Benchmark 论文写作 Checklist

请逐项检查以下关键项：
- [ ] 是否清晰定义了任务和评测目标？
- [ ] 数据集构建过程是否可复现？
- [ ] 是否讨论了数据集的局限性和潜在偏差？
- [ ] 评测指标是否全面且合理？
- [ ] Baseline 选择是否具有代表性？
- [ ] 实验设置是否公平（相同的预处理、超参数搜索范围等）？
- [ ] 是否提供了有价值的 Error Analysis？
- [ ] 是否讨论了数据集的伦理和隐私问题？
- [ ] 数据集和代码是否计划开源？
```

## 使用建议

- Benchmark 类论文的核心价值在于**数据集的设计质量**和**实验分析的深度**，而不是方法的复杂度。
- 审稿人最关注的是：你的 Benchmark 是否真的填补了一个重要的空白？数据质量是否经得起检验？
- 建议在论文写作初期就使用这个技能，确保五大核心要素都有充分的覆盖。
