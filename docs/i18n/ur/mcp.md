# MCP سرور

Co-op Translator میں ایجنٹس، ایڈیٹرز، اور MCP-مطابق کلائنٹس کے لیے ایک Model Context Protocol سرور شامل ہے۔

ڈیفالٹ لوکل سیٹ اپ کے لیے، صارفین الگ سرور ہاتھ سے نہیں چلاتے۔ وہ اپنا MCP کلائنٹ ترتیب دیتے ہیں، اور جب Co-op Translator ٹولز کی ضرورت ہوتی ہے تو کلائنٹ خودکار طور پر `co-op-translator-mcp` کو `stdio` کے ذریعے شروع کرتا ہے۔

اگر آپ CLI، Python API، اور MCP کے درمیان فیصلہ کر رہے ہیں تو [اپنا ورک فلو منتخب کریں](workflows.md) سے شروع کریں۔

جب کسی ایجنٹ یا ایڈیٹر کو Co-op Translator کو براہِ راست کال کرنا چاہیے تو MCP استعمال کریں:

| صارف کا ہدف | MCP ٹولز |
| --- | --- |
| ایک Markdown دستاویز، نوٹ بک، یا تصویر کا ترجمہ کریں | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| میزبان ایجنٹ ماڈل کے ساتھ Markdown یا نوٹ بک مواد کا ترجمہ کریں | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ترجمہ شدہ Markdown یا نوٹ بک لنکس کو آؤٹ پٹ راستہ منتخب کرنے کے بعد دوبارہ لکھیں | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI کی طرح پورے ریپوزیٹری کا ترجمہ کریں | `run_translation`, `translate_project` |
| LLM اسناد کے بغیر ترجمہ شدہ آؤٹ پٹ کا جائزہ لیں | `run_review` |
| صلاحیتیں اور ماحول کی حیثیت کا جائزہ لیں | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP سرور وہی عمومی پبلک Python API لپیٹتا ہے جیسا کہ [Python API](api.md) میں دستاویز شدہ ہے۔ پرووائیڈر-بیکڈ ٹولز وہی کنفیگر کیے گئے پرووائیڈرز استعمال کرتے ہیں جو CLI اور Python API استعمال کرتے ہیں۔ ایجنٹ-معاون ٹولز MCP ہوسٹ ایجنٹ کے ترجمے کے لیے چنکس تیار کرتے ہیں، پھر حتمی Markdown یا نوٹ بک کو دوبارہ بنانے کے لیے Co-op Translator استعمال کرتے ہیں۔

## مرحلہ 1: Co-op Translator انسٹال اور ترتیب دیں

اپنے MCP کلائنٹ کے استعمال کرنے والے Python ماحول میں Co-op Translator انسٹال کریں:

```bash
pip install co-op-translator
```

اس ریپوزیٹری سے لوکل ڈیولپمنٹ کے لیے، پیکج کو ایڈیٹیبل موڈ میں انسٹال کریں:

```bash
pip install -e .
```

وہ ترجمہ موڈ منتخب کریں جو آپ کا MCP کلائنٹ استعمال کرے گا:

| موڈ | اس کے لیے استعمال کریں | اسناد |
| --- | --- | --- |
| پرووائیڈر-بیکڈ | Co-op Translator `translate_markdown_content`، `translate_notebook_content`، `translate_image_content`، یا `run_translation` کو کال کرتا ہے۔ | ترجمہ کے لیے Azure OpenAI، OpenAI، یا Anthropic درکار ہیں۔ تصویر کے ترجمے کے لیے Azure AI Vision بھی درکار ہے۔ |
| ایجنٹ-معاون | MCP ہوسٹ ایجنٹ `start_markdown_agent_translation` یا `start_notebook_agent_translation` کی طرف سے واپس کیے گئے چنکس کا ترجمہ کرتا ہے۔ | Markdown یا نوٹ بک چنکس کے لیے Co-op Translator LLM پرووائیڈر اسناد کی ضرورت نہیں۔ تصویر کا ترجمہ ابھی ایجنٹ-معاون موڈ کے تحت شامل نہیں ہے۔ |

اگر آپ Codex یا Claude Code جیسے ایجنٹ کے اندر Markdown یا نوٹ بک ترجمے سے شروع کر رہے ہیں تو ایجنٹ-معاون موڈ سے شروع کریں۔ جب آپ چاہتے ہیں کہ Co-op Translator خود آپ کے کنفیگر کیے گئے پرووائیڈرز کو کال کرے، جب آپ تصاویر کا ترجمہ کر رہے ہوں، یا جب آپ CLI کی طرح ریپوزیٹری-سطح ترجمہ چلا رہے ہوں تو پرووائیڈر-بیکڈ موڈ استعمال کریں۔

