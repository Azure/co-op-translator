# Python API

The stable public Python API is exported from `co_op_translator.api`. Most integrations use one of these workflows:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | آپ کی ایپلیکیشن سورس مواد پڑھتی ہے، ترجمے کے لیے Co-op Translator کو کال کرتی ہے، اور نتیجہ کہاں محفوظ کرنا ہے فیصلہ کرتی ہے۔ | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | آپ کا MCP میزبان یا ایپ ماڈل چنکس کا ترجمہ کرے گا، جبکہ Co-op Translator چنکنگ اور دوبارہ تعمیر سنبھالتا ہے۔ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | آپ چاہتے ہیں کہ Python API CLI کی طرح کام کرے اور دریافت، آؤٹ پٹ راستے، میٹا ڈیٹا، کلین اپ، اور رائٹس سنبھالے۔ | `run_translation` |

Most lower-level modules under `core`, `config`, `review`, and `utils` are implementation details used by these API entry points.

MCP کلائنٹس وہی پبلک API [MCP Server](mcp.md) کے ذریعے استعمال کرتے ہیں۔ جب آپ براہِ راست Python سے کال کر رہے ہوں تو اس صفحے کو استعمال کریں، اور جب Co-op Translator کو کسی ایجنٹ یا ایڈیٹر کے لیے ظاہر کر رہے ہوں تو MCP گائیڈ دیکھیں۔ اگر آپ CLI، Python API، اور MCP کے درمیان فیصلہ کر رہے ہیں تو [Choose Your Workflow](workflows.md) سے شروع کریں۔

## First-Time API Flow

اگر آپ Python کوڈ سے Co-op Translator کال کر رہے ہیں تو یہاں سے شروع کریں:

1. [Configuration](configuration.md) میں بیان کردہ مطابق ایک LLM فراہم کنندہ کنفیگر کریں، جب تک کہ آپ صرف Markdown یا نوٹ بک چنکس کو میزبان-ایجنٹ ترجمے کے لیے تیار نہیں کر رہے۔
2. فیصلہ کریں کہ آیا آپ کی ایپلیکیشن فائل I/O کی ذمہ دار ہے۔
3. جب آپ کی ایپلیکیشن انفرادی فائلیں پڑھتی اور لکھتی ہے تو content APIs استعمال کریں۔
4. جب Co-op Translator کو CLI کی طرح ایک repository پروسیس کرنا ہو تو `run_translation` استعمال کریں۔
5. اگر آپ کو آٹومیشن میں Deterministic چیکس درکار ہوں تو ترجمے کے بعد `run_review` استعمال کریں۔

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` یا `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` یا `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenario 1: Translate Individual Files or Documents

اس ورک فلو کو استعمال کریں جب آپ کے پاس پہلے سے ایک فائل، ایڈیٹر بفر، نوٹ بک پیلوڈ، MCP ریکویسٹ، یا کسٹم پائپ لائن ان پٹ موجود ہو۔ آپ کے کوڈ کے زیرِ اہتمام فائل I/O ہے:

1. ماخذ مواد پڑھیں۔
2. content translation API کو کال کریں۔
3. اگر ترجمہ شدہ مواد کسی پروجیکٹ ٹرانسلیشن فولڈر میں لکھا جانے والا ہے تو اختیاری طور پر path rewriting API کو کال کریں۔
4. نتیجہ اپنی ایپلیکیشن میں محفوظ کریں یا واپس کریں۔

Content translation APIs پروجیکٹ دریافت نہیں چلاتے، میٹا ڈیٹا نہیں لکھتے، ڈسکلیمرز شامل نہیں کرتے، اور لنکس خودکار طور پر دوبارہ نہیں لکھتے۔

### Markdown File

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

اگر ترجمہ شدہ Markdown Co-op Translator پروجیکٹ لے آؤٹ میں نہیں رہے گا تو `rewrite_markdown_paths` کو چھوڑ دیں اور ترجمہ شدہ سٹرنگ کو براہِ راست محفوظ کریں۔

### Notebook File

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

`translate_notebook_content` Markdown سیلز کا ترجمہ کرتا ہے اور non-Markdown سیلز کو برقرار رکھتا ہے۔ path rewriting صرف Markdown سیلز پر لاگو ہوتی ہے۔

### Image File

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

`translate_image_content` سورس امیج پڑھتا ہے اور ایک رینڈر کردہ `PIL.Image.Image` واپس کرتا ہے۔ یہ ترجمہ شدہ امیج میٹا ڈیٹا نہیں لکھتا۔

