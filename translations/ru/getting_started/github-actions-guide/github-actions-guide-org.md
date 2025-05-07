<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c437820027c197f25fb2cbee95bae28c",
  "translation_date": "2025-05-06T18:05:04+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "ru"
}
-->
# Использование Co-op Translator GitHub Action (Руководство для организаций)

**Целевая аудитория:** Это руководство предназначено для **внутренних пользователей Microsoft** или **команд, имеющих доступ к необходимым учетным данным для предустановленного GitHub App Co-op Translator** или способных создать собственное GitHub App.

Автоматизируйте перевод документации вашего репозитория с помощью Co-op Translator GitHub Action. В этом руководстве показано, как настроить действие для автоматического создания pull request с обновленными переводами при изменении исходных Markdown-файлов или изображений.

> [!IMPORTANT]
> 
> **Выбор подходящего руководства:**
>
> Это руководство описывает настройку с использованием **GitHub App ID и приватного ключа**. Обычно метод «Руководство для организаций» необходим, если: **`GITHUB_TOKEN` Права ограничены:** Ваша организация или настройки репозитория ограничивают стандартные права, предоставляемые стандартному `GITHUB_TOKEN`. В частности, если `GITHUB_TOKEN` не имеет необходимых прав `write` (например, `contents: write` или `pull-requests: write`), рабочий процесс из [Публичного руководства по настройке](./github-actions-guide-public.md) не сможет работать из-за недостаточных прав. Использование выделенного GitHub App с явно назначенными правами обходит это ограничение.
>
> **Если это к вам не относится:**
>
> Если стандартный `GITHUB_TOKEN` имеет достаточные права в вашем репозитории (то есть организационные ограничения не мешают), используйте **[Публичное руководство по настройке с использованием GITHUB_TOKEN](./github-actions-guide-public.md)**. Публичное руководство не требует получения или управления App ID и приватными ключами, а полагается только на стандартный `GITHUB_TOKEN` и права репозитория.

## Предварительные требования

Перед настройкой GitHub Action убедитесь, что у вас есть необходимые учетные данные для AI-сервисов.

**1. Обязательно: Учетные данные для языковой модели AI**  
Вам нужны учетные данные хотя бы для одной поддерживаемой языковой модели:

- **Azure OpenAI**: Требуются Endpoint, API Key, имена моделей/развертываний, версия API.  
- **OpenAI**: Требуется API Key, (необязательно: Org ID, Base URL, Model ID).  
- Подробнее в разделе [Поддерживаемые модели и сервисы](../../../../README.md).  
- Руководство по настройке: [Настройка Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. По желанию: Учетные данные Computer Vision (для перевода изображений)**

- Требуется только если нужно переводить текст на изображениях.  
- **Azure Computer Vision**: Требуются Endpoint и Subscription Key.  
- Если не предоставлены, действие работает в [режиме только Markdown](../markdown-only-mode.md).  
- Руководство по настройке: [Настройка Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Настройка и конфигурация

Следуйте этим шагам для настройки Co-op Translator GitHub Action в вашем репозитории:

### Шаг 1: Установка и настройка аутентификации GitHub App

Рабочий процесс использует аутентификацию через GitHub App для безопасного взаимодействия с вашим репозиторием (например, для создания pull request) от вашего имени. Выберите один из вариантов:

#### **Вариант A: Установить предустановленный Co-op Translator GitHub App (для внутреннего использования Microsoft)**

1. Перейдите на страницу [Co-op Translator GitHub App](https://github.com/apps/co-op-translator).

1. Нажмите **Install** и выберите аккаунт или организацию, где находится ваш целевой репозиторий.

    ![Установка приложения](../../../../getting_started/github-actions-guide/imgs/install-app.png)

1. Выберите **Only select repositories** и отметьте ваш целевой репозиторий (например, `PhiCookBook`). Нажмите **Install**. Вас могут попросить пройти аутентификацию.

    ![Авторизация установки](../../../../getting_started/github-actions-guide/imgs/install-authorize.png)

1. **Получение учетных данных приложения (требуется внутренний процесс):** Чтобы рабочий процесс мог аутентифицироваться как приложение, вам нужны две информации от команды Co-op Translator:  
  - **App ID:** Уникальный идентификатор приложения Co-op Translator. App ID: `1164076`.  
  - **Приватный ключ:** Получите **полное содержимое** файла приватного ключа `.pem` у контактного лица по поддержке. **Обращайтесь с ключом как с паролем и храните его в безопасности.**

1. Перейдите к шагу 2.

#### **Вариант B: Использовать собственный кастомный GitHub App**

- При желании создайте и настройте собственное GitHub App. Убедитесь, что оно имеет права на чтение и запись Contents и Pull requests. Вам понадобятся его App ID и сгенерированный приватный ключ.

### Шаг 2: Настройка секретов репозитория

Добавьте учетные данные GitHub App и AI-сервисов в виде зашифрованных секретов в настройках репозитория.

1. Перейдите в ваш целевой репозиторий GitHub (например, `PhiCookBook`).

1. Откройте **Settings** > **Secrets and variables** > **Actions**.

1. В разделе **Repository secrets** нажмите **New repository secret** для каждого из перечисленных секретов.

   ![Выбор настроек Actions](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png)

**Обязательные секреты (для аутентификации GitHub App):**

| Имя секрета          | Описание                                      | Источник значения                             |
| :------------------- | :--------------------------------------------- | :--------------------------------------------- |
| `GH_APP_ID`          | App ID GitHub App (из шага 1).                  | Настройки GitHub App                          |
| `GH_APP_PRIVATE_KEY` | **Полное содержимое** скачанного файла `.pem`. | Файл `.pem` (из шага 1)            |

**Секреты AI-сервисов (добавьте ВСЕ, которые применимы согласно вашим требованиям):**

| Имя секрета                         | Описание                               | Источник значения                     |
| :---------------------------------- | :------------------------------------ | :----------------------------------- |
| `AZURE_SUBSCRIPTION_KEY`            | Ключ для Azure AI Service (Computer Vision)  | Azure AI Foundry                    |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint для Azure AI Service (Computer Vision) | Azure AI Foundry                   |
| `AZURE_OPENAI_API_KEY`              | Ключ для Azure OpenAI сервиса              | Azure AI Foundry                   |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint для Azure OpenAI сервиса         | Azure AI Foundry                   |
| `AZURE_OPENAI_MODEL_NAME`           | Имя вашей модели Azure OpenAI              | Azure AI Foundry                   |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Имя вашего развертывания Azure OpenAI         | Azure AI Foundry                   |
| `AZURE_OPENAI_API_VERSION`          | Версия API для Azure OpenAI              | Azure AI Foundry                   |
| `OPENAI_API_KEY`                    | API Key для OpenAI                        | OpenAI Platform                  |
| `OPENAI_ORG_ID`                     | ID организации OpenAI                    | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`              | Конкретный ID модели OpenAI                  | OpenAI Platform                  |
| `OPENAI_BASE_URL`                   | Пользовательский базовый URL API OpenAI                | OpenAI Platform                  |

![Добавление секретов](../../../../getting_started/github-actions-guide/imgs/add-secrets-done.png)

### Шаг 3: Создание файла рабочего процесса

В конце создайте YAML-файл, который определяет автоматизированный рабочий процесс.

1. В корневой папке вашего репозитория создайте каталог `.github/workflows/`, если он еще не существует.

1. Внутри `.github/workflows/` создайте файл с именем `co-op-translator.yml`.

1. Вставьте следующий контент в co-op-translator.yml.

```
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
          # Azure AI Service Credentials
          AZURE_SUBSCRIPTION_KEY: ${{ secrets.AZURE_SUBSCRIPTION_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
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

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
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

4.  **Настройка рабочего процесса:**  
  - **[!IMPORTANT] Целевые языки:** В `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` step if needed.

## Credential Management and Renewal

- **Security:** Always store sensitive credentials (API keys, private keys) as GitHub Actions secrets. Never expose them in your workflow file or repository code.
- **[!IMPORTANT] Key Renewal (Internal Microsoft Users):** Be aware that Azure OpenAI key used within Microsoft might have a mandatory renewal policy (e.g., every 5 months). Ensure you update the corresponding GitHub secrets (`AZURE_OPENAI_...` ключах) **до их истечения**, чтобы избежать сбоев рабочего процесса.

## Запуск рабочего процесса

После того, как файл `co-op-translator.yml` будет слит в вашу основную ветку (или ветку, указанную в фильтре `on:` trigger), the workflow will automatically run whenever changes are pushed to that branch (and match the `paths`, если настроено),

если переводы созданы или обновлены, действие автоматически создаст Pull Request с изменениями, готовый для вашего просмотра и слияния.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.