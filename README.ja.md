<div align="center">

<img src="assets/icon.png" alt="Supervisor-Skills" height="240" />

</div>

# Supervisor-Skills：博士指導教員としての 10 年分の研究経験を、あなたの AI 副指導教員に凝縮しました。

> アイデアの構想から論文の投稿まで、研究のライフサイクル全体をカバーします。

[English](README.en.md) · [中文](README.md) · 日本語

<p align="center">
  <a href="https://github.com/HKUSTDial/Supervisor-Skills/stargazers"><img src="https://img.shields.io/github/stars/HKUSTDial/Supervisor-Skills?style=flat-square&logo=github" alt="GitHub stars"></a>
  <a href="https://github.com/HKUSTDial/Supervisor-Skills/network/members"><img src="https://img.shields.io/github/forks/HKUSTDial/Supervisor-Skills?style=flat-square&logo=github" alt="GitHub forks"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square" alt="License"></a>
</p>

## 📰 ニュース

> - **[2026-11-05]** 🎓 Supervisor シリーズの次章となる **[Ducktor](https://github.com/yinwu01/Ducktor)** と **[DeepSeek-Ducktor](https://github.com/yinwu01/DeepSeek-Ducktor)** を正式にリリースしました！ 🚀 vibe research の波の中で、エージェントがあなたの研究を前に進める一方、Ducktor は各ステップの背後にある研究上の判断を説明し、研究者にとっての知識のループを閉じます 🔁。あなたとエージェントが共に学び、成長できるようにします 🌱。
> - **[2026-09-21]** 🤝 **Baidu** との提携により、Supervisor-Skills はエキスパートとして **Kuku AI（库库AI）** プラットフォームに組み込まれ、「[**Prof. Luo, Computer Science Research Expert**](https://kuku.baidu.com/#/workbench/expert)」として提供されています。
> - **[2026-07-15]** 🤝 **Doubao** との提携により、Supervisor-Skills は **Doubao Office Mode** の中核となる研究スキル群として正式に導入され、その「**Research Evaluation**」と「**Academic Writing**」の機能を支え、本プロジェクトの研究方法論を膨大なユーザーに届けています。
> - **[2026-07-10]** 🚀 **v2.1**：3 つの新しいスキル、`paper-writer`（エビデンスに基づく論文の執筆）、`paper-polish`（意味を保ったまま推敲）、`deep-research`（サーベイ級の文献調査）を追加しました。`intro-drafter` は文章を出力するようになり、評価とレビューのスキルにはパラダイムを考慮したルーティングが加わりました。[CHANGELOG](CHANGELOG.md) をご覧ください。
> - **[2026-07-03]** 🎤 **2026 China Agent Conference** の Skill セッションで招待講演を行いました。
> - **[2026-07-03]** 🧩 新しいスキル `drawio-reconstruction`：参考図を編集可能な Draw.io に再構築します。
> - **[2026-05-21]** ⭐ 公開から 32 日で GitHub のスター数が **1,000** を突破しました。
> - **[2026-04-19]** 🎉 プロジェクトを公開しました：論文のライフサイクルをカバーする 7 つの中核スキルと、体系的なハンドブックのカリキュラム。

---

## なぜこのプロジェクトなのか？

こんにちは、香港科技大学（広州）助理教授の [Yuyu Luo](https://luoyuyu.vip/) です。自分自身の博士課程から学生を指導する立場になるまで、同じ光景を何度も目にしてきました：優秀な大学院生たちが研究の世界に足を踏み入れると、とてもよく似た悩みに陥ってしまうのです：

*   **理論と実践のギャップ**：数えきれないほどの「研究入門」を読んだのに、いざ自分のテーマに取り組もうとすると、やはり何から始めればよいのかわからない。
*   **指導の手が足りない**：指導教員は忙しく、思いついたアイデアの一つひとつに、タイムリーかつ丁寧なフィードバックを返すことができない。
*   **投稿前の霧**：論文の下書きはできたものの、論理が十分に緻密なのか、図がトップ会議の美的基準を満たしているのか、本文に「初心者のミス」が潜んでいないのかがわからない。
*   **AI 時代の「能力のギャップ」**：大規模モデルは強力ですが、判断力と学術的なセンスがなければ、AI はただの「高級なおもちゃ」にすぎません。**「プロンプト」だけに頼っても、優れた研究は生まれません。**

これらの課題が合わさって、研究における **「ラストワンマイル問題」** を形作っています。それは方法論だけの問題ではなく、経験、センス、そして自信の問題でもあります。

だからこそ、私はこのプロジェクトを始めました。データサイエンスと AI のトップ会議（SIGMOD、VLDB、ICML、NeurIPS）で 10 年間積み重ねてきた論文の発表、査読の経験、そして学術的な直感を「蒸留」し、大規模言語モデル（Claude、GPT-4 など）が正確に実行できる、構造化された一連の **AI Skills** へと「鍛え上げ」ました。

このリポジトリは**単なる理論のガイドではありません**。その中核は、トップ研究者の頭の中にあるものの言葉にするのが難しい**暗黙知**を、**直接呼び出せる生産性**へと変える、初めての試みです。

私たちのビジョンはシンプルです：**AI を、あなたの本当の意味での、いつでもそばにいる研究の副指導教員にすること。**

## コミュニティ

**WeChat のディスカッショングループ**

グループのメンバーは 200 人を超えたため、QR コードからは参加できなくなりました。スキャンして管理者の WeChat（`xyp619`）を追加し、**「Supervisor-Skills + お名前」** と書き添えていただければ、招待いたします。

研究のニュース、論文執筆のコツ、AI の最前線の情報、研究ツールの紹介については、**Data Intelligence and Analytics Lab (DIAL)** と **Xie Bro Talks Research** の WeChat 公式アカウントもフォローしてください。

参加すると、次のことができます：
- 🔔 新しいスキルやハンドブックの公開についての最新情報をいち早く入手
- 💬 論文執筆や AI を活用した研究のコツを仲間と交換
- 🎙️ 不定期のオンライン Q&A や経験共有のセッションに参加

<table align="center">
  <tr>
    <td align="center" width="360">
      <strong>ディスカッショングループ</strong>
    </td>
    <td align="center" width="360">
      <strong>公式アカウント</strong>
    </td>
    <td align="center" width="360">
      <strong>研究の最新情報</strong>
    </td>
  </tr>
  <tr>
    <td align="center" valign="middle" height="360">
      <img src="assets/wechat-admin.JPG" height="300" />
    </td>
    <td align="center" valign="middle" height="360">
      <img src="assets/wechat-official-account.jpg" height="280" />
    </td>
    <td align="center" valign="middle" height="360">
      <img src="assets/wechat-xiebro-research.jpg" height="280" />
    </td>
  </tr>
  <tr>
    <td align="center">
      <sub>管理者 xyp619 を追加してグループに参加</sub>
    </td>
    <td align="center">
      <sub>Data Intelligence and Analytics Lab (DIAL)</sub>
    </td>
    <td align="center">
      <sub>Xie Bro Talks Research：AI、論文、研究ツール</sub>
    </td>
  </tr>
</table>

## チュートリアルの構成

このチュートリアルは、**Guide（理論のハンドブック）+ Skills（実行可能な AI スキル）** の 2 本立ての構成になっています：

```
Supervisor-Skills/
├── README.md                          # Chinese root README
├── README.en.md                       # this file
│
├── handbook/                          # 📖 Research and writing handbook (Chinese, canonical)
│   ├── 01_Preliminary/                # Chapter 1: macro perspective
│   │   ├── 1.1_如何评价一篇论文的质量.md
│   │   └── 博士生科研入门辅导.pdf         # 📄 companion slides
│   ├── 02_Idea_Generation/            # Chapter 2: idea generation
│   │   ├── 2.1_Idea的生命周期与能力匹配.md
│   │   ├── 2.2_想Idea的思路_更高更快更强.md
│   │   └── 2.3_进阶_如何做颠覆式创新.md
│   ├── 03_Paper_Writing/              # Chapter 3: paper writing
│   │   ├── 3.1_完成一篇科研论文你需要做几件事情.md
│   │   ├── 3.2_Introduction写作的思考模型.md
│   │   ├── 3.3_技术类Full_Paper思考模板.md
│   │   ├── 3.4_Benchmark与Evaluation类论文思考模板.md
│   │   └── 3.5_写作细节与Checklist.md
│   ├── 04_Scientific_Plotting/        # Chapter 4: scientific plotting
│   │   ├── 4.1_Motivated_Example_Figure.md
│   │   ├── 4.2_Solution_Overview_Figure.md
│   │   ├── 4.3_Experimental_Results_Figure.md
│   │   └── 4.4_绘图Checklist与工具速查表.md
│   ├── 05_Vibe_Research/              # Chapter 5: Vibe Research in practice
│   │   ├── 5.1_Vibe_Research与Vibe_Coding入门.md
│   │   └── 5.2_李伯岩实战经验分享与会议纪要.md
│   └── 06_Case_Studies/               # Chapter 6: top-venue case studies
│       ├── 6.1_ICML_2025_Alpha-SQL写作剖析.md
│       ├── 6.2_ICLR_2025_AFlow写作剖析.md
│       └── 6.3_VLDB_2026_LEAD写作剖析.md
│
├── handbook-en/                       # 📖 English mirror of the handbook
│
├── skills/                            # 🛠️ Executable AI Skills
│   ├── idea-evaluator/
│   ├── deep-research/
│   ├── vibe-research-workflow/
│   ├── tech-paper-template/
│   ├── intro-drafter/
│   ├── paper-writer/
│   ├── benchmark-paper-template/
│   ├── paper-polish/
│   ├── pre-submission-reviewer/
│   ├── figure-designer/
│   └── drawio-reconstruction/
│
└── assets/                            # Image assets
```

### 📖 handbook：研究と執筆の体系的なガイド

> **📄 付属スライド**：[博士生科研入门辅导.pdf](handbook/01_Preliminary/博士生科研入门辅导.pdf) — このガイドに付属する PDF で、印刷や iPad での閲覧に適しています。研究を始めるための完全なフレームワークがまとめられています。

このセクションには、じっくり読んで学ぶための体系的な理論のフレームワークが収められています。*道*を理解してこそ、*道具*をうまく使いこなせます。

| 章 | 内容 | 英語版 |
|---|---|---|
| **第 1 章：マクロな視点** | 査読者の視点から論文の質を評価する（Novel Problem、Novel Method、Nice Story、Nice Presentation） | [1.1 How to evaluate paper quality](handbook-en/01_Preliminary/1.1_how-to-evaluate-paper-quality.md) |
| **第 2 章：アイデアの創出** | アイデアのライフサイクル、5 つの観点の思考フレームワーク（Higher / Faster / Stronger / Cheaper / Broader）、破壊的イノベーション | [2.1 Idea lifecycle](handbook-en/02_Idea_Generation/2.1_idea-lifecycle-and-capability-matching.md) / [2.2 Higher-faster-stronger](handbook-en/02_Idea_Generation/2.2_higher-faster-stronger.md) / [2.3 Disruptive innovation](handbook-en/02_Idea_Generation/2.3_disruptive-innovation.md) |
| **第 3 章：論文の執筆** | 論文のライフサイクル全体、Introduction のフローチャート、技術論文 / ベンチマーク論文のテンプレート、執筆のチェックリスト | [3.1 Essentials](handbook-en/03_Paper_Writing/3.1_the-essentials-of-a-research-paper.md) / [3.2 Intro flowchart](handbook-en/03_Paper_Writing/3.2_introduction-writing-flowchart.md) / [3.3 Technical template](handbook-en/03_Paper_Writing/3.3_technical-paper-template.md) / [3.4 Benchmark template](handbook-en/03_Paper_Writing/3.4_benchmark-paper-template.md) / [3.5 Writing checklist](handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md) |
| **第 4 章：科学的な図の作成** | 動機付けの図 / 概要図 / 結果の図と、作図のチェックリスト | [4.1 Motivated example](handbook-en/04_Scientific_Plotting/4.1_motivated-example-figure.md) / [4.2 Solution overview](handbook-en/04_Scientific_Plotting/4.2_solution-overview-figure.md) / [4.3 Experimental results](handbook-en/04_Scientific_Plotting/4.3_experimental-results-figure.md) / [4.4 Checklist](handbook-en/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md) |
| **第 5 章：Vibe Research** | Vibe Research / Coding / Figure / Writing の実践 | [5.1 Intro](handbook-en/05_Vibe_Research/5.1_vibe-research-and-vibe-coding.md) / [5.2 Practitioner notes](handbook-en/05_Vibe_Research/5.2_liboyan-practical-notes.md) |
| **第 6 章：トップ会議の事例研究** | Alpha-SQL（ICML'25）、AFlow（ICLR'25）、LEAD（VLDB'26）の Introduction の分析 | [6.1 Alpha-SQL](handbook-en/06_Case_Studies/6.1_icml2025-alpha-sql-analysis.md) / [6.2 AFlow](handbook-en/06_Case_Studies/6.2_iclr2025-aflow-analysis.md) / [6.3 LEAD](handbook-en/06_Case_Studies/6.3_vldb2026-lead-analysis.md) |

中国語の原文は、同じ章構成で [`handbook/`](handbook/) にあります。

### 🛠️ Skills：実行可能な AI スキル

ここがこのリポジトリの中核です。上記の理論的な経験を、構造化された Prompt/Skill ファイルに凝縮しています。内容をそのまま任意の AI アシスタント（Claude、DeepSeek、Kimi など）にコピーして使えます。

| スキル | 説明 | リンク |
|---|---|---|
| **Idea Evaluator** | アイデアを入力すると、AI が「Higher / Faster / Stronger」の 5 つの観点のフレームワークと、能力のマッチング表に基づいて採点します。 | [スキルを使う](skills/idea-evaluator/SKILL.md) |
| **Vibe Research Guide** | ライフサイクル全体にわたる AI 支援の研究：Vibe Coding / Vibe Figure / Vibe Writing。 | [スキルを使う](skills/vibe-research-workflow/SKILL.md) |
| **Introduction Drafter** | Introduction Flowchart の思考モデルに基づき、研究の動機を入力すると、検索で検証された引用付きの 6 段落の Introduction の文章を返します（希望すればアウトラインモードも利用できます）。 | [スキルを使う](skills/intro-drafter/SKILL.md) |
| **Paper Writer** | 1 つの段落から論文全体まで、エビデンスに基づいて論文を執筆します：事実に関するすべての主張はあなたの資料か検証済みの文献にたどれ、引用は独立したチェックを通過し、何もでっち上げません。 | [スキルを使う](skills/paper-writer/SKILL.md) |
| **Paper Polish** | 意味を保ったまま言語を推敲します：文法、AI っぽい文体の除去、主張の強さの調整、投稿品質での中国語から英語への書き換え。意味が変わるおそれのある修正は、確認のために明示します。 | [スキルを使う](skills/paper-polish/SKILL.md) |
| **Deep Research** | サーベイ級の文献調査：多角的な検索、引用ごとの検証、相互比較を伴う MECE な統合を行い、明示された研究課題に答えるサーベイレポートとして届けます。 | [スキルを使う](skills/deep-research/SKILL.md) |
| **Tech Paper Template** | 「技術系フルペーパーの思考テンプレート」に基づき、論文の論理の流れ全体を一緒にたどります。 | [スキルを使う](skills/tech-paper-template/SKILL.md) |
| **Benchmark Paper Template** | Benchmark/Evaluation 系の論文向けに設計されており、評価の論理と実験の設計を構造化するのに役立ちます。 | [スキルを使う](skills/benchmark-paper-template/SKILL.md) |
| **Pre-Submission Reviewer** | トップ会議の査読者の視点から、執筆のチェックリストとよくある英文法の落とし穴に基づいて、下書き全体をレビューします。 | [スキルを使う](skills/pre-submission-reviewer/SKILL.md) |
| **Figure Design Advisor** | 表現したいことを AI に伝えると、動機付けの図 / 概要図 / 実験の図のパラダイムに基づいた、専門的な作図のアドバイスを返します。 | [スキルを使う](skills/figure-designer/SKILL.md) |
| **Draw.io Reconstruction** | 参考画像、論文の図、アーキテクチャ図、スライドの図、UI のスクリーンショットを、PNG のプレビューと視覚的な監査付きで、編集可能な `.drawio` ファイルに再構築します。 | [スキルを使う](skills/drawio-reconstruction/SKILL.md) |

## クイックスタート

次のプロンプトを AI アシスタント（Claude Code、Cursor、Codex など）に貼り付けると、インストールが完了します：

```
Help me install Supervisor-Skills from https://github.com/HKUSTDial/Supervisor-Skills with Skills.
```

## コントリビューションとフィードバック

これは、エージェントによる研究支援における「使いやすさ + 規範への準拠」の問題を解決しようとする、オープンソースの AI スキルプロジェクトです。

Issue、プルリクエスト、そしてこれらのスキルを使ってトップ会議に採択された論文のエピソードも、すべて歓迎します。

このプロジェクトが役に立ったなら、右上のスターを押すのが一番簡単な感謝の伝え方であり、私たちが更新を続ける最大の理由になります。

連絡先：Yuyu Luo（yuyuluo [AT] hkust-gz.edu.cn）。

##

このリポジトリの作成に協力し、貴重な提案をくださった [Yin Wu](https://openreview.net/profile?id=%7EYin_WU2)、[Boyan Li](https://liboyan.vip/)、[Yupeng Xie](https://xypkent.github.io/) に感謝します。

## TODO
**Guide**
- 説得力のあるリバッタルの書き方と、査読者が回答を無視したときの対処法。
- 学術的な共同作業を効果的に進める方法。

## ライセンス

本プロジェクトは [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) のもとで公開されています。非商用での共有と改変を歓迎します。帰属表示は保持してください。
