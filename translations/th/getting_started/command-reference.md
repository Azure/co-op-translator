<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:16:18+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "th"
}
-->
# อ้างอิงคำสั่ง

**Co-op Translator** CLI มีตัวเลือกหลายแบบให้ปรับแต่งกระบวนการแปลได้ตามต้องการ:

คำสั่ง                                       | คำอธิบาย
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | แปลโปรเจกต์ของคุณเป็นภาษาที่ระบุ เช่น translate -l "es fr de" จะแปลเป็นสเปน ฝรั่งเศส และเยอรมัน ใช้ translate -l "all" เพื่อแปลเป็นทุกภาษาที่รองรับ
translate -l "language_codes" -u              | อัปเดตการแปลโดยลบของเดิมและสร้างใหม่ทั้งหมด คำเตือน: จะลบการแปลปัจจุบันทั้งหมดของภาษาที่ระบุ
translate -l "language_codes" -img            | แปลเฉพาะไฟล์รูปภาพเท่านั้น
translate -l "language_codes" -md             | แปลเฉพาะไฟล์ Markdown เท่านั้น
translate -l "language_codes" -nb             | แปลเฉพาะไฟล์ Jupyter notebook (.ipynb) เท่านั้น
translate -l "language_codes" --fix           | แปลใหม่เฉพาะไฟล์ที่ได้คะแนนความมั่นใจต่ำจากผลการประเมินก่อนหน้า
translate -l "language_codes" -d              | เปิดโหมด debug เพื่อดู log รายละเอียด
translate -l "language_codes" --save-logs, -s | บันทึก log ระดับ DEBUG ลงไฟล์ที่ <root_dir>/logs/ (console ยังควบคุมด้วย -d)
translate -l "language_codes" -r "root_dir"   | ระบุ root directory ของโปรเจกต์
translate -l "language_codes" -f              | ใช้โหมดเร็วสำหรับการแปลรูปภาพ (plotting เร็วขึ้นสูงสุด 3 เท่า แต่คุณภาพและการจัดวางอาจลดลงเล็กน้อย)
translate -l "language_codes" -y              | ตอบตกลงอัตโนมัติทุก prompt (เหมาะกับ CI/CD pipeline)
translate -l "language_codes" --help          | แสดงรายละเอียดคำสั่งที่มีใน CLI
evaluate -l "language_code"                  | ประเมินคุณภาพการแปลของภาษาที่ระบุและให้คะแนนความมั่นใจ
evaluate -l "language_code" -c 0.8           | ประเมินการแปลโดยใช้ threshold ความมั่นใจที่กำหนดเอง
evaluate -l "language_code" -f               | โหมดประเมินเร็ว (ใช้ rule-based เท่านั้น ไม่ใช้ LLM)
evaluate -l "language_code" -D               | โหมดประเมินเชิงลึก (ใช้ LLM เท่านั้น ละเอียดกว่าแต่ช้ากว่า)
evaluate -l "language_code" --save-logs, -s  | บันทึก log ระดับ DEBUG ลงไฟล์ที่ <root_dir>/logs/
migrate-links -l "language_codes"             | ประมวลผลไฟล์ Markdown ที่แปลแล้วเพื่ออัปเดตลิงก์ไปยัง notebook (.ipynb) จะเลือกใช้ notebook ที่แปลแล้วถ้ามี ถ้าไม่มีก็ใช้ต้นฉบับแทนได้
migrate-links -l "language_codes" -r          | ระบุ root directory ของโปรเจกต์ (ค่าเริ่มต้น: โฟลเดอร์ปัจจุบัน)
migrate-links -l "language_codes" --dry-run   | แสดงไฟล์ที่จะถูกเปลี่ยนแปลงโดยไม่เขียนทับจริง
migrate-links -l "language_codes" --no-fallback-to-original | ไม่เขียนลิงก์กลับไปยัง notebook ต้นฉบับเมื่อไม่มีฉบับแปล (อัปเดตเฉพาะเมื่อมีฉบับแปลเท่านั้น)
migrate-links -l "language_codes" -d          | เปิดโหมด debug เพื่อดู log รายละเอียด
migrate-links -l "language_codes" --save-logs, -s | บันทึก log ระดับ DEBUG ลงไฟล์ที่ <root_dir>/logs/
migrate-links -l "all" -y                      | ประมวลผลทุกภาษาและยืนยัน prompt คำเตือนให้อัตโนมัติ

