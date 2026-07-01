# 选择你的工作流

Co-op Translator 可通过三种方式使用：CLI、Python API 和 MCP 服务器。它们共享相同的翻译功能，但各自适合不同的工作流。

在决定从哪里开始时使用本页。

## 快速决策

| 如果您想... | 使用 | 从这里开始 |
| --- | --- | --- |
| 在终端中翻译或审查仓库 | CLI | [CLI 参考](cli.md) |
| 将翻译添加到 Python 脚本、服务、笔记本或 CI 作业 | Python API | [Python API](api.md) |
| 让代理、编辑器或兼容 MCP 的客户端为您翻译内容 | MCP 服务器 | [MCP 服务器](mcp.md) |
| 翻译您的应用已加载的一个 Markdown 文档、笔记本或图像 | Python API 或 MCP 服务器 | [Python API](api.md) 或 [MCP 服务器](mcp.md) |
| 翻译整个仓库并生成标准输出文件夹和元数据 | CLI 或 `run_translation` | [CLI 参考](cli.md) 或 [Python API](api.md) |

## 何时使用 CLI

当个人或 CI 作业通过 shell 驱动仓库翻译时，选择 CLI。

CLI 是最直接的路径，当您希望 Co-op Translator 自动发现项目文件、创建翻译输出、保留项目布局、更新元数据并运行审查命令时。

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

适用场景：

- 您正在从终端翻译仓库。
- 您希望为 CI 或发布工作流程创建可重复的命令。
- 您希望内置项目发现、输出路径、元数据、清理和审查功能。
- 相比编写 Python 代码，您更喜欢命令行界面。

## 何时使用 Python API

当您的代码应控制工作流程时，选择 Python API。

该 API 适用于应用程序、自动化脚本、笔记本、服务和自定义管道。它允许您为单个文件调用低级内容翻译 API，或运行与 CLI 相同的仓库级编排。

翻译一个 Markdown 文档并决定将其保存到何处：

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

从 Python 运行仓库翻译：

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

适用场景：

- 您的应用程序已经读取文件、缓冲区、笔记本或图像字节。
- 您需要自定义验证、存储、日志记录、重试或审批流程。
- 您想翻译单个文档、笔记本或图像，而不处理整个仓库。
- 您想进行仓库翻译，但希望通过 Python 自动化而不是 shell 命令。

## 何时使用 MCP 服务器

当代理、编辑器或兼容 MCP 的客户端应调用 Co-op Translator 工具时，选择 MCP 服务器。

在正常的本地设置中，用户不会手动保持服务器运行。当需要工具时，MCP 客户端会通过 `stdio` 启动 `co-op-translator-mcp`。

代理可能处理的示例用户请求：

- "将此 Markdown 文件翻译为韩语并保持链接正确。"
- "使用代理辅助的 MCP 工作流程将此 Markdown 文件翻译为韩语，并为翻译的块使用您自己的模型。"
- "将此笔记本翻译为韩语，保留代码单元，并使用 Co-op Translator MCP 重建笔记本。"
- "将此图像中的文本翻译为日语并保存结果。"
- "对仓库翻译进行西班牙语的预演，并告诉我会有哪些更改。"
- "审核韩语翻译输出是否为最新。"

对于 Markdown 和笔记本，MCP 可以以两种模式工作：

| 模式 | 使用场景 | 主要工具 |
| --- | --- | --- |
| 代理辅助 | MCP 主机代理应使用其自己的模型翻译块，而无需 Co-op Translator LLM 提供者凭据。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 提供者支持 | Co-op Translator 应直接调用 Azure OpenAI 或 OpenAI。 | `translate_markdown_content`, `translate_notebook_content` |

MCP 提供者支持的 Markdown 工具调用格式：

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

通过 MCP 进行仓库翻译默认是预演（dry-run）：

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

适用场景：

- 您希望在代理或编辑器中使用自然语言翻译工作流程。
- 您希望主机代理模型翻译已准备的块来处理 Markdown 或笔记本翻译。
- 您希望代理翻译选定的内容而不是整个仓库。
- 您希望在对整个仓库写入之前有一个审批步骤。
- 您希望有一个接口，能提供 Markdown、笔记本、图像、审查和路径重写工具。

## 它们如何协同工作

对于人工从事仓库翻译的情况，CLI 是最佳默认选择。当您的代码负责工作流程时，Python API 最适合。当代理或编辑器负责工作流程时，MCP 服务器最合适。

这三条路径都使用相同的公共 Co-op Translator API，因此您可以先从 CLI 开始，随后用 Python 自动化，并在需要代理驱动的工作流时向 MCP 客户端公开相同的功能。