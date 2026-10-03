# คู่มือผู้ดูแล

หน้านี้สรุปการเชื่อมต่อระหว่าง API, CLI และไซต์เอกสารเข้าด้วยกัน

## ขอบเขต API สาธารณะ

API ของ Python ที่เสถียรถูกส่งออกจาก:

```python
co_op_translator.api
```

API สาธารณะถูกจัดเป็นตัวช่วยแปลเนื้อหา ตัวช่วยเขียนเส้นทางใหม่ การประสานงานโครงการ และการตรวจทาน:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` เป็นขอบเขตความคงทนสำหรับการรวมระบบแบบโฮสต์
มันต้องเก็บตัวอย่างที่สร้างขึ้นแยกจากฐานอ้างอิงที่ยอมรับไว้ เพื่อไม่ให้
การแปลที่ยังไม่ถูกรวมไม่ควรกลายเป็นแหล่งที่มาของความจริง

เมื่อเพิ่ม API สาธารณะใหม่ ให้ปรับปรุง:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- การทดสอบ API ที่เกี่ยวข้องภายใต้ `tests/co_op_translator/` เช่น `test_api.py` หรือ `test_review_api.py`

หลีกเลี่ยงการจัดทำเอกสารโมดูลระดับล่าง `core` เป็น API ที่เสถียร เว้นแต่โครงการตั้งใจจะรองรับโดยตรง

## จุดเข้าใช้งาน CLI

แพ็กเกจกำหนดสคริปต์ Poetry เหล่านี้:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` จะกระจายโดยชื่อสคริปต์:

- `translate` เรียก `co_op_translator.cli.translate.translate_command`
- `evaluate` เรียก `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` เรียก `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` เรียก `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` ข้าม `__main__.py` และเรียก `co_op_translator.mcp.server:main` โดยตรง

เมื่อเพิ่มหรือเปลี่ยนตัวเลือก CLI ให้ปรับปรุง:

- คำสั่งที่เกี่ยวข้องใน `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- การทดสอบที่เกี่ยวข้องกับ CLI หากพฤติกรรมมีการเปลี่ยนแปลง

## เซิร์ฟเวอร์ MCP

เซิร์ฟเวอร์ MCP ถูกนำไปใช้อยู่ใน:

```python
co_op_translator.mcp.server
```

เซิร์ฟเวอร์จงใจห่อหุ้ม API ของ Python แบบสาธารณะแทนการเรียกโมดูลระดับล่าง `core` ให้รักษาขอบเขตนี้ไว้เพื่อให้ลูกค้า MCP, ตัวเรียกใช้จาก Python และ CLI มีพฤติกรรมเหมือนกัน

เมื่อเพิ่มหรือเปลี่ยนเครื่องมือ MCP ให้ปรับปรุง:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` หากขอบเขตของ API สาธารณะเปลี่ยน

เครื่องมือแปลใน repository สามารถเรียกแบบ model ผ่าน MCP และสามารถเขียนไฟล์จำนวนมากได้ ให้เก็บค่าเริ่มต้น `dry_run=True` และต้องการ `confirm_write=True` ก่อนการแปลโครงการที่ไม่ใช่การ dry-run

## กระบวนการแปล

กระบวนการแปลโครงการระดับสูงคือ:

1. แยกวิเคราะห์อาร์กิวเมนต์ CLI หรือพารามิเตอร์ของ API
2. ตรวจสอบการกำหนดค่า LLM ด้วย `LLMConfig`
3. ตรวจสอบ Azure AI Vision เมื่อเลือกการแปลภาพ
4. ทำให้รหัสภาษาเป็นมาตรฐาน
5. ตรวจจับนามแฝงของโฟลเดอร์ภาษาแบบเก่า
6. ประมาณปริมาณการแปล
7. อัปเดตส่วนภาษา/คอร์สใน README เมื่อเหมาะสม
8. มอบหมายการแปลโครงการให้ `ProjectTranslator`
9. `ProjectTranslator` มอบหมายการประมวลผลไฟล์ให้ `TranslationManager`

`TranslationManager` ประกอบด้วย mixin สำหรับแต่ละประเภทไฟล์:

- `ProjectMarkdownTranslationMixin` จัดการการอ่านไฟล์ Markdown, การแปลเนื้อหา, การเขียนเส้นทางใหม่, เมตาดาต้า, ข้อจำกัดความรับผิดชอบ และการเขียนไฟล์
- `ProjectNotebookTranslationMixin` จัดการการอ่านไฟล์โน้ตบุ๊ก, การแปลเซลล์ Markdown, การเขียนเส้นทางใหม่, เมตาดาต้า, ข้อจำกัดความรับผิดชอบ และการเขียนไฟล์
- `ProjectImageTranslationMixin` จัดการการค้นหารูปภาพ, การสกัด/แปลข้อความ, การเขียนภาพที่เรนเดอร์แล้ว และเมตาดาต้า

API เนื้อหาระดับล่างข้ามเวิร์กโฟลว์โครงการ:

1. `translate_markdown_content` และ `translate_notebook_content` แปลเนื้อหาในหน่วยความจำเท่านั้น
2. `translate_image_content` แปลข้อความในภาพเดียวและส่งคืนวัตถุภาพที่เรนเดอร์แล้ว
3. `rewrite_markdown_paths` และ `rewrite_notebook_paths` เป็นตัวช่วยหลังการประมวลผลแบบชัดเจน พวกมันไม่ทำการแปลและไม่เขียนไฟล์ของโครงการ

## กระบวนการตรวจทาน

กระบวนการตรวจทานเชิงกำหนดคือ:

1. แยกวิเคราะห์อาร์กิวเมนต์ CLI หรือพารามิเตอร์ของ API
2. ทำให้รหัสภาษาที่ร้องขอเป็นมาตรฐาน
3. สร้างเป้าหมายการตรวจทานหนึ่งหรือหลายรายการจาก `root_dir`, `root_dirs` หรือ `groups`
4. จำกัดไฟล์ต้นทางได้ตามต้องการด้วย `--changed-from`
5. รันการตรวจสอบแบบกำหนดสำหรับโครงสร้าง ความสดของการแปล ความสมบูรณ์ของ Markdown และเส้นทางลิงก์/รูปภาพภายในเครื่อง
6. พิมพ์เป็นเอาต์พุตข้อความหรือ Markdown แบบ GitHub-flavored
7. ออกด้วยความล้มเหลวเมื่อพบข้อผิดพลาดในการตรวจทาน

กระบวนการตรวจทานไม่ต้องใช้คีย์ API และยังสามารถใช้งานได้สำหรับการตรวจสอบในเครื่องหรือ CI ของผู้ใช้แบบเลือกเข้าร่วม รีโพซิทอรีนี้ไม่รัน `co-op-review` โดยอัตโนมัติในทุก pull request

## เว็บไซต์เอกสาร

ไซต์เอกสารถูกกำหนดค่าโดย:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

ไดเรกทอรี `docs/` เป็นแหล่งเอกสารอ้างอิงหลัก อย่าเพิ่มคู่มือสำหรับผู้ใช้ใหม่นอกไดเรกทอรีนี้ เว้นแต่โครงการตั้งใจจะเพิ่มพื้นผิวเอกสารที่เผยแพร่อื่นๆ

สร้างในเครื่อง:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

พรีวิวในเครื่อง:

```bash
python -m mkdocs serve
```

ไซต์ที่สร้างขึ้นจะถูกเขียนไปที่ `site/` ซึ่งถูกละเว้นโดย git

## เวิร์กโฟลว์ GitHub Pages

`.github/workflows/docs.yml` สร้างไซต์เมื่อมี pull request และปรับใช้เมื่อ push ไปยัง `main`

เวิร์กโฟลว์ติดตั้ง:

```bash
pip install -r requirements-docs.txt
```

เวิร์กโฟลว์เอกสารติดตั้งเพียง toolchain สำหรับเอกสารเท่านั้น `mkdocs.yml` ชี้ `mkdocstrings` ไปที่ `src/` เพื่อให้หน้าของ API สาธารณะสามารถเรนเดอร์จากต้นไม้ของซอร์สโดยไม่ต้องติดตั้งชุด dependency ของ runtime ทั้งหมด หากเอกสาร API ในอนาคตต้องการนำเข้า optional runtime providers ระหว่างการ build ให้ปรับปรุงทั้ง `.github/workflows/docs.yml` และคู่มือนี้พร้อมกัน

## เกณฑ์คุณภาพเอกสาร

ก่อนจะรวมการเปลี่ยนแปลงเอกสาร ให้รัน:

```bash
python -m mkdocs build --strict
git diff --check
```

ใช้การ build แบบเข้มงวดเพื่อให้ลิงก์เสีย รายการนำทางที่ไม่ถูกต้อง และปัญหาการเรนเดอร์ API ล้มเหลวตั้งแต่เนิ่นๆ