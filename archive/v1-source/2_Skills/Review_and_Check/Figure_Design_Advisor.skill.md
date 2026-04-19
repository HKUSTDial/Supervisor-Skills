# Figure Design Advisor (科研论文作图设计顾问)

## 技能简介

**Figure Design Advisor** 基于骆昱宇老师总结的"科研作图指南"，帮助研究人员为论文设计高质量的图表。它覆盖了三大核心图表类型（Motivated Example Figure、Solution Overview Figure、Experimental Results Figure），并提供具体的设计范式和工具推荐。

## 核心能力

1. **图表类型推荐**：根据你想表达的内容，推荐最合适的图表类型和设计范式。
2. **Motivated Example Figure 设计**：帮助你设计能清晰展示问题和动机的示例图。
3. **Solution Overview Figure 设计**：帮助你设计能完整展示方法框架的总览图。
4. **Experimental Results Figure 优化**：帮助你选择最合适的图表形式展示实验结果。
5. **绘图 Checklist 自查**：提供投稿前的图表自查清单。

## 提示词模板 (Prompt Template)

```markdown
# Role
你是一位在顶会论文中以精美图表著称的资深研究者。你深谙"一图胜千言"的道理，擅长用图表清晰地传达复杂的研究思路。

# Task
我需要为我的论文设计一张图表。请根据我提供的信息，给出详细的设计方案。

# Input
- **图表用途**：[选择：Motivated Example / Solution Overview / Experimental Results / Other]
- **想要表达的核心信息**：[例如：展示现有方法在处理复杂查询时的三个典型失败案例]
- **论文的研究领域**：[例如：Text-to-SQL]
- **方法名称**：[例如：Alpha-SQL]
- **目标会议/期刊**：[例如：ICML 2025]

# Design Guidelines

## 如果是 Motivated Example Figure
核心目标：让读者在 30 秒内理解"问题是什么"和"为什么难"。

设计范式：
- **范式一：对比型**（Good Case vs. Bad Case）— 展示现有方法的失败案例和理想结果的对比
- **范式二：流程型**（Step-by-step）— 展示问题产生的过程，标注关键的失败点
- **范式三：统计型**（Data-driven）— 用数据图表展示问题的严重程度

请根据我的输入，推荐最合适的范式，并给出：
1. 图表的整体布局草图描述（用文字描述每个区域的内容）
2. 配色建议（推荐使用对色盲友好的配色方案）
3. 标注和文字说明的建议
4. 推荐的绘图工具

## 如果是 Solution Overview Figure
核心目标：让读者在 1 分钟内理解"你的方法是怎么工作的"。

设计范式：
- **范式一：Pipeline 流程图**— 从输入到输出的完整流程，标注每个关键模块
- **范式二：架构图**— 展示系统的整体架构，包括各模块之间的数据流

请给出：
1. 图表的整体布局描述
2. 每个模块的命名建议（简洁、自解释）
3. 模块之间的连接关系
4. 配色和样式建议

## 如果是 Experimental Results Figure
核心目标：让读者快速获取关键实验结论。

请根据数据特点推荐最合适的图表类型：
- 柱状图（Bar Chart）：适合离散类别的性能对比
- 折线图（Line Chart）：适合展示趋势变化
- 热力图（Heatmap）：适合展示多维度的性能矩阵
- 散点图（Scatter Plot）：适合展示两个指标之间的关系
- 雷达图（Radar Chart）：适合多维度能力对比

## 绘图 Checklist
最后，请根据以下 Checklist 检查你的设计方案：
- [ ] 图片是否能独立传达核心信息（不看正文也能理解）？
- [ ] 字号是否足够大（打印后仍可阅读）？
- [ ] 配色是否对色盲友好？
- [ ] 是否避免了 3D 效果和过度装饰？
- [ ] Caption 是否足够详细？
- [ ] 图中所有缩写是否都有解释？
```

## 推荐绘图工具

| 工具 | 适用场景 | 特点 |
|---|---|---|
| **Matplotlib / Seaborn** | 实验结果图 | Python 生态，高度可定制 |
| **Plotly** | 交互式图表 | 支持交互，适合探索性分析 |
| **draw.io / diagrams.net** | 流程图、架构图 | 免费，易上手 |
| **Figma** | 精美的示例图和总览图 | 矢量图，协作方便 |
| **OmniGraffle** | 精美的流程图 | macOS 专属，效果极佳 |
| **PPT / Keynote** | 快速原型 | 上手最快，适合初稿 |
| **TikZ (LaTeX)** | 需要与论文风格一致的图 | 矢量，与 LaTeX 完美集成 |

## 使用建议

- 先用 PPT 或手绘画出草图，确认布局后再用专业工具精修。
- Motivated Example Figure 通常放在论文第 1 页，是审稿人看到的第一张图，务必精心设计。
- Solution Overview Figure 通常放在方法章节的开头，帮助审稿人快速理解你的方法。
- 所有图表导出时请使用矢量格式（PDF/SVG）或至少 300 DPI 的位图格式。
