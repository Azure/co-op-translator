# MCP ဆာဗာ

Co-op Translator တွင် agent များ၊ editor များနှင့် MCP-ကိုက်ညီသော client များအတွက် Model Context Protocol ဆာဗာ တစ်ခု ပါဝင်သည်။

မူလ ဒေသအဆင်သင့် တပ်ဆင်မှုအတွက်၊ အသုံးပြုသူများသည် သီးခြား ဆာဗာကို ကိုယ့်လက်ဖြင့် အလုပ်မလည်ဖြစ်စေပါ။ သူတို့သည် သူတို့၏ MCP client ကို ဖွဲ့စည်းပြီး client သည် Co-op Translator tools မလိုအပ်သည့်အခါ `stdio` မှတဆင့် `co-op-translator-mcp` ကို အလိုအလျောက် စတင်လည်ပတ်စေပါလိမ့်မည်။

CLI၊ Python API နှင့် MCP အတွင်း ရွေးချယ်ရန်ရှိပါက [သင့်လုပ်ငန်းစဉ်ကို ရွေးချယ်ပါ](workflows.md) ကနေ စတင်ပါ။

agent သို့ editor တစ်ခုက Co-op Translator ကို တိုက်ရိုက် ခေါ်သင့်လျှင် MCP ကို အသုံးပြုပါ။

| အသုံးပြုသူ ရည်မှန်းချက် | MCP ကိရိယာများ |
| --- | --- |
| Markdown စာရွက်စာတမ်း တစ်ခု၊ notebook သို့မဟုတ် ဓာတ်ပုံ တစ်ပုံကို ဘာသာပြန်ရန် | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Host agent မော်ဒယ်ဖြင့် Markdown သို့မဟုတ် notebook အကြောင်းအရာ ဘာသာပြန်ရန် | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ထွက်မည့်လမ်းကြောင်းကို ရွေးချယ်ပြီးနောက် ဘာသာပြန်ထားသော Markdown သို့မဟုတ် notebook လင့်ခ်များကို ပြန်ရေးရန် | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI ကဲ့သို့ ပြုလုပ်သည့် ပရိုကျက်တစ်ခုလုံးကို ဘာသာပြန်ရန် | `run_translation`, `translate_project` |
| LLM အချက်အလက် မလိုအပ်ဘဲ ဘာသာပြန်ပြီး output ကို ပြန်လည်သုံးသပ်ရန် | `run_review` |
| စွမ်းရည်များနှင့် ပတ်ဝန်းကျင်အခြေအနေကို ကြည့်ရှုစစ်ဆေးရန် | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP ဆာဗာသည် [Python API](api.md) တွင် မှတ်တမ်းတင်ထားသည့် တူညီသော public Python API ကို ဖုံးလွှမ်းသည်။ Provider-backed ကိရိယာများသည် CLI နှင့် Python API နှင့်တူညီသည့် ပြင်ဆင်ထားသော provider များကို အသုံးပြုသည်။ Agent-assisted ကိရိယာများသည် MCP host agent အတွက် ဘာသာပြန်ရန် chunk များကို ပြင်ဆင်ပြီး Co-op Translator ကို အသုံးပြုကာ နောက်ဆုံး Markdown သို့မဟုတ် notebook ကို ပြန်လည်တည်ဆောက်သည်။

## ခြေလှမ်း ၁: Co-op Translator ကို တပ်ဆင်ပြီး ဖွဲ့စည်းပါ

သင့် MCP client သုံးမည့် Python ပတ်ဝန်းကျင်တွင် Co-op Translator ကို တပ်ဆင်ပါ:

```bash
pip install co-op-translator
```

ဒေသတွင်း ဖွံ့ဖြိုးရေးအတွက် ဤ repository မှ package ကို editable mode ဖြင့် တပ်ဆင်ပါ:

```bash
pip install -e .
```

သင့် MCP client သုံးမည့် ဘာသာပြန်မှု မုဒ်ကို ရွေးချယ်ပါ။

