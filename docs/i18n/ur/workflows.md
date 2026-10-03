# اپنا ورک فلو منتخب کریں

Co-op Translator کو تین طریقوں سے استعمال کیا جا سکتا ہے: CLI، Python API، اور MCP سرور۔ ان کے ترجمے کی صلاحیتیں ایک جیسی ہیں، لیکن ہر ایک مختلف ورک فلو کے لیے موزوں ہے۔

جب آپ یہ فیصلہ کر رہے ہوں کہ کہاں سے شروع کریں تو اس صفحے کا استعمال کریں۔

**اگر آپ ترجمے دستی طور پر ایڈٹ کرتے ہیں:** ڈیفالٹ CLI اور Actions ورک فلو تبدیل شدہ سورس فائلوں کو مکمل طور پر دوبارہ ترجمہ کرتے ہیں، اس لیے ان فائلوں میں آپ کا لکھا ہوا متن اوور رائٹ ہو سکتا ہے۔ اپ ڈیٹ قبول کرنے سے پہلے diff کا جائزہ لیں۔ قبول شدہ ایڈیٹس کے لیے Markdown بلاک-سطح کی حفاظت کے لیے، اختیاری [Python API ترجمہ اسٹیٹ پرووائیڈر](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) استعمال کریں۔

## فوری فیصلہ

| اگر آپ چاہتے ہیں کہ... | استعمال کریں | یہاں سے شروع کریں |
| --- | --- | --- |
| ریپوزیٹری کو ٹرمینل سے ترجمہ یا جائزہ لیں | CLI | [CLI حوالہ](cli.md) |
| ترجمہ کو کسی Python اسکرپٹ، سروس، نوٹ بک، یا CI جاب میں شامل کریں | Python API | [Python API](api.md) |
| کسی ایجنٹ، ایڈیٹر، یا MCP-مطابق کلائنٹ کو آپ کے لیے مواد ترجمہ کرنے دیں | MCP Server | [MCP Server](mcp.md) |
| اپنی ایپ پہلے ہی لوڈ کی ہوئی ایک Markdown دستاویز، نوٹ بک، یا تصویر کا ترجمہ کریں | Python API یا MCP Server | [Python API](api.md) یا [MCP Server](mcp.md) |
| معیاری آؤٹ پٹ فولڈرز اور میٹا ڈیٹا کے ساتھ پوری ریپوزیٹری کا ترجمہ کریں | CLI یا `run_translation` | [CLI حوالہ](cli.md) یا [Python API](api.md) |

## CLI استعمال کریں جب

جب کوئی شخص یا CI جاب شیل سے ریپوزیٹری کا ترجمہ چلا رہا ہو تو CLI کو منتخب کریں۔

جب آپ چاہتے ہیں کہ Co-op Translator پروجیکٹ فائلیں دریافت کرے، مترجم شدہ آؤٹ پٹس بنائے، پروجیکٹ لے آؤٹ قائم رکھے، میٹا ڈیٹا اپ ڈیٹ کرے، اور ریویو کمانڈز چلائے تو CLI سب سے براہِ راست راستہ ہے۔

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

