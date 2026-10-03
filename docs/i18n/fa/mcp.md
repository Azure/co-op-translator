# سرور MCP

Co-op Translator شامل یک سرور Model Context Protocol برای عوامل، ویرایشگرها و کلاینت‌های سازگار با MCP است.

برای پیکربندی محلی پیش‌فرض، کاربران نیازی به اجرای سرور جداگانه به‌صورت دستی ندارند. آن‌ها کلاینت MCP خود را پیکربندی می‌کنند و کلاینت هنگام نیاز به ابزارهای Co-op Translator به‌طور خودکار `co-op-translator-mcp` را از طریق `stdio` راه‌اندازی می‌کند.

اگر بین CLI، API پایتون و MCP در تردید هستید، با [روند کاری خود را انتخاب کنید](workflows.md) شروع کنید.

از MCP زمانی استفاده کنید که یک عامل یا ویرایشگر باید مستقیماً با Co-op Translator تماس بگیرد:

| هدف کاربر | ابزارهای MCP |
| --- | --- |
| ترجمه یک سند Markdown، نوت‌بوک یا تصویر | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| ترجمه محتوای Markdown یا نوت‌بوک با مدل عامل میزبان | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| بازنویسی لینک‌های ترجمه‌شده Markdown یا نوت‌بوک پس از انتخاب مسیر خروجی | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| ترجمه یک مخزن کامل مانند CLI | `run_translation`, `translate_project` |
| بازبینی خروجی ترجمه‌شده بدون اعتبارنامهٔ LLM | `run_review` |
| بازبینی قابلیت‌ها و وضعیت محیط | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

سرور MCP همان API عمومی پایتون را که در [API پایتون](api.md) مستند شده است بسته‌بندی می‌کند. ابزارهای مبتنی بر ارائه‌دهنده از همان ارائه‌دهنده‌های پیکربندی‌شده مانند CLI و API پایتون استفاده می‌کنند. ابزارهای کمک‌شده توسط عامل بخش‌ها را برای ترجمه توسط عامل میزبان MCP آماده می‌کنند و سپس از Co-op Translator برای بازسازی نهایی Markdown یا نوت‌بوک استفاده می‌کنند.

## گام ۱: نصب و پیکربندی Co-op Translator

Co-op Translator را در محیط پایتونی که کلاینت MCP شما استفاده خواهد کرد نصب کنید:

```bash
pip install co-op-translator
```

برای توسعه محلی از این مخزن، بسته را در حالت editable نصب کنید:

```bash
pip install -e .
```

حالت ترجمه‌ای را که کلاینت MCP شما استفاده خواهد کرد انتخاب کنید:

| حالت | استفاده برای | اعتبارنامه‌ها |
| --- | --- | --- |
| پشتیبانی‌شده توسط ارائه‌دهنده | Co-op Translator فراخوانی‌های `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` یا `run_translation` را انجام می‌دهد. | ترجمه نیاز به Azure OpenAI، OpenAI یا Anthropic دارد. ترجمهٔ تصویر همچنین به Azure AI Vision نیاز دارد. |
| با کمک عامل | عامل میزبان MCP بخش‌های بازگردانده‌شده توسط `start_markdown_agent_translation` یا `start_notebook_agent_translation` را ترجمه می‌کند. | برای بخش‌های Markdown یا نوت‌بوک نیازی به مدارک ارائه‌دهندهٔ LLM برای Co-op Translator نیست. ترجمهٔ تصویر هنوز تحت حالت با کمک عامل پوشش داده نمی‌شود. |

اگر کار خود را با ترجمهٔ Markdown یا نوت‌بوک درون یک عامل مانند Codex یا Claude Code شروع می‌کنید، با حالت با کمک عامل شروع کنید. زمانی از حالت مبتنی بر ارائه‌دهنده استفاده کنید که می‌خواهید خود Co-op Translator از ارائه‌دهنده‌های پیکربندی‌شدهٔ شما فراخوانی کند، هنگام ترجمهٔ تصاویر، یا هنگام اجرای ترجمه در سطح مخزن مانند CLI.

