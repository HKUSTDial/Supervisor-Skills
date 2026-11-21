# Concern 分类

在选择回应策略前，先将每条 Weakness / Question 归类。

## 分类表

| 类型 | 识别信号（审稿人原话） | 优先策略维度 | 推荐模板 |
|------|----------------------|-------------|---------|
| **misunderstanding** | "seems", "unclear whether", 与正文明显矛盾 | clarification_quality + paper_grounding | 模板 A |
| **evidence_gap** | "more experiments", "ablation", "only one dataset" | new_experiment_strength + specific_evidence | 模板 B |
| **novelty** | "incremental", "similar to X", "limited contribution" | specific_evidence + 差异化表述；必要时 controlled_concession | A 或 C |
| **baseline_fairness** | "unfair comparison", "weak baseline", "missing SOTA" | 补对比实验 + 实验协议说明 | 模板 B |
| **scope_claim** | "overclaim", "overstated", "not supported by evidence" | controlled_concession 收窄 claim | 模板 C |
| **writing_clarity** | "hard to follow", "notation", "organization" | 改表述 + 例子 + 正文指针 | 模板 A |
| **theory** | "proof", "assumption", "bound", "convergence" | 公式/证明指针 或 承认局限 | A 或 C |
| **efficiency** | "complexity", "scalability", "overhead" | 复杂度分析 + 实测延迟 | 模板 B |
| **other** | 不明显匹配以上 | 先复述再重新归类 | 视内容 |

## Weakness vs. Question 的处理差异

| | Weakness | Question |
|--|----------|----------|
| 审稿人心态 | "这里有缺陷" | "我没看懂 / 请确认" |
| 回应重点 | 证据 + 必要时修改 | 简短回答 + Section/Table 指针 |
| 常见错误 | 只解释不行动 | 过度道歉 |

## 快速关键词分类

```
novelty:     novel, contribution, incremental, original, marginal
experiments: experiment, baseline, ablation, dataset, evaluation
writing:     clarity, unclear, confusing, notation, presentation
theory:      proof, theorem, assumption, bound, convergence
efficiency:  scalable, complexity, computation, overhead, efficient
scope:       limitation, generalize, broader, overclaim, overstated
```

## 复合 concern 的处理

若一条 W 同时包含 novelty + evidence_gap，分拆为两个子关注点，分别给策略。
优先解决 **审稿人最在意** 的那个（通常出现在第一段）。
