# MCP సర్వర్

Co-op Translator ఏజెంట్‌లు, ఎడిటర్లు, మరియు MCP-అనుకూల క్లయింట్ల కోసం ఒక Model Context Protocol సర్వర్‌ను కలిగి ఉంటుంది.

ఒక సాధారణ లోకల్ సెటప్‌లో, వినియోగదారులు వేర్వేరు సర్వర్‌ను చేతితో నడిపించవలసిన అవసరం ఉండదు. వారు వారి MCP క్లయింట్‌ని కాన్ఫిగర్ చేస్తారు, మరియు క్లయింట్ Co-op Translator టూల్స్ అవసరమైన సమయంలో `stdio` ద్వారా ఆటోమేటిగ్గా `co-op-translator-mcp` ప్రారంభిస్తుంది.

CLI, Python API, మరియు MCP మధ్య నిర్ణయం తీసుకుంటుంటే, [మీ వర్క్‌ఫ్లోను ఎంచుకోండి](workflows.md) తో మొదలు పెట్టండి.

ఏజెంట్ లేదా ఎడిటర్ Co-op Translator‌ను నేరుగా పిలవాల్సినప్పుడు MCP వాడండి:

| వినియోగదారు లక్ష్యం | MCP టూల్స్ |
| --- | --- |
| ఒక Markdown డాక్యుమెంట్, నోట్‌బుక్, లేదా చిత్రం ఒకటిని అనువదించండి | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| హోస్ట్ ఏజెంట్ మోడల్‌తో Markdown లేదా నోట్‌బుక్ కంటెంట్‌ను అనువదించండి | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| అవుట్‌పుట్ మార్గం ఎంచుకున్న తర్వాత అనువాదించిన Markdown లేదా నోట్‌బుక్ లింకులను రిరైట్ చేయండి | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI లాగా ఒక సంపూర్ణ రిపాజిటరీని అనువదించండి | `run_translation`, `translate_project` |
| LLM క్రెడెన్షియల్స్ లేకుండా అనువదించిన ఔట్‌పుట్‌ను సమీక్షించండి | `run_review` |
| సామర్థ్యాలు మరియు వాతావరణ స్థితిని పరిశీలించండి | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP సర్వర్ అదే పబ్లిక్ Python API ని ర్యాప్ చేస్తుంది, ఇది [Python API](api.md)లో డాక్యుమెంటెడ్. ప్రొవైడర్-బ్యాక్డ్ టూల్స్ CLI మరియు Python API వలెనే కాన్ఫిగర్ చేయబడిన ప్రొవైడర్స్‌ను ఉపయోగిస్తాయి. ఏజెంట్-అసిస్టెడ్ టూల్స్ MCP హోస్ట్ ఏజెంట్ కోసం ఛంక్స్‌ను సిద్ధం చేసి, తరువాత Co-op Translator ను ఉపయోగించి తుది Markdown లేదా నోట్‌బుక్‌ను పునర్నిర్మించగలవని జోడిస్తాయి.

## దశ 1: Co-op Translatorని ఇన్‌స్టాల్ చేసి కాన్ఫిగర్ చేయండి

మీ MCP క్లయింట్ ఉపయోగించే Python పరిసరంలో Co-op Translatorని ఇన్‌స్టాల్ చేయండి:

```bash
pip install co-op-translator
```

ఈ రిపాజిటరీ నుండి లోకల్ డెవలప్‌మెంట్ కోసం, ప్యాకేజీని editable మోడ్‌లో ఇన్‌స్టాల్ చేయండి:

```bash
pip install -e .
```

మీ MCP క్లయింట్ ఉపయోగించే అనువాద మోడ్‌ను ఎంచుకోండి:

| మోడ్ | ఇది ఉపయోగించండి | క్రెడెన్షియల్స్ |
| --- | --- | --- |
| ప్రొవైడర్-బ్యాక్డ్ | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, లేదా `run_translation` పిలుస్తుంది. | అనువాదానికి Azure OpenAI, OpenAI, లేదా Anthropic అవసరం. చిత్రం అనువాదానికి Azure AI Vision కూడా అవసరం. |
| ఏజెంట్-అసిస్టెడ్ | MCP హోస్ట్ ఏజెంట్ `start_markdown_agent_translation` లేదా `start_notebook_agent_translation` ద్వారా తిరిగి ఇచ్చే ఛంక్స్‌ను అనువదిస్తుంది. | Markdown లేదా నోట్‌బుక్ ఛంక్స్ కోసం Co-op Translator LLM ప్రొవైడర్ క్రెడెన్షియల్స్ అవసరం లేదు. చిత్రం అనువాదం ఇప్పటివరకు ఏజెంట్-అసిస్టెడ్ మోడ్ ద్వారా కవర్ కాదు. |

