# سرور MCP

Co-op Translator شامل یک سرور Model Context Protocol برای ایجنت‌ها، ویرایشگرها و مشتریان سازگار با MCP است.

برای پیکربندی محلی پیش‌فرض، کاربران نیازی ندارند دستی یک سرور جداگانه را اجرا کنند. آن‌ها مشتری MCP خود را پیکربندی می‌کنند و مشتری به‌طور خودکار هنگام نیاز به ابزارهای Co-op Translator، `co-op-translator-mcp` را از طریق `stdio` راه‌اندازی می‌کند.

اگر بین CLI، Python API و MCP مردد هستید، با [Choose Your Workflow](workflows.md) شروع کنید.

از MCP استفاده کنید وقتی یک ایجنت یا ویرایشگر باید مستقیماً Co-op Translator را فراخوانی کند:

| هدف کاربر | ابزارهای MCP |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

سرور MCP همان API عمومی پایتون را که در [Python API](api.md) مستندسازی شده است، پوشش می‌دهد. ابزارهای مبتنی بر ارائه‌دهنده از همان ارائه‌دهنده‌های پیکربندی‌شده مانند CLI و Python API استفاده می‌کنند. ابزارهای همراه ایجنت قطعه‌ها را برای ایجنت میزبان MCP آماده می‌کنند تا ترجمه شوند، سپس Co-op Translator بازسازی نهایی Markdown یا notebook را انجام می‌دهد.

## مرحله 1: نصب و پیکربندی Co-op Translator

Co-op Translator را در محیط پایتونی که مشتری MCP شما استفاده خواهد کرد نصب کنید:

```bash
pip install co-op-translator
```

برای توسعه محلی از این مخزن، بسته را در حالت ویرایشی نصب کنید:

```bash
pip install -e .
```

حالت ترجمه‌ای را که مشتری MCP شما استفاده خواهد کرد، انتخاب کنید:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation require Azure OpenAI or OpenAI. Image translation also requires Azure AI Vision. |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | No Co-op Translator LLM provider credentials are required for Markdown or notebook chunks. Image translation is not covered by agent-assisted mode yet. |

اگر با ترجمه Markdown یا notebook در داخل یک ایجنت مانند Codex یا Claude Code شروع می‌کنید، با حالت agent-assisted شروع کنید. از حالت provider-backed استفاده کنید وقتی می‌خواهید خود Co-op Translator ارائه‌دهنده‌های پیکربندی‌شده‌ی شما را فراخوانی کند، وقتی تصاویر را ترجمه می‌کنید، یا وقتی ترجمه در سطح مخزن مانند CLI را اجرا می‌کنید.

فقط برای جریان‌های کاری مبتنی بر ارائه‌دهنده، اعتبارنامه‌های ارائه‌دهنده را پیکربندی کنید:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ترجمه تصاویر مبتنی بر ارائه‌دهنده علاوه بر این نیاز دارد:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## مرحله 2: پیکربندی مشتری MCP خود

برای پیکربندی معمول محلی `stdio`، Co-op Translator را به پیکربندی مشتری MCP خود اضافه کنید. مشتری فرآیند را به‌طور خودکار راه‌اندازی و متوقف می‌کند.

پیکربندی بسته نصب‌شده:

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

پیکربندی بررسی منبع روی ویندوز:

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

پیکربندی بررسی منبع روی macOS یا Linux:

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

پس از تغییر پیکربندی مشتری MCP، مشتری را مجدداً راه‌اندازی یا بارگذاری مجدد کنید تا بتواند سرور جدید را کشف کند.

## مرحله 3: تأیید سرور در مشتری

از مشتری MCP بخواهید ابزارهای موجود را فهرست کند، یا ابتدا یکی از کمک‌کننده‌های فقط خواندنی را فراخوانی کنید:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

چک‌های مفید اولیه:

| ابزار | چه چیزی را بررسی کنید |
| --- | --- |
| `get_api_overview` | تأیید می‌کند که سرور در دسترس است و جریان‌های کاری موجود را نمایش می‌دهد. |
| `list_supported_languages` | تأیید می‌کند که داده‌های زبانی بسته‌شده قابل بارگذاری هستند. |
| `get_configuration_status` | تأیید می‌کند که ارائه‌دهنده‌های LLM و Vision بدون افشای مقادیر محرمانه در دسترس‌اند. |

## مرحله 4: انتخاب یک جریان کاری

### ترجمه فایل‌ها یا اسناد جداگانه

از ابزارهای محتوایی مبتنی بر ارائه‌دهنده استفاده کنید وقتی مشتری MCP در حال حاضر محتوای سند یا مسیر تصویر را دارد و Co-op Translator باید ارائه‌دهنده‌های پیکربندی‌شده را فراخوانی کند.

برای Markdown:

1. `translate_markdown_content` را با `document`، `language_code` و در صورت تمایل `source_path` فراخوانی کنید.
2. اگر نتیجه ترجمه قرار است در یک چینش خروجی Co-op Translator نوشته شود، `rewrite_markdown_paths` را فراخوانی کنید.
3. اجازه دهید مشتری محتوای نهایی را بنویسد یا بازگرداند.

برای notebookها:

1. `translate_notebook_content` را با JSON نوت‌بوک و `language_code` فراخوانی کنید.
2. اگر لازم است لینک‌های نوت‌بوک ترجمه‌شده برای مسیر هدف تنظیم شوند، `rewrite_notebook_paths` را فراخوانی کنید.
3. JSON نوت‌بوک نهایی را بنویسید یا بازگردانید.

برای تصاویر:

1. `translate_image_content` را با `image_path`، `language_code` و در صورت تمایل `root_dir` یا `fast_mode` فراخوانی کنید.
2. `data_base64` و `mime_type` بازگردانده‌شده را بخوانید.
3. اگر `output_path` ارائه شده باشد، تصویر ترجمه‌شده نیز در آن مسیر ذخیره می‌شود.

ابزارهای محتوایی اکتشاف پروژه، به‌روزرسانی متادیتا، اعلامیه‌ها یا بازنویسی مسیر خودکار را انجام نمی‌دهند. اگر می‌خواهید ایجنت میزبان Markdown یا قطعه‌های نوت‌بوک را بدون اعتبارنامه‌های ارائه‌دهنده LLM Co-op Translator ترجمه کند، از جریان کاری agent-assisted زیر استفاده کنید.

### ترجمه با مدل ایجنت میزبان

از ابزارهای agent-assisted استفاده کنید وقتی می‌خواهید ایجنت میزبان MCP، مانند یک دستیار کدنویسی، متن ترجمه‌شده را تولید کند به‌جای اینکه برای Co-op Translator، Azure OpenAI یا OpenAI را پیکربندی کنید.

در یک مشتری مبتنی بر چت MCP، معمولاً نیازی به نوشتن دستی JSON ابزار ندارید. از ایجنت بخواهید از جریان کاری agent-assisted استفاده کند:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

برای نوت‌بوک‌ها، از الگوی مشابه استفاده کنید:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

اگر مشتری MCP شما از server prompts پشتیبانی می‌کند، از `agent_assisted_markdown_translation_prompt` استفاده کنید تا مشتری همان دستورالعمل‌های جریان کاری را بارگذاری کند.

برای Markdown:

1. `start_markdown_agent_translation` را با `document`، `language_code` و در صورت تمایل `source_path` فراخوانی کنید.
2. هر قطعه برگردانده‌شده را در ایجنت میزبان با پیروی از `prompt` قطعه ترجمه کنید.
3. `finish_markdown_agent_translation` را با `job` اصلی و قطعه‌های ترجمه‌شده با استفاده از `chunk_id` و `translated_text` فراخوانی کنید.
4. اگر محتوا قرار است در یک مسیر هدف ترجمه‌شده نوشته شود، `rewrite_markdown_paths` را فراخوانی کنید.

برای نوت‌بوک‌ها:

1. `start_notebook_agent_translation` را با JSON نوت‌بوک و `language_code` فراخوانی کنید.
2. هر قطعه برگردانده‌شده را در ایجنت میزبان ترجمه کنید.
3. `finish_notebook_agent_translation` را با `job` اصلی و قطعه‌های ترجمه‌شده فراخوانی کنید.
4. اگر لینک‌های نوت‌بوک ترجمه‌شده نیاز به تنظیم مسیر هدف دارند، `rewrite_notebook_paths` را فراخوانی کنید.

ابزارهای agent-assisted از Azure OpenAI یا OpenAI از طرف Co-op Translator فراخوانی نمی‌کنند. ایجنت میزبان مسئول ترجمه قطعات بازگردانده‌شده است. Co-op Translator تقسیم‌بندی Markdown، حفظ نگهدارنده‌ها، بازسازی frontmatter، جایگزینی سلول‌های نوت‌بوک و نرمال‌سازی پس از ترجمه را انجام می‌دهد.

### ترجمه یک مخزن کامل

از `run_translation` استفاده کنید وقتی کاربر می‌خواهد Co-op Translator مانند CLI رفتار کند.

ترجمه مخزن به‌صورت پیش‌فرض با `dry_run=true` اجرا می‌شود تا ایجنت بتواند دامنه را قبل از تغییر فایل‌ها بررسی کند:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

برای اجازه نوشتن، فراخوان باید هر دو `dry_run=false` و `confirm_write=true` را تنظیم کند:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` به‌عنوان یک نام سازگاری برای `run_translation` ارائه شده است.

### بازبینی خروجی ترجمه‌شده

از `run_review` برای بررسی‌های قطعی که نیازمند اعتبارنامه‌های LLM یا Vision نیستند استفاده کنید:

!!! note "Beta"
    MCP exposes the beta `run_review` API. It is safe for read-only review workflows, but review checks and issue schemas may evolve.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

نتیجه شامل خروجی متنی ضبط‌شده و در صورت موجود بودن یک خلاصه‌ی ساختاریافته از بازبینی است.

## اجرای دستی سرور

اجرای دستی عمدتاً برای اشکال‌زدایی یا برای انتقال‌هایی است که مانند سرورهای بلندمدت رفتار می‌کنند.

سرور stdio پیش‌فرض را برای اشکال‌زدایی اجرا کنید:

```bash
co-op-translator-mcp
```

از یک بررسی منبع اجرا کنید:

```bash
python -m co_op_translator.mcp.server
```

یک سرور HTTP یا SSE بلندمدت اجرا کنید:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

برای یکپارچه‌سازی‌های محلی ویرایشگر و ایجنت، ترجیحاً از پیکربندی `stdio` تحت مدیریت مشتری در مرحله 2 استفاده کنید.

## ابزارها

| ابزار | هدف | آیا فایل‌ها را می‌نویسد |
| --- | --- | --- |
| `translate_markdown_content` | ترجمه یک رشته Markdown. | No |
| `translate_notebook_content` | ترجمه سلول‌های Markdown در JSON نوت‌بوک. | No |
| `translate_image_content` | ترجمه متن در یک تصویر و بازگرداندن داده تصویر base64. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | آماده‌سازی قطعه‌های Markdown برای ترجمه توسط ایجنت میزبان بدون اعتبارنامه‌های LLM Co-op Translator. | No |
| `finish_markdown_agent_translation` | بازسازی Markdown از قطعه‌های ترجمه‌شده ایجنت میزبان. | No |
| `start_notebook_agent_translation` | آماده‌سازی قطعه‌های سلول‌های Markdown نوت‌بوک برای ترجمه توسط ایجنت میزبان. | No |
| `finish_notebook_agent_translation` | بازسازی JSON نوت‌بوک از قطعه‌های ترجمه‌شده ایجنت میزبان. | No |
| `rewrite_markdown_paths` | بازنویسی بدنه و مسیرهای frontmatter برای یک هدف ترجمه‌شده. | No |
| `rewrite_notebook_paths` | بازنویسی مسیرها در داخل سلول‌های Markdown نوت‌بوک. | No |
| `run_translation` | اجرای ترجمه در سطح پروژه مانند CLI. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | نام سازگاری برای `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | اجرای چک‌های قطعی بازبینی. | No |
| `get_configuration_status` | گزارش ارائه‌دهنده‌های LLM و Vision پیکربندی‌شده بدون افشای مقادیر محرمانه. | No |
| `list_supported_languages` | فهرست کُدهای زبان‌های هدف پشتیبانی‌شده را ارائه می‌دهد. | No |
| `get_api_overview` | توصیف جریان‌های کاری و ابزارهای MCP موجود. | No |

