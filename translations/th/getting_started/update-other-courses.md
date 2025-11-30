<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:44:31+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "th"
}
-->
# อัปเดตส่วน "คอร์สอื่นๆ" (Microsoft Beginners repos)

คำแนะนำนี้อธิบายวิธีทำให้ส่วน "คอร์สอื่นๆ" ซิงค์อัตโนมัติด้วย Co-op Translator และวิธีอัปเดตเทมเพลตทั่วโลกสำหรับทุกรีโพ

- ใช้กับ: รีโพ Microsoft Beginners เท่านั้น
- ทำงานร่วมกับ: Co-op Translator CLI และ GitHub Actions
- แหล่งที่มาของเทมเพลต: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## เริ่มต้นอย่างรวดเร็ว: เปิดใช้งานการซิงค์อัตโนมัติในรีโพของคุณ

เพิ่มตัวกำหนดขอบเขตต่อไปนี้รอบส่วน "คอร์สอื่นๆ" ใน README ของคุณ Co-op Translator จะทำการแทนที่ทุกอย่างระหว่างตัวกำหนดขอบเขตนี้ในทุกครั้งที่รัน

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ทุกครั้งที่ Co-op Translator ทำงาน — ผ่าน CLI (เช่น `translate -l "<language codes>"`) หรือ GitHub Actions — จะอัปเดตส่วน "คอร์สอื่นๆ" ที่ถูกครอบด้วยตัวกำหนดขอบเขตนี้โดยอัตโนมัติ

> [!NOTE]
> หากคุณมีรายการอยู่แล้ว เพียงแค่ครอบด้วยตัวกำหนดขอบเขตเดียวกัน ครั้งถัดไปที่รันจะทำการแทนที่ด้วยเนื้อหามาตรฐานล่าสุด

---

## วิธีเปลี่ยนเนื้อหาระดับโลก

หากคุณต้องการอัปเดตเนื้อหามาตรฐานที่แสดงในรีโพ Beginners ทุกตัว:

1. แก้ไขเทมเพลต: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. เปิด pull request ไปยังรีโพ Co-op Translator พร้อมการเปลี่ยนแปลงของคุณ
3. หลังจาก PR ถูกรวมเข้ากับรีโพแล้ว เวอร์ชันของ Co-op Translator จะได้รับการอัปเดต
4. ครั้งถัดไปที่ Co-op Translator ทำงาน (CLI หรือ GitHub Action) ในรีโพเป้าหมาย จะซิงค์ส่วนที่อัปเดตโดยอัตโนมัติ

วิธีนี้ช่วยให้มีแหล่งข้อมูลเดียวที่ถูกต้องสำหรับเนื้อหา "คอร์สอื่นๆ" ในรีโพ Beginners ทุกตัว

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->