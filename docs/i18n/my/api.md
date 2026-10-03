# Python API

တည်ငြိမ်သော အများသုံး Python API ကို `co_op_translator.api` မှ ထုတ်ပေးထားသည်။ ပေါင်းစည်းမှုများအများစုသည် အောက်ပါ လုပ်ငန်းစဉ်များထဲမှ တစ်ခုကို အသုံးပြုသည်။

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| တစ်ဖိုင်ချင်း သို့မဟုတ် စာရွက်စာတမ်းများ ဘာသာပြန်ခြင်း | သင့်အက်ပ်လိကေးရှင်းသည် မူလအကြောင်းအရာကို ဖတ်ပြီး၊ Co-op Translator ကို ဘာသာပြန်ရန် ခေါ်ဆိုကာ ရလဒ်ကို သိမ်းမည့်နေရာကို ဆုံးဖြတ်သည်။ | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| host-agent အတွက် ဘာသာပြန်ရန် အကြောင်းအရာ ပြင်ဆင်ခြင်း | သင့် MCP host သို့မဟုတ် application model မှ chunk များကို ဘာသာပြန်ပြီး၊ Co-op Translator သည် chunk ခွဲခြားခြင်းနှင့် ပြန်လည်တည်ဆောက်ခြင်းကို ကိုင်တွယ်ပေးသည်။ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Repository တစ်ခုလုံး ဘာသာပြန်ခြင်း | Python API ကို CLI ကဲ့သို့ လုပ်ဆောင်စေပြီး ရှာဖွေမှု၊ အထွက်လမ်းကြောင်းများ၊ မက်တာဒေတာ၊ ရှင်းလင်းခြင်း နှင့် ဖိုင်ရေးသိမ်းခြင်းများကို ကိုင်တွယ်စေလိုသည်။ | `run_translation` |

`core`, `config`, `review`, and `utils` အောက်ရှိ အနိမ့်အဆင့် modules အများစုသည် ဤ API ဝင်ပေါက်များတွင် အသုံးပြုသည့် အကောင်အထည်ဖော် အသေးစိတ်များဖြစ်ပါသည်။

MCP client များသည် [MCP Server](mcp.md) မှတဆင့် တူညီသော ပြည်သူ့ API ကို အသုံးပြုကြသည်။ Python ကို တိုက်ရိုက် ခေါ်သုံးသောအခါ ဤစာမျက်နှာကို အသုံးပြုပါ၊ Co-op Translator ကို agent သို့မဟုတ် editor တွင် ဖော်ပြချင်သည်များအတွက် MCP လမ်းညွှန်ကို အသုံးပြုပါ။ CLI, Python API နှင့် MCP အကြား ရွေးချယ်ရန် ဆုံးဖြတ်နေပါက [သင့်လုပ်ငန်းစဉ်ကို ရွေးချယ်ပါ](workflows.md) မှ စတင်ပါ။

## ပထမဆုံး API လည်ပတ်မှု

Python ကုဒ်မှ Co-op Translator ကို ခေါ်ဆိုမည့်အခါ ဤနေရာမှ စတင်ပါ။

1. [Configuration](configuration.md) တွင် ဖော်ပြထားသည့်အတိုင်း LLM provider ကို သတ်မှတ်ပါ၊ သင်သည် host-agent ဘာသာပြန်ရေးအတွက် Markdown သို့မဟုတ် notebook chunks များကိုသာ ပြင်ဆင်နေပါက မလိုအပ်ပါ။
2. သင်၏ အက်ပလီကေးရှင်းသည် ဖိုင် I/O ကို ပိုင်ဆိုင်မလား ဆုံးဖြတ်ပါ။
3. သင့်အက်ပ်လိကေးရှင်းသည် ဖိုင် တစ်ဖိုင်ချင်းကို ဖတ်ခြင်းနှင့် ရေးသိမ်းခြင်းလုပ်ဆောင်သောအခါ content API များကို အသုံးပြုပါ။
4. Co-op Translator က CLI ကဲ့သို့ repository တစ်ခုကို ပြုပြင်လည်ပတ်သင့်လျှင် `run_translation` ကို အသုံးပြုပါ။
5. အော်တိုမေးရှင်းတွင် သတ်မှတ်နိုင်သည့် စစ်ဆေးမှုများ လိုအပ်ပါက ဘာသာပြန်ပြီးနောက် `run_review` ကို အသုံးပြုပါ။

| Goal | API to start with |
| --- | --- |
| Markdown စာသားတစ်ခု သို့မဟုတ် ဖိုင် တစ်ခုကို ဘာသာပြန်ပါ | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| host agent ကို Markdown သို့မဟုတ် notebook အပိုင်းများကို ဘာသာပြန်စေပါ | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| output path ကို ရွေးချယ်ပြီးနောက် ဘာသာပြန်ထားသော လင့်ခ်များကို ပြန်ရေးပါ | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## အခြေအနေ 1: တစ်ဖိုင်ချင်း သို့မဟုတ် စာရွက်စာတမ်းများ ဘာသာပြန်ခြင်း

ဖိုင်၊ editor buffer၊ notebook payload၊ MCP request သို့မဟုတ် custom pipeline input တစ်ခုခုကို ရှိပြီးသားဖြစ်သောအခါ ဤ workflow ကို အသုံးပြုပါ။ သင့်ကုဒ်မှ ဖိုင် I/O ကို ကိုင်တွယ်ပါသည်။

