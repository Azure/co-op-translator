# GitHub Actions

जेव्हा तुम्हाला एखाद्या रिपॉझिटरीने बदललेला दस्तऐवज स्वयंचलितरित्या अनुवाद करावा आणि तयार केलेल्या आउटपुटसह एक pull request उघडावा तेव्हा GitHub Actions वापरा.

सुरुवात पारंपारिक `GITHUB_TOKEN` सेटअपपासून करा, संघटनेच्या रिपॉझिटरीजसाठीही जिथे धोरण परवानगी देते तेथे याचा समावेश करा. जेव्हा तुमच्या संघटनेला App ओळख आवश्यक असेल किंवा तुम्हाला स्वयंचलित डाउनस्ट्रीम वर्कफ्लो चालवायचे असतील तेव्हा [GitHub App Setup](#github-app-setup) बघा.

**मानवी संपादन:** ही वर्कफ्लो बदललेली स्रोत फाईल पूर्णपणे परत अनुवादित करतात आणि त्यांच्या अनुवादांमध्ये केलेले शब्दसुधार ओव्हरराइट करू शकतात. प्रत्येक PR मर्ज करण्यापूर्वी तपासा. स्वीकृत संपादने Markdown ब्लॉक-स्तरीय पद्धतीने जपण्यासाठी [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) सोबत एक सानुकूल समाकलन आवश्यक आहे.

## तुमचा पहिला README अनुवाद PR

एक मूळ `README.md` आणि एक लक्ष्य भाषा घेऊन सुरू करा. हा वर्कफ्लो फक्त Markdown अनुवाद करतो, त्यामुळे Azure AI Vision आवश्यक नाही.

1. [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([view the template on GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) फाइल कॉपी करा आणि ती रिपॉझिटरीमध्ये `.github/workflows/translate-readme.yml` म्हणून ठेवा, आणि ती त्या रिपॉझिटरीच्या डीफॉल्ट ब्रँचवर कमिट करा. टेम्पलेट मूळ Action मध्ये `Azure/co-op-translator@main` वापरते, जे CLI तेच स्रोत रेफरन्समधून इन्स्टॉल करते. पुन्हा पुनरुत्पादनक्षम धावांसाठी तपासलेला कमिट पिन करा.
2. Open **Actions > Translate README > Run workflow**, एक भाषा निवडा, आणि **Preview only** निवडलेले ठेवावे. प्रीव्ह्यू टप्प्यात टोकन अंदाज तपासा. प्रीव्ह्यू मॉडेल प्रदाते कॉल करत नाही, अनुवाद लिहीत नाही किंवा PR तयार करत नाही.
3. एका [टेक्स्ट प्रदात्याचे](#prerequisites) secrets जोडा, आणि **Settings > Actions > General** अंतर्गत **GitHub Actions ला pull requests तयार आणि मंजूर करण्याची परवानगी द्या** सक्षम करा. टेम्पलेट त्याच्या जॉबसाठी `contents: write` आणि `pull-requests: write` विनंती करते; प्रत्येक वर्कफ्लोसाठी डिफॉल्ट परवाने बदलण्याची आवश्यकता नाही. जर संघटना धोरण या परवान्यांना किंवा या सेटिंगला अडथळा करीत असेल तर मंजूर [GitHub App](#github-app-setup) संदर्भात प्रशासकाशी संपर्क करा.
4. **Preview only** अनचेक करून वर्कफ्लो पुन्हा चालवा. हे प्रीव्ह्यू करते, अनुवाद करते, `co-op-review --readme-only` चालवते, आणि अनुवाद व पुनरावलोकन यशस्वी झाल्यानंतरच एक अनुवाद PR तयार करते किंवा अपडेट करते. वर्कफ्लो सारांश PR कडे लिंक करतो.
5. PR मधील शब्दरचना आणि फाईल बदल तपासा, नंतर तयार झाल्यावर merge करा. वर्कफ्लो आपोआप merge करत नाही.

PR मध्ये फक्त `translations/<language>/README.md` आणि त्याची भाषा मेटाडेटा फाईल असते. स्रोत README अपरिवर्तित राहतो, आणि इतर दस्तऐवजांकडे असलेले दुवे स्रोत दस्तऐवजांकडेच निर्देशीत राहतात. PR बॉडीमध्ये बदललेल्या फाईल्स आणि संरचनात्मक पुनरावलोकनाच्या निकालांची यादी असते. जर अनुवाद किंवा पुनरावलोकन अयशस्वी झाले तर वर्कफ्लो सारांश आणि अयशस्वी स्टेप लॉग तपासा; कोणतीही PR तयार केली जात नाही. जर कोणतेही बदल नसतील तर नवीन PR ची आवश्यकता नाही.

**संस्था आणि CI नोंद:** GitHub App ऐच्छिक आहे, संघटनेच्या मालकीसाठी गरजेचे नाही. `GITHUB_TOKEN` सह, PR उघडणे, अपडेट करणे किंवा पुन्हा उघडण्याच्या pull-request वर्कफ्लो साठी **Approve workflows to run** निवडण्यासाठी write access असलेला वापरकर्ता आवश्यक असतो. Push वर्कफ्लो या टोकनने ट्रिगर होत नाहीत. नियंत्रण रहित डाउनस्ट्रीम CI साठी, [GitHub App Setup](#github-app-setup) आणि GitHub ची [वर्कफ्लो ट्रिगर नियम](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) पहा.

## पूर्वअटी

वर्कफ्लो तयार करण्यापूर्वी, तुमच्या अनुवाद धावनेसाठी आवश्यक AI सेवा secrets कॉन्फिगर करा.

टेक्स्ट अनुवादासाठी एक भाषा मॉडेल प्रदाता आवश्यक आहे:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

इमेज अनुवादासाठी अतिरिक्तपणे Azure AI Vision आवश्यक आहे:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

स्थानिक कॉन्फिगरेशन तपशीलांसाठी [Configuration](configuration.md) आणि [Azure AI Setup](azure-ai-setup.md) बघा.

## मानक सेटअप

README वर्कफ्लो वापरून पाहिल्यानंतर, रेपोच्या Markdown फाइल्स अनेक भाषांमध्ये अनुवादित करण्यासाठी हा सेटअप वापरा. हा PR उघडण्यापूर्वी Markdown पुनरावलोकन चालवतो आणि त्यासाठी Azure AI Vision ची आवश्यकता नाही.

### पाऊल 1: रिपॉझिटरी Secrets जोडा

तुमच्या लक्ष्य रिपॉझिटरीमध्ये, **Settings** > **Secrets and variables** > **Actions** उघडा, आणि नंतर तुमच्या वर्कफ्लो साठी आवश्यक प्रदाता secrets जोडा.

![Actions secrets निवडा](../../assets/github-actions/select-setting-action.png)

### पाऊल 2: वर्कफ्लो परवानग्या सक्षम करा

उघडा **Settings** > **Actions** > **General**.

**Workflow permissions** अंतर्गत:

1. **GitHub Actions ला pull requests तयार आणि मंजूर करण्याची परवानगी द्या** सक्षम करा.
2. सेटिंग जतन करा.

खालील जॉब स्पष्टपणे `contents: write` आणि `pull-requests: write` विनंती करतो. रिपॉझिटरीचे डीफॉल्ट वर्कफ्लो परवाने अपरिवर्तित ठेवा. जर संघटना धोरण PR निर्मिती अडवित असेल तर मंजूर [GitHub App](#github-app-setup) विषयी प्रशासकाशी संपर्क साधा.

### पाऊल 3: वर्कफ्लो जोडा

तयार करा `.github/workflows/co-op-translator.yml`:

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

तुमच्या प्रोजेक्टला लागणाऱ्या भाषांसाठी `TARGET_LANGUAGES` बदला. पुनरावलोकन Markdown फक्त तपासण्यासाठी Python API वापरते, जे अनुवाद टप्प्यासोबत जुळते. अनुवाद किंवा पुनरावलोकन त्रुटी असल्यास जॉब PR तयार होण्यापूर्वी थांबते. वर्कफ्लो PR आपोआप merge करत नाही. मोठ्या रिपॉझिटरीजसाठी, वर्कफ्लो फक्त दस्तऐवजीकरण बदलल्यावर चालणे यासाठी `on.push` अंतर्गत `paths:` फिल्टर जोडा.

### ऐच्छिक: नोटबुक आणि प्रतिमा

नोटबुकसाठी, अनुवाद कमांडमध्ये `-nb` जोडा आणि पुनरावलोकन टप्प्यात `notebook=True` सेट करा. इमेज टेक्स्टसाठी, दोन [Azure AI Vision secrets](#prerequisites) कॉन्फिगर करा, त्यांना अनुवाद टप्प्यातील `env` मध्ये पास करा, कमांडमध्ये `-img` जोडा, आणि PR टप्प्यातील `add-paths` मध्ये `translated_images/` जोडा. अनुवादित प्रतिमा दृष्टीने तपासा; deterministic review प्रतिमेतील मजकूर किंवा भाषिक अचूकता प्रमाणित करत नाही.

## GitHub App सेटअप

जेव्हा तुमच्या संघटनेला App ओळख आवश्यक असेल, किंवा जेव्हा तयार झालेला PR `GITHUB_TOKEN` मंजुरी चरणाशिवाय डाउनस्ट्रीम CI ट्रिगर करणे आवश्यक असेल, तेव्हा मंजूर केलेला GitHub App वापरा. App संघटना धोरणाला बायपास करत नाही; प्रशासक तरीही त्याची स्थापना आणि परवानग्यांचे नियंत्रण करतात.

### पाऊल 1: GitHub App तयार करा किंवा इन्स्टॉल करा

उपलब्ध असल्यास अस्तित्वात असलेला संघटनेने प्रदान केलेला App वापरा, किंवा **Contents** आणि **Pull requests** साठी read/write access असलेला App तयार करा. आवश्यक संघटना मंजुरीसह तो लक्ष्य रिपॉझिटरीवर इन्स्टॉल करा.

नोंद करा:

- App ID
- Private key सामग्री

त्यांना रिपॉझिटरी secrets म्हणून ठेवा:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### पाऊल 2: App Token तयार करा

विद्यमान pull request स्टेपच्या अगोदर हा स्टेप तत्काळ जोडा. README टेम्पलेटसाठी, प्रीव्ह्यू आणि अयशस्वी अनुवादांनी App token मागितले जाऊ नयेत यासाठी त्याच यशाच्या स्थितीचा वापर करा:

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

नंतर विद्यमान pull request स्टेपच्या `token` इनपुटला फक्त `${{ steps.generate_token.outputs.token }}` मध्ये बदला. त्याची success condition, ब्रँच, PR बॉडी आणि `add-paths` अपरिवर्तित ठेवा. टोकन डीफॉल्टने वर्तमान रिपॉझिटरीवर scoped असते. README टेम्पलेटऐवजी मानक सेटअप अनुकूल करताना, वरचे `if` वगळा: त्या वर्कफ्लोने डीफॉल्ट success condition वापरली आहे, त्यामुळे टोकन निर्मिती आणि PR निर्मिती फक्त अनुवाद आणि पुनरावलोकन यशस्वी झाल्यानंतर चालते.

इंस्टॉलेशन आणि टोकन परवानग्यांसाठी अधिकृत [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) पहा.

## रनर मर्यादा

GitHub-hosted रनर्सना जास्तीत जास्त जॉब कालावधी असतो. मोठ्या रिपॉझिटरीज किंवा अनेक लक्ष्य भाषा या मर्यादेपर्यंत पोहोचू शकतात.

मोठ्या अनुवाद कार्यभारासाठी:

- प्रत्येकी रनसाठी कमी भाषांमध्ये अनुवाद करा.
- `-md`, `-nb`, किंवा `-img` सारखे कंटेंट फ्लॅग वापरा.
- रिपॉझिटरीचा आकार किंवा मॉडेल विलंब hosted रनर्स अविश्वसनीय बनवित असल्यास self-hosted runner वापरा.

## CI मध्ये पुनरावलोकन

जेव्हा पुल रिक्वेस्टने तयार केलेले अनुवाद LLM किंवा Vision प्रदात्यांना कॉल न करता वैध ठरवायचे असतील तेव्हा `co-op-review` वापरा.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` हे एक बीटा deterministic review कमांड आहे. त्याचे तपासणी आणि आउटपुट स्कीमा विकसित होऊ शकतात, परंतु हे CI साठी सुरक्षित असावे म्हणून डिझाइन केले आहे कारण ते फाइल लिहीत नाही किंवा मॉडेल प्रदात्यांना कॉल करत नाही.