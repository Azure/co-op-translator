# Velg arbeidsflyt

Co-op Translator kan brukes på tre måter: CLI, Python API, og MCP-serveren. De deler de samme oversettelsesmulighetene, men hver passer til en ulik arbeidsflyt.

Bruk denne siden når du skal bestemme hvor du skal starte.

**Hvis du redigerer oversettelser for hånd:** standard arbeidsflyter for CLI og Actions oversetter endrede kildefiler på nytt i sin helhet, så formuleringene dine i disse filene kan bli overskrevet. Gå gjennom diffen før du godtar en oppdatering. For bevaring av aksepterte endringer på blokk-nivå i Markdown, bruk den valgfrie [Python API-oversettelsestilstandsleverandøren](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Rask beslutning

| Hvis du vil... | Bruk | Start her |
| --- | --- | --- |
| Oversette eller gjennomgå et repository fra en terminal | CLI | [CLI-referanse](cli.md) |
| Legg til oversettelse i et Python-skript, tjeneste, notatbok eller CI-jobb | Python API | [Python API](api.md) |
| La en agent, editor, eller MCP-kompatibel klient oversette innhold for deg | MCP Server | [MCP Server](mcp.md) |
| Oversett ett Markdown-dokument, notatbok eller bilde som applikasjonen din allerede har lastet | Python API eller MCP Server | [Python API](api.md) eller [MCP Server](mcp.md) |
| Oversett et helt repository med standard utdata-mapper og metadata | CLI eller `run_translation` | [CLI-referanse](cli.md) eller [Python API](api.md) |

## Bruk CLI når

Velg CLI når en person eller en CI-jobb styrer repository-oversettelsen fra kommandolinjen.

CLI er den mest direkte veien når du vil at Co-op Translator skal oppdage prosjektfiler, lage oversatte utdata, bevare prosjektoppsettet, oppdatere metadata og kjøre gjennomgangskommandoer.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Dette eksempelet oversetter Markdown og notatbøker. Legg til `-img` bare etter å ha konfigurert [Azure AI Vision](configuration.md#azure-ai-vision). For en førstegangs kjøring med kun Markdown, følg [Din første oversettelse](first-translation.md).

Passer godt når:

- Du oversetter et repository fra terminalen din.
- Du ønsker en gjentakbar kommando for CI- eller release-arbeidsflyter.
- Du ønsker innebygd prosjektoppdagelse, utdatastier, metadata, opprydding og gjennomgang.
- Du foretrekker et kommandogrensesnitt fremfor å skrive Python-kode.

## Bruk Python API når

Velg Python API når din egen kode skal kontrollere arbeidsflyten.

API-et er nyttig for applikasjoner, automatiseringsskript, notatbøker, tjenester og egendefinerte pipelines. Det lar deg kalle lavnivå-APIer for innholdsoversettelse for individuelle filer, eller kjøre den samme repositorie-nivå orkestreringen som CLI bruker.

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
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Passer godt når:

- Applikasjonen din leser allerede filer, buffere, notatbøker eller bildebytes.
- Du trenger egendefinert validering, lagring, logging, retry-mekanismer eller godkjenningsflyter.
- Du vil oversette ett dokument, notatbok eller bilde uten å behandle et helt repository.
- Du ønsker repository-oversettelse, men fra Python-automatisering i stedet for en shell-kommando.

## Bruk MCP-serveren når

Velg MCP-serveren når en agent, editor eller MCP-kompatibel klient skal kalle Co-op Translator-verktøyene.

I et vanlig lokalt oppsett holder ikke brukeren manuelt en server kjørende. MCP-klienten starter `co-op-translator-mcp` over `stdio` når den trenger verktøyene.

Eksempel på brukerforespørsler en agent kan håndtere:

- "Oversett denne Markdown-filen til koreansk og behold lenkene korrekte."
- "Oversett denne Markdown-filen til koreansk med den agent-assisterte MCP-arbeidsflyten, og bruk din egen modell for de oversatte delene."
- "Oversett denne notatboken til koreansk, bevar kodeceller, og bruk Co-op Translator MCP for å rekonstruere notatboken."
- "Oversett teksten i dette bildet til japansk og lagre resultatet."
- "Kjør en tørrkjøring av repository-oversettelse til spansk og fortell meg hva som ville endret seg."
- "Vurder om den koreanske oversettelsen er oppdatert."

For Markdown og notatbøker kan MCP fungere i to modi:

| Modus | Bruk når | Hovedverktøy |
| --- | --- | --- |
| Agent-assistert | MCP-vertsagenten bør oversette deler med sin egen modell, uten Co-op Translator LLM-leverandør-legitimasjon. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Leverandørstøttet | Co-op Translator bør kalle Azure OpenAI, OpenAI, eller Anthropic direkte. | `translate_markdown_content`, `translate_notebook_content` |

MCP-leverandørstøttet Markdown-verktøykall:

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

MCP-bildeverktøykall:

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

Repository-oversettelse kjøres som standard som en tørrkjøring gjennom MCP:

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

Passer godt når:

- Du ønsker naturlig-språkbaserte oversettelsesarbeidsflyter i en agent eller editor.
- Du ønsker Markdown- eller notatbokoversettelse hvor vertsagentens modell oversetter forberedte deler.
- Du vil at agenten skal oversette valgt innhold i stedet for et helt repository.
- Du ønsker et godkjenningssteg før skriveoperasjoner på tvers av hele repositoryet.
- Du ønsker ett grensesnitt som eksponerer verktøy for Markdown, notatbok, bilde, gjennomgang og sti-omskriving.

## Hvordan de passer sammen

CLI er det beste standardvalget for mennesker som oversetter repositories. Python API er best når koden din eier arbeidsflyten. MCP-serveren er best når en agent eller editor eier arbeidsflyten.

Alle tre veiene bruker det samme offentlige Co-op Translator API-et, så du kan starte med CLI, automatisere med Python senere, og eksponere de samme mulighetene til MCP-klienter når du trenger agentstyrte arbeidsflyter.