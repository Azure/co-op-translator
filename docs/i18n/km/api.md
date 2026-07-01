# Python API

The stable public Python API is exported from `co_op_translator.api`. Most integrations use one of these workflows:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | កម្មវិធីរបស់អ្នកអានមាតិកាដើម ហៅ Co-op Translator សម្រាប់ការបកប្រែ ហើយសម្រេចថានឹងរក្សាទុកលទ្ធផលនៅឯណា។ | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | ម៉ាស៊ីនទទួល MCP របស់អ្នក ឬម៉ូឌែលកម្មវិធី​នឹងបកប្រែក្នុងឈុត (chunks) ខណៈដែល Co-op Translator ជួយរៀបចំការបំបែក និងការស្តារឡើងវិញ។ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | អ្នកចង់ឲ្យ Python API ប្រតិបត្តិដូច CLI ហើយគ្រប់គ្រងការរកឃើញ ឯកសារបង្ហាញ ផ្លូវទិន្នផល មេតាដាតា ការសម្អាត និងការសរសេរ។ | `run_translation` |

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
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. បកប្រែ​មាតិកា Markdown ប៉ុណ្ណោះ។ មិនធ្វើការ rewrite links ទេ មិនសរសេរ metadata ហើយមិនបន្ថែម disclaimer ទេ។ |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. បកប្រែជា Markdown cells និងរក្សា non-Markdown cells ទុកដូចដើម។ មិនធ្វើការ rewrite links ទេ មិនសរសេរ metadata ហើយមិនបន្ថែម disclaimer ទេ។ |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. ទាញយក និងបកប្រែអត្ថបទនៅលើរូបភាព ហើយត្រឡប់មកជារូបភាពដែលបាន rendered។ មិនរក្សា metadata រូបភាពដែលបានបកប្រែទេ។ |

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
| `language_codes` | `str` | Required | កូដភាសាគោលដៅដែលបានបំបែកដោយចន្លោះ ទដូចជា `"ko ja fr"` ឬ `"all"`។ Alias codes ត្រូវបាន normalized ទៅជា canonical BCP 47 values។ |
| `root_dir` | `str` | `"."` | មូលដ្ឋានគម្រោងសម្រាប់គោលដៅបកប្រែតែមួយ។ មិនអនុវត្តនៅពេលដែលផ្តល់ `root_dirs` ឬ `groups`។ |
| `update` | `bool` | `False` | លុប និងបង្កើតឡើងវិញការបកប្រែមុនសម្រាប់ភាសាដែលបានជ្រើស។ |
| `images` | `bool` | `False` | រួមបញ្ចូលការបកប្រែរូបភាព។ តម្រូវឲ្យមានកំណត់កុងហ្វហ្គឺរ Azure AI Vision។ |
| `markdown` | `bool` | `False` | រួមបញ្ចូលការបកប្រែ Markdown។ |
| `notebook` | `bool` | `False` | រួមបញ្ចូលការបកប្រែ Jupyter notebook។ |
| `debug` | `bool` | `False` | បើក logging សម្រាប់ debug។ |
| `save_logs` | `bool` | `False` | រក្សាទុកឯកសារ log នៅកម្រិត DEBUG ក្រោមថត `logs/` នៅ root។ |
| `yes` | `bool` | `True` | បញ្ជាក់អូតូម៉ាទិកសំណួរសម្រាប់ប្រើប្រាស់ក្នុង script និង CI។ |
| `add_disclaimer` | `bool` | `False` | បន្ថែមការបដិសេធនៃការបកប្រែដោយម៉ាស៊ីនទៅ Markdown និង notebooks ដែលបានបកប្រែ។ |
| `translations_dir` | `str \| None` | `None` | ថតលទ្ធផលសម្រាប់ការបកប្រែអត្ថបទប្ដូរផ្ទាល់។ ផ្លូវសាប់ជាអក្សារអាស្រ័យលើមូលដ្ឋាននីមួយៗ។ |
| `image_dir` | `str \| None` | `None` | ថតលទ្ធផលសម្រាប់រូបភាពដែលបានបកប្រែ។ ផ្លូវសាប់ជាអក្សារអាស្រ័យលើមូលដ្ឋាននីមួយៗ។ |
| `root_dirs` | `Iterable[str] \| None` | `None` | មូលដ្ឋានច្រើនដែលចែករំលែកកំណត់ការបង្ហាញលទ្ធផលដូចគ្នា។ |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | ជាគូ `(root_dir, translations_dir)` ដែលបានបញ្ជាក់។ មានអាទិភាពលើ `root_dirs`។ |
| `repo_url` | `str \| None` | `None` | URL របស់ repository ដែលប្រើពេលបង្ហាញតារាងភាសា README។ |
| `glossaries` | `Iterable[str] \| None` | `None` | ពាក្យក្នុង glossary ដែលចង់រក្សាទុកនៅពេលបកប្រែ។ ពាក្យចម្លង និងពាក្យចន្លោះទទេ នឹងត្រូវ normalized។ |
| `dry_run` | `bool` | `False` | សិក្សាបរិមាណការបកប្រែ និងមើលជាមុនពីនិយមន័យការផ្លាស់ទីដោយគ្មានការសរសេរ ឯកសារ។ |

