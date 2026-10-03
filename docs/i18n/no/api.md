# Python-API

Den stabile, offentlige Python-API-en eksporteres fra `co_op_translator.api`. De fleste integrasjoner bruker en av disse arbeidsflytene:

| Scenario | Bruk dette når | Hoved-APIer |
| --- | --- | --- |
| Oversett individuelle filer eller dokumenter | Applikasjonen din leser kildeinnholdet, kaller Co-op Translator for oversettelse, og avgjør hvor resultatet skal lagres. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Forbered innhold for vert-agent-oversettelse | Din MCP-vert eller applikasjonsmodell vil oversette biter, mens Co-op Translator håndterer oppdeling og rekonstruksjon. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Oversett et helt repository | Du ønsker at Python-API-en skal oppføre seg som CLI-en og håndtere oppdagelse, utdata-stier, metadata, opprydding og skriving. | `run_translation` |

De fleste lavnivåmoduler under `core`, `config`, `review`, og `utils` er implementasjonsdetaljer brukt av disse API-innfallsportene.

MCP-klienter bruker det samme offentlige API-et via [MCP-serveren](mcp.md). Bruk denne siden når du kaller Python direkte, og MCP-veiledningen når du eksponerer Co-op Translator for en agent eller editor. Hvis du skal velge mellom CLI, Python-API og MCP, start med [Velg arbeidsflyt](workflows.md).

## Førstegangs API-flyt

Start her hvis du kaller Co-op Translator fra Python-kode:

1. Konfigurer en LLM-leverandør som beskrevet i [Konfigurasjon](configuration.md), med mindre du bare forbereder Markdown- eller notebook-biter for vert-agent-oversettelse.
2. Avgjør om applikasjonen din håndterer fil-I/O.
3. Bruk innholds-APIene når applikasjonen din leser og skriver individuelle filer.
4. Bruk `run_translation` når Co-op Translator skal behandle et repository på samme måte som CLI-en.
5. Bruk `run_review` etter oversettelse hvis du trenger deterministiske sjekker i automatisering.

| Goal | API to start with |
| --- | --- |
| Oversett én Markdown-streng eller fil | `translate_markdown_content` |
| Oversett en notebook-payload | `translate_notebook_content` |
| Oversett ett bilde | `translate_image_content` |
| La en vert-agent oversette Markdown- eller notebook-biter | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Omskriv oversatte lenker etter at du har valgt en utdata-sti | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Oversett et helt repository | `run_translation` |
| Gjennomgå oversatt innhold | `run_review` |

## Scenario 1: Oversett individuelle filer eller dokumenter

Bruk denne arbeidsflyten når du allerede har en fil, editor-buffer, notebook-payload, MCP-forespørsel eller egendefinert pipeline-input. Koden din håndterer fil-I/O:

1. Les kildeinnholdet.
2. Kall et innholdsoversettelses-API.
3. Valgfritt: kall et sti-omskrivings-API hvis det oversatte innholdet skal skrives inn i en prosjektoversettelsesmappe.
4. Lagre eller returner resultatet fra applikasjonen din.

Innholdsoversettelses-APIene kjører ikke prosjektoppdagelse, skriver ikke metadata, legger ikke til ansvarsfraskrivelser, og omskriver ikke lenker automatisk.

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

Hvis den oversatte Markdown-en ikke skal ligge i et Co-op Translator-prosjektoppsett, hopp over `rewrite_markdown_paths` og lagre den oversatte strengen direkte.

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

`translate_notebook_content` oversetter Markdown-celler og bevarer ikke-Markdown-celler. Sti-omskriving gjelder bare for Markdown-celler.

### Bildefil

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

`translate_image_content` leser kildebilde og returnerer et rendret `PIL.Image.Image`. Den skriver ikke oversatt bildemetadata.

## Scenario 2: Oversett et helt repository

Bruk denne arbeidsflyten når du ønsker at Python-API-en skal oppføre seg som `translate` CLI-en. `run_translation` oppdager støttede filer, oversetter valgte innholdstyper, omskriver stier, skriver utdatafiler, oppdaterer metadata og utfører vedlikeholdsoppgaver for oversettelse som opprydding.

`run_translation` er den foretrukne inngangsporten for prosjektorkestrering. `translate_project` eksporteres som et kompatibilitetsalias med samme oppførsel.

