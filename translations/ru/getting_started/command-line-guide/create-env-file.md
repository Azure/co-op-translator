<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "53c99ea0ead7a3500149d4bb96be5811",
  "translation_date": "2025-05-06T17:55:00+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ru"
}
-->
# Создайте файл *.env* в корневой директории

В этом руководстве мы покажем, как настроить переменные окружения для сервисов Azure с помощью файла *.env*. Переменные окружения позволяют безопасно управлять конфиденциальными данными, такими как API-ключи, без необходимости прописывать их напрямую в коде.

> [!IMPORTANT]
> - Необходимо настроить только один сервис языковой модели (Azure OpenAI или OpenAI). Заполните переменные окружения для выбранного вами сервиса. Если заданы переменные для нескольких моделей, Co-op Translator выберет одну из них по приоритету.
> - Если переменные окружения для Computer Vision не заданы, переводчик автоматически переключится в [режим только Markdown](./markdown-only-mode.md).

> [!NOTE]
> В этом руководстве основное внимание уделяется сервисам Azure, но вы можете выбрать любую поддерживаемую языковую модель из [списка поддерживаемых моделей и сервисов](../README.md#-supported-models-and-services).

## Создайте файл *.env*

В корневой директории вашего проекта создайте файл с именем *.env*. В этом файле будут храниться все ваши переменные окружения в простом формате.

> [!WARNING]
> Не добавляйте файл *.env* в систему контроля версий, например Git. Добавьте *.env* в файл .gitignore, чтобы избежать случайных коммитов.

1. Перейдите в корневую директорию вашего проекта.

1. Создайте файл *.env* в корневой директории проекта.

    ![Создание файла *.env*.](../../../../imgs/create-env.png)

1. Откройте файл *.env* и вставьте следующий шаблон:

    ```plaintext
    # Azure Credentials
    AZURE_SUBSCRIPTION_KEY="your_azure_AIServices_api_key"
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

## Соберите ваши учетные данные Azure

Вам понадобятся следующие учетные данные Azure для настройки окружения:

Все необходимые данные можно получить на странице обзора проекта в [AI Foundry](https://ai.azure.com/build/overview)

![Обзор Foundry](../../../../imgs/foundry-overview.png)


### Для Azure AI Service:

    - Azure Subscription Key: ваш API-ключ Azure AI Services, который позволяет получить доступ к сервисам Azure AI.
    - Azure AI Service Endpoint: URL конечной точки вашего конкретного сервиса Azure AI.

### Для Azure OpenAI Service:

    - Azure OpenAI API Key: API-ключ для доступа к сервисам Azure OpenAI.
    - Azure OpenAI Endpoint: URL конечной точки вашего сервиса Azure OpenAI.


1. Скопируйте и вставьте ваш ключ AI Services и Endpoint в файл *.env*.
2. Скопируйте и вставьте ваш Azure OpenAI API Key и Endpoint в файл *.env*.

### Детали модели

Выберите Модель и Конечные точки в левом меню

![Модели Foundry](../../../../imgs/gpt-models.png)

Теперь нужно выбрать модель, которую вы хотите использовать, чтобы получить детали модели

![Детали модели](../../../../imgs/model-deployment-name.png)

Для файла .env нам нужны следующие данные:

    - Azure OpenAI Model Name: имя модели, с которой вы будете работать.
    - Azure OpenAI Name: имя вашей развертки для моделей Azure OpenAI.
    - Azure OpenAI API Version: версия API Azure OpenAI, которую вы используете, указана в конце строки URL.

Чтобы получить эти данные, выберите развертку модели

![Информация о модели Foundry](../../../../imgs/foundry-model-info.png)

### Добавьте переменные окружения Azure

3. Скопируйте и вставьте ваше Azure OpenAI **Name** и версию модели **Version** в файл *.env*.
4. Сохраните файл *.env*.
5. Теперь вы можете использовать эти переменные окружения для работы с **Co-op Translator** и вашими сервисами Azure.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.