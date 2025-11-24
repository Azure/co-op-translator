<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-11-24T06:39:40+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "kn"
}
-->
# ಮೂಲ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ *.env* ಫೈಲ್ ಅನ್ನು ರಚಿಸಿ

ಈ ಪಾಠದಲ್ಲಿ, *.env* ಫೈಲ್ ಬಳಸಿ Azure ಸೇವೆಗಳಿಗಾಗಿ ನಿಮ್ಮ ಪರಿಸರ ವ್ಯತ್ಯಯಗಳನ್ನು ಹೊಂದಿಸುವ ಪ್ರಕ್ರಿಯೆಯನ್ನು ನಾವು ನಿಮಗೆ ಮಾರ್ಗದರ್ಶನ ಮಾಡುತ್ತೇವೆ. ಪರಿಸರ ವ್ಯತ್ಯಯಗಳು API ಕೀಗಳು ಮುಂತಾದ ಸಂವೇದನಶೀಲ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ನಿಮ್ಮ ಕೋಡ್‌ಬೇಸ್‌ನಲ್ಲಿ ನೇರವಾಗಿ ಹಾರ್ಡ್-ಕೋಡ್ ಮಾಡದೆ ಸುರಕ್ಷಿತವಾಗಿ ನಿರ್ವಹಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ.

> [!IMPORTANT]
> - ಒಂದೇ ಭಾಷಾ ಮಾದರಿ ಸೇವೆ (Azure OpenAI ಅಥವಾ OpenAI) ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಬೇಕಾಗಿದೆ. ನಿಮ್ಮ ಇಚ್ಛಿತ ಸೇವೆಗೆ ಸಂಬಂಧಿಸಿದ ಪರಿಸರ ವ್ಯತ್ಯಯಗಳನ್ನು ತುಂಬಿ. ಬಹು ಭಾಷಾ ಮಾದರಿಗಳಿಗಾಗಿ ಪರಿಸರ ವ್ಯತ್ಯಯಗಳನ್ನು ಹೊಂದಿಸಿದರೆ, ಸಹಕರಿಸುವ ಅನುವಾದಕವು ಆದ್ಯತೆಯ ಆಧಾರದ ಮೇಲೆ ಒಂದನ್ನು ಆಯ್ಕೆ ಮಾಡುತ್ತದೆ.
> - ಕಂಪ್ಯೂಟರ್ ವಿಸನ್ ಪರಿಸರ ವ್ಯತ್ಯಯಗಳನ್ನು ಹೊಂದಿಸದಿದ್ದರೆ, ಅನುವಾದಕವು ಸ್ವಯಂಚಾಲಿತವಾಗಿ [Markdown-only mode](./markdown-only-mode.md) ಗೆ ಬದಲಾಯಿಸುತ್ತದೆ.

> [!NOTE]
> ಈ ಮಾರ್ಗದರ್ಶನವು ಮುಖ್ಯವಾಗಿ Azure ಸೇವೆಗಳ ಮೇಲೆ ಕೇಂದ್ರೀಕೃತವಾಗಿದೆ, ಆದರೆ ನೀವು [ಆಧಾರಿತ ಮಾದರಿಗಳು ಮತ್ತು ಸೇವೆಗಳ ಪಟ್ಟಿ](../README.md#-supported-models-and-services) ಯಿಂದ ಯಾವುದೇ ಬೆಂಬಲಿತ ಭಾಷಾ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆ ಮಾಡಬಹುದು.

## *.env* ಫೈಲ್ ಅನ್ನು ರಚಿಸಿ

ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಮೂಲ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ *.env* ಎಂಬ ಫೈಲ್ ಅನ್ನು ರಚಿಸಿ. ಈ ಫೈಲ್ ನಿಮ್ಮ ಎಲ್ಲಾ ಪರಿಸರ ವ್ಯತ್ಯಯಗಳನ್ನು ಸರಳ ಸ್ವರೂಪದಲ್ಲಿ ಸಂಗ್ರಹಿಸುತ್ತದೆ.

> [!WARNING]
> ನಿಮ್ಮ *.env* ಫೈಲ್ ಅನ್ನು Git ಮುಂತಾದ ಆವೃತ್ತಿ ನಿಯಂತ್ರಣ ವ್ಯವಸ್ಥೆಗಳಿಗೆ ಕಮಿಟ್ ಮಾಡಬೇಡಿ. *.env* ಅನ್ನು ನಿಮ್ಮ .gitignore ಫೈಲ್‌ಗೆ ಸೇರಿಸಿ, ಆಕಸ್ಮಿಕ ಕಮಿಟ್‌ಗಳನ್ನು ತಡೆಯಲು.

1. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಮೂಲ ಡೈರೆಕ್ಟರಿಗೆ ಹೋಗಿ.

1. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಮೂಲ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ *.env* ಫೈಲ್ ಅನ್ನು ರಚಿಸಿ.

1. *.env* ಫೈಲ್ ಅನ್ನು ತೆರೆಯಿ ಮತ್ತು ಕೆಳಗಿನ ಟೆಂಪ್ಲೇಟ್ ಅನ್ನು ಪೇಸ್ಟ್ ಮಾಡಿ:

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
> ನಿಮ್ಮ API ಕೀಗಳು ಮತ್ತು ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಹುಡುಕಲು ನೀವು [set-up-azure-ai.md](../set-up-azure-ai.md) ಅನ್ನು ಉಲ್ಲೇಖಿಸಬಹುದು.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->