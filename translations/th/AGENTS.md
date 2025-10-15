<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:27:57+00:00",
  "source_file": "AGENTS.md",
  "language_code": "th"
}
-->
# ภาพรวมโครงการ

Co‑op Translator เป็นเครื่องมือบรรทัดคำสั่ง Python และ workflow ของ GitHub Actions สำหรับแปลไฟล์ Markdown, Jupyter notebooks และข้อความในภาพเป็นหลายภาษา โดยจะจัดระเบียบผลลัพธ์ไว้ในโฟลเดอร์แยกตามภาษา และซิงค์การแปลให้ตรงกับเนื้อหาต้นฉบับ โครงการนี้ถูกจัดโครงสร้างเป็นไลบรารีที่จัดการด้วย Poetry พร้อม CLI entry points

### ภาพรวมสถาปัตยกรรม

- จุดเข้า CLI (`translate`, `migrate-links`, `evaluate`) เรียก CLI กลางที่กระจายงานไปยัง flow การแปล, การย้ายลิงก์ และการประเมินผล
- ตัวโหลดคอนฟิกจะอ่าน `.env` และตรวจจับผู้ให้บริการ LLM อัตโนมัติ (Azure OpenAI หรือ OpenAI) และหากร้องขอ จะเลือกผู้ให้บริการ vision (Azure AI Service) สำหรับดึงข้อความจากภาพ
- แกนกลางการแปลดูแล Markdown และ notebooks; pipeline vision จะดึงข้อความจากภาพเมื่อใช้ `-img`
- ผลลัพธ์จะถูกจัดไว้ใน `translations/<lang>/` สำหรับข้อความ และ `translated_images/` สำหรับภาพ โดยคงโครงสร้างเดิมไว้

### เทคโนโลยีและเฟรมเวิร์กหลัก

- Python 3.10–3.12, Poetry สำหรับจัดการแพ็กเกจ
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP และข้อมูล: `httpx`, `pydantic`
- การจัดการภาพ: `pillow`, `opencv-python`, `matplotlib`
- เครื่องมือ: `pytest`, `black`, `ruff`

## คำสั่งติดตั้ง

### ข้อกำหนดเบื้องต้น

- Python 3.10–3.12
- บัญชี Azure (ไม่บังคับ, สำหรับบริการ Azure AI)
- อินเทอร์เน็ตสำหรับเชื่อมต่อ LLM/Vision APIs (เช่น Azure OpenAI/OpenAI, Azure AI Vision)

### ตัวเลือก A: Poetry (แนะนำ)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### ตัวเลือก B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## การใช้งานสำหรับผู้ใช้ปลายทาง

### Docker (อิมเมจที่เผยแพร่แล้ว)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

หมายเหตุ:
- จุดเข้าเริ่มต้นคือ `translate` หากต้องการย้ายลิงก์ให้ใช้ `--entrypoint migrate-links`
- ตรวจสอบให้แน่ใจว่า visibility ของ GHCR package เป็น Public เพื่อให้ดึงแบบไม่ต้องล็อกอินได้

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### การตั้งค่าสภาพแวดล้อม

สร้างไฟล์ `.env` ที่ root ของ repository และระบุข้อมูลรับรอง/endpoint สำหรับ language model ที่เลือกใช้ และ (ถ้าต้องการ) vision service สำหรับการตั้งค่าตามผู้ให้บริการ ดูที่ `getting_started/set-up-azure-ai.md`

### ตัวแปรสภาพแวดล้อมที่จำเป็น

ต้องตั้งค่า LLM provider อย่างน้อยหนึ่งตัว สำหรับการแปลภาพ ต้องตั้งค่า Azure AI Service ด้วย

- Azure OpenAI (แปลข้อความ):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (ทางเลือกสำหรับแปลข้อความ):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (ไม่บังคับ)
  - `OPENAI_CHAT_MODEL_ID` (จำเป็นเมื่อใช้ OpenAI provider)
  - `OPENAI_BASE_URL` (ไม่บังคับ; ค่าเริ่มต้นคือ `https://api.openai.com/v1`)

