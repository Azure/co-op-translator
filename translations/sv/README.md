<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:18:42+00:00",
  "source_file": "README.md",
  "language_code": "sv"
}
-->
# Co-op Translator

_Automatisera enkelt översättningen av ditt utbildningsinnehåll på GitHub till flera språk för att nå en global publik._

### 🌐 Stöd för flera språk

#### Stöds av [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabiska](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgariska](../bg/README.md) | [Burmesiska (Myanmar)](../my/README.md) | [Kinesiska (Förenklad)](../zh/README.md) | [Kinesiska (Traditionell, Hong Kong)](../hk/README.md) | [Kinesiska (Traditionell, Macao)](../mo/README.md) | [Kinesiska (Traditionell, Taiwan)](../tw/README.md) | [Kroatiska](../hr/README.md) | [Tjeckiska](../cs/README.md) | [Danska](../da/README.md) | [Nederländska](../nl/README.md) | [Estniska](../et/README.md) | [Finska](../fi/README.md) | [Franska](../fr/README.md) | [Tyska](../de/README.md) | [Grekiska](../el/README.md) | [Hebreiska](../he/README.md) | [Hindi](../hi/README.md) | [Ungerska](../hu/README.md) | [Indonesiska](../id/README.md) | [Italienska](../it/README.md) | [Japanska](../ja/README.md) | [Koreanska](../ko/README.md) | [Litauiska](../lt/README.md) | [Malajiska](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norska](../no/README.md) | [Persiska (Farsi)](../fa/README.md) | [Polska](../pl/README.md) | [Portugisiska (Brasilien)](../br/README.md) | [Portugisiska (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumänska](../ro/README.md) | [Ryska](../ru/README.md) | [Serbiska (Kyrilliska)](../sr/README.md) | [Slovakiska](../sk/README.md) | [Slovenska](../sl/README.md) | [Spanska](../es/README.md) | [Swahili](../sw/README.md) | [Svenska](./README.md) | [Tagalog (Filippinska)](../tl/README.md) | [Tamil](../ta/README.md) | [Thailändska](../th/README.md) | [Turkiska](../tr/README.md) | [Ukrainska](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesiska](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Översikt

**Co-op Translator** gör det möjligt för dig att snabbt översätta ditt utbildningsinnehåll på GitHub till flera språk, så att du enkelt kan nå en global publik. När du uppdaterar dina Markdown-filer, bilder eller Jupyter-notebooks synkroniseras översättningarna automatiskt för att säkerställa att ditt utbildningsinnehåll på GitHub alltid är aktuellt och relevant för internationella användare.

Se hur Co-op Translator organiserar översatt utbildningsinnehåll på GitHub:

![Exempel](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.sv.png)

## Snabbstart

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

## Minimal installation

- Skapa en `.env` med hjälp av mallen: [.env.template](../../.env.template)
- Konfigurera en LLM-leverantör (Azure OpenAI eller OpenAI)
- För bildöversättning (`-img`), konfigurera även Azure AI Vision
- Rekommenderat: Om du har översättningar som skapats av andra verktyg, rensa bort dem först för att undvika konflikter (till exempel: `translations/`).
- Rekommenderat: Lägg till en översättningssektion i din README med hjälp av [README languages template](./README_languages_template.md)
- Se: [Konfigurera Azure AI](./getting_started/set-up-azure-ai.md)

## Användning

Översätt alla stödda typer:

```bash
translate -l "ko ja"
```

Endast Markdown:

```bash
translate -l "de" -md
```

Markdown + bilder:

```bash
translate -l "pt" -md -img
```

Endast notebooks:

```bash
translate -l "zh" -nb
```

Fler flaggor: [Kommandoreferens](./getting_started/command-reference.md)

## Funktioner

- Automatisk översättning av Markdown, notebooks och bilder
- Håller översättningar synkroniserade med källändringar
- Fungerar lokalt (CLI) eller i CI (GitHub Actions)
- Använder Azure OpenAI eller OpenAI; valfritt Azure AI Vision för bilder
- Bevarar Markdown-format och struktur

## Dokumentation

- [Kommandoradsguide](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions-guide (Publika repos & standardhemligheter)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions-guide (Microsoft-organisationens repos & org-nivåinställningar)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Stödda språk](./getting_started/supported-languages.md)
- [Felsökning](./getting_started/troubleshooting.md)

