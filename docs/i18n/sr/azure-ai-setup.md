# Постављање Azure AI

Користите овај водич када желите да конфигуришете Azure OpenAI за превођење текста и Azure AI Vision за извлачење текста из слика.

## Претпоставке

- Azure претплата.
- Дозвола за креирање или коришћење Azure AI ресурса и распоређивања модела.
- Пројекат у Azure AI Foundry или еквивалентан приступ ресурсима Azure OpenAI и Azure AI Vision.

## Креирање Azure AI пројекта

1. Отворите [Azure AI Foundry](https://ai.azure.com).
2. Креирајте или изаберите пројекат.
3. Креирајте или изаберите AI хаб за пројекат.
4. Отворите преглед пројекта након креирања.

## Распоређивање Azure OpenAI модела

1. У пројекту отворите **Models + endpoints**.
2. Изаберите **Deploy model**.
3. Изаберите GPT модел као што је `gpt-4o`.
4. Распоредите модел.
5. Забележите endpoint, име распоређивања, име модела, API кључ и верзију API-ја.

!!! note
    Azure OpenAI API верзија је одвојена од верзије модела која је приказана у Azure AI Foundry. Изаберите подржану верзију API-ја за ваше распоређивање.

## Конфигурисање Azure AI Vision

Превођење слика користи Azure AI Vision за извлачење текста из изворних слика пре него што се текст преведе.

У вашем Azure AI пројекту пронађите Azure AI Services кључ и ендпоинт.

![Пронађите информације о Azure AI сервису](../../assets/find-azure-ai-info.png)

Record:

- Azure AI Service ендпоинт
- Azure AI Service API кључ

## Променљиве окружења

Додајте акредитиве у ваш `.env` фајл или CI тајне.

```bash
# Azure AI Vision, потребно за превођење слика
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, потребно за превођење текста
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator такође подржава опционе резервне сете акредитива. Дуплирајте комплетан скуп провајдера са суфиксима као што су `_1` или `_2`; све променљиве у резервном скупу морају делити исти суфикс.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Следећи кораци

- Вратите се на [Configuration](configuration.md) да подесите локалне или CI променљиве окружења.
- Користите [CLI референца](cli.md) за команде превођења.
- Користите [GitHub Actions](github-actions.md) за аутоматизацију pull request-ова за превођење.