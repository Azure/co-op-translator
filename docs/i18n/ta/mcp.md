# MCP சேவையகம்

Co-op Translator என்பது முகவர்கள், தொகுப்பாளர்கள் மற்றும் MCP-உடன் பொருந்தக்கூடிய கிளையன்டுகளுக்கான Model Context Protocol (MCP) சேவையகத்தை கொண்டுள்ளது.

இயல்புநிலை உள்ளூர் அமைப்பிற்கு, பயனர்கள் மற்றொரு சேவையகத்தை கைமுறையாக இயக்க வேண்டாம். அவர்கள் தங்கள் MCP கிளையன்டை கட்டமைக்கிறார்கள், மற்றும் கிளையன்ட் Co-op Translator கருவிகள் தேவைப்பட்டபோது `co-op-translator-mcp` ஐ தானாகவே `stdio` வழியாகத் தொடக்குகிறது.

நீங்கள் CLI, Python API மற்றும் MCP இடையே முடிவு செய்து கொண்டிருப்பின், [உங்கள் செயல்முறையைத் தேர்வு செய்யவும்](workflows.md) என்ற இடத்தில் தொடங்குங்கள்.

Agent அல்லது தொகுப்பாளர் Co-op Translator ஐ நேரடியாகப் பயன்படுத்த வேண்டும் என்றால் MCP ஐப் பயன்படுத்துங்கள்:

| பயனர் குறிக்கோள் | MCP கருவிகள் |
| --- | --- |
| ஒரு Markdown ஆவணம், நோட்புக் அல்லது படம் ஒன்றை மொழிபெயர்க்கவும் | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| ஹோஸ்ட் ஏஜென்ட் மாடலை பயன்படுத்தி Markdown அல்லது நோட்புக் உள்ளடக்கத்தை மொழிபெயர்க்கவும் | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| வெளிப்பாட்டு பாதையைத் தேர்வு செய்த பிறகு மொழிபெயர்க்கப்பட்ட Markdown அல்லது நோட்புக் இணைப்புகளை மறுஎழுதுக | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI போல முழு ரெப்போசிடரியை மொழிபெயர்க்கவும் | `run_translation`, `translate_project` |
| LLM அங்கீகாரம் இல்லாமல் மொழிபெயர்க்கப்பட்ட வெளிப்பாட்டை பரிசீலிக்கவும் | `run_review` |
| திறன்கள் மற்றும் சுற்றுச்சூழல் நிலையை ஆய்வு செய்யவும் | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP சேவையகம் [Python API](api.md) இல் ஆவணப்படுத்தப்பட்டுள்ள அதே பொதுப் Python API ஐ கட்டமைக்கிறது. வழங்குநர் ஆதரித்த கருவிகள் CLI மற்றும் Python API உடன் பயன்படுத்தப்படும் அதே கொரஸ்ட் வழங்குநர்களைப் பயன்படுத்துகின்றன. ஏஜென்ட் உதவியுடன் உள்ள கருவிகள் MCP ஹோஸ்ட் ஏஜென்ட் மூலம் மொழிபெயர்க்கப்பட்ட பாக்களைத் தயாரித்து, பின்னர் Co-op Translator final Markdown அல்லது நோட்புக் உருவாக்க பயன்படுத்து முடிக்கின்றன.

## படி 1: Co-op Translator ஐ நிறுவி கட்டமைக்கவும்

உங்கள் MCP கிளையன்ட் பயன்படுத்தும் Python சுற்றுச்சூழலில் Co-op Translator ஐ நிறுவவும்:

```bash
pip install co-op-translator
```

இந்த தொகுப்பிலிருந்து உள்ளூர் அபிவிருத்திக்காக, தொகுப்பை தொகுக்கக்கூடிய முறையில் நிறுவவும்:

```bash
pip install -e .
```

உங்கள் MCP கிளையன்ட் பயன்படுத்தும் மொழிபெயர்ப்பு முறையை தேர்வு செய்க:

| Mode | இத்துக்காக பயன்படுத்தவும் | அங்கீகாரங்கள் |
| --- | --- | --- |
| Provider-backed | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, அல்லது `run_translation` ஐ அழைக்கும் போது. | Markdown மற்றும் நோட்புக் மொழிபெயர்ப்பு Azure OpenAI அல்லது OpenAI தேவைப்படுகிறது. பட மொழிபெயர்ப்புக்கு Azure AI Vision கூட தேவை. |
| Agent-assisted | MCP ஹோஸ்ட் ஏஜென்ட் `start_markdown_agent_translation` அல்லது `start_notebook_agent_translation` மூலம் திரும்பும் பகுதிகளை மொழிபெயர்க்கும். | Markdown அல்லது நோட்புக் பகுதிகளுக்கு Co-op Translator LLM வழங்குநர் அங்கீகாரம் தேவையில்லை. பட மொழிபெயர்ப்பு இன்னும் agent-assisted முறையில் உள்ளடக்கப்படவில்லை. |

Codex அல்லது Claude Code போன்ற ஏஜெண்ட் உள்ளே Markdown அல்லது நோட்புக் மொழிபெயரிப்பில் தொடங்கினால், agent-assisted முறையுடன் தொடங்குங்கள். Co-op Translator தானே உங்கள் கட்டமைக்கப்பட்ட வழங்குநர்களை அழைக்க வேண்டும் என்றால், படங்களை மொழிபெயர்க்கும்போது, அல்லது CLI போல ரெப்போ-தர்ம மொழிபெயர்ப்பு இயங்கும்போது provider-backed முறையைப் பயன்படுத்தவும்.

வழங்குநர் அங்கீகாரங்களை provider-backed வேலைநடைகள் בלבד கட்டமைக்கவும்:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed பட மொழிபெயர்ப்பு கூடுதல் தேவைகள்:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted முறையாக தற்போது Markdown மற்றும் நோட்புக் Markdown செல்களைக் கையாளுகிறது. பட மொழிபெயர்ப்பு இன்னும் provider-backed படைப்பு குழாயைப் பயன்படுத்துகிறது மற்றும் OCR மற்றும் அமைப்பு-அறிந்த ரெண்டரிங்கிற்கான Azure AI Vision தேவைப்படுகிறது.

## படி 2: உங்கள் MCP கிளையன்டை கட்டமைக்கவும்

இயல்புநிலை உள்ளூர் `stdio` அமைப்பிற்கு, உங்கள் MCP கிளையன்ட் கட்டமைப்பில் Co-op Translator ஐ சேர்க்கவும். கிளையன்ட் அந்த செயல்முறையை தானாகத் துவக்கி நிறுத்தும்.

நிறுவப்பட்ட தொகுப்பு கட்டமைப்பு:

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

Windows இல் மூலச் சரிபார்ப்பு கட்டமைப்பு:

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

macOS அல்லது Linux இல் மூலச் சரிபார்ப்பு கட்டமைப்பு:

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

MCP கிளையன்ட் கட்டமைப்பை மாற்றியபின், புதிய சேவையகத்தை கண்டறிவதற்கு கிளையன்டை மறுதொடக்கம் அல்லது மீள்நகர்த்தவும்.

## படி 3: கிளையன்டில் சேவையகத்தை உறுதிப்படுத்துக

கிடைக்கும் கருவிகளைப் பட்டியலிட MCP கிளையன்டை கேட்கவும், அல்லது முதலில் படிக்க மட்டும் பொருந்தும் உதவியாளர்களில் ஒருவரை அழைக்கவும்:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

ஆரம்பச் சரிபார்ப்புகளுக்குப் பயனுள்ளவை:

| கருவி | என்ன மெய்ப்பித்து காண்பிக்க வேண்டும் |
| --- | --- |
| `get_api_overview` | சேவையகம் அணுகக்கூடியதா என்பதை உறுதிசெய்கிறது மற்றும் கிடைக்கும் வேலைநடைகளைக் காட்டுகிறது. |
| `list_supported_languages` | பண்பொதிந்த மொழி தரவுகள் ஏற்றப்படக்கூடியவையாக உள்ளதா என்பதை உறுதிசெய்கிறது. |
| `get_configuration_status` | ரகசிய மதிப்புகளை வெளிப்படுத்தாமலே LLM மற்றும் Vision வழங்குநர் கிடைப்பை உறுதிசெய்கிறது. |

## படி 4: ஒரு செயன்முறை தேர்வு செய்க

### தனித்த கோப்புகள் அல்லது ஆவணங்களை மொழிபெயர்க்கவும்

MCP கிளையன்ட் ஏற்கனவே ஆவண உள்ளடக்கத்தை அல்லது பட பாதையை கொண்டிருந்தால் மற்றும் Co-op Translator க்கு தொகுப்புகளை அழைக்கவேண்டும் என்று நீங்கள் விரும்பினால் provider-backed content கருவிகளை பயன்படுத்தவும்.

