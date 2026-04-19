# Quick Start: 如何使用 Paper.skill 提升你的科研效率

本指南将带你快速上手，将我们提炼的 **AI Skills** 导入到你日常使用的 AI 工具中（如 Claude, DeepSeek, Kimi 等），让它们变成你的专属科研副导师。

## 什么是 `.skill` 文件？

`.skill` 文件本质上是一段高度结构化的 **Prompt (提示词)**，其中包含了资深导师在数据智能方向多年积累的：
- **思考框架**（如：更高更快更强五维框架）
- **操作流程**（如：Introduction 写作的 Flowchart）
- **评估标准**（如：审稿人视角的 Checklist）
- **约束条件**（如：不要拿着解决方案找问题）

通过将这些 `.skill` 文件输入给 AI，你相当于给 AI 注入了顶会专家的"灵魂"和"工作习惯"。

## 步骤一：选择适合你的 Skill

浏览仓库中的 `2_Skills` 目录，根据你当前所处的科研阶段选择相应的 Skill：

- **阶段一：还在想 Idea，或者刚有一个雏形**
  - 使用 `Idea_Evaluator.skill.md` 评估可行性。
  - 使用 `Paradigm_Shift_Brainstormer.skill.md` 尝试颠覆式创新。

- **阶段二：准备动笔写论文**
  - 使用 `Introduction_Drafter.skill.md` 梳理核心逻辑。
  - 根据论文类型，使用 `Tech_Paper_Template_Filler.skill.md` 或 `Benchmark_Paper_Template_Filler.skill.md`。

- **阶段三：论文定稿与作图**
  - 使用 `Figure_Design_Advisor.skill.md` 优化图表表达。
  - 使用 `Pre_Submission_Reviewer.skill.md` 进行提交前的无情审查。

## 步骤二：如何导入 Skill

你可以通过以下几种方式使用这些 Skill：

### 方法 1：直接对话 (最简单)
这是最基础的用法，适用于所有大语言模型（LLM）。

1. 打开你想使用的 `.skill.md` 文件。
2. 复制文件中的**全部内容**（通常包括 System Prompt, Role, Workflow 等）。
3. 打开 ChatGPT / Claude / DeepSeek 的对话框。
4. 将复制的内容粘贴进去，并加上一句：**"请仔细阅读并理解上述设定，如果理解了请回复'已准备好'，然后我会输入我的内容。"**
5. 收到 AI 的确认后，按照 Skill 中定义的格式，输入你的 Idea、草稿或数据。

### 方法 2：创建自定义 GPTs (推荐 ChatGPT Plus 用户)
如果你是 ChatGPT Plus 用户，强烈建议创建专属的 GPTs，这样你就不需要每次都粘贴大段 Prompt。

1. 在 ChatGPT 左侧边栏点击 **"Explore GPTs"**，然后点击右上角的 **"Create"**。
2. 切换到 **"Configure"** 标签页。
3. **Name**: 给你的助手起个名字（例如：Paper Intro Drafter）。
4. **Description**: 简单描述其功能。
5. **Instructions**: 打开对应的 `.skill.md` 文件，将其中的核心 Prompt 内容**完整复制并粘贴**到这里。
6. **Conversation starters**: 设置几个快捷启动语，例如 "我想评估一个关于 LLM Agent 的 Idea"。
7. 点击右上角的 **"Create"** 或 **"Update"** 保存。
8. 以后需要使用时，直接在侧边栏点击你创建的 GPTs 即可。

### 方法 3：Claude Projects (推荐 Claude Pro 用户)
Claude 的 Projects 功能非常适合管理复杂的科研上下文。

1. 在 Claude 中创建一个新的 **Project**，命名为你的论文题目（例如："Data Agent Research"）。
2. 在 **"Custom Instructions"** 中，粘贴你想使用的核心 Skill 的 Prompt。
3. 更进阶的用法：你可以把整个 `1_Guide` 目录下的相关 Markdown 文件上传到 **Project Knowledge** 中。
4. 这样，Claude 在回答你问题时，不仅具备了 Skill 的能力，还能随时查阅完整的理论指南。

## 步骤三：与 AI 协作的最佳实践

- **迭代而非盲从**：AI 给出的建议或生成的草稿，只是一个起点。你需要根据自己的专业判断进行修改，然后将修改后的内容再次喂给 AI，让它在这个基础上继续优化。
- **提供充足上下文**：在使用 Skill 时，尽量提供详细的背景信息。例如，在使用 `Idea_Evaluator.skill.md` 时，不仅要说"我想用大模型做数据清洗"，还要说明"现有的 Baseline 是什么，遇到了什么痛点，我的具体切入点是哪一维"。
- **灵活组合**：科研是一个复杂的过程，你可以先用 Idea Evaluator 敲定方向，再用 Intro Drafter 梳理逻辑，最后用 Reviewer 进行审查，形成一套完整的工作流。

---

> 💡 **Tip**: 所有的 `.skill` 文件都是开源的。我们鼓励你根据自己实验室的具体情况和导师的偏好，对这些 Prompt 进行微调和优化，打造真正属于你自己的科研数字分身！