پرووائیڈر-بیکڈ ورک فلو کے لیے ایک پرووائیڈر ترتیب دیں:

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

# یا این تھروپک
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

پرووائیڈر-بیکڈ تصویر کے ترجمے کے لیے اضافی طور پر درج ذیل درکار ہیں:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    ایجنٹ-معاون موڈ فی الوقت Markdown اور نوٹ بک کے Markdown سیلز کو کور کرتا ہے۔ تصویر کا ترجمہ ابھی بھی پرووائیڈر-بیکڈ امیج پائپ لائن استعمال کرتا ہے اور OCR اور لے آؤٹ-آگاہ رینڈرنگ کے لیے Azure AI Vision درکار ہے۔

## مرحلہ 2: اپنا MCP کلائنٹ ترتیب دیں

عام لوکل `stdio` سیٹ اپ کے لیے، اپنے MCP کلائنٹ کی کنفیگریشن میں Co-op Translator شامل کریں۔ کلائنٹ عمل کو خود بخود شروع اور بند کرے گا۔

انسٹال شدہ پیکج کی کنفیگریشن:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Windows پر سورس چیک آؤٹ کنفیگریشن:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

macOS یا Linux پر سورس چیک آؤٹ کنفیگریشن:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

MCP کلائنٹ کنفیگریشن تبدیل کرنے کے بعد، کلائنٹ کو دوبارہ شروع یا ری لوڈ کریں تاکہ وہ نیا سرور دریافت کر سکے۔

## مرحلہ 3: کلائنٹ میں سرور کی تصدیق کریں

MCP کلائنٹ سے دستیاب ٹولز کی فہرست پوچھیں، یا پہلے پڑھنے-صرف ہیلپرز میں سے کسی ایک کو کال کریں:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

مفید ابتدائی چیکز:

| ٹول | کیا چیک کریں |
| --- | --- |
| `get_api_overview` | سرور قابلِ رسائی ہونے کی تصدیق کرتا ہے اور دستیاب ورک فلو دکھاتا ہے۔ |
| `list_supported_languages` | پیکج شدہ زبان کے ڈیٹا کے لوڈ ہونے کی تصدیق کرتا ہے۔ |
| `get_configuration_status` | LLM اور Vision پرووائیڈر کی دستیابی کی تصدیق کرتا ہے بغیر خفیہ قدروں کو ظاہر کیے۔ |

## مرحلہ 4: ایک ورک فلو منتخب کریں

### انفرادی فائلز یا دستاویزات کا ترجمہ کریں

جب MCP کلائنٹ کے پاس پہلے سے دستاویز کا مواد یا تصویر کا راستہ موجود ہو اور Co-op Translator کو کنفیگر کیے گئے ترجمہ پرووائیڈرز کو کال کرنا چاہیے تو پرووائیڈر-بیکڈ مواد کے ٹولز استعمال کریں۔

Markdown کے لیے:

1. `document`، `language_code`، اور اختیاری طور پر `source_path` کے ساتھ `translate_markdown_content` کال کریں۔
2. اگر ترجمہ شدہ نتیجہ Co-op Translator آؤٹ پٹ لے آؤٹ میں لکھا جائے گا تو `rewrite_markdown_paths` کال کریں۔
3. کلائنٹ کو حتمی `content` لکھنے یا واپس کرنے دیں۔

نوٹ بکس کے لیے:

1. نوٹ بک JSON اور `language_code` کے ساتھ `translate_notebook_content` کال کریں۔
2. اگر ترجمہ شدہ نوٹ بک لنکس کو ہدف راستے کے لیے ایڈجسٹ کرنے کی ضرورت ہو تو `rewrite_notebook_paths` کال کریں۔
3. حتمی نوٹ بک JSON لکھیں یا واپس کریں۔

تصاویر کے لیے:

1. `image_path`، `language_code`، اور اختیاری `root_dir` یا `fast_mode` کے ساتھ `translate_image_content` کال کریں۔
2. واپس کیے گئے `data_base64` اور `mime_type` کو پڑھیں۔
3. اگر `output_path` دیا گیا ہے تو ترجمہ شدہ تصویر اس راستے پر بھی محفوظ کی جاتی ہے۔

