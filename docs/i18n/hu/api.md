# Python API

A stabil, nyilvános Python API a `co_op_translator.api`-ból van exportálva. A legtöbb integráció a következő munkafolyamatok egyikét használja:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

A `core`, `config`, `review` és `utils` alatti alacsonyabb szintű modulok többsége megvalósítási részlet, amelyet ezek az API belépési pontok használnak.

Az MCP kliens ugyanazt a nyilvános API-t használja a [MCP Server](mcp.md) felületén keresztül. Ezt az oldalt használja, ha közvetlenül Pythonból hívja az API-t, és az MCP útmutatót akkor, ha a Co-op Translatort egy ügynöknek vagy szerkesztőnek teszi elérhetővé. Ha a CLI, a Python API és az MCP között dönt, kezdje a [Válassza a munkafolyamatot](workflows.md) lappal.

## First-Time API Flow

Kezdje itt, ha a Co-op Translatort Python kódból hívja:

1. Állítson be egy LLM szolgáltatót az [Configuration](configuration.md) leírás szerint, kivéve ha csak Markdown- vagy notebook-darabokat készít elő host-ügynök fordításhoz.
2. Döntse el, hogy az alkalmazása kezeli-e a fájl I/O-t.
3. Használja a tartalom API-kat, ha az alkalmazása egyedi fájlokat olvas és ír.
4. Használja a `run_translation`-t, ha a Co-op Translatornak a CLI-hez hasonlóan kell feldolgoznia egy repót.
5. Használja a `run_review`-t fordítás után, ha determinisztikus ellenőrzésekre van szükség automatizációban.

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

Ezt a munkafolyamatot akkor használja, ha már rendelkezik egy fájllal, szerkesztőpufferral, notebook-payloaddal, MCP kéréssel vagy egyéni pipeline bemenettel. Az Ön kódja kezeli a fájl I/O-t:

1. Olvassa be a forrás tartalmat.
2. Hívja a tartalomfordító API-t.
3. Opcionálisan hívjon útvonal-átíró API-t, ha a lefordított tartalmat egy projekt fordítási mappájába írja.
4. Mentse vagy adja vissza az eredményt az alkalmazásból.

A tartalomfordító API-k nem futtatnak projekt-felderítést, nem írnak metaadatot, nem fűznek hozzá felelősségkizárásokat, és automatikusan nem írják át a linkeket.

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

Ha a lefordított Markdown nem egy Co-op Translator projekt elrendezésében fog élni, hagyja ki a `rewrite_markdown_paths`-t, és mentse a lefordított stringet közvetlenül.

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

A `translate_notebook_content` lefordítja a Markdown cellákat és megőrzi a nem-Markdown cellákat. Az útvonal-átírás csak a Markdown cellákra vonatkozik.

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

A `translate_image_content` beolvassa a forrásképet és egy renderelt `PIL.Image.Image`-t ad vissza. Nem írja ki a lefordított képek metaadatait.

## Scenario 2: Translate an Entire Repository

Ezt a munkafolyamatot használja, ha azt szeretné, hogy a Python API a `translate` CLI-hez hasonlóan viselkedjen. A `run_translation` felfedezi a támogatott fájlokat, lefordítja a kiválasztott tartalomtípusokat, átírja az útvonalakat, kiírja a kimeneti fájlokat, frissíti a metaadatokat, és végrehajt fordítási karbantartási feladatokat, például takarítást.

A `run_translation` az ajánlott projekt-orchestration belépési pont. A `translate_project` kompatibilitási aliasként van exportálva ugyanezzel a viselkedéssel.

Fordítsa le a Markdown fájlokat a jelenlegi repóban koreaira és japánra:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Fordítson csak notebookokat egy adott projektgyökérből:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Nézze meg a fordítás mennyiségét fájlok írása nélkül:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Fordítson több tartalomgyökeret egy hívásban:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Írja a fordításokat explicit kimeneti csoportokba:

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

Használjon nyelvenként helykitöltőt, ha minden nyelvnek egy beágyazott alkönyvtárat kell tartalmaznia:

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

Ha a `markdown`, `notebook` vagy `images` közül egyik sincs beállítva, az API minden támogatott típust fordít: Markdown, notebookokat és képeket.

## Review Translated Output

A `run_review` determinisztikus fordításellenőrzéseket futtat LLM vagy Vision hitelesítő adatok nélkül.

!!! note "Béta"
    A `run_review` egy béta, determinisztikus ellenőrző API. Nem hív modellszolgáltatókat és nem ír fájlokat, de az ellenőrzések és a hibasémák változhatnak.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Ellenőrizze csak azokat a fájlokat, amelyek egy alap ref-hez képest megváltoztak, és nyomtassa GitHub ízű kimenettel:

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

Fordítsa a Markdown tartalmat fájlírás nélkül:

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

Fordítsa és írja át a Markdown linkeket:

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

Fordítson egy repót Pythonból:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Fordítson több gyökeret:

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

Őrizze meg a gloszszárium kifejezéseket:

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

A tartalomfordító API-k azoknak az integrációknak szólnak, amelyeknél a tartalom már memóriában van, például egy szerkesztőbővítmény, MCP eszköz, notebook feldolgozó vagy egy egyéni pipeline.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Translates Markdown content only. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Translates Markdown cells and preserves non-Markdown cells. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Extracts and translates image text, then returns a rendered image. It does not save translated image metadata. |

