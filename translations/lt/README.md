<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T04:39:09+00:00",
  "source_file": "README.md",
  "language_code": "lt"
}
-->
# Co-op Translator

_Lengvai automatizuokite savo edukacinio GitHub turinio vertimą į daugelį kalbų ir pasiekite pasaulinę auditoriją._

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

### 🌐 Daugiakalbė palaikymas

#### Palaikoma su [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabų](../ar/README.md) | [Bengalų](../bn/README.md) | [Bulgarų](../bg/README.md) | [Birmiečių (Mianmaras)](../my/README.md) | [Kinų (supaprastinta)](../zh/README.md) | [Kinų (tradicinė, Honkongas)](../hk/README.md) | [Kinų (tradicinė, Makao)](../mo/README.md) | [Kinų (tradicinė, Taivanas)](../tw/README.md) | [Kroatų](../hr/README.md) | [Čekų](../cs/README.md) | [Danų](../da/README.md) | [Olandų](../nl/README.md) | [Estų](../et/README.md) | [Suomių](../fi/README.md) | [Prancūzų](../fr/README.md) | [Vokiečių](../de/README.md) | [Graikų](../el/README.md) | [Hebrajų](../he/README.md) | [Hindi](../hi/README.md) | [Vengrų](../hu/README.md) | [Indoneziečių](../id/README.md) | [Italų](../it/README.md) | [Japonų](../ja/README.md) | [Korėjiečių](../ko/README.md) | [Lietuvių](./README.md) | [Malajų](../ms/README.md) | [Maratų](../mr/README.md) | [Nepalų](../ne/README.md) | [Norvegų](../no/README.md) | [Persų (farsi)](../fa/README.md) | [Lenkų](../pl/README.md) | [Portugalų (Brazilija)](../br/README.md) | [Portugalų (Portugalija)](../pt/README.md) | [Pandžabų (Gurmukhi)](../pa/README.md) | [Rumunų](../ro/README.md) | [Rusų](../ru/README.md) | [Serbų (kirilica)](../sr/README.md) | [Slovakų](../sk/README.md) | [Slovėnų](../sl/README.md) | [Ispanų](../es/README.md) | [Svahilių](../sw/README.md) | [Švedų](../sv/README.md) | [Tagalogų (filipiniečių)](../tl/README.md) | [Tamilų](../ta/README.md) | [Tajų](../th/README.md) | [Turkų](../tr/README.md) | [Ukrainiečių](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamiečių](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Apžvalga

**Co-op Translator** leidžia greitai išversti jūsų edukacinį GitHub turinį į daugelį kalbų ir be vargo pasiekti pasaulinę auditoriją. Kai atnaujinate savo Markdown failus, paveikslėlius ar Jupyter užrašines, vertimai automatiškai sinchronizuojami, kad jūsų edukacinis GitHub turinys išliktų aktualus ir naudingas tarptautiniams vartotojams.

Pažiūrėkite, kaip Co-op Translator organizuoja išverstą edukacinį GitHub turinį:

![Pavyzdys](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.lt.png)

## Greitas startas

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

## Minimalus paruošimas

- Sukurkite `.env` naudodami šabloną: [.env.template](../../.env.template)
- Sujunkite vieną LLM tiekėją (Azure OpenAI arba OpenAI)
- Norint versti paveikslėlius (`-img`), taip pat nustatykite Azure AI Vision
- Rekomenduojama: jei turite vertimų, sugeneruotų kitais įrankiais, pirmiausia juos išvalykite, kad išvengtumėte konfliktų (pavyzdžiui: `translations/`).
- Rekomenduojama: pridėkite vertimų skyrių į savo README naudodami [README kalbų šabloną](./README_languages_template.md)
- Žiūrėkite: [Azure AI nustatymas](./getting_started/set-up-azure-ai.md)

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

Tik užrašinės:

```bash
translate -l "zh" -nb
```

Daugiau vėliavėlių: [Komandų nuoroda](./getting_started/command-reference.md)

## Funkcijos

- Automatinis Markdown, užrašinių ir paveikslėlių vertimas
- Vertimai sinchronizuojami su šaltinio pakeitimais
- Veikia lokaliai (CLI) arba CI (GitHub Actions)
- Naudoja Azure OpenAI arba OpenAI; pasirinktinai Azure AI Vision paveikslėliams
- Išlaiko Markdown formatavimą ir struktūrą

## Dokumentacija

- [Komandų eilutės gidas](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions gidas (viešiems repozitorijams ir standartinėms paslaptims)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions gidas (Microsoft organizacijos repozitorijams ir organizacijos lygio nustatymams)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Palaikomos kalbos](./getting_started/supported-languages.md)
- [Trikčių šalinimas](./getting_started/troubleshooting.md)

## Palaikykite mus ir skatinkite pasaulinį mokymąsi

