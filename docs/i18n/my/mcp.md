# MCP ဆာဗာ

Co-op Translator တွင် agent များ၊ editor များနှင့် MCP-compatible clients များအတွက် Model Context Protocol ဆာဗာ တစ်ခု ပါဝင်သည်။

Default local setup အတွက်၊ အသုံးပြုသူများသည် သုံးစွဲသူက မိမိလက်ဖြင့် သီးခြား ဆာဗာတစ်ခုကို ကြိုးပမ်းစတင်ထားရန် မလိုပါ။ သူတို့သည် မိမိတို့၏ MCP client ကို ဖော်ပြပြီး၊ client သည် Co-op Translator ကိရိယာများလိုအပ်သည့်အခါ `co-op-translator-mcp` ကို `stdio` မှတဆင့် အလိုအလျောက် စတင်မည်။

CLI, Python API နှင့် MCP တို့ကို ကြားရွေးချယ်ရန် ရှိပါက [သင့်လုပ်ဆောင်မှုကို ရွေးချယ်ပါ](workflows.md) မှာ စတင်ပါ။

MCP ကို သုံးပါသည်ဆိုရင် agent သို့မဟုတ် editor သည် Co-op Translator ကို တိုက်ရိုက် ခေါ်ယူသင့်သည် -

| အသုံးပြုသူ ရည်ရွယ်ချက် | MCP ကိရိယာများ |
| --- | --- |
| Markdown စာရွက်စာတမ်း တစ်ခု၊ notebook သို့မဟုတ် ရုပ်ပုံ တစ်ပုံ ကို ဘာသာပြန်ရန် | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Host agent မော်ဒယ်ဖြင့် Markdown သို့မဟုတ် notebook အကြောင်းအရာကို ဘာသာပြန်ရန် | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ထွက်သော output လမ်းကြောင်းကို ရွေးချယ်ပြီးနောက် ဘာသာပြန်ထားသော Markdown သို့မဟုတ် notebook လင့်ခ်များကို ပြန်ရေးရန် | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI ကဲ့သို့ ပြည့်စုံသော repository တစ်ခုကို ဘာသာပြန်ရန် | `run_translation`, `translate_project` |
| LLM အခွင့်အရေးမလိုဘဲ ဘာသာပြန်ထားသော output ကို ပြန်လည်သုံးသပ်ရန် | `run_review` |
| တတ်နိုင်မှုများနှင့် ပတ်ဝန်းကျင် status ကို စစ်ဆေးရန် | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP ဆာဗာသည် [Python API](api.md) တွင် မှတ်တိုင်ထားသော 동일한 public Python API ကို ထုပ်ပိုးပေးသည်။ Provider-backed ကိရိယာများသည် CLI နှင့် Python API တို့တွင် အသုံးပြုထားသည့် configured providers တို့ကို အသုံးပြုသည်။ Agent-assisted ကိရိယာများသည် MCP host agent အတွက် ဘာသာပြန်ရန် chunk များကို ပြင်ဆင်ပေးပြီး၊ Co-op Translator ကို အသုံးပြု၍ အဆုံးသတ် Markdown သို့မဟုတ် notebook ကို ပြန်လည်တည်ဆောက်သည်။

## အဆင့် 1: Co-op Translator ကို ထည့်သွင်းပြီး ဖွဲ့စည်းရန်

အခွင့်အရေးရမည့် MCP client သည် အသုံးပြုမည့် Python ပတ်ဝန်းကျင်တွင် Co-op Translator ကို ထည့်သွင်းပါ။

```bash
pip install co-op-translator
```

ဒီ repository မှ local တည်ဆောက်မှုအတွက် package ကို editable mode ဖြင့် ထည့်သွင်းပါ -

```bash
pip install -e .
```

သင့် MCP client သုံးမည့် ဘာသာပြန်မှုအမျိုးအစားကို ရွေးချယ်ပါ -

