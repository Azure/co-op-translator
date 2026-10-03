# Python API

Di stable public Python API dey exported from `co_op_translator.api`. Most integrations dey use one of dis workflows:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Wen your app dey read source content, dey call Co-op Translator do translation, and e dey decide where to save di result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Wen your MCP host or application model go translate chunks, while Co-op Translator dey handle chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Wen you want make di Python API behave like di CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

Most lower-level modules under `core`, `config`, `review`, and `utils` na implementation details wey dem dey use for these API entry points.

MCP clients dey use di same public API through di [MCP Server](mcp.md). Use dis page when you dey call Python directly, and use di MCP guide when you dey expose Co-op Translator to an agent or editor. If you dey decide between CLI, Python API, and MCP, start with [Choose Your Workflow](workflows.md).

## First-Time API Flow

Start here if you dey call Co-op Translator from Python code:

1. Configure an LLM provider as dem talk for [Configuration](configuration.md), unless na only preparing Markdown or notebook chunks for host-agent translation you dey do.
2. Decide whether your application dey handle file I/O.
3. Use content APIs when your app dey read and write individual files.
4. Use `run_translation` when Co-op Translator suppose process a repository like di CLI.
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

Use dis workflow when you don already get file, editor buffer, notebook payload, MCP request, or custom pipeline input. Your code dey own file I/O:

1. Read di source content.
2. Call one content translation API.
3. If you want, call one path rewriting API if di translated content go near inside project translation folder.
4. Save or return di result from your application.

Di content translation APIs no dey run project discovery, no dey write metadata, no dey append disclaimers, and dem no dey rewrite links automatically.

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

`translate_notebook_content` dey translate Markdown cells and e dey preserve non-Markdown cells. Path rewriting dey apply only to Markdown cells.

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

`translate_image_content` dey read di source image and e return one rendered `PIL.Image.Image`. E no dey write translated image metadata.

## Scenario 2: Translate an Entire Repository

Use dis workflow when you want make di Python API behave like di `translate` CLI. `run_translation` dey discover supported files, translate selected content types, rewrite paths, write output files, update metadata, and perform translation maintenance tasks like cleanup.

`run_translation` na di preferred project orchestration entry point. `translate_project` dey exported as compatibility alias wey get di same behavior.

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

Record structured progress events for an integration:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Put di payload for your job-event table or stream am go your UI.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Events dey use di versioned schema `co-op.translation.event.v1`. Integrations suppose
depend on stable fields like `type` and `stage_key`, no depend on human-facing
console text or `stage_label`.

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

Use a per-language placeholder when each language suppose get a nested subdirectory:

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

### Preserve accepted human edits with a translation state provider

By default, Co-op Translator dey keep dia existing file-level behavior: when one
Markdown source don stale, di whole translated file go get regenerated. Hosted
integrations fit optionally pass one `TranslationStateProvider` to preserve human
edits inside source blocks wey never change.

Di provider dey supply di last accepted source/target pair and e dey record each new
candidate. Acceptance still na di integration responsibility—for example,
after one translation pull request don merge:

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

For Markdown files wey get valid accepted baseline, Co-op Translator dey align
top-level Markdown blocks. Source blocks wey never change go reuse di current translated
blocks, including edits wey people do; source blocks wey change or wey dem add go get send
for translation; deleted source blocks go remove. If alignment dey ambiguous,
di target structure don change, block translation invalid, or no baseline dey,
Co-op Translator go safely fallback to di existing full-file
translation path.

Dis API dey store document translation state, no be cross-document phrase or
segment translation memory. E right now dey apply to Markdown project
translation. Notebook and image behavior remain unchanged. Passing `update=True`
still dey request full regeneration.

If one or more files no fit translate, `run_translation` go raise one
`RuntimeError` after di project workflow finish instead of to report one
successful run wey get missing output. Integrations suppose treat dis as failed
job and retain di previous accepted translation state.

## Review Translated Output

`run_review` dey run deterministic translation checks without LLM or Vision credentials.

!!! note "Beta"
    `run_review` na beta deterministic review API. E no dey call model providers or write files, but checks and issue schemas fit change over time.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

