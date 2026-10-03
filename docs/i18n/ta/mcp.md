# MCP சர்வர்

Co-op Translator ஏஜென்டுகள், எடிட்டர்கள், மற்றும் MCP-உடன் பொருந்தக்கூடிய கிளையன்டுகளுக்கான Model Context Protocol சேவையகத்தை உள்ளடக்குகிறது.

இயல்புநிலை உள்ளூர் அமைப்பிற்கு, பயனர்கள் தனி சர்வரை கைமுறையாக ஓட்டுவதில்லை. அவர்கள் தங்கள் MCP கிளையன்டை அமைக்கின்றனர், மற்றும் கிளையன்ட் Co-op Translator கருவிகள் தேவைப்படும்போது `co-op-translator-mcp` ஐ `stdio` வழியாக தானாகத் தொடங்கும்.

CLI, Python API, மற்றும் MCP ஆகியவற்றின் இடையில் தேர்வு செய்ய நினைத்தால், [உங்கள் செயல்முறையை தேர்வு செய்க](workflows.md) என்றதிலிருந்து தொடங்குங்கள்.

ஏஜெண்ட் அல்லது எடிட்டர் Co-op Translator ஐ நேரடியாக அழைக்க வேண்டும் என்றால் MCP-ஐப் பயன்படுத்தவும்:

| பயனர் இலக்கு | MCP கருவிகள் |
| --- | --- |
| ஒரு Markdown ஆவணம், நோட்புக், அல்லது படத்தை மொழிபெயர்த்தல் | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| ஹோஸ்ட் ஏஜென்ட் மாதிரியைப் பயன்படுத்தி Markdown அல்லது நோட்புக் உள்ளடக்கத்தை மொழிபெயர்த்தல் | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| வெளியீடு பாதையை தேர்ந்தெடுத்தபின் மொழிபெயர்க்கப்பட்ட Markdown அல்லது நோட்புக் இணைப்புகளை மீழ்கொடு எழுத்து | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI போல முழு ரெப்பொசிட்டரியை மொழிபெயர்த்தல் | `run_translation`, `translate_project` |
| LLM அனுமதிகள் இல்லாமல் மொழிபெயர்க்கப்பட்ட வெளியீட்டை மதிப்பாய்வு செய்தல் | `run_review` |
| திறன்கள் மற்றும் சூழ்நிலையை ஆய்வு செய்தல் | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP சர்வர் [Python API](api.md) இல் ஆவணப்படுத்தப்பட்ட அதே public Python API-ஐ சுற்றி வைத்திருக்கிறது. Provider-ஆல் ஆதரிக்கப்படும் கருவிகள் CLI மற்றும் Python API போலவே கட்டமைக்கப்பட்ட providers-ஐப் பயன்படுத்துகின்றன. ஏஜெண்ட்-உதவியுடைய கருவிகள் MCP ஹோஸ்ட் ஏஜெண்ட் மொழிபெயர்க்க chunks-ஐ தயார் செய்து, பின்னர் இறுதி Markdown அல்லது notebook-ஐ மீட்டமைக்க Co-op Translator-ஐப் பயன்படுத்துகின்றன.

## படி 1: Co-op Translator ஐ நிறுவவும் மற்றும் கட்டமைக்கவும்

உங்கள் MCP கிளையன்ட் பயன்படுத்தப் போகும் Python சூழலில் Co-op Translator-ஐ நிறுவவும்:

```bash
pip install co-op-translator
```

இந்த ரெப்போசிட்டரியிலிருந்து உள்ளூர் அபிவிருத்திக்காக, பாக்கேஜை திருத்தக்கூடிய (editable) முறையில் நிறுவுங்கள்:

```bash
pip install -e .
```

உங்கள் MCP கிளையன்ட் பயன்படுத்தவிருக்கும் மொழிபெயர்ப்பு முறையை தேர்வு செய்யவும்:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| வழங்குநர் ஆதரவுடன் | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, அல்லது `run_translation` என்பதை அழைக்கிறது. | மொழிபெயர்ப்புக்கு Azure OpenAI, OpenAI, அல்லது Anthropic தேவை. பட மொழிபெயர்ப்பிற்காக கூடுதலாக Azure AI Vision தேவை. |
| Agent-assisted | MCP ஹோஸ்ட் ஏஜெண்ட் `start_markdown_agent_translation` அல்லது `start_notebook_agent_translation` மூலம் திருப்பி வழங்கப்படும் chunks-ஐ மொழிபெயர்க்கிறது. | Markdown அல்லது notebook chunks-களுக்கான Co-op Translator LLM provider சான்றுகள் தேவையில்லை. பட மொழிபெயர்ப்பு இன்னும் agent-assisted முறையில் கையாளப்படவில்லை. |

