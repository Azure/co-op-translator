# ထိန်းသိမ်းသူ လမ်းညွှန်

ဒီစာမျက်နှာမှာ API၊ CLI နှင့် စာတမ်းဆိုဒ်တို့ မည်သို့ ဆက်သွယ်ထားကြောင်း အကျဥ်းချုပ် ဖော်ပြထားသည်။

## အများပြည်သူ API နယ်နိမိတ်

တည်ငြိမ်သော Python API ကို အောက်ပါနေရာမှ ထုတ်ပေးထားသည်။

```python
co_op_translator.api
```

အများပြည်သူ API ကို အကြောင်းအရာ ဘာသာပြန် ကူညီသူများ၊ လမ်းကြောင်း ပြန်ရေး ကူညီသူများ၊ ပရောဂျက် စီမံခန့်ခွဲမှုနှင့် ပြန်လည်သုံးသပ်ခြင်း အပိုင်းများအဖြစ် စုစည်းထားသည်။

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` သည် hosted integrations များအတွက် တည်တံ့မှု နယ်နိမိတ်ဖြစ်သည်။
ထုတ်လုပ်ထားသော candidate များကို လက်ခံထားသော baseline များနှင့် သီးခြား စုဆောင်းထားရမည်၊ ထို့ကြောင့်
မသတ်မှတ်အောင်လက်မခံထားသော ဘာသာပြန်ချက်သည် အချက်အလက်၏ အဓိက အရင်းအမြစ် ဖြစ်လာခွင့် မရပါ။

အများပြည်သူ API အသစ်များ ထည့်သွင်းလိုက်ပါက အောက်ဖော်ပြပါများကို အပ်ဒိတ်လုပ်ပါ။

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- စပ်ဆိုင်သော API စမ်းသပ်ချက်များကို `tests/co_op_translator/` အောက်တွင် ထည့်ပါ၊ ဥပမာ `test_api.py` သို့မဟုတ် `test_review_api.py`

ပရောဂျက်က တိုက်ရိုက် ထောက်ပံ့ရန် ရည်ရွယ်မထားပါက အောက်ပါအဆင့် `core` မော်ဂျူးများကို တည်ငြိမ်သော API အဖြစ် စာတမ်းရေးရန် ရှောင်ရှားပါ။

## CLI ဝင်လမ်းများ

ဤ package သည် အောက်ပါ Poetry script များကို သတ်မှတ်ထားသည်။

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` သည် script အမည်အရ ခေါ်ဆောင်ပေးသည်။

- `translate` သည် `co_op_translator.cli.translate.translate_command` ကို ခေါ်သည်
- `evaluate` သည် `co_op_translator.cli.evaluate.evaluate_command` ကို ခေါ်သည်
- `migrate-links` သည် `co_op_translator.cli.migrate_links.migrate_links_command` ကို ခေါ်သည်
- `co-op-review` သည် `co_op_translator.cli.review.review_command` ကို ခေါ်သည်

`co-op-translator-mcp` သည် `__main__.py` ကို ကျော်လွှားပြီး `co_op_translator.mcp.server:main` ကို တိုက်ရိုက် ခေါ်ယူသည်။

CLI ရွေးချယ်စရာများ (options) အသစ် ထည့်သွင်းသော်လည်း ပြောင်းလဲသော်လည်း အောက်ဖော်ပြပါများကို အပ်ဒိတ်လုပ်ပါ။

- သက်ဆိုင်သော `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- လုပ်ဆောင်မှု ပြောင်းလဲပါက CLI-ဆိုင်ရာ စမ်းသပ်မှုများ

## MCP ဆာဗာ

MCP ဆာဗာကို အောက်ပါတွင် အကောင်အထည်ဖော်ထားသည်။

```python
co_op_translator.mcp.server
```

ဆာဗာသည် ရည်ရွယ်ချက်ရှိစွာ အနိမ့်အဆင့် `core` မော်ဂျူးများကို တိုက်ရိုက် ခေါ်ယူခြင်းမပြုဘဲ အများပြည်သူ Python API ကို wrapper အဖြစ် ပတ်လုပ်ထားသည်။ ဤနယ်နိမိတ်ကို ထိန်းသိမ်းထားပါက MCP clients၊ Python callers နှင့် CLI တို့သည် တစ်မျိုးတည်းသော အပြုအမူကို မျှဝေသည်။

MCP ကိရိယာများ ထည့်သွင်း သို့မဟုတ် ပြောင်းလဲသောအခါ အောက်ဖော်ပြပါများကို အပ်ဒိတ်လုပ်ပါ။

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` — public API surface ပြောင်းလဲပါက

