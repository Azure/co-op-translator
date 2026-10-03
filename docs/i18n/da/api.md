# Python-API

Det stabile offentlige Python-API eksporteres fra `co_op_translator.api`. De fleste integrationer bruger en af disse arbejdsgange:

| Scenarie | Brug dette, når | Primære API'er |
| --- | --- | --- |
| Oversæt individuelle filer eller dokumenter | Din applikation læser kildens indhold, kalder Co-op Translator for at oversætte og beslutter, hvor resultatet gemmes. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Forbered indhold til host-agent-oversættelse | Din MCP-host eller applikationsmodel vil oversætte bidderne, mens Co-op Translator tager sig af opdeling og rekonstruktion. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Oversæt et helt repository | Du vil have Python-API'et til at opføre sig som CLI'en og håndtere opdagelse, outputstier, metadata, oprydning og filskrivninger. | `run_translation` |

De fleste lavniveaumoduler under `core`, `config`, `review` og `utils` er implementeringsdetaljer, der bruges af disse API-entrépunkter.

MCP-klienter bruger samme offentlige API via [MCP-serveren](mcp.md). Brug denne side når du kalder Python direkte, og MCP-guiden når du eksponerer Co-op Translator for en agent eller editor. Hvis du skal vælge mellem CLI, Python-API og MCP, start med [Vælg din arbejdsgang](workflows.md).

## Førstegangs API-flow

Start her, hvis du kalder Co-op Translator fra Python-kode:

1. Konfigurer en LLM-udbyder som beskrevet i [Konfiguration](configuration.md), medmindre du kun forbereder Markdown- eller notebook-bidder til host-agent-oversættelse.
2. Beslut, om din applikation håndterer fil-I/O.
3. Brug indholds-API'erne når din applikation læser og skriver enkelte filer.
4. Brug `run_translation` når Co-op Translator skal behandle et repository som CLI'en.
5. Brug `run_review` efter oversættelse, hvis du har brug for deterministiske tjek i automatisering.

| Mål | API at starte med |
| --- | --- |
| Oversæt én Markdown-streng eller fil | `translate_markdown_content` |
| Oversæt en enkelt notebook-payload | `translate_notebook_content` |
| Oversæt ét billede | `translate_image_content` |
| Lad en host agent oversætte Markdown- eller notebook-bidder | `start_markdown_agent_translation` eller `start_notebook_agent_translation` |
| Omskriv oversatte links efter valg af outputsti | `rewrite_markdown_paths` eller `rewrite_notebook_paths` |
| Oversæt et helt repository | `run_translation` |
| Gennemgå oversat output | `run_review` |

## Scenarie 1: Oversæt individuelle filer eller dokumenter

Brug denne arbejdsgang, når du allerede har en fil, editor-buffer, notebook-payload, MCP-forespørgsel eller brugerdefineret pipeline-input. Din kode håndterer fil-I/O:

1. Læs kildeindholdet.
2. Kald en indholds-oversættelses-API.
3. Valgfrit: kald en sti-omskrivnings-API, hvis det oversatte indhold skal skrives ind i en projektoversættelsesmappe.
4. Gem eller returner resultatet fra din applikation.

Indholds-oversættelses-API'erne kører ikke projektopdagelse, skriver ikke metadata, tilføjer ikke ansvarsfraskrivelser og omskriver ikke links automatisk.

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

Hvis den oversatte Markdown ikke skal ligge i et Co-op Translator-projektlayout, spring `rewrite_markdown_paths` over og gem den oversatte streng direkte.

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

`translate_notebook_content` oversætter Markdown-celler og bevarer ikke-Markdown-celler. Stiomskrivning anvendes kun på Markdown-celler.

### Billedfil

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

`translate_image_content` læser kildebilledet og returnerer et gengivet `PIL.Image.Image`. Det skriver ikke metadata for det oversatte billede.

## Scenarie 2: Oversæt et helt repository

Brug denne arbejdsgang, når du ønsker, at Python-API'et opfører sig som `translate`-CLI'en. `run_translation` finder understøttede filer, oversætter valgte indholdstyper, omskriver stier, skriver outputfiler, opdaterer metadata og udfører vedligeholdelsesopgaver for oversættelsen såsom oprydning.

`run_translation` er den foretrukne projektorkestrerings-entrépunkt. `translate_project` eksporteres som et kompatibilitetsalias med samme adfærd.