1. Read the source content.
2. Call a content translation API.
3. ဘာသာပြန်ထားသော အကြောင်းအရာကို project translation ဖိုလ်ဒါထဲသို့ ရေးသွင်းမည်ဆိုပါက လမ်းကြောင်းပြန်ရေး API ကို လိုအပ်သလို ခေါ်ပါ။
4. သင်၏ အက်ပလီကေးရှင်းမှ ရရှိသော ရလဒ်ကို သိမ်းဆည်းပါ သို့မဟုတ် ပြန်ပေးပို့ပါ။

Content translation API များသည် project discovery ကို မပြုလုပ်ပါ၊ metadata မရေးပါ၊ disclaimers မထည့်ပါ၊ နှင့် links များကို အလိုအလျောက် ပြန်ရေးမလုပ်ပါ။

### Markdown ဖိုင်

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


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
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

ဘာသာပြန်ထားသော Markdown ကို Co-op Translator project အစီအစဉ်အလှည့်တန်းတွင် မတာဝန်ခံမရှိချင်ပါက `rewrite_markdown_paths` ကို ဖြတ်ပြီး ဘာသာပြန်ထားသော string ကို တိုက်ရိုက် သိမ်းဆည်းပါ။

### Notebook ဖိုင်

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` သည် Markdown ဆဲလ်များကို ဘာသာပြန်ပေးပြီး non-Markdown ဆဲလ်များကို ထိန်းသိမ်းထားသည်။ လမ်းကြောင်း ပြန်ရေးခြင်းကို Markdown ဆဲလ်များတွင်ပင်သာ သက်ရောက်ပါသည်။

### ပုံဖိုင်

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` သည် မူလ ရုပ်ပုံကို ဖတ်ပြီး ဖော်ပြထားသော `PIL.Image.Image` ကို ပြန်လည်ပေးသည်။ ဘာသာပြန်ထားသော ရုပ်ပုံ metadata ကို မရေးထည့်ပါ။

## အခြေအနေ 2: Repository တစ်ခုလုံးကို ဘာသာပြန်ခြင်း

Python API ကို `translate` CLI ကဲ့သို့ အလုပ်လုပ်စေချင်ပါက ဤ workflow ကို အသုံးပြုပါ။ `run_translation` သည် supported files များကို ရှာဖွေ၍ ရွေးချယ်ထားသော content အမျိုးအစားများကို ဘာသာပြန်ပြီး လမ်းကြောင်းများကို ပြန်ရေး၊ output ဖိုင်များကို ရေးသား၊ metadata ကို အပ်ဒိတ်လုပ်၊ နှင့် cleanup စသည်တို့ကဲ့သို့သော ဘာသာပြန် ထိန်းသိမ်းမည့် လုပ်ငန်းများကို ဆောင်ရွက်ပါသည်။

`run_translation` သည် project orchestration အတွက် ဦးစားပေးအသုံးပြုရန် အဝင်ပေါက်ဖြစ်သည်။ `translate_project` ကို ဆင်တူ အလုပ်ဆောင်နိုင်သော compatibility alias အဖြစ် ထုတ်ပေးထားသည်။

ယခု repository အတွင်းရှိ Markdown ဖိုင်များကို ကိုရီးယားနှင့် ဂျပန် ဘာသာသို့ ဘာသာပြန်ပါ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

တိကျသော project root အောက်မှ notebooks များကိုသာ ဘာသာပြန်ပါ။

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

ဖိုင်များ မရေးဘဲ ဘာသာပြန်ပမာဏကို ကြိုတင် ကြည့်ရှုရန်:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

ပေါင်းစည်းမှုအတွက် ဖွဲ့စည်းထားသော တိုးတက်မှု ဖြစ်ရပ်များကို မှတ်တမ်းတင်ရန်:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # payload ကို သင့် job-event ဇယားထဲသို့ သိမ်းဆည်းပါ သို့မဟုတ် သင့် UI သို့ တိုက်ရိုက်လွှင့်ပို့ပါ။


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Events use the versioned schema `co-op.translation.event.v1`. Integrations should
depend on stable fields such as `type` and `stage_key`, not on human-facing
console text or `stage_label`.

တစ်ခေါက်ခေါ်ဆိုခြင်းဖြင့် အမျိုးမျိုးသော အကြောင်းအရာ ရင်းမြစ်များကို ဘာသာပြန်ပါ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

ဘာသာပြန်ချက်များကို သတ်မှတ်ထားသော ထုတ်လွှတ်အုပ်စုများထဲသို့ ရေးထည့်ရန်:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

ဘာသာစကားတစ်ခုချင်းစီအတွက် nested subdirectory ပါရှိသင့်သော အခါ တိုင်းဘာသာအတွက် placeholder တစ်ခုကို အသုံးပြုပါ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

`markdown`, `notebook`, သို့မဟုတ် `images` တစ်ခုမျှ သတ်မှတ်ထားခြင်း မရှိပါက API သည် ပံ့ပိုးထားသည့် အမျိုးအစားအားလုံးကို ဘာသာပြန်ပါသည်: Markdown, notebooks, and images.

### လက်ခံထားသော လူ့ပြင်ဆင်မှုများကို ဘာသာပြန် အခြေအနေ ပေးသူဖြင့် ထိန်းသိမ်းပါ

