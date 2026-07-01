# Python API

De stabiele publieke Python-API wordt geëxporteerd uit `co_op_translator.api`. De meeste integraties gebruiken een van deze workflows:

| Scenario | Gebruik dit wanneer | Belangrijkste API's |
| --- | --- | --- |
| Translate individual files or documents | Uw applicatie leest de broninhoud, roept Co-op Translator aan voor vertaling en bepaalt waar het resultaat wordt opgeslagen. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Uw MCP-host of applicatiemodel vertaalt de stukken, terwijl Co-op Translator het opdelen en opnieuw samenstellen afhandelt. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | U wilt dat de Python-API zich gedraagt als de CLI en discovery, uitvoerpaden, metadata, cleanup en schrijfbewerkingen afhandelt. | `run_translation` |

De meeste onderliggende modules in `core`, `config`, `review` en `utils` zijn implementatiedetails die door deze API-entrypoints worden gebruikt.

MCP-clients gebruiken dezelfde publieke API via de [MCP Server](mcp.md). Gebruik deze pagina bij rechtstreeks aanroepen vanuit Python, en de MCP-gids wanneer u Co-op Translator aan een agent of editor blootstelt. Als u moet kiezen tussen CLI, Python API en MCP, begin dan met [Kies Uw Workflow](workflows.md).

## Eerste gebruik van de API

Begin hier als u Co-op Translator vanuit Python-code aanroept:

1. Configureer een LLM-provider zoals beschreven in [Configuratie](configuration.md), tenzij u alleen Markdown- of notebook-chunks voorbereidt voor host-agent-vertaling.
2. Bepaal of uw applicatie verantwoordelijk is voor bestands-I/O.
3. Gebruik content-API's wanneer uw applicatie individuele bestanden leest en schrijft.
4. Gebruik `run_translation` wanneer Co-op Translator een repository moet verwerken zoals de CLI.
5. Gebruik `run_review` na vertaling als u deterministische controles in automatisering nodig hebt.

| Doel | Aan te roepen API |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenario 1: Translate Individual Files or Documents

Gebruik deze workflow wanneer u al een bestand, editorbuffer, notebook-payload, MCP-verzoek of aangepaste pipeline-invoer hebt. Uw code is verantwoordelijk voor bestands-I/O:

1. Lees de broninhoud.
2. Roep een content-vertalings-API aan.
3. Optioneel: roep een pad-herschrijf-API aan als de vertaalde inhoud in een projectvertaalmappenstructuur moet worden geschreven.
4. Sla het resultaat op of retourneer het vanuit uw applicatie.

De contentvertalings-API's voeren geen projectdiscovery uit, schrijven geen metadata, voegen geen disclaimers toe en herschrijven links niet automatisch.

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

Als de vertaalde Markdown niet in een Co-op Translator-projectlayout komt te staan, sla `rewrite_markdown_paths` over en bewaar de vertaalde string rechtstreeks.

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

`translate_notebook_content` vertaalt Markdown-cellen en behoudt niet-Markdown-cellen. Het herschrijven van paden wordt alleen toegepast op Markdown-cellen.

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

`translate_image_content` leest de bronafbeelding en retourneert een gerenderde `PIL.Image.Image`. Het schrijft geen vertaald afbeeldingsmetadata.

## Scenario 2: Translate an Entire Repository

Gebruik deze workflow wanneer u wilt dat de Python-API zich gedraagt als de `translate` CLI. `run_translation` ontdekt ondersteunde bestanden, vertaalt geselecteerde inhoudstypen, herschrijft paden, schrijft uitvoerbestanden, werkt metadata bij en voert vertaalonderhoudstaken uit zoals cleanup.

`run_translation` is het aanbevolen entrypoint voor projectorchestratie. `translate_project` wordt geëxporteerd als een compatibiliteitsalias met hetzelfde gedrag.

Vertaal Markdown-bestanden in de huidige repository naar Koreaans en Japans:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Vertaal alleen notebooks vanaf een specifieke projectroot:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Bekijk het vertaalvolume zonder bestanden te schrijven:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Vertaal meerdere inhoudsroots in één aanroep:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Schrijf vertalingen naar expliciete uitvoergroepen:

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

Gebruik een per-taal plaatsaanduiding wanneer elke taal een geneste submap moet bevatten:

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

Als geen van `markdown`, `notebook` of `images` is ingesteld, vertaalt de API alle ondersteunde types: Markdown, notebooks en images.

## Review Translated Output

`run_review` voert deterministische vertaalcontroles uit zonder LLM- of Vision-referenties.

