# رابط برنامه‌نویسی پایتون

رابط برنامه‌نویسی عمومی و پایدار پایتون از `co_op_translator.api` صادر می‌شود. بیشتر یکپارچه‌سازی‌ها از یکی از این جریان‌های کاری استفاده می‌کنند:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | برنامه شما محتوای منبع را می‌خواند، برای ترجمه به Co-op Translator فراخوانی می‌کند و تصمیم می‌گیرد نتیجه را کجا ذخیره کند. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | میزبان MCP یا مدل برنامه شما بخش‌ها را ترجمه می‌کند، در حالی که Co-op Translator وظایف بخش‌بندی و بازسازی را انجام می‌دهد. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | می‌خواهید رابط پایتون مانند CLI رفتار کند و کشف فایل‌ها، مسیرهای خروجی، متادیتا، پاک‌سازی و نوشتن‌ها را بر عهده بگیرد. | `run_translation` |

بیشتر ماژول‌های سطح پایین‌تر تحت `core`، `config`، `review` و `utils` جزئیات پیاده‌سازی هستند که توسط این نقاط ورود API استفاده می‌شوند.

کلاینت‌های MCP همان API عمومی را از طریق [MCP Server](mcp.md) استفاده می‌کنند. وقتی مستقیم از پایتون فراخوانی می‌کنید از این صفحه استفاده کنید، و هنگام در معرض قرار دادن Co-op Translator برای یک عامل یا ویرایشگر از راهنمای MCP استفاده کنید. اگر بین CLI، رابط پایتون و MCP تردید دارید، از [Choose Your Workflow](workflows.md) شروع کنید.

## جریان اولیهٔ استفاده از API

اگر از کد پایتون Co-op Translator را فراخوانی می‌کنید از اینجا شروع کنید:

1. یک ارائه‌دهنده LLM را همان‌طور که در [Configuration](configuration.md) توضیح داده شده پیکربندی کنید، مگر اینکه فقط بخواهید بخش‌های Markdown یا نوت‌بوک را برای ترجمه توسط میزبان-عامل آماده کنید.
2. تصمیم بگیرید که آیا برنامه شما مسئول عملیات خواندن/نوشتن فایل است یا خیر.
3. وقتی برنامه شما فایل‌های مجزا را می‌خواند و می‌نویسد از APIهای محتوایی استفاده کنید.
4. زمانی که Co-op Translator باید یک مخزن را مانند CLI پردازش کند از `run_translation` استفاده کنید.
5. بعد از ترجمه در صورت نیاز به بررسی قطعی در اتوماسیون از `run_review` استفاده کنید.

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## سناریوی 1: ترجمهٔ فایل‌ها یا اسناد منفرد

از این جریان کاری زمانی استفاده کنید که قبلاً یک فایل، بافر ویرایشگر، payload نوت‌بوک، درخواست MCP، یا ورودی لولهٔ سفارشی دارید. کد شما مسئول I/O فایل است:

1. محتوای منبع را بخوانید.
2. یک API ترجمهٔ محتوا را فراخوانی کنید.
3. در صورت نیاز یک API بازنویسی مسیر را فراخوانی کنید اگر محتوای ترجمه‌شده قرار است در پوشهٔ ترجمهٔ پروژه نوشته شود.
4. نتیجه را در برنامه‌تان ذخیره یا بازگردانید.

APIهای ترجمهٔ محتوا کشف پروژه را اجرا نمی‌کنند، متادیتا نمی‌نویسند، متن‌های هشدار را اضافه نمی‌کنند و به‌طور خودکار لینک‌ها را بازنویسی نمی‌کنند.

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

اگر Markdown ترجمه‌شده قرار نیست در چیدمان پروژهٔ Co-op Translator قرار بگیرد، از `rewrite_markdown_paths` صرف‌نظر کنید و رشتهٔ ترجمه‌شده را مستقیماً ذخیره کنید.

### فایل نوت‌بوک

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

`translate_notebook_content` سلول‌های Markdown را ترجمه می‌کند و سلول‌های غیر-Markdown را حفظ می‌کند. بازنویسی مسیر تنها روی سلول‌های Markdown اعمال می‌شود.

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

`translate_image_content` تصویر منبع را می‌خواند و یک `PIL.Image.Image` رندرشده بازمی‌گرداند. متادیتای تصویر ترجمه‌شده را نمی‌نویسد.

