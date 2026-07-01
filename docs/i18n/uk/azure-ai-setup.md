# Налаштування Azure AI

Використовуйте цей посібник, коли хочете налаштувати Azure OpenAI для перекладу тексту та Azure AI Vision для витягання тексту з зображень.

## Передумови

- Підписка Azure.
- Дозвіл на створення або використання ресурсів Azure AI та розгортань моделей.
- Проєкт у Azure AI Foundry або еквівалентний доступ до ресурсів Azure OpenAI та Azure AI Vision.

## Створення проєкту Azure AI

1. Open [Azure AI Foundry](https://ai.azure.com).
2. Створіть або виберіть проєкт.
3. Створіть або виберіть AI-хаб для проєкту.
4. Відкрийте огляд проєкту після створення.

## Розгорніть модель Azure OpenAI

1. У проєкті відкрийте **Models + endpoints**.
2. Виберіть **Deploy model**.
3. Виберіть модель GPT, наприклад `gpt-4o`.
4. Розгорніть модель.
5. Запишіть endpoint, назву розгортання, назву моделі, API-ключ та версію API.

!!! note
    Версія API Azure OpenAI відрізняється від версії моделі, показаної в Azure AI Foundry. Оберіть підтримувану версію API для вашого розгортання.

## Налаштування Azure AI Vision

Переклад зображень використовує Azure AI Vision для витягання тексту з вихідних зображень перед перекладом.

У вашому проєкті Azure AI знайдіть ключ Azure AI Services та endpoint.

![Знайдіть інформацію про службу Azure AI](../../assets/find-azure-ai-info.png)

Запишіть:

- Endpoint служби Azure AI
- API-ключ служби Azure AI

## Змінні середовища

Додайте облікові дані до вашого `.env` файлу або секретів CI.

```bash
# Azure AI Vision, необхідний для перекладу зображень
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, необхідний для перекладу тексту
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator також підтримує необов'язкові набори резервних облікових даних. Скопіюйте повний набір постачальника з суфіксами, наприклад `_1` або `_2`; усі змінні в резервному наборі повинні мати один і той же суфікс.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Наступні кроки

- Поверніться до [Конфігурація](configuration.md), щоб налаштувати локальні або CI змінні середовища.
- Використовуйте [Довідник CLI](cli.md) для команд перекладу.
- Використовуйте [GitHub Actions](github-actions.md) для автоматизації запитів на витяг перекладів.