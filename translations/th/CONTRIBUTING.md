<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:15:53+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "th"
}
-->
# การมีส่วนร่วมกับ Co-op Translator

โครงการนี้ยินดีต้อนรับการมีส่วนร่วมและข้อเสนอแนะ ส่วนใหญ่การมีส่วนร่วมจะต้องให้คุณยอมรับข้อตกลง Contributor License Agreement (CLA) ซึ่งเป็นการประกาศว่าคุณมีสิทธิ์และได้ให้สิทธิ์แก่เราในการใช้ผลงานของคุณ สำหรับรายละเอียดเพิ่มเติม โปรดเยี่ยมชม https://cla.opensource.microsoft.com

เมื่อคุณส่ง pull request ระบบ CLA bot จะตรวจสอบโดยอัตโนมัติว่าคุณจำเป็นต้องส่ง CLA หรือไม่ และจะเพิ่มสถานะหรือคอมเมนต์ใน PR ตามที่เหมาะสม เพียงแค่ทำตามคำแนะนำที่บอทให้ไว้ คุณจะต้องทำเพียงครั้งเดียวสำหรับทุกรีโปที่ใช้ CLA ของเรา

## การตั้งค่าสภาพแวดล้อมสำหรับการพัฒนา

เพื่อเตรียมสภาพแวดล้อมสำหรับการพัฒนาในโครงการนี้ เราแนะนำให้ใช้ Poetry สำหรับจัดการ dependencies เราใช้ไฟล์ `pyproject.toml` ในการจัดการ dependencies ของโปรเจกต์ ดังนั้นในการติดตั้ง dependencies คุณควรใช้ Poetry

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

### การติดตั้งแพ็กเกจและแพ็กเกจที่จำเป็น

#### ใช้ Poetry (จาก pyproject.toml)

```bash
poetry install
```

### การทดสอบด้วยตนเอง

ก่อนส่ง PR ควรทดสอบฟังก์ชันการแปลกับเอกสารจริง:

1. สร้างไดเรกทอรีทดสอบในไดเรกทอรีหลัก:
    ```bash
    mkdir test_docs
    ```

2. คัดลอกเอกสาร markdown และรูปภาพที่ต้องการแปลไปยังไดเรกทอรีทดสอบ เช่น:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. ติดตั้งแพ็กเกจในเครื่อง:
    ```bash
    pip install -e .
    ```

4. รัน Co-op Translator กับเอกสารทดสอบของคุณ:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. ตรวจสอบไฟล์แปลใน `test_docs/translations` และ `test_docs/translated_images` เพื่อยืนยันว่า:
   - คุณภาพการแปลดี
   - คอมเมนต์ metadata ถูกต้อง
   - โครงสร้าง markdown เดิมยังคงอยู่
   - ลิงก์และรูปภาพทำงานได้อย่างถูกต้อง

การทดสอบด้วยตนเองนี้ช่วยให้มั่นใจว่าการเปลี่ยนแปลงของคุณทำงานได้ดีในสถานการณ์จริง

### ตัวแปรสภาพแวดล้อม

1. สร้างไฟล์ `.env` ในไดเรกทอรีหลักโดยคัดลอกจากไฟล์ `.env.template` ที่ให้มา
2. กรอกตัวแปรสภาพแวดล้อมตามคำแนะนำ

