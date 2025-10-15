<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:17:10+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "th"
}
-->
# ติดตั้งแพ็กเกจ Co-op Translator

**Co-op Translator** เป็นเครื่องมือแบบ command-line interface (CLI) ที่ช่วยให้คุณแปลไฟล์ markdown และรูปภาพทั้งหมดในโปรเจกต์ของคุณเป็นหลายภาษาได้ คู่มือนี้จะช่วยแนะนำวิธีตั้งค่าและใช้งานตัวแปลสำหรับกรณีต่าง ๆ

### สร้าง virtual environment

คุณสามารถสร้าง virtual environment ได้โดยใช้ `pip` หรือ `Poetry` พิมพ์คำสั่งใดคำสั่งหนึ่งในเทอร์มินัลของคุณ

#### ใช้ pip

```bash
python -m venv .venv
```

#### ใช้ Poetry

```bash
poetry init
```

### เปิดใช้งาน virtual environment

หลังจากสร้าง virtual environment แล้ว คุณต้องเปิดใช้งาน ขั้นตอนจะแตกต่างกันตามระบบปฏิบัติการ พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัลของคุณ

#### สำหรับทั้ง pip และ Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### ใช้ Poetry

1. ถ้าคุณสร้าง environment ด้วย Poetry ให้พิมพ์คำสั่งนี้ในเทอร์มินัลเพื่อเปิดใช้งาน

    ```bash
    poetry shell
    ```

### ติดตั้งแพ็กเกจและแพ็กเกจที่จำเป็น

เมื่อ virtual environment ของคุณถูกตั้งค่าและเปิดใช้งานแล้ว ขั้นตอนถัดไปคือการติดตั้ง dependencies ที่จำเป็น

### ติดตั้งแบบรวดเร็ว

ติดตั้ง Co-Op Translator ด้วย pip

```
pip install co-op-translator
```
หรือ

ติดตั้งด้วย poetry
```
poetry add co-op-translator
```

#### ใช้ pip (จาก requirements.txt) ถ้าคุณ clone repo นี้

> [!NOTE]
> กรุณาอย่าทำขั้นตอนนี้ถ้าคุณติดตั้ง co-op translator ด้วยวิธีติดตั้งแบบรวดเร็ว

1. ถ้าคุณใช้ pip ให้พิมพ์คำสั่งนี้ในเทอร์มินัล มันจะติดตั้งแพ็กเกจที่จำเป็นตามที่ระบุในไฟล์ `requirements.txt` โดยอัตโนมัติ:

    ```bash
    pip install -r requirements.txt
    ```

#### ใช้ Poetry (จาก pyproject.toml)

1. ถ้าคุณใช้ Poetry ให้พิมพ์คำสั่งนี้ในเทอร์มินัล มันจะติดตั้งแพ็กเกจที่จำเป็นตามที่ระบุในไฟล์ `pyproject.toml` โดยอัตโนมัติ:

    ```bash
    poetry install
    ```

---

**ข้อจำกัดความรับผิดชอบ**:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่เกิดขึ้นจากการใช้การแปลนี้