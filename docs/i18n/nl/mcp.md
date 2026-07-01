# MCP-server

Co-op Translator bevat een Model Context Protocol-server voor agents, editors en MCP-compatibele clients.

Voor de standaard lokale setup houden gebruikers geen aparte server handmatig draaiende. Ze configureren hun MCP-client en de client start `co-op-translator-mcp` automatisch over `stdio` wanneer deze Co-op Translator-tools nodig heeft.

Als u moet kiezen tussen CLI, Python-API en MCP, begin dan met [Kies uw workflow](workflows.md).

Gebruik MCP wanneer een agent of editor Co-op Translator direct moet aanroepen:

| Gebruikersdoel | MCP-tools |
| --- | --- |
| Vertaal één Markdown-document, notebook of afbeelding | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Vertaal Markdown- of notebookinhoud met het host-agentmodel | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Herschrijf vertaalde Markdown- of notebooklinks na het kiezen van het uitvoerpad | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Vertaal een volledige repository zoals de CLI | `run_translation`, `translate_project` |
| Bekijk vertaald resultaat zonder LLM-referenties | `run_review` |
| Inspecteer mogelijkheden en omgevingsstatus | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

De MCP-server wikkelt dezelfde openbare Python-API in die gedocumenteerd is in [Python-API](api.md). Provider-ondersteunde tools gebruiken dezelfde geconfigureerde providers als de CLI en Python-API. Agent-ondersteunde tools bereiden chunks voor zodat de MCP-hostagent ze kan vertalen en gebruiken vervolgens Co-op Translator om het uiteindelijke Markdown of notebook te reconstrueren.

## Stap 1: Installeer en configureer Co-op Translator

Installeer Co-op Translator in de Python-omgeving die uw MCP-client zal gebruiken:

```bash
pip install co-op-translator
```

Voor lokale ontwikkeling vanuit deze repository, installeer het pakket in bewerkbare modus:

```bash
pip install -e .
```

Kies de vertaalmodus die uw MCP-client zal gebruiken:

| Modus | Gebruik dit voor | Referenties |
| --- | --- | --- |
| Provider-backed | Co-op Translator roept `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, of `run_translation` aan. | Markdown- en notebookvertaling vereisen Azure OpenAI of OpenAI. Afbeeldingsvertaling vereist ook Azure AI Vision. |
| Agent-assisted | De MCP-hostagent vertaalt chunks die worden geretourneerd door `start_markdown_agent_translation` of `start_notebook_agent_translation`. | Voor Markdown- of notebook-chunks zijn geen Co-op Translator LLM-providerreferenties vereist. Afbeeldingsvertaling wordt nog niet gedekt door de agent-ondersteunde modus. |

Als u begint met Markdown- of notebookvertaling binnen een agent zoals Codex of Claude Code, begin dan met de agent-ondersteunde modus. Gebruik provider-ondersteunde modus wanneer u wilt dat Co-op Translator zelf uw geconfigureerde providers aanroept, wanneer u afbeeldingen vertaalt, of wanneer u repository-niveau vertaling uitvoert zoals de CLI.

Configureer providerreferenties alleen voor provider-ondersteunde workflows:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-ondersteunde afbeeldingsvertaling heeft daarnaast nodig:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    De agent-ondersteunde modus dekt momenteel Markdown en notebook-Markdowncellen. Afbeeldingsvertaling gebruikt nog steeds de provider-ondersteunde afbeeldingspipeline en vereist Azure AI Vision voor OCR en lay-outbewuste rendering.

## Stap 2: Configureer uw MCP-client

Voor de normale lokale `stdio`-setup voegt u Co-op Translator toe aan uw MCP-clientconfiguratie. De client start en stopt het proces automatisch.

Configuratie bij geïnstalleerd pakket:

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

Broncheckoutconfiguratie op Windows:

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

Broncheckoutconfiguratie op macOS of Linux:

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

Vraag de MCP-client om beschikbare tools te tonen, of roep eerst een van de alleen-lezen hulpprogramma's aan:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Nuttige eerste controles:

| Tool | Wat te controleren |
| --- | --- |
| `get_api_overview` | Bevestigt dat de server bereikbaar is en toont beschikbare workflows. |
| `list_supported_languages` | Bevestigt dat verpakte taalgegevens kunnen worden geladen. |
| `get_configuration_status` | Bevestigt de beschikbaarheid van LLM- en Vision-providers zonder geheime waarden bloot te geven. |

## Stap 4: Kies een workflow

### Vertaal individuele bestanden of documenten

Gebruik provider-ondersteunde contenttools wanneer de MCP-client al documentinhoud of een afbeeldingspad heeft en Co-op Translator de geconfigureerde vertaalproviders moet aanroepen.

Voor Markdown:

1. Roep `translate_markdown_content` aan met `document`, `language_code`, en optioneel `source_path`.
2. Als het vertaalde resultaat naar een Co-op Translator-uitvoerlayout geschreven zal worden, roep `rewrite_markdown_paths` aan.
3. Laat de client de uiteindelijke `content` schrijven of retourneren.

Voor notebooks:

1. Roep `translate_notebook_content` aan met notebook-JSON en `language_code`.
2. Roep `rewrite_notebook_paths` aan als vertaalde notebooklinks moeten worden aangepast voor een doelpad.
3. Schrijf of retourneer de uiteindelijke notebook-JSON.

Voor afbeeldingen:

1. Roep `translate_image_content` aan met `image_path`, `language_code`, en optioneel `root_dir` of `fast_mode`.
2. Lees de geretourneerde `data_base64` en `mime_type`.
3. Als `output_path` is opgegeven, wordt de vertaalde afbeelding ook naar dat pad opgeslagen.

De contenttools voeren geen projectontdekking, metadata-updates, disclaimers of automatische padherschrijving uit. Als u wilt dat de hostagent Markdown- of notebookchunks vertaalt zonder Co-op Translator LLM-providerreferenties, gebruik dan de hieronder beschreven agent-ondersteunde workflow.

### Vertalen met het host-agentmodel

Gebruik agent-ondersteunde tools wanneer u wilt dat de MCP-hostagent, zoals een code-assistent, de vertaalde tekst produceert in plaats van Azure OpenAI of OpenAI voor Co-op Translator te configureren.

In een chat-gebaseerde MCP-client hoeft u normaal gesproken niet zelf tool-JSON te schrijven. Vraag de agent de agent-ondersteunde workflow te gebruiken:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Voor notebooks gebruikt u hetzelfde patroon:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Als uw MCP-client serverprompts ondersteunt, gebruik dan `agent_assisted_markdown_translation_prompt` zodat de client dezelfde workflowinstructies kan laden.

Voor Markdown:

1. Roep `start_markdown_agent_translation` aan met `document`, `language_code`, en optioneel `source_path`.
2. Vertaal elk teruggegeven chunk in de hostagent door de chunk-`prompt` te volgen.
3. Roep `finish_markdown_agent_translation` aan met de oorspronkelijke `job` en vertaalde chunks met gebruik van `chunk_id` en `translated_text`.
4. Als de inhoud naar een vertaald doelpad zal worden geschreven, roep `rewrite_markdown_paths` aan.

Voor notebooks:

1. Roep `start_notebook_agent_translation` aan met notebook-JSON en `language_code`.
2. Vertaal elk teruggegeven chunk in de hostagent.
3. Roep `finish_notebook_agent_translation` aan met de oorspronkelijke `job` en vertaalde chunks.
4. Roep `rewrite_notebook_paths` aan als vertaalde notebooklinks doelpadaanpassing nodig hebben.

Agent-ondersteunde tools roepen geen Azure OpenAI of OpenAI aan vanuit Co-op Translator. De hostagent is verantwoordelijk voor het vertalen van de geretourneerde chunks. Co-op Translator handelt Markdown-chunking, placeholder-behoud, frontmatter-reconstructie, vervanging van notebookcellen en normalisatie na vertaling af.

### Vertaal een volledige repository

Gebruik `run_translation` wanneer de gebruiker wil dat Co-op Translator zich gedraagt als de `translate` CLI.

Repositoryvertaling staat standaard op `dry_run=true` zodat een agent de scope kan inspecteren voordat bestanden worden gewijzigd:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

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

`translate_project` wordt aangeboden als een compatibiliteitsalias voor `run_translation`.

### Beoordeel vertaald resultaat

Gebruik `run_review` voor deterministische controles die geen LLM- of Vision-referenties vereisen:

!!! note "Beta"
    MCP stelt de bèta-API `run_review` beschikbaar. Deze is veilig voor alleen-lezen reviewworkflows, maar reviewcontroles en issuesschema's kunnen evolueren.

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

Voer uit vanuit een source checkout:

```bash
python -m co_op_translator.mcp.server
```

Draai een langlopende HTTP- of SSE-server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Voor lokale editor- en agentintegraties heeft de client- beheerde `stdio`-configuratie in Stap 2 de voorkeur.

## Hulpmiddelen

| Tool | Doel | Schrijft bestanden |
| --- | --- | --- |
| `translate_markdown_content` | Vertaal een Markdown-string. | Nee |
| `translate_notebook_content` | Vertaal Markdown-cellen in notebook-JSON. | Nee |
| `translate_image_content` | Vertaal tekst in één afbeelding en retourneer base64-afbeeldingsdata. | Optioneel, alleen wanneer `output_path` is opgegeven |
| `start_markdown_agent_translation` | Bereid Markdown-chunks voor zodat de hostagent ze kan vertalen zonder Co-op Translator LLM-providerreferenties. | Nee |
| `finish_markdown_agent_translation` | Reconstrueer Markdown uit door de hostagent vertaalde chunks. | Nee |
| `start_notebook_agent_translation` | Bereid notebook Markdown-celchunks voor zodat de hostagent ze kan vertalen. | Nee |
| `finish_notebook_agent_translation` | Reconstrueer notebook-JSON uit door de hostagent vertaalde chunks. | Nee |
| `rewrite_markdown_paths` | Herschrijf Markdown-body- en frontmatterpaden voor een vertaald doel. | Nee |
| `rewrite_notebook_paths` | Herschrijf paden binnen notebook-Markdowncellen. | Nee |
| `run_translation` | Voer projectniveauvertaling uit zoals de CLI. | Ja wanneer `dry_run=false` en `confirm_write=true` |
| `translate_project` | Compatibiliteitsalias voor `run_translation`. | Ja wanneer `dry_run=false` en `confirm_write=true` |
| `run_review` | Voer deterministische reviewcontroles uit. | Nee |
| `get_configuration_status` | Rapporteer geconfigureerde LLM- en Vision-providers zonder geheimen te onthullen. | Nee |
| `list_supported_languages` | Geef een lijst met ondersteunde doeltaalcodes. | Nee |
| `get_api_overview` | Beschrijf beschikbare MCP-workflows en tools. | Nee |

## Bronnen

| Resource URI | Doel |
| --- | --- |
| `co-op://api` | JSON-overzicht van workflows en tools. |
| `co-op://supported-languages` | JSON-lijst van ondersteunde taalcodes. |
| `co-op://configuration` | JSON-samenvatting van providerbeschikbaarheid zonder geheimen. |