ပုံမှန်အနေဖြင့် Co-op Translator သည် ရှိပြီးသား ဖိုင်အဆင့် အပြုအမူကို ထိန်းသိမ်းထားသည်။ အခါတစ်ခုတွင်
Markdown အရင်းအမြစ် သက်ဆီးနေသည်ဆိုလျှင်၊ ဘာသာပြန်ပြီးသား ဖိုင်အားလုံးကို ထပ်မံဖန်တီးသည်။ Hosted
integrations များသည် ရွေးချယ်စွာ `TranslationStateProvider` ကို ပေးပို့၍ လူ့
မပြောင်းလဲဘဲရှိသော မူရင်းဘလော့များအတွင်း လူ့ပြင်ဆင်ချက်များကို ထိန်းသိမ်းနိုင်သည်။

provider သည် နောက်ဆုံးလက်ခံထားသော မူရင်း/ပစ်မှတ် အစုံကို ထောက်ပံ့ပေးပြီး အသစ်
လျှောက်လွှာ။ လက်ခံခြင်းသည် ပေါင်းစည်းမှု၏ တာဝန်ဖြစ်နေဆဲဖြစ်ပြီး—ဥပမာအားဖြင့်၊
ဘာသာပြန်ရန် pull request ကို merge ပြီးနောက်:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

လက်ခံထားသော အခြေခံလိုင်း (baseline) မှန်ကန်သော Markdown ဖိုင်များအတွက်၊ Co-op Translator သည်
ထိပ်တန်း Markdown ဘလော့များကို ကိုက်ညီစေသည်။ မူရင်း မပြောင်းလဲသော ဘလော့များသည် လက်ရှိ ဘာသာပြန်ထားသော
ဘလော့များကို ပြန်လည်အသုံးပြုသည်၊ လူများက ပြုလုပ်ထားသော ပြင်ဆင်ချက်များပါဝင်သည်; ပြောင်းလဲသို့မဟုတ် ထပ်ဆောင်းထားသော မူရင်း ဘလော့များကို ပို့၍
ဘာသာပြန်ရန်; ဖျက်ပြီးသော မူရင်း ဘလော့များကို ဖယ်ရှားပစ်သည်။ တန်းညှိခြင်း ရှုပ်ရှပ်ပါက、
ပစ်မှတ် ဖွဲ့စည်းပုံ ပြောင်းလဲသွားခြင်း၊ ဘလော့ ဘာသာပြန်ချက် မမှန်ကန်ခြင်း သို့မဟုတ် baseline မရရှိနိုင်ခြင်း ဖြစ်ပါက
ရရှိနိုင်ခြင်းမရှိပါက၊ Co-op Translator သည် လုံခြုံစိတ်ချစွာ ရှိပြီးသား ဖိုင်လုံးဝ
ဘာသာပြန်ခြင်း လမ်းကြောင်းသို့ ပြန်လျှောက်မည်။

ဤ API သည် စာရွက်စာတမ်း ဘာသာပြန် အခြေအနေကို သိမ်းဆည်းသည်၊ စာရွက်စာတမ်းများကြား စကားစု သို့မဟုတ်
segment translation memory မဟုတ်ပါ။ ယခုအချိန်တွင် Markdown project ဘာသာပြန် လုပ်ငန်းတွင်သာ သက်ရောက်သည်။
Notebook နှင့် ပုံဆိုင်ရာ အပြုအမူများ မပြောင်းလဲပါ။ Passing `update=True`
ထပ်မံ ပြန်လည်ဖန်တီးရန် ဆက်လက်တောင်းဆိုပါသည်။

တစ်ဖိုင် သို့မဟုတ် အများပိုင်း ဖိုင်များကို ဘာသာပြန်၍ မရနိုင်ပါက၊ `run_translation` သည်
`RuntimeError` ကို project workflow ပြီးဆုံးချိန်တွင် ထုတ်ပေးမည်ဖြစ်ပြီး၊
မရှိသည့် အထွက်(output)နဲ့ တကယ်အောင်မြင်သည်ဟု တင်ပြခြင်းကို မပြုဘဲ、
ပေါင်းစည်းမှုများသည် ဤအမှုကို မအောင်မြင်သော အလုပ်တစ်ခုအဖြစ် သတ်မှတ်၍ ယခင် လက်ခံထားသော ဘာသာပြန် အခြေအနေကို ထိန်းသိမ်းသင့်သည်။

## ဘာသာပြန်ပြီး အထွက်ကို ပြန်စစ်ပါ

`run_review` သည် LLM သို့မဟုတ် Vision ခွင့်ပြုချက်များမလိုဘဲ သတ်မှတ်ထားသော ဘာသာပြန် စစ်ဆေးမှုများကို အလုပ်လုပ်စေသည်။

!!! note "ဘီတာ"
    `run_review` သည် ဘီတာ အဆင့်ရှိ သတ်မှတ်ထားသော ပြန်လည်စစ်ဆေးရေး API တစ်ခု ဖြစ်သည်။ ၎င်းသည် မော်ဒယ်ပံ့ပိုးသူများကို ခေါ်မည် မဟုတ်၍ ဖိုင်များကို မရေးသားပါ၊ သို့သော် စစ်ဆေးမှုများနှင့် ပြဿနာဖွဲ့စည်းပုံများတွင် ပြောင်းလဲမှုရှိနိုင်ပါသည်။

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

