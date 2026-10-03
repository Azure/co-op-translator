# Python API

De stabiele openbare Python-API wordt geëxporteerd vanuit `co_op_translator.api`. De meeste integraties gebruiken een van deze workflows:

| Scenario | Gebruik dit wanneer | Belangrijkste API's |
| --- | --- | --- |
| Translate individual files or documents | Uw toepassing leest de broninhoud, roept Co-op Translator aan voor vertaling, en beslist waar het resultaat wordt opgeslagen. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Inhoud voorbereiden voor vertaling door host-agent | Uw MCP-host of toepassingsmodel vertaalt de chunks, terwijl Co-op Translator het opdelen in chunks en de reconstructie verzorgt. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | U wilt dat de Python-API zich gedraagt als de CLI en ontdekking, uitvoerpaden, metadata, opschonen en schrijfbewerkingen afhandelt. | `run_translation` |

De meeste lagere modules onder `core`, `config`, `review`, en `utils` zijn implementatiedetails die door deze API-toegangspunten worden gebruikt.

MCP-clients gebruiken dezelfde openbare API via de [MCP-server](mcp.md). Gebruik deze pagina wanneer u Python rechtstreeks aanroept, en de MCP-gids wanneer u Co-op Translator aan een agent of editor blootstelt. Als u moet kiezen tussen CLI, Python API en MCP, begin dan met [Kies uw workflow](workflows.md).

## Eerste API-stroom

Begin hier als u Co-op Translator vanuit Python-code aanroept:

1. Configureer een LLM-provider zoals beschreven in [Configuratie](configuration.md), tenzij u alleen Markdown- of notebook-chunks voorbereidt voor vertaling door een host-agent.
2. Bepaal of uw toepassing verantwoordelijk is voor bestands-I/O.
3. Gebruik content-API's wanneer uw toepassing individuele bestanden leest en schrijft.
4. Gebruik `run_translation` wanneer Co-op Translator een repository moet verwerken zoals de CLI.
5. Gebruik `run_review` na vertaling als u deterministische controles in automatisering nodig hebt.

| Doel | API om mee te beginnen |
| --- | --- |
| Vertaal één Markdown-tekenreeks of bestand | `translate_markdown_content` |
| Vertaal één notebook-payload | `translate_notebook_content` |
| Vertaal één afbeelding | `translate_image_content` |
| Laat een host-agent Markdown- of notebook-chunks vertalen | `start_markdown_agent_translation` of `start_notebook_agent_translation` |
| Herschrijf vertaalde links nadat u een uitvoerpad hebt gekozen | `rewrite_markdown_paths` of `rewrite_notebook_paths` |
| Vertaal een volledige repository | `run_translation` |
| Beoordeel vertaalde output | `run_review` |

## Scenario 1: Vertaal individuele bestanden of documenten

Gebruik deze workflow wanneer u al een bestand, editorbuffer, notebook-payload, MCP-verzoek of aangepaste pijplijninvoer hebt. Uw code is verantwoordelijk voor bestands-I/O:

1. Lees de broninhoud.
2. Roep een content-vertalings-API aan.
3. Roep optioneel een pad-herschrijf-API aan als de vertaalde inhoud in een projectvertalingsmap wordt weggeschreven.
4. Sla het resultaat op of geef het terug vanuit uw toepassing.

De content-vertalings-API's voeren geen projectontdekking uit, schrijven geen metadata, voegen geen disclaimers toe en herschrijven links niet automatisch.

### Markdown-bestand

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

Als de vertaalde Markdown niet in een Co-op Translator projectstructuur komt te staan, sla `rewrite_markdown_paths` over en sla de vertaalde tekenreeks direct op.

### Notebook-bestand

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

`translate_notebook_content` vertaalt Markdown-cellen en behoudt niet-Markdown-cellen. Pad-herschrijving wordt alleen toegepast op Markdown-cellen.

### Afbeeldingsbestand

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

`translate_image_content` leest de bronafbeelding en retourneert een gerenderde `PIL.Image.Image`. Het schrijft geen vertaalde afbeeldingsmetadata weg.

## Scenario 2: Vertaal een volledige repository

Gebruik deze workflow wanneer u wilt dat de Python-API zich gedraagt als de `translate` CLI. `run_translation` ontdekt ondersteunde bestanden, vertaalt geselecteerde inhoudstypen, herschrijft paden, schrijft uitvoerbestanden, werkt metadata bij en voert onderhoudstaken voor vertaling uit zoals opschonen.

`run_translation` is het aanbevolen toegangspunt voor projectorchestratie. `translate_project` wordt geëxporteerd als een compatibiliteitsalias met hetzelfde gedrag.

