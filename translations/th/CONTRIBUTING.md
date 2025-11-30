<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:15:26+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "th"
}
-->
# การมีส่วนร่วมกับ Co-op Translator

โปรเจกต์นี้ยินดีต้อนรับการมีส่วนร่วมและข้อเสนอแนะต่าง ๆ โดยส่วนใหญ่แล้วการมีส่วนร่วมจะต้องให้คุณยอมรับข้อตกลง Contributor License Agreement (CLA) เพื่อยืนยันว่าคุณมีสิทธิ์และได้ให้สิทธิ์เราในการใช้ผลงานของคุณ รายละเอียดเพิ่มเติมดูได้ที่ https://cla.opensource.microsoft.com

เมื่อคุณส่ง pull request จะมีบอท CLA ตรวจสอบโดยอัตโนมัติว่าคุณต้องยื่น CLA หรือไม่ และจะแสดงสถานะหรือคอมเมนต์ใน PR ให้คุณทำตามคำแนะนำของบอท ซึ่งคุณจะต้องทำขั้นตอนนี้เพียงครั้งเดียวสำหรับทุก repo ที่ใช้ CLA ของเรา

## การตั้งค่าสภาพแวดล้อมสำหรับการพัฒนา

สำหรับการตั้งค่าสภาพแวดล้อมการพัฒนา เราแนะนำให้ใช้ Poetry ในการจัดการ dependencies โดยเราใช้ `pyproject.toml` ในการจัดการ dependencies ของโปรเจกต์ ดังนั้นควรติดตั้ง dependencies ด้วย Poetry

### สร้าง virtual environment

#### ใช้ pip

```bash
python -m venv .venv
```

#### ใช้ Poetry

```bash
poetry init
```

### เปิดใช้งาน virtual environment

#### สำหรับทั้ง pip และ Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### ใช้ Poetry

```bash
poetry shell
```

### ติดตั้งแพ็กเกจและ dependencies ที่จำเป็น

#### ใช้ Poetry (จาก pyproject.toml)

```bash
poetry install
```

### การทดสอบแบบ manual

ก่อนจะส่ง PR ควรทดสอบฟีเจอร์แปลกับเอกสารจริงดังนี้:

1. สร้างโฟลเดอร์สำหรับทดสอบที่ root directory:
    ```bash
    mkdir test_docs
    ```

2. คัดลอกไฟล์ markdown และรูปภาพที่ต้องการแปลไปไว้ในโฟลเดอร์ทดสอบ เช่น:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. ติดตั้งแพ็กเกจแบบ local:
    ```bash
    pip install -e .
    ```

4. รัน Co-op Translator กับเอกสารทดสอบของคุณ:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. ตรวจสอบไฟล์ที่แปลแล้วใน `test_docs/translations` และ `test_docs/translated_images` เพื่อดูว่า:
   - คุณภาพการแปลเป็นที่น่าพอใจหรือไม่
   - คอมเมนต์ metadata ถูกต้องหรือไม่
   - โครงสร้าง markdown เดิมยังคงอยู่
   - ลิงก์และรูปภาพใช้งานได้ถูกต้อง

การทดสอบแบบ manual นี้จะช่วยให้มั่นใจว่าการเปลี่ยนแปลงของคุณใช้งานได้ดีในสถานการณ์จริง

### ตัวแปรสภาพแวดล้อม

1. สร้างไฟล์ `.env` ที่ root directory โดยคัดลอกจากไฟล์ `.env.template`
1. กรอกค่าตัวแปรสภาพแวดล้อมตามคำแนะนำ

