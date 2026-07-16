# Skills：面向读者的技能导读

[English](README.en.md) · 中文

你点进这个目录，大概是想搞清楚 Supervisor-Skills 的"可执行核心"到底是什么。这份 README 就是为你准备的：**不装插件也能当做科研思考清单用，装了插件之后也知道怎么用、什么时候用、用哪一个。**

## 这份 README 在项目里的位置

Supervisor-Skills 的内容被分成三层，各有各的读者：

| 入口 | 读者 | 作用 |
|---|---|---|
| 顶层 [`README.md`](../README.md) | 第一次打开项目的人 | 为什么做这个项目、教程结构、怎么装 |
| [`handbook/`](../handbook/) | 想系统学方法论的人 | 六章科研与写作系统指南（理论主轴） |
| **本文件** | 想直接上手技能的人 | 12 个技能**分别是什么、什么时候用、怎么接龙** |
| `SKILL.md`（每个技能目录内） | 插件 / LLM | 可执行规范：完整性核查、输出格式、模式选项（机器可读，人看有点累） |

一句话：**handbook 教"道"，SKILL.md 跑"器"，本 README 是"道器之间的桥"。**

## 两条主线：技术论文 vs Benchmark 论文

12 个技能不是一堆孤立工具，它们对应两条完整的论文生命周期，并补上研究侧的深度调研、证据闭环规划、正文写作与润色，以及 Draw.io 重建这一类执行型作图能力。先定位自己在写哪种论文，再决定从哪个技能入手。

### 主线一：技术类 / 立场类论文（新方法解决已有问题）

按博士生写第一篇顶会论文的自然节奏，推荐顺序：

1. **[idea-evaluator](idea-evaluator/SKILL.md)** — 在把一个 idea 立项前做体检，淘汰弱 idea、打磨有潜力的
2. **[tech-paper-template](tech-paper-template/SKILL.md)** — 动笔写任何段落之前，先锁住完整的论文逻辑骨架
3. **[write-top-tier-ml-paper](write-top-tier-ml-paper/SKILL.md)** — 把观察、原则、组件、贡献、实验和主图组织成可审稿的证据闭环
4. **[intro-drafter](intro-drafter/SKILL.md)** — 把骨架直接写成六段式 Introduction 正文（引用经真实检索核验；也可只要大纲）
5. **[paper-writer](paper-writer/SKILL.md)** — 其余章节的证据门控正文写作，从单段到整篇，绝不编造
6. **[figure-designer](figure-designer/SKILL.md)** — 规划 Motivated Example、Solution Overview、Experiment 三张承重图
7. **[drawio-reconstruction](drawio-reconstruction/SKILL.md)** — 当已有参考图、草图或截图时，重建为可编辑 Draw.io 文件
8. **[paper-polish](paper-polish/SKILL.md)** — 忠于原意的语言润色：去 AI 腔、把握分寸、中译英
9. **[pre-submission-reviewer](pre-submission-reviewer/SKILL.md)** — 投稿截止前 3 到 5 天的最终审核

**两个横向工具**，和上面九步**正交**，不是第 10 步：

- [deep-research](deep-research/SKILL.md) — 选题前或写作中随时可用的综述级文献调研：多视角检索、逐条引用核验、回答明确研究问题的 survey 报告
- [vibe-research-workflow](vibe-research-workflow/SKILL.md) — 无论你正在写代码、画图还是写文字，它都会给你 AI 协作的行为规则与工具选择建议

### 主线二：Benchmark / Evaluation 类论文

Benchmark 管线比技术论文更强调阶段先后，每个环节都要先于下一个完成。**[benchmark-paper-template](benchmark-paper-template/SKILL.md)** 是这条主线上的编排器：一份技能内置了"Gap → Design → Construction → Experiments → Paper Structure → Checklist"六阶段的完整思考支撑，按当前阶段自动定位并输出对应的五大支柱（Research Gap / Construction Pipeline / Evaluation Framework / Empirical Findings / 可选的 Companion Method）。

写 Benchmark 论文，起点与终点都是这一个技能；两张核心图的设计需要额外调用 figure-designer，已有参考图或截图的 Draw.io 执行可以交给 drawio-reconstruction，投稿前的细节审核仍然落在 pre-submission-reviewer。

### 已经卡在某一环？

