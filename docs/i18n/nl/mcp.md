# MCP-server

Co-op Translator bevat een Model Context Protocol-server voor agents, editors en MCP-compatibele clients.

Voor de standaard lokale setup houden gebruikers geen aparte server handmatig draaiend. Ze configureren hun MCP-client, en de client start `co-op-translator-mcp` automatisch over `stdio` wanneer deze Co-op Translator-tools nodig heeft.

Als je moet kiezen tussen CLI, Python API en MCP, begin met [Kies je workflow](workflows.md).

Gebruik MCP wanneer een agent of editor Co-op Translator direct moet aanroepen:

| User goal | MCP tools |
| --- | --- |
| Vertaal één Markdown-document, notebook of afbeelding | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Vertaal Markdown- of notebookinhoud met het host-agentmodel | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Herschrijf vertaalde Markdown- of notebooklinks nadat het uitvoerpad is gekozen | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Vertaal een volledige repository zoals de CLI | `run_translation`, `translate_project` |
| Beoordeel vertaald resultaat zonder LLM-referenties | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

De MCP-server wikkelt dezelfde publieke Python API in die gedocumenteerd is in [Python API](api.md). Tools die provider-gestuurd zijn gebruiken dezelfde geconfigureerde providers als de CLI en Python API. Agent-ondersteunde tools bereiden chunks voor zodat de MCP-hostagent ze kan vertalen en gebruiken daarna Co-op Translator om het uiteindelijke Markdown of notebook te reconstrueren.

## Stap 1: Installeer en configureer Co-op Translator

Installeer Co-op Translator in de Python-omgeving die je MCP-client zal gebruiken:

```bash
pip install co-op-translator
```

Voor lokale ontwikkeling vanuit deze repository, installeer het pakket in editable-modus:

```bash
pip install -e .
```

