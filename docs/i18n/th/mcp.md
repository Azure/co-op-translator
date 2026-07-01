# MCP เซิร์ฟเวอร์

Co-op Translator รวมเซิร์ฟเวอร์ Model Context Protocol สำหรับเอเยนต์ บรรณาธิการ และไคลเอนต์ที่เข้ากันได้กับ MCP

สำหรับการตั้งค่าเริ่มต้นแบบโลคัล ผู้ใช้จะไม่ต้องรันเซิร์ฟเวอร์แยกต่างหากด้วยตนเอง พวกเขากำหนดค่าไคลเอนต์ MCP ของตน แล้วไคลเอนต์จะเริ่ม `co-op-translator-mcp` โดยอัตโนมัติผ่าน `stdio` เมื่อจำเป็นต้องใช้เครื่องมือของ Co-op Translator

หากคุณกำลังตัดสินใจระหว่าง CLI, Python API และ MCP ให้เริ่มจาก [เลือกเวิร์กโฟลว์ของคุณ](workflows.md)

ใช้ MCP เมื่อเอเยนต์หรือบรรณาธิการควรเรียก Co-op Translator โดยตรง:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

เซิร์ฟเวอร์ MCP ห่อหุ้ม public Python API เดียวกันที่มีเอกสารใน [Python API](api.md) เครื่องมือที่พึ่งพาผู้ให้บริการใช้ผู้ให้บริการที่กำหนดค่าไว้เดียวกับ CLI และ Python API เครื่องมือที่ช่วยโดยเอเยนต์เตรียมชิ้นส่วนสำหรับเอเยนต์โฮสต์ของ MCP เพื่อแปล แล้วใช้ Co-op Translator เพื่อประกอบ Markdown หรือโน้ตบุ๊กสุดท้าย

## ขั้นตอนที่ 1: ติดตั้งและกำหนดค่า Co-op Translator

ติดตั้ง Co-op Translator ในสภาพแวดล้อม Python ที่ไคลเอนต์ MCP ของคุณจะใช้:

```bash
pip install co-op-translator
```

สำหรับการพัฒนาในเครื่องจากที่เก็บนี้ ให้ติดตั้งแพ็กเกจในโหมดแก้ไขได้:

```bash
pip install -e .
```

เลือกโหมดการแปลที่ไคลเอนต์ MCP ของคุณจะใช้:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation require Azure OpenAI or OpenAI. Image translation also requires Azure AI Vision. |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | No Co-op Translator LLM provider credentials are required for Markdown or notebook chunks. Image translation is not covered by agent-assisted mode yet. |

หากคุณเริ่มจากการแปล Markdown หรือโน้ตบุ๊กภายในเอเยนต์ เช่น Codex หรือ Claude Code ให้เริ่มด้วยโหมดเอเยนต์ช่วยเหลือ ใช้โหมดที่พึ่งพาผู้ให้บริการเมื่อคุณต้องการให้ Co-op Translator เรียกผู้ให้บริการที่คุณกำหนดค่าเอง เมื่อคุณกำลังแปลรูปภาพ หรือเมื่อคุณกำลังรันการแปลในระดับรีโพซิทอรีเหมือน CLI

กำหนดค่า credentials ของผู้ให้บริการเฉพาะสำหรับเวิร์กโฟลว์ที่พึ่งพาผู้ให้บริการเท่านั้น:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

การแปลภาพที่พึ่งพาผู้ให้บริการยังต้องการ:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## ขั้นตอนที่ 2: กำหนดค่าไคลเอนต์ MCP ของคุณ

สำหรับการตั้งค่า `stdio` ปกติในเครื่อง ให้เพิ่ม Co-op Translator ลงในการกำหนดค่าไคลเอนต์ MCP ของคุณ ไคลเอนต์จะเริ่มและหยุดกระบวนการโดยอัตโนมัติ

การกำหนดค่าจากแพ็กเกจที่ติดตั้ง:

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

การกำหนดค่าจากการเช็คเอาต์ซอร์สบน Windows:

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

การกำหนดค่าจากการเช็คเอาต์ซอร์สบน macOS หรือ Linux:

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

หลังจากเปลี่ยนการกำหนดค่าไคลเอนต์ MCP ให้รีสตาร์ทหรือโหลดใหม่ไคลเอนต์เพื่อให้ค้นพบเซิร์ฟเวอร์ใหม่

## ขั้นตอนที่ 3: ตรวจสอบเซิร์ฟเวอร์ในไคลเอนต์

ให้ไคลเอนต์ MCP รายการเครื่องมือที่มีอยู่ หรือเรียกหนึ่งใน helper แบบอ่านอย่างเดียวก่อน:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

การตรวจสอบเบื้องต้นที่มีประโยชน์:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | ยืนยันว่าเซิร์ฟเวอร์เข้าถึงได้และแสดงเวิร์กโฟลว์ที่ใช้งานได้ |
| `list_supported_languages` | ยืนยันว่าสามารถโหลดข้อมูลภาษาที่บรรจุมาได้ |
| `get_configuration_status` | ยืนยันความพร้อมของผู้ให้บริการ LLM และ Vision โดยไม่เปิดเผยค่าลับ |