Oversæt Markdown-filer i det aktuelle repository til koreansk og japansk:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Oversæt kun notebooks fra et specifikt projektrod:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Forhåndsvis oversættelsesomfang uden at skrive filer:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Optag strukturerede fremdriftshændelser for en integration:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Gem nyttelasten i din job-hændelsestabel, eller stream den til din brugergrænseflade.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Hændelser bruger det versionerede skema `co-op.translation.event.v1`. Integrationer bør
afhænge af stabile felter såsom `type` og `stage_key`, ikke af menneskevendt
konsoltekst eller `stage_label`.

Oversæt flere indholds-roots i et enkelt kald:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Skriv oversættelser ind i eksplicitte outputgrupper:

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

Brug en pladsholder pr. sprog, når hvert sprog skal indeholde en indlejret undermappe:

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

Hvis ingen af `markdown`, `notebook` eller `images` er sat, oversætter API'et alle understøttede typer: Markdown, notebooks og billeder.

### Bevar accepterede menneskelige redigeringer med en TranslationStateProvider

Som standard bevarer Co-op Translator sin eksisterende adfærd på filniveau: når en
Markdown-kilde er forældet, genereres hele den oversatte fil igen. Hosted
integrationer kan valgfrit give en `TranslationStateProvider` for at bevare menneskelige
redigeringer i kildeblokke, som ikke er ændret.

Provideren leverer det sidst accepterede kilde-/målpar og registrerer hver ny
kandidat. Accept forbliver integrationens ansvar—for eksempel,
efter en oversættelses-pull request er flettet:

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

For Markdown-filer med en gyldig accepteret baseline justerer Co-op Translator
topniveau Markdown-blokke. Uændrede kildeblokke genbruger de nuværende oversatte
blokke, inklusive ændringer foretaget af mennesker; ændrede eller tilføjede kildeblokke sendes
til oversættelse; slettede kildeblokke fjernes. Hvis justeringen er uklar,
målstrukturen ændrede sig, en blokoversættelse er ugyldig, eller ingen baseline er
tilgængelig, falder Co-op Translator sikkert tilbage til den eksisterende fuldfils-
oversættelsessti.

Denne API gemmer dokumentoversættelsestilstand, ikke en tværdokumental frase- eller
segmentoversættelseshukommelse. Den gælder i øjeblikket for Markdown-projektoversættelse.
Notebook- og billedadfærd er uændret. At angive `update=True`
anmoder stadig om fuld regenerering.

Hvis en eller flere filer ikke kan oversættes, rejser `run_translation` en
`RuntimeError` efter at projektworkflowen er afsluttet i stedet for at rapportere en
lykkedes kørsel med manglende output. Integrationer bør betragte dette som et mislykket
job og bevare den tidligere accepterede oversættelsestilstand.

## Gennemgå oversat output

`run_review` kører deterministiske oversættelsestjek uden LLM- eller Vision-legitimationsoplysninger.

