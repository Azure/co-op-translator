# Python-API

Den stabila publika Python-API:n exporteras från `co_op_translator.api`. De flesta integrationer använder ett av dessa arbetsflöden:

| Scenario | Använd när | Huvudsakliga API:er |
| --- | --- | --- |
| Translate individual files or documents | Din applikation läser källinnehållet, anropar Co-op Translator för översättning, och bestämmer var resultatet ska sparas. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Din MCP-värd eller applikationsmodell kommer att översätta bitar, medan Co-op Translator hanterar uppdelning och återuppbyggnad. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Du vill att Python-API:t ska bete sig som CLI:n och hantera upptäckt, utdata-sökvägar, metadata, städning och skrivningar. | `run_translation` |

De flesta lågnivåmoduler under `core`, `config`, `review` och `utils` är implementationdetaljer som används av dessa API-ingångspunkter.

MCP-klienter använder samma publika API via [MCP Server](mcp.md). Använd den här sidan när du anropar Python direkt, och MCP-guiden när du exponerar Co-op Translator för en agent eller en editor. Om du väljer mellan CLI, Python-API och MCP, börja med [Choose Your Workflow](workflows.md).

## Förstagångsflöde för API

Börja här om du anropar Co-op Translator från Python-kod:

1. Konfigurera en LLM-leverantör enligt [Configuration](configuration.md), om du inte bara förbereder Markdown- eller notebook-bitar för host-agent-översättning.
2. Bestäm om din applikation ansvarar för fil-I/O.
3. Använd innehålls-API:er när din applikation läser och skriver enstaka filer.
4. Använd `run_translation` när Co-op Translator ska bearbeta ett repository som CLI:n.
5. Använd `run_review` efter översättning om du behöver deterministiska kontroller i automation.

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

Använd det här arbetsflödet när du redan har en fil, editorbuffert, notebook-payload, MCP-förfrågan eller egen pipeline-input. Din kod ansvarar för fil-I/O:

1. Läs källinnehållet.
2. Anropa ett innehållsöversättnings-API.
3. Valfritt: anropa ett sökvägs-omskrivnings-API om det översatta innehållet ska skrivas i en projektöversättningsmapp.
4. Spara eller returnera resultatet från din applikation.

Innehållsöversättnings-API:erna kör inte projektupptäckt, skriver inte metadata, lägger inte till disclaimers och skriver inte om länkar automatiskt.

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

Om den översatta Markdown inte ska ligga i ett Co-op Translator-projekt, hoppa över `rewrite_markdown_paths` och spara den översatta strängen direkt.

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

`translate_notebook_content` översätter Markdown-celler och bevarar icke-Markdown-celler. Sökvägsomskrivning tillämpas endast på Markdown-celler.

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

`translate_image_content` läser källbilden och returnerar en renderad `PIL.Image.Image`. Den skriver inte översatt bildmetadata.

## Scenario 2: Translate an Entire Repository

Använd det här arbetsflödet när du vill att Python-API:t ska bete sig som `translate` CLI:n. `run_translation` upptäcker stödjade filer, översätter valda innehållstyper, skriver om sökvägar, skriver utdatafiler, uppdaterar metadata och utför underhållsuppgifter som städning.

`run_translation` är den föredragna ingångspunkten för projektorkestrering. `translate_project` exporteras som en kompatibilitetsalias med samma beteende.

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

`run_review` kör deterministiska översättningskontroller utan LLM- eller Vision-behörigheter.

!!! note "Beta"
    `run_review` är ett beta-deterministiskt gransknings-API. Det anropar inte modellleverantörer eller skriver filer, men kontroll- och issu-scheman kan förändras.

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

Innehållsöversättnings-API:er är avsedda för integrationer som redan har innehåll i minnet, såsom en editor-tillägg, MCP-verktyg, notebook-processor eller egen pipeline.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Översätter endast Markdown-innehåll. Den skriver inte om länkar, sparar metadata eller lägger till disclaimers. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Översätter Markdown-celler och bevarar icke-Markdown-celler. Den skriver inte om länkar, sparar metadata eller lägger till disclaimers. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Extraherar och översätter bildtext, och returnerar sedan en renderad bild. Den sparar inte översatt bildmetadata. |

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

Agent-assisterade API:er anropar inte Azure OpenAI eller OpenAI från Co-op Translator. De förbereder Markdown- eller notebook-bitar för att en värdagent ska översätta, och rekonstruerar sedan det slutgiltiga innehållet från de översatta bitarna.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Returnerar ett fristående Markdown-jobb med bitar, prompts och återuppbyggnadsstatus. |
| `finish_markdown_agent_translation` | Återuppbygger Markdown från ett jobb och värdagentens översatta bitar. |
| `start_notebook_agent_translation` | Returnerar ett notebook-jobb med Markdown-cellbitar för värdagent-översättning. |
| `finish_notebook_agent_translation` | Återuppbygger notebook JSON samtidigt som kodceller, outputs och metadata bevaras. |

