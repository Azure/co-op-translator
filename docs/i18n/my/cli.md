# CLI ကိုးကားချက်

Co-op Translator သည် အောက်ပါ command-line entry points များကို ထည့်သွင်းသည်။

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`, `evaluate`, `migrate-links` နှင့် `co-op-review` အမိန့်များကို `co_op_translator.__main__` မှတဆင့် ပို့သွားပြီး၊ ၎င်းသည် ခေါ်လိုက်သော script အမည်အပေါ် မူတည်၍ command implementation ကို ရွေးချယ်ပေးသည်။ MCP ဆာဗာသည် တိုက်ရိုက် `co_op_translator.mcp.server` ကို အသုံးပြုသည်။

CLI, Python API, နှင့် MCP အကြား ရွေးချယ်ရန် ဆုံးဖြတ်နေပါက၊ [သင်၏ လုပ်ငန်းစဉ်ကို ရွေးချယ်ပါ](workflows.md) မှ စတင်ပါ။

## ကွန်ဆောလ် အထွက်

Interactive terminals များတွင် command header, progress, နှင့် summaries များအတွက် Rich formatting ကို အသုံးပြုသည်။ CI နှင့် non-interactive အထွက်များသည် အလိုအလျောက် plain text သို့ ပြန်သွားပါသည်။

`CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` ကို သတ်မှတ်၍ plain output ကို အတင်းအကျပ် ပြပါ၊ သို့မဟုတ် `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` ကို သတ်မှတ်၍ Rich output ကို အတင်းအကျပ် ပြပါ။ Live progress bars များကို ပိတ်ထားပြီး summaries များကို ထိန်းသိမ်းရန် `CO_OP_TRANSLATOR_NO_PROGRESS=1` ကို သတ်မှတ်ပါ။

`translate --json-events progress.ndjson` ကို တခြားစနစ်တစ်ခုမှ လိုအပ်သောအခါ အသုံးပြုပါ
စက်ဖြင့် ဖတ်နိုင်သည့် တိုးတက်မှု အချက်အလက်များအတွက်။ CLI သည် လူကို ဦးတည်သော output ကို ဆက်လက် ဖော်ပြနေပါသည်၊
NDJSON ဖိုင်သည် ဗားရှင်းထည့်ထားသော `co-op.translation.event.v1` ဖြစ်ရပ်များကို လက်ခံရရှိပြီး
`type`, `stage_key`, `completed`, `total` နှင့် တို့ကဲ့သို့သော တည်ငြိမ်သော ကော်လံများ ပါရှိပါသည်၊
`current_path`။

## ပထမဆုံး CLI လည်ပတ်မှု

terminal မှ Co-op Translator ကို အသုံးပြုပါက ဒီနေရာမှ စတင်ပါ။

1. LLM provider ကို [Configuration](configuration.md) တွင် ဖော်ပြထားသည့်အတိုင်း ဖွဲ့စည်းပါ။
2. ဘာသာပြန်လိုသည့် အကြောင်းအရာ အမျိုးအစားကို ရွေးချယ်ပါ။
3. Markdown-only ဘာသာပြန်ကဲ့သို့ အာရုံစိုက်ထားသော command ကို အရင် လည်ပတ်ပါ။
4. repository ကို ကြီးမားစွာ ပြောင်းလဲမည့် မိတ္တူများမလုပ်မီ `--dry-run` ကို အသုံးပြုပါ။
5. ဘာသာပြန်ပြီးနောက် ဖွဲ့စည်းမှုနှင့် လက်ရှိပြင်ဆင်မှုများကို စစ်ဆေးရန် `co-op-review` ကို အသုံးပြုပါ။

| ရည်ရွယ်ချက် | စတင်ရန် command |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| MCP client သို့ tools များကို ဖော်ပြပါ | CLI command များကို တိုက်ရိုက် အသုံးမပြုဘဲ [MCP Server](mcp.md) ကို ပြင်ဆင်ပါ။ |

## translate

Markdown ဖိုင်များ၊ notebook များနှင့် ပုံထဲရှိ စာသားများကို တစ်ခု သို့မဟုတ် အများအပြား ရည်မှန်းဘာသာစကားများသို့ ဘာသာပြန်ပါ။

```bash
translate -l "ko ja fr"
```

### သာမန် ဥပမာများ

Translate only Markdown:

```bash
translate -l "de" -md
```

Translate only notebooks:

```bash
translate -l "zh-CN" -nb
```

Translate Markdown and images:

```bash
translate -l "pt-BR" -md -img
```

လက်ရှိ ဘာသာပြန်များကို ဖျက်ပြီး ပြန်ဖန်တီးခြင်းဖြင့် အပ်ဒိတ်လုပ်ပါ။

```bash
translate -l "ko" -u
```

Run without interactive prompts:

```bash
translate -l "ko ja" -md -y
```

Save logs:

```bash
translate -l "ko" -s
```

Write structured progress events:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### ရွေးချယ်စရာများ

| Option | လိုအပ်ပါသလား | ဖော်ပြချက် |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | space ဖြင့် ခွဲထားသော language codes များ၊ ဥပမာ `"es fr de"`, သို့မဟုတ် `"all"`။ |
| `-r`, `--root-dir` | No | Project root။ မပေးပါက လက်ရှိ directory ကို သတ်မှတ်သည်။ |
| `-u`, `--update` | No | ရွေးချယ်ထားသည့် ဘာသာစကားများအတွက် လက်ရှိ ဘာသာပြန်ချက်များကို ဖျက်ပြီး ထပ်မံ ဖန်တီးပေးပါ။ |
| `-img`, `--images` | No | ဓာတ်ပုံ/ပုံဖိုင်များကိုသာ ဘာသာပြန်မည်။ |
| `-md`, `--markdown` | No | Markdown ဖိုင်များကိုသာ ဘာသာပြန်မည်။ |
| `-nb`, `--notebook` | No | Jupyter notebook ဖိုင်များကိုသာ ဘာသာပြန်မည်။ |
| `-d`, `--debug` | No | ကွန်ဆောလ်တွင် debug logging ကို ဖွင့်မည်။ |
| `-s`, `--save-logs` | No | DEBUG-level logs များကို `<root-dir>/logs/` အောက်တွင် သိမ်းမည်။ |
| `--json-events` | No | machine-readable translation progress events များကို NDJSON အဖြစ် ရေးသွင်းမည်။ |
| `-x`, `--fix` | No | ယခင် အကဲဖြတ်ရလဒ်များအပေါ် မူတည်၍ ယုံကြည်မှုနည်းသော Markdown ဖိုင်များကို ထပ်မံ ဘာသာပြန်မည်။ |
| `-c`, `--min-confidence` | No | `--fix` အတွက် ယုံကြည်မှု အနိမ့်ဆုံး သတ်မှတ်ချက်။ မပေးပါက `0.7` ဖြစ်သည်။ |
| `--add-disclaimer`, `--no-disclaimer` | No | machine translation disclaimers များကို ထည့်သွင်းမည် သို့မဟုတ် ဖျောက်ပယ်မည်။ CLI တွင် မပေးပါက အလိုအလျောက် ဖွင့်ထားသည်။ |
| `-f`, `--fast` | No | အသုံးမပြုတော့သော fast image mode။ |
| `-y`, `--yes` | No | prompts များကို အလိုအလျောက် အတည်ပြုသည်၊ CI တွင် အသုံးဝင်သည်။ |
| `--repo-url` | No | README languages table မှ sparse-checkout အကြံပေးချက်တွင် အသုံးပြုမည့် repository URL။ |
| `--migrate-language-folders` | No | `cn` သို့မဟုတ် `tw` ကဲ့သို့ အရင် alias ဖိုလ်ဒါများကို canonical BCP 47 ဖိုလ်ဒါများသို့ အမည်ပြင်မည်။ |
| `--dry-run` | No | ဖိုင်များကို မရေးဘဲ language folder migration နှင့် ဘာသာပြန် ခန့်မှန်းချက်များကို ကြိုကြည့်ပါ။ |

type flag မပေးပါက `translate` သည် Markdown၊ notebooks နှင့် images များကို လုပ်ဆောင်ပါမည်။ ပုံများ ဘာသာပြန်ရန် Azure AI Vision configuration လိုအပ်သည်။

## evaluate

ဘာသာပြန်ထားသော Markdown ကို တစ်ဘာသာစကားအတွက် အရည်အသွေး အကဲဖြတ်ပါ။

!!! warning "Experimental"
    `evaluate` သည် လေ့လာမှု အဆင့်တွင် ရှိသည်။ ၎င်းသည် rule-based နှင့် LLM-based အရည်အသွေး စစ်ဆေးမှုများကို အသုံးပြုနိုင်ပြီး၊ အကဲဖြတ်ရလဒ်များကို ဘာသာပြန် metadata ထဲသို့ ရေးသွင်းသည်။ ၎င်း၏ scoring မော်ဒယ်နှင့် metadata အပြုအမူများသည် ပြောင်းလဲနိုင်သည်။

```bash
evaluate -l "ko"
```

### သာမန် ဥပမာများ

ယုံကြည်မှုနည်းသော အကန့်အသတ်ကို ပိုတင်းကြပ်စွာ အသုံးပြုပါ။

```bash
evaluate -l "es" -c 0.8
```

Run rule-based checks only:

```bash
evaluate -l "fr" -f
```

Run LLM-based checks only:

```bash
evaluate -l "ja" -D
```

### ရွေးချယ်စရာများ

| Option | လိုအပ်ပါသလား | ဖော်ပြချက် |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | အကဲဖြတ်ရန် တစ်ခုသော ဘာသာစကား code။ Alias codes များကို ပုံမှန်အတိုင်း ပြင်ဆင်သည်။ |
| `-r`, `--root-dir` | No | Project root။ မပေးပါက လက်ရှိ directory ကို သတ်မှတ်သည်။ |
| `-c`, `--min-confidence` | No | ယုံကြည်မှုနည်းသော ဘာသာပြန်ချက်များကို စာရင်းပြုစစ်ရာတွင် အသုံးပြုသည့် သတ်မှတ်ချက်။ မပေးပါက `0.7` ဖြစ်သည်။ |
| `-d`, `--debug` | No | debug logging ကို ဖွင့်မည်။ |
| `-s`, `--save-logs` | No | DEBUG-level logs များကို `<root-dir>/logs/` အောက်တွင် သိမ်းမည်။ |
| `-f`, `--fast` | No | Rule-based အကဲဖြတ်မှုသာ လုပ်ဆောင်မည်။ |
| `-D`, `--deep` | No | LLM-based အကဲဖြတ်မှုသာ လုပ်ဆောင်မည်။ |

ပုံမှန်အားဖြင့် `evaluate` သည် စည်းမျဉ်းအခြေပြု (rule-based) နှင့် LLM အခြေပြု (LLM-based) ဆန်းစစ်မှုနှစ်မျိုးစလုံးကို အသုံးပြုသည်။ ရလဒ်များကို ဘာသာပြန် metadata ထဲသို့ မှတ်တမ်းတင်ပြီး console တွင် အကျဉ်းချုပ် ပြသသည်။

## co-op-review

API အတည်ပြုချက်များ မလိုဘဲ သတ်မှတ်နိုင်သော ဘာသာပြန် ထိန်းသိမ်းမှု စစ်ဆေးမှုများကို ပြုလုပ်ပါ။

!!! note "Beta"
    `co-op-review` သည် beta deterministic review command ဖြစ်သည်။ ၎င်းသည် model providers များကို ခေါ်မည် မဟုတ်ဘဲ ဖိုင်များကို ရေးမည် မဟုတ်သည်၊ သို့သော် ၎င်း၏ စစ်ဆေးမှုများနှင့် issue output schema များသည် ပြောင်းလဲနိုင်ပါသည်။

```bash
co-op-review -l "ko"
```

### သာမန် ဥပမာများ

လက်ရှိ ဖိုလ်ဒါမှ ကိုရီးယားနှင့် ဂျပန် ဘာသာပြန်များကို စစ်ဆေးပါ:

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

README သာ ဘာသာပြန်ပြီးနောက် README ကိုသာ စစ်ဆေးပါ:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` သည် အခြားစာရွက်စာတမ်းများနှင့် nested READMEs များကို မထည့်ပါ။ ၎င်းသည် root
`README.md` မရှိပါက အလုပ်မလုပ်ပါ။ `--changed-from` နှင့် ပေါင်းသုံးလျှင်၊ ၎င်းသည် README ကိုသာ
အဲဒီ source ဖိုင် ပြောင်းလဲခဲ့ပါက စစ်ဆေးပါသည်။ README-only translation သည် source README ကို
မထိခိုက်စေပါ၊ shared-section markers များကိုပါ ထိန်းသိမ်းထားမည်။

