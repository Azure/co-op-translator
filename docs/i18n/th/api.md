# API ของ Python

API สาธารณะเวอร์ชันเสถียรของ Python ถูกส่งออกจาก `co_op_translator.api`. การผนวกรวมส่วนใหญ่ใช้หนึ่งในเวิร์กโฟลว์เหล่านี้:

| สถานการณ์ | ใช้เมื่อ | API หลัก |
| --- | --- | --- |
| แปลไฟล์หรือเอกสารแบบเดี่ยว | แอปของคุณอ่านเนื้อหาแหล่งที่มา เรียก Co-op Translator เพื่อแปล และตัดสินใจว่าจะบันทึกผลลัพธ์ไว้ที่ใด. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| เตรียมเนื้อหาสำหรับการแปลโดย host-agent | MCP host หรือโมเดลในแอปของคุณจะเป็นผู้แปลชิ้นส่วน ขณะที่ Co-op Translator จัดการการแบ่งชิ้นและการประกอบกลับ. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| แปลทั้งรีโพซิทอรี | คุณต้องการให้ Python API ทำงานเหมือน CLI และจัดการการค้นหา เส้นทางเอาต์พุต เมตาดาต้า การทำความสะอาด และการเขียนไฟล์. | `run_translation` |

โมดูลระดับต่ำส่วนใหญ่ภายใต้ `core`, `config`, `review`, และ `utils` เป็นรายละเอียดการใช้งานที่ถูกใช้โดยจุดเข้า API เหล่านี้.

ไคลเอนต์ MCP ใช้ API สาธารณะเดียวกันผ่าน [เซิร์ฟเวอร์ MCP](mcp.md). ใช้หน้าหน้านี้เมื่อเรียก Python โดยตรง และใช้คำแนะนำ MCP เมื่อเปิดเผย Co-op Translator ให้กับเอเย่นต์หรือเครื่องมือแก้ไข หากคุณกำลังตัดสินใจระหว่าง CLI, Python API และ MCP ให้เริ่มที่ [เลือกเวิร์กโฟลว์ของคุณ](workflows.md).

## ขั้นตอนการใช้งานครั้งแรกของ API

เริ่มที่นี่หากคุณเรียกใช้ Co-op Translator จากโค้ด Python:

1. ตั้งค่าผู้ให้บริการ LLM ตามที่อธิบายไว้ใน [การกำหนดค่า](configuration.md) เว้นแต่คุณกำลังเตรียมเฉพาะชิ้นส่วน Markdown หรือโน้ตบุ๊กสำหรับการแปลโดยโฮสต์-เอเย่นต์.
2. ตัดสินใจว่าการอ่าน/เขียนไฟล์เป็นความรับผิดชอบของแอปของคุณหรือไม่.
3. ใช้ content APIs เมื่อแอปของคุณอ่านและเขียนไฟล์แต่ละไฟล์.
4. ใช้ `run_translation` เมื่อ Co-op Translator ควรประมวลผลรีโพซิทอรีเหมือน CLI.
5. ใช้ `run_review` หลังการแปลหากคุณต้องการการตรวจสอบแบบกำหนดได้ในการทำงานอัตโนมัติ.

| เป้าหมาย | API ที่ควรเริ่มใช้ |
| --- | --- |
| แปลสตริงหรือไฟล์ Markdown เดียว | `translate_markdown_content` |
| แปลเพย์โหลดของโน้ตบุ๊กหนึ่งรายการ | `translate_notebook_content` |
| แปลภาพหนึ่งภาพ | `translate_image_content` |
| ให้ host agent แปลชิ้นส่วน Markdown หรือโน้ตบุ๊ก | `start_markdown_agent_translation` หรือ `start_notebook_agent_translation` |
| เขียนทับลิงก์ที่แปลแล้วหลังเลือกเส้นทางเอาต์พุต | `rewrite_markdown_paths` หรือ `rewrite_notebook_paths` |
| แปลรีโพซิทอรีทั้งหมด | `run_translation` |
| ตรวจทานผลลัพธ์การแปล | `run_review` |

## สถานการณ์ที่ 1: แปลไฟล์หรือเอกสารแบบเดี่ยว