!!! note "Bèta"
    `run_review` is een bèta-deterministische review-API. Het roept geen modelproviders aan of schrijft bestanden, maar controles en issue-schema's kunnen evolueren.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Beoordeel alleen bestanden die veranderd zijn ten opzichte van een baseref en print GitHub-geformatteerde output:

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

## Kopieer-plak API-voorbeelden

Vertaal Markdown-inhoud zonder bestandsopslaan:

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

Vertaal en herschrijf Markdown-links:

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

Vertaal een repository vanuit Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Vertaal meerdere roots:

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

Behoud woordenlijsttermen:

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

## Publieke toegangspunten

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

## API's voor contentvertaling

API's voor contentvertaling zijn bedoeld voor integraties die inhoud al in het geheugen hebben, zoals een editor-extensie, MCP-tool, notebook-processor of aangepaste pipeline.

| Functie | Invoer | Uitvoer | Bestands-I/O | Opmerkingen |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Nee | Asynchroon. Vertaalt alleen Markdown-inhoud. Het herschrijft geen links, schrijft geen metadata en voegt geen disclaimers toe. |
| `translate_notebook_content` | Notebook JSON `str` of `dict` | Notebook JSON `str` | Nee | Asynchroon. Vertaalt Markdown-cellen en behoudt niet-Markdown-cellen. Het herschrijft geen links, schrijft geen metadata en voegt geen disclaimers toe. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Leest alleen bronafbeelding | Synchroon. Extraheert en vertaalt tekst uit de afbeelding en retourneert vervolgens een gerenderde afbeelding. Het slaat geen vertaalde afbeeldingsmetadata op. |

`translate_markdown_content` en `translate_notebook_content` accepteren een optioneel `source_path` via hun opties. Het pad wordt als context aan de vertaler doorgegeven; aanroepen blijven verantwoordelijk voor eventuele project-specifieke padherschrijving na vertaling.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Dezelfde opties kunnen als dictionaries worden doorgegeven:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-geassisteerde vertaal-API's

Agent-geassisteerde API's roepen Azure OpenAI of OpenAI niet vanuit Co-op Translator aan. Ze bereiden Markdown- of notebook-chunks voor om door een host-agent vertaald te worden en reconstrueren vervolgens de uiteindelijke inhoud uit de vertaalde chunks.

| Functie | Doel |
| --- | --- |
| `start_markdown_agent_translation` | Retourneer een self-contained Markdown-job met chunks, prompts en reconstructiestatus. |
| `finish_markdown_agent_translation` | Herstel Markdown uit een job en door de host-agent vertaalde chunks. |
| `start_notebook_agent_translation` | Retourneer een notebook-job met Markdown-celchunks voor host-agentvertaling. |
| `finish_notebook_agent_translation` | Reconstrueer notebook-JSON terwijl codecellen, outputs en metadata behouden blijven. |

Deze workflow is voornamelijk bedoeld voor MCP-hosts. Als u productierepositoryvertaling nodig hebt waarbij Co-op Translator provider-aanroepen beheert, gebruik dan `translate_markdown_content`, `translate_notebook_content` of `run_translation`.

## API's voor padherschrijving

API's voor padherschrijving voeren geen vertaling uit. Ze werken links en frontmatter-paden bij nadat aanroepen het bronpad, het vertaalde doelpad en de projectlayout kennen.

| Functie | Omvang | Opmerkingen |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body en frontmatter | Herschrijft Markdown-links en ondersteunde frontmatter-padvelden voor een vertaalde target. |
| `rewrite_notebook_paths` | Markdown-cellen in notebook-JSON | Past Markdown-pad-herschrijving toe op elke Markdown-cel en laat niet-Markdown-cellen ongewijzigd. |

Het `policy`-argument kan een dictionary zijn met deze velden:

| Veld | Vereist | Doel |
| --- | --- | --- |
| `language_code` | Ja | Doeltaalcode, zoals `"ko"` of `"pt-BR"`. |
| `root_dir` | Nee | Bronprojectroot. Standaard `"."`. |
| `translations_dir` | Nee | Uitvoermap voor tekstvertalingen. Standaard `translations` onder `root_dir`. |
| `translated_images_dir` | Nee | Uitvoermap voor vertaalde afbeeldingen. Standaard `translated_images` onder `root_dir`. |
| `translation_types` | Nee | Ingeschakelde vertaaltypes. Standaard Markdown, notebooks en afbeeldingen. |
| `lang_subdir` | Nee | Optionele submap onder elke taalmmap. |

## Projectvertalingsparameters

