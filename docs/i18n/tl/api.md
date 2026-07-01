# Python API

Ang matatag na pampublikong Python API ay ine-export mula sa `co_op_translator.api`. Karamihan sa mga integrasyon ay gumagamit ng isa sa mga workflow na ito:

| Senaryo | Gamitin ito kapag | Pangunahing API |
| --- | --- | --- |
| Isalin ang indibidwal na mga file o dokumento | Binabasa ng iyong aplikasyon ang pinagmulan ng nilalaman, tinatawagan ang Co-op Translator para sa pagsasalin, at nagpapasya kung saan ise-save ang resulta. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Ihanda ang nilalaman para sa host-agent na pagsasalin | Ang iyong MCP host o modelo ng aplikasyon ang magsasalin ng mga bahagi (chunks), habang ang Co-op Translator ang humahawak ng paghahati-hati at muling pagsasama. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Isalin ang buong repositoryo | Nais mo na kumilos ang Python API tulad ng CLI at hawakan ang pagdiskubre, mga landas ng output, metadata, paglilinis, at pagsusulat. | `run_translation` |

Karamihan sa mga lower-level module sa ilalim ng `core`, `config`, `review`, at `utils` ay mga detalye ng implementasyon na ginagamit ng mga entry point ng API na ito.

Gumagamit ang mga kliyenteng MCP ng parehong pampublikong API sa pamamagitan ng [MCP Server](mcp.md). Gamitin ang pahinang ito kapag tumatawag ka ng Python nang direkta, at ang patnubay ng MCP kapag inilalantad ang Co-op Translator sa isang agent o editor. Kung nagpapasya ka sa pagitan ng CLI, Python API, at MCP, magsimula sa [Choose Your Workflow](workflows.md).

## Unang Daloy ng API

Magsimula rito kung tatawag ka sa Co-op Translator mula sa Python na code:

1. I-configure ang isang LLM provider gaya ng inilalarawan sa [Configuration](configuration.md), maliban kung naghahanda ka lamang ng mga Markdown o notebook chunks para sa host-agent na pagsasalin.
2. Tukuyin kung ang iyong aplikasyon ang humahawak ng file I/O.
3. Gamitin ang mga content API kapag binabasa at sinusulat ng iyong aplikasyon ang mga indibidwal na file.
4. Gamitin ang `run_translation` kapag dapat iproseso ng Co-op Translator ang isang repositoryo tulad ng CLI.
5. Gamitin ang `run_review` pagkatapos ng pagsasalin kung kailangan mo ng deterministic na mga tseke sa automation.

| Layunin | API na sisimulan |
| --- | --- |
| Isalin ang isang Markdown string o file | `translate_markdown_content` |
| Isalin ang isang notebook payload | `translate_notebook_content` |
| Isalin ang isang imahe | `translate_image_content` |
| Hayaan ang host agent na magsalin ng mga Markdown o notebook na chunks | `start_markdown_agent_translation` o `start_notebook_agent_translation` |
| I-rewrite ang mga naisaling link pagkatapos pumili ng output path | `rewrite_markdown_paths` o `rewrite_notebook_paths` |
| Isalin ang buong repositoryo | `run_translation` |
| Suriin ang naisaling output | `run_review` |

## Senaryo 1: Isalin ang Indibidwal na Mga File o Dokumento

Gamitin ang workflow na ito kapag mayroon ka nang file, editor buffer, notebook payload, MCP request, o custom pipeline input. Ang iyong code ang humahawak ng file I/O:

1. Basahin ang source na nilalaman.
2. Tawagan ang isang content translation API.
3. Opsyonal na tawagan ang isang path rewriting API kung ang naisaling nilalaman ay isusulat sa isang project translation folder.
4. I-save o ibalik ang resulta mula sa iyong aplikasyon.

Ang mga content translation API ay hindi nagpapatakbo ng project discovery, hindi sumusulat ng metadata, hindi nag-a-append ng mga disclaimer, at hindi awtomatikong ni-rererewrite ang mga link.

### File ng Markdown

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

Kung ang naisaling Markdown ay hindi ilalagay sa layout ng proyekto ng Co-op Translator, laktawan ang `rewrite_markdown_paths` at i-save nang direkta ang naisaling string.

### File ng Notebook

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

`translate_notebook_content` ay isinasalin ang mga Markdown cell at pinapanatili ang mga non-Markdown na cell. Ang pag-rewrite ng path ay inilalapat lamang sa mga Markdown cell.

