# CLI 参考

Co-op Translator 安装了以下命令行入口点：

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

The `translate`, `evaluate`, `migrate-links`, and `co-op-review` commands dispatch through `co_op_translator.__main__`, which selects the command implementation based on the invoked script name. The MCP server uses `co_op_translator.mcp.server` directly.

If you are deciding between CLI, Python API, and MCP, start with [选择工作流](workflows.md).

## 首次使用 CLI 流程

如果您从终端使用 Co-op Translator，请从这里开始：

1. 按照 [配置](configuration.md) 中的说明配置一个 LLM 提供商。
2. 选择您要翻译的内容类型。
3. 先运行一个专注的命令，例如仅翻译 Markdown。
4. 在对仓库做大规模更改之前使用 `--dry-run`。
5. 翻译后使用 `co-op-review` 检查结构和新鲜度。

| 目标 | 开始命令 |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP 服务器](mcp.md) instead of running CLI commands directly. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### 常见示例

仅翻译 Markdown：

```bash
translate -l "de" -md
```

仅翻译笔记本：

```bash
translate -l "zh-CN" -nb
```

翻译 Markdown 和图像：

```bash
translate -l "pt-BR" -md -img
```

通过删除并重新创建来更新现有翻译：

```bash
translate -l "ko" -u
```

在无交互提示的情况下运行：

```bash
translate -l "ko ja" -md -y
```

保存日志：

```bash
translate -l "ko" -s
```

### 选项

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | 是 | 以空格分隔的语言代码，例如 `"es fr de"`，或 `"all"`。 |
| `-r`, `--root-dir` | 否 | 项目根目录。默认是当前目录。 |
| `-u`, `--update` | 否 | 删除所选语言的现有翻译并重新创建。 |
| `-img`, `--images` | 否 | 仅翻译图像文件。 |
| `-md`, `--markdown` | 否 | 仅翻译 Markdown 文件。 |
| `-nb`, `--notebook` | 否 | 仅翻译 Jupyter 笔记本文件。 |
| `-d`, `--debug` | 否 | 在控制台启用调试日志。 |
| `-s`, `--save-logs` | 否 | 将 DEBUG 级别日志保存到 `<root-dir>/logs/`。 |
| `-x`, `--fix` | 否 | 根据先前的评估结果重新翻译低置信度的 Markdown 文件。 |
| `-c`, `--min-confidence` | 否 | 用于 `--fix` 的置信度阈值。默认值为 `0.7`。 |
| `--add-disclaimer`, `--no-disclaimer` | 否 | 添加或抑制机器翻译免责声明。CLI 中默认启用。 |
| `-f`, `--fast` | 否 | 已弃用的快速图像模式。 |
| `-y`, `--yes` | 否 | 自动确认提示，对 CI 有用。 |
| `--repo-url` | 否 | 仓库 URL，在 README 的语言表稀疏检出建议中使用。 |
| `--migrate-language-folders` | 否 | 将遗留别名文件夹，例如 `cn` 或 `tw`，重命名为规范的 BCP 47 文件夹。 |
| `--dry-run` | 否 | 预览语言文件夹迁移和翻译估算，而不写入文件。 |

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "实验性"
    `evaluate` 是实验性的。它可以使用基于规则和基于 LLM 的质量检查，将评估结果写入翻译元数据，其评分模型和元数据行为可能会发生变化。

```bash
evaluate -l "ko"
```

### 常见示例

使用更严格的低置信度阈值：

```bash
evaluate -l "es" -c 0.8
```

仅运行基于规则的检查：

```bash
evaluate -l "fr" -f
```

仅运行基于 LLM 的检查：

```bash
evaluate -l "ja" -D
```

