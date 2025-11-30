<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T12:51:40+00:00",
  "source_file": "README.md",
  "language_code": "lt"
}
-->
# Co-op Vertėjas

_Lengvai automatizuokite savo edukacinio GitHub turinio vertimą į kelias kalbas, kad pasiektumėte pasaulinę auditoriją._

[![Python paketas](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licencija: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Atsisiuntimai](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Atsisiuntimai](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Konteineris: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Kodo stilius: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub bendradarbiai](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub problemos](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-užklausos](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Daugiakalbė palaikymas

#### Palaikoma [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabų](../ar/README.md) | [Bengalų](../bn/README.md) | [Bulgarų](../bg/README.md) | [Birmos (Mianmaras)](../my/README.md) | [Kinų (supaprastinta)](../zh/README.md) | [Kinų (tradicinė, Honkongas)](../hk/README.md) | [Kinų (tradicinė, Makao)](../mo/README.md) | [Kinų (tradicinė, Taivanas)](../tw/README.md) | [Kroatų](../hr/README.md) | [Čekų](../cs/README.md) | [Danų](../da/README.md) | [Olandų](../nl/README.md) | [Estų](../et/README.md) | [Suomių](../fi/README.md) | [Prancūzų](../fr/README.md) | [Vokiečių](../de/README.md) | [Graikų](../el/README.md) | [Hebrajų](../he/README.md) | [Hindi](../hi/README.md) | [Vengrų](../hu/README.md) | [Indoneziečių](../id/README.md) | [Italų](../it/README.md) | [Japonų](../ja/README.md) | [Kannadų](../kn/README.md) | [Korėjiečių](../ko/README.md) | [Lietuvių](./README.md) | [Malajų](../ms/README.md) | [Malajalų](../ml/README.md) | [Maratų](../mr/README.md) | [Nepalų](../ne/README.md) | [Nigerijos pidžino](../pcm/README.md) | [Norvegų](../no/README.md) | [Persų (Farsi)](../fa/README.md) | [Lenkų](../pl/README.md) | [Portugalų (Brazilija)](../br/README.md) | [Portugalų (Portugalija)](../pt/README.md) | [Pandžabių (Gurmukhi)](../pa/README.md) | [Rumunų](../ro/README.md) | [Rusų](../ru/README.md) | [Serbų (kirilica)](../sr/README.md) | [Slovakų](../sk/README.md) | [Slovėnų](../sl/README.md) | [Ispanų](../es/README.md) | [Suahelio](../sw/README.md) | [Švedų](../sv/README.md) | [Tagalogų (Filipinų)](../tl/README.md) | [Tamilų](../ta/README.md) | [Telugų](../te/README.md) | [Tajų](../th/README.md) | [Turkų](../tr/README.md) | [Ukrainiečių](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamiečių](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub stebėtojai](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub šakos](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub žvaigždutės](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Atidaryti GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Apžvalga

**Co-op Vertėjas** padeda lengvai lokalizuoti jūsų edukacinį GitHub turinį į kelias kalbas.
Kai atnaujinate savo Markdown failus, paveikslėlius ar užrašų knygeles, vertimai automatiškai sinchronizuojami, užtikrinant, kad jūsų turinys būtų tikslus ir atnaujintas mokiniams visame pasaulyje.

Pavyzdys, kaip organizuojamas išverstas turinys:

![Pavyzdys](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.lt.png)

## Greitas pradėjimas

```bash
# Sukurkite ir aktyvuokite virtualią aplinką (rekomenduojama)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Įdiekite paketą
pip install co-op-translator
# Išversti
translate -l "ko ja fr" -md
```

Docker:

```bash
# Atsisiųskite viešą vaizdą iš GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Paleiskite su prijungtu dabartiniu aplanku ir pateiktu .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimalus nustatymas

1. Sukurkite `.env` failą naudodami šabloną: [.env.template](../../.env.template)
2. Konfigūruokite vieną LLM tiekėją (Azure OpenAI arba OpenAI)
3. (Pasirinktinai) Vaizdų vertimui (`-img`) konfigūruokite Azure AI Vision
4. (Rekomenduojama) Išvalykite ankstesnius vertimus, kad išvengtumėte konfliktų (pvz., `translations/`)
5. (Rekomenduojama) Pridėkite vertimų skyrių į savo README naudodami [README kalbų šabloną](./getting_started/README_languages_template.md)
6. Žr.: [Azure AI nustatymas](./getting_started/set-up-azure-ai.md)

## Naudojimas

Versti visus palaikomus tipus:

```bash
translate -l "ko ja"
```

Tik Markdown:

```bash
translate -l "de" -md
```

Markdown + paveikslėliai:

```bash
translate -l "pt" -md -img
```

Tik užrašų knygelės:

```bash
translate -l "zh" -nb
```

Daugiau parinkčių: [Komandų nuoroda](./getting_started/command-reference.md)

## Funkcijos

- Automatinis vertimas Markdown, užrašų knygelių ir paveikslėlių
- Vertimai sinchronizuojami su šaltinio pakeitimais
- Veikia lokaliai (CLI) arba CI (GitHub Actions)
- Naudoja Azure OpenAI arba OpenAI; pasirenkama Azure AI Vision paveikslėliams
- Išlaiko Markdown formatavimą ir struktūrą

## Dokumentacija

- [Komandų eilutės vadovas](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions vadovas (viešos saugyklos ir standartiniai slaptieji raktai)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions vadovas (Microsoft organizacijos saugyklos ir organizacijos lygio nustatymai)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README kalbų šablonas](./getting_started/README_languages_template.md)
- [Palaikomos kalbos](./getting_started/supported-languages.md)
- [Prisidėjimas](./CONTRIBUTING.md)
- [Trikčių šalinimas](./getting_started/troubleshooting.md)

### Microsoft specifinis vadovas
> [!NOTE]
> Tik Microsoft „Pradedantiesiems“ saugyklų prižiūrėtojams.

- [„Kitų kursų“ sąrašo atnaujinimas (tik MS Pradedantiesiems saugykloms)](./getting_started/update-other-courses.md)

## Palaikykite mus ir skatinkite globalų mokymąsi

Prisijunkite prie mūsų revoliucijos, kaip edukacinis turinys dalijamasi visame pasaulyje! Įvertinkite [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ GitHub ir palaikykite mūsų misiją įveikti kalbų barjerus mokymesi ir technologijose. Jūsų susidomėjimas ir indėlis daro didelį poveikį! Kodo indėliai ir funkcijų pasiūlymai visada laukiami.

### Tyrinėkite Microsoft edukacinį turinį savo kalba

- [AZD pradedantiesiems](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI pradedantiesiems](https://github.com/microsoft/edgeai-for-beginners)
- [Modelio konteksto protokolas (MCP) pradedantiesiems](https://github.com/microsoft/mcp-for-beginners)
- [AI agentai pradedantiesiems](https://github.com/microsoft/ai-agents-for-beginners)
- [Generatyvioji AI pradedantiesiems naudojant .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generatyvioji AI pradedantiesiems](https://github.com/microsoft/generative-ai-for-beginners)
- [Generatyvioji AI pradedantiesiems naudojant Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML pradedantiesiems](https://aka.ms/ml-beginners)
- [Duomenų mokslas pradedantiesiems](https://aka.ms/datascience-beginners)
- [AI pradedantiesiems](https://aka.ms/ai-beginners)
- [Kibernetinis saugumas pradedantiesiems](https://github.com/microsoft/Security-101)
- [Tinklalapių kūrimas pradedantiesiems](https://aka.ms/webdev-beginners)
- [IoT pradedantiesiems](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Vaizdo pristatymai

👉 Spustelėkite žemiau esantį paveikslėlį, kad žiūrėtumėte YouTube.

- **Open at Microsoft**: Trumpas 18 minučių įvadas ir greitas vadovas, kaip naudoti Co-op Vertėją.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.lt.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Prisidėjimas

Šis projektas kviečia prisidėti ir teikti pasiūlymus. Norite prisidėti prie Azure Co-op Translator? Prašome peržiūrėti mūsų [CONTRIBUTING.md](./CONTRIBUTING.md) gaires, kaip galite padėti padaryti Co-op Vertėją prieinamesnį.

## Bendradarbiai

[![co-op-translator bendradarbiai](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Elgesio kodeksas

Šis projektas priėmė [Microsoft atvirojo kodo elgesio kodeksą](https://opensource.microsoft.com/codeofconduct/).
Daugiau informacijos rasite [Elgesio kodekso DUK](https://opensource.microsoft.com/codeofconduct/faq/) arba
kreipkitės el. paštu [opencode@microsoft.com](mailto:opencode@microsoft.com) dėl papildomų klausimų ar pastabų.

## Atsakingas dirbtinis intelektas

Microsoft įsipareigoja padėti savo klientams atsakingai naudoti mūsų DI produktus, dalintis patirtimi ir kurti pasitikėjimu grįstas partnerystes per įrankius, tokius kaip Skaidrumo pastabos ir Poveikio vertinimai. Daugelį šių išteklių rasite adresu [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft požiūris į atsakingą DI remiasi mūsų DI principais: sąžiningumu, patikimumu ir saugumu, privatumu ir saugumu, įtrauktimi, skaidrumu ir atsakomybe.

Didelio masto natūralios kalbos, vaizdų ir balso modeliai – kaip ir šio pavyzdžio – gali elgtis neteisingai, nepatikimai ar įžeidžiančiai, sukeldami žalą. Prašome susipažinti su [Azure OpenAI paslaugos Skaidrumo pastaba](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), kad būtumėte informuoti apie rizikas ir apribojimus.
Rekomenduojamas būdas sumažinti šias rizikas – įtraukti saugumo sistemą į savo architektūrą, kuri galėtų aptikti ir užkirsti kelią žalingam elgesiui. <a href="https://learn.microsoft.com/azure/ai-services/content-safety/overview">Azure AI Content Safety</a> suteikia nepriklausomą apsaugos sluoksnį, galintį aptikti žalingą vartotojų ir dirbtinio intelekto generuotą turinį programose ir paslaugose. Azure AI Content Safety apima teksto ir vaizdų API, leidžiančias aptikti žalingą medžiagą. Taip pat turime interaktyvią Content Safety Studio, kurioje galite peržiūrėti, išnagrinėti ir išbandyti pavyzdinį kodą, skirtą žalingo turinio aptikimui įvairiomis modalitetėmis. Ši [greitojo starto dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) padės jums atlikti užklausas šiai paslaugai.

Kitas svarbus aspektas – bendras programos našumas. Naudojant daugiamodalius ir daugiamodelius sprendimus, našumu laikome tai, kad sistema veiktų taip, kaip tikitės jūs ir jūsų vartotojai, įskaitant ir tai, kad nesukurtų žalingų rezultatų. Svarbu įvertinti bendrą programos našumą naudodami <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in">generavimo kokybės bei rizikos ir saugumo metrikas</a>.

Galite įvertinti savo DI programą kūrimo aplinkoje naudodami <a href="https://microsoft.github.io/promptflow/index.html">prompt flow SDK</a>. Turėdami testinį duomenų rinkinį arba tikslą, jūsų generatyvios DI programos generavimai kiekybiškai įvertinami naudojant įmontuotus arba pasirinktinius vertintojus. Norėdami pradėti naudotis prompt flow SDK savo sistemos vertinimui, galite sekti [greitojo starto vadovą](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Įvykdę vertinimo paleidimą, galite <a href="https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results">vizualizuoti rezultatus Azure AI Studio</a>.

## Prekių ženklai

Šiame projekte gali būti prekių ženklų arba logotipų, susijusių su projektais, produktais ar paslaugomis. Leidžiamas Microsoft prekių ženklų ar logotipų naudojimas yra reglamentuojamas ir turi atitikti <a href="https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general">Microsoft prekių ženklų ir prekės ženklo gairių</a> reikalavimus. Microsoft prekių ženklų ar logotipų naudojimas modifikuotose šio projekto versijose neturi sukelti painiavos ar rodyti Microsoft rėmimo. Bet koks trečiųjų šalių prekių ženklų ar logotipų naudojimas yra reglamentuojamas tų trečiųjų šalių taisyklių.

## Pagalba

Jei susiduriate su sunkumais arba turite klausimų apie DI programų kūrimą, prisijunkite prie:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jei turite atsiliepimų apie produktą arba susiduriate su klaidomis kūrimo metu, apsilankykite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->