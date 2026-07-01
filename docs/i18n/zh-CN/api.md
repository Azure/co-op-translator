# Python API

The stable public Python API is exported from `co_op_translator.api`. Most integrations use one of these workflows:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

Most lower-level modules under `core`, `config`, `review`, and `utils` are implementation details used by these API entry points.

MCP clients use the same public API through the [MCP Server](mcp.md). Use this page when calling Python directly, and the MCP guide when exposing Co-op Translator to an agent or editor. If you are deciding between CLI, Python API, and MCP, start with [Choose Your Workflow](workflows.md).

## First-Time API Flow

Start here if you are calling Co-op Translator from Python code:

1. Configure an LLM provider as described in [Configuration](configuration.md), unless you are only preparing Markdown or notebook chunks for host-agent translation.
2. Decide whether your application owns file I/O.
3. Use content APIs when your application reads and writes individual files.
4. Use `run_translation` when Co-op Translator should process a repository like the CLI.
5. Use `run_review` after translation if you need deterministic checks in automation.

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenario 1: Translate Individual Files or Documents

Use this workflow when you already have a file, editor buffer, notebook payload, MCP request, or custom pipeline input. Your code owns file I/O:

1. Read the source content.
2. Call a content translation API.
3. Optionally call a path rewriting API if the translated content will be written into a project translation folder.
4. Save or return the result from your application.

The content translation APIs do not run project discovery, do not write metadata, do not append disclaimers, and do not rewrite links automatically.

### Markdown File

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


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
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

If the translated Markdown will not live in a Co-op Translator project layout, skip `rewrite_markdown_paths` and save the translated string directly.

### Notebook File

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` translates Markdown cells and preserves non-Markdown cells. Path rewriting is applied only to Markdown cells.

### Image File

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` reads the source image and returns a rendered `PIL.Image.Image`. It does not write translated image metadata.

## Scenario 2: Translate an Entire Repository

Use this workflow when you want the Python API to behave like the `translate` CLI. `run_translation` discovers supported files, translates selected content types, rewrites paths, writes output files, updates metadata, and performs translation maintenance tasks such as cleanup.

`run_translation` is the preferred project orchestration entry point. `translate_project` is exported as a compatibility alias with the same behavior.

Translate Markdown files in the current repository into Korean and Japanese:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Translate only notebooks from a specific project root:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Preview translation volume without writing files:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Translate multiple content roots in one call:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Write translations into explicit output groups:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

Use a per-language placeholder when each language should contain a nested subdirectory:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

If none of `markdown`, `notebook`, or `images` are set, the API translates all supported types: Markdown, notebooks, and images.

## Review Translated Output

`run_review` runs deterministic translation checks without LLM or Vision credentials.

!!! note "Beta"
    `run_review` is a beta deterministic review API. It does not call model providers or write files, but checks and issue schemas may evolve.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Review only files changed against a base ref and print GitHub-flavored output:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## Copy-Paste API Examples

Translate Markdown content without file writes:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Translate and rewrite Markdown links:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Translate a repository from Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Translate multiple roots:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

Preserve glossary terms:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## Public Entry Points

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## Content Translation APIs

Content translation APIs are intended for integrations that already have content in memory, such as an editor extension, MCP tool, notebook processor, or custom pipeline.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Translates Markdown content only. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Translates Markdown cells and preserves non-Markdown cells. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Extracts and translates image text, then returns a rendered image. It does not save translated image metadata. |

`translate_markdown_content` and `translate_notebook_content` accept an optional `source_path` through their options. The path is passed as context to the translator; callers remain responsible for any project-specific path rewriting after translation.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

The same options can be passed as dictionaries:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Agent-assisted APIs do not call Azure OpenAI or OpenAI from Co-op Translator. They prepare Markdown or notebook chunks for a host agent to translate, then reconstruct the final content from translated chunks.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return a self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from a job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return a notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while preserving code cells, outputs, and metadata. |

This workflow is mainly intended for MCP hosts. If you need production repository translation with Co-op Translator managing provider calls, use `translate_markdown_content`, `translate_notebook_content`, or `run_translation`.

## Path Rewriting APIs

Path rewriting APIs perform no translation. They update links and frontmatter paths after callers know the source path, translated target path, and project layout.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Rewrites Markdown links and supported frontmatter path fields for a translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Applies Markdown path rewriting to each Markdown cell and leaves non-Markdown cells unchanged. |

