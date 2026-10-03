# เซิร์ฟเวอร์ MCP

Co-op Translator รวมเซิร์ฟเวอร์ Model Context Protocol สำหรับเอเจนต์ บรรณาธิการ และไคลเอนต์ที่รองรับ MCP.

สำหรับการตั้งค่าเริ่มต้นในเครื่อง ผู้ใช้ไม่ต้องเปิดเซิร์ฟเวอร์แยกต่างหากด้วยตนเอง พวกเขากำหนดค่าไคลเอนต์ MCP ของตน และไคลเอนต์จะเริ่ม `co-op-translator-mcp` โดยอัตโนมัติผ่าน `stdio` เมื่อจำเป็นต้องใช้เครื่องมือของ Co-op Translator.

หากคุณกำลังตัดสินใจระหว่าง CLI, Python API, และ MCP ให้เริ่มที่ [เลือกเวิร์กโฟลว์ของคุณ](workflows.md).

ใช้ MCP เมื่อเอเจนต์หรือบรรณาธิการควรเรียก Co-op Translator โดยตรง:

| เป้าหมายของผู้ใช้ | เครื่องมือ MCP |
| --- | --- |
| แปลเอกสาร Markdown หนึ่งรายการ, โน้ตบุ๊ก, หรือรูปภาพ | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| แปลเนื้อหา Markdown หรือโน้ตบุ๊กโดยใช้โมเดลเอเจนต์โฮสต์ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| เขียนลิงก์ Markdown หรือโน้ตบุ๊กที่แปลแล้วใหม่หลังเลือกเส้นทางเอาต์พุต | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| แปลรีโพสิตอรีทั้งหมดเหมือน CLI | `run_translation`, `translate_project` |
| ตรวจทานผลการแปลโดยไม่ต้องใช้ข้อมูลรับรอง LLM | `run_review` |
| ตรวจสอบความสามารถและสถานะของสภาพแวดล้อม | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

เซิร์ฟเวอร์ MCP ห่อ API สาธารณะของ Python เดียวกันที่มีเอกสารใน [Python API](api.md). เครื่องมือที่มีผู้ให้บริการเป็นแบ็กเอนด์ใช้ผู้ให้บริการที่กำหนดค่าไว้เดียวกันกับ CLI และ Python API. เครื่องมือที่ช่วยโดยเอเจนต์เตรียมชิ้นส่วนสำหรับเอเจนต์โฮสต์ MCP เพื่อแปล แล้วใช้ Co-op Translator เพื่อประกอบ Markdown หรือ notebook สุดท้าย.

## ขั้นตอนที่ 1: ติดตั้งและกำหนดค่า Co-op Translator

ติดตั้ง Co-op Translator ในสภาพแวดล้อม Python ที่ไคลเอนต์ MCP ของคุณจะใช้:

```bash
pip install co-op-translator
```

สำหรับการพัฒนาในเครื่องจากรีโพสิตอรีนี้ ให้ติดตั้งแพ็กเกจในโหมดแก้ไขได้:

```bash
pip install -e .
```

เลือกโหมดการแปลที่ไคลเอนต์ MCP ของคุณจะใช้:

| โหมด | ใช้สำหรับ | ข้อมูลรับรอง |
| --- | --- | --- |
| Provider-backed | Co-op Translator เรียก `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, หรือ `run_translation`. | การแปลต้องใช้ Azure OpenAI, OpenAI, หรือ Anthropic. การแปลรูปภาพยังต้องใช้ Azure AI Vision. |
| Agent-assisted | เอเจนต์โฮสต์ MCP จะแปลชิ้นที่ถูกส่งคืนโดย `start_markdown_agent_translation` หรือ `start_notebook_agent_translation`. | ไม่ต้องใช้ข้อมูลรับรองผู้ให้บริการ LLM ของ Co-op Translator สำหรับชิ้น Markdown หรือโน้ตบุ๊ก การแปลรูปภาพยังไม่ครอบคลุมโดยโหมดเอเจนต์ช่วย |

ถ้าคุณเริ่มจากการแปล Markdown หรือโน้ตบุ๊กภายในเอเจนต์ เช่น Codex หรือ Claude Code ให้เริ่มด้วยโหมดเอเจนต์ช่วย ใช้โหมดที่ใช้ผู้ให้บริการเมื่อคุณต้องการให้ Co-op Translator เรียกผู้ให้บริการที่คุณกำหนดค่าเอง เมื่อคุณกำลังแปลรูปภาพ หรือเมื่อคุณกำลังรันการแปลระดับรีโพสิตอรีเช่น CLI.

กำหนดค่าผู้ให้บริการหนึ่งชุดสำหรับเวิร์กโฟลว์ที่ใช้ผู้ให้บริการ:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# หรือ OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# หรือ Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

การแปลรูปภาพที่ใช้ผู้ให้บริการต้องการเพิ่มเติม:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    โหมดเอเจนต์ช่วยในปัจจุบันครอบคลุม Markdown และเซลล์ Markdown ในโน้ตบุ๊ก การแปลรูปภาพยังคงใช้กระบวนการแปลรูปภาพที่ใช้ผู้ให้บริการและต้องการ Azure AI Vision สำหรับ OCR และการเรนเดอร์ที่คำนึงถึงเลย์เอาต์.

## ขั้นตอนที่ 2: กำหนดค่าไคลเอนต์ MCP ของคุณ

สำหรับการตั้งค่า `stdio` ปกติในเครื่อง ให้เพิ่ม Co-op Translator ในการกำหนดค่าไคลเอนต์ MCP ของคุณ ไคลเอนต์จะเริ่มและหยุดกระบวนการโดยอัตโนมัติ

การกำหนดค่าสำหรับแพ็กเกจที่ติดตั้ง:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

การกำหนดค่าสำหรับการเช็กเอาต์ซอร์สบน Windows:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

การกำหนดค่าสำหรับการเช็กเอาต์ซอร์สบน macOS หรือ Linux:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

หลังจากเปลี่ยนการกำหนดค่าไคลเอนต์ MCP ให้รีสตาร์ทหรือโหลดไคลเอนต์ใหม่เพื่อให้สามารถค้นหาเซิร์ฟเวอร์ใหม่ได้

## ขั้นตอนที่ 3: ตรวจสอบเซิร์ฟเวอร์ในไคลเอนต์

ให้ไคลเอนต์ MCP แสดงรายการเครื่องมือที่มี หรือเรียกหนึ่งในเฮลเปอร์แบบอ่านอย่างเดียวก่อน:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

การตรวจสอบเบื้องต้นที่เป็นประโยชน์:

| เครื่องมือ | สิ่งที่ควรตรวจสอบ |
| --- | --- |
| `get_api_overview` | ยืนยันว่าเซิร์ฟเวอร์เข้าถึงได้และแสดงเวิร์กโฟลว์ที่มีอยู่. |
| `list_supported_languages` | ยืนยันว่าสามารถโหลดข้อมูลภาษาแพ็กเกจได้. |
| `get_configuration_status` | ยืนยันความพร้อมใช้งานของผู้ให้บริการ LLM และ Vision โดยไม่เปิดเผยค่าลับ. |

## ขั้นตอนที่ 4: เลือกเวิร์กโฟลว์

### แปลไฟล์หรือเอกสารเดี่ยว

ใช้เครื่องมือเนื้อหาระบบผู้ให้บริการเมื่อไคลเอนต์ MCP มีเนื้อหาเอกสารหรือเส้นทางรูปภาพแล้วและต้องการให้ Co-op Translator เรียกผู้ให้บริการแปลที่กำหนดค่าไว้

สำหรับ Markdown:

1. เรียก `translate_markdown_content` ด้วย `document`, `language_code`, และถ้าต้องการ `source_path`.
2. หากผลการแปลจะถูกเขียนลงในเลย์เอาต์ผลลัพธ์ของ Co-op Translator ให้เรียก `rewrite_markdown_paths`.
3. ให้ไคลเอนต์เขียนหรือคืนค่า `content` สุดท้าย.

สำหรับโน้ตบุ๊ก:

1. เรียก `translate_notebook_content` ด้วย JSON ของโน้ตบุ๊กและ `language_code`.
2. เรียก `rewrite_notebook_paths` หากลิงก์ในโน้ตบุ๊กที่แปลแล้วจำเป็นต้องปรับให้เข้ากับเส้นทางเป้าหมาย.
3. เขียนหรือคืนค่า JSON ของโน้ตบุ๊กสุดท้าย.

สำหรับรูปภาพ:

1. เรียก `translate_image_content` ด้วย `image_path`, `language_code`, และทางเลือก `root_dir` หรือ `fast_mode`.
2. อ่าน `data_base64` และ `mime_type` ที่ส่งกลับมา.
3. หากมีการระบุ `output_path` รูปภาพที่แปลแล้วจะถูกบันทึกไปยังเส้นทางนั้นด้วย.

เครื่องมือด้านเนื้อหาไม่ทำการค้นหาโปรเจกต์ อัปเดตเมตาดาต้า ข้อจำกัดความรับผิดชอบ หรือการเขียนเส้นทางอัตโนมัติ หากคุณต้องการให้เอเจนต์โฮสต์แปลชิ้น Markdown หรือโน้ตบุ๊กโดยไม่ใช้ข้อมูลรับรองผู้ให้บริการ LLM ของ Co-op Translator ให้ใช้เวิร์กโฟลว์เอเจนต์ช่วยด้านล่าง.

### แปลด้วยโมเดลเอเจนต์โฮสต์

ใช้เครื่องมือเอเจนต์ช่วยเมื่อคุณต้องการให้เอเจนต์โฮสต์ MCP เช่น ผู้ช่วยด้านการเขียนโค้ด ผลิตข้อความที่แปลแล้วแทนการกำหนดค่าผู้ให้บริการ LLM สำหรับ Co-op Translator.

ในไคลเอนต์ MCP แบบแชท โดยปกติคุณไม่จำเป็นต้องเขียน JSON ของเครื่องมือเอง ขอให้เอเจนต์ใช้เวิร์กโฟลว์เอเจนต์ช่วย:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

สำหรับโน้ตบุ๊ก ให้ใช้รูปแบบเดียวกัน:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

หากไคลเอนต์ MCP ของคุณรองรับ server prompts ให้ใช้ `agent_assisted_markdown_translation_prompt` เพื่อให้ไคลเอนต์โหลดคำแนะนำเวิร์กโฟลว์เดียวกัน.

สำหรับ Markdown:

1. เรียก `start_markdown_agent_translation` ด้วย `document`, `language_code`, และถ้าจำเป็น `source_path`.
2. แปลแต่ละชิ้นที่ส่งกลับมาในเอเจนต์โฮสต์โดยทำตาม `prompt` ของชิ้นงาน.
3. เรียก `finish_markdown_agent_translation` ด้วย `job` ต้นฉบับและชิ้นที่แปลแล้วโดยใช้ `chunk_id` และ `translated_text`.
4. หากเนื้อหาจะถูกเขียนไปยังเส้นทางเป้าหมายที่แปลแล้ว ให้เรียก `rewrite_markdown_paths`.

สำหรับโน้ตบุ๊ก:

1. เรียก `start_notebook_agent_translation` ด้วย JSON ของโน้ตบุ๊กและ `language_code`.
2. แปลแต่ละชิ้นที่ส่งกลับมาในเอเจนต์โฮสต์.
3. เรียก `finish_notebook_agent_translation` ด้วย `job` ต้นฉบับและชิ้นที่แปลแล้ว.
4. เรียก `rewrite_notebook_paths` หากลิงก์ในโน้ตบุ๊กที่แปลแล้วต้องการการปรับเส้นทางเป้าหมาย.

เครื่องมือเอเจนต์ช่วยจะไม่เรียกผู้ให้บริการ LLM ที่กำหนดค่าไว้จาก Co-op Translator เอเจนต์โฮสต์รับผิดชอบการแปลชิ้นที่ส่งกลับมา Co-op Translator จัดการการแยกชิ้น Markdown การรักษาตำแหน่งสำรอง การประกอบ frontmatter ใหม่ การแทนที่เซลล์โน้ตบุ๊ก และการปรับมาตรฐานหลังการแปล.

### แปลรีโพสิทอรีทั้งหมด

ใช้ `run_translation` เมื่อผู้ใช้ต้องการให้ Co-op Translator ทำงานเหมือน CLI `translate`.

การแปลรีโพสิตอรีโดยค่าเริ่มต้นจะตั้งเป็น `dry_run=true` เพื่อให้อเจนต์สามารถตรวจสอบขอบเขตก่อนเปลี่ยนแปลงไฟล์:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

ผลลัพธ์ของ `run_translation` รวมอาเรย์ `events` ที่มีเหตุการณ์
`co-op.translation.event.v1` ของความคืบหน้า ไคลเอนต์ MCP ควรใช้ฟิลด์เช่น
 `type`, `stage_key`, `completed`, `total` และ `current_path` แทนการ
แยกวิเคราะห์ข้อความคอนโซลที่จับได้ ส่ง `json_events_path` เพื่อเขียนเหตุการณ์เหล่านั้น
ลงในไฟล์ NDJSON.

เพื่ออนุญาตการเขียน ผู้เรียกต้องตั้งทั้ง `dry_run=false` และ `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` ถูกเปิดเผยเป็นนามแฝงความเข้ากันได้สำหรับ `run_translation`.

### ตรวจทานผลการแปล

ใช้ `run_review` สำหรับการตรวจสอบแบบกำหนดได้ที่ไม่ต้องใช้ข้อมูลรับรอง LLM หรือ Vision:

!!! note "Beta"
    MCP เปิดเผย API เบต้า `run_review` ซึ่งปลอดภัยสำหรับเวิร์กโฟลว์การตรวจทานแบบอ่านอย่างเดียว แต่การตรวจสอบและสคีมาเรื่องปัญหาอาจเปลี่ยนแปลงได้.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

ผลลัพธ์รวมถึงข้อความที่จับได้และสรุปการตรวจทานที่มีโครงสร้างเมื่อพร้อมใช้งาน.

## การรันเซิร์ฟเวอร์ด้วยตนเอง

การรันด้วยตนเองมีไว้หลักๆ สำหรับการดีบักหรือสำหรับการขนส่งที่ทำงานเหมือนเซิร์ฟเวอร์ระยะยาว.

ดีบักเซิร์ฟเวอร์ stdio เริ่มต้น:

```bash
co-op-translator-mcp
```

Run from a source checkout:

```bash
python -m co_op_translator.mcp.server
```

เรียกใช้เซิร์ฟเวอร์ HTTP หรือ SSE ที่ทำงานเป็นเวลานาน:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

สำหรับการผนวกรูปแบบกับบรรณาธิการและเอเจนต์ในเครื่อง ให้ใช้การกำหนดค่า `stdio` ที่จัดการโดยไคลเอนต์ในขั้นตอนที่ 2.

## Tools

| เครื่องมือ | จุดประสงค์ | เขียนไฟล์ |
| --- | --- | --- |
| `translate_markdown_content` | แปลสตริง Markdown | ไม่ |
| `translate_notebook_content` | แปลเซลล์ Markdown ใน JSON ของโน้ตบุ๊ก | ไม่ |
| `translate_image_content` | แปลข้อความในรูปภาพหนึ่งภาพและคืนข้อมูลรูปภาพเป็น base64 | ตัวเลือก, เฉพาะเมื่อมีการระบุ `output_path` |
| `start_markdown_agent_translation` | เตรียมชิ้น Markdown เพื่อให้เอเจนต์โฮสต์แปลโดยไม่ต้องใช้ข้อมูลรับรอง LLM ของ Co-op Translator | ไม่ |
| `finish_markdown_agent_translation` | ประกอบ Markdown ใหม่จากชิ้นที่เอเจนต์โฮสต์แปลแล้ว | ไม่ |
| `start_notebook_agent_translation` | เตรียมชิ้นเซลล์ Markdown ในโน้ตบุ๊กเพื่อให้เอเจนต์โฮสต์แปล | ไม่ |
| `finish_notebook_agent_translation` | ประกอบ JSON ของโน้ตบุ๊กใหม่จากชิ้นที่เอเจนต์โฮสต์แปลแล้ว | ไม่ |
| `rewrite_markdown_paths` | เขียนเส้นทางเนื้อหา Markdown และ frontmatter ใหม่สำหรับเป้าหมายที่แปลแล้ว | ไม่ |
| `rewrite_notebook_paths` | เขียนเส้นทางภายในเซลล์ Markdown ของโน้ตบุ๊กใหม่ | ไม่ |
| `run_translation` | รันการแปลระดับโปรเจกต์เหมือน CLI | ใช่เมื่อ `dry_run=false` และ `confirm_write=true` |
| `translate_project` | นามแฝงสำหรับความเข้ากันได้กับ `run_translation` | ใช่เมื่อ `dry_run=false` และ `confirm_write=true` |
| `run_review` | รันการตรวจสอบแบบกำหนดได้ | ไม่ |
| `get_configuration_status` | รายงานผู้ให้บริการ LLM และ Vision ที่กำหนดค่าโดยไม่เปิดเผยความลับ | ไม่ |
| `list_supported_languages` | แสดงรายการรหัสภาษาปลายทางที่รองรับ | ไม่ |
| `get_api_overview` | อธิบายเวิร์กโฟลว์และเครื่องมือ MCP ที่มีอยู่ | ไม่ |

## Resources

| ที่อยู่ทรัพยากร | จุดประสงค์ |
| --- | --- |
| `co-op://api` | ภาพรวมเป็น JSON ของเวิร์กโฟลว์และเครื่องมือ. |
| `co-op://supported-languages` | รายการ JSON ของรหัสภาษาที่รองรับ. |
| `co-op://configuration` | สรุปความพร้อมใช้งานของผู้ให้บริการเป็น JSON โดยไม่รวมความลับ. |

