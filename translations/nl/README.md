<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:29:17+00:00",
  "source_file": "README.md",
  "language_code": "nl"
}
-->
# Co-op Translator

_Automatiseer eenvoudig de vertaling van je educatieve GitHub-content naar meerdere talen en bereik een wereldwijd publiek._

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

### 🌐 Ondersteuning voor meerdere talen

#### Ondersteund door [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisch](../ar/README.md) | [Bengaals](../bn/README.md) | [Bulgaars](../bg/README.md) | [Birmaans (Myanmar)](../my/README.md) | [Chinees (Vereenvoudigd)](../zh/README.md) | [Chinees (Traditioneel, Hong Kong)](../hk/README.md) | [Chinees (Traditioneel, Macau)](../mo/README.md) | [Chinees (Traditioneel, Taiwan)](../tw/README.md) | [Kroatisch](../hr/README.md) | [Tsjechisch](../cs/README.md) | [Deens](../da/README.md) | [Nederlands](./README.md) | [Ests](../et/README.md) | [Fins](../fi/README.md) | [Frans](../fr/README.md) | [Duits](../de/README.md) | [Grieks](../el/README.md) | [Hebreeuws](../he/README.md) | [Hindi](../hi/README.md) | [Hongaars](../hu/README.md) | [Indonesisch](../id/README.md) | [Italiaans](../it/README.md) | [Japans](../ja/README.md) | [Koreaans](../ko/README.md) | [Litouws](../lt/README.md) | [Maleis](../ms/README.md) | [Marathi](../mr/README.md) | [Nepalees](../ne/README.md) | [Noors](../no/README.md) | [Perzisch (Farsi)](../fa/README.md) | [Pools](../pl/README.md) | [Portugees (Brazilië)](../br/README.md) | [Portugees (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Roemeens](../ro/README.md) | [Russisch](../ru/README.md) | [Servisch (Cyrillisch)](../sr/README.md) | [Slowaaks](../sk/README.md) | [Sloveens](../sl/README.md) | [Spaans](../es/README.md) | [Swahili](../sw/README.md) | [Zweeds](../sv/README.md) | [Tagalog (Filipijns)](../tl/README.md) | [Tamil](../ta/README.md) | [Thais](../th/README.md) | [Turks](../tr/README.md) | [Oekraïens](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamees](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Overzicht

**Co-op Translator** maakt het mogelijk om je educatieve GitHub-content snel te vertalen naar meerdere talen, zodat je moeiteloos een wereldwijd publiek bereikt. Wanneer je je Markdown-bestanden, afbeeldingen of Jupyter-notebooks bijwerkt, worden de vertalingen automatisch gesynchroniseerd zodat je educatieve GitHub-content actueel en relevant blijft voor internationale gebruikers.

Bekijk hoe Co-op Translator vertaalde educatieve GitHub-content organiseert:

![Voorbeeld](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.nl.png)

## Snel starten

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

## Minimale setup

- Maak een `.env` aan met behulp van de template: [.env.template](../../.env.template)
- Configureer één LLM-provider (Azure OpenAI of OpenAI)
- Voor het vertalen van afbeeldingen (`-img`), stel ook Azure AI Vision in
- Aanbevolen: Als je vertalingen hebt die door andere tools zijn gegenereerd, ruim deze eerst op om conflicten te voorkomen (bijvoorbeeld: `translations/`).
- Aanbevolen: Voeg een vertalingen-sectie toe aan je README met behulp van de [README talen-template](./README_languages_template.md)
- Zie: [Azure AI instellen](./getting_started/set-up-azure-ai.md)

## Gebruik

Vertaal alle ondersteunde types:

```bash
translate -l "ko ja"
```

Alleen Markdown:

```bash
translate -l "de" -md
```

Markdown + afbeeldingen:

```bash
translate -l "pt" -md -img
```

Alleen notebooks:

```bash
translate -l "zh" -nb
```

Meer opties: [Commandoreferentie](./getting_started/command-reference.md)

## Functies

- Automatische vertaling van Markdown, notebooks en afbeeldingen
- Houdt vertalingen synchroon met bronwijzigingen
- Werkt lokaal (CLI) of in CI (GitHub Actions)
- Gebruikt Azure OpenAI of OpenAI; optioneel Azure AI Vision voor afbeeldingen
- Behoudt de opmaak en structuur van Markdown

## Documentatie

