# راهنمای نگهدارنده

این صفحه خلاصه می‌کند که چگونه API، CLI، و سایت مستندات به‌هم متصل شده‌اند.

## مرز API عمومی

API پایدار پایتون از این مکان صادر می‌شود:

```python
co_op_translator.api
```

API عمومی به ابزارهای کمکی ترجمه محتوا، ابزارهای کمکی بازنویسی مسیر، ارکستراسیون پروژه و بازبینی تقسیم شده است:

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

هنگام افزودن APIهای عمومی جدید، به‌روزرسانی کنید:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- تست‌های مرتبط با API تحت `tests/co_op_translator/`، مانند `test_api.py` یا `test_review_api.py`

از مستندسازی ماژول‌های سطح پایین‌تر `core` به‌عنوان API پایدار خودداری کنید مگر اینکه پروژه بخواهد آن‌ها را به‌طور مستقیم پشتیبانی کند.

## نقاط ورود CLI

پکیج این اسکریپت‌های Poetry را تعریف می‌کند:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` بر اساس نام اسکریپت هدایت می‌کند:

- `translate` فراخوانی می‌کند `co_op_translator.cli.translate.translate_command`
- `evaluate` فراخوانی می‌کند `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` فراخوانی می‌کند `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` فراخوانی می‌کند `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` از `__main__.py` عبور می‌کند و مستقیماً `co_op_translator.mcp.server:main` را فراخوانی می‌کند.

هنگام افزودن یا تغییر گزینه‌های CLI، به‌روزرسانی کنید:

- فرمان `src/co_op_translator/cli/*.py` مربوطه
- `docs/cli.md`
- تست‌های مرتبط با CLI، در صورت تغییر رفتار

## سرور MCP

سرور MCP در این فایل پیاده‌سازی شده است:

```python
co_op_translator.mcp.server
```

سرور عمداً یک لایه روی API عمومی پایتون قرار می‌دهد به‌جای اینکه مستقیماً ماژول‌های سطح پایین‌تر `core` را صدا بزند. این مرز را دست‌نخورده نگه دارید تا کلاینت‌های MCP، فراخوان‌های پایتون و CLI رفتار یکسانی داشته باشند.

هنگام افزودن یا تغییر ابزارهای MCP، به‌روزرسانی کنید:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` اگر سطح API عمومی تغییر کند

ابزارهای ترجمه مخزن از طریق MCP قابل فراخوانی توسط مدل هستند و می‌توانند فایل‌های زیادی بنویسند. مقدار پیش‌فرض را `dry_run=True` نگه دارید و قبل از ترجمه پروژه‌ای که dry-run نیست، نیاز به `confirm_write=True` داشته باشید.

## جریان ترجمه

جریان کلی ترجمه پروژه به‌صورت زیر است:

1. پارامترهای CLI یا پارامترهای API را تحلیل می‌کند.
2. `LLMConfig` را برای پیکربندی LLM اعتبارسنجی می‌کند.
3. هنگام انتخاب ترجمه تصویر، Azure AI Vision را اعتبارسنجی می‌کند.
4. کدهای زبان را نرمال‌سازی می‌کند.
5. نام‌های مستعار پوشه‌های زبان قدیمی را تشخیص می‌دهد.
6. حجم ترجمه را برآورد می‌کند.
7. در صورت قابل اعمال بودن، بخش‌های زبان/دوره در README را به‌روزرسانی می‌کند.
8. ترجمه پروژه را به `ProjectTranslator` واگذار می‌کند.
9. `ProjectTranslator` پردازش فایل‌ها را به `TranslationManager` واگذار می‌کند.

`TranslationManager` از mixinهای متمرکز بر نوع فایل تشکیل شده است:

- `ProjectMarkdownTranslationMixin` خواندن فایل‌های Markdown، ترجمه محتوا، بازنویسی مسیرها، فراداده، سلب‌مسئولیت‌ها و عملیات نوشتن را مدیریت می‌کند.
- `ProjectNotebookTranslationMixin` خواندن فایل‌های نوت‌بوک، ترجمه سلول‌های Markdown، بازنویسی مسیرها، فراداده، سلب‌مسئولیت‌ها و عملیات نوشتن را مدیریت می‌کند.
- `ProjectImageTranslationMixin` کشف تصاویر، استخراج/ترجمه متن، نوشتن تصاویر رندرشده و فراداده را مدیریت می‌کند.

APIهای سطح پایین‌تر محتوا از جریان کاری پروژه چشم‌پوشی می‌کنند:

1. `translate_markdown_content` و `translate_notebook_content` فقط محتوای درون‌حافظه‌ای را ترجمه می‌کنند.
2. `translate_image_content` متن داخل یک تصویر را ترجمه می‌کند و یک شی تصویر رندرشده برمی‌گرداند.
3. `rewrite_markdown_paths` و `rewrite_notebook_paths` ابزارهای کمکی صریح پس‌پردازش هستند. آن‌ها هیچ ترجمه‌ای انجام نمی‌دهند و هیچ نوشتن پروژه‌ای انجام نمی‌شود.

## جریان بازبینی

جریان بازبینی قطعی به‌صورت زیر است:

1. پارامترهای CLI یا پارامترهای API را تحلیل می‌کند.
2. کدهای زبان درخواست‌شده را نرمال‌سازی می‌کند.
3. یک یا چند هدف بازبینی از `root_dir`، `root_dirs` یا `groups` می‌سازد.
4. به‌صورت اختیاری فایل‌های منبع را با `--changed-from` محدود می‌کند.
5. چک‌های قطعی برای ساختار، تازه‌بودن ترجمه، یکپارچگی Markdown، و مسیرهای لینک/تصویر محلی را اجرا می‌کند.
6. یا خروجی متنی یا Markdown با فرمت GitHub را چاپ می‌کند.
7. هنگام یافتن خطاهای بازبینی با شکست خارج می‌شود.

جریان بازبینی به API key نیاز ندارد و باید برای CI درخواست کشش مناسب باقی بماند. جریان کاری pull request در هر اجرا یک خلاصه بررسی می‌نویسد و تنها زمانی یک کامنت PR ارسال می‌کند که `co-op-review` شکست بخورد.

## سایت مستندات

سایت مستندات با این موارد پیکربندی شده است:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

دایرکتوری `docs/` منبع رسمی مستندات است. راهنماهای جدید برای کاربران نهایی را خارج از این دایرکتوری اضافه نکنید مگر اینکه پروژه عمداً یک سطح مستندسازی منتشرشده دیگر معرفی کند.

ساخت محلی:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

پیش‌نمایش محلی:

```bash
python -m mkdocs serve
```

سایت تولیدشده به `site/` نوشته می‌شود، که توسط git نادیده گرفته شده است.

## گردش‌کار GitHub Pages

`.github/workflows/docs.yml` سایت را در pull requestها می‌سازد و آن را هنگام push به `main` مستقر می‌کند.

این گردش‌کار نصب می‌کند:

```bash
pip install -r requirements-docs.txt
```

گردش‌کار مستندات تنها زنجیره ابزار مستندسازی را نصب می‌کند. `mkdocs.yml`، `mkdocstrings` را به `src/` اشاره می‌دهد تا صفحات API عمومی بتوانند از درخت منبع رندر شوند بدون نصب مجموعه کامل وابستگی‌های زمان اجرا. اگر مستندات API آینده نیاز به وارد کردن ارائه‌دهنده‌های زمان‌اجرای اختیاری در زمان ساخت داشتند، هم `.github/workflows/docs.yml` و هم این راهنما را با هم به‌روز کنید.

## سطح کیفیت مستندات

قبل از ادغام تغییرات مستندات، اجرا کنید:

```bash
python -m mkdocs build --strict
git diff --check
```

از ساخت‌های سخت‌گیرانه استفاده کنید تا لینک‌های شکسته، ورودی‌های ناوبری نامعتبر و مشکلات رندرینگ API زود تشخیص داده شده و باعث شکست شوند.