ใช้เวิร์กโฟลว์นี้เมื่อคุณมีไฟล์ บัฟเฟอร์ของโปรแกรมแก้ไข เพย์โหลดโน้ตบุ๊ก คำขอ MCP หรืออินพุตของพายป์ไลน์ที่กำหนดเอง แอปของคุณเป็นผู้รับผิดชอบการอ่าน/เขียนไฟล์:

1. อ่านเนื้อหาแหล่งที่มา.
2. เรียกใช้ content translation API.
3. โดยเลือก เรียก API สำหรับเขียนทับเส้นทาง หากเนื้อหาที่แปลจะถูกเขียนลงในโฟลเดอร์แปลของโปรเจกต์.
4. บันทึกหรือคืนผลลัพธ์จากแอปของคุณ.

Content translation APIs จะไม่ทำการค้นหาโปรเจกต์ ไม่เขียนเมตาดาต้า ไม่แนบข้อความปฏิเสธความรับผิดชอบ และจะไม่เขียนทับลิงก์โดยอัตโนมัติ.

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

หาก Markdown ที่แปลแล้วจะไม่ได้อยู่ในโครงสร้างโปรเจกต์ของ Co-op Translator ให้ข้าม `rewrite_markdown_paths` และบันทึกสตริงที่แปลแล้วโดยตรง.

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

`translate_notebook_content` จะแปลเซลล์ Markdown และเก็บรักษาเซลล์ที่ไม่ใช่ Markdown ไว้ การเขียนทับเส้นทางจะนำไปใช้เฉพาะกับเซลล์ Markdown เท่านั้น.

### ไฟล์ภาพ

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

`translate_image_content` อ่านรูปต้นฉบับและคืนค่า `PIL.Image.Image` ที่เรนเดอร์แล้ว ไม่เขียนเมตาดาต้าภาพที่แปลแล้ว.

## สถานการณ์ที่ 2: แปลรีโพซิทอรีทั้งชุด

ใช้เวิร์กโฟลว์นี้เมื่อคุณต้องการให้ Python API ทำงานเหมือน `translate` CLI. `run_translation` จะค้นหาไฟล์ที่รองรับ แปลประเภทเนื้อหาที่เลือก เขียนทับเส้นทาง เขียนไฟล์เอาต์พุต อัปเดตเมตาดาต้า และทำงานบำรุงรักษาการแปล เช่น การทำความสะอาด.

`run_translation` เป็นจุดเข้าเชื่อมประสานโครงการที่แนะนำ `translate_project` ถูกส่งออกเป็นนามแฝงเพื่อความเข้ากันได้ที่มีพฤติกรรมเหมือนกัน.

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

ดูตัวอย่างปริมาณการแปลโดยไม่เขียนไฟล์:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

บันทึกเหตุการณ์ความคืบหน้าในรูปแบบมีโครงสร้างสำหรับการผนวกรวม:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # จัดเก็บเพย์โหลดไว้ในตาราง job-event ของคุณ หรือสตรีมไปยัง UI ของคุณ


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

เหตุการณ์ใช้สคีมาที่กำหนดเวอร์ชัน `co-op.translation.event.v1`. การผนวกรวมควร
อาศัยฟิลด์ที่เสถียร เช่น `type` และ `stage_key` ไม่ใช่ข้อความที่มุ่งสู่ผู้ใช้
บนคอนโซลหรือ `stage_label`.

แปลหลายรูทเนื้อหาในการเรียกครั้งเดียว:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

เขียนการแปลลงในกลุ่มเอาต์พุตที่ระบุ:

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

ใช้ตัวแทนต่อภาษาเมื่อแต่ละภาษาควรมีไดเรกทอรีย่อยซ้อนอยู่:

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

หากไม่ได้ตั้งค่า `markdown`, `notebook`, หรือ `images` ใดๆ API จะทำการแปลทุกประเภทที่รองรับ: Markdown, โน้ตบุ๊ก และภาพ.

### เก็บรักษาการแก้ไขโดยมนุษย์ที่ยอมรับแล้วด้วยตัวจัดหาสถานะการแปล

