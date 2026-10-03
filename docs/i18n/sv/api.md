# Python-API

Den stabila offentliga Python-API:n exporteras från `co_op_translator.api`. De flesta integrationer använder ett av dessa arbetsflöden:

| Scenario | Använd detta när | Huvud-API:er |
| --- | --- | --- |
| Översätt enskilda filer eller dokument | Din applikation läser källinnehållet, anropar Co-op Translator för översättning och bestämmer var resultatet ska sparas. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Förbered innehåll för värdagent-översättning | Din MCP-värd eller applikationsmodell kommer att översätta bitar, medan Co-op Translator hanterar uppdelning och rekonstruktion. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Översätt ett helt repository | Du vill att Python-API:t ska bete sig som CLI:t och hantera filupptäckt, utdata-sökvägar, metadata, städning och filskrivningar. | `run_translation` |

De flesta lägre nivåmoduler under `core`, `config`, `review` och `utils` är implementeringsdetaljer som används av dessa API-ingångspunkter.

MCP-klienter använder samma publika API via [MCP-servern](mcp.md). Använd den här sidan när du anropar Python direkt, och MCP-guiden när du exponerar Co-op Translator för en agent eller redigerare. Om du ska välja mellan CLI, Python-API och MCP, börja med [Välj ditt arbetsflöde](workflows.md).

## Förstagångsflöde för API

Börja här om du anropar Co-op Translator från Python-kod:

1. Konfigurera en LLM-leverantör enligt beskrivningen i [Configuration](configuration.md), om du inte bara förbereder Markdown- eller notebook-delar för värdagentöversättning.
2. Avgör om din applikation ansvarar för fil-I/O.
3. Använd innehålls-API:er när din applikation läser och skriver enskilda filer.
4. Använd `run_translation` när Co-op Translator ska bearbeta ett repository som CLI:t.
5. Använd `run_review` efter översättning om du behöver deterministiska kontroller i automatisering.

| Mål | API att börja med |
| --- | --- |
| Översätt en Markdown-sträng eller fil | `translate_markdown_content` |
| Översätt en notebook-payload | `translate_notebook_content` |
| Översätt en bild | `translate_image_content` |
| Låt en värdagent översätta Markdown- eller notebook-delar | `start_markdown_agent_translation` eller `start_notebook_agent_translation` |
| Skriv om översatta länkar efter att ha valt en utdata-sökväg | `rewrite_markdown_paths` eller `rewrite_notebook_paths` |
| Översätt ett helt repository | `run_translation` |
| Granska översatt utdata | `run_review` |

## Scenario 1: Översätt enskilda filer eller dokument

Använd detta arbetsflöde när du redan har en fil, en editor-buffer, en notebook-payload, en MCP-förfrågan eller en egen pipelineingång. Din kod ansvarar för fil-I/O:

1. Läs källinnehållet.
2. Anropa ett innehållsöversättnings-API.
3. Valfritt: anropa ett sökvägsskrivnings-API om det översatta innehållet ska skrivas till en projektöversättningsmapp.
4. Spara eller returnera resultatet från din applikation.

Innehållsöversättnings-API:erna kör inte projektdetektering, skriver inte metadata, lägger inte till ansvarsfriskrivningar och skriver inte om länkar automatiskt.

### Markdown-fil

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

Om den översatta Markdown-filen inte kommer att ligga i ett Co-op Translator-projektupplägg, hoppa över `rewrite_markdown_paths` och spara den översatta strängen direkt.

### Notebook-fil

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

`translate_notebook_content` översätter Markdown-celler och bevarar icke-Markdown-celler. Sökvägsskrivning tillämpas endast på Markdown-celler.

### Bildfil

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

`translate_image_content` läser källbilden och returnerar en renderad `PIL.Image.Image`. Den skriver inte översatt bildmetadata.

## Scenario 2: Översätt ett helt repository

Använd detta arbetsflöde när du vill att Python-API:et ska bete sig som `translate`-CLI:t. `run_translation` upptäcker stödjade filer, översätter valda innehållstyper, skriver om sökvägar, skriver ut filer, uppdaterar metadata och utför översättningsunderhållsåtgärder såsom städning.

`run_translation` är den föredragna ingångspunkten för projekthantering. `translate_project` exporteras som ett kompatibilitetsalias med samma beteende.

