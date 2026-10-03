# MCP-server

Co-op Translator inkluderar en Model Context Protocol-server för agenter, redaktörer och MCP-kompatibla klienter.

För standardlokal konfiguration kör inte användare en separat server manuellt. De konfigurerar sin MCP-klient, och klienten startar `co-op-translator-mcp` automatiskt över `stdio` när den behöver Co-op Translator-verktyg.

Om du ska välja mellan CLI, Python API och MCP, börja med [Välj ditt arbetsflöde](workflows.md).

Använd MCP när en agent eller redaktör ska anropa Co-op Translator direkt:

| Användarmål | MCP-verktyg |
| --- | --- |
| Översätt ett Markdown-dokument, en notebook eller en bild | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Översätt Markdown- eller notebookinnehåll med värdagentmodellen | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Omskriv översatta Markdown- eller notebook-länkar efter att ha valt utdata-sökväg | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Översätt ett helt repository som CLI:n | `run_translation`, `translate_project` |
| Granska översatt utdata utan LLM-inloggningsuppgifter | `run_review` |
| Kontrollera funktioner och miljöstatus | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP-servern omsluter samma publika Python-API som dokumenteras i [Python-API](api.md). Leverantörsbaserade verktyg använder samma konfigurerade leverantörer som CLI och Python-API:t. Agentassisterade verktyg förbereder chunkar för MCP-värdagenten att översätta, och använder sedan Co-op Translator för att rekonstruera slutligt Markdown eller notebook.

## Steg 1: Installera och konfigurera Co-op Translator

Installera Co-op Translator i den Python-miljö som din MCP-klient kommer att använda:

```bash
pip install co-op-translator
```

För lokal utveckling från det här repositoryt, installera paketet i redigerbart läge:

```bash
pip install -e .
```

Välj översättningsläge som din MCP-klient ska använda:

| Läge | Använd detta för | Autentiseringsuppgifter |
| --- | --- | --- |
| Leverantörsbaserat | Co-op Translator anropar `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, eller `run_translation`. | Översättning kräver Azure OpenAI, OpenAI eller Anthropic. Bildöversättning kräver dessutom Azure AI Vision. |
| Agentassisterat | MCP-värdagenten översätter chunkar som returneras av `start_markdown_agent_translation` eller `start_notebook_agent_translation`. | Inga Co-op Translator LLM-leverantörsuppgifter krävs för Markdown- eller notebook-chunkar. Bildöversättning täcks inte av agentassisterat läge ännu. |

Om du börjar med Markdown- eller notebook-översättning inuti en agent som Codex eller Claude Code, börja med agentassisterat läge. Använd leverantörsbaserat läge när du vill att Co-op Translator själv ska anropa dina konfigurerade leverantörer, när du översätter bilder, eller när du kör översättning på repositorienivå som CLI:n.

Konfigurera en leverantör för leverantörsbaserade arbetsflöden:

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

Leverantörsbaserad bildöversättning kräver dessutom:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agentassisterat läge täcker för närvarande Markdown och Markdown-celler i notebooks. Bildöversättning använder fortfarande den leverantörsbaserade bildpipen och kräver Azure AI Vision för OCR och layoutmedveten rendering.

## Steg 2: Konfigurera din MCP-klient

För den normala lokala `stdio`-konfigurationen, lägg till Co-op Translator i din MCP-klientkonfiguration. Klienten startar och stoppar processen automatiskt.

Konfiguration för installerat paket:

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

Konfiguration för källutcheckning på Windows:

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

Konfiguration för källutcheckning på macOS eller Linux:

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

Efter att ha ändrat MCP-klientens konfiguration, starta om eller ladda om klienten så att den kan upptäcka den nya servern.

## Steg 3: Verifiera servern i klienten

Be MCP-klienten lista tillgängliga verktyg, eller anropa först ett av de skrivskyddade hjälpverktygen:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Användbara första kontroller:

| Verktyg | Vad man ska kontrollera |
| --- | --- |
| `get_api_overview` | Bekräftar att servern är nåbar och visar tillgängliga arbetsflöden. |
| `list_supported_languages` | Bekräftar att paketerade språkdatan kan laddas. |
| `get_configuration_status` | Bekräftar tillgänglighet för LLM- och Vision-leverantörer utan att exponera hemliga värden. |

## Steg 4: Välj ett arbetsflöde

### Översätt enskilda filer eller dokument

Använd leverantörsbaserade innehållsverktyg när MCP-klienten redan har dokumentinnehåll eller en bildsökväg och Co-op Translator ska anropa de konfigurerade översättningsleverantörerna.

För Markdown:

1. Anropa `translate_markdown_content` med `document`, `language_code`, och valfritt `source_path`.
2. Om det översatta resultatet ska skrivas till en Co-op Translator-utdata-layout, anropa `rewrite_markdown_paths`.
3. Låt klienten skriva eller returnera det slutliga `content`.

För notebooks:

1. Anropa `translate_notebook_content` med notebookens JSON och `language_code`.
2. Anropa `rewrite_notebook_paths` om översatta notebook-länkar behöver justeras för en målsökväg.
3. Skriv eller returnera slutligt notebook-JSON.

För bilder:

1. Anropa `translate_image_content` med `image_path`, `language_code`, och valfritt `root_dir` eller `fast_mode`.
2. Läs det returnerade `data_base64` och `mime_type`.
3. Om `output_path` anges sparas också den översatta bilden på den sökvägen.

Innehållsverktygen utför inte projektupptäckt, metadatauppdateringar, ansvarsfriskrivningar eller automatisk omskrivning av sökvägar. Om du vill att värdagenten ska översätta Markdown- eller notebook-chunkar utan Co-op Translator LLM-leverantörsuppgifter, använd det agentassisterade arbetsflödet nedan.

### Översätt med värdagentmodellen

Använd agentassisterade verktyg när du vill att MCP-värdagenten, till exempel en kodassistent, ska producera den översatta texten istället för att konfigurera en LLM-leverantör för Co-op Translator.

I en chattbaserad MCP-klient behöver du normalt inte skriva verktygs-JSON själv. Be agenten använda det agentassisterade arbetsflödet:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

För notebooks, använd samma mönster:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Om din MCP-klient stödjer serverprompter, använd `agent_assisted_markdown_translation_prompt` för att få klienten att ladda samma arbetsflödesinstruktioner.

För Markdown:

1. Anropa `start_markdown_agent_translation` med `document`, `language_code` och valfritt `source_path`.
2. Översätt varje returnerad chunk i värdagenten genom att följa chunkens `prompt`.
3. Anropa `finish_markdown_agent_translation` med det ursprungliga `job` och de översatta chunkarna med `chunk_id` och `translated_text`.
4. Om innehållet ska skrivas till en översatt målsökväg, anropa `rewrite_markdown_paths`.

För notebooks:

1. Anropa `start_notebook_agent_translation` med notebookens JSON och `language_code`.
2. Översätt varje returnerad chunk i värdagenten.
3. Anropa `finish_notebook_agent_translation` med det ursprungliga `job` och de översatta chunkarna.
4. Anropa `rewrite_notebook_paths` om översatta notebook-länkar behöver justeras för målsökväg.

Agentassisterade verktyg anropar inte den konfigurerade LLM-leverantören från Co-op Translator. Värdagenten ansvarar för att översätta de returnerade chunkarna. Co-op Translator hanterar Markdown-chunkning, bevarande av platshållare, rekonstruktion av frontmatter, ersättning av notebook-celler och post-översättningsnormalisering.

### Översätt ett helt repository

Använd `run_translation` när användaren vill att Co-op Translator ska bete sig som `translate` CLI.

Repository-översättning har som standard `dry_run=true` så att en agent kan inspektera omfattningen innan filändringar:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Resultatet från `run_translation` inkluderar en `events`-array med versionerade
`co-op.translation.event.v1`-händelser för framsteg. MCP-klienter bör använda fält som
som `type`, `stage_key`, `completed`, `total` och `current_path` istället för
parsa fångad konsoltext. Skicka `json_events_path` för att även skriva dessa händelser
till en NDJSON-fil.

För att tillåta skrivningar måste anroparen sätta både `dry_run=false` och `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` exponeras som en kompatibilitetsalias för `run_translation`.

### Granska översatt utdata

Använd `run_review` för deterministiska kontroller som inte kräver LLM- eller Vision-inloggningsuppgifter:

!!! note "Beta"
    MCP exponerar beta-API:t `run_review`. Det är säkert för skrivskyddade granskningsarbetsflöden, men granskningskontroller och scheman för problem kan utvecklas.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Resultatet inkluderar fångad textutdata och en strukturerad granskningssammanfattning när sådan finns.

## Manuella serverkörningar

Manuella körningar är främst för felsökning eller för transportsätt som beter sig som långkörande servrar.

Felsök standard `stdio`-servern:

```bash
co-op-translator-mcp
```

Kör från en källutcheckning:

```bash
python -m co_op_translator.mcp.server
```

Kör en långlivad HTTP- eller SSE-server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

För lokala redaktörs- och agentintegrationer, föredra den klienthanterade `stdio`-konfigurationen i Steg 2.

## Verktyg

| Verktyg | Syfte | Skriver filer |
| --- | --- | --- |
| `translate_markdown_content` | Översätt en Markdown-sträng. | Nej |
| `translate_notebook_content` | Översätt Markdown-celler i notebook-JSON. | Nej |
| `translate_image_content` | Översätt text i en bild och returnera base64-bilddata. | Valfritt, endast när `output_path` anges |
| `start_markdown_agent_translation` | Förbered Markdown-chunkar för att värdagenten ska översätta utan Co-op Translator LLM-uppgifter. | Nej |
| `finish_markdown_agent_translation` | Rekonstruera Markdown från värdagentsöversatta chunkar. | Nej |
| `start_notebook_agent_translation` | Förbered notebook Markdown-cellchunkar för att värdagenten ska översätta. | Nej |
| `finish_notebook_agent_translation` | Rekonstruera notebook-JSON från värdagentsöversatta chunkar. | Nej |
| `rewrite_markdown_paths` | Omskriv Markdown-innehåll och frontmatter-sökvägar för ett översatt mål. | Nej |
| `rewrite_notebook_paths` | Omskriv sökvägar i notebook Markdown-celler. | Nej |
| `run_translation` | Kör projektnivå-översättning som CLI:n. | Ja när `dry_run=false` och `confirm_write=true` |
| `translate_project` | Kompatibilitetsalias för `run_translation`. | Ja när `dry_run=false` och `confirm_write=true` |
| `run_review` | Kör deterministiska granskningskontroller. | Nej |
| `get_configuration_status` | Rapportera konfigurerade LLM- och Vision-leverantörer utan att exponera hemligheter. | Nej |
| `list_supported_languages` | Lista stödda målspråkskoder. | Nej |
| `get_api_overview` | Beskriv tillgängliga MCP-arbetsflöden och verktyg. | Nej |

## Resurser

| Resurs-URI | Syfte |
| --- | --- |
| `co-op://api` | JSON-översikt över arbetsflöden och verktyg. |
| `co-op://supported-languages` | JSON-lista över stödda språkkoder. |
| `co-op://configuration` | JSON-sammanfattning av leverantörstillgänglighet utan hemligheter. |

