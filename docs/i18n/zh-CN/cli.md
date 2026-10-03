# CLI 参考

Co-op Translator 安装以下命令行入口点：

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

这些 `translate`、`evaluate`、`migrate-links` 和 `co-op-review` 命令通过 `co_op_translator.__main__` 派发，后者根据被调用的脚本名称选择命令实现。MCP 服务器直接使用 `co_op_translator.mcp.server`。

如果你在 CLI、Python API 与 MCP 之间做选择，请从 [Choose Your Workflow](workflows.md) 开始。

## 控制台输出

交互式终端使用 Rich 进行命令头、进度和摘要的格式化。CI 和非交互式输出会自动回退到纯文本。

将 `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` 设置为强制纯文本输出，或将 `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` 设置为强制使用 Rich 输出。设置 `CO_OP_TRANSLATOR_NO_PROGRESS=1` 可以在抑制实时进度条的同时保留摘要。

使用 `translate --json-events progress.ndjson` 当另一个系统需要
机器可读的进度时。CLI 会继续渲染面向人的输出，同时
NDJSON 文件会接收版本化的 `co-op.translation.event.v1` 事件，包含
稳定字段，例如 `type`, `stage_key`, `completed`, `total`, 和
`current_path`。

## 首次使用 CLI 的流程

如果你从终端使用 Co-op Translator，请从这里开始：

1. 按照 [Configuration](configuration.md) 中的说明配置一个 LLM 提供者。
2. 选择你要翻译的内容类型。
3. 首先运行一个有针对性的命令，例如仅 Markdown 翻译。
4. 在对大型仓库进行更改前使用 `--dry-run`。
5. 翻译后使用 `co-op-review` 检查结构和新鲜度。

| 目标 | 开始使用的命令 |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | 配置 [MCP Server](mcp.md)，而不是直接运行 CLI 命令，以向 MCP 客户端公开工具。 |

## translate

将 Markdown 文件、笔记本和图像文本翻译为一个或多个目标语言。

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

通过删除并重建来更新现有翻译：

```bash
translate -l "ko" -u
```

在无交互提示下运行：

```bash
translate -l "ko ja" -md -y
```

保存日志：

```bash
translate -l "ko" -s
```

写入结构化进度事件：

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### 选项

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | 是 | 以空格分隔的语言代码，例如 `"es fr de"` 或 `"all"`。 |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-u`, `--update` | 否 | 删除所选语言的现有翻译并重新创建。 |
| `-img`, `--images` | No | Translate only image files. |
| `-md`, `--markdown` | No | Translate only Markdown files. |
| `-nb`, `--notebook` | No | Translate only Jupyter notebook files. |
| `-d`, `--debug` | 否 | 在控制台中启用调试日志。 |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `--json-events` | 否 | 以 NDJSON 格式写入机器可读的翻译进度事件。 |
| `-x`, `--fix` | 否 | 根据先前的评估结果，重新翻译低置信度的 Markdown 文件。 |
| `-c`, `--min-confidence` | No | Confidence threshold for `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | 否 | 添加或抑制机器翻译免责声明。CLI 中默认启用。 |
| `-f`, `--fast` | No | Deprecated fast image mode. |
| `-y`, `--yes` | 否 | 自动确认提示，在 CI 中很有用。 |
| `--repo-url` | 否 | README 的语言表中 sparse-checkout 建议所使用的仓库 URL。 |
| `--migrate-language-folders` | 否 | 将旧的别名文件夹（例如 `cn` 或 `tw`）重命名为规范的 BCP 47 文件夹。 |
| `--dry-run` | 否 | 预览语言文件夹迁移和翻译估算，而不写入文件。 |

如果未提供类型标志，`translate` 将处理 Markdown、笔记本和图像。图像翻译需要配置 Azure AI Vision。

## evaluate

评估单一语言的已翻译 Markdown 的质量。

!!! warning "实验性"
    `evaluate` 处于实验阶段。它可以使用基于规则和基于 LLM 的质量检查，将评估结果写入翻译元数据，其评分模型和元数据行为可能会发生变化。

```bash
evaluate -l "ko"
```

### 常见示例

使用更严格的低置信度阈值：