Översätt Markdown-filer i det aktuella repositoryt till koreanska och japanska:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Översätt endast notebooks från ett specifikt projektrot:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Förhandsgranska översättningsvolymen utan att skriva filer:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Spela in strukturerade framstegshändelser för en integration:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Spara nyttolasten i din jobbhändelsetabell eller strömma den till ditt användargränssnitt.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Händelser använder det versionsstyrda schemat `co-op.translation.event.v1`. Integrationer bör
bero på stabila fält som `type` och `stage_key`, inte på användarvänlig
konsoltext eller `stage_label`.

Översätt flera källrötter i ett anrop:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Skriv översättningar till explicita utdata-grupper:

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

Använd en språkvis platshållare när varje språk ska innehålla en inbäddad undermapp:

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

Om ingen av `markdown`, `notebook` eller `images` är aktiverad, översätter API:et alla stödjade typer: Markdown, notebooks och bilder.

### Bevara accepterade mänskliga redigeringar med en översättningsstatusleverantör

Som standard bevarar Co-op Translator sitt befintliga filnivåbeteende: när en
Markdown-källa är föråldrad genereras hela den översatta filen på nytt. Hostade
integrationer kan valfritt skicka en `TranslationStateProvider` för att bevara mänskliga
redigeringar i källblock som inte har ändrats.

Leverantören tillhandahåller det senaste accepterade källa/mål-paret och registrerar varje ny
kandidat. Godkännande förblir integrationens ansvar—till exempel,
efter att en översättnings-pull request har mergats:

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

För Markdown-filer med en giltig accepterad baslinje, justerar Co-op Translator
toppnivå Markdown-block. Oförändrade källblock återanvänder de nuvarande översatta
blocken, inklusive ändringar gjorda av människor; ändrade eller tillagda källblock skickas
för översättning; borttagna källblock tas bort. Om justeringen är tvetydig,
målstrukturen ändrats, en blocköversättning är ogiltig, eller ingen baslinje är
tillgänglig, faller Co-op Translator säkert tillbaka till den befintliga helfilen
översättningsvägen.

Detta API lagrar dokumentöversättningsstatus, inte ett tvärdokumentellt fras-
segment-översättningsminne. Det gäller för närvarande Markdown-projekt
översättning. Notebook- och bildbeteende är oförändrat. Att skicka `update=True`
begär fortfarande full återgenerering.

Om en eller flera filer inte kan översättas, kastar `run_translation` ett
`RuntimeError` efter att projektarbetsflödet avslutats istället för att rapportera en
lyckad körning med saknat utdata. Integrationer bör behandla detta som ett misslyckat
jobb och behålla den tidigare accepterade översättningsstatusen.

## Granska översatt utdata

`run_review` kör deterministiska översättningskontroller utan LLM- eller Vision-behörigheter.

