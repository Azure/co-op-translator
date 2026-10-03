# GitHub Actions

Используйте GitHub Actions, когда вы хотите, чтобы репозиторий автоматически переводил изменённую документацию и открывал pull request с созданными результатами.

Начните со стандартной настройки `GITHUB_TOKEN`, включая репозитории организации, если политика это позволяет. См. [GitHub App Setup](#github-app-setup), когда вашей организации требуется идентичность приложения или вам нужны автоматические запуски downstream-воркфлоу.

**Ручные правки:** эти рабочие процессы повторно переводят изменённые исходные файлы полностью и могут перезаписать формулировки, отредактированные в их переводах. Просматривайте каждый PR перед слиянием. Сохранение принятых правок на уровне блоков Markdown требует пользовательской интеграции с [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Ваш первый PR перевода README

Начните с одного корневого `README.md` и одного целевого языка. Этот рабочий процесс переводит только Markdown, поэтому Azure AI Vision не требуется.

1. Скопируйте [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([просмотреть шаблон на GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) в `.github/workflows/translate-readme.yml` в репозитории, который вы хотите перевести, и закоммитьте его в ветку по умолчанию этого репозитория. Шаблон использует корневое Action в `Azure/co-op-translator@main`, которое устанавливает CLI из того же исходного рефа. Зафиксируйте проверенный коммит для воспроизводимых запусков.
2. Откройте **Actions > Translate README > Run workflow**, выберите язык и оставьте включённой опцию **Preview only**. Просмотрите оценку токенов на шаге предварительного просмотра. Предварительный просмотр не обращается к поставщикам моделей, не записывает переводы и не создаёт PR.
3. Добавьте секреты для одного [поставщика текста](#prerequisites), и включите **Разрешить GitHub Actions создавать и одобрять pull requests** в **Настройки > Actions > Общие**. Шаблон запрашивает `contents: write` и `pull-requests: write` для своей задачи; вам не нужно менять стандартные разрешения для каждого рабочего процесса. Если политика организации блокирует эти разрешения или этот параметр, обратитесь к администратору по поводу утверждённого [приложения GitHub](#github-app-setup).
4. Запустите рабочий процесс снова с отключённой опцией **Preview only**. Он выполняет предварительный просмотр, переводит, запускает `co-op-review --readme-only` и создаёт или обновляет PR с переводом только после успешного завершения перевода и проверки. В сводке рабочего процесса есть ссылка на PR.
5. Проверьте формулировки и изменения файлов в PR, затем выполняйте merge, когда будете готовы. Рабочий процесс не выполняет слияние автоматически.

PR содержит только `translations/<language>/README.md` и связанный файл метаданных языка. Исходный README остаётся без изменений, а ссылки на другие документы продолжают указывать на исходные документы. Тело PR перечисляет изменённые файлы и результаты структурной проверки. Если перевод или проверка не удались, просмотрите сводку рабочего процесса и журналы неудачных шагов; PR не создаётся. Если изменений нет, новый PR не требуется.

**Organization and CI note:** GitHub App является опциональным и не обязательным для владения организацией. С `GITHUB_TOKEN` рабочие процессы pull request для открытия, обновления или повторного открытия PR требуют, чтобы пользователь с правами записи выбрал **Approve workflows to run**. Push-воркфлоу не запускаются с этим токеном. Для безнадзорного downstream CI смотрите [GitHub App Setup](#github-app-setup) и правила запуска воркфлоу GitHub'а [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Требования

Прежде чем создавать рабочий процесс, настройте секреты сервисов ИИ, которые потребуются вашему запуску перевода.

Для текстового перевода требуется один поставщик языковых моделей:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Для перевода изображений дополнительно требуется Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

См. [Configuration](configuration.md) и [Azure AI Setup](azure-ai-setup.md) для деталей локальной конфигурации.

## Стандартная настройка

После опробования рабочего процесса для README используйте эту настройку, чтобы переводить Markdown-файлы репозитория на несколько языков. Она выполняет проверку Markdown перед открытием PR и не требует Azure AI Vision.

### Шаг 1: Добавьте секреты репозитория

В целевом репозитории откройте **Settings** > **Secrets and variables** > **Actions**, затем добавьте секреты поставщика, которые будет использовать ваш рабочий процесс.

![Выберите секреты Actions](../../assets/github-actions/select-setting-action.png)

### Шаг 2: Включите разрешения для рабочих процессов

Откройте **Settings** > **Actions** > **General**.

В разделе **Workflow permissions**:

1. Включите **Разрешить GitHub Actions создавать и одобрять pull requests**.
2. Сохраните настройку.

Приведённая ниже задача явно запрашивает `contents: write` и `pull-requests: write`. Оставьте настройки разрешений рабочего процесса репозитория без изменений. Если политика организации блокирует создание PR, обратитесь к администратору по поводу утверждённого [GitHub App](#github-app-setup).

### Шаг 3: Добавьте рабочий процесс

Создайте `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

Измените `TARGET_LANGUAGES` на языки, которые нужны вашему проекту. Проверка использует Python API для проверки только Markdown, что соответствует шагу перевода. Ошибка перевода или проверки останавливает задачу до создания PR. Рабочий процесс не выполняет автоматическое слияние PR. Для больших репозиториев добавьте фильтр `paths:` под `on.push`, чтобы рабочий процесс запускался только при изменениях в документации.

### Дополнительно: ноутбуки и изображения

Для ноутбуков добавьте `-nb` к команде перевода и установите `notebook=True` в шаге проверки. Для текстов на изображениях настройте два [секрета Azure AI Vision](#prerequisites), передайте их в `env` шага перевода, добавьте `-img` к команде и включите `translated_images/` в `add-paths` шага PR. Просматривайте переведённые изображения визуально; детерминированная проверка не гарантирует корректность текста на изображениях или лингвистическую точность.

## Настройка GitHub App

Используйте утверждённый GitHub App, когда вашей организации требуется идентичность App или когда сгенерированный PR должен запускать downstream CI без шага одобрения `GITHUB_TOKEN`. Приложение не обходит политику организации; администраторы по-прежнему контролируют его установку и разрешения.

### Шаг 1: Создайте или установите GitHub App

Используйте существующее приложение, предоставленное организацией, если оно доступно, либо создайте одно с правами чтения/записи для **Contents** и **Pull requests**. Установите его в целевом репозитории с любой необходимой организационной авторизацией.

Запишите:

- ID приложения
- Содержимое приватного ключа

Сохраните их как секреты репозитория:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Шаг 2: Сгенерируйте токен приложения

Добавьте этот шаг непосредственно перед существующим шагом pull request. Для шаблона README используйте то же условие успеха, чтобы предпросмотры и неудачные переводы не запрашивали токен приложения:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

Затем измените только вход `token` у существующего шага pull request на `${{ steps.generate_token.outputs.token }}`. Сохраните его условие успеха, ветку, тело PR и `add-paths` без изменений. По умолчанию токен ограничен текущим репозиторием. При адаптации стандартной настройки вместо шаблона README опустите приведённый выше `if`: тот рабочий процесс использует условие успеха по умолчанию, поэтому создание токена и создание PR выполняются только после успешного перевода и проверки.

См. официальное действие [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) для установки и прав доступа токена.

## Ограничения раннера

GitHub-hosted раннеры имеют максимальную продолжительность задачи. Большие репозитории или множество целевых языков могут превысить это ограничение.

Для больших объёмов перевода:

- Переводите меньше языков за один запуск.
- Используйте флаги контента, такие как `-md`, `-nb` или `-img`.
- Используйте self-hosted раннер, когда размер репозитория или задержки модели делают hosted раннеры ненадёжными.

## Проверка в CI

Используйте `co-op-review`, когда pull request должен проверять сгенерированные переводы без обращения к LLM или Vision-поставщикам.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` — это бета-версия детерминированной команды проверки. Её проверки и схема вывода могут меняться, но она разработана безопасной для CI, поскольку не записывает файлы и не обращается к поставщикам моделей.