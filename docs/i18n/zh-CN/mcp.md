# MCP 服务器

Co-op Translator 包含一个用于代理、编辑器和与 MCP 兼容的客户端的模型上下文协议服务器。

对于默认的本地设置，用户无需手动保持单独运行的服务器。他们配置他们的 MCP 客户端，客户端在需要 Co-op Translator 工具时会通过 `stdio` 自动启动 `co-op-translator-mcp`。

如果您在 CLI、Python API 和 MCP 之间做决定，请从 [选择你的工作流](workflows.md) 开始。

当代理或编辑器应直接调用 Co-op Translator 时使用 MCP：

| 用户目标 | MCP 工具 |
| --- | --- |
| 翻译一个 Markdown 文档、笔记本或图像 | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| 使用宿主代理模型翻译 Markdown 或笔记本内容 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 选择输出路径后重写已翻译的 Markdown 或笔记本链接 | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| 像 CLI 一样翻译整个仓库 | `run_translation`, `translate_project` |
| 在没有 LLM 凭证的情况下审查已翻译的输出 | `run_review` |
| 检查功能和环境状态 | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP 服务器封装了在 [Python API](api.md) 中记录的相同公共 Python API。基于提供商的工具使用与 CLI 和 Python API 相同配置的提供商。代理辅助工具为 MCP 宿主代理准备分块进行翻译，然后使用 Co-op Translator 重建最终的 Markdown 或笔记本。

## 第 1 步：安装并配置 Co-op Translator

在您的 MCP 客户端将使用的 Python 环境中安装 Co-op Translator：

```bash
pip install co-op-translator
```

对于来自此仓库的本地开发，请以可编辑模式安装该包：

```bash
pip install -e .
```

选择您的 MCP 客户端将使用的翻译模式：