| Parameter | Type | Standaard | Doel |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Taalcodes voor de doeltalen, gescheiden door spaties, zoals `"ko ja fr"`, of `"all"`. Aliascodes worden genormaliseerd naar canonieke BCP 47-waarden. |
| `root_dir` | `str` | `"."` | Projectroot voor een enkele vertaalknop. Wordt genegeerd wanneer `root_dirs` of `groups` zijn opgegeven. |
| `update` | `bool` | `False` | Verwijder en maak bestaande vertalingen voor de geselecteerde talen opnieuw aan. |
| `images` | `bool` | `False` | Inclusief afbeeldingsvertaling. Vereist Azure AI Vision-configuratie. |
| `markdown` | `bool` | `False` | Inclusief Markdown-vertaling. |
| `notebook` | `bool` | `False` | Inclusief Jupyter-notebookvertaling. |
| `debug` | `bool` | `False` | Schakel debug-logging in. |
| `save_logs` | `bool` | `False` | Sla DEBUG-niveau logbestanden op in de hoofdmap `logs/`. |
| `yes` | `bool` | `True` | Automatisch prompts bevestigen voor geautomatiseerd en CI-gebruik. |
| `add_disclaimer` | `bool` | `False` | Voeg machinevertalingsdisclaimers toe aan vertaalde Markdown en notebooks. |
| `translations_dir` | `str \| None` | `None` | Aangepaste uitvoermap voor tekstvertalingen. Relatieve paden worden ten opzichte van elke root opgelost. |
| `image_dir` | `str \| None` | `None` | Aangepaste uitvoermap voor vertaalde afbeeldingen. Relatieve paden worden ten opzichte van elke root opgelost. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Meerdere roots die dezelfde uitvoerinstellingen delen. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Expliciete `(root_dir, translations_dir)`-paren. Heeft prioriteit boven `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository-URL die wordt gebruikt bij het weergeven van de README-taaltabel. |
| `glossaries` | `Iterable[str] \| None` | `None` | Woordenlijsttermen die tijdens de vertaling behouden moeten blijven. Duplicaten en lege termen worden genormaliseerd. |
| `dry_run` | `bool` | `False` | Schat het vertaalvolume en bekijkt migratiegedrag zonder bestanden te schrijven. |

## Review-parameters

`run_review` weerspiegelt opzettelijk waar mogelijk de `run_translation`-handtekening, zodat automatisering gemakkelijk kan schakelen tussen vertaal- en reviewworkflows met minimale vertakkingen.

| Parameter | Type | Standaard | Doel |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Doel-taalmappen om te reviewen. Spatie-gescheiden strings en iterables worden geaccepteerd. `"all"` reviewt elke ontdekte vertaaltalenmap. |
| `root_dir` | `str` | `"."` | Projectroot voor een enkele reviewtarget. Wordt genegeerd wanneer `root_dirs` of `groups` zijn opgegeven. |
| `markdown` | `bool` | `False` | Inclusief Markdown- en MDX-bronbestanden. |
| `notebook` | `bool` | `False` | Inclusief Jupyter-notebookbronbestanden. |
| `images` | `bool` | `False` | Gereserveerd voor pariteit met vertaalopties. Linkverwijzingen naar afbeeldingen worden gecontroleerd vanuit Markdown. |
| `translations_dir` | `str \| None` | `None` | Aangepaste uitvoermap voor tekstvertalingen. Relatieve paden worden ten opzichte van elke root opgelost. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Meerdere roots die dezelfde uitvoerinstellingen delen. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Expliciete `(root_dir, translations_dir)`-paren. Gaat boven `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-ref gebruikt om de review te beperken tot gewijzigde bronbestanden. |
| `output_format` | `str` | `"text"` | Opmaak van de reviewuitvoer. Ondersteunde waarden zijn `"text"` en `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Behandel waarschuwingen als mislukkingen naast fouten. |
| `debug` | `bool` | `False` | Schakel debug-logging in. |
| `save_logs` | `bool` | `False` | Sla DEBUG-logbestanden op in de rootmap `logs/`. |

Als geen van `markdown`, `notebook` of `images` is ingesteld, reviewt de API Markdown, notebooks en afbeeldingslinkverwijzingen waar van toepassing. De review roept geen LLM-provider aan en vereist geen API-sleutels.

## Configuratievereisten

Vertaal-API's die door providers worden ondersteund vereisen providerconfiguratie voordat ze kunnen vertalen:

- Markdown- en notebookvertaling vereisen een LLM-provider. Configureer ofwel Azure OpenAI of OpenAI.
- Afbeeldingsvertaling vereist naast de LLM-provider ook Azure AI Vision.
- `run_translation` voert lichte connectiviteitscontroles uit voordat de projectvertaling begint.
- Agent-ondersteunde `start_*_agent_translation` en `finish_*_agent_translation` API's roepen geen Co-op Translator LLM-providers aan. De hostapplicatie of MCP-agent vertaalt de voorbereide blokken.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` en `run_review` zijn deterministisch en vereisen geen providerreferenties.

