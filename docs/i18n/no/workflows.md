# Velg arbeidsflyt

Co-op Translator kan brukes på tre måter: CLI-en, Python-API-en og MCP-serveren. De deler de samme oversettelsesmulighetene, men hver passer til en annen arbeidsflyt.

Bruk denne siden når du bestemmer hvor du skal starte.

## Rask avgjørelse

| Hvis du vil... | Bruk | Start her |
| --- | --- | --- |
| Oversette eller gjennomgå et repository fra en terminal | CLI | [CLI-referanse](cli.md) |
| Legge til oversettelse i et Python-skript, en tjeneste, en notatbok eller en CI-jobb | Python-API | [Python-API](api.md) |
| La en agent, redaktør eller MCP-kompatibel klient oversette innhold for deg | MCP-server | [MCP-server](mcp.md) |
| Oversette ett Markdown-dokument, en notatbok eller et bilde som appen din allerede har lastet | Python-API eller MCP-server | [Python-API](api.md) eller [MCP-server](mcp.md) |
| Oversette et helt repository med standard utdata-mapper og metadata | CLI eller `run_translation` | [CLI-referanse](cli.md) eller [Python-API](api.md) |

## Bruk CLI-en når

Velg CLI-en når en person eller en CI-jobb styrer oversettelsen av et repository fra et shell.

CLI-en er den mest direkte veien når du vil at Co-op Translator skal oppdage prosjektfiler, opprette oversatte utdata, bevare prosjektoppsettet, oppdatere metadata og kjøre gjennomgangskommandoer.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Passer godt:

- Du oversetter et repository fra terminalen.
- Du ønsker en repeterbar kommando for CI- eller utgivelsesarbeidsflyter.
- Du vil ha innebygd prosjektdeteksjon, utdata-stier, metadata, opprydding og gjennomgang.
- Du foretrekker et kommandogrensesnitt fremfor å skrive Python-kode.

## Bruk Python-API-en når

Velg Python-API-en når din egen kode skal kontrollere arbeidsflyten.

API-en er nyttig for applikasjoner, automasjonsskript, notatbøker, tjenester og egendefinerte pipelines. Den lar deg kalle lavnivås innholdsoversettelses-APIer for individuelle filer, eller kjøre samme repository-nivå orkestrering som CLI-en bruker.

Oversett ett Markdown-dokument og bestem hvor du vil lagre det:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


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
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Kjør en repository-oversettelse fra Python:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Passer godt:

- Applikasjonen din leser allerede filer, buffere, notatbøker eller bildebytes.
- Du trenger egendefinert validering, lagring, logging, gjentatte forsøk eller godkjenningsflyter.
- Du vil oversette ett dokument, en notatbok eller et bilde uten å behandle et helt repository.
- Du vil ha repository-oversettelse, men fra Python-automatisering i stedet for en shell-kommando.

## Bruk MCP-serveren når

Velg MCP-serveren når en agent, redaktør eller MCP-kompatibel klient skal kalle Co-op Translator-verktøy.

I den normale lokale oppsettet holder ikke brukeren manuelt en server kjørende. MCP-klienten starter `co-op-translator-mcp` over `stdio` når den trenger verktøyene.

Eksempler på brukerforespørsler en agent kan håndtere:

- "Oversett denne Markdown-filen til koreansk og behold lenkene korrekte."
- "Oversett denne Markdown-filen til koreansk med den agent-assisterte MCP-arbeidsflyten, og bruk din egen modell for de oversatte delene."
- "Oversett denne notatboken til koreansk, behold kodeceller, og bruk Co-op Translator MCP for å rekonstruere notatboken."
- "Oversett teksten i dette bildet til japansk og lagre resultatet."
- "Kjør en dry-run av en repository-oversettelse til spansk og fortell meg hva som ville endret seg."
- "Sjekk om den koreanske oversettelsen er oppdatert."

For Markdown og notatbøker kan MCP fungere i to moduser:

| Modus | Bruk når | Hovedverktøy |
| --- | --- | --- |
| Agent-assistert | MCP-vertagenten skal oversette biter med sin egen modell, uten Co-op Translator LLM-leverandørlegitimasjon. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Leverandørstøttet | Co-op Translator skal kalle Azure OpenAI eller OpenAI direkte. | `translate_markdown_content`, `translate_notebook_content` |

MCP leverandørstøttet Markdown-verktøykall-format:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP bildeverktøykall:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

Repository-oversettelse kjøres som dry-run som standard via MCP:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

Passer godt:

- Du ønsker naturlig-språkige oversettelsesarbeidsflyter inne i en agent eller redaktør.
- Du vil ha Markdown- eller notatbokoversettelse der vertagentmodellen oversetter forberedte biter.
- Du ønsker at agenten skal oversette valgt innhold i stedet for et helt repository.
- Du ønsker et godkjenningssteg før skriving på tvers av repository-et.
- Du vil ha ett grensesnitt som tilbyr Markdown-, notatbok-, bilde-, gjennomgangs- og sti-omskrivningsverktøy.

## Hvordan de passer sammen

CLI-en er det beste standardvalget for mennesker som oversetter repositories. Python-API-en er best når koden din eier arbeidsflyten. MCP-serveren er best når en agent eller redaktør eier arbeidsflyten.

Alle tre veier bruker det samme offentlige Co-op Translator-APIet, så du kan starte med CLI-en, automatisere med Python senere, og eksponere de samme mulighetene til MCP-klienter når du trenger agent-drevne arbeidsflyter.