| မုဒ် | အသုံးပြုရန် | အတည်ပြုချက်များ |
| --- | --- | --- |
| Provider-ထောက်ပံ့ | Co-op Translator သည် `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, သို့မဟုတ် `run_translation` ကို ခေါ်ယူသည်။ | ဘာသာပြန်မှုအတွက် Azure OpenAI၊ OpenAI သို့မဟုတ် Anthropic လိုအပ်သည်။ ဓာတ်ပုံ ဘာသာပြန်မှုအတွက် Azure AI Vision လည်း လိုအပ်သည်။ |
| Agent-assisted | MCP host agent သည် `start_markdown_agent_translation` သို့မဟုတ် `start_notebook_agent_translation` မှ ပြန်လာသော chunk များကို ဘာသာပြန်သည်။ | Markdown သို့ Notebook chunk များအတွက် Co-op Translator LLM provider အတည်ပြုချက် မလိုအပ်ပါ။ ဓာတ်ပုံ ဘာသာပြန်မှုကို agent-assisted မုဒ်တွင် မပါသေးပါ။ |

Codex သို့ Claude Code ကဲ့သို့ agent အတွင်း Markdown သို့ Notebook ဘာသာပြန်မှုကို စတင်ပါက agent-assisted မုဒ်ဖြင့် စတင်ပါ။ Co-op Translator ကို ကိုယ်တိုင် သင့်ပြင်ဆင်ထားသည့် provider များကို ခေါ်စေလိုသောအခါ၊ ဓာတ်ပုံများကို ဘာသာပြန်နေချိန်တွင် သို့မဟုတ် CLI ကဲ့သို့ repository-အဆင့် ဘာသာပြန်မှုများကို ပြုလုပ်ချိန်တွင် provider-backed မုဒ်ကို အသုံးပြုပါ။

Provider-backed workflows များအတွက် provider တစ်ခုကို ဖွဲ့စည်းပါ။

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# သို့မဟုတ် OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# သို့မဟုတ် Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Provider-backed ဓာတ်ပုံ ဘာသာပြန်မှုအတွက် ထပ်ဆောင်းလိုအပ်ချက်များ:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted မုဒ်သည် ယခုအခါ Markdown နှင့် notebook ၏ Markdown cell များကိုသာ ဖုံးလွှမ်းထားသည်။ ဓာတ်ပုံ ဘာသာပြန်မှုမှာ provider-backed image pipeline ကို အသုံးပြုထားပြီး OCR နှင့် layout-aware rendering အတွက် Azure AI Vision လိုအပ်သည်။

## ခြေလှမ်း ၂: သင့် MCP Client ကို ဖော်ဆောင်ပါ

ပုံမှန် ဒေသတွင်း `stdio` စီစဉ်မှုအတွက် Co-op Translator ကို သင့် MCP client configuration ထဲသို့ ထည့်ပါ။ client က အဆိုပါ process ကို အလိုအလျောက် စတင်/ပိတ်ပါလိမ့်မည်။

တပ်ဆင်ထားသည့် package အတွက် configuration:

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

Windows အတွက် source checkout configuration:

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

macOS သို့ Linux အတွက် source checkout configuration:

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

MCP client configuration ပြင်ဆင်ပြီးနောက် client ကို ပြန်စတင် သို့မဟုတ် reload ပြုလုပ်ပါ၊ ထို့ဖြင့် အသစ်သော ဆာဗာကို ရှာဖွေနိုင်မည်။

## ခြေလှမ်း ၃: Client တွင် ဆာဗာကို အတည်ပြုပါ

MCP client ကို အသုံးပြုနိုင်သော ကိရိယာများ စာရင်းပြပါစေ၊ သို့မဟုတ် ပထမဦးစွာ read-only helper များထဲမှ တစ်ခုကို ခေါ်ပါ။

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

အသုံးဝင်သော စစ်ဆေးမှုများ:

| ကိရိယာ | စစ်ဆေးရန်အချက်များ |
| --- | --- |
| `get_api_overview` | ဆာဗာကို ဆက်သွယ်နိုင်ကြောင်း အတည်ပြုပြီး အသုံးပြုနိုင်သည့် workflow များကို ပြသသည်။ |
| `list_supported_languages` | ထုပ်ပိုးထားသော ဘာသာစကားဒေတာများကို စတင်ဖတ်ယူနိုင်ကြောင်း အတည်ပြုသည်။ |
| `get_configuration_status` | လျှို့ဝှက်တန်ဖိုးများ မဖော်ထုတ်ဘဲ LLM နှင့် Vision provider များ ရရှိနိုင်ကြောင်း အတည်ပြုသည်။ |

## ခြေလှမ်း ၄: လုပ်ငန်းစဉ်ကို ရွေးချယ်ပါ

### တစ်ခုချင်း ဖိုင်များ သို့ စာရွက်စာတမ်းများ ဘာသာပြန်ရန်

MCP client တွင် စာရွက်စာတမ်း အကြောင်းအရာ သို့မဟုတ် ဓာတ်ပုံ လမ်းကြောင်း ရှိပြီး Co-op Translator က သတ်မှတ်ထားသော translation provider များကို ခေါ်စေလိုပါက provider-backed content tools များကို အသုံးပြုပါ။

Markdown အတွက်:

1. `document`, `language_code` နှင့် လိုအပ်ပါက `source_path` ဖြင့် `translate_markdown_content` ကို ခေါ်ပါ။
2. ဘာသာပြန်ပြီးသော ရလဒ်ကို Co-op Translator output layout တစ်ခုထဲသို့ ရေးရန် ရှိပါက `rewrite_markdown_paths` ကို ခေါ်ပါ။
3. client ကို နောက်ဆုံး `content` ကို ရေးစရာ သို့မဟုတ် ပြန်အပ်ရန် ခွင့်ပြုပါ။

notebook များအတွက်:

1. notebook JSON နှင့် `language_code` ဖြင့် `translate_notebook_content` ကို ခေါ်ပါ။
2. ဘာသာပြန်ထားသော notebook လင့်ခ်များကို ပစ်မှတ် လမ်းကြောင်းအတွက် ချိန်ညှိရန် လိုအပ်ပါက `rewrite_notebook_paths` ကို ခေါ်ပါ။
3. နောက်ဆုံး notebook JSON ကို ရေးထား သို့မဟုတ် ပြန်အပ်ပါ။

ဓာတ်ပုံများအတွက်:

1. `image_path`, `language_code` နှင့် လိုအပ်ပါက `root_dir` သို့မဟုတ် `fast_mode` ဖြင့် `translate_image_content` ကို ခေါ်ပါ။
2. ပြန်လာသော `data_base64` နှင့် `mime_type` ကို ဖတ်ပါ။
3. `output_path` ပေးထားပါက ဘာသာပြန်ထားသော ဓာတ်ပုံကို ထိုလမ်းကြောင်းတွင်လည်း သိမ်းဆည်းမည်။

content tools များသည် project discovery၊ metadata အပ်ဒိတ်များ၊ အာမခံချက်များ သို့မဟုတ် လမ်းကြောင်းကို အလိုအလျောက် ပြန်ရေးခြင်းများကို မပြုလုပ်ပါ။ Co-op Translator LLM provider အတည်ပြုချက်များ မလိုဘဲ host agent ကို Markdown သို့ notebook chunk များ ဘာသာပြန်စေလိုပါက အောက်ပါ agent-assisted workflow ကို အသုံးပြုပါ။

### Host Agent မော်ဒယ်ဖြင့် ဘာသာပြန်ခြင်း

Co-op Translator အတွက် LLM provider ကို ဖွဲ့စည်းရန် မလိုချင်ဘဲ coding assistant ကဲ့သို့ MCP host agent ကို ဘာသာပြန်စာ ထုတ်ပေးစေလိုပါက agent-assisted ကိရိယာများကို အသုံးပြုပါ။

chat-based MCP client တွင် ပုံမှန်အားဖြင့် သင်ကိုယ်တိုင် tool JSON ကို ရေးရန် မလိုအပ်ပါ။ agent ကို agent-assisted workflow ကို အသုံးပြုစေလိုက်ပါ။

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

notebook များအတွက်လည်း တူညီသော ပုံစံကို အသုံးပြုပါ:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

သင့် MCP client က server prompts ကို ထောက်ပံ့ပါက `agent_assisted_markdown_translation_prompt` ကို အသုံးပြုပြီး client ကို တူညီသော workflow ညွှန်ကြားချက်များကို load စေပါ။

Markdown အတွက်:

1. `document`, `language_code` နှင့် လိုအပ်ပါက `source_path` ဖြင့် `start_markdown_agent_translation` ကို ခေါ်ပါ။
2. ပြန်လာသော chunk တစ်ခုချင်းစီကို host agent ထဲတွင် chunk ရဲ့ `prompt` အတိုင်းလိုက်နာ၍ ဘာသာပြန်ပါ။
3. မူလ `job` နှင့် ဘာသာပြန်ပြီးသော chunks များကို `chunk_id` နှင့် `translated_text` အသုံးပြုပြီး `finish_markdown_agent_translation` ကို ခေါ်ပါ။
4. အကြောင်းအရာကို ဘာသာပြန်ထားသည့် ထိပ်တန်း လမ်းကြောင်းသို့ ရေးမည်ဆိုပါက `rewrite_markdown_paths` ကို ခေါ်ပါ။

notebook များအတွက်:

1. notebook JSON နှင့် `language_code` ဖြင့် `start_notebook_agent_translation` ကို ခေါ်ပါ။
2. ပြန်လာသော chunk တိုင်းကို host agent တွင် ဘာသာပြန်ပါ။
3. မူလ `job` နှင့် ဘာသာပြန်ပြီးသော chunks များဖြင့် `finish_notebook_agent_translation` ကို ခေါ်ပါ။
4. ဘာသာပြန်ထားသော notebook link များကို target-path ချိန်ညှိရန် လိုအပ်ပါက `rewrite_notebook_paths` ကို ခေါ်ပါ။

Agent-assisted tools များသည် Co-op Translator ထဲမှ ပြင်ဆင်ထားသည့် LLM provider ကို ခေါ်မည် မဟုတ်ပါ။ ပြန်လာသော chunks များကို ဘာသာပြန်ရန်တာဝန်ရှိသည်မှာ host agent ဖြစ်သည်။ Co-op Translator သည် Markdown chunking၊ placeholder ထိန်းသိမ်းခြင်း၊ frontmatter ပြန်လည်တည်ဆောက်ခြင်း၊ notebook cell အစားထိုးခြင်းနှင့် ဘာသာပြန်ပြီးနောက် စံနှုန်းပြုလုပ်ခြင်းတို့ကို ကိုင်တွယ်ပေးသည်။

### စုစုပေါင်း Repository တစ်ခုကို ဘာသာပြန်ရန်

အသုံးပြုသူသည် Co-op Translator ကို `translate` CLI ကဲ့သို့ လုပ်ဆောင်စေလိုပါက `run_translation` ကို အသုံးပြုပါ။

Repository ဘာသာပြန်မှုအတွက် မူရင်းအားဖြင့် `dry_run=true` သတ်မှတ်ထားပါသည်၊ ထို့ကြောင့် agent သည် ဖိုင်ပြောင်းလဲမှု မပြုမီ scope ကို စစ်ဆေးနိုင်သည်။

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

`run_translation` ရလဒ်တွင် versioned ဖြစ်သော `events` အစု(array) ပါဝင်သည်
`co-op.translation.event.v1` progress events များပါရှိသည်။ MCP client များသည် အတိအကျ
`type`, `stage_key`, `completed`, `total`, နှင့် `current_path` ကဲ့သို့သော field များကို အသုံးပြုသင့်ပြီး
captured console စာသားကို ဖတ်ပြန်ခြင်းအား အစား မသုံးသင့်ပါ။ `json_events_path` ကို ပေးပါက အဆိုပါ events များကိုလည်း
NDJSON ဖိုင်ထဲသို့ ရေးသွင်းနိုင်ပါသည်။

ရေးသားခွင့်များ သတ်မှတ်ရန် caller သည် `dry_run=false` နှင့် `confirm_write=true` နှစ်ခုလုံးကို သတ်မှတ်ထားရမည်။

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` ကို `run_translation` အတွက် compatibility alias အဖြစ် ထုတ်ပေးထားသည်။