base ref နှင့် နှိုင်းယှဉ် ပြောင်းလဲထားသော source ဖိုင်များကိုသာ သုံးသပ်ပါ။

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI အနှစ်ချုပ်များအတွက် GitHub-flavored Markdown ထုတ်လွှင့်ပါ:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### ရွေးချယ်စရာများ

| Option | လိုအပ်ပါသလား | ဖော်ပြချက် |
| --- | --- | --- |
| `-l`, `--language-code` | No | စစ်ဆေးရန် ဘာသာစကား code။ အကြိမ်ပေါင်းများစွာ ပေးနိုင်သည် သို့မဟုတ် space-separated တန်ဖိုးအဖြစ် ပေးနိုင်သည်။ မပေးပါက ရှာဖွေတွေ့ရှိထားသည့် ဘာသာစကားအားလုံးကို စစ်ဆေးပါသည်။ |
| `-r`, `--root-dir` | No | Project root။ မပေးပါက လက်ရှိ directory ကို သတ်မှတ်သည်။ |
| `--changed-from` | No | ပြောင်းလဲထားသည့် source ဖိုင်များကိုသာ စစ်ဆေးရန် အသုံးပြုသည့် Git ref။ |
| `--readme-only` | No | root `README.md` ဘာသာပြန်ကိုသာ စစ်ဆေးသည်။ |
| `--format` | No | အထွက်ပုံစံ: `text` သို့မဟုတ် `github`။ မပေးပါက `text` ဖြစ်သည်။ |

