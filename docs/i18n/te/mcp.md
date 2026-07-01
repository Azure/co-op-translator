# MCP సర్వర్

Co-op Translator ఏజెంట్లు, ఎడిటర్లు, మరియు MCP-అనుకూల క్లయింట్ల కోసం Model Context Protocol సర్వర్‌ను అందిస్తుంది.

ప్రామాణిక లోకల్ సెటప్ కోసం, వినియోగదారులు విడిగా సర్వర్‌ను చేతితో నడపరు. వారు తమ MCP క్లయింట్‌ను కాన్ఫిగర్ చేస్తారు, మరియు అవసరమైతే క్లయింట్ `co-op-translator-mcp` ను `stdio` ద్వారా ఆటోమాటిక్‌గా ప్రారంభిస్తుంది.

మీరు CLI, Python API, మరియు MCP మధ్య ఎంచుకుంటున్నట్లయితే, [మీ వర్క్‌ఫ్లోను ఎంచుకోండి](workflows.md) తో ప్రారంభించండి.

Use MCP when an agent or editor should call Co-op Translator directly:

| వినియోగదారు లక్ష్యం | MCP టూల్స్ |
| --- | --- |
| ఒక Markdown డాక్యుమెంట్, నోట్‌బుక్ లేదా చిత్రం అనువదించండి | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| హోస్ట్ ఏజెంట్ మోడల్‌తో Markdown లేదా నోట్‌బుక్ కంటెంట్‌ను అనువదించండి | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| అవుట్‌పుట్ పాత్‌ను ఎంచుకున్న తర్వాత అనువదించిన Markdown లేదా నోట్‌బుక్ లింక్‌లను తిరిగి రాయండి | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI లాంటి పూర్తి రిపోజిటరీని అనువదించండి | `run_translation`, `translate_project` |
| LLM క్రెడెన్షియల్స్ లేకుండా అనువదించిన అవుట్‌పుట్‌ను సమీక్షించండి | `run_review` |
| సామర్థ్యాలు మరియు పరిసర స్థితిని పరిశీలించండి | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP సర్వర్ [Python API](api.md)లో డాక్యుమెంట్ చేయబడిన అదే పబ్లిక్ Python APIని ర్యాప్ చేస్తుంది. ప్రొవైడర్-బ్యాక్ చేయబడిన టూల్స్ CLI మరియు Python APIతోనే కాన్ఫిగర్ చేసిన ప్రొవైడర్లు ఉపయోగిస్తాయి. ఏజెంట్-అసిస్టెడ్ టూల్స్ MCP హోస్ట్ ఏజెంట్ అనువదించడానికి chunks ను సిద్ధం చేస్తాయి, తరువాత Co-op Translator ను ఉపయోగించి తుది Markdown లేదా నోట్‌బుక్‌ను పునర్నిర్మిస్తాయి.

## Step 1: Install and Configure Co-op Translator

Install Co-op Translator in the Python environment your MCP client will use:

```bash
pip install co-op-translator
```

For local development from this repository, install the package in editable mode:

```bash
pip install -e .
```

Choose the translation mode your MCP client will use:

| మోడ్ | దానికి ఉపయోగించండి | అధికారపత్రాలు |
| --- | --- | --- |
| ప్రొవైడర్ ఆధారిత | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, లేదా `run_translation` ను కాల్ చేస్తుంది. | Markdown మరియు నోట్‌బుక్ అనువాదానికి Azure OpenAI లేదా OpenAI అవసరం. ఇమేజ్ అనువాదానికి Azure AI Vision కూడా అవసరం. |
| ఏజెంట్-అసిస్టెడ్ | MCP హోస్ట్ ఏజెంట్ `start_markdown_agent_translation` లేదా `start_notebook_agent_translation` ద్వారా తిరిగిచ్చిన chunks ను అనువదిస్తుంది. | Markdown లేదా నోಟ್‌బుక్ chunks కోసం Co-op Translator LLM ప్రొవైడర్ క్రెడెన్షియల్స్ అవసరం కాదు. ఇమేజ్ అనువాదం ఇంకా ఏజెంట్-అసిస్టెడ్ మోడ్ ద్వారా కవరుచేయబడలేదు. |

If you are starting with Markdown or notebook translation inside an agent such as Codex or Claude Code, start with agent-assisted mode. Use provider-backed mode when you want Co-op Translator itself to call your configured providers, when you are translating images, or when you are running repository-level translation like the CLI.

Configure provider credentials only for provider-backed workflows:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed image translation additionally needs:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    ఏజెంట్-అసిస్టెడ్ మోడ్ ప్రస్తుతం Markdown మరియు నోట్‌బుక్ Markdown సెల్స్‌ను కవర్ చేస్తుంది. ఇమేజ్ అనువాదం ఇంకా ప్రొవైడర్-ఆధారిత ఇమేజ్ పైప్లైన్‌ను ఉపయోగిస్తుంది మరియు OCR మరియు లేఅవుట్-అవగాహన రెండరింగ్ కోసం Azure AI Vision అవసరం.