Vertaal Markdown-bestanden in de huidige repository naar Koreaans en Japans:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Vertaal alleen notebooks uit een specifiek projectroot:

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

Registreer gestructureerde voortgangsevenementen voor een integratie:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Sla de payload op in uw job-eventtabel of stream deze naar uw gebruikersinterface.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Evenementen gebruiken het geversioneerde schema `co-op.translation.event.v1`. Integraties zouden
moeten afhangen van stabiele velden zoals `type` en `stage_key`, niet van gebruikersgerichte
consoletekst of `stage_label`.

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

Gebruik een per-taal-plaatsaanduiding wanneer elke taal een geneste submap moet bevatten:

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

Als geen van `markdown`, `notebook` of `images` is ingesteld, vertaalt de API alle ondersteunde typen: Markdown, notebooks en afbeeldingen.

### Behoud geaccepteerde bewerkingen door mensen met een TranslationStateProvider

Standaard behoudt Co-op Translator het bestaande bestandsniveaugedrag: wanneer een
Markdownbron verouderd is, wordt het volledige vertaalde bestand opnieuw gegenereerd. Gehoste
integraties kunnen optioneel een `TranslationStateProvider` doorgeven om menselijke
bewerkingen in bronblokken die niet zijn gewijzigd, te behouden.

De provider levert het laatst geaccepteerde bron/doel-paar en registreert elke nieuwe
kandidaat. Acceptatie blijft de verantwoordelijkheid van de integratie—bijvoorbeeld,
nadat een vertaal-pullrequest is samengevoegd:

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

Voor Markdown-bestanden met een geldige geaccepteerde basislijn lijnt Co-op Translator
Markdown-blokken op het hoogste niveau uit. Ongewijzigde bronblokken hergebruiken de huidige vertaalde
blokken, inclusief door mensen gemaakte bewerkingen; gewijzigde of toegevoegde bronblokken worden
voor vertaling verzonden; verwijderde bronblokken worden verwijderd. Als uitlijning onduidelijk is,
de doelstructuur is veranderd, een blokvertaling ongeldig is, of er geen basislijn is
beschikbaar, valt Co-op Translator veilig terug op het bestaande volledige-bestand
vertaalpad.

Deze API slaat documentvertalingsstatus op, niet een documentoverstijgend frase- of
segmentvertalingsgeheugen. Het geldt momenteel voor Markdown-projectvertaling.
Notebook- en afbeeldingsgedrag blijven ongewijzigd. Het doorgeven van `update=True`
vraagt nog steeds volledige regeneratie aan.

Als één of meer bestanden niet vertaald kunnen worden, geeft `run_translation` een
`RuntimeError` nadat de projectworkflow is voltooid in plaats van een
succesvolle run met ontbrekende uitvoer te rapporteren. Integraties moeten dit als een mislukte
taak behandelen en de vorige geaccepteerde vertaalstatus behouden.

## Beoordeel vertaalde output

`run_review` voert deterministische vertalingscontroles uit zonder LLM- of Vision-referenties.

!!! note "Bèta"
    `run_review` is een bètaversie van een deterministische review-API. Het roept geen modelproviders aan of schrijft bestanden, maar controles en issue-schema's kunnen evolueren.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Na een alleen-README-vertaling gebruikt u dezelfde scope voor beoordeling:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` controleert alleen `README.md` onder elke geconfigureerde bronroot,
inclusief aangepaste `groups` en uitvoermappen. Andere documenten en geneste
READMEs worden uitgesloten. Een ontbrekende bron-README veroorzaakt een `ValueError`; mislukte
vertaalcontroles geven een `RuntimeError`.

Controleer alleen bestanden die zijn gewijzigd ten opzichte van een baseref en druk uitvoer in GitHub-formaat af:

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

## Copy-paste API-voorbeelden

Vertaal Markdown-inhoud zonder bestanden te schrijven:

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

Behoud glossariumtermen:

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

## Content-vertalings-API's

Content-vertalings-API's zijn bedoeld voor integraties die al inhoud in het geheugen hebben, zoals een editorextensie, MCP-tool, notebookprocessor of aangepaste pijplijn.

| Functie | Invoer | Uitvoer | Bestands-I/O | Opmerkingen |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Nee | Asynchroon. Vertaalt alleen Markdown-inhoud. Het herschrijft geen links, schrijft geen metadata en voegt geen disclaimers toe. |
| `translate_notebook_content` | Notebook JSON `str` of `dict` | Notebook JSON `str` | Nee | Asynchroon. Vertaalt Markdown-cellen en behoudt niet-Markdown-cellen. Het herschrijft geen links, schrijft geen metadata en voegt geen disclaimers toe. |
| `translate_image_content` | Afbeeldingspad | `PIL.Image.Image` | Leest alleen de bronafbeelding | Synchroon. Extraheert en vertaalt afbeeldingstekst en retourneert vervolgens een gerenderde afbeelding. Het slaat geen vertaalde afbeeldingsmetadata op. |