| Mode | အသုံးပြုရန် | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator သည် `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, သို့မဟုတ် `run_translation` ကို ခေါ်သုံးသည်။ | Markdown နှင့် notebook ဘာသာပြန်မှုအတွက် Azure OpenAI သို့မဟုတ် OpenAI လိုအပ်သည်။ ရုပ်ပုံဘာသာပြန်မှုအတွက်လည်း Azure AI Vision လိုအပ်သည်။ |
| Agent-assisted | MCP host agent သည် `start_markdown_agent_translation` သို့မဟုတ် `start_notebook_agent_translation` ကနေ ပြန်လာတဲ့ chunks များကို ဘာသာပြန်ပေးသည်။ | Markdown သို့မဟုတ် notebook chunks များအတွက် Co-op Translator LLM provider credentials မလိုအပ်ပါ။ Image ဘာသာပြန်မှုကို agent-assisted mode သည် ထည့်သွင်းမထားသေးပါ။ |

Codex သို့ Claude Code ကဲ့သို့သော agent အတွင်း Markdown သို့မဟုတ် notebook ဘာသာပြန်မှုဖြင့် စတင်ပါက agent-assisted mode နှင့် စတင်ပါ။ Co-op Translator ကို ကိုယ်တိုင် သင့် configured providers များကို ခေါ်စေချင်သည်၊ ရုပ်ပုံများကို ဘာသာပြန်လိုသည်၊ သို့မဟုတ် CLI ကဲ့သို့ repository-level ဘာသာပြန်မှုကို ပြုလုပ်လိုပါက provider-backed mode ကို အသုံးပြုပါ။

Provider-backed workflows များအတွက်သာ provider credentials များကို သတ်မှတ်ပါ -

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed image ဘာသာပြန်မှုအတွက် ထပ်ဆင့်လိုအပ်ချက်များ -

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode သည် လောလောဆယ် Markdown နှင့် notebook Markdown cell များကိုသာ ဖုံးကွယ်ပေးသည်။ ရုပ်ပုံ ဘာသာပြန်မှုသည် ဆက်လက်၍ provider-backed image pipeline ကို အသုံးပြုသည်နှင့် OCR နှင့် layout-aware rendering များအတွက် Azure AI Vision ကို လိုအပ်သည်။

## အဆင့် 2: သင့် MCP Client ကို သတ်မှတ်ပါ

ယေဘုယျ local `stdio` ပြင်ဆင်မှုအတွက်၊ သင့် MCP client configuration ထဲသို့ Co-op Translator ကို ထည့်ပါ။ client သည် process ကို အလိုအလျောက် စတင်နှင့် ရပ်တန့်ပေးပါလိမ့်မည်။

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

MCP client configuration ပြင်ဆင်ပြင်လဲပြီးနောက်၊ client သည် ဆာဗာအသစ်ကို ရှာဖွေနိုင်ရန် client ကို restart သို့ reload လုပ်ပါ။

## အဆင့် 3: Client ထဲတွင် ဆာဗာကို အတည်ပြုပါ

အသုံးပြုသူ MCP client ကို အသုံးပြု၍ ရနိုင်သော ကိရိယာများကို စာရင်းပြရန် မေးမြန်းပါ၊ ဒါမှမဟုတ် read-only helper များထဲမှ တစ်ခုကို ပထမဦးဆုံး ခေါ်ပါ -

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

အသုံးဝင်သည့် ပထမစစ်ဆေးရန်များ -

| Tool | စစ်ဆေးရန်အချက်များ |
| --- | --- |
| `get_api_overview` | ဆာဗာကို ရောက်ရှိနိုင်ကြောင်း အတည်ပြုပြီး ရရှိနိုင်သော workflows များကို ပြသသည်။ |
| `list_supported_languages` | ရှေ့ထုပ်ပိုးထားသည့် ဘာသာစကားဒေတာများကို သွင်းနိုင်ကြောင်း အတည်ပြုသည်။ |
| `get_configuration_status` | လျှို့ဝှက်တန်ဖိုးများ ဖော်ပြခြင်းမရှိဘဲ LLM နှင့် Vision provider ရရှိနိုင်မှုကို အတည်ပြုသည်။ |

## အဆင့် 4: Workflow တစ်ခုကို ရွေးချယ်ပါ

### ဖိုင်များ သီးသန့် သို့ စာရွက်စာတမ်းများ ဘာသာပြန်ရန်

MCP client အနေဖြင့် စာရွက်စာတမ်း အကြောင်းအရာ သို့မဟုတ် image path ကို ရရှိထားပြီး Co-op Translator သည် configured translation providers ကို ခေါ်သင့်သည့်အခါ provider-backed content tools များကို အသုံးပြုပါ။

Markdown အတွက် -

1. `document`, `language_code`, နှင့် လိုအပ်ပါက `source_path` ဖြင့် `translate_markdown_content` ကို ခေါ်ပါ။
2. ဘာသာပြန်ထားသော ရလဒ်ကို Co-op Translator output layout ထဲသို့ ရေးချင်ပါက `rewrite_markdown_paths` ကို ခေါ်ပါ။
3. client သည် နောက်ဆက်တွဲ `content` ကို ရေးထုတ်ပေးမည် သို့မဟုတ် ပြန်လည်ပေးပို့မည်။

notebooks အတွက် -

1. notebook JSON နှင့် `language_code` ဖြင့် `translate_notebook_content` ကို ခေါ်ပါ။
2. ဘာသာပြန်ထားသော notebook လင့်ခ်များကို လိုအပ်သည့် target path အတွက် ပြုပြင်ရန် `rewrite_notebook_paths` ကို ခေါ်ပါ။
3. နောက်ဆုံး notebook JSON ကို ရေးထုတ် သို့မဟုတ် ပြန်လည်ပေးပို့ပါ။

ရုပ်ပုံများအတွက် -

1. `image_path`, `language_code`, နှင့် ရွေးချယ်စရာ `root_dir` သို့မဟုတ် `fast_mode` ဖြင့် `translate_image_content` ကို ခေါ်ပါ။
2. ပြန်လာသော `data_base64` နှင့် `mime_type` ကို ဖတ်ပါ။
3. `output_path` ပေးထားလျှင် ဘာသာပြန်ထားသော image ကို ထို path သို့လည်း သိမ်းဆည်းပေးသည်။

content tools များသည် project discovery, metadata updates, disclaimers, သို့မဟုတ် အလိုအလျောက် path ပြန်ရေးခြင်းများကို မဆောင်ရွက်ပါ။ Host agent သည် Co-op Translator LLM provider credentials မလိုအပ်ဘဲ Markdown သို့မဟုတ် notebook chunks များကို ဘာသာပြန်ပေးစေချင်ပါက agent-assisted workflow ကို အသုံးပြုပါ။

### Host Agent မော်ဒယ်ဖြင့် ဘာသာပြန်ရန်

Co-op Translator အတွက် Azure OpenAI သို့ OpenAI ကို ဖော်ပြရန် မလိုချင်ပဲ host agent (coding assistant ကဲ့သို့) သည် ဘာသာပြန်စာသား ထုတ်လုပ်ရန်လိုလျှင် agent-assisted ကိရိယာများကို အသုံးပြုပါ။

chat-based MCP client တစ်ခုတွင် သာမန်အားဖြင့် သင်သည် tool JSON ကို ကိုယ်တိုင် ရေးရန် မလိုအပ်ပါ။ agent ကို agent-assisted workflow ကို အသုံးပြုရန် မေးမြန်းပါ -

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

notebooks အတွက်လည်း တူညီသော ပုံစံကို အသုံးပြုပါ -

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

သင့် MCP client သည် server prompts ကို ထောက်ပံ့ပါက `agent_assisted_markdown_translation_prompt` ကို သုံး၍ client သည် 동일한 workflow instruction များကိုဖွင့်ပါစေ။

Markdown အတွက် -

1. `document`, `language_code`, နှင့် လိုအပ်ပါက `source_path` ဖြင့် `start_markdown_agent_translation` ကို ခေါ်ပါ။
2. အပြန်လာသော chunk တစ်ခုချင်းစီကို host agent တွင် chunk `prompt` အတိုင်း ဘာသာပြန်ပါ။
3. မူရင်း `job` နှင့် chunk `chunk_id` နှင့် `translated_text` များကို အသုံးပြုကာ `finish_markdown_agent_translation` ကို ခေါ်ပါ။
4. အကြောင်းအရာကို ဘာသာပြန်ထားသော target path သို့ ရေးမည်ဆိုလျှင် `rewrite_markdown_paths` ကို ခေါ်ပါ။

notebooks အတွက် -

1. notebook JSON နှင့် `language_code` ဖြင့် `start_notebook_agent_translation` ကို ခေါ်ပါ။
2. အပြန်လာသော chunk တစ်ခုချင်းစီကို host agent တွင် ဘာသာပြန်ပါ။
3. မူရင်း `job` နှင့် translated chunks များဖြင့် `finish_notebook_agent_translation` ကို ခေါ်ပါ။
4. ဘာသာပြန်ထားသော notebook လင့်ခ်များသည် target-path ပြုပြင်ခြင်း လိုအပ်လျှင် `rewrite_notebook_paths` ကို ခေါ်ပါ။

Agent-assisted ကိရိယာများသည် Co-op Translator မှ Azure OpenAI သို့ OpenAI ကို ခေါ်မည်မဟုတ်ပါ။ Host agent သည် ပြန်လာသော chunks များကို ဘာသာပြန်ပေးရန် တာဝန်ယူပါသည်။ Co-op Translator သည် Markdown chunking, placeholder သက်ဆိုင်ရာထိန်းသိမ်းမှု, frontmatter ပြန်လည်တည်ဆောက်ခြင်း, notebook cell ပြန်လဲရေးခြင်းနှင့် post-translation normalization များကို ကိုင်တွယ်ပေးပါသည်။

### ပင်လယ်သမားအစုံ repository တစ်ခုကို ဘာသာပြန်ရန်

အသုံးပြုသူက Co-op Translator ကို CLI ကဲ့သို့ အပြုအမူ ပြုရန်လိုလျှင် `run_translation` ကို အသုံးပြုပါ။

Repository ဘာသာပြန်မှုသည် agent ကို ဖိုင်ပြောင်းလဲမှုများ အကြို စစ်ဆေးစေဖို့ `dry_run=true` ကို default အဖြစ် အသုံးပြုထားသည် -

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

ရေးသားခွင့်များ လက်ခံခွင့်ပေးရန် `dry_run=false` နှင့် `confirm_write=true` နှစ်ခုလုံးကို ဖော်ပြရပါမည် -

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` သည် `run_translation` အတွက် compatibility alias အဖြစ် ထုတ်ပေးထားသည်။

