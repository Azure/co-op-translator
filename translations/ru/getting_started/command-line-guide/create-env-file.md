<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-05-07T14:11:05+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ru"
}
-->
# Создайте файл *.env* в корневой директории

В этом руководстве мы расскажем, как настроить переменные окружения для сервисов Azure с помощью файла *.env*. Переменные окружения позволяют безопасно управлять конфиденциальными данными, такими как API-ключи, без их жесткого прописывания в коде.

> [!IMPORTANT]
> - Необходимо настроить только один сервис языковой модели (Azure OpenAI или OpenAI). Заполните переменные окружения для выбранного вами сервиса. Если заданы переменные для нескольких языковых моделей, кооперативный переводчик выберет одну на основе приоритета.
> - Если переменные окружения для Computer Vision не заданы, переводчик автоматически переключится в [режим только Markdown](./markdown-only-mode.md).

> [!NOTE]
> Это руководство в первую очередь ориентировано на сервисы Azure, но вы можете выбрать любую поддерживаемую языковую модель из [списка поддерживаемых моделей и сервисов](../README.md#-supported-models-and-services).

## Создайте файл *.env*

В корневой директории вашего проекта создайте файл с именем *.env*. В этом файле будут храниться все переменные окружения в простом формате.

> [!WARNING]
> Не добавляйте файл *.env* в систему контроля версий, такую как Git. Добавьте *.env* в файл .gitignore, чтобы избежать случайных коммитов.

1. Перейдите в корневую директорию вашего проекта.

1. Создайте файл *.env* в корневой директории вашего проекта.

1. Откройте файл *.env* и вставьте следующий шаблон:

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
> Если вы хотите найти свои API-ключи и конечные точки, обратитесь к [set-up-azure-ai.md](../set-up-azure-ai.md).

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, пожалуйста, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.