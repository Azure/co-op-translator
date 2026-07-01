# Python API

Stabilni javni Python API izvezen je iz `co_op_translator.api`. Većina integracija koristi jedan od ovih tijekova rada:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

Većina niže razine modula pod `core`, `config`, `review` i `utils` su implementacijski detalji koje koriste ove API ulazne točke.

MCP klijenti koriste isti javni API putem [MCP poslužitelj](mcp.md). Upotrijebite ovu stranicu kada pozivate Python izravno, a MCP vodič kada izlažete Co-op Translator agentu ili uređivaču. Ako odlučujete između CLI-ja, Python API-ja i MCP-a, započnite s [Choose Your Workflow](workflows.md).

## First-Time API Flow

Započnite ovdje ako pozivate Co-op Translator iz Python koda:

1. Konfigurirajte pružatelja LLM-a kako je opisano u [Configuration](configuration.md), osim ako samo pripremate Markdown ili notebook komade za prijevod od strane host-agenta.
2. Odlučite hoće li vaša aplikacija upravljati datotečnim ulazom/izlazom.
3. Koristite content API-je kad vaša aplikacija čita i zapisuje pojedinačne datoteke.
4. Koristite `run_translation` kada Co-op Translator treba obraditi repozitorij poput CLI-ja.
5. Koristite `run_review` nakon prijevoda ako trebate determinističke provjere u automatizaciji.

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

Upotrijebite ovaj tijek rada kada već imate datoteku, sadržaj uređivača, notebook payload, MCP zahtjev ili prilagođeni ulaz u cjevovodu. Vaš kôd upravlja datotečnim I/O-om:

1. Pročitajte izvorni sadržaj.
2. Pozovite API za prevođenje sadržaja.
3. Po želji pozovite API za prepisivanje putanja ako će prevedeni sadržaj biti zapisan u mapu projekta za prijevod.
4. Spremite ili vratite rezultat iz vaše aplikacije.

API-ji za prevođenje sadržaja ne pokreću otkrivanje projekta, ne pišu metapodatke, ne dodaju odricanja i ne prepisuju poveznice automatski.

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

Ako prevedeni Markdown neće biti smješten u strukturi projekta Co-op Translator, preskočite `rewrite_markdown_paths` i spremite prevedeni niz izravno.

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

`translate_notebook_content` prevodi Markdown ćelije i zadržava ne-Markdown ćelije. Prepisivanje putanja primjenjuje se samo na Markdown ćelije.

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

`translate_image_content` čita izvorni image i vraća renderiranu `PIL.Image.Image`. Ne zapisuje metapodatke prevedene slike.

## Scenario 2: Translate an Entire Repository

Upotrijebite ovaj tijek rada kada želite da se Python API ponaša poput `translate` CLI-ja. `run_translation` otkriva podržane datoteke, prevodi odabrane tipove sadržaja, prepisuje putanje, zapisuje izlazne datoteke, ažurira metapodatke i obavlja zadatke održavanja prijevoda poput čišćenja.

`run_translation` je preferirana ulazna točka za orkestraciju projekta. `translate_project` je izvezen kao alias za kompatibilnost s istim ponašanjem.

Prevedite Markdown datoteke u trenutnom repozitoriju na korejski i japanski:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Prevedite samo notebooke iz određenog root projekta:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Pregledajte obujam prijevoda bez zapisivanja datoteka:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Prevedite više korijenskih mapa u jednom pozivu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Zapišite prijevode u eksplicitne izlazne grupe:

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

Koristite placeholder po jeziku kada svaki jezik treba sadržavati ugniježđeni poddirektorij:

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

Ako nijedan od `markdown`, `notebook`, ili `images` nije postavljen, API prevodi sve podržane tipove: Markdown, notebooke i slike.

## Review Translated Output

`run_review` pokreće determinističke provjere prijevoda bez LLM ili Vision vjerodajnica.

!!! note "Beta"
    `run_review` je beta deterministički review API. Ne poziva pružatelje modela niti zapisuje datoteke, ali provjere i sheme problema se mogu mijenjati.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Pregledajte samo datoteke promijenjene u odnosu na osnovni ref i ispišite izlaz u GitHub-flavored formatu:

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

Prevedite Markdown sadržaj bez zapisivanja datoteka:

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

Prevedite i prepišite Markdown poveznice:

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

Prevedite više rootova:

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

Sačuvajte pojmove iz rječnika:

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

API-ji za prevođenje sadržaja namijenjeni su integracijama koje već imaju sadržaj u memoriji, poput ekstenzije uređivača, MCP alata, procesora notebooka ili prilagođenog cjevovoda.

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

Iste opcije mogu se proslijediti kao rječnici:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

API-ji s pomoću agenta ne pozivaju Azure OpenAI ili OpenAI iz Co-op Translatora. Oni pripremaju Markdown ili notebook komade za host-agenta da ih prevede, a zatim rekonstruiraju konačni sadržaj iz prevedenih komada.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return a self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from a job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return a notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while preserving code cells, outputs, and metadata. |