README ဖိုင်သာ ဘာသာပြန်ပြီးနောက်၊ အဲဒီနယ်ပယ်ကို ဆန်းစစ်ရန် တူညီစွာ အသုံးပြုပါ။

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` reviews only `README.md` under each configured source root,
including custom `groups` and output directories. Other documents and nested
READMEs are excluded. A missing source README raises `ValueError`; failed
translation checks raise `RuntimeError`.

base ref နှင့် နှိုင်းယှဉ်၍ ပြောင်းလဲထားသော ဖိုင်များကိုသာ ပြန်လည်စစ်ဆေးပြီး GitHub-စတိုင်း အထွက်ကို ထုတ်ပါ။

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## ကူးထည့်နိုင်သော API ဥပမာများ

ဖိုင်များကို မရေးဘဲ Markdown အကြောင်းအရာများကို ဘာသာပြန်ရန်:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Translate and rewrite Markdown links:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Translate a repository from Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Translate multiple roots:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

Preserve glossary terms:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## အများပြည်သူအသုံးပြုနိုင်သော ဝင်ပေါက်များ

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## အကြောင်းအရာ ဘာသာပြန် API များ

Content translation APIs များကို ပြင်ဆင်ကိရိယာချဲ့ထွင်မှု (editor extension), MCP tool, notebook processor, သို့မဟုတ် custom pipeline ကဲ့သို့ မီမိုရီထဲတွင် အကြောင်းအရာရှိပြီးသား ပေါင်းစည်းမှုများ အတွက် ရည်ရွယ်ထားပါသည်။

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | မရှိပါ | အဆက်မပြတ် (Async). Markdown အကြောင်းအရာများကိုသာ ဘာသာပြန်သည်။ လင့်ခ်များကို ပြန်ရေးခြင်း၊ မီတာဒေတာရေးခြင်း သို့မဟုတ် အသိပေးချက်များ ထပ်ထည့်ခြင်း မရှိပါ။ |
| `translate_notebook_content` | Notebook JSON `str` သို့မဟုတ် `dict` | Notebook JSON `str` | မရှိပါ | အဆက်မပြတ် (Async). Markdown cell များကို ဘာသာပြန်ပြီး Markdown မဟုတ်သော cell များကို ထိန်းသိမ်းထားသည်။ လင့်ခ်များ ပြန်ရေးခြင်း၊ မီတာဒေတာရေးခြင်း သို့မဟုတ် အသိပေးချက် ထပ်ထည့်ခြင်း မရှိပါ။ |
| `translate_image_content` | ပုံလမ်းကြောင်း | `PIL.Image.Image` | မူရင်းပုံကိုသာ ဖတ်သည် | တပြိုင်နက် (Synchronous). ပုံမှ စာသားကို ထုတ်ယူ၍ ဘာသာပြန်ကာ ပြန်လည်ပုံဖော်ထားသော ပုံကို ထုတ်ပေးသည်။ ဘာသာပြန်ပြီးသော ပုံ၏ မီတာဒေတာကို သိမ်းဆည်းမှု မရှိပါ။ |

`translate_markdown_content` နှင့် `translate_notebook_content` သည် သူတို့၏ options မှတဆင့် ရွေးချယ်ထည့်နိုင်သည့် `source_path` ကို လက်ခံသည်။ လမ်းကြောင်းကို ဘာသာပြန်သူထံ context အဖြစ် ပေးပို့သည်; ခေါ်သုံးသူများသည် ဘာသာပြန်ပြီးနောက် စီမံကိန်းအထူး လမ်းကြောင်းပြန်ရေးခြင်းအတွက် တာဝန်ရှိနေပါသည်။

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

တူညီသော ရွေးချယ်စရာများကို dictionary များအဖြစ် ပေးပို့နိုင်သည်:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent အကူအညီဖြင့် ဘာသာပြန် API များ

Agent-assisted API များသည် Co-op Translator မှ ပြင်ဆင်ထားသည့် LLM provider ကို ခေါ်သုံး မည်မဟုတ်ပါ။ ၎င်းတို့သည် host agent အတွက် ဘာသာပြန်ရန် Markdown သို့မဟုတ် notebook ခွဲအစိတ်အပိုင်းများကို ပြင်ဆင်ပြီး၊ ဘာသာပြန်ပြီးသော ချန့်များမှ နောက်ဆုံး အကြောင်းအရာကို ပြန်လည်တည်ဆောက် ပေးသည်။

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | ကိုယ်ပိုင်ပြည့်စုံသော Markdown job တစ်ခုကို chunks၊ prompts နှင့် ပြန်လည်တည်ဆောက်မှု အခြေအနေတို့နှင့်အတူ ပြန်ပေးသည်။ |
| `finish_markdown_agent_translation` | job နှင့် host-agent ဖြင့် ဘာသာပြန်ထားသော chunks များမှ Markdown ကို ပြန်လည်တည်ဆောက်သည်။ |
| `start_notebook_agent_translation` | host-agent အတွက် ဘာသာပြန်ရန် Markdown-cell ချန့်များပါရှိသည့် notebook job တစ်ခုကို ပြန်ပေးသည်။ |
| `finish_notebook_agent_translation` | code cells၊ outputs နှင့် metadata များကို ထိန်းသိမ်းထားပြီး notebook JSON ကို ပြန်လည်တည်ဆောက်သည်။ |

ဤ workflow သည် အဓိကအားဖြင့် MCP hosts များအတွက် ရည်ရွယ်ထားသည်။ Co-op Translator မှ provider calls များကို စီမံပေးသော production repository ဘာသာပြန်မှု လိုအပ်ပါက `translate_markdown_content`, `translate_notebook_content`, သို့မဟုတ် `run_translation` ကို အသုံးပြုပါ။

## လမ်းကြောင်း ပြန်ရေးသားခြင်း API များ

Path rewriting APIs မည်သည့် ဘာသာပြန်မှုကိုမျှ မလုပ်ဆောင်ပါ။ callers များ source path၊ translated target path နှင့် project layout ကို သိရှိပြီးနောက်တွင် ၎င်းတို့သည် links နှင့် frontmatter paths များကို အပ်ဒိတ် ပြုလုပ်ပေးသည်။

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown ကိုယ်ထည်နှင့် frontmatter | ဘာသာပြန်ထားသော target အတွက် Markdown links များနှင့် ထောက်ခံထားသော frontmatter path ကဏ္ဍများကို ပြန်ရေးသားပေးသည်။ |
| `rewrite_notebook_paths` | notebook JSON တွင်ရှိသည့် Markdown ကွက်များ | Markdown ကွက် တစ်ခုချင်းစီတွင် Markdown path ပြန်ရေးခြင်းကို သက်ရောက်စေပြီး non-Markdown ကွက်များကို မပြောင်းလဲဘဲ ထားရှိသည်။ |

`policy` ဆိုသော argument သည် အောက်ပါ field များပါဝင်သည့် dictionary တစ်ခု ဖြစ်နိုင်သည်:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | မဟုတ်ပါ | ဖွင့်ထားသော ဘာသာပြန် အမျိုးအစားများ။ ပုံမှန်အားဖြင့် Markdown, notebooks, နှင့် images များ ဖြစ်သည်။ |
| `lang_subdir` | မဟုတ်ပါ | ဘာသာစကား ဖိုလ်ဒါတိုင်းအောက်ရှိ ရွေးချယ်နိုင်သော subdirectory တစ်ခု။ |

## ပရောဂျက် ဘာသာပြန် ပါရာမီတာများ

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | လိုအပ်သည် | အကွာသတ်ထားသော ရည်ရွယ်ဘာသာစကားကုဒ်များ၊ ဥပမာ `"ko ja fr"` သို့မဟုတ် `"all"`။ Alias ကုဒ်များကို canonical BCP 47 တန်ဖိုးများအဖြစ် ပုံမှန်ပြုလုပ်သည်။ |
| `root_dir` | `str` | `"."` | တစ်ခုတည်းသော ဘာသာပြန် ရည်ရွယ်ချက်အတွက် project root ဖြစ်သည်။ `root_dirs` သို့မဟုတ် `groups` များ ပေးထားလျှင် ဤသည်ကို မထည့်စဉ်းစားပါ။ |
| `update` | `bool` | `False` | ရွေးချယ်ထားသော ဘာသာစကားများအတွက် ရှိပြီးသား ဘာသာပြန်ချက်များကို ဖျက်ပြီး ထပ်မံဖန်တီးသည်။ |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | DEBUG အဆင့် လော့ဂ် ဖိုင်များကို root `logs/` ဖိုလ်ဒါအောက်တွင် သိမ်းဆည်းပါ။ |
| `yes` | `bool` | `True` | ပ႐ိုဂရမ်ဆိုင်ရာနှင့် CI အသုံးပြုမှုများအတွက် တုံ့ပြန်ချက်များကို အလိုအလျောက် အတည်ပြုပါ။ |
| `add_disclaimer` | `bool` | `False` | ဘာသာပြန်ထားသော Markdown နှင့် notebook များတွင် စက်ဘာသာပြန် သတိပေးချက်များကို ထည့်ပါ။ |
| `translations_dir` | `str \| None` | `None` | စာသားဘာသာပြန်ထွက်ဖိုင်များအတွက် စိတ်ကြိုက် ဒိုင်ရက်ထရီ။ ဆက်စပ် လမ်းကြောင်းများကို တစ်ခုချင်း root အပေါ်မှ ဖြေရှင်းသည်။ |
| `image_dir` | `str \| None` | `None` | ဘာသာပြန်ထားသော ပုံဖိုင်များအတွက် စိတ်ကြိုက် ထွက်ပေါက် ဒိုင်ရက်ထရီ။ ဆက်စပ် လမ်းကြောင်းများကို တစ်ခုချင်း root အပေါ်မှ ဖြေရှင်းသည်။ |
| `root_dirs` | `Iterable[str] \| None` | `None` | ထွက်ဖိုင် ဆက်တင်များကို မျှဝေသော အမျိုးမျိုးသော root များ။ |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | ရှင်းလင်း ဖော်ပြထားသော `(root_dir, translations_dir)` စုံတွဲများ။ `root_dirs` ထက် ဦးစားပေးသတ်မှတ်ခြင်းဖြစ်သည်။ |
| `repo_url` | `str \| None` | `None` | README ဘာသာစကားဇယား ညွှန်ကြားချက်များကို ပြသရာတွင် အသုံးပြုမည့် repository URL။ |
| `glossaries` | `Iterable[str] \| None` | `None` | ဘာသာပြန်ချိန်တွင် ထိန်းသိမ်းရန် glossary ဆိုင်ရာ စကားလုံးများ။ ထပ်တူနှင့် ရှင်းလင်းမရှိသော စကားလုံးများကို စံသတ်မှတ်ပါသည်။ |
| `dry_run` | `bool` | `False` | ဖိုင်များ မရေးဘဲ ဘာသာပြန်ပမာဏ ခန့်မှန်းပြီး ပြောင်းရွှေ့ အပြုအမူကို အကြို ကြည့်ရှုရန်။ |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | ရွေ့လျားသည့် Markdown အပ်ဒိတ်များအတွက် ရွေးချယ်နိုင်သည့် accepted-baseline နှင့် candidate persistence adapter။ မထည့်ပါက သာမန် ဖိုင်လုံးတစ်ခုလုံး လုပ်ဆောင်မှုကို ဆက်လက်ထိန်းသိမ်းမည်။ |

## ပြန်လည်သုံးသပ်ခြင်း ဆိုင်ရာ ပါရာမီတာများ

`run_review` ကို ဖြစ်နိုင်သလောက် `run_translation` ၏ signature နှင့် သက်ဆိုင်အောင် ထားသည်။ ထို့ကြောင့် automation များသည် ဘာသာပြန်ခြင်းနှင့် ပြန်လည်သုံးသပ်ခြင်း လုပ်ငန်းစဉ်များကို အနည်းဆုံး branching ဖြင့် ပြောင်းလဲနိုင်သည်။

| ပါရာမီတာ | အမျိုးအစား | ပုံမှန်တန်ဖိုး | ရည်ရွယ်ချက် |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | သုံးသပ်ရန် ရည်ညွှန်းထားသော ဘာသာစကား ဖိုလ်ဒါများ။ space-separated string များနှင့် iterable များကို လက်ခံသည်။ `"all"` သည် တွေ့ရှိသော ဘာသာပြန် ဘာသာစကားအားလုံးကို သုံးသပ်သည်။ |
| `root_dir` | `str` | `"."` | တစ်ခုသော သုံးသပ်ရန် အလေးထားသည့် target အတွက် project root ဖြစ်သည်။ `root_dirs` သို့မဟုတ် `groups` ကို ဖြည့်သွင်းထားပါက မယူဆောင်ပါ။ |
| `markdown` | `bool` | `False` | Markdown နှင့် MDX မူရင်းဖိုင်များကို ပါဝင်စေသည်။ |
| `notebook` | `bool` | `False` | Jupyter notebook မူရင်းဖိုင်များကို ပါဝင်စေသည်။ |
| `images` | `bool` | `False` | ဘာသာပြန်ရွေးချယ်မှုများနှင့် ကိုက်ညီမှုအတွက် ရှိထားသည်။ ပုံများဆိုင်ရာ link ကို Markdown မှ စစ်ဆေးသည်။ |
| `translations_dir` | `str \| None` | `None` | စာသားဘာသာပြန်ထွက်ဖိုင်များအတွက် စိတ်ကြိုက် ဒိုင်ရက်ထရီ။ ဆက်စပ် လမ်းကြောင်းများကို တစ်ခုချင်း root အပေါ်မှ ဖြေရှင်းသည်။ |
| `root_dirs` | `Iterable[str] \| None` | `None` | ထွက်ဖိုင် ဆက်တင်များကို မျှဝေသော အမျိုးမျိုးသော root များ။ |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | ရှင်းလင်း ဖော်ပြထားသော `(root_dir, translations_dir)` စုံတွဲများ။ `root_dirs` ထက် ဦးစားပေးသတ်မှတ်ခြင်းဖြစ်သည်။ |
| `changed_from` | `str \| None` | `None` | ပြောင်းလဲထားသော မူရင်းဖိုင်များကိုသာ သုံးသပ်ရန် အကန့်အသတ်ထားရန် အသုံးပြုသော Git ref။ |
| `readme_only` | `bool` | `False` | `README.md` သာ သုံးသပ်မည်။ အဓိက source README မရှိပါက `ValueError` ကို ထုတ်ပေးမည်။ |
| `output_format` | `str` | `"text"` | သုံးသပ်မှု ထွက်ပေါက် ဖော်မတ်။ ထောက်ခံသည့် တန်ဖိုးများမှာ `"text"` နှင့် `"github"` ဖြစ်သည်။ |
| `fail_on_warnings` | `bool` | `False` | သတိပေးချက်များကို အမှားများအနေဖြင့်သာမက မအောင်မြင်မှုအဖြစ်လည်း ယူဆမည်။ |
| `debug` | `bool` | `False` | debug logging ကို ဖွင့်ပါ။ |
| `save_logs` | `bool` | `False` | root `logs/` ဒိုင်ရက်ထရီအောက်တွင် DEBUG-level log ဖိုင်များကို သိမ်းဆည်းပါ။ |

`markdown`၊ `notebook` သို့မဟုတ် `images` တို့သည် မည်သို့မျှ သတ်မှတ်မထားပါက API သည် နယ်ပယ်သင့်သောနေရာများတွင် Markdown၊ notebook များနှင့် ပုံ link မှတ်တမ်းများကို သုံးသပ်သည်။ ပြန်လည်သုံးသပ်ခြင်းသည် LLM provider ကို ခေါ်ဆိုခြင်းမပြုသော်လည်း API key များ လိုအပ်မည် မဟုတ်ပါ။ |

## ဖွဲ့စည်းပုံ လိုအပ်ချက်များ

Provider support ရှိသော ဘာသာပြန် API များသည် ဘာသာပြန်မလုပ်မီ provider ဖော်ပြချက်များကို လိုအပ်သည်။

- Markdown နှင့် notebook ဘာသာပြန်ခြင်းအတွက် LLM provider လိုအပ်သည်။ Azure OpenAI၊ OpenAI သို့မဟုတ် Anthropic ကို ဖော်ပြပါ။
- ပုံဘာသာပြန်ရန် LLM provider အပြင် Azure AI Vision လည်း လိုအပ်သည်။
- `run_translation` သည် project ဘာသာပြန်မှု စတင်မည့်အောက်တွင် အလွယ်တကူ ချိတ်ဆက်နိုင်မှု စစ်ဆေးမှုများကို လုပ်ဆောင်သည်။
- Agent ဖြင့် ကူညီသည့် `start_*_agent_translation` နှင့် `finish_*_agent_translation` API များသည် Co-op Translator LLM provider များကို ခေါ်ယူသော မဟုတ်ပါ။ Host application သို့မဟုတ် MCP agent က ပြင်ဆင်ထားသော chunks များကို ဘာသာပြန်ပေးသည်။
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` သည် သတ်မှတ်ထားသည့် အမှုများဖြစ်ပြီး provider အတည်ပြုချက်များ မလိုအပ်ပါ။