Codex அல்லது Claude Code போன்ற ஏஜெண்டில் உள்ள Markdown அல்லது notebook மொழிபெயர்ப்புடன் தொடங்கினால், agent-assisted முறையுடன் தொடங்குங்கள். Co-op Translator தானாகவே உங்கள் கட்டமைக்கப்பட்ட providers-ஐ அழைக்க வேண்டும் என்றால், படங்களை மொழிபெயர்க்கும்போது அல்லது CLI போன்ற ரெப்போசிட்டரி-நிலைக் மொழிபெயர்ப்புகளை இயக்கும்போது provider-backed முறையைப் பயன்படுத்துங்கள்.

வழங்குநர்-ஆதாரமான பணிகளுக்கு ஒரு வழங்குநரை அமைக்கவும்:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# அல்லது OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# அல்லது Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

வழங்குநர்-ஆதாரமான பட மொழிபெயர்ப்பிற்கு கூடுதலாக தேவையானவை:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    ஏஜெண்ட்-உதவிய முறை தற்போது Markdown மற்றும் நோட்புக் Markdown செல்களை மட்டுமே கையாள்கிறது. பட மொழிபெயர்ப்பு இன்னும் புரொவைய்டர்-ஆதரிக்கப்பட்ட பட பணிச்சேர்க்கையை பயன்படுத்துகிறது மற்றும் OCR மற்றும் வடிவமைப்பு-அறிந்து ரெண்டரிங்குக்கு Azure AI Vision தேவை.

## படி 2: உங்கள் MCP கிளையன்டை கட்டமைக்கவும்

சாதாரண உள்ளூர் `stdio` அமைப்புக்காக, உங்கள் MCP கிளையன்ட் கட்டமைப்பில் Co-op Translator ஐச் சேர்க்கவும். கிளையன்ட் அந்த செயலியை தானாகத் தொடங்கி நிறுத்தும்.

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

macOS அல்லது Linux இல் மூலச் செக்-அவுட் கட்டமைப்பு:

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

MCP கிளையன்ட் கட்டமைப்பை மாற்றிய பிறகு, புதிய சர்வரை கண்டுபிடிக்க கிளையன்ட்டை மறுதொடக்கம் செய்யவோ அல்லது மீளேற்றி கொள்ளவோ செய்யவும்.

## படி 3: கிளையன்டில் சேவையகத்தை சரிபார்க்கவும்

கிடைக்கக்கூடிய கருவிகளை பட்டியலிட MCP கிளையன்ட்டை கேட்கவும், அல்லது முதலில் வாசிப்பிற்கான உதவிகளில் ஒன்றை அழைக்கவும்:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Useful first checks:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | சேவையகம் அணுகக்கூடியதா என்பதை உறுதி செய்து கிடைக்கும் வேலைபாடுகளை காட்டுகிறது. |
| `list_supported_languages` | பேக்கேஜ் செய்யப்பட்ட மொழி தரவுகளை ஏற்றக்கூடியதா என்பதை உறுதிசெய்கிறது. |
| `get_configuration_status` | ரகசிய மதிப்புகளை வெளிப்படுத்தாமலே LLM மற்றும் Vision புரொவைய்டர்கள் கிடைப்பதை உறுதிசெய்கிறது. |

## படி 4: ஒரு வேலைநடை தேர்ந்தெடுக்கவும்

### தனித்தனியான கோப்புகள் அல்லது ஆவணங்களை மொழிபெயர்க்க

MCP கிளையன்ட்டில் ஏற்கனவே ஆவண உள்ளடக்கம் அல்லது படத்தின் பாதை இருந்தால் மற்றும் Co-op Translator கட்டமைக்கப்பட்ட மொழிபெயர்ப்பு வழங்குநர்களை அழைக்க வேண்டும் என்றால், வழங்குநர்-ஆதரிக்கப்பட்ட உள்ளடக்க கருவிகளைப் பயன்படுத்தவும்.

