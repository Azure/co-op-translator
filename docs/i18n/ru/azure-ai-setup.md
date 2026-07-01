# Настройка Azure AI

Используйте это руководство, когда нужно настроить Azure OpenAI для перевода текста и Azure AI Vision для извлечения текста из изображений.

## Предварительные требования

- Подписка Azure.
- Разрешение на создание или использование ресурсов Azure AI и развертываний моделей.
- Проект в Azure AI Foundry или эквивалентный доступ к ресурсам Azure OpenAI и Azure AI Vision.

## Создание проекта Azure AI

1. Откройте [Azure AI Foundry](https://ai.azure.com).
2. Создайте или выберите проект.
3. Создайте или выберите AI-хаб для проекта.
4. Откройте обзор проекта после создания.

## Развертывание модели Azure OpenAI

1. В проекте откройте **Models + endpoints**.
2. Выберите **Deploy model**.
3. Выберите модель GPT, например `gpt-4o`.
4. Разверните модель.
5. Зафиксируйте endpoint, имя развертывания, имя модели, API-ключ и версию API.

!!! note
    Версия API Azure OpenAI отличается от версии модели, отображаемой в Azure AI Foundry. Выберите поддерживаемую версию API для вашего развертывания.

## Настройка Azure AI Vision

Перевод изображений использует Azure AI Vision для извлечения текста из исходных изображений перед их переводом.

В вашем проекте Azure AI найдите ключ и endpoint службы Azure AI Services.

![Найдите информацию об службе Azure AI](../../assets/find-azure-ai-info.png)

Record:

- Endpoint службы Azure AI
- API-ключ службы Azure AI

## Переменные окружения

Добавьте учетные данные в файл `.env` или в секреты CI.

```bash
# Azure AI Vision, необходим для перевода изображений
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, необходим для перевода текста
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator также поддерживает дополнительные наборы учетных данных для резервного варианта. Дублируйте полный набор поставщика с суффиксами, такими как `_1` или `_2`; все переменные в наборе резервных учетных данных должны иметь одинаковый суффикс.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Следующие шаги

- Вернитесь к [Configuration](configuration.md), чтобы настроить локальные или CI-переменные окружения.
- Используйте [Справочник CLI](cli.md) для команд перевода.
- Используйте [GitHub Actions](github-actions.md) для автоматизации pull-запросов перевода.