Repository translation tools များကို MCP မှတဆင့် model-callable ဖြစ်စေပြီး ဖိုင်များ များစွာ ရေးနိုင်သည်။ မူရင်းဖြစ်စဉ်အနေဖြင့် `dry_run=True` ကို default အဖြစ် ထားပြီး non-dry-run project translation မတိုင်မီ `confirm_write=True` ကို တောင်းခံပါ။

## ဘာသာပြန်လုပ်ငန်းစဉ်

ပရောဂျက် ဘာသာပြန်၏ အဆင့်မြင့် လုပ်ငန်းစဉ်မှာ အောက်ပါအတိုင်း ဖြစ်သည်။

1. CLI arguments သို့မဟုတ် API parameters များကို ခွဲထုတ်သည်။
2. `LLMConfig` ဖြင့် LLM configuration ကို အတည်ပြုသည်။
3. ပုံဘာသာပြန်ရွေးထားပါက Azure AI Vision ကို အတည်ပြုသည်။
4. ဘာသာစကား ကုဒ်များကို ပုံစံတစ်မျိုးတည်း ပြုစုသည်။
5. အဟောင်း ဘာသာစကား ဖိုလ်ဒါ အမည်များ (aliases) ကို တွေ့ရှိသည်။
6. ဘာသာပြန် အရေအတွက် ကို ခန့်မှန်းသည်။
7. သက်ဆိုင်ပါက README ရဲ့ language/course အပိုင်းများကို အပ်ဒိတ်လုပ်သည်။
8. ပရောဂျက် ဘာသာပြန်ကို `ProjectTranslator` သို့ လွှဲပေးသည်။
9. `ProjectTranslator` သည် ဖိုင်များကို ကိုင်တွယ်ရန် `TranslationManager` ထံ လွှဲပေးသည်။

`TranslationManager` ကို ဖိုင်အမျိုးအစားအလိုက် အာရုံစိုက်သော mixin များမှ ဖွဲ့စည်းထားသည်။

- `ProjectMarkdownTranslationMixin` သည် Markdown ဖိုင် ဖတ်ခြင်း၊ အကြောင်းအရာ ဘာသာပြန်ခြင်း၊ လမ်းကြောင်း ပြန်ရေးခြင်း၊ metadata၊ ငြင်းဆိုချက်များနှင့် ဖိုင်ရေးခြင်းတို့ကို ကိုင်တွယ်သည်။
- `ProjectNotebookTranslationMixin` သည် notebook ဖိုင် ဖတ်ခြင်း၊ Markdown-cell ဘာသာပြန်ခြင်း၊ လမ်းကြောင်း ပြန်ရေးခြင်း၊ metadata၊ ငြင်းဆိုချက်များနှင့် ဖိုင်ရေးခြင်းတို့ကို ကိုင်တွယ်သည်။
- `ProjectImageTranslationMixin` သည် ဓာတ်ပုံ ရှာဖွေခြင်း၊ စာသား ရယူ/ဘာသာပြန်ခြင်း၊ ပြန်လည်ဖန်တီးထားသော ဓာတ်ပုံများ ရေးသားခြင်းနှင့် metadata ကို ကိုင်တွယ်သည်။

အောက်ခြေ အဆင့် content API များသည် project workflow ကို ကျော်၍ တိုက်ရိုက် လုပ်ဆောင်သည်။

1. `translate_markdown_content` နှင့် `translate_notebook_content` သည် memory ပေါ်ရှိ အကြောင်းအရာများကိုသာ ဘာသာပြန်သည်။
2. `translate_image_content` သည် တစ်ပုံ၏ စာသားကို ဘာသာပြန်ပြီး ပြန်လည်ဖန်တီးထားသော ဓာတ်ပုံ object ကို ပြန်ပေးသည်။
3. `rewrite_markdown_paths` နှင့် `rewrite_notebook_paths` သည် post-processing အတွက် ရည်ရွယ်ထားသော ကူညီသူများဖြစ်သည်။ ၎င်းတို့သည် ဘာသာပြန်မှု မပြုလုပ်ဘဲ project ဖိုင်များကို မရေးဆွဲပါ။

## ပြန်လည်သုံးသပ်ခြင်း လုပ်ငန်းစဉ်

သတ်မှတ်လိုက်သော ပြန်လည်သုံးသပ်မှု လုပ်ငန်းစဉ်မှာ အောက်ပါအတိုင်း ဖြစ်သည်။