!!! note "Beta"
    `run_review` är ett beta deterministiskt gransknings-API. Det anropar inte modellleverantörer eller skriver filer, men kontroller och issue-scheman kan komma att förändras.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Efter en README-endast-översättning, använd samma omfattning för granskning:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` granskar endast `README.md` under varje konfigurerad källrot,
inklusive anpassade `groups` och utdata-kataloger. Andra dokument och inbäddade
README-filer utesluts. En saknad käll-README ger `ValueError`; misslyckade
översättningskontroller kastar `RuntimeError`.

Granska endast filer som ändrats mot en basref och skriv ut GitHub-stil utdata:

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

## API-exempel att kopiera/klistra in

Översätt Markdown-innehåll utan filskrivningar:

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

Översätt och skriv om Markdown-länkar:

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

Översätt ett repository från Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Översätt flera rötter:

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

Bevara ordlistetermer:

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

## Publika ingångspunkter

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

## Innehållsöversättnings-API:er

Innehållsöversättnings-API:er är avsedda för integrationer som redan har innehåll i minnet, såsom ett editor-tillägg, MCP-verktyg, notebook-processor eller en egen pipeline.

| Funktion | Inmatning | Utmatning | Fil-I/O | Noteringar |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Nej | Asynkront. Översätter endast Markdown-innehåll. Den skriver inte om länkar, skriver inte metadata eller lägger till ansvarsfriskrivningar. |
| `translate_notebook_content` | Notebook JSON `str` eller `dict` | Notebook JSON `str` | Nej | Asynkront. Översätter Markdown-celler och bevarar icke-Markdown-celler. Den skriver inte om länkar, skriver inte metadata eller lägger till ansvarsfriskrivningar. |
| `translate_image_content` | Bildsökväg | `PIL.Image.Image` | Läser endast källbilden | Synkront. Extraherar och översätter bildtext, sedan returnerar en renderad bild. Den sparar inte översatt bildmetadata. |

`translate_markdown_content` och `translate_notebook_content` accepterar en valfri `source_path` via sina options. Sökvägen skickas som kontext till översättaren; anroparna är fortfarande ansvariga för eventuell projektspecifik sökvägsskrivning efter översättning.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Samma options kan skickas som ordböcker:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agentassisterade översättnings-API:er

Agentassisterade API:er anropar inte den konfigurerade LLM-leverantören från Co-op Translator. De förbereder Markdown- eller notebook-delar för att en värdagent ska översätta, och rekonstruerar sedan det slutliga innehållet från de översatta delarna.

| Funktion | Syfte |
| --- | --- |
| `start_markdown_agent_translation` | Returnerar ett fristående Markdown-jobb med delar, prompts och rekonstruktionsstatus. |
| `finish_markdown_agent_translation` | Rekonstruerar Markdown från ett jobb och de av värdagenten översatta delarna. |
| `start_notebook_agent_translation` | Returnerar ett notebook-jobb med Markdown-cell-delar för värdagent-översättning. |
| `finish_notebook_agent_translation` | Rekonstruerar notebook-JSON samtidigt som kodceller, output och metadata bevaras. |

Detta arbetsflöde är huvudsakligen avsett för MCP-värdar. Om du behöver produktionens repository-översättning med Co-op Translator som hanterar leverantörsanrop, använd `translate_markdown_content`, `translate_notebook_content` eller `run_translation`.

## API:er för sökvägsskrivning

API:er för sökvägsskrivning utför ingen översättning. De uppdaterar länkar och frontmatter-sökvägar efter att anroparna känner till källsökvägen, den översatta målsökvägen och projektlayouten.

| Funktion | Område | Noteringar |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown-body och frontmatter | Skriver om Markdown-länkar och stödda frontmatter-sökvägsfält för ett översatt mål. |
| `rewrite_notebook_paths` | Markdown-celler i notebook-JSON | Tillämpa Markdown-sökvägsskrivning på varje Markdown-cell och lämnar icke-Markdown-celler oförändrade. |

Argumentet `policy` kan vara en ordbok med följande fält:

| Fält | Obligatoriskt | Syfte |
| --- | --- | --- |
| `language_code` | Ja | Målspråkskod, till exempel `"ko"` eller `"pt-BR"`. |
| `root_dir` | Nej | Projektrot för källan. Standard är `"."`. |
| `translations_dir` | Nej | Utgångskatalog för textöversättningar. Standard är `translations` under `root_dir`. |
| `translated_images_dir` | Nej | Utgångskatalog för översatta bilder. Standard är `translated_images` under `root_dir`. |
| `translation_types` | Nej | Aktiverade översättningstyper. Standard är Markdown, notebooks och bilder. |
| `lang_subdir` | Nej | Valfri undermapp under varje språk-mapp. |

## Parametrar för projektöversättning

| Parameter | Typ | Standard | Syfte |
| --- | --- | --- | --- |
| `language_codes` | `str` | Obligatoriskt | Målspråkskoder separerade med mellanslag, till exempel `"ko ja fr"`, eller `"all"`. Alias-koder normaliseras till kanoniska BCP 47-värden. |
| `root_dir` | `str` | `"."` | Projektrot för ett enskilt översättningsmål. Ignoreras när `root_dirs` eller `groups` anges. |
| `update` | `bool` | `False` | Ta bort och återskapa befintliga översättningar för de valda språken. |
| `images` | `bool` | `False` | Inkludera bildöversättning. Kräver Azure AI Vision-konfiguration. |
| `markdown` | `bool` | `False` | Inkludera Markdown-översättning. |
| `notebook` | `bool` | `False` | Inkludera Jupyter-notebook-översättning. |
| `debug` | `bool` | `False` | Aktivera debug-loggning. |
| `save_logs` | `bool` | `False` | Spara loggfiler på DEBUG-nivå i roten `logs/`-katalogen. |
| `yes` | `bool` | `True` | Bekräftar automatiskt uppmaningar för programmatisk användning och CI. |
| `add_disclaimer` | `bool` | `False` | Lägg till maskinöversättningsansvarsfriskrivningar i översatt Markdown och anteckningsböcker. |
| `translations_dir` | `str \| None` | `None` | Anpassad utmatningskatalog för textöversättningar. Relativa sökvägar löses i förhållande till varje rot. |
| `image_dir` | `str \| None` | `None` | Anpassad översatt bildutmatningskatalog. Relativa sökvägar löses i förhållande till varje rot. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Flera root-kataloger som delar samma utmatningsinställningar. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit angivna `(root_dir, translations_dir)`-par. Har företräde framför `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository-URL som används när README:s språktabell visas. |
| `glossaries` | `Iterable[str] \| None` | `None` | Termer i ordlista som ska bevaras under översättning. Dubbletter och tomma termer normaliseras. |
| `dry_run` | `bool` | `False` | Uppskatta översättningsvolym och förhandsgranska migreringsbeteende utan att skriva filer. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Valfri adapter för persistens av accepted-baseline och kandidater för inkrementella Markdown-uppdateringar. Om den utelämnas bevaras det befintliga beteendet med uppdateringar av hela filer. |