For Markdown:

1. Call `translate_markdown_content` with `document`, `language_code`, and optionally `source_path`.
2. மொழிபெயர்க்கப்பட்ட முடிவு Co-op Translator வெளியீட்டு அமைப்பில் எழுதப்பட வேண்டுமானால், `rewrite_markdown_paths`-ஐ அழைக்கவும்.
3. கிளையன்ட் இறுதி `content`-ஐ எழுதவோ அல்லது திருப்பி வழங்கவோ விடுங்கள்.

For notebooks:

1. Call `translate_notebook_content` with notebook JSON and `language_code`.
2. மொழிபெயர்க்கப்பட்ட நோட்புக் இணைப்புகளை இலக்கு பாதைக்கு பொருத்தமாக சரிசெய்ய வேண்டுமெனில் `rewrite_notebook_paths`-ஐ அழைக்கவும்.
3. இறுதி நோட்புக் JSON-ஐ எழுதி அல்லது திருப்பி வழங்கவும்.

For images:

1. Call `translate_image_content` with `image_path`, `language_code`, and optional `root_dir` or `fast_mode`.
2. Read the returned `data_base64` and `mime_type`.
3. `output_path` வழங்கப்பட்டிருந்தால், மொழிபெயர்க்கப்பட்ட படம் அந்த பாதையிலும் சேமிக்கப்படும்.

உள்ளடக்க கருவிகள் திட்டக் கண்டுபிடிப்பு, மெட்டாடேட்டா புதுப்பிப்புகள், எச்சரிக்கை குறிப்புகள் அல்லது பாதையை தானாக மறுஅமைக்குதல் போன்றவற்றைச் செய்யாது. Co-op Translator LLM வழங்குநர் அங்கீகாரங்கள் இல்லாமல் ஹோஸ்ட் முகவர் Markdown அல்லது நோட்புக் தொகுதிகளை மொழிபெயர்க்கவிருந்தால், கீழே கொடுக்கப்பட்ட முகவர்-உதவியுடன் செயல்முறையை பயன்படுத்தவும்.

### ஹோஸ்ட் ஏஜெண்ட் மாதிரியுடன் மொழிபெயர்க்க

MCP ஹோஸ்ட் ஏஜென்ட் (உதாரணத்திற்கு ஒரு கோடிங் அஸிஸ்டன்ட்) மொழிபெயர்த்த உரையை உருவாக்க வேண்டுமென்றால், LLM வழங்குனரை Co-op Translator க்காக அமைக்காமல், ஏஜென்டு-உதவியுடன் செயல்படும் கருவிகளைப் பயன்படுத்தவும்.

chat-அடிப்படையிலான MCP கிளையண்டில், பொதுவாக நீங்கள் கருவி JSON-ஐ 직접 எழுத தேவையில்லை. ஏஜெண்டிடம் ஏஜென்ட்-உதவியுடன் செயல்முறையைப் பயன்படுத்துமாறு கேளுங்கள்:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

நோட்புக்குகளுக்கு, அதே மாதிரியைப் பயன்படுத்தவும்:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

உங்கள் MCP கிளையண்ட் சர்வர் prompts-ஐ ஆதரிக்கின், அதே செயல்முறை வழிமுறைகளை கிளையண்ட் ஏற்ற `agent_assisted_markdown_translation_prompt`-ஐப் பயன்படுத்துங்கள்.

For Markdown:

1. Call `start_markdown_agent_translation` with `document`, `language_code`, and optionally `source_path`.
2. ஹோஸ்ட் ஏஜென்ட்-இல் திரும்ப வந்த ஒவ்வொரு chunk-ஐ `prompt`-ஐ பின்பற்றி மொழிபெயர்க்கவும்.
3. Call `finish_markdown_agent_translation` with the original `job` and translated chunks using `chunk_id` and `translated_text`.
4. உள்ளடக்கம் மொழிபெயர்க்கப்பட்ட இலக்கு பாதையில் எழுதப்படுவதாக இருந்தால், `rewrite_markdown_paths`-ஐ அழைக்கவும்.