## Scenario 2: Translate an Entire Repository

اس ورک فلو کو استعمال کریں جب آپ چاہتے ہیں کہ Python API `translate` CLI کی طرح برتاؤ کرے۔ `run_translation` سپورٹ شدہ فائلوں کو دریافت کرتا ہے، منتخب مواد کی اقسام کا ترجمہ کرتا ہے، راستے دوبارہ لکھتا ہے، آؤٹ پٹ فائلیں لکھتا ہے، میٹا ڈیٹا اپڈیٹ کرتا ہے، اور صفائی جیسے مینٹیننس ٹاسکس انجام دیتا ہے۔

`run_translation` پسندیدہ پروجیکٹ آرکیسٹریشن انٹری پوائنٹ ہے۔ `translate_project` اسی رویے کے ساتھ مطابقتی عرف کے طور پر برآمد کیا جاتا ہے۔

موجودہ repository میں Markdown فائلوں کو Korean اور Japanese میں ترجمہ کریں:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

کسی مخصوص پروجیکٹ روٹ سے صرف نوٹ بکس کا ترجمہ کریں:

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

ایک کال میں متعدد مواد کے روٹس کا ترجمہ کریں:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

ترجمے کو واضح آؤٹ پٹ گروپس میں لکھیں:

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

جب ہر زبان میں نیسٹڈ سب ڈائریکٹری ہونی چاہیے تو فی زبان ایک پلِیس ہولڈر استعمال کریں:

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

اگر `markdown`, `notebook`, یا `images` میں سے کوئی بھی سیٹ نہیں ہے، تو API تمام سپورٹ شدہ اقسام کا ترجمہ کرے گا: Markdown، نوٹ بکس، اور تصاویر۔

## Review Translated Output

`run_review` deterministic ترجمہ چیکس بغیر LLM یا Vision کریڈینشلز کے چلتا ہے۔

!!! note "بیटा"
    `run_review` ایک بیٹا deterministic review API ہے۔ یہ ماڈل فراہم کنندگان کو کال نہیں کرتا اور فائلیں نہیں لکھتا، مگر چیکس اور ایشو اسکیمز تبدیل ہو سکتی ہیں۔

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

صرف وہ فائلیں ریویو کریں جو base ref کے خلاف تبدیل ہوئی ہوں اور GitHub-flavored آؤٹ پُٹ پر پرنٹ کریں:

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

## Copy-Paste API Examples

فائل رائٹس کے بغیر Markdown مواد کا ترجمہ کریں:

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

Markdown لنکس کا ترجمہ اور دوبارہ لکھیں:

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

Python سے ایک repository کا ترجمہ کریں:

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

گلاسری اصطلاحات برقرار رکھیں:

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

## Public Entry Points

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

## Content Translation APIs

Content translation APIs ان انٹیگریشنز کے لیے ہیں جن کے پاس پہلے سے ہی مواد میموری میں موجود ہو، جیسے کہ ایک ایڈیٹر ایکسٹینشن، MCP ٹول، نوٹ بک پروسیسر، یا کسٹم پائپ لائن۔

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async۔ صرف Markdown مواد کا ترجمہ کرتا ہے۔ یہ لنکس دوبارہ نہیں لکھتا، میٹا ڈیٹا نہیں لکھتا، اور ڈسکلیمرز شامل نہیں کرتا۔ |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async۔ Markdown سیلز کا ترجمہ کرتا ہے اور non-Markdown سیلز کو برقرار رکھتا ہے۔ یہ لنکس دوبارہ نہیں لکھتا، میٹا ڈیٹا نہیں لکھتا، اور ڈسکلیمرز شامل نہیں کرتا۔ |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous۔ امیج سے متن نکالتا اور ترجمہ کرتا ہے، پھر ایک رینڈر شدہ امیج واپس کرتا ہے۔ یہ ترجمہ شدہ امیج میٹا ڈیٹا محفوظ نہیں کرتا۔ |

`translate_markdown_content` اور `translate_notebook_content` اپنے اختیارات کے ذریعے ایک اختیاری `source_path` قبول کرتے ہیں۔ یہ راستہ مترجم کو کونٹیکسٹ کے طور پر پاس کیا جاتا ہے؛ کالرز ترجمے کے بعد کسی بھی پروجیکٹ مخصوص path rewriting کے ذمے دار رہتے ہیں۔

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