## سناریوی 2: ترجمهٔ یک مخزن کامل

از این جریان کاری استفاده کنید وقتی می‌خواهید رابط پایتون مانند CLI رفتار کند. `run_translation` فایل‌های پشتیبانی‌شده را کشف می‌کند، انواع محتوای انتخاب‌شده را ترجمه می‌کند، مسیرها را بازنویسی می‌کند، فایل‌های خروجی را می‌نویسد، متادیتا را به‌روزرسانی می‌کند و وظایف نگهداری ترجمه مانند پاک‌سازی را انجام می‌دهد.

`run_translation` نقطهٔ ورود ترجیحی برای ارکستراسیون پروژه است. `translate_project` به عنوان یک نام مستعار سازگاری با همان رفتار صادر می‌شود.

ترجمهٔ فایل‌های Markdown در مخزن جاری به کره‌ای و ژاپنی:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

فقط نوت‌بوک‌ها را از یک ریشهٔ پروژه مشخص ترجمه کنید:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

حجم ترجمه را بدون نوشتن فایل‌ها پیش‌نمایش دهید:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

چند ریشهٔ محتوایی را در یک فراخوانی ترجمه کنید:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

ترجمه‌ها را در گروه‌های خروجی صریح بنویسید:

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

هنگامی که هر زبان باید یک زیرپوشهٔ تو در تو داشته باشد از یک نگهدارندهٔ مخصوص زبان استفاده کنید:

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

اگر هیچ‌یک از `markdown`، `notebook` یا `images` تنظیم نشده باشند، API همهٔ انواع پشتیبانی‌شده را ترجمه می‌کند: Markdown، نوت‌بوک‌ها و تصاویر.

## بازبینی خروجی ترجمه‌شده

`run_review` بررسی‌های ترجمهٔ قطعی را بدون اعتبارات LLM یا Vision اجرا می‌کند.

!!! note "Beta"
    `run_review` یک API بازبینی قطعی در نسخهٔ بتا است. این API فراخوانی ارائه‌دهندگان مدل یا نوشتن فایل‌ها را انجام نمی‌دهد، اما قوانین و طرح‌های مسأله ممکن است تغییر کنند.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

فقط فایل‌هایی که نسبت به یک مرجع پایه تغییر کرده‌اند را بازبینی کنید و خروجی با فرمت GitHub را چاپ کنید:

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

## مثال‌های API برای کپی-پیست

ترجمهٔ محتوای Markdown بدون نوشتن فایل:

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
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

ترجمهٔ یک مخزن از طریق پایتون:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

ترجمهٔ چند ریشه:

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

حفظ اصطلاحات فرهنگ‌لغت:

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

## نقاط ورودی عمومی

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## APIهای ترجمهٔ محتوا

APIهای ترجمهٔ محتوا برای یکپارچه‌سازی‌هایی طراحی شده‌اند که قبلاً محتوا را در حافظه دارند، مانند افزونهٔ ویرایشگر، ابزار MCP، پردازشگر نوت‌بوک یا لولهٔ سفارشی.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. فقط محتوای Markdown را ترجمه می‌کند. لینک‌ها را بازنویسی نمی‌کند، متادیتا نمی‌نویسد و متن‌های هشدار را اضافه نمی‌کند. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. سلول‌های Markdown را ترجمه می‌کند و سلول‌های غیر-Markdown را حفظ می‌کند. لینک‌ها را بازنویسی نمی‌کند، متادیتا نمی‌نویسد و متن‌های هشدار را اضافه نمی‌کند. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. متن داخل تصویر را استخراج و ترجمه می‌کند، سپس یک تصویر رندرشده بازمی‌گرداند. متادیتای تصویر ترجمه‌شده را ذخیره نمی‌کند. |

`translate_markdown_content` و `translate_notebook_content` یک `source_path` اختیاری را از طریق گزینه‌هایشان می‌پذیرند. مسیر به‌عنوان زمینه به مبدل منتقل می‌شود؛ فراخوان‌ها پس از ترجمه همچنان مسئول هر بازنویسی مسیر خاص پروژه هستند.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

گزینه‌های مشابه را می‌توان به‌صورت دیکشنری نیز پاس داد:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## APIهای ترجمه با کمک عامل

