# CLI حوالہ

Co-op Translator یہ کمانڈ لائن اندراج پوائنٹس انسٹال کرتا ہے:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

کمانڈز `translate`، `evaluate`، `migrate-links` اور `co-op-review` کو `co_op_translator.__main__` کے ذریعے بھیجا جاتا ہے، جو کال کیے گئے اسکرپٹ کے نام کی بنیاد پر کمانڈ کے نفاذ کا انتخاب کرتا ہے۔ MCP سرور براہِ راست `co_op_translator.mcp.server` استعمال کرتا ہے۔

اگر آپ CLI، Python API، اور MCP کے درمیان فیصلہ کر رہے ہیں تو [اپنا ورک فلو منتخب کریں](workflows.md) سے شروع کریں۔

## پہلی بار CLI کا بہاؤ

اگر آپ ٹرمینل سے Co-op Translator استعمال کر رہے ہیں تو یہاں سے شروع کریں:

1. ایک LLM پرووائیڈر کو ترتیب دیں جیسا کہ [ترتیب](configuration.md) میں بیان کیا گیا ہے۔
2. اس مواد کی قسم منتخب کریں جسے آپ ترجمہ کرنا چاہتے ہیں۔
3. سب سے پہلے ایک ہدف شدہ کمانڈ چلائیں، مثلاً صرف Markdown کا ترجمہ۔
4. بڑی ریپوزٹری تبدیلیوں سے پہلے `--dry-run` استعمال کریں۔
5. ترجمہ کے بعد ساخت اور تازگی چیک کرنے کے لیے `co-op-review` استعمال کریں۔

| مقصد | شروع کرنے کے لیے کمانڈ |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP سرور](mcp.md) instead of running CLI commands directly. |

## translate

Markdown فائلیں، نوٹ بکس، اور تصویراتی متن کو ایک یا زیادہ ہدف زبانوں میں ترجمہ کریں۔

```bash
translate -l "ko ja fr"
```

### عام مثالیں

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

Update existing translations by deleting and recreating them:

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

### اختیارات

| آپشن | ضروری | تفصیل |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | خالی جگہ سے جدا کیے گئے زبان کوڈز، جیسے `"es fr de"`، یا `"all"`. |
| `-r`, `--root-dir` | No | پروجیکٹ روٹ۔ ڈیفالٹ موجودہ ڈائریکٹری ہے۔ |
| `-u`, `--update` | No | منتخب زبانوں کے موجودہ تراجم کو حذف کر کے دوبارہ بنائیں۔ |
| `-img`, `--images` | No | صرف امیج فائلوں کا ترجمہ کریں۔ |
| `-md`, `--markdown` | No | صرف Markdown فائلوں کا ترجمہ کریں۔ |
| `-nb`, `--notebook` | No | صرف Jupyter نوٹ بک فائلوں کا ترجمہ کریں۔ |
| `-d`, `--debug` | No | کنسول میں ڈیبگ لاگنگ فعال کریں۔ |
| `-s`, `--save-logs` | No | DEBUG سطح کے لاگز `<root-dir>/logs/` کے تحت محفوظ کریں۔ |
| `-x`, `--fix` | No | پچھلے جائزے کے نتائج کی بنیاد پر کم اعتماد والے Markdown فائلوں کو دوبارہ ترجمہ کریں۔ |
| `-c`, `--min-confidence` | No | `--fix` کے لیے اعتماد کی حد۔ ڈیفالٹ `0.7` ہے۔ |
| `--add-disclaimer`, `--no-disclaimer` | No | مشینی ترجمے کے ڈس کلیمر شامل کریں یا دبائیں۔ CLI میں ڈیفالٹ طور پر فعال ہے۔ |
| `-f`, `--fast` | No | متروک تیز امیج موڈ۔ |
| `-y`, `--yes` | No | پرامپٹس کو خود بخود تصدیق کریں، CI میں مفید۔ |
| `--repo-url` | No | README زبانوں کی جدول میں sparse-checkout مشورے کے لیے استعمال ہونے والا repository URL۔ |
| `--migrate-language-folders` | No | وراثتی عرفی فولڈرز، جیسے `cn` یا `tw`، کو معیاری BCP 47 فولڈرز میں ری نیم کریں۔ |
| `--dry-run` | No | زبان فولڈر مائیگریشن اور ترجمے کے اندازوں کا پیش منظر دیکھیں بغیر فائلیں لکھے۔ |