The `policy` argument may be a dictionary with these fields:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | No | Enabled translation types. Defaults to Markdown, notebooks, and images. |
| `lang_subdir` | No | Optional subdirectory under each language folder. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Space-separated target language codes, such as `"ko ja fr"`, or `"all"`. Alias codes are normalized to canonical BCP 47 values. |
| `root_dir` | `str` | `"."` | Project root for a single translation target. Ignored when `root_dirs` or `groups` are supplied. |
| `update` | `bool` | `False` | Delete and recreate existing translations for the selected languages. |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | Save DEBUG-level log files under the root `logs/` directory. |
| `yes` | `bool` | `True` | Auto-confirm prompts for programmatic and CI usage. |
| `add_disclaimer` | `bool` | `False` | Add machine translation disclaimers to translated Markdown and notebooks. |
| `translations_dir` | `str \| None` | `None` | Custom text translation output directory. Relative paths resolve against each root. |
| `image_dir` | `str \| None` | `None` | Custom translated image output directory. Relative paths resolve against each root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Multiple roots that share the same output settings. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs. Takes precedence over `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository URL used when rendering README language table guidance. |
| `glossaries` | `Iterable[str] \| None` | `None` | Glossary terms to preserve during translation. Duplicates and blank terms are normalized. |
| `dry_run` | `bool` | `False` | Estimate translation volume and preview migration behavior without writing files. |

## Review Parameters

`run_review` intentionally mirrors the `run_translation` signature where possible so automation can switch between translation and review workflows with minimal branching.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | 自定义文本翻译输出目录。相对路径相对于每个根目录解析。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 共享相同输出设置的多个根目录。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 显式的 `(root_dir, translations_dir)` 对。优先于 `root_dirs`。 |
| `changed_from` | `str \| None` | `None` | 用于限制审查到已更改源文件的 Git 引用。 |
| `output_format` | `str` | `"text"` | 审查输出格式。支持的值为 `"text"` 和 `"github"`。 |
| `fail_on_warnings` | `bool` | `False` | 将警告视为与错误一样的失败。 |
| `debug` | `bool` | `False` | 启用调试日志记录。 |
| `save_logs` | `bool` | `False` | 在根目录的 `logs/` 目录下保存 DEBUG 级别的日志文件。 |

如果未设置 `markdown`、`notebook` 或 `images`，API 将在适用情况下审查 Markdown、笔记本和图像链接引用。审查不调用 LLM 提供者，并且不需要 API 密钥。

## 配置要求

基于提供者的翻译 API 在翻译之前需要配置提供者：

- Markdown 和笔记本翻译需要 LLM 提供者。配置 Azure OpenAI 或 OpenAI 中的任意一种。
- 图像翻译除了需要 LLM 提供者外，还需要 Azure AI Vision。
- `run_translation` 在项目翻译开始之前运行轻量级的连接性检查。
- Agent 辅助的 `start_*_agent_translation` 和 `finish_*_agent_translation` APIs 不会调用 Co-op Translator LLM 提供者。主机应用或 MCP agent 翻译准备好的块。
- `rewrite_markdown_paths`、`rewrite_notebook_paths` 和 `run_review` 是确定性的，不需要提供者凭证。

Required Azure OpenAI variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Required OpenAI variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Required Azure AI Vision variables for image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` 是确定性的，不需要 Azure OpenAI、OpenAI 或 Azure AI Vision 配置。

## 行为说明

- 内容翻译 API 将翻译与项目路径重写分离。当翻译后的内容需要将项目相对链接调整为目标位置时，请显式调用 `rewrite_markdown_paths` 或 `rewrite_notebook_paths`。
- 项目编排 API 在内容翻译周围添加项目行为，包括文件发现、写入、路径重写、元数据、清理和可选免责声明。
- `run_translation` 通过 Click 打印进度和估算摘要，匹配 CLI 用户体验。
- `dry_run=True` 使用虚拟 README 更新计算估算，但不会写入 README 或翻译文件。
- `groups` 按顺序处理。工作开始前会打印单个汇总估算。
- 当选择图像翻译时，缺少 Vision 配置会在翻译开始前引发错误。
- 检测到现有基于别名的语言文件夹，并且可以作为运行的一部分迁移到规范的语言文件夹名称。
- `run_review` 在以下情况下失败：缺少翻译文件、缺少或过时的翻译元数据、损坏的 Markdown frontmatter/代码围栏，以及无效的已翻译笔记本 JSON。
- `run_review` 默认将本地缺失的 Markdown 和图像链接目标报告为警告。

## 内部调用路径

该 API 委托给与 CLI 使用相同的核心实现：

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` 用于内存中翻译。
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` 用于显式路径后处理。
3. `co_op_translator.api.translation.run_translation` 用于完整的项目编排。
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. 针对 Markdown、笔记本和图像的项目翻译 mixins。
8. 位于 `co_op_translator.core` 下的 Markdown、笔记本、文本和图像翻译器。

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. 在 `co_op_translator.review.checks` 下的确定性检查

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | 协调项目级翻译、目录管理、每语言元数据规范化，并将工作委派给 Markdown、笔记本和图像翻译器。 |
| `TranslationManager` | `co_op_translator.core.project.translation` | 执行针对 Markdown、笔记本、图像的异步文件处理工作、过时检测以及翻译元数据更新。 |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | 协调 Markdown 文件读取、内容翻译、路径重写、元数据、免责声明和写入。 |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | 协调笔记本文件读取、Markdown 单元格翻译、路径重写、元数据、免责声明和写入。 |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | 协调源图像发现、图像翻译、输出路径、元数据和写入。 |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | 查找已翻译的 Markdown 配对，评估翻译质量，并读取置信度元数据以用于低置信度修复工作流程。 |
| `ReviewRunner` | `co_op_translator.review.runner` | 协调跨源文件、目标语言和已配置翻译根目录的确定性审查检查。 |
| `ReviewTarget` | `co_op_translator.review.targets` | 描述一个源根目录以及为该根目录审查的翻译输出目录。 |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | 检测旧的别名语言文件夹并准备规范的 BCP 47 文件夹迁移计划。 |
| `Config` | `co_op_translator.config.base_config` | 加载 `.env` 文件并检查是否配置了所需的 LLM 以及可选的 Vision 提供者。 |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | 自动检测 Azure OpenAI 或 OpenAI，验证所需的环境变量，并运行提供者连接性检查。 |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | 检测 Azure AI Vision 配置并为图像翻译运行连接性检查。 |