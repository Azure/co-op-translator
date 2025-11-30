<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T11:36:06+00:00",
  "source_file": "README.md",
  "language_code": "nl"
}
-->
# Co-op Translator

_Automatisch je educatieve GitHub-inhoud eenvoudig vertalen naar meerdere talen om een wereldwijd publiek te bereiken._

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

### 🌐 Meertalige ondersteuning

#### Ondersteund door [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisch](../ar/README.md) | [Bengaals](../bn/README.md) | [Bulgaars](../bg/README.md) | [Birmaans (Myanmar)](../my/README.md) | [Chinees (Vereenvoudigd)](../zh/README.md) | [Chinees (Traditioneel, Hong Kong)](../hk/README.md) | [Chinees (Traditioneel, Macau)](../mo/README.md) | [Chinees (Traditioneel, Taiwan)](../tw/README.md) | [Kroatisch](../hr/README.md) | [Tsjechisch](../cs/README.md) | [Deens](../da/README.md) | [Nederlands](./README.md) | [Ests](../et/README.md) | [Fins](../fi/README.md) | [Frans](../fr/README.md) | [Duits](../de/README.md) | [Grieks](../el/README.md) | [Hebreeuws](../he/README.md) | [Hindi](../hi/README.md) | [Hongaars](../hu/README.md) | [Indonesisch](../id/README.md) | [Italiaans](../it/README.md) | [Japans](../ja/README.md) | [Kannada](../kn/README.md) | [Koreaans](../ko/README.md) | [Litouws](../lt/README.md) | [Maleis](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalees](../ne/README.md) | [Nigeriaans Pidgin](../pcm/README.md) | [Noors](../no/README.md) | [Perzisch (Farsi)](../fa/README.md) | [Pools](../pl/README.md) | [Portugees (Brazilië)](../br/README.md) | [Portugees (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Roemeens](../ro/README.md) | [Russisch](../ru/README.md) | [Servisch (Cyrillisch)](../sr/README.md) | [Slowaaks](../sk/README.md) | [Sloveens](../sl/README.md) | [Spaans](../es/README.md) | [Swahili](../sw/README.md) | [Zweeds](../sv/README.md) | [Tagalog (Filipijns)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thais](../th/README.md) | [Turks](../tr/README.md) | [Oekraïens](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamees](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Overzicht

**Co-op Translator** helpt je om je educatieve GitHub-inhoud moeiteloos te lokaliseren in meerdere talen.  
Wanneer je je Markdown-bestanden, afbeeldingen of notebooks bijwerkt, blijven vertalingen automatisch gesynchroniseerd, zodat je inhoud accuraat en up-to-date blijft voor leerlingen wereldwijd.

Voorbeeld van hoe vertaalde inhoud is georganiseerd:

![Voorbeeld](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.nl.png)

## Snel aan de slag

```bash
# Maak en activeer een virtuele omgeving (aanbevolen)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installeer het pakket
pip install co-op-translator
# Vertalen
translate -l "ko ja fr" -md
```
  
Docker:

```bash
# Haal de openbare afbeelding op van GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Voer uit met de huidige map aangekoppeld en .env geleverd (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```
  
## Minimale setup

1. Maak een `.env` bestand aan met de template: [.env.template](../../.env.template)  
2. Configureer één LLM-provider (Azure OpenAI of OpenAI)  
3. (Optioneel) Voor afbeeldingvertaling (`-img`), configureer Azure AI Vision  
4. (Aanbevolen) Ruim eventuele eerdere vertalingen op om conflicten te voorkomen (bijv. `translations/`)  
5. (Aanbevolen) Voeg een vertaalsectie toe aan je README met behulp van de [README talen template](./getting_started/README_languages_template.md)  
6. Zie: [Azure AI instellen](./getting_started/set-up-azure-ai.md)

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

## Kenmerken

- Geautomatiseerde vertaling voor Markdown, notebooks en afbeeldingen  
- Houdt vertalingen synchroon met bronwijzigingen  
- Werkt lokaal (CLI) of in CI (GitHub Actions)  
- Gebruikt Azure OpenAI of OpenAI; optioneel Azure AI Vision voor afbeeldingen  
- Behoudt Markdown-opmaak en structuur

## Documentatie