### 选项

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | 是 | 要评估的单一语言代码。别名代码会被规范化。 |
| `-r`, `--root-dir` | 否 | 项目根目录。默认是当前目录。 |
| `-c`, `--min-confidence` | 否 | 在列出低置信度翻译时使用的阈值。默认值为 `0.7`。 |
| `-d`, `--debug` | 否 | 启用调试日志。 |
| `-s`, `--save-logs` | 否 | 将 DEBUG 级别日志保存到 `<root-dir>/logs/`。 |
| `-f`, `--fast` | 否 | 仅基于规则的评估。 |
| `-D`, `--deep` | 否 | 仅基于 LLM 的评估。 |

默认情况下，`evaluate` 同时使用基于规则和基于 LLM 的评估。结果会写入翻译元数据并在控制台中汇总。

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "测试版"
    `co-op-review` 是一个测试版的确定性审查命令。它不会调用模型提供商或写入文件，但其检查和问题输出模式可能会演进。

```bash
co-op-review -l "ko"
```

### 常见示例

审查当前目录下的韩语和日语翻译：

```bash
co-op-review -l "ko ja"
```

审查特定项目根目录：

```bash
co-op-review -l "fr" -r ./my-course
```

仅审查相对于基准引用更改的源文件：

```bash
co-op-review -l "ko" --changed-from origin/main
```

为 CI 汇总打印 GitHub 风格的 Markdown 输出：

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### 选项

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | 否 | 要审查的语言代码。可以多次传递或作为空格分隔的值。默认是所有检测到的翻译语言。 |
| `-r`, `--root-dir` | 否 | 项目根目录。默认是当前目录。 |
| `--changed-from` | 否 | 用于限制审查到已更改源文件的 Git 引用。 |
| `--format` | 否 | 输出格式：`text` 或 `github`。默认值为 `text`。 |

`co-op-review` 当前检查缺失的已翻译文件、缺失或过时的翻译元数据、Markdown frontmatter 和代码块完整性、无效的已翻译笔记本 JSON，以及缺失的本地 Markdown 或图像链接目标。缺失链接默认作为警告；结构性和新鲜度问题会导致命令失败。

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP 服务器](mcp.md) guide for client configuration, tools, resources, and safety notes.

### 选项

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | 否 | MCP 传输：`stdio`、`streamable-http`，或 `sse`。默认值为 `stdio`。 |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### 常见示例

预览链接更新：

```bash
migrate-links -l "ko" --dry-run
```

在不确认的情况下处理所有受支持的语言：

```bash
migrate-links -l "all" -y
```

仅在存在已翻译的笔记本时重写链接：

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### 选项

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | 是 | 以空格分隔的语言代码，或 `"all"`。 |
| `-r`, `--root-dir` | 否 | 项目根目录。默认是当前目录。 |
| `--image-dir` | 否 | 相对于根目录的已翻译图像目录。默认是 `translated_images`。 |
| `--dry-run` | 否 | 显示将要更改的文件而不写入更新。 |
| `--fallback-to-original`, `--no-fallback-to-original` | 否 | 当缺少已翻译笔记本时使用原始笔记本链接。默认启用。 |
| `-d`, `--debug` | 否 | 启用调试日志。 |
| `-s`, `--save-logs` | 否 | 将 DEBUG 级别日志保存到 `<root-dir>/logs/`。 |
| `-y`, `--yes` | 否 | 在处理所有语言时自动确认提示。 |

## 环境

All commands require one configured LLM provider:

```bash
# Azure OpenAI 服务
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# 或 OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## 输出布局

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

Translated image output is written under:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## 复制粘贴 CLI 示例

将 Markdown 翻译成三种语言：

```bash
translate -l "ko ja fr" -md
```

仅翻译笔记本：

```bash
translate -l "zh-CN" -nb
```

仅翻译图像：

```bash
translate -l "pt-BR" -img
```

预览 Markdown 翻译而不写入文件：

```bash
translate -l "de es" -md --dry-run
```

修复低置信度的 Markdown 翻译：

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

运行适合 CI 的 Markdown 翻译：

```bash
translate -l "ko ja" -md -y -s
```

审查已翻译的输出：

```bash
co-op-review -l "ko ja"
```

预览链接迁移：

```bash
migrate-links -l "ko" --dry-run
```