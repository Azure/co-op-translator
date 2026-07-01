# انتخاب جریان کاری شما

Co-op Translator می‌تواند به سه روش استفاده شود: CLI، API پایتون، و سرور MCP. آن‌ها توانایی‌های ترجمه یکسانی دارند، اما هر کدام برای یک جریان کاری متفاوت مناسب‌اند.

از این صفحه زمانی استفاده کنید که می‌خواهید تصمیم بگیرید از کجا شروع کنید.

## تصمیم سریع

| اگر می‌خواهید... | استفاده کنید | از اینجا شروع کنید |
| --- | --- | --- |
| Translate or review a repository from a terminal | CLI | [راهنمای CLI](cli.md) |
| Add translation to a Python script, service, notebook, or CI job | Python API | [API پایتون](api.md) |
| Let an agent, editor, or MCP-compatible client translate content for you | MCP Server | [سرور MCP](mcp.md) |
| Translate one Markdown document, notebook, or image that your app already loaded | Python API or MCP Server | [API پایتون](api.md) or [سرور MCP](mcp.md) |
| Translate an entire repository with standard output folders and metadata | CLI or `run_translation` | [راهنمای CLI](cli.md) or [API پایتون](api.md) |

## چه زمانی از CLI استفاده کنید

CLI را انتخاب کنید وقتی یک نفر یا یک کار CI ترجمهٔ مخزن را از یک شِل هدایت می‌کند.

CLI ساده‌ترین مسیر است وقتی می‌خواهید Co-op Translator فایل‌های پروژه را پیدا کند، خروجی‌های ترجمه‌شده بسازد، ساختار پروژه را حفظ کند، متادیتا را به‌روزرسانی کند، و دستورات بازبینی را اجرا کند.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

موارد مناسب:

- شما در حال ترجمهٔ یک مخزن از طریق ترمینال خود هستید.
- شما می‌خواهید یک فرمان تکرارشونده برای گردش‌کار CI یا انتشار داشته باشید.
- شما می‌خواهید کشف پروژه، مسیرهای خروجی، متادیتا، پاک‌سازی و بازبینی داخلی داشته باشید.
- شما رابط دستوری را به نوشتن کد Python ترجیح می‌دهید.

## چه زمانی از API پایتون استفاده کنید

API پایتون را انتخاب کنید وقتی کد خودتان باید جریان کار را کنترل کند.

این API برای برنامه‌ها، اسکریپت‌های اتوماسیون، دفترچه‌های یادداشت، سرویس‌ها، و خطوط پردازش سفارشی مفید است. این اجازه را می‌دهد که APIهای ترجمهٔ محتوای سطح پایین را برای فایل‌های منفرد فراخوانی کنید، یا همان ارکستراسیون سطح مخزن که توسط CLI استفاده می‌شود را اجرا کنید.

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

اجرای ترجمهٔ مخزن از پایتون:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

موارد مناسب:

- برنامهٔ شما در حال حاضر فایل‌ها، بافرها، دفترچهٔ یادداشت یا بایت‌های تصویر را می‌خواند.
- شما به اعتبارسنجی، ذخیره‌سازی، ثبت، تلاش مجدد، یا جریان‌های تصویب سفارشی نیاز دارید.
- شما می‌خواهید یک سند، دفترچهٔ یادداشت، یا تصویر را ترجمه کنید بدون پردازش کل مخزن.
- شما می‌خواهید ترجمهٔ مخزن را، اما از اتوماسیون Python به جای یک فرمان شِل انجام دهید.

## چه زمانی از سرور MCP استفاده کنید

سرور MCP را انتخاب کنید وقتی یک عامل، ویرایشگر، یا کلاینت سازگار با MCP باید ابزارهای Co-op Translator را فراخوانی کند.

در تنظیم محلی معمول، کاربر به‌صورت دستی سرور را روشن نگه نمی‌دارد. کلاینت MCP هنگام نیاز به ابزارها، `co-op-translator-mcp` را از طریق `stdio` راه‌اندازی می‌کند.

نمونه درخواست‌های کاربر که یک عامل می‌تواند رسیدگی کند:

- "این فایل Markdown را به کره‌ای ترجمه کن و لینک‌ها را درست نگه دار."
- "این فایل Markdown را با گردش‌کار MCP همراه با کمک عامل ترجمه کن، با استفاده از مدل خودت برای بخش‌های ترجمه‌شده."
- "این دفترچه یادداشت را به کره‌ای ترجمه کن، سلول‌های کد را حفظ کن، و از Co-op Translator MCP برای بازسازی دفترچه استفاده کن."
- "متن داخل این تصویر را به ژاپنی ترجمه کن و نتیجه را ذخیره کن."
- "یک اجرای آزمون (dry-run) از ترجمهٔ مخزن به اسپانیایی انجام بده و به من بگو چه تغییراتی رخ می‌دهد."
- "بررسی کن که خروجی ترجمهٔ کره‌ای به‌روز هست یا نه."

برای Markdown و دفترچه‌ها، MCP می‌تواند در دو حالت کار کند:

| حالت | استفاده وقتی | ابزارهای اصلی |
| --- | --- | --- |
| Agent-assisted | عامل میزبان MCP باید بخش‌ها را با مدل خود ترجمه کند، بدون اعتبارنامه‌های ارائه‌دهنده LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator باید مستقیماً Azure OpenAI or OpenAI را فراخوانی کند. | `translate_markdown_content`, `translate_notebook_content` |

قالب فراخوانی ابزار Markdown در حالت پشتیبانی‌شده توسط ارائه‌دهنده در MCP:

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

قالب فراخوانی ابزار تصویر در MCP:

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

ترجمهٔ مخزن به‌صورت پیش‌فرض از طریق MCP به‌صورت dry-run است:

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

- شما می‌خواهید گردش‌کارهای ترجمه به زبان طبیعی درون یک عامل یا ویرایشگر داشته باشید.
- شما می‌خواهید ترجمهٔ Markdown یا دفترچه را که در آن مدل عامل میزبان بخش‌های آماده‌شده را ترجمه می‌کند.
- شما می‌خواهید عامل تنها محتوای انتخاب‌شده را ترجمه کند نه کل مخزن را.
- شما می‌خواهید یک مرحلهٔ تصویب قبل از نوشتن در سطح مخزن داشته باشید.
- شما می‌خواهید یک رابط که ابزارهای Markdown، دفترچه، تصویر، بازبینی و بازنویسی مسیر را در دسترس قرار می‌دهد.

## چگونه با هم کار می‌کنند

CLI بهترین گزینهٔ پیش‌فرض برای انسان‌هایی است که مخازن را ترجمه می‌کنند. API پایتون بهترین گزینه است وقتی کد شما مالک جریان کار است. سرور MCP بهترین گزینه است وقتی یک عامل یا ویرایشگر مالک جریان کار است.

هر سه مسیر از همان API عمومی Co-op Translator استفاده می‌کنند، بنابراین می‌توانید با CLI شروع کنید، بعداً با Python اتوماسیون کنید، و همان قابلیت‌ها را وقتی به گردش‌های کاری هدایت‌شده توسط عامل نیاز دارید به کلاینت‌های MCP در دسترس قرار دهید.