လိုအပ်သော Azure OpenAI environment variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

လိုအပ်သော OpenAI environment variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

လိုအပ်သော Anthropic variables:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` နှင့် `ANTHROPIC_MAX_TOKENS` များသည် ရွေးချယ်စရာဖြစ်သည်။ Co-op Translator 0.22.0 မှစ၍ သတ်မှတ်ထားသော provider များအတွက် Microsoft Agent Framework သည် ပုံမှန် model client ဖြစ်သည်။ Semantic Kernel ကို ယာယီ သတ်မှတ်ရန် `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` ကို အသုံးပြုနိုင်သော်လည်း၊ ထိုသုံးစွဲမှုသည် deprecation သတိပေးချက်ကို ထုတ်ပေးမည်။ ဖျက်ဆီးခြင်းကို အဆင့်လိုက် လုပ်ဆောင်ရန် အစီအစဉ်ကို ကြည့်ရန် [configuration](configuration.md#model-client-backend) ကို ကြည့်ပါ။ |

ပုံဘာသာပြန်ခြင်းအတွက် လိုအပ်သော Azure AI Vision variables:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` သည် သတ်မှတ်ထားသည့် အလုပ်စဉ်ဖြစ်ပြီး LLM သို့ Azure AI Vision ဖော်ပြချက်များ မလိုအပ်ပါ။ |