وہی اختیارات ڈکشنریز کے طور پر بھی پاس کیے جا سکتے ہیں:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Agent-assisted APIs Co-op Translator سے Azure OpenAI یا OpenAI کو کال نہیں کرتے۔ یہ Markdown یا نوٹ بک چنکس کو میزبان ایجنٹ کے ترجمے کے لیے تیار کرتے ہیں، پھر میزبان ایجنٹ کے ترجمہ شدہ چنکس سے حتمی مواد دوبارہ تشکیل دیتے ہیں۔

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | چنکس، پرامپٹس، اور reconstruction state کے ساتھ ایک self-contained Markdown جاب واپس کریں۔ |
| `finish_markdown_agent_translation` | ایک جاب اور میزبان-ایجنٹ کے ترجمہ شدہ چنکس سے Markdown کو دوبارہ تعمیر کریں۔ |
| `start_notebook_agent_translation` | میزبان-ایجنٹ ترجمے کے لیے Markdown-cell چنکس کے ساتھ ایک نوٹ بک جاب واپس کریں۔ |
| `finish_notebook_agent_translation` | کوڈ سیلز، آؤٹ پٹس، اور میٹا ڈیٹا کو برقرار رکھتے ہوئے نوٹ بک JSON کو دوبارہ تعمیر کریں۔ |

یہ ورک فلو بنیادی طور پر MCP میزبانوں کے لیے مقصود ہے۔ اگر آپ پروڈکشن repository ترجمہ چاہتے ہیں جس میں Co-op Translator فراہم کنندہ کالز کو مینیج کرے، تو `translate_markdown_content`, `translate_notebook_content`, یا `run_translation` استعمال کریں۔

## Path Rewriting APIs

Path rewriting APIs کوئی ترجمہ نہیں کرتے۔ وہ کالرز کو معلوم سورس راستہ، ترجمہ شدہ ٹارگٹ راستہ، اور پروجیکٹ لے آؤٹ کے بعد لنکس اور frontmatter راستوں کو اپڈیٹ کرتے ہیں۔

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | ترجمہ شدہ ٹارگٹ کے لیے Markdown لنکس اور سپورٹ شدہ frontmatter path فیلڈز کو دوبارہ لکھتا ہے۔ |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | ہر Markdown سیل پر Markdown path rewriting لاگو کرتا ہے اور non-Markdown سیلز کو بغیر بدلے چھوڑ دیتا ہے۔ |