మీరు Codex లేదా Claude Code వంటి ఏజెంట్‌లో Markdown లేదా నోట్‌బుక్ అనువాదంతో ప్రారంభిస్తుంటే, ఏజెంట్-అసిస్టెడ్ మోడ్‌తో మొదలు పెడండి. ప్రొవైడర్-బ్యాక్డ్ మోడ్‌ను ఉపయోగించండి ఎప్పుడు మీరు Co-op Translator స్వయంగా మీ కాన్ఫిగర్ చేసిన ప్రొవైడర్స్‌ను పిలవాలని కోరుకుంటే, చిత్రాలను అనువదిస్తున్నప్పుడు, లేదా CLI లాంటి రిపాజిటరీ-స్థాయి అనువాదం నడుపుతున్నప్పుడు.

ప్రొవైడర్-బ్యాక్డ్ వర్క్‌ఫ్లోల కోసం ఒక ప్రొవైడర్‌ను కాన్ఫిగర్ చేయండి:

```bash
# ఆజ్యూర్ ఓపెన్‌ఏఐ
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# లేదా ఓపెన్‌ఏఐ
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# లేదా ఆంథ్రోపిక్
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

ప్రొవైడర్-బ్యాక్డ్ చిత్రం అనువాదం అదనంగా అవసరం:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    ఏజెంట్-అసిస్టెడ్ మోడ్ ప్రస్తుతం Markdown మరియు నోట్‌బుక్ Markdown సెల్స్‌ను మాత్రమే కవర్ చేస్తుంది. చిత్రం అనువాదం ఇంకా ప్రొవైడర్-బ్యాక్డ్ ఇమేజ్ పైప్లైన్‌ను ఉపయోగిస్తుంది మరియు OCR మరియు లేఅవుట్-అవగాహన రేందరింగ్ కోసం Azure AI Vision అవసరమే.

## దశ 2: మీ MCP క్లయింట్‌ను కాన్ఫిగర్ చేయండి

సాధారణ లోకల్ `stdio` సెటప్ కోసం, Co-op Translatorని మీ MCP క్లయింట్ కాన్ఫిగరేషన్‌లో జోడించండి. క్లయింట్ ప్రాసెస్‌ను ఆటోమేటిగ్గా ప్రారంభించి ఆపుతుంది.

ఇన్స్టాల్ చేసిన ప్యాకేజీ కాన్ఫిగరేషన్:

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

Windowsలో సోర్స్ చెకౌట్ కాన్ఫిగరేషన్:

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

macOS లేదా Linuxలో సోర్స్ చెకౌట్ కాన్ఫిగరేషన్:

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

MCP క్లయింట్ కాన్ఫిగరేషన్ మార్చిన తర్వాత, క్లయింట్ కొత్త సర్వర్‌ను కనుగొనేటట్లుగా రీస్టార్ట్ లేదా రిలోడ్ చేయండి.

## దశ 3: క్లయింట్‌లో సర్వర్‌ను ధృవీకరించండి

అందుబాటులో ఉన్న టూల్స్‌ను జాబితా చేయడానికి MCP క్లయింట్‌ను అడగండి, లేదా ముందుగా రీడ్ఓన్లీ హెల్పర్స్‌లో ఒకటిని పిలవండి:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

ప్రారంభిక ఉపయోగకరమైన తనిఖీలు:

| టూల్ | ఏమి తనిఖీ చేయాలి |
| --- | --- |
| `get_api_overview` | సర్వర్ చేరుకోవచ్చునని నిర్ధారిస్తుంది మరియు అందుబాటులో ఉన్న వర్క్‌ఫ్లోలను చూపిస్తుంది. |
| `list_supported_languages` | ప్యాకేజ్డ్ భాషా డేటా లోడ్ చేయబడగలదని నిర్ధారిస్తుంది. |
| `get_configuration_status` | రహస్య విలువలను బయటపెట్టకుండా LLM మరియు Vision ప్రొవైడర్‌ల అందుబాటును నిర్ధారిస్తుంది. |

## దశ 4: ఒక వర్క్‌ఫ్లోని ఎంచుకోండి

### వ్యక్తిగత ఫైళ్లు లేదా డాక్యుమెంట్లను అనువదించండి

MCP క్లయింట్‌కు ఇప్పటికే డాక్యుమెంట్ కంటెంట్ లేదా ఇమేజ్ పాత్ ఉన్నప్పుడు మరియు Co-op Translator కాన్ఫిగర్ చేసిన అనువాద ప్రొవైడర్లను పిలవాలనుకుంటే ప్రొవైడర్-బ్యాక్డ్ కంటెంట్ టూల్స్‌ను ఉపయోగించండి.

Markdown కోసం:

1. `document`, `language_code` మరియు ఐచ్చికంగా `source_path` తో `translate_markdown_content` పిలవండి.
2. అనువదించిన ఫలితం Co-op Translator అవుట్‌పుట్ లేఅవుట్‌లో రాయబడనున్నట్లయితే, `rewrite_markdown_paths` పిలవండి.
3. క్లయింట్ తుది `content` ను రాయాలి లేదా తిరిగి ఇవ్వాలి.

నోట్‌బుక్‌ల కోసం:

1. నోట్‌బుక్ JSON మరియు `language_code` తో `translate_notebook_content` పిలవండి.
2. అనువదించిన నోట్‌బుక్ లింకులను లక్ష్య మార్గానికి సర్దుబాటు చేయాలి అంటే `rewrite_notebook_paths` పిలవండి.
3. తుది నోట్‌బుక్ JSON ను రాయండి లేదా తిరిగి ఇవ్వండి.

చిత్రాల కోసం:

1. `image_path`, `language_code`, మరియు ఐచ్చికంగా `root_dir` లేదా `fast_mode` తో `translate_image_content` పిలవండి.
2. తిరిగి వచ్చిన `data_base64` మరియు `mime_type` ను చదవండి.
3. `output_path` అందించబడితే, అనువదించిన చిత్రం కూడా ఆ మార్గంలో సేవ్ చేయబడుతుంది.

కంటెంట్ టూల్స్ ప్రాజెక్ట్ డిస్కవరీ, మెటాడేటా అప్డేట్లు, డిస్క్లైమర్లు లేదా ఆటోమేటిక్ పాత్ రిరైటింగ్ చేయవు. మీరు Co-op Translator LLM ప్రొవైడర్ క్రెడెన్షియల్స్ లేకుండా హోస్ట్ ఏజెంట్ ద్వారా Markdown లేదా నోట్‌బుక్ ఛంక్స్ అనువదించించాలని ఉంటే, క్రింద ఉన్న ఏజెంట్-అసిస్టెడ్ వర్క్‌ఫ్లోను ఉపయోగించండి.

### హోస్ట్ ఏజెంట్ మోడల్‌తో అనువదించండి

Co-op Translator కోసం LLM ప్రొవైడర్‌ను కాన్ఫిగర్ చేయకుండానే MCP హోస్ట్ ఏజెంట్ (ఉదాహరణకు కోడింగ్ అసిస్టెంట్) అనువదించిన టెక్స్ట్‌ను ఉత్పత్తి చేయాల్సినప్పుడు agent-assisted టూల్స్‌ను ఉపయోగించండి.

చాట్-ఆధారిత MCP క్లయింట్‌లో, సాధారణంగా మీరు టూల్ JSON ని స్వయంగా రాయవలసిన అవసరం లేదు. ఏజెంట్‌ని agent-assisted వర్క్‌ఫలో ఉపయోగించాలని అడగండి:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

నోట్‌బుక్స్ కోసం, అదే విధానాన్ని ఉపయోగించండి:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

మీ MCP క్లయింట్ సర్వర్ ప్రాంప్ట్స్‌ని మద్దతిస్తే, క్లయింట్ అదే వర్క్‌ఫ్లో సూచనలను లోడ్ చేయడానికి `agent_assisted_markdown_translation_prompt` ఉపయోగించండి.

Markdown కోసం:

1. `document`, `language_code` మరియు ఐచ్చికంగా `source_path` తో `start_markdown_agent_translation` పిలవండి.
2. ప్రతి తిరిగి వచ్చిన ఛంక్‌కు ఉన్న `prompt` ని అనుసరించి వాటిని హోస్ట్ ఏజెంట్‌లో అనువదించండి.
3. ఒరిజినల్ `job` మరియు అనువదించిన ఛంక్స్‌ను `chunk_id` మరియు `translated_text` ఉపయోగించి `finish_markdown_agent_translation` పిలవండి.
4. కంటెంట్ అనువదించిన లక్ష్య మార్గంలో రాయబడాల్సినట్లయితే, `rewrite_markdown_paths` పిలవండి.

నోట్‌బుక్స్ కోసం:

1. నోట్‌బుక్ JSON మరియు `language_code` తో `start_notebook_agent_translation` పిలవండి.
2. తిరిగి వచ్చిన ప్రతి ఛంక్‌ని హోస్ట్ ఏజెంట్‌లో అనువదించండి.
3. ఒరిజినల్ `job` మరియు అనువదించిన ఛంక్స్‌తో `finish_notebook_agent_translation` పిలవండి.
4. అనువదించిన నోట్‌బుక్ లింకులు లక్ష్య మార్గానికి సర్దుబాటు అవసరం ఉంటే `rewrite_notebook_paths` పిలవండి.

Agent-assisted టూల్స్ Co-op Translator నుండి కాన్ఫిగర్ చేసిన LLM ప్రొవైడర్‌ను పిలవవు. తిరిగి ఇచ్చిన ఛంక్స్‌ను అనువదించడం హోస్ట్ ఏజెంట్ బాధ్యత. Co-op Translator Markdown ఛంకింగ్, ప్లేస్‌హోల్డర్ సంరక్షణ, frontmatter పునర్నిర్మాణం, నోట్‌బుక్ సెల్ స్థానం మార్చడం, మరియు అనువాద అనంతరం సాధారణీకరణను నిర్వహిస్తుంది.

### ఒక సంపూర్ణ రిపాజిటరీని అనువదించండి

వినియోగదారు Co-op Translator ను `translate` CLI లాగా ప్రవర్తింపచేయాలనుకుంటే `run_translation` ను ఉపయోగించండి.

రిపాజిటరీ అనువాదం డిఫాల్ట్‌గా `dry_run=true` అవుతుంది, తద్వారా ఏజెంట్ ఫైల్ మార్పులు చేయక ముందు స్కోప్‌ను పరిశీలించగలదు:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

`run_translation` ఫలితం వెర్షన్ చేయబడ్డ `events` అర్రేను కలిగి ఉంటుంది
`co-op.translation.event.v1` ప్రోగ్రెస్ ఈవెంట్స్. MCP క్లయింట్లు క్రింది ఫీల్డ్‌లను ఉపయోగించాలి
`type`, `stage_key`, `completed`, `total`, మరియు `current_path` వంటి ఫీల్డ్‌లు,
consoleలో క్యాప్చర్ చేసిన టెక్స్ట్‌ను పార్స్ చేయడం బదులు. `json_events_path` ఇవ్వడం ద్వారా ఆ ఈవెంట్స్‌ను
NDJSON ఫైల్‌లో కూడా రాయవచ్చు.

రాయడాలంటే, కాలర్ రెండింటిని సెట్ చేయాలి: `dry_run=false` మరియు `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` ను `run_translation` కి కంపాటిబిలిటీ అలియాస్‌గా అందజేస్తుంది.

### అనువదించిన ఔట్‌పుట్‌ను సమీక్షించండి

LLM లేదా Vision క్రెడెన్షియల్స్ అవసరం లేని నిర్ధారిత తనిఖీలు కోసం `run_review` ను ఉపయోగించండి:

!!! note "Beta"
    MCP బేటా `run_review` APIని ఎక్స్‌పోజ్ చేస్తుంది. ఇది రీడ్ఓన్లీ రివ్యూ వర్క్‌ఫ్లోలకు సురక్షితంగా ఉంటుంది, కానీ రివ్యూ చెక్స్ మరియు ఇష్యూ స్కీమాలు మారవచ్చు.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

ఫలితం క్యాప్చర్ చేసిన టెక్స్ట్ ఔట్‌పుట్ మరియు అందుబాటులో ఉన్నప్పుడు ఒక నిర్మిత రివ్యూ సంగ్రహాన్ని కలిగి ఉంటుంది.

## మాన్యువల్ సర్వర్ రన్స్

మాన్యువల్ రన్స్ ప్రధానంగా డిబగ్ కోసం లేదా దీర్ఘకాలం నడిచే సర్వర్ల్లా వ్యవహరించే ట్రాన్స్‌పోర్ట్స్ కోసం ఉంటాయి.

డిఫాల్ట్ stdio సర్వర్‌ను డిబగ్ చేయండి:

```bash
co-op-translator-mcp
```

సోర్స్ చెకౌట్ నుండి నడపండి:

```bash
python -m co_op_translator.mcp.server
```

దీర్ఘకాలిక HTTP లేదా SSE సర్వర్ నడిపించండి:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

లోకల్ ఎడిటర్ మరియు ఏజెంట్ ఇన­teగ్రేషన్స్ కోసం, దశ 2లోని క్లయింట్-మేనేజ్డ్ `stdio` కాన్ఫిగరేషన్‌ను ఇష్టపరచండి.

## టూల్స్

| టూల్ | ఉద్దేశ్యం | ఫైళ్ళను రాస్తుందా |
| --- | --- | --- |
| `translate_markdown_content` | ఒక Markdown స్ట్రింగ్‌ను అనువదించు. | కాదు |
| `translate_notebook_content` | నోట్‌బుక్ JSONలోని Markdown సెల్స్‌ను అనువదించు. | కాదు |
| `translate_image_content` | ఒక చిత్రంలో ఉన్న టెక్స్ట్‌ను అనువదించి base64 ఇమేజ్ డేటాను తిరిగి ఇస్తుంది. | ఐచ్చికం, ఫలితంగా `output_path` ఇచ్చినపుడు మాత్రమే |
| `start_markdown_agent_translation` | Co-op Translator LLM క్రెడెన్షియల్స్ లేకుండానే హోస్ట్ ఏజెంట్ అనువదించగలిగేలా Markdown ఛంక్స్‌ను సిద్ధం చేయండి. | కాదు |
| `finish_markdown_agent_translation` | హోస్ట్-ఏజెంట్ అనువదించిన ఛంక్స్ నుండి Markdown ను పునర్నిర్మించు. | కాదు |
| `start_notebook_agent_translation` | హోస్ట్ ఏజెంట్ అనువదించగలిగేలా నోట్‌బుక్ Markdown-సెల్ ఛంక్స్‌ను సిద్ధం చేయండి. | కాదు |
| `finish_notebook_agent_translation` | హోస్ట్-ఏజెంట్ అనువదించిన ఛంక్స్ నుండి నోట్‌బుక్ JSONను పునర్నిర్మించండి. | కాదు |
| `rewrite_markdown_paths` | అనువదించిన లక్ష్యానికి అనుగుణంగా Markdown బాడీ మరియు frontmatter మార్గాలను రిరైటు చేయండి. | కాదు |
| `rewrite_notebook_paths` | నోట్‌బుక్ Markdown సెల్స్ లోని మార్గాలను రిరైటు చేయండి. | కాదు |
| `run_translation` | CLI లాగా ప్రాజెక్ట్-స్థాయి అనువాదాన్ని నడపండి. | అవును, `dry_run=false` మరియు `confirm_write=true` అయినప్పుడు |
| `translate_project` | `run_translation` కు కంపాటిబిలిటీ అలియాస్. | అవును, `dry_run=false` మరియు `confirm_write=true` అయినప్పుడు |
| `run_review` | నిర్ధారిత రివ్యూ తనిఖీలను నడపండి. | కాదు |
| `get_configuration_status` | రహస్యాలు బయటపెట్టకుండా కాన్ఫిగర్ చేసిన LLM మరియు Vision ప్రొవైడర్లను నివేదించండి. | కాదు |
| `list_supported_languages` | మద్దతు పొందిన లక్ష్య భాషా కోడ్‌లను జాబితా చేయండి. | కాదు |
| `get_api_overview` | అందుబాటులో ఉన్న MCP వర్క్‌ఫ్లోలు మరియు టూల్స్‌ను వివరిచండి. | కాదు |

## వనరులు

| వనరు URI | ఉద్దేశ్యం |
| --- | --- |
| `co-op://api` | వర్క్‌ఫ్లోలు మరియు టూల్స్ యొక్క JSON అవలోకనం. |
| `co-op://supported-languages` | మద్దతు పొందిన భాషా కోడ్‌ల JSON జాబితా. |
| `co-op://configuration` | రహస్యాల raza లేకుండా ప్రొవైడర్ అందుబాటు సంగ్రహం JSON. |