برای گردش‌کار‌های مبتنی بر ارائه‌دهنده، یک ارائه‌دهنده را پیکربندی کنید:

```bash
# آژور اوپن‌ای‌آی
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# یا اوپن‌ای‌آی
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# یا آنتروپیک
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

ترجمهٔ تصویر مبتنی بر ارائه‌دهنده به‌طور اضافی نیاز دارد:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    حالت با کمک عامل در حال حاضر سلول‌های Markdown در Markdown و نوت‌بوک را پوشش می‌دهد. ترجمهٔ تصویر همچنان از خط لولهٔ تصویر مبتنی بر ارائه‌دهنده استفاده می‌کند و برای OCR و رندر آگاه از چیدمان به Azure AI Vision نیاز دارد.

## گام ۲: پیکربندی کلاینت MCP شما

برای پیکربندی محلی معمولی `stdio`، Co-op Translator را به پیکربندی کلاینت MCP خود اضافه کنید. کلاینت فرایند را به‌صورت خودکار شروع و متوقف خواهد کرد.

پیکربندی بستهٔ نصب‌شده:

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

پیکربندی منبع چک‌اوت در ویندوز:

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

پیکربندی منبع چک‌اوت در macOS یا Linux:

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

پس از تغییر پیکربندی کلاینت MCP، کلاینت را راه‌اندازی مجدد یا بارگذاری مجدد کنید تا بتواند سرور جدید را کشف کند.

## گام ۳: تایید سرور در کلاینت

از کلاینت MCP بخواهید ابزارهای در دسترس را لیست کند، یا ابتدا یکی از کمکی‌های فقط خواندنی را فراخوانی کنید:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

بررسی‌های اولیۀ مفید:

| ابزار | چه چیزی را بررسی کنید |
| --- | --- |
| `get_api_overview` | تأیید می‌کند که سرور در دسترس است و جریان‌های کاری موجود را نشان می‌دهد. |
| `list_supported_languages` | تأیید می‌کند که داده‌های زبانی بسته‌بندی‌شده قابل بارگذاری هستند. |
| `get_configuration_status` | تأیید می‌کند که ارائه‌دهندگان LLM و Vision در دسترس‌اند بدون افشای مقادیر محرمانه. |

## گام ۴: انتخاب یک روند کاری

### ترجمه فایل‌ها یا اسناد جداگانه

زمانی از ابزارهای محتوایی مبتنی بر ارائه‌دهنده استفاده کنید که کلاینت MCP از قبل محتوای سند یا مسیر تصویر را داشته باشد و Co-op Translator باید ارائه‌دهنده‌های پیکربندی‌شده را فراخوانی کند.

برای Markdown:

1. فراخوانی `translate_markdown_content` با `document`، `language_code` و در صورت لزوم `source_path`.
2. اگر نتیجهٔ ترجمه‌شده قرار است در یک چیدمان خروجی Co-op Translator نوشته شود، `rewrite_markdown_paths` را فراخوانی کنید.
3. اجازه دهید کلاینت `content` نهایی را بنویسد یا بازگرداند.

برای نوت‌بوک‌ها:

1. فراخوانی `translate_notebook_content` با JSON نوت‌بوک و `language_code`.
2. اگر نیاز به تنظیم لینک‌های نوت‌بوک ترجمه‌شده برای مسیر هدف است، `rewrite_notebook_paths` را فراخوانی کنید.
3. JSON نوت‌بوک نهایی را بنویسید یا بازگردانید.

برای تصاویر:

1. فراخوانی `translate_image_content` با `image_path`، `language_code` و به‌صورت اختیاری `root_dir` یا `fast_mode`.
2. `data_base64` و `mime_type` بازگردانده‌شده را بخوانید.
3. اگر `output_path` ارائه شده باشد، تصویر ترجمه‌شده نیز در آن مسیر ذخیره می‌شود.

ابزارهای محتوایی عملیات کشف پروژه، به‌روزرسانی متادیتا، اعلامیه‌ها یا بازنویسی خودکار مسیرها را انجام نمی‌دهند. اگر می‌خواهید عامل میزبان بخش‌های Markdown یا نوت‌بوک را بدون اعتبارنامه‌های ارائه‌دهندهٔ LLM برای Co-op Translator ترجمه کند، از گردش‌کار با کمک عامل زیر استفاده کنید.

### ترجمه با مدل عامل میزبان

از ابزارهای با کمک عامل استفاده کنید وقتی می‌خواهید عامل میزبان MCP، مانند یک دستیار کدنویسی، متن ترجمه‌شده را تولید کند به‌جای اینکه برای Co-op Translator یک ارائه‌دهندهٔ LLM پیکربندی کنید.

در یک کلاینت MCP مبتنی بر چت، معمولاً نیازی نیست خودتان JSON ابزار را بنویسید. از عامل بخواهید از گردش‌کار با کمک عامل استفاده کند:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

برای نوت‌بوک‌ها، از همان الگو استفاده کنید:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

اگر کلاینت MCP شما از server prompts پشتیبانی می‌کند، از `agent_assisted_markdown_translation_prompt` استفاده کنید تا کلاینت همان دستورالعمل‌های گردش‌کار را بارگذاری کند.

برای Markdown:

1. فراخوانی `start_markdown_agent_translation` با `document`، `language_code` و در صورت لزوم `source_path`.
2. هر بخش بازگردانده‌شده را در عامل میزبان با دنبال کردن `prompt` بخش ترجمه کنید.
3. با استفاده از `chunk_id` و `translated_text`، `finish_markdown_agent_translation` را با `job` اصلی و بخش‌های ترجمه‌شده فراخوانی کنید.
4. اگر محتوا قرار است در مسیر هدف ترجمه‌شده نوشته شود، `rewrite_markdown_paths` را فراخوانی کنید.

برای نوت‌بوک‌ها:

1. فراخوانی `start_notebook_agent_translation` با JSON نوت‌بوک و `language_code`.
2. هر بخش بازگردانده‌شده را در عامل میزبان ترجمه کنید.
3. `finish_notebook_agent_translation` را با `job` اصلی و بخش‌های ترجمه‌شده فراخوانی کنید.
4. اگر لینک‌های نوت‌بوک ترجمه‌شده نیاز به تنظیم مسیر هدف دارند، `rewrite_notebook_paths` را فراخوانی کنید.

ابزارهای با کمک عامل ارائه‌دهندهٔ LLM پیکربندی‌شده را از Co-op Translator فراخوانی نمی‌کنند. عامل میزبان مسئول ترجمهٔ بخش‌های بازگردانده‌شده است. Co-op Translator تقسیم‌بندی Markdown، حفظ نگهدارنده‌ها، بازسازی frontmatter، جایگزینی سلول‌های نوت‌بوک و نرمال‌سازی پس‌از‌ترجمه را مدیریت می‌کند.

### ترجمه یک مخزن کامل

زمانی از `run_translation` استفاده کنید که کاربر می‌خواهد Co-op Translator مانند CLI رفتار کند.

ترجمهٔ مخزن به‌طور پیش‌فرض `dry_run=true` است تا یک عامل بتواند محدوده را قبل از تغییر فایل‌ها بررسی کند:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

نتیجهٔ `run_translation` شامل یک آرایهٔ `events` با رویدادهای پیشرفت نسخه‌بندی‌شدهٔ
`co-op.translation.event.v1` است. کلاینت‌های MCP باید به‌جای تجزیهٔ متن ثبت‌شدۀ کنسول از فیلدهایی مانند
`type`, `stage_key`, `completed`, `total`, و `current_path` استفاده کنند.
متن ثبت‌شده را تجزیه نکنید. با ارسال `json_events_path` می‌توانید آن رویدادها را نیز
به یک فایل NDJSON بنویسید.

برای اجازهٔ نوشتن، فراخوان باید هر دو مقدار `dry_run=false` و `confirm_write=true` را تنظیم کند:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` به‌عنوان یک نام مستعار سازگاری برای `run_translation` در دسترس است.

