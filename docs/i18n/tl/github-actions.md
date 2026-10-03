# GitHub Actions

Gamitin ang GitHub Actions kapag nais mong awtomatikong isalin ng isang repositoryo ang mga binagong dokumento at magbukas ng pull request na may kasamang mga nalikhang output.

Magsimula sa karaniwang setup na `GITHUB_TOKEN`, pati na rin para sa mga repositoryo ng organisasyon kung pinahihintulutan ng polisiya. Tingnan ang [GitHub App Setup](#github-app-setup) kapag nangangailangan ang iyong organisasyon ng identidad ng App o kailangan mo ng awtomatikong pagpapatakbo ng downstream workflows.

**Human edits:** inuulit ng mga workflow na ito ang pagsasalin ng mga nabagong source file nang buo at maaaring mapalitan ang mga salita na inayos sa kanilang mga salin. Suriin ang bawat PR bago i-merge. Ang pagpapanatili ng antas-bloke ng Markdown para sa mga tinanggap na edit ay nangangailangan ng isang pasadyang integrasyon sa [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Ang iyong unang PR para sa pagsasalin ng README

Magsimula sa isang root `README.md` at isang target na wika. Ang workflow na ito ay nagsasalin lamang ng Markdown, kaya hindi kailangan ang Azure AI Vision.

1. Kopyahin ang [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([view the template on GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) sa `.github/workflows/translate-readme.yml` sa repositoryong nais mong isalin, at i-commit ito sa default branch ng repositoryo. Ginagamit ng template ang root Action na `Azure/co-op-translator@main`, na nag-iinstall ng CLI mula sa parehong source ref. I-pin ang isang nasuring commit para sa reproducible na mga run.
2. Buksan ang **Actions > Translate README > Run workflow**, pumili ng wika, at iwanang naka-check ang **Preview only**. Suriin ang pagtatantya ng token sa preview step. Ang preview ay hindi tumatawag ng model providers, hindi sumusulat ng mga salin, at hindi lumilikha ng PR.
3. Idagdag ang mga secrets para sa isang [tagapagbigay ng teksto](#prerequisites), at i-enable ang **Payagan ang GitHub Actions na lumikha at aprubahan ang mga pull request** sa ilalim ng **Settings > Actions > General**. Humihiling ang template ng `contents: write` at `pull-requests: write` para sa job nito; hindi mo kailangang baguhin ang default na permissions para sa bawat workflow. Kung hinaharangan ng polisiya ng organisasyon ang mga pahintulot o setting na ito, magtanong sa administrator tungkol sa isang aprubadong [GitHub App](#github-app-setup).
4. Patakbuhin muli ang workflow na may hindi naka-check ang **Preview only**. Ipe-preview nito, isasalin, pinapatakbo ang `co-op-review --readme-only`, at lilikha o mag-a-update ng translation PR lamang pagkatapos magtagumpay ang pagsasalin at review. Naglilink ang workflow summary sa PR.
5. Suriin ang mga salita at pagbabago sa mga file sa PR, pagkatapos i-merge kapag handa. Hindi awtomatikong nagme-merge ang workflow.

Naglalaman ang PR lamang ng `translations/<language>/README.md` at ang language metadata file nito. Mananatiling hindi nagbabago ang source README, at ang mga link sa ibang dokumento ay patuloy na tumuturo sa source documents. Naglilista ang body ng PR ng mga binagong file at mga resulta ng structural review. Kung nabigo ang pagsasalin o review, suriin ang workflow summary at mga log ng nabigong step; walang PR na nilikha. Kung walang pagbabago, hindi kailangan ng bagong PR.

**Organization and CI note:** Ang GitHub App ay opsyonal, hindi kinakailangan ng pag-aari ng organisasyon. Sa `GITHUB_TOKEN`, ang mga pull-request workflows para sa pagbubukas, pag-update, o muling pagbubukas ng PR ay nangangailangan ng user na may write access na pumili ng **Approve workflows to run**. Ang mga push workflows ay hindi nai-trigger ng token na ito. Para sa unattended downstream CI, tingnan ang [GitHub App Setup](#github-app-setup) at GitHub's [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Prerequisites

Bago lumikha ng workflow, i-configure ang mga secret ng AI service na kailangan ng iyong translation run.

Ang pagsasalin ng teksto ay nangangailangan ng isang tagapagbigay ng language model:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, kasama ang opsyonal na `OPENAI_ORG_ID` at `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, kasama ang opsyonal na `ANTHROPIC_BASE_URL`

Ang pagsasalin ng imahe ay karagdagan ding nangangailangan ng Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

See [Configuration](configuration.md) and [Azure AI Setup](azure-ai-setup.md) for local configuration details.

## Karaniwang Setup

Matapos subukan ang README workflow, gamitin ang setup na ito upang isalin ang mga Markdown na file ng repositoryo sa ilang mga wika. Nagsasagawa ito ng pagsusuri ng Markdown bago magbukas ng PR at hindi nangangailangan ng Azure AI Vision.

### Hakbang 1: Magdagdag ng Mga Lihim ng Repositoryo

Sa target mong repositoryo, buksan ang **Settings** > **Secrets and variables** > **Actions**, pagkatapos idagdag ang mga provider secrets na gagamitin ng iyong workflow.

![Piliin ang Actions secrets](../../assets/github-actions/select-setting-action.png)

### Hakbang 2: Paganahin ang Mga Pahintulot ng Workflow

Open **Settings** > **Actions** > **General**.

Under **Workflow permissions**:

1. Paganahin ang **Payagan ang GitHub Actions na lumikha at aprubahan ang mga pull request**.
2. I-save ang setting.

Ang job sa ibaba ay tahasang humihiling ng `contents: write` at `pull-requests: write`. Huwag baguhin ang default na workflow permissions ng repositoryo. Kung pinipigilan ng patakaran ng organisasyon ang paglikha ng PR, tanungin ang administrator tungkol sa isang aprubadong [App ng GitHub](#github-app-setup).

### Hakbang 3: Idagdag ang Workflow

Create `.github/workflows/co-op-translator.yml`:

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

Palitan ang `TARGET_LANGUAGES` ng mga wikang kailangan ng iyong proyekto. Ginagamit ng review ang Python API upang suriin lamang ang Markdown, na tumutugma sa hakbang ng pagsasalin. Hihinto ang job bago pa malikha ang PR kung may error sa pagsasalin o review. Hindi awtomatikong imi-merge ng workflow ang PR. Para sa malalaking repositoryo, magdagdag ng filter na `paths:` sa ilalim ng `on.push` upang tumakbo ang workflow lamang kapag may pagbabago sa dokumentasyon.

### Opsyonal: mga notebook at mga imahe

Para sa mga notebook, idagdag ang `-nb` sa utos ng pagsasalin at itakda ang `notebook=True` sa hakbang ng pagsusuri. Para sa teksto ng imahe, i-configure ang dalawang [mga lihim ng Azure AI Vision](#prerequisites), ipasa ang mga ito sa `env` ng hakbang ng pagsasalin, idagdag ang `-img` sa utos, at idagdag ang `translated_images/` sa hakbang ng PR na `add-paths`. Suriin ang mga isinaling imahe nang biswal; hindi ginagarantiya ng deterministic review ang kawastuhan ng teksto sa imahe o ng linggwistikong katumpakan.

## Pag-set up ng GitHub App

Gumamit ng aprubadong GitHub App kapag nangangailangan ang iyong organisasyon ng pagkakakilanlan ng App, o kapag kailangan ng nabuo na PR na mag-trigger ng downstream CI nang walang hakbang ng pag-apruba na `GITHUB_TOKEN`. Ang isang App ay hindi nilalampasan ang patakaran ng organisasyon; kontrolado pa rin ng mga administrador ang pag-install at mga pahintulot nito.

### Hakbang 1: Lumikha o Mag-install ng GitHub App

Gumamit ng umiiral na App na ibinigay ng organisasyon kapag magagamit, o lumikha ng isa na may read/write na access sa **Nilalaman** at **Mga Pull request**. I-install ito sa target repository na may anumang kinakailangang pag-apruba ng organisasyon.

Record:

- App ID
- Nilalaman ng private key

Store them as repository secrets:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Hakbang 2: Bumuo ng App Token

Idagdag ang hakbang na ito kaagad bago ang umiiral na hakbang ng pull request. Para sa README template, gamitin ang parehong kondisyon ng tagumpay upang ang mga preview at nabigong pagsasalin ay hindi humiling ng App token:

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

Pagkatapos, palitan lamang ang input na `token` ng umiiral na hakbang ng pull request ng `${{ steps.generate_token.outputs.token }}`. Panatilihin ang kondisyon ng tagumpay, branch, katawan ng PR, at `add-paths` na hindi nababago. Ang token ay sakop sa kasalukuyang repository bilang default. Kapag inaangkop ang karaniwang setup sa halip na ang README template, huwag isama ang `if` sa itaas: ang workflow na iyon ay gumagamit ng default na kondisyon ng tagumpay, kaya ang paglikha ng token at paglikha ng PR ay tatakbo lamang pagkatapos magtagumpay ang pagsasalin at pagsusuri.

See the official [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) for installation and token permissions.

## Mga Limitasyon ng Runner

May takdang maximum na tagal ng trabaho ang mga GitHub-hosted runner. Maaaring lumampas sa limitasyong iyon ang malalaking repositoryo o maraming target na wika.

For large translation workloads:

- Isalin ang mas kaunting mga wika kada run.
- Gumamit ng content flags tulad ng `-md`, `-nb`, o `-img`.
- Gumamit ng self-hosted runner kapag ang laki ng repositoryo o latency ng model ay ginagawang hindi maaasahan ang hosted runners.

## Pagsusuri sa CI

Gamitin ang `co-op-review` kapag ang isang pull request ay dapat i-validate ang mga nabuo na pagsasalin nang hindi tumatawag ng mga provider ng LLM o Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` ay isang beta na deterministikong utos sa pagsusuri. Maaaring magbago ang mga pagsusuri at ang schema ng output nito, ngunit idinisenyo ito upang maging ligtas para sa CI dahil hindi ito sumusulat ng mga file o tumatawag ng mga provider ng modelo.