After one README-only translation, use di same scope for review:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` go review only `README.md` wey dey under each configured source root,
including custom `groups` and output directories. Other documents and nested
READMEs dem dey excluded. If source README missing e go raise `ValueError`; failed
translation checks go raise `RuntimeError`.

Review only files wey change compare to a base ref and print GitHub-flavored output:

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

Translate Markdown content without writing files:

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

## Content Translation APIs

Content translation APIs dem suppose for integrations wey don already get content for memory, like editor extension, MCP tool, notebook processor, or custom pipeline.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Dey translate Markdown content only. E no dey rewrite links, write metadata, or append disclaimers. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Dey translate Markdown cells and e preserve non-Markdown cells. E no dey rewrite links, write metadata, or append disclaimers. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Dey extract and translate image text, then return rendered image. E no dey save translated image metadata. |

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

Agent-assisted APIs no dey call di configured LLM provider from Co-op Translator. Dem dey prepare Markdown or notebook chunks make host agent translate, then dem go reconstruct di final content from translated chunks.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return one self-contained Markdown job wey get chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from one job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return one notebook job wey get Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON and preserve code cells, outputs, and metadata. |

Dis workflow dey mainly for MCP hosts. If you need production repository translation with Co-op Translator wey go manage provider calls, use `translate_markdown_content`, `translate_notebook_content`, or `run_translation`.

## Path Rewriting APIs

Path rewriting APIs no dey perform translation. Dem dey update links and frontmatter paths after callers don know di source path, translated target path, and project layout.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Rewrites Markdown links and supported frontmatter path fields for a translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Apply Markdown path rewriting to each Markdown cell and leave non-Markdown cells unchanged. |

Di `policy` argument fit be one dictionary wey get these fields:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, like `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | No | Enabled translation types. Defaults to Markdown, notebooks, and images. |
| `lang_subdir` | No | Optional subdirectory under each language folder. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Space-separated target language codes, like `"ko ja fr"`, or `"all"`. Alias codes dey normalize to canonical BCP 47 values. |
| `root_dir` | `str` | `"."` | Project root for a single translation target. Ignored when `root_dirs` or `groups` dey supplied. |
| `update` | `bool` | `False` | Delete and recreate existing translations for di selected languages. |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | Save DEBUG-level log files under di root `logs/` directory. |
| `yes` | `bool` | `True` | Dey auto-confirm prompts for programmatic and CI usage. |
| `add_disclaimer` | `bool` | `False` | Put machine translation disclaimer dem for translated Markdown and notebooks. |
| `translations_dir` | `str \| None` | `None` | Custom text translation output directory. Relative paths dey resolve against each root. |
| `image_dir` | `str \| None` | `None` | Custom translated image output directory. Relative paths dey resolve against each root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Multiple roots wey share the same output settings. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs. E dey take precedence over `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository URL wey dem go use when rendering README language table guidance. |
| `glossaries` | `Iterable[str] \| None` | `None` | Glossary terms wey dem go preserve during translation. Duplicates and blank terms go dey normalized. |
| `dry_run` | `bool` | `False` | Estimate how much translation go be and preview migration behaviour without writing files. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Optional accepted-baseline and candidate persistence adapter for incremental Markdown updates. If you omit am, e go preserve existing full-file behavior. |

## Review Parameters

`run_review` intentionally mirrors the `run_translation` signature where possible so automation fit switch between translation and review workflows with minimal branching.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders wey you wan review. Space-separated strings and iterables dey accepted. `"all"` go review every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. E no dey considered when `root_dirs` or `groups` dey supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images dey checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | Custom text translation output directory. Relative paths dey resolve against each root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Multiple roots wey share the same output settings. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs. E dey take precedence over `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref wey dem go use to limit review to just changed source files. |
| `readme_only` | `bool` | `False` | Review only `README.md` under each source root. If source README dey miss e go raise `ValueError`. |
| `output_format` | `str` | `"text"` | Review output format. Supported values na `"text"` and `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Make warnings count as failures in addition to errors. |
| `debug` | `bool` | `False` | Turn on debug logging. |
| `save_logs` | `bool` | `False` | Save DEBUG-level log files under the root `logs/` directory. |

If none of `markdown`, `notebook`, or `images` are set, the API go review Markdown, notebooks, and image link references where applicable. Review no dey call any LLM provider and no need API keys.

## Configuration Requirements

Provider-backed translation APIs need provider configuration before dem fit translate:

- Markdown and notebook translation require an LLM provider. Configure Azure OpenAI, OpenAI, or Anthropic.
- Image translation requires Azure AI Vision in addition to the LLM provider.
- `run_translation` runs lightweight connectivity checks before project translation begins.
- Agent-assisted `start_*_agent_translation` and `finish_*_agent_translation` APIs no dey call Co-op Translator LLM providers. The host application or MCP agent go translate the prepared chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` dem be deterministic and no require provider credentials.

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

Required Anthropic variables:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` and `ANTHROPIC_MAX_TOKENS` dey optional. Microsoft Agent Framework na the default model client for all providers starting with Co-op Translator 0.22.0. Semantic Kernel fit still dey selected temporarily with `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, but if you do, e go emit a deprecation warning; see [configuration](configuration.md#model-client-backend) for the staged removal plan.

Required Azure AI Vision variables for image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` na deterministic and e no require LLM or Azure AI Vision configuration.

## Behavior Notes

- Content translation APIs dey keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content need project-relative links adjusted for a target location.
- Project orchestration APIs add project behaviour around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` go print progress and estimate summaries through the same Rich-backed reporter wey the CLI use. Non-interactive output go fall back to plain text.
- `dry_run=True` go compute estimates using virtual README updates, but e no go write the README or translation files.
- `groups` dem go process sequentially. One aggregate estimate go print before work begin.
- When image translation dey selected, missing Vision configuration go raise error before translation start.
- Existing alias-based language folders dem dey detected and fit get migrated to canonical language folder names as part of the run.
- `run_review` go fail on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` go report missing local Markdown and image link targets as warnings by default.

## Internal Call Path

The API dey delegate to the same core implementation used by the CLI:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes dey useful for maintainers, but dem no exported as the package-level stable API.

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
| `Config` | `co_op_translator.config.base_config` | E dey load `.env` files and check whether required LLM and optional Vision providers dem configured. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | E dey auto-detect Azure OpenAI, OpenAI, or Anthropic, validate required environment variables, and run provider connectivity checks. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | E dey detect Azure AI Vision configuration and run connectivity checks for image translation. |