## အပြုအမူ ဆိုင်ရာ မှတ်ချက်များ

- အကြောင်းအရာ ဘာသာပြန် API များသည် ဘာသာပြန်ခြင်းကို project လမ်းကြောင်း ပြန်ရေးခြင်းနှင့် သီးခြားထားသည်။ ဘာသာပြန်ထားသော အကြောင်းအရာများအတွက် project-relative link များကို ညှိလိုလျှင် `rewrite_markdown_paths` သို့မဟုတ် `rewrite_notebook_paths` ကို ထပ်မံ ခေါ်ပါ။ |
- Project orchestration API များသည် ဖိုင် ရှာဖွေခြင်း၊ ဖိုင်ရေးသွင်းခြင်း၊ လမ်းကြောင်း ပြန်ရေးခြင်း၊ metadata၊ သန့်ရှင်းရေးနှင့် ရွေးချယ်စရာ ပေါ်လာနိုင်သည့် သတိပေးချက်များ အပါအဝင် အကြောင်းအရာ ဘာသာပြန်ခြင်းဆိုင်ရာ project အပြုအမူများကို ထည့်သွင်းသည်။ |
- `run_translation` သည် CLI မှ အသုံးပြုသည့် Rich-backed reporter တူညီသည်ကို အသုံးပြုပြီး တိုးတက်မှုနှင့် ခန့်မှန်းချက် အကျဉ်းချုပ်များကို ပရင့်ထုတ်သည်။ အပြန်အလှန် မလိုအပ်သော output များတွင် plain text ကို အသုံးပြုမည်။ |
- `dry_run=True` သည် virtual README အပ်ဒိတ်များကို အသုံးပြု၍ ခန့်မှန်းချက်များကို ကဏ္ဍခွဲသည်၊ သို့သော် README သို့မဟုတ် ဘာသာပြန်ဖိုင်များကို မရေးပါ။ |
- `groups` များကို အဆက်တိုက် ဆောင်ရွက်သည်။ အလုပ်စတင်မီ တစ်ခုတည်းသော စုစုပေါင်း ခန့်မှန်းချက်တစ်ခုကို ပရင့်ထုတ်သည်။ |
- ပုံဘာသာပြန်ရွေးချယ်ထားပါက Vision ဖော်ပြချက် မရှိခြင်းသည် ဘာသာပြန်ခြင်း စတင်မီ အမှားတစ်ခုကို ထုတ်ပေးမည်။ |
- ရှိပြီးသား alias-အခြေပြု ဘာသာစကား ဖိုလ်ဒါများကို တွေ့ရှိနိုင်ပြီး run အတွင်း canonical language folder names များသို့ ပြောင်းရွှေ့နိုင်သည်။ |
- `run_review` သည် ဘာသာပြန်ထားသော ဖိုင်များ မရှိခြင်း၊ ဘာသာပြန် metadata မရှိခြင်း သို့မဟုတ် ပျက်ကွက်နေခြင်း၊ Markdown frontmatter/code fence မမှန်ကန်ခြင်းနှင့် ဘာသာပြန်ထားသော notebook JSON မတရားခြင်းတို့တွင် မအောင်မြင်ပါ။ |
- `run_review` သည် ဒေသဆိုင်ရာ Markdown နှင့် ပုံ link ဖြစ်ပေါ်မှု မရှိမှုများကို ပုံမှန်အားဖြင့် သတိပေးချက်များအဖြစ် အသိပေးသည်။ |

