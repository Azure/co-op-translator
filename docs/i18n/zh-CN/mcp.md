# MCP 服务器

Co-op Translator 包含一个用于代理、编辑器和 MCP 兼容客户端的模型上下文协议服务器。

对于默认的本地设置，用户不需要手动单独运行服务器。用户配置他们的 MCP 客户端，当客户端需要 Co-op Translator 工具时，客户端会自动通过 `stdio` 启动 `co-op-translator-mcp`。

如果您在 CLI、Python API 和 MCP 之间犹豫，请从 [选择您的工作流程](workflows.md) 开始。

当代理或编辑器应直接调用 Co-op Translator 时使用 MCP：

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP 服务器封装了 [Python API](api.md) 中记录的相同公共 Python API。基于提供者的工具使用与 CLI 和 Python API 相同配置的提供者。代理辅助工具为 MCP 主机代理准备要翻译的块，然后使用 Co-op Translator 重新构建最终的 Markdown 或笔记本。

## 步骤 1：安装并配置 Co-op Translator

在您的 MCP 客户端将使用的 Python 环境中安装 Co-op Translator：

```bash
pip install co-op-translator
```

对于来自此存储库的本地开发，请以可编辑模式安装该包：

```bash
pip install -e .
```

选择您的 MCP 客户端将使用的翻译模式：

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator 调用 `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, 或 `run_translation`。 | Markdown 和笔记本翻译需要 Azure OpenAI 或 OpenAI。图像翻译还需要 Azure AI Vision。 |
| Agent-assisted | MCP 主机代理翻译由 `start_markdown_agent_translation` 或 `start_notebook_agent_translation` 返回的块。 | Markdown 或笔记本块不需要 Co-op Translator 的 LLM 提供者凭证。图像翻译尚未涵盖代理辅助模式。 |

如果您从像 Codex 或 Claude Code 这样的代理内开始进行 Markdown 或笔记本翻译，请从代理辅助模式开始。当您希望 Co-op Translator 本身调用您配置的提供者、翻译图像或运行类似 CLI 的仓库级别翻译时，请使用基于提供者的模式。

仅为 provider-backed 工作流配置提供者凭证：

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

基于提供者的图像翻译还需要：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## 步骤 2：配置您的 MCP 客户端

对于常规的本地 `stdio` 设置，将 Co-op Translator 添加到您的 MCP 客户端配置中。客户端会自动启动和停止该进程。

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

更改 MCP 客户端配置后，请重启或重新加载客户端以便它可以发现新的服务器。

## 步骤 3：在客户端验证服务器

请让 MCP 客户端列出可用工具，或先调用其中一个只读辅助工具：

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

有用的初步检查：

| Tool | What to check |
| --- | --- |
| `get_api_overview` | 确认服务器可达并显示可用的工作流程。 |
| `list_supported_languages` | 确认打包的语言数据可以被加载。 |
| `get_configuration_status` | 在不暴露秘密值的情况下确认 LLM 和 Vision 提供者的可用性。 |

## 步骤 4：选择工作流程

### 翻译单个文件或文档

当 MCP 客户端已经具有文档内容或图像路径并且希望 Co-op Translator 调用配置的翻译提供者时，使用基于提供者的内容工具。

对于 Markdown：

1. 使用 `document`、`language_code`，可选 `source_path` 调用 `translate_markdown_content`。
2. 如果翻译结果将写入 Co-op Translator 的输出布局，请调用 `rewrite_markdown_paths`。
3. 让客户端写入或返回最终的 `content`。

对于笔记本：

1. 使用笔记本 JSON 和 `language_code` 调用 `translate_notebook_content`。
2. 如果已翻译的笔记本链接需要针对目标路径进行调整，请调用 `rewrite_notebook_paths`。
3. 写入或返回最终的笔记本 JSON。

对于图像：

1. 使用 `image_path`、`language_code`，可选 `root_dir` 或 `fast_mode` 调用 `translate_image_content`。
2. 读取返回的 `data_base64` 和 `mime_type`。
3. 如果提供了 `output_path`，已翻译的图像也会保存到该路径。

内容工具不执行项目发现、元数据更新、免责声明或自动路径重写。如果您希望主机代理在没有 Co-op Translator LLM 提供者凭证的情况下翻译 Markdown 或笔记本块，请使用下面的代理辅助工作流。

### 使用主机代理模型进行翻译

当您希望 MCP 主机代理（例如编码助手）生成翻译文本，而不是为 Co-op Translator 配置 Azure OpenAI 或 OpenAI 时，请使用代理辅助工具。

在基于聊天的 MCP 客户端中，通常不需要您自己编写工具 JSON。请让代理使用代理辅助工作流：

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

如果您的 MCP 客户端支持服务器提示，请使用 `agent_assisted_markdown_translation_prompt` 让客户端加载相同的工作流说明。

对于 Markdown：

1. 使用 `document`、`language_code`，可选 `source_path` 调用 `start_markdown_agent_translation`。
2. 在主机代理中按照块的 `prompt` 翻译每个返回的块。
3. 使用原始的 `job` 和包含 `chunk_id` 与 `translated_text` 的已翻译块调用 `finish_markdown_agent_translation`。
4. 如果内容将写入已翻译的目标路径，请调用 `rewrite_markdown_paths`。

对于笔记本：

1. 使用笔记本 JSON 和 `language_code` 调用 `start_notebook_agent_translation`。
2. 在主机代理中翻译每个返回的块。
3. 使用原始的 `job` 和已翻译的块调用 `finish_notebook_agent_translation`。
4. 如果已翻译的笔记本链接需要目标路径调整，请调用 `rewrite_notebook_paths`。

代理辅助工具不会从 Co-op Translator 调用 Azure OpenAI 或 OpenAI。主机代理负责翻译返回的块。Co-op Translator 处理 Markdown 分块、占位符保留、frontmatter 重建、笔记本单元替换以及翻译后归一化。

### 翻译整个仓库

当用户希望 Co-op Translator 的行为类似于 `translate` CLI 时，使用 `run_translation`。

仓库翻译默认 `dry_run=true`，以便代理在文件更改之前检查范围：

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

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

`translate_project` 作为 `run_translation` 的兼容别名公开。

### 审查翻译输出

对于不需要 LLM 或 Vision 凭证的确定性检查，请使用 `run_review`：

!!! note "Beta"
    MCP exposes the beta `run_review` API. It is safe for read-only review workflows, but review checks and issue schemas may evolve.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

结果包括捕获的文本输出以及可用时的结构化审查摘要。

## 手动运行服务器

手动运行主要用于调试或用于行为类似于长时间运行服务器的传输。

调试默认的 stdio 服务器：

```bash
co-op-translator-mcp
```

从源码检出运行：

```bash
python -m co_op_translator.mcp.server
```

运行长时间运行的 HTTP 或 SSE 服务器：

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

对于本地编辑器和代理集成，优先使用步骤 2 中由客户端管理的 `stdio` 配置。

## 工具

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | 翻译一个 Markdown 字符串。 | No |
| `translate_notebook_content` | 翻译笔记本 JSON 中的 Markdown 单元格。 | No |
| `translate_image_content` | 翻译一张图像中的文本并返回 base64 图像数据。 | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | 为主机代理准备 Markdown 块，以便在没有 Co-op Translator LLM 凭证的情况下翻译。 | No |
| `finish_markdown_agent_translation` | 从主机代理已翻译的块重建 Markdown。 | No |
| `start_notebook_agent_translation` | 为主机代理准备笔记本 Markdown 单元格块以供翻译。 | No |
| `finish_notebook_agent_translation` | 从主机代理已翻译的块重建笔记本 JSON。 | No |
| `rewrite_markdown_paths` | 为已翻译的目标重写 Markdown 正文和 frontmatter 中的路径。 | No |
| `rewrite_notebook_paths` | 重写笔记本 Markdown 单元格内的路径。 | No |
| `run_translation` | 以类似 CLI 的方式运行项目级翻译。 | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | `run_translation` 的兼容别名。 | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | 运行确定性审查检查。 | No |
| `get_configuration_status` | 报告已配置的 LLM 和 Vision 提供者的可用性，且不暴露秘密。 | No |
| `list_supported_languages` | 列出支持的目标语言代码。 | No |
| `get_api_overview` | 描述可用的 MCP 工作流和工具。 | No |

## 资源

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | 工作流和工具的 JSON 概览。 |
| `co-op://supported-languages` | 支持的语言代码的 JSON 列表。 |
| `co-op://configuration` | 提供者可用性摘要的 JSON（不包含秘密）。 |

