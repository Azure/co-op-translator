# Python API

Den stabile offentlige Python-API-en eksporteres fra `co_op_translator.api`. De fleste integrasjoner bruker ett av disse arbeidsflytene:

| Scenario | Bruk dette når | Hoved-API-er |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

De fleste lavnivåmodulene under `core`, `config`, `review`, og `utils` er implementasjonsdetaljer som brukes av disse API-inngangspunktene.

MCP-klienter bruker samme offentlige API gjennom [MCP Server](mcp.md). Bruk denne siden når du kaller Python direkte, og MCP-guiden når du eksponerer Co-op Translator til en agent eller editor. Hvis du skal velge mellom CLI, Python API og MCP, start med [Choose Your Workflow](workflows.md).

## First-Time API Flow

Start her hvis du kaller Co-op Translator fra Python-kode:

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
| `translations_dir` | `str \| None` | `None` | Egendefinert utdata-katalog for tekstoversettelser. Relative stier løses i forhold til hver rot. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Flere rotkataloger som deler de samme utdatainnstillingene. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Eksplisitte `(root_dir, translations_dir)`-par. Har forrang foran `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-ref som brukes for å begrense gjennomgangen til endrede kildefiler. |
| `output_format` | `str` | `"text"` | Utdataformat for gjennomgang. Støttede verdier er `"text"` og `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Behandle advarsler som feil i tillegg til eksisterende feil. |
| `debug` | `bool` | `False` | Aktiver debug-loggføring. |
| `save_logs` | `bool` | `False` | Lagre loggfiler på DEBUG-nivå under rotmappen `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Konfigurasjonskrav

- Oversettelses-APIer som bruker leverandører krever leverandørkonfigurasjon før oversettelse:
- Markdown- og notebook-oversettelse krever en LLM-leverandør. Konfigurer enten Azure OpenAI eller OpenAI.
- Bildoversettelse krever Azure AI Vision i tillegg til LLM-leverandøren.
- `run_translation` kjører lette tilkoblingssjekker før prosjektoversettelsen starter.
- Agent-assisterte `start_*_agent_translation`- og `finish_*_agent_translation`-APIer kaller ikke Co-op Translator LLM-leverandører. Vertsapplikasjonen eller MCP-agenten oversetter de forberedte delene.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` er deterministiske og krever ikke leverandørlegitimasjon.

Påkrevde Azure OpenAI-variabler:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Påkrevde OpenAI-variabler:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Påkrevde Azure AI Vision-variabler for bildoversettelse:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` er deterministisk og krever ikke Azure OpenAI-, OpenAI- eller Azure AI Vision-konfigurasjon.

## Merknader om oppførsel

- Innholdsoversettelses-APIene holder oversettelse adskilt fra prosjekt-sti-omskriving. Kall `rewrite_markdown_paths` eller `rewrite_notebook_paths` eksplisitt når oversatt innhold trenger justerte prosjektrelative lenker for et målsted.
- Prosjekt-orkestrerings-APIene legger til prosjektatferd rundt innholdsoversettelse, inkludert filoppdagelse, skrivinger, sti-omskriving, metadata, opprydding og valgfri ansvarsfraskrivelse.
- `run_translation` skriver ut fremdrift og estimatsammendrag gjennom Click, og matcher CLI-brukeropplevelsen.
- `dry_run=True` beregner estimater ved hjelp av virtuelle README-oppdateringer, men skriver ikke README eller oversettelsesfiler.
- `groups` behandles sekvensielt. Et enkelt aggregerende estimat skrives ut før arbeidet begynner.
- Når bildoversettelse er valgt, vil manglende Vision-konfigurasjon kaste en feil før oversettelsen starter.
- Eksisterende alias-baserte språkmapper oppdages og kan migreres til kanoniske språkmappe-navn som en del av kjøringen.
- `run_review` feiler ved manglende oversatte filer, manglende eller utdaterte oversettelsesmetadata, feilformatert Markdown-frontmatter/code fences, og ugyldig oversatt notebook-JSON.
- `run_review` rapporterer manglende lokale Markdown- og bildekoblingsmål som advarsler som standard.

## Intern kallvei

API-en delegerer til samme kjerneimplementasjon som brukes av CLI-en:

Oversettelse:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for oversettelse i minnet.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for eksplisitt etterbehandling av stier.
3. `co_op_translator.api.translation.run_translation` for full prosjektorkestrering.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Fokuserte prosjektoversettelses-mixins for Markdown, notatbøker og bilder.
8. Markdown-, notebook-, tekst- og bildetranslatorer under `co_op_translator.core`.

Gjennomgang:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministiske sjekker under `co_op_translator.review.checks`

Følgende klasser er nyttige for vedlikeholdere, men eksporteres ikke som den pakkesnivå stabile API-en.

| Klasse | Modul | Ansvar |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinerer prosjektnivå oversettelse, kataloghåndtering, normalisering av metadata per språk, og delegering til Markdown-, notatbok- og bildetranslatorer. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Utfører det asynkrone filbehandlingsarbeidet for Markdown, notatbøker, bilder, oppdagelse av foreldede filer, og oppdateringer av oversettelsesmetadata. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestrerer lesing av Markdown-filer, innholdsoversettelse, sti-omskriving, metadata, ansvarsfraskrivelser, og skriving. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestrerer lesing av notebook-filer, oversettelse av Markdown-celler, sti-omskriving, metadata, ansvarsfraskrivelser, og skriving. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestrerer oppdagelse av kildebilder, bildoversettelse, utdata-stier, metadata, og skriving. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Finner oversatte Markdown-par, evaluerer oversettelseskvalitet, og leser konfidensmetadata for reparasjonsarbeidsflyter ved lav tillit. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinerer deterministiske gjennomgangssjekker på tvers av kildefiler, målspråk, og konfigurerte oversettelsesrotkataloger. |
| `ReviewTarget` | `co_op_translator.review.targets` | Beskriver en kilderot og oversettelsesutdata-katalogen som gjennomgås for den kilderoten. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Oppdager eldre alias-språkmapper og forbereder migrasjonsplaner til kanoniske BCP 47-mappenavn. |
| `Config` | `co_op_translator.config.base_config` | Laster `.env`-filer og sjekker om påkrevde LLM- og valgfrie Vision-leverandører er konfigurert. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Oppdager automatisk Azure OpenAI eller OpenAI, validerer påkrevde miljøvariabler, og kjører tilkoblingssjekker mot leverandøren. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Oppdager Azure AI Vision-konfigurasjon og kjører tilkoblingssjekker for bildoversettelse. |