### ဘာသာပြန်ပြီး ထုတ်လွှင့်ချက်ကို ပြန်လည်သုံးသပ်ရန်

LLM သို့ Vision အတည်ပြုချက် မလိုအပ်သည့် သတ်မှတ်နိုင်သည့် စစ်ဆေးချက်များအတွက် `run_review` ကို အသုံးပြုပါ။

!!! note "Beta"
    MCP သည် beta အဆင့်ရှိသည့် `run_review` API ကို ထုတ်ပြသထားသည်။ ၎င်းသည် read-only ပြန်လည်သုံးသပ်မှုလုပ်ငန်းစဉ်များအတွက် ဘေးကင်း သောဖြစ်ပါသည်၊ သို့သော် review စစ်ဆေးချက်များနှင့် issue schema များသည် အပြောင်းအလဲရှိနိုင်သည်။

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

ရလဒ်တွင် ဖမ်းယူထားသည့် စာသား output နှင့် ရနိုင်ပါက ဖွဲ့စည်းထားသည့် review အကျဉ်းချုပ် ပါဝင်သည်။

## လက်ဖြင့် ဆာဗာ ပြေးပွဲများ

လက်ဖြင့် ပြေးခြင်းများသည် အဓိကအားဖြင့် debugging အတွက် သို့မဟုတ် ရေရှည်လည်ပတ်သည့် ဆာဗာသဘောအတိုင်း အပြန်အလှန် ဆောင်ရွက်သည့် transports များအတွက် ဖြစ်သည်။

