# Azure AI ಸೆಟ್‌ಅಪ್

ಈ ಮಾರ್ಗದರ್ಶನವನ್ನು ನೀವು ಪಠ್ಯ ಅನುವಾದಕ್ಕಾಗಿ Azure OpenAI ಮತ್ತು ಚಿತ್ರ ಪಠ್ಯ ಎಕ್ಸ್‌ಟ್ರಾಕ್ಷನ್‌ಗೆ Azure AI Vision ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಬೇಕಾದಾಗ ಬಳಸಿ.

## ಆವಶ್ಯಕತೆಗಳು

- Azure ಚಂದಾದಾರಿಕೆ.
- Azure AI ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಮಾದರಿ ನಿಯೋಜನೆಗಳನ್ನು ರಚಿಸಲು ಅಥವಾ ಬಳಸಲು ಅನುಮತಿ.
- Azure AI Foundry ನಲ್ಲಿ ಒಂದು ಯೋಜನೆ ಅಥವಾ Azure OpenAI ಮತ್ತು Azure AI Vision ಸಂಪನ್ಮೂಲಗಳಿಗೆ ಸಮತुल್ಯ ಪ್ರವೇಶ.

## Azure AI ಯೋಜನೆ ರಚಿಸಿ

1. [Azure AI Foundry](https://ai.azure.com) ತೆರೆಯಿರಿ.
2. ಯೋಜನೆಯನ್ನು ರಚಿಸಿ ಅಥವಾ ಆಯ್ಕೆಮಾಡಿ.
3. ಯೋಜನೆಗಾಗಿ AI ಹಬ್ ಅನ್ನು ರಚಿಸಿ ಅಥವಾ ಆಯ್ಕೆಮಾಡಿ.
4. ರಚನೆಯ ನಂತರ ಯೋಜನೆ ಅವಲೋಕನವನ್ನು ತೆರೆಯಿರಿ.

## Azure OpenAI ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿ

1. ಯೋಜನೆಯಲ್ಲಿ, **Models + endpoints** ತೆರೆಯಿರಿ.
2. **Deploy model** ಆಯ್ಕೆಮಾಡಿ.
3. `gpt-4o` ಹೀಗೆ GPT ಮಾದರಿಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.
4. ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿ.
5. ಎಂಡ್ಪಾಯಿಂಟ್, ನಿಯೋಜನೆಯ ಹೆಸರು, ಮಾದರಿ ಹೆಸರು, API ಕೀ ಮತ್ತು API ಆವೃತ್ತಿಯನ್ನು ದಾಖಲೆಮಾಡಿ.

!!! note
    The Azure OpenAI API version is separate from the model version shown in Azure AI Foundry. Choose a supported API version for your deployment.

## Azure AI Vision ಅನ್ನು ಸಂರಚಿಸಿ

ಚಿತ್ರ ಅನುವಾದಕ್ಕೆ ಮೊದಲಿಗೆ ಮೂಲ ಚಿತ್ರಗಳಿಂದ ಪಠ್ಯವನ್ನು ಎತ್ತಿಸಲು Azure AI Vision ಬಳಸಲಾಗುತ್ತದೆ ಮತ್ತು ನಂತರ ಪಠ್ಯವು ಅನುವಾದಿಸಲಾಗುತ್ತದೆ.

ನಿಮ್ಮ Azure AI ಯೋಜನೆಯಲ್ಲಿ, Azure AI Services ಕೀ ಮತ್ತು ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಹುಡುಕಿ.

![Azure AI ಸೇವಾ ಮಾಹಿತಿಯನ್ನು ಹುಡುಕಿ](../../assets/find-azure-ai-info.png)

ದಾಖಲೆ ಮಾಡಿ:

- Azure AI Service ಎಂಡ್ಪಾಯಿಂಟ್
- Azure AI Service API ಕೀ

## ಪರಿಸರ ಚರಗಳು

ನಿಮ್ಮ `.env` ಫೈಲ್ ಅಥವಾ CI ರಹಸ್ಯಗಳಿಗೆ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ಸೇರಿಸಿ.

```bash
# ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ ಅಗತ್ಯವಿರುವ Azure AI Vision
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# ಪಠ್ಯ ಅನುವಾದಕ್ಕಾಗಿ ಅಗತ್ಯವಿರುವ Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator ಆಯ್ಕೆಮಟ್ಟದ ಫಾಲ್ಬ್ಯಾಕ್ ಪ್ರಮಾಣಪತ್ರ ಸೆಟ್‌ಗಳನ್ನು ಸಹ ಬೆಂಬಲಿಸುತ್ತದೆ. ಪೂರ್ಣ ಪ್ರೊವೈಡರ್ ಸೆಟ್ ಅನ್ನು `_1` ಅಥವಾ `_2` ಎಂಬಂತಹ ಸಫಿಕ್ಸ್‌ಗಳೊಂದಿಗೆ ನಕಲಿಸಿ; ಫಾಲ್ಬ್ಯಾಕ್ ಸೆಟ್‌ನಲ್ಲಿರುವ ಎಲ್ಲಾ ಚರಗಳು ಒಂದೇ ಸಫಿಕ್ಸ್ ಅನ್ನು ಹಂಚಿಕೊಳ್ಳಬೇಕು.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## ಮುಂದಿನ ಹಂತಗಳು

- ಸ್ಥಳೀಯ ಅಥವಾ CI ಪರಿಸರ ಚರಗಳನ್ನು ಸಿದ್ಧಗೊಳಿಸಲು [Configuration](configuration.md) ಗೆ ಮರಳಿ ಹೋಗಿ.
- ಅನುವಾದ ಕಮಾಂಡ್‌ಗಳಿಗಾಗಿ [CLI Reference](cli.md) ಅನ್ನು ಬಳಸಿ.
- ಅನುವಾದ ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್‌ಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸಲು [GitHub Actions](github-actions.md) ಅನ್ನು ಬಳಸಿ.