```bash
evaluate -l "es" -c 0.8
```

Run rule-based checks only:

```bash
evaluate -l "fr" -f
```

Run LLM-based checks only:

```bash
evaluate -l "ja" -D
```

### 选项

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Single language code to evaluate. Alias codes are normalized. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-c`, `--min-confidence` | 否 | 在列出低置信度翻译时使用的阈值。默认为 `0.7`。 |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Rule-based evaluation only. |
| `-D`, `--deep` | No | LLM-based evaluation only. |

默认情况下，`evaluate` 同时使用基于规则和基于 LLM 的评估。结果会写入翻译元数据并在控制台中汇总。

## co-op-review

在没有 API 凭据的情况下运行确定性的翻译维护检查。

!!! note "测试版"
    `co-op-review` 是一个测试版的确定性审查命令。它不会调用模型提供者或写入文件，但其检查和问题输出模式可能会演变。

```bash
co-op-review -l "ko"
```

### 常见示例

从当前目录审查韩文和日文翻译：

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

在仅翻译 README 后，仅审查 README：

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` 忽略其他文档和嵌套的 README。如果根目录
`README.md` 缺失，则命令会失败。与 `--changed-from` 结合使用时，它仅在
该源文件更改时审查 README。仅限 README 的翻译会将源 README
保持不变，包括任何共享节标记。

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
| `-l`, `--language-code` | 否 | 要审查的语言代码。可以多次传递或作为以空格分隔的值传递。默认为所有已发现的翻译语言。 |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--changed-from` | 否 | 用于将审查限制为已更改源文件的 Git 引用。 |
| `--readme-only` | No | Review only the root `README.md` translation. |
| `--format` | No | Output format: `text` or `github`. Defaults to `text`. |

`co-op-review` 当前检查是否缺少已翻译的文件、缺失或过时的翻译元数据、Markdown frontmatter 和代码围栏的完整性、已翻译笔记本的无效 JSON，以及缺失的本地 Markdown 或图像链接目标。缺失的链接默认作为警告；结构性和过时问题会导致命令失败。

## co-op-translator-mcp

为代理、编辑器和与 MCP 兼容的客户端运行 Co-op 翻译器 MCP 服务器。

```bash
co-op-translator-mcp
```

默认传输为 `stdio`。有关客户端配置、工具、资源和安全注意事项，请参阅 [MCP 服务器](mcp.md) 指南。

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

重新处理翻译后的 Markdown 文件并更新笔记本链接，使其在可用时指向翻译后的笔记本。

```bash
migrate-links -l "ko ja"
```

### 常见示例

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

无需确认即可处理所有受支持的语言：

```bash
migrate-links -l "all" -y
```

仅在已存在翻译的笔记本时重写链接：

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### 选项

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, or `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--image-dir` | 否 | 相对于根目录的翻译图像目录。默认为 `translated_images`. |
| `--dry-run` | 否 | 显示将会更改（但不会写入更新）的文件。 |
| `--fallback-to-original`, `--no-fallback-to-original` | 否 | 在翻译后的笔记本缺失时使用原始笔记本链接。默认启用。 |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-y`, `--yes` | 否 | 在处理所有语言时自动确认提示。 |

## 环境

当命令需要提供程序凭据时，请配置以下其中一个提供程序集。 `translate --dry-run` 和 `co-op-review` 不需要提供程序凭据：

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# 或者 OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# 或者 Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

图像翻译还需要 Azure AI Vision：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## 输出布局

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

翻译后的图像输出将写入：

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## 可复制的 CLI 示例

Translate Markdown into three languages:

```bash
translate -l "ko ja fr" -md
```

Translate notebooks only:

```bash
translate -l "zh-CN" -nb
```

Translate images only:

```bash
translate -l "pt-BR" -img
```

预览 Markdown 翻译而不写入文件:

```bash
translate -l "de es" -md --dry-run
```

Repair low-confidence Markdown translations:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Run CI-friendly Markdown translation:

```bash
translate -l "ko ja" -md -y -s
```

Review translated output:

```bash
co-op-review -l "ko ja"
```

Preview link migration:

```bash
migrate-links -l "ko" --dry-run
```