### ဘာသာပြန်ထားသော Output ကို Review ပြုလုပ်ရန်

LLM သို့ Vision credentials မလိုအပ်သည့် deterministic အစစ်အငယ် စစ်ဆေးမှုများအတွက် `run_review` ကို အသုံးပြုပါ။

!!! note "Beta"
    MCP သည် beta `run_review` API ကို ထုတ်ပေးထားသည်။ ၎င်းသည် read-only review workflows များအတွက် လုံခြုံသော်လည်း review စစ်ဆေးမှုများနှင့် issue schemas များသည် ဖွံ့ဖြိုးပြောင်းလဲနိုင်သည်။

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

ရလဒ်တွင် ဖမ်းယူထားသော စာသား output နှင့် ရရှိနိုင်ပါက ဖွဲ့စည်းထားသည့် review အကျဉ်းချုပ် ပါဝင်သည်။

## လက်ဖြင့် ဆာဗာ စတင်အသုံးပြုခြင်း

လက်တွင် run မည်ဆိုပါက debugging သို့မဟုတ် long-running server ကဲ့သို့ လုပ်ဆောင်သည့် transports များအတွက် ဖြစ်သည်။

default stdio server ကို debug လုပ်ရန် -

```bash
co-op-translator-mcp
```

Source checkout မှ စတင် run မည်ဆိုပါက -

