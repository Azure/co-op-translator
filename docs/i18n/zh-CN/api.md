# Python API

稳定的公共 Python API 从 `co_op_translator.api` 导出。大多数集成使用下列工作流程之一：

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| 翻译单个文件或文档 | 您的应用读取源内容，调用 Co-op Translator 进行翻译，并决定将结果保存到何处。 | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| 为主机代理翻译准备内容 | 您的 MCP 主机或应用模型将翻译分块，而 Co-op Translator 负责分块和重组。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 翻译整个仓库 | 您希望 Python API 的行为像 CLI，并处理发现、输出路径、元数据、清理和写入。 | `run_translation` |

`core`、`config`、`review` 和 `utils` 下的大多数底层模块是这些 API 入口点使用的实现细节。

MCP 客户端通过 [MCP Server](mcp.md) 使用相同的公共 API。直接调用 Python 时请使用此页面，在将 Co-op Translator 暴露给代理或编辑器时请参阅 MCP 指南。如果您在 CLI、Python API 和 MCP 之间犹豫，请从 [Choose Your Workflow](workflows.md) 开始。

## 首次使用 API 的流程

如果您从 Python 代码调用 Co-op Translator，请从这里开始：

1. 按照 [Configuration](configuration.md) 中的说明配置 LLM 提供商，除非您只是为主机代理翻译准备 Markdown 或 notebook 的分块。
2. 决定您的应用是否负责文件 I/O。
3. 当您的应用读取和写入单个文件时使用内容 API。
4. 当希望 Co-op Translator 像 CLI 一样处理仓库时使用 `run_translation`。
5. 如果在自动化中需要确定性的检查，在翻译后使用 `run_review`。

| Goal | API to start with |
| --- | --- |
| 翻译一个 Markdown 字符串或文件 | `translate_markdown_content` |
| 翻译一个 notebook 有效载荷 | `translate_notebook_content` |
| 翻译一张图片 | `translate_image_content` |
| 让主机代理翻译 Markdown 或 notebook 分块 | `start_markdown_agent_translation` 或 `start_notebook_agent_translation` |
| 在选择输出路径后重写已翻译的链接 | `rewrite_markdown_paths` 或 `rewrite_notebook_paths` |
| 翻译完整仓库 | `run_translation` |
| 审查已翻译的输出 | `run_review` |

## 场景 1：翻译单个文件或文档

当您已经拥有文件、编辑器缓冲区、notebook 有效载荷、MCP 请求或自定义管道输入时使用此工作流程。您的代码负责文件 I/O：

1. 读取源内容。
2. 调用内容翻译 API。
3. 如果翻译后的内容将写入项目翻译文件夹，可选择调用路径重写 API。
4. 从您的应用保存或返回结果。

内容翻译 API 不会运行项目发现、不写入元数据、不附加免责声明，也不会自动重写链接。

### Markdown 文件

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

如果翻译后的 Markdown 不会存放在 Co-op Translator 项目布局中，请跳过 `rewrite_markdown_paths` 并直接保存翻译后的字符串。

### 笔记本文件

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

`translate_notebook_content` 翻译 Markdown 单元格并保留非 Markdown 单元格。路径重写仅应用于 Markdown 单元格。

### 图片文件

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

`translate_image_content` 读取源图像并返回呈现后的 `PIL.Image.Image`。它不会写入翻译后的图像元数据。

## 场景 2：翻译整个仓库

当您希望 Python API 的行为类似于 `translate` CLI 时使用此工作流程。`run_translation` 会发现受支持的文件，翻译选定的内容类型，重写路径，写入输出文件，更新元数据，并执行翻译维护任务（例如清理）。

`run_translation` 是首选的项目编排入口点。`translate_project` 作为兼容别名导出，行为相同。

将当前仓库中的 Markdown 文件翻译为韩语和日语：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

仅翻译来自特定项目根目录的 notebooks：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

在不写入文件的情况下预览翻译量：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

为集成记录结构化进度事件：

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # 将负载存储在你的作业事件表中，或将其流式传输到你的用户界面。


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

事件使用版本化的模式 `co-op.translation.event.v1`。集成应当
依赖诸如 `type` 和 `stage_key` 之类的稳定字段，而不是面向人的
控制台文本或 `stage_label`。

在一次调用中翻译多个内容根：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

将翻译写入显式的输出组：

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

当每种语言应包含嵌套子目录时，使用每语言占位符：

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

如果未设置 `markdown`、`notebook` 或 `images`，API 将翻译所有受支持的类型：Markdown、notebook 和图像。

### 使用翻译状态提供者保留已接受的人类编辑

