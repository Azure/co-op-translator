<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:16:48+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "th"
}
-->
# คู่มือแก้ปัญหา Microsoft Co-op Translator

## ภาพรวม
Microsoft Co-Op Translator เป็นเครื่องมือแปลเอกสาร Markdown ที่ทรงพลังและใช้งานง่าย คู่มือนี้จะช่วยคุณแก้ไขปัญหาทั่วไปที่อาจพบขณะใช้งานเครื่องมือนี้

## ปัญหาทั่วไปและวิธีแก้ไข

### 1. ปัญหาแท็ก Markdown
**ปัญหา:** เอกสาร Markdown ที่แปลแล้วมีแท็ก `markdown` อยู่ด้านบน ทำให้แสดงผลผิดปกติ

**วิธีแก้ไข:** เพียงลบแท็ก `markdown` ที่อยู่ด้านบนสุดของไฟล์ออก ก็จะแสดงผล Markdown ได้ถูกต้อง

**ขั้นตอน:**
1. เปิดไฟล์ Markdown (`.md`) ที่แปลแล้ว
2. หาแท็ก `markdown` ที่อยู่ด้านบนสุดของเอกสาร
3. ลบแท็ก `markdown` ออก
4. บันทึกไฟล์
5. เปิดไฟล์ใหม่อีกครั้งเพื่อตรวจสอบว่าแสดงผลถูกต้อง

### 2. ปัญหา URL ของรูปภาพฝังในเอกสาร
**ปัญหา:** URL ของรูปภาพที่ฝังไว้ไม่ตรงกับภาษาของเอกสาร ทำให้รูปภาพแสดงผิดหรือไม่แสดง

**วิธีแก้ไข:** ตรวจสอบ URL ของรูปภาพที่ฝังไว้ให้ตรงกับภาษาของเอกสาร รูปภาพทั้งหมดจะอยู่ในโฟลเดอร์ `translated_images` และชื่อไฟล์จะมีแท็กภาษากำกับ

**ขั้นตอน:**
1. เปิดเอกสาร Markdown ที่แปลแล้ว
2. ตรวจสอบรูปภาพที่ฝังไว้และ URL ของแต่ละรูป
3. ตรวจสอบว่าแท็กภาษาของชื่อไฟล์รูปภาพตรงกับภาษาของเอกสาร
4. แก้ไข URL หากจำเป็น
5. บันทึกไฟล์และเปิดใหม่เพื่อตรวจสอบว่ารูปภาพแสดงถูกต้อง

### 3. ความถูกต้องของการแปล
**ปัญหา:** เนื้อหาที่แปลยังไม่ถูกต้องหรือจำเป็นต้องแก้ไขเพิ่มเติม

**วิธีแก้ไข:** ตรวจทานเอกสารที่แปลแล้วและแก้ไขให้ถูกต้องและอ่านเข้าใจง่ายขึ้น

**ขั้นตอน:**
1. เปิดเอกสารที่แปลแล้ว
2. อ่านเนื้อหาอย่างละเอียด
3. แก้ไขเนื้อหาให้ถูกต้องและเหมาะสม
4. บันทึกไฟล์

## 4. Permission Error Redacted หรือ 404

หากรูปภาพหรือข้อความไม่ได้แปลเป็นภาษาที่ถูกต้อง และเมื่อรันในโหมด -d debug แล้วพบ error 401 นี่คือปัญหาการยืนยันตัวตน — อาจเป็นเพราะคีย์ไม่ถูกต้อง หมดอายุ หรือไม่ได้เชื่อมกับ region ของ endpoint

ให้รัน co-op translator พร้อม [สวิตช์ -d debug](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) เพื่อดูสาเหตุที่แท้จริง