Kies de vertaalmodus die je MCP-client zal gebruiken:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator roept `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, of `run_translation` aan. | Vertaling vereist Azure OpenAI, OpenAI of Anthropic. Afbeeldingsvertaling vereist daarnaast ook Azure AI Vision. |
| Agent-assisted | De MCP-hostagent vertaalt chunks die teruggegeven worden door `start_markdown_agent_translation` of `start_notebook_agent_translation`. | Voor Markdown- of notebook-chunks zijn geen Co-op Translator LLM-providerreferenties vereist. Afbeeldingsvertaling valt nog niet onder agent-assisted modus. |

Als je begint met Markdown- of notebookvertaling binnen een agent zoals Codex of Claude Code, begin dan met agent-assisted modus. Gebruik provider-backed modus wanneer je wilt dat Co-op Translator zelf je geconfigureerde providers aanroept, wanneer je afbeeldingen vertaalt, of wanneer je project-brede vertaling uitvoert zoals de CLI.

Configureer één provider voor provider-backed workflows:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Of OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Of Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Provider-backed afbeeldingsvertaling heeft daarnaast nodig:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted modus dekt momenteel Markdown en notebook Markdown-cellen. Afbeeldingsvertaling gebruikt nog steeds de provider-backed image pipeline en vereist Azure AI Vision voor OCR en layout-bewuste rendering.

## Stap 2: Configureer je MCP-client

Voor de normale lokale `stdio`-configuratie voeg Co-op Translator toe aan je MCP-clientconfiguratie. De client zal het proces automatisch starten en stoppen.

Geïnstalleerd pakket configuratie:

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

Source checkout-configuratie op Windows:

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

Source checkout-configuratie op macOS of Linux:

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

Na het wijzigen van de MCP-clientconfiguratie, herstart of herlaad de client zodat deze de nieuwe server kan ontdekken.

## Stap 3: Verifieer de server in de client

Vraag de MCP-client om beschikbare tools op te sommen, of roep eerst een van de read-only helpers aan:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Nuttige eerste controles:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Bevestigt dat de server bereikbaar is en toont beschikbare workflows. |
| `list_supported_languages` | Bevestigt dat verpakte taalgegevens geladen kunnen worden. |
| `get_configuration_status` | Bevestigt beschikbaarheid van LLM- en Vision-providers zonder geheime waarden prijs te geven. |

## Stap 4: Kies een workflow

### Vertaal individuele bestanden of documenten

Gebruik provider-backed content-tools wanneer de MCP-client al documentinhoud of een afbeeldingspad heeft en Co-op Translator de geconfigureerde vertaalproviders moet aanroepen.

Voor Markdown:

1. Roep `translate_markdown_content` aan met `document`, `language_code`, en optioneel `source_path`.
2. Als het vertaalde resultaat naar een Co-op Translator output-layout geschreven wordt, roep dan `rewrite_markdown_paths` aan.
3. Laat de client de uiteindelijke `content` schrijven of retourneren.

Voor notebooks:

1. Roep `translate_notebook_content` aan met notebook JSON en `language_code`.
2. Roep `rewrite_notebook_paths` aan als vertaalde notebook-links aangepast moeten worden voor een doelpad.
3. Schrijf of retourneer de uiteindelijke notebook JSON.

Voor afbeeldingen:

1. Roep `translate_image_content` aan met `image_path`, `language_code`, en optioneel `root_dir` of `fast_mode`.
2. Lees de teruggegeven `data_base64` en `mime_type`.
3. Als `output_path` is opgegeven, wordt de vertaalde afbeelding ook naar dat pad opgeslagen.

De content-tools voeren geen projectontdekking, metadata-updates, disclaimers of automatische pad-herschrijving uit. Als je wilt dat de hostagent Markdown- of notebookchunks vertaalt zonder Co-op Translator LLM-providerreferenties, gebruik dan de hieronder beschreven agent-assisted workflow.

### Vertaal met het hostagent-model

Gebruik agent-assisted tools wanneer je wilt dat de MCP-hostagent, zoals een coding assistant, de vertaalde tekst produceert in plaats van een LLM-provider voor Co-op Translator te configureren.

In een chat-gebaseerde MCP-client hoef je normaal gesproken geen tool-JSON zelf te schrijven. Vraag de agent om de agent-assisted workflow te gebruiken:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Voor notebooks gebruik je hetzelfde patroon:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Als je MCP-client serverprompts ondersteunt, gebruik `agent_assisted_markdown_translation_prompt` zodat de client dezelfde workflowinstructies kan laden.

Voor Markdown:

1. Roep `start_markdown_agent_translation` aan met `document`, `language_code`, en optioneel `source_path`.
2. Vertaal elke teruggegeven chunk in de hostagent door de chunk-`prompt` te volgen.
3. Roep `finish_markdown_agent_translation` aan met de originele `job` en vertaalde chunks met `chunk_id` en `translated_text`.
4. Als de inhoud naar een vertaald doelpad geschreven zal worden, roep dan `rewrite_markdown_paths` aan.

Voor notebooks:

1. Roep `start_notebook_agent_translation` aan met notebook JSON en `language_code`.
2. Vertaal elke teruggegeven chunk in de hostagent.
3. Roep `finish_notebook_agent_translation` aan met de originele `job` en vertaalde chunks.
4. Roep `rewrite_notebook_paths` aan als vertaalde notebook-links aangepast moeten worden voor het doelpad.

Agent-assisted tools roepen de geconfigureerde LLM-provider van Co-op Translator niet aan. De hostagent is verantwoordelijk voor het vertalen van de teruggegeven chunks. Co-op Translator verzorgt Markdown-chunking, behoud van placeholders, reconstructie van frontmatter, vervanging van notebookcellen en post-vertalingsnormalisatie.

### Vertaal een volledige repository

Gebruik `run_translation` wanneer de gebruiker wil dat Co-op Translator zich gedraagt als de `translate` CLI.

De vertaling van een repository staat standaard op `dry_run=true` zodat een agent de reikwijdte kan inspecteren voordat bestandswijzigingen plaatsvinden:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Het resultaat van `run_translation` bevat een `events`-array met versieerde
`co-op.translation.event.v1` voortgangsevenementen. MCP-clients moeten velden gebruiken zoals
`type`, `stage_key`, `completed`, `total`, en `current_path` in plaats van
vastgehouden consoletekst te parsen. Geef `json_events_path` door om die evenementen
ook naar een NDJSON-bestand te schrijven.

Om schrijven toe te staan, moet de aanroeper zowel `dry_run=false` als `confirm_write=true` instellen:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` is blootgesteld als compatibiliteitsalias voor `run_translation`.

### Review van vertaald output

Gebruik `run_review` voor deterministische controles die geen LLM- of Vision-referenties vereisen:

!!! note "Beta"
    MCP biedt de bèta-API `run_review` aan. Deze is veilig voor read-only review-workflows, maar reviewcontroles en issueschema's kunnen evolueren.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Het resultaat bevat vastgelegde tekstuitvoer en een gestructureerde review-samenvatting wanneer beschikbaar.

## Handmatige serverruns

Handmatige runs zijn voornamelijk voor debugging of voor transports die zich gedragen als langlopende servers.

Debug de standaard stdio-server:

```bash
co-op-translator-mcp
```

Run vanuit een source checkout:

```bash
python -m co_op_translator.mcp.server
```

