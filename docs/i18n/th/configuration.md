# การกำหนดค่า

Co-op Translator ต้องการผู้ให้บริการโมเดลภาษาอย่างน้อยหนึ่งราย สำหรับการแปลภาพจะต้องมี Azure AI Vision เพิ่มเติม

การกำหนดค่านี้อ่านจากตัวแปรแวดล้อม สำหรับโปรเจ็กต์ภายในเครื่อง ให้วางไว้ในไฟล์ `.env` ที่รากของโปรเจ็กต์

สำหรับการตั้งค่าทรัพยากร Azure ให้ดูที่ [การตั้งค่า Azure AI](azure-ai-setup.md).

## การตั้งค่าสภาพแวดล้อมรันไทม์ในเครื่อง

ใช้สภาพแวดล้อมเสมือน (virtual environment) ก่อนรัน CLI ในเครื่อง Co-op Translator รองรับ Python 3.11 ถึง 3.14

สำหรับการใช้งาน CLI ปกติ ให้ติดตั้งแพ็กเกจที่เผยแพร่ภายในสภาพแวดล้อมเสมือน:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### การพัฒนาในรีโพซิทอรี

สำหรับการพัฒนารีโพซิทอรี ให้ติดตั้ง dependencies จากรากของโปรเจ็กต์แทน:

```bash
poetry install
poetry run translate --help
```

หลังจากที่ CLI พร้อมใช้งาน ให้กำหนดค่าผู้ให้บริการโมเดลภาษาในไฟล์ `.env`

## การเลือกผู้ให้บริการ

เครื่องมือนี้จะตรวจจับผู้ให้บริการโดยอัตโนมัติตามลำดับต่อไปนี้:

1. Azure OpenAI
2. OpenAI
3. Anthropic

การแปลต้องการข้อมูลรับรองของผู้ให้บริการ ยกเว้นตัวอย่างเช่น `translate -l "ko" -md --dry-run` การทำงาน `migrate-links`, `co-op-review`, และ `run_review` เป็นการดำเนินการบำรุงรักษาที่มีพฤติกรรมกำหนดได้และไม่ต้องการข้อมูลรับรองของผู้ให้บริการ

## แบ็กเอนด์ของไคลเอนต์โมเดล

เริ่มตั้งแต่ Co-op Translator 0.22.0 เป็นต้นไป Azure OpenAI, OpenAI และ Anthropic จะใช้ Microsoft Agent Framework เป็นค่าเริ่มต้น ไม่จำเป็นต้องตั้งค่าแบ็กเอนด์สำหรับการใช้งานปกติ

Semantic Kernel ยังคงใช้งานได้ชั่วคราวเพื่อความเข้ากันได้ หากต้องการเลือกใช้อย่างชัดเจน ให้กำหนดค่าเป็น:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