`co-op-review` သည် လက်ရှိတွင် ပြန်လည်ဘာသာပြန်ထားသော ဖိုင်များမရှိခြင်း၊ ဘာသာပြန် metadata မရှိခြင်း သို့မဟုတ် အဟောင်းဖြစ်နေခြင်း၊ Markdown frontmatter နှင့် code fence အယူအဆ တိကျမှု၊ ဘာသာပြန်ထားသော notebook JSON မမှန်ကန်ခြင်းနှင့် ဒေသဆိုင်ရာ Markdown သို့မဟုတ် image link များ၏ ပစ်မှတ် မရှိခြင်းတို့ကို စစ်ဆေးပါသည်။ link မရှိခြင်းများသည် ပုံမှန်အားဖြင့် သတိပေးချက်များ ဖြစ်ကြပြီး ဖွဲ့စည်းမှုနှင့် လက်ရှိပြင်ဆင်မှုဆိုင်ရာ ပြဿနာများသည် command ကို မအောင်မြင်စေပါသည်။

## co-op-translator-mcp

Co-op Translator MCP ဆာဗာကို agents များ၊ editors များနှင့် MCP-ကိုက်ညီသည့် clients များအတွက် ပြေးပါ။

```bash
co-op-translator-mcp
```

ပုံမှန် သယ်ယူပို့ဆောင်မှုမှာ `stdio` ဖြစ်သည်။ client ဖော်မြူလာများ၊ ကိရိယာများ၊ အရင်းအမြစ်များနှင့် လုံခြုံရေး မှတ်ချက်များအတွက် [MCP Server](mcp.md) လမ်းညွှန်ကို ကြည့်ပါ။

