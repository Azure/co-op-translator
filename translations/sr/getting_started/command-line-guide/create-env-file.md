<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:29:33+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "sr"
}
-->
# Направите *.env* фајл у коренском директоријуму

У овом туторијалу ћемо вас провести кроз подешавање ваших променљивих окружења за Azure услуге користећи *.env* фајл. Променљиве окружења вам омогућавају да безбедно управљате осетљивим подацима, као што су API кључеви, без потребе да их уносите директно у код.

> [!IMPORTANT]
> - Потребно је конфигурисати само једну услугу језичког модела (Azure OpenAI или OpenAI). Попуните променљиве окружења за услугу коју користите. Ако су променљиве окружења подешене за више језичких модела, кооперативни преводилац ће одабрати један на основу приоритета.
> - Ако променљиве окружења за Computer Vision нису подешене, преводилац ће аутоматски прећи у [режим само за Markdown](./markdown-only-mode.md).

> [!NOTE]
> Овај водич је углавном фокусиран на Azure услуге, али можете одабрати било који подржани језички модел са листе [подржаних модела и услуга](../README.md#-supported-models-and-services).

## Направите *.env* фајл

У коренском директоријуму вашег пројекта, направите фајл под именом *.env*. Овај фајл ће чувати све ваше променљиве окружења у једноставном формату.

> [!WARNING]
> Не шаљите ваш *.env* фајл у системе за контролу верзија као што је Git. Додајте *.env* у ваш .gitignore фајл како бисте спречили случајне комите.

1. Идите у коренски директоријум вашег пројекта.

1. Направите *.env* фајл у коренском директоријуму вашег пројекта.

1. Отворите *.env* фајл и налепите следећи шаблон:

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
> Ако желите да пронађете ваше API кључеве и крајње тачке, можете погледати [set-up-azure-ai.md](../set-up-azure-ai.md).

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произлазе из употребе овог превода.