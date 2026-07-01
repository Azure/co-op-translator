# اپنا ورک فلو منتخب کریں

Co-op Translator کو تین طریقوں سے استعمال کیا جا سکتا ہے: CLI، Python API، اور MCP سرور۔ ان میں ترجمے کی صلاحیتیں ایک جیسی ہیں، مگر ہر ایک مختلف ورک فلو کے لیے مناسب ہے۔

جب آپ فیصلہ کر رہے ہوں کہ کہاں سے شروع کریں تو اس صفحے کا استعمال کریں۔

## فوری فیصلہ

| If you want to... | Use | Start here |
| --- | --- | --- |
| Translate or review a repository from a terminal | CLI | [CLI حوالہ](cli.md) |
| Add translation to a Python script, service, notebook, or CI job | Python API | [Python API](api.md) |
| Let an agent, editor, or MCP-compatible client translate content for you | MCP Server | [MCP Server](mcp.md) |
| Translate one Markdown document, notebook, or image that your app already loaded | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Translate an entire repository with standard output folders and metadata | CLI or `run_translation` | [CLI حوالہ](cli.md) or [Python API](api.md) |

## CLI استعمال کریں جب

CLI منتخب کریں جب کوئی شخص یا CI جاب شیل سے repository کا ترجمہ چلا رہی ہو۔

جب آپ چاہتے ہیں کہ Co-op Translator پروجیکٹ فائلیں دریافت کرے، ترجمہ شدہ آؤٹ پٹس بنائے، پروجیکٹ کی ترتیب کو برقرار رکھے، میٹا ڈیٹا اپڈیٹ کرے، اور ریویو کمانڈز چلائے تو CLI سب سے براہِ راست راستہ ہے۔

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

مناسب حالات:

- آپ ٹرمینل سے کسی repository کا ترجمہ کر رہے ہیں۔
- آپ CI یا ریلیز ورک فلو کے لیے ایک بار بار چلنے والی کمانڈ چاہتے ہیں۔
- آپ بلٹ ان پروجیکٹ دریافت، آؤٹ پٹ راستے، میٹا ڈیٹا، صفائی، اور ریویو چاہتے ہیں۔
- آپ Python کوڈ لکھنے کے بجائے کمانڈ انٹرفیس کو ترجیح دیتے ہیں۔

## Python API استعمال کریں جب

Python API منتخب کریں جب آپ کا اپنا کوڈ ورک فلو کو کنٹرول کرے۔

API ایپلیکیشنز، آٹومیشن اسکرپٹس، نوٹ بکس، سروسز، اور کسٹم پائپ لائنز کے لیے مفید ہے۔ یہ آپ کو انفرادی فائلوں کے لیے کم سطح کے مواد ترجمہ API کال کرنے دیتا ہے، یا وہی repository-سطح کا آرکسٹریشن چلانے دیتا ہے جو CLI استعمال کرتا ہے۔

ایک Markdown دستاویز کا ترجمہ کریں اور فیصلہ کریں کہ اسے کہاں محفوظ کرنا ہے:

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

Python سے repository ترجمہ چلائیں:

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

مناسب حالات:

- آپ کی ایپلیکیشن پہلے ہی فائلیں، بفرز، نوٹ بکس، یا image bytes پڑھ رہی ہے۔
- آپ کو کسٹم ویلیڈیشن، اسٹوریج، لاگنگ، ریٹرائیز، یا منظوری کے فلو کی ضرورت ہے۔
- آپ ایک دستاویز، نوٹ بک، یا تصویر کا ترجمہ کرنا چاہتے ہیں بغیر پورے repository کو پروسیس کیے۔
- آپ repository ترجمہ چاہتے ہیں، مگر شیل کمانڈ کے بجائے Python آٹومیشن سے۔

## MCP سرور استعمال کریں جب

MCP سرور منتخب کریں جب کسی ایجنٹ، ایڈیٹر، یا MCP-مطابق کلائنٹ کو Co-op Translator ٹولز کال کرنے چاہئیں۔