### ရွေးချယ်စရာများ

| Option | လိုအပ်ပါသလား | ဖော်ပြချက် |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, သို့မဟုတ် `sse`။ မပေးပါက `stdio` ဖြစ်သည်။ |

## migrate-links

ဘာသာပြန်ပြီးသော Markdown ဖိုင်များကို ပြန်လည်ပြုလုပ်ပြီး၊ notebook links များကို ရရှိနိုင်သလောက် ဘာသာပြန်ထားသော notebooks များကို ညွှန်ပြသရန် အပ်ဒိတ်လုပ်ပါ။

```bash
migrate-links -l "ko ja"
```

### သာမန် ဥပမာများ

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

အတည်ပြုချက် မလိုဘဲ အထောက်ပံ့ထားသော ဘာသာစကားအားလုံးကို လုပ်ဆောင်ပါ:

```bash
migrate-links -l "all" -y
```

ဘာသာပြန်ထားသော notebooks ရှိသောအခါတွင်သာ လင့်ခ်များကို ပြန်ရေးပါ:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### ရွေးချယ်စရာများ

| Option | လိုအပ်ပါသလား | ဖော်ပြချက် |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | space ဖြင့် ခွဲထားသော language codes များ သို့မဟုတ် `"all"`။ |
| `-r`, `--root-dir` | No | Project root။ မပေးပါက လက်ရှိ directory ကို သတ်မှတ်သည်။ |
| `--image-dir` | No | root နှင့် ဆက်စပ်သည့် translated image directory။ မပေးပါက `translated_images` ဖြစ်သည်။ |
| `--dry-run` | No | ပြင်ဆင်ချက်များကို မရေးဘဲ ဘာများပြောင်းလဲမည့် ဖိုင်များကို ပြသပါ။ |
| `--fallback-to-original`, `--no-fallback-to-original` | No | ဘာသာပြန်ထားသော notebooks မရှိပါက မူရင်း notebook links ကို အသုံးပြုမည်။ ပုံမှန်အားဖြင့် ဖွင့်ထားသည်။ |
| `-d`, `--debug` | No | debug logging ကို ဖွင့်မည်။ |
| `-s`, `--save-logs` | No | DEBUG-level logs များကို `<root-dir>/logs/` အောက်တွင် သိမ်းမည်။ |
| `-y`, `--yes` | No | ဘာသာစကားအားလုံးကို process လုပ်သည့်အခါ အတည်ပြုချက်များကို အလိုအလျောက် ချက်ချင်း ချက်ယူမည်။ |