## Granskningsparametrar

`run_review` speglar avsiktligt `run_translation`-signaturen där det är möjligt så att automatisering kan byta mellan översättnings- och granskningsarbetsflöden med minimal villkorsförgrening.

| Parameter | Typ | Standard | Syfte |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Mål-språkmappar att granska. Mellanrum-separerade strängar och itererbara accepteras. `"all"` granskar alla upptäckta översättningsspråk. |
| `root_dir` | `str` | `"."` | Projektets rot för ett enda granskningsmål. Ignoreras när `root_dirs` eller `groups` anges. |
| `markdown` | `bool` | `False` | Inkludera Markdown- och MDX-källfiler. |
| `notebook` | `bool` | `False` | Inkludera Jupyter-notebookkällfiler. |
| `images` | `bool` | `False` | Reserverat för paritet med översättningsalternativ. Länkreferenser till bilder kontrolleras från Markdown. |
| `translations_dir` | `str \| None` | `None` | Anpassad utmatningskatalog för textöversättningar. Relativa sökvägar löses i förhållande till varje rot. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Flera root-kataloger som delar samma utmatningsinställningar. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit angivna `(root_dir, translations_dir)`-par. Har företräde framför `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-ref som används för att begränsa granskningen till ändrade källfiler. |
| `readme_only` | `bool` | `False` | Granska endast `README.md` under varje källrot. Ett saknat käll-README utlöser `ValueError`. |
| `output_format` | `str` | `"text"` | Utdataformat för granskning. Stödda värden är `"text"` och `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Behandla varningar som fel, i tillägg till redan förekommande fel. |
| `debug` | `bool` | `False` | Aktivera debug-loggning. |
| `save_logs` | `bool` | `False` | Spara DEBUG-nivå loggfiler under rotkatalogen `logs/`. |

Om ingen av `markdown`, `notebook` eller `images` är angiven, granskar API:et Markdown, notebooks och bildlänkreferenser där det är tillämpligt. Granskning anropar inte en LLM-leverantör och kräver inga API-nycklar.

## Konfigurationskrav

Provider-stödda översättnings-API:er kräver leverantörskonfiguration innan översättning:

- Markdown- och notebook-översättning kräver en LLM-leverantör. Konfigurera Azure OpenAI, OpenAI eller Anthropic.
- Bildöversättning kräver Azure AI Vision utöver LLM-leverantören.
- `run_translation` kör lätta anslutningskontroller innan projektöversättningen börjar.
- Agent-assisterade `start_*_agent_translation` och `finish_*_agent_translation` API:er anropar inte Co-op Translator LLM-leverantörer. Värdapplikationen eller MCP-agenten översätter de förberedda chunkarna.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, och `run_review` är deterministiska och kräver inga leverantörsbehörigheter.

