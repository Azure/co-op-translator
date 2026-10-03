# MCP-server

Co-op Translator inkluderer en Model Context Protocol-server for agenter, redaktører og MCP-kompatible klienter.

For den normale lokale opsætning behøver brugere ikke køre en separat server manuelt. De konfigurerer deres MCP-klient, og klienten starter `co-op-translator-mcp` automatisk over `stdio`, når den har brug for Co-op Translator-værktøjer.

Hvis du skal vælge mellem CLI, Python API og MCP, start med [Vælg din arbejdsgang](workflows.md).

Brug MCP, når en agent eller redaktør skal kalde Co-op Translator direkte:

| Brugerens mål | MCP-værktøjer |
| --- | --- |
| Oversæt et Markdown-dokument, en notebook eller et billede | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Oversæt Markdown- eller notebook-indhold med værtsagentens model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Omskriv oversatte Markdown- eller notebook-links efter valg af outputsti | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Oversæt et helt repository som CLI'en | `run_translation`, `translate_project` |
| Gennemse oversat output uden LLM-legitimationsoplysninger | `run_review` |
| Undersøg kapaciteter og miljøstatus | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP-serveren omslutter den samme offentlige Python-API dokumenteret i [Python-API](api.md). Leverandør-understøttede værktøjer bruger de samme konfigurerede udbydere som CLI og Python-API. Agent-assisterede værktøjer forbereder chunks for MCP-værtsagenten til at oversætte, og bruger derefter Co-op Translator til at rekonstruere den endelige Markdown eller notebook.

## Trin 1: Installer og konfigurer Co-op Translator

Installer Co-op Translator i det Python-miljø, som din MCP-klient vil bruge:

```bash
pip install co-op-translator
```

For lokal udvikling fra dette repository, installer pakken i redigerbar tilstand:

```bash
pip install -e .
```

Vælg den oversættelsestilstand, som din MCP-klient vil bruge:

| Tilstand | Brug dette til | Legitimationsoplysninger |
| --- | --- | --- |
| Leverandør-understøttet | Co-op Translator kalder `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`. | Oversættelse kræver Azure OpenAI, OpenAI eller Anthropic. Billedeoversættelse kræver også Azure AI Vision. |
| Agent-assisteret | MCP-værtsagenten oversætter chunks returneret af `start_markdown_agent_translation` eller `start_notebook_agent_translation`. | Ingen Co-op Translator LLM-udbyder-legitimationsoplysninger kræves for Markdown- eller notebook-chunks. Billedeoversættelse dækkes endnu ikke af agent-assisteret tilstand. |

Hvis du starter med Markdown- eller notebook-oversættelse inden for en agent som Codex eller Claude Code, start med agent-assisteret tilstand. Brug leverandør-understøttet tilstand, når du vil have Co-op Translator til selv at kalde dine konfigurerede udbydere, når du oversætter billeder, eller når du kører repository-niveau oversættelse som CLI'en.

Konfigurer én udbyder for leverandør-understøttede arbejdsgange:

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

Leverandør-understøttet billedeoversættelse kræver derudover:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisteret tilstand dækker i øjeblikket Markdown og notebook Markdown-celler. Billedeoversættelse bruger stadig den leverandør-understøttede billedpipeline og kræver Azure AI Vision til OCR og layout-bevidst gengivelse.

## Trin 2: Konfigurer din MCP-klient

For den normale lokale `stdio`-opsætning, tilføj Co-op Translator til din MCP-klientkonfiguration. Klienten starter og stopper processen automatisk.

Konfiguration for installeret pakke:

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

Source checkout-konfiguration på Windows:

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

Source checkout-konfiguration på macOS eller Linux:

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

Efter ændring af MCP-klientkonfigurationen, genstart eller genindlæs klienten, så den kan opdage den nye server.

## Trin 3: Bekræft serveren i klienten

Bed MCP-klienten om at liste tilgængelige værktøjer, eller kald en af de skrivebeskyttede hjælpefunktioner først:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Nyttige første tjek:

| Værktøj | Hvad skal tjekkes |
| --- | --- |
| `get_api_overview` | Bekræfter, at serveren er tilgængelig og viser tilgængelige arbejdsgange. |
| `list_supported_languages` | Bekræfter, at indpakket sprogdata kan indlæses. |
| `get_configuration_status` | Bekræfter LLM- og Vision-udbyderes tilgængelighed uden at afsløre hemmelige værdier. |

## Trin 4: Vælg en arbejdsgang

### Oversæt enkelte filer eller dokumenter

Brug leverandør-understøttede indholdsværktøjer, når MCP-klienten allerede har dokumentindhold eller en billedsti, og Co-op Translator skal kalde de konfigurerede oversættelsesudbydere.

For Markdown:

1. Kald `translate_markdown_content` med `document`, `language_code`, og eventuelt `source_path`.
2. Hvis det oversatte resultat skal skrives ind i et Co-op Translator-outputlayout, kald `rewrite_markdown_paths`.
3. Lad klienten skrive eller returnere det endelige `content`.

For notebooks:

1. Kald `translate_notebook_content` med notebook-JSON og `language_code`.
2. Kald `rewrite_notebook_paths` hvis oversatte notebook-links skal justeres for en målsti.
3. Skriv eller returner den endelige notebook-JSON.

For billeder:

1. Kald `translate_image_content` med `image_path`, `language_code`, og eventuelt `root_dir` eller `fast_mode`.
2. Læs den returnerede `data_base64` og `mime_type`.
3. Hvis `output_path` er angivet, gemmes det oversatte billede også på den sti.

Indholdsværktøjerne udfører ikke projektopdagelse, metadataopdateringer, ansvarsfraskrivelser eller automatisk sti-omskrivning. Hvis du ønsker, at værtsagenten oversætter Markdown- eller notebook-chunks uden Co-op Translator LLM-udbyder-legitimationsoplysninger, brug den agent-assisterede arbejdsgang nedenfor.

### Oversæt med værtsagent-modellen

Brug agent-assisterede værktøjer, når du ønsker, at MCP-værtsagenten, f.eks. en kodeassistent, skal producere den oversatte tekst i stedet for at konfigurere en LLM-udbyder for Co-op Translator.

I en chatbaseret MCP-klient behøver du normalt ikke selv at skrive tool-JSON. Bed agenten om at bruge den agent-assisterede arbejdsgang:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

For notebooks, brug samme mønster:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Hvis din MCP-klient understøtter serverprompter, brug `agent_assisted_markdown_translation_prompt` for at få klienten til at indlæse de samme arbejdsgangsinstruktioner.

For Markdown:

1. Kald `start_markdown_agent_translation` med `document`, `language_code` og eventuelt `source_path`.
2. Oversæt hver returneret chunk i værtsagenten ved at følge chunk-`prompt`.
3. Kald `finish_markdown_agent_translation` med det oprindelige `job` og de oversatte chunks ved brug af `chunk_id` og `translated_text`.
4. Hvis indholdet skal skrives til en oversat målsti, kald `rewrite_markdown_paths`.

For notebooks:

1. Kald `start_notebook_agent_translation` med notebook-JSON og `language_code`.
2. Oversæt hver returneret chunk i værtsagenten.
3. Kald `finish_notebook_agent_translation` med det oprindelige `job` og de oversatte chunks.
4. Kald `rewrite_notebook_paths` hvis oversatte notebook-links skal justeres til en målsti.

Agent-assisterede værktøjer kalder ikke den konfigurerede LLM-udbyder fra Co-op Translator. Værtsagenten er ansvarlig for at oversætte de returnerede chunks. Co-op Translator håndterer Markdown-chunking, bevarelse af pladsholdere, rekonstruktion af frontmatter, udskiftning af notebook-celler og post-oversættelses-normalisering.

### Oversæt et helt repository

Brug `run_translation`, når brugeren ønsker, at Co-op Translator skal opføre sig som `translate`-CLI'en.

Repository-oversættelse har som standard `dry_run=true`, så en agent kan inspicere omfanget før filændringer:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Resultatet af `run_translation` inkluderer et `events`-array med versionerede
`co-op.translation.event.v1` fremskridtsbegivenheder. MCP-klienter bør bruge felter som
`type`, `stage_key`, `completed`, `total` og `current_path` i stedet for
at parse fanget konsoltekst. Angiv `json_events_path` for også at skrive disse begivenheder
til en NDJSON-fil.

For at tillade skrivninger skal kaldende part sætte både `dry_run=false` og `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` er eksponeret som et kompatibilitetsalias for `run_translation`.

### Gennemse oversat output

Brug `run_review` til deterministiske tjek, der ikke kræver LLM- eller Vision-legitimationsoplysninger:

!!! note "Beta"
    MCP eksponerer beta `run_review` API'en. Den er sikker til skrivebeskyttede gennemgangsarbejdsgange, men gennemgangstjek og issueskemaer kan udvikle sig.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Resultatet inkluderer fanget tekstoutput og et struktureret gennemgangsresumé, når det er tilgængeligt.

## Manuelle serverkørsler

Manuelle kørsler er primært til fejlfinding eller til transportsystemer, der opfører sig som langkørende servere.

Fejlfind den standard `stdio`-server:

```bash
co-op-translator-mcp
```

Kør fra et source checkout:

```bash
python -m co_op_translator.mcp.server
```

Kør en langvarig HTTP- eller SSE-server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

For lokale editor- og agentintegrationer, foretræk den klientstyrede `stdio`-konfiguration i trin 2.

## Værktøjer

