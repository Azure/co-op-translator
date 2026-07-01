# Co-op Translator

_Easily automate and maintain translations for your educational GitHub content across multiple languages as your project evolves._

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

**Börja här:** [Välj ditt arbetsflöde](https://azure.github.io/co-op-translator/workflows/) | [Konfiguration](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Fler språkstöd

#### Stöds av [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabiska](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgariska](../bg/README.md) | [Burmesiska (Myanmar)](../my/README.md) | [Kinesiska (förenklad)](../zh-CN/README.md) | [Kinesiska (traditionell, Hongkong)](../zh-HK/README.md) | [Kinesiska (traditionell, Macao)](../zh-MO/README.md) | [Kinesiska (traditionell, Taiwan)](../zh-TW/README.md) | [Kroatiska](../hr/README.md) | [Tjeckiska](../cs/README.md) | [Danska](../da/README.md) | [Nederländska](../nl/README.md) | [Estniska](../et/README.md) | [Finska](../fi/README.md) | [Franska](../fr/README.md) | [Tyska](../de/README.md) | [Grekiska](../el/README.md) | [Hebreiska](../he/README.md) | [Hindi](../hi/README.md) | [Ungerska](../hu/README.md) | [Indonesiska](../id/README.md) | [Italienska](../it/README.md) | [Japanska](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Koreanska](../ko/README.md) | [Litauiska](../lt/README.md) | [Malajiska](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigeriansk pidgin](../pcm/README.md) | [Norska](../no/README.md) | [Persiska (Farsi)](../fa/README.md) | [Polska](../pl/README.md) | [Portugisiska (Brasilien)](../pt-BR/README.md) | [Portugisiska (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumänska](../ro/README.md) | [Ryska](../ru/README.md) | [Serbiska (kyrilliska)](../sr/README.md) | [Slovakiska](../sk/README.md) | [Slovenska](../sl/README.md) | [Spanska](../es/README.md) | [Swahili](../sw/README.md) | [Svenska](./README.md) | [Tagalog (filippinska)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailändska](../th/README.md) | [Turkiska](../tr/README.md) | [Ukrainska](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesiska](../vi/README.md)

> **Föredrar du att klona lokalt?**
>
> Detta arkiv innehåller 50+ språköversättningar som avsevärt ökar nedladdningsstorleken. För att klona utan översättningar, använd sparse checkout:
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
> Detta ger dig allt du behöver för att slutföra kursen med en mycket snabbare nedladdning.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Översikt

**Co-op Translator** hjälper dig att lokalisera ditt utbildningsinnehåll på GitHub till flera språk utan ansträngning.
När du uppdaterar dina Markdown-filer, bilder eller notebooks hålls översättningarna automatiskt synkroniserade, så att ditt innehåll förblir korrekt och uppdaterat för studerande över hela världen.

Använd det från CLI för att översätta hela repo, från Python API för automatisering, eller via MCP-servern för agent- och redigeringsarbetsflöden.

Exempel på hur översatt innehåll är organiserat:

![Example](../../imgs/translation-ex.png)

## Varför Co-op Translator?

Att översätta en fil är enkelt. Att hålla ett helt dokumentationsrepo
översatt, länkat och uppdaterat är den svåra delen.

| Problem | Hur Co-op Translator hjälper |
| --- | --- |
| Long docs are not one prompt | Stora Markdown-filer delas upp i bitar, så en lång README är inte beroende av ett enda sårbart modell-svar. Om en bit misslyckas kan Co-op Translator försöka igen och endast omfördela den del som misslyckades. |
| Incomplete translations should not be marked current | En avkortad översättning bör aldrig markeras som aktuell. Co-op Translator kontrollerar översättningens integritet innan den sparas och kan upptäcka strukturellt ofullständiga befintliga översättningar. |
| Links should match the translated repo structure | Manuella översättningar lämnar ofta relativa länkar som pekar tillbaka till källträdet. Co-op Translator omskriver länkar i Markdown, notebooks, bilder och README-filer för att matcha strukturen `translations/<lang>/...`. |
| Translation should work across an entire repo | Co-op Translator hanterar README-filer, dokumentation, notebooks och bildtexter som en del av ett enda repository-arbetsflöde, istället för att översätta filer en och en. |
| Maintaining translations matters more than creating them once | Källhashar och översättningsmetadata låter Co-op Translator hitta föråldrade filer, hoppa över oförändrade filer och hålla översatt innehåll synkroniserat när källrepon utvecklas. |

## Hur översättningsstatus hanteras

Co-op Translator hanterar översatt innehåll som **versionerade mjukvaruartifakter**,  
inte som statiska filer.

Verktyget spårar tillståndet för översatt Markdown, bilder och notebooks
med hjälp av **språkbegränsad metadata**.

Denna design gör att Co-op Translator kan:

- Upptäcka föråldrade översättningar på ett tillförlitligt sätt
- Behandla Markdown, bilder och notebooks konsekvent
- Skala säkert över stora, snabbföränderliga och flerspråkiga repo

Genom att modellera översättningar som hanterade artifakter,
passar översättningsarbetsflöden naturligt med moderna
mjukvarudependency- och artifact-hanteringsmetoder.

→ [Hur översättningsstatus hanteras](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Relaterade fördjupningar

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Kom igång

Co-op Translator kan användas från CLI, Python API eller MCP-servern. Börja med arbetsflödesguiden om du väljer mellan lokal översättning, automatisering, CI och agent-/redigerarintegration.

- [Välj ditt arbetsflöde](../../docs/workflows.md)
- [Konfigurera referenser](../../docs/configuration.md)
- [Översätt från CLI](../../docs/cli.md)
- [Automatisera med Python API](../../docs/api.md)
- [Anslut med MCP Server](../../docs/mcp.md)
- [Kör i GitHub Actions](../../docs/github-actions.md)

Minimalt CLI-exempel efter konfiguration:

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

För första körningar på stora repositories, använd `--dry-run` innan du skriver översatta filer. Se [CLI Reference](../../docs/cli.md) för flaggor för innehållstyper, loggar, granskning och länk-migrering.

Snabbkörning i container med Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Snabbkörning i container med PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Funktioner

- Automatiserad översättning för Markdown, notebooks och bilder
- Håller översättningar synkade med ändringar i källan
- Fungerar lokalt (CLI) eller i CI (GitHub Actions)
- Exponerar verktyg för Markdown-, notebook-, bild-, granskning- och projektöversättning genom MCP
- Använder Azure OpenAI eller OpenAI för leverantörsbackad översättning
- Låter MCP värdagentöversätta Markdown- och notebook-bitar utan Co-op Translator LLM-referenser
- Använder Azure AI Vision för att extrahera och översätta bildtext
- Granskar översättningens struktur och aktualitet med deterministiska kontroller
- Bevarar Markdown-formatering och struktur

## Dokumentation

- [Dokumentationssajt](https://azure.github.io/co-op-translator/)
- [Välj ditt arbetsflöde](../../docs/workflows.md)
- [Konfiguration](../../docs/configuration.md)
- [Azure AI-uppsättning](../../docs/azure-ai-setup.md)
- [CLI Reference](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README-språkmall](../../docs/readme-languages-template.md)
- [Stödda språk](../../docs/supported-languages.md)
- [Bidra](../../CONTRIBUTING.md)
- [Felsökning](../../docs/troubleshooting.md)

### Microsoft-specifik guide
> [!NOTE]
> Endast för underhållare av Microsofts “For Beginners”-arkiv.

- [Uppdatera listan "other courses" (endast för MS Beginners-repos)](../../docs/microsoft-beginners.md)

## Stöd oss och främja globalt lärande

Delta i att revolutionera hur utbildningsinnehåll delas globalt! Ge [Co-op Translator](https://github.com/azure/co-op-translator) en ⭐ på GitHub och stöd vårt uppdrag att bryta ned språkbarriärer inom lärande och teknik. Ditt intresse och dina bidrag gör stor skillnad! Kodbidrag och förslag på funktioner är alltid välkomna.

### Utforska Microsofts utbildningsinnehåll på ditt språk
- [LangChain4j-för-nybörjare](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD för nybörjare](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI för nybörjare](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) för nybörjare](https://github.com/microsoft/mcp-for-beginners)
- [AI-agenter för nybörjare](https://github.com/microsoft/ai-agents-for-beginners)
- [Generativ AI för nybörjare med .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generativ AI för nybörjare](https://github.com/microsoft/generative-ai-for-beginners)
- [Generativ AI för nybörjare med Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML för nybörjare](https://aka.ms/ml-beginners)
- [Data Science för nybörjare](https://aka.ms/datascience-beginners)
- [AI för nybörjare](https://aka.ms/ai-beginners)
- [Cybersäkerhet för nybörjare](https://github.com/microsoft/Security-101)
- [Webbutveckling för nybörjare](https://aka.ms/webdev-beginners)
- [IoT för nybörjare](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Videopresentationer

👉 Klicka på bilden nedan för att titta på YouTube.

- **Open på Microsoft**: En kort 18-minuters introduktion och snabbguide om hur man använder Co-op Translator.

  [![Open på Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Bidra

Detta projekt välkomnar bidrag och förslag. Är du intresserad av att bidra till Azure Co-op Translator? Se vår [CONTRIBUTING.md](../../CONTRIBUTING.md) för riktlinjer om hur du kan hjälpa till att göra Co-op Translator mer tillgänglig.

## Bidragsgivare

[![co-op-translator bidragsgivare](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Uppförandekod

Detta projekt har antagit [Microsofts uppförandekod för öppen källkod](https://opensource.microsoft.com/codeofconduct/).
För mer information se [Vanliga frågor om uppförandekoden](https://opensource.microsoft.com/codeofconduct/faq/) eller
kontakta [opencode@microsoft.com](mailto:opencode@microsoft.com) vid ytterligare frågor eller kommentarer.

## Ansvarsfull AI

Microsoft är engagerat i att hjälpa våra kunder att använda våra AI-produkter ansvarsfullt, dela med sig av våra lärdomar och bygga förtroendebaserade partnerskap genom verktyg som Transparency Notes och Impact Assessments. Många av dessa resurser finns på [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofts syn på ansvarsfull AI grundar sig i våra AI-principer om rättvisa, tillförlitlighet och säkerhet, integritet och skydd, inkludering, transparens och ansvar.

Storskaliga modeller för naturligt språk, bild och tal - som de som används i detta exempel - kan potentiellt uppträda på sätt som är orättvisa, opålitliga eller stötande, vilket i sin tur kan orsaka skada. Vänligen se [Azure OpenAI-tjänstens transparensanteckning](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) för att få information om risker och begränsningar.

Det rekommenderade tillvägagångssättet för att mildra dessa risker är att inkludera ett säkerhetssystem i din arkitektur som kan upptäcka och förhindra skadligt beteende. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) erbjuder ett oberoende skyddsskikt som kan upptäcka skadligt användargenererat och AI-genererat innehåll i applikationer och tjänster. Azure AI Content Safety inkluderar text- och bild-API:er som låter dig upptäcka material som är skadligt. Vi har också ett interaktivt Content Safety Studio som låter dig visa, utforska och prova exempel på kod för att upptäcka skadligt innehåll över olika modaliteter. Följande [snabbstartsdokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vägleder dig genom att göra anrop till tjänsten.

En annan aspekt att ta hänsyn till är den övergripande applikationsprestandan. Med multimodala och multimodellsapplikationer anser vi att prestanda innebär att systemet fungerar som du och dina användare förväntar er, inklusive att det inte genererar skadliga utdata. Det är viktigt att bedöma prestandan för din övergripande applikation med hjälp av [genereringskvalitet samt risk- och säkerhetsmått](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Du kan utvärdera din AI-applikation i din utvecklingsmiljö med hjälp av [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Med antingen en testdatamängd eller ett mål mäts dina generativa AI-genereringar kvantitativt med inbyggda utvärderare eller egna utvärderare du väljer. För att komma igång med prompt flow SDK för att utvärdera ditt system kan du följa [snabbstartsguiden](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). När du har kört en utvärderingsomgång kan du [visualisera resultaten i Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Varumärken

Detta projekt kan innehålla varumärken eller logotyper för projekt, produkter eller tjänster. Auktoriserad användning av Microsofts varumärken eller logotyper omfattas av och måste följa
[Microsofts riktlinjer för varumärken och varumärkesprofil](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Användning av Microsofts varumärken eller logotyper i modifierade versioner av detta projekt får inte orsaka förvirring eller antyda Microsofts sponsring.
All användning av tredjeparts varumärken eller logotyper omfattas av dessa tredjeparters policys.

## Få hjälp

Om du fastnar eller har frågor om att bygga AI-appar, gå med i:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Om du har produktfeedback eller stöter på fel under utveckling, besök:

[![Microsoft Foundry utvecklarforum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)