## ပတ်ဝန်းကျင်

Command တစ်ခုတွင် provider credentials လိုအပ်ပါက ဤ provider sets များထဲမှ တစ်ခုကို ဖွဲ့စည်းပါ။ `translate --dry-run` နှင့် `co-op-review` များသည် provider credentials မလိုအပ်ပါ။

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

ပုံများ ဘာသာပြန်ရန် အတူတကွ Azure AI Vision ကိုလည်း လိုအပ်ပါသည်:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## ထွက် ပုံစံ

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

ဘာသာပြန်ထားသော ပုံထွက်ကို အောက်တွင် သိမ်းထားသည်:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## ကော်ပီ-ပိပ် CLI ဥပမာများ

Translate Markdown into three languages:

```bash
translate -l "ko ja fr" -md
```

Translate notebooks only:

```bash
translate -l "zh-CN" -nb
```

Translate images only:

```bash
translate -l "pt-BR" -img
```

ဖိုင်များ မရေးဘဲ Markdown ဘာသာပြန်ချက်ကို ကြိုကြည့်ရန်:

```bash
translate -l "de es" -md --dry-run
```

Repair low-confidence Markdown translations:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Run CI-friendly Markdown translation:

```bash
translate -l "ko ja" -md -y -s
```

Review translated output:

```bash
co-op-review -l "ko ja"
```

Preview link migration:

```bash
migrate-links -l "ko" --dry-run
```