ဒေဖော်လ် `stdio` ဆာဗာကို debugging ပြုရန်:

```bash
co-op-translator-mcp
```

source checkout မှ run ပြရန်:

```bash
python -m co_op_translator.mcp.server
```

ရေရှည်လည်ပတ်နိုင်သော HTTP သို့ SSE ဆာဗာကို ပြေးရန်:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

ဒေသတွင်း editor နှင့် agent ပေါင်းစည်းမှုများအတွက် ခြေလှမ်း ၂ တွင် ဖော်ပြထားသည့် client-managed `stdio` configuration ကို ဦးစားပေး အသုံးပြုပါ။

## ကိရိယာများ

| ကိရိယာ | ရည်ရွယ်ချက် | ဖိုင်များကို ရေးသလား |
| --- | --- | --- |
| `translate_markdown_content` | Markdown string ကို ဘာသာပြန်ရန်။ | No |
| `translate_notebook_content` | notebook JSON ထဲရှိ Markdown cell များကို ဘာသာပြန်ရန်။ | No |
| `translate_image_content` | တစ်ပုံလျှင် ရှိသော စာသားကို ဘာသာပြန်ပြီး base64 image data ကို ပြန်ပေးသည်။ | ရွေးချယ်နိုင်ပါသည်၊ `output_path` ကို ပေးထားသောအခါတွင်ပင် |
| `start_markdown_agent_translation` | Co-op Translator LLM credential မလိုဘဲ host agent ကို ဘာသာပြန်စေမည့် Markdown chunk များကို ပြင်ဆင်ရန်။ | No |
| `finish_markdown_agent_translation` | host-agent ဘာသာပြန်ပြီးသော chunks မှ Markdown ကို ပြန်လည်တည်ဆောက်ရန်။ | No |
| `start_notebook_agent_translation` | notebook ထဲရှိ Markdown-cell chunks များကို host agent သည် ဘာသာပြန်နိုင်ရန် ပြင်ဆင်ရန်။ | No |
| `finish_notebook_agent_translation` | host-agent ဘာသာပြန်ပြီးသော chunks များမှ notebook JSON ကို ပြန်လည်တည်ဆောက်ရန်။ | No |
| `rewrite_markdown_paths` | ဘာသာပြန်ထားသော ပစ်မှတ်အတွက် Markdown body နှင့် frontmatter အတွင်း လမ်းကြောင်းများကို ပြန်ရေးရန်။ | No |
| `rewrite_notebook_paths` | notebook ထဲရှိ Markdown cell များအတွင်း လမ်းကြောင်းများကို ပြန်ရေးရန်။ | No |
| `run_translation` | CLI ကဲ့သို့ project-အဆင့် ဘာသာပြန်မှုကို လုပ်ဆောင်ရန်။ | ဟုတ်သည် (`dry_run=false` နှင့် `confirm_write=true` ဖြစ်သောအခါ) |
| `translate_project` | `run_translation` အတွက် compatibility alias ဖြစ်သည်။ | ဟုတ်သည် (`dry_run=false` နှင့် `confirm_write=true` ဖြစ်သောအခါ) |
| `run_review` | သတ်မှတ်နိုင်သည့် ပြန်လည်သုံးသပ် စစ်ဆေးမှုများကို ပြေးရန်။ | No |
| `get_configuration_status` | လျှို့ဝှက်တန်ဖိုးများ မဖော်ထုတ်ဘဲ ပြင်ဆင်ထားသည့် LLM နှင့် Vision provider များ၏ ရရှိနိုင်မှုကို ပုံဖော်ပေးသည်။ | No |
| `list_supported_languages` | ထောက်ပံ့ထားသည့် ပစ်မှတ် ဘာသာစကား code များကို စာရင်းပြုစုပြပါ။ | No |
| `get_api_overview` | အသုံးပြုနိုင်သော MCP workflows နှင့် ကိရိယာများကို ဖော်ပြရန်။ | No |