Markdown க்காக:

1. `document`, `language_code`, மற்றும் விருப்பமாக `source_path` உடன் `translate_markdown_content` ஐ அழிக்கவும்.
2. மொழிபெயர்க்கப்பட்ட முடிவு Co-op Translator வெளிப்பாட்டு அமைப்பில் எழுதப்படவுள்ளதெனில், `rewrite_markdown_paths` ஐ அழிக்கவும்.
3. இறுதி `content` ஐ கிளையன்ட் எழுதவோ அல்லது திருப்பி அனுப்பவோ விடுங்கள்.

நோட்புக்குகளுக்கு:

1. நோட்புக் JSON மற்றும் `language_code` உடன் `translate_notebook_content` ஐ அழிக்கவும்.
2. மொழிபெயர்க்கப்பட்ட நோட்புக் இணைப்புகள் இலக்கு பாதைக்காக சரிசெய்யப்பட வேண்டுமெனில் `rewrite_notebook_paths` ஐ அழிக்கவும்.
3. இறுதி நோட்புக் JSON ஐ எழுதவோ அல்லது திருப்பி அனுப்பவோ செய்க.

படங்களுக்கு:

1. `image_path`, `language_code`, மற்றும் விருப்பமான `root_dir` அல்லது `fast_mode` உடன் `translate_image_content` ஐ அழிக்கவும்.
2. திரும்ப வரும் `data_base64` மற்றும் `mime_type` ஐ வாசிக்கவும்.
3. `output_path` வழங்கப்பட்டிருந்தால், மொழிபெயர்க்கப்பட்ட படம் அந்த பாதையிலும் சேமிக்கப்படும்.

உள்ளடக்க கருவிகள் திட்ட கண்டறிதல், மெட்டாடேட்டா மேம்பாடுகள், நிச்சய மாற்றக் குறிப்புகள் அல்லது தானாக பாதை மறுஎழுதல்களை செய்வதில்லை. ஹோஸ்ட் ஏஜென்ட் Co-op Translator LLM வழங்குநர் அங்கீகாரம் இல்லாமல் Markdown அல்லது நோட்புக் பகுதிகளை மொழிபெயரிக்க வேண்டும் என்றால், கீழுள்ள agent-assisted வேலைநடையைப் பயன்படுத்தவும்.

### ஹோஸ்ட் ஏஜென்ட் மாடலுடன் மொழிபெயர்க்கவும்

Azure OpenAI அல்லது OpenAI ஐ Co-op Translatorக்காக அமைக்காமல் MCP ஹோஸ்ட் ஏஜென்ட் (உதாரணமாக ஒரு கோடிங் உதவியாளர்) மொழிபெயர்க்கப்பட்ட உரையை உருவாக்க வேண்டும் என்றால் agent-assisted கருவிகளை பயன்படுத்தவும்.

அடி-அமைவுக் கிளையன்டில், சாதாரணமாக உங்களுக்கு கருவி JSON ကို பார்்றதற்கு தேவையில்லை. ஏஜென்டை agent-assisted வேலைநடை பயன்படுத்தச் சொல்லுங்கள்:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

நோட்புக்குகளுக்காக அதே முறைமைப் பின்பற்றவும்:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

உங்கள் MCP கிளையன்ட் சர்வர் ப்ரொம்ப்ட்களை ஆதரிக்கும் என்றால், அதே வேலைநடை மேற்கோள்களை ஏஜென்ட்-அசிஸ்ட்டெட் பாரம்பரிய ப்ரொம்ப்ட் `agent_assisted_markdown_translation_prompt` மூலம் கிளையன்ட் ஏற்றவைத்து கொள்ளுங்கள்.

Markdown க்காக:

1. `document`, `language_code`, மற்றும் விருப்பமாக `source_path` உடன் `start_markdown_agent_translation` ஐ அழிக்கவும்.
2. மீண்டும் பெறப்பட்ட ஒவ்வொரு பகுதிக்கும் ஹோஸ்ட் ஏஜென்டில் அந்த பகுதி `prompt` ஐ பின்பற்றி மொழிபெயர்க்கவும்.
3. மொழிபெயர்க்கப்பட்ட பகுதிகள் `chunk_id` மற்றும் `translated_text` உடன் மூலம் முதன்மை `job` உடன் `finish_markdown_agent_translation` ஐ அழிக்கவும்.
4. உள்ளடக்கம் மொழிபெயர்க்கப்பட்ட இலக்கு பாதையில் எழுதப்படவிருந்தால், `rewrite_markdown_paths` ஐ அழிக்கவும்.

