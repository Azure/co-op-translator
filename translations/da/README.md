# Co-op Translator

_Easily automate and maintain translations for your educational GitHub content across multiple languages as your project evolves._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python-pakke](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licens: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Kodeformat: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub-bidragsydere](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Start her:** [Vælg din arbejdsgang](https://azure.github.io/co-op-translator/workflows/) | [Konfiguration](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python-API](https://azure.github.io/co-op-translator/api/) | [MCP-server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Understøttelse af flere sprog

#### Understøttet af [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisk](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarsk](../bg/README.md) | [Burmesisk (Myanmar)](../my/README.md) | [Kinesisk (forenklet)](../zh-CN/README.md) | [Kinesisk (traditionelt, Hongkong)](../zh-HK/README.md) | [Kinesisk (traditionelt, Macau)](../zh-MO/README.md) | [Kinesisk (traditionelt, Taiwan)](../zh-TW/README.md) | [Kroatisk](../hr/README.md) | [Tjekkisk](../cs/README.md) | [Dansk](./README.md) | [Hollandsk](../nl/README.md) | [Estisk](../et/README.md) | [Finsk](../fi/README.md) | [Fransk](../fr/README.md) | [Tysk](../de/README.md) | [Græsk](../el/README.md) | [Hebraisk](../he/README.md) | [Hindi](../hi/README.md) | [Ungarsk](../hu/README.md) | [Indonesisk](../id/README.md) | [Italiensk](../it/README.md) | [Japansk](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Koreansk](../ko/README.md) | [Litauisk](../lt/README.md) | [Malayisk](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalesisk](../ne/README.md) | [Nigeriansk pidgin](../pcm/README.md) | [Norsk](../no/README.md) | [Persisk (Farsi)](../fa/README.md) | [Polsk](../pl/README.md) | [Portugisisk (Brasilien)](../pt-BR/README.md) | [Portugisisk (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumænsk](../ro/README.md) | [Russisk](../ru/README.md) | [Serbisk (kyrillisk)](../sr/README.md) | [Slovakisk](../sk/README.md) | [Slovensk](../sl/README.md) | [Spansk](../es/README.md) | [Swahili](../sw/README.md) | [Svensk](../sv/README.md) | [Tagalog (Filippinsk)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Tyrkisk](../tr/README.md) | [Ukrainsk](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesisk](../vi/README.md)

> **Foretrækker du at klone lokalt?**
>
> Dette repository indeholder over 50 sprogoversættelser, hvilket øger downloadstørrelsen betydeligt. For at klone uden oversættelser skal du bruge sparse checkout:
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
> Dette giver dig alt, hvad du behøver for at gennemføre kurset med en meget hurtigere download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Oversigt

**Co-op Translator** hjælper dig med at lokalisere dit uddannelsesindhold på GitHub til flere sprog uden besvær. Når du opdaterer dine Markdown-filer, billeder eller notesbøger, forbliver oversættelserne automatisk synkroniserede, så dit indhold forbliver korrekt og opdateret for lærende verden over.

Brug det fra CLI'en til repository-oversættelse, fra Python-API'en til automatisering, eller via MCP-serveren til agent- og redaktørarbejdsgange.

Eksempel på, hvordan oversat indhold er organiseret:

![Eksempel](../../imgs/translation-ex.png)

## Hvorfor Co-op Translator?

At oversætte én fil er nemt. At holde et helt dokumentationsrepository oversat, linket og opdateret er den svære del.

| Problem | Hvordan Co-op Translator hjælper |
| --- | --- |
| Lange dokumenter er ikke én prompt | Store Markdown-filer deles op i bidder, så en lang README ikke afhænger af ét skrøbeligt modelrespons. Hvis en bid fejler, kan Co-op Translator prøve igen og kun gen-opdele den fejlede del. |
| Ufuldstændige oversættelser bør ikke markeres som aktuelle | En afkortet oversættelse bør aldrig betragtes som opdateret. Co-op Translator tjekker oversættelsens integritet, før den gemmes, og kan opdage strukturelt ufuldstændige eksisterende oversættelser. |
| Links bør matche den oversatte repo-struktur | Manuelle oversættelser efterlader ofte relative links, der peger tilbage på kildetræet. Co-op Translator omskriver Markdown-, notebook-, billede- og README-links, så de matcher strukturen `translations/<lang>/...`. |
| Oversættelse bør fungere på et helt repo | Co-op Translator håndterer README-filer, dokumentation, notebooks og billedtekst som en del af én repository-arbejdsgang i stedet for at oversætte filer enkeltvis. |
| Vedligeholdelse af oversættelser er vigtigere end at lave dem kun én gang | Kildehashes og oversættelsesmetadata gør det muligt for Co-op Translator at finde forældede filer, springe uændrede filer over og holde oversat indhold synkroniseret, efterhånden som kilde-repoet udvikler sig. |

## Hvordan oversættelsesstatus håndteres

Co-op Translator styrer oversat indhold som **versionsstyrede softwareartefakter**,  
ikke som statiske filer.

Værktøjet sporer tilstanden for oversatte Markdown-filer, billeder og notebooks
ved hjælp af **sprogspecifik metadata**.

Dette design gør det muligt for Co-op Translator at:

- Pålideligt opdage forældede oversættelser
- Behandle Markdown, billeder og notebooks konsekvent
- Skalere sikkert på tværs af store, hurtigt bevægende, flersprogede repositories

Ved at modellere oversættelser som styrede artefakter,
tilpasser oversættelsesarbejdsgange sig naturligt til moderne
softwareafhængigheds- og artefaktstyringspraksisser.

→ [Hvordan oversættelsestilstand håndteres](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Relaterede dybdegående artikler

- [Ret afbrudt Markdown i AI-oversættelse: Hærdning af en produktionspipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Kom godt i gang

Co-op Translator kan bruges fra CLI'en, Python-API'en eller MCP-serveren. Start med arbejdsgangsvejledningen, hvis du vælger mellem lokal oversættelse, automatisering, CI og agent-/redaktørintegration.

- [Vælg din arbejdsgang](../../docs/workflows.md)
- [Konfigurer legitimationsoplysninger](../../docs/configuration.md)
- [Oversæt fra CLI'en](../../docs/cli.md)
- [Automatiser med Python-API'en](../../docs/api.md)
- [Forbind til MCP-serveren](../../docs/mcp.md)
- [Kør i GitHub Actions](../../docs/github-actions.md)

Minimalt CLI-eksempel efter konfiguration:

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

Ved første kørsel på store repositories skal du bruge `--dry-run` før du skriver oversatte filer. Se [CLI-reference](../../docs/cli.md) for indholdstyper, logs, gennemgang og linkmigration.

Hurtig kørsel i container med Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Hurtig kørsel i container med PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Funktioner

- Automatiseret oversættelse af Markdown, notebooks og billeder
- Holder oversættelser synkroniseret med kildeændringer
- Fungerer lokalt (CLI) eller i CI (GitHub Actions)
- Udstiller værktøjer til Markdown-, notebook-, billed-, gennemgangs- og projektoversættelse via MCP
- Bruger Azure OpenAI eller OpenAI til leverandørunderstøttet oversættelse
- Giver MCP mulighed for at lade agenter oversætte Markdown- og notebook-udsnit uden Co-op Translator LLM-legitimationsoplysninger
- Bruger Azure AI Vision til udtrækning af tekst fra billeder og oversættelse
- Gennemgår oversættelsesstruktur og friskhed med deterministiske kontroller
- Bevarer Markdown-formatering og struktur

## Dokumentation

- [Dokumentationsside](https://azure.github.io/co-op-translator/)
- [Vælg din arbejdsgang](../../docs/workflows.md)
- [Konfiguration](../../docs/configuration.md)
- [Azure AI-opsætning](../../docs/azure-ai-setup.md)
- [CLI-reference](../../docs/cli.md)
- [Python-API](../../docs/api.md)
- [MCP-server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README-sprogskabelon](../../docs/readme-languages-template.md)
- [Understøttede sprog](../../docs/supported-languages.md)
- [Bidrag](../../CONTRIBUTING.md)
- [Fejlfinding](../../docs/troubleshooting.md)

### Microsoft-specifik vejledning
> [!NOTE]
> Kun for vedligeholdere af Microsoft “For Beginners” repositories.

- [Opdatering af listen "other courses" (kun for MS Beginners-repositories)](../../docs/microsoft-beginners.md)

## Støt os og vær med til at fremme global læring

Vær med til at revolutionere, hvordan undervisningsindhold deles globalt! Giv [Co-op Translator](https://github.com/azure/co-op-translator) en ⭐ på GitHub og støt vores mission om at nedbryde sprogbarrierer inden for læring og teknologi. Din interesse og dine bidrag gør en stor forskel! Kodebidrag og forslag til funktioner er altid velkomne.

### Udforsk Microsofts undervisningsindhold på dit sprog
- [LangChain4j for begyndere](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for begyndere](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for begyndere](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) for begyndere](https://github.com/microsoft/mcp-for-beginners)
- [AI-agenter for begyndere](https://github.com/microsoft/ai-agents-for-beginners)
- [Generativ AI for begyndere ved brug af .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generativ AI for begyndere](https://github.com/microsoft/generative-ai-for-beginners)
- [Generativ AI for begyndere ved brug af Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for begyndere](https://aka.ms/ml-beginners)
- [Data Science for begyndere](https://aka.ms/datascience-beginners)
- [AI for begyndere](https://aka.ms/ai-beginners)
- [Cybersikkerhed for begyndere](https://github.com/microsoft/Security-101)
- [Webudvikling for begyndere](https://aka.ms/webdev-beginners)
- [IoT for begyndere](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Videopræsentationer

👉 Klik på billedet nedenfor for at se på YouTube.

- **Open hos Microsoft**: En kort 18-minutters introduktion og en hurtig guide til, hvordan man bruger Co-op Translator.

  [![Open hos Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Bidrag

Dette projekt byder velkommen til bidrag og forslag. Er du interesseret i at bidrage til Azure Co-op Translator? Se venligst vores [CONTRIBUTING.md](../../CONTRIBUTING.md) for retningslinjer om, hvordan du kan hjælpe med at gøre Co-op Translator mere tilgængelig.

## Bidragydere

[![co-op-translator bidragydere](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Adfærdskodeks

Dette projekt har vedtaget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For mere information se [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) med eventuelle yderligere spørgsmål eller kommentarer.

## Ansvarlig AI

Microsoft er forpligtet til at hjælpe vores kunder med at bruge vores AI-produkter ansvarligt, dele vores erfaringer og opbygge tillidsbaserede partnerskaber gennem værktøjer som Transparency Notes og Impact Assessments. Mange af disse ressourcer kan findes på [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofts tilgang til ansvarlig AI er forankret i vores AI-principper om retfærdighed, pålidelighed og sikkerhed, privatliv og sikkerhed, inklusivitet, gennemsigtighed og ansvarlighed.

Storskala sprog-, billede- og tale modeller - ligesom dem, der bruges i dette eksempel - kan potentielt opføre sig på måder, der er uretfærdige, upålidelige eller krænkende og dermed forårsage skader. Konsulter venligst [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) for at blive informeret om risici og begrænsninger.

Den anbefalede tilgang til at mindske disse risici er at inkludere et sikkerhedssystem i din arkitektur, som kan registrere og forhindre skadelig adfærd. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) leverer et uafhængigt beskyttelseslag, der kan opdage skadeligt brugergenereret og AI-genereret indhold i applikationer og tjenester. Azure AI Content Safety omfatter tekst- og billede-API'er, der gør det muligt at opdage skadeligt materiale. Vi har også et interaktivt Content Safety Studio, som giver dig mulighed for at se, udforske og prøve eksempelkode til at opdage skadeligt indhold på tværs af forskellige modaliteter. Følgende [quickstart-dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guider dig gennem, hvordan du foretager forespørgsler til tjenesten.

Et andet aspekt, der bør tages i betragtning, er den samlede applikations ydeevne. Med multimodale og multi-model applikationer betragter vi ydeevne som, at systemet opfører sig, som du og dine brugere forventer, inklusive ikke at generere skadelige output. Det er vigtigt at vurdere ydeevnen af din samlede applikation ved hjælp af [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Du kan evaluere din AI-applikation i dit udviklingsmiljø ved hjælp af [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Givet enten et testdatasæt eller et mål måles dine generative AI-genereringer kvantitativt med indbyggede evaluatorer eller brugerdefinerede evaluatorer efter eget valg. For at komme i gang med prompt flow SDK til at evaluere dit system kan du følge [quickstart-guiden](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Når du har kørt en evalueringskørsel, kan du [visualisere resultaterne i Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Varemærker

Dette projekt kan indeholde varemærker eller logoer for projekter, produkter eller tjenester. Autoriseret brug af Microsofts
varemærker eller logoer er betinget af og skal følge
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Brug af Microsofts varemærker eller logoer i ændrede versioner af dette projekt må ikke skabe forvirring eller antyde Microsofts sponsorat.
Enhver brug af tredjeparts varemærker eller logoer er underlagt disse tredjeparters politikker.

## Få hjælp

Hvis du kører fast eller har spørgsmål om at bygge AI-apps, så deltag:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Hvis du har produktfeedback eller oplever fejl under udvikling, besøg:

[![Microsoft Foundry Udviklerforum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)