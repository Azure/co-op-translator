<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c64ba65e091e5d87385490fa63a8f574",
  "translation_date": "2025-06-12T12:35:29+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "th"
}
-->
# วิธีใช้คำสั่ง Co-op Translator ผ่าน command line interface (CLI)

## ข้อกำหนดเบื้องต้น

- **Python 3.10 ขึ้นไป**: จำเป็นสำหรับการใช้งาน Co-op Translator

## สารบัญ

1. [สร้างไฟล์ '.env' ในโฟลเดอร์หลัก](./create-env-file.md)
   - ใส่คีย์ที่จำเป็นสำหรับบริการโมเดลภาษาที่เลือกใช้
   - หากไม่ใส่คีย์ Azure Computer Vision หรือระบุ `-md` ตัวแปลภาษาจะทำงานในโหมด Markdown เท่านั้น
1. [ติดตั้งแพ็กเกจ Co-op translator](./install-package.md)
1. [แปลโปรเจกต์ของคุณด้วย Co-op Translator](./translator-your-project.md)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความถูกต้องสูงสุด โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดจากการใช้การแปลนี้