Oversett Markdown-filer i det nåværende repositoryet til koreansk og japansk:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Oversett kun notebooks fra et spesifikt prosjektrot:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Forhåndsvis oversettelsesomfang uten å skrive filer:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Registrer strukturerte fremdriftshendelser for en integrasjon:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Lagre nyttelast i jobbhendelsestabellen din eller strøm den til brukergrensesnittet ditt.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Hendelser bruker det versjonerte skjemaet `co-op.translation.event.v1`. Integrasjoner bør
avhenge av stabile felt som `type` og `stage_key`, ikke av menneskevendt
konsolltekst eller `stage_label`.

Oversett flere innholdsrotkataloger i ett kall:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Skriv oversettelser inn i eksplisitte utdata-grupper:

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

Bruk en per-språk-plassholder når hvert språk skal inneholde en nestet undermappe:

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

Hvis ingen av `markdown`, `notebook` eller `images` er satt, oversetter API-et alle støttede typer: Markdown, notebooks og bilder.

### Bevar aksepterte menneskelige redigeringer med en TranslationStateProvider

Som standard beholder Co-op Translator sin eksisterende filnivåatferd: når en
Markdown-kilde er utdatert, regenereres hele den oversatte filen. Hosted
integrasjoner kan valgfritt sende inn en `TranslationStateProvider` for å bevare menneskelige
redigeringer i kildeblokker som ikke har endret seg.

Provideren leverer det sist aksepterte kilde-/målparet og registrerer hver ny
kandidat. Aksept forblir integrasjonens ansvar—for eksempel,
etter at en oversettelses pull request er merget:

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

For Markdown-filer med en gyldig akseptert baseline, tilpasser Co-op Translator
toppnivå Markdown-blokker. Uendrede kildeblokker gjenbruker de nåværende oversatte
blokkene, inkludert redigeringer gjort av personer; endrede eller nye kildeblokker sendes
for oversettelse; slettede kildeblokker fjernes. Hvis justeringen er tvetydig,
målstrukturen har endret seg, en blokkoversettelse er ugyldig, eller ingen baseline er
tilgjengelig, faller Co-op Translator trygt tilbake til den eksisterende hele-fil
oversettelsesbanen.

Dette API-et lagrer dokumentoversettelsestilstand, ikke en tvers-dokument frase- eller
segmentoversettelseshukommelse. Det gjelder for øyeblikket Markdown-prosjektoversettelse.
Notebook- og bildeadferd er uendret. Å sende `update=True`
ber fortsatt om fullgjenoppbygging.

Hvis en eller flere filer ikke kan oversettes, kaster `run_translation` en
`RuntimeError` etter at prosjektarbeidsflyten er fullført i stedet for å rapportere en
vellykket kjøring med manglende utdata. Integrasjoner bør behandle dette som et mislykket
jobb og beholde den tidligere aksepterte oversettelsestilstanden.

## Gjennomgang av oversatt innhold

`run_review` kjører deterministiske oversettelsessjekker uten LLM- eller Vision-legitimasjon.

!!! note "Beta"
    `run_review` er et beta deterministisk gjennomgangs-API. Det kaller ikke modellleverandører eller skriver filer, men sjekker og skjemaer for problemer kan utvikle seg.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Etter en oversettelse som bare omfatter README, bruk samme omfang for gjennomgang:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` gjennomgår kun `README.md` under hver konfigurert source root,
inkludert egendefinerte `groups` og utdata-kataloger. Andre dokumenter og nestede
READMEs er ekskludert. En manglende kilde-README kaster `ValueError`; mislykkede
oversettelsessjekker kaster `RuntimeError`.

Gjennomgå kun filer endret mot en base-ref og skriv ut GitHub-formatert output:

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

## Kopier-og-lim inn API-eksempler

Oversett Markdown-innhold uten filskriving:

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

Oversett og omskriv Markdown-lenker:

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

Oversett et repository fra Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Oversett flere rotmapper:

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

Bevar ordlistebegreper:

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

## Offentlige inngangspunkter

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

## Innholdsoversettelses-APIer

Innholdsoversettelses-APIer er ment for integrasjoner som allerede har innhold i minnet, som en editorutvidelse, MCP-verktøy, notebook-prosessor eller egendefinert pipeline.

| Funksjon | Input | Output | Fil-I/O | Notater |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Nei | Asynkron. Oversetter kun Markdown-innhold. Den omskriver ikke lenker, skriver ikke metadata, eller legger ikke til ansvarsfraskrivelser. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Nei | Asynkron. Oversetter Markdown-celler og bevarer ikke-Markdown-celler. Den omskriver ikke lenker, skriver ikke metadata, eller legger ikke til ansvarsfraskrivelser. |
| `translate_image_content` | Bildebane | `PIL.Image.Image` | Leser kun kildebilde | Synkron. Ekstraherer og oversetter bildetekst, og returnerer så et rendret bilde. Den lagrer ikke oversatt bildemetadata. |

`translate_markdown_content` og `translate_notebook_content` aksepterer en valgfri `source_path` gjennom sine alternativer. Stien sendes som kontekst til oversetteren; kallende kode er fortsatt ansvarlig for eventuelle prosjektspesifikke sti-omskrivinger etter oversettelse.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

De samme alternativene kan sendes som ordbøker:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-assisterte oversettelses-APIer

Agent-assisterte APIer kaller ikke den konfigurerte LLM-leverandøren fra Co-op Translator. De forbereder Markdown- eller notebook-biter for at en vert-agent skal oversette dem, og rekonstruerer deretter sluttinnholdet fra de oversatte bitene.

| Funksjon | Formål |
| --- | --- |
| `start_markdown_agent_translation` | Returnerer en selvstendig Markdown-jobb med biter, ledetekster og rekonstruksjonstilstand. |
| `finish_markdown_agent_translation` | Rekonstruerer Markdown fra en jobb og vert-agent-oversatte biter. |
| `start_notebook_agent_translation` | Returnerer en notebook-jobb med Markdown-cellebiter for vert-agent-oversettelse. |
| `finish_notebook_agent_translation` | Rekonstruerer notebook JSON samtidig som kodeceller, output og metadata bevares. |

Denne arbeidsflyten er hovedsakelig ment for MCP-verter. Hvis du trenger produksjonsoversettelse av repository der Co-op Translator håndterer leverandørkall, bruk `translate_markdown_content`, `translate_notebook_content`, eller `run_translation`.

## APIer for sti-omskriving

Sti-omskrivings-APIer utfører ingen oversettelse. De oppdaterer lenker og frontmatter-stier etter at kallende kode kjenner til kildebanen, den oversatte målbanen og prosjektoppsettet.

| Funksjon | Omfang | Notater |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown-body og frontmatter | Omskriver Markdown-lenker og støttede frontmatter-sti-felt for et oversatt mål. |
| `rewrite_notebook_paths` | Markdown-celler i notebook-JSON | Bruker Markdown-stiomskriving på hver Markdown-celle og lar ikke-Markdown-celler være uendret. |

Argumentet `policy` kan være en ordbok med disse feltene:

| Felt | Obligatorisk | Formål |
| --- | --- | --- |
| `language_code` | Ja | Målspråkkode, for eksempel `"ko"` eller `"pt-BR"`. |
| `root_dir` | Nei | Kilde prosjektrot. Standard er `"."`. |
| `translations_dir` | Nei | Utdata-katalog for tekstoversettelser. Standard er `translations` under `root_dir`. |
| `translated_images_dir` | Nei | Utdata-katalog for oversatte bilder. Standard er `translated_images` under `root_dir`. |
| `translation_types` | Nei | Aktiverte oversettelsestyper. Standard er Markdown, notebooks og bilder. |
| `lang_subdir` | Nei | Valgfri undermappe under hver språkmappe. |

## Prosjektoversettelsesparametre

| Parameter | Type | Standard | Formål |
| --- | --- | --- | --- |
| `language_codes` | `str` | Påkrevd | Mellomromseparerte målspråkkoder, for eksempel `"ko ja fr"`, eller `"all"`. Alias-koder normaliseres til kanoniske BCP 47-verdier. |
| `root_dir` | `str` | `"."` | Prosjektrot for ett enkelt oversettelsesmål. Ignoreres når `root_dirs` eller `groups` er angitt. |
| `update` | `bool` | `False` | Slett og gjenskap eksisterende oversettelser for de valgte språkene. |
| `images` | `bool` | `False` | Inkluder bildeoversettelse. Krever Azure AI Vision-konfigurasjon. |
| `markdown` | `bool` | `False` | Inkluder Markdown-oversettelse. |
| `notebook` | `bool` | `False` | Inkluder Jupyter notebook-oversettelse. |
| `debug` | `bool` | `False` | Aktiver feilsøkingslogging. |
| `save_logs` | `bool` | `False` | Lagre loggfiler på DEBUG-nivå under rotkatalogen `logs/`. |
| `yes` | `bool` | `True` | Bekreft forespørsler automatisk for programmatisk bruk og CI. |
| `add_disclaimer` | `bool` | `False` | Legg til advarsler om maskinoversettelse i oversatt Markdown og notatbøker. |
| `translations_dir` | `str \| None` | `None` | Egendefinert utdata-katalog for tekstoversettelser. Relative stier løses i forhold til hver root. |
| `image_dir` | `str \| None` | `None` | Egendefinert utdata-katalog for oversatte bilder. Relative stier løses i forhold til hver root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Flere root-kataloger som deler de samme utdatainnstillingene. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Eksplisitte `(root_dir, translations_dir)`-par. Har forrang over `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository-URL som brukes ved gjengivelse av README-språktabellens veiledning. |
| `glossaries` | `Iterable[str] \| None` | `None` | Gloselisteord som bevares under oversettelse. Duplikater og tomme termer blir normalisert. |
| `dry_run` | `bool` | `False` | Estimer oversettelsesvolum og forhåndsvis migrasjonsoppførsel uten å skrive filer. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Valgfri adapter for persistens av accepted-baseline og candidate for inkrementelle Markdown-oppdateringer. Å utelate den bevarer eksisterende full-file-oppførsel. |

## Gjennomgangsparametere

`run_review` speiler bevisst signaturen til `run_translation` der det er mulig, slik at automatisering kan bytte mellom oversettelses- og gjennomgangsarbeidsflyter med minimal forgrening.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Mål-språkmapper som skal gjennomgås. Strenger adskilt med mellomrom og iterable aksepteres. `"all"` gjennomgår alle oppdagede oversettelsesspråk. |
| `root_dir` | `str` | `"."` | Prosjektrot for ett enkelt gjennomgangsmål. Ignoreres når `root_dirs` eller `groups` er angitt. |
| `markdown` | `bool` | `False` | Inkluder Markdown- og MDX-kildefiler. |
| `notebook` | `bool` | `False` | Inkluder Jupyter-notatbok-kildefiler. |
| `images` | `bool` | `False` | Reservert for samsvar med oversettelsesalternativer. Lenkehenvisninger til bilder sjekkes fra Markdown. |
| `translations_dir` | `str \| None` | `None` | Egendefinert utdata-katalog for tekstoversettelser. Relative stier løses i forhold til hver root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Flere root-kataloger som deler de samme utdatainnstillingene. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Eksplisitte `(root_dir, translations_dir)`-par. Har forrang over `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-ref brukt for å begrense gjennomgangen til endrede kildefiler. |
| `readme_only` | `bool` | `False` | Gjennomgå kun `README.md` under hver kilderot. En manglende kilde-README utløser `ValueError`. |
| `output_format` | `str` | `"text"` | Utdataformat for gjennomgang. Støttede verdier er `"text"` og `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Behandle advarsler som feil i tillegg til andre feil. |
| `debug` | `bool` | `False` | Aktiver debug-logging. |
| `save_logs` | `bool` | `False` | Lagre loggfiler på DEBUG-nivå under rotkatalogen `logs/`. |

Hvis ingen av `markdown`, `notebook` eller `images` er satt, gjennomgår API-et Markdown, notatbøker og referanser til bildelenker der det er aktuelt. Gjennomgang kaller ikke en LLM-leverandør og krever ikke API-nøkler.

## Konfigurasjonskrav

Leverandørstøttede oversettelses-APIer krever leverandørkonfigurasjon før oversettelse:

- Oversettelse av Markdown og notatbøker krever en LLM-leverandør. Konfigurer Azure OpenAI, OpenAI eller Anthropic.
- Bildeoversettelse krever Azure AI Vision i tillegg til LLM-leverandøren.
- `run_translation` kjører lette tilkoblingskontroller før prosjektoversettelsen begynner.
- Agent-assisterte APIer `start_*_agent_translation` og `finish_*_agent_translation` kaller ikke Co-op Translator LLM-leverandører. Vertsapplikasjonen eller MCP-agenten oversetter de forberedte biter.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, og `run_review` er deterministiske og krever ikke leverandørlegitimasjon.

Påkrevde Azure OpenAI-variabler:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Påkrevde OpenAI-variabler:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Påkrevde Anthropic-variabler:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` og `ANTHROPIC_MAX_TOKENS` er valgfrie. Microsoft Agent Framework er standard modellklient for alle leverandører fra og med Co-op Translator 0.22.0. Semantic Kernel kan fortsatt velges midlertidig med `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, men det vil gi en avviklingsadvarsel; se [konfigurasjon](configuration.md#model-client-backend) for planen for trinnvis fjerning. |

Påkrevde Azure AI Vision-variabler for bildeoversettelse:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` er deterministisk og krever ikke LLM- eller Azure AI Vision-konfigurasjon.

## Merknader om oppførsel

- Innholdsoversettelses-APIer holder oversettelse adskilt fra prosjektsti-omskriving. Kall eksplisitt `rewrite_markdown_paths` eller `rewrite_notebook_paths` når oversatt innhold trenger at prosjekt-relative lenker justeres for et målsted.
- Prosjekt-orkestrerings-APIer legger til prosjektatferd rundt innholdsoversettelse, inkludert filoppdagelse, skriving, sti-omskriving, metadata, opprydding og valgfrie ansvarsfraskrivelser.
- `run_translation` skriver ut fremdrifts- og estimatsammendrag gjennom samme Rich-støttede rapportør som brukes av CLI-en. Ikke-interaktivt utdata faller tilbake til ren tekst.
- `dry_run=True` beregner estimater ved å bruke virtuelle README-oppdateringer, men skriver ikke README-en eller oversettelsesfilene.
- `groups` behandles sekvensielt. Et enkelt aggregert estimat skrives ut før arbeidet begynner.
- Når bildeoversettelse velges, vil manglende Vision-konfigurasjon utløse en feil før oversettelsen starter.
- Eksisterende alias-baserte språkmapper oppdages og kan migreres til kanoniske språkmappe-navn som en del av kjøringen.
- `run_review` feiler ved manglende oversatte filer, manglende eller utdaterte oversettelsesmetadata, feilformatert Markdown-frontmatter/kodegjerder, og ugyldig oversatt notatbok-JSON.
- `run_review` rapporterer manglende lokale Markdown- og bildelenkemål som advarsler som standard.

## Intern kallbane

API-et delegerer til samme kjerneimplementering som brukes av CLI-en:

Oversettelse:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Fokusert prosjekt-oversettelses-mixins for Markdown, notatbøker og bilder.
8. Markdown-, notatbok-, tekst- og bildeoversettere under `co_op_translator.core`.

Gjennomgang:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministiske sjekker under `co_op_translator.review.checks`

Følgende klasser er nyttige for vedlikeholdere, men eksporteres ikke som pakkenivåets stabile API.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinerer prosjekt-nivå oversettelse, kataloghåndtering, metadata-normalisering per språk, og delegasjon til Markdown-, notatbok- og bildeoversettere. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Utfører det asynkrone filbehandlingsarbeidet for Markdown, notatbøker, bilder, deteksjon av utdaterte filer, og oppdateringer av oversettelsesmetadata. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestrerer lesing av Markdown-filer, innholdsoversettelse, sti-omskriving, metadata, ansvarsfraskrivelser og skriving. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestrerer lesing av notatbok-filer, oversettelse av Markdown-celler, sti-omskriving, metadata, ansvarsfraskrivelser og skriving. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestrerer oppdagelse av kildebilder, bildeoversettelse, utdata-stier, metadata og skriving. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Finner oversatte Markdown-par, vurderer oversettelseskvalitet og leser konfidensmetadata for arbeidsflyter for reparasjon ved lav konfidens. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinerer deterministiske gjennomgangssjekker på tvers av kildefiler, målspråk og konfigurerte oversettelses-roots. |
| `ReviewTarget` | `co_op_translator.review.targets` | Beskriver en kilderot og oversettelsesutdata-katalogen som gjennomgås for den roten. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Oppdager eldre alias-språkmapper og forbereder migrasjonsplaner til kanoniske BCP 47-mappe-navn. |
| `Config` | `co_op_translator.config.base_config` | Laster `.env`-filer og sjekker om nødvendige LLM- og valgfrie Vision-leverandører er konfigurert. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Oppdager automatisk Azure OpenAI, OpenAI eller Anthropic, validerer nødvendige miljøvariabler og kjører tilkoblingssjekker mot leverandører. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Oppdager Azure AI Vision-konfigurasjon og kjører tilkoblingssjekker for bildeoversettelse. |