مواد کے ٹولز پروجیکٹ کی دریافت، میٹا ڈیٹا اپڈیٹس، دستبرداری، یا خودکار راستہ دوبارہ تحریر نہیں کرتے۔ اگر آپ چاہتے ہیں کہ میزبان ایجنٹ Co-op Translator LLM پرووائیڈر اسناد کے بغیر Markdown یا نوٹ بک چنکس کا ترجمہ کرے، تو نیچے دیے گئے ایجنٹ-معاون ورک فلو کا استعمال کریں۔

### میزبان ایجنٹ ماڈل کے ساتھ ترجمہ کریں

جب آپ چاہیں کہ MCP ہوسٹ ایجنٹ، مثلاً کوڈنگ اسسٹنٹ، ترجمہ شدہ متن تیار کرے بجائے اس کے کہ Co-op Translator کے لیے کسی LLM پرووائیڈر کو ترتیب دیں، تو ایجنٹ-معاون ٹولز استعمال کریں۔

چَیٹ بیسڈ MCP کلائنٹ میں، آپ عام طور پر خود ٹول JSON لکھنے کی ضرورت نہیں رکھتے۔ ایجنٹ سے کہیں کہ وہ ایجنٹ-معاون ورک فلو استعمال کرے:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

نوٹ بکس کے لیے، اسی نمونے کا استعمال کریں:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

اگر آپ کا MCP کلائنٹ سرور پرامپٹس کو سپورٹ کرتا ہے تو کلائنٹ کو اسی ورک فلو ہدایات لوڈ کروانے کے لیے `agent_assisted_markdown_translation_prompt` استعمال کریں۔

Markdown کے لیے:

1. `document`، `language_code`، اور اختیاری طور پر `source_path` کے ساتھ `start_markdown_agent_translation` کال کریں۔
2. ہر واپس کیے گئے چنک کو میزبان ایجنٹ میں چنک کے `prompt` کی پیروی کرتے ہوئے ترجمہ کریں۔
3. اصل `job` اور ترجمہ شدہ چنکس کو `chunk_id` اور `translated_text` استعمال کرتے ہوئے `finish_markdown_agent_translation` کال کریں۔
4. اگر مواد کو ترجمہ شدہ ہدف راستے میں لکھا جائے گا تو `rewrite_markdown_paths` کال کریں۔

نوٹ بکس کے لیے:

1. نوٹ بک JSON اور `language_code` کے ساتھ `start_notebook_agent_translation` کال کریں۔
2. میزبان ایجنٹ میں ہر واپس کیے گئے چنک کا ترجمہ کریں۔
3. اصل `job` اور ترجمہ شدہ چنکس کے ساتھ `finish_notebook_agent_translation` کال کریں۔
4. اگر ترجمہ شدہ نوٹ بک لنکس کو ہدف-راستے کے مطابق ایڈجسٹ کرنے کی ضرورت ہو تو `rewrite_notebook_paths` کال کریں۔

ایجنٹ-معاون ٹولز Co-op Translator سے کنفیگر کیے گئے LLM پرووائیڈر کو کال نہیں کرتے۔ میزبان ایجنٹ واپس کیے گئے چنکس کے ترجمے کا ذمہ دار ہے۔ Co-op Translator Markdown چنکنگ، پلیس ہولڈر برقرار رکھنا، فرنٹ میٹر کی بحالی، نوٹ بک سیل کی جگہ بندی، اور ترجمے کے بعد نارملائزیشن کو ہینڈل کرتا ہے۔

### پورے ریپوزیٹری کا ترجمہ کریں

جب صارف چاہتا ہے کہ Co-op Translator `translate` CLI کی طرح عمل کرے تو `run_translation` استعمال کریں۔

ریپوزیٹری ترجمہ کی ڈیفالٹ سیٹنگ `dry_run=true` ہے تا کہ فائلوں میں تبدیلی سے پہلے ایجنٹ دائرہ کار کا معائنہ کر سکے:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

`run_translation` کے نتیجے میں ایک `events` اررے شامل ہوتا ہے جس میں ورژن شدہ
`co-op.translation.event.v1` پروگریس ایونٹس ہوتے ہیں۔ MCP کلائنٹس کو ایسے فیلڈز استعمال کرنے چاہئیں
جیسے `type`، `stage_key`، `completed`، `total`، اور `current_path` بجائے
کیپچر شدہ کنسول ٹیکسٹ کو پارس کرنے کے۔ `json_events_path` پاس کریں تاکہ وہ ایونٹس
ایک NDJSON فائل میں بھی لکھے جائیں۔

