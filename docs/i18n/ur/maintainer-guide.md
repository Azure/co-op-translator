# مینٹینر رہنما

یہ صفحہ خلاصہ پیش کرتا ہے کہ API، CLI، اور دستاویزاتی سائٹ کس طرح آپس میں مربوط ہیں۔

## پبلک API کی حد

مستحکم Python API درج ذیل سے برآمد ہوتی ہے:

```python
co_op_translator.api
```

پبلک API مندرجہ ذیل حصوں میں منظم ہے: مواد کے ترجمے کے مددگار، راستہ دوبارہ لکھنے کے مددگار، پروجیکٹ آرکسٹریشن، اور جائزہ:

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

جب نئے پبلک APIs شامل کریں، اپ ڈیٹ کریں:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

اس بات سے گریز کریں کہ نچلے درجے کے `core` ماڈیولز کو بطور مستحکم API دستاویزی شکل دی جائے جب تک کہ پروجیکٹ انہیں براہِ راست سپورٹ کرنے کا ارادہ نہ رکھتا ہو۔

## CLI انٹری پوائنٹس

پیکیج یہ Poetry اسکرپٹس متعین کرتا ہے:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` اسکرپٹ کے نام کے مطابق ڈسپیچ کرتا ہے:

- `translate` کال کرتا ہے `co_op_translator.cli.translate.translate_command`
- `evaluate` کال کرتا ہے `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` کال کرتا ہے `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` کال کرتا ہے `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` براہِ راست `__main__.py` کو بائی پاس کرتا ہے اور براہِ راست `co_op_translator.mcp.server:main` کو کال کرتا ہے۔

جب CLI اختیارات شامل یا تبدیل کریں، اپ ڈیٹ کریں:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- CLI-related tests, if behavior changes

## MCP سرور

MCP سرور درج ذیل میں نافذ کیا گیا ہے:

```python
co_op_translator.mcp.server
```

سرور جان بوجھ کر پبلک Python API کو لپیٹتا ہے بجائے اس کے کہ نچلے درجے کے `core` ماڈیولز کو کال کرے۔ اس سرحد کو برقرار رکھیں تاکہ MCP کلائنٹس، Python کالرز، اور CLI ایک ہی رویہ شیئر کریں۔

جب MCP ٹولز شامل یا تبدیل کریں، اپ ڈیٹ کریں:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Repository translation tools are model-callable through MCP and can write many files. Keep `dry_run=True` as the default and require `confirm_write=True` before non-dry-run project translation.

## ترجمہ کا بہاؤ

پراجیکٹ کے اعلی سطحی ترجمہ کا بہاؤ یہ ہے:

1. CLI دلائل یا API پیرامیٹرز کو تجزیہ کریں۔
2. LLM کنفیگریشن کو `LLMConfig` کے ساتھ تصدیق کریں۔
3. جب تصویر کے ترجمے کا انتخاب کیا گیا ہو تو Azure AI Vision کی تصدیق کریں۔
4. زبان کے کوڈز کو معیاری بنائیں۔
5. لیگیسی زبان کے فولڈر الیاس کا پتہ لگائیں۔
6. ترجمے کے حجم کا اندازہ لگائیں۔
7. جب قابلِ اطلاق ہو تو README کی زبان/کورس سیکشنز کو اپ ڈیٹ کریں۔
8. پراجیکٹ کے ترجمے کو `ProjectTranslator` کو تفویض کریں۔
9. `ProjectTranslator` فائل پروسیسنگ کو `TranslationManager` کو تفویض کرتا ہے۔

`TranslationManager` مخصوص فائل-ٹائپ مکس انز سے مرکب ہے:

- `ProjectMarkdownTranslationMixin` Markdown فائل پڑھنے، مواد کے ترجمے، راستہ دوبارہ لکھنے، میٹا ڈیٹا، ڈس کلیمرز، اور لکھنے کو ہینڈل کرتا ہے۔
- `ProjectNotebookTranslationMixin` نوٹ بک فائل پڑھنے، Markdown-سیل کے ترجمے، راستہ دوبارہ لکھنے، میٹا ڈیٹا، ڈس کلیمرز، اور لکھنے کو ہینڈل کرتا ہے۔
- `ProjectImageTranslationMixin` امیج کی دریافت، متن نکالنا/ترجمہ، رینڈر شدہ تصویر کی تحریر، اور میٹا ڈیٹا کو ہینڈل کرتا ہے۔

نچلے سطح کے مواد API پروجیکٹ ورک فلو کو چھوڑ دیتے ہیں:

1. `translate_markdown_content` and `translate_notebook_content` صرف میموری میں موجود مواد کا ترجمہ کرتے ہیں۔
2. `translate_image_content` ایک تصویر میں متن کا ترجمہ کرتا ہے اور ایک رینڈر شدہ تصویر آبجیکٹ واپس کرتا ہے۔
3. `rewrite_markdown_paths` and `rewrite_notebook_paths` واضح پوسٹ-پروسیسنگ ہیلپرز ہیں۔ یہ نہ تو ترجمہ کرتے ہیں اور نہ ہی پروجیکٹ تحریرات کرتے ہیں۔

## جائزہ کا بہاؤ

ڈیٹرمنسٹک جائزے کا بہاؤ یہ ہے:

1. CLI دلائل یا API پیرامیٹرز کو تجزیہ کریں۔
2. درخواست کردہ زبان کے کوڈز کو معیاری بنائیں۔
3. `root_dir`, `root_dirs`, یا `groups` سے ایک یا زیادہ جائزہ ٹارگٹس بنائیں۔
4. اختیاری طور پر سورس فائلوں کو `--changed-from` کے ساتھ محدود کریں۔
5. ساخت، ترجمے کی تازگی، Markdown سالمیت، اور لوکل لنک/امیج راستوں کے لیے ڈیٹرمنسٹک چیک چلائیں۔
6. یا تو متن آؤٹ پٹ پرنٹ کریں یا GitHub-flavored Markdown۔
7. جب جائزہ میں غلطیاں ملیں تو ناکامی کے ساتھ باہر نکلیں۔

جائزہ بہاؤ کو API keys کی ضرورت نہیں ہوتی اور یہ pull request CI کے لیے مناسب رہنا چاہیے۔ pull request ورک فلو ہر رن پر چیک سمری لکھتا ہے اور صرف اس وقت PR کمنٹ پوسٹ کرتا ہے جب `co-op-review` ناکام ہو۔

## دستاویزی سائٹ

ڈوکس سائٹ درج ذیل سے کنفیگر کی جاتی ہے:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` ڈائریکٹری کینونیکل دستاویزاتی ماخذ ہے۔ اس ڈائریکٹری کے باہر نئے اینڈ-یوزر گائیڈز نہ شامل کریں جب تک کہ پروجیکٹ جان بوجھ کر کوئی اور شائع شدہ ڈاکیومنٹیشن سطح متعارف نہ کرائے۔

