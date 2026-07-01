# Pythoni API

Stabiilne avalik Pythoni API eksporditakse moodulist `co_op_translator.api`. Enamik integratsioone kasutab ühte järgmistest töövoogudest:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

Enamik `core`, `config`, `review` ja `utils` all olevatest madalama taseme moodulitest on teostuse üksikasjad, mida need API sisenemispunktid kasutavad.

MCP kliendid kasutavad sama avalikku API-d läbi [MCP Server](mcp.md). Kasuta seda lehekülge, kui kutseid teed Pythonilt otse, ja MCP juhendit, kui avad Co-op Translatori agendile või redaktorile. Kui valid CLI, Python API ja MCP vahel, alusta leheküljest [Choose Your Workflow](workflows.md).

## Esmakordne API-voog

Alusta siit, kui kutsud Co-op Translatorit Pythonist:

1. Konfigureeri LLM-teenuse pakkuja nagu kirjeldatud jaotises [Configuration](configuration.md), välja arvatud juhul, kui sa valmistad Markdowni või märkmiku tüki ainult host-agendi tõlkeks ette.
2. Otsusta, kas su rakendus haldab failide I/O-d.
3. Kasuta sisu-API-sid, kui su rakendus loeb ja kirjutab üksikuid faile.
4. Kasuta `run_translation`, kui Co-op Translator peaks töötlema repositooriumi nagu CLI.
5. Kasuta `run_review` pärast tõlget, kui vajad deterministlikke kontrolle automatiseerimises.

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Stsenaarium 1: Tõlgi üksikuid faile või dokumente

Kasuta seda töövoogu siis, kui sul on juba fail, redaktori puhver, märkmiku paylaod, MCP päring või kohandatud töötluse sisend. Sinu kood haldab failide I/O-d:

1. Loe lähte sisu.
2. Kutsu sisu tõlke-API-d.
3. Valikuliselt kutsu path-rewrite API-d, kui tõlgitud sisu kirjutatakse projekti tõlke kausta.
4. Salvesta või tagasta tulemus oma rakendusest.

Sisu tõlke API-d ei käivita projekti avastust, ei kirjuta metaandmeid, ei lisa allkirju ega kirjuta linke automaatselt ümber.

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

Kui tõlgitud Markdown ei ela Co-op Translatori projekti paigutuses, jäta `rewrite_markdown_paths` vahele ja salvesta tõlgitud string otse.

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

`translate_notebook_content` tõlgib Markdown-kesed ja säilitab mittemarkdown-kesed. Path-ümberkirjutus rakendub ainult Markdown-kestadele.

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

`translate_image_content` loeb lähtepildi ja tagastab renderdatud `PIL.Image.Image`. See ei kirjelda tõlgitud pildi metaandmeid kirjana.

## Stsenaarium 2: Tõlgi kogu repositoorium

Kasuta seda töövoogu, kui soovid, et Pythoni API käituks nagu `translate` CLI. `run_translation` avastab toetatud failid, tõlgib valitud sisutüüpe, kirjutab ümber teed, kirjutab väljundfaile, uuendab metaandmeid ja sooritab tõlke hooldustöid nagu puhastus.

`run_translation` on eelistatud projekti orkestreerimise sisenemispunkt. `translate_project` eksporditakse kui ühilduvusalias sama käitumisega.

Tõlgi Markdown-faile praeguses repositooriumis korea ja jaapani keelde:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Tõlgi ainult märkmikud konkreetsest projekti juurest:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Eelvaata tõlke mahtu ilma faile kirjutamata:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Tõlgi mitu sisendjuurt ühes kutses:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Kirjuta tõlked eksplicitsetesse väljundgruppidesse:

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

Kasuta iga keele jaoks eraldi kohatäiteid, kui iga keel peaks sisaldama pesastatud alamkausta:

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

Kui ükski `markdown`, `notebook` või `images` pole määratud, tõlgib API kõiki toetatud tüüpe: Markdowni, märkmikke ja pilte.

## Tõlgitud väljundi ülevaatus

`run_review` käitab deterministlikke tõlke kontrolle ilma LLMi või Visioni volitusteta.

!!! note "Beta"
    `run_review` on beetaversiooni deterministlik ülevaate-API. See ei kutsu mudeli pakkujaid ega kirjuta faile, kuid kontrollide ja probleemiskeemide struktuur võib muutuda.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Vaata üle ainult failid, mis on muudetud baasrefiga võrreldes, ja prindi GitHubi-laadset väljundit:

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

## Kopeeri-kleebi API näited

Tõlgi Markdown-sisu ilma failikirjeteta:

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

Tõlgi ja kirjuta Markdowni lingid ümber:

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

Tõlgi repositoorium Pythonilt:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Tõlgi mitu juurt:

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

Säilita terminoloogia glosaarist:

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

## Avalikud sisenemispunktid

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

## Sisu tõlke API-d

Sisu tõlke API-d on mõeldud integratsioonidele, millel on sisu mälu sees juba olemas, nagu redaktori laiendus, MCP tööriist, märkmikute töötleja või kohandatud torujuhe.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Translates Markdown content only. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Translates Markdown cells and preserves non-Markdown cells. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Extracts and translates image text, then returns a rendered image. It does not save translated image metadata. |

