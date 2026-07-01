# MCP سرور

Co-op Translator میں ایجنٹس، ایڈیٹرز، اور MCP-مطابقت رکھنے والے کلائنٹس کے لیے ایک Model Context Protocol سرور شامل ہے۔

بنیادی مقامی سیٹ اپ کے لیے، صارفین الگ سرور دستی طور پر نہیں چلاتے۔ وہ اپنے MCP کلائنٹ کو کنفیگر کرتے ہیں، اور جب کلائنٹ کو Co-op Translator ٹولز کی ضرورت ہوتی ہے تو کلائنٹ خودکار طور پر `co-op-translator-mcp` کو `stdio` کے ذریعے شروع کرتا ہے۔

اگر آپ CLI، Python API، اور MCP کے درمیان فیصلہ کر رہے ہیں، تو [Choose Your Workflow](workflows.md) سے شروع کریں۔

جب کسی ایجنٹ یا ایڈیٹر کو Co-op Translator کو براہِ راست کال کرنا چاہیے تو MCP استعمال کریں:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP سرور وہی پبلک Python API لپیٹتا ہے جو [Python API](api.md) میں دستاویزی ہے۔ Provider-backed ٹولز وہی کنفیگرڈ پرووائیڈرز استعمال کرتے ہیں جو CLI اور Python API استعمال کرتے ہیں۔ ایجنٹ-مدد یافتہ ٹولز MCP ہوسٹ ایجنٹ کے لیے ٹکڑے تیار کرتے ہیں تاکہ وہ تراجم کریں، پھر Co-op Translator حتمی Markdown یا نوٹ بک کو دوبارہ تعمیر کرتا ہے۔

## Step 1: Install and Configure Co-op Translator

اپنے MCP کلائنٹ کے استعمال کرنے والے Python ماحول میں Co-op Translator انسٹال کریں:

```bash
pip install co-op-translator
```

اس مخزن سے مقامی ترقی کے لیے، پیکیج کو editable موڈ میں انسٹال کریں:

```bash
pip install -e .
```