默认情况下，Co-op Translator 保持其现有的文件级行为：当一个
Markdown 源已过时时，整个翻译文件会被重新生成。托管的
集成可以可选地传入 `TranslationStateProvider`，以保留人类
在未更改的源块中的编辑。

该提供者提供最后已接受的源/目标对并记录每个新的
候选项。接受仍然是集成的责任——例如，
在翻译拉取请求被合并之后：

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

对于具有有效已接受基线的 Markdown 文件，Co-op Translator 对齐
顶层 Markdown 块。未更改的源块重用当前的已翻译
块，包括人所做的编辑；已更改或新增的源块将被发送
进行翻译；已删除的源块将被移除。如果对齐存在歧义，
目标结构已改变、块翻译无效，或没有基线，
Co-op Translator 将安全地回退到现有的全文件
翻译路径。

该 API 存储文档翻译状态，而不是跨文档的短语或
段落级翻译记忆。它当前适用于 Markdown 项目
翻译。Notebook 和图像的行为保持不变。传入 `update=True`
仍会请求完全重新生成。

如果一个或多个文件无法翻译，`run_translation` 会在项目工作流完成后引发一个
`RuntimeError`，而不是报告一次
成功运行但缺少输出。集成应将此视为失败的
作业并保留先前已接受的翻译状态。

## 审查已翻译的输出

`run_review` 在无需 LLM 或 Vision 凭证的情况下运行确定性的翻译检查。

!!! note "Beta"
    `run_review` 是一个处于测试阶段的确定性审查 API。它不会调用模型提供者或写入文件，但检查和问题的模式可能会改变。

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

