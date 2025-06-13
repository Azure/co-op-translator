<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:34:53+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "th"
}
-->
# ติดตั้งแพ็กเกจ Co-op translator

**Co-op Translator** คือเครื่องมือบรรทัดคำสั่ง (CLI) ที่ช่วยให้คุณแปลไฟล์ markdown และรูปภาพทั้งหมดในโปรเจกต์ของคุณเป็นหลายภาษา บทแนะนำนี้จะนำทางคุณในการตั้งค่า translator และการใช้งานในกรณีต่างๆ

### สร้าง virtual environment

คุณสามารถสร้าง virtual environment โดยใช้ `pip` หรือ `Poetry` พิมพ์คำสั่งใดคำสั่งหนึ่งต่อไปนี้ในเทอร์มินัลของคุณ

#### ใช้ pip

```bash
python -m venv .venv
```

#### ใช้ Poetry

```bash
poetry init
```

### เปิดใช้งาน virtual environment

หลังจากสร้าง virtual environment แล้ว คุณจะต้องเปิดใช้งาน ขั้นตอนจะแตกต่างกันตามระบบปฏิบัติการของคุณ พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัล

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

1. หากคุณสร้าง environment ด้วย Poetry ให้พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัลเพื่อเปิดใช้งาน

    ```bash
    poetry shell
    ```

### การติดตั้งแพ็กเกจและแพ็กเกจที่จำเป็น

เมื่อ virtual environment ถูกตั้งค่าและเปิดใช้งานแล้ว ขั้นตอนถัดไปคือการติดตั้ง dependencies ที่จำเป็น

### การติดตั้งอย่างรวดเร็ว

ติดตั้ง Co-Op Translator ผ่าน pip

```
pip install co-op-translator
```  
หรือ  

ติดตั้งผ่าน poetry  
```
poetry add co-op-translator
```

#### ใช้ pip (จาก requirements.txt) หากคุณโคลน repo นี้

![NOTE] กรุณาอย่าทำเช่นนี้หากคุณติดตั้ง co-op translator ผ่านการติดตั้งอย่างรวดเร็ว

1. หากคุณใช้ pip ให้พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัล มันจะติดตั้งแพ็กเกจที่จำเป็นตามที่ระบุในไฟล์ `requirements.txt` โดยอัตโนมัติ:

    ```bash
    pip install -r requirements.txt
    ```

#### ใช้ Poetry (จาก pyproject.toml)

1. หากคุณใช้ Poetry ให้พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัล มันจะติดตั้งแพ็กเกจที่จำเป็นตามที่ระบุในไฟล์ `pyproject.toml` โดยอัตโนมัติ:

    ```bash
    poetry install
    ```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้องได้ เอกสารต้นฉบับในภาษาต้นฉบับถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญด้านภาษามนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลฉบับนี้