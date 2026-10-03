# پائتھن API

مستحکم عوامی Python API کو `co_op_translator.api` سے برآمد کیا جاتا ہے۔ زیادہ تر انضمام ان میں سے ایک ورک فلو استعمال کرتے ہیں:

| منظر نامہ | اسے کب استعمال کریں | اہم APIs |
| --- | --- | --- |
| انفرادی فائلیں یا دستاویزات ترجمہ کریں | آپ کی ایپلیکیشن ماخذ مواد پڑھتی ہے، Co-op Translator کو ترجمے کے لیے کال کرتی ہے، اور نتیجہ کہاں محفوظ کرنا ہے طے کرتی ہے۔ | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| ہوسٹ-ایجنٹ کے ترجمے کے لیے مواد تیار کریں | آپ کا MCP ہوسٹ یا ایپلیکیشن ماڈل چنکس کا ترجمہ کرے گا، جبکہ Co-op Translator چنکنگ اور دوبارہ تعمیر کو سنبھالتا ہے۔ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| مکمل ریپوزٹری کا ترجمہ کریں | آپ چاہتے ہیں کہ Python API CLI کی طرح برتاؤ کرے اور دریافت، آؤٹ پٹ راستے، میٹاڈیٹا، صفائی، اور لکھائی سنبھالے۔ | `run_translation` |

زیادہ تر نچلے درجے کے ماڈیولز جو `core`, `config`, `review`, اور `utils` کے تحت آتے ہیں، ان API اندراج پوائنٹس کے لیے استعمال ہونے والی عملدرآمدی تفصیلات ہیں۔

MCP کلائنٹس وہی پبلک API [MCP سرور](mcp.md) کے ذریعے استعمال کرتے ہیں۔ جب آپ Python کو براہِ راست کال کر رہے ہوں تو اس صفحے کا استعمال کریں، اور جب Co-op Translator کو کسی ایجنٹ یا ایڈیٹر کے سامنے ظاہر کر رہے ہوں تو MCP گائیڈ استعمال کریں۔ اگر آپ CLI، Python API، اور MCP کے درمیان فیصلہ کر رہے ہیں، تو [اپنا ورک فلو منتخب کریں](workflows.md) سے شروعات کریں۔

## پہلی بار API فلو

اگر آپ Python کوڈ سے Co-op Translator کال کر رہے ہیں تو یہاں سے شروع کریں:

1. LLM فراہم کنندہ کو [Configuration](configuration.md) میں بیان کے مطابق ترتیب دیں، جب تک کہ آپ صرف Markdown یا نوٹ بک چنکس کو ہوسٹ-ایجنٹ کے ترجمے کے لیے تیار نہیں کر رہے ہوں۔
2. فیصلہ کریں کہ آیا آپ کی ایپلیکیشن فائل I/O کی ملکیت رکھتی ہے۔
3. جب آپ کی ایپلیکیشن انفرادی فائلیں پڑھتی اور لکھتی ہو تو کنٹینٹ APIs استعمال کریں۔
4. جب Co-op Translator کو CLI کی طرح ریپوزٹری پروسیس کرنا چاہیے تو `run_translation` استعمال کریں۔
5. اگر آپ کو آٹومیشن میں متعین (deterministic) چیکس کی ضرورت ہو تو ترجمے کے بعد `run_review` استعمال کریں۔

| مقصد | شروع کرنے کے لیے API |
| --- | --- |
| ایک Markdown سٹرنگ یا فائل ترجمہ کریں | `translate_markdown_content` |
| ایک نوٹ بک پیلوڈ ترجمہ کریں | `translate_notebook_content` |
| ایک تصویر ترجمہ کریں | `translate_image_content` |
| ہوسٹ ایجنٹ کو Markdown یا نوٹ بک چنکس کا ترجمہ کرنے دیں | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| آؤٹ پٹ راستہ منتخب کرنے کے بعد ترجمہ شدہ لنکس کو دوبارہ لکھیں | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| مکمل ریپوزٹری ترجمہ کریں | `run_translation` |
| ترجمہ شدہ آؤٹ پٹ کا جائزہ لیں | `run_review` |

## منظر نامہ 1: انفرادی فائلیں یا دستاویزات کا ترجمہ

جب آپ کے پاس پہلے سے فائل، ایڈیٹر بفر، نوٹ بک پیلوڈ، MCP ریکوئسٹ، یا کسٹم پائپ لائن ان پٹ موجود ہو تو یہ ورک فلو استعمال کریں۔ آپ کا کوڈ فائل I/O کا مالک ہے:

1. ماخذ مواد پڑھیں۔
2. کنٹینٹ ترجمہ API کو کال کریں۔
3. اگر ترجمہ شدہ مواد پروجیکٹ کے ترجمہ فولڈر میں لکھا جائے گا تو اختیاری طور پر پاتھ ری رائٹنگ API کو کال کریں۔
4. نتیجہ اپنی ایپلیکیشن میں محفوظ کریں یا واپس کریں۔

کنٹینٹ ترجمہ APIs پروجیکٹ کی دریافت نہیں چلائیں گی، میٹاڈیٹا نہیں لکھیں گی، ڈس کلائمرز شامل نہیں کریں گی، اور خود کار طریقے سے لنکس کو دوبارہ نہیں لکھیں گی۔

### Markdown فائل

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

اگر ترجمہ شدہ Markdown Co-op Translator پروجیکٹ لے آؤٹ میں موجود نہیں رہے گا، تو `rewrite_markdown_paths` کو چھوڑیں اور ترجمہ شدہ سٹرنگ کو براہِ راست محفوظ کریں۔

### نوٹ بک فائل

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

`translate_notebook_content` Markdown سیلز کا ترجمہ کرتا ہے اور غیر-Markdown سیلز کو برقرار رکھتا ہے۔ پاتھ ری رائٹنگ صرف Markdown سیلز پر لاگو ہوتی ہے۔

### امیج فائل

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

`translate_image_content` ماخذ تصویر پڑھتا ہے اور ایک رینڈر شدہ `PIL.Image.Image` واپس کرتا ہے۔ یہ ترجمہ شدہ تصویر کا میٹاڈیٹا نہیں لکھتا۔

## منظر نامہ 2: مکمل ریپوزٹری کا ترجمہ

جب آپ چاہتے ہیں کہ Python API `translate` CLI کی طرح برتاؤ کرے تو یہ ورک فلو استعمال کریں۔ `run_translation` سپورٹ شدہ فائلوں کی دریافت کرتا ہے، منتخب کردہ کنٹینٹ اقسام کا ترجمہ کرتا ہے، راستے دوبارہ لکھتا ہے، آؤٹ پٹ فائلیں لکھتا ہے، میٹاڈیٹا کو اپ ڈیٹ کرتا ہے، اور صفائی جیسی ترجمے کی مینٹیننس ٹاسکس انجام دیتا ہے۔

`run_translation` ترجیحی پروجیکٹ آرکسٹریشن انٹری پوائنٹ ہے۔ `translate_project` اسی رویے کے ساتھ مطابقتی عرف کے طور پر ایکسپورٹ کیا جاتا ہے۔

موجودہ ریپوزٹری میں Markdown فائلوں کو کورین اور جاپانی میں ترجمہ کریں:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

ایک مخصوص پروجیکٹ روٹ سے صرف نوٹ بکس کا ترجمہ کریں:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

فائلیں لکھے بغیر ترجمے کے حجم کا پیش نظارہ کریں:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

کسی انٹیگریشن کے لیے ساختی پیش رفت ایونٹس ریکارڈ کریں:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # اپنے جاب-ایونٹ ٹیبل میں پیلوڈ محفوظ کریں یا اسے اپنی یو آئی پر اسٹریم کریں۔


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

ایونٹس ورژن شدہ اسکیمہ `co-op.translation.event.v1` استعمال کرتے ہیں۔ انٹیگریشنز کو
مستحکم فیلڈز جیسے `type` اور `stage_key` پر انحصار کرنا چاہیے، نہ کہ انسانی-سامنے
کنسول متن یا `stage_label` پر۔

ایک کال میں متعدد کنٹینٹ روٹس کا ترجمہ کریں:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

ترجموں کو واضح آؤٹ پٹ گروپس میں لکھیں:

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

جب ہر زبان میں ایک نیسٹڈ سب ڈائریکٹری ہونی چاہیے تو فی زبان پلیس ہولڈر استعمال کریں:

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

اگر `markdown`، `notebook`، یا `images` میں سے کوئی بھی سیٹ نہیں ہے، تو API تمام سپورٹڈ اقسام کا ترجمہ کرتا ہے: Markdown، نوٹ بکس، اور تصاویر۔

### منظور شدہ انسانی ترمیمات کو ترجمہ اسٹیٹ پرووائیڈر کے ساتھ محفوظ کریں

