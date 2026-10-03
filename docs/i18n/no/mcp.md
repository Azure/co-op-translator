# MCP-server

Co-op Translator inkluderer en Model Context Protocol-server for agenter, redaktører og MCP-kompatible klienter.

For standard lokal oppsett trenger ikke brukere å kjøre en separat server manuelt. De konfigurerer MCP-klienten sin, og klienten starter `co-op-translator-mcp` automatisk over `stdio` når den trenger Co-op Translator-verktøy.

Hvis du skal velge mellom CLI, Python API og MCP, begynn med [Velg arbeidsflyt](workflows.md).

Bruk MCP når en agent eller redaktør bør kalle Co-op Translator direkte:

| Brukermål | MCP-verktøy |
| --- | --- |
| Oversett ett Markdown-dokument, notatbok eller bilde | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Oversett Markdown- eller notatbokinnhold med vertagentmodellen | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Omskriv oversatte Markdown- eller notatboklenker etter å ha valgt målsti | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Oversett et helt repository som CLI-en | `run_translation`, `translate_project` |
| Gjennomgå oversatt output uten LLM-legitimasjon | `run_review` |
| Inspiser funksjoner og miljøstatus | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP-serveren pakker inn den samme offentlige Python-API-en dokumentert i [Python API](api.md). Leverandørstøttede verktøy bruker de samme konfigurerte providerne som CLI-en og Python-API-en. Agent-assisterte verktøy forbereder chunks for MCP-vertagenten å oversette, og bruker deretter Co-op Translator for å rekonstruere den endelige Markdown-en eller notatboken.

## Trinn 1: Installer og konfigurer Co-op Translator

Installer Co-op Translator i Python-miljøet som MCP-klienten din vil bruke:

```bash
pip install co-op-translator
```

For lokal utvikling fra dette repositoryet, installer pakken i redigerbar modus:

```bash
pip install -e .
```

Velg oversettelsesmodus som MCP-klienten din vil bruke:

| Modus | Bruk dette for | Legitimasjon |
| --- | --- | --- |
| Provider-backed | Co-op Translator kaller `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, eller `run_translation`. | Oversettelse krever Azure OpenAI, OpenAI, eller Anthropic. Bildeoversettelse krever også Azure AI Vision. |
| Agent-assisted | MCP-vertagenten oversetter chunks returnert av `start_markdown_agent_translation` eller `start_notebook_agent_translation`. | Ingen Co-op Translator LLM-providerlegitimasjon kreves for Markdown- eller notatbokchunks. Bildeoversettelse dekkes foreløpig ikke av agent-assistert modus. |

Hvis du starter med Markdown- eller notatbokoversettelse inne i en agent som Codex eller Claude Code, start med agent-assistert modus. Bruk provider-backed modus når du vil at Co-op Translator selv skal kalle de konfigurerte providerne, når du oversetter bilder, eller når du kjører repository-nivå oversettelse som CLI-en.

Konfigurer én provider for leverandørstøttede arbeidsflyter:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Eller OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Eller Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Leverandørstøttet bildeoversettelse trenger i tillegg:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assistert modus dekker for øyeblikket Markdown og Markdown-celler i notatbøker. Bildeoversettelse bruker fortsatt leverandørstøttet bilde-pipeline og krever Azure AI Vision for OCR og layout-bevisst gjengivelse.

## Trinn 2: Konfigurer MCP-klienten din

For normal lokal `stdio`-oppsett, legg Co-op Translator til i MCP-klientens konfigurasjon. Klienten starter og stopper prosessen automatisk.

Konfigurasjon for installert pakke:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Konfigurasjon for kildekode-sjekk ut på Windows:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

Konfigurasjon for kildekode-sjekk ut på macOS eller Linux:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

Etter å ha endret MCP-klientkonfigurasjonen, start eller last klienten på nytt slik at den kan oppdage den nye serveren.

## Trinn 3: Verifiser serveren i klienten

Be MCP-klienten liste tilgjengelige verktøy, eller kall en av de skrivebeskyttede hjelperne først:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Nyttige første sjekker:

| Verktøy | Hva du bør sjekke |
| --- | --- |
| `get_api_overview` | Bekrefter at serveren er tilgjengelig og viser tilgjengelige arbeidsflyter. |
| `list_supported_languages` | Bekrefter at pakkede språkdata kan lastes. |
| `get_configuration_status` | Bekrefter tilgjengelighet for LLM- og Vision-providers uten å eksponere hemmelige verdier. |

## Trinn 4: Velg en arbeidsflyt

### Oversett individuelle filer eller dokumenter

Bruk leverandørstøttede innholdsverktøy når MCP-klienten allerede har dokumentinnhold eller en bildefilbane og Co-op Translator skal kalle de konfigurerte oversettelsesleverandørene.

For Markdown:

1. Kall `translate_markdown_content` med `document`, `language_code`, og eventuelt `source_path`.
2. Hvis det oversatte resultatet skal skrives inn i et Co-op Translator-utdataoppsett, kall `rewrite_markdown_paths`.
3. La klienten skrive eller returnere den endelige `content`.

For notatbøker:

1. Kall `translate_notebook_content` med notatbok-JSON og `language_code`.
2. Kall `rewrite_notebook_paths` hvis oversatte notatboklenker må justeres for en målbane.
3. Skriv eller returner den endelige notatbok-JSONen.

For bilder:

1. Kall `translate_image_content` med `image_path`, `language_code`, og valgfri `root_dir` eller `fast_mode`.
2. Les den returnerte `data_base64` og `mime_type`.
3. Hvis `output_path` er oppgitt, lagres også det oversatte bildet til den banen.

Innholdsverktøyene utfører ikke prosjektoppdagelse, metadataoppdateringer, ansvarsfraskrivelser eller automatisk sti-omskriving. Hvis du vil at vertagenten skal oversette Markdown- eller notatbokchunks uten Co-op Translator LLM-providerlegitimasjon, bruk den agent-assisterte arbeidsflyten nedenfor.

### Oversett med vertagentmodellen

Bruk agent-assisterte verktøy når du vil at MCP-vertagenten, for eksempel en kodeassistent, skal produsere den oversatte teksten i stedet for å konfigurere en LLM-provider for Co-op Translator.

I en chat-basert MCP-klient trenger du vanligvis ikke å skrive verktøy-JSON selv. Be agenten bruke den agent-assisterte arbeidsflyten:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

For notatbøker, bruk samme mønster:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Hvis MCP-klienten din støtter serverprompter, bruk `agent_assisted_markdown_translation_prompt` for å få klienten til å laste de samme arbeidsflytinstruksjonene.

For Markdown:

1. Kall `start_markdown_agent_translation` med `document`, `language_code`, og eventuelt `source_path`.
2. Oversett hver returnerte chunk i vertagenten ved å følge chunkens `prompt`.
3. Kall `finish_markdown_agent_translation` med den opprinnelige `job` og oversatte chunks ved å bruke `chunk_id` og `translated_text`.
4. Hvis innholdet skal skrives til en oversatt målsti, kall `rewrite_markdown_paths`.

For notatbøker:

1. Kall `start_notebook_agent_translation` med notatbok-JSON og `language_code`.
2. Oversett hver returnerte chunk i vertagenten.
3. Kall `finish_notebook_agent_translation` med den opprinnelige `job` og oversatte chunks.
4. Kall `rewrite_notebook_paths` hvis oversatte notatboklenker trenger justering for målsti.

Agent-assisterte verktøy kaller ikke den konfigurerte LLM-provideren fra Co-op Translator. Vertagenten er ansvarlig for å oversette de returnerte chunks. Co-op Translator håndterer Markdown-chunking, bevaring av plassholdere, rekonstruksjon av frontmatter, utskifting av notatbokceller og normalisering etter oversettelse.

### Oversett et helt repository

Bruk `run_translation` når brukeren vil at Co-op Translator skal oppføre seg som `translate`-CLI-en.

Repository-oversettelse er som standard `dry_run=true` slik at en agent kan inspisere omfanget før filendringer:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Resultatet fra `run_translation` inkluderer en `events`-array med versjonerte
`co-op.translation.event.v1` fremdriftshendelser. MCP-klienter bør bruke felt som
`type`, `stage_key`, `completed`, `total`, og `current_path` i stedet for
å analysere fanget konsolltekst. Send med `json_events_path` for også å skrive disse hendelsene
til en NDJSON-fil.

For å tillate skriving må anroper sette både `dry_run=false` og `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` er eksponert som et kompatibilitetsalias for `run_translation`.

### Gjennomgå oversatt output

Bruk `run_review` for deterministiske sjekker som ikke krever LLM- eller Vision-legitimasjon:

!!! note "Beta"
    MCP eksponerer beta-`run_review`-APIet. Det er trygt for skrivebeskyttede gjennomgangsarbeidsflyter, men gjennomgangssjekker og issueskjemaer kan utvikle seg.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Resultatet inkluderer fanget tekstutdata og et strukturert gjennomgangssammendrag når tilgjengelig.

## Manuelle serverkjøringer

Manuelle kjøringer er hovedsakelig for feilsøking eller for transportmåter som oppfører seg som langkørende servere.

Feilsøk standard stdio-serveren:

```bash
co-op-translator-mcp
```

Kjør fra en kildekode-sjekk ut:

```bash
python -m co_op_translator.mcp.server
```

Kjør en langlevd HTTP- eller SSE-server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

For lokale editor- og agentintegrasjoner, foretrekk klientadministrert `stdio`-konfigurasjon i Trinn 2.

## Verktøy

| Verktøy | Formål | Skriver filer |
| --- | --- | --- |
| `translate_markdown_content` | Oversett en Markdown-streng. | Nei |
| `translate_notebook_content` | Oversett Markdown-celler i notatbok-JSON. | Nei |
| `translate_image_content` | Oversett tekst i ett bilde og returner base64-bildedata. | Valgfritt, kun når `output_path` er oppgitt |
| `start_markdown_agent_translation` | Forbered Markdown-chunks for at vertagenten skal oversette uten Co-op Translator LLM-legitimasjon. | Nei |
| `finish_markdown_agent_translation` | Rekonstruer Markdown fra vertagent-oversatte chunks. | Nei |
| `start_notebook_agent_translation` | Forbered notatbokens Markdown-cellechunks for vertagenten å oversette. | Nei |
| `finish_notebook_agent_translation` | Rekonstruer notatbok-JSON fra vertagent-oversatte chunks. | Nei |
| `rewrite_markdown_paths` | Omskriv Markdown-innhold og frontmatter-stier for et oversatt mål. | Nei |
| `rewrite_notebook_paths` | Omskriv stier inne i notatbokens Markdown-celler. | Nei |
| `run_translation` | Kjør prosjektnivå-oversettelse som CLI-en. | Ja når `dry_run=false` og `confirm_write=true` |
| `translate_project` | Kompatibilitetsalias for `run_translation`. | Ja når `dry_run=false` og `confirm_write=true` |
| `run_review` | Kjør deterministiske gjennomgangssjekker. | Nei |
| `get_configuration_status` | Rapporter konfigurerte LLM- og Vision-providers uten å eksponere hemmeligheter. | Nei |
| `list_supported_languages` | List støttede målspråkkoder. | Nei |
| `get_api_overview` | Beskriv tilgjengelige MCP-arbeidsflyter og verktøy. | Nei |

## Ressurser

| Ressurs URI | Formål |
| --- | --- |
| `co-op://api` | JSON-oversikt over arbeidsflyter og verktøy. |
| `co-op://supported-languages` | JSON-liste over støttede språkkoder. |
| `co-op://configuration` | JSON-oppsummering av provider-tilgjengelighet uten hemmeligheter. |