```bash
python -m co_op_translator.mcp.server
```

ရှည်လျားသော HTTP သို့ SSE ဆာဗာ run မည် -

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

local editor နှင့် agent အင်တင်ဂရেশনများအတွက် Step 2 တွင် client-managed `stdio` configuration ကို ပိုသင့်တော်သည်။

## ကိရိယာများ

| Tool | ရည်ရွယ်ချက် | ဖိုင်များ ရေးသွင်းပါသလား |
| --- | --- | --- |
| `translate_markdown_content` | Markdown string ကို ဘာသာပြန်ရန်။ | မရှိ |
| `translate_notebook_content` | notebook JSON ထဲရှိ Markdown cell များကို ဘာသာပြန်ရန်။ | မရှိ |
| `translate_image_content` | တစ်ပုံထဲရှိ စာသားကို ဘာသာပြန်ပြီး base64 image data ကို ပြန်ပေးရန်။ | ရွေးချယ်နိုင်သည်၊ `output_path` ပေးထားပါကသာ |
| `start_markdown_agent_translation` | Co-op Translator LLM provider credentials မလိုဘဲ host agent အတွက် Markdown chunks များကို ပြင်ဆင်ရန်။ | မရှိ |
| `finish_markdown_agent_translation` | host-agent ဘာသာပြန်ပြီးသော chunks များမှ Markdown ကို ပြန်လည်တည်ဆောက်ရန်။ | မရှိ |
| `start_notebook_agent_translation` | host agent အတွက် notebook Markdown-cell chunks များကို ပြင်ဆင်ရန်။ | မရှိ |
| `finish_notebook_agent_translation` | host-agent ဘာသာပြန်ပြီးသော chunks များမှ notebook JSON ကို ပြန်လည်တည်ဆောက်ရန်။ | မရှိ |
| `rewrite_markdown_paths` | ဘာသာပြန်ထားသည့် target အတွက် Markdown body နှင့် frontmatter paths ကို ပြန်ရေးရန်။ | မရှိ |
| `rewrite_notebook_paths` | notebook Markdown cell များအတွင်းရှိ paths များကို ပြန်ရေးရန်။ | မရှိ |
| `run_translation` | CLI ကဲ့သို့ project-level ဘာသာပြန်မှုကို စဉ်ဆောင်ရန်။ | `dry_run=false` နှင့် `confirm_write=true` ဖြစ်သောအချိန်တွင် ဟုတ် |
| `translate_project` | `run_translation` အတွက် compatibility alias ဖြစ်သည်။ | `dry_run=false` နှင့် `confirm_write=true` ဖြစ်သောအချိန်တွင် ဟုတ် |
| `run_review` | deterministic review စစ်ဆေးမှုများ အလုပ်လုပ်စေသည်။ | မရှိ |
| `get_configuration_status` | secret တန်ဖိုးများ မဖော်ထုတ်ဘဲ configured LLM နှင့် Vision providers များကို รายงานပေးသည်။ | မရှိ |
| `list_supported_languages` | ထောက်ပံ့ထားသည့် target language codes များကို စာရင်းပြုစုပေးသည်။ | မရှိ |
| `get_api_overview` | ရနိုင်သည့် MCP workflows နှင့် ကိရိယာများကို ရှင်းပြသည်။ | မရှိ |