!!! note "Beta"
    `run_review` er en beta deterministisk review-API. Den kalder ikke modeludbydere eller skriver filer, men tjek og issue-skemaer kan udvikle sig.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Efter en README-only-oversættelse, brug samme omfang til gennemgang:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` gennemgår kun `README.md` under hver konfigureret kilderod,
inklusive brugerdefinerede `groups` og outputmapper. Andre dokumenter og indlejrede
README'er udelukkes. En manglende kilde-README rejser `ValueError`; mislykkede
oversættelsestjek rejser `RuntimeError`.

Gennemgå kun filer ændret i forhold til en base-ref og udskriv GitHub-stil output:

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

## Copy-paste API-eksempler

Oversæt Markdown-indhold uden filskrivninger:

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

Oversæt og omskriv Markdown-links:

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

Oversæt et repository fra Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Oversæt flere indholds-roots:

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

Bevar glosetermer:

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

## Offentlige adgangspunkter

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

## Indholdsoversættelses-API'er

Indholds-oversættelses-API'er er beregnet til integrationer, der allerede har indhold i hukommelsen, såsom en editorudvidelse, MCP-værktøj, notebook-processor eller brugerdefineret pipeline.

| Funktion | Input | Output | Fil-I/O | Noter |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Nej | Asynkron. Oversætter kun Markdown-indhold. Den omskriver ikke links, skriver ikke metadata eller tilføjer ansvarsfraskrivelser. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Nej | Asynkron. Oversætter Markdown-celler og bevarer ikke-Markdown-celler. Den omskriver ikke links, skriver ikke metadata, eller tilføjer ikke ansvarsfraskrivelser. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Læser kun kildebilledet | Synkron. Ekstraherer og oversætter billedtekst, og returnerer derefter et gengivet billede. Den gemmer ikke metadata for det oversatte billede. |

`translate_markdown_content` og `translate_notebook_content` accepterer en valgfri `source_path` gennem deres options. Stien videregives som kontekst til oversætteren; kaldere forbliver ansvarlige for enhver projektspecifik stiomskrivning efter oversættelse.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

De samme indstillinger kan gives som ordbøger:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-assisterede oversættelses-API'er

Agent-assisterede API'er kalder ikke den konfigurerede LLM-udbyder fra Co-op Translator. De forbereder Markdown- eller notebook-bidder til at en host-agent kan oversætte, og rekonstruerer derefter det endelige indhold fra de oversatte bidder.

| Funktion | Formål |
| --- | --- |
| `start_markdown_agent_translation` | Returner et selvstændigt Markdown-job med bidder, prompter og rekonstruktionsstatus. |
| `finish_markdown_agent_translation` | Rekonstruer Markdown fra et job og host-agent-oversatte bidder. |
| `start_notebook_agent_translation` | Returner et notebook-job med Markdown-celle-bidder til host-agent-oversættelse. |
| `finish_notebook_agent_translation` | Rekonstruer notebook-JSON samtidig med at kodeceller, output og metadata bevares. |

Denne arbejdsgang er primært beregnet til MCP-hosts. Hvis du har brug for produktionsoversættelse af repository, hvor Co-op Translator styrer udbyderkald, brug `translate_markdown_content`, `translate_notebook_content` eller `run_translation`.

## Sti-omskrivnings-API'er

Stiomskrivnings-API'er udfører ingen oversættelse. De opdaterer links og frontmatter-stier efter at kaldere kender kilde-stien, den oversatte målsti og projektets layout.

| Funktion | Omfang | Noter |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown-krop og frontmatter | Omskriver Markdown-links og understøttede frontmatter-stifelter for et oversat mål. |
| `rewrite_notebook_paths` | Markdown-celler i notebook-JSON | Anvender Markdown-stiomskrivning på hver Markdown-celle og lader ikke-Markdown-celler være uændrede. |

Argumentet `policy` kan være en ordbog med disse felter:

| Felt | Påkrævet | Formål |
| --- | --- | --- |
| `language_code` | Ja | Målsprogskode, f.eks. `"ko"` eller `"pt-BR"`. |
| `root_dir` | Nej | Kildeprojektets rod. Standard er `"."`. |
| `translations_dir` | Nej | Outputmappe for tekstoversættelse. Standard er `translations` under `root_dir`. |
| `translated_images_dir` | Nej | Outputmappe for oversatte billeder. Standard er `translated_images` under `root_dir`. |
| `translation_types` | Nej | Aktiverede oversættelsestyper. Standard er Markdown, notebooks og billeder. |
| `lang_subdir` | Nej | Valgfri undermappe under hver sprogmappe. |

## Projektoversættelsesparametre

| Parameter | Type | Standard | Formål |
| --- | --- | --- | --- |
| `language_codes` | `str` | Påkrævet | Målsprogskoder adskilt af mellemrum, f.eks. `"ko ja fr"`, eller `"all"`. Alias-koder normaliseres til kanoniske BCP 47-værdier. |
| `root_dir` | `str` | `"."` | Projektrod for et enkelt oversættelsesmål. Ignoreres når `root_dirs` eller `groups` er angivet. |
| `update` | `bool` | `False` | Slet og genskab eksisterende oversættelser for de valgte sprog. |
| `images` | `bool` | `False` | Inkluder billedoversættelse. Kræver Azure AI Vision-konfiguration. |
| `markdown` | `bool` | `False` | Inkluder Markdown-oversættelse. |
| `notebook` | `bool` | `False` | Inkluder Jupyter-notebook-oversættelse. |
| `debug` | `bool` | `False` | Aktiver debug-logning. |
| `save_logs` | `bool` | `False` | Gem logfiler på DEBUG-niveau under rodens `logs/`-mappe. |
| `yes` | `bool` | `True` | Automatisk bekræftelse af forespørgsler til programmatisk brug og CI. |
| `add_disclaimer` | `bool` | `False` | Tilføj ansvarsfraskrivelser for maskinoversættelse til oversatte Markdown-filer og notebooks. |
| `translations_dir` | `str \| None` | `None` | Egendefineret outputmappe til tekstoversættelser. Relative stier opløses i forhold til hver rod. |
| `image_dir` | `str \| None` | `None` | Egendefineret outputmappe til oversatte billeder. Relative stier opløses i forhold til hver rod. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Flere rødder, der deler de samme outputindstillinger. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Udtrykkelige `(root_dir, translations_dir)`-par. Har forrang frem for `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository-URL, der bruges ved gengivelse af vejledningen i README-sprogtabellen. |
| `glossaries` | `Iterable[str] \| None` | `None` | Gloseliste-termer, der bevares under oversættelse. Duplikater og tomme termer normaliseres. |
| `dry_run` | `bool` | `False` | Estimér oversættelsesomfang og forhåndsvis migrationsadfærd uden at skrive filer. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Valgfri adapter til persistens af accepted-baseline og kandidat for inkrementelle Markdown-opdateringer. Udeladelse bevarer den eksisterende fuldfilsadfærd. |