## ขั้นตอนที่ 4: เลือกเวิร์กโฟลว์

### แปลไฟล์หรือเอกสารเดี่ยว

ใช้เครื่องมือเนื้อหาที่พึ่งพาผู้ให้บริการเมื่อไคลเอนต์ MCP มีเนื้อหาเอกสารหรือเส้นทางรูปภาพแล้ว และต้องการให้ Co-op Translator เรียกผู้ให้บริการการแปลที่กำหนดไว้

สำหรับ Markdown:

1. เรียก `translate_markdown_content` พร้อม `document`, `language_code`, และไม่บังคับ `source_path`
2. หากผลลัพธ์การแปลจะถูกเขียนลงในเลเอาต์เอาต์พุตของ Co-op Translator ให้เรียก `rewrite_markdown_paths`
3. ให้ไคลเอนต์เขียนหรือส่งคืน `content` สุดท้าย

สำหรับโน้ตบุ๊ก:

1. เรียก `translate_notebook_content` พร้อม JSON ของโน้ตบุ๊กและ `language_code`
2. เรียก `rewrite_notebook_paths` หากลิงก์ในโน้ตบุ๊กที่แปลแล้วจำเป็นต้องปรับสำหรับเส้นทางเป้าหมาย
3. เขียนหรือส่งคืน JSON โน้ตบุ๊กสุดท้าย

สำหรับรูปภาพ:

1. เรียก `translate_image_content` พร้อม `image_path`, `language_code`, และไม่บังคับ `root_dir` หรือ `fast_mode`
2. อ่าน `data_base64` และ `mime_type` ที่ส่งกลับมา
3. หากมีการระบุ `output_path` รูปภาพที่แปลแล้วจะถูกบันทึกไปยังเส้นทางนั้นด้วย

เครื่องมือเนื้อหาไม่ทำการค้นหาโปรเจกต์ อัปเดตเมตาดาต้า ข้อจำกัดความรับผิดชอบ หรือการเขียนเส้นทางอัตโนมัติ หากคุณต้องการให้เอเยนต์โฮสต์แปลชิ้นส่วนของ Markdown หรือโน้ตบุ๊กโดยไม่ต้องใช้ credentials ผู้ให้บริการ LLM ของ Co-op Translator ให้ใช้เวิร์กโฟลว์เอเยนต์ช่วยเหลือด้านล่าง

### แปลด้วยโมเดลเอเยนต์โฮสต์

ใช้เครื่องมือเอเยนต์ช่วยเหลือเมื่อคุณต้องการให้เอเยนต์โฮสต์ของ MCP เช่น ผู้ช่วยเขียนโค้ด ผลิตข้อความที่แปลแทนการกำหนดค่า Azure OpenAI หรือ OpenAI สำหรับ Co-op Translator

ในไคลเอนต์ MCP แบบแชท โดยปกติคุณไม่จำเป็นต้องเขียน JSON ของเครื่องมือด้วยตนเอง ขอให้เอเยนต์ใช้เวิร์กโฟลว์เอเยนต์ช่วยเหลือ:

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

ถ้าไคลเอนต์ MCP ของคุณรองรับ server prompts ให้ใช้ `agent_assisted_markdown_translation_prompt` เพื่อให้ไคลเอนต์โหลดคำแนะนำเวิร์กโฟลว์เดียวกัน

สำหรับ Markdown:

1. เรียก `start_markdown_agent_translation` พร้อม `document`, `language_code`, และไม่บังคับ `source_path`
2. แปลแต่ละชิ้นส่วนที่ส่งกลับมาในเอเยนต์โฮสต์โดยทำตาม `prompt` ของชิ้นส่วนนั้น
3. เรียก `finish_markdown_agent_translation` พร้อม `job` ต้นฉบับและชิ้นส่วนที่แปลโดยใช้ `chunk_id` และ `translated_text`
4. หากเนื้อหาจะถูกเขียนไปยังเส้นทางเป้าหมายที่แปลแล้ว ให้เรียก `rewrite_markdown_paths`

สำหรับโน้ตบุ๊ก:

1. เรียก `start_notebook_agent_translation` พร้อม JSON ของโน้ตบุ๊กและ `language_code`
2. แปลแต่ละชิ้นส่วนที่ส่งกลับมาในเอเยนต์โฮสต์
3. เรียก `finish_notebook_agent_translation` พร้อม `job` ต้นฉบับและชิ้นส่วนที่แปล
4. เรียก `rewrite_notebook_paths` หากลิงก์ในโน้ตบุ๊กที่แปลแล้วต้องปรับเส้นทางเป้าหมาย

เครื่องมือเอเยนต์ช่วยเหลือจะไม่เรียก Azure OpenAI หรือ OpenAI จาก Co-op Translator เอเยนต์โฮสต์รับผิดชอบการแปลชิ้นส่วนนั้น Co-op Translator ดูแลการแบ่งชิ้นส่วน Markdown การรักษาตำแหน่งสำรอง การประกอบ frontmatter ใหม่ การแทนที่เซลล์โน้ตบุ๊ก และการทำให้เป็นปกติหลังการแปล