| Værktøj | Formål | Skriver filer |
| --- | --- | --- |
| `translate_markdown_content` | Oversæt en Markdown-streng. | Nej |
| `translate_notebook_content` | Oversæt Markdown-celler i notebook-JSON. | Nej |
| `translate_image_content` | Oversæt tekst i et billede og returner base64 billeddata. | Valgfrit, kun når `output_path` er angivet |
| `start_markdown_agent_translation` | Forbered Markdown-chunks til at værtsagenten kan oversætte uden Co-op Translator LLM-legitimationsoplysninger. | Nej |
| `finish_markdown_agent_translation` | Genskab Markdown fra værtsagent-oversatte chunks. | Nej |
| `start_notebook_agent_translation` | Forbered notebook Markdown-celle-chunks til at værtsagenten kan oversætte. | Nej |
| `finish_notebook_agent_translation` | Genskab notebook-JSON fra værtsagent-oversatte chunks. | Nej |
| `rewrite_markdown_paths` | Omskriv Markdown-body og frontmatter-stier til et oversat mål. | Nej |
| `rewrite_notebook_paths` | Omskriv stier inden i notebook Markdown-celler. | Nej |
| `run_translation` | Kør projektniveau-oversættelse som CLI'en. | Ja når `dry_run=false` og `confirm_write=true` |
| `translate_project` | Kompatibilitetsalias for `run_translation`. | Ja når `dry_run=false` og `confirm_write=true` |
| `run_review` | Kør deterministiske gennemgangstjek. | Nej |
| `get_configuration_status` | Rapportér konfigurerede LLM- og Vision-udbydere uden at eksponere hemmeligheder. | Nej |
| `list_supported_languages` | List understøttede mål-sprogkoder. | Nej |
| `get_api_overview` | Beskriv tilgængelige MCP-arbejdsgange og værktøjer. | Nej |

## Ressourcer

| Ressource-URI | Formål |
| --- | --- |
| `co-op://api` | JSON-oversigt over arbejdsgange og værktøjer. |
| `co-op://supported-languages` | JSON-liste over understøttede sprogkoder. |
| `co-op://configuration` | JSON-oversigt over udbydertilgængelighed uden hemmeligheder. |

## Prompter

| Prompt | Formål |
| --- | --- |
| `translate_markdown_document_prompt` | Guide en MCP-klient gennem indholdsoversættelse plus valgfri sti-omskrivning. |
| `agent_assisted_markdown_translation_prompt` | Guide en MCP-klient gennem værtsagent Markdown-oversættelse uden Co-op Translator LLM-udbyder-legitimationsoplysninger. |
| `translate_repository_prompt` | Guide en MCP-klient gennem repository-oversættelse, hvor der først køres en dry-run. |

## Eksempler til kopi-og-indsæt

Oversæt Markdown-indhold:

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

Omskriv oversatte Markdown-links:

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

Oversæt Markdown med værtsagent-modellen:

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

Efter værtsagenten har oversat hver returneret chunk, afslut jobbet med det komplette `job`-objekt returneret af `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Forhåndsvis repository-oversættelse:

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

## Fejlfinding

| Problem | Hvad du kan prøve |
| --- | --- |
| MCP-klienten kan ikke finde `co-op-translator-mcp`. | Brug den absolutte Python-eksekverbare sti og `["-m", "co_op_translator.mcp.server"]` source checkout-konfiguration. |
| Serveren er listet, men oversættelse mislykkes. | Kald `get_configuration_status` og bekræft, at en LLM-udbyder er tilgængelig. |
| Du ønsker Markdown- eller notebook-oversættelse uden udbyderlegitimationsoplysninger. | Brug `start_markdown_agent_translation` / `finish_markdown_agent_translation` eller notebook-ækvivalenterne, så værtsagenten oversætter chunks. |
| Billedeoversættelse mislykkes. | Bekræft at Azure AI Vision-variabler er sat og kald `get_configuration_status`. |
| Repository-oversættelse skriver ikke filer. | Sæt `dry_run=false` og `confirm_write=true` kun efter udtrykkelig brugergodkendelse. |
| Ændringer i klientkonfigurationen dukker ikke op. | Genstart eller genindlæs MCP-klienten. |

## Sikkerhedsbemærkninger

- MCP-værktøjsopkald styres af modellen i værtsapplikationen, så repository-oversættelse er dry-run som standard.
- Fuldt repository-oversættelse kan oprette, opdatere eller fjerne mange filer. Kræv udtrykkelig brugergodkendelse før du sætter `confirm_write=true`.
- Konfigurationsstatus-værktøjet returnerer aldrig API-nøgler, endpoints eller andre hemmelige værdier.
- Billedeoversættelse returnerer base64 billeddata. Store billeder kan give store værktøjssvar.
- Agent-assisterede værktøjer returnerer kildechunks og prompter til MCP-værten. Brug dem kun med indhold, som brugeren er tryg ved at sende til den værtsagentmodel.