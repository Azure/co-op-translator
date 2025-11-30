<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:21:05+00:00",
  "source_file": "README.md",
  "language_code": "da"
}
-->
# Co-op Translator

_Automatisk oversætning af dit uddannelsesindhold på GitHub til flere sprog, så du kan nå ud til et globalt publikum._

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

### 🌐 Understøttelse af flere sprog

#### Understøttet af [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisk](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarsk](../bg/README.md) | [Burmesisk (Myanmar)](../my/README.md) | [Kinesisk (forenklet)](../zh/README.md) | [Kinesisk (traditionelt, Hong Kong)](../hk/README.md) | [Kinesisk (traditionelt, Macau)](../mo/README.md) | [Kinesisk (traditionelt, Taiwan)](../tw/README.md) | [Kroatisk](../hr/README.md) | [Tjekkisk](../cs/README.md) | [Dansk](./README.md) | [Hollandsk](../nl/README.md) | [Estisk](../et/README.md) | [Finsk](../fi/README.md) | [Fransk](../fr/README.md) | [Tysk](../de/README.md) | [Græsk](../el/README.md) | [Hebraisk](../he/README.md) | [Hindi](../hi/README.md) | [Ungarsk](../hu/README.md) | [Indonesisk](../id/README.md) | [Italiensk](../it/README.md) | [Japansk](../ja/README.md) | [Koreansk](../ko/README.md) | [Litauisk](../lt/README.md) | [Malaysisk](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norsk](../no/README.md) | [Persisk (Farsi)](../fa/README.md) | [Polsk](../pl/README.md) | [Portugisisk (Brasilien)](../br/README.md) | [Portugisisk (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumænsk](../ro/README.md) | [Russisk](../ru/README.md) | [Serbisk (kyrillisk)](../sr/README.md) | [Slovakisk](../sk/README.md) | [Slovensk](../sl/README.md) | [Spansk](../es/README.md) | [Swahili](../sw/README.md) | [Svensk](../sv/README.md) | [Tagalog (Filippinsk)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Tyrkisk](../tr/README.md) | [Ukrainsk](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesisk](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Overblik

**Co-op Translator** gør det nemt og hurtigt at oversætte dit uddannelsesindhold på GitHub til flere sprog, så du uden besvær kan nå ud til et globalt publikum. Når du opdaterer dine Markdown-filer, billeder eller Jupyter-notebooks, bliver oversættelserne automatisk synkroniseret, så dit indhold altid er opdateret og relevant for internationale brugere.

Se hvordan Co-op Translator organiserer oversat uddannelsesindhold på GitHub:

![Eksempel](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.da.png)

## Kom hurtigt i gang

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

## Minimal opsætning

- Opret en `.env` ud fra skabelonen: [.env.template](../../.env.template)
- Konfigurer én LLM-udbyder (Azure OpenAI eller OpenAI)
- For billedoversættelse (`-img`), skal du også sætte Azure AI Vision op
- Anbefalet: Hvis du har oversættelser genereret af andre værktøjer, så ryd op i dem først for at undgå konflikter (for eksempel: `translations/`).
- Anbefalet: Tilføj et oversættelsesafsnit til din README ved hjælp af [README-sprogskabelonen](./README_languages_template.md)
- Se: [Opsæt Azure AI](./getting_started/set-up-azure-ai.md)

## Brug

Oversæt alle understøttede typer:

```bash
translate -l "ko ja"
```

Kun Markdown:

```bash
translate -l "de" -md
```

Markdown + billeder:

```bash
translate -l "pt" -md -img
```

Kun notebooks:

```bash
translate -l "zh" -nb
```

Flere flag: [Kommando-reference](./getting_started/command-reference.md)

## Funktioner

- Automatisk oversættelse af Markdown, notebooks og billeder
- Holder oversættelser synkroniseret med kildeændringer
- Kan bruges lokalt (CLI) eller i CI (GitHub Actions)
- Understøtter Azure OpenAI eller OpenAI; valgfrit Azure AI Vision til billeder
- Bevarer Markdown-formatering og struktur

## Dokumentation

