<div align="center">

<img src="assets/images/icon-example.png" alt="Supervisor-Skills" height="140" />

<h1>Supervisor-Skills</h1>

<h3>博导科研技能包</h3>

<p>
  <strong>博士生科研方法论：一份完整的中文课程，以及七个可被任意 AI 助手直接调用的科研技能。覆盖从 idea 到投稿的完整论文生命周期。</strong>
</p>

<p>
  <a href="README.en.md">English</a>
  &nbsp;·&nbsp;
  <strong>中文</strong>
  &nbsp;·&nbsp;
  <a href="docs/zh/README.md">中文文档</a>
  &nbsp;·&nbsp;
  <a href="#快速开始">快速开始</a>
  &nbsp;·&nbsp;
  <a href="CONTRIBUTING.md">参与贡献</a>
</p>

<p>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg" alt="License: CC BY 4.0" /></a>
</p>

</div>

---

## 项目缘起

科研新手最痛苦的"Last Mile"，往往卡在隐性知识（Tacit Knowledge）上：什么样的 Idea 值得做、一张 Motivated Example Figure 如何在 30 秒内打动审稿人、Introduction 的六段式逻辑链为什么缺一不可、Benchmark 论文的核心为什么是"发现评估盲区"而不是"又造一个数据集"。

这些判断，过去只能在课题组里手把手传授。本项目将十年顶会论文写作与审稿的系统方法论整理为一个同时服务人类读者和 AI 助手的技能包：既是一份可独立阅读的完整中文课程，也是七个可直接接入 AI 助手的结构化技能。

## 快速开始

### AI 助手：一句话安装

把下方这段 Prompt 发给你的 AI 助手（Cursor、Codex，或任意支持 MCP 的客户端），它会自动 clone 仓库、将技能注册到你 Agent 的 skill 目录、并完成安装校验。

```
Help me install Supervisor-Skills from https://github.com/HKUSTDial/Supervisor-Skills with MCP and Skills.
```

安装后，七个技能会根据自然语言请求（例如"帮我评估这个 idea"、"起草 Introduction"、"投稿前审核这篇论文"）自动匹配触发。

### 人类读者：直接阅读课程

从 [`docs/zh/README.md`](docs/zh/README.md) 起步，按顺序阅读论文质量基础、七个技能的长篇详解，以及三篇顶会论文的写作剖析（ICML 2025 Alpha-SQL、ICLR 2025 AFlow、VLDB 2026 LEAD）。英文镜像位于 [`docs/en/`](docs/en/README.md)，与中文逐文件对齐。

## 适用人群

- 正在写第一篇论文、希望有结构化路线图从 idea 走到投稿的博士生。
- 以 NeurIPS、ICML、ICLR、VLDB、SIGMOD、KDD、ACL、EMNLP、CVPR 等顶会为目标的早期科研工作者。
- 草稿已完成、希望在投稿前获得审稿人视角自查的首次投稿作者。
- 博导、实验室组长，希望将课题组内"口传心授"的指导系统化、可复用。

## 技能目录

七个锚点技能共处同一插件，覆盖论文的完整生命周期。

| 技能 | 使用时机 | 功能简述 | 文件 |
|---|---|---|---|
| `idea-evaluator` | idea 初期 | 五维潜力分析（更高 / 更快 / 更强 / 更省 / 更广）、生命周期与能力匹配、致命缺陷审计、颠覆式创新探测 | [SKILL.md](plugins/phd-research/skills/idea-evaluator/SKILL.md) |
| `vibe-research-workflow` | 贯穿全过程 | Vibe Coding / Vibe Figure / Vibe Writing 的工具选择与六条行为准则 | [SKILL.md](plugins/phd-research/skills/vibe-research-workflow/SKILL.md) |
| `intro-drafter` | 搭骨架 | 六段式 Introduction 大纲：背景 → 现有局限 → 问题与目标 → 关键挑战 → 方法概览 → 贡献 | [SKILL.md](plugins/phd-research/skills/intro-drafter/SKILL.md) |
| `tech-paper-template` | 搭骨架 | 技术类论文思考表 + 自洽性四项检查 + Technique vs New Problem 定位 | [SKILL.md](plugins/phd-research/skills/tech-paper-template/SKILL.md) |
| `benchmark-paper-template` | 搭骨架 | Benchmark 类论文五大要素审计 + 6 段 Introduction 逻辑链 + 章节结构 + 投稿自查清单 | [SKILL.md](plugins/phd-research/skills/benchmark-paper-template/SKILL.md) |
| `figure-designer` | 画图 | Motivated Example / Solution Overview / Experimental Results 三类核心配图的范式选择与质量自查 | [SKILL.md](plugins/phd-research/skills/figure-designer/SKILL.md) |
| `pre-submission-reviewer` | 投稿前 | 宏观逻辑、写作细节、英文语法、LaTeX 格式、图表质量，五维审稿人视角自查 | [SKILL.md](plugins/phd-research/skills/pre-submission-reviewer/SKILL.md) |

一条典型的技术论文工作流：`idea-evaluator` → `tech-paper-template` → `intro-drafter` → `figure-designer` → `pre-submission-reviewer`，全程搭配 `vibe-research-workflow` 提供的工具与行为准则。Benchmark 论文将 `tech-paper-template` 替换为 `benchmark-paper-template`，其余一致。

## 仓库结构

```
Supervisor-Skills/
├── README.md                           # 中文主 README（本文件）
├── README.en.md                        # English mirror
├── CONTRIBUTING.md                     # 贡献指南
├── CHANGELOG.md                        # 版本记录
├── LICENSE                             # CC BY 4.0
├── llms.txt                            # 面向 LLM 的导航索引
├── plugins/phd-research/skills/
│   ├── idea-evaluator/                 # Idea 多维评估
│   ├── vibe-research-workflow/         # AI 辅助科研工作流
│   ├── intro-drafter/                  # Introduction 章节起草
│   ├── tech-paper-template/            # 技术类论文逻辑骨架
│   ├── benchmark-paper-template/       # Benchmark 类论文逻辑骨架
│   ├── figure-designer/                # 三大核心配图设计
│   └── pre-submission-reviewer/        # 投稿前审稿人视角自查
├── docs/
│   ├── en/                             # English reader index
│   └── zh/                             # 中文读者指南（主）
├── assets/
│   └── images/                         # 项目图标与示意图
├── scripts/
│   └── lint_skills.py                  # 技能结构校验器
└── archive/
    └── v1-source/                      # 原版课程资料，原样保留
```

## 参与贡献

欢迎各种形式的反馈与贡献：提 Issue 汇报使用体验与 Bug、发 PR 改进技能实现，或分享你在真实投稿中的使用案例。提交规范与代码风格详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 联系与致谢

**方法论原作：** 骆昱宇 教授，香港科技大学（广州），<yuyuluo@hkust-gz.edu.cn>。本项目的全部科研方法论来自其十年 Data+AI 方向顶会论文写作与指导经验。

**实现与维护贡献者：**

- Wu Yin（[@JoeyWu-tech](https://github.com/JoeyWu-tech)），Agent Skills 打包、lint 校验、仓库结构与迁移。
- Yupeng Xie，Benchmark 类论文相关技能与参考资料。
- Boyan Li，Vibe Research 章节与实战配图经验。

如果本项目帮助过一篇论文顺利落地，右上角 Star 是对维护者最轻便的感谢，也是项目持续更新的最大动力。欢迎提 Issue、开 Discussion、发 PR。

## 许可协议

本项目采用 [CC BY 4.0](LICENSE) 协议发布。使用与再分发请保留署名。