- Azure AI Service สำหรับดึงข้อความจากภาพ (จำเป็นเมื่อใช้ `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (แนะนำ) หรือ `AZURE_SUBSCRIPTION_KEY` (แบบเก่า)
  - `AZURE_AI_SERVICE_ENDPOINT`

ตัวอย่าง `.env`:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

หมายเหตุ:

- เครื่องมือจะตรวจจับ LLM provider ที่ตั้งค่าไว้โดยอัตโนมัติ; ตั้งค่า Azure OpenAI หรือ OpenAI อย่างใดอย่างหนึ่ง
- การแปลภาพต้องใช้ทั้ง `AZURE_AI_SERVICE_API_KEY` และ `AZURE_AI_SERVICE_ENDPOINT`
- CLI จะแจ้งข้อผิดพลาดชัดเจนหากขาดตัวแปรที่จำเป็น

## เวิร์กโฟลว์สำหรับนักพัฒนา

- โค้ดต้นฉบับอยู่ใน `src/co_op_translator`; โค้ดทดสอบอยู่ใน `tests/`
- CLI หลัก (ติดตั้งผ่าน entry points):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

ดูเอกสารการใช้งานเพิ่มเติมใน `getting_started/`

## คำแนะนำการทดสอบ

รันทดสอบจาก root ของ repository บางเทสอาจต้องใช้ API credentials; ข้ามเทสเหล่านั้นหากจำเป็น

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

ถ้าต้องการดู coverage (ต้องติดตั้ง `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## แนวทางการเขียนโค้ด

- Formatter: Black (ตั้งค่าใน `pyproject.toml`, ความยาวบรรทัด 88)
- Linter: Ruff (ตั้งค่าใน `pyproject.toml`, ความยาวบรรทัด 120)
- ตรวจสอบ type: mypy (มีไฟล์คอนฟิก; เปิดใช้หากติดตั้งแล้ว)

คำสั่ง:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

จัดระเบียบโค้ด Python ไว้ใน `src/`, โค้ดทดสอบใน `tests/` และควรใช้ explicit imports ใน namespace ของแพ็กเกจ (`co_op_translator.*`)

## การ build และการ deploy

ไฟล์ build จะถูกสร้างไว้ใน `dist/`

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

รองรับการทำงานอัตโนมัติผ่าน GitHub Actions; ดูได้ที่:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### อิมเมจคอนเทนเนอร์ (GHCR)

- อิมเมจทางการ: `ghcr.io/azure/co-op-translator:<tag>`
- แท็ก: `latest` (บน main), แท็ก semantic เช่น `vX.Y.Z` และแท็ก `sha`
- รองรับหลายสถาปัตยกรรม: `linux/amd64, linux/arm64` ผ่าน Buildx
- รูปแบบ Dockerfile: สร้าง dependency wheels ใน builder (พร้อม `build-essential` และ `python3-dev`) และติดตั้งจาก wheelhouse ใน runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` จะ build และ push ไปยัง GHCR

## ข้อควรระวังด้านความปลอดภัย

- เก็บ API key และ endpoint ไว้ใน `.env` หรือ CI secrets store; ห้าม commit ข้อมูลลับ
- สำหรับการแปลภาพ ต้องใช้ key/endpoint ของ Azure AI Vision; หากไม่ใช้ ให้ละเว้น `-img`
- ตรวจสอบโควต้า/อัตราการใช้งานของผู้ให้บริการเมื่อแปลจำนวนมาก

## แนวทางการ Pull Request

### ก่อนส่ง PR

1. **ทดสอบการเปลี่ยนแปลงของคุณ:**
   - รัน notebook ที่เกี่ยวข้องจนจบ
   - ตรวจสอบว่า cell ทั้งหมดทำงานได้โดยไม่มี error
   - ตรวจสอบว่า output ถูกต้องเหมาะสม

2. **อัปเดตเอกสาร:**
   - อัปเดต `README.md` หากเพิ่มแนวคิดใหม่
   - เพิ่มคอมเมนต์ใน notebook สำหรับโค้ดที่ซับซ้อน
   - ตรวจสอบว่า markdown cell อธิบายจุดประสงค์ชัดเจน

3. **การเปลี่ยนแปลงไฟล์:**
   - หลีกเลี่ยงการ commit ไฟล์ `.env` (ใช้ `.env.example` แทน)
   - อย่า commit โฟลเดอร์ `venv/` หรือ `__pycache__/`
   - คง output ของ notebook ไว้หากแสดงแนวคิด
   - ลบไฟล์ชั่วคราวและ notebook สำรอง (`*-backup.ipynb`)

4. **รูปแบบและสไตล์:**
   - ปฏิบัติตามแนวทางสไตล์และรูปแบบ
   - รัน `poetry run black .` และ `poetry run ruff check .` เพื่อตรวจสอบปัญหาสไตล์และรูปแบบ

5. **เพิ่ม/อัปเดตเทสและ CLI help:**
   - เพิ่มหรืออัปเดตเทสเมื่อเปลี่ยนพฤติกรรม
   - ให้ CLI help สอดคล้องกับการเปลี่ยนแปลง


### รูปแบบ commit message และกลยุทธ์ merge

เราใช้ Squash and Merge เป็นค่าเริ่มต้น ข้อความ commit หลัง squash ควรเป็นไปตามนี้:

```bash
<type>: <description> (#<PR number>)
```

ประเภทที่อนุญาต:
- `Docs` — อัปเดตเอกสาร
- `Build` — ระบบ build, dependencies, การตั้งค่า/CI
- `Core` — ฟีเจอร์และฟังก์ชันหลัก (เช่น `src/co_op_translator/core`)

ตัวอย่าง:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

หมายเหตุ:
- ชื่อ PR มักจะถูกเติม prefix อัตโนมัติตาม label; ตรวจสอบให้แน่ใจว่า prefix ถูกต้อง

### รูปแบบชื่อ PR

ใช้ชื่อที่ชัดเจน กระชับ และควรใช้โครงสร้างเดียวกับ commit message สุดท้าย:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## การดีบักและแก้ปัญหา

- ปัญหาทั่วไปและวิธีแก้: `getting_started/troubleshooting.md`
- ภาษาที่รองรับและหมายเหตุ (รวมถึงฟอนต์/ปัญหาที่ทราบ): `getting_started/supported-languages.md`
- หากพบปัญหาลิงก์ใน notebook ให้รัน: `migrate-links -l "all" -y` อีกครั้ง

## หมายเหตุสำหรับ Agent

- แนะนำให้ใช้ Poetry เพื่อความสามารถในการทำซ้ำสภาพแวดล้อม; หากไม่ใช้ ให้ใช้ `requirements.txt`
- เมื่อเรียก CLI ใน CI ให้ส่งข้อมูลลับที่จำเป็นผ่าน environment variable หรือ inject `.env`
- สำหรับผู้ใช้แบบ monorepo repo นี้ทำงานเป็นแพ็กเกจเดี่ยว ไม่ต้องประสานกับ sub-package อื่น

- คำแนะนำ multi-arch: ควรรองรับ `linux/arm64` หากมีผู้ใช้ ARM (Apple Silicon/ARM server) เป็นเป้าหมาย; หากไม่ ให้ใช้เฉพาะ `linux/amd64` เพื่อความง่าย
- แนะนำผู้ใช้ไปที่ Docker Quick Start ใน `README.md` หากต้องการใช้ container; ให้รวมตัวอย่างทั้ง Bash และ PowerShell เพราะการ escape อาจต่างกัน

---

**ข้อจำกัดความรับผิดชอบ**:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่เกิดขึ้นจากการใช้การแปลนี้