โดยเริ่มต้น Co-op Translator จะเก็บพฤติกรรมระดับไฟล์ที่มีอยู่: เมื่อ
แหล่ง Markdown ล้าสมัย ไฟล์ที่แปลทั้งหมดจะถูกสร้างใหม่ ระบบที่โฮสต์
การผนวกรวมสามารถเลือกส่ง `TranslationStateProvider` เพื่อเก็บรักษาการแก้ไขโดยมนุษย์
ในบล็อกต้นฉบับที่ไม่ได้เปลี่ยนแปลง.

ตัวจัดหา (provider) จะจัดหาคู่ต้นฉบับ/เป้าหมายที่ได้รับการยอมรับครั้งล่าสุดและบันทึกตัวเลือกใหม่แต่ละรายการ.
การยอมรับยังคงเป็นความรับผิดชอบของการผนวกรวม—for example,
หลังจากคำขอ pull request สำหรับการแปลถูกรวม:

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

สำหรับไฟล์ Markdown ที่มี baseline ที่ได้รับการยอมรับและถูกต้อง, Co-op Translator จะจัดแนว
บล็อก Markdown ระดับบนสุด. บล็อกต้นฉบับที่ไม่เปลี่ยนแปลงจะนำบล็อกที่แปลไว้แล้วในปัจจุบันกลับมาใช้ใหม่
รวมถึงการแก้ไขที่ทำโดยผู้คน; บล็อกต้นฉบับที่ถูกเปลี่ยนหรือเพิ่มจะถูกส่ง
สำหรับการแปล; บล็อกต้นฉบับที่ถูกลบจะถูกลบออก. หากการจัดแนวไม่ชัดเจน,
โครงสร้างเป้าหมายเปลี่ยนแปลง, การแปลบล็อกไม่ถูกต้อง, หรือไม่มี baseline
พร้อมใช้งาน, Co-op Translator จะกลับไปอย่างปลอดภัยยัง
เส้นทางการแปลแบบไฟล์ฉบับเต็มที่มีอยู่.

API นี้เก็บสถานะการแปลของเอกสาร ไม่ใช่หน่วยความจำการแปลวลีหรือ
ส่วนต่อประโยคข้ามเอกสาร ขณะนี้ใช้กับการแปลโปรเจกต์ Markdown.
พฤติกรรมของโน้ตบุ๊กและภาพยังไม่เปลี่ยนแปลง การส่ง `update=True`
ยังคงขอการสร้างใหม่ทั้งไฟล์.

หากไฟล์หนึ่งไฟล์หรือมากกว่านั้นไม่สามารถแปลได้ `run_translation` จะยกข้อยกเว้น
`RuntimeError` หลังจากเวิร์กโฟลว์โปรเจกต์เสร็จสิ้น แทนที่จะรายงาน
การรันที่สำเร็จโดยมีเอาต์พุตหาย Integrations ควรพิจารณานี่เป็นงานที่ล้มเหลว
และเก็บรักษาสถานะการแปลที่ยอมรับก่อนหน้านั้นไว้.

## ตรวจทานผลลัพธ์การแปล

`run_review` รันการตรวจสอบการแปลที่กำหนดได้โดยไม่ต้องใช้ข้อมูลรับรอง LLM หรือ Vision.

!!! note "เบต้า"
    `run_review` เป็น API การตรวจทบทวนแบบเดตเทอมินิสติกในสถานะเบต้า. มันไม่เรียกผู้ให้บริการโมเดลหรือเขียนไฟล์ แต่การตรวจและสคีมาของปัญหาอาจมีการพัฒนา.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

