# GitHub Actions

Користите GitHub Actions када желите да репозиторијум аутоматски преведе изменjену документацију и отвори pull request са генерисаним резултатима.

Почните са стандардним подешавањем `GITHUB_TOKEN`, укључујући и за репозиторијуме организације где политика то дозвољава. Погледајте [Постављање GitHub апликације](#github-app-setup) када ваша организација захтева идентитет апликације или вам треба аутоматско покретање downstream workflow-а.

**Ручне измене:** ови workflows поново у потпуности преводе изменјене изворне фајлове и могу преписати формулације које сте изменили у преводима. Прегледајте сваки PR пре сливања. Задржавање блок-структуре Markdown-а за прихваћене измене захтева прилагођену интеграцију са [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Ваш први PR за превод README

Почните са једним коренским `README.md` и једним циљним језиком. Овај workflow преводи само Markdown, тако да Azure AI Vision није потребан.

1. Копирајте [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([погледајте шаблон на GitHub-у](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) у `.github/workflows/translate-readme.yml` у репозиторијуму који желите да преведете и комитујте га у подразумевану грану тог репозиторијума. Шаблон користи root Action у `Azure/co-op-translator@main`, који инсталира CLI из истог source ref-а. За репродуцибилна покретања означите (pin) прегледани commit.
2. Отворите **Actions > Translate README > Run workflow**, изаберите језик и оставите **Preview only** означеним. Прегледајте процену потребних токена у кораку прегледа. Preview не позива провајдере модела, не уписује преводе и не креира PR.
3. Додајте тајне за једног [провајдера текста](#prerequisites), и омогућите **Дозволите GitHub Actions да креирају и одобравају pull захтеве** под **Подешавања > Actions > General**. Шаблон захтева `contents: write` и `pull-requests: write` за свој job; не морате мењати подразумеване дозволе за сваки workflow. Ако политика организације блокира ове дозволе или ово подешавање, обратите се администратору у вези одобрене [GitHub апликације](#github-app-setup).
4. Покрените workflow поново са уклоњеним означавањем **Preview only**. Он прави преглед, преводи, покреће `co-op-review --readme-only` и креира или ажурира PR за превод само након што превод и преглед успешно прођу. Сажетак workflow-а садржи линк до PR-а.
5. Прегледајте формулације и измене фајлова у PR-у, а затим слиједините када будете спремни. Workflow не обавља аутоматско сливање.

PR садржи само `translations/<language>/README.md` и његов фајл са метаподацима о језику. Изворни README остаје непромењен, а линкови ка другим документима и даље показу на изворне документе. Тело PR-а наводи измењене фајлове и резултате структурног прегледа. Ако превођење или преглед не успе, проверите сажетак workflow-а и логове неуспелих корака; PR неће бити креиран. Ако нема измена, нови PR није потребан.

**Напомена за организацију и CI:** GitHub апликација је опционална и није захтев власништва организације. Са `GITHUB_TOKEN`, workflows који се односе на pull request-ове за отварање, ажурирање или поновно отварање PR-а захтевају корисника са write приступом да изабере **Approve workflows to run**. Push workflows се не покрећу овим токеном. За ненадгледани downstream CI, погледајте [Постављање GitHub апликације](#github-app-setup) и GitHub-ова правила о [покретању workflow-ова](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Захтеви

Пре креирања workflow-а, конфигуришите тајне AI сервиса које ваш покретач превођења захтева.

Текстуални превод захтева једног провајдера језичког модела:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Превођење слика додатно захтева Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Погледајте [Конфигурација](configuration.md) и [Постављање Azure AI](azure-ai-setup.md) за детаље локалне конфигурације.

## Стандардно подешавање

Након испробавања README workflow-а, користите ово подешавање да преведете Markdown фајлове репозиторијума на више језика. Покреће Markdown преглед пре отварања PR-а и не захтева Azure AI Vision.

### Корак 1: Додајте тајне репозиторијума

У циљном репозиторијуму отворите **Settings** > **Secrets and variables** > **Actions**, па додајте провајдерске тајне које ће ваш workflow користити.

![Изаберите тајне за Actions](../../assets/github-actions/select-setting-action.png)

### Корак 2: Омогућите дозволе за workflow

Отворите **Settings** > **Actions** > **General**.

Под **Workflow permissions**:

1. Омогућите **Дозволите GitHub Actions да креирају и одобравају pull захтеве**.
2. Сачувајте подешавање.

Испод job-а је експлицитно затражено `contents: write` и `pull-requests: write`. Оставите подразумеване дозволе workflow-а непромењене. Ако политика организације блокира креирање PR-ова, обратите се администратору у вези одобренe [GitHub апликације](#github-app-setup).

### Корак 3: Додајте workflow

Креирајте `.github/workflows/co-op-translator.yml`:

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

Промените `TARGET_LANGUAGES` у језике које ваш пројекат захтева. Преглед користи Python API да провери само Markdown, у складу са кораком превођења. Грешка у превођењу или прегледу зауставља job пре креирања PR-а. Workflow не слива PR аутоматски. За велике репозиторијуме додајте `paths:` филтер под `on.push` тако да workflow ради само када се документација промени.

### Опционо: notebook-и и слике

За notebook-е додајте `-nb` команди за превођење и подесите `notebook=True` у кораку прегледа. За текст на сликама конфигуришите две [Azure AI Vision тајне](#prerequisites), проследите их у `env` корака за превођење, додајте `-img` команди и у кораку за PR додајте `translated_images/` у `add-paths`. Преглед преведених слика обавите визуелно; детерминистички преглед не гарантује тачност текста на слици нити лингвистичку исправност.

## Постављање GitHub апликације

Користите одобрену GitHub апликацију када ваша организација захтева идентитет апликације, или када генерисани PR треба да покрене downstream CI без корака одобрења `GITHUB_TOKEN`-ом. Апликација не поништава политику организације; администратори и даље контролишу њену инсталацију и дозволе.

### Корак 1: Креирајте или инсталирајте GitHub апликацију

Користите постојећу апликацију коју пружа организација када је доступна, или креирајте нову са read/write приступом за **Contents** и **Pull requests**. Инсталирајте је на циљни репозиторијум уз потребно одобрење организације.

Запишите:

- ID апликације
- Садржај приватног кључа

Сачувајте их као репозиторијумске тајне:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Корак 2: Генеришите токен апликације

Додајте овај корак одмах пре постојећег корака за pull request. За README шаблон, користите исти услов успеха тако да прегледи и неуспели преводи не захтевају App токен:

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

Затим измените само `token` улазе постојећег корака за pull request на `${{ steps.generate_token.outputs.token }}`. Задржите његов услов успеха, грану, тело PR-а и `add-paths` непромењеним. Токен је по подразумеваној вредности ограничен на текући репозиторијум. Када прилагођавате стандардно подешавање уместо README шаблона, изоставите `if` изнад: тај workflow користи подразумевани услов успеха, па креирање токена и креирање PR-а се извршавају само након што превод и преглед успешно прођу.

Погледајте званичну [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) за инсталацију и дозволе токена.

## Ограничења рунера

GitHub-hosted runner-и имају максимално трајање job-а. Велики репозиторијуми или велики број циљних језика могу прећи то ограничење.

За велика оптерећења превођења:

- Преведите мање језика по покретању.
- Користите content флагове као што су `-md`, `-nb`, или `-img`.
- Користите self-hosted runner када величина репозиторијума или латенција модела чине hosted рунере непоузданим.

## Преглед у CI

Користите `co-op-review` када pull request треба да валидира генерисане преводе без позива LLM или Vision провајдера.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` је бета детерминистички прегледни командни алат. Његове провере и шема излаза могу еволуирати, али је дизајниран да буде сигуран за CI јер не уписује фајлове нити позива провајдере модела.