Vereiste Azure OpenAI-variabelen:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Vereiste OpenAI-variabelen:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Vereiste Azure AI Vision-variabelen voor afbeeldingsvertaling:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` is deterministisch en vereist geen Azure OpenAI-, OpenAI- of Azure AI Vision-configuratie.

## Gedragsnotities

- Contentvertaling-API's scheiden vertaling van projecteelpad-herschrijving. Roep `rewrite_markdown_paths` of `rewrite_notebook_paths` expliciet aan wanneer vertaald inhoud projectrelatieve links moet laten aanpassen voor een doellocatie.
- Projectorchestratie-API's voegen projectgedrag toe rond inhoudsvertaling, inclusief het ontdekken van bestanden, schrijfbewerkingen, padherschrijving, metadata, opruiming en optionele disclaimers.
- `run_translation` toont voortgangs- en schattingssamenvattingen via Click, overeenkomstig de CLI-gebruikerservaring.
- `dry_run=True` berekent schattingen met behulp van virtuele README-updates, maar schrijft de README of vertaalbestanden niet weg.
- `groups` worden sequentieel verwerkt. Eén enkele geaggregeerde schatting wordt afgedrukt voordat het werk begint.
- Wanneer afbeeldingsvertaling is geselecteerd, veroorzaakt het ontbreken van Vision-configuratie een fout voordat de vertaling begint.
- Bestaande op aliassen gebaseerde taalmappen worden gedetecteerd en kunnen als onderdeel van de uitvoering naar canonieke taalmappennamen worden gemigreerd.
- `run_review` faalt bij ontbrekende vertaalde bestanden, ontbrekende of verouderde vertaalmetadata, onjuiste Markdown-frontmatter/code-fences en ongeldig vertaald notebook-JSON.
- `run_review` rapporteert ontbrekende lokale Markdown- en afbeeldingslinkdoelen standaard als waarschuwingen.

## Interne aanroeproute

De API delegeert aan dezelfde kernimplementatie die door de CLI wordt gebruikt:

Vertaling:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` voor vertaling in het geheugen.
2. `co_op_translator.api.translation.rewrite_markdown_paths` of `rewrite_notebook_paths` voor expliciete padnabehandeling.
3. `co_op_translator.api.translation.run_translation` voor volledige projectorchestratie.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Gerichte projectvertalingsmixins voor Markdown, notebooks en afbeeldingen.
8. Markdown-, notebook-, tekst- en afbeeldingsvertalers onder `co_op_translator.core`.

Beoordeling:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministische controles onder `co_op_translator.review.checks`

De volgende klassen zijn nuttig voor onderhouders, maar worden niet geëxporteerd als de stabiele pakketniveau-API.

| Class | Module | Verantwoordelijkheid |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Coördineert projectniveauvertaling, mapbeheer, normalisatie van per-taal metadata en delegatie naar Markdown-, notebook- en afbeeldingsvertalers. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Voert het asynchrone bestandsverwerkingswerk uit voor Markdown, notebooks, afbeeldingen, detectie van verouderde bestanden en updates van vertaalmetadata. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestreert het lezen van Markdown-bestanden, inhoudsvertaling, padherschrijving, metadata, disclaimers en schrijfbewerkingen. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestreert het lezen van notebookbestanden, vertaling van Markdown-cellen, padherschrijving, metadata, disclaimers en schrijfbewerkingen. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestreert het ontdekken van bronafbeeldingen, afbeeldingsvertaling, uitvoerpaden, metadata en schrijfbewerkingen. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Vindt vertaalde Markdown-paren, beoordeelt de vertaalkwaliteit en leest vertrouwensmetadata voor herstelworkflows bij lage vertrouwensscore. |
| `ReviewRunner` | `co_op_translator.review.runner` | Coördineert deterministische reviewcontroles over bronbestanden, doeltalen en geconfigureerde vertaalroots. |
| `ReviewTarget` | `co_op_translator.review.targets` | Beschrijft een bronroot en de vertaaluitvoermap die voor die root wordt beoordeeld. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Detecteert verouderde alias-taalmappen en bereidt migratieplannen voor naar canonieke BCP 47-mappen. |
| `Config` | `co_op_translator.config.base_config` | Laadt `.env`-bestanden en controleert of vereiste LLM- en optionele Vision-providers zijn geconfigureerd. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Detecteert automatisch Azure OpenAI of OpenAI, valideert vereiste omgevingsvariabelen en voert connectiviteitscontroles voor providers uit. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Detecteert Azure AI Vision-configuratie en voert connectiviteitscontroles uit voor afbeeldingsvertaling. |