## Stöd oss och främja globalt lärande

Var med och förändra hur utbildningsinnehåll delas globalt! Ge [Co-op Translator](https://github.com/azure/co-op-translator) en ⭐ på GitHub och stöd vårt uppdrag att riva språkbarriärer inom lärande och teknik. Ditt intresse och dina bidrag gör stor skillnad! Kodbidrag och förslag på nya funktioner är alltid välkomna.

### Utforska Microsofts utbildningsinnehåll på ditt språk

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

## Videopresentationer

Lär dig mer om Co-op Translator genom våra presentationer _(Klicka på bilden nedan för att se på YouTube.)_:

- **Open at Microsoft**: En kort 18-minuters introduktion och snabbguide om hur du använder Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.sv.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Bidra

Detta projekt välkomnar bidrag och förslag. Är du intresserad av att bidra till Azure Co-op Translator? Läs vår [CONTRIBUTING.md](./CONTRIBUTING.md) för riktlinjer om hur du kan hjälpa till att göra Co-op Translator mer tillgänglig.

## Bidragsgivare

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Uppförandekod

Detta projekt har antagit [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
För mer information, se [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller
kontakta [opencode@microsoft.com](mailto:opencode@microsoft.com) om du har ytterligare frågor eller kommentarer.

## Ansvarsfull AI

Microsoft är engagerade i att hjälpa våra kunder att använda våra AI-produkter ansvarsfullt, dela våra lärdomar och bygga förtroendebaserade partnerskap genom verktyg som Transparency Notes och Impact Assessments. Många av dessa resurser finns på [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofts syn på ansvarsfull AI grundar sig i våra AI-principer: rättvisa, tillförlitlighet och säkerhet, integritet och säkerhet, inkludering, transparens och ansvarstagande.

Storskaliga språk-, bild- och talmodeller – som de som används i detta exempel – kan ibland bete sig på sätt som är orättvisa, opålitliga eller stötande, vilket kan orsaka skada. Läs gärna [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) för att bli informerad om risker och begränsningar.

Det rekommenderade sättet att minska dessa risker är att inkludera ett säkerhetssystem i din arkitektur som kan upptäcka och förhindra skadligt beteende. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ger ett oberoende skyddslager som kan upptäcka skadligt användargenererat och AI-genererat innehåll i applikationer och tjänster. Azure AI Content Safety inkluderar text- och bild-API:er som låter dig upptäcka skadligt material. Vi har också ett interaktivt Content Safety Studio där du kan se, utforska och testa exempel på kod för att upptäcka skadligt innehåll i olika format. Följande [snabbstartsdokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guidar dig genom hur du gör förfrågningar till tjänsten.
En annan aspekt att ta hänsyn till är applikationens övergripande prestanda. Med multimodala och multi-modellapplikationer menar vi med prestanda att systemet fungerar som du och dina användare förväntar sig, inklusive att det inte genererar skadliga resultat. Det är viktigt att utvärdera prestandan för hela din applikation med hjälp av [genereringskvalitet samt risk- och säkerhetsmått](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Du kan utvärdera din AI-applikation i din utvecklingsmiljö med hjälp av [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Med antingen en testdatamängd eller ett mål mäts dina generativa AI-applikationers resultat kvantitativt med inbyggda eller egna utvärderingsverktyg som du väljer. För att komma igång med prompt flow sdk för att utvärdera ditt system kan du följa [snabbstartsguiden](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). När du har kört en utvärdering kan du [visualisera resultaten i Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Varumärken

Detta projekt kan innehålla varumärken eller logotyper för projekt, produkter eller tjänster. Auktoriserad användning av Microsofts
varumärken eller logotyper omfattas av och måste följa
[Microsofts riktlinjer för varumärken och varumärkesanvändning](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Användning av Microsofts varumärken eller logotyper i modifierade versioner av detta projekt får inte orsaka förväxling eller antyda att Microsoft står bakom projektet.
All användning av tredje parts varumärken eller logotyper omfattas av dessa tredje parters policyer.

## Få hjälp

Om du kör fast eller har frågor om att bygga AI-appar, gå med i:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Om du har feedback på produkten eller stöter på fel under utvecklingen, besök:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.