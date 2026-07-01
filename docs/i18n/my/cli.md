# CLI အညွှန်း

Co-op Translator သည် အောက်ပါ command-line entry point များကို တပ်ဆင်ပေးသည်။

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`, `evaluate`, `migrate-links`, နှင့် `co-op-review` command များကို `co_op_translator.__main__` မှအားဖြင့် dispatch လုပ်ပြီး ခလုတ်အမည်အရ အကောင်အထည်ဖော်မှုကို ရွေးချယ်သည်။ MCP server သည် `co_op_translator.mcp.server` ကို တိုက်ရိုက် အသုံးပြုသည်။

CLI, Python API, နှင့် MCP တို့ကြား ရွေးချယ်ရန် ရှိပါက [Choose Your Workflow](workflows.md) ကို စတင် ဖတ်ရှုပါ။

## First-Time CLI Flow

Terminal မှ Co-op Translator ကို အသုံးပြုပြီးစတင်မည့်သူများအတွက် အစမှ စတင်ရန် ထိုနေရာမှ စတင်ပါ။

1. [Configuration](configuration.md) တွင် ဖော်ပြထားသည့် အတိုင်း LLM provider ကို setup ပြုလုပ်ပါ။
2. ဘာသားအမျိုးအစားကို ဘာသာပြန်လိုသည်ကို ရွေးချယ်ပါ။
3. ပထမဦးဆုံး အာရုံစိုက်သော command တစ်ခုကို လုပ်ဆောင်ပါ၊ ဥပမာ Markdown-only ဘာသာပြန်ခြင်း။
4. ကြီးမားသော repository ပြင်ဆင်မှုများမလုပ်မီ `--dry-run` ကို အသုံးပြု၍ ကြို-preview လုပ်ပါ။
5. ဘာသာပြန်ပြီးနောက် structure နှင့် freshness ကို စစ်ဆေးရန် `co-op-review` ကို အသုံးပြုပါ။

| ရည်ရွယ်ချက် | စတင်ရန် အသုံးပြုမည့် အမိန့် |
| --- | --- |
| Markdown စာရွက်စာတမ်းများ ဘာသာပြန်ခြင်း | `translate -l "ko" -md` |
| Notebook များ ဘာသာပြန်ခြင်း | `translate -l "ko" -nb` |
| ပုံစာသား ဘာသာပြန်ခြင်း | `translate -l "ko" -img` |
| ဖိုင်များကို မရေးထည့်ဘဲ အလုပ်ကို ကြိုပြရန် | `translate -l "ko" -md --dry-run` |
| ရှိပြီးသား ဘာသာပြန်များကို စိစစ်ရန် | `co-op-review -l "ko"` |
| Notebook နှင့် Markdown link များကို အပ်ဒိတ်လုပ်ရန် | `migrate-links -l "ko" --dry-run` |
| MCP client သို့ ကိရိယာများကို ဖော်ပြရန် | CLI commands များကို တိုက်ရိုက် မရိုက်ပေးဘဲ [MCP Server](mcp.md) ကို ဖော်ပြ၍ သတ်မှတ်ပါ။ |

## translate

Markdown ဖိုင်များ၊ notebook များ၊ နှင့် ပုံစာသားများကို တစ်ခု သို့မဟုတ် အများသော target language များသို့ ဘာသာပြန်သည်။

```bash
translate -l "ko ja fr"
```

### Common examples

Markdown ပဲ ဘာသာပြန်ရန်:

```bash
translate -l "de" -md
```

Notebook ပဲ ဘာသာပြန်ရန်:

```bash
translate -l "zh-CN" -nb
```

Markdown နှင့် ပုံများကို ဘာသာပြန်ရန်:

```bash
translate -l "pt-BR" -md -img
```

ရှိပြီးသား ဘာသာပြန်များကို ဖျက်ပြီး ထပ်မံဖန်တီး၍ အပ်ဒိတ်လုပ်ရန်:

```bash
translate -l "ko" -u
```

အင်တာ‌က်တက်မရှိဘဲ လည်ပတ်ရန်:

```bash
translate -l "ko ja" -md -y
```

လော့ဂ်များကို သိမ်းဆည်းရန်:

```bash
translate -l "ko" -s
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | ဟုတ် | Space-separated language codes, such as `"es fr de"`, or `"all"`. |
| `-r`, `--root-dir` | မဟုတ် | Project root. Defaults to the current directory. |
| `-u`, `--update` | မဟုတ် | Delete existing translations for selected languages and recreate them. |
| `-img`, `--images` | မဟုတ် | Translate only image files. |
| `-md`, `--markdown` | မဟုတ် | Translate only Markdown files. |
| `-nb`, `--notebook` | မဟုတ် | Translate only Jupyter notebook files. |
| `-d`, `--debug` | မဟုတ် | Enable debug logging in the console. |
| `-s`, `--save-logs` | မဟုတ် | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-x`, `--fix` | မဟုတ် | Retranslate low-confidence Markdown files based on previous evaluation results. |
| `-c`, `--min-confidence` | မဟုတ် | Confidence threshold for `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | မဟုတ် | Add or suppress machine translation disclaimers. Defaults to enabled in the CLI. |
| `-f`, `--fast` | မဟုတ် | Deprecated fast image mode. |
| `-y`, `--yes` | မဟုတ် | Auto-confirm prompts, useful in CI. |
| `--repo-url` | မဟုတ် | Repository URL used in the README languages table sparse-checkout advisory. |
| `--migrate-language-folders` | မဟုတ် | Rename legacy alias folders, such as `cn` or `tw`, to canonical BCP 47 folders. |
| `--dry-run` | မဟုတ် | Preview language folder migration and translation estimates without writing files. |

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Experimental"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### Common examples