### File ng Imahe

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

`translate_image_content` binabasa ang source na imahe at nagbabalik ng isang rendered na `PIL.Image.Image`. Hindi nito sinusulat ang translated image metadata.

## Senaryo 2: Isalin ang Buong Repositoryo

Gamitin ang workflow na ito kapag gusto mong kumilos ang Python API tulad ng `translate` CLI. Ang `run_translation` ay naghahanap ng mga suportadong file, isinasalin ang napiling mga uri ng nilalaman, nirerewrite ang mga path, sumusulat ng output files, ina-update ang metadata, at nagsasagawa ng mga maintenance na gawain sa pagsasalin tulad ng paglilinis.

Ang `run_translation` ang inirerekomendang entry point para sa orchestration ng proyekto. Ang `translate_project` ay ine-export bilang compatibility alias na may parehong pag-uugali.

Isalin ang mga Markdown file sa kasalukuyang repositoryo sa Korean at Japanese:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Isalin lamang ang mga notebook mula sa isang partikular na project root:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

I-preview ang dami ng pagsasalin nang hindi nagsusulat ng mga file:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Isalin ang maramihang content roots sa isang tawag:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Isulat ang mga pagsasalin sa mga explicit na output group:

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

Gumamit ng per-language placeholder kapag ang bawat wika ay dapat magkaroon ng nested na subdirectory:

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

Kung wala sa `markdown`, `notebook`, o `images` ang naka-set, isinasalin ng API ang lahat ng suportadong uri: Markdown, notebooks, at images.

## Suriin ang Naisaling Output

`run_review` ay nagpapatakbo ng deterministic na mga tseke sa pagsasalin nang walang LLM o Vision credentials.

!!! note "Beta"
    `run_review` ay isang beta deterministic review API. Hindi ito tumatawag ng mga model provider o nagsusulat ng mga file, ngunit maaaring magbago ang mga tseke at mga schema ng isyu.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Suriin lamang ang mga file na nagbago kumpara sa isang base ref at i-print ang GitHub-flavored output:

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

## Mga Halimbawa ng Copy-Paste na API

Isalin ang Markdown content nang walang file writes:

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

Isalin at i-rewrite ang mga Markdown link:

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

Isalin ang isang repositoryo mula sa Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Isalin ang maramihang root:

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

Panatilihin ang mga term mula sa glossary:

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

## Mga Pampublikong Entry Point

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

## Mga API para sa Pagsasalin ng Nilalaman

Ang mga content translation API ay inilaan para sa mga integrasyon na mayroon nang nilalaman sa memorya, tulad ng isang editor extension, MCP tool, notebook processor, o custom pipeline.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Isinasalin lamang ang Markdown content. Hindi nito ni-rerewrite ang mga link, sumusulat ng metadata, o nag-a-append ng mga disclaimer. |
| `translate_notebook_content` | Notebook JSON `str` o `dict` | Notebook JSON `str` | No | Async. Isinasalin ang mga Markdown cell at pinapanatili ang mga non-Markdown na cell. Hindi nito ni-rerewrite ang mga link, sumusulat ng metadata, o nag-a-append ng mga disclaimer. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Kinukuha at isinasalin ang teksto sa imahe, pagkatapos ay nagbabalik ng isang rendered na imahe. Hindi nito sine-save ang translated image metadata. |

Tumatanggap ang `translate_markdown_content` at `translate_notebook_content` ng opsyonal na `source_path` sa pamamagitan ng kanilang options. Ang path ay ipinapasa bilang konteksto sa translator; nananatiling responsable ang tumatawag para sa anumang project-specific na path rewriting pagkatapos ng pagsasalin.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Ang parehong mga option ay maaaring ipasa bilang mga dictionary:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Mga API na Tinutulungan ng Agent para sa Pagsasalin

Ang mga agent-assisted API ay hindi tumatawag sa Azure OpenAI o OpenAI mula sa Co-op Translator. Inihahanda nila ang mga Markdown o notebook chunks para isalin ng host agent, at pagkatapos ay muling binubuo ang panghuling nilalaman mula sa mga naisaling chunk.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Ibalik ang isang self-contained na Markdown job na may mga chunk, prompts, at reconstruction state. |
| `finish_markdown_agent_translation` | Muling buuin ang Markdown mula sa isang job at sa mga naisaling chunk ng host-agent. |
| `start_notebook_agent_translation` | Ibalik ang isang notebook job na may mga Markdown-cell chunks para sa pagsasalin ng host-agent. |
| `finish_notebook_agent_translation` | Muling buuin ang notebook JSON habang pinapanatili ang mga code cell, outputs, at metadata. |