> [!TIP]
>
> ### ตัวเลือกเพิ่มเติมสำหรับสภาพแวดล้อมการพัฒนา
>
> นอกจากการรันโปรเจกต์บนเครื่องของคุณเองแล้ว คุณยังสามารถใช้ GitHub Codespaces หรือ VS Code Dev Containers เพื่อสร้างสภาพแวดล้อมการพัฒนาแบบทางเลือกได้เช่นกัน
>
> #### GitHub Codespaces
>
> คุณสามารถรันตัวอย่างนี้แบบออนไลน์ผ่าน GitHub Codespaces ได้เลยโดยไม่ต้องตั้งค่าเพิ่มเติม
>
> ปุ่มนี้จะเปิด VS Code เวอร์ชันเว็บในเบราว์เซอร์ของคุณ:
>
> 1. เปิดเทมเพลต (อาจใช้เวลาสักครู่):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### การรันบนเครื่องโดยใช้ VS Code Dev Containers
>
> ⚠️ ตัวเลือกนี้จะใช้ได้ก็ต่อเมื่อ Docker Desktop ของคุณถูกจัดสรร RAM อย่างน้อย 16 GB หากมี RAM น้อยกว่านี้ แนะนำให้ใช้ [GitHub Codespaces](../..) หรือ [ตั้งค่าบนเครื่อง](../..)
>
> อีกทางเลือกหนึ่งคือ VS Code Dev Containers ซึ่งจะเปิดโปรเจกต์ใน VS Code บนเครื่องของคุณโดยใช้ [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. เปิด Docker Desktop (ติดตั้งหากยังไม่มี)
> 2. เปิดโปรเจกต์:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### รูปแบบโค้ด

เราใช้ [Black](https://github.com/psf/black) เป็นตัวจัดรูปแบบโค้ด Python เพื่อให้โค้ดในโปรเจกต์มีมาตรฐานเดียวกัน Black จะจัดรูปแบบโค้ด Python ให้อัตโนมัติตามมาตรฐานของ Black

#### การตั้งค่า

การตั้งค่าของ Black จะอยู่ใน `pyproject.toml` ของเรา:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### การติดตั้ง Black

คุณสามารถติดตั้ง Black ได้ทั้งผ่าน Poetry (แนะนำ) หรือ pip:

##### ใช้ Poetry

Black จะถูกติดตั้งอัตโนมัติเมื่อคุณตั้งค่าสภาพแวดล้อมการพัฒนา:
```bash
poetry install
```

##### ใช้ pip

หากใช้ pip สามารถติดตั้ง Black ได้โดยตรง:
```bash
pip install black
```

#### การใช้งาน Black

##### กับ Poetry

1. จัดรูปแบบไฟล์ Python ทั้งหมดในโปรเจกต์:
    ```bash
    poetry run black .
    ```

2. จัดรูปแบบไฟล์หรือโฟลเดอร์เฉพาะ:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### กับ pip

1. จัดรูปแบบไฟล์ Python ทั้งหมดในโปรเจกต์:
    ```bash
    black .
    ```

2. จัดรูปแบบไฟล์หรือโฟลเดอร์เฉพาะ:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> แนะนำให้ตั้งค่า editor ของคุณให้จัดรูปแบบโค้ดด้วย Black อัตโนมัติเมื่อบันทึกไฟล์ ปัจจุบัน editor ส่วนใหญ่รองรับฟีเจอร์นี้ผ่าน extension หรือ plugin

## การใช้งาน Co-op Translator

หากต้องการรัน Co-op Translator ด้วย Poetry ในสภาพแวดล้อมของคุณ ให้ทำตามขั้นตอนนี้:

1. ไปยังโฟลเดอร์ที่ต้องการทดสอบการแปล หรือสร้างโฟลเดอร์ชั่วคราวสำหรับทดสอบ

2. รันคำสั่งต่อไปนี้ โดยเปลี่ยน `-l ko` เป็นรหัสภาษาที่ต้องการแปล และ `-d` คือโหมด debug

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> ตรวจสอบให้แน่ใจว่าสภาพแวดล้อม Poetry ของคุณถูกเปิดใช้งาน (poetry shell) ก่อนรันคำสั่ง

## การเพิ่มภาษาใหม่

เรายินดีรับการมีส่วนร่วมที่เพิ่มการรองรับภาษาใหม่ ๆ ก่อนเปิด PR กรุณาทำตามขั้นตอนด้านล่างเพื่อให้การรีวิวเป็นไปอย่างราบรื่น

1. เพิ่มภาษาใน font mapping
   - แก้ไขไฟล์ `src/co_op_translator/fonts/font_language_mappings.yml`
   - เพิ่ม entry โดยระบุ:
     - `code`: รหัสภาษาแบบ ISO (เช่น `vi`)
     - `name`: ชื่อภาษาที่อ่านเข้าใจง่าย
     - `font`: ฟอนต์ที่อยู่ใน `src/co_op_translator/fonts/` และรองรับตัวอักษรของภาษา
     - `rtl`: `true` ถ้าเป็นภาษาเขียนจากขวาไปซ้าย, ถ้าไม่ใช่ให้ใส่ `false`

2. เพิ่มไฟล์ฟอนต์ที่จำเป็น (ถ้าต้องใช้)
   - หากต้องใช้ฟอนต์ใหม่ ตรวจสอบให้แน่ใจว่า license สามารถแจกจ่ายแบบ open source ได้
   - เพิ่มไฟล์ฟอนต์ใน `src/co_op_translator/fonts/`

3. ตรวจสอบผลลัพธ์ในเครื่อง
   - ทดสอบแปลตัวอย่างเล็ก ๆ (Markdown, รูปภาพ, หรือ notebooks ตามความเหมาะสม)
   - ตรวจสอบผลลัพธ์ว่าการแสดงผลถูกต้อง รวมถึงฟอนต์และการจัดวาง RTL ถ้ามี

4. อัปเดตเอกสาร
   - ตรวจสอบให้แน่ใจว่าภาษาที่เพิ่มปรากฏใน `getting_started/supported-languages.md`
   - ไม่ต้องแก้ไข `README_languages_template.md` เพราะไฟล์นี้จะถูกสร้างจากรายการภาษาโดยอัตโนมัติ

5. เปิด PR
   - อธิบายภาษาที่เพิ่มและข้อควรพิจารณาเรื่องฟอนต์/ลิขสิทธิ์
   - แนบภาพหน้าจอของผลลัพธ์ที่แสดงผลแล้วถ้าเป็นไปได้

ตัวอย่าง entry ใน YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## ผู้ดูแลโปรเจกต์

### รูปแบบ commit message และกลยุทธ์การ merge

เพื่อความสม่ำเสมอและชัดเจนในประวัติ commit ของโปรเจกต์ เรากำหนดรูปแบบ commit message **สำหรับ commit สุดท้าย** เมื่อใช้กลยุทธ์ **Squash and Merge**

เมื่อ pull request (PR) ถูก merge, commit ย่อย ๆ ทั้งหมดจะถูกรวมเป็น commit เดียว โดย commit message สุดท้ายควรเป็นไปตามรูปแบบด้านล่างเพื่อให้ประวัติสะอาดและสม่ำเสมอ

#### รูปแบบ commit message (สำหรับ squash and merge)

เราใช้รูปแบบ commit message ดังนี้:

```bash
<type>: <description> (#<PR number>)
```

- **type**: ระบุหมวดหมู่ของ commit โดยใช้ประเภทต่อไปนี้:
  - `Docs`: สำหรับการอัปเดตเอกสาร
  - `Build`: สำหรับการเปลี่ยนแปลงที่เกี่ยวกับระบบ build หรือ dependencies รวมถึงการอัปเดตไฟล์ config, CI workflow หรือ Dockerfile
  - `Core`: สำหรับการเปลี่ยนแปลงฟีเจอร์หลักของโปรเจกต์ โดยเฉพาะไฟล์ใน `src/co_op_translator/core`

- **description**: สรุปสั้น ๆ ว่ามีการเปลี่ยนแปลงอะไร
- **PR number**: หมายเลข pull request ที่เกี่ยวข้องกับ commit

**ตัวอย่าง**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> ปัจจุบัน prefix **`Docs`**, **`Core`**, และ **`Build`** จะถูกเพิ่มให้อัตโนมัติในชื่อ PR ตาม label ที่กำกับไว้กับ source code ที่แก้ไข ดังนั้นโดยปกติคุณไม่ต้องแก้ไขชื่อ PR เอง เพียงแค่ตรวจสอบให้แน่ใจว่าทุกอย่างถูกต้องและ prefix ถูกสร้างอย่างเหมาะสม

#### กลยุทธ์การ merge

เราใช้ **Squash and Merge** เป็นกลยุทธ์หลักสำหรับ pull request วิธีนี้จะช่วยให้ commit message เป็นไปตามรูปแบบที่กำหนด แม้ว่า commit ย่อย ๆ จะไม่ได้เขียนตามรูปแบบก็ตาม

**เหตุผล**:

- ประวัติโปรเจกต์สะอาดและเป็นเส้นตรง
- commit message มีความสม่ำเสมอ
- ลด commit ย่อยที่ไม่สำคัญ (เช่น "fix typo")

เมื่อ merge ให้ตรวจสอบว่า commit message สุดท้ายเป็นไปตามรูปแบบที่กำหนด

**ตัวอย่าง Squash and Merge**
ถ้า PR มี commit ดังนี้:

- `fix typo`
- `update README`
- `adjust formatting`

ควรถูกรวมเป็น:
`Docs: Improve documentation clarity and formatting (#65)`

---

**ข้อจำกัดความรับผิดชอบ**:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่เกิดจากการใช้การแปลนี้