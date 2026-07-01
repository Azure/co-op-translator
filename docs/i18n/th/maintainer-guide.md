# คู่มือผู้ดูแล

หน้านี้สรุปการเชื่อมโยงระหว่าง API, CLI และเว็บไซต์เอกสาร

## ขอบเขต API สาธารณะ

The stable Python API is exported from:

```python
co_op_translator.api
```

API สาธารณะถูกจัดเป็นชุดช่วยสำหรับการแปลเนื้อหา, ชุดช่วยสำหรับการเขียนทับเส้นทาง, การประสานงานโครงการ และการตรวจทาน:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

เมื่อเพิ่ม API สาธารณะใหม่ ให้ปรับปรุง:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

หลีกเลี่ยงการจัดทำเอกสารโมดูลระดับต่ำกว่า `core` เป็น API ที่เสถียร เว้นแต่โครงการมีเจตนาจะสนับสนุนโดยตรง

## จุดเข้าใช้งาน CLI

The package defines these Poetry scripts:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` dispatches by script name:

- `translate` เรียก `co_op_translator.cli.translate.translate_command`
- `evaluate` เรียก `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` เรียก `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` เรียก `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` ข้าม `__main__.py` และเรียก `co_op_translator.mcp.server:main` โดยตรง.

เมื่อเพิ่มหรือเปลี่ยนตัวเลือก CLI ให้ปรับปรุง:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- CLI-related tests, if behavior changes

## เซิร์ฟเวอร์ MCP

The MCP server is implemented in:

```python
co_op_translator.mcp.server
```

เซิร์ฟเวอร์ตั้งใจทำหน้าที่ห่อหุ้ม API Python สาธารณะแทนที่จะเรียกใช้โมดูลระดับต่ำกว่า `core` ให้รักษาขอบเขตนี้ไว้เพื่อให้ไคลเอนต์ MCP, ผู้เรียกผ่าน Python และ CLI มีพฤติกรรมร่วมกัน

เมื่อเพิ่มหรือเปลี่ยนเครื่องมือ MCP ให้ปรับปรุง:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Repository translation tools are model-callable through MCP and can write many files. Keep `dry_run=True` as the default and require `confirm_write=True` before non-dry-run project translation.

## กระบวนการแปล

The high-level project translation flow is:

1. แยกวิเคราะห์อาร์กิวเมนต์ CLI หรือพารามิเตอร์ API.
2. ตรวจสอบการกำหนดค่า LLM ด้วย `LLMConfig`.
3. ตรวจสอบ Azure AI Vision เมื่อเลือกการแปลภาพ
4. ปรับรูปแบบรหัสภาษาให้เป็นมาตรฐาน.
5. ตรวจจับนามแฝงโฟลเดอร์ภาษารุ่นเก่า.
6. ประเมินปริมาณการแปล.
7. อัปเดต README language/course sections เมื่อเหมาะสม.
8. มอบหมายการแปลโครงการให้ `ProjectTranslator`.
9. `ProjectTranslator` มอบหมายการประมวลผลไฟล์ให้ `TranslationManager`.

`TranslationManager` ประกอบด้วยมิกซ์อินสำหรับประเภทไฟล์เฉพาะ:

- `ProjectMarkdownTranslationMixin` รับผิดชอบการอ่านไฟล์ Markdown, การแปลเนื้อหา, การเขียนทับเส้นทาง, เมตาดาต้า, ข้อปฏิเสธความรับผิดชอบ, และการเขียนไฟล์.
- `ProjectNotebookTranslationMixin` รับผิดชอบการอ่านไฟล์โน้ตบุ๊ก, การแปลเซลล์ Markdown, การเขียนทับเส้นทาง, เมตาดาต้า, ข้อปฏิเสธความรับผิดชอบ, และการเขียนไฟล์.
- `ProjectImageTranslationMixin` รับผิดชอบการค้นหารูปภาพ, การสกัด/แปลข้อความ, การเขียนภาพที่เรนเดอร์แล้ว, และเมตาดาต้า.

API เนื้อหาระดับล่างจะข้ามกระบวนการของโครงการ:

1. ฟังก์ชัน `translate_markdown_content` และ `translate_notebook_content` แปลเฉพาะเนื้อหาในหน่วยความจำเท่านั้น.
2. ฟังก์ชัน `translate_image_content` แปลข้อความในภาพเดียวและส่งกลับออบเจกต์ภาพที่เรนเดอร์แล้ว.
3. ฟังก์ชัน `rewrite_markdown_paths` และ `rewrite_notebook_paths` เป็นตัวช่วยสำหรับขั้นตอนหลังการประมวลผลอย่างชัดเจน พวกมันไม่ทำการแปลและไม่เขียนไฟล์โครงการใด ๆ.

## กระบวนการตรวจทาน

กระบวนการตรวจทานที่มีผลลัพธ์แน่นอนมีดังนี้:

1. แยกวิเคราะห์อาร์กิวเมนต์ CLI หรือพารามิเตอร์ API.
2. ปรับรูปแบบรหัสภาษาที่ร้องขอให้เป็นมาตรฐาน.
3. สร้างเป้าหมายการตรวจทานหนึ่งหรือหลายรายการจาก `root_dir`, `root_dirs`, หรือ `groups`.
4. จำกัดไฟล์ต้นทางโดยเลือกได้ด้วย `--changed-from`.
5. รันการตรวจสอบแบบมีผลลัพธ์แน่นอนสำหรับโครงสร้าง, ความทันสมัยของการแปล, ความสมบูรณ์ของ Markdown, และเส้นทางลิงก์/ภาพท้องถิ่น.
6. พิมพ์เอาต์พุตเป็นข้อความหรือ Markdown แบบ GitHub-flavored.
7. ออกด้วยสถานะล้มเหลวเมื่อพบข้อผิดพลาดในการตรวจทาน.

กระบวนการตรวจทานไม่ต้องการคีย์ API และควรยังคงเหมาะสำหรับ CI ของ pull request. เวิร์กโฟลว์ pull request เขียนสรุปการตรวจสอบในทุกการรันและจะโพสต์คอมเมนต์บน PR เฉพาะเมื่อ `co-op-review` ล้มเหลว.

## เว็บไซต์เอกสาร

The docs site is configured by:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

ไดเรกทอรี `docs/` เป็นแหล่งเอกสารที่เป็นมาตรฐานหลัก อย่าเพิ่มคำแนะนำสำหรับผู้ใช้ใหม่ภายนอกไดเรกทอรีนี้ เว้นแต่โครงการตั้งใจจะนำเสนอแหล่งเอกสารที่เผยแพร่อื่น

สร้างในเครื่อง:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

ดูตัวอย่างในเครื่อง:

```bash
python -m mkdocs serve
```

ไซต์ที่สร้างขึ้นจะถูกเขียนไปยัง `site/` ซึ่งถูกละเว้นโดย git.

## เวิร์กโฟลว์ GitHub Pages

.github/workflows/docs.yml สร้างไซต์เมื่อเกิด pull request และปรับใช้เมื่อ push ไปยัง `main`.

เวิร์กโฟลว์ติดตั้ง:

```bash
pip install -r requirements-docs.txt
```

เวิร์กโฟลว์เอกสารติดตั้งเฉพาะชุดเครื่องมือเอกสารเท่านั้น `mkdocs.yml` ชี้ `mkdocstrings` ไปที่ `src/` เพื่อให้หน้าของ API สาธารณะสามารถเรนเดอร์จากต้นไม้ซอร์สได้โดยไม่ต้องติดตั้งชุดการพึ่งพา runtime ทั้งหมด หากเอกสาร API ในอนาคตต้องการการนำเข้าผู้ให้บริการ runtime แบบเลือกได้ในระหว่างการสร้าง ให้ปรับปรุงทั้ง `.github/workflows/docs.yml` และคู่มือนี้พร้อมกัน.

## มาตรฐานคุณภาพเอกสาร

ก่อนจะรวมการเปลี่ยนแปลงเอกสาร ให้รัน:

```bash
python -m mkdocs build --strict
git diff --check
```

ใช้การสร้างแบบเข้มงวดเพื่อให้ลิงก์ที่เสีย รายการการนำทางที่ไม่ถูกต้อง และปัญหาการเรนเดอร์ API ล้มเหลวตั้งแต่เนิ่นๆ.