اپنے MCP کلائنٹ کے استعمال کے لیے ترجمہ موڈ منتخب کریں:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator کالز کرتا ہے `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, یا `run_translation`. | Markdown اور نوٹ بک کے تراجم کے لیے Azure OpenAI یا OpenAI درکار ہیں۔ تصویر کے ترجمے کے لیے اضافی طور پر Azure AI Vision بھی درکار ہے۔ |
| Agent-assisted | MCP ہوسٹ ایجنٹ ان چنکس کا ترجمہ کرتا ہے جو `start_markdown_agent_translation` یا `start_notebook_agent_translation` سے واپس کیے جاتے ہیں۔ | Markdown یا نوٹ بک چنکس کے لیے Co-op Translator LLM پرووائیڈر کریڈینشلز درکار نہیں ہیں۔ ایجنٹ-مدد یافتہ موڈ میں ابھی تک تصویر کا ترجمہ شامل نہیں ہے۔ |

اگر آپ Codex یا Claude Code جیسے ایجنٹ کے اندر Markdown یا نوٹ بک ترجمہ شروع کر رہے ہیں، تو ایجنٹ-مدد یافتہ موڈ سے آغاز کریں۔ جب آپ چاہتے ہیں کہ Co-op Translator خود آپ کے کنفیگرڈ پرووائیڈرز کو کال کرے، جب آپ تصاویر کا ترجمہ کر رہے ہوں، یا جب آپ CLI کی طرح repository-سطح کا ترجمہ چلا رہے ہوں تو provider-backed موڈ استعمال کریں۔

صرف provider-backed ورک فلو کے لیے پرووائیڈر کریڈینشلز کنفیگر کریں:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed تصویر کے ترجمے کے لیے اضافی طور پر یہ درکار ہے:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted موڈ فی الحال Markdown اور نوٹ بک کے Markdown سیلز کو کور کرتا ہے۔ تصویر کا ترجمہ اب بھی provider-backed امیج پائپ لائن استعمال کرتا ہے اور OCR اور layout-aware rendering کے لیے Azure AI Vision درکار ہے۔

## Step 2: Configure Your MCP Client

عام مقامی `stdio` سیٹ اپ کے لیے، Co-op Translator کو اپنے MCP کلائنٹ کنفیگریشن میں شامل کریں۔ کلائنٹ عمل کو خود بخود شروع اور بند کرے گا۔

انسٹال شدہ پیکیج کنفیگریشن:

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

MCP کلائنٹ کنفیگریشن تبدیل کرنے کے بعد، کلائنٹ کو دوبارہ شروع یا ری لوڈ کریں تاکہ وہ نئے سرور کو دریافت کر سکے۔

## Step 3: Verify the Server in the Client

MCP کلائنٹ سے دستیاب ٹولز کی فہرست طلب کریں، یا پہلے ان میں سے کسی read-only ہیلپر کو کال کریں:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

مفید ابتدائی چیکس:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | تصدیق کرتا ہے کہ سرور قابلِ پہنچ ہے اور دستیاب ورک فلو دکھاتا ہے۔ |
| `list_supported_languages` | تصدیق کرتا ہے کہ پیک شدہ زبان کا ڈیٹا لوڈ کیا جا سکتا ہے۔ |
| `get_configuration_status` | LLM اور Vision پرووائیڈر کی دستیابی کی تصدیق کرتا ہے بغیر خفیہ اقدار کو ظاہر کیے۔ |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

جب MCP کلائنٹ کے پاس پہلے سے دستاویز کا مواد یا تصویر کا پاتھ موجود ہو اور Co-op Translator کو کنفیگرڈ پرووائیڈرز کو کال کرنا چاہیے تو provider-backed content tools استعمال کریں۔

Markdown کے لیے:

1. `document`, `language_code`, اور اختیاری طور پر `source_path` کے ساتھ `translate_markdown_content` کال کریں۔
2. اگر ترجمہ شدہ نتیجہ Co-op Translator آؤٹ پٹ لے آؤٹ میں لکھا جائے گا تو `rewrite_markdown_paths` کال کریں۔
3. کلائنٹ کو حتمی `content` لکھنے یا واپس کرنے دیں۔

نوٹ بکس کے لیے:

1. نوٹ بک JSON اور `language_code` کے ساتھ `translate_notebook_content` کال کریں۔
2. اگر ترجمہ شدہ نوٹ بک کے لنکس کو ہدف راستے کے لیے ایڈجسٹ کرنے کی ضرورت ہو تو `rewrite_notebook_paths` کال کریں۔
3. حتمی نوٹ بک JSON لکھیں یا واپس کریں۔

تصاویر کے لیے:

1. `image_path`, `language_code`, اور اختیاری `root_dir` یا `fast_mode` کے ساتھ `translate_image_content` کال کریں۔
2. واپس کردہ `data_base64` اور `mime_type` پڑھیں۔
3. اگر `output_path` فراہم کیا گیا ہے، تو ترجمہ شدہ تصویر اس راستے پر بھی محفوظ کی جاتی ہے۔

کانٹینٹ ٹولز پروجیکٹ ڈسکوری، میٹا ڈیٹا اپڈیٹس، ڈس کلیمرز، یا خودکار راستہ دوبارہ لکھنے کو انجام نہیں دیتے۔ اگر آپ چاہتے ہیں کہ ہوسٹ ایجنٹ Markdown یا نوٹ بک چنکس کا ترجمہ کرے بغیر Co-op Translator LLM پرووائیڈر کریڈینشلز کے، تو نیچے دیا گیا ایجنٹ-مدد یافتہ ورک فلو استعمال کریں۔

### Translate with the Host Agent Model

ایجنٹ-مدد یافتہ ٹولز استعمال کریں جب آپ چاہتے ہیں کہ MCP ہوسٹ ایجنٹ، جیسے کہ ایک کوڈنگ اسسٹنٹ، ترجمہ شدہ متن پیدا کرے بجائے اس کے کہ آپ Co-op Translator کے لیے Azure OpenAI یا OpenAI ترتیب دیں۔

ایک چیٹ-بیسڈ MCP کلائنٹ میں، عام طور پر آپ کو خود ٹول JSON لکھنے کی ضرورت نہیں ہوتی۔ ایجنٹ سے کہیں کہ وہ ایجنٹ-مدد یافتہ ورک فلو استعمال کرے:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

نوٹ بکس کے لیے، اسی پیٹرن کو استعمال کریں:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

اگر آپ کا MCP کلائنٹ سرور پرومپٹس کی حمایت کرتا ہے تو `agent_assisted_markdown_translation_prompt` استعمال کریں تاکہ کلائنٹ وہی ورک فلو ہدایات لوڈ کرے۔

Markdown کے لیے:

1. `document`, `language_code`, اور اختیاری `source_path` کے ساتھ `start_markdown_agent_translation` کال کریں۔
2. ہوسٹ ایجنٹ میں ہر واپس کیے گئے چنک کو چنک `prompt` کی پیروی کرکے ترجمہ کریں۔
3. اصل `job` اور `chunk_id` اور `translated_text` استعمال کرتے ہوئے ترجمہ شدہ چنکس کے ساتھ `finish_markdown_agent_translation` کال کریں۔
4. اگر مواد کو ترجمہ شدہ ہدف راستے پر لکھا جائے گا تو `rewrite_markdown_paths` کال کریں۔

نوٹ بکس کے لیے:

1. نوٹ بک JSON اور `language_code` کے ساتھ `start_notebook_agent_translation` کال کریں۔
2. ہوسٹ ایجنٹ میں ہر واپس کیے گئے چنک کو ترجمہ کریں۔
3. اصل `job` اور ترجمہ شدہ چنکس کے ساتھ `finish_notebook_agent_translation` کال کریں۔
4. اگر ترجمہ شدہ نوٹ بک لنکس کے لیے ہدف راستہ ایڈجسٹمنٹ درکار ہو تو `rewrite_notebook_paths` کال کریں۔

ایجنٹ-مدد یافتہ ٹولز Co-op Translator سے Azure OpenAI یا OpenAI کو کال نہیں کرتے۔ واپس کیے گئے چنکس کا ترجمہ کرنے کی ذمہ داری ہوسٹ ایجنٹ پر ہے۔ Co-op Translator Markdown چنکنگ، پلیس ہولڈر برقرار رکھنا، فرنٹ میٹر کی دوبارہ تعمیر، نوٹ بک سیل کی جگہ بندی، اور بعد از ترجمہ نارملائزیشن کو ہینڈل کرتا ہے۔

### Translate an Entire Repository

جب صارف چاہتا ہے کہ Co-op Translator CLI کی طرح عمل کرے تو `run_translation` استعمال کریں۔

Repository ترجمہ پہلے سے `dry_run=true` پر ڈیفالٹ ہے تاکہ ایجنٹ فائل تبدیلیوں سے پہلے دائرہ کار کا جائزہ لے سکے:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

لکھائی کی اجازت دینے کے لیے، کال کرنے والے کو دونوں `dry_run=false` اور `confirm_write=true` سیٹ کرنا ضروری ہے:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` کو `run_translation` کے لیے مطابقتی عرف کے طور پر ایکسپوز کیا گیا ہے۔

