<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:30:20+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "uk"
}
-->
# Створіть файл *.env* у кореневій директорії

У цьому посібнику ми допоможемо вам налаштувати змінні середовища для сервісів Azure за допомогою файлу *.env*. Змінні середовища дозволяють безпечно керувати конфіденційними даними, такими як API-ключі, без необхідності жорстко вписувати їх у код.

> [!IMPORTANT]
> - Потрібно налаштувати лише один сервіс мовної моделі (Azure OpenAI або OpenAI). Заповніть змінні середовища для обраного сервісу. Якщо налаштовано змінні для кількох мовних моделей, кооперативний перекладач вибере одну за пріоритетом.
> - Якщо змінні середовища для Computer Vision не встановлені, перекладач автоматично перейде в [режим лише Markdown](./markdown-only-mode.md).

> [!NOTE]
> Цей посібник зосереджений переважно на сервісах Azure, але ви можете обрати будь-яку підтримувану мовну модель зі списку [підтримуваних моделей і сервісів](../README.md#-supported-models-and-services).

## Створіть файл *.env*

У кореневій директорії вашого проєкту створіть файл із назвою *.env*. У цьому файлі зберігатимуться всі ваші змінні середовища у простому форматі.

> [!WARNING]
> Не додавайте файл *.env* до систем контролю версій, таких як Git. Додайте *.env* до файлу .gitignore, щоб уникнути випадкових комітів.

1. Перейдіть до кореневої директорії вашого проєкту.

1. Створіть файл *.env* у кореневій директорії проєкту.

1. Відкрийте файл *.env* і вставте наступний шаблон:

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
> Якщо ви хочете знайти свої API-ключі та кінцеві точки, зверніться до [set-up-azure-ai.md](../set-up-azure-ai.md).

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.