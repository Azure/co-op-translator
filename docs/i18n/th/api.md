# API ของ Python

อินเทอร์เฟซสาธารณะคงที่สำหรับ Python ถูกส่งออกจาก `co_op_translator.api` การผสานงานส่วนใหญ่ใช้เวิร์กโฟลว์หนึ่งในรายการต่อไปนี้:

| สถานการณ์ | ใช้เมื่อ | API หลัก |
| --- | --- | --- |
| แปลไฟล์หรือเอกสารเดี่ยว | แอปของคุณอ่านเนื้อหาต้นทาง เรียก Co-op Translator เพื่อแปล และตัดสินใจว่าจะบันทึกผลลัพธ์ไว้ที่ใด | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| เตรียมเนื้อหาสำหรับการแปลโดย host-agent | โฮสต์ MCP หรือโมเดลแอปของคุณจะแปลชิ้นส่วน ในขณะที่ Co-op Translator จัดการการแบ่งชิ้นและการประกอบใหม่ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| แปลทั้งรีโพซิทอรี่ | คุณต้องการให้ Python API ทำงานเหมือน CLI และจัดการการค้นหา เส้นทางผลลัพธ์ เมตาดาต้า การล้างข้อมูล และการเขียนไฟล์ | `run_translation` |

โมดูลระดับล่างส่วนใหญ่ภายใต้ `core`, `config`, `review`, และ `utils` เป็นรายละเอียดการใช้งานที่ถูกใช้โดยจุดเข้าของ API เหล่านี้

ไคลเอนต์ MCP ใช้ API สาธารณะเดียวกันผ่าน [MCP Server](mcp.md) ใช้หน้านี้เมื่อเรียก Python โดยตรง และใช้คู่มือ MCP เมื่อเปิดเผย Co-op Translator ให้กับเอเย่นต์หรือแก้ไข หากคุณกำลังตัดสินใจระหว่าง CLI, Python API, และ MCP ให้เริ่มจาก [Choose Your Workflow](workflows.md)

## ขั้นตอนแรกสำหรับการใช้ API

เริ่มที่นี่ถ้าคุณเรียกใช้ Co-op Translator จากโค้ด Python:

1. กำหนดค่าโปรไวเดอร์ LLM ตามที่อธิบายใน [Configuration](configuration.md) เว้นแต่คุณจะเพียงเตรียม Markdown หรือชิ้นโน้ตบุ๊กสำหรับการแปลโดย host-agent เท่านั้น
2. ตัดสินใจว่าแอปของคุณเป็นผู้จัดการ I/O ไฟล์หรือไม่
3. ใช้ API เนื้อหาเมื่อแอปของคุณอ่านและเขียนไฟล์ทีละไฟล์
4. ใช้ `run_translation` เมื่อ Co-op Translator ควรประมวลผลรีโพซิทอรีเหมือน CLI
5. ใช้ `run_review` หลังการแปลหากต้องการการตรวจสอบที่กำหนดผลลัพธ์อย่างแน่นอนในการทำงานอัตโนมัติ

| เป้าหมาย | API ที่เริ่มต้นด้วย |
| --- | --- |
| แปลสตริงหรือไฟล์ Markdown เดียวดาย | `translate_markdown_content` |
| แปลเพย์โหลดโน้ตบุ๊กเดียว | `translate_notebook_content` |
| แปลรูปภาพหนึ่งภาพ | `translate_image_content` |
| ให้ host agent แปลชิ้น Markdown หรือโน้ตบุ๊ก | `start_markdown_agent_translation` หรือ `start_notebook_agent_translation` |
| เขียนทับลิงก์ที่แปลแล้วหลังเลือกเส้นทางผลลัพธ์ | `rewrite_markdown_paths` หรือ `rewrite_notebook_paths` |
| แปลรีโพซิทอรีทั้งหมด | `run_translation` |
| ตรวจสอบผลลัพธ์ที่แปล | `run_review` |

## สถานการณ์ที่ 1: แปลไฟล์หรือเอกสารเดี่ยว

ใช้เวิร์กโฟลว์นี้เมื่อคุณมีไฟล์ แก้ไขบัฟเฟอร์ เพย์โหลดโน้ตบุ๊ก คำขอ MCP หรืออินพุตท่อข้อมูลที่กำหนดเอง โค้ดของคุณเป็นผู้จัดการ I/O ไฟล์:

1. อ่านเนื้อหาต้นทาง
2. เรียก API การแปลเนื้อหา
3. ทางเลือก: เรียก API การเขียนเส้นทางใหม่หากเนื้อหาที่แปลจะถูกเขียนลงในโฟลเดอร์แปลของโปรเจกต์
4. บันทึกหรือคืนค่าผลลัพธ์จากแอปของคุณ

