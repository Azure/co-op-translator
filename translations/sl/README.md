<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T12:36:09+00:00",
  "source_file": "README.md",
  "language_code": "sl"
}
-->
# Co-op prevajalnik

_Preprosto avtomatizirajte prevajanje vaših izobraževalnih vsebin na GitHubu v več jezikov, da dosežete globalno občinstvo._

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

### 🌐 Podpora za več jezikov

#### Podprto s strani [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabščina](../ar/README.md) | [Bengalščina](../bn/README.md) | [Bolgarščina](../bg/README.md) | [Burmanščina (Mjanmar)](../my/README.md) | [Kitajščina (poenostavljena)](../zh/README.md) | [Kitajščina (tradicionalna, Hong Kong)](../hk/README.md) | [Kitajščina (tradicionalna, Makao)](../mo/README.md) | [Kitajščina (tradicionalna, Tajvan)](../tw/README.md) | [Hrvaščina](../hr/README.md) | [Češčina](../cs/README.md) | [Danščina](../da/README.md) | [Nizozemščina](../nl/README.md) | [Estonščina](../et/README.md) | [Finščina](../fi/README.md) | [Francoščina](../fr/README.md) | [Nemščina](../de/README.md) | [Grščina](../el/README.md) | [Hebrejščina](../he/README.md) | [Hindijščina](../hi/README.md) | [Madžarščina](../hu/README.md) | [Indonezijščina](../id/README.md) | [Italijanščina](../it/README.md) | [Japonščina](../ja/README.md) | [Kannada](../kn/README.md) | [Korejščina](../ko/README.md) | [Litovščina](../lt/README.md) | [Malajščina](../ms/README.md) | [Malajalščina](../ml/README.md) | [Maratščina](../mr/README.md) | [Nepalščina](../ne/README.md) | [Nigerijski pidžin](../pcm/README.md) | [Norveščina](../no/README.md) | [Perzijščina (Farsi)](../fa/README.md) | [Poljščina](../pl/README.md) | [Portugalščina (Brazilija)](../br/README.md) | [Portugalščina (Portugalska)](../pt/README.md) | [Pandžabščina (Gurmukhi)](../pa/README.md) | [Romunščina](../ro/README.md) | [Ruščina](../ru/README.md) | [Srbščina (cirilica)](../sr/README.md) | [Slovaščina](../sk/README.md) | [Slovenščina](./README.md) | [Španščina](../es/README.md) | [Svahili](../sw/README.md) | [Švedščina](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamilščina](../ta/README.md) | [Telugu](../te/README.md) | [Tajščina](../th/README.md) | [Turščina](../tr/README.md) | [Ukrajinščina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamščina](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Pregled

**Co-op prevajalnik** vam pomaga enostavno lokalizirati vaše izobraževalne vsebine na GitHubu v več jezikov.
Ko posodobite svoje Markdown datoteke, slike ali zvezke, se prevodi samodejno sinhronizirajo, kar zagotavlja, da so vaše vsebine točne in ažurne za učence po vsem svetu.

Primer, kako je organizirana prevedena vsebina:

![Primer](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.sl.png)

## Hitri začetek

```bash
# Ustvari in aktiviraj virtualno okolje (priporočeno)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Namesti paket
pip install co-op-translator
# Prevedi
translate -l "ko ja fr" -md
```

Docker:

```bash
# Potegnite javno sliko iz GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Zaženite z montirano trenutno mapo in zagotovljeno datoteko .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimalna nastavitev

1. Ustvarite datoteko `.env` po predlogi: [.env.template](../../.env.template)
2. Nastavite enega ponudnika LLM (Azure OpenAI ali OpenAI)
3. (Neobvezno) Za prevajanje slik (`-img`) nastavite Azure AI Vision
4. (Priporočeno) Očistite prejšnje prevode, da se izognete konfliktom (npr. `translations/`)
5. (Priporočeno) Dodajte prevajalski odsek v vaš README z uporabo [predloge za jezike v README](./getting_started/README_languages_template.md)
6. Oglejte si: [Nastavitev Azure AI](./getting_started/set-up-azure-ai.md)

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

## Funkcije

- Avtomatizirano prevajanje Markdown, zvezkov in slik
- Prevodi se sinhronizirajo z izvirnimi spremembami
- Deluje lokalno (CLI) ali v CI (GitHub Actions)
- Uporablja Azure OpenAI ali OpenAI; neobvezno Azure AI Vision za slike
- Ohranja oblikovanje in strukturo Markdowna

## Dokumentacija

- [Vodnik za ukazno vrstico](./getting_started/command-line-guide/command-line-guide.md)
- [Vodnik za GitHub Actions (javni repozitoriji in standardni skrivnosti)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Vodnik za GitHub Actions (Microsoft organizacijski repozitoriji in nastavitve na ravni organizacije)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Predloga za jezike v README](./getting_started/README_languages_template.md)
- [Podprti jeziki](./getting_started/supported-languages.md)
- [Prispevanje](./CONTRIBUTING.md)
- [Reševanje težav](./getting_started/troubleshooting.md)

### Poseben Microsoftov vodnik
> [!NOTE]
> Samo za vzdrževalce Microsoftovih repozitorijev "Za začetnike".

- [Posodobitev seznama "drugih tečajev" (samo za MS začetniške repozitorije)](./getting_started/update-other-courses.md)

## Podprite nas in spodbujajte globalno učenje

Pridružite se nam pri revoluciji deljenja izobraževalnih vsebin po vsem svetu! Podprite [Co-op Translator](https://github.com/azure/co-op-translator) z zvezdico na GitHubu in podprite našo misijo razbijanja jezikovnih ovir pri učenju in tehnologiji. Vaše zanimanje in prispevki imajo velik vpliv! Prispevki kode in predlogi za funkcije so vedno dobrodošli.

### Raziščite Microsoftove izobraževalne vsebine v vašem jeziku

- [AZD za začetnike](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI za začetnike](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) za začetnike](https://github.com/microsoft/mcp-for-beginners)
- [AI agenti za začetnike](https://github.com/microsoft/ai-agents-for-beginners)
- [Generativna AI za začetnike z uporabo .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generativna AI za začetnike](https://github.com/microsoft/generative-ai-for-beginners)
- [Generativna AI za začetnike z uporabo Jave](https://github.com/microsoft/generative-ai-for-beginners-java)
- [Strojno učenje za začetnike](https://aka.ms/ml-beginners)
- [Podatkovna znanost za začetnike](https://aka.ms/datascience-beginners)
- [AI za začetnike](https://aka.ms/ai-beginners)
- [Kibernetska varnost za začetnike](https://github.com/microsoft/Security-101)
- [Spletni razvoj za začetnike](https://aka.ms/webdev-beginners)
- [IoT za začetnike](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video predstavitve

👉 Kliknite na spodnjo sliko za ogled na YouTubu.

- **Open at Microsoft**: Kratek 18-minutni uvod in hiter vodič, kako uporabljati Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.sl.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Prispevanje

Ta projekt sprejema prispevke in predloge. Vas zanima prispevati k Azure Co-op Translator? Prosimo, preberite naš [CONTRIBUTING.md](./CONTRIBUTING.md) za navodila, kako lahko pomagate narediti Co-op Translator bolj dostopen.

## Prispevalci

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodeks ravnanja

Ta projekt je sprejel [Microsoftov kodeks ravnanja za odprto kodo](https://opensource.microsoft.com/codeofconduct/).
Za več informacij si oglejte [Pogosta vprašanja o kodeksu ravnanja](https://opensource.microsoft.com/codeofconduct/faq/) ali
kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Odgovorna umetna inteligenca

Microsoft si prizadeva pomagati svojim strankam, da uporabljajo naše AI izdelke odgovorno, deliti naše izkušnje in graditi zaupanja vredna partnerstva z orodji, kot so Transparency Notes in Impact Assessments. Veliko teh virov najdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftov pristop k odgovorni umetni inteligenci temelji na naših AI načelih pravičnosti, zanesljivosti in varnosti, zasebnosti in varnosti, vključevanju, preglednosti in odgovornosti.

Veliki modeli za naravni jezik, slike in govor – kot tisti, uporabljeni v tem vzorcu – se lahko obnašajo na načine, ki so nepravični, nezanesljivi ali žaljivi, kar lahko povzroči škodo. Prosimo, preberite [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), da se seznanite z tveganji in omejitvami.
Priporočeni pristop za zmanjševanje teh tveganj je vključitev varnostnega sistema v vašo arhitekturo, ki lahko zazna in prepreči škodljivo vedenje. <a href="https://learn.microsoft.com/azure/ai-services/content-safety/overview">Azure AI Content Safety</a> zagotavlja neodvisno zaščitno plast, ki lahko zazna škodljivo vsebino, ki jo ustvarijo uporabniki ali AI, v aplikacijah in storitvah. Azure AI Content Safety vključuje API-je za besedilo in slike, ki omogočajo zaznavanje škodljivega gradiva. Na voljo imamo tudi interaktivno Content Safety Studio, ki vam omogoča ogled, raziskovanje in preizkušanje vzorčne kode za zaznavanje škodljive vsebine v različnih modalitetah. Naslednja <a href="https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest">dokumentacija za hiter začetek</a> vas vodi skozi postopek pošiljanja zahtevkov storitvi.

Drugi vidik, ki ga je treba upoštevati, je splošna zmogljivost aplikacije. Pri večmodalnih in večmodelnih aplikacijah zmogljivost pomeni, da sistem deluje tako, kot vi in vaši uporabniki pričakujete, vključno s tem, da ne ustvarja škodljivih izhodov. Pomembno je oceniti zmogljivost vaše celotne aplikacije z uporabo <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in">meril kakovosti generiranja ter tveganj in varnosti</a>.

Vašo AI aplikacijo lahko ocenite v razvojni okolju z uporabo <a href="https://microsoft.github.io/promptflow/index.html">prompt flow SDK</a>. Glede na testni nabor podatkov ali cilj se generacije vaše generativne AI aplikacije kvantitativno ocenijo z vgrajenimi ali poljubnimi ocenilci po vaši izbiri. Za začetek z uporabo prompt flow SDK za ocenjevanje vašega sistema lahko sledite <a href="https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk">vodniku za hiter začetek</a>. Ko izvedete ocenjevalno izvajanje, lahko <a href="https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results">vizualizirate rezultate v Azure AI Studio</a>.

## Blagovne znamke

Ta projekt lahko vsebuje blagovne znamke ali logotipe za projekte, izdelke ali storitve. Pooblaščena uporaba Microsoftovih blagovnih znamk ali logotipov je predmet in mora slediti <a href="https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general">Microsoftovim smernicam za blagovne znamke in znamčenje</a>. Uporaba Microsoftovih blagovnih znamk ali logotipov v spremenjenih različicah tega projekta ne sme povzročati zmede ali nakazovati sponzorstva Microsofta. Vsaka uporaba blagovnih znamk ali logotipov tretjih oseb je predmet pravil teh tretjih oseb.

## Pomoč

Če se zataknete ali imate vprašanja o gradnji AI aplikacij, se pridružite:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Če imate povratne informacije o izdelku ali naletite na napake med gradnjo, obiščite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->