หลังการแปลแบบเฉพาะ README ให้ใช้ขอบเขตเดียวกันสำหรับการตรวจทบทวน:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` ตรวจเฉพาะ `README.md` ภายใต้แต่ละต้นทางที่กำหนด,
รวมถึง `groups` ที่กำหนดเองและไดเรกทอรีเอาต์พุต เอกสารอื่นๆ และ
README ที่ซ้อนกันจะถูกยกเว้น หากไม่มี README ต้นทางจะทำให้เกิด `ValueError`; การตรวจ
การแปลที่ล้มเหลวจะทำให้เกิด `RuntimeError`.

ตรวจเฉพาะไฟล์ที่เปลี่ยนแปลงเมื่อเทียบกับ base ref และแสดงผลลัพธ์แบบ GitHub-flavored:

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

## ตัวอย่าง API สำหรับคัดลอกและวาง

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

แปลรีโพสิทอรีจาก Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

แปลหลาย root:

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

รักษาคำศัพท์:

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

## จุดเข้าถึงสาธารณะ

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

## API การแปลเนื้อหา

API การแปลเนื้อหามีไว้สำหรับการรวมระบบที่มีเนื้อหาอยู่ในหน่วยความจำแล้ว เช่น ส่วนขยายตัวแก้ไข เครื่องมือ MCP ตัวประมวลผลโน๊ตบุ๊ก หรือพายป์ไลน์แบบกำหนดเอง.

| ฟังก์ชัน | อินพุต | เอาต์พุต | การอ่าน/เขียนไฟล์ | หมายเหตุ |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | ไม่ | อะซิงโครนัส. แปลเฉพาะเนื้อหา Markdown เท่านั้น มันไม่เขียนทับลิงก์ ไม่เขียนเมทาดาทา หรือแนบข้อจำกัดความรับผิดชอบ. |
| `translate_notebook_content` | Notebook JSON `str` หรือ `dict` | Notebook JSON `str` | ไม่ | อะซิงโครนัส. แปลเซลล์ Markdown และรักษาเซลล์ที่ไม่ใช่ Markdown ไว้ มันไม่เขียนทับลิงก์ ไม่เขียนเมทาดาทา หรือแนบข้อจำกัดความรับผิดชอบ. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | ซิงโครนัส. สกัดและแปลข้อความในรูปภาพ แล้วคืนค่ารูปภาพที่เรนเดอร์แล้ว มันจะไม่บันทึกเมทาดาทารูปภาพที่แปลแล้ว. |

`translate_markdown_content` และ `translate_notebook_content` รับ `source_path` เป็นอ็อปชันทางเลือก พาธถูกส่งเป็นบริบทไปยังตัวแปล; ผู้เรียกยังคงรับผิดชอบการเขียนทับพาธเฉพาะโครงการหลังการแปล.

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

## API การแปลโดยผู้ช่วยเอเจนต์

API ที่มีผู้ช่วยเอเจนต์จะไม่เรียกผู้ให้บริการ LLM ที่กำหนดไว้จาก Co-op Translator พวกมันเตรียมชิ้นส่วนของ Markdown หรือโน๊ตบุ๊กเพื่อให้เอเจนต์โฮสต์แปล แล้วจึงสร้างเนื้อหาสุดท้ายจากชิ้นส่วนที่แปลแล้ว.

| ฟังก์ชัน | จุดประสงค์ |
| --- | --- |
| `start_markdown_agent_translation` | คืนงาน Markdown ที่ครบถ้วนในตัว ประกอบด้วยชิ้นส่วน พรอมต์ และสถานะการสร้างใหม่. |
| `finish_markdown_agent_translation` | สร้าง Markdown ใหม่จากงานและชิ้นส่วนที่โฮสต์เอเจนต์แปล. |
| `start_notebook_agent_translation` | คืนงานโน๊ตบุ๊กที่มีชิ้นส่วนของเซลล์ Markdown สำหรับการแปลโดยโฮสต์เอเจนต์. |
| `finish_notebook_agent_translation` | สร้าง JSON ของโน๊ตบุ๊กใหม่โดยรักษาเซลล์โค้ด ผลลัพธ์ และเมทาดาทาไว้. |

เวิร์กโฟลว์นี้มีไว้สำหรับโฮสต์ MCP เป็นหลัก หากคุณต้องการการแปลรีโพสิทอรีในงานจริง โดยให้ Co-op Translator จัดการการเรียกผู้ให้บริการ ให้ใช้ `translate_markdown_content`, `translate_notebook_content`, หรือ `run_translation`.

## API การเขียนทับพาธ

API การเขียนทับพาธจะไม่ทำการแปล พวกมันอัปเดตลิงก์และพาธใน frontmatter หลังจากผู้เรียกรู้พาธต้นทาง พาธเป้าหมายที่แปลแล้ว และโครงสร้างโปรเจกต์.

| ฟังก์ชัน | ขอบเขต | หมายเหตุ |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | เขียนทับลิงก์ Markdown และฟิลด์พาธใน frontmatter ที่รองรับสำหรับเป้าหมายที่แปลแล้ว. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | ใช้การเขียนทับพาธ Markdown กับแต่ละเซลล์ Markdown และปล่อยเซลล์ที่ไม่ใช่ Markdown ให้ไม่เปลี่ยนแปลง. |

อาร์กิวเมนต์ `policy` อาจเป็นพจนานุกรมที่มีฟิลด์เหล่านี้:

| ฟิลด์ | จำเป็น | จุดประสงค์ |
| --- | --- | --- |
| `language_code` | Yes | รหัสภาษาปลายทาง เช่น `"ko"` หรือ `"pt-BR"`. |
| `root_dir` | No | รูทโปรเจกต์ต้นทาง ค่าเริ่มต้นเป็น `"."`. |
| `translations_dir` | No | ไดเรกทอรีผลลัพธ์การแปลข้อความ ค่าเริ่มต้นคือ `translations` ภายใต้ `root_dir`. |
| `translated_images_dir` | No | ไดเรกทอรีผลลัพธ์รูปภาพที่แปลแล้ว ค่าเริ่มต้นคือ `translated_images` ภายใต้ `root_dir`. |
| `translation_types` | No | ประเภทการแปลที่เปิดใช้งาน ค่าเริ่มต้นคือ Markdown, โน๊ตบุ๊ก และรูปภาพ. |
| `lang_subdir` | No | ไดเรกทอรีย่อยทางเลือกภายใต้แต่ละโฟลเดอร์ภาษา. |

## พารามิเตอร์การแปลของโครงการ

| พารามิเตอร์ | ประเภท | ค่าเริ่มต้น | จุดประสงค์ |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | รหัสภาษาปลายทางที่คั่นด้วยช่องว่าง เช่น `"ko ja fr"` หรือ `"all"` รหัสแทนจะถูกปรับเป็นค่ามาตรฐาน BCP 47. |
| `root_dir` | `str` | `"."` | รูทโครงการสำหรับเป้าหมายการแปลเดียว จะถูกละเลยเมื่อมีการระบุ `root_dirs` หรือ `groups`. |
| `update` | `bool` | `False` | ลบและสร้างการแปลที่มีอยู่ใหม่สำหรับภาษาที่เลือก. |
| `images` | `bool` | `False` | รวมการแปลรูปภาพ ต้องการการตั้งค่า Azure AI Vision. |
| `markdown` | `bool` | `False` | รวมการแปล Markdown. |
| `notebook` | `bool` | `False` | รวมการแปล Jupyter notebook. |
| `debug` | `bool` | `False` | เปิดใช้งานการบันทึกดีบัก. |
| `save_logs` | `bool` | `False` | บันทึกไฟล์ล็อกระดับ DEBUG ในไดเรกทอรี `logs/` ที่ราก. |
| `yes` | `bool` | `True` | ยืนยันพรอมต์โดยอัตโนมัติสำหรับการใช้งานเชิงโปรแกรมและใน CI. |
| `add_disclaimer` | `bool` | `False` | เพิ่มคำชี้แจงการแปลด้วยเครื่องลงใน Markdown และโน้ตบุ๊กที่แปลแล้ว. |
| `translations_dir` | `str \| None` | `None` | ไดเรกทอรีผลลัพธ์การแปลข้อความแบบกำหนดเอง เส้นทางสัมพัทธ์จะอ้างอิงจากแต่ละ root. |
| `image_dir` | `str \| None` | `None` | ไดเรกทอรีผลลัพธ์ภาพที่แปลแบบกำหนดเอง เส้นทางสัมพัทธ์จะอ้างอิงจากแต่ละ root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | หลาย root ที่ใช้การตั้งค่าผลลัพธ์ร่วมกัน. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | คู่ `(root_dir, translations_dir)` ที่ระบุอย่างชัดเจน มีลำดับความสำคัญเหนือ `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL ของรีโพซิทอรีที่ใช้เมื่อเรนเดอร์คำแนะนำตารางภาษาใน README. |
| `glossaries` | `Iterable[str] \| None` | `None` | คำศัพท์ในกลอสซารีที่จะรักษาไว้ระหว่างการแปล คำที่ซ้ำหรือว่างจะถูกปรับให้เป็นมาตรฐาน. |
| `dry_run` | `bool` | `False` | ประเมินปริมาณการแปลและดูตัวอย่างพฤติกรรมการย้ายข้อมูลโดยไม่เขียนไฟล์. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | อะแดปเตอร์การเก็บสถานะแบบเลือกได้สำหรับ accepted-baseline และ candidate เพื่อการอัปเดต Markdown แบบเพิ่มทีละน้อย หากไม่ระบุ จะคงพฤติกรรมเดิมแบบไฟล์ทั้งหมด. |