## Prompts

| Prompt | Doel |
| --- | --- |
| `translate_markdown_document_prompt` | Leid een MCP-client door contentvertaling plus optionele padherschrijving. |
| `agent_assisted_markdown_translation_prompt` | Leid een MCP-client door host-agent Markdownvertaling zonder Co-op Translator LLM-providerreferenties. |
| `translate_repository_prompt` | Leid een MCP-client door repositoryvertaling met eerst dry-run. |

## Kopieer-plakvoorbeelden

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

Vertaal Markdown met het host-agentmodel:

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

Nadat de hostagent elk teruggegeven chunk heeft vertaald, voltooi het job met het volledige `job`-object dat door `start_markdown_agent_translation` is geretourneerd:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Voorbeeld van repositoryvertaling:

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

| Probleem | Wat te proberen |
| --- | --- |
| De MCP-client kan `co-op-translator-mcp` niet vinden. | Gebruik het absolute Python-uitvoerbare pad en de `["-m", "co_op_translator.mcp.server"]` source checkout-configuratie. |
| De server wordt vermeld maar vertaling faalt. | Roep `get_configuration_status` aan en bevestig dat een LLM-provider beschikbaar is. |
| U wilt Markdown- of notebookvertaling zonder Azure OpenAI/OpenAI-sleutels. | Gebruik `start_markdown_agent_translation` / `finish_markdown_agent_translation` of de notebook-equivalenten zodat de hostagent de chunks vertaalt. |
| Afbeeldingsvertaling faalt. | Bevestig dat Azure AI Vision-variabelen zijn ingesteld en roep `get_configuration_status` aan. |
| Repositoryvertaling schrijft geen bestanden. | Stel `dry_run=false` en `confirm_write=true` alleen in na uitdrukkelijke goedkeuring van de gebruiker. |
| Wijzigingen aan clientconfig verschijnen niet. | Herstart of herlaad de MCP-client. |

## Veiligheidsopmerkingen

- MCP-toolaanroepen worden door het hostprogramma gemodelleerd, dus repositoryvertaling is standaard dry-run.
- Volledige repositoryvertaling kan veel bestanden creëren, bijwerken of verwijderen. Vraag uitdrukkelijke goedkeuring van de gebruiker voordat u `confirm_write=true` instelt.
- De configuratiestatus-tool geeft nooit API-sleutels, endpoints of andere geheime waarden terug.
- Afbeeldingsvertaling retourneert base64-afbeeldingsdata. Grote afbeeldingen kunnen grote toolantwoorden genereren.
- Agent-ondersteunde tools retourneren bronchunks en prompts aan de MCP-host. Gebruik ze alleen met inhoud die de gebruiker comfortabel vindt om naar dat host-agentmodel te sturen.