## Gennemgangsparametre

`run_review` efterligner bevidst `run_translation`-signaturen, hvor det er muligt, så automatisering kan skifte mellem oversættelses- og gennemgangs-workflows med minimal forgrening.

| Parameter | Type | Default | Formål |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Målsprogmapper til gennemgang. Mellemrum-separerede strenge og iterables accepteres. `"all"` gennemgår alle opdagede oversættelsessprog. |
| `root_dir` | `str` | `"."` | Projektrod for et enkelt gennemgangsmål. Ignoreres når `root_dirs` eller `groups` er angivet. |
| `markdown` | `bool` | `False` | Inkluder Markdown- og MDX-kildefiler. |
| `notebook` | `bool` | `False` | Inkluder Jupyter-notebook-kildefiler. |
| `images` | `bool` | `False` | Reserveret for lighed med oversættelsesmuligheder. Linkreferencer til billeder kontrolleres fra Markdown. |
| `translations_dir` | `str \| None` | `None` | Egendefineret outputmappe til tekstoversættelser. Relative stier opløses i forhold til hver rod. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Flere rødder, der deler de samme outputindstillinger. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Udtrykkelige `(root_dir, translations_dir)`-par. Har forrang frem for `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-ref brugt til at begrænse gennemgang til ændrede kildefiler. |
| `readme_only` | `bool` | `False` | Gennemgå kun `README.md` under hver kilderod. En manglende kilde-README udløser `ValueError`. |
| `output_format` | `str` | `"text"` | Gennemgangens outputformat. Understøttede værdier er `"text"` og `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Behandl advarsler som fejl i tillæg til fejl. |
| `debug` | `bool` | `False` | Aktivér debug-logging. |
| `save_logs` | `bool` | `False` | Gem DEBUG-niveau logfiler under rodmappen `logs/`. |

Hvis ingen af `markdown`, `notebook` eller `images` er sat, gennemgår API'en Markdown, notebooks og billedelinkreferencer hvor relevant. Gennemgang kalder ikke en LLM-udbyder og kræver ikke API-nøgler.

## Konfigurationskrav

Oversættelses-API'er med udbyderunderstøttelse kræver udbyderkonfiguration før oversættelse:

- Oversættelse af Markdown og notebooks kræver en LLM-udbyder. Konfigurer Azure OpenAI, OpenAI, eller Anthropic.
- Billedoversættelse kræver Azure AI Vision ud over LLM-udbyderen.
- `run_translation` kører letvægtsforbindelsestjek før projektoversættelse påbegyndes.
- Agent-assisterede `start_*_agent_translation` og `finish_*_agent_translation` API'er kalder ikke Co-op Translator LLM-udbydere. Værtsapplikationen eller MCP-agenten oversætter de forberedte chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` og `run_review` er deterministiske og kræver ikke udbyderlegitimationsoplysninger.

