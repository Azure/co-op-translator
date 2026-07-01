# Python API

API-ul public stabil pentru Python este exportat din `co_op_translator.api`. Majoritatea integrărilor folosesc unul dintre aceste fluxuri de lucru:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

Majoritatea modulelor de nivel inferior din `core`, `config`, `review` și `utils` sunt detalii de implementare folosite de aceste puncte de intrare ale API-ului.

Clienții MCP folosesc același API public prin [MCP Server](mcp.md). Folosiți această pagină când apelați Python direct, iar ghidul MCP când expuneți Co-op Translator unui agent sau editor. Dacă decideți între CLI, API-ul Python și MCP, începeți cu [Choose Your Workflow](workflows.md).

## First-Time API Flow

Porniți de aici dacă apelați Co-op Translator din cod Python:

1. Configurați un furnizor LLM așa cum este descris în [Configuration](configuration.md), cu excepția cazului în care doar pregătiți fragmente Markdown sau notebook pentru traducerea de către gazdă/agent.
2. Decideți dacă aplicația dvs. deține operațiile de I/O pentru fișiere.
3. Folosiți API-urile de conținut când aplicația dvs. citește și scrie fișiere individuale.
4. Folosiți `run_translation` când Co-op Translator ar trebui să proceseze un repository ca CLI-ul.
5. Folosiți `run_review` după traducere dacă aveți nevoie de verificări deterministe în automatizare.

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

Folosiți acest flux de lucru când aveți deja un fișier, un buffer din editor, un payload de notebook, o cerere MCP sau un input personalizat de pipeline. Codul dvs. deține I/O pentru fișiere:

1. Citiți conținutul sursă.
2. Apelați un API de traducere a conținutului.
3. Opțional apelați un API de rescriere a căilor dacă conținutul tradus va fi scris într-un folder de traduceri al proiectului.
4. Salvați sau returnați rezultatul din aplicația dvs.

API-urile de traducere a conținutului nu rulează descoperirea proiectului, nu scriu metadate, nu adaugă declinări și nu rescriu linkuri automat.

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

Dacă Markdown-ul tradus nu va exista într-un layout de proiect Co-op Translator, omiteți `rewrite_markdown_paths` și salvați șirul tradus direct.

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

`translate_notebook_content` traduce celulele Markdown și păstrează celulele non-Markdown. Rescrierea căilor se aplică doar celulelor Markdown.

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

`translate_image_content` citește imaginea sursă și returnează o `PIL.Image.Image` redată. Nu scrie metadate pentru imaginea tradusă.

## Scenario 2: Translate an Entire Repository

Folosiți acest flux de lucru când doriți ca API-ul Python să se comporte ca CLI-ul `translate`. `run_translation` descoperă fișiere suportate, traduce tipurile de conținut selectate, rescrie căi, scrie fișierele de ieșire, actualizează metadatele și execută sarcini de întreținere a traducerilor, cum ar fi curățarea.

`run_translation` este punctul de intrare preferat pentru orchestrarea proiectului. `translate_project` este exportat ca alias de compatibilitate cu același comportament.

Traduceți fișiere Markdown din repository-ul curent în coreeană și japoneză:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Traduceți doar notebook-uri dintr-un root specific al proiectului:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Previzualizați volumul traducerii fără a scrie fișiere:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Traduceți mai multe root-uri de conținut într-un apel:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Scrieți traducerile în grupuri de ieșire explicite:

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

Folosiți un placeholder pe limbă când fiecare limbă ar trebui să conțină un subdirector imbricat:

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

Dacă nici unul dintre `markdown`, `notebook`, sau `images` nu este setat, API-ul traduce toate tipurile suportate: Markdown, notebook-uri și imagini.

## Review Translated Output

`run_review` rulează verificări deterministe ale traducerii fără acreditări LLM sau Vision.

!!! note "Beta"
    `run_review` este un API beta de revizuire deterministă. Nu apelează furnizori de modele și nu scrie fișiere, dar schemele de verificare și de raportare a problemelor pot evolua.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Revizuiți doar fișierele schimbate față de un ref de bază și afișați ieșire în stil GitHub:

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

Traduceți conținut Markdown fără scrierea în fișiere:

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

Traduceți și rescrieți linkuri Markdown:

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

Traduceți un repository din Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Traduceți mai multe root-uri:

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

Păstrați termeni din glosar:

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

