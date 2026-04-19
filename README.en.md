<div align="center">

<img src="assets/images/icon-example.png" alt="Supervisor-Skills" height="140" />

<h1>Supervisor-Skills</h1>

<h3>PhD supervisor's research skill pack</h3>

<p>
  <strong>A PhD research methodology: a complete Chinese curriculum, and seven structured skills usable with any AI assistant. Covers the full paper lifecycle from idea to submission.</strong>
</p>

<p>
  <strong>English</strong>
  &nbsp;·&nbsp;
  <a href="README.md">中文</a>
  &nbsp;·&nbsp;
  <a href="docs/en/README.md">Docs</a>
  &nbsp;·&nbsp;
  <a href="#quick-start">Quick start</a>
  &nbsp;·&nbsp;
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg" alt="License: CC BY 4.0" /></a>
</p>

</div>

---

## Project origin

Early-career researchers most often stumble on the "last mile": knowing the sections, having read many good papers, yet watching the draft drift. The hardest part is the tacit knowledge that does not fit in a textbook: which ideas are worth pursuing, how a motivated-example figure can win a reviewer in thirty seconds, why an Introduction must follow a six-paragraph logic chain, why a benchmark paper's core is identifying an evaluation blind spot rather than "yet another dataset".

Those judgments have traditionally passed only through lab apprenticeship. This project systematises a decade of top-venue paper writing and reviewing into a package that serves both human readers and AI assistants: a standalone Chinese curriculum and seven structured skills that plug into any AI assistant.

## Quick start

### For AI assistants: one-sentence install

Paste the prompt below into your AI assistant (Cursor, Codex, or any MCP-aware client). It will clone the repository, register the skills into your agent's skill directory, and verify the install.

```
Help me install Supervisor-Skills from https://github.com/HKUSTDial/Supervisor-Skills with MCP and Skills.
```

Once installed, the seven skills auto-trigger on natural-language requests like "evaluate this idea", "draft my Introduction", or "run a pre-submission review on this paper".

### For human readers: read the curriculum

Start at [`docs/en/README.md`](docs/en/README.md). Paper-quality foundations, long-form overviews of each of the seven skills, and case studies of three accepted papers (Alpha-SQL at ICML 2025, AFlow at ICLR 2025, LEAD at VLDB 2026). The Chinese mirror at [`docs/zh/`](docs/zh/README.md) is file-by-file aligned.

## Who this is for

- PhD students writing their first paper who want a structured path from idea to submission.
- Early-career researchers targeting NeurIPS, ICML, ICLR, VLDB, SIGMOD, KDD, ACL, EMNLP, CVPR, and similar top venues.
- First-time submitters whose draft is done and who want a reviewer-style self-check before submission.
- PhD advisors and lab leads who want to systematise their group's tacit guidance into a reusable package.

## Skill catalog

Seven anchor skills in a single plugin cover the full paper lifecycle.

| Skill | When to use | What it does | File |
|---|---|---|---|
| `idea-evaluator` | Early idea | Five-dimensional potential analysis (Higher / Faster / Stronger / Cheaper / Broader), lifecycle-capability matching, fatal-flaws audit, paradigm-shift probe | [SKILL.md](plugins/phd-research/skills/idea-evaluator/SKILL.md) |
| `vibe-research-workflow` | Throughout | Vibe Coding / Vibe Figure / Vibe Writing tool choice and six behavioral rules | [SKILL.md](plugins/phd-research/skills/vibe-research-workflow/SKILL.md) |
| `intro-drafter` | Skeleton | Six-paragraph Introduction outline: background, limitations, problem, challenges, method, contributions | [SKILL.md](plugins/phd-research/skills/intro-drafter/SKILL.md) |
| `tech-paper-template` | Skeleton | Technical-paper thinking table, four consistency checks, Technique vs New Problem positioning | [SKILL.md](plugins/phd-research/skills/tech-paper-template/SKILL.md) |
| `benchmark-paper-template` | Skeleton | Benchmark-paper five-pillar audit, six-part Introduction logic chain, section structure, pre-submission checklist | [SKILL.md](plugins/phd-research/skills/benchmark-paper-template/SKILL.md) |
| `figure-designer` | Figures | Motivated Example / Solution Overview / Experimental Results paradigm choice and quality audit | [SKILL.md](plugins/phd-research/skills/figure-designer/SKILL.md) |
| `pre-submission-reviewer` | Pre-submission | Five-dimension reviewer self-check: macro logic, writing detail, grammar, LaTeX format, figure quality | [SKILL.md](plugins/phd-research/skills/pre-submission-reviewer/SKILL.md) |

A typical technical-paper workflow: `idea-evaluator` → `tech-paper-template` → `intro-drafter` → `figure-designer` → `pre-submission-reviewer`, with `vibe-research-workflow` running in parallel. Benchmark papers swap `tech-paper-template` for `benchmark-paper-template`.

## Repository layout

```
Supervisor-Skills/
├── README.md                           # Chinese primary
├── README.en.md                        # English mirror (this file)
├── CONTRIBUTING.md                     # Contribution guide
├── CHANGELOG.md                        # Version history
├── LICENSE                             # CC BY 4.0
├── llms.txt                            # LLM-facing index
├── plugins/phd-research/skills/
│   ├── idea-evaluator/
│   ├── vibe-research-workflow/
│   ├── intro-drafter/
│   ├── tech-paper-template/
│   ├── benchmark-paper-template/
│   ├── figure-designer/
│   └── pre-submission-reviewer/
├── docs/
│   ├── en/                             # English reader index
│   └── zh/                             # Chinese reader guide (primary)
├── assets/
│   └── images/                         # Project icon and diagrams
├── scripts/
│   └── lint_skills.py                  # SKILL.md structural linter
└── archive/
    └── v1-source/                      # Original curriculum, preserved verbatim
```

## Contributing

Feedback and PRs are welcome. File an issue to report usability or bugs, submit a PR to improve a skill implementation, or share a real-submission case study. See [CONTRIBUTING.md](CONTRIBUTING.md) for commit conventions and style expectations.

## Contact and acknowledgements

**Methodology:** Prof. Yuyu Luo, The Hong Kong University of Science and Technology (Guangzhou), <yuyuluo@hkust-gz.edu.cn>. All research methodology in this project comes from a decade of Data+AI top-venue paper writing and advising.

**Implementation contributors:**

- Wu Yin ([@JoeyWu-tech](https://github.com/JoeyWu-tech)), Agent Skills packaging, lint harness, repository structure and migration.
- Yupeng Xie, benchmark-track skills and reference material.
- Boyan Li, Vibe Research section and practical figure-design experience.

If this project helps ship a paper, a Star is the lightest thanks you can send and the surest signal for continued maintenance.

## License

Released under [CC BY 4.0](LICENSE). Keep attribution on redistribution.