ڈیفالٹ کے طور پر، Co-op Translator اپنی موجودہ فائل-سطح رویہ کو برقرار رکھتا ہے: جب ایک
Markdown ماخذ پرانا ہو جاتا ہے، تو پوری ترجمہ شدہ فائل دوبارہ جنریٹ کی جاتی ہے۔ ہوسٹڈ
انٹیگریشنز اختیاری طور پر `TranslationStateProvider` پاس کر سکتی ہیں تاکہ انسانی
ترمیمات اُن سورس بلاکس میں محفوظ رکھی جائیں جو تبدیل نہیں ہوئے۔

پرووائیڈر آخری قبول شدہ ماخذ/ہدف جوڑی فراہم کرتا ہے اور ہر نئے
امیدوار (candidate) کو ریکارڈ کرتا ہے۔ قبولیت انٹیگریشن کی ذمہ داری ہی رہتی ہے—مثال کے طور پر،
جب ایک ترجمے کا پل ریکویسٹ مرج ہو جائے:

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

Markdown فائلوں کے لیے، اگر ایک معتبر قبول شدہ بنیاد موجود ہو، تو Co-op Translator ہم آہنگ کرتا ہے
ٹاپ-لیول Markdown بلاکس کو۔ غیر تبدیل شدہ ماخذ بلاکس موجودہ ترجمہ شدہ
بلاکس کو دوبارہ استعمال کرتے ہیں، بشمول لوگوں کی جانب سے کی گئی ترامیم؛ تبدیل شدہ یا شامل کیے گئے ماخذ بلاکس ترجمے کے لیے بھیجے جاتے ہیں
ہیں؛ حذف کیے گئے ماخذ بلاکس ہٹا دیے جاتے ہیں۔ اگر الائنمنٹ مبہم ہو،
ہدف ساخت بدل گئی ہو، کسی بلاک کا ترجمہ نامناسب ہو، یا کوئی بنیاد
دستیاب نہ ہو، تو Co-op Translator محفوظ طریقے سے موجودہ پورے فائل کے
ترجمے کے راستے پر واپس آ جاتا ہے۔

یہ API دستاویزاتی ترجمے کی حالت محفوظ کرتی ہے، نہ کہ دستاویزات کے مابین کسی فریز یا
حصہ وار ترجمہ میموری۔ یہ فی الحال Markdown پروجیکٹ ترجمہ پر لاگو ہوتا ہے
۔ نوٹ بک اور تصویر کا طرزِ عمل تبدیل نہیں ہوتا۔ `update=True` پاس کرنا
اب بھی مکمل دوبارہ جنریشن کی درخواست کرتا ہے۔

اگر ایک یا زیادہ فائلیں ترجمہ نہیں ہو سکتیں، تو `run_translation` پروجیکٹ ورک فلو ختم ہونے کے بعد
`RuntimeError` پھینکے گا بجائے اس کے کہ وہ کامیاب رن رپورٹ کرے جس میں آؤٹ پٹ غائب ہو۔
انٹیگریشنز کو اسے ایک ناکام جاب سمجھنا چاہیے اور
پچھلی قبول شدہ ترجمہ حالت کو برقرار رکھنا چاہیے۔

## ترجمہ شدہ آؤٹ پٹ کا جائزہ

`run_review` بغیر LLM یا Vision کریڈینشلز کے متعین (deterministic) ترجمہ چیکس چلاتا ہے۔

!!! note "Beta"
    `run_review` ایک بیٹا متعین ریویو API ہے۔ یہ ماڈل پرووائیڈرز کو کال نہیں کرتا اور فائلیں نہیں لکھتا، مگر چیکس اور ایشو سکیمیں تبدیل ہو سکتی ہیں۔

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

