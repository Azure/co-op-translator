<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:26:30+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "pl"
}
-->
# Utwórz plik *.env* w katalogu głównym

W tym poradniku przeprowadzimy Cię przez proces konfiguracji zmiennych środowiskowych dla usług Azure za pomocą pliku *.env*. Zmienne środowiskowe pozwalają bezpiecznie zarządzać poufnymi danymi, takimi jak klucze API, bez konieczności umieszczania ich bezpośrednio w kodzie.

> [!IMPORTANT]
> - Wystarczy skonfigurować tylko jedną usługę modelu językowego (Azure OpenAI lub OpenAI). Wypełnij zmienne środowiskowe dla wybranej usługi. Jeśli ustawione są zmienne dla kilku modeli językowych, tłumacz współpracujący wybierze jeden na podstawie priorytetu.
> - Jeśli zmienne środowiskowe dla Computer Vision nie są ustawione, tłumacz automatycznie przełączy się na [tryb tylko Markdown](./markdown-only-mode.md).

> [!NOTE]
> Ten przewodnik koncentruje się głównie na usługach Azure, ale możesz wybrać dowolny obsługiwany model językowy z listy [supported models and services](../README.md#-supported-models-and-services).

## Utwórz plik *.env*

W katalogu głównym projektu utwórz plik o nazwie *.env*. Plik ten będzie przechowywał wszystkie zmienne środowiskowe w prostym formacie.

> [!WARNING]
> Nie dodawaj pliku *.env* do systemów kontroli wersji, takich jak Git. Dodaj *.env* do pliku .gitignore, aby uniknąć przypadkowego zatwierdzenia.

1. Przejdź do katalogu głównego swojego projektu.

1. Utwórz plik *.env* w katalogu głównym projektu.

1. Otwórz plik *.env* i wklej następujący szablon:

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
> Jeśli chcesz znaleźć swoje klucze API i punkty końcowe, możesz skorzystać z [set-up-azure-ai.md](../set-up-azure-ai.md).

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić poprawność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o krytycznym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.