## Review Parameters

`run_review` intentionally mirrors the `run_translation` signature where possible so automation can switch between translation and review workflows with minimal branching.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | ថតភាសាគោលដៅសម្រាប់ពិនិត្យ។ អាចប្រើ string ដែលបំបែកដោយចន្លោះ ឬ iterable ។ `"all"` ពិនិត្យរាល់ភាសាបកប្រែដែលរកឃើញបាន។ |
| `root_dir` | `str` | `"."` | មូលដ្ឋានគម្រោងសម្រាប់ការពិនិត្យតែមួយ។ មិនអនុវត្តនៅពេលដែលផ្តល់ `root_dirs` ឬ `groups`។ |
| `markdown` | `bool` | `False` | រួមបញ្ចូលឯកសារ Markdown និង MDX ដើម។ |
| `notebook` | `bool` | `False` | រួមបញ្ចូលឯកសារ Jupyter notebook ដើម។ |
| `images` | `bool` | `False` | រក្សាទុកសម្រាប់គោលដៅស្រដៀងនឹងជម្រើសការបកប្រែ។ ឯកសារយោងទៅរូបភាពត្រូវបានពិនិត្យពី Markdown។ |
| `translations_dir` | `str \| None` | `None` | ថតចេញសម្រាប់លទ្ធផលការបកប្រែអត្ថបទផ្ទាល់ខ្លួន។ ផ្លូវទាក់ទង (relative paths) នឹងត្រូវបានដោះស្រាយទាក់ទងនឹង root នីមួយៗ។ |
| `root_dirs` | `Iterable[str] \| None` | `None` | root ច្រើនដែលចែករំលែកការកំណត់លទ្ធផលដូចគ្នា។ |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | គូ `(root_dir, translations_dir)` បញ្ជាក់ជាក់លាក់។ មានអាទិភាពលើ `root_dirs`។ |
| `changed_from` | `str \| None` | `None` | Git ref ដែលប្រើដើម្បីកំណត់ការពិនិត្យទៅឯកសារដើមដែលបានប្តូរ។ |
| `output_format` | `str` | `"text"` | ទ្រង់ទ្រាយលទ្ធផលពិនិត្យ។ តម្លៃដែលគាំទ្រ​គឺ `"text"` និង `"github"`។ |
| `fail_on_warnings` | `bool` | `False` | ចាត់ទុកការព្រមានជាការបរាជ័យ បន្ថែមពីលើកំហុស។ |
| `debug` | `bool` | `False` | បើកកំណត់ហេតុ debug។ |
| `save_logs` | `bool` | `False` | រក្សាទុកឯកសារ​កំណត់ហេតុកម្រិត DEBUG នៅក្រោមថត `logs/` នៃ root។ |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## តម្រូវការកំណត់រចនាសម្ព័ន្ធ

API បកប្រែដែលពឹងផ្អែកលើអ្នកផ្គត់ផ្គង់ ត្រូវការការកំណត់អ្នកផ្គត់ផ្គង់មុនពេលបកប្រែ៖

