# GitHub Actions

जब आप चाहते हैं कि एक रिपॉज़िटरी बदले हुए दस्तावेज़ों का स्वतः अनुवाद करे और उत्पन्न आउटपुट के साथ एक पुल रिक्वेस्ट खोले, तो GitHub Actions का उपयोग करें।

मानक `GITHUB_TOKEN` सेटअप से शुरू करें, जिसमें उन संगठन रिपॉज़िटरीज़ के लिए भी शामिल हैं जहाँ नीति इसकी अनुमति देती है। जब आपका संगठन एक App पहचान की मांग करे या आपको स्वत: डाउनस्ट्रीम वर्कफ़्लो रन चाहिए हों तो [GitHub ऐप सेटअप](#github-app-setup) देखें।

**मानव संपादन:** ये वर्कफ़्लो बदले हुए स्रोत फ़ाइलों का पूरा पुनःअनुवाद करते हैं और उनकी अनुवादित प्रतियों में संपादित शब्दों को ओवरराइट कर सकते हैं। मर्ज करने से पहले प्रत्येक PR की समीक्षा करें। स्वीकृत संपादनों का Markdown ब्लॉक-स्तरीय संरक्षण एक कस्टम इंटीग्रेशन की आवश्यकता करता है [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) से।

## आपका पहला README अनुवाद PR

एक रूट `README.md` और एक लक्ष्य भाषा से शुरू करें। यह वर्कफ़्लो केवल Markdown का अनुवाद करता है, इसलिए Azure AI Vision आवश्यक नहीं है।

1. `.github/workflows/translate-readme.yml` में उस रिपॉज़िटरी की जड़ पर [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([GitHub पर टेम्पलेट देखें](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) कॉपी करें, और इसे उस रिपॉज़िटरी की डिफ़ॉल्ट ब्रांच पर कमिट करें जिसे आप अनुवाद करना चाहते हैं। टेम्पलेट रूट Action `Azure/co-op-translator@main` का उपयोग करता है, जो CLI को समान सोर्स रेफ़ से इंस्टॉल करता है। पुनरुत्पादन योग्य रन के लिए एक समीक्षा किए गए कमिट को पिन करें।
2. खोलें **Actions > Translate README > Run workflow**, एक भाषा चुनें, और **Preview only** को चुना हुआ छोड़ें। पूर्वावलोकन चरण में टोकन का अनुमान देखें। Preview मॉडल प्रदाताओं को कॉल नहीं करता, अनुवाद नहीं लिखता, और PR नहीं बनाता।
3. एक [टेक्स्ट प्रदाता](#prerequisites) के लिए सीक्रेट्स जोड़ें, और **Settings > Actions > General** के तहत **GitHub Actions को पुल अनुरोध बनाने और अनुमोदित करने की अनुमति दें**। टेम्पलेट अपने जॉब के लिए `contents: write` और `pull-requests: write` का अनुरोध करता है; आपको हर वर्कफ़्लो के लिए डिफ़ॉल्ट अनुमतियाँ बदलने की आवश्यकता नहीं है। यदि संगठन नीति इन अनुमतियों या इस सेटिंग को ब्लॉक करती है, तो अनुमोदित [GitHub ऐप](#github-app-setup) के लिए किसी प्रशासक से पूछें।
4. **Preview only** अनचेक करके वर्कफ़्लो को फिर से चलाएँ। यह पूर्वावलोकन करता है, अनुवाद करता है, `co-op-review --readme-only` चलाता है, और केवल अनुवाद और समीक्षा सफल होने के बाद ही अनुवाद PR बनाता या अपडेट करता है। workflow सारांश PR के लिंक देता है।
5. PR में शब्दावली और फ़ाइल परिवर्तनों की समीक्षा करें, फिर तैयार होने पर मर्ज करें। वर्कफ़्लो स्वतः मर्ज नहीं करता।

PR में केवल `translations/<language>/README.md` और उसकी भाषा मेटाडेटा फ़ाइल शामिल होती है। स्रोत README अपरिवर्तित रहता है, और अन्य दस्तावेज़ों के लिंक स्रोत दस्तावेज़ों की ओर ही संकेत करते रहते हैं। PR बॉडी में बदली गई फ़ाइलें और संरचनात्मक समीक्षा परिणाम सूचीबद्ध होते हैं। यदि अनुवाद या समीक्षा विफल हो जाती है, तो वर्कफ़्लो सारांश और विफल चरण लॉग्स की जाँच करें; कोई PR नहीं बनाया जाएगा। यदि कोई परिवर्तन नहीं है, तो नया PR आवश्यक नहीं है।

**संगठन और CI नोट:** एक GitHub App वैकल्पिक है, संगठन स्वामित्व की आवश्यकता नहीं है। `GITHUB_TOKEN` के साथ, PR खोलने, अपडेट करने, या पुनःखोलने वाले पुल-रिक्वेस्ट वर्कफ़्लो के लिए **Approve workflows to run** चुनने हेतु लिखने वाले उपयोगकर्ता की आवश्यकता होती है। इस टोकन से पुश वर्कफ़्लो ट्रिगर नहीं होते। बिना मानव हस्तक्षेप वाले डाउनस्ट्रीम CI के लिए [GitHub ऐप सेटअप](#github-app-setup) और GitHub के [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) देखें।

## पूर्वापेक्षाएँ

वर्कफ़्लो बनाने से पहले, उन AI सेवा सीक्रेट्स को कॉन्फ़िगर करें जिनकी आपकी अनुवाद रन को आवश्यकता है।

टेक्स्ट अनुवाद के लिए एक भाषा मॉडल प्रदाता आवश्यक है:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

छवि अनुवाद के लिए अतिरिक्त रूप से Azure AI Vision की आवश्यकता होती है:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

स्थानीय कॉन्फ़िगरेशन विवरणों के लिए [Configuration](configuration.md) और [Azure AI Setup](azure-ai-setup.md) देखें।

## मानक सेटअप

README वर्कफ़्लो आज़माने के बाद, इस सेटअप का उपयोग किसी रिपॉज़िटरी की Markdown फ़ाइलों को कई भाषाओं में अनुवाद करने के लिए करें। यह PR खोलने से पहले Markdown समीक्षा चलाता है और Azure AI Vision की आवश्यकता नहीं है।

### चरण 1: रिपॉज़िटरी सीक्रेट्स जोड़ें

अपने लक्ष्य रिपॉज़िटरी में **Settings** > **Secrets and variables** > **Actions** खोलें, फिर अपने वर्कफ़्लो द्वारा उपयोग किए जाने वाले प्रदाता सीक्रेट्स जोड़ें।

![Actions सीक्रेट्स चुनें](../../assets/github-actions/select-setting-action.png)

### चरण 2: वर्कफ़्लो अनुमतियाँ सक्षम करें

खोलें **Settings** > **Actions** > **General**।

के अंतर्गत **Workflow permissions**:

1. सक्षम करें **GitHub Actions को पुल अनुरोध बनाने और अनुमोदित करने की अनुमति दें**।
2. सेटिंग सहेजें।

नीचे दिया गया जॉब स्पष्ट रूप से `contents: write` और `pull-requests: write` का अनुरोध करता है। रिपॉज़िटरी की डिफ़ॉल्ट वर्कफ़्लो अनुमतियाँ अपरिवर्तित रखें। यदि संगठन नीति PR निर्माण को अवरुद्ध करती है, तो किसी प्रशासक से अनुमोदित [GitHub App](#github-app-setup) के बारे में पूछें।

### चरण 3: वर्कफ़्लो जोड़ें

बनाएँ `.github/workflows/co-op-translator.yml`:

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

`TARGET_LANGUAGES` को उन भाषाओं में बदलें जिनकी आपकी परियोजना को आवश्यकता है। समीक्षा केवल Markdown की जांच करने के लिए Python API का उपयोग करती है, जो अनुवाद चरण के साथ मेल खाती है। अनुवाद या समीक्षा त्रुटि PR निर्माण से पहले जॉब रोक देती है। वर्कफ़्लो PR को स्वतः मर्ज नहीं करता। बड़े रिपॉज़िटरी के लिए, `on.push` के तहत एक `paths:` फ़िल्टर जोड़ें ताकि वर्कफ़्लो केवल तब चले जब दस्तावेज़ों में बदलाव हों।

### वैकल्पिक: नोटबुक और छवियाँ

नोटबुक के लिए, अनुवाद कमांड में `-nb` जोड़ें और समीक्षा चरण में `notebook=True` सेट करें। छवि टेक्स्ट के लिए, दो [Azure AI Vision secrets](#prerequisites) कॉन्फ़िगर करें, उन्हें ट्रांसलेशन स्टेप के `env` में पास करें, कमांड में `-img` जोड़ें, और PR स्टेप के `add-paths` में `translated_images/` जोड़ें। अनुवादित छवियों की दृश्य रूप से समीक्षा करें; निर्णायक समीक्षा छवि टेक्स्ट या भाषाई सटीकता की पुष्टि नहीं करती।

## GitHub ऐप सेटअप

जब आपका संगठन एक App पहचान की मांग करता है, या जब जेनरेट किया गया PR `GITHUB_TOKEN` अनुमोदन चरण के बिना डाउनस्ट्रीम CI को ट्रिगर करने की जरूरत रखता है, तो एक अनुमोदित GitHub App का उपयोग करें। एक App संगठन नीति को बायपास नहीं करता; प्रशासक अभी भी इसकी इंस्टॉलेशन और अनुमतियाँ नियंत्रित करते हैं।

### चरण 1: GitHub ऐप बनाएँ या इंस्टॉल करें

जब उपलब्ध हो तो पहले से मौजूद संगठन-प्रदान किया गया App उपयोग करें, या ऐसा App बनाएं जिसे **Contents** और **Pull requests** के लिए रीड/राइट एक्सेस हो। आवश्यक संगठन अनुमोदन के साथ इसे लक्ष्य रिपॉज़िटरी पर इंस्टॉल करें।

नोट करें:

- App ID
- निजी कुंजी की सामग्री

उन्हें रिपॉज़िटरी सीक्रेट्स के रूप में स्टोर करें:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### चरण 2: एक ऐप टोकन उत्पन्न करें

मौजूदा पुल रिक्वेस्ट स्टेप के ठीक पहले यह स्टेप जोड़ें। README टेम्पलेट के लिए, वही सफलता शर्त उपयोग करें ताकि पूर्वावलोकन और असफल अनुवाद App टोकन न माँगें:

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

फिर केवल मौजूदा पुल रिक्वेस्ट स्टेप के `token` इनपुट को `${{ steps.generate_token.outputs.token }}` में बदलें। इसकी सफलता शर्त, ब्रांच, PR बॉडी, और `add-paths` अपरिवर्तित रखें। टोकन डिफ़ॉल्ट रूप से वर्तमान रिपॉज़िटरी तक सीमित होता है। मानक सेटअप को README टेम्पलेट के बजाय अनुकूलित करते समय ऊपर दिया `if` छोड़ दें: वह वर्कफ़्लो डिफ़ॉल्ट सफलता शर्त का उपयोग करता है, इसलिए टोकन निर्माण और PR निर्माण केवल अनुवाद और समीक्षा सफल होने के बाद चलेंगे।

इंस्टॉलेशन और टोकन अनुमतियों के लिए आधिकारिक [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) देखें।

## रनर सीमाएँ

GitHub-होस्टेड रनर्स की अधिकतम जॉब अवधि होती है। बड़े रिपॉज़िटरी या कई लक्ष्य भाषाएँ उस सीमा से अधिक हो सकती हैं।

बड़े अनुवाद कार्यभार के लिए:

- प्रति रन कम भाषाएँ अनुवाद करें।
- `-md`, `-nb`, या `-img` जैसे कंटेंट फ्लैग्स का उपयोग करें।
- रिपॉज़िटरी का आकार या मॉडल विलंबता होस्टेड रनर्स को अविश्वसनीय बनाती है तो self-hosted runner का उपयोग करें।

## CI में समीक्षा

जब किसी पुल रिक्वेस्ट को जेनरेट किए गए अनुवादों को LLM या Vision प्रदाताओं को कॉल किए बिना सत्यापित करना चाहिए तो `co-op-review` का उपयोग करें।

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` एक बीटा निर्णायक समीक्षा कमांड है। इसकी जाँचें और आउटपुट स्कीमा बदल सकते हैं, लेकिन इसे CI के लिए सुरक्षित बनाने के लिए डिज़ाइन किया गया है क्योंकि यह फ़ाइलें नहीं लिखता और मॉडल प्रदाताओं को कॉल नहीं करता।