## พารามิเตอร์การตรวจทาน

`run_review` ตั้งใจให้สะท้อน signature ของ `run_translation` เท่าที่เป็นไปได้ เพื่อให้ระบบอัตโนมัติสามารถสลับระหว่างเวิร์กโฟลว์การแปลและการตรวจทานด้วยการตัดสินใจสาขาน้อยที่สุด.

| พารามิเตอร์ | ประเภท | ค่าเริ่มต้น | วัตถุประสงค์ |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | โฟลเดอร์ภาษาที่ต้องการตรวจทาน รองรับสตริงที่คั่นด้วยช่องว่างและ iterable ค่า `"all"` จะตรวจทุกรูปแบบภาษาการแปลที่ค้นพบ. |
| `root_dir` | `str` | `"."` | รากโปรเจกต์สำหรับเป้าหมายการตรวจทานเดียว จะถูกละเลยเมื่อมีการระบุ `root_dirs` หรือ `groups`. |
| `markdown` | `bool` | `False` | รวมไฟล์ต้นฉบับ Markdown และ MDX. |
| `notebook` | `bool` | `False` | รวมไฟล์ต้นฉบับ Jupyter notebook. |
| `images` | `bool` | `False` | สงวนไว้เพื่อให้เทียบเท่ากับตัวเลือกการแปล อ้างอิงลิงก์ไปยังภาพจะถูกตรวจสอบจาก Markdown. |
| `translations_dir` | `str \| None` | `None` | ไดเรกทอรีผลลัพธ์การแปลข้อความแบบกำหนดเอง เส้นทางสัมพัทธ์จะอ้างอิงจากแต่ละ root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | หลาย root ที่ใช้การตั้งค่าผลลัพธ์ร่วมกัน. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | คู่ `(root_dir, translations_dir)` ที่ระบุอย่างชัดเจน มีลำดับความสำคัญเหนือ `root_dirs`. |
| `changed_from` | `str \| None` | `None` | อ้างอิง Git ที่ใช้จำกัดการตรวจทานเฉพาะไฟล์ต้นฉบับที่เปลี่ยนแปลง. |
| `readme_only` | `bool` | `False` | ตรวจทานเฉพาะ `README.md` ภายใต้แต่ละ root แหล่งที่มา หาก README ต้นฉบับขาดหาย จะเกิด `ValueError`. |
| `output_format` | `str` | `"text"` | รูปแบบผลลัพธ์การตรวจทาน ค่าที่รองรับได้แก่ `"text"` และ `"github"`. |
| `fail_on_warnings` | `bool` | `False` | พิจารณาคำเตือนเป็นความล้มเหลวด้วยเช่นเดียวกับข้อผิดพลาด. |
| `debug` | `bool` | `False` | เปิดใช้งานการบันทึกแบบ debug. |
| `save_logs` | `bool` | `False` | บันทึกไฟล์ล็อกระดับ DEBUG ใต้ไดเรกทอรี `logs/` ของราก. |