## Prompter

| Prompt | Formål |
| --- | --- |
| `translate_markdown_document_prompt` | Veilede en MCP-klient gjennom innholdsoversettelse pluss valgfri sti-omskriving. |
| `agent_assisted_markdown_translation_prompt` | Veilede en MCP-klient gjennom vertagent-markdown-oversettelse uten Co-op Translator LLM-providerlegitimasjon. |
| `translate_repository_prompt` | Veilede en MCP-klient gjennom repository-oversettelse med først en dry-run. |

## Kopier-og-lim-eksempler

Oversett Markdown-innhold:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Omskriv oversatte Markdown-lenker:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

Oversett Markdown med vertagentmodellen:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Etter at vertagenten har oversatt hver returnerte chunk, fullfør jobben med det komplette `job`-objektet returnert av `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Forhåndsvis repository-oversettelse:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Feilsøking

| Problem | Hva du kan prøve |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Bruk den absolutte Python-eksekverbare banen og `["-m", "co_op_translator.mcp.server"]` source checkout-konfigurasjon. |
| Serveren er oppført, men oversettelsen feiler. | Kall `get_configuration_status` og bekreft at en LLM-provider er tilgjengelig. |
| Du vil ha oversettelse av Markdown eller notatbok uten leverandørlegitimasjon. | Bruk `start_markdown_agent_translation` / `finish_markdown_agent_translation` eller tilsvarende for notatbøker slik at vertagenten oversetter chunks. |
| Image translation fails. | Bekreft at Azure AI Vision-variablene er satt og kall `get_configuration_status`. |
| Repository-oversettelsen skriver ikke filer. | Sett `dry_run=false` og `confirm_write=true` bare etter eksplisitt brukergodkjenning. |
| Endringer i klientkonfigurasjonen vises ikke. | Start MCP-klienten på nytt eller last den inn på nytt. |

## Sikkerhetsmerknader

- MCP-verktøysanrop styres av modellen i vertapplikasjonen, så repository-oversettelse er som standard en dry-run.
- Full repository-oversettelse kan opprette, oppdatere eller fjerne mange filer. Krev eksplisitt brukerbekreftelse før du setter `confirm_write=true`.
- Konfigurasjonsstatusverktøyet returnerer aldri API-nøkler, endepunkter eller andre hemmelige verdier.
- Bildeoversettelse returnerer base64-bildedata. Store bilder kan gi store verktøyssvar.
- Agent-assisterte verktøy returnerer kildechunks og prompter til MCP-verten. Bruk dem kun med innhold brukeren er komfortabel med å sende til den vertagentmodellen.