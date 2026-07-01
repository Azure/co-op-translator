# Pag-setup ng Azure AI

Gamitin ang gabay na ito kapag nais mong i-configure ang Azure OpenAI para sa pagsasalin ng teksto at ang Azure AI Vision para sa pagkuha ng teksto mula sa mga larawan.

## Mga Kinakailangan

- Isang Azure subscription.
- Pahintulot na gumawa o gumamit ng mga Azure AI resources at mga deployment ng modelo.
- Isang proyekto sa Azure AI Foundry o katumbas na access sa mga Azure OpenAI at Azure AI Vision na resources.

## Lumikha ng Proyekto sa Azure AI

1. Buksan ang [Azure AI Foundry](https://ai.azure.com).
2. Lumikha o pumili ng isang proyekto.
3. Lumikha o pumili ng AI hub para sa proyekto.
4. Buksan ang overview ng proyekto pagkatapos ng paglikha.

## I-deploy ang Azure OpenAI na Modelo

1. Sa proyekto, buksan ang **Models + endpoints**.
2. Piliin ang **Deploy model**.
3. Pumili ng GPT na modelo tulad ng `gpt-4o`.
4. I-deploy ang modelo.
5. Itala ang endpoint, deployment name, model name, API key, at API version.

!!! note
    Ang bersyon ng Azure OpenAI API ay hiwalay mula sa bersyon ng modelo na ipinapakita sa Azure AI Foundry. Pumili ng isang sinusuportahang API version para sa iyong deployment.

## I-configure ang Azure AI Vision

Gumagamit ang pagsasalin ng imahe ng Azure AI Vision upang kunin ang teksto mula sa mga larawan ng pinagmulan bago isalin ang teksto.

Sa iyong Azure AI proyekto, hanapin ang Azure AI Services key at endpoint.

![Hanapin ang impormasyon ng serbisyo ng Azure AI](../../assets/find-azure-ai-info.png)

Itala:

- Endpoint ng Azure AI Service
- API key ng Azure AI Service

## Mga Environment Variables

Idagdag ang mga kredensyal sa iyong `.env` file o CI secrets.

```bash
# Azure AI Vision, kinakailangan para sa pagsasalin ng imahe
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, kinakailangan para sa pagsasalin ng teksto
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

## Mga Susunod na Hakbang

- Bumalik sa [Configuration](configuration.md) upang i-configure ang lokal o CI environment variables.
- Gamitin ang [CLI Reference](cli.md) para sa mga command ng pagsasalin.
- Gamitin ang [GitHub Actions](github-actions.md) upang awtomatihin ang mga pull request para sa pagsasalin.