在仅翻译 README 之后，使用相同的范围进行审查：

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` 只会审查每个配置的源根目录下的 `README.md`，
包括自定义的 `groups` 和输出目录。其他文档和嵌套的
README 会被排除。缺少源 README 会引发 `ValueError`；翻译检查失败会
引发 `RuntimeError`。

仅审查相对于基准引用有更改的文件并打印 GitHub 风格的输出：

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

## 复制粘贴 API 示例

翻译 Markdown 内容但不写入文件：

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

翻译并重写 Markdown 链接：

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

从 Python 翻译整个仓库：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

翻译多个根目录：

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

保留术语表中的术语：

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

## 公开入口点

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## 内容翻译 API

内容翻译 API 旨在用于那些内容已在内存中的集成场景，例如编辑器扩展、MCP 工具、笔记本处理器或自定义管道。

| 函数 | 输入 | 输出 | 文件 I/O | 备注 |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | 否 | 异步。仅翻译 Markdown 内容。不重写链接、不写入元数据或附加免责声明。 |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | 否 | 异步。翻译 Markdown 单元并保留非 Markdown 单元。不重写链接、不写入元数据或附加免责声明。 |
| `translate_image_content` | Image path | `PIL.Image.Image` | 仅读取源图像 | 同步。提取并翻译图像文本，然后返回渲染后的图像。不保存已翻译图像的元数据。 |

`translate_markdown_content` 和 `translate_notebook_content` 通过它们的选项接受可选的 `source_path`。该路径作为上下文传递给翻译器；调用方仍需负责在翻译后进行任何特定于项目的路径重写。

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

相同的选项也可以作为字典传入：

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## 代理辅助翻译 API

代理辅助 API 不会调用 Co-op Translator 中配置的 LLM 提供者。它们准备供宿主代理翻译的 Markdown 或笔记本块，然后从已翻译的块重建最终内容。

| 函数 | 目的 |
| --- | --- |
| `start_markdown_agent_translation` | 返回一个自包含的 Markdown 作业，包含块、提示和重建状态。 |
| `finish_markdown_agent_translation` | 从作业和宿主代理翻译的块中重建 Markdown。 |
| `start_notebook_agent_translation` | 返回一个包含供宿主代理翻译的 Markdown 单元块的笔记本作业。 |
| `finish_notebook_agent_translation` | 在保留代码单元、输出和元数据的同时重建笔记本 JSON。 |

该工作流主要针对 MCP 主机。如果您需要由 Co-op Translator 管理提供者调用的生产仓库翻译，请使用 `translate_markdown_content`、`translate_notebook_content` 或 `run_translation`。

## 路径重写 API

路径重写 API 不执行翻译。它们在调用方知道源路径、已翻译的目标路径和项目布局之后，更新链接和 frontmatter 中的路径。

| 函数 | 范围 | 备注 |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown 正文和 frontmatter | 为已翻译的目标重写 Markdown 链接和受支持的 frontmatter 路径字段。 |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | 将 Markdown 路径重写应用到每个 Markdown 单元，并保持非 Markdown 单元不变。 |

`policy` 参数可以是包含以下字段的字典：

| 字段 | 必需 | 用途 |
| --- | --- | --- |
| `language_code` | 是 | 目标语言代码，例如 `"ko"` 或 `"pt-BR"`。 |
| `root_dir` | 否 | 源项目根目录。默认值为 `"."`。 |
| `translations_dir` | 否 | 文本翻译输出目录。默认在 `root_dir` 下为 `translations`。 |
| `translated_images_dir` | 否 | 已翻译图像输出目录。默认在 `root_dir` 下为 `translated_images`。 |
| `translation_types` | 否 | 启用的翻译类型。默认包括 Markdown、笔记本和图像。 |
| `lang_subdir` | 否 | 每个语言文件夹下的可选子目录。 |

## 项目翻译参数

| 参数 | 类型 | 默认 | 用途 |
| --- | --- | --- | --- |
| `language_codes` | `str` | 必需 | 以空格分隔的目标语言代码，例如 `"ko ja fr"`，或 `"all"`。别名代码会标准化为规范的 BCP 47 值。 |
| `root_dir` | `str` | `"."` | 用于单一翻译目标的项目根目录。当提供 `root_dirs` 或 `groups` 时将被忽略。 |
| `update` | `bool` | `False` | 删除并重新创建所选语言的现有翻译。 |
| `images` | `bool` | `False` | 包括图像翻译。需要配置 Azure AI Vision。 |
| `markdown` | `bool` | `False` | 包含 Markdown 翻译。 |
| `notebook` | `bool` | `False` | 包含 Jupyter 笔记本翻译。 |
| `debug` | `bool` | `False` | 启用调试日志记录。 |
| `save_logs` | `bool` | `False` | 将在根目录下的 `logs/` 目录中保存 DEBUG 级别日志文件。 |
| `yes` | `bool` | `True` | 自动确认提示以便程序化和 CI 使用。 |
| `add_disclaimer` | `bool` | `False` | 向已翻译的 Markdown 和笔记本添加机器翻译声明。 |
| `translations_dir` | `str \| None` | `None` | 自定义文本翻译输出目录。相对路径相对于每个根目录解析。 |
| `image_dir` | `str \| None` | `None` | 自定义翻译后图像输出目录。相对路径相对于每个根目录解析。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 共享相同输出设置的多个根目录。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 显式的 `(root_dir, translations_dir)` 对。优先于 `root_dirs`。 |
| `repo_url` | `str \| None` | `None` | 在呈现 README 语言表指导时使用的仓库 URL。 |
| `glossaries` | `Iterable[str] \| None` | `None` | 翻译过程中需保留的术语表条目。重复项和空白条目将被规范化。 |
| `dry_run` | `bool` | `False` | 估算翻译量并预览迁移行为而不写入文件。 |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | 用于增量 Markdown 更新的可选已接受基线和候选持久化适配器。省略此项将保留现有的全文件行为。 |

## 审查参数

`run_review` 有意在可能的情况下模仿 `run_translation` 的签名，以便自动化可以在翻译和审查工作流之间以最少的分支进行切换。

| 参数 | 类型 | 默认 | 用途 |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | 要审查的目标语言文件夹。接受以空格分隔的字符串和可迭代对象。 "all" 会审查所有发现的翻译语言。 |
| `root_dir` | `str` | `"."` | 单个审查目标的项目根目录。当提供 `root_dirs` 或 `groups` 时忽略。 |
| `markdown` | `bool` | `False` | 包含 Markdown 和 MDX 源文件。 |
| `notebook` | `bool` | `False` | 包含 Jupyter 笔记本源文件。 |
| `images` | `bool` | `False` | 保留以与翻译选项保持一致。图像的链接引用从 Markdown 中检查。 |
| `translations_dir` | `str \| None` | `None` | 自定义文本翻译输出目录。相对路径相对于每个根目录解析。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 共享相同输出设置的多个根目录。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 显式的 `(root_dir, translations_dir)` 对。优先于 `root_dirs`。 |
| `changed_from` | `str \| None` | `None` | 用于限制审查仅包含已更改源文件的 Git 引用。 |
| `readme_only` | `bool` | `False` | 仅审查每个源根目录下的 `README.md`。缺少源 README 会引发 `ValueError`。 |
| `output_format` | `str` | `"text"` | 审查输出格式。支持的值为 `"text"` 和 `"github"`。 |
| `fail_on_warnings` | `bool` | `False` | 将警告视为失败（与错误一样处理）。 |
| `debug` | `bool` | `False` | 启用调试日志。 |
| `save_logs` | `bool` | `False` | 将 DEBUG 级别的日志文件保存到根目录下的 `logs/` 目录。 |

如果未设置 `markdown`、`notebook` 或 `images` 中的任何一个，API 会在适用的情况下审核 Markdown、笔记本 和 图像链接引用。审核不会调用 LLM provider，也不需要 API keys。

## 配置要求

由提供者支持的翻译 APIs 在翻译之前需要进行提供者配置：

- Markdown 和笔记本的翻译需要一个 LLM 提供者。请配置 Azure OpenAI、OpenAI 或 Anthropic。
- 图像翻译除了 Azure AI Vision 外，还需要 LLM provider。
- `run_translation` 在项目翻译开始前运行轻量级连接检查。
- 使用代理协助的 `start_*_agent_translation` 和 `finish_*_agent_translation` APIs 不会调用 Co-op Translator LLM providers。宿主应用或 MCP agent 翻译准备好的分块。
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, 和 `run_review` 是确定性的，不需要提供者凭据。

所需的 Azure OpenAI 变量：

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

所需的 OpenAI 变量：

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

所需的 Anthropic 变量：

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` 和 `ANTHROPIC_MAX_TOKENS` 是可选的。 从 Co-op Translator 0.22.0 开始，Microsoft Agent Framework 是所有提供者的默认模型客户端。 仍然可以临时使用 `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` 选择 Semantic Kernel，但这样做会发出弃用警告；有关分阶段删除计划，请参见 [配置](configuration.md#model-client-backend)。

用于图像翻译的所需 Azure AI Vision 变量：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` 是确定性的，不需要 LLM 或 Azure AI Vision 的配置。

## 行为说明

- 内容翻译 API 将翻译与项目路径重写分离。当翻译后的内容需要为目标位置调整项目前相对链接时，请显式调用 `rewrite_markdown_paths` 或 `rewrite_notebook_paths`。
- 项目编排 API 在内容翻译周围添加项目级行为，包括文件发现、写入、路径重写、元数据、清理和可选的免责声明。
- `run_translation` 通过与 CLI 使用的相同 Rich 支持的报告器打印进度和估算摘要。非交互式输出回退为纯文本。
- `dry_run=True` 使用虚拟的 README 更新来计算估算，但不写入 README 或翻译文件。
- `groups` 按顺序处理。在工作开始前会打印单个汇总估算。
- 当选择图像翻译时，缺少 Vision 配置会在翻译开始前引发错误。
- 会检测现有基于别名的语言文件夹，并可以在运行中将其迁移为规范的语言文件夹名称。
- `run_review` 会在翻译文件缺失、翻译元数据缺失或过时、Markdown frontmatter/代码围栏格式错误，以及翻译后的 notebook JSON 无效时失败。
- `run_review` 默认将本地 Markdown 和图像链接目标缺失报告为警告。

## 内部调用路径

该 API 委托给 CLI 使用的相同核心实现：

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. 面向项目的专注翻译 mixins，适用于 Markdown、笔记本和图像。
8. Markdown、笔记本、文本和图像翻译器位于 `co_op_translator.core` 下。

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

以下类对维护者有用，但不会作为包级别的稳定 API 导出。

| 类 | 模块 | 职责 |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | 协调项目级翻译、目录管理、按语言的元数据规范化，以及委托给 Markdown、笔记本和图像翻译器。 |
| `TranslationManager` | `co_op_translator.core.project.translation` | 执行 Markdown、笔记本、图像、过期检测和翻译元数据更新的异步文件处理工作。 |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | 协调 Markdown 文件读取、内容翻译、路径重写、元数据、免责声明和写入。 |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | 协调笔记本文件读取、Markdown 单元格翻译、路径重写、元数据、免责声明和写入。 |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | 协调源图像发现、图像翻译、输出路径、元数据和写入。 |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | 查找已翻译的 Markdown 配对，评估翻译质量，并读取低置信度修复工作流的置信度元数据。 |
| `ReviewRunner` | `co_op_translator.review.runner` | 协调针对源文件、目标语言和配置的翻译根目录的确定性审查检查。 |
| `ReviewTarget` | `co_op_translator.review.targets` | 描述要为其审查的源根目录和翻译输出目录。 |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | 检测遗留的别名语言文件夹并准备规范 BCP 47 文件夹迁移计划。 |
| `Config` | `co_op_translator.config.base_config` | 加载 `.env` 文件并检查所需的 LLM 和可选的 Vision 提供商是否已配置。 |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | 自动检测 Azure OpenAI、OpenAI 或 Anthropic，验证所需的环境变量，并运行提供商连通性检查。 |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | 检测 Azure AI Vision 配置并为图像翻译运行连通性检查。 |