### بازبینی خروجی ترجمه‌شده

از `run_review` برای بررسی‌های قطعی که نیاز به مدارک LLM یا Vision ندارند استفاده کنید:

!!! note "Beta"
    MCP API بتای `run_review` را افشا می‌کند. برای گردش‌کارهای بازبینی فقط خواندنی امن است، اما بررسی‌ها و اسکیمای مسائل ممکن است تکامل یابد.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

نتیجه شامل خروجی متن ثبت‌شده و یک خلاصهٔ ساختاریافتهٔ بازبینی در صورت موجود بودن است.

## اجرای دستی سرور

اجرای دستی عمدتاً برای رفع اشکال یا برای انتقال‌هایی است که مانند سرورهای بلندمدت رفتار می‌کنند.

دیباگ سرور stdio پیش‌فرض:

```bash
co-op-translator-mcp
```

اجرای از یک منبع چک‌اوت:

```bash
python -m co_op_translator.mcp.server
```

اجرای یک سرور HTTP یا SSE با طول عمر طولانی:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

برای یکپارچه‌سازی‌های ویرایشگر و عامل محلی، پیکربندی `stdio` که توسط کلاینت مدیریت می‌شود در گام ۲ را ترجیح دهید.

## ابزارها

| ابزار | هدف | فایل‌ها را می‌نویسد |
| --- | --- | --- |
| `translate_markdown_content` | یک رشتهٔ Markdown را ترجمه می‌کند. | خیر |
| `translate_notebook_content` | سلول‌های Markdown در JSON نوت‌بوک را ترجمه می‌کند. | خیر |
| `translate_image_content` | متن در یک تصویر را ترجمه کرده و دادهٔ تصویر base64 را بازمی‌گرداند. | اختیاری، فقط وقتی که `output_path` ارائه شده باشد |
| `start_markdown_agent_translation` | بخش‌های Markdown را برای ترجمه توسط عامل میزبان بدون اعتبارنامهٔ LLM Co-op Translator آماده می‌کند. | خیر |
| `finish_markdown_agent_translation` | Markdown را از بخش‌های ترجمه‌شده توسط عامل میزبان بازسازی می‌کند. | خیر |
| `start_notebook_agent_translation` | بخش‌های سلول Markdown نوت‌بوک را برای ترجمه توسط عامل میزبان آماده می‌کند. | خیر |
| `finish_notebook_agent_translation` | JSON نوت‌بوک را از بخش‌های ترجمه‌شده توسط عامل میزبان بازسازی می‌کند. | خیر |
| `rewrite_markdown_paths` | مسیرهای بدنهٔ Markdown و frontmatter را برای یک هدف ترجمه‌شده بازنویسی می‌کند. | خیر |
| `rewrite_notebook_paths` | مسیرها داخل سلول‌های Markdown نوت‌بوک را بازنویسی می‌کند. | خیر |
| `run_translation` | اجرای ترجمهٔ سطح پروژه مانند CLI. | بله وقتی `dry_run=false` و `confirm_write=true` |
| `translate_project` | نام مستعار سازگاری برای `run_translation`. | بله وقتی `dry_run=false` و `confirm_write=true` |
| `run_review` | اجرای بررسی‌های قطعی بازبینی. | خیر |
| `get_configuration_status` | گزارش فراهمی ارائه‌دهندگان LLM و Vision بدون افشای مقادیر محرمانه. | خیر |
| `list_supported_languages` | لیست کدهای زبان‌های هدف پشتیبانی‌شده. | خیر |
| `get_api_overview` | توصیف جریان‌های کاری و ابزارهای MCP موجود. | خیر |

