# Azure AI nustatymas

Use this guide when you want to configure Azure OpenAI for text translation and Azure AI Vision for image text extraction.

## Išankstiniai reikalavimai

- Azure prenumerata.
- Teisė sukurti arba naudoti Azure AI išteklius ir modelių diegimus.
- Projektas Azure AI Foundry arba lygiavertis prieigos prie Azure OpenAI ir Azure AI Vision išteklių.

## Sukurti Azure AI projektą

1. Atidarykite [Azure AI Foundry](https://ai.azure.com).
2. Sukurkite arba pasirinkite projektą.
3. Sukurkite arba pasirinkite AI hubą projektui.
4. Atidarykite projekto apžvalgą po sukūrimo.

## Diegti Azure OpenAI modelį

1. Projekte atidarykite **Models + endpoints**.
2. Pasirinkite **Deploy model**.
3. Pasirinkite GPT modelį, pvz., `gpt-4o`.
4. Įdiekite modelį.
5. Užsirašykite endpointą, diegimo pavadinimą, modelio pavadinimą, API raktą ir API versiją.

!!! note
    Azure OpenAI API version is separate from the model version shown in Azure AI Foundry. Choose a supported API version for your deployment.

## Konfigūruoti Azure AI Vision

Image translation uses Azure AI Vision to extract text from source images before the text is translated.

Savo Azure AI projekte suraskite Azure AI Services raktą ir endpointą.

![Suraskite Azure AI paslaugos informaciją](../../assets/find-azure-ai-info.png)

Record:

- Azure AI Service endpoint
- Azure AI Service API key

## Aplinkos kintamieji

Add the credentials to your `.env` file or CI secrets.

```bash
# Azure AI Vision, reikalingas vaizdų vertimui
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, reikalingas tekstų vertimui
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

## Tolimesni veiksmai

- Grįžkite į [Configuration](configuration.md) to set up local or CI environment variables.
- Use [CLI Reference](cli.md) for translation commands.
- Use [GitHub Actions](github-actions.md) to automate translation pull requests.