- **ข้อความ Error**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **สาเหตุที่เป็นไปได้**:
  - Subscription key ถูกปิดบังหรือใส่ผิดใน request
  - AI Services Key หรือ Subscription Key อาจเป็นของ Azure resource อื่น (เช่น Translator หรือ OpenAI) แทนที่จะเป็น **Azure AI Vision**

 **Resource Type**
  - ไปที่ [Azure Portal](https://portal.azure.com) หรือ [Azure AI Foundry](https://ai.azure.com) และตรวจสอบว่า resource เป็นประเภท `Azure AI services` → `Vision`
  - ตรวจสอบคีย์และให้แน่ใจว่าใช้คีย์ที่ถูกต้อง

## 5. ข้อผิดพลาดการตั้งค่า (New Error Handling)

ตั้งแต่ระบบ selective translation ใหม่ Co-op Translator จะแจ้ง error ชัดเจนเมื่อยังไม่ได้ตั้งค่าบริการที่จำเป็น

### 5.1. ยังไม่ได้ตั้งค่า Azure AI Service สำหรับแปลรูปภาพ

**ปัญหา:** คุณร้องขอให้แปลรูปภาพ (`-img` flag) แต่ยังไม่ได้ตั้งค่า Azure AI Service

**ข้อความ Error:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**วิธีแก้ไข:**
1. **ทางเลือกที่ 1**: ตั้งค่า Azure AI Service
   - เพิ่ม `AZURE_AI_SERVICE_API_KEY` ในไฟล์ `.env`
   - เพิ่ม `AZURE_AI_SERVICE_ENDPOINT` ในไฟล์ `.env`
   - ตรวจสอบว่าบริการเข้าถึงได้

2. **ทางเลือกที่ 2**: ยกเลิกการร้องขอแปลรูปภาพ
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. ขาดการตั้งค่าที่จำเป็น

**ปัญหา:** ยังไม่ได้ตั้งค่า LLM ที่จำเป็น

**ข้อความ Error:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**วิธีแก้ไข:**
1. ตรวจสอบว่าไฟล์ `.env` มีการตั้งค่า LLM อย่างน้อยหนึ่งแบบดังนี้:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` และ `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   คุณต้องตั้งค่าอย่างใดอย่างหนึ่งระหว่าง Azure OpenAI หรือ OpenAI

### 5.3. สับสนกับการแปลแบบเลือกไฟล์

**ปัญหา:** ไม่มีไฟล์ใดถูกแปลทั้งที่คำสั่งสำเร็จ

**สาเหตุที่เป็นไปได้:**
- ใช้ flag ประเภทไฟล์ผิด (`-md`, `-img`, `-nb`)
- ไม่มีไฟล์ที่ตรงกับที่เลือกในโปรเจกต์
- โครงสร้างไดเรกทอรีผิด

**วิธีแก้ไข:**
1. **ใช้ debug mode** เพื่อตรวจสอบสิ่งที่เกิดขึ้น:
   ```bash
   translate -l "ko" -md -d
   ```

2. **ตรวจสอบประเภทไฟล์** ในโปรเจกต์ของคุณ:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **ตรวจสอบการใช้ flag ร่วมกัน**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. การย้ายจากระบบเก่า

### 6.1. โหมด Markdown-Only ถูกยกเลิก

**ปัญหา:** คำสั่งที่เคย fallback เป็น markdown-only อัตโนมัติจะไม่ทำงานแบบเดิมอีกต่อไป

**พฤติกรรมเดิม:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**พฤติกรรมใหม่:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**วิธีแก้ไข:**
- **ระบุให้ชัดเจน** ว่าต้องการแปลอะไร:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. พฤติกรรมลิงก์ที่ไม่คาดคิด

**ปัญหา:** ลิงก์ในไฟล์ที่แปลแล้วชี้ไปยังตำแหน่งที่ไม่คาดคิด

**สาเหตุ:** การประมวลผลลิงก์แบบไดนามิกเปลี่ยนไปตามประเภทไฟล์ที่เลือก

**วิธีแก้ไข:**
1. **ทำความเข้าใจพฤติกรรมลิงก์ใหม่**:
   - มี `-nb`: ลิงก์ notebook จะชี้ไปยังไฟล์ที่แปลแล้ว
   - ไม่มี `-nb`: ลิงก์ notebook จะชี้ไปยังไฟล์ต้นฉบับ
   - มี `-img`: ลิงก์รูปภาพจะชี้ไปยังไฟล์ที่แปลแล้ว
   - ไม่มี `-img`: ลิงก์รูปภาพจะชี้ไปยังไฟล์ต้นฉบับ

2. **เลือกใช้ flag ให้เหมาะกับงานของคุณ**:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action ทำงานแต่ไม่มี Pull Request (PR) ถูกสร้าง

**อาการ:** ใน workflow logs ของ `peter-evans/create-pull-request` แสดงว่า:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**สาเหตุที่เป็นไปได้:**
- **ไม่มีการเปลี่ยนแปลง:** ขั้นตอนแปลไม่มี diff ใหม่ (repo อัปเดตอยู่แล้ว)
- **ไฟล์ output ถูก ignore:** `.gitignore` ไม่รวมไฟล์ที่ต้องการ commit (เช่น `*.ipynb`, `translations/`, `translated_images/`)
- **add-paths ไม่ตรง:** path ที่กำหนดใน action ไม่ตรงกับตำแหน่ง output จริง
- **เงื่อนไข/ตรรกะ workflow:** ขั้นตอนแปลจบก่อนหรือเขียนไฟล์ไปยังไดเรกทอรีที่ไม่คาดคิด

**วิธีตรวจสอบ/แก้ไข:**
1. **ตรวจสอบ output:** หลังแปลแล้ว ให้เช็คว่าใน workspace มีไฟล์ใหม่หรือไฟล์ที่เปลี่ยนแปลงใน `translations/` และ/หรือ `translated_images/`
   - ถ้าแปล notebook ให้แน่ใจว่าไฟล์ `.ipynb` ถูกเขียนไว้ใน `translations/<lang>/...`
2. **ตรวจสอบ `.gitignore`:** อย่า ignore ไฟล์ output ที่สร้างขึ้น ตรวจสอบว่าไม่ได้ ignore:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (ถ้าแปล notebook)
3. **ตรวจสอบ add-paths ให้ตรงกับ output:** ใช้ค่าหลายบรรทัดและรวมทั้งสองโฟลเดอร์ถ้าจำเป็น:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **บังคับสร้าง PR เพื่อ debug:** อนุญาต empty commit ชั่วคราวเพื่อตรวจสอบ wiring:
   ```yaml
   with:
     commit-empty: true
   ```
5. **รันแบบ debug:** เพิ่ม `-d` ในคำสั่งแปลเพื่อดูว่าเจอไฟล์อะไรและเขียนไฟล์อะไรบ้าง
6. **สิทธิ์ (GITHUB_TOKEN):** ตรวจสอบว่า workflow มีสิทธิ์เขียนเพื่อสร้าง commit และ PR:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## เช็กลิสต์แก้ปัญหาเบื้องต้น

เมื่อเจอปัญหาเกี่ยวกับการแปล:

1. **ใช้ debug mode:** เพิ่ม flag `-d` เพื่อดู log รายละเอียด
2. **ตรวจสอบ flag:** ให้แน่ใจว่า `-md`, `-img`, `-nb` ตรงกับที่ต้องการ
3. **ตรวจสอบการตั้งค่า:** เช็คว่าไฟล์ `.env` มีคีย์ที่จำเป็นครบ
4. **ทดสอบทีละขั้น:** เริ่มจาก `-md` อย่างเดียว แล้วค่อยเพิ่มประเภทอื่น
5. **ตรวจสอบโครงสร้างไฟล์:** ให้แน่ใจว่าไฟล์ต้นฉบับมีอยู่และเข้าถึงได้

ดูรายละเอียดเพิ่มเติมเกี่ยวกับคำสั่งและ flag ได้ที่ [Command Reference](./command-reference.md)

---

**ข้อจำกัดความรับผิดชอบ**:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ ขอแนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่เกิดขึ้นจากการใช้การแปลนี้