`translate_markdown_content` en `translate_notebook_content` accepteren een optionele `source_path` via hun opties. Het pad wordt als context aan de vertaler doorgegeven; aanroepers blijven verantwoordelijk voor project-specifieke pad-herschrijving na vertaling.

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

## Agent-geassisteerde vertalings-API's

Agent-geassisteerde API's roepen de geconfigureerde LLM-provider van Co-op Translator niet aan. Ze bereiden Markdown- of notebook-chunks voor die door een host-agent vertaald moeten worden en reconstrueren vervolgens de uiteindelijke inhoud uit de vertaalde chunks.

| Functie | Doel |
| --- | --- |
| `start_markdown_agent_translation` | Geeft een zelfstandige Markdown-taak terug met chunks, prompts en reconstructiestatus. |
| `finish_markdown_agent_translation` | Reconstrueer Markdown uit een taak en door de host-agent vertaalde chunks. |
| `start_notebook_agent_translation` | Geeft een notebook-taak terug met Markdown-cel-chunks voor vertaling door een host-agent. |
| `finish_notebook_agent_translation` | Reconstrueer notebook JSON terwijl codecellen, outputs en metadata behouden blijven. |

Deze workflow is voornamelijk bedoeld voor MCP-hosts. Als u vertaling van repositories in productie nodig hebt waarbij Co-op Translator provider-aanroepen beheert, gebruik dan `translate_markdown_content`, `translate_notebook_content` of `run_translation`.

## Pad-herschrijvings-API's

Pad-herschrijvings-API's voeren geen vertaling uit. Ze werken links en frontmatter-paden bij nadat aanroepers het bronpad, het vertaalde doelpad en de projectindeling kennen.

| Functie | Reikwijdte | Opmerkingen |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown-body en frontmatter | Herschrijft Markdown-links en ondersteunde frontmatter-padvelden voor een vertaald doel. |
| `rewrite_notebook_paths` | Markdown-cellen in notebook JSON | Past Markdown-pad-herschrijving toe op elke Markdown-cel en laat niet-Markdown-cellen ongewijzigd. |

Het `policy`-argument kan een dictionary zijn met deze velden:

| Veld | Vereist | Doel |
| --- | --- | --- |
| `language_code` | Ja | Doeltaalcode, zoals `"ko"` of `"pt-BR"`. |
| `root_dir` | Nee | Bronprojectroot. Standaard `"."`. |
| `translations_dir` | Nee | Uitvoermap voor tekstvertalingen. Standaard `translations` onder `root_dir`. |
| `translated_images_dir` | Nee | Uitvoermap voor vertaalde afbeeldingen. Standaard `translated_images` onder `root_dir`. |
| `translation_types` | Nee | Ingeschakelde vertaaltypen. Standaard Markdown, notebooks en afbeeldingen. |
| `lang_subdir` | Nee | Optionele submap onder elke taalmap. |

## Projectvertalingsparameters