遇到具体瓶颈的读者，跳过顺序，直接去对应章节：
- 还没有具体想法，想先摸清一个方向的全貌 → **deep-research**
- Idea 立项没底气 → **idea-evaluator**
- Introduction 逻辑链断了、或想直接拿到 Intro 正文 → **intro-drafter**
- 方法章节写不顺 → **tech-paper-template**
- 骨架已经有了，但贡献、实验和主图还没有形成可审稿的证据闭环 → **write-top-tier-ml-paper**
- 想法和结果都有了，想直接写出某个章节的正文 → **paper-writer**
- 文字生硬、AI 味重、中文稿要改成投稿英文 → **paper-polish**
- 图画得别扭，不知道用什么工具 → **figure-designer**
- 已有参考图、论文图、架构图或截图，想生成可编辑 Draw.io → **drawio-reconstruction**
- 投稿前慌，不知道该查什么 → **pre-submission-reviewer**
- Benchmark 的 gap 说不清、评估维度理不顺 → **benchmark-paper-template**
- AI 辅助科研的规则拿不准 → **vibe-research-workflow**

## 12 张技能卡片

每张卡把 SKILL.md 的严谨定义翻译成"人话"，附带配套的 handbook 章节以及与其它技能的接龙关系。

### idea-evaluator — Idea 的"投稿前体检"

- **定位**：把资深导师评估一个 idea 时的隐式流程，显式化成四层可核查的检查单。
- **什么时候触发**：
  - 学生提出一个 idea，想在投入几个月之前知道"值不值得做"
  - 审稿式自查：现有工作是否已经覆盖、能不能落到 Higher/Faster/Stronger/Cheaper/Broader 某个维度上、学生自身能力与时间窗是否匹配
  - 对一份 idea 列表做粗筛，保留前三，砍掉其余
- **四层检查**：致命缺陷审计（Fatal Flaws，早期闸门）→ Idea 生命周期与学生能力匹配 → 五维打分（更高更快更强更省更广）→ 范式跃迁探测与可行性核查。次序不能换——一个七分的"Higher"分数，在一个 CRITICAL 的 Fatal Flaw 面前毫无意义。
- **产出**：每条证据驱动的打分、CRITICAL / MAJOR / MINOR 的缺陷严重性分级、一份 "Reject and Pivot" 或 "Proceed with Guardrails" 的结论。
- **对应 handbook 章节**：[2.1 Idea 生命周期](../handbook/02_Idea_Generation/2.1_Idea的生命周期与能力匹配.md) · [2.2 更高更快更强](../handbook/02_Idea_Generation/2.2_想Idea的思路_更高更快更强.md) · [2.3 颠覆式创新](../handbook/02_Idea_Generation/2.3_进阶_如何做颠覆式创新.md)
- **下游接龙**：体检通过 → **tech-paper-template** 锁骨架；范式探测信号为"颠覆候选"时，先去看 handbook 2.3。

### deep-research — 综述级文献深度调研

- **定位**：像写一篇真正的 survey paper 那样调研一个方向：先冻结 2-3 个具体研究问题，再从主流方 / 批评方 / 相邻领域 / 方法论 / 应用政策 3-5 个视角独立检索，逐条核验引用真伪，按 MECE 分类综合、句内交叉对比，最后逐条回答研究问题。
- **什么时候触发**：
  - 还没有具体想法，想先搞清一个方向的全貌、关键工作、争议和空白
  - idea-evaluator 或写作过程中发现需要先补全文献地图
  - 需要一份引用可靠、有判断力的调研报告，而不是搜索结果罗列
- **关键纪律**：编造引用零容忍（灰区 = 不使用）；矛盾如实呈现、不平均掉；判断强度不超过证据强度；六维内部门禁（角度/覆盖/引用/分类/分寸/交织）不过就回炉。
- **产出**：survey 结构的调研报告（摘要、研究问题、方法、分类框架、分支分析与对比表、综合讨论、开放问题、逐条回答 RQ 的结论、经核验的参考文献）。
- **上下游**：下游接 **idea-evaluator**（方向摸清后评具体想法）或 **paper-writer**（Related Work 的文献池）。

### tech-paper-template — 下笔前的"逻辑骨架"