## Prompter

| Prompt | Syfte |
| --- | --- |
| `translate_markdown_document_prompt` | Vägled en MCP-klient genom innehållsöversättning samt valfri omskrivning av sökvägar. |
| `agent_assisted_markdown_translation_prompt` | Vägled en MCP-klient genom värdagentens Markdown-översättning utan Co-op Translator LLM-leverantörsuppgifter. |
| `translate_repository_prompt` | Vägled en MCP-klient genom repositorieöversättning med dry-run först. |

## Klipp-och-klistraexempel

Översätt Markdown-innehåll:

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

Omskriv översatta Markdown-länkar:

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

Översätt Markdown med värdagentmodellen:

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

Efter att värdagenten översatt varje returnerad chunk, avsluta jobbet med det kompletta `job`-objektet som returnerades av `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Förhandsgranska repository-översättning:

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

## Felsökning

| Problem | Vad du kan prova |
| --- | --- |
| MCP-klienten kan inte hitta `co-op-translator-mcp`. | Använd den absoluta Python-exekverbara sökvägen och `["-m", "co_op_translator.mcp.server"]` source checkout-konfiguration. |
| Servern listas men översättning misslyckas. | Anropa `get_configuration_status` och bekräfta att en LLM-leverantör är tillgänglig. |
| Du vill ha Markdown- eller notebook-översättning utan leverantörsuppgifter. | Använd `start_markdown_agent_translation` / `finish_markdown_agent_translation` eller motsvarande för notebook så att värdagenten översätter chunkarna. |
| Bildöversättning misslyckas. | Bekräfta att Azure AI Vision-variabler är inställda och anropa `get_configuration_status`. |
| Repository-översättning skriver inte filer. | Sätt `dry_run=false` och `confirm_write=true` endast efter uttryckligt användargodkännande. |
| Ändringar i klientkonfigurationen syns inte. | Starta om eller ladda om MCP-klienten. |

## Säkerhetsnoteringar

- MCP-verktygsanrop styrs av värdapplikationens modell, så repository-översättning är som standard en förhandskörning (dry-run).
- Fullständig repository-översättning kan skapa, uppdatera eller ta bort många filer. Kräv uttryckligt användargodkännande innan du ställer in `confirm_write=true`.
- Verktyget för konfigurationsstatus returnerar aldrig API-nycklar, endpoints eller andra hemliga värden.
- Bildöversättning returnerar base64-bilddata. Stora bilder kan ge stora verktygsresponser.
- Agentassisterade verktyg returnerar källchunkar och prompts till MCP-värden. Använd dem endast med innehåll som användaren är bekväm med att skicka till den värdagentsmodellen.