# رابط برنامه‌نویسی پایتون

رابط عمومی پایدار پایتون از `co_op_translator.api` صادر می‌شود. بیشتر یکپارچه‌سازی‌ها از یکی از این روندها استفاده می‌کنند:

| سناریو | از این زمانی استفاده کنید | APIهای اصلی |
| --- | --- | --- |
| ترجمه فایل‌ها یا اسناد منفرد | برنامهٔ شما محتوای منبع را می‌خواند، برای ترجمه به Co-op Translator فراخوانی می‌کند و تصمیم می‌گیرد نتیجه را کجا ذخیره کند. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| آماده‌سازی محتوا برای ترجمه توسط عامل میزبان | میزبان MCP یا مدل برنامهٔ شما قطعات را ترجمه خواهد کرد، در حالی که Co-op Translator تقسیم‌بندی و بازسازی را مدیریت می‌کند. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ترجمه یک مخزن کامل | می‌خواهید API پایتون مانند CLI رفتار کند و کشف فایل‌ها، مسیرهای خروجی، متادیتا، پاکسازی و نوشتن‌ها را مدیریت کند. | `run_translation` |

اکثر ماژول‌های سطح پایین تحت `core`، `config`، `review` و `utils` جزئیات پیاده‌سازی هستند که توسط این نقاط ورود API استفاده می‌شوند.

کلاینت‌های MCP از همان API عمومی از طریق [سرور MCP](mcp.md) استفاده می‌کنند. هنگام فراخوانی مستقیم پایتون از این صفحه استفاده کنید، و هنگام در معرض قرار دادن Co-op Translator به یک عامل یا ویرایشگر از راهنمای MCP استفاده کنید. اگر بین CLI، API پایتون، و MCP تصمیم می‌گیرید، با [روند کاری خود را انتخاب کنید](workflows.md) شروع کنید.

## روند اولیهٔ API

اگر Co-op Translator را از کد پایتون فراخوانی می‌کنید، از اینجا شروع کنید:

1. یک ارائه‌دهنده LLM را مطابق توضیحات در [پیکربندی](configuration.md) پیکربندی کنید، مگر اینکه تنها در حال آماده‌سازی قطعات Markdown یا دفترچه برای ترجمه توسط عامل میزبان باشید.
2. تصمیم بگیرید آیا برنامهٔ شما مسئول ورودی/خروجی فایل است.
3. وقتی برنامهٔ شما فایل‌های منفرد را می‌خواند و می‌نویسد، از APIهای محتوا استفاده کنید.
4. هنگامی که Co-op Translator باید یک مخزن را مانند CLI پردازش کند، از `run_translation` استفاده کنید.
5. اگر به بررسی‌های قطعی در اتوماسیون نیاز دارید، پس از ترجمه از `run_review` استفاده کنید.

| هدف | API برای شروع |
| --- | --- |
| ترجمه یک رشته یا فایل Markdown | `translate_markdown_content` |
| ترجمه محتوای یک دفترچه | `translate_notebook_content` |
| ترجمه یک تصویر | `translate_image_content` |
| اجازه دهید یک عامل میزبان قطعات Markdown یا دفترچه را ترجمه کند | `start_markdown_agent_translation` یا `start_notebook_agent_translation` |
| بازنویسی لینک‌های ترجمه‌شده پس از انتخاب مسیر خروجی | `rewrite_markdown_paths` یا `rewrite_notebook_paths` |
| ترجمه یک مخزن کامل | `run_translation` |
| بازبینی خروجی ترجمه‌شده | `run_review` |

## سناریو ۱: ترجمه فایل‌ها یا اسناد منفرد

از این روند زمانی استفاده کنید که قبلاً یک فایل، بافر ویرایشگر، محتوای دفترچه، درخواست MCP، یا ورودی خط لولهٔ سفارشی را دارید. کد شما مسئول ورودی/خروجی فایل است:

1. محتوای منبع را بخوانید.
2. یک API ترجمهٔ محتوا را فراخوانی کنید.
3. در صورت تمایل، یک API بازنویسی مسیر را فراخوانی کنید اگر محتوای ترجمه‌شده قرار است در یک پوشهٔ ترجمهٔ پروژه نوشته شود.
4. نتیجه را در برنامهٔ خود ذخیره یا بازگردانید.

