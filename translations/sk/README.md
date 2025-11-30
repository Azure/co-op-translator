<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:54:01+00:00",
  "source_file": "README.md",
  "language_code": "sk"
}
-->
# Co-op Translator

_Jednoducho automatizujte preklad svojho vzdelávacieho obsahu na GitHube do viacerých jazykov a oslovte tak celosvetové publikum._

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

### 🌐 Podpora viacerých jazykov

#### Podporované nástrojom [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabčina](../ar/README.md) | [Bengálčina](../bn/README.md) | [Bulharčina](../bg/README.md) | [Barmčina (Mjanmarsko)](../my/README.md) | [Čínština (zjednodušená)](../zh/README.md) | [Čínština (tradičná, Hongkong)](../hk/README.md) | [Čínština (tradičná, Macao)](../mo/README.md) | [Čínština (tradičná, Taiwan)](../tw/README.md) | [Chorvátčina](../hr/README.md) | [Čeština](../cs/README.md) | [Dánčina](../da/README.md) | [Holandčina](../nl/README.md) | [Estónčina](../et/README.md) | [Fínčina](../fi/README.md) | [Francúzština](../fr/README.md) | [Nemčina](../de/README.md) | [Gréčtina](../el/README.md) | [Hebrejčina](../he/README.md) | [Hindčina](../hi/README.md) | [Maďarčina](../hu/README.md) | [Indonézština](../id/README.md) | [Taliančina](../it/README.md) | [Japončina](../ja/README.md) | [Kórejčina](../ko/README.md) | [Litovčina](../lt/README.md) | [Malajčina](../ms/README.md) | [Maráthčina](../mr/README.md) | [Nepálčina](../ne/README.md) | [Nórčina](../no/README.md) | [Perzština (Fársí)](../fa/README.md) | [Poľština](../pl/README.md) | [Portugalčina (Brazília)](../br/README.md) | [Portugalčina (Portugalsko)](../pt/README.md) | [Pandžábčina (Gurmukhi)](../pa/README.md) | [Rumunčina](../ro/README.md) | [Ruština](../ru/README.md) | [Srbčina (cyrilika)](../sr/README.md) | [Slovenčina](./README.md) | [Slovinčina](../sl/README.md) | [Španielčina](../es/README.md) | [Swahilčina](../sw/README.md) | [Švédčina](../sv/README.md) | [Tagalog (filipínčina)](../tl/README.md) | [Tamilčina](../ta/README.md) | [Thajčina](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinčina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamčina](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Prehľad

**Co-op Translator** vám umožní rýchlo prekladať váš vzdelávací obsah na GitHube do viacerých jazykov a bez námahy tak osloviť globálne publikum. Keď aktualizujete svoje Markdown súbory, obrázky alebo Jupyter notebooky, preklady sa automaticky synchronizujú, aby váš vzdelávací obsah na GitHube zostal aktuálny a relevantný pre používateľov z celého sveta.

Pozrite sa, ako Co-op Translator organizuje preložený vzdelávací obsah na GitHube:

![Príklad](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.sk.png)

## Rýchly štart

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

## Minimálne nastavenie

- Vytvorte súbor `.env` podľa šablóny: [.env.template](../../.env.template)
- Nastavte jedného poskytovateľa LLM (Azure OpenAI alebo OpenAI)
- Pre preklad obrázkov (`-img`) nastavte aj Azure AI Vision
- Odporúčané: Ak už máte preklady vytvorené inými nástrojmi, najskôr ich odstráňte, aby ste predišli konfliktom (napríklad: `translations/`).
- Odporúčané: Pridajte sekciu s prekladmi do svojho README pomocou [README šablóny jazykov](./README_languages_template.md)
- Pozrite: [Nastavenie Azure AI](./getting_started/set-up-azure-ai.md)

## Použitie

Preklad všetkých podporovaných typov:

```bash
translate -l "ko ja"
```

Len Markdown:

```bash
translate -l "de" -md
```

Markdown + obrázky:

```bash
translate -l "pt" -md -img
```

Len notebooky:

```bash
translate -l "zh" -nb
```

Ďalšie prepínače: [Referenčný zoznam príkazov](./getting_started/command-reference.md)

## Funkcie

- Automatizovaný preklad Markdownu, notebookov a obrázkov
- Udržiava preklady synchronizované so zmenami v zdrojových súboroch
- Funguje lokálne (CLI) aj v CI (GitHub Actions)
- Využíva Azure OpenAI alebo OpenAI; voliteľne Azure AI Vision pre obrázky
- Zachováva formátovanie a štruktúru Markdownu

## Dokumentácia

- [Príručka príkazového riadku](./getting_started/command-line-guide/command-line-guide.md)
- [Príručka pre GitHub Actions (verejné repozitáre & štandardné tajomstvá)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Príručka pre GitHub Actions (repozitáre Microsoft organizácie & nastavenia na úrovni organizácie)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Podporované jazyky](./getting_started/supported-languages.md)
- [Riešenie problémov](./getting_started/troubleshooting.md)

## Podporte nás a rozvíjajte globálne vzdelávanie

Pridajte sa k nám a pomôžte zmeniť spôsob, akým sa vzdelávací obsah zdieľa po celom svete! Dajte [Co-op Translatoru](https://github.com/azure/co-op-translator) ⭐ na GitHube a podporte našu misiu búrať jazykové bariéry vo vzdelávaní a technológiách. Váš záujem a príspevky majú veľký význam! Príspevky do kódu a návrhy na nové funkcie sú vždy vítané.

### Objavte vzdelávací obsah Microsoftu vo svojom jazyku

- [AZD pre začiatočníkov](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI pre začiatočníkov](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) pre začiatočníkov](https://github.com/microsoft/mcp-for-beginners)
- [AI agenti pre začiatočníkov](https://github.com/microsoft/ai-agents-for-beginners)
- [Generatívna AI pre začiatočníkov s .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generatívna AI pre začiatočníkov](https://github.com/microsoft/generative-ai-for-beginners)
- [Generatívna AI pre začiatočníkov s Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [Strojové učenie pre začiatočníkov](https://aka.ms/ml-beginners)
- [Data Science pre začiatočníkov](https://aka.ms/datascience-beginners)
- [AI pre začiatočníkov](https://aka.ms/ai-beginners)
- [Kybernetická bezpečnosť pre začiatočníkov](https://github.com/microsoft/Security-101)
- [Webový vývoj pre začiatočníkov](https://aka.ms/webdev-beginners)
- [IoT pre začiatočníkov](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video prezentácie

Zistite viac o Co-op Translatori prostredníctvom našich prezentácií _(Kliknite na obrázok nižšie a pozrite si video na YouTube.)_:

- **Open at Microsoft**: Krátky 18-minútový úvod a rýchly sprievodca používaním Co-op Translatora.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.sk.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Prispievanie

Tento projekt víta príspevky a návrhy. Máte záujem prispieť do Azure Co-op Translator? Pozrite si náš [CONTRIBUTING.md](./CONTRIBUTING.md) pre pokyny, ako môžete pomôcť spraviť Co-op Translator dostupnejším.

## Prispievatelia

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kódex správania

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Viac informácií nájdete v [často kladených otázkach ku kódexu správania](https://opensource.microsoft.com/codeofconduct/faq/) alebo
kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s ďalšími otázkami alebo pripomienkami.

## Zodpovedná AI

Microsoft sa zaväzuje pomáhať zákazníkom používať naše AI produkty zodpovedne, zdieľať naše poznatky a budovať dôveru prostredníctvom nástrojov ako Transparency Notes a Impact Assessments. Mnohé z týchto zdrojov nájdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Prístup Microsoftu k zodpovednej AI je založený na našich AI princípoch: férovosť, spoľahlivosť a bezpečnosť, súkromie a bezpečnosť, inkluzívnosť, transparentnosť a zodpovednosť.

Veľké jazykové, obrazové a hlasové modely – ako tie použité v tejto ukážke – sa môžu správať nečakane, nespoľahlivo alebo nevhodne, čo môže viesť k škodám. Prečítajte si [Transparency note k Azure OpenAI službe](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby ste boli informovaní o rizikách a obmedzeniach.

Odporúčaným spôsobom, ako tieto riziká zmierniť, je zahrnúť do svojej architektúry bezpečnostný systém, ktorý dokáže detegovať a zabrániť škodlivému správaniu. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislú vrstvu ochrany, ktorá dokáže detegovať škodlivý obsah vytvorený používateľmi aj AI v aplikáciách a službách. Azure AI Content Safety obsahuje textové a obrazové API, ktoré umožňujú detegovať škodlivý materiál. K dispozícii je aj interaktívne Content Safety Studio, kde si môžete vyskúšať detekciu škodlivého obsahu v rôznych modalitách. Nasledujúca [rýchla príručka](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás prevedie odoslaním požiadaviek na túto službu.


Ďalším aspektom, ktorý treba zohľadniť, je celkový výkon aplikácie. Pri aplikáciách, ktoré využívajú viacero modalít a modelov, považujeme za výkon to, že systém funguje podľa očakávaní vás aj vašich používateľov, vrátane toho, že negeneruje škodlivé výstupy. Je dôležité hodnotiť výkon celej vašej aplikácie pomocou [metrik kvality generovania a rizika a bezpečnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Svoju AI aplikáciu môžete vyhodnotiť vo vývojovom prostredí pomocou [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Pri použití testovacej množiny alebo cieľa sú generácie vašej generatívnej AI aplikácie kvantitatívne merané pomocou vstavaných alebo vlastných hodnotiacich nástrojov podľa vášho výberu. Ak chcete začať s prompt flow SDK na vyhodnotenie vášho systému, môžete postupovať podľa [rýchleho sprievodcu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po vykonaní hodnotiaceho behu môžete [vizualizovať výsledky v Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ochranné známky

Tento projekt môže obsahovať ochranné známky alebo logá projektov, produktov alebo služieb. Povolené používanie ochranných známok alebo log spoločnosti Microsoft podlieha a musí byť v súlade s [Pokynmi pre používanie ochranných známok a značky Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Použitie ochranných známok alebo log spoločnosti Microsoft v upravených verziách tohto projektu nesmie spôsobovať zmätok ani naznačovať sponzorstvo zo strany Microsoftu. Akékoľvek použitie ochranných známok alebo log tretích strán podlieha pravidlám týchto tretích strán.

## Získanie pomoci

Ak sa zaseknete alebo máte otázky ohľadom tvorby AI aplikácií, pridajte sa do:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Ak máte spätnú väzbu k produktu alebo narazíte na chyby pri vývoji, navštívte:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Vyhlásenie o vylúčení zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj by sa mal považovať pôvodný dokument v jeho pôvodnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.