Nödvändiga Azure OpenAI-variabler:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Nödvändiga OpenAI-variabler:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Nödvändiga Anthropic-variabler:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` och `ANTHROPIC_MAX_TOKENS` är valfria. Microsoft Agent Framework är standardmodellklienten för alla leverantörer från och med Co-op Translator 0.22.0. Semantic Kernel kan fortfarande väljas tillfälligt med `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, men att göra det utlöser en avvecklingsvarning; se [konfiguration](configuration.md#model-client-backend) för den etapperade borttagningsplanen.

Nödvändiga Azure AI Vision-variabler för bildöversättning:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` är deterministisk och kräver ingen LLM- eller Azure AI Vision-konfiguration.

## Anmärkningar om beteende

- Innehållsöversättnings-API:er håller översättning åtskild från projektvägsomskrivning. Anropa `rewrite_markdown_paths` eller `rewrite_notebook_paths` uttryckligen när översatt innehåll behöver projektrelativa länkar justerade för en målplats.
- Projektorkestrerings-API:er lägger till projektbeteende kring innehållsöversättning, inklusive filupptäckt, skrivningar, väg-omskrivning, metadata, städning och valfria ansvarsfriskrivningar.
- `run_translation` skriver ut status- och uppskattningssammanfattningar via samma Rich-baserade rapportör som används av CLI:n. I icke-interaktivt läge faller utdata tillbaka till ren text.
- `dry_run=True` beräknar uppskattningar med virtuella README-uppdateringar, men skriver inte README eller översättningsfilerna.
- `groups` behandlas sekventiellt. En enda aggregerad uppskattning skrivs ut innan arbetet börjar.
- När bildöversättning väljs, ger saknad Vision-konfiguration ett fel innan översättningen startar.
- Befintliga alias-baserade språkmappar upptäcks och kan migreras till kanoniska språkmappnamn som en del av körningen.
- `run_review` misslyckas vid saknade översatta filer, saknad eller föråldrad översättningsmetadata, felaktig Markdown-frontmatter/code-fences och ogiltig översatt notebook-JSON.
- `run_review` rapporterar saknade lokala Markdown- och bildlänkmål som varningar som standard.

## Intern anropsväg

API:et delegerar till samma kärnimplementering som används av CLI:n:

Översättning:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, eller `translate_image_content` för översättning i minnet.
2. `co_op_translator.api.translation.rewrite_markdown_paths` eller `rewrite_notebook_paths` för explicit efterbearbetning av sökvägar.
3. `co_op_translator.api.translation.run_translation` för fullständig projektorkestrering.
4. `co_op_translator.config.Config`, `LLMConfig`, och `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Fokuserade projektöversättnings-mixins för Markdown, notebooks och bilder.
8. Markdown-, notebook-, text- och bildöversättare under `co_op_translator.core`.

Granskning:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministiska kontroller under `co_op_translator.review.checks`

Följande klasser är användbara för underhållare, men exporteras inte som paketnivåns stabila API.

| Klass | Modul | Ansvar |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinerar översättning på projektnivå, kataloghantering, språkvis metadata-normalisering och delegering till Markdown-, notebook- och bildöversättare. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Utför det asynkrona filbearbetningsarbetet för Markdown, notebooks, bilder, detektion av åldrade filer och uppdateringar av översättningsmetadata. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestrerar läsning av Markdown-filer, innehållsöversättning, väg-omskrivning, metadata, ansvarsfriskrivningar och skrivningar. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestrerar läsning av notebook-filer, översättning av Markdown-celler, väg-omskrivning, metadata, ansvarsfriskrivningar och skrivningar. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestrerar upptäckt av källbilder, bildöversättning, utdata-sökvägar, metadata och skrivningar. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Hittar översatta Markdown-par, utvärderar översättningskvalitet och läser förtroendemetadata för reparationsarbetsflöden med låg förtroendegrad. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinerar deterministiska granskningskontroller över källfiler, målspråk och konfigurerade översättningsrötter. |
| `ReviewTarget` | `co_op_translator.review.targets` | Beskriver en källrot och översättningsutmatningskatalogen som granskas för den roten. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Upptäcker gamla aliasbaserade språkmappar och förbereder migrationsplaner för kanoniska BCP 47-mappar. |
| `Config` | `co_op_translator.config.base_config` | Laddar `.env`-filer och kontrollerar om erforderliga LLM- och valfria Vision-leverantörer är konfigurerade. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Autodetekterar Azure OpenAI, OpenAI eller Anthropic, validerar nödvändiga miljövariabler och kör anslutningskontroller för leverantören. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Upptäcker Azure AI Vision-konfiguration och kör anslutningskontroller för bildöversättning. |