- **定位**：用思考模板表格，把论文的 Background、Limitations、Key Idea/Goal、Challenges、Methodology Modules、Contributions 强制对齐。
- **什么时候触发**：
  - idea 已通过评估，动笔前想先把故事线理清楚
  - 合作者对"要不要加一个模块 X"意见不一致——让表格仲裁
  - 写到一半发现方法与 Motivation 接不上——回表格重排
- **关键纪律**：技术类论文 vs 新问题/设定类论文的**论文定位**必须先选一次；挑战与模块一一对应，数量不超过三；贡献点必须指向具体章节编号。
- **产出**：一张完整的 thinking-template 表 + 自洽性核查（"挑战—模块—贡献"三路互锁）+ 下游 intro-drafter 直接可用的结构化输入。
- **对应 handbook 章节**：[3.1 完成一篇科研论文你需要做几件事情](../handbook/03_Paper_Writing/3.1_完成一篇科研论文你需要做几件事情.md) · [3.3 技术类 Full Paper 思考模板](../handbook/03_Paper_Writing/3.3_技术类Full_Paper思考模板.md)
- **上下游**：上游 **idea-evaluator**；需要强化贡献与证据闭环时，下游先接 **write-top-tier-ml-paper**，再进入 **intro-drafter** 与 **figure-designer**。

### write-top-tier-ml-paper — 贡献与证据的“论文架构师”

- **定位**：把技术论文骨架或部分实验结果整理成可审稿的完整论证，将诊断观察、设计原则、方法组件、贡献、实验和主图一一对齐。
- **什么时候触发**：
  - 论文读起来像模块清单，而不是一条完整论证
  - Introduction 的主张、Method 的组件与 Experiments 没有对齐
  - 想知道每一节、每一段应该证明什么
  - `lossless`、`general`、`plug-and-play`、`mechanism-grounded` 等主张需要校准证据强度
- **关键纪律**：每项贡献必须进入 claim-evidence 台账；每个组件必须来自一项观察或约束；实验按审稿问题选择，而不是按现成 benchmark 堆叠；证据不足时降低主张强度，不用形容词掩盖。
- **产出**：一句话 research spine、有边界的贡献列表、claim-evidence 矩阵、逐节逐段蓝图、分优先级的实验计划、主图与表格 storyboard，以及最危险的审稿问题。
- **来源说明**：基于 TaylorSeer、ToCa、GlobalCom2、VidCom2 四篇 arXiv 论文论证结构的原创综合，skill 内明确标注来源；它们只作为写作案例，不作为措辞模板或接收状态证据。
- **上下游**：上游是 **tech-paper-template**；证据计划闭环后，下游接 **intro-drafter**、**paper-writer** 和 **figure-designer**。

### intro-drafter — 六段式 Introduction 正文

- **定位**：以 Background、Limitations、Goal、Challenges、Solution Overview、Contributions 六段流程图为**内部脚手架**，直接产出六段流畅的 Introduction 正文；五条跨段逻辑链在动笔前静默核查，交付物里没有任何脚手架痕迹。
- **什么时候触发**：
  - tech-paper-template 的骨架做完，要把 Intro 写出来
  - 手上有一段研究想法，想直接拿到成段的 Intro 文字而不是要点列表
  - 只想要大纲也可以：明确说"只要大纲"，会切回经典大纲输出
- **关键纪律**：引用先检索后写（完整 Intro 通常织入 15-25 条经核验的文献）；Running Example 绝不编造——用户没给真实案例就用抽象描述写背景段，并在尾注里请用户提供；遵守与 paper-writer 共享的证据纪律（零占位标签、用户没给的细节不写）。
- **产出**：六段 Introduction 正文 + References 列表（编号双向对应）+ 至多三行的尾注提醒。
- **对应 handbook 章节**：[3.2 Introduction 写作的思考模型](../handbook/03_Paper_Writing/3.2_Introduction写作的思考模型.md)
- **上下游**：上游 **tech-paper-template**，需要证据对齐时再经过 **write-top-tier-ml-paper**；下游接 **figure-designer** 和 **paper-writer**。

### paper-writer — 证据门控的论文正文写作