| Parameter | Type | Standaard | Doel |
| --- | --- | --- | --- |
| `language_codes` | `str` | Vereist | Met spaties gescheiden doeltaalcodes, zoals `"ko ja fr"`, of `"all"`. Alias-codes worden genormaliseerd naar canonieke BCP 47-waarden. |
| `root_dir` | `str` | `"."` | Projectroot voor één vertaalsdoel. Wordt genegeerd wanneer `root_dirs` of `groups` zijn opgegeven. |
| `update` | `bool` | `False` | Verwijder en maak bestaande vertalingen opnieuw aan voor de geselecteerde talen. |
| `images` | `bool` | `False` | Inclusief afbeeldingsvertaling. Vereist Azure AI Vision-configuratie. |
| `markdown` | `bool` | `False` | Inclusief Markdown-vertaling. |
| `notebook` | `bool` | `False` | Inclusief Jupyter-notebookvertaling. |
| `debug` | `bool` | `False` | Schakel debug-logging in. |
| `save_logs` | `bool` | `False` | Sla DEBUG-niveau logbestanden op onder de rootmap `logs/`. |
| `yes` | `bool` | `True` | Bevestig prompts automatisch voor programmatisch en CI-gebruik. |
| `add_disclaimer` | `bool` | `False` | Voeg machinevertalingsdisclaimers toe aan vertaalde Markdown-bestanden en notebooks. |
| `translations_dir` | `str \| None` | `None` | Aangepaste uitvoermap voor tekstvertalingen. Relatieve paden worden ten opzichte van elke root opgelost. |
| `image_dir` | `str \| None` | `None` | Aangepaste uitvoermap voor vertaalde afbeeldingen. Relatieve paden worden ten opzichte van elke root opgelost. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Meerdere roots die dezelfde uitvoerinstellingen delen. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Expliciete `(root_dir, translations_dir)`-paren. Hebben voorrang op `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository-URL die wordt gebruikt bij het genereren van de README-taaltabel. |
| `glossaries` | `Iterable[str] \| None` | `None` | Woordenlijsttermen die tijdens vertaling behouden moeten blijven. Duplicaten en lege termen worden genormaliseerd. |
| `dry_run` | `bool` | `False` | Schat de hoeveelheid vertaling en bekijk het migratiegedrag zonder bestanden weg te schrijven. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Optionele persistentie-adapter voor accepted-baseline en kandidaat bij incrementele Markdown-updates. Het weglaten ervan behoudt het bestaande volledige-bestandsgedrag. |

## Beoordelingsparameters

`run_review` weerspiegelt opzettelijk waar mogelijk de handtekening van `run_translation`, zodat automatisering met minimale vertakkingen tussen vertaal- en reviewworkflows kan schakelen.

| Parameter | Type | Standaard | Doel |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Doel-taalmappen om te controleren. Spatie-gescheiden strings en iterables worden geaccepteerd. `"all"` controleert elke ontdekte doeltaal. |
| `root_dir` | `str` | `"."` | Project-root voor een enkel reviewdoel. Wordt genegeerd wanneer `root_dirs` of `groups` zijn opgegeven. |
| `markdown` | `bool` | `False` | Inclusief Markdown- en MDX-bronbestanden. |
| `notebook` | `bool` | `False` | Inclusief Jupyter-notebook-bronbestanden. |
| `images` | `bool` | `False` | Gereserveerd voor pariteit met vertaalopties. Linkreferenties naar afbeeldingen worden vanuit Markdown gecontroleerd. |
| `translations_dir` | `str \| None` | `None` | Aangepaste uitvoermap voor tekstvertalingen. Relatieve paden worden ten opzichte van elke root opgelost. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Meerdere roots die dezelfde uitvoerinstellingen delen. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Expliciete `(root_dir, translations_dir)`-paren. Hebben voorrang op `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-ref die wordt gebruikt om de review te beperken tot gewijzigde bronbestanden. |
| `readme_only` | `bool` | `False` | Controleer alleen `README.md` onder elke bronroot. Een ontbrekende bron-README veroorzaakt `ValueError`. |
| `output_format` | `str` | `"text"` | Uitvoerformaat van de review. Ondersteunde waarden zijn `"text"` en `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Behandel waarschuwingen naast fouten ook als mislukkingen. |
| `debug` | `bool` | `False` | Schakel debuglogging in. |
| `save_logs` | `bool` | `False` | Sla logbestanden op DEBUG-niveau op in de hoofdmap `logs/`. |

Als geen van `markdown`, `notebook` of `images` is ingesteld, beoordeelt de API Markdown, notebooks en afbeeldingslinkreferenties waar van toepassing. De review roept geen LLM-provider aan en vereist geen API-sleutels.

## Configuratievereisten

Door een provider ondersteunde vertaal-API's vereisen providerconfiguratie voordat er vertaald wordt:

- Voor het vertalen van Markdown en notebooks is een LLM-provider vereist. Configureer Azure OpenAI, OpenAI of Anthropic.
- Voor beeldvertaling is naast de LLM-provider ook Azure AI Vision vereist.
- `run_translation` voert lichte connectiviteitscontroles uit voordat de projectvertaling begint.
- Agent-ondersteunde `start_*_agent_translation` en `finish_*_agent_translation` APIs roepen geen Co-op Translator LLM-providers aan. De host-applicatie of MCP-agent vertaalt de voorbereide stukken.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, en `run_review` zijn deterministisch en vereisen geen providerreferenties.

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

Vereiste Anthropic-variabelen:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` en `ANTHROPIC_MAX_TOKENS` zijn optioneel. Microsoft Agent Framework is de standaard modelclient voor alle providers vanaf Co-op Translator 0.22.0. Semantic Kernel kan tijdelijk nog steeds geselecteerd worden met `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, maar het doen hiervan genereert een deprecatie-waarschuwing; zie [configuratie](configuration.md#model-client-backend) voor het gefaseerde verwijderingsplan.

Vereiste Azure AI Vision-variabelen voor beeldvertaling:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` is deterministisch en vereist geen LLM- of Azure AI Vision-configuratie.

