# API ng Python

Ang matatag na pampublikong API ng Python ay ine-export mula sa `co_op_translator.api`. Karamihan sa mga integration ay gumagamit ng isa sa mga workflow na ito:

| Senaryo | Gamitin ito kapag | Pangunahing API |
| --- | --- | --- |
| Isalin ang indibidwal na mga file o dokumento | Binabasa ng iyong aplikasyon ang pinagmulan ng nilalaman, tinatawagan ang Co-op Translator para sa pagsasalin, at pinipili kung saan ise-save ang resulta. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Ihanda ang nilalaman para sa host-agent translation | Ang iyong MCP host o application model ang magsasalin ng mga chunk, habang ang Co-op Translator ang humahawak ng chunking at reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Isalin ang buong repositoryo | Gusto mong kumilos ang Python API tulad ng CLI at humawak ng discovery, output paths, metadata, cleanup, at mga write. | `run_translation` |

Karamihan sa mga lower-level na module sa ilalim ng `core`, `config`, `review`, at `utils` ay mga detalye ng implementasyon na ginagamit ng mga entry point ng API na ito.

Gumagamit ang mga kliyente ng MCP ng parehong pampublikong API sa pamamagitan ng [MCP Server](mcp.md). Gamitin ang pahinang ito kapag tumatawag nang direkta sa Python, at ang gabay ng MCP kapag inilalantad ang Co-op Translator sa isang agent o editor. Kung nagpapasya ka sa pagitan ng CLI, Python API, at MCP, magsimula sa [Pumili ng Iyong Workflow](workflows.md).

## Unang Daloy ng API

Magsimula rito kung tumatawag ka sa Co-op Translator mula sa Python code:

1. I-configure ang isang LLM provider tulad ng inilarawan sa [Konfigurasyon](configuration.md), maliban kung naghahanda ka lamang ng mga chunk ng Markdown o notebook para sa host-agent translation.
2. Magpasya kung ang iyong aplikasyon ang bahala sa file I/O.
3. Gamitin ang content APIs kapag binabasa at sinusulat ng iyong aplikasyon ang indibidwal na mga file.
4. Gamitin ang `run_translation` kapag dapat iproseso ng Co-op Translator ang isang repositoryo tulad ng CLI.
5. Gamitin ang `run_review` pagkatapos ng pagsasalin kung kailangan mo ng deterministic na mga tsek sa automation.

| Layunin | API na sisimulan |
| --- | --- |
| Isalin ang isang Markdown string o file | `translate_markdown_content` |
| Isalin ang isang notebook payload | `translate_notebook_content` |
| Isalin ang isang imahe | `translate_image_content` |
| Hayaan ang host agent na isalin ang mga chunk ng Markdown o notebook | `start_markdown_agent_translation` o `start_notebook_agent_translation` |
| Isulat muli ang mga isinalin na link pagkatapos pumili ng output path | `rewrite_markdown_paths` o `rewrite_notebook_paths` |
| Isalin ang buong repositoryo | `run_translation` |
| Suriin ang isinaling output | `run_review` |

## Senaryo 1: Isalin ang Indibidwal na Mga File o Dokumento

Gamitin ang workflow na ito kapag mayroon ka nang file, editor buffer, notebook payload, kahilingan ng MCP, o custom pipeline input. Ang iyong code ang may responsibilidad sa file I/O:

1. Basahin ang pinagmulan ng nilalaman.
2. Tawagan ang isang content translation API.
3. Opsyonal na tawagan ang isang path rewriting API kung ang isinaling nilalaman ay isusulat sa isang project translation folder.
4. I-save o ibalik ang resulta mula sa iyong aplikasyon.

Ang content translation APIs ay hindi nagpapatakbo ng project discovery, hindi nagsusulat ng metadata, hindi naglalagay ng mga disclaimer, at hindi awtomatikong nire-rewrite ang mga link.

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

Kung ang isinaling Markdown ay hindi maninirahan sa Co-op Translator project layout, laktawan ang `rewrite_markdown_paths` at i-save ang isinaling string nang direkta.

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