`policy` آرگومینٹ ایک ڈکشنری ہو سکتی ہے جس میں یہ فیلڈز شامل ہوں:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | ہدف زبان کا کوڈ، جیسے `"ko"` یا `"pt-BR"`۔ |
| `root_dir` | No | سورس پروجیکٹ روٹ۔ ڈیفالٹ `"."` ہے۔ |
| `translations_dir` | No | ٹیکسٹ ترجمہ آؤٹ پٹ ڈائریکٹری۔ ڈیفالٹ `root_dir` کے تحت `translations` ہے۔ |
| `translated_images_dir` | No | ترجمہ شدہ امیج آؤٹ پٹ ڈائریکٹری۔ ڈیفالٹ `root_dir` کے تحت `translated_images` ہے۔ |
| `translation_types` | No | فعال شدہ ترجمہ اقسام۔ ڈیفالٹ Markdown، نوٹ بکس، اور تصاویر ہیں۔ |
| `lang_subdir` | No | ہر زبان کے فولڈر کے تحت اختیاری سب ڈائریکٹری۔ |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | اسپیس سے جدا ہدف زبان کوڈز، جیسے `"ko ja fr"`، یا `"all"`۔ علیاسات کو canonical BCP 47 اقدار میں نارملائز کیا جاتا ہے۔ |
| `root_dir` | `str` | `"."` | ایک واحد ترجمہ ہدف کے لیے پروجیکٹ روٹ۔ جب `root_dirs` یا `groups` فراہم کیے جائیں تو نظر انداز کیا جاتا ہے۔ |
| `update` | `bool` | `False` | منتخب زبانوں کے لیے موجودہ ترجموں کو حذف اور دوبارہ بنائیں۔ |
| `images` | `bool` | `False` | امیج ترجمہ شامل کریں۔ Azure AI Vision کنفیگریشن درکار ہے۔ |
| `markdown` | `bool` | `False` | Markdown ترجمہ شامل کریں۔ |
| `notebook` | `bool` | `False` | Jupyter نوٹ بک ترجمہ شامل کریں۔ |
| `debug` | `bool` | `False` | ڈیبگ لاگنگ فعال کریں۔ |
| `save_logs` | `bool` | `False` | روٹ `logs/` ڈائریکٹری کے تحت DEBUG سطح کے لاگ فائلز محفوظ کریں۔ |
| `yes` | `bool` | `True` | پروگرامیٹک اور CI استعمال کے لیے پرامپٹس کو خود کار طور پر کنفرم کریں۔ |
| `add_disclaimer` | `bool` | `False` | ترجمہ شدہ Markdown اور نوٹ بکس میں مشین ترجمہ ڈسکلیمرز شامل کریں۔ |
| `translations_dir` | `str \| None` | `None` | کسٹم ٹیکسٹ ترجمہ آؤٹ پٹ ڈائریکٹری۔ نسبتی راستے ہر روٹ کے خلاف resolve ہوتے ہیں۔ |
| `image_dir` | `str \| None` | `None` | کسٹم ترجمہ شدہ امیج آؤٹ پٹ ڈائریکٹری۔ نسبتی راستے ہر روٹ کے خلاف resolve ہوتے ہیں۔ |
| `root_dirs` | `Iterable[str] \| None` | `None` | متعدد روٹس جو ایک ہی آؤٹ پٹ سیٹنگز شیئر کرتے ہیں۔ |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | واضح `(root_dir, translations_dir)` جوڑی۔ `root_dirs` پر فوقیت رکھتا ہے۔ |
| `repo_url` | `str \| None` | `None` | README زبان ٹیبل گائیڈینس رینڈر کرتے وقت استعمال ہونے والا repository URL۔ |
| `glossaries` | `Iterable[str] \| None` | `None` | ترجمے کے دوران برقرار رکھنے کے لیے گلاسری اصطلاحات۔ ڈپلیکٹس اور خالی اصطلاحات نارملائز کی جاتی ہیں۔ |
| `dry_run` | `bool` | `False` | ترجمے کا حجم اندازہ کریں اور فائلیں لکھے بغیر مائیگریشن کے برتاؤ کا پیش نظارہ کریں۔ |

## Review Parameters

`run_review` جان بوجھ کر `run_translation` دستخط کی عکاسی کرتا ہے جہاں ممکن ہو تاکہ آٹومیشن کم برانچنگ کے ساتھ ترجمہ اور ریویو ورک فلو کے درمیان سوئچ کر سکے۔

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | ریویو کے لیے ہدف زبان فولڈرز۔ اسپیس سے جدا سٹرنگز اور iterable دونوں قبول کیے جاتے ہیں۔ `"all"` ہر دریافت شدہ ترجمہ زبان کو ریویو کرتا ہے۔ |
| `root_dir` | `str` | `"."` | ایک واحد ریویو ہدف کے لیے پروجیکٹ روٹ۔ جب `root_dirs` یا `groups` فراہم کیے جائیں تو نظر انداز کیا جاتا ہے۔ |
| `markdown` | `bool` | `False` | Markdown اور MDX سورس فائلز شامل کریں۔ |
| `notebook` | `bool` | `False` | Jupyter نوٹ بک سورس فائلز شامل کریں۔ |
| `images` | `bool` | `False` | ترجمہ کے آپشنز کے ساتھ ہم آہنگی کے لیے مخصوص۔ امیج کے حوالے والے لنک Markdown سے چیک کیے جاتے ہیں۔ |
‏| `translations_dir` | `str \| None` | `None` | کسٹم متن ترجمے کی آؤٹ پٹ ڈائریکٹری۔ نسبتی راستے ہر روٹ کے نسبت سے حل کیے جاتے ہیں۔ |
| `root_dirs` | `Iterable[str] \| None` | `None` | متعدد روٹس جو ایک ہی آؤٹ پٹ سیٹنگز شیئر کرتے ہیں۔ |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | واضح `(root_dir, translations_dir)` جوڑے۔ `root_dirs` پر فوقیت رکھتے ہیں۔ |
| `changed_from` | `str \| None` | `None` | Git ریف جو جائزہ کو تبدیل شدہ سورس فائلوں تک محدود کرنے کے لیے استعمال ہوتا ہے۔ |
| `output_format` | `str` | `"text"` | جائزے کا آؤٹ پٹ فارمیٹ۔ مدد شدہ مقداریں ہیں `"text"` اور `"github"`۔ |
| `fail_on_warnings` | `bool` | `False` | وارننگز کو غلطیوں کے ساتھ ساتھ ناکامیاں سمجھیں۔ |
| `debug` | `bool` | `False` | ڈی بگ لاگنگ کو فعال کریں۔ |
| `save_logs` | `bool` | `False` | DEBUG سطح کی لاگ فائلیں روٹ `logs/` ڈائریکٹری کے تحت محفوظ کریں۔ |