API การแปลเนื้อหาไม่รันการค้นหาโปรเจกต์ ไม่เขียนเมตาดาต้า ไม่แนบคำปฏิเสธความรับผิดชอบ และไม่เขียนทับลิงก์โดยอัตโนมัติ

### ไฟล์ Markdown

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

หาก Markdown ที่แปลแล้วจะไม่ถูกเก็บอยู่ในเลย์เอาต์โปรเจกต์ของ Co-op Translator ให้ข้าม `rewrite_markdown_paths` และบันทึกสตริงที่แปลแล้วโดยตรง

### ไฟล์โน้ตบุ๊ก

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

`translate_notebook_content` แปลเซลล์ Markdown และเก็บเซลล์ที่ไม่ใช่ Markdown ไว้ การเขียนทับเส้นทางใช้กับเฉพาะเซลล์ Markdown เท่านั้น

### ไฟล์รูปภาพ

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

`translate_image_content` อ่านรูปต้นทางและคืนค่า `PIL.Image.Image` ที่เรนเดอร์แล้ว มันไม่เขียนเมตาดาต้าของภาพที่แปลแล้ว

## สถานการณ์ที่ 2: แปลทั้งรีโพซิทอรี

ใช้เวิร์กโฟลว์นี้เมื่อคุณต้องการให้ Python API ทำงานเหมือนคำสั่ง `translate` ของ CLI `run_translation` จะค้นหาไฟล์ที่รองรับ แปลประเภทเนื้อหาที่เลือก เขียนทับเส้นทาง เขียนไฟล์ผลลัพธ์ อัปเดตเมตาดาต้า และดำเนินงานบำรุงรักษาการแปล เช่น การล้างข้อมูล

`run_translation` เป็นจุดเข้าจัดการโปรเจกต์ที่แนะนำ `translate_project` ถูกส่งออกเป็นนามแฝงเพื่อความเข้ากันได้ที่มีพฤติกรรมเดียวกัน

แปลไฟล์ Markdown ในรีโพซิทอรีปัจจุบันเป็นภาษาเกาหลีและภาษาญี่ปุ่น:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

แปลเฉพาะโน้ตบุ๊กจากรากโปรเจกต์ที่ระบุ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

พรีวิวปริมาณการแปลโดยไม่เขียนไฟล์:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

แปลหลายโฟลเดอร์รากในการเรียกครั้งเดียว:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

เขียนการแปลลงในกลุ่มผลลัพธ์ที่ระบุชัดเจน:

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

ใช้ตัวเติมเฉพาะภาษาต่อภาษาเมื่อแต่ละภาษาควรมีไดเรกทอรีย่อย:

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

หากไม่มีค่าใดใน `markdown`, `notebook`, หรือ `images` ถูกตั้งไว้ API จะทำการแปลทุกประเภทที่รองรับ: Markdown, โน้ตบุ๊ก, และรูปภาพ

## ตรวจสอบผลลัพธ์การแปล

`run_review` รันการตรวจสอบการแปลที่กำหนดผลลัพธ์โดยไม่ต้องใช้ข้อมูลรับรอง LLM หรือ Vision

!!! note "Beta"
    `run_review` เป็น API การตรวจสอบกำหนดผลลัพธ์รุ่นเบต้า มันไม่เรียกโปรไวเดอร์โมเดลหรือเขียนไฟล์ แต่สกีมาเรื่องการตรวจสอบและรายการปัญหาอาจพัฒนาได้

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

ตรวจสอบเฉพาะไฟล์ที่เปลี่ยนแปลงเมื่อเทียบกับ base ref และพิมพ์ผลลัพธ์แบบ GitHub-flavored:

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

## ตัวอย่างสำหรับคัดลอก-วาง API

แปลเนื้อหา Markdown โดยไม่เขียนไฟล์:

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

แปลและเขียนทับลิงก์ Markdown:

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

แปลรีโพซิทอรีจาก Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

แปลหลายราก:

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

รักษาคำศัพท์ในพจนานุกรม:

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

## จุดเข้าที่สาธารณะ

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

## API การแปลเนื้อหา