การใช้ Semantic Kernel จะทำให้เกิดคำเตือนการเลิกใช้ แผนคือจะย้าย Semantic Kernel ไปเป็น dependency แบบไม่บังคับใน 0.23.0 และนำการผนวกรวมออกใน 0.24.0 ขึ้นกับผลการทดสอบความเข้ากันได้และความคิดเห็นจากผู้ใช้ Anthropic ต้องการ `agent-framework`; การเลือก `semantic-kernel` แบบชัดเจนกับ Anthropic จะล้มเหลวพร้อมข้อผิดพลาดการกำหนดค่า ค่าไม่ถูกต้องจะล้มเหลวระหว่างการเริ่มต้นตัวแปลที่พึ่งพาผู้ให้บริการ แทนที่จะตกกลับอย่างเงียบ ๆ ติดตามการเปิดตัวและรายงานปัญหาได้ที่ [ปัญหา GitHub #543](https://github.com/Azure/co-op-translator/issues/543)

## Azure OpenAI

ใช้ Azure OpenAI เมื่อโมเดลของคุณถูกปรับใช้ใน Azure AI Foundry หรือ Azure OpenAI Service

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

การตรวจสอบการเชื่อมต่อจะใช้ endpoint, API key, เวอร์ชันของ API และชื่อ deployment ก่อนที่การแปลจะเริ่มต้น

## OpenAI

ใช้ OpenAI เมื่อเรียก OpenAI API โดยตรง

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` จำเป็นเพราะตัวแปลต้องการ chat model ที่ระบุชัดเจนสำหรับการเรียก API

ปล่อยให้ `OPENAI_ORG_ID` และ `OPENAI_BASE_URL` ไม่ถูกตั้งค่าสำหรับการตั้งค่าเริ่มต้น เพิ่ม organization ID ก็ต่อเมื่อบัญชีของคุณต้องการ หรือเพิ่ม base URL ก็ต่อเมื่อใช้ endpoint ที่กำหนดเอง อย่าคัดลอกค่าตัวอย่าง (placeholder) สำหรับการตั้งค่าแบบไม่บังคับ

## Anthropic Claude

ใช้ Anthropic เมื่อเรียก Claude API โดยตรง สร้าง [คีย์ API ของ Anthropic](https://platform.claude.com/docs/en/get-started) และเลือก [ID โมเดล Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) ที่รองรับ

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` และ `ANTHROPIC_MODEL` จำเป็น ไม่จำเป็นต้องตั้งค่า `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework เป็นแบ็กเอนด์เริ่มต้น

ปล่อยให้ `ANTHROPIC_BASE_URL` ไม่ถูกตั้งค่าสำหรับ Anthropic API ตั้งค่าเฉพาะเมื่อใช้ endpoint ที่กำหนดเอง

`ANTHROPIC_MAX_TOKENS` ตั้งค่าเริ่มต้นเป็น `8192` ซึ่งเผื่อพื้นที่สำหรับสคริปต์ที่หนาแน่นด้วยโทเค็นเช่น Meitei Mayek ลดค่านี้ลงหากโมเดลของคุณหรือ endpoint ที่เข้ากันได้กับ Anthropic จำกัดผลลัพธ์ต่ำกว่านั้น

## Azure AI Vision

การแปลภาพต้องใช้ Azure AI Vision เพื่อให้เครื่องมือสามารถสกัดข้อความจากภาพก่อนที่โมเดลภาษาที่กำหนดจะทำการแปล Anthropic สามารถแปลข้อความที่สกัดได้เช่นเดียวกับ Azure OpenAI หรือ OpenAI

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

หากเลือกการแปลภาพด้วย `-img`, `images=True` หรือไม่มีตัวกรอง content-type เครื่องมือจะตรวจสอบการกำหนดค่า Vision ก่อนที่การแปลจะเริ่มต้น

## ชุดข้อมูลรับรองหลายชุด

ชั้นการกำหนดค่าสนับสนุนชุดข้อมูลรับรองหลายชุดโดยการเติมเลขดัชนีท้ายตัวแปรด้วยค่าเดียวกัน:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

แต่ละชุดต้องครบถ้วน การตรวจสอบสถานะจะเลือกชุดที่ใช้งานได้ก่อนที่การแปลจะดำเนินการต่อ

OpenAI และ Anthropic รองรับคอนเวนชันการเติมท้ายนามเดียวกัน ให้เก็บตัวแปรทั้งหมดในชุดข้อมูลรับรองไว้บนท้ายนามเดียวกัน รวมถึงค่าที่ไม่บังคับเช่น `OPENAI_BASE_URL_1` หรือ `ANTHROPIC_BASE_URL_1`

## ข้อกำหนดของคำสั่ง

| คำสั่งหรือ API | ต้องการ LLM | ต้องการ Vision | หมายเหตุ |
| --- | --- | --- | --- |
| `translate -md` | ใช่ | ไม่ | แปลเฉพาะ Markdown. |
| `translate -nb` | ใช่ | ไม่ | แปลเฉพาะโน้ตบุ๊ก. |
| `translate -img` | ใช่ | ใช่ | แปลเฉพาะภาพ. |
| `translate` เมื่อไม่มีแฟล็กประเภท | ใช่ | ใช่ | โหมดเริ่มต้นรวมถึง Markdown, โน้ตบุ๊ก และภาพ. |
| `evaluate` | ใช่ | ไม่ | ใช้การประเมินโดย LLM ยกเว้นเมื่อเลือก `--fast`. |
| `migrate-links` | ไม่ | ไม่ | ดำเนินการย้ายลิงก์ภายในเครื่องโดยไม่เรียกผู้ให้บริการ. |
| `co-op-review` | ไม่ | ไม่ | ดำเนินการตรวจสอบโครงสร้างการแปลแบบกำหนดได้, ความสดใหม่, Markdown, โน้ตบุ๊ก และลิงก์ภายในเครื่อง. |
| `run_translation(markdown=True)` | ใช่ | ไม่ | การแปล Markdown ผ่านโปรแกรม. |
| `run_translation(images=True)` | ใช่ | ใช่ | การแปลภาพผ่านโปรแกรม. |
| `run_review(...)` | ไม่ | ไม่ | การตรวจสอบแบบกำหนดได้ผ่านโปรแกรม. |

## ไดเร็กทอรีผลลัพธ์

ผลลัพธ์การแปลข้อความเริ่มต้น:

```text
translations/<language-code>/<source-relative-path>
```

ผลลัพธ์การแปลภาพเริ่มต้น:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API สามารถเขียนทับไดเร็กทอรีเหล่านี้ได้ด้วย `translations_dir` และ `image_dir`