لکھنے کی اجازت دینے کے لیے، کال کرنے والے کو دونوں `dry_run=false` اور `confirm_write=true` سیٹ کرنا ہوں گے:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` کو `run_translation` کے لیے کمپٹیبیلٹی عرف کے طور پر ظاہر کیا گیا ہے۔

### ترجمہ شدہ آؤٹ پٹ کا جائزہ لیں

ایسے متعین چیکس کے لیے جو LLM یا Vision اسناد کی ضرورت نہیں رکھتے `run_review` استعمال کریں:

!!! note "Beta"
    MCP بیٹا `run_review` API کو ظاہر کرتا ہے۔ یہ پڑھنے-صرف ریویو ورک فلو کے لیے محفوظ ہے، لیکن ریویو چیکس اور ایشو اسکیمیں تبدیل ہو سکتی ہیں۔

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

نتیجہ میں جب دستیاب ہو تو کیپچر شدہ متن آؤٹ پٹ اور ایک منظم ریویو خلاصہ شامل ہوتا ہے۔

## دستی سرور رنز

دستی رنز بنیادی طور پر ڈیبگنگ کے لیے یا اُن ٹرانسپورٹس کے لیے ہیں جو طویل مدت چلنے والے سرورز کی طرح عمل کرتے ہیں۔

ڈیفالٹ stdio سرور کا ڈیبگ کریں:

```bash
co-op-translator-mcp
```

سورس چیک آؤٹ سے چلائیں:

```bash
python -m co_op_translator.mcp.server
```

لمبی عمر والا HTTP یا SSE سرور چلائیں:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

لوکل ایڈیٹر اور ایجنٹ انٹیگریشنز کے لیے، مرحلہ 2 میں کلائنٹ-مینجڈ `stdio` کنفیگریشن کو ترجیح دیں۔

## ٹولز

| ٹول | مقصد | فائلیں لکھتا ہے |
| --- | --- | --- |
| `translate_markdown_content` | ایک Markdown سٹرنگ کا ترجمہ کریں۔ | نہیں |
| `translate_notebook_content` | نوٹ بک JSON میں Markdown سیلز کا ترجمہ کریں۔ | نہیں |
| `translate_image_content` | ایک تصویر میں متن کا ترجمہ کریں اور base64 تصویر کا ڈیٹا واپس کریں۔ | اختیاری، صرف جب `output_path` فراہم کیا گیا ہو |
| `start_markdown_agent_translation` | Co-op Translator LLM اسناد کے بغیر میزبان ایجنٹ کے ترجمے کے لیے Markdown چنکس تیار کریں۔ | نہیں |
| `finish_markdown_agent_translation` | میزبان-ایجنٹ کے ترجمہ شدہ چنکس سے Markdown کو دوبارہ بنائیں۔ | نہیں |
| `start_notebook_agent_translation` | میزبان ایجنٹ کے ترجمے کے لیے نوٹ بک Markdown-سیل چنکس تیار کریں۔ | نہیں |
| `finish_notebook_agent_translation` | میزبان-ایجنٹ کے ترجمہ شدہ چنکس سے نوٹ بک JSON کو دوبارہ بنائیں۔ | نہیں |
| `rewrite_markdown_paths` | ترجمہ شدہ ہدف کے لیے Markdown باڈی اور فرنٹ میٹر راستوں کو دوبارہ لکھیں۔ | نہیں |
| `rewrite_notebook_paths` | نوٹ بک Markdown سیلز کے اندر راستوں کو دوبارہ لکھیں۔ | نہیں |
| `run_translation` | CLI کی طرح پروجیکٹ-لیول ترجمہ چلائیں۔ | ہاں جب `dry_run=false` اور `confirm_write=true` ہو |
| `translate_project` | `run_translation` کے لیے کمپٹیبیلٹی عرف۔ | ہاں جب `dry_run=false` اور `confirm_write=true` ہو |
| `run_review` | متعین ریویو چیکس چلائیں۔ | نہیں |
| `get_configuration_status` | کنفیگر کیے گئے LLM اور Vision پرووائیڈرز کی رپورٹ کریں بغیر خفیہ معلومات ظاہر کیے۔ | نہیں |
| `list_supported_languages` | مدد کردہ ہدف زبان کے کوڈز کی فہرست دیں۔ | نہیں |
| `get_api_overview` | دستیاب MCP ورک فلو اور ٹولز کی وضاحت کریں۔ | نہیں |

## وسائل

| ذریعہ URI | مقصد |
| --- | --- |
| `co-op://api` | ورک فلو اور ٹولز کا JSON جائزہ۔ |
| `co-op://supported-languages` | مدد کردہ زبان کے کوڈز کی JSON فہرست۔ |
| `co-op://configuration` | خفیہ معلومات کے بغیر پرووائیڈر دستیابی کا JSON خلاصہ۔ |