- [Kommando-linje guide](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions guide (offentlige repositories & standard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions guide (Microsoft organisation repositories & org-niveau opsætninger)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Understøttede sprog](./getting_started/supported-languages.md)
- [Fejlfinding](./getting_started/troubleshooting.md)

## Støt os og frem global læring

Vær med til at revolutionere måden uddannelsesindhold deles på globalt! Giv [Co-op Translator](https://github.com/azure/co-op-translator) en ⭐ på GitHub og støt vores mission om at nedbryde sprogbarrierer i læring og teknologi. Din interesse og dine bidrag gør en stor forskel! Kodebidrag og forslag til nye funktioner er altid velkomne.

### Udforsk Microsofts uddannelsesindhold på dit sprog

- [AZD for begyndere](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for begyndere](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For begyndere](https://github.com/microsoft/mcp-for-beginners)
- [AI-agenter for begyndere](https://github.com/microsoft/ai-agents-for-beginners)
- [Generativ AI for begyndere med .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generativ AI for begyndere](https://github.com/microsoft/generative-ai-for-beginners)
- [Generativ AI for begyndere med Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for begyndere](https://aka.ms/ml-beginners)
- [Data Science for begyndere](https://aka.ms/datascience-beginners)
- [AI for begyndere](https://aka.ms/ai-beginners)
- [Cybersecurity for begyndere](https://github.com/microsoft/Security-101)
- [Webudvikling for begyndere](https://aka.ms/webdev-beginners)
- [IoT for begyndere](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video-præsentationer

Lær mere om Co-op Translator gennem vores præsentationer _(Klik på billedet herunder for at se på YouTube.)_:

- **Open at Microsoft**: En kort 18-minutters introduktion og hurtig guide til brug af Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.da.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Bidrag

Dette projekt byder bidrag og forslag velkommen. Vil du bidrage til Azure Co-op Translator? Se venligst vores [CONTRIBUTING.md](./CONTRIBUTING.md) for retningslinjer om, hvordan du kan hjælpe med at gøre Co-op Translator mere tilgængelig.

## Bidragydere

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Adfærdskodeks

Dette projekt har vedtaget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For mere information, se [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller
kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) hvis du har yderligere spørgsmål eller kommentarer.

## Ansvarlig AI

Microsoft er engageret i at hjælpe vores kunder med at bruge vores AI-produkter ansvarligt, dele vores erfaringer og opbygge tillidsbaserede partnerskaber gennem værktøjer som Transparency Notes og Impact Assessments. Mange af disse ressourcer findes på [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofts tilgang til ansvarlig AI bygger på vores AI-principper om retfærdighed, pålidelighed og sikkerhed, privatliv og sikkerhed, inklusion, gennemsigtighed og ansvarlighed.

Store sprog-, billed- og tale-modeller – som dem, der bruges i dette eksempel – kan potentielt opføre sig på måder, der er uretfærdige, upålidelige eller stødende, hvilket kan forårsage skade. Læs venligst [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) for at blive informeret om risici og begrænsninger.

Den anbefalede måde at mindske disse risici på er at inkludere et sikkerhedssystem i din arkitektur, der kan opdage og forhindre skadelig adfærd. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) giver et uafhængigt beskyttelseslag, der kan opdage skadeligt bruger- og AI-genereret indhold i applikationer og tjenester. Azure AI Content Safety indeholder tekst- og billed-API'er, der gør det muligt at opdage skadeligt materiale. Vi har også et interaktivt Content Safety Studio, hvor du kan se, udforske og prøve eksempler på kode til at opdage skadeligt indhold på tværs af forskellige modaliteter. Følgende [quickstart-dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guider dig igennem, hvordan du laver forespørgsler til tjenesten.
En anden vigtig faktor at tage højde for er den overordnede applikationsydelse. Med multimodale og multi-model applikationer betyder ydeevne, at systemet fungerer, som du og dine brugere forventer, herunder at det ikke genererer skadelige output. Det er vigtigt at vurdere ydeevnen for din samlede applikation ved hjælp af [genereringskvalitet samt risikometrikker og sikkerhedsmetrikker](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Du kan evaluere din AI-applikation i dit udviklingsmiljø ved hjælp af [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Med enten et testdatasæt eller et mål bliver dine generative AI-applikationsresultater målt kvantitativt med indbyggede eller brugerdefinerede evaluatorer efter eget valg. For at komme i gang med prompt flow sdk til at evaluere dit system, kan du følge [quickstart-guiden](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Når du har udført en evalueringskørsel, kan du [visualisere resultaterne i Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Varemærker

Dette projekt kan indeholde varemærker eller logoer for projekter, produkter eller tjenester. Autoriseret brug af Microsofts
varemærker eller logoer er underlagt og skal følge
[Microsofts retningslinjer for varemærker og branding](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Brug af Microsofts varemærker eller logoer i ændrede versioner af dette projekt må ikke skabe forvirring eller antyde, at Microsoft står bag.
Al brug af tredjeparts varemærker eller logoer er underlagt de pågældende tredjeparts politikker.

## Få hjælp

Hvis du går i stå eller har spørgsmål om at bygge AI-apps, så deltag i:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Hvis du har feedback til produktet eller oplever fejl under udvikling, så besøg:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.