# သင်၏ အလုပ်စဉ်ကို ရွေးချယ်ပါ

Co-op Translator ကို သုံးနိုင်သည့် နည်းလမ်းသုံးမျိုးရှိသည်။ CLI၊ Python API၊ နှင့် MCP server ဖြစ်သည်။ ၎င်းတိုင်းတွင် ဘာသာပြန်နိုင်စွမ်းများသည် တစ်ပုံတည်းသာဖြစ်သော်လည်း အချို့သည် မတူညီသော လုပ်ငန်းစဉ်များနှင့် သင့်လျော်သည်။

စတင်ရမည့်နေရာကို ဆုံးဖြတ်ရာတွင် ဤစာမျက်နှာကို အသုံးပြုပါ။

## အမြန်ဆုံး ဆုံးဖြတ်ချက်

| သင် ... လုပ်ချင်ပါက | အသုံးပြုရန် | ဒီနေရာကစပါ |
| --- | --- | --- |
| တာမင်နယ်မှ ရှေ့ပိုင်း repository ကို ဘာသာပြန်ရန် သို့မဟုတ် ပြန်လည်ဆန်းစစ်ရန် | CLI | [CLI Reference](cli.md) |
| Python script, service, notebook, သို့မဟုတ် CI job ထဲသို့ ဘာသာပြန်ခြင်း ထည့်သွင်းရန် | Python API | [Python API](api.md) |
| Agent, editor, သို့မဟုတ် MCP-compatible client တစ်ခုက သင့်အစား အကြောင်းအရာ ဘာသာပြန်ပေးစေချင်ပါက | MCP Server | [MCP Server](mcp.md) |
| သင့်အက်ප්လီကေးရှင်းသည် ယခုအချိန်တွင် လက်ခံထားသော Markdown မှတ်တမ်းတစ်ခု၊ notebook တစ်ခု၊ သို့မဟုတ် image တစ်ပုံကို ဘာသာပြန်လိုသည် | Python API သို့မဟုတ် MCP Server | [Python API](api.md) သို့မဟုတ် [MCP Server](mcp.md) |
| စံအထွေထွေ output ဖိုလ္ဒါများနှင့် မက်တာဒေတာဖြင့် တစ်ခုလုံး repository ကို ဘာသာပြန်လိုသည် | CLI သို့မဟုတ် `run_translation` | [CLI Reference](cli.md) သို့မဟုတ် [Python API](api.md) |

## CLI ကို ဘယ်အချိန် သုံးသင့်သည်

Terminal မှ repository ဘာသာပြန်ခြင်းကို လူတစ်ဦး သို့မဟုတ် CI job တစ်ခုက အကြောင်းအရာ ဦးဆောင်လျှင် CLI ကို ရွေးချယ်ပါ။

Co-op Translator ကို project ဖိုင်များ ရှာဖွေခြင်း၊ ဘာသာပြန်ထားသော output များ ဖန်တီးခြင်း၊ project လုပ်ထုံးလုပ်နည်းကို ထိန်းသိမ်းခြင်း၊ မက်တာဒေတာ ပြင်ဆင်ခြင်းနှင့် သုံးသပ်ရေးကိရိယာများ ကို အကောင်အထည်ဖော်ပေးရန် CLI သည် တိုက်ရိုက်ဆုံး ချိတ်ဆက်မှုဖြစ်သည်။

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

သင့်တော်ချက်များ:

- သင်သည် terminal မှ repository တစ်ခုကို ဘာသာပြန်နေသည်။
- CI သို့မဟုတ် release workflow များအတွက် တစ်ဦးတည်းသော command ကို ထပ်မံ အသုံးပြုနိုင်ချင်သည်။
- Built-in project discovery, output paths, metadata, cleanup, နှင့် review ကို လိုသည်။
- Python ကုဒ်ရေးခြင်းထက် command အပြင်မှ အင်တာဖေ့စ်ကို ưu preferr လျှင်။

## Python API ကို ဘယ်အချိန် သုံးသင့်သည်

သင့်ကိုယ်ပိုင်ကုဒ်သည် workflow ကို ထိန်းချုပ်ရမည်ဆိုပါက Python API ကို ရွေးချယ်ပါ။

API သည် application များ၊ automation script များ၊ notebook များ၊ service များနှင့် custom pipeline များအတွက် အသုံးဝင်သည်။ ထိုသို့ API သည် တစ်ဖိုင်ချင်းစီအတွက် အကြောင်းအရာ ဘာသာပြန်ရန် အောက်လွှာ API များကို ခေါ်ယူရန် သို့မဟုတ် CLI မှ အသုံးပြုသည့် repository မျက်နှာပြင်-level အဖွဲ့ချုပ်ကို ကူးယူ အသုံးပြုနိုင်သည်။

Markdown မှတ်တမ်းတစ်ခုကို ဘာသာပြန်၍ ဘယ်နေရာသိမ်းမည်ကို ဆုံးဖြတ်ပါ:

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

Python မှ repository ဘာသာပြန်မှုကို ပြေးပါ:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

သင့်တော်ချက်များ:

- သင့်အက်ပလီကေးရှင်းသည် ဖိုင်များ၊ buffer များ၊ notebook များ သို့မဟုတ် image bytes များကို ရှာဖွေပြီးသားဖြစ်သည်။
- သင်သည် custom validation, storage, logging, retries, သို့မဟုတ် approval flow များ လိုအပ်သည်။
- တစ်ခုသော စာရွက်စာတမ်း၊ notebook သို့မဟုတ် image ကို အခြား repository တစ်ခုလုံးကို အလုပ်လုပ်စေခြင်းမလုပ်ဘဲ ဘာသာပြန်လိုသည်။
- Repository ဘာသာပြန်မှုကို လုပ်လိုသော သို့သော် shell command အစား Python automation ကနေ မောင်းနှင်လိုသည်။