APIهای کمکی عامل از Co-op Translator برای فراخوانی Azure OpenAI یا OpenAI استفاده نمی‌کنند. آن‌ها بخش‌هایی از Markdown یا نوت‌بوک را برای ترجمه توسط میزبان-عامل آماده می‌کنند و سپس محتوای نهایی را از بخش‌های ترجمه‌شده بازسازی می‌کنند.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | یک کار Markdown خودکفا با بخش‌ها، پرامپت‌ها و وضعیت بازسازی بازمی‌گرداند. |
| `finish_markdown_agent_translation` | Markdown را از یک کار و بخش‌های ترجمه‌شدهٔ میزبان-عامل بازسازی می‌کند. |
| `start_notebook_agent_translation` | یک کار نوت‌بوک با بخش‌های سلول‌های Markdown برای ترجمه توسط میزبان-عامل بازمی‌گرداند. |
| `finish_notebook_agent_translation` | JSON نوت‌بوک را بازسازی می‌کند در حالی که سلول‌های کد، خروجی‌ها و متادیتا را حفظ می‌کند. |

این جریان کاری عمدتاً برای میزبان‌های MCP در نظر گرفته شده است. اگر نیاز به ترجمهٔ مخزن در تولید با مدیریت فراخوانی ارائه‌دهنده توسط Co-op Translator دارید، از `translate_markdown_content`، `translate_notebook_content` یا `run_translation` استفاده کنید.

## APIهای بازنویسی مسیر

APIهای بازنویسی مسیر هیچ ترجمه‌ای انجام نمی‌دهند. آن‌ها لینک‌ها و مسیرهای frontmatter را پس از اینکه فراخوان‌ها مسیر منبع، مسیر ترجمه‌شدهٔ هدف و چیدمان پروژه را دانستند به‌روزرسانی می‌کنند.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | لینک‌های Markdown و زمینه‌های مسیر frontmatter پشتیبانی‌شده را برای یک هدف ترجمه‌شده بازنویسی می‌کند. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | بازنویسی مسیر Markdown را روی هر سلول Markdown اعمال می‌کند و سلول‌های غیر-Markdown را بدون تغییر باقی می‌گذارد. |

آرگومان `policy` ممکن است یک دیکشنری با این فیلدها باشد:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | کد زبان هدف، مانند `"ko"` یا `"pt-BR"`. |
| `root_dir` | No | ریشهٔ پروژهٔ منبع. پیش‌فرض `"."` است. |
| `translations_dir` | No | دایرکتوری خروجی ترجمهٔ متن. پیش‌فرض `translations` زیر `root_dir` است. |
| `translated_images_dir` | No | دایرکتوری خروجی تصاویر ترجمه‌شده. پیش‌فرض `translated_images` زیر `root_dir` است. |
| `translation_types` | No | انواع ترجمهٔ فعال. پیش‌فرض Markdown، نوت‌بوک‌ها و تصاویر است. |
| `lang_subdir` | No | زیرپوشهٔ اختیاری زیر هر پوشهٔ زبان. |