API การแปลเนื้อหามีไว้สำหรับการผสานงานที่มีเนื้อหาอยู่ในหน่วยความจำแล้ว เช่น ส่วนขยายแก้ไข เครื่องมือ MCP ตัวประมวลผลโน้ตบุ๊ก หรือท่อข้อมูลที่กำหนดเอง

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. แปลเฉพาะเนื้อหา Markdown เท่านั้น มันไม่เขียนทับลิงก์ ไม่เขียนเมตาดาต้า หรือแนบคำปฏิเสธความรับผิดชอบ |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. แปลเซลล์ Markdown และเก็บเซลล์ที่ไม่ใช่ Markdown ไว้ มันไม่เขียนทับลิงก์ ไม่เขียนเมตาดาต้า หรือแนบคำปฏิเสธความรับผิดชอบ |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. ดึงข้อความจากภาพและแปล แล้วคืนภาพที่เรนเดอร์แล้ว มันไม่บันทึกเมตาดาต้าของภาพที่แปลแล้ว |

`translate_markdown_content` และ `translate_notebook_content` ยอมรับ `source_path` แบบทางเลือกผ่าน options ของพวกมัน เส้นทางจะถูกส่งเป็นบริบทให้ตัวแปล; ผู้เรียกยังคงรับผิดชอบการเขียนทับเส้นทางเฉพาะโปรเจกต์หลังการแปล

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

ตัวเลือกเดียวกันสามารถส่งเป็นพจนานุกรมได้:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API การแปลที่ช่วยโดยเอเย่นต์

API ที่ช่วยโดยเอเย่นต์จะไม่เรียก Azure OpenAI หรือ OpenAI จาก Co-op Translator พวกมันเตรียมชิ้น Markdown หรือโน้ตบุ๊กสำหรับให้โฮสต์เอเย่นต์แปล จากนั้นประกอบเนื้อหาให้สมบูรณ์จากชิ้นที่แปลแล้ว

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | คืนงาน Markdown ที่เป็นอิสระพร้อมชิ้น ชุดคำสั่ง และสถานะการประกอบใหม่ |
| `finish_markdown_agent_translation` | ประกอบ Markdown ใหม่จากงานและชิ้นที่โฮสต์เอเย่นต์แปลแล้ว |
| `start_notebook_agent_translation` | คืนงานโน้ตบุ๊กที่มีชิ้นเซลล์ Markdown สำหรับการแปลโดยโฮสต์เอเย่นต์ |
| `finish_notebook_agent_translation` | ประกอบโน้ตบุ๊ก JSON ใหม่ในขณะที่เก็บเซลล์โค้ด ผลลัพธ์ และเมตาดาต้าไว้ |

เวิร์กโฟลว์นี้มีไว้สำหรับโฮสต์ MCP เป็นหลัก หากคุณต้องการการแปลรีโพซิทอรีในสภาพการผลิตโดยให้ Co-op Translator จัดการการเรียกโปรไวเดอร์ ให้ใช้ `translate_markdown_content`, `translate_notebook_content`, หรือ `run_translation`

## API การเขียนทับเส้นทาง

API การเขียนทับเส้นทางไม่ทำการแปลใด ๆ พวกมันอัปเดตลิงก์และเส้นทาง frontmatter หลังจากที่ผู้เรียกรู้เส้นทางต้นทาง เส้นทางเป้าหมายที่แปลแล้ว และเลย์เอาต์โปรเจกต์

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | เขียนทับลิงก์ Markdown และฟิลด์เส้นทาง frontmatter ที่รองรับสำหรับเป้าหมายที่แปลแล้ว |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | นำการเขียนทับเส้นทาง Markdown ไปใช้กับแต่ละเซลล์ Markdown และปล่อยให้เซลล์ที่ไม่ใช่ Markdown ไม่เปลี่ยนแปลง |

อาร์กิวเมนต์ `policy` อาจเป็นพจนานุกรมที่มีฟิลด์เหล่านี้:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | รหัสภาษาปลายทาง เช่น `"ko"` หรือ `"pt-BR"` |
| `root_dir` | No | รากโปรเจกต์ต้นทาง ค่าเริ่มต้นเป็น `"."` |
| `translations_dir` | No | ไดเรกทอรีผลลัพธ์การแปลข้อความ ค่าเริ่มต้นเป็น `translations` ภายใต้ `root_dir` |
| `translated_images_dir` | No | ไดเรกทอรีผลลัพธ์ภาพที่แปลแล้ว ค่าเริ่มต้นเป็น `translated_images` ภายใต้ `root_dir` |
| `translation_types` | No | ประเภทการแปลที่เปิดใช้งาน ค่าเริ่มต้นเป็น Markdown, โน้ตบุ๊ก, และรูปภาพ |
| `lang_subdir` | No | ไดเรกทอรีย่อยทางเลือกภายใต้โฟลเดอร์แต่ละภาษา |