اگر کوئی قسم کا فلیگ فراہم نہ کیا گیا ہو تو `translate` Markdown، نوٹ بکس، اور تصاویر کو پروسیس کرتا ہے۔ تصویر کے ترجمے کے لیے Azure AI Vision کنفیگریشن ضروری ہے۔

## evaluate

ایک زبان کے لیے ترجمہ شدہ Markdown کے معیار کا جائزہ لیں۔

!!! warning "تجرباتی"
    `evaluate` تجرباتی ہے۔ یہ قواعد پر مبنی اور LLM پر مبنی کوالٹی چیکس استعمال کر سکتا ہے، جائزہ کے نتائج کو ترجمہ میٹاڈیٹا میں لکھتا ہے، اور اس کا اسکورنگ ماڈل اور میٹاڈیٹا رویہ بدل سکتا ہے۔

```bash
evaluate -l "ko"
```

### عام مثالیں

Use a stricter low-confidence threshold:

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

### اختیارات

| آپشن | ضروری | تفصیل |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | جائزہ کے لیے ایک زبان کا کوڈ۔ عرفی کوڈ معیاری کیے جاتے ہیں۔ |
| `-r`, `--root-dir` | No | پروجیکٹ روٹ۔ ڈیفالٹ موجودہ ڈائریکٹری ہے۔ |
| `-c`, `--min-confidence` | No | کم اعتماد تراجم کی فہرست بناتے وقت استعمال ہونے والی حد۔ ڈیفالٹ `0.7` ہے۔ |
| `-d`, `--debug` | No | ڈیبگ لاگنگ فعال کریں۔ |
| `-s`, `--save-logs` | No | DEBUG سطح کے لاگز `<root-dir>/logs/` کے تحت محفوظ کریں۔ |
| `-f`, `--fast` | No | صرف قواعد پر مبنی تشخیص۔ |
| `-D`, `--deep` | No | صرف LLM پر مبنی تشخیص۔ |

ڈفالٹ کے طور پر، `evaluate` دونوں قواعد پر مبنی اور LLM پر مبنی تشخیص استعمال کرتا ہے۔ نتائج ترجمہ میٹاڈیٹا میں لکھے جاتے ہیں اور کنسول میں خلاصہ کیے جاتے ہیں۔

## co-op-review

API اسناد کے بغیر طے شدہ ترجمہ مرمت چیکس چلائیں۔

!!! note "بیٹا"
    `co-op-review` ایک بیٹا متعین جائزہ کمانڈ ہے۔ یہ ماڈل پرووائیڈرز کو کال نہیں کرتا اور فائلیں نہیں لکھتا، مگر اس کے چیکس اور مسئلے کے آؤٹ پٹ اسکیمہ میں تبدیلی آ سکتی ہے۔

```bash
co-op-review -l "ko"
```

### عام مثالیں

Review Korean and Japanese translations from the current directory:

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

Review only source files changed against a base ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Print GitHub-flavored Markdown output for CI summaries:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### اختیارات