## Step 2: Configure Your MCP Client

For the normal local `stdio` setup, add Co-op Translator to your MCP client configuration. The client will start and stop the process automatically.

Installed package configuration:

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

Source checkout configuration on Windows:

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

Source checkout configuration on macOS or Linux:

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

After changing MCP client configuration, restart or reload the client so it can discover the new server.

## Step 3: Verify the Server in the Client

Ask the MCP client to list available tools, or call one of the read-only helpers first:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Useful first checks:

| టూల్ | పరీక్షించవలసినది |
| --- | --- |
| `get_api_overview` | సర్వర్ చేరుకోవచ్చని నిర్ధారిస్తుంది మరియు లభ్యమైన వర్క్‌ఫ్లోలను చూపిస్తుంది. |
| `list_supported_languages` | ప్యాకేజ్డ్ చేసిన భాషా డేటా లోడ్ చేయగలదని నిర్ధారిస్తుంది. |
| `get_configuration_status` | రహస్య విలువలను బయట పెట్టకుండా LLM మరియు Vision ప్రొవైడర్ అందుబాటును నిర్ధారిస్తుంది. |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

Use provider-backed content tools when the MCP client already has document content or an image path and Co-op Translator should call the configured translation providers.

For Markdown:

1. `document`, `language_code`, మరియు ఐచ్చికంగా `source_path` తో `translate_markdown_content` ను కాల్ చేయండి.
2. అనువదించిన ఫలితాన్ని Co-op Translator అవుట్‌పుట్ లేఅవుట్‌లో రాయాల్సినట్లయితే, `rewrite_markdown_paths` ను కాల్ చేయండి.
3. క్లయింట్ తుది `content` ను రాయగలిగేలా లేదా రిటర్న్ చేయగలిగేలా చేయండి.

For notebooks:

1. నోట్‌బుక్ JSON మరియు `language_code` తో `translate_notebook_content` ను కాల్ చేయండి.
2. అనువదించిన నోట్‌బుక్ లింక్‌లు లక్ష్య పాత్‌కు సర్దుబాటు చేయాల్సిన అవసరం ఉంటే `rewrite_notebook_paths` ను కాల్ చేయండి.
3. తుది నోట్‌బుక్ JSON ను రాయండి లేదా రిటర్న్ చేయండి.

For images:

1. `image_path`, `language_code`, మరియు ఐచ్చికంగా `root_dir` లేదా `fast_mode` తో `translate_image_content` ను కాల్ చేయండి.
2. తిరిగి వచ్చిన `data_base64` మరియు `mime_type` ను చదవండి.
3. `output_path` ఇవ్వబడితే, అనువదించిన చిత్రం కూడా ఆ పాత్‌కు సేవ్ చేయబడుతుంది.

The content tools do not perform project discovery, metadata updates, disclaimers, or automatic path rewriting. If you want the host agent to translate Markdown or notebook chunks without Co-op Translator LLM provider credentials, use the agent-assisted workflow below.

### Translate with the Host Agent Model

Use agent-assisted tools when you want the MCP host agent, such as a coding assistant, to produce the translated text instead of configuring Azure OpenAI or OpenAI for Co-op Translator.

In a chat-based MCP client, you normally do not need to write tool JSON yourself. Ask the agent to use the agent-assisted workflow:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

For notebooks, use the same pattern:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

If your MCP client supports server prompts, use `agent_assisted_markdown_translation_prompt` to have the client load the same workflow instructions.

For Markdown:

1. `document`, `language_code`, మరియు ఐచ్చికంగా `source_path` తో `start_markdown_agent_translation` ను కాల్ చేయండి.
2. chunk `prompt` పాటిస్తూ హోస్ట్ ఏజెంట్‌లో ప్రతి తిరిగి ఇచ్చిన chunk ను అనువదించండి.
3. మౌలిక `job` మరియు `chunk_id` మరియు `translated_text` ఉపయోగించి అనువదించిన chunks తో `finish_markdown_agent_translation` ను కాల్ చేయండి.
4. కంటెంట్ అనువదించిన టార్గెట్ పాత్‌లో రాయబడాల్సినట్లయితే, `rewrite_markdown_paths` ను కాల్ చేయండి.

For notebooks:

1. నోట్‌బుక్ JSON మరియు `language_code` తో `start_notebook_agent_translation` ను కాల్ చేయండి.
2. హోస్ట్ ఏజెంట్‌లో ప్రతి తిరిగిచ్చిన chunk ను అనువదించండి.
3. మౌలిక `job` మరియు అనువదించిన chunks తో `finish_notebook_agent_translation` ను కాల్ చేయండి.
4. అనువదించిన నోట్‌బుక్ లింక్‌లకు లక్ష్య-పాత్ సర్దుబాటు అవసరమైతే `rewrite_notebook_paths` ను కాల్ చేయండి.

Agent-assisted tools do not call Azure OpenAI or OpenAI from Co-op Translator. The host agent is responsible for translating the returned chunks. Co-op Translator handles Markdown chunking, placeholder preservation, frontmatter reconstruction, notebook cell replacement, and post-translation normalization.

### Translate an Entire Repository

Use `run_translation` when the user wants Co-op Translator to behave like the `translate` CLI.

Repository translation defaults to `dry_run=true` so an agent can inspect scope before file changes:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

To allow writes, the caller must set both `dry_run=false` and `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` is exposed as a compatibility alias for `run_translation`.

### Review Translated Output

Use `run_review` for deterministic checks that do not require LLM or Vision credentials:

!!! note "Beta"
    MCP బీటా `run_review` APIని ఎక్స్‌పోజ్ చేస్తుంది. ఇది రీడ్-ఒన్లీ రివ్యూ వర్క్‌ఫ్లోలకు సురక్షితంగా ఉంటుంది, కానీ రివ్యూ పరీక్షలు మరియు ఇష్యూ స్కీమాలు అభివృద్ధి చెందవచ్చు.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

The result includes captured text output and a structured review summary when available.

## Manual Server Runs

Manual runs are mainly for debugging or for transports that behave like long-running servers.

Debug the default stdio server:

```bash
co-op-translator-mcp
```

Run from a source checkout:

```bash
python -m co_op_translator.mcp.server
```

Run a long-lived HTTP or SSE server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

For local editor and agent integrations, prefer the client-managed `stdio` configuration in Step 2.

## Tools

| టూల్ | ప్రయోజనం | ఫైళ్ళను రాస్తుందా |
| --- | --- | --- |
| `translate_markdown_content` | Markdown స్ట్రింగ్‌ను అనువదిస్తుంది. | లేదు |
| `translate_notebook_content` | నోట్‌బుక్ JSONలోని Markdown సెల్స్‌ను అనువదిస్తుంది. | లేదు |
| `translate_image_content` | ఒక చిత్రంలోని టెక్స్ట్‌ను అనువదించి base64 ఇమేజ్ డేటాను తిరిగి ఇస్తుంది. | ఐచ్చికం, కేవలం `output_path` ఇవ్వబడినప్పుడు మాత్రమే |
| `start_markdown_agent_translation` | Co-op Translator LLM క్రెడెన్షియల్స్ లేకుండా హోస్ట్ ఏజెంట్‌కు అనువదించేందుకు Markdown chunks ను సిద్ధం చేస్తుంది. | లేదు |
| `finish_markdown_agent_translation` | హోస్ట్-ఏజెంట్ అనువదించిన chunks నుండి Markdown ను పునర్నిర్మిస్తుంది. | లేదు |
| `start_notebook_agent_translation` | హోస్ట్ ఏజెంట్ అనువదించేందుకు నోట్‌బుక్ Markdown-సెల్ chunks ను సిద్ధం చేస్తుంది. | లేదు |
| `finish_notebook_agent_translation` | హోస్ట్-ఏజెంట్ అనువదించిన chunks నుండి నోట్‌బుక్ JSON ను పునర్నిర్మిస్తుంది. | లేదు |
| `rewrite_markdown_paths` | అనువదించిన టార్గెట్ కోసం Markdown బాడీ మరియు frontmatter పాత్‌లను రిరైటు చేస్తుంది. | లేదు |
| `rewrite_notebook_paths` | నోట్‌బుక్ Markdown సెల్స్‌లోని పాత్‌లను రిరైటు చేస్తుంది. | లేదు |
| `run_translation` | CLI లాంటి ప్రాజెక్ట్-స్థాయి అనువాదాన్ని నడిపిస్తుంది. | అవును, `dry_run=false` మరియు `confirm_write=true` ఉన్నప్పుడు |
| `translate_project` | `run_translation` కోసం కంపాటిబిలిటీ అలియాస్. | అవును, `dry_run=false` మరియు `confirm_write=true` ఉన్నప్పుడు |
| `run_review` | నిర్ణీత రివ్యూ పరీక్షలను నడిపిస్తుంది. | లేదు |
| `get_configuration_status` | రహస్యాలను బయట పెట్టకుండా కాన్ఫిగర్ చేయబడిన LLM మరియు Vision ప్రొవైడర్లను నివేదిస్తుంది. | లేదు |
| `list_supported_languages` | సమర్థించబడిన లక్ష్య భాష కోడ్‌ల జాబితా చేస్తుంది. | లేదు |
| `get_api_overview` | లభ్యమయ్యే MCP వర్క్‌ఫ్లోలు మరియు టూల్‌లను వివరించు. | లేదు |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | వర్క్‌ఫ్లోలు మరియు టూల్‌ల యొక్క JSON అవలోకనం. |
| `co-op://supported-languages` | సమర్థించబడిన భాష కోడ్‌ల యొక్క JSON జాబితా. |
| `co-op://configuration` | రహస్యాలను బయట పెట్టకుండానే ప్రొవైడర్ అందుబాటు సారాంశం (JSON). |