## 提示

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | 指导 MCP 客户端完成内容翻译并可选地重写路径。 |
| `agent_assisted_markdown_translation_prompt` | 指导 MCP 客户端在没有 Co-op Translator LLM 提供者凭证的情况下通过主机代理进行 Markdown 翻译。 |
| `translate_repository_prompt` | 指导 MCP 客户端先进行 dry-run 的仓库翻译。 |

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
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

使用主机代理模型翻译 Markdown：

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

在主机代理翻译每个返回的块之后，使用 `start_markdown_agent_translation` 返回的完整 `job` 对象完成该作业：

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

## 故障排除

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | 使用绝对的 Python 可执行文件路径以及 `["-m", "co_op_translator.mcp.server"]` 的源码检出配置。 |
| The server is listed but translation fails. | 调用 `get_configuration_status` 并确认有可用的 LLM 提供者。 |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | 使用 `start_markdown_agent_translation` / `finish_markdown_agent_translation` 或相应的笔记本接口，让主机代理翻译这些块。 |
| Image translation fails. | 确认 Azure AI Vision 变量已设置并调用 `get_configuration_status`。 |
| Repository translation does not write files. | 仅在明确的用户批准之后设置 `dry_run=false` 和 `confirm_write=true`。 |
| Changes to client config do not appear. | 重启或重新加载 MCP 客户端。 |

## 安全说明

- MCP 工具调用由主机应用程序的模型控制，因此仓库翻译默认以 dry-run 方式进行。
- 完整的仓库翻译可能会创建、更新或删除大量文件。在将 `confirm_write=true` 之前要求明确的用户批准。
- 配置状态工具从不返回 API 密钥、端点或其他秘密值。
- 图像翻译返回 base64 图像数据。大型图像可能导致大型的工具响应。
- 代理辅助工具将源块和提示返回给 MCP 主机。仅在用户愿意将内容发送到该主机代理模型时使用这些工具。