Påkrævede Azure OpenAI-variabler:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Påkrævede OpenAI-variabler:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Påkrævede Anthropic-variabler:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` og `ANTHROPIC_MAX_TOKENS` er valgfrie. Microsoft Agent Framework er standardmodelklienten for alle udbydere fra og med Co-op Translator 0.22.0. Semantic Kernel kan stadig vælges midlertidigt med `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, men det medfører en advarsel om forældelse; se [configuration](configuration.md#model-client-backend) for den trinvise fjernelsesplan.

Påkrævede Azure AI Vision-variabler til billedoversættelse:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` er deterministisk og kræver ikke LLM- eller Azure AI Vision-konfiguration.

## Bemærkninger om adfærd

- Indholdsoversættelses-API'er holder oversættelse adskilt fra projektsti-omskrivning. Kald eksplicit `rewrite_markdown_paths` eller `rewrite_notebook_paths` når oversat indhold har brug for, at projektrelaterede links justeres for en målplacering.
- Projektorkestrerings-API'er tilføjer projektadfærd omkring indholdsoversættelse, herunder filopdagelse, skrivning, sti-omskrivning, metadata, oprydning og valgfrie ansvarsfraskrivelser.
- `run_translation` printer fremdrifts- og estimatsammenfatninger via den samme Rich-understøttede reporter, som CLI'en bruger. Ikke-interaktiv output falder tilbage til almindelig tekst.
- `dry_run=True` beregner estimater ved hjælp af virtuelle README-opdateringer, men skriver ikke README eller oversættelsesfiler.
- `groups` behandles sekventielt. Et enkelt samlet estimat udskrives før arbejdet påbegyndes.
- Når billedoversættelse er valgt, udløser manglende Vision-konfiguration en fejl før oversættelsen starter.
- Eksisterende alias-baserede sprogmapper opdages og kan migreres til kanoniske sprogmappe-navne som en del af kørslen.
- `run_review` fejler ved manglende oversatte filer, manglende eller forældet oversættelsesmetadata, forkert formet Markdown frontmatter/code fences og ugyldig oversat notebook-JSON.
- `run_review` rapporterer manglende lokale Markdown- og billedelinkmål som advarsler som standard.

## Intern kaldsti

API'en delegerer til den samme kerneimplementering, som CLI'en bruger:

Oversættelse:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Fokuserede mixins til projektoversættelse for Markdown, notesbøger og billeder.
8. Markdown-, notebook-, tekst- og billedoversættere under `co_op_translator.core`.

Gennemgang:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

Følgende klasser er nyttige for vedligeholdere, men eksporteres ikke som den stabile API på pakkeniveau.

| Class | Module | Ansvar |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinerer projektniveau-oversættelse, mappehåndtering, sprogspecifik metadata-normalisering, og delegering til Markdown-, notebook- og billedoversættere. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Udfører det asynkrone filbehandlingsarbejde for Markdown, notebooks, images, forældelsesdetektion, og opdateringer af oversættelsesmetadata. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestrerer Markdown-fil-læsning, indholdsoversættelse, sti-omskrivning, metadata, ansvarsfraskrivelser, og skrivninger. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestrerer notebook-fil-læsning, Markdown-celle-oversættelse, sti-omskrivning, metadata, ansvarsfraskrivelser, og skrivninger. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestrerer kilde-billedopdagelse, billedoversættelse, outputstier, metadata, og skrivninger. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Finder oversatte Markdown-par, evaluerer oversættelseskvalitet, og læser tillidsmetadata til workflows for reparation ved lav tillid. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinerer deterministiske gennemgangskontroller på tværs af kildefiler, målsprog, og konfigurerede oversættelsesrødder. |
| `ReviewTarget` | `co_op_translator.review.targets` | Beskriver en kilderod og den oversættelsesoutputmappe, der gennemgås for den rod. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Registrerer ældre alias-baserede sprogmapper og forbereder kanoniske BCP 47-mappe-migrationsplaner. |
| `Config` | `co_op_translator.config.base_config` | Indlæser `.env`-filer og tjekker om krævede LLM- og valgfrie Vision-udbydere er konfigureret. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Registrerer automatisk Azure OpenAI, OpenAI, eller Anthropic, validerer krævede miljøvariabler, og kører udbyderforbindelsestjek. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Registrerer Azure AI Vision-konfiguration og kører forbindelsestjek for billedoversættelse. |