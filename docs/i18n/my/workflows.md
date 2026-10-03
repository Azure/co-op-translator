# သင့် အလုပ်စဉ်ကို ရွေးချယ်ပါ

Co-op Translator ကို CLI, Python API, နှင့် MCP server ဆိုသည့် နည်းလမ်းသုံးမျိုးဖြင့် အသုံးပြုနိုင်သည်။ ၎င်းတို့တွင် ဘာသာပြန်နိုင်စွမ်းတူညီပေမယ့် တစ်ခုချင်းစီသည် အလုပ်စဉ်ကွဲပြားချက်အလိုက် သင့်တော်သည်။

စတင်ရန် ဘယ်နေရာမှ စရမည်ဟု ဆုံးဖြတ်နေစဉ် ဤစာမျက်နှာကို အသုံးပြုပါ။

**ဘာသာပြန်ချက်များကို ကိုယ့်လက်ဖြင့် တည်းဖြတ်ပါက:** ပုံမှန် CLI နှင့် Actions အလုပ်စဉ်များသည် ပြောင်းလဲထားသည့် မူလဖိုင်များအားလုံးကို ပြန်လည်ဘာသာပြန်ပေးသဖြင့် သင်၏ စကားလုံးများကို အစားထိုးခံရနိုင်သည်။ အပ်ဒိတ်တစ်ခုကို လက်ခံမီ diff ကို ပြန်လည်သုံးသပ်ပါ။ လက်ခံထားသော တည်းဖြတ်ချက်များကို Markdown block-level အနေနှင့် ထိန်းသိမ်းရန် ရွေးချယ်ဖြစ်နိုင်သည့် [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) ကို အသုံးပြုပါ။

## အမြန်ဆုံးဆုံးဖြတ်ချက်

| သင်လိုချင်သည်မှာ... | သုံးရန် | ဒီမှာ စတင်ပါ |
| --- | --- | --- |
| Terminal မှ repository ကို ဘာသာပြန်ရန် သို့မဟုတ် စစ်ဆေးရန် | CLI | [CLI Reference](cli.md) |
| Python script၊ service၊ notebook သို့မဟုတ် CI job ထဲသို့ ဘာသာပြန်ချက် ထည့်သွင်းရန် | Python API | [Python API](api.md) |
| Agent၊ editor သို့မဟုတ် MCP-compatible client ကို သင်အတွက် အကြောင်းအရာကို ဘာသာပြန်ပေးစေလိုပါက | MCP Server | [MCP Server](mcp.md) |
| သင့်အက်ပ်က အရင်က load လုပ်ထားသော Markdown စာရွက်တစ်ခု၊ notebook သို့မဟုတ် image တစ်ပုံကို ဘာသာပြန်လိုပါက | Python API သို့မဟုတ် MCP Server | [Python API](api.md) သို့မဟုတ် [MCP Server](mcp.md) |
| စံနှုန်းအတိုင်း output ဖိုင်ဖိုဒါများနှင့် metadata ပါသည့် တစ်ခုလုံး repository ကို ဘာသာပြန်ရန် | CLI သို့မဟုတ် `run_translation` | [CLI Reference](cli.md) သို့မဟုတ် [Python API](api.md) |

## CLI ကို အောက်ပါအခါ အသုံးပြုပါ

လူတစ်ဦး သို့မဟုတ် CI job တစ်ခုက shell မှ repository ဘာသာပြန်မှုကို ဦးစီးနေသောအခါ CLI ကို ရွေးချယ်ပါ။

Co-op Translator ကို project ဖိုင်များ ရှာဖွေစေ၊ ဘာသာပြန်ထွက်များ ဖန်တီးစေ၊ project ဖွဲ့စည်းမှုပုံစံကို ထိန်းသိမ်းစေ၊ metadata ကို အပ်ဒိတ်လုပ်စေ၊ နှင့် review command များကို လည်ပတ်စေချင်သောအခါ CLI သည် အတိုက်ဆုံးလမ်းကြောင်း ဖြစ်သည်။

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