## منابع

| شناسهٔ منبع | هدف |
| --- | --- |
| `co-op://api` | نمای کلی JSON از جریان‌های کاری و ابزارها. |
| `co-op://supported-languages` | لیست JSON از کدهای زبان‌های پشتیبانی‌شده. |
| `co-op://configuration` | خلاصهٔ JSON از فراهمی ارائه‌دهندگان بدون مقادیر محرمانه. |

## پرومپت‌ها

| پرومپت | هدف |
| --- | --- |
| `translate_markdown_document_prompt` | راهنمایی یک کلاینت MCP در فرایند ترجمهٔ محتوا همراه با بازنویسی اختیاری مسیر. |
| `agent_assisted_markdown_translation_prompt` | راهنمایی یک کلاینت MCP در ترجمهٔ Markdown توسط عامل میزبان بدون اعتبارنامهٔ ارائه‌دهندهٔ LLM برای Co-op Translator. |
| `translate_repository_prompt` | راهنمایی یک کلاینت MCP در ترجمهٔ مخزن با رویکرد dry-run ابتدا. |

## مثال‌های کپی-پیست

ترجمهٔ محتوای Markdown:

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

بازنویسی لینک‌های ترجمه‌شدهٔ Markdown:

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

ترجمهٔ Markdown با مدل عامل میزبان:

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