1. CLI arguments သို့မဟုတ္ API parameters များကို ခွဲထုတ်သည်။
2. တောင်းဆိုထားသော ဘာသာစကား ကုဒ်များကို ပုံစံတူညီစေသည်။
3. `root_dir`, `root_dirs`, သို့မဟုတ် `groups` မှ review target တစ်ခု သို့မဟုတ် အများစွာကို တည်ဆောက်သည်။
4. အလိုက်အရ `--changed-from` ဖြင့် အရင်းအမြစ် ဖိုင်များကို ကန့်သတ်နိုင်သည်။
5. ဖွဲ့စည်းပုံ၊ ဘာသာပြန် အသစ်လက်ရှိမှု၊ Markdown တင်းကြပ်မှုနှင့် ဒေသတွင်း link/ဓာတ်ပုံ လမ်းကြောင်းများအတွက် သတ်မှတ်ထားသော စစ်ဆေးမှုများကို ဆောင်ရွက်သည်။
6. စာသား output သို့မဟုတ် GitHub-flavored Markdown တစ်မျိုးကို ထုတ်ပေးသည်။
7. ပြန်လည်သုံးသပ်မှုတွင် အမှားတွေ့ပါက မအောင်မြင်သော အခြေအနေဖြင့် ထွက်မည်။

ပြန်လည်သုံးသပ်မှု လုပ်ငန်းစဉ်တွင် API key မလိုအပ်၍ ဒေသတွင်း စစ်ဆေးမှုများ သို့မဟုတ် ရွေးချယ်ဝင်ရန် consumer CI များအတွက် ရရှိနိုင်သည်။ ဒီ repository မှာ မည်သည့် pull request တစ်ခုစီတွင်ကို `co-op-review` ကို အလိုအလျောက် မပြုလုပ်ပါ။

## စာတမ်းဆိုဒ်

docs ဆိုဒ်ကို အောက်ပါဖိုင်များဖြင့် ဆက်တင် တပ်ဆင်ထားသည်။

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` directory သည် canonical documentation အရင်းမြစ် ဖြစ်သည်။ ပရောဂျက်က ရည်ရွယ်ချက်ရှိစွာ အခြား ထုတ်ပြန်သော documentation surface တစ်ခု မိတ်ဆက်ရန် ရည်ရွယ်ထားလျှင် မဟုတ်ပါက ဤ directory ပြင်ပတွင် အသုံးပြုသူ အတွက် လမ်းညွှန်အသစ်များ မထည့်ပါ။

ဒေသတွင်း၌ ဆောက်လုပ်ရန်：

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

ဒေသတွင်း ကြည့်ရှုရန်：

```bash
python -m mkdocs serve
```

ဖန်တီးထားသည့် ဆိုဒ်ကို `site/` တွင် ရေးသွားပြီး git ၌ ignore ထားသည်။

## GitHub Pages လုပ်ငန်းစဉ်

`.github/workflows/docs.yml` သည် pull request များတွင် ဆိုဒ်ကို ဆောက်၍ `main` သို့ push တက်သည့်အခါ deploy ပြုလုပ်သည်။

အလုပ်စဉ်သည် အောက်ပါအရာများကို တပ်ဆင်သည်။

```bash
pip install -r requirements-docs.txt
```

docs workflow သည် documentation toolchain ကိုသာ တပ်ဆင်သည်။ `mkdocs.yml` သည် `mkdocstrings` ကို `src/` သို့ ညွှန်ပြထား၍ public API စာမျက်နှာများကို အပြည့်အစုံ runtime dependency မတပ်ဆင်ဘဲ source tree မှ မှမ်းမံဖော်ပြနိုင်စေသည်။ အနာဂတ်တွင် API စာတမ်းများကို build အတွင်း optional runtime providers များကို import လုပ်ရန် လိုအပ်လာပါက `.github/workflows/docs.yml` နှင့် ဤလမ်းညွှန်စာကို အတူတကွ အပ်ဒိတ်လုပ်ပါ။

## စာတမ်း အရည်အသွေး အဆင့်

စာတမ်း ပြင်ဆင်မှုများကို merge မလုပ်ခင် အောက်ပါကို လည်ပတ်ပါ။

```bash
python -m mkdocs build --strict
git diff --check
```

strict builds ကို အသုံးပြုပါ၊ ထို့ဖြင့် ချိုးကျသော link များ၊ မမှန်သော navigation entry များနှင့် API rendering ပြဿနာများကို စောစီးစွာ ဖော်ထုတ်နိုင်ရန် ဖြစ်စေမည်။