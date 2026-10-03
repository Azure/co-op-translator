# GitHub Actions

మీరు ఒక రిపోజిటరీని మారిన డాక్యుమెంటేషన్‌ను స్వయంచాలకంగా అనువదించి ఉత్పన్నించిన ఫలితాలతో ఒక పుల్ రిక్వెస్ట్ తెరవించాలనుకున్నప్పుడు GitHub Actions వాడండి.

ప్రామాణిక `GITHUB_TOKEN` సెటప్‌తో మొదలుపెట్టు, పాలసీ అనుమతించే సంస్థా రిపోజిటరీలు కూడా సహా. మీ సంస్థకు ఒక App గుర్తింపు అవసరమైతే లేదా ఆటోమేటిక్ డౌన్‌స్ట్రీమ్ వర్క్‌ఫ్లోలు అవసరమైతే [GitHub App Setup](#github-app-setup) చూడండి.

**Human edits:** ఈ వర్క్‌ఫ్లోలు మారిన సోర్స్ ఫైళ్లను పూర్తిగా మళ్లీ అనువదిస్తాయి మరియు వాటి అనువాదాల్లో మానవులు సవరించిన పదచయాలను మార్చవచ్చు. విలీనం చేయకముందు ప్రతి PRని సమీక్షించండి. ఆమోదించబడిన సవరణల యొక్క Markdown బ్లాక్-లెవల్ సంరక్షణకు ఒక కస్టమ్ ఇంటిగ్రేషన్ అవసరం, దీనికి [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) ఉపయోగించాలి.

## మీ మొదటి README అనువాద PR

ఒక రూట్ `README.md` మరియు ఒక లక్ష్య భాషతో ప్రారంభించండి. ఈ వర్క్‌‌ఫ్లో కేవలం Markdownనే అనువదిస్తుంది, అందుచేత Azure AI Vision అవసరం లేదు.

1. అనువదించదలిచిన రిపోజిటరీలో [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([view the template on GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) ను `.github/workflows/translate-readme.yml` గా కాపీ చేసి ఆ రిపోజిటరీ యొక్క డిఫాల్ట్ బ్రాంచ్‌కి కమిట్ చేయండి. టెంప్లెట్ రూట్ Action ను `Azure/co-op-translator@main` లో ఉపయోగిస్తుంది, ఇది CLIని అదే సోర్స్ రిఫ్ నుండి ఇన్‌స్టాల్ చేస్తుంది. పునరుత్పత్తికరమైన రన్‌ల కోసం సమీక్షించిన కమిట్‌ను పిన్ చేయండి.
2. **Actions > Translate README > Run workflow** తెరవచి ఒక భాషను ఎంచుకోండి, మరియు **Preview only** ఎంపిక చేక్కై ఉండాలని వదలండి. ప్రివ్యూ దశలో టోకెన్ అంచనాను సమీక్షించండి. ప్రివ్యూ మోడల్ ప్రొవైడర్లను పిలవదు, అనువాదాలను లిఖించదు, లేదా PRను సృష్టించదు.
3. ఒక [టెక్స్ట్ ప్రొవైడర్](#prerequisites) కోసం గుప్తచిరునామాలను జోడించండి, మరియు **సెట్టింగ్స్ > ఆక్షన్స్ > జనరల్** లో **GitHub Actionsకి పుల్ రిక్వెస్టులను సృష్టించడానికి మరియు అనుమోదించడానికి అనుమతించండి** ను ఎనేబుల్ చేయండి. టెంప్లెట్ తన జాబ్ కోసం `contents: write` మరియు `pull-requests: write`ని అభ్యర్థిస్తుంది; ప్రతి వర్క్‌‌ఫ్లో కోసం డిఫాల్ట్ అనుమతులను మార్చాల్సిన అవసరం లేదు. సంస్థా పాలసీ ఈ అనుమతులను లేదా సెట్టింగ్‌ను నిరోధిస్తే, ఆమోదించిన [GitHub App](#github-app-setup) గురించి అడగండి.
4. **Preview only** అన్‌చెక్ చేసి వర్క్‌‌ఫ్లోని మళ్లీ నడపండి. ఇది ప్రివ్యూ చేస్తుంది, అనువదిస్తుంది, `co-op-review --readme-only` ను నడిపిస్తుంది, మరియు అనువాదం మరియు సమీక్ష విజయవంతమైతే మాత్రమే అనువాద PRని సృష్టిస్తుంది లేదా అప్డేట్ చేస్తుంది. వర్క్‌‌ఫ్లో సారాంశం PRకి లింక్ ఇవ్వును.
5. PRలో పదచయం మరియు ఫైల్ మార్పులను సమీక్షించి, సిద్ధమైతే మర్జ్ చేయండి. వర్క్‌‌ఫ్లో స్వయంచాలకంగా మర్జ్ చేయదు.

PRలో కేవలం `translations/<language>/README.md` మరియు దాని భాషా మెటాడేటా ఫైల్ మాత్రమే ఉంటాయి. మూల README మారవు, మరియు ఇతర డాక్యుమెంట్లకు ఉన్న లింకులు మూల డాక్యుమెంట్లనే సూచిస్తూనే ఉంటాయి. PR బాడీ మార్చబడిన ఫైళ్లను మరియు నిర్మాణాత్మక సమీక్ష ఫలితాలను జాబితా చేస్తుంది. అనువాదం లేదా సమీక్ష విఫలమైతే, వర్క్‌‌ఫ్లో సారాంశం మరియు విఫలమైన దశల లాగ్స్‌ను పరిశీలించండి; PR సృష్టించబడదు. మార్పులు లేనప్పుడు కొత్త PR అవసరం లేదు.

**Organization and CI note:** ఒక GitHub App ఐచ్ఛికమే, అది సంస్థా యజమాన్యానికి అవసరమవదు. `GITHUB_TOKEN` తో, PRను ఓపెన్ చేయడం, అప్డేట్ చేయడం లేదా మళ్లీ ఓపెన్ చేయడానికి సంబంధించిన pull-request వర్క్‌‌ఫ్లోలకు **Approve workflows to run** ఎంపికను సెట్ చేయడానికి రైటు యాక్సెస్ కలిగిన యూజర్ అవసరం. పుష్ వర్క్‌‌ఫ్లోలు ఈ టోకెన్‌తో ట్రిగ్గర్ కావవు. నిరవధిక డౌన్‌స్ట్రీమ్ CI కోసం, [GitHub App Setup](#github-app-setup) మరియు GitHub యొక్క [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) చూడండి.

## ముందస్తు అవసరాలు

వర్క్‌‌ఫ్లో సృష్టించేముందు, మీ అనువాద రన్‌కి అవసరమైన AI సేవ గుప్తచిరునామాలను కాన్ఫిగర్ చేసుకోండి.

టెక్స్ట్ అనువాదానికి ఒక భాషా మోడల్ ప్రొవైడర్ అవసరం:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

ఇమేజ్ అనువాదానికి అదనంగా Azure AI Vision అవసరం:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

స్థానిక కాన్ఫిగరేషన్ వివరాల కోసం [Configuration](configuration.md) మరియు [Azure AI Setup](azure-ai-setup.md) చూడండి.

## ప్రమాణిక సెటప్

README వర్క్‌‌ఫ్లోను ప్రయత్నించిన తర్వాత, ఈ సెటప్‌ను ఉపయోగించి ఒక రిపోజిటరీ యొక్క Markdown ఫైళ్లను అనేక భాషల్లో అనువదించండి. ఇది PR తెరవడానికి ముందు Markdown సమీక్షను నడపుతుంది మరియు Azure AI Vision అవసరం కాదు.

### దశ 1: రిపోజిటరీ గుప్తచిరునామాలను జోడించండి

మీ లక్ష్య రిపోజిటరీలో **Settings** > **Secrets and variables** > **Actions** ఓపెన్ చేసి, మీ వర్క్‌‌ఫ్లో ఉపయోగించగల ప్రొవైడర్ గుప్తచిరునామాలను జోడించండి.

![Actions రహస్యాలను ఎంచుకోండి](../../assets/github-actions/select-setting-action.png)

### దశ 2: వర్క్‌‌ఫ్లో అనుమతులను ఎనేబుల్ చేయండి

**Settings** > **Actions** > **General** ఓపెన్ చేయండి.

**Workflow permissions** కింద:

1. **GitHub Actionsకి పుల్ రిక్వెస్టులను సృష్టించడానికి మరియు అనుమోదించడానికి అనుమతించండి** ను ఎనేబుల్ చేయండి.
2. సెట్టింగను సేవ్ చేయండి.

క్రింది జాబ్ స్పష్టంగా `contents: write` మరియు `pull-requests: write`ని అభ్యర్థిస్తుంది. రిపోజిటరీ యొక్క డిఫాల్ట్ వర్క్‌‌ఫ్లో అనుమతులను మార్చకుండా ఉంచండి. సంస్థా పాలసీ PR సృష్టింపుని నిరోధిస్తే, ఆమోదించిన [GitHub App](#github-app-setup) గురించి అడగండి.

### దశ 3: వర్క్‌‌ఫ్లో జోడించండి

`.github/workflows/co-op-translator.yml` సృష్టించండి:

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

మీ ప్రాజెక్ట్‌కు అవసరమైన భాషలకు `TARGET_LANGUAGES`ని మార్చండి. సమీక్ష అనువాద దశ‌కు సరిపోయేలా కేవలం Markdown ని తనిఖీ చేయడానికి Python API ను ఉపయోగిస్తుంది. అనువాద లేదా సమీక్షలో లోపం వస్తే అది PR సృష్టించకముందే జాబ్ ను ఆపేస్తుంది. వర్క్‌‌ఫ్లో PR ని స్వయంచాలకంగా మర్జ్ చేయదు. పెద్ద రిపోజిటరీలకు, డాక్యుమెంటేషన్ మారినప్పుడే వర్క్‌‌ఫ్లో మాత్రమే నడవడానికి `on.push` కింద `paths:` ఫిల్టర్ జోడించండి.

### ఐచ్ఛికం: నోటుబుక్స్ మరియు చిత్రాలు

నోటుబుక్స్ కోసం, అనువాద కమాండ్‌కు `-nb` జోడించి సమీక్ష దశలో `notebook=True` సెెట్ చేయండి. చిత్రం టెక్స్ట్ కోసం, రెండు [Azure AI Vision secrets](#prerequisites) ను కాన్ఫిగర్ చేసి, వాటిని అనువాద దశ యొక్క `env` లో పాస్ చేయండి, కమాండ్‌కు `-img` జోడించి, PR దశలో `add-paths` కు `translated_images/` ను జోడించండి. అనువదించిన చిత్రాలను بصు గమనించి సమీక్షించండి; డిటర్మినిస్టిక్ సమీక్ష చిత్రం టెక్స్ట్ లేదా భాషా ఖచ్చితత్వాన్ని ధృవీకరించదు.

## GitHub App సెటప్

మీ సంస్థకు App గుర్తింపు అవసరమైతే లేదా ఉత్పన్నమైన PRకి `GITHUB_TOKEN` ఆమోద దశ లేకుండా డౌన్‌స్ట్రీమ్ CI ని ట్రिग్గర్ చేయాల్సిన అవసరం ఉంటే ఆమోదించిన GitHub App ఉపయోగించండి. App సంస్థా పాలసీని బైపాస్ చేయదు; ఇన్‌స్టాలేషన్ మరియు అనుమతులను అడ్మినిస్ట్రేటర్లు ఇంకా నియంత్రిస్తారు.

### దశ 1: GitHub App సృష్టించండి లేదా ఇన్‌స్టాల్ చేయండి

అందుబాటులో ఉంటే ఇప్పటికే సంస్థ పంపిణీ చేసిన App ను ఉపయోగించండి, లేదా **Contents** మరియు **Pull requests** కు చదవ/రాయడం అనుమతులు ఇచ్చేలా ఒక App సృష్టించండి. అవసరమైన సంస్థ ఆమోదంతో దానిని లక్ష్య రిపోజిటరీపై ఇన్‌స్టాల్ చేయండి.

నమోదు చేయండి:

- App ID
- Private key contents

వాటిని రిపోజిటరీ గుప్తచిరునామాలుగా భద్రపరచండి:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### దశ 2: App టోకెన్ ఉత్పత్తి చేయండి

ఈ దశను ప్రస్తుత pull request దశకి తక్షణమే ముందు జోడించండి. README టెంప్లెట్ కోసం, ప్రివ్యూలు మరియు విఫలమైన అనువాదాలు App టోకెన్‌ను కోరకుండా అదే విజయం శరతును ఉపయోగించండి:

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

తరువాత మాత్రమే ప్రస్తుత pull request దశలోని `token` ఇన్పुट్‌ను `${{ steps.generate_token.outputs.token }}` గా మార్చండి. దాని సక్సెస్ షరతు, బ్రాంచ్, PR బాడీ, మరియు `add-paths` అపరివర్తనీయంగా ఉంచండి. టోకెన్ డిఫాల్ట్‌గా ప్రస్తుత రిపోజిటరీకు స్కోప్ చేయబడుతుంది. README టెంప్లెట్‌కి బదులుగా స్టాండర్డ్ సెటప్‌ను అనుకూలీకరించేటప్పుడు, పై `if` ని తీసివేయండి: ఆ వర్క్‌‌ఫ్లో డిఫాల్ట్ సక్సెస్ షరతును ఉపయోగిస్తుంది, కాబట్టి టోకెన్ సృష్టి మరియు PR సృష్టి అనువాదం మరియు సమీక్ష విజయవంతమైన తర్వాతే నడుస్తాయి.

ఇన్‌స్టాలేషన్ మరియు టోకెన్ అనుమతుల కోసం అధికారిక [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) చూడండి.

## రన్నర్ పరిమితులు

GitHub-హోస్టెడ్ రన్నర్లకు గరిష్ట జాబ్ వ్యవధి ఉంటుంది. పెద్ద రిపోజిటరీలు లేదా అనేక లక్ష్య భాషలు ఆ పరిమితిని మించి పోవచ్చు.

పెద్ద అనువాద పనిభారాల కోసం:

- ఒక రన్‌కు తక్కువ భాషలను అనువదించండి.
- పదార్థ ఫ్లాగ్‌లు (`-md`, `-nb`, లేదా `-img`) ఉపయోగించండి.
- రిపోజిటరీ పరిమాణం లేదా మోడల్ లేటెన్సీ హోస్టెడ్ రన్నర్లను నమ్మకంగా ఉండనివ్వనట్లైతే self-hosted రన్నర్ ఉపయోగించండి.

## CIలో సమీక్ష

LLM లేదా Vision ప్రొవైడర్లను పిలవకుండా ఉత్పన్నించిన అనువాదాలను పుల్ రిక్వెస్ట్ ద్వారా ధృవీకరించాలనుకునే సందర్భాల్లో `co-op-review` ఉపయోగించండి.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` ఒక బీటా డిటర్మినిస్టిక్ సమీక్ష ఆదేశం. దాని తనిఖీలు మరియు అవుట్‌పుట్ స్కీమా అభివృద్ధి చెందవచ్చు, కానీ ఇది ఫైళ్లను రాయదు లేదా మోడల్ ప్రొవైడర్లను పిలవదు కనుక CI కోసం భద్రంగా ఉండేలా డిజైన్ చేయబడింది.