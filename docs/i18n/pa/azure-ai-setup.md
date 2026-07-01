# Azure AI ਸੈੱਟਅਪ

Use this guide when you want to configure Azure OpenAI for text translation and Azure AI Vision for image text extraction.

## ਲੋੜੀਂਦੀਆਂ ਸ਼ਰਤਾਂ

- ਇੱਕ Azure subscription.
- Azure AI ਸਰੋਤਾਂ ਅਤੇ ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ ਬਣਾਉਣ ਜਾਂ ਵਰਤਣ ਦੀ ਇਜਾਜ਼ਤ।
- Azure AI Foundry ਵਿੱਚ ਇੱਕ ਪ੍ਰੋਜੈਕਟ ਜਾਂ Azure OpenAI ਅਤੇ Azure AI Vision ਸਰੋਤਾਂ ਤੱਕ ਸਮਾਨ ਪਹੁੰਚ।

## ਇੱਕ Azure AI ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ

1. [Azure AI Foundry](https://ai.azure.com) ਖੋਲ੍ਹੋ।
2. ਇੱਕ ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ ਜਾਂ ਚੁਣੋ।
3. ਪ੍ਰੋਜੈਕਟ ਲਈ ਇੱਕ AI ਹੱਬ ਬਣਾਓ ਜਾਂ ਚੁਣੋ।
4. ਬਣਾਉਣ ਤੋਂ ਬਾਅਦ ਪ੍ਰੋਜੈਕਟ ਓਵਰਵਿਊ ਖੋਲ੍ਹੋ।

## ਇੱਕ Azure OpenAI ਮਾਡਲ ਡਿਪਲੌਇ ਕਰੋ

1. ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ, **Models + endpoints** ਖੋਲ੍ਹੋ।
2. **Deploy model** ਚੁਣੋ।
3. `gpt-4o` ਵਰਗਾ ਕੋਈ GPT ਮਾਡਲ ਚੁਣੋ।
4. ਮਾਡਲ ਡਿਪਲੌਇ ਕਰੋ।
5. endpoint, deployment name, model name, API key, ਅਤੇ API version ਨੂੰ ਦਰਜ ਕਰੋ।

!!! note
    Azure OpenAI ਦੀ API ਵਰਜਨ Azure AI Foundry ਵਿੱਚ ਦਿਖਾਏ ਗਏ ਮਾਡਲ ਵਰਜਨ ਤੋਂ ਵੱਖਰਾ ਹੁੰਦੀ ਹੈ। ਆਪਣੇ ਡਿਪਲੌਇਮੈਂਟ ਲਈ ਇੱਕ ਸਹਾਇਤ ਕੀਤੀ ਗਈ API ਵਰਜਨ ਚੁਣੋ।

## Azure AI Vision ਸੰਰਚਿਤ ਕਰੋ

Image translation uses Azure AI Vision to extract text from source images before the text is translated.

In your Azure AI project, find the Azure AI Services key and endpoint.

![Azure AI ਸੇਵਾ ਦੀ ਜਾਣਕਾਰੀ ਲੱਭੋ](../../assets/find-azure-ai-info.png)

Record:

- Azure AI Service ਦਾ endpoint
- Azure AI Service ਦਾ API key

## ਮਾਹੌਲ ਵੈਰੀਏਬਲ

Add the credentials to your `.env` file or CI secrets.

```bash
# ਤਸਵੀਰਾਂ ਦੇ ਅਨੁਵਾਦ ਲਈ Azure AI Vision ਦੀ ਲੋੜ ਹੈ
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# ਟੈਕਸਟ ਅਨੁਵਾਦ ਲਈ Azure OpenAI ਦੀ ਲੋੜ ਹੈ
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator also supports optional fallback credential sets. Duplicate a complete provider set with suffixes such as `_1` or `_2`; all variables in a fallback set must share the same suffix.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## ਅਗਲੇ ਕਦਮ

- ਲੋਕਲ ਜਾਂ CI environment variables ਸੈੱਟ ਕਰਨ ਲਈ [Configuration](configuration.md) 'ਤੇ ਵਾਪਸ ਜਾਓ।
- ਤਰਜਮੇ ਦੇ ਕਮਾਂਡਾਂ ਲਈ [CLI Reference](cli.md) ਵਰਤੋ।
- ਤਰਜਮੇ pull requests ਨੂੰ ਆਟੋਮੇਟ ਕਰਨ ਲਈ [GitHub Actions](github-actions.md) ਵਰਤੋ।