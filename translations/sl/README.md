<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T04:08:34+00:00",
  "source_file": "README.md",
  "language_code": "sl"
}
-->
# Co-op Translator

_Preprosto avtomatizirajte prevajanje svoje izobraževalne vsebine na GitHubu v več jezikov in dosezite globalno občinstvo._

### 🌐 Večjezična podpora

#### Podprto s strani [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](./README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Pregled

**Co-op Translator** vam omogoča hitro prevajanje izobraževalne vsebine na GitHubu v več jezikov, tako da brez truda dosežete globalno občinstvo. Ko posodobite svoje Markdown datoteke, slike ali Jupyter zvezke, se prevodi samodejno sinhronizirajo, da je vaša izobraževalna vsebina na GitHubu vedno sveža in relevantna za mednarodne uporabnike.

Poglejte, kako Co-op Translator organizira prevedeno izobraževalno vsebino na GitHubu:

![Primer](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.sl.png)

## Hitri začetek

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

## Minimalna nastavitev

- Ustvarite `.env` po predlogi: [.env.template](../../.env.template)
- Nastavite enega ponudnika LLM (Azure OpenAI ali OpenAI)
- Za prevajanje slik (`-img`) nastavite tudi Azure AI Vision
- Priporočilo: Če imate prevode, ustvarjene z drugimi orodji, jih najprej počistite, da se izognete konfliktom (na primer: `translations/`).
- Priporočilo: Dodajte razdelek s prevodi v svoj README z uporabo [predloge za jezike README](./README_languages_template.md)
- Glejte: [Nastavitev Azure AI](./getting_started/set-up-azure-ai.md)

## Uporaba

Prevedite vse podprte tipe:

```bash
translate -l "ko ja"
```

Samo Markdown:

```bash
translate -l "de" -md
```

Markdown + slike:

```bash
translate -l "pt" -md -img
```

Samo zvezki:

```bash
translate -l "zh" -nb
```

Več možnosti: [Referenca ukazov](./getting_started/command-reference.md)

## Značilnosti

- Samodejno prevajanje za Markdown, zvezke in slike
- Ohranja prevode usklajene s spremembami izvorne vsebine
- Deluje lokalno (CLI) ali v CI (GitHub Actions)
- Uporablja Azure OpenAI ali OpenAI; opcijsko Azure AI Vision za slike
- Ohranja oblikovanje in strukturo Markdowna

## Dokumentacija

- [Vodnik za ukazno vrstico](./getting_started/command-line-guide/command-line-guide.md)
- [Vodnik za GitHub Actions (javna skladišča & standardne skrivnosti)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Vodnik za GitHub Actions (skladišča organizacije Microsoft & nastavitve na ravni organizacije)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Podprti jeziki](./getting_started/supported-languages.md)
- [Odpravljanje težav](./getting_started/troubleshooting.md)

## Podprite nas in spodbujajte globalno učenje

