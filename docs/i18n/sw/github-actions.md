# GitHub Actions

Tumia GitHub Actions unapotaka hifadhi (repository) kutafsiri kiotomatiki nyaraka zilizobadilika na kufungua pull request yenye matokeo yaliyozalishwa.

Anza na usanidi wa kawaida wa `GITHUB_TOKEN`, ikiwa ni pamoja na kwa hifadhi za shirika pale sera inaporuhusu. Tazama [Usanidi wa App ya GitHub](#github-app-setup) wakati shirika lako linapohitaji utambulisho wa App au unahitaji kuendesha kwa otomatiki utekelezaji wa workflow za chini.

**Marekebisho ya binadamu:** workflows hizi zinatafsiri tena faili za chanzo zilizo badilika kikamilifu na zinaweza kuandika juu maneno yaliyohaririwa katika tafsiri zao. Kagua kila PR kabla ya kuunganisha. Uhifadhi wa block-level wa marekebisho yaliyokubaliwa wa Markdown unahitaji ujumuishaji maalum na [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## PR yako ya kwanza ya tafsiri ya README

Anza na `README.md` moja ya mizizi na lugha moja lengwa. Workflow hii inatafsiri Markdown pekee, hivyo Azure AI Vision haitahitajika.

1. Nakili [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([view the template on GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) kwenda `.github/workflows/translate-readme.yml` katika hifadhi unayotaka kutafsiri, na ufanye commit kwenye tawi la default la hifadhi hiyo. Kiolezo kinatumia Action ya mzizi `Azure/co-op-translator@main`, ambayo inasakinisha CLI kutoka ref hiyo ya chanzo. Funga commit iliyopitiwa kwa ajili ya utekelezaji unaoweza kurudiwa.
2. Fungua **Actions > Translate README > Run workflow**, chagua lugha, na uache **Preview only** ikibaki ikichaguliwa. Kagua makadirio ya tokeni katika hatua ya mapitio. Mapitio hayatawaita watoa modeli, hayataandika tafsiri, wala haitaunda PR.
3. Ongeza siri za mtoa mmoja wa [mtoa wa maandishi](#prerequisites), na washa **Ruhusu GitHub Actions kuunda na kuidhinisha maombi ya pull** chini ya **Settings > Actions > General**. Kiolezo kinahitaji `contents: write` na `pull-requests: write` kwa kazi yake; huna haja ya kubadilisha ruhusa za chaguo-msingi kwa kila workflow. Ikiwa sera ya shirika inazuia ruhusa hizi au mpangilio huu, muulize msimamizi kuhusu [App ya GitHub](#github-app-setup) iliyothibitishwa.
4. Endesha workflow tena ukiitoa alama kwenye **Preview only**. Inafanya mapitio, inatafsiri, inaendesha `co-op-review --readme-only`, na huunda au kusasisha PR ya tafsiri tu baada ya tafsiri na ukaguzi kufanikiwa. Muhtasari wa workflow una kiungo kuelekea PR.
5. Kagua uandishi na mabadiliko ya faili katika PR, kisha merge unapokuwa tayari. Workflow haitamerge kiotomatiki.

PR hiyo ina tu `translations/<language>/README.md` na faili yake ya metadata ya lugha. README chanzo inabaki isiyobadilika, na viungo kwenda nyaraka nyingine vinaendelea kuelekeza kwenye nyaraka za chanzo. Mwili wa PR unaorodhesha faili zilizobadilika na matokeo ya ukaguzi wa muundo. Ikiwa tafsiri au ukaguzi vitashindwa, angalia muhtasari wa workflow na kumbukumbu za hatua zilizoshindwa; hakuna PR itakayoundwa. Ikiwa hakuna mabadiliko, PR mpya haitahitajika.

**Kumbuka kwa Shirika na CI:** App ya GitHub ni hiari, si mahitaji ya umiliki wa shirika. Kwa `GITHUB_TOKEN`, workflows za pull-request za kufungua, kusasisha, au kufungua tena PR zinahitaji mtumiaji mwenye ruhusa za kuandika kuchagua **Approve workflows to run**. Workflows za push hazianzishwi na tokeni hii. Kwa CI ya chini isiyo na mshikiliaji, angalia [Usanidi wa App ya GitHub](#github-app-setup) na [kanuni za kuanzisha workflow](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) za GitHub.

## Prerequisites

Kabla ya kuunda workflow, sanidi siri za huduma za AI ambazo utekelezaji wako wa tafsiri unazohitaji.

Tafsiri ya maandishi inahitaji mtoa huduma mmoja wa modeli ya lugha:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Tafsiri ya picha pia inahitaji Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

See [Configuration](configuration.md) and [Azure AI Setup](azure-ai-setup.md) for local configuration details.

## Usanidi wa Kawaida

Baada ya kujaribu workflow ya README, tumia usanidi huu kutafsiri faili za Markdown za repozitori kwa lugha kadhaa. Inafanya ukaguzi wa Markdown kabla ya kufungua PR na haitahitaji Azure AI Vision.

### Hatua 1: Ongeza Siri za Hifadhi

Katika repozitori lengwa lako, fungua **Settings** > **Secrets and variables** > **Actions**, kisha ongeza siri za mtoa huduma ambazo workflow yako itatumia.

![Chagua siri za Actions](../../assets/github-actions/select-setting-action.png)

### Hatua 2: Wezesha Vibali vya Mtiririko wa Kazi

Open **Settings** > **Actions** > **General**.

Under **Workflow permissions**:

1. Washa **Ruhusu GitHub Actions kuunda na kuidhinisha maombi ya pull**.
2. Save the setting.

Kazi hapa chini inaomba `contents: write` na `pull-requests: write` waziwazi. Usiubadilishe ruhusa za chaguo-msingi za workflow za repository. Ikiwa sera ya shirika inazuia uundaji wa PR, muulize msimamizi kuhusu [App ya GitHub](#github-app-setup) iliyothibitishwa.

### Hatua ya 3: Ongeza Workflow

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

Badilisha `TARGET_LANGUAGES` kwa lugha ambazo mradi wako unazihitaji. Ukaguzi unatumia API ya Python kuchunguza Markdown pekee, ikilingana na hatua ya tafsiri. Hitilafu ya tafsiri au ukaguzi itasitisha kazi kabla ya uundaji wa PR. Workflow haiunganishi PR kiotomatiki. Kwa repositories kubwa, ongeza kigezo `paths:` chini ya `on.push` ili workflow iendeshe tu wakati nyaraka zinabadilika.

### Hiari: notebooks na picha

Kwa notebooks, ongeza `-nb` kwenye amri ya tafsiri na weka `notebook=True` katika hatua ya ukaguzi. Kwa maandishi ya picha, sanidi siri mbili za [Azure AI Vision](#prerequisites), zipitishe katika hatua ya tafsiri kwa `env`, ongeza `-img` kwenye amri, na ongeza `translated_images/` kwenye hatua ya PR `add-paths`. Kagua picha zilizotafsiriwa kwa kuona; ukaguzi wa kuamuliwa hauhakiki maandishi ya picha au usahihi wa lugha.

## Usanidi wa App ya GitHub

Tumia App ya GitHub iliyothibitishwa wakati shirika lako linahitaji utambulisho wa App, au wakati PR iliyotengenezwa inahitaji kuanzisha CI ya zifuatazo bila hatua ya idhini ya `GITHUB_TOKEN`. App haipite kando sera ya shirika; wasimamizi bado wanadhibiti usakinishaji wake na ruhusa.

### Hatua 1: Unda au Sakinisha App ya GitHub

Tumia App iliyotolewa na shirika ilipo, au unda moja yenye ruhusa za kusoma/kuandika kwa **Contents** na **Pull requests**. Sakinisha kwenye hazina lengwa kwa idhini yoyote ya shirika inayohitajika.

Record:

- App ID
- Maudhui ya private key

Store them as repository secrets:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Hatua 2: Tengeneza Tokeni ya App

Ongeza hatua hii mara moja kabla ya hatua iliyopo ya pull request. Kwa kiolezi cha README, tumia sharti la mafanikio lile lile ili mapitio ya awali na tafsiri zilizoshindwa zisizombe tokeni ya App:

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

Kisha badilisha tu ingizo la hatua iliyopo ya pull request `token` kuwa `${{ steps.generate_token.outputs.token }}`. Weka sharti lake la mafanikio, tawi, mwili wa PR, na `add-paths` visivyo badilishwa. Tokeni imepangwa kwa hazina ya sasa kwa chaguo-msingi. Wakati unapo badilisha usanidi wa kawaida badala ya kiolezi cha README, toa `if` iliyo hapo juu: workflow hiyo inatumia sharti la mafanikio la chaguo-msingi, hivyo uundaji wa tokeni na uundaji wa PR hufanyika tu baada ya tafsiri na ukaguzi kufanikiwa.

See the official [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) for installation and token permissions.

## Vizuizi vya Watekelezaji

Wakimbiaji wanaohostwa na GitHub wana muda wa juu wa kazi. Hazina kubwa au lugha nyingi lengwa zinaweza kuzidi kikomo hicho.

For large translation workloads:

- Translate fewer languages per run.
- Use content flags such as `-md`, `-nb`, or `-img`.
- Tumia runner mwenyeji mwenyewe (self-hosted) wakati ukubwa wa hazina au ucheleweshaji wa modeli unapoifanya runners waliohifadhiwa (hosted) wasiokuwa wa kuaminika.

## Mapitio katika CI

Tumia `co-op-review` wakati pull request inapaswa kuthibitisha tafsiri zilizotengenezwa bila kuita watoa huduma za LLM au Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` ni amri ya mapitio ya deterministic iliyo katika awamu ya beta. Ukaguzi wake na skema ya pato yanaweza kubadilika, lakini imeundwa kuwa salama kwa CI kwa sababu haiandiki faili wala haiwaiti watoa modeli.