یہ مثال Markdown اور نوٹ بکس کا ترجمہ کرتی ہے۔ `-img` کو صرف [Azure AI Vision](configuration.md#azure-ai-vision) کو ترتیب دینے کے بعد شامل کریں۔ پہلی بار صرف Markdown کے لیے، [آپ کا پہلا ترجمہ](first-translation.md) پر عمل کریں۔

مناسب استعمال:

- آپ ٹرمینل سے ایک ریپوزیٹری کا ترجمہ کر رہے ہیں۔
- آپ CI یا ریلیز کے ورک فلو کے لیے ایک قابلِ تکرار کمانڈ چاہتے ہیں۔
- آپ بلٹ-ان پروجیکٹ ڈسکوری، آؤٹ پٹ پاتھز، میٹا ڈیٹا، صفائی، اور ریویو چاہتے ہیں۔
- آپ Python کوڈ لکھنے کی بجائے کمانڈ انٹرفیس کو ترجیح دیتے ہیں۔

## Python API استعمال کریں جب

جب آپ کا اپنا کوڈ ورک فلو کو کنٹرول کرنا چاہیے تو Python API کو منتخب کریں۔

API ایپلیکیشنز، آٹومیشن اسکرپٹس، نوٹ بکس، سروسز، اور کسٹم پائپ لائنز کے لیے مفید ہے۔ یہ آپ کو انفرادی فائلوں کے لیے لو لیول کنٹینٹ ترجمہ APIs کال کرنے یا CLI کے ذریعے استعمال ہونے والے اسی ریپوزیٹری-سطح کے آرکسٹریشن کو چلانے کی اجازت دیتی ہے۔

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

Python سے ریپوزیٹری ترجمہ چلائیں:

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

مناسب حالات:

- آپ کی ایپ پہلے سے فائلیں، بفرز، نوٹ بکس، یا امیج بائٹس پڑھتی ہے۔
- آپ کو کسٹم ویلیڈیشن، اسٹوریج، لاگنگ، ریٹرائیز، یا منظوری کے فلو کی ضرورت ہے۔
- آپ ایک دستاویز، نوٹ بک، یا تصویر کا ترجمہ کرنا چاہتے ہیں بغیر پوری ریپوزیٹری کو پراسیس کیے۔
- آپ ریپوزیٹری ترجمہ چاہتے ہیں، مگر شیل کمانڈ کی بجائے Python آٹومیشن سے۔

## MCP Server استعمال کریں جب

جب کسی ایجنٹ، ایڈیٹر، یا MCP-مطابق کلائنٹ کو Co-op Translator ٹولز کال کرنے چاہئیں تو MCP سرور کو منتخب کریں۔

معمول کے لوکل سیٹ اپ میں، صارف دستی طور پر سرور کو چلتا ہوا نہیں رکھتا۔ جب ٹولز کی ضرورت ہو تو MCP کلائنٹ `stdio` کے ذریعے `co-op-translator-mcp` شروع کرتا ہے۔

مثالی صارف کی وہ درخواستیں جو ایک ایجنٹ سنبھال سکتا ہے:

- "اس Markdown فائل کو کوریائی میں ترجمہ کریں اور لنکس کو درست رکھیں۔"
- "اس Markdown فائل کو ایجنٹ-مدد یافتہ MCP ورک فلو کے ساتھ کوریائی میں ترجمہ کریں، ترجمہ شدہ چنکس کے لیے اپنا ماڈل استعمال کرتے ہوئے۔"
- "اس نوٹ بک کو کوریائی میں ترجمہ کریں، کوڈ سیلز کو برقرار رکھیں، اور نوٹ بک کو دوبارہ تعمیر کرنے کے لیے Co-op Translator MCP استعمال کریں۔"
- "اس تصویر کے متن کو جاپانی میں ترجمہ کریں اور نتیجہ محفوظ کریں۔"
- "ریپوزیٹری ترجمہ کو ہسپانوی کے لیے ڈرائی-رن کریں اور بتائیں کہ کیا بدلے گا۔"
- "جائزہ لیں کہ کیا کوریائی ترجمہ آؤٹ پٹ تازہ ترین ہے۔"

Markdown اور نوٹ بکس کے لیے، MCP دو وضعوں میں کام کر سکتا ہے:

| وضع | کب استعمال کریں | بنیادی ٹولز |
| --- | --- | --- |
| ایجنٹ-مدد یافتہ | MCP ہوسٹ ایجنٹ کو اپنے ماڈل کے ساتھ چنکس کا ترجمہ کرنا چاہیے، بغیر Co-op Translator LLM فراہم کنندہ کی اسناد کے۔ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| پرووائڈر-بیکڈ | Co-op Translator کو براہِ راست Azure OpenAI، OpenAI، یا Anthropic کو کال کرنا چاہیے۔ | `translate_markdown_content`, `translate_notebook_content` |

MCP پرووائڈر-بیکڈ Markdown ٹول کال کی شکل:

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

MCP امیج ٹول کال کی شکل:

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

ریپوزیٹری ترجمہ MCP کے ذریعے بطورِ ڈیفالٹ ڈرائی-رن ہوتا ہے:

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

- آپ ایک ایجنٹ یا ایڈیٹر کے اندر قدرتی زبان کے ترجمے کے ورک فلو چاہتے ہیں۔
- آپ Markdown یا نوٹ بک کی ترجمہ چاہتے ہیں جہاں ہوسٹ ایجنٹ ماڈل تیار کردہ چنکس کا ترجمہ کرے۔
- آپ چاہتے ہیں کہ ایجنٹ منتخب شدہ مواد کا ترجمہ کرے نہ کہ پوری ریپوزیٹری کا۔
- آپ چاہتے ہیں کہ ریپوزیٹری بھر میں تحریر سے پہلے منظوری کا مرحلہ ہو۔
- آپ ایک ایسا انٹرفیس چاہتے ہیں جو Markdown، نوٹ بک، تصویر، جائزہ، اور پاتھ-ریرائٹنگ ٹولز کو ظاہر کرے۔

## یہ ایک دوسرے کے ساتھ کیسے ملتے ہیں

CLI انسانوں کے لیے ریپوزیٹریاں ترجمہ کرنے کے لیے بہترین ڈیفالٹ ہے۔ جب آپ کا کوڈ ورک فلو کا مالک ہو تو Python API بہترین ہے۔ جب ایجنٹ یا ایڈیٹر ورک فلو کا مالک ہو تو MCP سرور بہترین ہے۔

یہ تینوں راستے ایک ہی پبلک Co-op Translator API استعمال کرتے ہیں، اس لیے آپ CLI سے شروع کر سکتے ہیں، بعد میں Python سے خود کار بنا سکتے ہیں، اور جب آپ کو ایجنٹ-چلائے گئے ورک فلو کی ضرورت ہو تو وہی صلاحیتیں MCP کلائنٹس کو فراہم کر سکتے ہیں۔