## အရင်းအမြစ်များ

| Resource URI | ရည်ရွယ်ချက် |
| --- | --- |
| `co-op://api` | workflows နှင့် ကိရိယာများ၏ JSON အကျဉ်းချုပ်။ |
| `co-op://supported-languages` | ထောက်ပံ့ထားသည့် ဘာသာစကား code များ၏ JSON စာရင်း။ |
| `co-op://configuration` | လျှို့ဝှက်ချက်များ မပါဘဲ provider ရရှိနိုင်မှု အကျဉ်းချုပ် JSON။ |

## Prompt များ

| Prompt | ရည်ရွယ်ချက် |
| --- | --- |
| `translate_markdown_document_prompt` | MCP client ကို အကြောင်းအရာ ဘာသာပြန်ခြင်းနှင့် ရွေးချယ်နိုင်သည့် လမ်းကြောင်း ပြန်ရေးခြင်းတို့ဖြင့် ဦးတည်ညွှန်ကြားရန်။ |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM provider အတည်ပြုချက် မလိုဘဲ host-agent မှ Markdown ကို ဘာသာပြန်စေခြင်းအတွက် MCP client ကို ဦးတည်ညွှန်ကြားရန်။ |
| `translate_repository_prompt` | dry-run ကို မူလထားသော repository ဘာသာပြန်ခြင်းအတွက် MCP client ကို ဦးတည်ညွှန်ကြားရန်။ |