`translate_notebook_content` ay nagsasalin ng mga Markdown cell at pinangangalagaan ang mga non-Markdown na cell. Ang path rewriting ay inilalapat lamang sa mga Markdown cell.

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

`translate_image_content` binabasa ang source image at nagbabalik ng rendered na `PIL.Image.Image`. Hindi nito sinisulat ang translated image metadata.

## Senaryo 2: Isalin ang Buong Repositoryo

Gamitin ang workflow na ito kapag gusto mong kumilos ang Python API tulad ng `translate` CLI. Inidi-discover ng `run_translation` ang mga suportadong file, isinasalin ang napiling mga uri ng nilalaman, nirerewrite ang mga path, sumusulat ng mga output file, ina-update ang metadata, at nagsasagawa ng mga maintenance na gawain sa pagsasalin tulad ng cleanup.

`run_translation` ang inirerekomendang entry point para sa project orchestration. Ang `translate_project` ay ine-export bilang compatibility alias na may parehong pag-uugali.

Isalin ang mga Markdown file sa kasalukuyang repositoryo sa Korean at Hapon:

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

I-preview ang volume ng pagsasalin nang hindi nagsusulat ng mga file:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

I-record ang naka-istrukturang mga progress event para sa isang integration:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Iimbak ang payload sa iyong job-event na talahanayan o i-stream ito sa iyong UI.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Gumagamit ang mga event ng versioned schema na `co-op.translation.event.v1`. Dapat ang mga integration
umasa sa mga stable na field tulad ng `type` at `stage_key`, hindi sa human-facing
console text o `stage_label`.

Isalin ang maramihang content root sa isang tawag:

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

Gumamit ng per-language placeholder kapag ang bawat wika ay dapat magkaroon ng nested subdirectory:

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

### Panatilihin ang mga tinanggap na pag-edit ng tao gamit ang translation state provider

Sa default, pinapanatili ng Co-op Translator ang umiiral nitong file-level na pag-uugali: kapag ang
Markdown source ay stale, ang buong isinalang file ay nire-regenerate. Ang naka-host na
mga integration ay opsyonal na maaaring magpasa ng `TranslationStateProvider` upang panatilihin ang mga pag-edit ng tao
sa mga source block na hindi nagbago.

Ang provider ay nagbibigay ng huling tinanggap na source/target pair at nire-record ang bawat bagong
candidate. Ang pag-apruba ay nananatiling responsibilidad ng integration—halimbawa,
pagkatapos ma-merge ang isang translation pull request:

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

Para sa mga Markdown file na may valid na tinanggap na baseline, inia-align ng Co-op Translator
ang top-level Markdown blocks. Ang mga hindi nagbago na source block ay muling gumagamit ng kasalukuyang isinaling
mga block, kabilang ang mga pag-edit na ginawa ng mga tao; ang mga nagbago o idinagdag na source block ay ipinapadala
para sa pagsasalin; ang mga tinanggal na source block ay inaalis. Kung ang alignment ay malabo,
nagbago ang istruktura ng target, invalid ang block translation, o walang baseline na
magagamit, ligtas na bumabalik ang Co-op Translator sa umiiral na full-file
translation path.

Ang API na ito ay nag-iimbak ng document translation state, hindi ng cross-document na parirala o
segment translation memory. Sa kasalukuyan inilalapat ito sa Markdown project
translation. Hindi nagbago ang pag-uugali ng notebook at image. Ang pagpasa ng `update=True`
ay humihiling pa rin ng buong regeneration.

Kung ang isa o higit pang file ay hindi mai-salin, nagta-throw ang `run_translation` ng isang
`RuntimeError` pagkatapos matapos ang project workflow sa halip na i-report ang isang
matagumpay na run na may nawawalang output. Dapat ituring ng mga integration ito bilang nabigong
job at panatilihin ang naunang tinanggap na translation state.

## Suriin ang Isinaling Output

`run_review` nagpapatakbo ng deterministic na mga tsek sa pagsasalin nang walang LLM o Vision credentials.