## အတွင်းခေါ်ယူမှု လမ်းကြောင်း

API သည် CLI မှ အသုံးပြုသည့် အဓိက implementation ကို အသုံးပြု၍ လက်လှမ်းပေးသည်။

ဘာသာပြန်မှု:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` အတွက် in-memory ဘာသာပြန်သည်။ |
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` အတွက် လမ်းကြောင်း post-processing ဖော်ပြချက်။ |
3. `co_op_translator.api.translation.run_translation` အတွက် project အပြည့်အစုံ စီမံခန့်ခွဲရေး။ |
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`. |
5. `co_op_translator.core.project.ProjectTranslator`. |
6. `co_op_translator.core.project.TranslationManager`. |
7. Markdown, notebooks, နှင့် images အတွက် အထူး သတ်မှတ်ထားသော project translation mixins များ။ |
8. `co_op_translator.core` အောက်ရှိ Markdown, notebook, text, နှင့် image translators။ |

ပြန်လည်သုံးသပ်ခြင်း:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` အောက်ရှိ သတ်မှတ်ထားသည့် စစ်ဆေးချက်များ |

အောက်ပါ class များသည် မှုန့်ထိန်းသူများအတွက် အသုံးဝင်သော်လည်း package-level stable API အဖြစ် export မလုပ်ထားပါ။ |