ဤဥပမာတွင် Markdown နှင့် notebook များကို ဘာသာပြန်ပါသည်။ `-img` ကို [Azure AI Vision](configuration.md#azure-ai-vision) ဖြင့် ပြင်ဆင်ပြီးမှသာ ထည့်ပါ။ Markdown ပဲ အသုံးပြုသော ပထမဆုံး ဆောင်ရွက်မှုအတွက် [Your first translation](first-translation.md) ကို လိုက်နာပါ။

သင့်တော်သော အခြေအနေများ:

- သင်သည် terminal မှ repository ကို ဘာသာပြန်နေပါသည်။
- သင်သည် CI သို့မဟုတ် release အလုပ်စဉ်များအတွက် ထပ်တလဲလဲ အသုံးပြုနိုင်သော command လိုချင်သည်။
- သင်သည် built-in project ရှာဖွေရေး၊ output လမ်းကြောင်းများ၊ metadata၊ သန့်ရှင်းရေးနှင့် review အစီအစဉ်များလိုချင်သည်။
- Python ကိုဒ်ရေးရန်ထက် command အင်တာဖေ့စ်ကို ကြိုက်နှစ်သက်သည်။

## Python API ကို အောက်ပါအခါ အသုံးပြုပါ

သင့်ရဲ့ ကိုယ်ပိုင် ကုဒ်က အလုပ်စဉ်ကို ထိန်းချုပ်သင့်လျှင် Python API ကို ရွေးချယ်ပါ။

API သည် အပလီကေးရှင်းများ၊ အော်တိုမေးရှင်း စကရစ်ပ်များ၊ notebooks၊ ဆာဗစ်များ နှင့် စိတ်ကြိုက် pipelines များအတွက် အသုံးဝင်သည်။ ၎င်းက သင့်အား တစ်ဖိုင်ချင်းစီအတွက် အောက်ပိုင်း content translation API များကို ခေါ်သုံးခွင့်ပြုကာ CLI အသုံးပြုသည့် အတူတူ repository-level orchestration ကိုလည်း ပြေးနိုင်စေသည်။

Markdown စာရွက်တစ်ခုကို ဘာသာပြန်ၿပီး ဘယ်နေရာသိမ်းမည်ဆိုတာ ဆုံးဖြတ်ပါ။

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Python မှ repository ဘာသာပြန်မှုကို ဆောင်ရွက်ရန်:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

သင့်တော်သော အခြေအနေများ:

- သင့်အက်ပ်သည် ဖိုင်များ၊ buffer များ၊ notebook များ သို့မဟုတ် image bytes များကို ရှိပြီး ဖတ်ယူထားပြီးသားဖြစ်သည်။
- သင်သည် စိတ်ကြိုက် အတည်ပြုခြင်း၊ သိမ်းဆည်းမှု၊ မှတ်တမ်းတင်မှု၊ ပြန်လည်ကြိုးစားမှုများ သို့မဟုတ် အတည်ပြု လုပ်ငန်းစဉ်များလိုအပ်သည်။
- သင်သည် စာရွက်စာတမ်း တစ်ခု၊ notebook သို့မဟုတ် image တစ်ပုံကို repository တစ်ခုလုံးကို မလုပ်ဆောင်ဘဲ ဘာသာပြန်လိုသည်။
- သင်သည် repository ဘာသာပြန်ခြင်းကို shell command မဟုတ်ဘဲ Python automation မှ တာဝန်ယူစေချင်သည်။

## MCP Server ကို အောက်ပါအခါ အသုံးပြုပါ

agent၊ editor သို့မဟုတ် MCP-compatible client တစ်ခုက Co-op Translator tools များကို ခေါ်သုံးသင့်သောအခါ MCP server ကို ရွေးချယ်ပါ။

ပုံမှန် local setup တွင် အသုံးပြုသူသည် server ကို လက်ဖြင့် ထားစဉ်းဆံ့ရန် မလိုပါ။ MCP client သည် tools မလိုအပ်သည့်အခါ `stdio` အပေါ် `co-op-translator-mcp` ကို စတင်ခေါ်ပေးသည်။

agent က ကိုင်တွယ်နိုင်သော ဥပမာ အသုံးပြုသူ တောင်းဆိုမှုများ:

- "ဤ Markdown ဖိုင်ကို ကိုရီးယားဘာသာသို့ ဘာသာပြန်ပြီး link များကို မှန်ကန်စေပါ။"
- "ဤ Markdown ဖိုင်ကို agent-assisted MCP workflow ဖြင့် ကိုရီးယားဘာသာသို့ ဘာသာပြန်ပါ၊ ဘာသာပြန်ထားသော ပိုင်းများအတွက် သင့်ပိုင် မော်ဒယ်ကို အသုံးပြုကာ။"
- "ဤ notebook ကို ကိုရီးယားဘာသာသို့ ဘာသာပြန်ပြီး code cells များကို ထိန်းသိမ်းပါ၊ Co-op Translator MCP ကို အသုံးပြု၍ notebook ကို ထပ်မံဖန်တီးပါ။"
- "ဤပုံအတွင်းရှိ စာသားကို ဂျပန်ဘာသာသို့ ဘာသာပြန်ပြီး ရလဒ်ကို သိမ်းဆည်းပါ။"
- "repository ဘာသာပြန်မှုကို စမ်းသပ် (dry-run) အဖြစ် စပိန်ဘာသာသို့ ပြန်လုပ်ပြီး ဘာတွေပြောင်းလဲမလဲ ပြောပြပါ။"
- "ကိုရီးယားဘာသာပြန် ထွက်ချက်သည် နောက်ဆုံးပေါ်ဖြစ်/မဖြစ်ကို ပြန်လည်စစ်ဆေးပါ။"

Markdown နှင့် notebook များအတွက် MCP သည် mode နှစ်မျိုးဖြင့် အလုပ်လုပ်နိုင်သည်။

| Mode | ဘယ်အခါ အသုံးပြုမလဲ | အဓိကကိရိယာများ |
| --- | --- | --- |
| Agent-assisted | MCP host agent သည် Co-op Translator LLM provider credentials မလိုအပ်ဘဲ ၎င်း၏ မော်ဒယ်ဖြင့် ပိုင်းများကို ဘာသာပြန်ပေးရမည့်အခါ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator သည် Azure OpenAI, OpenAI, သို့မဟုတ် Anthropic ကို တိုက်ရိုက် ခေါ်သင့်သည်။ | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown tool ခေါ်ဆိုမှု အပုံစံ:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP image tool ခေါ်ဆိုမှု အပုံစံ:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

MCP တွင် repository ဘာသာပြန်မှုကို အပေါ်မှတင်အားဖြင့် dry-run အဖြစ် ဆောင်ရွက်သည်။

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

သင့်တော်သော အခြေအနေများ:

- သင်သည် agent သို့မဟုတ် editor အတွင်းတွင် သဘာဝဘာသာစကား အခြေပြု ဘာသာပြန် အလုပ်စဉ်များလိုချင်သည်။
- သင်သည် host agent မော်ဒယ်က ပြင်ဆင်ထားသော ပိုင်းများကို ဘာသာပြန်ပေးသော Markdown သို့မဟုတ် notebook ဘာသာပြန်မှုလိုချင်သည်။
- သင်သည် စုစုပေါင်း repository အစား ရွေးချယ်ထားသော အကြောင်းအရာများကို agent က ဘာသာပြန်စေချင်သည်။
- သင်သည် repository အားလုံးကို ရေးသားမှုပြုလုပ်မီ အတည်ပြုခြင်း အဆင့်တစ်ခုလိုချင်သည်။
- သင်သည် Markdown, notebook, image, review, နှင့် path-rewriting ကိရိယာများကို ထုတ်ဖော်ပြသနိုင်မည့် တစ်ခုတည်းသော အင်တာဖေ့စ်ကို လိုချင်သည်။

## ၎င်းတို့ ဘယ်လို ပေါင်းစည်းသလဲ

Repository များကို လူများက ဘာသာပြန်ရာတွင် CLI သည် ပုံမှန်အတွက် အကောင်းဆုံး ဖြစ်သည်။ ကိုယ်ပိုင် ကုဒ်က workflow ကို ထိန်းချုပ်သောအခါ Python API သည် အကောင်းဆုံး ဖြစ်သည်။ agent သို့မဟုတ် editor က workflow ကို ထိန်းချုပ်သောအခါ MCP server သည် အကောင်းဆုံး ဖြစ်သည်။

လမ်းကြောင်းသုံးခုလုံးသည် တူညီသော public Co-op Translator API ကို အသုံးပြုသောကြောင့် CLI ဖြင့် စတင်၍ နောက်ပိုင်း Python ဖြင့် အော်တိုမိတ်လုပ်ပြီး agent-driven workflows လိုအပ်လာသောအခါ MCP clients များအား အတူတူ စွမ်းရည်များကို ထုတ်ဖော်နိုင်သည်။