!!! note "Beta"
    `run_review` ay isang beta deterministic review API. Hindi nito tinatawagan ang mga model provider o nagsusulat ng mga file, ngunit ang mga tsek at mga schema ng isyu ay maaaring magbago.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Pagkatapos ng README-only na pagsasalin, gamitin ang parehong saklaw para sa review:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` nagre-review lamang ng `README.md` sa ilalim ng bawat naka-configure na source root,
kabilang ang custom na `groups` at mga output directory. Ang ibang dokumento at mga nested
README ay hindi kasama. Ang nawawalang source README ay nagta-raise ng `ValueError`; ang nabigong
mga tsek sa pagsasalin ay nagta-raise ng `RuntimeError`.

I-review lamang ang mga file na nagbago laban sa base ref at i-print ang GitHub-flavored na output:

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

## Mga Halimbawa ng Copy-Paste ng API

Isalin ang Markdown na nilalaman nang hindi nagsusulat ng mga file:

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

Isalin at isulat muli ang mga link ng Markdown:

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

Panatilihin ang mga termino sa glossary:

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

## Pampublikong Entry Points

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

## Mga API para sa Pagsasalin ng Nilalaman

Ang content translation APIs ay nilalayong gamitin para sa mga integration na mayroon nang nilalaman sa memorya, tulad ng isang editor extension, MCP tool, notebook processor, o custom pipeline.

| Function | Input | Output | File I/O | Mga Tala |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Nagsasalin lamang ng nilalaman ng Markdown. Hindi nito nire-rewrite ang mga link, sumusulat ng metadata, o nagdaragdag ng mga disclaimer. |
| `translate_notebook_content` | Notebook JSON `str` o `dict` | Notebook JSON `str` | No | Async. Nagsasalin ng mga Markdown cell at pinangangalagaan ang mga non-Markdown na cell. Hindi nito nire-rewrite ang mga link, sumusulat ng metadata, o nagdaragdag ng mga disclaimer. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Binabasa lamang ang source image | Synchronous. Nag-e-extract at nagsasalin ng teksto sa imahe, pagkatapos ay nagbabalik ng rendered na imahe. Hindi nito sine-save ang translated image metadata. |

`translate_markdown_content` at `translate_notebook_content` tumatanggap ng optional na `source_path` sa pamamagitan ng kanilang mga option. Ang path ay ipinapasa bilang konteksto sa translator; nananatiling responsibilidad ng tumatawag ang anumang project-specific na path rewriting pagkatapos ng pagsasalin.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Parehong mga option ay maaaring ipasa bilang mga dictionary:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Mga API na Tinutulungan ng Agent para sa Pagsasalin

Ang mga agent-assisted na API ay hindi tumatawag sa naka-configure na LLM provider mula sa Co-op Translator. Inihahanda nila ang mga chunk ng Markdown o notebook para isalin ng host agent, pagkatapos ay nire-reconstruct ang pangwakas na nilalaman mula sa mga isinaling chunk.

| Function | Layunin |
| --- | --- |
| `start_markdown_agent_translation` | Ibalik ang isang self-contained na Markdown job na may mga chunk, prompt, at reconstruction state. |
| `finish_markdown_agent_translation` | I-reconstruct ang Markdown mula sa isang job at mga host-agent na isinaling chunk. |
| `start_notebook_agent_translation` | Ibalik ang isang notebook job na may mga Markdown-cell chunk para sa host-agent translation. |
| `finish_notebook_agent_translation` | I-reconstruct ang notebook JSON habang pinangangalagaan ang code cells, outputs, at metadata. |

Ang workflow na ito ay pangunahing nilalayong para sa MCP hosts. Kung kailangan mo ng production repository translation na pinamamahalaan ng Co-op Translator ang mga provider call, gamitin ang `translate_markdown_content`, `translate_notebook_content`, o `run_translation`.

## Mga API para sa Path Rewriting

Ang path rewriting APIs ay walang isinasagawang pagsasalin. Ina-update nila ang mga link at frontmatter path pagkatapos malaman ng tumatawag ang source path, isinaling target path, at project layout.

| Function | Saklaw | Mga Tala |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body at frontmatter | Nirerewrite ang mga Markdown link at suportadong frontmatter path field para sa isang isinaling target. |
| `rewrite_notebook_paths` | Mga Markdown cell sa notebook JSON | Inilalapat ang Markdown path rewriting sa bawat Markdown cell at iniwang hindi nagbabago ang non-Markdown na mga cell. |

Ang argumentong `policy` ay maaaring isang dictionary na may mga field na ito:

| Field | Kinakailangan | Layunin |
| --- | --- | --- |
| `language_code` | Oo | Code ng target na wika, tulad ng `"ko"` o `"pt-BR"`. |
| `root_dir` | Hindi | Source project root. Default ay `"."`. |
| `translations_dir` | Hindi | Text translation output directory. Default ay `translations` sa ilalim ng `root_dir`. |
| `translated_images_dir` | Hindi | Translated image output directory. Default ay `translated_images` sa ilalim ng `root_dir`. |
| `translation_types` | Hindi | Enabled translation types. Default ay Markdown, notebooks, at images. |
| `lang_subdir` | Hindi | Optional subdirectory sa ilalim ng bawat language folder. |

## Mga Parameter ng Project Translation

| Parameter | Uri | Default | Layunin |
| --- | --- | --- | --- |
| `language_codes` | `str` | Kinakailangan | Mga target language code na pinaghiwalay ng espasyo, tulad ng `"ko ja fr"`, o `"all"`. Ang alias codes ay nir-normalize sa canonical BCP 47 values. |
| `root_dir` | `str` | `"."` | Project root para sa isang solong translation target. Hindi pinapansin kapag ang `root_dirs` o `groups` ay ibinigay. |
| `update` | `bool` | `False` | Tanggalin at muling likhain ang umiiral na mga pagsasalin para sa mga napiling wika. |
| `images` | `bool` | `False` | Isama ang image translation. Nangangailangan ng Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Isama ang Markdown translation. |
| `notebook` | `bool` | `False` | Isama ang Jupyter notebook translation. |
| `debug` | `bool` | `False` | Paganahin ang debug logging. |
| `save_logs` | `bool` | `False` | I-save ang mga DEBUG-level na log file sa ilalim ng root `logs/` directory. |
| `yes` | `bool` | `True` | Awtomatikong kinukumpirma ang mga prompt para sa programmatic at CI na paggamit. |
| `add_disclaimer` | `bool` | `False` | Magdagdag ng mga disclaimer tungkol sa machine translation sa mga isinaling Markdown at notebook. |
| `translations_dir` | `str \| None` | `None` | Pasadyang direktoryo para sa output ng tekstong isinalin. Ang mga relative na path ay nireresolba batay sa bawat root. |
| `image_dir` | `str \| None` | `None` | Pasadyang direktoryo para sa output ng isinaling mga imahe. Ang mga relative na path ay nireresolba batay sa bawat root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Maramihang root na nagbabahagi ng parehong mga setting ng output. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Tiyak na pares na `(root_dir, translations_dir)`. Mas inuuna kaysa sa `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL ng repositoryo na ginagamit kapag nirender ang gabay sa talahanayan ng wika ng README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Mga termino sa glosaryo na pinananatili habang isinasalin. Ang mga duplicate at blangkong termino ay nininormalisa. |
| `dry_run` | `bool` | `False` | Tantiyahin ang dami ng pagsasalin at i-preview ang kilos ng migrasyon nang hindi sumusulat ng mga file. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Opsyonal na persistence adapter para sa accepted-baseline at candidate para sa incremental na pag-update ng Markdown. Kung hindi ito isasama, mananatili ang kasalukuyang pag-uugali ng buong-file. |