عام لوکل سیٹ اپ میں، صارف دستی طور پر سرور کو چلائے نہیں رکھتا۔ جب ضرورت ہو تو MCP کلائنٹ `co-op-translator-mcp` کو `stdio` پر شروع کرتا ہے۔

ایجنٹ سنبھال سکتا ہے ایسی صارف کی درخواستوں کی مثالیں:

- "اس Markdown فائل کا ترجمہ کوریائی میں کریں اور لنکس درست رکھیں۔"
- "اس Markdown فائل کا ترجمہ کوریائی کریں ایجنٹ-مدد یافتہ MCP ورک فلو کے ساتھ، آپ ماڈل کو ترجمہ شدہ چنکس کے لیے استعمال کریں۔"
- "اس نوٹ بک کو کوریائی میں ترجمہ کریں، کوڈ سیلز کو برقرار رکھیں، اور نوٹ بک کو دوبارہ تعمیر کرنے کے لیے Co-op Translator MCP استعمال کریں۔"
- "اس تصویر کے متن کو جاپانی میں ترجمہ کریں اور نتیجہ محفوظ کریں۔"
- "ایک repository ترجمہ dry-run کریں ہسپانوی میں اور بتائیں کہ کون سی تبدیلیاں ہوں گی۔"
- "جائزہ لیں کہ کوریائی ترجمہ آؤٹ پٹ اپ ٹو ڈیٹ ہے یا نہیں۔"

Markdown اور نوٹ بکس کے لیے، MCP دو طریقوں سے کام کر سکتا ہے:

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-assisted | جب MCP ہوسٹ ایجنٹ کو اپنے ماڈل کے ساتھ چنکس ترجمہ کرنے چاہئیں، بغیر Co-op Translator LLM فراہم کنندہ کی اسناد کے۔ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | جب Co-op Translator کو براہِ راست Azure OpenAI یا OpenAI کال کرنا چاہیے۔ | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown tool call shape:

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

MCP image tool call shape:

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

Repository translation بذاتِ خود MCP کے ذریعے ڈیفالٹ طور پر dry-run ہوتی ہے:

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

مناسب حالات:

- آپ ایجنٹ یا ایڈیٹر کے اندر نیچرل-لینگویج ترجمہ ورک فلو چاہتے ہیں۔
- آپ وہ Markdown یا نوٹ بک ترجمہ چاہتے ہیں جہاں ہوسٹ ایجنٹ تیار کیے گئے چنکس کا ترجمہ کرے۔
- آپ چاہتے ہیں کہ ایجنٹ منتخب شدہ مواد کا ترجمہ کرے بجائے پورے repository کے۔
- آپ چاہتے ہیں کہ repository-وسیع لکھائی سے پہلے ایک منظوری مرحلہ ہو۔
- آپ ایک ایسا انٹرفیس چاہتے ہیں جو Markdown، نوٹ بک، تصویر، ریویو، اور path-rewriting ٹولز سب کو ایک جگہ پیش کرے۔

## یہ ایک ساتھ کیسے کام کرتے ہیں

CLI انسانوں کے لیے repositories کے ترجمے کے لیے بہترین ڈیفالٹ ہے۔ Python API بہترین ہے جب آپ کے کوڈ کے پاس ورک فلو کی ملکیت ہو۔ MCP سرور بہترین ہے جب ایجنٹ یا ایڈیٹر ورک فلو کی ملکیت رکھتا ہو۔

یہ تینوں راستے ایک ہی عوامی Co-op Translator API استعمال کرتے ہیں، لہٰذا آپ CLI سے شروع کر سکتے ہیں، بعد میں Python کے ساتھ خودکار کر سکتے ہیں، اور جب آپ کو ایجنٹ-متعلق ورک فلو کی ضرورت ہو تو ویسی ہی صلاحیتیں MCP کلائنٹس کو فراہم کر سکتے ہیں۔