صرف README کے ترجمے کے بعد، جائزے کے لیے وہی اسکوپ استعمال کریں:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` صرف ہر ترتیب شدہ سورس روٹ کے تحت `README.md` کا جائزہ لیتا ہے،
بشمول کسٹم `groups` اور آؤٹ پٹ ڈائریکٹریز۔ دیگر دستاویزات اور نیسٹڈ
READMEs کو خارج کیا جاتا ہے۔ ایک غائب ماخذ README `ValueError` اٹھاتا ہے؛ ناکام
ترجمہ چیکس `RuntimeError` اٹھاتے ہیں۔

صرف وہ فائلیں جائزہ لیں جو بیس ریف کے مقابلے میں تبدیل ہوئی ہیں اور GitHub طرز کا آؤٹ پٹ پرنٹ کریں:

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

## کاپی-پیسٹ API مثالیں

فائل لکھے بغیر Markdown مواد کا ترجمہ کریں:

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

Markdown لنکس کا ترجمہ کریں اور دوبارہ لکھیں:

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

Python سے ایک ریپوزٹری کا ترجمہ کریں:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

متعدد روٹس کا ترجمہ کریں:

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

گلوسری اصطلاحات کو محفوظ رکھیں:

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

## پبلک انٹری پوائنٹس

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

## کنٹینٹ ترجمہ APIs

کنٹینٹ ترجمہ APIs ان انٹیگریشنز کے لیے ہیں جن کے پاس پہلے سے ہی مواد میموری میں موجود ہوتا ہے، جیسے کہ ایک ایڈیٹر ایکسٹینشن، MCP ٹول، نوٹ بک پروسیسر، یا کسٹم پائپ لائن۔

| فنکشن | ان پٹ | آؤٹ پٹ | فائل I/O | نوٹس |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | غیر متزامن۔ صرف Markdown مواد کا ترجمہ کرتا ہے۔ یہ لنکس کو دوبارہ نہیں لکھتا، میٹاڈیٹا نہیں لکھتا، یا ڈس کلیمرز شامل نہیں کرتا۔ |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | غیر متزامن۔ Markdown سیلز کا ترجمہ کرتا ہے اور غیر-Markdown سیلز کو برقرار رکھتا ہے۔ یہ لنکس کو دوبارہ نہیں لکھتا، میٹاڈیٹا نہیں لکھتا، یا ڈس کلیمرز شامل نہیں کرتا۔ |
| `translate_image_content` | Image path | `PIL.Image.Image` | صرف ماخذ تصویر پڑھتا ہے | ہم وقت۔ تصویری متن نکالتا اور ترجمہ کرتا ہے، پھر ایک رینڈر شدہ تصویر واپس کرتا ہے۔ یہ ترجمہ شدہ تصویر کا میٹاڈیٹا محفوظ نہیں کرتا۔ |

`translate_markdown_content` اور `translate_notebook_content` اپنے آپشنز کے ذریعے ایک اختیاری `source_path` قبول کرتے ہیں۔ یہ راستہ مترجم کو سیاق و سباق کے طور پر دیا جاتا ہے؛ کال کرنے والے ترجمے کے بعد کسی بھی پروجیکٹ مخصوص پاتھ ری رائٹنگ کے ذمہ دار رہتے ہیں۔

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

ایک ہی آپشنز ڈکشنریز کے طور پر بھی پاس کیے جا سکتے ہیں:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## ایجنٹ مدد یافتہ ترجمہ APIs

ایجنٹ-مدد یافتہ APIs Co-op Translator سے کنفیگر کردہ LLM پرووائیڈر کو کال نہیں کرتیں۔ یہ ہوسٹ ایجنٹ کے ترجمے کے لیے Markdown یا نوٹ بک چنکس تیار کرتی ہیں، پھر ترجمہ شدہ چنکس سے حتمی مواد کو دوبارہ تعمیر کرتی ہیں۔

| فنکشن | مقصد |
| --- | --- |
| `start_markdown_agent_translation` | ایک خود مختار Markdown جاب واپس کرتا ہے جس میں چنکس، پرامپٹس، اور دوبارہ تعمیر کی حالت ہوتی ہے۔ |
| `finish_markdown_agent_translation` | جاب اور ہوسٹ-ایجنٹ کے ترجمہ شدہ چنکس سے Markdown کو دوبارہ تعمیر کریں۔ |
| `start_notebook_agent_translation` | ہوسٹ-ایجنٹ ترجمے کے لیے Markdown-سیل چنکس کے ساتھ ایک نوٹ بک جاب واپس کریں۔ |
| `finish_notebook_agent_translation` | کوڈ سیلز، آؤٹ پٹس، اور میٹاڈیٹا کو برقرار رکھتے ہوئے نوٹ بک JSON کو دوبارہ تعمیر کریں۔ |

یہ ورک فلو بنیادی طور پر MCP ہوسٹس کے لیے مقصود ہے۔ اگر آپ کو پروڈکشن ریپوزٹری ترجمے کی ضرورت ہے جہاں Co-op Translator پرووائیڈر کالز کو مینیج کرے، تو `translate_markdown_content`, `translate_notebook_content`, یا `run_translation` استعمال کریں۔

## پاتھ ری رائٹنگ APIs

پاتھ ری رائٹنگ APIs کوئی ترجمہ انجام نہیں دیتیں۔ وہ لنکس اور فرنٹ میٹر پاتھز کو اپ ڈیٹ کرتی ہیں جب کال کرنے والے ماخذ پاتھ، ترجمہ شدہ ہدف پاتھ، اور پروجیکٹ لے آؤٹ جان لیں۔

| فنکشن | دائرہ کار | نوٹس |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown باڈی اور فرنٹ میٹر | ترجمہ شدہ ہدف کے لیے Markdown لنکس اور سپورٹڈ فرنٹ میٹر پاتھ فیلڈز کو دوبارہ لکھتا ہے۔ |
| `rewrite_notebook_paths` | نوٹ بک JSON میں Markdown سیلز | ہر Markdown سیل پر Markdown پاتھ ری رائٹنگ لاگو کرتا ہے اور غیر-Markdown سیلز کو تبدیل کیے بغیر چھوڑ دیتا ہے۔ |

`policy` دلیل ایک ڈکشنری ہو سکتی ہے جس میں یہ فیلڈز ہیں:

| فیلڈ | ضروری | مقصد |
| --- | --- | --- |
| `language_code` | Yes | ہدف زبان کا کوڈ، مثلاً `"ko"` یا `"pt-BR"`۔ |
| `root_dir` | No | سورس پروجیکٹ روٹ۔ ڈیفالٹ `"."` ہے۔ |
| `translations_dir` | No | متن ترجمہ آؤٹ پٹ ڈائریکٹری۔ ڈیفالٹ `translations` ہے جو `root_dir` کے تحت ہے۔ |
| `translated_images_dir` | No | ترجمہ شدہ تصویر آؤٹ پٹ ڈائریکٹری۔ ڈیفالٹ `translated_images` ہے جو `root_dir` کے تحت ہے۔ |
| `translation_types` | No | فعال ترجمہ کی اقسام۔ ڈیفالٹ Markdown، نوٹ بکس، اور تصاویر ہیں۔ |
| `lang_subdir` | No | ہر زبان کے فولڈر کے تحت ایک اختیاری سب ڈائریکٹری۔ |

## پروجیکٹ ترجمہ پیرامیٹرز

| پیرا میٹر | قسم | ڈیفالٹ | مقصد |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | ہدف زبان کے کوڈز جو اسپیس سے الگ کیے گئے ہوں، جیسا کہ `"ko ja fr"`، یا `"all"`۔ عرفی کوڈز canonical BCP 47 اقدار میں نارملائز کیے جاتے ہیں۔ |
| `root_dir` | `str` | `"."` | ایک واحد ترجمہ ہدف کے لیے پروجیکٹ روٹ۔ جب `root_dirs` یا `groups` فراہم کیے جائیں تو نظر انداز کیا جاتا ہے۔ |
| `update` | `bool` | `False` | منتخب زبانوں کے لیے موجودہ ترجموں کو حذف کر کے دوبارہ بنائیں۔ |
| `images` | `bool` | `False` | تصویر کے ترجمے کو شامل کریں۔ Azure AI Vision کنفیگریشن درکار ہے۔ |
| `markdown` | `bool` | `False` | Markdown ترجمہ شامل کریں۔ |
| `notebook` | `bool` | `False` | Jupyter نوٹ بک ترجمہ شامل کریں۔ |
| `debug` | `bool` | `False` | ڈیبگ لاگنگ کو اہل کریں۔ |
| `save_logs` | `bool` | `False` | DEBUG سطح کی لوگ فائلز کو روٹ `logs/` ڈائریکٹری کے تحت محفوظ کریں۔ |
| `yes` | `bool` | `True` | پروگراماتی اور CI استعمال کے لیے پرامپٹس کو خودکار طور پر تصدیق کریں۔ |
| `add_disclaimer` | `bool` | `False` | ترجمہ شدہ Markdown اور نوٹ بکس میں مشینی ترجمے کے ڈسکلیمر شامل کریں۔ |
| `translations_dir` | `str \| None` | `None` | کسٹم متن ترجمہ آؤٹ پٹ ڈائریکٹری۔ نسبتی راستے ہر روٹ کے حساب سے حل ہوتے ہیں۔ |
| `image_dir` | `str \| None` | `None` | کسٹم ترجمہ شدہ تصاویر کی آؤٹ پٹ ڈائریکٹری۔ نسبتی راستے ہر روٹ کے حساب سے حل ہوتے ہیں۔ |
| `root_dirs` | `Iterable[str] \| None` | `None` | متعدد روٹس جو ایک ہی آؤٹ پٹ سیٹنگز شیئر کرتے ہیں۔ |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | واضح `(root_dir, translations_dir)` جوڑ۔ `root_dirs` پر فوقیت رکھتا ہے۔ |
| `repo_url` | `str \| None` | `None` | README زبان کی جدول کی رہنمائی کو رینڈر کرتے وقت استعمال ہونے والا ریپوزٹری URL۔ |
| `glossaries` | `Iterable[str] \| None` | `None` | ترجمے کے دوران محفوظ رکھنے کے لیے گلاسری اصطلاحات۔ نقل شدہ اور خالی اصطلاحات کو معمول کے مطابق یکساں بنایا جاتا ہے۔ |
| `dry_run` | `bool` | `False` | فائلیں لکھے بغیر ترجمے کے حجم کا اندازہ لگائیں اور مائیگریشن کے طرز عمل کا پیش منظر دیکھیں۔ |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | مرحلہ وار Markdown اپڈیٹس کے لیے اختیاری accepted-baseline and candidate persistence adapter۔ اسے چھوڑنے سے موجودہ مکمل-فائل رویہ برقرار رہتا ہے۔ |

## جائزہ کے پیرامیٹرز

`run_review` جان بوجھ کر `run_translation` کے دستخط کی عکاسی کرتا ہے جہاں ممکن ہو تاکہ خودکار عمل کم شاخ بندی کے ساتھ ترجمہ اور جائزہ ورک فلو کے درمیان سوئچ کر سکے۔

| پیرامیٹر | قسم | ڈیفالٹ | مقصد |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | جائزہ لینے کے لیے ہدف زبان کے فولڈرز۔ خالی جگہ سے جدا کردہ سٹرنگز اور تکرار پذیر قبول کیے جاتے ہیں۔ `"all"` ہر دریافت شدہ ترجمہ زبان کا جائزہ لیتا ہے۔ |
| `root_dir` | `str` | `"."` | ایک جائزہ ہدف کے لیے پروجیکٹ روٹ۔ جب `root_dirs` یا `groups` مہیا کیے جائیں تو نظر انداز کیا جاتا ہے۔ |
| `markdown` | `bool` | `False` | Markdown اور MDX سورس فائلز شامل کریں۔ |
| `notebook` | `bool` | `False` | Jupyter نوٹ بک سورس فائلز شامل کریں۔ |
| `images` | `bool` | `False` | ترجمہ کے اختیارات کے ساتھ ہم آہنگی کے لیے مختص۔ Markdown سے تصاویر کے لنک حوالہ جات چیک کیے جاتے ہیں۔ |
| `translations_dir` | `str \| None` | `None` | کسٹم متن ترجمہ آؤٹ پٹ ڈائریکٹری۔ نسبتی راستے ہر روٹ کے حساب سے حل ہوتے ہیں۔ |
| `root_dirs` | `Iterable[str] \| None` | `None` | متعدد روٹس جو ایک ہی آؤٹ پٹ سیٹنگز شیئر کرتے ہیں۔ |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | واضح `(root_dir, translations_dir)` جوڑ۔ `root_dirs` پر فوقیت رکھتا ہے۔ |
| `changed_from` | `str \| None` | `None` | جائزہ کو تبدیل شدہ سورس فائلوں تک محدود کرنے کے لیے استعمال ہونے والا Git ریف۔ |
| `readme_only` | `bool` | `False` | ہر سورس روٹ کے تحت صرف `README.md` کا جائزہ لیں۔ ایک گم شدہ سورس README `ValueError` اٹھاتا ہے۔ |
| `output_format` | `str` | `"text"` | جائزہ آؤٹ پٹ فارمیٹ۔ معاون اقدار `"text"` اور `"github"` ہیں۔ |
| `fail_on_warnings` | `bool` | `False` | تنبیہات کو غلطیوں کے علاوہ ناکامیوں کے طور پر بھی شمار کریں۔ |
| `debug` | `bool` | `False` | ڈیبگ لوگنگ فعال کریں۔ |
| `save_logs` | `bool` | `False` | روٹ `logs/` ڈائریکٹری کے تحت DEBUG سطح کی لاگ فائلیں محفوظ کریں۔ |

اگر `markdown`، `notebook`، یا `images` میں سے کوئی سیٹ نہیں ہے، تو API جہاں لاگو ہو Markdown، نوٹ بکس، اور تصویر کے لنک حوالہ جات کا جائزہ لیتا ہے۔ جائزہ LLM پرووائیڈر کو کال نہیں کرتا اور API keys کی ضرورت نہیں ہوتی۔

## کنفیگریشن کی ضروریات

پرووائیڈر سے وابستہ ترجمہ APIs ترجمہ شروع کرنے سے پہلے پرووائیڈر کنفیگریشن کی ضرورت رکھتے ہیں:

- Markdown اور نوٹ بک کے ترجمے کے لیے LLM پرووائیڈر درکار ہے۔ Azure OpenAI، OpenAI، یا Anthropic کو کنفیگر کریں۔
- تصویر کے ترجمے کے لیے LLM پرووائیڈر کے علاوہ Azure AI Vision درکار ہے۔
- `run_translation` پروجیکٹ کے ترجمے کے آغاز سے پہلے ہلکے وزن کی کنیکٹیویٹی چیکس چلتا ہے۔
- ایجنٹ معاونت یافتہ `start_*_agent_translation` اور `finish_*_agent_translation` APIs Co-op Translator LLM پرووائیڈرز کو کال نہیں کرتے۔ ہوسٹ ایپلیکیشن یا MCP ایجنٹ تیار کردہ چنکس کا ترجمہ کرتا ہے۔
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, اور `run_review` قطعی ہیں اور پرووائیڈر کریڈینشلز کی ضرورت نہیں ہوتی۔

ضروری Azure OpenAI متغیرات:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ضروری OpenAI متغیرات:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

ضروری Anthropic متغیرات:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` اور `ANTHROPIC_MAX_TOKENS` اختیاری ہیں۔ Microsoft Agent Framework تمام پرووائیڈرز کے لیے Co-op Translator 0.22.0 سے بطور ڈیفالٹ ماڈل کلائنٹ ہے۔ Semantic Kernel کو عارضی طور پر `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` کے ساتھ منتخب کیا جا سکتا ہے، لیکن ایسا کرنے پر استعمال ختم ہونے کی وارننگ آتی ہے؛ مرحلہ وار ہٹانے کے منصوبے کے لیے [configuration](configuration.md#model-client-backend) دیکھیں۔

تصویری ترجمے کے لیے ضروری Azure AI Vision متغیرات:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` قطعی (deterministic) ہے اور اسے LLM یا Azure AI Vision کنفیگریشن کی ضرورت نہیں ہوتی۔

## طرزِ عمل کے نوٹس

- مواد کے ترجمے والی APIs ترجمہ کو پروجیکٹ راستہ دوبارہ لکھنے سے الگ رکھتی ہیں۔ جب ترجمہ شدہ مواد کے لیے پروجیکٹ نسبی لنکس کو کسی ہدف مقام کے مطابق ایڈجسٹ کرنے کی ضرورت ہو تو واضح طور پر `rewrite_markdown_paths` یا `rewrite_notebook_paths` کال کریں۔
- پروجیکٹ آرکسٹریشن APIs مواد کے ترجمے کے گرد پروجیکٹ کے رویے شامل کرتی ہیں، جن میں فائل کی دریافت، لکھائی، راستے کی دوبارہ تحریر، میٹاڈیٹا، صفائی، اور اختیاری ڈسکلیمرز شامل ہیں۔
- `run_translation` وہی Rich-بیکڈ رپورٹر استعمال کرتے ہوئے ترقی اور اندازے کے خلاصے پرنٹ کرتا ہے جو CLI استعمال کرتا ہے۔ غیر تعاملی آؤٹ پٹ سادہ متن پر واپس آ جاتا ہے۔
- `dry_run=True` ورچوئل README اپڈیٹس استعمال کرتے ہوئے اندازے کا حساب کرتا ہے، لیکن README یا ترجمہ شدہ فائلیں لکھتا نہیں ہے۔
- `groups` ترتیب وار پروسیس ہوتے ہیں۔ کام شروع ہونے سے پہلے ایک واحد مجموعی اندازہ پرنٹ کیا جاتا ہے۔
- جب تصویر کا ترجمہ منتخب کیا جاتا ہے تو Vision کنفیگریشن کی عدم موجودگی ترجمہ شروع ہونے سے پہلے ایک ایرر اٹھاتی ہے۔
- موجودہ عرفی بنیاد زبان فولڈرز کا پتہ لگایا جاتا ہے اور انہیں رن کے حصے کے طور پر معیاری BCP 47 فولڈر ناموں میں منتقل کیا جا سکتا ہے۔
- `run_review` گم شدہ ترجمہ شدہ فائلوں، گم یا فرسودہ ترجمہ میٹا ڈیٹا، خراب شکل والا Markdown frontmatter/code fences، اور غیر معتبر ترجمہ شدہ نوٹ بک JSON پر ناکام ہوتا ہے۔
- `run_review` مقامی Markdown اور تصویر لنک اہداف کی عدم موجودگی کو بطورِ ڈیفالٹ وارننگز کے طور پر رپورٹ کرتا ہے۔

## داخلی کال پاتھ

API اسی بنیادی نفاذ کو تفویض کرتی ہے جو CLI استعمال کرتا ہے:

ترجمہ:

1. میموری میں ترجمے کے لیے `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, یا `translate_image_content`۔
2. واضح راستے کی بعد از عمل پروسیسنگ کے لیے `co_op_translator.api.translation.rewrite_markdown_paths` یا `rewrite_notebook_paths`۔
3. مکمل پروجیکٹ آرکسٹریشن کے لیے `co_op_translator.api.translation.run_translation`۔
4. `co_op_translator.config.Config`, `LLMConfig`, اور `VisionConfig`۔
5. `co_op_translator.core.project.ProjectTranslator`۔
6. `co_op_translator.core.project.TranslationManager`۔
7. Markdown، نوٹ بکس، اور تصاویر کے لیے مرکوز پروجیکٹ ترجمہ میکسنز۔
8. `co_op_translator.core` کے تحت Markdown، نوٹ بک، متن، اور تصویر کے مترجم۔

جائزہ:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` کے تحت قطعی چیکس

ذیل کی کلاسیں مینٹینرز کے لیے مفید ہیں، لیکن پیکیج-سطح کے مستحکم API کے طور پر ایکسپورٹ نہیں کی جاتیں۔

| کلاس | ماڈیول | ذمہ داری |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | پروجیکٹ سطح پر ترجمہ، ڈائریکٹری مینیجمنٹ، فی زبان میٹاڈیٹا کی معمول سازی، اور Markdown، نوٹ بک، اور تصویر کے مترجمین کو تفویض کرتا ہے۔ |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown، نوٹ بکس، تصاویر، فرسودہ شناخت، اور ترجمے کے میٹاڈیٹا اپڈیٹس کے لیے async فائل پروسیسنگ کا کام انجام دیتا ہے۔ |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown فائل ریڈز، مواد کا ترجمہ، راستے کی دوبارہ تحریر، میٹاڈیٹا، ڈسکلیمرز، اور لکھنے کا بندوبست کرتا ہے۔ |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | نوٹ بک فائل ریڈز، Markdown-cell کا ترجمہ، راستے کی دوبارہ تحریر، میٹاڈیٹا، ڈسکلیمرز، اور لکھنے کا بندوبست کرتا ہے۔ |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | ماخذ تصاویر کی دریافت، تصویر کا ترجمہ، آؤٹ پٹ راستے، میٹاڈیٹا، اور لکھنے کا بندوبست کرتا ہے۔ |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | ترجمہ شدہ Markdown جوڑوں کو تلاش کرتا ہے، ترجمے کے معیار کا جائزہ لیتا ہے، اور کم اعتماد مرمت ورک فلو کے لیے اعتماد میٹاڈیٹا پڑھتا ہے۔ |
| `ReviewRunner` | `co_op_translator.review.runner` | ماخذ فائلوں، ہدف زبانوں، اور کنفیگر کردہ ترجمہ روٹس کے درمیان قطعی جائزہ چیکس کو ہم آہنگ کرتا ہے۔ |
| `ReviewTarget` | `co_op_translator.review.targets` | ایک سورس روٹ اور اس روٹ کے لیے جائزہ لیے جانے والے ترجمہ آؤٹ پٹ ڈائریکٹری کی وضاحت کرتا ہے۔ |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | ورثے میں موجود عرفی زبان فولڈرز کا پتہ لگاتا ہے اور معیاری BCP 47 فولڈر مائیگریشن منصوبے تیار کرتا ہے۔ |
| `Config` | `co_op_translator.config.base_config` | `.env` فائلیں لوڈ کرتا ہے اور چیک کرتا ہے کہ آیا ضروری LLM اور اختیاری Vision پرووائیڈرز کنفیگر ہیں۔ |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI، OpenAI، یا Anthropic کو خودکار طور پر شناخت کرتا ہے، ضروری ماحولیاتی متغیرات کی توثیق کرتا ہے، اور پرووائیڈر کنیکٹیویٹی چیکس چلائے۔ |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision کنفیگریشن کا پتہ لگاتا ہے اور تصویری ترجمے کے لیے کنیکٹیویٹی چیکس چلائے۔ |