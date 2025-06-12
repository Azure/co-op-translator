<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T12:39:24+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ur"
}
-->
# *.env* فائل کو روٹ ڈائریکٹری میں بنائیں

اس ٹیوٹوریل میں، ہم آپ کو Azure سروسز کے لیے اپنے ماحول کے متغیرات کو *.env* فائل کے ذریعے سیٹ کرنے کا طریقہ بتائیں گے۔ ماحول کے متغیرات آپ کو حساس اسناد، جیسے API کیز، کو محفوظ طریقے سے منظم کرنے کی اجازت دیتے ہیں بغیر انہیں کوڈ میں سختی سے لکھے۔

> [!IMPORTANT]
> - صرف ایک زبان ماڈل سروس (Azure OpenAI یا OpenAI) کو ترتیب دینا ضروری ہے۔ اپنی پسندیدہ سروس کے لیے ماحول کے متغیرات بھریں۔ اگر متعدد زبان ماڈلز کے ماحول کے متغیرات سیٹ کیے گئے ہیں، تو co-op translator ترجیح کی بنیاد پر ایک منتخب کرے گا۔
> - اگر Computer Vision کے ماحول کے متغیرات سیٹ نہیں کیے گئے، تو translator خود بخود [Markdown-only mode](./markdown-only-mode.md) پر سوئچ کر جائے گا۔

> [!NOTE]
> یہ رہنمائی بنیادی طور پر Azure سروسز پر مرکوز ہے، لیکن آپ [supported models and services list](../README.md#-supported-models-and-services) میں سے کسی بھی سپورٹڈ زبان ماڈل کو منتخب کر سکتے ہیں۔

## *.env* فائل بنائیں

اپنے پروجیکٹ کی روٹ ڈائریکٹری میں، *.env* نامی فائل بنائیں۔ یہ فائل تمام ماحول کے متغیرات کو آسان فارمیٹ میں محفوظ کرے گی۔

> [!WARNING]
> اپنی *.env* فائل کو ورژن کنٹرول سسٹمز جیسے Git میں commit نہ کریں۔ غلطی سے commit ہونے سے بچنے کے لیے *.env* کو اپنی .gitignore فائل میں شامل کریں۔

1. اپنے پروجیکٹ کی روٹ ڈائریکٹری پر جائیں۔

1. پروجیکٹ کی روٹ ڈائریکٹری میں *.env* فائل بنائیں۔

1. *.env* فائل کھولیں اور درج ذیل ٹیمپلیٹ پیسٹ کریں:

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
> اگر آپ اپنی API کیز اور endpoints تلاش کرنا چاہتے ہیں تو آپ [set-up-azure-ai.md](../set-up-azure-ai.md) دیکھ سکتے ہیں۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات کا خیال رکھیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