<div align="center">

# Draw.io Reconstruction Skill

[English](README.md) | [中文](README.zh-CN.md)

**一个用于将图像中的图示重建为可编辑 Draw.io 文件的 Codex skill。若要较稳定地复现仓库中的示例，建议使用 Codex + GPT-5.5 xhigh。**

[![arXiv](https://img.shields.io/badge/arXiv-2605.15677-b31b1b)](https://arxiv.org/abs/2605.15677)
[![Dataset](https://img.shields.io/badge/HuggingFace-VCG--Bench-yellow)](https://huggingface.co/datasets/sxy1620348809/VCG-Bench)

</div>

这个仓库包含一个 Codex skill，以及一组辅助脚本，用于把参考图中的图示转换成可编辑的 `.drawio` 文件。它对应的是 VCG-Bench 发布示例中的实际重建流程：agent 先检查参考图、建立可见元素清单，再用 Draw.io 原生图元重建文本和结构，在合适的时候使用裁剪图或 SVG，导出 PNG 预览，并对结果进行验证。仓库中自带了示例，便于其他人基于原始 PNG 输入进行复现。若希望尽量接近 README 中展示的重建效果，建议使用 Codex + GPT-5.5 xhigh；更弱的模型或更低的推理模式，视觉保真度通常会明显下降。

配套 benchmark 仓库地址：
https://github.com/sxy1499894281/VCG-Bench

工作流包含两组独立验收的修复循环：Icon Producer 负责准备图标，另一个只读 Icon Reviewer 负责验收；完整重建同样由 Reconstruction Producer 和不同的只读 Reconstruction Reviewer 分工。每个 FIX 都会启动新的修复 Producer，修复后再启动新的 Reviewer，Producer 不能验收自己的工作。

图标准备和最终嵌入验收图必须拆成小型 `icons-review*.png` / `placement-review*.png` 分片，每片最多 8 个图标，并使用真实 1:1、2x 视图及带 bbox 标记的源图/成品外围上下文。Reviewer 必须逐图标返回结论，不能只对一张超长总表笼统 PASS。

## 推荐复现配置

本仓库中的示例重建，推荐使用以下参考配置：

- Runtime：Codex
- Model / mode：GPT-5.5 xhigh
- 输入：`examples/` 目录中的原始图片（PNG/JPG）
- 输出：可编辑的 `.drawio` 文件和导出的 PNG 预览图

这是我们建议用于复现 README 案例图的配置。你也可以用其他运行时、模型或更低的推理设置来做实验，但不应把这些配置视为等价复现条件，因为它们更容易遗漏小元素、在布局上漂移，或者生成保真度更低的 Draw.io 结构。

复现时，建议使用 `examples/` 中对应的原始图片作为源图，并把导出预览图写到单独文件，例如 `examples/<name>_preview.png`，这样不会覆盖原始输入。

## 仓库内容

| 路径 | 用途 |
|---|---|
| `SKILL.md` | Codex skill 的说明文件。安装 skill 后，Codex 实际读取的就是这个文件。 |
| `scripts/batch_manifest.py` | 为一批输入图片生成 manifest。 |
| `scripts/batch_verify.py` | 校验一批 `.drawio` 输出及其导出的预览图。 |
| `scripts/check_drawio.py` | 检查 `.drawio` XML 结构、嵌入图像，以及常见重建问题。 |
| `scripts/export_drawio.py` | 通过 Draw.io Desktop/CLI 将 `.drawio` 导出为 PNG。 |
| `scripts/crop_assist.py` | 辅助从复杂参考图中裁出局部图像。 |
| `agents/openai.yaml` | 示例 agent 配置元数据。 |
| `examples/` | 原始 PNG/JPG 输入，以及对应的示例 `.drawio` 文件。 |
| `assets/` | README 中展示案例所需的图片资源。 |

## 重建案例

下面的示例展示的是 Codex + GPT-5.5 xhigh + skill 在完成规定的独立修复与审查循环后的重建结果。左侧是原始图，右侧是由重建后的 `.drawio` 导出的 PNG，并作为 README 展示图使用。

<table>
  <tr>
    <th width="50%">原图</th>
    <th width="50%">重建后的 Draw.io 导出图</th>
  </tr>
  <tr>
    <td><img src="assets/cases/data_cn_original.png" alt="Chinese data-analysis workflow original"></td>
    <td><img src="assets/cases/data_cn_drawio.png" alt="Chinese data-analysis workflow reconstructed Draw.io export"></td>
  </tr>
  <tr>
    <td><img src="assets/cases/data_lake_original.png" alt="Data lake original"></td>
    <td><img src="assets/cases/data_lake_drawio.png" alt="Data lake reconstructed Draw.io export"></td>
  </tr>
  <tr>
    <td><img src="assets/cases/data_man_original.png" alt="Data management original"></td>
    <td><img src="assets/cases/data_man_drawio.png" alt="Data management reconstructed Draw.io export"></td>
  </tr>
  <tr>
    <td><img src="assets/cases/data_sci2_original.png" alt="Scientific data original"></td>
    <td><img src="assets/cases/data_sci2_drawio.png" alt="Scientific data reconstructed Draw.io export"></td>
  </tr>
  <tr>
    <td><img src="assets/cases/m1_original.png" alt="Biogeochemical process original"></td>
    <td><img src="assets/cases/m1_drawio.png" alt="Biogeochemical process reconstructed Draw.io export"></td>
  </tr>
  <tr>
    <td><img src="assets/cases/m2_original.png" alt="Treatment selection matrix original"></td>
    <td><img src="assets/cases/m2_drawio.png" alt="Treatment selection matrix reconstructed Draw.io export"></td>
  </tr>
  <tr>
    <td><img src="assets/cases/m3_original.png" alt="Low-temperature nitrogen removal original"></td>
    <td><img src="assets/cases/m3_drawio.png" alt="Low-temperature nitrogen removal reconstructed Draw.io export"></td>
  </tr>
</table>

示例输入图和可编辑输出位于：

```text
examples/data_cn.jpg
examples/data_cn.drawio
examples/data_lake.png
examples/data_lake.drawio
examples/data_man.png
examples/data_man.drawio
examples/data_sci2.png
examples/data_sci2.drawio
examples/m1.png
examples/m1.drawio
examples/m2.png
examples/m2.drawio
examples/m3.png
examples/m3.drawio
```

## 作为 Codex Skill 安装

把这个仓库复制或软链接到你的 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
ln -s /path/to/drawio-reconstruction-skill ~/.codex/skills/drawio-reconstruction
```

之后让 Codex 对某张图，或某个图片文件夹，使用 `drawio-reconstruction` 即可。

## 依赖要求

- Codex，或其他能遵循 `SKILL.md` 的 agent。
- Python 3.10+，用于运行辅助脚本。
- Draw.io Desktop/CLI，用于把 `.drawio` 导出为 PNG。

macOS：

```bash
brew install --cask drawio
```

Ubuntu / Debian：

```bash
sudo apt update
sudo apt install drawio
```

如果脚本没有自动识别到 Draw.io，可为支持该参数的脚本显式传入可执行文件路径，或设置 `DRAWIO_PATH` 环境变量。

## 批处理工作流

为一个图片目录创建 manifest：

```bash
python scripts/batch_manifest.py path/to/images --output-dir path/to/output --write
```

对于 manifest 中的每个条目，agent 应产出：

```text
<stem>.drawio
<stem>_preview.png
<stem>.audit.md
```

验证批处理结果：

```bash
python scripts/batch_verify.py path/to/output/drawio_batch_manifest.json
```

导出单个 `.drawio` 文件：

```bash
python scripts/export_drawio.py examples/data_lake.drawio examples/data_lake_preview.png
```

检查单个 `.drawio` 文件：

```bash
python scripts/check_drawio.py examples/data_lake.drawio
```

## 重建原则

这个 skill 的首要目标是尽可能贴近参考图的视觉效果。对于文本和结构，它优先使用 Draw.io 原生元素；对于简单图标，可使用 SVG 或原生形状；对于复杂、风格强或带场景感的视觉元素，则优先使用图像裁剪。是否“完成”，不应只看 XML 能否导出成功，还必须和参考图做视觉对比。

核心质量门槛：

- 在最终交付前，应盘点每一个可见元素。
- 文本和结构几何在可行时应保持可编辑。
- 复杂视觉元素应裁剪或谨慎修补，而不是直接替换成泛化图标。
- 导出的 PNG 预览图必须检查缺失元素、裁剪接缝、模糊和布局漂移。
- audit 文件应记录尚未解决的缺陷，而不是宣称“完美重建”。

## 与 VCG-Bench 的关系

VCG-Bench 关注的是围绕 `mxGraph` XML 的视觉中心化结构生成与编辑问题。这个 skill 是其中一类实际工作流：从参考图出发，重建高保真、可编辑的 Draw.io 图示。

相关资源：

- Homepage: https://sxy1499894281.github.io/VCG-Bench/
- Paper: https://arxiv.org/abs/2605.15677
- Dataset: https://huggingface.co/datasets/sxy1620348809/VCG-Bench
- Code: https://github.com/sxy1499894281/VCG-Bench

## 许可证

这个 skill 仓库采用 [MIT License](LICENSE) 发布。

## 引用

如果你在研究中使用了这个 skill 或它配套的 benchmark，请引用 VCG-Bench：

```bibtex
@misc{su2026vcgbenchunifiedvisualcentricbenchmark,
      title={VCG-Bench: Towards A Unified Visual-Centric Benchmark for Structured Generation and Editing}, 
      author={Xiaoyan Su and Peijie Dong and Zhenheng Tang and Song Tang and Yuyao Zhai and Kaitao Lin and Liang Chen and Gai Yuhang and Yuyu Luo and Qiang Wang and Xiaowen Chu},
      year={2026},
      eprint={2605.15677},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.15677}, 
}
```