## ကော်ပီ-ပိတ် ဥပမာများ

Markdown အကြောင်းအရာ ဘာသာပြန်ရန်:

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

ဘာသာပြန်ပြီးသား Markdown link များကို ပြန်ရေးရန်:

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

Host agent မော်ဒယ်ဖြင့် Markdown ကို ဘာသာပြန်ရန်:

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

host agent သည် ပြန်လာသော မည်သည့် chunk ကိုမဆို ဘာသာပြန်ပြီးနောက် `start_markdown_agent_translation` မှ ပြန်လာသည့် ပြည့်စုံသော `job` object ဖြင့် အလုပ်ကို ပြီးစီးပါ။

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

repository ဘာသာပြန်မှုကို ကြိုကြည့်ရန်:

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

## ပြဿနာဖြေရှင်းခြင်း

| ပြဿနာ | ကြိုးစားစမ်းသပ်ရန် |
| --- | --- |
| MCP client သည် `co-op-translator-mcp` ကို ရှာမတွေ့ပါ။ | absolute Python executable path နှင့် `["-m", "co_op_translator.mcp.server"]` source checkout configuration ကို အသုံးပြုပါ။ |
| ဆာဗာကို စာရင်းပြထားသော်လည်း ဘာသာပြန်မှု မအောင်မြင်ပါ။ | `get_configuration_status` ကို ခေါ်ပြီး LLM provider ရရှိနိုင်မှုကို အတည်ပြုပါ။ |
| Provider credential မရှိဘဲ Markdown သို့ notebook ဘာသာပြန်ချင်သည်။ | `start_markdown_agent_translation` / `finish_markdown_agent_translation` သို့မဟုတ် notebook ညီမျှသော ကိရိယာများကို အသုံးပြုပြီး host agent ကို chunks များ ဘာသာပြန်စေပါ။ |
| ဓာတ်ပုံ ဘာသာပြန်မှု မအောင်မြင်ပါ။ | Azure AI Vision ပြောင်းလဲမှုများကို သတ်မှတ်ထားကြောင်း အတည်ပြုပြီး `get_configuration_status` ကို ခေါ်ပါ။ |
| Repository ဘာသာပြန်မှုသည် ဖိုင်များကို မရေးပါ။ | `dry_run=false` နှင့် `confirm_write=true` ကို အသုံးပြုမှသာ user ၏ ထောက်ခံချက် ရရှိပြီးနောက် သတ်မှတ်ပါ။ |
| client configuration အပြောင်းအလဲများ မပြပါ။ | MCP client ကို ပြန်စတင် သို့မဟုတ် reload ပြုလုပ်ပါ။ |