## အသုံးအဆောင်များ

| Resource URI | ရည်ရွယ်ချက် |
| --- | --- |
| `co-op://api` | workflows နှင့် ကိရိယာများ၏ JSON အကျဉ်းချုပ်။ |
| `co-op://supported-languages` | ထောက်ပံ့ထားသည့် ဘာသာစကားကုဒ်များ၏ JSON စာရင်း။ |
| `co-op://configuration` | secret မဖော်ထုတ်ဘဲ provider ရရှိနိုင်မှု စုစုပေါင်း JSON အကျဉ်းချုပ်။ |

## Prompts

| Prompt | ရည်ရွယ်ချက် |
| --- | --- |
| `translate_markdown_document_prompt` | MCP client ကို content ဘာသာပြန်ခြင်းနှင့် ရွေးချယ်နိုင်သည့် path ပြန်ရေးခြင်းတို့အတွက် လမ်းညွှန်ရန်။ |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM provider credentials မလိုဘဲ host-agent Markdown ဘာသာပြန်မှုအတွက် MCP client ကို လမ်းညွှန်ရန်။ |
| `translate_repository_prompt` | dry-run အရင်ဆုံး repository ဘာသာပြန်မှုအတွက် MCP client ကို လမ်းညွှန်ရန်။ |

## ကော်ပီ-ပိတ်စ် ဥပမာများ