APIهای ترجمهٔ محتوا کشف پروژه را اجرا نمی‌کنند، متادیتا نمی‌نویسند، اظهارات سلب مسؤولیت را الصاق نمی‌کنند و به‌طور خودکار لینک‌ها را بازنویسی نمی‌کنند.

### فایل Markdown

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


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
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

اگر Markdown ترجمه‌شده در ساختار پروژهٔ Co-op Translator قرار نخواهد گرفت، `rewrite_markdown_paths` را رد کنید و رشتهٔ ترجمه‌شده را مستقیماً ذخیره کنید.

### فایل دفترچه

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` سلول‌های Markdown را ترجمه می‌کند و سلول‌های غیر-Markdown را حفظ می‌کند. بازنویسی مسیر تنها به سلول‌های Markdown اعمال می‌شود.

### فایل تصویر

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` تصویر منبع را می‌خواند و یک `PIL.Image.Image` رندر شده بازمی‌گرداند. متادیتای تصویر ترجمه‌شده را نمی‌نویسد.

## سناریو ۲: ترجمه یک مخزن کامل

از این روند زمانی استفاده کنید که می‌خواهید API پایتون مانند CLI `translate` رفتار کند. `run_translation` فایل‌های پشتیبانی‌شده را کشف می‌کند، انواع محتوای انتخاب‌شده را ترجمه می‌کند، مسیرها را بازنویسی می‌کند، فایل‌های خروجی را می‌نویسد، متادیتا را به‌روز می‌کند و وظایف نگهداری ترجمه مانند پاکسازی را انجام می‌دهد.

`run_translation` نقطهٔ ورود ارجح برای هماهنگی پروژه است. `translate_project` به‌عنوان یک نام مستعار سازگاری با همان رفتار صادر شده است.

فایل‌های Markdown را در مخزن فعلی به کره‌ای و ژاپنی ترجمه کنید:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

فقط دفترچه‌ها را از ریشهٔ پروژهٔ مشخص ترجمه کنید:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

پیش‌نمایش حجم ترجمه بدون نوشتن فایل‌ها:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

ثبت رویدادهای پیشرفت ساختارمند برای یک یکپارچه‌سازی:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # پی‌لود را در جدول رویدادهای شغل خود ذخیره کنید یا آن را به رابط کاربری‌تان به صورت جریان پخش کنید.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

رویدادها از اسکیمای نسخه‌بندی‌شدهٔ `co-op.translation.event.v1` استفاده می‌کنند. یکپارچه‌سازی‌ها باید
به فیلدهای ثابت مانند `type` و `stage_key` وابسته باشند،
نه به متن کنسول قابل‌فهم برای انسان یا `stage_label`.

چندین ریشهٔ محتوا را در یک فراخوانی ترجمه کنید:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

نوشتن ترجمه‌ها در گروه‌های خروجی صریح:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

از نگهدارندهٔ مخصوص هر زبان استفاده کنید وقتی هر زبان باید یک زیرپوشهٔ تو در تو داشته باشد:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

اگر هیچ‌یک از `markdown`، `notebook` یا `images` تنظیم نشده باشند، API تمام انواع پشتیبانی‌شده را ترجمه می‌کند: Markdown، دفترچه‌ها، و تصاویر.

### حفظ ویرایش‌های پذیرفته‌شدهٔ انسانی با یک ارائه‌دهندهٔ وضعیت ترجمه

به‌طور پیش‌فرض، Co-op Translator رفتار سطح-فایل موجود خود را حفظ می‌کند: زمانی که یک
منبع Markdown قدیمی باشد، کل فایل ترجمه‌شده بازتولید می‌شود. یکپارچه‌سازی‌های میزبانی‌شده
می‌توانند اختیاری یک `TranslationStateProvider` ارسال کنند تا ویرایش‌های انسانی را
در بلوک‌های منبعی که تغییر نکرده‌اند حفظ کنند.

این ارائه‌دهنده جفت منبع/هدف پذیرفته‌شدهٔ آخر را فراهم می‌کند و هر نامزد جدید را ثبت می‌کند
نامزد. پذیرش همچنان مسئولیت یکپارچه‌سازی است—برای مثال،
پس از ادغام یک pull request ترجمه:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

