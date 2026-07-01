# Python API

Di stable public Python API dey exported from `co_op_translator.api`. Most integrations dey use one of dis workflows:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | If your app dey read source content, dey call Co-op Translator for translation, and fit decide where to save di result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | If your MCP host or application model go translate chunks, while Co-op Translator dey handle chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | If you want make di Python API behave like di CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

Most lower-level modules under `core`, `config`, `review`, and `utils` na implementation details wey dem dey use for these API entry points.

MCP clients dey use di same public API through di [MCP Server](mcp.md). Use dis page when you dey call Python directly, and use di MCP guide when you dey expose Co-op Translator to an agent or editor. If you dey decide between CLI, Python API, and MCP, start with [Choose Your Workflow](workflows.md).

## First-Time API Flow

Start here if you dey call Co-op Translator from Python code:

1. Configure an LLM provider like e dey describe for [Configuration](configuration.md), unless na only preparing Markdown or notebook chunks you dey do for host-agent translation.
2. Decide if your application go handle file I/O.
3. Use content APIs when your app dey read and write individual files.
4. Use `run_translation` when you want Co-op Translator to process repository like di CLI.
5. Use `run_review` after translation if you need deterministic checks for automation.

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

Use dis workflow when you don already get file, editor buffer, notebook payload, MCP request, or custom pipeline input. Your code go handle file I/O:

1. Read di source content.
2. Call one content translation API.
3. If need, call path rewriting API if di translated content go dey write inside project translation folder.
4. Save or return di result from your application.

Di content translation APIs no dey run project discovery, dem no dey write metadata, dem no dey append disclaimers, and dem no dey rewrite links automatically.

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

If di translated Markdown no go live for Co-op Translator project layout, skip `rewrite_markdown_paths` and save di translated string directly.

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

`translate_notebook_content` dey translate Markdown cells and e go preserve non-Markdown cells. Path rewriting dey apply only to Markdown cells.

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

`translate_image_content` go read di source image and return a rendered `PIL.Image.Image`. E no dey write translated image metadata.

## Scenario 2: Translate an Entire Repository

Use dis workflow when you want make di Python API behave like di `translate` CLI. `run_translation` go discover supported files, translate selected content types, rewrite paths, write output files, update metadata, and do translation maintenance tasks like cleanup.

`run_translation` na di preferred project orchestration entry point. `translate_project` na exported compatibility alias wey get same behavior.

Translate Markdown files for di current repository into Korean and Japanese:

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

Use a per-language placeholder when each language suppose get nested subdirectory:

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

If none of `markdown`, `notebook`, or `images` dey set, di API go translate all supported types: Markdown, notebooks, and images.

## Review Translated Output

`run_review` dey run deterministic translation checks without LLM or Vision credentials.

!!! note "Beta"
    `run_review` na beta deterministic review API. E no dey call model providers or write files, but checks and issue schemas fit still change.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Review only files wey don change against a base ref and print GitHub-flavored output:

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

Content translation APIs dem suppose make sense for integrations wey don already get content for memory, like editor extension, MCP tool, notebook processor, or custom pipeline.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. E dey translate only Markdown content. E no dey rewrite links, write metadata, or append disclaimers. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. E dey translate Markdown cells and e dey preserve non-Markdown cells. E no dey rewrite links, write metadata, or append disclaimers. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. E go extract and translate image text, then return rendered image. E no go save translated image metadata. |

`translate_markdown_content` and `translate_notebook_content` fit accept optional `source_path` through their options. Di path dey pass as context to di translator; callers still dey responsible for any project-specific path rewriting after translation.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Di same options fit pass as dictionaries:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Agent-assisted APIs no dey call Azure OpenAI or OpenAI from Co-op Translator. Dem dey prepare Markdown or notebook chunks for host agent to translate, then dem go reconstruct final content from translated chunks.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while e dey preserve code cells, outputs, and metadata. |

Dis workflow mainly dey intended for MCP hosts. If you need production repository translation with Co-op Translator wey go manage provider calls, use `translate_markdown_content`, `translate_notebook_content`, or `run_translation`.

## Path Rewriting APIs

Path rewriting APIs no dey perform any translation. Dem go update links and frontmatter paths after callers don sabi di source path, translated target path, and project layout.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | E dey rewrite Markdown links and supported frontmatter path fields for translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | E go apply Markdown path rewriting to each Markdown cell and leave non-Markdown cells unchanged. |