API-urile de traducere a conținutului sunt destinate integrărilor care deja au conținut în memorie, cum ar fi o extensie de editor, un instrument MCP, un procesator de notebook-uri sau un pipeline personalizat.

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

Acest flux de lucru este destinat în principal gazdelor MCP. Dacă aveți nevoie de traducere în producție a repository-ului cu Co-op Translator gestionând apelurile către furnizori, folosiți `translate_markdown_content`, `translate_notebook_content`, sau `run_translation`.

## Path Rewriting APIs

API-urile de rescriere a căilor nu efectuează traducere. Ele actualizează linkurile și căile din frontmatter după ce apelanții cunosc calea sursă, calea țintă tradusă și layout-ul proiectului.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Rewrites Markdown links and supported frontmatter path fields for a translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Applies Markdown path rewriting to each Markdown cell and leaves non-Markdown cells unchanged. |

Argumentul `policy` poate fi un dicționar cu aceste câmpuri:

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

`run_review` intenționat oglindește semnătura `run_translation` acolo unde este posibil astfel încât automatizarea să poată comuta între fluxurile de traducere și revizuire cu un minim de ramificare.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | Directorul de ieșire personalizat pentru traducerea textului. Căile relative se rezolvă în raport cu fiecare rădăcină. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Mai multe rădăcini care partajează aceleași setări de ieșire. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Perechi explicite `(root_dir, translations_dir)`. Au prioritate față de `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Referință Git folosită pentru a limita revizuirea la fișierele sursă modificate. |
| `output_format` | `str` | `"text"` | Formatul de ieșire al revizuirii. Valorile acceptate sunt `"text"` și `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Tratează avertismentele ca și eșecuri pe lângă erori. |
| `debug` | `bool` | `False` | Activează înregistrarea de depanare. |
| `save_logs` | `bool` | `False` | Salvează fișierele jurnal la nivel DEBUG în directorul `logs/` din rădăcină. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Cerințe de configurare

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

## Observații privind comportamentul

- Content translation APIs keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content needs project-relative links adjusted for a target location.
- Project orchestration APIs add project behavior around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` prints progress and estimate summaries through Click, matching the CLI user experience.
- `dry_run=True` computes estimates using virtual README updates, but does not write the README or translation files.
- `groups` are processed sequentially. A single aggregate estimate is printed before work begins.
- When image translation is selected, missing Vision configuration raises an error before translation starts.
- Existing alias-based language folders are detected and can be migrated to canonical language folder names as part of the run.
- `run_review` fails on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` reports missing local Markdown and image link targets as warnings by default.

## Cale internă de apel

The API delegates to the same core implementation used by the CLI:

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

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Clasă | Modul | Responsabilitate |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Coordonează traducerea la nivel de proiect, gestionarea directoarelor, normalizarea metadatelor pe limbă și delegarea către traducători pentru Markdown, notebook-uri și imagini. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Execută munca asincronă de procesare a fișierelor pentru Markdown, notebook-uri, imagini, detectarea fișierelor învechite și actualizări ale metadatelor de traducere. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orchestrează citirile fișierelor Markdown, traducerea conținutului, rescrierea căilor, metadatele, declarațiile de exonerare și scrierile. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orchestrează citirile fișierelor notebook, traducerea celulelor Markdown, rescrierea căilor, metadatele, declarațiile de exonerare și scrierile. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orchestrează descoperirea imaginilor sursă, traducerea imaginilor, căile de ieșire, metadatele și scrierile. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Găsește perechile de Markdown traduse, evaluează calitatea traducerii și citește metadatele de încredere pentru fluxuri de lucru de reparare a traducerilor cu încredere scăzută. |
| `ReviewRunner` | `co_op_translator.review.runner` | Coordonează verificările deterministe de revizuire pe fișierele sursă, limbile țintă și rădăcinile de traducere configurate. |
| `ReviewTarget` | `co_op_translator.review.targets` | Descrie o rădăcină sursă și directorul de ieșire al traducerii revizuit pentru acea rădăcină. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Detectează foldere de limbă legacy bazate pe aliasuri și pregătește planuri de migrare către nume canonice de foldere BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Încarcă fișiere `.env` și verifică dacă furnizorii LLM necesari și furnizorii Vision opționali sunt configurați. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Detectează automat Azure OpenAI sau OpenAI, validează variabilele de mediu necesare și rulează verificări de conectivitate pentru furnizor. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Detectează configurația Azure AI Vision și rulează verificări de conectivitate pentru traducerea imaginilor. |