## Gedragsopmerkingen

- Content-translation-API's houden vertaling gescheiden van het herschrijven van projectpaden. Roep `rewrite_markdown_paths` of `rewrite_notebook_paths` expliciet aan wanneer vertaalde inhoud projectrelatieve links voor een doellocatie moet aanpassen.
- Project-orchestratie-API's voegen projectgedrag toe rond contentvertaling, inclusief bestandsdetectie, schrijfbewerkingen, pad-herschrijving, metadata, opruiming en optionele disclaimers.
- `run_translation` toont voortgangs- en schattingssamenvattingen via dezelfde Rich-ondersteunde reporter die door de CLI wordt gebruikt. Niet-interactieve output valt terug op platte tekst.
- `dry_run=True` berekent schattingen met behulp van virtuele README-updates, maar schrijft de README of vertaalbestanden niet weg.
- `groups` worden sequentieel verwerkt. Een enkele geaggregeerde schatting wordt afgedrukt voordat het werk begint.
- Wanneer beeldvertaling is geselecteerd, veroorzaakt het ontbreken van Vision-configuratie een fout voordat de vertaling begint.
- Bestaande alias-gebaseerde taalmappen worden gedetecteerd en kunnen tijdens het uitvoeren worden gemigreerd naar canonieke taalmappennamen.
- `run_review` faalt bij ontbrekende vertaalde bestanden, ontbrekende of verouderde vertaalmetadata, onjuist gevormde Markdown-frontmatter/code-fences en ongeldig vertaald notebook-JSON.
- `run_review` rapporteert standaard ontbrekende lokale Markdown- en afbeeldingslinkdoelen als waarschuwingen.

## Interne aanroeproute

De API delegeert aan dezelfde kernimplementatie die door de CLI wordt gebruikt:

Vertaling:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, of `translate_image_content` voor in-memory vertaling.
2. `co_op_translator.api.translation.rewrite_markdown_paths` of `rewrite_notebook_paths` voor expliciete pad-nabewerking.
3. `co_op_translator.api.translation.run_translation` voor volledige projectorchestratie.
4. `co_op_translator.config.Config`, `LLMConfig` en `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Gefocuste projectvertalingsmixins voor Markdown, notebooks en afbeeldingen.
8. Markdown-, notebook-, tekst- en beeldvertalers onder `co_op_translator.core`.

Beoordeling:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministische controles onder `co_op_translator.review.checks`

De volgende klassen zijn nuttig voor onderhouders, maar worden niet geëxporteerd als de stabiele package-level API.

| Klasse | Module | Verantwoordelijkheid |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Coördineert vertalingen op projectniveau, mapbeheer, normalisatie van per-taal metadata en delegatie naar Markdown-, notebook- en beeldvertalers. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Voert het asynchrone bestandverwerkingswerk uit voor Markdown, notebooks, afbeeldingen, verouderingsdetectie en updates van vertaalmetadata. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestreert het lezen van Markdown-bestanden, inhoudsvertaling, pad-herschrijving, metadata, disclaimers en schrijfbewerkingen. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestreert het lezen van notebookbestanden, vertaling van Markdown-cellen, pad-herschrijving, metadata, disclaimers en schrijfbewerkingen. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestreert bronafbeeldingsdetectie, beeldvertaling, uitvoerpaden, metadata en schrijfbewerkingen. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Vindt vertaalde Markdown-paren, evalueert vertaalkwaliteit en leest betrouwbaarheidsmetadata voor reparatieworkflows met lage betrouwbaarheid. |
| `ReviewRunner` | `co_op_translator.review.runner` | Coördineert deterministische reviewcontroles over bronbestanden, doeltalen en geconfigureerde vertaalroots. |
| `ReviewTarget` | `co_op_translator.review.targets` | Beschrijft een bronroot en de vertaaluitvoermap die voor die root wordt beoordeeld. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Detecteert legacy alias-taalmappen en bereidt migratieplannen voor naar canonieke BCP 47-mappen. |
| `Config` | `co_op_translator.config.base_config` | Laadt `.env`-bestanden en controleert of vereiste LLM- en optionele Vision-providers zijn geconfigureerd. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Detecteert automatisch Azure OpenAI, OpenAI of Anthropic, valideert vereiste omgevingsvariabelen en voert connectiviteitscontroles voor providers uit. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Detecteert Azure AI Vision-configuratie en voert connectiviteitscontroles uit voor beeldvertaling. |