پس از اینکه عامل میزبان هر بخش بازگردانده‌شده را ترجمه کرد، کار را با شیٔ کامل `job` که توسط `start_markdown_agent_translation` بازگردانده شده است، انجام دهید:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

پیش‌نمایش ترجمهٔ مخزن:

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

## عیب‌یابی

| مشکل | چه کاری را امتحان کنید |
| --- | --- |
| کلاینت MCP نمی‌تواند `co-op-translator-mcp` را پیدا کند. | از مسیر اجرایی پایتون مطلق و پیکربندی منبع چک‌اوت `["-m", "co_op_translator.mcp.server"]` استفاده کنید. |
| سرور فهرست شده اما ترجمه انجام نمی‌شود. | `get_configuration_status` را فراخوانی کرده و تأیید کنید که یک ارائه‌دهندهٔ LLM در دسترس است. |
| می‌خواهید ترجمهٔ Markdown یا نوت‌بوک بدون مدارک ارائه‌دهنده داشته باشید. | از `start_markdown_agent_translation` / `finish_markdown_agent_translation` یا معادل‌های نوت‌بوک استفاده کنید تا عامل میزبان بخش‌ها را ترجمه کند. |
| ترجمهٔ تصویر با خطا روبه‌رو می‌شود. | تأیید کنید متغیرهای Azure AI Vision تنظیم شده‌اند و `get_configuration_status` را فراخوانی کنید. |
| ترجمهٔ مخزن فایل‌ها را نمی‌نویسد. | فقط پس از تایید صریح کاربر `dry_run=false` و `confirm_write=true` را تنظیم کنید. |
| تغییرات در پیکربندی کلاینت ظاهر نمی‌شوند. | کلاینت MCP را راه‌اندازی مجدد یا بارگذاری مجدد کنید. |

## نکات ایمنی

- فراخوانی‌های ابزار MCP تحت کنترل مدل توسط برنامهٔ میزبان هستند، بنابراین ترجمهٔ مخزن به‌صورت پیش‌فرض dry-run است.
- ترجمهٔ کامل مخزن می‌تواند فایل‌های زیادی ایجاد، به‌روزرسانی یا حذف کند. قبل از تنظیم `confirm_write=true` تایید صریح کاربر را الزامی کنید.
- ابزار وضعیت پیکربندی هرگز کلیدهای API، نقاط انتهایی یا سایر مقادیر محرمانه را بازنمی‌گرداند.
- ترجمهٔ تصویر دادهٔ تصویر base64 را بازمی‌گرداند. تصاویر بزرگ می‌توانند پاسخ‌های ابزار بزرگی ایجاد کنند.
- ابزارهای با کمک عامل بخش‌های منبع و پرومپت‌ها را به میزبان MCP بازمی‌گردانند. از آن‌ها تنها با محتوایی استفاده کنید که کاربر با ارسال آن به مدل عامل میزبان راحت است.