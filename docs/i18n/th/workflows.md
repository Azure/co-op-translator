# เลือกเวิร์กโฟลว์ของคุณ

Co-op Translator สามารถใช้ได้ในสามวิธี: CLI, Python API, และ MCP server. พวกมันมีความสามารถในการแปลเหมือนกัน แต่ละแบบเหมาะกับเวิร์กโฟลว์ที่ต่างกัน.

ใช้หน้านี้เมื่อคุณกำลังตัดสินใจว่าจะเริ่มจากจุดใด

**หากคุณแก้ไขการแปลด้วยมือ:** เวิร์กโฟลว์เริ่มต้นของ CLI และ Actions จะทำการแปลใหม่ไฟล์ต้นฉบับที่มีการเปลี่ยนแปลงทั้งหมด ดังนั้นข้อความที่คุณเขียนในไฟล์เหล่านั้นอาจถูกเขียนทับ ควรตรวจทาน diff ก่อนยอมรับการอัปเดต สำหรับการรักษาระดับบล็อกของ Markdown เมื่อยอมรับการแก้ไข ให้ใช้ตัวให้บริการสถานะการแปลของ Python API(api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## การตัดสินใจอย่างรวดเร็ว

| ถ้าคุณต้องการ... | ใช้ | เริ่มที่นี่ |
| --- | --- | --- |
| แปลหรือทบทวนรีโพซิทอรีจากเทอร์มินัล | CLI | [เอกสารอ้างอิง CLI](cli.md) |
| เพิ่มการแปลลงในสคริปต์ Python, บริการ, โน้ตบุ๊ก, หรืองาน CI | Python API | [Python API](api.md) |
| ให้เอเย่นต์, โปรแกรมแก้ไข, หรือไคลเอนต์ที่เข้ากันได้กับ MCP แปลเนื้อหาให้คุณ | MCP Server | [MCP Server](mcp.md) |
| แปลเอกสาร Markdown หนึ่งฉบับ, โน้ตบุ๊ก, หรือรูปภาพที่แอปของคุณโหลดมาแล้ว | Python API หรือ MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| แปลรีโพซิทอรีทั้งหมดพร้อมโฟลเดอร์เอาต์พุตมาตรฐานและเมตาดาต้า | CLI or `run_translation` | [เอกสารอ้างอิง CLI](cli.md) หรือ [Python API](api.md) |

## ใช้ CLI เมื่อ

เลือกใช้ CLI เมื่อบุคคลหรืองาน CI เป็นผู้ควบคุมการแปลรีโพซิทอรีจากเชลล์

CLI เป็นวิธีที่ตรงที่สุดเมื่อคุณต้องการให้ Co-op Translator ค้นหาไฟล์โครงการ สร้างผลลัพธ์ที่แปลแล้ว รักษาเค้าโครงโครงการ อัปเดตเมตาดาต้า และรันคำสั่งตรวจทาน

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

ตัวอย่างนี้แปล Markdown และโน้ตบุ๊ก ให้เพิ่ม `-img` เฉพาะหลังจากตั้งค่า [Azure AI Vision](configuration.md#azure-ai-vision) แล้ว สำหรับการรันครั้งแรกที่แปลเฉพาะ Markdown เท่านั้น ให้ทำตาม [การแปลครั้งแรกของคุณ](first-translation.md).

เหมาะสำหรับ:

- คุณกำลังแปลรีโพซิทอรีจากเทอร์มินัลของคุณ.
- คุณต้องการคำสั่งที่ทำซ้ำได้สำหรับเวิร์กโฟลว์ CI หรือการปล่อย
- คุณต้องการการค้นหาโปรเจกต์ในตัว, เส้นทางเอาต์พุต, เมตาดาต้า, การทำความสะอาด และการตรวจทาน
- คุณชอบอินเทอร์เฟซคำสั่งมากกว่าการเขียนโค้ด Python

## ใช้ Python API เมื่อ

เลือก Python API เมื่อโค้ดของคุณเองควรเป็นผู้ควบคุมเวิร์กโฟลว์

API มีประโยชน์สำหรับแอปพลิเคชัน สคริปต์อัตโนมัติ โน้ตบุ๊ก บริการ และไพป์ไลน์ที่กำหนดเอง มันช่วยให้คุณเรียก API การแปลเนื้อหาระดับต่ำสำหรับไฟล์แต่ละไฟล์ หรือรันการออร์เคสตราระดับรีโพซิทอรีเดียวกันที่ CLI ใช้

แปลเอกสาร Markdown หนึ่งฉบับแล้วตัดสินใจว่าจะบันทึกที่ไหน:

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

รันการแปลรีโพซิทอรีจาก Python:

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

เหมาะสำหรับ:

- แอปของคุณอ่านไฟล์ บัฟเฟอร์ โน้ตบุ๊ก หรือไบต์รูปภาพอยู่แล้ว
- คุณต้องการการตรวจสอบ ความเก็บรักษา การบันทึก การลองใหม่ หรือกระบวนการอนุมัติที่กำหนดเอง
- คุณต้องการแปลเอกสาร โน้ตบุ๊ก หรือรูปภาพหนึ่งไฟล์โดยไม่ต้องประมวลผลทั้งรีโพซิทอรี
- คุณต้องการการแปลรีโพซิทอรี แต่จากการอัตโนมัติด้วย Python แทนคำสั่งเชลล์

## ใช้ MCP Server เมื่อ

เลือก MCP server เมื่อเอเย่นต์ โปรแกรมแก้ไข หรือไคลเอนต์ที่เข้ากันได้กับ MCP ควรเรียกใช้เครื่องมือของ Co-op Translator

ในการตั้งค่าท้องถิ่นปกติ ผู้ใช้จะไม่ต้องคอยเปิดเซิร์ฟเวอร์ด้วยตัวเอง MCP client จะเริ่ม `co-op-translator-mcp` ผ่าน `stdio` เมื่อจำเป็นต้องใช้เครื่องมือ

ตัวอย่างคำขอของผู้ใช้ที่เอเย่นต์อาจจัดการได้:

- "แปลไฟล์ Markdown นี้เป็นภาษาเกาหลีและคงลิงก์ให้ถูกต้อง."
- "แปลไฟล์ Markdown นี้เป็นภาษาเกาหลีด้วยเวิร์กโฟลว์ MCP ที่มีเอเย่นต์ช่วย โดยใช้โมเดลของคุณเองสำหรับชิ้นที่แปล."
- "แปลโน้ตบุ๊กนี้เป็นภาษาเกาหลี รักษาเซลล์โค้ดไว้ และใช้ Co-op Translator MCP ในการประกอบโน้ตบุ๊กกลับ"
- "แปลข้อความในรูปภาพนี้เป็นภาษาญี่ปุ่นและบันทึกผลลัพธ์"
- "ทดสอบการรันการแปลรีโพซิทอรีเป็นภาษาสเปนแบบ dry-run แล้วบอกฉันว่าจะมีอะไรเปลี่ยนแปลงบ้าง"
- "ตรวจสอบว่าเอาต์พุตการแปลภาษาเกาหลีเป็นปัจจุบันหรือไม่"

สำหรับ Markdown และโน้ตบุ๊ก MCP สามารถทำงานได้ในสองโหมด:

| โหมด | ใช้เมื่อ | เครื่องมือหลัก |
| --- | --- | --- |
| มีเอเย่นต์ช่วย | เอเย่นต์โฮสต์ MCP ควรแปลชิ้นส่วนด้วยโมเดลของตัวเอง โดยไม่ต้องใช้ข้อมูลรับรองผู้ให้บริการ LLM ของ Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ใช้ผู้ให้บริการ | Co-op Translator ควรเรียก Azure OpenAI, OpenAI, หรือ Anthropic โดยตรง. | `translate_markdown_content`, `translate_notebook_content` |

รูปแบบการเรียกเครื่องมือ Markdown แบบมีผู้ให้บริการของ MCP:

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

รูปแบบการเรียกเครื่องมือรูปภาพของ MCP:

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

การแปลรีโพซิทอรีจะเป็น dry-run ตามค่าเริ่มต้นผ่าน MCP:

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

เหมาะสำหรับ:

- คุณต้องการเวิร์กโฟลว์การแปลที่ใช้ภาษาธรรมชาติภายในเอเย่นต์หรือโปรแกรมแก้ไข
- คุณต้องการการแปล Markdown หรือโน้ตบุ๊กโดยที่โมเดลของเอเย่นต์โฮสต์จะแปลชิ้นที่เตรียมไว้
- คุณต้องการให้เอเย่นต์แปลเนื้อหาที่เลือกแทนการแปลทั้งรีโพซิทอรี
- คุณต้องการขั้นตอนการอนุมัติก่อนการเขียนทั่วทั้งรีโพซิทอรี
- คุณต้องการอินเทอร์เฟซเดียวที่เปิดเผยเครื่องมือสำหรับ Markdown, โน้ตบุ๊ก, รูปภาพ, การตรวจทาน และการเขียนเส้นทางใหม่

## วิธีการทำงานร่วมกัน

CLI เป็นค่าเริ่มต้นที่ดีที่สุดสำหรับผู้ที่แปลรีโพซิทอรีด้วยตนเอง. Python API เหมาะที่สุดเมื่อโค้ดของคุณเป็นผู้ควบคุมเวิร์กโฟลว์. MCP server เหมาะที่สุดเมื่อเอเย่นต์หรือโปรแกรมแก้ไขเป็นผู้ควบคุมเวิร์กโฟลว์.

ทั้งสามเส้นทางใช้ Co-op Translator API สาธารณะชุดเดียวกัน ดังนั้นคุณสามารถเริ่มด้วย CLI, ทำให้เป็นอัตโนมัติด้วย Python ในภายหลัง, และเปิดเผยความสามารถเดียวกันแก่ไคลเอนต์ MCP เมื่อคุณต้องการเวิร์กโฟลว์ที่ขับเคลื่อนโดยเอเย่นต์.