Pridružite se nam pri revoluciji deljenja izobraževalne vsebine po svetu! Dajte [Co-op Translatorju](https://github.com/azure/co-op-translator) ⭐ na GitHubu in podprite našo misijo odpravljanja jezikovnih ovir v učenju in tehnologiji. Vaše zanimanje in prispevki imajo velik vpliv! Veseli bomo vaših prispevkov in predlogov za nove funkcije.

### Raziščite Microsoftovo izobraževalno vsebino v svojem jeziku

- [AZD za začetnike](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI za začetnike](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) za začetnike](https://github.com/microsoft/mcp-for-beginners)
- [AI agenti za začetnike](https://github.com/microsoft/ai-agents-for-beginners)
- [Generativna AI za začetnike z .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generativna AI za začetnike](https://github.com/microsoft/generative-ai-for-beginners)
- [Generativna AI za začetnike z Javo](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML za začetnike](https://aka.ms/ml-beginners)
- [Podatkovna znanost za začetnike](https://aka.ms/datascience-beginners)
- [AI za začetnike](https://aka.ms/ai-beginners)
- [Kibernetska varnost za začetnike](https://github.com/microsoft/Security-101)
- [Spletni razvoj za začetnike](https://aka.ms/webdev-beginners)
- [IoT za začetnike](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video predstavitve

Več o Co-op Translatorju si lahko ogledate v naših predstavitvah _(Kliknite na spodnjo sliko za ogled na YouTubu.)_:

- **Open at Microsoft**: Kratek 18-minutni uvod in hitri vodnik za uporabo Co-op Translatorja.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.sl.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Prispevanje

Ta projekt pozdravlja prispevke in predloge. Vas zanima prispevanje k Azure Co-op Translatorju? Oglejte si [CONTRIBUTING.md](./CONTRIBUTING.md) za smernice, kako lahko pomagate narediti Co-op Translator bolj dostopen.

## Prispevalci

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodeks ravnanja

Ta projekt je sprejel [Microsoftov kodeks ravnanja za odprto kodo](https://opensource.microsoft.com/codeofconduct/).
Za več informacij si oglejte [pogosta vprašanja o kodeksu ravnanja](https://opensource.microsoft.com/codeofconduct/faq/) ali
kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Odgovorna umetna inteligenca

Microsoft se zavezuje, da bo svojim strankam pomagal odgovorno uporabljati naše AI izdelke, delil svoje izkušnje in gradil partnerske odnose na zaupanju s pomočjo orodij, kot so Transparency Notes in Impact Assessments. Veliko teh virov najdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftov pristop k odgovorni AI temelji na naših načelih: pravičnost, zanesljivost in varnost, zasebnost in varovanje, vključenost, transparentnost in odgovornost.

Veliki jezikovni, slikovni in govorni modeli – kot so tisti, ki se uporabljajo v tem vzorcu – se lahko obnašajo nepravično, nezanesljivo ali žaljivo, kar lahko povzroči škodo. Prosimo, preberite [Transparency note za Azure OpenAI storitev](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), da se seznanite s tveganji in omejitvami.

Priporočamo, da v svojo arhitekturo vključite varnostni sistem, ki lahko zazna in prepreči škodljivo vedenje. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) zagotavlja neodvisno zaščitno plast, ki lahko zazna škodljivo vsebino, ki jo ustvarijo uporabniki ali AI v aplikacijah in storitvah. Azure AI Content Safety vključuje API-je za besedilo in slike, ki omogočajo zaznavanje škodljive vsebine. Na voljo je tudi interaktivni Content Safety Studio, kjer lahko preizkusite primere kode za zaznavanje škodljive vsebine v različnih modalnostih. Naslednja [dokumentacija za hitri začetek](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vas vodi skozi pošiljanje zahtevkov storitvi.
Drug vidik, ki ga je treba upoštevati, je splošna zmogljivost aplikacije. Pri večmodalnih in večmodelnih aplikacijah zmogljivost pomeni, da sistem deluje tako, kot vi in vaši uporabniki pričakujete, vključno s tem, da ne ustvarja škodljivih rezultatov. Pomembno je oceniti zmogljivost vaše celotne aplikacije z uporabo [meril za kakovost generiranja ter tveganja in varnost](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Svojo AI aplikacijo lahko ocenite v razvojnem okolju z uporabo [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Glede na testni podatkovni niz ali cilj se generacije vaše generativne AI aplikacije kvantitativno merijo z vgrajenimi ali po meri izbranimi evalvatorji. Za začetek uporabe prompt flow SDK za ocenjevanje vašega sistema lahko sledite [hitremu vodniku](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Ko izvedete ocenjevalni zagon, lahko [rezultate vizualizirate v Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Blagovne znamke

Ta projekt lahko vsebuje blagovne znamke ali logotipe za projekte, izdelke ali storitve. Dovoljena uporaba Microsoftovih
blagovnih znamk ali logotipov je predmet in mora slediti
[Microsoftovim smernicam za uporabo blagovnih znamk in znamčenja](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Uporaba Microsoftovih blagovnih znamk ali logotipov v spremenjenih različicah tega projekta ne sme povzročati zmede ali nakazovati, da projekt sponzorira Microsoft.
Vsaka uporaba blagovnih znamk ali logotipov tretjih oseb je predmet politik teh tretjih oseb.

## Pomoč

Če se zataknete ali imate vprašanja o razvoju AI aplikacij, se pridružite:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Če imate povratne informacije o izdelku ali naletite na napake med razvojem, obiščite:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden s pomočjo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvoru jeziku naj velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.