اگر `markdown`, `notebook`, یا `images` میں سے کوئی سیٹ نہیں ہے، تو API جہاں موزوں ہو Markdown، نوٹ بکس، اور امیج لنک حوالہ جات کا جائزہ لیتا ہے۔ یہ جائزہ کسی LLM فراہم کنندہ کو کال نہیں کرتا اور API Keys کی ضرورت نہیں ہوتی۔

## کنفیگریشن کی ضروریات

فراہم کنندہ پر مبنی ترجمہ APIs کو ترجمہ کرنے سے پہلے فراہم کنندہ کی کنفیگریشن درکار ہوتی ہے:

- Markdown اور نوٹ بک ترجمہ کے لیے ایک LLM فراہم کنندہ درکار ہوتا ہے۔ یا تو Azure OpenAI یا OpenAI کو کنفیگر کریں۔
- امیج ترجمہ کے لیے LLM فراہم کنندہ کے علاوہ Azure AI Vision درکار ہوتا ہے۔
- `run_translation` پروجیکٹ ترجمہ شروع ہونے سے پہلے ہلکے کنیکٹیویٹی چیکس چلائے گا۔
- ایجنٹ معاون `start_*_agent_translation` اور `finish_*_agent_translation` APIs Co-op Translator LLM فراہم کنندگان کو کال نہیں کرتی ہیں۔ ہوسٹ ایپلیکیشن یا MCP ایجنٹ تیار کیے گئے چنکس کا ترجمہ کرتی ہے۔
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, اور `run_review` متعین (deterministic) ہیں اور فراہم کنندہ کے کریڈینشلز کی ضرورت نہیں ہوتی۔

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

`run_review` متعین ہے اور Azure OpenAI، OpenAI، یا Azure AI Vision کنفیگریشن کی ضرورت نہیں رکھتا۔

## طرز عمل کے نوٹس

- مواد کے ترجمہ APIs ترجمہ کو پروجیکٹ راستہ دوبارہ لکھنے سے الگ رکھتی ہیں۔ جب ترجمہ شدہ مواد کے پروجیکٹ-نسبتی لنکس کو ہدف مقام کے لیے ایڈجسٹ کرنے کی ضرورت ہو تو واضح طور پر `rewrite_markdown_paths` یا `rewrite_notebook_paths` کو کال کریں۔
- پروجیکٹ اورکسٹریشن APIs مواد کے ترجمہ کے ارد گرد پروجیکٹ کا رویّہ شامل کرتی ہیں، بشمول فائل کی دریافت، لکھنا، راستہ دوبارہ لکھنا، میٹاڈیٹا، صفائی، اور اختیاری ڈس کلیمرز۔
- `run_translation` Click کے ذریعے پیش رفت اور اندازے کے خلاصے پرنٹ کرتا ہے، CLI صارف کے تجربے سے میل کھاتا ہے۔
- `dry_run=True` فرضی README اپڈیٹس استعمال کرکے تخمینے نکالتا ہے، لیکن README یا ترجمہ فائلیں نہیں لکھتا۔
- `groups` کو متسلسل طور پر پروسیس کیا جاتا ہے۔ کام شروع ہونے سے پہلے ایک واحد مجموعی اندازہ پرنٹ کیا جاتا ہے۔
- جب امیج ترجمہ منتخب کیا جائے تو Vision کنفیگریشن کی عدم موجودگی ترجمہ شروع ہونے سے پہلے ایک ایرر اٹھاتی ہے۔
- موجودہ علیاس-بنیاد زبان کے فولڈرز کا پتہ چلتا ہے اور انہیں رن کے حصے کے طور پر معیاری زبان کے فولڈر ناموں میں منتقل کیا جا سکتا ہے۔
- `run_review` ترجمہ شدہ فائلوں کی عدم موجودگی، ترجمہ میٹاڈیٹا کی عدم موجودگی یا پرانی حالت، بگڑی ہوئی Markdown frontmatter/code fences، اور غلط ترجمہ شدہ نوٹ بک JSON پر ناکام ہوتا ہے۔
- `run_review` مقامی Markdown اور امیج لنک ٹارگٹس کی عدم موجودگی کو بطور ڈیفالٹ وارننگز کے طور پر رپورٹ کرتا ہے۔