### Review Translated Output

ایسے deterministic چیکس کے لیے جو LLM یا Vision کریڈینشلز کی ضرورت نہیں رکھتے `run_review` استعمال کریں:

!!! note "Beta"
    MCP بیٹا `run_review` API کو ایکسپوز کرتا ہے۔ یہ read-only ریویو ورک فلو کے لیے محفوظ ہے، لیکن ریویو چیکس اور ایشو اسکیمہ بدل سکتے ہیں۔

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

نتیجہ میں قید شدہ متن آؤٹ پٹ اور دستیاب ہونے پر ایک ساختی ریویو خلاصہ شامل ہوتا ہے۔

## Manual Server Runs

دستی رنز زیادہ تر ڈیبگنگ یا ایسے ٹرانسپورٹس کے لیے ہیں جو طویل مدتی سرور جیسا برتاؤ کرتے ہیں۔

ڈیفالٹ stdio سرور کو ڈیبگ کریں:

```bash
co-op-translator-mcp
```

سورس چیک آؤٹ سے چلائیں:

```bash
python -m co_op_translator.mcp.server
```

طویل العمری HTTP یا SSE سرور چلائیں:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

مقامی ایڈیٹر اور ایجنٹ انٹیگریشنز کے لیے، مرحلہ 2 میں کلائنٹ-مینیجڈ `stdio` کنفیگریشن کو ترجیح دیں۔

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | ایک Markdown سٹرنگ کا ترجمہ کریں۔ | No |
| `translate_notebook_content` | نوٹ بک JSON میں Markdown سیلز کا ترجمہ کریں۔ | No |
| `translate_image_content` | ایک تصویر میں متن کا ترجمہ کریں اور base64 امیج ڈیٹا واپس کریں۔ | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | ہوسٹ ایجنٹ کے لیے ایسے Markdown چنکس تیار کریں تاکہ وہ Co-op Translator LLM کریڈینشلز کے بغیر ترجمہ کریں۔ | No |
| `finish_markdown_agent_translation` | ہوسٹ ایجنٹ کے ترجمہ شدہ چنکس سے Markdown کو دوبارہ تعمیر کریں۔ | No |
| `start_notebook_agent_translation` | ہوسٹ ایجنٹ کے لیے نوٹ بک کے Markdown-سیل چنکس تیار کریں۔ | No |
| `finish_notebook_agent_translation` | ہوسٹ ایجنٹ کے ترجمہ شدہ چنکس سے نوٹ بک JSON کو دوبارہ تعمیر کریں۔ | No |
| `rewrite_markdown_paths` | ترجمہ شدہ ہدف کے لیے Markdown باڈی اور فرنٹ میٹر کے راستوں کو دوبارہ لکھیں۔ | No |
| `rewrite_notebook_paths` | نوٹ بک Markdown سیلز کے اندر راستوں کو دوبارہ لکھیں۔ | No |
| `run_translation` | CLI کی طرح پروجیکٹ-سطح کا ترجمہ چلائیں۔ | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | `run_translation` کے لیے مطابقتی عرف۔ | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | deterministic ریویو چیکس چلائیں۔ | No |
| `get_configuration_status` | کنفیگرڈ LLM اور Vision پرووائیڈر رپورٹ کریں بغیر خفیہ اقدار کو ظاہر کیے۔ | No |
| `list_supported_languages` | سپورٹ شدہ ہدف زبانوں کے کوڈز کی فہرست۔ | No |
| `get_api_overview` | دستیاب MCP ورک فلو اور ٹولز کی وضاحت کریں۔ | No |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | ورک فلو اور ٹولز کا JSON اوورویو۔ |
| `co-op://supported-languages` | سپورٹ شدہ زبان کوڈز کی JSON فہرست۔ |
| `co-op://configuration` | خفیہ اقدار کے بغیر پرووائیڈر دستیابی کا JSON خلاصہ۔ |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | MCP کلائنٹ کو مواد کے ترجمے اور اختیاری طور پر راستہ دوبارہ لکھنے کے ذریعے رہنمائی کریں۔ |
| `agent_assisted_markdown_translation_prompt` | MCP کلائنٹ کو ہوسٹ ایجنٹ کے ذریعے Markdown ترجمے کے لیے رہنمائی کریں بغیر Co-op Translator LLM پرووائیڈر کریڈینشلز کے۔ |
| `translate_repository_prompt` | MCP کلائنٹ کو dry-run پہلے repository ترجمے کے عمل کے ذریعے رہنمائی کریں۔ |

