# ထိန်းသိမ်းသူ လမ်းညွှန်

ဤစာမျက်နှာသည် API, CLI, နှင့် စာရွက်စာတမ်း ဆိုက်တို့ကို ဘယ်လိုဆက်ထားကြောင်း အကျဉ်းချုပ် ဖော်ပြထားသည်။

## အများပြည်သူ API နယ်နိမိတ်

တည်ငြိမ်သော Python API သည် အောက်ပါမှ တင်ပို့ထားသည်။

```python
co_op_translator.api
```

အများပြည်သူ API ကို အကြောင်းအရာ ဘာသာပြန် ကူညီပေးမှုများ၊ လမ်းကြောင်း ပြန်ရေး ကူညီပေးမှုများ၊ ပရောဂျက် စီမံခန့်ခွဲမှု နှင့် ပြန်လည်သုံးသပ်မှု အဖြစ် အုပ်စုဖွဲ့ထားသည်။

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

အများပြည်သူ API အသစ်များ ထည့်သည့်အခါ အောက်ပါများကို အပ်ဒိတ်လုပ်ပါ။

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- သက်ဆိုင်ရာ API စမ်းသပ်မှုများကို `tests/co_op_translator/` အောက်တွင် အပ်ဒိတ်လုပ်ပါ၊ ဥပမာ `test_api.py` သို့မဟုတ် `test_review_api.py`

ပရောဂျက်သည် တိုက်ရိုက် ထောက်ပံ့ရန် ရည်ရွယ်ထားမဟုတ်ပါက အနိမ့်အဆင့်ရှိ `core` modules များကို တည်ငြိမ်သော API အဖြစ် မှတ်တမ်းတင်ရန် ရှောင်ကြဉ်ပါ။

## CLI entry points

