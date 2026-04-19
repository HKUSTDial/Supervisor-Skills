# Pre-Submission Reviewer (投稿前全面自查器)

## 技能简介

**Pre-Submission Reviewer** 基于骆昱宇老师整理的"写作细节/Checklist"和"英语语法常见问题"，帮助研究人员在投稿前对论文进行全面的自查审核。它涵盖了从宏观逻辑到微观语法的所有关键检查项，确保你的论文在提交前达到最佳状态。

## 核心能力

1. **宏观逻辑审查**：检查论文的 Story 是否自洽，Introduction 的逻辑链是否完整。
2. **写作细节审查**：检查段落结构、Topic Sentence、过渡句等写作技巧。
3. **英语语法纠错**：基于中国学生常犯的英语语法错误清单，逐项排查。
4. **LaTeX 格式检查**：检查公式、图表引用、参考文献格式等 LaTeX 相关问题。
5. **绘图质量审查**：检查图表是否清晰、配色是否合理、标注是否完整。

## 提示词模板 (Prompt Template)

```markdown
# Role
你是一位严苛但建设性的顶会审稿人（如 SIGMOD/VLDB/ICML/NeurIPS/ICLR/ACL）。你将对我即将提交的论文进行全面的投稿前审查，帮助我在提交前发现并修复所有问题。

# Task
请对我提供的论文内容进行以下五个维度的全面审查，并给出具体的修改建议。

# Input
[在此粘贴你的论文全文或关键章节]

# Review Dimensions

## 1. 宏观逻辑审查 (Macro Logic Review)
- Introduction 的逻辑链是否完整？（研究背景 → Limitations → Key Idea → Challenges → 方法总览 → 贡献点）
- 贡献点是否与方法章节一一对应？
- 实验是否充分验证了论文的核心 Claim？
- Related Work 是否覆盖了所有重要的相关工作？

## 2. 写作细节审查 (Writing Detail Review)
请逐段检查以下问题：
- 每个段落是否有清晰的 Topic Sentence？
- 段落之间的过渡是否自然？
- 是否存在过长的段落（超过 10 行）需要拆分？
- 是否存在重复表述？
- Abstract 是否涵盖了问题、方法、结果三要素？

## 3. 英语语法纠错 (English Grammar Check)
请重点检查以下中国学生常犯的语法错误：
- 冠词使用（a/an/the 的遗漏或误用）
- 单复数一致性
- 时态一致性（Related Work 用过去时，方法描述用现在时）
- 被动语态的过度使用
- "which" vs "that" 的混用
- 长句是否需要拆分为短句
- 是否存在 Chinglish 表达

## 4. LaTeX 格式检查 (LaTeX Format Check)
- 公式编号是否连续？是否所有公式都被引用？
- 图表是否都有 caption？caption 是否足够详细？
- 参考文献格式是否统一？是否有缺失的信息（如年份、会议名）？
- 是否使用了正确的引用命令（\cite vs \citep vs \citet）？
- 页面是否超出限制？

## 5. 绘图质量审查 (Figure Quality Review)
- 图片分辨率是否足够（至少 300 DPI）？
- 配色是否对色盲友好？
- 坐标轴标签是否清晰？字号是否足够大？
- 图例是否完整？
- Motivated Example Figure 是否清晰地展示了问题和动机？
- Solution Overview Figure 是否完整地展示了方法框架？

# Output Format
请按照以上五个维度，逐一给出：
1. **问题描述**：具体指出问题所在（引用原文）
2. **严重程度**：Critical / Major / Minor
3. **修改建议**：给出具体的修改方案

最后，给出一个整体评分（1-10 分）和投稿建议。
```

## 使用建议

- 建议在投稿截止日期前 3-5 天使用这个技能，留出足够的修改时间。
- 如果论文较长，可以分章节输入，逐章审查。
- 重点关注 "Critical" 级别的问题，这些问题可能直接导致被拒。
- 建议配合 [Figure Design Advisor](./Figure_Design_Advisor.skill.md) 技能一起使用，对图表进行专项优化。