## Copy-Paste Examples

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
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

ہوسٹ ایجنٹ ماڈل کے ساتھ Markdown کا ترجمہ کریں:

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

جب ہوسٹ ایجنٹ نے ہر واپس کیے گئے چنک کا ترجمہ کر لیا ہو، تو `start_markdown_agent_translation` سے واپس ہونے والے مکمل `job` آبجیکٹ کے ساتھ کام ختم کریں:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

ریپوزیٹری ترجمہ کا پریویو کریں:

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

## Troubleshooting

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | абсолют Python executable path استعمال کریں اور `["-m", "co_op_translator.mcp.server"]` سورس چیک آؤٹ کنفیگریشن۔ |
| The server is listed but translation fails. | `get_configuration_status` کال کریں اور تصدیق کریں کہ کوئی LLM پرووائیڈر دستیاب ہے۔ |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | `start_markdown_agent_translation` / `finish_markdown_agent_translation` یا نوٹ بک کے مساوی استعمال کریں تاکہ ہوسٹ ایجنٹ چنکس کا ترجمہ کرے۔ |
| Image translation fails. | تصدیق کریں کہ Azure AI Vision ویریبلز سیٹ ہیں اور `get_configuration_status` کال کریں۔ |
| Repository translation does not write files. | صرف واضح صارف کی منظوری کے بعد `dry_run=false` اور `confirm_write=true` سیٹ کریں۔ |
| Changes to client config do not appear. | MCP کلائنٹ کو دوبارہ شروع یا ری لوڈ کریں۔ |

## Safety Notes

- MCP ٹول کالز میزبان ایپلیکیشن کے ذریعے ماڈل کنٹرولڈ ہوتی ہیں، اس لیے repository ترجمہ بذاتِ خود dry-run پر ڈیفالٹ ہے۔
- پورا repository ترجمہ کئی فائلیں بنا، اپڈیٹ، یا حذف کر سکتا ہے۔ `confirm_write=true` سیٹ کرنے سے پہلے واضح صارف کی منظوری ضروری کریں۔
- کنفیگریشن اسٹیٹس ٹول کبھی بھی API کیز، endpoints، یا دیگر خفیہ اقدار واپس نہیں کرتا۔
- تصویر کا ترجمہ base64 امیج ڈیٹا واپس کرتا ہے۔ بڑی تصاویر بڑے ٹول جواب پیدا کر سکتی ہیں۔
- ایجنٹ-مدد یافتہ ٹولز سورس چنکس اور پرومپٹس MCP ہوسٹ کو واپس کرتے ہیں۔ انہیں صرف اسی مواد کے ساتھ استعمال کریں جسے صارف اس ہوسٹ ایجنٹ ماڈل کو بھیجنے میں آرام محسوس کرے۔