## منابع

| Resource URI | هدف |
| --- | --- |
| `co-op://api` | JSON نمای کلی از جریان‌های کاری و ابزارها. |
| `co-op://supported-languages` | فهرست JSON از کدهای زبان‌های پشتیبانی‌شده. |
| `co-op://configuration` | خلاصه‌ی JSON از در دسترس بودن ارائه‌دهنده‌ها بدون افشای اسرار. |

## پرامپت‌ها

| Prompt | هدف |
| --- | --- |
| `translate_markdown_document_prompt` | راهنمایی یک مشتری MCP از طریق ترجمه محتوا به‌علاوه بازنویسی مسیر اختیاری. |
| `agent_assisted_markdown_translation_prompt` | راهنمایی یک مشتری MCP برای ترجمه Markdown توسط ایجنت میزبان بدون اعتبارنامه‌های LLM Co-op Translator. |
| `translate_repository_prompt` | راهنمایی یک مشتری MCP برای ترجمه مخزن که ابتدا dry-run را انجام می‌دهد. |

## مثال‌های کپی-پیست

Translate Markdown content:

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

Rewrite translated Markdown links:

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

Translate Markdown with the host agent model:

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

After the host agent translates each returned chunk, finish the job with the complete `job` object returned by `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Preview repository translation:

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
| The MCP client cannot find `co-op-translator-mcp`. | از مسیر اجرایی پایتون مطلق و پیکربندی بررسی منبع `["-m", "co_op_translator.mcp.server"]` استفاده کنید. |
| The server is listed but translation fails. | `get_configuration_status` را فراخوانی کنید و تأیید کنید که یک ارائه‌دهنده LLM در دسترس است. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | از `start_markdown_agent_translation` / `finish_markdown_agent_translation` یا معادل‌های نوت‌بوک استفاده کنید تا ایجنت میزبان قطعات را ترجمه کند. |
| Image translation fails. | تأیید کنید متغیرهای Azure AI Vision تنظیم شده‌اند و `get_configuration_status` را فراخوانی کنید. |
| Repository translation does not write files. | تنها پس از تأیید صریح کاربر `dry_run=false` و `confirm_write=true` را تنظیم کنید. |
| Changes to client config do not appear. | مشتری MCP را مجدداً راه‌اندازی یا بارگذاری مجدد کنید. |

## نکات ایمنی

- فراخوانی‌های ابزار MCP توسط برنامه میزبان کنترل می‌شوند، بنابراین ترجمه مخزن به‌صورت پیش‌فرض dry-run است.
- ترجمه کامل مخزن می‌تواند فایل‌های زیادی را ایجاد، به‌روزرسانی یا حذف کند. قبل از تنظیم `confirm_write=true` تأیید صریح کاربر را دریابید.
- ابزار وضعیت پیکربندی هرگز کلیدهای API، نقاط انتهایی یا سایر مقادیر محرمانه را بازنمی‌گرداند.
- ترجمه تصویر داده تصویر base64 بازمی‌گرداند. تصاویر بزرگ می‌توانند پاسخ‌های ابزار بزرگی تولید کنند.
- ابزارهای agent-assisted قطعه‌های منبع و پرامپت‌ها را به میزبان MCP بازمی‌گردانند. آن‌ها را فقط با محتوایی استفاده کنید که کاربر راضی است به آن ایجنت میزبان ارسال شود.