Ang workflow na ito ay pangunahing inilaan para sa mga MCP host. Kung kailangan mo ng production repository translation na pinangangasiwaan ng Co-op Translator ang mga provider call, gamitin ang `translate_markdown_content`, `translate_notebook_content`, o `run_translation`.

## Mga API ng Pag-rewrite ng Path

Ang mga path rewriting API ay hindi nagsasagawa ng pagsasalin. Ina-update nila ang mga link at mga frontmatter path pagkatapos malaman ng tumatawag ang source path, naisaling target path, at layout ng proyekto.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Nirerewrite ang mga Markdown link at sinusuportahang frontmatter path fields para sa isang naisaling target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Inilalapat ang Markdown path rewriting sa bawat Markdown cell at iniiiwan ang mga non-Markdown na cell na hindi nagagalaw. |

Ang argumentong `policy` ay maaaring isang dictionary na may mga sumusunod na field:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, tulad ng `"ko"` o `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | No | Enabled translation types. Defaults to Markdown, notebooks, and images. |
| `lang_subdir` | No | Optional subdirectory under each language folder. |

## Mga Parameter ng Project Translation

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

## Mga Parameter ng Review

Nilalayong i-mirror ng `run_review` ang signature ng `run_translation` kung maaari para ang automation ay makalipat sa pagitan ng translation at review workflows nang may minimal na branching.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Tinanggap ang space-separated strings at iterables. `"all"` ay sumusuri sa bawat natuklasang translation language. |
| `root_dir` | `str` | `"."` | Project root para sa isang review target. Hindi pinapansin kapag may `root_dirs` o `groups` na ibinigay. |
| `markdown` | `bool` | `False` | Isama ang Markdown at MDX source files. |
| `notebook` | `bool` | `False` | Isama ang Jupyter notebook source files. |
| `images` | `bool` | `False` | Nakalaan para sa parity sa translation options. Sinusuri ang link references sa mga imahe mula sa Markdown. |
| `translations_dir` | `str \| None` | `None` | Pasadyang direktoryo ng output para sa pagsasalin ng teksto. Ang mga relatibong path ay nireresolba laban sa bawat root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Maramihang root na nagbabahagi ng parehong mga setting ng output. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Eksplisit na mga pares (root_dir, translations_dir). Mas inuuna ito kaysa sa `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref na ginagamit upang limitahan ang review sa mga nabagong source file. |
| `output_format` | `str` | `"text"` | Format ng output ng review. Sinusuportahan ang mga halaga na `"text"` at `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Ituring ang mga babala bilang pagkabigo pati na rin sa mga error. |
| `debug` | `bool` | `False` | Paganahin ang debug logging. |
| `save_logs` | `bool` | `False` | I-save ang mga DEBUG-level na log file sa ilalim ng root na direktoryong `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Mga Kinakailangan sa Konfigurasyon

Ang mga provider-backed na translation API ay nangangailangan ng konfigurasyon ng provider bago magsagawa ng pagsasalin:

- Ang pagsasalin ng Markdown at notebook ay nangangailangan ng LLM provider. I-configure alinman ang Azure OpenAI o OpenAI.
- Ang pagsasalin ng imahe ay nangangailangan ng Azure AI Vision bilang karagdagan sa LLM provider.
- `run_translation` nagpapatakbo ng magagaan na mga pagsusuri ng konektibidad bago magsimula ang pagsasalin ng proyekto.
- Ang mga Agent-assisted `start_*_agent_translation` at `finish_*_agent_translation` APIs ay hindi tumatawag sa Co-op Translator LLM providers. Ang host application o MCP agent ang nagsasalin ng inihandang mga chunk.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, at `run_review` ay deterministic at hindi nangangailangan ng kredensyal ng provider.

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

`run_review` ay deterministic at hindi nangangailangan ng Azure OpenAI, OpenAI, o Azure AI Vision na konfigurasyon.

## Mga Tala sa Pag-uugali

