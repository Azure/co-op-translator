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

**Start her:** [Velg arbeidsflyten](https://azure.github.io/co-op-translator/workflows/) | [Konfigurasjon](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Flerspråklig støtte

#### Støttet av [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisk](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarsk](../bg/README.md) | [Burmesisk (Myanmar)](../my/README.md) | [Kinesisk (forenklet)](../zh-CN/README.md) | [Kinesisk (tradisjonell, Hongkong)](../zh-HK/README.md) | [Kinesisk (tradisjonell, Macau)](../zh-MO/README.md) | [Kinesisk (tradisjonell, Taiwan)](../zh-TW/README.md) | [Kroatisk](../hr/README.md) | [Tsjekkisk](../cs/README.md) | [Dansk](../da/README.md) | [Nederlandsk](../nl/README.md) | [Estisk](../et/README.md) | [Finsk](../fi/README.md) | [Fransk](../fr/README.md) | [Tysk](../de/README.md) | [Gresk](../el/README.md) | [Hebraisk](../he/README.md) | [Hindi](../hi/README.md) | [Ungarsk](../hu/README.md) | [Indonesisk](../id/README.md) | [Italiensk](../it/README.md) | [Japansk](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Koreansk](../ko/README.md) | [Litauisk](../lt/README.md) | [Malaysisk](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigeriansk pidgin](../pcm/README.md) | [Norsk](./README.md) | [Persisk (Farsi)](../fa/README.md) | [Polsk](../pl/README.md) | [Portugisisk (Brasil)](../pt-BR/README.md) | [Portugisisk (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumensk](../ro/README.md) | [Russisk](../ru/README.md) | [Serbisk (kyrillisk)](../sr/README.md) | [Slovakisk](../sk/README.md) | [Slovensk](../sl/README.md) | [Spansk](../es/README.md) | [Swahili](../sw/README.md) | [Svensk](../sv/README.md) | [Tagalog (filippinsk)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Tyrkisk](../tr/README.md) | [Ukrainsk](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesisk](../vi/README.md)

> **Foretrekker du å klone lokalt?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
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
> This gives you everything you need to complete the course with a much faster download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Oversikt

**Co-op Translator** hjelper deg med å lokalisere ditt pedagogiske GitHub-innhold til flere språk uten store anstrengelser.
Når du oppdaterer Markdown-filer, bilder eller notebooks, holdes oversettelsene automatisk synkronisert, slik at innholdet forblir nøyaktig og oppdatert for elever over hele verden.

Bruk det fra CLI for repository-oversettelse, fra Python-APIet for automatisering, eller gjennom MCP-serveren for agent- og redaktørarbeidsflyter.

Eksempel på hvordan oversatt innhold er organisert:

![Eksempel](../../imgs/translation-ex.png)

## Hvorfor Co-op Translator?

Å oversette én fil er enkelt. Å holde et helt dokumentasjonsrepository
oversatt, lenket og oppdatert er den vanskelige delen.

| Problem | Hvordan Co-op Translator hjelper |
| --- | --- |
| Lange dokumenter er ikke én enkelt prompt | Store Markdown-filer deles opp i biter, så en lang README ikke er avhengig av ett sårbart modell-svar. Hvis en bit feiler, kan Co-op Translator prøve på nytt og re-chunke bare den feilede delen. |
| Ufullstendige oversettelser bør ikke markeres som oppdaterte | En avkortet oversettelse bør aldri låses som oppdatert. Co-op Translator sjekker oversettelsens integritet før lagring og kan oppdage strukturelt ufullstendige eksisterende oversettelser. |
| Lenker bør samsvare med den oversatte repo-strukturen | Manuelle oversettelser etterlater ofte relative lenker som peker tilbake til kildetreet. Co-op Translator omskriver Markdown-, notebook-, bilde- og README-lenker for å samsvare med strukturen `translations/<lang>/...`. |
| Oversettelse bør fungere på tvers av hele repoet | Co-op Translator håndterer README-filer, dokumentasjon, notebooks og bildetekst som en del av én repository-arbeidsflyt, i stedet for å oversette filer én og én. |
| Å vedlikeholde oversettelser er viktigere enn å lage dem én gang | Kilde-hasher og oversettelsesmetadata lar Co-op Translator finne utdaterte filer, hoppe over uendrede filer og holde oversatt innhold synkronisert etter hvert som kilde-repoet utvikler seg. |

## Hvordan oversettelsestilstanden håndteres

Co-op Translator håndterer oversatt innhold som **versjonerte programvareartefakter**,  
ikke som statiske filer.

Verktøyet sporer tilstanden til oversatt Markdown, bilder og notebooks
ved hjelp av **språkspesifikk metadata**.

Dette designet gjør det mulig for Co-op Translator å:

- Oppdage utdaterte oversettelser pålitelig
- Behandle Markdown, bilder og notebooks konsekvent
- Skalere trygt over store, raskt bevegende, flerspråklige repositories

Ved å modellere oversettelser som administrerte artefakter,
stemmer oversettelsesarbeidsflytene naturlig overens med moderne
praksiser for programvareavhengigheter og artefakthåndtering.

→ [How translation state is managed](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Relaterte dypdykk

- [Fikse ødelagt Markdown i AI-oversettelse: Herding av en produksjonspipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Kom i gang

Co-op Translator kan brukes fra CLI, Python-APIet eller MCP-serveren. Start med veiledningen for arbeidsflyt hvis du skal velge mellom lokal oversettelse, automatisering, CI og agent-/redaktørintegrasjon.

- [Velg arbeidsflyten](../../docs/workflows.md)
- [Konfigurer legitimasjon](../../docs/configuration.md)
- [Oversett fra CLI](../../docs/cli.md)
- [Automatiser med Python-APIet](../../docs/api.md)
- [Koble til MCP-serveren](../../docs/mcp.md)
- [Kjør i GitHub Actions](../../docs/github-actions.md)

Minimal CLI-eksempel etter konfigurasjon:

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

For første kjøringer på store repositoryer, bruk `--dry-run` før du skriver oversatte filer. Se [CLI-referanse](../../docs/cli.md) for flagg for innholdstyper, logger, gjennomgang og lenkemigrering.

Rask kjøring i container med Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Rask kjøring i container med PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Funksjoner

- Automatisk oversettelse av Markdown, notebooks og bilder
- Holder oversettelsene synkronisert med endringer i kilden
- Fungerer lokalt (CLI) eller i CI (GitHub Actions)
- Eksponerer verktøy for Markdown-, notebook-, bilde-, gjennomgangs- og prosjektoversettelse gjennom MCP
- Bruker Azure OpenAI eller OpenAI for leverandørstøttet oversettelse
- Lar MCP være vert for agenter som oversetter Markdown- og notebook-biter uten Co-op Translator LLM-legitimasjon
- Bruker Azure AI Vision for utvinning og oversettelse av bildetekst
- Gjennomgår oversettelsens struktur og friskhet med deterministiske kontroller
- Bevarer Markdown-formatering og struktur

## Dokumentasjon

- [Dokumentasjonsnettstedet](https://azure.github.io/co-op-translator/)
- [Velg arbeidsflyten](../../docs/workflows.md)
- [Konfigurasjon](../../docs/configuration.md)
- [Azure AI-oppsett](../../docs/azure-ai-setup.md)
- [CLI-referanse](../../docs/cli.md)
- [Python-API](../../docs/api.md)
- [MCP-serveren](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README-språkmal](../../docs/readme-languages-template.md)
- [Støttede språk](../../docs/supported-languages.md)
- [Bidra](../../CONTRIBUTING.md)
- [Feilsøking](../../docs/troubleshooting.md)

### Microsoft-spesifikk veiledning
> [!NOTE]
> Kun for vedlikeholdere av Microsoft «For Beginners»-repoene.

- [Oppdatere listen «andre kurs» (kun for MS Beginners-repoer)](../../docs/microsoft-beginners.md)

## Støtt oss og fremme global læring

Bli med oss i å revolusjonere hvordan pedagogisk innhold deles globalt! Gi [Co-op Translator](https://github.com/azure/co-op-translator) en ⭐ på GitHub og støtt vårt oppdrag om å bryte ned språkbarrierer i læring og teknologi. Din interesse og dine bidrag har stor betydning! Kodebidrag og forslag til funksjoner er alltid velkomne.

### Utforsk Microsofts opplæringsinnhold på ditt språk
- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
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

## Videopresentasjoner

👉 Klikk på bildet nedenfor for å se på YouTube.

- **Åpne hos Microsoft**: En kort 18-minutters introduksjon og en rask guide til hvordan du bruker Co-op Translator.

  [![Åpne hos Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Bidra

Dette prosjektet tar imot bidrag og forslag. Er du interessert i å bidra til Azure Co-op Translator? Se vår [CONTRIBUTING.md](../../CONTRIBUTING.md) for retningslinjer om hvordan du kan bidra til å gjøre Co-op Translator mer tilgjengelig.

## Bidragsytere

[![co-op-translator bidragsytere](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Atferdskodeks

Dette prosjektet har vedtatt den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For mer informasjon, se [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) ved eventuelle ytterligere spørsmål eller kommentarer.

## Ansvarlig AI

Microsoft er forpliktet til å hjelpe kundene våre med å bruke AI-produktene våre ansvarlig, dele våre erfaringer, og bygge tillitsbaserte partnerskap gjennom verktøy som Transparency Notes og Impact Assessments. Mange av disse ressursene kan finnes på [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofts tilnærming til ansvarlig AI er forankret i våre AI-prinsipper om rettferdighet, pålitelighet og sikkerhet, personvern og sikkerhet, inkludering, åpenhet og ansvarlighet.

Storskala modeller for naturlig språk, bilder og tale — som de som brukes i dette eksempelet — kan potensielt oppføre seg på måter som er urettferdige, upålitelige eller støtende, og dermed forårsake skade. Se [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) for å få informasjon om risikoer og begrensninger.

Den anbefalte tilnærmingen for å redusere disse risikoene er å inkludere et sikkerhetssystem i arkitekturen din som kan oppdage og forhindre skadelig atferd. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) gir et uavhengig beskyttelseslag som kan oppdage skadelig brukergenerert og AI-generert innhold i applikasjoner og tjenester. Azure AI Content Safety inkluderer tekst- og bilde-APIer som lar deg oppdage materiale som er skadelig. Vi har også et interaktivt Content Safety Studio som lar deg vise, utforske og prøve ut eksempelkode for å oppdage skadelig innhold på tvers av ulike modaliteter. Den følgende [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) veileder deg gjennom hvordan du gjør forespørsler til tjenesten.

Et annet aspekt å ta i betraktning er den samlede applikasjonsytelsen. For multimodale og multimodellsapplikasjoner anser vi ytelse som at systemet oppfører seg slik du og brukerne dine forventer, inkludert at det ikke genererer skadelig innhold. Det er viktig å vurdere ytelsen til hele applikasjonen din ved å bruke [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Du kan evaluere AI-applikasjonen din i utviklingsmiljøet ved å bruke [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Enten du har et testdatasett eller et mål, blir generasjonene fra generativ AI-applikasjonen din kvantitativt målt med innebygde evaluatorer eller egne evaluatorer etter eget valg. For å komme i gang med prompt flow sdk for å evaluere systemet ditt, kan du følge [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Når du har kjørt en evalueringskjøring, kan du [visualize the results in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Varemerker

Dette prosjektet kan inneholde varemerker eller logoer for prosjekter, produkter eller tjenester. Autorisert bruk av Microsofts varemerker eller logoer er underlagt og må følge [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Bruk av Microsofts varemerker eller logoer i endrede versjoner av dette prosjektet må ikke skape forvirring eller antyde Microsoft-sponsorering.
Enhver bruk av tredjeparts varemerker eller logoer er underlagt disse tredjepartenes retningslinjer.

## Få hjelp

Hvis du står fast eller har spørsmål om å bygge AI-apper, bli med:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Hvis du har produkttilbakemeldinger eller opplever feil mens du bygger, besøk:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)