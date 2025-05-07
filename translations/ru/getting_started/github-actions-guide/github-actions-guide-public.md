<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "87bf95d45e684475ef1e67d8dae5f6eb",
  "translation_date": "2025-05-06T18:12:08+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "ru"
}
-->
# Использование Co-op Translator GitHub Action (Публичная настройка)

**Целевая аудитория:** Это руководство предназначено для пользователей большинства публичных или приватных репозиториев, где достаточно стандартных прав GitHub Actions. В нем используется встроенный `GITHUB_TOKEN`.

Автоматизируйте перевод документации вашего репозитория с помощью Co-op Translator GitHub Action. В этом руководстве показано, как настроить действие для автоматического создания pull request с обновленными переводами при изменении исходных Markdown-файлов или изображений.

> [!IMPORTANT]
>
> **Выбор правильного руководства:**
>
> Это руководство описывает **более простую настройку с использованием стандартного `GITHUB_TOKEN`**. Этот способ рекомендуется большинству пользователей, так как не требует управления конфиденциальными ключами GitHub App Private Keys.
>

## Требования

Перед настройкой GitHub Action убедитесь, что у вас есть необходимые учетные данные для AI-сервисов.

**1. Обязательно: учетные данные для языковой модели AI**  
Вам нужны учетные данные хотя бы для одной поддерживаемой языковой модели:

- **Azure OpenAI**: требуется Endpoint, API Key, имена моделей/развертываний, версия API.  
- **OpenAI**: требуется API Key, (опционально: Org ID, базовый URL, ID модели).  
- Подробнее см. в разделе [Supported Models and Services](../../../../README.md).  
- Руководство по настройке: [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. По желанию: учетные данные Computer Vision (для перевода изображений)**

- Требуются только если нужно переводить текст на изображениях.  
- **Azure Computer Vision**: необходимы Endpoint и Subscription Key.  
- Если не указаны, действие работает в [режиме только Markdown](../markdown-only-mode.md).  
- Руководство по настройке: [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Настройка и конфигурация

Выполните следующие шаги, чтобы настроить Co-op Translator GitHub Action в вашем репозитории с использованием стандартного `GITHUB_TOKEN`.

### Шаг 1: Понимание аутентификации (с использованием `GITHUB_TOKEN`)

Этот workflow использует встроенный `GITHUB_TOKEN`, предоставляемый GitHub Actions. Этот токен автоматически предоставляет workflow права на взаимодействие с вашим репозиторием в соответствии с настройками, заданными в **Шаге 3**.

### Шаг 2: Настройка секретов репозитория

Вам нужно добавить **учетные данные AI-сервисов** в виде зашифрованных секретов в настройках репозитория.

1. Перейдите в нужный репозиторий на GitHub.  
2. Откройте **Settings** > **Secrets and variables** > **Actions**.  
3. В разделе **Repository secrets** нажмите **New repository secret** для каждого требуемого секрета AI-сервиса из списка ниже.

![Select setting action](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png) *(Скриншот: где добавлять секреты)*

**Обязательные секреты AI-сервисов (добавьте ВСЕ, что требуется согласно вашим требованиям):**

| Название секрета                  | Описание                                    | Источник значения                |
| :-------------------------------- | :------------------------------------------ | :------------------------------- |
| `AZURE_SUBSCRIPTION_KEY`            | Ключ для Azure AI Service (Computer Vision)  | Ваша Azure AI Foundry            |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint для Azure AI Service (Computer Vision) | Ваша Azure AI Foundry            |
| `AZURE_OPENAI_API_KEY`              | Ключ для Azure OpenAI сервиса                | Ваша Azure AI Foundry            |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint для Azure OpenAI сервиса             | Ваша Azure AI Foundry            |
| `AZURE_OPENAI_MODEL_NAME`           | Имя модели Azure OpenAI                        | Ваша Azure AI Foundry            |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Имя развертывания Azure OpenAI                    | Ваша Azure AI Foundry            |
| `AZURE_OPENAI_API_VERSION`          | Версия API для Azure OpenAI                      | Ваша Azure AI Foundry            |
| `OPENAI_API_KEY`                    | API Key для OpenAI                             | Ваша OpenAI Platform             |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (опционально)            | Ваша OpenAI Platform             |
| `OPENAI_CHAT_MODEL_ID`              | Конкретный ID модели OpenAI (опционально)         | Ваша OpenAI Platform             |
| `OPENAI_BASE_URL`                   | Кастомный базовый URL OpenAI API (опционально)    | Ваша OpenAI Platform             |

### Шаг 3: Настройка прав workflow

GitHub Action требует прав, предоставляемых через `GITHUB_TOKEN`, чтобы получать код и создавать pull request.

1. В вашем репозитории перейдите в **Settings** > **Actions** > **General**.  
2. Пролистайте до раздела **Workflow permissions**.  
3. Выберите **Read and write permissions**. Это даст `GITHUB_TOKEN` необходимые права `contents: write` и `pull-requests: write` для данного workflow.  
4. Убедитесь, что галочка **Allow GitHub Actions to create and approve pull requests** установлена.  
5. Нажмите **Save**.

![Permission setting](../../../../getting_started/github-actions-guide/imgs/permission-setting.png)

### Шаг 4: Создание файла workflow

В конце создайте YAML-файл, который определит автоматический workflow с использованием `GITHUB_TOKEN`.

1. В корневой папке вашего репозитория создайте директорию `.github/workflows/`, если ее нет.  
2. Внутри `.github/workflows/` создайте файл с именем `co-op-translator.yml`.  
3. Вставьте в `co-op-translator.yml` следующий контент.

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
4. **Настройте workflow под себя:**  
  - **[!IMPORTANT] Целевые языки:** при необходимости измените в шаге `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request`.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.