For notebooks:

1. Call `start_notebook_agent_translation` with notebook JSON and `language_code`.
2. திருப்பி வழங்கப்பட்ட ஒவ்வொரு துண்டையும் ஹோஸ்ட் ஏஜென்டில் மொழிபெயர்க்கவும்.
3. Call `finish_notebook_agent_translation` with the original `job` and translated chunks.
4. மொழிபெயர்க்கப்பட்ட நோட்புக் இணைப்புகளுக்கு இலக்கு பாதையைச் சரிசெய்ய வேண்டும் என்றால் `rewrite_notebook_paths`-ஐ அழைக்கவும்.

ஏஜென்ட்-உதவியுடன் செயல்படும் கருவிகள் Co-op Translator-இலிருந்து கட்டமைக்கப்பட்ட LLM வழங்குனரை அழைக்காது. திரும்ப வழங்கப்பட்ட chunk-களை மொழிபெயர்ப்பது ஹோஸ்ட் ஏஜென்டின் பொறுப்பாகும். Co-op Translator Markdown சக்குகள் பிரித்தல், placeholder பாதுகாப்பு, frontmatter மறுதொடக்கம், நோட்புக் செல் மாற்றம் மற்றும் மொழிபெயர்ப்புக்குப்பிந்தைய சீரமைப்பை கையாளுகிறது.

### முழு ரெப்பொசிட்டரியை மொழிபெயர்க்க

பயனர் Co-op Translator-ஐ `translate` CLI போல நடக்க நினைத்தால் `run_translation`-ஐ பயன்படுத்துங்கள்.

Repository மொழிபெயர்ப்பு இயல்பாக `dry_run=true` ஆகும், ஆகவே ஏஜென்ட் கோப்பு மாற்றங்களுக்கு முன் பரப்பைப் பரிசீலிக்கலாம்:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

The `run_translation` result includes an `events` array with versioned
`co-op.translation.event.v1` progress events. MCP clients should use fields such
as `type`, `stage_key`, `completed`, `total`, and `current_path` instead of
parsing captured console text. Pass `json_events_path` to also write those events
to an NDJSON file.

