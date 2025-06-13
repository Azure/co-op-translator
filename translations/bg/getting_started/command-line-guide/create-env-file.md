<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:29:25+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "bg"
}
-->
# Създайте файла *.env* в главната директория

В този урок ще ви покажем как да настроите променливите на средата за услугите на Azure чрез файл *.env*. Променливите на средата ви позволяват да управлявате сигурно чувствителни данни, като API ключове, без да ги вграждате директно в кода си.

> [!IMPORTANT]
> - Не е необходимо да конфигурирате повече от една услуга за езиков модел (Azure OpenAI или OpenAI). Попълнете променливите на средата за предпочитаната от вас услуга. Ако са зададени променливи за няколко езикови модела, кооперативният преводач ще избере една според приоритета.
> - Ако променливите за Computer Vision не са зададени, преводачът автоматично ще премине в [режим само с Markdown](./markdown-only-mode.md).

> [!NOTE]
> Този наръчник е основно насочен към услугите на Azure, но можете да изберете всеки поддържан езиков модел от [списъка с поддържани модели и услуги](../README.md#-supported-models-and-services).

## Създайте файла *.env*

В главната директория на проекта си създайте файл с име *.env*. Този файл ще съхранява всички ваши променливи на средата в прост формат.

> [!WARNING]
> Не качвайте файла *.env* в системи за контрол на версиите като Git. Добавете *.env* към вашия .gitignore, за да предотвратите случайни качвания.

1. Отидете в главната директория на проекта си.

1. Създайте файл *.env* в главната директория на проекта.

1. Отворете файла *.env* и поставете следния шаблон:

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
> Ако искате да намерите вашите API ключове и крайни точки, можете да се обърнете към [set-up-azure-ai.md](../set-up-azure-ai.md).

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.