برای فایل‌های Markdown با یک خط مبنای پذیرفته‌شدهٔ معتبر، Co-op Translator
بلوک‌های سطح‌بالای Markdown را تراز می‌کند. بلوک‌های منبع بدون تغییر از بلوک‌های ترجمه‌شدهٔ فعلی استفاده می‌کنند،
از جمله ویرایش‌های انجام‌شده توسط افراد؛ بلوک‌های منبع تغییر‌کرده یا اضافه‌شده برای ترجمه ارسال می‌شوند
برای ترجمه؛ بلوک‌های منبع حذف‌شده حذف می‌شوند. اگر تراز مبهم باشد،
ساختار هدف تغییر کرده باشد، ترجمهٔ یک بلوک نامعتبر باشد، یا هیچ خط مبنایی موجود نباشد،
Co-op Translator به‌طور ایمن به مسیر ترجمهٔ کامل فایل موجود بازمی‌گردد.


بخش‌ها بین اسناد. در حال حاضر این برای ترجمهٔ پروژه‌های Markdown اعمال می‌شود.
رفتار دفترچه و تصویر بدون تغییر است. ارسال `update=True`
هنوز درخواست بازتولید کامل را می‌دهد.


`RuntimeError` پس از پایان جریان کاری پروژه پرتاب می‌کند به‌جای گزارش یک
اجرای موفق با خروجی مفقود.
یکپارچه‌سازی‌ها باید این را به‌عنوان یک کار ناموفق در نظر بگیرند
و وضعیت ترجمهٔ پذیرفته‌شدهٔ قبلی را حفظ کنند.

## بازبینی خروجی ترجمه‌شده

`run_review` بررسی‌های ترجمهٔ قطعی را بدون اعتبارنامهٔ LLM یا Vision اجرا می‌کند.

!!! note "بتا"
    `run_review` یک API بازبینی قطعی در حالت بتا است. این API فراخوانی ارائه‌دهندگان مدل را انجام نمی‌دهد یا فایل‌ها را نمی‌نویسد، اما بررسی‌ها و اسکیمای مسائل ممکن است تغییر کنند.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

