# Python API

The stable public Python API is exported from `co_op_translator.api`. Most integrations use one of these workflows:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

Most lower-level modules under `core`, `config`, `review`, and `utils` are implementation details used by these API entry points.

MCP clients use the same public API through the [MCP serveris](mcp.md). Use this page when calling Python directly, and the MCP guide when exposing Co-op Translator to an agent or editor. If you are deciding between CLI, Python API, and MCP, start with [Pasirinkite savo darbo eigą](workflows.md).

## Pirmą kartą naudojant API

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

## Scenarijus 1: Išversti atskirus failus ar dokumentus

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

## Scenarijus 2: Išversti visą saugyklą

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

## Peržiūrėti išverstą turinį

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

## Kopijuoti-ir-įklijuoti API pavyzdžiai

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

## Vieši įėjimo taškai

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

## Turinio vertimo API

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

## Kelių perrašymo API

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

## Projekto vertimo parametrai

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

## Peržiūros parametrai

`run_review` intentionally mirrors the `run_translation` signature where possible so automation can switch between translation and review workflows with minimal branching.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | Vartotojo teksto vertimo išvesties katalogas. Santykiniai keliai interpretuojami pagal kiekvieną šaknį. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Kelios šaknys, kurios naudoja tas pačias išvesties nustatymus. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Aiškūs `(root_dir, translations_dir)` poros. Teikia pirmenybę prieš `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref, naudojamas peržiūrai apriboti tik pakeistiems šaltinio failams. |
| `output_format` | `str` | `"text"` | Peržiūros išvesties formatas. Palaikomos reikšmės yra `"text"` ir `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Įspėjimus traktuoti taip pat kaip klaidas. |
| `debug` | `bool` | `False` | Įjungti derinimo žurnalavimą. |
| `save_logs` | `bool` | `False` | Išsaugoti DEBUG lygio žurnalo failus šakniniame `logs/` kataloge. |

Jei nėra nustatyti `markdown`, `notebook` arba `images`, API peržiūri Markdown, užrašus ir vaizdų nuorodų nuorodas, kur tai taikoma. Peržiūra nekviečia LLM tiekėjo ir nereikalauja API raktų.

## Konfigūracijos reikalavimai

Paslaugų teikėjo palaikomos vertimo API reikalauja paslaugų teikėjo konfigūracijos prieš pradedant vertimą:

- Markdown ir užrašų vertimui reikalingas LLM tiekėjas. Sukonfigūruokite Azure OpenAI arba OpenAI.
- Vaizdų vertimui, be LLM tiekėjo, taip pat reikalinga Azure AI Vision.
- `run_translation` atlieka lengvus jungties patikrinimus prieš pradedant projekto vertimą.
- Agentų pagalba veikiantys API `start_*_agent_translation` ir `finish_*_agent_translation` nekviečia Co-op Translator LLM tiekėjų. Paruoštus fragmentus verčia šeimininko programa arba MCP agentas.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` ir `run_review` yra deterministiniai ir nereikalauja tiekėjo kredencialų.

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

`run_review` yra deterministinis ir nereikalauja Azure OpenAI, OpenAI ar Azure AI Vision konfigūracijos.

## Veikimo pastabos

- Turinio vertimo API atskiria vertimą nuo projekto kelių perrašymo. Jei išverstam turiniui reikia sureguliuoti projekto atžvilgiu santykines nuorodas pagal tikslinę vietą, aiškiai iškvieskite `rewrite_markdown_paths` arba `rewrite_notebook_paths`.
- Projekto orkestravimo API prideda projekto elgseną aplink turinio vertimą, įskaitant failų radimą, įrašymus, kelių perrašymą, metaduomenis, išvalymą ir pasirenkamus atsisakymus (disclaimers).
- `run_translation` spausdina pažangos ir įvertinimų santraukas per Click, atitinkančias CLI naudotojo patirtį.
- `dry_run=True` apskaičiuoja įvertinimus naudojant virtualius README atnaujinimus, bet neišrašo README arba vertimo failų.
- `groups` apdorojami iš eilės. Vienas suvestinis įvertinimas išspausdinamas prieš pradedant darbus.
- Jei pasirenkamas vaizdų vertimas, trūkstama Vision konfigūracija sukels klaidą prieš pradedant vertimą.
- Esami pagal alius sukurti kalbų katalogai aptinkami ir gali būti perkelti į kanoninius kalbų katalogų pavadinimus vykdymo metu.
- `run_review` nepavyksta, jei trūksta išverstų failų, trūksta arba yra pasenę vertimo metaduomenys, netaisyklingas Markdown frontmatter arba kodo tvoros (code fences), arba neteisingas išversto užrašo (notebook) JSON.
- `run_review` pagal numatytuosius nustatymus praneša apie trūkstamas vietines Markdown ir vaizdų nuorodų paskirties vietas kaip įspėjimus.

## Vidinis kvietimų kelias

API deleguoja tas pačias pagrindines įgyvendinimo dalis, kurias naudoja CLI:

Vertimas:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content` arba `translate_image_content` atmintyje atliekamam vertimui.
2. `co_op_translator.api.translation.rewrite_markdown_paths` arba `rewrite_notebook_paths` aiškiam kelių poapdorojimui.
3. `co_op_translator.api.translation.run_translation` pilnai projekto orkestracijai.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Peržiūra:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministiniai patikrinimai pagal `co_op_translator.review.checks`

Žemiau pateiktos klasės yra naudingos prižiūrintiems, bet jos nėra eksportuojamos kaip stabilus paketo lygio API.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinuoja projektinio lygio vertimą, katalogų valdymą, metaduomenų normalizavimą pagal kalbą ir deleguoja Markdown, užrašų (notebook) ir vaizdų vertėjams. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Atlieka asinchroninį failų apdorojimo darbą Markdown, užrašų, vaizdų, pasenusio turinio aptikimo ir vertimo metaduomenų atnaujinimams. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestruoja Markdown failų skaitymą, turinio vertimą, kelių perrašymą, metaduomenis, atsisakymus (disclaimers) ir įrašymus. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestruoja užrašų failų skaitymą, Markdown langelių vertimą, kelių perrašymą, metaduomenis, atsisakymus ir įrašymus. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestruoja šaltinio vaizdų paiešką, vaizdų vertimą, išvesties kelius, metaduomenis ir įrašymus. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Randa išverstus Markdown poras, įvertina vertimo kokybę ir skaito pasitikėjimo metaduomenis taisymo darbo eigoms, kai pasitikėjimas mažas. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinuoja deterministinius peržiūros patikrinimus per šaltinio failus, tikslines kalbas ir sukonfigūruotas vertimo šaknis. |
| `ReviewTarget` | `co_op_translator.review.targets` | Aprašo šaltinio šaknį ir tos šaknies peržiūrai skirtą vertimo išvesties katalogą. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Aptinka paveldėtas aliastų kalbų aplankus ir paruošia kanoninių BCP 47 aplankų migracijos planus. |
| `Config` | `co_op_translator.config.base_config` | Įkelia `.env` failus ir tikrina, ar reikalingi LLM ir pasirenkami Vision tiekėjai sukonfigūruoti. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Automatiškai aptinka Azure OpenAI arba OpenAI, tikrina reikiamus aplinkos kintamuosius ir atlieka tiekėjo jungtumo patikrinimus. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Nustato Azure AI Vision konfigūraciją ir atlieka jungties patikrinimus vaizdų vertimui. |