| 模式 | 用途 | 凭证 |
| --- | --- | --- |
| 基于提供商 | Co-op Translator 将调用 `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, 或 `run_translation`。 | 翻译需要 Azure OpenAI、OpenAI 或 Anthropic。图像翻译还需要 Azure AI Vision。 |
| 代理辅助 | MCP 宿主代理翻译由 `start_markdown_agent_translation` 或 `start_notebook_agent_translation` 返回的分块。 | Markdown 或笔记本分块不需要 Co-op Translator 的 LLM 提供商凭证。代理辅助模式尚不涵盖图像翻译。 |

如果您在像 Codex 或 Claude Code 这样的代理内开始进行 Markdown 或笔记本翻译，请从代理辅助模式开始。当您希望 Co-op Translator 自行调用已配置的提供商、正在翻译图像，或正在运行类似 CLI 的仓库级别翻译时，请使用基于提供商的模式。

为基于提供商的工作流配置一个提供商：

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# 或 OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# 或 Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

基于提供商的图像翻译还需要：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    代理辅助模式目前涵盖 Markdown 和笔记本的 Markdown 单元格。图像翻译仍然使用基于提供商的图像流水线，并且需要 Azure AI Vision 来进行 OCR 和布局感知渲染。

## 第 2 步：配置您的 MCP 客户端

对于常规本地 `stdio` 设置，将 Co-op Translator 添加到您的 MCP 客户端配置中。客户端会自动启动和停止该进程。

已安装包的配置：

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

在 Windows 上的源码检出配置：

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

在 macOS 或 Linux 上的源码检出配置：

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

更改 MCP 客户端配置后，重启或重新加载客户端，以便它能发现新服务器。

## 第 3 步：在客户端验证服务器

让 MCP 客户端列出可用工具，或首先调用其中一个只读帮助程序：

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

有用的初步检查：

| 工具 | 要检查的内容 |
| --- | --- |
| `get_api_overview` | 确认服务器可达并显示可用的工作流。 |
| `list_supported_languages` | 确认打包的语言数据可以加载。 |
| `get_configuration_status` | 确认 LLM 和 Vision 提供商可用，且不暴露秘密值。 |

## 第 4 步：选择工作流

### 翻译单个文件或文档

当 MCP 客户端已经拥有文档内容或图像路径，并且希望 Co-op Translator 调用已配置的翻译提供商时，使用基于提供商的内容工具。

对于 Markdown：

1. 调用 `translate_markdown_content`，传入 `document`、`language_code`，可选地传入 `source_path`。
2. 如果翻译结果将写入 Co-op Translator 的输出布局，请调用 `rewrite_markdown_paths`。
3. 让客户端写入或返回最终的 `content`。

对于笔记本：

1. 调用 `translate_notebook_content`，传入笔记本 JSON 和 `language_code`。
2. 如果已翻译的笔记本链接需要针对目标路径进行调整，请调用 `rewrite_notebook_paths`。
3. 写入或返回最终的笔记本 JSON。

对于图像：

1. 调用 `translate_image_content`，传入 `image_path`、`language_code`，以及可选的 `root_dir` 或 `fast_mode`。
2. 读取返回的 `data_base64` 和 `mime_type`。
3. 如果提供了 `output_path`，已翻译的图像也会保存到该路径。

这些内容工具不会执行项目发现、元数据更新、免责声明或自动路径重写。如果您希望宿主代理在没有 Co-op Translator LLM 提供商凭证的情况下翻译 Markdown 或笔记本分块，请使用下面的代理辅助工作流。

### 使用宿主代理模型进行翻译

当您希望 MCP 宿主代理（例如编码助手）生成翻译文本，而不是为 Co-op Translator 配置 LLM 提供商时，请使用代理辅助工具。

在基于聊天的 MCP 客户端中，通常不需要自己编写工具 JSON。请让代理使用代理辅助工作流：

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

对于笔记本，使用相同的模式：

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

如果您的 MCP 客户端支持服务器提示，请使用 `agent_assisted_markdown_translation_prompt`，让客户端加载相同的工作流指令。

对于 Markdown：

1. 调用 `start_markdown_agent_translation`，传入 `document`、`language_code`，并可选地传入 `source_path`。
2. 在宿主代理中按照每个分块的 `prompt` 翻译返回的每个分块。
3. 使用原始 `job` 和包含 `chunk_id` 及 `translated_text` 的已翻译分块调用 `finish_markdown_agent_translation`。
4. 如果内容将写入已翻译的目标路径，请调用 `rewrite_markdown_paths`。

对于笔记本：

1. 调用 `start_notebook_agent_translation`，传入笔记本 JSON 和 `language_code`。
2. 在宿主代理中翻译返回的每个分块。
3. 使用原始 `job` 和已翻译的分块调用 `finish_notebook_agent_translation`。
4. 如果已翻译的笔记本链接需要针对目标路径进行调整，请调用 `rewrite_notebook_paths`。

代理辅助工具不会由 Co-op Translator 调用已配置的 LLM 提供商。宿主代理负责翻译返回的分块。Co-op Translator 处理 Markdown 分块、占位符保留、frontmatter 重建、笔记本单元替换以及翻译后的规范化。

### 翻译整个仓库

当用户希望 Co-op Translator 类似于 `translate` CLI 行为时，请使用 `run_translation`。

仓库翻译默认 `dry_run=true`，以便代理在文件更改前检查范围：

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

The `run_translation` result includes an `events` array with versioned
`co-op.translation.event.v1` progress events. MCP clients should use fields such
as `type`, `stage_key`, `completed`, `total`, and `current_path` instead of
parsing captured console text. Pass `json_events_path` to also write those events
to an NDJSON file.

要允许写入，调用方必须同时设置 `dry_run=false` 和 `confirm_write=true`：

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` 被作为 `run_translation` 的兼容别名暴露。

### 审查已翻译的输出

使用 `run_review` 进行不需要 LLM 或 Vision 凭证的确定性检查：

!!! note "Beta"
    MCP 暴露了测试版的 `run_review` API。它对只读审查工作流是安全的，但审查检查和问题架构可能会演变。

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

结果包含捕获的文本输出以及在可用时的结构化审查摘要。

## 手动运行服务器

手动运行主要用于调试或用于像长时间运行服务器一样工作的传输方式。

调试默认的 stdio 服务器：

```bash
co-op-translator-mcp
```

从源码检出运行：

```bash
python -m co_op_translator.mcp.server
```

运行一个长时运行的 HTTP 或 SSE 服务器：

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

对于本地编辑器和代理集成，优先在第 2 步使用客户端管理的 `stdio` 配置。

## 工具