Detta arbetsflöde är främst avsett för MCP-värdar. Om du behöver produktionsöversättning av repositories med Co-op Translator som hanterar anrop till leverantörer, använd `translate_markdown_content`, `translate_notebook_content` eller `run_translation`.

## Path Rewriting APIs

Sökvägsomskrivnings-API:er utför ingen översättning. De uppdaterar länkar och frontmatter-sökvägar efter att anropare känner till källvägen, den översatta målvägen och projektlayouten.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Skriver om Markdown-länkar och stödda frontmatter-fält för en översatt mål. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Tillämpa Markdown-sökvägsomskrivning på varje Markdown-cell och lämnar icke-Markdown-celler oförändrade. |

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

`run_review` avsiktligt speglar `run_translation`-signaturen där det är möjligt så att automation kan växla mellan översättnings- och granskningsarbetsflöden med minimala skillnader.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | Anpassad katalog för textöversättningsutdata. Relativa sökvägar tolkas i förhållande till respektive rot. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Flera rotkataloger som delar samma utdatainställningar. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit angivna `(root_dir, translations_dir)`-par. Har företräde framför `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-ref som används för att begränsa granskningen till ändrade källfiler. |
| `output_format` | `str` | `"text"` | Granskningsutdataformat. Stödda värden är "text" och "github". |
| `fail_on_warnings` | `bool` | `False` | Behandla varningar som fel i tillägg till befintliga fel. |
| `debug` | `bool` | `False` | Aktivera debug-loggning. |
| `save_logs` | `bool` | `False` | Spara loggfiler på DEBUG-nivå i rotkatalogen `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Konfigurationskrav

Översättnings-API:er som stöds av leverantörer kräver leverantörskonfiguration innan översättning:

- Markdown and notebook translation require an LLM provider. Configure either Azure OpenAI or OpenAI.
- Image translation requires Azure AI Vision in addition to the LLM provider.
- `run_translation` runs lightweight connectivity checks before project translation begins.
- Agent-assisted `start_*_agent_translation` and `finish_*_agent_translation` APIs do not call Co-op Translator LLM providers. The host application or MCP agent translates the prepared chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` are deterministic and do not require provider credentials.

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

`run_review` is deterministic and does not require Azure OpenAI, OpenAI, or Azure AI Vision configuration.

## Beteendeanteckningar

- Content translation APIs keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content needs project-relative links adjusted for a target location.
- Project orchestration APIs add project behavior around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` prints progress and estimate summaries through Click, matching the CLI user experience.
- `dry_run=True` computes estimates using virtual README updates, but does not write the README or translation files.
- `groups` are processed sequentially. A single aggregate estimate is printed before work begins.
- When image translation is selected, missing Vision configuration raises an error before translation starts.
- Existing alias-based language folders are detected and can be migrated to canonical language folder names as part of the run.
- `run_review` fails on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` reports missing local Markdown and image link targets as warnings by default.

## Intern anropsväg

The API delegates to the same core implementation used by the CLI:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig` och `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Klass | Modul | Ansvar |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinerar projektnivåöversättning, kataloghantering, normalisering av metadata per språk och delegering till Markdown-, notebook- och bildöversättare. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Utför det asynkrona filbearbetningsarbetet för Markdown, notebooks, bilder, upptäckt av föråldrade filer och uppdateringar av översättningsmetadata. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestrerar läsning av Markdown-filer, innehållsöversättning, sökvägsomskrivning, metadata, ansvarsfriskrivningar och skrivningar. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestrerar läsning av notebook-filer, översättning av Markdown-celler, sökvägsomskrivning, metadata, ansvarsfriskrivningar och skrivningar. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestrerar upptäckt av källbilder, bildöversättning, utdata-sökvägar, metadata och skrivningar. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Hittar översatta Markdown-par, utvärderar översättningskvalitet och läser konfidensmetadata för arbetsflöden för reparation vid låg konfidens. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinerar deterministiska granskningskontroller över källfiler, målspråk och konfigurerade översättningsrötter. |
| `ReviewTarget` | `co_op_translator.review.targets` | Beskriver en källrot och den översättningsutdata-katalog som granskas för den roten. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Upptäcker äldre alias-språkmappar och förbereder kanoniska BCP 47-mappmigrationsplaner. |
| `Config` | `co_op_translator.config.base_config` | Läser in `.env`-filer och kontrollerar om nödvändiga LLM- och valfria Vision-leverantörer är konfigurerade. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Autodetekterar Azure OpenAI eller OpenAI, validerar nödvändiga miljövariabler och kör anslutningskontroller mot leverantören. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Upptäcker Azure AI Vision-konfiguration och kör anslutningskontroller för bildöversättning. |