## Mga Parameter ng Review

`run_review` sadyang ginagaya ang signature ng `run_translation` kapag posible upang ang automation ay makalipat sa pagitan ng mga workflow ng pagsasalin at review nang may kaunting branching.

| Parameter | Uri | Default | Layunin |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Mga target na folder ng wika na susuriin. Tinatanggap ang mga string na pinaghiwalay ng espasyo at mga iterable. Sinusuri ng `"all"` ang bawat natuklasang wika ng pagsasalin. |
| `root_dir` | `str` | `"."` | Root ng proyekto para sa isang target ng review. Hindi ito pinapansin kapag ang `root_dirs` o `groups` ay ibinigay. |
| `markdown` | `bool` | `False` | Isama ang mga source na file na Markdown at MDX. |
| `notebook` | `bool` | `False` | Isama ang mga source file ng Jupyter notebook. |
| `images` | `bool` | `False` | Nakalaan para sa pagkakapantay-pantay sa mga opsyon ng pagsasalin. Sinusuri ang mga sanggunian ng link sa mga imahe mula sa Markdown. |
| `translations_dir` | `str \| None` | `None` | Pasadyang direktoryo para sa output ng tekstong isinalin. Ang mga relative na path ay nireresolba batay sa bawat root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Maramihang root na nagbabahagi ng parehong mga setting ng output. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Tiyak na pares na `(root_dir, translations_dir)`. Mas inuuna kaysa sa `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref na ginagamit para limitahan ang review sa mga nabagong source file. |
| `readme_only` | `bool` | `False` | Susuriin lamang ang `README.md` sa ilalim ng bawat source root. Ang nawawalang source README ay magtataas ng `ValueError`. |
| `output_format` | `str` | `"text"` | Format ng output ng review. Sinusuportahang mga halaga ay `"text"` at `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Ituring ang mga babala bilang pagkabigo bukod sa mga error. |
| `debug` | `bool` | `False` | Paganahin ang debug logging. |
| `save_logs` | `bool` | `False` | I-save ang mga log file na nasa DEBUG level sa ilalim ng root na direktoryong `logs/`. |

