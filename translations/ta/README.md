<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T04:39:43+00:00",
  "source_file": "README.md",
  "language_code": "ta"
}
-->
# Co-op Translator

_உங்கள் கல்வி சார்ந்த GitHub உள்ளடக்கங்களை பல மொழிகளில் தானாக மொழிபெயர்த்து, உலகளாவிய பார்வையாளர்களை எளிதாக அடைய உதவும் ஒரு கருவி._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 பல மொழி ஆதரவு

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) வழங்கும் மொழிகள்

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](./README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## அறிமுகம்

**Co-op Translator** உங்கள் கல்வி சார்ந்த GitHub உள்ளடக்கங்களை பல மொழிகளில் விரைவாக மொழிபெயர்க்க உதவுகிறது, இதனால் உலகம் முழுவதும் உள்ள பயனர்களை எளிதாக அடைய முடியும். நீங்கள் உங்கள் Markdown கோப்புகள், படங்கள் அல்லது Jupyter நோட்புக்குகளை புதுப்பித்தால், மொழிபெயர்ப்புகள் தானாக ஒத்திசைக்கப்படும், இதனால் உங்கள் கல்வி GitHub உள்ளடக்கம் எப்போதும் புதிதாகவும், சரியானதாகவும் இருக்கும்.

Co-op Translator எப்படி மொழிபெயர்க்கப்பட்ட கல்வி GitHub உள்ளடக்கங்களை ஒழுங்குபடுத்துகிறது என்பதை பாருங்கள்:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.ta.png)

## விரைவான தொடக்கம்

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## குறைந்தபட்ச அமைப்பு

- [.env.template](../../.env.template) என்ற மாதிரியைப் பயன்படுத்தி `.env` உருவாக்கவும்
- ஒரு LLM வழங்குநரை அமைக்கவும் (Azure OpenAI அல்லது OpenAI)
- பட மொழிபெயர்ப்புக்கு (`-img`), Azure AI Vision ஐயும் அமைக்கவும்
- பரிந்துரை: பிற கருவிகள் மூலம் உருவாக்கப்பட்ட மொழிபெயர்ப்புகள் இருந்தால், முதலில் அவற்றை நீக்கவும் (உதாரணம்: `translations/`).
- பரிந்துரை: உங்கள் README-வில் மொழிபெயர்ப்பு பகுதியை [README languages template](./README_languages_template.md) மூலம் சேர்க்கவும்
- மேலும் பார்க்க: [Azure AI அமைக்க](./getting_started/set-up-azure-ai.md)

## பயன்பாடு

அனைத்து ஆதரிக்கப்படும் வகைகளையும் மொழிபெயர்க்க:

```bash
translate -l "ko ja"
```

Markdown மட்டும்:

```bash
translate -l "de" -md
```

Markdown + படங்கள்:

```bash
translate -l "pt" -md -img
```

நோட்புக்குகள் மட்டும்:

```bash
translate -l "zh" -nb
```

மேலும் விருப்பங்கள்: [கட்டளை குறிப்பு](./getting_started/command-reference.md)

## அம்சங்கள்

- Markdown, நோட்புக், படங்களுக்கு தானாக மொழிபெயர்ப்பு
- மூலத்தில் மாற்றங்கள் வந்தால் மொழிபெயர்ப்புகளை ஒத்திசைக்கிறது
- உள்ளூர் (CLI) அல்லது CI (GitHub Actions) மூலம் இயங்கும்
- Azure OpenAI அல்லது OpenAI பயன்படுத்துகிறது; படங்களுக்கு விருப்பமாக Azure AI Vision
- Markdown வடிவமைப்பு மற்றும் அமைப்பை பாதுகாக்கிறது

## ஆவணங்கள்