எழுதுவதற்கு அனுமதி அளிக்க, கூப்பிடுபவர் `dry_run=false` மற்றும் `confirm_write=true` இரண்டையும் அமைத்திருக்க வேண்டும்:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` என்பது `run_translation` இற்கான இணக்கத்தன்மை அழைப்புப் பெயராக வெளிப்படுத்தப்பட்டுள்ளது.

### மொழிபெயர்க்கப்பட்ட வெளியீட்டை ஆய்வு செய்க

LLM அல்லது Vision சான்றிதழ்களைத் தேவையில்லை என்று இருக்கும் தீர்மானமான சரிபார்ப்புகளுக்காக `run_review`-ஐப் பயன்படுத்தவும்:

!!! note "Beta"
    MCP பீட்டா `run_review` API-ஐ வெளியிடுகிறது. இது வாசிப்பிற்கான விமர்சன வேலைவாய்ப்புகளுக்கு பாதுகாப்பானது, ஆனால் விமர்சனச் சோதனைகள் மற்றும் பிரச்சினை ஸ்கீமைகள் மாறக்கூடும்.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

முடிவு பிடிக்கப்பட்ட உரை வெளியீடையும், கிடைத்தால் ஒரு கட்டமைக்கப்பட்ட விமர்சன சுருக்கத்தையும் உள்ளடக்குகிறது.

## கைமுறை சேவையக இயக்கங்கள்

கைமுறை ஓட்டங்கள் பெரும்பாலும் பிழைதிருத்தத்திற்கோ அல்லது நீண்ட காலம் இயங்கும் சர்வர் போன்ற நடத்தை கொண்ட டிரான்ஸ்போர்டுகளுக்காகவே இருக்கும்.

Debug the default stdio server:

```bash
co-op-translator-mcp
```

Run from a source checkout:

```bash
python -m co_op_translator.mcp.server
```

நீண்ட காலமாக இயங்கும் HTTP அல்லது SSE சர்வரை இயக்கவும்:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

உள்ளூர்நிரலாக்கி மற்றும் ஏஜென்ட் ஒருங்கிணைப்புகளுக்கு, படி 2-இல் கிளையண்ட்-மேலாண்மையிலான `stdio` கட்டமைப்பை முன்னுரிமையாகப் பயன்படுத்தவும்.

## கருவிகள்

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Markdown உள்ளடக்கத்தை மொழிபெயர்க்க. | இல்லை |
| `translate_notebook_content` | நோட்புக் JSON இல் Markdown செல்களை மொழிபெயர்க்க. | இல்லை |
| `translate_image_content` | ஒரு படத்திலுள்ள உரையை மொழிபெயர்த்து base64 படத் தரவைக் கொடுக்கும். | விருப்பம், `output_path` வழங்கப்பட்டால் மட்டுமே |
| `start_markdown_agent_translation` | Co-op Translator LLM புரொவைய்டர் அங்கீகாரங்கள் இல்லாமல் ஹோஸ்ட் ஏஜெண்ட் மொழிபெயர்க்கக் கூடிய வகையில் Markdown பகுதிகளை தயாரிக்க. | இல்லை |
| `finish_markdown_agent_translation` | ஹோஸ்ட் ஏஜெண்ட் மொழிபெயர்த்த பகுதிகளிலிருந்து Markdown ஐ மீண்டும் உருவாக்க. | இல்லை |
| `start_notebook_agent_translation` | நோட்புக் Markdown-செல் பகுதிகளை ஹோஸ்ட் ஏஜெண்ட் மொழிபெயர்க்க தயாரிக்க. | இல்லை |
| `finish_notebook_agent_translation` | ஹோஸ்ட் ஏஜெண்ட் மொழிபெயர்த்த பகுதிகளிலிருந்து நோட்புக் JSON ஐ மீண்டும் உருவாக்க. | இல்லை |
| `rewrite_markdown_paths` | மொழிபெயர்க்கப்பட்ட இலக்குக்காக Markdown உடல் மற்றும் frontmatter பாதைகளை மறுசரிசெய். | இல்லை |
| `rewrite_notebook_paths` | நோட்புக் Markdown செல்களில் உள்ள பாதைகளை மறுசரிசெய். | இல்லை |
| `run_translation` | CLI போல திட்ட மட்டத்திற்கு மொழிபெயர்ப்பு இயக்கு. | ஆம், `dry_run=false` மற்றும் `confirm_write=true` இருக்கும்போது |
| `translate_project` | `run_translation` க்கான இணக்கமான பெயர்ப்பு. | ஆம், `dry_run=false` மற்றும் `confirm_write=true` இருக்கும்போது |
| `run_review` | தீர்மானப்படுத்தக்கூடிய மதிப்பாய்வு சரிபார்ப்புகளை இயக்கு. | இல்லை |
| `get_configuration_status` | ரகசியங்களை வெளிப்படுத்தாமலே கட்டமைக்கப்பட்ட LLM மற்றும் Vision புரொவைய்டர்கள் பற்றிய தகவலை அறிவிக்க. | இல்லை |
| `list_supported_languages` | ஆதரவு வழங்கப்படும் இலக்கு மொழி குறியீடுகளை பட்டியலிடு. | இல்லை |
| `get_api_overview` | கிடைக்கக்கூடிய MCP வேலைநடவடிக்கைகள் மற்றும் கருவிகளை விவரிக்க. | இல்லை |

## வளங்கள்

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | வேலைநடவடிக்கைகள் மற்றும் கருவிகள் பற்றிய JSON மேலோட்டம். |
| `co-op://supported-languages` | ஆதரிக்கப்படும் மொழி குறியீடுகளின் JSON பட்டியல். |
| `co-op://configuration` | ரகசியங்கள் இல்லாமல் புரொவைக்டர் கிடைப்புத் தகவல்களின் JSON சுருக்கம். |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | உள்ளடக்க மொழிபெயர்ப்பு மற்றும் விருப்பமான பாதை மறுஅழைக்கைக்கு MCP கிளையன்டை வழிநடத்தவும். |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM புரொவைய்டர் அங்கீகாரங்கள் இல்லாமல் ஹோஸ்ட் ஏஜெண்ட் மூலம் Markdown மொழிபெயர்ப்புக்கு MCP கிளையன்டை வழிநடத்தவும். |
| `translate_repository_prompt` | முதலில் dry-run செய்து பின்னர் ரெப்பொசிட்டரி மொழிபெயர்ப்புக்கு MCP கிளையன்டை வழிநடத்தவும். |

