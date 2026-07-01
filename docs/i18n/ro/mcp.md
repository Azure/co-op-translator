# Server MCP

Co-op Translator include un server Model Context Protocol pentru agenți, editoare și clienți compatibili MCP.

Pentru configurația locală implicită, utilizatorii nu rulează un server separat manual. Ei își configurează clientul MCP, iar clientul pornește `co-op-translator-mcp` automat peste `stdio` atunci când are nevoie de instrumentele Co-op Translator.

Dacă decideți între CLI, API Python și MCP, începeți cu [Alegeți-vă fluxul de lucru](workflows.md).

Folosiți MCP când un agent sau editor ar trebui să apeleze Co-op Translator direct:

| Scopul utilizatorului | Instrumente MCP |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Serverul MCP înfășoară aceeași API Python publică documentată în [Python API](api.md). Instrumentele care folosesc furnizori utilizează aceiași furnizori configurați ca și CLI și API-ul Python. Instrumentele asistate de agent pregătesc fragmente pentru agentul gazdă MCP pentru a le traduce, apoi folosesc Co-op Translator pentru a reconstrui Markdown-ul sau notebook-ul final.

## Pasul 1: Instalați și configurați Co-op Translator

Instalați Co-op Translator în mediul Python pe care îl va folosi clientul MCP:

```bash
pip install co-op-translator
```

Pentru dezvoltare locală din acest depozit, instalați pachetul în modul editabil:

```bash
pip install -e .
```

Alegeți modul de traducere pe care îl va folosi clientul MCP:

| Mod | Folosiți pentru | Credenciale |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation require Azure OpenAI or OpenAI. Image translation also requires Azure AI Vision. |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | No Co-op Translator LLM provider credentials are required for Markdown or notebook chunks. Image translation is not covered by agent-assisted mode yet. |

Dacă începeți cu traducerea Markdown sau a notebook-urilor în interiorul unui agent precum Codex sau Claude Code, începeți cu modul agent-assisted. Folosiți provider-backed atunci când doriți ca Co-op Translator să apeleze el însuși furnizorii configurați, când traduceți imagini sau când rulați traducerea la nivel de depozit ca CLI.

Configurați credențialele furnizorilor doar pentru fluxurile de lucru provider-backed:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Traducerea imaginilor susținută de furnizor necesită în plus:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## Pasul 2: Configurați clientul MCP

Pentru configurația normală locală `stdio`, adăugați Co-op Translator la configurația clientului MCP. Clientul va porni și opri procesul automat.

Configurare pentru pachet instalat:

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

Configurare din sursă pe Windows:

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

Configurare din sursă pe macOS sau Linux:

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

După ce schimbați configurația clientului MCP, reporniți sau reîncărcați clientul astfel încât să poată descoperi noul server.

## Pasul 3: Verificați serverul în client

Rugați clientul MCP să listeze instrumentele disponibile sau apelați mai întâi unul dintre ajutoarele doar-în-citire:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Verificări utile inițiale:

| Instrument | Ce să verificați |
| --- | --- |
| `get_api_overview` | Confirmă că serverul este accesibil și arată fluxurile de lucru disponibile. |
| `list_supported_languages` | Confirmă că datele de limbă incluse pot fi încărcate. |
| `get_configuration_status` | Confirmă disponibilitatea furnizorilor LLM și Vision fără a expune valori secrete. |

## Pasul 4: Alegeți un flux de lucru

### Traduceți fișiere sau documente individuale

Folosiți instrumentele de conținut provider-backed când clientul MCP are deja conținutul documentului sau calea imaginii și Co-op Translator ar trebui să apeleze furnizorii de traducere configurați.

Pentru Markdown:

1. Apelați `translate_markdown_content` cu `document`, `language_code` și opțional `source_path`.
2. Dacă rezultatul tradus va fi scris într-un layout de ieșire Co-op Translator, apelați `rewrite_markdown_paths`.
3. Lăsați clientul să scrie sau să returneze `content` final.

Pentru notebook-uri:

1. Apelați `translate_notebook_content` cu JSON-ul notebook-ului și `language_code`.
2. Apelați `rewrite_notebook_paths` dacă linkurile din notebook tradus trebuie ajustate pentru o cale țintă.
3. Scrieți sau returnați JSON-ul notebook-ului final.

Pentru imagini:

1. Apelați `translate_image_content` cu `image_path`, `language_code` și opțional `root_dir` sau `fast_mode`.
2. Citiți `data_base64` și `mime_type` returnate.
3. Dacă este furnizat `output_path`, imaginea tradusă este de asemenea salvată la acea cale.

Instrumentele de conținut nu efectuează descoperire a proiectului, actualizări de metadate, declinări sau rescriere automată a căilor. Dacă doriți ca agentul gazdă să traducă fragmente Markdown sau notebook fără credențiale LLM ale Co-op Translator, folosiți fluxul de lucru agent-assisted de mai jos.

### Traduceți cu modelul agentului gazdă

Folosiți instrumentele agent-assisted când doriți ca agentul gazdă MCP, precum un asistent de codare, să producă textul tradus în loc să configurați Azure OpenAI sau OpenAI pentru Co-op Translator.

Într-un client MCP bazat pe chat, de obicei nu trebuie să scrieți JSON de instrument manual. Rugați agentul să folosească fluxul de lucru agent-assisted:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Pentru notebook-uri, folosiți același tipar:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Dacă clientul MCP acceptă server prompts, folosiți `agent_assisted_markdown_translation_prompt` pentru ca clientul să încarce aceleași instrucțiuni de flux de lucru.

Pentru Markdown:

1. Apelați `start_markdown_agent_translation` cu `document`, `language_code` și opțional `source_path`.
2. Traduceți fiecare fragment returnat în agentul gazdă urmând `prompt`-ul fragmentului.
3. Apelați `finish_markdown_agent_translation` cu `job` original și fragmentele traduse folosind `chunk_id` și `translated_text`.
4. Dacă conținutul va fi scris într-o cale țintă tradusă, apelați `rewrite_markdown_paths`.

Pentru notebook-uri:

1. Apelați `start_notebook_agent_translation` cu JSON-ul notebook-ului și `language_code`.
2. Traduceți fiecare fragment returnat în agentul gazdă.
3. Apelați `finish_notebook_agent_translation` cu `job` original și fragmentele traduse.
4. Apelați `rewrite_notebook_paths` dacă linkurile din notebook tradus trebuie ajustate pentru calea țintă.

Instrumentele agent-assisted nu apelează Azure OpenAI sau OpenAI din Co-op Translator. Agentul gazdă este responsabil pentru traducerea fragmentelor returnate. Co-op Translator se ocupă de împărțirea în fragmente Markdown, păstrarea placeholder-urilor, reconstrucția frontmatter, înlocuirea celulelor din notebook și normalizarea post-traducere.

### Traduceți un întreg depozit

Folosiți `run_translation` când utilizatorul vrea ca Co-op Translator să se comporte ca CLI-ul `translate`.

Traducerea depozitului are implicit `dry_run=true` astfel încât un agent să poată inspecta domeniul înainte de modificările fișierelor:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Pentru a permite scrierea, apelantul trebuie să seteze atât `dry_run=false`, cât și `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` este expus ca alias de compatibilitate pentru `run_translation`.

### Revizuiți rezultatul tradus

Folosiți `run_review` pentru verificări deterministe care nu necesită credențiale LLM sau Vision:

!!! note "Beta"
    MCP exposes the beta `run_review` API. It is safe for read-only review workflows, but review checks and issue schemas may evolve.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Rezultatul include text capturat și un rezumat structurat al reviziei când este disponibil.

## Rulări manuale ale serverului

Rulările manuale sunt utilizate în principal pentru depanare sau pentru transporturi care se comportă ca servere long-running.

Depanați serverul stdio implicit:

```bash
co-op-translator-mcp
```

Rulați dintr-un checkout sursă:

```bash
python -m co_op_translator.mcp.server
```

Rulați un server HTTP sau SSE de lungă durată:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Pentru integrările locale cu editorul și agentul, preferați configurația `stdio` gestionată de client din Pasul 2.

## Instrumente

| Instrument | Scop | Scrie fișiere |
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

## Resurse

| Resource URI | Scop |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## Prompts

| Prompt | Scop |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## Exemple copy-paste

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

## Depanare

| Problemă | Ce să încercați |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Note de securitate

- MCP tool calls are model-controlled by the host application, so repository translation is dry-run by default.
- Full repository translation can create, update, or remove many files. Require explicit user approval before setting `confirm_write=true`.
- The configuration status tool never returns API keys, endpoints, or other secret values.
- Image translation returns base64 image data. Large images can produce large tool responses.
- Agent-assisted tools return source chunks and prompts to the MCP host. Use them only with content the user is comfortable sending to that host agent model.