- [கமாண்டு-லைன் வழிகாட்டி](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions வழிகாட்டி (பொது ரெப்போ & சாதாரண ரகசியங்கள்)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions வழிகாட்டி (Microsoft நிறுவனம் மற்றும் அமைப்பு நிலை அமைப்புகள்)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [ஆதரிக்கப்படும் மொழிகள்](./getting_started/supported-languages.md)
- [சிக்கல்கள் தீர்க்க](./getting_started/troubleshooting.md)

## எங்களை ஆதரித்து உலகளாவிய கல்வியை ஊக்குவிக்கவும்

உலகளாவிய கல்வி உள்ளடக்க பகிர்வை மாற்றும் இந்த முயற்சியில் எங்களுடன் சேருங்கள்! [Co-op Translator](https://github.com/azure/co-op-translator)க்கு GitHub-ல் ⭐ அளித்து, கற்றல் மற்றும் தொழில்நுட்பத்தில் மொழி தடைகளை உடைக்கும் எங்கள் நோக்கை ஆதரிக்கவும். உங்கள் ஆர்வமும் பங்களிப்பும் மிகுந்த தாக்கத்தை ஏற்படுத்தும்! குறியீடு பங்களிப்பும், அம்ச பரிந்துரைகளும் எப்போதும் வரவேற்கப்படுகின்றன.

### உங்கள் மொழியில் Microsoft கல்வி உள்ளடக்கங்களை ஆராயுங்கள்

- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## வீடியோ விளக்கங்கள்

Co-op Translator பற்றி மேலும் அறிய எங்கள் விளக்கங்களைப் பாருங்கள் _(கீழே உள்ள படத்தை கிளிக் செய்து YouTube-ல் பார்க்கவும்.)_:

- **Open at Microsoft**: Co-op Translator-ஐ எவ்வாறு பயன்படுத்துவது என்ற 18 நிமிட சுருக்கமான அறிமுகம் மற்றும் விரைவான வழிகாட்டி.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.ta.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## பங்களிப்பு

இந்த திட்டம் பங்களிப்புகளையும் பரிந்துரைகளையும் வரவேற்கிறது. Azure Co-op Translator-க்கு பங்களிக்க விரும்புகிறீர்களா? எங்கள் [CONTRIBUTING.md](./CONTRIBUTING.md) வழிகாட்டியைப் பார்க்கவும், Co-op Translator-ஐ மேலும் அணுகக்கூடியதாக மாற்ற உதவுங்கள்.

## பங்களிப்பாளர்கள்

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## நடத்தை விதிகள்

இந்த திட்டம் [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ஐ பின்பற்றுகிறது.
மேலும் தகவலுக்கு [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) பார்க்கவும் அல்லது
[opencode@microsoft.com](mailto:opencode@microsoft.com) என்ற முகவரிக்கு உங்கள் கேள்விகள் அல்லது கருத்துகளை அனுப்பவும்.

## பொறுப்பான AI

Microsoft எங்கள் AI தயாரிப்புகளை வாடிக்கையாளர்கள் பொறுப்புடன் பயன்படுத்த உதவ, எங்கள் அனுபவங்களை பகிர்ந்து, நம்பிக்கையுடன் கூடிய கூட்டாண்மையை உருவாக்கும் நோக்கில் Transparency Notes மற்றும் Impact Assessments போன்ற கருவிகளை வழங்குகிறது. இந்த வளங்களில் பலவற்றை [https://aka.ms/RAI](https://aka.ms/RAI) இல் காணலாம்.
Microsoft-ன் பொறுப்பான AI அணுகுமுறை நியாயம், நம்பகத்தன்மை மற்றும் பாதுகாப்பு, தனியுரிமை மற்றும் பாதுகாப்பு, உள்ளடக்கம், வெளிப்படைத்தன்மை மற்றும் பொறுப்பு ஆகிய AI கொள்கைகளில் அடிப்படையிலுள்ளது.

இந்த மாதிரியில் பயன்படுத்தப்படும் பெரிய அளவிலான இயற்கை மொழி, படம் மற்றும் பேச்சு மாதிரிகள் - அவை சில நேரங்களில் நியாயமற்ற, நம்பகமற்ற அல்லது ஆபத்தான முறையில் செயல்படலாம், இதனால் பாதிப்புகள் ஏற்படலாம். தயவுசெய்து [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ஐ படித்து, அபாயங்கள் மற்றும் வரம்புகள் பற்றி அறிந்து கொள்ளவும்.

இந்த அபாயங்களை குறைக்கும் பரிந்துரைக்கப்பட்ட வழி உங்கள் கட்டமைப்பில் பாதுகாப்பு அமைப்பை சேர்ப்பது. இது ஆபத்தான நடத்தை ஏற்படுவதை கண்டறிந்து தடுக்கும். [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) என்பது ஒரு சுயாதீன பாதுகாப்பு அடுக்கு, இது பயனர் உருவாக்கிய மற்றும் AI உருவாக்கிய ஆபத்தான உள்ளடக்கங்களை கண்டறிய உதவுகிறது. Azure AI Content Safety-யில் உரை மற்றும் படம் API-கள் உள்ளன, அவை ஆபத்தான உள்ளடக்கத்தை கண்டறிய உதவுகின்றன. மேலும், Content Safety Studio என்ற இடைமுகம் உள்ளது, இதில் நீங்கள் பல்வேறு வகைகளில் உள்ள ஆபத்தான உள்ளடக்கத்தை கண்டறியும் மாதிரி குறியீடுகளை முயற்சி செய்யலாம். கீழ்காணும் [விரைவான தொடக்கம் ஆவணம்](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) இந்த சேவைக்கு கோரிக்கைகளை அனுப்புவது எப்படி என்பதை வழிகாட்டுகிறது.


மற்றொரு முக்கிய அம்சம் என்பது முழு பயன்பாட்டின் செயல்திறன். பல்வேறு முறைகள் மற்றும் பல்வேறு மாதிரிகள் கொண்ட பயன்பாடுகளில், செயல்திறன் என்பது உங்கள் மற்றும் உங்கள் பயனர்களின் எதிர்பார்ப்புக்கு ஏற்ப அமைப்பின் செயல்பாடு, அதில் தீங்கு விளைவிக்கும் வெளியீடுகள் உருவாகாமல் இருப்பதும் அடங்கும். உங்கள் முழு பயன்பாட்டின் செயல்திறனை மதிப்பீடு செய்வது முக்கியம், அதற்காக [உருவாக்க தரம் மற்றும் அபாயம் மற்றும் பாதுகாப்பு அளவீடுகள்](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) பயன்படுத்தலாம்.

உங்கள் AI பயன்பாட்டை உங்கள் மேம்பாட்டு சூழலில் [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) மூலம் மதிப்பீடு செய்யலாம். ஒரு சோதனை தரவுத்தொகுப்பு அல்லது இலக்கை கொண்டு, உங்கள் உருவாக்கும் AI பயன்பாட்டின் வெளியீடுகள், உள்ளமைக்கப்பட்ட மதிப்பீட்டாளர்கள் அல்லது உங்கள் விருப்பப்படி தனிப்பயன் மதிப்பீட்டாளர்களால் அளவிடப்படுகின்றன. உங்கள் அமைப்பை மதிப்பீடு செய்ய prompt flow sdk-ஐ பயன்படுத்த தொடங்க, [விரைவு வழிகாட்டி](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)யை பின்பற்றலாம். ஒரு மதிப்பீட்டு இயக்கத்தை செயல்படுத்திய பிறகு, [Azure AI Studio-வில் முடிவுகளை காணலாம்](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## வர்த்தகமுத்திரைகள்

இந்த திட்டத்தில் திட்டங்கள், தயாரிப்புகள் அல்லது சேவைகளுக்கான வர்த்தகமுத்திரைகள் அல்லது லோகோக்கள் இருக்கலாம். Microsoft
வர்த்தகமுத்திரைகள் அல்லது லோகோக்களை அங்கீகரிக்கப்பட்ட முறையில் பயன்படுத்துவது
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) ஐ பின்பற்ற வேண்டும்.
இந்த திட்டத்தின் மாற்றியமைக்கப்பட்ட பதிப்புகளில் Microsoft வர்த்தகமுத்திரைகள் அல்லது லோகோக்களை பயன்படுத்தும் போது குழப்பம் ஏற்படக்கூடாது அல்லது Microsoft ஆதரவு உள்ளது என்று தெரிவிக்க கூடாது.
மூன்றாம் தரப்பு வர்த்தகமுத்திரைகள் அல்லது லோகோக்களை பயன்படுத்தும் போது அந்த மூன்றாம் தரப்பின் கொள்கைகளை பின்பற்ற வேண்டும்.

## உதவி பெறுதல்

நீங்கள் சிக்கலில் சிக்கினால் அல்லது AI பயன்பாடுகளை உருவாக்குவது குறித்து கேள்விகள் இருந்தால், இணைந்திருங்கள்:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

தயாரிப்பில் கருத்து தெரிவிக்க அல்லது பிழைகள் ஏற்பட்டால், இங்கே செல்லவும்:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**பொறுப்புத்துறப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவையான [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாம் துல்லியத்திற்காக முயற்சி செய்தாலும், தானாக மொழிபெயர்க்கப்பட்ட மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை தயவுசெய்து கவனிக்கவும். மூல ஆவணம் அதன் சொந்த மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்தவொரு தவறான புரிதல் அல்லது தவறான விளக்கத்திற்கு நாங்கள் பொறுப்பல்ல.