| 工具 | 目的 | 是否写入文件 |
| --- | --- | --- |
| `translate_markdown_content` | 翻译 Markdown 字符串。 | 否 |
| `translate_notebook_content` | 翻译笔记本 JSON 中的 Markdown 单元格。 | 否 |
| `translate_image_content` | 翻译单张图像中的文本并返回 base64 图像数据。 | 可选，仅当提供 `output_path` 时 |
| `start_markdown_agent_translation` | 为宿主代理准备 Markdown 分块，以便在没有 Co-op Translator LLM 凭证的情况下进行翻译。 | 否 |
| `finish_markdown_agent_translation` | 从宿主代理已翻译的分块重建 Markdown。 | 否 |
| `start_notebook_agent_translation` | 为宿主代理准备笔记本的 Markdown 单元格分块以进行翻译。 | 否 |
| `finish_notebook_agent_translation` | 从宿主代理已翻译的分块重建笔记本 JSON。 | 否 |
| `rewrite_markdown_paths` | 为翻译目标重写 Markdown 正文和 frontmatter 中的路径。 | 否 |
| `rewrite_notebook_paths` | 重写笔记本 Markdown 单元格内的路径。 | 否 |
| `run_translation` | 像 CLI 一样运行项目级别翻译。 | 当 `dry_run=false` 且 `confirm_write=true` 时写入 |
| `translate_project` | `run_translation` 的兼容别名。 | 当 `dry_run=false` 且 `confirm_write=true` 时写入 |
| `run_review` | 运行确定性审查检查。 | 否 |
| `get_configuration_status` | 报告已配置的 LLM 和 Vision 提供商的状态，且不暴露秘密。 | 否 |
| `list_supported_languages` | 列出支持的目标语言代码。 | 否 |
| `get_api_overview` | 描述可用的 MCP 工作流和工具。 | 否 |

## 资源

| 资源 URI | 用途 |
| --- | --- |
| `co-op://api` | 工作流和工具的 JSON 概览。 |
| `co-op://supported-languages` | 支持的语言代码的 JSON 列表。 |
| `co-op://configuration` | 不包含秘密的提供商可用性摘要（JSON）。 |

## 提示

| 提示 | 用途 |
| --- | --- |
| `translate_markdown_document_prompt` | 指导 MCP 客户端完成内容翻译以及可选的路径重写。 |
| `agent_assisted_markdown_translation_prompt` | 指导 MCP 客户端在没有 Co-op Translator LLM 提供商凭证的情况下完成宿主代理的 Markdown 翻译。 |
| `translate_repository_prompt` | 指导 MCP 客户端进行先干运行（dry-run）的仓库翻译。 |

## 复制粘贴示例

翻译 Markdown 内容：

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

重写已翻译的 Markdown 链接：

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

使用宿主代理模型翻译 Markdown：

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

在宿主代理翻译每个返回的分块后，使用 `start_markdown_agent_translation` 返回的完整 `job` 对象完成该作业：

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

预览仓库翻译：

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## 故障排查

| 问题 | 可尝试的操作 |
| --- | --- |
| MCP 客户端找不到 `co-op-translator-mcp`。 | 使用绝对的 Python 可执行文件路径和 `["-m", "co_op_translator.mcp.server"]` 的源码检出配置。 |
| 服务器已列出但翻译失败。 | 调用 `get_configuration_status` 并确认有可用的 LLM 提供商。 |
| 您希望在没有提供商凭证的情况下进行 Markdown 或笔记本翻译。 | 使用 `start_markdown_agent_translation` / `finish_markdown_agent_translation` 或笔记本等效方法，以便宿主代理翻译这些分块。 |
| 图像翻译失败。 | 确认已设置 Azure AI Vision 相关变量并调用 `get_configuration_status`。 |
| 仓库翻译未写入文件。 | 仅在明确的用户批准后设置 `dry_run=false` 和 `confirm_write=true`。 |
| 客户端配置的更改未生效。 | 重启或重新加载 MCP 客户端。 |

## 安全说明

- MCP 工具调用由宿主应用控制，因此仓库翻译默认是 dry-run。
- 完整的仓库翻译可能会创建、更新或删除大量文件。在设置 `confirm_write=true` 之前需要明确的用户批准。
- 配置状态工具永远不会返回 API 密钥、端点或其他秘密值。
- 图像翻译返回 base64 图像数据。大型图像可能产生很大的工具响应。
- 代理辅助工具会将源分块和提示返回给 MCP 宿主。仅在用户愿意将内容发送给该宿主代理模型时使用。