நோட்புக்குகளுக்கு:

1. நோட்புக் JSON மற்றும் `language_code` உடன் `start_notebook_agent_translation` ஐ அழிக்கவும்.
2. மீண்டும் பெறப்பட்ட ஒவ்வொரு பகுதிக்கும் ஹோஸ்ட் ஏஜென்டில் மொழிபெயர்க்கவும்.
3. மதிப்பீடு செய்யப்பட்ட பகுதிகளுடன் மூல `job` ஐ `finish_notebook_agent_translation` ஐ அழிக்கவும்.
4. மொழிபெயர்க்கப்பட்ட நோட்புக் இணைப்புகள் இலக்கு-பாதை சரிசெய்யப்பட வேண்டுமெனில் `rewrite_notebook_paths` ஐ அழிக்கவும்.

Agent-assisted கருவிகள் Co-op Translator இலிருந்து Azure OpenAI அல்லது OpenAI ஐ அழைக்காது. திரும்ப வழங்கப்பட்ட பகுதிகளை மொழிபெயர்க்குவது ஹோஸ்ட் ஏஜெனட் பொறுப்பாகும். Co-op Translator Markdown பகுதி பிளக்கிங், placeholder பாதுகாப்பு, frontmatter மறுவமைப்பு, நோட்புக் செல் மாற்றம் மற்றும் மொழிபெயர்ப்பின் பிறகு ஒழுங்குபடுத்தலைச் செய்கிறது.

### முழு ரெப்போசிடரியை மொழிபெயர்க்கவும்

பயனர் Co-op Translator ஐ CLI போல நடந்து செயல்படச் செய்யும்போது `run_translation` ஐ பயன்படுத்தவும்.

ரெப்போசிடரி மொழிபெயர்ப்பு இயல்பாக `dry_run=true` ஆகும், எனக்கு ஏஜெண்ட் கோம்பத்தில் உருவாக்கப்படும் கோப்பு மாற்றங்களைப் பரிசீலிக்க முடியும்:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

