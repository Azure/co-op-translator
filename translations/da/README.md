<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T11:24:22+00:00",
  "source_file": "README.md",
  "language_code": "da"
}
-->
# Co-op Translator

_Automatiser nemt oversættelsen af dit uddannelsesindhold på GitHub til flere sprog for at nå et globalt publikum._

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
[Arabisk](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarsk](../bg/README.md) | [Burmesisk (Myanmar)](../my/README.md) | [Kinesisk (forenklet)](../zh/README.md) | [Kinesisk (traditionelt, Hong Kong)](../hk/README.md) | [Kinesisk (traditionelt, Macau)](../mo/README.md) | [Kinesisk (traditionelt, Taiwan)](../tw/README.md) | [Kroatisk](../hr/README.md) | [Tjekkisk](../cs/README.md) | [Dansk](./README.md) | [Hollandsk](../nl/README.md) | [Estisk](../et/README.md) | [Finsk](../fi/README.md) | [Fransk](../fr/README.md) | [Tysk](../de/README.md) | [Græsk](../el/README.md) | [Hebraisk](../he/README.md) | [Hindi](../hi/README.md) | [Ungarsk](../hu/README.md) | [Indonesisk](../id/README.md) | [Italiensk](../it/README.md) | [Japansk](../ja/README.md) | [Kannada](../kn/README.md) | [Koreansk](../ko/README.md) | [Litauisk](../lt/README.md) | [Malayisk](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalesisk](../ne/README.md) | [Nigeriansk Pidgin](../pcm/README.md) | [Norsk](../no/README.md) | [Persisk (Farsi)](../fa/README.md) | [Polsk](../pl/README.md) | [Portugisisk (Brasilien)](../br/README.md) | [Portugisisk (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumænsk](../ro/README.md) | [Russisk](../ru/README.md) | [Serbisk (kyrillisk)](../sr/README.md) | [Slovakisk](../sk/README.md) | [Slovensk](../sl/README.md) | [Spansk](../es/README.md) | [Swahili](../sw/README.md) | [Svensk](../sv/README.md) | [Tagalog (Filippinsk)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Tyrkisk](../tr/README.md) | [Ukrainsk](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesisk](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Oversigt

**Co-op Translator** hjælper dig med nemt at lokalisere dit uddannelsesindhold på GitHub til flere sprog. Når du opdaterer dine Markdown-filer, billeder eller notebooks, holdes oversættelserne automatisk synkroniserede, så dit indhold forbliver præcist og opdateret for lærende verden over.

Eksempel på, hvordan oversat indhold er organiseret:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.da.png)

## Kom godt i gang

```bash
# Opret og aktiver et virtuelt miljø (anbefalet)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installer pakken
pip install co-op-translator
# Oversæt
translate -l "ko ja fr" -md
```

Docker:

```bash
# Hent det offentlige billede fra GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Kør med den aktuelle mappe monteret og .env leveret (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimal opsætning

1. Opret en `.env`-fil ved hjælp af skabelonen: [.env.template](../../.env.template)
2. Konfigurer en LLM-udbyder (Azure OpenAI eller OpenAI)
3. (Valgfrit) For billedoversættelse (`-img`), konfigurer Azure AI Vision
4. (Anbefalet) Ryd op i tidligere oversættelser for at undgå konflikter (f.eks. `translations/`)
5. (Anbefalet) Tilføj en oversættelsessektion til din README ved hjælp af [README sprogskabelon](./getting_started/README_languages_template.md)
6. Se: [Opsæt Azure AI](./getting_started/set-up-azure-ai.md)

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
- Holder oversættelser synkroniserede med kildeforandringer
- Fungerer lokalt (CLI) eller i CI (GitHub Actions)
- Bruger Azure OpenAI eller OpenAI; valgfri Azure AI Vision til billeder
- Bevarer Markdown-format og struktur

## Dokumentation

- [Kommando-linje guide](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions guide (offentlige repositories & standard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions guide (Microsoft organisationsrepositories & org-niveau opsætninger)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README sprogskabelon](./getting_started/README_languages_template.md)
- [Understøttede sprog](./getting_started/supported-languages.md)
- [Bidrag](./CONTRIBUTING.md)
- [Fejlfinding](./getting_started/troubleshooting.md)

### Microsoft-specifik guide
> [!NOTE]
> Kun for vedligeholdere af Microsoft “For Beginners” repositories.

- [Opdatering af listen over “andre kurser” (kun for MS Beginners repositories)](./getting_started/update-other-courses.md)

## Støt os og frem læring globalt

Vær med til at revolutionere, hvordan uddannelsesindhold deles globalt! Giv [Co-op Translator](https://github.com/azure/co-op-translator) en ⭐ på GitHub og støt vores mission om at nedbryde sprogbarrierer inden for læring og teknologi. Din interesse og dine bidrag gør en stor forskel! Kodebidrag og forslag til funktioner er altid velkomne.

### Udforsk Microsofts uddannelsesindhold på dit sprog

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

## Video-præsentationer

👉 Klik på billedet nedenfor for at se på YouTube.

- **Open at Microsoft**: En kort 18-minutters introduktion og hurtig guide til, hvordan man bruger Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.da.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Bidrag

Dette projekt byder velkommen til bidrag og forslag. Er du interesseret i at bidrage til Azure Co-op Translator? Se venligst vores [CONTRIBUTING.md](./CONTRIBUTING.md) for retningslinjer om, hvordan du kan hjælpe med at gøre Co-op Translator mere tilgængelig.

## Bidragydere

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Adfærdskodeks

Dette projekt har vedtaget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For mere information se [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller
kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) med eventuelle yderligere spørgsmål eller kommentarer.

## Ansvarlig AI

Microsoft er engageret i at hjælpe vores kunder med at bruge vores AI-produkter ansvarligt, dele vores erfaringer og opbygge tillidsbaserede partnerskaber gennem værktøjer som Transparency Notes og Impact Assessments. Mange af disse ressourcer findes på [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofts tilgang til ansvarlig AI er baseret på vores AI-principper om retfærdighed, pålidelighed og sikkerhed, privatliv og sikkerhed, inklusivitet, gennemsigtighed og ansvarlighed.

Storskala modeller for naturligt sprog, billeder og tale – som dem, der bruges i dette eksempel – kan potentielt opføre sig på måder, der er uretfærdige, upålidelige eller stødende, hvilket kan forårsage skade. Se venligst [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) for at blive informeret om risici og begrænsninger.
Den anbefalede tilgang til at mindske disse risici er at inkludere et sikkerhedssystem i din arkitektur, som kan opdage og forhindre skadelig adfærd. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tilbyder et uafhængigt beskyttelseslag, der kan opdage skadeligt bruger- og AI-genereret indhold i applikationer og tjenester. Azure AI Content Safety inkluderer tekst- og billed-API'er, som gør det muligt at opdage skadeligt materiale. Vi har også et interaktivt Content Safety Studio, der giver dig mulighed for at se, udforske og prøve eksempelkode til at opdage skadeligt indhold på tværs af forskellige modaliteter. Følgende [quickstart-dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guider dig gennem, hvordan du laver forespørgsler til tjenesten.

En anden faktor, der skal tages i betragtning, er den samlede applikationsydelse. Med multimodale og multimodel-applikationer betragter vi ydelse som, at systemet fungerer som du og dine brugere forventer, herunder ikke at generere skadelige output. Det er vigtigt at vurdere ydelsen af din samlede applikation ved hjælp af [genereringskvalitet samt risik- og sikkerhedsmålinger](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Du kan evaluere din AI-applikation i dit udviklingsmiljø ved hjælp af [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Givet enten et testdatasæt eller et mål, bliver dine generative AI-applikationsgenereringer kvantitativt målt med indbyggede evaluatorer eller brugerdefinerede evaluatorer efter eget valg. For at komme i gang med prompt flow SDK til at evaluere dit system kan du følge [quickstart-guiden](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Når du har kørt en evaluering, kan du [visualisere resultaterne i Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Varemærker

Dette projekt kan indeholde varemærker eller logoer for projekter, produkter eller tjenester. Autoriseret brug af Microsofts varemærker eller logoer er underlagt og skal følge [Microsofts retningslinjer for varemærker og branding](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Brug af Microsofts varemærker eller logoer i modificerede versioner af dette projekt må ikke skabe forvirring eller antyde Microsoft-sponsorering. Enhver brug af tredjeparts varemærker eller logoer er underlagt disse tredjeparts politikker.

## Få hjælp

Hvis du sidder fast eller har spørgsmål om at bygge AI-apps, så deltag i:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Hvis du har produktfeedback eller oplever fejl under udvikling, besøg:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->