## Prompts

| ప్రాంప్ట్ | ప్రయోజనం |
| --- | --- |
| `translate_markdown_document_prompt` | కంటెంట్ అనువాదం మరియు ఐచ్చిక పాత్ రిరైటింగ్ ద్వారా MCP క్లయింట్‌ను మార్గనిర్దేశించండి. |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM ప్రొవైడర్ క్రెడెన్షియల్స్ లేకుండా హోస్ట్-ఏజెంట్ Markdown అనువాదానికి MCP క్లయింట్‌ను మార్గనిర్దేశించండి. |
| `translate_repository_prompt` | Dry-run-ముందుగా రిపోజిటరీ అనువాదం ద్వారా MCP క్లయింట్‌ను మార్గనిర్దేశించండి. |

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
| MCP క్లయింట్ `co-op-translator-mcp` ను కనుగొనలేకపోతుంది. | అబ్సొల్యూట్ Python ఎగ్జిక్యూటబుల్ పాత్ మరియు `["-m", "co_op_translator.mcp.server"]` సోర్స్ చెకౌట్ కాన్ఫిగరేషన్ ఉపయోగించండి. |
| సర్వర్ లిస్ట్ లో ఉంది కానీ అనువాదం విఫలమవుతోంది. | `get_configuration_status` ను కాల్ చేసి ఒక LLM ప్రొవైడర్ అందుబాటులో ఉందని నిర్ధారించండి. |
| Azure OpenAI/OpenAI కీలు లేకుండా Markdown లేదా నోట్‌బుక్ అనువాదం కావాలి. | హోస్ట్ ఏజెంట్ chunks ను అనువదించేందుకు `start_markdown_agent_translation` / `finish_markdown_agent_translation` లేదా నోట్‌బుక్ సమానమైన ఫంక్షన్లు ఉపయోగించండి. |
| ఇమేజ్ అనువాదం విఫలమవుతోంది. | Azure AI Vision కోసం వాతావరణ వేరియబుల్స్ సెట్ అయ్యాయా అని నిర్ధారించండి మరియు `get_configuration_status` ను కాల్ చేయండి. |
| రిపోజిటరీ అనువాదం ఫైళ్లను రచించడంలేదు. | స్పష్టమైన వినియోగదారు ఆమోదం వచ్చిన తరువాత మాత్రమే `dry_run=false` మరియు `confirm_write=true` ను సెట్ చేయండి. |
| క్లయింట్ కాన్ఫిగ్‌లో చేసిన మార్పులు కనిపించడంలేదు. | MCP క్లయింట్‌ను రీస్టార్ట్ లేదా రीलోడ్ చేయండి. |

## Safety Notes

- MCP టూల్ కాల్స్ హోస్ట్ అప్లికేషన్ ద్వారా మోడల్-నియంత్రించబడతాయి, కాబట్టి రిపోజిటరీ అనువాదం డిఫాల్ట్‌గా dry-run ఉంటుంది.
- పూర్తి రిపోజిటరీ అనువాదం అనేక ఫైళ్లను సృష్టించవచ్చు, నవీకరించవచ్చు లేదా తొలగించవచ్చు. `confirm_write=true` సెట్చేసేముందు స్పష్టమైన వినియోగదారు ఆమోదం కోరండి.
- కాన్ఫిగరేషన్ స్థితి టూల్ ఎప్పుడూ API కీలు, endpoints, లేదా ఇతర రహస్య విలువలను తిరిగి ఇవ్వదు.
- ఇమేజ్ అనువాదం base64 ఇమేజ్ డేటాను తిరిగి ఇస్తుంది. పెద్ద ఇమేజ్‌లు పెద్ద టూల్ రిస్పాన్సులను ఉత్పత్తి చేయవచ్చు.
- ఏజెంట్-అసిస్టెడ్ టూల్స్ మూల chunks మరియు ప్రాంప్ట్‌లను MCP హోస్ట్‌కు తిరిగి అందిస్తాయి. వాటిని ఆ హోస్ట్ ఏజెంట్ మోడల్‌కు పంపటానికి వినియోగదారు సౌకర్యంగా ఉన్న కంటెంట్‌తో మాత్రమే ఉపయోగించండి.