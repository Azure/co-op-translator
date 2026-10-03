# راهنمای نگهدارنده

این صفحه خلاصه می‌کند که چگونه API، CLI و سایت مستندات به هم متصل شده‌اند.

## مرز API عمومی

API پایتون پایدار از اینجا صادر می‌شود:

```python
co_op_translator.api
```

API عمومی به کمک‌کننده‌های ترجمه محتوا، کمک‌کننده‌های بازنویسی مسیر، ارکستراسیون پروژه و بازبینی سازماندهی شده است:

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

`TranslationStateProvider` مرز پایداری برای یکپارچه‌سازی‌های میزبانی‌شده است.
باید نامزدهای تولیدشده را از خطوط پایه پذیرفته‌شده جدا نگه دارد تا یک
ترجمهٔ ادغام‌نشده نتواند منبع حقیقت شود.

هنگام افزودن APIهای عمومی جدید، به‌روزرسانی کنید:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- تست‌های API مرتبط در زیر `tests/co_op_translator/`، مانند `test_api.py` یا `test_review_api.py`

از مستندسازی ماژول‌های سطح‌پایین `core` به‌عنوان API پایدار خودداری کنید مگر اینکه پروژه قصد داشته باشد آن‌ها را مستقیماً پشتیبانی کند.

## نقاط ورود CLI

این بسته اسکریپت‌های Poetry زیر را تعریف می‌کند:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` بر اساس نام اسکریپت هدایت می‌کند:

- `translate` تابع `co_op_translator.cli.translate.translate_command` را فراخوانی می‌کند
- `evaluate` تابع `co_op_translator.cli.evaluate.evaluate_command` را فراخوانی می‌کند
- `migrate-links` تابع `co_op_translator.cli.migrate_links.migrate_links_command` را فراخوانی می‌کند
- `co-op-review` تابع `co_op_translator.cli.review.review_command` را فراخوانی می‌کند

`co-op-translator-mcp` از `__main__.py` عبور می‌کند و به‌طور مستقیم `co_op_translator.mcp.server:main` را فراخوانی می‌کند.

هنگام افزودن یا تغییر گزینه‌های CLI، به‌روزرسانی کنید:

- فرمان مرتبط در `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- تست‌های مرتبط با CLI، در صورت تغییر رفتار

## سرور MCP

سرور MCP در این فایل‌ها پیاده‌سازی شده است:

```python
co_op_translator.mcp.server
```

سرور عمداً API عمومی پایتون را می‌پوشاند (به‌جای اینکه ماژول‌های سطح‌پایین `core` را فراخوانی کند). این مرز را دست‌نخورده نگه دارید تا مشتریان MCP، فراخوانندگان پایتون و CLI رفتار یکسانی داشته باشند.