## ตัวอย่างการใช้งาน

  1. พฤติกรรมปกติ (เพิ่มการแปลใหม่โดยไม่ลบของเดิม):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. เพิ่มเฉพาะการแปลรูปภาพเกาหลีใหม่ (ไม่ลบของเดิม):    translate -l "ko" -img

  3. อัปเดตการแปลเกาหลีทั้งหมด (คำเตือน: ลบการแปลเก่าทั้งหมดก่อนแปลใหม่):    translate -l "ko" -u

  4. อัปเดตเฉพาะรูปภาพเกาหลี (คำเตือน: ลบรูปภาพเก่าทั้งหมดก่อนแปลใหม่):    translate -l "ko" -img -u

  5. เพิ่มการแปล markdown ภาษาเกาหลีใหม่โดยไม่กระทบการแปลอื่น:    translate -l "ko" -md

  6. แก้ไขการแปลที่ได้คะแนนความมั่นใจต่ำตามผลประเมินก่อนหน้า: translate -l "ko" --fix

  7. แก้ไขการแปลที่ได้คะแนนความมั่นใจต่ำเฉพาะไฟล์ (markdown): translate -l "ko" --fix -md

  8. แก้ไขการแปลที่ได้คะแนนความมั่นใจต่ำเฉพาะไฟล์ (รูปภาพ): translate -l "ko" --fix -img

  9. ใช้โหมดเร็วสำหรับแปลรูปภาพ:    translate -l "ko" -img -f

  10. แก้ไขการแปลที่ได้คะแนนความมั่นใจต่ำโดยใช้ threshold กำหนดเอง: translate -l "ko" --fix -c 0.8

  11. ตัวอย่างโหมด debug: - translate -l "ko" -d: เปิด log debug
  12. บันทึก log ลงไฟล์: translate -l "ko" -s
  13. DEBUG ทั้งบน console และไฟล์: translate -l "ko" -d -s

  14. อัปเดตลิงก์ notebook สำหรับการแปลเกาหลี (อัปเดตลิงก์ไปยัง notebook ที่แปลแล้วถ้ามี):    migrate-links -l "ko"

  15. อัปเดตลิงก์แบบ dry-run (ไม่เขียนไฟล์จริง):    migrate-links -l "ko" --dry-run

  16. อัปเดตลิงก์เฉพาะเมื่อมี notebook ที่แปลแล้ว (ไม่ fallback ไปต้นฉบับ):    migrate-links -l "ko" --no-fallback-to-original

  17. ประมวลผลทุกภาษาพร้อม prompt ยืนยัน:    migrate-links -l "all"

  18. ประมวลผลทุกภาษาและยืนยันอัตโนมัติ:    migrate-links -l "all" -y
  19. บันทึก log ลงไฟล์สำหรับ migrate-links:    migrate-links -l "ko ja" -s

### ตัวอย่างการประเมิน

> [!WARNING]  
> **ฟีเจอร์เบต้า**: ฟังก์ชันการประเมินยังอยู่ในช่วงเบต้า ฟีเจอร์นี้ถูกปล่อยมาเพื่อประเมินเอกสารที่แปลแล้ว วิธีการประเมินและรายละเอียดการทำงานอาจมีการเปลี่ยนแปลงในอนาคต

  1. ประเมินการแปลภาษาเกาหลี: evaluate -l "ko"

  2. ประเมินโดยใช้ threshold ความมั่นใจที่กำหนดเอง: evaluate -l "ko" -c 0.8

  3. ประเมินแบบเร็ว (ใช้ rule-based เท่านั้น): evaluate -l "ko" -f

  4. ประเมินเชิงลึก (ใช้ LLM เท่านั้น): evaluate -l "ko" -D

---

**ข้อจำกัดความรับผิดชอบ**:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่เกิดขึ้นจากการใช้การแปลนี้