# GitHub Actions

परिवर्तित डक्युमेन्टेशनलाई स्वचालित रूपमा अनुवाद गर्न र उत्पन्न आउटपुटहरूसँग एउटा पुल अनुरोध खोल्न चाहनुहुन्छ भने GitHub Actions प्रयोग गर्नुहोस्।

मानक `GITHUB_TOKEN` सेटअपबाट सुरु गर्नुहोस्, संगठन रिपोजिटरीहरूमा जहाँ नीति अनुमति दिन्छ त्यसमा पनि। जब तपाईंको संगठनले App पहिचान आवश्यक पर्छ वा तपाईंलाई स्वत: डाउनस्ट्रीम वर्कफ्लो चलाउन आवश्यक छ तब हेर्नुहोस् [GitHub App Setup](#github-app-setup)।

**Human edits:** यी वर्कफ्लोहरूले परिवर्तन भएका स्रोत फाइलहरू पूर्ण रूपमा पुन:अनुवाद गर्दछन् र तिनीहरूको अनुवादहरूमा सम्पादन गरिएको शब्दावलीलाई ओभरराइट गर्न सक्छन्। मर्ज गर्नु अघि प्रत्येक PR समीक्षा गर्नुहोस्। स्वीकार गरिएका सम्पादनहरूको Markdown ब्लक-स्तर संरक्षणको लागि कस्टम एकीकरण आवश्यक पर्छ, [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) सँग।

## तपाईंको पहिलो README अनुवाद PR

एक मूल `README.md` र एउटा लक्षित भाषा बाट सुरु गर्नुहोस्। यस वर्कफ्लोले केवल Markdown अनुवाद गर्दछ, त्यसैले Azure AI Vision आवश्यक पर्दैन।

1. आफ्नो अनुवाद गर्न चाहनु भएको रिपोजिटरीमा [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([GitHub मा टेम्पलेट हेर्नुहोस्](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) लाई `.github/workflows/translate-readme.yml` मा प्रतिलिपि गर्नुहोस्, र त्यस रिपोजिटरीको डिफल्ट ब्रान्चमा कमिट गर्नुहोस्। टेम्पलेटले `Azure/co-op-translator@main` मा रुट Action प्रयोग गर्छ, जसले CLI सोही सोर्स रिफबाट इन्स्टल गर्छ। पुनरुत्पादनयोग्य रनका लागि समीक्षा गरिएको कमिट पिन गर्नुहोस्।
2. **Actions > Translate README > Run workflow** खोल्नुहोस्, भाषा छान्नुहोस्, र **Preview only** जाँचिएको अवस्थामा छोड्नुहोस्। प्रिभ्यू चरणमा टोकन अनुमान समीक्षा गर्नुहोस्। प्रिभ्यूले मोडल प्रदायकहरूलाई कल गर्दैन, अनुवाद लेख्दैन, वा PR सिर्जना गर्दैन।
3. एक [टेक्स्ट प्रदायक](#prerequisites) का लागि सीक्रेटहरू थप्नुहोस्, र **Settings > Actions > General** अन्तर्गत **GitHub Actions लाई pull requests सिर्जना र अनुमोदन गर्न अनुमति दिनुहोस्** सक्षम गर्नुहोस्। टेम्पलेटले आफ्नो कामका लागि `contents: write` र `pull-requests: write` अनुरोध गर्छ; प्रत्येक वर्कफ्लोका लागि पूर्वनिर्धारित अनुमति परिवर्तन गर्नु आवश्यक छैन। यदि संगठनको नीति यी अनुमतिहरू वा उक्त सेटिङलाई अवरुद्ध गर्छ भने, अनुमोदित [GitHub App](#github-app-setup) सम्बन्धी प्रशासकसँग सोध्नुहोस्।
4. **Preview only** अनचेक गरेर workflow फेरि चलाउनुहोस्। यसले प्रिभ्यू गर्छ, अनुवाद गर्छ, `co-op-review --readme-only` चलाउँछ, र केवल अनुवाद र समीक्षा सफल भएपछि मात्र अनुवाद PR सिर्जना वा अपडेट गर्छ। workflow सारांशले PR लाई लिंक गर्छ।
5. PR मा शब्द चयन र फाइल परिवर्तनहरू समीक्षा गर्नुहोस्, र तयार भएपछि मर्ज गर्नुहोस्। workflow स्वतः मर्ज गर्दैन।

PR मा केवल `translations/<language>/README.md` र यसको भाषा मेटाडाटा फाइल मात्र समावेश हुन्छ। स्रोत README अपरिवर्तित रहन्छ, र अन्य कागजातहरूका लिंकहरू स्रोत कागजातहरूलाई नै संकेत गरिरहन्छन्। PR बडीले परिवर्तन भएका फाइलहरू र संरचनात्मक समीक्षा परिणामहरू सूचीकृत गर्छ। यदि अनुवाद वा समीक्षा असफल भयो भने, वर्कफ्लो समरी र असफल चरणका लगहरू जाँच्नुहोस्; कुनै PR सिर्जना हुँदैन। यदि कुनै परिवर्तन छैन भने, नयाँ PR आवश्यक छैन।

**Organization and CI note:** GitHub App वैकल्पिक छ, संगठन स्वामित्वको आवश्यक्ता होइन। `GITHUB_TOKEN` सँग, PR खोल्ने, अपडेट गर्ने, वा पुन:खोल्ने पुल-रेक्वेस्ट वर्कफ्लोहरूका लागि एउटा लेखन अनुमति भएको प्रयोगकर्ताले **Approve workflows to run** चयन गर्न आवश्यक पर्छ। Push वर्कफ्लोहरू यस टोकनले ट्रिगर गर्दैनन्। अव्यवस्थित डाउनस्ट्रीम CI का लागि, [GitHub App Setup](#github-app-setup) र GitHub का [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) हेर्नुहोस्।

## पूर्व-आवश्यकताहरू

वर्कफ्लो सिर्जना गर्नु अघि, तपाईंको अनुवाद रनले आवश्यक पर्ने AI सेवा secrets कन्फिगर गर्नुहोस्।

टेक्स्ट अनुवादका लागि एउटा भाषा मोडेल प्रदायक आवश्यक छ:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, साथै वैकल्पिक `OPENAI_ORG_ID` र `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, साथै वैकल्पिक `ANTHROPIC_BASE_URL`

छवि अनुवादका लागि थप रूपमा Azure AI Vision आवश्यक छ:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

स्थानीय कन्फिगरेसन विवरणहरूको लागि [Configuration](configuration.md) र [Azure AI Setup](azure-ai-setup.md) हेर्नुहोस्।

## मानक सेटअप

README वर्कफ्लो प्रयोग गरेपछि, भण्डारका Markdown फाइलहरूलाई विभिन्न भाषाहरूमा अनुवाद गर्न यो सेटअप प्रयोग गर्नुहोस्। यसले PR खोल्नुअघि Markdown समीक्षा चलाउँछ र Azure AI Vision आवश्यक पर्दैन।

### चरण 1: रिपोजिटरी सिक्रेटहरू थप्नुहोस्

तपाईंको लक्ष्य भण्डारमा, **Settings > Secrets and variables > Actions** खोल्नुहोस्, त्यसपछि तपाईंको वर्कफ्लोले प्रयोग गर्ने प्रदायक सिक्रेटहरू थप्नुहोस्।

![Actions का सिक्रेटहरू चयन गर्नुहोस्](../../assets/github-actions/select-setting-action.png)

### चरण 2: वर्कफ्लो अनुमति सक्षम गर्नुहोस्

खोल्नुहोस् **Settings > Actions > General**।

**Workflow permissions** अन्तर्गत:

1. सक्षम गर्नुहोस् **GitHub Actions लाई पुल अनुरोधहरू सिर्जना र अनुमोदन गर्न अनुमति दिनुहोस्**।
2. सेभ गर्नुहोस्।

तलको जॉबले स्पष्ट रूपमा `contents: write` र `pull-requests: write` अनुरोध गर्दछ। रिपोजिटरीको डिफल्ट वर्कफ्लो अनुमति अपरिवर्तित राख्नुहोस्। यदि संगठन नीतिले PR सिर्जना अवरुद्ध गर्छ भने, अनुमोदित [GitHub App](#github-app-setup) को बारेमा प्रशासकलाई सोध्नुहोस्।

### चरण 3: वर्कफ्लो थप्नुहोस्

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

`TARGET_LANGUAGES` लाई तपाईंको परियोजनाले चाहिने भाषाहरूमा परिवर्तन गर्नुहोस्। समीक्षा केवल Markdown जाँच गर्न Python API प्रयोग गर्दछ, जसले अनुवाद चरणसँग मेल खान्छ। अनुवाद वा समीक्षा त्रुटिले PR सिर्जनाअघि नै जॉब रोक्छ। वर्कफ्लोले PR स्वचालित रूपमा मर्ज गर्दैन। ठूलो रिपोजिटरीहरूको लागि, `on.push` अन्तर्गत `paths:` फिल्टर थप्नुहोस् ताकि वर्कफ्लो केवल दस्तावेज़ परिवर्तन हुँदा मात्र चलोस्।

### वैकल्पिक: नोटबुकहरू र छविहरू

नोटबुकहरूको लागि, अनुवाद कमाण्डमा `-nb` थप्नुहोस् र समीक्षा चरणमा `notebook=True` सेट गर्नुहोस्। छवि टेक्स्टका लागि, दुईवटा [Azure AI Vision secrets](#prerequisites) कन्फिगर गर्नुहोस्, तिनीहरूलाई अनुवाद चरणको `env` मा पास गर्नुहोस्, कमाण्डमा `-img` थप्नुहोस्, र PR चरणको `add-paths` मा `translated_images/` थप्नुहोस्। अनूदित छविहरूलाई दृश्य रूपमा समीक्षा गर्नुहोस्; निश्चित समीक्षा (deterministic review)ले छवि टेक्स्ट वा भाषागत शुद्धताको प्रमाणिकरण गर्दैन।

## GitHub App सेटअप

जब तपाईंको संगठनले App पहिचान आवश्यक पार्छ, वा उत्पन्न PR ले `GITHUB_TOKEN` को अनुमोदन चरण बिना डाउनस्ट्रीम CI ट्रिगर गर्नुपर्ने हुन्छ तब अनुमोदित GitHub App प्रयोग गर्नुहोस्। App ले संगठन नीतिलाई बाइपास गर्दैन; प्रशासकहरूले यसको इन्स्टलेशन र अनुमतिहरू नियन्त्रण गर्दछन्।

### चरण 1: GitHub App सिर्जना वा इन्स्टल गर्नुहोस्

उपलब्ध भएमा अवस्थित संगठन-प्रदत्त App प्रयोग गर्नुहोस्, वा **Contents** र **Pull requests** मा read/write पहुँच सहित एउटा सिर्जना गर्नुहोस्। आवश्यक संगठन अनुमोदनका साथ यसलाई लक्ष्य भण्डारमा इन्स्टल गर्नुहोस्।

Record:

- App ID
- Private key सामग्री

Store them as repository secrets:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### चरण 2: App टोकन उत्पन्न गर्नुहोस्

यस चरणलाई वर्तमानका पुल अनुरोध चरणको ठीक अघि थप्नुहोस्। README टेम्पलेटको लागि, पूर्वावलोकन र असफल अनुवादहरूले App टोकन अनुरोध नगरोस् भनी उही सफलता सर्त प्रयोग गर्नुहोस्:

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

त्यसपछि मात्र वर्तमान पुल अनुरोध चरणको `token` इनपुटलाई `${{ steps.generate_token.outputs.token }}` मा परिवर्तन गर्नुहोस्। यसको सफलता सर्त, branch, PR body, र `add-paths` अपरिवर्तित राख्नुहोस्। टोकन सामान्यतया वर्तमान रिपोजिटरीमा स्कोप गरिन्छ। README टेम्पलेटको साटो मानक सेटअप अनुकूलन गर्दा माथिको `if` हटाउनुहोस्: त्यो वर्कफ्लोले डिफल्ट सफलता सर्त प्रयोग गर्दछ, त्यसैले टोकन सिर्जना र PR सिर्जना मात्र अनुवाद र समीक्षा सफल भएपछि चल्छ।

See the official [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) for installation and token permissions.

## रनर सीमाहरू

GitHub-होस्ट गरिएको रनरहरूमा अधिकतम जॉब अवधी हुन्छ। ठूला रिपोजिटरीहरू वा धेरै लक्षित भाषाहरूले त्यो सीमा पार गर्न सक्छन्।

ठूला अनुवाद कार्यभारहरूको लागि:

- प्रति रन कम भाषाहरू अनुवाद गर्नुहोस्।
- `-md`, `-nb`, वा `-img` जस्ता सामग्री फ्ल्यागहरू प्रयोग गर्नुहोस्।
- जब रिपोजिटरीको आकार वा मोडेल विलम्बले होस्टेड रनरहरूलाई अविश्वसनीय बनाउँछ, स्वयं-होस्टेड रनर प्रयोग गर्नुहोस्।

## CI मा समीक्षा

`co-op-review` प्रयोग गर्नुहोस् जब पुल अनुरोधले LLM वा Vision प्रदायकहरूलाई कल नगरी उत्पन्न अनुवादहरूलाई मान्य गर्नुपर्छ।

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` एउटा बेटा deterministic समीक्षा कमाण्ड हो। यसको जाँचहरू र आउटपुट स्कीमा परिवर्तन हुनसक्छ, तर यो CI का लागि सुरक्षित हुने गरी डिजाइन गरिएको छ किनभने यसले फाइलहरू लेख्दैन वा मोडेल प्रदायकहरूलाई कल गर्दैन।