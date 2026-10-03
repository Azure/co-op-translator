# 选择您的工作流

Co-op Translator 可以通过三种方式使用：CLI、Python API 和 MCP 服务器。它们具有相同的翻译能力，但各自适合不同的工作流。

在决定从哪里开始时请使用此页面。

**如果您手动编辑翻译：** 默认的 CLI 和 Actions 工作流会对已更改的源文件进行完整的重新翻译，因此这些文件中的措辞可能会被覆盖。在接受更新之前请审查差异(diff)。要保留已接受编辑的 Markdown 块级结构，请使用可选的 [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider)。

## 快速决策

| 如果您想... | 使用 | 从这里开始 |
| --- | --- | --- |
| 在终端中翻译或审查存储库 | CLI | [CLI Reference](cli.md) |
| 将翻译添加到 Python 脚本、服务、笔记本或 CI 作业 | Python API | [Python API](api.md) |
| 让代理、编辑器或兼容 MCP 的客户端为您翻译内容 | MCP Server | [MCP Server](mcp.md) |
| 翻译您的应用已加载的单个 Markdown 文档、笔记本或图像 | Python API 或 MCP Server | [Python API](api.md) 或 [MCP Server](mcp.md) |
| 使用标准输出文件夹和元数据翻译整个存储库 | CLI 或 `run_translation` | [CLI Reference](cli.md) 或 [Python API](api.md) |

## 何时使用 CLI

当有人或 CI 作业从 shell 驱动存储库翻译时，请选择 CLI。

当您希望 Co-op Translator 自动发现项目文件、创建翻译输出、保留项目布局、更新元数据并运行审查命令时，CLI 是最直接的途径。

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

此示例翻译 Markdown 和笔记本。仅在配置 [Azure AI Vision](configuration.md#azure-ai-vision) 之后添加 `-img`。如果想首次只翻译 Markdown，请参阅 [Your first translation](first-translation.md)。

适合情况：

- 您正在从终端翻译一个存储库。
- 您希望为 CI 或发布工作流提供可重复的命令。
- 您希望具有内置的项目发现、输出路径、元数据、清理和审查功能。
- 您更喜欢命令界面而不是编写 Python 代码。

## 何时使用 Python API

当您的代码需要控制工作流时，请选择 Python API。

该 API 适用于应用、自动化脚本、笔记本、服务和自定义流水线。它允许您调用用于单个文件的低级内容翻译 API，或运行 CLI 使用的相同存储库级编排。

翻译一个 Markdown 文档并决定保存位置：

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

从 Python 运行存储库翻译：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

适合情况：

- 您的应用已读取文件、缓冲区、笔记本或图像字节。
- 您需要自定义验证、存储、日志记录、重试或审批流程。
- 您想在不处理整个存储库的情况下翻译单个文档、笔记本或图像。
- 您希望翻译存储库，但通过 Python 自动化而不是 shell 命令。

## 何时使用 MCP 服务器

当代理、编辑器或兼容 MCP 的客户端应调用 Co-op Translator 工具时，请选择 MCP 服务器。

在普通的本地设置中，用户不需要手动保持服务器运行。MCP 客户端在需要这些工具时通过 `stdio` 启动 `co-op-translator-mcp`。

代理可能处理的示例用户请求：

- "将此 Markdown 文件翻译为韩语并保持链接正确。"
- "使用代理辅助的 MCP 工作流将此 Markdown 文件翻译为韩语，并使用您自己的模型翻译各个片段。"
- "将此笔记本翻译为韩语，保留代码单元，并使用 Co-op Translator MCP 重建笔记本。"
- "将此图像中的文本翻译为日语并保存结果。"
- "对存储库翻译执行预演（dry-run）为西班牙语，并告诉我会有哪些更改。"
- "检查韩语翻译输出是否是最新的。"

对于 Markdown 和笔记本，MCP 可以以两种模式工作：

| 模式 | 何时使用 | 主要工具 |
| --- | --- | --- |
| Agent-assisted | 当 MCP 主机代理应使用其自己的模型翻译片段，而不使用 Co-op Translator LLM 提供商凭据。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator 应直接调用 Azure OpenAI、OpenAI 或 Anthropic。 | `translate_markdown_content`, `translate_notebook_content` |

MCP 提供方支持的 Markdown 工具调用格式：

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP 图像工具调用格式：

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

通过 MCP，存储库翻译默认以 dry-run（演练）方式进行：

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

适合情况：

- 您希望在代理或编辑器内部使用自然语言的翻译工作流。
- 您希望在主机代理模型翻译已准备片段的情况下进行 Markdown 或笔记本翻译。
- 您希望代理翻译选定内容，而不是整个存储库。
- 您希望在整个存储库写入之前有审批步骤。
- 您希望有一个接口，提供 Markdown、笔记本、图像、审查和路径重写工具。

## 它们如何协同工作

对于人工翻译存储库，CLI 是最佳默认选项。当您的代码负责工作流时，Python API 最适合。当代理或编辑器负责工作流时，MCP 服务器最合适。

这三种方式都使用相同的公共 Co-op Translator API，因此您可以先从 CLI 开始，随后用 Python 自动化，并在需要代理驱动的工作流时将相同功能暴露给 MCP 客户端。