پس از ترجمه‌ای که فقط README را شامل می‌شود، از همان دامنه برای بازبینی استفاده کنید:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` تنها `README.md` را تحت هر ریشهٔ منبع پیکربندی‌شده بررسی می‌کند،
شامل `groups` سفارشی و دایرکتوری‌های خروجی. سایر اسناد و READMEهای تو در تو مستثنا هستند.
نبودن README منبع باعث پرتاب `ValueError` می‌شود؛ بررسی‌های ترجمه ناموفق
منجر به پرتاب `RuntimeError` می‌شوند.

فقط فایل‌هایی را که نسبت به یک مرجع پایه تغییر کرده‌اند بازبینی کنید و خروجی با فرمت GitHub را چاپ کنید:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## مثال‌های قابل کپی-پیست API

محتوای Markdown را بدون نوشتن فایل ترجمه کنید:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

ترجمه و بازنویسی لینک‌های Markdown:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

ترجمه یک مخزن از پایتون:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

ترجمه چندین ریشه:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

حفظ اصطلاحات واژه‌نامه:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## نقاط ورود عمومی

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## APIهای ترجمه محتوا

APIهای ترجمهٔ محتوا برای یکپارچه‌سازی‌هایی در نظر گرفته شده‌اند که قبلاً محتوا را در حافظه دارند، مانند افزونهٔ ویرایشگر، ابزار MCP، پردازشگر دفترچه، یا خط لولهٔ سفارشی.

| تابع | ورودی | خروجی | ورودی/خروجی فایل | یادداشت‌ها |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | خیر | غیرهمزمان. تنها محتوای Markdown را ترجمه می‌کند. لینک‌ها را بازنویسی نمی‌کند، متادیتا را نمی‌نویسد، یا اظهارات سلب مسئولیت را الصاق نمی‌کند. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | خیر | غیرهمزمان. سلول‌های Markdown را ترجمه می‌کند و سلول‌های غیر-Markdown را حفظ می‌کند. لینک‌ها را بازنویسی نمی‌کند، متادیتا را نمی‌نویسد، یا اظهارات سلب مسئولیت را الصاق نمی‌کند. |
| `translate_image_content` | Image path | `PIL.Image.Image` | فقط تصویر منبع را می‌خواند | همزمان. متن تصویر را استخراج و ترجمه می‌کند، سپس یک تصویر رندرشده بازمی‌گرداند. متادیتای تصویر ترجمه‌شده را ذخیره نمی‌کند. |

`translate_markdown_content` و `translate_notebook_content` یک `source_path` اختیاری را از طریق گزینه‌های خود می‌پذیرند. مسیر به‌عنوان زمینه به مترجم منتقل می‌شود؛ فراخواننده‌ها همچنان مسئول هر بازنویسی مسیر خاص پروژه پس از ترجمه هستند.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

همان گزینه‌ها می‌توانند به‌صورت دیکشنری ارسال شوند:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## APIهای ترجمه با کمک عامل

APIهای با کمک عامل فراخوانی ارائه‌دهندهٔ LLM پیکربندی‌شده از Co-op Translator را انجام نمی‌دهند. آن‌ها قطعات Markdown یا دفترچه را برای ترجمه توسط عامل میزبان آماده می‌کنند، سپس محتوای نهایی را از قطعات ترجمه‌شده بازسازی می‌کنند.

| تابع | هدف |
| --- | --- |
| `start_markdown_agent_translation` | بازگرداندن یک کار Markdown خودکفا با قطعات، پرامپت‌ها و وضعیت بازسازی. |
| `finish_markdown_agent_translation` | بازسازی Markdown از یک کار و قطعات ترجمه‌شده توسط عامل میزبان. |
| `start_notebook_agent_translation` | بازگرداندن یک کار دفترچه با قطعات سلول‌های Markdown برای ترجمه توسط عامل میزبان. |
| `finish_notebook_agent_translation` | بازسازی JSON دفترچه در حالی که سلول‌های کد، خروجی‌ها و متادیتا را حفظ می‌کند. |

این روند عمدتاً برای میزبان‌های MCP در نظر گرفته شده است. اگر به ترجمهٔ مخزن تولیدی نیاز دارید که Co-op Translator فراخوانی‌های ارائه‌دهنده را مدیریت کند، از `translate_markdown_content`، `translate_notebook_content`، یا `run_translation` استفاده کنید.

## APIهای بازنویسی مسیر

APIهای بازنویسی مسیر هیچ ترجمه‌ای انجام نمی‌دهند. آن‌ها لینک‌ها و مسیرهای frontmatter را پس از اینکه فراخواننده‌ها مسیر منبع، مسیر هدف ترجمه‌شده و ساختار پروژه را بدانند به‌روزرسانی می‌کنند.

| تابع | دامنه | یادداشت‌ها |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | لینک‌های Markdown و فیلدهای مسیر frontmatter پشتیبانی‌شده را برای یک هدف ترجمه‌شده بازنویسی می‌کند. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | بازنویسی مسیر Markdown را به هر سلول Markdown اعمال می‌کند و سلول‌های غیر-Markdown را بدون تغییر رها می‌کند. |

آرگومان `policy` ممکن است یک دیکشنری با این فیلدها باشد:

| فیلد | الزامی | هدف |
| --- | --- | --- |
| `language_code` | بله | کد زبان هدف، مانند `"ko"` یا `"pt-BR"`. |
| `root_dir` | خیر | ریشهٔ پروژه منبع. مقدار پیش‌فرض `"."`. |
| `translations_dir` | خیر | دایرکتوری خروجی ترجمهٔ متن. مقدار پیش‌فرض `translations` زیر `root_dir`. |
| `translated_images_dir` | خیر | دایرکتوری خروجی تصاویر ترجمه‌شده. مقدار پیش‌فرض `translated_images` زیر `root_dir`. |
| `translation_types` | خیر | انواع ترجمهٔ فعال. مقدار پیش‌فرض Markdown، دفترچه‌ها، و تصاویر. |
| `lang_subdir` | خیر | زیرپوشهٔ اختیاری تحت هر پوشهٔ زبان. |

## پارامترهای ترجمهٔ پروژه

| پارامتر | نوع | پیش‌فرض | هدف |
| --- | --- | --- | --- |
| `language_codes` | `str` | الزامی | کدهای زبان هدف جداشده با فاصله، مانند `"ko ja fr"`، یا `"all"`. کدهای جایگزین به مقادیر استاندارد BCP 47 نرمال‌سازی می‌شوند. |
| `root_dir` | `str` | `"."` | ریشهٔ پروژه برای یک هدف ترجمهٔ واحد. هنگام ارائهٔ `root_dirs` یا `groups` نادیده گرفته می‌شود. |
| `update` | `bool` | `False` | ترجمه‌های موجود برای زبان‌های انتخاب‌شده را حذف و بازایجاد می‌کند. |
| `images` | `bool` | `False` | شامل ترجمهٔ تصویر می‌شود. نیازمند پیکربندی Azure AI Vision است. |
| `markdown` | `bool` | `False` | شامل ترجمهٔ Markdown می‌شود. |
| `notebook` | `bool` | `False` | شامل ترجمهٔ Jupyter notebook می‌شود. |
| `debug` | `bool` | `False` | فعال‌سازی لاگ دیباگ. |
| `save_logs` | `bool` | `False` | ذخیرهٔ فایل‌های لاگ با سطح DEBUG در زیرشاخهٔ `logs/` ریشه. |
| `yes` | `bool` | `True` | پرسش‌ها را برای استفاده برنامه‌ای و CI به‌طور خودکار تأیید می‌کند. |
| `add_disclaimer` | `bool` | `False` | افزودن هشدارهای مربوط به ترجمه ماشینی به فایل‌های Markdown و نوت‌بوک‌های ترجمه‌شده. |
| `translations_dir` | `str \| None` | `None` | پوشه خروجی سفارشی برای ترجمه متن. مسیرهای نسبی نسبت به هر ریشه حل می‌شوند. |
| `image_dir` | `str \| None` | `None` | پوشه خروجی تصاویر ترجمه‌شده سفارشی. مسیرهای نسبی نسبت به هر ریشه حل می‌شوند. |
| `root_dirs` | `Iterable[str] \| None` | `None` | چندین ریشه که تنظیمات خروجی یکسانی را به‌اشتراک می‌گذارند. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | جفت‌های صریح `(root_dir, translations_dir)`. بر `root_dirs` ارجحیت دارد. |
| `repo_url` | `str \| None` | `None` | URL مخزن که هنگام رندر جدول زبان README برای راهنمایی استفاده می‌شود. |
| `glossaries` | `Iterable[str] \| None` | `None` | اصطلاحات واژه‌نامه که باید در طول ترجمه حفظ شوند. تکراری‌ها و عبارات خالی نرمال‌سازی می‌شوند. |
| `dry_run` | `bool` | `False` | برآورد حجم ترجمه و پیش‌نمایش رفتار مهاجرت بدون نوشتن فایل‌ها. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | آداپتور اختیاری نگهداری پایگاه-پذیرفته‌شده و نامزد برای به‌روزرسانی‌های افزایشی Markdown. حذف آن رفتار موجود فایل-کامل را حفظ می‌کند. |

## پارامترهای بازبینی

`run_review` عمداً تا حد امکان امضای `run_translation` را بازتاب می‌دهد تا اتوماسیون بتواند با حداقل شاخه‌بندی بین گردش‌کار‌های ترجمه و بازبینی جابه‌جا شود.

| پارامتر | نوع | پیش‌فرض | هدف |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | پوشه‌های زبان هدف برای بازبینی. رشته‌های جداشده با فاصله و iterableها پذیرفته می‌شوند. `"all"` همه زبان‌های ترجمه کشف‌شده را بازبینی می‌کند. |
| `root_dir` | `str` | `"."` | ریشه پروژه برای یک هدف بازبینی واحد. هنگام فراهم بودن `root_dirs` یا `groups` نادیده گرفته می‌شود. |
| `markdown` | `bool` | `False` | شامل فایل‌های منبع Markdown و MDX باشد. |
| `notebook` | `bool` | `False` | شامل فایل‌های منبع Jupyter notebook باشد. |
| `images` | `bool` | `False` | برای توازن با گزینه‌های ترجمه محفوظ است. ارجاعات لینکی به تصاویر از Markdown بررسی می‌شوند. |
| `translations_dir` | `str \| None` | `None` | پوشه خروجی سفارشی برای ترجمه متن. مسیرهای نسبی نسبت به هر ریشه حل می‌شوند. |
| `root_dirs` | `Iterable[str] \| None` | `None` | چندین ریشه که تنظیمات خروجی یکسانی را به‌اشتراک می‌گذارند. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | جفت‌های صریح `(root_dir, translations_dir)`. بر `root_dirs` ارجحیت دارد. |
| `changed_from` | `str \| None` | `None` | مرجع Git که برای محدود کردن بازبینی به فایل‌های منبع تغییرکرده استفاده می‌شود. |
| `readme_only` | `bool` | `False` | فقط `README.md` زیر هر ریشه منبع را بازبینی کند. نبود README منبع منجر به `ValueError` می‌شود. |
| `output_format` | `str` | `"text"` | فرمت خروجی بازبینی. مقادیر پشتیبانی‌شده `"text"` و `"github"` هستند. |
| `fail_on_warnings` | `bool` | `False` | هشدارها را علاوه بر خطاها به‌عنوان شکست در نظر بگیرد. |
| `debug` | `bool` | `False` | فعال‌سازی لاگ‌گیری اشکال‌زدایی. |
| `save_logs` | `bool` | `False` | ذخیره فایل‌های لاگ در سطح DEBUG زیر پوشه ریشه `logs/`. |

اگر هیچ‌کدام از `markdown`، `notebook`، یا `images` تنظیم نشده باشند، API در جاهایی که مناسب است Markdown، نوت‌بوک‌ها و ارجاعات لینک تصویر را بازبینی می‌کند. بازبینی فراخوانی ارائه‌دهنده LLM ندارد و به کلیدهای API نیاز ندارد.

## نیازمندی‌های پیکربندی

APIهای ترجمه مبتنی بر ارائه‌دهنده نیازمند پیکربندی ارائه‌دهنده قبل از ترجمه هستند:

- ترجمه Markdown و نوت‌بوک نیاز به یک ارائه‌دهنده LLM دارد. Azure OpenAI، OpenAI، یا Anthropic را پیکربندی کنید.
- ترجمه تصویر علاوه بر ارائه‌دهنده LLM نیاز به Azure AI Vision دارد.
- `run_translation` قبل از آغاز ترجمه پروژه بررسی‌های اتصال سبک را اجرا می‌کند.
- APIهای کمکی عامل `start_*_agent_translation` و `finish_*_agent_translation` فراخوانی‌کننده‌های LLM Co-op Translator را صدا نمی‌زنند. برنامه میزبان یا عامل MCP قطعات آماده‌شده را ترجمه می‌کند.
- `rewrite_markdown_paths`، `rewrite_notebook_paths` و `run_review` قطعی هستند و به مدارک ارائه‌دهنده نیاز ندارند.

متغیرهای موردنیاز Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

متغیرهای موردنیاز OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

متغیرهای موردنیاز Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` و `ANTHROPIC_MAX_TOKENS` اختیاری هستند. Microsoft Agent Framework از Co-op Translator نسخه 0.22.0 به بعد مشتری مدل پیش‌فرض برای همه ارائه‌دهندگان است. Semantic Kernel هنوز را می‌توان موقتاً با `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` انتخاب کرد، اما انجام این کار یک هشدار منسوخ‌سازی صادر می‌کند؛ طرح حذف تدریجی را در [پیکربندی](configuration.md#model-client-backend) ببینید.

متغیرهای موردنیاز Azure AI Vision برای ترجمه تصویر:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` قطعی است و نیازی به پیکربندی LLM یا Azure AI Vision ندارد.

## نکات رفتاری

- APIهای ترجمه محتوا ترجمه را از بازنویسی مسیرهای پروژه جدا نگه می‌دارند. وقتی محتوای ترجمه‌شده نیاز به تنظیم لینک‌های نسبی پروژه برای مکان هدف دارد، به‌صراحت `rewrite_markdown_paths` یا `rewrite_notebook_paths` را فراخوانی کنید.
- APIهای هماهنگی پروژه رفتارهای پروژه را حول ترجمه محتوا اضافه می‌کنند، از جمله کشف فایل، نوشتن‌ها، بازنویسی مسیرها، متاداده، پاک‌سازی و هشدارهای اختیاری.
- `run_translation` پیشرفت و خلاصه‌های برآورد را از طریق همان گزارشگر مبتنی بر Rich که CLI استفاده می‌کند چاپ می‌کند. خروجی غیرتعاملی به متن ساده تنزل می‌یابد.
- `dry_run=True` برآوردها را با استفاده از بروزرسانی‌های README مجازی محاسبه می‌کند، اما README یا فایل‌های ترجمه را نمی‌نویسد.
- `groups` به‌صورت متوالی پردازش می‌شوند. یک برآورد تجمعی واحد قبل از شروع کار چاپ می‌شود.
- وقتی ترجمه تصویر انتخاب شده باشد، پیکربندی Vision مفقود قبل از شروع ترجمه خطا ایجاد می‌کند.
- پوشه‌های زبان مبتنی بر نام‌های مستعار موجود شناسایی می‌شوند و می‌توان آن‌ها را به نام‌های پوشه زبان کاننیکال BCP 47 به‌عنوان بخشی از اجرا مهاجرت داد.
- `run_review` در صورت فایل‌های ترجمه‌شده مفقود، متاداده ترجمه مفقود یا کهنه، frontmatter/fenceهای کد نامنظم Markdown، و JSON نوت‌بوک ترجمه‌شده نامعتبر شکست می‌خورد.
- `run_review` به‌طور پیش‌فرض اهداف محلی Markdown و لینک‌های تصویر مفقود را به‌صورت هشدار گزارش می‌کند.

## مسیر فراخوانی داخلی

API به همان پیاده‌سازی هسته که توسط CLI استفاده می‌شود واگذار می‌کند:

ترجمه:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` برای ترجمه در حافظه. |
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` برای پردازش پس‌از مسیرها به‌صورت صریح. |
3. `co_op_translator.api.translation.run_translation` برای هماهنگی کامل پروژه. |
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`. |
5. `co_op_translator.core.project.ProjectTranslator`. |
6. `co_op_translator.core.project.TranslationManager`. |
7. افزونه‌های ترجمه متمرکز پروژه برای Markdown، نوت‌بوک‌ها و تصاویر. |
8. مترجم‌های Markdown، نوت‌بوک، متن و تصویر تحت `co_op_translator.core`. |

بازبینی:

1. `co_op_translator.api.review.run_review` |
2. `co_op_translator.review.targets.build_review_targets` |
3. `co_op_translator.review.runner.ReviewRunner` |
4. چک‌های قطعی تحت `co_op_translator.review.checks` |

کلاس‌های زیر برای نگهدارندگان مفید هستند، اما به‌عنوان API پایدار در سطح بسته صادر نمی‌شوند.

| کلاس | ماژول | مسئولیت |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | هماهنگ‌کننده ترجمه در سطح پروژه، مدیریت دایرکتوری، نرمال‌سازی متاداده در هر زبان، و ارجاع به مترجم‌های Markdown، نوت‌بوک و تصویر. |
| `TranslationManager` | `co_op_translator.core.project.translation` | اجرای کار پردازش فایل به‌صورت async برای Markdown، نوت‌بوک‌ها، تصاویر، تشخیص کهنگی، و به‌روزرسانی متاداده ترجمه. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | هماهنگی خواندن فایل‌های Markdown، ترجمه محتوا، بازنویسی مسیرها، متاداده، هشدارها، و نوشتن‌ها. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | هماهنگی خواندن فایل‌های نوت‌بوک، ترجمه سلول‌های Markdown، بازنویسی مسیرها، متاداده، هشدارها، و نوشتن‌ها. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | هماهنگی کشف تصاویر منبع، ترجمه تصویر، مسیرهای خروجی، متاداده، و نوشتن‌ها. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | یافتن جفت‌های Markdown ترجمه‌شده، ارزیابی کیفیت ترجمه، و خواندن متاداده اطمینان برای گردش‌کارهای تعمیر با اطمینان پایین. |
| `ReviewRunner` | `co_op_translator.review.runner` | هماهنگی چک‌های قطعی بازبینی در سراسر فایل‌های منبع، زبان‌های هدف، و ریشه‌های ترجمه پیکربندی‌شده. |
| `ReviewTarget` | `co_op_translator.review.targets` | توصیف یک ریشه منبع و پوشه خروجی ترجمه که برای آن ریشه بازبینی می‌شود. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | تشخیص پوشه‌های زبان قدیمی مبتنی بر نام مستعار و آماده‌سازی طرح‌های مهاجرت پوشه‌های کاننیکال BCP 47. |
| `Config` | `co_op_translator.config.base_config` | بارگذاری فایل‌های `.env` و بررسی اینکه آیا ارائه‌دهنده‌های LLM مورد نیاز و Vision اختیاری پیکربندی شده‌اند. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | تشخیص خودکار Azure OpenAI، OpenAI، یا Anthropic، اعتبارسنجی متغیرهای محیطی موردنیاز، و اجرای بررسی‌های اتصال ارائه‌دهنده. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | تشخیص پیکربندی Azure AI Vision و اجرای بررسی‌های اتصال برای ترجمه تصویر. |