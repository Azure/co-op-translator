# MCP-server

Co-op Translator inkluderer en Model Context Protocol-server for agenter, redaktører og MCP-kompatible klienter.

For standard lokal oppsett trenger ikke brukere å holde en separat server kjørende manuelt. De konfigurerer sin MCP-klient, og klienten starter `co-op-translator-mcp` automatisk over `stdio` når den trenger Co-op Translator-verktøy.

Hvis du vurderer mellom CLI, Python API og MCP, start med [Velg arbeidsflyt](workflows.md).

Bruk MCP når en agent eller redaktør skal kalle Co-op Translator direkte:

| Brukermål | MCP-verktøy |
| --- | --- |
| Oversett et Markdown-dokument, en notatbok eller et bilde | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Oversett Markdown- eller notatbokinnhold med vertsagentmodellen | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Omskriv oversatte Markdown- eller notatboklenker etter valg av målsti | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Oversett et helt prosjekt som CLI-en | `run_translation`, `translate_project` |
| Gjennomgå oversatt output uten LLM-legitimasjon | `run_review` |
| Inspiser kapasiteter og miljøstatus | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP-serveren pakker inn den samme offentlige Python-API-en dokumentert i [Python-API](api.md). Provider-støttede verktøy bruker de samme konfigurerte leverandørene som CLI-en og Python-API-en. Agent-assisterte verktøy forbereder biter for MCP-vertsagenten å oversette, og bruker deretter Co-op Translator for å rekonstruere den endelige Markdown-en eller notatboken.

## Trinn 1: Installer og konfigurer Co-op Translator

Installer Co-op Translator i Python-miljøet som din MCP-klient vil bruke:

```bash
pip install co-op-translator
```

For lokal utvikling fra dette depotet, installer pakken i redigerbar modus:

```bash
pip install -e .
```

Velg oversettelsesmodusen din MCP-klient skal bruke:

| Modus | Bruk dette for | Legitimasjon |
| --- | --- | --- |
| Provider-støttet | Co-op Translator kaller `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, eller `run_translation`. | Markdown- og notatbokoversettelse krever Azure OpenAI eller OpenAI. Bildeoversettelse krever også Azure AI Vision. |
| Agent-assistert | MCP-vertsagenten oversetter biter returnert av `start_markdown_agent_translation` eller `start_notebook_agent_translation`. | Ingen Co-op Translator LLM-leverandørlegitimasjon kreves for Markdown- eller notatbokbiter. Bildeoversettelse dekkes ikke av agent-assistert modus ennå. |

Hvis du begynner med Markdown- eller notatbokoversettelse inne i en agent som Codex eller Claude Code, start med agent-assistert modus. Bruk provider-støttet modus når du vil at Co-op Translator selv skal kalle dine konfigurerte leverandører, når du oversetter bilder, eller når du kjører repositorie-nivå oversettelse som CLI-en.

Konfigurer leverandørlegitimasjon kun for provider-støttede arbeidsflyter:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-støttet bildeoversettelse trenger i tillegg:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assistert modus dekker for øyeblikket Markdown og Markdown-celler i notatbøker. Bildeoversettelse bruker fortsatt den provider-støttede bilde-pipelinen og krever Azure AI Vision for OCR og layout-bevisst gjengivelse.

## Trinn 2: Konfigurer din MCP-klient

For det normale lokale `stdio`-oppsettet, legg til Co-op Translator i din MCP-klientkonfigurasjon. Klienten vil starte og stoppe prosessen automatisk.

Installert pakkekonfigurasjon:

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

Kildekassekonfigurasjon på Windows:

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

Kildekassekonfigurasjon på macOS eller Linux:

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

Etter å ha endret MCP-klientkonfigurasjonen, restart eller last klienten på nytt slik at den kan oppdage den nye serveren.

## Trinn 3: Verifiser serveren i klienten

Be MCP-klienten liste tilgjengelige verktøy, eller kall en av de skrivebeskyttede hjelpefunksjonene først:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Nyttige første kontroller:

| Verktøy | Hva du bør sjekke |
| --- | --- |
| `get_api_overview` | Bekrefter at serveren er tilgjengelig og viser tilgjengelige arbeidsflyter. |
| `list_supported_languages` | Bekrefter at pakkede språkdata kan lastes. |
| `get_configuration_status` | Bekrefter tilgjengeligheten til LLM- og Vision-leverandører uten å avsløre hemmelige verdier. |

## Trinn 4: Velg en arbeidsflyt

### Oversett individuelle filer eller dokumenter

Bruk provider-støttede innholdsverktøy når MCP-klienten allerede har dokumentinnhold eller en bildefilbane og Co-op Translator skal kalle de konfigurerte oversettelsesleverandørene.

For Markdown:

1. Kall `translate_markdown_content` med `document`, `language_code`, og eventuelt `source_path`.
2. Hvis det oversatte resultatet skal skrives inn i et Co-op Translator-utdataoppsett, kall `rewrite_markdown_paths`.
3. La klienten skrive eller returnere den endelige `content`.

For notatbøker:

1. Kall `translate_notebook_content` med notatbok-JSON og `language_code`.
2. Kall `rewrite_notebook_paths` hvis oversatte notatboklenker må justeres for en målsti.
3. Skriv eller returner den endelige notatbok-JSON-en.

For bilder:

1. Kall `translate_image_content` med `image_path`, `language_code`, og eventuelt `root_dir` eller `fast_mode`.
2. Les den returnerte `data_base64` og `mime_type`.
3. Hvis `output_path` er oppgitt, lagres også det oversatte bildet til den stien.

Innholdsverktøyene utfører ikke prosjektdiscovery, metadataoppdateringer, ansvarsfraskrivelser eller automatisk sti-omskriving. Hvis du ønsker at vertsagenten skal oversette Markdown- eller notatbokbiter uten Co-op Translator LLM-leverandørlegitimasjon, bruk den agent-assisterte arbeidsflyten nedenfor.

### Oversett med vertsagentmodellen

Bruk agent-assisterte verktøy når du vil at MCP-vertsagenten, slik som en kodeassistent, skal produsere den oversatte teksten i stedet for å konfigurere Azure OpenAI eller OpenAI for Co-op Translator.

I en chat-basert MCP-klient trenger du normalt ikke å skrive verktøy-JSON selv. Be agenten bruke den agent-assisterte arbeidsflyten:

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

Hvis din MCP-klient støtter serverprompter, bruk `agent_assisted_markdown_translation_prompt` for at klienten skal laste de samme arbeidsflytinstruksjonene.

For Markdown:

1. Kall `start_markdown_agent_translation` med `document`, `language_code`, og eventuelt `source_path`.
2. Oversett hver returnerte bit i vertsagenten ved å følge bitens `prompt`.
3. Kall `finish_markdown_agent_translation` med den originale `job` og oversatte biter ved å bruke `chunk_id` og `translated_text`.
4. Hvis innholdet skal skrives til en oversatt målsti, kall `rewrite_markdown_paths`.

For notatbøker:

1. Kall `start_notebook_agent_translation` med notatbok-JSON og `language_code`.
2. Oversett hver returnerte bit i vertsagenten.
3. Kall `finish_notebook_agent_translation` med den originale `job` og oversatte biter.
4. Kall `rewrite_notebook_paths` hvis oversatte notatboklenker må justeres for en målsti.

Agent-assisterte verktøy kaller ikke Azure OpenAI eller OpenAI fra Co-op Translator. Vertsagenten er ansvarlig for å oversette de returnerte bitene. Co-op Translator håndterer Markdown-chunking, bevaring av plassholdere, gjenoppbygging av frontmatter, erstatning av notatbokceller og normalisering etter oversettelse.

### Oversett et helt prosjekt

Bruk `run_translation` når brukeren ønsker at Co-op Translator skal oppføre seg som `translate` CLI-en.

Prosjektoversettelse har som standard `dry_run=true` slik at en agent kan inspisere omfanget før filendringer:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

For å tillate skriving må kalleren sette både `dry_run=false` og `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` eksponeres som et kompatibilitetsalias for `run_translation`.

### Gjennomgå oversatt innhold

Bruk `run_review` for deterministiske sjekker som ikke krever LLM- eller Vision-legitimasjon:

!!! note "Beta"
    MCP eksponerer den betatele `run_review`-API-en. Den er trygg for skrivebeskyttede gjennomgangsarbeidsflyter, men gjennomgangssjekker og issue-skjemaer kan utvikle seg.

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

Manuelle kjøringer er hovedsakelig for feilsøking eller for transporter som oppfører seg som langlevde servere.

Feilsøk standard stdio-serveren:

```bash
co-op-translator-mcp
```

Kjør fra en kildekasseutgave:

```bash
python -m co_op_translator.mcp.server
```

Kjør en langlevd HTTP- eller SSE-server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

For lokale redaktør- og agentintegrasjoner, foretrekk klientadministrert `stdio`-konfigurasjon i Trinn 2.

## Verktøy

| Verktøy | Formål | Skriver filer |
| --- | --- | --- |
| `translate_markdown_content` | Oversett en Markdown-streng. | Nei |
| `translate_notebook_content` | Oversett Markdown-celler i notatbok-JSON. | Nei |
| `translate_image_content` | Oversett tekst i ett bilde og returner base64-bildedata. | Valgfritt, kun når `output_path` er oppgitt |
| `start_markdown_agent_translation` | Forbered Markdown-biter for vertsagenten slik at de kan oversettes uten Co-op Translator LLM-legitimasjon. | Nei |
| `finish_markdown_agent_translation` | Rekonstruer Markdown fra vertsagent-oversatte biter. | Nei |
| `start_notebook_agent_translation` | Forbered notatbok Markdown-cellebiter for vertsagenten å oversette. | Nei |
| `finish_notebook_agent_translation` | Rekonstruer notatbok-JSON fra vertsagent-oversatte biter. | Nei |
| `rewrite_markdown_paths` | Omskriv Markdown-body og frontmatter-stier for et oversatt mål. | Nei |
| `rewrite_notebook_paths` | Omskriv stier inne i notatbok Markdown-celler. | Nei |
| `run_translation` | Kjør prosjekt-nivå oversettelse som CLI-en. | Ja når `dry_run=false` og `confirm_write=true` |
| `translate_project` | Kompatibilitetsalias for `run_translation`. | Ja når `dry_run=false` og `confirm_write=true` |
| `run_review` | Kjør deterministiske gjennomgangssjekker. | Nei |
| `get_configuration_status` | Rapporter konfigurerte LLM- og Vision-leverandører uten å eksponere hemmeligheter. | Nei |
| `list_supported_languages` | List støttede mål-språkkoder. | Nei |
| `get_api_overview` | Beskriv tilgjengelige MCP-arbeidsflyter og verktøy. | Nei |

## Ressurser

| Ressurs-URI | Formål |
| --- | --- |
| `co-op://api` | JSON-oversikt over arbeidsflyter og verktøy. |
| `co-op://supported-languages` | JSON-liste over støttede språkkoder. |
| `co-op://configuration` | JSON-oppsummering av leverandørtilgjengelighet uten hemmeligheter. |