Ovaj tijek rada je uglavnom namijenjen MCP hostovima. Ako vam treba produkcijski prijevod repozitorija s Co-op Translatorom koji upravlja pozivima pružatelja, koristite `translate_markdown_content`, `translate_notebook_content`, ili `run_translation`.

## Path Rewriting APIs

API-ji za prepisivanje putanja ne obavljaju prijevod. Ažuriraju poveznice i frontmatter putanje nakon što pozivatelji znaju izvorni put, prevedeni cilj i strukturu projekta.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Rewrites Markdown links and supported frontmatter path fields for a translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Applies Markdown path rewriting to each Markdown cell and leaves non-Markdown cells unchanged. |

Argument `policy` može biti rječnik s ovim poljima:

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

`run_review` namjerno oponaša potpis `run_translation` gdje je moguće kako bi automatizacija mogla prelaziti između tijekova prijevoda i pregleda s minimalnim grananjem.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | Prilagođeni izlazni direktorij za prijevod teksta. Relativne putanje se rješavaju u odnosu na svaki root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Više rootova koji dijele iste izlazne postavke. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Eksplicitni `(root_dir, translations_dir)` parovi. Imaju prednost nad `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref koji se koristi za ograničavanje pregleda na promijenjene izvorne datoteke. |
| `output_format` | `str` | `"text"` | Format izlaza pregleda. Podržane vrijednosti su `"text"` i `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Smatraj upozorenja kao neuspjehe pored pogrešaka. |
| `debug` | `bool` | `False` | Omogući debug logiranje. |
| `save_logs` | `bool` | `False` | Spremi DEBUG-level log datoteke u root direktorij `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Zahtjevi za konfiguraciju

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

## Napomene o ponašanju

- API-ji za prevođenje sadržaja drže prijevod odvojenim od prepisivanja putanja projekta. Pozovite `rewrite_markdown_paths` ili `rewrite_notebook_paths` eksplicitno kada prevedeni sadržaj zahtijeva prilagodbu projektno-relativnih poveznica za ciljnu lokaciju.
- API-ji za orkestraciju projekta dodaju projektno ponašanje oko prevođenja sadržaja, uključujući otkrivanje datoteka, upis datoteka, prepisivanje putanja, metapodatke, čišćenje i opcionalne izjave o odricanju odgovornosti.
- `run_translation` ispisuje sažetke napretka i procjena putem Click-a, usklađeno s CLI korisničkim iskustvom.
- `dry_run=True` izračunava procjene koristeći virtualne izmjene README-a, ali ne zapisuje README niti datoteke prijevoda.
- `groups` se obrađuju sekvencijalno. Jedna zbirna procjena ispisuje se prije početka rada.
- Kada je odabrano prevođenje slika, nedostajuća Vision konfiguracija izaziva grešku prije početka prevođenja.
- Postojeće mape jezika temeljene na aliasima detektiraju se i mogu se migrirati u kanonična imena mapa jezika kao dio izvođenja.
- `run_review` prijavljuje pogrešku za nedostajuće prevedene datoteke, nedostajuće ili zastarjele metapodatke prijevoda, neispravno oblikovan Markdown frontmatter/code fence-ove i nevažeći prevedeni notebook JSON.
- `run_review` prijavljuje nedostajuće lokalne Markdown i ciljeve poveznica slika kao upozorenja po zadanim postavkama.

## Interni pozivni put

The API delegates to the same core implementation used by the CLI:

Prevođenje:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Pregled:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

Sljedeće klase su korisne za održavatelje, ali nisu izvezene kao stabilni API na razini paketa.

| Klasa | Modul | Odgovornost |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinira prevođenje na razini projekta, upravljanje direktorijima, normalizaciju metapodataka po jeziku i delegiranje na prevoditelje za Markdown, notebook i slike. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Izvodi asinhroni rad obrade datoteka za Markdown, bilježnice, slike, otkrivanje zastarjelosti i ažuriranje metapodataka prijevoda. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestrira čitanje Markdown datoteka, prevođenje sadržaja, prepisivanje putanja, metapodatke, izjave o odricanju i upise. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestrira čitanje notebook datoteka, prevođenje Markdown-celija, prepisivanje putanja, metapodatke, izjave o odricanju i upise. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestrira otkrivanje izvornih slika, prevođenje slika, izlazne putanje, metapodatke i upise. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Pronalaženje prevedenih parova Markdown datoteka, procjena kvalitete prijevoda i čitanje metapodataka o povjerenju za tijekove rada popravaka niske pouzdanosti. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinira determinističke provjere pregleda kroz izvorne datoteke, ciljne jezike i konfigurirane root direktorije prijevoda. |
| `ReviewTarget` | `co_op_translator.review.targets` | Opisuje izvornu root i izlazni direktorij prijevoda koji se pregledava za taj root. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Detektira naslijeđene mape jezika temeljene na aliasima i priprema planove migracije u kanonična imena mapa BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Učitava `.env` datoteke i provjerava jesu li potrebni LLM i opcionalni Vision provideri konfigurirani. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Automatski otkriva Azure OpenAI ili OpenAI, validira potrebne varijable okruženja i izvodi provjere povezanosti providera. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Detektira konfiguraciju Azure AI Vision i izvodi provjere povezanosti za prevođenje slika. |