- ការបកប្រែ Markdown និង notebook ត្រូវការអ្នកផ្គត់ផ្គង់ LLM។ កំណត់ Azure OpenAI ឬ OpenAI មួយ។
- ការបកប្រែរូបភាពត្រូវការព្រមទាំង Azure AI Vision លើសពីអ្នកផ្គត់ផ្គង់ LLM។
- `run_translation` ប្រតិបត្តិការត្រួតពិនិត្យការតភ្ជាប់ទំងន់ស្រាល មុនការបកប្រែគម្រោងចាប់ផ្តើម។
- API ជំនួយដោយ agent `start_*_agent_translation` និង `finish_*_agent_translation` មិនហៅ Co-op Translator LLM providers ទេ។ កម្មវិធីម៉ាក់ហូស (host application) ឬ agent MCP នឹងបកប្រែចំណែកដែលបានរៀបចំ។
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, និង `run_review` គីប្រកបដោយភាពកំណត់ច្បាស់ (deterministic) ហើយមិនទាមទារអះអាងសម្គាល់ (credentials) នៃអ្នកផ្គត់ផ្គង់។

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

`run_review` គឺប្រាកដន័យ និងមិនទាមទារការកំណត់ Azure OpenAI, OpenAI, ឬ Azure AI Vision ទេ។

## កត់សម្គាល់អាកប្បកម្ម

- API បកប្រែអត្ថបទរក្សាការបកប្រែឲ្យបែកពីការកែផ្លូវគម្រោង។ កុំភ្លេចហៅ `rewrite_markdown_paths` ឬ `rewrite_notebook_paths` ពេលដែលមាតិកាបកប្រែត្រូវការកែតម្រូវតំណភ្ជាប់ទាក់ទងគម្រោងសម្រាប់ទីតាំងគោលដៅ។
- API គ្រប់គ្រងគម្រោងបន្ថែមឥរិយាបទជុំវិញការបកប្រែមាតិកា រួមមានការស្វែងរកឯកសារ ការសរសេរ ការកែផ្លូវ មេតាដែនទី ការសម្អាត និងការបញ្ចាក់ជាជម្រើស។
- `run_translation` បោះពុម្ពច progresso និង សេចក្តីសន្និដ្ឋានការប៉ាន់ស្មានតាម Click ដើម្បីផ្គូផ្គងនឹងបទពិសោធន៍ CLI។
- `dry_run=True` គណនាការប៉ាន់ស្មានដោយប្រើការអាប់ដេត README ពីចំណុចក្លែងក្លាយ ប៉ុន្តែមិនសរសេរ README ឬឯកសារបកប្រែឡើយ។
- `groups` ត្រូវបានដំណើរការតាមលំដាប់។ មានការបោះពុម្ពសេចក្តីសន្និដ្ឋានសរុបមួយមុនការងារចាប់ផ្តើម។
- នៅពេលជ្រើសរើសការបកប្រែរូបភាព ការខកខានក្នុងការកំណត់ Vision នឹងបង្កការកើតកំហុសមុនការចាប់ផ្តើមបកប្រែ។
- ថតភាសាដែលមានឈ្មោះប្រើ alias ពីមុននឹងត្រូវបានរកឃើញ ហើយអាចធ្វើការផ្លាស់ទីទៅឈ្មោះថតភាសាតាម BCP 47 តាមផ្នែកនៃរត់នោះបាន។
- `run_review` ព្រុះបរាជ័យពេលឯកសារបកប្រែបាត់ ការ​មេតាដែលបកប្រែបាត់ឬចាស់ ប្រហោង frontmatter/code fences នៃ Markdown ដែលខូច សុទ្ធភាព JSON របស់ notebook បកប្រែមិនត្រឹមត្រូវ។
- `run_review` រាយការណ៍ការខកខាននៃគោលដៅ Markdown និងតំណរូបភាពក្នុងលוקាល់ជាការព្រមានដោយលំនាំដើម។

## ផ្លូវហៅខាងក្នុង