## พารามิเตอร์การแปลโปรเจกต์

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | รหัสภาษาปลายทางที่คั่นด้วยช่องว่าง เช่น `"ko ja fr"` หรือ `"all"` รหัสนามแฝงจะถูกปรับเป็นค่า BCP 47 แบบมาตรฐาน |
| `root_dir` | `str` | `"."` | รากโปรเจกต์สำหรับเป้าหมายการแปลเดียว ถูกละเลยเมื่อมีการให้ `root_dirs` หรือ `groups` |
| `update` | `bool` | `False` | ลบแล้วสร้างการแปลที่มีอยู่ใหม่สำหรับภาษาที่เลือก |
| `images` | `bool` | `False` | รวมการแปลรูปภาพ ต้องมีการกำหนดค่า Azure AI Vision |
| `markdown` | `bool` | `False` | รวมการแปล Markdown |
| `notebook` | `bool` | `False` | รวมการแปล Jupyter notebook |
| `debug` | `bool` | `False` | เปิดการบันทึกดีบัก |
| `save_logs` | `bool` | `False` | บันทึกไฟล์ล็อกระดับ DEBUG ภายใต้ไดเรกทอรี `logs/` ที่ราก |
| `yes` | `bool` | `True` | ยืนยันคำถามโดยอัตโนมัติสำหรับการใช้งานเชิงโปรแกรมและ CI |
| `add_disclaimer` | `bool` | `False` | เพิ่มคำปฏิเสธความรับผิดชอบการแปลด้วยเครื่องลงใน Markdown และโน้ตบุ๊กที่แปลแล้ว |
| `translations_dir` | `str \| None` | `None` | ไดเรกทอรีผลลัพธ์การแปลข้อความแบบกำหนดเอง เส้นทางสัมพัทธ์จะถูกแก้ไขสัมพันธ์กับแต่ละราก |
| `image_dir` | `str \| None` | `None` | ไดเรกทอรีผลลัพธ์ภาพที่แปลแล้วแบบกำหนดเอง เส้นทางสัมพัทธ์จะถูกแก้ไขสัมพันธ์กับแต่ละราก |
| `root_dirs` | `Iterable[str] \| None` | `None` | หลายรากที่ใช้การตั้งค่าผลลัพธ์เดียวกัน |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | คู่ `(root_dir, translations_dir)` ที่ระบุชัดเจน มีลำดับความสำคัญเหนือ `root_dirs` |
| `repo_url` | `str \| None` | `None` | URL รีโพซิทอรีที่ใช้เมื่อเรนเดอร์คำแนะนำตารางภาษาใน README |
| `glossaries` | `Iterable[str] \| None` | `None` | คำศัพท์พจนานุกรมที่ต้องการรักษาในระหว่างการแปล รายการซ้ำและคำว่างจะถูกปรับให้เป็นมาตรฐาน |
| `dry_run` | `bool` | `False` | ประเมินปริมาณการแปลและพรีวิวพฤติกรรมการย้ายโดยไม่เขียนไฟล์ |

## พารามิเตอร์การตรวจสอบ

