<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:27:01+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "th"
}
-->
# สร้างไฟล์ *.env* ในไดเรกทอรีหลัก

ในบทเรียนนี้ เราจะพาคุณตั้งค่าตัวแปรแวดล้อมสำหรับบริการ Azure โดยใช้ไฟล์ *.env* ตัวแปรแวดล้อมช่วยให้คุณจัดการข้อมูลรับรองที่สำคัญ เช่น กุญแจ API ได้อย่างปลอดภัยโดยไม่ต้องฝังไว้ในโค้ดของคุณ

> [!IMPORTANT]
> - จำเป็นต้องตั้งค่าบริการโมเดลภาษาเพียงหนึ่งบริการเท่านั้น (Azure OpenAI หรือ OpenAI) ให้กรอกตัวแปรแวดล้อมสำหรับบริการที่คุณต้องการใช้ หากตั้งค่าตัวแปรแวดล้อมสำหรับหลายโมเดลพร้อมกัน ตัวแปลภาษาร่วมจะเลือกบริการตามลำดับความสำคัญ
> - หากไม่ได้ตั้งค่าตัวแปรแวดล้อมสำหรับ Computer Vision ตัวแปลภาษาจะเปลี่ยนไปใช้ [โหมด Markdown เท่านั้น](./markdown-only-mode.md) โดยอัตโนมัติ

> [!NOTE]
> คู่มือนี้เน้นที่บริการ Azure เป็นหลัก แต่คุณสามารถเลือกใช้โมเดลภาษาที่รองรับได้จาก [รายการโมเดลและบริการที่รองรับ](../README.md#-supported-models-and-services)

## สร้างไฟล์ *.env*

ในไดเรกทอรีหลักของโปรเจกต์ ให้สร้างไฟล์ชื่อ *.env* ไฟล์นี้จะเก็บตัวแปรแวดล้อมทั้งหมดในรูปแบบที่เรียบง่าย

> [!WARNING]
> อย่าคอมมิตไฟล์ *.env* เข้าสู่ระบบควบคุมเวอร์ชันเช่น Git ให้เพิ่ม *.env* ลงในไฟล์ .gitignore เพื่อป้องกันการคอมมิตโดยไม่ตั้งใจ

1. ไปที่ไดเรกทอรีหลักของโปรเจกต์ของคุณ

1. สร้างไฟล์ *.env* ในไดเรกทอรีหลักของโปรเจกต์

1. เปิดไฟล์ *.env* และวางเทมเพลตดังต่อไปนี้:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

> [!NOTE]
> หากต้องการหากุญแจ API และจุดเชื่อมต่อ คุณสามารถดูได้ที่ [set-up-azure-ai.md](../set-up-azure-ai.md)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อนได้ เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ควรใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดจากการใช้การแปลนี้