API នេះប្រគល់ទៅកាន់ការអនុវត្តមូលដ្ឋានដូចគ្នាដែល CLI ប្រើ៖

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` សម្រាប់ការបកប្រែនៅក្នុងចំណាំ memory។
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` សម្រាប់ការបន្ទាប់បន្សំផ្លូវ (explicit path post-processing)។
3. `co_op_translator.api.translation.run_translation` សម្រាប់ការគ្រប់គ្រងគម្រោងពេញលេញ។
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`។
5. `co_op_translator.core.project.ProjectTranslator`។
6. `co_op_translator.core.project.TranslationManager`।
7. focused project translation mixins សម្រាប់ Markdown, notebooks, និង រូបភាព។
8. អ្នកបកប្រែ Markdown, notebook, អត្ថបទ, និង រូបភាព នៅក្រោម `co_op_translator.core`។

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. ការត្រួតពិនិត្យប្រាកដនិយមនៅក្រោម `co_op_translator.review.checks`

ថ្នាក់ដូចតទៅមានប្រយោជន៍សម្រាប់អ្នកថែទាំ ប៉ុន្តែមិនត្រូវបាននាំចេញជារមូល API ថាស្ថិរភាពនៅកម្រិត package។

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | សម្របសម្រួលការបកប្រែនៅកម្រិតគម្រោង ការគ្រប់គ្រងថត ការធម្មតាមេតាដាតាតាមភាសា និងការបញ្ជូនទៅអ្នកបកប្រែ Markdown, notebook និង រូបភាព។ |
| `TranslationManager` | `co_op_translator.core.project.translation` | ប្រតិបត្តិការងាររីករាយ async សម្រាប់ដំណើរការឯកសារ Markdown, notebooks, រូបភាព ការស្វែងរក stale និងការអាប់ដេតមេតាដាតាបកប្រែ។ |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | សម្របសម្រួលការអានឯកសារ Markdown ការបកប្រែមាតិកា ការកែផ្លូវ មេតាដា ទីការបដិសេធ និងការសរសេរ។ |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | សម្របសម្រួលការអានឯកសារ notebook ការបកប្រែនុញ្ញាណច<Cell Markdown> ការកែផ្លូវ មេតាដារ ការបដិសេធ និងការសរសេរ។ |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | សម្របសម្រួលការស្វែងរករូបភាពដើម ការបកប្រែរូបភាព ផ្លូវចេញ លេខមេតា និងការសរសេរ។ |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | ស្វែងរកគូម៉ាឌុល Markdown ដែលបានបកប្រែ វាយតម្លៃគុណភាពការបកប្រែ និងអានមេតាដាតានៃការជឿជាក់សម្រាប់ប្រតិបត្តិការជួសជុលនៅពេលមានជឿជាក់ទាប។ |
| `ReviewRunner` | `co_op_translator.review.runner` | សម្របសម្រួលការត្រួតពិនិត្យប្រាកដនិយមលើឯកសារដើម ភាសាគោល និង root បកប្រែដែលបានកំណត់។ |
| `ReviewTarget` | `co_op_translator.review.targets` | វិពណ៌នាអំពី root ដើម និងថតលទ្ធផលបកប្រែដែលត្រូវបានពិនិត្យសម្រាប់ root នោះ។ |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | ស្វែងរកថតភាសាជា alias ចាស់ៗ ហើយរៀបចំផែនការផ្លាស់ទីទៅឈ្មោះថតភាសាតាម BCP 47 ដែលមានភាពស្តង់ដារ។ |
| `Config` | `co_op_translator.config.base_config` | ធ្វើការផ្ទុកឯកសារ `.env` និងពិនិត្យថាតើអ្នកផ្គត់ផ្គង់ LLM ដែលចាំបាច់ និង Vision ជាចម្ងល់ត្រូវបានកំណត់រួចរឺនៅទៅទេ។ |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | អនុញ្ញាតឲ្យចាប់ផ្ដើមស្វ័យប្រវត្តិរក Azure OpenAI ឬ OpenAI ផ្ទៀងផ្ទាត់អថេរបរិស្ថានដែលចាំបាច់ និងរត់ការត្រួតពិនិត្យការតភ្ជាប់អ្នកផ្គត់ផ្គង់។ |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | ស្វែងរកការកំណត់ Azure AI Vision និងរត់ការត្រួតពិនិត្យការតភ្ជាប់សម្រាប់ការបកប្រែរូបភាព។ |