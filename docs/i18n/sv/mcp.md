# MCP-server

Co-op Translator inkluderar en Model Context Protocol-server för agenter, redaktörer och MCP-kompatibla klienter.

För standardlokal installation behöver användare inte köra en separat server manuellt. De konfigurerar sin MCP-klient, och klienten startar `co-op-translator-mcp` automatiskt över `stdio` när den behöver Co-op Translator-verktyg.

Om du väljer mellan CLI, Python API och MCP, börja med [Välj ditt arbetsflöde](workflows.md).

Använd MCP när en agent eller redaktör ska anropa Co-op Translator direkt:

| Användarmål | MCP-verktyg |
| --- | --- |
| Översätt ett Markdown-dokument, en notebook eller en bild | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Översätt Markdown- eller notebook-innehåll med värdagentmodellen | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Skriv om översatta Markdown- eller notebook-länkar efter att målvägen valts | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Översätt ett helt repository som CLI:n | `run_translation`, `translate_project` |
| Granska översatt innehåll utan LLM-uppgifter | `run_review` |
| Kontrollera funktioner och miljöstatus | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP-servern omsluter samma publika Python-API som dokumenteras i [Python API](api.md). Provider-stödda verktyg använder samma konfigurerade leverantörer som CLI och Python API. Agentassisterade verktyg förbereder chunkar för MCP-värdagenten att översätta, och använder sedan Co-op Translator för att återskapa slutlig Markdown eller notebook.

## Steg 1: Installera och konfigurera Co-op Translator

Installera Co-op Translator i den Python-miljö som din MCP-klient kommer att använda:

```bash
pip install co-op-translator
```

För lokal utveckling från detta repository, installera paketet i redigerbart läge:

```bash
pip install -e .
```

Välj det översättningsläge som din MCP-klient kommer att använda:

| Läge | Använd detta för | Autentiseringsuppgifter |
| --- | --- | --- |
| Leverantörsstödd | Co-op Translator anropar `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, eller `run_translation`. | Markdown- och notebook-översättning kräver Azure OpenAI eller OpenAI. Bildöversättning kräver dessutom Azure AI Vision. |
| Agentassisterad | MCP-värdagenten översätter chunkar som returneras av `start_markdown_agent_translation` eller `start_notebook_agent_translation`. | Inga Co-op Translator LLM-leverantörsautentiseringsuppgifter krävs för Markdown- eller notebookchunkar. Bildöversättning täcks ännu inte av agentassisterat läge. |

Om du börjar med Markdown- eller notebook-översättning inuti en agent som Codex eller Claude Code, börja med agentassisterat läge. Använd leverantörsstödd läge när du vill att Co-op Translator själv ska anropa dina konfigurerade leverantörer, när du översätter bilder, eller när du kör översättning på projektnivå som CLI:n.

Konfigurera leverantörsautentiseringsuppgifter endast för leverantörsstödda arbetsflöden:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Leverantörsstödd bildöversättning kräver dessutom:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agentassisterat läge täcker för närvarande Markdown och notebook Markdown-celler. Bildöversättning använder fortfarande den leverantörsstödda bildpipen och kräver Azure AI Vision för OCR och layoutmedveten rendering.

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

Be MCP-klienten lista tillgängliga verktyg, eller anropa en av de skrivskyddade hjälparna först:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Användbara första kontroller:

| Verktyg | Vad att kontrollera |
| --- | --- |
| `get_api_overview` | Bekräftar att servern är nåbar och visar tillgängliga arbetsflöden. |
| `list_supported_languages` | Bekräftar att paketdata för språk kan laddas. |
| `get_configuration_status` | Bekräftar tillgänglighet för LLM- och Vision-leverantörer utan att exponera hemliga värden. |

## Steg 4: Välj ett arbetsflöde

### Översätt enskilda filer eller dokument

Använd leverantörsstödda innehållsverktyg när MCP-klienten redan har dokumentinnehåll eller en bildväg och Co-op Translator ska anropa de konfigurerade översättningsleverantörerna.

För Markdown:

1. Anropa `translate_markdown_content` med `document`, `language_code` och valfritt `source_path`.
2. Om det översatta resultatet ska skrivas till en Co-op Translator-utdata-layout, anropa `rewrite_markdown_paths`.
3. Låt klienten skriva eller returnera slutligt `content`.

För notebooks:

1. Anropa `translate_notebook_content` med notebook-JSON och `language_code`.
2. Anropa `rewrite_notebook_paths` om översatta notebook-länkar behöver justeras för en målväg.
3. Skriv eller returnera slutligt notebook-JSON.

För bilder:

1. Anropa `translate_image_content` med `image_path`, `language_code` och valfritt `root_dir` eller `fast_mode`.
2. Läs den returnerade `data_base64` och `mime_type`.
3. Om `output_path` anges sparas den översatta bilden också till den sökvägen.

Innehållsverktygen utför inte projektdetektering, metadatauppdateringar, ansvarsfriskrivningar eller automatisk omskrivning av sökvägar. Om du vill att värdagenten ska översätta Markdown- eller notebook-chunkar utan Co-op Translator LLM-leverantörsautentiseringsuppgifter, använd det agentassisterade arbetsflödet nedan.

### Översätt med värdagentmodellen

Använd agentassisterade verktyg när du vill att MCP-värdagenten, som en kodningsassistent, ska producera den översatta texten istället för att konfigurera Azure OpenAI eller OpenAI för Co-op Translator.

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

Om din MCP-klient stöder serverpromptar, använd `agent_assisted_markdown_translation_prompt` för att låta klienten ladda samma arbetsflödesinstruktioner.

För Markdown:

1. Anropa `start_markdown_agent_translation` med `document`, `language_code` och valfritt `source_path`.
2. Översätt varje returnerad chunk i värdagenten genom att följa chunkens `prompt`.
3. Anropa `finish_markdown_agent_translation` med det ursprungliga `job` och översatta chunkar med `chunk_id` och `translated_text`.
4. Om innehållet ska skrivas till en översatt målväg, anropa `rewrite_markdown_paths`.

För notebooks:

1. Anropa `start_notebook_agent_translation` med notebook-JSON och `language_code`.
2. Översätt varje returnerad chunk i värdagenten.
3. Anropa `finish_notebook_agent_translation` med det ursprungliga `job` och översatta chunkar.
4. Anropa `rewrite_notebook_paths` om översatta notebook-länkar behöver justeras för målvägen.

Agentassisterade verktyg anropar inte Azure OpenAI eller OpenAI från Co-op Translator. Värdagenten är ansvarig för att översätta de returnerade chunkarna. Co-op Translator hanterar Markdown-chunkning, bevarande av platshållare, återuppbyggnad av frontmatter, ersättning av notebook-celler och post-översättningsnormalisering.

### Översätt ett helt repository

Använd `run_translation` när användaren vill att Co-op Translator ska bete sig som `translate` CLI.

Repository-översättning är som standard `dry_run=true` så att en agent kan granska omfattningen innan filändringar:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

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

### Granska översatt innehåll

Använd `run_review` för deterministiska kontroller som inte kräver LLM- eller Vision-autentiseringsuppgifter:

!!! note "Beta"
    MCP exponerar beta-API:t `run_review`. Det är säkert för skrivskyddade granskningsarbetsflöden, men granskningskontroller och ärendescheman kan utvecklas.

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

Manuella körningar är främst för felsökning eller för transportsätt som beter sig som långlivade servrar.

Felsök standard-stdio-servern:

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

För lokala editor- och agentintegrationer, föredra klienthanterad `stdio`-konfiguration i Steg 2.

## Verktyg

| Verktyg | Syfte | Skriver filer |
| --- | --- | --- |
| `translate_markdown_content` | Översätt en Markdown-sträng. | Nej |
| `translate_notebook_content` | Översätt Markdown-celler i notebook-JSON. | Nej |
| `translate_image_content` | Översätt text i en bild och returnera base64-bilddata. | Valfritt, endast när `output_path` anges |
| `start_markdown_agent_translation` | Förbered Markdown-chunkar för att värdagenten ska översätta utan Co-op Translator LLM-leverantörsautentiseringsuppgifter. | Nej |
| `finish_markdown_agent_translation` | Återskapa Markdown från värdagentens översatta chunkar. | Nej |
| `start_notebook_agent_translation` | Förbered notebook Markdown-cellchunkar för att värdagenten ska översätta. | Nej |
| `finish_notebook_agent_translation` | Återskapa notebook-JSON från värdagentens översatta chunkar. | Nej |
| `rewrite_markdown_paths` | Omskriv Markdown-body och frontmatter-sökvägar för en översatt målväg. | Nej |
| `rewrite_notebook_paths` | Omskriv sökvägar i notebook Markdown-celler. | Nej |
| `run_translation` | Kör projektöversättning som CLI. | Ja när `dry_run=false` och `confirm_write=true` |
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

## Promptar

| Prompt | Syfte |
| --- | --- |
| `translate_markdown_document_prompt` | Vägled en MCP-klient genom innehållsöversättning plus valfri omskrivning av sökvägar. |
| `agent_assisted_markdown_translation_prompt` | Vägled en MCP-klient genom värdagent-översättning av Markdown utan Co-op Translator LLM-leverantörsautentiseringsuppgifter. |
| `translate_repository_prompt` | Vägled en MCP-klient genom repository-översättning med först en dry-run. |

## Kopiera-klistra-exempel

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

Skriv om översatta Markdown-länkar:

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

Efter att värdagenten översatt varje returnerad chunk, avsluta jobbet med det fullständiga `job`-objektet som returnerades av `start_markdown_agent_translation`:

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

| Problem | Vad att prova |
| --- | --- |
| MCP-klienten kan inte hitta `co-op-translator-mcp`. | Använd den absoluta Python-exekverbara sökvägen och `["-m", "co_op_translator.mcp.server"]` källutcheckningskonfiguration. |
| Servern listas men översättning misslyckas. | Anropa `get_configuration_status` och bekräfta att en LLM-leverantör är tillgänglig. |
| Du vill ha Markdown- eller notebook-översättning utan Azure OpenAI/OpenAI-nycklar. | Använd `start_markdown_agent_translation` / `finish_markdown_agent_translation` eller motsvarande för notebooks så att värdagenten översätter chunkarna. |
| Bildöversättning misslyckas. | Bekräfta att Azure AI Vision-variabler är inställda och anropa `get_configuration_status`. |
| Repository-översättning skriver inte filer. | Sätt `dry_run=false` och `confirm_write=true` endast efter uttryckligt användarsamtycke. |
| Ändringar i klientkonfigurationen syns inte. | Starta om eller ladda om MCP-klienten. |

## Säkerhetsanteckningar

- MCP-verktygsanrop styrs av modellen i värdapplikationen, så repository-översättning är som standard en dry-run.
- Fullständig repository-översättning kan skapa, uppdatera eller ta bort många filer. Kräv uttryckligt användargodkännande innan du sätter `confirm_write=true`.
- Konfigurationsstatusverktyget returnerar aldrig API-nycklar, endpoints eller andra hemliga värden.
- Bildöversättning returnerar base64-bilddata. Stora bilder kan ge stora verktygsresponser.
- Agentassisterade verktyg returnerar källchunkar och promptar till MCP-värden. Använd dem endast med innehåll som användaren är bekväm med att skicka till den värdagentsmodellen.