หากไม่ได้ตั้งค่า `markdown`, `notebook` หรือ `images` ใดๆ API จะตรวจทาน Markdown, โน้ตบุ๊ก และอ้างอิงลิงก์ภาพที่เกี่ยวข้องโดยอัตโนมัติ การตรวจทานจะไม่เรียกใช้ผู้ให้บริการ LLM และไม่ต้องการคีย์ API.

## ข้อกำหนดการกำหนดค่า

API การแปลที่พึ่งพา provider จำเป็นต้องกำหนดค่า provider ก่อนการแปล:

- การแปล Markdown และโน้ตบุ๊กต้องการ LLM provider กำหนดค่า Azure OpenAI, OpenAI, หรือ Anthropic.
- การแปลภาพต้องใช้ Azure AI Vision นอกเหนือจาก LLM provider.
- `run_translation` จะรันการตรวจเชื่อมต่อแบบน้ำหนักเบาก่อนเริ่มการแปลของโปรเจกต์.
- API แบบช่วยด้วยเอเย่นต์ `start_*_agent_translation` และ `finish_*_agent_translation` จะไม่เรียกใช้ Co-op Translator LLM providers แอปโฮสต์หรือเอเย่นต์ MCP เป็นผู้แปลชิ้นข้อมูลที่เตรียมไว้.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, และ `run_review` มีความเป็นเชิงกำหนดได้ (deterministic) และไม่ต้องการข้อมูลรับรองของ provider.