- [Commandoregelgids](./getting_started/command-line-guide/command-line-guide.md)  
- [GitHub Actions gids (Openbare repositories & standaard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [GitHub Actions gids (Microsoft organisatie repositories & org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [README talen template](./getting_started/README_languages_template.md)  
- [Ondersteunde talen](./getting_started/supported-languages.md)  
- [Bijdragen](./CONTRIBUTING.md)  
- [Probleemoplossing](./getting_started/troubleshooting.md)

### Microsoft-specifieke gids
> [!NOTE]
> Alleen voor beheerders van de Microsoft “For Beginners” repositories.

- [De lijst met “andere cursussen” bijwerken (alleen voor MS Beginners repositories)](./getting_started/update-other-courses.md)

## Steun ons en bevorder wereldwijd leren

Doe mee aan de revolutie in het delen van educatieve content wereldwijd! Geef [Co-op Translator](https://github.com/azure/co-op-translator) een ⭐ op GitHub en steun onze missie om taalbarrières in leren en technologie te doorbreken. Jouw interesse en bijdragen maken een groot verschil! Codebijdragen en suggesties voor functies zijn altijd welkom.

### Ontdek Microsoft educatieve content in jouw taal

- [AZD voor Beginners](https://github.com/microsoft/AZD-for-beginners)  
- [Edge AI voor Beginners](https://github.com/microsoft/edgeai-for-beginners)  
- [Model Context Protocol (MCP) Voor Beginners](https://github.com/microsoft/mcp-for-beginners)  
- [AI Agents voor Beginners](https://github.com/microsoft/ai-agents-for-beginners)  
- [Generatieve AI voor Beginners met .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)  
- [Generatieve AI voor Beginners](https://github.com/microsoft/generative-ai-for-beginners)  
- [Generatieve AI voor Beginners met Java](https://github.com/microsoft/generative-ai-for-beginners-java)  
- [ML voor Beginners](https://aka.ms/ml-beginners)  
- [Data Science voor Beginners](https://aka.ms/datascience-beginners)  
- [AI voor Beginners](https://aka.ms/ai-beginners)  
- [Cybersecurity voor Beginners](https://github.com/microsoft/Security-101)  
- [Webontwikkeling voor Beginners](https://aka.ms/webdev-beginners)  
- [IoT voor Beginners](https://aka.ms/iot-beginners)  
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video presentaties

👉 Klik op de afbeelding hieronder om te bekijken op YouTube.

- **Open at Microsoft**: Een korte introductie van 18 minuten en een snelle gids over het gebruik van Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.nl.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Bijdragen

Dit project verwelkomt bijdragen en suggesties. Geïnteresseerd om bij te dragen aan Azure Co-op Translator? Bekijk onze [CONTRIBUTING.md](./CONTRIBUTING.md) voor richtlijnen over hoe je kunt helpen om Co-op Translator toegankelijker te maken.

## Bijdragers

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Gedragscode

Dit project heeft de [Microsoft Open Source Gedragscode](https://opensource.microsoft.com/codeofconduct/) aangenomen.  
Voor meer informatie zie de [Gedragscode FAQ](https://opensource.microsoft.com/codeofconduct/faq/) of  
neem contact op met [opencode@microsoft.com](mailto:opencode@microsoft.com) voor aanvullende vragen of opmerkingen.

## Verantwoorde AI

Microsoft zet zich in om onze klanten te helpen onze AI-producten op een verantwoorde manier te gebruiken, onze ervaringen te delen en vertrouwen op te bouwen via tools zoals Transparency Notes en Impact Assessments. Veel van deze bronnen zijn te vinden op [https://aka.ms/RAI](https://aka.ms/RAI).  
De aanpak van Microsoft voor verantwoorde AI is gebaseerd op onze AI-principes van eerlijkheid, betrouwbaarheid en veiligheid, privacy en beveiliging, inclusiviteit, transparantie en verantwoordelijkheid.

Grote taal-, beeld- en spraakmodellen - zoals die in dit voorbeeld worden gebruikt - kunnen zich mogelijk op manieren gedragen die oneerlijk, onbetrouwbaar of aanstootgevend zijn, wat schade kan veroorzaken. Raadpleeg de [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) om geïnformeerd te zijn over risico’s en beperkingen.
De aanbevolen aanpak om deze risico's te beperken is het opnemen van een veiligheidssysteem in je architectuur dat schadelijk gedrag kan detecteren en voorkomen. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) biedt een onafhankelijke beschermingslaag die schadelijke door gebruikers en AI gegenereerde inhoud in applicaties en diensten kan detecteren. Azure AI Content Safety bevat tekst- en beeld-API's waarmee je schadelijk materiaal kunt opsporen. We hebben ook een interactieve Content Safety Studio waarmee je voorbeeldcode kunt bekijken, verkennen en uitproberen voor het detecteren van schadelijke inhoud in verschillende modaliteiten. De volgende [quickstart-documentatie](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) begeleidt je bij het maken van verzoeken aan de service.

Een ander aspect om rekening mee te houden is de algehele prestatie van de applicatie. Bij multimodale en multimodelapplicaties verstaan we onder prestatie dat het systeem presteert zoals jij en je gebruikers verwachten, inclusief het niet genereren van schadelijke output. Het is belangrijk om de prestaties van je gehele applicatie te beoordelen met behulp van [generatiekwaliteit en risico- en veiligheidsmetriek](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Je kunt je AI-applicatie evalueren in je ontwikkelomgeving met behulp van de [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Op basis van een testdataset of een doel worden de generaties van je generatieve AI-applicatie kwantitatief gemeten met ingebouwde evaluators of aangepaste evaluators naar keuze. Om aan de slag te gaan met de prompt flow SDK voor het evalueren van je systeem, kun je de [quickstart-gids](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) volgen. Zodra je een evaluatieronde hebt uitgevoerd, kun je de resultaten [visualiseren in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Handelsmerken

Dit project kan handelsmerken of logo's bevatten van projecten, producten of diensten. Het geautoriseerd gebruik van Microsoft-handelsmerken of logo's is onderhevig aan en moet voldoen aan de [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Gebruik van Microsoft-handelsmerken of logo's in gewijzigde versies van dit project mag geen verwarring veroorzaken of impliceren dat Microsoft sponsor is. Elk gebruik van handelsmerken of logo's van derden is onderhevig aan het beleid van die derden.

## Hulp krijgen

Als je vastloopt of vragen hebt over het bouwen van AI-apps, sluit je aan bij:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Als je productfeedback hebt of fouten tegenkomt tijdens het bouwen, bezoek dan:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->