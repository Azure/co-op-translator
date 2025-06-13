<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:25:55+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "pa"
}
-->
# ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ *.env* ਫਾਈਲ ਬਣਾਓ

ਇਸ ਟਿਊਟੋਰਿਯਲ ਵਿੱਚ, ਅਸੀਂ ਤੁਹਾਨੂੰ Azure ਸੇਵਾਵਾਂ ਲਈ ਆਪਣੇ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਸ ਨੂੰ *.env* ਫਾਈਲ ਦੀ ਵਰਤੋਂ ਨਾਲ ਸੈੱਟ ਕਰਨ ਦੀ ਰਾਹਦਾਰੀ ਕਰਾਂਗੇ। ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਤੁਹਾਨੂੰ ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ ਸੰਵੇਦਨਸ਼ੀਲ ਕ੍ਰੈਡੈਂਸ਼ਲ ਜਿਵੇਂ ਕਿ API ਕੁੰਜੀਆਂ ਬਿਨਾਂ ਕੋਡ ਵਿੱਚ ਸਿੱਧਾ ਲਿਖੇ ਹੋਏ ਸੰਭਾਲਣ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ।

> [!IMPORTANT]
> - ਸਿਰਫ਼ ਇੱਕ ਭਾਸ਼ਾ ਮਾਡਲ ਸੇਵਾ (Azure OpenAI ਜਾਂ OpenAI) ਨੂੰ ਕਨਫਿਗਰ ਕਰਨ ਦੀ ਲੋੜ ਹੈ। ਆਪਣੇ ਮਨਪਸੰਦ ਸੇਵਾ ਲਈ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਭਰੋ। ਜੇ ਕਈ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਲਈ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈੱਟ ਕੀਤੇ ਗਏ ਹਨ, ਤਾਂ ਕੋ-ਆਪ ਟ੍ਰਾਂਸਲੇਟਰ ਪ੍ਰਾਥਮਿਕਤਾ ਦੇ ਅਧਾਰ 'ਤੇ ਇੱਕ ਚੁਣੇਗਾ।
> - ਜੇ Computer Vision ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈੱਟ ਨਹੀਂ ਹਨ, ਤਾਂ ਟ੍ਰਾਂਸਲੇਟਰ ਆਪਣੇ ਆਪ [Markdown-ਕੇਵਲ ਮੋਡ](./markdown-only-mode.md) 'ਤੇ ਚੱਲ ਜਾਵੇਗਾ।

> [!NOTE]
> ਇਹ ਗਾਈਡ ਮੁੱਖ ਤੌਰ 'ਤੇ Azure ਸੇਵਾਵਾਂ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਦੀ ਹੈ, ਪਰ ਤੁਸੀਂ [supported models and services list](../README.md#-supported-models-and-services) ਵਿੱਚੋਂ ਕਿਸੇ ਵੀ ਸਮਰਥਿਤ ਭਾਸ਼ਾ ਮਾਡਲ ਨੂੰ ਚੁਣ ਸਕਦੇ ਹੋ।

## *.env* ਫਾਈਲ ਬਣਾਓ

ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦੀ ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ, *.env* ਨਾਮਕ ਇੱਕ ਫਾਈਲ ਬਣਾਓ। ਇਹ ਫਾਈਲ ਸਾਰੇ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਸ ਨੂੰ ਸਧਾਰਣ ਫਾਰਮੈਟ ਵਿੱਚ ਸਟੋਰ ਕਰੇਗੀ।

> [!WARNING]
> ਆਪਣੀ *.env* ਫਾਈਲ ਨੂੰ Git ਵਰਗੇ ਵਰਜ਼ਨ ਕੰਟਰੋਲ ਸਿਸਟਮਾਂ ਵਿੱਚ ਕਮੇਟ ਨਾ ਕਰੋ। ਅਚਾਨਕ ਕਮੇਟ ਤੋਂ ਬਚਣ ਲਈ *.env* ਨੂੰ ਆਪਣੀ .gitignore ਫਾਈਲ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ।

1. ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦੀ ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ।

1. ਪ੍ਰੋਜੈਕਟ ਦੀ ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ *.env* ਫਾਈਲ ਬਣਾਓ।

1. *.env* ਫਾਈਲ ਖੋਲ੍ਹੋ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤਾ ਟੈਮਪਲੇਟ ਪੇਸਟ ਕਰੋ:

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
> ਜੇ ਤੁਸੀਂ ਆਪਣੀਆਂ API ਕੁੰਜੀਆਂ ਅਤੇ ਐਂਡਪੌਇੰਟ ਲੱਭਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ [set-up-azure-ai.md](../set-up-azure-ai.md) ਨੂੰ ਦੇਖ ਸਕਦੇ ਹੋ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਿਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਣ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ਾਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਉੱਪਜਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।