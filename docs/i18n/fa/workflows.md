# انتخاب جریان کاری شما

Co-op Translator می‌تواند به سه روش استفاده شود: CLI، Python API، و سرور MCP. آن‌ها قابلیت‌های ترجمه یکسانی دارند، اما هرکدام مناسب جریان کاری متفاوتی هستند.

از این صفحه هنگام تصمیم‌گیری برای شروع استفاده کنید.

**اگر ترجمه‌ها را دستی ویرایش می‌کنید:** روال‌های پیش‌فرض CLI و Actions فایل‌های منبع تغییر‌یافته را به‌طور کامل دوباره ترجمه می‌کنند، بنابراین عبارت‌های شما در آن فایل‌ها ممکن است بازنویسی شوند. قبل از پذیرش یک به‌روزرسانی، diff را بازبینی کنید. برای حفظ سطح‌بندی بلوک‌های Markdown از ویرایش‌های پذیرفته‌شده، از ارائه‌دهندهٔ حالت ترجمه Python API (api.md#preserve-accepted-human-edits-with-a-translation-state-provider) اختیاری استفاده کنید.

## تصمیم سریع

| اگر می‌خواهید... | استفاده | از اینجا شروع کنید |
| --- | --- | --- |
| ترجمه یا بررسی یک مخزن از طریق ترمینال | CLI | [مرجع CLI](cli.md) |
| ترجمه را به یک اسکریپت، سرویس، نوت‌بوک یا کار CI در Python اضافه کنید | Python API | [مستندات Python API](api.md) |
| اجازه دهید یک عامل، ویرایشگر یا مشتری سازگار با MCP محتوایی را برای شما ترجمه کند | MCP Server | [سرور MCP](mcp.md) |
| یک سند Markdown، نوت‌بوک یا تصویری را که برنامهٔ شما قبلاً بارگذاری کرده است ترجمه کنید | Python API یا MCP Server | [Python API](api.md) یا [سرور MCP](mcp.md) |
| یک مخزن کامل را با پوشه‌های خروجی استاندارد و متادیتا ترجمه کنید | CLI یا `run_translation` | [مرجع CLI](cli.md) یا [مستندات Python API](api.md) |

## از CLI استفاده کنید وقتی

CLI را وقتی انتخاب کنید که یک فرد یا کار CI ترجمه مخزن را از یک شل اجرا می‌کند.

CLI مستقیم‌ترین راه است وقتی می‌خواهید Co-op Translator فایل‌های پروژه را کشف کند، خروجی‌های ترجمه‌شده ایجاد کند، چیدمان پروژه را حفظ کند، فراداده را به‌روزرسانی کند، و دستورات بازبینی را اجرا کند.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

این مثال Markdown و نوت‌بوک‌ها را ترجمه می‌کند. تنها پس از پیکربندی [Azure AI Vision](configuration.md#azure-ai-vision) مقدار `-img` را اضافه کنید. برای یک اجرای اولیه که فقط شامل Markdown است، از [اولین ترجمه‌ی شما](first-translation.md) پیروی کنید.

موارد مناسب:

- شما در حال ترجمه یک مخزن از ترمینال خود هستید.
- شما یک دستور قابل تکرار برای جریان‌های کاری CI یا انتشار می‌خواهید.
- شما کشف پروژه، مسیرهای خروجی، فراداده، پاک‌سازی و بازبینی داخلی می‌خواهید.
- شما رابط دستوری را به نوشتن کد پایتون ترجیح می‌دهید.

## از Python API استفاده کنید وقتی

Python API را وقتی انتخاب کنید که کد شما باید جریان کاری را کنترل کند.

این API برای برنامه‌ها، اسکریپت‌های خودکارسازی، دفترچه‌ها، سرویس‌ها، و خطوط لولهٔ سفارشی مفید است. این امکان را می‌دهد که از APIهای ترجمه محتوای سطح پایین برای فایل‌های مجزا فراخوانی کنید، یا همان هماهنگ‌سازی در سطح مخزن که توسط CLI استفاده می‌شود را اجرا کنید.

یک سند Markdown را ترجمه کنید و تصمیم بگیرید کجا آن را ذخیره کنید:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


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
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

از پایتون یک ترجمهٔ مخزن اجرا کنید:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

موارد مناسب:

- برنامه شما قبلاً فایل‌ها، بافرها، دفترچه‌ها، یا بایت‌های تصویر را می‌خواند.
- شما به اعتبارسنجی سفارشی، ذخیره‌سازی، ثبت لاگ، تلاش مجدد، یا جریان‌های تأیید نیاز دارید.
- می‌خواهید یک سند، دفترچه، یا تصویر را بدون پردازش یک مخزن کامل ترجمه کنید.
- می‌خواهید ترجمه مخزن را انجام دهید، اما از طریق خودکارسازی پایتون به‌جای دستور شل.

## از سرور MCP استفاده کنید وقتی

سرور MCP را زمانی انتخاب کنید که یک عامل، ویرایشگر، یا کلاینت سازگار با MCP باید ابزارهای Co-op Translator را فراخوانی کند.

در تنظیم محلی معمول، کاربر به‌صورت دستی سرور را در حالت اجرا نگه نمی‌دارد. کلاینت MCP وقتی به ابزارها نیاز دارد، `co-op-translator-mcp` را از طریق `stdio` شروع می‌کند.

درخواست‌های نمونه‌ای که یک عامل می‌تواند رسیدگی کند:

- "این فایل Markdown را به کره‌ای ترجمه کنید و لینک‌ها را درست نگه دارید."
- "این فایل Markdown را به کره‌ای با جریان کاری MCP با کمک عامل ترجمه کنید، و برای بخش‌های ترجمه‌شده از مدل خودتان استفاده کنید."
- "این دفترچه را به کره‌ای ترجمه کنید، سلول‌های کد را حفظ کنید، و از Co-op Translator MCP برای بازسازی دفترچه استفاده کنید."
- "متن این تصویر را به ژاپنی ترجمه کنید و نتیجه را ذخیره کنید."
- "اجرای آزمایشی ترجمه یک مخزن به اسپانیایی و به من بگویید چه چیزهایی تغییر خواهند کرد."
- "بررسی کنید که آیا خروجی ترجمه کره‌ای به‌روز است یا خیر."

برای Markdown و دفترچه‌ها، MCP می‌تواند در دو حالت کار کند:

| حالت | زمان استفاده | ابزارهای اصلی |
| --- | --- | --- |
| با کمک عامل | عامل میزبان MCP باید بخش‌ها را با مدل خود ترجمه کند، بدون اعتبارنامه ارائه‌دهنده LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| پشتیبانی ارائه‌دهنده | Co-op Translator باید مستقیماً Azure OpenAI، OpenAI، یا Anthropic را فراخوانی کند. | `translate_markdown_content`, `translate_notebook_content` |

شکل فراخوانی ابزار Markdown در حالت پشتیبانی‌شده توسط ارائه‌دهنده MCP:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

شکل فراخوانی ابزار تصویر MCP:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

ترجمه مخزن به‌صورت پیش‌فرض از طریق MCP به‌صورت اجرای آزمایشی (dry-run) انجام می‌شود:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

موارد مناسب:

- شما می‌خواهید جریان‌های کاری ترجمه به زبان طبیعی داخل یک عامل یا ویرایشگر داشته باشید.
- شما می‌خواهید ترجمه Markdown یا دفترچه‌ای که در آن مدل عامل میزبان بخش‌های آماده‌شده را ترجمه کند.
- می‌خواهید عامل محتوای انتخاب‌شده را ترجمه کند به‌جای کل مخزن.
- می‌خواهید یک مرحله تصویب قبل از نوشتن در کل مخزن وجود داشته باشد.
- شما یک رابط می‌خواهید که ابزارهای Markdown، دفترچه، تصویر، بازبینی و بازنویسی مسیر را در اختیار بگذارد.

## چگونه با هم سازگارند

CLI بهترین گزینه پیش‌فرض برای انسان‌ها هنگام ترجمه مخازن است. Python API زمانی بهتر است که کد شما جریان کاری را در اختیار داشته باشد. سرور MCP زمانی بهتر است که یک عامل یا ویرایشگر جریان کاری را در اختیار داشته باشد.

هر سه مسیر از همان API عمومی Co-op Translator استفاده می‌کنند، بنابراین می‌توانید با CLI شروع کنید، بعدها با پایتون خودکارسازی کنید، و همان قابلیت‌ها را زمانی که به جریان‌های کاری تحت هدایت عامل نیاز دارید، در اختیار کلاینت‌های MCP قرار دهید.