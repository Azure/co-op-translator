# GitHub Actions

Використовуйте GitHub Actions, коли ви хочете, щоб репозиторій автоматично перекладав змінені документи та створював pull request з отриманими результатами.

Почніть зі стандартної налаштування `GITHUB_TOKEN`, включно з репозиторіями організації, де це дозволено політикою. Див. [GitHub App Setup](#github-app-setup), якщо ваша організація вимагає ідентичності App або вам потрібні автоматичні запуски підлеглих workflow.

**Ручні правки:** ці workflow повністю повторно перекладають змінені вихідні файли і можуть перезаписати формулювання, відредаговані в їхніх перекладах. Переглядайте кожний PR перед злиттям. Збереження змін Markdown на рівні блоків для прийнятих правок потребує спеціальної інтеграції з [провайдером стану перекладу Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Ваш перший PR перекладу README

Почніть з одного кореневого `README.md` і однієї цільової мови. Цей workflow перекладає лише Markdown, тому Azure AI Vision не потрібен.

1. Скопіюйте [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([переглянути шаблон на GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) до `.github/workflows/translate-readme.yml` у репозиторії, який ви хочете перекласти, і закомітьте його в гілку за замовчуванням цього репозиторію. Шаблон використовує кореневу Action в `Azure/co-op-translator@main`, яка встановлює CLI з того ж source ref. Закріпіть перевірений коміт для відтворюваних запусків.
2. Відкрийте **Actions > Translate README > Run workflow**, виберіть мову і залиште позначеним **Лише попередній перегляд**. Перегляньте оцінку токена у кроці попереднього перегляду. Попередній перегляд не викликає провайдерів моделей, не записує переклади і не створює PR.
3. Додайте секрети для одного [text provider](#prerequisites), і увімкніть **Дозволити GitHub Actions створювати та схвалювати pull requests** у **Settings > Actions > General**. Шаблон запитує `contents: write` та `pull-requests: write` для своєї задачі; вам не потрібно змінювати дозволи за замовчуванням для кожного workflow. Якщо політика організації блокує ці дозволи або цю настройку, зверніться до адміністратора щодо схваленого [GitHub App](#github-app-setup).
4. Запустіть workflow знову з вимкненим прапорцем **Лише попередній перегляд**. Він виконує попередній перегляд, перекладає, запускає `co-op-review --readme-only`, і створює або оновлює PR перекладу тільки після успішного перекладу та перевірки. Підсумок workflow містить посилання на PR.
5. Перегляньте формулювання та зміни файлів у PR, потім зливайте, коли будете готові. Workflow не зливає автоматично.

У PR міститься лише `translations/<language>/README.md` та його файл метаданих мови. Вихідний README залишається незмінним, а посилання на інші документи продовжують вказувати на вихідні документи. Тіло PR перелічує змінені файли та результати структурної перевірки. Якщо переклад або перевірка не вдаються, перегляньте підсумок workflow та логи неуспішних кроків; PR не створюється. Якщо змін немає, новий PR не потрібен.

**Примітка для організацій і CI:** GitHub App є опційним, а не вимогою власності організації. З `GITHUB_TOKEN` workflow для створення, оновлення або повторного відкриття pull request вимагає, щоб користувач з правами запису обрав **Approve workflows to run**. Push-workflow не запускаються цим токеном. Для ненаглядного downstream CI див. [GitHub App Setup](#github-app-setup) та правила тригерів workflow GitHub [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Попередні умови

Перед створенням workflow налаштуйте секрети сервісів ШІ, які потрібні для запуску перекладу.

Текстовий переклад вимагає одного провайдера мовної моделі:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Для перекладу зображень додатково потрібен Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Див. [Configuration](configuration.md) та [Azure AI Setup](azure-ai-setup.md) для деталей локального налаштування.

## Стандартне налаштування

Після випробування workflow для README використайте це налаштування, щоб перекладати Markdown-файли репозиторію на кілька мов. Воно виконує перевірку Markdown перед відкриттям PR і не вимагає Azure AI Vision.

### Крок 1: Додайте секрети репозиторію

У вашому цільовому репозиторії відкрийте **Settings** > **Secrets and variables** > **Actions**, потім додайте секрети провайдера, які використовуватиме ваш workflow.

![Вибрати секрети Actions](../../assets/github-actions/select-setting-action.png)

### Крок 2: Увімкніть дозволи workflow

Відкрийте **Settings** > **Actions** > **General**.

У розділі **Workflow permissions**:

1. Увімкніть **Дозволити GitHub Actions створювати та схвалювати pull requests**.
2. Збережіть налаштування.

Нижче наведена задача явно запитує `contents: write` та `pull-requests: write`. Залиште дозволи workflow за замовчуванням для репозиторію без змін. Якщо політика організації блокує створення PR, зверніться до адміністратора щодо схваленого [GitHub App](#github-app-setup).

### Крок 3: Додайте workflow

Створіть `.github/workflows/co-op-translator.yml`:

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

Змініть `TARGET_LANGUAGES` на мови, які потрібні вашому проєкту. Перевірка використовує Python API для перевірки лише Markdown, відповідно до кроку перекладу. Помилка перекладу або перевірки зупиняє задачу до створення PR. Workflow не зливає PR автоматично. Для великих репозиторіїв додайте фільтр `paths:` під `on.push`, щоб workflow запускався лише при змінах документації.

### Опційно: блокноти і зображення

Для блокнотів додайте `-nb` до команди перекладу та встановіть `notebook=True` у кроці перевірки. Для тексту на зображеннях налаштуйте два [Azure AI Vision secrets](#prerequisites), передайте їх у `env` кроку перекладу, додайте `-img` до команди та додайте `translated_images/` до `add-paths` кроку PR. Переглядайте перекладені зображення візуально; детерміністична перевірка не гарантує точність тексту на зображеннях або лінгвістичну точність.

## Налаштування GitHub App

Використовуйте схвалений GitHub App, коли ваша організація вимагає ідентичності App, або коли згенерований PR має запускати downstream CI без кроку затвердження `GITHUB_TOKEN`. App не обходить політику організації; адміністратори все одно контролюють його встановлення та дозволи.

### Крок 1: Створіть або встановіть GitHub App

Використовуйте наявний App, наданий організацією, якщо він доступний, або створіть один із правами read/write для **Contents** та **Pull requests**. Встановіть його в цільовому репозиторії з необхідним схваленням організації.

Запишіть:

- App ID
- Вміст приватного ключа

Збережіть їх як секрети репозиторію:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Крок 2: Згенеруйте токен App

Додайте цей крок безпосередньо перед існуючим кроком pull request. Для шаблону README використайте ту ж умову успішності, щоб попередні перегляди та неуспішні переклади не вимагали токен App:

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

Потім змініть лише `token` вхід існуючого кроку pull request на `${{ steps.generate_token.outputs.token }}`. Збережіть без змін його умову успішності, гілку, тіло PR та `add-paths`. Токен за замовчуванням обмежений поточним репозиторієм. Коли ви адаптовуєте стандартне налаштування замість шаблону README, опустіть наведений `if` вище: той workflow використовує умову успішності за замовчуванням, тож створення токена і створення PR виконуються лише після успішного перекладу та перевірки.

Див. офіційну дію [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) для встановлення та дозволів токена.

## Обмеження раннера

GitHub-хостовані раннери мають максимальну тривалість задачі. Великі репозиторії або багато цільових мов можуть перевищити цей ліміт.

Для великих робочих навантажень перекладу:

- Перекладайте менше мов за запуск.
- Використовуйте прапорці контенту, такі як `-md`, `-nb` або `-img`.
- Використовуйте self-hosted runner, коли розмір репозиторію або затримка моделі робить хостовані раннери ненадійними.

## Перевірка в CI

Використовуйте `co-op-review`, коли pull request має перевіряти згенеровані переклади без виклику LLM або Vision провайдерів.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` — це бета-версія детерміністичної команди перевірки. Її перевірки та схема виводу можуть розвиватися, але вона призначена бути безпечною для CI, оскільки не записує файли і не викликає провайдерів моделей.