- [Command-line gids](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions gids (Publieke repositories & standaard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions gids (Microsoft organisatie-repositories & org-niveau setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Ondersteunde talen](./getting_started/supported-languages.md)
- [Probleemoplossing](./getting_started/troubleshooting.md)

## Steun ons en stimuleer wereldwijd leren

Help mee om de manier waarop educatieve content wereldwijd wordt gedeeld te vernieuwen! Geef [Co-op Translator](https://github.com/azure/co-op-translator) een ⭐ op GitHub en steun onze missie om taalbarrières in leren en technologie te doorbreken. Jouw interesse en bijdragen maken echt verschil! Code-bijdragen en suggesties voor nieuwe functies zijn altijd welkom.

### Ontdek Microsoft educatieve content in jouw taal

- [AZD voor Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI voor Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) Voor Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents voor Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI voor Beginners met .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI voor Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI voor Beginners met Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML voor Beginners](https://aka.ms/ml-beginners)
- [Data Science voor Beginners](https://aka.ms/datascience-beginners)
- [AI voor Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity voor Beginners](https://github.com/microsoft/Security-101)
- [Webontwikkeling voor Beginners](https://aka.ms/webdev-beginners)
- [IoT voor Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video Presentaties

Leer meer over Co-op Translator via onze presentaties _(Klik op de afbeelding hieronder om te bekijken op YouTube.)_:

- **Open bij Microsoft**: Een korte introductie van 18 minuten en snelle gids over het gebruik van Co-op Translator.

  [![Open bij Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.nl.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Bijdragen

Dit project verwelkomt bijdragen en suggesties. Wil je bijdragen aan Azure Co-op Translator? Bekijk dan onze [CONTRIBUTING.md](./CONTRIBUTING.md) voor richtlijnen over hoe je kunt helpen om Co-op Translator toegankelijker te maken.

## Bijdragers

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Gedragscode

Dit project hanteert de [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Voor meer informatie zie de [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) of
neem contact op met [opencode@microsoft.com](mailto:opencode@microsoft.com) voor extra vragen of opmerkingen.

## Verantwoordelijke AI

Microsoft zet zich in om klanten te helpen onze AI-producten verantwoord te gebruiken, onze ervaringen te delen en vertrouwensrelaties op te bouwen via tools zoals Transparency Notes en Impact Assessments. Veel van deze bronnen zijn te vinden op [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofts benadering van verantwoordelijke AI is gebaseerd op onze AI-principes: eerlijkheid, betrouwbaarheid en veiligheid, privacy en beveiliging, inclusiviteit, transparantie en verantwoordelijkheid.

Grootschalige modellen voor natuurlijke taal, beeld en spraak – zoals die in dit voorbeeld worden gebruikt – kunnen zich soms oneerlijk, onbetrouwbaar of aanstootgevend gedragen, wat schade kan veroorzaken. Raadpleeg de [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) om op de hoogte te zijn van risico’s en beperkingen.

De aanbevolen manier om deze risico’s te beperken is het opnemen van een veiligheidssysteem in je architectuur dat schadelijk gedrag kan detecteren en voorkomen. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) biedt een onafhankelijke beschermingslaag die schadelijke door gebruikers of AI gegenereerde content in applicaties en diensten kan detecteren. Azure AI Content Safety bevat tekst- en beeld-API’s waarmee je schadelijk materiaal kunt opsporen. Er is ook een interactieve Content Safety Studio waarmee je voorbeelden kunt bekijken, verkennen en uitproberen voor het detecteren van schadelijke content in verschillende vormen. De volgende [quickstart documentatie](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) helpt je bij het maken van verzoeken naar de service.


Een ander aspect om rekening mee te houden is de algemene prestatie van de applicatie. Bij applicaties die gebruikmaken van meerdere modaliteiten en modellen, bedoelen we met prestaties dat het systeem werkt zoals jij en je gebruikers verwachten, inclusief het voorkomen van schadelijke uitkomsten. Het is belangrijk om de prestaties van je hele applicatie te beoordelen met behulp van [generatiekwaliteit en risico- en veiligheidsmetingen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Je kunt je AI-applicatie evalueren in je ontwikkelomgeving met de [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Op basis van een testdataset of een doel worden de generaties van je generatieve AI-applicatie kwantitatief gemeten met ingebouwde evaluators of evaluators die je zelf kiest. Wil je aan de slag met de prompt flow sdk om je systeem te evalueren, volg dan de [quickstart-gids](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Zodra je een evaluatierun hebt uitgevoerd, kun je [de resultaten visualiseren in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Handelsmerken

Dit project kan handelsmerken of logo’s bevatten van projecten, producten of diensten. Geautoriseerd gebruik van Microsoft
handelsmerken of logo’s is onderhevig aan en moet voldoen aan de
[Richtlijnen voor het gebruik van Microsoft handelsmerken en merk](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Gebruik van Microsoft handelsmerken of logo’s in aangepaste versies van dit project mag geen verwarring veroorzaken of suggereren dat Microsoft het sponsort.
Elk gebruik van handelsmerken of logo’s van derden valt onder het beleid van die derde partij.

## Hulp nodig

Loop je vast of heb je vragen over het bouwen van AI-apps? Word lid van:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Heb je feedback over het product of kom je fouten tegen tijdens het bouwen? Bezoek dan:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritische informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.