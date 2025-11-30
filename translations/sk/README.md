<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T12:13:16+00:00",
  "source_file": "README.md",
  "language_code": "sk"
}
-->
# Co-op Translator

_Ľahko automatizujte preklad vášho vzdelávacieho obsahu na GitHube do viacerých jazykov a oslovte tak globálne publikum._

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

#### Podporované [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabčina](../ar/README.md) | [Bengálčina](../bn/README.md) | [Bulharčina](../bg/README.md) | [Barmčina (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh/README.md) | [Čínština (tradičná, Hongkong)](../hk/README.md) | [Čínština (tradičná, Macau)](../mo/README.md) | [Čínština (tradičná, Taiwan)](../tw/README.md) | [Chorvátčina](../hr/README.md) | [Čeština](../cs/README.md) | [Dánčina](../da/README.md) | [Holandčina](../nl/README.md) | [Estónčina](../et/README.md) | [Fínčina](../fi/README.md) | [Francúzština](../fr/README.md) | [Nemčina](../de/README.md) | [Gréčtina](../el/README.md) | [Hebrejčina](../he/README.md) | [Hindčina](../hi/README.md) | [Maďarčina](../hu/README.md) | [Indonézština](../id/README.md) | [Taliančina](../it/README.md) | [Japončina](../ja/README.md) | [Kannadčina](../kn/README.md) | [Kórejčina](../ko/README.md) | [Litovčina](../lt/README.md) | [Malajčina](../ms/README.md) | [Malajálamčina](../ml/README.md) | [Maráthčina](../mr/README.md) | [Nepálčina](../ne/README.md) | [Nigérijská pidžinčina](../pcm/README.md) | [Nórčina](../no/README.md) | [Perzština (Farsi)](../fa/README.md) | [Poľština](../pl/README.md) | [Portugalčina (Brazília)](../br/README.md) | [Portugalčina (Portugalsko)](../pt/README.md) | [Pandžábčina (Gurmukhi)](../pa/README.md) | [Rumunčina](../ro/README.md) | [Ruština](../ru/README.md) | [Srbčina (cyrilika)](../sr/README.md) | [Slovenčina](./README.md) | [Slovinčina](../sl/README.md) | [Španielčina](../es/README.md) | [Svahilčina](../sw/README.md) | [Švédčina](../sv/README.md) | [Tagalog (Filipínčina)](../tl/README.md) | [Tamilčina](../ta/README.md) | [Telugčina](../te/README.md) | [Thajčina](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinčina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamčina](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Prehľad

**Co-op Translator** vám pomáha jednoducho lokalizovať váš vzdelávací obsah na GitHube do viacerých jazykov.
Keď aktualizujete svoje Markdown súbory, obrázky alebo notebooky, preklady sa automaticky synchronizujú, čím zabezpečujú, že váš obsah zostane presný a aktuálny pre študentov po celom svete.

Príklad, ako je preložený obsah usporiadaný:

![Príklad](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.sk.png)

## Rýchly štart

```bash
# Vytvorte a aktivujte virtuálne prostredie (odporúčané)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Nainštalujte balík
pip install co-op-translator
# Preložiť
translate -l "ko ja fr" -md
```

Docker:

```bash
# Stiahnite verejný obraz z GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Spustite s pripojenou aktuálnou zložkou a poskytnutým .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimálne nastavenie

1. Vytvorte súbor `.env` podľa šablóny: [.env.template](../../.env.template)
2. Nakonfigurujte jedného poskytovateľa LLM (Azure OpenAI alebo OpenAI)
3. (Voliteľné) Pre preklad obrázkov (`-img`) nastavte Azure AI Vision
4. (Odporúčané) Vyčistite predchádzajúce preklady, aby ste predišli konfliktom (napr. `translations/`)
5. (Odporúčané) Pridajte sekciu pre preklady do vášho README pomocou [README languages template](./getting_started/README_languages_template.md)
6. Pozrite si: [Nastavenie Azure AI](./getting_started/set-up-azure-ai.md)

## Použitie

Preložte všetky podporované typy:

```bash
translate -l "ko ja"
```

Iba Markdown:

```bash
translate -l "de" -md
```

Markdown + obrázky:

```bash
translate -l "pt" -md -img
```

Iba notebooky:

```bash
translate -l "zh" -nb
```

Viac príznakov: [Referenčný manuál príkazov](./getting_started/command-reference.md)

## Funkcie

- Automatický preklad Markdown, notebookov a obrázkov
- Udržiava preklady synchronizované so zdrojovými zmenami
- Funguje lokálne (CLI) alebo v CI (GitHub Actions)
- Používa Azure OpenAI alebo OpenAI; voliteľne Azure AI Vision pre obrázky
- Zachováva formátovanie a štruktúru Markdown

## Dokumentácia

- [Príručka príkazového riadku](./getting_started/command-line-guide/command-line-guide.md)
- [Príručka GitHub Actions (verejné repozitáre a štandardné tajomstvá)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Príručka GitHub Actions (Microsoft organizácie a nastavenia na úrovni organizácie)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Šablóna jazykov README](./getting_started/README_languages_template.md)
- [Podporované jazyky](./getting_started/supported-languages.md)
- [Príspevky](./CONTRIBUTING.md)
- [Riešenie problémov](./getting_started/troubleshooting.md)

### Microsoft špecifický sprievodca
> [!NOTE]
> Len pre správcov repozitárov Microsoft „Pre začiatočníkov“.

- [Aktualizácia zoznamu „iných kurzov“ (len pre MS Beginners repozitáre)](./getting_started/update-other-courses.md)

## Podporte nás a podporte globálne vzdelávanie

Pridajte sa k nám v revolúcii zdieľania vzdelávacieho obsahu po celom svete! Dajte [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHube a podporte našu misiu prekonávať jazykové bariéry vo vzdelávaní a technológiách. Váš záujem a príspevky majú veľký význam! Kódové príspevky a návrhy funkcií sú vždy vítané.

### Preskúmajte vzdelávací obsah Microsoftu vo vašom jazyku

- [AZD pre začiatočníkov](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI pre začiatočníkov](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) pre začiatočníkov](https://github.com/microsoft/mcp-for-beginners)
- [AI Agenti pre začiatočníkov](https://github.com/microsoft/ai-agents-for-beginners)
- [Generatívna AI pre začiatočníkov pomocou .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generatívna AI pre začiatočníkov](https://github.com/microsoft/generative-ai-for-beginners)
- [Generatívna AI pre začiatočníkov pomocou Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [Strojové učenie pre začiatočníkov](https://aka.ms/ml-beginners)
- [Dátová veda pre začiatočníkov](https://aka.ms/datascience-beginners)
- [AI pre začiatočníkov](https://aka.ms/ai-beginners)
- [Kybernetická bezpečnosť pre začiatočníkov](https://github.com/microsoft/Security-101)
- [Webový vývoj pre začiatočníkov](https://aka.ms/webdev-beginners)
- [IoT pre začiatočníkov](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video prezentácie

👉 Kliknite na obrázok nižšie pre sledovanie na YouTube.

- **Open at Microsoft**: Krátka 18-minútová úvodná prezentácia a rýchly návod, ako používať Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.sk.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Príspevky

Tento projekt vítá príspevky a návrhy. Máte záujem prispieť do Azure Co-op Translator? Pozrite si prosím náš [CONTRIBUTING.md](./CONTRIBUTING.md) pre pokyny, ako môžete pomôcť sprístupniť Co-op Translator širšiemu publiku.

## Prispievatelia

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kód správania

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Pre viac informácií si pozrite [Často kladené otázky o Kóde správania](https://opensource.microsoft.com/codeofconduct/faq/) alebo
kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s akýmikoľvek ďalšími otázkami či pripomienkami.

## Zodpovedná AI

Microsoft sa zaväzuje pomáhať svojim zákazníkom používať naše AI produkty zodpovedne, zdieľať naše poznatky a budovať dôveru prostredníctvom nástrojov ako Transparency Notes a Impact Assessments. Mnohé z týchto zdrojov nájdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Prístup Microsoftu k zodpovednej AI je založený na princípoch spravodlivosti, spoľahlivosti a bezpečnosti, ochrany súkromia a bezpečnosti, inkluzívnosti, transparentnosti a zodpovednosti.

Veľké modely pre spracovanie prirodzeného jazyka, obrázkov a reči – ako tie použité v tomto príklade – môžu potenciálne vykazovať správanie, ktoré je nespravodlivé, nespoľahlivé alebo urážlivé, čo môže viesť k škodám. Prosím, prečítajte si [Transparency note služby Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby ste boli informovaní o rizikách a obmedzeniach.
Odporúčaným prístupom na zmiernenie týchto rizík je zahrnúť do vašej architektúry bezpečnostný systém, ktorý dokáže detegovať a zabrániť škodlivému správaniu. <a href="https://learn.microsoft.com/azure/ai-services/content-safety/overview">Azure AI Content Safety</a> poskytuje nezávislú ochrannú vrstvu, schopnú detegovať škodlivý obsah vytvorený používateľmi aj AI v aplikáciách a službách. Azure AI Content Safety zahŕňa textové a obrazové API, ktoré vám umožňujú detegovať škodlivý materiál. Máme tiež interaktívne Content Safety Studio, ktoré vám umožňuje prezerať, skúmať a vyskúšať ukážkový kód na detekciu škodlivého obsahu v rôznych modalitách. Nasledujúca <a href="https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest">rýchla príručka</a> vás prevedie vytváraním požiadaviek na službu.

Ďalším aspektom, ktorý treba zvážiť, je celkový výkon aplikácie. Pri multimodálnych a multimodelových aplikáciách považujeme výkon za to, že systém funguje tak, ako vy a vaši používatelia očakávate, vrátane toho, že nevytvára škodlivé výstupy. Je dôležité vyhodnotiť výkon vašej celkovej aplikácie pomocou <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in">metrik kvality generovania a rizika a bezpečnosti</a>.

Vašu AI aplikáciu môžete vyhodnotiť vo vašom vývojovom prostredí pomocou <a href="https://microsoft.github.io/promptflow/index.html">prompt flow SDK</a>. Na základe testovacej dátovej sady alebo cieľa sú generácie vašej generatívnej AI aplikácie kvantitatívne merané pomocou vstavaných alebo vlastných hodnotiteľov podľa vášho výberu. Ak chcete začať s prompt flow SDK na vyhodnotenie vášho systému, môžete sledovať <a href="https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk">rýchlu príručku</a>. Po vykonaní hodnotiaceho behu môžete <a href="https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results">vizualizovať výsledky v Azure AI Studio</a>.

## Ochranné známky

Tento projekt môže obsahovať ochranné známky alebo logá projektov, produktov alebo služieb. Autorizované používanie ochranných známok alebo log Microsoftu podlieha a musí dodržiavať <a href="https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general">Pravidlá používania ochranných známok a značiek Microsoftu</a>. Použitie ochranných známok alebo log Microsoftu v upravených verziách tohto projektu nesmie spôsobovať zmätok ani naznačovať sponzorstvo Microsoftom. Akékoľvek použitie ochranných známok alebo log tretích strán podlieha pravidlám týchto tretích strán.

## Získanie pomoci

Ak sa zaseknete alebo máte otázky ohľadom tvorby AI aplikácií, pripojte sa:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ak máte spätnú väzbu k produktu alebo narazíte na chyby počas vývoja, navštívte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->