Prisijunkite prie mūsų revoliucionuojant, kaip edukacinis turinys dalijamasi visame pasaulyje! Suteikite [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ GitHub platformoje ir palaikykite mūsų misiją naikinti kalbines kliūtis mokymesi ir technologijose. Jūsų susidomėjimas ir indėlis daro didelę įtaką! Kodo indėliai ir funkcijų pasiūlymai visada laukiami.

### Atraskite Microsoft edukacinį turinį savo kalba

- [AZD pradedantiesiems](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI pradedantiesiems](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) pradedantiesiems](https://github.com/microsoft/mcp-for-beginners)
- [AI agentai pradedantiesiems](https://github.com/microsoft/ai-agents-for-beginners)
- [Generatyvinis AI pradedantiesiems naudojant .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generatyvinis AI pradedantiesiems](https://github.com/microsoft/generative-ai-for-beginners)
- [Generatyvinis AI pradedantiesiems naudojant Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML pradedantiesiems](https://aka.ms/ml-beginners)
- [Duomenų mokslas pradedantiesiems](https://aka.ms/datascience-beginners)
- [AI pradedantiesiems](https://aka.ms/ai-beginners)
- [Kibernetinis saugumas pradedantiesiems](https://github.com/microsoft/Security-101)
- [Web kūrimas pradedantiesiems](https://aka.ms/webdev-beginners)
- [IoT pradedantiesiems](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Vaizdo pristatymai

Sužinokite daugiau apie Co-op Translator per mūsų pristatymus _(Spustelėkite paveikslėlį žemiau, kad žiūrėtumėte YouTube.)_:

- **Open at Microsoft**: Trumpas 18 minučių įvadas ir greitas gidas, kaip naudoti Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.lt.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Prisidėjimas

Šis projektas laukia jūsų indėlio ir pasiūlymų. Norite prisidėti prie Azure Co-op Translator? Prašome peržiūrėti mūsų [CONTRIBUTING.md](./CONTRIBUTING.md) gaires, kaip galite padėti padaryti Co-op Translator dar prieinamesnį.

## Prisidėję asmenys

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Elgesio kodeksas

Šis projektas laikosi [Microsoft atvirojo kodo elgesio kodekso](https://opensource.microsoft.com/codeofconduct/).
Daugiau informacijos rasite [Elgesio kodekso DUK](https://opensource.microsoft.com/codeofconduct/faq/) arba
kreipkitės el. paštu [opencode@microsoft.com](mailto:opencode@microsoft.com) su papildomais klausimais ar komentarais.

## Atsakingas dirbtinis intelektas

Microsoft siekia padėti savo klientams atsakingai naudoti mūsų DI produktus, dalintis savo patirtimi ir kurti pasitikėjimu grįstus partnerystės santykius, naudodama tokius įrankius kaip skaidrumo pastabos ir poveikio vertinimai. Daugelį šių išteklių rasite adresu [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft atsakingo DI požiūris grindžiamas mūsų DI principais: sąžiningumas, patikimumas ir saugumas, privatumas ir saugumas, įtrauktis, skaidrumas ir atskaitomybė.

Didelio masto natūralios kalbos, vaizdų ir kalbos modeliai – kaip tie, kurie naudojami šiame pavyzdyje – gali elgtis nesąžiningai, nepatikimai ar įžeidžiančiai, taip sukeldami žalą. Prašome susipažinti su [Azure OpenAI paslaugos skaidrumo pastaba](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), kad žinotumėte apie rizikas ir apribojimus.

Rekomenduojamas būdas sumažinti šias rizikas – įtraukti saugumo sistemą į savo architektūrą, kuri galėtų aptikti ir užkirsti kelią žalingam elgesiui. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) suteikia nepriklausomą apsaugos sluoksnį, galintį aptikti žalingą vartotojų ar DI sugeneruotą turinį programose ir paslaugose. Azure AI Content Safety apima teksto ir vaizdų API, leidžiančias aptikti žalingą medžiagą. Taip pat turime interaktyvią Content Safety Studio, kurioje galite peržiūrėti, tyrinėti ir išbandyti pavyzdinį kodą žalingo turinio aptikimui įvairiais būdais. Ši [greito starto dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) padės jums atlikti užklausas šiai paslaugai.
Kitas svarbus aspektas – bendras programos našumas. Kuriant daugiarūšes ir daugiamodelines programas, našumas reiškia, kad sistema veikia taip, kaip tikitės jūs ir jūsų naudotojai, įskaitant ir tai, kad negeneruoja žalingų rezultatų. Svarbu įvertinti bendrą programos našumą naudojant [generavimo kokybės, rizikos ir saugumo metrikas](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Savo AI programą galite įvertinti kūrimo aplinkoje naudodami [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Turėdami testavimo duomenų rinkinį arba tikslą, jūsų generatyvios AI programos rezultatai kiekybiškai įvertinami naudojant integruotus arba jūsų pasirinktus vertintojus. Norėdami pradėti naudotis prompt flow SDK ir įvertinti savo sistemą, sekite [greitos pradžios vadovą](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Atlikę vertinimo paleidimą, galite [peržiūrėti rezultatus Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Prekės ženklai

Šiame projekte gali būti prekių ženklų ar logotipų, susijusių su projektais, produktais ar paslaugomis. Leidžiamas Microsoft prekių ženklų ar logotipų naudojimas turi atitikti ir laikytis [Microsoft prekių ženklų ir prekės ženklo gairių](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Naudojant Microsoft prekių ženklus ar logotipus modifikuotose šio projekto versijose, negalima sukelti painiavos ar sudaryti įspūdžio, kad Microsoft remia projektą. Bet kokiam trečiųjų šalių prekių ženklų ar logotipų naudojimui taikomos tų trečiųjų šalių taisyklės.

## Pagalba

Jei susidūrėte su sunkumais ar turite klausimų apie AI programų kūrimą, prisijunkite:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jei turite atsiliepimų apie produktą ar susidūrėte su klaidomis kurdami, apsilankykite:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Atsakomybės atsisakymas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį naudojantis šiuo vertimu.