## காப்பி-பேஸ்ட் உதாரணங்கள்

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

ஹோஸ்ட் ஏஜென்ட் மாடலைப் பயன்படுத்தி Markdown ஐ மொழிபெயர்க்கவும்:

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

ஹோஸ்ட் ஏஜென்ட் ஒவ்வொரு திரும்பவந்த துண்டையும் மொழிபெயர்த்த பிறகு, `start_markdown_agent_translation` வழங்கும் முழுமையான `job` பொருளை கொண்டு பணியை முடிக்கவும்:

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

## பிரச்சினை தீர்வு

| Problem | What to try |
| --- | --- |
| MCP கிளையன்ட் `co-op-translator-mcp` ஐ கண்டறிய முடியவில்லை. | முழுமையான Python executable பாதையை மற்றும் `["-m", "co_op_translator.mcp.server"]` source checkout கட்டமைப்பை பயன்படுத்தவும். |
| சேவையகம் பட்டியலிடப்பட்டுள்ளது ஆனால் மொழிபெயர்பு தோல்வியடைந்துள்ளது. | `get_configuration_status` ஐ அழைத்து LLM வழங்குநர் கிடைக்கிறதா என்பதை உறுதிப்படுத்தவும். |
| நீங்கள் வழங்குநர் அடையாளச் சான்றுகள் இல்லாமல் Markdown அல்லது நோட்புக் மொழிபெயர்ப்பை விரும்பினால். | ஹோஸ்ட் ஏஜென்ட் துண்டுகளை மொழிபெயர்க்க `start_markdown_agent_translation` / `finish_markdown_agent_translation` அல்லது நோட்புக் சமமானவற்றை பயன்படுத்துங்கள். |
| பட மொழிபெயர்ப்பு தோல்வியடைந்தது. | Azure AI Vision மாறிலிகள் அமைக்கப்பட்டுள்ளதா என்பதை உறுதி செய்து `get_configuration_status` ஐ அழைக்கவும். |
| சேமிப்பக மொழிபெயர்ப்பு கோப்புகளை எழுதவில்லை. | தெளிவான பயனர் அனுமதியைப் பெற்ற பிறகு மட்டுமே `dry_run=false` மற்றும் `confirm_write=true` ஐ அமைக்கவும். |
| கிளையன்ட் கட்டமைப்பில் செய்யப்பட்ட மாற்றங்கள் தோன்றவில்லை. | MCP கிளையன்டை மறுதொடக்கம் செய்யவும் அல்லது மீண்டும் ஏற்றவும். |

## பாதுகாப்பு குறிப்புகள்

- MCP கருவி அழைப்புகள் ஹோஸ்ட் பயன்பாட்டால் மாதிரியால் கட்டுப்படுத்தப்படுகின்றன, எனவே ரெப்பொசிட்டரி மொழிபெயர்ப்பு இயல்பாக dry-run ஆகும்.
- முழு ரெப்பொசிடரி மொழிபெயர்ப்பு பல கோப்புகளை உருவாக்கலாம், புதுப்பிக்கலாம் அல்லது நீக்கலாம். `confirm_write=true` ஐ அமைக்கும்முன் பயனரின் தெளிவான அனுமதியை கேட்கவும்.
- கட்டமைப்பு நிலை கருவி எப்போதும் API விசைகள், endpoints அல்லது பிற ரகசிய மதிப்புகளை வழங்காது.
- பட மொழிபெயர்ப்பு base64 படத் தரவாகப் பெறப்படுகிறது. பெரிய படங்கள் பெரிய கருவி பதில்களை உருவாக்கலாம்.
- ஏஜென்ட்-உதவியாளரான கருவிகள் மூலக் துண்டுகளையும் பிராம்ப்ட்களையும் MCP ஹோஸ்டுக்கு திரும்ப அளிக்கின்றன. பயனர் அந்த ஹோஸ்ட் ஏஜென்ட் மாதிரிக்கு அனுப்ப விரும்பும் உள்ளடக்கத்தினோடு மட்டுமே அவற்றைப் பயன்படுத்தவும்.