Di `policy` argument fit be dictionary wey get these fields:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, like `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Default na `"."`. |
| `translations_dir` | No | Text translation output directory. Default na `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Default na `translated_images` under `root_dir`. |
| `translation_types` | No | Enabled translation types. Default na Markdown, notebooks, and images. |
| `lang_subdir` | No | Optional subdirectory under each language folder. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Space-separated target language codes, like `"ko ja fr"`, or `"all"`. Alias codes dey normalize to canonical BCP 47 values. |
| `root_dir` | `str` | `"."` | Project root for single translation target. Dem ignore am when `root_dirs` or `groups` dey supplied. |
| `update` | `bool` | `False` | Delete and recreate existing translations for di selected languages. |
| `images` | `bool` | `False` | Include image translation. E need Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Turn on debug logging. |
| `save_logs` | `bool` | `False` | Save DEBUG-level log files under di root `logs/` directory. |
| `yes` | `bool` | `True` | Auto-confirm prompts for programmatic and CI usage. |
| `add_disclaimer` | `bool` | `False` | Add machine translation disclaimers to translated Markdown and notebooks. |
| `translations_dir` | `str \| None` | `None` | Custom text translation output directory. Relative paths dey resolve against each root. |
| `image_dir` | `str \| None` | `None` | Custom translated image output directory. Relative paths dey resolve against each root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Multiple roots wey share same output settings. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs. E get precedence pass `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository URL wey dem go use when dem dey render README language table guidance. |
| `glossaries` | `Iterable[str] \| None` | `None` | Glossary terms wey you wan preserve during translation. Duplicates and blank terms go normalize. |
| `dry_run` | `bool` | `False` | Estimate translation volume and preview migration behavior without writing files. |

## Review Parameters

`run_review` intentionally dey mirror di `run_translation` signature where possible so automation fit switch between translation and review workflows with small changes.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables dey accepted. `"all"` go review every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for single review target. Dem ignore am when `root_dirs` or `groups` dey supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved so e go match translation options. Link references to images dey checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | Custom directory wey translations go land. Relative paths dey resolve against each root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Plenty roots wey dey share di same output settings. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs. E get precedence pass `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref wey dem dey use to limit review to changed source files. |
| `output_format` | `str` | `"text"` | Review output format. Supported values na `"text"` and `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Treat warnings like failures join errors. |
| `debug` | `bool` | `False` | Turn on debug logging. |
| `save_logs` | `bool` | `False` | Save DEBUG-level log files for di root `logs/` directory. |

If none of `markdown`, `notebook`, or `images` are set, the API go review Markdown, notebooks, and image link references where e fit. Review no dey call any LLM provider and e no need API keys.

## Wetin Configuration Need

Provider-backed translation APIs need provider configuration before dem fit translate:

- Markdown and notebook translation need an LLM provider. Configure either Azure OpenAI or OpenAI.
- Image translation need Azure AI Vision in addition to the LLM provider.
- `run_translation` dey run small connectivity checks before project translation begin.
- Agent-assisted `start_*_agent_translation` and `finish_*_agent_translation` APIs no dey call Co-op Translator LLM providers. Di host application or MCP agent na dem go translate di prepared chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` dem deterministic and no need provider credentials.

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

`run_review` na deterministic and e no need Azure OpenAI, OpenAI, or Azure AI Vision configuration.

## Notes About How E Dey Work

- Content translation APIs dey keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content need make project-relative links adjust to di target location.
- Project orchestration APIs dey add project behavior around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` go print progress and estimate summaries through Click, to match the CLI user experience.
- `dry_run=True` go compute estimates using virtual README updates, but e no go write di README or translation files.
- `groups` dem dey processed one after another. One aggregate estimate go print before work begin.
- When image translation dey selected and Vision configuration missing, e go raise an error before translation start.
- Existing alias-based language folders dey detected and fit be migrated to canonical BCP 47 folder names as part of the run.
- `run_review` go fail on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` dey report missing local Markdown and image link targets as warnings by default.

## How Di Internal Call Dey Flow

The API dey delegate to the same core implementation wey the CLI dey use:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Project translation mixins wey focus on Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators wey dey under `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks wey dey under `co_op_translator.review.checks`

The following classes dey useful for maintainers, but dem no export dem as the package-level stable API.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | E dey coordinate project-level translation, directory management, per-language metadata normalization, and e dey delegate to Markdown, notebook, and image translators. |
| `TranslationManager` | `co_op_translator.core.project.translation` | E dey perform the async file processing work for Markdown, notebooks, images, stale detection, and translation metadata updates. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | E dey orchestrate Markdown file reads, content translation, path rewriting, metadata, disclaimers, and writes. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | E dey orchestrate notebook file reads, Markdown-cell translation, path rewriting, metadata, disclaimers, and writes. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | E dey orchestrate source image discovery, image translation, output paths, metadata, and writes. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | E dey find translated Markdown pairs, evaluate translation quality, and read confidence metadata for low-confidence repair workflows. |
| `ReviewRunner` | `co_op_translator.review.runner` | E dey coordinate deterministic review checks across source files, target languages, and configured translation roots. |
| `ReviewTarget` | `co_op_translator.review.targets` | E dey describe a source root and the translation output directory wey dem review for that root. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | E dey detect legacy alias language folders and e dey prepare canonical BCP 47 folder migration plans. |
| `Config` | `co_op_translator.config.base_config` | E dey load `.env` files and e dey check whether required LLM and optional Vision providers dey configured. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | E dey auto-detect Azure OpenAI or OpenAI, e dey validate required environment variables, and e dey run provider connectivity checks. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | E dey detect Azure AI Vision configuration and e dey run connectivity checks for image translation. |