- **定位**：把想法和材料直接写成可投稿的论文正文，单段到整篇都行；每写一个字都要能追溯到证据。实质内容（想法、设计、结果、结论）归作者，语言实现归技能。
- **什么时候触发**：
  - "帮我把这个想法写成一段 Discussion / Methods / Related Work"
  - "写一篇完整的论文初稿"（STEM Intro 自动转交 intro-drafter）
  - 非 STEM 学科（人文 / 社科 / 经济 / 法学）的章节写作——按 CER 骨架逐段规划
- **关键纪律**：事实性声明只有三种合法来源（用户材料 / 本次检索核验过的文献 / 不含数字人名比较的领域常识），模型记忆永远不算；输出零占位标签，缺证据的唯一路径是检索、改写或删除；引用密度先检索后写；整篇 / 终稿 / 引用满 3 条时触发**独立引用核查**（全新上下文的子代理逐条核验，环境不支持则诚实降级并披露）。
- **产出**：干净的章节或全文正文 + References（双向对应）+ 至多三行说明；整篇任务附证据台账与章节蓝图两份工作文件（不嵌入正文）。
- **对应 handbook 章节**：[3.1 全流程](../handbook/03_Paper_Writing/3.1_完成一篇科研论文你需要做几件事情.md) · [3.3 技术类模板](../handbook/03_Paper_Writing/3.3_技术类Full_Paper思考模板.md) · [3.5 写作细节](../handbook/03_Paper_Writing/3.5_写作细节与Checklist.md)
- **上下游**：上游 **tech-paper-template**、**write-top-tier-ml-paper**（贡献与证据计划）与 **intro-drafter**；下游 **paper-polish** 与 **pre-submission-reviewer**。

### benchmark-paper-template — Benchmark 论文的一站式编排器

- **定位**：专为 Benchmark / Evaluation 类论文设计，把五大支柱（Research Gap、Construction Pipeline、Evaluation Framework、Empirical Findings、可选的 Companion Method）和六阶段工作流打包为一个技能。
- **什么时候触发**：
  - 开始一个 Benchmark 项目，从"为什么需要这个 Benchmark"开始思考
  - 已经收了数据，但 evaluation 维度定义模糊
  - 实验做完，不确定 Finding-X 是否"够深"
  - 投稿前对照 Benchmark Paper Checklist 走一遍
- **六阶段**：Gap Analysis → Design → Construction Pipeline → Experiments → Paper Structure → Checklist。技能会**先识别当前所处阶段**，再路由到对应的思考支撑。
- **产出**：阶段性交付物 + 六段式 Introduction 逻辑链 + Section 2-7 骨架 + 投稿前检查单。
- **对应 handbook 章节**：[3.4 Benchmark 与 Evaluation 类论文思考模板](../handbook/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md) · [6.3 LEAD 写作剖析](../handbook/06_Case_Studies/6.3_VLDB_2026_LEAD写作剖析.md)
- **横向接龙**：figure-designer（两张核心图）· pre-submission-reviewer（细节审核）。

### figure-designer — 三张承重图的设计顾问

- **定位**：围绕技术论文中三张决定叙事重量的图——Motivated Example（Figure 1）、Solution Overview（方法章节）、Experimental Results——给出设计范式、排版规则、工具选型建议。
- **什么时候触发**：
  - Intro 大纲锁定后，要把第一段的 Running Example 翻成 Motivated Example 图
  - 方法章节写之前，要决定 Solution Overview 图按什么逻辑切分
  - 实验做完，主表太挤、想把主结果用图呈现
  - 纠结"用 PPT 还是 TikZ 还是 Inkscape"
- **关键原则**：一张图只讲一件事；坐标轴、图例、配色的顶会审美；实验图必须直接回应 Introduction 里的 Motivation。
- **产出**：针对每张图的设计要点、常见反例、工具选择、可复用的布局模板。
- **对应 handbook 章节**：[4.1 Motivated Example Figure](../handbook/04_Scientific_Plotting/4.1_Motivated_Example_Figure.md) · [4.2 Solution Overview Figure](../handbook/04_Scientific_Plotting/4.2_Solution_Overview_Figure.md) · [4.3 Experimental Results Figure](../handbook/04_Scientific_Plotting/4.3_Experimental_Results_Figure.md) · [4.4 绘图 Checklist](../handbook/04_Scientific_Plotting/4.4_绘图Checklist与工具速查表.md)
- **上下游**：上游 **intro-drafter**（Running Example 定了图才好画）和 **tech-paper-template**（模块结构定了 Solution Overview 的骨架）；下游 **pre-submission-reviewer**（图的质量进入最终审核）。

