# การตั้งค่า Azure AI

ใช้คำแนะนำนี้เมื่อคุณต้องการกำหนดค่า Azure OpenAI สำหรับการแปลข้อความ และ Azure AI Vision สำหรับการดึงข้อความจากรูปภาพ

## ความต้องการเบื้องต้น

- การสมัครใช้งาน Azure.
- สิทธิ์ในการสร้างหรือใช้งานทรัพยากร Azure AI และการปรับใช้โมเดล.
- โปรเจกต์ใน Azure AI Foundry หรือการเข้าถึงทรัพยากร Azure OpenAI และ Azure AI Vision ที่เทียบเท่า.

## สร้างโปรเจกต์ Azure AI

1. เปิด [Azure AI Foundry](https://ai.azure.com).
2. สร้างหรือเลือกโปรเจกต์.
3. สร้างหรือเลือก AI hub สำหรับโปรเจกต์.
4. เปิดภาพรวมของโปรเจกต์หลังจากสร้างเสร็จ.

## ปรับใช้โมเดล Azure OpenAI

1. ในโปรเจกต์ ให้เปิด **Models + endpoints**.
2. เลือก **Deploy model**.
3. เลือกโมเดล GPT เช่น `gpt-4o`.
4. ปรับใช้โมเดล.
5. บันทึก endpoint, deployment name, model name, API key และ API version.

!!! note
    เวอร์ชัน API ของ Azure OpenAI แยกจากเวอร์ชันของโมเดลที่แสดงใน Azure AI Foundry เลือกเวอร์ชัน API ที่ได้รับการรองรับสำหรับการปรับใช้ของคุณ.

## กำหนดค่า Azure AI Vision

การแปลภาพใช้ Azure AI Vision เพื่อดึงข้อความจากรูปภาพต้นฉบับก่อนที่ข้อความจะถูกแปล.

ในโปรเจกต์ Azure AI ของคุณ ให้ค้นหา Azure AI Services key และ endpoint.

![ค้นหาข้อมูลบริการ Azure AI](../../assets/find-azure-ai-info.png)

บันทึก:

- endpoint ของ Azure AI Service
- API key ของ Azure AI Service

## ตัวแปรแวดล้อม

เพิ่มข้อมูลรับรองไปยังไฟล์ `.env` หรือความลับของ CI.

```bash
# Azure AI Vision จำเป็นสำหรับการแปลภาพ
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI จำเป็นสำหรับการแปลข้อความ
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator ยังรองรับชุดข้อมูลรับรองแบบสำรอง (fallback) ทางเลือก โดยทำสำเนาชุดผู้ให้บริการทั้งหมดพร้อมคำต่อท้ายเช่น `_1` หรือ `_2`; ตัวแปรทั้งหมดในชุดสำรองต้องมีคำต่อท้ายเดียวกัน.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## ขั้นตอนต่อไป

- กลับไปที่ [การกำหนดค่า](configuration.md) เพื่อตั้งค่าตัวแปรแวดล้อมในเครื่องหรือ CI.
- ใช้ [ข้อมูลอ้างอิง CLI](cli.md) สำหรับคำสั่งแปล.
- ใช้ [GitHub Actions](github-actions.md) เพื่อทำให้คำขอ pull request สำหรับการแปลเป็นแบบอัตโนมัติ.