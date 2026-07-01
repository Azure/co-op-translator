# Python API

Den stabile offentlige Python-API eksporteres fra `co_op_translator.api`. De fleste integrationer bruger en af disse arbejdsgange:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

De fleste lavere niveau-moduler under `core`, `config`, `review`, og `utils` er implementationsdetaljer, der bruges af disse API-indgangspunkter.

MCP clients bruger den samme offentlige API gennem [MCP Server](mcp.md). Brug denne side når du kalder Python direkte, og MCP-guiden når du eksponerer Co-op Translator for en agent eller editor. Hvis du skal vælge mellem CLI, Python API og MCP, start med [Choose Your Workflow](workflows.md).

## First-Time API Flow

Start her hvis du kalder Co-op Translator fra Python-kode:

1. Konfigurer en LLM-udbyder som beskrevet i [Configuration](configuration.md), medmindre du kun forbereder Markdown eller notebook-udsnit til host-agent-oversættelse.
2. Beslut om din applikation skal håndtere fil-I/O.
3. Brug indholds-API'erne når din applikation læser og skriver individuelle filer.
4. Brug `run_translation` når Co-op Translator skal behandle et repository som CLI'en.
5. Brug `run_review` efter oversættelse hvis du har brug for deterministiske checks i automatisering.

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

Brug denne arbejdsgang når du allerede har en fil, editor-buffer, notebook-payload, MCP-anmodning eller brugerdefineret pipeline-input. Din kode ejer fil-I/O:

1. Læs kildeindholdet.
2. Kald en indholds-oversættelses-API.
3. Valgfrit: kald en sti-omskrivnings-API hvis det oversatte indhold skal skrives ind i en projektoversættelsesmappe.
4. Gem eller returner resultatet fra din applikation.

Indholdsoversættelses-API'erne kører ikke projektopdagelse, skriver ikke metadata, indsætter ikke disclaimers og omskriver ikke links automatisk.

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

Hvis den oversatte Markdown ikke skal leve i et Co-op Translator projektlayout, spring `rewrite_markdown_paths` over og gem den oversatte streng direkte.

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

`translate_notebook_content` oversætter Markdown-celler og bevarer ikke-Markdown-celler. Sti-omskrivning anvendes kun på Markdown-celler.

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

`translate_image_content` læser kildebilledet og returnerer et renderet `PIL.Image.Image`. Det skriver ikke oversat billedmetadata.

## Scenario 2: Translate an Entire Repository

Brug denne arbejdsgang når du vil have Python API'en til at opføre sig som `translate` CLI'en. `run_translation` opdager understøttede filer, oversætter valgte indholdstyper, omskriver stier, skriver outputfiler, opdaterer metadata og udfører vedligeholdelsesopgaver i forbindelse med oversættelse som f.eks. oprydning.

`run_translation` er det foretrukne orkestreringsindgangspunkt for projekter. `translate_project` eksporteres som et kompatibilitetsalias med samme opførsel.

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

`run_review` udfører deterministiske oversættelsestjek uden LLM- eller Vision-legitimationsoplysninger.

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

Indholdsoversættelses-API'erne er beregnet til integrationer, der allerede har indhold i hukommelsen, såsom en editor-udvidelse, MCP-værktøj, notebook-processor eller brugerdefineret pipeline.

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

Agent-assisterede API'er kalder ikke Azure OpenAI eller OpenAI fra Co-op Translator. De forbereder Markdown- eller notebook-udsnit til en host-agent, som oversætter, og derefter rekonstruerer Co-op Translator det endelige indhold fra de oversatte udsnit.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return a self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from a job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return a notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while preserving code cells, outputs, and metadata. |

Denne arbejdsgang er primært beregnet til MCP-hosts. Hvis du har brug for produktionsoversættelse af repositories med Co-op Translator, der håndterer provider-kald, brug `translate_markdown_content`, `translate_notebook_content` eller `run_translation`.

## Path Rewriting APIs

Sti-omskrivnings-API'er udfører ingen oversættelse. De opdaterer links og frontmatter-stier efter at kaldende kode kender kildebanen, den oversatte målsti og projektlayoutet.

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
| `language_codes` | `str` | Påkrævet | Space-separated target language codes, such as `"ko ja fr"`, or `"all"`. Alias codes are normalized to canonical BCP 47 values. |
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

`run_review` is bevidst designet til at spejle `run_translation`-signaturen hvor muligt, så automatisering kan skifte mellem oversættelses- og gennemgangsarbejdsgange med minimal branching.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | Brugerdefineret outputmappe for tekstoversættelser. Relative stier fortolkes i forhold til hver rod. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Flere rødder, der deler de samme outputindstillinger. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Eksplicitte `(root_dir, translations_dir)`-par. Har forrang frem for `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-ref, der bruges til at begrænse gennemgangen til ændrede kildefiler. |
| `output_format` | `str` | `"text"` | Outputformat for review. Understøttede værdier er `"text"` og `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Behandle advarsler som fejl ud over almindelige fejl. |
| `debug` | `bool` | `False` | Aktivér debug-logging. |
| `save_logs` | `bool` | `False` | Gem logfiler på DEBUG-niveau under rodmappen `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Konfigurationskrav

Oversættelses-API'er, som er afhængige af en udbyder, kræver konfiguration af udbyderen før oversættelse:

- Markdown- og notebook-oversættelse kræver en LLM-udbyder. Konfigurer enten Azure OpenAI eller OpenAI.
- Billedoversættelse kræver Azure AI Vision ud over LLM-udbyderen.
- `run_translation` kører lette forbindelsestjek, før projektoversættelsen begynder.
- Agent-assisterede `start_*_agent_translation` og `finish_*_agent_translation` API'er kalder ikke Co-op Translator LLM-udbydere. Host-applikationen eller MCP-agenten oversætter de forberedte chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` og `run_review` er deterministiske og kræver ikke udbyder-legitimationsoplysninger.

Påkrævede Azure OpenAI-variabler:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Påkrævede OpenAI-variabler:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Påkrævede Azure AI Vision-variabler for billedoversættelse:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` er deterministisk og kræver ikke Azure OpenAI-, OpenAI- eller Azure AI Vision-konfiguration.

## Bemærkninger om adfærd

- Indholdsoversættelses-API'er holder oversættelsen adskilt fra omskrivning af projektstier. Kald eksplicit `rewrite_markdown_paths` eller `rewrite_notebook_paths`, når oversat indhold kræver, at projektrelaterede links justeres for en målplacering.
- Projekt-orkestrerings-API'er tilføjer projektadfærd omkring indholdsoversættelse, inklusive filopdagelse, skrivning, stiomskrivning, metadata, oprydning og valgfrie ansvarsfraskrivelser.
- `run_translation` udskriver status og estimatsummer via Click, hvilket svarer til CLI-brugeroplevelsen.
- `dry_run=True` beregner estimater ved hjælp af virtuelle README-opdateringer, men skriver ikke README'en eller oversættelsesfilerne.
- `groups` behandles sekventielt. Et samlet estimat udskrives, før arbejdet begynder.
- Når billedoversættelse er valgt, udløser manglende Vision-konfiguration en fejl, før oversættelsen starter.
- Eksisterende alias-baserede sprogmapper opdages og kan migreres til kanoniske sprogmappe-navne som en del af kørslen.
- `run_review` fejler ved manglende oversatte filer, manglende eller forældet oversættelsesmetadata, forkert formateret Markdown-frontmatter/code fences og ugyldig oversat notebook-JSON.
- `run_review` rapporterer manglende lokale Markdown- og billedelinkmål som advarsler som standard.

## Intern kaldsti

API'en delegerer til den samme kerneimplementering, som CLI'en bruger:

Oversættelse:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Fokuserede projektoversættelses-mixins til Markdown, notebooks og billeder.
8. Markdown-, notebook-, tekst- og billedoversættere under `co_op_translator.core`.

Gennemgang:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministiske kontroller under `co_op_translator.review.checks`

Følgende klasser er nyttige for vedligeholdere, men eksporteres ikke som den stabile pakke-API.

| Klasse | Modul | Ansvar |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinerer projektniveau-oversættelse, kataloghåndtering, normalisering af metadata per sprog, og delegering til Markdown-, notebook- og billedoversættere. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Udfører det asynkrone filbehandlingsarbejde for Markdown, notebooks, billeder, detektion af forældede filer og opdateringer af oversættelsesmetadata. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestrerer læsning af Markdown-filer, indholdsoversættelse, stiomskrivning, metadata, ansvarsfraskrivelser og skrivning. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestrerer læsning af notebook-filer, oversættelse af Markdown-celler, stiomskrivning, metadata, ansvarsfraskrivelser og skrivning. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestrerer opdagelse af kildebilleder, billedoversættelse, outputstier, metadata og skrivning. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Finder oversatte Markdown-par, vurderer oversættelseskvalitet og læser konfidencemetadata til workflows for reparation ved lav konfidens. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinerer deterministiske review-kontroller på tværs af kildefiler, målsprog og konfigurerede oversættelsesrødder. |
| `ReviewTarget` | `co_op_translator.review.targets` | Beskriver en kilderod og den oversættelses-outputmappe, der gennemgås for den rod. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Finder ældre alias-baserede sprogmapper og forbereder migrationsplaner til kanoniske BCP 47-mappenavne. |
| `Config` | `co_op_translator.config.base_config` | Indlæser `.env`-filer og tjekker om krævede LLM- og valgfrie Vision-udbydere er konfigureret. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Auto-opdager Azure OpenAI eller OpenAI, validerer krævede miljøvariabler og kører forbindelsestjek for udbydere. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Registrerer Azure AI Vision-konfiguration og kører forbindelsestjek for billedoversættelse. |