Kung wala sa `markdown`, `notebook`, o `images` ang naka-set, nire-review ng API ang Markdown, mga notebook, at mga sanggunian ng link ng imahe kapag naaangkop. Ang review ay hindi tumatawag ng LLM provider at hindi nangangailangan ng mga API key.

## Mga Kinakailangan sa Konfigurasyon

Ang mga translation API na may suporta ng provider ay nangangailangan ng konfigurasyon ng provider bago magsagawa ng pagsasalin:

- Ang pagsasalin ng Markdown at notebook ay nangangailangan ng LLM provider. I-configure ang Azure OpenAI, OpenAI, o Anthropic.
- Ang pagsasalin ng imahe ay nangangailangan ng Azure AI Vision bukod pa sa LLM provider.
- Ang `run_translation` ay nagpapatakbo ng magaan na connectivity checks bago magsimula ang pagsasalin ng proyekto.
- Ang mga Agent-assisted na `start_*_agent_translation` at `finish_*_agent_translation` na API ay hindi tumatawag sa Co-op Translator LLM providers. Ang host application o MCP agent ang nagsasalin ng mga inihandang chunk.
- Ang `rewrite_markdown_paths`, `rewrite_notebook_paths`, at `run_review` ay deterministic at hindi nangangailangan ng kredensyal ng provider.

