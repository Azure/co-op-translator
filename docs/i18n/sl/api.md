# Python API

Stabilen javni Python API je izvezen iz `co_op_translator.api`. Večina integracij uporablja enega od teh potekov:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Vaša aplikacija bere izvorno vsebino, kliče Co-op Translator za prevod in odloči, kam shraniti rezultat. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Vaš MCP gostitelj ali aplikacijski model bo prevajal kose, medtem ko Co-op Translator upravlja razbitje na kose in rekonstrukcijo. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Želite, da se Python API obnaša kot CLI in upravlja odkrivanje, izhodne poti, metapodatke, čiščenje in zapise. | `run_translation` |

Večina nižjenivojskih modulov pod `core`, `config`, `review` in `utils` so implementacijski detajli, ki jih uporabljajo ti API vstopni punkti.

MCP klienti uporabljajo isti javni API preko [MCP Server](mcp.md). Uporabite to stran, ko kličete Python neposredno, in MCP vodnik, ko izpostavljate Co-op Translator agentu ali urejevalniku. Če se odločate med CLI, Python API in MCP, začnite z [Choose Your Workflow](workflows.md).

## Začetni potek uporabe API

Začnite tukaj, če kličete Co-op Translator iz Python kode:

1. Konfigurirajte ponudnika LLM, kot je opisano v [Configuration](configuration.md), razen če samo pripravljate Markdown ali notebook kose za prevajanje z gostiteljskim agentom.
2. Odločite, ali vaša aplikacija upravlja datotečni I/O.
3. Uporabite vsebinski API, ko vaša aplikacija bere in piše posamezne datoteke.
4. Uporabite `run_translation`, ko naj Co-op Translator obdela repozitorij kot CLI.
5. Uporabite `run_review` po prevajanju, če potrebujete deterministične preglede v avtomatizaciji.

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

Uporabite ta potek, ko že imate datoteko, vsebino urejevalnika, notebook payload, MCP zahtevo ali vhod iz prilagojenega cevovoda. Vaša koda upravlja datotečni I/O:

1. Preberite izvorno vsebino.
2. Pokličite API za prevajanje vsebine.
3. Po želji pokličite API za prepisovanje poti, če bo prevedena vsebina zapisana v projektno prevajalsko mapo.
4. Shranite ali vrnite rezultat iz vaše aplikacije.

API-ji za prevajanje vsebine ne izvajajo odkrivanja projekta, ne zapišejo metapodatkov, ne dodajo izjav o strojni prevodi in samodejno ne prepisujejo povezav.

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

Če prevedeni Markdown ne bo živel v postavitvi projekta Co-op Translator, preskočite `rewrite_markdown_paths` in shranite prevedeni niz neposredno.

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

`translate_notebook_content` prevaja Markdown celice in ohranja ne-Markdown celice. Prepisovanje poti se uporablja samo za Markdown celice.

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

`translate_image_content` prebere izvorno sliko in vrne renderirano `PIL.Image.Image`. Ne zapisuje prevedenih metapodatkov slike.

## Scenario 2: Translate an Entire Repository

Uporabite ta potek, ko želite, da se Python API obnaša kot `translate` CLI. `run_translation` odkrije podprte datoteke, prevede izbrane vrste vsebin, prepiše poti, zapiše izhodne datoteke, posodobi metapodatke in izvede naloge vzdrževanja prevajanja, kot je čiščenje.

`run_translation` je priporočen vstopni prikaz za orkestracijo projektov. `translate_project` je izvezen kot združljivostni alias z enakim vedenjem.

Prevedite Markdown datoteke v trenutnem repozitoriju v korejščino in japonščino:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Prevedite samo zvezke iz določenega korena projekta:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Predogled obsega prevajanja brez zapisovanja datotek:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Prevedite več korenov vsebine v enem klicu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Zapišite prevode v eksplicitne izhodne skupine:

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

Uporabite nadomestni znak na jezik za primer, ko naj vsak jezik vsebuje gnezdeno podmapo:

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

Če nobeden od `markdown`, `notebook`, ali `images` ni nastavljen, API prevede vse podprte tipe: Markdown, notebooks in slike.

## Review Translated Output

`run_review` izvaja deterministične preverbe prevajanja brez LLM ali Vision poverilnic.

!!! note "Beta"
    `run_review` je beta deterministični pregledni API. Ne kliče ponudnikov modelov ali ne zapisuje datotek, vendar se sheme preverjanja in poročil lahko razvijejo.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Preglejte samo datoteke, spremenjene glede na osnovni ref, in natisnite izhod v GitHub formatu:

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

Prevedite Markdown vsebino brez zapisovanja datotek:

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