لوکل طور پر بنائیں:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

مقامی پیش نظارہ:

```bash
python -m mkdocs serve
```

جنریٹر کی گئی سائٹ `site/` میں لکھی جاتی ہے، جسے git نظر انداز کرتا ہے۔

## GitHub Pages ورک فلو

.github/workflows/docs.yml pull requests پر سائٹ بناتا ہے اور `main` پر pushes پر اسے تعینات کرتا ہے۔

ورک فلو یہ انسٹال کرتا ہے:

```bash
pip install -r requirements-docs.txt
```

ڈوکس ورک فلو صرف دستاویزات کے ٹول چین کو انسٹال کرتا ہے۔ `mkdocs.yml` `mkdocstrings` کو `src/` کی طرف اشارہ کرتا ہے تاکہ پبلک API صفحات سورس ٹری سے رینڈر کیے جا سکیں بغیر مکمل رن ٹائم ڈیپنڈینسی سیٹ کو انسٹال کیے۔ اگر مستقبل کے API دستاویزات کو بلڈ کے دوران اختیاری رن ٹائم پرووائیڈرز کو امپورٹ کرنے کی ضرورت ہو، تو دونوں `.github/workflows/docs.yml` اور اس گائیڈ کو ایک ساتھ اپ ڈیٹ کریں۔

## دستاویزات کا معیار

دستاویزاتی تبدیلیاں مرج کرنے سے پہلے، چلائیں:

```bash
python -m mkdocs build --strict
git diff --check
```

سخت بلڈز استعمال کریں تاکہ ٹوٹے ہوئے لنکس، غلط نیویگیشن انٹریز، اور API رینڈرنگ کے مسائل جلدی ناکام ہوں۔