هنگام افزودن یا تغییر ابزارهای MCP، به‌روزرسانی کنید:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` اگر سطح API عمومی تغییر کند

ابزارهای ترجمه مخزن از طریق MCP قابل فراخوانی توسط مدل هستند و می‌توانند فایل‌های زیادی بنویسند. مقدار پیش‌فرض را `dry_run=True` نگه دارید و قبل از ترجمه پروژه در حالت غیر dry-run، نیاز به `confirm_write=True` داشته باشید.

## جریان ترجمه

جریان سطح‌بالای ترجمه پروژه به‌صورت زیر است:

1. تجزیهٔ آرگومان‌های CLI یا پارامترهای API.
2. اعتبارسنجی پیکربندی LLM با `LLMConfig`.
3. اعتبارسنجی Azure AI Vision وقتی ترجمهٔ تصویر انتخاب شده است.
4. نرمال‌سازی کدهای زبان.
5. تشخیص نام‌های مستعار پوشه‌های زبان قدیمی.
6. برآورد حجم ترجمه.
7. در صورت لزوم بخش‌های زبان/دوره در README را به‌روزرسانی کنید.
8. واگذاری ترجمه پروژه به `ProjectTranslator`.
9. `ProjectTranslator` پردازش فایل را به `TranslationManager` واگذار می‌کند.

`TranslationManager` از mixinهای متمرکز بر نوع فایل تشکیل شده است:

- `ProjectMarkdownTranslationMixin` خواندن فایل‌های Markdown، ترجمهٔ محتوا، بازنویسی مسیرها، متادیتا، سلب‌مسئولیت‌ها و نوشتن‌ها را مدیریت می‌کند.
- `ProjectNotebookTranslationMixin` خواندن فایل‌های نوت‌بوک، ترجمهٔ سلول‌های Markdown، بازنویسی مسیرها، متادیتا، سلب‌مسئولیت‌ها و نوشتن‌ها را مدیریت می‌کند.
- `ProjectImageTranslationMixin` کشف تصاویر، استخراج/ترجمه متن، نوشتن تصاویر رندرشده و متادیتا را مدیریت می‌کند.

APIهای محتوای سطح پایین از گردش کار پروژه صرف‌نظر می‌کنند:

1. `translate_markdown_content` و `translate_notebook_content` فقط محتوای در حافظه را ترجمه می‌کنند.
2. `translate_image_content` متن در یک تصویر را ترجمه می‌کند و یک شیء تصویر رندرشده برمی‌گرداند.
3. `rewrite_markdown_paths` و `rewrite_notebook_paths` کمک‌کننده‌های صریح پس‌پردازش هستند. آن‌ها هیچ ترجمه‌ای انجام نمی‌دهند و هیچ نوشتن پروژه‌ای انجام نمی‌دهند.

## جریان بازبینی

جریان بازبینی قطعی به‌صورت زیر است:

1. تجزیهٔ آرگومان‌های CLI یا پارامترهای API.
2. نرمال‌سازی کدهای زبان درخواست‌شده.
3. ساخت یک یا چند هدف بازبینی از `root_dir`، `root_dirs` یا `groups`.
4. به‌طور اختیاری فایل‌های منبع را با `--changed-from` محدود کنید.
5. اجرای چک‌های قطعی برای ساختار، تازگی ترجمه، یکپارچگی Markdown و مسیرهای لینک/تصویر محلی.
6. چاپ خروجی متنی یا Markdown با فرمت GitHub.
7. در صورت یافتن خطاهای بازبینی، با وضعیت شکست خارج شوید.

جریان بازبینی به کلیدهای API نیاز ندارد و برای بررسی‌های محلی یا CI مشتریان که به‌صورت اختیاری فعال می‌شوند در دسترس باقی می‌ماند. این مخزن به‌طور خودکار `co-op-review` را در هر pull request اجرا نمی‌کند.

## سایت مستندات

سایت مستندات با موارد زیر پیکربندی شده است:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

دایرکتوری `docs/` منبع مرجع مستندات است. راهنماهای جدید کاربران نهایی را بیرون از این دایرکتوری اضافه نکنید مگر اینکه پروژه عمداً یک سطح مستنداتی منتشرشدهٔ دیگر معرفی کند.

ساخت به‌صورت محلی:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

پیش‌نمایش محلی:

```bash
python -m mkdocs serve
```

سایت تولیدشده در `site/` نوشته می‌شود که توسط git نادیده گرفته شده است.

## روند کاری GitHub Pages

فایل `.github/workflows/docs.yml` سایت را در pull requestها می‌سازد و در هنگام push به `main` آن را مستقر می‌کند.

روند کاری نصب می‌کند:

```bash
pip install -r requirements-docs.txt
```

روند کاری مستندات تنها ابزارهای مربوط به مستندسازی را نصب می‌کند. `mkdocs.yml` به `mkdocstrings` می‌گوید که از `src/` استفاده کند تا صفحات API عمومی بتوانند از درخت سورس بدون نصب مجموعه کامل وابستگی‌های اجرایی رندر شوند. اگر در آینده مستندات API نیاز به وارد کردن فراهم‌کننده‌های اختیاری زمان اجرا در زمان ساخت داشته باشند، هر دو فایل `.github/workflows/docs.yml` و این راهنما را با هم به‌روزرسانی کنید.

## معیار کیفیت مستندات

قبل از ادغام تغییرات مستندات، اجرا کنید:

```bash
python -m mkdocs build --strict
git diff --check
```

از ساخت‌های سخت‌گیرانه استفاده کنید تا لینک‌های شکسته، ورودی‌های ناوبری نامعتبر و مشکلات رندر API زود شناسایی و باعث شکست شوند.