Prevedite in prepišite Markdown povezave:

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

Prevedite repozitorij iz Pythona:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Prevedite več korenov:

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

Ohranite izraze iz glosarja:

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

API-ji za prevajanje vsebine so namenjeni integracijam, ki že imajo vsebino v pomnilniku, kot so vtičnik urejevalnika, MCP orodje, procesor zvezkov ali prilagojen cevovod.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Prevede samo Markdown vsebino. Ne prepisuje povezav, ne zapisuje metapodatkov in ne dodaja izjav. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Prevede Markdown celice in ohrani ne-Markdown celice. Ne prepisuje povezav, ne zapisuje metapodatkov in ne dodaja izjav. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Izvleče in prevede besedilo na sliki, nato vrne renderirano sliko. Ne shrani prevedenih metapodatkov slike. |

`translate_markdown_content` in `translate_notebook_content` sprejmeta opcijsko `source_path` prek svojih možnosti. Pot se posreduje kot kontekst prevajalcu; klicalci so še vedno odgovorni za kakršnokoli projektno-specifično prepisovanje poti po prevodu.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Iste možnosti je mogoče posredovati kot slovarje:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

API-ji s podporo agenta ne kličejo Azure OpenAI ali OpenAI iz Co-op Translator. Pripravijo Markdown ali notebook kose za gostiteljskega agenta, da jih prevede, nato rekonstruirajo končno vsebino iz prevedenih kosov.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Vrne samostojen Markdown job s kosi, pozivi in stanjem za rekonstrukcijo. |
| `finish_markdown_agent_translation` | Rekonstruira Markdown iz joba in prevedenih kosov host-agenta. |
| `start_notebook_agent_translation` | Vrne notebook job z Markdown-celičnimi kosi za prevod s strani host-agenta. |
| `finish_notebook_agent_translation` | Rekonstruira notebook JSON in ohrani kode, izhode in metapodatke. |

Ta potek je predvsem namenjen MCP gostiteljem. Če potrebujete produkcijsko prevajanje repozitorija, kjer Co-op Translator upravlja klice ponudnikov, uporabite `translate_markdown_content`, `translate_notebook_content` ali `run_translation`.

## Path Rewriting APIs

API-ji za prepisovanje poti ne izvajajo prevajanja. Posodobijo povezave in polja frontmatter po tem, ko imajo klicalci informacije o izvorni poti, prevedeni ciljni poti in postavitvi projekta.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Prepiše Markdown povezave in podprta frontmatter polja poti za preveden cilj. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Uporabi prepisovanje Markdown poti na vsako Markdown celico in pusti ne-Markdown celice nespremenjene. |