எழுதALLOW செய்ய, அழைப்பதாரர் இரண்டையும் `dry_run=false` மற்றும் `confirm_write=true` ஆக அமைக்க வேண்டும்:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` என்பது `run_translation` க்கான இணக்கமான ஆலியாஸ் ஆக வெளிப்படுத்தப்பட்டுள்ளது.

### மொழிபெயர்க்கப்பட்ட வெளிப்பாட்டை பரிசீலனை செய்யவும்

LLM அல்லது Vision அங்கீகாரம் தேவையாத உறுதிப்படுத்திய சரிபார்ப்புகளுக்கு `run_review` ஐ பயன்படுத்தவும்:

!!! note "Beta"
    MCP பெருங்கோலி `run_review` API ஐ வீடுபோக எக்ஸ்போஸ் செய்கிறது. இது படிக்க மட்டும் பரிசீலனை வேலைநடைகளுக்கு பாதுகாப்பானது, ஆனால் பரிசீலனை சோதனைகள் மற்றும் பிரச்சார ஸ்கீமா பரிணாமம் அடையலாம்.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

முடிவு பிடிக்கப்பட்ட உரை வெளியீடு மற்றும் கிடைக்கும்போது அமைக்கப்பட்ட ஒருங்கிணைந்த பரிசீலனை சாராம்சத்தை கொண்டுள்ளது.

## கைமுறை சேவையக இயக்கங்கள்

கைமுறை இயக்கங்கள் பெரும்பாலும் பிழைதிருத்தத்துக்கு அல்லது நீண்டகால சேவையகப் போன்றதாக நடக்கும் போக்குவரதுகளுக்கு உகந்தவை.

இயல்புநிலை stdio சேவையகத்தை பிழைதிருத்து:

```bash
co-op-translator-mcp
```

மூலச் சரிபார்ப்பில் இருந்து இயக்கவும்:

```bash
python -m co_op_translator.mcp.server
```

நீண்டகால HTTP அல்லது SSE சேவையகத்தை இயக்கவும்:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

உள்ளூரில் தொகுப்பாளரும் ஏஜெண்ட் ஒருங்கிணைப்புகளுக்கும், படி 2 இல் கிளையன்ட்-கையாளப்பட்ட `stdio` கட்டமைப்பை முதன்மையாகப் பயன்படுத்தவும்.

## கருவிகள்

| கருவி | நோக்கம் | கோப்புகளை எழுதி விடுமா |
| --- | --- | --- |
| `translate_markdown_content` | Markdown ஸ்ட்ரிங்கை மொழிபெயர்க்கவும். | இல்லை |
| `translate_notebook_content` | நோட்புக் JSON இல் Markdown செல்களை மொழிபெயர்க்கவும். | இல்லை |
| `translate_image_content` | ஒரு படத்தில் உள்ள உரையை மொழிபெயர்த்து base64 படம் தரவைத் திருப்பி விடும். | விருப்பமானது, மட்டும் `output_path` வழங்கப்பட்டபோது |
| `start_markdown_agent_translation` | Co-op Translator LLM அங்கீகாரம் இல்லாமல் ஹோஸ்ட் ஏஜென்ட் மொழிபெயரிக்க Markdown பகுதிகளை தயார் செய்க. | இல்லை |
| `finish_markdown_agent_translation` | ஹோஸ்ட்-ஏஜென்ட் மொழிபெயரித்த பகுதிகளிலிருந்து Markdown ஐ மீண்டும் கட்டமைக்கவும். | இல்லை |
| `start_notebook_agent_translation` | ஹோஸ்ட் ஏஜென்ட் மொழிபெயரிக்க நோட்புக் Markdown-செல் பகுதிகளை தயார் செய்க. | இல்லை |
| `finish_notebook_agent_translation` | ஹோஸ்ட்-ஏஜென்ட் மொழிபெயரித்த பகுதிகளிலிருந்து நோட்புக் JSON ஐ மீண்டும் கட்டமைக்கவும். | இல்லை |
| `rewrite_markdown_paths` | மொழிபெயர்க்கப்பட்ட இலக்கு-path க்காக Markdown உடல் மற்றும் frontmatter பாதைகளை மறுஎழுதுக. | இல்லை |
| `rewrite_notebook_paths` | நோட்புக் Markdown செல்களின் உள்ளே பாதைகளை மறுஎழுதுக. | இல்லை |
| `run_translation` | CLI போலுள்ள திட்ட நிலை மொழிபெயர்ப்பு இயக்கவும். | `dry_run=false` மற்றும் `confirm_write=true` ஆகியபோது ஆம் |
| `translate_project` | `run_translation` க்கான இணக்கமான ஆலியாஸ். | `dry_run=false` மற்றும் `confirm_write=true` ஆகியபோது ஆம் |
| `run_review` | நிர்ணயமான பரிசீலனை சோதனைகளை நடக்க. | இல்லை |
| `get_configuration_status` | ரகசியங்களை வெளிப்படுத்தாமலே கட்டமைக்கப்பட்ட LLM மற்றும் Vision வழங்குநர்களைப் புகாரளிக்கவும். | இல்லை |
| `list_supported_languages` | ஆதரிக்கப்படும் இலக்கு மொழி குறியீடுகளை பட்டியலிடவும். | இல்லை |
| `get_api_overview` | கிடைக்கக்கூடிய MCP வேலைநடைகள் மற்றும் கருவிகளை விவரிக்கவும். | இல்லை |

## வளங்கள்

| வள URI | நோக்கம் |
| --- | --- |
| `co-op://api` | வேலைநடைகள் மற்றும் கருவிகளின் JSON இருப்பு முறை. |
| `co-op://supported-languages` | ஆதரிக்கப்படும் மொழி குறியீடுகளின் JSON பட்டியல். |
| `co-op://configuration` | ரகசியம் இல்லாமல் வழங்குநர் கிடைப்புத் தகவலின் JSON சுருக்கம். |

## ப்ரொம்ப்ட்கள்

| ப்ரொம்ப்ட் | நோக்கம் |
| --- | --- |
| `translate_markdown_document_prompt` | உள்ளடக்க மொழிபெயர்ப்பு மற்றும் விருப்பமான பாதை மறுஎழுதலை வழிநடத்தல். |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM வழங்குநர் அங்கீகாரம் இல்லாமல் ஹோஸ்ட்-ஏஜென்ட் Markdown மொழிபெயர்ப்பை வழிநடத்தல். |
| `translate_repository_prompt` | முதலில் dry-run பின்பற்றியும் ரெப்போசிடரி மொழிபெயர்ப்பை வழிநடத்தல். |

