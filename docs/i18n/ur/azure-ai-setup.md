# Azure AI سیٹ اپ

اس رہنما کو استعمال کریں جب آپ متن کا ترجمہ کرنے کے لیے Azure OpenAI اور تصویروں سے متن نکالنے کے لیے Azure AI Vision کو ترتیب دینا چاہتے ہوں۔

## ضروریات

- ایک Azure سبسکرپشن۔
- Azure AI وسائل اور ماڈل ڈپلائمنٹس بنانے یا استعمال کرنے کی اجازت۔
- Azure AI Foundry میں ایک پروجیکٹ یا Azure OpenAI اور Azure AI Vision وسائل تک مساوی رسائی۔

## ایک Azure AI پروجیکٹ بنائیں

1. کھولیں [Azure AI Foundry](https://ai.azure.com).
2. ایک پروجیکٹ بنائیں یا منتخب کریں۔
3. پروجیکٹ کے لیے ایک AI ہب بنائیں یا منتخب کریں۔
4. تخلیق کے بعد پروجیکٹ کا جائزہ کھولیں۔

## ایک Azure OpenAI ماڈل تعینات کریں

1. پروجیکٹ میں، **Models + endpoints** کھولیں۔
2. منتخب کریں **Deploy model**۔
3. ایک GPT ماڈل منتخب کریں مثلاً `gpt-4o`۔
4. ماڈل کو تعینات کریں۔
5. endpoint، deployment name، model name، API key، اور API version کو ریکارڈ کریں۔

!!! note
    Azure OpenAI API ورژن Azure AI Foundry میں دکھائے جانے والے ماڈل ورژن سے الگ ہوتا ہے۔ اپنے ڈیپلائمنٹ کے لیے ایک سپورٹ شدہ API ورژن منتخب کریں۔

## Azure AI Vision کو ترتیب دیں

امیج ترجمہ متن کے ترجمے سے قبل ماخذ تصاویر سے متن نکالنے کے لیے Azure AI Vision استعمال کرتا ہے۔

اپنے Azure AI پروجیکٹ میں، Azure AI Services کی key اور endpoint تلاش کریں۔

![Azure AI سروس کی معلومات تلاش کریں](../../assets/find-azure-ai-info.png)

ریکارڈ کریں:

- Azure AI Service کا endpoint
- Azure AI Service کی API key

## ماحول کے متغیرات

اپنے `.env` فائل یا CI secrets میں اسناد شامل کریں۔

```bash
# تصویری ترجمے کے لیے Azure AI Vision ضروری ہے
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# متنی ترجمے کے لیے Azure OpenAI ضروری ہے
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator اختیاری fallback credential sets کو بھی سپورٹ کرتا ہے۔ کسی مکمل provider سیٹ کی نقل بنائیں اور اسے `_1` یا `_2` جیسے suffix سے ختم کریں؛ fallback سیٹ میں موجود تمام متغیرات کو ایک ہی suffix ہونا ضروری ہے۔

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## اگلے اقدامات

- لوکل یا CI ماحول کے متغیرات ترتیب دینے کے لیے [Configuration](configuration.md) پر واپس جائیں۔
- ترجمے کے کمانڈز کے لیے [CLI Reference](cli.md) استعمال کریں۔
- ترجمہ pull requests کو خودکار بنانے کے لیے [GitHub Actions](github-actions.md) استعمال کریں۔