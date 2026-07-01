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

**Pradėkite čia:** [Pasirinkite savo darbo eigą](https://azure.github.io/co-op-translator/workflows/) | [Konfigūracija](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Daugiakalbis palaikymas

#### Palaiko [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](./README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Prefer to Clone Locally?**
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
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Apžvalga

**Co-op Translator** padeda jums lengvai lokalizuoti edukacinį GitHub turinį į kelias kalbas.
Kai atnaujinate savo Markdown failus, vaizdus ar užrašų bylas (notebook), vertimai automatiškai sinchronizuojami, užtikrindami, kad jūsų turinys būtų tikslus ir atnaujintas mokiniams visame pasaulyje.

Naudokite įrankį per CLI saugyklos vertimui, per Python API automatizacijai arba per MCP serverį agentų ir redaktorių darbo eigoms.

Example of how translated content is organized:

![Example](../../imgs/translation-ex.png)

## Kodėl Co-op Translator?

Vertimas vieno failo yra lengvas. Išsaugoti visą dokumentacijos saugyklą
išverstą, susietą ir atnaujintą yra sudėtinga.

| Problem | How Co-op Translator helps |
| --- | --- |
| Long docs are not one prompt | Large Markdown files are split into chunks, so a long README does not depend on one fragile model response. If a chunk fails, Co-op Translator can retry and re-chunk only the failed part. |
| Incomplete translations should not be marked current | A truncated translation should never be sealed as up to date. Co-op Translator checks translation integrity before saving and can detect structurally incomplete existing translations. |
| Links should match the translated repo structure | Manual translations often leave relative links pointing back to the source tree. Co-op Translator rewrites Markdown, notebook, image, and README links to match the `translations/<lang>/...` structure. |
| Translation should work across an entire repo | Co-op Translator handles README files, docs, notebooks, and image text as part of one repository workflow, instead of translating files one by one. |
| Maintaining translations matters more than creating them once | Source hashes and translation metadata let Co-op Translator find outdated files, skip unchanged files, and keep translated content synchronized as the source repo evolves. |

## Kaip valdoma vertimo būsena

Co-op Translator valdo išverstą turinį kaip **versijuotus programinės įrangos artefaktus**,  
o ne kaip statinius failus.

Įrankis seka išverstų Markdown, vaizdų ir užrašų failų būseną
naudodamas **kalbai pritaikytą metaduomenų** sistemą.

Toks dizainas leidžia Co-op Translator:

- Patikimai aptikti pasenusius vertimus
- Tvarkyti Markdown, vaizdus ir užrašus vienodai
- Saugiu būdu išplėsti veikimą didelėms, greitai kintančioms, daugakalbėms saugykloms

Modeliuodamas vertimus kaip valdomus artefaktus,
vertimo darbo eigos natūraliai dera su moderniomis
programinės įrangos priklausomybių ir artefaktų valdymo praktikomis.

→ [How translation state is managed](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Related deep dives

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Pradėkite

Co-op Translator galima naudoti per CLI, Python API arba MCP serverį. Pradėkite nuo darbo eigos vadovo, jei renkatės tarp lokalaus vertimo, automatizacijos, CI ar agento/redaktoriaus integracijos.

- [Choose your workflow](../../docs/workflows.md)
- [Configure credentials](../../docs/configuration.md)
- [Translate from the CLI](../../docs/cli.md)
- [Automate with the Python API](../../docs/api.md)
- [Connect with the MCP Server](../../docs/mcp.md)
- [Run in GitHub Actions](../../docs/github-actions.md)

Minimalus CLI pavyzdys po konfigūracijos:

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

Pirmiems paleidimams didelėse saugyklose, prieš rašant išverstus failus naudokite `--dry-run`. Daugiau apie turinio tipų parametruose, žurnalus, peržiūrą ir nuorodų migraciją žr. [CLI Reference](../../docs/cli.md).

Greitas konteinerio paleidimas su Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Greitas konteinerio paleidimas su PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Funkcijos

- Automatizuotas Markdown, užrašų ir vaizdų vertimas
- Išlaiko vertimus sinchronizuotus su šaltinio pakeitimais
- Veikia lokaliai (CLI) arba CI (GitHub Actions)
- Pateikia Markdown, užrašų, vaizdų, peržiūros ir projekto vertimo įrankius per MCP
- Naudoja Azure OpenAI arba OpenAI kaip vertimo tiekėją
- Leidžia MCP talpinti agentus, kad jie versti Markdown ir užrašų dalis be Co-op Translator LLM kredencialų
- Naudoja Azure AI Vision vaizdų teksto ištraukai ir vertimui
- Peržiūri vertimo struktūrą ir atnaujintumą deterministiniais patikrinimais
- Išlaiko Markdown formatavimą ir struktūrą

## Dokumentacija

- [Documentation site](https://azure.github.io/co-op-translator/)
- [Choose your workflow](../../docs/workflows.md)
- [Configuration](../../docs/configuration.md)
- [Azure AI Setup](../../docs/azure-ai-setup.md)
- [CLI Reference](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README languages template](../../docs/readme-languages-template.md)
- [Supported languages](../../docs/supported-languages.md)
- [Contributing](../../CONTRIBUTING.md)
- [Troubleshooting](../../docs/troubleshooting.md)

### Microsoft-specific guide
> [!NOTE]
> For maintainers of the Microsoft “For Beginners” repositories only.

- [Updating the “other courses” list (for MS Beginners repositories only)](../../docs/microsoft-beginners.md)

## Paremkite mus ir skatinkite pasaulinį mokymąsi

Prisijunkite prie mūsų revoliucijos, kaip edukacinis turinys dalijamas visame pasaulyje! Įvertinkite [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ GitHub ir palaikykite mūsų misiją pašalinti kalbų barjerus mokymesi ir technologijose. Jūsų susidomėjimas ir indėlis turi didelę įtaką! Kodo prisidėjimai ir funkcijų pasiūlymai visuomet laukiami.

### Atraskite Microsoft mokomąjį turinį savo kalba
- [LangChain4j pradedantiesiems](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD pradedantiesiems](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI pradedantiesiems](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) pradedantiesiems](https://github.com/microsoft/mcp-for-beginners)
- [AI agentai pradedantiesiems](https://github.com/microsoft/ai-agents-for-beginners)
- [Generatyvinė AI pradedantiesiems naudojant .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generatyvinė AI pradedantiesiems](https://github.com/microsoft/generative-ai-for-beginners)
- [Generatyvinė AI pradedantiesiems naudojant Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [Mašininis mokymasis pradedantiesiems](https://aka.ms/ml-beginners)
- [Duomenų mokslas pradedantiesiems](https://aka.ms/datascience-beginners)
- [Dirbtinis intelektas pradedantiesiems](https://aka.ms/ai-beginners)
- [Kibernetinis saugumas pradedantiesiems](https://github.com/microsoft/Security-101)
- [Tinklalapių kūrimas pradedantiesiems](https://aka.ms/webdev-beginners)
- [Daiktų internetas pradedantiesiems](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Vaizdo pristatymai

👉 Spustelėkite paveikslėlį žemiau, kad žiūrėtumėte YouTube.

- **Open at Microsoft**: Trumpas 18 minučių pristatymas ir greitas vadovas, kaip naudotis Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Prisidėjimas

Šis projektas kviečia prisidėti ir teikti pasiūlymus. Norite prisidėti prie Azure Co-op Translator? Peržiūrėkite mūsų [CONTRIBUTING.md](../../CONTRIBUTING.md) gaires, kaip galite padėti padaryti Co-op Translator prieinamesnį.

## Bendradarbiai

[![co-op-translator prisidėtojai](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Elgesio kodeksas

Šis projektas priėmė [Microsoft atvirojo kodo elgesio kodeksą](https://opensource.microsoft.com/codeofconduct/).
Daugiau informacijos rasite [Elgesio kodekso DUK](https://opensource.microsoft.com/codeofconduct/faq/) arba susisiekite su [opencode@microsoft.com](mailto:opencode@microsoft.com) dėl papildomų klausimų ar komentarų.

## Atsakingas DI

Microsoft įsipareigoja padėti savo klientams atsakingai naudoti mūsų DI produktus, dalintis įžvalgomis ir kurti abipusio pasitikėjimo partnerystes naudodama tokius įrankius kaip Transparency Notes ir Impact Assessments. Daug šių išteklių rasite adresu [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft požiūris į atsakingą DI remiasi mūsų DI principais: sąžiningumas, patikimumas ir saugumas, privatumas ir saugumas, įtrauktis, skaidrumas ir atsakingumas.

Didelio masto natūralios kalbos, vaizdų ir kalbos modeliai – tokie, kokie naudojami šiame pavyzdyje – gali elgtis netinkamai, nepatikimai arba įžeidžiamai, kas savo ruožtu gali sukelti žalą. Prašome susipažinti su [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), kad sužinotumėte apie rizikas ir apribojimus.

Rekomenduojamas rizikų mažinimo požiūris yra įtraukti saugumo sistemą į savo architektūrą, kuri galėtų aptikti ir užkirsti kelią žalingam elgesiui. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) suteikia nepriklausomą apsaugos sluoksnį, galintį aptikti žalingą vartotojų sukurtą ir DI sukurtą turinį programėlėse ir paslaugose. Azure AI Content Safety apima teksto ir vaizdų API, leidžiančias aptikti žalingą medžiagą. Taip pat turime interaktyvią Content Safety Studio, kurioje galite peržiūrėti, išbandyti ir išbandyti pavyzdinį kodą, skirtą aptikti žalingą turinį per įvairias modalumas. Šią [greito pradžios dokumentaciją](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) rasite instrukcijas, kaip siųsti užklausas į paslaugą.

Kitas svarbus aspektas – bendra programėlės našumas. Daugiamodalėse ir daugelių modelių programėlėse našumas reiškia, kad sistema veikia taip, kaip tikitės jūs ir jūsų vartotojai, įskaitant ir tai, kad ji negeneruotų žalingų rezultatų. Svarbu įvertinti bendrą programėlės našumą naudojant [generavimo kokybės ir rizikos bei saugumo metrikas](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Galite įvertinti savo DI programėlę kūrimo aplinkoje naudodami [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Turėdami testinį duomenų rinkinį arba tikslą, jūsų generatyvinės DI programėlės generacijos kiekybiškai įvertinamos naudojant įmontuotus arba pasirinktinius vertintojo įrankius. Norėdami pradėti naudoti prompt flow SDK savo sistemos vertinimui, sekite [greito pradžios vadovą](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Vykdę vertinimo paleidimą, galite [vizualizuoti rezultatus Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Prekės ženklai

Šis projektas gali turėti prekių ženklus arba logotipus, susijusius su projektais, produktais ar paslaugomis. Leidžiamas Microsoft prekių ženklų arba logotipų naudojimas turi atitikti ir vadovautis [Microsoft prekių ženklų ir prekės ženklo gairėmis](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Naudojimas Microsoft prekių ženklų ar logotipų pakeistose šio projekto versijose neturi sukelti painiavos ar nurodyti Microsoft rėmimą. Bet koks trečiųjų šalių prekių ženklų ar logotipų naudojimas yra priklausomas nuo tų trečiųjų šalių politikos.

## Pagalba

Jei užstrigote arba turite klausimų apie DI programėlių kūrimą, prisijunkite:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jei turite atsiliepimų apie produktą arba randate klaidų kūrimo metu, apsilankykite:

[![Microsoft Foundry kūrėjų forumas](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)