### แปลทั้งรีโพซิทอรี

ใช้ `run_translation` เมื่อผู้ใช้ต้องการให้ Co-op Translator ทำงานเหมือน CLI `translate`

การแปลรีโพซิทอรีจะตั้งค่าเริ่มต้นเป็น `dry_run=true` เพื่อให้เอเยนต์สามารถตรวจสอบขอบเขตก่อนเปลี่ยนแปลงไฟล์:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

เพื่ออนุญาตการเขียน ผู้เรียกต้องตั้งค่า `dry_run=false` และ `confirm_write=true` ทั้งสองค่าด้วย:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` ถูกเปิดเผยเป็นนามแฝงที่เข้ากันได้สำหรับ `run_translation`

### ตรวจทานผลลัพธ์การแปล

ใช้ `run_review` สำหรับการตรวจสอบแบบกำหนดค่าได้ที่ไม่ต้องการ credentials ของ LLM หรือ Vision

!!! note "Beta"
    MCP exposes the beta `run_review` API. It is safe for read-only review workflows, but review checks and issue schemas may evolve.

ผลลัพธ์รวมถึงเอาต์พุตข้อความที่จับได้และสรุปการตรวจทานเชิงโครงสร้างเมื่อมีให้

## การรันเซิร์ฟเวอร์ด้วยตนเอง

การรันด้วยตนเองส่วนใหญ่สำหรับการดีบักหรือสำหรับทรานสปอร์ตที่ทำงานเหมือนเซิร์ฟเวอร์ยาวนาน

ดีบักเซิร์ฟเวอร์ stdio เริ่มต้น:

```bash
co-op-translator-mcp
```

รันจากการเช็คเอาต์ซอร์ส:

```bash
python -m co_op_translator.mcp.server
```

รันเซิร์ฟเวอร์ HTTP หรือ SSE ที่ทำงานยาวนาน:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

สำหรับการรวมกับบรรณาธิการท้องถิ่นและเอเยนต์ ให้ใช้การกำหนดค่า `stdio` ที่จัดการโดยไคลเอนต์ในขั้นตอนที่ 2

## เครื่องมือ

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Translate Markdown cells in notebook JSON. | No |
| `translate_image_content` | Translate text in one image and return base64 image data. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | Prepare Markdown chunks for the host agent to translate without Co-op Translator LLM credentials. | No |
| `finish_markdown_agent_translation` | Reconstruct Markdown from host-agent translated chunks. | No |
| `start_notebook_agent_translation` | Prepare notebook Markdown-cell chunks for the host agent to translate. | No |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON from host-agent translated chunks. | No |
| `rewrite_markdown_paths` | Rewrite Markdown body and frontmatter paths for a translated target. | No |
| `rewrite_notebook_paths` | Rewrite paths inside notebook Markdown cells. | No |
| `run_translation` | Run project-level translation like the CLI. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Run deterministic review checks. | No |
| `get_configuration_status` | Report configured LLM and Vision providers without exposing secrets. | No |
| `list_supported_languages` | List supported target language codes. | No |
| `get_api_overview` | Describe available MCP workflows and tools. | No |

## แหล่งข้อมูล

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## พรอมต์

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## ตัวอย่างคัดลอก-วาง

Translate Markdown content:

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

Rewrite translated Markdown links:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

Translate Markdown with the host agent model:

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

After the host agent translates each returned chunk, finish the job with the complete `job` object returned by `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Preview repository translation:

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

## การแก้ปัญหา

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## ข้อควรระวังด้านความปลอดภัย

- การเรียกเครื่องมือ MCP ถูกควบคุมโดยโมเดลผ่านแอปพลิเคชันโฮสต์ ดังนั้นการแปลรีโพซิทอรีจะเป็น dry-run โดยค่าเริ่มต้น
- การแปลรีโพซิทอรีเต็มรูปแบบสามารถสร้าง อัปเดต หรือลบไฟล์จำนวนมาก ต้องการการอนุมัติจากผู้ใช้โดยชัดเจนก่อนตั้งค่า `confirm_write=true`
- เครื่องมือสถานะการกำหนดค่าไม่เคยส่งคืนคีย์ API, endpoints, หรือค่าอื่น ๆ ที่เป็นความลับ
- การแปลรูปภาพส่งคืนข้อมูลรูปภาพเป็น base64 รูปภาพขนาดใหญ่สามารถสร้างการตอบสนองของเครื่องมือที่มีขนาดใหญ่ได้
- เครื่องมือเอเยนต์ช่วยเหลือส่งคืนชิ้นส่วนต้นฉบับและพรอมต์ไปยังโฮสต์ของ MCP ใช้เฉพาะกับเนื้อหาที่ผู้ใช้ยินดีส่งไปยังโมเดลเอเยนต์โฮสต์นั้นเท่านั้น