`translate_markdown_content` ja `translate_notebook_content` aktsepteerivad valikulist `source_path` oma valikute kaudu. See path antakse tõlkijale kontekstina; kutsujad jäävad vastutavaks projekti-spetsiifilise path-ümberkirjutuse eest pärast tõlget.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Samad valikud saab anda ka sõnastikena:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agendi abiga tõlke API-d

Agendi abiga API-d ei kutsu Co-op Translatorist Azure OpenAI-d ega OpenAI-d. Need valmistavad Markdowni või märkmiku tükid ette host-agendi tõlkimiseks ja seejärel konstrueerivad lõpliku sisu tõlgitud tükkidest.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return a self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from a job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return a notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while preserving code cells, outputs, and metadata. |

See töövoog on peamiselt mõeldud MCP hostidele. Kui vajad tootmisrepositooriumi tõlget, kus Co-op Translator haldab pakkuja kutseid, kasuta `translate_markdown_content`, `translate_notebook_content` või `run_translation`.

## Path-ümberkirjutuse API-d

Path-ümberkirjutuse API-d ei tee tõlget. Need uuendavad linke ja frontmatteri teid pärast seda, kui kutsuja teab lähte teed, tõlgitud sihtteed ja projekti paigutust.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Rewrites Markdown links and supported frontmatter path fields for a translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Applies Markdown path rewriting to each Markdown cell and leaves non-Markdown cells unchanged. |

Argumendi `policy` võib olla sõnastik järgmiste väljadega:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | No | Enabled translation types. Defaults to Markdown, notebooks, and images. |
| `lang_subdir` | No | Optional subdirectory under each language folder. |

## Projekti tõlke parameetrid

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

## Ülevaatuse parameetrid

`run_review` peegeldab meelega `run_translation` signatuuri, kus võimalik, nii et automatiseerimine saab tõlke ja ülevaatuse töövoogude vahel minimaalse haruharuga vahetada.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | Kohandatud tekstide tõlke väljundkataloog. Relatiivsed teed lahendatakse iga juurkausta suhtes. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Mitmed juurkaustad, mis jagavad samu väljundseadeid. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Selgesõnalised `(root_dir, translations_dir)` paarid. Neil on eelis `root_dirs`-i ees. |
| `changed_from` | `str \| None` | `None` | Git ref, mida kasutatakse ülevaate piiramseks muutunud lähtefailidele. |
| `output_format` | `str` | `"text"` | Ülevaate väljundvorming. Toetatud väärtused on `"text"` ja `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Käsitle hoiatusi ebaõnnestumistena lisaks vigadele. |
| `debug` | `bool` | `False` | Luba silumislogimine. |
| `save_logs` | `bool` | `False` | Salvesta DEBUG-taseme logifailid juurkataloogis `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Konfiguratsiooni nõuded

Provider-backed translation APIs require provider configuration before translating:

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

## Käitumise märkused

- Content translation APIs keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content needs project-relative links adjusted for a target location.
- Project orchestration APIs add project behavior around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` prints progress and estimate summaries through Click, matching the CLI user experience.
- `dry_run=True` computes estimates using virtual README updates, but does not write the README or translation files.
- `groups` are processed sequentially. A single aggregate estimate is printed before work begins.
- When image translation is selected, missing Vision configuration raises an error before translation starts.
- Existing alias-based language folders are detected and can be migrated to canonical language folder names as part of the run.
- `run_review` fails on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` reports missing local Markdown and image link targets as warnings by default.

## Sisemine kutsetee

The API delegates to the same core implementation used by the CLI:

Tõlkimine:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Ülevaatus:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Klass | Moodul | Vastutus |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordineerib projekti-taseme tõlkimist, kataloogi haldust, iga keele metaandmete normaliseerimist ja delegeerimist Markdowni, notebooki ja pilditõlkijatele. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Teostab asünkroonset failitöötlust Markdowni, notebookide, piltide, aegunud oleku tuvastamise ja tõlkemetaandmete uuenduste jaoks. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestreerib Markdown-failide lugemist, sisu tõlkimist, teede ümberkirjutamist, metaandmeid, lahtiütlusi ja kirjutamisi. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestreerib notebook-failide lugemist, Markdown-rakkude tõlkimist, teede ümberkirjutamist, metaandmeid, lahtiütlusi ja kirjutamisi. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestreerib lähtepiltide avastamist, piltide tõlkimist, väljundteid, metaandmeid ja kirjutamisi. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Leiab tõlgitud Markdowni paarid, hindab tõlke kvaliteeti ja loeb usaldusväärsuse metaandmeid madala usalduse parandustöövoogude jaoks. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordineerib deterministlikke ülevaatuse kontrolle lähtefailide, sihtkeelte ja konfigureeritud tõlkejuuride vahel. |
| `ReviewTarget` | `co_op_translator.review.targets` | Kirjeldab lähtejuurkausta ja selle jaoks ülevaadatavat tõlke väljundkataloogi. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Tuvastab vananenud alias-keelekaustad ja valmistab ette kanoniliste BCP 47 kausta migratsiooniplaanid. |
| `Config` | `co_op_translator.config.base_config` | Laadib `.env` faile ja kontrollib, kas nõutud LLM ja valikulised Visioni teenusepakkujad on konfigureeritud. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Automaatselt tuvastab Azure OpenAI või OpenAI, valideerib nõutud keskkonnamuutujad ja käivitab pakkuja ühenduvuse kontrollid. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Tuvastab Azure AI Vision konfiguratsiooni ja käivitab ühenduvuse kontrollid piltide tõlkimiseks. |