`run_review` ตั้งใจให้มีลายเซ็นใกล้เคียงกับ `run_translation` เท่าที่เป็นไปได้เพื่อให้การทำงานอัตโนมัติสามารถสลับระหว่างเวิร์กโฟลว์การแปลและการตรวจสอบด้วยการแยกสาขาน้อยที่สุด

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | โฟลเดอร์ภาษาปลายทางที่จะตรวจสอบ ยอมรับสตริงที่คั่นด้วยช่องว่างและอิตเทอเรเบิล `"all"` จะตรวจสอบทุกภาษาที่ค้นพบ |
| `root_dir` | `str` | `"."` | รากโปรเจกต์สำหรับเป้าหมายการตรวจสอบเดียว ถูกละเลยเมื่อมีการให้ `root_dirs` หรือ `groups` |
| `markdown` | `bool` | `False` | รวมไฟล์ต้นทาง Markdown และ MDX |
| `notebook` | `bool` | `False` | รวมไฟล์ต้นทาง Jupyter notebook |
| `images` | `bool` | `False` | สำรองไว้เพื่อความเท่าเทียมกับตัวเลือกการแปล การอ้างอิงลิงก์ไปยังภาพจะถูกตรวจจาก Markdown |
| `translations_dir` | `str \| None` | `None` | ไดเรกทอรีเอาต์พุตการแปลข้อความแบบกำหนดเอง เส้นทางสัมพัทธ์จะถูกแก้ไขอ้างอิงกับแต่ละ root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | หลายรูทที่ใช้การตั้งค่าเอาต์พุตเดียวกัน. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | คู่ `(root_dir, translations_dir)` ที่ระบุอย่างชัดเจน จะมีลำดับความสำคัญเหนือ `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref ที่ใช้จำกัดการตรวจทานให้เฉพาะไฟล์ต้นฉบับที่เปลี่ยนแปลง. |
| `output_format` | `str` | `"text"` | รูปแบบเอาต์พุตการตรวจทาน ค่าที่รองรับคือ `"text"` และ `"github"`. |
| `fail_on_warnings` | `bool` | `False` | ถือว่าคำเตือนเป็นความล้มเหลวเพิ่มเติมจากข้อผิดพลาด. |
| `debug` | `bool` | `False` | เปิดการบันทึกดีบัก. |
| `save_logs` | `bool` | `False` | บันทึกไฟล์ล็อกระดับ DEBUG ภายใต้ไดเรกทอรี `logs/` ของรูท. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## ข้อกำหนดการกำหนดค่า

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

## หมายเหตุพฤติกรรม

- Content translation APIs keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content needs project-relative links adjusted for a target location.
- Project orchestration APIs add project behavior around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` prints progress and estimate summaries through Click, matching the CLI user experience.
- `dry_run=True` computes estimates using virtual README updates, but does not write the README or translation files.
- `groups` are processed sequentially. A single aggregate estimate is printed before work begins.
- When image translation is selected, missing Vision configuration raises an error before translation starts.
- Existing alias-based language folders are detected and can be migrated to canonical language folder names as part of the run.
- `run_review` fails on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` reports missing local Markdown and image link targets as warnings by default.

## Internal Call Path

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

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | ประสานงานการแปลในระดับโปรเจกต์ การจัดการไดเรกทอรี การปรับมาตรฐานเมแทดาต้าต่อภาษาต่าง ๆ และการมอบหมายงานไปยังตัวแปล Markdown, notebook, และ image. |
| `TranslationManager` | `co_op_translator.core.project.translation` | ดำเนินการประมวลผลไฟล์แบบอะซิงค์สำหรับ Markdown, notebooks, images, การตรวจจับไฟล์เก่า (stale), และการอัปเดตเมแทดาต้าการแปล. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | จัดลำดับการอ่านไฟล์ Markdown, การแปลเนื้อหา, การเขียนเส้นทางใหม่, เมแทดาต้า, หมายปฏิเสธความรับผิดชอบ, และการเขียนไฟล์. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | จัดลำดับการอ่านไฟล์โน้ตบุ๊ก, การแปลเซลล์ Markdown, การเขียนเส้นทางใหม่, เมแทดาต้า, หมายปฏิเสธความรับผิดชอบ, และการเขียนไฟล์. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | จัดลำดับการค้นหาไฟล์ภาพต้นทาง, การแปลภาพ, เส้นทางเอาต์พุต, เมแทดาต้า, และการเขียนไฟล์. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | ค้นหาคู่ไฟล์ Markdown ที่แปลแล้ว, ประเมินคุณภาพการแปล, และอ่านเมแทดาต้าความเชื่อมั่นสำหรับเวิร์กโฟลว์ซ่อมแซมที่มีความเชื่อมั่นต่ำ. |
| `ReviewRunner` | `co_op_translator.review.runner` | ประสานการตรวจสอบเชิงกำหนดได้ข้ามไฟล์ต้นทาง ภาษาที่เป็นเป้าหมาย และรูทการแปลที่กำหนดค่าไว้. |
| `ReviewTarget` | `co_op_translator.review.targets` | อธิบายรูทต้นทางและไดเรกทอรีเอาต์พุตการแปลที่ถูกตรวจทานสำหรับรูทนั้น. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | ตรวจจับโฟลเดอร์ภาษาที่เป็น alias แบบเก่าและเตรียมแผนการย้ายไปยังชื่อโฟลเดอร์ภาษาแบบมาตรฐาน BCP 47. |
| `Config` | `co_op_translator.config.base_config` | โหลดไฟล์ `.env` และตรวจสอบว่า LLM ที่จำเป็นและผู้ให้บริการ Vision ทางเลือกได้รับการกำหนดค่าหรือไม่. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | ตรวจจับอัตโนมัติว่าเป็น Azure OpenAI หรือ OpenAI, ตรวจสอบตัวแปรสภาพแวดล้อมที่จำเป็น, และเรียกการตรวจสอบการเชื่อมต่อกับผู้ให้บริการ. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | ตรวจจับการกำหนดค่า Azure AI Vision และเรียกการตรวจสอบการเชื่อมต่อสำหรับการแปลภาพ. |