# การกำหนดค่า

Co-op Translator ต้องการผู้ให้บริการโมเดลภาษาอย่างน้อยหนึ่งราย สำหรับการแปลภาพจะต้องมี Azure AI Vision เพิ่มด้วย

การกำหนดค่าถูกอ่านจากตัวแปรแวดล้อม สำหรับโปรเจกต์ในเครื่อง ให้วางไว้ในไฟล์ `.env` ที่รากโปรเจกต์

สำหรับการตั้งค่าทรัพยากร Azure ดูที่ [Azure AI Setup](azure-ai-setup.md).

## การตั้งค่าสำหรับรันในเครื่อง

ใช้สภาพแวดล้อมเสมือน (virtual environment) ก่อนรัน CLI ในเครื่อง Co-op Translator รองรับ Python 3.10 ถึง 3.12

สำหรับการใช้งาน CLI ปกติ ให้ติดตั้งแพ็กเกจที่เผยแพร่ภายในสภาพแวดล้อมเสมือน:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

สำหรับการพัฒนาใน repository ให้ติดตั้ง dependencies จากรากโปรเจกต์แทน:

```bash
poetry install
poetry run translate --help
```

หลังจาก CLI พร้อมใช้งาน ให้กำหนดค่าผู้ให้บริการโมเดลภาษาอย่างน้อยหนึ่งรายใน `.env`

## การเลือกผู้ให้บริการ

เครื่องมือจะตรวจจับผู้ให้บริการโดยอัตโนมัติตามลำดับต่อไปนี้:

1. Azure OpenAI
2. OpenAI

หากไม่ได้กำหนดค่าผู้ให้บริการทั้งสอง รายการ `translate`, `evaluate`, `migrate-links`, และ `run_translation` จะล้มเหลวระหว่างการตรวจสอบการกำหนดค่า `co-op-review` และ `run_review` เป็นการตรวจสอบบำรุงรักษาที่ให้ผลลัพธ์แน่นอนและไม่ต้องการข้อมูลประจำตัวของผู้ให้บริการ

## Azure OpenAI

ใช้ Azure OpenAI เมื่อโมเดลของคุณถูกปรับใช้งานใน Azure AI Foundry หรือ Azure OpenAI Service

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

การตรวจสอบการเชื่อมต่อจะใช้ endpoint, API key, API version, และชื่อการปรับใช้งานก่อนเริ่มการแปล

## OpenAI

ใช้ OpenAI เมื่อต้องเรียก OpenAI API โดยตรง

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # ไม่บังคับ
OPENAI_BASE_URL="..."        # ไม่บังคับ
```

`OPENAI_CHAT_MODEL_ID` จำเป็นเพราะตัวแปลต้องการโมเดลแชทที่ชัดเจนสำหรับการเรียก API

## Azure AI Vision

การแปลภาพต้องใช้ Azure AI Vision เพื่อให้เครื่องมือสามารถสกัดข้อความจากภาพก่อนแปล

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

หากเลือกการแปลภาพด้วย `-img`, `images=True`, หรือไม่มีตัวกรองประเภทเนื้อหา เครื่องมือจะตรวจสอบการกำหนดค่า Vision ก่อนเริ่มการแปล

## ชุดข้อมูลประจำตัวหลายชุด

ชั้นกำหนดค่าสนับสนุนชุดข้อมูลประจำตัวหลายชุดโดยการเติมตัวเลขดัชนีเดียวกันต่อท้ายตัวแปร:

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

แต่ละชุดต้องสมบูรณ์ การตรวจสอบสถานะจะเลือกชุดที่ใช้งานได้ก่อนดำเนินการแปลต่อ

## ข้อกำหนดของคำสั่ง

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | Yes | No | แปลเฉพาะ Markdown เท่านั้น. |
| `translate -nb` | Yes | No | แปลเฉพาะโน้ตบุ๊กเท่านั้น. |
| `translate -img` | Yes | Yes | แปลเฉพาะภาพเท่านั้น. |
| `translate` with no type flags | Yes | Yes | โหมดเริ่มต้นรวม Markdown, โน้ตบุ๊ก และภาพ. |
| `evaluate` | Yes | No | ใช้การประเมินด้วย LLM เว้นแต่เลือก `--fast`. |
| `migrate-links` | Yes | No | ทำการย้ายลิงก์ แต่ยังคงเรียกการตรวจสอบการกำหนดค่าที่ใช้ร่วมกัน. |
| `co-op-review` | No | No | ดำเนินการตรวจสอบการบำรุงรักษาที่ให้ผลลัพธ์แน่นอน: โครงสร้างการแปล, ความสดของเนื้อหา, การตรวจสอบ Markdown และโน้ตบุ๊ก รวมถึงลิงก์ภายในเครื่อง. |
| `run_translation(markdown=True)` | Yes | No | การแปล Markdown แบบโปรแกรม. |
| `run_translation(images=True)` | Yes | Yes | การแปลภาพแบบโปรแกรม. |
| `run_review(...)` | No | No | การทบทวนแบบ deterministic แบบโปรแกรม. |

## ไดเรกทอรีผลลัพธ์

ผลลัพธ์การแปลข้อความเริ่มต้น:

```text
translations/<language-code>/<source-relative-path>
```

ผลลัพธ์การแปลภาพเริ่มต้น:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API สามารถแทนที่ไดเรกทอรีเหล่านี้ด้วย `translations_dir` และ `image_dir`