Run een langlopende HTTP- of SSE-server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Voor lokale editor- en agentintegraties heeft de voorkeur de client-beheerde `stdio`-configuratie uit Stap 2.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Vertaal Markdown-cellen in notebook JSON. | No |
| `translate_image_content` | Vertaal tekst in één afbeelding en geef base64-afbeeldingsgegevens terug. | Optioneel, alleen wanneer `output_path` is opgegeven |
| `start_markdown_agent_translation` | Bereid Markdown-chunks voor zodat het host-agent ze kan vertalen zonder Co-op Translator LLM-referenties. | No |
| `finish_markdown_agent_translation` | Reconstructeer Markdown uit door host-agent vertaalde chunks. | No |
| `start_notebook_agent_translation` | Bereid notebook Markdown-celchunks voor zodat het host-agent ze kan vertalen. | No |
| `finish_notebook_agent_translation` | Reconstructeer notebook JSON uit door host-agent vertaalde chunks. | No |
| `rewrite_markdown_paths` | Herschrijf Markdown-inhoud en frontmatter-paden voor een vertaald doel. | No |
| `rewrite_notebook_paths` | Herschrijf paden binnen notebook Markdown-cellen. | No |
| `run_translation` | Voer vertaling op projectniveau uit zoals de CLI. | Ja wanneer `dry_run=false` en `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Run deterministic review checks. | No |
| `get_configuration_status` | Rapporteer geconfigureerde LLM- en Vision-providers zonder geheimen bloot te leggen. | No |
| `list_supported_languages` | List supported target language codes. | No |
| `get_api_overview` | Beschrijf beschikbare MCP-workflows en -tools. | Nee |

## Bronnen

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON-overzicht van workflows en tools. |
| `co-op://supported-languages` | JSON-lijst van ondersteunde taalcodes. |
| `co-op://configuration` | JSON-samenvatting van providerbeschikbaarheid zonder geheimen. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Begeleid een MCP-client bij het vertalen van inhoud en optioneel het herschrijven van paden. |
| `agent_assisted_markdown_translation_prompt` | Begeleid een MCP-client bij host-agent Markdown-vertaling zonder referenties van de Co-op Translator LLM-provider. |
| `translate_repository_prompt` | Begeleid een MCP-client bij repositoryvertaling met eerst een proefrun. |

## Copy-Paste Voorbeelden

Vertaal Markdown-inhoud:

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

Herschrijf vertaalde Markdown-links:

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

Vertaal Markdown met het hostagent-model:

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

Nadat de hostagent elke teruggegeven chunk heeft vertaald, maak de job af met het volledige `job`-object dat door `start_markdown_agent_translation` is teruggegeven:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Preview van repositoryvertaling:

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

## Probleemoplossing

| Problem | What to try |
| --- | --- |
| De MCP-client kan `co-op-translator-mcp` niet vinden. | Gebruik het absolute pad naar de Python-executable en de `["-m", "co_op_translator.mcp.server"]` broncheckoutconfiguratie. |
| De server staat vermeld maar de vertaling faalt. | Roep `get_configuration_status` aan en bevestig dat een LLM-provider beschikbaar is. |
| U wilt Markdown- of notebookvertaling zonder providerreferenties. | Gebruik `start_markdown_agent_translation` / `finish_markdown_agent_translation` of de notebook-equivalenten zodat de host-agent de chunks vertaalt. |
| Afbeeldingsvertaling mislukt. | Bevestig dat Azure AI Vision-variabelen zijn ingesteld en roep `get_configuration_status` aan. |
| Repositoryvertaling schrijft geen bestanden. | Stel `dry_run=false` en `confirm_write=true` alleen in na expliciete goedkeuring door de gebruiker. |
| Wijzigingen in de clientconfiguratie verschijnen niet. | Herstart of herlaad de MCP-client. |

## Veiligheidsnotities

- MCP-toolaanroepen worden door het model van de hosttoepassing gecontroleerd, dus repositoryvertaling is standaard een proefrun.
- Volledige repositoryvertaling kan veel bestanden aanmaken, bijwerken of verwijderen. Vereis expliciete gebruikersgoedkeuring voordat `confirm_write=true` wordt ingesteld.
- De configuratiestatustool geeft nooit API-sleutels, endpoints of andere geheime waarden terug.
- Afbeeldingsvertaling retourneert base64-afbeeldingsgegevens. Grote afbeeldingen kunnen grote toolreacties veroorzaken.
- Hulpmiddelen met agentondersteuning geven bronchunks en prompts terug aan de MCP-host. Gebruik ze alleen met inhoud die de gebruiker comfortabel vindt om naar dat host-agentmodel te sturen.
