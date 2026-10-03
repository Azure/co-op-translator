# مینٹینر کا رہنما

یہ صفحہ خلاصہ بیان کرتا ہے کہ API، CLI، اور دستاویزی سائٹ کس طرح مربوط ہیں۔

## عوامی API کی حد

مستحکم Python API مندرجہ ذیل جگہ سے برآمد ہوتی ہے:

```python
co_op_translator.api
```

عوامی API کو مواد کے ترجمے کے ہیلپرز، راستوں کو دوبارہ لکھنے کے ہیلپرز، پروجیکٹ آرکسٹریشن، اور جائزے میں منظم کیا گیا ہے:

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

`TranslationStateProvider` ہوسٹ شدہ انضمام کے لیے پائیداری کی حد ہے۔
اسے تیار کردہ امیدواروں کو قبول شدہ بنیادی نسخوں سے الگ رکھنا چاہیے تاکہ ایک
غیر ضم شدہ ترجمہ حقیقت کا ماخذ نہیں بن سکتا۔

جب نئے عوامی APIs شامل کیے جائیں تو درج ذیل کو اپ ڈیٹ کریں:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- متعلقہ API ٹیسٹس جو `tests/co_op_translator/` کے تحت ہوں، جیسے `test_api.py` یا `test_review_api.py`

جب تک پروجیکٹ کا ارادہ براہ راست ان کی حمایت کرنے کا نہ ہو، نچلے سطح کے `core` ماڈیولز کو مستحکم API کے طور پر دستاویزی شکل دینے سے گریز کریں۔

## CLI انٹری پوائنٹس