## Prompts

| พรอมพ์ | จุดประสงค์ |
| --- | --- |
| `translate_markdown_document_prompt` | แนะนำไคลเอนต์ MCP ผ่านการแปลเนื้อหาและการเขียนเส้นทางใหม่แบบเลือกได้. |
| `agent_assisted_markdown_translation_prompt` | แนะนำไคลเอนต์ MCP ผ่านการแปล Markdown โดยเอเจนต์โฮสต์โดยไม่ต้องใช้ข้อมูลรับรองผู้ให้บริการ LLM ของ Co-op Translator. |
| `translate_repository_prompt` | แนะนำไคลเอนต์ MCP ผ่านการแปลรีโพสิตอรีโดยเริ่มจาก dry-run ก่อน. |

## ตัวอย่างสำหรับคัดลอก-วาง

แปลเนื้อหา Markdown:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

เขียนลิงก์ Markdown ที่แปลแล้วใหม่:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

แปล Markdown ด้วยโมเดลเอเจนต์โฮสต์:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

หลังจากเอเจนต์โฮสต์แปลแต่ละชิ้นที่ส่งกลับมา ให้จบงานด้วยวัตถุ `job` ที่ครบถ้วนซึ่งส่งกลับโดย `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

พรีวิวการแปลรีโพสิตอรี:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Troubleshooting

| ปัญหา | สิ่งที่ควรลอง |
| --- | --- |
| ไคลเอนต์ MCP ไม่สามารถหา `co-op-translator-mcp` ได้. | ใช้พาธของตัวปฏิบัติการ Python แบบเต็มและการกำหนดค่าสำหรับการเช็กเอาต์ซอร์ส `["-m", "co_op_translator.mcp.server"]`. |
| เซิร์ฟเวอร์ปรากฏอยู่แต่การแปลล้มเหลว. | เรียก `get_configuration_status` และยืนยันว่ามีผู้ให้บริการ LLM พร้อมใช้งาน. |
| คุณต้องการการแปล Markdown หรือโน้ตบุ๊กโดยไม่ใช้ข้อมูลรับรองผู้ให้บริการ. | ใช้ `start_markdown_agent_translation` / `finish_markdown_agent_translation` หรือเทียบเท่าสำหรับโน้ตบุ๊กเพื่อให้เอเจนต์โฮสต์แปลชิ้นงาน. |
| การแปลรูปภาพล้มเหลว. | ยืนยันว่าตัวแปร Azure AI Vision ถูกตั้งค่าแล้วและเรียก `get_configuration_status`. |
| การแปลรีโพสิตอรีไม่ได้เขียนไฟล์. | ตั้ง `dry_run=false` และ `confirm_write=true` เฉพาะหลังจากได้รับการอนุมัติจากผู้ใช้โดยชัดแจ้ง. |
| การเปลี่ยนแปลงการกำหนดค่าไคลเอนต์ไม่ปรากฏ. | รีสตาร์ทหรือโหลดไคลเอนต์ MCP ใหม่. |

## หมายเหตุด้านความปลอดภัย

- การเรียกเครื่องมือ MCP ถูกควบคุมโดยโมเดลของแอปโฮสต์ ดังนั้นการแปลรีโพสิตอรีจึงเป็น dry-run ตามค่าเริ่มต้น.
- การแปลรีโพสิตอรีทั้งหมดสามารถสร้าง อัปเดต หรือลบไฟล์จำนวนมากได้ ต้องการการอนุมัติจากผู้ใช้อย่างชัดแจ้งก่อนตั้งค่า `confirm_write=true`.
- เครื่องมือสถานะการกำหนดค่าไม่เคยส่งคืนคีย์ API จุดเชื่อมต่อ หรือค่าลับอื่นๆ.
- การแปลรูปภาพจะคืนข้อมูลรูปภาพเป็น base64 รูปภาพขนาดใหญ่สามารถทำให้การตอบกลับของเครื่องมือมีขนาดใหญ่ได้.
- เครื่องมือเอเจนต์ช่วยส่งคืนชิ้นต้นฉบับและพรอมพ์ไปยังโฮสต์ MCP ใช้งานพวกมันเฉพาะกับเนื้อหาที่ผู้ใช้สบายใจที่จะส่งไปยังโมเดลเอเจนต์โฮสต์นั้นเท่านั้น.