> [!TIP]
>
> ### ตัวเลือกเพิ่มเติมสำหรับสภาพแวดล้อมการพัฒนา
>
> นอกจากการรันโปรเจกต์ในเครื่องแล้ว คุณยังสามารถใช้ GitHub Codespaces หรือ VS Code Dev Containers เป็นตัวเลือกสภาพแวดล้อมการพัฒนาได้
>
> #### GitHub Codespaces
>
> คุณสามารถรันตัวอย่างนี้แบบเสมือนจริงโดยใช้ GitHub Codespaces โดยไม่ต้องตั้งค่าหรือกำหนดค่าเพิ่มเติม
>
> ปุ่มนี้จะเปิด VS Code เวอร์ชันเว็บในเบราว์เซอร์ของคุณ:
>
> 1. เปิดเทมเพลต (อาจใช้เวลาหลายวินาที):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### การรันในเครื่องโดยใช้ VS Code Dev Containers
>
> ⚠️ ตัวเลือกนี้จะทำงานได้ก็ต่อเมื่อ Docker Desktop ของคุณมี RAM อย่างน้อย 16 GB หากมี RAM น้อยกว่า 16 GB คุณสามารถลองใช้ [GitHub Codespaces](../..) หรือ [ตั้งค่าในเครื่อง](../..) แทน
>
> ตัวเลือกที่เกี่ยวข้องคือ VS Code Dev Containers ซึ่งจะเปิดโปรเจกต์ใน VS Code บนเครื่องของคุณโดยใช้ [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. เริ่ม Docker Desktop (ติดตั้งถ้ายังไม่มี)
> 2. เปิดโปรเจกต์:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### รูปแบบโค้ด

เราใช้ [Black](https://github.com/psf/black) เป็นตัวจัดรูปแบบโค้ด Python เพื่อรักษาความสม่ำเสมอของรูปแบบโค้ดในโปรเจกต์ Black เป็นตัวจัดรูปแบบโค้ดที่ไม่ยืดหยุ่นซึ่งจะจัดรูปแบบโค้ด Python โดยอัตโนมัติเพื่อให้เป็นไปตามรูปแบบของ Black

#### การตั้งค่า

การตั้งค่า Black ถูกกำหนดไว้ในไฟล์ `pyproject.toml` ของเรา:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### การติดตั้ง Black

คุณสามารถติดตั้ง Black ได้โดยใช้ Poetry (แนะนำ) หรือ pip:

##### ใช้ Poetry

Black จะถูกติดตั้งโดยอัตโนมัติเมื่อคุณตั้งค่าสภาพแวดล้อมการพัฒนา:
```bash
poetry install
```

##### ใช้ pip

ถ้าคุณใช้ pip คุณสามารถติดตั้ง Black ได้โดยตรง:
```bash
pip install black
```

#### การใช้ Black

##### กับ Poetry

1. จัดรูปแบบไฟล์ Python ทั้งหมดในโปรเจกต์:
    ```bash
    poetry run black .
    ```

2. จัดรูปแบบไฟล์หรือไดเรกทอรีเฉพาะ:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### กับ pip

1. จัดรูปแบบไฟล์ Python ทั้งหมดในโปรเจกต์:
    ```bash
    black .
    ```

2. จัดรูปแบบไฟล์หรือไดเรกทอรีเฉพาะ:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> เราแนะนำให้ตั้งค่า editor ของคุณให้จัดรูปแบบโค้ดด้วย Black อัตโนมัติเมื่อบันทึกไฟล์ ตัวแก้ไขสมัยใหม่ส่วนใหญ่รองรับฟีเจอร์นี้ผ่านส่วนขยายหรือปลั๊กอิน

## การรัน Co-op Translator

เพื่อรัน Co-op Translator โดยใช้ Poetry ในสภาพแวดล้อมของคุณ ให้ทำตามขั้นตอนดังนี้:

1. ไปยังไดเรกทอรีที่คุณต้องการทดสอบการแปล หรือสร้างโฟลเดอร์ชั่วคราวสำหรับการทดสอบ

2. รันคำสั่งต่อไปนี้ โดยเปลี่ยน `-l ko` เป็นรหัสภาษาที่คุณต้องการแปลเข้าไป ตัวเลือก `-d` คือโหมดดีบัก

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> ตรวจสอบให้แน่ใจว่าสภาพแวดล้อม Poetry ของคุณถูกเปิดใช้งาน (poetry shell) ก่อนรันคำสั่งนี้

## การเพิ่มภาษาใหม่

เรายินดีรับการมีส่วนร่วมที่เพิ่มการรองรับภาษาใหม่ ก่อนเปิด PR โปรดทำตามขั้นตอนด้านล่างเพื่อให้การตรวจสอบเป็นไปอย่างราบรื่น

1. เพิ่มภาษาลงในแมปปิ้งฟอนต์
   - แก้ไขไฟล์ `src/co_op_translator/fonts/font_language_mappings.yml`
   - เพิ่มรายการโดยระบุ:
     - `code`: รหัสภาษาแบบ ISO (เช่น `vi`)
     - `name`: ชื่อแสดงที่เข้าใจง่าย
     - `font`: ฟอนต์ที่รวมอยู่ใน `src/co_op_translator/fonts/` ที่รองรับสคริปต์นั้น
     - `rtl`: `true` ถ้าเป็นภาษาที่อ่านจากขวาไปซ้าย มิฉะนั้น `false`

2. รวมไฟล์ฟอนต์ที่จำเป็น (ถ้ามี)
   - หากต้องใช้ฟอนต์ใหม่ ให้ตรวจสอบความเข้ากันได้ของไลเซนส์สำหรับการแจกจ่ายแบบโอเพนซอร์ส
   - เพิ่มไฟล์ฟอนต์ลงใน `src/co_op_translator/fonts/`

3. ตรวจสอบในเครื่อง
   - รันการแปลกับตัวอย่างเล็กๆ (Markdown, รูปภาพ และโน้ตบุ๊กตามความเหมาะสม)
   - ตรวจสอบผลลัพธ์ว่ารันได้ถูกต้อง รวมถึงฟอนต์และการจัดวางแบบ RTL หากมี

4. อัปเดตเอกสาร
   - ตรวจสอบให้แน่ใจว่าภาษาใหม่ปรากฏใน `getting_started/supported-languages.md`
   - ไม่ต้องแก้ไข `getting_started/README_languages_template.md` เพราะสร้างจากรายการภาษาที่รองรับ

5. เปิด PR
   - อธิบายภาษาที่เพิ่มและข้อควรพิจารณาเรื่องฟอนต์/ไลเซนส์
   - แนบภาพหน้าจอของผลลัพธ์ที่แสดงถ้าเป็นไปได้

ตัวอย่างรายการ YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### ทดสอบภาษาใหม่

คุณสามารถทดสอบภาษาใหม่โดยรันคำสั่งนี้:

```bash
# สร้างและเปิดใช้งานสภาพแวดล้อมเสมือน
python -m venv .venv
# วินโดวส์
.venv\Scripts\activate
# แมคโอเอส/ลินุกซ์
source .venv/bin/activate
# ติดตั้งแพ็กเกจสำหรับการพัฒนา
pip install -e .
# รันการแปล
translate -l "new_lang"
```

## ผู้ดูแลโครงการ

### รูปแบบข้อความคอมมิตและกลยุทธ์การรวมโค้ด

เพื่อให้ประวัติการคอมมิตของโปรเจกต์มีความสม่ำเสมอและชัดเจน เราใช้รูปแบบข้อความคอมมิตเฉพาะ **สำหรับข้อความคอมมิตสุดท้าย** เมื่อใช้กลยุทธ์ **Squash and Merge**

เมื่อ pull request (PR) ถูกผสาน คอมมิตแต่ละรายการจะถูกรวมเป็นคอมมิตเดียว ข้อความคอมมิตสุดท้ายควรเป็นไปตามรูปแบบด้านล่างเพื่อรักษาความสะอาดและความสม่ำเสมอของประวัติ

#### รูปแบบข้อความคอมมิต (สำหรับ squash and merge)

เราใช้รูปแบบข้อความคอมมิตดังนี้:

```bash
<type>: <description> (#<หมายเลข PR>)
```

- **type**: ระบุประเภทของคอมมิต เราใช้ประเภทดังนี้:
  - `Docs`: สำหรับการอัปเดตเอกสาร
  - `Build`: สำหรับการเปลี่ยนแปลงที่เกี่ยวข้องกับระบบ build หรือ dependencies รวมถึงการอัปเดตไฟล์ config, workflow CI หรือ Dockerfile
  - `Core`: สำหรับการแก้ไขฟังก์ชันหลักหรือฟีเจอร์ของโปรเจกต์ โดยเฉพาะไฟล์ในไดเรกทอรี `src/co_op_translator/core`

- **description**: สรุปสั้นๆ ของการเปลี่ยนแปลง
- **PR number**: หมายเลข pull request ที่เกี่ยวข้องกับคอมมิตนี้

**ตัวอย่าง**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> ปัจจุบัน prefix **`Docs`**, **`Core`**, และ **`Build`** จะถูกเพิ่มโดยอัตโนมัติในชื่อ PR ตามป้ายกำกับที่ใช้กับโค้ดที่แก้ไข ตราบใดที่ป้ายกำกับถูกต้อง คุณไม่จำเป็นต้องแก้ไขชื่อ PR ด้วยตนเอง เพียงตรวจสอบให้แน่ใจว่าทุกอย่างถูกต้องและ prefix ถูกสร้างขึ้นอย่างเหมาะสม

#### กลยุทธ์การรวมโค้ด

เราใช้ **Squash and Merge** เป็นกลยุทธ์เริ่มต้นสำหรับ pull requests วิธีนี้ช่วยให้ข้อความคอมมิตเป็นไปตามรูปแบบที่กำหนด แม้ว่าคอมมิตย่อยจะไม่เป็นไปตามรูปแบบก็ตาม

**เหตุผล**:

- ประวัติโปรเจกต์ที่สะอาดและเป็นเส้นตรง
- ความสม่ำเสมอของข้อความคอมมิต
- ลดเสียงรบกวนจากคอมมิตเล็กๆ (เช่น "fix typo")

เมื่อรวมโค้ด ให้แน่ใจว่าข้อความคอมมิตสุดท้ายเป็นไปตามรูปแบบที่อธิบายไว้ข้างต้น

**ตัวอย่าง Squash and Merge**
ถ้า PR มีคอมมิตดังนี้:

- `fix typo`
- `update README`
- `adjust formatting`

จะถูกรวมเป็น:
`Docs: Improve documentation clarity and formatting (#65)`

### กระบวนการปล่อยเวอร์ชัน

ส่วนนี้อธิบายวิธีง่ายที่สุดสำหรับผู้ดูแลในการปล่อยเวอร์ชันใหม่ของ Co-op Translator

#### 1. เพิ่มเวอร์ชันใน `pyproject.toml`

1. ตัดสินใจหมายเลขเวอร์ชันถัดไป (เราใช้ semantic versioning: `MAJOR.MINOR.PATCH`)
2. แก้ไขไฟล์ `pyproject.toml` และอัปเดตฟิลด์ `version` ภายใต้ `[tool.poetry]`
3. เปิด pull request ที่เปลี่ยนแปลงเฉพาะเวอร์ชัน (และไฟล์ lock/metadata ที่อัปเดตอัตโนมัติถ้ามี)
4. หลังจากตรวจสอบแล้ว ใช้ **Squash and Merge** และตรวจสอบให้แน่ใจว่าข้อความคอมมิตสุดท้ายเป็นไปตามรูปแบบที่กำหนด

#### 2. สร้าง GitHub Release

1. ไปที่หน้ารีโป GitHub และเปิด **Releases** → **Draft a new release**
2. สร้างแท็กใหม่ (เช่น `v0.13.0`) จากสาขา `main`
3. ตั้งชื่อ release ให้ตรงกับเวอร์ชัน (เช่น `v0.13.0`)
4. คลิก **Generate release notes** เพื่อเติม changelog อัตโนมัติ
5. แก้ไขข้อความตามต้องการ (เช่น เน้นภาษาที่รองรับใหม่หรือการเปลี่ยนแปลงสำคัญ)
6. เผยแพร่ release

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->