پیکج درج ذیل Poetry اسکرپٹس متعین کرتا ہے:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` اسکرپٹ کے نام کے مطابق ڈسپیچ کرتا ہے:

- `translate` `co_op_translator.cli.translate.translate_command` کو کال کرتا ہے
- `evaluate` `co_op_translator.cli.evaluate.evaluate_command` کو کال کرتا ہے
- `migrate-links` `co_op_translator.cli.migrate_links.migrate_links_command` کو کال کرتا ہے
- `co-op-review` `co_op_translator.cli.review.review_command` کو کال کرتا ہے

`co-op-translator-mcp` `__main__.py` کو بائی پاس کرتا ہے اور براہِ راست `co_op_translator.mcp.server:main` کو کال کرتا ہے۔

جب CLI اختیارات شامل یا تبدیل کیے جائیں تو درج ذیل کو اپ ڈیٹ کریں:

- متعلقہ `src/co_op_translator/cli/*.py` کمانڈ
- `docs/cli.md`
- CLI سے متعلقہ ٹیسٹس، اگر رویہ بدلتا ہے

## MCP سرور

MCP سرور درج ذیل میں نافذ کیا گیا ہے:

```python
co_op_translator.mcp.server
```

سرور جان بوجھ کر عوامی Python API کو ریپ کرتا ہے بجائے اس کے کہ یہ نچلے درجے کے `core` ماڈیولز کو کال کرے۔ اس حد کو برقرار رکھیں تاکہ MCP کلائنٹس، Python کالرز، اور CLI ایک ہی رویہ شیئر کریں۔

جب MCP ٹولز شامل یا تبدیل کیے جائیں تو، درج ذیل کو اپ ڈیٹ کریں:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` اگر عوامی API کا احاطہ تبدیل ہوتا ہے

ریپوزیٹری ترجمہ کے ٹولز MCP کے ذریعے ماڈل-کال ایبل ہیں اور کئی فائلیں لکھ سکتے ہیں۔ `dry_run=True` کو بطور ڈیفالٹ رکھیں اور غیر-dry-run پروجیکٹ ترجمہ سے پہلے `confirm_write=True` درکار کریں۔

## ترجمے کا بہاؤ

پروجیکٹ کے اعلیٰ سطحی ترجمے کا بہاؤ یہ ہے:

1. CLI دلائل یا API پیرامیٹرز کو پارس کریں۔
2. LLMConfig کے ساتھ LLM کنفیگریشن کی توثیق کریں۔
3. جب امیج ترجمہ منتخب کیا گیا ہو تو Azure AI Vision کی تصدیق کریں۔
4. زبان کے کوڈز کو نارملائز کریں۔
5. پرانے زبان فولڈر کے عرفی نام کا پتہ لگائیں۔
6. ترجمے کے حجم کا اندازہ لگائیں۔
7. جب قابلِ اطلاق ہو تو README کے زبان/کورس سیکشنز کو اپ ڈیٹ کریں۔
8. پروجیکٹ ترجمہ کو `ProjectTranslator` کو سونپیں۔
9. `ProjectTranslator` فائل پراسیسنگ کو `TranslationManager` کو سونپتا ہے۔

`TranslationManager` مخصوص فائل ٹائپ مکسِنز سے مرکب ہوتا ہے:

- `ProjectMarkdownTranslationMixin` Markdown فائل کی پڑھائی، مواد کے ترجمے، راستہ دوبارہ لکھنے، میٹا ڈیٹا، ڈس کلیمرز، اور لکھائی کو ہینڈل کرتا ہے۔
- `ProjectNotebookTranslationMixin` نوٹ بک فائل کی پڑھائی، Markdown-سیل کے ترجمے، راستہ دوبارہ لکھنے، میٹا ڈیٹا، ڈس کلیمر، اور لکھائی کو ہینڈل کرتا ہے۔
- `ProjectImageTranslationMixin` امیج کی دریافت، متن نکالنا/ترجمہ، رینڈر کردہ امیج لکھائی، اور میٹا ڈیٹا کو ہینڈل کرتا ہے۔

نچلی سطح کے مواد API پروجیکٹ ورک فلو کو چھوڑ دیتے ہیں:

1. `translate_markdown_content` اور `translate_notebook_content` صرف میموری میں موجود مواد کا ترجمہ کرتے ہیں۔
2. `translate_image_content` ایک تصویر میں متن کا ترجمہ کرتا ہے اور ایک رینڈرڈ امیج آبجیکٹ واپس کرتا ہے۔
3. `rewrite_markdown_paths` اور `rewrite_notebook_paths` واضح پوسٹ-پروسیسنگ ہیلپرز ہیں۔ یہ کوئی ترجمہ یا پروجیکٹ لکھائی نہیں کرتے۔

## جائزہ کا بہاؤ

متعین جائزے کا بہاؤ یہ ہے:

1. CLI دلائل یا API پیرامیٹرز کو پارس کریں۔
2. درخواست کردہ زبان کے کوڈز کو نارملائز کریں۔
3. `root_dir`, `root_dirs`, یا `groups` سے ایک یا زیادہ جائزے کے ہدف بنائیں۔
4. اختیاری طور پر `--changed-from` کے ساتھ ماخذ فائلوں کو محدود کریں۔
5. ساخت، ترجمے کی تازگی، Markdown کی سالمیت، اور مقامی لنک/امیج راستوں کے لیے متعین چیکس چلائیں۔
6. یا تو ٹیکسٹ آؤٹ پٹ پرنٹ کریں یا GitHub طرز کا Markdown۔
7. جب جائزے میں غلطیاں ملیں تو ناکامی کے ساتھ خارج ہوں۔

جائزے کا بہاؤ API کیز کا تقاضا نہیں کرتا اور مقامی جانچ یا اختیاری صارف CI کے لیے دستیاب رہتا ہے۔ یہ ریپوزیٹری ہر پل ریکویسٹ پر خودکار طور پر `co-op-review` نہیں چلاتی۔

## دستاویزی سائٹ

دستاویزی سائٹ درج ذیل کے ذریعے تشکیل دی گئی ہے:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` ڈائریکٹری سرکاری دستاویزی ماخذ ہے۔ نئے اینڈ-یوزر گائیڈز اس ڈائریکٹری کے باہر نہ شامل کریں جب تک کہ پروجیکٹ جان بوجھ کر کوئی دوسرا شائع شدہ دستاویزاتی سطح متعارف نہ کروائے۔

مقامی طور پر بلڈ کریں:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

مقامی طور پر پیش نظارہ کریں:

```bash
python -m mkdocs serve
```

تخلیق شدہ سائٹ `site/` میں لکھی جاتی ہے، جسے git نظر انداز کرتا ہے۔

## GitHub Pages ورک فلو

`.github/workflows/docs.yml` پل ریکویسٹ پر سائٹ کو بلڈ کرتا ہے اور `main` پر push ہونے پر اسے ڈپلائے کرتا ہے۔

ورک فلو درج ذیل کو انسٹال کرتا ہے:

```bash
pip install -r requirements-docs.txt
```

دستاویزات ورک فلو صرف دستاویزی ٹول چین انسٹال کرتا ہے۔ `mkdocs.yml` `mkdocstrings` کو `src/` کی طرف اشارہ کرتا ہے تاکہ عوامی API صفحات سورس ٹری سے مکمل رن ٹائم ڈیپنڈنسی سیٹ کو انسٹال کیے بغیر رینڈر کیے جا سکیں۔ اگر مستقبل کے API دستاویزات کو بلڈ کے دوران اختیاری رن ٹائم پرووائیڈرز کو امپورٹ کرنے کی ضرورت ہو، تو دونوں `.github/workflows/docs.yml` اور اس گائیڈ کو ساتھ اپ ڈیٹ کریں۔

## دستاویزات کا معیار

دستاویزی تبدیلیاں مرج کرنے سے پہلے، چلائیں:

```bash
python -m mkdocs build --strict
git diff --check
```

سخت بلڈز استعمال کریں تاکہ ٹوٹے ہوئے لنکس، غیر درست نیویگیشن اندراجات، اور API رینڈرنگ مسائل جلدی ناکام ہوں۔