## ప్రాంప్ట్స్

| ప్రాంప్ట్ | ఉద్దేశ్యం |
| --- | --- |
| `translate_markdown_document_prompt` | కంటెంట్ అనువాదం మరియు ఐచ్చిక పాత్ రిరైటింగ్ ద్వారా MCP క్లయింట్‌ను మార్గనిర్దేశం చేయండి. |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM ప్రొవైడర్ క్రెడెన్షియల్స్ లేకుండానే హోస్ట్-ఏజెంట్ Markdown అనువాదం ద్వారా MCP క్లయింట్‌ను మార్గనిర్దేశం చేయండి. |
| `translate_repository_prompt` | మొదట dry-run చేయడంతో రిపాజిటరీ అనువాదం ద్వారా MCP క్లయింట్‌ను మార్గనిర్దేశం చేయండి. |

## కాపీ-పేస్ట్ ఉదాహరణలు

Markdown కంటెంట్ అనువదించండి:

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

అనువదించిన Markdown లింకులను రిరైటు చేయండి:

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

హోస్ట్ ఏజెంట్ మోడల్‌తో Markdown అనువదించండి:

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

హోస్ట్ ఏజెంట్ ప్రతి తిరిగి ఇచ్చిన ఛంక్‌ని అనువదించిన తర్వాత, `start_markdown_agent_translation` ద్వారా తిరిగి వచ్చిన పూర్తి `job` ఆబ్జెక్టుతో జాబ్‌ని పూర్తి చేయండి:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