## လုံခြုံရေး မှတ်စုများ

- MCP tool ခေါ်ဆိုမှုများကို host application မှ မော်ဒယ်ဖြင့် ထိန်းချုပ်လျက်ရှိသည်၊ ထို့ကြောင့် repository ဘာသာပြန်မှုသည် မူရင်းအားဖြင့် dry-run ဖြစ်သည်။
- စုစုပေါင်း repository ဘာသာပြန်မှုသည် ဖိုင်များ အများအပြားကို ဖန်တီး၊ အပ်ဒိတ် သို့ ဖျက်ပစ်နိုင်သည်။ `confirm_write=true` ကို သတ်မှတ်ရန်မတိုင်မီ အသုံးပြုသူ၏ ထောက်ခံချက်ကို ရယူပါ။
- configuration status ကိရိယာသည် API keys၊ endpoints သို့မဟုတ် အခြားလျှို့ဝှက်တန်ဖိုးများကို မပြန်ပေးပါ။
- ဓာတ်ပုံ ဘာသာပြန်မှုသည် base64 image data ကို ပြန်ပေးသည်။ အကြီးစား ဓာတ်ပုံများသည် ကြီးမားသော ကိရိယာ တုံ့ပြန်မှုများ ဖြစ်စေနိုင်သည်။
- Agent-assisted tools များသည် source chunks နှင့် prompt များကို MCP host ထံပြန်ပို့သည်။ ထို host agent မော်ဒယ်သို့ ပို့ပေးရန်အသုံးပြုသူ အဆင်ပြေသည့် အကြောင်းအရာများနှင့် မျှသာ အသုံးပြုပါ။