| အတန်း | မော်ဒျူး | တာဝန် |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | project အဆင့် ဘာသာပြန်ခြင်းကို ပူးပေါင်းညှိနှိုင်းသည်၊ ဒိုင်ရက်ထရီ စီမံခန့်ခွဲမှု၊ တစ်ဘာသာစကားလျှင် metadata ကို စံပြုထားသည့်ပုံစံသို့ ပြန်လည်တင်းကြပ်ခြင်း၊ နှင့် Markdown၊ notebook၊ နှင့် image translators သို့ တာဝန်ပေးပိုက်ခြင်းတို့ကို ဆောင်ရွက်သည်။ |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown၊ notebook များ၊ ပုံများ၊ stale တွေ့ရှိရေးနှင့် ဘာသာပြန် metadata အပ်ဒိတ်များအတွက် async ဖိုင် ကိုင်တွယ်မှု အလုပ်များကို ဆောင်ရွက်သည်။ |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown ဖိုင် ဖတ်ယူခြင်း၊ အကြောင်းအရာ ဘာသာပြန်ခြင်း၊ လမ်းကြောင်း ပြန်ရေးခြင်း၊ metadata၊ သတိပေးချက်များနှင့် ဖိုင်ရေးသွင်းခြင်းတို့ကို စီမံခန့်ခွဲသည်။ |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | notebook ဖိုင်ဖတ်ယူခြင်း၊ Markdown-cell ဘာသာပြန်ခြင်း၊ လမ်းကြောင်း ပြန်ရေးခြင်း၊ metadata၊ သတိပေးချက်များနှင့် ဖိုင်ရေးသွင်းခြင်းတို့ကို စီမံခန့်ခွဲသည်။ |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | မူရင်းပုံများ ရှာဖွေခြင်း၊ ပုံဘာသာပြန်ခြင်း၊ ထွက်ဖိုင်လမ်းကြောင်းများ၊ metadata နှင့် ဖိုင်ရေးသွင်းခြင်းတို့ကို စီမံခန့်ခွဲသည်။ |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | ဘာသာပြန်ထားသော Markdown စုံတွဲများကို ရှာဖွေပြီး ဘာသာပြန်အရည်အသွေးကို တင်ပြသုံးသပ်ကာ ယုံကြည်မှုပမာဏနည်းသော ပြုပြင်မှု လုပ်ငန်းစဉ်များအတွက် confidence metadata ကို ဖတ်သည်။ |
| `ReviewRunner` | `co_op_translator.review.runner` | မူရင်းဖိုင်များ၊ ပစ်မှတ်ဘာသာစကားများနှင့် ဖော်ပြထားသော translation root များအနှံ့ သတ်မှတ်ထားသော review စစ်ဆေးချက်များကို ညှိနှိုင်းလုပ်ဆောင်သည်။ |
| `ReviewTarget` | `co_op_translator.review.targets` | source root တစ်ခုနှင့် အဆိုပါ root အတွက် သုံးသပ်လေ့လာသည့် translation ထုတ်ပေါက် ဒိုင်ရက်ထရီကို ဖော်ပြသည်။ |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | အဟောင်း alias ဘာသာစကား ဖိုလ်ဒါများကို တွေ့ရှိကာ canonical BCP 47 ဖိုလ်ဒါ ပြောင်းရွှေ့ရေး အစီအစဉ်များကို ပြင်ဆင်သည်။ |
| `Config` | `co_op_translator.config.base_config` | `.env` ဖိုင်များကို ဖတ်ယူပြီး လိုအပ်သော LLM နှင့် ရွေးချယ်နိုင်သော Vision provider များ သတ်မှတ်ထားခဲ့မထား စစ်ဆေးသည်။ |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI၊ OpenAI သို့မဟုတ် Anthropic ကို အလိုအလျောက် တွေ့ရှိပြီး လိုအပ်သော environment variable များအား အတည်ပြုပြီး provider ချိတ်ဆက်နိုင်မှု စစ်ဆေးချက်များကို ဆောင်ရွက်သည်။ |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision ဖော်ပြချက်ကို တွေ့ရှိကာ ပုံဘာသာပြန်မှု အတွက် ချိတ်ဆက်နိုင်မှု စစ်ဆေးချက်များကို လုပ်ဆောင်သည်။ |