రిపాజిటరీ అనువాదాన్ని ప్రీవ్యూ చేయండి:

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

## సమస్యలు పరిష్కరణ

| సమస్య | ప్రయత్నించాల్సిందేమిటి |
| --- | --- |
| MCP క్లయింట్ `co-op-translator-mcp` ను కనుగొనలేకపోతోంది. | అబ్సల్యూట్ Python ఎగ్జిక్యూటబుల్ పాత్ మరియు `["-m", "co_op_translator.mcp.server"]` సోర్స్ చెకౌట్ కాన్ఫిగరేషన్ ఉపయోగించండి. |
| సర్వర్ జాబితాలో ఉంది కాని అనువాదం విఫలమవుతుంది. | `get_configuration_status` పిలవండి మరియు LLM ప్రొవైడర్ అందుబాటులో ఉందో నిర్ధారించండి. |
| మీరు ప్రొవైడర్ క్రెడెన్షియల్స్ లేకుండా Markdown లేదా నోట్‌బుక్ అనువాదం కోరుకుంటున్నారు. | హోస్ట్ ఏజెంట్ ఛంక్స్‌ను అనువదింపచేయడానికి `start_markdown_agent_translation` / `finish_markdown_agent_translation` లేదా నోట్‌బుక్ సమానాలను ఉపయోగించండి. |
| చిత్ర అనువాదం విఫలమవుతోంది. | Azure AI Vision వేరియబుల్స్ సెట్ చేయబడ్డాయా అని నిర్ధారించండి మరియు `get_configuration_status` పిలవండి. |
| రిపాజిటరీ అనువాదం ఫైళ్లను రాయడం లేదు. | స్పష్టమైన వినియోగదారు అంగీకారం తర్వాత మాత్రమే `dry_run=false` మరియు `confirm_write=true` సెట్ చేయండి. |
| క్లయింట్ కాన్ఫిగ్లో మార్పులు కనిపించడం లేదు. | MCP క్లయింట్‌ను రీస్టార్ట్ లేదా రిలోడ్ చేయండి. |