ตัวแปรที่จำเป็นสำหรับ Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ตัวแปรที่จำเป็นสำหรับ OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

ตัวแปรที่จำเป็นสำหรับ Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` และ `ANTHROPIC_MAX_TOKENS` เป็นค่าที่เลือกได้ Microsoft Agent Framework เป็นไคลเอนต์โมเดลเริ่มต้นสำหรับผู้ให้บริการทั้งหมดตั้งแต่ Co-op Translator 0.22.0. Semantic Kernel ยังคงสามารถเลือกได้ชั่วคราวด้วย `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` แต่การทำเช่นนั้นจะส่งคำเตือนการเลิกใช้; ดู [การกำหนดค่า](configuration.md#model-client-backend) สำหรับแผนการลบเป็นขั้นตอน.

ตัวแปรที่จำเป็นสำหรับ Azure AI Vision สำหรับการแปลภาพ:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` มีความเป็นเชิงกำหนดได้และไม่ต้องการการกำหนดค่า LLM หรือ Azure AI Vision.

## หมายเหตุการทำงาน

- API การแปลเนื้อหาจะแยกการแปลออกจากการเขียนทับเส้นทางของโปรเจกต์ เรียก `rewrite_markdown_paths` หรือ `rewrite_notebook_paths` โดย explit เมื่อเนื้อหาที่แปลต้องปรับลิงก์สัมพันธ์กับโปรเจกต์ให้เข้ากับตำแหน่งเป้าหมาย.
- API การจัดการโปรเจกต์เพิ่มพฤติกรรมระดับโปรเจกต์รอบๆ การแปลเนื้อหา รวมถึงการค้นหาไฟล์ การเขียน การเขียนทับเส้นทาง ข้อมูลเมตา การทำความสะอาด และคำชี้แจงแบบเลือกได้.
- `run_translation` จะแสดงความคืบหน้าและสรุปการประเมินผ่านตัวรายงานที่ใช้ Rich เดียวกับที่ CLI ใช้ ผลลัพธ์แบบไม่โต้ตอบจะลดรูปเป็นข้อความธรรมดา.
- `dry_run=True` คำนวณการประมาณโดยใช้การอัปเดต README เสมือน แต่จะไม่เขียน README หรือไฟล์การแปล.
- `groups` จะถูกประมวลผลทีละกลุ่ม ผลรวมการประมาณเดียวจะถูกพิมพ์ก่อนเริ่มงาน.
- เมื่อเลือกการแปลภาพ หากการกำหนดค่า Vision ขาดหาย จะเกิดข้อผิดพลาดก่อนเริ่มการแปล.
- ตรวจพบโฟลเดอร์ภาษาที่เป็น alias อยู่แล้วและสามารถย้ายไปยังชื่อโฟลเดอร์ภาษามาตรฐานได้เป็นส่วนหนึ่งของการรัน.
- `run_review` จะล้มเหลวเมื่อไฟล์แปลหาย ข้อมูลแปลที่ขาดหายหรือเก่า เนื้อหา frontmatter/fence ของ Markdown ที่ผิดรูป หรือ JSON ของโน้ตบุ๊กที่แปลไม่ถูกต้อง.
- `run_review` โดยดีฟอลต์จะแจ้งเป้าหมายลิงก์ Markdown และภาพที่หายเป็นคำเตือน.

## เส้นทางการเรียกภายใน

