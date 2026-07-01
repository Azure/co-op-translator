# MCP Server

Co-op Translator inkluderer en Model Context Protocol-server til agenter, redaktører og MCP-kompatible klienter.

For den standard lokale opsætning holder brugerne ikke en separat server kørende manuelt. De konfigurerer deres MCP-klient, og klienten starter `co-op-translator-mcp` automatisk over `stdio`, når den har brug for Co-op Translator-værktøjer.

Hvis du vælger mellem CLI, Python API og MCP, start med [Choose Your Workflow](workflows.md).

Brug MCP, når en agent eller redaktør skal kalde Co-op Translator direkte:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP-serveren indpakker det samme offentlige Python-API dokumenteret i [Python API](api.md). Værktøjer, der bruger provider, anvender de samme konfigurerede udbydere som CLI og Python API. Agent-assisterede værktøjer forbereder chunks for MCP-host-agenten til at oversætte, og bruger derefter Co-op Translator til at rekonstruere den endelige Markdown eller notebook.

## Step 1: Install and Configure Co-op Translator

Installér Co-op Translator i det Python-miljø, som din MCP-klient vil bruge:

```bash
pip install co-op-translator
```

Til lokal udvikling fra dette repository, installér pakken i editable mode:

```bash
pip install -e .
```

Vælg den oversættelsestilstand, som din MCP-klient vil bruge:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator kalder `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, eller `run_translation`. | Markdown- og notebook-oversættelse kræver Azure OpenAI eller OpenAI. Billedoversættelse kræver også Azure AI Vision. |
| Agent-assisted | MCP-host-agenten oversætter chunks returneret af `start_markdown_agent_translation` eller `start_notebook_agent_translation`. | Ingen Co-op Translator LLM-provider-legitimationsoplysninger kræves for Markdown- eller notebook-chunks. Billedoversættelse dækkes endnu ikke af agent-assisted mode. |

Hvis du begynder med Markdown- eller notebook-oversættelse inde i en agent såsom Codex eller Claude Code, start med agent-assisted mode. Brug provider-backed mode, når du ønsker, at Co-op Translator selv skal kalde dine konfigurerede udbydere, når du oversætter billeder, eller når du kører projektomfattende oversættelse som CLI.

Konfigurer provider-legitimationsoplysninger kun for provider-backed workflows:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed billedoversættelse kræver desuden:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode dækker i øjeblikket Markdown og notebook Markdown-celler. Billedoversættelse bruger stadig den provider-backed billedpipeline og kræver Azure AI Vision til OCR og layout-aware gengivelse.

## Step 2: Configure Your MCP Client

For den normale lokale `stdio`-opsætning, tilføj Co-op Translator til din MCP-klientkonfiguration. Klienten vil starte og stoppe processen automatisk.

Installeret pakke-konfiguration:

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

## Step 3: Verify the Server in the Client

Bed MCP-klienten om at liste tilgængelige værktøjer, eller kald en af hjælpefunktionerne, der kun læser først:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Nyttige første checks:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Bekræfter, at serveren er tilgængelig og viser tilgængelige workflows. |
| `list_supported_languages` | Bekræfter, at pakkede sprogdata kan indlæses. |
| `get_configuration_status` | Bekræfter LLM- og Vision-provider-tilgængelighed uden at udsætte hemmelige værdier. |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

Brug provider-backed content-værktøjer, når MCP-klienten allerede har dokumentindhold eller en sti til et billede, og Co-op Translator skal kalde de konfigurerede oversættelsesudbydere.

For Markdown:

1. Kald `translate_markdown_content` med `document`, `language_code` og eventuelt `source_path`.
2. Hvis det oversatte resultat skal skrives ind i en Co-op Translator output-layout, kald `rewrite_markdown_paths`.
3. Lad klienten skrive eller returnere det endelige `content`.

For notebooks:

1. Kald `translate_notebook_content` med notebook JSON og `language_code`.
2. Kald `rewrite_notebook_paths` hvis oversatte notebook-links skal justeres til en målsti.
3. Skriv eller returner den endelige notebook JSON.

For billeder:

1. Kald `translate_image_content` med `image_path`, `language_code` og valgfrit `root_dir` eller `fast_mode`.
2. Læs de returnerede `data_base64` og `mime_type`.
3. Hvis `output_path` er angivet, gemmes det oversatte billede også på den sti.

Content-værktøjerne udfører ikke projektopdagelelse, metadata-opdateringer, disclaimers eller automatisk sti-omskrivning. Hvis du ønsker, at host-agenten skal oversætte Markdown- eller notebook-chunks uden Co-op Translator LLM-provider-legitimationsoplysninger, brug agent-assisted workflowet nedenfor.

### Translate with the Host Agent Model

Brug agent-assisted-værktøjer, når du ønsker, at MCP-host-agenten, såsom en kodeassistent, skal producere den oversatte tekst i stedet for at konfigurere Azure OpenAI eller OpenAI for Co-op Translator.

I en chat-baseret MCP-klient behøver du normalt ikke selv at skrive tool-JSON. Bed agenten om at bruge agent-assisted workflowet:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

For notebooks, brug det samme mønster:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Hvis din MCP-klient understøtter server prompts, brug `agent_assisted_markdown_translation_prompt` for at få klienten til at indlæse de samme workflow-instruktioner.

For Markdown:

1. Kald `start_markdown_agent_translation` med `document`, `language_code`, og eventuelt `source_path`.
2. Oversæt hver returneret chunk i host-agenten ved at følge chunk-`prompt`.
3. Kald `finish_markdown_agent_translation` med det oprindelige `job` og de oversatte chunks ved hjælp af `chunk_id` og `translated_text`.
4. Hvis indholdet skal skrives til en oversat målsti, kald `rewrite_markdown_paths`.

For notebooks:

1. Kald `start_notebook_agent_translation` med notebook JSON og `language_code`.
2. Oversæt hver returneret chunk i host-agenten.
3. Kald `finish_notebook_agent_translation` med det oprindelige `job` og de oversatte chunks.
4. Kald `rewrite_notebook_paths` hvis oversatte notebook-links skal justeres til målsti.

Agent-assisted værktøjer kalder ikke Azure OpenAI eller OpenAI fra Co-op Translator. Host-agenten er ansvarlig for at oversætte de returnerede chunks. Co-op Translator håndterer Markdown-chunking, bevarelse af pladsholdere, rekonstruktion af frontmatter, udskiftning af notebook-celler og post-oversættelses-normalisering.

### Translate an Entire Repository

Brug `run_translation`, når brugeren ønsker, at Co-op Translator skal opføre sig som `translate` CLI.

Repository-oversættelse standardiserer til `dry_run=true`, så en agent kan inspicere omfanget før filændringer:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

For at tillade skrivning skal kaldende part sætte både `dry_run=false` og `confirm_write=true`:

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

### Review Translated Output

Brug `run_review` til deterministiske checks, der ikke kræver LLM- eller Vision-legitimationsoplysninger:

!!! note "Beta"
    MCP eksponerer den beta `run_review` API. Den er sikker til read-only review-workflows, men review-checks og issue-skemaer kan udvikle sig.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Resultatet inkluderer fanget tekstoutput og et struktureret review-resumé, når det er tilgængeligt.

## Manual Server Runs

Manuelle køringer er primært til debugging eller til transports, der opfører sig som langkørende servere.

Debug den standard stdio-server:

```bash
co-op-translator-mcp
```

Kør fra en source checkout:

```bash
python -m co_op_translator.mcp.server
```

Kør en langlevende HTTP- eller SSE-server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

For lokale editor- og agent-integrationer, foretræk den klient-styrede `stdio`-konfiguration i Step 2.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Translate Markdown cells in notebook JSON. | No |
| `translate_image_content` | Translate text in one image and return base64 image data. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | Prepare Markdown chunks for the host agent to translate without Co-op Translator LLM credentials. | No |
| `finish_markdown_agent_translation` | Reconstruct Markdown from host-agent translated chunks. | No |
| `start_notebook_agent_translation` | Prepare notebook Markdown-cell chunks for the host agent to translate. | No |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON from host-agent translated chunks. | No |
| `rewrite_markdown_paths` | Rewrite Markdown body and frontmatter paths for a translated target. | No |
| `rewrite_notebook_paths` | Rewrite paths inside notebook Markdown cells. | No |
| `run_translation` | Run project-level translation like the CLI. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Run deterministic review checks. | No |
| `get_configuration_status` | Report configured LLM and Vision providers without exposing secrets. | No |
| `list_supported_languages` | List supported target language codes. | No |
| `get_api_overview` | Describe available MCP workflows and tools. | No |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## Copy-Paste Examples

Translate Markdown content:

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

Rewrite translated Markdown links:

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

Translate Markdown with the host agent model:

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

After the host agent translates each returned chunk, finish the job with the complete `job` object returned by `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Preview repository translation:

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

## Troubleshooting

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Safety Notes

- MCP tool calls are model-controlled by the host application, so repository translation is dry-run by default.
- Full repository translation can create, update, or remove many files. Require explicit user approval before setting `confirm_write=true`.
- The configuration status tool never returns API keys, endpoints, or other secret values.
- Image translation returns base64 image data. Large images can produce large tool responses.
- Agent-assisted tools return source chunks and prompts to the MCP host. Use them only with content the user is comfortable sending to that host agent model.