## సురక్షత సూచనలు

- MCP టూల్ పిలుపులు హోస్ట్ అప్లికేషన్ ద్వారా మోడల్ నియంత్రణలో ఉంటాయి, కాబట్టి రిపాజిటరీ అనువాదం డిఫాల్ట్‌గా dry-run ఉంటుంది.
- పూర్తి రిపాజిటరీ అనువాదం అనేక ఫైళ్ళను సృష్టించగలదు, నవీకరించగలదు లేదా తొలగించగలదు. `confirm_write=true` సెటింగ్ చేయడానికి ముందుగా స్పష్టమైన వినియోగదారు అనుమతిని తీసుకోండి.
- configuration status టూల్ ఎప్పుడూ API కీలు, ఎండ్పాయింట్లు లేదా ఇతర రహస్య విలువలను తిరిగి ఇవ్వదు.
- చిత్రం అనువాదం base64 ఇమేజ్ డాటాను తిరిగి ఇస్తుంది. పెద్ద చిత్రాలు పెద్ద టూల్ రిస్పాన్సులను ఉత్పత్తి చేయవచ్చు.
- ఏజెంట్-అసిస్టెడ్ టూల్స్ మూల ఛంక్‌లు మరియు ప్రాంప్ట్స్‌ను MCP హోస్ట్‌కు ఇవ్వగలవు. వాటిని వినియోగదారు ఆ హోస్ట్ ఏజెంట్ మోడల్‌కు పంపటానికి అనుకూలమైన కంటెంట్‌తోనే ఉపయోగించండి.