- Pinaghihiwalay ng mga Content translation API ang pagsasalin mula sa pag-rewrite ng project path. Tawagin nang tahasan ang `rewrite_markdown_paths` o `rewrite_notebook_paths` kapag kailangan i-adjust ang mga project-relative na link sa isasagawang lokasyon.
- Idinadagdag ng mga Project orchestration API ang pag-uugali ng proyekto sa paligid ng content translation, kasama ang pagtuklas ng file, pagsusulat, pag-rewrite ng path, metadata, paglilinis, at opsyonal na mga disclaimer.
- `run_translation` nagpi-print ng mga buod ng progreso at estima sa pamamagitan ng Click, na tumutugma sa karanasan ng gumagamit ng CLI.
- `dry_run=True` kinakalkula ang mga estima gamit ang virtual na mga update ng README, ngunit hindi isinusulat ang README o mga translation file.
- `groups` ay pinoproseso nang sunud-sunod. Isang pinagsamang estima ang pini-print bago magsimula ang trabaho.
- Kapag napili ang image translation, ang nawawalang Vision configuration ay magtataas ng error bago magsimula ang pagsasalin.
- Ang umiiral na alias-based na mga language folder ay natutukoy at maaaring ilipat sa mga canonical na pangalan ng language folder bilang bahagi ng pagpapatakbo.
- `run_review` nabibigo kapag may mga nawawalang translated na file, nawawala o lipas na translation metadata, maling porma ng Markdown frontmatter/code fences, at hindi valid na translated notebook JSON.
- `run_review` nag-uulat ng mga nawawalang lokal na Markdown at mga target ng image link bilang mga babala bilang default.

## Panloob na Landas ng Tawag

Ipinapasa ng API sa parehong core na implementasyon na ginagamit ng CLI:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` para sa in-memory na pagsasalin.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` para sa tahasang post-processing ng mga path.
3. `co_op_translator.api.translation.run_translation` para sa buong orkestrasyon ng proyekto.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mga nakatuon na project translation mixins para sa Markdown, mga notebook, at mga imahe.
8. Ang mga translator ng Markdown, notebook, text, at imahe sa ilalim ng `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Mga deterministikong pagsusuri sa ilalim ng `co_op_translator.review.checks`

Ang mga sumusunod na klase ay kapaki-pakinabang para sa mga nagpapanatili, ngunit hindi ine-export bilang matatag na API sa antas ng package.

| Klase | Modulo | Responsibilidad |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Nag-uugnay ng pagsasalin sa antas-proyekto, pamamahala ng direktoryo, normalisasyon ng metadata kada-wika, at pagtatalaga sa mga translator ng Markdown, notebook, at imahe. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Gumaganap ng async na pagproseso ng mga file para sa Markdown, mga notebook, mga imahe, pagtuklas ng mga lipas, at pag-update ng translation metadata. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Nag-oorganisa ng pagbabasa ng Markdown file, pagsasalin ng nilalaman, pag-rewrite ng path, metadata, mga disclaimer, at pagsusulat. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Nag-oorganisa ng pagbabasa ng notebook file, pagsasalin ng Markdown-cell, pag-rewrite ng path, metadata, mga disclaimer, at pagsusulat. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Nag-oorganisa ng pagtuklas ng source na imahe, pagsasalin ng imahe, output paths, metadata, at pagsusulat. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Naghahanap ng mga pares ng translated Markdown, sinusuri ang kalidad ng pagsasalin, at binabasa ang confidence metadata para sa mga workflow ng pag-aayos na may mababang kumpiyansa. |
| `ReviewRunner` | `co_op_translator.review.runner` | Nag-uugnay ng mga deterministikong pagsusuri ng review sa mga source file, target na wika, at mga nakonfigurang translation roots. |
| `ReviewTarget` | `co_op_translator.review.targets` | Naglalarawan ng isang source root at ang translation output directory na sinusuri para sa root na iyon. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Tinutukoy ang mga legacy alias language folder at naghahanda ng mga plano para sa migrasyon sa canonical na BCP 47 folder. |
| `Config` | `co_op_translator.config.base_config` | Naglo-load ng `.env` files at sinusuri kung ang kinakailangang LLM at opsyonal na Vision providers ay nakonfigura. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Awtomatikong natutukoy ang Azure OpenAI o OpenAI, beripikahin ang kinakailangang mga environment variable, at nagpapatakbo ng mga connectivity check para sa provider. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Tinutukoy ang Azure AI Vision configuration at nagpapatakbo ng mga connectivity check para sa image translation. |