ပက်ကေ့ချ်တွင် အောက်ပါ Poetry scripts များကို သတ်မှတ်ထားသည်။

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` သည် script name အလိုက် dispatch လုပ်သည်။

- `translate` က `co_op_translator.cli.translate.translate_command` ကို ခေါ်သည်
- `evaluate` က `co_op_translator.cli.evaluate.evaluate_command` ကို ခေါ်သည်
- `migrate-links` က `co_op_translator.cli.migrate_links.migrate_links_command` ကို ခေါ်သည်
- `co-op-review` က `co_op_translator.cli.review.review_command` ကို ခေါ်သည်

`co-op-translator-mcp` သည် `__main__.py` ကို ကျော်လွန်ပြီး `co_op_translator.mcp.server:main` ကို တိုက်ရိုက် ခေါ်သည်။

CLI ရွေးချယ်စရာများ ထည့်သို့မဟုတ် ပြောင်းလဲသောအခါ အောက်ပါကို အပ်ဒိတ်လုပ်ပါ။

- သက်ဆိုင်ရာ `src/co_op_translator/cli/*.py` အမိန့်
- `docs/cli.md`
- အပြုအမူ ပြောင်းလဲပါက CLI ဆိုင်ရာ စမ်းသပ်မှုများ

## MCP server

MCP ဆာဗာကို အောက်ပါတွင် အကောင်အထည်ဖော်ထားသည်။

```python
co_op_translator.mcp.server
```

ဆာဗာသည် အနိမ့်အဆင့်ရှိ `core` မော်ဂျူးများကို ခေါ်သုံးရန်မဟုတ်ဘဲ အများပြည်သူ Python API ကို ထုပ်ပိုးသတ်မှတ်ထားသည်။ ဤနယ်နိမိတ်ကို မဖျက်စီးစေရန် ထိန်းသိမ်းပါ၊ ထို့ကြောင့် MCP clients, Python callers, နှင့် CLI သုံးသူများသည် တူညီသော အပြုအမူကို မျှဝေခံနိုင်မည်ဖြစ်သည်။

MCP ကိရိယာများ ထည့်သို့မဟုတ် ပြောင်းလဲသောအခါ အောက်ပါများကို အပ်ဒိတ်လုပ်ပါ။

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- ပြည့်စုံသော public API အကွာအဝေး ပြောင်းလဲပါက `docs/api.md`

Repository translation tool များကို MCP မှတဆင့် မော်ဒယ်ဖြင့် ခေါ်နိုင်ပြီး ဖိုင်များစွာရေးထုတ်နိုင်သည်။ default အဖြစ် `dry_run=True` ကို ထားပြီး dry run မဟုတ်သော ပရောဂျက် ဘာသာပြန်မှု မစတင်မီ `confirm_write=True` ကို လိုအပ်အောင် ထိန်းသိမ်းပါ။

## Translation flow

အဆင့်မြင့် ပရောဂျက် ဘာသာပြန် လုပ်ငန်းစဉ်မှာ အောက်ပါအတိုင်းဖြစ်သည်။

1. CLI arguments သို့မဟုတ် API parameters များကို ခွဲထုတ်ပါ။
2. `LLMConfig` ဖြင့် LLM ဖွဲ့စည်းမှုကို စစ်ဆေးပါ။
3. ပုံများ ဘာသာပြန်ရန် ရွေးချယ်ထားပါက Azure AI Vision ကို စစ်ဆေးပါ။
4. ဘာသာစကားကုဒ်များကို ပုံမှန်စေပါ။
5. အဟောင်း ဘာသာစကား ဖိုလ်ဒါ alias များကို ရှာဖွေပါ။
6. ဘာသာပြန် အလုပ်ပမာဏကို ခန့်မှန်းပါ။
7. လိုအပ်သောအခါ README ၏ ဘာသာစကား/သင်တန်း အပိုင်းများကို အပ်ဒိတ်လုပ်ပါ။
8. ပရောဂျက် ဘာသာပြန်မှုကို `ProjectTranslator` သို့ ပေးအပ်ပါ။
9. `ProjectTranslator` သည် ဖိုင် ကြီးကြပ်မှုကို `TranslationManager` သို့ ပေးအပ်သည်။

`TranslationManager` သည် သီးသန့် ဖိုင်အမျိုးအစား mixin များမှ ပေါင်းစပ်တည်ဆောက်ထားသည်။

- `ProjectMarkdownTranslationMixin` သည် Markdown ဖိုင် ဖတ်ခြင်း၊ အကြောင်းအရာ ဘာသာပြန်ခြင်း၊ လမ်းကြောင်း ပြန်ရေးခြင်း၊ မီတာဒေတာ၊ သတိပေးချက်များနှင့် ဖိုင်ရေးထုတ်ခြင်းတို့ကို ကိုင်တွယ်သည်။
- `ProjectNotebookTranslationMixin` သည် notebook ဖိုင် ဖတ်ခြင်း၊ Markdown-cell ဘာသာပြန်ခြင်း၊ လမ်းကြောင်း ပြန်ရေးခြင်း၊ မီတာဒေတာ၊ သတိပေးချက်များနှင့် ဖိုင်ရေးထုတ်ခြင်းတို့ကို ကိုင်တွယ်သည်။
- `ProjectImageTranslationMixin` သည် image ရှာဖွေခြင်း၊ စာသား ထုတ်ယူ/ဘာသာပြန်ခြင်း၊ ပြင်ဆင်ပြီး image ရေးထုတ်ခြင်းနှင့် မီတာဒေတာကို ကိုင်တွယ်သည်။

အနိမ့်အဆင့် အကြောင်းအရာ API များသည် ပရောဂျက် လုပ်ငန်းစဉ်ကို ကျော်လွှားသည်။

1. `translate_markdown_content` နှင့် `translate_notebook_content` သည် မှတ်ဉာဏ်တွင်း အကြောင်းအရာများကိုသာ ဘာသာပြန်သည်။
2. `translate_image_content` သည် တစ်ပုံ၏ စာသားကို ဘာသာပြန်၍ ပြင်ဆင်ထားသော image object ကို ပြန်ပေးသည်။
3. `rewrite_markdown_paths` နှင့် `rewrite_notebook_paths` သည် သေချာသတ်မှတ်ထားသော post-processing ကူညီမှုများဖြစ်သည်။ ၎င်းတို့မှာ ဘာသာပြန်ခြင်းမပြုလုပ်ဘဲ ပရောဂျက် ဖိုင်ရေးထုတ်မှုကိုလည်း မလုပ်ပါ။

## Review flow

သတ်မှတ်နိုင်သော ပြန်လည်သုံးသပ် လုပ်ငန်းစဉ်မှာ အောက်ပါအတိုင်းဖြစ်သည်။

1. CLI arguments သို့မဟုတ် API parameters များကို ခွဲထုတ်ပါ။
2. တောင်းဆိုထားသော ဘာသာစကားကုဒ်များကို ပုံမှန်စေပါ။
3. `root_dir`, `root_dirs`, သို့မဟုတ် `groups` မှ review target တစ်ခု ဒါမှမဟုတ် အများအပြား တည်ဆောက်ပါ။
4. လိုအပ်ပါက `--changed-from` ဖြင့် မူလဖိုင်များကို ကန့်သတ်နိုင်သည်။
5. ဖွဲ့စည်းပုံ၊ ဘာသာပြန်၏ နောက်ဆုံးမှတ်တမ်း (translation freshness)、Markdown တည်ငြိမ်မှု (integrity) နှင့် ဒေသဆိုင်ရာ link/image လမ်းကြောင်းများအတွက် သတ်မှတ်နိုင်သော စစ်ဆေးမှုများကို ပြုလုပ်ပါ။
6. စာသား output သို့မဟုတ် GitHub-flavored Markdown တစ်ခုအား ထုတ်ပြပါ။
7. review အမှားများ တွေ့ရှိပါက အချက်အလက်အမှားဖြင့် ထွက်ပေါက်ပါ။

ပြန်လည်သုံးသပ် လုပ်ငန်းစဉ်သည် API keys မလိုအပ်ပါနှင့် pull request CI အတွက် သင့်တော်စေရန် ထိန်းသိမ်းထားသင့်သည်။ Pull request workflow သည် run တစ်ခုချင်းစီတွင် စစ်ဆေးချက် အကျဉ်းကို ရေးသွင်းပြီး `co-op-review` မအောင်မြင်ပါကသာ PR comment တင်ပေးမည်ဖြစ်သည်။

## Documentation site

စာရွက်စာတမ်း ဆိုက်ကို အောက်ပါဖြင့် ဖွဲ့ထားသည်။

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` ဒိုင်ရေးထရီသည် တရားဝင် စာရွက်စာတမ်း မူလ အရင်းအမြစ် ဖြစ်သည်။ ပရောဂျက်သည် အခြား ထုတ်ပြန်ထားသော စာရွက်စာတမ်း မျက်နှာပြင်တစ်ခု ကို ရည်ရွယ်ထည့်သွင်းထားခြင်း မရှိပါက ဤဒိုင်ရက်ပြင်ပတွင် အသုံးပြုသူ လမ်းညွှန်အသစ် မထည့်ပါနှင့်။

ကိုယ်ပိုင်စက်တွင် ဆောက်လုပ်ရန်:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

ဒေသတွင်း ကြိုတင်ကြည့်ရန်:

```bash
python -m mkdocs serve
```

ဖန်တီးထားသော ဆိုက်ကို `site/` သို့ ရေးထုတ်ပြီး ၎င်းကို git မှ မထည့်သွင်းပါ။

## GitHub Pages workflow

`.github/workflows/docs.yml` သည် pull requests များတွင် ဆိုက်ကို ဆောက်ပြီး `main` သို့ push လုပ်သောအခါ ထုတ်လွှင့်သည်။

workflow သည် အောက်ပါများကို တပ်ဆင်သည်။

```bash
pip install -r requirements-docs.txt
```

docs workflow သည် documentation toolchain များကိုသာ တပ်ဆင်ပါသည်။ `mkdocs.yml` သည် `mkdocstrings` ကို `src/` သို့ ညွှန်ထားပြီး public API စာမျက်နှာများကို full runtime dependency မတပ်ဘဲ source tree မှ တိုက်ရိုက် render ပြုလုပ်နိုင်စေသည်။ အနာဂတ်တွင် API စာတမ်းများကို build အတွင်း optional runtime providers များကို import လုပ်ရန် လိုအပ်လာပါက `.github/workflows/docs.yml` နှင့် ဤလမ်းညွှန်ကို အတူတကွ အပ်ဒိတ်လုပ်ပါ။

## Docs quality bar

စာရွက်စာတမ်း ပြင်ဆင်မှုများကို merge မပြုမီ အောက်ပါကို run လုပ်ပါ။

```bash
python -m mkdocs build --strict
git diff --check
```

ဖောက်ထွင်းနေသော link များ၊ navigation မှားယွင်းမှုများနှင့် API rendering ပြဿနာများကို စောစီးစွာ တွေ့ရှိနိုင်စေရန် strict builds များကို အသုံးပြုပါ။