Argument `policy` je lahko slovar s temi polji:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Ciljna koda jezika, npr. `"ko"` ali `"pt-BR"`. |
| `root_dir` | No | Izvorni koren projekta. Privzeto `"."`. |
| `translations_dir` | No | Izhodna mapa za prevedeno besedilo. Privzeto `translations` znotraj `root_dir`. |
| `translated_images_dir` | No | Izhodna mapa za prevedene slike. Privzeto `translated_images` znotraj `root_dir`. |
| `translation_types` | No | Omogočene vrste prevodov. Privzeto Markdown, notebooks in slike. |
| `lang_subdir` | No | Opcijska podmapa znotraj vsake jezikovne mape. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Ciljne kode jezikov, ločene s presledki, npr. `"ko ja fr"`, ali `"all"`. Alias kode se normalizirajo v kanonične BCP 47 vrednosti. |
| `root_dir` | `str` | `"."` | Koren projekta za en cilj prevoda. Ignorirano, ko so podani `root_dirs` ali `groups`. |
| `update` | `bool` | `False` | Izbriše in ponovno ustvari obstoječe prevode za izbrane jezike. |
| `images` | `bool` | `False` | Vključi prevajanje slik. Zahteva konfiguracijo Azure AI Vision. |
| `markdown` | `bool` | `False` | Vključi prevajanje Markdown. |
| `notebook` | `bool` | `False` | Vključi prevajanje Jupyter notebookov. |
| `debug` | `bool` | `False` | Omogoči debug beleženje. |
| `save_logs` | `bool` | `False` | Shrani DEBUG nivo log datotek v korensko mapo `logs/`. |
| `yes` | `bool` | `True` | Samodejno potrdi pozive za programatično in CI uporabo. |
| `add_disclaimer` | `bool` | `False` | Doda izjave o strojnih prevodih v prevedene Markdown in notebooke. |
| `translations_dir` | `str \| None` | `None` | Prilagojena izhodna mapa za prevod besedila. Relativne poti se rešujejo glede na vsak koren. |
| `image_dir` | `str \| None` | `None` | Prilagojena izhodna mapa za prevedene slike. Relativne poti se rešujejo glede na vsak koren. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Več korenov, ki delijo iste izhodne nastavitve. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Izrecne `(root_dir, translations_dir)` pare. Ima prednost pred `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL repozitorija, uporabljen pri upodobitvi navodil tabele jezikov v README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Izrazi iz glosarja, ki naj se ohranijo med prevajanjem. Duplicirani in prazni izrazi se normalizirajo. |
| `dry_run` | `bool` | `False` | Ocenite obseg prevajanja in predogled vedenja migracije brez zapisovanja datotek. |

## Review Parameters

`run_review` namerno zrcali podpis `run_translation`, kjer je mogoče, tako da lahko avtomatizacija preklaplja med prevodnim in preglednim potekom z minimalnim vejami.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Ciljne jezikovne mape za pregled. Sprejemajo se stringi, ločeni s presledki, in iterable. `"all"` pregleda vsak odkrit prevodni jezik. |
| `root_dir` | `str` | `"."` | Koren projekta za en cilj pregleda. Ignorirano, ko so podani `root_dirs` ali `groups`. |
| `markdown` | `bool` | `False` | Vključi izvorne Markdown in MDX datoteke. |
| `notebook` | `bool` | `False` | Vključi Jupyter notebook izvorne datoteke. |
| `images` | `bool` | `False` | Rezervirano za vzporednost z možnostmi prevajanja. Referenčne povezave do slik se preverijo iz Markdown. |
| `translations_dir` | `str \| None` | `None` | Prilagojen imenik za izhod prevedenega besedila. Relativne poti se rešujejo glede na vsak koren. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Več korenov, ki delijo iste nastavitve izhoda. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Jasno določeni `(root_dir, translations_dir)` pari. Ima prednost pred `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref, uporabljen za omejitev pregleda na spremenjene izvorne datoteke. |
| `output_format` | `str` | `"text"` | Format izhoda pregleda. Podprte vrednosti so `"text"` in `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Obravnava opozorila kot neuspehe poleg napak. |
| `debug` | `bool` | `False` | Omogoči debug zapisovanje. |
| `save_logs` | `bool` | `False` | Shrani dnevniške datoteke nivoja DEBUG v korenski imenik `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Configuration Requirements

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

## Behavior Notes

- Content translation APIs keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content needs project-relative links adjusted for a target location.
- Project orchestration APIs add project behavior around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` prints progress and estimate summaries through Click, matching the CLI user experience.
- `dry_run=True` computes estimates using virtual README updates, but does not write the README or translation files.
- `groups` are processed sequentially. A single aggregate estimate is printed before work begins.
- When image translation is selected, missing Vision configuration raises an error before translation starts.
- Existing alias-based language folders are detected and can be migrated to canonical language folder names as part of the run.
- `run_review` fails on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` reports missing local Markdown and image link targets as warnings by default.

## Internal Call Path

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

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Usmerja prevajanje na ravni projekta, upravljanje imenikov, normalizacijo metapodatkov po jezikih in delegiranje na prevajalce za Markdown, zvezke in slike. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Izvaja asinhrono obdelavo datotek za Markdown, zvezke, slike, zaznavanje zastarelosti in posodobitve metapodatkov prevoda. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestrira branje Markdown datotek, prevod vsebine, prepisovanje poti, metapodatke, izjave o omejitvi odgovornosti in zapisovanje. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestrira branje zvezkov, prevod Markdown celic, prepisovanje poti, metapodatke, izjave o omejitvi odgovornosti in zapisovanje. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestrira odkrivanje izvornih slik, prevod slik, izhodne poti, metapodatke in zapisovanje. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Najde pare prevedenih Markdown datotek, oceni kakovost prevoda in prebere metapodatke o zaupanju za delovne tokove popravil z nizkim zaupanjem. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinira deterministične preglede čez izvorne datoteke, ciljne jezike in konfigurirane prevajalske korene. |
| `ReviewTarget` | `co_op_translator.review.targets` | Opisuje izvorni koren in mapo z izhodom prevoda, ki se preverja za ta koren. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Zazna zastarele alias jezikovne mape in pripravi načrte migracije v kanonične BCP 47 mape. |
| `Config` | `co_op_translator.config.base_config` | Naloži `.env` datoteke in preveri, ali so zahtevani LLM in neobvezni Vision ponudniki konfigurirani. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Samodejno zazna Azure OpenAI ali OpenAI, preveri zahtevane spremenljivke okolja in izvede preizkuse povezljivosti ponudnika. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Zazna konfiguracijo Azure AI Vision in izvede preizkuse povezljivosti za prevajanje slik. |