Markdown အကြောင်းအရာ ဘာသာပြန်ရန် -

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

ဘာသာပြန်ထားသော Markdown link များ ပြန်ရေးရန် -

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

host agent မော်ဒယ်ဖြင့် Markdown ဘာသာပြန်ရန် -

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

host agent သည် အပြန်လာသော chunk တစ်ခုချင်းစီကို ဘာသာပြန်ပြီးနောက်၊ `start_markdown_agent_translation` မှ ပြန်လာသည့် အပြည့်အစုံ `job` object ဖြင့် အလုပ်ကို ပြီးစီးပါ -

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Repository ဘာသာပြန်မှု ကို ကြည့်မည်မဆို ကြိုတင်ကြည့်ရှုရန် -

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

| ပြဿနာ | စမ်းကြည့်ရန် |
| --- | --- |
| MCP client သည် `co-op-translator-mcp` ကို မတွေ့ပါ။ | absolute Python executable path ကို အသုံးပြုပြီး `["-m", "co_op_translator.mcp.server"]` source checkout configuration ကို အသုံးပြုပါ။ |
| ဆာဗာ စာရင်းတွင် ပါသော်လည်း ဘာသာပြန်မှု မအောင်မြင်ပါ။ | `get_configuration_status` ကို ခေါ်၍ LLM provider ရရှိနိုင်ကြောင်း အတည်ပြုပါ။ |
| Azure OpenAI/OpenAI Keys မလိုဘဲ Markdown သို့မဟုတ် notebook ဘာသာပြန်ချင်သည်။ | `start_markdown_agent_translation` / `finish_markdown_agent_translation` သို့မဟုတ် notebook နှင့်သက်ဆိုင်သော အမျိုးအစားများကို အသုံးပြု၍ host agent သည် chunks များကို ဘာသာပြန်ပေးစေပါ။ |
| ရုပ်ပုံ ဘာသာပြန်မှု မအောင်မြင်ပါ။ | Azure AI Vision အပြောင်းအလဲများကို သတ်မှတ်ထားကြောင်း အတည်ပြု၍ `get_configuration_status` ကို ခေါ်ပါ။ |
| Repository ဘာသာပြန်မှုသည် ဖိုင်များကို မရေးသေးပါ။ | user ၏ ထောက်ခံချက်ရရှိပြီးမှသာ `dry_run=false` နှင့် `confirm_write=true` ကို သတ်မှတ်ပါ။ |
| client config တွင် ပြင်ဆင်မှုများ ပြသမည်မဟုတ်။ | MCP client ကို restart သို့ reload လုပ်ပါ။ |

## လုံခြုံရေး မှတ်စုများ

- MCP tool ခေါ်ဆိုမှုများကို host application ၏ မော်ဒယ်က ထိန်းချုပ်နေသောကြောင့် repository ဘာသာပြန်မှုသည် default အဖြစ် dry-run ဖြစ်သည်။
- အပြည့်အစုံ repository ဘာသာပြန်မှုမှ ဖိုင်များ များစွာကို ဖန်တီး၊ အပ်ဒိတ် သို့မဟုတ် ဖျက်ပေးနိုင်သည်။ `confirm_write=true` သတ်မှတ်ရန်မပြုမီ အသုံးပြုသူ၏ ထောက်ခံချက်ကို လိုအပ်သည်။
- configuration status tool သည် API keys၊ endpoints သို့မဟုတ် အခြား secret တန်ဖိုးများကို မပြန်ပေးပါ။
- ရုပ်ပုံ ဘာသာပြန်မှုသည် base64 image data ကို ပြန်ပေးသည်။ အကြီးစား image များသည် tool response များကို ကြီးထွားစေနိုင်သည်။
- Agent-assisted ကိရိယာများသည် source chunks နှင့် prompts များကို MCP host သို့ ပြန်ပို့ပေးသည်။ ၎င်းကို user သည် host agent မော်ဒယ်ထံတွင် ပို့ရန် အဆင်ပြေသည့် အကြောင်းအရာများနှင့်သာ အသုံးပြုပါ။