Kinakailangang mga variable para sa Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Kinakailangang mga variable para sa OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Kinakailangang mga variable para sa Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` at `ANTHROPIC_MAX_TOKENS` ay opsyonal. Ang Microsoft Agent Framework ang default na model client para sa lahat ng providers simula sa Co-op Translator 0.22.0. Maaaring pansamantalang piliin ang Semantic Kernel gamit ang `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, ngunit maglalabas iyon ng deprecation warning; tingnan ang [konfigurasyon](configuration.md#model-client-backend) para sa planong unti-unting pagtanggal.

Kinakailangang mga variable ng Azure AI Vision para sa pagsasalin ng imahe:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` ay deterministic at hindi nangangailangan ng konfigurasyon ng LLM o Azure AI Vision.

## Mga Tala sa Pag-uugali

- Pinapanatiling hiwalay ng mga content translation API ang pagsasalin mula sa pagre-rewrite ng path ng proyekto. Tawagin ang `rewrite_markdown_paths` o `rewrite_notebook_paths` nang tahasan kapag kailangan i-adjust ang mga project-relative na link ng isinaling nilalaman para sa target na lokasyon.
- Idinadagdag ng mga project orchestration API ang pag-uugali ng proyekto sa paligid ng pagsasalin ng nilalaman, kasama ang pagtuklas ng mga file, pagsusulat, pagre-rewrite ng path, metadata, paglilinis, at opsyonal na mga disclaimer.
- Ipi-print ng `run_translation` ang mga buod ng progreso at pagtatantiya gamit ang parehong Rich-backed reporter na ginagamit ng CLI. Ang non-interactive na output ay babalik sa plain text.
- Ang `dry_run=True` ay nagkukumputa ng mga pagtatantiya gamit ang virtual na mga update ng README, ngunit hindi nito sinususulat ang README o mga translation file.
- Ang mga `groups` ay pinoproseso nang sunud-sunod. Isang nag-iisang aggregate na pagtatantiya ang ipi-print bago magsimula ang trabaho.
- Kapag pinili ang pagsasalin ng imahe, ang nawawalang Vision configuration ay magtataas ng error bago magsimula ang pagsasalin.
- Natutukoy ang umiiral na mga language folder na batay sa alias at maaari silang mailipat sa mga canonical na pangalan ng folder ng wika bilang bahagi ng pagpapatakbo.
- Nabibigo ang `run_review` kapag may nawawalang isinaling mga file, nawawala o lipas na translation metadata, maling format ng Markdown frontmatter/code fences, at hindi wastong JSON ng isinaling notebook.
- Nag-uulat ang `run_review` ng nawawalang lokal na mga target ng Markdown at mga link ng imahe bilang mga babala sa default.

## Panloob na Landas ng Tawag

Ine-delegate ng API sa parehong core na implementasyon na ginagamit ng CLI:

Pagsasalin:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` para sa in-memory na pagsasalin.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` para sa tahasang post-processing ng path.
3. `co_op_translator.api.translation.run_translation` para sa buong orchestration ng proyekto.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mga nakatuong project translation mixins para sa Markdown, mga notebook, at mga imahe.
8. Ang mga tagasalin para sa Markdown, notebook, teksto, at imahe sa ilalim ng `co_op_translator.core`.

Pagsusuri:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic na mga check sa ilalim ng `co_op_translator.review.checks`

Ang mga sumusunod na klase ay kapaki-pakinabang para sa mga maintainer, ngunit hindi in-export bilang package-level na stable API.

| Klase | Modul | Responsibilidad |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Nag-uugnay ng project-level na pagsasalin, pamamahala ng direktoryo, normalisasyon ng per-language metadata, at pagdelegar sa mga tagasalin para sa Markdown, notebook, at imahe. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Gumaganap ng async na pagpoproseso ng mga file para sa Markdown, mga notebook, imahe, pagtukoy ng stale, at mga update ng translation metadata. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Inaayos ang pagbabasa ng mga file ng Markdown, pagsasalin ng nilalaman, pagre-rewrite ng path, metadata, mga disclaimer, at pagsusulat. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Inaayos ang pagbabasa ng mga notebook file, pagsasalin ng mga Markdown-cell, pagre-rewrite ng path, metadata, mga disclaimer, at pagsusulat. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Inaayos ang pagtuklas ng mga source image, pagsasalin ng imahe, mga output path, metadata, at pagsusulat. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Naghahanap ng mga pares ng isinaling Markdown, sinusuri ang kalidad ng pagsasalin, at binabasa ang confidence metadata para sa mga workflow ng pag-aayos sa mababang kumpiyansa. |
| `ReviewRunner` | `co_op_translator.review.runner` | Nako-coordinate ang deterministic na mga review check sa mga source file, mga target na wika, at mga naka-configure na translation root. |
| `ReviewTarget` | `co_op_translator.review.targets` | Naglalarawan ng source root at ang translation output directory na sinusuri para sa root na iyon. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Natutukoy ang mga legacy alias na language folder at naghahanda ng mga plano ng migrasyon tungo sa canonical na BCP 47 na mga folder. |
| `Config` | `co_op_translator.config.base_config` | Naglo-load ng `.env` files at sinusuri kung naka-configure ang kinakailangang LLM at opsyonal na Vision providers. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Awtomatikong natutukoy ang Azure OpenAI, OpenAI, o Anthropic, binavalida ang kinakailangang environment variables, at nagpapatakbo ng connectivity checks ng provider. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Natutukoy ang konfigurasyon ng Azure AI Vision at nagpapatakbo ng connectivity checks para sa pagsasalin ng imahe. |