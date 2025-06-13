<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a52587a512e667f70d92db853d3c61d5",
  "translation_date": "2025-06-12T19:35:06+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "bg"
}
-->
# Използване на Co-op Translator GitHub Action (Публична настройка)

**Целева аудитория:** Този наръчник е предназначен за потребители в повечето публични или частни хранилища, където стандартните разрешения на GitHub Actions са достатъчни. Той използва вградения `GITHUB_TOKEN`.

Автоматизирайте превода на документацията във вашето хранилище лесно с помощта на Co-op Translator GitHub Action. Този наръчник ви води през настройката на действието, за да създава автоматично pull request-и с обновени преводи винаги, когато се променят изходните Markdown файлове или изображения.

> [!IMPORTANT]
>
> **Избор на правилния наръчник:**
>
> Този наръчник описва **по-лесната настройка с използване на стандартния `GITHUB_TOKEN`**. Това е препоръчителният метод за повечето потребители, тъй като не изисква управление на чувствителни GitHub App Private Keys.
>

## Предварителни изисквания

Преди да конфигурирате GitHub Action, уверете се, че разполагате с необходимите идентификационни данни за AI услугата.

**1. Задължително: Идентификационни данни за AI езиков модел**  
Необходими са ви идентификационни данни поне за един от поддържаните езикови модели:

- **Azure OpenAI**: Изисква Endpoint, API Key, имена на Модел/Деплоймънт, версия на API.
- **OpenAI**: Изисква API Key, (по избор: Org ID, Base URL, Model ID).
- Вижте [Supported Models and Services](../../../../README.md) за подробности.

**2. По избор: Идентификационни данни за AI Vision (за превод на изображения)**

- Необходими само ако трябва да превеждате текст в изображения.
- **Azure AI Vision**: Изисква Endpoint и Subscription Key.
- Ако не са предоставени, действието по подразбиране работи в [Markdown-only mode](../markdown-only-mode.md).

## Настройка и конфигурация

Следвайте тези стъпки, за да конфигурирате Co-op Translator GitHub Action във вашето хранилище, използвайки стандартния `GITHUB_TOKEN`.

### Стъпка 1: Разберете автентикацията (Използване на `GITHUB_TOKEN`)

Този workflow използва вградения `GITHUB_TOKEN`, предоставен от GitHub Actions. Токенът автоматично дава на workflow необходимите разрешения да взаимодейства с вашето хранилище според настройките, зададени в **Стъпка 3**.

### Стъпка 2: Конфигурирайте тайните на хранилището

Трябва само да добавите вашите **идентификационни данни за AI услугите** като криптирани тайни в настройките на хранилището.

1. Отидете в целевото GitHub хранилище.
2. Изберете **Settings** > **Secrets and variables** > **Actions**.
3. Под **Repository secrets** кликнете **New repository secret** за всяка необходима AI услуга от списъка по-долу.

![Избор на действие за настройка](../../../../translated_images/select-setting-action.32e2394813d09dc148494f34daea40724f24ff406de889f26cbbbf05f98ed621.bg.png) *(Изображение: Показва къде се добавят тайни)*

**Задължителни тайни за AI услуги (Добавете ВСИЧКИ, които са приложими според вашите предварителни изисквания):**

| Име на тайната                      | Описание                                   | Източник на стойността           |
| :--------------------------------- | :----------------------------------------- | :------------------------------- |
| `AZURE_SUBSCRIPTION_KEY`            | Ключ за Azure AI услуга (Computer Vision)  | Вашият Azure AI Foundry           |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint за Azure AI услуга (Computer Vision) | Вашият Azure AI Foundry           |
| `AZURE_OPENAI_API_KEY`              | Ключ за Azure OpenAI услуга                 | Вашият Azure AI Foundry           |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint за Azure OpenAI услуга              | Вашият Azure AI Foundry           |
| `AZURE_OPENAI_MODEL_NAME`           | Име на вашия Azure OpenAI модел              | Вашият Azure AI Foundry           |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Име на вашия Azure OpenAI деплоймънт          | Вашият Azure AI Foundry           |
| `AZURE_OPENAI_API_VERSION`          | Версия на API за Azure OpenAI                | Вашият Azure AI Foundry           |
| `OPENAI_API_KEY`                    | API ключ за OpenAI                         | Вашата OpenAI платформа           |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (по избор)          | Вашата OpenAI платформа           |
| `OPENAI_CHAT_MODEL_ID`              | Конкретен OpenAI модел ID (по избор)         | Вашата OpenAI платформа           |
| `OPENAI_BASE_URL`                   | Персонализиран OpenAI API Base URL (по избор) | Вашата OpenAI платформа           |

### Стъпка 3: Конфигурирайте разрешенията на workflow

GitHub Action изисква разрешения, предоставени чрез `GITHUB_TOKEN`, за да проверява кода и да създава pull request-и.

1. В хранилището отидете на **Settings** > **Actions** > **General**.
2. Превъртете надолу до секцията **Workflow permissions**.
3. Изберете **Read and write permissions**. Това дава на `GITHUB_TOKEN` необходимите `contents: write` и `pull-requests: write` разрешения за този workflow.
4. Уверете се, че е отметнато полето **Allow GitHub Actions to create and approve pull requests**.
5. Натиснете **Save**.

![Настройка на разрешения](../../../../translated_images/permission-setting.cb1f57fdb5194f0743b1f6932f221e404ae2928ee88d77f1de39aba46fbf774a.bg.png)

### Стъпка 4: Създайте workflow файла

Накрая, създайте YAML файл, който дефинира автоматизирания workflow с използване на `GITHUB_TOKEN`.

1. В коренната директория на вашето хранилище създайте папката `.github/workflows/`, ако все още не съществува.
2. Вътре в `.github/workflows/` създайте файл с име `co-op-translator.yml`.
3. Поставете следното съдържание в `co-op-translator.yml`.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_SUBSCRIPTION_KEY: ${{ secrets.AZURE_SUBSCRIPTION_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```  
4. **Персонализирайте workflow-а:**  
  - **[!IMPORTANT] Целеви езици:** В стъпката `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` променете езиците, ако е необходимо.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.