## پرامپٹس

| پرامپٹ | مقصد |
| --- | --- |
| `translate_markdown_document_prompt` | مواد کے ترجمے اور اختیاری راستہ دوبارہ تحریر کے ذریعے MCP کلائنٹ کی رہنمائی کریں۔ |
| `agent_assisted_markdown_translation_prompt` | بغیر Co-op Translator LLM پرووائیڈر اسناد کے میزبان-ایجنٹ Markdown ترجمہ کے ذریعے MCP کلائنٹ کی رہنمائی کریں۔ |
| `translate_repository_prompt` | پہلے dry-run کرنے والے ریپوزیٹری ترجمہ کے ذریعے MCP کلائنٹ کی رہنمائی کریں۔ |

## کاپی-پیسٹ مثالیں

Markdown مواد کا ترجمہ کریں:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

ترجمہ شدہ Markdown لنکس کو دوبارہ لکھیں:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

میزبان ایجنٹ ماڈل کے ساتھ Markdown کا ترجمہ کریں:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

جب میزبان ایجنٹ ہر واپس کیے گئے چنک کا ترجمہ کر لے، تو `start_markdown_agent_translation` کی طرف سے واپس کیے گئے مکمل `job` آبجیکٹ کے ساتھ جاب ختم کریں:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

ریپوزیٹری ترجمہ کا پری ویو کریں:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## مسئلہ حل کرنا

| مسئلہ | کیا آزمانا ہے |
| --- | --- |
| MCP کلائنٹ `co-op-translator-mcp` نہیں ڈھونڈ پا رہا۔ | مطلق Python executable راستہ اور `["-m", "co_op_translator.mcp.server"]` سورس چیک آؤٹ کنفیگریشن استعمال کریں۔ |
| سرور لسٹ میں ہے لیکن ترجمہ ناکام ہو جاتا ہے۔ | `get_configuration_status` کال کریں اور تصدیق کریں کہ کوئی LLM پرووائیڈر دستیاب ہے۔ |
| آپ بغیر پرووائیڈر اسناد کے Markdown یا نوٹ بک کا ترجمہ چاہتے ہیں۔ | `start_markdown_agent_translation` / `finish_markdown_agent_translation` یا نوٹ بک کے متبادل استعمال کریں تاکہ میزبان ایجنٹ چنکس کا ترجمہ کرے۔ |
| تصویر کا ترجمہ ناکام ہو جاتا ہے۔ | Azure AI Vision متغیرات سیٹ ہونے کی تصدیق کریں اور `get_configuration_status` کال کریں۔ |
| ریپوزیٹری ترجمہ فائلیں نہیں لکھ رہا۔ | واضح صارف کی منظوری کے بعد ہی `dry_run=false` اور `confirm_write=true` سیٹ کریں۔ |
| کلائنٹ کنفیگ میں تبدیلیاں ظاہر نہیں ہوتیں۔ | MCP کلائنٹ کو دوبارہ شروع یا ری لوڈ کریں۔ |

## حفاظتی نوٹس

- MCP ٹول کالز ہوسٹ ایپلیکیشن کے ذریعے ماڈل-کنٹرولڈ ہوتی ہیں، لہٰذا ریپوزیٹری ترجمہ بطورِ ڈیفالٹ dry-run ہوتا ہے۔
- پورا ریپوزیٹری ترجمہ بہت سی فائلیں بنا، اپڈیٹ، یا حذف کر سکتا ہے۔ `confirm_write=true` سیٹ کرنے سے پہلے واضح صارف کی منظوری لازم کریں۔
- configuration status ٹول کبھی API keys، endpoints، یا دیگر خفیہ قدریں واپس نہیں کرتا۔
- تصویر کا ترجمہ base64 امیج ڈیٹا واپس کرتا ہے۔ بڑی تصاویر بڑے ٹول جوابات پیدا کر سکتی ہیں۔
- ایجنٹ-معاون ٹولز سورس چنکس اور پرامپٹس MCP ہوسٹ کو واپس کرتے ہیں۔ انہیں صرف ایسے مواد کے ساتھ استعمال کریں جسے صارف اس میزبان ایجنٹ ماڈل کو بھیجنے میں آرام محسوس کرے۔