| آپشن | ضروری | تفصیل |
| --- | --- | --- |
| `-l`, `--language-code` | No | جائزہ کے لیے زبان کا کوڈ۔ اسے متعدد بار یا اسپیس سے جدا قدر کے طور پر پاس کیا جا سکتا ہے۔ ڈیفالٹ تمام دریافت شدہ تراجم کی زبانیں ہیں۔ |
| `-r`, `--root-dir` | No | پروجیکٹ روٹ۔ ڈیفالٹ موجودہ ڈائریکٹری ہے۔ |
| `--changed-from` | No | Git ریف جو جائزہ کو صرف تبدیل شدہ سورس فائلوں تک محدود کرنے کے لیے استعمال ہوتا ہے۔ |
| `--format` | No | آؤٹ پٹ فارمیٹ: `text` یا `github`۔ ڈیفالٹ `text` ہے۔ |

`co-op-review` فی الحال گمشدہ ترجمہ شدہ فائلوں، گمشدہ یا پرانے ترجمہ میٹاڈیٹا، Markdown فرونٹ میٹر اور کوڈ فینس کی سالمیت، غلط ترجمہ شدہ نوٹ بک JSON، اور مقامی Markdown یا تصویر لنک اہداف کے گم ہونے کی جانچ کرتا ہے۔ گم شدہ لنکس بطور وارننگ ہوتے ہیں؛ ساختی اور تازگی کے مسائل کمانڈ کو ناکام قرار دیتے ہیں۔

## co-op-translator-mcp

ایجنٹس، ایڈیٹرز، اور MCP-مطابقت رکھنے والے کلائنٹس کے لیے Co-op Translator MCP سرور چلائیں۔

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP سرور](mcp.md) guide for client configuration, tools, resources, and safety notes.

### اختیارات

| آپشن | ضروری | تفصیل |
| --- | --- | --- |
| `--transport` | No | MCP ٹرانسپورٹ: `stdio`, `streamable-http`, یا `sse`۔ ڈیفالٹ `stdio` ہے۔ |

## migrate-links

ترجمہ شدہ Markdown فائلوں کو دوبارہ پروسیس کریں اور نوٹ بک لنکس کو اپ ڈیٹ کریں تاکہ جب دستیاب ہوں تو وہ ترجمہ شدہ نوٹ بکس کی طرف اشارہ کریں۔

```bash
migrate-links -l "ko ja"
```

### عام مثالیں

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

Process all supported languages without confirmation:

```bash
migrate-links -l "all" -y
```

Only rewrite links when translated notebooks exist:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### اختیارات

| آپشن | ضروری | تفصیل |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | خلا سے جدا زبان کوڈز، یا `"all"`. |
| `-r`, `--root-dir` | No | پروجیکٹ روٹ۔ ڈیفالٹ موجودہ ڈائریکٹری ہے۔ |
| `--image-dir` | No | ترجمہ شدہ تصویر کی ڈائریکٹری روٹ کے لحاظ سے۔ ڈیفالٹ `translated_images` ہے۔ |
| `--dry-run` | No | وہ فائلیں دکھائیں جو بدلیں گی بغیر اپڈیٹس لکھے۔ |
| `--fallback-to-original`, `--no-fallback-to-original` | No | جب ترجمہ شدہ نوٹ بکس موجود نہ ہوں تو اصل نوٹ بک لنکس استعمال کریں۔ ڈیفالٹ طور پر فعال ہے۔ |
| `-d`, `--debug` | No | ڈیبگ لاگنگ فعال کریں۔ |
| `-s`, `--save-logs` | No | DEBUG سطح کے لاگز `<root-dir>/logs/` کے تحت محفوظ کریں۔ |
| `-y`, `--yes` | No | جب تمام زبانیں پروسیس کر رہے ہوں تو پرامپٹس خود بخود تصدیق کریں۔ |

## Environment

تمام کمانڈز کے لیے ایک ترتیب شدہ LLM پرووائیڈر ضروری ہے:

```bash
# ایزور اوپن اے آئی
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# یا اوپن اے آئی
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## آؤٹ پٹ کی ساخت

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

## کاپی-پیست CLI مثالیں

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

Preview Markdown translation without writing files:

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