### drawio-reconstruction — 把参考图重建成可编辑 Draw.io

- **定位**：执行型作图技能，把参考图、论文图、架构图、幻灯片图、UI 截图或图片文件夹重建为 `.drawio` 文件，并导出 PNG 预览与审计记录。
- **什么时候触发**：
  - 已经有一张目标风格明确的参考图，希望得到可编辑 Draw.io 版本
  - 需要批量把多张图重建为 `.drawio`，并逐张做视觉一致性检查
  - 想保留文字和结构的可编辑性，同时对复杂图标、截图、视觉隐喻使用裁剪或透明 PNG 保真
- **关键纪律**：视觉保真优先于语义近似；脚本检查只能证明 XML 与导出有效，最终质量必须对照参考图做视觉审计。
- **产出**：`.drawio` 源文件、PNG 预览、复杂或批量任务的 audit 文件，以及未解决视觉差异的明确记录。
- **来源与授权**：改编自 [drawio-reconstruction-skill](https://github.com/sxy1499894281/drawio-reconstruction-skill)，保留 MIT License。
- **上下游**：上游可以接 **figure-designer** 的设计方案或用户已有参考图；下游进入 **pre-submission-reviewer** 的图表质量检查。

### paper-polish — 忠于原意的语言润色

- **定位**：帮作者把**他想说的话**说得更好，不是换成润色者想说的话。改语法、调语序、去 AI 腔、把握措辞分寸、中文稿改写成投稿级英文。
- **什么时候触发**：
  - "帮我润色这段 / 改自然一点 / 去掉 AI 味"
  - "我中文写的，帮我翻成能投稿的英文"
  - "这句是不是说得太满了"
- **关键纪律**：任何可能改变科学含义的改动绝不默默做掉——逐条列出原句 / 改句 / 理由请作者确认；绝不补原文没有的数据、公式、引用、机制解释；默认保守（能小改就不大改）；在文件上工作时直接改文件，版本 diff 就是改动清单。
- **产出**：干净的润色正文 + 3-5 条主要改动说明（含含义风险项对照）。
- **对应 handbook 章节**：[3.5 写作细节与 Checklist](../handbook/03_Paper_Writing/3.5_写作细节与Checklist.md)
- **上下游**：上游 **paper-writer** / **intro-drafter**（起草后的打磨）；发现问题超出语言层（逻辑断裂、核心主张存疑）时转 **paper-writer** 重写或 **pre-submission-reviewer** 评审。

### pre-submission-reviewer — 顶会审稿人视角的最终审核

- **定位**：模拟顶会审稿人，从宏观逻辑、写作细节、英语语法、LaTeX 排版、图表质量五个维度批改草稿。
- **什么时候触发**：
  - 投稿截止前 3 到 5 天的 final pass
  - 合作者改不动了，需要一个"冷眼"的完整体检
  - Rebuttal 写完，想对照常见的"审稿人会挑什么毛病"再扫一遍
- **方法论**：严重性分级（CRITICAL / MAJOR / MINOR）+ 审稿人视角写作 checklist + 英语语法高频坑位表 + LaTeX 常见格式问题。
- **产出**：按严重性排序的缺陷清单、每条配可行的修复建议，并明确**能在 72 小时内修完的子集**。
- **对应 handbook 章节**：[3.5 写作细节与 Checklist](../handbook/03_Paper_Writing/3.5_写作细节与Checklist.md) · [1.1 如何评价一篇论文的质量](../handbook/01_Preliminary/1.1_如何评价一篇论文的质量.md)
- **上游**：技术论文主线的终点；Benchmark 论文主线的终点。

### vibe-research-workflow — 贯穿始终的 AI 协作行为守则

- **定位**：AI 辅助科研的全流程指南，覆盖三条子流水线——Vibe Coding、Vibe Figure、Vibe Writing。
- **什么时候触发**：
  - 第一次用 Claude / Cursor / Codex 辅助写研究代码，不知道分工边界
  - 要画图，纠结"用 AI 生成还是自己画"
  - 写作时担心 LLM 代笔稀释了学术品味
  - 总觉得"AI 在瞎写"——通常是行为守则没对齐
- **核心原则**：**学术判断保留在人手里，把机械劳动交给 AI**；每次 AI 产出都要有明确的可复核证据；工具选型按任务类型落到具体清单。
- **产出**：当前场景的推荐工具链、人机分工示意、常见失败模式对照表。
- **对应 handbook 章节**：[5.1 Vibe Research 与 Vibe Coding 入门](../handbook/05_Vibe_Research/5.1_Vibe_Research与Vibe_Coding入门.md) · [5.2 实战经验分享](../handbook/05_Vibe_Research/5.2_李伯岩实战经验分享与会议纪要.md)
- **用法特点**：与其它十一个技能**正交**。不是第 N 步，而是你走每一步时都可以随时调用的协作规则。写作类请求（起草正文）是合法的：转给 paper-writer / intro-drafter，它们的证据纪律保证不编造实质内容；披露义务与逐段核验义务不变。

## 怎么用这些技能

### 装了 Claude 插件（推荐）

按顶层 README 的[快速开始](../README.md#快速开始-quick-start)装好之后，自然语言即可触发，不需要记任何命令。下面这类短语会自动命中对应技能：

- "帮我调研一下这个方向 / 做个文献综述" → `deep-research`
- "帮我评估一下这个 idea" → `idea-evaluator`
- "先帮我把论文的逻辑骨架搭出来" → `tech-paper-template`
- "把我的贡献和结果整理成可审稿的论文与实验证据计划" → `write-top-tier-ml-paper`
- "起草 Introduction / 我想写一下 Intro" → `intro-drafter`
- "帮我把这个想法写成一段 Discussion / 写篇初稿" → `paper-writer`
- "帮我润色这段 / 去掉 AI 味 / 中文稿翻成投稿英文" → `paper-polish`
- "这张图应该怎么画 / 用什么工具画" → `figure-designer`
- "把这张参考图重建成 draw.io / 生成可编辑 drawio" → `drawio-reconstruction`
- "投稿前帮我审一遍 / 做最后的 final pass" → `pre-submission-reviewer`
- "我想写一个 Benchmark 论文 / 我在做 evaluation" → `benchmark-paper-template`
- "怎么用 AI 辅助我做研究" → `vibe-research-workflow`

### 没装插件也能用

每个技能目录下的 `SKILL.md`，本身就是一份可读的"结构化思考清单"。你可以：
- 直接把 SKILL.md 贴到你用的任何 AI 助手里（Claude、GPT、DeepSeek、Kimi 等），当 system prompt 使用
- 或者把它当成**一份静态 checklist**——不必借助任何 AI，拿笔和纸也能照着每一节逐项自查

`references/` 目录里还有更细的按需加载参考资料（比如 `idea-evaluator/references/five-dimensions.md` 是"更高更快更强"五维度的深度展开）。

## 与 handbook 的对应关系总表

| Skill | 主要对应 handbook 章节 |
|---|---|
| deep-research | 2.1（选题前的方向侦察，主体为新增研究侧能力） |
| idea-evaluator | 2.1 / 2.2 / 2.3 |
| tech-paper-template | 3.1 / 3.3 |
| write-top-tier-ml-paper | 3.1 / 3.3 / 3.5，并补充四篇已标注来源的 arXiv 案例 |
| intro-drafter | 3.2 |
| paper-writer | 3.1 / 3.3 / 3.5 |
| paper-polish | 3.5 |
| benchmark-paper-template | 3.4 / 6.3 |
| figure-designer | 4.1 / 4.2 / 4.3 / 4.4 |
| drawio-reconstruction | 4.4 / VCG-Bench |
| pre-submission-reviewer | 3.5 / 1.1 |
| vibe-research-workflow | 5.1 / 5.2 |

**阅读顺序建议：handbook 先读一遍建立"道"的直觉，再回到本 README 按技能挑场景使用；具体执行交给 SKILL.md。**

## 贡献与反馈

新增技能、修订 SKILL.md、补 references，或者想把你用这些技能写出的顶会论文分享回来——都欢迎。请先阅读顶层 [CONTRIBUTING.md](../CONTRIBUTING.md)；新技能的硬性约定写在那里。

有问题、建议、或想在自己的实验室推广 Supervisor-Skills，请发邮件给 Yuyu Luo (yuyuluo [AT] hkust-gz.edu.cn)。

---

[English](README.en.md) | [中文]
