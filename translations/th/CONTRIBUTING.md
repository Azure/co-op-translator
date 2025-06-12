<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:35:21+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "th"
}
-->
# Contributing to Co-op Translator

โครงการนี้ยินดีรับการมีส่วนร่วมและข้อเสนอแนะ ส่วนใหญ่การมีส่วนร่วมจะต้องให้คุณยอมรับ Contributor License Agreement (CLA) ที่ระบุว่าคุณมีสิทธิ์และได้ให้สิทธิ์เราในการใช้ผลงานของคุณ สำหรับรายละเอียดเพิ่มเติม โปรดเยี่ยมชม https://cla.opensource.microsoft.com

เมื่อคุณส่ง pull request ระบบ CLA bot จะตรวจสอบโดยอัตโนมัติว่าคุณจำเป็นต้องส่ง CLA หรือไม่ และจะประดับ PR ให้เหมาะสม (เช่น ตรวจสอบสถานะ, คอมเมนต์) เพียงแค่ทำตามคำแนะนำที่บอทให้มา คุณจะต้องทำเพียงครั้งเดียวในทุกรีโพที่ใช้ CLA ของเรา

## การตั้งค่าสภาพแวดล้อมสำหรับการพัฒนา

เพื่อเตรียมสภาพแวดล้อมการพัฒนาสำหรับโครงการนี้ เราแนะนำให้ใช้ Poetry สำหรับจัดการ dependencies เราใช้ `pyproject.toml` ในการจัดการ dependencies ของโครงการ ดังนั้นในการติดตั้ง dependencies คุณควรใช้ Poetry

### สร้างสภาพแวดล้อมเสมือน

#### ใช้ pip

```bash
python -m venv .venv
```

#### ใช้ Poetry

```bash
poetry init
```

### เปิดใช้งานสภาพแวดล้อมเสมือน

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

ก่อนส่ง PR สิ่งสำคัญคือต้องทดสอบฟังก์ชันการแปลกับเอกสารจริง:

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

5. ตรวจสอบไฟล์แปลใน `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`  
1. กรอกตัวแปรสภาพแวดล้อมตามคำแนะนำ

> [!TIP]
>
> ### ตัวเลือกเพิ่มเติมสำหรับสภาพแวดล้อมการพัฒนา
>
> นอกจากการรันโครงการในเครื่องแล้ว คุณยังสามารถใช้ GitHub Codespaces หรือ VS Code Dev Containers เป็นตัวเลือกสภาพแวดล้อมการพัฒนาอีกทางหนึ่ง
>
> #### GitHub Codespaces
>
> คุณสามารถรันตัวอย่างนี้แบบเสมือนโดยใช้ GitHub Codespaces โดยไม่ต้องตั้งค่าหรือกำหนดค่าเพิ่มเติม
>
> ปุ่มนี้จะเปิด VS Code เวอร์ชันเว็บในเบราว์เซอร์ของคุณ:
>
> 1. เปิดเทมเพลต (อาจใช้เวลาหลายนาที):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### รันในเครื่องโดยใช้ VS Code Dev Containers
>
> ⚠️ ตัวเลือกนี้จะทำงานได้ก็ต่อเมื่อ Docker Desktop ของคุณถูกจัดสรร RAM อย่างน้อย 16 GB หากคุณมี RAM น้อยกว่า 16 GB คุณสามารถลองใช้ [GitHub Codespaces](../..) หรือ [ตั้งค่าในเครื่อง](../..)
>
> ตัวเลือกที่เกี่ยวข้องคือ VS Code Dev Containers ซึ่งจะเปิดโครงการใน VS Code บนเครื่องของคุณโดยใช้ [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. เริ่ม Docker Desktop (ติดตั้งถ้ายังไม่มี)
> 2. เปิดโครงการ:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### รูปแบบโค้ด

เราใช้ [Black](https://github.com/psf/black) เป็นตัวจัดรูปแบบโค้ด Python เพื่อรักษารูปแบบโค้ดให้สม่ำเสมอทั่วทั้งโครงการ Black เป็นตัวจัดรูปแบบโค้ดที่ไม่ประนีประนอมซึ่งจะจัดรูปแบบโค้ด Python โดยอัตโนมัติเพื่อให้ตรงกับรูปแบบของ Black

#### การตั้งค่า

การตั้งค่า Black ถูกกำหนดไว้ใน `pyproject.toml` ของเรา:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### การติดตั้ง Black

คุณสามารถติดตั้ง Black โดยใช้ Poetry (แนะนำ) หรือ pip:

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

1. จัดรูปแบบไฟล์ Python ทั้งหมดในโครงการ:
    ```bash
    poetry run black .
    ```

2. จัดรูปแบบไฟล์หรือไดเรกทอรีเฉพาะ:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### กับ pip

1. จัดรูปแบบไฟล์ Python ทั้งหมดในโครงการ:
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

เพื่อรัน Co-op Translator โดยใช้ Poetry ในสภาพแวดล้อมของคุณ ให้ทำตามขั้นตอนเหล่านี้:

1. ไปยังไดเรกทอรีที่คุณต้องการทดสอบการแปล หรือสร้างโฟลเดอร์ชั่วคราวสำหรับการทดสอบ

2. รันคำสั่งต่อไปนี้ โดยแฟลก `-l ko` with the language code you wish to translate into. The `-d` หมายถึงโหมดดีบัก

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> ตรวจสอบให้แน่ใจว่าสภาพแวดล้อม Poetry ของคุณถูกเปิดใช้งาน (poetry shell) ก่อนรันคำสั่ง

## ผู้ดูแล

### รูปแบบข้อความคอมมิตและกลยุทธ์การรวมโค้ด

เพื่อให้ประวัติการคอมมิตของโครงการมีความสอดคล้องและชัดเจน เราใช้รูปแบบข้อความคอมมิตเฉพาะสำหรับข้อความคอมมิตสุดท้ายเมื่อใช้กลยุทธ์ **Squash and Merge**

เมื่อ pull request (PR) ถูกผสาน คอมมิตแต่ละรายการจะถูกรวมเป็นคอมมิตเดียว ข้อความคอมมิตสุดท้ายควรเป็นไปตามรูปแบบด้านล่างเพื่อรักษาความสะอาดและความสม่ำเสมอของประวัติ

#### รูปแบบข้อความคอมมิต (สำหรับ squash and merge)

เราใช้รูปแบบต่อไปนี้สำหรับข้อความคอมมิต:

```bash
<type>: <description> (#<PR number>)
```

- **type**: ระบุประเภทของคอมมิต เราใช้ประเภทดังนี้:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ ควรใช้การแปลโดยผู้เชี่ยวชาญมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้