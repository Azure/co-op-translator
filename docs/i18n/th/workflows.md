# เลือกเวิร์กโฟลว์ของคุณ

Co-op Translator สามารถใช้งานได้สามวิธี: CLI, Python API และ MCP server ทั้งสามวิธีมีความสามารถในการแปลเหมือนกัน แต่แต่ละวิธีเหมาะกับเวิร์กโฟลว์ที่ต่างกัน

ใช้หน้านี้เมื่อคุณกำลังตัดสินใจว่าจะเริ่มจากที่ไหน

## การตัดสินใจอย่างรวดเร็ว

| If you want to... | Use | Start here |
| --- | --- | --- |
| แปลหรือทบทวนรีโพซิทอรีจากเทอร์มินัล | CLI | [CLI Reference](cli.md) |
| เพิ่มการแปลลงในสคริปต์ Python, บริการ, โน้ตบุ๊ก หรือ งาน CI | Python API | [Python API](api.md) |
| ให้เอเย่นต์, เครื่องมือแก้ไข, หรือไคลเอนต์ที่เข้ากันได้กับ MCP แปลเนื้อหาให้คุณ | MCP Server | [MCP Server](mcp.md) |
| แปลเอกสาร Markdown หนึ่งฉบับ, โน้ตบุ๊ก หรือรูปภาพที่แอปของคุณโหลดไว้แล้ว | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| แปลรีโพซิทอรีทั้งหมดโดยมีโฟลเดอร์ผลลัพธ์มาตรฐานและเมตาดาต้า | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Use the CLI when

Choose the CLI when a person or CI job is driving repository translation from a shell.

The CLI is the most direct path when you want Co-op Translator to discover project files, create translated outputs, preserve the project layout, update metadata, and run review commands.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

เหมาะสำหรับ:

- คุณกำลังแปลรีโพซิทอรีจากเทอร์มินัลของคุณ
- คุณต้องการคำสั่งที่ทำซ้ำได้สำหรับเวิร์กโฟลว์ CI หรือการปล่อยเวอร์ชัน
- คุณต้องการการค้นหาโปรเจกต์, เส้นทางผลลัพธ์, เมตาดาต้า, การทำความสะอาด, และการทบทวนที่มีมาให้
- คุณชอบอินเทอร์เฟซแบบคำสั่งมากกว่าการเขียนโค้ด Python

## Use the Python API when

Choose the Python API when your own code should control the workflow.

The API is useful for applications, automation scripts, notebooks, services, and custom pipelines. It lets you call low-level content translation APIs for individual files, or run the same repository-level orchestration used by the CLI.

Translate one Markdown document and decide where to save it:

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

Run a repository translation from Python:

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

เหมาะสำหรับ:

- แอปของคุณอ่านไฟล์, บัฟเฟอร์, โน้ตบุ๊ก, หรือไบต์ของรูปภาพอยู่แล้ว
- คุณต้องการการตรวจสอบความถูกต้อง, การจัดเก็บ, การบันทึก, การลองใหม่, หรือโฟลว์การอนุมัติแบบกำหนดเอง
- คุณต้องการแปลเอกสาร, โน้ตบุ๊ก, หรือรูปภาพเพียงชิ้นเดียวโดยไม่ต้องประมวลผลทั้งรีโพซิทอรี
- คุณต้องการการแปลรีโพซิทอรี แต่จากการทำงานอัตโนมัติด้วย Python แทนคำสั่งเชลล์

## Use the MCP Server when

Choose the MCP server when an agent, editor, or MCP-compatible client should call Co-op Translator tools.

In the normal local setup, the user does not manually keep a server running. The MCP client starts `co-op-translator-mcp` over `stdio` when it needs the tools.

Example user requests an agent could handle:

- "แปลไฟล์ Markdown นี้เป็นภาษาเกาหลีและรักษาความถูกต้องของลิงก์ไว้"
- "แปลไฟล์ Markdown นี้เป็นภาษาเกาหลีด้วยเวิร์กโฟลว์ MCP ที่มีการช่วยจากเอเย่นต์ โดยใช้โมเดลของคุณเองสำหรับชิ้นที่จะแปล"
- "แปลโน้ตบุ๊กนี้เป็นภาษาเกาหลี รักษาเซลล์โค้ดไว้ และใช้ Co-op Translator MCP ในการสร้างโน้ตบุ๊กขึ้นมาใหม่"
- "แปลข้อความในรูปภาพนี้เป็นภาษาญี่ปุ่นและบันทึกผลลัพธ์"
- "จำลองการแปลรีโพซิทอรีเป็นภาษาสเปนและบอกฉันว่าจะมีการเปลี่ยนแปลงอะไรบ้าง"
- "ตรวจสอบว่าผลลัพธ์การแปลเป็นภาษาเกาหลีเป็นปัจจุบันหรือไม่"

For Markdown and notebooks, MCP can work in two modes:

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-assisted | The MCP host agent should translate chunks with its own model, without Co-op Translator LLM provider credentials. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator should call Azure OpenAI or OpenAI directly. | `translate_markdown_content`, `translate_notebook_content` |

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

Repository translation is dry-run by default through MCP:

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

- คุณต้องการเวิร์กโฟลว์การแปลด้วยภาษาธรรมชาติภายในเอเย่นต์หรือเครื่องมือแก้ไข
- คุณต้องการการแปล Markdown หรือโน้ตบุ๊กที่โฮสต์เอเย่นต์แปลชิ้นที่เตรียมไว้ด้วยโมเดลของตัวเอง
- คุณต้องการให้เอเย่นต์แปลเนื้อหาที่เลือกแทนการแปลทั้งรีโพซิทอรี
- คุณต้องการขั้นตอนการอนุมัติก่อนการเขียนทั่วทั้งรีโพซิทอรี
- คุณต้องการอินเทอร์เฟซเดียวที่เปิดเผยเครื่องมือสำหรับ Markdown, โน้ตบุ๊ก, รูปภาพ, การทบทวน, และการเขียนเส้นทางใหม่

## How They Fit Together

The CLI is the best default for humans translating repositories. The Python API is best when your code owns the workflow. The MCP server is best when an agent or editor owns the workflow.

All three paths use the same public Co-op Translator API, so you can start with the CLI, automate with Python later, and expose the same capabilities to MCP clients when you need agent-driven workflows.