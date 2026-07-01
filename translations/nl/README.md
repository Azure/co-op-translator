# Co-op Translator

_Een eenvoudige manier om vertalingen voor je educatieve GitHub-inhoud te automatiseren en te onderhouden in meerdere talen terwijl je project zich ontwikkelt._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
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

**Begin hier:** [Kies je workflow](https://azure.github.io/co-op-translator/workflows/) | [Configuratie](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP-server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Ondersteuning voor meerdere talen

#### Ondersteund door [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisch](../ar/README.md) | [Bengaals](../bn/README.md) | [Bulgaars](../bg/README.md) | [Birmaans (Myanmar)](../my/README.md) | [Chinees (Vereenvoudigd)](../zh-CN/README.md) | [Chinees (Traditioneel, Hongkong)](../zh-HK/README.md) | [Chinees (Traditioneel, Macau)](../zh-MO/README.md) | [Chinees (Traditioneel, Taiwan)](../zh-TW/README.md) | [Kroatisch](../hr/README.md) | [Tsjechisch](../cs/README.md) | [Deens](../da/README.md) | [Nederlands](./README.md) | [Ests](../et/README.md) | [Fins](../fi/README.md) | [Frans](../fr/README.md) | [Duits](../de/README.md) | [Grieks](../el/README.md) | [Hebreeuws](../he/README.md) | [Hindi](../hi/README.md) | [Hongaars](../hu/README.md) | [Indonesisch](../id/README.md) | [Italiaans](../it/README.md) | [Japans](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Koreaans](../ko/README.md) | [Litouws](../lt/README.md) | [Maleis](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalees](../ne/README.md) | [Nigeriaans Pidgin](../pcm/README.md) | [Noors](../no/README.md) | [Perzisch (Farsi)](../fa/README.md) | [Pools](../pl/README.md) | [Portugees (Brazilië)](../pt-BR/README.md) | [Portugees (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Roemeens](../ro/README.md) | [Russisch](../ru/README.md) | [Servisch (Cyrillisch)](../sr/README.md) | [Slowaaks](../sk/README.md) | [Sloveens](../sl/README.md) | [Spaans](../es/README.md) | [Swahili](../sw/README.md) | [Zweeds](../sv/README.md) | [Tagalog (Filipijns)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thais](../th/README.md) | [Turks](../tr/README.md) | [Oekraïens](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamees](../vi/README.md)

> **Lieverd om lokaal te klonen?**
>
> Deze repository bevat meer dan 50 taalvertalingen, wat de downloadgrootte aanzienlijk vergroot. Om te klonen zonder vertalingen, gebruik sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Dit geeft je alles wat je nodig hebt om de cursus te voltooien met een veel snellere download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Overzicht

**Co-op Translator** helpt je om je educatieve GitHub-inhoud moeiteloos te lokaliseren naar meerdere talen.
Wanneer je je Markdown-bestanden, afbeeldingen of notebooks bijwerkt, blijven vertalingen automatisch gesynchroniseerd, zodat je inhoud accuraat en up-to-date blijft voor leerlingen wereldwijd.

Gebruik het vanaf de CLI voor repository-vertaling, via de Python API voor automatisering, of via de MCP-server voor agent- en editorworkflows.

Voorbeeld van hoe vertaalde inhoud is georganiseerd:

![Example](../../imgs/translation-ex.png)

## Waarom Co-op Translator?

Het vertalen van één bestand is eenvoudig. Het up-to-date en vertaald houden van een hele documentatierepository, met koppelingen, is het lastige deel.

| Probleem | Hoe Co-op Translator helpt |
| --- | --- |
| Lange docs zijn niet één prompt | Grote Markdown-bestanden worden opgesplitst in stukken, zodat een lange README niet afhankelijk is van één fragiele modelrespons. Als een chunk faalt, kan Co-op Translator opnieuw proberen en alleen het mislukte gedeelte opnieuw opsplitsen. |
| Onvolledige vertalingen mogen niet als actueel worden gemarkeerd | Een ingekorte vertaling mag nooit als up-to-date worden afgesloten. Co-op Translator controleert de integriteit van vertalingen voordat deze worden opgeslagen en kan structureel onvolledige bestaande vertalingen detecteren. |
| Koppelingen moeten overeenkomen met de vertaalde repo-structuur | Handmatige vertalingen laten vaak relatieve koppelingen die terugverwijzen naar de bronboom. Co-op Translator herschrijft Markdown-, notebook-, afbeelding- en README-koppelingen zodat ze overeenkomen met de `translations/<lang>/...`-structuur. |
| Vertaling moet werken voor een hele repo | Co-op Translator verwerkt README-bestanden, docs, notebooks en afbeeldingstekst als onderdeel van één repository-workflow, in plaats van bestanden één voor één te vertalen. |
| Het onderhouden van vertalingen is belangrijker dan ze één keer maken | Bron-hashes en vertaalmetadata laten Co-op Translator verouderde bestanden vinden, ongewijzigde bestanden overslaan en vertaalde inhoud gesynchroniseerd houden terwijl de bronrepo zich ontwikkelt. |

## Hoe de vertaantoestand wordt beheerd

Co-op Translator beheert vertaalde inhoud als **geversioneerde software-artifacten**,  
niet als statische bestanden.

De tool volgt de staat van vertaalde Markdown, afbeeldingen en notebooks
met behulp van **taalspecifieke metadata**.

Dit ontwerp stelt Co-op Translator in staat om:

- Betrouwbaar verouderde vertalingen te detecteren
- Markdown, afbeeldingen en notebooks consequent te behandelen
- Veilig op te schalen over grote, snel veranderende, meertalige repositories

Door vertalingen te modelleren als beheerde artifacts,
sluiten vertaalworkflows op natuurlijke wijze aan bij moderne
praktijken voor software-afhankelijkheden en artifactbeheer.

→ [Hoe de vertaantoestand wordt beheerd](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Gerelateerde deep dives

- [Broken Markdown repareren bij AI-vertaling: het versterken van een productie-pijplijn](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Aan de slag

Co-op Translator kan worden gebruikt vanaf de CLI, de Python API, of de MCP-server. Begin met de workflow-gids als je moet kiezen tussen lokale vertaling, automatisering, CI en agent/editor-integratie.

- [Kies je workflow](../../docs/workflows.md)
- [Configureer referenties](../../docs/configuration.md)
- [Vertaal vanaf de CLI](../../docs/cli.md)
- [Automatiseer met de Python API](../../docs/api.md)
- [Verbind met de MCP-server](../../docs/mcp.md)
- [Draaien in GitHub Actions](../../docs/github-actions.md)

Minimaal CLI-voorbeeld na configuratie:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

Voor eerste runs op grote repositories, gebruik `--dry-run` voordat je vertaalde bestanden schrijft. Zie de [CLI-referentie](../../docs/cli.md) voor contenttype-vlaggen, logs, review en linkmigratie.

Snelle container-run met Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Snelle container-run met PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Functies

- Geautomatiseerde vertaling voor Markdown, notebooks en afbeeldingen
- Houdt vertalingen in sync met bronwijzigingen
- Werkt lokaal (CLI) of in CI (GitHub Actions)
- Biedt Markdown-, notebook-, afbeelding-, review- en projectvertaalgereedschappen via MCP
- Gebruikt Azure OpenAI of OpenAI voor provider-ondersteunde vertaling
- Laat MCP agents hosten die Markdown- en notebook-chunks vertalen zonder Co-op Translator LLM-referenties
- Gebruikt Azure AI Vision voor extractie en vertaling van afbeeldingstekst
- Beoordeelt vertaalstructuur en actualiteit met deterministische controles
- Behoudt Markdown-opmaak en structuur

## Documentatie

- [Documentatiesite](https://azure.github.io/co-op-translator/)
- [Kies je workflow](../../docs/workflows.md)
- [Configuratie](../../docs/configuration.md)
- [Azure AI Setup](../../docs/azure-ai-setup.md)
- [CLI-referentie](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP-server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README-talen sjabloon](../../docs/readme-languages-template.md)
- [Ondersteunde talen](../../docs/supported-languages.md)
- [Bijdragen](../../CONTRIBUTING.md)
- [Probleemoplossing](../../docs/troubleshooting.md)

### Microsoft-specifieke gids
> [!NOTE]
> Alleen voor beheerders van de Microsoft “For Beginners” repositories.

- [De lijst “other courses” bijwerken (alleen voor MS Beginners-repositories)](../../docs/microsoft-beginners.md)

## Steun ons en bevorder wereldwijd leren

Doe met ons mee in het revolutioneren van de manier waarop educatieve inhoud wereldwijd wordt gedeeld! Geef [Co-op Translator](https://github.com/azure/co-op-translator) een ⭐ op GitHub en steun onze missie om taalbarrières in leren en technologie te doorbreken. Je interesse en bijdragen maken een groot verschil! Codebijdragen en functiesuggesties zijn altijd welkom.

### Ontdek Microsoft-educatieve inhoud in jouw taal
- [LangChain4j voor beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD voor beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI voor beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) voor beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents voor beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI voor beginners met .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI voor beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI voor beginners met Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML voor beginners](https://aka.ms/ml-beginners)
- [Data Science voor beginners](https://aka.ms/datascience-beginners)
- [AI voor beginners](https://aka.ms/ai-beginners)
- [Cybersecurity voor beginners](https://github.com/microsoft/Security-101)
- [Webontwikkeling voor beginners](https://aka.ms/webdev-beginners)
- [IoT voor beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video presentations

👉 Klik op de afbeelding hieronder om op YouTube te bekijken.

- **Open bij Microsoft**: Een korte introductie van 18 minuten en een snelle handleiding over hoe je Co-op Translator gebruikt.

  [![Open bij Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contributing

Dit project verwelkomt bijdragen en suggesties. Geïnteresseerd om bij te dragen aan Azure Co-op Translator? Zie onze [CONTRIBUTING.md](../../CONTRIBUTING.md) voor richtlijnen over hoe u kunt helpen Co-op Translator toegankelijker te maken.

## Contributors

[![bijdragers van co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

Dit project heeft de [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) aangenomen.
Voor meer informatie zie de [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) of
neem contact op met [opencode@microsoft.com](mailto:opencode@microsoft.com) voor eventuele aanvullende vragen of opmerkingen.

## Responsible AI

Microsoft zet zich in om onze klanten te helpen onze AI-producten op een verantwoorde manier te gebruiken, onze inzichten te delen en vertrouwensgebaseerde samenwerkingen op te bouwen via tools zoals Transparency Notes en Impact Assessments. Veel van deze bronnen zijn te vinden op [https://aka.ms/RAI](https://aka.ms/RAI).
De benadering van Microsoft ten aanzien van verantwoordelijke AI is gebaseerd op onze AI-principes van eerlijkheid, betrouwbaarheid en veiligheid, privacy en beveiliging, inclusiviteit, transparantie en verantwoordelijkheid.

Grote taal-, beeld- en spraakmodellen op grote schaal - zoals die in dit voorbeeld worden gebruikt - kunnen zich mogelijk op manieren gedragen die oneerlijk, onbetrouwbaar of aanstootgevend zijn, en daardoor schade veroorzaken. Raadpleeg de [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) om geïnformeerd te worden over risico's en beperkingen.

De aanbevolen aanpak om deze risico's te beperken is het opnemen van een veiligheidslaag in uw architectuur die schadelijk gedrag kan detecteren en voorkomen. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) biedt een onafhankelijke beschermingslaag die schadelijke door gebruikers gegenereerde en door AI gegenereerde inhoud in applicaties en services kan detecteren. Azure AI Content Safety bevat tekst- en beeld-API's waarmee u materiaal kunt detecteren dat schadelijk is. We hebben ook een interactieve Content Safety Studio waarmee u voorbeeldcode kunt bekijken, verkennen en uitproberen voor het detecteren van schadelijke inhoud in verschillende modaliteiten. De volgende [quickstart-documentatie](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) begeleidt u bij het maken van verzoeken naar de service.

Een ander aspect om rekening mee te houden is de algehele applicatieprestaties. Bij multimodale en multi-model applicaties beschouwen we prestaties als het systeem dat presteert zoals u en uw gebruikers verwachten, inclusief het niet genereren van schadelijke output. Het is belangrijk om de prestaties van uw gehele applicatie te beoordelen met behulp van [generatiekwaliteit- en risico- en veiligheidsstatistieken](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

U kunt uw AI-toepassing in uw ontwikkelomgeving evalueren met de [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Met een testdataset of een doel worden de generaties van uw generatieve AI-toepassing kwantitatief gemeten met ingebouwde evaluators of aangepaste evaluators naar keuze. Om aan de slag te gaan met de prompt flow SDK om uw systeem te evalueren, kunt u de [quickstartgids](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) volgen. Zodra u een evaluatieronde uitvoert, kunt u de resultaten [visualiseren in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Dit project kan handelsmerken of logo's bevatten van projecten, producten of services. Het geautoriseerde gebruik van Microsoft-handelsmerken of logo's is onderworpen aan en moet voldoen aan de [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Het gebruik van Microsoft-handelsmerken of logo's in gewijzigde versies van dit project mag geen verwarring veroorzaken of impliceren dat Microsoft sponsoring verleent.
Elk gebruik van handelsmerken of logo's van derden valt onder het beleid van die derden.

## Getting Help

Als u vastloopt of vragen heeft over het bouwen van AI-apps, doe mee aan:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Als u productfeedback heeft of fouten ondervindt tijdens het bouwen, bezoek:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)