ပိုတိကျသော low-confidence သတ်မှတ်ချက် threshold ကို သတ်မှတ်ရန်:

```bash
evaluate -l "es" -c 0.8
```

rule-based စစ်ဆေးချက်များပဲ အသုံးပြုရန်:

```bash
evaluate -l "fr" -f
```

LLM-based စစ်ဆေးချက်များပဲ အသုံးပြုရန်:

```bash
evaluate -l "ja" -D
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | ဟုတ် | Single language code to evaluate. Alias codes are normalized. |
| `-r`, `--root-dir` | မဟုတ် | Project root. Defaults to the current directory. |
| `-c`, `--min-confidence` | မဟုတ် | Threshold used when listing low-confidence translations. Defaults to `0.7`. |
| `-d`, `--debug` | မဟုတ် | Enable debug logging. |
| `-s`, `--save-logs` | မဟုတ် | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | မဟုတ် | Rule-based evaluation only. |
| `-D`, `--deep` | မဟုတ် | LLM-based evaluation only. |

By default, `evaluate` uses both rule-based and LLM-based evaluation. Results are written into translation metadata and summarized in the console.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "Beta"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

```bash
co-op-review -l "ko"
```

### Common examples

ယခု directory မှ Korean နှင့် Japanese ဘာသာပြန်များကို စိစစ်ရန်:

```bash
co-op-review -l "ko ja"
```

သတ်မှတ်ထားသော project root ကို စိစစ်ရန်:

```bash
co-op-review -l "fr" -r ./my-course
```

base ref နှင့် နှိုင်းယှဉ်ပြီး ပြောင်းလဲထားသည့် source ဖိုင်များသာ စိစစ်ရန်:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI စာအကျဉ်းများအတွက် GitHub-flavored Markdown output ကို 출력ရန်:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | မဟုတ် | Language code to review. Can be passed multiple times or as a space-separated value. Defaults to all discovered translation languages. |
| `-r`, `--root-dir` | မဟုတ် | Project root. Defaults to the current directory. |
| `--changed-from` | မဟုတ် | Git ref used to limit review to changed source files. |
| `--format` | မဟုတ် | Output format: `text` or `github`. Defaults to `text`. |

`co-op-review` သည် လက်ရှိတွင် missing translated files, missing or stale translation metadata, Markdown frontmatter နှင့် code fence တည်ငြိမ်မှု, မမှန်ကန်သော translated notebook JSON, နှင့် မရှိသေးသော local Markdown သို့မဟုတ် image link targets များကို စစ်ဆေးပါသည်။ Missing links များကို ပုံမှန်အားဖြင့် အကြောင်းကြားချက်များ (warnings) အဖြစ် ပြသသည်; structural နှင့် freshness ပတ်သက်သော ပြဿနာများသည် command ကို fail လုပ်စေပါသည်။

## co-op-translator-mcp

Agents, editors, နှင့် MCP-compatible clients များအတွက် Co-op Translator MCP server ကို ဖွင့်ပါ။

```bash
co-op-translator-mcp
```

Default transport သည် `stdio` ဖြစ်သည်။ client configuration, tools, resources, နှင့် safety မှတ်ချက်များအတွက် [MCP Server](mcp.md) ကို ကြည့်ပါ။

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | မဟုတ် | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Translated Markdown ဖိုင်များကို ပြန်လည် επတွင်း ဆန်းစစ်ပြီး translated notebooks ရှိနှင့်မရှိ အခြေအနေတွင် notebook link များကို translated notebooks သို့ ညွှန်ပြになるよう update လုပ်သည်။

```bash
migrate-links -l "ko ja"
```

### Common examples

link update များကို ကြိုပြရန်:

```bash
migrate-links -l "ko" --dry-run
```

အတည်ပြုချက်မလိုပဲ supported languages များအားလုံးကို ပြုလုပ်ရန်:

```bash
migrate-links -l "all" -y
```

translated notebooks ရှိသည့်အခါမှသာ links ကို rewrite လုပ်ရန်:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | ဟုတ် | Space-separated language codes, or `"all"`. |
| `-r`, `--root-dir` | မဟုတ် | Project root. Defaults to the current directory. |
| `--image-dir` | မဟုတ် | Translated image directory relative to the root. Defaults to `translated_images`. |
| `--dry-run` | မဟုတ် | Show files that would change without writing updates. |
| `--fallback-to-original`, `--no-fallback-to-original` | မဟုတ် | Use original notebook links when translated notebooks are missing. Enabled by default. |
| `-d`, `--debug` | မဟုတ် | Enable debug logging. |
| `-s`, `--save-logs` | မဟုတ် | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-y`, `--yes` | မဟုတ် | Auto-confirm prompts when processing all languages. |

## Environment

All commands require one configured LLM provider:

```bash
# အေဇာ OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# သို့မဟုတ် OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

Translated image output is written under:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Copy-Paste CLI Examples

Markdown ကို သုံးဘာသာစကားသို့ ဘာသာပြန်ရန်:

```bash
translate -l "ko ja fr" -md
```

Notebook များပဲ ဘာသာပြန်ရန်:

```bash
translate -l "zh-CN" -nb
```

ပုံများပဲ ဘာသာပြန်ရန်:

```bash
translate -l "pt-BR" -img
```

Markdown ဘာသာပြန်ကို ဖိုင်များမရေးထည့်ဘဲ ကြိုပြရန်:

```bash
translate -l "de es" -md --dry-run
```

low-confidence Markdown ဘာသာပြန်များကို ပြန်ပြုပြင်ရန်:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

CI နဲ့ ကိုက်ညီသော Markdown ဘာသာပြန်ကို အသုံးပြုရန်:

```bash
translate -l "ko ja" -md -y -s
```

ဘာသာပြန်ပြီး output ကို စစ်ဆေးရန်:

```bash
co-op-review -l "ko ja"
```

link migration ကို ကြိုပြရန်:

```bash
migrate-links -l "ko" --dry-run
```