A `translate_markdown_content` és a `translate_notebook_content` opcionálisan elfogad egy `source_path`-ot az opcióikban. Az útvonal a fordítónak kontextusként van átadva; a hívók továbbra is felelősek a projekt-specifikus útvonal-átírásért fordítás után.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Ugyanezek az opciók szótárként is átadhatók:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Az ügynök által segített API-k nem hívják az Azure OpenAI-t vagy az OpenAI-t a Co-op Translatorból. Előkészítik a Markdown- vagy notebook-darabokat egy host-ügynök fordításához, majd rekonstruálják a végső tartalmat a lefordított darabokból.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return a self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from a job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return a notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while preserving code cells, outputs, and metadata. |

Ez a munkafolyamat elsősorban MCP hostok számára szánt. Ha production repository fordításra van szüksége, amelynél a Co-op Translator kezeli a szolgáltatóhívásokat, használja a `translate_markdown_content`, `translate_notebook_content` vagy a `run_translation`-t.

## Path Rewriting APIs

Az útvonal-átíró API-k nem végeznek fordítást. A linkeket és a frontmatter útvonalakat frissítik, miután a hívók ismerik a forrásútvonalat, a lefordított célt és a projekt elrendezését.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Rewrites Markdown links and supported frontmatter path fields for a translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Applies Markdown path rewriting to each Markdown cell and leaves non-Markdown cells unchanged. |

A `policy` argumentum egy olyan szótár lehet, amely a következő mezőket tartalmazza:

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

A `run_review` szándékosan tükrözi a `run_translation` aláírását, ahol lehetséges, hogy az automatizáció minimális elágazással válthasson a fordítási és az ellenőrzési munkafolyamatok között.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | Egyéni szövegfordítási kimeneti könyvtár. A relatív útvonalak minden gyökérhez viszonyítva oldódnak fel. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Több gyökér, amelyek ugyanazokat a kimeneti beállításokat használják. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Kifejezett `(root_dir, translations_dir)` párok. Elsőbbséget élvez a `root_dirs`-szal szemben. |
| `changed_from` | `str \| None` | `None` | Git ref, amely a felülvizsgálatot a megváltozott forrásfájlokra korlátozza. |
| `output_format` | `str` | `"text"` | A felülvizsgálat kimeneti formátuma. A támogatott értékek: `"text"` és `"github"`. |
| `fail_on_warnings` | `bool` | `False` | A figyelmeztetések hibaként való kezelése a hibák mellett. |
| `debug` | `bool` | `False` | Engedélyezi a hibakeresési naplózást. |
| `save_logs` | `bool` | `False` | DEBUG szintű naplófájlok mentése a gyökér `logs/` könyvtárába. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Konfigurációs követelmények

A szolgáltató által támogatott fordítási API-k szolgáltatókonfigurációt igényelnek fordítás előtt:

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

## Viselkedési megjegyzések

- Content translation APIs keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content needs project-relative links adjusted for a target location.
- Project orchestration APIs add project behavior around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` prints progress and estimate summaries through Click, matching the CLI user experience.
- `dry_run=True` computes estimates using virtual README updates, but does not write the README or translation files.
- `groups` are processed sequentially. A single aggregate estimate is printed before work begins.
- When image translation is selected, missing Vision configuration raises an error before translation starts.
- Existing alias-based language folders are detected and can be migrated to canonical language folder names as part of the run.
- `run_review` fails on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` reports missing local Markdown and image link targets as warnings by default.

## Belső hívási út

The API delegates to the same core implementation used by the CLI:

Fordítás:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for memóriabeli fordításhoz.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for kifejezett útvonal utófeldolgozáshoz.
3. `co_op_translator.api.translation.run_translation` for teljes projektorchestrációhoz.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Felülvizsgálat:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Determinisztikus ellenőrzések a `co_op_translator.review.checks` alatt

A következő osztályok hasznosak a fenntartók számára, de nem exportáltak a csomagszintű stabil API-ként.

| Osztály | Modul | Felelősség |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinálja a projekt szintű fordítást, a könyvtárkezelést, a nyelvenkénti metaadat-normalizálást, valamint a delegálást a Markdown-, jegyzetfüzet- és képfordítók felé. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, jegyzetfüzetek, képek, elavultság-észlelés és fordítási metaadat-frissítések aszinkron fájlfeldolgozását végzi. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Koordinálja a Markdown fájlok olvasását, a tartalom fordítását, az útvonal-átírást, a metaadatokat, a nyilatkozatokat és az írást. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Koordinálja a jegyzetfüzet fájlok olvasását, a Markdown-cellák fordítását, az útvonal-átírást, a metaadatokat, a nyilatkozatokat és az írást. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Koordinálja a forrásképek felderítését, a képfordítást, a kimeneti útvonalakat, a metaadatokat és az írást. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Megtalálja a lefordított Markdown párokat, értékeli a fordítás minőségét, és beolvassa a bizalmi metaadatokat az alacsony megbízhatóságú javítási munkafolyamatokhoz. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinálja a determinisztikus felülvizsgálati ellenőrzéseket a forrásfájlok, célnyelvek és konfigurált fordítási gyökerek között. |
| `ReviewTarget` | `co_op_translator.review.targets` | Leír egy forrás gyökeret és a hozzá tartozó, vizsgált fordítási kimeneti könyvtárat. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Felderíti a régi alias nyelvi mappákat és előkészíti a kanonikus BCP 47 mappamigrációs terveket. |
| `Config` | `co_op_translator.config.base_config` | Betölti a `.env` fájlokat és ellenőrzi, hogy a szükséges LLM és az opcionális Vision szolgáltatók konfigurálva vannak-e. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Automatikusan felismeri az Azure OpenAI-t vagy az OpenAI-t, érvényesíti a szükséges környezeti változókat, és futtat kapcsolódási ellenőrzéseket a szolgáltatóhoz. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Felderíti az Azure AI Vision konfigurációt és kapcsolódási ellenőrzéseket futtat a képfordításhoz. |