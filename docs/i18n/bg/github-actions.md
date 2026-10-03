# GitHub Actions

Използвайте GitHub Actions, когато искате хранилище да превежда автоматично променената документация и да отвори pull request със създадените резултати.

Започнете със стандартната настройка на `GITHUB_TOKEN`, включително за организационни хранилища, където политиката го позволява. Вижте [Настройка на GitHub App](#github-app-setup) когато вашата организация изисква идентичност на App или имате нужда от автоматично изпълнение на downstream workflows.

**Човешки редакции:** тези workflow-ове прегенерират променените изходни файлове изцяло и могат да презапишат формулировки, редактирани в техните преводи. Прегледайте всеки PR преди сливане. Запазването на блоковите нива в Markdown за приетите редакции изисква персонална интеграция с [доставчик на състоянието на превода на Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Вашият първи README преводен PR

Започнете с един основен `README.md` и един целеви език. Този workflow превежда само Markdown, така че Azure AI Vision не е задължителен.

1. Копирайте [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([прегледайте шаблона в GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) в `.github/workflows/translate-readme.yml` в хранилището, което искате да преведете, и го комитнете в основния клон на това хранилище. Шаблонът използва root Action в `Azure/co-op-translator@main`, който инсталира CLI от същия source ref. За възпроизводими изпълнения закответе прегледан комит.
2. Отворете **Actions > Translate README > Run workflow**, изберете език и оставете **Preview only** отметнато. Прегледайте оценката за токени в стъпката за преглед. Preview не извиква доставчици на модели, не записва преводи и не създава PR.
3. Добавете секретите за един [доставчик на текст](#prerequisites) и разрешете **GitHub Actions да създава и одобрява pull requests** в **Настройки > Действия > Общи**. Шаблонът изисква `contents: write` и `pull-requests: write` за своята задача; не е нужно да променяте подразбиращите се разрешения за всеки работен процес. Ако организацията блокира тези разрешения или тази настройка, попитайте администратор за одобрен [Настройка на GitHub App](#github-app-setup).
4. Стартирайте workflow-а отново с **Preview only** без отметка. Той прави преглед, превежда, изпълнява `co-op-review --readme-only` и създава или обновява преводен PR само след като преводът и прегледът са успешни. Резюмето на workflow-а съдържа връзка към PR.
5. Прегледайте формулировките и промените по файловете в PR, след което го слейте, когато сте готови. Workflow-ът не слива автоматично.

PR-ът съдържа само `translations/<language>/README.md` и неговия езиков файл с метаданни. Източникът README остава непроменен и връзките към други документи продължават да сочат към източниковите документи. Тялото на PR изрежда променените файлове и резултатите от структурния преглед. Ако преводът или прегледът се провалят, инспектирайте резюмето на workflow-а и логовете на неуспешните стъпки; PR не се създава. Ако няма промени, нов PR не е необходим.

**Бележка за организацията и CI:** GitHub App е опция, а не изискване на организационното собственичество. С `GITHUB_TOKEN` workflow-ове за pull-request при отваряне, обновяване или повторно отваряне на PR изискват потребител с write достъп да избере **Approve workflows to run**. Push workflow-овете не се задействат от този токен. За автоматизиран downstream CI вижте [Настройка на GitHub App](#github-app-setup) и правилата на GitHub за [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Prerequisites

Преди да създадете workflow-а, конфигурирайте секретите за AI услугите, от които се нуждае вашето изпълнение на превода.

Текстовият превод изисква един доставчик на езиков модел:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, плюс по избор `OPENAI_ORG_ID` и `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, плюс по избор `ANTHROPIC_BASE_URL`

Преводът на изображения допълнително изисква Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Вижте [Configuration](configuration.md) и [Azure AI Setup](azure-ai-setup.md) за подробности относно локалната конфигурация.

## Стандартна настройка

След като изпробвате README workflow-а, използвайте тази настройка за превеждане на Markdown файловете на хранилището на няколко езика. Тя изпълнява Markdown преглед преди отваряне на PR и не изисква Azure AI Vision.

### Стъпка 1: Добавете секрети на хранилището

В целевото си хранилище отворете **Settings** > **Secrets and variables** > **Actions**, след което добавете секретите на доставчика, които вашият workflow ще използва.

![Изберете секрети за Actions](../../assets/github-actions/select-setting-action.png)

### Стъпка 2: Активирайте разрешенията за работния процес

Отворете **Settings** > **Actions** > **General**.

Под **Workflow permissions**:

1. Разрешете **GitHub Actions да създава и одобрява pull requests**.
2. Запазете настройката.

По-долу задачата изрично заявява `contents: write` и `pull-requests: write`. Оставете подразбиращите се разрешения за workflow-а на хранилището непроменени. Ако политиката на организацията блокира създаването на PR, попитайте администратор за одобрен [Настройка на GitHub App](#github-app-setup).

### Стъпка 3: Добавете работния процес

Създайте `.github/workflows/co-op-translator.yml`:

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

Променете `TARGET_LANGUAGES` на езиците, от които проектът ви се нуждае. Прегледът използва Python API, за да проверява само Markdown, съвпадайки със стъпката на превода. Грешка при превода или прегледа спира задачата преди създаване на PR. Workflow-ът не слива PR автоматично. За големи хранилища добавете филтър `paths:` под `on.push`, така че workflow-ът да се изпълнява само когато има промени в документацията.

### По избор: бележници и изображения

За notebooks добавете `-nb` към командата за превод и задайте `notebook=True` в стъпката за преглед. За текст в изображенията конфигурирайте двете [секрета на Azure AI Vision](#prerequisites), предайте ги в `env` на стъпката за превод, добавете `-img` към командата и добавете `translated_images/` към `add-paths` на PR стъпката. Преглеждайте преведените изображения визуално; детерминистичният преглед не сертифицира текста в изображенията или лингвистичната точност.

## Настройка на GitHub App

Използвайте одобрен GitHub App, когато вашата организация изисква идентичност на App или когато генерираният PR трябва да задейства downstream CI без стъпката за одобрение на `GITHUB_TOKEN`. App не заобикаля организацията политика; администраторите все още контролират инсталацията и разрешенията му.

### Стъпка 1: Създайте или инсталирайте приложение на GitHub

Използвайте наличен App, предоставен от организацията, когато има такъв, или създайте такъв с read/write достъп до **Contents** и **Pull requests**. Инсталирайте го в целевото хранилище с необходимото одобрение от организацията.

Запишете:

- App ID
- съдържанието на частния ключ

Съхранете ги като секрети на хранилището:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Стъпка 2: Генерирайте токен на приложението

Добавете тази стъпка веднага преди съществуващата стъпка за pull request. За README шаблона използвайте същото условие за успех, така че прегледите и неуспешните преводи да не изискват App токен:

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

След това променете само `token` входа на съществуващата стъпка за pull request на `${{ steps.generate_token.outputs.token }}`. Запазете нейното условие за успех, клон, тяло на PR и `add-paths` непроменени. Токенът е обвързан с текущото хранилище по подразбиране. При адаптиране на стандартната настройка вместо README шаблона, пропуснете горния `if`: този workflow използва подразбиращото се условие за успех, така че създаването на токен и създаването на PR се изпълняват само след като преводът и прегледът успеят.

Вижте официалния [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) за инсталиране и разрешения на токена.

## Ограничения за Runner

GitHub-hosted runners имат максимална продължителност на задачите. Големи хранилища или много целеви езици могат да надхвърлят този лимит.

За големи преводни натоварвания:

- Превеждайте по-малко езици на изпълнение.
- Използвайте флагове за съдържание като `-md`, `-nb` или `-img`.
- Използвайте self-hosted runner, когато размерът на хранилището или латентността на модела правят hosted runner-ите ненадеждни.

## Преглед в CI

Използвайте `co-op-review`, когато pull request трябва да валидира генерираните преводи без да извиква LLM или Vision доставчици.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` е бета детерминистична команда за преглед. Нейните проверки и схема на изхода може да се развиват, но е проектирана да е безопасна за CI, защото не записва файлове и не извиква доставчици на модели.