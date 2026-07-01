# Настройване на Azure AI

Използвайте това ръководство, когато искате да конфигурирате Azure OpenAI за превод на текст и Azure AI Vision за извличане на текст от изображения.

## Предпоставки

- Абонамент за Azure.
- Разрешение за създаване или използване на ресурси на Azure AI и разгръщания на модели.
- Проект в Azure AI Foundry или еквивалентен достъп до ресурси на Azure OpenAI и Azure AI Vision.

## Създаване на проект в Azure AI

1. Отворете [Azure AI Foundry](https://ai.azure.com).
2. Създайте или изберете проект.
3. Създайте или изберете AI hub за проекта.
4. Отворете прегледа на проекта след създаването.

## Разгръщане на модел на Azure OpenAI

1. В проекта отворете **Models + endpoints**.
2. Изберете **Deploy model**.
3. Изберете GPT модел, като например `gpt-4o`.
4. Разгърнете модела.
5. Запишете endpoint-а, името на разгръщането, името на модела, API ключа и версията на API-то.

!!! note
    Версията на Azure OpenAI API е отделна от версията на модела, показана в Azure AI Foundry. Изберете поддържана версия на API за вашето разгръщане.

## Конфигуриране на Azure AI Vision

Преводът на изображения използва Azure AI Vision за извличане на текста от изходните изображения, преди текстът да бъде преведен.

Във вашия проект в Azure AI намерете ключа и endpoint-а на Azure AI Services.

![Намерете информация за услугата Azure AI](../../assets/find-azure-ai-info.png)

Запишете:

- Endpoint на Azure AI Service
- API ключ на Azure AI Service

## Променливи на средата

Добавете идентификационните данни във вашия `.env` файл или CI secrets.

```bash
# Azure AI Vision, необходим за превод на изображения
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, необходим за превод на текст
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator също поддържа опционални резервни комплекти с идентификационни данни. Дублирайте пълен комплект от доставчик с суфикси като `_1` или `_2`; всички променливи в резервния комплект трябва да имат един и същ суфикс.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Следващи стъпки

- Върнете се към [Configuration](configuration.md) за да настроите локални или CI променливи на средата.
- Използвайте [CLI Reference](cli.md) за команди за превод.
- Използвайте [GitHub Actions](github-actions.md) за автоматизиране на pull request-ове за преводи.