## Prompter

| Prompt | Formål |
| --- | --- |
| `translate_markdown_document_prompt` | Veilede en MCP-klient gjennom innholdsoversettelse pluss valgfri sti-omskriving. |
| `agent_assisted_markdown_translation_prompt` | Veilede en MCP-klient gjennom vertsagent Markdown-oversettelse uten Co-op Translator LLM-leverandørlegitimasjon. |
| `translate_repository_prompt` | Veilede en MCP-klient gjennom prosjektoversettelse som starter med dry-run. |

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
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

Oversett Markdown med vertsagentmodellen:

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

Etter at vertsagenten har oversatt hver returnerte bit, fullfør jobben med hele `job`-objektet returnert av `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Forhåndsvis prosjektoversettelse:

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
| MCP-klienten finner ikke `co-op-translator-mcp`. | Bruk den absolutte Python-eksekverbare banen og `["-m", "co_op_translator.mcp.server"]` source checkout-konfigurasjonen. |
| Serveren er listet, men oversettelsen feiler. | Kall `get_configuration_status` og bekreft at en LLM-leverandør er tilgjengelig. |
| Du vil ha Markdown- eller notatbokoversettelse uten Azure OpenAI/OpenAI-nøkler. | Bruk `start_markdown_agent_translation` / `finish_markdown_agent_translation` eller de tilsvarende for notatbøker slik at vertsagenten oversetter bitene. |
| Bildeoversettelse feiler. | Bekreft at Azure AI Vision-variabler er satt og kall `get_configuration_status`. |
| Repositorieoversettelse skriver ikke filer. | Sett `dry_run=false` og `confirm_write=true` bare etter eksplisitt brukerbekreftelse. |
| Endringer i klientkonfigurasjonen vises ikke. | Restart eller last MCP-klienten på nytt. |

## Sikkerhetsmerknader

- MCP-verktøykall styres av modellen i vertsapplikasjonen, så repositorieoversettelse er som standard en dry-run.
- Full repositorieoversettelse kan opprette, oppdatere eller fjerne mange filer. Krev eksplisitt brukerbekreftelse før du setter `confirm_write=true`.
- Konfigurasjonsstatusverktøyet returnerer aldri API-nøkler, endepunkter eller andre hemmelige verdier.
- Bildeoversettelse returnerer base64 bildedata. Store bilder kan gi store verktøysvar.
- Agent-assisterte verktøy returnerer kildebiter og prompter til MCP-vertsagenten. Bruk dem bare med innhold brukeren er komfortabel med å sende til den vertsagentmodellen.