## MCP Server ကို ဘယ်အချိန် သုံးသင့်သည်

Agent, editor, သို့မဟုတ် MCP-compatible client တစ်ခုက Co-op Translator ကိရိယာများကို ဖုန်းခေါ်လိုသည်ဆိုပါက MCP server ကို ရွေးချယ်ပါ။

ပုံမှန် local ဖွဲ့စည်းမှုတွင်၊ အသုံးပြုသူသည် လက်ဖြင့် server ကို စောင့်ထားရန် မလိုအပ်ပါ။ MCP client သည် tools လိုအပ်သည့်အခါ `co-op-translator-mcp` ကို `stdio` ပေါ်တွင် စတင်မောင်းနှင်မည်။

အသုံးပြုသူ တောင်းဆိုချက်များအနေဖြင့် agent က ကိုင်တွယ်နိုင်သော နမူနာများ -

- "ဤ Markdown ဖိုင်ကို ကိုရီးယားဘာသာသို့ ဘာသာပြန်နှင့် links များကို မှန်ကန်စေပါ။"
- "ဤ Markdown ဖိုင်ကို agent-assisted MCP workflow ဖြင့် ကိုရီးယားဘာသာသို့ ဘာသာပြန်ပါ၊ ဘာသာပြန်ထားသော chunks များအတွက် သင့်ရဲ့ မော်ဒယ်ကို အသုံးပြုပါ။"
- "ဤ notebook ကို ကိုရီးယားဘာသာသို့ ဘာသာပြန်ပါ၊ code cells များကို ထိန်းသိမ်းပြီး Co-op Translator MCP ကို အသုံးပြုပြီး notebook ကို ပြန်တည်ဆောက်ပါ။"
- "ဤ image ထဲရှိ စာသားကို ဂျပန်ဘာသာသို့ ဘာသာပြန်ပြီး ရလဒ်ကို သိမ်းဆည်းပါ။"
- "Repository ဘာသာပြန်မှုကို Spanish သို့ dry-run ပြုလုပ်၍ ဘာတွေ ပြောင်းလဲမည်ကို ပြောပြပါ။"
- "ကိုရီးယားဘာသာပြန် ထွက်ရှိမှုသည် up to date ဖြစ်မရှိ စစ်ဆေးပေးပါ။"

Markdown နှင့် notebook များအတွက် MCP သည် နှစ်မျိုးသော မုဒ်ဖြင့် လုပ်ဆောင်နိုင်သည် -

| Mode | ဘယ်အချိန် အသုံးပြုရန် | Main tools |
| --- | --- | --- |
| Agent-assisted | MCP host agent သည် Co-op Translator LLM provider credentials မရှိပဲ သူ့ရဲ့ ကိုယ်ပိုင်မော်ဒယ်ဖြင့် chunks များကို ဘာသာပြန်သင့်သည့်အခါ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator သည် Azure OpenAI သို့မဟုတ် OpenAI ကို တိုက်ရိုက် ခေါ်ယူသင့်သည် | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown tool call shape:

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

MCP image tool call shape:

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

Repository ဘာသာပြန်မှုသည် MCP မှတဆင့် မူလအားဖြင့် dry-run ဖြစ်သည်:

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

သင့်တော်ချက်များ:

- Agent သို့ editor အတွင်းတွင် သဘာဝ-ဘာသာစကား ဘာသာပြန် workflow များ လိုချင်ပါက။
- Host agent model သည် ပြင်ဆင်ထားသော chunks များကို ဘာသာပြန်ပေးသင့်သော Markdown သို့မဟုတ် notebook ဘာသာပြန်မှုများလိုချင်ပါက။
- Agent ကို repository တစ်ခုလုံးမဟုတ်ပဲ ရွေးချယ်ထားသော အကြောင်းအရာကို ဘာသာပြန်စေလိုပါက။
- Repository အားလုံးကို ရေးသားမှတ်သားမှုများမပြုခင် အတည်ပြုခြင်း အဆင့်လိုချင်ပါက။
- Markdown, notebook, image, review နှင့် path-rewriting ကိရိယာများကို ဖော်ပြသည့် တစ်ခုတည်းသော အင်တာဖေ့စ် တစ်ခုလိုချင်ပါက။

## ၎င်းတို့သည် ဘယ်လို ကိုက်ညီသနည်း

CLI သည် လူများက repository များကို ဘာသာပြန်ရာတွင် ပုံမှန် အကောင်းဆုံး ရွေးချယ်မှုဖြစ်သည်။ Python API သည် သင်၏ကုဒ်သည် workflow ကို ကိုင်တွယ်သည့်အခါ အကောင်းဆုံးဖြစ်သည်။ MCP server သည် agent သို့ editor က workflow ကို ကိုင်တွယ်သည့်အခါ အကောင်းဆုံးဖြစ်သည်။

ทั้งသုံးမျိုးလည်း တူညီသော public Co-op Translator API ကို အသုံးပြုသည်။ ထို့ကြောင့် CLI ဖြင့် စတင်ပြီးနောက် Python ဖြင့် အလိုအလျောက်လုပ်ငန်းများကို ပြုလုပ်နိုင်ပြီး MCP clients များအတွက် agent-ကို အားပေးလိုသော workflow များကို ထုတ်ပေးနိုင်သည်။