# Tool selection for Vibe Research

## Table of contents

1. Selection heuristic
2. Vibe Coding tools
3. Vibe Figure tools
4. Vibe Writing tools
5. Cost considerations
6. Access from mainland China

## 1. Selection heuristic

Pick the tool that matches the phase, not the other way around.

| Phase | Primary tool | Alternative | When |
|---|---|---|---|
| Coding (IDE-native) | Cursor | VS Code + GitHub Copilot | User wants to stay in a VS Code-compatible editor |
| Coding (agentic CLI) | Claude Code | Codex | User prefers CLI, rich Skills ecosystem |
| Coding (cloud-integrated) | Codex | Cursor | User wants GitHub-integrated cloud workflows |
| Figure (conceptual sketch) | Gemini or Nano Banana | Hand-drawn plus photo | Early exploration |
| Figure (final Figure 1) | PowerPoint then Figma | OmniGraffle (macOS) | Paper-ready |
| Figure (experimental charts) | Matplotlib + Seaborn | TikZ + PGFPlots | Reproducible scientific plots |
| Writing (polish) | Claude | ChatGPT, Gemini | Long-form polish with context preservation |
| Writing (grammar) | Grammarly | LanguageTool | Final pass on mechanical grammar |

## 2. Vibe Coding tools

### Cursor

- VS Code-based AI-native editor.
- Low adoption cost for VS Code users.
- Pro plan 20 USD per month.
- Plan Mode plus Agent Mode separation is valuable.
- Recommended HTTP Compatibility Mode setting: HTTP 1.1.

### Claude Code

- CLI and desktop agentic coding tool by Anthropic.
- Steeper entry curve; rewards investment with rich Skills and
  MCP ecosystem.
- Works well for extended autonomous sessions.

### Codex

- OpenAI agentic coding tool with CLI and desktop.
- Strong GitHub integration and cloud environment support.
- 20 USD per month floor.
- No in-editor code surface; works through the CLI or desktop
  app.

### Tool-specific tips

For Cursor: enable Plan Mode for any non-trivial task. Toggle
with Shift+Tab.

For Claude Code: install relevant Skills (from marketplaces or
local) before starting. `ralph-loop`, `writing-skills`, and
`debugging` are frequently useful.

For Codex: use the cloud environment for heavier tasks;
configure repository access via GitHub.

## 3. Vibe Figure tools

### Conceptual sketches

- Gemini can produce rough visual concepts given a description.
- Nano Banana is useful for quick layout exploration.
- Hand-drawing on paper remains the fastest concept tool.

### Layout and polish

- PowerPoint: fastest iteration for Motivated Example; exports
  to PDF as vector.
- Figma: cleanest polish; component reuse; browser-based.
- OmniGraffle: professional diagram quality on macOS; paid.
- draw.io: free, offline, good for pipelines and architectures.

### Experimental charts

- Matplotlib plus Seaborn: reproducible, scriptable, versioned.
- TikZ plus PGFPlots: LaTeX-integrated; steep learning curve;
  best for final camera-ready.
- Plotly: interactive, useful in supplementary materials.

## 4. Vibe Writing tools

### Polish

- Claude: long context, preserves technical detail reliably.
- ChatGPT: strong at style suggestions; be careful of AI-tone
  drift.
- Gemini: free tier is usable for light polish.

### Grammar

- Grammarly: integrates with Overleaf as a browser extension.
- LanguageTool: open-source alternative.
- Overleaf built-in: basic grammar and spell-check.

### LaTeX

- Overleaf: cloud-based LaTeX with collaboration.
- Local LaTeX: preferred when the paper is under heavy
  revision or when internet access is unstable.

## 5. Cost considerations

Minimal monthly cost for a serious Vibe Research setup:

- 20 USD for one coding assistant (Cursor or Codex or Claude
  Code).
- 0 to 20 USD for writing polish (many options at zero).
- 0 to 10 USD for figure tools (most free; Figma Pro optional).

Total: roughly 20 to 50 USD per month. Lab or institutional
subscriptions often cover this.

Watch for:

- Inference-quota limits during high-load weeks (deadline
  crunches often trigger throttling).
- Pay-per-token costs in API-based flows; cap via dashboard
  budgets.

## 6. Access from mainland China

Researchers in mainland China face additional access constraints
for OpenAI and Anthropic endpoints. Options:

- Proxy services (ensure OpenAI and Google requests are
  correctly forwarded; check latency).
- Lab OpenAI-compatible endpoints (the group's
  hk.yi-zhan.top and vip.yi-zhan.top serve this purpose).
- Cursor Pro with proxy setup.
- Local models for offline development when cloud is
  unavailable.

Network stability is itself a tool-selection factor: unstable
network favours tools that degrade gracefully (Cursor's local
model option, local Matplotlib) over tools that require
continuous cloud access (fully agentic CLIs during long
sessions).