## اندرونی کال پاتھ

API وہی بنیادی امپلیمینٹیشن استعمال کرتی ہے جسے CLI استعمال کرتی ہے:

ترجمہ:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` میموری میں ترجمے کے لیے۔
2. `co_op_translator.api.translation.rewrite_markdown_paths` یا `rewrite_notebook_paths` واضح راستے کی پوسٹ-پروسیسنگ کے لیے۔
3. `co_op_translator.api.translation.run_translation` مکمل پروجیکٹ اورکسٹریشن کے لیے۔
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown، نوٹ بکس، اور تصاویر کے لیے فوکسڈ پروجیکٹ ٹرانسلیشن مکسنز۔
8. Markdown، نوٹ بک، ٹیکسٹ، اور امیج ٹرانسلیٹرز `co_op_translator.core` کے تحت۔

جائزہ:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. متعین چیکس `co_op_translator.review.checks` کے تحت

مندرجہ ذیل کلاسیں دیکھ بھال کرنے والوں کے لیے مفید ہیں، لیکن پیکیج لیول کی مستحکم API کے طور پر برآمد نہیں کی جاتیں۔

| کلاس | ماڈیول | ذمہ داری |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | پروجیکٹ سطح کے ترجمہ، ڈائریکٹری مینجمنٹ، فی زبان میٹاڈیٹا نارملائزیشن، اور Markdown، نوٹ بک، اور امیج ٹرانسلیٹرز کے لیے تفویض کو مربوط کرتا ہے۔ |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown، نوٹ بکس، تصاویر، پرانی حالت کی تلاش، اور ترجمہ میٹاڈیٹا اپڈیٹس کے لیے غیر متزامن فائل پروسیسنگ کا کام انجام دیتا ہے۔ |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown فائلوں کی ریڈنگ، مواد کا ترجمہ، راستہ دوبارہ لکھنا، میٹاڈیٹا، ڈس کلیمرز، اور رائٹس کو مربوط کرتا ہے۔ |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | نوٹ بک فائلوں کی ریڈنگ، Markdown-سیل کا ترجمہ، راستہ دوبارہ لکھنا، میٹاڈیٹا، ڈس کلیمرز، اور رائٹس کو مربوط کرتا ہے۔ |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | ماخذ امیج کی دریافت، امیج ترجمہ، آؤٹ پٹ راستے، میٹاڈیٹا، اور رائٹس کو مربوط کرتا ہے۔ |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | ترجمہ شدہ Markdown جوڑوں کا پتہ لگاتا ہے، ترجمے کے معیار کا اندازہ کرتا ہے، اور کم اعتماد ریپئر ورک فلو کے لیے اعتماد میٹاڈیٹا پڑھتا ہے۔ |
| `ReviewRunner` | `co_op_translator.review.runner` | سورس فائلوں، ہدف زبانوں، اور کنفیگر کیے گئے ترجمہ روٹس میں متعین ریویو چیکس کو مربوط کرتا ہے۔ |
| `ReviewTarget` | `co_op_translator.review.targets` | ایک سورس روٹ اور اس روٹ کے لیے جائزہ لیے گئے ترجمہ آؤٹ پٹ ڈائریکٹری کو بیان کرتا ہے۔ |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | قدیم علیاس زبان کے فولڈرز کا پتہ لگاتا ہے اور معیاری BCP 47 فولڈر مائگریشن منصوبے تیار کرتا ہے۔ |
| `Config` | `co_op_translator.config.base_config` | `.env` فائلیں لوڈ کرتا ہے اور چیک کرتا ہے کہ درکار LLM اور اختیاری Vision فراہم کنندگان کنفیگر ہیں یا نہیں۔ |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI یا OpenAI کو خود بخود شناخت کرتا ہے، درکار ماحول کے متغیرات کی صحت کی جانچ کرتا ہے، اور فراہم کنندہ کنیکٹیویٹی چیکس چلاتا ہے۔ |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision کنفیگریشن کا پتہ لگاتا ہے اور امیج ترجمہ کے لیے کنیکٹیویٹی چیکس چلاتا ہے۔ |