## நகல்-ஒட்டிப் பதிவு எடுத்துக்காட்டு

Markdown உள்ளடக்கத்தை மொழிபெயர்க்கவும்:

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

மொழிபெயர்க்கப்பட்ட Markdown இணைப்புகளை மறுஎழுதுக:

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

ஹோஸ்ட் ஏஜென்ட் மாடல் பயன்படுத்தி Markdown மொழிபெயர்க்கவும்:

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

ஹோஸ்ட் ஏஜென்ட் ஒவ்வொரு திரும்பும் பகுதியையும் மொழிபெயரித்த பிறகு, `start_markdown_agent_translation` மூலம் திரும்பிய முழு `job` பொருளுடன் வேலை முடிக்கவும்:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

ரெப்போசிடரி மொழிபெயர்ப்பை முன்னோட்டம் பார்க்கவும்:

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

## பிழைதிருத்தல்

| பிரச்சினை | முயற்சி செய்ய வேண்டியது |
| --- | --- |
| MCP கிளையன்ட் `co-op-translator-mcp` ஐ கண்டுபிடிக்க முடியவில்லை. | இனிமேல் Python நிறைவை முழு பாதையை பயன்படுத்தவும் மற்றும் `["-m", "co_op_translator.mcp.server"]` மூலச் சரிபார்ப்பு கட்டமைப்பைப் பயன்படுத்து. |
| சேவையகம் பட்டியலிடப்பட்டு இருந்தாலும் மொழிபெயர்ப்பு தோல்வியடைக்கிறது. | `get_configuration_status` ஐ அழைத்து LLM வழங்குநர் கிடைப்பதை உறுதிசெய்க. |
| Azure OpenAI/OpenAI விசைகளைத் தட்டாமல் Markdown அல்லது நோட்புக் மொழிபெயர்ப்பு வேண்டும். | ஹோஸ்ட் ஏஜென்ட் பகுதிகளை மொழிபெயரிக்க `start_markdown_agent_translation` / `finish_markdown_agent_translation` அல்லது நோட்புக் இணையான கருவிகளைப் பயன்படுத்தவும். |
| படம் மொழிபெயர்ப்பு தோல்வி அடைகிறது. | Azure AI Vision மாறி மதிப்புகள் அமைக்கப்பட்டுள்ளதா என்பதை உறுதிசெய்க மற்றும் `get_configuration_status` ஐ அழிக்கவும். |
| ரெப்போசிடரி மொழிபெயர்ப்பு கோப்புகளை எழுதவில்லை. | பயனர் தெளிவான அனுமதி அளித்த பிறகு மட்டுமே `dry_run=false` மற்றும் `confirm_write=true` அமைக்கவும். |
| கிளையன்ட் கட்டமைப்பில் மாற்றங்கள் தோன்றவில்லை. | MCP கிளையன்டை மறுதொடக்கம் அல்லது மீள்நகர்த்தவும். |

## பாதுகாப்பு குறிப்பு

- MCP கருவி அழைப்புகள் ஹோஸ்ட் பயன்பாட்டினால் மாடல்-கட்டுப்படுத்தப்படுகின்றன, எனவே ரெப்போசிடரி மொழிபெயர்ப்பு இயல்பாக dry-run ஆகும்.
- முழு ரெப்போசிடரி மொழிபெயர்ப்பு பல கோப்புகளை உருவாக்க, மேம்படுத்த அல்லது நீக்கக் கூடும். `confirm_write=true` ஐ அமைக்குவதற்கு முன் தெளிவான பயனர் அனுமதியைக் கோரவும்.
- கட்டமைப்பு நிலை கருவி எப்போதும் API விசைகள், எண்ட்பாயின்ட்கள் அல்லது பிற ரகசிய மதிப்புகளை திருப்பி வைக்காது.
- பட மொழிபெயர்ப்பு base64 படம் தரவினை திருப்பி விடும். பெரிய படங்கள் பெரிய கருவி பதில்களை உருவாக்கக்கூடும்.
- Agent-assisted கருவிகள் மூல பகுதிகளையும் ப்ரொம்ப்ட்களையும் MCP ஹோஸ்ட் தளத்திற்கு வழங்குகின்றன. யாரின் ஹோஸ்ட் ஏஜென்ட் மாடலுக்கு அனுப்புவதை பயனர் வசதியாக இருக்குமெனில் மட்டும் அவைகளைப் பயன்படுத்துங்கள்.