API จะส่งต่อไปยังการใช้งานหลักเดียวกันที่ CLI ใช้:

การแปล:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` สำหรับการแปลในหน่วยความจำ. |
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` สำหรับการประมวลผลเส้นทางภายหลังโดยชัดแจ้ง. |
3. `co_op_translator.api.translation.run_translation` สำหรับการประสานงานโปรเจกต์แบบเต็มรูปแบบ. |
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`. |
5. `co_op_translator.core.project.ProjectTranslator`. |
6. `co_op_translator.core.project.TranslationManager`. |
7. มิกซินการแปลระดับโปรเจกต์ที่เน้นสำหรับ Markdown, โน้ตบุ๊ก, และภาพ. |
8. ตัวแปลสำหรับ Markdown, โน้ตบุ๊ก, ข้อความ, และภาพ ภายใต้ `co_op_translator.core`. |

การตรวจทาน:

1. `co_op_translator.api.review.run_review` |
2. `co_op_translator.review.targets.build_review_targets` |
3. `co_op_translator.review.runner.ReviewRunner` |
4. การตรวจสอบเชิงกำหนดภายใต้ `co_op_translator.review.checks` |

คลาสต่อไปนี้เป็นประโยชน์สำหรับผู้ดูแลระบบ แต่ไม่ได้ส่งออกเป็น API ระดับแพ็กเกจที่มีความเสถียร.

| คลาส | โมดูล | ความรับผิดชอบ |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | ประสานงานการแปลระดับโปรเจกต์ การจัดการไดเรกทอรี การปรับข้อมูลเมตาต่อภาษาให้เป็นมาตรฐาน และมอบหมายงานไปยังตัวแปล Markdown, โน้ตบุ๊ก, และภาพ. |
| `TranslationManager` | `co_op_translator.core.project.translation` | ดำเนินงานประมวลผลไฟล์แบบอะซิงโครนัสสำหรับ Markdown, โน้ตบุ๊ก, ภาพ, การตรวจจับความเก่า และการอัปเดตข้อมูลเมตาการแปล. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | จัดการการอ่านไฟล์ Markdown การแปลเนื้อหา การเขียนทับเส้นทาง ข้อมูลเมตา คำชี้แจง และการเขียนไฟล์. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | จัดการการอ่านไฟล์โน้ตบุ๊ก การแปลเซลล์ Markdown การเขียนทับเส้นทาง ข้อมูลเมตา คำชี้แจง และการเขียนไฟล์. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | จัดการการค้นพบภาพต้นทาง การแปลภาพ เส้นทางผลลัพธ์ ข้อมูลเมตา และการเขียนไฟล์. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | ค้นหาโครงคู่ Markdown ที่แปลแล้ว ประเมินคุณภาพการแปล และอ่านข้อมูลเมตาความเชื่อมั่นสำหรับเวิร์กโฟลว์ซ่อมแซมเมื่อความเชื่อมั่นต่ำ. |
| `ReviewRunner` | `co_op_translator.review.runner` | ประสานการตรวจสอบเชิงกำหนดข้ามไฟล์ต้นทาง ภาษาที่เป็นเป้าหมาย และรากการแปลที่กำหนดค่า. |
| `ReviewTarget` | `co_op_translator.review.targets` | อธิบายรากต้นทางและไดเรกทอรีผลลัพธ์การแปลที่ถูกตรวจทานสำหรับรากนั้น. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | ตรวจจับโฟลเดอร์ภาษาแบบ alias เก่าและเตรียมแผนการย้ายไปยังโฟลเดอร์มาตรฐาน BCP 47. |
| `Config` | `co_op_translator.config.base_config` | โหลดไฟล์ `.env` และตรวจสอบว่าผู้ให้บริการ LLM ที่จำเป็นและ Vision แบบเลือกได้ถูกกำหนดค่าหรือไม่. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | ตรวจจับอัตโนมัติว่าเป็น Azure OpenAI, OpenAI, หรือ Anthropic ยืนยันตัวแปรสภาพแวดล้อมที่จำเป็น และรันการตรวจเชื่อมต่อของ provider. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | ตรวจจับการกำหนดค่า Azure AI Vision และรันการตรวจเชื่อมต่อสำหรับการแปลภาพ. |