## پارامترهای ترجمهٔ پروژه

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | کدهای زبان هدف جداشده با فاصله، مانند `"ko ja fr"`، یا `"all"`. کدهای مستعار به مقادیر BCP 47 کانونیکال نرمال‌سازی می‌شوند. |
| `root_dir` | `str` | `"."` | ریشهٔ پروژه برای یک هدف ترجمهٔ واحد. وقتی `root_dirs` یا `groups` عرضه شود نادیده گرفته می‌شود. |
| `update` | `bool` | `False` | حذف و بازسازی ترجمه‌های موجود برای زبان‌های انتخاب‌شده. |
| `images` | `bool` | `False` | شامل ترجمهٔ تصویر. نیازمند پیکربندی Azure AI Vision است. |
| `markdown` | `bool` | `False` | شامل ترجمهٔ Markdown. |
| `notebook` | `bool` | `False` | شامل ترجمهٔ نوت‌بوک Jupyter. |
| `debug` | `bool` | `False` | فعال‌سازی لاگ‌گیری در حالت اشکال‌زدایی. |
| `save_logs` | `bool` | `False` | ذخیرهٔ فایل‌های لاگ با سطح DEBUG در زیر دایرکتوری `logs/` ریشه. |
| `yes` | `bool` | `True` | تأیید خودکار پرسش‌ها برای استفاده برنامه‌ای و CI. |
| `add_disclaimer` | `bool` | `False` | افزودن متن‌های هشدار ترجمهٔ ماشینی به Markdownها و نوت‌بوک‌های ترجمه‌شده. |
| `translations_dir` | `str \| None` | `None` | دایرکتوری خروجی متن ترجمه‌شدهٔ سفارشی. مسیرهای نسبی در برابر هر ریشه حل می‌شوند. |
| `image_dir` | `str \| None` | `None` | دایرکتوری خروجی تصاویر ترجمه‌شدهٔ سفارشی. مسیرهای نسبی در برابر هر ریشه حل می‌شوند. |
| `root_dirs` | `Iterable[str] \| None` | `None` | چند ریشه که تنظیمات خروجی یکسانی را به اشتراک می‌گذارند. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | زوج‌های صریح `(root_dir, translations_dir)`. بر `root_dirs` اولویت دارد. |
| `repo_url` | `str \| None` | `None` | URL مخزن که هنگام رندر کردن راهنمای جدول زبان README استفاده می‌شود. |
| `glossaries` | `Iterable[str] \| None` | `None` | اصطلاحات فرهنگ‌لغتی که باید در حین ترجمه حفظ شوند. تکراری‌ها و اصطلاحات خالی نرمال‌سازی می‌شوند. |
| `dry_run` | `bool` | `False` | برآورد حجم ترجمه و پیش‌نمایش رفتار مهاجرت بدون نوشتن فایل‌ها. |

## پارامترهای بازبینی

`run_review` عمداً تا حد امکان امضای `run_translation` را آینه‌سازی می‌کند تا اتوماسیون بتواند با حداقل انشعاب بین گردش‌های کاری ترجمه و بازبینی جابجا شود.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | پوشه‌های زبان هدف برای بازبینی. رشته‌های جداشده با فاصله و مجموعه‌ها پذیرفته می‌شوند. `"all"` همهٔ زبان‌های ترجمه‌شدهٔ کشف‌شده را بازبینی می‌کند. |
| `root_dir` | `str` | `"."` | ریشهٔ پروژه برای یک هدف بازبینی واحد. وقتی `root_dirs` یا `groups` عرضه شود نادیده گرفته می‌شود. |
| `markdown` | `bool` | `False` | شامل فایل‌های منبع Markdown و MDX. |
| `notebook` | `bool` | `False` | شامل فایل‌های منبع نوت‌بوک Jupyter. |
| `images` | `bool` | `False` | برای توازن با گزینه‌های ترجمه رزرو شده است. ارجاعات لینک به تصاویر از Markdown بررسی می‌شوند. |
| `translations_dir` | `str \| None` | `None` | دایرکتوری خروجی ترجمه متون سفارشی. مسیرهای نسبی نسبت به هر روت حل می‌شوند. |
| `root_dirs` | `Iterable[str] \| None` | `None` | چند روت که تنظیمات خروجی یکسانی را به اشتراک می‌گذارند. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | جفت‌های صریح (root_dir, translations_dir). برتری نسبت به `root_dirs` دارد. |
| `changed_from` | `str \| None` | `None` | مرجع Git که برای محدود کردن بررسی به فایل‌های منبع تغییر یافته استفاده می‌شود. |
| `output_format` | `str` | `"text"` | فرمت خروجی بررسی. مقادیر پشتیبانی‌شده `"text"` و `"github"` هستند. |
| `fail_on_warnings` | `bool` | `False` | اخطارها را علاوه بر خطاها به عنوان شکست در نظر بگیرید. |
| `debug` | `bool` | `False` | ثبت‌لاگ اشکال‌زدایی را فعال کنید. |
| `save_logs` | `bool` | `False` | فایل‌های لاگ سطح DEBUG را در زیرشاخه ریشه `logs/` ذخیره کنید. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## نیازمندی‌های پیکربندی

Provider-backed translation APIs require provider configuration before translating:

- Markdown and notebook translation require an LLM provider. Configure either Azure OpenAI or OpenAI.
- Image translation requires Azure AI Vision in addition to the LLM provider.
- `run_translation` runs lightweight connectivity checks before project translation begins.
- Agent-assisted `start_*_agent_translation` and `finish_*_agent_translation` APIs do not call Co-op Translator LLM providers. The host application or MCP agent translates the prepared chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` are deterministic and do not require provider credentials.

Required Azure OpenAI variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Required OpenAI variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Required Azure AI Vision variables for image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` is deterministic and does not require Azure OpenAI, OpenAI, or Azure AI Vision configuration.

## نکات رفتار

- APIهای ترجمه محتوا ترجمه را جدا از بازنویسی مسیر پروژه نگه می‌دارند. هنگامی که محتوای ترجمه‌شده نیاز به تنظیم لینک‌های نسبی پروژه برای مکان هدف دارد، به‌طور صریح `rewrite_markdown_paths` یا `rewrite_notebook_paths` را فراخوانی کنید.
- APIهای ارکستراسیون پروژه رفتارهای مربوط به پروژه را در اطراف ترجمه محتوا اضافه می‌کنند، از جمله کشف فایل، نوشتن‌ها، بازنویسی مسیرها، متادیتا، پاک‌سازی و سلب مسئولیت‌های اختیاری.
- `run_translation` prints progress and estimate summaries through Click, matching the CLI user experience.
- `dry_run=True` computes estimates using virtual README updates, but does not write the README or translation files.
- `groups` are processed sequentially. A single aggregate estimate is printed before work begins.
- When image translation is selected, missing Vision configuration raises an error before translation starts.
- Existing alias-based language folders are detected and can be migrated to canonical language folder names as part of the run.
- `run_review` fails on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` reports missing local Markdown and image link targets as warnings by default.

## مسیر فراخوان داخلی

The API delegates to the same core implementation used by the CLI:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| کلاس | ماژول | مسئولیت |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | هماهنگ‌سازی ترجمه در سطح پروژه، مدیریت دایرکتوری، نرمال‌سازی متادیتا برای هر زبان، و واگذاری به مترجمان Markdown، نوت‌بوک و تصویر. |
| `TranslationManager` | `co_op_translator.core.project.translation` | کار پردازش فایل‌های ناهمگام برای Markdown، نوت‌بوک‌ها، تصاویر، تشخیص قدیمی بودن، و به‌روزرسانی‌های متادیتای ترجمه را انجام می‌دهد. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | خواندن فایل‌های Markdown، ترجمه محتوا، بازنویسی مسیر، متادیتا، سلب مسئولیت‌ها و نوشتن‌ها را هماهنگ می‌کند. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | خواندن فایل‌های نوت‌بوک، ترجمه سلول‌های Markdown، بازنویسی مسیر، متادیتا، سلب مسئولیت‌ها و نوشتن‌ها را هماهنگ می‌کند. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | کشف تصاویر منبع، ترجمه تصویر، مسیرهای خروجی، متادیتا و نوشتن‌ها را هماهنگ می‌کند. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | جفت‌های Markdown ترجمه‌شده را پیدا می‌کند، کیفیت ترجمه را ارزیابی می‌کند، و متادیتای اطمینان را برای جریان‌های کاری تعمیر با اطمینان پایین می‌خواند. |
| `ReviewRunner` | `co_op_translator.review.runner` | بررسی‌های قطعی را در سراسر فایل‌های منبع، زبان‌های هدف و روت‌های ترجمه پیکربندی‌شده هماهنگ می‌کند. |
| `ReviewTarget` | `co_op_translator.review.targets` | یک روت منبع و دایرکتوری خروجی ترجمه شده برای آن روت را توصیف می‌کند. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | پوشه‌های زبانی قدیمی مبتنی بر نام مستعار را شناسایی کرده و طرح‌های مهاجرت پوشه به نام‌های کاننیکال BCP 47 را آماده می‌کند. |
| `Config` | `co_op_translator.config.base_config` | فایل‌های `.env` را بارگذاری کرده و بررسی می‌کند که آیا ارائه‌دهندگان LLM مورد نیاز و Vision اختیاری پیکربندی شده‌اند. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | به‌صورت خودکار Azure OpenAI یا OpenAI را تشخیص می‌دهد، متغیرهای محیطی ضروری را تأیید می‌کند و چک‌های اتصال ارائه‌دهنده را اجرا می‌کند. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | پیکربندی Azure AI Vision را تشخیص داده و چک‌های اتصال را برای ترجمه تصویر اجرا می‌کند. |