# Microsoft Beginners Repositories

หน้านี้มีไว้สำหรับผู้ดูแลของที่เก็บ "For Beginners" ของ Microsoft ที่ใช้ส่วน README ร่วม "Other Courses"

ผู้ใช้ Co-op Translator ส่วนใหญ่ไม่จำเป็นต้องใช้หน้านี้

## ซิงค์อัตโนมัติส่วน "Other Courses"

เพิ่มตัวบ่งชี้เหล่านี้รอบส่วน "Other Courses" ใน README ของคุณ:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ทุกครั้งที่ Co-op Translator ทำงานผ่าน CLI หรือ GitHub Actions มันจะทดแทนเนื้อหาที่อยู่ระหว่างตัวบ่งชี้ด้วยเทมเพลตที่ถูกแพ็กเกจไว้

## อัปเดตเทมเพลตร่วม

แหล่งที่มาของเทมเพลตอยู่ที่:

```text
src/co_op_translator/templates/other_courses.md
```

ในการอัปเดตเนื้อหาร่วม:

1. แก้ไขเทมเพลต
2. เปิด pull request ไปยัง Co-op Translator
3. หลังจากการเปลี่ยนแปลงถูกปล่อยออกมา ให้รัน Co-op Translator ในที่เก็บเป้าหมาย

## คำแนะนำเกี่ยวกับ Sparse Checkout

ที่เก็บหลักสูตรขนาดใหญ่สามารถมีค่าใช้จ่ายสูงเมื่อต้องโคลนหากรวมเอาผลลัพธ์การแปลจำนวนมาก คุณสามารถใส่คำแนะนำนี้ในส่วนภาษาที่ถูกสร้างขึ้น:

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```