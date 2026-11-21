# Rebuttal 策略维度（Y 向量）

基于历史成功/失败 rebuttal 数据提炼的 10 个策略维度，1–5 分制。
**overpromise_risk** 和 **vague_future_work** 为风险项（分越高越危险）。

## 十个维度一览

| 维度 | 含义 | 写作要点 |
|------|------|---------|
| **direct_address** | 直击该条 concern 核心，不绕弯 | 每条 W/Q 独立标题，不合并处理 |
| **specific_evidence** | 使用数字、图表、对比结果 | 禁止"significantly improve"无数字支撑 |
| **new_experiment_strength** | 新实验精准回应质疑点 | 说明新实验与主结论的关系 |
| **clarification_quality** | 误解澄清清晰，指向论文原文 | 2–4 句 + Section/Table 指针 |
| **controlled_concession** | 承认合理局限，不过度让步 | 承认后立即给出对应改进或缩窄范围 |
| **structure_quality** | W/Q 结构清晰，便于审稿人对应 | 小标题、编号列表 |
| **tone_confidence** | 语气自信、尊重，不防御 | 避免"you misunderstood"等防御表述 |
| **paper_grounding** | claim 锚定正文/附录的具体位置 | 不提出正文未提及的新 claim |
| **overpromise_risk** ↓ | 承诺可交付，不过度许诺 | 避免"fully solve"等不切实际表述 |
| **vague_future_work** ↓ | 能回应就回应，少推给未来工作 | 推给 future work = 回避信号 |

## 心态条件下的维度优先级

匹配到心态后，从 `mindset-library.md` 对应簇读取：

1. **rule_diff Top 3**: 成功组 vs 失败组差异最大的 3 个维度（正值 = 成功更高）。
2. **Cohen's d 效应**: d > 0.8 表示该维度对该心态有显著区分力。
3. **success_patterns / failure_patterns**: LLM 提炼的具体策略描述。

原则：正差异的维度加强，负差异的维度谨慎（失败组反而更高，可能是过度补救信号）。

## 高效策略组合（交互项）

数据分析发现以下维度组合有协同效应，同时高分时成功率更高：

- `direct_address` + `specific_evidence`: 直接回应 + 具体证据，核心组合
- `specific_evidence` + `paper_grounding`: 数据有论文锚点，可信度最高
- `new_experiment_strength` + `specific_evidence`: 新实验要配具体数字
- `tone_confidence` + 低 `overpromise_risk`: 自信但不夸大

## 每条 concern 的策略标注格式

```
R1.W2 → 优先: specific_evidence, paper_grounding, clarification_quality
         规避: high overpromise_risk, vague_future_work
```
